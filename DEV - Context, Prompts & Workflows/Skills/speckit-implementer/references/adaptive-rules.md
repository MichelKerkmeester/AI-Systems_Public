# Adaptive Rules for Implementation Execution - Context-Aware Adaptation

Rules to adapt implementation depth and execution mode based on complexity, debt, and risk.

---

## 1. 📊 Implementation Complexity Assessment

### Complexity Factors

```yaml
complexity_factors:
  code:
    lines_of_code:
      low: <200
      medium: 200-800
      high: >800
    modules:
      low: 1-2
      medium: 3-5
      high: >5
    cyclomatic_complexity:
      low: <10
      medium: 10-25
      high: >25

  integration:
    api_integrations:
      low: 0-1
      medium: 2-4
      high: >4
    external_dependencies:
      low: 0-2
      medium: 3-6
      high: >6
    data_transformations:
      low: simple
      medium: moderate
      high: complex

  testing:
    test_cases_required:
      low: <15
      medium: 15-40
      high: >40
    mocking_complexity:
      low: none
      medium: basic
      high: extensive
```

### Complexity Score Calculation

```python
def calculate_implementation_complexity(factors):
    weights = {
        'lines_of_code': 0.15,
        'modules': 0.15,
        'cyclomatic_complexity': 0.20,
        'api_integrations': 0.20,
        'external_dependencies': 0.15,
        'test_cases': 0.10,
        'mocking_complexity': 0.05
    }

    score = 0
    for factor, value in factors.items():
        if value in ['low', 'simple', 'none'] or value < thresholds[factor].low:
            points = 1
        elif value in ['medium', 'moderate', 'basic'] or value < thresholds[factor].medium:
            points = 2
        else:
            points = 3
        score += points * weights[factor]

    return score * 33.33  # Normalize to 0-100
```

.

## 2. ⚠️ Technical Debt Assessment

### Debt Indicators

```yaml
technical_debt:
  existing_codebase:
    test_coverage:
      healthy: >80%
      moderate: 40-80%
      poor: <40%
    code_quality:
      clean: well_structured
      moderate: some_issues
      messy: refactor_needed
    documentation:
      complete: >70%
      partial: 30-70%
      sparse: <30%

  implementation_risk:
    breaking_changes:
      none: 0
      minor: 1-2
      major: >2
    backwards_compatibility:
      maintained: true
      degraded: partial
      broken: false
    migration_required:
      none: 0
      simple: 1-3_steps
      complex: >3_steps
```

### Debt Score Calculation

```python
def calculate_technical_debt(indicators):
    weights = {
        'test_coverage': 0.25,
        'code_quality': 0.25,
        'documentation': 0.15,
        'breaking_changes': 0.20,
        'migration_complexity': 0.15
    }

    score = 0
    for indicator, value in indicators.items():
        if value in ['healthy', 'clean', 'complete', 'none', 'maintained']:
            points = 1
        elif value in ['moderate', 'partial', 'minor', 'simple', 'degraded']:
            points = 2
        else:
            points = 3
        score += points * weights[indicator]

    return score * 33.33  # Normalize to 0-100
```

.

## 3. 🔄 Adaptive Strategies

### Based on Implementation Complexity

#### Low Complexity (0-30)
```yaml
strategy:
  concurrency: 3
  preparation_depth: standard
  checkpoint_frequency: major_milestones
  testing_rigor: standard
  documentation: essential
  review: basic
```

#### Medium Complexity (31-70)
```yaml
strategy:
  concurrency: 2
  preparation_depth: thorough
  checkpoint_frequency: per_module
  testing_rigor: comprehensive
  documentation: detailed
  review: thorough
  additions:
    - integration_validation
    - performance_checks
    - error_path_testing
```

#### High Complexity (71-100)
```yaml
strategy:
  concurrency: 2
  preparation_depth: exhaustive
  checkpoint_frequency: per_component
  testing_rigor: exhaustive
  documentation: comprehensive
  review: exhaustive
  additions:
    - incremental_implementation
    - proof_of_concepts
    - stress_testing
    - security_review
    - rollback_planning
```

### Based on Technical Debt

#### Low Debt (0-30)
```yaml
strategy:
  implementation_approach: standard
  refactoring: minimal
  testing: new_code_only
  documentation_update: changes_only
  migration: none
```

#### Medium Debt (31-70)
```yaml
strategy:
  implementation_approach: cautious
  refactoring: targeted
  testing: new_plus_affected
  documentation_update: comprehensive
  migration: planned
  additions:
    - backwards_compatibility_layer
    - deprecation_warnings
    - migration_guides
```

#### High Debt (71-100)
```yaml
strategy:
  implementation_approach: phased
  refactoring: extensive
  testing: full_regression
  documentation_update: complete_rewrite
  migration: multi_phase
  additions:
    - tech_debt_reduction
    - comprehensive_refactoring
    - dual_run_period
    - extensive_migration_support
```

.

## 4. ⚙️ Execution Modes

### Mode 1: Standard Implementation (Default)

```yaml
configuration:
  preparation: [core, integrations, tests, docs]
  parallelism: 3
  implementation: autonomous
  checkpoints: module_level
  testing: comprehensive
  when: complexity < 60 AND debt < 40
```

### Mode 2: Incremental Implementation

```yaml
configuration:
  preparation: sequential_detailed
  parallelism: 1
  implementation: step_by_step
  checkpoints: component_level
  testing: continuous
  when: complexity > 70 OR debt > 60
```

### Mode 3: Prototype-First

```yaml
configuration:
  preparation: minimal
  parallelism: 2
  implementation: poc_then_production
  checkpoints: proof_of_concept
  testing: validation_focused
  when: high_uncertainty OR new_technology
```

### Mode 4: Refactor-Then-Implement

```yaml
configuration:
  preparation: extensive_analysis
  parallelism: 1
  implementation: refactor_first
  checkpoints: refactor_milestones
  testing: regression_heavy
  when: debt > 70 OR legacy_codebase
```

.

## 5. 🎯 Dynamic Adjustments

### Runtime Monitoring

```python
class ImplementationMonitor:
    def adjust_strategy(self, metrics):
        if metrics.test_failure_rate > 0.2:
            self.add_testing_rigor()
            self.pause_for_debugging()

        if metrics.build_failures > 2:
            self.check_dependencies()
            self.validate_environment()

        if metrics.complexity_spike:
            self.break_into_subtasks()
            self.add_checkpoint()

        if metrics.time_elapsed > estimate * 1.5:
            self.reassess_approach()
            self.consider_simplification()
```

### Progressive Implementation

```yaml
implementation_phases:
  phase_1_foundation:
    scope: core_data_structures
    testing: unit_only
    validation: type_checking
    checkpoint: required

  phase_2_logic:
    scope: business_logic
    testing: unit_integration
    validation: coverage_targets
    checkpoint: required

  phase_3_integration:
    scope: external_apis
    testing: integration_e2e
    validation: contract_testing
    checkpoint: required

  phase_4_polish:
    scope: error_handling_docs
    testing: edge_cases
    validation: quality_review
    checkpoint: required
```

.

## 6. 🛡️ Fallback Strategies

### Graceful Degradation Path

```
1. Full Autonomous Implementation
   ↓ (test failures)
2. Checkpoint-Based Implementation
   ↓ (complexity spike)
3. Incremental with Review
   ↓ (understanding gaps)
4. Prototype + Validate
   ↓ (approach uncertain)
5. Pair with Human Developer
   ↓ (blocked)
6. Document Blockers + Manual Handoff
```

### Recovery Actions

```yaml
on_test_failure:
  - analyze_failure_pattern
  - check_test_correctness
  - review_implementation
  - add_debugging_logs
  - fix_and_rerun

on_build_failure:
  - check_dependencies
  - validate_syntax
  - review_imports
  - check_configuration
  - rollback_if_needed

on_integration_failure:
  - validate_contracts
  - check_api_compatibility
  - review_error_handling
  - add_resilience
  - fallback_to_mock

on_complexity_spike:
  - break_into_subtasks
  - extract_functions
  - add_abstractions
  - document_rationale
  - refactor_incrementally
```

.

## 7. 🚀 Optimization Rules

### Pre-implementation Optimization

```python
def optimize_before_implementation(context):
    # Analyze implementation needs
    complexity = calculate_complexity(context)
    debt = calculate_technical_debt(context)
    resources = check_resources()

    # Select optimal approach
    if complexity < 30 and debt < 30:
        return 'direct_implementation'
    elif debt > 70:
        return 'refactor_first'
    elif complexity > 70:
        return 'incremental_with_checkpoints'
    else:
        return 'standard_autonomous'
```

### Code Quality Gates

```python
def quality_gates(code):
    gates = {
        'linting': run_linter(code),
        'type_checking': run_type_checker(code),
        'test_coverage': calculate_coverage(code) > 80,
        'cyclomatic_complexity': max_complexity(code) < 15,
        'no_duplicates': duplication_ratio(code) < 5
    }

    passed = all(gates.values())
    return passed, gates
```

.

## 8. 🧪 Testing Strategy Adaptation

### Test Coverage Targets

```yaml
coverage_by_complexity:
  low_complexity:
    unit: 75%
    integration: 50%
    e2e: optional

  medium_complexity:
    unit: 85%
    integration: 70%
    e2e: critical_paths

  high_complexity:
    unit: 90%
    integration: 85%
    e2e: comprehensive
```

### Test Priority Matrix

```python
def prioritize_tests(component):
    priority = {
        'critical_path': 1,
        'high_complexity': 2,
        'data_validation': 3,
        'error_handling': 4,
        'edge_cases': 5,
        'performance': 6
    }

    tests = []
    for category, p in priority.items():
        tests.extend(generate_tests(component, category, priority=p))

    return sorted(tests, key=lambda t: t.priority)
```

.

## 9. 📋 Configuration Examples

### Example 1: Simple Feature Addition

```yaml
detected:
  complexity: 25
  debt: 15
  tests_required: 8
  modules: 2

applied_rules:
  concurrency: 3
  approach: direct
  checkpoints: minimal
  testing: standard
  documentation: inline
```

### Example 2: Complex Integration

```yaml
detected:
  complexity: 85
  debt: 40
  tests_required: 45
  modules: 8
  apis: 5

applied_rules:
  concurrency: 2
  approach: incremental
  checkpoints: per_module
  testing: exhaustive
  documentation: comprehensive
  additions:
    - contract_testing
    - resilience_patterns
    - monitoring
```

### Example 3: Legacy Refactoring

```yaml
detected:
  complexity: 60
  debt: 85
  tests_required: 30
  breaking_changes: 3

applied_rules:
  concurrency: 1
  approach: refactor_first
  checkpoints: per_refactor
  testing: regression_heavy
  documentation: complete_rewrite
  additions:
    - backwards_compatibility
    - deprecation_period
    - migration_tooling
```

.

## 10. ✅ Success Metrics

### Implementation Quality Metrics

```yaml
metrics:
  implementation_completeness:
    target: >95%
    measure: completed_tasks / total_tasks

  test_coverage:
    target: >85%
    measure: covered_lines / total_lines

  build_success_rate:
    target: >98%
    measure: successful_builds / total_builds

  test_pass_rate:
    target: >95%
    measure: passing_tests / total_tests

  code_quality_score:
    target: >80
    measure: linter_score + complexity_score / 2

  checkpoint_success:
    target: >90%
    measure: successful_checkpoints / total_checkpoints
```

.

## 11. 🎯 YAML ADAPTIVE RULES MAPPING

This section maps the YAML `adaptive_rules` fields from `sk_p__implementation.yaml` to concrete workflow behaviors.

### Rule: high_complexity

**YAML Configuration**:
```yaml
high_complexity:
  concurrency: 2
  review_depth: exhaustive
```

**Triggers**:
- Large implementation scope (>20 files to modify)
- Complex technical requirements (>15 modules)
- Multiple integration points (>5 external systems)
- High technical debt score
- Implementation complexity score > 70

**Adaptations Applied**:
- **Reduce Concurrency**: `3 → 2` parallel agents (fewer simultaneous executions)
- **Increase Review Depth**: `standard → exhaustive` (more thorough validation)
- **Add Checkpoints**: More frequent validation during implementation
- **Extended Timeouts**: Allow more time for complex implementation tasks

**Impact**:
- **Execution Time**: Longer (reduced parallelism, more checkpoints)
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
- Unclear implementation approach in plan.md
- Missing technical specifications
- New technology or unfamiliar patterns
- Contradictory information in artifacts
- Uncertainty score > 80

**Adaptations Applied**:
- **Insert Discovery Phase**: Add proof-of-concept step BEFORE parallel blocks
- **Use Estimate Ranges**: Replace point estimates with min-max ranges
- **Prototype First**: Create throwaway prototypes to validate approach
- **Iterative Refinement**: Enable progressive implementation with frequent validation

**Impact**:
- **Execution Time**: Additional discovery/prototyping adds time
- **Risk Mitigation**: Discovery phase prevents implementing wrong solution
- **Accuracy**: More conservative estimates reduce over-commitment

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
Start Implementation Workflow
    ↓
Check Implementation Complexity Score
    ↓
    ├─ >70? → Apply high_complexity rules
    └─ ≤70? → Continue
    ↓
Check Technical Uncertainty Score
    ↓
    ├─ >80? → Apply high_uncertainty rules (insert discovery)
    └─ ≤80? → Continue
    ↓
Check Parallel Support
    ↓
    ├─ Not supported? → Apply parallel_not_supported rules (sequential)
    └─ Supported? → Use default parallelism (concurrency=3)
    ↓
Execute Implementation with Adapted Configuration
```

---

### Rule Combination Matrix

| Complexity | Uncertainty | Parallel Support | Concurrency | Review Depth | Discovery Phase |
|-----------|-------------|------------------|-------------|--------------|-----------------|
| Low | Low | Yes | 3 | Standard | No |
| High | Low | Yes | 2 | Exhaustive | No |
| Low | High | Yes | 3 | Standard | Yes (Prototype) |
| High | High | Yes | 2 | Exhaustive | Yes (Prototype) |
| Any | Any | No | 1 | Standard/Exhaustive* | As needed |

*Review depth determined by complexity score

---

.

## 12. ⭐ Best Practices

### DO:

- Write tests before implementation
- Commit after each module
- Add inline documentation
- Use type hints/annotations
- Handle errors explicitly

### DON'T:

- Skip test writing
- Ignore linter warnings
- Leave TODOs uncommitted
- Over-engineer solutions
- Ignore performance implications

### ALWAYS:

- Follow code standards
- Run tests before commit
- Update documentation
- Check for regressions
- Validate against spec