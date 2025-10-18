---
name: speckit_complete
description: Execute the complete 12-step SpecKit workflow with sequential execution and manual approval gates. Implements spec-driven development from requirements analysis through branch integration with validation checkpoints.
---

# SpecKit Complete

Execute the complete SpecKit workflow with sequential execution and manual approval gates at each step.

## When to Use This Skill

**Use this skill when**:
- Executing full end-to-end feature development
- Need comprehensive workflow with validation gates
- Want manual control and approval at each step
- Following spec-driven development methodology
- Require complete documentation trail

**Do NOT use this skill for**:
- Quick changes without full workflow
- Research-only tasks (use speckit_feature_research)
- Planning-only tasks (use speckit_spec_plan)
- Implementation-only tasks (use speckit_implementation)
- Workflows requiring parallel execution (use parallel_speckit_complete)

## Quick Command Reference

**Complete 12-Step Workflow**:

| Step | Command | Purpose |
|------|---------|----------|
| 1 | Manual | Request Analysis |
| 2 | Manual | Pre-work Review |
| 3 | `/specify` | Create spec.md |
| 4 | `/clarify` | Resolve ambiguities |
| 5 | `/speckit.checklist` | Quality checklist |
| 6 | `/plan` | Technical planning |
| 7 | `/tasks` | Task breakdown |
| 8 | `/analyze` | Consistency check |
| 9 | `/implement` | Implementation check |
| 10 | Manual | Development - Code changes |
| 11 | Manual | Document changes |
| 12 | Manual | Branch Integration |

**Manual Control**: This workflow requires **12 approval gates** (one after each step)

## Architecture Overview

This skill implements the complete 12-step workflow with sequential execution by the main agent.

### The 12 Workflow Steps

1. **Request Analysis** - Parse and understand requirements
2. **Pre-work Review** - Review AGENTS.md, constitution, knowledge base
3. **Specification** - Create spec.md with `/speckit.specify`
4. **Clarification** - Resolve ambiguities with `/speckit.clarify`
5. **Quality Checklist** - Generate checklists with `/speckit.checklist`
6. **Planning** - Create technical plan with `/plan`
7. **Task Breakdown** - Generate tasks with `/tasks`
8. **Analysis** - Check consistency with `/analyze`
9. **Implementation Check** - Verify prerequisites with `/implement`
10. **Development** - Execute code changes
11. **Completion** - Document changes
12. **Branch Integration** - Merge to main

## Workflow Steps (Detailed Execution)

This section provides step-by-step execution guidance as defined in sk__complete.yaml.

### Step 1: Request Analysis

**Action**: Analyze user inputs, choose branch strategy, and confirm understanding

**Input Source**: USER_INPUTS_SECTION

**Branch Strategy Prompt** (REQUIRED):

Before proceeding, you must choose how to work with Git for this spec:

**Option A: Create new feature branch**
- We will auto-create `feature-{NNN}` aligned with the spec folder
- Allows isolated development and testing
- Final step will offer to merge to main

**Option B: Work on main branch**
- Skip branch creation and commit directly to main
- Faster for small changes or hotfixes
- No merge step at the end

This decision is required before proceeding and will control later integration gates.

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

**Approval Gate**: "Pre-work documentation reviewed. Proceed to specification?"

---

### Step 3: Specification

**Command**: `/specify [feature-description]`

**Action**: Create spec.md with acceptance criteria

**Outputs**:
- Feature branch: created
- spec.md: acceptance_criteria
- Location: `specs/[NNN-feature]/spec.md`

**Validation**: `spec_complete`

**Chrome DevTools** (when analyzing existing features):
- Navigate → Snapshot → Analyze → Document

**Approval Gate**: "Specification created. Review spec.md and approve to proceed to clarification?"

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

**Approval Gate**: "Quality checklist complete. Proceed to planning?"

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

**Approval Gate**: "Technical plan created. Review plan.md and approve to proceed to task breakdown?"

---

### Step 7: Task Breakdown

**Command**: `/tasks`

**Action**: Generate actionable task checklist

**Outputs**:
- tasks/checklist.md
- task_duration: 15_to_60_minutes
- tracking_structure: established

**Validation**: `tasks_actionable`

**Approval Gate**: "Tasks broken down. Review checklist.md and approve to proceed to analysis?"

---

### Step 8: Analysis

**Command**: `/analyze`

**Action**: Check consistency and verify alignment

**Outputs**:
- consistency_report
- coverage_verification
- alignment_check
- gap_analysis

**Validation**: `consistency_verified`

**Chrome DevTools** (when comparing staging vs spec):
- Navigate → Snapshot → Compare → Report
- Focus: ui_consistency, functionality_gaps, performance_baseline

**Approval Gate**: "Analysis complete. Review consistency report and approve to proceed to implementation check?"

---

### Step 9: Implementation Check

**Command**: `/implement [task-id]`

**Action**: Verify prerequisites before code changes

**Checks**:
- Prerequisites: verified
- Blockers: none
- Environment: ready

**Critical Gate**: CONFIRM_BEFORE_CODE

**Chrome DevTools** (when validating environment):
- Verify: api_endpoints_accessible, authentication_working, dependencies_loaded

**Approval Gate**: "Implementation prerequisites verified. APPROVE TO BEGIN CODE IMPLEMENTATION?"

**Warning**: "This will begin actual code changes"

---

### Step 10: Development

**Approach**: manual_implementation_with_checkpoints

**Requirements**:
- Follow: knowledge/code_standards.md
- Update: task_checklist_progressively
- Test: before_commit

**Checkpoints**:

**Major Changes**:
- Action: log_progress
- Approval: USER_APPROVAL_REQUIRED

**Issues Found**:
- Action: document_resolution
- Approval: USER_APPROVAL_REQUIRED

**Architecture Change**:
- Action: note_deviation
- Approval: USER_APPROVAL_REQUIRED

**Chrome DevTools** (when debugging implementation):
- Test in browser
- Verify network calls
- Check console output
- Validate DOM changes
- Measure performance impact

**Approval Gate**: "Development complete. Approve to proceed to completion summary?"

---

### Step 11: Completion

**Action**: Document changes and create summary

**Summary Document**:
- Location: `specs/[NNN-feature]/implementation-summary.md`
- Required Sections:
  - feature_branch_name
  - files_modified_created
  - verification_steps_taken
  - deviations_from_plan
  - knowledge_base_updates
  - recommended_next_steps
  - browser_testing_results

**Final Checklist**:
- update_task_status: completed
- validation_passed: confirmed
- summary_created: true
- staging_verified: true

**Approval Gate**: "Implementation summary complete. Approve to finalize workflow?"

---

### Step 12: Branch Integration

**Name**: Branch Integration Approval

**Condition**: **Only execute if `branch_strategy == feature_branch`**

**Skip When**: `branch_strategy == main_branch`

**Skip Message**: "Skipping branch integration (working on main branch)"

**Note**: This step is automatically skipped when working on the main branch. If you selected `main_branch` at Step 1, changes are already committed directly to main and no integration is needed.

**Approval Gate** (when feature_branch is selected):
- **Prompt**: "All checks passed. Branch: {git_branch}. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?"
- **Confirmation Needed**: true
- **Condition**: Only prompt if `branch_strategy == feature_branch`

**Integration Policy**:
- Merge strategy: rebase_then_fast_forward
- Safety checks:
  - Clean working tree
  - Validations/tests/pass checks are green
  - No unresolved blockers
- Conflict policy:
  - On rebase conflict: pause and ask for guidance
  - Fallback to PR: offer to open a PR if user prefers manual resolution
- Steps:
  - Fetch origin
  - Update main (pull --ff-only)
  - Rebase feature branch onto main
  - Fast-forward merge into main
  - Push origin main
  - After successful integration, offer to delete the feature branch locally and on origin (explicit confirmation required)
- Tagging: optional; only on user request

**Termination**: Workflow ends after this step (or after Step 11 if main_branch was selected)

## Approval Gates

Each step has a mandatory approval gate per sk__complete.yaml:

| Step | Approval Prompt | Confirmation | Warning |
|------|-----------------|--------------|---------|
| 1→2 | "Requirements analyzed. Proceed to pre-work review?" | Required | None |
| 2→3 | "Pre-work documentation reviewed. Proceed to specification?" | Required | None |
| 3→4 | "Specification created. Review spec.md and approve to proceed?" | Required | None |
| 4→5 | "Requirements clarified. Proceed to quality checklist?" | Required | None |
| 5→6 | "Quality checklist complete. Proceed to planning?" | Required | None |
| 6→7 | "Technical plan created. Approve to proceed to task breakdown?" | Required | None |
| 7→8 | "Tasks broken down. Review and approve to proceed to analysis?" | Required | None |
| 8→9 | "Analysis complete. Approve to proceed to implementation check?" | Required | None |
| 9→10 | "Prerequisites verified. APPROVE TO BEGIN CODE IMPLEMENTATION?" | Required | "This will begin actual code changes" |
| 10→11 | "Development complete. Approve to proceed to completion?" | Required | None |
| 11→12 | "Implementation summary complete. Approve to finalize?" | Required | None |
| 12 | "All checks passed. Push to main now?" | Required | None |

**Note**: All 12 approval gates require explicit user confirmation before proceeding.

## Field Handling

This workflow automatically handles empty input fields per sk__complete.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: User must choose at Step 1; cannot proceed without selection
- **Controls**: Branch creation behavior and Step 12 integration gate

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

## Execution Model

This workflow executes sequentially with manual approval at each step:

```
Step 1: Request Analysis
        ↓ [Approval Required]
Step 2: Pre-work Review
        ↓ [Approval Required]
Step 3: Specification (/specify)
        ↓ [Approval Required]
Step 4: Clarification (/clarify)
        ↓ [Approval Required]
Step 5: Quality Checklist (/speckit.checklist)
        ↓ [Approval Required]
Step 6: Planning (/plan)
        ↓ [Approval Required]
Step 7: Task Breakdown (/tasks)
        ↓ [Approval Required]
Step 8: Analysis (/analyze)
        ↓ [Approval Required]
Step 9: Implementation Check (/implement)
        ↓ [Approval Required - CRITICAL]
Step 10: Development
        ↓ [Approval Required]
Step 11: Completion
        ↓ [Approval Required]
Step 12: Branch Integration (conditional)
        ↓ [Complete]
```

## Integration Points

### With Chrome DevTools
- Step 3: Analyze current implementation
- Step 4: Capture current behavior screenshots
- Step 6: Inspect network, DOM, errors, performance
- Step 8: Compare staging vs spec
- Step 9: Validate environment
- Step 10: Debug implementation

### With Manual Steps
- Approval gates require user confirmation
- Review artifacts between stages
- Manual fixes for identified issues

## Rules

**ALWAYS**:
- follow_workflow_sequence
- document_all_changes
- validate_before_completion
- use_devtools_for_staging_analysis
- await_user_approval_at_gates

**NEVER**:
- skip_workflow_steps
- ignore_blockers
- submit_without_validation
- skip_browser_testing
- proceed_without_approval
- over_engineer_or_expand_scope

## Version

**Current Version**: 1.0.0
**Based On**: sk__complete.yaml
**Created**: 2025-10-18
**Architecture**: Sequential execution with manual approval gates
