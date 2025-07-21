#!/usr/bin/env python3
"""Simple hook runner for testing"""

import sys
import json
import subprocess

def main():
    # Get the actual hook script
    hook_script = sys.argv[0].replace('run-hook.py', 'code-reuse-validation-hook.py')
    
    # Forward all arguments
    result = subprocess.run(
        [sys.executable, hook_script] + sys.argv[1:],
        capture_output=True,
        text=True
    )
    
    # Output the result
    print(result.stdout)
    
    # Exit with hook's exit code
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()