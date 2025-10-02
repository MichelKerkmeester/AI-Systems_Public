# Prompt - Evaluation & Refinement - v0.612

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

**Processing Modes:**
- **Standard:** Always 10 rounds for thorough analysis
- **Quick:** 1-5 rounds scaled by complexity

```python
def validate_evaluation_prerequisites():
    """Automatic validation for evaluation with DEPTH"""
    
    prerequisites = {
        'depth_processing': True,  # Always automatic
        'methodology': 'DEPTH',
        'rounds': 10,  # Standard mode
        'artifact_ready': self.artifact_format == 'text/markdown',
        'framework_identified': self.framework is not None,
        'header_has_dollar_prefix': self.header_format_valid
    }
    
    if not all(prerequisites.values()):
        failed = [k for k, v in prerequisites.items() if not v]
        print(f"Preparing evaluation. Setting up: {failed}")
        apply_depth_processing()
    
    return True
```

### Detailed Scoring Rubric

**CLEAR Scoring System:**
- Each dimension: 1-10 points (base score)
- 5 dimensions × 10 = 50 total possible
- DEPTH processing adds +1 per dimension = +5 total

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

### CLEAR Grade Scale

| Total Score | Base Range | With DEPTH (+5) | Grade | Interpretation | Action Required |
|-------------|------------|-----------------|-------|----------------|-----------------|
| 45-50 | 40-45 | 45-50 | A+ | Exceptional | Ship immediately |
| 40-44 | 35-39 | 40-44 | A | Excellent | Minor polish only |
| 35-39 | 30-34 | 35-39 | B | Good | Target weak areas |
| 30-34 | 25-29 | 30-34 | C | Adequate | Framework switch recommended |
| 25-29 | 20-24 | 25-29 | D | Poor | Major refinement needed |
| <25 | <20 | <25 | F | Failing | Complete rewrite with RCAF |

**Note:** Most prompts achieve 35-39 base (B), which becomes 40-44 (A) with DEPTH bonus.

---

<a id="-quick-eval-with-clear"></a>

## 2. ⚡ QUICK EVAL WITH CLEAR

### Rapid CLEAR Assessment with Automatic DEPTH Optimization

```python
def quick_clear_eval(prompt, format='standard'):
    """Quick CLEAR scoring with automatic DEPTH processing"""
    
    # Apply automatic DEPTH methodology (10 rounds standard)
    apply_depth_processing()
    
    base_scores = {
        'correctness': score_requirements_captured(prompt),
        'logic': score_completeness(prompt),
        'expression': score_clarity(prompt),
        'arrangement': score_structure(prompt),
        'reuse': score_adaptability(prompt)
    }
    
    # Apply DEPTH bonus: +1 per dimension
    final_scores = {
        dim: score + 1 for dim, score in base_scores.items()
    }
    
    # Format adjustments
    if format == 'json':
        final_scores['correctness'] += 1
        final_scores['logic'] += 1
        final_scores['expression'] -= 1
        final_scores['arrangement'] += 1
        final_scores['reuse'] += 1
    elif format == 'yaml':
        final_scores['logic'] += 1
        final_scores['arrangement'] += 1
        final_scores['reuse'] += 1
    
    base_total = sum(base_scores.values())
    final_total = sum(final_scores.values())
    weakest = min(base_scores, key=base_scores.get)
    
    result = {
        'base_total': base_total,
        'final_total': final_total,
        'depth_bonus': final_total - base_total,
        'grade': get_grade(final_total),
        'base_scores': base_scores,
        'final_scores': final_scores,
        'priority_fix': weakest,
        'framework_rec': 'RCAF' if final_total < 35 else 'Current',
        'format_rec': recommend_format(final_scores),
        'processing': 'automatic_depth_applied'
    }
    
    # CRITICAL: Must deliver as artifact with minimal header
    return create_evaluation_artifact(result)
```

### Quick CLEAR Report Template

```markdown
Mode: $evaluate | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50

**QUICK CLEAR EVALUATION**

Base Score: [X]/50 | With DEPTH: [X+5]/50 (Grade: [A-F])
Processing: Automatic DEPTH applied (10 rounds)

📊 **Scores:**
• Correctness: [X]/10 (base) → [X+1]/10 (with DEPTH)
• Logic/Coverage: [X]/10 (base) → [X+1]/10 (with DEPTH)
• Expression: [X]/10 (base) → [X+1]/10 (with DEPTH)
• Arrangement: [X]/10 (base) → [X+1]/10 (with DEPTH)
• Reuse: [X]/10 (base) → [X+1]/10 (with DEPTH)

**Strengths:** [Two highest dimensions]
**Priority Fix:** [Lowest dimension] → [Solution]
**Framework:** [RCAF recommended if < 35 with DEPTH]
**Format:** [Optimal format based on scores]
**Quick Win:** [One immediate improvement]
```

### Quick Fix Matrix by CLEAR Dimension

| Weak Dimension | Quick Fix | Framework Switch | Format Recommendation | Expected Base Gain | With DEPTH Total |
|----------------|-----------|------------------|----------------------|-------------------|-----------------|
| Correctness | Add verification steps | Consider CRAFT | JSON for precision | +2-3 points | +3-4 with DEPTH |
| Logic/Coverage | Fill requirement gaps | Consider CRAFT | YAML for structure | +2-3 points | +3-4 with DEPTH |
| Expression | Simplify with RCAF | Switch to RCAF | Standard for clarity | +3-4 points | +4-5 with DEPTH |
| Arrangement | Apply RCAF structure | Switch to RCAF | YAML for hierarchy | +2-3 points | +3-4 with DEPTH |
| Reuse | Parameterize elements | Either framework | YAML for templates | +2-3 points | +3-4 with DEPTH |

---

<a id="-full-evaluation-process"></a>

## 3. 📊 FULL EVALUATION PROCESS

### Comprehensive CLEAR Evaluation with Automatic DEPTH Processing

#### Step 1: Automatic DEPTH Processing Applied
```markdown
Processing: Automatic DEPTH (10 rounds standard, 1-5 quick)
Methodology: Discover → Engineer → Prototype → Test → Harmonize
Complexity: Level [X]
Artifact: Ready

**DEPTH processing enhances all dimensions by +1 point each (+5 total)**
```

#### Step 2: Baseline CLEAR Scoring
```markdown
**BASELINE CLEAR SCORES (before DEPTH bonus):**
• C (Correctness): [X]/10 - [specific assessment]
• L (Logic/Coverage): [X]/10 - [gaps identified]
• E (Expression): [X]/10 - [clarity notes]
• A (Arrangement): [X]/10 - [structure notes]
• R (Reuse): [X]/10 - [adaptability notes]

**Base Total: [X]/50**

**WITH DEPTH BONUS (+1 each):**
• C: [X+1]/10
• L: [X+1]/10
• E: [X+1]/10
• A: [X+1]/10
• R: [X+1]/10

**Final Total: [X+5]/50 - Grade: [A-F]**
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
• C: [Current] → [Projected] (+X base, +1 DEPTH)
• L: [Current] → [Projected] (+X base, +1 DEPTH)
• E: [Current] → [Projected] (+X base, +1 DEPTH)
• A: [Current] → [Projected] (+X base, +1 DEPTH)
• R: [Current] → [Projected] (+X base, +1 DEPTH)
Base Total: [Current] → [Projected] (+X)
Final Total: [Current+5] → [Projected+5] (+X)

**Best Path:** [RCAF/CRAFT] + [Format] for [total gain]
**DEPTH processing ensures +5 bonus**
```

### Full Evaluation Report Template

```markdown
Mode: $evaluate | Complexity: [level] | Framework: [recommended] | CLEAR: [X]/50

**COMPREHENSIVE CLEAR EVALUATION**

Processing: Automatic DEPTH applied (10 rounds)
Base Score: [X]/50 | With DEPTH: [X+5]/50 (Grade: [A-F])
Format: [Standard/JSON/YAML]

Detailed Scores (base → with DEPTH):
• Correctness: [X]/10 → [X+1]/10 - [strength/weakness]
• Logic/Coverage: [X]/10 → [X+1]/10 - [strength/weakness]
• Expression: [X]/10 → [X+1]/10 - [strength/weakness]
• Arrangement: [X]/10 → [X+1]/10 - [strength/weakness]
• Reuse: [X]/10 → [X+1]/10 - [strength/weakness]

**Framework Assessment:**
Current: [Framework]
Optimal: [RCAF/CRAFT]
Switch Benefit: +[X] base points, +[X+5] with DEPTH

**Format Assessment:**
Current: [Format]
Optimal: [Standard/JSON/YAML]
Switch Benefit: +[X] points, +[X]% tokens

**Priority Improvements:**
1. [Lowest dimension]: [Specific fix] (+X base, +X+1 with DEPTH)
2. [Second lowest]: [Specific fix] (+X base, +X+1 with DEPTH)
3. [Third area]: [Specific fix] (+X base, +X+1 with DEPTH)

**Recommended Action:**
[Apply RCAF / Enhance with CRAFT / Change format]

**Expected Outcome:**
Base: [X]/50 → [Y]/50
With DEPTH: [X+5]/50 → [Y+5]/50
```

---

<a id="-rcaf-vs-craft-evaluation"></a>

## 4. 🎯 RCAF VS CRAFT EVALUATION

### Framework Comparison Scoring with Automatic DEPTH Processing

| Aspect | RCAF Impact | CRAFT Impact | Decision Factor | DEPTH Boost |
|--------|-------------|--------------|-----------------|-------------|
| **Correctness** | +0 to +1 | +1 to +2 | Detail needs | +1 per framework |
| **Logic/Coverage** | -1 to 0 | +1 to +2 | Completeness needs | +1 per framework |
| **Expression** | +2 to +3 | -1 to 0 | Clarity priority | +1 per framework |
| **Arrangement** | +1 to +2 | 0 to +1 | Simplicity helps | +1 per framework |
| **Reuse** | +1 to +2 | 0 to +1 | Cleaner templates | +1 per framework |

### Framework Selection Based on CLEAR

```python
def select_framework_by_clear(base_scores, format='standard'):
    """Choose framework based on CLEAR with automatic DEPTH optimization"""
    
    # DEPTH processing enhances all scores (+1 each)
    apply_depth_processing()
    final_scores = {dim: score + 1 for dim, score in base_scores.items()}
    
    if base_scores['expression'] < 7:
        return 'RCAF', 'Low expression score needs simplicity'
    
    elif base_scores['logic'] < 7:
        if format == 'yaml':
            return 'Either', 'YAML helps organize complexity'
        return 'CRAFT', 'Low coverage needs comprehensiveness'
    
    elif sum(base_scores.values()) < 30:
        return 'RCAF', 'Low overall base score needs clarity focus'
    
    elif sum(final_scores.values()) > 42:
        return 'Current', 'High score with DEPTH, maintain approach'
    
    else:
        return 'User choice', 'Both frameworks viable'
```

### RCAF vs CRAFT Decision Matrix

| Base CLEAR | With DEPTH (+5) | Best Framework | Best Format | Rationale | Expected Gain |
|------------|----------------|---------------|-------------|-----------|---------------|
| < 25/50 | < 30/50 | RCAF | Standard | Need clarity foundation | +8-12 base |
| 25-30/50 | 30-35/50 | RCAF | Standard/YAML | Simplification priority | +5-8 base |
| 30-35/50 | 35-40/50 | User choice | All viable | Both frameworks work | +3-5 base |
| 35-40/50 | 40-45/50 | Current | Current | Working well | +2-3 base |
| > 40/50 | > 45/50 | Current | Current | Excellent already | +0-2 base |

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

Processing: Automatic DEPTH active (10 rounds)
Current Format: [Standard/JSON/YAML]
Base CLEAR: [X]/50
With DEPTH: [X+5]/50

Format Projections (all include +5 DEPTH bonus):
• Standard: [Best for Expression]
  - Base Projected: [X]/50
  - With DEPTH: [X+5]/50
  - Token impact: Baseline
  - Use when: Maximum clarity needed
  
• YAML: [Best for Structure & Templates]
  - Base Projected: [X]/50
  - With DEPTH: [X+5]/50
  - Token impact: +3-7%
  - Use when: Human editing, configuration
  
• JSON: [Best for APIs]
  - Base Projected: [X]/50
  - With DEPTH: [X+5]/50
  - Token impact: +5-10%
  - Use when: System integration

**Recommendation:** [Format] for [reason]
**All formats receive +5 DEPTH bonus**
```

### Format Decision Tree

```python
def select_optimal_format(clear_scores, use_case):
    """Select format based on CLEAR scores and use case"""
    
    # Apply DEPTH optimization (+1 per dimension)
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

#### Phase Distribution
**Standard Mode (10 rounds):**
- Phase 1 - Discover (Rounds 1-2, 25%): Complete CLEAR scoring, format evaluation
- Phase 2 - Engineer (Rounds 3-5, 25%): Create alternative versions
- Phase 3 - Prototype (Rounds 6-7, 20%): Add targeted improvements
- Phase 4 - Test (Rounds 8-9, 20%): Re-score, verify improvements
- Phase 5 - Harmonize (Round 10, 10%): Choose best version, deliver

**Quick Mode (1-5 rounds, scaled by complexity)**

#### Phase 1 - Discover (25% of processing)
- Apply DEPTH automatically based on mode
- Complete CLEAR scoring (all 5 dimensions)
- Evaluate current format effectiveness
- Identify lowest 2 dimensions
- Measure complexity (1-10 scale)

#### Phase 2 - Engineer (25% of processing)
- Create minimal version (RCAF + Standard)
- Create balanced version (RCAF + YAML)
- Create comprehensive version (CRAFT + Standard)
- Project CLEAR scores for each (base + DEPTH)
- Apply DEPTH optimization to all

#### Phase 3 - Prototype (20% of processing)
- Add elements targeting lowest CLEAR scores
- Apply RCAF for Expression issues
- Apply CRAFT for Coverage issues
- Apply YAML for Arrangement issues
- Filter to only score-improving layers

#### Phase 4 - Test (20% of processing)
- Re-score all dimensions with DEPTH processing
- Apply +1 per dimension (DEPTH bonus)
- Verify improvements in weak areas
- Check for unintended score drops
- Evaluate format overhead
- Calculate net CLEAR gain

#### Phase 5 - Harmonize (10% of processing)
- Choose version with highest CLEAR (with DEPTH)
- Select optimal format
- Document score improvements
- Present as artifact with minimal header
- Note DEPTH bonus applied

### CLEAR-Driven Refinement Process

```python
def refine_with_clear_focus(prompt, base_scores, current_format):
    """Refinement with automatic DEPTH processing"""
    
    # Apply automatic DEPTH methodology (10 rounds standard)
    depth_phases = {
        'discover': analyze_weaknesses,
        'engineer': generate_improvements,
        'prototype': build_enhancements,
        'test': validate_gains,
        'harmonize': finalize_prompt
    }
    
    weak_dimensions = get_lowest_two(base_scores)
    
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
        
    # Score with DEPTH bonus
    new_base_scores = evaluate_clear(prompt)
    new_final_scores = {dim: score + 1 for dim, score in new_base_scores.items()}
    
    base_improvement = sum(new_base_scores.values()) - sum(base_scores.values())
    final_improvement = sum(new_final_scores.values()) - sum(base_scores.values()) - 5
    
    # CRITICAL: Deliver as artifact with minimal header
    result = create_refinement_artifact(
        prompt, 
        new_base_scores,
        new_final_scores,
        base_improvement,
        suggested_format,
        processing='automatic_depth',
        depth_bonus=5
    )
    
    return result
```

---

<a id="-challenge-based-refinement"></a>

## 7. 🚀 CHALLENGE-BASED REFINEMENT

### Challenge Triggers by CLEAR Score

| Base CLEAR | With DEPTH | Challenge Level | Action | Framework Push | Format Suggestion |
|------------|-----------|----------------|--------|----------------|-------------------|
| **40-45** | **45-50** | None | Polish only | Maintain | Keep current |
| **35-39** | **40-44** | Gentle | Suggest refinements | Consider RCAF | Optimize format |
| **30-34** | **35-39** | Moderate | Recommend changes | Suggest RCAF | Standard/YAML |
| **25-29** | **30-34** | Strong | Push for overhaul | Switch to RCAF | Force Standard |
| **<25** | **<30** | Aggressive | Complete rewrite | Force RCAF | Standard only |

### CLEAR-Based Challenge Templates

**High Score (Base 40+, Final 45+):**
```
Processing: Automatic DEPTH applied (+5 bonus)
Base CLEAR: [X]/50 - Excellent foundation!
With DEPTH: [X+5]/50 - Outstanding!
Format: [Current] working well

Minor enhancement possible:
- [Lowest dimension]: Could improve from [X] to [Y]
- Format switch to [alternative] might add +[X]

Worth the effort? (Automatic DEPTH refinement ready)
```

**Medium Score (Base 30-39, Final 35-44):**
```
Processing: Automatic DEPTH active (+5 bonus)
Base CLEAR: [X]/50 - Good foundation
With DEPTH: [X+5]/50 - Solid performance
Format: [Current] (+[X]% tokens)

Simplifying with RCAF + Standard could achieve:
- Expression: [Current] → [+3 base, +4 with DEPTH]
- Arrangement: [Current] → [+2 base, +3 with DEPTH]
- Base Total: [Current] → [Projected]
- With DEPTH: [Current+5] → [Projected+5]

Or RCAF + YAML for templates:
- Arrangement: [Current] → [+2 base, +3 with DEPTH]
- Reuse: [Current] → [+2 base, +3 with DEPTH]
- Token cost: +3-7%

Switch approach? (DEPTH optimization will be applied)
```

**Low Score (Base <30, Final <35):**
```
Processing: Automatic DEPTH engaged (+5 bonus)
Base CLEAR: [X]/50 - Needs improvement
With DEPTH: [X+5]/50 - Still below target
Format contributing to confusion

RCAF + Standard restructuring recommended:
- Will improve Expression by +[X] base (+[X+1] with DEPTH)
- Will improve Arrangement by +[X] base (+[X+1] with DEPTH)
- Reduce token overhead to baseline
- Base Target: 40+/50
- With DEPTH Target: 45+/50

**Automatic refinement will apply 10-round DEPTH processing**
```

---

<a id="-refinement-patterns"></a>

## 8. 🔍 REFINEMENT PATTERNS

### Common CLEAR Improvements with Automatic DEPTH Processing

| Issue | Base CLEAR Impact | RCAF Fix | Format Solution | Base Gain | With DEPTH |
|-------|------------------|----------|-----------------|-----------|------------|
| **No artifact** | All:-5 | N/A | Force artifact | +5 | +10 with DEPTH |
| **Vague requirements** | C:4, L:5 | Add specific Context/Action | Standard clarity | +4-5 | +9-10 with DEPTH |
| **No role defined** | C:6, E:6 | Add clear Role | Any format | +2-3 | +7-8 with DEPTH |
| **Poor structure** | A:4, E:5 | Apply RCAF format | YAML hierarchy | +4-5 | +9-10 with DEPTH |
| **Over-complex** | E:4, A:5 | Simplify to RCAF | Standard only | +5-6 | +10-11 with DEPTH |
| **Not reusable** | R:3 | Extract parameters | YAML template | +3-4 | +8-9 with DEPTH |
| **API needs** | C:6 | Add precision | JSON structure | +2-3 | +7-8 with DEPTH |

### RCAF Transformation Examples

**Before - Vague (Base: 22/50, With DEPTH: 27/50):**
```
"Analyze our sales data and provide insights"

Base Scores:
C:4 L:3 E:5 A:5 R:5 = 22/50

With DEPTH:
C:5 L:4 E:6 A:6 R:6 = 27/50

Format: None
[DEPTH applied but insufficient base quality]
```

**After DEPTH Processing:**
```
Processing: Automatic DEPTH (10 rounds) applied
Creating artifact with minimal header...
```

**After - RCAF Standard (Base: 40/50, With DEPTH: 45/50):**
```
Mode: $refine | Complexity: Medium | Framework: RCAF | CLEAR: 45/50

Role: Senior data analyst specializing in SaaS metrics.
Context: Q4 2024 sales data from our B2B platform (50K transactions).
Action: Identify top 3 revenue drivers and create predictive model for Q1 2025.
Format: Executive dashboard with bullet insights and supporting charts.
```

**Base Scores:** C:9 L:8 E:9 A:9 R:5 = 40/50
**With DEPTH (+1 each):** C:10 L:9 E:10 A:10 R:6 = 45/50

**Improvement:** +18 base points (82% gain), +18 final points with DEPTH

---

<a id="-examples"></a>

## 9. 💡 EXAMPLES

### Example 1: Progressive CLEAR Improvement

**Initial Assessment:**
```
"Write a technical guide about machine learning"

Base: C:3 L:4 E:5 A:4 R:4 = 20/50 (Grade: F)
With DEPTH: C:4 L:5 E:6 A:5 R:5 = 25/50 (Grade: D)
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
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 42/50

Role: ML educator with 10 years teaching experience.
Context: Writing for developers new to machine learning.
Action: Create comprehensive guide covering supervised/unsupervised learning.
Format: 2000-word tutorial with code examples and diagrams.
```

**Base Scores:** C:8 L:8 E:9 A:8 R:4 = 37/50
**With DEPTH:** C:9 L:9 E:10 A:9 R:5 = 42/50

**Round 2 - Convert to YAML:**
```
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 45/50

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

**Base Scores:** C:9 L:9 E:9 A:9 R:4 = 40/50
**With DEPTH:** C:10 L:10 E:10 A:10 R:5 = 45/50

### Example 2: Framework and Format Comparison

**Same Task - Three Approaches:**

**RCAF + Standard (Base: 38/50, With DEPTH: 43/50):**
```
Mode: $refine | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

Role: Customer success analyst with churn prediction expertise.
Context: 12 months subscription data, 10K B2B customers, 15% churn rate.
Action: Build churn prediction model and identify top 3 risk factors.
Format: Jupyter notebook with model code and executive summary.
```

**RCAF + YAML (Base: 37/50, With DEPTH: 42/50):**
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

**RCAF + JSON (Base: 36/50, With DEPTH: 41/50):**
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
- Processing methodology: DEPTH (10 rounds standard, 1-5 quick)
- Optimization consistency: 100%
- DEPTH bonus application: +5 points every time

**Quality Targets:**
- Average base CLEAR: > 37/50
- Average with DEPTH: > 42/50
- Grade distribution: 60% A, 30% B, 10% C
- Expression average: > 8.5/10 base, > 9.5/10 with DEPTH
- Correctness average: > 8.5/10 base, > 9.5/10 with DEPTH
- No base scores below 20/50
- No final scores (with DEPTH) below 25/50

**Format Distribution Targets:**
- Standard: 55-65%
- YAML: 20-25%
- JSON: 15-20%

**Improvement Metrics:**
- Average base gain per refinement: +8 points
- Average final gain with DEPTH: +13 points
- First-pass success (base 35+): > 70%
- First-pass success (final 40+): > 85%
- Framework switch success: +5 base points minimum
- Format optimization gain: +2 base points average
- Weak dimension improvement: +2 minimum base
- DEPTH processing bonus: +5 points consistent

### CLEAR Tracking Dashboard

```markdown
Mode: $evaluate | Complexity: N/A | Framework: N/A | CLEAR: N/A

**CLEAR PERFORMANCE DASHBOARD**

Processing: Automatic DEPTH (Always Active, 10 rounds standard)
Methodology: 10-round optimization standard
Artifacts: Always Delivered with Minimal Header ($ prefix)

📊 **Session Statistics:**
- Evaluations completed: [X]
- Average base CLEAR: [X]/50
- Average with DEPTH: [X+5]/50
- Average improvement: +[X] base points
- DEPTH consistency: 100% (+5 every time)

📈 **Dimension Averages (base → with DEPTH):**
- Correctness: [X]/10 → [X+1]/10
- Logic/Coverage: [X]/10 → [X+1]/10
- Expression: [X]/10 → [X+1]/10 ⭐ [if highest]
- Arrangement: [X]/10 → [X+1]/10
- Reuse: [X]/10 → [X+1]/10

🎯 **Framework Performance:**
- RCAF base average: [X]/50
- RCAF with DEPTH: [X+5]/50
- CRAFT base average: [X]/50
- CRAFT with DEPTH: [X+5]/50
- RCAF adoption: [X]%

📄 **Format Performance:**
- Standard: [X]% usage, base [X]/50, final [X+5]/50
- YAML: [X]% usage, base [X]/50, final [X+5]/50
- JSON: [X]% usage, base [X]/50, final [X+5]/50

✅ **Success Metrics:**
- A grades (40-50 with DEPTH): [X]%
- B grades (35-39 with DEPTH): [X]%
- Improvement rate: [X]%
- Format optimization: [X]%

**Processing Status:** AUTOMATIC DEPTH OPTIMIZATION ACTIVE (+5 BONUS)
```

---

<a id="-key-principles"></a>

## 11. 🎓 KEY PRINCIPLES

### Evaluation Philosophy

> "CLEAR scores tell the truth. Expression beats Coverage. Format serves purpose. Automatic DEPTH processing ensures quality (+5 bonus). Minimal header delivers focus."

### Core Evaluation Principles

| Principle | Description | CLEAR Focus | Priority | DEPTH Impact |
|-----------|-------------|-------------|----------|--------------|
| **DEPTH First** | Always apply processing | All dimensions | 1.0 | +5 total |
| **Measure Always** | Score before and after | All dimensions | 0.95 | Enhanced |
| **Expression Priority** | Clarity trumps completeness | E > L | 0.9 | +1 per dim |
| **Framework Fit** | RCAF default, CRAFT when needed | E vs L balance | 0.8 | Optimized |
| **Format Purpose** | Match format to use case | Task-specific | 0.8 | Flexible |
| **Target Weakness** | Fix lowest scores first | Lowest 2 dims | 0.8 | Strategic |
| **Verify Gains** | Confirm improvements | Re-score always | 0.7 | Required |
| **Artifact Delivery** | Always use artifact format | All | 1.0 | MANDATORY |
| **Minimal Header** | Single line at top with $ | All | 1.0 | MANDATORY |

### CLEAR Interpretation Guidelines

**Score Ranges (Base → With DEPTH):**
1. **Below 25 → Below 30:** Complete rewrite with RCAF + Standard needed
2. **25-30 → 30-35:** Major refinement with DEPTH processing
3. **30-35 → 35-40:** Good foundation, optimize format for task
4. **35-40 → 40-45:** Excellent foundation, minor polish only
5. **40-45 → 45-50:** Exceptional, ship immediately

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
- ✅ Automatic DEPTH processing applied (10 rounds standard, 1-5 quick)
- ✅ Complete CLEAR scoring (all 5 dimensions, base + DEPTH)
- ✅ DEPTH bonus applied (+1 per dimension = +5 total)
- ✅ Framework recommendation based on scores
- ✅ Format optimization considered
- ✅ Token overhead calculated
- ✅ Clear improvement path identified
- ✅ Projected gains calculated (base + with DEPTH)
- ✅ Session patterns applied appropriately (current conversation only)
- ✅ Minimum base 35/50, target 40/50 with DEPTH
- ✅ Appropriate format selected
- ✅ Delivered as artifact with minimal header ($ prefix)

### The CLEAR Mantra

```
DEPTH processing first (+5 automatic)
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
Minimal header at top with $
Together: CLEAR excellence
Powered by automatic DEPTH
Every dimension +1 = Total +5
```