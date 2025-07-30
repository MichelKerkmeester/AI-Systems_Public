# Ticket Patterns & Methodology

Full specification of ticket writing patterns, methodologies, and best practices for creating effective development tickets.

## Table of Contents

1. [🔍 CLARIFYING QUESTIONS](#1--clarifying-questions)
2. [🔄 PATTERN TRANSFORMATIONS](#2--pattern-transformations)
3. [🎨 PARTIAL INPUT ENHANCEMENT](#3--partial-input-enhancement)
4. [📋 FORMATTING PATTERNS](#4--formatting-patterns)
5. [✅ QUALITY CHECKLIST](#5--quality-checklist)
6. [🎯 COMMON SCENARIOS](#6--common-scenarios)
7. [⚠️ ANTI-PATTERNS TO AVOID](#7-️-anti-patterns-to-avoid)
8. [🧭 MODE SELECTION FLOWCHART](#8--mode-selection-flowchart)
9. [💬 RESPONSE TEMPLATES](#9--response-templates)
10. [🏎️ QUICK REFERENCE](#10-️-quick-reference)

---

## 1. 🔍 CLARIFYING QUESTIONS

### 💭 When You Need More Info

**Vague Request:** "Make the dashboard better"

**Response:**
```
I need some clarification to write an effective ticket:

What specific problems are users having with the current dashboard?

Once I understand the pain points, I can create a focused ticket with clear success criteria.

Or try $interactive mode for guided ticket creation!
```

---

**Missing Context:** "Add export feature"

**Response:**
```
To create a complete ticket, I need to know:

What data should users be able to export, and in what formats?

This will help me define clear requirements and success criteria.
```

---

**Too Broad:** "Redesign the whole app"

**Response:**
```
This sounds like multiple features. To keep tickets actionable, should we:

1. Start with the highest-priority area?
2. Create an epic with multiple tickets?
3. Use $interactive mode to break this down together?

What would have the most impact for users right now?
```

---

## 2. 🔄 PATTERN TRANSFORMATIONS

### 📐 Complex Features → Phased Tickets

Instead of one massive ticket, break into phases with clear boundaries:

#### Phase-Based Ticket Pattern

```markdown
### ❖ Feed Personalization System

**User Value:** See the most relevant content first, every time

**Business Goal:** Increase daily active users by 30%

---

## ◇ Phase 1: Data Collection (Week 1-2)
- Track user interactions with feed items
- Store preference signals
- Basic analytics dashboard

---

## ◇ Phase 2: Algorithm Implementation (Week 3-4)
- Personalization engine based on behavior
- A/B test framework
- Fallback to default feed

---

## ◇ Phase 3: Optimization (Week 5-6)
- Machine learning improvements
- Real-time adjustments
- Performance tuning

---

## ✓ Success Criteria
- [ ] 30% increase in session duration
- [ ] 50% more interactions per session
- [ ] <100ms added latency

---

## → Designs & References
- [Figma - Personalized Feed](link)
- [Algorithm Documentation](link)

---

## ⊗ Dependencies
- Requires: User tracking infrastructure (#2001)
- Requires: A/B testing framework (#2002)
```

---

### 🔧 Monolithic → Modular Pattern

Transform large requests into digestible pieces:

**Before:** "Build complete analytics dashboard"

**After:** 
1. Core Metrics Display
2. Date Range Selection
3. Data Export Feature
4. Real-time Updates
5. Custom Report Builder

Each becomes a standalone ticket with clear value.

---

## 3. 🎨 PARTIAL INPUT ENHANCEMENT

### 📋 From Lists to Tickets

When users provide technical lists or incomplete specifications, intelligently enhance them:

**Technical List Input:**
```
Add filters:
- Category
- Date
- Status
```

**Enhanced to Full Ticket:**
- Extract clear requirements
- Add missing user value
- Infer business goals
- Generate success criteria
- Note what needs design

See **Ticket Examples - Partial Input Handling.md** for comprehensive patterns.

---

### 🖼️ Visual Input Processing

**Screenshot/Design Input Patterns:**

| Visual Element | Extract as Requirement |
|----------------|------------------------|
| Button | User action + outcome |
| Form field | Data input + validation |
| Chart | Data viz + interaction |
| Filter | Selection + persistence |
| Navigation | User flow + states |

**Key Principles:**
- Mark extracted requirements as **"Extracted from screenshot:"**
- Flag inferences with **"Inferred:"**
- Note gaps with **"Needs:"**
- Mode determines enhancement depth

---

### 🔄 Mode-Specific Enhancement

Same partial input enhances differently by mode:

- **$interactive:** Guide through conversation
- **$q (Quick):** Minimal viable enhancement
- **$s (Standard):** Balanced enhancement with dependencies
- **$c (Complex):** Deep analysis with phases
- **$e (Epic):** Identify hidden child tickets

---

## 4. 📋 FORMATTING PATTERNS

### ➡️ Arrow Notation Usage

Use arrows (`→`) to show cause and effect or user flows:

```markdown
## ◇ Requirements
- **Click filter** → Results update instantly
- **Hover on chart** → Show detailed tooltip
- **Save changes** → Confirmation message appears
- **Error occurs** → Display helpful message
```

---

### 📌 Notice Callouts

For critical information that might be missed:

```markdown
## → Designs & References
- [Figma - Feature](link)

**Notice:** Component headers contain implementation notes

**Notice:** Mobile view uses different layout approach

**Notice:** Max 10 concurrent users per session
```

---

### 🔀 Logic Sections

When behavior has conditional paths:

```markdown
### ◇ Logic:
- **IF new user (<5 actions)** → Show onboarding
- **IF returning user** → Show dashboard
- **IF error occurs** → Display helpful message
- **IF offline** → Enable read-only mode
```

---

### 📊 Nested Information

For related but detailed specs:

```markdown
## ◇ Requirements
- Resizable columns
  - Default: 240px
  - Min: 120px  
  - Max: unlimited
  - Double-click: auto-fit
- Persistent settings
  - Store in user preferences
  - Apply on next visit
  - Reset option available
```

---

## 5. ✅ QUALITY CHECKLIST

Before delivering any ticket, verify:

### ❖ Structure & Format
- [ ] Has `---` dividers between all sections?
- [ ] Uses abstract symbols throughout (no emojis)?
- [ ] Follows correct section order?
- [ ] Links instead of describing designs?

### 📝 Content Quality
- [ ] Can be read in under 2 minutes?
- [ ] Clear user value in first section?
- [ ] Requirements are outcomes, not solutions?
- [ ] Success criteria are measurable?
- [ ] Would a developer know what "done" looks like?

### ✓ Completeness
- [ ] Dependencies noted with ticket numbers?
- [ ] Proper mode selected for complexity?
- [ ] Is this one deployable unit?
- [ ] All edge cases considered?

### 🎨 Partial Input Handling
- [ ] Extracted all clear requirements from input?
- [ ] Marked assumptions appropriately?
- [ ] Asked for critical missing info?
- [ ] Enhanced based on correct mode?
- [ ] Suggested $interactive if too vague?

If any answer is "no," revise before delivering.

---

## 6. 🎯 COMMON SCENARIOS

### 📈 Scenario: Performance Request

**Request:** "Make it faster"

**Ticket Pattern:**
```markdown
### ❖ [Feature] Performance Optimization

**User Value:** [Specific action] completes 3x faster

**Business Goal:** [Metric improvement]

---

## ◈ Current Performance
- Metric: [current value]
- User impact: [pain point]

---

## ◆ Target Performance  
- Metric: [target value]
- Measurement method: [how to verify]

---

## ◇ Requirements
[Specific optimizations]

---

## ✓ Success Criteria
- [ ] [Measurable outcome]
```

---

### 🔌 Scenario: New Integration

**Request:** "Connect to [Service]"

**Ticket Pattern:**
```markdown
### ❖ [Service] Integration

**User Value:** [What users can do with integration]

**Business Goal:** [Why this integration matters]

---

## ◇ Requirements
- Authentication flow
- Data sync capabilities
- Error handling
- Disconnect option

---

## → Designs & References
- [Figma - Integration Flow](link)
- [API Documentation](link)

---

## ✓ Success Criteria
- [ ] Successful connection rate >95%
- [ ] Data syncs within 30 seconds
- [ ] Clear error messages
- [ ] Secure credential storage
```

---

## 7. ⚠️ ANTI-PATTERNS TO AVOID

### ❌ Over-Specification
**Wrong:** "Use React hooks with Redux for state management"
**Right:** "Maintain user selections across sessions"

### ❌ Technical Solutioning  
**Wrong:** "Implement WebSocket connections"
**Right:** "Show real-time updates without refresh"

### ❌ Vague Success Criteria
**Wrong:** "It should work well"
**Right:** "Page loads in under 2 seconds for 95% of users"

### ❌ Missing User Value
**Wrong:** "Upgrade to latest framework"
**Right:** "Reduce app crashes by 90% for better reliability"

### ❌ Bundled Features
**Wrong:** "Add search, filters, sorting, and export"
**Right:** Create separate tickets for each feature

### ❌ Ignoring Partial Input
**Wrong:** Asking user to rewrite their input completely
**Right:** Extract what's useful, enhance intelligently, ask for gaps

---

## 8. 🧭 MODE SELECTION FLOWCHART

```
How complex is the feature?
│
├─ DEFAULT: Start with Interactive Mode
│  └─ Use $interactive for guided creation
│
├─ User explicitly requests quick?
│  └─ Yes → $q (Quick Mode)
│
├─ User explicitly requests standard?
│  └─ Yes → $s (Standard Mode)
│
├─ User explicitly requests complex?
│  └─ Yes → $c (Complex Mode)
│
└─ User explicitly requests epic?
   └─ Yes → $e (Epic Mode)

Note: Interactive mode is the default. Other modes require explicit request.
```

---

## 9. 💬 RESPONSE TEMPLATES

### ✅ When request is perfect:
"Here's your ticket, ready for sprint planning:"
[Artifact with ticket]

### 🤔 When clarification needed:
"I need one detail to complete this ticket: [specific question]"

### 🤝 When too vague:
"This needs more context. Try $interactive mode for guided ticket creation!"

### 📊 When suggesting split:
"This sounds like 3 separate features. Would you like:
1. One epic with child tickets?
2. Just the highest priority feature?
3. All three as separate tickets?
4. Use $interactive to explore together?"

### 🎨 When design missing:
"I've created the ticket structure. Note that we'll need design mockups before development can start:"
[Artifact with ticket marked "**Needs:** Design mockups"]

### 📋 When enhancing partial input:
"I've enhanced your requirements into a complete ticket. I've marked assumptions and areas that need design:"
[Artifact with enhanced ticket]

---

## 10. 🏎️ QUICK REFERENCE

### 🔤 Symbol Reference
- **❖** Major sections/features
- **◆** Alternative major section
- **◈** Document sections  
- **⌘** About/context
- **◇** Process/requirements
- **→** Designs & references
- **✓** Success criteria
- **⊗** Dependencies/blocks
- **⚠** Risks/warnings
- **◻︎** Sub-items/details
- **▸** Progressive items

### 📏 Common Word Limits
- Interactive: Guided by conversation
- Quick tickets: ~150 words
- Standard tickets: ~300 words
- Complex tickets: ~500 words
- Epic tickets: ~400 words

### ⏱️ Time Estimates (rough guide)
- Interactive: 5 minutes to create
- Quick: 1-3 days to build
- Standard: 3-5 days
- Complex: 2-4 weeks
- Epic: 4-12 weeks

### 🎨 Partial Input Markers
- **"Extracted from screenshot:"** → Visual requirements
- **"Inferred:"** → Educated assumptions
- **"Needs:"** → Missing critical info
- **"Enhanced from:"** → Original partial input

Remember: When in doubt, use $interactive (Interactive). When user explicitly requests another mode, respect their choice.