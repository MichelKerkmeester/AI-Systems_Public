#!/usr/bin/env python3
"""
Complete Automation Test Suite
Date: 2025-01-21
Time: 11:45:00
"""

import os
import sys
import json
import tempfile
import shutil
from datetime import datetime
from pathlib import Path

# Add .claude to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../../'))

from logic.tasks.task_manager import TaskManager

# Import spec generation hook differently
spec_hook_module = 'spec-generation-hook'
spec_hook_path = os.path.join(os.path.dirname(__file__), '../../../../logic/hooks/core/spec-generation-hook.py')
import importlib.util
spec = importlib.util.spec_from_file_location("spec_generation_hook", spec_hook_path)
spec_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(spec_module)
SpecGenerationHook = spec_module.SpecGenerationHook

class AutomationTester:
    def __init__(self):
        self.tm = TaskManager()
        # Don't instantiate spec hook, just use its methods
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
        
    def test_task_creation_with_folders(self):
        """Test automatic folder and test directory creation"""
        test_name = "AUTO-01: Task Creation with Folders"
        
        try:
            # Create a test task
            task_name = f"Test Automation Task {self.timestamp}"
            task = self.tm.create_task(
                name=task_name,
                description="Testing automatic folder creation"
            )
            
            # Check folder structure
            subfolder = self.tm._determine_task_subfolder(task_name)
            safe_project_name = ''.join(c for c in task_name.lower() if c.isalnum() or c in ' -_')
            safe_project_name = safe_project_name.replace(' ', '-')
            
            project_dir = self.tm.to_do_dir / subfolder / safe_project_name
            test_dir = project_dir / "tests"
            
            # Verify directories exist
            checks = [
                (project_dir.exists(), "Project directory created"),
                (test_dir.exists(), "Test directory created"),
                (any(project_dir.glob("*.md")), "Task file created"),
                (any(test_dir.glob("test-plan-*.md")), "Test plan created")
            ]
            
            all_passed = True
            for check, desc in checks:
                self.log_result(f"{test_name} - {desc}", check, desc if check else f"Failed: {desc}")
                if not check:
                    all_passed = False
                    
            # Cleanup
            if project_dir.exists():
                shutil.rmtree(project_dir)
                
            return all_passed
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def test_spec_generation_hook(self):
        """Test automatic spec generation"""
        test_name = "AUTO-02: Spec Generation Hook"
        
        try:
            # Test complex query detection
            complex_query = """
            I need to implement a new authentication system with the following requirements:
            - User registration with email verification
            - Login with JWT tokens
            - Password reset functionality
            - Role-based access control
            - Integration with existing database
            First, analyze the current auth system, then design the new architecture,
            and finally implement it with proper tests.
            """
            
            # Create a temporary instance for testing
            spec_hook = SpecGenerationHook.__new__(SpecGenerationHook)
            spec_hook.spec_threshold = 6
            
            # Calculate complexity score
            score = spec_hook._calculate_complexity_score(complex_query)
            
            # Test continuation detection
            session_data = {
                "active_task": "Test Task",
                "query_history": ["previous query"]
            }
            
            continuation_queries = [
                "continue with that",
                "also add logging",
                "what about error handling?",
                "next, implement the UI"
            ]
            
            non_continuation_queries = [
                "Create a new feature for data export",
                "I need help with a different problem",
                "Analyze the performance metrics"
            ]
            
            results = []
            
            # Test complexity score
            results.append((score >= 6, f"Complexity score: {score} (threshold: 6)"))
            
            # Test continuation detection
            for query in continuation_queries:
                is_cont = spec_hook._is_continuation_query(query, session_data)
                results.append((is_cont, f"'{query[:20]}...' detected as continuation"))
                
            for query in non_continuation_queries:
                is_cont = spec_hook._is_continuation_query(query, session_data)
                results.append((not is_cont, f"'{query[:20]}...' detected as new query"))
                
            all_passed = True
            for passed, desc in results:
                self.log_result(f"{test_name} - {desc}", passed, desc)
                if not passed:
                    all_passed = False
                    
            return all_passed
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def test_timestamp_in_documents(self):
        """Test timestamp inclusion in all documents"""
        test_name = "AUTO-03: Timestamps in Documents"
        
        try:
            # Create a test task
            task_name = f"Timestamp Test {self.timestamp}"
            task = self.tm.create_task(name=task_name)
            
            # Find the created files
            subfolder = self.tm._determine_task_subfolder(task_name)
            safe_project_name = ''.join(c for c in task_name.lower() if c.isalnum() or c in ' -_')
            safe_project_name = safe_project_name.replace(' ', '-')
            
            project_dir = self.tm.to_do_dir / subfolder / safe_project_name
            
            # Check task file
            task_files = list(project_dir.glob("*.md"))
            test_plan_files = list((project_dir / "tests").glob("test-plan-*.md"))
            
            results = []
            
            if task_files:
                task_file = task_files[0]
                # Check filename has timestamp
                has_timestamp_filename = self.timestamp[:10] in str(task_file)
                results.append((has_timestamp_filename, "Task filename has timestamp"))
                
                # Check content has date/time
                content = task_file.read_text()
                has_date = "**Date:**" in content
                has_time = "**Time:**" in content
                results.append((has_date and has_time, "Task content has date/time"))
                
            if test_plan_files:
                test_file = test_plan_files[0]
                # Check test plan has timestamp
                has_timestamp_filename = self.timestamp[:10] in str(test_file)
                results.append((has_timestamp_filename, "Test plan filename has timestamp"))
                
                # Check content
                content = test_file.read_text()
                has_date = "**Date:**" in content
                results.append((has_date, "Test plan has date"))
                
            # Cleanup
            if project_dir.exists():
                shutil.rmtree(project_dir)
                
            all_passed = True
            for passed, desc in results:
                self.log_result(f"{test_name} - {desc}", passed, desc)
                if not passed:
                    all_passed = False
                    
            return all_passed
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def test_folder_categorization(self):
        """Test improved categorization logic"""
        test_name = "AUTO-04: Folder Categorization"
        
        try:
            test_cases = [
                # (task_name, expected_category)
                ("Update API Documentation", "documentation"),
                ("Add Unit Tests for User Service", "testing"),
                ("Fix Security Vulnerability in Auth", "security"),
                ("Implement User Profile Feature", "features"),
                ("Enhance Search Performance", "performance"),
                ("Refactor Database Layer", "refactoring"),
                ("Connect Stripe API", "integrations"),
                ("Improve UI Responsiveness", "enhancements"),
                ("Debug Login Issue", "bugs"),
                ("Random Task Name", "general")
            ]
            
            all_passed = True
            for task_name, expected in test_cases:
                actual = self.tm._determine_task_subfolder(task_name)
                passed = actual == expected
                self.log_result(
                    f"{test_name} - '{task_name}'",
                    passed,
                    f"Expected '{expected}', got '{actual}'" if not passed else f"Correctly categorized as '{actual}'"
                )
                if not passed:
                    all_passed = False
                    
            return all_passed
            
        except Exception as e:
            self.log_result(test_name, False, f"Error: {str(e)}")
            return False
            
    def run_all_tests(self):
        """Run all automation tests"""
        print(f"\n🤖 Running Complete Automation Tests - {self.timestamp}\n")
        
        # Run tests
        self.test_task_creation_with_folders()
        self.test_spec_generation_hook()
        self.test_timestamp_in_documents()
        self.test_folder_categorization()
        
        # Summary
        passed = sum(1 for r in self.test_results if r["passed"])
        total = len(self.test_results)
        
        print(f"\n📊 Test Summary: {passed}/{total} passed")
        
        # Key improvements implemented
        improvements = {
            "task_categorization": "Fixed - now correctly categorizes docs, tests, security",
            "test_folder_creation": "Implemented - automatic /tests folder with test plan",
            "spec_generation": "Implemented - automatic spec creation for complex queries",
            "continuation_detection": "Implemented - detects follow-up vs new queries",
            "timestamps": "Implemented - all documents include date/time",
            "project_folders": "Implemented - each task in its own subfolder"
        }
        
        # Save results
        results_file = f"automation-test-results-{self.timestamp}.json"
        with open(results_file, 'w') as f:
            json.dump({
                "test_run": self.timestamp,
                "summary": {
                    "total": total,
                    "passed": passed,
                    "failed": total - passed,
                    "success_rate": f"{(passed/total*100):.1f}%"
                },
                "improvements_implemented": improvements,
                "results": self.test_results
            }, f, indent=2)
            
        print(f"\n💾 Results saved to: {results_file}")
        
        # Final verdict
        if passed == total:
            print("\n🎉 All automation features working correctly!")
        else:
            print(f"\n⚠️  {total - passed} tests failed - review results file")
        
        return passed == total

if __name__ == "__main__":
    tester = AutomationTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)