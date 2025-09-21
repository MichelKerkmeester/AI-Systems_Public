# Product Design - Copywriter Frameworks v0.201

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

<a id="1-⚠️-critical-note"></a>

## 1. ⚠️ CRITICAL NOTE

### Core Principles

| **Principle** | **Details** | **Example** |
|--------------|------------|-------------|
| **Goal-based selection** | Apply based on objective, not keywords | "problem" ≠ automatic PATH |
| **Simple edits bypass** | Direct rewrites skip framework selection | Quick edits → no framework |
| **Intelligence enhancement** | Add data when differentiation matters | Tool comparison → add stats |
| **ATLAS determines complexity** | Thinking rounds guide framework depth | 1-2 rounds → simple framework |
| **Challenge Mode at 6+** | Always suggests simpler alternatives | 6+ rounds → auto-challenge |
| **Wait for user input** | Never proceed without thinking rounds response | ALWAYS WAIT |
| **Natural voice always** | Even frameworks use real language | No corporate speak |
| **Proper caps always** | Authentic still uses capitalization | Professional readability |

---

<a id="2-🚀-framework-decision-tree"></a>

## 2. 🚀 FRAMEWORK DECISION TREE

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

<a id="3-📋-framework-selection-matrix"></a>

## 3. 📋 FRAMEWORK SELECTION MATRIX

### Framework Selection Matrix (PRIMARY SOURCE)

| **Content Goal** | **Framework** | **Structure** | **Best For** | **Natural Example** |
|-----------------|---------------|---------------|--------------|---------------------|
| Simple edit | None needed | Direct edit | Quick rewrites | Just fix it |
| Share insight | SVC | Story→Value→Call | Social posts | "Here's what we learned" |
| Tell story | CASE | Context→Action→Solution→Evolution | Case studies | "Let me tell you about..." |
| Start discussion | QPT | Question→Perspective→Takeaway | Community | "What do you think?" |
| Document process | PATH | Problem→Approach→Test→Harvest | Methods | "Here's how we did it" |
| Teach something | HELP | Hook→Example→Lesson→Practice | Tutorials | "Let me show you" |
| Default/unclear | Match to goal | Varies | Adaptive | "Whatever works" |

**Notes:**
- Variations: See Main System for 3/2/1 rule
- Verification: Required for any statistics (see Design Intelligence)
- ATLAS integration: See ATLAS Framework
- Challenge at 6+ rounds: See ATLAS Framework Section 4
- Voice: Natural language always, proper caps always

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

<a id="4-📚-framework-library"></a>

## 4. 📚 FRAMEWORK LIBRARY


<a id="5-🎨-tone--framework-integration"></a>

## 🟢 Simple Frameworks (3-Part)

### SVC Framework → Story • Value • Call

**Structure:**
- Story: Brief situation or observation
- Value: Key insight or benefit
- Call: Question or action

**Example (Short form - 1-30 words) - NATURAL VOICE:**
Story: "Spent 3 hours debugging that z-index issue"
Value: "CSS grid solved it in 5 minutes"  
Call: "What's your debugging lifesaver?"

**When to use:** Quick insights, social posts, observations
**Typical length:** 1-30 words (see Main System for variations)
**Verification:** Required if statistics used (see Design Intelligence)

### QPT Framework → Question • Perspective • Takeaway

**Structure:**
- Question: Engaging opener
- Perspective: Your view or data
- Takeaway: Key learning or action

**Example - NATURAL VOICE:**
Question: "Should designers actually learn to code?"
Perspective: "Understanding constraints helps everyone collaborate better"
Takeaway: "Start with CSS basics, see what happens"

**When to use:** Community discussions, debates, thought leadership

### PATH Framework → Problem • Approach • Test • Harvest

**Structure:**
- Problem: Current pain or challenge
- Approach: Solution attempted
- Test: Validation method
- Harvest: Learning or result

**Example - NATURAL VOICE:**
Problem: "Navigation testing at 60% fail rate (ouch)"
Approach: "Card sorted with 20 real users"
Test: "A/B tested 3 variations for a week"
Harvest: "Turns out information scent matters most"

**When to use:** Process documentation, methodology sharing

---


<a id="6-✅-meqt-scoring-system"></a>

## 🟡 Medium Frameworks (4-Part)

### CASE Framework → Context • Action • Solution • Evolution

**Structure:**
- Context: Situation setup
- Action: What was done
- Solution: How it was resolved
- Evolution: What changed or improved

**Example - NATURAL VOICE:**
Context: "Onboarding had 60% drop-off, yikes"
Action: "Interviewed 20 frustrated users"
Solution: "Simplified to just 2 steps"
Evolution: "78% completion now, team's happy"

**When to use:** Case studies, project stories, journey documentation

### HELP Framework → Hook • Example • Lesson • Practice

**Structure:**
- Hook: Attention grabber
- Example: Concrete demonstration
- Lesson: Key teaching
- Practice: Application exercise

**Example - NATURAL VOICE:**
Hook: "Component keeps breaking? Same."
Example: "Our button had 47 re-renders (not kidding)"
Lesson: "React.memo is your friend"
Practice: "Profile your components, find the culprit"

**When to use:** Tutorials, how-to guides, educational content

---


<a id="7-📋-output-templates"></a>

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
**Challenge at 6+:** "Could we focus on just one phase instead?"
**Voice:** Still natural, just more detailed

---



## 5. 🎨 TONE + FRAMEWORK INTEGRATION

### Tone Impact on Frameworks (ALL NATURAL NOW)

| **Framework** | **+ Natural** | **+ Technical** | **+ Design Intel** | **Challenge at 6+** |
|--------------|--------------|-----------------|-------------------|-------------------|
| **SVC** | Personal story | Specific details | + Market data | "Skip the story?" |
| **CASE** | Journey format | Metrics included | + Salary context | "Just the outcome?" |
| **QPT** | Conversational | Precise language | + Industry stats | "Question only?" |
| **PATH** | Honest struggle | Data-driven | + Benchmarks | "Final learning?" |
| **HELP** | Approachable | Code examples | + Documentation | "Example only?" |

**Reality Check:** All tones now use human language, proper caps, no corporate speak

For complete tone specifications: See Voice & Tone Guide v0.201

---



## 6. ✅ MEQT SCORING SYSTEM

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



## 7. 📋 OUTPUT TEMPLATES

### Template Application

For complete artifact structure: See Artifact Standards & Templates v0.201

**Key Requirements:**
- Apply selected framework
- Generate variations per Main System (3/2/1 rule)
- Include proper formatting
- Document in AI System section
- Use natural voice always
- Maintain proper capitalization

---

<a id="8-🎯-problem-handling"></a>

## 8. 🎯 PROBLEM HANDLING

### Common Design Problems Matrix (NATURAL VOICE)

| **Problem** | **Reality** | **Counter** | **Framework** | **Natural Response** |
|------------|-------------|-------------|--------------|---------------------|
| **"Too slow"** | Process takes time | Show iteration value | CASE + Process | "Yeah, good stuff takes 3 rounds minimum" |
| **"Not technical"** | Design ≠ code | Technical premium | QPT + data | "Designers who code earn €15K more BTW" |
| **"Too expensive"** | vs no design | ROI demonstration | Direct compare | "€200K saved beats €150K salary" |
| **"Can't measure"** | ROI unclear | Measurement methods | PATH + method | "We track everything now, here's how" |
| **"Not scalable"** | One-off concern | System thinking | HELP + process | "Built it once, used it 100 times" |
| **"Too complex"** | Overwhelm fear | Simplification | SVC + clarity | "Start with one component, seriously" |

### Psychology-Based Concerns (MORE EMPATHETIC)

| **Designer Concerns** | **Response** | **Trust Element** | **Natural Language** |
|--------------------|-------------|------------------|---------------------|
| Imposter syndrome | "3 iterations is normal" | Process transparency | "We all feel like frauds sometimes" |
| Tool overwhelm | "One tool usually wins" | Market clarity | "Yeah, Figma basically owns everything now" |
| Career uncertainty | "Clear salary ranges exist" | Data grounding | "€120-180K is pretty standard" |
| Stakeholder pushback | "Show your process" | Documentation | "They trust you when they see the work" |
| Team dynamics | "Credit everyone" | Collaboration | "Sarah's idea saved the project" |
| Skill gaps | "Takes practice" | Growth mindset | "Nobody knows everything, relax" |

**Each problem gets variations based on exact word count per Main System**

---

<a id="9-❌-common-mistakes"></a>

## 9. ❌ COMMON MISTAKES

### Framework Selection Mistakes

| **Mistake** | **Impact** | **Prevention** |
|------------|-----------|---------------|
| CASE when SVC fits | Wrong structure | Check goal first |
| Missing harvest in PATH | Incomplete learning | Template check |
| Hook without practice | No action enabled | HELP checklist |
| No process transparency | Generic message | Add iterations |
| Wrong variation count | Poor scaling | Check word count |
| Poor formatting | Hard to read | Line breaks/dividers |
| Corporate language | Sounds fake | Use real words |
| All lowercase | Unprofessional | Proper caps always |

### ATLAS Integration Mistakes

| **Mistake** | **Impact** | **Prevention** |
|------------|-----------|---------------|
| Not asking thinking rounds | No user control | ALWAYS ASK AND WAIT |
| Skipping Challenge at 6+ | Complex content | Auto-trigger |
| Ignoring patterns | No learning | Track everything |
| Not using REPAIR | Quality issues | Monitor MEQT |
| Missing session learning | No improvement | Document patterns |
| Using unverified stats | Inaccuracy | Always verify |

### Voice Mistakes in Frameworks

| **Mistake** | **Impact** | **Prevention** | **Example Fix** |
|------------|-----------|---------------|----------------|
| Corporate speak | Sounds fake | Use real words | "Leverage" → "Use" |
| All lowercase | Hard to read | Proper caps always | "took 3 tries" → "Took 3 tries" |
| Perfect process | Unbelievable | Show the mess | Add "failed twice first" |
| No team credit | Seems arrogant | Credit everyone | "Our QA spotted it" |
| Too formal | Not engaging | Natural voice | "Therefore" → "So" |

---

<a id="10-🧠-atlas-integration"></a>

## 10. 🧠 ATLAS INTEGRATION

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

<a id="11-🔄-pattern-learning"></a>

## 11. 🔄 PATTERN LEARNING

### Framework Pattern Tracking

**What to track:**
- Which frameworks succeed (MEQT 18+)
- User selection patterns
- Audience-framework correlation
- Stat effectiveness per framework
- Variation preferences
- Voice tolerance levels

**How to apply:**
- Patterns inform suggestions
- Never restrict choices
- User can always override
- Track but don't force
- Learn from each use

### REPAIR Protocol for Frameworks

```markdown
R - Recognize: Framework not working
E - Explain: "CASE too long for social post"
P - Propose: 
    1. Switch to SVC (simpler)
    2. Shorten CASE (hybrid)
    3. Continue full (original)
A - Adapt: Apply selected approach
I - Iterate: Test improvement
R - Record: Framework preference noted
```

---

<a id="12-📝-content-formulas"></a>

## 12. 📝 CONTENT FORMULAS

### Proven Content Formulas (ALL NATURAL NOW)

**Process Story Pattern:**
"Took [X] iterations to nail it (yeah, really)"
→ Use in: Story element of SVC, Context of CASE

**Tool Reality Pattern:**
"[Tool] has like [%] of the market now"
→ Use in: Value element of SVC, Solution of CASE
→ Requires verification (always check current stats)

**Team Credit Pattern:**
"Our [role] figured out that [insight]"
→ Use in: Any framework for trust building

**Learning Share Pattern:**
"Failed hard at [X], learned [Y] though"
→ Use in: Harvest of PATH, Evolution of CASE

**Career Path Pattern:**
"Went from [A] to [B] in [time] (wild ride)"
→ Use in: Context setting, journey framing

**Pain Point Pattern:**
"Yeah, [problem] really sucks, here's what helped"
→ Use in: Problem element of PATH, Hook of HELP

**Solution Pattern:**
"Tried everything, [X] actually worked"
→ Use in: Solution of CASE, Takeaway of QPT

**Reality Check Pattern:**
"Not perfect but ships (good enough)"
→ Use in: Any framework for authenticity

**Collaboration Pattern:**
"[Role] and [role] figured this out together"
→ Use in: Team credit across all frameworks

**Uncertainty Pattern:**
"Still figuring out [X], but [Y] helps"
→ Use in: Natural voice in any framework

### Formula Application Rules

- Make frameworks feel like actual conversations
- Add natural uncertainty where appropriate
- Credit team members by name when possible
- Show iterations and failures
- Use casual language with proper caps
- Include "BTW" or "honestly" for natural flow
- Verify all stats before using
- Keep EUR currency consistent

---

*Frameworks structure thinking, not creativity. ATLAS guides depth, Challenge Mode ensures simplicity (always at 6+ rounds). Pattern Learning makes selection smarter. Design Intelligence strengthens positioning when verified. Process transparency builds trust. Team credit reflects reality. Natural voice beats corporate speak. Proper caps maintain professionalism. Every session makes framework selection more intelligent. We're all just trying to ship good stuff.*