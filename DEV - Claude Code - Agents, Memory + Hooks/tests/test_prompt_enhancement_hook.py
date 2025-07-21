#!/usr/bin/env python3
"""
Test script for the prompt enhancement hook
Tests various scenarios to ensure proper functionality
"""

import json
import subprocess
import sys
from pathlib import Path

# Test cases
test_cases = [
    {
        "name": "Simple code generation request",
        "input": {
            "userMessage": "create a function to validate email"
        },
        "expected": {
            "enhanced": True,
            "contains": ["code", "production-ready", "project"]
        }
    },
    {
        "name": "Bypass with raw prefix",
        "input": {
            "userMessage": "raw: just give me a simple email validator"
        },
        "expected": {
            "enhanced": False
        }
    },
    {
        "name": "Command bypass",
        "input": {
            "userMessage": "/memory search email validation"
        },
        "expected": {
            "enhanced": False
        }
    },
    {
        "name": "Simple confirmation",
        "input": {
            "userMessage": "yes"
        },
        "expected": {
            "enhanced": False
        }
    },
    {
        "name": "Complex task request",
        "input": {
            "userMessage": "I need to refactor the authentication system to use JWT tokens"
        },
        "expected": {
            "enhanced": True,
            "contains": ["spec folder", "constraints"]
        }
    },
    {
        "name": "Webflow-specific request",
        "input": {
            "userMessage": "Add animation to the hero section"
        },
        "expected": {
            "enhanced": True,
            "contains": ["Webflow", "platform"]
        }
    },
    {
        "name": "Debug request",
        "input": {
            "userMessage": "Fix the error in the contact form"
        },
        "expected": {
            "enhanced": True,
            "contains": ["identify", "fix", "explanation"]
        }
    }
]

def run_hook(test_input):
    """Run the hook with test input and capture output"""
    hook_path = Path(__file__).parent.parent / "logic" / "hooks" / "core" / "prompt-enhancement-hook.py"
    
    # Run the hook
    process = subprocess.Popen(
        ["python3", str(hook_path)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Send input and get output
    stdout, stderr = process.communicate(input=json.dumps(test_input))
    
    return {
        "exit_code": process.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "input": test_input
    }

def check_enhancement(result, expected):
    """Check if the result matches expected behavior"""
    # Parse the output to see if message was enhanced
    original_message = result["input"]["userMessage"]
    
    # Check exit code (should always be 0 for non-blocking)
    if result["exit_code"] != 0:
        return False, f"Exit code was {result['exit_code']}, expected 0"
    
    # Check if enhancement happened
    if expected["enhanced"]:
        # Should have output indicating enhancement
        if not result["stdout"]:
            return False, "Expected enhancement output but got none"
        
        # Check for expected content
        if "contains" in expected:
            for keyword in expected["contains"]:
                # Note: In real usage, the enhanced prompt is in hook_input["userMessage"]
                # but we can check the output message for indicators
                if keyword.lower() not in result["stdout"].lower():
                    return False, f"Expected keyword '{keyword}' not found in output"
    else:
        # Should not have enhancement output for bypassed prompts
        if result["stdout"] and "Enhanced" in result["stdout"]:
            return False, "Expected no enhancement but got enhancement output"
    
    return True, "Test passed"

def main():
    """Run all tests"""
    print("Testing Prompt Enhancement Hook")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        print(f"Input: {test_case['input']['userMessage']}")
        
        result = run_hook(test_case["input"])
        success, message = check_enhancement(result, test_case["expected"])
        
        if success:
            print(f"✅ PASSED: {message}")
            passed += 1
        else:
            print(f"❌ FAILED: {message}")
            if result["stderr"]:
                print(f"   Error: {result['stderr']}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())