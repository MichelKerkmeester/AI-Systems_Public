---
name: speckit_feature_research
description: Conduct sequential technical research and investigation for SpecKit features. Execute comprehensive research workflow to produce research.md documentation through systematic collection, analysis, and synthesis.
---

# SpecKit Feature Research

Execute sequential technical research workflow to produce comprehensive documentation for feature planning and implementation.

## When to Use This Skill

**Use this skill when**:
- Conducting technical investigation for a new feature
- Researching libraries, frameworks, and ecosystem patterns
- Analyzing vendor solutions and alternatives
- Evaluating technical feasibility and costs
- Documenting platform constraints and limitations
- Creating comprehensive research documentation

**Do NOT use this skill for**:
- Full SpecKit workflow execution (use speckit_complete)
- Simple command recommendations
- Implementation without research
- Writing specs without investigation
- Workflows requiring parallel execution (use parallel_speckit_feature_research)

## Quick Command Reference

| Step | Command | Purpose |
|------|---------|----------|
| 1 | Manual | Request Analysis - Define research scope |
| 2 | Manual | Pre-work Review |
| 3 | Manual | Codebase Investigation |
| 4 | Manual | External Research |
| 5 | Manual | Technical Analysis |
| 6 | `/speckit.checklist` | Quality validation |
| 7 | Manual | Solution Design |
| 8 | Manual | Research Compilation |
| 9 | Manual | Branch Integration (optional) |

**Autonomous**: This workflow executes steps 1-8 without approval gates. Only step 9 (branch integration) requires user confirmation.

## Architecture Overview

This skill implements the sk__feature_research.yaml workflow with sequential execution by the main agent.

### Research Workflow Steps

1. **Request Analysis** - Define research scope and goals
2. **Pre-work Review** - Review AGENTS.md, code standards
3. **Codebase Investigation** - Investigate existing patterns
4. **External Research** - Research external documentation
5. **Technical Analysis** - Perform feasibility assessment
6. **Quality Checklist** - Generate quality gates
7. **Solution Design** - Architecture and integration patterns
8. **Research Compilation** - Compile comprehensive documentation
9. **Branch Integration** - Optional merge to main

**Note**: This is an autonomous workflow with NO approval gates (except branch integration).

## Workflow Steps (Detailed Execution)

This section provides step-by-step execution guidance as defined in sk__feature_research.yaml.

### Step 1: Request Analysis

**Action**: Analyze inputs, choose branch strategy, and define research scope and goals

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
- `issues`: Investigate during workflow if empty
- `request`: REQUIRED
- `environment`: Skip browser testing if empty
- `scope`: Default to `specs/**` if empty

**Outputs**:
- Branch strategy chosen
- Git branch resolved
- Research scope defined
- Feature summary
- Research objectives
- Complexity assessment
- Key questions to answer
- Research questions identified
- Investigation priorities
- Technical depth required
- Output structure planning

**Validation**: `scope_defined_and_branch_strategy_set`

**Approval Gate**: None (autonomous execution)

---

### Step 2: Pre-work Review

**Action**: Review required documents

**Required Documents**:
- AGENTS.md
- knowledge/code_standards.md
- knowledge/debugging.md

**Verification**: MUST REVIEW

**Validation**: `principles_established`

**Approval Gate**: None (autonomous execution)

---

### Step 3: Codebase Investigation

**Action**: Investigate existing codebase and patterns

**Research Areas**:
- existing_implementations
- related_components
- current_architecture
- code_conventions
- dependencies

**Tools**:
- grep_patterns
- file_exploration
- dependency_analysis

**Deep Analysis**:
- Focus: codebase_pattern_analysis
- Approach: systematic_code_investigation
- Outputs:
  - current_state_analysis
  - existing_patterns
  - technical_constraints
  - pattern_identification
  - architectural_constraints
  - reusable_components
  - integration_opportunities

**Validation**: `codebase_understood`

**Approval Gate**: None (autonomous execution)

---

### Step 4: External Research

**Action**: Research external documentation and best practices

**Sources**:
- official_documentation
- api_references
- community_solutions
- industry_standards
- similar_implementations

**Chrome DevTools** (when analyzing live examples):
- inspect_implementations
- analyze_network_patterns
- review_dom_structures
- capture_performance_metrics

**Deep Analysis**:
- Focus: external_solutions_analysis
- Approach: comprehensive_research
- Outputs:
  - best_practices_summary
  - external_solutions_analysis
  - api_specifications
  - integration_options
  - best_practice_synthesis
  - api_evaluation
  - integration_strategy
  - vendor_comparison

**Validation**: `external_research_complete`

**Approval Gate**: None (autonomous execution)

---

### Step 5: Technical Analysis

**Action**: Perform deep technical analysis and feasibility assessment

**Analysis Areas**:
- architecture_implications
- performance_considerations
- security_requirements
- accessibility_standards
- browser_compatibility
- mobile_responsiveness

**Deep Analysis**:
- Focus: technical_feasibility_analysis
- Approach: rigorous_evaluation
- Outputs:
  - technical_specifications
  - constraints_and_limitations
  - risk_assessment
  - compatibility_matrix
  - architecture_assessment
  - performance_projections
  - security_analysis
  - compatibility_verification
  - risk_mitigation_strategies

**Validation**: `technical_analysis_complete`

**Approval Gate**: None (autonomous execution)

---

### Step 6: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist: generated

**Validation**: `checklist_generated`

**Approval Gate**: None (autonomous execution)

---

### Step 7: Solution Design

**Action**: Design solution architecture and integration patterns

**Deliverables**:
- proposed_architecture
- integration_patterns
- api_design
- data_flow_diagrams
- component_interactions

**Chrome DevTools** (when prototyping solutions):
- test_api_endpoints
- validate_approaches
- measure_performance_impact
- verify_compatibility

**Deep Analysis**:
- Focus: solution_architecture_design
- Approach: comprehensive_design
- Outputs:
  - solution_architecture
  - implementation_patterns
  - code_examples
  - configuration_requirements
  - architectural_patterns
  - integration_blueprint
  - implementation_roadmap
  - edge_case_handling

**Validation**: `solution_designed`

**Approval Gate**: None (autonomous execution)

---

### Step 8: Research Compilation

**Action**: Compile comprehensive research documentation for spec folder

**Deep Analysis**:
- Focus: comprehensive_research_document
- Approach: exhaustive_documentation

**Required Sections**:
- changelog_and_updates
- investigation_report
- executive_overview
- architecture_analysis
- technical_specifications
- constraints_and_limitations
- integration_patterns
- implementation_guide
- code_examples_and_snippets
- testing_strategies
- performance_optimization
- security_considerations
- future_proofing
- api_reference
- troubleshooting_guide
- acknowledgements

**Document Structure**:
- Format: markdown
- Location: `[SPEC_FOLDER]/research.md`
- table_of_contents: required
- code_blocks: syntax_highlighted
- diagrams: ascii_art
- cross_references: linked

**Detailed Section Requirements**:

**Investigation Report**:
- request_summary
- current_behavior
- findings
- recommendations

**Overview**:
- executive_summary
- architecture_diagram
- quick_reference_guide
- research_sources

**Core Architecture**:
- system_components
- data_flow
- integration_points
- dependencies

**Technical Specifications**:
- api_documentation
- attribute_reference
- event_contracts
- state_management

**Constraints & Limitations**:
- platform_limitations
- security_restrictions
- performance_boundaries
- browser_compatibility
- rate_limiting

**Integration Patterns**:
- third_party_services
- authentication_handling
- error_management
- retry_strategies

**Implementation Guide**:
- markup_requirements
- javascript_implementation
- css_specifications
- configuration_options

**Code Examples**:
- initialization_patterns
- helper_functions
- api_usage
- edge_cases

**Testing & Debugging**:
- test_strategies
- debugging_approaches
- e2e_examples
- diagnostic_tools

**Performance**:
- optimization_tactics
- benchmarks
- rate_limiting
- caching_strategies

**Security**:
- validation_approach
- data_protection
- spam_prevention
- authentication

**Maintenance**:
- upgrade_paths
- compatibility_matrix
- decision_trees
- spa_support

**API Reference**:
- attributes_table
- javascript_api
- events_reference
- cleanup_methods

**Troubleshooting**:
- common_issues
- error_messages
- solutions
- workarounds

**Validation**: `documentation_complete`

**Final Output Message**:
```
Research documentation complete.
Comprehensive technical investigation has been documented in [SPEC_FOLDER]/research.md
This document serves as the authoritative reference for feature implementation.

Spec folder structure:
- [SPEC_FOLDER]/research.md - Complete research documentation

Next steps:
- Review research findings in the spec folder
- Validate technical approach
- Proceed to specification (/specify) if needed
- Use research as reference during implementation planning
```

**Approval Gate**: None (autonomous execution)

---

### Step 9: Branch Integration

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
  - Validations/tests/pass checks are green (as applicable)
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

**Termination**: Workflow ends after this step (or after Step 8 if main_branch was selected)

## Approval Gates

This workflow is **autonomous** with minimal user interaction:

| Step | Approval Prompt | Confirmation | Note |
|------|-----------------|--------------|------|
| 9 | "All checks passed. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?" | Required | Branch integration only |

**Note**: Steps 1-8 execute autonomously without approval gates. Only step 9 (branch integration) requires user confirmation.

## Field Handling

This workflow automatically handles empty input fields per sk__feature_research.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`feature_branch`, `main_branch`]
- **Options**:
  - `feature_branch`: Create new feature branch (auto-create feature-{NNN} aligned with spec folder)
  - `main_branch`: Work on main branch (skip branch creation and commit directly to main)
- **Empty Handling**: User must choose at Step 1; cannot proceed without selection
- **Controls**: Branch creation behavior and Step 9 integration gate

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

This workflow executes sequentially and autonomously:

```
Step 1: Request Analysis (autonomous)
        ↓
Step 2: Pre-work Review (autonomous)
        ↓
Step 3: Codebase Investigation (autonomous)
        ↓
Step 4: External Research (autonomous)
        ↓
Step 5: Technical Analysis (autonomous)
        ↓
Step 6: Quality Checklist (autonomous)
        ↓
Step 7: Solution Design (autonomous)
        ↓
Step 8: Research Compilation (autonomous)
        ↓
Step 9: Branch Integration [Approval Required if feature_branch]
        ↓
[Complete]
```

## Integration Points

### With Chrome DevTools
- Step 4: Test API endpoints, validate approaches
- Step 7: Measure performance impact, verify compatibility

### With SpecKit Workflow
- Research before `/speckit.specify`
- Inform technical planning
- Support implementation decisions
- Document constraints early

## Quality Standards

### Documentation Requirements
- production_ready_examples
- defensive_programming_patterns
- error_handling_strategies
- memory_leak_prevention
- spa_compatibility

### Code Examples
- working_snippets
- proper_error_handling
- performance_optimized
- accessibility_compliant
- browser_compatible

### Analysis Depth
- edge_cases_covered
- failure_modes_documented
- recovery_strategies_defined
- monitoring_approaches_specified

## Spec Folder Integration

**Note**: This workflow generates research.md within a spec folder structure. It does NOT follow the full GitHub SpecKit workflow (no /specify, /plan, etc). It creates comprehensive research documentation to support feature planning.

**Workflow Relationship**:
- This is a standalone research workflow
- Outputs to spec folders for consistency
- Can be used before or during SpecKit workflows
- Provides research foundation for specifications

**Expected Output**:
- `[SPEC_FOLDER]/research.md` - Primary research documentation
- Optional supplementary files in spec folder as needed

## Rules

**ALWAYS**:
- follow_research_methodology
- document_all_findings
- validate_technical_feasibility
- use_devtools_for_live_analysis
- generate_comprehensive_documentation
- self_validate_and_proceed
- do_not_prompt_for_user_approval
- limit_context_to_active_scope

**NEVER**:
- skip_investigation_steps
- ignore_platform_constraints
- submit_without_thorough_analysis
- proceed_to_implementation
- invent_new_patterns_when_existing_work

## Version

**Current Version**: 1.0.0
**Based On**: sk__feature_research.yaml
**Created**: 2025-10-18
**Architecture**: Sequential research execution with autonomous operation
