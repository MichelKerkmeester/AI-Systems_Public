#!/usr/bin/env python3
"""Comprehensive test of session management hook functionality"""

import json
import subprocess
import sys
import os
import shutil
from datetime import datetime, timezone, timedelta

# Test scenarios for description extraction
description_tests = [
    {
        "name": "Git commit",
        "input": {"tool": "Bash", "arguments": {"command": "git commit -m 'Fix bug'"}},
        "expected": "git-commit"
    },
    {
        "name": "Git push",
        "input": {"tool": "Bash", "arguments": {"command": "git push origin main"}},
        "expected": "git-push"
    },
    {
        "name": "NPM install",
        "input": {"tool": "Bash", "arguments": {"command": "npm install --save-dev jest"}},
        "expected": "package-management"
    },
    {
        "name": "Run tests",
        "input": {"tool": "Bash", "arguments": {"command": "npm test"}},
        "expected": "testing"
    },
    {
        "name": "Edit file with dashes",
        "input": {"tool": "Edit", "arguments": {"file_path": "/src/session-manager-utils.js"}},
        "expected": "session-manager"
    },
    {
        "name": "Write new file",
        "input": {"tool": "Write", "arguments": {"file_path": "/src/auth_handler.py"}},
        "expected": "auth-handler"
    },
    {
        "name": "Todo with multiple words",
        "input": {"tool": "TodoWrite", "arguments": {"todos": [{"content": "Refactor authentication system for better security"}]}},
        "expected": "refactor-authentication"
    }
]

def setup_old_session():
    """Create an old session to trigger timeout"""
    session_file = ".claude/project/sessions/.current-session"
    old_time = datetime.now(timezone.utc) - timedelta(hours=5)
    session_data = {
        "name": "old-session.md",
        "created_at": old_time.isoformat(),
        "description": "old"
    }
    with open(session_file, 'w') as f:
        json.dump(session_data, f)

def cleanup_sessions():
    """Clean up test sessions"""
    current_dir = ".claude/project/sessions/current"
    if os.path.exists(current_dir):
        for file in os.listdir(current_dir):
            if file.startswith("2025-07-18") and file != "2025-07-18-103200-session-enhancements-complete.md":
                os.remove(os.path.join(current_dir, file))

def run_hook(input_data):
    """Run the session hook and return result"""
    hook_path = ".claude/logic/session/hooks/session-management-hook.py"
    result = subprocess.run(
        [sys.executable, hook_path],
        input=json.dumps(input_data),
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        return None, result.stderr
        
    try:
        return json.loads(result.stdout), None
    except json.JSONDecodeError:
        return None, f"Invalid JSON: {result.stdout}"

def test_description_extraction():
    """Test that descriptions are extracted correctly"""
    print("🧪 Testing Description Extraction")
    print("=" * 50)
    
    for test in description_tests:
        print(f"\n📋 Test: {test['name']}")
        
        # Setup old session
        setup_old_session()
        
        # Run hook
        output, error = run_hook(test['input'])
        
        if error:
            print(f"   ❌ Error: {error}")
            continue
            
        if "feedback" in output and "new session created" in output["feedback"].lower():
            # Extract description from feedback
            feedback = output["feedback"]
            if "-" in feedback:
                parts = feedback.split("-")
                if len(parts) >= 3:
                    description = "-".join(parts[3:]).strip()
                    if description == test['expected']:
                        print(f"   ✅ Description '{description}' matches expected")
                    else:
                        print(f"   ❌ Description '{description}' doesn't match expected '{test['expected']}'")
                else:
                    print(f"   ❌ Could not extract description from: {feedback}")
            else:
                print(f"   ❌ Unexpected feedback format: {feedback}")
        else:
            print(f"   ❌ No session created")

def test_excluded_tools():
    """Test that excluded tools don't trigger session creation"""
    print("\n\n🧪 Testing Excluded Tools")
    print("=" * 50)
    
    excluded_tools = ["Read", "LS", "Grep", "Glob"]
    
    for tool in excluded_tools:
        print(f"\n📋 Test: {tool}")
        
        # Setup old session
        setup_old_session()
        
        # Create test input
        test_input = {"tool": tool, "arguments": {}}
        
        # Run hook
        output, error = run_hook(test_input)
        
        if error:
            print(f"   ❌ Error: {error}")
            continue
            
        if output.get("action") == "continue" and "feedback" not in output:
            print(f"   ✅ Tool excluded (no session created)")
        else:
            print(f"   ❌ Unexpected result: {output}")

def test_session_within_timeout():
    """Test that sessions within timeout don't create new ones"""
    print("\n\n🧪 Testing Session Within Timeout")
    print("=" * 50)
    
    # Create recent session
    session_file = ".claude/project/sessions/.current-session"
    recent_time = datetime.now(timezone.utc) - timedelta(hours=2)
    session_data = {
        "name": "recent-session.md",
        "created_at": recent_time.isoformat(),
        "description": "recent"
    }
    with open(session_file, 'w') as f:
        json.dump(session_data, f)
    
    # Test a command
    test_input = {"tool": "Bash", "arguments": {"command": "echo test"}}
    output, error = run_hook(test_input)
    
    if error:
        print(f"   ❌ Error: {error}")
    elif output.get("action") == "continue" and "feedback" not in output:
        print(f"   ✅ No new session created (within timeout)")
    else:
        print(f"   ❌ Unexpected result: {output}")

if __name__ == "__main__":
    # Run all tests
    test_description_extraction()
    test_excluded_tools()
    test_session_within_timeout()
    
    # Cleanup
    print("\n\n🧹 Cleaning up test sessions...")
    cleanup_sessions()
    print("✅ Done!")