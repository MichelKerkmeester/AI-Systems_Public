---
name: speckit_parallel_complete
description: Execute the complete 14-step SpecKit workflow with 18 specialized sub-agents running in 3 parallel stages. Implements the full sk_p__complete.yaml workflow with approval gates, review/synthesis phases, and adaptive rules for complexity handling.
---

# SpecKit Parallel Complete

Execute the complete SpecKit workflow with parallel sub-agent orchestration as defined in the sk_p__complete.yaml specification.

## When to Use This Skill

**Use this skill when**:
- SpecKit commands need to execute their underlying parallel workflows
- `/speckit.plan` needs to run 4 specialist agents in parallel
- `/speckit.implement` needs to coordinate implementation agents
- `/speckit.analyze` needs parallel quality reviewers
- Complex workflows require orchestration of multiple agents

**Do NOT use this skill for**:
- Simple command recommendations (use speckit-command-guide)
- Single-agent tasks
- Sequential workflows without parallelization needs

## Architecture Overview

This skill implements the complete 14-step workflow with 18 specialized sub-agents organized into 3 parallel execution stages.

### The 14 Workflow Steps

1. **Request Analysis** - Parse and understand requirements
2. **Pre-work Review** - Review AGENTS.md, constitution, knowledge base
3. **Specification** - Create spec.md with `/speckit.specify`
4. **Clarification** - Resolve ambiguities with `/speckit.clarify`
5. **Quality Checklist** - Generate checklists with `/speckit.checklist`
6. **Parallel Planning** (Stage A) - 4 specialist agents + review + synthesis
7. **Task Breakdown** - Generate tasks with `/speckit.tasks`
8. **Analysis** - Check consistency with `/speckit.analyze`
9. **Parallel Implementation Prep** (Stage B) - 4 implementation agents
10. **Implementation Check** - Verify prerequisites
11. **Development** - Execute code changes
12. **Parallel Quality Review** (Stage C) - 4 quality reviewers
13. **Completion** - Document changes
14. **Branch Integration** - Merge to main

### The 18 Sub-Agents

**Note**: For complete sub-agent role definitions and output specifications, see [references/sub-agents.md](references/sub-agents.md).

**Stage A: Planning/Spec (Step 6)**
1. Requirements Analyst
2. Solution Architect
3. Risk/Compliance Analyst
4. Estimation/Scope Analyst
5. Lead Reviewer A
6. Lead Synthesizer A

**Stage B: Implementation Prep (Step 9)**
7. Core Implementer
8. Integrations/Adapters Engineer
9. Test Engineer
10. Docs Engineer
11. Integration Reviewer B
12. Lead Synthesizer B

**Stage C: Quality Review (Step 12)**
13. Completeness Reviewer
14. Feasibility Reviewer
15. Security/Privacy Reviewer
16. Consistency/Traceability Reviewer
17. Lead Reviewer C
18. Lead Synthesizer C

## Execution Model

### Parallel Block Pattern

Each parallel stage follows this pattern:

```
┌─────────────────────────────────┐
│     Parallel Agent Execution     │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │ A1 │ │ A2 │ │ A3 │ │ A4 │   │ ← Execute in parallel
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│         Review Phase             │ ← Lead Reviewer consolidates
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Synthesis Phase           │ ← Lead Synthesizer creates output
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Main Agent QA Phase         │ ← Main agent finalizes
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Approval Gate             │ ← User approval required
└─────────────────────────────────┘
```

## Stage A: Planning/Spec (Step 6)

**Note**: This stage executes as part of the workflow's step 6 parallel planning block. The association with `/speckit.plan` is inferred from workflow context.

### Sub-Agents

**Requirements Analyst**:
- Extracts functional requirements
- Identifies constraints
- Defines success metrics
- Maps dependencies

**Solution Architect**:
- Designs components
- Defines interfaces
- Maps data flow
- Considers architecture patterns

**Risk/Compliance Analyst**:
- Identifies risks with severity
- Defines mitigations
- Checks compliance requirements
- Analyzes edge cases

**Estimation/Scope Analyst**:
- Creates milestones
- Defines sequencing
- Provides effort ranges
- Documents assumptions

### Review & Synthesis

**Lead Reviewer A**:
- Reconciles conflicting recommendations
- Validates completeness
- Resolves contradictions
- Provides synthesis guidance

**Lead Synthesizer A**:
- Creates plan.md
- Generates planning-summary.md
- Integrates all findings
- Ensures coherence

### Outputs
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

## Stage B: Implementation Prep (Step 9)

**Note**: This stage executes as part of the workflow's step 9 parallel implementation preparation block. Runs before actual implementation begins.

### Sub-Agents

**Core Implementer**:
- Defines modules
- Designs data structures
- Plans algorithms
- Maps business logic

**Integrations/Adapters Engineer**:
- Defines integrations
- Creates API contracts
- Plans configuration
- Error handling strategies

**Test Engineer**:
- Creates test plan
- Defines test cases
- Prepares fixtures
- Sets coverage targets

**Docs Engineer**:
- Plans usage documentation
- Creates examples
- Prepares migration guides
- API documentation

### Review & Synthesis

**Integration Reviewer B**:
- Ensures API coherence
- Validates testability
- Checks quality standards
- Provides integration guidance

**Lead Synthesizer B**:
- Creates implementation_plan.md
- Coordinates approaches
- Synthesizes strategies
- Ensures alignment

### Outputs
- `[SPEC_FOLDER]/implementation_plan.md`

## Stage C: Quality Review (Step 12)

**Note**: This stage executes as part of the workflow's step 12 parallel quality review block. Provides comprehensive quality validation after development.

### Sub-Agents

**Completeness Reviewer**:
- Checks coverage gaps
- Validates non-functionals
- Ensures requirements met
- Identifies missing pieces

**Feasibility Reviewer**:
- Validates technical viability
- Checks performance implications
- Assesses scalability
- Reviews constraints

**Security/Privacy Reviewer**:
- Identifies vulnerabilities
- Checks authentication/authorization
- Reviews encryption needs
- Validates input handling

**Consistency/Traceability Reviewer**:
- Finds contradictions
- Checks terminology consistency
- Validates references
- Ensures traceability

### Review & Synthesis

**Lead Reviewer C**:
- Assesses severity
- Prioritizes issues
- Provides resolution guidance
- Creates action items

**Lead Synthesizer C**:
- Creates quality_report.md
- Consolidates findings
- Generates recommendations
- Provides summary

### Outputs
- `[SPEC_FOLDER]/quality_report.md`

## Approval Gates

Each step has a mandatory approval gate:

| Step | Approval Prompt |
|------|-----------------|
| 1→2 | "Requirements analyzed. Proceed to pre-work review?" |
| 2→3 | "Pre-work documentation reviewed. Proceed to specification?" |
| 3→4 | "Specification created. Review spec.md and approve to proceed?" |
| 4→5 | "Requirements clarified. Proceed to quality checklist?" |
| 5→6 | "Quality checklist complete. Proceed to planning parallel block?" |
| 6→7 | "Planning artifacts synthesized. Approve to proceed to task breakdown?" |
| 7→8 | "Tasks broken down. Review and approve to proceed to analysis?" |
| 8→9 | "Analysis complete. Approve to proceed to implementation prep?" |
| 9→10 | "Implementation plan synthesized. Approve to proceed?" |
| 10→11 | "Prerequisites verified. APPROVE TO BEGIN CODE IMPLEMENTATION?" |
| 11→12 | "Development complete. Proceed to quality review?" |
| 12→13 | "Quality review complete. Approve to proceed to completion?" |
| 13→14 | "Implementation summary complete. Approve to finalize?" |
| 14 | "All checks passed. Push to main now?" |

## Adaptive Rules

**Note**: For detailed adaptive rule specifications and decision trees, see [references/adaptive-rules.md](references/adaptive-rules.md).

### High Complexity
When complexity is high:
- Reduce concurrency from 3 to 2
- Increase review depth to exhaustive
- Add discovery microsteps
- Use effort ranges instead of point estimates

### High Uncertainty
When uncertainty is high:
- Insert discovery steps before parallel blocks
- Add validation checkpoints
- Increase clarification depth
- Document assumptions explicitly

### Fallback Strategy
If parallel execution fails:
- Run tasks sequentially
- Maintain review and synthesis phases
- Document degraded mode
- Continue with partial results

## Field Handling

### Auto-Creation
- **git_branch**: Auto-create `feature-{NNN}` from highest +001
- **spec_folder**: Auto-create `specs/{NNN}` from highest +001
- **context**: Infer from request and staging link
- **issues**: Discover during workflow execution

### Scope Policy
- **Default**: `specs/**`
- **Enforcement**: Limit file operations to scope
- **Validation**: Block operations outside scope

## Integration Points

### With speckit-command-guide
- Command guide recommends commands
- Executor handles parallel execution
- Clear handoff at command boundaries

### With Chrome DevTools
- Stage A: Analyze current implementation
- Stage B: Validate environment
- Stage C: Compare staging vs spec

### With Manual Steps
- Approval gates require user confirmation
- Review artifacts between stages
- Manual fixes for identified issues

## Performance Characteristics

**Note**: Performance varies based on system resources, complexity, and agent response efficiency.

- **Parallel Execution**: Significantly faster than sequential execution
- **Stage A**: Parallel execution of 4 planning agents + review + synthesis
- **Stage B**: Parallel execution of 4 implementation agents + review + synthesis
- **Stage C**: Parallel execution of 4 quality reviewers + review + synthesis
- **Orchestration**: Minimal overhead for coordination between stages

## Error Handling

### Retry Policy
- **Targeted retries**: Only failed agents
- **Max retries**: 2 per agent
- **Backoff**: Exponential with jitter

### Failure Modes
- **Agent failure**: Retry then fallback to sequential
- **Review failure**: Escalate to main agent
- **Synthesis failure**: Use partial results
- **Approval rejection**: Document and stop

## Limitations

- **Requires parallel execution support**: Falls back to sequential if unavailable
- **Memory intensive**: 18 agents require significant context
- **Approval gates mandatory**: Cannot skip user confirmations
- **English only**: Agent prompts and outputs in English

## Success Metrics

**Note**: Target quality metrics for workflow execution. These represent ideal performance goals.

- **Parallel efficiency**: Significant performance improvement vs sequential
- **Agent success rate**: >95% first attempt
- **Synthesis quality**: >90% coherence score
- **Approval rate**: >80% first-time approvals

## Version

**Current Version**: 1.0.0
**Based On**: sk_p__complete.yaml
**Created**: 2025-10-18
**Architecture**: Parallel sub-agent orchestration

---

## References

- `references/sub-agents.md` - Detailed sub-agent definitions
- `references/parallel-stages.md` - Stage orchestration patterns
- `references/adaptive-rules.md` - Complexity handling rules