# Content - Copywriter Frameworks - v0.120

## Table of Contents
1. [⚠️ Critical Note](#1-⚠️-critical-note)
2. [🚀 Framework Decision Tree](#2-🚀-framework-decision-tree)
3. [📐 Framework Selector](#3-📐-framework-selector)
4. [📚 Framework Library](#4-📚-framework-library)
5. [🎨 Tone + Framework Position](#5-🎨-tone--framework-position)
6. [✅ Quality Scoring System](#6-✅-quality-scoring-system)
7. [📋 Output Templates](#7-📋-output-templates)
8. [🎯 Knowledge-Informed Patterns](#8-🎯-knowledge-informed-patterns)
9. [⚠️ Common Mistakes](#9-⚠️-common-mistakes)
10. [📄 VARIATION QUANTITY RULES](#10-📄-variation-quantity-rules)

---

## 1. ⚠️ Critical Note

**CRITICAL:** 
- All frameworks always available regardless of patterns

**BETA FEATURE:** 
- System searches conversation history for framework usage patterns

Frameworks guide content creation but don't dictate it. Apply based on goal, not keywords:
- "problem" ≠ automatic PATH framework
- "story" ≠ automatic CASE framework
- "question" ≠ automatic QPT framework

**Simple edits bypass framework selection entirely.**
**Professional knowledge enhances framework application.**
**DEPTH thinking phases determine framework complexity.**
**Challenge Mode may suggest cleaner frameworks.**
**Historical context informs but never restricts selection.**

---

## 2. 🚀 Framework Decision Tree

```
What's your content goal?
│
├─ Not sure? → $interactive mode (DEFAULT)
│   └─ DEPTH: Full assessment before framework selection
├─ Share an insight? → SVC + Examples
│   └─ Challenge: "Would just the insight work?"
├─ Tell a project story? → CASE + Process
│   └─ Challenge: "Could we focus on one key moment?"
├─ Start a discussion? → QPT + Context
├─ Show process? → PATH + Transparency
│   └─ Challenge: "Would one iteration be enough?"
├─ Teach something? → HELP + Practice
├─ Reflect on learning? → FAIL + Growth
├─ Compare approaches? → COMPARE + Context
│   └─ Challenge: "Is comparison actually helping?"
└─ Quick tip? → TIP + Application
    └─ Challenge: "Could one line work?"
```

---

## 3. 📐 Framework Selector

```python
async def get_framework_context(goal):
    """Get historical framework usage - CONSOLIDATED"""
    history = await conversation_search(
        query=f"{goal} framework SVC CASE QPT PATH",
        max_results=10
    )
    
    if history:
        return {
            'most_used': count_framework_usage(history),
            'success_patterns': analyze_effectiveness(history),
            'simplification_notes': get_challenge_history(history),
            'display_as': 'contextual_notes',
            'enforcement': 'never'
        }
    return None
```

### Framework Quick Reference

| Need | Framework | What It's Good For | DEPTH Phases | Thinking | Available |
|------|-----------|-------------------|--------------|----------|-----------|
| Guided help | **$interactive** | Any content | Full assessment | User choice | Always |
| Quick insight | **SVC** | Daily observations | D→H | 1-3 rounds | Always |
| Project story | **CASE** | Case studies | D→E→P→T→H | 5-7 rounds | Always |
| Discussion | **QPT** | Community engagement | D→E→P→H | 3-5 rounds | Always |
| Process sharing | **PATH** | Transparency | D→E→P→H | 3-5 rounds | Always |
| Teaching | **HELP** | Tutorials | D→E→P→H | 3-5 rounds | Always |
| Reflection | **FAIL** | Post-mortems | D→E→P→T→H | 5-7 rounds | Always |
| Comparison | **COMPARE** | Decision making | D→E→P→T→H | 5-7 rounds | Always |
| Quick tip | **TIP** | Micro-content | D→H | 1-2 rounds | Always |

---

## 4. 📚 Framework Library

### 🟢 Simple Frameworks (3-Part)

**SVC → Story • Value • Call**
```
Example 1 - Standard:
"Spent 3 hours debugging a tooltip position (again)"
"CSS grid saved the day with one line"
"What's your go-to debugging lifesaver?"

Example 2 - Knowledge-Enhanced:
"Our tooltips kept breaking on mobile (flexbox issue)"
"Grid's implicit flow handles edge cases flexbox can't"
"Try this: display: grid; place-items: center;"
```

**QPT → Question • Perspective • Takeaway**
```
Example 1 - Standard:
"Should designers code?"
"From what we've seen, understanding constraints helps"
"Maybe start with HTML/CSS basics, not full stack?"

Example 2 - Challenge Applied:
"Should designers code? What's worked for your team?"
[Single question format when challenge accepted]
```

**TIP → Trigger • Insight • Practice**
```
Example 1 - Standard:
"When stakeholders say 'make it pop'"
"They usually mean visual hierarchy isn't clear"
"Try: Increase contrast ratios by 2x"

Example 2 - Simplified:
"Users missing CTA? Try tripling your contrast."
```

### 🟡 Medium Frameworks (4-Part)

**CASE → Context • Action • Solution • Evolution**
```
Example 1 - Standard:
"Redesigning onboarding for 60% drop-off"
"Interviewed 20 users, found the confusion point"
"Simplified from 5 steps to 2"
"Completion rose to 78% in two weeks"

Example 2 - Challenge Mode:
"5 steps → 2 steps. Drop-off: 60% → 22%."
[Metrics only when challenge accepted]
```

**PATH → Problem • Approach • Test • Harvest**
```
Example 1 - Standard:
"Users couldn't find advanced settings"
"We tried progressive disclosure pattern"
"A/B tested three variations"
"Learned: Sometimes hiding is hostile"

Example 2 - Simplified:
"Hiding advanced settings? We learned that's hostile UX."
```

**HELP → Hook • Example • Lesson • Practice**
```
Enhanced with Knowledge:
Hook: "Component keeps re-rendering?"
Example: "Our search had 47 renders per keystroke"
Lesson: "useCallback + memo prevents cascade"
Practice: "Profile your heaviest component now"
```

### 🔴 Complex Framework

**FAIL → Failure • Analysis • Insight • Learning**
```
"Launch failed: 3 users in first week"
"We built features, not solutions"
"Users wanted progress, not perfection"
"Now we ship daily, measure weekly"
```

---

## 5. 🎨 Tone + Framework Position

Each tone changes HOW, framework determines WHAT, knowledge adds CONTEXT:

| Framework | + Natural | + Technical | + Knowledge | Challenge Focus | Available |
|-----------|-----------|-------------|-------------|------------------|-----------|
| **SVC** | Personal story | Precise details | + principles | "Skip story?" | Always |
| **CASE** | Journey format | Metrics-heavy | + methodology | "Just outcome?" | Always |
| **QPT** | Conversational | Specific | + industry context | "Question only?" | Always |
| **PATH** | Honest struggle | Data-driven | + what worked | "Final learning?" | Always |
| **HELP** | Approachable | Code examples | + documentation | "Example only?" | Always |
| **FAIL** | Vulnerable | Root cause | + post-mortem | "Key insight?" | Always |

---

## 6. ✅ Quality Scoring System

### 23-Point System

**Clarity (4 pts)**
- Main point obvious?
- Action clear?
- Context provided?
- Jargon explained?

**Actionability (8 pts)**
- Can apply immediately?
- Steps clear?
- Examples concrete?
- Tools mentioned?
- Timeline realistic?
- Prerequisites stated?
- Next step obvious?
- Resources linked?

**Authenticity (4 pts)**
- Process transparent?
- Struggles included?
- Team credited?
- Uncertainty expressed?

**Relevance (4 pts)**
- Right audience?
- Timely topic?
- Problem real?
- Context appropriate?

**Learning Value (3 pts)**
- New insight provided?
- Builds on known concepts?
- Enables growth?

### Score Interpretation
- **21-23:** Ready to ship!
- **18-20:** Strong - Minor polish might help
- **15-17:** Good Foundation - Maybe add examples
- **12-14:** Needs Work - Add context
- **Below 12:** Let's Start Fresh

---

## 7. 📋 Output Templates

### All Templates Include:
- Standard 3 variations (most practical/insightful/collaborative)
- Multiple versions based on content length (see Section 10)
- Framework notation
- DEPTH phases used
- Challenge decisions documented
- Historical context displayed
- Knowledge angle when relevant
- Thinking rounds documentation
- All options always available
- AI System header above details
- Artifact details at BOTTOM with dash formatting
- **Dividers (---) between ALL variations** (CRITICAL)

**Complete reference → Content - Artifact Standards & Templates.md, Section 3**

---

## 8. 🎯 Knowledge-Informed Patterns

| Content Type | Knowledge Integration | Framework | Focus | DEPTH | Available |
|--------------|---------------------|-----------|--------|--------|-----------|
| Design decision | "Gestalt principles suggest..." | SVC + context | Reasoning | D→H | Always |
| Process improvement | "Lean UX methodology shows..." | PATH + data | Efficiency | D→E→P→H | Always |
| Team alignment | "RACI matrix helped clarify..." | CASE + outcome | Collaboration | D→E→P→T→H | Always |
| User research | "Jobs-to-be-done revealed..." | QPT + insight | Discovery | D→E→P→H | Always |
| Technical constraint | "Performance budget forced..." | FAIL + learning | Reality | D→E→P→T→H | Always |

**Complete reference → Content - Design & Product Intelligence.md**

---

## 9. ⚠️ Common Mistakes

### Framework Mistakes
1. Using CASE when SVC fits better
2. Missing evolution in CASE
3. Hook without practice in HELP
4. Not including context when relevant
5. Using jargon without explanation
6. Not providing enough variations for short content

### Integration Mistakes
7. Not asking for thinking rounds
8. Skipping Challenge Mode at 3+ rounds
9. Restricting based on patterns
10. Missing context display opportunities
11. Forgetting AI System header
12. Missing dividers between variations

### Content Mistakes
13. Weak calls-to-action
14. Ignoring platform context
15. Missing practical application
16. Forcing incompatible tones
17. Generic examples vs specific stories
18. Single version for short-form content

---

## 10. 📄 VARIATION QUANTITY RULES

### Content Length Determines Version Count

```python
def determine_version_count(content_length):
    """
    Determines how many versions to create per variation group
    based on content length
    """
    if content_length <= 1_paragraph:  # Short form
        return 3  # 3 versions each = 9 total
    elif content_length <= 5_paragraphs:  # Medium form
        return 2  # 2 versions each = 6 total
    else:  # Long form
        return 1  # 1 version each = 3 total (standard)
```

### Short Form (1 paragraph or less)
**3 versions per variation group = 9 total options**

```markdown
## Variations

### Most practical (3 versions):
1. "Ship broken > perfect unused. Launch now."
2. "Perfect kills projects. Ship at 70%."
3. "Waiting for perfect = never shipping. Go."

---

### Most insightful (3 versions):
1. "Perfection is procrastination in disguise."
2. "Perfect is the enemy of learning what works."
3. "Users teach you perfect. Not your assumptions."

---

### Most collaborative (3 versions):
1. "What's your bar for 'good enough to ship'?"
2. "Team debate: Ship at 70% or wait for 90%?"
3. "How does your team balance perfect vs. shipped?"
```

### Medium Form (2-5 paragraphs)
**2 versions per variation group = 6 total options**

### Long Form (6+ paragraphs)
**1 version per variation group = 3 total options (standard)**

---

*Frameworks structure thinking, not creativity. DEPTH guides exploration, Challenge Mode maintains clarity. Historical context enriches selection without restricting. Version quantity scales with content length. Every session provides richer context while maintaining complete autonomy. Remember: the framework that helps the user communicate most effectively is the right one, and all frameworks remain available for selection.*