#!/usr/bin/env python3
"""
Test script for memory hook functionality
"""

import sys
import json
from pathlib import Path

# Add paths for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

# Import the hook classes directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "memory"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_context_hook import MemoryContextHook
from post_tool_use_memory import PostToolUseMemoryHook


def test_memory_context_hook():
    """Test the memory context hook"""
    print("\n=== Testing Memory Context Hook ===")
    
    hook = MemoryContextHook()
    
    # Test various inputs
    test_cases = [
        "I need to implement authentication for the API",
        "We decided to use JWT tokens for security",
        "The user said they want dark mode support",
        "I learned that webpack 5 has better tree shaking",
        "Fixed the performance issue by optimizing queries",
        "Just checking the weather"  # Should not trigger
    ]
    
    for test_input in test_cases:
        print(f"\nInput: {test_input}")
        
        result_code, output = hook.process({"user_input": test_input})
        
        if output:
            print(f"Output: {output.strip()}")
        else:
            print("No output (no patterns detected)")
            
        # Show detected patterns
        patterns = hook.detect_patterns(test_input)
        if patterns:
            print(f"Patterns detected: {[p[0] for p in patterns]}")


def test_post_tool_use_hook():
    """Test the post tool use memory hook"""
    print("\n\n=== Testing Post Tool Use Memory Hook ===")
    
    hook = PostToolUseMemoryHook()
    
    # Test various tool uses
    test_cases = [
        {
            "tool_name": "Edit",
            "tool_args": {
                "file_path": "/path/to/file.js",
                "old_string": "console.log('debug')",
                "new_string": "// Removed debug statement"
            },
            "result": {"success": True}
        },
        {
            "tool_name": "Bash",
            "tool_args": {
                "command": "npm install axios"
            },
            "result": {"output": "added 5 packages"}
        },
        {
            "tool_name": "mcp__github-mcp-server__create_pull_request",
            "tool_args": {
                "owner": "user",
                "repo": "project",
                "title": "Add authentication system"
            },
            "result": {"pr_number": 123}
        }
    ]
    
    for test_case in test_cases:
        print(f"\nTool: {test_case['tool_name']}")
        
        should_capture = hook.should_capture(
            test_case['tool_name'],
            test_case['tool_args'],
            test_case['result']
        )
        
        print(f"Should capture: {should_capture}")
        
        if should_capture:
            context = hook.extract_operation_context(
                test_case['tool_name'],
                test_case['tool_args'],
                test_case['result']
            )
            
            episode = hook.format_memory_episode(context)
            print(f"Memory episode: {json.dumps(episode, indent=2)}")


if __name__ == "__main__":
    test_memory_context_hook()
    test_post_tool_use_hook()
    
    print("\n\n✅ Hook tests completed!")
    print("\nCurrent settings:")
    settings_path = Path(__file__).parent.parent.parent / "logic" / "memory" / "settings.json"
    with open(settings_path) as f:
        settings = json.load(f)
    print(json.dumps(settings, indent=2))