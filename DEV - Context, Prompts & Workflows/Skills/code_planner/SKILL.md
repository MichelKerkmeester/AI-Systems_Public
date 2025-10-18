---
name: code_planner
description: Create comprehensive project plans using 5 parallel autonomous planning agents (Scope, Breakdown, Resource, Timeline, Quality). Deploys agents simultaneously, reviews outputs, resolves conflicts, and synthesizes into single consolidated plan. Use for project planning, feature breakdown, timeline estimation, and resource allocation.
---

# Code Planner

Strategic planning through parallel agent orchestration - deploy 5 specialized planners, review outputs, synthesize into unified plan.

## When to Use This Skill

**Use this skill when**:
- Need comprehensive project plan
- Breaking down complex features
- Estimating timeline and resources
- Identifying risks and dependencies
- Planning multi-phase projects
- Want detailed scope analysis
- Need resource allocation planning

**Do NOT use this skill for**:
- Simple single-file changes
- Quick bug fixes
- Documentation-only updates
- Trivial tasks (<1 hour)
- Already have detailed plan

## How It Works

This skill orchestrates 5 autonomous planning agents running in parallel, each specializing in a different aspect of planning:

1. **Scope Analyst** - Defines boundaries and success criteria
2. **Task Decomposer** - Breaks down phases and tasks
3. **Resource Analyst** - Identifies requirements and dependencies
4. **Timeline Estimator** - Estimates durations and sequencing
5. **Quality Validator** - Validates completeness and identifies risks

**Workflow**: Initialize → Deploy 5 Agents (Parallel) → Review Outputs → Synthesize Plan

**Output**: Single consolidated `plan-[slug]-[timestamp].md` file

## Inputs

### Required Inputs

**Request**:
- **Description**: What needs to be planned
- **Format**: Natural language description
- **Examples**:
  - "Plan implementation of user authentication system"
  - "Break down e-commerce checkout flow"
  - "Create timeline for API migration"

### Optional Inputs

**Target Folder**:
- **Type**: Directory path
- **Purpose**: Where to write plan file
- **Default**: `/specs` if empty
- **Example**: `/specs/auth-system/`

**Context**:
- **Type**: Text
- **Purpose**: Additional background information
- **Default**: Inferred from request
- **Example**: "Existing system uses JWT, need to migrate to OAuth2"

**Complexity**:
- **Type**: Enum [`quick`, `standard`, `deep`]
- **Purpose**: Controls number of agents and depth
- **Default**: `standard`
- **Options**:
  - `quick`: 3 agents (Scope, Breakdown, Timeline), light review
  - `standard`: 5 agents (all), comprehensive review
  - `deep`: 6 agents (adds Compliance), exhaustive review, +30% timeline buffer

## Knowledge References

**Output Documentation Standard**:

### Document Style Guide
**Location**: `knowledge/document_style_guide.md`
**Purpose**: Standard format for all markdown documents including plan outputs

**Plan Output Requirements**:
- **H1 Format**: `# Project Plan: [Name]` (title with descriptive subtitle)
- **H2 Format**: `## 1. 📄 Section Name` (numbered with appropriate emoji)
- **H3 Format**: `### 1.1 Subsection` (decimal numbering for subsections)
- **Section Separators**: Use single `.` on own line between major sections
- **Table of Contents**: Include with anchor links at top
- **Writing Style**: Concise, technical, actionable (present tense, imperative mood)

**Required Plan Sections** (following style guide):
1. 📋 Executive Summary
2. 🎯 Scope & Boundaries
3. 📦 Phase Breakdown
4. 🛠️ Resource Requirements
5. ⏱️ Timeline Overview
6. 🔒 Risk Matrix
7. ✅ Success Metrics
8. 🚀 Next Actions

**Note**: Synthesized plan.md files automatically follow this structure as defined in workflow Step 4.

---

## Workflow

### Step 1: Initialization

**Purpose**: Validate inputs and prepare agent deployment

**Actions**:
1. Parse and validate all inputs
2. Apply defaults for empty fields
3. Determine complexity level
4. Configure agent selection
5. Generate plan filename
6. Verify target folder accessible

**Validation**:
- [ ] Request not empty
- [ ] Target folder exists or can be created
- [ ] Complexity value valid
- [ ] Inputs normalized

**Outputs**:
- Normalized inputs
- Agent configuration (3, 5, or 6 agents)
- Plan filename: `[TARGET_FOLDER]/plan-[slug]-[YYYYMMDD-HHMMSS].md`

---

### Step 2: Parallel Planning Deployment

**Purpose**: Deploy specialized agents to analyze from multiple perspectives

**Execution**: All agents run simultaneously in parallel

**Shared Context** (provided to all agents):
- Original request
- Additional context
- Target folder location
- Complexity level

**Agents Deployed**:

#### 1. Scope Analyst
**Focus**: Objectives, boundaries, success criteria, constraints
**Output Sections**:
- Objectives: What we're trying to achieve
- Boundaries: What's in scope vs. out of scope
- Success Criteria: How we measure success
- Constraints: Limitations and dependencies

#### 2. Task Decomposer
**Focus**: Phases, tasks, dependencies, milestones
**Output Sections**:
- Phases: High-level project stages
- Tasks per Phase: Detailed breakdown
- Dependencies: Task relationships
- Milestones: Key checkpoints

#### 3. Resource Analyst
**Focus**: Tools, skills, external dependencies, blockers
**Output Sections**:
- Required Tools: Technologies and platforms needed
- Required Skills: Team capabilities required
- External Dependencies: Third-party services or APIs
- Potential Blockers: Known impediments

#### 4. Timeline Estimator
**Focus**: Durations, sequencing, critical path, buffer
**Complexity Scaling**:
- Quick: Minimal estimates (rough ranges)
- Standard: Balanced estimates (realistic ranges)
- Deep: Detailed estimates (precise ranges with contingency)
**Output Sections**:
- Duration Estimates: Time required per task/phase
- Task Sequencing: Order of execution
- Critical Path: Tasks that can't be delayed
- Buffer Allocation: Contingency time (30% for deep complexity)

#### 5. Quality Validator
**Focus**: Completeness, feasibility, risks, gaps
**Output Sections**:
- Completeness Check: Are all aspects covered?
- Feasibility Assessment: Is plan realistic?
- Risk Matrix: Identified risks with severity
- Identified Gaps: Missing information or unknowns

**Validation**: `all_agents_completed_successfully`

---

### Step 3: Review & Analysis

**Purpose**: Comprehensive review of all agent outputs

**Reviewer Role**: Meta-planner synthesizing multiple perspectives

**Review Focus**:
- Identify overlaps and complementary elements
- Resolve conflicts between agent plans
- Validate internal consistency
- Assess overall completeness
- Flag risks, gaps, or concerns
- Identify integration points
- Note contradictions or tensions
- Evaluate feasibility holistically

**Review Process**:
1. Read all 5 agent outputs
2. Create cross-agent analysis
3. Identify conflicts (e.g., timeline vs. resources)
4. Document resolution strategy
5. Note missing elements
6. Assess overall quality

**Review Deliverable**: Comprehensive synthesis guidance document

**Validation**: `review_completed_with_insights`

---

### Step 4: Synthesis & Finalization

**Purpose**: Create single consolidated plan from all inputs

**Synthesis Process**:
1. Aggregate all 5 agent native plans
2. Apply review insights and resolutions
3. Integrate complementary elements
4. Resolve conflicts per review guidance
5. Apply priority tags (P0 critical → P3 nice-to-have)
6. Structure into unified markdown
7. Validate against checklist
8. Write single file
9. Display summary

**Validation Checklist**:
- [ ] All 5 agents completed native planning
- [ ] Review step completed
- [ ] Minimum 3 phases (unless trivial)
- [ ] All tasks have owner, effort, success criteria
- [ ] Dependencies are acyclic (no circular deps)
- [ ] Timeline has buffer allocation
- [ ] Risks identified with severity levels
- [ ] Success metrics measurable
- [ ] Filename convention followed
- [ ] Markdown syntax valid
- [ ] Single file output confirmed

**Output Markdown Structure**:
```markdown
# Project Plan: [Name]

## Executive Summary
[High-level overview from Scope Analyst]

## Scope & Boundaries
[Detailed scope from Scope Analyst]

## Phase Breakdown
[Phases and tasks from Task Decomposer]

## Resource Requirements
[Tools, skills, dependencies from Resource Analyst]

## Timeline Overview
[Durations, sequencing, milestones from Timeline Estimator]

## Risk Matrix
[Risks and mitigations from Quality Validator]

## Success Metrics
[Measurable success criteria]

## Next Actions
[Immediate next steps synthesized from all agents]

## Plan Metadata
[Synthesis timestamp, agents used, complexity level, confidence]
```

**Final Output**: `[TARGET_FOLDER]/plan-[slug]-[timestamp].md`

**Validation**: `plan_complete_and_validated`

---

## Complexity Levels

### Quick (3 Agents)
**When to Use**: Simple features, rough estimates needed fast
**Agents**: Scope Analyst, Task Decomposer, Timeline Estimator
**Review Depth**: Light (identify major conflicts only)
**Timeline**: Minimal estimates with broad ranges
**Phases**: 1-3 phases expected

### Standard (5 Agents) - Default
**When to Use**: Most projects, balanced detail and speed
**Agents**: All 5 (Scope, Breakdown, Resource, Timeline, Quality)
**Review Depth**: Comprehensive (resolve all conflicts)
**Timeline**: Balanced estimates with realistic ranges
**Phases**: 3-7 phases expected

### Deep (6 Agents)
**When to Use**: Complex projects, high stakes, need exhaustive analysis
**Agents**: All 5 + Compliance Analyst (regulatory/policy review)
**Review Depth**: Exhaustive (validate every assumption)
**Timeline**: Detailed ranges with +30% buffer added automatically
**Phases**: 7+ phases expected

## Error Handling

### Agent Failure
**Action**: Retry with simplified scope
**Fallback**: Note limitation in quality section
**Max Retries**: 2
**Impact**: Proceed with available outputs (if ≥50% agents complete)

### Review Identifies Critical Gap
**Action**: Return to specific agent for re-planning
**Max Iterations**: 2
**Fallback**: Document gap in plan warnings section

### Validation Failure
**Action**: Return to synthesis with corrections
**Max Iterations**: 2
**Fallback**: Generate with warnings section noting issues

### File Write Failure
**Action**: Check folder permissions
**Fallback**: Offer stdout output or alternate location

## Output Format

**Primary Deliverable**:
- **Location**: `[TARGET_FOLDER]/plan-[slug]-[timestamp].md`
- **Format**: Markdown with headers, checklists, tables
- **Size**: Typically 500-2000 lines depending on complexity

**Sections** (8 required):
1. Executive Summary
2. Scope & Boundaries
3. Phase Breakdown with Tasks
4. Resource Requirements
5. Timeline with Milestones
6. Risk Matrix and Mitigations
7. Success Metrics
8. Immediate Next Actions

**Formatting Standards**:
- Tasks as checklists: `- [ ] Task name`
- Risks as tables: `| Risk | Severity | Mitigation |`
- Timeline as Gantt approximation (text-based)
- Priority tags: P0 (critical) → P3 (nice-to-have)

**Metadata Included**:
- Synthesis timestamp
- Agent outputs referenced
- Complexity level used
- Confidence assessment

## Rules

### ALWAYS
- Deploy all agents (3, 5, or 6) in parallel
- Allow agents full autonomy in their planning
- Review all agent outputs comprehensively before synthesis
- Create single consolidated markdown file (not multiple files)
- Validate folder path before write
- Include measurable success criteria
- Identify dependencies explicitly
- Allocate timeline buffer (especially for deep complexity)
- Generate plan filename with timestamp
- Enforce review step before synthesis

### NEVER
- Skip agent execution to save time
- Skip review step (critical for conflict resolution)
- Create multiple output files (must be single file)
- Constrain agent planning autonomy
- Create circular dependencies
- Omit risk assessment
- Write to unvalidated paths

## Quality Standards

**Completeness Criteria**:
- All agents completed successfully (or ≥50% with noted gaps)
- Review identified and resolved conflicts
- Synthesis covers all critical aspects
- No circular dependencies
- Timeline is realistic with buffer

**Validation Requirements**:
- Phases: Minimum 3 unless project is trivial
- Tasks: All have owner and effort estimate
- Dependencies: Clearly defined and acyclic
- Risks: Assessed with severity and mitigation
- Success Metrics: Measurable and achievable
- Timeline: Includes 30% buffer for uncertainties
- Resources: Identified and assessed for availability

## Bundled Resources

### References

**`references/adaptive-rules.md`** (~500 lines):
- **Purpose**: Comprehensive complexity assessment and agent configuration strategies
- **When to Load**: When determining complexity level or adapting agent deployment
- **Contents**:
  - Complexity scoring methodology (Scope, Duration, Dependencies, Team, Risk factors)
  - Configuration per complexity level (quick/standard/deep)
  - Agent selection rules and priority ranking
  - Review depth adaptation strategies
  - Timeline buffer allocation rules
  - Fallback strategies for agent failures
  - Quality gates per complexity level
  - Real-world adaptation examples

**`references/parallel-stages.md`** (~400 lines):
- **Purpose**: Orchestration patterns for parallel agent execution, review, and synthesis
- **When to Load**: When understanding workflow orchestration or debugging stage transitions
- **Contents**:
  - Parallel execution patterns (5 agents simultaneously)
  - Review & analysis process (conflict identification, resolution strategies)
  - Synthesis process (aggregation, integration, validation)
  - Coordination patterns (agent independence, review as integration layer)
  - Performance optimization (concurrency control, timeout management, retry strategy)
  - Quality metrics and monitoring
  - Best practices for stage transitions

**`references/sub-agents.md`** (~600 lines):
- **Purpose**: Detailed specifications for all 5 planning agents
- **When to Load**: When understanding agent capabilities or customizing agent prompts
- **Contents**:
  - Complete specifications for each agent:
    1. Scope Analyst (objectives, boundaries, success criteria, constraints)
    2. Task Decomposer (phases, tasks, dependencies, milestones)
    3. Resource Analyst (tools, skills, dependencies, blockers)
    4. Timeline Estimator (durations, sequencing, critical path, buffer)
    5. Quality Validator (completeness, feasibility, risks, gaps)
  - Agent communication protocol
  - Expected output formats and templates
  - Success criteria per agent
  - Error handling strategies per agent
  - Quality standards and best practices

---

## Version Information

**Current Version**: 1.0.0
**Created**: 2025-10-18
**Based On**: `code_plan.yaml`
**Architecture**: Parallel agent orchestration (5 specialized planners)
**Compatible With**: Native Plan mode, Claude Code workflows

---

## Planning Philosophy

**Core Principle**: "Multiple perspectives create better plans"

By deploying 5 specialized planning agents simultaneously, this skill ensures:

- **Comprehensive Coverage**: Each agent focuses on their specialty
- **Conflict Identification**: Review phase catches contradictions
- **Balanced Plans**: Synthesis integrates all perspectives
- **Reduced Blind Spots**: Multiple viewpoints reduce oversight
- **Quality Assurance**: Dedicated validator ensures completeness

The result is a thorough, realistic, actionable plan validated from multiple angles.
