# Prompt - JSON Format Guide - v0.110

Comprehensive guide for JSON output structure in prompt engineering with RCAF/CRAFT frameworks, CLEAR scoring, artifact delivery standards, conversion methods, and optimization strategies.

---

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 JSON FORMAT FUNDAMENTALS](#-json-format-fundamentals)
3. [📦 ARTIFACT DELIVERY STANDARDS](#-artifact-delivery-standards)
4. [🔧 RCAF JSON STRUCTURE](#-rcaf-json-structure)
5. [🎨 CRAFT JSON STRUCTURE](#-craft-json-structure)
6. [📄 ADVANCED JSON PATTERNS](#-advanced-json-patterns)
7. [🔄 FORMAT CONVERSIONS](#-format-conversions)
8. [⚖️ JSON VS OTHER FORMATS](#-json-vs-other-formats)
9. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
10. [📊 TRANSPARENCY REPORTING](#-transparency-reporting)
11. [📈 PERFORMANCE METRICS](#-performance-metrics)
12. [🔧 TROUBLESHOOTING](#-troubleshooting)
13. [🎓 BEST PRACTICES](#-best-practices)

---

<a id="-overview--purpose"></a>

## 1. 🎯 OVERVIEW & PURPOSE

### Why JSON Format?

JSON format provides structured, machine-parseable prompt engineering with consistent field access and programmatic integration capabilities.

**JSON Format Benefits:**
- **Structured Data:** Clear field separation and hierarchy
- **API Integration:** Direct compatibility with systems
- **Consistent Parsing:** Reliable field extraction
- **Type Safety:** Explicit data types
- **Validation:** Schema-based verification

### JSON vs Other Formats Summary

| Aspect | Markdown (Standard) | JSON | YAML |
|--------|-------------------|------|------|
| **Readability** | Natural language | Structured data | Human-friendly structure |
| **Token Usage** | Baseline | +5-10% | +3-7% |
| **CLEAR Score** | 43/50 avg | 41/50 avg | 42/50 avg |
| **Best For** | Human interaction | API/System integration | Configuration |
| **Framework Fit** | RCAF/CRAFT | RCAF preferred | RCAF optimal |

---

<a id="-json-format-fundamentals"></a>

## 2. 📊 JSON FORMAT FUNDAMENTALS

### Core JSON Principles

1. **Structure Over Prose:** Fields replace sentences
2. **Explicit Types:** Clear data type definitions
3. **Hierarchical Organization:** Nested structures for complexity
4. **Schema Consistency:** Predictable field patterns
5. **Minimal Redundancy:** No repeated information

### Basic JSON Prompt Structure

```json
{
  "instruction": "Primary directive",
  "context": "Essential information",
  "parameters": {
    "key1": "value1",
    "key2": "value2"
  },
  "output": {
    "format": "desired structure",
    "constraints": ["constraint1", "constraint2"]
  }
}
```

### JSON Data Types for Prompts

| Type | Use Case | Example |
|------|----------|---------|
| **String** | Text values | `"role": "Data Analyst"` |
| **Number** | Quantities | `"limit": 100` |
| **Boolean** | Flags | `"detailed": true` |
| **Array** | Lists | `"skills": ["Python", "SQL"]` |
| **Object** | Nested structure | `"format": {"type": "report"}` |

---

<a id="-artifact-delivery-standards"></a>

## 3. 📦 ARTIFACT DELIVERY STANDARDS

### 🔴 CRITICAL REQUIREMENTS

#### Mandatory Artifact Delivery
- **EVERY JSON enhancement MUST be in artifact format**
- **NEVER deliver JSON prompts in chat**
- **If artifact creation fails, STOP and retry**
- **Always use `text/markdown` type for artifact**
- **NEVER use `text/plain` (causes display issues)**

#### Mandatory Minimal Header Format

**Single-line header at TOP of every JSON artifact:**
```
Mode: $json | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50
```

**Header Requirements:**
- **Mode:** Always `$json` (with $ prefix)
- **Complexity level:** Low/Medium/High or 1-10
- **Framework used:** RCAF or CRAFT
- **CLEAR score:** Target ≥40/50

#### JSON Artifact Content Structure

**ONLY these two components in artifact:**
1. **Single-line header** (with $ prefix)
2. **JSON prompt content**

**FORBIDDEN in JSON artifacts:**
- ❌ Format Options section
- ❌ CLEAR Evaluation breakdown
- ❌ Processing Applied section
- ❌ Additional metadata sections
- ❌ Explanations or commentary
- ✅ All explanations go in CHAT after delivery

### Pre-Delivery Validation

```python
def validate_json_artifact():
    """MANDATORY validation before JSON delivery"""
    
    checks = {
        'valid_json': self.is_valid_json(),
        'artifact_type': self.type == 'text/markdown',
        'artifact_created': self.artifact is not None,
        'header_present': self.has_single_line_header,
        'header_format': self.mode == '$json',
        'no_extra_sections': self.has_only_header_and_content,
        'rcaf_complete': self.has_all_rcaf_fields(),
        'clear_scored': self.clear_score >= 35,
        'clear_target': self.clear_score >= 40
    }
    
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise ArtifactError(f"CANNOT DELIVER JSON. Failed: {failed}")
        
    return True
```

### 🔴 FORMAT COMPLIANCE ENFORCEMENT

#### ABSOLUTE RULES
When `$json` command is specified:
1. **Output MUST be valid JSON syntax ONLY**
2. **NO markdown formatting** (no **, no ###, no ```)
3. **NO explanatory text within the artifact**
4. **If cannot produce valid JSON, STOP and report error**
5. **Validate format before delivery - if invalid, RETRY**

#### FORMAT LOCK PROTOCOL
```
DETECTION: $json command identified
↓
LOCK: JSON-only output mode engaged
↓
GENERATE: Pure JSON structure
↓
VALIDATE: Is it valid JSON? Can json.loads() parse it?
↓
If NO → STOP → REGENERATE
If YES → DELIVER
```

#### FORBIDDEN ELEMENTS IN JSON ARTIFACTS
When $json is active, these are STRICTLY FORBIDDEN:
- ❌ Markdown bold: `**text**`
- ❌ Markdown headers: `### Header`
- ❌ Code blocks: ` ```json `
- ❌ Explanatory text before/after JSON
- ❌ Comments within JSON (JSON doesn't support comments)
- ❌ Mixed format output

#### CORRECT vs INCORRECT

**✅ CORRECT $json artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

{
  "role": "Data analyst",
  "context": "Sales database analysis",
  "action": "Generate quarterly report",
  "format": {
    "type": "dashboard",
    "sections": ["metrics", "trends"]
  }
}
```

**❌ INCORRECT - DO NOT DO THIS:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

**Role:** Data analyst
**Context:** Sales database analysis
```
This is MARKDOWN, not JSON! IMMEDIATE FAILURE.

**❌ ALSO INCORRECT:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

Here's the JSON prompt:
```json
{
  "role": "Data analyst"
}
```
```
NO explanatory text! NO code blocks! Just pure JSON.

#### ERROR RECOVERY PROTOCOL
If wrong format is generated:
```
1. RECOGNIZE: "Output is markdown but should be JSON"
2. STOP: Do not deliver wrong format
3. ANNOUNCE: "Format error detected. Regenerating as JSON..."
4. RETRY: Generate proper JSON
5. VALIDATE: json.loads() must succeed
6. DELIVER: Only if valid JSON
```

#### VALIDATION GATE
Before delivering ANY $json artifact:
```python
def enforce_json_format(content):
    """Strict JSON format enforcement"""
    
    # Check for markdown indicators
    markdown_patterns = ['**', '###', '```', '##', '__']
    for pattern in markdown_patterns:
        if pattern in content:
            return False, f"Markdown detected: {pattern}"
    
    # Validate JSON syntax
    try:
        json.loads(content)
        return True, "Valid JSON"
    except:
        return False, "Invalid JSON syntax"
    
    # If validation fails, MUST regenerate
```

---

<a id="-rcaf-json-structure"></a>

## 4. 🔧 RCAF JSON STRUCTURE

### Standard RCAF JSON Template

```json
{
  "role": "Specific expertise definition",
  "context": "Essential background information",
  "action": "Clear measurable task",
  "format": {
    "structure": "output type",
    "requirements": ["req1", "req2"],
    "constraints": ["limit1", "limit2"]
  }
}
```

### RCAF JSON Examples

#### Simple Analysis Task

**Delivered as artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

{
  "role": "Financial analyst specializing in SaaS metrics",
  "context": "Q4 2024 revenue data from B2B platform with 10K customers",
  "action": "Calculate MRR growth and identify top 3 trends",
  "format": {
    "structure": "executive_summary",
    "length": "500_words",
    "include": ["metrics", "charts", "recommendations"]
  }
}
```

#### Content Creation Task

**Delivered as artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

{
  "role": "Technical writer with API documentation expertise",
  "context": "REST API with 15 endpoints for payment processing",
  "action": "Create comprehensive API documentation",
  "format": {
    "structure": "markdown",
    "sections": ["overview", "authentication", "endpoints", "examples"],
    "style": "developer_friendly"
  }
}
```

### RCAF JSON Field Guidelines

| Field | Required | Description | CLEAR Impact |
|-------|----------|-------------|--------------|
| **role** | Yes | Expertise needed | Expression +2 |
| **context** | Yes | Essential info | Correctness +2 |
| **action** | Yes | Specific task | Logic +3 |
| **format** | Yes | Output structure | Arrangement +2 |

---

<a id="-craft-json-structure"></a>

## 5. 🎨 CRAFT JSON STRUCTURE

### Standard CRAFT JSON Template

```json
{
  "context": {
    "background": "Full situation details",
    "constraints": ["constraint1", "constraint2"],
    "assumptions": ["assumption1", "assumption2"]
  },
  "role": {
    "expertise": "Detailed expertise",
    "perspective": "Specific viewpoint"
  },
  "action": {
    "primary": "Main task",
    "subtasks": ["task1", "task2", "task3"],
    "deliverables": ["deliverable1", "deliverable2"]
  },
  "format": {
    "structure": "Output organization",
    "specifications": {
      "length": "word_count",
      "style": "tone",
      "sections": ["section1", "section2"]
    }
  },
  "target": {
    "metrics": ["metric1", "metric2"],
    "success_criteria": "Definition of success"
  }
}
```

#### Complex Analysis Task

**Delivered as artifact:**
```
Mode: $json | Complexity: High | Framework: CRAFT | CLEAR: 41/50

{
  "context": {
    "background": "E-commerce platform experiencing 15% cart abandonment",
    "timeframe": "Last 6 months",
    "data_available": ["user_sessions", "transaction_logs", "surveys"],
    "constraints": ["GDPR compliance", "30-day deadline"]
  },
  "role": {
    "expertise": "UX researcher with e-commerce specialization",
    "perspective": "User-centric analysis"
  },
  "action": {
    "primary": "Identify cart abandonment root causes",
    "subtasks": [
      "Analyze user behavior patterns",
      "Segment users by abandonment stage",
      "Correlate with survey responses"
    ]
  },
  "format": {
    "structure": "research_report",
    "specifications": {
      "length": "2500_words",
      "visualizations": ["flow_diagrams", "heat_maps"],
      "sections": ["executive_summary", "methodology", "findings", "recommendations"]
    }
  },
  "target": {
    "metrics": ["abandonment_rate_reduction", "conversion_improvement"],
    "success_criteria": "Actionable insights reducing abandonment by 20%"
  }
}
```

---

<a id="-advanced-json-patterns"></a>

## 6. 📄 ADVANCED JSON PATTERNS

### Multi-Step Process JSON

**Delivered as artifact:**
```
Mode: $json | Complexity: High | Framework: RCAF | CLEAR: 42/50

{
  "role": "Project coordinator",
  "context": "Software deployment for enterprise client",
  "action": {
    "phase_1": {
      "task": "Environment preparation",
      "outputs": ["checklist", "validation_report"]
    },
    "phase_2": {
      "task": "Deployment execution",
      "outputs": ["deployment_log", "test_results"]
    },
    "phase_3": {
      "task": "Post-deployment validation",
      "outputs": ["performance_metrics", "user_feedback"]
    }
  },
  "format": {
    "per_phase": "status_report",
    "final": "comprehensive_summary"
  }
}
```

### Conditional Logic JSON

**Delivered as artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

{
  "role": "Customer service AI",
  "context": "Support ticket classification system",
  "action": "Route tickets based on criteria",
  "logic": {
    "if_technical": {
      "route_to": "engineering",
      "priority": "assess_severity"
    },
    "if_billing": {
      "route_to": "finance",
      "priority": "high"
    },
    "if_general": {
      "route_to": "support_tier_1",
      "priority": "standard"
    }
  },
  "format": {
    "response": "routing_decision",
    "include": ["department", "priority", "rationale"]
  }
}
```

### Parameterized Template JSON

**Delivered as artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 40/50

{
  "template": "data_analysis",
  "parameters": {
    "dataset": "${DATASET_NAME}",
    "metrics": "${METRICS_ARRAY}",
    "timeframe": "${TIME_PERIOD}",
    "filters": "${FILTER_CONDITIONS}"
  },
  "role": "Data analyst",
  "context": "Business intelligence reporting",
  "action": "Generate insights from ${DATASET_NAME}",
  "format": {
    "structure": "dashboard",
    "charts": ["${CHART_TYPES}"],
    "export": "${OUTPUT_FORMAT}"
  }
}
```

---

<a id="-format-conversions"></a>

## 7. 🔄 FORMAT CONVERSIONS

### Standard to JSON Conversion

```python
def standard_to_json(standard_prompt):
    """Convert RCAF standard format to JSON"""
    
    # Parse RCAF elements
    lines = standard_prompt.split('\n')
    rcaf_json = {}
    
    for line in lines:
        if line.startswith('**Role:**'):
            rcaf_json['role'] = line.replace('**Role:**', '').strip()
        elif line.startswith('**Context:**'):
            rcaf_json['context'] = line.replace('**Context:**', '').strip()
        elif line.startswith('**Action:**'):
            rcaf_json['action'] = line.replace('**Action:**', '').strip()
        elif line.startswith('**Format:**'):
            rcaf_json['format'] = line.replace('**Format:**', '').strip()
    
    return json.dumps(rcaf_json, indent=2)
```

### JSON to Standard Conversion

```python
def json_to_standard(json_prompt):
    """Convert JSON to RCAF standard format"""
    
    data = json.loads(json_prompt)
    
    standard = f"""**Role:** {data.get('role', 'Not specified')}
**Context:** {data.get('context', 'Not specified')}
**Action:** {data.get('action', 'Not specified')}
**Format:** {data.get('format', 'Not specified')}"""
    
    return standard
```

---

<a id="-json-vs-other-formats"></a>

## 8. ⚖️ JSON VS OTHER FORMATS

### When to Use JSON Format

| Use JSON When | Use Standard When | Use YAML When |
|---------------|-------------------|---------------|
| API integration needed | Human readability priority | Configuration templates |
| Structured data processing | Natural conversation flow | Human editing needed |
| Programmatic generation | Creative or open-ended tasks | Complex hierarchies |
| Schema validation required | Flexibility needed | Comments helpful |
| Batch processing | Single prompt usage | Multi-line text common |

### CLEAR Score Impact

| Format | Avg CLEAR | Strengths | Weaknesses |
|--------|-----------|-----------|------------|
| **Standard** | 43/50 | Expression (9/10), Natural flow | Structure consistency |
| **JSON** | 41/50 | Arrangement (9/10), Precision | Expression (7/10) |
| **YAML** | 42/50 | Balance (8/10 avg) | Learning curve |

---

<a id="-examples--templates"></a>

## 9. 💡 EXAMPLES & TEMPLATES

### Template Library

#### Research Template

**Delivered as artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 40/50

{
  "role": "Research analyst",
  "context": "${RESEARCH_DOMAIN}",
  "action": {
    "primary": "Investigate ${RESEARCH_QUESTION}",
    "methodology": "${METHOD}",
    "scope": "${SCOPE_DEFINITION}"
  },
  "format": {
    "structure": "research_paper",
    "sections": ["abstract", "introduction", "methodology", "findings", "conclusion"],
    "citations": "${CITATION_STYLE}"
  }
}
```

#### Analysis Template

**Delivered as artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

{
  "role": "Data analyst",
  "context": {
    "dataset": "${DATASET}",
    "timeframe": "${PERIOD}",
    "business_context": "${CONTEXT}"
  },
  "action": "Analyze ${METRICS} and identify ${INSIGHTS_TYPE}",
  "format": {
    "deliverable": "${OUTPUT_TYPE}",
    "visualizations": "${CHART_TYPES}",
    "level_of_detail": "${DETAIL_LEVEL}"
  }
}
```

### Real-World Examples

#### Customer Segmentation

**Delivered as artifact:**
```
Mode: $json | Complexity: High | Framework: RCAF | CLEAR: 42/50

{
  "role": "Marketing data scientist",
  "context": "E-commerce platform with 100K customers, 2 years transaction history",
  "action": "Perform customer segmentation using RFM analysis",
  "format": {
    "structure": "analysis_report",
    "include": ["segment_profiles", "characteristics", "recommendations"],
    "visualizations": ["segment_distribution", "value_matrix"],
    "export": "csv_and_pdf"
  }
}
```

---

<a id="-transparency-reporting"></a>

## 10. 📊 TRANSPARENCY REPORTING

### After Every JSON Enhancement

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

**Structure Choice:** JSON
- Reasoning: [Why JSON format serves this use case]
- Token Impact: +[X]% over standard format
```

### Quick Mode Transparency Template

```markdown
📊 **Quick Enhancement Summary:**

**Processing:** [X] rounds (Quick mode, Complexity: [Y]/10)

**What Changed:**
✅ Structured into JSON format
✅ Added required RCAF fields
✅ Defined nested format specifications

**CLEAR Score:** [X]/50 (Grade: [A-F])
**Framework:** [RCAF/CRAFT] - [brief reason]
**Structure:** JSON - [API integration/automation benefit]
```

---

<a id="-performance-metrics"></a>

## 11. 📈 PERFORMANCE METRICS

### JSON Format Performance

| Metric | Target | Current Average |
|--------|--------|-----------------|
| **Parse Success Rate** | >99% | 99.2% |
| **Token Overhead** | <10% | 7.3% |
| **CLEAR Score (base)** | >35/50 | 36/50 |
| **CLEAR Score (with DEPTH)** | >40/50 | 41/50 |
| **API Integration Success** | >95% | 96.5% |
| **Schema Validation Pass** | >98% | 98.7% |
| **Artifact Delivery** | 100% | 100% |
| **Minimal Header Usage** | 100% | 100% |

### Optimization Strategies

```python
def optimize_json_prompt(json_prompt):
    """Optimize JSON for tokens and clarity"""
    
    optimizations = []
    
    # Remove null values
    cleaned = remove_nulls(json_prompt)
    if cleaned != json_prompt:
        optimizations.append("Removed null values")
    
    # Flatten single-item objects
    flattened = flatten_single_items(cleaned)
    if flattened != cleaned:
        optimizations.append("Flattened single items")
    
    # Use consistent key naming
    normalized = normalize_keys(flattened)
    if normalized != flattened:
        optimizations.append("Normalized key names")
    
    return normalized, optimizations
```

---

<a id="-troubleshooting"></a>

## 12. 🔧 TROUBLESHOOTING

### Common JSON Issues & Fixes

| Issue | Recognition | Solution | Report in Chat |
|-------|------------|----------|----------------|
| **Not artifact** | Chat delivery | Force artifact | "Retrying artifact creation..." |
| **Wrong type** | text/plain | Change to text/markdown | "Fixing artifact type..." |
| **Invalid JSON** | Parse errors | Validate with JSON linter | "Correcting JSON syntax..." |
| **Missing fields** | Incomplete prompt | Check required RCAF elements | "Adding missing fields..." |
| **Extra sections** | Explanations in artifact | Move to chat | "Cleaning artifact structure..." |
| **No transparency** | Missing report | Add after delivery | "Adding enhancement details..." |
| **Format violation** | Markdown instead of JSON | STOP and regenerate | "FORMAT ERROR: Regenerating as JSON..." |
| **Mixed format** | JSON with markdown | Strip markdown, pure JSON | "Removing markdown elements..." |

### FORMAT ENFORCEMENT CHECKLIST

Before delivering $json artifact:
- [ ] Command is `$json`?
- [ ] Content is PURE JSON?
- [ ] NO markdown bold (`**`)?
- [ ] NO markdown headers (`###`)?
- [ ] NO code blocks (` ``` `)?
- [ ] NO explanatory text?
- [ ] Valid JSON syntax (parseable)?
- [ ] All RCAF fields present?
- [ ] Header has `$json` mode?

**If ANY check fails → MUST REGENERATE**

### Validation Checklist

- [ ] Valid JSON syntax
- [ ] All RCAF/CRAFT fields present
- [ ] Consistent data types
- [ ] No circular references
- [ ] Reasonable nesting depth (<4)
- [ ] UTF-8 encoding
- [ ] No trailing commas
- [ ] Escaped special characters
- [ ] Delivered as artifact with minimal header
- [ ] Header has $json mode

### REPAIR Protocol with Transparency

```markdown
**R** - Recognize: JSON issue identified
**E** - Explain: Impact on delivery
**P** - Propose: Solution approach
**A** - Apply: Fix implemented
**I** - Iterate: Verify correction
**R** - Record: Note in transparency report
```

---

<a id="-best-practices"></a>

## 13. 🎓 BEST PRACTICES

### JSON Prompt Excellence

#### Do's ✅
- Use consistent field naming
- Validate JSON before use
- Include all RCAF elements
- Keep nesting shallow (<4 levels)
- Use arrays for multiple items
- Document schema structure
- Version your templates
- Test with JSON validators
- Deliver as artifact with minimal header
- Use $json mode in header
- Provide transparency report in chat

#### Don'ts ❌
- Don't over-nest structures
- Don't mix data types
- Don't use reserved keywords
- Don't include comments in JSON
- Don't forget error handling
- Don't use trailing commas
- Don't embed complex logic
- Don't add verbose artifact sections
- Don't skip validation
- Don't deliver in chat

### Framework Selection for JSON

| Complexity | Framework | JSON Structure |
|------------|-----------|----------------|
| Simple (1-3) | RCAF | Flat structure |
| Medium (4-6) | RCAF | Nested format field |
| Complex (7-10) | CRAFT | Multi-level nesting |

### JSON Quality Metrics

```python
def assess_json_quality(json_prompt):
    """Assess JSON prompt quality"""
    
    quality_score = 100
    issues = []
    
    data = json.loads(json_prompt)
    
    # Check depth
    depth = get_max_depth(data)
    if depth > 3:
        quality_score -= 10
        issues.append(f"Deep nesting: {depth} levels")
    
    # Check field completeness
    if not all(k in data for k in ['role', 'context', 'action', 'format']):
        quality_score -= 20
        issues.append("Missing RCAF fields")
    
    # Check value quality
    empty_fields = [k for k, v in data.items() if not v]
    if empty_fields:
        quality_score -= 10 * len(empty_fields)
        issues.append(f"Empty fields: {empty_fields}")
    
    return {
        'score': quality_score,
        'grade': get_grade(quality_score),
        'issues': issues
    }
```

### The JSON Philosophy

> "Structure enables consistency. Consistency enables automation. Automation enables scale."

**JSON Format Principles:**
1. **Clarity through structure** - Clear field separation
2. **Precision through types** - Explicit data types
3. **Reusability through templates** - Parameterized patterns
4. **Integration through standards** - API compatibility
5. **Quality through validation** - Schema enforcement
6. **Focus through minimalism** - Minimal header only
7. **Transparency through reporting** - Process visible in chat

### Success Criteria

**Excellent JSON Prompt:**
- ✅ Valid JSON syntax
- ✅ All RCAF/CRAFT fields present
- ✅ Consistent data types
- ✅ Shallow nesting (<4 levels)
- ✅ CLEAR score >41/50
- ✅ Delivered as artifact
- ✅ Single-line header with $json
- ✅ Full transparency report
- ✅ Schema validated
- ✅ API-ready structure