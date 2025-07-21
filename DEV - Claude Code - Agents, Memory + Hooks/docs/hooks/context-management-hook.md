# Context Management Hook

## Overview

**Hook Name**: Context Management Hook  
**Purpose**: Automatically saves and manages context state across operations  
**Location**: `.claude/logic/hooks/core/context-management-hook.py`  
**Triggers**: PostToolUse events  
**Priority**: 4 (Context management)  
**Performance**: ~5ms typical execution time

## Description

The Context Management Hook automatically tracks and saves the working context during a Claude Code session. It replaces the manual `/context` command by intelligently monitoring file operations, command usage, and memory references to maintain an up-to-date context state.

## Configuration

Settings file: `.claude/logic/context/context-settings.json`

```json
{
  "enabled": true,
  "auto_save_interval": 300,        // Save every 5 minutes
  "auto_save_operations": 10,       // Save after 10 operations
  "track_file_context": true,       // Track file operations
  "track_command_history": true,    // Track command usage
  "track_memory_references": true,  // Track memory system usage
  "max_context_size": 50,          // Max items per category
  "context_file_limit": 20         // Max files to track
}
```

## How It Works

1. **Monitors Tool Usage**: Tracks all PostToolUse events
2. **Updates Context**: Maintains lists of:
   - Recently accessed files
   - Commands used
   - Memory references
   - Active patterns
3. **Auto-Saves**: Triggers save when:
   - Time interval reached (5 minutes)
   - Operation count reached (10 operations)
   - Significant context change detected
4. **Manages Size**: Keeps context within limits using LRU strategy

## Example Usage

The hook runs automatically and requires no manual intervention. Context is saved to:
- `.claude/sessions/context.json` - Current context
- `.claude/state/context-state.json` - Hook state

### Context Structure
```json
{
  "session_id": "2025-01-19-session",
  "last_updated": "2025-01-19T10:30:00Z",
  "files": [
    {
      "path": "/src/components/hero.js",
      "last_accessed": "2025-01-19T10:29:00Z",
      "operations": ["read", "edit"]
    }
  ],
  "commands": [
    "/memory search patterns",
    "/logic tasks new"
  ],
  "memory_references": [
    "hero-optimization-pattern",
    "webflow-constraints"
  ],
  "statistics": {
    "total_operations": 47,
    "files_accessed": 12,
    "commands_used": 8
  }
}
```

## Integration Points

- **Session Hook**: Coordinates with session management for context persistence
- **Memory Context Hook**: Shares memory reference tracking
- **Pattern Extraction Hook**: Provides context for pattern analysis
- **Task Management**: Context included in task state

## Performance Considerations

- Uses incremental updates to minimize overhead
- Caches frequently accessed data
- Debounces saves to prevent excessive writes
- Typical execution: 5ms per operation

## Troubleshooting

### Context Not Saving
- Check if hook is enabled in settings
- Verify write permissions to context paths
- Check if operation/time thresholds are too high

### Context Too Large
- Reduce `max_context_size` in settings
- Clear old context with `/logic context clear`
- Enable automatic pruning

### Missing Context Data
- Ensure relevant tracking options are enabled
- Check if specific tools are excluded
- Verify hook is properly registered in settings.json

## Advanced Features

### Manual Control
While the hook is automatic, you can:
- Force save: `/logic context save`
- View current: `/logic context show`
- Clear context: `/logic context clear`

### Context Filtering
Configure which operations to track:
```json
{
  "exclude_patterns": ["*.log", "*.tmp"],
  "include_only": ["src/", "tests/"],
  "ignore_tools": ["WebSearch", "WebFetch"]
}
```

## Related Documentation

- [Session Hook](./session-hook.md) - Session management integration
- [Pattern Extraction Hook](./pattern-extraction-hook.md) - Pattern analysis using context
- [Hook Development Guide](./hook-development-guide.md) - Creating custom hooks