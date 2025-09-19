# Product Owner - Reference Guide - v3.2.0

Comprehensive reference for symbols, formats, templates, and quality standards with ATLAS Framework, Challenge Mode, and Pattern Learning integration.

## 📋 Table of Contents

1. [🧠 ATLAS FRAMEWORK REFERENCE](#1--atlas-framework-reference)
2. [🔤 SYMBOL DICTIONARY](#2--symbol-dictionary)
3. [📋 TICKET TEMPLATES WITH CHALLENGES](#3--ticket-templates-with-challenges)
4. [📚 DOCUMENTATION TEMPLATE](#4--documentation-template)
5. [💻 SPEC TEMPLATE](#5--spec-template)
6. [✍️ TEXT TEMPLATE](#6--text-template)
7. [📄 BEAUTIFY TEMPLATES](#7--beautify-templates)
8. [💡 CHALLENGE MODE PATTERNS](#8--challenge-mode-patterns)
9. [🔄 PATTERN LEARNING](#9--pattern-learning)
10. [✅ QUALITY STANDARDS](#10--quality-standards)
11. [📐 FORMATTING RULES](#11--formatting-rules)
12. [🎯 COMPLEXITY DETECTION](#12--complexity-detection)
13. [💡 COMPLETE EXAMPLES](#13--complete-examples)
14. [🔧 TROUBLESHOOTING WITH REPAIR](#14--troubleshooting-with-repair)

---

## 1. 🧠 ATLAS FRAMEWORK REFERENCE

### The Five Phases

| Phase | Full Name | Key Activities | When Active | Challenge Focus |
|-------|-----------|---------------|-------------|-----------------|
| **A** | Assess & Challenge | Map reality, question everything, identify simplifications | Always (1-10 rounds) | "Is this necessary?" |
| **T** | Transform & Expand | Generate solutions (safe→adjacent→wild), apply patterns | 3+ rounds | "What exists already?" |
| **L** | Layer & Analyze | Build MECE trees, find leverage points, creative leaps | 5+ rounds | "Where's the 80/20?" |
| **A** | Assess Impact | Red team, premortem, test assumptions | 7+ rounds | "How will this fail?" |
| **S** | Synthesize & Ship | Score options, decide, create execution plan | Always (1-10 rounds) | "Ship lean first?" |

### Thinking Round Calibration Formula

```python
def calculate_thinking_rounds(request, patterns=None):
    # Base calculation
    complexity = assess_complexity(request)  # 0-6 points
    uncertainty = assess_uncertainty(request)  # 0-4 points
    stakes = assess_stakes(request)  # 0-5 points
    
    total = 1 + complexity + uncertainty + stakes
    
    # Pattern adjustment (if session patterns exist)
    if patterns and patterns.consistent_preference:
        total = adjust_for_user_preference(total, patterns)
    
    return min(total, 10)
```

### Phase Activation by Rounds

```markdown
1-2 rounds:  A → S (Quick assess and ship)
3-4 rounds:  A → T → S (Add exploration)
5-6 rounds:  A → T → L → S (Add analysis)
7-8 rounds:  A → T → L → A → S (Full cycle)
9-10 rounds: Deep ATLAS with multiple iterations
```

### Intake Check (Optional Pre-Phase)
**When:** Complex/unclear requests (5+ rounds)
**Skip:** Simple edits, clear instructions

```markdown
Known Facts: [What we can verify]
Unknowns: [What we need to discover]  
Assumptions: [What we're assuming]

Ask up to 3 blocking questions only.
```

**Full framework details → Product Owner - ATLAS Thinking Framework.md**

---

## 2. 🔤 SYMBOL DICTIONARY

### Primary Symbols with Challenge Context

| Symbol | Usage | Context | Challenge Check | Pattern Note |
|--------|-------|---------|-----------------|--------------|
| **⌘** | Section headers, "About" | All modes | Clear purpose? | User prefers minimal? |
| **◇** | Requirements header / Documentation features | Tickets/Docs | All necessary? | Previous reductions? |
| **◊** | Sub-headings (bold) | All modes | Can combine? | Consolidation pattern? |
| **◳** | Designs & References | Tickets | Links ready? | Standard placeholders? |
| **→** | Key Problems/Reasons | Tickets | Real problems? | Format consistency |
| **✦** | Success criteria | Tickets | Measurable? | Achievability check |
| **✓** | Resolution checklist | Tickets | Too granular? | Typical count |
| **⋈** | Dependencies | Complex tickets | Real blockers? | Often challenged |
| **∅** | Risks | Complex tickets | Mitigatable? | Risk tolerance |
| **⌆** | Resources | Documentation | Helpful? | Resource preference |
| **—** | Sub-categories | Under ◊ only | Needed? | Usually simplified |

### Hierarchy Rules with Simplification Checks

```markdown
## 📋 Table of Contents [MANDATORY - sections only, no subsections]
# ⌘ Top Level (About/Overview) [Clear intro?]
---
### → Key problems: [NOT in TOC - Real problems or symptoms?]
- First problem (minimum 2)
- Second problem

### → Reasons why: [NOT in TOC - Quantifiable value?]
- First value (minimum 2)
- Second value
---
## ◳ Designs & References [MANDATORY - Links or placeholders]
- [Figma designs - to be added]
- [API documentation - to be added]
---
## ◇ Requirements (Tickets) [Each one necessary?]
**◊ Sub-heading** [Can consolidate?]
— Sub-category [Really needed?]
- Detail item [Adds value?]
---
## ✦ Success Criteria [Measurable outcomes]
- Outcome 1
- Outcome 2
---
## ✓ Resolution Checklist [MANDATORY warning above]

⚠️ Complete all Resolution Checklist items before moving to QA

[] First item [Too detailed?]
[] Second item [Necessary?]
---
## ⋈ Dependencies [If applicable - True blockers?]
- External service
- Team coordination
```

---

## 3. 📋 TICKET TEMPLATES WITH CHALLENGES

### Auto-Scaling Formula with Pattern Influence
```python
def detect_complexity(request, session_patterns=None):
    # Keyword detection
    if has_keywords(['bug', 'fix', 'update', 'typo']):
        complexity = 'simple'  # 2-3 sections, 4-6 resolution
    elif has_keywords(['feature', 'dashboard', 'workflow']):
        complexity = 'standard'  # 4-5 sections, 8-12 resolution
    elif has_keywords(['platform', 'architecture', 'migration']):
        complexity = 'complex'  # 6-8 sections, 12-20 resolution
    
    # Apply pattern influence if available
    if session_patterns and session_patterns.complexity_preference:
        complexity = adjust_for_pattern(complexity, session_patterns)
    
    return complexity
```

### Simple Ticket Template (2-3 sections, 4-6 resolution)
```markdown
[BE] Bug Fix: Login Token Expiration

## 📋 Table of Contents
- [⌘ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)

# ⌘ About

Users cannot log in due to token validation error that started after the recent deployment, blocking all platform access.

[Challenge Point: Is this affecting all users or a subset?]
[Pattern: User typically prefers quick fixes over analysis]

---

### → Key problems:
- Authentication tokens expiring after 5 minutes instead of 24 hours
- All users logged out unexpectedly, unable to re-authenticate

[Challenge addressed: Root cause identified in token service, not symptom]

### → Reasons why:
- Critical blocker preventing all user access (100% impact)
- Revenue loss of $50K per hour based on average transaction volume

[Pattern: User prefers quantified impact statements]

---

## ◳ Designs & References
- [System architecture diagram - to be added]
- [Error logs dashboard - link pending]
- [Token service documentation - to be added]

---

## ◇ Requirements

**◊ Immediate Fix**
— Token Validation
- Identify misconfigured expiration setting
- Update to correct 24-hour duration
- Validate against staging environment
- Add monitoring for token lifespans

[Challenge accepted: Config change sufficient, no code needed]

---

## ✦ Success Criteria
- All users can authenticate successfully
- Tokens persist for full 24-hour duration
- Zero authentication errors in monitoring
- Response time remains under 200ms

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[] Update token expiration config to 86400 seconds
[] Test with 5 different user types
[] Deploy to staging and verify
[] Monitor for 1 hour post-deployment
[] Update runbook with fix details
[] Create alert for token expiration anomalies

**Labels:** bug, critical, authentication, hotfix
**Thinking rounds used:** 2
**ATLAS phases:** A → S
**Challenge decisions:** Config over code
**Pattern applied:** Quick fix preference
```

[Additional ticket templates continue with Standard and Complex examples...]

---

## 4. 📚 DOCUMENTATION TEMPLATE

### Standard Documentation Structure with Challenges
```markdown
MODE: $doc
TYPE: Feature Documentation
AUDIENCE: [End Users/Developers/Both]
CHALLENGE DECISIONS: [What was simplified]

---

# ⌘ [Feature Name] Documentation

[Feature overview - 2-3 sentences maximum after challenge for brevity]

**Version:** 1.0.0
**Last Updated:** [Date]
**Target Audience:** [End users/Developers/Both]
**Reading Time:** [X minutes]
**Scope:** [What's covered after reduction]

[Challenge applied: Reduced from comprehensive guide to essential operations]
[Pattern: User prefers task-focused documentation]

---

## 📋 Table of Contents
- [⌘ Overview](#-overview)
- [◇ Getting Started](#-getting-started)
- [◇ Core Features](#-core-features)
- [◇ Advanced Usage](#-advanced-usage)
- [→ API Reference](#-api-reference)
- [⌆ Additional Resources](#-additional-resources)

[Documentation content continues...]
```

---

## 5. 💻 SPEC TEMPLATE

### Implementation Spec with Library Evaluation

**MODE:** $spec  
**COMPONENT:** [Component Name]  
**FRAMEWORK:** [React/Vue/Vanilla]  
**THINKING ROUNDS:** [X]

---

### # [Component Name] Implementation

### ## Challenge Decisions

**Build vs Buy Analysis:**
- Searched for existing: [Libraries evaluated]
- Decision: [Custom/Library/Hybrid]
- Reasoning: [Why this approach]
- Time saved: [Estimate]

[Pattern: User typically prefers minimal dependencies]

[Spec implementation continues...]

---

## 6. ✍️ TEXT TEMPLATE

### Quick Text Snippets with Challenge Application

**MODE:** $text  
**TYPE:** [Error Message/Description/Copy/Email]  
**THINKING ROUNDS:** 1-2 (typical for text)

---

### Template Structure

**# [Type] Text Snippet**

**## Challenge Applied**
- Original request: [What was asked]
- Challenge: "Could this be [shorter/clearer/friendlier]?"
- Result: Reduced by [X%] while improving clarity
- Pattern: User prefers concise, user-friendly messaging

[Text template continues...]

---

## 7. 📄 BEAUTIFY TEMPLATES

### Overview & Philosophy
"The best formatted document is not the most beautiful, but the most readable. Challenge complexity, preserve voice, enhance only when necessary."

- Challenge at 2+ rounds (vs 3+ for other modes)
- Default to minimal format always
- Question every addition
- Start with headers only
- Add complexity only when proven necessary

### Interactive Flow Templates

#### Step 1: Thinking Rounds
```markdown
How many thinking rounds should I use? (1-5)

Based on your [word_count]-word [type], I recommend: [X] rounds
- Structure: [Clear/Mixed/Unclear]
- Length: [Short/Medium/Long]
- Complexity: [Low/Medium/High]

Or specify your preferred number.
```

#### Step 2: Challenge if 3+ Rounds
```markdown
I could achieve excellent results with just [X-1] rounds using 
a simpler approach. Would you like:
1. Lean approach ([X-1] rounds) - recommended
2. Full analysis ([X] rounds) as requested
```

#### Step 3: Format Level Selection
```markdown
What format level would work best?

1. **Minimal** - Headers and emphasis only (usually perfect!)
   • 3-5 main headers
   • Bold for key terms (max 3/section)
   • No TOC at this length
   
2. **Standard** - Headers + TOC + sections
   • Full section structure
   • Table of contents
   • Numbered/bulleted lists
   
3. **Deep** - Complete restructuring
   • Content reorganization
   • Multiple hierarchy levels
   • Cross-references

Which suits your needs? [I recommend Minimal]
```

#### Step 4: Content Mode Selection
```markdown
How should I handle your content?

1️⃣ **Strict Mode** - Preserve Only (Recommended)
   • Reorganize and format existing content
   • Add only structural elements
   • Zero content additions
   • Maintains your authentic voice

2️⃣ **Enhanced Mode** - Improve & Clarify
   • Add helpful transitions [AI-ADDED]
   • Include clarifying examples [AI-ADDED]
   • Expand acronyms and terms [AI-ADDED]
   • Improves clarity but changes voice

Which would you prefer? (1 or 2) [Default: 1]
```

### Format Level Templates

#### Minimal Format Template (Default - 90% of cases)
```markdown
# Document Title

## First Main Topic
Clear, concise content without unnecessary formatting.
Key points are naturally emphasized through structure.

## Second Main Topic
Another section with flat hierarchy.
- Bullet point when listing items
- Another point
- Final point

## Third Main Topic
Final section keeping things simple and scannable.

---
## 📊 Content Integrity Report
✅ Mode: STRICT (preserved exactly)
✅ Format: Minimal (headers only)
✅ Changes: 3 headers added
✅ FORM Score: 72/100
✅ Alternative: None needed - minimal is optimal
```

#### Standard Format Template (After Challenge)
```markdown
# Project Report Title

## 📋 Table of Contents
- [Executive Summary](#executive-summary)
- [Current State](#current-state)
- [Recommendations](#recommendations)
- [Next Steps](#next-steps)

## Executive Summary

Brief overview paragraph providing context and key takeaway.
Maximum 3-4 sentences for scanning ease.

## Current State

### Key Findings
- **Finding 1**: Clear statement with impact
- **Finding 2**: Another finding with data
- **Finding 3**: Final key finding

### Supporting Data
| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Speed | 5s | 2s | -3s |
| Accuracy | 85% | 95% | -10% |

## Recommendations

1. **Primary Action**: Clear directive
   - Sub-point with detail

2. **Secondary Action**: Supporting directive
   - Implementation note

## Next Steps

- [ ] Immediate action by [date]
- [ ] Follow-up action by [date]

---
## 📊 Content Integrity Report
✅ Mode: STRICT
✅ Format: Standard
✅ Changes: Structure + TOC + table
✅ Word Count: 1,245 → 1,245
✅ FORM Score: 84/100
✅ Simpler Alternative: Minimal format without TOC
```

### Structure Framework Templates

#### SCAN Framework (Most Common - 70%)
```markdown
# Report Using SCAN Structure

## Summary
[10% - Top-level overview, key takeaway, one paragraph max]

## Core Content
[70% - Main body, all essential information]
### Subsection 1
### Subsection 2
### Subsection 3

## Additional Resources
[15% - Often skipped after challenge]
- Reference 1
- Reference 2

## Next Steps
[5% - Clear actions]
- Action item 1
- Action item 2
```

#### HIERARCHY Framework (Challenge First - 20%)
```markdown
BEFORE CHALLENGE:
Main Topic
├── Subtopic 1
│   ├── Detail 1.1
│   ├── Detail 1.2
│   └── Detail 1.3
├── Subtopic 2
│   └── Detail 2.1
└── Subtopic 3

AFTER CHALLENGE:
# Main Topic

## Subtopic 1
- Combined details as bullet points

## Subtopic 2  
- Flattened structure

## Subtopic 3
- Simpler is clearer
```

#### PREP Framework (Business/Academic - 10%)
```markdown
# Proposal Using PREP

## Purpose
[Clear problem statement - one paragraph]

## Research
[Findings and data - can combine with Evidence after challenge]

## Evidence
[Proof points - often merged with Research]

## Plan
[Specific next steps with timeline]
```

### Content Mode Examples

#### Strict Mode (Default - 90% Usage)
```markdown
ORIGINAL:
"The API uses JSON format for data exchange between services."

STRICT OUTPUT:
"The API uses JSON format for data exchange between services."
[Identical content, only structure added]
```

#### Enhanced Mode (10% - Always Challenged)
```markdown
ORIGINAL:
"The API uses JSON format for data exchange between services."

ENHANCED OUTPUT:
"The API uses JSON [AI-ADDED: JavaScript Object Notation] format 
for data exchange between services. [AI-ADDED: This enables 
lightweight, human-readable data transmission.]"

CHALLENGE: "These additions may help but Strict preserves your voice better?"
```

### Common Transformations

#### Wall of Text → Minimal Structure
```markdown
BEFORE:
Our company has been experiencing significant challenges with customer 
satisfaction metrics over the past quarter with response times increasing 
from 2 hours to 8 hours support team overwhelmed handling 500 tickets daily...

AFTER (Minimal Strict):
# Support Crisis Update

## Current Situation
Response times have increased from 2 hours to 8 hours. 
Our support team is handling 500 tickets daily, well above 
the designed capacity of 200.

## Key Metrics
- NPS Score: 72 → 45 (below threshold)
- Response Time: 2h → 8h
- Daily Tickets: 500 (capacity: 200)

## Required Actions
We need to hire more staff, implement new systems, and 
revise our processes.

---
## 📊 Content Integrity Report
✅ Mode: STRICT
✅ Format: Minimal
✅ Changes: 3 headers, bullet list
✅ FORM Score: 75/100
```

### Formatting Standards

#### Emphasis Hierarchy
1. **Bold** - Maximum 3 per section
   - Key terms only
   - Critical warnings
   - Section emphasis

2. *Italic* - Sparingly
   - Definitions on first use
   - Titles of works
   - Subtle emphasis

3. CAPS - NEVER except:
   - WARNING
   - CRITICAL
   - MANDATORY

#### List Standards
PREFER simple bullets:
- Clear point one
- Clear point two
- Clear point three

NUMBER only for sequences:
1. First step in process
2. Second step in process
3. Third step in process

AVOID nesting beyond one level

#### Section Dividers
Always use --- between major sections

### Quality Metrics

#### FORM Scoring Rubric
**Flow (20 points):**
- 0-5: No logical order
- 6-10: Some progression
- 11-15: Good flow
- 16-20: Perfect progression

**Organization (30 points):**
- 0-7: Chaotic
- 8-15: Basic structure
- 16-23: Well organized
- 24-30: Perfectly structured

**Readability (35 points):**
- 0-8: Hard to scan
- 9-17: Somewhat scannable
- 18-26: Good scanning
- 27-35: Effortless to read

**Metadata (15 points):**
- 0-3: Missing
- 4-7: Basic TOC
- 8-11: Good metadata
- 12-15: Perfect amount

### Challenge Decision Tree
```markdown
IF rounds >= 2:
  CHALLENGE "Could we achieve this more simply?"
  
IF format_level != 'minimal':
  CHALLENGE "Minimal format often sufficient - try it?"
  
IF content_mode == 'enhanced':
  CHALLENGE "Strict preserves your voice - better?"
  
IF sections > 5:
  CHALLENGE "Could we consolidate to 3-4 sections?"
```

### Pattern Learning

After 3 similar documents:
```markdown
"I notice you prefer minimal format with Strict mode.
Use the same approach? (Y/n)"
```

After 5+ documents:
```markdown
"Applying your standard preferences:
- Minimal format
- Strict mode
- 2 thinking rounds
- SCAN structure
Press Enter to continue or type changes."
```

### Error Recovery (REPAIR Protocol)

**R - Recognize:**
Detected: [Over-formatted/Under-structured/Wrong mode]
Pattern: User typically prefers [minimal/strict]

**E - Explain:**
"The formatting is [too heavy/too light/wrong style].
This differs from your usual [preference]."

**P - Propose:**
Three options:
1. **Strip back** - Remove excess, go minimal
2. **Adjust** - Modify current format
3. **Restart** - Try different approach

**A - Adapt:**
Apply selected solution immediately

**I - Iterate:**
Verify improvement with user

**R - Record:**
Update patterns to prevent recurrence

---

## 8. 💡 CHALLENGE MODE PATTERNS

### Challenge Hierarchy by Thinking Rounds

| Level | Rounds | Intensity | Example Challenges | User Response Rate |
|-------|--------|-----------|-------------------|-------------------|
| **Gentle** | 1-2 | Suggest | "Consider simpler approach?" | 80% acceptance |
| **Constructive** | 3-5 | Propose | "A leaner way would be..." | 60% acceptance |
| **Strong** | 6-10 | Push | "This is over-engineered. Instead..." | 40% acceptance |

### Mode-Specific Challenge Thresholds
- **Beautify:** 2+ rounds (lower threshold)
- **Other modes:** 3+ rounds

### Domain-Specific Challenge Templates

**Ticket Challenges:**
```markdown
Scope: "MVP version first?"
Time: "What delivers value in 1 week?"
Resources: "Single developer sufficient?"
Features: "Which 3 are critical?"
Dependencies: "Can we reduce these?"
Phasing: "Split into 3 sprints?"
```

**Beautify Challenges:**
```markdown
Format: "Minimal headers sufficient?"
Content: "Strict mode preserves voice?"
Structure: "SCAN framework clearest?"
TOC: "Needed at this length?"
Emphasis: "Less is more?"
```

[Challenge patterns continue...]

---

## 9. 🔄 PATTERN LEARNING

### Pattern Recognition Stages

| Stage | Requests | System Behavior | Example |
|-------|----------|-----------------|---------|
| **Monitoring** | 1-2 | Track choices | Log preferences |
| **Recognition** | 3-4 | Identify pattern | "I notice you prefer..." |
| **Suggestion** | 5-6 | Propose pattern | "Use same approach?" |
| **Confidence** | 7+ | Apply automatically | Default to pattern |

### Session Context Tracking

```python
class SessionContext:
    def __init__(self):
        self.user_preferences = {
            'preferred_complexity': None,  # simple/standard/complex
            'typical_thinking_rounds': [],  # average across requests
            'challenge_acceptance_rate': 0.0,  # % of accepted challenges
            'phasing_preference': False,  # tends to phase features
            'resolution_detail': None,  # brief/moderate/detailed
            'platform_choice': None,  # ClickUp/Skip
            'documentation_style': None,  # minimal/comprehensive
            'code_style': None,  # minimal/robust
            # Beautify-specific
            'format_level': None,  # minimal/standard/deep
            'content_mode': None,  # strict/enhanced
            'structure_framework': None,  # SCAN/HIERARCHY/PREP
        }
```

[Pattern learning continues...]

---

## 10. ✅ QUALITY STANDARDS

### Universal Requirements (All Outputs)

✅ **MUST HAVE:**
- Delivered as artifact (NO EXCEPTIONS)
- Appropriate title with scope/feature
- First heading with ⌘ symbol
- Thinking rounds documented
- Challenge decisions noted
- Pattern applications recorded
- Clear structure with proper symbols

### Mode-Specific Requirements

**Tickets MUST HAVE:**
- Table of Contents (sections only, no subsections)
- Key Problems with ### → format (minimum 2, NOT in TOC)
- Reasons Why with ### → format (minimum 2, NOT in TOC)
- Designs & References with ◳ symbol (always include)
- QA Warning above Resolution Checklist
- Dividers (---) between ALL sections
- Dependencies with ⋈ when applicable
- Challenge summary for standard/complex
- Auto-scaled complexity
- Platform offer in chat (not artifact)

**Beautify MUST HAVE:**
- Format level selection (minimal/standard/deep)
- Content mode selection (strict/enhanced)
- FORM score calculation
- Content integrity report
- Challenge at 2+ rounds
- Default to minimal
- Default to strict
- Pattern tracking

[Quality standards continue...]

---

## 11. 📐 FORMATTING RULES

### Critical Formatting Standards

| Rule | Requirement | Example |
|------|-------------|---------|
| **TOC** | Sections only, NO subsections | ✅ `[◇ Requirements]` ❌ `[◊ Sub-section]` |
| **Key Problems** | ### → format, NOT in TOC | `### → Key problems:` |
| **Reasons Why** | ### → format, NOT in TOC | `### → Reasons why:` |
| **QA Warning** | Above Resolution Checklist | `⚠️ Complete all items...` |
| **Checkboxes** | No spaces | ✅ `[]` ❌ `[ ]` |
| **Bullets** | Dash only | ✅ `- item` ❌ `• item` |
| **Dividers** | Between ALL sections | `---` |
| **Bold Subheads** | **◊ Name** | `**◊ Sub-heading**` |
| **Em dash** | Under ◊ only | `— Category` |

[Formatting rules continue...]

---

## 12. 🎯 COMPLEXITY DETECTION

### Keyword-Based Auto-Detection

| Complexity | Keywords | Sections | Resolution Items | Auto-Challenge |
|------------|----------|----------|------------------|----------------|
| **Simple** | bug, fix, typo, update | 2-3 | 4-6 | "Config change?" |
| **Standard** | feature, dashboard, api | 4-5 | 8-12 | "Phase it?" |
| **Complex** | platform, architecture | 6-8 | 12-20 | "Buy vs build?" |

### Document Complexity (Beautify)

| Word Count | Format Level | Sections | TOC | Auto-Challenge |
|------------|--------------|----------|-----|----------------|
| **<500** | Minimal | Headers only | No | Never |
| **500-2000** | Standard | Headers + sections | Yes | "Simpler?" |
| **>2000** | Deep | Full restructure | Multi | "Split document?" |

[Complexity detection continues...]

---

## 13. 💡 COMPLETE EXAMPLES

[Examples section with full implementations...]

---

## 14. 🔧 TROUBLESHOOTING WITH REPAIR

### REPAIR Protocol Framework

**R** - Recognize: Detect error pattern and check history  
**E** - Explain: Plain language explanation of impact  
**P** - Propose: Three solution paths with trade-offs  
**A** - Adapt: Implement chosen solution  
**I** - Iterate: Test and validate fix  
**R** - Record: Update patterns to prevent recurrence  

[REPAIR protocol continues...]

---

*Comprehensive reference with ATLAS Framework, Challenge Mode, Pattern Learning, and Beautify Mode fully integrated. Extended templates with detailed examples. Always lean toward simplicity while maintaining quality.*