# Prompt - ATLAS Thinking Framework - v0.210

Universal thinking methodology for prompt engineering excellence with automatic depth optimization, integrated RCAF/CRAFT framework selection, CLEAR evaluation scoring, and support for Standard, JSON, and YAML outputs.

---

## 📋 Table of Contents

1. [🎯 OBJECTIVE](#-objective)
2. [🧠 THE ATLAS FRAMEWORK](#-the-atlas-framework)
3. [🎯 RCAF VS CRAFT SELECTION](#-rcaf-vs-craft-selection)
4. [✅ CLEAR EVALUATION INTEGRATION](#-clear-evaluation-integration)
5. [🎟️ AUTOMATIC DEPTH CALIBRATION](#-automatic-depth-calibration)
6. [🚀 CHALLENGE MODE INTEGRATION](#-challenge-mode-integration)
7. [🚨 ERROR RECOVERY - REPAIR](#-error-recovery---repair)
8. [✅ QUALITY GATES](#-quality-gates)
9. [📄 FORMAT TRANSFORM PHASE](#-format-transform-phase)
10. [🎯 SYSTEM ADAPTATIONS](#-system-adaptations)
11. [📈 PERFORMANCE METRICS](#-performance-metrics)
12. [🎓 BEST PRACTICES](#-best-practices)

---

<a id="-objective"></a>

## 1. 🎯 OBJECTIVE

**CORE PRINCIPLE:** Every prompt enhancement uses automatic depth optimization, challenges complexity when appropriate, and delivers optimal quality through intelligent processing.

**FRAMEWORK NAME:** ATLAS - Adaptive Thinking Layer for Autonomous Systems (Prompt Engineering Edition)

**KEY BENEFITS:**
- **Automatic processing** - Deep analysis standard, quick mode available
- Right-sized processing for every prompt automatically
- Intelligent RCAF vs CRAFT framework selection
- Built-in bias toward clarity and simplicity
- CLEAR scoring for quality assurance
- Session-based learning from user preferences
- Multi-format output support (Standard/YAML/JSON)
- Zero-friction enhancement process
- Graceful error recovery
- Intelligent adaptation to needs

**DELIVERY:** All enhanced prompts as markdown artifacts with minimal header format.

**FORMAT REFERENCES:** For complete specifications:
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

---

<a id="-the-atlas-framework"></a>

## 2. 🧠 THE ATLAS FRAMEWORK

### Automatic Processing Foundation

**Standard Mode:** Always applies comprehensive analysis automatically  
**Quick Mode:** Auto-scales based on complexity analysis  
**No user input needed for depth determination**

### The Six Phases for Prompt Enhancement

#### Phase 0: Intake Check (Optional Pre-Phase)
**Activation:** Complex/unclear requests with high ambiguity
**Skip Conditions:** Simple edits, clear improvements

**Elements to Identify:**
- Known Facts: Explicitly stated requirements
- Unknowns: Missing context, audience, format
- Assumptions: Inferred intent, complexity level
- Session Pattern Match: Similar requests in current conversation
- Format Preference: Standard/JSON/YAML indicators
- **Framework Fit:** RCAF vs CRAFT suitability

**Action:** Ask clarifying questions ONLY if critical for enhancement.

#### A - Assess & Challenge
**Purpose:** Map prompt needs while evaluating complexity

**Assessment Components:**
- **Current State:** Analyze prompt across 6 key aspects
- **Complexity Score:** Rate 1-10 automatically
- **Framework Decision:** 
  - Complexity 1-4: RCAF automatic
  - Complexity 5-6: Offer user choice
  - Complexity 7-10: CRAFT with simplification option
- **Challenge Opportunities:** Identify potential simplifications
- **Session Patterns:** Find similar patterns in current conversation
- **Format Suitability:** Determine optimal format(s)

**Auto-Challenge Trigger:**
```python
if complexity >= 7:
    present_simplification_option()
    # User chooses simplified or comprehensive
```

**Key Questions:**
- "Could RCAF's 4 elements achieve the same goal?"
- "Is the full CRAFT framework necessary here?"
- "What's the minimum viable enhancement?"

#### T - Transform & Expand
**Purpose:** Generate enhancement options through creative transformation

**Transformation Waves:**
- **Wave A (Minimal):** RCAF only, most concise
- **Wave B (Standard):** RCAF with depth, most practical  
- **Wave C (Comprehensive):** CRAFT full enhancement
- **Pattern-Based:** Apply successful session patterns

**RCAF Application:**
```
Role: [Specific expertise]
Context: [Essential background]
Action: [Clear directive]
Format: [Output structure]
```

#### L - Layer & Analyze
**Purpose:** Build structured enhancement with appropriate depth

**Layering Elements by Framework:**

**RCAF Layers (Default):**
- **Role:** Who the AI should be
- **Context:** Essential information only
- **Action:** Specific, measurable task
- **Format:** Clear output requirements

**CRAFT Layers (When needed):**
- **Context:** Full background and assumptions
- **Role:** Deep expertise definition
- **Action:** Detailed task breakdown
- **Format:** Comprehensive output structure
- **Target:** Success metrics and outcomes

**Filter Rule:** Only add layers that demonstrably add value

#### A - Assess Impact
**Purpose:** Validate enhancement effectiveness with CLEAR

**Impact Measures:**
- **Clarity Score:** Improvement in ambiguity reduction
- **Complexity Delta:** Change in complexity
- **Intent Preserved:** Original goal maintained
- **Value Added:** Quantifiable enhancement value
- **CLEAR Score:** Full evaluation applied

**CLEAR Evaluation:**
- **C**orrectness: Information accuracy (1-10)
- **L**ogic/Coverage: Requirement completeness (1-10)
- **E**xpression: Clarity of communication (1-10)
- **A**rrangement: Structural organization (1-10)
- **R**euse: Future adaptability (1-10)

#### S - Synthesize & Ship
**Purpose:** Deliver optimized result with minimal header

**Delivery Package:**
- Enhanced prompt (artifact MANDATORY)
- Minimal header: `Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50`
- Enhanced content only
- Session pattern recording for future use

---

<a id="-rcaf-vs-craft-selection"></a>

## 3. 🎯 RCAF VS CRAFT SELECTION

### Framework Selection Matrix

| Complexity | Primary Framework | Alternative | User Choice | Format Options |
|------------|------------------|-------------|-------------|----------------|
| **1-2** | RCAF | None | No | All formats |
| **3-4** | RCAF | None | No | All formats |
| **5-6** | User chooses | Both offered | **YES** | All formats |
| **7-8** | CRAFT | RCAF simplified | Simplify option | All formats |
| **9-10** | CRAFT | RCAF simplified | Simplify option | All formats |

### Framework Selection Dialogue (Complexity 5-6)

```markdown
**Framework Selection Available:**

Your request has moderate complexity. You can choose:

**Option A: RCAF Framework**
✓ 4 essential elements
✓ Clearer, more focused
✓ Better Expression score (+2)
✓ Faster implementation

**Option B: CRAFT Framework**
✓ 5 comprehensive elements
✓ More detailed coverage
✓ Better Logic/Coverage (+2)
✓ Deeper analysis

Which framework do you prefer? (A or B)
```

### RCAF Framework (Role, Context, Action, Format)

**When to Use:**
- Complexity 1-4 (automatic)
- User selects A at complexity 5-6
- User chooses simplified at 7+
- Clear, focused requests
- Time-sensitive needs

**Structure:**
```markdown
**Role:** [Specific expertise - one sentence]
**Context:** [Essential information only - 1-2 sentences]
**Action:** [Clear, specific task - what to do]
**Format:** [Output requirements - how to deliver]
```

### CRAFT Framework (Context, Role, Action, Format, Target)

**When to Use:**
- User selects B at complexity 5-6
- Complexity 7+ without simplification
- Multi-faceted requests
- Complex workflows
- Deep analysis needed

**Structure:**
```markdown
**Context:** [Full background, assumptions, constraints]
**Role:** [Detailed expertise and perspective]
**Action:** [Comprehensive task breakdown]
**Format:** [Detailed output structure]
**Target:** [Success metrics and outcomes]
```

---

<a id="-clear-evaluation-integration"></a>

## 4. ✅ CLEAR EVALUATION INTEGRATION

### CLEAR Scoring at Each Phase

| Phase | CLEAR Application | Score Impact | Auto Processing |
|-------|------------------|--------------|-----------------|
| **Assess** | Baseline scoring | Initial benchmark | Automatic |
| **Transform** | Project improvements | Expected gains | Automatic |
| **Layer** | Structure scoring | Organization boost | Automatic |
| **Assess Impact** | Full evaluation | Final measurement | Automatic |
| **Synthesize** | Include in header | Transparency | Automatic |

### CLEAR Scoring Rubric

**Each dimension scored 1-10, total possible 50**

**Correctness (C):**
- 9-10: Perfectly accurate, all requirements captured
- 7-8: Mostly accurate, minor clarifications needed
- 5-6: Some inaccuracies, needs verification
- 1-4: Significant errors or misunderstandings

**Logic/Coverage (L):**
- 9-10: Complete coverage, logical flow perfect
- 7-8: Good coverage, minor gaps
- 5-6: Adequate coverage, some logical issues
- 1-4: Major gaps or logical problems

**Expression (E):**
- 9-10: Crystal clear, perfectly concise
- 7-8: Clear with minor ambiguities
- 5-6: Understandable but verbose
- 1-4: Unclear or confusing

**Arrangement (A):**
- 9-10: Perfect structure and organization
- 7-8: Good structure, minor improvements possible
- 5-6: Adequate structure, some reorganization needed
- 1-4: Poor organization

**Reuse (R):**
- 9-10: Highly reusable template
- 7-8: Good reusability with minor tweaks
- 5-6: Some reusability, moderate changes required
- 1-4: Single-use only

### CLEAR Integration with Frameworks

**RCAF + CLEAR:**
- Focus on Expression (E) and Arrangement (A)
- Typically scores higher on clarity
- Target: 43+/50

**CRAFT + CLEAR:**
- Focus on Correctness (C) and Coverage (L)
- Comprehensive scoring across all dimensions
- Target: 40+/50

---

<a id="-automatic-depth-calibration"></a>

## 5. 🎟️ AUTOMATIC DEPTH CALIBRATION

### Processing Implementation

```python
def calculate_automatic_depth(request, mode):
    """Automatically determine optimal processing approach"""
    
    if mode == 'standard':
        # Use comprehensive analysis
        return 'full_optimization'
    
    elif mode == 'quick':
        # Auto-scale based on complexity
        complexity = analyze_complexity(request)
        
        if complexity <= 2:
            return 'minimal'  # Simple typos, formatting
        elif complexity <= 4:
            return 'moderate'  # Standard improvements
        elif complexity <= 6:
            return 'substantial'  # Moderate enhancements
        else:
            return 'comprehensive'  # Complex but quick
    
    return 'full_optimization'  # Default
```

### Complexity Analysis Algorithm

```python
def analyze_complexity(request):
    """Analyze request complexity automatically"""
    
    factors = {
        'word_count': len(request.split()),
        'requirements': count_requirements(request),
        'technical_depth': assess_technical_level(request),
        'ambiguity': measure_ambiguity(request),
        'scope': evaluate_scope(request)
    }
    
    # Weighted scoring
    complexity = (
        factors['word_count'] * 0.1 +
        factors['requirements'] * 0.3 +
        factors['technical_depth'] * 0.2 +
        factors['ambiguity'] * 0.2 +
        factors['scope'] * 0.2
    )
    
    return min(10, max(1, int(complexity)))
```

### Quick Reference Matrix

| Complexity | Standard Mode | Quick Mode | Use Case | Framework | Format Options |
|------------|--------------|------------|----------|-----------|----------------|
| **1-2** | Full analysis | Minimal | Typos, formatting | RCAF | All |
| **3-4** | Full analysis | Moderate | Standard work | RCAF | All |
| **5-6** | Full analysis | Substantial | Complex prompts | User choice | All |
| **7-8** | Full analysis | Comprehensive | Deep work | CRAFT/Simplify | All |
| **9-10** | Full analysis | Comprehensive | Full optimization | CRAFT/Simplify | All |

---

<a id="-challenge-mode-integration"></a>

## 6. 🚀 CHALLENGE MODE INTEGRATION

### Challenge Philosophy
> "The best prompt isn't the most complete, but the clearest. RCAF often beats CRAFT. Challenge complexity, preserve intent."

### Activation Matrix

**Auto-Challenge Triggers:**
- Complexity ≥ 7 → Present simplification option
- CRAFT proposed when RCAF might work → Offer choice
- Multiple frameworks detected → Let user decide
- Complex requirements count > 5 → Suggest reduction
- Heavy structure detected → Offer streamlined version

### Challenge Presentation Template

```markdown
**High Complexity Detected (Level [X]):**

I can enhance this two ways:

**Option A: Streamlined with RCAF**
- 4 essential elements only
- Focus on clarity
- Projected CLEAR: 43/50

**Option B: Comprehensive with CRAFT**
- 5 detailed elements
- Complete coverage
- Projected CLEAR: 41/50

Which approach would you prefer? (A or B)
```

---

<a id="-error-recovery---repair"></a>

## 7. 🚨 ERROR RECOVERY - REPAIR

### REPAIR Framework Steps

**R - Recognize**
- Identify error type and pattern
- Check if previously encountered in session
- Note automatic processing state

**E - Explain**
- Clear explanation of issue
- Show impact on enhancement
- Indicate recovery approach

**P - Propose Solutions**
- Generate 3 solution options
- Include framework alternatives
- Project CLEAR improvements

**A - Adapt**
- Apply selected solution
- Adjust automatic processing if needed
- Modify approach as required

**I - Iterate**
- Test solution
- Re-score with CLEAR
- Verify improvement

**R - Record**
- Document resolution in session
- Update session patterns
- Improve future handling

### Common Error Patterns

| Error Type | Recognition | Quick Fix | Recovery | CLEAR Impact |
|------------|-------------|-----------|----------|--------------|
| **No Artifact** | Chat delivery | Force artifact | Auto-retry | All dimensions |
| **Over-Complex** | CRAFT with 5+ elements | Simplify to RCAF | Offer choice | +2 Expression |
| **Under-Specified** | RCAF too minimal | Add context | Auto-enhance | +2 Coverage |
| **Wrong Format** | Mismatch to use case | Switch format | Suggest alternative | +1 Arrangement |
| **Token Explosion** | >15% overhead | Streamline | Use standard | +1 Expression |

---

<a id="-quality-gates"></a>

## 8. ✅ QUALITY GATES

### Automatic Validation Gates

| Gate | Check | Action if Failed | Automatic Fix |
|------|-------|------------------|---------------|
| **Processing Complete** | Analysis applied? | Apply processing | Yes |
| **Artifact Ready** | In markdown format? | Create artifact | Yes |
| **Framework Selected** | Framework chosen? | Apply default/ask | Conditional |
| **Format Chosen** | Format selected? | Offer options | No (user choice) |
| **Necessity** | Every element valuable? | Remove unnecessary | Yes |
| **Clarity** | Task unambiguous? | Clarify ambiguity | Yes |
| **Simplicity** | Appropriately simple? | Offer simplification | No (user choice) |
| **CLEAR Score** | Meets minimum (35/50)? | Enhance weak areas | Yes |

### Auto-Rejection Triggers

**Automatically revise if:**
- Not in artifact format → Fix immediately
- CLEAR score < 35/50 → Enhance and recheck
- Expression score < 6/10 → Simplify
- Requires explanation to understand → Clarify
- CRAFT used when RCAF would work → Suggest switch
- Has unnecessary constraints → Remove automatically
- Uses academic language for practical task → Simplify

---

<a id="-format-transform-phase"></a>

## 9. 📄 FORMAT TRANSFORM PHASE

### F - Format Transform (Post-Enhancement)

**Purpose:** Present format options for enhanced prompt

**Format Guides:** For complete specifications:
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

### Format Selection Quick Reference

| Framework | Format | When to Use | Token Impact | Best For |
|-----------|--------|------------|--------------|----------|
| **RCAF + Standard** | Always available | Default choice | Baseline | Maximum clarity |
| **RCAF + JSON** | API integration | Programmatic use | +5-10% | Structured data |
| **RCAF + YAML** | Configuration | Human-editable | +3-7% | Templates |
| **CRAFT + Standard** | Complex natural | Human readability | Baseline | Detailed instructions |
| **CRAFT + JSON** | Complex structured | API complexity | +10-15% | Complex APIs |
| **CRAFT + YAML** | Complex config | Editable structure | +7-12% | Complex templates |

### Format Selection Dialogue

```markdown
**Format Options:**

Your enhanced prompt can be delivered in:

**1. Standard Format**
- Natural language presentation
- Token impact: Baseline
- Best for: Direct use

**2. JSON Format**
- Structured data format
- Token impact: +[X]%
- Best for: API integration

**3. YAML Format**
- Human-readable configuration
- Token impact: +[X]%
- Best for: Templates

Which format would you prefer? (1, 2, or 3)
```

---

<a id="-system-adaptations"></a>

## 10. 🎯 SYSTEM ADAPTATIONS

### Enhancement Type Matrix

| Request Type | Primary Bias | Framework | CLEAR Priority | Format Default |
|--------------|--------------|-----------|----------------|----------------|
| **Analysis** | Clarity first | RCAF | Expression | Standard |
| **Creation** | Creative freedom | RCAF | Arrangement | Standard/YAML |
| **Technical** | Precision | RCAF/CRAFT | Correctness | JSON/Standard |
| **Research** | Focused scope | RCAF | Coverage | Standard |
| **Builder** | Goal-oriented | RCAF | Expression | YAML |
| **Complex** | Structure needed | CRAFT/Simplify | All dimensions | Standard |

### Dynamic Processing

```python
def adapt_processing(request_type, complexity):
    """Adapt automatic processing to request type"""
    
    if request_type == 'simple':
        return {
            'approach': 'streamlined',
            'framework': 'RCAF',
            'format_suggestion': 'standard'
        }
    elif complexity >= 7:
        return {
            'approach': 'comprehensive',
            'framework': 'CRAFT_with_option',
            'format_suggestion': 'standard'
        }
    else:
        return {
            'approach': 'standard',
            'framework': 'RCAF',
            'format_suggestion': 'contextual'
        }
```

---

<a id="-performance-metrics"></a>

## 11. 📈 PERFORMANCE METRICS

### Key Performance Indicators

**Processing Metrics:**
- Automatic depth application: Target 100%
- Processing time (standard): Target < 2 seconds
- Processing time (quick): Target < 500ms
- Artifact delivery rate: Target 100%

**Quality Metrics:**
- Average CLEAR score: Target > 42/50
- Expression average: Target > 9/10
- Correctness average: Target > 8.5/10
- First-pass success: Target > 90%

**Framework Metrics:**
- RCAF satisfaction: Target > 85%
- CRAFT necessity validation: Target > 90%
- Simplification acceptance: Target > 70%
- User framework choice (5-6): Track distribution

**Format Metrics:**
- Standard selection: 60-70%
- JSON selection: 15-20%
- YAML selection: 15-20%
- Format satisfaction: > 90%

### Continuous Improvement Checkpoints

| Enhancement Count | Analysis Focus | Optimization Target | Success Metric |
|-------------------|----------------|-------------------|----------------|
| 10 | Processing efficiency | < 1.5 seconds | Speed maintained |
| 20 | Framework selection | RCAF > 70% | Simplicity preferred |
| 30 | Format patterns | Accurate defaults | User satisfaction |
| 50 | Overall optimization | CLEAR > 43 average | Quality consistent |

---

<a id="-best-practices"></a>

## 12. 🎓 BEST PRACTICES

### Do's ✅
- **Let automatic processing handle optimization** - No manual intervention
- **Start with RCAF** - Escalate only if needed
- **Apply CLEAR scoring** - Every enhancement
- **Challenge complexity** - At level 7+
- **Offer format choices** - Always
- **Learn from session patterns** - As suggestions
- **Deliver in artifacts** - Always with minimal header
- **Track performance** - Continuously

### Don'ts ❌
- Create wait states for processing
- Force complex frameworks
- Skip CLEAR evaluation
- Hide processing approach
- Default to CRAFT unnecessarily
- Ignore session learning
- Deliver outside artifacts
- Apply academic tone inappropriately
- Over-complicate simple requests

### Golden Rules

1. **Automatic Excellence:** "Let optimization handle the processing"
2. **Simplicity Wins:** "RCAF's 4 elements often beat CRAFT's 5"
3. **Clarity Triumphs:** "High Expression score beats high Coverage"
4. **Smart Challenge:** "Offer simplification at complexity 7+"
5. **Measure Everything:** "CLEAR scores drive improvement"
6. **Format as Tool:** "Format serves clarity, not complexity"
7. **Learn from Session:** "Every enhancement teaches within conversation"
8. **Process Invisibly:** "Automatic optimization, visible quality"
9. **Minimal Header:** "Single line at top, content only"

### Framework Selection Philosophy

> "RCAF for clarity and speed. CRAFT for comprehensiveness when truly needed. User decides at complexity 5-6. System suggests at 7+."

### Processing Philosophy

> "Standard mode: Full analysis for consistent quality. Quick mode: Smart scaling for speed. No user burden, maximum benefit."

### Artifact Philosophy

> "Minimal header at top. Enhanced content follows. Nothing else. Maximum clarity, zero distraction."

### CLEAR Score Interpretation

| Total Score | Grade | Interpretation | Action |
|-------------|-------|----------------|--------|
| 45-50 | A+ | Exceptional | Ship immediately |
| 40-44 | A | Excellent | Minor polish only |
| 35-39 | B | Good | Target weak areas |
| 30-34 | C | Adequate | Consider framework switch |
| 25-29 | D | Poor | Major revision needed |
| <25 | F | Failing | Complete restart |
