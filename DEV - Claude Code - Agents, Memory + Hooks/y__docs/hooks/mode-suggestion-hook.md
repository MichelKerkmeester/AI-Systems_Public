# Mode Suggestion Hook

## Overview

**Hook Name**: Mode Suggestion Hook  
**Purpose**: Intelligently suggests mode changes based on task complexity  
**Location**: `/hooks/core/mode-suggestion-hook.py`  
**Triggers**: UserPromptSubmit events  
**Priority**: 3 (Workflow suggestions)  
**Performance**: ~2ms typical execution time

## Description

The Mode Suggestion Hook analyzes user prompts and task complexity to suggest appropriate working modes. It helps users switch between different modes (Standard, Deep Work, Review, Auto) based on the nature of their current task, replacing manual mode selection with intelligent recommendations.

## Configuration

Settings file: `/hooks/core/mode-settings.json`

```json
{
  "enabled": true,
  "suggestion_threshold": 0.7,
  "current_mode": "auto",
  "mode_history": [],
  "patterns": {
    "deep_work": ["implement", "build", "create", "develop"],
    "review": ["check", "verify", "test", "validate"],
    "debug": ["fix", "debug", "troubleshoot", "error"]
  }
}
```

## How It Works

1. **Analyzes User Prompt**: 
   - Detects keywords and patterns
   - Evaluates task complexity
   - Considers recent mode history

2. **Calculates Mode Score**:
   - Each mode has pattern weights
   - Scores based on keyword matches
   - Considers context and history

3. **Suggests When Appropriate**:
   - Only suggests if confidence > threshold
   - Avoids repetitive suggestions
   - Respects user preferences

4. **Provides Easy Switching**:
   - Shows current mode
   - One-command mode change
   - Explains why mode was suggested

## Example Usage

### Automatic Suggestion
```
User: "I need to implement a new authentication system with OAuth2"

Mode Suggestion:
🎯 Deep Work Mode Recommended
This task involves complex implementation. Deep Work mode will:
• Enable extended focus time
• Provide detailed progress tracking
• Minimize interruptions

Switch with: /mode deep-work
```

### Mode Patterns

| Mode | Triggers | Best For |
|------|----------|----------|
| **Standard** | General queries | Quick tasks, Q&A |
| **Deep Work** | Implementation keywords | Complex development |
| **Review** | Testing/validation terms | Code review, QA |
| **Debug** | Error/fix keywords | Troubleshooting |
| **Auto** | Default | Adaptive behavior |

## Integration Points

- **Workflow Automation Hook**: Coordinates with complexity detection
- **Task Management**: Mode tracked in task state
- **Session Management**: Mode changes logged in session
- **Quality Hook**: Different thresholds per mode

## Performance Considerations

- Lightweight pattern matching (~2ms)
- Caches compiled regex patterns
- Minimal memory footprint
- No external dependencies

## Advanced Features

### Custom Mode Patterns
Add your own patterns:

```json
{
  "custom_patterns": {
    "research": ["analyze", "investigate", "explore"],
    "planning": ["design", "architect", "plan"]
  }
}
```

### Mode Automation
Configure automatic mode switching:

```json
{
  "auto_switch": {
    "enabled": true,
    "require_confirmation": false,
    "sticky_duration": 1800  // 30 minutes
  }
}
```

## Troubleshooting

### Not Getting Suggestions
- Check suggestion threshold (lower if too high)
- Verify patterns match your terminology
- Ensure hook is enabled

### Wrong Mode Suggested
- Adjust pattern weights in configuration
- Add custom patterns for your workflow
- Use `/mode` to manually override

### Too Many Suggestions
- Increase suggestion threshold
- Enable sticky duration
- Disable for specific modes

## Mode Commands

- `/mode` - Show current mode and options
- `/mode [name]` - Switch to specific mode
- `/mode auto` - Enable automatic mode
- `/mode settings` - Configure suggestions

## Related Documentation

- [Workflow Automation Hook](./workflow-automation-hook.md) - Complexity detection
- [Mode System Guide](../../logic/modes.md) - Detailed mode documentation
- [Hook Development Guide](./hook-development-guide.md) - Creating custom hooks