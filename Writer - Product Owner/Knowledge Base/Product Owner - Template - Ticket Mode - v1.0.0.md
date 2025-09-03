# Product Owner - Template: Ticket Mode - v1.0.0

## 📋 Table of Contents

1. [🎫 TICKET MODE OVERVIEW](#-ticket-mode-overview)
2. [📊 COMPLEXITY AUTO-SCALING](#-complexity-auto-scaling)
3. [📝 SIMPLE TICKET TEMPLATE](#-simple-ticket-template-2-3-sections-4-6-resolution)
4. [📝 STANDARD TICKET TEMPLATE](#-standard-ticket-template-4-5-sections-8-12-resolution)
5. [📝 COMPLEX TICKET TEMPLATE](#-complex-ticket-template-6-8-sections-12-20-resolution)
6. [🎯 TICKET FORMATTING RULES](#-ticket-formatting-rules)
7. [💬 INTERACTIVE QUESTIONS](#-interactive-questions)
8. [📦 PLATFORM INTEGRATION](#-platform-integration)

---

## 🎫 TICKET MODE OVERVIEW

### Command: `$ticket`

- **Purpose:** Create development tickets that auto-scale complexity
- **Output:** Always as artifact
- **Thinking Rounds:** 1-10
- **Challenge Activation:** 3+ rounds

---

## 📊 Complexity Auto-Scaling

| Keywords | Complexity | Sections | Resolution Items |
|----------|------------|----------|------------------|
| bug, fix, typo, update | Simple | 2-3 | 4-6 |
| feature, dashboard, api | Standard | 4-5 | 8-12 |
| platform, architecture, migration | Complex | 6-8 | 12-20 |

---

## 📝 SIMPLE TICKET TEMPLATE (2-3 sections, 4-6 resolution)

```markdown
[SCOPE] Bug Fix: [Feature Name]

## 📋 Table of Contents
- [⌘ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)

# ⌘ About

[Brief description of the issue and its impact]

---

### → Key problems:
- [First problem - what's broken]
- [Second problem - impact on users]

### → Reasons why:
- [Business impact with metrics]
- [User impact with numbers]

---

## ◳ Designs & References
- [Figma designs - to be added]
- [Error logs - to be added]
- [Related documentation - to be added]

---

## ◇ Requirements

**◊ Fix Implementation**
— Technical Details
- [Specific fix requirement]
- [Validation requirement]
- [Testing requirement]

---

## ✦ Success Criteria
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Response time/performance metric]

---

## ✔ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[] [Specific fix action]
[] [Testing verification]
[] [Staging deployment]
[] [Monitoring setup]
[] [Documentation update]

**Labels:** bug, [priority], [component]
```

---

## 📝 STANDARD TICKET TEMPLATE (4-5 sections, 8-12 resolution)

```markdown
[SCOPE] Feature: [Feature Name]

## 📋 Table of Contents
- [⌘ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)
- [⋈ Dependencies](#-dependencies)

# ⌘ About

[Feature overview explaining what we're building and why]

---

### → Key problems:
- [User pain point 1]
- [User pain point 2]
- [Business challenge]

### → Reasons why:
- [Business value with ROI]
- [User benefit with metrics]
- [Strategic alignment]

---

## ◳ Designs & References
- [Figma designs - to be added]
- [User flows - to be added]
- [API documentation - to be added]
- [Competitor analysis - to be added]

---

## ◇ Requirements

**◊ Frontend Requirements**
— User Interface
- [Component requirement]
- [Interaction requirement]
- [Responsive design requirement]

**◊ Backend Requirements**
— API & Data
- [Endpoint requirement]
- [Data model requirement]
- [Performance requirement]

**◊ Business Logic**
— Core Functionality
- [Rule implementation]
- [Validation logic]
- [Error handling]

---

## ✦ Success Criteria
- [User can complete primary action]
- [Performance metric achieved]
- [Business metric improved]
- [Error rate below threshold]

---

## ✔ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[] Frontend components implemented
[] API endpoints created and tested
[] Data migrations completed
[] Unit tests passing (>80% coverage)
[] Integration tests completed
[] Performance benchmarks met
[] Security review passed
[] Documentation updated
[] Staging deployment verified
[] Feature flags configured
[] Monitoring dashboards created
[] Rollback plan documented

---

## ⋈ Dependencies
- [External service requirement]
- [Team coordination needed]
- [Third-party integration]

**Labels:** feature, [priority], [sprint]
```

---

## 📝 COMPLEX TICKET TEMPLATE (6-8 sections, 12-20 resolution)

```markdown
[SCOPE] Platform: [Initiative Name]

## 📋 Table of Contents
- [⌘ About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [📊 Phasing Strategy](#-phasing-strategy)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)
- [⋈ Dependencies](#-dependencies)
- [∅ Risks & Mitigations](#-risks--mitigations)

# ⌘ About

[Comprehensive overview of the platform/initiative including context, goals, and expected impact]

---

### → Key problems:
- [System-level challenge 1]
- [Architecture limitation 2]
- [Business constraint 3]
- [User experience gap 4]

### → Reasons why:
- [Strategic business imperative]
- [Market opportunity with TAM]
- [Technical debt reduction]
- [Competitive advantage]

---

## ◳ Designs & References
- [System architecture diagrams - to be added]
- [Detailed Figma designs - to be added]
- [Technical specifications - to be added]
- [Migration plans - to be added]
- [API contracts - to be added]
- [Security assessments - to be added]

---

## ◇ Requirements

**◊ Phase 1: Foundation**
— Core Infrastructure
- [Database architecture requirement]
- [Service mesh setup]
- [Authentication system]
- [Monitoring foundation]

**◊ Phase 2: Core Features**
— Primary Functionality
- [Feature set 1 requirements]
- [Feature set 2 requirements]
- [Integration requirements]
- [Performance requirements]

**◊ Phase 3: Advanced Capabilities**
— Enhanced Features
- [Advanced feature 1]
- [Advanced feature 2]
- [Optimization requirements]

**◊ Technical Requirements**
— Architecture & Performance
- [Scalability requirements]
- [Security requirements]
- [Compliance requirements]
- [Performance SLAs]

---

## 📊 Phasing Strategy

### Phase 1: Foundation (Weeks 1-4)
- Core infrastructure setup
- Basic authentication
- Database migrations
- **Deliverable:** Working foundation

### Phase 2: Core Features (Weeks 5-8)
- Primary user flows
- Essential integrations
- Initial performance optimization
- **Deliverable:** MVP release

### Phase 3: Enhancement (Weeks 9-12)
- Advanced features
- Full optimization
- Scale testing
- **Deliverable:** Full platform

---

## ✦ Success Criteria
- [Platform metric 1: availability >99.9%]
- [Performance metric: p99 latency <100ms]
- [Business metric: cost reduction >30%]
- [User metric: adoption >80%]
- [Quality metric: error rate <0.1%]

---

## ✔ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

### Foundation Phase
[] Infrastructure provisioned
[] CI/CD pipelines configured
[] Base services deployed
[] Monitoring established
[] Security baseline implemented

### Development Phase
[] All services implemented
[] Database migrations completed
[] Integration tests passing
[] Performance tests passing
[] Security audit completed

### Validation Phase
[] Load testing completed
[] Disaster recovery tested
[] Documentation comprehensive
[] Training materials created
[] Runbooks updated

### Launch Phase
[] Production deployment plan approved
[] Rollback procedures tested
[] Monitoring alerts configured
[] Support team trained
[] Communication plan executed

---

## ⋈ Dependencies
- [Infrastructure team: provisioning]
- [Security team: audit and approval]
- [Data team: migration support]
- [External vendor: API access]
- [Platform team: deployment windows]

---

## ∅ Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Data migration failure | Medium | High | Incremental migration with rollback points |
| Performance degradation | Low | High | Progressive rollout with monitoring |
| Integration delays | Medium | Medium | Early vendor engagement |
| Resource constraints | Medium | Medium | Phased approach with MVPs |

**Labels:** platform, strategic, [quarter], multi-sprint
```

---

## 🎯 TICKET FORMATTING RULES

### Required Elements
- ✅ Scope indicator: [BE], [FE], [Mobile], [FS], [DevOps], or [QA]
- ✅ Table of Contents (sections only, NO subsections)
- ✅ First heading: # ⌘ About
- ✅ Key Problems with ### → format (NOT in TOC)
- ✅ Reasons Why with ### → format (NOT in TOC)
- ✅ Designs & References section with ◳ symbol
- ✅ QA Warning above Resolution Checklist
- ✅ Dividers (---) between ALL sections
- ✅ Minimum 2 items in Key Problems
- ✅ Minimum 2 items in Reasons Why

### Symbol Usage
- **⌘** - Main sections and "About"
- **◇** - Requirements section
- **◊** - Sub-headings (always bold)
- **◳** - Designs & References
- **→** - Key Problems/Reasons (H3 only)
- **✦** - Success criteria (bullets)
- **✔** - Resolution checklist (checkboxes)
- **⋈** - Dependencies
- **∅** - Risks
- **—** - Sub-categories (under ◊ only)

## 💬 Interactive Questions

Interactive questions to ask during ticket creation.

**Reference:** Full interactive flows → `Product Owner - Interactive Mode.md`

```markdown
1. "What scope? [BE/FE/Mobile/FS/DevOps/QA]"
2. "Brief description of the issue/feature?"
3. [If complex] "Should we phase this delivery?"
4. [If platform] "What's the timeline flexibility?"
```

---

## 📦 Platform Integration

After ticket creation, offer platform integration options.

**Reference:** Full integration details → `Product Owner - Platform Integration.md`

```markdown
📦 **Add to your workspace?**

1. **ClickUp** - Task management, sprints
2. **Skip** - Keep as artifact only

Which option? (1 or 2)
```

**Pattern Tracking:** After 3+ similar choices, the system will recognize and suggest your preference.

---

*All tickets delivered as artifacts. Complexity auto-scales. Challenge Mode activates at 3+ thinking rounds.*