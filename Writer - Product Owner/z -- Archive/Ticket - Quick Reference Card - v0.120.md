# Ticket - Quick Reference Card - v0.120

Your daily companion for creating professional development tickets with developer-first clarity. Everything you need at a glance, including scope prefixes and comprehensive descriptions.

## 📌 Description

This quick reference card provides instant access to the most commonly needed information for creating development tickets with enhanced clarity. It's designed for:
- **Quick lookups** during ticket creation
- **Mode selection** guidance
- **Scope prefix** reference
- **Symbol reference** with hierarchy
- **Common patterns** and responses
- **Quality verification** checklist

Keep this open while writing tickets for maximum efficiency.

## 📑 Table of Contents

1. [🚀 MODE ACTIVATION](#1--mode-activation)
2. [🎯 SCOPE PREFIXES](#2--scope-prefixes)
3. [🔤 ESSENTIAL SYMBOLS](#3--essential-symbols)
4. [📋 TICKET STRUCTURE](#4--ticket-structure)
5. [✍️ WRITING RULES](#5--writing-rules)
6. [🎯 QUICK PATTERNS](#6--quick-patterns)
7. [🚨 MCP SELECTION](#7--mcp-selection)
8. [💬 MODE RESPONSES](#8--mode-responses)
9. [📊 RESOLUTION CHECKLIST SIZES](#9--resolution-checklist-sizes)
10. [🏷️ LABEL MAPPING](#10--label-mapping)
11. [🔗 QUICK LINKS](#11--quick-links)
12. [⚡ COMMON COMMANDS](#12--common-commands)
13. [📐 SYMBOL HIERARCHY](#13--symbol-hierarchy)
14. [✅ QUALITY CHECKLIST](#14--quality-checklist)
15. [🚀 QUICK START](#15--quick-start)

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

## 2. 🎯 SCOPE PREFIXES

**Required in every title!**

| Prefix | Use For | Indicators |
|--------|---------|------------|
| **[BE]** | Backend | API, database, server, authentication |
| **[FE]** | Frontend | UI, components, display, user interface |
| **[Mobile]** | Mobile | iOS, Android, app, native |
| **[FS]** | Full Stack | End-to-end features |
| **[DevOps]** | Infrastructure | Deployment, CI/CD, monitoring |
| **[QA]** | Testing | Test automation, quality |

---

## 3. 🔤 ESSENTIAL SYMBOLS

```markdown
❖  Title and major features (use with #)
◇  Requirements and main sections
◊  Sub-headings within sections
→  Designs & References
✓  Success criteria AND Resolution Checklist
⊗  Dependencies
⚠  Risks and warnings
—  Sub-categories under ◊ sub-headings
```

**Full symbol reference →** Ticket - Templates & Standards.md#symbols

---

## 4. 📋 TICKET STRUCTURE

Every ticket must include (in order):
1. **Title** with `# ❖ [SCOPE]` format
2. **Description** - 1-2 comprehensive paragraphs
3. **User Value** - What users gain
4. **Business Goal** - Measurable outcome
5. **Requirements** - WHAT not HOW
   - Use **◊** for sub-headings in complex sections
   - Use — for sub-categories
6. **Technical Details** - Components, APIs, architecture
7. **Success Criteria** - Checkboxes
8. **Resolution Checklist** - Implementation steps
9. **Dependencies** (if any)
10. **Labels** - Auto-generated

**Full templates →** Ticket - Templates & Standards.md#base-templates

---

## 5. ✍️ WRITING RULES

### ✅ Always
- Start with scope prefix [BE], [FE], etc.
- Write 1-2 paragraph descriptions
- Include Technical Details section
- Make success measurable (no percentages)
- Include Resolution Checklist
- Use symbols consistently
- Use **◊** for complex requirement organization
- Use — only under **◊** sub-headings
- Keep under 2 minutes reading
- Add relevant labels

### ❌ Never
- Use percentages (replace with descriptive terms)
- Use em dashes except for sub-categories
- Specify HOW to implement
- Mix multiple features
- Skip required sections
- Assume missing context
- Use h3 for main titles (use h1)

**Writing principles →** Writer - Dev Tickets.md#writing-principles

---

## 6. 🎯 QUICK PATTERNS

### Title Format
```markdown
# ❖ [BE] User Authentication System
```

### Description Pattern
```markdown
[First paragraph: Current situation, problems, impacts with bullet points if needed]

[Second paragraph: Solution approach, benefits, expected outcomes]
```

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

### Technical Details Pattern
```markdown
## ◇ Technical Details

**◊** Architecture
- **Component:** Backend-System (Go)
- **API:** POST /endpoint
- **Database:** PostgreSQL

**◊** Performance
- **Response:** Fast response required
- **Caching:** Strategic approach
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

## 7. 🚨 MCP SELECTION

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

## 8. 💬 MODE RESPONSES

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

## 9. 📊 RESOLUTION CHECKLIST SIZES

| Mode | Items | Structure |
|------|-------|-----------|
| Quick | 3-5 | Single list |
| Standard | 8-15 | 2-3 categories |
| Complex | 15-30 | Phase-based |
| Epic | 10-20 | Coordination |

**Checklist templates →** Ticket - Templates & Standards.md#resolution-checklist-templates

---

## 10. 🏷️ LABEL MAPPING

**Automatic labels based on content:**

| Content Type | Labels Applied |
|--------------|----------------|
| Backend | `Backend-System`, `API` |
| Frontend | `[App]-App`, `UI` |
| Mobile | `Mobile-App` |
| Database | `Database`, `Backend-System` |
| Authentication | `Authentication`, `Security` |
| Bug | `bug`, `defect` |
| Feature | `feature`, `enhancement` |
| Performance | `performance`, `optimization` |

---

## 11. 🔗 QUICK LINKS

**Need help with:**
- **Templates?** → Ticket - Templates & Standards.md
- **Examples?** → Ticket - Examples Library.md
- **Interactive mode?** → Ticket - Interactive Mode.md
- **System rules?** → Writer - Dev Tickets.md
- **Specific pattern?** → Ticket - Examples Library.md#feature-type-patterns

---

## 12. ⚡ COMMON COMMANDS

```markdown
$interactive          Start guided creation (DEFAULT)
$q search feature    Quick ticket
$s user dashboard    Standard ticket
$c payment system    Complex ticket
$e mobile app        Epic ticket
```

---

## 13. 📐 SYMBOL HIERARCHY

The complete hierarchy for complex tickets:

```markdown
# ❖ [SCOPE] Feature Title
Rich description paragraphs...

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

## 14. ✅ QUALITY CHECKLIST

Before delivering ANY ticket:
1. 🎯 Scope prefix included?
2. 📝 1-2 paragraph description?
3. ❖ Symbols in all sections?
4. 💡 User value clear?
5. 🎯 Success measurable (no %)?
6. 🔧 Technical Details included?
7. ✓ Resolution checklist included?
8. ⏱️ Under 2 minutes to read?
9. 🔗 Dependencies noted?
10. 🏷️ Labels added?
11. **◊** Sub-headings used for complex sections?
12. 📦 In markdown artifact?

---

## 15. 🚀 QUICK START

1. User makes request
2. No mode? → Use Interactive
3. Detect scope → Add [BE], [FE], etc.
4. Write rich description
5. Complex requirements? → Use **◊** and —
6. Add Technical Details
7. Generate labels
8. Deliver ticket in artifact
9. Show quality dashboard

**Remember:** When in doubt, use Interactive Mode!

---

## 📝 Description Writing Tips

### First Paragraph Should Include:
- Current situation/problem
- Specific pain points
- User/business impact
- Can use bullet points for multiple issues

### Second Paragraph Should Include:
- Proposed solution
- Expected benefits
- Key improvements
- Success indicators

### Avoid:
- Percentages (use "significant", "majority", etc.)
- Technical jargon in main description
- Implementation details
- Assumptions about priority

---

## 🔄 Quick Replacements

Instead of percentages, use:
- "dramatically improve"
- "significant reduction"
- "majority of users"
- "substantial increase"
- "minimal impact"
- "highly effective"

---

*Keep this card handy for quick reference. Version 1.2.0 adds scope prefixes, comprehensive descriptions, technical details, and developer-first clarity without percentages.*