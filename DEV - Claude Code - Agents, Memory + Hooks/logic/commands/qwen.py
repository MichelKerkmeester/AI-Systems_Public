#!/usr/bin/env python3
"""
QWEN command for Claude Code CLI
Usage: /qwen [task]
"""

import os
import sys
import json
import subprocess
from pathlib import Path

def execute_qwen(prompt: str):
    """Execute QWEN via Hyperbolic"""
    
    # Path to QWEN script
    script_path = Path(__file__).parent.parent / "scripts" / "qwen-hyperbolic.py"
    
    # Check if API key is set
    if not os.getenv('HYPERBOLIC_API_KEY'):
        print("Error: HYPERBOLIC_API_KEY not set!")
        print("\nSetup instructions:")
        print("1. Sign up at https://app.hyperbolic.ai")
        print("2. Get your API key")
        print("3. Export it: export HYPERBOLIC_API_KEY='your-key-here'")
        return
    
    # Execute QWEN
    try:
        result = subprocess.run(
            [sys.executable, str(script_path), prompt],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("Error: Request timed out after 120 seconds")
    except Exception as e:
        print(f"Error executing QWEN: {e}")

def main():
    """Main entry point for /qwen command"""
    
    # Get the prompt from command line
    if len(sys.argv) < 2:
        print("QWEN Command - Use QWEN 3 Coder via Hyperbolic")
        print("=" * 50)
        print("\nUsage:")
        print("  /qwen [task]              - Run a task with QWEN")
        print("  /qwen help               - Show this help")
        print("  /qwen setup              - Setup instructions")
        print("\nExamples:")
        print("  /qwen 'Write a Python function to validate emails'")
        print("  /qwen 'Optimize this React component for performance'")
        print("  /qwen 'Implement a binary search algorithm'")
        print("\nModel: Qwen3-Coder-480B-A35B-Instruct (262k context)")
        print("Performance: On par with Claude Sonnet 3.5")
        return
    
    command = sys.argv[1].lower()
    
    if command == "help":
        main()  # Show help
    elif command == "setup":
        print("QWEN Setup Instructions")
        print("=" * 50)
        print("\n1. Sign up at https://app.hyperbolic.ai")
        print("2. Navigate to API Keys section")
        print("3. Generate a new API key")
        print("4. Add to your shell profile:")
        print("   export HYPERBOLIC_API_KEY='your-api-key-here'")
        print("5. Restart your terminal or run: source ~/.zshrc")
        print("\nThen you can use: /qwen 'Your task here'")
    else:
        # Join all arguments as the prompt
        prompt = ' '.join(sys.argv[1:])
        execute_qwen(prompt)

if __name__ == "__main__":
    main()