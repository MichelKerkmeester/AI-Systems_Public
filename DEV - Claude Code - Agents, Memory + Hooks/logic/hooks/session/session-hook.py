#!/usr/bin/env python3
"""
Unified Session Hook for Claude Code
Combines: session management (creation/archival) and session updates
"""

import sys
import os
import json
import shutil
import tarfile
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, Tuple, List

# Add parent directory to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import (
    HookBase, ToolHook,
    SettingsManager, SessionStateManager,
    MessageFormatter, FileTracker
)


class SessionHook(HookBase):
    """Unified session hook handling creation, archival, and updates"""
    
    def __init__(self):
        super().__init__()
        
        # Session paths
        self.sessions_dir = self.claude_path / "project" / "sessions"
        self.current_dir = self.sessions_dir / "current"
        self.old_dir = self.sessions_dir / "old"
        self.backups_dir = self.sessions_dir / "backups"
        
        # Settings and state
        self.settings_path = self.claude_path / "logic" / "session" / "hooks" / "session-settings.json"
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        
        self.state_dir = self.claude_path / "project" / "state"
        self.session_state = SessionStateManager(self.state_dir)
        
        # File tracking
        self.file_tracker = FileTracker()
        
        # Excluded tools (don't track in sessions)
        self.excluded_tools = self.settings.get("exclude_tools", [])
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "enabled": True,
            "session_timeout_hours": 4,
            "session_limit": 10,
            "backup_before_delete": True,
            "exclude_tools": ["Read", "LS", "Grep", "Glob", "WebSearch", "WebFetch"],
            "auto_description": True,
            "verbose_updates": False
        }
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook based on event type"""
        if not self.settings.get("enabled"):
            return 0, None
        
        # Detect event type from hook input structure
        # PreToolUse has toolName but no toolResult
        # PostToolUse has both toolName and toolResult
        if "toolName" in hook_input and "toolResult" not in hook_input:
            return self._handle_pre_tool_use(hook_input)
        elif "toolName" in hook_input and "toolResult" in hook_input:
            return self._handle_post_tool_use(hook_input)
        else:
            return 0, None
    
    def _handle_pre_tool_use(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Handle PreToolUse event - create/archive sessions"""
        tool_name = hook_input.get("toolName", "")
        
        # Skip excluded tools
        if tool_name in self.excluded_tools:
            return 0, None
        
        # Check if we need a new session
        current_session = self.session_state.get_current_session()
        session_age = self.session_state.get_session_age_hours()
        
        needs_new_session = (
            not current_session or
            session_age is None or
            session_age > self.settings.get("session_timeout_hours", 4)
        )
        
        if needs_new_session:
            # Create new session
            output = self._create_new_session(hook_input)
            return 0, output
        
        return 0, None
    
    def _handle_post_tool_use(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Handle PostToolUse event - update session content"""
        tool_name = hook_input.get("toolName", "")
        
        # Skip excluded tools
        if tool_name in self.excluded_tools:
            return 0, None
        
        # Get current session
        current_session = self.session_state.get_current_session()
        if not current_session:
            return 0, None
        
        # Update session file
        session_file = self.current_dir / current_session
        if not session_file.exists():
            return 0, None
        
        # Track file changes
        self._track_file_changes(hook_input)
        
        # Update session content
        self._update_session_content(session_file, hook_input)
        
        # No output for updates unless verbose
        if self.settings.get("verbose_updates"):
            return 0, f"📝 Updated session: {current_session}"
        
        return 0, None
    
    def _create_new_session(self, hook_input: Dict[str, Any]) -> str:
        """Create a new session"""
        # Ensure directories exist
        os.makedirs(self.current_dir, exist_ok=True)
        os.makedirs(self.old_dir, exist_ok=True)
        os.makedirs(self.backups_dir, exist_ok=True)
        
        # Check session limit and archive if needed
        self._enforce_session_limit()
        
        # Generate session name
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        description = self._extract_description(hook_input)
        session_name = f"{timestamp}-{description}.md"
        
        # Create session file
        session_file = self.current_dir / session_name
        
        # Initial content
        content = f"""# Session: {description}
**Started:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Status:** Active

## Summary
New session started after {self.settings.get('session_timeout_hours', 4)}-hour timeout.

## Tools Used

## Files Modified

## Key Decisions

## Notes

---

### Activity Log
"""
        
        # Write session file
        with open(session_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Update state
        self.session_state.set_current_session(session_name)
        self.session_state.increment_counter("sessions_created")
        
        # Reset file tracker
        self.file_tracker = FileTracker()
        
        # Build output
        output = MessageFormatter.header("New Session Created", "session")
        output += f"\n📂 Session: {session_name}"
        output += f"\n⏰ Timeout: {self.settings.get('session_timeout_hours', 4)} hours"
        output += f"\n📁 Location: {session_file.relative_to(self.project_root)}"
        
        # Show session stats
        tracking = self.session_state.load_tracking_data()
        output += f"\n📊 Total sessions: {tracking.get('sessions_created', 0)}"
        
        output += "\n" + MessageFormatter.footer()
        
        return output
    
    def _extract_description(self, hook_input: Dict[str, Any]) -> str:
        """Extract description from tool input"""
        if not self.settings.get("auto_description"):
            return "development"
        
        tool_name = hook_input.get("toolName", "")
        tool_input = hook_input.get("toolInput", {})
        
        # Try to extract meaningful description
        if tool_name == "Bash":
            command = tool_input.get("command", "")
            if "git" in command:
                return "git-operations"
            elif "npm" in command:
                return "npm-commands"
            elif "test" in command:
                return "testing"
            else:
                # Use first word of command
                first_word = command.split()[0] if command else "bash"
                return first_word[:20]  # Limit length
        
        elif tool_name in ["Edit", "Write", "MultiEdit"]:
            file_path = tool_input.get("file_path", "")
            if file_path:
                # Use file name without extension
                file_name = Path(file_path).stem
                return file_name[:30]  # Limit length
        
        elif tool_name == "TodoWrite":
            return "task-management"
        
        # Default based on tool
        return tool_name.lower()[:20] if tool_name else "development"
    
    def _enforce_session_limit(self):
        """Enforce session limit by archiving old sessions"""
        current_sessions = list(self.current_dir.glob("*.md"))
        
        if len(current_sessions) >= self.settings.get("session_limit", 10):
            # Sort by modification time (oldest first)
            current_sessions.sort(key=lambda p: p.stat().st_mtime)
            
            # Archive oldest sessions
            to_archive = len(current_sessions) - self.settings.get("session_limit", 10) + 1
            
            for session_file in current_sessions[:to_archive]:
                self._archive_session(session_file)
    
    def _archive_session(self, session_file: Path):
        """Archive a session file"""
        # Generate summary before archiving
        self._generate_session_summary(session_file)
        
        # Move to old directory
        old_file = self.old_dir / session_file.name
        shutil.move(str(session_file), str(old_file))
        
        # Create backup if enabled
        if self.settings.get("backup_before_delete"):
            self._create_backup(old_file)
        
        # Update tracking
        self.session_state.increment_counter("sessions_archived")
    
    def _create_backup(self, file_path: Path):
        """Create compressed backup of session"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_name = f"backup-{timestamp}-{file_path.stem}.tar.gz"
        backup_path = self.backups_dir / backup_name
        
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(file_path, arcname=file_path.name)
    
    def _track_file_changes(self, hook_input: Dict[str, Any]):
        """Track file changes from tool usage"""
        tool_name = hook_input.get("toolName", "")
        tool_input = hook_input.get("toolInput", {})
        
        if tool_name == "Edit":
            file_path = tool_input.get("file_path", "")
            if file_path:
                lines = len(tool_input.get("new_string", "").split('\n'))
                self.file_tracker.track_modification(file_path, lines)
        
        elif tool_name == "MultiEdit":
            file_path = tool_input.get("file_path", "")
            if file_path:
                total_lines = sum(
                    len(edit.get("new_string", "").split('\n'))
                    for edit in tool_input.get("edits", [])
                )
                self.file_tracker.track_modification(file_path, total_lines)
        
        elif tool_name == "Write":
            file_path = tool_input.get("file_path", "")
            if file_path:
                lines = len(tool_input.get("content", "").split('\n'))
                self.file_tracker.track_creation(file_path, lines)
        
        elif tool_name == "Bash":
            command = tool_input.get("command", "")
            if "rm " in command:
                # Try to extract file path from rm command
                parts = command.split()
                if len(parts) > 1:
                    file_path = parts[-1].strip("'\"")
                    self.file_tracker.track_deletion(file_path)
    
    def _update_session_content(self, session_file: Path, hook_input: Dict[str, Any]):
        """Update session file content"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        tool_name = hook_input.get("toolName", "")
        tool_input = hook_input.get("toolInput", {})
        
        # Build activity entry
        activity = f"\n**[{timestamp}]** `{tool_name}`"
        
        # Add tool-specific details
        if tool_name == "Bash":
            command = tool_input.get("command", "")
            activity += f" - {command[:100]}..."
        
        elif tool_name in ["Edit", "Write", "MultiEdit"]:
            file_path = tool_input.get("file_path", "")
            if file_path:
                activity += f" - {Path(file_path).name}"
        
        elif tool_name == "TodoWrite":
            todos = tool_input.get("todos", [])
            completed = sum(1 for t in todos if t.get("status") == "completed")
            total = len(todos)
            activity += f" - {completed}/{total} tasks"
        
        # Append to session file
        with open(session_file, 'a', encoding='utf-8') as f:
            f.write(activity + "\n")
        
        # Update file lists periodically
        if self.file_tracker.files_modified or self.file_tracker.files_created:
            self._update_file_lists(session_file)
    
    def _update_file_lists(self, session_file: Path):
        """Update file modification lists in session"""
        # Read current content
        content = session_file.read_text(encoding='utf-8')
        
        # Update files modified section
        summary = self.file_tracker.get_summary()
        
        files_section = "\n## Files Modified\n"
        if summary["modified_files"]:
            for f in summary["modified_files"]:
                files_section += f"- {f}\n"
        if summary["created_files"]:
            files_section += "\n### Created\n"
            for f in summary["created_files"]:
                files_section += f"- {f}\n"
        
        # Replace the section
        import re
        pattern = r'## Files Modified.*?(?=##|\n---|\Z)'
        replacement = files_section.rstrip() + "\n"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # If section doesn't exist, add it
        if "## Files Modified" not in new_content:
            # Insert after summary
            insert_point = new_content.find("## Key Decisions")
            if insert_point > 0:
                new_content = (
                    new_content[:insert_point] +
                    files_section + "\n" +
                    new_content[insert_point:]
                )
        
        # Write back
        session_file.write_text(new_content, encoding='utf-8')
    
    def _generate_session_summary(self, session_file: Path):
        """Generate auto-summary for session"""
        try:
            content = session_file.read_text(encoding='utf-8')
            
            # Extract key information
            summary_data = self.file_tracker.get_summary()
            
            # Calculate session duration
            session_name = session_file.stem
            try:
                # Extract timestamp from filename
                parts = session_name.split('-')
                if len(parts) >= 6:
                    timestamp_str = '-'.join(parts[:6])
                    created = datetime.strptime(timestamp_str[:19], '%Y-%m-%d-%H%M%S')
                    duration_hours = (datetime.now() - created).total_seconds() / 3600
                else:
                    duration_hours = 0
            except:
                duration_hours = 0
            
            # Count tools used
            tool_pattern = r'\*\*\[\d{2}:\d{2}:\d{2}\]\*\* `(\w+)`'
            tools_used = {}
            for match in re.finditer(tool_pattern, content):
                tool = match.group(1)
                tools_used[tool] = tools_used.get(tool, 0) + 1
            
            # Generate summary section
            summary = "\n## 📊 Auto-Generated Summary\n"
            summary += f"**Duration:** {duration_hours:.1f} hours\n"
            summary += f"**Files Modified:** {summary_data['files_modified']}\n"
            summary += f"**Files Created:** {summary_data['files_created']}\n"
            summary += f"**Total Lines Changed:** {summary_data['lines_changed']}\n"
            
            if tools_used:
                summary += "\n### Most Used Tools:\n"
                for tool, count in sorted(tools_used.items(), key=lambda x: x[1], reverse=True)[:5]:
                    summary += f"- {tool}: {count} times\n"
            
            if summary_data['modified_files']:
                summary += "\n### Key Files Modified:\n"
                for file in summary_data['modified_files'][:10]:
                    summary += f"- {Path(file).name}\n"
            
            # Insert summary after the Summary section
            summary_marker = "## Summary"
            if summary_marker in content:
                parts = content.split(summary_marker, 1)
                # Find the next section
                next_section = re.search(r'\n##\s', parts[1])
                if next_section:
                    insert_pos = next_section.start()
                    new_content = (
                        parts[0] + summary_marker + 
                        parts[1][:insert_pos] +
                        summary + "\n" +
                        parts[1][insert_pos:]
                    )
                else:
                    new_content = content + summary
            else:
                new_content = content + summary
            
            # Write updated content
            session_file.write_text(new_content, encoding='utf-8')
            
        except Exception as e:
            # Don't fail archival if summary generation fails
            pass


if __name__ == "__main__":
    hook = SessionHook()
    hook.run()