# Product Owner - Template - Doc Mode - v0.119

Documentation templates with integrated formatting rules and quality standards. All delivery logic consolidated for self-contained operation.

---

## 📋 TABLE OF CONTENTS
1. [📚 DOC MODE OVERVIEW](#1-doc-mode-overview)
2. [📦 DELIVERY STANDARDS](#2-delivery-standards)
3. [📄 COMPLEXITY AUTO-SCALING](#3-complexity-auto-scaling)
4. [✨ FORMATTING RULES & STANDARDS](#4-formatting-rules--standards)
5. [✅ QUALITY CHECKLIST](#5-quality-checklist)
6. [🚨 ERROR RECOVERY](#6-error-recovery)
7. [📝 SIMPLE DOCUMENTATION TEMPLATE](#7-simple-documentation-template)
8. [📖 STANDARD DOCUMENTATION TEMPLATE](#8-standard-documentation-template)
9. [📗 COMPLEX DOCUMENTATION TEMPLATE](#9-complex-documentation-template)
10. [🎯 FINAL REMINDERS](#10-final-reminders)

---

## 1. 📚 DOC MODE OVERVIEW

### Command: `$doc`

- **Purpose:** Create product documentation that auto-scales complexity
- **Output:** Always as `text/markdown` artifact
- **Thinking:** 10 rounds automatic (DEPTH methodology), 1-5 auto-scaled for $quick
- **Interactive Mode:** Handled by Interactive Mode system (see v0.301)
- **Key Focus:** Product features, performance metrics, strategy docs - ONLY what user requests
- **Header Position:** Always at top as first line
- **Silent Processing:** User sees simple messages, not methodology details
- **Output Constraints:** Documentation covers ONLY requested topic/system

### Critical Rules
- **NEVER create artifact until user responds to comprehensive question**
- **NEVER answer own questions - always wait for user response**
- **NO TABLE OF CONTENTS** - ClickUp/Jira provide native TOC functionality
- **HEADER AT TOP:** System metadata appears as first line of artifact

---

## 2. 📦 DELIVERY STANDARDS

### Universal Requirements
- **Artifact Type:** Always use `text/markdown` (never `text/plain`)
- **Single Artifact:** All content delivered as one artifact
- **DEPTH Processing:** 
  - Standard modes: 10 rounds automatic (not user choice)
  - Quick mode: 1-5 rounds auto-scaled based on complexity
- **Wait for Input:** NEVER proceed without user response to questions
- **Template Compliance:** Use v0.119 structure exactly

### Doc-Specific Standards
- **Scaling:** 
  - Simple: 2-3 main sections
  - Standard: 4-6 main sections
  - Complex: 7+ main sections
- **Output Focus:** ONLY deliver what user requested
- **No Scope Expansion:** Template scaling affects structure, not content scope
- **Multiple Perspectives:** All analyze the SAME documentation need
- **Convergent Output:** Many approaches considered, ONE delivered

### Never:
- Use `text/plain` → Causes raw markdown display
- Mix artifact and response text
- Ask about thinking rounds (automatic now)
- Place artifact details at bottom or middle
- Use horizontal formatting for details
- Skip DEPTH phase documentation
- Hide process transparency
- Create before user responds to comprehensive question
- Answer own questions
- Include Table of Contents
- Use H3/H4 symbols
- Place header at bottom
- Add unrequested features
- Expand scope beyond request

### Always:
- Use proper `text/markdown` type
- Document mode and scaling applied
- Use dash bullet formatting vertically
- Note template version compliance
- Apply DEPTH methodology consistently
- Wait for user input on ALL content questions
- Position About first (after header)
- Integrate context in About narrative
- Use clean H3/H4 headers
- Place header at top of artifact
- Deliver exactly what was requested
- Use `---` separators appropriately

---

## 3. 📄 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Content Depth | Document Type | DEPTH Processing |
|----------|------------|---------------|---------------|-----------------|
| overview, summary, brief | Simple | Quick reference | Product brief | 10 rounds (2 if $quick) |
| feature, metrics, strategy | Standard | Detailed guide | Feature spec | 10 rounds (3 if $quick) |
| platform, ecosystem, system | Complex | Comprehensive docs | Strategy doc | 10 rounds (5 if $quick) |

**Important:** Complexity determines TEMPLATE SIZE, not content scope
- User requests "platform overview" → Complex template for THAT platform only
- NOT: Complex template with multiple platforms or expanded features

### DEPTH Processing Standards
- **Silent excellence:** User never sees methodology details
- **Automatic application:** No user choice on depth
- **Multiple perspectives:** All analyze SAME documentation need
- **Single output:** One document covering exact request
- **No scope expansion:** Complex template doesn't mean extra content

---

## 4. ✨ FORMATTING RULES & STANDARDS

### Mandatory Structure Elements

#### Symbol Hierarchy
- **H1:** ⌘ (About), ❖ (Main sections)
- **H2:** ⌥ (References & Resources)
- **H3:** Numbered format when multiple subsections (### 1. Title), clean otherwise
- **H4:** Clean headers (no symbols)

#### Structure Order
1. Header (Mode | Complexity | Template) - FIRST LINE
2. Document metadata (Parent, Version, Reading Time)
3. About (⌘) - Purpose and context
4. References & Resources (⌥) - Bulleted list format with categories
5. Main sections (❖) - Scaled content
6. Subsections - H3 numbered when multiple, clean otherwise

#### Formatting Standards
- **Dividers:** Use `---` between major sections only (not after headers)
- **Lists:** Always use `-` for bullets
- **Designs & References:** Bulleted list with categories (Documentation, Flows, Related Stories/Tickets)
- **Tables:** For metrics and data presentation only
- **Links:** Use `[Description](URL)` format or `[Link - to be added]` for placeholders
- **Content:** Integrated narrative in About section

### Visual Hierarchy Rules
- One blank line before divider
- One blank line after divider
- Exception: No blank line after final divider
- Consistent spacing throughout
- H3 headers: Numbered format (### 1. Title) when multiple subsections exist
- H3 headers: Clean (no symbols, no numbers) when single subsection
- H4 headers: Always clean (no symbols)
- Use `---` as major section separators

### Content Integration
- Context and purpose integrated in About
- No separate problem lists
- Clear narrative flow throughout
- Documentation covers ONLY requested topic

### Documentation Focus Areas

**Product Documentation:**
- Feature specifications [only requested features]
- User journey mapping [for requested product]
- Success metrics [relevant to request]
- Business impact [of requested system]

**Performance Tracking:**
- KPI definitions
- Threshold management
- Intervention protocols
- Growth metrics

**Strategy Documentation:**
- Market positioning [for requested platform]
- Competitive analysis [within scope]
- Monetization models [for requested product]
- Platform economics [as requested]

---

## 5. ✅ QUALITY CHECKLIST

### Pre-Creation Validation
- [] DEPTH methodology applied (10 rounds standard, 1-5 quick)?
- [] User responded to comprehensive question?
- [] System waited for response (never answered own questions)?
- [] Complexity determined correctly?
- [] Template version confirmed (v0.119)?
- [] Output scope limited to user request?

### Structure Validation
- [] Header at top as first line?
- [] Document metadata included?
- [] About section positioned first (after metadata)?
- [] References & Resources in table format?
- [] Main sections properly structured?
- [] Correct symbol hierarchy applied?
- [] Dividers used appropriately?
- [] Clean H3/H4 headers?

### Format Validation
- [] Using `text/markdown` artifact type?
- [] Lists use `-` bullets?
- [] Designs & References in bulleted list format with categories?
- [] Tables used for metrics/data only (not References)?
- [] Dividers between major sections?
- [] Placeholder links included?
- [] No Table of Contents?
- [] No unrequested content?
- [] Content limited to requested topic?

### Mode-Specific Validation
- [] Header at top?
- [] About first with purpose?
- [] References in bulleted list format with categories?
- [] Complexity appropriate (2-3/4-6/7+)?
- [] Structure logical?
- [] Separators used correctly?
- [] 10-round DEPTH applied?
- [] Only requested topic covered?

---

## 6. 🚨 ERROR RECOVERY

### Common Errors & Fixes

#### Wrong Symbol Hierarchy
**Fix:** Update to H1: ⌘/❖, H2: ⌥, H3: numbered when multiple subsections, H4: clean

#### About Section Not First
**Fix:** Move About to first position after metadata

#### Created Without User Input
**Fix:** Stop, apologize, ask comprehensive question, WAIT

#### Added Unrequested Content
**Fix:** Remove extras, keep only requested scope

#### Wrong Artifact Type
**Fix:** Recreate with `text/markdown`

#### Designs & References as Table
**Fix:** Convert to bulleted list with categories (Documentation, Flows, Related Stories/Tickets)

#### Missing Separators
**Fix:** Add `---` between major sections

#### Table of Contents Included
**Fix:** Remove ToC, rely on external tools

### Prevention Strategies
1. Apply DEPTH automatically (10 rounds standard, 1-5 quick)
2. Wait for comprehensive response
3. Check template version
4. Verify symbol hierarchy
5. Position sections correctly
6. Limit output to request
7. Use correct artifact type
8. Include all required elements
9. Apply appropriate separators
10. NEVER answer own questions

---

## 7. 📝 SIMPLE DOCUMENTATION TEMPLATE

```markdown
Mode: $doc | Complexity: Simple | Template: v0.119
---
# [Document Title]

**Parent:** [Parent Doc] | **Version:** 1.0 | **Reading Time:** 5 minutes
---

# ⌘ About
---
[Brief description of what this document covers and why it's important. 
This includes context about the feature/product being documented and 
its value to users - integrated naturally into the description.
Covers ONLY what user requested.]
---

## ⌥ References & Resources
---
**Documentation**
- UI Mockups - Current - [Link - to be added]
- Requirements Doc - Latest - [Link - to be added]

**Analytics**
- Performance Dashboard - Live - [Link - to be added]

**Related Stories**
- [Story 1] - [Link - to be added]
- [Story 2] - [Link - to be added]
---

# ❖ Key Features
---

### Overview
---
High-level description of the main capabilities and value proposition
[ONLY for the requested feature/product].
---

### Prerequisites

- Required access or permissions
- System requirements
- Prior knowledge needed

### Core Capabilities

1. **Feature One**
   - What it does [within requested scope]
   - Value proposition
   
2. **Feature Two**
   - What it does [within requested scope]
   - Value proposition

3. **Feature Three**
   - What it does [within requested scope]
   - Value proposition
---

# ❖ Success Metrics
---

### Performance Indicators
---

### Key Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Adoption Rate | >70% | 65% | On Track |
| Daily Usage | >80% | 82% | Achieved |
| User Satisfaction | >4.5 | 4.3 | At Risk |

### Response Protocols

- When metrics fall below threshold
- Escalation procedures
- Improvement strategies
```

---

## 8. 📖 STANDARD DOCUMENTATION TEMPLATE

```markdown
Mode: $doc | Complexity: Standard | Template: v0.119
---
# [Document Title]

**Parent:** [Parent Doc] | **Version:** 1.0 | **Reading Time:** 10 minutes
---

# ⌘ About
---
[Detailed description of the documented feature or product, incorporating
the business context, user needs, market positioning, and value 
proposition. This narrative naturally includes why this documentation 
exists, who benefits from it, and how it fits into the larger ecosystem.
Covers ONLY the specific feature/product requested by user.]
---

## ⌥ References & Resources
---
**Documentation**
- Component Library - v2.1 - [Link - to be added]
- Product Requirements - Current - [Link - to be added]

**Flows**
- User Journey - Latest - [Link - to be added]

**Analytics**
- Performance Dashboard - Live - [Link - to be added]

**Research**
- User Studies - Latest - [Link - to be added]

**Related Stories**
- [Story 1] - [Link - to be added]
- [Story 2] - [Link - to be added]
---

# ❖ Product Overview
---

### 1. Architecture & Flow
---
System components and their relationships, showing how value flows through 
the product [limited to requested system only].
---

#### User Journey

- Entry points and onboarding
- Key interaction points
- Value delivery moments
- Success states

#### Integration Points

- External systems [relevant to requested feature]
- API connections
- Data flows
- Dependencies
---

### 2. Key Terminology
---

| Term | Definition | Context |
|------|------------|---------|
| **[Term 1]** | [Clear definition] | [When/where used] |
| **[Term 2]** | [Clear definition] | [When/where used] |
| **[Term 3]** | [Clear definition] | [When/where used] |
---

# ❖ Feature Specifications
---

### 1. Core Features
---

#### Primary Feature

**Description:** What the feature does and why it matters
[Within scope of user's request only]

**User Value:** Direct benefits to the end user

**Success Criteria:**
- Measurable outcome 1
- Measurable outcome 2
- Measurable outcome 3

#### Secondary Features

1. **Feature Name**
   - Purpose and functionality [as requested]
   - Target users
   - Expected impact

2. **Feature Name**
   - Purpose and functionality [as requested]
   - Target users
   - Expected impact
---

### 2. User Scenarios
---

#### Happy Path

1. User discovers feature
2. Initial engagement
3. Value realization
4. Continued usage

#### Edge Cases

**Scenario:** [Unusual situation]
**Handling:** [How system responds]
**Recovery:** [Path back to success]
---

# ❖ Performance Framework
---

### 1. Success Metrics
---

#### Key Performance Indicators

| Metric | Target | Threshold | Response |
|--------|--------|-----------|----------|
| User Adoption | >70% | <50% | Engagement campaign |
| Feature Usage | Daily | Weekly | Review positioning |
| Success Rate | >85% | <60% | UX improvements |
| Time to Value | <5 min | >15 min | Simplify onboarding |

#### Tracking Strategy

- Event definitions
- Data collection methods
- Reporting frequency
- Review cycles
---

### 2. Business Impact
---

#### Revenue Impact

- Direct monetization potential
- Indirect value creation
- Cost savings
- Efficiency gains

#### Strategic Value

- Market positioning
- Competitive advantage
- User retention impact
- Platform stickiness
```

---

## 9. 📗 COMPLEX DOCUMENTATION TEMPLATE

```markdown
Mode: $doc | Complexity: Complex | Template: v0.119
---
# [Platform/Ecosystem Documentation]

**Parent:** [Strategy Docs] | **Version:** 1.0 | **Reading Time:** 20 minutes
---

# ⌘ About
---
[Comprehensive overview of the documented platform, incorporating its 
evolution, current state, strategic importance, and future roadmap. 
This narrative weaves together the product vision, business 
drivers, market requirements, user needs, and stakeholder 
impacts into a cohesive story that explains not just what the platform 
does, but why it exists and how it creates value.
Documentation covers ONLY the specific platform/ecosystem requested by user.]
---

## ⌥ References & Resources
---
**Documentation**
- Product Vision - Current - [Link - to be added]
- Design System - v3.0 - [Link - to be added]
- Feature Specifications - Latest - [Link - to be added]

**Flows**
- User Journey Map - Current - [Link - to be added]

**Analytics**
- Platform Metrics Dashboard - Live - [Link - to be added]

**Research**
- Market Analysis - Recent - [Link - to be added]

**Roadmap**
- Product Planning - Active - [Link - to be added]

**Related Epics**
- [Epic 1] - [Link - to be added]
- [Epic 2] - [Link - to be added]

**Related Stories**
- [Story 1] - [Link - to be added]
- [Story 2] - [Link - to be added]
---

# ❖ Platform Strategy
---

## ◻︎ Vision & Mission
---
The north star that guides all platform decisions and investments
[for the requested platform only].
```
---

# ❖ Platform Strategy
---

### 1. Vision & Mission
---
The north star that guides all platform decisions and investments
[for the requested platform only].
---

#### Core Value Propositions

1. **Primary Value Driver**
   - What it solves [within platform scope]
   - Why it matters
   - Market impact

2. **Network Effects**
   - Growth mechanisms
   - Viral loops
   - Retention drivers

3. **Competitive Moat**
   - Unique advantages
   - Barriers to entry
   - Defensibility
---

### 2. Market Positioning
---

#### Target Segments

| Segment | TAM | Our Approach | Focus Level |
|---------|-----|--------------|-------------|
| **Enterprise** | $2.5B | Direct sales | High |
| **Mid-Market** | $1.8B | Product-led | High |
| **SMB** | $3.2B | Self-serve | Medium |
| **Consumer** | $5.0B | Freemium | Exploratory |

#### Go-to-Market Strategy

- Customer acquisition channels
- Conversion funnel optimization
- Expansion revenue model
- Partnership ecosystem
---

# ❖ Product Architecture
---

### 1. Core Capabilities
---

#### Discovery Engine

**Purpose:** Help users find value quickly

**Components:**
- Search functionality
- Recommendation system
- Personalization layer
- Content curation

**Success Metrics:**
- Time to first value
- Discovery satisfaction
- Engagement depth
---

#### Engagement Framework

**Purpose:** Keep users active and engaged

**Components:**
- Interaction model
- Gamification elements
- Social features
- Notification system

**Success Metrics:**
- Daily active usage
- Session duration
- Return frequency
---

### 2. Feature Ecosystem
---

#### Feature Map

| Category | Features | User Segment | Business Value |
|----------|----------|--------------|----------------|
| **Discovery** | Search, Browse, Recommend | All | Engagement |
| **Creation** | Tools, Templates, AI Assist | Power Users | Supply |
| **Collaboration** | Share, Comment, Co-create | Teams | Virality |
| **Analytics** | Insights, Reports, Tracking | Business | Monetization |
| **Administration** | Controls, Permissions, Billing | Enterprise | Revenue |
---

# ❖ Performance Metrics
---

### 1. North Star Framework
---

#### Primary Metrics

| Metric | Current | Target | Owner |
|--------|---------|--------|-------|
| MAU | 250K | 500K | Growth |
| Revenue/User | $25 | $45 | Product |
| NPS | 42 | 65 | Success |
| Retention D30 | 45% | 70% | Product |

#### Leading Indicators

- Activation rate trends
- Feature adoption curves
- User satisfaction scores
- Support ticket volume
---

### 2. Operational Excellence
---

#### Performance Tracking

**Real-time Monitoring**
- System health dashboards
- User behavior analytics
- Business metrics tracking
- Alert management

**Review Cadence**
- Daily standups: Operational metrics
- Weekly reviews: Business KPIs
- Monthly deep-dives: Strategic progress
- Period planning: Goal adjustment
---

#### Intervention Framework

| Status | Trigger | Response Time | Action | Escalation |
|--------|---------|---------------|---------|------------|
| Healthy | On track | Weekly | Monitor | None |
| Warning | -10% target | Daily | Investigate | Team Lead |
| Critical | -25% target | Immediate | Intervene | Director |
| Crisis | -50% target | War Room | All Hands | C-Suite |
---

# ❖ User Segments
---

### 1. Segmentation Strategy
---

#### Power Users (Top 10%)

**Characteristics:**
- Daily platform usage
- High feature adoption
- Content creation
- Community leadership

**Value Strategy:**
- VIP treatment
- Early access
- Enhanced support
- Revenue sharing
---

#### Core Users (Next 30%)

**Characteristics:**
- Regular engagement
- Moderate feature use
- Some content creation
- Social participation

**Growth Strategy:**
- Feature education
- Engagement campaigns
- Upgrade incentives
- Community building
---

### 2. Persona Development
---

#### Detailed Personas

| Persona | Primary Need | Solution | Success Metric | Monetization |
|---------|-------------|----------|----------------|--------------|
| **Creator** | Audience | Discovery | Followers | Subscription |
| **Business** | ROI | Analytics | Revenue | Enterprise |
| **Consumer** | Content | Curation | Time Spent | Ads/Premium |
| **Team Lead** | Efficiency | Collaboration | Productivity | Seats |
---

# ❖ Growth & Scaling
---

### 1. Growth Framework
---

#### Acquisition Strategy

**Channels:**
- Organic search (SEO)
- Paid acquisition (SEM/Social)
- Content marketing
- Partnership channels
- Referral program

**Metrics:**
- CAC by channel
- Conversion rates
- Payback period
- LTV/CAC ratio
---

#### Retention Mechanics

**Engagement Loops:**
- Daily habits formation
- Progress tracking
- Social reinforcement
- Reward systems

**Resurrection Campaigns:**
- Win-back sequences
- Re-engagement offers
- Feature announcements
- Community events
---

### 2. Scaling Operations
---

#### Infrastructure Scaling

| Component | Current | Target | Investment |
|-----------|---------|--------|------------|
| Users | 250K | 2M | $2M |
| Requests/sec | 1K | 10K | $500K |
| Data Storage | 10TB | 100TB | $300K |
| Team Size | 25 | 75 | $8M |

#### International Expansion

**Phase 1: English Markets**
- Market validation
- Minimal localization
- Payment integration
- Support coverage

**Phase 2: European Markets**
- Full localization
- Regional teams
- Local partnerships
- Compliance adherence

---

## 10. 🎯 FINAL REMINDERS

1. **Always wait** for user response (except $quick)
2. **Never answer** own questions
3. **About section first** after metadata (integrate context narratively)
4. **Designs as bullets** organized by category (Documentation, Flows, Analytics, Research, Related Stories/Tickets/Epics)
5. **Tables for metrics only** - not for References & Resources
6. **Use H3 for subsections** - number them (### 1. Title) only when multiple subsections exist
7. **Single subsection** uses clean H3 (no numbers, no symbols)
8. **Use `---` dividers** between all major sections
9. **Interactive questions** handled by Interactive Mode v0.305 file
10. **Header at top** as first line (Mode | Complexity | Template)
11. **No Table of Contents** (ClickUp/Jira provide native TOC)
12. **Only requested topic** - no scope expansion beyond user request
13. **DEPTH methodology** applied automatically (10 rounds standard, 1-5 quick)
14. **Template version** v0.119 confirmed before creation
15. **Complexity scales structure** not content scope (Simple: 2-3 sections, Standard: 4-6, Complex: 7+)
16. **Documentation focus** maintained throughout (product features, performance metrics, strategy docs)
```