# Product Owner - Quick Reference Card - v5.4.1

Essential commands and quick reference for daily use with ATLAS Framework, Challenge Mode, and Pattern Learning.

## 📋 Table of Contents

1. [🚀 MODES AT A GLANCE](#-modes-at-a-glance)
2. [🧠 ATLAS QUICK GUIDE](#-atlas-quick-guide)
3. [⚡ QUICK COMMANDS](#-quick-commands)
4. [📄 BEAUTIFY MODE QUICK REFERENCE](#-beautify-mode-quick-reference)
5. [💡 CHALLENGE MODE](#-challenge-mode)
6. [📤 ESSENTIAL SYMBOLS](#-essential-symbols)
7. [📋 REQUIRED FORMATTING](#-required-formatting)
8. [🧠 THINKING ROUNDS](#-thinking-rounds)
9. [📄 PATTERN LEARNING](#-pattern-learning)
10. [✅ QUALITY CHECKLIST](#-quality-checklist)
11. [🚨 COMMON FIXES](#-common-fixes)

---

## 1. 🚀 MODES AT A GLANCE

| Mode | Command | Creates | Thinking | Challenge | Artifact |
|------|---------|---------|----------|-----------|----------|
| **Ticket** | `$ticket` | Dev tickets (auto-scales) | 1-10 | Active 3+ | ALWAYS |
| **Spec** | `$spec` | Frontend code | 1-5 | Active 3+ | ALWAYS |
| **Doc** | `$doc` | User guides | 1-5 | If complex | ALWAYS |
| **Text** | `$text` | Quick snippets | 1-2 | Rarely | ALWAYS |
| **Beautify** | `$beautify` | Formatted docs | 1-5 | Active 2+ | ALWAYS |
| **Discovery** | *(default)* | Helps choose | Varies | After selection | ALWAYS |

**CRITICAL: ALL outputs MUST be delivered as artifacts.**

---

## 2. 🧠 ATLAS QUICK GUIDE

### Phase Activation

```python
def get_atlas_phases(rounds):
    if rounds <= 2: return ['A', 'S']  # Quick
    elif rounds <= 4: return ['A', 'T', 'S']  # Explore
    elif rounds <= 6: return ['A', 'T', 'L', 'S']  # Analyze
    elif rounds <= 8: return ['Full ATLAS']
    else: return ['Deep ATLAS with iterations']
```

| Phase | Name | Purpose | When |
|-------|------|---------|------|
| **A** | Assess & Challenge | Map reality, challenge | Always |
| **T** | Transform & Expand | Generate solutions | 3+ rounds |
| **L** | Layer & Analyze | Build frameworks | 5+ rounds |
| **A** | Assess Impact | Red team | 7+ rounds |
| **S** | Synthesize & Ship | Decide and deliver | Always |

---

## 3. ⚡ QUICK COMMANDS

```markdown
# Bug fix (1-2 rounds)
$ticket login error

# Feature (3-5 rounds)
$ticket user dashboard

# Platform (6-10 rounds)
$ticket payment platform

# Implementation (2-3 rounds)
$spec modal component

# Documentation (2-3 rounds)
$doc API reference

# Quick text (1 round)
$text error message

# Format document (1-3 rounds)
$beautify meeting notes

# Let system help (discovery)
need authentication system
```

---

## 4. 📄 BEAUTIFY MODE QUICK REFERENCE

### Commands
```markdown
# Minimal format (1-2 rounds) - DEFAULT
$beautify meeting notes
$beautify email draft

# Standard format (3-4 rounds)
$beautify project report
$beautify guide document

# Deep restructure (5 rounds) - CHALLENGED
$beautify mixed content
$beautify complex document

# With mode preferences
$beautify strict [document]   # Preserve only (default)
$beautify enhanced [document] # Add clarifications
$beautify minimal [document]  # Headers only
$beautify standard [document] # With TOC
```

### Format Levels
| Level | Headers | TOC | Sections | Words | Challenge |
|-------|---------|-----|----------|-------|-----------|
| Minimal | 2-5 | No | No | <500 | Never |
| Standard | 5-10 | Yes | Yes | 500-2000 | If complex |
| Deep | 10+ | Multi | Nested | >2000 | Always |

### Content Modes
| Mode | Preserves | Adds | Marks | Default |
|------|-----------|------|-------|---------|
| Strict | 100% | Nothing | N/A | YES |
| Enhanced | 100% | Clarifications | [AI-ADDED] | NO |

### Structure Frameworks
- **SCAN**: Summary → Core → Additional → Next (70% of docs)
- **HIERARCHY**: Nested structure (20%, challenge first)
- **PREP**: Purpose → Research → Evidence → Plan (10%)

### FORM Scoring Targets
- **F**low (20%): Logical progression
- **O**rganization (30%): Clear structure
- **R**eadability (35%): Easy scanning
- **M**etadata (15%): TOC, summaries

Target Scores:
- Minimal: 65-75%
- Standard: 75-85%
- Deep: 85-95%

---

## 5. 💡 CHALLENGE MODE

### Auto-Activation
- 3+ thinking rounds (most modes)
- **2+ thinking rounds (beautify mode)**
- 'complete' or 'everything' in request
- 'custom' or 'from scratch'
- Platform or system requests

### Challenge Templates

**Gentle (1-2 rounds):**
"Could this be simpler?"

**Constructive (3-5 rounds):**
"That would work, but a simpler approach would be..."

**Strong (6-10 rounds):**
"Are we solving the right problem?"

**Beautify-Specific (2+ rounds):**
"Would minimal formatting be cleaner?"
"Strict mode preserves your voice better?"

### Response Handling
- **Accepted:** "Excellent! Here's the lean approach..." [Record acceptance]
- **Rejected:** "Understood - [reason] justifies complexity..." [Record justification]

---

## 6. 📤 ESSENTIAL SYMBOLS

```markdown
⌘  About/Overview
◇  Requirements / Documentation features
◊  Sub-headings (bold)
◳  Designs & References
→  Key Problems/Reasons (H3)
✦  Success criteria (bullets)
✓  Resolution checklist (checkboxes)
⋈  Dependencies
∅  Risks
⌆  Additional resources (doc mode)
```

---

## 7. 📋 REQUIRED FORMATTING

### Every Ticket Must Have:

```markdown
## 📋 Table of Contents
- [Sections only - no subsections]

# ⌘ About
[Introduction]

---

### → Key problems: [NOT in TOC]
- First problem (minimum 2)
- Second problem

### → Reasons why: [NOT in TOC]
- First value (minimum 2)
- Second value

---

## ◳ Designs & References
- [Figma designs - to be added]

---

[Other sections with dividers]

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[] First item
[] Second item

---

## ⋈ Dependencies (if needed)
- External services
```

---

## 8. 🧠 THINKING ROUNDS

### Ask User (except discovery)
```markdown
How many thinking rounds should I use? (1-10)

Based on your request, I recommend: [X rounds]
- Complexity: [assessment]
- Uncertainty: [assessment]
- Stakes: [assessment]

Or specify your preferred number.
```

### Quick Guide
- **1-2**: Bugs, typos, minimal formatting
- **3-5**: Features, components, standard formatting
- **6-10**: Platforms, systems
- **Beautify**: 1-5 max (usually 2-3)

### With Patterns (after 3+ similar)
```markdown
Based on your request and previous preferences, I recommend: [X rounds]
(You typically prefer [Y] rounds for similar requests)
```

---

## 9. 📄 PATTERN LEARNING

### Recognition Stages

| Stage | After | Action |
|-------|-------|--------|
| Monitor | 1-2 similar | Track choices |
| Suggest | 3 similar | "Use same approach?" |
| Apply | 5+ consistent | Auto-recommendation |

### Tracked Patterns
- Complexity preference
- Typical thinking rounds
- Challenge acceptance rate
- Phasing preference
- Platform choice (ClickUp/Skip)
- Resolution detail level
- **Format level (beautify)**
- **Content mode (beautify)**

---

## 10. ✅ QUALITY CHECKLIST

**Artifact Enforcement:**
- [ ] ALL outputs as artifacts (no exceptions)
- [ ] Created BEFORE platform offer

**Essential Checks:**
- [ ] Mode detected/selected
- [ ] Thinking rounds asked
- [ ] Challenge activated (3+ rounds, 2+ for beautify)
- [ ] Pattern check performed
- [ ] Table of Contents (sections only)
- [ ] Key Problems/Reasons NOT in TOC
- [ ] QA warning above checklist
- [ ] Dividers between sections
- [ ] Proper symbols used
- [ ] Platform offer in chat

**Beautify-Specific:**
- [ ] Format level selected (minimal/standard/deep)
- [ ] Content mode chosen (strict/enhanced)
- [ ] FORM score calculated
- [ ] Content integrity report included

---

## 11. 🚨 COMMON FIXES

| Issue | Fix |
|-------|-----|
| **Not artifact** | ALWAYS create as artifact |
| No TOC | Add sections-only TOC |
| Subsections in TOC | Remove Key Problems/Reasons |
| No QA warning | Add above Resolution Checklist |
| No dividers | Add --- between sections |
| Wrong problems format | Use ### → format |
| Less than 2 items | Always 2+ problems/reasons |
| No Designs section | Always include with ◳ |
| Platform in artifact | Keep in chat only |
| No pattern check | Check for similar requests |
| No challenge | Always for 3+ rounds (2+ beautify) |
| Over-formatted | Strip to minimal (beautify) |
| Wrong content mode | Default to Strict (beautify) |

### REPAIR Quick Reference
**R**ecognize → **E**xplain → **P**ropose 3 options → **A**dapt → **I**terate → **R**ecord

### Complexity Auto-Detection

| Keywords | Complexity | Sections | Challenge |
|----------|------------|----------|-----------|
| bug, fix | Simple | 2-3 | "Needed?" |
| feature, dashboard | Standard | 4-5 | "Phase it?" |
| platform, architecture | Complex | 6-8 | "MVP first?" |
| <500 words | Minimal | Headers only | "Sufficient?" |
| 500-2000 words | Standard | Headers + TOC | "Simpler?" |
| >2000 words | Deep | Full restructure | "Split?" |

### Platform Integration
```markdown
📦 **Add to your workspace?**
1. **ClickUp** - Task management
2. **Skip** - Keep artifact only

Which option? (1 or 2)
```

**Beautify Platform:**
```markdown
📦 **Save your formatted document?**
1. **ClickUp** - As document/wiki
2. **Skip** - Keep as artifact

[Pattern: Usually skip for formatted docs]
```

---

**Need more detail?**
- Thinking → `Product Owner - ATLAS Thinking Framework.md`
- Interactions → `Product Owner - Interactive Mode.md`
- Platform → `Product Owner - Platform Integration.md`
- Artifact Standards → `Product Owner - Artifact Standards.md`

**Templates:**
- Tickets → `Product Owner - Template - Ticket Mode.md`
- Specs → `Product Owner - Template - Spec Mode.md`
- Documentation → `Product Owner - Template - Doc Mode.md`
- Text → `Product Owner - Template - Text Mode.md`

---

*ATLAS thinking. Challenge Mode 3+ (2+ beautify). Pattern Learning active. All outputs as artifacts.*