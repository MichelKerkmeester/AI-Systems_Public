# Prompt - Patterns & Enhancements - v0.612

Comprehensive prompt engineering framework with RCAF/CRAFT patterns, CLEAR evaluation, advanced reasoning techniques, and performance-driven optimization strategies with automatic DEPTH processing and support for Standard, JSON, and YAML formats.

**CRITICAL:** All patterns benefit from automatic 10-round DEPTH processing (1-5 rounds in quick mode). All enhancements must be delivered as artifacts with minimal header only.

---

## 📋 Table of Contents

1. [🚀 QUICK TEMPLATES](#-quick-templates)
2. [🔍 CORE PATTERNS - RCAF & CRAFT](#-core-patterns---rcaf--craft)
3. [✅ CLEAR EVALUATION SYSTEM](#-clear-evaluation-system)
4. [🧠 ADVANCED REASONING TECHNIQUES](#-advanced-reasoning-techniques)
5. [📊 OUTPUT STRUCTURE EFFICIENCY](#-output-structure-efficiency)
6. [🎯 DEPTH-ENHANCED TECHNIQUES](#-depth-enhanced-techniques)
7. [⚙️ REACT PATTERN - REASONING & ACTION](#-react-pattern---reasoning--action)
8. [🌳 TREE OF THOUGHTS (TOT) PATTERN](#-tree-of-thoughts-tot-pattern)
9. [📈 EVALUATION METRICS & OPTIMIZATION](#-evaluation-metrics--optimization)
10. [🚨 ERROR RECOVERY & REPAIR](#-error-recovery--repair)
11. [💡 META-PROMPTING TECHNIQUES](#-meta-prompting-techniques)
12. [🛡️ CONSTITUTIONAL AI PATTERNS](#-constitutional-ai-patterns)
13. [🎓 KEY PRINCIPLES & PHILOSOPHY](#-key-principles--philosophy)

---

<a id="-quick-templates"></a>

## 1. 🚀 QUICK TEMPLATES

### Automatic DEPTH Processing Foundation

**All templates benefit from automatic DEPTH optimization:**
```python
def apply_template_with_depth():
    """Every template gets automatic enhancement via DEPTH"""
    
    processing = {
        'methodology': 'DEPTH',
        'rounds': 10,  # Standard depth (1-5 for quick mode)
        'phases': ['Discover', 'Engineer', 'Prototype', 'Test', 'Harmonize'],
        'optimization': 'automatic',
        'quality_target': 'CLEAR 40+/50',
        'depth_bonus': '+5 total (+1 per dimension)'
    }
    
    return enhanced_template
```

### Enhanced Template Matrix - RCAF Optimized

| Type | Purpose | Framework | CLEAR Target (Base) | CLEAR with DEPTH | Processing |
|------|---------|-----------|-------------------|------------------|------------|
| **Analysis** | Analyze topic focusing on aspects | RCAF | 38+/50 | 43+/50 | DEPTH-optimized |
| **Creation** | Create deliverable for audience | RCAF | 37+/50 | 42+/50 | DEPTH applied |
| **Solution** | Solve problem with approach | RCAF | 38+/50 | 43+/50 | DEPTH analysis |
| **Research** | Research topic finding insights | RCAF/CRAFT | 37+/50 | 42+/50 | DEPTH-enhanced |
| **Complex** | Multi-step workflow execution | CRAFT | 35+/50 | 40+/50 | Full DEPTH |

### RCAF Quick Template
```
Role: [One sentence expertise]
Context: [Essential background only]
Action: [Specific, measurable task]
Format: [Clear output requirements]
```

**Delivered as artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

Role: [One sentence expertise]
Context: [Essential background only]
Action: [Specific, measurable task]
Format: [Clear output requirements]
```

### Token Efficiency Reference

**For complete format specifications:**
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

| Framework | Elements | Token Overhead | Clarity Score | Processing |
|-----------|----------|----------------|---------------|------------|
| **RCAF** | 4 | Baseline | 9/10 | DEPTH |
| **CRAFT** | 5 | +10-15% | 7/10 | DEPTH |

### Output Structure Token Impact

| Structure | Overhead | Best For | Enhancement |
|-----------|----------|----------|-------------|
| **Standard** | Baseline | Natural language | DEPTH-optimized |
| **JSON** | +5-10% | APIs | Structure enhanced |
| **YAML** | +3-7% | Configuration | Template ready |

---

<a id="-core-patterns---rcaf--craft"></a>

## 2. 🔍 CORE PATTERNS - RCAF & CRAFT

### Pattern Application with Automatic DEPTH Enhancement

```python
class PatternApplication:
    """Automatic DEPTH enhancement for all patterns"""
    
    def apply_pattern(self, pattern_type, content):
        # Automatic DEPTH processing
        self.processing_methodology = 'DEPTH'
        self.processing_rounds = 10  # Standard (1-5 for quick)
        self.optimization = 'automatic'
        self.depth_bonus = 5  # +1 per dimension
        
        # Execute DEPTH phases silently
        depth_phases = {
            'discover': self.analyze_requirements,
            'engineer': self.optimize_structure,
            'prototype': self.build_enhancement,
            'test': self.validate_quality,
            'harmonize': self.polish_final
        }
        
        # Verify prerequisites
        checks = {
            'artifact_prepared': self.artifact_format == 'text/markdown',
            'clear_baseline': self.baseline_clear_score is not None,
            'depth_active': self.depth_enabled
        }
        
        if not all(checks.values()):
            self.prepare_prerequisites()
            
        return self.enhance_with_pattern(pattern_type, content)
```

### RCAF Pattern (Primary - Recommended)

**Role, Context, Action, Format - The Essential Four**

**Standard RCAF Template:**
```
Role: [Specific expertise in one sentence]
Context: [Essential information only - 1-2 sentences max]
Action: [Clear, specific, measurable task]
Format: [Output structure and requirements]
```

**Artifact Format:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

Role: [Specific expertise in one sentence]
Context: [Essential information only - 1-2 sentences max]
Action: [Clear, specific, measurable task]
Format: [Output structure and requirements]
```

**YAML RCAF Artifact:**
```
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

role: Specific expertise in one sentence
context: Essential information only - 1-2 sentences max
action: Clear, specific, measurable task
format: Output structure and requirements
```

**JSON RCAF Artifact:**
```
Mode: $json | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

{
  "role": "Specific expertise in one sentence",
  "context": "Essential information only - 1-2 sentences max",
  "action": "Clear, specific, measurable task",
  "format": "Output structure and requirements"
}
```

**Real Example - Meeting Summary Artifact:**

```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 44/50

Role: You are the Chief of Staff with executive communication expertise.
Context: Using the Q3 planning meeting transcript from the product team.
Action: Extract all decisions, risks, action items with owners, and key discussion points.
Format: Return exactly 7 bullets for executives. Must include at least one risk and one decision. Use neutral, concise tone with no jargon.
```

### CRAFT Pattern (Alternative - When Comprehensive Needed)

**Context, Role, Action, Format, Target - The Full Five**

**Automatic Complexity Check:**
```python
if complexity < 7:
    print("RCAF might be clearer. Use simplified approach? (recommended)")
    if user_agrees:
        return use_rcaf_with_depth_optimization()
```

**Standard CRAFT Template:**
```
Context: [Full background, assumptions, constraints]
Role: [Detailed expertise and perspective]
Action: [Comprehensive task breakdown]
Format: [Detailed output structure]
Target: [Success metrics and outcomes]
```

**Artifact Format:**
```
Mode: $refine | Complexity: High | Framework: CRAFT | CLEAR: 41/50

Context: [Full background, assumptions, constraints]
Role: [Detailed expertise and perspective]
Action: [Comprehensive task breakdown]
Format: [Detailed output structure]
Target: [Success metrics and outcomes]
```

### Pattern Comparison with CLEAR Scores

**CLEAR Scoring System:**
- Each dimension: 1-10 points
- 5 dimensions × 10 = 50 total possible
- DEPTH processing adds +1 per dimension = +5 total

| Pattern | Avg CLEAR (Base) | With DEPTH | Correctness | Logic | Expression | Arrangement | Reuse | Best Format | Processing |
|---------|-----------------|------------|-------------|-------|------------|-------------|-------|-------------|------------|
| **RCAF** | 38/50 | 43/50 | 7.5 | 7.0 | 8.5 | 8.0 | 7.0 | Standard/YAML | DEPTH |
| **CRAFT** | 36/50 | 41/50 | 8.0 | 8.0 | 6.5 | 7.0 | 6.5 | Standard | DEPTH |

### Chain-of-Thought Enhanced RCAF

**Standard RCAF + CoT Artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 44/50

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

---

<a id="-clear-evaluation-system"></a>

## 3. ✅ CLEAR EVALUATION SYSTEM

### CLEAR Framework Overview

**Correctness, Logic/Coverage, Expression, Arrangement, Reuse**

**Scoring System:**
- Each dimension scored 1-10 points
- Total possible: 50 points (5 dimensions × 10)
- DEPTH processing adds +1 per dimension = +5 total
- Automatic scoring before and after enhancement
- Delivered in artifact header

**Score Targets:**
| Range | Status | Interpretation | Action Required |
|-------|--------|----------------|-----------------|
| **45-50** | Excellent | 90%+ quality | Ship immediately |
| **40-44** | Standard Target | 80-88% quality | Minor polish only |
| **35-39** | Minimum Viable | 70-78% quality | Target weak areas |
| **30-34** | Below Target | 60-68% quality | Consider framework switch |
| **<30** | Failing | <60% quality | Complete rewrite with RCAF |

### Detailed Scoring Rubric

#### Correctness (C) - Accuracy & Requirements
| Score | Description | Indicators |
|-------|-------------|------------|
| 9-10 | Perfect accuracy | All facts correct, requirements captured, no ambiguity |
| 7-8 | Mostly accurate | Minor clarifications needed, 90% correct |
| 5-6 | Adequate accuracy | Some errors, needs verification |
| 3-4 | Poor accuracy | Multiple errors, missing requirements |
| 1-2 | Incorrect | Fundamental misunderstandings |

#### Logic/Coverage (L) - Completeness & Flow
| Score | Description | Indicators |
|-------|-------------|------------|
| 9-10 | Complete coverage | All requirements addressed, perfect flow |
| 7-8 | Good coverage | Minor gaps, logical progression |
| 5-6 | Adequate coverage | Some gaps, logic mostly clear |
| 3-4 | Poor coverage | Major gaps, logic issues |
| 1-2 | Incomplete | Critical omissions |

#### Expression (E) - Clarity & Conciseness
| Score | Description | Indicators |
|-------|-------------|------------|
| 9-10 | Crystal clear | Perfect clarity, optimally concise |
| 7-8 | Clear | Minor ambiguities, well-expressed |
| 5-6 | Understandable | Some confusion, wordy |
| 3-4 | Unclear | Ambiguous, verbose |
| 1-2 | Confusing | Cannot understand intent |

#### Arrangement (A) - Structure & Organization
| Score | Description | Indicators |
|-------|-------------|------------|
| 9-10 | Perfect structure | Optimal organization, clear hierarchy |
| 7-8 | Good structure | Well-organized, minor improvements |
| 5-6 | Adequate structure | Basic organization present |
| 3-4 | Poor structure | Disorganized, hard to follow |
| 1-2 | No structure | Random, chaotic |

#### Reuse (R) - Adaptability & Templates
| Score | Description | Indicators |
|-------|-------------|------------|
| 9-10 | Highly reusable | Perfect template, easily adapted |
| 7-8 | Good reusability | Minor modifications needed |
| 5-6 | Some reusability | Moderate changes required |
| 3-4 | Limited reuse | Major rework needed |
| 1-2 | Single-use only | Not adaptable |

### Automatic DEPTH Processing Bonus

**DEPTH Enhancement:** +1 point per dimension through automatic optimization = +5 total

**Example:**
```
Base Scores:
- Correctness: 7/10
- Logic: 7/10
- Expression: 8/10
- Arrangement: 8/10
- Reuse: 6/10
Base Total: 36/50

With DEPTH Bonus (+1 each):
- Correctness: 8/10
- Logic: 8/10
- Expression: 9/10
- Arrangement: 9/10
- Reuse: 7/10
Final Total: 41/50 ✔
```

### CLEAR Application Example

**High-Scoring RCAF Artifact (45/50 with DEPTH):**

```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 45/50

Role: Senior data analyst specializing in customer behavior.
Context: Q4 2024 sales data from e-commerce platform, 100K transactions.
Action: Identify top 3 revenue drivers and create predictive model for Q1 2025.
Format: Executive dashboard with bullet insights and visual charts.
```

**Score Breakdown:**
- Base: 40/50 (C:8, L:8, E:9, A:8, R:7)
- With DEPTH: 45/50 (C:9, L:9, E:10, A:9, R:8)

---

<a id="-advanced-reasoning-techniques"></a>

## 4. 🧠 ADVANCED REASONING TECHNIQUES

### Reasoning Pattern with Automatic DEPTH Enhancement

```python
def apply_reasoning_pattern(pattern_type, content):
    """Apply reasoning patterns with automatic DEPTH optimization"""
    
    # All patterns get DEPTH processing
    depth_config = {
        'cot': {'rounds': 10, 'focus': 'step_by_step', 'bonus': 5},
        'few_shot': {'rounds': 10, 'focus': 'pattern_learning', 'bonus': 5},
        'react': {'rounds': 10, 'focus': 'iterative', 'bonus': 5},
        'tot': {'rounds': 10, 'focus': 'branching', 'bonus': 5}
    }
    
    pattern_config = depth_config.get(pattern_type)
    
    # Apply DEPTH enhancement silently
    return enhance_with_depth(content, pattern_config)
```

### Chain-of-Thought (CoT) with RCAF

**Standard RCAF-CoT Artifact:**
```
Mode: $improve | Complexity: High | Framework: RCAF | CLEAR: 44/50

Role: Expert problem solver using systematic reasoning.
Context: [Complex problem requiring step-by-step thinking]
Action: Solve by thinking through each step explicitly:
- Step 1: [Decompose problem]
- Step 2: [Analyze components]
- Step 3: [Build solution]
- Step 4: [Verify result]
Format: Show all reasoning with final answer highlighted.
```

### Few-Shot Learning with RCAF

**Standard RCAF Few-Shot Artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

Role: Pattern recognition expert.
Context: Learn from these examples to handle new case.
Action: Apply the pattern from examples to new input.
Format:
Example 1: Input: [x] → Output: [y]
Example 2: Input: [x] → Output: [y]
Now apply to: Input: [new] → Output: [generate]
```

---

<a id="-output-structure-efficiency"></a>

## 5. 📊 OUTPUT STRUCTURE EFFICIENCY

### Output Structure Selection with Framework Pairing

**Terminology:**
- **Framework** = Prompt organization (RCAF vs CRAFT)
- **Output Structure** = Data format (Standard vs JSON vs YAML)

| Framework | Best Structure | Token Impact | CLEAR Impact (Base) | CLEAR with DEPTH | Use Case | Processing |
|-----------|---------------|--------------|---------------------|------------------|----------|------------|
| **RCAF + Standard** | Default choice | Baseline | E:+2, A:+1 (38) | 43/50 | Most prompts | DEPTH-optimized |
| **RCAF + JSON** | API/structured | +5-10% | C:+1, L:+1 (36) | 41/50 | APIs | DEPTH-enhanced |
| **RCAF + YAML** | Configuration | +3-7% | A:+1, R:+1 (37) | 42/50 | Templates | DEPTH-structured |
| **CRAFT + Standard** | Complex natural | +10-15% | L:+2 (37) | 42/50 | Detailed | Deep DEPTH |
| **CRAFT + JSON** | Complex structured | +15-20% | L:+2, A:+1 (35) | 40/50 | Complex APIs | Full DEPTH |
| **CRAFT + YAML** | Complex config | +12-17% | L:+1, A:+1 (36) | 41/50 | Complex templates | Complete DEPTH |

### Output Structure Selection Algorithm with CLEAR

```python
def select_optimal_structure(framework, complexity, constraints):
    """
    Select structure based on framework and requirements
    Returns structure and expected CLEAR score impact
    """
    
    # DEPTH optimization ensures quality (+5 bonus)
    depth_bonus = 5  # +1 per dimension
    
    if framework == 'RCAF':
        if constraints.get('api_integration'):
            return 'json', {'C': +1 + 1, 'L': +1 + 1}  # +1 structure, +1 DEPTH each
        elif constraints.get('human_editable'):
            return 'yaml', {'A': +1 + 1, 'R': +1 + 1}
        else:
            return 'standard', {'E': +2 + 1, 'A': +1 + 1}
    
    elif framework == 'CRAFT':
        # Similar logic with DEPTH bonus
        pass
```

---

<a id="-depth-enhanced-techniques"></a>

## 6. 🎯 DEPTH-ENHANCED TECHNIQUES

### DEPTH Pattern with RCAF/CLEAR

**DEPTH Phases Applied Silently:**
```python
def apply_depth_enhancement(prompt):
    # Automatic DEPTH processing (hidden from user)
    processing = {
        'methodology': 'DEPTH',
        'rounds': 10,  # Standard (1-5 for quick)
        'optimization': 'automatic',
        'bonus': '+5 total (+1 per dimension)'
    }
    
    phases = {
        'discover': {
            'analyze_requirements': True,
            'identify_weaknesses': True,
            'map_context': True,
            'time': '25%'
        },
        'engineer': {
            'apply_framework': True,
            'optimize_structure': True,
            'select_approach': True,
            'time': '25%'
        },
        'prototype': {
            'build_enhancement': True,
            'apply_format': True,
            'ensure_completeness': True,
            'time': '20%'
        },
        'test': {
            'clear_scoring': True,
            'validate_requirements': True,
            'check_quality': True,
            'apply_depth_bonus': '+5',
            'time': '20%'
        },
        'harmonize': {
            'final_polish': True,
            'create_artifact': True,
            'time': '10%'
        }
    }
    
    # Execute silently
    for phase, config in phases.items():
        execute_phase_silently(phase, config)
    
    return enhanced_prompt
```

### DEPTH-Driven Enhancement Example

**User Input:** "Write analysis"

**DEPTH Processing (Hidden):**
- **D**iscover: Identify vague requirements, need for specificity
- **E**ngineer: Apply RCAF framework, optimize for clarity
- **P**rototype: Build structured enhancement
- **T**est: CLEAR score validation (base 38+, target 40+ with DEPTH)
- **H**armonize: Polish and deliver artifact

**Delivered Artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

Role: Business analyst with data visualization expertise.
Context: Using Q4 2024 performance metrics from all departments.
Action: Analyze trends, identify top 3 opportunities, and provide actionable recommendations.
Format: Executive report with visual dashboard and 5 key insights.
```

**Score Details:**
- Base scores: C:7, L:7, E:8, A:8, R:8 = 38/50
- With DEPTH (+5): C:8, L:8, E:9, A:9, R:9 = 43/50

---

<a id="-react-pattern---reasoning--action"></a>

## 7. ⚙️ REACT PATTERN - REASONING & ACTION

### ReAct with RCAF Structure

**Standard RCAF-ReAct Artifact:**
```
Mode: $improve | Complexity: High | Framework: RCAF | CLEAR: 42/50

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

**YAML RCAF-ReAct Artifact:**
```
Mode: $yaml | Complexity: High | Framework: RCAF | CLEAR: 42/50

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

---

<a id="-tree-of-thoughts-tot-pattern"></a>

## 8. 🌳 TREE OF THOUGHTS (TOT) PATTERN

### ToT with RCAF Framework

**Standard RCAF-ToT Artifact:**
```
Mode: $improve | Complexity: High | Framework: RCAF | CLEAR: 43/50

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

---

<a id="-evaluation-metrics--optimization"></a>

## 9. 📈 EVALUATION METRICS & OPTIMIZATION

### Comprehensive Evaluation Framework with CLEAR

| Metric Category | Target | Measurement | Optimization | CLEAR Dimension | Processing |
|-----------------|--------|-------------|--------------|-----------------|------------|
| **DEPTH Complete** | 100% | Application rate | Automatic | All | 10 rounds (1-5 quick) |
| **Artifact Delivery** | 100% | Success rate | Mandatory | All | Enhanced |
| **Accuracy** | >95% | Task completion | RCAF precision | Correctness | DEPTH-optimized |
| **Coverage** | >90% | Requirements met | Framework choice | Logic/Coverage | Deep DEPTH |
| **Clarity** | >90% | Ambiguity reduction | RCAF emphasis | Expression | Clear |
| **Structure** | >85% | Organization quality | Pattern selection | Arrangement | Organized |
| **Efficiency** | Optimal | Token management | Format selection | All dimensions | Optimized |
| **Reusability** | >80% | Template adaptation | YAML templates | Reuse | Flexible |

### Performance Optimization Strategy with CLEAR

```python
def optimize_prompt_performance(prompt, clear_scores, format_pref=None):
    """Optimize based on CLEAR weaknesses with automatic DEPTH enhancement"""
    
    # Automatic DEPTH ensures quality
    processing = {
        'methodology': 'DEPTH',
        'rounds': 10,
        'optimization': 'applied',
        'bonus': 5  # +1 per dimension
    }
    
    optimizations = {
        'correctness': add_verification_steps,
        'logic': expand_requirements,
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
    
    # Deliver as enhanced artifact with minimal header
    return create_optimized_artifact(prompt, processing)
```

### Session Pattern Tracking

```python
class SessionPatternTracker:
    """Track patterns within current session only"""
    
    def __init__(self):
        self.framework_choices = []
        self.format_choices = []
        self.clear_scores_base = []
        self.clear_scores_with_depth = []
        self.complexity_levels = []
        self.depth_rounds = []  # Track DEPTH processing
        
    def update(self, interaction):
        """Learn from current session"""
        self.framework_choices.append(interaction.framework)
        self.format_choices.append(interaction.format)
        self.clear_scores_base.append(interaction.clear_base)
        self.clear_scores_with_depth.append(interaction.clear_base + 5)
        self.complexity_levels.append(interaction.complexity)
        self.depth_rounds.append(10)  # Standard DEPTH
        
    def get_suggestions(self):
        """Provide session-based suggestions"""
        if len(self.framework_choices) >= 3:
            most_common_framework = max(set(self.framework_choices), 
                                       key=self.framework_choices.count)
            return f"You've preferred {most_common_framework} in this session"
        return None
```

### Pattern Usage Tracking with CLEAR

| Pattern | Usage Rate | Success Rate | Avg CLEAR (Base) | Avg CLEAR (DEPTH) | Best Complexity | User Satisfaction | Preferred Format | Processing |
|---------|------------|--------------|------------------|-------------------|-----------------|-------------------|------------------|------------|
| **RCAF** | 45% | 92% | 38/50 | 43/50 | 1-4 | 91% | Standard/YAML | DEPTH |
| **RCAF+CoT** | 20% | 90% | 39/50 | 44/50 | 4-6 | 88% | Standard | Deep DEPTH |
| **CRAFT** | 15% | 88% | 36/50 | 41/50 | 7-10 | 85% | Standard | Full DEPTH |
| **RCAF+ReAct** | 10% | 87% | 37/50 | 42/50 | 5-7 | 86% | YAML | Iterative DEPTH |
| **RCAF+ToT** | 10% | 91% | 38/50 | 43/50 | 6-8 | 89% | YAML | Branching DEPTH |

**NOTE:** All patterns benefit from automatic 10-round DEPTH processing (+5 CLEAR bonus).

---

<a id="-error-recovery--repair"></a>

## 10. 🚨 ERROR RECOVERY & REPAIR

### Pattern-Specific Error Recovery with CLEAR

| Error Type | Recognition | Recovery Pattern | CLEAR Fix | Format Recommendation | Prevention | Processing |
|------------|-------------|------------------|-----------|----------------------|------------|------------|
| **No Artifact** | Chat delivery | Force artifact | All | Any | Retry creation | Automatic |
| **Ambiguity** | Multiple interpretations | Switch to RCAF | +3 Expression | Standard | Clear definitions | DEPTH-enhanced |
| **Incomplete** | Missing requirements | Add CRAFT elements | +2 Coverage | YAML for structure | Requirement checklist | Deep DEPTH |
| **Over-complex** | Too many elements | Simplify to RCAF | +2 Expression | Standard | Complexity limit | Streamlined |
| **Logic Error** | Incorrect conclusion | Apply RCAF+CoT | +2 Correctness | Standard | Step validation | Reasoning DEPTH |
| **Poor Structure** | Confusing organization | Restructure with RCAF | +3 Arrangement | YAML | Template use | Organized |

### Recovery Decision Framework with CLEAR

```python
def select_recovery_pattern(error_type, current_clear_scores):
    """Select recovery based on CLEAR scores with automatic DEPTH fix"""
    
    # Automatic DEPTH processing handles recovery (+5 bonus)
    processing = {'rounds': 10, 'mode': 'recovery', 'bonus': 5}
    
    # Recovery matrix with DEPTH enhancement
    recovery_matrix = {
        'ambiguity': ('rcaf', 'expression', 'standard'),
        'incomplete': ('craft', 'logic', 'yaml'),
        'over_complex': ('rcaf', 'expression', 'standard'),
        'logic_error': ('rcaf_cot', 'correctness', 'standard'),
        'poor_structure': ('rcaf', 'arrangement', 'yaml'),
        'format_overhead': ('rcaf', 'expression', 'standard')
    }
    
    pattern, target_dimension, format_rec = recovery_matrix.get(
        error_type, 
        ('rcaf', 'expression', 'standard')
    )
    
    # Apply DEPTH enhancement automatically
    return apply_recovery_with_depth(pattern, target_dimension, format_rec)
```

---

<a id="-meta-prompting-techniques"></a>

## 11. 💡 META-PROMPTING TECHNIQUES

### Meta-Prompt Generator with RCAF/CLEAR

**Standard Meta-Prompt Artifact:**
```
Mode: $refine | Complexity: High | Framework: RCAF | CLEAR: 44/50

Role: Expert prompt engineer optimizing for clarity and effectiveness.
Context: Creating optimal prompt for: [task description]
Action: Generate RCAF-structured prompt considering:
- Appropriate reasoning pattern (CoT, ReAct, ToT)
- Optimal format (Standard, JSON, YAML)
- Target CLEAR score of 40+ base (45+ with DEPTH)
- Minimum complexity needed
- DEPTH optimization applied automatically
- Mandatory artifact delivery
Format: RCAF prompt with explanation of design choices and CLEAR score projection.
```

---

<a id="-constitutional-ai-patterns"></a>

## 12. 🛡️ CONSTITUTIONAL AI PATTERNS

### Safety Integration with RCAF

**Standard Safety Pattern Artifact:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

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

---

<a id="-key-principles--philosophy"></a>

## 13. 🎓 KEY PRINCIPLES & PHILOSOPHY

### Framework Selection Hierarchy

```
        ┌─────────────────┐
        │      RCAF       │ (Default: 1-4 complexity, 70% of cases)
        │  [DEPTH 10r]    │ [Automatic optimization, +5 bonus]
        ├─────────────────┤
        │   RCAF + CoT    │ (Reasoning: 4-6 complexity)
        │  [Deep DEPTH]   │ [Step-by-step enhancement, +5 bonus]
        ├─────────────────┤
        │  RCAF + ReAct   │ (Iterative: 5-7 complexity)
        │   [Iterative]   │ [Cycle optimization, +5 bonus]
        ├─────────────────┤
        │   RCAF + ToT    │ (Decisions: 6-8 complexity)
        │   [Branching]   │ [Path analysis, +5 bonus]
        ├─────────────────┤
        │     CRAFT       │ (Comprehensive: 7+ complexity, 15% of cases)
        │   [Full DEPTH]  │ [Complete coverage, +5 bonus]
        └─────────────────┘
```

### Output Structure Selection Philosophy

```
        ┌─────────────────┐
        │    Standard     │ (Default: 60% of cases, maximum clarity)
        │ [DEPTH-optimized]│ [+5 bonus, E:+2, A:+1]
        ├─────────────────┤
        │      YAML       │ (Config/Templates: 20%, human-editable)
        │ [DEPTH-structured]│ [+5 bonus, A:+1, R:+1]
        ├─────────────────┤
        │      JSON       │ (APIs: 20%, machine-parseable)
        │ [DEPTH-formatted] │ [+5 bonus, C:+1, L:+1]
        └─────────────────┘
```

### Core Guidelines with CLEAR

**CLEAR Scoring Reminder:**
- Each dimension: 1-10 points
- 5 dimensions × 10 = 50 total
- DEPTH bonus: +1 per dimension = +5 total

| Principle | Description | Priority | CLEAR Focus | Processing |
|-----------|-------------|----------|-------------|------------|
| **Automatic DEPTH** | 10-round processing handles optimization | 1.0 | All | Always |
| **Artifact Always** | Never deliver in chat | 1.0 | All | Mandatory |
| **Minimal Header Only** | Single line with $ prefix + content | 1.0 | All | Standard |
| **Clarity First** | RCAF's 4 elements beat CRAFT's 5 | 0.9 | Expression | DEPTH-enhanced |
| **Complete Coverage** | Include all requirements | 0.9 | Logic/Coverage | Deep DEPTH |
| **Correct Information** | Accuracy matters most | 0.9 | Correctness | Verified |
| **Structure Matters** | Good organization aids understanding | 0.8 | Arrangement | Organized |
| **Think Reuse** | Build adaptable patterns | 0.7 | Reuse | Flexible |
| **Simplify Always** | Minimum complexity for maximum effect | 0.8 | Expression | Streamlined |
| **Measure Everything** | CLEAR scores drive improvement | 0.9 | All dimensions | Tracked |

### The Ultimate Pattern Question

> "Does this pattern improve CLEAR scores without adding unnecessary complexity?"

**Decision Framework:**
```python
def should_use_pattern(task, pattern, format):
    # DEPTH processing ensures quality (+5 bonus)
    processing = {'rounds': 10, 'methodology': 'DEPTH', 'bonus': 5}
    
    current_clear = evaluate_without_pattern(task)
    projected_clear_base = evaluate_with_pattern(task, pattern)
    projected_clear_with_depth = projected_clear_base + 5
    format_overhead = calculate_format_tokens(format)
    
    clear_improvement = projected_clear_with_depth - current_clear
    
    # Pattern worth it if CLEAR improves by 5+ points
    # DEPTH optimization handles the rest
    return (clear_improvement >= 5 or any(
        dim_improvement >= 2 
        for dim_improvement in dimension_improvements
    )) and format_overhead < 0.15
```

### Success Metrics Summary

**Excellent Prompt Engineering Achieves:**
- ✅ 100% automatic DEPTH processing (10 rounds standard, 1-5 quick)
- ✅ 100% artifact delivery compliance
- ✅ 100% minimal header format with $ prefix (no extra sections)
- ✅ RCAF used 70%+ of the time
- ✅ Average CLEAR base score > 38/50
- ✅ Average CLEAR with DEPTH > 43/50
- ✅ Expression score > 9/10
- ✅ Correctness > 9/10 (with DEPTH)
- ✅ Right pattern for the task
- ✅ Optimal format selection
- ✅ Minimal complexity overhead
- ✅ 95%+ task completion accuracy
- ✅ Format overhead < 10% average

### RCAF Transformation Examples

**Before (Vague):**
```
"Analyze customer data and tell me what's important"
CLEAR Base: 20/50
```

**After - Artifact (DEPTH-Enhanced):**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 45/50

Role: Customer analytics specialist with churn prediction expertise.
Context: 12 months of subscription data for 50K SaaS customers.
Action: Identify top 3 churn indicators and segment at-risk customers.
Format: Executive summary with data table and actionable recommendations.
```

**Improvement:** 
- Base score: 40/50 (100% improvement)
- With DEPTH: 45/50 (125% improvement from original)

**Output Structure Guides:** For complete format specifications:
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**