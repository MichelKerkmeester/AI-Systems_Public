# Memory Automation v2 - Implementation Plan

## Overview
Implementing direct MCP execution for memory automation to achieve 50+ captures/day with zero manual intervention.

## Current State vs Target State

### Current (v1)
- Hooks detect patterns but only suggest captures
- No automatic MCP execution
- 1-2 memories captured per day
- Manual memory search required

### Target (v2)
- Direct MCP execution from hooks
- Automatic pattern-based capture
- 50+ memories per day
- Mandatory memory search before tasks
- Zero manual intervention

## Implementation Phases

### Phase 1: Core Infrastructure (Priority: HIGH)

#### 1.1 MCP Bridge Implementation
**File**: `.claude/logic/memory/mcp_bridge.py`
```python
# Core functionality:
- Subprocess wrapper for executing MCP tools
- JSON serialization/deserialization
- Error handling and timeout management
- Logging and debugging support
```

#### 1.2 Memory Capture Queue
**File**: `.claude/logic/memory/memory_capture_queue.py`
```python
# Features:
- Thread-safe queue for memory captures
- Persistent storage in .claude/state/memory_queue.json
- Batch processing (5 memories per batch)
- Failed capture retry logic
```

#### 1.3 Updated Memory Context Hook v2
**File**: `.claude/logic/hooks/memory-context-hook-v2.py`
```python
# Changes:
- Direct MCP execution via mcp_bridge
- Queue integration for batch processing
- Enhanced pattern detection
- Async capture to prevent blocking
```

### Phase 2: Enhanced Pattern Detection (Priority: MEDIUM)

#### 2.1 Additional Patterns
Add to existing 14 patterns:
- `REUSABLE_COMPONENT`: Detects existing code that can be reused
- `EXISTING_SOLUTION`: Identifies already solved problems
- `REFACTOR_OPPORTUNITY`: Spots code improvement chances
- `CLIENT_PREFERENCE`: Captures user preferences
- `API_LIMIT`: Tracks platform limitations

#### 2.2 Context Extraction
- Improve memory body content quality
- Include relevant code snippets
- Add file paths and line numbers
- Enhanced metadata (source, group_id)

### Phase 3: Task Integration (Priority: HIGH)

#### 3.1 Pre-Task Memory Search
**File**: `.claude/logic/tasks/task_memory_integration.py`
```python
# Features:
- Mandatory search before task execution
- Display "Searched X memories, found Y relevant"
- Block task start if search not performed
- Integration with TodoWrite tool
```

#### 3.2 Post-Task Capture
- Automatic capture of task outcomes
- Error resolution tracking
- Pattern discovery during tasks
- Integration with completion events

### Phase 4: Conversation Buffer v2 (Priority: MEDIUM)

#### 4.1 Enhanced Buffer
**File**: `.claude/logic/memory/conversation_buffer_v2.py`
```python
# Features:
- Track all user<->assistant exchanges
- Immediate capture for critical patterns
- Automatic capture after 5 exchanges
- Smart grouping of related memories
```

### Phase 5: Statistics and Monitoring (Priority: LOW)

#### 5.1 Memory Statistics Tracker
**File**: `.claude/logic/memory/memory_stats_tracker.py`
```python
# Metrics:
- Daily capture count
- Pattern hit rates
- Automation success rate
- Performance metrics
- Session summaries
```

## File Structure Updates

```
.claude/logic/memory/
├── __init__.py
├── commands/
│   └── memory-command.py (update for v2)
├── hooks/
│   ├── memory-context-hook-v2.py (new)
│   └── post-tool-use-memory-v2.py (new)
├── mcp_bridge.py (new)
├── memory_capture_queue.py (new)
├── conversation_buffer_v2.py (new)
├── memory_stats_tracker.py (new)
└── settings.json (update)

.claude/state/
├── memory_queue.json (new)
└── memory_stats.json (new)
```

## Configuration Updates

### settings.json Changes
```json
{
  "memory": {
    "version": "2.0",
    "automation": {
      "level": "full",
      "execution_mode": "direct",
      "batch_size": 5,
      "capture_delay_ms": 100
    },
    "patterns": {
      "existing_patterns": true,
      "code_reuse_patterns": true,
      "client_patterns": true
    },
    "enforcement": {
      "pre_task_search": true,
      "post_task_capture": true,
      "session_tracking": true
    }
  }
}
```

## CLAUDE.md Updates

Add mandatory memory operations section:
- Clear enforcement rules
- Invalid response if skipped
- Session memory counter requirement
- Code reuse pattern capture

## Testing Strategy

### Unit Tests
- MCP bridge execution
- Queue operations
- Pattern detection
- Error handling

### Integration Tests
- End-to-end memory capture
- Task lifecycle integration
- Hook coordination
- Performance benchmarks

### Rollback Plan
1. Disable v2 hooks in settings.json
2. Revert to v1 hooks
3. Clear memory queue
4. Reset statistics
5. Time: < 5 minutes

## Implementation Order

1. **Day 1**: MCP Bridge + Queue System
2. **Day 2**: Memory Context Hook v2
3. **Day 3**: Task Integration
4. **Day 4**: Conversation Buffer v2
5. **Day 5**: Testing and Refinement
6. **Day 6**: Statistics and Monitoring
7. **Day 7**: Documentation and Rollout

## Success Criteria

- [ ] 50+ memories captured per day
- [ ] Zero manual intervention required
- [ ] Memory search before 90% of tasks
- [ ] Capture latency < 100ms
- [ ] Queue processing < 1 second
- [ ] No breaking changes to existing system
- [ ] All tests passing
- [ ] Rollback tested and verified