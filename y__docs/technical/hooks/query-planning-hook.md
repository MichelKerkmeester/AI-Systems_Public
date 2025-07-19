# Query Planning Hook

## Overview

**Hook Name**: Query Planning Hook  
**Purpose**: Automatically creates task documents for complex queries requiring planning  
**Location**: `/hooks/core/query-planning-hook.py`  
**Triggers**: UserPromptSubmit events  
**Priority**: 3 (Planning automation)  
**Performance**: ~5ms typical execution time

## Description

The Query Planning Hook detects when user queries require systematic planning and execution, automatically suggesting the creation of structured task documents. It ensures complex requests are properly documented and tracked through the task management system.

## Configuration

Settings file: `/hooks/core/query-planning-settings.json`

```json
{
  "enabled": true,
  "planning_threshold": 6,
  "auto_create_task": true,
  "require_approval": true,
  "task_folder": "to-do",
  "include_timeline": true,
  "include_metrics": true
}
```

## How It Works

1. **Analyzes Query Intent**:
   - Detects analysis requests
   - Identifies enhancement needs
   - Recognizes planning keywords
   - Checks task creation patterns

2. **Calculates Planning Score**:
   - Pattern weights (3-5 points)
   - Length and structure bonus
   - Multi-requirement detection

3. **Suggests Task Creation**:
   - When score exceeds threshold
   - Not already in task context
   - Would benefit from structure

4. **Guides Workflow**:
   - Explains task benefits
   - Shows lifecycle flow
   - Suggests task naming

## Planning Indicators

### Analysis Requests (Weight: 3)
```python
patterns = [
    r'\banalyz[es]?\s+(?:the\s+)?(?:completion|summary|state)\b',
    r'\bwhat\s+(?:was|has been)\s+(?:accomplished|completed|done)\b',
    r'\breview\s+(?:the\s+)?(?:project|work|tasks?)\b',
    r'\bassess\s+(?:the\s+)?(?:current|overall)\s+(?:state|status)\b'
]
```

### Enhancement Requests (Weight: 4)
```python
patterns = [
    r'\b(?:enhance|improve|optimize|upgrade)\s+(?:the\s+)?(?:system|project)\b',
    r'\bdo\s+(?:all|everything)\s+including\s+optional\b',
    r'\bcomprehensive\s+(?:improvement|enhancement|upgrade)\b',
    r'\bpost[- ]?refactoring\s+(?:tasks?|work)\b'
]
```

### Planning Keywords (Weight: 3)
```python
patterns = [
    r'\b(?:plan|planning|roadmap|strategy)\b',
    r'\b(?:phases?|stages?|steps?)\s+(?:of|for)\b',
    r'\bwhat\s+(?:should|needs to)\s+(?:be\s+)?(?:done|implemented)\b',
    r'\bnext\s+steps?\b'
]
```

## Example Usage

### Planning Detection
```
User: "Analyze the completion summary and create a comprehensive plan 
       for all remaining enhancements including optional features"

📋 Planning Detected

Planning Score: 10/6
Query Type: analysis_request, enhancement_request, planning_keywords

This query requires systematic planning and execution.

Recommended Action: Create a structured task document

A task document will:
• Organize all requirements clearly
• Track progress systematically
• Ensure nothing is missed
• Document decisions and rationale

Suggested task name: enhancement-system-enhancement
```

## Task Naming Logic

The hook suggests task names based on query type:

```python
Task Templates:
- analysis-* : For analysis/review requests
- enhancement-* : For improvement requests  
- refactoring-* : For refactoring work
- implementation-* : For new features
- optimization-* : For performance work
```

## Integration Points

- **Task Management Hook**: Handles created tasks
- **Workflow Automation Hook**: Complementary complexity detection
- **TodoWrite**: Progress tracking after task creation
- **File Operations**: Task document creation

## Performance Considerations

- Lightweight pattern matching (~5ms)
- No external dependencies
- Early exit optimization
- Efficient scoring algorithm

## Advanced Features

### Context Awareness
Prevents duplicate suggestions:
- Checks for active tasks
- Detects task-related commands
- Avoids suggestion loops

### Smart Task Templates
```python
templates = {
    "analysis": "Current state, findings, recommendations",
    "enhancement": "Goals, phases, metrics, timeline",
    "implementation": "Requirements, design, testing, deployment"
}
```

## Troubleshooting

### Not Detecting Planning Needs
- Lower planning threshold
- Add custom patterns
- Check query length
- Review detected types

### Too Many Suggestions
- Increase threshold
- Add context checks
- Limit to specific patterns

### Wrong Task Names
- Adjust naming templates
- Add pattern mappings
- Use custom prefixes

## Manual Control

While automatic, you can:
- Disable: Set `enabled: false` in settings
- Adjust threshold: Change `planning_threshold`
- Force planning: Include "create task" in query
- Skip planning: Already in task context

## Best Practices

1. **Let it guide you**: Trust the planning detection
2. **Review suggestions**: Ensure task name fits
3. **Complete the cycle**: Follow through to completion
4. **Learn patterns**: Hook improves with usage

## Related Documentation

- [Task Management Hook](./task-management-hook.md)
- [Task System Guide](../../logic/tasks.md)
- [Workflow Automation Hook](./workflow-automation-hook.md)