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

## 🚀 Quick Command Reference

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

## Workflow Steps (Detailed Execution)

This section provides step-by-step execution guidance as defined in sk_p__complete.yaml.

### Step 1: Request Analysis

**Action**: Analyze user inputs and confirm understanding

**Input Source**: USER_INPUTS_SECTION

**Inputs**:
- `git_branch`: Auto-create `feature-{NNN}` if empty
- `spec_folder`: Auto-create `specs/{NNN}` if empty
- `context`: Infer from request if empty
- `issues`: Discover during workflow if empty
- `request`: REQUIRED
- `environment`: Skip DevTools steps if empty
- `scope`: Default to `specs/**` if empty

**Outputs**:
- Requirement summary
- Approach overview
- Complexity assessment

**Validation**: `understanding_confirmed`

**Approval Gate**: "Requirements analyzed. Proceed to pre-work review?"

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

**Approval Gate**: "Quality checklist complete. Proceed to planning parallel block?"

---

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

---

### Step 7: Task Breakdown

**Command**: `/tasks`

**Action**: Generate actionable task checklist

**Outputs**:
- tasks/checklist.md
- Task duration: 15_to_60_minutes
- Tracking structure: established

**Validation**: `tasks_actionable`

**Approval Gate**: "Tasks broken down. Review checklist.md and approve to proceed to analysis?"

---

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

---

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

---

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

---

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

---

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

---

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

---

### Step 14: Branch Integration

**Name**: Branch Integration Approval

**Approval Gate**: "All checks passed. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?"

**Confirmation Needed**: true

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

**Termination**: Workflow ends after this step

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

---

## ✅ Approval Gates

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

---

## ⚙️ Field Handling

This workflow automatically handles empty input fields per sk_p__complete.yaml:

### git_branch
- **Auto-create**: Yes
- **Default Pattern**: `feature-{NNN}` where {NNN} is highest existing +001
- **Scope**: Repository-wide feature branches
- **Empty Handling**: Automatically creates new branch following naming convention

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