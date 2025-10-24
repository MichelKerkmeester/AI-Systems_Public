# Product Owner - Template - PRD Mode - v0.129

Product Requirements Document templates with integrated formatting rules and quality standards. All delivery logic consolidated for self-contained operation.

---

## 📋 TABLE OF CONTENTS
1. [📝 PRD MODE OVERVIEW](#1-prd-mode-overview)
2. [📦 DELIVERY STANDARDS](#2-delivery-standards)
3. [📊 COMPLEXITY AUTO-SCALING](#3-complexity-auto-scaling)
4. [✨ FORMATTING RULES & STANDARDS](#4-formatting-rules--standards)
5. [✅ QUALITY CHECKLIST](#5-quality-checklist)
6. [🚨 ERROR RECOVERY](#6-error-recovery)
7. [📊 INITIATIVE PRD TEMPLATE](#7-initiative-prd-template)
8. [🎯 PROGRAM PRD TEMPLATE](#8-program-prd-template)
9. [🚀 STRATEGIC PRD TEMPLATE](#9-strategic-prd-template)
10. [⭐ FEATURE SPECIFICATION TEMPLATE](#10-feature-specification-template)

---

## 1. 📝 PRD MODE OVERVIEW

### Command: `$prd`

- **Purpose:** Create Product Requirements Documents with clear scope and implementation details
- **Output:** Always as `text/markdown` artifact
- **Thinking:** 10 rounds automatic (DEPTH methodology), 1-5 auto-scaled for $quick
- **Interactive Mode:** Handled by Interactive Mode system (see v0.301)
- **Key Focus:** Implementation clarity, success metrics, feature specifications - ONLY what user requests
- **Header Position:** Always at top as first line
- **Silent Processing:** User sees simple messages, not methodology details
- **Output Constraints:** Features limited to user's exact request, no scope expansion

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
- **Template Compliance:** Use v0.129 structure exactly

### PRD-Specific Standards
- **Scaling:** 
  - Initiative: 5-10 features, single team
  - Program: 10-20 features, multi-team
  - Strategic: 20+ features, company-wide
- **Output Focus:** ONLY deliver what user requested
- **No Scope Expansion:** Scale affects template structure, not feature count beyond request
- **Multiple Perspectives:** All analyze the SAME PRD requirements
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
- Put Success Metrics at top (should be after About)
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
- Position Success Metrics after About
- Use clean H3/H4 headers
- Place header at top of artifact
- Use status note format: `[Status note: "description"]`
- Deliver exactly what was requested

---

## 3. 📊 COMPLEXITY AUTO-SCALING

| Keywords | Scale | Team Scope | Features | DEPTH Processing |
|----------|-------|------------|----------|-----------------|
| feature, component | Initiative | Single team | 5-10 | 10 rounds (2 if $quick) |
| platform, system | Program | Multi-team | 10-20 | 10 rounds (3 if $quick) |
| strategic, ecosystem | Strategic | Company-wide | 20+ | 10 rounds (5 if $quick) |

**Important:** Scale determines TEMPLATE STRUCTURE, not content scope
- User requests "platform PRD" → Program template for THAT platform only
- NOT: Program template with multiple platforms or extra features

### DEPTH Processing Standards
- **Silent excellence:** User never sees methodology details
- **Automatic application:** No user choice on depth
- **Multiple perspectives:** All analyze SAME PRD requirements
- **Single output:** One PRD covering exact request
- **No scope expansion:** Scale affects template size, not feature count beyond request

---

## 4. ✨ FORMATTING RULES & STANDARDS

### Mandatory Structure Elements

#### Symbol Hierarchy
- **H1:** ⌘ (About), ❖ (Main sections)
- **H2:** ✦ (Success Metrics), ◻ (Subsections), ⌥ (Designs & References), ∅ (Risks when criteria met)
- **H3:** Clean headers (no symbols)
- **H4:** Clean headers (no symbols)

#### Structure Order
1. Header (Mode | Scale | Template) - FIRST LINE
2. Title
3. About (⌘) - Strategic context (2-5 sentences)
4. Success Metrics (✦) - Business/product metrics
5. Designs & References (⌥) - Numbered list format
6. Scope & Features (❖) - ONLY requested features
7. Technical Requirements (❖)
8. User Research (❖) - If applicable
9. Implementation Plan (❖)
10. Stakeholders (❖)
11. Risks & Mitigations (∅) - When criteria met

#### Formatting Standards
- **Dividers:** Use `---` between header and content, between sections
- **Lists:** Always use `-` for bullets
- **Designs & References:** Numbered list with bulleted items (no tables)
- **Links:** Use `[Link - to be added]` for placeholders
- **Brief About:** Keep to 2-5 sentences with executive summary
- **Status Notes:** Format as `[Status note: "description"]`

### Visual Hierarchy Rules
- One blank line before divider
- One blank line after divider
- Exception: No blank line after final divider
- Consistent spacing throughout
- Clean H3/H4 headers without symbols

### Content Integration
- Strategic context integrated in About
- Success metrics quantified and measurable
- Features limited to user's request
- Implementation phases clearly defined
- Platform specifications clear

### Risks Section Criteria (∅)
**Include Risks section with ∅ symbol (H2) when ANY of these apply:**
- Program/Strategic PRDs with 3+ identified risks
- Platform/architecture changes requiring mitigation strategies
- User explicitly requests risk analysis
- Project involves compliance, security, or data migration concerns

---

## 5. ✅ QUALITY CHECKLIST

### Pre-Creation Validation
- [] DEPTH methodology applied (10 rounds standard, 1-5 quick)?
- [] User responded to comprehensive question?
- [] System waited for response (never answered own questions)?
- [] Scale determined correctly?
- [] Template version confirmed (v0.129)?
- [] Output scope limited to user request?

### Structure Validation
- [] Header at top as first line?
- [] About section positioned first (after header)?
- [] Success Metrics after About?
- [] Designs & References in numbered list format?
- [] Feature inventory complete but limited to request?
- [] Correct symbol hierarchy applied?
- [] Implementation phases defined?
- [] Platform specifications included?
- [] Risks section (∅) if criteria met?

### Format Validation
- [] Using `text/markdown` artifact type?
- [] Lists use `-` bullets?
- [] Designs & References as numbered list (not table)?
- [] Dividers between sections?
- [] Placeholder links included?
- [] No Table of Contents?
- [] Features limited to user's request?
- [] Status notes use standard format?

### Mode-Specific Validation
- [] Header at top?
- [] About concise (2-5 sentences)?
- [] Success Metrics quantified?
- [] Feature inventory scaled (5-10/10-20/20+)?
- [] Implementation phases clear?
- [] Platform specifications included?
- [] 10-round DEPTH applied?
- [] Risks section (∅) if criteria met?
- [] Only requested features included?

---

## 6. 🚨 ERROR RECOVERY

### Common Errors & Fixes

#### Wrong Symbol Hierarchy
**Fix:** Update to H1: ⌘/❖, H2: ✦/◻/⌥/∅, H3/H4: clean

#### Success Metrics at Top
**Fix:** Move after About section

#### About Section Too Long
**Fix:** Condense to 2-5 sentences with executive summary

#### Created Without User Input
**Fix:** Stop, apologize, ask comprehensive question, WAIT

#### Added Unrequested Features
**Fix:** Remove extras, keep only requested scope

#### Wrong Artifact Type
**Fix:** Recreate with `text/markdown`

#### Missing RACI Matrix
**Fix:** Add stakeholder matrix to appropriate section

#### Feature Inventory Expanded Beyond Request
**Fix:** Limit to only what user specified

#### Designs & References as Table
**Fix:** Convert to numbered list with bulleted items

### Prevention Strategies
1. Apply DEPTH automatically (10 rounds standard, 1-5 quick)
2. Wait for comprehensive response
3. Check template version
4. Verify symbol hierarchy
5. Position sections correctly
6. Keep About concise
7. Position Success Metrics after About
8. Limit features to request
9. Include RACI matrix
10. Apply Risks criteria
11. NEVER answer own questions
12. Use correct artifact type
13. Use numbered list format for Designs & References

---

## 7. 📊 INITIATIVE PRD TEMPLATE

```markdown
Mode: $prd | Scale: Initiative | Template: v0.129
---
# [PRD Name]

# ⌘ About

[2-5 sentences describing what we're building, why it matters, and the value it delivers to users and the business. Covers ONLY the specific initiative/product requested by user.]

**Executive Summary**

**Product:** [One-sentence definition of requested product]
**Target Users:** [Primary segments for this product]
**Core Value:** [Key benefits and differentiation]

---

## ✦ Success Metrics

**Business Metrics**

| Metric | Current | Target | Measurement |
|--------|---------|--------|-------------|
| Primary KPI | [X] | [Y] | [How tracked] |
| Revenue Impact | $[X] | $[Y] | [System] |
| Cost Savings | $[X] | $[Y] | [Method] |

**Product Metrics**

| Metric | Baseline | Target | Success Threshold |
|--------|----------|--------|-------------------|
| Adoption Rate | - | [X]% | >[Y]% |
| Daily Active Users | [A] | [B] | >[C] |
| Feature Usage | - | [X]% | >[Y]% |

---

## ⌥ Designs & References

1. PRD
   • Product Requirements - Current - [Private - to be added]

2. Design
   • Feature Set 1 - Complete - [Link - to be added]
   • Feature Set 2 - In Progress - [Link - to be added]

3. Technical
   • API Specification - Review - [Private - to be added]

---

# ❖ Scope & Features

## ◻ Complete Feature List

**Core Features (Must Have)**
[Only features explicitly requested by user]

1. **[Feature Name 1 - from user's request]**
   
   - Description: [What this feature does and how it works]
   - User Value: [Why users need this and problems it solves]
   - Business Value: [Strategic reasons and expected ROI]
   
   Acceptance Criteria:
   - [Specific measurable criterion]
   - [Clear pass/fail condition]
   - [Feature completeness check]

2. **[Feature Name 2 - from user's request]**
   
   - Description: [Functionality breakdown with components]
   - Components: [UI/UX elements and interactions]
   - Behavior: [How the feature operates]
   - Edge Cases: [Special scenarios and handling]

3. **[Feature Name 3 - from user's request]**
   
   - Description: [Core functionality details]
   - Integration: [How it connects with other features]
   - Performance: [Expected metrics and standards]

**Enhanced Features (Should Have)**
[Only if user mentioned optional features]

4. **[Feature Name 4 - if requested]**
   
   - Description: [Enhancement building on core features]
   - Dependencies: [Prerequisites for implementation]
   - Value Add: [Additional benefits beyond core]

## ◻ Platform-Specific Implementation

**[Platform specified by user]**

[Status note: "Design 80% complete, awaiting final review"]

[2-4 sentences on platform-focused interface and workflows for user's specified platform only]

1. **[Component relevant to user's request]**
   - Layout: [Specific to requested feature]
   - Interactions: [Within requested scope]
   - State: [As needed for requested functionality]

---

# ❖ Technical Requirements

## ◻ Architecture

**System Overview**

[2-4 sentences on architecture approach for the requested system only]

- Services Affected: [Existing services requiring updates for this feature]
- New Services: [Services to create for requested functionality]
- Database Changes: [Schema modifications for requested features]
- API Changes: [Endpoints for requested capabilities]

## ◻ Integration Points

| System | Integration Type | Data Flow | Criticality |
|--------|-----------------|-----------|-------------|
| [Relevant to request] | REST/GraphQL | Bidirectional | High |
| [Relevant to request] | Event-driven | Publish | Medium |
| [If applicable] | Webhook | Subscribe | Low |

## ◻ Performance Requirements

**Response Time Targets**

| Operation | Target | Maximum | Measurement Point |
|-----------|--------|---------|-------------------|
| Page Load | <2s | 3s | First meaningful paint |
| API Response | <200ms | 500ms | Server response time |
| Search | <100ms | 200ms | Results display |

[2-3 sentences on caching strategy and graceful degradation for requested features]

---

# ❖ User Research & Validation

## ◻ Research Summary

[2-4 sentences on research methodology and key insights relevant to requested product]

**Research Conducted**

- Method: [Interviews, surveys, analytics]
- Key Finding: [Specific pain point related to user's request]
- Impact on Design: [How insights influenced requested features]

---

# ❖ Implementation Plan

## ◻ Development Phases

**Phase 1: Foundation**

[2-3 sentences on core infrastructure for requested features]

Deliverables:
- Core feature implementation [from user's request]
- Analytics integration
- API endpoints [for requested functionality]
- CI/CD pipelines

Exit Criteria:
- Unit test coverage >80%
- Deployment pipeline operational
- Security review completed

**Phase 2: Enhancement**

[2-3 sentences on advanced functionality for user's features]

Deliverables:
- Enhanced features [if requested]
- Performance optimizations
- Platform support [as specified]
- Integration testing

## ◻ Testing Strategy

**Test Coverage**

| Test Type | Coverage Target | Responsibility | Tools |
|-----------|-----------------|----------------|-------|
| Unit | >80% | Engineering | Jest/Mocha |
| Integration | Critical paths | QA | Selenium |
| E2E | User journeys | QA | Cypress |
| Performance | All endpoints | DevOps | K6/JMeter |

[2-3 sentences on testing philosophy for requested product]

---

# ❖ Stakeholders

## ◻ RACI Matrix

| Area | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| Product Definition | PM | VP Product | Stakeholders | Company |
| Technical Design | Tech Lead | Eng Manager | Architects | PM |
| Implementation | Engineers | Tech Lead | QA | PM |
| Quality Assurance | QA Lead | Eng Manager | PM | Stakeholders |
| Launch | PM | VP Product | All teams | Company |
```

---

## 8. 🎯 PROGRAM PRD TEMPLATE

```markdown
Mode: $prd | Scale: Program | Template: v0.129
---
# [Program Name] PRD

# ⌘ About

[2-5 sentences describing the program initiative, its strategic importance, and the transformational value it delivers across multiple teams and user segments. Focused ONLY on the specific program requested by user.]

**Executive Summary**

**Program:** [One-sentence definition of multi-team initiative]
**Scope:** [Teams and platforms involved in THIS program]
**Impact:** [User segments and business areas affected]

---

## ✦ Success Metrics

**Program-Level Metrics**

| Metric | Current | Target | Owner |
|--------|---------|--------|-------|
| Platform Adoption | [X]% | [Y]% | Product |
| Revenue Impact | $[X]M | $[Y]M | Business |
| User Satisfaction | [X] | [Y] | Success |
| Operating Efficiency | [X]% | [Y]% | Operations |

**Team-Specific Metrics**

| Team | Primary KPI | Target | Dependencies |
|------|-------------|--------|--------------|
| Frontend | Page Performance | <2s | API Team |
| Backend | API Latency | <200ms | Infrastructure |
| Mobile | App Crash Rate | <1% | <0.5% | Backend |
| Data | Pipeline Reliability | 99% | 99.5% | Infrastructure |

---

## ⌥ Designs & References

1. Architecture
   • System Design - Complete - Platform - [Link - to be added]

2. Frontend
   • UI Components - In Progress - Design - [Figma - to be added]

3. Backend
   • API Specs - Review - Engineering - [Swagger - to be added]

4. Mobile
   • App Designs - Complete - Mobile - [Link - to be added]

5. Data
   • Schema Design - Draft - Data Team - [Doc - to be added]

---

# ❖ Program Scope & Features

## ◻ Feature Inventory (10-20 Features)

**Platform Core (Features 1-5)**
[User's requested platform features only]

1. **[Core Feature 1]**
   - Team: [Responsible team]
   - Dependencies: [Other features/teams]
   - Success Criteria: [Measurable outcome]

2. **[Core Feature 2]**
   - Team: [Responsible team]
   - Dependencies: [Other features/teams]
   - Success Criteria: [Measurable outcome]

[Continue for features 3-5]

**User Experience (Features 6-10)**
[User's requested UX improvements only]

6. **[UX Feature 1]**
   - Team: Frontend + Design
   - User Impact: [Specific improvement]
   - Success Metric: [Measurable]

[Continue for features 7-10]

**Integration Layer (Features 11-15)**
[User's requested integrations only]

11. **[Integration Feature 1]**
    - Team: Backend + Partners
    - Systems: [Systems to integrate]
    - Data Flow: [Direction and volume]

[Continue for features 12-15]

**Analytics & Monitoring (Features 16-20)**
[If requested by user]

16. **[Analytics Feature 1]**
    - Team: Data + DevOps
    - Metrics Tracked: [Key metrics]
    - Dashboard: [Reporting tool]

[Continue as needed up to 20]

---

# ❖ Cross-Team Dependencies

## ◻ Dependency Matrix

| Feature | Depends On | Teams Involved | Critical Path | Risk Level |
|---------|------------|----------------|---------------|------------|
| [Feature A] | [Feature B, C] | Frontend, Backend | Yes | High |
| [Feature D] | [Feature A] | Mobile, API | Yes | Medium |
| [Feature E] | [Infrastructure] | All Teams | No | Low |

## ◻ Communication Plan

**Sync Schedule**

- Daily: Team standups (15 min)
- Weekly: Program sync (1 hour)
- Bi-weekly: Stakeholder update (30 min)
- Monthly: Executive review (1 hour)

**Escalation Path**

1. Team Lead → Engineering Manager
2. Engineering Manager → Program Manager
3. Program Manager → VP Engineering
4. VP Engineering → C-Suite

---

# ❖ Technical Architecture

## ◻ System Design

**Multi-Service Architecture**

[3-4 sentences describing the distributed system architecture for THIS program only]

**Service Breakdown**

| Service | Purpose | Technology | Team | Status |
|---------|---------|------------|------|--------|
| [Service 1] | [Core function] | [Tech stack] | [Team] | [Status] |
| [Service 2] | [Core function] | [Tech stack] | [Team] | [Status] |
| [Service 3] | [Core function] | [Tech stack] | [Team] | [Status] |

## ◻ Data Architecture

**Data Flow**

[2-3 sentences on how data moves through the system]

**Storage Strategy**

| Data Type | Storage | Volume | Retention | Backup |
|-----------|---------|--------|-----------|--------|
| Transactional | PostgreSQL | [X]TB | 7 years | Daily |
| Analytics | Data Lake | [X]PB | 2 years | Weekly |
| Cache | Redis | [X]GB | Session | None |
| Files | S3 | [X]TB | Permanent | Continuous |

---

# ❖ Implementation Roadmap

## ◻ Phase 1 Deliverables

**Month 1: Foundation**
- Infrastructure setup
- Core services deployment
- Basic feature rollout
- Initial testing

**Month 2: Integration**
- Service connections
- Data pipelines
- API gateway
- Monitoring setup

**Month 3: Optimization**
- Performance tuning
- Bug fixes
- User feedback incorporation
- Phase 1 feature completion

## ◻ Phase 2 Deliverables

**Month 4: Expansion**
- Additional features
- Platform scaling
- Partner integrations
- Advanced analytics

**Month 5: Enhancement**
- UX improvements
- Performance optimization
- Security hardening
- Feature refinement

**Month 6: Completion**
- Final features
- Full rollout
- Documentation
- Handoff to operations

---

## ∅ Risks & Mitigations

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| Technical debt accumulation | High | High | Dedicated refactoring sprints | Tech Lead |
| Cross-team coordination delays | Medium | High | Weekly sync meetings, shared dashboard | PM |
| Scope creep | High | Medium | Change control board, weekly reviews | Product |
| Resource constraints | Medium | High | Hiring plan, contractor backup | HR |
| Integration failures | Low | High | Early testing, fallback systems | Engineering |
```

---

## 9. 🚀 STRATEGIC PRD TEMPLATE

```markdown
Mode: $prd | Scale: Strategic | Template: v0.129
---
# [Strategic Initiative] PRD

# ⌘ About

[2-5 sentences describing the strategic transformation, its company-wide impact, market positioning advantages, and long-term value creation. Focused entirely on the user's requested strategic initiative.]

**Executive Summary**

**Vision:** [Transformational goal in one sentence]
**Scale:** [Company-wide impact across all divisions]
**Investment:** $[X]M
**ROI:** [Expected return]

---

## ✦ Success Metrics

**Strategic Objectives**

| Objective | Current State | Year 1 Target | Year 2 Target | Measurement |
|-----------|---------------|---------------|---------------|-------------|
| Market Share | [X]% | [Y]% | [Z]% | Industry reports |
| Revenue Growth | $[X]M | $[Y]M | $[Z]M | Financial systems |
| User Base | [X]M | [Y]M | [Z]M | Analytics platform |
| NPS Score | [X] | [Y] | [Z] | Survey platform |
| Operating Margin | [X]% | [Y]% | [Z]% | Finance |

**Phase Milestones**

| Phase | Key Results | Success Criteria | Risk Indicators |
|-------|-------------|------------------|-----------------|
| Phase 1 | Foundation complete | Infrastructure ready | Delays >2 weeks |
| Phase 2 | Core features live | 30% adoption | <20% adoption |
| Phase 3 | Scale achieved | 60% adoption | <40% adoption |
| Phase 4 | Optimization done | 90% adoption | <70% adoption |

---

## ⌥ Designs & References

1. Vision
   • Strategy Document - Approved - Critical - [Exec - to be added]

2. Architecture
   • Platform Design - Complete - Critical - [Tech - to be added]

3. Roadmap
   • Feature Plan - Active - High - [Product - to be added]

4. Business Case
   • ROI Analysis - Validated - Critical - [Finance - to be added]

5. Market Research
   • Competitive Analysis - Current - High - [Strategy - to be added]

---

# ❖ Strategic Scope (20+ Features)

## ◻ Feature Portfolio Overview

**Infrastructure & Platform (Features 1-7)**
[Foundation for user's requested transformation]

1. **Cloud Migration**
   - Scope: All services to AWS/Azure/GCP
   - Investment: $[X]M
   - Success: 99.99% uptime

[Continue for features 2-7]

**Core Product Features (Features 8-15)**
[User's requested product capabilities]

8. **[Core Capability 1]**
   - Impact: [User segment affected]
   - Team: Product + Engineering
   - Success: [Metric and target]

[Continue for features 9-15]

**Market Expansion (Features 16-20)**
[User's requested market initiatives]

16. **[Market Feature 1]**
    - Region: [Geographic/segment]
    - Investment: $[X]M
    - Success: [Market penetration %]

[Continue for features 17-20]

**Innovation Initiatives (Features 21-25+)**
[User's requested innovation areas]

21. **[Innovation 1]**
    - Technology: [AI/ML/Blockchain/etc]
    - R&D Investment: $[X]M
    - Expected Impact: [Metric]

[Continue for remaining features]

---

# ❖ Organizational Impact

## ◻ Transformation Requirements

**Organizational Structure**

| Division | Current State | Future State | Change Required |
|----------|---------------|--------------|-----------------|
| Engineering | [X] teams | [Y] teams | Hire [Z] engineers |
| Product | [X] PMs | [Y] PMs | Hire [Z] PMs |
| Sales | [X] reps | [Y] reps | Train & hire |
| Support | [X] agents | [Y] agents | Scale team |

**Capability Development**

- Technical Skills: [Required upskilling]
- Leadership Development: [Management training]
- Cultural Transformation: [Change management]
- Process Optimization: [Operational improvements]

---

# ❖ Technology Transformation

## ◻ Platform Architecture Evolution

**Current State → Future State**

[3-4 sentences describing the architectural transformation]

**Technology Stack Evolution**

| Layer | Current | Future | Migration Path | Risk |
|-------|---------|--------|----------------|------|
| Frontend | [Current tech] | [Future tech] | [Strategy] | [Level] |
| Backend | [Current tech] | [Future tech] | [Strategy] | [Level] |
| Data | [Current tech] | [Future tech] | [Strategy] | [Level] |
| Infrastructure | [Current tech] | [Future tech] | [Strategy] | [Level] |

## ◻ Scalability Requirements

**Performance Targets**

| Metric | Current | Year 1 | Year 2 | Infrastructure Needed |
|--------|---------|--------|--------|----------------------|
| Users | [X]M | [Y]M | [Z]M | [Requirements] |
| Transactions/sec | [X]K | [Y]K | [Z]K | [Requirements] |
| Data Storage | [X]PB | [Y]PB | [Z]PB | [Requirements] |
| Global Regions | [X] | [Y] | [Z] | [Requirements] |

---

# ❖ Market & Competition

## ◻ Competitive Positioning

**Market Analysis**

| Competitor | Their Strength | Our Advantage | Gap to Close | Strategy |
|------------|---------------|---------------|--------------|----------|
| [Competitor 1] | [Strength] | [Advantage] | [Gap] | [Approach] |
| [Competitor 2] | [Strength] | [Advantage] | [Gap] | [Approach] |
| [Competitor 3] | [Strength] | [Advantage] | [Gap] | [Approach] |

**Differentiation Strategy**

[3-4 sentences on unique value proposition and competitive moat]

---

# ❖ Financial Model

## ◻ Investment & Returns

**Investment Breakdown**

| Category | Year 1 | Year 2 | Total | Expected ROI |
|----------|--------|--------|-------|--------------|
| Technology | $[X]M | $[Y]M | $[Z]M | [Percentage] |
| People | $[X]M | $[Y]M | $[Z]M | [Percentage] |
| Marketing | $[X]M | $[Y]M | $[Z]M | [Percentage] |
| Operations | $[X]M | $[Y]M | $[Z]M | [Percentage] |
| **Total** | **$[X]M** | **$[Y]M** | **$[Z]M** | **[Percentage]** |

**Revenue Projections**

| Revenue Stream | Current | Year 1 | Year 2 | Growth % |
|---------------|---------|--------|--------|----------|
| [Stream 1] | $[X]M | $[Y]M | $[Z]M | [%] |
| [Stream 2] | $[X]M | $[Y]M | $[Z]M | [%] |
| [Stream 3] | $[X]M | $[Y]M | $[Z]M | [%] |
| **Total** | **$[X]M** | **$[Y]M** | **$[Z]M** | **[%]** |

---

## ∅ Strategic Risks & Mitigations

**Risk Portfolio**

| Risk Category | Specific Risk | Probability | Impact | Mitigation Strategy | Owner |
|---------------|---------------|-------------|--------|-------------------|-------|
| Market | Competitor response | High | High | First-mover advantage, patents | Strategy |
| Technology | Platform stability | Medium | Critical | Phased rollout, testing | CTO |
| Financial | Budget overrun | Medium | High | Contingency fund, phase gates | CFO |
| Organizational | Change resistance | High | Medium | Change management program | CHRO |
| Regulatory | Compliance changes | Low | High | Legal review, flexibility | Legal |
| Customer | Adoption resistance | Medium | High | Beta program, incentives | CMO |

**Contingency Plans**

[3-4 sentences on fallback strategies and pivot options]
```

---

## 10. ⭐ FEATURE SPECIFICATION TEMPLATE

```markdown
Mode: $prd | Scale: Feature | Template: v0.129
---
# [Feature Name] PRD

# ⌘ About

[2-5 sentences describing the specific feature requested by user, its purpose, who uses it, and the value it creates]

---

## ✦ Success Metrics

| Metric | Baseline | Current | Target |
|--------|----------|---------|--------|
| Usage | [X]% | [Y]% | >[Z]% |
| Errors | <[X]% | <[Y]% | <[Z]% |
| Performance | [X]ms | [Y]ms | <[Z]ms |
| Satisfaction | [X] | [Y] | >[Z] |

---

## ⌥ Designs & References

1. Design
   • Mockups - Complete - [Figma - to be added]
   • Prototype - In Review - [Link - to be added]

2. Docs
   • Spec Document - Approved - [Private - to be added]

3. API
   • Endpoint Spec - Draft - [Swagger - to be added]

---

# ❖ Feature Specification

## ◻ Functional Requirements

**Core Functionality**

[2-3 sentences on user interactions and system responses for requested feature only]

1. **Primary Function**
   - User Action: [What user does with this feature]
   - System Response: [How system behaves]
   - Result: [Outcome and value delivered]
   - Data Operations: [CRUD operations needed]

2. **Secondary Functions**
   - Supporting Action: [Additional capability]
   - Integration: [How it works with other features]
   - Constraints: [Limitations and boundaries]

## ◻ User Interface

**Component Architecture**

[2-3 sentences on modular components for requested feature]

Components:
- [Component 1]: [Responsibility within feature scope]
- [Component 2]: [Responsibility within feature scope]
- [Component 3]: [Functionality for this feature]

**User Flow**

1. Entry Point: [How users access feature]
2. Main Interaction: [Primary user actions]
3. Completion: [Success state]
4. Exit: [How users leave/complete]

## ◻ Business Logic

**Validation Rules**

[2-3 sentences on validation for requested feature]

Validation:
- Input validation: [Format, range, requirements]
- Business rules: [Constraints and conditions]
- Error handling: [User-friendly messages]
- Edge cases: [Special scenarios]

**State Management**

| State | Trigger | Behavior | Next State |
|-------|---------|----------|------------|
| Initial | Page load | Show default | Ready |
| Loading | User action | Show spinner | Success/Error |
| Success | Valid input | Show result | Ready |
| Error | Invalid input | Show message | Ready |

---

# ❖ Technical Implementation

## ◻ API Specification

**RESTful Endpoints**
[Only endpoints needed for requested feature]

```
GET /api/[feature]/list
Parameters: page, limit, sort, filter
Response: {items: [], total: number, page: number}

POST /api/[feature]/create
Body: {field1, field2, field3}
Response: {id: string, ...createdObject}

PUT /api/[feature]/update/{id}
Body: {updatable fields}
Response: {success: boolean, ...updatedObject}

DELETE /api/[feature]/delete/{id}
Response: {success: boolean, message: string}
```

## ◻ Data Model

**Schema Definition**

```javascript
{
  id: String (UUID),
  name: String (required),
  type: Enum ['type1', 'type2'],
  status: Enum ['active', 'inactive'],
  metadata: {
    created: DateTime,
    updated: DateTime,
    createdBy: String (userId),
    version: Number
  },
  [additionalFields]: [types]
}
```

---

# ❖ Testing & Acceptance

## ◻ Acceptance Criteria

**Functional Acceptance**

- [ ] User can [primary action]
- [ ] System [expected response]
- [ ] Data is [properly stored/retrieved]
- [ ] Feature works across [platforms/browsers]

**Non-Functional Acceptance**

- [ ] Performance meets targets (<[X]ms)
- [ ] Accessibility standards met (WCAG 2.1 AA)
- [ ] Security requirements satisfied
- [ ] Mobile responsive design works

## ◻ Test Scenarios

**Happy Path**
```
Given: [Initial state]
When: [User action]
Then: [Expected result]
```

**Error Scenarios**
```
Given: [Error condition]
When: [User action]
Then: [Error message and recovery]
```

**Edge Cases**
```
Given: [Unusual state]
When: [Uncommon action]
Then: [Graceful handling]
```

---

# ❖ Rollout Plan

## ◻ Phased Deployment

**Release Strategy**

| Phase | Audience | Size | Duration | Success Criteria |
|-------|----------|------|----------|------------------|
| Alpha | Internal | 100 | 1 week | No critical bugs |
| Beta | Selected | 1K | 2 weeks | <5% error rate |
| Pilot | Segment | 10K | 2 weeks | >80% satisfaction |
| GA | Everyone | All | Ongoing | All metrics met |

**Monitoring Plan**

[2-3 sentences on success tracking and rollback criteria]

**Communication**
- Internal announcement
- User documentation
- Training materials
- Support preparation
```