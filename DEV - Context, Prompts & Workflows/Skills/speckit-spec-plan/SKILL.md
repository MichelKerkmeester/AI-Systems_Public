---
name: speckit-spec-plan
description: Execute spec-driven planning workflow with parallel specialist analyses. Orchestrates 6 specialized planning sub-agents through parallel execution, review, and synthesis to produce plan.md and planning-summary.md with manual approval gates
---

# SpecKit Plan & Spec
Plan and Specify Features with Parallel Analysis Workflow

> Change Notes (2025-10-21)
- Removed 4.x sub-step numbering; standardized headers and emojis
- Added YAML → Steps Crosswalk; clarified approval gates
- Cleaned sub-agent references (removed placeholder appendices, de-numbered headings)

## 1. 🎯 When to Use This Skill

**Use this skill when**:
- Creating technical plans from specifications
- Need parallel analysis from multiple specialists
- Require comprehensive risk and architecture assessment
- Want estimation and milestone planning
- Following manual approval workflow

**Do NOT use this skill for**:

Use other skills or direct edits for:
- Implementing or refactoring code, shipping patches, or writing production-ready solutions
- Simple copy edits, formatting-only changes, or trivial content tweaks without planning value
- Direct bug fixes, debugging, or hotfixes that don't require a planning deliverable
- Non-planning workflows (e.g., content writing, generic brainstorming) unrelated to a Speckit spec/plan
- Executing or orchestrating agents and pipelines (this skill outputs planning artifacts, not execution)
- Generating tests, migration scripts, or infra changes (belongs to implementation/build skills)
- Replacing or diverging from AGENTS.md standards (this skill must align to AGENTS.md)

.
  
## 2. 🚀 Quick Command Reference
| Step | Command | Purpose |
|------|---------|----------|
| 1 | Manual | Request Analysis |
| 2 | Manual | Pre-work Review |
| 3 | `/speckit.specify` | Create spec.md |
| 4 | `/speckit.clarify` | Resolve ambiguities |
| 5 | `/speckit.checklist` | Generate quality checklist |
| 6 | *Parallel Block* | 4 analysts work in parallel |
| 7 | `/speckit.plan` | Finalize technical approach |

**⚠️ Important**: This workflow requires **3 approval gates** (steps 1→2, 4→5, 6→7)

.

## 3. 🏗️ Architecture Overview

This skill implements the sk_p__spec_plan.yaml workflow with 6 specialized planning sub-agents executing in parallel analysis phase.

### Planning Steps

1. **Request Analysis** - Analyze inputs and confirm understanding
2. **Pre-work Review** - Review AGENTS.md and constitution
3. **Specification** - Create spec.md with acceptance criteria
4. **Clarification** - Resolve ambiguities and clarify requirements
5. **Quality Checklist** - Generate quality validation checklist
6. **Parallel Planning Block** - 4 analysts work in parallel
7. **Planning** - Finalize technical approach and plan.md

**Termination**: This workflow ends after step 7 (planning phase only)

.

## YAML → Steps Crosswalk

- Source: b_prompts/github_spec_kit/parallel_agents/sk_p__spec_plan.yaml
- Mapping:
  - Step 1 → Request Analysis
  - Step 2 → Pre-work Review
  - Step 3 → Specification (/speckit.specify)
  - Step 4 → Clarification (/speckit.clarify)
  - Step 5 → Quality Checklist (/speckit.checklist)
  - Step 6 → Parallel Planning Block
  - Step 7 → Planning (/speckit.plan)

## 4. 📋 Steps

This section provides step-by-step execution guidance as defined in sk_p__spec_plan.yaml.

### Step 1: Gather User Inputs & Request Analysis

**Action**: Collect all required information from the user before proceeding

**IMPORTANT**: Before starting the workflow, ask the user for the following inputs in a conversational way:

#### Required Inputs:

1. **Branch Strategy** (REQUIRED):
   - Ask: "How would you like to work with Git for this planning workflow?"
   - Options:
     - **feature_branch**: Create new feature branch (auto-create `feature-{NNN}` aligned with spec folder). Allows isolated development and testing. Can be integrated to main later via complete workflow.
     - **main_branch**: Work on main branch (skip branch creation and commit directly to main). Faster for small changes or hotfixes. No separate integration needed.
   - This decision controls branch creation and will be inherited by implementation workflow.

2. **Request/Feature Description** (REQUIRED):
   - Ask: "What feature would you like to plan? Please describe the feature you want to create a specification and plan for."
   - This is the main feature description that drives the planning workflow.

#### Optional Inputs (with smart defaults):

3. **Spec Folder**:
   - Ask: "Which spec folder should I use? (Leave empty to auto-create `specs/{NNN}` from highest +001)"
   - Default: Auto-create `specs/{NNN}` based on existing specs

4. **Context**:
   - Ask: "Any additional context about this feature? (Leave empty to infer from your request)"
   - Default: Infer from request and environment

5. **Known Issues**:
   - Ask: "Are there any known issues or bugs to address? (Leave empty to investigate during workflow)"
   - Default: Discover during workflow

6. **Environment/Staging Link**:
   - Ask: "Do you have a staging environment URL to analyze? (Leave empty to skip browser testing steps)"
   - Default: Skip DevTools/browser testing if not provided

7. **Scope/Files**:
   - Ask: "Which files or directories should I focus on? (Leave empty to default to `specs/**`)"
   - Default: `specs/**`

**After Collecting Inputs**:
- Confirm all inputs with the user
- Resolve `git_branch` from branch_strategy (either `feature-{NNN}` or `main`)
- Parse and analyze the request
- Create requirement summary
- Assess complexity

**Outputs**:
- Branch strategy chosen
- Git branch resolved
- Spec folder determined
- All inputs confirmed
- Requirement summary
- Approach overview
- Complexity assessment

**Validation**: `all_inputs_collected_and_confirmed`

**Approval Gate**: "All inputs collected. Branch strategy: {branch_strategy} on {git_branch}. Spec folder: {spec_folder}. Proceed to pre-work review?"

### Step 2: Pre-work Review

**Action**: Review required documents

**Required Documents**:
- AGENTS.md
- .specify/memory/constitution.md
- knowledge/*.md

**Verification**: MUST REVIEW

**Validation**: `principles_established`

**Note**: No approval gate for this step

### Step 3: Specification

**Command**: `/speckit.specify [feature-description]`

**Action**: Create spec.md with acceptance criteria

**Outputs**:
- Feature branch created
- spec.md with acceptance criteria
- Location: `specs/[NNN-feature]/spec.md`

**Validation**: `spec_complete_and_testable`

**Note**: No approval gate for this step

### Step 4: Clarification

**Command**: `/speckit.clarify`

**Action**: Resolve ambiguities and clarify requirements

**Outputs**:
- Resolved ambiguities
- Clarified requirements
- Updated spec

**Validation**: `requirements_clear`

**Approval Gate**: "Requirements clarified. Proceed to quality checklist?"

### Step 5: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist generated

**Validation**: `checklist_generated`

**Note**: No approval gate for this step

### Step 6: Parallel Planning Block

**Description**: Parallel specialist analyses with bounded concurrency

This step contains sub-phases that execute sequentially:

#### Phase A: Analyze Inputs
- Summarize goals, constraints, unknowns
- Shard plan across: requirements, architecture, risk, estimation

#### Phase B: Parallel Work

**Execution**: Parallel

**Concurrency**: 3 (maximum parallel agents)

**Shared Context**:
- `[SPEC_FOLDER]/spec.md`
- quality_checklist
- request_summary
- context

**Parallel Agent Tasks**:

| Agent | Instructions | Output Sections |
|-------|--------------|------------------|
| **Requirements Analyst** | Produce requirements dossier with explicit success metrics and dependencies | objectives, acceptance_criteria_map, dependencies, constraints, success_metrics |
| **Solution Architect** | Propose clear architecture with components, interfaces, data flow, and alternatives | components, interfaces, data_flow, patterns, alternatives, tradeoffs |
| **Risk/Compliance Analyst** | Identify risks, edge cases, and non-functional requirements with severities and mitigations | risks, severities, mitigations, edge_cases, security_privacy, performance_accessibility |
| **Estimation/Scope Analyst** | Propose phases, milestones, sequencing, and effort ranges; include assumptions | phases, milestones, dependencies, sequencing, effort_ranges, assumptions |

#### Phase C: Review

**By**: Lead Reviewer

**Focus**:
- Resolve conflicts
- Validate completeness  
- Ensure consistency
- Identify open questions

**Outputs**:
- Synthesis guidance
- Review notes

#### Phase D: Synthesis

**By**: Lead Synthesizer

**Action**: Create plan.md and planning-summary.md from parallel outputs + review guidance

**Output Files**:
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

**Validation Checklist**:
- All parallel tasks present
- Risks have mitigations
- Dependencies acyclic
- Success metrics measurable
- Phases have owners and effort

#### Phase E: Main Agent Finalization

**By**: MAIN_AGENT

**Action**: QA review and finalization of planning artifacts (deferred to step 7)

**Checks**:
- Confirm alignment with request and context
- Validate completeness and consistency
- Ensure output format and sections present
- Resolve remaining open questions or note them

**Outputs**:
- Main agent review notes
- Final signoff: true

**Note**: This phase executes BEFORE the approval gate

**Approval Gate**: "Planning artifacts synthesized. Approve to proceed?"

### Step 7: Planning

**Command**: `/speckit.plan [context]`

**Action**: Finalize technical approach and plan.md

**Outputs**:
- plan.md: technical_approach
- Dependencies identified
- Upstream docs reviewed

**Validation**: `approach_defined`

**Chrome DevTools** (when analyzing current implementation):
- Inspect network requests
- Analyze DOM structure
- Review console errors
- Capture performance metrics

**Deep Analysis**:
- Focus: comprehensive_planning
- Approach: deep_analysis
- Outputs: detailed_technical_approach, implementation_strategy, risk_assessment, dependency_mapping

**Final Output**:
- Location: `specs/[NNN-feature]/planning-summary.md`
- Required Sections: feature_overview, technical_approach, dependencies_identified, risks_and_mitigation, recommended_next_steps
- Completion Message: "Planning phase complete. The workflow has been executed through step 7. Technical plan and approach have been documented. To proceed with implementation, use the full workflow_automated.yaml."

**Termination**: Workflow ends after this step

**Branch Integration Note**:

Branch strategy has been set and will be inherited by subsequent workflows.

- **If `feature_branch` was selected**:
  - Feature branch created for planning artifacts
  - Implementation workflow will use this branch
  - Complete workflow will offer integration to main at the end

- **If `main_branch` was selected**:
  - Planning artifacts committed directly to main
  - Implementation workflow will continue on main
  - No integration step needed

**Next Steps**:
- Review planning documentation
- Approve technical approach
- Branch strategy: {branch_strategy} on {git_branch}
- Use workflow_automated.yaml for full implementation (will inherit branch strategy)
- Or use workflow.yaml for manual implementation with gates

.

## 5. 👥 Planning Sub-Agents

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

.

## 6. 🔄 Execution Model

### Parallel Planning Pattern

**Note**: All parallel execution, review, synthesis, and main agent finalization occur within Step 6 as sub-phases, NOT as separate steps.

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
│      Main Agent QA Phase         │ ← Final validation BEFORE approval
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Approval Gate             │ ← User approval required
└─────────────────────────────────┘
```

### Parallel Execution Configuration

**Concurrency Settings**:
- **Default**: 3 parallel agents maximum
- **High Complexity**: 2 parallel agents (reduced concurrency)
- **Fallback**: 1 (sequential execution if parallel not supported)

**Shared Context** (passed to all parallel agents):
- `[SPEC_FOLDER]/spec.md` - Feature specification
- `quality_checklist` - Generated quality validation checklist
- `request_summary` - Parsed user request
- `context` - Additional context from user inputs

**Important**: 
- Review and synthesis phases execute sequentially AFTER parallel work completes
- Main agent finalization occurs BEFORE any approval gate
- All phases in Step 6 are sub-phases within that single workflow step

.

## 7. 📄 Planning Document Structure

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

.

## 8. ✅ Approval Gates

This workflow includes manual approval gates at key points:

| Step | Approval Prompt | Confirmation | Warning |
|------|-----------------|--------------|----------|
| 1→2 | "Requirements analyzed. Proceed to pre-work review?" | Required | None |
| 4→5 | "Requirements clarified. Proceed to quality checklist?" | Required | None |
| 6→7 | "Planning artifacts synthesized. Approve to proceed?" | Required | None |

**Note**: All approval gates require explicit user confirmation before proceeding to the next step

.

## 9. ⚙️ Field Handling

This workflow automatically handles empty input fields per sk_p__spec_plan.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: User must choose at Step 1; cannot proceed without selection
- **Controls**: Branch creation during planning; inherited by implementation workflow

### spec_id
- **Derived From**: spec_folder path using pattern `specs/{NNN}` or `specs/{NNN-name}`
- **Fallback**: Extract numeric portion or use timestamp if extraction fails
- **Usage**: Used to generate feature_branch_name

### feature_branch_name
- **Pattern**: `feature-{spec_id}`
- **Condition**: Only used when `branch_strategy == feature_branch`

### git_branch
- **Derived**: Based on branch_strategy
- **If feature_branch**: Use `feature_branch_name` (feature-{NNN})
- **If main_branch**: Use `main`
- **Empty Handling**: Cannot be empty; derived automatically from branch_strategy

### spec_folder  
- **Auto-create**: Yes
- **Default Pattern**: `specs/{NNN}` where {NNN} is highest existing +001
- **Scope**: Project specs directory
- **Empty Handling**: Automatically creates new folder following naming convention

### context
- **Auto-create**: No
- **Default**: Inferred from request and staging link if provided
- **Empty Handling**: Inference from available inputs

### issues
- **Auto-create**: No  
- **Default**: None
- **Empty Handling**: Investigated and discovered during workflow execution

### environment (staging link)
- **Auto-create**: No
- **Default**: None
- **Empty Handling**: DevTools/browser testing steps are skipped

### scope (files)
- **Auto-create**: No
- **Default**: `specs/**`
- **Empty Handling**: Uses default scope policy limiting operations to specs directory

### Branch Creation
- **Condition**: Only execute when `branch_strategy == feature_branch`
- **Steps**:
  1. Check if feature branch already exists
  2. Create feature-{spec_id} if not exists
   3. Checkout feature branch
- **Skip When**: `branch_strategy == main_branch`

.

## 10. 📥 Inputs

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

.

## 11. 📤 Outputs

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

.

## 12. 🧩 Parallel Agent Specifications

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

.

## 13. 🌐 Chrome DevTools Integration

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

.

## 14. 🎛️ Adaptive Rules

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

.

## 15. ✨ Quality Standards

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

.

## 16. ⚡ Performance Characteristics

**Note**: Performance varies based on specification complexity and detail level.

- **Overall execution**: Variable based on planning depth required
- **Parallel analysis**: 4 specialist agents work concurrently
- **Review phase**: Lead reviewer reconciles outputs
- **Synthesis phase**: Document generation and integration
- **QA phase**: Main agent final validation

.

## 17. 🚨 Error Handling

### Retry Policy
- **Targeted retries**: Failed agents only
- **Max attempts**: 2 per agent
- **Fallback**: Sequential execution

### Recovery Actions
- Rerun failed tasks
- Proceed with partial results
- Annotate gaps in review
- Document issues

.

## 18. ⚠️ Limitations

- **Scope**: Planning phase only (not implementation)
- **Approvals**: Manual gates required
- **Termination**: Ends after step 7
- **Dependencies**: Requires spec.md
- **Language**: English only

.

## 19. 📈 Success Metrics

**Note**: Target benchmarks for planning quality and thoroughness.

- **Coverage**: All planning aspects addressed
- **Alignment**: >95% requirement mapping
- **Completeness**: No critical gaps
- **Quality**: >85% first-pass approval
- **Efficiency**: Optimized parallel execution

.

## 20. References

- Source: `/b_prompts/github_spec_kit/parallel_agents/sk_p__spec_plan.yaml`
- Prerequisites: Feature request or existing spec
- Next Steps: Use speckit-implementer for execution
- Output: plan.md, planning-summary.md
