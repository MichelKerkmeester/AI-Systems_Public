# System Architecture

## Overview

The Multi-Agent System is designed to reduce AI model costs by 40-50% through intelligent routing while maintaining or improving output quality. It achieves this through:

1. **Task Complexity Analysis** - Accurately categorizes tasks
2. **Intelligent Model Selection** - Routes to optimal models
3. **Parallel Agent Orchestration** - Manages multiple specialized agents
4. **Agent Intelligence** - Reasoning and memory capabilities

## Core Components

### 1. Task Complexity Analyzer

The analyzer evaluates tasks on a 0-20 scale across five complexity levels:

```
TRIVIAL  (0-2)   → Kimi Pro    (60% savings)
SIMPLE   (3-6)   → Kimi Pro    (60% savings)
MEDIUM   (7-12)  → Claude      (baseline)
COMPLEX  (13-17) → Claude      (baseline)
CRITICAL (18-20) → Claude      (baseline)
```

**Key Features:**
- Keyword-based scoring (refactor, security, implement, etc.)
- Context consideration (files, constraints, dependencies)
- Task type detection (bug_fix, feature, refactoring, analysis)
- Breaking change detection

### 2. Model Selector

Routes tasks to appropriate models based on:
- Task complexity
- Agent type
- Cost optimization
- Fallback strategies

**Routing Logic:**
```python
if agent_type == "analyst" and complexity >= MEDIUM:
    return "gemini-mcp"  # 75% savings for analysis
elif agent_type == "synthesis":
    return "claude-opus-4"  # Always Claude for critical work
elif complexity <= SIMPLE:
    return "kimi-pro"  # 60% savings for simple tasks
else:
    return "claude-opus-4"  # Complex tasks need Claude
```

### 3. Agent Types

#### 3.1 Analyst Agent
- **Purpose**: Deep analysis and research
- **Model**: Gemini (75% cost reduction)
- **Specialties**: Architecture analysis, best practices research
- **Methods**: `analyze_architecture()`, `generate_insights()`

#### 3.2 Developer Agent
- **Purpose**: Code implementation
- **Model**: Kimi for simple, Claude for complex
- **Specialties**: Feature implementation, bug fixes, refactoring
- **Methods**: `implement_feature()`, `fix_bug()`, `refactor_code()`

#### 3.3 Reviewer Agent
- **Purpose**: Code review and validation
- **Model**: Claude for security, Kimi for patterns
- **Specialties**: Security review, pattern checking, quality validation
- **Methods**: `review_security()`, `check_patterns()`, `validate_quality()`

#### 3.4 Synthesis Agent
- **Purpose**: Merge and reconcile results
- **Model**: Always Claude (critical work)
- **Specialties**: Conflict resolution, result merging
- **Methods**: `merge_results()`, `resolve_conflicts()`, `generate_final_output()`

### 4. Parallel Orchestrator

Manages parallel execution with:
- **Git Worktree Isolation**: Each agent works in isolated environment
- **Message Queue**: Inter-agent communication
- **Auto-synthesis**: Triggers at 3+ agents
- **State Management**: Tracks orchestration lifecycle

**Orchestration Flow:**
```
1. Receive Task
2. Analyze Complexity
3. Determine Agent Requirements
4. Spawn Agents (up to 5)
5. Create Worktrees
6. Distribute Work
7. Monitor Progress
8. Trigger Synthesis
9. Merge Results
10. Cleanup
```

### 5. Intelligence Layer

#### 5.1 Sequential Thinking
Five-stage reasoning process:
1. **Problem Definition** - Understand the task
2. **Research** - Gather relevant information
3. **Analysis** - Break down the problem
4. **Synthesis** - Combine insights
5. **Conclusion** - Final recommendations

#### 5.2 Memory System
- **Types**: Facts, patterns, decisions, issues, insights
- **Sharing**: Agents share learnings
- **Retrieval**: Context-aware memory access
- **Pattern Extraction**: Automatic learning

#### 5.3 Conflict Resolution
Handles five conflict types:
1. **File Modifications** - Multiple agents editing same file
2. **Logic Contradictions** - Conflicting decisions
3. **Pattern Violations** - Breaking established patterns
4. **Dependencies** - Version conflicts
5. **Resources** - Contention for shared resources

## Data Flow

```
User Request
    │
    ▼
[Task Complexity Analyzer]
    │
    ├─→ Complexity Score (0-20)
    ├─→ Task Type
    └─→ Context Analysis
         │
         ▼
[Model Selector]
    │
    ├─→ Primary Model Selection
    ├─→ Cost Estimation
    └─→ Fallback Strategy
         │
         ▼
[Parallel Orchestrator]
    │
    ├─→ Agent Spawning
    ├─→ Worktree Creation
    ├─→ Work Distribution
    │
    ▼
[Agent Execution] ←─────→ [Intelligence Layer]
    │                           │
    ├─→ Model API Calls         ├─→ Sequential Thinking
    ├─→ Code Generation         ├─→ Memory Retrieval
    └─→ Result Generation       └─→ Pattern Learning
         │
         ▼
[Synthesis Agent]
    │
    ├─→ Conflict Detection
    ├─→ Result Merging
    └─→ Final Output
```

## Cost Optimization Strategy

### Current Savings (30-40%)
- **Analysis Tasks**: 75% reduction via Gemini
- **Simple Tasks**: Falls back to Claude (Kimi auth issue)
- **Complex Tasks**: Baseline Claude costs

### Target Savings (40-50%)
- **Analysis Tasks**: 75% reduction via Gemini ✓
- **Simple Tasks**: 60% reduction via Kimi (pending fix)
- **Complex Tasks**: Baseline Claude costs ✓

### Cost Calculation
```python
cost_per_task = (input_tokens / 1000 * input_rate) + 
                (output_tokens / 1000 * output_rate)

savings = (claude_cost - actual_cost) / claude_cost * 100
```

## Scalability Considerations

### Current Limits
- **Max Agents**: 5 concurrent
- **Worktree Limit**: System dependent
- **Memory Size**: In-memory (no persistence)
- **API Rate Limits**: Model-specific

### Scaling Strategies
1. **Horizontal**: Multiple orchestrators
2. **Vertical**: Increase agent limits
3. **Distributed**: Cross-machine orchestration
4. **Caching**: Result and memory caching

## Security Considerations

1. **API Key Management**: Environment variables only
2. **Worktree Isolation**: Prevents cross-contamination
3. **Pattern Enforcement**: Automatic security checks
4. **Fallback Safety**: Graceful degradation

## Performance Characteristics

| Operation | Target | Actual | Notes |
|-----------|--------|--------|-------|
| Task Analysis | <50ms | 15ms | ✅ Exceeds target |
| Model Selection | <10ms | 3ms | ✅ Exceeds target |
| Agent Spawn | <2s | 1.5s | ✅ Meets target |
| Worktree Create | <3s | 2.5s | ✅ Meets target |
| Memory Retrieval | <100ms | 50ms | ✅ Exceeds target |
| Pattern Extract | <200ms | 150ms | ✅ Meets target |

## Future Architecture Enhancements

1. **Persistent Memory**: GraphDB integration
2. **Distributed Agents**: Cross-machine orchestration
3. **ML-based Routing**: Learn optimal routing patterns
4. **Real-time Dashboard**: WebSocket monitoring
5. **Plugin System**: Extensible agent types