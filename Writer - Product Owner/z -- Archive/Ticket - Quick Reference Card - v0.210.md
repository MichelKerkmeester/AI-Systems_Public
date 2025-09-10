# Ticket - Quick Reference Card - v0.210

Your daily companion for creating professional development tickets with developer-first clarity. **Major update: Resolution Checklists now use global approach with max 3 items per section.**

## 📌 Description

This quick reference card provides instant access to the most commonly needed information for creating development tickets. It's designed for:
- **Quick lookups** during ticket creation
- **Mode selection** guidance
- **Interactive offer** reminders
- **Symbol reference** with hierarchy
- **Resolution checklist** sizing (NEW global approach)
- **Spec mode** fast paths
- **Quality verification** checklist

Keep this open while writing tickets for maximum efficiency.

## 📑 Table of Contents

1. [🚀 MODE ACTIVATION](#1--mode-activation)
2. [🎯 INTERACTIVE OFFERS](#2--interactive-offers)
3. [🔤 ESSENTIAL SYMBOLS](#3--essential-symbols)
4. [📋 TICKET STRUCTURE](#4--ticket-structure)
5. [✍️ WRITING RULES](#5--writing-rules)
6. [🎯 QUICK PATTERNS](#6--quick-patterns)
7. [🚨 MCP SELECTION](#7--mcp-selection)
8. [💬 MODE RESPONSES](#8--mode-responses)
9. [📊 RESOLUTION CHECKLIST SIZES](#9--resolution-checklist-sizes)
10. [💻 SPEC MODE FAST PATHS](#10--spec-mode-fast-paths)
11. [🔗 QUICK LINKS](#11--quick-links)
12. [⚡ COMMON COMMANDS](#12--common-commands)
13. [📐 SYMBOL HIERARCHY](#13--symbol-hierarchy)
14. [✅ QUALITY CHECKLIST](#14--quality-checklist)
15. [🚀 QUICK START](#15--quick-start)

---

## 1. 🚀 MODE ACTIVATION

| Mode | Command | When to Use | Sections | Items/Section | Total Items | Interactive Offer |
|------|---------|-------------|----------|---------------|-------------|-------------------|
| **Interactive** | DEFAULT | No mode specified | Adaptive | 2-3 | Adaptive | N/A (Default) |
| **Quick** | `$q` | Simple features | 2-3 | 2-3 | 4-6 | No |
| **Standard** | `$s` | Full features | 4-5 | 2-3 | 8-12 | **YES - Always** |
| **Complex** | `$c` | Major features | 6-8 | 2-3 | 12-20 | **YES - Always** |
| **Spec** | `$spec` | Frontend implementation | N/A | N/A | 20-60 lines | No (Minimal) |

**Remember:** 
- Interactive mode is the default unless you explicitly specify another mode
- **ALWAYS offer Interactive** when users use $s or $c
- Complex handles both phases AND child tickets
- Spec mode uses minimal conversation (1-3 questions max)
- **NEW**: Resolution checklists focus on outcomes, not tasks

---

## 2. 🎯 INTERACTIVE OFFERS

### When to Offer (MANDATORY)

**Standard Mode ($s):**
```markdown
System: I see you want a standard ticket for [feature].

Would you like me to:
1. **Guide you through creating it interactively**
2. **Create it directly**

Which would you prefer? (1 or 2)
```

**Complex Mode ($c):**
```markdown
System: I see you want a complex ticket for [feature].

This is a substantial feature! Would you like me to:
1. **Walk you through it interactively**
2. **Create it directly**

Interactive mode can help ensure we don't miss critical requirements.
What's your preference? (1 or 2)
```

### Response Handling
- **If 1 (Interactive)**: Start conversational flow
- **If 2 (Direct)**: Still ask for scope and labels

---

## 3. 🔤 ESSENTIAL SYMBOLS

**Standard Modes:**
```markdown
❖  Title and major features
◇  Requirements and main sections
◊  Sub-headings within sections
→  Designs & References
✓  Success criteria AND Resolution Checklist
⊗  Dependencies
⚠  Risks and warnings
⚠︎  Key problems in descriptions
⁉  Reasons why in descriptions
—  Sub-categories under ◊ sub-headings
```

**Spec Mode (Minimal):**
```markdown
#  Plain headers
## Section headers
```[language] for code blocks
- Bullet points for key points
```

---

## 4. 📋 TICKET STRUCTURE

### Standard Ticket Components
1. **Title** with `# ❖ [SCOPE]` format
2. **Description** - 1 paragraph with ⚠︎ and ⁉
3. **User Value** - What users gain
4. **Business Goal** - Measurable outcome
5. **Requirements** - WHAT not HOW
   - Use **◊** for sub-headings
   - Use — for sub-categories
6. **Success Criteria** - Checkboxes
7. **Resolution Checklist** - **Global outcomes (max 3 items per section)**
8. **Dependencies** (if any)
9. **Labels** - User-specified

### Complex Mode Options
- **Option A: Phased Development** - Incremental building
- **Option B: Child Ticket Breakdown** - Multi-team coordination

### Spec Mode Structure
1. **Objective** - 1-2 sentences
2. **Implementation** - Working code
3. **Browser Compatibility** (if needed)
4. **Key Points** - Essential notes only
5. **Testing** (if requested)

---

## 5. ✍️ WRITING RULES

### ✅ Always
- Offer Interactive for $s and $c
- Ask user for scope ([BE], [FE], etc.)
- Ask user for labels
- Write 1 paragraph description
- Include Resolution Checklist (**max 3 items per section**)
- Use symbols consistently
- Keep under 2 minutes reading
- Focus on outcomes, not tasks

### ❌ Never
- Skip Interactive offer for $s/$c
- Assume scope or labels
- Use percentages in metrics
- Mix multiple features
- Skip required sections
- Include placeholders in Spec mode
- Create detailed task lists (use global outcomes)
- Exceed 3 items per checklist section

### 🔧 Resolution Checklist Rules (NEW)
- Think in **work streams**, not tasks
- Each checkbox = **meaningful deliverable**
- Maximum **3 items per section**
- Focus on **WHAT gets delivered**, not HOW
- Each item represents **2-8 hours minimum** work

---

## 6. 🎯 QUICK PATTERNS

### Title Formats
**Standard:** `# ❖ [BE] User Authentication System`
**Complex:** `# ❖ [FS] Real-time Collaboration Platform`
**Spec:** `# Hidden Scrollbar Implementation`

### Description Pattern
```markdown
[Single paragraph with context]

⚠︎ **Key problems/changes:**
* **Issue 1** - Description
* **Issue 2** - Description

⁉ **Reasons why:**
[Solution and benefits statement]
```

### Resolution Checklist Pattern (NEW)
```markdown
## ✓ Resolution Checklist

### Work Stream 1
- [ ] Outcome 1
- [ ] Outcome 2
- [ ] Outcome 3 (max)

### Work Stream 2
- [ ] Outcome 1
- [ ] Outcome 2
```

### Spec Pattern (Concise)
```markdown
## Objective
[1-2 sentences]

## Implementation
```code
[Working code]
```

## Key Points
- [Essential only]
```

---

## 7. 🚨 MCP SELECTION

```
Simple request + $q → Sequential Thinking (1-2 thoughts)
Standard request + $s → Sequential Thinking (2-3 thoughts)
Spec request + $spec → Sequential Thinking (1-2 thoughts)
Interactive mode → Cascade Thinking (3-5 thoughts)
Complex/unclear → Cascade Thinking (3-5+ thoughts)
+ UI features → Add Figma MCP (optional)
```

---

## 8. 💬 MODE RESPONSES

**Interactive (Default):**
"Let's create a great ticket together! 🤝"

**Quick:**
"Quick ticket coming up! ⚡"

**Standard:**
"I see you want a standard ticket. Would you like me to:
1. Guide you through it interactively
2. Create it directly"

**Complex:**
"I see you want a complex ticket. This is substantial! Would you like me to:
1. Walk you through it interactively
2. Create it directly"

**Spec:**
"Let me create that implementation spec. [1-3 quick questions]"

---

## 9. 📊 RESOLUTION CHECKLIST SIZES

### NEW Global Approach

| Mode | Total Sections | Items per Section | Total Items | Focus |
|------|---------------|-------------------|-------------|--------|
| **Quick** | 2-3 | 2-3 | 4-6 | Essential outcomes |
| **Standard** | 4-5 | 2-3 | 8-12 | Complete delivery |
| **Complex - Phased** | 6-8 | 2-3 | 12-20 | Phase milestones |
| **Complex - Child** | 5-6 | 2-3 | 10-15 | Coordination points |
| **Bug** | 3-4 | 2-3 | 6-10 | Fix & verify |
| **Improvement** | 4-5 | 2-3 | 8-12 | Optimize & validate |
| **Spec** | N/A | N/A | Key Points | Implementation notes |

### Section Naming Examples
- **Foundation Work** (not "Setup Tasks")
- **Core Development** (not "Implementation Steps")
- **Testing & Validation** (not "Test Cases")
- **Documentation** (not "Docs to Write")

### Item Examples
✅ **Good (Outcome):** "Build filter components with state management"
❌ **Bad (Task):** "Create FilterComponent.tsx file"

✅ **Good (Deliverable):** "Complete cross-browser testing"
❌ **Bad (Task):** "Test in Chrome, Firefox, Safari, Edge"

---

## 10. 💻 SPEC MODE FAST PATHS

### Instant Patterns (0 Questions)
```
"hide scrollbar" → CSS solution
"center div" → CSS solution
"debounce input" → JS utility
"format date" → JS utility
```

### Quick Patterns (1-2 Questions)
```
"button component" → Framework?
"data table" → Rows? Framework?
"form validation" → Framework? Inline/toast?
"autocomplete" → Framework? Local/API?
```

### Standard Patterns (3-4 Questions Max)
```
"virtual scroll" → Rows? Framework? Selection?
"real-time collab" → Users? Framework? Offline?
"responsive grid" → Grid/Flex? Columns? Gap?
```

### Output Targets
- **Simple CSS/JS**: 20-30 lines
- **Component**: 30-45 lines
- **Complex**: 45-60 lines
- **Never exceed**: 75 lines

---

## 11. 🔗 QUICK LINKS

**Need help with:**
- **Templates?** → Ticket - Templates & Standards.md
- **Examples?** → Ticket - Examples Library.md
- **Interactive mode?** → Ticket - Interactive Mode.md
- **Spec patterns?** → Ticket - Spec Mode.md
- **System rules?** → Writer - Dev Tickets.md

---

## 12. ⚡ COMMON COMMANDS

```markdown
# Default (Interactive)
need user profiles

# Quick
$q search feature

# Standard (offers Interactive)
$s user dashboard

# Complex (offers Interactive)  
$c payment system

# Spec (minimal conversation)
$spec hide scrollbar
$spec virtual table
```

---

## 13. 📐 SYMBOL HIERARCHY

### Standard Tickets
```markdown
# ❖ [SCOPE] Feature Title
## ◇ Requirements
**◊** Sub-heading
— Sub-category
• Bullet point
```

### Resolution Checklist (NEW)
```markdown
## ✓ Resolution Checklist

### Work Stream Name
- [ ] Outcome 1
- [ ] Outcome 2
- [ ] Outcome 3 (max)
```

### Spec Mode (Minimal)
```markdown
# Feature Implementation
## Objective
## Implementation
```code
```
## Key Points
```

---

## 14. ✅ QUALITY CHECKLIST

### All Tickets
Before delivering ANY ticket:
1. 🎯 Interactive offered for $s/$c?
2. 🏷️ Scope specified by user?
3. 🏷️ Labels specified by user?
4. 📝 1 paragraph description with ⚠︎ and ⁉?
5. ❖ Symbols in all sections?
6. ✓ Resolution checklist with **max 3 items per section**?
7. 🎯 Each checklist item is an **outcome, not a task**?
8. ⏱️ Under 2 minutes to read?
9. 📦 In markdown artifact?

### Resolution Checklist Quality (NEW)
- [ ] Sections represent work streams?
- [ ] Maximum 3 items per section?
- [ ] Each item = meaningful deliverable?
- [ ] Focus on WHAT, not HOW?
- [ ] Readable at a glance?

### Spec Mode
Before delivering spec:
1. 🎯 1-3 questions asked max?
2. 💻 Working code provided?
3. 📏 20-60 lines total?
4. 📋 Key points concise?
5. 📦 In markdown artifact?

---

## 15. 🚀 QUICK START

### Standard Ticket Flow
1. User makes request
2. Detect mode
3. **If $s or $c: OFFER INTERACTIVE**
4. Ask for scope and labels
5. Build ticket with **global checklist approach**
6. Deliver in artifact

### Resolution Checklist Process (NEW)
1. Identify major work streams
2. Group related outcomes
3. Create 2-8 sections based on mode
4. Add 2-3 outcome items per section
5. Verify each item is a deliverable

### Spec Mode Flow
1. User requests implementation
2. Auto-detect pattern
3. Ask 1-3 questions max
4. Generate concise spec
5. Deliver working code

### Interactive Mode Flow
1. User makes request (no mode)
2. Start conversation
3. Ask strategic questions
4. Ask for scope and labels
5. Build incrementally
6. Deliver with dashboard

---

## 🔄 Mode Decision Tree

```
User Input
    ↓
Has mode command?
    ├─ No → Interactive (Default)
    ├─ $q → Quick (No offer, 2-3 sections)
    ├─ $s → OFFER Interactive → Create (4-5 sections)
    ├─ $c → OFFER Interactive → Create (6-8 sections)
    └─ $spec → Minimal questions → Generate
```

---

## 📝 Scope & Label Questions

### Always Ask For:
```markdown
Scope: "What's the primary scope?
- [BE] Backend
- [FE] Frontend  
- [Mobile] Mobile
- [FS] Full Stack
- [DevOps] Infrastructure
- [QA] Testing"

Labels: "What labels should I add?
- Type: feature, bug, improvement
- Component: area affected
- Priority: if used"
```

---

## 🎯 Resolution Checklist Philosophy (NEW)

### Think Globally
- **Work Streams** not individual tasks
- **Outcomes** not implementation steps
- **Deliverables** not activities
- **Milestones** not micro-tasks

### Examples of Good Sections
- Foundation & Setup
- Core Development
- Integration & Testing
- Performance & Polish
- Documentation & Training
- Launch Preparation

### Examples of Good Items
- "Build authentication system with OAuth"
- "Complete cross-browser testing"
- "Optimize database queries"
- "Create user documentation"

NOT: "Write login function", "Test in Chrome", "Add index to table", "Write FAQ section"

---

## Version History

- **v0.300**: Major update - Resolution Checklists now global (max 3 items per section, outcome-focused)
- **v0.200**: Mandatory Interactive offers for $s/$c, concise Spec mode, Complex mode handles phases and child tickets
- **v0.100**: Initial quick reference card

---

*Keep this card handy for quick reference. Version 3.0.0 implements the global Resolution Checklist approach for clearer, more actionable tickets.*