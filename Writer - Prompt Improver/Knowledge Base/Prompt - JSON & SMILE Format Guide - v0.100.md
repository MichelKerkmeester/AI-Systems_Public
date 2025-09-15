# Prompt - JSON & SMILE Format Guide - v1.000

Comprehensive guide for JSON and SMILE format prompt engineering, covering syntax, best practices, conversion methods, and optimization strategies.

## 📋 Table of Contents

1. [🎯 OVERVIEW & PURPOSE](#-overview--purpose)
2. [📊 JSON FORMAT GUIDE](#-json-format-guide)
3. [😊 SMILE FORMAT GUIDE](#-smile-format-guide)
4. [🔄 FORMAT CONVERSION](#-format-conversion)
5. [⚖️ FORMAT COMPARISON & SELECTION](#-format-comparison--selection)
6. [🚀 ADVANCED TECHNIQUES](#-advanced-techniques)
7. [💡 EXAMPLES & TEMPLATES](#-examples--templates)
8. [📈 PERFORMANCE METRICS](#-performance-metrics)
9. [🔧 TROUBLESHOOTING](#-troubleshooting)
10. [🎓 BEST PRACTICES](#-best-practices)

---

## 1. 🎯 OVERVIEW & PURPOSE

### Why Alternative Formats?

**Standard Format:**
- Natural language prompts
- Maximum readability
- Baseline token usage
- Best for: Most general prompts

**JSON Format:**
- Structured data representation
- Machine-parseable
- Consistent field access
- Best for: APIs, systematic processing, structured outputs

**SMILE Format:**
- Semantic Markup for Instruction-oriented Language Expression
- Enhanced instruction following through visual structure
- Clear hierarchical organization
- Best for: Complex multi-step workflows, precise control

### Token Impact Summary

| Format | Token Overhead | Structure Benefit | Parse Reliability |
|--------|---------------|-------------------|-------------------|
| Standard | Baseline (0%) | Low | Good |
| JSON | +5-10% | Very High | Excellent |
| SMILE | +20-30% | High | Very Good |

---

## 2. 📊 JSON FORMAT GUIDE

### Core Principles

JSON prompting leverages structured data format to:
- **Eliminate ambiguity** through explicit key-value pairs
- **Ensure consistency** across similar requests
- **Enable programmatic generation** and processing
- **Facilitate API integration** with systems

### Basic Structure

```json
{
  "role": "Define the AI's expertise",
  "task": "Primary action to perform",
  "context": "Background information",
  "requirements": ["req1", "req2", "req3"],
  "constraints": ["limit1", "limit2"],
  "output": {
    "format": "desired structure",
    "length": "size requirements",
    "style": "tone and approach"
  }
}
```

### Advanced JSON Patterns

#### Nested Instructions
```json
{
  "task": "analyze_document",
  "steps": [
    {
      "step": 1,
      "action": "identify",
      "target": "key_themes",
      "method": "semantic_analysis"
    },
    {
      "step": 2,
      "action": "evaluate",
      "target": "arguments",
      "criteria": ["validity", "evidence", "logic"]
    }
  ],
  "output": {
    "summary": {"max_words": 200},
    "themes": {"count": 5},
    "evaluation": {"format": "structured"}
  }
}
```

#### Chain-of-Thought in JSON
```json
{
  "task": "solve_problem",
  "approach": "chain_of_thought",
  "show_reasoning": true,
  "steps": [
    "understand_problem",
    "identify_approach",
    "work_through_solution",
    "verify_answer"
  ],
  "format_reasoning": {
    "style": "numbered_steps",
    "include_justification": true
  }
}
```

#### Multi-Agent Coordination
```json
{
  "agents": [
    {
      "name": "researcher",
      "role": "gather_information",
      "output_to": "analyst"
    },
    {
      "name": "analyst",
      "role": "process_data",
      "input_from": "researcher",
      "output_to": "writer"
    },
    {
      "name": "writer",
      "role": "create_report",
      "input_from": "analyst"
    }
  ],
  "coordination": "sequential",
  "final_output": "comprehensive_report"
}
```

### JSON Best Practices

1. **Key Naming Conventions:**
   - Use `snake_case` for consistency
   - Be descriptive but concise
   - Avoid special characters

2. **Value Types:**
   - Strings for text instructions
   - Arrays for multiple items
   - Objects for nested structures
   - Booleans for flags

3. **Optimization Strategies:**
   - Minimize key length while maintaining clarity
   - Use arrays instead of numbered keys
   - Flatten deeply nested structures when possible

### When to Use JSON

✅ **Use JSON when:**
- Integrating with APIs
- Need consistent structure across prompts
- Processing outputs programmatically
- Working with technical teams
- Building systematic workflows

❌ **Avoid JSON when:**
- Creative writing tasks
- Open-ended exploration
- Conversational interactions
- Token budget is critical

---

## 3. 😊 SMILE FORMAT GUIDE

### SMILE Philosophy

SMILE (Semantic Markup for Instruction-oriented Language Expression) uses emoticon-like markers to create visual structure that enhances AI instruction following.

### Symbol Reference

| Symbol | Name | Purpose | Usage |
|--------|------|---------|-------|
| `(: :)` | Sections | Group related content | Major divisions |
| `[: :]` | Rigid Requirements | Strict instructions | Must-follow rules |
| `[= =]` | Exact Task | Core action definition | Primary objective |
| `[$ $]` | Variables | User input placeholders | Dynamic content |
| `[! !]` | Emphasis | Critical points | Priority items |
| `[? ?]` | Conditionals | Optional elements | If-then logic |
| `[@ @]` | References | External resources | Links/citations |
| `{...}` | AI Fills | Creative sections | Open generation |

### SMILE Structure Patterns

#### Basic Structure
```
(: Task Name
  [: Role [
    Define expertise and perspective
  ] :]
  
  [= Primary Task =]
  Main action to accomplish
  
  [: Requirements [
    • First requirement
    • Second requirement
    [! Critical requirement !]
  ] :]
  
  [: Output [
    {Generate content here}
  ] :]
) :)
```

#### Nested Hierarchy
```
(: Complex Project
  (: Phase 1
    [= Initial Setup =]
    [: Steps [
      1. First step
      2. Second step
    ] :]
  ) :)
  
  (: Phase 2
    [= Implementation =]
    [? If successful ?]
      Continue to next phase
    [? Otherwise ?]
      Return to Phase 1
  ) :)
) :)
```

#### Advanced SMILE Patterns

##### Multi-Step Workflow
```
(: Data Analysis Pipeline
  [: Configuration [
    [$ input_file $]: User provided
    [$ output_format $]: User specified
    [! Max processing time: 30 seconds !]
  ] :]
  
  (: Step 1: Load
    [= Load [$input_file$] =]
    [: Validation [
      Check format compatibility
      Verify data integrity
    ] :]
  ) :)
  
  (: Step 2: Process
    [= Transform data =]
    [: Methods [
      • Clean missing values
      • Normalize scales
      • [! Preserve original backup !]
    ] :]
  ) :)
  
  (: Step 3: Output
    [= Generate [$output_format$] =]
    {Create formatted output}
  ) :)
) :)
```

##### Conditional Logic
```
(: Decision Tree Task
  [= Evaluate situation =]
  
  [? If complexity > high ?]
    (: Complex Path
      [: Actions [
        Use advanced methods
        Apply deep analysis
      ] :]
    ) :)
  
  [? If complexity = medium ?]
    (: Standard Path
      Apply balanced approach
    ) :)
  
  [? Otherwise ?]
    (: Simple Path
      Use basic solution
    ) :)
) :)
```

### SMILE Depth Levels

| Level | Complexity | Symbol Usage | Token Impact |
|-------|-----------|--------------|--------------|
| **Minimal** | Low (1-3) | Basic sections only | +10-15% |
| **Moderate** | Medium (4-6) | Sections + emphasis | +20-25% |
| **Heavy** | High (7-10) | Full notation set | +25-35% |

### When to Use SMILE

✅ **Use SMILE when:**
- Complex multi-step processes
- Precise instruction following critical
- Hierarchical organization needed
- Clear visual structure helps
- Working with detailed workflows

❌ **Avoid SMILE when:**
- Simple, straightforward tasks
- Token budget is tight
- Creative, open-ended generation
- Conversational interactions

---

## 4. 🔄 FORMAT CONVERSION

### Standard to JSON

```python
def standard_to_json(prompt):
    """Convert natural language to JSON"""
    return {
        "role": extract_role(prompt),
        "task": extract_main_task(prompt),
        "context": extract_context(prompt),
        "requirements": extract_requirements_list(prompt),
        "output": extract_output_spec(prompt)
    }
```

**Example Conversion:**

Standard:
```
As a data scientist, analyze the sales dataset to identify trends and patterns. Focus on seasonal variations and customer segments. Provide a summary report with visualizations.
```

JSON:
```json
{
  "role": "data_scientist",
  "task": "analyze_sales_dataset",
  "focus": ["seasonal_variations", "customer_segments"],
  "output": {
    "type": "summary_report",
    "include": ["visualizations"]
  }
}
```

### Standard to SMILE

```python
def standard_to_smile(prompt):
    """Convert natural language to SMILE"""
    role = extract_role(prompt)
    task = extract_task(prompt)
    requirements = extract_requirements(prompt)
    
    return f"""
(: Task
  [: Role [ {role} ] :]
  [= {task} =]
  [: Requirements [
    {format_as_bullets(requirements)}
  ] :]
  [: Output [
    {{{extract_output(prompt)}}}
  ] :]
) :)
"""
```

### JSON to SMILE

```python
def json_to_smile(json_prompt):
    """Convert JSON to SMILE format"""
    smile = "(: Task\n"
    
    if "role" in json_prompt:
        smile += f"  [: Role [ {json_prompt['role']} ] :]\n"
    
    if "task" in json_prompt:
        smile += f"  [= {json_prompt['task']} =]\n"
    
    if "requirements" in json_prompt:
        smile += "  [: Requirements [\n"
        for req in json_prompt["requirements"]:
            smile += f"    • {req}\n"
        smile += "  ] :]\n"
    
    smile += ") :)"
    return smile
```

---

## 5. ⚖️ FORMAT COMPARISON & SELECTION

### Decision Matrix

```python
def select_optimal_format(complexity, use_case, constraints):
    """Select the best format for the task"""
    
    # API or programmatic use
    if use_case in ["api", "automation", "integration"]:
        return "json"
    
    # Complex multi-step workflows
    if complexity >= 7 or use_case == "workflow":
        return "smile"
    
    # Token constraints
    if constraints.get("token_limit_critical"):
        return "standard"
    
    # Default to standard for most cases
    return "standard"
```

### Format Strength Comparison

| Aspect | Standard | JSON | SMILE |
|--------|----------|------|-------|
| **Readability** | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| **Structure** | ★★☆☆☆ | ★★★★★ | ★★★★☆ |
| **Flexibility** | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| **Precision** | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| **Token Efficiency** | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| **Learning Curve** | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |

---

## 6. 🚀 ADVANCED TECHNIQUES

### Hybrid Approaches

#### JSON with Embedded Natural Language
```json
{
  "task": "write_article",
  "instructions": "Write a comprehensive article about climate change. Focus on recent developments and include scientific data.",
  "structure": {
    "introduction": "Hook the reader with a compelling fact",
    "body": ["recent_research", "impact_analysis", "solutions"],
    "conclusion": "Call to action"
  }
}
```

#### SMILE with JSON Data
```
(: Data Processing Task
  [: Configuration [
    ```json
    {
      "input": "data.csv",
      "output": "report.pdf",
      "filters": ["date>2024", "region=US"]
    }
    ```
  ] :]
  
  [= Process according to configuration =]
) :)
```

### Dynamic Format Selection

```python
class FormatOptimizer:
    def __init__(self):
        self.history = []
        
    def recommend_format(self, task):
        # Learn from past performance
        if self.history:
            success_rates = self.calculate_success_by_format()
            
        # Dynamic selection based on task characteristics
        if self.needs_structure(task):
            if self.is_technical(task):
                return "json"
            else:
                return "smile"
        
        return "standard"
```

---

## 7. 💡 EXAMPLES & TEMPLATES

### JSON Templates

#### Analysis Template
```json
{
  "role": "analyst",
  "task": "analyze",
  "data_source": "[SOURCE]",
  "analysis_type": "[TYPE]",
  "metrics": ["metric1", "metric2"],
  "output": {
    "format": "report",
    "sections": ["summary", "findings", "recommendations"],
    "visualizations": true
  }
}
```

#### Creation Template
```json
{
  "role": "creator",
  "task": "generate",
  "type": "[CONTENT_TYPE]",
  "audience": "[TARGET]",
  "requirements": {
    "length": "[SIZE]",
    "style": "[TONE]",
    "include": ["element1", "element2"]
  }
}
```

### SMILE Templates

#### Research Template
```
(: Research Project
  [: Setup [
    Topic: [$ research_topic $]
    Scope: [$ scope_definition $]
  ] :]
  
  [= Conduct Research =]
  
  [: Process [
    1. Literature review
    2. Data collection
    3. Analysis
    [! Verify sources !]
  ] :]
  
  [: Output [
    {Comprehensive research report}
  ] :]
) :)
```

#### Builder Template
```
(: Build [$ project_type $]
  [: Phase 1: MVP [
    [= Create minimal version =]
    • Core functionality only
    • Basic UI
    [! Test with users !]
  ] :]
  
  [? If successful ?]
    (: Phase 2: Enhancement
      Add features based on feedback
    ) :)
) :)
```

---

## 8. 📈 PERFORMANCE METRICS

### Format Effectiveness Tracking

| Metric | Standard | JSON | SMILE |
|--------|----------|------|-------|
| **Task Completion Rate** | 92% | 94% | 93% |
| **Instruction Following** | 85% | 90% | 95% |
| **Token Efficiency** | 100% | 92% | 75% |
| **User Satisfaction** | 90% | 85% | 82% |
| **Processing Speed** | Fast | Fast | Moderate |

### Optimization Metrics

```python
def calculate_format_efficiency(format_type, task_result):
    """Calculate efficiency score for format choice"""
    
    metrics = {
        'completion': task_result.completed,
        'accuracy': task_result.accuracy,
        'tokens_used': task_result.token_count,
        'time_taken': task_result.duration
    }
    
    # Weight factors
    weights = {
        'completion': 0.3,
        'accuracy': 0.3,
        'token_efficiency': 0.2,
        'speed': 0.2
    }
    
    return calculate_weighted_score(metrics, weights)
```

---

## 9. 🔧 TROUBLESHOOTING

### Common JSON Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| **Parse errors** | Invalid syntax | Validate JSON structure |
| **Over-nesting** | Too complex | Flatten structure |
| **Key confusion** | Ambiguous names | Use clear naming |
| **Type mismatch** | Wrong value types | Ensure consistency |

### Common SMILE Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| **Symbol confusion** | Wrong markers | Reference guide |
| **Over-complexity** | Too many levels | Simplify hierarchy |
| **Token explosion** | Heavy notation | Use moderate depth |
| **Unclear structure** | Poor organization | Reorganize sections |

### Format Migration Checklist

- [ ] Identify current format limitations
- [ ] Assess task complexity
- [ ] Calculate token budget
- [ ] Choose target format
- [ ] Convert systematically
- [ ] Test output quality
- [ ] Measure improvement

---

## 10. 🎓 BEST PRACTICES

### Universal Guidelines

1. **Start with Standard** - Default choice for most tasks
2. **Consider JSON** - When structure and consistency matter
3. **Apply SMILE** - For complex workflows needing precision
4. **Monitor tokens** - Track overhead vs. benefit
5. **Test formats** - Measure actual performance
6. **Document choice** - Record why format selected

### Format-Specific Tips

#### JSON Best Practices
- Keep keys short but clear
- Use consistent naming conventions
- Avoid deep nesting (max 3 levels)
- Include schema when complex
- Test parseability

#### SMILE Best Practices
- Match depth to complexity
- Use symbols semantically
- Maintain visual clarity
- Group related content
- Balance structure with readability

### The Golden Rule

> "The best format is invisible to the task. Choose based on genuine need, not novelty."

### Quick Decision Framework

```
Is it an API/integration task? → JSON
Is it a complex multi-step workflow? → SMILE
Is token efficiency critical? → Standard
Is creative freedom important? → Standard
Default choice? → Standard
```

---

*Excellence through intelligent format selection. Standard for clarity, JSON for structure, SMILE for precision. Every format has its purpose, every token has a cost, every choice should be intentional.*