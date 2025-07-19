#!/usr/bin/env python3
"""
Context Management Hook for Claude Code
Automatically saves and manages context state
Replaces manual /context command
"""

import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared import HookBase, ToolHook, SettingsManager, StateManager, MessageFormatter


class ContextManagementHook(ToolHook):
    """Automatically manages context state across operations"""
    
    def __init__(self):
        super().__init__()
        
        # Paths
        self.settings_path = self.claude_path / "logic" / "context" / "context-settings.json"
        self.context_path = self.claude_path / "project" / "sessions" / "context.json"
        self.state_path = self.claude_path / "project" / "state" / "context-state.json"
        
        # Managers
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        self.state = StateManager(self.state_path, self._get_default_state())
        
        # Context tracking
        self.current_context = self._load_context()
        self.operations_since_save = 0
        self.last_save_time = time.time()
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "enabled": True,
            "auto_save_interval": 300,  # 5 minutes
            "auto_save_operations": 10,  # Save after N operations
            "track_file_context": True,
            "track_command_history": True,
            "track_memory_references": True,
            "max_context_size": 50,  # Max items per category
            "checkpoint_enabled": True,
            "checkpoint_interval": 3600  # 1 hour
        }
    
    def _get_default_state(self) -> Dict[str, Any]:
        """Get default state"""
        return {
            "last_save": time.time(),
            "operations_count": 0,
            "last_checkpoint": time.time(),
            "total_saves": 0
        }
    
    def _get_default_context(self) -> Dict[str, Any]:
        """Get default context structure"""
        return {
            "session_id": f"context-{int(time.time())}",
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat(),
            "working_files": [],  # Recently accessed files
            "active_tasks": [],  # Current TodoWrite tasks
            "command_history": [],  # Recent commands
            "memory_references": [],  # Referenced memories
            "key_decisions": [],  # Important decisions made
            "error_patterns": [],  # Recent errors encountered
            "metadata": {
                "project": str(self.project_root),
                "mode": "auto",  # Current mode
                "agent_id": "main"
            }
        }
    
    def _load_context(self) -> Dict[str, Any]:
        """Load existing context or create new"""
        if self.context_path.exists():
            try:
                with open(self.context_path, 'r') as f:
                    return json.load(f)
            except:
                pass
        return self._get_default_context()
    
    def _save_context(self):
        """Save current context to file"""
        self.context_path.parent.mkdir(parents=True, exist_ok=True)
        self.current_context["updated"] = datetime.now().isoformat()
        
        with open(self.context_path, 'w') as f:
            json.dump(self.current_context, f, indent=2)
        
        # Update state
        self.state.update({
            "last_save": time.time(),
            "operations_count": 0,
            "total_saves": self.state.get("total_saves", 0) + 1
        })
        
        self.operations_since_save = 0
        self.last_save_time = time.time()
    
    def process_tool_use(self, tool_name: str, tool_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process tool use and update context"""
        if not self.settings.get("enabled"):
            return 0, None
        
        # Track operation
        self.operations_since_save += 1
        self.state.increment("operations_count")
        
        # Update context based on tool
        if self.settings.get("track_file_context"):
            self._track_file_operations(tool_name, tool_input)
        
        if self.settings.get("track_command_history"):
            self._track_commands(tool_name, tool_input)
        
        # Check if we should auto-save
        should_save = False
        save_reason = ""
        
        # Check operation count
        if self.operations_since_save >= self.settings.get("auto_save_operations", 10):
            should_save = True
            save_reason = f"Reached {self.operations_since_save} operations"
        
        # Check time interval
        time_since_save = time.time() - self.last_save_time
        if time_since_save >= self.settings.get("auto_save_interval", 300):
            should_save = True
            save_reason = f"Auto-save after {int(time_since_save/60)} minutes"
        
        # Check for checkpoint
        if self.settings.get("checkpoint_enabled"):
            time_since_checkpoint = time.time() - self.state.get("last_checkpoint", 0)
            if time_since_checkpoint >= self.settings.get("checkpoint_interval", 3600):
                self._create_checkpoint()
                save_reason = "Created hourly checkpoint"
        
        # Save if needed
        if should_save:
            self._save_context()
            return 0, self._generate_save_notification(save_reason)
        
        return 0, None
    
    def _track_file_operations(self, tool_name: str, tool_input: Dict[str, Any]):
        """Track file-related operations"""
        file_path = None
        
        if tool_name in ["Read", "Edit", "Write", "MultiEdit"]:
            file_path = tool_input.get("file_path")
        elif tool_name == "Grep":
            file_path = tool_input.get("path", ".")
        
        if file_path and file_path != ".":
            # Add to working files
            working_files = self.current_context.get("working_files", [])
            
            # Create file entry
            file_entry = {
                "path": file_path,
                "last_accessed": datetime.now().isoformat(),
                "operation": tool_name,
                "access_count": 1
            }
            
            # Check if already tracked
            existing = next((f for f in working_files if f["path"] == file_path), None)
            if existing:
                existing["last_accessed"] = file_entry["last_accessed"]
                existing["access_count"] += 1
            else:
                working_files.append(file_entry)
            
            # Limit size
            max_size = self.settings.get("max_context_size", 50)
            if len(working_files) > max_size:
                # Keep most recently accessed
                working_files.sort(key=lambda x: x["last_accessed"], reverse=True)
                self.current_context["working_files"] = working_files[:max_size]
            else:
                self.current_context["working_files"] = working_files
    
    def _track_commands(self, tool_name: str, tool_input: Dict[str, Any]):
        """Track command execution"""
        if tool_name == "Bash":
            command = tool_input.get("command", "")
            if command:
                command_entry = {
                    "command": command[:200],  # Truncate long commands
                    "timestamp": datetime.now().isoformat(),
                    "tool": tool_name
                }
                
                history = self.current_context.get("command_history", [])
                history.append(command_entry)
                
                # Limit size
                max_size = self.settings.get("max_context_size", 50)
                if len(history) > max_size:
                    self.current_context["command_history"] = history[-max_size:]
                else:
                    self.current_context["command_history"] = history
    
    def _create_checkpoint(self):
        """Create a context checkpoint"""
        checkpoint_path = self.context_path.parent / "checkpoints" / f"context-{int(time.time())}.json"
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save checkpoint
        with open(checkpoint_path, 'w') as f:
            json.dump(self.current_context, f, indent=2)
        
        # Update state
        self.state.update({"last_checkpoint": time.time()})
        
        # Clean old checkpoints (keep last 5)
        checkpoints = sorted(checkpoint_path.parent.glob("context-*.json"))
        if len(checkpoints) > 5:
            for old_checkpoint in checkpoints[:-5]:
                old_checkpoint.unlink()
    
    def _generate_save_notification(self, reason: str) -> str:
        """Generate context save notification"""
        stats = {
            "files": len(self.current_context.get("working_files", [])),
            "commands": len(self.current_context.get("command_history", [])),
            "saves": self.state.get("total_saves", 0)
        }
        
        return f"""
💾 **Context Auto-Saved**
Reason: {reason}
Tracking: {stats['files']} files, {stats['commands']} commands
Total saves this session: {stats['saves']}"""
    
    def get_context_summary(self) -> Dict[str, Any]:
        """Get context summary for manual inspection"""
        return {
            "session_id": self.current_context.get("session_id"),
            "duration": int((time.time() - self.last_save_time) / 60),  # minutes
            "working_files": len(self.current_context.get("working_files", [])),
            "recent_files": [f["path"] for f in self.current_context.get("working_files", [])[:5]],
            "command_count": len(self.current_context.get("command_history", [])),
            "last_save": datetime.fromtimestamp(self.last_save_time).isoformat(),
            "operations_since_save": self.operations_since_save
        }
    
    def refresh_context(self):
        """Manually refresh context (for /context refresh command)"""
        self._save_context()
        return self.get_context_summary()


if __name__ == "__main__":
    hook = ContextManagementHook()
    hook.run()