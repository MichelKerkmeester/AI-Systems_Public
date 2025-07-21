#!/usr/bin/env python3
"""
Mode Management System for Claude Code
Handles mode state, suggestions, and command adaptations
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, Optional, Tuple, List

class ModeManager:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.state_file = os.path.join(self.base_dir, "logic", "state", "mode-state.json")
        self.config_file = os.path.join(self.base_dir, "..", "claude.config.json")
        self.state = self._load_state()
        self.config = self._load_config()
        
    def _load_state(self) -> Dict:
        """Load mode state from JSON file"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return self._default_state()
    
    def _load_config(self) -> Dict:
        """Load Claude configuration"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}
    
    def _default_state(self) -> Dict:
        """Return default mode state"""
        return {
            "current_mode": "auto",
            "suggested_mode": None,
            "suggestion_reason": None,
            "last_suggestion_time": None,
            "auto_suggest_enabled": True,
            "require_approval": True,
            "suggestion_accepted": True,
            "mode_history": [
                {
                    "mode": "auto",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "reason": "initial"
                }
            ],
            "mode_overrides": {
                "/test": "inherit",
                "/workflow": "inherit",
                "/context": "inherit",
                "/memory": "inherit",
                "/security": "strict"
            },
            "statistics": {
                "suggestions_made": 0,
                "suggestions_accepted": 0,
                "suggestions_rejected": 0,
                "manual_switches": 0
            }
        }
    
    def save_state(self):
        """Save current state to JSON file"""
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def analyze_query(self, query: str, context: Dict = None) -> Tuple[Optional[str], Optional[str]]:
        """
        Analyze a query to suggest appropriate mode
        Returns: (suggested_mode, reason)
        """
        if not self.state["auto_suggest_enabled"]:
            return None, None
            
        query_lower = query.lower()
        context = context or {}
        
        # Get mode detection patterns from config
        mode_detection = self.config.get("mode_detection", {})
        
        # Check for strict mode triggers
        strict_patterns = mode_detection.get("strict", {}).get("patterns", [])
        for pattern in strict_patterns:
            if pattern.lower() in query_lower:
                return "strict", f"Detected '{pattern}' in query"
        
        # Check branch-based triggers
        current_branch = context.get("git_branch", "")
        strict_branches = mode_detection.get("strict", {}).get("branches", [])
        if current_branch in strict_branches:
            return "strict", f"Working on {current_branch} branch"
        
        # Check for hybrid mode triggers
        hybrid_patterns = mode_detection.get("hybrid", {}).get("patterns", [])
        for pattern in hybrid_patterns:
            if pattern.lower() in query_lower:
                return "hybrid", f"Detected '{pattern}' in query"
        
        # Check file count
        file_count = context.get("modified_files", 0)
        hybrid_file_threshold = mode_detection.get("hybrid", {}).get("file_count", 10)
        if file_count >= hybrid_file_threshold:
            return "hybrid", f"{file_count} files modified"
        
        # Check for security-related queries
        security_keywords = ["security", "vulnerability", "exploit", "injection", "xss", "csrf"]
        if any(keyword in query_lower for keyword in security_keywords):
            return "strict", "Security-related query detected"
        
        # Check for testing queries
        test_keywords = ["test", "validate", "audit", "check", "verify"]
        if any(keyword in query_lower for keyword in test_keywords):
            current = self.state["current_mode"]
            if current == "auto":
                return "strict", "Testing operations benefit from strict validation"
        
        # Default: stay in current mode
        return None, None
    
    def suggest_mode(self, query: str, context: Dict = None) -> Dict:
        """
        Generate mode suggestion based on query
        Returns suggestion info dict
        """
        suggested_mode, reason = self.analyze_query(query, context)
        
        if suggested_mode and suggested_mode != self.state["current_mode"]:
            self.state["suggested_mode"] = suggested_mode
            self.state["suggestion_reason"] = reason
            self.state["last_suggestion_time"] = datetime.utcnow().isoformat() + "Z"
            self.state["suggestion_accepted"] = False
            self.state["statistics"]["suggestions_made"] += 1
            self.save_state()
            
            return {
                "current": self.state["current_mode"],
                "suggested": suggested_mode,
                "reason": reason,
                "require_approval": self.state["require_approval"]
            }
        
        return {
            "current": self.state["current_mode"],
            "suggested": None,
            "reason": None,
            "require_approval": False
        }
    
    def switch_mode(self, new_mode: str, reason: str = "manual", accepted: bool = True):
        """Switch to a new mode"""
        if new_mode not in ["strict", "auto", "hybrid"]:
            raise ValueError(f"Invalid mode: {new_mode}")
        
        old_mode = self.state["current_mode"]
        self.state["current_mode"] = new_mode
        self.state["suggested_mode"] = None
        self.state["suggestion_reason"] = None
        
        # Update history
        self.state["mode_history"].append({
            "mode": new_mode,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "reason": reason,
            "from_mode": old_mode
        })
        
        # Update statistics
        if reason == "manual":
            self.state["statistics"]["manual_switches"] += 1
        elif accepted:
            self.state["statistics"]["suggestions_accepted"] += 1
        
        # Update config file
        if self.config:
            self.config["current_mode"] = new_mode
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        
        self.save_state()
    
    def get_command_mode(self, command: str) -> str:
        """Get effective mode for a specific command"""
        override = self.state["mode_overrides"].get(command, "inherit")
        if override == "inherit":
            return self.state["current_mode"]
        return override
    
    def get_mode_config(self, mode: str = None) -> Dict:
        """Get configuration for a specific mode"""
        mode = mode or self.state["current_mode"]
        return self.config.get("modes", {}).get(mode, {})
    
    def get_available_commands(self, mode: str = None) -> List[str]:
        """Get commands available/recommended for current mode"""
        mode = mode or self.state["current_mode"]
        
        all_commands = [
            "/workflow", "/test", "/memory", "/mode", "/pr", 
            "/security", "/save", "/gemini", "/notebook", "/context"
        ]
        
        # In strict mode, recommend validation and security commands
        if mode == "strict":
            return ["/test", "/security", "/context", "/mode", "/save"]
        
        # In hybrid mode, balance between safety and features
        elif mode == "hybrid":
            return ["/workflow", "/test", "/context", "/memory", "/mode", "/save"]
        
        # In auto mode, all commands available
        return all_commands
    
    def format_mode_status(self) -> str:
        """Format current mode status for display"""
        mode = self.state["current_mode"]
        config = self.get_mode_config(mode)
        icon = config.get("icon", "")
        
        status = f"[{icon} Mode: {mode.capitalize()}"
        
        if self.state["suggested_mode"]:
            sug_config = self.get_mode_config(self.state["suggested_mode"])
            sug_icon = sug_config.get("icon", "")
            status += f" | Suggested: {sug_icon} {self.state['suggested_mode'].capitalize()}"
            if self.state["suggestion_reason"]:
                status += f" ({self.state['suggestion_reason']})"
        
        status += "]"
        
        # Add available commands
        commands = self.get_available_commands()
        if commands:
            cmd_str = " | ".join(commands[:5])  # Show first 5
            status += f"\n[Available: {cmd_str}]"
        
        return status
    
    def handle_mode_command(self, args: List[str]) -> str:
        """Handle /mode command with various subcommands"""
        if not args:
            # Show current status
            return self._format_detailed_status()
        
        subcommand = args[0].lower()
        
        if subcommand in ["strict", "auto", "hybrid"]:
            # Switch mode
            self.switch_mode(subcommand, reason="manual")
            return f"Switched to {subcommand} mode"
        
        elif subcommand == "suggest":
            # Force suggestion analysis
            if len(args) > 1:
                query = " ".join(args[1:])
                suggestion = self.suggest_mode(query)
                if suggestion["suggested"]:
                    return f"Suggested mode: {suggestion['suggested']} (Reason: {suggestion['reason']})"
                return "No mode change suggested for this query"
            return "Please provide a query to analyze"
        
        elif subcommand == "auto":
            # Toggle auto-suggestions
            if len(args) > 1 and args[1].lower() in ["on", "off"]:
                self.state["auto_suggest_enabled"] = args[1].lower() == "on"
                self.save_state()
                return f"Auto-suggestions {'enabled' if self.state['auto_suggest_enabled'] else 'disabled'}"
            return f"Auto-suggestions are {'enabled' if self.state['auto_suggest_enabled'] else 'disabled'}"
        
        elif subcommand == "manual":
            # Disable mode enforcement
            self.state["require_approval"] = False
            self.save_state()
            return "Mode enforcement disabled - suggestions will be informational only"
        
        elif subcommand == "status":
            # Detailed status report
            return self._format_detailed_status()
        
        else:
            return f"Unknown subcommand: {subcommand}"
    
    def _format_detailed_status(self) -> str:
        """Format detailed mode status report"""
        mode = self.state["current_mode"]
        config = self.get_mode_config(mode)
        stats = self.state["statistics"]
        
        report = f"""
🎯 Mode System Status
━━━━━━━━━━━━━━━━━━━━━
Current Mode: {config.get('icon', '')} {mode.capitalize()}
Auto-Suggest: {'✅ Enabled' if self.state['auto_suggest_enabled'] else '❌ Disabled'}
Require Approval: {'✅ Yes' if self.state['require_approval'] else '❌ No'}

Mode Configuration:
• Safe Guards: {config.get('safe_guards', 'standard')}
• Checkpoints: {config.get('checkpoint_frequency', 'smart')}
• Max Staleness: {config.get('max_staleness', 120)} points

Statistics:
• Suggestions Made: {stats['suggestions_made']}
• Accepted: {stats['suggestions_accepted']}
• Rejected: {stats['suggestions_rejected']}
• Manual Switches: {stats['manual_switches']}

Recent History:
"""
        # Add last 3 mode switches
        history = self.state["mode_history"][-3:]
        for entry in reversed(history):
            timestamp = entry.get("timestamp", "").split("T")[0]
            from_mode = entry.get("from_mode", "?")
            to_mode = entry.get("mode", "?")
            reason = entry.get("reason", "unknown")
            report += f"• {timestamp}: {from_mode} → {to_mode} ({reason})\n"
        
        return report.strip()


if __name__ == "__main__":
    # Test the mode manager
    manager = ModeManager()
    
    # Test query analysis
    test_queries = [
        "deploy to production",
        "fix a small bug",
        "refactor the entire codebase",
        "run security audit",
        "add a new feature"
    ]
    
    for query in test_queries:
        suggestion = manager.suggest_mode(query, {"git_branch": "main", "modified_files": 5})
        print(f"\nQuery: {query}")
        print(f"Suggestion: {suggestion}")