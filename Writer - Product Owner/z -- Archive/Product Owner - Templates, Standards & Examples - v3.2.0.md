# Product Owner - Templates, Standards & Examples - v3.2.0

Complete templates, standards, and examples for the Product Owner system with native thinking. Reference this for all formatting, symbols, and structure patterns.

## Table of Contents

1. [📤 SYMBOL REFERENCE](#1--symbol-reference)
2. [📋 UNIFIED TICKET TEMPLATES](#2--unified-ticket-templates)
3. [📚 DOCUMENTATION TEMPLATES](#3--documentation-templates)
4. [💻 SPEC TEMPLATES](#4--spec-templates)
5. [🎯 MODE EXAMPLES](#5--mode-examples)
6. [📊 ARTIFACT STRUCTURE](#6--artifact-structure)
7. [✅ QUALITY STANDARDS](#7--quality-standards)
8. [🔧 FORMATTING RULES](#8--formatting-rules)
9. [💡 REAL EXAMPLES](#9--real-examples)
10. [🚨 COMMON MISTAKES](#10--common-mistakes)

---

## 1. 📤 SYMBOL REFERENCE

### Primary Symbols

| Symbol | Name | Usage | Context |
|--------|------|-------|---------|
| **⌘** | Command | Section headers, "About" | All modes |
| **◇** | Diamond | Requirements header | Tickets |
| **◻️** | Square | Feature sections | Documentation |
| **◊** | Small Diamond | Sub-headings (bold) | All modes |
| **→** | Arrow | References, links | All modes |
| **✦** | Star | Success criteria | Tickets (bullets) |
| **✓** | Check | Resolution checklist | Tickets (checkboxes) |
| **⊗** | Cross | Dependencies | Tickets |
| **⚡** | Lightning | Risks | Tickets |
| **⚠️** | Warning | Key problems | All modes |
| **⌥** | Option | Reasons why | Tickets |
| **📚** | Books | Resources | Documentation |
| **—** | Em dash | Sub-categories | Under ◊ only |
| **•** | Bullet | Detail items | All modes |

### Hierarchy Rules

```markdown
# ⌘ Top Level
## ⌘ Major Section
### ◻️ or ◇ Feature/Requirement
**◊** Sub-heading
— Sub-category
• Detail point
```

---

## 2. 📋 UNIFIED TICKET TEMPLATES

### Simple Ticket (Auto-detected for bugs/small features)

```markdown
[BE] Bug Fix: Authentication Error

# ⌘ About

Users cannot log in due to token validation error.

⚠️ **Key problem:**
Authentication tokens are expiring prematurely, blocking user access.

⌥ **Reason why:**
Fixing this restores service availability and prevents user churn.

## ◇ Requirements

**◊ Core Fix**
— Token Validation
• Identify expiration logic issue
• Update validation timeframe
• Add proper error handling

## ✦ Success Criteria
- Users can authenticate successfully
- Tokens persist for correct duration
- Zero authentication errors in logs

## ✓ Resolution Checklist
[] Fix token validation logic
[] Add comprehensive tests
[] Deploy hotfix to production

**Labels:** bug, authentication, critical
**Thinking rounds used:** 2
```

### Standard Ticket (Auto-detected for full features)

```markdown
[FS] User Dashboard

# ⌘ About

Comprehensive dashboard for users to monitor their account activity and metrics.

⚠️ **Key problems:**
* **No visibility** - Users lack insight into their usage
* **Manual tracking** - Users resort to spreadsheets

⌥ **Reasons why:**
This dashboard empowers users with real-time insights, reducing support tickets by 40% and improving retention.

## ◇ Requirements

**◊ Frontend Components**
— Dashboard Layout
• Overview cards with key metrics
• Interactive charts for trends
• Filter controls for date ranges

---

**◊ Backend Services**
— Data Aggregation
• API endpoints for metrics
• Caching strategy for performance
• Real-time data streaming

---

**◊ Analytics Integration**
— Tracking Setup
• User interaction events
• Performance metrics
• Export functionality

## ✦ Success Criteria
- Dashboard loads in under 2 seconds
- All metrics update in real-time
- 90% user satisfaction score
- Mobile responsive design

## ✓ Resolution Checklist

### Foundation
[] Design API contracts
[] Set up data models
[] Create component architecture

### Development
[] Build dashboard components
[] Implement backend services
[] Integrate analytics

### Deployment
[] Complete testing suite
[] Deploy to staging
[] Release to production

## ⊗ Dependencies
- Analytics service v3.0
- Design system components
- Data warehouse access

**Labels:** feature, dashboard, full-stack
**Thinking rounds used:** 4
```

### Complex Ticket (Auto-detected for major initiatives)

```markdown
[FS] Payment Platform Integration

# ⌘ About

Enterprise payment processing system supporting multiple providers and currencies.

⚠️ **Key problems:**
* **Limited payment options** - Losing 30% of international customers
* **Manual reconciliation** - Finance team spending 20 hours weekly
* **Compliance gaps** - Not meeting new regulatory requirements

⌥ **Reasons why:**
This integration opens new markets, automates financial operations, and ensures compliance, projecting $2M additional revenue in Q1.

## ◇ Implementation Strategy

### Phase 1: Foundation (Week 1-2)

**◊ Payment Provider Integration**
— Core Setup
• Stripe integration for cards
• PayPal for digital wallets
• Bank transfer infrastructure
• Webhook handling system

---

**◊ Security & Compliance**
— PCI Compliance
• Tokenization implementation
• Encryption at rest/transit
• Audit logging system
• GDPR compliance layer

### Phase 2: Processing Engine (Week 3-4)

**◊ Transaction Management**
— Processing Pipeline
• Multi-currency support
• Retry logic for failures
• Refund automation
• Chargeback handling

---

**◊ Reconciliation System**
— Automated Matching
• Daily settlement reports
• Discrepancy detection
• Finance team dashboard
• Export capabilities

### Phase 3: Advanced Features (Week 5-6)

**◊ Subscription Billing**
— Recurring Payments
• Subscription lifecycle
• Proration logic
• Payment retry schedules
• Dunning management

---

**◊ Fraud Prevention**
— Risk Management
• ML-based fraud detection
• Velocity checking
• Blacklist management
• Manual review queue

## ✦ Success Criteria
- Support 10+ payment methods
- 99.95% transaction success rate
- PCI DSS Level 1 compliance
- <200ms transaction processing
- Zero security vulnerabilities
- $0 reconciliation discrepancies

## ✓ Resolution Checklist

### Phase 1: Foundation
[] Integrate payment providers
[] Implement security measures
[] Achieve PCI compliance
[] Set up monitoring

### Phase 2: Engine
[] Build processing pipeline
[] Create reconciliation system
[] Deploy to staging
[] Complete security audit

### Phase 3: Enhancement
[] Launch subscription billing
[] Activate fraud prevention
[] Complete load testing
[] Production deployment

### Post-Launch
[] Monitor performance metrics
[] Gather user feedback
[] Optimize based on data
[] Plan next iterations

## ⊗ Major Dependencies
- Payment provider accounts
- Security audit completion
- Finance team training
- Legal compliance review

## ⚡ Risks
- **Technical:** Legacy system migration complexity
- **Regulatory:** Changing compliance requirements
- **Operational:** Payment provider API limits
- **Financial:** Currency fluctuation impact

**Labels:** initiative, payments, complex, strategic
**Thinking rounds used:** 8
```

---

## 3. 📚 DOCUMENTATION TEMPLATES

### Interactive Documentation Template

```markdown
Analytics Dashboard Documentation

MODE: $doc
TYPE: Feature Documentation
THINKING ROUNDS: 3
AUDIENCE: End Users

---

# ⌘ Overview

The Analytics Dashboard provides real-time insights into your application's performance and user behavior.

**Target Audience:** Product managers and analysts
**Complexity:** Intermediate
**Version:** 2.1.0
**Last Updated:** January 2025

---

## ⌘ Features

### ◻️ Dashboard Overview

Your command center for data-driven decisions.

**◊ Getting Started**
— Prerequisites
• Active account with analytics permissions
• Data collection enabled (7+ days)
• Modern browser (Chrome, Firefox, Safari)

— First Steps
• Navigate to Analytics from main menu
• Select your date range (top right)
• Choose primary metric view

---

**◊ Key Metrics**
— Available Data
• User engagement (DAU, MAU, retention)
• Performance metrics (load time, errors)
• Business KPIs (conversion, revenue)
• Custom metrics (user-defined)

---

### ◻️ Custom Reports

Build reports tailored to your needs.

**◊ Report Builder**
— Creating Reports
• Select metrics to track
• Apply filters and segments
• Choose visualization type
• Set refresh frequency

— Sharing Options
• Export to PDF/CSV
• Schedule email delivery
• Embed in presentations
• Share via secure link

---

## → Related Materials

**◊ Visual Guides**
— Resources
• [Video Walkthrough](link)
• [Interactive Demo](link)
• [Screenshot Gallery](link)

---

## ⚠️ Important Notes

- Data refreshes every 15 minutes
- Historical data: 365 days retention
- Export limit: 100,000 rows
- Custom metrics require admin approval

---

## 📚 Additional Resources

- [Best Practices Guide](link)
- [API Documentation](link)
- [Training Videos](link)
- [Support Forum](link)

**Thinking rounds used:** 3
```

---

## 4. 💻 SPEC TEMPLATES

### Interactive Spec Template

```markdown
# Virtual Scrolling Implementation

## Objective
Efficiently render 10,000+ list items with smooth scrolling.

## Quick Setup
Framework: React
Data size: 10,000 items
Features: Selection, sorting
Thinking rounds used: 3

## Implementation
```typescript
import { FixedSizeList } from 'react-window';
import { useState, useCallback, memo } from 'react';

const VirtualList = ({ data }) => {
  const [selected, setSelected] = useState(new Set());
  
  const Row = memo(({ index, style }) => {
    const item = data[index];
    const isSelected = selected.has(item.id);
    
    return (
      <div 
        style={style}
        className={`row ${isSelected ? 'selected' : ''}`}
        onClick={() => {
          setSelected(prev => {
            const next = new Set(prev);
            isSelected ? next.delete(item.id) : next.add(item.id);
            return next;
          });
        }}
      >
        <span>{item.name}</span>
        <span>{item.value}</span>
      </div>
    );
  });
  
  return (
    <FixedSizeList
      height={600}
      itemCount={data.length}
      itemSize={40}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
};
```

## Performance Notes
- Only renders visible rows
- React.memo prevents re-renders
- Selection state outside list
- Add `overscanCount` for smoother scrolling

## Browser Support
- All modern browsers ✓
- IE11 requires polyfills
```

---

## 5. 🎯 MODE EXAMPLES

### Discovery Mode (Default)

```markdown
User: need user authentication

System: Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. **Development ticket** - Feature or bug for developers
2. **Implementation spec** - Frontend code/styling solution
3. **Product documentation** - User guide or feature docs

Which best fits? (1, 2, or 3)

User: 1

System: Great! Let's create your ticket. 🎯

How many thinking rounds should I use? (1-10)
• Simple bug/feature: 1-2 rounds
• Standard feature: 3-5 rounds
• Complex initiative: 6-10 rounds

Suggested for authentication: 3-5 rounds

User: 4

[Continues with ticket questions...]
```

### $ticket Mode

```markdown
User: $ticket payment integration

System: Let's create your payment integration ticket! 🎯

How many thinking rounds should I use? (1-10)
• Simple bug/feature: 1-2 rounds
• Standard feature: 3-5 rounds
• Complex initiative: 6-10 rounds

Suggested for payment integration: 6-8 rounds

User: 7

System: I'll guide you through building a clear, actionable ticket.

First, tell me:
- What payment methods do you need?
- Is this a new system or updating existing?
- Any compliance requirements?

[System auto-detects this is complex based on responses]
```

### $spec Mode

```markdown
User: $spec infinite scroll

System: Let's build your infinite scroll implementation! 🔧

How many thinking rounds should I use? (1-10)
Suggested: 2-3 for component features

User: 3

System: Quick setup:
1. React, Vue, or Vanilla JS?
2. Approximate data size?
3. Need virtual scrolling?

User: React, 50k items, yes

[Generates optimized implementation]
```

### $doc Mode

```markdown
User: $doc analytics dashboard

System: Let's document the analytics dashboard! 📚

How many thinking rounds should I use? (1-10)
Suggested: 2-3 for documentation

User: 3

System: I'll help create clear user documentation:
1. Who will read this? (end users/internal/both)
2. How many main features to cover?
3. Documentation depth needed?

User: End users, 4 features, detailed

[Creates structured documentation]
```

---

## 6. 📊 ARTIFACT STRUCTURE

### Unified Ticket Structure
```
[SCOPE] Feature Name (artifact title)
# ⌘ About (first heading)
Description with ⚠️ and ⌥
## ◇ Requirements
## ✦ Success Criteria
## ✓ Resolution Checklist
## ⊗ Dependencies (if needed)
Labels: (at bottom)
Thinking rounds used: X
```

### Documentation Structure
```
Product Documentation (artifact title)
# ⌘ Overview (first heading)
Metadata block
## ⌘ Features
### ◻️ Feature sections
## → References
## ⚠️ Important Notes
## 📚 Resources
Thinking rounds used: X
```

### Spec Structure
```
Implementation Name (artifact title)
## Objective
## Quick Setup (including thinking rounds)
## Implementation
## Key Points
## Browser Support (if relevant)
```

---

## 7. ✅ QUALITY STANDARDS

### Ticket Quality
- Clear problem statement (⚠️)
- Value articulation (⌥)
- Measurable success criteria (✦)
- Actionable resolution items (✓)
- Proper complexity scaling
- User-specified scope and labels
- Thinking rounds noted

### Documentation Quality
- Defined audience
- Logical feature flow
- Interactive guidance
- Helpful resources
- Version information
- Clear limitations
- Thinking rounds noted

### Spec Quality
- Working code examples
- No placeholders
- Browser compatibility notes
- Performance considerations
- Interactive setup
- Thinking rounds noted

---

## 8. 🔧 FORMATTING RULES

### Mandatory Rules
1. First heading always ⌘ About/Overview
2. Symbols required for all sections
3. ✦ for success (bullets only)
4. ✓ for resolution (checkboxes only)
5. Bold **◊** sub-headings
6. Em dash — only under ◊
7. Dividers between ◊ subsections
8. Platform offer in chat, not artifact
9. ⌥ for "Reasons why"
10. Note thinking rounds used

### Style Rules
- Concise and clear
- No space in checkbox brackets []
- Max 3 items per resolution section
- Outcomes not tasks in resolution
- Interactive for all modes
- Thinking rounds always asked

---

## 9. 💡 REAL EXAMPLES

### Auto-Scaling Example

**User Input:** `$ticket fix slow database queries`

**System:** 
1. Asks for 1-2 thinking rounds
2. Detects: Simple bug fix
3. Output: 2-3 section ticket with 4-6 resolution items

---

**User Input:** `$ticket multi-tenant architecture`

**System:**
1. Asks for 6-10 thinking rounds
2. Detects: Complex initiative
3. Output: 6-8 section ticket with phased approach, 12-20 resolution items

---

## 10. 🚨 COMMON MISTAKES

### Avoid These
❌ Choosing complexity manually
❌ Missing ⌘ in first heading
❌ Using wrong symbol for reasons
❌ Mixing ✦ and ✓ symbols
❌ Space in checkboxes [ ]
❌ Platform offer in artifact
❌ Skipping interactive guidance
❌ Assuming scope or labels
❌ Not asking for thinking rounds

### Do These Instead
✅ Let system auto-detect complexity
✅ # ⌘ About always first
✅ Use ⌥ for "Reasons why"
✅ ✦ bullets, ✓ checkboxes
✅ [] no space in brackets
✅ Platform offer in chat
✅ Always guide interactively
✅ Ask for scope and labels
✅ Always ask thinking rounds (except discovery)

---

*Unified ticket mode with auto-scaling. Native thinking with user control. All modes interactive. Use these templates for consistent output.*