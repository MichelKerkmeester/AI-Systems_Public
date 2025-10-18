---
name: speckit_spec_plan
description: Execute spec-driven planning workflow with sequential execution. Run SpecKit from specification through planning with validation and manual approval gates.
---

# SpecKit Plan & Spec

Execute comprehensive planning and specification workflow with sequential execution and manual approval gates.

## When to Use This Skill

**Use this skill when**:
- Creating technical plans from specifications
- Need comprehensive risk and architecture assessment
- Want estimation and milestone planning
- Following manual approval workflow
- Stopping workflow after planning (before implementation)

**Do NOT use this skill for**:
- Full end-to-end workflow (use speckit_complete)
- Implementation execution (use speckit_implementation)
- Research tasks (use speckit_feature_research)
- Workflows requiring parallel analysis (use parallel_speckit_spec_plan)

## Quick Command Reference

| Step | Command | Purpose |
|------|---------|----------|
| 1 | Manual | Request Analysis |
| 2 | Manual | Pre-work Review |
| 3 | `/specify` | Create spec.md |
| 4 | `/clarify` | Resolve ambiguities |
| 5 | `/speckit.checklist` | Generate quality checklist |
| 6 | `/plan` | Technical planning and approach |

**Important**: This workflow requires **2 approval gates** (steps 1→2 and 4→5)

**Termination**: This workflow ends after step 6 (planning phase only).

## Architecture Overview

This skill implements the sk__spec_plan.yaml workflow with sequential execution by the main agent.

### Planning Workflow Steps

1. **Request Analysis** - Analyze inputs and confirm understanding
2. **Pre-work Review** - Review AGENTS.md and constitution
3. **Specification** - Create spec.md with acceptance criteria
4. **Clarification** - Resolve ambiguities and clarify requirements
5. **Quality Checklist** - Generate quality validation checklist
6. **Planning** - Create technical approach and plan.md

**Termination**: Workflow ends after step 6 (planning phase only).

## Workflow Steps (Detailed Execution)

This section provides step-by-step execution guidance as defined in sk__spec_plan.yaml.

### Step 1: Request Analysis

**Action**: Analyze user inputs, choose branch strategy, and confirm understanding

**Input Source**: USER_INPUTS_SECTION

**Branch Strategy Prompt** (REQUIRED):

Before proceeding, you must choose how to work with Git for this spec:

**Option A: Create new feature branch**
- We will auto-create `feature-{NNN}` aligned with the spec folder
- Allows isolated development and testing
- Can be integrated to main later via complete workflow

**Option B: Work on main branch**
- Skip branch creation and commit directly to main
- Faster for small changes or hotfixes
- No separate integration needed

This decision is required before proceeding and will be inherited by implementation workflow.

**Inputs**:
- `branch_strategy`: **REQUIRED** - Choose `feature_branch` or `main_branch`
- `git_branch`: Derived from branch_strategy (feature-{NNN} or main)
- `spec_folder`: Auto-create `specs/{NNN}` if empty
- `context`: Infer from request if empty
- `issues`: Discover during workflow if empty
- `request`: REQUIRED
- `environment`: Skip DevTools steps if empty
- `scope`: Default to `specs/**` if empty

**Outputs**:
- Branch strategy chosen
- Git branch resolved
- Requirement summary
- Approach overview
- Complexity assessment

**Validation**: `understanding_confirmed_and_branch_strategy_set`

**Approval Gate**: "Requirements analyzed. Branch strategy: {branch_strategy} on {git_branch}. Proceed to pre-work review?"

---

### Step 2: Pre-work Review

**Action**: Review required documents

**Required Documents**:
- AGENTS.md
- .specify/memory/constitution.md
- knowledge/*.md

**Verification**: MUST REVIEW

**Validation**: `principles_established`

**Approval Gate**: None (proceeds automatically after Step 1 approval)

---

### Step 3: Specification

**Command**: `/specify [feature-description]`

**Action**: Create spec.md with acceptance criteria

**Outputs**:
- Feature branch: created
- spec.md: acceptance_criteria
- Location: `specs/[NNN-feature]/spec.md`

**Validation**: `spec_complete_and_testable`

**Chrome DevTools** (when analyzing existing features):
- Navigate → Snapshot → Analyze → Document

**Approval Gate**: None (proceeds automatically)

---

### Step 4: Clarification

**Command**: `/clarify`

**Action**: Resolve ambiguities and clarify requirements

**Outputs**:
- Resolved ambiguities
- Clarified requirements
- Updated spec

**Validation**: `requirements_clear`

**Chrome DevTools** (when staging URL provided):
- Navigate → Inspect → Analyze → Clarify
- Capture: current_behavior_screenshots

**Approval Gate**: "Requirements clarified. Proceed to quality checklist?"

---

### Step 5: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist: generated

**Validation**: `checklist_generated`

**Approval Gate**: None (proceeds automatically after Step 4 approval)

---

### Step 6: Planning

**Command**: `/plan [context]`

**Action**: Create technical plan and approach

**Outputs**:
- plan.md: technical_approach
- dependencies: identified
- upstream_docs: reviewed

**Validation**: `approach_defined`

**Chrome DevTools** (when analyzing current implementation):
- inspect_network_requests
- analyze_dom_structure
- review_console_errors
- capture_performance_metrics

**Deep Analysis**:
- Focus: comprehensive_planning
- Approach: deep_analysis
- Outputs:
  - detailed_technical_approach
  - implementation_strategy
  - risk_assessment
  - dependency_mapping

**Final Output**:

**Summary Document**:
- Location: `specs/[NNN-feature]/planning-summary.md`
- Required Sections:
  - feature_overview
  - technical_approach
  - dependencies_identified
  - risks_and_mitigation
  - recommended_next_steps

**Completion Message**:
```
Planning phase complete. The workflow has been executed through step 6.
Technical plan and approach have been documented.
To proceed with implementation, use the full speckit_complete workflow
or use speckit_implementation for autonomous implementation.
```

---

## Workflow Termination

**After Step**: 6

**Message**: "Planning phase completed successfully. Workflow terminated after step 6 as requested."

**Next Steps**:
- Review planning documentation
- Approve technical approach
- Use speckit_complete for full implementation with gates
- Or use speckit_implementation for autonomous implementation

## Approval Gates

This workflow has 2 mandatory approval gates:

| Step | Approval Prompt | Confirmation |
|------|-----------------|--------------|
| 1→2 | "Requirements analyzed. Branch strategy: {branch_strategy} on {git_branch}. Proceed to pre-work review?" | Required |
| 4→5 | "Requirements clarified. Proceed to quality checklist?" | Required |

**Note**: Steps 2, 3, 5, and 6 proceed automatically after their preceding approval gate.

## Field Handling

This workflow automatically handles empty input fields per sk__spec_plan.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: User must choose at Step 1; cannot proceed without selection
- **Controls**: Branch creation behavior during planning

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
- **Empty Handling**: Browser testing and DevTools steps are skipped

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

## Execution Model

This workflow executes sequentially with 2 approval gates:

```
Step 1: Request Analysis
        ↓ [Approval Required]
Step 2: Pre-work Review (automatic)
        ↓
Step 3: Specification (/specify) (automatic)
        ↓
Step 4: Clarification (/clarify) (automatic)
        ↓ [Approval Required]
Step 5: Quality Checklist (/speckit.checklist) (automatic)
        ↓
Step 6: Planning (/plan) (automatic)
        ↓
[Workflow Terminated]
```

## Integration Points

### With Chrome DevTools
- Step 3: Analyze current implementation
- Step 4: Capture current behavior screenshots
- Step 6: Inspect network, DOM, errors, performance

### With SpecKit Workflows
- Output planning artifacts used by implementation workflows
- Branch strategy inherited by implementation phase
- Planning documents inform task breakdown

### Continuation Workflows
- Use **speckit_implementation** for autonomous implementation continuation
- Use **speckit_complete** for full workflow with approval gates

## Rules

**ALWAYS**:
- follow_workflow_sequence
- document_all_changes
- validate_before_completion
- use_devtools_for_staging_analysis
- await_user_approval_at_gates
- evidence_before_decisions

**NEVER**:
- skip_workflow_steps
- ignore_blockers
- submit_without_validation
- skip_browser_testing
- proceed_without_approval
- proceed_beyond_planning

## Version

**Current Version**: 1.0.0
**Based On**: sk__spec_plan.yaml
**Created**: 2025-10-18
**Architecture**: Sequential execution with manual approval gates (planning phase only)
