---
name: speckit-feature-research
description: Conduct parallel technical research and investigation for SpecKit features. Orchestrates 6 specialized research sub-agents to produce comprehensive research.md documentation through parallel collection, review, and synthesis phases
---

# SpecKit Feature Research
Parallel Technical Investigation

## 1. 🎯 When to Use

**Use this skill when**:
- Conducting technical investigation for a new feature
- Researching libraries, frameworks, and ecosystem patterns
- Analyzing vendor solutions and alternatives
- Evaluating technical feasibility and costs
- Documenting platform constraints and limitations
- Creating comprehensive research documentation

**Do NOT use this skill for**:
- Full SpecKit workflow execution (use speckit-complete)
- Implementation without research
- Writing specs without investigation

.

## 2. 🚀 Quick Command Reference

| Step | Command | Purpose |
|------|---------|----------|
| 1 | Manual | Request Analysis - Define research scope |
| 2 | Manual | Pre-work Review |
| 3 | *Parallel Block* | 4 researchers collect data |
| 4 | Manual | Research Compilation |
| 5 | `/speckit.checklist` | Quality validation |
| 6 | Manual | Solution Design |
| 7 | Manual | Final Compilation |
| 8 | Manual | Branch Integration (optional) |

**✅ Autonomous**: This workflow executes steps 1–7 without approval gates. Step 8 (branch integration) requires explicit user confirmation.

.

## 3. 🏗️ Architecture Overview

This skill implements the sk_p__feature_research.yaml workflow with 6 specialized research sub-agents executing in parallel.

### Research Steps

1. **Request Analysis** - Define research scope and goals
2. **Pre-work Review** - Review AGENTS.md, code standards
3. **Parallel Research Block** - 4 researchers collect data
4. **Research Compilation** - Intermediate compilation
5. **Quality Checklist** - Generate quality gates
6. **Solution Design** - Architecture and integration patterns
7. **Final Research Compilation** - Complete comprehensive documentation
8. **Branch Integration** - Optional merge to main

**Note**: This workflow runs autonomously for steps 1–7; step 8 requires user confirmation for branch integration.

,

## 4. 📝 Steps

This section provides step-by-step execution guidance as defined in sk_p__feature_research.yaml.

### Step 1: Gather User Inputs & Define Research Scope

**Action**: Collect all required information from the user before proceeding with research

**IMPORTANT**: Before starting the workflow, ask the user for the following inputs in a conversational way:

#### Required Inputs:

1. **Branch Strategy** (REQUIRED):
   - Ask: "Select development isolation strategy for this research:"
   - Options:
     - **main_temp** (⭐ RECOMMENDED - default): Temporary worktree with short-lived branch `temp/{NNN}`. Work is isolated, then merged back to main immediately after research.
     - **feature_branch**: Long-running feature branch `feature-{NNN}` in a worktree for PR review.
   - Default: `main_temp`
   - This decision controls workspace setup and final integration gates.

2. **Research Request** (REQUIRED):
   - Ask: "What would you like to research? Please describe the feature or technical area you need investigated."
   - This is the main research topic that drives the investigation.

#### Optional Inputs (with smart defaults):

3. **Spec Folder**:
   - Ask: "Which spec folder should I use for research documentation? (Leave empty to auto-create `specs/{NNN}` from highest +001)"
   - Default: Auto-create `specs/{NNN}` based on existing specs

4. **Context**:
   - Ask: "Any additional context about this research? (Leave empty to infer from your request)"
   - Default: Infer from request and environment

5. **Known Issues**:
   - Ask: "Are there any known issues or constraints to investigate? (Leave empty to investigate during workflow)"
   - Default: Discover during research

6. **Environment/Staging Link**:
   - Ask: "Do you have a staging environment URL? (Leave empty to skip browser testing)"
   - Default: None (browser testing steps skipped)

7. **Scope/Files**:
   - Ask: "Which files or directories should I focus on? (Leave empty to default to `specs/**`)"
   - Default: `specs/**`

**After Collecting Inputs**:
- Confirm all inputs with the user
- Resolve `git_branch` from branch_strategy (`temp/{NNN}` for main_temp, or `feature-{NNN}`)
- Define research scope and goals
- Identify key research areas

**Outputs**:
- Branch strategy chosen
- Git branch resolved
- Spec folder determined
- All inputs confirmed
- Research scope defined
- Research goals established

**Validation**: `all_inputs_collected_and_scope_defined`

**Approval Gate**: None (autonomous execution)

### Step 1.5: Workspace Setup

**Action**: Create isolated worktree for research

**Skill Invocation**: Execute git-worktrees workflow
**Strategy**: Use selected `branch_strategy` (default: `main_temp`)
**Inputs passed**:
- Task description: {request}
- Branch strategy: {branch_strategy}
- Worktree directory: Auto-detect via priority system

**Worktree Creation**:
- If `main_temp`: Creates `.worktrees/{spec-id}` with temp branch `temp/{spec-id}`
- If `feature_branch`: Creates `.worktrees/{spec-id}` with branch `feature-{spec-id}`

**Dependencies installed**: Auto-detected (npm/cargo/pip/go)
**Tests run**: Baseline verification (if applicable)
**Environment verified**: Clean starting state

**Outputs**:
- worktree_path: Absolute path to worktree (e.g., `.worktrees/003`)
- git_branch: Active branch name (e.g., `temp/003` or `feature-003`)
- baseline_tests: Pass/fail status

**Validation**: `worktree_ready_and_verified`

**Note**: All subsequent steps execute within this worktree context

### Step 2: Pre-work Review

**Action**: Review required documents

**Required Documents**:
- AGENTS.md
- knowledge/code_standards.md
- knowledge/debugging.md

**Validation**: `principles_established`

**Approval Gate**: None (autonomous execution)

### Step 3: Parallel Research Block

**Description**: Parallel research execution spanning codebase and external sources

This step contains sub-phases that execute sequentially:

#### Phase A: Analyze Inputs

**Define Queries**:
- Domains to search
- Keywords and search terms
- Constraints and filters

**Structure Outputs**:
- Fields: title, url, quote, finding, assessment, confidence

#### Phase B: Parallel Work

**Execution**: Parallel

**Concurrency**: 3 (maximum parallel agents)

**Shared Context**:
- request
- context

**Tasks**:

1. **Web/Ecosystem Researcher**:
   - Instructions: Collect libraries, repos, issues, ecosystem patterns with pros/cons
   - Focus: Libraries, frameworks, repos, issues, community patterns

2. **Academic/Docs Researcher**:
   - Instructions: Collect standards, official docs, papers; extract key constraints and canonical patterns
   - Focus: Standards, RFCs, official documentation, academic papers, canonical patterns

3. **Competitive/Market Analyst**:
   - Instructions: Collect vendor options, alternatives, benchmark data
   - Focus: Vendor solutions, alternative approaches, benchmarks, market trends

4. **Feasibility/Cost Analyst**:
   - Instructions: Analyze complexity, cost, operational impact, risks
   - Focus: Technical complexity, operational costs, risk assessment, trade-offs

#### Phase C: Review

**By**: Lead Reviewer

**Focus**:
- Deduplicate findings
- Rank relevance
- Identify conflicts
- Flag insufficient citations

**Outputs**:
- Synthesis guidance
- Ranked findings
- Contradictions noted

#### Phase D: Synthesis

**By**: Lead Synthesizer

**Action**: Produce research.md per required sections

**Output Files**:
- `[SPEC_FOLDER]/research.md`

**Validation Checklist**:
- Citations present
- Contradictory sources flagged
- Options matrix complete
- Recommendation justified

#### Phase E: Main Agent Finalization

**By**: MAIN_AGENT

**Action**: QA review and finalization of `[SPEC_FOLDER]/research.md`

**Checks**:
- Confirm alignment with request and context
- Validate completeness and consistency
- Ensure output format and sections present
- Resolve remaining open questions or note them

**Outputs**:
- Main agent review notes
- Final signoff: true

**Note**: Main agent finalization occurs within this step (no subsequent approval gate)

### Step 4: Research Compilation

**Action**: Intermediate compilation (note: research document already synthesized in step 3)

**Note**: Ensure section coverage and polish

**Validation**: Research sections structured

### Step 5: Quality Checklist

**Command**: `/speckit.checklist`

**Action**: Generate quality validation checklist

**Outputs**:
- Quality checklist generated

**Validation**: `checklist_generated`

### Step 6: Solution Design

**Action**: Design solution architecture and integration patterns

**Deliverables**:
- Proposed architecture
- Integration patterns
- API design
- Data flow diagrams
- Component interactions

**Chrome DevTools** (when prototyping solutions):
- Test API endpoints
- Validate approaches
- Measure performance impact
- Verify compatibility

**Deep Analysis**:
- Focus: solution_architecture_design
- Approach: comprehensive_design
- Outputs: solution_architecture, implementation_patterns, code_examples, configuration_requirements, architectural_patterns, integration_blueprint, implementation_roadmap, edge_case_handling

**Validation**: `solution_designed`

### Step 7: Final Research Compilation

**Action**: Compile comprehensive research documentation for spec folder

**Deep Analysis**:
- Focus: comprehensive_research_document
- Approach: exhaustive_documentation

**Required Sections** (complete list in YAML lines 217-289):
- Changelog and updates
- Investigation report
- Executive overview
- Architecture analysis
- Technical specifications
- Constraints and limitations
- Integration patterns
- Implementation guide
- Code examples and snippets
- Testing strategies
- Performance optimization
- Security considerations
- Future proofing
- API reference
- Troubleshooting guide
- Acknowledgements

**Document Structure**:
- Format: Markdown
- Location: `[SPEC_FOLDER]/research.md`
- Table of contents: Required
- Code blocks: Syntax highlighted
- Diagrams: ASCII art
- Cross-references: Linked

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
- Proceed to specification (/speckit.specify) if needed
- Use research as reference during implementation planning
```

### Step 8: Branch Integration & Cleanup

**Action**: Integrate research outputs and cleanup based on strategy

#### If `main_temp` (Default)
1. Verify worktree clean
2. Return to main repository
3. Checkout and update main: `git checkout main && git pull --ff-only`
4. Fast-forward merge temp branch: `git merge --ff-only temp/{spec-id}`
5. Delete temp branch: `git branch -d temp/{spec-id}`
6. Remove worktree: `git worktree remove .worktrees/{spec-id}`
7. Verify: `git worktree list` clean; no `temp/{spec-id}` branch remains

#### If `feature_branch` (Exception)
1. Push feature branch: `git push -u origin feature-{spec-id}`
2. Keep worktree for continued work
3. Create PR and proceed with review; cleanup after merge

**Approval Gate** (when `feature_branch` is selected):
- Prompt: "Feature branch pushed. Create PR now?"
- Confirmation: Required if you want to proceed to PR creation

**Termination**: Workflow ends after integration/push

### The 6 Research Sub-Agents

1. **Web/Ecosystem Researcher**
   - Libraries and frameworks
   - GitHub repos and issues
   - Community patterns
   - Ecosystem trends

2. **Academic/Docs Researcher**
   - Standards and RFCs
   - Official documentation
   - Academic papers
   - Canonical patterns

3. **Competitive/Market Analyst**
   - Vendor solutions
   - Alternative approaches
   - Benchmarks and comparisons
   - Market trends

4. **Feasibility/Cost Analyst**
   - Technical complexity
   - Operational costs
   - Risk assessment
   - Trade-off analysis

5. **Lead Reviewer**
   - Deduplication
   - Relevance ranking
   - Contradiction resolution
   - Citation validation

6. **Lead Synthesizer**
   - Document generation
   - Section organization
   - Findings integration
   - Markdown formatting

.

## 6. 🔄 Execution Model

### Parallel Research Pattern

**Note**: All parallel execution, review, synthesis, and main agent finalization occur within Step 3 as sub-phases, NOT as separate steps.

```
┌─────────────────────────────────┐
│   Parallel Research Execution    │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │Web │ │Docs│ │Mkt │ │Feas│   │ ← Execute in parallel
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│         Review Phase             │ ← Lead Reviewer deduplicates
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Synthesis Phase           │ ← Lead Synthesizer creates document
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Main Agent QA Phase         │ ← Final polish and validation
└─────────────────────────────────┘
```

### Parallel Execution Configuration

**Concurrency Settings**:
- **Default**: 3 parallel research agents maximum
- **Low signal**: Broaden queries and include secondary sources
- **Fallback**: 1 (sequential execution if parallel not supported)

**Shared Context** (passed to all parallel agents):
- `request` - User research request
- `context` - Additional context from user inputs

**Research Output Format** (all agents):
```yaml
finding:
  title: [descriptive title]
  url: [source URL]
  quote: [relevant excerpt]
  finding: [key insight]
  assessment: [evaluation]
  confidence: [high/medium/low]
```

**Important**:
- Review and synthesis phases execute sequentially AFTER parallel work completes
- Main agent finalization occurs within Step 3 (no approval gate)
- All phases in Step 3 are sub-phases within that single workflow step
- This is an autonomous workflow - no user approval needed until branch integration

.

## 7. 📋 Research Document Structure

The skill produces a comprehensive `research.md` with these sections:

**Note**: This is a high-level overview. For the complete section specifications with all subsections and required fields, see [sk_p__feature_research.yaml lines 217-289](../../../b_prompts/github_spec_kit/parallel_agents/sk_p__feature_research.yaml#L217-L289).

### Core Sections

**Investigation Report**
- Request summary
- Current behavior analysis
- Key findings
- Recommendations

**Architecture Analysis**
- System components
- Data flow patterns
- Integration points
- Dependencies

**Technical Specifications**
- API documentation
- Attribute reference
- Event contracts
- State management

**Implementation Guide**
- Markup requirements
- JavaScript implementation
- CSS specifications
- Configuration options

### Supporting Sections

**Constraints & Limitations**
- Platform limitations
- Security restrictions
- Performance boundaries
- Browser compatibility

**Integration Patterns**
- Third-party services
- Authentication handling
- Error management
- Retry strategies

**Testing & Debugging**
- Test strategies
- Debugging approaches
- E2E examples
- Diagnostic tools

**Performance & Security**
- Optimization tactics
- Benchmarks
- Data protection
- Spam prevention

.

## 8. 📥 Inputs & Outputs

### Inputs

#### Required Inputs
- **request**: Feature description or research goals
- **spec_folder**: Where to save research.md

### Optional Inputs
- **context**: Additional context for research
- **issues**: Known issues to investigate
- **environment**: Staging URL for live analysis
- **scope**: File scope limitations

### Outputs

### Primary Output
- **research.md**: Complete research documentation
  - Location: `[SPEC_FOLDER]/research.md`
  - Format: Structured markdown
  - Sections: 15+ comprehensive sections

### Research Findings Structure

```yaml
finding:
  title: [descriptive title]
  url: [source URL]
  quote: [relevant excerpt]
  finding: [key insight]
  assessment: [evaluation]
  confidence: [high/medium/low]
```

## Parallel Execution Details

### Concurrency Settings
- **Default**: 3 parallel agents
- **High complexity**: 2 parallel agents
- **Fallback**: Sequential execution

### Quality Controls
- Deduplication of findings
- Citation verification
- Contradiction flagging
- Completeness validation

.

## 9. ✅ Approval Gates

This workflow is **autonomous** with minimal user interaction:

| Step | Approval Prompt | Confirmation | Note |
|------|-----------------|--------------|------|
| 8 | "All checks passed. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?" | Required | Branch integration only |

**Note**: Steps 1-7 execute autonomously without approval gates. Only step 8 (branch integration) requires user confirmation

.

## 10. 🏷️ Field Handling

This workflow automatically handles empty input fields per sk_p__feature_research.yaml:

### branch_strategy
- **Required**: Yes
- **Type**: Enum [`main_temp`, `feature_branch`]
- **Options**:
  - `main_temp` (default): Temporary worktree with short-lived branch `temp/{spec-id}`; integrate immediately after research
  - `feature_branch`: Long-running feature branch `feature-{spec-id}` for PR workflow
- **Default**: `main_temp`
- **Empty Handling**: Defaults to `main_temp` if not specified
- **Controls**: Workspace setup and Step 8 integration behavior

### spec_id
- **Derived From**: spec_folder path using pattern `specs/{NNN}` or `specs/{NNN-name}`
- **Fallback**: Extract numeric portion or use timestamp if extraction fails
- **Usage**: Used to generate feature_branch_name

### feature_branch_name
- **Pattern**: `feature-{spec_id}`
- **Condition**: Only used when `branch_strategy == feature_branch`

### git_branch
- **Derived**: Based on `branch_strategy`
- **If `main_temp`**: Use `temp/{spec-id}` (e.g., `temp/003`)
- **If `feature_branch`**: Use `feature-{spec-id}` (e.g., `feature-003`)
- **Empty Handling**: Cannot be empty; derived automatically from `branch_strategy`

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
- **Skip When**: `branch_strategy == main_temp`

.

## 11. 🔗 Integration Points

### With Chrome DevTools
- Test API endpoints
- Validate approaches
- Measure performance impact
- Verify compatibility

### With SpecKit Workflow
- Research before `/speckit.specify`
- Inform technical planning
- Support implementation decisions
- Document constraints early

### With Other Skills
- **speckit-complete**: Uses research for full workflow
- **speckit-spec-plan**: Leverages research for planning

### Workflow Relationship

**⚠️ Important**: This is a **standalone research workflow**

- **Does NOT run**: `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.analyze`, or `/speckit.implement`
- **Only generates**: `research.md` documentation in spec folder
- **Purpose**: Provide research foundation before or during SpecKit workflows
- **Flexibility**: Can be used independently or as prep step for full SpecKit execution

**When to Use This vs. Complete Workflow**:

| Use speckit-feature-research | Use speckit-complete |
|------------------------------|----------------------|
| Need research only | Need full spec → implementation |
| Evaluating feasibility | Building complete feature |
| Gathering vendor options | End-to-end automated workflow |
| Creating knowledge base | Managed approval gates |

**Output Location**:
- Primary: `[SPEC_FOLDER]/research.md`
- Optional: Supplementary files in spec folder as needed

**Integration Pattern**:
1. **Before SpecKit**: Run research → Use findings in `/speckit.specify`
2. **During SpecKit**: Reference research.md in planning steps
3. **Standalone**: Use research.md as decision document without implementation

.

## 12. ⚙️ Adaptive Rules & Quality Standards

### Adaptive Rules

**Note**: For complete adaptive rule specifications, complexity scoring, and execution mode details, see [references/adaptive-rules.md](references/adaptive-rules.md).

#### Low Signal Handling
When research yields limited results:
- Broaden search queries
- Include secondary sources
- Expand to related domains
- Document gaps explicitly

#### High Uncertainty
When findings are contradictory:
- Add clarification pass
- Document conflicting sources
- Provide multiple options
- Highlight trade-offs

#### Fallback Strategy
If parallel execution fails:
- Run agents sequentially
- Maintain review/synthesis phases
- Document degraded mode
- Continue with partial results

### Quality Standards

### Documentation Requirements
- Production-ready examples
- Defensive programming patterns
- Error handling strategies
- Memory leak prevention
- SPA compatibility

### Code Examples
- Working snippets
- Proper error handling
- Performance optimized
- Accessibility compliant
- Browser compatible

### Analysis Depth
- Edge cases covered
- Failure modes documented
- Recovery strategies defined
- Monitoring approaches specified
- Source attribution present

.

## 13. ⚡ Performance Characteristics

**Note**: Performance varies based on research scope, available sources, and system resources.

- **Execution**: Variable based on research depth and source availability
- **Parallel phase**: Multiple researchers execute concurrently
- **Review/synthesis**: Sequential refinement after parallel collection
- **Document generation**: Comprehensive markdown output
- **Output size**: 50-150KB markdown (typical)

.

## 14. 🚨 Error Handling

### Retry Policy
- **Max retries**: 2 per agent
- **Backoff**: Exponential
- **Targeted**: Only failed agents

### Recovery Actions
- Use cached results if available
- Continue with partial findings
- Document missing research areas
- Provide fallback recommendations

.

## 14. ⚠️ Limitations

- **Research scope**: Technical/implementation focus
- **Sources**: Public information only
- **Language**: English sources primarily
- **Real-time**: No live system monitoring
- **Dependencies**: Requires internet access

.

## 15. 📈 Success Metrics

**Note**: Target quality benchmarks for research completeness and accuracy.

- **Coverage**: >80% of research areas
- **Citations**: >20 validated sources
- **Contradictions**: <10% unresolved
- **Completeness**: All sections populated
- **Quality score**: >85% validation pass