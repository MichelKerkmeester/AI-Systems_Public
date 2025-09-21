# Prompt - JSON & SMILE Format Guide - v0.101

Comprehensive guide for JSON and SMILE format prompt engineering with RCAF/CRAFT frameworks, CLEAR scoring, conversion methods, and optimization strategies.

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 JSON FORMAT GUIDE](#-json-format-guide)
3. [😊 SMILE FORMAT GUIDE](#-smile-format-guide)
4. [🔄 RCAF FORMAT CONVERSIONS](#-rcaf-format-conversions)
5. [⚖️ FORMAT COMPARISON & SELECTION](#-format-comparison--selection)
6. [🚀 ADVANCED TECHNIQUES](#-advanced-techniques)
7. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
8. [📈 PERFORMANCE METRICS](#-performance-metrics)
9. [🔧 TROUBLESHOOTING](#-troubleshooting)
10. [🎓 BEST PRACTICES](#-best-practices)

---

## 1. 🎯 OVERVIEW & PURPOSE

### Why Alternative Formats?

**Standard Format with RCAF:**
- Natural language with RCAF structure
- Maximum readability and clarity
- Baseline token usage
- Best for: Most general prompts
- CLEAR average: 43/50

**JSON Format with RCAF:**
- Structured RCAF data representation
- Machine-parseable
- Consistent field access
- Best for: APIs, systematic processing
- CLEAR average: 41/50

**SMILE Format with CRAFT:**
- Enhanced instruction following
- Clear hierarchical organization
- Best for: Complex multi-step workflows
- CLEAR average: 40/50

### Token Impact Summary with CLEAR

| Format | Framework | Token Overhead | CLEAR Score | Best Use |
|--------|-----------|----------------|-------------|----------|
| Standard | RCAF | Baseline (0%) | 43/50 | General prompts |
| JSON | RCAF | +5-10% | 41/50 | API integration |
| SMILE | CRAFT | +20-30% | 40/50 | Complex workflows |

---

## 2. 📊 JSON FORMAT GUIDE

### Core Principles with RCAF

JSON prompting with RCAF framework:
- **Role clarity** through explicit field
- **Context precision** in structured format
- **Action specificity** with clear task definition
- **Format consistency** across requests

### Basic RCAF JSON Structure

```json
{
  "role": "Specific expertise definition",
  "context": "Essential background information",
  "action": "Clear measurable task",
  "format": {
    "structure": "desired output type",
    "requirements": ["req1", "req2"],
    "constraints": ["limit1", "limit2"]
  }
}
```

### RCAF JSON Example

```json
{
  "role": "Data analyst specializing in customer behavior",
  "context": "E-commerce platform with 100K monthly transactions",
  "action": "Identify top 3 conversion drivers",
  "format": {
    "structure": "executive_summary",
    "length": "500_words",
    "include": ["metrics", "visualizations", "recommendations"]
  }
}
```

**CLEAR Score: 41/50**
- Correctness: 9/10
- Logic: 8/10
- Expression: 7/10
- Arrangement: 9/10
- Reuse: 8/10

### Advanced JSON Patterns with RCAF

#### Multi-Step RCAF JSON
```json
{
  "role": "Project manager with agile expertise",
  "context": {
    "project": "mobile_app_development",
    "team_size": 8,
    "timeline": "3_months"
  },
  "action": {
    "primary": "create_sprint_plan",
    "steps": [
      "analyze_requirements",
      "define_sprints",
      "assign_resources",
      "identify_risks"
    ]
  },
  "format": {
    "deliverable": "sprint_roadmap",
    "structure": {
      "sprints": "2_week_cycles",
      "milestones": "weekly",
      "reports": "burndown_charts"
    }
  }
}
```

### JSON Best Practices with CLEAR

1. **RCAF Field Naming:**
   - Use exact RCAF terms for clarity
   - Maintain consistent structure
   - CLEAR Expression: +2 points

2. **Value Clarity:**
   - Explicit values over ambiguous
   - Structured over free-form
   - CLEAR Correctness: +2 points

3. **Optimization for CLEAR:**
   - Minimize nesting (Expression)
   - Complete coverage (Logic)
   - Clear hierarchy (Arrangement)

---

## 3. 😊 SMILE FORMAT GUIDE

### SMILE Philosophy with CRAFT

SMILE works best with CRAFT's comprehensive structure, using emoticon-like markers for visual organization.

### Symbol Reference for CRAFT Elements

| Symbol | Name | CRAFT Mapping | CLEAR Impact |
|--------|------|---------------|--------------|
| `(: :)` | Sections | Major divisions | Arrangement +2 |
| `[: :]` | Requirements | Context/Constraints | Correctness +2 |
| `[= =]` | Task | Action definition | Logic +2 |
| `[$ $]` | Variables | Dynamic elements | Reuse +1 |
| `[! !]` | Emphasis | Critical points | Correctness +1 |
| `{...}` | AI Fills | Format/Output | Expression varies |

### CRAFT to SMILE Structure

```
(: Task Name
  [: Context [
    Background information
    Constraints and requirements
  ] :]
  
  [: Role [
    Expertise definition
    Perspective required
  ] :]
  
  [= Action =]
  Primary task description
  
  [: Format [
    Output structure
    Deliverable requirements
  ] :]
  
  [: Target [
    Success metrics
    [! Critical outcomes !]
  ] :]
) :)
```

### SMILE with CRAFT Example

```
(: Customer Analysis System
  [: Context [
    E-commerce platform data
    100K monthly transactions
    B2C market focus
  ] :]
  
  [: Role [
    Data scientist specializing in customer analytics
    E-commerce domain expertise
  ] :]
  
  [= Action =]
  Analyze customer behavior patterns and create predictive model
  
  [: Format [
    {Executive dashboard with visualizations}
    {Predictive model documentation}
    {Implementation recommendations}
  ] :]
  
  [: Target [
    Model accuracy > 85%
    [! Identify top 3 churn factors !]
    Actionable insights within 48 hours
  ] :]
) :)
```

**CLEAR Score: 40/50**
- Correctness: 9/10
- Logic: 9/10
- Expression: 6/10 (token overhead)
- Arrangement: 8/10
- Reuse: 8/10

---

## 4. 🔄 RCAF FORMAT CONVERSIONS

### Standard RCAF to JSON

```python
def rcaf_to_json(rcaf_prompt):
    """Convert RCAF natural language to JSON"""
    return {
        "role": extract_role_line(rcaf_prompt),
        "context": extract_context_line(rcaf_prompt),
        "action": extract_action_line(rcaf_prompt),
        "format": extract_format_spec(rcaf_prompt)
    }
```

**Example Conversion:**

Standard RCAF:
```
Role: Marketing analyst with SEO expertise.
Context: Tech blog with 50K monthly visitors, declining organic traffic.
Action: Audit content and identify top 5 SEO improvements.
Format: Actionable report with priority matrix.
```

JSON RCAF:
```json
{
  "role": "Marketing analyst with SEO expertise",
  "context": "Tech blog with 50K monthly visitors, declining organic traffic",
  "action": "Audit content and identify top 5 SEO improvements",
  "format": "Actionable report with priority matrix"
}
```

CLEAR Impact: -2 Expression, +1 Arrangement

### RCAF to SMILE (via CRAFT expansion)

```python
def rcaf_to_smile_craft(rcaf_prompt):
    """Convert RCAF to SMILE using CRAFT expansion"""
    
    # Expand RCAF to CRAFT first
    craft = {
        'context': rcaf_prompt.context,
        'role': rcaf_prompt.role,
        'action': rcaf_prompt.action,
        'format': rcaf_prompt.format,
        'target': infer_success_metrics(rcaf_prompt)
    }
    
    # Convert CRAFT to SMILE
    return format_as_smile(craft)
```

### JSON to SMILE Conversion

```python
def json_rcaf_to_smile(json_prompt):
    """Convert JSON RCAF to SMILE format"""
    
    smile = f"""
(: Task
  [: Role [ {json_prompt['role']} ] :]
  
  [: Context [
    {json_prompt['context']}
  ] :]
  
  [= {json_prompt['action']} =]
  
  [: Format [
    {{{json_prompt['format']}}}
  ] :]
) :)
""