---
name: speckit-implementer
description: Execute autonomous spec-driven implementation with parallel preparation agents. Orchestrates 6 specialized sub-agents for implementation planning (core, integrations, tests, docs) through parallel execution, review, and synthesis into implementation_plan.md, then proceeds with development
---

# SpecKit Implementer - Autonomous Implementation Workflow

## 1. 📄 Description

Execute autonomous spec-driven implementation with parallel preparation agents. Orchestrates 6 specialized sub-agents for implementation planning (core, integrations, tests, docs) through parallel execution, review, and synthesis into implementation_plan.md, then proceeds with development

## 📋 Table of Contents

- [📄 Description](#description)
- [🎯 When to Use](#when-to-use)
- [🚀 Quick Command Reference](#quick-command-reference)
- [🏗️ Architecture Overview](#architecture-overview)
- [📝 Steps](#steps)
- [📋 Implementation Plan Structure](#implementation-plan-structure)
- [✅ Approval Gates](#approval-gates)
- [⚙️ Field Handling](#field-handling)
- [📥 Inputs & Outputs](#inputs--outputs)
- [👥 Implementation Agents & Checkpoints](#implementation-agents--checkpoints)
- [🔗 Integration & Standards](#integration--standards)
- [⚡ Performance Characteristics](#performance-characteristics)
- [🚨 Error Handling](#error-handling)
- [⚠️ Limitations](#limitations)
- [📈 Success Metrics](#success-metrics)

.

## 2. 🎯 When to Use

**Use this skill when**:
- Ready to implement a fully specified feature
- Have spec.md and plan.md completed
- Need comprehensive implementation preparation
- Want parallel planning for core, tests, and docs
- Executing actual code changes autonomously

**Do NOT use this skill for**:
- Initial specification creation (use speckit-spec-plan)
- Simple planning without implementation
- Manual implementation processes

.

## 3. 🚀 Quick Command Reference

> **📌 Context Note**: This skill implements **Steps 8-17** from the SpecKit implementation process (continuation from planning steps 1-7). References to "Step N" indicate steps from the source YAML specification, while "Section N" refers to document organization below.

| Step | Command | Purpose |
|------|---------|----------|
| **8** | Manual | Review Plan and Spec |
| **9** | Manual | Workspace Setup |
| **10** | `/speckit.tasks` | Generate actionable tasks |
| **11** | `/speckit.analyze` | Check consistency |
| **12** | `/speckit.checklist` | Quality gates |
| **13** | *Parallel Block* | 4 implementation agents prepare |
| **14** | `/speckit.implement` | Verify prerequisites |
| **15** | Manual | Autonomous development |
| **16** | Manual | Completion summary |
| **17** | Manual | Integration & cleanup |

**✅ Autonomous**: This workflow executes all steps without approval gates

.

## 4. 🏗️ Architecture Overview

This skill implements the sk_p__implementation.yaml workflow with 6 specialized implementation sub-agents: 4 execute in the parallel preparation phase, followed by sequential review and synthesis.

### Implementation Steps

**Note**: This workflow covers Steps 8-17 of the complete SpecKit process. Steps 1-7 are assumed completed via planning workflow.

- **Step 8**: Review Plan and Spec - Understand existing artifacts
- **Step 9**: Workspace Setup - Verify/reuse or create worktree
- **Step 10**: Task Breakdown - Generate actionable tasks
- **Step 11**: Analysis - Check consistency and coverage
- **Step 12**: Quality Checklist - Generate quality gates
- **Step 13**: Parallel Implementation Prep - 4 agents prepare approach
- **Step 14**: Implementation Check - Verify prerequisites
- **Step 15**: Development - Execute autonomous implementation
- **Step 16**: Completion - Document changes and summary
- **Step 17**: Integration & Cleanup - Merge or push branch and clean up worktree

**Note**: This is an autonomous workflow with NO approval gates
Integration (Step 17) also proceeds autonomously without a manual approval gate.

.

## 5. 📝 Steps

**Prerequisites**: Requires `spec.md`, `plan.md`, and `planning-summary.md` from Steps 1-7.

This section provides step-by-step execution guidance as defined in sk_p__implementation.yaml.

### Step 8: Gather User Inputs & Review Plan and Spec

**Note**: This workflow is typically a continuation of the planning phase (Steps 1-7). If continuing from planning, inputs should be inherited. If starting independently, all inputs must be collected first.

**Action**: Collect inputs (if not inherited), then review spec and planning artifacts

**IMPORTANT**: Before starting implementation, ask the user for the following inputs in a conversational way (skip if inherited from planning):

#### Required Inputs:

1. **Branch Strategy** (REQUIRED if not inherited):
   - Ask: "Select development isolation strategy (or inherit from planning):"
   - Options:
     - **main_temp** (⭐ RECOMMENDED - default): Temporary worktree with short-lived branch.
       Work is isolated, tested, then merged back to main immediately.
       Use for: 80% of work - normal features, bug fixes, improvements.

     - **feature_branch**: Long-running feature branch in worktree for PR review.
       Work stays on separate branch for team review before integration.
       Use for: 20% of work - complex features requiring multi-day development and code review.

   - Default: Inherit from planning workflow if available, otherwise `main_temp`
   - Note: main_branch option removed (use main_temp for quick integration)
   - If inherited from planning workflow, use the existing branch_strategy.

2. **Request/Implementation Goal** (OPTIONAL):
   - Ask: "What should I implement? (Leave empty to use default: 'Conduct comprehensive review of spec folder and carry out its implementation fully autonomously')"
   - Default: "Conduct a comprehensive review of the spec folder and carry out its implementation fully autonomously."

#### Optional Inputs (with smart defaults):

3. **Spec Folder**:
   - Ask: "Which spec folder should I implement? (Leave empty to auto-create `specs/{NNN}`)"
   - Default: Auto-determine from existing specs

4. **Context**:
   - Ask: "Any additional context about this implementation? (Leave empty to infer from spec/plan)"
   - Default: Infer from spec and plan documents

5. **Known Issues**:
   - Ask: "Are there any known issues to address during implementation? (Leave empty to investigate)"
   - Default: Discover during implementation

6. **Environment/Staging Link**:
   - Ask: "Do you have a staging environment URL to test against? (Leave empty to skip browser testing)"
   - Default: Skip DevTools/browser testing if not provided

7. **Scope/Files**:
   - Ask: "Which files should I focus on? (Leave empty to use all relevant project files)"
   - Default: All relevant project files

**After Collecting Inputs**:
- Confirm all inputs with the user
- Resolve `git_branch` from branch_strategy (either `feature-{NNN}` or `main`)
- Review required planning artifacts

**Required Documents**:
- `[SPEC_FOLDER]/spec.md`
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

**Outputs**:
- Branch strategy confirmed
- Git branch validated
- All inputs confirmed
- Planning artifacts understood

**Validation**: `all_inputs_collected_and_planning_artifacts_understood`

**Approval Gate**: None (autonomous execution)

### Step 9: Workspace Setup

**Action**: Create or verify isolated worktree for implementation

**Note**: If continuing from planning workflow (speckit-spec-plan), worktree may already exist. Verify and reuse if available, otherwise create new.

**Skill Invocation**: Execute git-worktrees workflow (if worktree doesn't exist)
**Strategy**: Use selected or inherited branch_strategy
**Inputs passed**:
- Task description: {request}
- Branch strategy: {branch_strategy}
- Worktree directory: Auto-detect via priority system

**Worktree Verification/Creation**:
- Check if worktree exists at `.worktrees/{spec-id}`
- If exists: Verify it's clean and ready
- If not exists:
  - If main_temp: Creates `.worktrees/{spec-id}` with temp branch `temp/{spec-id}`
  - If feature_branch: Creates `.worktrees/{spec-id}` with branch `feature-{spec-id}`

**Dependencies verified**: Already installed (from planning) or auto-detected (npm/cargo/pip/go)
**Tests run**: Baseline verification (if worktree newly created)
**Environment verified**: Clean starting state for implementation

**Outputs**:
- worktree_path: Absolute path to worktree (e.g., `.worktrees/001`)
- git_branch: Active branch name (e.g., `temp/001` or `feature-001`)
- worktree_status: existing | newly_created
- baseline_tests: Pass/fail status

**Validation**: `worktree_ready_for_implementation`

**Note**: All subsequent steps execute within this worktree context

### Step 10: Task Breakdown

**Command**: `/speckit.tasks`

**Action**: Generate actionable task checklist

**Outputs**:
- `tasks/checklist.md`
- Task duration: 15-60 minutes per task
- Tracking structure established

**Validation**: `tasks_actionable`

### Step 11: Analysis

**Command**: `/speckit.analyze`

**Action**: Check consistency and verify alignment

**Outputs**:
- Consistency report
- Coverage verification
- Alignment check
- Gap analysis

**Validation**: `consistency_verified`

### Step 12: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist generated

**Validation**: `checklist_generated`

### Step 13: Parallel Implementation Preparation

**Description**: Parallel preparation for core, integrations, tests, and docs

This step contains sub-phases that execute sequentially:

#### Phase A: Analyze Inputs

**Summarize**:
- Key requirements
- Constraints
- Unknowns

**Shard Plan Across**:
- Core
- Adapters
- Tests
- Docs

#### Phase B: Parallel Work

**Execution**: Parallel

**Concurrency**: 3 (maximum parallel agents)

**Shared Context**:
- `[SPEC_FOLDER]/spec.md`
- `[SPEC_FOLDER]/plan.md`
- `tasks/checklist.md`
- consistency_report

**Tasks**:

1. **Core Implementer**:
   - Instructions: Draft module breakdown, key data structures, and algorithmic approach with rationale
   - Expected Output Sections: modules, data_structures, algorithms, rationale

2. **Integrations/Adapters Engineer**:
   - Instructions: Enumerate integration points, API contracts, error-handling, and configuration matrix
   - Expected Output Sections: integrations, api_contracts, error_handling, configuration

3. **Test Engineer**:
   - Instructions: Define test plan with key test cases, fixtures, and coverage goals
   - Expected Output Sections: test_plan, key_cases, fixtures, coverage_targets

4. **Docs Engineer**:
   - Instructions: Draft developer-facing docs: usage patterns, examples, migration notes
   - Expected Output Sections: usage, examples, migration_upgrade

#### Phase C: Review

**By**: Integration Reviewer

**Focus**:
- Coherence across tracks
- API consistency
- Testability
- Identify gaps

**Outputs**:
- Synthesis guidance
- Review notes

#### Phase D: Synthesis

**By**: Lead Synthesizer

**Action**: Produce `implementation_plan.md` combining parallel outputs + review guidance

**Output Files**:
- `[SPEC_FOLDER]/implementation_plan.md`

**Validation Checklist**:
- Modules and integrations aligned
- Tests cover critical paths
- Docs reflect actual interfaces
- Risks and open questions listed

#### Phase E: Main Agent Finalization

**By**: MAIN_AGENT

**Action**: QA review and finalization of `[SPEC_FOLDER]/implementation_plan.md`

**Checks**:
- Confirm alignment with request and context
- Validate completeness and consistency
- Ensure output format and sections present
- Resolve remaining open questions or note them

**Outputs**:
- Main agent review notes
- Final signoff: true

**Note**: Main agent finalization occurs within this step (no subsequent approval gate)

### Step 14: Implementation Check

**Command**: `/speckit.implement [task-id]`

**Action**: Verify prerequisites before code changes

**Checks**:
- Prerequisites: verified
- Blockers: none
- Environment: ready

**Chrome DevTools** (when validating environment):
- Verify API endpoints accessible
- Check authentication working
- Confirm dependencies loaded

**Deep Analysis**:
- Focus: pre_implementation_verification
- Approach: environment_validation
- Outputs: environment_status, dependency_verification, blocker_identification, readiness_confirmation

**Validation**: Environment ready for implementation

### Step 15: Development

**Approach**: Autonomous implementation with checkpoints

**Requirements**:
- Follow: `knowledge/code_standards.md`
- Update: task_checklist_progressively
- Test: before_commit
- No premature optimization

**Checkpoints**:

**Major Changes**:
- Action: Log progress

**Issues Found**:
- Action: Document resolution

**Architecture Change**:
- Action: Note deviation

**Chrome DevTools** (when debugging implementation):
- Test in browser
- Verify network calls
- Check console output
- Validate DOM changes
- Measure performance impact

For deeper debugging techniques and patterns, see `knowledge/debugging.md`.

**Deep Analysis**:
- Focus: iterative_problem_solving
- Approach: continuous_validation
- Outputs: implementation_decisions, debugging_insights, optimization_opportunities, test_coverage_gaps

### Step 16: Completion

**Action**: Document changes and create summary

#### Part A: Documentation

**Summary Document**:
- Location: `[SPEC_FOLDER]/implementation-summary.md`
- Required Sections:
  - Branch name and strategy used
  - Worktree path
  - Files modified/created
  - Verification steps taken
  - Deviations from plan
  - Knowledge base updates
  - Recommended next steps
  - Browser testing results
  - Integration status

**Final Checklist**:
- Update task status: completed
- Validation passed: confirmed
- Summary created: true
- Staging verified: true

**Deep Analysis**:
- Focus: comprehensive_completion_review
- Approach: retrospective_analysis
- Outputs: implementation_quality_assessment, lessons_learned, technical_debt_noted, future_improvements

### Step 17: Integration & Cleanup

**Action**: Integrate work based on branch_strategy

##### If main_temp (Default - 80% of work):

**Philosophy**: Temp branches are immediately merged and deleted

**Integration Steps**:
1. Verify worktree clean (no uncommitted changes)
2. Return to main repository
3. Checkout and update main: `git checkout main && git pull --ff-only`
4. Merge temp branch: `git merge --ff-only temp/{spec-id}`
5. Delete temp branch: `git branch -d temp/{spec-id}`
6. Remove worktree: `git worktree remove .worktrees/{spec-id}`
7. Verify integration complete

**Validation**: `temp_branch_integrated_and_cleaned`

**Termination**: Workflow ends after integration

##### If feature_branch (Exception - 20% of work):

**Philosophy**: Long-running branches remain for PR workflow

**Actions**:
1. Push feature branch: `git push -u <remote> feature-{spec-id}` (default remote: `origin`)
2. Keep worktree: Preserved at `.worktrees/{spec-id}` for continued work
3. Notify user: Feature branch ready for PR creation

**Next Steps** (User manual):
- Create PR on GitHub/GitLab
- Request code review
- Address feedback in worktree
- Merge via web interface after approval
- Manual cleanup after PR merged

**Validation**: `feature_branch_pushed_and_ready_for_pr`

**Termination**: Workflow pauses; PR workflow takes over

#### Troubleshooting

**Issue**: "Merge not fast-forward"
**Solution**: Rebase temp branch onto main, then retry merge

**Issue**: "Worktree removal fails"
**Solution**: Commit or stash uncommitted changes first

**Issue**: "Temp branch still exists after cleanup"
**Solution**: Force delete with `git branch -D temp/{spec-id}`

### The 6 Implementation Sub-Agents

**Note**: For detailed agent specifications with complete output formats, see [references/sub-agents.md](references/sub-agents.md).

1. **Core Implementer**
   - Module breakdown
   - Data structures
   - Algorithms
   - Business logic

2. **Integrations/Adapters Engineer**
   - External integrations
   - API surfaces
   - Configuration matrix
   - Error handling

3. **Test Engineer**
   - Test plan creation
   - Test cases definition
   - Fixtures preparation
   - Coverage targets

4. **Docs Engineer**
   - Usage documentation
   - Code examples
   - Migration notes
   - API documentation

5. **Integration Reviewer**
   - Coherence validation
   - API consistency
   - Testability assessment
   - Gap identification

6. **Lead Synthesizer**
   - Implementation strategy
   - Task ordering
   - Dependency mapping
   - Plan document creation

```text
┌─────────────────────────────────┐
│  Parallel Implementation Prep    │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │Core│ │Intg│ │Test│ │Docs│   │ ← Execute in parallel
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Integration Review          │ ← Reviewer validates coherence
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Synthesis Phase           │ ← Synthesizer creates plan
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Main Agent QA Phase         │ ← Final validation (no approval gate)
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│    Autonomous Implementation     │ ← Execute code changes
└─────────────────────────────────┘
```

### Parallel Execution Configuration

**Concurrency Settings**:
- **Default**: 3 parallel implementation agents maximum
- **High Complexity**: 2 parallel agents (reduced concurrency)
- **Fallback**: 1 (sequential execution if parallel not supported)

**Shared Context** (passed to all parallel agents):
- `[SPEC_FOLDER]/spec.md` - Feature specification
- `[SPEC_FOLDER]/plan.md` - Technical plan
- `tasks/checklist.md` - Task breakdown
- consistency_report - Analysis results

**Important**:
- Review and synthesis phases execute sequentially AFTER parallel work completes
- Main agent finalization occurs within Step 12 (no approval gate)
- All phases in Step 12 are sub-phases within that single workflow step
- This is an autonomous workflow - no user approval needed

.

## 6. 📋 Implementation Plan Structure

The skill produces `implementation_plan.md` with these sections:

### Core Sections

**Module Architecture**
- Component breakdown
- Module responsibilities
- Interface definitions
- Dependency graph

**Data Structures**
- Type definitions
- State management
- Data flow patterns
- Storage schemas

**Integration Points**
- External APIs
- Service contracts
- Configuration requirements
- Error handling strategies

**Test Strategy**
- Unit test plan
- Integration tests
- E2E scenarios
- Coverage targets

### Supporting Sections

**Development Approach**
- Implementation sequence
- Task dependencies
- Risk mitigation
- Checkpoint definitions

**Documentation Plan**
- User guides
- API references
- Migration guides
- Code examples

**Quality Gates**
- Acceptance criteria
- Performance targets
- Security requirements
- Accessibility standards

.

## 7. ✅ Approval Gates

This workflow is **autonomous** with NO approval gates:

| Step | Note |
|------|------|
| 8-15 | All steps execute autonomously without user approval |

**Note**: This is a fully autonomous workflow designed for continuous execution once prerequisites are met

.

## 8. ⚙️ Field Handling

This workflow automatically handles empty input fields per sk_p__implementation.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`main_temp`, `feature_branch`]
- **Default**: Inherit from planning phase, otherwise `main_temp` ⭐
- **Options**:
  - `main_temp`: Create temporary worktree with short-lived branch. Merge immediately after completion (80% of work)
  - `feature_branch`: Create long-running feature branch in worktree for PR workflow (20% of work)
- **Empty Handling**: Inherit from planning phase; if unavailable, defaults to `main_temp`
- **Breaking Change**: `main_branch` option removed; use `main_temp` for quick integration
- **Note**: This field should be inherited from the planning workflow (Steps 1-7). If starting implementation independently, defaults to `main_temp`.

### spec_id
- **Derived From**: spec_folder path using pattern `specs/{NNN}` or `specs/{NNN-name}`
- **Fallback**: Extract numeric portion or use timestamp if extraction fails
- **Usage**: Used to generate worktree path and branch name

### temp_branch_name
- **Pattern**: `temp/{spec_id}`
- **Condition**: Only used when `branch_strategy == main_temp`
- **Lifecycle**: Created, used, merged, deleted automatically

### feature_branch_name
- **Pattern**: `feature-{spec_id}`
- **Condition**: Only used when `branch_strategy == feature_branch`
- **Lifecycle**: Created, used, pushed for PR, manually cleaned up after merge

### git_branch
- **Derived**: Based on branch_strategy
- **If main_temp**: Use `temp/{spec-id}` (e.g., `temp/001`)
- **If feature_branch**: Use `feature-{spec-id}` (e.g., `feature-001`)
- **Empty Handling**: Cannot be empty; derived automatically from branch_strategy

### worktree_path
- **Pattern**: `.worktrees/{spec-id}`
- **Purpose**: Isolated workspace for implementation
- **Verification**: At Step 9, check if exists from planning phase
- **Lifecycle**:
  - If main_temp: Created → Used → Removed (Step 17)
  - If feature_branch: Created → Used → Preserved for PR workflow

### spec_folder
- **Auto-create**: Yes
- **Default Pattern**: `specs/{NNN}` where {NNN} is highest existing +001
- **Scope**: Project specs directory
- **Empty Handling**: Automatically creates new folder following naming convention

### Worktree & Branch Creation
- **Execution**: Step 9 via git-worktrees skill invocation
- **Verification**: Check if worktree already exists from planning phase
- **Creation** (if not exists):
  1. Determine spec_id from spec_folder
  2. Create worktree at `.worktrees/{spec-id}`
  3. Create and checkout branch based on strategy:
     - If main_temp: Create `temp/{spec-id}` from main
     - If feature_branch: Create `feature-{spec-id}` from main
  4. Install dependencies in worktree (if newly created)
  5. Run baseline tests
  6. Return worktree_path and git_branch
- **Reuse** (if exists): Verify worktree is clean and ready for implementation
- **Note**: All workspace setup delegated to git-worktrees skill

### request
- **Default**: "Conduct a comprehensive review of the spec folder and carry out its implementation fully autonomously."
- **Override**: Uses provided request if specified
- **Empty Handling**: Uses default request string

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

.

## 9. 📥 Inputs & Outputs

### Inputs

#### Required Inputs
- **spec_folder**: Location with spec.md and plan.md
- **request**: Implementation requirements (or uses default)

#### Optional Inputs
- **git_branch**: Feature branch name
- **context**: Additional implementation context
- **issues**: Known issues to address
- **environment**: Staging URL for testing
- **scope**: File scope limitations

### Default Request
If no request provided:
```text
"Conduct a comprehensive review of the spec folder and
carry out its implementation fully autonomously."
```

## Outputs

### Primary Outputs

1. **implementation_plan.md**
   - Location: `[SPEC_FOLDER]/implementation_plan.md`
   - Complete implementation strategy
   - All preparation artifacts synthesized

2. **implementation-summary.md**
   - Location: `[SPEC_FOLDER]/implementation-summary.md`
   - Files modified/created
   - Verification steps taken
   - Deviations from plan

3. **Actual Code Changes**
   - Implementation of all tasks
   - Tests and documentation
   - Progressive updates

.

## 10. 👥 Implementation Agents & Checkpoints

### Parallel Agent Details

### Core Implementer Output
```yaml
modules:
  - name: [module name]
    responsibility: [purpose]
    exports: [public interface]
    dependencies: [imports]
data_structures:
  - type: [structure]
    purpose: [usage]
    fields: [properties]
algorithms:
  - name: [algorithm]
    complexity: [Big O]
    approach: [description]
```

### Integration Engineer Output
```yaml
integrations:
  - service: [external service]
    protocol: [REST/GraphQL/etc]
    authentication: [method]
api_contracts:
  - endpoint: [path]
    method: [HTTP method]
    request: [schema]
    response: [schema]
error_handling:
  - error_type: [class]
    handling: [strategy]
    recovery: [approach]
```

### Test Engineer Output
```yaml
test_plan:
  unit_tests:
    - module: [name]
      cases: [count]
      coverage: [target%]
  integration_tests:
    - scenario: [description]
      components: [list]
  fixtures:
    - name: [fixture]
      purpose: [usage]
      data: [sample]
```

### Docs Engineer Output
```yaml
documentation:
  usage_guide:
    - section: [title]
      content: [outline]
  api_reference:
    - endpoint: [name]
      description: [purpose]
  examples:
    - scenario: [use case]
      code: [snippet]
  migration:
    - from: [version]
      to: [version]
      steps: [process]
```

### Development Checkpoints

#### Major Change Checkpoint
- Log progress to summary
- Update task checklist
- Verify against spec

#### Issue Found Checkpoint
- Document issue and resolution
- Update implementation plan if needed
- Continue or escalate

### Architecture Change Checkpoint
- Note deviation from plan
- Document rationale
- Update affected documentation

.

## 11. 🔗 Integration & Standards

### Chrome DevTools Integration

#### Environment Validation
- Test API endpoints
- Verify authentication
- Check dependencies

#### Implementation Testing
- Test in browser
- Verify network calls
- Check console output
- Validate DOM changes
- Measure performance

- Measure performance impact

### Adaptive Rules

**Note**: For complete adaptive rule specifications, complexity assessment, technical debt scoring, and testing strategies, see [references/adaptive-rules.md](references/adaptive-rules.md).

### High Complexity
- Reduce concurrency to 2
- Exhaustive review depth
- Additional validation steps

### High Uncertainty
- Add discovery phase before parallel
- Document assumptions
- Create proof of concepts

### Fallback Strategy
- Sequential execution if parallel fails
- Maintain review/synthesis phases
- Continue with partial results

### Quality Standards

### Implementation Requirements
- Follow code_standards.md
- Progressive task updates
- Test before commit
- No premature optimization

### Documentation Standards
- Developer-facing clarity
- Working code examples
- Migration paths documented
- API contracts complete

### Testing Requirements
- Critical paths covered
- Edge cases identified
- Performance benchmarks
- Security validations
- Source attribution present

.

## 12. ⚡ Performance Characteristics

**Note**: Performance varies based on implementation scope and complexity. Preparation is structured; implementation duration depends on feature requirements.

- **Preparation phase**: Parallel agent execution + review + synthesis
- **Parallel execution**: Multiple agents work concurrently
- **Review/synthesis**: Sequential refinement process
- **Implementation**: Variable based on scope and complexity
- **Checkpoints**: Lightweight validation points

.

## 13. 🚨 Error Handling

### Retry Policy
- **Targeted retries**: Only failed components
- **Max attempts**: 2 per agent
- **Backoff**: Exponential

### Recovery Actions
- Document blockers
- Use partial results
- Manual intervention points
- Graceful degradation
- Provide fallback recommendations

.

## 14. ⚠️ Limitations

- **Prerequisites**: Requires completed spec/plan
- **Scope**: Limited to defined file scope
- **Autonomy**: No user interaction during execution
- **Testing**: Browser testing requires staging URL
- **Complexity**: Best for medium complexity features

.

## 15. 📈 Success Metrics

**Note**: Target quality objectives for implementation execution.

- **Preparation completeness**: All sections populated
- **Review pass rate**: >90% first pass
- **Implementation coverage**: >95% tasks completed
- **Test coverage**: Meets defined targets
- **Documentation**: Complete and accurate
