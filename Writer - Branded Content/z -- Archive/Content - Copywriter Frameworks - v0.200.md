# Product Design - Copywriter Frameworks v0.200

## 📚 Table of Contents

1. [⚠️ Critical Note](#1-⚠️-critical-note)
2. [🚀 Framework Decision Tree](#2-🚀-framework-decision-tree)
3. [📋 Framework Selection Matrix](#3-📋-framework-selection-matrix)
4. [📚 Framework Library](#4-📚-framework-library)
5. [🎨 Tone + Framework Integration](#5-🎨-tone--framework-integration)
6. [✅ MEQT Scoring System](#6-✅-meqt-scoring-system)
7. [📋 Output Templates](#7-📋-output-templates)
8. [🎯 Problem Handling](#8-🎯-problem-handling)
9. [❌ Common Mistakes](#9-❌-common-mistakes)
10. [🧠 ATLAS Integration](#10-🧠-atlas-integration)
11. [🔄 Pattern Learning](#11-🔄-pattern-learning)
12. [📝 Content Formulas](#12-📝-content-formulas)

---

## 1. ⚠️ Critical Note

### Core Principles

| **Principle** | **Details** | **Example** |
|--------------|------------|-------------|
| **Goal-based selection** | Apply based on objective, not keywords | "problem" ≠ automatic PATH |
| **Simple edits bypass** | Direct rewrites skip framework selection | Quick edits → no framework |
| **Intelligence enhancement** | Add data when differentiation matters | Tool comparison → add stats |
| **ATLAS determines complexity** | Thinking rounds guide framework depth | 1-2 rounds → simple framework |
| **Challenge Mode at 6+** | Always suggests simpler alternatives | 6+ rounds → auto-challenge |
| **Wait for user input** | Never proceed without thinking rounds response | ALWAYS WAIT |

---

## 2. 🚀 Framework Decision Tree

### Simplified Decision Flow

```
START
  ↓
What's your content goal?
  ↓
Is it a simple edit?
  YES → No framework needed
  NO ↓
  
Sharing an insight?
  YES → SVC Framework
  NO ↓
  
Telling a project story?
  YES → CASE Framework
  NO ↓
  
Starting a discussion?
  YES → QPT Framework
  NO ↓
  
Documenting process?
  YES → PATH Framework
  NO ↓
  
Teaching something?
  YES → HELP Framework
  NO ↓
  
DEFAULT → Match user goal to framework
```

---

## 3. 📋 Framework Selection Matrix

### Framework Selection Matrix (PRIMARY SOURCE)

| **Content Goal** | **Framework** | **Structure** | **Best For** |
|-----------------|---------------|---------------|--------------|
| Simple edit | None needed | Direct edit | Quick rewrites |
| Share insight | SVC | Story→Value→Call | Social posts, observations |
| Tell story | CASE | Context→Action→Solution→Evolution | Case studies, journeys |
| Start discussion | QPT | Question→Perspective→Takeaway | Community engagement |
| Document process | PATH | Problem→Approach→Test→Harvest | Methodology sharing |
| Teach something | HELP | Hook→Example→Lesson→Practice | Tutorials, guides |
| Default/unclear | Match to goal | Varies | Adaptive selection |

**Notes:**
- Variations: See Main System for 3/2/1 rule
- Verification: Required for any statistics (see Design Intelligence)
- ATLAS integration: See ATLAS Framework
- Challenge at 6+ rounds: See ATLAS Framework Section 4

### Framework Selection Logic

```python
def select_framework(goal, patterns=None):
    """Framework selection with pattern awareness"""
    
    # Primary decision tree
    framework_map = {
        'simple_edit': None,           # No framework needed
        'share_insight': 'SVC',
        'tell_story': 'CASE',
        'start_discussion': 'QPT',
        'document_process': 'PATH',
        'teach_something': 'HELP'
    }
    
    # Determine goal type
    goal_type = analyze_goal(goal)
    framework = framework_map.get(goal_type, 'ADAPTIVE')
    
    # Apply patterns if available (never restricts options)
    if patterns and patterns.get('success_rate', {}).get(framework, 0) > 0.8:
        # Suggest successful framework but user chooses
        suggested = patterns['preferred_framework']
        return framework, suggested  # Return both options
    
    return framework, None  # No pattern suggestion

def analyze_goal(goal_text):
    """Determine primary goal from request"""
    if 'edit' in goal_text or 'rewrite' in goal_text:
        return 'simple_edit'
    elif 'share' in goal_text or 'insight' in goal_text:
        return 'share_insight'
    # ... etc
    return 'unclear'
```

---

## 4. 📚 Framework Library

## 🟢 Simple Frameworks (3-Part)

### SVC Framework → Story • Value • Call

**Structure:**
- Story: Brief situation or observation
- Value: Key insight or benefit
- Call: Question or action

**Example (Short form - 1-30 words):**
Story: "Spent 3 hours debugging z-index"
Value: "CSS grid solved everything"  
Call: "What's your debugging lifesaver?"

**When to use:** Quick insights, social posts, observations
**Typical length:** 1-30 words (see Main System for variations)
**Verification:** Required if statistics used (see Design Intelligence)

### QPT Framework → Question • Perspective • Takeaway

**Structure:**
- Question: Engaging opener
- Perspective: Your view or data
- Takeaway: Key learning or action

**Example:**
Question: "Should designers code?"
Perspective: "Understanding constraints helps collaboration"
Takeaway: "Start with CSS basics"

**When to use:** Community discussions, debates, thought leadership

### PATH Framework → Problem • Approach • Test • Harvest

**Structure:**
- Problem: Current pain or challenge
- Approach: Solution attempted
- Test: Validation method
- Harvest: Learning or result

**Example:**
Problem: "Navigation testing at 60% fail rate"
Approach: "Card sorting with 20 users"
Test: "A/B tested 3 variations"
Harvest: "Information scent matters most"

**When to use:** Process documentation, methodology sharing

---

## 🟡 Medium Frameworks (4-Part)

### CASE Framework → Context • Action • Solution • Evolution

**Structure:**
- Context: Situation setup
- Action: What was done
- Solution: How it was resolved
- Evolution: What changed or improved

**Example:**
Context: "Onboarding had 60% drop-off"
Action: "Interviewed 20 users"
Solution: "Simplified to 2 steps"
Evolution: "78% completion now"

**When to use:** Case studies, project stories, journey documentation

### HELP Framework → Hook • Example • Lesson • Practice

**Structure:**
- Hook: Attention grabber
- Example: Concrete demonstration
- Lesson: Key teaching
- Practice: Application exercise

**Example:**
Hook: "Component keeps breaking"
Example: "Button with 47 re-renders"
Lesson: "Use React.memo"
Practice: "Profile your components"

**When to use:** Tutorials, how-to guides, educational content

---

## 🔴 Complex Framework (5+ Part)

### Design Process Framework → Discover • Define • Develop • Deliver • Document

**Structure:**
- Discover: Research and insights
- Define: Problem framing
- Develop: Solution creation
- Deliver: Implementation
- Document: Learning capture

**When to use:** Full case studies, comprehensive documentation
**Requires:** Full ATLAS cycle
**Challenge at 6+:** "Could we focus on one phase?"

---

## 5. 🎨 Tone + Framework Integration

### Tone Impact on Frameworks

| **Framework** | **+ Natural** | **+ Technical** | **+ Design Intel** | **Challenge at 6+** |
|--------------|--------------|-----------------|-------------------|-------------------|
| **SVC** | Personal story | Precise details | + Market share data | "Skip story?" |
| **CASE** | Journey format | Metrics-heavy | + Salary context | "Just outcome?" |
| **QPT** | Conversational | Specific | + Industry context | "Question only?" |
| **PATH** | Honest struggle | Data-driven | + Benchmarks | "Final learning?" |
| **HELP** | Approachable | Code examples | + Documentation | "Example only?" |

For complete tone specifications: See Voice & Tone Guide

---

## 6. ✅ MEQT Scoring System

### MEQT Scoring System (PRIMARY SOURCE - 23 points total)

**Components:**
1. **Message Clarity** (4 points)
   - Is value clear? (2 points)
   - Is next step obvious? (2 points)

2. **Effectiveness** (8 points)
   - Problem addressed? (3 points)
   - Trust built? (3 points)
   - Learning enabled? (2 points)

3. **Quality** (4 points)
   - Grammar correct? (2 points)
   - Platform appropriate? (2 points)

4. **Targeting** (4 points)
   - Right audience? (2 points)
   - Appropriate language? (2 points)

5. **Differentiation & Trust** (3 points)
   - Process shown? (1 point)
   - Team credited? (1 point)
   - Data verified? (1 point bonus if verified)

**Scoring Actions:**
- 21-23: Ship immediately
- 18-20: Minor polish only
- 15-17: Strengthen key areas
- 12-14: Apply REPAIR Protocol (see ATLAS Framework)
- Below 12: Complete redo

**Note:** Verification bonus available if stats properly verified (see Design Intelligence)

### Scoring Calculation

```python
def calculate_meqt_score(content):
    """Calculate MEQT score for content"""
    
    score = 0
    
    # Message Clarity (4 points)
    if value_is_clear(content): score += 2
    if next_step_obvious(content): score += 2
    
    # Effectiveness (8 points)
    if problem_addressed(content): score += 3
    if trust_built(content): score += 3
    if learning_enabled(content): score += 2
    
    # Quality (4 points)
    if grammar_correct(content): score += 2
    if platform_appropriate(content): score += 2
    
    # Targeting (4 points)
    if right_audience(content): score += 2
    if appropriate_language(content): score += 2
    
    # Differentiation & Trust (3 points)
    if process_shown(content): score += 1
    if team_credited(content): score += 1
    if data_verified(content): score += 1  # Bonus point
    
    return score
```

---

## 7. 📋 Output Templates

### Template Application

For complete artifact structure: See Artifact Standards & Templates

**Key Requirements:**
- Apply selected framework
- Generate variations per Main System (3/2/1 rule)
- Include proper formatting
- Document in AI System section

---

## 8. 🎯 Problem Handling

### Common Design Problems Matrix

| **Problem** | **Reality** | **Counter** | **Framework** | **ATLAS** |
|------------|-------------|-------------|--------------|-----------|
| **"Too slow"** | Process takes time | Show iteration value | CASE + Process | A→T→S |
| **"Not technical"** | Design ≠ code | Technical premium value | QPT + data | A→T→S |
| **"Too expensive"** | vs no design | ROI demonstration | Direct compare | A→S |
| **"Can't measure"** | ROI unclear | Measurement methods | PATH + method | A→T→S |

### Psychology-Based Concerns

| **Designer Concerns** | **Response** | **Trust Element** |
|--------------------|-------------|------------------|
| Imposter syndrome | "3 iterations is normal" | Process transparency |
| Tool overwhelm | "Leading tools dominate" | Market clarity |
| Career uncertainty | "Clear salary ranges" | Data grounding |
| Stakeholder pushback | "Show your process" | Documentation |

**Each problem gets variations based on exact word count per Main System**

---

## 9. ❌ Common Mistakes

### Framework Selection Mistakes

| **Mistake** | **Impact** | **Prevention** |
|------------|-----------|---------------|
| CASE when SVC fits | Wrong structure | Check goal first |
| Missing harvest in PATH | Incomplete learning | Template check |
| Hook without practice | No action enabled | HELP checklist |
| No process transparency | Generic message | Add iterations |
| Wrong variation count | Poor scaling | Check word count |
| Poor formatting | Hard to read | Line breaks/dividers |

### ATLAS Integration Mistakes

| **Mistake** | **Impact** | **Prevention** |
|------------|-----------|---------------|
| Not asking thinking rounds | No user control | ALWAYS ASK AND WAIT |
| Skipping Challenge at 6+ | Complex content | Auto-trigger |
| Ignoring patterns | No learning | Track everything |
| Not using REPAIR | Quality issues | Monitor MEQT |
| Missing session learning | No improvement | Document patterns |

---

## 10. 🧠 ATLAS Integration

### Framework Selection by ATLAS Phase

| **ATLAS Phase** | **Framework Actions** | **Key Decisions** |
|----------------|---------------------|------------------|
| **A - Assess** | Map content needs, check history | Framework needed? Word count? |
| **T - Transform** | Generate 3-5 options | Which framework? How many versions? |
| **L - Layer** | Add intelligence | Which stats? Process elements? |
| **A - Assess Impact** | MEQT scoring | Pass quality gates? |
| **S - Synthesize** | Apply and deliver | Document patterns |

For complete ATLAS methodology: See ATLAS Framework

---

## 11. 🔄 Pattern Learning

### Framework Pattern Tracking

**What to track:**
- Which frameworks succeed (MEQT 18+)
- User selection patterns
- Audience-framework correlation
- Stat effectiveness per framework
- Variation preferences

**How to apply:**
- Patterns inform suggestions
- Never restrict choices
- User can always override
- Track but don't force

### REPAIR Protocol for Frameworks

```markdown
R - Recognize: Framework not resonating
E - Explain: "CASE too long for social"
P - Propose: 
    1. Switch to SVC (simpler)
    2. Shorten CASE (hybrid)
    3. Continue full (original)
A - Adapt: Apply selected approach
I - Iterate: Test improvement
R - Record: Framework preference noted
```

---

## 12. 📝 Content Formulas

### Proven Content Formulas

**Process Story Pattern:**
"Took [X] iterations to [result]"
→ Use in: Story element of SVC, Context of CASE

**Tool Reality Pattern:**
"[Tool] at [%] market share"
→ Use in: Value element of SVC, Solution of CASE
→ Requires verification (see Design Intelligence)

**Team Credit Pattern:**
"Our [role] discovered [insight]"
→ Use in: Any framework for trust building

**Learning Share Pattern:**
"Failed at [X], learned [Y]"
→ Use in: Harvest of PATH, Evolution of CASE

**Career Path Pattern:**
"From [A] to [B] in [time]"
→ Use in: Context setting, journey framing

**Application:** Enhance frameworks with these patterns when relevant

---

*Frameworks structure thinking, not creativity. ATLAS guides depth, Challenge Mode ensures simplicity (always at 6+ rounds). Pattern Learning makes selection smarter. Design Intelligence strengthens positioning when verified. Process transparency builds trust. Team credit reflects reality. Every session makes framework selection more intelligent.*