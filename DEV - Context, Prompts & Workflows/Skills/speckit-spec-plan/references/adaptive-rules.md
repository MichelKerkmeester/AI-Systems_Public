# Adaptive Rules for Planning & Specification - Context-Aware Adaptation

Rules to adapt planning depth and execution mode based on complexity, clarity, and uncertainty.

---

## 1. 📊 Planning Complexity Assessment

### Complexity Factors

```yaml
planning_factors:
  requirements:
    stakeholders:
      low: 1-2
      medium: 3-5
      high: >5
    user_stories:
      low: <5
      medium: 5-12
      high: >12
    acceptance_criteria:
      low: <10
      medium: 10-25
      high: >25

  technical:
    architectural_decisions:
      low: <3
      medium: 3-7
      high: >7
    integration_points:
      low: 0-2
      medium: 3-6
      high: >6
    new_technologies:
      low: 0
      medium: 1-2
      high: >2

  constraints:
    regulatory_compliance:
      none: 0
      moderate: 1-2
      strict: >2
    performance_requirements:
      basic: standard_perf
      demanding: high_perf
      critical: real_time
    security_level:
      standard: basic_auth
      elevated: encryption
      critical: zero_trust
```

### Planning Complexity Score

```python
def calculate_planning_complexity(factors):
    weights = {
        'stakeholders': 0.15,
        'user_stories': 0.15,
        'acceptance_criteria': 0.10,
        'architectural_decisions': 0.20,
        'integration_points': 0.15,
        'new_technologies': 0.10,
        'compliance': 0.10,
        'security_level': 0.05
    }

    score = 0
    for factor, value in factors.items():
        if value in ['low', 'none', 'basic', 'standard', 0] or value < thresholds[factor].low:
            points = 1
        elif value in ['medium', 'moderate', 'demanding', 'elevated'] or value < thresholds[factor].medium:
            points = 2
        else:
            points = 3
        score += points * weights[factor]

    return score * 33.33  # Normalize to 0-100
```

.

## 2. 🔍 Requirement Clarity Assessment

### Clarity Indicators

```yaml
clarity_indicators:
  specification:
    goal_clarity:
      clear: well_defined_objectives
      unclear: vague_objectives
      ambiguous: conflicting_objectives

    scope_definition:
      clear: explicit_boundaries
      fuzzy: implicit_boundaries
      undefined: no_boundaries

    success_metrics:
      defined: measurable_kpis
      partial: qualitative_only
      missing: no_metrics

  constraints:
    known_constraints:
      complete: all_identified
      partial: some_identified
      unknown: discovery_needed

    priorities:
      clear: ranked_by_value
      unclear: all_high_priority
      conflicting: contradictory
```

### Clarity Score Calculation

```python
def calculate_clarity(indicators):
    weights = {
        'goal_clarity': 0.30,
        'scope_definition': 0.25,
        'success_metrics': 0.20,
        'known_constraints': 0.15,
        'priorities': 0.10
    }

    score = 0
    for indicator, value in indicators.items():
        if value in ['clear', 'defined', 'complete']:
            points = 3
        elif value in ['fuzzy', 'partial', 'unclear']:
            points = 2
        else:
            points = 1
        score += points * weights[indicator]

    return (score / 3) * 100  # Normalize to 0-100
```

.

## 3. 🎯 Adaptive Strategies

### Based on Planning Complexity

#### Low Complexity (0-30)
```yaml
strategy:
  concurrency: 3
  planning_depth: standard
  iterations: 1
  approval_gates: streamlined
  documentation: essential
  risk_analysis: basic
```

#### Medium Complexity (31-70)
```yaml
strategy:
  concurrency: 2
  planning_depth: thorough
  iterations: 1
  approval_gates: standard
  documentation: comprehensive
  risk_analysis: detailed
  additions:
    - trade_off_analysis
    - dependency_mapping
    - milestone_planning
```

#### High Complexity (71-100)
```yaml
strategy:
  concurrency: 2
  planning_depth: exhaustive
  iterations: 2
  approval_gates: strict
  documentation: exhaustive
  risk_analysis: comprehensive
  additions:
    - stakeholder_alignment
    - phased_approach
    - decision_documentation
    - contingency_planning
    - external_review
```

### Based on Requirement Clarity

#### High Clarity (>70)
```yaml
strategy:
  execution: standard_parallel
  clarification: minimal
  validation: basic
  documentation: standard
  iterations: 1
```

#### Medium Clarity (40-70)
```yaml
strategy:
  execution: parallel_with_validation
  clarification: targeted
  validation: thorough
  documentation: detailed
  iterations: 1
  additions:
    - assumption_documentation
    - decision_rationale
    - stakeholder_review
```

#### Low Clarity (<40)
```yaml
strategy:
  execution: discovery_then_planning
  clarification: comprehensive
  validation: extensive
  documentation: exhaustive
  iterations: 2+
  additions:
    - discovery_phase
    - stakeholder_interviews
    - prototype_validation
    - iterative_refinement
    - frequent_checkpoints
```

.

## 4. ⚙️ Execution Modes

### Mode 1: Standard Planning (Default)

```yaml
configuration:
  analysts: [requirements, architecture, risk, estimation]
  parallelism: 3
  depth: thorough
  iterations: 1
  validation: standard
  approval_gates: normal
  when: complexity < 60 AND clarity > 50
```

### Mode 2: Discovery Planning

```yaml
configuration:
  analysts: all + exploratory
  parallelism: 2
  depth: iterative
  iterations: 2+
  validation: continuous
  approval_gates: frequent
  when: clarity < 40 OR new_domain
```

### Mode 3: Rapid Planning

```yaml
configuration:
  analysts: [requirements, architecture]
  parallelism: 2
  depth: overview
  iterations: 1
  validation: basic
  approval_gates: streamlined
  when: time_critical AND complexity < 40
```

### Mode 4: Enterprise Planning

```yaml
configuration:
  analysts: all + compliance + stakeholder
  parallelism: 2
  depth: exhaustive
  iterations: 2
  validation: extensive
  approval_gates: strict
  when: complexity > 70 OR regulated_industry
```

.

## 5. 🔄 Dynamic Adjustments

### Runtime Monitoring

```python
class PlanningMonitor:
    def adjust_strategy(self, metrics):
        if metrics.ambiguity_count > 5:
            self.add_clarification_round()

        if metrics.stakeholder_conflicts > 2:
            self.add_alignment_session()

        if metrics.risk_count > 10:
            self.increase_risk_analysis_depth()

        if metrics.dependency_cycles_found:
            self.add_architecture_review()
```

### Progressive Refinement

```yaml
refinement_stages:
  stage_1_rough:
    scope: high_level_only
    details: minimal
    validation: conceptual
    checkpoint: direction_approval

  stage_2_detailed:
    scope: component_level
    details: thorough
    validation: technical
    checkpoint: approach_approval

  stage_3_comprehensive:
    scope: implementation_ready
    details: complete
    validation: comprehensive
    checkpoint: final_approval

  stage_4_refined:
    scope: edge_cases_risks
    details: exhaustive
    validation: stakeholder_aligned
    checkpoint: commitment
```

.

## 6. 🛡️ Fallback Strategies

### Graceful Degradation Path

```
1. Full Parallel Planning (4 analysts)
   ↓ (conflicting perspectives)
2. Sequential with Reconciliation
   ↓ (clarity issues)
3. Discovery + Iterative Planning
   ↓ (stakeholder misalignment)
4. Phased Consensus Building
   ↓ (too complex)
5. Break into Sub-plans
   ↓ (complete failure)
6. External Facilitation Required
```

### Recovery Actions

```yaml
on_conflicting_requirements:
  - document_all_perspectives
  - create_comparison_matrix
  - facilitate_stakeholder_meeting
  - establish_priority_framework
  - get_executive_decision

on_missing_information:
  - document_assumptions
  - identify_information_owners
  - schedule_discovery_sessions
  - create_information_checklist
  - proceed_with_flags

on_unclear_priorities:
  - apply_value_scoring
  - estimate_effort_ranges
  - create_decision_matrix
  - facilitate_prioritization
  - document_rationale

on_architectural_uncertainty:
  - research_approaches
  - create_proof_of_concepts
  - evaluate_alternatives
  - document_trade_offs
  - recommend_with_confidence_levels
```

.

## 7. 🚀 Optimization Rules

### Planning Workflow Optimization

```python
def optimize_planning_workflow(context):
    # Assess planning needs
    complexity = calculate_complexity(context)
    clarity = calculate_clarity(context)

    # Select optimal workflow
    if clarity > 70 and complexity < 40:
        return 'streamlined_planning'
    elif clarity < 40:
        return 'discovery_first'
    elif complexity > 70:
        return 'phased_detailed_planning'
    else:
        return 'standard_parallel'
```

### Stakeholder Engagement Strategy

```python
def optimize_stakeholder_engagement(stakeholders):
    strategy = {
        'high_involvement': [],
        'review_approval': [],
        'keep_informed': []
    }

    for sh in stakeholders:
        if sh.decision_authority or sh.domain_expert:
            strategy['high_involvement'].append(sh)
        elif sh.approval_required:
            strategy['review_approval'].append(sh)
        else:
            strategy['keep_informed'].append(sh)

    return strategy
```

.

## 8. ⚠️ Risk Analysis Adaptation

### Risk Assessment Depth

```yaml
risk_depth_by_criticality:
  low_criticality:
    identification: basic
    assessment: qualitative
    mitigation: optional
    monitoring: periodic

  medium_criticality:
    identification: thorough
    assessment: semi_quantitative
    mitigation: planned
    monitoring: regular

  high_criticality:
    identification: exhaustive
    assessment: quantitative
    mitigation: detailed_plans
    monitoring: continuous
    additions:
      - contingency_plans
      - escalation_procedures
```

.

## 9. 💡 Configuration Examples

### Example 1: Well-Defined Feature

```yaml
detected:
  complexity: 35
  clarity: 85
  stakeholders: 2
  compliance: none

applied_rules:
  concurrency: 3
  depth: standard
  iterations: 1
  approval_gates: streamlined
  documentation: standard
```

### Example 2: Enterprise Initiative

```yaml
detected:
  complexity: 80
  clarity: 60
  stakeholders: 8
  compliance: strict

applied_rules:
  concurrency: 2
  depth: exhaustive
  iterations: 2
  approval_gates: strict
  documentation: comprehensive
  additions:
    - compliance_review
    - stakeholder_alignment
    - risk_mitigation_planning
```

### Example 3: Exploratory Project

```yaml
detected:
  complexity: 55
  clarity: 25
  stakeholders: 4
  new_domain: true

applied_rules:
  concurrency: 2
  depth: iterative
  iterations: 3
  approval_gates: frequent
  documentation: progressive
  additions:
    - discovery_sprints
    - prototype_validation
    - assumption_testing
```

.

## 10. 📈 Success Metrics

### Planning Quality Metrics

```yaml
metrics:
  requirement_completeness:
    target: >95%
    measure: defined_requirements / total_requirements

  stakeholder_alignment:
    target: >90%
    measure: approved_aspects / total_aspects

  risk_coverage:
    target: >85%
    measure: identified_risks / expected_risks

  architectural_clarity:
    target: >90%
    measure: defined_components / total_components

  estimation_confidence:
    target: >75%
    measure: high_confidence_estimates / total_estimates

  approval_efficiency:
    target: <3_iterations
    measure: approval_rounds_needed
```

.

## 11. 🎯 YAML ADAPTIVE RULES MAPPING

This section maps the YAML `adaptive_rules` fields from `sk_p__spec_plan.yaml` to concrete workflow behaviors.

### Rule: high_complexity

**YAML Configuration**:
```yaml
high_complexity:
  concurrency: 2
  review_depth: exhaustive
```

**Triggers**:
- Large spec folder (>10 files)
- Complex requirements (>50 acceptance criteria)
- Multiple integration points (>5 external systems)
- High technical complexity (planning_complexity_score > 70)

**Adaptations Applied**:
- **Reduce Concurrency**: `3 → 2` parallel agents (fewer simultaneous executions)
- **Increase Review Depth**: `standard → exhaustive` (more thorough validation)
- **Add Checkpoints**: Insert intermediate validation between parallel blocks
- **Extended Timeouts**: Allow more time for complex agent processing

**Impact**:
- **Execution Time**: Longer (reduced parallelism)
- **Quality**: Higher (exhaustive review catches more issues)
- **Resource Usage**: Lower peak usage (fewer concurrent agents)

---

### Rule: high_uncertainty

**YAML Configuration**:
```yaml
high_uncertainty:
  insert: discovery_microstep_before_parallel_blocks
  estimates: use_ranges
```

**Triggers**:
- Ambiguous requirements in spec.md
- Missing critical context
- Contradictory information in artifacts
- Requirement clarity score < 60
- New domain or unfamiliar technology

**Adaptations Applied**:
- **Insert Discovery Phase**: Add microstep BEFORE parallel blocks to clarify unknowns
- **Use Estimate Ranges**: Replace point estimates with min-max ranges
- **Flag Uncertainty Areas**: Explicitly mark unclear sections for user review
- **Iterative Refinement**: Enable progressive clarification loops

**Impact**:
- **Execution Time**: Additional clarification pass adds time
- **Accuracy**: More conservative estimates reduce over-commitment
- **Risk Mitigation**: Discovery phase prevents wasted parallel effort

---

### Rule: parallel_not_supported

**YAML Configuration**:
```yaml
parallel_not_supported:
  concurrency: 1
  note: "If parallel sub-agents unsupported, run tasks one-by-one; keep review and synthesis."
```

**Triggers**:
- Environment limitations (single-threaded execution environment)
- API rate limits preventing concurrent requests
- Context window constraints (insufficient memory for parallel agents)
- System resources exhausted

**Adaptations Applied**:
- **Reduce to Sequential**: `concurrency → 1` (all agents run one-by-one)
- **Preserve Phases**: Keep review and synthesis phases intact
- **Extend Timeouts**: Account for sequential execution duration
- **Simplified Monitoring**: Reduce overhead of parallel coordination

**Impact**:
- **Execution Time**: Significantly longer (3-4x sequential vs parallel)
- **Quality**: Same (review/synthesis phases preserved)
- **Resource Usage**: Minimal (single agent at a time)

---

### Adaptive Rule Decision Tree

```
Start Planning Workflow
    ↓
Check Planning Complexity Score
    ↓
    ├─ >70? → Apply high_complexity rules
    └─ ≤70? → Continue
    ↓
Check Requirement Clarity Score
    ↓
    ├─ <60? → Apply high_uncertainty rules (insert discovery)
    └─ ≥60? → Continue
    ↓
Check Parallel Support
    ↓
    ├─ Not supported? → Apply parallel_not_supported rules (sequential)
    └─ Supported? → Use default parallelism (concurrency=3)
    ↓
Execute Planning with Adapted Configuration
```

---

### Rule Combination Matrix

| Complexity | Uncertainty | Parallel Support | Concurrency | Review Depth | Discovery Phase |
|-----------|-------------|------------------|-------------|--------------|-----------------|
| Low | Low | Yes | 3 | Standard | No |
| High | Low | Yes | 2 | Exhaustive | No |
| Low | High | Yes | 3 | Standard | Yes |
| High | High | Yes | 2 | Exhaustive | Yes |
| Any | Any | No | 1 | Standard/Exhaustive* | As needed |

*Review depth determined by complexity score

---

.

## 12. ✅ Best Practices

### DO:

- Start with why (business value)
- Involve stakeholders early
- Document assumptions explicitly
- Consider alternatives
- Define success metrics

### DON'T:

- Skip stakeholder alignment
- Ignore constraints
- Over-commit on timelines
- Leave risks unmitigated
- Assume requirements are static

### ALWAYS:

- Validate understanding
- Document decisions and rationale
- Consider technical debt
- Plan for change
- Get explicit approval before proceeding