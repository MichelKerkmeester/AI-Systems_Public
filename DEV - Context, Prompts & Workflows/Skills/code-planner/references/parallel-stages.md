# Parallel Planning Orchestration

Detailed patterns for orchestrating 5 parallel planning agents, reviewing outputs, and synthesizing unified plans.

## Stage Overview

The planning workflow has 3 major stages:
1. **Parallel Planning** - 5 agents work simultaneously
2. **Review & Analysis** - Meta-planner reviews all outputs
3. **Synthesis** - Create single consolidated plan

---

## Stage 1: Parallel Planning Execution

### Execution Pattern

```
T0: Launch all agents simultaneously
    ├─ Scope Analyst: START
    ├─ Task Decomposer: START
    ├─ Resource Analyst: START
    ├─ Timeline Estimator: START
    └─ Quality Validator: START

T1-T5: Agents work independently
    ├─ Scope → Analyzing objectives...
    ├─ Breakdown → Decomposing phases...
    ├─ Resource → Identifying dependencies...
    ├─ Timeline → Estimating durations...
    └─ Quality → Validating feasibility...

T6: Collect outputs
    ├─ Scope: ✓ (scope_output.md)
    ├─ Breakdown: ✓ (breakdown_output.md)
    ├─ Resource: ✓ (resource_output.md)
    ├─ Timeline: ✓ (timeline_output.md)
    └─ Quality: ✓ (quality_output.md)
```

**Concurrency**: Maximum 5 agents simultaneously
**Timeout**: 60 seconds per agent (with retry)
**Minimum Viable**: 3/5 agents must complete (Scope, Breakdown, Timeline)

### Shared Context Distribution

All agents receive:
```yaml
shared_context:
  request: "[Original planning request]"
  context: "[Additional background]"
  target_folder: "[Output location]"
  complexity: "[quick|standard|deep]"
```

### Agent Output Format

Each agent returns structured markdown:
```markdown
# [Agent Name] Output

## [Section 1]
[Content]

## [Section 2]
[Content]

## Key Insights
- [Insight 1]
- [Insight 2]

## Confidence Level
[High|Medium|Low] with reasoning
```

### Error Handling During Parallel Execution

**Single Agent Failure**:
1. Retry once with simplified prompt
2. If retry fails, note failure
3. Continue with remaining agents
4. Flag incomplete analysis in review

**Multiple Agent Failures (≥2)**:
1. Assess which agents failed
2. If critical agents (Scope, Breakdown) failed → Abort
3. If non-critical failed → Continue with warnings
4. Document limitations in quality section

---

## Stage 2: Review & Analysis

### Review Process

**Reviewer Role**: Meta-planner with bird's-eye view

**Step 1: Initial Pass** (5 minutes)
- Read all agent outputs quickly
- Note overall themes
- Identify obvious conflicts

**Step 2: Deep Analysis** (10-15 minutes)
- Cross-validate outputs
- Create conflict matrix
- Map integration points
- Assess completeness

**Step 3: Resolution Strategy** (5 minutes)
- Document how to resolve conflicts
- Note areas requiring synthesis judgment
- Provide guidance for final plan

### Conflict Identification Patterns

**Timeline vs. Resource Conflicts**:
```
Timeline says: "2 weeks with 1 developer"
Resource says: "Requires 2 senior devs + designer"

Resolution: Adjust timeline or scope
```

**Scope vs. Quality Conflicts**:
```
Scope says: "Include features A, B, C, D"
Quality says: "Feature D is high risk, not feasible in timeline"

Resolution: Make feature D phase 2, or increase timeline
```

**Breakdown vs. Timeline Conflicts**:
```
Breakdown identifies: 45 tasks
Timeline estimates: 30 days total
Math: 45 tasks ÷ 30 days = 1.5 tasks/day (unrealistic)

Resolution: Increase timeline or reduce tasks
```

### Review Deliverable Structure

```markdown
# Meta-Planning Review

## Executive Assessment
[Overall quality and completeness assessment]

## Cross-Agent Analysis

### Complementary Elements
[Where agents reinforce each other]

### Conflicts Identified
1. [Conflict 1: Description + Resolution strategy]
2. [Conflict 2: Description + Resolution strategy]

### Integration Points
[How outputs should be combined]

### Gaps Identified
[Missing information or areas needing attention]

## Synthesis Guidance

### Priority 1 (Critical)
- [Guidance 1]

### Priority 2 (Important)
- [Guidance 2]

### Priority 3 (Nice-to-have)
- [Guidance 3]

## Confidence Assessment
[Overall confidence in plan feasibility]
```

---

## Stage 3: Synthesis

### Synthesis Process

**Step 1: Aggregate** (5 minutes)
- Collect all agent outputs
- Apply review guidance
- Create outline structure

**Step 2: Integrate** (10-15 minutes)
- Combine complementary elements
- Resolve conflicts per review guidance
- Fill gaps with reasoned assumptions
- Apply priority tags (P0-P3)

**Step 3: Structure** (5 minutes)
- Organize into standard sections
- Format consistently
- Add metadata
- Validate against checklist

**Step 4: Finalize** (5 minutes)
- Write to file
- Generate summary
- Display completion message

### Conflict Resolution Strategies

**Strategy 1: Conservative Approach**
- When Timeline vs. Scope conflict: Extend timeline
- When Resource vs. Scope conflict: Add resources or reduce scope
- Default to feasibility over ambition

**Strategy 2: Phased Approach**
- Split conflicting features into phases
- Phase 1: Core functionality (high confidence)
- Phase 2: Additional features (lower confidence)

**Strategy 3: Risk Mitigation**
- If Quality flags high risk: Add contingency
- If Timeline is tight: Add buffer
- If Resources uncertain: Identify alternatives

### Priority Tagging Rules

**P0 (Critical)**:
- Core functionality
- Required for success criteria
- Blocking other work
- No alternative available

**P1 (High)**:
- Important features
- Significantly impacts value
- Dependency for other work
- Difficult to add later

**P2 (Medium)**:
- Nice-to-have features
- Incremental value
- Can be added later
- No dependencies

**P3 (Low)**:
- Future considerations
- Minimal immediate value
- Easy to add later
- No urgency

### Output Validation Checklist

**Structure Validation**:
- [ ] All 8 required sections present
- [ ] Markdown syntax valid
- [ ] Headers properly nested
- [ ] Lists formatted correctly
- [ ] Tables properly structured

**Content Validation**:
- [ ] Executive summary clear and concise
- [ ] Scope boundaries explicit
- [ ] Phases logically sequenced
- [ ] Tasks have owners and estimates
- [ ] Dependencies clearly defined
- [ ] Timeline includes buffer
- [ ] Risks have severity ratings
- [ ] Success metrics measurable
- [ ] Next actions specific

**Quality Validation**:
- [ ] No circular dependencies
- [ ] Estimates seem realistic
- [ ] Risks acknowledged
- [ ] Assumptions documented
- [ ] Confidence level stated

---

## Coordination Patterns

### Agent Independence

**Principle**: Agents work autonomously without coordination

**Benefits**:
- Faster execution (true parallelism)
- Diverse perspectives (no groupthink)
- Each agent goes deep in their area

**Trade-offs**:
- Potential conflicts (resolved in review)
- Some overlap (deduplicated in synthesis)
- Requires strong review phase

### Review as Integration Layer

**Principle**: Review resolves conflicts and provides integration guidance

**Review Outputs Used in Synthesis**:
- Conflict resolution strategies
- Integration points mapping
- Gap filling guidance
- Priority recommendations
- Confidence assessments

### Synthesis as Unification

**Principle**: One voice, one plan, multiple perspectives integrated

**Synthesis Techniques**:
- **Merge**: Combine complementary elements
- **Choose**: Select best option when conflicting
- **Bridge**: Create transition when both needed
- **Phase**: Split into stages when both valid but incompatible

---

## Performance Optimization

### Concurrency Control

```yaml
concurrency_limits:
  default: 5 agents
  fallback: 3 agents (if 2 fail)
  minimum: 2 agents (Scope + Breakdown)
```

### Timeout Management

```yaml
timeouts:
  per_agent: 60 seconds
  total_parallel_stage: 5 minutes
  review_stage: 20 minutes
  synthesis_stage: 20 minutes
  total_workflow: 45 minutes maximum
```

### Retry Strategy

```yaml
retry_policy:
  max_retries: 1 per agent
  retry_delay: 5 seconds
  simplified_prompt: true
  fallback: continue_without_agent
```

---

## Quality Metrics

### Stage Success Criteria

**Parallel Planning Success**:
- ≥80% agents completed (4/5 or 5/5)
- All critical agents completed (Scope, Breakdown, Timeline)
- Outputs meet format requirements
- Confidence levels stated

**Review Success**:
- All outputs read and analyzed
- Conflicts identified and resolution strategies documented
- Integration guidance provided
- Completeness assessed

**Synthesis Success**:
- Single file output created
- All required sections present
- Validation checklist passed
- Metadata included

### Overall Plan Quality

**High Quality Plan** (90%+ score):
- All agents completed
- Comprehensive review
- All conflicts resolved
- No critical gaps
- High confidence

**Medium Quality Plan** (70-89% score):
- Most agents completed
- Standard review
- Major conflicts resolved
- Minor gaps noted
- Medium confidence

**Acceptable Plan** (50-69% score):
- Minimum agents completed
- Basic review
- Critical conflicts resolved
- Gaps documented
- Lower confidence with caveats

---

## Monitoring & Telemetry

### Tracked Metrics

**Agent Metrics**:
- Completion rate per agent
- Average execution time per agent
- Retry rate
- Output quality scores

**Review Metrics**:
- Conflicts identified count
- Resolution rate
- Review duration
- Completeness score

**Synthesis Metrics**:
- Final plan size
- Sections completed
- Validation pass rate
- Time to completion

---

## Best Practices

**DO**:
- Run all agents in parallel (don't sequence)
- Allow agents full autonomy
- Conduct thorough review before synthesis
- Resolve conflicts explicitly
- Document assumptions and confidence
- Validate output before finalizing

**DON'T**:
- Skip agents to save time
- Constrain agent creativity
- Rush review phase
- Ignore conflicts
- Assume best-case scenarios
- Proceed without validation

**CONSIDER**:
- Agent failure impact on plan quality
- Conflict resolution trade-offs
- Buffer allocation adequacy
- Risk assessment completeness
- Success criteria measurability
