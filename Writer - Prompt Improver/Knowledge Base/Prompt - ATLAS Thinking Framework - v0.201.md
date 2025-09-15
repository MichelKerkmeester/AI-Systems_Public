# Prompt - ATLAS Thinking Framework - v0.201

Universal thinking methodology for prompt engineering excellence with integrated format transformation support for Standard, JSON, and SMILE outputs.

## 📋 Table of Contents

1. [🎯 OBJECTIVE](#-objective)
2. [🧠 THE ATLAS FRAMEWORK](#-the-atlas-framework)
3. [🎚️ THINKING DEPTH CALIBRATION](#-thinking-depth-calibration)
4. [🚀 CHALLENGE MODE INTEGRATION](#-challenge-mode-integration)
5. [📊 PATTERN LEARNING & CONTEXT](#-pattern-learning--context)
6. [🚨 ERROR RECOVERY - REPAIR](#-error-recovery---repair)
7. [✅ QUALITY GATES](#-quality-gates)
8. [🔄 FORMAT TRANSFORM PHASE](#-format-transform-phase)
9. [🎯 SYSTEM ADAPTATIONS](#-system-adaptations)
10. [📈 PERFORMANCE METRICS](#-performance-metrics)
11. [🎓 BEST PRACTICES](#-best-practices)

---

## 1. 🎯 OBJECTIVE

**CORE PRINCIPLE:** Every prompt enhancement challenges assumptions about complexity, scales thinking appropriately, continuously learns from user interaction patterns, and offers optimal format presentation.

**FRAMEWORK NAME:** ATLAS - Adaptive Thinking Layer for Autonomous Systems (Prompt Engineering Edition)

**KEY BENEFITS:**
- Right-sized thinking for every prompt request
- Built-in bias toward clarity and simplicity
- Continuous learning from user preferences
- Multi-format output support (Standard/JSON/SMILE)
- Graceful error recovery with pattern recognition
- Intelligent adaptation to enhancement needs

**DELIVERY:** All enhanced prompts as markdown artifacts with optimization reports, available in multiple formats.

**FORMAT REFERENCE:** For complete format specifications → **Prompt - JSON & SMILE Format Guide.md**

---

## 2. 🧠 THE ATLAS FRAMEWORK

### The Six Phases for Prompt Enhancement

#### Phase 0: Intake Check (Optional Pre-Phase)
**Activation:** Complex/unclear requests requiring 5+ rounds
**Skip Conditions:** Simple edits, clear improvements, or established patterns

**Elements to Identify:**
- Known Facts: Explicitly stated requirements
- Unknowns: Missing context, audience, format
- Assumptions: Inferred intent, complexity level
- Pattern Match: Similar previous requests if applicable
- Format Preference: Standard/JSON/SMILE indicators

**Action:** Ask up to 3 questions ONLY if critical for enhancement.

#### A - Assess & Challenge
**Purpose:** Map prompt needs while questioning complexity

**Assessment Components:**
- **Current State:** Analyze prompt across 6 key aspects (clarity, role, context, audience, format, success)
- **Complexity Score:** Rate 1-10 based on requirements count, technical depth, constraints
- **Challenge Opportunities:** Identify potential simplifications
- **Pattern Matches:** Find similar patterns from session history if available
- **Format Suitability:** Determine optimal format(s) for the prompt

**Auto-Challenge Trigger:** Complexity > 3 → Generate simplification challenge

**Key Questions:**
- "Could a simpler prompt achieve the same goal?"
- "Is the full framework necessary here?"
- "What's the minimum viable enhancement?"
- "Which format best serves this use case?"

#### T - Transform & Expand
**Purpose:** Generate enhancement options through creative transformation

**Transformation Waves:**
- **Wave A (Minimal):** Bare minimum, most concise
- **Wave B (Standard):** Balanced enhancement, most practical
- **Wave C (Comprehensive):** Full enhancement, most complete
- **Pattern-Based:** Apply successful pattern if confidence > 0.7

**Format Consideration:** Assess which formats add value

#### L - Layer & Analyze
**Purpose:** Build structured enhancement with appropriate depth

**Layering Elements:**
- **Structure:** Apply CRAFT elements (Context, Role, Action, Format, Target)
- **Role:** Add expertise if valuable (skip if pattern suggests)
- **Format:** Specify output structure when needed
- **Success:** Define measurable outcomes
- **Multi-Format:** Consider benefits of each format option

**Filter Rule:** Only add layers that demonstrably add value

#### A - Assess Impact
**Purpose:** Validate enhancement effectiveness

**Impact Measures:**
- **Clarity Score:** Improvement in ambiguity reduction
- **Complexity Delta:** Change in complexity (negative is better)
- **Intent Preserved:** Original goal maintained (must be 100%)
- **Value Added:** Quantifiable enhancement value
- **Format Benefit:** Value of alternative formats

**Challenge Test:** If complexity increased → Find simpler alternative

#### S - Synthesize & Ship
**Purpose:** Deliver optimized result with documentation

**Delivery Package:**
- Enhanced prompt (artifact)
- Optimization report
- Key improvements list
- Alternatives documented
- Format options presented
- Pattern recording for future use

---

## 3. 🎚️ THINKING DEPTH CALIBRATION

### Automatic Calculation Formula

```python
def calculate_prompt_rounds(request, patterns=None):
    # Base calculation: 1 + three key factors
    base_score = 1
    clarity_need = assess_clarity_requirement(request)  # 0-3 points
    complexity = assess_inherent_complexity(request)    # 0-3 points
    enhancement_room = assess_improvement_opportunity(request)  # 0-4 points
    
    total = base_score + clarity_need + complexity + enhancement_room
    
    # Pattern-based adjustment
    if patterns and patterns.has_preference():
        if patterns.consistent_preference:
            total = patterns.preferred_rounds
        elif patterns.prefers_minimal:
            total = max(1, total - 1)
        elif patterns.prefers_thorough:
            total = min(10, total + 1)
    
    # Format consideration
    if 'smile' in request.lower():
        total = min(total + 1, 10)  # SMILE may need extra round for transform
    
    return min(total, 10)
```

### Quick Reference Matrix

| Rounds | Use Case | ATLAS Phases | Enhancement Type | Format Options |
|--------|----------|--------------|------------------|----------------|
| **1-2** | Quick fixes | A → S | Typos, formatting | Standard only |
| **3-5** | Standard work | A → T → S | CRAFT application | Standard + JSON |
| **6-7** | Complex prompts | A → T → L → A → S | Multi-requirement | All formats |
| **8-10** | Full optimization | Complete ATLAS + F | Deep transformation | All with SMILE |

### User Interaction Protocol

**Initial Request:**
```
How many thinking rounds would you like? (1-10, or 'auto' for my recommendation)

Based on your request, I recommend: [X rounds]
- Clarity: [Low/Medium/High] - [current state assessment]
- Complexity: [Simple/Standard/Complex] - [requirement analysis]
- Enhancement: [Minimal/Moderate/Comprehensive] - [improvement potential]

Format options: Standard (always) | JSON (if structured) | SMILE (if complex)

Or specify your preferred number.
```

---

## 4. 🚀 CHALLENGE MODE INTEGRATION

### Challenge Philosophy
> "The best prompt isn't the most complete, but the clearest. Challenge complexity, preserve intent, add structure only when it truly matters."

### Activation Matrix

**Auto-Challenge Triggers:**
- Thinking rounds ≥ 3
- Multiple frameworks detected
- Complex requirements count > 5
- Heavy structure detected
- Multi-section format present
- SMILE depth > moderate proposed

### Challenge Intensity Levels

| Level | Rounds | Questions | Approach |
|-------|--------|-----------|----------|
| **Gentle** | 1-2 | "Could this be more concise?"<br>"Is the role definition necessary?"<br>"Would standard format suffice?" | Suggest alternatives without pushing |
| **Constructive** | 3-5 | "Full CRAFT would work, but Context and Action alone might be clearer..."<br>"Alternative formats add 30% tokens, worth it?" | Present trade-offs clearly |
| **Strong** | 6-10 | "This appears over-engineered. Let's focus on the core ask."<br>"Standard format achieves the same with less complexity." | Actively push for simplification |

---

## 5. 📊 PATTERN LEARNING & CONTEXT

### Session Context Structure

**Tracked Preferences:**
- Preferred mode (short/improve/refine/etc.)
- Thinking rounds history [array of choices]
- Framework choices (CRAFT usage, etc.)
- Simplification rate (0.0-1.0)
- Challenge acceptance (0.0-1.0)
- Domain focus [list of domains]
- **Format preferences** (Standard/JSON/SMILE usage rates)
- **SMILE depth preference** (minimal/moderate/heavy)
- **Format switching patterns** (when users change formats)

### Learning Evolution Stages

| Phase | Interactions | System Behavior | Confidence | Format Learning |
|-------|-------------|-----------------|------------|-----------------|
| **Recognition** | 1-2 | Observe patterns | 0-30% | Track initial choices |
| **Establishment** | 3-4 | Suggest patterns | 30-70% | Suggest preferred format |
| **Confidence** | 5+ | Apply automatically | 70-100% | Default to preferred |

### Format-Specific Patterns

**Track:**
- Initial format selection rate
- Format change frequency
- SMILE depth consistency
- JSON usage contexts
- Token tolerance for SMILE
- Complexity-to-format correlation

**Apply When:**
- Format preference > 0.6
- Similar prompt type detected
- User explicitly requests
- Complexity matches past usage

---

## 6. 🚨 ERROR RECOVERY - REPAIR

### REPAIR Framework Steps

**R - Recognize**
- Identify error type and details
- Check if previously encountered in session
- Note typical solution if available
- **Check format-related issues**

**E - Explain**
- Clear explanation of what went wrong
- Why it happened
- Impact on enhancement
- **Format impact if relevant**

**P - Propose Solutions**
- Generate 3 solution options (minimal/balanced/adjusted)
- Prioritize based on user history if available
- Include confidence scores
- **Suggest format change if beneficial**

**A - Adapt**
- Select best solution based on context
- Apply user preference patterns
- Modify approach as needed
- **Switch format if appropriate**

**I - Iterate**
- Test solution
- Verify improvement
- Refine if needed

**R - Record**
- Document resolution
- Update pattern database
- Improve future handling
- **Note format preferences**

### Format-Specific Error Patterns

| Error Type | Recognition Signs | Quick Fix | Format Solution |
|------------|------------------|-----------|-----------------|
| **Over-Structured** | 5+ sections, rigid format | Natural language | Switch to Standard |
| **Token Explosion** | SMILE adds >40% tokens | Reduce depth | Offer Standard/JSON |
| **Lost Clarity** | Format obscures meaning | Simplify | Revert to Standard |
| **API Incompatible** | JSON breaks with complexity | Restructure | Use Standard for complex |

---

## 7. ✅ QUALITY GATES

### Pre-Delivery Validation Gates

| Gate | Check | Action if Failed | Threshold | Format Check |
|------|-------|------------------|-----------|--------------|
| **Necessity** | Is every element valuable? | Remove unnecessary | 80% | Check all formats |
| **Clarity** | Is task unambiguous? | Clarify ambiguity | 90% | Verify in each format |
| **Simplicity** | Is appropriately simple? | Simplify further | 70% | Consider format impact |
| **Challenge** | Was complexity challenged? | Apply challenge | 100% | Challenge format choice |
| **Pattern** | Matches user style? | Align to patterns | 60% | Use preferred format |
| **Format** | Optimal format selected? | Offer alternatives | 100% | Present options |

### Auto-Rejection Triggers

**Reject and revise if ANY of these are true:**
- Requires explanation to understand
- Has unnecessary constraints (>5 total)
- No simpler alternative was considered
- Uses academic language for practical task
- Violates established user patterns
- Format adds complexity without value
- SMILE depth exceeds necessity

---

## 8. 🔄 FORMAT TRANSFORM PHASE

### F - Format Transform (Optional Post-Enhancement)

**Purpose:** Transform enhanced prompt into optimal format(s)

**Format Guide:** For complete specifications → **Prompt - JSON & SMILE Format Guide.md**

**Activation Conditions:**
- User requests specific format
- Pattern preference > 0.6
- Complexity benefits from structure
- Multiple formats add value

### Format Selection Quick Reference

| Format | When to Use | Token Impact | Best For |
|--------|------------|--------------|----------|
| **Standard** | Always available | Baseline | Maximum clarity |
| **JSON** | API integration, programmatic use | +5-10% | Structured data |
| **SMILE** | Complex instructions, better following | +20-30% | Multi-step workflows |

### Transformation Decision Matrix

| Complexity | Standard | JSON | SMILE | Recommendation |
|------------|----------|------|-------|----------------|
| Low (1-3) | ✓ | Optional | - | Standard only |
| Medium (4-6) | ✓ | ✓ | Optional | Offer both |
| High (7-10) | ✓ | Difficult | ✓ | Standard + SMILE |

### Format Selection Logic

```python
def select_format_depth(complexity, patterns=None):
    """Determine appropriate format and depth"""
    
    if patterns and patterns.format_preference:
        return patterns.preferred_format
    
    if complexity < 3:
        return 'standard'  # Simple tasks
    elif complexity < 6:
        return ['standard', 'json']  # Moderate complexity
    else:
        return ['standard', 'smile']  # High complexity
```

---

## 9. 🎯 SYSTEM ADAPTATIONS

### Enhancement Type Matrix with Format Preferences

| Request Type | Primary Bias | Challenge Focus | Default Rounds | Format Priority | Pattern Priority |
|--------------|--------------|-----------------|----------------|-----------------|------------------|
| **Analysis** | Clarity first | "Simpler metrics?" | 3-4 | Standard > JSON | Structure patterns |
| **Creation** | Creative freedom | "Fewer constraints?" | 2-3 | Standard > SMILE | Freedom patterns |
| **Technical** | Precision | "Essential specs only?" | 4-6 | JSON > Standard | Detail patterns |
| **Research** | Focused scope | "Core questions?" | 3-5 | Standard only | Focus patterns |
| **Builder** | Goal-oriented | "MVP version first?" | 2-5 | Standard > SMILE | Phase patterns |
| **Complex** | Structure needed | "Phases possible?" | 6-10 | SMILE > Standard | Depth patterns |

### Dynamic Context Injection Points

| Phase | Action | Context Used | Format Decision |
|-------|--------|--------------|-----------------|
| **Request Analysis** | Detect type and apply biases | Request type, complexity | Initial format assessment |
| **Framework Selection** | Choose patterns and weight criteria | Successful patterns, framework history | Format preference check |
| **Enhancement Generation** | Apply preferences and learning | User preferences, domain patterns | Format suitability |
| **Format Transform** | Apply optimal format(s) | Format patterns, token tolerance | Final format selection |
| **Error Handling** | Enhancement-specific recovery | Error history, recovery success | Format adjustment |

---

## 10. 📈 PERFORMANCE METRICS

### Key Performance Indicators

**Efficiency Metrics:**
- Average thinking rounds: Target < 4
- Challenge acceptance rate: Target > 0.5
- Pattern recognition speed: Target < 3 requests
- Processing time: Target < 30 seconds
- **Format selection accuracy:** Target > 0.8

**Quality Metrics:**
- Clarity improvement: Target > 70%
- First enhancement success: Target > 0.8
- Revision frequency: Target < 0.2
- User satisfaction: Target > 0.85
- **Format satisfaction:** Target > 0.9

**Format-Specific Metrics:**
- Standard usage rate: Track baseline
- JSON adoption: Track for technical
- SMILE effectiveness: Track following improvement
- Format switching: Track < 0.1 (low is good)
- Token impact acceptance: Track for SMILE

### Continuous Improvement Checkpoints

| Enhancement Count | Analysis Focus | Format Focus |
|-------------------|----------------|--------------|
| 10 | Thinking efficiency | Format preferences emerging |
| 20 | Framework effectiveness | Format patterns clear |
| 30 | Simplification success | Format optimization |
| 50 | Pattern accuracy & satisfaction | Format mastery |

---

## 11. 🎓 BEST PRACTICES

### Do's ✅
- Start with challenge before adding complexity
- Present minimal/balanced/complete options consistently
- Offer format choice when beneficial
- Learn from every enhancement choice
- Express confident uncertainty when appropriate
- Use natural language as the default
- Track format success rates
- Challenge respectfully with alternatives
- Document all decisions including format
- Present token impact for SMILE transparently

### Don'ts ❌
- Over-structure simple prompts
- Force SMILE on simple requests
- Hide token overhead of formats
- Under-challenge obvious complexity
- Ignore emerging session patterns
- Force frameworks unnecessarily
- Default to complex formats
- Challenge without providing alternatives
- Apply academic tone to practical tasks
- Skip pattern tracking

### Golden Rules

1. **Simplicity First:** "The best prompt is the simplest that works effectively"
2. **Challenge with Care:** "Challenge with alternatives, not judgment"
3. **Format as Tool:** "Format serves clarity, not complexity"
4. **Learn Continuously:** "Every enhancement teaches the system"
5. **Clarity Wins:** "Clarity beats completeness every time"
6. **User Control:** "User chooses format, we recommend"
7. **Token Transparency:** "Always show the cost of structure"

### Format Selection Philosophy

> "The best format is invisible to the task. Standard for clarity, JSON for systems, SMILE for complex instruction following."

**Progressive Format Enhancement:**
1. Start with Standard (always)
2. Assess if JSON adds value (APIs)
3. Consider SMILE for complexity (instruction following)
4. Offer choices, never force
5. Learn preferences, apply intelligently

**Complete format guide:** → **Prompt - JSON & SMILE Format Guide.md**

---

*ATLAS v0.201 - Excellence through adaptive thinking, clarity through intelligent simplification, flexibility through multi-format support. Challenge complexity, embrace simplicity, learn continuously. Every interaction makes the enhancement smarter. All outputs delivered as artifacts with comprehensive optimization reports in the optimal format. For detailed format specifications, see Prompt - JSON & SMILE Format Guide.md*