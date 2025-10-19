# Adaptive Planning Rules

Rules and strategies for adapting planning complexity and agent deployment based on project characteristics.

## Complexity Assessment

### Factors to Consider

**Project Scope**:
- **Narrow** (<10 files affected): Single feature or component
- **Moderate** (10-30 files): Feature set or subsystem
- **Broad** (>30 files): Full system or major architecture change

**Duration Estimate**:
- **Short** (<1 week): Quick enhancement
- **Medium** (1-4 weeks): Standard feature
- **Long** (>4 weeks): Major initiative

**Dependencies**:
- **Few** (<3): Mostly self-contained
- **Moderate** (3-7): Some integration points
- **Many** (>7): Highly integrated

**Team Size**:
- **Solo** (1 person): Individual work
- **Small** (2-3): Pair or small team
- **Large** (>3): Coordinated team effort

**Risk Level**:
- **Low**: Well-understood domain, existing patterns
- **Medium**: Some unknowns, moderate technical challenge
- **High**: Novel approach, significant uncertainty

### Complexity Scoring

```
Score = (Scope × 3) + (Duration × 2) + (Dependencies × 2) + (Team × 1) + (Risk × 2)

Where: Narrow/Short/Few/Solo/Low = 1, Moderate/Medium = 2, Broad/Long/Many/Large/High = 3

Result:
- 10-15: Quick complexity
- 16-25: Standard complexity
- 26-30: Deep complexity
```

---

## Complexity-Based Configuration

### Quick Complexity (Score 10-15)

**Characteristics**: Simple feature, short timeline, few dependencies

**Agent Configuration**:
- **Agents Used**: 3 (Scope, Breakdown, Timeline)
- **Agents Skipped**: Resource, Quality (assumed manageable)

**Review Depth**: Light
- Identify major conflicts only
- Quick consistency check
- 5-10 minute review

**Timeline Approach**: Minimal estimates
- Rough ranges (1-2 days, 3-5 days)
- No detailed breakdown
- No buffer allocation

**Output Expectations**:
- 1-3 phases
- 10-20 tasks total
- Basic risk identification
- 200-500 line plan

---

### Standard Complexity (Score 16-25) - Default

**Characteristics**: Typical feature, moderate timeline, some integration

**Agent Configuration**:
- **Agents Used**: 5 (Scope, Breakdown, Resource, Timeline, Quality)
- **All agents deployed**

**Review Depth**: Comprehensive
- Resolve all conflicts
- Validate consistency across all agents
- Check completeness
- 15-20 minute review

**Timeline Approach**: Balanced estimates
- Realistic ranges (2-3 days, 1-2 weeks)
- Task-level estimates
- Basic buffer (10-15%)

**Output Expectations**:
- 3-7 phases
- 30-60 tasks total
- Detailed risk matrix
- 500-1500 line plan

---

### Deep Complexity (Score 26-30)

**Characteristics**: Complex project, long timeline, high integration, significant risk

**Agent Configuration**:
- **Agents Used**: 6 (Scope, Breakdown, Resource, Timeline, Quality, Compliance)
- **Compliance Agent Added**: Regulatory, policy, security review

**Review Depth**: Exhaustive
- Validate every assumption
- Multi-pass review
- Challenge feasibility
- Document all uncertainties
- 30-40 minute review

**Timeline Approach**: Detailed ranges with contingency
- Precise estimates (2-3 days best case, 5-7 days worst case)
- Task and subtask breakdown
- Automatic +30% buffer added
- Contingency planning

**Output Expectations**:
- 7+ phases
- 80-150+ tasks
- Comprehensive risk analysis with probability × impact scoring
- 1500-3000 line plan

---

## Agent Selection Rules

### When to Skip Agents

**Resource Analyst can be skipped if**:
- Project uses only existing, well-understood tools
- No external dependencies
- All required skills available on team
- No blocking concerns

**Quality Validator can be skipped if**:
- Simple, low-risk change
- Well-established pattern
- Short duration (<1 week)
- Easy to validate

**Compliance Analyst only added if**:
- Regulatory requirements (GDPR, HIPAA, etc.)
- Security-critical changes (auth, encryption)
- Policy enforcement needed
- Audit trail required

### Agent Priority Ranking

**Always Include** (Critical):
1. Scope Analyst - Defines what we're doing
2. Task Decomposer - Breaks down the work

**High Priority** (Standard+):
3. Timeline Estimator - Essential for scheduling
4. Resource Analyst - Identifies dependencies and skills
5. Quality Validator - Catches issues early

**Optional** (Deep only):
6. Compliance Analyst - Regulatory/policy specific

---

## Review Depth Adaptation

### Light Review (Quick)

**Time**: 5-10 minutes

**Focus**:
- Major contradictions only
- Basic consistency
- Obvious gaps

**Process**:
- Scan all outputs quickly
- Flag critical conflicts
- Document 2-3 key insights
- Proceed to synthesis

---

### Comprehensive Review (Standard)

**Time**: 15-20 minutes

**Focus**:
- Resolve all conflicts
- Validate consistency
- Check completeness
- Identify integration points

**Process**:
- Read all outputs carefully
- Create conflict matrix
- Document resolution strategy
- Validate assumptions
- Note risks and gaps
- Provide synthesis guidance

---

### Exhaustive Review (Deep)

**Time**: 30-40 minutes

**Focus**:
- Validate every assumption
- Challenge feasibility
- Stress-test estimates
- Document all uncertainties
- Multi-pass analysis

**Process**:
- Read all outputs thoroughly
- Cross-validate between agents
- Create detailed conflict analysis
- Challenge optimistic estimates
- Identify hidden dependencies
- Document counter-evidence
- Provide comprehensive synthesis guidance
- Flag high-risk areas requiring validation

---

## Timeline Buffer Rules

### No Buffer (Quick)
- Use minimal estimates as-is
- Assume best-case scenarios
- Acceptable for low-risk, short duration

### Basic Buffer (Standard)
- Add 10-15% contingency
- Round up task estimates
- Include slack between phases

### Contingency Buffer (Deep)
- Automatic +30% buffer
- Range estimates (best/worst case)
- Phase-level contingency
- Critical path analysis with float

---

## Fallback Strategies

### Agent Failure Handling

**If 1 agent fails**:
- Retry with simplified prompt
- If retry fails, proceed without that agent
- Note limitation in quality section
- Reduce confidence rating

**If 2+ agents fail**:
- Reduce complexity level automatically
- Quick → Manual planning recommended
- Standard → Downgrade to Quick (3 agents)
- Deep → Downgrade to Standard (5 agents)

### Review Identifies Critical Gap

**Action**:
1. Identify which agent's output has gap
2. Re-run that specific agent with additional context
3. Re-review focused on that area
4. Integrate revised output
5. Max 2 iterations to prevent loops

**Examples**:
- Timeline unrealistic → Re-run Timeline Estimator with more conservative estimates
- Missing dependencies → Re-run Resource Analyst with deeper analysis
- Scope unclear → Re-run Scope Analyst with clarifying questions

---

## Quality Gates

### Quick Complexity Gates
- [ ] Scope defined
- [ ] Tasks identified
- [ ] Timeline estimated
- [ ] Basic risks noted

### Standard Complexity Gates
- [ ] All 5 agents completed
- [ ] Review resolved conflicts
- [ ] Dependencies mapped
- [ ] Risks assessed with severity
- [ ] Timeline has buffer
- [ ] Success criteria measurable

### Deep Complexity Gates
- [ ] All 6 agents completed
- [ ] Exhaustive review completed
- [ ] All assumptions validated
- [ ] Risks have probability × impact scores
- [ ] Timeline has +30% buffer
- [ ] Compliance checked
- [ ] Contingency plans documented

---

## Adaptation Examples

### Example 1: Simple Bug Fix

**Assessment**:
- Scope: Narrow (2 files)
- Duration: Short (4 hours)
- Dependencies: Few (none)
- Risk: Low

**Score**: 10 → **Quick Complexity**

**Configuration**:
- 3 agents (Scope, Breakdown, Timeline)
- Light review
- Minimal estimates
- No buffer

---

### Example 2: Feature Implementation

**Assessment**:
- Scope: Moderate (15 files)
- Duration: Medium (2 weeks)
- Dependencies: Moderate (API integration)
- Risk: Medium

**Score**: 20 → **Standard Complexity**

**Configuration**:
- 5 agents (all standard)
- Comprehensive review
- Balanced estimates
- 15% buffer

---

### Example 3: System Migration

**Assessment**:
- Scope: Broad (50+ files)
- Duration: Long (2 months)
- Dependencies: Many (10+ services)
- Risk: High

**Score**: 28 → **Deep Complexity**

**Configuration**:
- 6 agents (adds Compliance)
- Exhaustive review
- Detailed ranges with contingency
- +30% buffer
- Multi-pass validation

---

## Quick Reference Matrix

| Complexity | Agents | Review Time | Buffer | Plan Size |
|-----------|--------|-------------|--------|-----------|
| Quick | 3 | 5-10 min | None | 200-500 lines |
| Standard | 5 | 15-20 min | 10-15% | 500-1500 lines |
| Deep | 6 | 30-40 min | +30% | 1500-3000 lines |

---

## Best Practices

**DO**:
- Assess complexity before starting
- Use Standard as default unless clear reason
- Upgrade to Deep for high-risk projects
- Downgrade to Quick only for trivial changes
- Add buffer for uncertainties

**DON'T**:
- Use Quick for anything >1 week
- Skip review step to save time
- Ignore agent failures
- Assume best-case timelines
- Skip buffer allocation

**CONSIDER**:
- User's risk tolerance
- Team's planning experience
- Project's strategic importance
- Available time for planning
- Consequences of underestimation
