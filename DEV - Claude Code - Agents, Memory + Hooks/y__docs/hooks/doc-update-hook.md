# Documentation Update Hook

## Overview

**Hook Name**: Documentation Update Hook  
**Purpose**: Automatically maintains documentation structure and integrity  
**Location**: `/hooks/core/doc-update-hook.py`  
**Triggers**: Write/Edit/MultiEdit on documentation files, periodic on /save  
**Priority**: 4 (Documentation maintenance)  
**Performance**: ~50-100ms (runs doc-updater.py script)

## Description

The Documentation Update Hook automatically maintains the documentation system by running the doc-updater script when documentation files are modified. It ensures that tables of contents, cross-references, and index files remain up-to-date without manual intervention.

## Configuration

The hook uses state tracking to prevent excessive updates:

```json
{
  "last_update": "2025-01-19T10:30:00Z",
  "update_count": 42,
  "min_interval_minutes": 5,
  "files_updated": []
}
```

## How It Works

1. **Monitors Documentation Changes**: 
   - Triggers on any Write/Edit/MultiEdit to `.claude/docs/*.md` files
   - Also runs periodically on `/save` commands

2. **Throttling**: 
   - Prevents updates more frequent than every 5 minutes
   - Tracks state to avoid redundant processing

3. **Executes doc-updater.py**:
   - Updates directory INDEX.md files
   - Validates internal links
   - Generates cross-references
   - Creates update reports

4. **Reports Results**:
   - Shows summary of changes
   - Highlights any issues found

## Example Usage

The hook runs automatically when you edit documentation:

```bash
# Edit a documentation file
/edit /docs/logic/commands.md

# Hook automatically:
# 1. Detects the change
# 2. Runs doc-updater.py
# 3. Updates affected index files
# 4. Reports results
```

### Sample Output
```
📚 Documentation Update Complete

Updated:
• /docs/INDEX.md - Added new command reference
• /docs/logic/INDEX.md - Updated command list
• 3 cross-references validated

All documentation links verified ✓
```

## Integration Points

- **doc-updater.py Script**: Main documentation maintenance script
- **add-toc.py Script**: Called for TOC generation
- **Task Management**: Updates tracked in task progress
- **Session Management**: Documentation state included in sessions

## Performance Considerations

- Runs asynchronously to avoid blocking
- Caches documentation structure for efficiency
- Only processes changed directories
- Typical execution: 50-100ms depending on changes

## Troubleshooting

### Updates Not Running
- Check minimum interval hasn't been reached (5 minutes)
- Verify doc-updater.py script exists and is executable
- Check write permissions on documentation directories

### Slow Updates
- Large documentation changes may take longer
- Consider increasing throttle interval if frequent
- Check for circular references in documentation

### Missing Updates
- Ensure file paths match `.claude/docs` pattern
- Verify hook is registered for PostToolUse events
- Check state file isn't corrupted

## Advanced Configuration

### Custom Update Rules
Add to the hook's configuration:

```python
{
  "update_rules": {
    "force_update_on": ["README.md", "INDEX.md"],
    "exclude_patterns": ["*-draft.md", "*.tmp"],
    "custom_scripts": ["my-doc-processor.py"]
  }
}
```

### Batch Processing
For large documentation updates:
- Updates are batched automatically
- Maximum 10 directories per update cycle
- Continues on next trigger if more needed

## Dependencies

- **doc-updater.py**: Main update script (required)
- **add-toc.py**: TOC generation (optional)
- **Python 3.8+**: Script execution environment

## Error Handling

The hook gracefully handles:
- Missing or corrupted documentation files
- Script execution failures
- Permission errors
- Network issues (for external references)

Errors are logged but don't block operation.

## Related Documentation

- [Script Documentation - doc-updater.py](../scripts/doc-updater.md)
- [Script Documentation - add-toc.py](../scripts/add-toc.md)
- [Hook Development Guide](./hook-development-guide.md)