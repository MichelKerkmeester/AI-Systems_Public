# Prompt - Patterns & Enhancements - v0.602

Comprehensive prompt engineering framework with RCAF/CRAFT patterns, CLEAR evaluation, advanced reasoning techniques, and performance-driven optimization strategies.

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

**For complete format specifications and token analysis → Prompt - JSON & SMILE Format Guide.md**

| Framework | Elements | Token Overhead | Clarity Score |
|-----------|----------|----------------|---------------|
| **RCAF** | 4 | Baseline | 9/10 |
| **CRAFT** | 5 | +10-15% | 7/10 |

---

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

**Real Example - Meeting Summary:**
```
Role: You are the Chief of Staff with executive communication expertise.
Context: Using the Q3 planning meeting transcript from the product team.
Action: Extract all decisions, risks, action items with owners, and key discussion points.
Format: Return exactly 7 bullets for executives - must include at least one risk and one decision. Use neutral, concise tone with no jargon.
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

**When to Choose CRAFT over RCAF:**
- Requirements exceed 5 distinct elements
- Multiple stakeholders involved
- Complex success criteria
- Detailed context essential
- Iterative refinement expected

### Pattern Comparison with CLEAR Scores

| Pattern | Avg CLEAR | Correctness | Logic | Expression | Arrangement | Reuse |
|---------|-----------|-------------|-------|------------|-------------|-------|
| **RCAF** | 43/50 | 8.5 | 8.0 | 9.5 | 9.0 | 8.0 |
| **CRAFT** | 41/50 | 9.0 | 9.0 | 7.5 | 8.0 | 7.5 |

### Chain-of-Thought Enhanced RCAF

**RCAF + CoT:**
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

### Creation Pattern with RCAF

**RCAF Creation:**
```
Role: Creative [role] with [specific expertise].
Context: Creating for [audience] to achieve [purpose].
Action: Create [specific deliverable] that meets these requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
Format: [Output format] with [specific elements].
```

---

## 3. ✅ CLEAR EVALUATION SYSTEM

### CLEAR Framework Overview

**Correctness, Logic/Coverage, Expression, Arrangement, Reuse**

Each dimension scored 1-10, total 50 points possible.

### Scoring Guide

**Correctness (C):**
- Accuracy of information
- Requirements captured
- Facts verified
- No hallucinations

**Logic/Coverage (L):**
- Complete requirement coverage
- Logical flow
- No gaps
- Dependencies addressed

**Expression (E):**
- Clarity of communication
- Conciseness
- Ambiguity elimination
- Appropriate tone

**Arrangement (A):**
- Structural organization
- Information hierarchy
- Section flow
- Visual clarity

**Reuse (R):**
- Template adaptability
- Pattern extraction
- Future applicability
- Parameterization

### CLEAR Application Examples

**High-Scoring RCAF Prompt (45/50):**
```
Role: Senior data analyst specializing in customer behavior.
Context: Q4 2024 sales data from e-commerce platform, 100K transactions.
Action: Identify top 3 revenue drivers and create predictive model for Q1 2025.
Format: Executive dashboard with bullet insights and visual charts.

CLEAR: C:9 L:8 E:10 A:9 R:9 = 45/50
```

**Lower-Scoring Vague Prompt (22/50):**
```
Analyze our data and give me insights about what's working.

CLEAR: C:4 L:3 E:5 A:5 R:5 = 22/50
```

### CLEAR-Based Improvement Process

1. **Baseline Score:** Evaluate original prompt
2. **Identify Weaknesses:** Find lowest scores
3. **Target Improvements:** Focus on weak dimensions
4. **Apply Framework:** Use RCAF/CRAFT appropriately
5. **Re-score:** Verify improvement
6. **Document:** Record score changes

---

## 4. 🧠 ADVANCED REASONING TECHNIQUES

### Chain-of-Thought (CoT) with RCAF

**RCAF-CoT Integration:**
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

**CLEAR Score: 44/50** (High expression and arrangement)

### Self-Consistency with RCAF

**RCAF Implementation:**
```
Role: Analytical expert generating multiple solution paths.
Context: [Problem requiring high confidence answer]
Action: Generate 5 different reasoning paths and identify consensus.
Format: 
Path 1: [reasoning] → Answer: [answer]
Path 2: [reasoning] → Answer: [answer]
Path 3: [reasoning] → Answer: [answer]
Path 4: [reasoning] → Answer: [answer]
Path 5: [reasoning] → Answer: [answer]
Consensus: [most common answer] (Confidence: X%)
```

### Few-Shot Learning with RCAF

**RCAF Few-Shot Template:**
```
Role: Pattern recognition expert.
Context: Learn from these examples to handle new case.
Action: Apply the pattern from examples to new input.
Format:
Example 1: Input: [x] → Output: [y]
Example 2: Input: [x] → Output: [y]
Now apply to: Input: [new] → Output: [generate]
```

### Zero-Shot CoT with RCAF

**Simplest RCAF-CoT:**
```
Role: Analytical thinker.
Context: [Complex question or task]
Action: Approach step-by-step for accuracy.
Format: Numbered reasoning steps with clear conclusion.
```

---

## 5. 📊 FORMAT EFFICIENCY

### Format Selection with Framework Pairing

| Framework | Best Format | Token Impact | CLEAR Impact |
|-----------|------------|--------------|--------------|
| **RCAF + Standard** | Default choice | Baseline | E:+2, A:+1 |
| **RCAF + JSON** | API/structured | +5-10% | C:+1, L:+1 |
| **CRAFT + Standard** | Complex natural | +10-15% | L:+2 |
| **CRAFT + SMILE** | Complex structured | +30-40% | L:+2, A:+1 |

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
        else:
            return 'standard', {'E': +2, 'A': +1}
    
    elif framework == 'CRAFT':
        if complexity > 7:
            return 'smile', {'L': +2, 'A': +1}
        else:
            return 'standard', {'L': +1}
```

**Format Reference:** For complete specifications → **Prompt - JSON & SMILE Format Guide.md**

---

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
    else:
        framework = 'CRAFT'
        target_clear = 40
    
    return determine_enhancement_approach(factors, framework, target_clear)
```

**Transform Phase with RCAF Priority:**
```
Create three enhancement levels:
1. Minimal: RCAF only (4 elements)
2. Standard: RCAF with depth
3. Comprehensive: CRAFT if needed
```

**Layer Phase with CLEAR Targeting:**
- Add elements that improve lowest CLEAR scores
- Apply RCAF first, CRAFT only if needed
- Include only value-adding layers

---

## 7. ⚙️ REACT PATTERN - REASONING & ACTION

### ReAct with RCAF Structure

**RCAF-ReAct Format:**
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

**CLEAR Score: 42/50** - Good structure and logic

### ReAct for Problem Solving with RCAF

```
Role: Systematic problem solver.
Context: Solving [complex problem] with unknown variables.
Action: Apply ReAct methodology:
- Think: Analyze current state
- Act: Take specific action
- Observe: Record results
- Repeat: Until solved
Format: Table with columns: Cycle | Thought | Action | Observation | Progress
```

---

## 8. 🌳 TREE OF THOUGHTS (TOT) PATTERN

### ToT with RCAF Framework

**RCAF-ToT Structure:**
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

**CLEAR Score: 43/50** - Excellent arrangement and logic

### ToT Evaluation Criteria with CLEAR

Each branch evaluated on:
- Feasibility (maps to Correctness)
- Completeness (maps to Coverage)
- Clarity (maps to Expression)
- Structure (maps to Arrangement)
- Scalability (maps to Reuse)

---

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
        
    def select_pattern(self, task_type, complexity, target_clear_score):
        if task_type == 'simple' and target_clear_score > 42:
            return 'rcaf'
        elif task_type == 'reasoning' and complexity > 5:
            return 'rcaf_cot'
        elif task_type == 'problem_solving':
            return 'rcaf_react'
        elif task_type == 'decision':
            return 'rcaf_tot'
        elif complexity > 7:
            return 'craft'
        else:
            return 'rcaf'
```

### Pattern Usage Tracking with CLEAR

| Pattern | Usage Rate | Success Rate | Avg CLEAR | Best Complexity | User Satisfaction |
|---------|------------|--------------|-----------|-----------------|-------------------|
| **RCAF** | 45% | 92% | 43/50 | 1-4 | 91% |
| **RCAF+CoT** | 20% | 90% | 44/50 | 4-6 | 88% |
| **CRAFT** | 15% | 88% | 41/50 | 7-10 | 85% |
| **RCAF+ReAct** | 10% | 87% | 42/50 | 5-7 | 86% |
| **RCAF+ToT** | 10% | 91% | 43/50 | 6-8 | 89% |

---

## 10. 📈 EVALUATION METRICS & OPTIMIZATION

### Comprehensive Evaluation Framework with CLEAR

| Metric Category | Target | Measurement | Optimization | CLEAR Dimension |
|-----------------|--------|-------------|--------------|-----------------|
| **Accuracy** | >95% | Task completion | RCAF precision | Correctness |
| **Coverage** | >90% | Requirements met | Framework choice | Logic/Coverage |
| **Clarity** | >90% | Ambiguity reduction | RCAF emphasis | Expression |
| **Structure** | >85% | Organization quality | Pattern selection | Arrangement |
| **Efficiency** | <200ms | Processing time | Simplification | All dimensions |
| **Reusability** | >80% | Template adaptation | Pattern extraction | Reuse |

### Performance Optimization Strategy with CLEAR

```python
def optimize_prompt_performance(prompt, clear_scores):
    """Optimize based on CLEAR weaknesses"""
    
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
    
    return prompt
```

---

## 11. 🚨 ERROR RECOVERY & REPAIR

### Pattern-Specific Error Recovery with CLEAR

| Error Type | Recognition | Recovery Pattern | CLEAR Fix | Prevention |
|------------|-------------|------------------|-----------|------------|
| **Ambiguity** | Multiple interpretations | Switch to RCAF | +3 Expression | Clear definitions |
| **Incomplete** | Missing requirements | Add CRAFT elements | +2 Coverage | Requirement checklist |
| **Over-complex** | Too many elements | Simplify to RCAF | +2 Expression | Complexity limit |
| **Logic Error** | Incorrect conclusion | Apply RCAF+CoT | +2 Correctness | Step validation |
| **Poor Structure** | Confusing organization | Restructure with RCAF | +3 Arrangement | Template use |

### Recovery Decision Framework with CLEAR

```python
def select_recovery_pattern(error_type, current_clear_scores):
    """Select recovery based on CLEAR scores"""
    
    recovery_matrix = {
        'ambiguity': ('rcaf', 'expression'),
        'incomplete': ('craft', 'coverage'),
        'over_complex': ('rcaf', 'expression'),
        'logic_error': ('rcaf_cot', 'correctness'),
        'poor_structure': ('rcaf', 'arrangement')
    }
    
    pattern, target_dimension = recovery_matrix.get(
        error_type, 
        ('rcaf', 'expression')
    )
    
    return pattern, target_dimension
```

---

## 12. 💡 META-PROMPTING TECHNIQUES

### Meta-Prompt Generator with RCAF/CLEAR

**RCAF Meta-Prompt:**
```
Role: Expert prompt engineer optimizing for clarity and effectiveness.
Context: Creating optimal prompt for: [task description]
Action: Generate RCAF-structured prompt considering:
- Appropriate reasoning pattern (CoT, ReAct, ToT)
- Optimal format (Standard, JSON, SMILE)
- Target CLEAR score of 43+/50
- Minimum complexity needed
Format: RCAF prompt with explanation of design choices and CLEAR score projection.
```

### Self-Improving Prompts with CLEAR

```
Role: Prompt improvement specialist.
Context: Original prompt: [prompt to improve]
Action: 
1. Score with CLEAR (show all 5 dimensions)
2. Identify lowest scoring dimensions
3. Apply RCAF to improve clarity
4. Re-score to verify improvement
Format: Before/After comparison with CLEAR scores and improvement explanation.
```

### RCAF vs CRAFT Decision Meta-Prompt

```
Role: Framework selection expert.
Context: Task requires [description of requirements]
Action: Determine optimal framework:
- If complexity ≤ 4: Use RCAF
- If complexity 5-6: Compare both, show trade-offs
- If complexity ≥ 7: Consider CRAFT
- Always prefer RCAF unless CRAFT adds clear value
Format: Framework recommendation with rationale and expected CLEAR score.
```

---

## 13. 🛡️ CONSTITUTIONAL AI PATTERNS

### Safety Integration with RCAF

**RCAF Safety Pattern:**
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

**CLEAR Score: 44/50** - High correctness and coverage

### Ethical Reasoning with RCAF

```
Role: Ethical decision advisor.
Context: Potentially sensitive request about [topic].
Action: Apply ethical framework:
1. Identify stakeholders
2. Assess potential harms
3. Consider alternatives
4. Apply ethical principles
5. Generate recommendation
Format: Ethical analysis with clear recommendation and rationale.
```

---

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

### Core Guidelines with CLEAR

| Principle | Description | Priority | CLEAR Focus |
|-----------|-------------|----------|-------------|
| **Clarity First** | RCAF's 4 elements beat CRAFT's 5 for clarity | 1.0 | Expression |
| **Complete Coverage** | Include all requirements | 0.9 | Logic/Coverage |
| **Correct Information** | Accuracy matters most | 0.9 | Correctness |
| **Structure Matters** | Good organization aids understanding | 0.8 | Arrangement |
| **Think Reuse** | Build adaptable patterns | 0.7 | Reuse |
| **Simplify Always** | Minimum complexity for maximum effect | 0.8 | Expression |
| **Measure Everything** | CLEAR scores drive improvement | 0.9 | All dimensions |

### The Ultimate Pattern Question

> "Does this pattern improve CLEAR scores without adding unnecessary complexity?"

**Decision Framework:**
```python
def should_use_pattern(task, pattern):
    current_clear = evaluate_without_pattern(task)
    projected_clear = evaluate_with_pattern(task, pattern)
    complexity_cost = calculate_complexity_increase(pattern)
    
    clear_improvement = projected_clear - current_clear
    
    # Pattern worth it if CLEAR improves by 5+ points
    # OR specific dimension improves by 2+ points
    return clear_improvement >= 5 or any(
        dim_improvement >= 2 
        for dim_improvement in dimension_improvements
    )
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

### Pattern Evolution Best Practices

1. **Start with RCAF** - Simplest effective pattern
2. **Add complexity only if needed** - CLEAR must improve by 5+
3. **Prefer RCAF variants** - RCAF+CoT over CRAFT when possible
4. **Measure with CLEAR** - Every enhancement scored
5. **Document patterns** - Build reusable library
6. **Challenge complexity** - Always ask "Could RCAF work?"
7. **Learn from scores** - Track what improves each dimension

### RCAF Transformation Examples

**Before (Vague):**
```
"Analyze customer data and tell me what's important"
CLEAR: 20/50
```

**After (RCAF):**
```
Role: Customer analytics specialist with churn prediction expertise.
Context: 12 months of subscription data for 50K SaaS customers.
Action: Identify top 3 churn indicators and segment at-risk customers.
Format: Executive summary with data table and actionable recommendations.
CLEAR: 45/50
```

**Improvement:** +25 points (125% improvement)
- Correctness: +3
- Coverage: +5
- Expression: +6
- Arrangement: +5
- Reuse: +6

**Format Guide:** For complete format specifications → **Prompt - JSON & SMILE Format Guide.md**

---

*Excellence through RCAF simplicity and CLEAR measurement. Every pattern has its purpose, but RCAF is the default. Complexity serves clarity, not ego. CLEAR scores drive decisions. For detailed format implementations, see Prompt - JSON & SMILE Format Guide.md*