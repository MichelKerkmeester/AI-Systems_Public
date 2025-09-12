# Product Owner - Template - Ticket Mode - v0.104

## 📋 Table Of Contents

1. [🎫 Ticket Mode Overview](#1-🎫-ticket-mode-overview)
2. [📊 Complexity Auto-Scaling](#2-📊-complexity-auto-scaling)
3. [📝 Simple Ticket Template](#3-📝-simple-ticket-template-2-3-sections-4-6-resolution)
4. [📝 Standard Ticket Template](#4-📝-standard-ticket-template-4-5-sections-8-12-resolution)
5. [📝 Complex Ticket Template](#5-📝-complex-ticket-template-6-8-sections-12-20-resolution)
6. [🎯 Ticket Formatting Rules](#6-🎯-ticket-formatting-rules)
7. [💬 Interactive Questions](#7-💬-interactive-questions)

---

## 1. 🎫 Ticket Mode Overview

### Command: `$ticket`

- **Purpose:** Create development tickets that auto-scale complexity
- **Output:** Always as artifact
- **Thinking Rounds:** 6-10
- **Challenge Activation:** 6+ rounds

---

## 2. 📊 Complexity Auto-Scaling

| Keywords | Complexity | Sections | Resolution Items |
|----------|------------|----------|------------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 |
| feature, dashboard, api | Standard | 4-5 | 8-12 |
| platform, architecture, migration | Complex | 6-8 | 12-20 |

---

## 3. 📝 Simple Ticket Template (2-3 Sections, 4-6 Resolution)

```markdown
[SCOPE] Bug Fix: [Feature Name]

## 📋 Table of Contents
- [◆ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)

---

# ◆ About

[Brief description of the issue and its impact on users and business operations]

---

### → Key problems:
- First specific problem that users are experiencing
- Second specific problem affecting functionality

### → Reasons why:
- Business value of fixing this issue
- User experience improvement expected

---

## ◳ Designs & References

- [Link to bug report - to be added]
- [Screenshots/videos - to be added]
- [Related documentation - to be added]

---

## ◇ Requirements

**◊ Functional Requirements**

— Fix [specific issue with clear description]
— Ensure [expected behavior after fix]
— Validate [edge cases to check]

---

## ✦ Success Criteria

- Issue resolved and verified in production environment
- No regression in existing functionality
- Performance metrics maintained or improved

---

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

- [ ] Identify root cause through debugging
- [ ] Implement fix with appropriate solution
- [ ] Test fix locally with various scenarios
- [ ] Update unit tests if needed
- [ ] Verify no regressions occur
- [ ] Document fix in PR description
```

---

## 4. 📝 Standard Ticket Template (4-5 Sections, 8-12 Resolution)

```markdown
[SCOPE] Feature: [Feature Name]

## 📋 Table of Contents
- [◆ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [💥 User Stories](#-user-stories)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)
- [≈ Dependencies](#-dependencies)

---

# ◆ About

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

## ◳ Designs & References

- [Figma designs - to be added]
- [PRD document - to be added]
- [API documentation - to be added]
- [Technical specifications - to be added]

---

## ◇ Requirements

**◊ Functional Requirements**

— Primary requirement with clear acceptance criteria
— Secondary requirement with measurable outcome
— Tertiary requirement with defined scope

**◊ Non-Functional Requirements**

— Performance requirement (e.g., <200ms response time)
— Security requirement (e.g., OAuth 2.0 implementation)
— Accessibility requirement (e.g., WCAG 2.1 AA compliance)

**◊ Technical Requirements**

— Backend API changes needed
— Frontend framework requirements
— Database schema modifications

---

## 💥 User Stories

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

- [ ] Implement core functionality per requirements
- [ ] Add comprehensive input validation
- [ ] Handle all identified error cases
- [ ] Write unit tests (>80% coverage)
- [ ] Write integration tests for workflows
- [ ] Update API documentation
- [ ] Add analytics tracking events
- [ ] Perform security review
- [ ] Test on all supported browsers
- [ ] Verify mobile responsiveness
- [ ] Get design approval on implementation
- [ ] Complete code review with team

---

## ≈ Dependencies

- External API integration requirements
- Database schema migration needs
- Third-party library updates required
- DevOps configuration changes
```

---

## 5. 📝 Complex Ticket Template (6-8 Sections, 12-20 Resolution)

```markdown
[SCOPE] Platform: [Platform/Architecture Name]

## 📋 Table of Contents
- [◆ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [🗓 Technical Architecture](#-technical-architecture)
- [💥 User Stories](#-user-stories)
- [🔄 Migration Strategy](#-migration-strategy)
- [∅ Risks & Mitigations](#-risks--mitigations)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)
- [≈ Dependencies](#-dependencies)

---

# ◆ About

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

## ◳ Designs & References

- [System architecture diagrams - to be added]
- [Technical specifications - to be added]
- [Migration documentation - to be added]
- [Performance benchmarks - to be added]
- [Security assessment - to be added]

---

## ◇ Requirements

**◊ Functional Requirements**

— Core platform capability with detailed specifications
— Integration requirements with existing systems
— Data migration and transformation needs
— User-facing feature modifications

**◊ Non-Functional Requirements**

— Scalability requirement (e.g., 10,000 concurrent users)
— Performance requirement (e.g., 99.9% uptime SLA)
— Security requirement (e.g., SOC 2 compliance)
— Compliance requirement (e.g., GDPR, CCPA)

**◊ Integration Requirements**

— System integration with service A
— API compatibility with existing clients
— Data synchronization requirements
— Third-party service connections

---

## 🗓 Technical Architecture

**◊ Current State**

— Existing architecture overview and limitations
— Current technology stack and versions
— Performance metrics and bottlenecks
— Technical debt identification

**◊ Target State**

— New architecture design and benefits
— Technology stack updates and rationale
— Expected performance improvements
— Scalability and maintenance advantages

**◊ Technology Stack**

— Framework changes and versions
— Infrastructure updates (cloud, containers)
— Database technology decisions
— Monitoring and observability tools

---

## 💥 User Stories

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

## 🔄 Migration Strategy

**◊ Phase 1: Preparation (Week 1-2)**

— Environment setup and configuration
— Data backup and recovery procedures
— Dependency installation and verification
— Team training and documentation

**◊ Phase 2: Implementation (Week 3-6)**

— Core platform components deployment
— Data migration execution
— Integration testing and validation
— Performance baseline establishment

**◊ Phase 3: Cutover (Week 7-8)**

— Production deployment preparation
— Traffic routing and load balancing
— Monitoring and alerting setup
— Rollback procedures documentation

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

**Planning & Design**
- [ ] Complete technical design review
- [ ] Obtain stakeholder approval
- [ ] Finalize migration strategy
- [ ] Document rollback procedures

**Development & Testing**
- [ ] Set up development environment
- [ ] Implement Phase 1 components
- [ ] Create comprehensive test suite
- [ ] Perform security audit
- [ ] Complete load testing
- [ ] Document all APIs

**Integration & Validation**
- [ ] Conduct integration testing
- [ ] Validate data migration scripts
- [ ] Perform user acceptance testing
- [ ] Verify monitoring coverage

**Deployment & Operations**
- [ ] Create deployment runbooks
- [ ] Train support team
- [ ] Execute staged deployment
- [ ] Monitor system metrics
- [ ] Complete performance optimization
- [ ] Update all documentation

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

## 6. 🎯 Ticket Formatting Rules

### Mandatory Elements

1. **[SCOPE]** prefix before title
2. **Table of Contents** - sections only (no subsections)
3. **Key Problems/Reasons** - NOT in TOC, formatted as H3
4. **QA Warning** - Above resolution checklist
5. **Symbol usage** - As per symbol guide
6. **Dividers** - Use `---` between ALL major sections

### Symbol Reference

- **◆** - About section
- **◇** - Requirements
- **◊** - Sub-headings (bold)
- **◳** - Designs & References
- **→** - Key Problems/Reasons (H3)
- **✦** - Success Criteria
- **✓** - Resolution Checklist
- **≈** - Dependencies
- **∅** - Risks
- **💥** - User Stories
- **🗓** - Technical Architecture
- **🔄** - Migration/Process

### Formatting Standards

- Use `- [ ]` for checkboxes in Resolution Checklist (with space)
- Each checkbox item on its own line
- Use `—` for requirement items (em dash)
- Use `-` for bullet points (hyphen)
- Bold all sub-headings with **◊**
- Always include "to be added" for placeholder links
- Use consistent spacing between sections
- Tables for complex comparisons

### Checklist Formatting

**Correct Format:**
```markdown
- [ ] First item with clear action
- [ ] Second item with measurable outcome
- [ ] Third item with specific deliverable
```

**Incorrect Format:**
```markdown
[] First item [] Second item [] Third item
```

---

## 7. 💬 Interactive Questions

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

*All tickets delivered as artifacts with auto-scaled complexity. Always ask thinking rounds and wait for response. Challenge when 6+ rounds. Use proper symbols and formatting. Include AI System footer with process documentation.*
