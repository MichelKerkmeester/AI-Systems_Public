# Task Management Hook

## Overview

**Hook Name**: Task Management Hook  
**Purpose**: Monitors task lifecycle and suggests state transitions  
**Location**: `/hooks/core/task-management-hook.py`  
**Triggers**: TodoWrite operations, task file operations  
**Priority**: 3 (Workflow management)  
**Performance**: ~15ms typical execution time

## Description

The Task Management Hook automates the task lifecycle by monitoring TodoWrite operations and task file changes. It tracks progress, suggests task completion when all todos are done, and provides guidance for the task workflow from creation through archival.

## Configuration

The hook uses task states and lifecycle rules:

```python
Task Lifecycle:
/specs → /active → /completed → /z__archive (user-managed)

Rules:
- Only one task can be active at a time
- Tasks must be explicitly activated
- Completion triggered at 100% todo completion
- Automatic archival after 30 days
```

## How It Works

1. **Monitors TodoWrite**:
   - Tracks todo completion percentage
   - Identifies high-priority items
   - Detects task patterns (WP mentions)

2. **Monitors Task Files**:
   - Detects task creation in `/specs`
   - Tracks movement between folders
   - Provides workflow guidance

3. **Suggests Actions**:
   - Task activation when none active
   - Task completion at 100%
   - New task creation from patterns

4. **Maintains State**:
   - Updates task progress
   - Links todos to tasks
   - Tracks task history

## Example Usage

### Task Creation Detection
```
File created: /tasks/specs/new-feature.md

✅ Task 'new-feature' created in /specs

Task Workflow Reminder:
1. Review the task document for completeness
2. Approve to begin implementation
3. Activate with: /logic tasks activate new-feature
4. Track progress with TodoWrite
5. Complete when finished: /logic tasks complete

The task will automatically flow through:
/specs → /active → /completed → /z__archive (user-managed)
```

### Progress Tracking
```
TodoWrite updated: 8/10 tasks completed (80%)

Active Task: implement-authentication
Progress: ████████░░ 80%

2 remaining todos:
• Add password reset flow
• Write integration tests
```

### Completion Suggestion
```
✅ Task Complete!

Task 'implement-authentication' appears to be complete
All todos have been marked as completed

To archive this task and update records:
/logic tasks complete

Or continue with any remaining work...
```

## Task Pattern Detection

The hook identifies potential tasks from todo patterns:

- **Work Package Format**: `WP1: Description`
- **Action Keywords**: Create, Implement, Build, Design
- **Multi-step Indicators**: Numbered items, phases

## Integration Points

- **TodoWrite Tool**: Primary progress tracking
- **File Operations**: Task file monitoring
- **Session Management**: Task state in sessions
- **Query Planning Hook**: Task creation suggestions

## Performance Considerations

- Lightweight todo analysis (~15ms)
- Efficient file path checking
- Caches active task state
- Minimal file system operations

## Advanced Features

### Task Templates
Recognizes and suggests templates:
```python
templates = {
    "feature": "Feature implementation template",
    "bugfix": "Bug fix workflow template",
    "refactor": "Refactoring checklist template"
}
```

### Progress Visualization
```
Task: authentication-system
┌─────────────────────────────┐
│ ██████████████████░░░░░░░░ │ 72%
└─────────────────────────────┘
Todos: 18/25 complete
Time: 3.5 hours
```

### Task Metrics
- Completion time tracking
- Todo velocity calculation
- Bottleneck identification
- Historical analysis

## Troubleshooting

### Task Not Activating
- Check if another task is active
- Verify task exists in `/specs`
- Ensure proper file naming (.md)

### Progress Not Updating
- Confirm TodoWrite is being used
- Check todo ID consistency
- Verify hook is enabled

### Wrong Suggestions
- Adjust pattern detection
- Check task state accuracy
- Clear stale state if needed

## Commands

- `/logic tasks` - Task management menu
- `/logic tasks list` - Show all tasks
- `/logic tasks activate [name]` - Start task
- `/logic tasks status` - Current progress
- `/logic tasks complete` - Finish task

## Task States

| State | Location | Description |
|-------|----------|-------------|
| **Pending** | `/specs` | Awaiting activation |
| **Active** | `/active` | Currently working |
| **Complete** | `/completed` | Finished tasks (organize in sub-folders) |
| **Archived** | `/z__archive` | User-managed archive |

## Best Practices

1. **One Active Task**: Focus on single task completion
2. **Use TodoWrite**: Enables progress tracking
3. **Regular Updates**: Keep todos current
4. **Clear Naming**: Use descriptive task names
5. **Template Usage**: Leverage task templates

## Related Documentation

- [Task System Guide](../../logic/tasks.md)
- [TodoWrite Integration](../tools/todowrite.md)
- [Query Planning Hook](./query-planning-hook.md)