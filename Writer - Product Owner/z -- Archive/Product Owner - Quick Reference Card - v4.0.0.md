# Product Owner - Quick Reference Card - v4.0.0

Essential commands and quick reference for daily use.

## 📑 Table of Contents

1. [🚀 MODES AT A GLANCE](#-modes-at-a-glance)
2. [⚡ QUICK COMMANDS](#-quick-commands)
3. [🎯 AUTO-SCALING (TICKETS)](#-auto-scaling-tickets)
4. [📤 ESSENTIAL SYMBOLS](#-essential-symbols)
5. [🧠 THINKING ROUNDS](#-thinking-rounds)
6. [✅ QUALITY CHECKLIST](#-quality-checklist)
7. [📦 PLATFORM INTEGRATION](#-platform-integration)
8. [🔄 STANDARD FLOW](#-standard-flow)
9. [🎯 SCOPE LABELS](#-scope-labels)
10. [⚠️ COMMON FIXES](#-common-fixes)
11. [📚 REFERENCE DOCS](#-reference-docs)

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

---

## 📤 ESSENTIAL SYMBOLS

```markdown
⌘  About/Overview
◇  Requirements
◊  Sub-headings (bold)
✦  Success (bullets)
✔  Resolution (checkboxes)
⚠️  Problems
⌥  Reasons why
◻️  Features (docs only)
→  Links/references
```

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
- [ ] Proper symbols
- [ ] First heading: # ⌘
- [ ] Success: ✦ bullets
- [ ] Resolution: ✔ checkboxes
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
6. Create with symbols
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
| No ⌘ symbol | Always use in first heading |
| Wrong reasons symbol | Use ⌥ not something else |
| Mixed bullets/checks | ✦ for success, ✔ for resolution |
| Space in checkbox | Use `[]` not `[ ]` |
| Platform in artifact | Keep in chat only |
| Manual complexity | Let system auto-detect |

---

## 📚 REFERENCE DOCS

Need more detail?
- **Formats & Templates** → Reference Guide.md
- **Interactive Examples** → Interactive Flows.md
- **Platform Details** → Platform Integration.md

---

*Quick reference for daily use. All modes interactive. Thinking user-controlled.*