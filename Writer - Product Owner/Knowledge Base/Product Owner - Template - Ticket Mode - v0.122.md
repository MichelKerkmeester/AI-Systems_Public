# Product Owner - Template - Ticket Mode - v0.122

## 📋 TABLE OF CONTENTS

1. [🎫 TICKET MODE OVERVIEW](#1-🎫-ticket-mode-overview)
2. [📝 COMPLEXITY AUTO-SCALING](#2-📝-complexity-auto-scaling)
3. [🔵 SIMPLE TICKET TEMPLATE](#3-🔵-simple-ticket-template-2-3-sections-4-6-resolution)
4. [🟠 STANDARD TICKET TEMPLATE](#4-🟠-standard-ticket-template-4-5-sections-8-12-resolution)
5. [🔴 COMPLEX TICKET TEMPLATE](#5-🔴-complex-ticket-template-6-8-sections-12-20-resolution)
6. [✨ TICKET FORMATTING RULES](#6-✨-ticket-formatting-rules)
7. [🗣️ INTERACTIVE QUESTIONS](#7-🗣️-interactive-questions)

---

<a id="1-🎫-ticket-mode-overview"></a>

## 1. 🎫 TICKET MODE OVERVIEW

### Command: `$ticket` or `$story`

- **Purpose:** Create development tickets or user stories that auto-scale complexity
- **Output:** Always as artifact
- **Thinking:** 10 rounds automatic (ultrathink), 1-5 auto-scaled for $quick
- **Interactive Mode:** Asks ticket vs story, Figma MCP connection
- **Key Difference:** Stories omit Resolution Checklist

---

<a id="2-📝-complexity-auto-scaling"></a>

## 2. 📝 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Sections | Resolution Items |
|----------|------------|----------|------------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 |
| feature, dashboard, api | Standard | 4-5 | 8-12 |
| platform, architecture, migration | Complex | 6-8 | 12-20 |

---

<a id="3-🔵-simple-ticket-template-2-3-sections-4-6-resolution"></a>

## 3. 🔵 SIMPLE TICKET TEMPLATE (2-3 SECTIONS, 4-6 RESOLUTION)

```markdown
[SCOPE] Bug Fix: [Feature Name]

# ⌘ About

[Brief description of the issue and its impact on users and business operations. 
This includes context about why this needs fixing and the problems it's causing 
for users - integrated naturally into the description rather than as separate sections.]

---

## ✦ Success Criteria

- Issue resolved and verified in production environment
- No regression in existing functionality
- Performance metrics maintained or improved

---

## ⌥ Designs & References

| Type | Resource | Status | Link |
|------|----------|--------|------|
| Bug Report | JIRA-123 | Open | [Link - to be added] |
| Screenshot | Error State | Captured | [Link - to be added] |
| Documentation | API Spec | Current | [Link - to be added] |

---

## ■ Requirements

### ◻️ Functional Requirements

- Fix [specific issue with clear description]
- Ensure [expected behavior after fix]
- Validate [edge cases to check]

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[] Identify root cause through debugging
[] Implement fix with appropriate solution
[] Test fix locally with various scenarios
[] Update unit tests if needed
[] Verify no regressions occur
[] Document fix in PR description

---
Mode: $ticket | Complexity: Simple | Template: v0.121
```

---

<a id="4-🟠-standard-ticket-template-4-5-sections-8-12-resolution"></a>

## 4. 🟠 STANDARD TICKET TEMPLATE (4-5 SECTIONS, 8-12 RESOLUTION)

```markdown
[SCOPE] Feature: [Feature Name]

# ⌘ About

[Comprehensive description of the feature, its purpose, and how it delivers value to users 
and the business. This narrative naturally incorporates the problems this feature solves, 
why it matters for users, the business value and ROI expectations, and competitive advantages 
- all woven into a cohesive description rather than listed separately.]

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
| Design | Figma Mockups | Complete | [Figma - to be added] |
| PRD | Product Requirements | Approved | [Doc - to be added] |
| API | Endpoint Spec | Draft | [Swagger - to be added] |
| Tech Spec | Architecture | In Review | [Wiki - to be added] |

---

## ■ Requirements

### ◻️ Functional Requirements

- Primary requirement with clear acceptance criteria
- Secondary requirement with measurable outcome
- Tertiary requirement with defined scope

### ◻️ Non-Functional Requirements

- Performance requirement (e.g., <200ms response time)
- Security requirement (e.g., OAuth 2.0 implementation)
- Accessibility requirement (e.g., WCAG 2.1 AA compliance)

### ◻️ Technical Requirements

- Backend API changes needed
- Frontend framework requirements
- Database schema modifications

---

## ■ User Stories

**As a** [primary user type]
**I want to** [specific action or capability]
**So that** [business or personal benefit achieved]

**As a** [secondary user type]
**I want to** [specific action or capability]
**So that** [business or personal benefit achieved]

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

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

---
Mode: $ticket | Complexity: Standard | Template: v0.121
```

---

<a id="5-🔴-complex-ticket-template-6-8-sections-12-20-resolution"></a>

## 5. 🔴 COMPLEX TICKET TEMPLATE (6-8 SECTIONS, 12-20 RESOLUTION)

```markdown
[SCOPE] Platform: [Platform/Architecture Name]

# ⌘ About

[Detailed description of the platform/architecture change, its strategic importance, and long-term vision.
This comprehensive narrative includes the critical scalability limitations affecting growth, 
technical debt preventing feature velocity, security or compliance gaps requiring resolution,
performance bottlenecks impacting user experience, along with strategic business objective alignment,
cost reduction or efficiency gains, risk mitigation needs, and competitive advantages - 
all integrated into a cohesive overview rather than listed as separate problems and reasons.]

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
| API | Integration Specs | Review | [Swagger - to be added] |

---

## ■ Requirements

### ◻️ Functional Requirements

- Core platform capability with detailed specifications
- Integration requirements with existing systems
- Data migration and transformation needs
- User-facing feature modifications

### ◻️ Non-Functional Requirements

- Scalability requirement (e.g., 10,000 concurrent users)
- Performance requirement (e.g., 99.9% uptime SLA)
- Security requirement (e.g., SOC 2 compliance)
- Compliance requirement (e.g., GDPR, CCPA)

### ◻️ Integration Requirements

- System integration with service A
- API compatibility with existing clients
- Data synchronization requirements
- Third-party service connections

---

## ■ User Stories

**PRD: [PRD Name]**

**Story 1: Core Platform Capability**
**As a** [user type]
**I want to** [capability enabled by platform]
**So that** [business value achieved]

**Story 2: Migration Experience**
**As a** [existing user]
**I want to** [seamless transition]
**So that** [no disruption to workflow]

**Story 3: New Capabilities**
**As a** [power user]
**I want to** [advanced features]
**So that** [enhanced productivity]

---

## ∅ Risks & Mitigations

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| **Data loss during migration** | High | Low | Comprehensive backups, dry runs, validation scripts |
| **Extended downtime** | High | Medium | Blue-green deployment, feature flags, staged rollout |
| **Performance degradation** | Medium | Low | Load testing, performance monitoring, optimization plan |
| **Integration failures** | Medium | Medium | Contract testing, sandbox environment, fallback APIs |

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

### ◻️ Planning & Design
[] Complete technical design review
[] Obtain stakeholder approval
[] Finalize migration strategy
[] Document rollback procedures

### ◻️ Development & Testing
[] Set up development environment
[] Implement Phase 1 components
[] Create comprehensive test suite
[] Perform security audit
[] Complete load testing
[] Document all APIs

### ◻️ Integration & Validation
[] Conduct integration testing
[] Validate data migration scripts
[] Perform user acceptance testing
[] Verify monitoring coverage

### ◻️ Deployment & Operations
[] Create deployment runbooks
[] Train support team
[] Execute staged deployment
[] Monitor system metrics
[] Complete performance optimization
[] Update all documentation

---
Mode: $ticket | Complexity: Complex | Template: v0.121
```

---

<a id="6-✨-ticket-formatting-rules"></a>

## 6. ✨ TICKET FORMATTING RULES

### Mandatory Elements

1. **[SCOPE]** prefix before title
2. **About section FIRST** with integrated problems/reasons
3. **Success Criteria AFTER About** (not at top)
4. **QA Warning** - Above resolution checklist
5. **Symbol usage** - As per hierarchy
6. **Dividers** - Use `---` between ALL major sections
7. **Designs as Table** - Not bullet lists
8. **Minimal Footer** - Single line with mode, complexity, template

### Symbol Reference

- **⌘** - About section (H1)
- **■** - Main sections (H1) 
- **◻️** - Sub-sections (H2)
- **⌥** - Designs & References (H2)
- **✦** - Success Criteria (H2)
- **✓** - Resolution Checklist (H2)
- **∅** - Risks (H2, Complex tickets only)

### Structure Order

1. Title with [SCOPE]
2. About (⌘) - Context and integrated problems
3. Success Criteria (✦) - Measurable outcomes
4. Designs & References (⌥) - Table format
5. Requirements (■) - Detailed specifications
6. User Stories (■) - If applicable
7. Risks (∅) - Complex tickets only
8. Resolution Checklist (✓) - QA items
9. Footer - Minimal single line

### Formatting Standards

- Use consistent spacing between sections
- Tables for complex comparisons and designs
- Always include "to be added" for placeholder links
- Use `-` (hyphen + space) for all regular list items
- Use `[]` for checkboxes in Resolution Checklist (no spaces)
- Each checkbox item on its own line
- Minimal footer at bottom

### Correct Formatting Examples

**Correct Table for Designs:**
```markdown
| Type | Resource | Status | Link |
|------|----------|--------|------|
| Design | UI Flow | Ready | [Figma] |
| API | Endpoints | Draft | [Swagger] |
```

**Correct Footer:**
```markdown
Mode: $ticket | Complexity: Standard | Template: v0.121
```

---

<a id="7-🗣️-interactive-questions"></a>

## 7. 🗣️ INTERACTIVE QUESTIONS

### Initial Interactive Flow

```markdown
User: $ticket payment integration

System: Let me help you create the right format for your needs.

**Applying deep ATLAS analysis (10 rounds automatic)...**

**Question 1: Is this a ticket or a story?**
- Ticket = Development task with resolution checklist for QA
- Story = User story format without checklist

[WAIT FOR USER RESPONSE]

User: ticket

System: **Question 2: Can I connect to Figma MCP to inspect your designs?**
- Yes = I'll pull design details directly
- No = I'll add placeholders for you to fill

[WAIT FOR USER RESPONSE]

User: no

System: **Question 3: What's the scope?** (BE/FE/Mobile/FS/DevOps/QA)

[WAIT FOR USER RESPONSE]

User: BE

System: Creating your backend payment integration ticket...
- 10-round ultrathink applied automatically
- Success criteria positioned after About section
[Creates ticket based on complexity detected with minimal footer]
```

### Story Format (When Selected)

When user selects "Story", the template omits the Resolution Checklist:

```markdown
[SCOPE] Story: [Name]

# ⌘ About
[Same narrative format with integrated problems]

## ✦ Success Criteria
[Positioned after About section]

## ⌥ Designs & References
[Same table format]

## ■ Requirements
[Same structure]

## ■ User Stories
[Same format]

[NOTE: No Resolution Checklist for stories]

---
Mode: $story | Complexity: [level] | Template: v0.121
```