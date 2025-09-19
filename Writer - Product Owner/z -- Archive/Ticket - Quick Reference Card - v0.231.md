# Ticket - Quick Reference Card - v0.231

Daily companion for creating professional development tickets with developer clarity.

## 📌 Description

Quick access to commonly needed information for ticket creation:
- **Quick lookups** during creation
- **Mode selection** guidance
- **Interactive offer** reminders
- **Format reference** with distinctions
- **Resolution checklist** sizing
- **Spec mode** patterns
- **Quality verification**

Keep this open while writing tickets.

## 📑 Table of Contents

1. [🚀 MODE ACTIVATION](#1--mode-activation)
2. [🎯 INTERACTIVE OFFERS](#2--interactive-offers)
3. [📤 ESSENTIAL SYMBOLS](#3--essential-symbols)
4. [📋 TICKET STRUCTURE](#4--ticket-structure)
5. [✍️ WRITING RULES](#5--writing-rules)
6. [🎯 QUICK PATTERNS](#6--quick-patterns)
7. [🚨 MCP SELECTION](#7--mcp-selection)
8. [💬 MODE RESPONSES](#8--mode-responses)
9. [✓ RESOLUTION SIZING](#9--resolution-sizing)
10. [💻 SPEC FAST PATHS](#10--spec-fast-paths)
11. [🔗 QUICK LINKS](#11--quick-links)
12. [⚡ COMMON COMMANDS](#12--common-commands)
13. [📝 FORMAT HIERARCHY](#13--format-hierarchy)
14. [✅ QUALITY CHECKLIST](#14--quality-checklist)
15. [🚀 QUICK START](#15--quick-start)

---

## 1. 🚀 MODE ACTIVATION

| Mode | Command | When | Sections | Items/Sec | Total | Offer |
|------|---------|------|----------|-----------|-------|-------|
| **Interactive** | DEFAULT | No mode | Adaptive | 2-3 | Adaptive | N/A |
| **Quick** | `$q` | Simple | 2-3 | 2-3 | 4-6 | No |
| **Standard** | `$s` | Full | 4-5 | 2-3 | 8-12 | **YES** |
| **Complex** | `$c` | Major | 6-8 | 2-3 | 12-20 | **YES** |
| **Spec** | `$spec` | Frontend | N/A | N/A | 20-60 lines | No |

**Remember:** 
- Interactive is DEFAULT
- **ALWAYS offer Interactive** for $s/$c
- Complex handles phases AND child tickets
- Spec: 1-3 questions max
- **First heading always "About" with ⌘ icon**
- **Checkboxes use `[]` format**
- **Add dividers between requirement subsections**
- **20% more concise than v4.1**

---

## 2. 🎯 INTERACTIVE OFFERS

### Standard Mode ($s):
```markdown
I see you want a standard ticket for [feature].

Would you like me to:
1. **Guide you through it** - Ask questions for completeness
2. **Create directly** - Use my judgment

Which? (1 or 2)
```

### Complex Mode ($c):
```markdown
I see you want a complex ticket for [feature].

This is substantial! Would you like me to:
1. **Walk through it interactively** - Think through all aspects
2. **Create directly** - Structure it myself

Interactive helps ensure completeness. Preference? (1 or 2)
```

### Response:
- **If 1**: Start conversation
- **If 2**: Ask scope and labels

---

## 3. 📤 ESSENTIAL SYMBOLS

```markdown
⌘  "About" heading and sections
◇  Requirements
◊  Sub-headings (bold)
→  Designs & References
✦  Success criteria (bullets only)
✓  Resolution Checklist (checkboxes only with [] format)
⊗  Dependencies
⚠  Risks
⚠️  Key problems
≈  Reasons why
—  Sub-categories under ◊
```

**Spec Mode**: Minimal symbols, clean markdown

---

## 4. 📋 TICKET STRUCTURE

### Standard Components
1. **Artifact Title**: `[SCOPE] Feature Name`
2. **First Heading**: `# ⌘ About`
3. **Description**: Brief with ⚠️ and ≈
4. **User Value**: What users gain
5. **Business Goal**: Measurable outcome
6. **Requirements**: WHAT not HOW (with dividers)
7. **Success Criteria**: ✦ bullets only
8. **Resolution**: ✓ checkboxes only (max 3/section, `[]` format)
9. **Dependencies**: If any
10. **Labels**: User-specified

### Complex Options
- **Option A: Phased** - Incremental
- **Option B: Child Tickets** - Multi-team

### Spec Structure
1. **Objective**: 1-2 sentences
2. **Implementation**: Working code
3. **Browser Compatibility**: If needed
4. **Key Points**: Essential only

---

## 5. ✍️ WRITING RULES

### ✅ Always
- Offer Interactive for $s/$c
- Ask for scope ([BE], [FE], etc.)
- Ask for labels
- **First heading "About" with ⌘**
- Write brief description
- Use ✓ for Resolution (checkboxes with `[]`)
- Use ✦ for Success (bullets)
- Keep under 2 minutes
- Focus on outcomes
- **Be 20% more concise**
- **Add dividers between ◊ subsections**

### ❌ Never
- Skip Interactive offer
- Assume scope/labels
- Use percentages
- Mix features
- Skip sections
- Include placeholders
- Create task lists
- Exceed 3 items/section
- Mix ✦ and ✓
- Use space in checkbox brackets

### 🔧 Resolution Rules (✓)
- Think **work streams**
- Each checkbox = **deliverable**
- Max **3 items/section**
- Focus on **WHAT**, not HOW
- Each item = **2-8 hours minimum**
- Use `[]` format (no space)

---

## 6. 🎯 QUICK PATTERNS

### Title Formats
**Artifact**: `[BE] User Authentication`
**Body**: `# ⌘ About`

### Description Pattern
```markdown
[Brief context]

⚠️ **Key problems:**
* **Issue** - Description
* **Problem** - Impact

≈ **Reasons why:**
[Solution and benefits]
```

### Success Criteria (✦)
```markdown
## ✦ Success Criteria
- Feature works
- Performance met
- User completes task
```

### Resolution Checklist (✓)
```markdown
## ✓ Resolution Checklist

### Work Stream
[] Outcome 1
[] Outcome 2
```

### Requirements with Dividers
```markdown
## ◇ Requirements

**◊ Interface**
— Components
• Updates

---

**◊ Backend**
— API
• Endpoints
```

### Spec Pattern
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
Simple + $q → Sequential (1-2 thoughts)
Standard + $s → Sequential (2-3 thoughts)
Spec + $spec → Sequential (1-2 thoughts)
Interactive → Cascade (3-5 thoughts)
Complex/unclear → Cascade (3-5+ thoughts)
+ UI features → Add Figma (optional)
```

---

## 8. 💬 MODE RESPONSES

**Interactive**: "Let's create a great ticket! 🤔"
**Quick**: "Quick ticket! ⚡"
**Standard**: "Would you like: 1. Guidance 2. Direct?"
**Complex**: "This is substantial! 1. Interactive 2. Direct?"
**Spec**: "Let me create that spec. [1-3 questions]"

---

## 9. ✓ RESOLUTION SIZING

| Mode | Sections | Items/Sec | Total | Focus |
|------|----------|-----------|-------|-------|
| **Quick** | 2-3 | 2-3 | 4-6 | Essential |
| **Standard** | 4-5 | 2-3 | 8-12 | Complete |
| **Complex-Phased** | 6-8 | 2-3 | 12-20 | Milestones |
| **Complex-Child** | 5-6 | 2-3 | 10-15 | Coordination |
| **Bug** | 3-4 | 2-3 | 6-10 | Fix & verify |
| **Improvement** | 4-5 | 2-3 | 8-12 | Optimize |

### Section Names
- **Foundation Work** (not "Setup")
- **Core Development** (not "Implementation")
- **Testing & Validation** (not "Tests")

### Item Examples
✅ **Good**: "[] Build filter components with state"
❌ **Bad**: "[] Create FilterComponent.tsx"

---

## 10. 💻 SPEC FAST PATHS

### Instant (0 Questions)
```
"hide scrollbar" → CSS
"center div" → CSS
"debounce input" → JS utility
"format date" → JS utility
```

### Quick (1-2 Questions)
```
"button component" → Framework?
"data table" → Rows? Framework?
"form validation" → Framework? Inline/toast?
```

### Standard (3-4 Questions Max)
```
"virtual scroll" → Rows? Framework? Selection?
"real-time collab" → Users? Framework? Offline?
```

### Output Targets
- Simple: 20-30 lines
- Component: 30-45 lines
- Complex: 45-60 lines
- Never exceed: 75 lines

---

## 11. 🔗 QUICK LINKS

- **Templates** → Templates & Standards.md
- **Examples** → Examples Library.md
- **Interactive** → Interactive Mode.md
- **Spec patterns** → Spec Mode.md
- **System rules** → Writer - Dev Tickets.md

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
```

---

## 13. 📝 FORMAT HIERARCHY

### Standard Tickets
```markdown
# ⌘ About
## ◇ Requirements
**◊** Sub-heading
— Sub-category
• Bullet

---

**◊** Next Sub-heading
— Sub-category

## ✦ Success Criteria
- Metric (bullets only)

## ✓ Resolution Checklist
### Stream
[] Outcome (checkboxes only, no space)
```

### Rules
- **✦** Success: bullets only
- **✓** Resolution: checkboxes only with `[]`
- Never mix formats
- **First heading always "About" with ⌘**
- **Dividers between ◊ subsections**

---

## 14. ✅ QUALITY CHECKLIST

### All Tickets
1. 🎯 First heading "About" with ⌘?
2. 🎯 Interactive offered for $s/$c?
3. 🏷️ Scope specified by user?
4. 🏷️ Labels specified by user?
5. 📝 Brief description with ⚠️ ≈?
6. ⌘ Symbols in sections?
7. ✦ Success with bullets only?
8. ✓ Resolution with checkboxes only (`[]` format)?
9. 🎯 Each item = outcome?
10. ⏱️ Under 2 minutes?
11. 📦 In markdown artifact?
12. ➖ Dividers between ◊ subsections?

### Format Verification
- [ ] ✦ ONLY for Success (bullets)?
- [ ] ✓ ONLY for Resolution (checkboxes with `[]`)?
- [ ] No mixing?
- [ ] First heading "About" with ⌘?
- [ ] Dividers between requirements?

### Resolution Quality (✓)
- [ ] Work streams?
- [ ] Max 3 items/section?
- [ ] Meaningful deliverables?
- [ ] Focus on WHAT?
- [ ] Using `[]` format?

### Spec Mode
1. 🎯 1-3 questions max?
2. 💻 Working code?
3. 📝 20-60 lines?
4. 📋 Key points concise?
5. 📦 In markdown artifact?

---

## 15. 🚀 QUICK START

### Standard Flow
1. User request
2. Detect mode
3. **If $s/$c: OFFER INTERACTIVE**
4. Ask scope and labels
5. Build with ✓ Resolution (`[]` format)
6. Add ✦ Success
7. Add dividers between ◊ subsections
8. Deliver artifact

### Resolution Process (✓)
1. Identify work streams
2. Group outcomes
3. Create 2-8 sections
4. Add 2-3 items/section
5. Verify deliverables
6. Use ✓ with checkboxes (`[]` format)

### Success Process (✦)
1. Define measurable metrics
2. Create 3-5 bullets
3. Focus on outcomes
4. Use ✦ with bullets

### Spec Flow
1. User requests implementation
2. Auto-detect pattern
3. Ask 1-3 questions max
4. Generate concise spec
5. Deliver working code

### Interactive Flow
1. User request (no mode)
2. Start conversation
3. Ask strategic questions
4. Ask scope and labels
5. Build incrementally
6. Deliver with dashboard

---

## 📄 Mode Decision Tree

```
User Input
    ↓
Has mode?
    ├─ No → Interactive (Default)
    ├─ $q → Quick (No offer, 2-3 sections)
    ├─ $s → OFFER Interactive → Create (4-5)
    ├─ $c → OFFER Interactive → Create (6-8)
    └─ $spec → Minimal questions → Generate
```

---

## 📝 Scope & Labels

### Always Ask:
```markdown
Scope: "What's the primary scope?
- [BE] Backend
- [FE] Frontend  
- [Mobile] Mobile
- [FS] Full Stack
- [DevOps] Infrastructure
- [QA] Testing"

Labels: "What labels?
- Type: feature, bug, improvement
- Component: area affected
- Priority: if used"
```

---

## 🎯 Format Reference

| Symbol | Usage | Section | Purpose | Format |
|--------|-------|---------|---------|--------|
| **✦** | Success | ## ✦ Success Criteria | Measurable success | Bullets only |
| **✓** | Resolution | ## ✓ Resolution Checklist | Work to complete | Checkboxes only (`[]`) |
| **⌘** | About | # ⌘ About | First heading | Symbol + text |
| **◇** | Requirements | ## ◇ Requirements | Feature requirements | Symbol + text |
| **---** | Divider | Between ◊ subsections | Visual separation | Markdown divider |

### Resolution Philosophy (✓)

**Think Globally:**
- Work Streams not tasks
- Outcomes not steps
- Deliverables not activities
- Milestones not micro-tasks

**Good Sections:**
- Foundation & Setup
- Core Development
- Integration & Testing
- Performance & Polish
- Documentation & Training

**Good Items:**
- "[] Build authentication with OAuth"
- "[] Complete cross-browser testing"
- "[] Optimize database queries"

NOT: "[] Write login function", "[] Test in Chrome", "[] Add index"

---

## Version History

- **v0.421**: Updated About icon (⌘), checkbox format `[]`, requirement dividers
- **v0.420**: First heading "About", 20% more concise throughout
- **v0.410**: Updated formatting distinctions
- **v0.400**: Mandatory Interactive offers, concise Spec mode

---

*Keep this card handy for quick reference. Remember: First heading always "About" with ⌘, be 20% more concise, use `[]` for checkboxes, add dividers between requirement subsections.*