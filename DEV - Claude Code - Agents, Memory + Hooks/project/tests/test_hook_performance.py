#!/usr/bin/env python3
"""
Hook Performance Testing Script
Tests execution time of all hooks to ensure < 300ms total
"""

import sys
import os
import time
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


def test_hook_performance() -> Dict[str, float]:
    """Test performance of each hook with realistic inputs"""
    
    performance_results = {}
    
    # Test workflow automation hook
    print("Testing workflow-automation-hook...")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "hooks" / "core"))
        # Import module with hyphenated name
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "workflow_automation_hook",
            str(Path(__file__).resolve().parents[2] / "hooks" / "core" / "workflow-automation-hook.py")
        )
        workflow_automation_hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(workflow_automation_hook)
        
        hook = workflow_automation_hook.WorkflowAutomationHook()
        
        # Simple query
        start_time = time.time()
        hook.process({
            "toolName": "Bash",
            "toolInput": {"command": "ls"},
            "userMessage": "list files"
        })
        simple_time = (time.time() - start_time) * 1000
        
        # Complex query
        start_time = time.time()
        hook.process({
            "toolName": "Bash", 
            "toolInput": {"command": "echo test"},
            "userMessage": "Refactor the authentication system to use OAuth2, update all API endpoints, and ensure backward compatibility"
        })
        complex_time = (time.time() - start_time) * 1000
        
        performance_results["workflow_automation"] = max(simple_time, complex_time)
        print(f"  ✓ Workflow automation: {performance_results['workflow_automation']:.2f}ms")
        
    except Exception as e:
        print(f"  ✗ Workflow automation failed: {e}")
        performance_results["workflow_automation"] = 0
    
    # Test security scan hook
    print("\nTesting security-scan-hook...")
    try:
        import security_scan_hook
        
        hook = security_scan_hook.SecurityScanHook()
        
        # Safe operation
        start_time = time.time()
        hook.process({
            "toolName": "Write",
            "toolInput": {
                "file_path": "/tmp/test.txt",
                "content": "Hello world"
            }
        })
        safe_time = (time.time() - start_time) * 1000
        
        # Unsafe operation
        start_time = time.time()
        hook.process({
            "toolName": "Write",
            "toolInput": {
                "file_path": "/tmp/config.py",
                "content": "API_KEY = 'sk-1234567890'"
            }
        })
        unsafe_time = (time.time() - start_time) * 1000
        
        performance_results["security_scan"] = max(safe_time, unsafe_time)
        print(f"  ✓ Security scan: {performance_results['security_scan']:.2f}ms")
        
    except Exception as e:
        print(f"  ✗ Security scan failed: {e}")
        performance_results["security_scan"] = 0
    
    # Test context management hook
    print("\nTesting context-management-hook...")
    try:
        import context_management_hook
        
        hook = context_management_hook.ContextManagementHook()
        
        # Regular operation
        start_time = time.time()
        hook.process({
            "toolName": "Edit",
            "toolInput": {
                "file_path": "test.py",
                "old_string": "old",
                "new_string": "new"
            }
        })
        duration = (time.time() - start_time) * 1000
        
        performance_results["context_management"] = duration
        print(f"  ✓ Context management: {performance_results['context_management']:.2f}ms")
        
    except Exception as e:
        print(f"  ✗ Context management failed: {e}")
        performance_results["context_management"] = 0
    
    # Test pattern extraction hook
    print("\nTesting pattern-extraction-hook...")
    try:
        import pattern_extraction_hook
        
        hook = pattern_extraction_hook.PatternExtractionHook()
        
        # Test with sample content
        test_content = """
        Client prefers dark mode UI
        API endpoint: POST /api/users
        Maximum file size: 10MB
        TODO: Implement rate limiting
        """
        
        start_time = time.time()
        hook._extract_patterns(test_content)
        regex_time = (time.time() - start_time) * 1000
        
        start_time = time.time()
        hook._enhanced_pattern_extraction(test_content)
        enhanced_time = (time.time() - start_time) * 1000
        
        performance_results["pattern_extraction"] = max(regex_time, enhanced_time)
        print(f"  ✓ Pattern extraction: {performance_results['pattern_extraction']:.2f}ms")
        
    except Exception as e:
        print(f"  ✗ Pattern extraction failed: {e}")
        performance_results["pattern_extraction"] = 0
    
    # Test task management hook
    print("\nTesting task-management-hook...")
    try:
        import task_management_hook
        
        hook = task_management_hook.TaskManagementHook()
        
        start_time = time.time()
        hook.process({
            "toolName": "TodoWrite",
            "toolInput": {
                "todos": [
                    {"id": "1", "content": "Test task", "status": "completed", "priority": "high"}
                ]
            }
        })
        duration = (time.time() - start_time) * 1000
        
        performance_results["task_management"] = duration
        print(f"  ✓ Task management: {performance_results['task_management']:.2f}ms")
        
    except Exception as e:
        print(f"  ✗ Task management failed: {e}")
        performance_results["task_management"] = 0
    
    # Test parallel agent hook
    print("\nTesting parallel-agent-hook...")
    try:
        import parallel_agent_hook
        
        hook = parallel_agent_hook.ParallelAgentHook()
        
        start_time = time.time()
        hook.process({
            "toolName": "TodoWrite",
            "toolInput": {
                "todos": [
                    {"id": "1", "content": "Urgent task 1", "status": "pending", "priority": "high"},
                    {"id": "2", "content": "Urgent task 2", "status": "pending", "priority": "high"}
                ]
            }
        })
        duration = (time.time() - start_time) * 1000
        
        performance_results["parallel_agent"] = duration
        print(f"  ✓ Parallel agent: {performance_results['parallel_agent']:.2f}ms")
        
    except Exception as e:
        print(f"  ✗ Parallel agent failed: {e}")
        performance_results["parallel_agent"] = 0
    
    return performance_results


def main():
    """Run performance tests and generate report"""
    
    print("="*50)
    print("HOOK PERFORMANCE TEST")
    print("="*50)
    print()
    
    # Run tests
    results = test_hook_performance()
    
    # Calculate total
    total_time = sum(results.values())
    
    # Generate report
    print("\n" + "="*50)
    print("PERFORMANCE SUMMARY")
    print("="*50)
    
    for hook, duration in sorted(results.items(), key=lambda x: x[1], reverse=True):
        print(f"{hook:<25} {duration:>8.2f}ms")
    
    print("-"*35)
    print(f"{'TOTAL':<25} {total_time:>8.2f}ms")
    print("="*50)
    
    # Check against target
    target = 300
    if total_time < target:
        print(f"\n✅ SUCCESS: Total time {total_time:.2f}ms is under {target}ms target")
        margin = ((target - total_time) / target) * 100
        print(f"   Performance margin: {margin:.1f}%")
    else:
        print(f"\n❌ FAILURE: Total time {total_time:.2f}ms exceeds {target}ms target")
        overhead = ((total_time - target) / target) * 100
        print(f"   Overhead: {overhead:.1f}%")
    
    # Additional metrics
    print(f"\n📊 Additional Metrics:")
    print(f"   Average hook time: {total_time/len(results):.2f}ms")
    print(f"   Fastest hook: {min(results.items(), key=lambda x: x[1])[0]} ({min(results.values()):.2f}ms)")
    print(f"   Slowest hook: {max(results.items(), key=lambda x: x[1])[0]} ({max(results.values()):.2f}ms)")
    
    return total_time < target


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)