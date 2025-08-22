# Product Owner - Reference Guide - v1.1.0

Consolidated reference for all symbols, formats, templates, and quality standards with updated symbols.

## 📑 Table of Contents

1. [📤 SYMBOL DICTIONARY](#-symbol-dictionary)
2. [📋 TICKET TEMPLATES](#-ticket-templates)
3. [📚 DOCUMENTATION TEMPLATE](#-documentation-template)
4. [💻 SPEC TEMPLATE](#-spec-template)
5. [✏️ TEXT TEMPLATE](#-text-template)
6. [✅ QUALITY STANDARDS](#-quality-standards)
7. [📝 FORMATTING RULES](#-formatting-rules)
8. [🎯 COMPLEXITY DETECTION](#-complexity-detection)
9. [🚨 COMMON MISTAKES](#-common-mistakes)
10. [💡 COMPLETE EXAMPLES](#-complete-examples)
11. [🔧 TROUBLESHOOTING GUIDE](#-troubleshooting-guide)

---

## 📤 SYMBOL DICTIONARY

### Primary Symbols
| Symbol | Usage | Context | Notes |
|--------|-------|---------|-------|
| **⌘** | Section headers, "About" | All modes | Always first heading |
| **◇** | Requirements header | Tickets only | Major section |
| **◻️** | Feature sections | Documentation | Not in tickets |
| **◊** | Sub-headings | All modes | Always bold |
| **◳** | Designs & References | Tickets | New symbol |
| **→** | References, H3 headers | All modes | In "Key problems" & "Reasons why" |
| **✦** | Success criteria | Tickets | Bullets only |
| **✔** | Resolution checklist | Tickets | Checkboxes `[]` |
| **⋈** | Dependencies | Complex tickets | New symbol |
| **⚡** | Risks | Complex tickets | Optional |
| **📚** | Resources | Documentation | External links |
| **–** | Sub-categories | Under ◊ only | Em dash |

### Updated Symbols
- **◳** - Now used for Designs & References section (previously used ⌘)
- **⋈** - Now used for Dependencies section (previously used ⊗)

### Hierarchy Rules
```markdown
## 📑 Table of Contents
# ⌘ Top Level (About/Overview)
---
### → Key problems:
### → Reasons why:
---
## ◳ Designs & References
---
## ◇ Requirements (Tickets)
### ◻️ Feature Name (Docs)
**◊ Sub-heading**
– Sub-category
- Detail item
---
## ⋈ Dependencies
```

### Symbol Usage Guidelines

**When to Use Each Symbol:**
- **⌘** - Every first heading, major sections
- **◇** - Only for requirements section in tickets
- **◻️** - Each feature in documentation (never in tickets)
- **◊** - All sub-headings requiring emphasis
- **◳** - Designs & References section in tickets
- **→** - In H3 headers for Key problems/Reasons why
- **✦** - Success metrics that are measurable
- **✔** - Action items in resolution
- **⋈** - When external dependencies exist
- **⚡** - Risk factors in complex tickets
- **📚** - Help resources, training materials

---

## 📋 TICKET TEMPLATES

### Auto-Scaling Formula
`Complexity = Keywords + Scope + Impact + Timeline`

### Simple Ticket (2-3 sections, 4-6 resolution)
```markdown
[BE] Bug Fix: Login Error

## 📑 Table of Contents
- [⌘ About](#-about)
- [Key Problems & Reasons](#key-problems--reasons)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)

# ⌘ About

Users cannot log in due to token validation error blocking all access.

---

### → Key problems:
- Authentication tokens expiring prematurely causing login failures
- All users blocked from accessing the platform

### → Reasons why:
- Critical blocker preventing all user access to platform
- Revenue impact of $50K per hour of downtime

---

## ◳ Designs & References
- [System architecture diagram - to be added]
- [Error logs dashboard - link pending]
- [API documentation - to be added]

---

## ◇ Requirements

**◊ Core Fix**
– Token validation
- Identify expiration logic issue
- Update validation timeframe
- Add proper error handling
- Test with multiple user types

---

## ✦ Success Criteria
- Users can authenticate successfully
- Tokens persist for correct 24-hour duration
- Zero authentication errors in logs
- Response time under 200ms

---

## ✔ Resolution Checklist
[] Fix token validation logic
[] Add comprehensive test coverage
[] Update error handling
[] Deploy hotfix to production
[] Monitor for 24 hours
[] Document root cause

**Labels:** bug, critical, authentication, hotfix
**Thinking rounds used:** 2
```

### Standard Ticket (4-5 sections, 8-12 resolution)
```markdown
[FS] User Analytics Dashboard

## 📑 Table of Contents
- [⌘ About](#-about)
- [Key Problems & Reasons](#key-problems--reasons)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)
- [⋈ Dependencies](#-dependencies)

# ⌘ About

Comprehensive dashboard providing users with real-time insights into their account activity, usage patterns, and performance metrics.

---

### → Key problems:
- No visibility into usage patterns causing blind decision-making
- Manual data compilation taking 5+ hours weekly per team
- Missing competitive features leading to customer churn

### → Reasons why:
- Dashboard will reduce support tickets by 40% saving $200K annually
- Increase user engagement by 25% based on competitor analysis
- Provide critical insights for data-driven decisions improving retention by 15%

---

## ◳ Designs & References
- [Figma mockups - dashboard layouts](link)
- [Competitor analysis document](link)
- [User research findings - to be added]
- [API specification - pending]

---

## ◇ Requirements

**◊ Frontend Components**
– Dashboard Layout
- Responsive grid system with widgets
- Drag-and-drop customization
- Real-time data refresh indicators
- Mobile-optimized view
- Dark/light theme support

– Data Visualization
- Interactive charts (line, bar, pie)
- Heat maps for activity patterns
- Comparison tools for periods
- Export capabilities (PNG, CSV)

---

**◊ Backend Services**
– Data Aggregation
- RESTful API endpoints
- GraphQL for complex queries
- Redis caching layer
- WebSocket for real-time updates
- Rate limiting implementation

– Performance Optimization
- Query optimization (< 100ms)
- CDN integration for assets
- Lazy loading for charts
- Background job processing

---

**◊ Analytics Integration**
– Tracking Setup
- User interaction events
- Performance metrics
- Error tracking
- Custom event definitions
- Privacy-compliant collection

---

## ✦ Success Criteria
- Dashboard loads in under 2 seconds
- Real-time updates within 5 seconds
- 90% user satisfaction score
- Mobile responsive (320px minimum)
- 99.9% uptime
- Supports 10,000 concurrent users

---

## ✔ Resolution Checklist

### Foundation
[] Design system components
[] API contract definitions
[] Database schema design
[] Caching strategy

### Development
[] Build dashboard layout
[] Implement chart components
[] Create API endpoints
[] Set up WebSocket connections

### Quality & Deployment
[] Unit test coverage > 80%
[] E2E testing suite
[] Performance testing
[] Security audit
[] Deploy to staging
[] Production release

---

## ⋈ Dependencies
- Analytics service v3.0 upgrade
- Design system v2.0 components
- Data warehouse read access
- CDN configuration

**Labels:** feature, dashboard, full-stack, priority-high
**Thinking rounds used:** 4
```

### Complex Ticket Pattern (6-8 sections, 12-20 resolution)
```markdown
[FS] Multi-tenant Payment Platform

## 📑 Table of Contents
- [⌘ About](#-about)
- [Key Problems & Reasons](#key-problems--reasons)
- [◳ Designs & References](#-designs--references)
- [◇ Implementation Strategy](#-implementation-strategy)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)
- [⋈ Major Dependencies](#-major-dependencies)
- [⚡ Risks](#-risks)

# ⌘ About

Enterprise-grade payment processing system supporting multiple payment providers, currencies, and compliance requirements across global markets.

---

### → Key problems:
- Limited to credit cards only - losing 30% of international customers
- Manual reconciliation consuming 20 hours weekly per team
- Non-compliant with new EU regulations (deadline: Q2)
- $500K monthly revenue loss from failed transactions

### → Reasons why:
- Strategic initiative enabling global expansion into 15 new markets
- Automated operations saving $1M annually in manual processing
- Regulatory compliance avoiding $5M potential fines
- Projected $2M additional revenue in Q1 from reduced payment failures

---

## ◳ Designs & References
- [System architecture diagram](link)
- [Payment flow diagrams - Figma](link)
- [Compliance requirements matrix](link)
- [API documentation - Stripe/PayPal](link)
- [Security audit report - to be added]
- [Performance benchmarks - pending]

---

## ◇ Implementation Strategy

### Phase 1: Foundation (Week 1-3)

**◊ Payment Provider Integration**
– Core Providers
- Stripe integration (cards, wallets)
- PayPal/Venmo implementation
- Bank transfer infrastructure (ACH, SEPA)
- Cryptocurrency gateway (Bitcoin, Ethereum)
- Regional providers (Alipay, WeChat Pay)

– Infrastructure Setup
- Multi-region deployment
- Load balancing configuration
- Database sharding strategy
- Message queue implementation
- Monitoring and alerting

---

**◊ Security & Compliance**
– PCI DSS Level 1
- Tokenization implementation
- End-to-end encryption
- Key management service
- Secure vault integration
- Audit logging system

– Regulatory Compliance
- GDPR data handling
- PSD2 strong authentication
- SOC 2 Type II preparation
- Regional compliance mapping

---

### Phase 2: Processing Engine (Week 4-6)

**◊ Transaction Management**
– Core Processing
- Multi-currency support (150+ currencies)
- Real-time FX rates
- Smart routing logic
- Retry mechanisms
- Fallback providers

– Advanced Features
- Split payments
- Delayed capture
- Partial refunds
- Chargeback handling
- Dispute management

---

**◊ Reconciliation System**
– Automated Matching
- Daily settlement processing
- Three-way matching logic
- Discrepancy detection
- Exception handling workflow
- Financial reporting

– Integration Points
- ERP system sync
- Accounting software APIs
- Bank statement imports
- Custom report builder

---

### Phase 3: Advanced Features (Week 7-9)

**◊ Subscription Billing**
– Recurring Payments
- Flexible billing cycles
- Trial period management
- Proration calculations
- Payment retry schedules
- Dunning management

– Customer Portal
- Self-service management
- Payment method updates
- Invoice history
- Subscription modifications

---

**◊ Fraud Prevention**
– Risk Management
- ML-based fraud scoring
- Rule engine configuration
- Velocity checking
- Blacklist management
- Manual review queue

– Monitoring & Analytics
- Real-time dashboards
- Fraud pattern detection
- Performance metrics
- Custom alerts
- Predictive analytics

---

## ✦ Success Criteria
- Support 15+ payment methods
- 99.95% transaction success rate
- PCI DSS Level 1 certified
- < 200ms transaction processing
- Zero security vulnerabilities
- $0 reconciliation discrepancies
- 50% reduction in fraud losses
- 24/7 system availability

---

## ✔ Resolution Checklist

### Phase 1: Foundation
[] Set up payment provider accounts
[] Implement provider SDKs
[] Build tokenization system
[] Deploy infrastructure
[] Complete security audit
[] Achieve PCI compliance

### Phase 2: Core Engine
[] Build transaction processor
[] Implement retry logic
[] Create reconciliation system
[] Develop admin dashboard
[] Set up monitoring
[] Complete integration testing

### Phase 3: Advanced
[] Launch subscription billing
[] Deploy fraud prevention
[] Enable customer portal
[] Implement analytics
[] Complete load testing
[] Full security review

### Go-Live
[] Staged rollout plan
[] Migration strategy
[] Team training
[] Documentation complete
[] Support runbooks
[] Post-launch monitoring

---

## ⋈ Major Dependencies
- Payment provider approvals
- Security audit completion
- Legal compliance review
- Infrastructure provisioning
- Third-party integrations
- Finance team training

---

## ⚡ Risks
- **Technical:** Legacy system migration complexity
- **Regulatory:** Changing compliance requirements
- **Operational:** Payment provider API limits
- **Financial:** Currency fluctuation impact
- **Timeline:** Third-party approval delays
- **Security:** Increased attack surface

**Labels:** initiative, payments, complex, strategic, compliance, multi-phase
**Thinking rounds used:** 8
```

---

## 📚 DOCUMENTATION TEMPLATE

### Standard Structure
```markdown
MODE: $doc
TYPE: Feature Documentation
THINKING ROUNDS: [X]
AUDIENCE: [User/Developer/Both]

---

# ⌘ Overview

[Feature description - 2-3 sentences]

**Target Audience:** [End users/Developers/Both]
**Complexity:** [Basic/Intermediate/Advanced]
**Version:** [Semantic version]
**Last Updated:** [Date]

---

## ⌘ Features

### ◻️ [Feature Name]

[Feature introduction paragraph]

**◊ Getting Started**
– Prerequisites
- Requirement 1
- Requirement 2

– Initial Setup
- Step 1
- Step 2

---

**◊ Core Functionality**
– Category
- Feature detail
- Feature detail

---

**◊ Advanced Options**
– Category
- Option 1
- Option 2

### ◻️ [Feature Name 2]

[Continue pattern...]

---

## → Development References

**◊ Technical Documentation**
- [API Reference](link)
- [Integration Guide](link)

**◊ Design Resources**
- [Figma Designs](link)
- [Component Library](link)

---

## 📚 Additional Resources

- [Video Tutorials](link)
- [FAQ](link)
- [Support Contact](link)
```

### Quick Start Template
```markdown
# ⌘ Quick Start Guide

Get up and running in 5 minutes.

**Thinking rounds used:** 2

## ◻️ Initial Setup
**◊ Prerequisites**
– Requirements
- Item 1
- Item 2

## ◻️ First Task
**◊ Basic Steps**
– Process
- Step 1
- Step 2

## ◻️ Next Steps
**◊ Where to Go**
– Resources
- Advanced guide
- API docs
```

---

## 💻 SPEC TEMPLATE

### Standard Implementation
```markdown
# [Component] Implementation

## Objective
[1-2 sentences describing what this solves]

## Quick Setup
Framework: [React/Vue/Vanilla]
Features: [List of features]
Thinking rounds used: [X]
Dependencies: [If any]

## Implementation
```javascript
// Complete, working code
// No TODO comments or placeholders
import React, { useState } from 'react';

const Component = () => {
  // Full implementation
  return (
    // JSX
  );
};

export default Component;
```

## Key Points
- Performance consideration
- Browser compatibility note
- Usage tip
- Edge case handling

## Browser Compatibility
- Modern browsers: ✔
- IE11: [Requires polyfills/Not supported]
- Mobile: [Responsive/Touch-enabled]

## Usage Example
```javascript
// How to use the component
<Component prop="value" />
```
```

### CSS Utility Template
```markdown
# [Utility Name]

## Objective
[What problem this solves]

## Quick Setup
Browser support: [All/Modern]
Thinking rounds used: [1-2]

## Implementation
```css
/* Pure CSS solution */
.class-name {
  /* Properties */
}

/* Browser-specific fixes */
.class-name::-webkit-scrollbar {
  /* Webkit browsers */
}
```

## Key Points
- Browser support note
- Performance impact
- Alternative approaches
```

---

## ✏️ TEXT TEMPLATE

```markdown
# Text Snippets

## Component Description
"A secure modal with OAuth integration..."

## Error Messages
"Payment failed. Please check details."

## Marketing Copy
"Transform your workflow with..."

Thinking rounds used: 1
```

---

## ✅ QUALITY STANDARDS

### All Outputs Must Have
1. Appropriate title with scope/feature
2. First heading with ⌘ symbol
3. Thinking rounds noted
4. Proper symbol usage
5. Clear structure

### Tickets Specifically Must Have
- **Table of Contents** - ALL tickets, regardless of size
- **User value** - ### → Reasons why: (minimum 2 items)
- **Problem statement** - ### → Key problems: (minimum 2 items)
- **Designs & References** - Section with ◳ symbol and placeholders if no links
- **Success criteria** - ✦ bullets
- **Resolution checklist** - ✔ checkboxes
- **Dividers** - Between ALL sections (---)
- **Bullet format** - Using "- text" not bullet symbols
- **Auto-scaled complexity** - System determined
- **User-specified labels** - Ask user for tags
- **Dependencies** - ⋈ section when needed

### Documentation Specifically
- Defined audience
- Version information
- ◻️ for features
- → for references
- 📚 for resources

### Specs Specifically
- Working code only
- No "TODO" comments
- Browser notes if relevant
- Performance considerations

---

## 📝 FORMATTING RULES

### Mandatory for Tickets
- **Table of Contents**: Required for ALL tickets
- **No space in checkboxes**: `[]` not `[ ]`
- **Bold ◊ sub-headings**: `**◊ Name**`
- **Em dash only under ◊**: `– Category`
- **Dividers between sections**: `---` between ALL sections
- **Key Problems format**: `### → Key problems:` with 2+ items
- **Reasons Why format**: `### → Reasons why:` with 2+ items
- **Bullet format**: `- text` not bullet symbols
- **Designs section**: Always include with ◳ symbol
- **Dependencies section**: Include with ⋈ when needed
- **Platform offer in chat**: Never in artifact

### Style Guide
- Concise descriptions
- Outcome-focused resolution
- Value-driven requirements
- Clear success metrics
- Professional tone
- Minimum 2 items for problems/reasons

---

## 🎯 COMPLEXITY DETECTION

### Keywords → Complexity

| Simple | Standard | Complex |
|--------|----------|---------|
| fix | feature | platform |
| bug | dashboard | architecture |
| update | workflow | migration |
| change | integration | enterprise |
| modify | process | compliance |
| adjust | system | multi-tenant |

### Scaling Rules
- Simple: 1-2 ◊ sections, 2-3 ✔ per section
- Standard: 2-3 ◊ sections, 3-4 ✔ per section
- Complex: 4-6 ◊ sections, 3-4 ✔ per section

### All Complexities Get
- Table of Contents
- Dividers between sections
- Key Problems (### → format, 2+ items)
- Reasons Why (### → format, 2+ items)
- Designs & References section (◳)
- Dependencies section when needed (⋈)

---

## 🚨 COMMON MISTAKES

### Never Do
❌ Skip Table of Contents for any ticket
❌ Mix ✦ and ✔ symbols
❌ Skip ⌘ in first heading
❌ Less than 2 items for problems/reasons
❌ Forget dividers between sections
❌ Skip Designs & References section
❌ Use wrong symbol for Designs (use ◳ not ⌘)
❌ Use wrong symbol for Dependencies (use ⋈ not ⊗)
❌ Use wrong format for Key Problems (use ### →)
❌ Use wrong format for Reasons Why (use ### →)
❌ Manual complexity selection
❌ Platform offer in artifact
❌ Assume scope or labels
❌ Use bullet symbols instead of "-"

### Always Do
✅ Include Table of Contents for ALL tickets
✅ Auto-detect complexity
✅ Ask for thinking rounds
✅ Use interactive guidance
✅ Apply proper symbols (◳ for Designs, ⋈ for Dependencies)
✅ Include dividers between ALL sections
✅ Format Key Problems with ### → and 2+ items
✅ Format Reasons Why with ### → and 2+ items
✅ Include Designs & References with ◳ symbol
✅ Include Dependencies with ⋈ when needed
✅ Note thinking rounds used
✅ Use "- text" for bullets

---

## 🔧 TROUBLESHOOTING GUIDE

### Formatting Issues

**Problem:** No Table of Contents
**Solution:** Add TOC to ALL tickets, even simple ones

**Problem:** Missing dividers
**Solution:** Add `---` between ALL sections

**Problem:** Wrong Key Problems format
**Solution:** Use `### → Key problems:` with 2+ items using "-"

**Problem:** Wrong Reasons Why format
**Solution:** Use `### → Reasons why:` with 2+ items using "-"

**Problem:** Less than 2 items in problems/reasons
**Solution:** Always include minimum 2 items for each

**Problem:** No Designs section
**Solution:** Always include with ◳ symbol: `## ◳ Designs & References`

**Problem:** Wrong Dependencies symbol
**Solution:** Use ⋈ not ⊗: `## ⋈ Dependencies`

**Problem:** Wrong bullet format
**Solution:** Use "- text" not bullet symbols

### Symbol Issues

**Problem:** Using old symbols
**Solution:** Update to new symbols (◳ for Designs, ⋈ for Dependencies)

**Problem:** Missing symbols in sections
**Solution:** Every major section needs its symbol

### Complexity Issues

**Problem:** Manually selecting complexity
**Solution:** Let system auto-detect based on keywords

**Problem:** Wrong section count
**Solution:** Simple (2-3), Standard (4-5), Complex (6-8)

### Quality Issues

**Problem:** Missing required elements
**Solution:** Use quality checklist to verify all elements

**Problem:** Inconsistent formatting
**Solution:** Follow templates exactly with new symbols

---

*Single source of truth for all formats, symbols, and standards. Every ticket needs TOC, dividers, and properly formatted Key Problems/Reasons with minimum 2 items each. Uses ◳ for Designs & References, ⋈ for Dependencies.*