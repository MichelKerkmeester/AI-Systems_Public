# Simple Task Example

This example demonstrates how the multi-agent system handles a simple task efficiently.

## Task: Fix a Typo in README

### 1. Input
```bash
/logic agents orchestrate "Fix typo in README: change 'teh' to 'the'"
```

### 2. Task Analysis
The system analyzes the task:
```python
{
    "complexity_score": 1,
    "complexity_level": "TRIVIAL",
    "task_type": "bug_fix",
    "keywords_found": ["fix", "typo"],
    "estimated_tokens": 500
}
```

### 3. Model Selection
Based on the analysis:
```python
{
    "primary_model": "kimi-pro",
    "fallback_model": "claude-opus-4",
    "reasoning": "Simple task suitable for Kimi Pro",
    "estimated_cost": 0.009,  # $0.009
    "confidence": 0.95
}
```

### 4. Agent Spawning
A single developer agent is spawned:
```
[2025-01-19T10:00:00] Spawning developer_1 for wp_12345
[2025-01-19T10:00:01] Creating worktree at .claude/agents/worktrees/developer_1
```

### 5. Execution
The developer agent:
1. Searches for "teh" in README files
2. Identifies the typo location
3. Makes the correction
4. Validates the change

### 6. Result
```python
{
    "status": "completed",
    "agent": "developer_1",
    "model_used": "kimi-pro",  # Or "claude-opus-4" if Kimi fails
    "changes": [
        {
            "file": "README.md",
            "line": 42,
            "old": "teh project",
            "new": "the project"
        }
    ],
    "cost": 0.009,
    "time_ms": 1250,
    "cost_savings": "60%"  # If Kimi worked
}
```

### 7. Complete Code Example

```python
import asyncio
from orchestration import orchestrator_command

async def fix_typo_example():
    """Example: Fix a typo using the multi-agent system"""
    
    # Create orchestration request
    task = "Fix typo in README: change 'teh' to 'the'"
    
    # Execute orchestration
    result = await orchestrator_command.handle_orchestrate(task)
    
    # Print results
    print(f"Task completed by: {result['agent']}")
    print(f"Model used: {result['model_used']}")
    print(f"Cost: ${result['cost']:.3f}")
    print(f"Savings: {result['cost_savings']}")
    
    # Show changes
    for change in result['changes']:
        print(f"\nFile: {change['file']}")
        print(f"Line {change['line']}: '{change['old']}' → '{change['new']}'")

# Run the example
if __name__ == "__main__":
    asyncio.run(fix_typo_example())
```

### 8. Cost Analysis

**With Kimi Pro (when working):**
- Input tokens: ~300
- Output tokens: ~200
- Cost: $0.009
- Savings: 60% vs Claude

**With Claude (fallback):**
- Input tokens: ~300
- Output tokens: ~200
- Cost: $0.023
- Savings: 0%

### 9. Performance Metrics

- Task analysis: 15ms
- Model selection: 3ms
- Agent spawn: 1.2s
- Task execution: 1.0s
- Total time: ~2.2s

### 10. What Happens Behind the Scenes

1. **Complexity Analysis**: Keywords "fix" and "typo" score low complexity
2. **Model Routing**: TRIVIAL complexity routes to Kimi Pro
3. **Single Agent**: Only one developer agent needed
4. **No Synthesis**: Single agent means no synthesis required
5. **Automatic Cleanup**: Worktree removed after completion

This demonstrates the system's efficiency for simple tasks, achieving significant cost savings while maintaining quality.