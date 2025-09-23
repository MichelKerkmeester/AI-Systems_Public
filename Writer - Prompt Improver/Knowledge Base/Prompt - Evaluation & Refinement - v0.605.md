# Prompt - Evaluation & Refinement - v0.605

Systematic quality assessment and improvement for optimizing prompts through CLEAR evaluation as primary method, RCAF framework preference, ATLAS-powered refinement, and multi-format support including Standard, JSON, and YAML.

## 📋 Table of Contents

1. [✅ CLEAR EVALUATION SYSTEM (PRIMARY)](#-clear-evaluation-system-primary)
2. [⚡ QUICK EVAL WITH CLEAR](#-quick-eval-with-clear)
3. [📊 FULL EVALUATION PROCESS](#-full-evaluation-process)
4. [🎯 RCAF VS CRAFT EVALUATION](#-rcaf-vs-craft-evaluation)
5. [📄 FORMAT EVALUATION](#-format-evaluation)
6. [🧠 ATLAS-POWERED REFINEMENT](#-atlas-powered-refinement)
7. [🔄 PATTERN-BASED REFINEMENT](#-pattern-based-refinement)
8. [🚀 CHALLENGE-BASED REFINEMENT](#-challenge-based-refinement)
9. [🔍 REFINEMENT PATTERNS](#-refinement-patterns)
10. [💡 EXAMPLES](#-examples)
11. [📈 PERFORMANCE METRICS](#-performance-metrics)
12. [🎓 KEY PRINCIPLES](#-key-principles)

---

<a id="-clear-evaluation-system-primary"></a>

## 1. ✅ CLEAR EVALUATION SYSTEM (PRIMARY)

### The CLEAR Framework with Mandatory Prerequisites [UPDATED]

**Correctness, Logic/Coverage, Expression, Arrangement, Reuse**

CLEAR is the primary evaluation method for all prompt assessments. Each dimension is scored 1-10, with a total possible score of 50.

**CRITICAL PREREQUISITE:** Before ANY evaluation, thinking rounds MUST be collected.

```python
def validate_evaluation_prerequisites():
    """Mandatory checks before any evaluation"""
    
    prerequisites = {
        'thinking_rounds': self.thinking_rounds is not None,
        'artifact_ready': self.artifact_format == 'text/markdown',
        'user_consent': self.has_user_input
    }
    
    if not all(prerequisites.values()):
        failed = [k for k, v in prerequisites.items() if not v]
        print(f"CANNOT EVALUATE. Missing: {failed}")
        print("How many thinking rounds should I use? (1-10)")
        print("WAITING FOR YOUR INPUT...")
        return False
    
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

### Rapid CLEAR Assessment with Mandatory Setup [UPDATED]

```python
def quick_clear_eval(prompt, format='standard'):
    """Quick CLEAR scoring for rapid assessment"""
    
    # CRITICAL CHECKPOINT
    if not validate_evaluation_prerequisites():
        return None  # Cannot proceed without prerequisites
    
    scores = {
        'correctness': score_requirements_captured(prompt),  # 1-10
        'logic': score_completeness(prompt),                # 1-10
        'expression': score_clarity(prompt),                # 1-10
        'arrangement': score_structure(prompt),             # 1-10
        'reuse': score_adaptability(prompt)                # 1-10
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
        'thinking_rounds': self.thinking_rounds  # Include rounds used
    }
    
    # CRITICAL: Must deliver as artifact
    return create_evaluation_artifact(result)
```

### Quick CLEAR Report Template [UPDATED]

```markdown
**QUICK CLEAR EVALUATION: [X]/50 (Grade: [A-F])**

[✓ Thinking rounds: [X] used]
[✓ Artifact format: Markdown]

📊 **Scores:**
• Correctness: [X]/10
• Logic/Coverage: [X]/10  
• Expression: [X]/10
• Arrangement: [X]/10
• Reuse: [X]/10

**Format Impact:**
• Standard: Baseline (current)
• YAML: +1 Arrangement, +1 Reuse (+3-7% tokens)
• JSON: +1 Correctness, -1 Expression (+5-10% tokens)

**Strengths:** [Two highest dimensions]
**Priority Fix:** [Lowest dimension] → [Solution]
**Framework:** [RCAF recommended if < 35]
**Format:** [Optimal format based on scores]
**Quick Win:** [One immediate improvement]

Pattern: [User typically scores X in this dimension]

**Refinement Ready:** Specify thinking rounds for enhancement
```

### Quick Fix Matrix by CLEAR Dimension

| Weak Dimension | Quick Fix | Framework Switch | Format Recommendation | Expected Gain | Checkpoint |
|----------------|-----------|------------------|----------------------|---------------|------------|
| Correctness | Add verification steps | Consider CRAFT | JSON for precision | +2-3 points | Rounds needed |
| Logic/Coverage | Fill requirement gaps | Consider CRAFT | YAML for structure | +2-3 points | Rounds needed |
| Expression | Simplify with RCAF | Switch to RCAF | Standard for clarity | +3-4 points | Rounds needed |
| Arrangement | Apply RCAF structure | Switch to RCAF | YAML for hierarchy | +2-3 points | Rounds needed |
| Reuse | Parameterize elements | Either framework | YAML for templates | +2-3 points | Rounds needed |

---

<a id="-full-evaluation-process"></a>

## 3. 📊 FULL EVALUATION PROCESS

### Comprehensive CLEAR Evaluation with Checkpoints [UPDATED]

#### Step 0: Prerequisite Collection [NEW]
```markdown
**BEFORE EVALUATION:**

How many thinking rounds should I use for this evaluation? (1-10)

Based on complexity, I recommend: [X] rounds
- Simple eval: 1-2 rounds
- Standard eval: 3-4 rounds
- Deep analysis: 5-6 rounds

Please specify your preferred number:

[WAITING FOR INPUT - Cannot evaluate without this]
```

#### Step 1: Baseline CLEAR Scoring
```markdown
[✓ Thinking rounds: [X] collected]
[✓ Artifact format: Ready]

**BASELINE CLEAR SCORES:**
• C (Correctness): [X]/10 - [specific issues]
• L (Logic/Coverage): [X]/10 - [gaps identified]
• E (Expression): [X]/10 - [clarity problems]
• A (Arrangement): [X]/10 - [structure issues]
• R (Reuse): [X]/10 - [adaptability limits]

**Total: [X]/50 - Grade: [A-F]**
**Current Format: [Standard/JSON/YAML]**
```

#### Step 2: Framework Assessment
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
```

#### Step 3: Format Analysis
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

#### Step 4: Enhancement Projection
```markdown
**PROJECTED IMPROVEMENTS:**

[Based on [X] thinking rounds]

With RCAF + [Format]:
• C: [Current] → [Projected] (+X)
• L: [Current] → [Projected] (+X)
• E: [Current] → [Projected] (+X)
• A: [Current] → [Projected] (+X)
• R: [Current] → [Projected] (+X)
Total: [Current] → [Projected] (+X)

With CRAFT + [Format]:
• [Similar projection]

**Best Path:** [RCAF/CRAFT] + [Format] for [total gain]
```

### Full Evaluation Report Template [UPDATED]

```markdown
**COMPREHENSIVE CLEAR EVALUATION**

[✓ Thinking rounds: [X] applied]
[✓ Delivered as artifact]

┌─────────────────
**Current State: [X]/50 (Grade: [A-F])**
**Format: [Standard/JSON/YAML]**

Detailed Scores:
• Correctness: [X]/10
  - [Specific strength/weakness]
• Logic/Coverage: [X]/10
  - [Specific strength/weakness]
• Expression: [X]/10
  - [Specific strength/weakness]
• Arrangement: [X]/10
  - [Specific strength/weakness]
• Reuse: [X]/10
  - [Specific strength/weakness]

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

**Ready for Refinement:** Confirm thinking rounds to proceed
└─────────────────
```

---

<a id="-rcaf-vs-craft-evaluation"></a>

## 4. 🎯 RCAF VS CRAFT EVALUATION

### Framework Comparison Scoring with Prerequisites [UPDATED]

| Aspect | RCAF Impact | CRAFT Impact | Decision Factor | Checkpoint |
|--------|-------------|--------------|-----------------|------------|
| **Correctness** | +0 to +1 | +1 to +2 | Detail needs | Rounds required |
| **Logic/Coverage** | -1 to 0 | +1 to +2 | Completeness needs | Rounds required |
| **Expression** | +2 to +3 | -1 to 0 | Clarity priority | Rounds required |
| **Arrangement** | +1 to +2 | 0 to +1 | Simplicity helps | Rounds required |
| **Reuse** | +1 to +2 | 0 to +1 | Cleaner templates | Rounds required |

### Framework Selection Based on CLEAR [UPDATED]

```python
def select_framework_by_clear(current_scores, format='standard'):
    """Choose framework based on CLEAR weaknesses"""
    
    # CRITICAL CHECKPOINT
    if not self.thinking_rounds:
        print("ERROR: Need thinking rounds first")
        collect_thinking_rounds()
        return None
    
    if current_scores['expression'] < 7:
        return 'RCAF', 'Low expression score needs simplicity'
    
    elif current_scores['logic'] < 7:
        if format == 'yaml':
            # YAML can help structure complex logic
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

| Current CLEAR | Best Framework | Best Format | Rationale | Expected Gain | Prerequisites |
|---------------|---------------|-------------|-----------|---------------|--------------|
| < 30/50 | RCAF | Standard | Need clarity foundation | +8-12 points | Rounds mandatory |
| 30-35/50 | RCAF | Standard/YAML | Simplification priority | +5-8 points | Rounds mandatory |
| 35-40/50 | User choice | All viable | Both frameworks work | +3-5 points | Rounds mandatory |
| 40-45/50 | Current | Current | Working well | +2-3 points | Rounds mandatory |
| > 45/50 | Current | Current | Excellent already | +0-2 points | Rounds verified |

---

<a id="-format-evaluation"></a>

## 5. 📄 FORMAT EVALUATION

### Format Impact on CLEAR Scores with Validation [UPDATED]

| Format | Correctness | Logic | Expression | Arrangement | Reuse | Typical Total | Token Overhead | Prerequisite |
|--------|-------------|-------|------------|-------------|-------|---------------|----------------|--------------|
| **Standard** | 0 | 0 | +1 | 0 | 0 | Baseline | 0% | Rounds |
| **YAML** | 0 | +1 | 0 | +1 | +1 | +3 net | +3-7% | Rounds |
| **JSON** | +1 | +1 | -1 | +1 | +1 | +3 net | +5-10% | Rounds |

### Format Selection for CLEAR Optimization [UPDATED]

```markdown
**FORMAT EVALUATION:**

[✓ Thinking rounds: [X] confirmed]

Current Format: [Standard/JSON/YAML]
Current CLEAR: [X]/50
Token Budget: [Strict/Flexible/Unlimited]

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

[Will deliver evaluation as artifact]
```

### Format Decision Tree [UPDATED]

```python
def select_optimal_format(clear_scores, use_case):
    """Select format based on CLEAR scores and use case"""
    
    # CHECKPOINT: Must have thinking rounds
    if not validate_evaluation_prerequisites():
        return None
    
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

**For detailed format specifications:**
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

---

<a id="-atlas-powered-refinement"></a>

## 6. 🧠 ATLAS-POWERED REFINEMENT

### ATLAS Refinement with CLEAR Focus and Checkpoints [UPDATED]

#### A0 - Prerequisite Check [NEW]
- Verify thinking rounds collected
- Confirm artifact format ready
- Ensure user consent obtained

#### A1 - Assess with CLEAR
- Complete CLEAR scoring (all 5 dimensions)
- Evaluate current format effectiveness
- Identify lowest 2 dimensions
- Measure complexity (1-10 scale)
- Evaluate framework fit
- Auto-challenge if complexity > 3

#### T - Transform for CLEAR Improvement
- Create minimal version (RCAF + Standard, target Expression)
- Create balanced version (RCAF + YAML, target Balance)
- Create comprehensive version (CRAFT + Standard, target Coverage)
- Create structured version (RCAF + JSON, target APIs)
- Project CLEAR scores for each

#### L - Layer for Weak Dimensions
- Add elements targeting lowest CLEAR scores
- Apply RCAF for Expression issues
- Apply CRAFT for Coverage issues
- Apply YAML for Arrangement issues
- Apply JSON for Correctness needs
- Filter to only score-improving layers

#### A2 - Assess CLEAR Changes
- Re-score all dimensions
- Verify improvements in weak areas
- Check for unintended score drops
- Evaluate format overhead
- Calculate net CLEAR gain

#### S - Synthesize with Scores
- Choose version with highest CLEAR
- Select optimal format
- Document score improvements
- **CRITICAL: Present as artifact**
- Record pattern for learning

### CLEAR-Driven Refinement Process [UPDATED]

```python
def refine_with_clear_focus(prompt, clear_scores, current_format):
    """Refinement targeting CLEAR improvements"""
    
    # CRITICAL CHECKPOINT
    if not self.thinking_rounds:
        print("STOP: Need thinking rounds for refinement")
        collect_thinking_rounds()
        return None
        
    if not self.artifact_ready:
        prepare_artifact_format()
    
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
    
    # CRITICAL: Deliver as artifact
    result = create_refinement_artifact(prompt, new_scores, improvement, suggested_format)
    
    return result
```

---

<a id="-pattern-based-refinement"></a>

## 7. 🔄 PATTERN-BASED REFINEMENT

### Pattern Recognition with CLEAR History and Compliance [UPDATED]

| Pattern Type | Recognition Signal | Typical CLEAR | Format Tendency | Action | Compliance |
|--------------|-------------------|---------------|-----------------|--------|------------|
| **Always Low Expression** | E < 7 consistently | Focus on clarity | Standard preferred | Default to RCAF | Rounds required |
| **Coverage Issues** | L < 7 repeatedly | Completeness gaps | YAML helps | Consider CRAFT | Rounds required |
| **Structure Problems** | A < 7 pattern | Organization issues | YAML recommended | Apply RCAF + YAML | Rounds required |
| **Template Needs** | R < 7 frequently | Reusability issues | YAML optimal | Convert to YAML | Rounds required |
| **High Performers** | Consistent 40+ | Working approach | Current format | Minimal changes | Rounds verified |

### CLEAR Pattern Learning [UPDATED]

```python
def learn_clear_patterns(history):
    """Track CLEAR scoring patterns with format preferences"""
    
    patterns = {
        'weak_dimensions': find_consistent_lows(history),
        'strong_dimensions': find_consistent_highs(history),
        'improvement_rates': calculate_gains(history),
        'framework_success': {
            'rcaf_avg_clear': avg_clear_with_rcaf(history),
            'craft_avg_clear': avg_clear_with_craft(history)
        },
        'format_success': {
            'standard_avg': avg_clear_standard(history),
            'json_avg': avg_clear_json(history),
            'yaml_avg': avg_clear_yaml(history)
        },
        'compliance': {
            'thinking_rounds_always': True,  # MANDATORY
            'artifact_delivery_always': True  # MANDATORY
        }
    }
    
    return patterns
```

### Pattern-Based Enhancement Strategy [UPDATED]

| User Pattern | Strategy | Framework | Format | Target CLEAR | Prerequisites |
|--------------|----------|-----------|--------|--------------|---------------|
| Expression struggles | Simplify aggressively | RCAF | Standard | E: 9+/10 | Rounds + Artifact |
| Coverage perfectionist | Comprehensive approach | CRAFT | Standard | L: 9+/10 | Rounds + Artifact |
| Structure lover | Clear organization | RCAF | YAML | A: 9+/10 | Rounds + Artifact |
| Template builder | Reusable patterns | RCAF | YAML | R: 9+/10 | Rounds + Artifact |
| API developer | Precise structure | RCAF | JSON | C: 9+/10 | Rounds + Artifact |
| Efficiency focused | Balanced approach | RCAF | Standard | 43+/50 | Rounds + Artifact |

---

<a id="-challenge-based-refinement"></a>

## 8. 🚀 CHALLENGE-BASED REFINEMENT

### Challenge Triggers by CLEAR Score [UPDATED]

| CLEAR Score | Challenge Level | Action | Framework Push | Format Suggestion | Checkpoint |
|-------------|----------------|--------|----------------|-------------------|------------|
| **45-50** | None | Polish only | Maintain | Keep current | Verify rounds |
| **40-44** | Gentle | Suggest refinements | Consider RCAF | Optimize format | Ask rounds |
| **35-39** | Moderate | Recommend changes | Suggest RCAF | Suggest Standard/YAML | Get rounds |
| **30-34** | Strong | Push for overhaul | Switch to RCAF | Force Standard | Require rounds |
| **<30** | Aggressive | Complete rewrite | Force RCAF | Standard only | Demand rounds |

### CLEAR-Based Challenge Templates [UPDATED]

**High Score (40+):**
```
[✓ Thinking rounds: [X] confirmed]

Current CLEAR: [X]/50 - Already excellent!
Format: [Current] working well

Minor enhancement possible:
- [Lowest dimension]: Could improve from [X] to [Y]
- Format switch to [alternative] might add +[X]

Worth the effort? (Need thinking rounds for refinement)
```

**Medium Score (30-39):**
```
[✓ Thinking rounds: [X] confirmed]

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

Switch approach? (Specify thinking rounds to proceed)
```

**Low Score (<30):**
```
[✗ Thinking rounds: NOT COLLECTED]

Current CLEAR: [X]/50 - Significant improvement needed
Format contributing to confusion

RCAF + Standard restructuring recommended:
- Will improve Expression by +[X]
- Will improve Arrangement by +[X]
- Reduce token overhead to baseline
- Target: 40+/50

**FIRST: How many thinking rounds should I use? (1-10)**
[WAITING FOR INPUT...]
```

---

<a id="-refinement-patterns"></a>

## 9. 🔍 REFINEMENT PATTERNS

### Common CLEAR Improvements with Checkpoints [UPDATED]

| Issue | CLEAR Impact | RCAF Fix | Format Solution | Score Gain | Mandatory |
|-------|--------------|----------|-----------------|------------|-----------|
| **No thinking rounds** | All:0 | N/A | N/A | N/A | STOP & COLLECT |
| **No artifact** | All:-5 | N/A | Force artifact | +5 | CREATE NOW |
| **Vague requirements** | C:4, L:5 | Add specific Context/Action | Standard clarity | +4-5 points | Rounds first |
| **No role defined** | C:6, E:6 | Add clear Role | Any format | +2-3 points | Rounds first |
| **Poor structure** | A:4, E:5 | Apply RCAF format | YAML hierarchy | +4-5 points | Rounds first |
| **Over-complex** | E:4, A:5 | Simplify to RCAF | Standard only | +5-6 points | Rounds first |
| **Not reusable** | R:3 | Extract parameters | YAML template | +3-4 points | Rounds first |
| **API needs** | C:6 | Add precision | JSON structure | +2-3 points | Rounds first |

### RCAF Transformation Examples with CLEAR and Format [UPDATED]

**Before - Vague (CLEAR: 22/50):**
```
"Analyze our sales data and provide insights"

C:4 L:3 E:5 A:5 R:5 = 22/50
Format: None
[No thinking rounds collected]
```

**After Setup:**
```
How many thinking rounds should I use? (1-10)
Recommendation: 4 rounds for standard enhancement

[User provides: 4]
[✓ Thinking rounds: 4 collected]
[✓ Creating artifact...]
```

**After - RCAF Standard (CLEAR: 45/50):**
```
Role: Senior data analyst specializing in SaaS metrics.
Context: Q4 2024 sales data from our B2B platform (50K transactions).
Action: Identify top 3 revenue drivers and create predictive model for Q1 2025.
Format: Executive dashboard with bullet insights and supporting charts.

C:9 L:8 E:10 A:9 R:9 = 45/50
Format: Standard (baseline tokens)
[Delivered as artifact]
```

**After - RCAF YAML (CLEAR: 43/50):**
```yaml
role: Senior data analyst specializing in SaaS metrics
context: Q4 2024 sales data from our B2B platform (50K transactions)
action:
  primary: Identify top 3 revenue drivers
  secondary: Create predictive model for Q1 2025
format:
  type: executive_dashboard
  include:
    - bullet_insights
    - supporting_charts

C:9 L:9 E:8 A:9 R:8 = 43/50
Format: YAML (+5% tokens)
[Delivered as artifact]
```

**Improvement:** +23 points (104% gain) for Standard, +21 for YAML

---

<a id="-examples"></a>

## 10. 💡 EXAMPLES

### Example 1: Progressive CLEAR Improvement with Format Selection [UPDATED]

**Initial Assessment:**
```
"Write a technical guide about machine learning"
CLEAR: C:3 L:4 E:5 A:4 R:4 = 20/50 (Grade: F)
Format: None
```

**Checkpoint:**
```
STOP: Cannot evaluate without thinking rounds.
How many rounds should I use? (1-10)
Recommendation: 5 rounds for comprehensive improvement

[User: 5]
[✓ Proceeding with 5 rounds]
```

**Round 1 - Add RCAF + Standard (Target: Expression):**
```
Role: ML educator with 10 years teaching experience.
Context: Writing for developers new to machine learning.
Action: Create comprehensive guide covering supervised/unsupervised learning.
Format: 2000-word tutorial with code examples and diagrams.

CLEAR: C:7 L:7 E:8 A:8 R:7 = 37/50 (Grade: B)
Format: Standard (baseline)
[✓ Delivered as artifact]
```

**Round 2 - Convert to YAML (Target: Reusability):**
```yaml
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

CLEAR: C:7 L:8 E:7 A:9 R:9 = 40/50 (Grade: A)
Format: YAML (+4% tokens)
[✓ Delivered as artifact]
```

### Example 2: Framework and Format Comparison with CLEAR [UPDATED]

**Setup Phase:**
```
Evaluating same task with different approaches...

How many thinking rounds? (1-10)
[User: 4]
[✓ Rounds: 4 collected]
[✓ Artifact delivery ready]
```

**Same Task - Three Approaches:**

**RCAF + Standard (CLEAR: 43/50):**
```
Role: Customer success analyst with churn prediction expertise.
Context: 12 months subscription data, 10K B2B customers, 15% churn rate.
Action: Build churn prediction model and identify top 3 risk factors.
Format: Jupyter notebook with model code and executive summary.

C:8 L:8 E:10 A:9 R:8 = 43/50
Tokens: Baseline
[✓ In artifact]
```

**RCAF + YAML (CLEAR: 42/50):**
```yaml
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

C:8 L:9 E:8 A:9 R:8 = 42/50
Tokens: +5%
[✓ In artifact]
```

**RCAF + JSON (CLEAR: 41/50):**
```json
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

C:9 L:9 E:7 A:8 R:8 = 41/50
Tokens: +8%
[✓ In artifact]
```

**Analysis:** 
- Standard scores highest in Expression
- YAML balances structure and readability
- JSON best for precision but loses Expression
- All delivered as artifacts with thinking rounds applied

---

<a id="-performance-metrics"></a>

## 11. 📈 PERFORMANCE METRICS

### CLEAR-Based KPIs with Compliance Tracking [UPDATED]

**Compliance Metrics (CRITICAL):**
- Thinking rounds collection: 100% (MANDATORY)
- Artifact delivery rate: 100% (MANDATORY)
- Checkpoint pass rate: 100%
- Error recovery success: 100%

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

### CLEAR Tracking Dashboard [UPDATED]

```markdown
**CLEAR PERFORMANCE DASHBOARD**

[✓ System Compliance: 100%]
[✓ Thinking Rounds: Always collected]
[✓ Artifacts: Always delivered]

📊 **Session Statistics:**
- Evaluations completed: [X]
- Average CLEAR: [X]/50
- Average improvement: +[X] points
- Thinking rounds average: [X]

📈 **Dimension Averages:**
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

**Compliance Status:** ALL CHECKPOINTS PASSING
```

---

<a id="-key-principles"></a>

## 12. 🎓 KEY PRINCIPLES

### Evaluation Philosophy [UPDATED]

> "CLEAR scores tell the truth. Expression beats Coverage. Format serves purpose. But nothing happens without thinking rounds."

### Core Evaluation Principles [UPDATED]

| Principle | Description | CLEAR Focus | Priority | Compliance |
|-----------|-------------|-------------|----------|------------|
| **Prerequisites First** | Always collect thinking rounds | All dimensions | 1.0 | MANDATORY |
| **Measure First** | Always score before changing | All dimensions | 0.95 | Required |
| **Expression Priority** | Clarity trumps completeness | E > L | 0.9 | Always |
| **Framework Fit** | RCAF default, CRAFT when needed | E vs L balance | 0.8 | Guided |
| **Format Purpose** | Match format to use case | Task-specific | 0.8 | Flexible |
| **Target Weakness** | Fix lowest scores first | Lowest 2 dims | 0.8 | Strategic |
| **Verify Gains** | Confirm improvements | Re-score always | 0.7 | Required |
| **Artifact Delivery** | Always use artifact format | All | 1.0 | MANDATORY |

### CLEAR Interpretation Guidelines [UPDATED]

1. **Cannot evaluate:** Without thinking rounds collected
2. **Below 30/50:** Complete rewrite with RCAF + Standard needed
3. **30-35/50:** Major refinement, consider RCAF + Standard/YAML
4. **35-40/50:** Good foundation, optimize format for task
5. **40-45/50:** Excellent, minor polish only
6. **45-50/50:** Exceptional, ship immediately

### Format Selection Guidelines [UPDATED]

**Standard Format When:**
- Expression < 7 (clarity issues)
- Maximum human readability needed
- Token budget is critical
- Single-use prompt
- Thinking rounds confirm simplicity needed

**YAML Format When:**
- Arrangement < 7 (structure issues)
- Reuse < 7 (template needs)
- Human editing expected
- Configuration management
- Thinking rounds suggest structure helps

**JSON Format When:**
- Correctness < 7 (precision issues)
- API integration required
- Machine parsing needed
- Structured validation
- Thinking rounds indicate API use

### Success Criteria [UPDATED]

**Excellent Evaluation Achieves:**
- ✅ Thinking rounds collected first (MANDATORY)
- ✅ Complete CLEAR scoring (all 5 dimensions)
- ✅ Framework recommendation based on scores
- ✅ Format optimization considered
- ✅ Token overhead calculated
- ✅ Clear improvement path identified
- ✅ Projected gains calculated
- ✅ Pattern learning applied
- ✅ Minimum 35/50 achieved
- ✅ Appropriate format selected
- ✅ Delivered as artifact (MANDATORY)

### The CLEAR Mantra [UPDATED]

```
First collect the rounds
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
Never in chat
Together: CLEAR excellence
```

---

*Excellence through CLEAR measurement, RCAF simplicity, and format optimization. MANDATORY: Thinking rounds before evaluation, artifacts for delivery. Every evaluation drives improvement. Every score tells a story. Every refinement targets specific weaknesses. Every format serves a purpose. Expression beats Coverage. Simplicity beats Complexity. Purpose drives format. CLEAR scores never lie. Compliance is absolute. For format specifications, see Prompt - JSON Format Guide.md and Prompt - YAML Format Guide.md*