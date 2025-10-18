---
name: speckit_implementation
description: Execute autonomous spec-driven implementation with sequential execution. Continue from planning phase with comprehensive implementation preparation, autonomous development, and progressive checkpoints.
---

# SpecKit Implementation

Execute autonomous implementation workflow with sequential preparation and progressive development checkpoints.

## When to Use This Skill

**Use this skill when**:
- Ready to implement a fully specified feature
- Have spec.md and plan.md completed
- Need comprehensive implementation preparation
- Want autonomous implementation without approval gates
- Executing actual code changes

**Do NOT use this skill for**:
- Initial specification creation (use speckit_spec_plan)
- Research and investigation (use speckit_feature_research)
- Simple planning without implementation
- Manual implementation with approval gates (use speckit_complete)
- Workflows requiring parallel preparation (use parallel_speckit_implementation)

## Quick Command Reference

**CRITICAL**: This workflow starts at **Step 7** (continuation from planning workflow steps 1-6)

| Step | Command | Purpose |
|------|---------|----------|
| **7** | Manual | Review Plan and Spec |
| **8** | `/tasks` | Generate actionable tasks |
| **9** | `/analyze` | Check consistency |
| **10** | `/speckit.checklist` | Quality gates |
| **11** | `/implement` | Verify prerequisites |
| **12** | Manual | Autonomous development |
| **13** | Manual | Document changes and completion |

**Autonomous**: This workflow executes all steps without approval gates.

## Architecture Overview

This skill implements the sk__implementation.yaml workflow with sequential execution by the main agent.

### Implementation Workflow Steps

**CRITICAL**: Step numbering continues from planning workflow (steps 1-6).

**Note**: This workflow covers steps 7-13 of the complete SpecKit process. Steps 1-6 are assumed completed via planning workflow.

7. **Review Plan and Spec** - Understand existing artifacts
8. **Task Breakdown** - Generate actionable tasks
9. **Analysis** - Check consistency and coverage
10. **Quality Checklist** - Generate quality gates
11. **Implementation Check** - Verify prerequisites
12. **Development** - Execute autonomous implementation
13. **Completion** - Document changes and summary

**Note**: This is an autonomous workflow with NO approval gates.

## Workflow Steps (Detailed Execution)

**Prerequisites**: Requires `spec.md`, `plan.md`, and `planning-summary.md` from steps 1-6.

This section provides step-by-step execution guidance as defined in sk__implementation.yaml.

### Step 7: Review Plan and Spec

**Note**: This workflow is a continuation of the planning phase (steps 1-6). Branch strategy should have been set during planning. If starting independently, branch_strategy must be provided.

**Action**:
1. Confirm branch_strategy (should be inherited from planning phase)
2. Verify git_branch is correctly set based on strategy
3. Review spec and planning artifacts

**Input Source**: USER_INPUTS_SECTION

**Branch Strategy** (inherited from planning):
- `branch_strategy`: Should be set from planning workflow
- `git_branch`: Derived from branch_strategy
  - If `feature_branch`: Uses feature-{NNN}
  - If `main_branch`: Uses main

**Request Handling**:
- Default: "Conduct a comprehensive review of the spec folder and carry out its implementation fully autonomously."
- Override: Use provided request if specified, else use default above

**Inputs**:
- `branch_strategy`: Should be inherited from planning phase
- `git_branch`: Derived from branch_strategy
- `spec_folder`: Auto-create `specs/{NNN}` if empty
- `context`: Infer from request if empty
- `issues`: Discover during workflow if empty
- `request`: Use default or override if provided
- `environment`: Skip browser testing if empty
- `scope`: Default to `specs/**` if empty

**Required Documents**:
- `[SPEC_FOLDER]/spec.md`
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

**Review Focus**:
- understand_feature_requirements
- analyze_technical_approach
- identify_dependencies
- note_implementation_constraints
- clarify_acceptance_criteria

**Deep Analysis**:
- Focus: comprehensive_plan_review
- Approach: deep_understanding
- Outputs:
  - requirements_summary
  - technical_approach_understanding
  - identified_dependencies
  - potential_challenges
  - implementation_readiness_assessment
  - specification_interpretation
  - technical_approach_validation
  - dependency_impact_analysis
  - edge_case_identification
  - implementation_strategy_refinement

**Outputs**:
- Branch strategy confirmed
- Git branch validated
- Planning artifacts understood

**Validation**: `planning_artifacts_understood_and_branch_confirmed`

**Approval Gate**: None (autonomous execution)

---

### Step 8: Task Breakdown

**Command**: `/tasks`

**Action**: Generate actionable task checklist

**Outputs**:
- tasks/checklist.md
- task_duration: 15_to_60_minutes
- tracking_structure: established

**Deep Analysis**:
- Focus: comprehensive_task_analysis
- Approach: deep_breakdown
- Outputs:
  - granular_task_list
  - dependency_chain
  - time_estimates
  - priority_ordering

**Validation**: `tasks_actionable`

**Approval Gate**: None (autonomous execution)

---

### Step 9: Analysis

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
- Focus:
  - ui_consistency
  - functionality_gaps
  - performance_baseline

**Deep Analysis**:
- Focus: comprehensive_consistency_check
- Approach: deep_analysis
- Outputs:
  - spec_vs_implementation_gaps
  - potential_edge_cases
  - integration_points
  - risk_assessment

**Approval Gate**: None (autonomous execution)

---

### Step 10: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist: generated

**Validation**: `checklist_generated`

**Approval Gate**: None (autonomous execution)

---

### Step 11: Implementation Check

**Command**: `/implement [task-id]`

**Action**: Verify prerequisites before code changes

**Checks**:
- Prerequisites: verified
- Blockers: none
- Environment: ready

**Chrome DevTools** (when validating environment):
- Verify:
  - api_endpoints_accessible
  - authentication_working
  - dependencies_loaded

**Deep Analysis**:
- Focus: pre_implementation_verification
- Approach: environment_validation
- Outputs:
  - environment_status
  - dependency_verification
  - blocker_identification
  - readiness_confirmation

**Approval Gate**: None (autonomous execution)

---

### Step 12: Development

**Approach**: autonomous_implementation_with_checkpoints

**Requirements**:
- Follow: knowledge/code_standards.md
- Update: task_checklist_progressively
- Test: before_commit
- no_premature_optimization

**Checkpoints**:

**Major Changes**:
- Action: log_progress

**Issues Found**:
- Action: document_resolution

**Architecture Change**:
- Action: note_deviation

**Chrome DevTools** (when debugging implementation):
- test_in_browser
- verify_network_calls
- check_console_output
- validate_dom_changes
- measure_performance_impact

**Deep Analysis**:
- Focus: iterative_problem_solving
- Approach: continuous_validation
- Outputs:
  - implementation_decisions
  - debugging_insights
  - optimization_opportunities
  - test_coverage_gaps

**Approval Gate**: None (autonomous execution)

---

### Step 13: Completion

**Action**: Document changes and create summary

**Summary Document**:
- Location: `[SPEC_FOLDER]/implementation-summary.md`
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

**Deep Analysis**:
- Focus: comprehensive_completion_review
- Approach: retrospective_analysis
- Outputs:
  - implementation_quality_assessment
  - lessons_learned
  - technical_debt_noted
  - future_improvements

**Approval Gate**: None (autonomous execution)

---

## Workflow Termination

**After Step**: 13

**Message**: "Implementation phase completed successfully. Workflow terminated after step 13 as requested."

**Next Steps**:
- Review implementation-summary.md
- Verify all changes in staging environment
- Prepare for code review and PR submission
- Update knowledge base if needed

## Approval Gates

This workflow is **autonomous** with NO approval gates:

| Step | Approval Prompt | Note |
|------|-----------------|------|
| 7-13 | None | Fully autonomous execution |

**Note**: All steps execute autonomously without user approval gates.

## Field Handling

This workflow automatically handles empty input fields per sk__implementation.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: Inherit from planning phase; if unavailable, prompt user
- **Note**: This field should be inherited from the planning workflow. If starting implementation independently, prompt user for choice.

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
- **Note**: Branch should already exist from planning phase if feature_branch was selected

## Execution Model

This workflow executes sequentially and autonomously:

```
Step 7: Review Plan and Spec (autonomous)
        ↓
Step 8: Task Breakdown (/tasks) (autonomous)
        ↓
Step 9: Analysis (/analyze) (autonomous)
        ↓
Step 10: Quality Checklist (/speckit.checklist) (autonomous)
        ↓
Step 11: Implementation Check (/implement) (autonomous)
        ↓
Step 12: Development (autonomous with checkpoints)
        ↓
Step 13: Completion (autonomous)
        ↓
[Workflow Terminated]
```

## Prerequisites

**Required Artifacts**:
- `[SPEC_FOLDER]/spec.md`
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

**Verification**: MUST EXIST BEFORE PROCEEDING

**Note**: This workflow assumes steps 1-6 completed via speckit_spec_plan workflow or equivalent.

**User Context**: `[CONTEXT]`

**User Request**: `[REQUEST]`

## Integration Points

### With Chrome DevTools
- Step 9: Compare staging vs spec
- Step 11: Validate environment prerequisites
- Step 12: Debug implementation, verify network, check console

### With Planning Workflows
- Inherits branch strategy from planning phase
- Reads planning artifacts from spec folder
- Continues from step 6 completion

## Rules

**ALWAYS**:
- follow_workflow_sequence
- document_all_changes
- validate_before_completion
- use_devtools_for_staging_analysis
- update_task_checklist_progressively
- self_validate_and_proceed
- do_not_prompt_for_user_approval

**NEVER**:
- skip_workflow_steps
- ignore_blockers
- submit_without_validation
- skip_browser_testing
- expand_scope_beyond_spec

## Version

**Current Version**: 1.0.0
**Based On**: sk__implementation.yaml
**Created**: 2025-10-18
**Architecture**: Sequential execution with autonomous operation (implementation phase only)
