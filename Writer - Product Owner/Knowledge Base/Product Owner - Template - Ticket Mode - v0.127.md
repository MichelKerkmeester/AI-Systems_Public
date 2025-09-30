# Product Owner - Template - Ticket Mode - v0.127

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
- **Thinking:** 10 rounds automatic (ultrathink), 1-5 auto-scaled for $quick
- **Interactive Mode:** Single comprehensive question gathering all requirements
- **Key Difference:** Stories omit Resolution Checklist
- **Header Position:** Always at top as first line

---

## 2. 🔍 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Sections | Resolution Items |
|----------|------------|----------|------------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 |
| feature, dashboard, api | Standard | 4-5 | 8-12 |
| platform, architecture, migration | Complex | 6-8 | 12-20 |

---

## 3. 🔵 SIMPLE TICKET TEMPLATE

```markdown
Mode: $ticket | Complexity: Simple | Template: v0.127
---
[SCOPE] Bug Fix: [Feature Name]

# ⌘ About

[2-3 sentences describing the issue and its impact]

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

- Fix [specific issue]
- Ensure [expected behavior]
- Validate [edge cases]

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
Mode: $ticket | Complexity: Standard | Template: v0.127
---
[SCOPE] Feature: [Feature Name]

# ⌘ About

[2-4 sentences describing what this feature does and why it matters to users and the business]

---

## ✦ Success Criteria

- Measurable outcome with specific metrics
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

- Primary requirement with clear acceptance criteria
- Secondary requirement with measurable outcome
- Tertiary requirement with defined scope

### ◻︎ Non-Functional Requirements

- Performance: <200ms response time
- Security: OAuth 2.0 implementation
- Accessibility: WCAG 2.1 AA compliance

### ◻︎ Technical Requirements

- Backend API changes needed
- Frontend framework requirements
- Database schema modifications

---

## ❖ User Stories

**As a** [primary user type]
**I want to** [specific action]
**So that** [benefit achieved]

**As a** [secondary user type]
**I want to** [specific action]
**So that** [benefit achieved]

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
Mode: $ticket | Complexity: Complex | Template: v0.127
---
[SCOPE] Platform: [Platform/Architecture Name]

# ⌘ About

[3-5 sentences describing the platform change, its strategic importance, and what problems it solves]

---

## ✦ Success Criteria

- All systems migrated with zero data loss
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

- System integration with service A
- API compatibility with existing clients
- Data synchronization requirements
- Third-party service connections

---

## ❖ User Stories

**PRD: [PRD Name]**

**Story 1: Core Platform Capability**
**As a** [user type]
**I want to** [capability]
**So that** [business value]

**Story 2: Migration Experience**
**As an** [existing user]
**I want to** [seamless transition]
**So that** [no disruption]

**Story 3: New Capabilities**
**As a** [power user]
**I want to** [advanced features]
**So that** [enhanced productivity]

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
3. **About section** - Brief 2-5 sentences max
4. **Success Criteria** - After About section
5. **QA Warning** - Above resolution checklist
6. **Dividers** - Use `---` between major sections
7. **Designs as Table** - Not bullet lists

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
3. About (⌘) - 2-5 sentences
4. Success Criteria (✦)
5. Designs & References (⌥)
6. Requirements (❖)
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

---

## 7. 🗣️ INTERACTIVE QUESTIONS

### Initial Interactive Flow

```markdown
User: $ticket payment integration

System: Let me help you create your payment integration ticket. 🎯

Please provide the following details:

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

Please respond with all information (e.g., "1. Ticket, 2. BE, 3. Stripe API integration")

[WAIT FOR USER RESPONSE]
```

### Story Format

When user selects "Story", omit the Resolution Checklist:

```markdown
Mode: $story | Complexity: [level] | Template: v0.127
---
[SCOPE] Story: [Name]

# ⌘ About
[2-5 sentences max]

## ✦ Success Criteria
[Positioned after About]

## ⌥ Designs & References
[Same table format]

## ❖ Requirements
[Same structure]

## ❖ User Stories
[Same format]

[NOTE: No Resolution Checklist for stories]
```