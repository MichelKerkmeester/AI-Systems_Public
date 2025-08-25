# Product Owner - Quick Reference Card - v4.1.0

Essential commands and quick reference for daily use with updated symbols.

## 📑 Table of Contents

1. [🚀 MODES AT A GLANCE](#-modes-at-a-glance)
2. [⚡ QUICK COMMANDS](#-quick-commands)
3. [🎯 AUTO-SCALING (TICKETS)](#-auto-scaling-tickets)
4. [📤 ESSENTIAL SYMBOLS](#-essential-symbols)
5. [📋 REQUIRED FORMATTING](#-required-formatting)
6. [🧠 THINKING ROUNDS](#-thinking-rounds)
7. [✅ QUALITY CHECKLIST](#-quality-checklist)
8. [📦 PLATFORM INTEGRATION](#-platform-integration)
9. [🔄 STANDARD FLOW](#-standard-flow)
10. [🎯 SCOPE LABELS](#-scope-labels)
11. [⚠️ COMMON FIXES](#-common-fixes)
12. [📚 REFERENCE DOCS](#-reference-docs)

---

## 🚀 MODES AT A GLANCE

| Mode | Command | Creates | Questions | Thinking |
|------|---------|---------|-----------|----------|
| **Ticket** | `$ticket [feature]` | Dev tickets (auto-scales) | 2-4 | 1-10 |
| **Spec** | `$spec [component]` | Frontend code | 2-3 | 1-5 |
| **Doc** | `$doc [feature]` | User guides | 3-4 | 1-5 |
| **Text** | `$text [content]` | Quick snippets | 1-2 | 1-2 |
| **Discovery** | *(no command)* | Helps choose | 1 + mode | Varies |

---

## ⚡ QUICK COMMANDS

```markdown
# Bug fix
$ticket login error

# Feature
$ticket user dashboard

# Implementation
$spec modal component

# Documentation
$doc API reference

# Quick text
$text error message

# Let system help
need authentication system
→ Discovery flow
```

---

## 🎯 AUTO-SCALING (TICKETS)

| Detected | Keywords | Sections | Resolution |
|----------|----------|----------|------------|
| **Simple** | fix, bug, update | 2-3 | 4-6 items |
| **Standard** | feature, dashboard | 4-5 | 8-12 items |
| **Complex** | platform, architecture | 6-8 | 12-20 items |

System detects automatically - no manual selection needed.
**All tickets get:** TOC, dividers, proper formatting.

---

## 📤 ESSENTIAL SYMBOLS

```markdown
⌘  About/Overview
◇  Requirements
◊  Sub-headings (bold)
◳  Designs & References
→  References & H3 headers
✦  Success (bullets)
✔  Resolution (checkboxes)
⋈  Dependencies
⚡  Risks
◻️  Features (docs only)
📚  Resources (docs)
```

**Updated Symbols:**
- **◳** - Designs & References section (was ⌘)
- **⋈** - Dependencies section (was ⊗)

---

## 📋 REQUIRED FORMATTING

### Every Ticket Must Have:

```markdown
## 📑 Table of Contents
- [All sections listed]

# ⌘ About
[Introduction]

---

### → Key problems:
- First problem (minimum 2)
- Second problem

### → Reasons why:
- First value (minimum 2)
- Second value

---

## ◳ Designs & References
- [Figma designs - to be added]
- [API docs - to be added]

---

[Other sections with dividers between each]

## ⋈ Dependencies (if needed)
- External services
- Team coordination
```

### Formatting Rules:
- **TOC**: Required for ALL tickets
- **Dividers**: Between ALL sections (---)
- **Key Problems**: ### → format, 2+ items
- **Reasons Why**: ### → format, 2+ items
- **Bullets**: Use "- text" not bullet symbols
- **Designs**: Always include section with ◳

---

## 🧠 THINKING ROUNDS

### When Asked
After mode selection: "How many thinking rounds? (1-10)"

### Quick Guide
- **1-2**: Bugs, snippets
- **3-5**: Features, components
- **6-10**: Platforms, initiatives

### Suggest Based On
- Complexity detected
- Scope mentioned
- Impact described

---

## ✅ QUALITY CHECKLIST

Every output needs:
- [ ] Mode detected/selected
- [ ] Thinking rounds asked
- [ ] Interactive guidance
- [ ] **Table of Contents (all tickets)**
- [ ] **Dividers between sections**
- [ ] **Key Problems (### → with 2+ items)**
- [ ] **Reasons Why (### → with 2+ items)**
- [ ] **Designs & References section (◳)**
- [ ] **Dependencies section if needed (⋈)**
- [ ] Proper symbols
- [ ] First heading: # ⌘
- [ ] Success: ✦ bullets
- [ ] Resolution: ✔ checkboxes
- [ ] Bullets as "- text"
- [ ] Platform offer (in chat)

---

## 📦 PLATFORM INTEGRATION

After creation, always in chat:
```markdown
📦 **Add to your workspace?**
1. **ClickUp** - Tasks, sprints
2. **Skip** - Keep artifact only

Which option? (1 or 2)
```

---

## 🔄 STANDARD FLOW

```
1. User input
   ↓
2. Mode detection/selection
   ↓
3. Ask thinking rounds
   ↓
4. Interactive questions (1-4)
   ↓
5. Auto-scale if ticket
   ↓
6. Create with:
   - Table of Contents
   - All formatting
   - Dividers
   - Proper symbols (◳, ⋈)
   ↓
7. Deliver artifact
   ↓
8. Offer platform
```

---

## 🎯 SCOPE LABELS

Always ask user for tickets:
- `[BE]` Backend
- `[FE]` Frontend
- `[FS]` Full Stack
- `[Mobile]` Mobile
- `[DevOps]` Infrastructure
- `[QA]` Testing

---

## ⚠️ COMMON FIXES

| Issue | Fix |
|-------|-----|
| No TOC | Add Table of Contents to ALL tickets |
| No dividers | Add --- between ALL sections |
| Wrong problems format | Use ### → Key problems: |
| Wrong reasons format | Use ### → Reasons why: |
| Less than 2 items | Always 2+ problems/reasons |
| No Designs section | Always include with ◳ symbol |
| Missing Dependencies | Add ⋈ section when needed |
| Bullet symbols | Use "- text" format |
| No ⌘ symbol | Always use in first heading |
| Space in checkbox | Use `[]` not `[ ]` |
| Platform in artifact | Keep in chat only |
| Manual complexity | Let system auto-detect |

---

## 📚 REFERENCE DOCS

Need more detail?
- **Formats & Templates** → Reference Guide.md
- **Interactive Examples** → Interactive Flows.md
- **Platform Details** → Platform Integration.md
- **All Formatting Rules** → Reference Guide.md

### Quick Symbol Reference:
```markdown
# Core Symbols
⌘ - About/Overview sections
◇ - Requirements
◊ - Sub-headings (bold)
◳ - Designs & References (NEW)
⋈ - Dependencies (NEW)
→ - References & H3 headers
✦ - Success criteria
✔ - Resolution checklist
⚡ - Risks
◻️ - Doc features
📚 - Resources
```

### Quick Formatting Reference:
```markdown
# Ticket Structure
1. Table of Contents
2. # ⌘ About
3. ---
4. ### → Key problems: (2+ items)
5. ### → Reasons why: (2+ items)
6. ---
7. ## ◳ Designs & References
8. ---
9. ## ◇ Requirements
10. [sections with dividers]
11. ## ⋈ Dependencies (if needed)
```

---

*Quick reference for daily use. All modes interactive. Thinking user-controlled. Every ticket needs TOC, dividers, and proper Key Problems/Reasons formatting. Uses ◳ for Designs & References, ⋈ for Dependencies.*