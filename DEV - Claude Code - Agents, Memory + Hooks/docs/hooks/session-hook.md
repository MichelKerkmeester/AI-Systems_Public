# Session Hook

## Overview

**Hook Name**: Session Hook  
**Purpose**: Manages session lifecycle and automatic archival  
**Location**: `/hooks/session/session-hook.py`  
**Triggers**: PreToolUse and PostToolUse events  
**Priority**: 4 (Session management)  
**Performance**: ~5ms typical execution time

## Description

The Session Hook automatically manages development sessions, creating new sessions, tracking activity, and archiving old sessions after 4 hours of inactivity. It ensures all work is properly documented and retrievable without manual session management.

## Configuration

Settings file: `/hooks/session/session-settings.json`

```json
{
  "auto_archive_after_hours": 4,
  "create_on_startup": true,
  "include_context": true,
  "include_patterns": true,
  "archive_completed_tasks": true,
  "session_name_format": "{timestamp}-{mode}-session"
}
```

## How It Works

1. **Session Creation**:
   - Automatic on Claude startup
   - Named with timestamp and mode
   - Initializes session structure

2. **Activity Tracking**:
   - Monitors all tool usage
   - Records file operations
   - Tracks command history
   - Updates last activity time

3. **Auto-Archival**:
   - Checks activity on each operation
   - Archives after 4 hours inactive
   - Preserves complete session state
   - Creates new session automatically

4. **Session Continuity**:
   - Links related sessions
   - Maintains context across archives
   - Enables session resumption

## Session Structure

```json
{
  "session_id": "2025-01-19-1430-auto-session",
  "created": "2025-01-19T14:30:00Z",
  "last_activity": "2025-01-19T18:45:00Z",
  "mode": "auto",
  "statistics": {
    "duration_hours": 4.25,
    "operations_count": 156,
    "files_modified": 23,
    "todos_completed": 8
  },
  "context": {
    "active_task": "documentation-enhancement",
    "recent_files": ["hooks.md", "tasks.md"],
    "memory_references": ["pattern-123", "fact-456"]
  }
}
```

## Example Usage

### Session Creation
```
🔄 New Session Started
ID: 2025-01-19-1430-auto-session
Mode: Auto
Task: documentation-enhancement

Previous session archived: 2025-01-19-0930-deep-work-session
```

### Activity Updates
The hook silently tracks:
- File reads/writes
- Command executions
- Pattern discoveries
- Task progress

### Auto-Archive Notice
```
📦 Session Auto-Archived

Session: 2025-01-19-0930-deep-work-session
Duration: 4.5 hours
Operations: 203
Files Modified: 31

Reason: 4 hours of inactivity
New Session: 2025-01-19-1430-auto-session
```

## Session Commands

While automatic, manual control available:
- `/save` - Force save current session
- `/save new [name]` - Start new session
- `/save list` - View all sessions
- `/save search [query]` - Find in sessions

## Integration Points

- **Context Management Hook**: Session includes context
- **Pattern Extraction Hook**: Patterns linked to sessions
- **Task Management**: Tasks tracked in sessions
- **Memory System**: Memory references preserved

## Performance Optimization

- Lightweight operation tracking (~5ms)
- Batched session updates
- Async archive operations
- Efficient state management

## Advanced Features

### Session Linking
```json
{
  "session_links": {
    "previous": "2025-01-19-0930-session",
    "related": ["2025-01-18-task-session"],
    "continues": "authentication-implementation"
  }
}
```

### Activity Patterns
```json
{
  "activity_patterns": {
    "peak_hours": [10, 11, 14, 15],
    "common_operations": ["edit", "read", "test"],
    "productivity_score": 0.85
  }
}
```

### Session Templates
```json
{
  "templates": {
    "bug-fix": {
      "name_format": "{timestamp}-bugfix-{issue}",
      "required_context": ["issue_number", "severity"]
    }
  }
}
```

## Troubleshooting

### Sessions Not Creating
- Check startup configuration
- Verify write permissions
- Look for error logs
- Manual create with `/save new`

### Premature Archival
- Adjust timeout setting
- Check system clock
- Verify activity tracking
- Review operation hooks

### Lost Sessions
- Check archive directory
- Use `/save search`
- Review session links
- Check backup location

## Session Best Practices

1. **Let it run**: Trust automatic management
2. **Meaningful names**: Use descriptive session names
3. **Regular commits**: Session != version control
4. **Search effectively**: Use session search tools
5. **Archive wisely**: Don't delete old sessions

## Archive Management

Sessions older than 30 days:
- Move to `.z__archive/sessions/`
- Compressed for storage
- Still searchable
- Excluded from normal operations

## Recovery Features

### Session Recovery
```bash
# Recover from crash
/save recover

# Resume previous session
/save resume [session-id]

# Merge broken sessions
/save merge [session1] [session2]
```

## Related Documentation

- [Save Command Guide](../../logic/commands.md#save)
- [Context Management Hook](./context-management-hook.md)
- [Session Architecture](../../architecture/sessions.md)