# Prompt - Evaluation & Refinement - v6.0.0

Systematic quality assessment and improvement for optimizing prompts through ATLAS-powered evaluation, intelligent challenge-based refinement, adaptive pattern learning, and multi-format support including SMILE assessment.

## 📋 Table of Contents

1. [⚡ QUICK EVAL (10 CRITERIA)](#-quick-eval-10-criteria)
2. [📊 FULL EVALUATION (35 CRITERIA)](#-full-evaluation-35-criteria)
3. [🔄 FORMAT EVALUATION](#-format-evaluation)
4. [🧠 ATLAS-POWERED REFINEMENT](#-atlas-powered-refinement)
5. [📄 PATTERN-BASED REFINEMENT](#-pattern-based-refinement)
6. [🚀 CHALLENGE-BASED REFINEMENT](#-challenge-based-refinement)
7. [📝 REFINEMENT PATTERNS](#-refinement-patterns)
8. [💡 EXAMPLES](#-examples)
9. [📈 PERFORMANCE METRICS](#-performance-metrics)
10. [🎓 KEY PRINCIPLES](#-key-principles)

---

## 1. ⚡ QUICK EVAL (10 CRITERIA)

### Core Assessment Criteria with Format Consideration

| Criterion | Weight | Check | Adaptive | Format Impact |
|-----------|--------|-------|----------|---------------|
| **Clarity/Specificity** | 5 | Task clear and specific? | Yes | All formats need |
| **Role/Expertise** | 5 | Appropriate expertise defined? | Yes | SMILE: `[: Role :]` |
| **Context Provided** | 5 | Sufficient background given? | Yes | SMILE: `(: Context :)` |
| **Target Audience** | 5 | Reader/user identified? | Yes | JSON: "audience" field |
| **Format/Structure** | 5 | Output format specified? | Yes | SMILE inherently structured |
| **Success Criteria** | 5 | Quality measures defined? | No | SMILE: `[! Success !]` |
| **Scope Boundaries** | 5 | Limits clearly set? | Yes | All formats benefit |
| **Examples Provided** | 5 | Helpful samples included? | Yes | Format agnostic |
| **Methodology Clear** | 5 | Approach specified? | Yes | Structure helps |
| **Simplicity Achieved** | 5 | No unnecessary complexity? | No | SMILE adds tokens |

### Format-Aware Quick Evaluation

```python
def evaluate_quick_with_format(prompt, format_type, patterns=None):
    total_score = 0
    format_bonus = 0
    
    for criterion in criteria:
        score = assess_criterion(prompt, criterion)
        
        # Apply format-specific adjustments
        if format_type == 'smile':
            if criterion['name'] == 'Format/Structure':
                score = criterion['weight']  # SMILE auto-structures
            elif criterion['name'] == 'Simplicity':
                score -= 1  # Token overhead penalty
        elif format_type == 'json':
            if criterion['name'] in ['Format/Structure', 'Methodology']:
                score += 1  # JSON aids structure
        
        total_score += min(score, criterion['weight'])
    
    return total_score, format_bonus
```

### Quick Report Template with Format

```markdown
QUICK EVALUATION: [X]/50 ([X]%)
Format: [Standard/JSON/SMILE]

Strengths: [Top 2 criteria]
Priority Fix: [Weakest criterion] → [Solution]
Format Impact: [Token +X%] [Structure +X%]
Simplification: [If applicable]

Pattern Note: [User typically values X over Y]
Format History: SMILE used [X]% for similar
Thinking: [X] rounds
Challenge: [Applied/Not needed]
```

---

## 2. 📊 FULL EVALUATION (35 CRITERIA)

### Evaluation Groups with Format Scoring

| Group | Base Weight | Criteria Count | Format Bonus | Focus Area |
|-------|-------------|----------------|--------------|------------|
| **Task Definition** | 40 | 8 | SMILE +5 | Clarity, deliverables, scope |
| **Context** | 30 | 6 | SMILE +3 | Background, problem, assumptions |
| **Expertise** | 25 | 5 | All equal | Role, domain, experience |
| **Audience** | 25 | 5 | JSON +2 | Target, needs, value |
| **Structure** | 20 | 4 | SMILE +4, JSON +3 | Format, sections, length |
| **Methodology** | 20 | 4 | SMILE +2 | Method, process, tools |
| **Simplicity** | 15 | 3 | Standard +3 | Minimal complexity |

### Format-Specific Evaluation Adjustments

**SMILE Format Bonuses:**
- Automatic structure: +4 to Structure group
- Clear sections: +5 to Task Definition
- Rigid requirements: +3 to Context
- Token overhead: -3 to Simplicity

**JSON Format Bonuses:**
- Programmatic clarity: +3 to Structure
- Field definition: +2 to Audience
- Parsing ease: +2 to Methodology
- Compact form: +1 to Simplicity

### Full Evaluation Report with Format

```markdown
FULL EVALUATION: [X]/175 ([X]%)
Format: [Standard/JSON/SMILE]

Group Scores:
- Task Definition: [X/40] [+X format bonus]
- Context: [X/30] [+X format bonus]
- Expertise: [X/25]
- Audience: [X/25]
- Structure: [X/20] [+X format bonus]
- Methodology: [X/20]
- Simplicity: [X/15] [-X if SMILE]

Format Analysis:
- Token Impact: [+X% for SMILE]
- Structure Clarity: [Excellent/Good/Fair]
- Instruction Following: [+X% expected]

Priority Improvements: [Top 3 with solutions]
Format Recommendation: [Optimal format for this prompt]
ATLAS Applied: [Phases used]
Pattern Insights: [What patterns suggest]
```

---

## 3. 🔄 FORMAT EVALUATION

### SMILE Format Assessment

| Aspect | Evaluation | Score Impact | Recommendation |
|--------|------------|--------------|----------------|
| **Depth Appropriateness** | Matches complexity? | ±5 points | Adjust depth |
| **Symbol Usage** | Semantic correctness? | ±3 points | Fix markers |
| **Nesting Level** | Max 3 levels? | ±2 points | Flatten if > 3 |
| **Variable Placement** | `[$Var$]` correct? | ±2 points | Standardize |
| **Section Balance** | Proportional sections? | ±3 points | Rebalance |
| **Token Overhead** | Acceptable (<30%)? | -5 if > 30% | Consider standard |

### SMILE Depth Evaluation

```python
def evaluate_smile_depth(prompt, complexity):
    depth = get_smile_depth(prompt)
    optimal = calculate_optimal_depth(complexity)
    
    if depth == optimal:
        return 10  # Perfect match
    elif abs(depth - optimal) == 1:
        return 7   # Close enough
    else:
        return 3   # Needs adjustment
```

### JSON Format Assessment

| Aspect | Evaluation | Score Impact | Fix |
|--------|------------|--------------|-----|
| **Field Completeness** | All needed fields? | ±5 points | Add missing |
| **Nesting Depth** | Reasonable? | ±3 points | Flatten |
| **Type Consistency** | Consistent types? | ±2 points | Standardize |
| **Parsing Validity** | Valid JSON? | -10 if invalid | Fix syntax |

### Format Comparison Scoring

```markdown
FORMAT COMPARISON:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Standard: [X]/50
- Clarity: [X]/10
- Simplicity: [X]/10
- Flexibility: [X]/10
- Tokens: Baseline

JSON: [X]/50
- Structure: [X]/10
- Parsing: [X]/10
- Integration: [X]/10
- Tokens: [±X%]

SMILE: [X]/50
- Following: [X]/10
- Organization: [X]/10
- Complexity: [X]/10
- Tokens: [+X%]

Recommendation: [Format] for [reasons]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 4. 🧠 ATLAS-POWERED REFINEMENT

### ATLAS Refinement Phases with Format

**A1 - Assess Current**
- Identify issues from scores
- Measure complexity (1-10 scale)
- Find simplification opportunities
- **Evaluate format effectiveness**
- Check pattern history for typical issues
- Auto-challenge if complexity > 3

**T - Transform Alternatives**
- Create minimal version (bare essentials)
- Create balanced version (standard enhancement)
- Create comprehensive version (full enhancement)
- **Create format variations** (if beneficial)
- Add pattern-based version if confidence > 0.7

**L - Layer Improvements**
- Apply clarity improvements
- Enhance structure
- Increase specificity
- **Optimize for chosen format**
- Simplify further
- Filter to only valuable improvements

**A2 - Assess Changes**
- Measure clarity change (+/- %)
- Calculate complexity change (negative is better)
- **Verify format adds value**
- Quantify value added
- Find simpler alternative if complexity increased

**F - Format Transform**
- **Apply optimal format**
- Adjust depth/structure
- Verify improvement

**S - Synthesize Final**
- Choose optimal version based on assessment
- **Present in best format(s)**
- Record outcome for pattern learning

### Format-Aware Refinement Logic

```python
def refine_with_format(prompt, eval_scores, current_format, patterns=None):
    # A1: Assess including format
    issues = identify_issues(eval_scores)
    format_issues = assess_format_issues(current_format, prompt)
    
    # T: Transform with format options
    alternatives = {}
    for format_type in ['standard', 'json', 'smile']:
        alternatives[format_type] = create_in_format(prompt, format_type, issues)
    
    # L: Layer improvements
    for format_type, alt in alternatives.items():
        alternatives[format_type] = apply_format_optimizations(alt, format_type)
    
    # A2: Assess format value
    best_format = evaluate_format_effectiveness(alternatives, eval_scores)
    
    # F: Format transform
    final = apply_optimal_format(alternatives[best_format])
    
    # S: Synthesize
    return create_final_version(final, best_format)
```

---

## 5. 📄 PATTERN-BASED REFINEMENT

### Pattern Recognition with Format

| Confidence | Approach | Format Application |
|------------|----------|-------------------|
| < 30% | Standard | Try all formats |
| 30-60% | Hybrid | Suggest likely format |
| > 60% | Pattern-driven | Use preferred format |

### Format Pattern Cache

**Cache Structure:**
```python
format_patterns = {
    'complexity_to_format': {
        'low': 'standard',
        'medium': ['standard', 'json'],
        'high': ['standard', 'smile']
    },
    'domain_to_format': {
        'technical': 'json',
        'creative': 'standard',
        'complex_workflow': 'smile'
    },
    'success_rates': {
        'standard': 0.85,
        'json': 0.75,
        'smile': 0.90
    }
}
```

---

## 6. 🚀 CHALLENGE-BASED REFINEMENT

### Challenge with Format Awareness

| Score Range | Level | Action | Format Challenge |
|-------------|-------|--------|------------------|
| **140-175** | Excellent | Minor polish only | Keep format |
| **105-139** | Good | Targeted refinement | Consider simpler format |
| **70-104** | Adequate | Major restructuring | Try different format |
| **Below 70** | Poor | Complete rewrite | Start with standard |

### Format-Specific Challenges

**SMILE Complexity Challenge:**
```
This SMILE structure adds 35% tokens. Worth it?

Alternatives:
1. Standard format (clearer, fewer tokens)
2. Minimal SMILE (basic structure only)
3. Keep full SMILE (maximum following)

Your preference?
```

**JSON Limitation Challenge:**
```
JSON struggles with this nested complexity.

Options:
1. Flatten JSON structure
2. Switch to SMILE format
3. Use standard format

Which works best?
```

---

## 7. 📝 REFINEMENT PATTERNS

### Format Transformation Patterns

| Pattern | Standard | JSON | SMILE | Usage |
|---------|----------|------|-------|-------|
| **Role Simplification** | "As a data scientist..." | `"role": "data_scientist"` | `[: Role [ Data scientist ] :]` | Track acceptance |
| **Context Reduction** | One paragraph | `"context": "..."` | `(: Context ( Essential info ) :)` | Monitor effectiveness |
| **Structure Definition** | Bullet points | `"format": ["item1", "item2"]` | `[: Format [ • Item 1\n• Item 2 ] :]` | Note preference |
| **Success Clarification** | "Success means..." | `"success": ["metric1"]` | `[! Success: Metrics !]` | Track clarity |

### Format Migration Patterns

**Standard → SMILE:**
1. Identify sections
2. Apply appropriate markers
3. Add rigid requirements
4. Include variables
5. Test comprehension

**SMILE → Standard:**
1. Remove markers
2. Convert to paragraphs
3. Maintain structure via formatting
4. Preserve critical emphasis
5. Verify clarity

---

## 8. 💡 EXAMPLES

### Example 1: Format Progressive Refinement

**Initial (Standard):**
```
Write a technical guide about machine learning for beginners.
Score: 60/175 - Too vague
```

**Refinement 1 (Enhanced Standard):**
```
As a machine learning educator, write a 2000-word beginner's guide covering:
- Core concepts (supervised/unsupervised)
- Common algorithms
- Practical examples
- Getting started steps

Score: 120/175 - Good
```

**Refinement 2 (SMILE Format):**
```
(: Machine Learning Guide Creation
  [: Role [ Machine learning educator ] :]
  [= Task =] Write comprehensive beginner's guide
  
  [: Requirements [
    [! Length: 2000 words !]
    • Core concepts explanation
    • Algorithm overview
    • Practical examples
    • Step-by-step tutorial
  ] :]
  
  [: Output Format [
    Introduction (200 words)
    {Core concepts section}
    {Algorithms with examples}
    {Getting started guide}
    Conclusion (200 words)
  ] :]
) :)

Score: 145/175 - Excellent structure
Token Impact: +25%
```

### Example 2: Format Comparison

**Same Prompt, Three Formats:**

**Complexity: Data Analysis Task**

**Standard (135/175):**
Clear, readable, flexible

**JSON (130/175):**
```json
{
  "task": "analyze_sales_data",
  "metrics": ["revenue", "growth", "segments"],
  "output": "executive_summary"
}
```
Structured, parseable, limited

**SMILE (150/175):**
Better following, higher tokens, clearer structure

---

## 9. 📈 PERFORMANCE METRICS

### Format-Enhanced KPIs

**Quality Metrics:**
- Score improvement: Target > 30 points
- Clarity increase: Target > 40%
- **Format effectiveness**: Target > 80%
- Intent preservation: Target 100%

**Efficiency Metrics:**
- Word reduction: Target 20-40%
- Complexity reduction: Target 30-50%
- **Token efficiency**: Monitor per format
- Time to refine: Target < 30s

**Format Metrics:**
- **SMILE adoption rate**: Track by complexity
- **JSON usage**: Track for technical
- **Format satisfaction**: Target > 0.85
- **Format switch rate**: Target < 0.15
- **Token tolerance**: Track acceptance

### Format Performance Tracking

| Format | Avg Score | Token Impact | User Satisfaction | Best For |
|--------|-----------|--------------|-------------------|----------|
| Standard | 85% | Baseline | 0.90 | Most prompts |
| JSON | 80% | -5% to +5% | 0.75 | APIs |
| SMILE | 92% | +20-30% | 0.85 | Complex |

---

## 10. 🎓 KEY PRINCIPLES

### Evaluation Philosophy with Formats

| Principle | Description | Weight | Format Note |
|-----------|-------------|--------|-------------|
| **Clarity First** | Ambiguity kills prompt quality | 1.0 | All formats |
| **Simplicity Matters** | Complexity needs strong justification | 0.9 | Standard wins |
| **Structure Guides** | Format shapes output | 0.8 | SMILE excels |
| **Specificity Drives** | Details determine results | 0.8 | Any format |
| **Token Efficiency** | Balance structure vs overhead | 0.7 | Monitor SMILE |
| **Measurability Required** | Success must be definable | 0.6 | JSON helps |

### Format Selection Philosophy

> "The best format is invisible to the task. Choose based on complexity, use case, and user preference."

**Format Decision Tree:**
1. Assess complexity and structure needs
2. Check user patterns and preferences
3. Evaluate token tolerance
4. Consider use case (human/API)
5. Recommend optimal format(s)
6. Let user choose final format
7. Track satisfaction and effectiveness

### Success Criteria for Format Refinement

**Excellent refinement achieves:**
1. Higher score with optimal format
2. Format matches complexity perfectly
3. Token overhead justified by gains
4. Structure enhances not obscures
5. User accepts format choice
6. Pattern correctly predicted
7. Measurable improvement shown

---

*Excellence through systematic evaluation, intelligent format selection, and continuous pattern learning. Every format serves a purpose: Standard for clarity, JSON for systems, SMILE for complex instruction following. Every refinement considers format as a tool for enhancement, not an end in itself.*