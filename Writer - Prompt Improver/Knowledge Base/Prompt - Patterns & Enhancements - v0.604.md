# Prompt - Patterns & Enhancements - v0.604

Comprehensive prompt engineering framework with RCAF/CRAFT patterns, CLEAR evaluation, advanced reasoning techniques, and performance-driven optimization strategies with support for Standard, JSON, and YAML formats.

## 📋 Table of Contents

1. [🚀 QUICK TEMPLATES](#-quick-templates)
2. [📝 CORE PATTERNS - RCAF & CRAFT](#-core-patterns---rcaf--craft)
3. [✅ CLEAR EVALUATION SYSTEM](#-clear-evaluation-system)
4. [🧠 ADVANCED REASONING TECHNIQUES](#-advanced-reasoning-techniques)
5. [📊 FORMAT EFFICIENCY](#-format-efficiency)
6. [🎯 ATLAS-ENHANCED TECHNIQUES](#-atlas-enhanced-techniques)
7. [⚙️ REACT PATTERN - REASONING & ACTION](#-react-pattern---reasoning--action)
8. [🌳 TREE OF THOUGHTS (TOT) PATTERN](#-tree-of-thoughts-tot-pattern)
9. [🔄 PATTERN LEARNING & ADAPTATION](#-pattern-learning--adaptation)
10. [📈 EVALUATION METRICS & OPTIMIZATION](#-evaluation-metrics--optimization)
11. [🚨 ERROR RECOVERY & REPAIR](#-error-recovery--repair)
12. [💡 META-PROMPTING TECHNIQUES](#-meta-prompting-techniques)
13. [🛡️ CONSTITUTIONAL AI PATTERNS](#-constitutional-ai-patterns)
14. [🎓 KEY PRINCIPLES & PHILOSOPHY](#-key-principles--philosophy)

---

<a id="-quick-templates"></a>

## 1. 🚀 QUICK TEMPLATES

### Enhanced Template Matrix - RCAF Optimized

| Type | Purpose | Framework | CLEAR Target | Performance |
|------|---------|-----------|--------------|-------------|
| **Analysis** | Analyze topic focusing on aspects | RCAF | Expression: 9/10 | Speed: 100ms |
| **Creation** | Create deliverable for audience | RCAF | Arrangement: 9/10 | Speed: 200ms |
| **Solution** | Solve problem with approach | RCAF | Correctness: 9/10 | Speed: 150ms |
| **Research** | Research topic finding insights | RCAF/CRAFT | Coverage: 9/10 | Speed: 300ms |
| **Complex** | Multi-step workflow execution | CRAFT | All: 40+/50 | Speed: 400ms |

### RCAF Quick Template
```
Role: [One sentence expertise]
Context: [Essential background only]
Action: [Specific, measurable task]
Format: [Clear output requirements]
```

### Token Efficiency Reference

**For complete format specifications:**
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

| Framework | Elements | Token Overhead | Clarity Score |
|-----------|----------|----------------|---------------|
| **RCAF** | 4 | Baseline | 9/10 |
| **CRAFT** | 5 | +10-15% | 7/10 |

### Format Token Impact

| Format | Overhead | Best For |
|--------|----------|----------|
| **Standard** | Baseline | Natural language |
| **JSON** | +5-10% | APIs |
| **YAML** | +3-7% | Configuration |

---

<a id="-core-patterns---rcaf--craft"></a>

## 2. 📝 CORE PATTERNS - RCAF & CRAFT

### RCAF Pattern (Primary - Recommended)

**Role, Context, Action, Format - The Essential Four**

**Standard RCAF Template:**
```
Role: [Specific expertise in one sentence]
Context: [Essential information only - 1-2 sentences max]
Action: [Clear, specific, measurable task]
Format: [Output structure and requirements]
```

**YAML RCAF Template:**
```yaml
role: Specific expertise in one sentence
context: Essential information only - 1-2 sentences max
action: Clear, specific, measurable task
format: Output structure and requirements
```

**JSON RCAF Template:**
```json
{
  "role": "Specific expertise in one sentence",
  "context": "Essential information only - 1-2 sentences max",
  "action": "Clear, specific, measurable task",
  "format": "Output structure and requirements"
}
```

**Real Example - Meeting Summary:**

**Standard:**
```
Role: You are the Chief of Staff with executive communication expertise.
Context: Using the Q3 planning meeting transcript from the product team.
Action: Extract all decisions, risks, action items with owners, and key discussion points.
Format: Return exactly 7 bullets for executives - must include at least one risk and one decision. Use neutral, concise tone with no jargon.
```

**YAML:**
```yaml
role: Chief of Staff with executive communication expertise
context: Using the Q3 planning meeting transcript from the product team
action: Extract all decisions, risks, action items with owners, and key discussion points
format:
  structure: bullet_points
  count: 7
  requirements:
    - at least one risk
    - at least one decision
  tone: neutral, concise, no jargon
```

**CLEAR Score: 45/50**
- Correctness: 9/10
- Logic/Coverage: 8/10
- Expression: 10/10
- Arrangement: 9/10
- Reuse: 9/10

### CRAFT Pattern (Alternative - When Comprehensive Needed)

**Context, Role, Action, Format, Target - The Full Five**

**Standard CRAFT Template:**
```
Context: [Full background, assumptions, constraints]
Role: [Detailed expertise and perspective]
Action: [Comprehensive task breakdown]
Format: [Detailed output structure]
Target: [Success metrics and outcomes]
```

**YAML CRAFT Template:**
```yaml
context:
  background: Full situation description
  assumptions:
    - assumption one
    - assumption two
  constraints:
    - constraint one
    - constraint two
role:
  expertise: Detailed expertise description
  perspective: Specific viewpoint
action:
  primary: Main task
  subtasks:
    - subtask one
    - subtask two
format:
  structure: Detailed output type
  specifications:
    length: word count
    style: tone and voice
target:
  metrics:
    - metric one
    - metric two
  success_criteria: Definition of success
```

### Pattern Comparison with CLEAR Scores

| Pattern | Avg CLEAR | Correctness | Logic | Expression | Arrangement | Reuse | Best Format |
|---------|-----------|-------------|-------|------------|-------------|-------|-------------|
| **RCAF** | 43/50 | 8.5 | 8.0 | 9.5 | 9.0 | 8.0 | Standard/YAML |
| **CRAFT** | 41/50 | 9.0 | 9.0 | 7.5 | 8.0 | 7.5 | Standard |

### Chain-of-Thought Enhanced RCAF

**Standard RCAF + CoT:**
```
Role: As [expert], approach this step-by-step.
Context: [Situation requiring reasoning]
Action: 
1. First, identify [primary elements]
2. Then, analyze [relationships]
3. Consider [implications]
4. Finally, synthesize [conclusions]
Show reasoning at each step.
Format: [Structured reasoning output]
```

**YAML RCAF + CoT:**
```yaml
role: Expert approaching step-by-step
context: Situation requiring reasoning
action:
  steps:
    - identify: primary elements
    - analyze: relationships
    - consider: implications
    - synthesize: conclusions
  requirement: Show reasoning at each step
format: Structured reasoning output
```

---

<a id="-clear-evaluation-system"></a>

## 3. ✅ CLEAR EVALUATION SYSTEM

### CLEAR Framework Overview

**Correctness, Logic/Coverage, Expression, Arrangement, Reuse**

Each dimension scored 1-10, total 50 points possible.

### Format Impact on CLEAR Scores

| Format | Correctness | Logic | Expression | Arrangement | Reuse | Average |
|--------|-------------|-------|------------|-------------|-------|---------|
| **Standard** | 0 | 0 | +1 | 0 | 0 | 43/50 |
| **JSON** | +1 | +1 | -1 | +1 | +1 | 41/50 |
| **YAML** | 0 | +1 | 0 | +1 | +1 | 42/50 |

### CLEAR Application Examples

**High-Scoring RCAF Prompt (45/50):**

**Standard:**
```
Role: Senior data analyst specializing in customer behavior.
Context: Q4 2024 sales data from e-commerce platform, 100K transactions.
Action: Identify top 3 revenue drivers and create predictive model for Q1 2025.
Format: Executive dashboard with bullet insights and visual charts.
```

**YAML (43/50):**
```yaml
role: Senior data analyst specializing in customer behavior
context: Q4 2024 sales data from e-commerce platform, 100K transactions
action:
  primary: Identify top 3 revenue drivers
  secondary: Create predictive model for Q1 2025
format:
  type: executive_dashboard
  include:
    - bullet insights
    - visual charts
```

---

<a id="-advanced-reasoning-techniques"></a>

## 4. 🧠 ADVANCED REASONING TECHNIQUES

### Chain-of-Thought (CoT) with RCAF

**Standard RCAF-CoT Integration:**
```
Role: Expert problem solver using systematic reasoning.
Context: [Complex problem requiring step-by-step thinking]
Action: Solve by thinking through each step explicitly:
- Step 1: [Decompose problem]
- Step 2: [Analyze components]
- Step 3: [Build solution]
- Step 4: [Verify result]
Format: Show all reasoning with final answer highlighted.
```

**YAML RCAF-CoT:**
```yaml
role: Expert problem solver using systematic reasoning
context: Complex problem requiring step-by-step thinking
action:
  method: systematic_thinking
  steps:
    - step: 1
      action: Decompose problem
    - step: 2
      action: Analyze components
    - step: 3
      action: Build solution
    - step: 4
      action: Verify result
format:
  display: all_reasoning
  highlight: final_answer
```

**CLEAR Score: 44/50** (High expression and arrangement)

### Few-Shot Learning with RCAF

**Standard RCAF Few-Shot:**
```
Role: Pattern recognition expert.
Context: Learn from these examples to handle new case.
Action: Apply the pattern from examples to new input.
Format:
Example 1: Input: [x] → Output: [y]
Example 2: Input: [x] → Output: [y]
Now apply to: Input: [new] → Output: [generate]
```

**YAML RCAF Few-Shot:**
```yaml
role: Pattern recognition expert
context: Learn from these examples to handle new case
action: Apply the pattern from examples to new input
format:
  examples:
    - input: x1
      output: y1
    - input: x2
      output: y2
  apply_to:
    input: new_input
    output: generate
```

---

<a id="-format-efficiency"></a>

## 5. 📊 FORMAT EFFICIENCY

### Format Selection with Framework Pairing

| Framework | Best Format | Token Impact | CLEAR Impact | Use Case |
|-----------|------------|--------------|--------------|----------|
| **RCAF + Standard** | Default choice | Baseline | E:+2, A:+1 | Most prompts |
| **RCAF + JSON** | API/structured | +5-10% | C:+1, L:+1 | APIs |
| **RCAF + YAML** | Configuration | +3-7% | A:+1, R:+1 | Templates |
| **CRAFT + Standard** | Complex natural | +10-15% | L:+2 | Detailed |
| **CRAFT + JSON** | Complex structured | +15-20% | L:+2, A:+1 | Complex APIs |
| **CRAFT + YAML** | Complex config | +12-17% | L:+1, A:+1 | Complex templates |

### Format Selection Algorithm with CLEAR

```python
def select_optimal_format(framework, complexity, constraints):
    """
    Select format based on framework and requirements
    Returns format and expected CLEAR score impact
    """
    
    if framework == 'RCAF':
        if constraints.get('api_integration'):
            return 'json', {'C': +1, 'L': +1}
        elif constraints.get('human_editable'):
            return 'yaml', {'A': +1, 'R': +1}
        else:
            return 'standard', {'E': +2, 'A': +1}
    
    elif framework == 'CRAFT':
        if constraints.get('api_integration'):
            return 'json', {'L': +2, 'A': +1}
        elif constraints.get('template_system'):
            return 'yaml', {'L': +1, 'A': +1}
        else:
            return 'standard', {'L': +1}
```

**Format References:** For complete specifications:
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

---

<a id="-atlas-enhanced-techniques"></a>

## 6. 🎯 ATLAS-ENHANCED TECHNIQUES

### ATLAS-R Pattern with RCAF/CLEAR

**Assessment Phase with Framework Selection:**
```python
def assess_enhancement_need(prompt):
    factors = {
        'clarity': assess_clarity(prompt),
        'complexity': calculate_complexity(prompt),
        'structure_needed': needs_structure(prompt),
        'current_clear_score': evaluate_clear(prompt)
    }
    
    if factors['complexity'] <= 4:
        framework = 'RCAF'
        target_clear = 43
        format_rec = 'standard' if factors['clarity'] < 7 else 'yaml'
    else:
        framework = 'CRAFT'
        target_clear = 40
        format_rec = 'standard'
    
    return determine_enhancement_approach(factors, framework, target_clear, format_rec)
```

**Transform Phase with RCAF Priority:**
```
Create three enhancement levels:
1. Minimal: RCAF only (4 elements) - Standard format
2. Standard: RCAF with depth - Standard or YAML
3. Comprehensive: CRAFT if needed - Standard or JSON
```

---

<a id="-react-pattern---reasoning--action"></a>

## 7. ⚙️ REACT PATTERN - REASONING & ACTION

### ReAct with RCAF Structure

**Standard RCAF-ReAct Format:**
```
Role: Problem-solving agent using reasoning and action cycles.
Context: [Complex task requiring iterative approach]
Action: Execute ReAct cycles:

Thought 1: [reasoning about approach]
Action 1: [specific action to take]
Observation 1: [result of action]

Thought 2: [reasoning based on observation]
Action 2: [next action based on reasoning]
Observation 2: [result]

Continue until solution achieved.

Format: Document all thoughts, actions, and observations. Conclude with final answer.
```

**YAML RCAF-ReAct:**
```yaml
role: Problem-solving agent using reasoning and action cycles
context: Complex task requiring iterative approach
action:
  method: react_cycles
  cycles:
    - cycle: 1
      thought: reasoning about approach
      action: specific action to take
      observation: result of action
    - cycle: 2
      thought: reasoning based on observation
      action: next action based on reasoning
      observation: result
  termination: solution achieved
format:
  documentation: all cycles
  conclusion: final answer
```

**CLEAR Score: 42/50** - Good structure and logic

---

<a id="-tree-of-thoughts-tot-pattern"></a>

## 8. 🌳 TREE OF THOUGHTS (TOT) PATTERN

### ToT with RCAF Framework

**Standard RCAF-ToT Structure:**
```
Role: Strategic decision analyst exploring solution paths.
Context: [Complex decision with multiple approaches]
Action: Explore 3 solution branches:

Branch 1: [Approach A]
- Method: [description]
- Pros: [list]
- Cons: [list]
- Score: [1-10]

Branch 2: [Approach B]
- Method: [description]
- Pros: [list]
- Cons: [list]
- Score: [1-10]

Branch 3: [Approach C]
- Method: [description]
- Pros: [list]
- Cons: [list]
- Score: [1-10]

Format: Recommendation with rationale based on highest score.
```

**YAML RCAF-ToT:**
```yaml
role: Strategic decision analyst exploring solution paths
context: Complex decision with multiple approaches
action:
  method: tree_of_thoughts
  branches:
    - id: 1
      approach: A
      method: description
      pros:
        - pro one
        - pro two
      cons:
        - con one
        - con two
      score: 8
    - id: 2
      approach: B
      method: description
      pros:
        - pro one
      cons:
        - con one
      score: 7
    - id: 3
      approach: C
      method: description
      pros:
        - pro one
      cons:
        - con one
      score: 9
format:
  output: recommendation
  basis: highest_score
  include_rationale: true
```

**CLEAR Score: 43/50** - Excellent arrangement and logic

---

<a id="-pattern-learning--adaptation"></a>

## 9. 🔄 PATTERN LEARNING & ADAPTATION

### Adaptive Pattern Selection with CLEAR

```python
class PatternOptimizer:
    def __init__(self):
        self.pattern_performance = {
            'rcaf': {'success_rate': 0.92, 'avg_clear': 43, 'best_for': 'clarity'},
            'craft': {'success_rate': 0.88, 'avg_clear': 41, 'best_for': 'comprehensive'},
            'rcaf_cot': {'success_rate': 0.90, 'avg_clear': 44, 'best_for': 'reasoning'},
            'rcaf_react': {'success_rate': 0.87, 'avg_clear': 42, 'best_for': 'iterative'},
            'rcaf_tot': {'success_rate': 0.91, 'avg_clear': 43, 'best_for': 'decisions'}
        }
        
        self.format_performance = {
            'standard': {'usage': 0.60, 'satisfaction': 0.93},
            'json': {'usage': 0.20, 'satisfaction': 0.89},
            'yaml': {'usage': 0.20, 'satisfaction': 0.91}
        }
        
    def select_pattern(self, task_type, complexity, target_clear_score):
        if task_type == 'simple' and target_clear_score > 42:
            return 'rcaf', 'standard'
        elif task_type == 'config':
            return 'rcaf', 'yaml'
        elif task_type == 'api':
            return 'rcaf', 'json'
        elif task_type == 'reasoning' and complexity > 5:
            return 'rcaf_cot', 'standard'
        elif task_type == 'problem_solving':
            return 'rcaf_react', 'yaml'
        elif task_type == 'decision':
            return 'rcaf_tot', 'yaml'
        elif complexity > 7:
            return 'craft', 'standard'
        else:
            return 'rcaf', 'standard'
```

### Pattern Usage Tracking with CLEAR

| Pattern | Usage Rate | Success Rate | Avg CLEAR | Best Complexity | User Satisfaction | Preferred Format |
|---------|------------|--------------|-----------|-----------------|-------------------|------------------|
| **RCAF** | 45% | 92% | 43/50 | 1-4 | 91% | Standard/YAML |
| **RCAF+CoT** | 20% | 90% | 44/50 | 4-6 | 88% | Standard |
| **CRAFT** | 15% | 88% | 41/50 | 7-10 | 85% | Standard |
| **RCAF+ReAct** | 10% | 87% | 42/50 | 5-7 | 86% | YAML |
| **RCAF+ToT** | 10% | 91% | 43/50 | 6-8 | 89% | YAML |

---

<a id="-evaluation-metrics--optimization"></a>

## 10. 📈 EVALUATION METRICS & OPTIMIZATION

### Comprehensive Evaluation Framework with CLEAR

| Metric Category | Target | Measurement | Optimization | CLEAR Dimension |
|-----------------|--------|-------------|--------------|-----------------|
| **Accuracy** | >95% | Task completion | RCAF precision | Correctness |
| **Coverage** | >90% | Requirements met | Framework choice | Logic/Coverage |
| **Clarity** | >90% | Ambiguity reduction | RCAF emphasis | Expression |
| **Structure** | >85% | Organization quality | Pattern selection | Arrangement |
| **Efficiency** | <200ms | Processing time | Format selection | All dimensions |
| **Reusability** | >80% | Template adaptation | YAML templates | Reuse |

### Performance Optimization Strategy with CLEAR

```python
def optimize_prompt_performance(prompt, clear_scores, format_pref=None):
    """Optimize based on CLEAR weaknesses and format preferences"""
    
    optimizations = {
        'correctness': add_verification_steps,
        'coverage': expand_requirements,
        'expression': simplify_to_rcaf,
        'arrangement': restructure_sections,
        'reuse': parameterize_template
    }
    
    # Target lowest CLEAR dimension
    weakest = min(clear_scores, key=clear_scores.get)
    if clear_scores[weakest] < 7:
        prompt = optimizations[weakest](prompt)
    
    # Apply format optimization
    if format_pref == 'yaml' and clear_scores['reuse'] < 8:
        prompt = convert_to_yaml_template(prompt)
    
    return prompt
```

---

<a id="-error-recovery--repair"></a>

## 11. 🚨 ERROR RECOVERY & REPAIR

### Pattern-Specific Error Recovery with CLEAR

| Error Type | Recognition | Recovery Pattern | CLEAR Fix | Format Recommendation | Prevention |
|------------|-------------|------------------|-----------|----------------------|------------|
| **Ambiguity** | Multiple interpretations | Switch to RCAF | +3 Expression | Standard | Clear definitions |
| **Incomplete** | Missing requirements | Add CRAFT elements | +2 Coverage | YAML for structure | Requirement checklist |
| **Over-complex** | Too many elements | Simplify to RCAF | +2 Expression | Standard | Complexity limit |
| **Logic Error** | Incorrect conclusion | Apply RCAF+CoT | +2 Correctness | Standard | Step validation |
| **Poor Structure** | Confusing organization | Restructure with RCAF | +3 Arrangement | YAML | Template use |
| **Format Overhead** | Token explosion | Change format | +1 Expression | Standard | Monitor tokens |

### Recovery Decision Framework with CLEAR

```python
def select_recovery_pattern(error_type, current_clear_scores):
    """Select recovery based on CLEAR scores"""
    
    recovery_matrix = {
        'ambiguity': ('rcaf', 'expression', 'standard'),
        'incomplete': ('craft', 'coverage', 'yaml'),
        'over_complex': ('rcaf', 'expression', 'standard'),
        'logic_error': ('rcaf_cot', 'correctness', 'standard'),
        'poor_structure': ('rcaf', 'arrangement', 'yaml'),
        'format_overhead': ('rcaf', 'expression', 'standard')
    }
    
    pattern, target_dimension, format_rec = recovery_matrix.get(
        error_type, 
        ('rcaf', 'expression', 'standard')
    )
    
    return pattern, target_dimension, format_rec
```

---

<a id="-meta-prompting-techniques"></a>

## 12. 💡 META-PROMPTING TECHNIQUES

### Meta-Prompt Generator with RCAF/CLEAR

**Standard Meta-Prompt:**
```
Role: Expert prompt engineer optimizing for clarity and effectiveness.
Context: Creating optimal prompt for: [task description]
Action: Generate RCAF-structured prompt considering:
- Appropriate reasoning pattern (CoT, ReAct, ToT)
- Optimal format (Standard, JSON, YAML)
- Target CLEAR score of 43+/50
- Minimum complexity needed
Format: RCAF prompt with explanation of design choices and CLEAR score projection.
```

**YAML Meta-Prompt:**
```yaml
role: Expert prompt engineer optimizing for clarity and effectiveness
context:
  task: Creating optimal prompt for specified task
  constraints: Clarity and effectiveness priorities
action:
  generate: RCAF-structured prompt
  considerations:
    - reasoning_pattern: [CoT, ReAct, ToT]
    - format_options: [Standard, JSON, YAML]
    - target_clear: 43
    - complexity: minimum_needed
format:
  output: RCAF prompt
  include:
    - design_choices
    - clear_projection
```

### Format Decision Meta-Prompt

```yaml
role: Format selection expert
context: Task requires optimal format selection
action:
  evaluate:
    - api_integration: boolean
    - human_editing: boolean
    - template_reuse: boolean
    - token_budget: number
  recommend:
    if_api: json
    if_human_edit: yaml
    if_simple: standard
format:
  recommendation: format_choice
  rationale: explanation
  token_impact: percentage
```

---

<a id="-constitutional-ai-patterns"></a>

## 13. 🛡️ CONSTITUTIONAL AI PATTERNS

### Safety Integration with RCAF

**Standard Safety Pattern:**
```
Role: Responsible AI assistant with safety priorities.
Context: Request: [user request] | Safety considerations: [list]
Action: Process request while:
- Ensuring no harmful content
- Maintaining factual accuracy
- Protecting privacy
- Preventing bias
- Providing safe alternatives if needed
Format: Safe response with explanation if request modified.
```

**YAML Safety Pattern:**
```yaml
role: Responsible AI assistant with safety priorities
context:
  request: user request
  safety_considerations:
    - harmful content check
    - accuracy requirement
    - privacy protection
action:
  process: request
  while_ensuring:
    - no_harmful_content
    - factual_accuracy
    - privacy_protection
    - bias_prevention
  alternatives: provide if needed
format:
  response: safe_output
  explanation: if modified
```

**CLEAR Score: 44/50** - High correctness and coverage

---

<a id="-key-principles--philosophy"></a>

## 14. 🎓 KEY PRINCIPLES & PHILOSOPHY

### Framework Selection Hierarchy

```
        ┌─────────────────┐
        │      RCAF       │ (Default: 1-4 complexity, 70% of cases)
        ├─────────────────┤
        │   RCAF + CoT    │ (Reasoning: 4-6 complexity)
        ├─────────────────┤
        │  RCAF + ReAct   │ (Iterative: 5-7 complexity)
        ├─────────────────┤
        │   RCAF + ToT    │ (Decisions: 6-8 complexity)
        ├─────────────────┤
        │     CRAFT       │ (Comprehensive: 7+ complexity, 15% of cases)
        └─────────────────┘
```

### Format Selection Philosophy

```
        ┌─────────────────┐
        │    Standard     │ (Default: 60% of cases, maximum clarity)
        ├─────────────────┤
        │      YAML       │ (Config/Templates: 20%, human-editable)
        ├─────────────────┤
        │      JSON       │ (APIs: 20%, machine-parseable)
        └─────────────────┘
```

### Core Guidelines with CLEAR

| Principle | Description | Priority | CLEAR Focus | Format Choice |
|-----------|-------------|----------|-------------|---------------|
| **Clarity First** | RCAF's 4 elements beat CRAFT's 5 for clarity | 1.0 | Expression | Standard |
| **Complete Coverage** | Include all requirements | 0.9 | Logic/Coverage | Any |
| **Correct Information** | Accuracy matters most | 0.9 | Correctness | Any |
| **Structure Matters** | Good organization aids understanding | 0.8 | Arrangement | YAML |
| **Think Reuse** | Build adaptable patterns | 0.7 | Reuse | YAML |
| **Simplify Always** | Minimum complexity for maximum effect | 0.8 | Expression | Standard |
| **Measure Everything** | CLEAR scores drive improvement | 0.9 | All dimensions | Any |

### The Ultimate Pattern Question

> "Does this pattern improve CLEAR scores without adding unnecessary complexity?"

**Decision Framework:**
```python
def should_use_pattern(task, pattern, format):
    current_clear = evaluate_without_pattern(task)
    projected_clear = evaluate_with_pattern(task, pattern)
    format_overhead = calculate_format_tokens(format)
    
    clear_improvement = projected_clear - current_clear
    
    # Pattern worth it if CLEAR improves by 5+ points
    # OR specific dimension improves by 2+ points
    # AND format overhead is acceptable
    return (clear_improvement >= 5 or any(
        dim_improvement >= 2 
        for dim_improvement in dimension_improvements
    )) and format_overhead < 0.15
```

### Success Metrics Summary

**Excellent Prompt Engineering Achieves:**
- ✅ RCAF used 70%+ of the time
- ✅ Average CLEAR score > 43/50
- ✅ Expression score > 9/10
- ✅ Correctness > 9/10
- ✅ Right pattern for the task
- ✅ Optimal format selection
- ✅ Minimal complexity overhead
- ✅ 95%+ task completion accuracy
- ✅ Format overhead < 10% average

### RCAF Transformation Examples

**Before (Vague):**
```
"Analyze customer data and tell me what's important"
CLEAR: 20/50
```

**After - Standard (RCAF):**
```
Role: Customer analytics specialist with churn prediction expertise.
Context: 12 months of subscription data for 50K SaaS customers.
Action: Identify top 3 churn indicators and segment at-risk customers.
Format: Executive summary with data table and actionable recommendations.
CLEAR: 45/50
```

**After - YAML (RCAF):**
```yaml
role: Customer analytics specialist with churn prediction expertise
context: 12 months of subscription data for 50K SaaS customers
action:
  primary: Identify top 3 churn indicators
  secondary: Segment at-risk customers
format:
  type: executive_summary
  include:
    - data_table
    - actionable_recommendations
```
CLEAR: 43/50

**Improvement:** +25 points (125% improvement) for Standard, +23 for YAML

**Format Guides:** For complete format specifications:
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

---

*Excellence through RCAF simplicity and CLEAR measurement. Every pattern has its purpose, but RCAF is the default. Complexity serves clarity, not ego. CLEAR scores drive decisions. Standard format for clarity, YAML for configuration, JSON for APIs. For detailed format implementations, see format guide documents.*