#!/usr/bin/env python3
"""
Config Sync Hook

Automatically updates config.json when commands change in the system.
Monitors command files and CLAUDE.md for changes to keep config.json in sync.

What could go wrong:
- Hook might miss command changes in non-standard locations
- Could create invalid JSON if sync fails
- Manual config.json edits might be overwritten
- Race conditions if multiple updates happen simultaneously

Author: Claude
Date: 2025-01-22
"""

import json
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any
from datetime import datetime

# Add parent directories to path for imports
hooks_path = Path(__file__).resolve().parent
logic_path = hooks_path.parent
claude_path = logic_path.parent
sys.path.insert(0, str(claude_path))

from logic.shared import ToolHook

class ConfigSyncHook(ToolHook):
    """Sync config.json with actual command implementations"""
    
    def __init__(self):
        super().__init__()
        self.config_path = self.claude_path / "config.json"
        self.commands_dir = self.claude_path / "logic" / "commands"
        self.claude_md_path = self.project_root / "CLAUDE.md"
        
        # Files that trigger sync
        self.trigger_files = [
            "CLAUDE.md",
            "logic.py",
            "memory-command.py",
            "status-command.py"
        ]
        
        # Tools that trigger sync
        self.relevant_tools = ["edit_file", "write_file", "str_replace"]
        
    def _should_sync(self, file_path: str) -> bool:
        """Check if file change should trigger config sync"""
        # Check if it's a trigger file
        file_name = Path(file_path).name
        if file_name in self.trigger_files:
            return True
            
        # Check if it's in commands directory
        if ".claude/logic/commands/" in file_path and file_path.endswith(".py"):
            return True
            
        return False
    
    def _extract_commands_from_claude_md(self) -> Dict[str, str]:
        """Extract current commands from CLAUDE.md"""
        commands = {}
        
        if not self.claude_md_path.exists():
            return commands
            
        try:
            with open(self.claude_md_path, 'r') as f:
                content = f.read()
                
            # Look for command definitions in Essential Commands section
            commands_section = re.search(
                r'### Essential Commands.*?```bash(.*?)```',
                content,
                re.DOTALL
            )
            
            if commands_section:
                lines = commands_section.group(1).strip().split('\n')
                for line in lines:
                    # Parse lines like: /memory [search|manual|auto]  # Knowledge management
                    match = re.match(r'^(/\w+)(?:\s+\[([^\]]+)\])?\s*#\s*(.+)$', line.strip())
                    if match:
                        cmd = match.group(1)
                        options = match.group(2) or ""
                        desc = match.group(3)
                        commands[cmd] = f"{desc} ({options})" if options else desc
                        
        except Exception as e:
            print(f"Error extracting commands from CLAUDE.md: {e}")
            
        return commands
    
    def _extract_subcommands_from_logic(self) -> Dict[str, List[str]]:
        """Extract subcommands from logic.py"""
        subcommands = {}
        logic_file = self.commands_dir / "logic.py"
        
        if not logic_file.exists():
            return subcommands
            
        try:
            with open(logic_file, 'r') as f:
                content = f.read()
                
            # Find handlers dictionary
            handlers_match = re.search(
                r'handlers\s*=\s*{([^}]+)}',
                content,
                re.DOTALL
            )
            
            if handlers_match:
                handlers = handlers_match.group(1)
                # Extract handler names
                handler_names = re.findall(r'"([\w-]+)":', handlers)
                subcommands["/logic"] = handler_names
                
        except Exception as e:
            print(f"Error extracting subcommands: {e}")
            
        return subcommands
    
    def _update_config(self, commands: Dict[str, str], subcommands: Dict[str, List[str]]) -> bool:
        """Update config.json with current commands"""
        try:
            # Read current config
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            
            # Update command whitelist
            config["settings"]["command_whitelist"] = [cmd.lstrip("/") for cmd in commands.keys()]
            
            # Update current commands section
            config["current_commands"] = {}
            for cmd, desc in commands.items():
                if cmd in subcommands:
                    subs = ", ".join(subcommands[cmd])
                    config["current_commands"][cmd] = f"{desc} - Subcommands: {subs}"
                else:
                    config["current_commands"][cmd] = desc
            
            # Update command sync metadata
            if "command_sync" not in config:
                config["command_sync"] = {}
            config["command_sync"]["last_sync"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            config["command_sync"]["sync_enabled"] = True
            config["command_sync"]["_comment"] = "Auto-updated by config-sync-hook.py when commands change"
            
            # Update aliases if needed
            if "aliases" in config and "commands" in config["aliases"]:
                # Remove aliases for deprecated commands
                valid_commands = set(commands.keys())
                config["aliases"]["commands"] = {
                    alias: cmd for alias, cmd in config["aliases"]["commands"].items()
                    if cmd in valid_commands
                }
            
            # Write updated config
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
                
            return True
            
        except Exception as e:
            print(f"Error updating config: {e}")
            return False
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook input for file edits"""
        tool_name, tool_input = self.get_tool_info()
        
        # Only process relevant tools
        if not self.is_relevant_tool(self.relevant_tools):
            return 0, None
            
        # Extract file path from tool input
        file_path = None
        if tool_name == "edit_file":
            file_path = tool_input.get("path", "")
        elif tool_name == "write_file":
            file_path = tool_input.get("path", "")
        elif tool_name == "str_replace":
            file_path = tool_input.get("path", "")
            
        if not file_path:
            return 0, None
            
        # Don't sync if we're editing config.json itself
        if "config.json" in file_path:
            return 0, None
            
        if not self._should_sync(file_path):
            return 0, None
        
        # Extract current commands
        commands = self._extract_commands_from_claude_md()
        subcommands = self._extract_subcommands_from_logic()
        
        # If we found commands, update config
        if commands:
            if self._update_config(commands, subcommands):
                message = "⚙️ **Config Sync**\n\n"
                message += "Updated config.json with current commands:\n"
                message += "\n".join([f"  • {cmd}" for cmd in commands.keys()])
                return 0, message
            else:
                return 1, "⚙️ **Config Sync Failed**\n\nFailed to update config.json. Check the file manually."
                
        return 0, None
    
    def run(self):
        """Main entry point for hook execution"""
        try:
            hook_input = self.read_input()
            exit_code, output = self.process(hook_input)
            
            if output:
                print(output)
                
            sys.exit(exit_code)
        except Exception as e:
            self.error_exit(f"Hook execution failed: {e}")


if __name__ == "__main__":
    hook = ConfigSyncHook()
    hook.run()