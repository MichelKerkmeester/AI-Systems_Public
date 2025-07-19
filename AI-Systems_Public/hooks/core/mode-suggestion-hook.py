#!/usr/bin/env python3
"""
Mode Suggestion Hook for Claude Code
Analyzes user queries and suggests appropriate modes
"""

import json
import sys
import os
import subprocess

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

try:
    from mode_manager import ModeManager
except ImportError:
    # Fallback if import fails
    print(json.dumps({"messages": [{"role": "text", "content": "Mode system temporarily unavailable"}]}))
    sys.exit(0)

def get_git_context():
    """Get current git context"""
    try:
        # Get current branch
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        current_branch = branch_result.stdout.strip()
        
        # Get modified file count
        status_result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        modified_files = len(status_result.stdout.strip().split('\n')) if status_result.stdout.strip() else 0
        
        return {
            "git_branch": current_branch,
            "modified_files": modified_files
        }
    except:
        return {}

def main():
    # Read input from stdin
    try:
        input_data = json.loads(sys.stdin.read())
    except json.JSONDecodeError:
        sys.exit(0)
    
    # Extract prompt text
    prompt = input_data.get("params", {}).get("messages", [{}])[-1].get("content", "")
    if not prompt:
        sys.exit(0)
    
    # Initialize mode manager
    manager = ModeManager()
    
    # Get git context
    context = get_git_context()
    
    # Analyze query for mode suggestion
    suggestion = manager.suggest_mode(prompt, context)
    
    # Build response messages
    messages = []
    
    # Add mode suggestion if different from current
    if suggestion["suggested"] and suggestion["require_approval"]:
        mode_icons = {
            "strict": "🔒",
            "auto": "🚀",
            "hybrid": "⚖️"
        }
        
        current_icon = mode_icons.get(suggestion["current"], "")
        suggested_icon = mode_icons.get(suggestion["suggested"], "")
        
        suggestion_msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 MODE SUGGESTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current Mode: {current_icon} {suggestion['current'].capitalize()}
Suggested Mode: {suggested_icon} {suggestion['suggested'].capitalize()}
Reason: {suggestion['reason']}

Would you like to switch to {suggestion['suggested']} mode? 
• Type '/mode {suggestion['suggested']}' to switch
• Type '/mode manual' to disable suggestions
• Or continue in {suggestion['current']} mode

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        messages.append({
            "role": "text",
            "content": suggestion_msg
        })
    
    # Always add current mode status
    mode_status = manager.format_mode_status()
    messages.append({
        "role": "text", 
        "content": mode_status
    })
    
    # Check if this is a mode command
    if prompt.strip().startswith("/mode") or prompt.strip().startswith("/m"):
        # Let the main system handle the command
        sys.exit(0)
    
    # Output response
    if messages:
        print(json.dumps({"messages": messages}))
    
    sys.exit(0)

if __name__ == "__main__":
    main()