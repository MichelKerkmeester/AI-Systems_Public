# Prompt - YAML Format Guide - v0.110

Comprehensive guide for YAML output structure in prompt engineering with RCAF/CRAFT frameworks, CLEAR scoring, artifact delivery standards, conversion methods, and optimization strategies.

---

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 YAML FORMAT FUNDAMENTALS](#-yaml-format-fundamentals)
3. [📦 ARTIFACT DELIVERY STANDARDS](#-artifact-delivery-standards)
4. [🔧 RCAF YAML STRUCTURE](#-rcaf-yaml-structure)
5. [🎨 CRAFT YAML STRUCTURE](#-craft-yaml-structure)
6. [📄 ADVANCED YAML PATTERNS](#-advanced-yaml-patterns)
7. [🔄 FORMAT CONVERSIONS](#-format-conversions)
8. [⚖️ YAML VS OTHER FORMATS](#-yaml-vs-other-formats)
9. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
10. [📊 TRANSPARENCY REPORTING](#-transparency-reporting)
11. [📈 PERFORMANCE METRICS](#-performance-metrics)
12. [🔧 TROUBLESHOOTING](#-troubleshooting)
13. [🎓 BEST PRACTICES](#-best-practices)

---

<a id="-overview--purpose"></a>

## 1. 🎯 OVERVIEW & PURPOSE

### Why YAML Format?

YAML (YAML Ain't Markup Language) provides human-readable structured data with minimal syntax overhead, making it ideal for configuration-style prompts and multi-level hierarchies.

**Terminology Clarification:**
- **Framework** = Prompt organization (RCAF vs CRAFT)
- **Output Structure** = Data format (Standard/Markdown vs JSON vs YAML)
- This guide covers YAML as an **output structure** option

**YAML Format Benefits:**
- **Human Readable:** Cleaner than JSON, more structured than Standard
- **Minimal Syntax:** No brackets or quotes for simple values
- **Clear Hierarchy:** Indentation-based structure
- **Comment Support:** Inline documentation capability
- **Multi-line Strings:** Natural text block handling

### YAML vs Other Formats Summary

| Aspect | Markdown (Standard) | JSON | YAML |
|--------|-------------------|------|------|
| **Readability** | Natural language | Structured data | Human-friendly structure |
| **Token Usage** | Baseline | +5-10% | +3-7% |
| **CLEAR Score (Base)** | 43/50 avg | 41/50 avg | 42/50 avg |
| **CLEAR with DEPTH** | 48/50 avg | 46/50 avg | 47/50 avg |
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

<a id="-artifact-delivery-standards"></a>

## 3. 📦 ARTIFACT DELIVERY STANDARDS

### 🔴 CRITICAL REQUIREMENTS

#### Mandatory Artifact Delivery
- **EVERY YAML enhancement MUST be in artifact format**
- **NEVER deliver YAML prompts in chat**
- **If artifact creation fails, STOP and retry**
- **Always use `text/markdown` type for artifact**
- **NEVER use `text/plain` (causes display issues)**

#### Mandatory Minimal Header Format

**Single-line header at TOP of every YAML artifact:**
```
Mode: $yaml | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50
```

**Header Requirements:**
- **Mode:** Always `$yaml` (with $ prefix)
- **Complexity level:** Low/Medium/High or 1-10
- **Framework used:** RCAF or CRAFT
- **CLEAR score:** Target ≥40/50

#### YAML Artifact Content Structure

**ONLY these two components in artifact:**
1. **Single-line header** (with $ prefix)
2. **YAML prompt content**

**FORBIDDEN in YAML artifacts:**
- ❌ Format Options section
- ❌ CLEAR Evaluation breakdown
- ❌ Processing Applied section
- ❌ Additional metadata sections
- ❌ Explanations or commentary
- ✅ All explanations go in CHAT after delivery

### Pre-Delivery Validation

```python
def validate_yaml_artifact():
    """MANDATORY validation before YAML delivery"""
    
    checks = {
        'valid_yaml': self.is_valid_yaml(),
        'artifact_type': self.type == 'text/markdown',
        'artifact_created': self.artifact is not None,
        'header_present': self.has_single_line_header,
        'header_format': self.mode == '$yaml',
        'no_extra_sections': self.has_only_header_and_content,
        'rcaf_complete': self.has_all_rcaf_fields(),
        'indentation_correct': self.check_yaml_indentation(),
        'clear_scored': self.clear_score >= 35,
        'clear_target': self.clear_score >= 40
    }
    
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise ArtifactError(f"CANNOT DELIVER YAML. Failed: {failed}")
        
    return True
```

### 🔴 FORMAT COMPLIANCE ENFORCEMENT

#### ABSOLUTE RULES
When `$yaml` command is specified:
1. **Output MUST be valid YAML syntax ONLY**
2. **NO markdown formatting** (no **, no ###, no ```)
3. **NO explanatory text within the artifact**
4. **If cannot produce valid YAML, STOP and report error**
5. **Validate format before delivery - if invalid, RETRY**

#### FORMAT LOCK PROTOCOL
```
DETECTION: $yaml command identified
↓
LOCK: YAML-only output mode engaged
↓
GENERATE: Pure YAML structure
↓
VALIDATE: Is it valid YAML? Can yaml.safe_load() parse it?
↓
If NO → STOP → REGENERATE
If YES → DELIVER
```

#### FORBIDDEN ELEMENTS IN YAML ARTIFACTS
When $yaml is active, these are STRICTLY FORBIDDEN:
- ❌ Markdown bold: `**text**`
- ❌ Markdown headers: `### Header`
- ❌ Code blocks: ` ```yaml `
- ❌ Explanatory text before/after YAML
- ❌ Mixed format output
- ❌ Tabs (use spaces only)
- ❌ Inconsistent indentation

#### CORRECT vs INCORRECT

**✅ CORRECT $yaml artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

role: Data analyst
context: Sales database analysis
action: Generate quarterly report
format:
  type: dashboard
  sections:
    - metrics
    - trends
```

**❌ INCORRECT - DO NOT DO THIS:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

**Role:** Data analyst
**Context:** Sales database analysis
```
This is MARKDOWN, not YAML! IMMEDIATE FAILURE.

**❌ ALSO INCORRECT:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

Here's the YAML prompt:
```yaml
role: Data analyst
```
```
NO explanatory text! NO code blocks! Just pure YAML.

#### ERROR RECOVERY PROTOCOL
If wrong format is generated:
```
1. RECOGNIZE: "Output is markdown but should be YAML"
2. STOP: Do not deliver wrong format
3. ANNOUNCE: "Format error detected. Regenerating as YAML..."
4. RETRY: Generate proper YAML
5. VALIDATE: yaml.safe_load() must succeed
6. DELIVER: Only if valid YAML
```

#### VALIDATION GATE
Before delivering ANY $yaml artifact:
```python
def enforce_yaml_format(content):
    """Strict YAML format enforcement"""
    
    # Check for markdown indicators
    markdown_patterns = ['**', '###', '```', '##', '__']
    for pattern in markdown_patterns:
        if pattern in content:
            return False, f"Markdown detected: {pattern}"
    
    # Check for tabs (YAML requires spaces)
    if '\t' in content:
        return False, "Tabs detected (use spaces)"
    
    # Validate YAML syntax
    try:
        yaml.safe_load(content)
        return True, "Valid YAML"
    except:
        return False, "Invalid YAML syntax"
    
    # If validation fails, MUST regenerate
```

---

<a id="-rcaf-yaml-structure"></a>

## 4. 🔧 RCAF YAML STRUCTURE

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

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

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

#### Content Creation Task

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

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

### RCAF Field Guidelines

| Field | Required | Description | Best Practices |
|-------|----------|-------------|----------------|
| **role** | Yes | Expertise needed | Be specific about domain |
| **context** | Yes | Essential info | Include constraints |
| **action** | Yes | Specific task | Make measurable |
| **format** | Yes | Output structure | Define sections |

---

<a id="-craft-yaml-structure"></a>

## 5. 🎨 CRAFT YAML STRUCTURE

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

#### Complex Analysis Task

**Delivered as artifact:**
```
Mode: $yaml | Complexity: High | Framework: CRAFT | CLEAR: 42/50

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

---

<a id="-advanced-yaml-patterns"></a>

## 6. 📄 ADVANCED YAML PATTERNS

### Multi-Phase Process YAML

**Delivered as artifact:**
```
Mode: $yaml | Complexity: High | Framework: RCAF | CLEAR: 42/50

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

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

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

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 40/50

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

## 7. 🔄 FORMAT CONVERSIONS

### Standard to YAML Conversion

```python
def standard_to_yaml(standard_prompt):
    """Convert RCAF standard format to YAML"""
    
    import yaml
    import re
    
    # Parse RCAF elements using bold markers
    pattern = r'\*\*(\w+):\*\*\s*([^\*]+?)(?=\*\*\w+:|\Z)'
    matches = re.findall(pattern, standard_prompt, re.DOTALL)
    
    rcaf_dict = {}
    for key, value in matches:
        rcaf_dict[key.lower()] = value.strip()
        
        # Parse format if it contains lists
        if key.lower() == 'format' and ',' in value:
            rcaf_dict['format'] = {
                'structure': value.split(',')[0].strip()
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
    
    standard = f"""**Role:** {data.get('role', 'Not specified')}
**Context:** {data.get('context', 'Not specified')}
**Action:** {data.get('action', 'Not specified')}
**Format:** {data.get('format', 'Not specified')}"""
    
    return standard
```

---

<a id="-yaml-vs-other-formats"></a>

## 8. ⚖️ YAML VS OTHER FORMATS

### When to Use Each Format

| Use YAML When | Use JSON When | Use Standard When |
|---------------|---------------|-------------------|
| Configuration templates | API integration | Natural conversation |
| Human editing needed | Machine parsing only | Creative tasks |
| Complex hierarchies | Simple structures | Quick prompts |
| Comments helpful | Validation required | Flexibility needed |
| Multi-line text common | Data exchange | Single use |

### CLEAR Score Comparison

| Format | Base CLEAR | With DEPTH | Strengths | Weaknesses |
|--------|-----------|------------|-----------|------------|
| **Standard** | 43/50 avg | 48/50 avg | Expression (9/10) | Structure consistency |
| **JSON** | 41/50 avg | 46/50 avg | Arrangement (9/10) | Expression (7/10) |
| **YAML** | 42/50 avg | 47/50 avg | Balance (8/10 avg) | Learning curve |

---

<a id="-examples--templates"></a>

## 9. 💡 EXAMPLES & TEMPLATES

### Template Library

#### Research Template

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 40/50

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

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

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

### Real-World Examples

#### Customer Segmentation

**Delivered as artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

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

**Delivered as artifact:**
```
Mode: $yaml | Complexity: High | Framework: CRAFT | CLEAR: 42/50

context:
  api_type: REST
  endpoints: 25
  authentication: OAuth 2.0
  versioning: semantic

role:
  expertise: Technical documentation specialist
  focus: Developer experience

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

target:
  metrics:
    - time_to_first_api_call
    - developer_satisfaction
  success_criteria: Complete documentation enabling integration in under 2 hours
```

---

<a id="-transparency-reporting"></a>

## 10. 📊 TRANSPARENCY REPORTING

### After Every YAML Enhancement

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

**Structure Choice:** YAML
- Reasoning: [Why YAML format serves this use case]
- Token Impact: +[X]% over standard format
```

### Quick Mode Transparency Template

```markdown
📊 **Quick Enhancement Summary:**

**Processing:** [X] rounds (Quick mode, Complexity: [Y]/10)

**What Changed:**
✅ Structured into YAML format
✅ Applied indentation hierarchy
✅ Created nested specifications

**CLEAR Score:** [X]/50 (Grade: [A-F])
**Framework:** [RCAF/CRAFT] - [brief reason]
**Structure:** YAML - [configuration benefit]
```

---

<a id="-performance-metrics"></a>

## 11. 📈 PERFORMANCE METRICS

### YAML Format Performance

| Metric | Target | Current Average |
|--------|--------|-----------------|
| **Parse Success Rate** | >99% | 99.5% |
| **Token Overhead** | <7% | 5.2% |
| **Base CLEAR Score** | >40/50 | 42/50 |
| **CLEAR with DEPTH** | >45/50 | 47/50 |
| **Human Readability** | High | 9/10 |
| **Edit Efficiency** | >JSON | 1.4x faster |
| **Artifact Delivery** | 100% | 100% |
| **Header Compliance** | 100% | 100% |

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
            optimizations.append(f"Compacted {key} list")
    
    return yaml.dump(data, default_flow_style=False), optimizations
```

---

<a id="-troubleshooting"></a>

## 12. 🔧 TROUBLESHOOTING

### Common YAML Issues & Fixes

| Issue | Recognition | Solution | Report in Chat |
|-------|------------|----------|----------------|
| **Not artifact** | Chat delivery | Force artifact | "Retrying artifact creation..." |
| **Wrong type** | text/plain | Change to text/markdown | "Fixing artifact type..." |
| **Indentation errors** | Parse fails | Use exactly 2 spaces | "Correcting indentation..." |
| **Quote confusion** | String parsing issues | Remove unnecessary quotes | "Simplifying syntax..." |
| **List syntax** | Structure errors | Ensure dash-space prefix | "Fixing list format..." |
| **Extra sections** | Explanations in artifact | Move to chat | "Cleaning artifact..." |
| **No transparency** | Missing report | Add after delivery | "Adding enhancement details..." |

### Validation Checklist

- [ ] Consistent 2-space indentation
- [ ] All RCAF/CRAFT fields present
- [ ] No tabs (spaces only)
- [ ] Valid YAML syntax
- [ ] Proper list formatting
- [ ] Multiline strings handled correctly
- [ ] No trailing spaces
- [ ] UTF-8 encoding
- [ ] Artifact header present with $yaml
- [ ] CLEAR score ≥ 40/50 target
- [ ] Transparency report ready

### REPAIR Protocol with Transparency

```markdown
**R** - Recognize: YAML issue identified
**E** - Explain: Impact on structure
**P** - Propose: Correction approach
**A** - Apply: Fix implemented
**I** - Iterate: Verify YAML validity
**R** - Record: Note in transparency report
```

---

<a id="-best-practices"></a>

## 13. 🎓 BEST PRACTICES

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
- **Always deliver as artifact with header**
- **Use $yaml mode in header**
- **Provide transparency report in chat**

#### Don'ts ❌
- Don't mix tabs and spaces
- Don't over-nest structures
- Don't use special characters in keys
- Don't forget list dash-space
- Don't use flow style for complex data
- Don't ignore indentation rules
- Don't embed complex logic
- Don't use without validation
- **Don't deliver in chat (artifact mandatory)**
- **Don't skip validation**
- **Don't add extra artifact sections**

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
6. **Focus through minimalism** - Single header only
7. **Transparency through reporting** - Process visible in chat

### Command Activation

To use YAML format, users can:
- Use `$yaml` command for automatic YAML formatting
- Use `$y` as shorthand
- Combine with modes: `$improve $yaml` or `$refine $yaml`
- Request in Interactive Mode when format selection appears

### Success Criteria

**Excellent YAML Prompt:**
- ✅ Valid YAML syntax
- ✅ All RCAF/CRAFT elements present
- ✅ Consistent indentation
- ✅ Clear hierarchy
- ✅ Minimal nesting
- ✅ Human readable
- ✅ Base CLEAR score > 42/50
- ✅ With DEPTH: > 47/50
- ✅ Token overhead < 7%
- ✅ **Delivered as artifact with $yaml header**
- ✅ **Full transparency report in chat**