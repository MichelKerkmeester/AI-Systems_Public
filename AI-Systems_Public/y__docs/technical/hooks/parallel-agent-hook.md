# Parallel Agent Hook

## Overview

**Hook Name**: Parallel Agent Hook  
**Purpose**: Suggests and manages parallel agent execution for large tasks  
**Location**: `/hooks/core/parallel-agent-hook.py`  
**Triggers**: TodoWrite operations with multiple work packages  
**Priority**: 3 (Workflow optimization)  
**Performance**: ~20ms typical execution time

## Description

The Parallel Agent Hook monitors task complexity and suggests parallel agent execution when it detects opportunities for concurrent development. It's designed to enable 70%+ speed improvements on large projects by intelligently distributing work across multiple Claude agents.

## Configuration

Settings file: `/hooks/core/parallel-settings.json`

```json
{
  "enabled": true,
  "suggestion_threshold": 5,    // Min WPs for suggestion
  "max_agents": 10,            // Maximum concurrent agents
  "auto_suggest": true,
  "require_confirmation": true,
  "agent_workspace": ".claude/agents/"
}
```

## How It Works

1. **Monitors TodoWrite**:
   - Analyzes todo items for work packages (WP patterns)
   - Detects independent vs dependent tasks
   - Calculates potential parallelization

2. **Evaluates Parallelization**:
   - Identifies task dependencies
   - Groups independent work
   - Estimates time savings

3. **Suggests When Beneficial**:
   - Multiple independent work packages
   - Estimated 50%+ time reduction
   - System resources available

4. **Manages Agent Lifecycle**:
   - Tracks agent states
   - Monitors resource usage
   - Coordinates merges

## Example Usage

### Parallel Execution Suggestion
```
Todo Analysis:
Found 6 independent work packages:
• WP1: Hook Implementation (2 hours)
• WP2: Documentation (3 hours)
• WP3: Testing Suite (2 hours)
• WP4: Performance Benchmarks (1 hour)
• WP5: Integration (2 hours)
• WP6: Deployment (1 hour)

🚀 Parallel Execution Available!
Sequential Time: ~11 hours
Parallel Time: ~3 hours (72% reduction)

Suggested Distribution:
• Agent 1: WP1 + WP4 (3 hours)
• Agent 2: WP2 (3 hours)
• Agent 3: WP3 + WP5 + WP6 (5 hours)

Enable with: /logic agents spawn 3
```

## Agent Architecture

### Agent States
```
IDLE -> ASSIGNED -> WORKING -> MERGING -> COMPLETE
                      ↓
                   FAILED -> RETRY
```

### Resource Allocation
- Each agent gets dedicated workspace
- Isolated git worktree
- Resource quotas enforced
- Automatic cleanup on completion

## Integration Points

- **Task Management Hook**: Coordinates task distribution
- **Git Integration**: Manages worktrees and merges
- **Resource Monitor**: Tracks system usage
- **Distributed Lock Manager**: Prevents conflicts

## Performance Considerations

- Lightweight analysis (~20ms)
- Async agent spawning
- Resource pooling for efficiency
- Automatic load balancing

## Advanced Features

### Custom Work Distribution
```json
{
  "distribution_strategy": "balanced",  // or "greedy", "dependencies"
  "agent_specialization": {
    "documentation": ["Agent-2"],
    "testing": ["Agent-3"],
    "implementation": ["Agent-1", "Agent-4"]
  }
}
```

### Dependency Management
```json
{
  "task_dependencies": {
    "WP2": ["WP1"],      // WP2 depends on WP1
    "WP5": ["WP3", "WP4"] // WP5 needs both WP3 and WP4
  }
}
```

## Troubleshooting

### Agents Not Spawning
- Check max_agents limit
- Verify system resources
- Ensure git worktree support
- Check agent workspace permissions

### Merge Conflicts
- Agents work in isolated branches
- Automatic conflict detection
- Manual resolution interface
- Rollback capability

### Performance Issues
- Reduce concurrent agents
- Check resource quotas
- Enable agent pooling
- Monitor system load

## Commands

- `/logic agents status` - View all agents
- `/logic agents spawn [n]` - Start n agents
- `/logic agents monitor` - Live monitoring
- `/logic agents merge` - Coordinate merges
- `/logic agents cleanup` - Clean resources

## Safety Features

- Distributed locking prevents conflicts
- Atomic operations ensure consistency
- Automatic rollback on failures
- Resource limits prevent exhaustion
- Health monitoring with auto-recovery

## Related Documentation

- [Multi-Agent Architecture](../../architecture/multi-agent.md)
- [Task Management Hook](./task-management-hook.md)
- [Agent Development Guide](../../development/agents.md)