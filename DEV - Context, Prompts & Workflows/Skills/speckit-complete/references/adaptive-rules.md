# Adaptive Rules for Parallel Execution - Context-Aware Planning Adaptation Rules

Dynamic rules for adapting parallel execution strategies based on complexity and uncertainty.

---

## 1. 📊 COMPLEXITY ASSESSMENT

### Complexity Factors

```yaml
complexity_factors:
  requirements:
    feature_count:
      low: <5
      medium: 5-15
      high: >15
    integration_points:
      low: <3
      medium: 3-7
      high: >7
    user_stories:
      low: <3
      medium: 3-8
      high: >8

  technical:
    components:
      low: <5
      medium: 5-10
      high: >10
    external_dependencies:
      low: 0-1
      medium: 2-4
      high: >4
    data_models:
      low: <3
      medium: 3-8
      high: >8

  risk:
    critical_risks:
      low: 0
      medium: 1-2
      high: >2
    compliance_requirements:
      low: none
      medium: basic
      high: regulated
```

### Complexity Score Calculation

```python
def calculate_complexity(factors):
    weights = {
        'feature_count': 0.15,
        'integration_points': 0.20,
        'user_stories': 0.10,
        'components': 0.15,
        'external_dependencies': 0.20,
        'data_models': 0.10,
        'critical_risks': 0.05,
        'compliance_requirements': 0.05
    }

    score = 0
    for factor, value in factors.items():
        if value == 'low' or value <= thresholds.low:
            points = 1
        elif value == 'medium' or value <= thresholds.medium:
            points = 2
        else:
            points = 3
        score += points * weights[factor]

    return score * 33.33  # Normalize to 0-100
```

.

## 2. 🔍 UNCERTAINTY ASSESSMENT

### Uncertainty Indicators

```yaml
uncertainty_indicators:
  specification:
    unclear_requirements: count
    needs_clarification_markers: count
    ambiguous_terms: count
    missing_acceptance_criteria: count

  technical:
    unknown_dependencies: count
    new_technology: boolean
    integration_uncertainty: level
    performance_unknowns: count

  domain:
    business_rule_clarity: percentage
    edge_cases_identified: percentage
    user_behavior_predictability: level
```

### Uncertainty Score Calculation

```python
def calculate_uncertainty(indicators):
    weights = {
        'unclear_requirements': 0.25,
        'technical_unknowns': 0.25,
        'domain_uncertainty': 0.20,
        'missing_criteria': 0.15,
        'new_technology': 0.15
    }

    score = 0
    for indicator, value in indicators.items():
        normalized = normalize_indicator(value)
        score += normalized * weights.get(indicator, 0.1)

    return score * 100  # Percentage
```

.

## 3. 🎯 ADAPTIVE STRATEGIES

### Based on Complexity

#### Low Complexity (0-30)
```yaml
strategy:
  concurrency: 3
  review_depth: standard
  synthesis_iterations: 1
  approval_gates: normal
  fallback: none
```

#### Medium Complexity (31-70)
```yaml
strategy:
  concurrency: 2
  review_depth: thorough
  synthesis_iterations: 1
  approval_gates: normal
  fallback: sequential_on_failure
  additions:
    - validation_checkpoints
    - progress_monitoring
```

#### High Complexity (71-100)
```yaml
strategy:
  concurrency: 2
  review_depth: exhaustive
  synthesis_iterations: 2
  approval_gates: strict
  fallback: always_sequential_option
  additions:
    - discovery_phase
    - incremental_execution
    - detailed_logging
    - checkpoint_saves
```

### Based on Uncertainty

#### Low Uncertainty (0-30%)
```yaml
strategy:
  execution: standard_parallel
  clarification: minimal
  validation: standard
  documentation: normal
```

#### Medium Uncertainty (31-60%)
```yaml
strategy:
  execution: parallel_with_validation
  clarification: targeted_questions
  validation: enhanced
  documentation: detailed
  additions:
    - assumption_documentation
    - risk_mitigation_plans
```

#### High Uncertainty (61-100%)
```yaml
strategy:
  execution: staged_with_discovery
  clarification: comprehensive
  validation: extensive
  documentation: exhaustive
  additions:
    - discovery_sprints
    - prototype_phases
    - user_feedback_loops
    - iterative_refinement
```

.

## 4. ⚙️ EXECUTION MODES

### Mode 1: Full Parallel (Default)

```yaml
configuration:
  stages: [A, B, C]
  parallelism: maximum
  review: complete
  synthesis: full
  qa: thorough
  when: complexity < 70 AND uncertainty < 60 AND resources > 40%
```

### Mode 2: Staged Parallel

```yaml
configuration:
  stages: sequential([A], [B], [C])
  parallelism: within_stage_only
  review: complete
  synthesis: full
  qa: standard
  when: complexity > 70 OR memory < 30%
```

### Mode 3: Sequential Fallback

```yaml
configuration:
  stages: sequential(all_agents)
  parallelism: none
  review: simplified
  synthesis: basic
  qa: essential
  when: parallel_failure OR resources < 20%
```

### Mode 4: Discovery Mode

```yaml
configuration:
  stages: [discovery, A, validation, B, C]
  parallelism: reduced
  review: iterative
  synthesis: progressive
  qa: continuous
  when: uncertainty > 80 OR new_domain
```

.

## 5. 🔄 DYNAMIC ADJUSTMENTS

### Runtime Monitoring

```python
class RuntimeMonitor:
    def adjust_strategy(self, metrics):
        if metrics.failure_rate > 0.3:
            self.reduce_concurrency()

        if metrics.timeout_rate > 0.2:
            self.increase_timeouts()

        if metrics.memory_pressure > 0.8:
            self.enable_memory_optimizations()

        if metrics.user_rejections > 2:
            self.increase_review_depth()
```

### Progressive Enhancement

```yaml
enhancement_levels:
  level_1:
    name: minimal
    agents: core_only
    review: basic
    synthesis: essential

  level_2:
    name: standard
    agents: core + quality
    review: standard
    synthesis: complete

  level_3:
    name: comprehensive
    agents: all
    review: thorough
    synthesis: detailed

  level_4:
    name: exhaustive
    agents: all + validators
    review: exhaustive
    synthesis: iterative
```

.

## 6. 🛡️ FALLBACK STRATEGIES

### Graceful Degradation Path

```
1. Full Parallel
   ↓ (failure)
2. Reduced Parallel (concurrency: 2)
   ↓ (failure)
3. Sequential Stages (parallel within stage)
   ↓ (failure)
4. Full Sequential (one agent at a time)
   ↓ (failure)
5. Essential Only (skip optional agents)
   ↓ (failure)
6. Manual Intervention Required
```

### Recovery Actions

```yaml
on_agent_failure:
  - retry_with_backoff
  - use_cached_if_available
  - try_alternative_agent
  - continue_with_partial
  - mark_as_degraded

on_stage_failure:
  - attempt_recovery
  - rollback_changes
  - save_checkpoint
  - notify_user
  - provide_manual_steps

on_complete_failure:
  - save_all_artifacts
  - generate_error_report
  - provide_recovery_instructions
  - offer_manual_continuation
  - schedule_retry
```

.

## 7. 🚀 OPTIMIZATION RULES

### Pre-execution Optimization

```python
def optimize_before_execution(context):
    # Analyze task characteristics
    complexity = calculate_complexity(context)
    uncertainty = calculate_uncertainty(context)
    resources = check_resources()

    # Select optimal strategy
    if complexity < 30 and uncertainty < 30:
        return 'fast_track'
    elif resources.memory < 1024:
        return 'memory_optimized'
    else:
        return 'balanced'
```

### During-execution Optimization

```python
def optimize_during_execution(metrics):
    # Monitor and adjust
    if metrics.progress < expected_progress(metrics.elapsed_time):
        increase_resources()

    if metrics.error_rate > threshold:
        switch_to_safer_mode()

    if metrics.quality_score < minimum:
        increase_review_depth()
```

### Post-execution Optimization

```python
def learn_from_execution(results):
    # Update heuristics
    if results.success:
        reinforce_strategy(results.strategy)
    else:
        penalize_strategy(results.strategy)

    # Cache successful patterns
    if results.quality_score > 90:
        cache_pattern(results.pattern)

    # Document learnings
    log_execution_insights(results)
```

.

## 8. 💡 CONFIGURATION EXAMPLES

### Example 1: Complex Enterprise Feature

```yaml
detected:
  complexity: 85
  uncertainty: 45
  resources: adequate

applied_rules:
  concurrency: 2
  timeouts: extended
  review: exhaustive
  synthesis: iterative
  stages: sequential
  checkpoints: enabled
  fallback: ready
```

### Example 2: Simple Enhancement

```yaml
detected:
  complexity: 20
  uncertainty: 15
  resources: abundant

applied_rules:
  concurrency: 3
  timeouts: standard
  review: basic
  synthesis: single
  stages: parallel
  checkpoints: disabled
  fallback: none
```

### Example 3: Uncertain Requirements

```yaml
detected:
  complexity: 50
  uncertainty: 85
  resources: adequate

applied_rules:
  concurrency: 1
  timeouts: flexible
  review: iterative
  synthesis: progressive
  stages: discovery_first
  checkpoints: frequent
  fallback: manual
```

.

## 9. 📈 SUCCESS METRICS

### Adaptation Effectiveness

```yaml
metrics:
  adaptation_success_rate:
    target: >90%
    measure: successful_completions / total_attempts

  resource_efficiency:
    target: >70%
    measure: useful_work / resources_consumed

  quality_maintenance:
    target: >85%
    measure: quality_with_adaptation / quality_without

  execution_efficiency:
    target: optimized
    measure: parallel_speedup_vs_sequential

  failure_recovery:
    target: >95%
    measure: recovered_failures / total_failures
```

.

## 10. ✅ BEST PRACTICES

### DO:

- Monitor continuously
- Adjust progressively
- Document decisions
- Cache learnings
- Fail gracefully

### DON'T

- Over-optimize prematurely
- Ignore resource limits
- Skip monitoring
- Force inappropriate modes
- Hide degradation from user

### ALWAYS:

- Preserve quality over speed
- Maintain audit trail
- Respect user preferences
- Provide visibility
