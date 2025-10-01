# Prompt - Evaluation & Refinement - v0.610

Systematic quality assessment and improvement for optimizing prompts through CLEAR evaluation, automatic DEPTH processing, RCAF framework preference, and multi-format support including Standard, JSON, and YAML.

---

## 📋 Table of Contents

1. [✅ CLEAR EVALUATION SYSTEM (PRIMARY)](#-clear-evaluation-system-primary)
2. [⚡ QUICK EVAL WITH CLEAR](#-quick-eval-with-clear)
3. [📊 FULL EVALUATION PROCESS](#-full-evaluation-process)
4. [🎯 RCAF VS CRAFT EVALUATION](#-rcaf-vs-craft-evaluation)
5. [📄 FORMAT EVALUATION](#-format-evaluation)
6. [🧠 AUTOMATIC DEPTH REFINEMENT](#-automatic-depth-refinement)
7. [🚀 CHALLENGE-BASED REFINEMENT](#-challenge-based-refinement)
8. [🔍 REFINEMENT PATTERNS](#-refinement-patterns)
9. [💡 EXAMPLES](#-examples)
10. [📈 PERFORMANCE METRICS](#-performance-metrics)
11. [🎓 KEY PRINCIPLES](#-key-principles)

---

<a id="-clear-evaluation-system-primary"></a>

## 1. ✅ CLEAR EVALUATION SYSTEM (PRIMARY)

### The CLEAR Framework with Automatic DEPTH Processing

**Correctness, Logic/Coverage, Expression, Arrangement, Reuse**

CLEAR is the primary evaluation method for all prompt assessments. Each dimension is scored 1-10, with a total possible score of 50.

**AUTOMATIC PROCESSING:** All evaluations benefit from automatic DEPTH optimization.

```python
def validate_evaluation_prerequisites():
    """Automatic validation for evaluation with DEPTH"""
    
    prerequisites = {
        'depth_processing': True,  # Always automatic
        'methodology': 'DEPTH',
        'rounds': 10,
        'artifact_ready': self.artifact_format == 'text/markdown',
        'framework_identified': self.framework is not None
    }
    
    if not all(prerequisites.values()):
        failed = [k for k, v in prerequisites.items() if not v]
        print(f"Preparing evaluation. Setting up: {failed}")
        apply_depth_processing()
    
    return True
```

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

**DEPTH Enhancement:** +1-2 points per dimension through automatic optimization

### CLEAR Grade Scale

| Total Score | Grade | Interpretation | Action Required |
|-------------|-------|----------------|-----------------|
| 45-50 | A+ | Exceptional | Ship immediately |
| 40-44 | A | Excellent | Minor polish only |
| 35-39 | B | Good | Target weak areas |
| 30-34 | C | Adequate | Consider framework switch |
| 25-29 | D | Poor | Major refinement needed |
| <25 | F | Failing | Complete rewrite with RCAF |

---

<a id="-quick-eval-with-clear"></a>

## 2. ⚡ QUICK EVAL WITH CLEAR

### Rapid CLEAR Assessment with Automatic DEPTH Optimization

```python
def quick_clear_eval(prompt, format='standard'):
    """Quick CLEAR scoring with automatic DEPTH processing"""
    
    # Apply automatic DEPTH methodology
    apply_depth_processing()
    
    scores = {
        'correctness': score_requirements_captured(prompt) + 1,  # +1 from DEPTH
        'logic': score_completeness(prompt) + 1,
        'expression': score_clarity(prompt) + 1,
        'arrangement': score_structure(prompt) + 1,
        'reuse': score_adaptability(prompt) + 1
    }
    
    # Format adjustments
    if format == 'json':
        scores['correctness'] += 1
        scores['logic'] += 1
        scores['expression'] -= 1
        scores['arrangement'] += 1
        scores['reuse'] += 1
    elif format == 'yaml':
        scores['logic'] += 1
        scores['arrangement'] += 1
        scores['reuse'] += 1
    
    total = sum(scores.values())
    weakest = min(scores, key=scores.get)
    
    result = {
        'total': total,
        'grade': get_grade(total),
        'scores': scores,
        'priority_fix': weakest,
        'framework_rec': 'RCAF' if total < 35 else 'Current',
        'format_rec': recommend_format(scores),
        'processing': 'automatic_depth_applied'
    }
    
    # CRITICAL: Must deliver as artifact with minimal header
    return create_evaluation_artifact(result)
```

### Quick CLEAR Report Template

```markdown
Mode: $evaluate | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50

**QUICK CLEAR EVALUATION**

Current Score: [X]/50 (Grade: [A-F])
Processing: Automatic DEPTH applied

📊 **Scores:**
• Correctness: [X]/10
• Logic/Coverage: [X]/10  
• Expression: [X]/10
• Arrangement: [X]/10
• Reuse: [X]/10

**Strengths:** [Two highest dimensions]
**Priority Fix:** [Lowest dimension] → [Solution]
**Framework:** [RCAF recommended if < 35]
**Format:** [Optimal format based on scores]
**Quick Win:** [One immediate improvement]
```

### Quick Fix Matrix by CLEAR Dimension

| Weak Dimension | Quick Fix | Framework Switch | Format Recommendation | Expected Gain | Processing |
|----------------|-----------|------------------|----------------------|---------------|------------|
| Correctness | Add verification steps | Consider CRAFT | JSON for precision | +2-3 points | DEPTH-applied |
| Logic/Coverage | Fill requirement gaps | Consider CRAFT | YAML for structure | +2-3 points | DEPTH-applied |
| Expression | Simplify with RCAF | Switch to RCAF | Standard for clarity | +3-4 points | DEPTH-applied |
| Arrangement | Apply RCAF structure | Switch to RCAF | YAML for hierarchy | +2-3 points | DEPTH-applied |
| Reuse | Parameterize elements | Either framework | YAML for templates | +2-3 points | DEPTH-applied |

---

<a id="-full-evaluation-process"></a>

## 3. 📊 FULL EVALUATION PROCESS

### Comprehensive CLEAR Evaluation with Automatic DEPTH Processing

#### Step 1: Automatic DEPTH Processing Applied
```markdown
Processing: Automatic DEPTH (10 rounds)
Methodology: Discover → Engineer → Prototype → Test → Harmonize
Complexity: Level [X]
Artifact: Ready

**DEPTH processing enhances all dimensions by +1-2 points**
```

#### Step 2: Baseline CLEAR Scoring
```markdown
**BASELINE CLEAR SCORES (with DEPTH bonus):**
• C (Correctness): [X]/10 - [specific improvements]
• L (Logic/Coverage): [X]/10 - [gaps addressed]
• E (Expression): [X]/10 - [clarity enhanced]
• A (Arrangement): [X]/10 - [structure optimized]
• R (Reuse): [X]/10 - [adaptability improved]

**Total: [X]/50 - Grade: [A-F]**
**Current Format: [Standard/JSON/YAML]**
```

#### Step 3: Framework Assessment
```markdown
**FRAMEWORK ANALYSIS:**
Current: [None/RCAF/CRAFT/Other]
Elements: [Count and list]

RCAF Suitability: [X]/10
- Would 4 elements suffice? [Yes/No]
- Clarity gain potential: [+X points]

CRAFT Necessity: [X]/10
- Requires 5+ elements? [Yes/No]
- Coverage gain potential: [+X points]

**Recommendation:** [RCAF/CRAFT] for [+X CLEAR points]
**DEPTH optimization supports this choice**
```

#### Step 4: Format Analysis
```markdown
**FORMAT OPTIMIZATION:**

Current Format: [Standard/JSON/YAML]
Token Overhead: [Baseline/+X%]

Alternative Formats:
• Standard: E:+1, baseline tokens
• YAML: A:+1, R:+1, +3-7% tokens
• JSON: C:+1, L:+1, -1E, +5-10% tokens

**Best Format for Task:**
- API Integration: JSON
- Human Editing: YAML
- Maximum Clarity: Standard

**Recommendation:** [Format] for [reason]
```

#### Step 5: Enhancement Projection
```markdown
**PROJECTED IMPROVEMENTS:**

[With DEPTH processing applied]

With RCAF + [Format]:
• C: [Current] → [Projected] (+X)
• L: [Current] → [Projected] (+X)
• E: [Current] → [Projected] (+X)
• A: [Current] → [Projected] (+X)
• R: [Current] → [Projected] (+X)
Total: [Current] → [Projected] (+X)

**Best Path:** [RCAF/CRAFT] + [Format] for [total gain]
**DEPTH processing ensures optimal quality**
```

### Full Evaluation Report Template

```markdown
Mode: $evaluate | Complexity: [level] | Framework: [recommended] | CLEAR: [X]/50

**COMPREHENSIVE CLEAR EVALUATION**

Processing: Automatic DEPTH applied (10 rounds)
Current State: [X]/50 (Grade: [A-F])
Format: [Standard/JSON/YAML]

Detailed Scores (with DEPTH bonus):
• Correctness: [X]/10 - [strength/weakness]
• Logic/Coverage: [X]/10 - [strength/weakness]
• Expression: [X]/10 - [strength/weakness]
• Arrangement: [X]/10 - [strength/weakness]
• Reuse: [X]/10 - [strength/weakness]

**Framework Assessment:**
Current: [Framework]
Optimal: [RCAF/CRAFT]
Switch Benefit: +[X] points

**Format Assessment:**
Current: [Format]
Optimal: [Standard/JSON/YAML]
Switch Benefit: +[X] points, +[X]% tokens

**Priority Improvements:**
1. [Lowest dimension]: [Specific fix] (+X points)
2. [Second lowest]: [Specific fix] (+X points)
3. [Third area]: [Specific fix] (+X points)

**Recommended Action:**
[Apply RCAF / Enhance with CRAFT / Change format]

**Expected Outcome: [X]/50 → [Y]/50**
```

---

<a id="-rcaf-vs-craft-evaluation"></a>

## 4. 🎯 RCAF VS CRAFT EVALUATION

### Framework Comparison Scoring with Automatic DEPTH Processing

| Aspect | RCAF Impact | CRAFT Impact | Decision Factor | DEPTH Boost |
|--------|-------------|--------------|-----------------|-------------|
| **Correctness** | +0 to +1 | +1 to +2 | Detail needs | +1 from DEPTH |
| **Logic/Coverage** | -1 to 0 | +1 to +2 | Completeness needs | +1 from DEPTH |
| **Expression** | +2 to +3 | -1 to 0 | Clarity priority | +1 from DEPTH |
| **Arrangement** | +1 to +2 | 0 to +1 | Simplicity helps | +1 from DEPTH |
| **Reuse** | +1 to +2 | 0 to +1 | Cleaner templates | +1 from DEPTH |

### Framework Selection Based on CLEAR

```python
def select_framework_by_clear(current_scores, format='standard'):
    """Choose framework based on CLEAR with automatic DEPTH optimization"""
    
    # DEPTH processing enhances all scores
    apply_depth_processing()
    
    if current_scores['expression'] < 7:
        return 'RCAF', 'Low expression score needs simplicity'
    
    elif current_scores['logic'] < 7:
        if format == 'yaml':
            return 'Either', 'YAML helps organize complexity'
        return 'CRAFT', 'Low coverage needs comprehensiveness'
    
    elif current_scores['total'] < 35:
        return 'RCAF', 'Low overall score needs clarity focus'
    
    elif current_scores['total'] > 42:
        return 'Current', 'High score, maintain approach'
    
    else:
        return 'User choice', 'Both frameworks viable'
```

### RCAF vs CRAFT Decision Matrix

| Current CLEAR | Best Framework | Best Format | Rationale | Expected Gain | Processing |
|---------------|---------------|-------------|-----------|---------------|------------|
| < 30/50 | RCAF | Standard | Need clarity foundation | +8-12 points | DEPTH |
| 30-35/50 | RCAF | Standard/YAML | Simplification priority | +5-8 points | DEPTH |
| 35-40/50 | User choice | All viable | Both frameworks work | +3-5 points | DEPTH |
| 40-45/50 | Current | Current | Working well | +2-3 points | DEPTH |
| > 45/50 | Current | Current | Excellent already | +0-2 points | DEPTH |

---

<a id="-format-evaluation"></a>

## 5. 📄 FORMAT EVALUATION

### Format Impact on CLEAR Scores with DEPTH Processing

| Format | Correctness | Logic | Expression | Arrangement | Reuse | DEPTH Boost | Token Overhead |
|--------|-------------|-------|------------|-------------|-------|-------------|----------------|
| **Standard** | 0 | 0 | +1 | 0 | 0 | +5 total | 0% |
| **YAML** | 0 | +1 | 0 | +1 | +1 | +5 total | +3-7% |
| **JSON** | +1 | +1 | -1 | +1 | +1 | +5 total | +5-10% |

### Format Selection for CLEAR Optimization

```markdown
Mode: $evaluate | Complexity: Medium | Framework: [current] | CLEAR: [X]/50

**FORMAT EVALUATION**

Processing: Automatic DEPTH active
Current Format: [Standard/JSON/YAML]
Current CLEAR: [X]/50
DEPTH Bonus: +5 points applied

Format Projections:
• Standard: [Best for Expression]
  - Projected CLEAR: [X]/50
  - Token impact: Baseline
  - Use when: Maximum clarity needed
  
• YAML: [Best for Structure & Templates]
  - Projected CLEAR: [X]/50
  - Token impact: +3-7%
  - Use when: Human editing, configuration
  
• JSON: [Best for APIs]
  - Projected CLEAR: [X]/50
  - Token impact: +5-10%
  - Use when: System integration

**Recommendation:** [Format] for [reason]
```

### Format Decision Tree

```python
def select_optimal_format(clear_scores, use_case):
    """Select format based on CLEAR scores and use case"""
    
    # Apply DEPTH optimization
    apply_depth_processing()
    
    if use_case == 'api':
        return 'json', 'API integration priority'
    
    elif use_case == 'template':
        return 'yaml', 'Template reusability'
    
    elif use_case == 'config':
        return 'yaml', 'Human-editable configuration'
    
    elif clear_scores['expression'] < 7:
        return 'standard', 'Maximize clarity'
    
    elif clear_scores['reuse'] < 7:
        return 'yaml', 'Improve template adaptability'
    
    elif clear_scores['arrangement'] < 7:
        return 'yaml', 'Better structural hierarchy'
    
    else:
        return 'standard', 'Default for simplicity'
```

---

<a id="-automatic-depth-refinement"></a>

## 6. 🧠 AUTOMATIC DEPTH REFINEMENT

### DEPTH-Powered Refinement Process

#### Phase 1 - Discover (25% of processing)
- Apply 10-round DEPTH automatically
- Complete CLEAR scoring (all 5 dimensions)
- Evaluate current format effectiveness
- Identify lowest 2 dimensions
- Measure complexity (1-10 scale)

#### Phase 2 - Engineer (25% of processing)
- Create minimal version (RCAF + Standard)
- Create balanced version (RCAF + YAML)
- Create comprehensive version (CRAFT + Standard)
- Project CLEAR scores for each
- Apply DEPTH optimization to all

#### Phase 3 - Prototype (20% of processing)
- Add elements targeting lowest CLEAR scores
- Apply RCAF for Expression issues
- Apply CRAFT for Coverage issues
- Apply YAML for Arrangement issues
- Filter to only score-improving layers

#### Phase 4 - Test (20% of processing)
- Re-score all dimensions with DEPTH processing
- Verify improvements in weak areas
- Check for unintended score drops
- Evaluate format overhead
- Calculate net CLEAR gain

#### Phase 5 - Harmonize (10% of processing)
- Choose version with highest CLEAR
- Select optimal format
- Document score improvements
- Present as artifact with minimal header
- Record session pattern for learning

### CLEAR-Driven Refinement Process

```python
def refine_with_clear_focus(prompt, clear_scores, current_format):
    """Refinement with automatic DEPTH processing"""
    
    # Apply automatic DEPTH methodology
    depth_phases = {
        'discover': analyze_weaknesses,
        'engineer': generate_improvements,
        'prototype': build_enhancements,
        'test': validate_gains,
        'harmonize': finalize_prompt
    }
    
    weak_dimensions = get_lowest_two(clear_scores)
    
    refinements = {
        'correctness': (add_requirements_verification, 'json'),
        'logic': (fill_coverage_gaps, 'yaml'),
        'expression': (apply_rcaf_simplification, 'standard'),
        'arrangement': (restructure_with_rcaf, 'yaml'),
        'reuse': (extract_template_parameters, 'yaml')
    }
    
    for dimension in weak_dimensions:
        refinement_func, suggested_format = refinements[dimension]
        prompt = refinement_func(prompt)
        
        if current_format != suggested_format:
            consider_format_switch = True
        
    new_scores = evaluate_clear(prompt)
    improvement = new_scores['total'] - clear_scores['total']
    
    # CRITICAL: Deliver as artifact with minimal header
    result = create_refinement_artifact(
        prompt, 
        new_scores, 
        improvement, 
        suggested_format,
        processing='automatic_depth'
    )
    
    return result
```

---

<a id="-challenge-based-refinement"></a>

## 7. 🚀 CHALLENGE-BASED REFINEMENT

### Challenge Triggers by CLEAR Score

| CLEAR Score | Challenge Level | Action | Framework Push | Format Suggestion | Processing |
|-------------|----------------|--------|----------------|-------------------|------------|
| **45-50** | None | Polish only | Maintain | Keep current | Maintain |
| **40-44** | Gentle | Suggest refinements | Consider RCAF | Optimize format | DEPTH |
| **35-39** | Moderate | Recommend changes | Suggest RCAF | Suggest Standard/YAML | DEPTH |
| **30-34** | Strong | Push for overhaul | Switch to RCAF | Force Standard | DEPTH |
| **<30** | Aggressive | Complete rewrite | Force RCAF | Standard only | DEPTH |

### CLEAR-Based Challenge Templates

**High Score (40+):**
```
Processing: Automatic DEPTH applied
Current CLEAR: [X]/50 - Already excellent!
Format: [Current] working well

Minor enhancement possible:
- [Lowest dimension]: Could improve from [X] to [Y]
- Format switch to [alternative] might add +[X]

Worth the effort? (Automatic DEPTH refinement ready)
```

**Medium Score (30-39):**
```
Processing: Automatic DEPTH active
Current CLEAR: [X]/50 - Good, but could be better
Format: [Current] (+[X]% tokens)

Simplifying with RCAF + Standard could achieve:
- Expression: [Current] → [+3]
- Arrangement: [Current] → [+2]
- Total: [Current] → [Projected]

Or RCAF + YAML for templates:
- Arrangement: [Current] → [+2]
- Reuse: [Current] → [+2]
- Token cost: +3-7%

Switch approach? (DEPTH optimization will be applied)
```

**Low Score (<30):**
```
Processing: Automatic DEPTH engaged
Current CLEAR: [X]/50 - Significant improvement needed
Format contributing to confusion

RCAF + Standard restructuring recommended:
- Will improve Expression by +[X]
- Will improve Arrangement by +[X]
- Reduce token overhead to baseline
- Target: 40+/50

**Automatic refinement will apply 10-round DEPTH processing**
```

---

<a id="-refinement-patterns"></a>

## 8. 🔍 REFINEMENT PATTERNS

### Common CLEAR Improvements with Automatic DEPTH Processing

| Issue | CLEAR Impact | RCAF Fix | Format Solution | Score Gain | Processing |
|-------|--------------|----------|-----------------|------------|------------|
| **No artifact** | All:-5 | N/A | Force artifact | +5 | Auto-fix |
| **Vague requirements** | C:4, L:5 | Add specific Context/Action | Standard clarity | +4-5 points | DEPTH |
| **No role defined** | C:6, E:6 | Add clear Role | Any format | +2-3 points | DEPTH |
| **Poor structure** | A:4, E:5 | Apply RCAF format | YAML hierarchy | +4-5 points | DEPTH |
| **Over-complex** | E:4, A:5 | Simplify to RCAF | Standard only | +5-6 points | DEPTH |
| **Not reusable** | R:3 | Extract parameters | YAML template | +3-4 points | DEPTH |
| **API needs** | C:6 | Add precision | JSON structure | +2-3 points | DEPTH |

### RCAF Transformation Examples

**Before - Vague (CLEAR: 22/50):**
```
"Analyze our sales data and provide insights"

C:4 L:3 E:5 A:5 R:5 = 22/50
Format: None
[No DEPTH applied]
```

**After DEPTH Processing:**
```
Processing: Automatic DEPTH (10 rounds) applied
Creating artifact with minimal header...
```

**After - RCAF Standard (CLEAR: 45/50):**
```
Mode: $refine | Complexity: Medium | Framework: RCAF | CLEAR: 45/50

Role: Senior data analyst specializing in SaaS metrics.
Context: Q4 2024 sales data from our B2B platform (50K transactions).
Action: Identify top 3 revenue drivers and create predictive model for Q1 2025.
Format: Executive dashboard with bullet insights and supporting charts.
```

**Improvement:** +23 points (104% gain) with automatic DEPTH processing

---

<a id="-examples"></a>

## 9. 💡 EXAMPLES

### Example 1: Progressive CLEAR Improvement

**Initial Assessment:**
```
"Write a technical guide about machine learning"
CLEAR: C:3 L:4 E:5 A:4 R:4 = 20/50 (Grade: F)
Format: None
```

**Automatic DEPTH Processing Applied:**
```
Applying 10-round DEPTH methodology...
Phases: Discover → Engineer → Prototype → Test → Harmonize
Analyzing complexity: Level 5
Optimizing structure...
```

**Round 1 - Add RCAF + Standard:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 37/50

Role: ML educator with 10 years teaching experience.
Context: Writing for developers new to machine learning.
Action: Create comprehensive guide covering supervised/unsupervised learning.
Format: 2000-word tutorial with code examples and diagrams.
```

**Round 2 - Convert to YAML:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 40/50

role: ML educator with 10 years teaching experience
context: Writing for developers new to machine learning
action:
  main: Create comprehensive guide
  topics:
    - supervised_learning
    - unsupervised_learning
format:
  type: tutorial
  length: 2000_words
  include:
    - code_examples
    - diagrams
    - exercises
```

### Example 2: Framework and Format Comparison

**Same Task - Three Approaches:**

**RCAF + Standard (CLEAR: 43/50):**
```
Mode: $refine | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

Role: Customer success analyst with churn prediction expertise.
Context: 12 months subscription data, 10K B2B customers, 15% churn rate.
Action: Build churn prediction model and identify top 3 risk factors.
Format: Jupyter notebook with model code and executive summary.
```

**RCAF + YAML (CLEAR: 42/50):**
```
Mode: $refine | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

role: Customer success analyst with churn prediction expertise
context:
  data: 12 months subscription data
  customers: 10K B2B
  churn_rate: 15%
action:
  primary: Build churn prediction model
  secondary: Identify top 3 risk factors
format:
  deliverable: jupyter_notebook
  include:
    - model_code
    - executive_summary
```

**RCAF + JSON (CLEAR: 41/50):**
```
Mode: $refine | Complexity: Medium | Framework: RCAF | CLEAR: 41/50

{
  "role": "Customer success analyst with churn prediction expertise",
  "context": {
    "data_period": "12_months",
    "customer_count": 10000,
    "customer_type": "B2B",
    "churn_rate": 0.15
  },
  "action": {
    "primary": "Build churn prediction model",
    "secondary": "Identify top 3 risk factors"
  },
  "format": {
    "type": "jupyter_notebook",
    "components": ["model_code", "executive_summary"]
  }
}
```

**Analysis:** 
- Standard scores highest in Expression
- YAML balances structure and readability
- JSON best for precision but loses Expression
- All benefit from automatic DEPTH processing (+5 points)

---

<a id="-performance-metrics"></a>

## 10. 📈 PERFORMANCE METRICS

### CLEAR-Based KPIs with Automatic DEPTH Processing

**Processing Metrics:**
- Automatic DEPTH application: 100%
- Processing methodology: DEPTH (10 rounds)
- Optimization consistency: 100%
- Processing time: < 2 seconds

**Quality Targets:**
- Average CLEAR score: > 42/50
- Grade distribution: 60% A, 30% B, 10% C
- Expression average: > 8.5/10
- Correctness average: > 8.5/10
- No scores below 25/50

**Format Distribution Targets:**
- Standard: 55-65%
- YAML: 20-25%
- JSON: 15-20%

**Improvement Metrics:**
- Average gain per refinement: +8 points
- First-pass success (35+): > 70%
- Framework switch success: +5 points minimum
- Format optimization gain: +2 points average
- Weak dimension improvement: +2 minimum
- DEPTH processing bonus: +5 points consistent

### CLEAR Tracking Dashboard

```markdown
Mode: $evaluate | Complexity: N/A | Framework: N/A | CLEAR: N/A

**CLEAR PERFORMANCE DASHBOARD**

Processing: Automatic DEPTH (Always Active)
Methodology: 10-round optimization
Artifacts: Always Delivered with Minimal Header

📊 **Session Statistics:**
- Evaluations completed: [X]
- Average CLEAR: [X]/50
- Average improvement: +[X] points
- DEPTH consistency: 100%

📈 **Dimension Averages (with DEPTH bonus):**
- Correctness: [X]/10
- Logic/Coverage: [X]/10
- Expression: [X]/10 ⭐ [if highest]
- Arrangement: [X]/10
- Reuse: [X]/10

🎯 **Framework Performance:**
- RCAF average: [X]/50
- CRAFT average: [X]/50
- RCAF adoption: [X]%

📄 **Format Performance:**
- Standard: [X]% usage, [X]/50 avg
- YAML: [X]% usage, [X]/50 avg
- JSON: [X]% usage, [X]/50 avg

✅ **Success Metrics:**
- A grades: [X]%
- B grades: [X]%
- Improvement rate: [X]%
- Format optimization: [X]%

**Processing Status:** AUTOMATIC DEPTH OPTIMIZATION ACTIVE
```

---

<a id="-key-principles"></a>

## 11. 🎓 KEY PRINCIPLES

### Evaluation Philosophy

> "CLEAR scores tell the truth. Expression beats Coverage. Format serves purpose. Automatic DEPTH processing ensures quality. Minimal header delivers focus."

### Core Evaluation Principles

| Principle | Description | CLEAR Focus | Priority | Processing |
|-----------|-------------|-------------|----------|------------|
| **DEPTH First** | Always apply 10-round processing | All dimensions | 1.0 | Always |
| **Measure Always** | Score before and after | All dimensions | 0.95 | Required |
| **Expression Priority** | Clarity trumps completeness | E > L | 0.9 | Enhanced |
| **Framework Fit** | RCAF default, CRAFT when needed | E vs L balance | 0.8 | Optimized |
| **Format Purpose** | Match format to use case | Task-specific | 0.8 | Flexible |
| **Target Weakness** | Fix lowest scores first | Lowest 2 dims | 0.8 | Strategic |
| **Verify Gains** | Confirm improvements | Re-score always | 0.7 | Required |
| **Artifact Delivery** | Always use artifact format | All | 1.0 | MANDATORY |
| **Minimal Header** | Single line at top | All | 1.0 | MANDATORY |

### CLEAR Interpretation Guidelines

1. **Below 30/50:** Complete rewrite with RCAF + Standard needed
2. **30-35/50:** Major refinement with DEPTH processing
3. **35-40/50:** Good foundation, optimize format for task
4. **40-45/50:** Excellent, minor polish only
5. **45-50/50:** Exceptional, ship immediately

### Format Selection Guidelines

**Standard Format When:**
- Expression < 7 (clarity issues)
- Maximum human readability needed
- Token budget is critical
- Single-use prompt
- DEPTH processing confirms simplicity

**YAML Format When:**
- Arrangement < 7 (structure issues)
- Reuse < 7 (template needs)
- Human editing expected
- Configuration management
- DEPTH processing suggests structure helps

**JSON Format When:**
- Correctness < 7 (precision issues)
- API integration required
- Machine parsing needed
- Structured validation
- DEPTH processing indicates API use

### Success Criteria

**Excellent Evaluation Achieves:**
- ✅ Automatic DEPTH processing applied (10 rounds)
- ✅ Complete CLEAR scoring (all 5 dimensions)
- ✅ Framework recommendation based on scores
- ✅ Format optimization considered
- ✅ Token overhead calculated
- ✅ Clear improvement path identified
- ✅ Projected gains calculated
- ✅ Session patterns applied appropriately
- ✅ Minimum 35/50 achieved
- ✅ Appropriate format selected
- ✅ Delivered as artifact with minimal header

### The CLEAR Mantra

```
DEPTH processing first
Then measure with CLEAR

Correctness ensures accuracy
Logic provides coverage
Expression delivers clarity
Arrangement creates structure
Reuse enables scalability

Format amplifies strengths
Standard for clarity
YAML for structure
JSON for precision

Always in artifacts
Minimal header at top
Together: CLEAR excellence
Powered by automatic DEPTH
```