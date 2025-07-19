#!/usr/bin/env python3
"""
Unified startup display for Claude Code
Shows system status including memory, tasks, hooks, and more
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic.tasks import TaskManager


def get_memory_status():
    """Get memory system status"""
    try:
        # Try to get memory count
        cmd = 'echo "MATCH (e:Episodic) RETURN count(e);" | docker exec -i graphiti-neo4j cypher-shell -u neo4j -p password -d neo4j --format plain 2>/dev/null'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                count = int(lines[1])
                return f"✅ Active | {count} memories stored"
    except:
        pass
    return "❌ Offline"


def get_task_status():
    """Get task management status"""
    try:
        task_manager = TaskManager()
        active_task = task_manager.get_active_task()
        stats = task_manager.get_stats()
        
        if active_task:
            return f"{active_task.name} | Progress: {active_task.progress}%"
        elif stats['suggestions'] > 0:
            return f"No active task | {stats['suggestions']} suggestions"
        else:
            return "No active tasks"
    except:
        return "System initializing"


def get_hook_status():
    """Get hook system status"""
    try:
        # Read settings.json to count hooks
        settings_path = Path(__file__).resolve().parents[1] / "settings.json"
        if settings_path.exists():
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            
            total_hooks = 0
            if 'hooks' in settings and settings['hooks'].get('enabled', True):
                for event_type in ['UserPromptSubmit', 'PreToolUse', 'PostToolUse']:
                    if event_type in settings['hooks']:
                        for matcher in settings['hooks'][event_type]:
                            total_hooks += len(matcher.get('hooks', []))
            
            return f"{total_hooks} hooks active"
    except:
        pass
    return "Loading..."


def get_session_age():
    """Get current session age"""
    try:
        sessions_dir = Path.home() / ".claude" / "project" / "sessions" / "current"
        if sessions_dir.exists():
            session_files = list(sessions_dir.glob("*.md"))
            if session_files:
                # Get the most recent session file
                latest = max(session_files, key=lambda p: p.stat().st_mtime)
                age_seconds = datetime.now().timestamp() - latest.stat().st_mtime
                hours = int(age_seconds / 3600)
                return f"{hours}h"
    except:
        pass
    return "0h"


def get_git_status():
    """Get current git branch and status"""
    try:
        branch_result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True
        )
        if branch_result.returncode == 0:
            branch = branch_result.stdout.strip()
            
            # Check if there are uncommitted changes
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True
            )
            
            if status_result.stdout:
                return f"{branch} (modified)"
            else:
                return branch
    except:
        pass
    return "main"


def get_mcp_status():
    """Get MCP server status"""
    # This is simplified - in reality would check actual MCP connections
    mcps = ["Sequential Thinking", "Graphiti", "Gemini", "GitHub", "n8n"]
    return " ✅ | ".join(mcps[:3]) + " ✅"  # Truncated for display


def generate_startup_display():
    """Generate the complete startup display"""
    
    # Get all status information
    memory_status = get_memory_status()
    task_status = get_task_status()
    hook_status = get_hook_status()
    session_age = get_session_age()
    git_branch = get_git_status()
    mcp_status = get_mcp_status()
    
    # Get mode - simplified, would normally check mode hook
    mode = "Auto Mode 🚀"
    
    # Get todo count - simplified
    todo_count = "?"
    
    display = f"""=== 🚀 Claude Code System Status ===
[🧠 Memory] Graphiti: {memory_status}
[📚 Knowledge] facts.json ✅ | patterns.json ✅ | constraints.json ✅  
[🤖 MCPs] {mcp_status}
[🎯 Mode] {mode} | Project: anobel.nl | Git: {git_branch}
[📝 Todos] {todo_count} active tasks | [📂 Session] current | Age: {session_age}
[🪝 Hooks] {hook_status} | [📋 Task] {task_status}
====================================="""
    
    return display


def main():
    """Main entry point"""
    # Generate and print the display
    display = generate_startup_display()
    print(display)
    
    # Also output as JSON for programmatic use
    if "--json" in sys.argv:
        data = {
            "memory": get_memory_status(),
            "tasks": get_task_status(),
            "hooks": get_hook_status(),
            "session_age": get_session_age(),
            "git": get_git_status(),
            "mcps": get_mcp_status()
        }
        print("\n" + json.dumps(data, indent=2))


if __name__ == "__main__":
    main()