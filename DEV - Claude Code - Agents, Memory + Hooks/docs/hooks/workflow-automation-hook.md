# Workflow Automation Hook

## Overview

**Hook Name**: Workflow Automation Hook  
**Purpose**: Detects complex tasks and triggers Sequential Thinking automation  
**Location**: `/hooks/core/workflow-automation-hook.py`  
**Triggers**: UserPromptSubmit events  
**Priority**: 3 (Workflow automation)  
**Performance**: ~2ms typical execution time

## Description

The Workflow Automation Hook analyzes user prompts to detect complexity and automatically triggers Sequential Thinking MCP for tasks that would benefit from structured analysis. It replaces the manual `/workflow` command with intelligent automation based on task patterns.

## Configuration

Settings file: `/logic/workflow/workflow-settings.json`

```json
{
  "enabled": true,
  "complexity_threshold": 3,
  "auto_trigger": true,
  "show_analysis": true,
  "exclude_patterns": [
    "\\b(?:simple|quick|small|minor)\\b",
    "\\bjust\\s+(?:a\\s+)?(?:quick|simple)\\b",
    "\\bone[- ]?liner?\\b"
  ]
}
```

## How It Works

1. **Analyzes Prompt Complexity**:
   - Pattern matching for complexity indicators
   - Keyword detection for workflow needs
   - Structural analysis (length, formatting)

2. **Calculates Complexity Score**:
   - Each pattern has weight (1-4 points)
   - Multiple indicators increase score
   - Threshold comparison (default: 3)

3. **Triggers When Beneficial**:
   - Score exceeds threshold
   - No exclusion patterns match
   - Auto-trigger enabled for high scores

4. **Provides Recommendations**:
   - Explains why workflow suggested
   - Shows detected patterns
   - Offers manual control

## Complexity Patterns

### Multi-Step Tasks (Weight: 3)
```python
patterns = [
    r'\b(?:step|phase|stage)s?\s*\d+',
    r'\bfirst\b.*\bthen\b.*\bfinally\b',
    r'\b(?:1\.|one).*\b(?:2\.|two).*\b(?:3\.|three)',
    r'\bsequence\s+of\b',
    r'\bmulti[- ]?step\b'
]
```

### Architecture Tasks (Weight: 4)
```python
patterns = [
    r'\barchitect(?:ure|ural)\b',
    r'\bdesign\s+pattern\b',
    r'\bsystem\s+design\b',
    r'\brefactor(?:ing)?\b',
    r'\brestructur(?:e|ing)\b'
]
```

### Complex Features (Weight: 3)
```python
patterns = [
    r'\bimplement\s+(?:a\s+)?(?:new\s+)?(?:feature|system|module)\b',
    r'\bbuild\s+(?:a\s+)?(?:complete|full|entire)\b',
    r'\bcreate\s+(?:a\s+)?(?:comprehensive|complex)\b',
    r'\bintegrat(?:e|ion)\s+(?:with|multiple)\b'
]
```

## Example Usage

### Low Complexity (No Trigger)
```
User: "How do I print Hello World in Python?"
Score: 0 (below threshold)
Action: None - simple query handled normally
```

### Medium Complexity (Suggestion)
```
User: "I need to implement user authentication"

💡 Workflow Automation Detection
Complexity Score: 4/3 (threshold)
Detected Patterns: complex_features, workflow_keywords

Sequential Thinking will be triggered automatically if needed
```

### High Complexity (Auto-Trigger)
```
User: "Design and implement a multi-tenant architecture with..."

🚀 Workflow Automation Detection
Complexity Score: 8/3 (threshold)
Detected Patterns: architecture, multi_step, complex_features

Sequential Thinking Auto-Triggered
Starting workflow analysis...
```

## Integration Points

- **Sequential Thinking MCP**: Primary automation target
- **Query Planning Hook**: Coordinates for task creation
- **Mode Suggestion Hook**: Aligns with mode detection
- **Task Management**: Complex tasks tracked

## Performance Optimization

- Compiled regex patterns (~2ms)
- Early exit on exclusions
- Minimal memory usage
- No external dependencies

## Advanced Configuration

### Custom Complexity Patterns
```json
{
  "custom_patterns": {
    "data_pipeline": {
      "patterns": ["pipeline", "etl", "data flow"],
      "weight": 3
    },
    "optimization": {
      "patterns": ["optimize", "performance", "speed up"],
      "weight": 2
    }
  }
}
```

### Trigger Customization
```json
{
  "trigger_rules": {
    "min_prompt_length": 50,
    "require_keywords": 2,
    "auto_trigger_multiplier": 1.5
  }
}
```

## Troubleshooting

### Not Triggering
- Check complexity threshold
- Review excluded patterns
- Verify hook enabled
- Test with known complex prompt

### Too Many Triggers
- Increase threshold
- Add exclusion patterns
- Disable auto-trigger
- Adjust pattern weights

### Wrong Analysis
- Review detected patterns
- Adjust pattern matching
- Check keyword list
- Update weights

## Manual Control

- Enable/disable: `/logic hooks workflow [on|off]`
- Adjust threshold: `/logic hooks workflow threshold 5`
- Force trigger: Add "workflow:" to prompt
- Skip automation: Add "simple:" to prompt

## Workflow Keywords

Triggers include:
- plan, design, architect
- implement, build, create
- refactor, restructure
- analyze, investigate
- debug, optimize
- migrate, integrate
- automate

## Related Documentation

- [Sequential Thinking MCP](../mcp/sequential-thinking/README.md)
- [Query Planning Hook](./query-planning-hook.md)
- [Workflow System Guide](../../logic/workflow.md)