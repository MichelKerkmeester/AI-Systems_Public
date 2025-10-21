# Parallel Research Orchestration - Parallel Execution Stages and Dependencies

Parallel orchestration for research with clear stage flow, review gates, and approval.

---

## 1. 🎯 Stage Overview

The research workflow contains one major parallel execution block:

**Research Stage** (Step 3) - Parallel multi-source research collection

This stage follows a specific execution pattern optimized for research gathering and synthesis

.

## 2. ⚙️ Execution Pattern

### 2.1 Parallel Research Phase

```
Launch →
T0: Launch all research agents simultaneously
    ├─ Web/Ecosystem Researcher: Start
    ├─ Academic/Docs Researcher: Start
    ├─ Competitive/Market Analyst: Start
    └─ Feasibility/Cost Analyst: Start

Collect →
    ├─ Web: Gathering libraries, repos, patterns...
    ├─ Docs: Collecting standards, RFCs, papers...
    ├─ Market: Analyzing vendors, alternatives...
    └─ Feasibility: Assessing complexity, costs...

Complete →
    ├─ Web: ✓ (findings_1)
    ├─ Docs: ✓ (findings_2)
    ├─ Market: ✓ (findings_3)
    └─ Feasibility: ✓ (findings_4)
```

**Rules**:
- Maximum concurrency: 3 (configurable)
- Retry on failure: 2 attempts
- Continue with partial results if needed
- Minimum viable: 2 of 4 researchers

### 2.2 Review Phase

```
Inputs: [web_findings, docs_findings, market_findings, feasibility_findings]
    ↓
Lead Reviewer:
- Deduplicate sources
- Rank by relevance
- Identify contradictions
- Flag citation gaps
- Quality assessment
    ↓
Output: synthesis_guidance + ranked_findings + contradictions
```

**Rules**:
- Single reviewer consolidates all research
- Must wait for all parallel researchers
- Can proceed with 50% research coverage
- Focus: Contradiction resolution

### 2.3 Synthesis Phase

```
Inputs: [all_findings, review_guidance, ranked_sources]
    ↓
Lead Synthesizer:
- Create research.md document
- Organize by sections
- Integrate findings
- Document gaps
- Provide recommendations
    ↓
Output: research.md
```

**Rules**:
- Single synthesizer creates document
- Must wait for review phase
- Creates comprehensive research artifact
- Follows required section structure

### 2.4 Main Agent QA Phase

```
Inputs: [research.md]
    ↓
Main Agent:
- Validate alignment with request
- Check completeness
- Verify citations present
- Resolve open questions
- Final polish
    ↓
Output: final_research.md + signoff
```

**Rules**:
- Main agent has final authority
- Ensures all sections present
- Validates research quality
- Can request additional research

.

## 3. 📊 Research Stage Details

**Parallel Researchers** (Step 3):

1. **Web/Ecosystem Researcher**
   - Focus: Libraries, frameworks, repos, community patterns
   - Output: Ecosystem findings with pros/cons
   - Sources: GitHub, npm, package registries, forums

2. **Academic/Docs Researcher**
   - Focus: Standards, RFCs, official docs, papers
   - Output: Canonical patterns and constraints
   - Sources: MDN, W3C, RFCs, academic databases

3. **Competitive/Market Analyst**
   - Focus: Vendors, alternatives, benchmarks
   - Output: Comparison matrix
   - Sources: Vendor sites, benchmark tools, case studies

4. **Feasibility/Cost Analyst**
   - Focus: Complexity, operational costs, risks
   - Output: Viability assessment
   - Sources: Technical docs, cost calculators, case studies

**Review**: Lead Reviewer
- Focus: Source quality and relevance
- Priority: Contradiction resolution
- Key output: Ranked, deduplicated findings

**Synthesis**: Lead Synthesizer
- Creates: research.md (comprehensive document)
- Focus: Structured knowledge capture
- Structure: Problem → Options → Recommendations

**QA Check**: Main Agent
- Validates: Research coverage and quality
- Ensures: All required sections present
- Resolves: Open questions and gaps

.

## 4. 🔍 Orchestration Implementation

### 4.1 Coordinator Pattern

```python
class ResearchCoordinator:
    def execute_research(self, research_config):
        # 1. Launch parallel researchers
        researcher_futures = []
        for researcher in research_config.parallel_researchers:
            future = self.launch_researcher(researcher)
            researcher_futures.append(future)

        # 2. Collect research results
        findings = self.collect_findings(
            researcher_futures,
            min_success_ratio=0.50
        )

        # 3. Review phase (deduplicate & rank)
        review_output = self.run_reviewer(
            research_config.reviewer,
            findings
        )

        # 4. Synthesis phase (create research.md)
        research_doc = self.run_synthesizer(
            research_config.synthesizer,
            findings + review_output
        )

        # 5. Main agent QA
        final_research = self.main_agent_qa(
            research_doc,
            original_request
        )

        return final_research
```

### 4.2 Error Handling

```python
def handle_researcher_failure(self, researcher, error):
    # 1. Retry with different queries
    for attempt in range(2):
        try:
            return self.retry_researcher(
                researcher,
                broaden_queries=True
            )
        except:
            continue

    # 2. Mark as partial failure
    return PartialFindings(researcher.id, error)

def handle_low_signal(self, findings):
    # 1. Check if we have minimum viable research
    if self.has_minimum_findings(findings):
        return self.continue_with_partial(findings)

    # 2. Broaden search scope
    if self.can_broaden_scope():
        return self.run_with_broader_queries()

    # 3. Document gaps explicitly
    return self.document_research_gaps(findings)
```

.

## 5. 📈 Performance Optimization

### 5.1 Concurrency Control

```yaml
concurrency_limits:
  default: 3
  broad_scope: 2
  narrow_scope: 4

  per_researcher:
    web: 3  # I/O-bound
    docs: 2  # API rate limits
    market: 2  # Web scraping
    feasibility: 3  # Analysis-heavy
```

### 5.2 Query Optimization

```yaml
query_strategy:
  initial_precision: high
  fallback_breadth: medium_to_broad
  retry_variations: enabled

  per_researcher:
    web:
      queries: 3-5
      depth: thorough
    docs:
      queries: 2-3
      depth: canonical_only
    market:
      queries: 3-4
      depth: comparison_focused
    feasibility:
      queries: internal_analysis
      depth: comprehensive
```

.

## 6. 📡 Monitoring & Telemetry

### 6.1 Research Metrics

```yaml
research_metrics:
  - findings_count
  - source_quality_score
  - citation_coverage
  - contradiction_rate
  - gap_documentation_rate
```

### 6.2 Researcher Metrics

```yaml
researcher_metrics:
  - sources_found
  - relevance_score
  - citation_quality
  - retry_attempts
  - query_modifications
```

### 6.3 Quality Metrics

```yaml
quality_metrics:
  - research_completeness
  - source_diversity
  - contradiction_resolution_rate
  - actionable_recommendations
```

.

## 7. 🔄 Adaptive Rules

### 7.1 Low Signal Handling

When findings < minimum_threshold:
```yaml
adjustments:
  broaden_queries: true
  include_secondary_sources: true
  extend_search_domains: true
  document_gaps: explicit
  reduce_precision: increase_recall
```

### 7.2 High Contradiction Handling

When contradiction_rate > 25%:
```yaml
adjustments:
  add_reconciliation_pass: true
  document_all_perspectives: true
  create_comparison_matrix: true
  flag_for_validation: true
  provide_context: all_sources
```

### 7.3 Scope Adaptation

When scope = broad:
```yaml
adjustments:
  concurrency: 2
  query_depth: exhaustive
  sources_minimum: 20+
  iterations: 2
  synthesis: multi_pass
```

.

## 8. 🔗 Research Dependencies

### 8.1 Input Requirements

```yaml
research_requires:
  - request (feature description)
  - context (domain/problem)
  - spec_folder (output location)
  optional:
    - existing_research
    - constraints
    - preferred_sources
```

### 8.2 Output Contract

```yaml
research_produces:
  required:
    - research.md (comprehensive documentation)
  sections:
    - investigation_report
    - overview
    - core_architecture
    - technical_specifications
    - constraints_limitations
    - integration_patterns
    - implementation_guide
    - code_examples
    - testing_debugging
    - performance
    - security
    - maintenance
    - api_reference
    - troubleshooting
```

.

## 9. ✅ Best Practices

### 9.1 DO:

- Start specific, broaden if needed
- Cite all significant sources
- Document contradictions explicitly
- Flag confidence levels
- Note research limitations

### 9.2 DON'T:

- Ignore contradictory findings
- Rely on single source types
- Skip validation for critical claims
- Omit source citations
- Hide research gaps

### 9.3 CONSIDER:

- Caching research for similar queries
- Progressive search refinement
- Source quality scoring
- Multi-pass synthesis for complex topics
- Expert source prioritization
