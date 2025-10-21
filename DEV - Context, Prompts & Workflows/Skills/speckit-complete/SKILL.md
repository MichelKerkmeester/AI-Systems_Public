---
name: speckit-complete
description: Execute the complete 14-step SpecKit workflow with 18 specialized sub-agents running in 3 parallel stages. Implements the full sk_p__complete.yaml workflow with approval gates, review/synthesis phases, and adaptive rules for complexity handling
---

# SpecKit Parallel Complete
Full 14-Step Workflow Orchestration

> Change Notes (2025-10-21)
- Removed 4.x sub-step numbering across Workflow Steps
- Standardized headers and header-only emoji usage
- Added YAML → Steps Crosswalk; preserved stage semantics and approval gates

## 1. 🎯 When to Use

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

.

## 2. 🚀 Quick Command Reference

**Complete 14-Step Workflow** with 3 Parallel Stages:

| Step | Command | Stage | Purpose |
|------|---------|-------|----------|
| 1 | Manual | - | Request Analysis |
| 2 | Manual | - | Pre-work Review |
| 3 | `/specify` | - | Create spec.md |
| 4 | `/clarify` | - | Resolve ambiguities |
| 5 | `/speckit.checklist` | - | Quality checklist |
| 6 | *Parallel Block* | **A: Planning** | 4 analysts work in parallel |
| 7 | `/tasks` | - | Task breakdown |
| 8 | `/analyze` | - | Consistency check |
| 9 | *Parallel Block* | **B: Implementation** | 4 implementation agents prepare |
| 10 | `/implement` | - | Implementation check |
| 11 | Manual | - | Development - Code changes |
| 12 | *Parallel Block* | **C: Quality** | 4 quality reviewers validate |
| 13 | Manual | - | Document changes |
| 14 | Manual | - | Branch Integration |

**⚠️ Manual Control**: This workflow requires **14 approval gates** (one after each step)

.

## 3. 🏗️ Architecture Overview

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

.

## YAML → Steps Crosswalk

- Source: b_prompts/github_spec_kit/parallel_agents/sk_p__complete.yaml
- Mapping:
  - Step 1 → Request Analysis
  - Step 2 → Pre-work Review
  - Step 3 → Specification (/speckit.specify)
  - Step 4 → Clarification (/speckit.clarify)
  - Step 5 → Quality Checklist (/speckit.checklist)
  - Step 6 → Parallel Planning (Stage A)
  - Step 7 → Task Breakdown (/speckit.tasks)
  - Step 8 → Analysis (/speckit.analyze)
  - Step 9 → Parallel Implementation Prep (Stage B)
  - Step 10 → Implementation Check (/speckit.implement)
  - Step 11 → Development
  - Step 12 → Parallel Quality Review (Stage C)
  - Step 13 → Completion
  - Step 14 → Branch Integration

## 4. 📝 Workflow Steps

This section provides step-by-step execution guidance as defined in sk_p__complete.yaml.

### Step 1: Gather User Inputs

**Action**: Collect all required information from the user before proceeding

**IMPORTANT**: Before starting the workflow, ask the user for the following inputs in a conversational way:

#### Required Inputs:

1. **Branch Strategy** (REQUIRED):
   - Ask: "How would you like to work with Git for this feature?"
   - Options:
     - **feature_branch**: Create new feature branch (auto-create `feature-{NNN}` aligned with spec folder). Allows isolated development and testing. Final step will offer to merge to main.
     - **main_branch**: Work on main branch (skip branch creation and commit directly to main). Faster for small changes or hotfixes. No merge step at the end.
   - This decision controls branch creation and final integration gates.

2. **Request/Feature Description** (REQUIRED):
   - Ask: "What feature would you like to build? Please describe the request or feature you want to implement."
   - This is the main feature description that drives the entire workflow.

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
   - Ask: "Do you have a staging environment URL to test against? (Leave empty to skip browser testing steps)"
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

**Approval Gate**: "Pre-work documentation reviewed. Proceed to specification?"

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

### Step 5: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist: generated

**Validation**: `checklist_generated`

**Approval Gate**: "Quality checklist complete. Proceed to planning parallel block?"

### Step 6: Parallel Planning Block (Stage A)

**Description**: Parallel specialist analyses for planning/spec

This step contains sub-phases that execute sequentially:

#### Phase A: Parallel Work

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
| **Requirements Analyst** | Requirements dossier with success metrics and dependencies | objectives, acceptance_criteria_map, dependencies, constraints, success_metrics |
| **Solution Architect** | Architecture with components, interfaces, data flow, alternatives | components, interfaces, data_flow, patterns, alternatives, tradeoffs |
| **Risk/Compliance Analyst** | Risks, severities, mitigations, edge cases, non-functionals | risks, severities, mitigations, edge_cases, security_privacy, performance_accessibility |
| **Estimation/Scope Analyst** | Phases, milestones, sequencing, effort ranges, assumptions | phases, milestones, dependencies, sequencing, effort_ranges, assumptions |

#### Phase B: Review

**By**: Lead Reviewer A

**Outputs**: [synthesis_guidance, review_notes]

#### Phase C: Synthesis

**By**: Lead Synthesizer A

**Output Files**:
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

#### Phase D: Main Agent Finalization

**By**: MAIN_AGENT

**Action**: QA review and finalization of planning artifacts

**Checks**:
- Confirm alignment with request and context
- Validate completeness and consistency
- Ensure output format and sections present
- Resolve remaining open questions or note them

**Outputs**:
- Main agent review notes
- Final signoff: true

**Note**: This phase executes BEFORE the approval gate

**Approval Gate**: "Planning artifacts synthesized. Approve to proceed to task breakdown?"

### Step 7: Task Breakdown

**Command**: `/tasks`

**Action**: Generate actionable task checklist

**Outputs**:
- tasks/checklist.md
- Task duration: 15_to_60_minutes
- Tracking structure: established

**Validation**: `tasks_actionable`

**Approval Gate**: "Tasks broken down. Review checklist.md and approve to proceed to analysis?"

### Step 8: Analysis

**Command**: `/analyze`

**Action**: Check consistency and verify alignment

**Outputs**:
- Consistency report
- Coverage verification
- Alignment check
- Gap analysis

**Validation**: `consistency_verified`

**Chrome DevTools** (when comparing staging vs spec):
- Navigate → Snapshot → Compare → Report
- Focus: ui_consistency, functionality_gaps, performance_baseline

**Approval Gate**: "Analysis complete. Review consistency report and approve to proceed to implementation parallel prep?"

### Step 9: Parallel Implementation Prep (Stage B)

**Description**: Parallel prep for core, integrations, tests, docs

This step contains sub-phases that execute sequentially:

#### Phase A: Parallel Work

**Execution**: Parallel

**Concurrency**: 3 (maximum parallel agents)

**Shared Context**:
- `[SPEC_FOLDER]/spec.md`
- `[SPEC_FOLDER]/plan.md`
- tasks/checklist.md
- consistency_report

**Parallel Agent Tasks**:

| Agent | Instructions | Output Sections |
|-------|--------------|------------------|
| **Core Implementer** | Modules, data structures, algorithmic approach | modules, data_structures, algorithms, rationale |
| **Integrations/Adapters Engineer** | Integrations, API contracts, configuration, error handling | integrations, api_contracts, error_handling, configuration |
| **Test Engineer** | Test plan, key cases, fixtures, coverage targets | test_plan, key_cases, fixtures, coverage_targets |
| **Docs Engineer** | Usage docs, examples, migration | usage, examples, migration_upgrade |

#### Phase B: Review

**By**: Integration Reviewer B

**Outputs**: [synthesis_guidance, review_notes]

#### Phase C: Synthesis

**By**: Lead Synthesizer B

**Output Files**:
- `[SPEC_FOLDER]/implementation_plan.md`

#### Phase D: Main Agent Finalization

**By**: MAIN_AGENT

**Action**: QA review and finalization of implementation plan

**Checks**:
- Confirm alignment with request and context
- Validate completeness and consistency
- Ensure output format and sections present
- Resolve remaining open questions or note them

**Outputs**:
- Main agent review notes
- Final signoff: true

**Note**: This phase executes BEFORE the approval gate

**Approval Gate**: "Implementation plan synthesized. Approve to proceed to implementation check?"

### Step 10: Implementation Check

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

### Step 11: Development

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

**Approval Gate**: "Development complete. Proceed to quality parallel review before completion?"

### Step 12: Parallel Quality Review (Stage C)

**Description**: Parallel reviewers for final quality validation

This step contains sub-phases that execute sequentially:

#### Phase A: Parallel Work

**Execution**: Parallel

**Concurrency**: 3 (maximum parallel agents)

**Parallel Agent Tasks**:

| Agent | Instructions | Focus |
|-------|--------------|--------|
| **Completeness Reviewer** | Coverage and non-functionals validation | coverage_gaps, missing_requirements, non_functionals |
| **Feasibility Reviewer** | Technical viability, performance, scalability | technical_viability, performance, scalability, constraints |
| **Security/Privacy Reviewer** | Security/privacy assessment and mitigations | vulnerabilities, auth, encryption, input_validation |
| **Consistency/Traceability Reviewer** | Contradictions, terminology, references | contradictions, terminology, references, traceability |

#### Phase B: Review

**By**: Lead Reviewer C

**Outputs**: [synthesis_guidance, prioritized_issue_list]

#### Phase C: Synthesis

**By**: Lead Synthesizer C

**Output Files**:
- `[SPEC_FOLDER]/quality_report.md`

#### Phase D: Main Agent Finalization

**By**: MAIN_AGENT

**Action**: QA review and finalization of quality report

**Checks**:
- Confirm alignment with request and context
- Validate completeness and consistency
- Ensure output format and sections present
- Resolve remaining open questions or note them

**Outputs**:
- Main agent review notes
- Final signoff: true

**Note**: This phase executes BEFORE the approval gate

**Approval Gate**: "Quality review complete. Approve to proceed to completion summary?"

### Step 13: Completion

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
- Update task status: completed
- Validation passed: confirmed
- Summary created: true
- Staging verified: true

**Approval Gate**: "Implementation summary complete. Approve to finalize workflow?"

### Step 14: Branch Integration

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

**Termination**: Workflow ends after this step (or after Step 13 if main_branch was selected)

.

## 5. 🤝 Agent Coordination

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

.

## 6. 🔄 Execution Model

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

.

## 7. 📊 Stage Definitions

### Stage A: Planning/Spec (Step 6)

**Note**: This stage executes as part of the workflow's step 6 parallel planning block. The association with `/speckit.plan` is inferred from workflow context.

#### Sub-Agents

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

#### Review & Synthesis

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

#### Outputs
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

### Stage B: Implementation Prep (Step 9)

**Note**: This stage executes as part of the workflow's step 9 parallel implementation preparation block. Runs before actual implementation begins.

#### Sub-Agents

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

#### Review & Synthesis

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

#### Outputs
- `[SPEC_FOLDER]/implementation_plan.md`

### Stage C: Quality Review (Step 12)

**Note**: This stage executes as part of the workflow's step 12 parallel quality review block. Provides comprehensive quality validation after development.

#### Sub-Agents

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

#### Review & Synthesis

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

#### Outputs
- `[SPEC_FOLDER]/quality_report.md`

.

## 8. ✅ Approval Gates

Each step has a mandatory approval gate per sk_p__complete.yaml:

| Step | Approval Prompt | Confirmation | Warning |
|------|-----------------|--------------|---------|
| 1→2 | "Requirements analyzed. Proceed to pre-work review?" | Required | None |
| 2→3 | "Pre-work documentation reviewed. Proceed to specification?" | Required | None |
| 3→4 | "Specification created. Review spec.md and approve to proceed to clarification?" | Required | None |
| 4→5 | "Requirements clarified. Proceed to quality checklist?" | Required | None |
| 5→6 | "Quality checklist complete. Proceed to planning parallel block?" | Required | None |
| 6→7 | "Planning artifacts synthesized. Approve to proceed to task breakdown?" | Required | None |
| 7→8 | "Tasks broken down. Review checklist.md and approve to proceed to analysis?" | Required | None |
| 8→9 | "Analysis complete. Review consistency report and approve to proceed to implementation parallel prep?" | Required | None |
| 9→10 | "Implementation plan synthesized. Approve to proceed to implementation check?" | Required | None |
| 10→11 | "Prerequisites verified. APPROVE TO BEGIN CODE IMPLEMENTATION?" | Required | "This will begin actual code changes" |
| 11→12 | "Development complete. Proceed to quality parallel review before completion?" | Required | None |
| 12→13 | "Quality review complete. Approve to proceed to completion summary?" | Required | None |
| 13→14 | "Implementation summary complete. Approve to finalize workflow?" | Required | None |
| 14 | "All checks passed. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?" | Required | None |

**Note**: All 14 approval gates require explicit user confirmation before proceeding.

.

## 9. ⚙️ Adaptive Rules & Field Handling

### Adaptive Rules

**Note**: For detailed adaptive rule specifications and decision trees, see [references/adaptive-rules.md](references/adaptive-rules.md).

This workflow automatically handles empty input fields per sk_p__complete.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: User must choose at Step 1; cannot proceed without selection
- **Controls**: Branch creation behavior and Step 14 integration gate

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

### Field Handling

#### Auto-Creation
- **git_branch**: Auto-create `feature-{NNN}` from highest +001
- **spec_folder**: Auto-create `specs/{NNN}` from highest +001
- **context**: Infer from request and staging link
- **issues**: Discover during workflow execution

#### Scope Policy
- **Default**: `specs/**`
- **Enforcement**: Limit file operations to scope
- **Validation**: Block operations outside scope

.

## 10. 🔗 Integration Points

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

.

## 11. ⚡ Performance Characteristics

**Note**: Performance varies based on system resources, complexity, and agent response efficiency.

- **Parallel Execution**: Significantly faster than sequential execution
- **Stage A**: Parallel execution of 4 planning agents + review + synthesis
- **Stage B**: Parallel execution of 4 implementation agents + review + synthesis
- **Stage C**: Parallel execution of 4 quality reviewers + review + synthesis
- **Orchestration**: Minimal overhead for coordination between stages

## 12. 🚨 Error Handling

### Retry Policy
- **Targeted retries**: Only failed agents
- **Max retries**: 2 per agent
- **Backoff**: Exponential with jitter

### Failure Modes
- **Agent failure**: Retry then fallback to sequential
- **Review failure**: Escalate to main agent
- **Synthesis failure**: Use partial results
- **Approval rejection**: Document and stop

.

## 13. ⚠️ Limitations

- **Requires parallel execution support**: Falls back to sequential if unavailable
- **Memory intensive**: 18 agents require significant context
- **Approval gates mandatory**: Cannot skip user confirmations
- **English only**: Agent prompts and outputs in English

.

## 14. 📈 Success Metrics

**Note**: Target quality metrics for workflow execution. These represent ideal performance goals.

- **Parallel efficiency**: Significant performance improvement vs sequential
- **Agent success rate**: >95% first attempt
- **Synthesis quality**: >90% coherence score
- **Approval rate**: >80% first-time approvals

.

## 15. References

## 🔧 Troubleshooting / Notes
- Missing inputs (branch_strategy/spec_folder): rerun Step 1 input collection
- Stage sequence confusion: follow YAML ↔ Steps Crosswalk mapping
- Branch integration issues: open a PR instead of force-pushing; resolve conflicts externally if needed
etrics

### Success Criteria / Quality Gates
- Approval gates acknowledged and passed at each step
- Planning, implementation plan, and quality report artifacts present
- No blockers in environment check; development checkpoints completed
- Crosswalk step-order adhered to; branch integration policy followed

## 15. References

- `references/sub-agents.md` - Detailed sub-agent definitions
- `references/parallel-stages.md` - Stage orchestration patterns
- `references/adaptive-rules.md` - Complexity handling rules