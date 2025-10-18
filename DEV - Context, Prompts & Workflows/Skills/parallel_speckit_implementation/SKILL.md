---
name: parallel_speckit_implementation
description: Execute autonomous spec-driven implementation with parallel preparation agents. Orchestrates 6 specialized sub-agents for implementation planning (core, integrations, tests, docs) through parallel execution, review, and synthesis into implementation_plan.md, then proceeds with development.
---

# SpecKit Implementation

Execute autonomous implementation workflow with parallel preparation and progressive development checkpoints.

## When to Use This Skill

**Use this skill when**:
- Ready to implement a fully specified feature
- Have spec.md and plan.md completed
- Need comprehensive implementation preparation
- Want parallel planning for core, tests, and docs
- Executing actual code changes autonomously

**Do NOT use this skill for**:
- Initial specification creation (use speckit-plan-spec)
- Research and investigation (use speckit-feature-research)
- Simple planning without implementation
- Manual implementation processes

## 🚀 Quick Command Reference

> **⚠️ CRITICAL**: This workflow starts at **Step 8** (continuation from planning workflow steps 1-7)

| Step | Command | Purpose |
|------|---------|----------|
| **8** | Manual | Review Plan and Spec |
| **9** | `/tasks` | Generate actionable tasks |
| **10** | `/analyze` | Check consistency |
| **11** | `/speckit.checklist` | Quality gates |
| **12** | *Parallel Block* | 4 implementation agents prepare |
| **13** | `/implement` | Verify prerequisites |
| **14** | Manual | Autonomous development |
| **15** | Manual | Document changes and completion |

**✅ Autonomous**: This workflow executes all steps without approval gates.

## Architecture Overview

This skill implements the sk_p__implementation.yaml workflow with 6 specialized implementation sub-agents executing in parallel preparation phase.

### Implementation Workflow Steps

**CRITICAL**: Step numbering starts at **8** (continuation from planning workflow steps 1-7).

**Note**: This workflow covers steps 8-15 of the complete SpecKit process (8 steps total). Steps 1-7 are assumed completed via planning workflow.

8. **Review Plan and Spec** - Understand existing artifacts
9. **Task Breakdown** - Generate actionable tasks
10. **Analysis** - Check consistency and coverage
11. **Quality Checklist** - Generate quality gates
12. **Parallel Implementation Prep** - 4 agents prepare approach
13. **Implementation Check** - Verify prerequisites
14. **Development** - Execute autonomous implementation
15. **Completion** - Document changes and summary

**Note**: This is an autonomous workflow with NO approval gates.

## Workflow Steps (Detailed Execution)

**Prerequisites**: Requires `spec.md`, `plan.md`, and `planning-summary.md` from steps 1-7.

This section provides step-by-step execution guidance as defined in sk_p__implementation.yaml.

### Step 8: Review Plan and Spec

**Note**: This workflow is a continuation of the planning phase (steps 1-7). Branch strategy should have been set during planning. If starting independently, branch_strategy must be provided.

**Action**: 
1. Confirm branch_strategy (should be inherited from planning phase)
2. Verify git_branch is correctly set based on strategy
3. Review spec and planning artifacts

**Branch Strategy** (inherited from planning):
- `branch_strategy`: Should be set from planning workflow
- `git_branch`: Derived from branch_strategy
  - If `feature_branch`: Uses feature-{NNN}
  - If `main_branch`: Uses main

**Required Documents**:
- `[SPEC_FOLDER]/spec.md`
- `[SPEC_FOLDER]/plan.md`
- `[SPEC_FOLDER]/planning-summary.md`

**Outputs**:
- Branch strategy confirmed
- Git branch validated
- Planning artifacts understood

**Validation**: `planning_artifacts_understood_and_branch_confirmed`

**Approval Gate**: None (autonomous execution)

---

### Step 9: Task Breakdown

**Command**: `/tasks`

**Action**: Generate actionable task checklist

**Outputs**:
- `tasks/checklist.md`
- Task duration: 15-60 minutes per task
- Tracking structure established

**Validation**: `tasks_actionable`

---

### Step 10: Analysis

**Command**: `/analyze`

**Action**: Check consistency and verify alignment

**Outputs**:
- Consistency report
- Coverage verification
- Alignment check
- Gap analysis

**Validation**: `consistency_verified`

---

### Step 11: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist generated

**Validation**: `checklist_generated`

---

### Step 12: Parallel Implementation Preparation

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

---

### Step 13: Implementation Check

**Command**: `/implement [task-id]`

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

---

### Step 14: Development

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

**Deep Analysis**:
- Focus: iterative_problem_solving
- Approach: continuous_validation
- Outputs: implementation_decisions, debugging_insights, optimization_opportunities, test_coverage_gaps

---

### Step 15: Completion

**Action**: Document changes and create summary

**Summary Document**:
- Location: `[SPEC_FOLDER]/implementation-summary.md`
- Required Sections:
  - Feature branch name
  - Files modified/created
  - Verification steps taken
  - Deviations from plan
  - Knowledge base updates
  - Recommended next steps
  - Browser testing results

**Final Checklist**:
- Update task status: completed
- Validation passed: confirmed
- Summary created: true
- Staging verified: true

**Deep Analysis**:
- Focus: comprehensive_completion_review
- Approach: retrospective_analysis
- Outputs: implementation_quality_assessment, lessons_learned, technical_debt_noted, future_improvements

**Termination**: Workflow ends after this step

**Branch Integration Note**:
- **If `feature_branch` was selected**: Branch has changes but is NOT automatically merged to main. User should run the complete workflow for branch integration or merge manually.
- **If `main_branch` was selected**: Changes are already on main; no integration needed.

**Next Steps**:
- Review implementation-summary.md
- Verify all changes in staging environment
- **If feature_branch**: Use complete workflow for branch integration or merge manually
- **If main_branch**: Changes are already integrated
- Prepare for code review and PR submission
- Update knowledge base if needed

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

## Execution Model

### Parallel Preparation Pattern

**Note**: All parallel execution, review, synthesis, and main agent finalization occur within Step 12 as sub-phases, NOT as separate steps.

```
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

## Implementation Plan Structure

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

---

## ✅ Approval Gates

This workflow is **autonomous** with NO approval gates:

| Step | Note |
|------|------|
| 8-15 | All steps execute autonomously without user approval |

**Note**: This is a fully autonomous workflow designed for continuous execution once prerequisites are met.

---

## ⚙️ Field Handling

This workflow automatically handles empty input fields per sk_p__implementation.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: Inherit from planning phase; if unavailable, prompt user
- **Note**: This field should be inherited from the planning workflow (steps 1-7). If starting implementation independently, prompt user for choice.

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

### Branch Creation
- **Condition**: Only execute when `branch_strategy == feature_branch`
- **Steps**:
  1. Check if feature branch already exists
  2. Create feature-{spec_id} if not exists
  3. Checkout feature branch
- **Skip When**: `branch_strategy == main_branch`
- **Note**: Branch should already exist from planning phase if feature_branch was selected

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

## Inputs

### Required Inputs
- **spec_folder**: Location with spec.md and plan.md
- **request**: Implementation requirements (or uses default)

### Optional Inputs
- **git_branch**: Feature branch name
- **context**: Additional implementation context
- **issues**: Known issues to address
- **environment**: Staging URL for testing
- **scope**: File scope limitations

### Default Request
If no request provided:
```
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

## Parallel Agent Details

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

## Development Checkpoints

### Major Change Checkpoint
- Log progress to summary
- Update task checklist
- Verify against spec

### Issue Found Checkpoint
- Document issue and resolution
- Update implementation plan if needed
- Continue or escalate

### Architecture Change Checkpoint
- Note deviation from plan
- Document rationale
- Update affected documentation

## Chrome DevTools Integration

### Environment Validation
- Test API endpoints
- Verify authentication
- Check dependencies

### Implementation Testing
- Test in browser
- Verify network calls
- Check console output
- Validate DOM changes
- Measure performance

## Adaptive Rules

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

## Quality Standards

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

## Performance Characteristics

**Note**: Performance varies based on implementation scope and complexity. Preparation is structured; implementation duration depends on feature requirements.

- **Preparation phase**: Parallel agent execution + review + synthesis
- **Parallel execution**: Multiple agents work concurrently
- **Review/synthesis**: Sequential refinement process
- **Implementation**: Variable based on scope and complexity
- **Checkpoints**: Lightweight validation points

## Error Handling

### Retry Policy
- **Targeted retries**: Only failed components
- **Max attempts**: 2 per agent
- **Backoff**: Exponential

### Recovery Actions
- Document blockers
- Use partial results
- Manual intervention points
- Graceful degradation

## Limitations

- **Prerequisites**: Requires completed spec/plan
- **Scope**: Limited to defined file scope
- **Autonomy**: No user interaction during execution
- **Testing**: Browser testing requires staging URL
- **Complexity**: Best for medium complexity features

## Success Metrics

**Note**: Target quality objectives for implementation execution.

- **Preparation completeness**: All sections populated
- **Review pass rate**: >90% first pass
- **Implementation coverage**: >95% tasks completed
- **Test coverage**: Meets defined targets
- **Documentation**: Complete and accurate

## Version

**Current Version**: 1.0.0
**Based On**: sk_p__implementation.yaml
**Created**: 2025-10-18
**Architecture**: Parallel preparation → Autonomous implementation

---

## References

- Source: `/b_prompts/github_spec_kit/parallel_agents/sk_p__implementation.yaml`
- Prerequisites: spec.md, plan.md, planning-summary.md
- Integration: Works with all SpecKit skills
- Output: implementation_plan.md, implementation-summary.md, code changes