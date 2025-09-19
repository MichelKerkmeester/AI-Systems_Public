# Ticket - Quick Reference Card - v0.140

Your daily companion for creating professional development tickets with developer-first clarity. Everything you need at a glance, including scope prefixes and streamlined structure.

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
16. [🔧 SPEC MODE GUIDE](#16--spec-mode-guide)

---

## 1. 🚀 MODE ACTIVATION

| Mode | Command | When to Use | Checklist Items |
|------|---------|-------------|-----------------|
| **Interactive** | DEFAULT | No mode specified | Adaptive |
| **Quick** | `$q` | Simple features | 3-5 |
| **Standard** | `$s` | Full features | 8-15 |
| **Complex** | `$c` | Multi-phase work | 15-30 |
| **Epic** | `$e` | Major initiatives | 10-20 |
| **Spec** | `$spec` | Implementation details | 5-10 |

**Remember:** Interactive mode is the default unless you explicitly specify another mode.

---

## 2. 🎯 SCOPE PREFIXES

**Required in every title (except $spec mode)!**

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

**Standard Modes:**
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

**Spec Mode (Simplified):**
```markdown
#  Plain headers
## Section headers
- Bullet points
```[language] for code blocks
```

**Full symbol reference →** Ticket - Templates & Standards.md#symbols

---

## 4. 📋 TICKET STRUCTURE

### Standard Ticket Structure
Every ticket must include (in order):
1. **Title** with `# ❖ [SCOPE]` format
2. **Description** - 1 comprehensive paragraph
3. **User Value** - What users gain
4. **Business Goal** - Measurable outcome
5. **Requirements** - WHAT not HOW
   - Use **◊** for sub-headings in complex sections
   - Use — for sub-categories
6. **Success Criteria** - Checkboxes
7. **Resolution Checklist** - Implementation steps
8. **Dependencies** (if any)
9. **Labels** - Auto-generated

### Spec Mode Structure
1. **Title** - `# [Feature] Implementation Spec`
2. **Objective** - Clear technical goal (1-2 sentences)
3. **Technical Sections** - Code examples with language
4. **Browser Compatibility** - Support matrix
5. **Key Points** - Implementation notes
6. **Testing Checklist** - Specific tests

**Full templates →** Ticket - Templates & Standards.md#base-templates

---

## 5. ✍️ WRITING RULES

### ✅ Always
- Start with scope prefix [BE], [FE], etc. (except $spec)
- Write 1 paragraph description (except $spec)
- Make success measurable (no percentages)
- Include Resolution/Testing Checklist
- Use symbols consistently (simplified for $spec)
- Use **◊** for complex requirement organization
- Use — only under **◊** sub-headings
- Keep under 2 minutes reading
- Add relevant labels

### ❌ Never
- Use percentages (replace with descriptive terms)
- Use em dashes except for sub-categories
- Specify HOW to implement (except $spec mode)
- Mix multiple features
- Skip required sections
- Assume missing context
- Use h3 for main titles (use h1)
- Include Technical Details sections (except in $spec)

### 🔧 Spec Mode Exception
In $spec mode:
- **DO** include implementation details
- **DO** provide code examples
- **DO** focus on HOW
- **DON'T** include business justification
- **DON'T** use complex symbol hierarchy

**Writing principles →** Writer - Dev Tickets.md#writing-principles

---

## 6. 🎯 QUICK PATTERNS

### Title Format
**Standard:** `# ❖ [BE] User Authentication System`
**Spec:** `# Scrollbar Visibility Implementation Spec`

### Description Pattern
```markdown
[Single comprehensive paragraph covering: current situation, problems, impacts, proposed solution, benefits, and expected outcomes. Use bullet points within the paragraph if needed for clarity.]
```

### Spec Objective Pattern
```markdown
## Objective
[1-2 sentences stating the technical goal clearly and concisely]
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

### Bug Sections Pattern
```markdown
## ◆ Current Behavior
[What's happening now]

## ✓ Desired Behavior
[What should happen]
```

### Missing Info?
Ask ONE specific question:
- "Who uses this feature?"
- "How do we measure success?"
- "Do you have designs?"
- "Would you like a technical spec instead?"

### UI Feature?
Offer Figma integration:
"Do you have Figma designs I can review?"

**Pattern examples →** Ticket - Examples Library.md#partial-input-examples

---

## 7. 🚨 MCP SELECTION

```
Simple request + $q → Sequential Thinking (1-2 thoughts)
Standard request + $s → Sequential Thinking (2-3 thoughts)
Implementation spec + $spec → Sequential Thinking (1-2 thoughts)
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

**Spec:**
"Creating implementation spec! 🔧"

---

## 9. 📊 RESOLUTION CHECKLIST SIZES

| Mode | Items | Structure | Type |
|------|-------|-----------|------|
| Quick | 3-5 | Single list | Resolution |
| Standard | 8-15 | 2-3 categories | Resolution |
| Complex | 15-30 | Phase-based | Resolution |
| Epic | 10-20 | Coordination | Resolution |
| Spec | 5-10 | Testing focus | Testing |

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
| Spec | `implementation`, `technical-spec` |

---

## 11. 🔗 QUICK LINKS

**Need help with:**
- **Templates?** → Ticket - Templates & Standards.md
- **Examples?** → Ticket - Examples Library.md
- **Interactive mode?** → Ticket - Interactive Mode.md
- **System rules?** → Writer - Dev Tickets.md
- **Specific pattern?** → Ticket - Examples Library.md#feature-type-patterns
- **Spec examples?** → Ticket - Examples Library.md#spec-mode-examples

---

## 12. ⚡ COMMON COMMANDS

```markdown
$interactive          Start guided creation (DEFAULT)
$q search feature    Quick ticket
$s user dashboard    Standard ticket
$c payment system    Complex ticket
$e mobile app        Epic ticket
$spec hide scrollbar Implementation spec
```

---

## 13. 📐 SYMBOL HIERARCHY

### Standard Hierarchy
```markdown
# ❖ [SCOPE] Feature Title
Comprehensive description paragraph...

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

### Spec Mode (Simplified)
```markdown
# Feature Implementation Spec

## Objective
Clear technical goal...

## Implementation
```language
// Code here
```

## Key Points
- Important note
- Another note
```

---

## 14. ✅ QUALITY CHECKLIST

### Standard Tickets
Before delivering ANY ticket:
1. 🎯 Scope prefix included?
2. 📝 1 paragraph description?
3. ❖ Symbols in all sections?
4. 💡 User value clear?
5. 🎯 Success measurable (no %)?
6. ✓ Resolution checklist included?
7. ⏱️ Under 2 minutes to read?
8. 🔗 Dependencies noted?
9. 🏷️ Labels added?
10. **◊** Sub-headings used for complex sections?
11. 📦 In markdown artifact?

### Spec Mode
Before delivering spec:
1. 🎯 Clear objective stated?
2. 💻 Code examples included?
3. 🌐 Browser compatibility noted?
4. 📝 Key points listed?
5. ✓ Testing checklist included?
6. 📦 In markdown artifact?

---

## 15. 🚀 QUICK START

1. User makes request
2. No mode? → Use Interactive
3. Implementation request? → Suggest $spec
4. Detect scope → Add [BE], [FE], etc. (except $spec)
5. Write comprehensive paragraph (except $spec)
6. Complex requirements? → Use **◊** and —
7. Generate labels
8. Deliver ticket in artifact
9. Show quality dashboard

**Remember:** When in doubt, use Interactive Mode!

---

## 16. 🔧 SPEC MODE GUIDE

### When to Use $spec
- User asks "how to implement"
- Request for CSS/JS code
- Technical approach needed
- Browser compatibility questions
- Performance optimization techniques

### Spec Structure
```markdown
# [Feature] Implementation Spec

## Objective
[1-2 sentences - technical goal]

## [Technical Section]
```language
// Implementation code
```

## Browser Compatibility
- Chrome: ✓ [method/property]
- Firefox: ✓ [method/property]
- Safari: ✓ [method/property]

## Key Points
- [Implementation detail]
- [Important consideration]

## Testing Checklist
- [ ] [Specific test]
- [ ] [Compatibility test]
```

### Common Spec Types
- CSS layouts/styling
- JavaScript utilities
- API integration patterns
- Performance optimizations
- Browser-specific implementations
- Responsive design patterns

### Spec Mode Tips
- Keep code examples focused
- Always include browser support
- Provide alternative approaches when relevant
- Include edge case handling
- Make code copy-paste ready

---

## 📝 Description Writing Tips

### Single Paragraph Should Include:
- Current situation/problem
- Specific pain points
- User/business impact
- Proposed solution
- Expected benefits
- Key improvements
- Success indicators
- Can use bullet points within paragraph

### Avoid:
- Percentages (use "significant", "majority", etc.)
- Technical jargon in main description
- Implementation details (except $spec)
- Assumptions about priority
- Multiple paragraphs

---

## 🔄 Quick Replacements

Instead of percentages, use:
- "dramatically improve"
- "significant reduction"
- "majority of users"
- "substantial increase"
- "minimal impact"
- "highly effective"

For bug tickets:
- Use "Desired Behavior" (not "Expected")
- Keep descriptions focused on impact

For spec mode:
- Use "Implementation Spec" (not "Technical Spec")
- Focus on HOW (not WHY)

---

*Keep this card handy for quick reference. Version 1.3.0 updates: single-paragraph descriptions, "Desired Behavior" for bugs, removed Technical Details sections, added Spec Mode for implementation specifications.*