# mode-manager.py

## Overview

**Script Name**: Mode Manager  
**Purpose**: Manages working mode states and transitions  
**Location**: `/scripts/mode-manager.py`  
**Performance**: <10ms for mode operations

## Description

The mode-manager.py script handles the mode system for Claude Code, managing transitions between different working modes (Auto, Deep Work, Review, Debug), tracking mode history, and providing mode-specific adaptations for commands and behaviors.

## Usage

### Command Line
```bash
# Get current mode
python3 .claude/logic/scripts/mode-manager.py --current

# Change mode
python3 .claude/logic/scripts/mode-manager.py --set deep-work

# View mode history
python3 .claude/logic/scripts/mode-manager.py --history

# Get mode suggestions
python3 .claude/logic/scripts/mode-manager.py --suggest "implement authentication"
```

### As a Module
```python
from mode_manager import ModeManager

manager = ModeManager()
current = manager.get_current_mode()
manager.set_mode("deep-work", "Complex implementation task")
```

### Options
- `--current` - Show current mode
- `--set [mode]` - Change to specified mode
- `--history` - View mode change history
- `--suggest [prompt]` - Get mode suggestion
- `--config` - Show mode configurations

## Working Modes

### Auto Mode (Default)
```python
{
    "name": "auto",
    "description": "Adaptive mode that adjusts based on context",
    "features": {
        "suggestions": "enabled",
        "interruptions": "normal",
        "detail_level": "balanced"
    }
}
```

### Deep Work Mode
```python
{
    "name": "deep-work",
    "description": "Focused mode for complex implementation",
    "features": {
        "suggestions": "minimal",
        "interruptions": "blocked",
        "detail_level": "high",
        "progress_tracking": "enhanced"
    }
}
```

### Review Mode
```python
{
    "name": "review",
    "description": "Careful review and validation mode",
    "features": {
        "quality_checks": "strict",
        "suggestions": "quality-focused",
        "testing": "emphasized"
    }
}
```

### Debug Mode
```python
{
    "name": "debug",
    "description": "Troubleshooting and error fixing",
    "features": {
        "logging": "verbose",
        "error_details": "complete",
        "suggestions": "diagnostic"
    }
}
```

## State Management

### Mode State Structure
```json
{
    "current_mode": "auto",
    "suggested_mode": "deep-work",
    "suggestion_reason": "Complex implementation detected",
    "last_suggestion_time": "2025-01-19T15:00:00Z",
    "auto_suggest_enabled": true,
    "require_approval": true,
    "mode_history": [
        {
            "mode": "auto",
            "timestamp": "2025-01-19T14:00:00Z",
            "reason": "initial"
        },
        {
            "mode": "deep-work",
            "timestamp": "2025-01-19T14:30:00Z",
            "reason": "user_request"
        }
    ]
}
```

### State Persistence
- Stored in `/state/mode-state.json`
- Atomic writes prevent corruption
- History limited to last 50 changes
- Automatic cleanup of old entries

## Mode Detection

### Pattern Analysis
```python
mode_patterns = {
    "deep-work": [
        r"\bimplement\b",
        r"\bbuild\b",
        r"\bcreate\s+(?:a\s+)?(?:new|complex)\b",
        r"\barchitect\b"
    ],
    "review": [
        r"\breview\b",
        r"\bcheck\b",
        r"\bvalidate\b",
        r"\btest\b"
    ],
    "debug": [
        r"\bfix\b",
        r"\bdebug\b",
        r"\berror\b",
        r"\btroubleshot\b"
    ]
}
```

### Scoring Algorithm
1. Pattern matching (keyword detection)
2. Context analysis (recent operations)
3. Task complexity evaluation
4. Historical preferences

## Command Adaptations

### Mode-Specific Behaviors
```python
adaptations = {
    "deep-work": {
        "memory_hints": "minimal",
        "progress_updates": "detailed",
        "interruption_threshold": "high"
    },
    "review": {
        "quality_warnings": "all",
        "test_suggestions": "automatic",
        "documentation_checks": "strict"
    },
    "debug": {
        "error_context": "full",
        "stack_traces": "complete",
        "related_files": "show"
    }
}
```

## Integration Points

- **Mode Suggestion Hook**: Uses this for mode detection
- **Quality Hook**: Adapts standards per mode
- **Memory System**: Mode-aware context
- **Session Management**: Tracks mode in sessions

## Performance Optimization

- Compiled regex patterns
- Cached mode configurations
- Minimal file I/O
- Efficient state updates

## API Methods

### Core Methods
```python
get_current_mode() -> str
# Returns current mode name

set_mode(mode: str, reason: str) -> bool
# Changes mode with reason

suggest_mode(prompt: str) -> Optional[str]
# Returns suggested mode for prompt

get_mode_config(mode: str) -> Dict
# Returns mode configuration

get_adaptations() -> Dict
# Returns current mode adaptations
```

### History Methods
```python
get_mode_history(limit: int = 10) -> List[Dict]
# Returns recent mode changes

get_mode_stats() -> Dict
# Returns usage statistics

clear_history() -> bool
# Clears mode history
```

## Configuration

### Settings Location
- Global: `.claude/config.json`
- Mode-specific: `/logic/mode/mode-settings.json`

### Customization
```json
{
    "modes": {
        "custom-mode": {
            "description": "My custom mode",
            "patterns": ["my-keyword"],
            "adaptations": {
                "feature": "value"
            }
        }
    }
}
```

## Error Handling

- **Invalid mode**: Falls back to auto
- **Corrupted state**: Resets to default
- **Missing config**: Uses built-in defaults
- **Write failures**: Retries with backoff

## Best Practices

1. **Trust suggestions**: Algorithm improves over time
2. **Use appropriate modes**: Better results per task
3. **Review history**: Understand patterns
4. **Customize carefully**: Test new modes
5. **Let auto adapt**: Default works well

## Troubleshooting

### Mode Not Changing
- Check if locked in current mode
- Verify valid mode name
- Check permissions on state file

### Wrong Suggestions
- Review pattern configuration
- Check recent history influence
- Adjust suggestion threshold

### State Corruption
- Delete state file (auto-recreates)
- Check disk space
- Verify file permissions

## Command Examples

### Mode Status
```
Current Mode: deep-work
Active for: 45 minutes
Reason: Complex implementation task

Recent History:
- 14:30 deep-work (user requested)
- 14:00 auto (session start)
- 10:30 review (PR preparation)
```

### Mode Change
```
Switching to review mode...
✓ Mode changed to: review
Reason: Code review requested

Adaptations:
- Strict quality checks enabled
- Test suggestions active
- Documentation validation on
```

## Related Documentation

- [Mode Suggestion Hook](../hooks/mode-suggestion-hook.md)
- [Mode System Guide](../../logic/modes.md)
- [Command Adaptations](../../logic/adaptations.md)