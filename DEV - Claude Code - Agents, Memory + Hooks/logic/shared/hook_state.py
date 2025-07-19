#!/usr/bin/env python3
"""
State management utilities for Claude hooks
Handles tracking and persistence for file changes and tests
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime


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