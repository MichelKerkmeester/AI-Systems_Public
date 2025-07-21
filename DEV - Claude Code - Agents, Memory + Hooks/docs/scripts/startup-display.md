# startup-display.py

## Overview

**Script Name**: Startup Display Generator  
**Purpose**: Shows comprehensive system status at Claude Code startup  
**Location**: `/scripts/startup-display.py`  
**Performance**: <100ms for full status

## Description

The startup-display.py script generates a unified status display showing memory system status, task management, hooks, MCP servers, Git status, and session information. It provides both human-readable and JSON output formats.

## Usage

### Command Line
```bash
# Show startup display
python3 .claude/logic/scripts/startup-display.py

# Output as JSON
python3 .claude/logic/scripts/startup-display.py --json

# Use in session start
echo "$(python3 .claude/logic/scripts/startup-display.py)"
```

### Options
- `--json` - Output status as JSON instead of formatted display

## Display Format

### Standard Output
```
=== 🚀 Claude Code System Status ===
[🧠 Memory] Graphiti: ✅ Active | 42 memories stored
[📚 Knowledge] facts.json ✅ | patterns.json ✅ | constraints.json ✅  
[🤖 MCPs] Sequential Thinking ✅ | Graphiti ✅ | Gemini ✅
[🎯 Mode] Auto Mode 🚀 | Project: anobel.nl | Git: main
[📝 Todos] 5 active tasks | [📂 Session] current | Age: 2h
[🪝 Hooks] 13 hooks active | [📋 Task] implement-auth | Progress: 45%
=====================================
```

### JSON Output
```json
{
  "memory": "✅ Active | 42 memories stored",
  "tasks": "implement-auth | Progress: 45%",
  "hooks": "13 hooks active",
  "session_age": "2h",
  "git": "main (modified)",
  "mcps": "Sequential Thinking ✅ | Graphiti ✅ | Gemini ✅"
}
```

## Status Components

### Memory Status
```python
def get_memory_status():
    # Queries Graphiti Neo4j for memory count
    # Returns: "✅ Active | X memories stored" or "❌ Offline"
```

Checks:
- Docker container running
- Neo4j connection
- Memory count query

### Task Status
```python
def get_task_status():
    # Uses TaskManager to get active task
    # Returns: "task-name | Progress: X%" or "No active tasks"
```

Shows:
- Active task name
- Progress percentage
- Suggestion count if no active task

### Hook Status
```python
def get_hook_status():
    # Reads settings.json and counts enabled hooks
    # Returns: "X hooks active"
```

Counts hooks across:
- UserPromptSubmit
- PreToolUse
- PostToolUse

### Session Information
```python
def get_session_age():
    # Calculates age of current session
    # Returns: "Xh" (hours since creation)
```

### Git Status
```python
def get_git_status():
    # Gets current branch and modification status
    # Returns: "branch" or "branch (modified)"
```

### MCP Status
Simplified display of MCP server status:
- Sequential Thinking
- Graphiti
- Gemini
- GitHub
- n8n

## Integration Points

### With Session Hook
Called at session start:
```python
# In session-hook.py
display = subprocess.run(
    ["python3", startup_display_path],
    capture_output=True
)
```

### With Memory Hook
Updates when memory system changes:
```python
# In memory-context-hook.py
if memory_updated:
    refresh_startup_display()
```

### With Mode Manager
Reflects current working mode:
```python
# Gets mode from mode-state.json
mode = get_current_mode()
```

## Error Handling

### Graceful Degradation
- **Memory offline**: Shows "❌ Offline"
- **No tasks**: Shows "No active tasks"
- **Git errors**: Defaults to "main"
- **Hook errors**: Shows "Loading..."

### Fallback Values
```python
DEFAULTS = {
    "memory": "❌ Offline",
    "tasks": "System initializing",
    "hooks": "Loading...",
    "session_age": "0h",
    "git": "main",
    "mcps": "Checking..."
}
```

## Performance Optimization

### Strategies
- Parallel status checks
- Cached values for slow operations
- Timeout limits on external calls
- Minimal file I/O

### Benchmarks
- Full display: <100ms
- Memory check: ~50ms
- Task check: ~10ms
- Git check: ~20ms

## Customization

### Display Elements
Control what's shown via environment variables:
```bash
STARTUP_SHOW_MEMORY=false   # Hide memory status
STARTUP_SHOW_TASKS=false    # Hide task status
STARTUP_COMPACT=true        # Use compact format
```

### Custom Formatting
```python
# Override display format
CUSTOM_FORMAT = """
Project: {project}
Status: {git} | {mode}
Tasks: {tasks}
"""
```

## Best Practices

1. **Fast execution**: Keep under 100ms
2. **Error resilience**: Never crash on errors
3. **Clear indicators**: Use ✅/❌ for status
4. **Concise output**: Fit in terminal width
5. **Fresh data**: No caching beyond session

## Troubleshooting

### Display Not Showing
- Check Python path
- Verify script permissions
- Test individual components
- Review error logs

### Incorrect Status
- Verify service connections
- Check file permissions
- Update paths if needed
- Test JSON output

### Performance Issues
- Profile individual checks
- Disable slow components
- Use cached values
- Reduce query complexity

## Examples

### In Hooks
```python
# Show on complex task start
if task_complexity > 3:
    show_startup_display()
```

### In Scripts
```bash
#!/bin/bash
# Show status before operations
python3 .claude/logic/scripts/startup-display.py
echo "---"
# Continue with operations
```

### In Automation
```python
# Refresh display on major changes
def on_major_change():
    refresh_display()
    notify_user()
```

## Related Documentation

- [startup-with-memory.py](./startup-with-memory.md) - Memory-focused variant
- [Session Hook](../hooks/session-hook.md) - Session startup integration
- [System Status Guide](../../logic/system-status.md) - Status monitoring