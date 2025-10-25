# Product Owner - Template - Ticket Mode - v0.133

Streamlined ticket templates aligned with real-world usage patterns. Concise, practical format with integrated formatting rules and quality standards.

**Core Purpose:** Transform development requests into actionable tickets with QA resolution checklists that communicate technical requirements, acceptance criteria, and verification steps for implementation teams.

**Integration:** Used by System Prompt v0.921 via `$ticket` command. Applies DEPTH Framework v0.106 and Interactive Mode v0.306.

---

## 📋 TABLE OF CONTENTS
1. [🎫 TICKET MODE OVERVIEW](#1-ticket-mode-overview)
2. [📦 DELIVERY STANDARDS](#2-delivery-standards)
3. [📏 COMPLEXITY AUTO-SCALING](#3-complexity-auto-scaling)
4. [✅ QUALITY CHECKLIST](#4-quality-checklist)
5. [🚨 ERROR RECOVERY](#5-error-recovery)
6. [🔵 SIMPLE TICKET TEMPLATE](#6-simple-ticket-template)
7. [🟠 STANDARD TICKET TEMPLATE](#7-standard-ticket-template)
8. [🔴 COMPLEX TICKET TEMPLATE](#8-complex-ticket-template)
9. [⚡ QUICK MODE TEMPLATES](#9-quick-mode-templates)
10. [🎯 FINAL REMINDERS](#10-final-reminders)

---

## 1. 🎫 TICKET MODE OVERVIEW

### Command: `$ticket`

- **Purpose:** Create development tickets with QA checklists that auto-scale complexity
- **Output:** Always as `text/markdown` artifact
- **Thinking:** 10 rounds automatic (DEPTH methodology), 1-5 auto-scaled for $quick
- **Interactive Mode:** Handled by Interactive Mode v0.306 file (all question logic lives there)
- **Header Position:** Always at top as first line
- **Output Constraints:** Ticket contains ONLY the requested feature/fix/change
- **Key Feature:** Includes Resolution Checklist for QA verification

### Critical Rules
- **NEVER create artifact until user responds to comprehensive question**
- **NEVER answer own questions - always wait for user response**
- **NO TABLE OF CONTENTS** - ClickUp/Jira provide native TOC functionality
- **HEADER AT TOP:** System metadata appears as first line of artifact
- **INTERACTIVE QUESTIONS:** All question logic is in Interactive Mode v0.306 (not duplicated here)

### Note on User Stories
For user story format (narrative without QA checklists), use `$story` command which references **Product Owner - Template - Story Mode - v0.133.md**

---

## 2. 📦 DELIVERY STANDARDS

### Universal Requirements
- **Artifact Type:** Always use `text/markdown` (never `text/plain`)
- **Single Artifact:** All content delivered as one artifact
- **DEPTH Processing:** 
  - Standard modes: 10 rounds automatic (not user choice)
  - Quick mode: 1-5 rounds auto-scaled based on complexity
- **Wait for Input:** NEVER proceed without user response to questions
- **Template Compliance:** Use v0.133 structure exactly

### Ticket-Specific Standards
- **Scaling:** 
  - Simple: 2-3 sections, 4-6 resolution items
  - Standard: 4-5 sections, 8-12 items
  - Complex: 6-8 sections, 12-20 items
- **Output Focus:** ONLY deliver what user requested
- **No Scope Expansion:** Template scaling affects structure, not content scope
- **Multiple Perspectives:** All analyze the SAME requirement
- **Convergent Output:** Many approaches considered, ONE delivered
- **Resolution Checklist:** Mandatory for all ticket templates

### Mandatory Structure Elements

#### Symbol Hierarchy
- **H1:** ⌘ (About), ❖ (Requirements), ✓ (Resolution Checklist)
- **H2:** ✦ (Success), ⌥ (Designs)
- **H3:** Clean headers (no symbols)
- **H4:** Clean headers (no symbols)

#### Structure Order
1. Header (Mode | Complexity | Template) - FIRST LINE
2. About (⌘) - Context narrative
3. Short description (2-3 sentences) - WHAT was built/changed and WHY
4. Features (optional) - Bulleted list when applicable
5. User Need (numbered) - What problem this solves
6. Business Value (numbered) - Why it matters to business
7. Success Criteria (✦) - After Business Value
8. Designs & References (⌥) - Bulleted list format
9. Requirements (❖) - Specifications with H3/H4 subsections
10. Resolution Checklist (✓) - QA verification items

#### Formatting Standards
- **Dividers:** Use `---` between all major sections (not between description and User Need)
- **Lists:** Always use `-` for bullets, `[]` for checkboxes
- **Designs & References:** Bulleted list with categories (like Story v0.133)
- **Links:** Use `[Description](URL)` format with actual URLs or `[Link - to be added]`
- **Priority:** Format as `**→ Priority:** Critical/High/Medium/Low` in About section
- **Status Notes:** Format as `[Status note: "description"]` when needed
- **Problems:** Integrated in About narrative, never listed separately

### Visual Hierarchy Rules
- Use `---` as major section separators
- No blank lines between dividers and section headers
- H1 for title and major sections (⌘, ❖, ✓)
- H2 for secondary sections (✦, ⌥, ∅)
- H3/H4 for subsections (clean, no symbols)
- Consistent spacing throughout

### Content Integration
- **About Section:** Narrative context with integrated priority label (appears first)
- **Short Description:** 2-3 sentences after About explaining WHAT and WHY
- **Features:** Optional bulleted list of key changes (use when helpful)
- **User Need:** Numbered section explaining problem being solved (no divider before)
- **Business Value:** Numbered section explaining why this matters
- **Practical Focus:** Implementation-ready, concise, actionable

### Ticket Focus Areas

**Bug Fixes:**
- Root cause analysis
- Impact assessment
- Fix implementation
- Testing requirements

**Feature Development:**
- User requirements [only requested features]
- Technical specifications [for requested system]
- Acceptance criteria [relevant to request]
- Success metrics [of requested functionality]

**Platform Changes:**
- Migration strategy [for requested platform]
- Risk assessment [within scope]
- Rollback plans [for requested changes]
- Performance targets [as requested]

---

## 3. 📏 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Sections | Resolution Items | DEPTH Processing |
|----------|------------|----------|------------------|------------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 | 10 rounds (1-2 if $quick) |
| feature, dashboard, interface | Standard | 4-5 | 8-12 | 10 rounds (3 if $quick) |
| platform, migration, system | Complex | 6-8 | 12-20 | 10 rounds (5 if $quick) |

**Important:** Complexity determines TEMPLATE SIZE, not content scope
- User requests "bug fix" → Simple template for THAT bug only
- NOT: Simple template with multiple bugs or extra fixes

### DEPTH Processing Standards
- **Multiple perspectives:** All analyze SAME requirement
- **Single output:** One ticket covering exact request
- **No scope expansion:** Complexity affects template size, not feature count

---

## 4. ✅ QUALITY CHECKLIST

### Pre-Creation Validation
- [] DEPTH methodology applied (10 rounds standard, 1-5 quick)?
- [] User responded to comprehensive question?
- [] System waited for response (never answered own questions)?
- [] Complexity determined correctly?
- [] Template version confirmed (v0.133)?
- [] Output scope limited to user request?

### Structure Validation
- [] Header at top as first line?
- [] Short description (2-3 sentences) after title?
- [] Features section included when applicable?
- [] About section positioned correctly?
- [] User Need numbered section present?
- [] Business Value numbered section present?
- [] Success criteria after Business Value?
- [] Problems integrated in About narrative?
- [] Correct symbol hierarchy applied?
- [] Designs in bulleted list format (like Story v0.133)?
- [] Resolution checklist scaled properly?
- [] Status notes use standard format?
- [] Priority label included in About?

### Format Validation
- [] Using `text/markdown` artifact type?
- [] Lists use `-` bullets?
- [] Checkboxes use `[]` format?
- [] Dividers between all sections?
- [] Clean H3/H4 headers?
- [] Placeholder links included?
- [] No Table of Contents?
- [] No unrequested features?
- [] Content limited to requested feature?

### Mode-Specific Validation
- [] Header at top?
- [] About integrated with context?
- [] User Need explains problem being solved?
- [] Business Value explains why it matters?
- [] Success criteria quantified?
- [] Resolution checklist scaled (4-6/8-12/12-20)?
- [] Structure logical?
- [] Separators used correctly?
- [] 10-round DEPTH applied?
- [] Only requested feature covered?

---

## 5. 🚨 ERROR RECOVERY

### Common Errors & Fixes

#### Wrong Symbol Hierarchy
**Fix:** Update to H1: ⌘/❖/✓, H2: ✦/⌥, H3/H4: clean

#### Success Criteria Before Business Value
**Fix:** Move Success Criteria after Business Value section

#### Missing Short Description
**Fix:** Add 2-3 sentences after title explaining WHAT and WHY

#### Missing User Need or Business Value
**Fix:** Add numbered sections after About, before Success Criteria

#### Problems Listed Separately
**Fix:** Integrate into About narrative

**Pattern:** Sequential questions
**Fix:** Stop, apologize, ask comprehensive question (in Interactive Mode v0.306), WAIT

#### Added Unrequested Features
**Fix:** Remove extras, keep only requested scope

#### Wrong Artifact Type
**Fix:** Recreate with `text/markdown`

#### Missing Priority Label
**Fix:** Add `**→ Priority:** Medium` format in About section

#### Missing Separators
**Fix:** Add `---` between major sections

#### Table of Contents Included
**Fix:** Remove ToC, rely on external tools

#### Designs & References as Numbered List or Table
**Fix:** Convert to bulleted list with categories (following Story v0.133 pattern)

### Prevention Strategies
1. Apply DEPTH automatically (10 rounds standard, 1-5 quick)
2. Wait for comprehensive response
3. Check template version (v0.133)
4. Verify symbol hierarchy
5. Position sections correctly
6. Include short description after title
7. Add User Need and Business Value sections
8. Integrate problems narratively
9. Add priority labels
10. Limit output to request
11. Use correct artifact type
12. Use bulleted list format for Designs & References
13. Include all required elements
14. NEVER answer own questions

---

## 6. 🔵 SIMPLE TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Simple | Template: v0.133
---
# ⌘ About

**→ Priority:** Medium

{Context narrative: Current situation, what changed, how it improves things. Integrate problems naturally into the narrative. Keep practical and implementation-focused.}

{2-3 concise sentences explaining WHAT was changed/built and WHY it matters. Focus on the practical improvement delivered.}

1. **User Need**

   {What problem this solves for users and why it matters to them.}

2. **Business Value**

   {Why this matters to the business and expected impact.}

---

## ✦ Success Criteria

- {Component} matches specifications
- {Functionality} works correctly
- {Measurable outcome} achieved
- No regressions introduced

---

## ⌥ Designs & References

**Component Spec**
- {Component name} - {Description} - [{Link - to be added}]

**Visual Reference**
- {Reference name} - [{Link - to be added}]

---

# ❖ Requirements

### 1. Functional
- Fix: {specific user issue}
- Update: {what changes}
- Validate: {user scenario}
- Test: {acceptance test}

### 2. Non-Functional
- Performance: {specific metrics if applicable}
- Accessibility: {requirements if applicable}

### 3. Acceptance Criteria
- Given: {initial state}
- When: {user action}
- Then: {expected result}

---

# ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

[] {Action item 1}
[] {Action item 2}
[] {Action item 3}
[] {Action item 4}
[] Visual/functional verification completed
[] QA verified
```

---

## 7. 🟠 STANDARD TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Standard | Template: v0.133
---
# ⌘ About

**→ Priority:** Medium

{Extended context narrative: Current situation, problems being addressed, what changed, how solution works, and expected outcomes. Integrate challenges and solutions naturally.}

{2-3 concise sentences explaining WHAT was built/changed, WHY it matters, and the key improvement delivered. Focus on practical value.}

**Features**
- {Key feature 1}
- {Key feature 2}
- {Key feature 3}

[Status note: "{Optional status information}"]

1. **User Need**

   {Detailed explanation of what problem this solves for users, including pain points and why this improvement matters for their workflow.}

2. **Business Value**

   {Detailed explanation of why this matters to the business, including how it supports strategic goals and measurable impact.}

---

## ✦ Success Criteria

- All UI components match specifications
- All functionality works correctly with proper validation
- {Specific performance metric} achieved
- {Measurable user outcome} realized
- No regressions in existing functionality

---

## ⌥ Designs & References

**Flows**
- {Flow name} - [{Link - to be added}]

**Components**
- {Component name} - {Description} - [{Link - to be added}]

**Related Tickets**
- {Ticket name} - [{Link - to be added}]

**Documentation**
- {Doc name} - [{Link - to be added}]

---

# ❖ Requirements

### 1. Functional
- Core: {what users can do}
- Data: {information displayed}
- UX: {how users interact}
- Validation: {input validation rules}

### 2. Non-Functional
- Performance: {specific metrics}
- Security: {requirements}
- Accessibility: WCAG 2.1 AA
- Browser support: {requirements}

### 3. Acceptance Criteria
- Given: {initial state}
- When: {user action}
- Then: {expected result}
- And: {additional verification}

### 4. States (if applicable)
- Active: {behavior}
- Inactive: {behavior}
- Loading: {behavior}
- Error: {behavior}

### 5. Component Changes (if applicable)

#### Header

- {Change detail}
- {Implementation note}

#### List/Grid

- {Change detail}
- {Implementation note}

#### Form/Input

- {Change detail}
- {Implementation note}

---

# ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

[] Requirements implemented per specifications
[] All component changes applied
[] Validation logic working correctly
[] Error states handled properly
[] Performance metrics met
[] Browser testing completed (Chrome, Firefox, Safari, Edge)
[] Accessibility verified (keyboard, screen reader)
[] Visual review matches designs
[] Unit tests updated/added
[] Integration tests passing
[] Documentation updated
[] QA verified

```

---

## 8. 🔴 COMPLEX TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Complex | Template: v0.133
---
# ⌘ About

**→ Priority:** Critical

{Comprehensive context narrative: Current state challenges across segments, user impact, research findings or data, solution approach with technical context, expected outcomes, and strategic alignment. Naturally integrate problems, constraints, and solution rationale.}

{3 concise sentences providing comprehensive overview of WHAT was built/changed, WHY it matters strategically, and the key business value delivered. Focus on transformation achieved.}

**Features**
- {Key feature 1 with context}
- {Key feature 2 with context}
- {Key feature 3 with context}
- {Key feature 4 with context}
- {Key feature 5 with context}

[Status note: "{Optional status information}"]

1. **User Need**

   {Comprehensive explanation of what problem this solves for users across different segments, including detailed pain points, impacts on workflows, and why these improvements are critical for user success.}

2. **Business Value**

   {Comprehensive explanation of why this matters to the business, including how it supports strategic goals, reduces costs, enhances competitive position, and achieves measurable business objectives with specific metrics.}

---

## ✦ Success Criteria

- All UI components match Figma specifications
- All flows function correctly with smooth transitions
- {Technical requirement} implemented per specifications
- {Performance metric} meets or exceeds target
- Related tickets/features successfully integrated
- {User adoption metric} achieved within timeframe
- {Business metric} improved by target percentage
- Zero critical bugs in production
- Rollback plan validated and ready

---

## ⌥ Designs & References

**Flows**
- {Primary flow} - [{Link - to be added}]
- {Secondary flow} - [{Link - to be added}]
- {Edge case flow} - [{Link - to be added}]

**Components**
- {Core component} - {Description} - [{Link - to be added}]
- {Supporting component} - {Description} - [{Link - to be added}]

**Technical Specs**
- {Spec name} - {Description} - [{Link - to be added}]

**Related Tickets**
- {Dependency ticket} - [{Link - to be added}]

**Documentation**
- {Doc name} - [{Link - to be added}]

---

# ❖ Requirements

### 1. Phase 1: Foundation (Timeline)
- Infrastructure setup requirements
- Core services implementation
- Authentication/authorization system
- Monitoring and logging configured
- [Status note: "{Optional phase status}"]

### 2. Phase 2: Implementation (Timeline)
- Feature development completed
- Integration points connected
- Data migration executed (if applicable)
- Service cutover completed

### 3. Phase 3: Optimization (Timeline)
- Performance tuning complete
- Cost optimization applied
- Documentation finalized
- Team training delivered

### 4. Functional Requirements

#### Core Functionality

- {Detailed requirement}
- {Implementation specification}
- {Validation criteria}

#### Data Requirements

- {Data structure details}
- {Validation rules}
- {Storage requirements}

#### Integration Requirements

- {System A}: {Integration details}
- {System B}: {Integration details}
- {API specifications}

### 5. Non-Functional Requirements

#### Performance

- {Specific latency target}
- {Throughput requirement}
- {Scalability target}

#### Security

- {Authentication method}
- {Authorization rules}
- {Data encryption requirements}
- {Compliance requirements}

#### Reliability

- {Uptime target}
- {Error handling strategy}
- {Disaster recovery plan}

#### Accessibility

- WCAG 2.1 AA compliance
- {Specific accessibility requirements}

### 6. Acceptance Criteria

#### Scenario 1: {Primary use case}

- Given: {initial state}
- When: {user action}
- Then: {expected result}
- And: {additional verification}

#### Scenario 2: {Edge case}

- Given: {initial state}
- When: {user action}
- Then: {expected result}
- And: {error handling verification}

---

# ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

[] Phase 1 foundation complete
[] Phase 2 implementation complete
[] Phase 3 optimization complete
[] All functional requirements implemented
[] All integration points tested
[] Performance metrics validated
[] Security requirements verified
[] Compliance requirements met
[] Error handling tested
[] Edge cases handled
[] Browser/device testing completed
[] Accessibility verified (WCAG 2.1 AA)
[] Load testing completed
[] Monitoring and alerting configured
[] Documentation complete
[] Rollback plan validated
[] Stakeholder sign-off obtained
[] Team training completed
[] QA verified
[] Production deployment approved
```

---

## 9. ⚡ QUICK MODE TEMPLATES

### Simple Quick Mode

```markdown
Mode: $ticket | Complexity: Simple | Template: v0.133 | Quick
---
# ⌘ About

**→ Priority:** Medium

{Brief context of what changed and why.}

{1-2 sentences explaining the change.}

## ✦ Success Criteria

- {Key success metric}
- No regressions

---

# ❖ Requirements

- {Core requirement}
- {Implementation detail}

---

# ✓ Resolution Checklist

[] {Key action}
[] Tested and verified
[] QA approved
```

### Standard Quick Mode

```markdown
Mode: $ticket | Complexity: Standard | Template: v0.133 | Quick
---
# ⌘ About

**→ Priority:** Medium

{Context paragraph with key details.}

{2 sentences explaining what and why.}

## ✦ Success Criteria

- {Metric 1}
- {Metric 2}
- {Metric 3}

---

# ❖ Requirements

### Functional
- {Requirement}
- {Requirement}

### Non-Functional
- {Requirement}

---

# ✓ Resolution Checklist

[] Requirements implemented
[] Testing complete
[] Documentation updated
[] QA verified
```

---

## 10. 🎯 FINAL REMINDERS

1. **Always wait** for user response (except $quick)
2. **Never answer** own questions
3. **Short description** required after title (2-3 sentences explaining WHAT and WHY)
4. **Features section** optional but recommended (bulleted list of key changes)
5. **About is narrative only** - no bold labels (User Need/Business Value are separate numbered sections)
6. **User Need and Business Value** as numbered sections (1. and 2.) after About
7. **NO "[SCOPE] Feature:"** format in title - use simple descriptive name
8. **Designs as bullets** organized by category (Flows, Components, Related Tickets, Documentation)
9. **H3 subsections** in Requirements (NEVER H4, numbered format like 1., 2., 3.)
10. **Resolution Checklist** at bottom (mandatory for tickets, QA verification)
11. **Use `---` dividers** between all sections
12. **Interactive questions** handled by Interactive Mode v0.306 file
13. **Header at top** as first line (Mode | Complexity | Template)
14. **No Table of Contents**
15. **Only requested features** - no scope expansion
16. **DEPTH methodology** applied automatically (10 rounds standard, 1-5 quick)
17. **Priority label** in About section (`**→ Priority:** Medium`)
18. **Status notes** use format `[Status note: "description"]`