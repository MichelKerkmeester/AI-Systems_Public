# Feature Research Sub-Agents - Specialized Responsibilities and Coordination

Sub-agent roles for feature research and the required research artifacts.

---

## 1. 🔍 Web/Ecosystem Researcher

**Role**: Investigate libraries, frameworks, and ecosystem patterns

**Responsibilities**:
- Search for relevant libraries and frameworks
- Analyze GitHub repositories and issues
- Identify community patterns and best practices
- Evaluate ecosystem maturity and trends
- Collect implementation examples

**Research Domains**:
- GitHub repositories
- NPM/package registries
- Stack Overflow discussions
- Developer forums
- Blog posts and tutorials

**Output Format**:
```yaml
findings:
  - title: "Library/Framework Name"
    url: "https://github.com/..."
    quote: "Key feature or description"
    finding: "How this solves the problem"
    assessment: "Pros and cons analysis"
    confidence: "high/medium/low"
    metrics:
      stars: number
      downloads: number
      last_updated: date
      issues: count
```

**Quality Criteria**:
- Recent and maintained projects
- Community adoption metrics
- Documentation quality
- License compatibility
- Security considerations

.

## 2. 📚 Academic/Docs Researcher

**Role**: Research standards, RFCs, and official documentation

**Responsibilities**:
- Find relevant standards and specifications
- Analyze RFC documents
- Extract canonical patterns
- Review official documentation
- Identify technical constraints

**Research Domains**:
- W3C specifications
- IETF RFCs
- MDN documentation
- Official API docs
- Academic papers
- Technical standards

**Output Format**:
```yaml
findings:
  - title: "Standard/Specification Name"
    url: "https://www.w3.org/..."
    quote: "Authoritative requirement"
    finding: "Technical constraint or pattern"
    assessment: "Implementation implications"
    confidence: "high"
    metadata:
      specification: name
      version: number
      status: draft/recommendation
      date: publication_date
```

**Quality Criteria**:
- Authoritative sources only
- Current specifications
- Implementation support
- Browser compatibility
- Standards compliance

.

## 3. 🏪 Competitive/Market Analyst

**Role**: Analyze vendor solutions and market alternatives

**Responsibilities**:
- Research commercial solutions
- Analyze competitor implementations
- Benchmark performance metrics
- Identify market trends
- Evaluate pricing models

**Research Domains**:
- Vendor websites
- Product comparisons
- Benchmark reports
- Market analysis
- Case studies
- Customer reviews

**Output Format**:
```yaml
findings:
  - title: "Vendor/Product Name"
    url: "https://vendor.com/..."
    quote: "Key differentiator"
    finding: "Competitive advantage"
    assessment: "Market position analysis"
    confidence: "medium/high"
    comparison:
      features: [list]
      pricing: model
      performance: metrics
      adoption: market_share
```

**Quality Criteria**:
- Current market data
- Verified benchmarks
- Feature completeness
- Integration capabilities
- Total cost of ownership

.

## 4. 💰 Feasibility/Cost Analyst

**Role**: Evaluate technical complexity and operational costs

**Responsibilities**:
- Assess implementation complexity
- Calculate operational costs
- Identify technical risks
- Analyze trade-offs
- Estimate resource requirements

**Research Focus**:
- Technical complexity metrics
- Infrastructure requirements
- Operational overhead
- Maintenance burden
- Scalability limits

**Output Format**:
```yaml
analysis:
  complexity:
    implementation: "low/medium/high"
    maintenance: "low/medium/high"
    testing: "low/medium/high"
  costs:
    development_hours: range
    infrastructure: monthly_estimate
    licensing: cost_structure
    operational: ongoing_costs
  risks:
    - type: "technical/operational/security"
      severity: "low/medium/high/critical"
      mitigation: "strategy"
      likelihood: percentage
  trade_offs:
    - option: description
      pros: [list]
      cons: [list]
      recommendation: rationale
```

**Quality Criteria**:
- Data-driven estimates
- Risk quantification
- Clear trade-offs
- Mitigation strategies
- ROI analysis

.

## 5. 🔄 Lead Reviewer

**Role**: Consolidate and validate research findings

**Responsibilities**:
- Deduplicate findings across researchers
- Rank by relevance and impact
- Identify contradictions
- Validate citations
- Provide synthesis guidance

**Review Process**:
1. **Deduplication**
   - Identify overlapping findings
   - Merge related insights
   - Preserve unique perspectives

2. **Ranking**
   - Relevance to requirements
   - Technical merit
   - Implementation impact
   - Risk factors

3. **Contradiction Resolution**
   - Flag conflicting information
   - Document different viewpoints
   - Provide reconciliation

4. **Citation Validation**
   - Verify source credibility
   - Check link validity
   - Confirm quote accuracy

**Output Format**:
```yaml
review_summary:
  total_findings: count
  deduplicated: count
  high_relevance: count
  contradictions:
    - finding_a: reference
      finding_b: reference
      resolution: explanation
  synthesis_guidance:
    priority_findings: [ordered list]
    key_themes: [list]
    gaps_identified: [list]
  quality_score: percentage
```

.

## 6. ✍️ Lead Synthesizer

**Role**: Create comprehensive research.md document

**Responsibilities**:
- Generate structured markdown document
- Organize findings by section
- Integrate all research
- Ensure narrative flow
- Format for readability

**Document Structure Template**:

The Lead Synthesizer produces a research.md document following this structure. Each section below represents the output document structure, not additional sub-agent sections:

```markdown
# Research Documentation
Specialized Sub-Agent Specifications

[High-level overview]

## 🧭 Investigation Report

### Request Summary
### Current Behavior
### Key Findings
### Recommendations

## 🏗️ Architecture Analysis

### System Components
### Data Flow
### Integration Points

## 📋 Technical Specifications

[Detailed specs]

## 📖 Implementation Guide

[Step-by-step guidance]

## ⚠️ Constraints & Limitations

[Platform limitations]

## 🧪 Testing Strategy

[Test approaches]

## 📊 Performance Analysis

[Benchmarks and optimization]

## 🔒 Security Considerations

[Security analysis]

## 📚 References

[All citations]
```

**Synthesis Rules**:
- Maintain objectivity
- Include all perspectives
- Highlight critical findings
- Document uncertainties
- Provide clear recommendations

**Quality Standards**:
- Comprehensive coverage
- Logical organization
- Clear writing
- Proper citations
- Actionable insights

.

## 7. 🔗 Agent Coordination

### Execution Flow

```
1. PARALLEL PHASE (45-60 seconds)
   ├─ Web Researcher: Ecosystem investigation
   ├─ Docs Researcher: Standards research
   ├─ Market Analyst: Competitive analysis
   └─ Feasibility Analyst: Cost/complexity

2. REVIEW PHASE (15-20 seconds)
   └─ Lead Reviewer: Consolidation & validation

3. SYNTHESIS PHASE (20-30 seconds)
   └─ Lead Synthesizer: Document generation

4. QA PHASE (10-15 seconds)
   └─ Main Agent: Final review & polish
```

### Communication Protocol

Agents communicate findings using structured format:

```yaml
agent_output:
  agent_id: "web|docs|market|feasibility"
  timestamp: ISO-8601
  findings_count: number
  confidence_average: percentage
  findings: [array of findings]
  metadata:
    sources_checked: count
    time_spent: seconds
    issues_encountered: [list]
```

### Quality Metrics

Each agent must meet minimum quality thresholds:

- **Finding count**: Minimum 5 relevant findings
- **Citation rate**: 100% of findings cited
- **Confidence average**: >70% high/medium confidence
- **Execution time**: Within timeout limits
- **Error rate**: <10% failed searches

## 8. ⚠️ Error Handling

### Agent-Level Errors

**Search Failures**:
- Retry with broader terms
- Use alternative sources
- Document search gaps

**Timeout Handling**:
- Save partial results
- Continue with available data
- Note incomplete areas

**Quality Issues**:
- Low finding count → Expand search
- Low confidence → Seek additional sources
- Contradictions → Document all viewpoints

### System-Level Errors

**Parallel Execution Failure**:
- Fallback to sequential
- Maintain phases
- Document degradation

**Review/Synthesis Failure**:
- Use partial results
- Manual intervention
- Error documentation

## 9. ✅ Success Criteria

### Individual Agent Success

- **Web Researcher**: 10+ relevant libraries/repos
- **Docs Researcher**: 5+ authoritative sources
- **Market Analyst**: 3+ vendor solutions
- **Feasibility Analyst**: Complete assessment
- **Lead Reviewer**: <5% contradictions unresolved
- **Lead Synthesizer**: All sections populated

### Overall Success

- **Coverage**: >80% research areas addressed
- **Quality**: >85% findings high/medium confidence
- **Completeness**: No critical gaps
- **Timeliness**: <5 minutes total execution
