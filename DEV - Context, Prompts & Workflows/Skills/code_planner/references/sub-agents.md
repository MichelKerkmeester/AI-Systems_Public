# Planning Sub-Agents Specifications

Detailed specifications for the 5 specialized planning agents.

## Agent 1: Scope Analyst

**Role**: Define project boundaries and success criteria

**Focus Areas**:
- Objectives: What we're trying to achieve
- Boundaries: What's in/out of scope
- Success Criteria: How we measure success
- Constraints: Limitations and dependencies

**Analysis Approach**:
1. Parse request for goals and requirements
2. Identify explicit and implicit objectives
3. Define clear boundaries (what's included, what's excluded)
4. Establish measurable success criteria
5. Document constraints (time, budget, technical, regulatory)

**Output Structure**:
```markdown
# Scope Analysis

## Objectives
### Primary Objectives
- [Objective 1]
- [Objective 2]

### Secondary Objectives
- [Objective 3]

## Boundaries

### In Scope
- [What's included]

### Out of Scope
- [What's explicitly excluded]

### Assumptions
- [What we're assuming]

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]

## Constraints
- **Technical**: [Technology limitations]
- **Resource**: [Budget, team size]
- **Timeline**: [Deadlines]
- **Regulatory**: [Compliance requirements]

## Confidence Level
[High|Medium|Low] - [Reasoning]
```

**Quality Criteria**:
- Objectives are specific and actionable
- Boundaries are clearly defined
- Success criteria are measurable
- Constraints are documented
- Assumptions are explicit

---

## Agent 2: Task Decomposer

**Role**: Break down project into phases and tasks

**Focus Areas**:
- Phases: High-level project stages
- Tasks per Phase: Detailed breakdown
- Dependencies: Task relationships
- Milestones: Key checkpoints

**Decomposition Approach**:
1. Identify logical phases (design, build, test, deploy)
2. Break each phase into tasks
3. Define task dependencies (what blocks what)
4. Establish milestones (completion markers)
5. Validate no circular dependencies

**Output Structure**:
```markdown
# Task Breakdown

## Phase Overview
1. [Phase 1]: [Description]
2. [Phase 2]: [Description]
3. [Phase 3]: [Description]

## Detailed Breakdown

### Phase 1: [Name]
**Duration**: [Estimate]
**Dependencies**: [Prerequisites]

#### Tasks
1. [Task 1.1]: [Description]
   - Owner: [Role]
   - Effort: [Time estimate]
   - Dependencies: None
   - Success Criteria: [How we know it's done]

2. [Task 1.2]: [Description]
   - Owner: [Role]
   - Effort: [Time estimate]
   - Dependencies: Task 1.1
   - Success Criteria: [Done criteria]

### Phase 2: [Name]
[Similar structure]

## Dependencies
- Task 1.2 depends on Task 1.1
- Phase 2 depends on Phase 1 completion

## Milestones
- **M1**: [Milestone 1] - End of Phase 1
- **M2**: [Milestone 2] - End of Phase 2

## Confidence Level
[High|Medium|Low] - [Reasoning]
```

**Quality Criteria**:
- Phases are logically sequenced
- Tasks are specific and actionable
- All tasks have owners and estimates
- Dependencies are explicit and acyclic
- Milestones mark clear progress points

---

## Agent 3: Resource Analyst

**Role**: Identify requirements and dependencies

**Focus Areas**:
- Required Tools: Technologies and platforms
- Required Skills: Team capabilities needed
- External Dependencies: Third-party services/APIs
- Potential Blockers: Known impediments

**Analysis Approach**:
1. Identify technical stack requirements
2. Assess team skill needs
3. Map external dependencies
4. Flag potential blockers
5. Suggest mitigation strategies

**Output Structure**:
```markdown
# Resource Analysis

## Required Tools

### Development Tools
- [Tool 1]: [Purpose] - [Availability status]
- [Tool 2]: [Purpose] - [Availability status]

### Infrastructure
- [Platform 1]: [Purpose] - [Availability status]
- [Platform 2]: [Purpose] - [Availability status]

## Required Skills

### Critical Skills
- [Skill 1]: [Required level] - [Current team capability]
- [Skill 2]: [Required level] - [Current team capability]

### Nice-to-Have Skills
- [Skill 3]: [Purpose]

### Skill Gaps
- [Gap 1]: [Mitigation strategy]

## External Dependencies

### APIs/Services
- [Service 1]: [Purpose] - [SLA/Availability]
- [Service 2]: [Purpose] - [SLA/Availability]

### Third-Party Libraries
- [Library 1]: [Version] - [Stability]
- [Library 2]: [Version] - [Stability]

## Potential Blockers

### Technical Blockers
- [Blocker 1]: [Impact] - [Mitigation]

### Resource Blockers
- [Blocker 2]: [Impact] - [Mitigation]

### Process Blockers
- [Blocker 3]: [Impact] - [Mitigation]

## Recommendations
- [Recommendation 1]
- [Recommendation 2]

## Confidence Level
[High|Medium|Low] - [Reasoning]
```

**Quality Criteria**:
- All required tools identified
- Skill gaps acknowledged
- External dependencies mapped
- Blockers identified with mitigations
- Recommendations are actionable

---

## Agent 4: Timeline Estimator

**Role**: Estimate durations and sequencing

**Focus Areas**:
- Duration Estimates: Time required per task/phase
- Task Sequencing: Order of execution
- Critical Path: Tasks that can't be delayed
- Buffer Allocation: Contingency time

**Estimation Approach**:
1. Review task breakdown
2. Estimate duration per task (best/realistic/worst)
3. Identify critical path
4. Calculate parallel work opportunities
5. Add buffer for uncertainties
6. Validate timeline is realistic

**Complexity-Based Estimation**:

**Quick Complexity**:
- Rough ranges (1-2 days, 3-5 days)
- Optimistic estimates
- No detailed breakdown

**Standard Complexity**:
- Balanced estimates (2-3 days, 1-2 weeks)
- Realistic ranges
- Some buffer included

**Deep Complexity**:
- Detailed ranges (2-3 days best, 5-7 days worst)
- Conservative estimates
- +30% buffer automatically added

**Output Structure**:
```markdown
# Timeline Estimation

## Overall Timeline
**Total Duration**: [X weeks/months]
**Buffer Allocation**: [Y%]
**Confidence**: [High|Medium|Low]

## Phase Timelines

### Phase 1: [Name]
**Duration**: [Best: X days, Realistic: Y days, Worst: Z days]
**Start**: [Date or relative]
**End**: [Date or relative]

#### Task Estimates
| Task | Best Case | Realistic | Worst Case | Owner |
|------|-----------|-----------|------------|-------|
| Task 1.1 | 1 day | 2 days | 3 days | [Role] |
| Task 1.2 | 2 days | 3 days | 5 days | [Role] |

### Phase 2: [Name]
[Similar structure]

## Task Sequencing

### Sequential Tasks (Must happen in order)
1. Task 1.1 → Task 1.2 → Task 1.3

### Parallel Tasks (Can happen simultaneously)
- Task 2.1, Task 2.2, Task 2.3 (all in parallel)

## Critical Path
**Duration**: [X days on critical path]

**Path**: Task 1.1 → Task 1.3 → Task 2.2 → Task 3.1

**Impact**: Delays to these tasks delay project completion

## Buffer Strategy

### Phase-Level Buffer
- Phase 1: +15% (high uncertainty)
- Phase 2: +10% (moderate uncertainty)
- Phase 3: +5% (low uncertainty)

### Overall Buffer
- Contingency: [Y days/weeks]
- Rationale: [Why this amount]

## Milestones
- **M1** (End of Phase 1): [Date]
- **M2** (End of Phase 2): [Date]
- **M3** (Project Complete): [Date]

## Assumptions
- [Assumption 1]
- [Assumption 2]

## Confidence Level
[High|Medium|Low] - [Reasoning]
```

**Quality Criteria**:
- Estimates include ranges (not single numbers)
- Critical path identified
- Buffer allocated appropriately
- Parallel work opportunities noted
- Assumptions documented

---

## Agent 5: Quality Validator

**Role**: Validate completeness and identify risks

**Focus Areas**:
- Completeness Check: Are all aspects covered?
- Feasibility Assessment: Is plan realistic?
- Risk Matrix: Identified risks with severity
- Identified Gaps: Missing information

**Validation Approach**:
1. Review all other agents' outputs
2. Check for completeness
3. Assess feasibility
4. Identify risks (technical, schedule, resource)
5. Calculate risk scores (probability × impact)
6. Suggest mitigations

**Output Structure**:
```markdown
# Quality Validation

## Completeness Check

### Scope Coverage
- [x] Objectives defined
- [x] Boundaries clear
- [ ] Success criteria could be more specific
- [x] Constraints documented

### Task Coverage
- [x] All phases broken down
- [x] Tasks have owners
- [x] Dependencies mapped
- [ ] Some task estimates seem optimistic

### Resource Coverage
- [x] Tools identified
- [x] Skills assessed
- [ ] External dependency SLAs need verification
- [x] Blockers noted

### Timeline Coverage
- [x] Estimates provided
- [x] Critical path identified
- [ ] Buffer may be insufficient for Phase 2
- [x] Milestones defined

## Feasibility Assessment

### Technical Feasibility
**Rating**: [High|Medium|Low]
**Concerns**:
- [Concern 1]
**Recommendations**:
- [Recommendation 1]

### Schedule Feasibility
**Rating**: [High|Medium|Low]
**Concerns**:
- Timeline for Phase 2 is aggressive
**Recommendations**:
- Add 1 week buffer to Phase 2

### Resource Feasibility
**Rating**: [High|Medium|Low]
**Concerns**:
- Skill gap in [area]
**Recommendations**:
- Training or hire specialist

## Risk Matrix

| Risk | Probability | Impact | Score | Mitigation |
|------|------------|--------|-------|------------|
| API rate limits | High | High | 9 | Cache aggressively |
| Skill gap | Medium | High | 6 | Training plan |
| Timeline slip | Medium | Medium | 4 | Add buffer |

**Risk Scoring**: Probability (1-3) × Impact (1-3) = Score (1-9)
- 7-9: Critical (must mitigate)
- 4-6: High (should mitigate)
- 1-3: Low (monitor)

## Identified Gaps

### Information Gaps
- [What information is missing]
- [How to obtain it]

### Planning Gaps
- [What aspects need more planning]
- [Who should address them]

### Execution Gaps
- [What could go wrong during execution]
- [Preventive measures]

## Recommendations

### Priority 1 (Must address)
- [Critical recommendation 1]

### Priority 2 (Should address)
- [Important recommendation 2]

### Priority 3 (Nice to have)
- [Optional recommendation 3]

## Overall Assessment
**Confidence**: [High|Medium|Low]
**Readiness**: [Ready|Needs refinement|Not ready]
**Reasoning**: [Explanation of assessment]
```

**Quality Criteria**:
- All aspects reviewed
- Risks identified with scores
- Feasibility honestly assessed
- Gaps explicitly documented
- Recommendations are actionable

---

## Agent Communication Protocol

### Input Format (to agents)

```yaml
agent_input:
  request: "[Original planning request]"
  context: "[Additional background]"
  complexity: "[quick|standard|deep]"
  focus_area: "[Agent-specific focus]"
```

### Output Format (from agents)

```yaml
agent_output:
  agent_id: "[scope|breakdown|resource|timeline|quality]"
  timestamp: "[ISO-8601 timestamp]"
  content: "[Markdown output following template]"
  confidence: "[high|medium|low]"
  issues_encountered: "[List of problems]"
```

---

## Success Criteria Per Agent

**Scope Analyst Success**:
- Objectives clearly stated
- Boundaries explicitly defined
- Success criteria measurable
- Constraints documented
- Confidence level stated

**Task Decomposer Success**:
- 3-7 phases defined (or 1-3 for simple projects)
- 20-80 tasks identified
- All tasks have owners and estimates
- Dependencies explicit
- No circular dependencies

**Resource Analyst Success**:
- All required tools identified
- Skill gaps acknowledged
- External dependencies mapped
- Blockers identified with mitigations
- Confidence level stated

**Timeline Estimator Success**:
- All tasks have time estimates
- Critical path identified
- Buffer allocated
- Milestones defined
- Assumptions documented

**Quality Validator Success**:
- Completeness checked across all areas
- Feasibility assessed honestly
- Risks identified with scores
- Gaps documented
- Recommendations prioritized

---

## Error Handling Per Agent

### Agent-Specific Failures

**Scope Analyst Fails**:
- **Impact**: CRITICAL - No clear objectives
- **Action**: Retry with simplified prompt focusing on "What problem are we solving?"
- **Fallback**: Manual scope definition required

**Task Decomposer Fails**:
- **Impact**: CRITICAL - Can't plan without task breakdown
- **Action**: Retry with simplified prompt "Break this into 5-10 major steps"
- **Fallback**: Manual task breakdown required

**Resource Analyst Fails**:
- **Impact**: MEDIUM - Can proceed with basic assumptions
- **Action**: Retry once
- **Fallback**: Document "Resource analysis incomplete" in plan

**Timeline Estimator Fails**:
- **Impact**: HIGH - Timeline needed for planning
- **Action**: Retry with simpler prompt "Estimate rough duration"
- **Fallback**: Use rule-of-thumb estimates (task count × average days)

**Quality Validator Fails**:
- **Impact**: MEDIUM - Can proceed but with lower confidence
- **Action**: Retry once
- **Fallback**: Document "Quality validation incomplete, review plan carefully"

---

## Best Practices

**For All Agents**:
- Use provided templates
- State confidence levels
- Document assumptions
- Note issues encountered
- Provide actionable outputs

**Agent-Specific**:
- **Scope**: Be explicit about boundaries
- **Breakdown**: Keep tasks atomic (1-5 days each)
- **Resource**: Flag skill gaps early
- **Timeline**: Include buffer, be realistic
- **Quality**: Be honest about risks

**Quality Standards**:
- Complete all sections
- Use clear language
- Provide specific examples
- Quantify where possible
- Note uncertainties explicitly
