# Ticket - Quick Reference Card - v1.1.0

Your daily companion for creating professional development tickets. Everything you need at a glance, including the new **◊** sub-heading pattern.

## 📌 Description

This quick reference card provides instant access to the most commonly needed information for creating development tickets. It's designed for:
- **Quick lookups** during ticket creation
- **Mode selection** guidance
- **Symbol reference** without searching (now with **◊**)
- **Common patterns** and responses
- **Quality verification** checklist

Keep this open while writing tickets for maximum efficiency.

## 📑 Table of Contents

1. [🚀 MODE ACTIVATION](#1--mode-activation)
2. [🔤 ESSENTIAL SYMBOLS](#2--essential-symbols)
3. [📋 TICKET STRUCTURE](#3--ticket-structure)
4. [✍️ WRITING RULES](#4--writing-rules)
5. [🎯 QUICK PATTERNS](#5--quick-patterns)
6. [🚨 MCP SELECTION](#6--mcp-selection)
7. [💬 MODE RESPONSES](#7--mode-responses)
8. [📊 RESOLUTION CHECKLIST SIZES](#8--resolution-checklist-sizes)
9. [🔗 QUICK LINKS](#9--quick-links)
10. [⚡ COMMON COMMANDS](#10--common-commands)
11. [📐 SYMBOL HIERARCHY](#11--symbol-hierarchy)
12. [✅ QUALITY CHECKLIST](#12--quality-checklist)
13. [🚀 QUICK START](#13--quick-start)

---

## 1. 🚀 MODE ACTIVATION

| Mode | Command | When to Use | Checklist Items |
|------|---------|-------------|-----------------|
| **Interactive** | DEFAULT | No mode specified | Adaptive |
| **Quick** | `$q` | Simple features | 3-5 |
| **Standard** | `$s` | Full features | 8-15 |
| **Complex** | `$c` | Multi-phase work | 15-30 |
| **Epic** | `$e` | Major initiatives | 10-20 |

**Remember:** Interactive mode is the default unless you explicitly specify another mode.

---

## 2. 🔤 ESSENTIAL SYMBOLS

```markdown
❖  Title and major features
◇  Requirements and main sections
◊  Sub-headings within sections (NEW)
→  Designs & References
✓  Success criteria AND Resolution Checklist
⊗  Dependencies
⚠  Risks and warnings
—  Sub-categories under ◊ sub-headings (NEW)
```

**Full symbol reference →** Ticket - Templates & Standards.md#symbols

---

## 3. 📋 TICKET STRUCTURE

Every ticket must include (in order):
1. **Title** with ❖ symbol
2. **User Value** - What users gain
3. **Business Goal** - Measurable outcome
4. **Requirements** - WHAT not HOW
   - Use **◊** for sub-headings in complex sections
   - Use — for sub-categories
5. **Success Criteria** - Checkboxes
6. **Resolution Checklist** - Implementation steps
7. **Dependencies** (if any)

**Full templates →** Ticket - Templates & Standards.md#base-templates

---

## 4. ✍️ WRITING RULES

### ✅ Always
- Start with user value
- Make success measurable
- Include Resolution Checklist
- Use symbols consistently
- Use **◊** for complex requirement organization
- Use — only under **◊** sub-headings
- Keep under 2 minutes reading

### ❌ Never
- Use em dashes except for sub-categories
- Specify HOW to implement
- Mix multiple features
- Skip required sections
- Assume missing context

**Writing principles →** Writer - Dev Tickets.md#writing-principles

---

## 5. 🎯 QUICK PATTERNS

### Complex Requirements Pattern
```markdown
## ◇ Requirements

**◊** Component Name
— Category 1
• Requirement
• Another requirement
— Category 2
• More requirements
```

### Missing Info?
Ask ONE specific question:
- "Who uses this feature?"
- "How do we measure success?"
- "Do you have designs?"

### UI Feature?
Offer Figma integration:
"Do you have Figma designs I can review?"

**Pattern examples →** Ticket - Examples Library.md#partial-input-examples

---

## 6. 🚨 MCP SELECTION

```
Simple request + $q → Sequential Thinking (1-2 thoughts)
Standard request + $s → Sequential Thinking (2-3 thoughts)
Interactive mode → Cascade Thinking (3-5 thoughts)
Complex/unclear → Cascade Thinking (3-5+ thoughts)
Epic/major → Cascade Thinking (5+ thoughts)
+ UI features → Add Figma MCP (optional)
```

**Full MCP guide →** Writer - Dev Tickets.md#intelligent-mcp-process

---

## 7. 💬 MODE RESPONSES

**Interactive (Default):**
"Let's create a great ticket together! 🤝"

**Quick:**
"Quick ticket coming up! ⚡"

**Standard:**
"Creating your ticket with all the essentials! 📋"

**Complex:**
"Breaking this down into manageable phases! 🔧"

**Epic:**
"Building your epic initiative! 🚀"

---

## 8. 📊 RESOLUTION CHECKLIST SIZES

| Mode | Items | Structure |
|------|-------|-----------|
| Quick | 3-5 | Single list |
| Standard | 8-15 | 2-3 categories |
| Complex | 15-30 | Phase-based |
| Epic | 10-20 | Coordination |

**Checklist templates →** Ticket - Templates & Standards.md#resolution-checklist-templates

---

## 9. 🔗 QUICK LINKS

**Need help with:**
- **Templates?** → Ticket - Templates & Standards.md
- **Examples?** → Ticket - Examples Library.md
- **Interactive mode?** → Ticket - Interactive Mode.md
- **System rules?** → Writer - Dev Tickets.md
- **Specific pattern?** → Ticket - Examples Library.md#feature-type-patterns

---

## 10. ⚡ COMMON COMMANDS

```markdown
$interactive          Start guided creation (DEFAULT)
$q search feature    Quick ticket
$s user dashboard    Standard ticket
$c payment system    Complex ticket
$e mobile app        Epic ticket
```

---

## 11. 📐 SYMBOL HIERARCHY

The complete hierarchy for complex tickets:

```markdown
### ❖ Feature Title
## ◇ Requirements
**◊** Sub-heading
— Sub-category
• Bullet point
• Another point
— Another Sub-category
• More points

**◊** Another Sub-heading
— Category
• Details
```

This creates clear visual organization for complex requirements.

---

## 12. ✅ QUALITY CHECKLIST

Before delivering ANY ticket:
1. ❖ Symbols in all sections?
2. 📝 User value clear?
3. 🎯 Success measurable?
4. ✓ Resolution checklist included?
5. ⏱️ Under 2 minutes to read?
6. 🔗 Dependencies noted?
7. **◊** Sub-headings used for complex sections?
8. 📦 In markdown artifact?

---

## 13. 🚀 QUICK START

1. User makes request
2. No mode? → Use Interactive
3. Complex requirements? → Use **◊** and —
4. Deliver ticket in artifact
5. Show quality dashboard

**Remember:** When in doubt, use Interactive Mode!

---

*Keep this card handy for quick reference. Version 1.1.0 adds **◊** for sub-headings and — for sub-categories to improve complex requirement organization.*