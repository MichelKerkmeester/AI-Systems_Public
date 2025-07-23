#!/usr/bin/env python3
"""
Status command - Shows system status display

Usage:
    /status         - Show system status
    /status --json  - Show status as JSON
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Execute the status command"""
    # Path to startup display script
    script_path = Path(__file__).resolve().parents[2] / "logic" / "scripts" / "startup-display.py"
    
    # Build command with force flag to always show
    cmd = [sys.executable, str(script_path), "--force"]
    
    # Add JSON flag if requested
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        cmd.append("--json")
    
    # Execute the script
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error showing status: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()