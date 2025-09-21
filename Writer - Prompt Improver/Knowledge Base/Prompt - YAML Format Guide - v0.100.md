# Prompt - YAML Format Guide - v0.100

Comprehensive guide for YAML format prompt engineering with RCAF/CRAFT frameworks, CLEAR scoring, conversion methods, and optimization strategies.

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 YAML FORMAT FUNDAMENTALS](#-yaml-format-fundamentals)
3. [🔧 RCAF YAML STRUCTURE](#-rcaf-yaml-structure)
4. [🎨 CRAFT YAML STRUCTURE](#-craft-yaml-structure)
5. [🔄 ADVANCED YAML PATTERNS](#-advanced-yaml-patterns)
6. [🔄 FORMAT CONVERSIONS](#-format-conversions)
7. [⚖️ YAML VS OTHER FORMATS](#-yaml-vs-other-formats)
8. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
9. [📈 PERFORMANCE METRICS](#-performance-metrics)
10. [🔧 TROUBLESHOOTING](#-troubleshooting)
11. [🎓 BEST PRACTICES](#-best-practices)

---

<a id="-overview--purpose"></a>

## 1. 🎯 OVERVIEW & PURPOSE

### Why YAML Format?

YAML (YAML Ain't Markup Language) provides human-readable structured data with minimal syntax overhead, making it ideal for configuration-style prompts and multi-level hierarchies.

**YAML Format Benefits:**
- **Human Readable:** Cleaner than JSON, more structured than Standard
- **Minimal Syntax:** No brackets or quotes for simple values
- **Clear Hierarchy:** Indentation-based structure
- **Comment Support:** Inline documentation capability
- **Multi-line Strings:** Natural text block handling

### YAML vs Other Formats Summary

| Aspect | Standard | JSON | YAML |
|--------|----------|------|------|
| **Readability** | Natural language | Structured data | Human-friendly structure |
| **Token Usage** | Baseline | +5-10% | +3-7% |
| **CLEAR Score** | 43/50 avg | 41/50 avg | 42/50 avg |
| **Best For** | Human interaction | API integration | Configuration, templates |
| **Framework Fit** | RCAF/CRAFT | RCAF preferred | RCAF optimal |

---

<a id="-yaml-format-fundamentals"></a>

## 2. 📊 YAML FORMAT FUNDAMENTALS

### Core YAML Principles

1. **Indentation Matters:** 2 spaces define hierarchy
2. **No Quotes Required:** For simple strings
3. **Lists with Dashes:** Clean array syntax
4. **Key-Value Simplicity:** Colon separation
5. **Multi-line Support:** Literal and folded blocks

### Basic YAML Prompt Structure

```yaml
instruction: Primary directive for the task
context: Essential background information
parameters:
  key1: value1
  key2: value2
  nested:
    subkey: subvalue
output:
  format: desired structure
  constraints:
    - constraint one
    - constraint two
  requirements:
    - requirement one
    - requirement two
```

### YAML Data Types for Prompts

| Type | Syntax | Example |
|------|--------|---------|
| **String** | No quotes needed | `role: Data Analyst` |
| **Number** | Direct value | `limit: 100` |
| **Boolean** | true/false | `detailed: true` |
| **List** | Dash prefix | `- Python`<br>`- SQL` |
| **Object** | Indented keys | `format:`<br>`  type: report` |
| **Multi-line** | Pipe or > | `description: |`<br>`  Multiple lines` |

---

<a id="-rcaf-yaml-structure"></a>

## 3. 🔧 RCAF YAML STRUCTURE

### Standard RCAF YAML Template

```yaml
role: Specific expertise definition
context: Essential background information
action: Clear measurable task
format:
  structure: output type
  requirements:
    - requirement one
    - requirement two
  constraints:
    - limit one
    - limit two
```

### RCAF YAML Examples

#### Simple Analysis Task
```yaml
role: Financial analyst specializing in SaaS metrics
context: Q4 2024 revenue data from B2B platform
action: Calculate MRR growth and identify top 3 trends
format:
  structure: executive_summary
  length: 500_words
  include:
    - metrics
    - charts
    - recommendations
```

**CLEAR Score: 43/50**
- Correctness: 9/10
- Logic: 8/10
- Expression: 8/10 (YAML clarity)
- Arrangement: 9/10
- Reuse: 9/10

#### Content Creation Task
```yaml
role: Technical writer with API documentation expertise
context: REST API with 15 endpoints for payment processing
action: Create comprehensive API documentation
format:
  structure: markdown
  sections:
    - overview
    - authentication
    - endpoints
    - examples
  style: developer_friendly
  examples_per_endpoint: 2
```

### RCAF YAML Field Guidelines

| Field | Required | Description | CLEAR Impact |
|-------|----------|-------------|--------------|
| **role** | Yes | Expertise needed | Expression +2 |
| **context** | Yes | Essential info | Correctness +2 |
| **action** | Yes | Specific task | Logic +3 |
| **format** | Yes | Output structure | Arrangement +2 |

---

<a id="-craft-yaml-structure"></a>

## 4. 🎨 CRAFT YAML STRUCTURE

### Standard CRAFT YAML Template

```yaml
context:
  background: Full situation details
  constraints:
    - constraint one
    - constraint two
  assumptions:
    - assumption one
    - assumption two
  
role:
  expertise: Detailed expertise description
  perspective: Specific viewpoint or approach
  
action:
  primary: Main task to accomplish
  subtasks:
    - task one
    - task two
    - task three
  deliverables:
    - deliverable one
    - deliverable two
    
format:
  structure: Output organization type
  specifications:
    length: word_count
    style: tone_and_voice
    sections:
      - section one
      - section two
      
target:
  metrics:
    - metric one
    - metric two
  success_criteria: Definition of successful outcome
```

### CRAFT YAML Examples

#### Complex Analysis Task
```yaml
context:
  background: E-commerce platform experiencing 15% cart abandonment
  timeframe: Last 6 months
  data_available:
    - user_sessions
    - transaction_logs
    - surveys
  constraints:
    - GDPR compliance required
    - 30-day deadline

role:
  expertise: UX researcher with e-commerce specialization
  perspective: User-centric analysis approach
  tools: Google Analytics, Hotjar, custom tracking

action:
  primary: Identify cart abandonment root causes
  subtasks:
    - Analyze user behavior patterns
    - Segment users by abandonment stage
    - Correlate with survey responses
    - Generate actionable recommendations

format:
  structure: research_report
  specifications:
    length: 2500_words
    visualizations:
      - flow_diagrams
      - heat_maps
      - conversion_funnels
    sections:
      - executive_summary
      - methodology
      - findings
      - recommendations

target:
  metrics:
    - abandonment_rate_reduction
    - conversion_improvement
  success_criteria: Actionable insights reducing abandonment by 20%
```

**CLEAR Score: 42/50**
- Correctness: 9/10
- Logic: 9/10
- Expression: 7/10 (some complexity)
- Arrangement: 9/10
- Reuse: 8/10

---

<a id="-advanced-yaml-patterns"></a>

## 5. 🔄 ADVANCED YAML PATTERNS

### Multi-Phase Process YAML

```yaml
role: Project coordinator
context: Software deployment for enterprise client
phases:
  - name: Environment Preparation
    action: Setup and validate infrastructure
    outputs:
      - checklist
      - validation_report
      
  - name: Deployment Execution
    action: Execute deployment procedures
    outputs:
      - deployment_log
      - test_results
      
  - name: Post-Deployment
    action: Validate and monitor
    outputs:
      - performance_metrics
      - user_feedback

format:
  per_phase: status_report
  final: comprehensive_summary
  delivery: markdown_documents
```

### Conditional Logic YAML

```yaml
role: Customer service AI
context: Support ticket classification system
action: Route tickets based on criteria

routing_logic:
  technical:
    route_to: engineering
    priority: assess_severity
    conditions:
      - contains: error
      - contains: bug
      - contains: crash
      
  billing:
    route_to: finance
    priority: high
    conditions:
      - contains: payment
      - contains: invoice
      - contains: subscription
      
  general:
    route_to: support_tier_1
    priority: standard
    default: true

format:
  response: routing_decision
  include:
    - department
    - priority
    - rationale
```

### Template with Anchors YAML

```yaml
# Define reusable components
defaults: &default_format
  style: professional
  tone: concise
  audience: technical

templates:
  analysis: &analysis_template
    structure: analytical_report
    <<: *default_format
    sections:
      - overview
      - methodology
      - findings
      - recommendations

# Main prompt using anchors
role: Data analyst
context: Customer behavior analysis needed
action: Analyze purchase patterns
format:
  <<: *analysis_template
  length: 2000_words
  visualizations:
    - trend_charts
    - segment_analysis
```

---

<a id="-format-conversions"></a>

## 6. 🔄 FORMAT CONVERSIONS

### Standard to YAML Conversion

```python
def standard_to_yaml(standard_prompt):
    """Convert RCAF standard format to YAML"""
    
    import yaml
    
    # Parse RCAF elements
    lines = standard_prompt.split('\n')
    rcaf_dict = {}
    
    for line in lines:
        if line.startswith('Role:'):
            rcaf_dict['role'] = line.replace('Role:', '').strip()
        elif line.startswith('Context:'):
            rcaf_dict['context'] = line.replace('Context:', '').strip()
        elif line.startswith('Action:'):
            rcaf_dict['action'] = line.replace('Action:', '').strip()
        elif line.startswith('Format:'):
            # Parse format as nested structure
            format_text = line.replace('Format:', '').strip()
            rcaf_dict['format'] = {
                'structure': format_text.split(',')[0] if ',' in format_text else format_text
            }
    
    return yaml.dump(rcaf_dict, default_flow_style=False, sort_keys=False)
```

### JSON to YAML Conversion

```python
def json_to_yaml(json_prompt):
    """Convert JSON to YAML format"""
    
    import json
    import yaml
    
    data = json.loads(json_prompt)
    return yaml.dump(data, default_flow_style=False, sort_keys=False)
```

### YAML to Standard Conversion

```python
def yaml_to_standard(yaml_prompt):
    """Convert YAML to RCAF standard format"""
    
    import yaml
    
    data = yaml.safe_load(yaml_prompt)
    
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

**YAML Equivalent:**
```yaml
role: Marketing analyst with SEO expertise
context: Tech blog with 50K monthly visitors
action: Audit content and identify improvements
format: Actionable report with priorities
```

**JSON Equivalent:**
```json
{
  "role": "Marketing analyst with SEO expertise",
  "context": "Tech blog with 50K monthly visitors",
  "action": "Audit content and identify improvements",
  "format": "Actionable report with priorities"
}
```

---

<a id="-yaml-vs-other-formats"></a>

## 7. ⚖️ YAML VS OTHER FORMATS

### When to Use Each Format

| Use YAML When | Use JSON When | Use Standard When |
|---------------|---------------|-------------------|
| Configuration templates | API integration | Natural conversation |
| Human editing needed | Machine parsing only | Creative tasks |
| Complex hierarchies | Simple structures | Quick prompts |
| Comments helpful | Validation required | Flexibility needed |
| Multi-line text common | Data exchange | Single use |

### CLEAR Score Comparison

| Format | Avg CLEAR | Strengths | Weaknesses |
|--------|-----------|-----------|------------|
| **Standard** | 43/50 | Expression (9/10) | Structure consistency |
| **JSON** | 41/50 | Arrangement (9/10) | Expression (7/10) |
| **YAML** | 42/50 | Balance (8/10 avg) | Learning curve |

### Token Efficiency Analysis

```python
def compare_format_tokens(standard, json_version, yaml_version):
    """Compare token usage across formats"""
    
    standard_tokens = count_tokens(standard)
    json_tokens = count_tokens(json_version)
    yaml_tokens = count_tokens(yaml_version)
    
    return {
        'standard': standard_tokens,
        'json': {
            'tokens': json_tokens,
            'overhead': f"{((json_tokens - standard_tokens) / standard_tokens * 100):.1f}%"
        },
        'yaml': {
            'tokens': yaml_tokens,
            'overhead': f"{((yaml_tokens - standard_tokens) / standard_tokens * 100):.1f}%"
        }
    }
```

---

<a id="-examples--templates"></a>

## 8. 💡 EXAMPLES & TEMPLATES

### Template Library

#### Research Template
```yaml
# Research Prompt Template
role: Research analyst
context: ${RESEARCH_DOMAIN}
action:
  primary: Investigate ${RESEARCH_QUESTION}
  methodology: ${METHOD}
  scope: ${SCOPE_DEFINITION}
  
format:
  structure: research_paper
  sections:
    - abstract
    - introduction
    - methodology
    - findings
    - conclusion
  citations: ${CITATION_STYLE}
  length: ${WORD_COUNT}
```

#### Analysis Template
```yaml
# Data Analysis Template
role: Data analyst
context:
  dataset: ${DATASET}
  timeframe: ${PERIOD}
  business_context: ${CONTEXT}
  
action: Analyze ${METRICS} and identify ${INSIGHTS_TYPE}

format:
  deliverable: ${OUTPUT_TYPE}
  visualizations: ${CHART_TYPES}
  detail_level: ${DETAIL_LEVEL}
  export_formats:
    - pdf
    - csv
    - interactive_dashboard
```

#### Builder Template
```yaml
# Application Builder Template
role: ${DEVELOPER_TYPE}
context:
  platform: ${TARGET_PLATFORM}
  users: ${USER_DESCRIPTION}
  constraints: ${TECHNICAL_CONSTRAINTS}
  
action:
  build: ${APPLICATION_TYPE}
  features:
    - ${FEATURE_1}
    - ${FEATURE_2}
    - ${FEATURE_3}
    
format:
  architecture: ${ARCHITECTURE_TYPE}
  tech_stack:
    frontend: ${FRONTEND_TECH}
    backend: ${BACKEND_TECH}
    database: ${DATABASE_TYPE}
  deployment: ${DEPLOYMENT_METHOD}
```

### Real-World Examples

#### Customer Segmentation
```yaml
role: Marketing data scientist
context: E-commerce platform with 100K customers, 2 years transaction history

action:
  primary: Perform customer segmentation using RFM analysis
  steps:
    - Calculate recency scores
    - Calculate frequency scores
    - Calculate monetary scores
    - Create segment profiles
    - Generate recommendations

format:
  structure: analysis_report
  include:
    - segment_profiles
    - characteristics
    - size_distribution
    - value_analysis
    - recommendations
  visualizations:
    - segment_distribution
    - value_matrix
    - trend_analysis
  export:
    - csv_data
    - pdf_report
    - interactive_dashboard
```

#### API Documentation
```yaml
role: Technical documentation specialist
context:
  api_type: REST
  endpoints: 25
  authentication: OAuth 2.0
  versioning: semantic

action:
  document:
    - endpoint_specifications
    - authentication_flow
    - error_handling
    - rate_limits
    - examples

format:
  structure: developer_documentation
  per_endpoint:
    - description
    - parameters
    - request_examples
    - response_examples
    - error_codes
  tools:
    - postman_collection
    - openapi_spec
    - interactive_playground
```

---

<a id="-performance-metrics"></a>

## 9. 📈 PERFORMANCE METRICS

### YAML Format Performance

| Metric | Target | Current Average |
|--------|--------|-----------------|
| **Parse Success Rate** | >99% | 99.5% |
| **Token Overhead** | <7% | 5.2% |
| **CLEAR Score** | >40/50 | 42/50 |
| **Human Readability** | High | 9/10 |
| **Edit Efficiency** | >JSON | 1.4x faster |

### Optimization Strategies

```python
def optimize_yaml_prompt(yaml_prompt):
    """Optimize YAML for clarity and efficiency"""
    
    import yaml
    
    optimizations = []
    data = yaml.safe_load(yaml_prompt)
    
    # Flatten single-item lists
    for key, value in data.items():
        if isinstance(value, list) and len(value) == 1:
            data[key] = value[0]
            optimizations.append(f"Flattened {key}")
    
    # Remove null values
    data = {k: v for k, v in data.items() if v is not None}
    if len(data) < len(yaml.safe_load(yaml_prompt)):
        optimizations.append("Removed null values")
    
    # Use flow style for short lists
    for key, value in data.items():
        if isinstance(value, list) and len(value) <= 3:
            # Would use flow style in actual YAML dump
            optimizations.append(f"Compacted {key} list")
    
    return yaml.dump(data, default_flow_style=False), optimizations
```

---

<a id="-troubleshooting"></a>

## 10. 🔧 TROUBLESHOOTING

### Common YAML Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Indentation errors** | Parse fails | Use exactly 2 spaces |
| **Quote confusion** | String parsing issues | Use quotes for special chars only |
| **List syntax** | Structure errors | Ensure dash-space prefix |
| **Multiline strings** | Text truncation | Use pipe (|) or > correctly |
| **Type ambiguity** | Wrong data type | Use explicit typing when needed |

### Validation Checklist

- [ ] Consistent 2-space indentation
- [ ] All RCAF/CRAFT fields present
- [ ] No tabs (spaces only)
- [ ] Valid YAML syntax
- [ ] Proper list formatting
- [ ] Multiline strings handled correctly
- [ ] No trailing spaces
- [ ] UTF-8 encoding

### Debug Helper

```python
def validate_yaml_prompt(yaml_str):
    """Validate YAML prompt structure"""
    
    import yaml
    
    try:
        data = yaml.safe_load(yaml_str)
        
        # Check RCAF fields
        required = ['role', 'context', 'action', 'format']
        missing = [f for f in required if f not in data]
        
        if missing:
            return False, f"Missing fields: {missing}"
        
        # Check for empty values
        empty = [f for f in required if not data[f]]
        if empty:
            return False, f"Empty fields: {empty}"
        
        # Check indentation (basic)
        lines = yaml_str.split('\n')
        for i, line in enumerate(lines):
            if '\t' in line:
                return False, f"Tab character on line {i+1}"
        
        return True, "Valid YAML prompt"
        
    except yaml.YAMLError as e:
        return False, f"YAML parse error: {e}"
```

---

<a id="-best-practices"></a>

## 11. 🎓 BEST PRACTICES

### YAML Prompt Excellence

#### Do's ✅
- Use 2-space indentation consistently
- Keep hierarchy shallow (<4 levels)
- Use meaningful key names
- Leverage multiline strings for text
- Add comments for complex sections
- Validate before use
- Use anchors for repeated content
- Test with YAML validators

#### Don'ts ❌
- Don't mix tabs and spaces
- Don't over-nest structures
- Don't use special characters in keys
- Don't forget list dash-space
- Don't use flow style for complex data
- Don't ignore indentation rules
- Don't embed complex logic
- Don't use without validation

### Framework Selection for YAML

| Complexity | Framework | YAML Structure |
|------------|-----------|----------------|
| Simple (1-3) | RCAF | Flat, 4 keys |
| Medium (4-6) | RCAF | Nested format |
| Complex (7-10) | CRAFT | Multi-level hierarchy |

### YAML Quality Metrics

```python
def assess_yaml_quality(yaml_prompt):
    """Assess YAML prompt quality"""
    
    import yaml
    
    quality_score = 100
    issues = []
    
    data = yaml.safe_load(yaml_prompt)
    
    # Check depth
    def get_depth(d, level=0):
        if not isinstance(d, dict):
            return level
        return max([get_depth(v, level+1) for v in d.values()] or [level])
    
    depth = get_depth(data)
    if depth > 4:
        quality_score -= 10
        issues.append(f"Deep nesting: {depth} levels")
    
    # Check completeness
    required = ['role', 'context', 'action', 'format']
    missing = [f for f in required if f not in data]
    if missing:
        quality_score -= 20
        issues.append(f"Missing: {missing}")
    
    # Check readability
    yaml_lines = yaml_prompt.split('\n')
    long_lines = [i for i, line in enumerate(yaml_lines) if len(line) > 80]
    if long_lines:
        quality_score -= 5
        issues.append(f"Long lines: {len(long_lines)}")
    
    return {
        'score': quality_score,
        'grade': 'A' if quality_score >= 90 else 'B' if quality_score >= 80 else 'C',
        'issues': issues
    }
```

### The YAML Philosophy

> "Structure with humanity. YAML bridges machine precision with human readability."

**YAML Format Principles:**
1. **Clarity through indentation** - Visual hierarchy
2. **Simplicity through minimalism** - Less syntax overhead
3. **Flexibility through structure** - Nested when needed
4. **Readability through spacing** - Natural formatting
5. **Maintainability through comments** - Self-documenting

### Command Activation

To use YAML format, users can:
- Use `$yaml` command for automatic YAML formatting
- Use `$y` as shorthand
- Combine with modes: `$improve $yaml` or `$builder $yaml`
- Request in Interactive Mode when format selection appears

### Success Criteria

**Excellent YAML Prompt:**
- ✅ Valid YAML syntax
- ✅ All RCAF/CRAFT elements present
- ✅ Consistent indentation
- ✅ Clear hierarchy
- ✅ Minimal nesting
- ✅ Human readable
- ✅ CLEAR score > 42/50
- ✅ Token overhead < 7%

---

*YAML Format Guide: Human-readable structured prompts with minimal syntax. RCAF provides framework, YAML provides clarity. Every indent matters, every dash counts. Validate everything, optimize for readability. For comparison with other formats, refer to main system documentation.*