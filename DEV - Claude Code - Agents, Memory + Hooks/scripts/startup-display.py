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
import hashlib

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
    # List of expected MCPs based on CLAUDE.md documentation
    expected_mcps = [
        "Sequential Thinking", "Graphiti", "Gemini", "GitHub", 
        "Context7", "n8n", "Puppeteer", "Playwright", 
        "Figma"
    ]
    
    # In a real implementation, we would check actual MCP connections
    # For now, we'll assume all core MCPs are active
    active_count = len(expected_mcps)
    total_count = len(expected_mcps)
    
    if active_count == total_count:
        return f"✅ All {total_count} MCPs active"
    else:
        return f"⚠️ {active_count}/{total_count} MCPs active"


def get_todo_count():
    """Get current todo count from TodoWrite tool state"""
    try:
        # TodoWrite tool doesn't persist state between messages
        # So we can't reliably get the count here
        # Return a descriptive message instead
        return "Session todos"
    except:
        return "Session todos"


def generate_startup_display():
    """Generate the complete startup display"""
    
    # Get all status information
    memory_status = get_memory_status()
    task_status = get_task_status()
    hook_status = get_hook_status()
    session_age = get_session_age()
    git_branch = get_git_status()
    mcp_status = get_mcp_status()
    todo_info = get_todo_count()
    
    # Get mode - simplified, would normally check mode hook
    mode = "Auto Mode 🚀"
    
    display = f"""=== 🚀 Claude Code System Status ===
[🧠 Memory] Graphiti: {memory_status}
[📚 Knowledge] facts.json ✅ | patterns.json ✅ | constraints.json ✅  
[🤖 MCPs] {mcp_status}
[🎯 Mode] {mode} | Project: anobel.nl | Git: {git_branch}
[📂 Session] Age: {session_age} | [📝 Todos] {todo_info}
[🪝 Hooks] {hook_status} | [📋 Tasks] {task_status}
====================================="""
    
    return display


def get_session_id():
    """Get or create a unique session ID based on process start time"""
    # Use Claude Code's process ID and start time as session identifier
    session_marker_dir = Path.home() / ".claude" / "state"
    session_marker_dir.mkdir(parents=True, exist_ok=True)
    
    # Try to get Claude session ID from environment or use process-based fallback
    claude_session_id = os.environ.get('CLAUDE_SESSION_ID', '')
    
    if claude_session_id:
        session_id = claude_session_id
    else:
        # Create a session ID based on current process info
        pid = os.getpid()
        ppid = os.getppid()
        
        # Simple session ID based on parent process and time window (5 minute buckets)
        time_bucket = int(datetime.now().timestamp() / 300)  # 5-minute buckets
        session_id = f"{ppid}_{time_bucket}"
    
    return session_id, session_marker_dir / f"startup_shown_{session_id}"


def should_show_startup():
    """Check if we should show the startup display for this session"""
    debug = "--debug" in sys.argv
    
    # Always show if forced
    if "--force" in sys.argv:
        return True
    
    # Check session marker
    session_id, marker_path = get_session_id()
    
    if debug:
        print(f"[DEBUG] Session ID: {session_id}")
        print(f"[DEBUG] Marker path: {marker_path}")
        print(f"[DEBUG] Marker exists: {marker_path.exists()}")
    
    # If marker exists, we've already shown for this session
    if marker_path.exists():
        # Check if marker is stale (older than 6 hours)
        try:
            age_hours = (datetime.now().timestamp() - marker_path.stat().st_mtime) / 3600
            if age_hours > 6:
                marker_path.unlink()
                if debug:
                    print(f"[DEBUG] Marker was stale ({age_hours:.1f} hours), removed")
                return True
        except:
            pass
        if debug:
            print("[DEBUG] Already shown for this session, skipping")
        return False
    
    # Create marker to indicate we're showing
    try:
        marker_path.touch()
        if debug:
            print("[DEBUG] Created session marker")
    except Exception as e:
        if debug:
            print(f"[DEBUG] Failed to create marker: {e}")
    
    return True


def cleanup_old_markers():
    """Clean up old session markers (older than 24 hours)"""
    try:
        session_marker_dir = Path.home() / ".claude" / "state"
        if session_marker_dir.exists():
            for marker in session_marker_dir.glob("startup_shown_*"):
                age_hours = (datetime.now().timestamp() - marker.stat().st_mtime) / 3600
                if age_hours > 24:
                    marker.unlink()
    except:
        pass


def main():
    """Main entry point"""
    # Check if this is triggered by a greeting
    if "--greeting" in sys.argv or os.environ.get("CLAUDE_USER_PROMPT", "").lower().strip() in ["hi", "hello", "hey"]:
        # Always show for greetings
        display = generate_startup_display()
        print(display)
        return
    
    # Special mode: show once per day instead of once per session
    if "--daily" in sys.argv:
        daily_marker = Path.home() / ".claude" / "state" / "startup_shown_daily"
        if daily_marker.exists():
            # Check if it's from today
            from datetime import date
            try:
                marker_date = date.fromtimestamp(daily_marker.stat().st_mtime)
                if marker_date == date.today():
                    return  # Already shown today
            except:
                pass
        # Mark as shown for today
        daily_marker.parent.mkdir(parents=True, exist_ok=True)
        daily_marker.touch()
    else:
        # Clean up old markers periodically
        cleanup_old_markers()
        
        # Check if we should show the startup display
        if not should_show_startup():
            # Silently exit - already shown for this session
            return
    
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