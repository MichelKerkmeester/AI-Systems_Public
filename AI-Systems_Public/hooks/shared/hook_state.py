#!/usr/bin/env python3
"""
State management utilities for Claude hooks
Handles session state, tracking, and persistence
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime


class SessionStateManager:
    """Manages session state across hook invocations"""
    
    def __init__(self, state_dir: Path):
        """
        Initialize session state manager
        
        Args:
            state_dir: Directory for state files
        """
        self.state_dir = state_dir
        self.session_file = state_dir / ".current-session"
        self.tracking_file = state_dir / "session-tracking.json"
        self.recovery_file = state_dir / ".session-recovery.json"
        
        # Attempt recovery on init
        self._attempt_recovery()
        
    def get_current_session(self) -> Optional[str]:
        """Get current session name"""
        if self.session_file.exists():
            try:
                return self.session_file.read_text().strip()
            except IOError:
                pass
        return None
    
    def set_current_session(self, session_name: str):
        """Set current session name"""
        os.makedirs(self.state_dir, exist_ok=True)
        self.session_file.write_text(session_name)
        # Also store the creation timestamp
        session_data = {
            "name": session_name,
            "created_at": datetime.now().isoformat()
        }
        session_info_file = self.state_dir / ".session-info.json"
        with open(session_info_file, 'w') as f:
            json.dump(session_data, f)
    
    def clear_current_session(self):
        """Clear current session"""
        if self.session_file.exists():
            self.session_file.unlink()
        session_info_file = self.state_dir / ".session-info.json"
        if session_info_file.exists():
            session_info_file.unlink()
    
    def get_session_age_hours(self) -> Optional[float]:
        """Get age of current session in hours"""
        session_info_file = self.state_dir / ".session-info.json"
        
        if session_info_file.exists():
            try:
                with open(session_info_file, 'r') as f:
                    session_data = json.load(f)
                created_at = datetime.fromisoformat(session_data['created_at'])
                age_seconds = (datetime.now() - created_at).total_seconds()
                return age_seconds / 3600
            except (json.JSONDecodeError, KeyError, ValueError, IOError):
                # Fallback to file modification time for backward compatibility
                if self.session_file.exists():
                    try:
                        mtime = self.session_file.stat().st_mtime
                        age_seconds = datetime.now().timestamp() - mtime
                        return age_seconds / 3600
                    except (OSError, IOError):
                        pass
        return None
    
    def load_tracking_data(self) -> Dict[str, Any]:
        """Load session tracking data"""
        default_tracking = {
            "sessions_created": 0,
            "sessions_archived": 0,
            "last_cleanup": None,
            "total_files_tracked": 0
        }
        
        if self.tracking_file.exists():
            try:
                with open(self.tracking_file, 'r') as f:
                    data = json.load(f)
                    return {**default_tracking, **data}
            except (json.JSONDecodeError, IOError):
                pass
        
        return default_tracking
    
    def save_tracking_data(self, data: Dict[str, Any]):
        """Save session tracking data"""
        os.makedirs(self.state_dir, exist_ok=True)
        with open(self.tracking_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def increment_counter(self, counter_name: str):
        """Increment a tracking counter"""
        data = self.load_tracking_data()
        data[counter_name] = data.get(counter_name, 0) + 1
        self.save_tracking_data(data)
    
    def _attempt_recovery(self):
        """Attempt to recover from crash or incomplete state"""
        if self.recovery_file.exists():
            try:
                with open(self.recovery_file, 'r') as f:
                    recovery_data = json.load(f)
                
                # Check if recovery is needed
                if recovery_data.get("needs_recovery", False):
                    self._perform_recovery(recovery_data)
                    
                # Clean up recovery file
                self.recovery_file.unlink()
            except Exception:
                # If recovery fails, just clean up
                try:
                    self.recovery_file.unlink()
                except:
                    pass
    
    def _perform_recovery(self, recovery_data: Dict[str, Any]):
        """Perform session recovery"""
        # Restore session name
        if "session_name" in recovery_data and recovery_data["session_name"]:
            self.set_current_session(recovery_data["session_name"])
        
        # Restore tracking data
        if "tracking_data" in recovery_data:
            tracking = self.load_tracking_data()
            tracking.update(recovery_data["tracking_data"])
            self.save_tracking_data(tracking)
    
    def create_recovery_point(self):
        """Create a recovery point for crash recovery"""
        recovery_data = {
            "timestamp": datetime.now().isoformat(),
            "session_name": self.get_current_session(),
            "tracking_data": self.load_tracking_data(),
            "needs_recovery": True
        }
        
        os.makedirs(self.state_dir, exist_ok=True)
        with open(self.recovery_file, 'w') as f:
            json.dump(recovery_data, f, indent=2)
    
    def clear_recovery_point(self):
        """Clear recovery point after successful operation"""
        if self.recovery_file.exists():
            try:
                self.recovery_file.unlink()
            except:
                pass


class FileTracker:
    """Tracks file changes during a session"""
    
    def __init__(self):
        self.files_modified: List[str] = []
        self.files_created: List[str] = []
        self.files_deleted: List[str] = []
        self.lines_changed: int = 0
        
    def track_modification(self, file_path: str, lines_changed: int = 0):
        """Track a file modification"""
        if file_path not in self.files_modified:
            self.files_modified.append(file_path)
        self.lines_changed += lines_changed
    
    def track_creation(self, file_path: str, lines: int = 0):
        """Track a file creation"""
        if file_path not in self.files_created:
            self.files_created.append(file_path)
        self.lines_changed += lines
    
    def track_deletion(self, file_path: str):
        """Track a file deletion"""
        if file_path not in self.files_deleted:
            self.files_deleted.append(file_path)
    
    def get_summary(self) -> Dict[str, Any]:
        """Get tracking summary"""
        return {
            "files_modified": len(self.files_modified),
            "files_created": len(self.files_created),
            "files_deleted": len(self.files_deleted),
            "total_files_changed": len(set(self.files_modified + self.files_created)),
            "lines_changed": self.lines_changed,
            "modified_files": self.files_modified,
            "created_files": self.files_created,
            "deleted_files": self.files_deleted
        }
    
    def merge_from_state(self, state: Dict[str, Any]):
        """Merge tracking data from saved state"""
        if "files_modified" in state:
            for f in state["files_modified"]:
                if f not in self.files_modified:
                    self.files_modified.append(f)
        
        if "files_created" in state:
            for f in state["files_created"]:
                if f not in self.files_created:
                    self.files_created.append(f)
        
        if "lines_changed" in state:
            self.lines_changed = state["lines_changed"]
    
    def to_state(self) -> Dict[str, Any]:
        """Convert to state dictionary"""
        return {
            "files_modified": self.files_modified,
            "files_created": self.files_created,
            "files_deleted": self.files_deleted,
            "lines_changed": self.lines_changed
        }


class TestTracker:
    """Tracks test execution state"""
    
    def __init__(self, state_path: Path):
        """Initialize test tracker"""
        self.state_path = state_path / "test-state.json"
        self._state = None
    
    @property
    def state(self) -> Dict[str, Any]:
        """Get test state"""
        if self._state is None:
            self._state = self.load()
        return self._state
    
    def load(self) -> Dict[str, Any]:
        """Load test state"""
        default_state = {
            "tests_run": False,
            "last_test_time": None,
            "test_count": 0,
            "files_since_test": 0,
            "lines_since_test": 0
        }
        
        if self.state_path.exists():
            try:
                with open(self.state_path, 'r') as f:
                    data = json.load(f)
                    return {**default_state, **data}
            except (json.JSONDecodeError, IOError):
                pass
        
        return default_state
    
    def save(self):
        """Save test state"""
        os.makedirs(self.state_path.parent, exist_ok=True)
        with open(self.state_path, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def mark_test_run(self):
        """Mark that tests have been run"""
        self.state["tests_run"] = True
        self.state["last_test_time"] = datetime.now().isoformat()
        self.state["test_count"] += 1
        self.state["files_since_test"] = 0
        self.state["lines_since_test"] = 0
        self.save()
    
    def increment_changes(self, files: int = 0, lines: int = 0):
        """Increment change counters since last test"""
        self.state["files_since_test"] += files
        self.state["lines_since_test"] += lines
        self.save()
    
    def should_remind_test(self, file_threshold: int = 3, 
                          line_threshold: int = 50) -> bool:
        """Check if test reminder should be shown"""
        return (not self.state["tests_run"] or 
                self.state["files_since_test"] >= file_threshold or
                self.state["lines_since_test"] >= line_threshold)
    
    def reset(self):
        """Reset test state"""
        self._state = None
        if self.state_path.exists():
            self.state_path.unlink()