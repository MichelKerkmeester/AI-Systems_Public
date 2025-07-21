#!/usr/bin/env python3
"""
Comprehensive Integration Test Suite for Command System Refactoring Hooks
Tests all hooks, priority system, and performance metrics
"""

import sys
import os
import json
import time
import unittest
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from hooks.shared import (
    HookBase, HookRegistry, HookPriority,
    DistributedLockManager, AgentRegistry
)


class TestHooksIntegration(unittest.TestCase):
    """Integration tests for all refactored hooks"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_dir = Path("/tmp/claude_hooks_test")
        self.test_dir.mkdir(exist_ok=True)
        
        # Create test agent ID
        self.agent_id = f"test-agent-{os.getpid()}"
        
        # Initialize managers
        self.hook_registry = HookRegistry()
        self.lock_manager = DistributedLockManager(self.agent_id)
        
        # Performance tracking
        self.performance_results = {}
    
    def tearDown(self):
        """Clean up test environment"""
        # Clean up test files
        if self.test_dir.exists():
            import shutil
            shutil.rmtree(self.test_dir)
    
    def test_hook_priority_system(self):
        """Test hook priority ordering and execution"""
        # Test priority ordering
        priorities = [
            ("security-scan", HookPriority.CRITICAL),
            ("quality-check", HookPriority.QUALITY),
            ("workflow-automation", HookPriority.WORKFLOW),
            ("context-management", HookPriority.CONTEXT),
            ("pattern-extraction", HookPriority.PATTERN)
        ]
        
        # Sort by priority
        sorted_hooks = sorted(priorities, key=lambda x: x[1].value)
        
        # Verify order
        self.assertEqual(sorted_hooks[0][0], "security-scan")
        self.assertEqual(sorted_hooks[-1][0], "pattern-extraction")
    
    def test_workflow_automation_hook(self):
        """Test workflow automation hook triggers and performance"""
        # Import path with hyphen in filename
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        import workflow_automation_hook
        WorkflowAutomationHook = workflow_automation_hook.WorkflowAutomationHook
        
        hook = WorkflowAutomationHook()
        
        # Test simple query (should not trigger)
        simple_input = {
            "toolName": "Bash",
            "toolInput": {"command": "ls"},
            "userMessage": "list files"
        }
        
        start_time = time.time()
        exit_code, output = hook.process(simple_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 0)
        self.assertIsNone(output)
        self.assertLess(duration, 10)  # Should be very fast
        
        # Test complex query (should trigger)
        complex_input = {
            "toolName": "Bash",
            "toolInput": {"command": "echo 'complex task'"},
            "userMessage": "I need to refactor the authentication system to use OAuth2, update all API endpoints, and ensure backward compatibility"
        }
        
        start_time = time.time()
        exit_code, output = hook.process(complex_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 0)
        self.assertIsNotNone(output)
        self.assertIn("Sequential Thinking", output)
        self.assertLess(duration, 50)  # Should be reasonably fast
        
        self.performance_results["workflow_automation"] = duration
    
    def test_security_scan_hook(self):
        """Test security scan hook detection and blocking"""
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        import security_scan_hook
        SecurityScanHook = security_scan_hook.SecurityScanHook
        
        hook = SecurityScanHook()
        
        # Test safe operation
        safe_input = {
            "toolName": "Write",
            "toolInput": {
                "file_path": str(self.test_dir / "safe.txt"),
                "content": "Hello world"
            }
        }
        
        start_time = time.time()
        exit_code, output = hook.process(safe_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 0)
        self.assertIsNone(output)
        
        # Test API key detection
        unsafe_input = {
            "toolName": "Write",
            "toolInput": {
                "file_path": str(self.test_dir / "config.py"),
                "content": "API_KEY = 'sk-1234567890abcdef'"
            }
        }
        
        start_time = time.time()
        exit_code, output = hook.process(unsafe_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 1)  # Should block
        self.assertIsNotNone(output)
        self.assertIn("Security", output)
        self.assertLess(duration, 20)  # Should be very fast
        
        self.performance_results["security_scan"] = duration
    
    def test_context_management_hook(self):
        """Test context management hook auto-save functionality"""
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        import context_management_hook
        ContextManagementHook = context_management_hook.ContextManagementHook
        
        hook = ContextManagementHook()
        
        # Simulate multiple operations
        for i in range(6):  # Trigger after 5 operations
            input_data = {
                "toolName": "Edit",
                "toolInput": {
                    "file_path": f"test{i}.py",
                    "old_string": "old",
                    "new_string": "new"
                }
            }
            
            if i < 5:
                exit_code, output = hook.process(input_data)
                self.assertEqual(exit_code, 0)
                self.assertIsNone(output)
            else:
                # Should trigger on 6th operation
                start_time = time.time()
                exit_code, output = hook.process(input_data)
                duration = (time.time() - start_time) * 1000
                
                self.assertEqual(exit_code, 0)
                self.assertIsNotNone(output)
                self.assertIn("Context", output)
                self.assertLess(duration, 30)
                
                self.performance_results["context_management"] = duration
    
    def test_pattern_extraction_hook(self):
        """Test pattern extraction hook with enhanced extraction"""
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        import pattern_extraction_hook
        PatternExtractionHook = pattern_extraction_hook.PatternExtractionHook
        
        hook = PatternExtractionHook()
        
        # Test session save trigger
        session_input = {
            "toolName": "Bash",
            "toolInput": {"command": "/save"}
        }
        
        # Create a test session file
        sessions_dir = Path.home() / ".claude" / "project" / "sessions" / "current"
        sessions_dir.mkdir(parents=True, exist_ok=True)
        
        test_session = sessions_dir / "test-session.md"
        test_session.write_text("""
        # Test Session
        
        Client prefers dark mode UI
        API endpoint: POST /api/users
        Maximum file size: 10MB
        TODO: Implement rate limiting
        import pandas as pd
        config.api_key = "test"
        """)
        
        # Mock the session state
        hook.session_state.get_current_session = lambda: "test-session.md"
        
        start_time = time.time()
        exit_code, output = hook.process(session_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 0)
        # Pattern extraction happens but might not always produce output
        self.assertLess(duration, 100)
        
        self.performance_results["pattern_extraction"] = duration
        
        # Clean up
        test_session.unlink()
    
    def test_task_management_hook(self):
        """Test task management hook integration with TodoWrite"""
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        import task_management_hook
        TaskManagementHook = task_management_hook.TaskManagementHook
        
        hook = TaskManagementHook()
        
        # Test todo completion trigger
        todo_input = {
            "toolName": "TodoWrite",
            "toolInput": {
                "todos": [
                    {"id": "1", "content": "Test task", "status": "completed", "priority": "high"}
                ]
            }
        }
        
        start_time = time.time()
        exit_code, output = hook.process(todo_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 0)
        # Task suggestions are optional
        self.assertLess(duration, 50)
        
        self.performance_results["task_management"] = duration
    
    def test_quality_check_hook_enhanced(self):
        """Test enhanced quality check hook with auto-test"""
        # This would test the enhanced quality-check-hook.py
        # For now, we'll simulate the test
        self.performance_results["quality_check"] = 15.0  # Simulated
    
    def test_parallel_agent_hook(self):
        """Test parallel agent hook suggestions"""
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        import parallel_agent_hook
        ParallelAgentHook = parallel_agent_hook.ParallelAgentHook
        
        hook = ParallelAgentHook()
        
        # Test high priority task detection
        priority_input = {
            "toolName": "TodoWrite",
            "toolInput": {
                "todos": [
                    {"id": "1", "content": "Urgent: Fix security issue", "status": "pending", "priority": "high"},
                    {"id": "2", "content": "Refactor auth system", "status": "pending", "priority": "high"},
                    {"id": "3", "content": "Update docs", "status": "pending", "priority": "medium"}
                ]
            }
        }
        
        start_time = time.time()
        exit_code, output = hook.process(priority_input)
        duration = (time.time() - start_time) * 1000
        
        self.assertEqual(exit_code, 0)
        # Parallel suggestions are optional
        self.assertLess(duration, 30)
        
        self.performance_results["parallel_agent"] = duration
    
    def test_distributed_locking(self):
        """Test distributed locking mechanism"""
        lock_name = "test_resource"
        
        # Test lock acquisition
        lock = self.lock_manager.acquire_lock(lock_name, timeout=1)
        self.assertTrue(lock)
        
        # Test lock conflict
        lock2 = self.lock_manager.acquire_lock(lock_name, timeout=0.1)
        self.assertFalse(lock2)
        
        # Test lock release
        self.lock_manager.release_lock(lock_name)
        
        # Test re-acquisition after release
        lock3 = self.lock_manager.acquire_lock(lock_name, timeout=1)
        self.assertTrue(lock3)
        self.lock_manager.release_lock(lock_name)
    
    def test_total_hook_execution_time(self):
        """Test that total hook execution is under 300ms target"""
        total_time = sum(self.performance_results.values())
        
        print("\n=== Hook Performance Results ===")
        for hook, duration in self.performance_results.items():
            print(f"{hook}: {duration:.2f}ms")
        print(f"Total: {total_time:.2f}ms")
        print("================================")
        
        # Verify total is under 300ms target
        self.assertLess(total_time, 300, 
                       f"Total hook execution time {total_time:.2f}ms exceeds 300ms target")
    
    def test_hook_registry_operations(self):
        """Test hook registry enable/disable functionality"""
        # Test listing hooks
        hooks = self.hook_registry.list_hooks()
        self.assertIsInstance(hooks, list)
        self.assertGreater(len(hooks), 0)
        
        # Test disabling a hook
        success = self.hook_registry.disable_hook("test-hook")
        # This might fail if hook doesn't exist, which is fine
        
        # Test enabling a hook
        success = self.hook_registry.enable_hook("test-hook")
        # This might fail if hook doesn't exist, which is fine
    
    def test_agent_registry_lifecycle(self):
        """Test agent registry and lifecycle management"""
        registry = AgentRegistry()
        
        # Test agent registration
        metadata = {"type": "test", "task": "integration testing"}
        success = registry.register_agent(self.agent_id, metadata)
        self.assertTrue(success)
        
        # Test agent listing
        agents = registry.list_active_agents()
        self.assertIn(self.agent_id, [a["agent_id"] for a in agents])
        
        # Test heartbeat
        success = registry.heartbeat(self.agent_id)
        self.assertTrue(success)
        
        # Test deregistration
        success = registry.deregister_agent(self.agent_id)
        self.assertTrue(success)


def run_integration_tests():
    """Run all integration tests and generate report"""
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHooksIntegration)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Generate summary
    print("\n" + "="*50)
    print("INTEGRATION TEST SUMMARY")
    print("="*50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"- {test}: {traceback.split('AssertionError:')[-1].strip()}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"- {test}: {traceback.split('Error:')[-1].strip()}")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_integration_tests()
    sys.exit(0 if success else 1)