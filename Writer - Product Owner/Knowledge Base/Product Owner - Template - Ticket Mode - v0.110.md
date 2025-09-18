# Product Owner - Template - Ticket Mode - v0.110

## 📋 TABLE OF CONTENTS

1. [🎫 TICKET MODE OVERVIEW](#1-🎫-ticket-mode-overview)
2. [🔍 COMPLEXITY AUTO-SCALING](#2-🔍-complexity-auto-scaling)
3. [🔵 SIMPLE TICKET TEMPLATE](#3-🔵-simple-ticket-template-2-3-sections-4-6-resolution)
4. [🔶 STANDARD TICKET TEMPLATE](#4-🔶-standard-ticket-template-4-5-sections-8-12-resolution)
5. [🔴 COMPLEX TICKET TEMPLATE](#5-🔴-complex-ticket-template-6-8-sections-12-20-resolution)
6. [✨ TICKET FORMATTING RULES](#6-✨-ticket-formatting-rules)
7. [🗣️ INTERACTIVE QUESTIONS](#7-🗣️-interactive-questions)

---

## 1. 🎫 TICKET MODE OVERVIEW

### Command: `$ticket`

- **Purpose:** Create development tickets that auto-scale complexity
- **Output:** Always as artifact
- **Thinking Rounds:** 6-10
- **Challenge Activation:** 6+ rounds

---

## 2. 🔍 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Sections | Resolution Items |
|----------|------------|----------|------------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 |
| feature, dashboard, api | Standard | 4-5 | 8-12 |
| platform, architecture, migration | Complex | 6-8 | 12-20 |

---

## 3. 🔵 SIMPLE TICKET TEMPLATE (2-3 SECTIONS, 4-6 RESOLUTION)

```markdown
[SCOPE] Bug Fix: [Feature Name]

## 📋 Table of Contents
- [⌘ About](#⌘-about)
- [→ Designs & References](#→-designs--references)
- [❖ Requirements](#❖-requirements)
- [✦ Success Criteria](#✦-success-criteria)
- [✓ Resolution Checklist](#✓-resolution-checklist)

---

# ⌘ About

[Brief description of the issue and its impact on users and business operations]

---

### → Key problems:
- First specific problem that users are experiencing
- Second specific problem affecting functionality

### → Reasons why:
- Business value of fixing this issue
- User experience improvement expected

---

## → Designs & References

- [Link to bug report - to be added]
- [Screenshots/videos - to be added]
- [Related documentation - to be added]

---

## ❖ Requirements

### ◻︎ Functional Requirements

- Fix [specific issue with clear description]
- Ensure [expected behavior after fix]
- Validate [edge cases to check]

---

## ✦ Success Criteria

- Issue resolved and verified in production environment
- No regression in existing functionality
- Performance metrics maintained or improved

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[ ] Identify root cause through debugging
[ ] Implement fix with appropriate solution
[ ] Test fix locally with various scenarios
[ ] Update unit tests if needed
[ ] Verify no regressions occur
[ ] Document fix in PR description
```

---

## 4. 🔶 STANDARD TICKET TEMPLATE (4-5 SECTIONS, 8-12 RESOLUTION)

```markdown
[SCOPE] Feature: [Feature Name]

## 📋 Table of Contents
- [⌘ About](#⌘-about)
- [→ Designs & References](#→-designs--references)
- [❖ Requirements](#❖-requirements)
- [❖ User Stories](#❖-user-stories)
- [✦ Success Criteria](#✦-success-criteria)
- [✓ Resolution Checklist](#✓-resolution-checklist)
- [≈ Dependencies](#≈-dependencies)

---

# ⌘ About

[Comprehensive description of the feature, its purpose, and how it delivers value to users and the business]

[Additional context about the current state and desired future state]

---

### → Key problems:
- First problem this feature solves for users
- Second problem affecting current workflow
- Third problem impacting business metrics

### → Reasons why:
- Business value and ROI expectations
- User experience improvements
- Competitive advantage or parity

---

## → Designs & References

- [Figma designs - to be added]
- [PRD document - to be added]
- [API documentation - to be added]
- [Technical specifications - to be added]

---

## ❖ Requirements

### ◻︎ Functional Requirements

- Primary requirement with clear acceptance criteria
- Secondary requirement with measurable outcome
- Tertiary requirement with defined scope

### ◻︎ Non-Functional Requirements

- Performance requirement (e.g., <200ms response time)
- Security requirement (e.g., OAuth 2.0 implementation)
- Accessibility requirement (e.g., WCAG 2.1 AA compliance)

### ◻︎ Technical Requirements

- Backend API changes needed
- Frontend framework requirements
- Database schema modifications

---

## ❖ User Stories

**As a** [primary user type]
**I want to** [specific action or capability]
**So that** [business or personal benefit achieved]

**As a** [secondary user type]
**I want to** [specific action or capability]
**So that** [business or personal benefit achieved]

---

## ✦ Success Criteria

- Measurable outcome with specific metrics
- User acceptance criteria clearly defined
- Performance benchmarks achieved
- Analytics tracking implemented

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[ ] Implement core functionality per requirements
[ ] Add comprehensive input validation
[ ] Handle all identified error cases
[ ] Write unit tests (>80% coverage)
[ ] Write integration tests for workflows
[ ] Update API documentation
[ ] Add analytics tracking events
[ ] Perform security review
[ ] Test on all supported browsers
[ ] Verify mobile responsiveness
[ ] Get design approval on implementation
[ ] Complete code review with team

---

## ≈ Dependencies

- External API integration requirements
- Database schema migration needs
- Third-party library updates required
- DevOps configuration changes
```

---

## 5. 🔴 COMPLEX TICKET TEMPLATE (6-8 SECTIONS, 12-20 RESOLUTION)

```markdown
[SCOPE] Platform: [Platform/Architecture Name]

## 📋 Table of Contents
- [⌘ About](#⌘-about)
- [→ Designs & References](#→-designs--references)
- [❖ Requirements](#❖-requirements)
- [❖ Technical Architecture](#❖-technical-architecture)
- [❖ User Stories](#❖-user-stories)
- [❖ Migration Strategy](#❖-migration-strategy)
- [∅ Risks & Mitigations](#∅-risks--mitigations)
- [✦ Success Criteria](#✦-success-criteria)
- [✓ Resolution Checklist](#✓-resolution-checklist)
- [≈ Dependencies](#≈-dependencies)

---

# ⌘ About

[Detailed description of the platform/architecture change, its strategic importance, and long-term vision]

[Context about current limitations and how this initiative addresses them]

[Expected impact on users, business metrics, and technical capabilities]

---

### → Key problems:
- Critical scalability limitation affecting growth
- Technical debt preventing feature velocity
- Security or compliance gap requiring resolution
- Performance bottleneck impacting user experience

### → Reasons why:
- Strategic business objective alignment
- Cost reduction or efficiency gains
- Risk mitigation and compliance needs
- Competitive advantage or market requirements

---

## → Designs & References

- [System architecture diagrams - to be added]
- [Technical specifications - to be added]
- [Migration documentation - to be added]
- [Performance benchmarks - to be added]
- [Security assessment - to be added]

---

## ❖ Requirements

### ◻︎ Functional Requirements

- Core platform capability with detailed specifications
- Integration requirements with existing systems
- Data migration and transformation needs
- User-facing feature modifications

### ◻︎ Non-Functional Requirements

- Scalability requirement (e.g., 10,000 concurrent users)
- Performance requirement (e.g., 99.9% uptime SLA)
- Security requirement (e.g., SOC 2 compliance)
- Compliance requirement (e.g., GDPR, CCPA)

### ◻︎ Integration Requirements

- System integration with service A
- API compatibility with existing clients
- Data synchronization requirements
- Third-party service connections

---

## ❖ Technical Architecture

### ◻︎ Current State

- Existing architecture overview and limitations
- Current technology stack and versions
- Performance metrics and bottlenecks
- Technical debt identification

### ◻︎ Target State

- New architecture design and benefits
- Technology stack updates and rationale
- Expected performance improvements
- Scalability and maintenance advantages

### ◻︎ Technology Stack
---
#### ◊ Framework & Runtime
- Framework changes and versions
- Runtime environment specifications
- Package management strategy
---
#### ◊ Infrastructure
- Cloud provider and services
- Container orchestration platform
- CI/CD pipeline configuration
---
#### ◊ Data Layer
- Database technology decisions
- Caching strategy and tools
- Message queue implementation
---
#### ◊ Monitoring
- Observability platform
- Logging aggregation service
- Performance monitoring tools
- Error tracking system

---

## ❖ User Stories

**Epic: [Epic Name]**

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

## ❖ Migration Strategy

### ◻︎ Phase 1: Preparation (Week 1-2)
---
#### ◊ Environment Setup
- Development environment configuration
- Staging environment preparation
- Production environment planning
---
#### ◊ Data Preparation
- Data backup procedures
- Migration script development
- Validation script creation
---
#### ◊ Team Readiness
- Team training sessions
- Documentation preparation
- Support plan development

### ◻︎ Phase 2: Implementation (Week 3-6)
---
---
#### ◊ Core Deployment
- Platform components deployment
- Service integration setup
- Configuration management
---
#### ◊ Data Migration
- Initial data migration execution
- Data validation and reconciliation
- Performance baseline establishment
---
#### ◊ Testing
- Integration testing execution
- Performance testing completion
- Security testing validation

### ◻︎ Phase 3: Cutover (Week 7-8)
---
#### ◊ Production Preparation
- Production deployment checklist
- Rollback procedures documentation
- Monitoring setup completion
---
#### ◊ Go-Live
- Traffic routing configuration
- Load balancing setup
- Feature flag activation
---
#### ◊ Post-Launch
- Performance monitoring
- Issue triage process
- Optimization execution

---

## ∅ Risks & Mitigations

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| **Data loss during migration** | High | Low | Comprehensive backups, dry runs, validation scripts |
| **Extended downtime** | High | Medium | Blue-green deployment, feature flags, staged rollout |
| **Performance degradation** | Medium | Low | Load testing, performance monitoring, optimization plan |
| **Integration failures** | Medium | Medium | Contract testing, sandbox environment, fallback APIs |

---

## ✦ Success Criteria

- All systems migrated with zero data loss
- Performance metrics meet or exceed targets
- 99.9% uptime maintained during migration
- User acceptance testing passed
- Compliance requirements verified
- Cost savings targets achieved

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

### ◻︎ Planning & Design
[ ] Complete technical design review
[ ] Obtain stakeholder approval
[ ] Finalize migration strategy
[ ] Document rollback procedures

### ◻︎ Development & Testing
[ ] Set up development environment
[ ] Implement Phase 1 components
[ ] Create comprehensive test suite
[ ] Perform security audit
[ ] Complete load testing
[ ] Document all APIs

### ◻︎ Integration & Validation
[ ] Conduct integration testing
[ ] Validate data migration scripts
[ ] Perform user acceptance testing
[ ] Verify monitoring coverage

### ◻︎ Deployment & Operations
[ ] Create deployment runbooks
[ ] Train support team
[ ] Execute staged deployment
[ ] Monitor system metrics
[ ] Complete performance optimization
[ ] Update all documentation

---

## ≈ Dependencies

- Infrastructure provisioning and access
- Third-party service agreements
- Security and compliance approvals
- Budget allocation confirmation
- Team availability and expertise
- External vendor coordination
```

---

## 6. ✨ TICKET FORMATTING RULES

### Mandatory Elements

1. **[SCOPE]** prefix before title
2. **Table of Contents** - sections only (no subsections)
3. **Key Problems/Reasons** - NOT in TOC, formatted as H3 with →
4. **QA Warning** - Above resolution checklist
5. **Symbol usage** - As per hierarchy
6. **Dividers** - Use `---` between ALL major sections

### Symbol Reference

- **⌘** - About section (H1)
- **❖** - Main sections (H2) 
- **◻︎** - Sub-sections (H3)
- **◊** - Children of Sub-sections (H4)
- **—** - Bold text sub-headings within H4 sub-section groups (Not a H[x] heading)
- **→** - Key Problems/Reasons/References
- **✦** - Success Criteria
- **✓** - Resolution Checklist
- **≈** - Dependencies
- **∅** - Risks

### Formatting Standards

- Use consistent spacing between sections
- Tables for complex comparisons
- Always include "to be added" for placeholder links
- Use `**—**` for bold sub-headings within H4 sub-section groups
- Use `- ` (hyphen + space) for all regular list items
- Use `[ ]` for checkboxes in Resolution Checklist (no hyphen before)
    - Each checkbox item on its own line

### Correct Formatting Examples

**Correct Format for Simple Lists:**
```markdown
### ◻︎ Functional Requirements

- First requirement
- Second requirement
- Third requirement
```

**Correct Format with Bold Sub-headings:**
```markdown
#### ◊ Technology Stack
---
**— Backend Requirements**
- API endpoint implementation
- Database schema updates
---
**— Frontend Requirements**
- UI component development
- State management setup
---
```

**Correct Resolution Checklist Format:**
```markdown
### ◻︎ Planning & Design
[ ] Complete technical design review
[ ] Obtain stakeholder approval
[ ] Finalize migration strategy
```

**Incorrect Formats:**
```markdown
### ◊ Functional Requirements

— First requirement  ❌ (em dash for list items)
* Second requirement ❌ (asterisk for list items)

- [ ] Checkbox item  ❌ (hyphen before checkbox)
#### — Subheading  ❌ (H4 with em dash instead of bold)
```

---

## 7. 🗣️ INTERACTIVE QUESTIONS

### Initial Flow (Wait For Responses)

```markdown
User: $ticket payment integration

System: Let's create your payment integration ticket! 🎯

**How many thinking rounds should I use? (6-10)**

Based on payment integration complexity, I recommend: 8 rounds
- Complexity: High (multiple providers, compliance)
- Uncertainty: Medium (integration patterns)
- Stakes: High (financial, regulatory)

Your choice?

[WAIT FOR USER INPUT]

User: 8

System: [If 6+ rounds, present challenge]

Before we proceed, could we simplify the scope?
- Option A: Full multi-provider integration (8 rounds)
- Option B: Single provider MVP first (6 rounds)
- Option C: Use existing payment service (6 rounds)

Which approach? (A/B/C)

[WAIT FOR USER RESPONSE]

User: B

System: Great! Single provider MVP approach.

Two quick questions:
1. Which payment provider? (Stripe/PayPal/Other)
2. What's the primary use case? (Subscriptions/One-time/Both)

[WAIT FOR ANSWERS]

[THEN CREATE TICKET]
```

### Complexity Detection

```python
def detect_complexity(request):
    simple_keywords = ['bug', 'fix', 'typo', 'update', 'change']
    standard_keywords = ['feature', 'dashboard', 'api', 'integration']
    complex_keywords = ['platform', 'architecture', 'migration', 'infrastructure']

    if any(k in request.lower() for k in complex_keywords):
        return 'complex'
    elif any(k in request.lower() for k in standard_keywords):
        return 'standard'
    else:
        return 'simple'
```

---

*All tickets delivered as artifacts with auto-scaled complexity. Always ask thinking rounds and wait for response. Challenge when 6+ rounds. Use proper symbols and formatting. Include AI System footer with process documentation