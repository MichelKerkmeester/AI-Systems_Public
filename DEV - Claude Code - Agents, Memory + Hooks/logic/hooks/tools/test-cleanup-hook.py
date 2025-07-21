#!/usr/bin/env python3
"""
Test Cleanup Hook
Automatically removes test files after test execution completes
"""

import sys
import json
import re
import os
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List
from datetime import datetime

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared.hook_base import HookBase


class TestCleanupHook(HookBase):
    """Automatically clean up test files after test execution"""
    
    def __init__(self):
        super().__init__()
        import logging
        self.logger = logging.getLogger(__name__)
        
        # Patterns that indicate test execution
        self.test_execution_patterns = [
            r"test.*passed",
            r"test.*failed",
            r"test.*complete",
            r"finished.*test",
            r"pytest.*===",
            r"unittest.*ran \d+ test",
            r"test results:",
            r"tests? (passed|failed|complete)"
        ]
        
        # File patterns to clean up
        self.cleanup_patterns = [
            "test_*.py",
            "*_test.py",
            "test-*.py",
            "*-test.py",
            "test*.json",
            "*test-results*.json",
            "*test-output*.txt"
        ]
        
        # Directories to exclude from cleanup (never delete from these)
        self.protected_dirs = [
            "node_modules",
            ".git",
            "venv",
            "__pycache__",
            "z__archive",  # User-managed archives
            "y__templates",  # Templates
            "specs"  # Active specs might have test plans
        ]
        
        # Track recent test executions
        self.recent_tests = []
        
    def detect_test_completion(self, tool_name: str, tool_args: Dict, result: Any) -> bool:
        """Detect if a test has completed based on tool output"""
        if tool_name != "Bash":
            return False
            
        # Check command for test execution
        command = tool_args.get("command", "")
        test_commands = ["pytest", "python.*test", "npm test", "yarn test", "unittest"]
        
        for pattern in test_commands:
            if re.search(pattern, command, re.IGNORECASE):
                # Check if result indicates completion
                result_str = str(result)
                for completion_pattern in self.test_execution_patterns:
                    if re.search(completion_pattern, result_str, re.IGNORECASE):
                        return True
        
        return False
        
    def find_test_files_to_cleanup(self, base_path: Path = None) -> List[Path]:
        """Find test files that should be cleaned up"""
        if base_path is None:
            base_path = Path.cwd()
            
        files_to_cleanup = []
        
        # Check each cleanup pattern
        for pattern in self.cleanup_patterns:
            for file_path in base_path.rglob(pattern):
                # Skip protected directories
                if any(protected in str(file_path) for protected in self.protected_dirs):
                    continue
                    
                # Skip files in active specs
                if "specs" in file_path.parts and "tests" in file_path.parts:
                    # Check if this is part of an active spec
                    spec_dir = file_path
                    while spec_dir.parent != base_path and "specs" not in spec_dir.name:
                        spec_dir = spec_dir.parent
                    
                    # If there's a requirements.md in the spec dir, it's likely active
                    if (spec_dir / "requirements.md").exists():
                        continue
                        
                # Skip recently modified files (within last 5 minutes for normal files)
                # But allow immediate cleanup for test result files
                try:
                    stat = file_path.stat()
                    age_minutes = (datetime.now().timestamp() - stat.st_mtime) / 60
                    
                    # Test result files can be cleaned immediately
                    if "test-results" in file_path.name or file_path.suffix == ".json":
                        pass  # Don't skip
                    elif age_minutes < 5:
                        continue
                except:
                    continue
                    
                files_to_cleanup.append(file_path)
                
        return files_to_cleanup
        
    def cleanup_test_files(self, files: List[Path]) -> Dict[str, Any]:
        """Remove test files and return cleanup summary"""
        cleanup_summary = {
            "removed": [],
            "failed": [],
            "total": len(files)
        }
        
        for file_path in files:
            try:
                if file_path.exists():  # Check if file still exists
                    file_path.unlink()
                    cleanup_summary["removed"].append(str(file_path))
                    self.logger.info(f"Removed test file: {file_path}")
            except Exception as e:
                cleanup_summary["failed"].append({
                    "file": str(file_path),
                    "error": str(e)
                })
                self.logger.error(f"Failed to remove {file_path}: {e}")
                
        return cleanup_summary
        
    def format_cleanup_message(self, summary: Dict[str, Any]) -> str:
        """Format a user-friendly cleanup message"""
        if not summary["removed"]:
            return None
            
        message_parts = [
            f"🧹 Test cleanup completed:",
            f"- Removed {len(summary['removed'])} test file(s)"
        ]
        
        # Show first few removed files
        for file_path in summary["removed"][:3]:
            message_parts.append(f"  • {Path(file_path).name}")
            
        if len(summary["removed"]) > 3:
            message_parts.append(f"  • ... and {len(summary['removed']) - 3} more")
            
        if summary["failed"]:
            message_parts.append(f"- Failed to remove {len(summary['failed'])} file(s)")
            
        return "\n".join(message_parts)
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process tool use events and clean up test files when tests complete"""
        tool_name = hook_input.get('tool_name', '')
        tool_args = hook_input.get('tool_args', {})
        result = hook_input.get('result', {})
        
        try:
            # Check if this is a test completion
            if not self.detect_test_completion(tool_name, tool_args, result):
                return 0, None
                
            # Find test files to clean up
            test_files = self.find_test_files_to_cleanup()
            
            if not test_files:
                return 0, None
                
            # Perform cleanup
            summary = self.cleanup_test_files(test_files)
            
            # Format user message
            message = self.format_cleanup_message(summary)
            
            # Log the cleanup
            self.recent_tests.append({
                "timestamp": datetime.now().isoformat(),
                "command": tool_args.get("command", ""),
                "cleaned": len(summary["removed"]),
                "failed": len(summary["failed"])
            })
            
            # Keep only last 10 test records
            self.recent_tests = self.recent_tests[-10:]
            
            return 0, message
                    
        except Exception as e:
            self.logger.error(f"TestCleanupHook error: {e}")
            
        return 0, None


# Main entry point
if __name__ == "__main__":
    hook = TestCleanupHook()
    hook.run()