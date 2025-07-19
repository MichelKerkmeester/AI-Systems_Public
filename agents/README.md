# Multi-Agent Development Guide

This guide explains how to use Claude's multi-agent system for parallel development of work packages.

## Overview

The multi-agent system allows multiple Claude instances to work concurrently on different parts of your project. Each agent:
- Works in an isolated git worktree
- Has its own resource limits
- Communicates through a message queue
- Coordinates through distributed locking

## Quick Start

### 1. Start Parallel Agents

```bash
# Start agents for specific work packages
/logic tasks parallel start wp1,wp2,wp3

# Start agents for all high-priority tasks
/logic tasks parallel start all
```

### 2. Monitor Progress

```bash
# Check status of all agents
/logic tasks parallel status

# View logs for specific agent
/logic tasks parallel logs claude-wp1-abc123
```

### 3. Merge Completed Work

```bash
# Merge specific agent's work
/logic tasks parallel merge claude-wp1-abc123

# Clean up all agents
/logic tasks parallel cleanup
```

## Architecture

### Component Overview

```
.claude/agents/
├── registry/              # Agent registration & tracking
│   ├── active-agents.json # Currently active agents
│   └── agent-history.json # Historical records
├── locks/                 # Distributed locking
│   ├── git.lock          # Git operation mutex
│   ├── memory.lock       # Memory system mutex
│   └── hooks/            # Per-hook locks
├── messages/             # Inter-agent communication
│   ├── broadcast/        # Broadcast messages
│   └── {agent-id}/       # Agent-specific messages
├── worktrees/            # Git worktrees for agents
│   └── {work-package}/   # Isolated development branch
└── monitoring/           # Resource usage tracking
```

### Agent Lifecycle

1. **Spawn**: Create worktree, register agent, start process
2. **Initialize**: Set up workspace, subscribe to messages
3. **Execute**: Process assigned tasks with resource monitoring
4. **Complete**: Finish tasks, prepare for merge
5. **Merge**: Integrate changes back to main branch
6. **Cleanup**: Remove worktree, deregister, release resources

## Key Components

### 1. Distributed Locking

Prevents conflicts when agents access shared resources:

```python
from logic.shared import DistributedLockManager

lock_manager = DistributedLockManager(agent_id)

# Exclusive file access
with lock_manager.atomic_file_operation("config.json"):
    # Safe to modify file
    update_config()

# Named resource lock
lock = lock_manager.acquire_lock("database", timeout=10)
if lock:
    try:
        perform_database_operation()
    finally:
        lock_manager.release_lock("database")
```

### 2. Message Queue

Agents communicate asynchronously:

```python
from logic.shared import MessageQueue, Message

queue = MessageQueue(agent_id)

# Send status update
queue.send_status_update("Working on feature X", {
    "progress": 50,
    "estimated_completion": "10 minutes"
})

# Subscribe to messages
def on_task_complete(message):
    print(f"Task {message.payload['task_id']} completed!")

queue.subscribe("task_complete", on_task_complete)
queue.start()
```

### 3. Resource Monitoring

Each agent has resource limits:

```python
from logic.shared import ResourceMonitor

monitor = ResourceMonitor(agent_id)
monitor.start_monitoring()

# Check if within limits
if not monitor.check_limits():
    # Throttle or pause work
    await asyncio.sleep(5)

# Get usage statistics
stats = monitor.get_usage_stats()
print(f"Memory: {stats['avg_memory_mb']}MB")
print(f"CPU: {stats['avg_cpu_percent']}%")
```

### 4. Conflict Resolution

Automatic handling of concurrent access:

```python
from logic.shared import ConflictResolver, Conflict, ConflictType

resolver = ConflictResolver()

# Report conflict
conflict = Conflict(
    conflict_type=ConflictType.FILE_EDIT,
    resource="src/main.py",
    agent1_id=agent1,
    agent2_id=agent2,
    details={"lines": [10, 20]}
)

resolution = resolver.resolve_conflict(conflict)
# Returns: MERGE, QUEUE, FIRST_WINS, etc.
```

## Resource Limits

Default per-agent limits:
- Memory: 512MB
- CPU: 25%
- Open files: 100
- Disk writes: 100MB/min

Global limits:
- Total memory: 2GB
- Total CPU: 80%
- Max agents: 10

## Best Practices

### 1. Work Package Design

- **Independent**: Minimize dependencies between packages
- **Focused**: Single responsibility per package
- **Sized**: 2-8 hours of work per package
- **Testable**: Clear acceptance criteria

### 2. Conflict Avoidance

- **File Isolation**: Work on different files when possible
- **Lock Granularity**: Use fine-grained locks
- **Quick Operations**: Hold locks briefly
- **Async Work**: Use message queue for coordination

### 3. Performance

- **Batch Operations**: Group file operations
- **Lazy Loading**: Load resources on-demand
- **Shared Cache**: Use agent-local caches
- **Resource Awareness**: Monitor usage regularly

## Troubleshooting

### Agent Not Starting

```bash
# Check resource availability
/logic tasks parallel status

# View system resources
/logic system

# Check for stale locks
/logic agents emergency clean
```

### Merge Conflicts

```bash
# Check for conflicts before merge
git merge --no-commit --no-ff {branch}

# If conflicts exist, create integration agent
/logic tasks parallel start {wp}-integration
```

### Performance Issues

```bash
# Monitor resource usage
/logic agents monitor

# Check agent logs
/logic tasks parallel logs {agent-id}

# Reduce parallel agents
/logic tasks parallel pause {agent-id}
```

### Emergency Recovery

```bash
# Stop all agents
/logic agents emergency stop

# Clean up resources
/logic agents emergency clean

# Reset system
/logic agents emergency reset
```

## Advanced Usage

### Custom Agent Types

Create specialized agents in `.claude/logic/shared/agent_base.py`:

```python
class ReviewAgent(AgentBase):
    def __init__(self, work_package, **kwargs):
        super().__init__(
            agent_type="review",
            work_package=work_package,
            **kwargs
        )
    
    async def initialize(self):
        # Set up review tools
        pass
    
    async def run(self):
        # Review implementation
        pass
```

### Work Distribution

Configure in `.claude/logic/shared/work_distribution.py`:

```python
# Define agent capabilities
engine.agent_capabilities["specialist"] = AgentCapabilities(
    agent_type="specialist",
    supported_tasks=[TaskType.OPTIMIZE, TaskType.PROFILE],
    performance_multiplier=1.5
)

# Create distribution plan
plan = engine.create_distribution_plan()
optimized = engine.optimize_distribution(plan, max_agents=5)
```

### Hook Integration

Hooks automatically support multi-agent execution:

```python
class MyHook(HookBase):
    def __init__(self):
        super().__init__()
        self.metadata = {
            "concurrent_safe": True,
            "exclusive_resources": ["database"],
            "max_parallel": 3
        }
```

## Examples

### Example 1: Parallel Feature Development

```bash
# Define work packages in todos
/todo
- wp1-auth: Implement authentication system
- wp2-api: Create REST API endpoints  
- wp3-ui: Build user interface

# Start parallel development
/logic tasks parallel start wp1-auth,wp2-api,wp3-ui

# Monitor progress
/logic tasks parallel status

# Merge as completed
/logic tasks parallel merge claude-wp1-auth-abc123
/logic tasks parallel merge claude-wp2-api-def456
/logic tasks parallel merge claude-wp3-ui-ghi789
```

### Example 2: Large Refactoring

```bash
# Start all refactoring tasks
/logic tasks parallel start all

# Monitor resource usage
/logic agents monitor

# Pause heavy agent if needed
/logic tasks parallel pause claude-wp-database-xyz

# Resume when resources available
/logic tasks parallel resume claude-wp-database-xyz
```

### Example 3: Integration Testing

```bash
# Run tests in parallel
/logic tasks parallel start test-unit,test-integration,test-e2e

# View test results
/logic tasks parallel logs claude-test-unit-123
/logic tasks parallel logs claude-test-integration-456

# Merge test improvements
/logic tasks parallel merge all
```

## Security Considerations

1. **File Access**: Agents only access project directory
2. **Git Operations**: Sequential through locking
3. **Resource Limits**: Prevent system exhaustion
4. **Message Privacy**: Agent-specific message directories
5. **Lock Timeouts**: Prevent indefinite blocking

## Future Enhancements

- Cloud-based agent execution
- GPU-accelerated agents
- Cross-project agent sharing
- Agent skill marketplace
- Visual monitoring dashboard

---

For more information, see:
- `/logic help agents` - Command reference
- `.claude/logic/shared/` - Implementation details
- `.claude/project/tests/test_multi_agent.py` - Test examples