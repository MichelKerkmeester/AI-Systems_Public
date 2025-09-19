# Ticket - Quick Reference Card - v0.250

Daily companion for creating professional development tickets and documentation with developer clarity and platform integration.

## 📌 Description

Quick access to commonly needed information for ticket and documentation creation:
- **Quick lookups** during creation
- **Mode selection** guidance (now with $doc)
- **Interactive offer** reminders
- **Format reference** with distinctions
- **Resolution checklist** sizing
- **Documentation structure** patterns
- **Platform integration** steps
- **Spec mode** patterns
- **Quality verification**

Keep this open while writing tickets or documentation.

## 📑 Table of Contents

1. [🚀 MODE ACTIVATION](#1--mode-activation)
2. [🎯 INTERACTIVE OFFERS](#2--interactive-offers)
3. [📤 ESSENTIAL SYMBOLS](#3--essential-symbols)
4. [📋 TICKET STRUCTURE](#4--ticket-structure)
5. [📚 DOCUMENTATION STRUCTURE](#5--documentation-structure)
6. [✏️ WRITING RULES](#6--writing-rules)
7. [🎯 QUICK PATTERNS](#7--quick-patterns)
8. [🚨 MCP SELECTION](#8--mcp-selection)
9. [💬 MODE RESPONSES](#9--mode-responses)
10. [✓ RESOLUTION SIZING](#10--resolution-sizing)
11. [🔗 PLATFORM INTEGRATION](#11--platform-integration)
12. [💻 SPEC FAST PATHS](#12--spec-fast-paths)
13. [📔 DOC PATTERNS](#13--doc-patterns)
14. [🔗 QUICK LINKS](#14--quick-links)
15. [⚡ COMMON COMMANDS](#15--common-commands)
16. [📝 FORMAT HIERARCHY](#16--format-hierarchy)
17. [✅ QUALITY CHECKLIST](#17--quality-checklist)
18. [🚀 QUICK START](#18--quick-start)

---

## 1. 🚀 MODE ACTIVATION

| Mode | Command | When | Sections | Items/Sec | Total | Offer |
|------|---------|------|----------|-----------|-------|-------|
| **Interactive** | DEFAULT | No mode | Adaptive | 2-3 | Adaptive | N/A |
| **Quick** | `$q` | Simple | 2-3 | 2-3 | 4-6 | No |
| **Standard** | `$s` | Full | 4-5 | 2-3 | 8-12 | **YES** |
| **Complex** | `$c` | Major | 6-8 | 2-3 | 12-20 | **YES** |
| **Spec** | `$spec` | Frontend | N/A | N/A | 20-60 lines | No |
| **Documentation** | `$doc` | User guides | 3-5 | N/A | N/A | No |

**Remember:** 
- Interactive is DEFAULT
- **ALWAYS offer Interactive** for $s/$c
- Complex handles phases AND child tickets
- Spec: 1-3 questions max
- Doc: User-focused guides
- **First heading always "About" with ⌘ icon** (or "Overview" for docs)
- **Checkboxes use `[]` format**
- **Add dividers between requirement subsections**
- **Always offer platform integration after ticket/doc**
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
- **If 2**: Ask scope and labels (except $doc)

---

## 3. 📤 ESSENTIAL SYMBOLS

```markdown
⌘  "About"/"Overview" heading and sections
◇  Requirements (tickets)
◻️ Features (documentation)
◊  Sub-headings (bold)
→  Designs & References
✦  Success criteria (bullets only)
✓  Resolution Checklist (checkboxes only with [] format)
⊗  Dependencies
⚠  Risks
⚠️ Key problems
≈  Reasons why
📚 Additional resources (docs)
—  Sub-categories under ◊
```

**Mode-specific:**
- Tickets: ◇ for requirements
- Docs: ◻️ for features
- Spec: Minimal symbols

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

### After Ticket (In Chat):
11. **Platform Offer**: ClickUp/Notion/Skip

### Complex Options
- **Option A: Phased** - Incremental
- **Option B: Child Tickets** - Multi-team

### Spec Structure
1. **Objective**: 1-2 sentences
2. **Implementation**: Working code
3. **Browser Compatibility**: If needed
4. **Key Points**: Essential only

---

## 5. 📚 DOCUMENTATION STRUCTURE

### Documentation Components
1. **Artifact Title**: `[Product] Documentation`
2. **First Heading**: `# ⌘ Overview`
3. **Target Audience**: End users/Internal/Both
4. **Complexity**: Basic/Intermediate/Advanced
5. **Version**: Semantic versioning
6. **Features**: ◻️ sections with ◊ components
7. **Related Materials**: Screenshots, tutorials
8. **Important Notes**: Limitations, tips
9. **Additional Resources**: Links, guides

### Feature Section Pattern
```markdown
### ◻️ Feature Name

[What users can accomplish]

**◊ Getting Started**
— Prerequisites
• Requirements

**◊ Core Functionality**
— Main Capabilities
• Key workflows

**◊ Tips & Best Practices**
— Recommendations
• Pro tips
```

### After Documentation (In Chat):
**Platform Offer**: Notion (KB)/ClickUp (Help)/Skip

---

## 6. ✏️ WRITING RULES

### ✅ Always
- Offer Interactive for $s/$c
- Ask for scope ([BE], [FE], etc.) - except $doc
- Ask for labels (tickets only)
- **First heading "About" with ⌘** (tickets)
- **First heading "Overview" with ⌘** (docs)
- Write brief description
- Use ✓ for Resolution (checkboxes with `[]`)
- Use ✦ for Success (bullets)
- Use ◻️ for Doc features
- Keep under 2 minutes
- Focus on outcomes
- **Be 20% more concise**
- **Add dividers between ◊ subsections**
- **Offer platform integration after creation**

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
- Put platform offer in artifact

### 📧 Resolution Rules (✓)
- Think **work streams**
- Each checkbox = **deliverable**
- Max **3 items/section**
- Focus on **WHAT**, not HOW
- Each item = **2-8 hours minimum**
- Use `[]` format (no space)

---

## 7. 🎯 QUICK PATTERNS

### Title Formats
**Ticket Artifact**: `[BE] User Authentication`
**Doc Artifact**: `Analytics Dashboard Documentation`
**Body**: `# ⌘ About` or `# ⌘ Overview`

### Description Pattern (Tickets)
```markdown
[Brief context]

⚠️ **Key problems:**
* **Issue** - Description
* **Problem** - Impact

≈ **Reasons why:**
[Solution and benefits]
```

### Overview Pattern (Docs)
```markdown
[Product description and purpose]

**Target Audience:** [Users]
**Complexity:** [Level]
**Version:** [1.0.0]
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

### Documentation Features (◻️)
```markdown
### ◻️ Feature Name

[User benefit]

**◊ Getting Started**
— Setup
• Steps

**◊ Core Usage**
— Workflow
• Actions
```

---

## 8. 🚨 MCP SELECTION

```
Simple + $q → Sequential (1-2 thoughts)
Standard + $s → Sequential (2-3 thoughts)
Documentation + $doc → Sequential (2-3 thoughts)
Spec + $spec → Sequential (1-2 thoughts)
Interactive → Cascade (3-5 thoughts)
Complex/unclear → Cascade (3-5+ thoughts)
+ UI features → Add Figma (optional)
```

---

## 9. 💬 MODE RESPONSES

**Interactive**: "Let's create a great ticket! 🤔"
**Quick**: "Quick ticket! ⚡"
**Standard**: "Would you like: 1. Guidance 2. Direct?"
**Complex**: "This is substantial! 1. Interactive 2. Direct?"
**Spec**: "Let me create that spec. [1-3 questions]"
**Documentation**: "Let's document this feature! 📚"
**Platform**: "📦 Add to your workspace?" (after creation, in chat)

---

## 10. ✓ RESOLUTION SIZING

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

## 11. 🔗 PLATFORM INTEGRATION

### After Every Ticket/Doc (In Chat):
```markdown
📦 **Add to your workspace?**

1. **ClickUp** - Task management, sprints, time tracking
2. **Notion** - Documentation, knowledge base, wikis
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

### For Documentation:
- **Prefer Notion** for knowledge bases
- **ClickUp** for help center articles
- **Skip** for standalone docs

### User Selects Platform:
**ClickUp (1):**
```markdown
✅ Passing your [ticket/doc] to ClickUp...
[ClickUp MCP handles creation]
```

**Notion (2):**
```markdown
✅ Passing your [ticket/doc] to Notion...
[Notion MCP handles creation]
```

**Skip (3):**
```markdown
✅ [Ticket/Documentation] saved as artifact for manual use
```

### MCP Not Available:
```markdown
⚠️ [Platform] MCP not available

Options:
1. Try the other platform
2. Copy formatted text for manual entry
3. Keep as artifact only

Your choice? (1/2/3)
```

---

## 12. 💻 SPEC FAST PATHS

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

## 13. 📔 DOC PATTERNS

### Interactive Questions
1. **Audience?** (end users/internal/both)
2. **Feature name?**
3. **How many features?** (1-5)
4. **List features?**
5. **Depth?** (overview/detailed/comprehensive)
6. **Screenshots?** (none/key/all)

### Depth Guidelines
| Level | Paragraphs | Components | Tips | Links |
|-------|------------|------------|------|-------|
| **Overview** | 1-2 | Core only | Few | Minimal |
| **Detailed** | 3-4 | Most | Some | Yes |
| **Comprehensive** | 5+ | All | Many | Complete |

### Common Documentation Types
- **Feature Docs**: How to use specific features
- **Getting Started**: Onboarding new users
- **User Guides**: Complete workflows
- **Release Notes**: What's new
- **FAQs**: Common questions

---

## 14. 🔗 QUICK LINKS

- **Templates** → Ticket - Templates & Standards.md
- **Examples** → Ticket - Examples Library.md
- **Interactive** → Ticket - Interactive Mode.md
- **Documentation** → Ticket - Documentation Mode.md
- **Spec patterns** → Ticket - Spec Mode.md
- **Platform Integration** → Ticket - Platform Integration.md
- **System rules** → Writer - Dev Tickets.md

---

## 15. ⚡ COMMON COMMANDS

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

# Documentation (user guides)
$doc analytics dashboard

# After any creation
[Platform offer appears in chat]
```

---

## 16. 📝 FORMAT HIERARCHY

### Tickets
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

### Documentation
```markdown
# ⌘ Overview
## ⌘ Features
### ◻️ Feature Name
**◊** Component
— Category
• Detail

## → Related Materials
## ⚠️ Important Notes
## 📚 Additional Resources
```

### Rules
- **✦** Success: bullets only
- **✓** Resolution: checkboxes only with `[]`
- **◻️** Features: documentation only
- Never mix formats
- **First heading always has ⌘**
- **Dividers between ◊ subsections**

---

## 17. ✅ QUALITY CHECKLIST

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
13. 🔗 Platform offer in chat (not artifact)?

### Documentation
1. 🎯 First heading "Overview" with ⌘?
2. 👥 Audience specified?
3. 📊 Version included?
4. ◻️ Features use correct symbol?
5. 📚 Resources included?
6. ⚠️ Limitations noted?
7. 📷 Visual references mentioned?
8. 🔗 Platform offer in chat?

### Format Verification
- [ ] ✦ ONLY for Success (bullets)?
- [ ] ✓ ONLY for Resolution (checkboxes with `[]`)?
- [ ] ◻️ ONLY for Doc features?
- [ ] No mixing symbols?
- [ ] First heading has ⌘?
- [ ] Dividers between requirements?
- [ ] Platform offer after creation?

### Platform Integration
- [ ] Offer presented after creation?
- [ ] In chat, not artifact?
- [ ] Three options clear?
- [ ] Doc prefers Notion?

### Spec Mode
1. 🎯 1-3 questions max?
2. 💻 Working code?
3. 📝 20-60 lines?
4. 📋 Key points concise?
5. 📦 In markdown artifact?

---

## 18. 🚀 QUICK START

### Standard Ticket Flow
1. User request
2. Detect mode
3. **If $s/$c: OFFER INTERACTIVE**
4. Ask scope and labels
5. Build with ✓ Resolution (`[]` format)
6. Add ✦ Success
7. Add dividers between ◊ subsections
8. Deliver artifact
9. **Offer platform integration in chat**
10. Handle platform selection

### Documentation Flow
1. User request with $doc
2. Ask audience
3. Ask feature count
4. List features
5. Ask depth level
6. Ask about visuals
7. Build with ◻️ features
8. Add resources
9. Deliver artifact
10. **Offer platform (prefer Notion)**

### Resolution Process (✓)
1. Identify work streams
2. Group outcomes
3. Create 2-8 sections
4. Add 2-3 items/section
5. Verify deliverables
6. Use ✓ with checkboxes (`[]` format)

### Documentation Process (◻️)
1. Define features
2. Create ◻️ sections
3. Add ◊ components
4. Include tips
5. Add resources
6. Note limitations

### Platform Process
1. Complete ticket/doc artifact
2. Display in conversation
3. Offer platform options (in chat)
4. User selects 1/2/3
5. Pass to MCP or skip
6. Confirm action

### Spec Flow
1. User requests implementation
2. Auto-detect pattern
3. Ask 1-3 questions max
4. Generate concise spec
5. Deliver working code
6. Offer platform (if applicable)

### Interactive Flow
1. User request (no mode)
2. Start conversation
3. Ask strategic questions
4. Ask scope and labels (tickets)
5. Build incrementally
6. Deliver with dashboard
7. Offer platform integration

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
    ├─ $spec → Minimal questions → Generate
    └─ $doc → Interactive questions → Document
         ↓
    All modes
         ↓
    Creation Complete
         ↓
    Platform Offer (in chat)
         ↓
    ClickUp / Notion / Skip
```

---

## 📝 Scope & Labels

### Always Ask (Tickets):
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

### Always Ask (Docs):
```markdown
Audience: "Who will read this?
- End users
- Internal team
- Both"

Depth: "Documentation depth?
- Overview (1-2 paragraphs)
- Detailed (step-by-step)
- Comprehensive (all details)"
```

---

## 🎯 Format Reference

| Symbol | Usage | Section | Purpose | Format |
|--------|-------|---------|---------|--------|
| **✦** | Success | ## ✦ Success Criteria | Measurable success | Bullets only |
| **✓** | Resolution | ## ✓ Resolution Checklist | Work to complete | Checkboxes only (`[]`) |
| **⌘** | About/Overview | # ⌘ About/Overview | First heading | Symbol + text |
| **◇** | Requirements | ## ◇ Requirements | Feature requirements | Symbol + text |
| **◻️** | Doc Features | ### ◻️ Feature | Documentation sections | Symbol + text |
| **---** | Divider | Between ◊ subsections | Visual separation | Markdown divider |
| **📦** | Platform | After creation (chat) | Integration offer | In conversation |
| **📚** | Resources | ## 📚 Additional Resources | External links | Symbol + text |

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

*Keep this card handy for quick reference. Remember: First heading always has ⌘, be 20% more concise, use `[]` for checkboxes, add dividers between requirement subsections, use ◻️ for doc features, and always offer platform integration after creation (in chat, not artifact).*