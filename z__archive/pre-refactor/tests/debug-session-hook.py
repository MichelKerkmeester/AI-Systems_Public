#!/usr/bin/env python3
"""Debug the session management hook"""

import json
import sys
import os
from datetime import datetime, timezone

# Add the hooks directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the hook module
import importlib.util
spec = importlib.util.spec_from_file_location("session_management_hook", 
                                               os.path.join(os.path.dirname(__file__), "session-management-hook.py"))
session_management_hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(session_management_hook)
SessionManagementHook = session_management_hook.SessionManagementHook

def debug_hook():
    """Debug the session management hook"""
    hook = SessionManagementHook()
    
    print("🔍 Debug Session Management Hook")
    print("=" * 50)
    
    # Check settings
    print("\n📋 Settings:")
    print(json.dumps(hook.settings, indent=2))
    
    # Check current session
    print("\n📂 Current Session Info:")
    current = hook.get_current_session_info()
    if current:
        print(json.dumps(current, indent=2))
        
        # Check timeout
        try:
            session_time = datetime.fromisoformat(current.get("created_at", ""))
            now = datetime.now(timezone.utc)
            hours_passed = (now - session_time).total_seconds() / 3600
            print(f"\n⏰ Session age: {hours_passed:.2f} hours")
            print(f"   Timeout threshold: {hook.settings.get('session_timeout_hours', 4)} hours")
            print(f"   Should create new: {hours_passed > hook.settings.get('session_timeout_hours', 4)}")
        except Exception as e:
            print(f"   ❌ Error checking timeout: {e}")
    else:
        print("   No current session found")
    
    # Test a command
    test_input = {
        "tool": "Bash",
        "arguments": {"command": "git commit -m 'Test'"}
    }
    
    print(f"\n🧪 Testing with input:")
    print(json.dumps(test_input, indent=2))
    
    # Check if should create new session
    should_create = hook.should_create_new_session(test_input["tool"])
    print(f"\n📝 Should create new session: {should_create}")
    
    # Process the hook
    result = hook.process_hook(test_input)
    print(f"\n📤 Hook result:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    debug_hook()