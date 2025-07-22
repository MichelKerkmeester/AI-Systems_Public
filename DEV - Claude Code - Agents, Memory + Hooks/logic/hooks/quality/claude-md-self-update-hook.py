#!/usr/bin/env python3
"""
Claude MD Self-Update Hook

Monitors system changes and suggests CLAUDE.md updates when significant changes occur.

What could go wrong:
- Hook might suggest updates too frequently
- Could miss subtle but important changes
- Manual updates might conflict with suggestions
- False positives from temporary changes

Author: Claude
Date: 2025-01-22
"""

import json
import os
import sys
import hashlib
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Set

# Add the project root to the Python path
project_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(project_root))

from claude_logic_shared.base_hook import BaseHook
from claude_logic_shared.message_formatter import MessageFormatter

class ClaudeMdSelfUpdateHook(BaseHook):
    """Monitor system changes and suggest CLAUDE.md updates"""
    
    def __init__(self):
        super().__init__("claude-md-self-update-hook", "file:write,file:edit,response")
        self.formatter = MessageFormatter()
        self.last_check_file = self.logic_dir / "system" / "claude_md_last_check.json"
        self.changes_file = self.logic_dir / "system" / "claude_md_changes.json"
        self.significant_paths = [
            ".claude/logic/hooks/",
            ".claude/logic/commands/",
            ".claude/logic/code_reuse/",
            ".claude/logic/memory/",
            ".claude/project-management/specs/"
        ]
        self.update_threshold = 5  # Number of significant changes before suggesting update
        
    def _is_significant_change(self, file_path: str) -> bool:
        """Check if a file change is significant enough to warrant CLAUDE.md update"""
        # Check if path is in significant directories
        for sig_path in self.significant_paths:
            if sig_path in file_path:
                # Filter out test files and temporary files
                if any(x in file_path for x in ["test_", ".tmp", ".backup", "__pycache__"]):
                    return False
                return True
        
        # Check for completed specs (indicates major feature completion)
        if "specs/" in file_path and "/completed/" in file_path:
            return True
            
        return False
    
    def _load_changes(self) -> Dict:
        """Load tracked changes"""
        if self.changes_file.exists():
            try:
                with open(self.changes_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"changes": [], "last_update": None}
    
    def _save_changes(self, changes: Dict):
        """Save tracked changes"""
        os.makedirs(self.changes_file.parent, exist_ok=True)
        with open(self.changes_file, 'w') as f:
            json.dump(changes, f, indent=2)
    
    def _check_last_update(self) -> bool:
        """Check if enough time has passed since last check"""
        if self.last_check_file.exists():
            try:
                with open(self.last_check_file, 'r') as f:
                    last_check = json.load(f)
                    last_time = datetime.fromisoformat(last_check["timestamp"])
                    # Only check once per day
                    if datetime.now() - last_time < timedelta(days=1):
                        return False
            except:
                pass
        return True
    
    def _update_last_check(self):
        """Update last check timestamp"""
        os.makedirs(self.last_check_file.parent, exist_ok=True)
        with open(self.last_check_file, 'w') as f:
            json.dump({"timestamp": datetime.now().isoformat()}, f)
    
    def _get_change_summary(self, changes: List[Dict]) -> str:
        """Generate a summary of changes"""
        categories = {
            "hooks": [],
            "commands": [],
            "code_reuse": [],
            "memory": [],
            "specs": []
        }
        
        for change in changes:
            file_path = change["file"]
            if "hooks/" in file_path:
                categories["hooks"].append(change)
            elif "commands/" in file_path:
                categories["commands"].append(change)
            elif "code_reuse/" in file_path:
                categories["code_reuse"].append(change)
            elif "memory/" in file_path:
                categories["memory"].append(change)
            elif "specs/" in file_path and "/completed/" in file_path:
                categories["specs"].append(change)
        
        summary = []
        if categories["hooks"]:
            summary.append(f"- {len(categories['hooks'])} hook changes")
        if categories["commands"]:
            summary.append(f"- {len(categories['commands'])} command changes")
        if categories["code_reuse"]:
            summary.append(f"- {len(categories['code_reuse'])} code reuse system changes")
        if categories["memory"]:
            summary.append(f"- {len(categories['memory'])} memory system changes")
        if categories["specs"]:
            summary.append(f"- {len(categories['specs'])} major features completed")
            
        return "\n".join(summary)
    
    def _should_suggest_update(self, operation: str, content: str) -> bool:
        """Check if we should suggest a CLAUDE.md update"""
        # Don't check too frequently
        if not self._check_last_update():
            return False
            
        # Check for manual trigger
        if operation == "response" and "/logic claude-md-update" in content:
            self._update_last_check()
            return True
            
        changes = self._load_changes()
        
        # Check if we have enough significant changes
        if len(changes["changes"]) >= self.update_threshold:
            self._update_last_check()
            return True
            
        return False
    
    def process(self, operation: str, content: str, metadata: Optional[Dict] = None) -> Optional[str]:
        """Process hook and track/suggest updates"""
        # Track file changes
        if operation in ["file:write", "file:edit"] and metadata and "file_path" in metadata:
            file_path = metadata["file_path"]
            
            # Don't track CLAUDE.md itself
            if "CLAUDE.md" in file_path:
                return None
                
            if self._is_significant_change(file_path):
                changes = self._load_changes()
                change_entry = {
                    "file": file_path,
                    "operation": operation,
                    "timestamp": datetime.now().isoformat(),
                    "description": self._get_change_description(file_path, operation)
                }
                changes["changes"].append(change_entry)
                self._save_changes(changes)
        
        # Check if we should suggest update
        if self._should_suggest_update(operation, content):
            changes = self._load_changes()
            if changes["changes"]:
                suggestion = self.formatter.format_section(
                    "📝 CLAUDE.md Update Suggested",
                    f"""System changes detected that may require CLAUDE.md updates:

{self._get_change_summary(changes['changes'])}

Total changes: {len(changes['changes'])}

To review and update CLAUDE.md:
1. Run: /logic claude-md-update
2. Review suggested changes
3. Apply updates to keep documentation current

Note: This suggestion appears once per day when threshold is reached.""",
                    style="info"
                )
                
                # Clear changes after suggesting
                changes["changes"] = []
                changes["last_update"] = datetime.now().isoformat()
                self._save_changes(changes)
                
                return suggestion
                
        return None
    
    def _get_change_description(self, file_path: str, operation: str) -> str:
        """Get a description of what changed"""
        file_name = Path(file_path).name
        
        if "hook" in file_name:
            return f"Hook {'created' if operation == 'file:write' else 'modified'}: {file_name}"
        elif file_path.endswith((".py", "")) and "commands/" in file_path:
            return f"Command {'created' if operation == 'file:write' else 'modified'}: {file_name}"
        elif "specs/" in file_path and "/completed/" in file_path:
            spec_name = Path(file_path).parent.parent.name
            return f"Feature completed: {spec_name}"
        else:
            return f"System file {'created' if operation == 'file:write' else 'modified'}"

# Hook registration
hook_instance = ClaudeMdSelfUpdateHook()

def process(operation: str, content: str, metadata: Optional[Dict] = None) -> Optional[str]:
    """Process function called by hook system"""
    return hook_instance.process(operation, content, metadata)

if __name__ == "__main__":
    # Test the hook
    print("Testing Claude MD Self-Update Hook...")
    
    # Test file change tracking
    result = process("file:write", "", {"file_path": ".claude/logic/hooks/new-test-hook.py"})
    print(f"File change result: {result}")
    
    # Test manual trigger
    result = process("response", "/logic claude-md-update")
    print(f"Manual trigger result: {result}")