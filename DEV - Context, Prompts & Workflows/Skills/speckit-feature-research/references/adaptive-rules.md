# Adaptive Rules for Research Execution - Context-Aware Adaptation

Rules to adapt research scope and execution modes based on clarity, signal quality, and uncertainty.

---

## 1. 🎯 Research Scope Assessment

### Scope Factors

```yaml
scope_factors:
  breadth:
    narrow: single technology/library
    moderate: 2-3 technologies
    broad: ecosystem/domain analysis

  depth:
    shallow: overview only
    moderate: implementation details
    deep: architectural patterns + edge cases

  sources:
    minimal: <5 sources required
    moderate: 5-15 sources
    extensive: >15 sources

  novelty:
    familiar: well-documented technology
    emerging: recent/evolving technology
    cutting_edge: experimental/new
```

### Scope Score Calculation

```python
def calculate_research_scope(factors):
    weights = {
        'breadth': 0.25,
        'depth': 0.30,
        'sources_needed': 0.25,
        'novelty': 0.20
    }

    score = 0
    for factor, value in factors.items():
        if value in ['narrow', 'shallow', 'minimal', 'familiar']:
            points = 1
        elif value in ['moderate', 'emerging']:
            points = 2
        else:
            points = 3
        score += points * weights[factor]

    return score * 33.33  # Normalize to 0-100
```

.

## 2. 📊 Signal Quality Assessment

### Signal Indicators

```yaml
signal_indicators:
  source_availability:
    high: >20 quality sources found
    medium: 10-20 sources found
    low: <10 sources found

  source_relevance:
    high: >80% on-topic
    medium: 50-80% on-topic
    low: <50% on-topic

  contradiction_level:
    low: <10% conflicting info
    medium: 10-25% conflicting
    high: >25% conflicting

  recency:
    current: <6 months old
    recent: 6-24 months
    dated: >24 months
```

### Signal Quality Score

```python
def calculate_signal_quality(indicators):
    weights = {
        'source_availability': 0.30,
        'source_relevance': 0.30,
        'contradiction_level': 0.25,
        'recency': 0.15
    }

    score = 0
    for indicator, value in indicators.items():
        if value in ['high', 'current']:
            points = 3
        elif value in ['medium', 'recent']:
            points = 2
        else:
            points = 1

        # Invert contradiction score
        if indicator == 'contradiction_level':
            points = 4 - points

        score += points * weights[indicator]

    return (score / 3) * 100  # Normalize to 0-100
```

.

## 3. 🔄 Adaptive Strategies

### Based on Research Scope

#### Narrow Scope (0-30)
```yaml
strategy:
  concurrency: 3
  query_depth: standard
  source_minimum: 5
  iterations: 1
  review_depth: basic
  synthesis: single_pass
```

#### Moderate Scope (31-70)
```yaml
strategy:
  concurrency: 3
  query_depth: thorough
  source_minimum: 10
  iterations: 1
  review_depth: thorough
  synthesis: comprehensive
  additions:
    - cross_validation
    - pattern_extraction
```

#### Broad Scope (71-100)
```yaml
strategy:
  concurrency: 2
  query_depth: exhaustive
  source_minimum: 20
  iterations: 2
  review_depth: exhaustive
  synthesis: multi_pass
  additions:
    - domain_mapping
    - trend_analysis
    - comparative_assessment
    - ecosystem_overview
```

### Based on Signal Quality

#### High Signal (>70)
```yaml
strategy:
  execution: standard_parallel
  source_expansion: minimal
  validation: standard
  documentation: comprehensive
  confidence: high
```

#### Medium Signal (40-70)
```yaml
strategy:
  execution: parallel_with_validation
  source_expansion: targeted
  validation: enhanced
  documentation: detailed
  additions:
    - secondary_sources
    - contradiction_resolution
    - confidence_scoring
```

#### Low Signal (<40)
```yaml
strategy:
  execution: broadened_parallel
  source_expansion: aggressive
  validation: extensive
  documentation: exhaustive
  additions:
    - query_broadening
    - alternative_angles
    - expert_sources
    - community_insights
    - gap_documentation
```

.

## 4. ⚙️ Execution Modes

### Mode 1: Comprehensive Research (Default)

```yaml
configuration:
  researchers: [web, docs, market, feasibility]
  parallelism: 3
  depth: thorough
  sources: 15-25
  review: complete
  synthesis: comprehensive
  when: scope < 70 AND signal > 40
```

### Mode 2: Focused Research

```yaml
configuration:
  researchers: [web, docs, feasibility]
  parallelism: 2
  depth: targeted
  sources: 10-15
  review: essential
  synthesis: targeted
  when: scope < 40 AND time_limited
```

### Mode 3: Discovery Research

```yaml
configuration:
  researchers: all + exploratory
  parallelism: 2
  depth: exploratory
  sources: 25+
  review: iterative
  synthesis: progressive
  when: signal < 30 OR novelty == cutting_edge
```

### Mode 4: Rapid Assessment

```yaml
configuration:
  researchers: [web, docs]
  parallelism: 2
  depth: overview
  sources: 5-10
  review: basic
  synthesis: quick
  when: time_critical OR initial_assessment
```

.

## 5. 🎚️ Dynamic Adjustments

### Runtime Monitoring

```python
class ResearchMonitor:
    def adjust_strategy(self, metrics):
        if metrics.source_quality < 0.4:
            self.broaden_queries()
            self.add_secondary_sources()

        if metrics.contradiction_rate > 0.3:
            self.add_reconciliation_pass()

        if metrics.findings_count < minimum:
            self.expand_search_scope()

        if metrics.relevance_score < 0.5:
            self.refine_queries()
```

### Progressive Enhancement

```yaml
enhancement_levels:
  level_1_quick:
    researchers: [web, docs]
    sources: 5-8
    depth: overview
    synthesis: basic

  level_2_standard:
    researchers: [web, docs, market]
    sources: 10-15
    depth: thorough
    synthesis: comprehensive

  level_3_deep:
    researchers: all
    sources: 15-25
    depth: exhaustive
    synthesis: detailed

  level_4_exhaustive:
    researchers: all + validators
    sources: 25+
    depth: comprehensive
    synthesis: multi_iteration
```

.

## 6. 🔧 Fallback Strategies

### Graceful Degradation Path

```
1. Full Parallel Research (4 agents)
   ↓ (low signal)
2. Broadened Queries (expanded scope)
   ↓ (still low)
3. Sequential Deep Dive (one domain at a time)
   ↓ (insufficient)
4. Secondary Sources (community, forums)
   ↓ (still gaps)
5. Document Gaps (explicit unknowns)
   ↓ (complete failure)
6. Manual Research Required
```

### Recovery Actions

```yaml
on_low_signal:
  - broaden_search_terms
  - include_synonyms
  - try_related_domains
  - search_case_studies
  - check_communities

on_high_contradiction:
  - document_conflicts
  - cite_all_perspectives
  - provide_comparison_matrix
  - flag_for_validation
  - suggest_proof_of_concept

on_missing_sources:
  - try_alternative_keywords
  - search_adjacent_topics
  - check_historical_approaches
  - document_gaps_explicitly
  - recommend_prototyping

on_paywall_blocking:
  - find_alternative_sources
  - use_preview_content
  - search_open_alternatives
  - cite_abstract_only
  - note_limitation
```

.

## 7. 🚀 Optimization Rules

### Query Optimization

```python
def optimize_queries(context):
    # Start specific, broaden if needed
    queries = []

    # Level 1: Specific
    queries.append(f"{context.technology} {context.use_case}")

    # Level 2: Technology focus
    if signal_low(queries):
        queries.append(f"{context.technology} best practices")
        queries.append(f"{context.technology} architecture")

    # Level 3: Broader domain
    if still_low(queries):
        queries.append(f"{context.domain} solutions")
        queries.append(f"{context.problem} approaches")

    return queries
```

### Source Quality Filtering

```python
def filter_sources(sources):
    quality_criteria = {
        'official_docs': 1.0,
        'reputable_blogs': 0.8,
        'stackoverflow': 0.7,
        'github_repos': 0.9,
        'academic_papers': 0.95,
        'random_blogs': 0.4
    }

    scored = [(s, quality_criteria.get(s.type, 0.5)) for s in sources]
    sorted_sources = sorted(scored, key=lambda x: x[1], reverse=True)

    return [s for s, score in sorted_sources if score > 0.6]
```

.

## 8. 📋 Configuration Examples

### Example 1: New Framework Research

```yaml
detected:
  scope: 75  # broad
  signal: 45  # medium
  novelty: cutting_edge
  time: adequate

applied_rules:
  concurrency: 2
  researchers: all
  depth: exhaustive
  sources: 20+
  review: iterative
  synthesis: multi_pass
  additions:
    - ecosystem_mapping
    - trend_analysis
```

### Example 2: Well-Known Library

```yaml
detected:
  scope: 25  # narrow
  signal: 85  # high
  novelty: familiar
  time: limited

applied_rules:
  concurrency: 3
  researchers: [web, docs]
  depth: standard
  sources: 8-10
  review: basic
  synthesis: single_pass
```

### Example 3: Uncertain Requirements

```yaml
detected:
  scope: 60  # moderate
  signal: 30  # low
  novelty: emerging
  time: adequate

applied_rules:
  concurrency: 2
  researchers: all
  depth: exploratory
  sources: 25+
  review: thorough
  synthesis: progressive
  additions:
    - query_broadening
    - alternative_perspectives
    - gap_documentation
```

.

## 9. 📈 Success Metrics

### Research Quality Metrics

```yaml
metrics:
  source_coverage:
    target: >80%
    measure: relevant_sources_found / expected_sources

  finding_relevance:
    target: >85%
    measure: on_topic_findings / total_findings

  contradiction_resolution:
    target: >90%
    measure: resolved_conflicts / total_conflicts

  citation_quality:
    target: >75%
    measure: high_quality_sources / total_sources

  gap_documentation:
    target: 100%
    measure: documented_gaps / identified_gaps
```

.

## 10. 🎯 YAML ADAPTIVE RULES MAPPING

This section maps the YAML `adaptive_rules` fields from `sk_p__feature_research.yaml` to concrete workflow behaviors.

### Rule: high_complexity

**YAML Configuration**:
```yaml
high_complexity:
  concurrency: 2
  review_depth: exhaustive
```

**Triggers**:
- Broad research scope (>10 research areas)
- Multiple competing solutions (>5 alternatives)
- Deep technical domain (specialized knowledge required)
- Research complexity score > 70

**Adaptations Applied**:
- **Reduce Concurrency**: `3 → 2` parallel researchers (fewer simultaneous executions)
- **Increase Review Depth**: `standard → exhaustive` (more thorough source validation)
- **Additional Domain Expert**: Add specialized researcher for complex areas
- **Extended Timeouts**: Allow more time for deep research

**Impact**:
- **Execution Time**: Longer (reduced parallelism, deeper research)
- **Quality**: Higher (exhaustive review validates sources better)
- **Resource Usage**: Lower peak usage (fewer concurrent researchers)

---

### Rule: low_signal (high_uncertainty for research)

**YAML Configuration**:
```yaml
low_signal:
  action: broaden_queries_and_include_secondary_sources
```

**Triggers**:
- Limited search results (<10 quality sources)
- Niche or emerging technology
- Contradictory findings (>30% conflicting sources)
- New research domain with sparse documentation

**Adaptations Applied**:
- **Broaden Search Queries**: Expand keywords and search terms
- **Include Secondary Sources**: Add blogs, forums, community discussions
- **Cross-Domain Research**: Look for analogous solutions in related fields
- **Document Gaps Explicitly**: Flag areas with insufficient evidence

**Impact**:
- **Execution Time**: Additional search rounds add time
- **Coverage**: Better breadth (secondary sources fill gaps)
- **Transparency**: Explicit gap documentation helps decision-making

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
- **Reduce to Sequential**: `concurrency → 1` (all researchers run one-by-one)
- **Preserve Phases**: Keep review and synthesis phases intact
- **Extend Timeouts**: Account for sequential execution duration
- **Simplified Monitoring**: Reduce overhead of parallel coordination

**Impact**:
- **Execution Time**: Significantly longer (3-4x sequential vs parallel)
- **Quality**: Same (review/synthesis phases preserved)
- **Resource Usage**: Minimal (single researcher at a time)

---

### Adaptive Rule Decision Tree

```
Start Research Workflow
    ↓
Check Research Complexity Score
    ↓
    ├─ >70? → Apply high_complexity rules
    └─ ≤70? → Continue
    ↓
Execute Initial Research Pass
    ↓
Check Signal Quality (sources found)
    ↓
    ├─ <10 quality sources? → Apply low_signal rules (broaden)
    └─ ≥10 sources? → Continue
    ↓
Check Parallel Support
    ↓
    ├─ Not supported? → Apply parallel_not_supported rules (sequential)
    └─ Supported? → Use default parallelism (concurrency=3)
    ↓
Execute Research with Adapted Configuration
```

---

### Rule Combination Matrix

| Complexity | Signal Quality | Parallel Support | Concurrency | Review Depth | Broaden Search |
|-----------|----------------|------------------|-------------|--------------|----------------|
| Low | High (>10 sources) | Yes | 3 | Standard | No |
| High | High (>10 sources) | Yes | 2 | Exhaustive | No |
| Low | Low (<10 sources) | Yes | 3 | Standard | Yes |
| High | Low (<10 sources) | Yes | 2 | Exhaustive | Yes |
| Any | Any | No | 1 | Standard/Exhaustive* | As needed |

*Review depth determined by complexity score

---

.

## 11. ✅ Best Practices

### DO:

- Start specific, broaden if needed
- Cite all significant sources
- Document contradictions explicitly
- Flag confidence levels
- Note research limitations

### DON'T:

- Ignore contradictory findings
- Rely on single source types
- Skip validation for critical claims
- Omit source citations
- Hide research gaps

### ALWAYS:

- Prioritize official documentation
- Cross-validate critical findings
- Document search methodology
- Provide source URLs
- Flag outdated information