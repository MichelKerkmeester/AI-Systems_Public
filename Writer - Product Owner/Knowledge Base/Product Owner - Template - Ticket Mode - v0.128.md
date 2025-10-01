# Product Owner - Template - Ticket Mode - v0.128

Development ticket and user story templates with complexity auto-scaling (Simple: 2-3 sections/4-6 items, Standard: 4-5 sections/8-12 items, Complex: 6-8 sections/12-20 items). Includes resolution checklists, requirements, user stories, and acceptance criteria.

---

## 📋 TABLE OF CONTENTS
1. [🎫 TICKET MODE OVERVIEW](#1-ticket-mode-overview)
2. [🔍 COMPLEXITY AUTO-SCALING](#2-complexity-auto-scaling)
3. [🔵 SIMPLE TICKET TEMPLATE](#3-simple-ticket-template)
4. [🟠 STANDARD TICKET TEMPLATE](#4-standard-ticket-template)
5. [🔴 COMPLEX TICKET TEMPLATE](#5-complex-ticket-template)
6. [✨ TICKET FORMATTING RULES](#6-ticket-formatting-rules)
7. [🗣️ INTERACTIVE QUESTIONS](#7-interactive-questions)

---

## 1. 🎫 TICKET MODE OVERVIEW

### Command: `$ticket` or `$story`

- **Purpose:** Create development tickets or user stories that auto-scale complexity
- **Output:** Always as artifact
- **Thinking:** 10 rounds automatic (DEPTH methodology), 1-5 auto-scaled for $quick
- **Interactive Mode:** Single comprehensive question gathering ALL requirements at once
- **Key Difference:** Stories omit Resolution Checklist
- **Header Position:** Always at top as first line
- **Silent Processing:** User sees simple messages, not methodology details
- **Output Constraints:** Ticket contains ONLY the requested feature/fix/change

---

## 2. 🔍 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Sections | Resolution Items | DEPTH Processing |
|----------|------------|----------|------------------|-----------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 | 10 rounds (1-2 if $quick) |
| feature, dashboard, api | Standard | 4-5 | 8-12 | 10 rounds (3 if $quick) |
| platform, architecture, migration | Complex | 6-8 | 12-20 | 10 rounds (5 if $quick) |

**Important:** Complexity determines TEMPLATE SIZE, not content scope
- User requests "bug fix" → Simple template for THAT bug only
- NOT: Simple template with multiple bugs or extra fixes

---

## 3. 🔵 SIMPLE TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Simple | Template: v0.128
---
[SCOPE] Bug Fix: [Feature Name]

# ⌘ About

[2-3 sentences describing the specific issue requested by user and its impact. 
Covers ONLY the bug/fix mentioned, no additional issues.]

---

## ✦ Success Criteria

- Issue resolved and verified in production
- No regression in existing functionality
- Performance metrics maintained or improved

---

## ⌥ Designs & References

| Type | Resource | Status | Link |
|------|----------|--------|------|
| Bug Report | JIRA-123 | Open | [Link - to be added] |
| Screenshot | Error State | Captured | [Link - to be added] |

---

## ❖ Requirements

### ◻︎ Functional Requirements

- Fix [specific issue from user's request]
- Ensure [expected behavior for this fix]
- Validate [edge cases for this specific bug]

---

## ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

[] Identify root cause through debugging
[] Implement fix with appropriate solution
[] Test fix locally with various scenarios
[] Update unit tests if needed
[] Verify no regressions occur
[] Document fix in PR description
```

---

## 4. 🟠 STANDARD TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Standard | Template: v0.128
---
[SCOPE] Feature: [Feature Name]

# ⌘ About

[2-4 sentences describing what this specific feature requested by user does 
and why it matters to users and the business. Contains ONLY the feature 
described in the request, no additional capabilities.]

---

## ✦ Success Criteria

- Measurable outcome with specific metrics [for requested feature]
- User acceptance criteria clearly defined
- Performance benchmarks achieved
- Analytics tracking implemented

---

## ⌥ Designs & References

| Type | Resource | Status | Link |
|------|----------|--------|------|
| Design | Mockups | Complete | [Link - to be added] |
| PRD | Product Requirements | Approved | [Doc - to be added] |
| API | Endpoint Spec | Draft | [Swagger - to be added] |

---

## ❖ Requirements

### ◻︎ Functional Requirements
[Only requirements for the requested feature]

- Primary requirement with clear acceptance criteria
- Secondary requirement with measurable outcome
- Tertiary requirement with defined scope

### ◻︎ Non-Functional Requirements

- Performance: <200ms response time
- Security: OAuth 2.0 implementation
- Accessibility: WCAG 2.1 AA compliance

### ◻︎ Technical Requirements

- Backend API changes needed [for this feature]
- Frontend framework requirements [for this feature]
- Database schema modifications [for this feature]

---

## ❖ User Stories

**As a** [primary user type]
**I want to** [specific action related to requested feature]
**So that** [benefit achieved from this feature]

**As a** [secondary user type]
**I want to** [specific action related to requested feature]
**So that** [benefit achieved from this feature]

---

## ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

[] Implement core functionality per requirements
[] Add comprehensive input validation
[] Handle all identified error cases
[] Write unit tests (>80% coverage)
[] Write integration tests for workflows
[] Update API documentation
[] Add analytics tracking events
[] Perform security review
[] Test on all supported browsers
[] Verify mobile responsiveness
[] Get design approval on implementation
[] Complete code review with team
```

---

## 5. 🔴 COMPLEX TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Complex | Template: v0.128
---
[SCOPE] Platform: [Platform/Architecture Name]

# ⌘ About

[3-5 sentences describing the specific platform change requested by user, 
its strategic importance, and what problems it solves. Covers ONLY the 
platform/architecture/migration mentioned in the request.]

---

## ✦ Success Criteria

- All systems migrated with zero data loss [for requested platform]
- Performance metrics meet or exceed targets
- 99.9% uptime maintained during migration
- User acceptance testing passed
- Compliance requirements verified
- Cost savings targets achieved

---

## ⌥ Designs & References

| Type | Resource | Status | Link |
|------|----------|--------|------|
| Architecture | System Diagrams | Complete | [Miro - to be added] |
| Tech Spec | Migration Plan | Draft | [Confluence - to be added] |
| Performance | Benchmarks | Baseline | [DataDog - to be added] |
| Security | Assessment Report | In Progress | [Doc - to be added] |

---

## ❖ Requirements

### ◻︎ Functional Requirements
[Only for the requested platform/architecture change]

- Core platform capability with detailed specifications
- Integration requirements with existing systems
- Data migration and transformation needs
- User-facing feature modifications

### ◻︎ Non-Functional Requirements

- Scalability: 10,000 concurrent users
- Performance: 99.9% uptime SLA
- Security: SOC 2 compliance
- Compliance: GDPR, CCPA

### ◻︎ Integration Requirements

- System integration with service A [if relevant to request]
- API compatibility with existing clients
- Data synchronization requirements
- Third-party service connections [if mentioned]

---

## ❖ User Stories

**PRD: [PRD Name]**

**Story 1: Core Platform Capability**
**As a** [user type]
**I want to** [capability within requested platform]
**So that** [business value from this platform]

**Story 2: Migration Experience**
**As an** [existing user]
**I want to** [seamless transition for requested change]
**So that** [no disruption during requested migration]

**Story 3: New Capabilities**
**As a** [power user]
**I want to** [advanced features of requested platform]
**So that** [enhanced productivity with new platform]

---

## ∅ Risks & Mitigations

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Data loss during migration | High | Low | Comprehensive backups, dry runs, validation scripts |
| Extended downtime | High | Medium | Blue-green deployment, feature flags, staged rollout |
| Performance degradation | Medium | Low | Load testing, performance monitoring, optimization plan |
| Integration failures | Medium | Medium | Contract testing, sandbox environment, fallback APIs |

---

## ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

### ◻︎ Planning & Design
[] Complete technical design review
[] Obtain stakeholder approval
[] Finalize migration strategy
[] Document rollback procedures

### ◻︎ Development & Testing
[] Set up development environment
[] Implement Phase 1 components
[] Create comprehensive test suite
[] Perform security audit
[] Complete load testing
[] Document all APIs

### ◻︎ Integration & Validation
[] Conduct integration testing
[] Validate data migration scripts
[] Perform user acceptance testing
[] Verify monitoring coverage

### ◻︎ Deployment & Operations
[] Create deployment runbooks
[] Train support team
[] Execute staged deployment
[] Monitor system metrics
[] Complete performance optimization
[] Update all documentation
```

---

## 6. ✨ TICKET FORMATTING RULES

### Mandatory Elements

1. **Header at top** - Mode | Complexity | Template (first line)
2. **[SCOPE]** prefix - Before title
3. **About section** - Brief 2-5 sentences max, covers ONLY requested item
4. **Success Criteria** - After About section
5. **QA Warning** - Above resolution checklist
6. **Dividers** - Use `---` between major sections
7. **Designs as Table** - Not bullet lists

### DEPTH Processing Standards

- **Automatic Application:** 10 rounds for standard, 1-5 for $quick
- **No User Choice:** System determines depth automatically
- **Silent Processing:** User never sees methodology details
- **Multiple Perspectives:** All analyze the SAME ticket requirements
- **Single Output:** One ticket covering exact request
- **No Scope Expansion:** Complexity affects template structure, not content beyond request

### Symbol Reference

- **⌘** About section (H1)
- **❖** Main sections (H1) 
- **◻︎** Sub-sections (H2)
- **⌥** Designs & References (H2)
- **✦** Success Criteria (H2)
- **✓** Resolution Checklist (H2)
- **∅** Risks (H2, Complex only)

### Structure Order

1. Header (Mode | Complexity | Template)
2. Title with [SCOPE]
3. About (⌘) - 2-5 sentences about REQUESTED item only
4. Success Criteria (✦)
5. Designs & References (⌥)
6. Requirements (❖) - For requested feature only
7. User Stories (❖)
8. Risks (∅) - Complex only
9. Resolution Checklist (✓)

### Formatting Standards

- Always use divider `---` after header
- Keep About section concise (2-5 sentences)
- Use tables for Designs & References
- Use `-` for bullet points
- Use `[]` for checkboxes (no spaces inside)
- Include "to be added" for placeholder links
- Content limited to exact request

---

## 7. 🗣️ INTERACTIVE QUESTIONS

### Initial Interactive Flow - Single Comprehensive Question

```markdown
User: $ticket payment integration

System: Let me help you create your payment integration ticket. 🎯

Please provide ALL of the following details:

1️⃣ **Format type:**
   • Ticket - Development task with resolution checklist
   • Story - User story format without checklist

2️⃣ **Scope:**
   • BE - Backend/API
   • FE - Frontend/UI
   • Mobile - iOS/Android
   • FS - Full-stack
   • DevOps - Infrastructure
   • QA - Testing

3️⃣ **Requirements & context:**
   • What needs to be built/fixed?
   • Key features or integration points
   • Timeline or dependencies

Please respond with complete information (e.g., "1. Ticket, 2. BE, 3. Stripe API integration with webhook support, Q2 deadline")

[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]
```

**After user responds:**

```markdown
User: 1. Ticket, 2. BE, 3. Stripe payment processing with subscriptions

System: Perfect! Creating your backend ticket.

Processing now...
• Applying 10-round DEPTH methodology
• Analyzing payment requirements
• Building ticket structure
• Creating resolution checklist

[CREATES TICKET with ONLY Stripe payment processing and subscriptions]
```

### Story Format

When user selects "Story", omit the Resolution Checklist:

```markdown
Mode: $story | Complexity: [level] | Template: v0.128
---
[SCOPE] Story: [Name]

# ⌘ About
[2-5 sentences max about requested story]

## ✦ Success Criteria
[Positioned after About]

## ⌥ Designs & References
[Same table format]

## ❖ Requirements
[Same structure, for requested feature only]

## ❖ User Stories
[Same format, related to request]

[NOTE: No Resolution Checklist for stories]
```

### Important Processing Notes

**DEPTH Application:**
- Multiple perspectives analyze the SAME ticket requirements
- Various approaches considered for the SAME feature/fix
- Output contains ONLY the requested ticket content
- Complexity affects template size, not feature count

**Output Guarantee:**
```
User Request: "Ticket for login bug"
↓
Internal DEPTH Analysis:
- 5 perspectives analyze the SAME login bug
- 8 fix approaches for the SAME login bug
- Quality optimized for the SAME login bug
↓
Output: ONE login bug ticket
- Exactly what user requested
- No additional bugs or features
- No scope expansion
- Perfect template format
```

### Ticket vs Story Decision Matrix

| User Selects | Includes | Excludes | Use Case |
|--------------|----------|----------|-----------|
| Ticket | Resolution Checklist | - | Development tasks |
| Story | User narrative format | Resolution Checklist | Agile stories |

### Complexity Detection Examples

**Simple Detection:**
```
"fix typo in header" → Simple (2-3 sections, 4-6 items)
"bug in login" → Simple
"update button color" → Simple
```

**Standard Detection:**
```
"add dashboard feature" → Standard (4-5 sections, 8-12 items)
"implement API endpoint" → Standard
"create user profile" → Standard
```

**Complex Detection:**
```
"migrate to new platform" → Complex (6-8 sections, 12-20 items)
"rebuild architecture" → Complex
"system-wide refactor" → Complex
```

### Critical Reminders

- **WAIT FOR USER:** Never proceed without complete response
- **NEVER ANSWER OWN QUESTIONS:** Always wait for user input
- **OUTPUT = REQUEST:** Deliver exactly what was asked for
- **DEPTH AUTOMATIC:** 10 rounds standard, 1-5 for $quick
- **SILENT PROCESSING:** Hide methodology from user
- **SINGLE COMPREHENSIVE QUESTION:** Get all info at once