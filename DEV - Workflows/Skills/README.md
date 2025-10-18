# SpecKit Skills Integration Guide

Complete documentation of how all SpecKit skills work together in the ecosystem.

## Skills Overview

The SpecKit system consists of 5 specialized skills:

1. **speckit-command-guide** - Navigation and command recommendations
2. **speckit_parallel_complete** - Complete 14-step workflow orchestration
3. **speckit_parallel_feature_research** - Parallel technical research
4. **speckit_parallel_implementation** - Autonomous implementation execution
5. **speckit_parallel_plan_spec** - Planning and specification with approvals

## Architecture Diagram

```
                    User Request
                          ↓
              ┌───────────────────────┐
              │ speckit-command-guide │ ← Entry point for navigation
              └───────────────────────┘
                          ↓
                 Recommends Command
                          ↓
        ┌─────────────────────────────────────┐
        │         User Executes Command       │
        └─────────────────────────────────────┘
                          ↓
    Command triggers appropriate parallel skill:
                          ↓
    ┌────────────────────────────────────────────────┐
    │                                                │
    ├─ speckit_parallel_complete (Full workflow)    │
    ├─ speckit_parallel_feature_research  (Research) │
    ├─ speckit_parallel_implementation (Implementation)   │
    └─ speckit_parallel_plan_spec (Planning phase)  │
    └────────────────────────────────────────────────┘
                          ↓
                   Parallel Execution
                          ↓
                  Results to User
```

## Skill Responsibilities

### 1. speckit-command-guide
- **Type**: Navigation Layer
- **Purpose**: Recommend next SpecKit command
- **Complexity**: Simple (<400 lines)
- **Sub-agents**: None
- **Token Usage**: Minimal
- **When Used**: User needs guidance on workflow

### 2. speckit_parallel_complete
- **Type**: Full Orchestration
- **Purpose**: Execute complete 14-step workflow
- **Complexity**: Complex (18 sub-agents)
- **Sub-agents**: 3 stages × 6 agents each
- **Token Usage**: Very High
- **When Used**: Full feature development cycle

### 3. speckit_parallel_feature_research
- **Type**: Research Execution
- **Purpose**: Parallel technical investigation
- **Complexity**: Medium (6 sub-agents)
- **Sub-agents**: 4 researchers + review + synthesis
- **Token Usage**: High
- **When Used**: Before specification, need research

### 4. speckit_parallel_implementation
- **Type**: Implementation Execution
- **Purpose**: Autonomous code implementation
- **Complexity**: Medium (6 sub-agents)
- **Sub-agents**: 4 preparers + review + synthesis
- **Token Usage**: High
- **When Used**: Ready to build from specs

### 5. speckit_parallel_plan_spec
- **Type**: Planning Execution
- **Purpose**: Technical planning with approvals
- **Complexity**: Medium (6 sub-agents)
- **Sub-agents**: 4 analysts + review + synthesis
- **Token Usage**: High
- **When Used**: Creating technical plans

## Command to Skill Mapping

| SpecKit Command | Primary Skill | Sub-agents | Execution Time |
|-----------------|---------------|------------|----------------|
| `/speckit.specify` | (built-in) | None | 10-20s |
| `/speckit.clarify` | (built-in) | None | 5-10s |
| `/speckit.plan` | speckit_parallel_plan_spec | 6 agents | 2-3 min |
| `/speckit.tasks` | (built-in) | None | 10-15s |
| `/speckit.implement` | speckit_parallel_implementation | 6 agents | Variable |
| `/speckit.analyze` | speckit_parallel_complete | 4 agents | 1-2 min |
| `/speckit.checklist` | (built-in) | None | 5-10s |
| `/speckit.constitution` | (built-in) | None | 10-15s |
| (research) | speckit_parallel_feature_research | 6 agents | 2-5 min |
| (full workflow) | speckit_parallel_complete | 18 agents | 10-15 min |

## Usage Patterns

### Pattern 1: Complete Feature Development

```
1. User: "I need to build feature X"
2. speckit-command-guide: Recommends /speckit.specify
3. User: Runs /speckit.specify
4. speckit-command-guide: Recommends /speckit.plan
5. User: Runs /speckit.plan
6. speckit_parallel_plan_spec: Executes parallel planning (6 agents)
7. User: Reviews plan.md
8. speckit-command-guide: Recommends /speckit.tasks
9. User: Runs /speckit.tasks
10. speckit-command-guide: Recommends /speckit.implement
11. User: Runs /speckit.implement
12. speckit_parallel_implementation: Executes implementation (6 agents)
```

### Pattern 2: Research Before Planning

```
1. User: "I need to research authentication options"
2. speckit_parallel_feature_research: Executes research (6 agents)
3. User: Reviews research.md
4. speckit-command-guide: Recommends /speckit.specify
5. Continue with standard flow...
```

### Pattern 3: Full Automated Workflow

```
1. User: "Execute complete SpecKit workflow for feature X"
2. speckit_parallel_complete: Runs all 14 steps
   - Stage A: Planning (6 agents)
   - Stage B: Implementation prep (6 agents)
   - Stage C: Quality review (6 agents)
3. User: Approves at each gate
4. Complete feature delivered
```

### Pattern 4: Planning Only

```
1. User: "Create technical plan for existing spec"
2. speckit_parallel_plan_spec: Executes planning
   - Requirements analysis
   - Architecture design
   - Risk assessment
   - Estimation
3. User: Reviews and approves plan.md
```

## Inter-Skill Communication

### Shared State

Skills communicate through artifacts:

```yaml
shared_artifacts:
  specifications:
    - spec.md
    - clarifications.md
  planning:
    - plan.md
    - planning-summary.md
    - research.md
  implementation:
    - implementation_plan.md
    - implementation-summary.md
  tasks:
    - tasks/checklist.md
  quality:
    - analysis/consistency-report.md
    - quality_report.md
```

### State Detection

```javascript
// Each skill can detect current state
function detectWorkflowState() {
  return {
    hasSpec: exists('spec.md'),
    hasPlan: exists('plan.md'),
    hasTasks: exists('tasks/checklist.md'),
    hasImplementation: exists('implementation-summary.md'),
    hasResearch: exists('research.md')
  };
}
```

### Handoff Points

1. **Research → Specification**
   - Output: research.md
   - Input to: /speckit.specify

2. **Specification → Planning**
   - Output: spec.md
   - Input to: speckit_parallel_plan_spec

3. **Planning → Tasks**
   - Output: plan.md
   - Input to: /speckit.tasks

4. **Tasks → Implementation**
   - Output: tasks/checklist.md
   - Input to: speckit_parallel_implementation

## Parallel Execution Patterns

### Common Pattern: 4 Workers + Review + Synthesis

All specialized skills follow this pattern:

```
┌─────────────────────────────────┐
│      4 Parallel Workers          │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │ W1 │ │ W2 │ │ W3 │ │ W4 │   │
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
         Lead Reviewer
                ↓
         Lead Synthesizer
                ↓
         Main Agent QA
                ↓
         User Approval (if needed)
```

### Execution Comparison

| Skill | Workers | Reviewer | Synthesizer | Approval Gates |
|-------|---------|----------|-------------|----------------|
| speckit_parallel_complete | 4×3 stages | 3 reviewers | 3 synthesizers | 14 gates |
| speckit_parallel_feature_research | 4 researchers | 1 reviewer | 1 synthesizer | None |
| speckit_parallel_implementation | 4 preparers | 1 reviewer | 1 synthesizer | None |
| speckit_parallel_plan_spec | 4 analysts | 1 reviewer | 1 synthesizer | 3 gates |

## Performance Optimization

### Token Usage Strategy

```yaml
optimization:
  command_guide:
    load: always          # Small, stateless
    cache: none          # No benefit

  speckit_parallel_complete:
    load: on_demand      # Very large
    cache: aggressive    # Expensive to reload

  speckit_parallel_feature_research:
    load: on_demand      # Medium size
    cache: moderate      # Some reuse expected

  speckit_parallel_implementation:
    load: on_demand      # Medium size
    cache: minimal       # Rarely reused

  speckit_parallel_plan_spec:
    load: on_demand      # Medium size
    cache: moderate      # Planning iterations common
```

### Concurrency Management

```yaml
concurrency_limits:
  default: 3
  high_complexity: 2
  resource_constrained: 1

  per_skill:
    speckit_parallel_complete: 3    # Can handle high load
    speckit_parallel_feature_research: 3     # Research parallelizable
    speckit_parallel_implementation: 2       # Memory intensive
    speckit_parallel_plan_spec: 3           # Analysis parallelizable
```

## Error Handling

### Skill Failure Recovery

```python
def handle_skill_failure(skill, error):
    fallback_map = {
        'speckit_parallel_complete': 'Try individual commands',
        'speckit_parallel_feature_research': 'Manual research required',
        'speckit_parallel_implementation': 'Manual implementation needed',
        'speckit_parallel_plan_spec': 'Use /speckit.plan directly'
    }

    return {
        'error': error,
        'fallback': fallback_map[skill],
        'recovery': 'Check artifacts and retry'
    }
```

### Cross-Skill Failures

If one skill fails, others can often continue:
- Research failure → Can still specify
- Planning failure → Can research alternatives
- Implementation failure → Can replan

## Best Practices

### DO:
- Start with command-guide for navigation
- Use specialized skills for parallel work
- Check artifacts between skill executions
- Allow skills to share context through files
- Monitor token usage across skills

### DON'T:
- Load all skills simultaneously
- Skip the command guide
- Mix skill responsibilities
- Ignore approval gates
- Cache sensitive data

### ALWAYS:
- Verify prerequisites before skill execution
- Document skill handoffs
- Maintain artifact consistency
- Provide user visibility
- Enable manual override

## Skill Selection Guide

### Decision Tree

```
Need guidance on what to do next?
└─ YES → speckit-command-guide

Need comprehensive research?
└─ YES → speckit_parallel_feature_research

Have spec, need technical plan?
└─ YES → speckit_parallel_plan_spec

Ready to implement with specs/plan?
└─ YES → speckit_parallel_implementation

Want complete automated workflow?
└─ YES → speckit_parallel_complete
```

### Quick Reference

| Scenario | Recommended Skill |
|----------|-------------------|
| "What command should I run?" | speckit-command-guide |
| "Research authentication options" | speckit_parallel_feature_research |
| "Create technical architecture" | speckit_parallel_plan_spec |
| "Implement this feature" | speckit_parallel_implementation |
| "Do everything automatically" | speckit_parallel_complete |

## Integration Testing

### Test Scenarios

1. **End-to-end workflow**
   - Start: No artifacts
   - Use: All skills in sequence
   - Verify: Complete feature delivered

2. **Parallel skill coordination**
   - Start: Multiple skills needed
   - Use: Skills in parallel
   - Verify: No conflicts

3. **Failure recovery**
   - Start: Skill execution
   - Inject: Failure condition
   - Verify: Graceful fallback

### Integration Points to Test

- Command guide → Each parallel skill
- Research output → Planning input
- Planning output → Implementation input
- Artifact consistency across skills
- Approval gate handling

## Version Compatibility

| Skill | Version | Compatible With | Based On |
|-------|---------|-----------------|----------|
| speckit-command-guide | 2.0.0 | All versions | N/A |
| speckit_parallel_complete | 1.0.0 | All versions | sk_p__complete.yaml |
| speckit_parallel_feature_research | 1.0.0 | All versions | sk_p__feature_research.yaml |
| speckit_parallel_implementation | 1.0.0 | All versions | sk_p__implementation.yaml |
| speckit_parallel_plan_spec | 1.0.0 | All versions | sk_p__plan_spec.yaml |

## Future Enhancements

### Planned Improvements

1. **Unified Orchestrator**: Meta-skill that coordinates all skills
2. **Parallel Skill Execution**: Run multiple skills simultaneously
3. **State Persistence**: Save workflow state between sessions
4. **Custom Workflows**: User-defined skill sequences
5. **Performance Metrics**: Track execution patterns

### Extension Points

```yaml
extensions:
  custom_agents:
    location: .claude/agents/
    format: yaml

  custom_workflows:
    location: .claude/workflows/
    format: yaml

  skill_plugins:
    location: .claude/plugins/
    format: python
```

## Troubleshooting

### Common Issues

**Issue**: Skills not triggering
**Solution**: Check command format matches exactly

**Issue**: Parallel execution timeout
**Solution**: Reduce concurrency or increase timeouts

**Issue**: Artifact mismatch between skills
**Solution**: Verify file paths and naming conventions

**Issue**: Token limit exceeded
**Solution**: Use skills sequentially, not in parallel

**Issue**: Approval gates blocking
**Solution**: Ensure user provides explicit approval

## Summary

The SpecKit skill ecosystem provides:

- **Navigation**: Command guide for workflow guidance
- **Research**: Parallel technical investigation
- **Planning**: Comprehensive planning with approvals
- **Implementation**: Autonomous code execution
- **Orchestration**: Complete workflow automation

Together, these skills enable efficient, parallel execution of complex software development workflows while maintaining clarity and control.