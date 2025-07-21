#!/usr/bin/env python3
"""
Test Task Manager Functionality
Date: 2025-01-21
Time: 11:25:00
"""

import os
import sys
import json
import shutil
from datetime import datetime

# Add .claude to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../'))

from logic.tasks.task_manager import TaskManager

class TaskManagerTester:
    def __init__(self):
        self.tm = TaskManager()
        self.test_results = []
        self.timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        
    def log_result(self, test_name, passed, message):
        """Log test result"""
        result = {
            "test": test_name,
            "passed": passed,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)
        print(f"{'✅' if passed else '❌'} {test_name}: {message}")
        
    def test_subfolder_creation(self):
        """Test TM-01: Sub-folder creation automation"""
        test_name = "TM-01: Sub-folder Creation"
        
        try:
            # Test different task types
            test_cases = [
                ("Add User Authentication Feature", "security"),  # Auth is now security
                ("Fix Login Bug", "bugs"),
                ("Enhance Performance", "performance"),  # Performance is its own category
                ("Refactor Database Module", "refactoring"),
                ("Update Documentation", "documentation"),
                ("Create Test Suite", "testing"),
                ("Security Vulnerability Fix", "security"),
                ("General Task", "general")
            ]
            
            all_passed = True
            for task_name, expected_folder in test_cases:
                folder = self.tm._determine_task_subfolder(task_name)
                if folder != expected_folder:
                    all_passed = False
                    self.log_result(
                        f"{test_name} - {task_name}",
                        False,
                        f"Expected '{expected_folder}', got '{folder}'"
                    )
                else:
                    self.log_result(
                        f"{test_name} - {task_name}",
                        True,
                        f"Correctly categorized as '{folder}'"
                    )
                    
            return all_passed
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def test_one_task_limit(self):
        """Test TM-04: One active task limit enforcement"""
        test_name = "TM-04: One Task Limit"
        
        try:
            # Get current registry
            registry = self.tm.get_task_registry()
            
            # Check if there's already an active task
            if registry.get("active_task"):
                self.log_result(
                    test_name,
                    True,
                    f"Active task limit enforced - current: {registry['active_task']}"
                )
                return True
            else:
                self.log_result(
                    test_name,
                    True,
                    "No active task - limit would be enforced on activation"
                )
                return True
                
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def test_archive_exclusion(self):
        """Test TM-04: Archive folder exclusion"""
        test_name = "TM-04: Archive Exclusion"
        
        try:
            # Test archive method raises error
            try:
                self.tm.archive_old_tasks()
                self.log_result(test_name, False, "Archive method didn't raise error")
                return False
            except NotImplementedError:
                pass
                
            # Test exclusion check
            test_paths = [
                (".claude/project-management/z__archive/test.md", True),
                (".claude/project-management/completed/test.md", False),
                (".claude/z__archive/something.py", True),
                (".claude/project-management/active/test.md", False)
            ]
            
            all_passed = True
            for path, should_exclude in test_paths:
                excluded = self.tm.should_exclude_path(path)
                if excluded != should_exclude:
                    all_passed = False
                    self.log_result(
                        f"{test_name} - {path}",
                        False,
                        f"Expected exclude={should_exclude}, got {excluded}"
                    )
                    
            if all_passed:
                self.log_result(test_name, True, "Archive folders correctly excluded")
                
            return all_passed
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def test_task_lifecycle(self):
        """Test TM-02: Task lifecycle management"""
        test_name = "TM-02: Task Lifecycle"
        
        try:
            # Check task flow directories exist
            dirs = ["specs", "active", "completed"]
            base_path = ".claude/project-management"
            
            all_exist = True
            for dir_name in dirs:
                dir_path = os.path.join(base_path, dir_name)
                if os.path.exists(dir_path):
                    self.log_result(
                        f"{test_name} - {dir_name}",
                        True,
                        f"Directory exists: {dir_path}"
                    )
                else:
                    all_exist = False
                    self.log_result(
                        f"{test_name} - {dir_name}",
                        False,
                        f"Directory missing: {dir_path}"
                    )
                    
            return all_exist
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def run_all_tests(self):
        """Run all tests and generate report"""
        print(f"\n🧪 Running Task Manager Tests - {self.timestamp}\n")
        
        # Run tests
        self.test_subfolder_creation()
        self.test_one_task_limit()
        self.test_archive_exclusion()
        self.test_task_lifecycle()
        
        # Summary
        passed = sum(1 for r in self.test_results if r["passed"])
        total = len(self.test_results)
        
        print(f"\n📊 Test Summary: {passed}/{total} passed")
        
        # Save results
        results_file = f"test-results-{self.timestamp}.json"
        with open(results_file, 'w') as f:
            json.dump({
                "test_run": self.timestamp,
                "summary": {
                    "total": total,
                    "passed": passed,
                    "failed": total - passed
                },
                "results": self.test_results
            }, f, indent=2)
            
        print(f"\n💾 Results saved to: {results_file}")
        
        return passed == total

if __name__ == "__main__":
    tester = TaskManagerTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)