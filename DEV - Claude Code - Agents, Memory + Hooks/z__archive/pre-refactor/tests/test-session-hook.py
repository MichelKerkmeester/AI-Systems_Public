#!/usr/bin/env python3
"""Test the session management hook functionality"""

import json
import subprocess
import sys
import os

# Test data for different tool scenarios
test_cases = [
    {
        "name": "Git commit command",
        "input": {
            "tool": "Bash",
            "arguments": {"command": "git commit -m 'Fix bug in session manager'"}
        },
        "expected_description": "git-commit"
    },
    {
        "name": "NPM install",
        "input": {
            "tool": "Bash", 
            "arguments": {"command": "npm install axios"}
        },
        "expected_description": "package-management"
    },
    {
        "name": "File edit",
        "input": {
            "tool": "Edit",
            "arguments": {"file_path": "/path/to/session-manager.py"}
        },
        "expected_description": "session-manager"
    },
    {
        "name": "Todo creation",
        "input": {
            "tool": "TodoWrite",
            "arguments": {"todos": [{"content": "Implement new feature", "status": "pending"}]}
        },
        "expected_description": "implement-new"
    },
    {
        "name": "Excluded tool (Read)",
        "input": {
            "tool": "Read",
            "arguments": {"file_path": "/some/file.txt"}
        },
        "expected_description": None  # Should not create session
    }
]

def test_hook():
    """Test the session management hook with various inputs"""
    hook_path = os.path.join(os.path.dirname(__file__), "session-management-hook.py")
    
    print("🧪 Testing Session Management Hook")
    print("=" * 50)
    
    for test in test_cases:
        print(f"\n📋 Test: {test['name']}")
        print(f"   Input: {json.dumps(test['input'], indent=2)}")
        
        # Run the hook
        result = subprocess.run(
            [sys.executable, hook_path],
            input=json.dumps(test['input']),
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"   ❌ Hook failed: {result.stderr}")
            continue
            
        try:
            output = json.loads(result.stdout)
            print(f"   📤 Output: {json.dumps(output, indent=2)}")
            
            if "feedback" in output:
                print(f"   💬 Feedback: {output['feedback']}")
                
            # Check if description matches expected
            if test['expected_description']:
                if "new session" in output.get("feedback", "").lower():
                    print(f"   ✅ New session created (as expected)")
                else:
                    print(f"   ⚠️  Expected new session but got: {output}")
            else:
                if output.get("action") == "continue" and "feedback" not in output:
                    print(f"   ✅ Tool excluded (as expected)")
                else:
                    print(f"   ⚠️  Expected no action but got: {output}")
                    
        except json.JSONDecodeError:
            print(f"   ❌ Invalid JSON output: {result.stdout}")

if __name__ == "__main__":
    test_hook()