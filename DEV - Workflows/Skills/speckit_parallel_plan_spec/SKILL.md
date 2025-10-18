---
name: speckit_parallel_plan_spec
description: Execute spec-driven planning workflow with parallel specialist analyses. Orchestrates 6 specialized planning sub-agents through parallel execution, review, and synthesis to produce plan.md and planning-summary.md with manual approval gates.
---

# SpecKit Plan & Spec

Execute comprehensive planning and specification workflow with parallel specialist analyses and approval gates.

## When to Use This Skill

**Use this skill when**:
- Creating technical plans from specifications
- Need parallel analysis from multiple specialists
- Require comprehensive risk and architecture assessment
- Want estimation and milestone planning
- Following manual approval workflow

**Do NOT use this skill for**:
- Quick planning without parallel analysis
- Implementation execution (use speckit-implementation)
- Research tasks (use speckit-feature-research)
- Automated workflows without approvals

## Architecture Overview

This skill implements the sk_p__plan_spec.yaml workflow with 6 specialized planning sub-agents executing in parallel analysis phase.

### Planning Workflow Steps

1. **Request Analysis** - Analyze inputs and confirm understanding
2. **Pre-work Review** - Review AGENTS.md and constitution
3. **Specification** - Create spec.md with acceptance criteria
4. **Clarification** - Resolve ambiguities and clarify requirements
5. **Quality Checklist** - Generate quality validation checklist
6. **Parallel Planning Block** - 4 analysts work in parallel
7. **Planning** - Finalize technical approach and plan.md

### The 6 Planning Sub-Agents

**Note**: For detailed agent specifications and output formats, see [references/sub-agents.md](references/sub-agents.md).

1. **Requirements Analyst**
   - Extract requirements
   - Define constraints
   - Map dependencies
   - Create success metrics

2. **Solution Architect**
   - Design architecture
   - Define components
   - Map interfaces
   - Document data flows

3. **Risk/Compliance Analyst**
   - Identify risks
   - Assess severity
   - Define mitigations
   - Check compliance

4. **Estimation/Scope Analyst**
   - Create milestones
   - Sequence phases
   - Estimate effort
   - Document assumptions

5. **Lead Reviewer**
   - Reconcile outputs
   - Resolve conflicts
   - Validate completeness
   - Identify gaps

6. **Lead Synthesizer**
   - Generate plan.md
   - Create planning-summary.md
   - Integrate findings
   - Format artifacts

## Execution Model

### Parallel Planning Pattern

```
┌─────────────────────────────────┐
│    Parallel Planning Analysis    │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │Req │ │Arch│ │Risk│ │Est │   │ ← Execute in parallel
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│         Review Phase             │ ← Lead Reviewer reconciles
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Synthesis Phase           │ ← Lead Synthesizer creates docs
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Main Agent QA Phase         │ ← Final validation
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Approval Gate             │ ← User approval required
└─────────────────────────────────┘
```

## Planning Document Structure

The skill produces two key documents:

### plan.md Structure

**Technical Approach**
- Architecture overview
- Component design
- Integration strategy
- Technology choices

**Implementation Phases**
- Phase breakdown
- Milestone definitions
- Dependencies mapping
- Timeline estimates

**Risk Assessment**
- Identified risks
- Severity levels
- Mitigation strategies
- Contingency plans

**Success Metrics**
- Measurable objectives
- Acceptance criteria
- Performance targets
- Quality indicators

### planning-summary.md Structure

**Executive Summary**
- Feature overview
- Key decisions
- Critical risks
- Timeline summary

**Recommended Next Steps**
- Immediate actions
- Prerequisite tasks
- Resource needs
- Decision points

## Approval Gates

This workflow includes manual approval gates at key points:

| Step | Approval Prompt |
|------|-----------------|
| 1→2 | "Requirements analyzed. Proceed to pre-work review?" |
| 4→5 | "Requirements clarified. Proceed to quality checklist?" |
| 6→7 | "Planning artifacts synthesized. Approve to proceed?" |

## Inputs

### Required Inputs
- **request**: Feature description or requirements
- **spec_folder**: Location for planning artifacts

### Optional Inputs
- **git_branch**: Feature branch name
- **context**: Additional planning context
- **issues**: Known issues to address
- **environment**: Staging URL for analysis
- **scope**: File scope limitations

### Field Defaults
- **git_branch**: Auto-create `feature-{NNN}`
- **spec_folder**: Auto-create `specs/{NNN}`
- **context**: Infer from request
- **scope**: Default to `specs/**`

## Outputs

### Primary Outputs

1. **plan.md**
   - Location: `[SPEC_FOLDER]/plan.md`
   - Technical approach documentation
   - Complete planning artifact

2. **planning-summary.md**
   - Location: `[SPEC_FOLDER]/planning-summary.md`
   - Executive summary
   - Next steps guidance

### Intermediate Outputs
- Requirements dossier
- Architecture proposal
- Risk assessment
- Estimation breakdown

## Parallel Agent Specifications

### Requirements Analyst Output
```yaml
requirements_dossier:
  objectives:
    - objective: "Clear goal"
      priority: "P0|P1|P2"
      success_criteria: "Measurable outcome"

  acceptance_criteria:
    - feature: "Feature name"
      criteria:
        - "Given X, When Y, Then Z"

  dependencies:
    - type: "internal|external"
      name: "Dependency"
      status: "available|needed"

  constraints:
    - type: "technical|business|regulatory"
      description: "Constraint"
      impact: "high|medium|low"

  success_metrics:
    - metric: "KPI"
      target: "Value"
      measurement: "How to measure"
```

### Solution Architect Output
```yaml
architecture_proposal:
  components:
    - name: "ComponentName"
      responsibility: "What it does"
      interfaces:
        - type: "API|Event|Data"
        - contract: "Specification"

  data_flow:
    - source: "Origin"
      destination: "Target"
      data_type: "Type"
      protocol: "Method"

  patterns:
    - pattern: "Design pattern"
      rationale: "Why chosen"

  alternatives:
    - option: "Alternative approach"
      pros: ["Benefits"]
      cons: ["Drawbacks"]
      decision: "Why not chosen"
```

### Risk Analyst Output
```yaml
risk_assessment:
  risks:
    - category: "technical|business|security"
      description: "Risk description"
      severity: "critical|high|medium|low"
      likelihood: "percentage"
      mitigation: "Strategy"
      owner: "Responsible party"

  edge_cases:
    - scenario: "Edge case"
      handling: "Approach"
      validation: "How to test"

  non_functionals:
    security:
      - requirement: "Security need"
        implementation: "How to address"
    performance:
      - metric: "Performance KPI"
        target: "Goal"
    accessibility:
      - standard: "WCAG level"
        compliance: "How to meet"
```

### Estimation Analyst Output
```yaml
estimation_breakdown:
  phases:
    - phase: "Phase name"
      deliverables: ["List of outputs"]
      effort_range: "min-max hours"
      dependencies: ["Prerequisites"]

  milestones:
    - milestone: "Achievement"
      target_date: "When"
      success_criteria: "Definition of done"

  sequencing:
    - step: 1
      task: "What to do"
      dependency: "What must complete first"

  effort_summary:
    total_range: "min-max person-days"
    confidence_level: "percentage"
    assumptions:
      - "Assumption about scope"
      - "Resource availability"
```

## Chrome DevTools Integration

When staging URL is provided:

### Analysis Actions
- Inspect network requests
- Analyze DOM structure
- Review console errors
- Capture performance metrics

### Planning Insights
- Current implementation patterns
- API endpoint discovery
- Performance baselines
- Integration points

## Adaptive Rules

**Note**: For complete adaptive rule specifications, planning complexity assessment, requirement clarity scoring, and stakeholder strategies, see [references/adaptive-rules.md](references/adaptive-rules.md).

### High Complexity Handling
- Add security/privacy reviewer
- Exhaustive review depth
- Reduce concurrency to 2
- Extended analysis time

### High Uncertainty Handling
- Insert discovery phase
- Use effort ranges
- Document unknowns
- Additional clarification

### Fallback Strategy
- Sequential execution if parallel fails
- Maintain review/synthesis
- Proceed with partial results
- Document degradation

## Quality Standards

### Planning Quality
- Complete requirement coverage
- Clear architecture definition
- Comprehensive risk analysis
- Realistic estimations

### Document Quality
- Logical organization
- Clear writing
- Measurable metrics
- Actionable recommendations

### Review Quality
- Conflict resolution
- Gap identification
- Consistency validation
- Completeness check

## Performance Characteristics

**Note**: Performance varies based on specification complexity and detail level.

- **Overall execution**: Variable based on planning depth required
- **Parallel analysis**: 4 specialist agents work concurrently
- **Review phase**: Lead reviewer reconciles outputs
- **Synthesis phase**: Document generation and integration
- **QA phase**: Main agent final validation

## Error Handling

### Retry Policy
- **Targeted retries**: Failed agents only
- **Max attempts**: 2 per agent
- **Fallback**: Sequential execution

### Recovery Actions
- Rerun failed tasks
- Proceed with partial results
- Annotate gaps in review
- Document issues

## Limitations

- **Scope**: Planning phase only (not implementation)
- **Approvals**: Manual gates required
- **Termination**: Ends after step 7
- **Dependencies**: Requires spec.md
- **Language**: English only

## Success Metrics

**Note**: Target benchmarks for planning quality and thoroughness.

- **Coverage**: All planning aspects addressed
- **Alignment**: >95% requirement mapping
- **Completeness**: No critical gaps
- **Quality**: >85% first-pass approval
- **Efficiency**: Optimized parallel execution

## Version

**Current Version**: 1.0.0
**Based On**: sk_p__plan_spec.yaml
**Created**: 2025-10-18
**Architecture**: Parallel planning with approval gates

---

## References

- Source: `/b_prompts/github_spec_kit/parallel_agents/sk_p__plan_spec.yaml`
- Prerequisites: Feature request or existing spec
- Next Steps: Use speckit-implementation for execution
- Output: plan.md, planning-summary.md