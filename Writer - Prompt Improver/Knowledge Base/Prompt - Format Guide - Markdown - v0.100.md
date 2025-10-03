# Prompt - Markdown Format Guide - v0.100

Comprehensive guide for Markdown (Standard) output structure in prompt engineering with RCAF/CRAFT frameworks, CLEAR scoring, artifact delivery standards, and optimization strategies.

---

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 MARKDOWN FORMAT FUNDAMENTALS](#-markdown-format-fundamentals)
3. [📦 ARTIFACT DELIVERY STANDARDS](#-artifact-delivery-standards)
4. [🔧 RCAF MARKDOWN STRUCTURE](#-rcaf-markdown-structure)
5. [🎨 CRAFT MARKDOWN STRUCTURE](#-craft-markdown-structure)
6. [📄 ADVANCED MARKDOWN PATTERNS](#-advanced-markdown-patterns)
7. [🔄 FORMAT CONVERSIONS](#-format-conversions)
8. [⚖️ MARKDOWN VS OTHER FORMATS](#-markdown-vs-other-formats)
9. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
10. [📊 TRANSPARENCY REPORTING](#-transparency-reporting)
11. [📈 PERFORMANCE METRICS](#-performance-metrics)
12. [🔧 TROUBLESHOOTING](#-troubleshooting)
13. [🎓 BEST PRACTICES](#-best-practices)

---

<a id="-overview--purpose"></a>

## 1. 🎯 OVERVIEW & PURPOSE

### Why Markdown (Standard) Format?

Markdown format provides natural language prompt engineering with optimal human readability while maintaining clear structure through RCAF/CRAFT frameworks.

**Terminology Clarification:**
- **Framework** = Prompt organization method (RCAF vs CRAFT)
- **Output Structure** = Data format (Standard/Markdown vs JSON vs YAML)
- **Standard Format** = Markdown-based natural language structure

**Markdown Format Benefits:**
- **Natural Language:** Conversational flow
- **Human Readable:** Immediate comprehension
- **Flexible Structure:** Adapts to complexity
- **Minimal Overhead:** Baseline token usage
- **Direct Communication:** Clear intent expression

### Format Comparison Summary

| Aspect | Markdown (Standard) | JSON | YAML |
|--------|-------------------|------|------|
| **Readability** | Natural language | Structured data | Human-friendly structure |
| **Token Usage** | Baseline (100%) | +5-10% | +3-7% |
| **CLEAR Score** | 43/50 avg | 41/50 avg | 42/50 avg |
| **Best For** | Human interaction | API integration | Configuration |
| **Framework Fit** | RCAF/CRAFT equal | RCAF preferred | RCAF optimal |
| **Learning Curve** | None | Medium | Low |

---

<a id="-markdown-format-fundamentals"></a>

## 2. 📊 MARKDOWN FORMAT FUNDAMENTALS

### Core Markdown Principles

1. **Clarity First:** Every word must earn its place
2. **Natural Flow:** Conversational structure
3. **Semantic Headers:** Clear section delineation
4. **Concise Expression:** Maximum clarity, minimum tokens
5. **Action-Oriented:** Focus on what needs to be done

### Basic Markdown Prompt Structure

```markdown
**Role:** [Specific expertise needed]
**Context:** [Essential background information]
**Action:** [Clear, measurable task]
**Format:** [Expected output structure]
```

### Markdown Elements for Prompts

| Element | Use Case | Example |
|---------|----------|---------|
| **Bold Headers** | Section markers | `**Role:** Data Analyst` |
| **Bullet Lists** | Multiple requirements | `- Requirement 1` |
| **Numbered Lists** | Sequential steps | `1. First step` |
| **Inline Code** | Technical terms | `` `API endpoint` `` |
| **Block Quotes** | Context emphasis | `> Important note` |

---

<a id="-artifact-delivery-standards"></a>

## 3. 📦 ARTIFACT DELIVERY STANDARDS

### 🔴 CRITICAL REQUIREMENTS

#### Mandatory Artifact Delivery
- **EVERY enhancement MUST be in artifact format**
- **NEVER deliver prompts in chat**
- **If artifact creation fails, STOP and retry**
- **Always use `text/markdown` type**
- **NEVER use `text/plain` (causes raw display issues)**

#### Mandatory Minimal Header Format

**Single-line header at TOP of every artifact:**
```
Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50
```

**Header Requirements:**
- **Mode with $ prefix:** $improve, $refine, $quick, etc.
- **Complexity level:** Low/Medium/High or 1-10
- **Framework used:** RCAF or CRAFT
- **CLEAR score:** Target ≥40/50

#### Artifact Content Structure

**ONLY these two components in artifact:**
1. **Single-line header** (with $ prefix)
2. **Enhanced prompt content**

**FORBIDDEN in artifacts:**
- ❌ Format Options section
- ❌ CLEAR Evaluation breakdown
- ❌ Processing Applied section
- ❌ Additional metadata sections
- ❌ Explanations or commentary
- ✅ All explanations go in CHAT after delivery

### Pre-Delivery Validation

```python
def validate_markdown_artifact():
    """MANDATORY validation before delivery"""
    
    checks = {
        'artifact_type': self.type == 'text/markdown',
        'artifact_created': self.artifact is not None,
        'header_present': self.has_single_line_header,
        'header_format': self.header_has_dollar_prefix,
        'no_extra_sections': self.has_only_header_and_content,
        'clear_scored': self.clear_score >= 35,
        'clear_target': self.clear_score >= 40
    }
    
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise ArtifactError(f"CANNOT DELIVER. Failed: {failed}")
        
    return True
```

---

<a id="-rcaf-markdown-structure"></a>

## 4. 🔧 RCAF MARKDOWN STRUCTURE

### Standard RCAF Template

```markdown
**Role:** [Specific expertise definition]
**Context:** [Essential background information]
**Action:** [Clear measurable task]
**Format:** [Expected output requirements]
```

### RCAF Markdown Examples

#### Simple Analysis Task

**Delivered as artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 44/50

**Role:** Financial analyst specializing in SaaS metrics and growth analysis.
**Context:** Q4 2024 revenue data from B2B platform with 10,000 customers, focusing on subscription trends.
**Action:** Calculate MRR growth rate, identify top 3 revenue trends, and provide actionable insights.
**Format:** Executive summary (500 words) with key metrics, trend charts, and 3-5 strategic recommendations.
```

#### Content Creation Task

**Delivered as artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

**Role:** Technical writer with API documentation expertise and developer experience focus.
**Context:** REST API with 15 endpoints for payment processing, OAuth 2.0 authentication, versioned at v2.1.
**Action:** Create comprehensive API documentation including authentication flow, endpoint specifications, and integration examples.
**Format:** Developer-friendly markdown with overview, authentication guide, endpoint reference, code examples, and troubleshooting section.
```

### RCAF Field Guidelines

| Field | Required | Description | Best Practices |
|-------|----------|-------------|----------------|
| **Role** | Yes | Expertise needed | Be specific about domain and skills |
| **Context** | Yes | Essential background | Include constraints and scope |
| **Action** | Yes | Task to perform | Make measurable and specific |
| **Format** | Yes | Output structure | Define sections and length |

---

<a id="-craft-markdown-structure"></a>

## 5. 🎨 CRAFT MARKDOWN STRUCTURE

### Standard CRAFT Template

```markdown
**Context:** [Comprehensive background and constraints]
**Role:** [Detailed expertise and perspective]
**Action:** [Primary task with subtasks and deliverables]
**Format:** [Detailed output specifications]
**Target:** [Success metrics and criteria]
```

### CRAFT Markdown Examples

#### Complex Analysis Task

**Delivered as artifact:**
```
Mode: $refine | Complexity: High | Framework: CRAFT | CLEAR: 45/50

**Context:** E-commerce platform experiencing 15% cart abandonment rate over the last 6 months. Available data includes user session logs, transaction records, and customer surveys. Must comply with GDPR and deliver within 30 days.

**Role:** UX researcher with e-commerce specialization, applying user-centric analysis methodology using behavioral analytics and qualitative research techniques.

**Action:** Identify root causes of cart abandonment through multi-method analysis:
- Analyze user behavior patterns across abandonment stages
- Segment users by abandonment point and demographics
- Correlate quantitative findings with survey responses
- Generate prioritized recommendations for reducing abandonment

**Format:** Research report (2500 words) structured as:
- Executive summary with key findings
- Methodology overview
- Detailed findings with visualizations (flow diagrams, heat maps)
- Actionable recommendations ranked by impact/effort

**Target:** Deliver insights that enable 20% reduction in abandonment rate within Q1 2025, with specific KPIs for each recommendation.
```

### CRAFT vs RCAF Decision Matrix

| Use CRAFT When | Use RCAF When |
|----------------|---------------|
| Multiple success metrics needed | Single clear outcome |
| Complex multi-stakeholder scenarios | Straightforward task |
| Detailed specifications required | Flexibility preferred |
| Comprehensive documentation needed | Quick clarity needed |

---

<a id="-advanced-markdown-patterns"></a>

## 6. 📄 ADVANCED MARKDOWN PATTERNS

### Multi-Step Process Pattern

**Delivered as artifact:**
```
Mode: $improve | Complexity: High | Framework: RCAF | CLEAR: 44/50

**Role:** Project coordinator with software deployment expertise.

**Context:** Enterprise client deployment for cloud-based CRM system, 500+ users, multiple departments, requiring zero downtime migration.

**Action:** Execute three-phase deployment process:

**Phase 1 - Environment Preparation:**
- Validate infrastructure requirements
- Configure staging environment
- Create rollback procedures
- Output: Readiness checklist and validation report

**Phase 2 - Deployment Execution:**
- Migrate data in batches
- Deploy application components
- Run integration tests
- Output: Deployment log and test results

**Phase 3 - Post-Deployment Validation:**
- Monitor system performance
- Gather user feedback
- Address immediate issues
- Output: Performance metrics and optimization recommendations

**Format:** Status report per phase with traffic light indicators, plus comprehensive summary document with lessons learned.
```

### Conditional Logic Pattern

```markdown
**Role:** Customer service specialist with technical troubleshooting skills.

**Context:** First-line support for software platform with varied user base.

**Action:** Classify and route support tickets using decision tree:

If technical issue detected (error messages, system behavior):
  → Route to: Engineering team
  → Priority: Assess based on severity indicators
  → Include: Full error logs and reproduction steps

If billing/payment related:
  → Route to: Finance team  
  → Priority: High (affects revenue)
  → Include: Account details and transaction IDs

If general inquiry or how-to question:
  → Route to: Support Tier 1
  → Priority: Standard queue
  → Include: User context and previous tickets

**Format:** Routing decision with department assignment, priority level, and brief rationale (50 words max).
```

---

<a id="-format-conversions"></a>

## 7. 🔄 FORMAT CONVERSIONS

### Markdown to JSON Conversion

```python
def markdown_to_json(markdown_prompt):
    """Convert RCAF markdown to JSON format"""
    
    import re
    import json
    
    # Parse RCAF elements using bold markers
    pattern = r'\*\*(\w+):\*\*\s*([^\*]+?)(?=\*\*\w+:|\Z)'
    matches = re.findall(pattern, markdown_prompt, re.DOTALL)
    
    rcaf_dict = {}
    for key, value in matches:
        rcaf_dict[key.lower()] = value.strip()
    
    return json.dumps(rcaf_dict, indent=2)
```

### Markdown to YAML Conversion

```python
def markdown_to_yaml(markdown_prompt):
    """Convert RCAF markdown to YAML format"""
    
    import re
    import yaml
    
    pattern = r'\*\*(\w+):\*\*\s*([^\*]+?)(?=\*\*\w+:|\Z)'
    matches = re.findall(pattern, markdown_prompt, re.DOTALL)
    
    rcaf_dict = {}
    for key, value in matches:
        rcaf_dict[key.lower()] = value.strip()
    
    return yaml.dump(rcaf_dict, default_flow_style=False)
```

### Conversion Examples

**Original Markdown:**
```markdown
**Role:** Data analyst with SQL expertise.
**Context:** Sales database with 5 years of transaction data.
**Action:** Identify top performing products by region.
**Format:** Dashboard with charts and executive summary.
```

**JSON Equivalent:**
```json
{
  "role": "Data analyst with SQL expertise",
  "context": "Sales database with 5 years of transaction data",
  "action": "Identify top performing products by region",
  "format": "Dashboard with charts and executive summary"
}
```

**YAML Equivalent:**
```yaml
role: Data analyst with SQL expertise
context: Sales database with 5 years of transaction data
action: Identify top performing products by region
format: Dashboard with charts and executive summary
```

---

<a id="-markdown-vs-other-formats"></a>

## 8. ⚖️ MARKDOWN VS OTHER FORMATS

### Format Selection Matrix

| Factor | Choose Markdown | Choose JSON | Choose YAML |
|--------|----------------|-------------|-------------|
| **Audience** | Humans | Machines/APIs | Configurations |
| **Complexity** | Any level | Structured only | Hierarchical |
| **Flexibility** | High | Low | Medium |
| **Readability** | Excellent | Fair | Good |
| **Token Efficiency** | Best | Lower | Medium |
| **Integration** | Manual | Automated | Semi-automated |

### CLEAR Score Impact by Format

| Format | Avg CLEAR | Strengths | Weaknesses |
|--------|-----------|-----------|------------|
| **Markdown** | 43/50 | Expression (9/10), Flexibility | Parsing consistency |
| **JSON** | 41/50 | Arrangement (9/10), Precision | Expression (7/10) |
| **YAML** | 42/50 | Balance (8/10 avg) | Special character handling |

---

<a id="-examples--templates"></a>

## 9. 💡 EXAMPLES & TEMPLATES

### Template Library

#### Research Template

**Delivered as artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

**Role:** Research analyst with expertise in [DOMAIN].
**Context:** Investigating [RESEARCH_QUESTION] within [SCOPE] using [AVAILABLE_RESOURCES].
**Action:** Conduct systematic research using [METHODOLOGY] to identify [KEY_FINDINGS] and develop [DELIVERABLES].
**Format:** Research paper with abstract, methodology, findings, and recommendations, approximately [LENGTH] words.
```

#### Analysis Template

**Delivered as artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

**Role:** Data analyst specializing in [DOMAIN].
**Context:** Dataset containing [DATA_DESCRIPTION] from [TIME_PERIOD] with [CONSTRAINTS].
**Action:** Analyze [METRICS] to identify [INSIGHTS_TYPE] and provide [RECOMMENDATIONS_COUNT] actionable recommendations.
**Format:** [OUTPUT_TYPE] including visualizations ([CHART_TYPES]) and executive summary.
```

---

<a id="-transparency-reporting"></a>

## 10. 📊 TRANSPARENCY REPORTING

### After Every Markdown Enhancement

**Required in CHAT after artifact delivery:**

```markdown
📊 **Enhancement Report:**

**Complexity Assessment:** Level [X]/10
- [Reasoning for complexity level]

**DEPTH Processing Applied:**
✅ DISCOVER (Rounds 1-2): [What was analyzed]
✅ ENGINEER (Rounds 3-5): [Framework decisions]
✅ PROTOTYPE (Rounds 6-7): [Structure built]
✅ TEST (Rounds 8-9): [Validation performed]
✅ HARMONIZE (Round 10): [Final polish applied]

**Key Improvements:**
1. [Specific improvement #1]: [Impact/reasoning]
2. [Specific improvement #2]: [Impact/reasoning]
3. [Specific improvement #3]: [Impact/reasoning]

**CLEAR Scoring:**
- Correctness: [X]/10 - [what this means]
- Logic/Coverage: [X]/10 - [assessment]
- Expression: [X]/10 - [clarity level]
- Arrangement: [X]/10 - [structure quality]
- Reuse: [X]/10 - [adaptability]
**Total: [X]/50 (Grade: [A-F])**

**Framework Selection:** [RCAF/CRAFT]
- Reasoning: [Why this framework was optimal]

**Structure Choice:** Markdown/Standard
- Reasoning: Natural language best for human interaction
```

---

<a id="-performance-metrics"></a>

## 11. 📈 PERFORMANCE METRICS

### Markdown Format Performance

| Metric | Target | Current Average |
|--------|--------|-----------------|
| **Readability Score** | >90% | 94% |
| **Token Efficiency** | Baseline | 100% |
| **CLEAR Score (base)** | >40/50 | 43/50 |
| **CLEAR with DEPTH** | >45/50 | 48/50 |
| **User Comprehension** | >95% | 97% |
| **Artifact Delivery** | 100% | 100% |
| **Header Compliance** | 100% | 100% |

---

<a id="-troubleshooting"></a>

## 12. 🔧 TROUBLESHOOTING

### Common Issues & Solutions

| Issue | Recognition | Solution |
|-------|------------|----------|
| **Not artifact** | Chat delivery | Force artifact creation |
| **Wrong type** | text/plain used | Change to text/markdown |
| **Missing header** | No metadata line | Add single-line header |
| **Header format** | Missing $ prefix | Add $ to mode |
| **Extra sections** | Explanations in artifact | Move to chat |
| **Low CLEAR** | Score <35/50 | Apply more DEPTH rounds |

### REPAIR Protocol

```markdown
**R** - Recognize: Issue identified
**E** - Explain: Impact on delivery
**P** - Propose: Solution approach
**A** - Apply: Fix implemented
**I** - Iterate: Verify correction
**R** - Record: Note in transparency report
```

---

<a id="-best-practices"></a>

## 13. 🎓 BEST PRACTICES

### Markdown Excellence Guidelines

#### Do's ✅
- Use bold for section headers
- Keep paragraphs concise
- Use lists for multiple items
- Include specific examples
- Define measurable outcomes
- Maintain conversational tone
- Validate before delivery
- Always use artifact format
- Include minimal header with $
- Provide transparency in chat

#### Don'ts ❌
- Don't over-format
- Don't use complex markdown
- Don't embed code blocks unnecessarily
- Don't include metadata in content
- Don't deliver in chat
- Don't skip validation
- Don't add extra artifact sections
- Don't hide the process

### Quality Checklist

**Before Delivery:**
- [ ] Artifact type is `text/markdown`
- [ ] Single-line header present
- [ ] Mode has $ prefix
- [ ] CLEAR score ≥40/50
- [ ] Framework clearly applied
- [ ] All RCAF/CRAFT elements included
- [ ] Language is clear and specific
- [ ] Output format well-defined
- [ ] No extra sections in artifact
- [ ] Transparency report ready

### The Markdown Philosophy

> "Natural language is the universal interface. Markdown provides structure without sacrificing humanity."

**Core Principles:**
1. **Clarity through simplicity** - Direct communication
2. **Structure through convention** - Consistent patterns
3. **Flexibility through natural language** - Adaptable expression
4. **Efficiency through minimalism** - No wasted tokens
5. **Quality through validation** - Always verified
6. **Transparency through explanation** - Process visible

### Success Criteria

**Excellent Markdown Prompt:**
- ✅ Clear role definition
- ✅ Complete context
- ✅ Specific, measurable action
- ✅ Well-defined format
- ✅ CLEAR score >43/50
- ✅ Delivered as artifact
- ✅ Minimal header with $
- ✅ Full transparency report
- ✅ Natural readability
- ✅ Immediate usability