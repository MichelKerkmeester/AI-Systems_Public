# Prompt Enhancement Hook

## Overview

The Prompt Enhancement Hook integrates with the UserPromptSubmit pipeline to automatically enhance user prompts based on project best practices and CLAUDE.md rules. It uses a two-pass enhancement system that applies general prompt engineering best practices first, then injects project-specific rules.

## Features

### Two-Pass Enhancement System
1. **Pass 1: General Best Practices**
   - Adds clarity to vague prompts
   - Structures complex prompts
   - Adds output specifications
   - Includes context for code-related tasks

2. **Pass 2: Project-Specific Rules**
   - Injects CLAUDE.md principles
   - Adds technical constraints
   - Includes platform limits
   - Provides task management rules
   - Adds production checklists

### Enhancement Levels
- **Minimal**: Light touch, only essential clarifications
- **Moderate** (default): Balanced enhancement without being intrusive
- **Aggressive**: Maximum assistance with comprehensive context

### Bypass Mechanisms
Users can bypass enhancement using:
- Prefixes: `raw:`, `exact:`, `no-enhance:`
- Commands: `/memory`, `/save`, etc.
- Code blocks: Prompts that are mainly code
- Simple confirmations: "yes", "no", "ok"

## Configuration

Settings are stored in `.claude/logic/hooks/core/prompt-enhancement-settings.json`:

```json
{
  "enabled": true,
  "enhancement_level": "moderate",
  "show_enhancement_notice": true,
  "show_enhancement_details": false,
  "bypass_prefixes": ["raw:", "exact:", "no-enhance:"],
  "always_enhance_types": ["code_generation", "code_review"],
  "never_enhance_types": [],
  "log_enhancements": true,
  "max_prompt_length": 10000
}
```

### Settings Explained

- **enabled**: Master switch for the hook
- **enhancement_level**: Controls how aggressive enhancement is
- **show_enhancement_notice**: Shows a notice when prompts are enhanced
- **show_enhancement_details**: Shows detailed enhancement information
- **bypass_prefixes**: Prefixes that skip enhancement
- **always_enhance_types**: Prompt types that always get enhanced
- **never_enhance_types**: Prompt types that never get enhanced
- **log_enhancements**: Track enhancement statistics
- **max_prompt_length**: Skip enhancement for very long prompts

## Prompt Type Detection

The hook automatically detects prompt types:
- **code_generation**: "create", "implement", "build" + code context
- **code_review**: "review", "check", "analyze" + code context
- **debugging**: "debug", "fix", "error", "issue"
- **documentation**: "document", "explain", "describe"
- **system_design**: "design", "architect", "structure"
- **task_planning**: "task", "todo", "plan"
- **general**: Default for unmatched prompts

## Integration with PromptEnhancer

The hook uses the `PromptEnhancer` class from `.claude/logic/prompt_improver/prompt_enhancer.py` which:
- Loads rules from CLAUDE.md
- Integrates with pattern libraries
- Applies context-aware enhancements
- Tracks enhancement confidence

## Usage Examples

### Example 1: Simple Code Request
**Input**: "create a function to validate email"

**Enhanced**: 
```
create a function to validate email

Please provide well-commented, production-ready code following the project's coding standards.

## Project Coding Principles:
- Elite JavaScript & CSS specialist - Fix root causes, not symptoms
- Production-grade code - DRY, KISS, secure, performant
- Webflow enhancement - Work with platform, never against it
- Full ownership - Complete solutions, not patches
```

### Example 2: Bypassed Command
**Input**: "/memory search validation patterns"

**Result**: No enhancement (command pattern detected)

### Example 3: Complex Task
**Input**: "I need to refactor the authentication system"

**Enhanced**:
```
I need to refactor the authentication system

Please provide specific details about what you need, including any constraints or requirements.

Reminder: Follow the project's technical constraints and create a spec folder for major changes.

## Task Management:
- Create spec folder for major changes
- Active task limit: 1
- Task flow: specs → active → completed
```

## Monitoring and Logging

When `log_enhancements` is enabled, the hook tracks:
- Enhancement count
- Bypass count
- Rules applied
- Prompt types detected
- Enhancement confidence
- Recent enhancement history

State is stored in `.claude/logic/state/prompt-enhancement-state.json`.

## Best Practices

1. **Start with moderate level** - Provides good balance
2. **Use bypass prefixes** for specific/technical prompts
3. **Monitor enhancement logs** to understand patterns
4. **Adjust settings** based on your workflow
5. **Disable for pair programming** if it's too intrusive

## Troubleshooting

### Hook not enhancing prompts
1. Check if enabled in settings
2. Verify prompt isn't matching bypass patterns
3. Check prompt length isn't exceeding limit

### Too aggressive enhancement
1. Switch to "minimal" level
2. Add more bypass prefixes
3. Use `show_enhancement_details: false`

### Not enough enhancement
1. Switch to "aggressive" level
2. Remove items from `never_enhance_types`
3. Lower `min_word_count` thresholds

## Technical Details

### Hook Pipeline Position
The hook runs early in UserPromptSubmit pipeline:
1. Greeting hook
2. **Prompt Enhancement Hook** (modifies input)
3. Quality hook (uses enhanced prompt)
4. Memory context hook
5. Other hooks...

### Performance Considerations
- Adds ~50-200ms to prompt processing
- Caches CLAUDE.md parsing
- Skips very long prompts
- Minimal memory footprint

### Error Handling
- Never blocks on errors
- Logs errors to state file
- Falls back to original prompt
- Returns exit code 0 always