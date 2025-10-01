# Prompt - JSON Format Guide - v0.101

Comprehensive guide for JSON format prompt engineering with RCAF/CRAFT frameworks, CLEAR scoring, conversion methods, and optimization strategies.

---

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 JSON FORMAT FUNDAMENTALS](#-json-format-fundamentals)
3. [🔧 RCAF JSON STRUCTURE](#-rcaf-json-structure)
4. [🎨 CRAFT JSON STRUCTURE](#-craft-json-structure)
5. [📄 ADVANCED JSON PATTERNS](#-advanced-json-patterns)
6. [📄 FORMAT CONVERSIONS](#-format-conversions)
7. [⚖️ JSON VS STANDARD COMPARISON](#-json-vs-standard-comparison)
8. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
9. [📈 PERFORMANCE METRICS](#-performance-metrics)
10. [🔧 TROUBLESHOOTING](#-troubleshooting)
11. [🎓 BEST PRACTICES](#-best-practices)

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

### JSON vs Standard Format Summary

| Aspect | Standard | JSON |
|--------|----------|------|
| **Readability** | Natural language | Structured data |
| **Token Usage** | Baseline | +5-10% |
| **CLEAR Score** | 43/50 avg | 41/50 avg |
| **Best For** | Human interaction | API/System integration |
| **Framework Fit** | RCAF/CRAFT | RCAF preferred |
| **Artifact Header** | Minimal single-line | Minimal single-line |

### Delivery Format

**All JSON prompts delivered as artifacts with minimal header:**
```
Mode: $json | Complexity: [level] | Framework: RCAF | CLEAR: [X]/50

{JSON content here}
```

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

<a id="-rcaf-json-structure"></a>

## 3. 🔧 RCAF JSON STRUCTURE

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

**Delivered as:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

{
  "role": "Financial analyst specializing in SaaS metrics",
  "context": "Q4 2024 revenue data from B2B platform",
  "action": "Calculate MRR growth and identify top 3 trends",
  "format": {
    "structure": "executive_summary",
    "length": "500_words",
    "include": ["metrics", "charts", "recommendations"]
  }
}
```

**CLEAR Score: 42/50**
- Correctness: 9/10
- Logic: 8/10
- Expression: 7/10 (JSON overhead)
- Arrangement: 9/10
- Reuse: 9/10

#### Content Creation Task

**Delivered as:**
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

## 4. 🎨 CRAFT JSON STRUCTURE

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

### CRAFT JSON Examples

#### Complex Analysis Task

**Delivered as:**
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

**CLEAR Score: 41/50**
- Correctness: 9/10
- Logic: 9/10
- Expression: 6/10 (complexity overhead)
- Arrangement: 9/10
- Reuse: 8/10

---

<a id="-advanced-json-patterns"></a>

## 5. 📄 ADVANCED JSON PATTERNS

### Multi-Step Process JSON

**Delivered as:**
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

```json
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

```json
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

## 6. 📄 FORMAT CONVERSIONS

### Standard to JSON Conversion

```python
def standard_to_json(standard_prompt):
    """Convert RCAF standard format to JSON"""
    
    # Parse RCAF elements
    lines = standard_prompt.split('\n')
    rcaf_json = {}
    
    for line in lines:
        if line.startswith('Role:'):
            rcaf_json['role'] = line.replace('Role:', '').strip()
        elif line.startswith('Context:'):
            rcaf_json['context'] = line.replace('Context:', '').strip()
        elif line.startswith('Action:'):
            rcaf_json['action'] = line.replace('Action:', '').strip()
        elif line.startswith('Format:'):
            rcaf_json['format'] = line.replace('Format:', '').strip()
    
    return json.dumps(rcaf_json, indent=2)
```

### JSON to Standard Conversion

```python
def json_to_standard(json_prompt):
    """Convert JSON to RCAF standard format"""
    
    data = json.loads(json_prompt)
    
    standard = f"""Role: {data.get('role', 'Not specified')}
Context: {data.get('context', 'Not specified')}
Action: {data.get('action', 'Not specified')}
Format: {data.get('format', 'Not specified')}"""
    
    return standard
```

### Conversion Examples

**Standard RCAF:**
```
Role: Marketing analyst with SEO expertise.
Context: Tech blog with 50K monthly visitors.
Action: Audit content and identify improvements.
Format: Actionable report with priorities.
```

**JSON Equivalent (delivered as artifact):**
```
Mode: $json | Complexity: Low | Framework: RCAF | CLEAR: 41/50

{
  "role": "Marketing analyst with SEO expertise",
  "context": "Tech blog with 50K monthly visitors",
  "action": "Audit content and identify improvements",
  "format": "Actionable report with priorities"
}
```

---

<a id="-json-vs-standard-comparison"></a>

## 7. ⚖️ JSON VS STANDARD COMPARISON

### When to Use JSON Format

| Use JSON When | Use Standard When |
|---------------|-------------------|
| API integration needed | Human readability priority |
| Structured data processing | Natural conversation flow |
| Programmatic generation | Creative or open-ended tasks |
| Schema validation required | Flexibility needed |
| Batch processing | Single prompt usage |

### CLEAR Score Impact

| Format | Avg CLEAR | Strengths | Weaknesses |
|--------|-----------|-----------|------------|
| **Standard** | 43/50 | Expression (9/10), Natural flow | Structure consistency |
| **JSON** | 41/50 | Arrangement (9/10), Precision | Expression (7/10) |

### Token Efficiency Analysis

```python
def calculate_token_overhead(standard, json_version):
    """Calculate JSON overhead"""
    
    standard_tokens = count_tokens(standard)
    json_tokens = count_tokens(json_version)
    
    overhead_percent = ((json_tokens - standard_tokens) / standard_tokens) * 100
    
    return {
        'standard_tokens': standard_tokens,
        'json_tokens': json_tokens,
        'overhead_percent': round(overhead_percent, 1),
        'typical_range': '5-10%'
    }
```

---

<a id="-examples--templates"></a>

## 8. 💡 EXAMPLES & TEMPLATES

### Template Library

#### Research Template

**Delivered as:**
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

```json
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

#### Creation Template

```json
{
  "role": "${CREATOR_TYPE}",
  "context": {
    "audience": "${TARGET_AUDIENCE}",
    "purpose": "${PURPOSE}",
    "constraints": "${CONSTRAINTS}"
  },
  "action": "Create ${DELIVERABLE_TYPE}",
  "format": {
    "style": "${STYLE}",
    "length": "${LENGTH}",
    "tone": "${TONE}"
  }
}
```

### Real-World Examples

#### Customer Segmentation

**Delivered as:**
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

#### Code Review

**Delivered as:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

{
  "role": "Senior software engineer",
  "context": "Python microservice with 5000 lines of code",
  "action": {
    "review": ["code_quality", "security", "performance", "maintainability"],
    "identify": ["bugs", "vulnerabilities", "optimization_opportunities"]
  },
  "format": {
    "structure": "review_report",
    "severity_levels": ["critical", "high", "medium", "low"],
    "include_fixes": true
  }
}
```

---

<a id="-performance-metrics"></a>

## 9. 📈 PERFORMANCE METRICS

### JSON Format Performance

| Metric | Target | Current Average |
|--------|--------|-----------------|
| **Parse Success Rate** | >99% | 99.2% |
| **Token Overhead** | <10% | 7.3% |
| **CLEAR Score** | >40/50 | 41/50 |
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

## 10. 🔧 TROUBLESHOOTING

### Common JSON Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Invalid JSON** | Parse errors | Validate with JSON linter |
| **Missing fields** | Incomplete prompt | Check required RCAF elements |
| **Over-nesting** | Complex structure | Flatten where possible |
| **Type mismatch** | Processing errors | Ensure consistent types |
| **Encoding issues** | Special character errors | Use UTF-8 encoding |

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

### Debug Helper

```python
def validate_json_prompt(json_str):
    """Validate JSON prompt structure"""
    
    try:
        data = json.loads(json_str)
        
        # Check RCAF fields
        required = ['role', 'context', 'action', 'format']
        missing = [f for f in required if f not in data]
        
        if missing:
            return False, f"Missing fields: {missing}"
        
        # Check for empty values
        empty = [f for f in required if not data[f]]
        if empty:
            return False, f"Empty fields: {empty}"
        
        return True, "Valid JSON prompt"
        
    except json.JSONDecodeError as e:
        return False, f"JSON parse error: {e}"
```

---

<a id="-best-practices"></a>

## 11. 🎓 BEST PRACTICES

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
- Use single-line header format

#### Don'ts ❌
- Don't over-nest structures
- Don't mix data types
- Don't use reserved keywords
- Don't include comments in JSON
- Don't forget error handling
- Don't use trailing commas
- Don't embed complex logic
- Don't add verbose artifact sections

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

### Migration Strategy

For systems previously using other formats:

1. **Assess Current Format**: Document existing structure
2. **Map to RCAF/CRAFT**: Identify field mappings
3. **Create Templates**: Build reusable JSON templates
4. **Validate Schema**: Ensure consistency
5. **Test Integration**: Verify API compatibility
6. **Monitor Performance**: Track CLEAR scores
7. **Ensure Artifact Delivery**: Always use minimal header

### The JSON Philosophy

> "Structure enables consistency. Consistency enables automation. Automation enables scale. Minimal header enables focus."

**JSON Format Principles:**
1. **Clarity through structure** - Clear field separation
2. **Precision through types** - Explicit data types
3. **Reusability through templates** - Parameterized patterns
4. **Integration through standards** - API compatibility
5. **Quality through validation** - Schema enforcement
6. **Focus through minimalism** - Minimal header only

### Artifact Delivery Standard

**Every JSON prompt delivered as:**
```
Mode: $json | Complexity: [level] | Framework: RCAF | CLEAR: [X]/50

{JSON content}
```

**No additional sections. No verbose headers. Maximum clarity.**