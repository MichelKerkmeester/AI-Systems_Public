# Memory Automation v2 Test Plan

## Test Objectives

1. Verify direct MCP execution works without user intervention
2. Validate all 4 enforcement layers function correctly
3. Ensure performance targets are met
4. Confirm no regression in existing functionality
5. Validate failover and error handling

## Test Environment

- Neo4j Desktop with Graphiti MCP
- Claude Code CLI (not Desktop app)
- Test dataset with known patterns
- Performance monitoring tools

## Test Phases

### Phase 1: Unit Testing

#### 1.1 Direct MCP Execution
```python
def test_direct_mcp_execution():
    """Test hook can execute MCP calls directly"""
    hook = MemoryContextHookV2()
    
    # Test successful capture
    result = hook.execute_mcp_call(
        "mcp__graphiti-gemini__add_episode",
        {"data": create_test_episode()}
    )
    assert result["status"] == "success"
    
    # Test failure handling
    result = hook.execute_mcp_call(
        "invalid_tool",
        {}
    )
    assert result is None
    assert hook.queue.failed_count() == 1
```

#### 1.2 Queue Management
```python
def test_queue_operations():
    """Test memory queue functionality"""
    queue = MemoryCaptureQueue()
    
    # Test adding memories
    for i in range(10):
        queue.add(create_test_episode(i))
    
    # Test batch retrieval
    batch = queue.get_batch(5)
    assert len(batch) == 5
    
    # Test persistence
    queue2 = MemoryCaptureQueue()
    assert queue2.size() == 5
```

#### 1.3 Pattern Detection
```python
def test_pattern_detection():
    """Test all pattern types are detected"""
    patterns = {
        "DECISION": "We decided to use React for the frontend",
        "SECURITY": "Found a security vulnerability in auth",
        "ERROR_RESOLVED": "Fixed the null pointer exception",
        "OPTIMIZATION": "Optimized query performance by 80%"
    }
    
    for pattern_type, text in patterns.items():
        detected = detect_patterns(text)
        assert pattern_type in detected
```

### Phase 2: Integration Testing

#### 2.1 Conversation Buffer
```bash
# Test conversation flow
python test_conversation_buffer.py << EOF
User: I need to implement authentication
Assistant: I'll implement JWT authentication
User: Make sure it's secure
Assistant: Added security measures including rate limiting
User: Great, that works
Assistant: Authentication system complete with security
EOF

# Verify captures
assert memory_count_increased_by >= 2
```

#### 2.2 Task Lifecycle
```python
def test_task_lifecycle():
    """Test pre/post task memory operations"""
    
    # Start task - should search memories
    task = start_task("Implement user authentication")
    assert task.memories_searched > 0
    
    # Complete task - should capture outcome
    complete_task(task, success=True)
    assert task.memories_captured > 0
```

#### 2.3 CLAUDE.md Enforcement
```bash
# Test that Claude follows memory rules
claude_response = simulate_task_without_memory_search()
assert "invalid" in validate_response(claude_response)

claude_response = simulate_task_with_memory_ops()
assert "valid" in validate_response(claude_response)
```

### Phase 3: System Testing

#### 3.1 End-to-End Workflow
```bash
# Full conversation with automation
./test_e2e_automation.sh

# Verify metrics
- Memories captured: 15+
- Automation rate: >95%
- Search operations: 5+
- No manual captures required
```

#### 3.2 Performance Testing
```python
def test_performance():
    """Ensure no noticeable latency"""
    
    # Measure baseline response time
    baseline = measure_response_time(automation=False)
    
    # Measure with automation
    automated = measure_response_time(automation=True)
    
    # Should be within 100ms
    assert (automated - baseline) < 100
```

#### 3.3 Load Testing
```bash
# Simulate heavy usage
parallel -j 10 ./simulate_conversation.sh ::: {1..10}

# Verify system stability
- Queue processing time < 1s
- No memory leaks
- All captures successful
```

### Phase 4: Failure Testing

#### 4.1 Graphiti Outage
```python
def test_graphiti_failure():
    """Test behavior when Graphiti is down"""
    
    # Simulate Graphiti failure
    stop_graphiti_server()
    
    # Memories should queue
    capture_test_memories(5)
    assert queue_size() == 5
    
    # Restart and verify recovery
    start_graphiti_server()
    wait_for_queue_processing()
    assert queue_size() == 0
```

#### 4.2 Partial Failures
```python
def test_partial_batch_failure():
    """Test batch processing with some failures"""
    
    # Create batch with invalid memory
    batch = [
        valid_memory(),
        invalid_memory(),  # Will fail
        valid_memory()
    ]
    
    process_batch(batch)
    
    # 2 should succeed, 1 should retry
    assert successful_captures() == 2
    assert retry_queue_size() == 1
```

### Phase 5: User Acceptance Testing

#### 5.1 Daily Usage Simulation
```bash
# Run full day simulation
./simulate_workday.sh

# Check metrics
python check_daily_stats.py
# Expected:
# - Total captures: 50-80
# - Automation rate: >95%
# - Pattern coverage: >90%
# - User interventions: <5
```

#### 5.2 A/B Testing
```python
# Compare with control group
control_stats = get_stats(group="control")
test_stats = get_stats(group="automation_v2")

assert test_stats.captures > control_stats.captures * 10
assert test_stats.context_quality > control_stats.context_quality
```

## Test Data

### Pattern Test Cases
```json
{
  "decisions": [
    "I've decided to use PostgreSQL for this",
    "Let's go with the microservices approach",
    "Choosing TypeScript over JavaScript"
  ],
  "errors": [
    "Fixed the memory leak issue",
    "Resolved the authentication bug",
    "Found solution for the race condition"
  ],
  "patterns": [
    "Always use rem units instead of pixels",
    "Pattern: Check for null before accessing",
    "Standard practice is to validate inputs"
  ]
}
```

## Success Criteria

### Functional
- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] E2E workflow captures 15+ memories
- [ ] No manual intervention required
- [ ] Proper error handling and recovery

### Performance
- [ ] Capture latency < 100ms
- [ ] Queue processing < 1s
- [ ] No memory leaks after 1hr
- [ ] Handles 100+ captures/hour

### Quality
- [ ] 95%+ automation rate
- [ ] <1% capture failure rate
- [ ] All patterns detected
- [ ] Relevant memories found

## Test Schedule

- **Week 1**: Unit tests + integration tests
- **Week 2**: System tests + performance tests
- **Week 3**: UAT + A/B testing
- **Week 4**: Final validation + metrics review

## Risk Mitigation

1. **Test in isolated environment first**
2. **Monitor queue sizes closely**
3. **Have manual override ready**
4. **Track all metrics from day 1**
5. **Keep rollback scripts ready**