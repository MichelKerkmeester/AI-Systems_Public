#!/usr/bin/env python3
"""
Greeting Detection Hook
Shows system status when user says hi/hello/hey
"""

import json
import sys
import subprocess
import os
from pathlib import Path
from datetime import datetime

# Create a log entry immediately to verify the hook is called
try:
    with open('/tmp/greeting_hook_called.log', 'a') as f:
        f.write(f"{datetime.now().isoformat()} - Greeting hook started\n")
except:
    pass

def main():
    # Debug mode - set CLAUDE_HOOK_DEBUG=1 to enable
    debug = os.environ.get('CLAUDE_HOOK_DEBUG', '0') == '1'
    
    # Read input from stdin
    try:
        raw_input = sys.stdin.read()
        # Always log raw input for debugging
        with open('/tmp/greeting_hook_raw.log', 'a') as f:
            f.write(f"{datetime.now().isoformat()} - Raw input: {repr(raw_input)}\n")
        
        input_data = json.loads(raw_input)
    except json.JSONDecodeError as e:
        with open('/tmp/greeting_hook_debug.log', 'a') as f:
            f.write(f"{datetime.now().isoformat()} - Failed to parse JSON: {e}\n")
            f.write(f"{datetime.now().isoformat()} - Raw input was: {repr(raw_input)}\n")
        sys.exit(0)
    
    # Extract prompt text
    prompt = input_data.get("params", {}).get("messages", [{}])[-1].get("content", "").strip().lower()
    
    if debug:
        with open('/tmp/greeting_hook_debug.log', 'a') as f:
            f.write(f"{datetime.now().isoformat()} - Received prompt: '{prompt}'\n")
            f.write(f"{datetime.now().isoformat()} - Full input: {json.dumps(input_data, indent=2)}\n")
    
    # Check if it's a greeting
    greetings = ["hi", "hello", "hey", "greetings", "howdy", "yo"]
    
    # Only trigger on exact match greetings (to avoid false positives)
    if prompt in greetings or (len(prompt) < 20 and any(g in prompt for g in greetings)):
        if debug:
            with open('/tmp/greeting_hook_debug.log', 'a') as f:
                f.write(f"{datetime.now().isoformat()} - Greeting detected! Running startup display\n")
        
        # Run the startup display with greeting flag
        startup_script = Path(__file__).parent / "startup-display.py"
        if startup_script.exists():
            result = subprocess.run([sys.executable, str(startup_script), "--greeting"], 
                                  capture_output=True, text=True)
            
            if debug:
                with open('/tmp/greeting_hook_debug.log', 'a') as f:
                    f.write(f"{datetime.now().isoformat()} - Startup script result: {result.returncode}\n")
                    f.write(f"{datetime.now().isoformat()} - Stdout: {result.stdout}\n")
                    f.write(f"{datetime.now().isoformat()} - Stderr: {result.stderr}\n")
            
            # Print the output so Claude sees it
            if result.stdout:
                print(result.stdout)
    
    # Exit without output (hooks should be silent unless they have messages)
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Log any errors
        try:
            with open('/tmp/greeting_hook_error.log', 'a') as f:
                f.write(f"{datetime.now().isoformat()} - Error: {str(e)}\n")
                import traceback
                f.write(traceback.format_exc())
        except:
            pass
        sys.exit(1)