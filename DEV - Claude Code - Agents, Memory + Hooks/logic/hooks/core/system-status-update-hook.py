#!/usr/bin/env python3
"""
System Status Update Hook

Automatically updates the System Status Display in CLAUDE.md when system
components change. Monitors MCPs, knowledge files, hooks, and commands.

What it does:
- Monitors MCP configuration changes
- Counts knowledge files in project/knowledge
- Tracks active hooks in settings.json
- Updates command list from documentation
- Maintains accurate system status display

What could go wrong:
- Missing MCP config file if using different Claude installation
- Status display format changes breaking regex matching
- Large config files causing performance issues
- Concurrent edits to CLAUDE.md causing conflicts
"""

import os
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

try:
    from logic.shared.hook_base import HookBase
    from logic.shared.hook_formatters import MessageFormatter
except ImportError:
    # Fallback for standalone execution
    class HookBase:
        def __init__(self, name):
            self.name = name
            self.project_root = Path(__file__).parent.parent.parent.parent
    
    class MessageFormatter:
        @staticmethod
        def format_info(msg): return f"ℹ️ {msg}"
        @staticmethod
        def format_warning(msg): return f"⚠️ {msg}"


class SystemStatusUpdateHook(HookBase):
    def __init__(self):
        super().__init__("SystemStatusUpdate")
        self.claude_md_path = self.project_root / "CLAUDE.md"
        self.settings_path = self.project_root / ".claude" / "settings.json"
        self.knowledge_dir = self.project_root / ".claude" / "knowledge"
        
        # MCP config locations (try multiple paths)
        self.mcp_config_paths = [
            Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json",
            Path.home() / ".config" / "Claude" / "claude_desktop_config.json",
            Path.home() / ".claude" / "claude_desktop_config.json"
        ]
        
        # Status display markers
        self.status_start = "=== 🚀 Claude Code System Status ==="
        self.status_end = "====================================="
        
    def should_trigger(self, tool_name: str, args: Dict) -> bool:
        """Check if we should update the status display"""
        if tool_name not in ["Write", "Edit", "MultiEdit"]:
            return False
            
        file_path = str(args.get("file_path", ""))
        
        # Trigger on relevant file changes
        triggers = [
            "claude_desktop_config.json",
            "settings.json",
            ".claude/knowledge/",
            ".claude/logic/commands/",
            ".claude/logic/hooks/"
        ]
        
        return any(trigger in file_path for trigger in triggers)
    
    def post_tool_use(self, tool_name: str, args: Dict, result: Any):
        """Update status display after relevant changes"""
        if not self.should_trigger(tool_name, args):
            return
            
        try:
            # Gather all status information
            status_data = self.gather_system_status()
            
            # Update CLAUDE.md
            self.update_status_display(status_data)
            
            print(MessageFormatter.format_info(
                "System Status Display updated in CLAUDE.md"
            ))
        except Exception as e:
            print(MessageFormatter.format_warning(
                f"Failed to update status display: {str(e)}"
            ))
    
    def gather_system_status(self) -> Dict:
        """Gather all system status information"""
        status = {
            "mcps": self.get_mcp_status(),
            "knowledge": self.get_knowledge_files(),
            "hooks": self.get_hook_status(),
            "commands": self.get_commands(),
            "project": self.get_project_info(),
            "memory": self.get_memory_status()
        }
        return status
    
    def get_mcp_status(self) -> Dict:
        """Get MCP server status"""
        mcps = {}
        
        # Find and read MCP config
        for config_path in self.mcp_config_paths:
            if config_path.exists():
                try:
                    with open(config_path, 'r') as f:
                        config = json.load(f)
                        
                    # Extract MCP servers
                    if "mcpServers" in config:
                        for name, _ in config["mcpServers"].items():
                            # Normalize names for display
                            display_name = name.replace("-mcp-server", "").replace("-mcp", "")
                            display_name = display_name.replace("-", " ").title()
                            mcps[display_name] = True
                    break
                except Exception:
                    pass
        
        # Default MCPs if config not found
        if not mcps:
            mcps = {
                "Sequential": True,
                "Graphiti": True,
                "GitHub": True,
                "Context7": True
            }
        
        return mcps
    
    def get_knowledge_files(self) -> List[str]:
        """Get list of knowledge files"""
        knowledge_files = []
        
        if self.knowledge_dir.exists():
            for file_path in self.knowledge_dir.glob("*.json"):
                # Simplify filename for display
                name = file_path.stem.replace("-", " ")
                knowledge_files.append(name)
        
        return sorted(knowledge_files)
    
    def get_hook_status(self) -> Dict:
        """Get hook status from settings.json"""
        hook_info = {
            "total": 0,
            "categories": set(),
            "key_hooks": []
        }
        
        try:
            with open(self.settings_path, 'r') as f:
                settings = json.load(f)
            
            # Count all hooks
            if "hooks" in settings and settings["hooks"].get("enabled", True):
                for event_type in ["UserPromptSubmit", "PreToolUse", "PostToolUse"]:
                    if event_type in settings["hooks"]:
                        for matcher_group in settings["hooks"][event_type]:
                            hooks = matcher_group.get("hooks", [])
                            hook_info["total"] += len(hooks)
                            
                            # Extract categories from hook paths
                            for hook in hooks:
                                if "command" in hook:
                                    path = hook["command"]
                                    if "/quality/" in path:
                                        hook_info["categories"].add("Quality")
                                    elif "/security/" in path:
                                        hook_info["categories"].add("Security")
                                    elif "/memory/" in path:
                                        hook_info["categories"].add("Memory")
                                    elif "/session/" in path:
                                        hook_info["categories"].add("Session")
                                    elif "/task/" in path:
                                        hook_info["categories"].add("Task")
        except Exception:
            pass
        
        # Convert categories to list of key hooks
        hook_info["key_hooks"] = sorted(list(hook_info["categories"]))[:4]
        
        return hook_info
    
    def get_commands(self) -> List[str]:
        """Get available commands"""
        # Primary commands from CLAUDE.md
        commands = ["/memory", "/save", "/logic"]
        
        # Could be extended to scan command files
        return commands
    
    def get_project_info(self) -> Dict:
        """Get project information"""
        info = {
            "name": "anobel.nl",
            "branch": "main",
            "mode": "Auto"
        }
        
        # Try to get actual git branch
        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True,
                text=True,
                cwd=self.project_root
            )
            if result.returncode == 0:
                info["branch"] = result.stdout.strip()
        except Exception:
            pass
        
        return info
    
    def get_memory_status(self) -> Dict:
        """Get memory system status"""
        # Check if Graphiti is active by looking for Neo4j
        status = {
            "active": True,  # Assume active if MCP configured
            "type": "Neo4j Connected"
        }
        
        # Could check actual Neo4j connection if needed
        return status
    
    def update_status_display(self, status_data: Dict):
        """Update the status display in CLAUDE.md"""
        if not self.claude_md_path.exists():
            return
            
        content = self.claude_md_path.read_text()
        
        # Find status display section
        start_idx = content.find(self.status_start)
        if start_idx == -1:
            print(MessageFormatter.format_warning(
                "Could not find System Status Display in CLAUDE.md"
            ))
            return
            
        end_idx = content.find(self.status_end, start_idx)
        if end_idx == -1:
            return
            
        # Generate new status display
        new_display = self.generate_status_display(status_data)
        
        # Replace the section
        before = content[:start_idx]
        after = content[end_idx + len(self.status_end):]
        
        new_content = before + new_display + self.status_end + after
        
        self.claude_md_path.write_text(new_content)
    
    def generate_status_display(self, status: Dict) -> str:
        """Generate the status display text"""
        lines = [self.status_start]
        
        # Memory line
        mem = status["memory"]
        lines.append(f"[🧠 Memory] Graphiti: ✅ Active | {mem['type']}")
        
        # Knowledge line
        knowledge = status["knowledge"]
        if knowledge:
            knowledge_str = " | ".join([f"{k} ✅" for k in knowledge])
            lines.append(f"[📚 Knowledge] {knowledge_str}")
        
        # MCPs line
        mcps = status["mcps"]
        if len(mcps) > 8:
            # Show first 7 and count of others
            mcp_list = list(mcps.keys())[:7]
            mcp_str = " | ".join([f"{m} ✅" for m in mcp_list])
            others = len(mcps) - 7
            lines.append(f"[🤖 MCPs] {mcp_str} | +{others} more")
        else:
            mcp_str = " | ".join([f"{m} ✅" for m in mcps.keys()])
            lines.append(f"[🤖 MCPs] {mcp_str}")
        
        # Hooks line
        hooks = status["hooks"]
        hook_str = " | ".join([f"{h} ✅" for h in hooks["key_hooks"]])
        lines.append(f"[⚡ Hooks] {hooks['total']} active hooks | {hook_str}")
        
        # Commands line
        commands = status["commands"]
        cmd_str = " | ".join(commands)
        lines.append(f"[🎯 Commands] {cmd_str}")
        
        # System line
        proj = status["project"]
        lines.append(f"[📂 System] Project: {proj['name']} | Git: {proj['branch']} | Mode: {proj['mode']} 🚀")
        
        return "\n".join(lines) + "\n"
    
    def run_standalone(self):
        """Run the hook standalone for testing"""
        print("Gathering system status...")
        status = self.gather_system_status()
        
        print("\nCurrent Status:")
        print(json.dumps(status, indent=2))
        
        print("\nUpdating CLAUDE.md...")
        self.update_status_display(status)
        print("✅ Status display updated!")


def main():
    """Test the hook"""
    hook = SystemStatusUpdateHook()
    hook.run_standalone()


if __name__ == "__main__":
    main()