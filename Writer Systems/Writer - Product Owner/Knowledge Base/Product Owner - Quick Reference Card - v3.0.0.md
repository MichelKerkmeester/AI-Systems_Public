# Quick Reference Card - v3.0.0

Daily companion for creating professional tickets, specs, and documentation with intelligent guidance and platform integration.

## 📌 Description

Quick access to the unified Product Owner system. All modes are interactive with smart complexity detection.

## 📑 Table of Contents

1. [🚀 MODE ACTIVATION](#1--mode-activation)
2. [📤 ESSENTIAL SYMBOLS](#2--essential-symbols)
3. [🎯 TICKET AUTO-SCALING](#3--ticket-auto-scaling)
4. [📋 TICKET STRUCTURE](#4--ticket-structure)
5. [📚 DOCUMENTATION STRUCTURE](#5--documentation-structure)
6. [💻 SPEC STRUCTURE](#6--spec-structure)
7. [✍️ WRITING RULES](#7--writing-rules)
8. [🔍 DISCOVERY FLOW](#8--discovery-flow)
9. [🚨 MCP SELECTION](#9--mcp-selection)
10. [💬 MODE RESPONSES](#10--mode-responses)
11. [✓ RESOLUTION SIZING](#11--resolution-sizing)
12. [🔗 PLATFORM INTEGRATION](#12--platform-integration)
13. [⚡ COMMON COMMANDS](#13--common-commands)
14. [📐 FORMAT HIERARCHY](#14--format-hierarchy)
15. [✅ QUALITY CHECKLIST](#15--quality-checklist)
16. [🚀 QUICK START](#16--quick-start)

---

## 1. 🚀 MODE ACTIVATION

| Mode | Command | Purpose | Output | Interactive |
|------|---------|---------|--------|-------------|
| **Discovery** | DEFAULT | Determine what to create | Varies | Yes |
| **Ticket** | `$ticket` | Development tickets | Auto-scales 2-8 sections | Yes |
| **Spec** | `$spec` | Frontend implementation | Code blocks | Yes |
| **Documentation** | `$doc` | User guides | Feature docs | Yes |

**Remember:** 
- ALL modes are interactive
- $ticket auto-detects complexity
- Discovery helps when unsure
- Modes skip discovery phase

---

## 2. 📤 ESSENTIAL SYMBOLS

```markdown
⌘  "About"/"Overview" heading and sections
◇  Requirements (tickets)
◻️  Features (documentation)
◊  Sub-headings (bold)
→  Designs & References
✦  Success criteria (bullets only)
✓  Resolution Checklist (checkboxes only)
⊗  Dependencies
⚡  Risks
⚠️  Key problems
⌥  Reasons why
📚  Additional resources (docs)
—  Sub-categories under ◊
```

---

## 3. 🎯 TICKET AUTO-SCALING

### Automatic Detection

| Request Type | Complexity | Sections | Resolution |
|--------------|------------|----------|------------|
| Bug fix, small change | **Simple** | 2-3 | 4-6 items |
| Feature, clear scope | **Standard** | 4-5 | 8-12 items |
| Platform, initiative | **Complex** | 6-8 | 12-20 items |

### Keywords Triggering Complexity

**Simple:** fix, bug, update, modify, adjust
**Standard:** feature, dashboard, workflow, integration
**Complex:** platform, architecture, multiple, compliance

---

## 4. 📋 TICKET STRUCTURE

### All Tickets Include
1. **Artifact Title**: `[SCOPE] Feature Name`
2. **First Heading**: `# ⌘ About`
3. **Description**: Brief with ⚠️ and ⌥
4. **Requirements**: ◇ with auto-scaled ◊ sections
5. **Success Criteria**: ✦ bullets only
6. **Resolution**: ✓ checkboxes (scaled by complexity)
7. **Dependencies**: If detected
8. **Labels**: User-specified

### After Ticket (In Chat):
**Platform Offer**: ClickUp/Notion/Skip

---

## 5. 📚 DOCUMENTATION STRUCTURE

### Documentation Components
1. **Artifact Title**: `[Product] Documentation`
2. **First Heading**: `# ⌘ Overview`
3. **Metadata**: Audience, version, complexity
4. **Features**: ◻️ sections with ◊ components
5. **Related Materials**: Links and resources
6. **Important Notes**: Limitations, warnings
7. **Additional Resources**: Guides, support

### After Documentation (In Chat):
**Platform Offer**: Notion (preferred)/ClickUp/Skip

---

## 6. 💻 SPEC STRUCTURE

### Spec Components
1. **Title**: Implementation name
2. **Objective**: 1-2 sentences
3. **Quick Setup**: Interactive choices
4. **Implementation**: Working code
5. **Key Points**: Performance, compatibility
6. **Browser Support**: If relevant

### After Spec (In Chat):
**Platform Offer**: Based on team preference

---

## 7. ✍️ WRITING RULES

### ✅ Always
- Use interactive guidance
- Auto-detect complexity ($ticket)
- First heading with ⌘
- ✓ for Resolution (checkboxes)
- ✦ for Success (bullets)
- Add dividers between ◊ sections
- Offer platform integration

### ❌ Never
- Manual complexity selection
- Skip interactive flow
- Mix ✦ and ✓ symbols
- Space in checkbox brackets
- Platform offer in artifact

---

## 8. 🔍 DISCOVERY FLOW

### When No Mode Specified

```markdown
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket
2. Implementation spec
3. Product documentation

Which best fits? (1, 2, or 3)
```

### User Selection Routes
- **1** → Ticket flow (auto-scales)
- **2** → Spec flow (implementation)
- **3** → Doc flow (documentation)

---

## 9. 🚨 MCP SELECTION

```
Simple ticket → Sequential (1-2 thoughts)
Standard ticket → Sequential (2-3 thoughts)
Complex ticket → Cascade (3-5 thoughts)
Spec → Sequential (1-2 thoughts)
Documentation → Sequential (2-3 thoughts)
Discovery → Cascade (3-5 thoughts)
+ UI features → Add Figma (optional)
```

---

## 10. 💬 MODE RESPONSES

**Discovery**: "Welcome! Let's figure out what you need. 🤔"
**$ticket**: "Let's create your ticket! 🎯"
**$spec**: "Let's build your implementation! 🔧"
**$doc**: "Let's document this feature! 📚"
**Platform**: "📦 Add to your workspace?" (after creation)

---

## 11. ✓ RESOLUTION SIZING

### Auto-Scaled by Complexity

| Complexity | Sections | Items/Section | Total Items |
|------------|----------|---------------|-------------|
| **Simple** | 2-3 | 2-3 | 4-6 |
| **Standard** | 4-5 | 2-3 | 8-12 |
| **Complex** | 6-8 | 2-3 | 12-20 |

### Good Resolution Items
✅ "[] Build authentication system"
✅ "[] Complete integration testing"
❌ "[] Write login function" (too granular)

---

## 12. 🔗 PLATFORM INTEGRATION

### After Every Creation (In Chat):
```markdown
📦 **Add to your workspace?**

1. **ClickUp** - Task management, sprints
2. **Notion** - Documentation, wikis
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

### Platform Preferences
- **Tickets** → ClickUp (tasks)
- **Documentation** → Notion (knowledge base)
- **Specs** → Either (team preference)

---

## 13. ⚡ COMMON COMMANDS

```markdown
# Discovery (default)
need user profiles

# Direct ticket
$ticket payment system

# Implementation spec
$spec modal component

# Documentation
$doc analytics dashboard

# After any creation
[Platform offer appears in chat]
```

---

## 14. 📐 FORMAT HIERARCHY

### Tickets
```markdown
# ⌘ About
## ◇ Requirements
**◊** Sub-heading
— Sub-category
• Detail
---
[Next ◊ section]

## ✦ Success Criteria
- Metric (bullets only)

## ✓ Resolution Checklist
[] Outcome (checkboxes only)
```

### Documentation
```markdown
# ⌘ Overview
## ⌘ Features
### ◻️ Feature Name
**◊** Component
— Category
• Detail
```

---

## 15. ✅ QUALITY CHECKLIST

### All Outputs
1. 🎯 Interactive guidance used?
2. 🎯 Appropriate mode selected?
3. 📝 First heading with ⌘?
4. 📝 Symbols consistent?
5. 📝 Using correct symbols?
6. ✦ Success with bullets only?
7. ✓ Resolution with checkboxes?
8. ➖ Dividers between ◊ sections?
9. 🔗 Platform offer in chat?

### Ticket Specific
- [ ] Complexity auto-detected?
- [ ] Scope specified by user?
- [ ] Labels specified by user?
- [ ] Scaled appropriately?

---

## 16. 🚀 QUICK START

### Standard Flow
1. User input
2. Mode detection or discovery
3. Interactive questions
4. Auto-scale if ticket
5. Build with proper symbols
6. Deliver artifact
7. **Offer platform integration**

### Mode Decision Tree
```
User Input
    ↓
Has mode command?
    ├─ No → Discovery flow
    ├─ $ticket → Ticket questions (auto-scale)
    ├─ $spec → Implementation questions
    └─ $doc → Documentation questions
         ↓
    All modes
         ↓
    Creation Complete
         ↓
    Platform Offer (in chat)
         ↓
    ClickUp / Notion / Skip
```

### Key Features in v5.0.0
- **Unified $ticket** with auto-scaling
- **All modes interactive**
- **Auto-complexity** detection
- **Smarter system** with less choices

---

*Unified ticket mode with auto-scaling. All modes interactive. Smart complexity detection. Platform integration after every creation.*