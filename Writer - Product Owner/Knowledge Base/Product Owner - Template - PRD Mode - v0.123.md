# Product Owner - Template - PRD Mode - v0.123

## 📋 TABLE OF CONTENTS

1. [📝 PRD MODE OVERVIEW](#1-📝-prd-mode-overview)
2. [📊 COMPLEXITY AUTO-SCALING](#2-📊-complexity-auto-scaling)
3. [📊 DETAILED PRD TEMPLATE](#3-📊-detailed-prd-template)
4. [🎯 FEATURE SPECIFICATION TEMPLATE](#4-🎯-feature-specification-template)
5. [✨ PRD FORMATTING RULES](#5-✨-prd-formatting-rules)
6. [🗣️ INTERACTIVE QUESTIONS](#6-🗣️-interactive-questions)

---

<a id="1-📝-prd-mode-overview"></a>

## 1. 📝 PRD MODE OVERVIEW

### Command: `$prd`

- **Purpose:** Create Product Requirements Documents with clear scope and implementation details
- **Output:** Always as artifact
- **Thinking:** 10 rounds automatic (ultrathink), 1-5 auto-scaled for $quick
- **Interactive Mode:** Single comprehensive question gathering all requirements
- **Key Focus:** Implementation clarity, success metrics, feature specifications

---

<a id="2-📊-complexity-auto-scaling"></a>

## 2. 📊 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Scope Level | Features | Document Depth |
|----------|------------|-------------|----------|----------------|
| feature, component, update | Initiative | Single team/quarter | 5-10 | Component level |
| platform, system, integration | Program | Multi-team/half-year | 10-20 | System level |
| strategic, ecosystem, transformation | Strategic | Company-wide/annual | 20+ | Platform level |

---

<a id="3-📊-detailed-prd-template"></a>

## 3. 📊 DETAILED PRD TEMPLATE

```markdown
# [PRD Name]

# ⌘ About

[Comprehensive description of what we're building and why it matters. This narrative 
naturally incorporates the problem we're solving, the opportunity we're capturing, 
the impact on our users and business, and how this aligns with our strategic goals. 
The story weaves together market context, user needs, competitive landscape, and 
business objectives into a compelling case for why this product or feature needs 
to exist now.]

**Executive Summary**

**Product:** [Clear one-sentence definition of what we're building]
**Target Users:** [Primary segments who will benefit]
**Core Value:** [Key benefits and differentiation]
**Timeline:** [Duration with major milestones]

---

## ✦ Success Metrics

**Business Metrics**

| Metric | Current | Target (Q1) | Target (Q2) | Measurement |
|--------|---------|-------------|-------------|-------------|
| Primary KPI | [X] | [Y] | [Z] | [How tracked] |
| Revenue Impact | $[X] | $[Y] | $[Z] | [System] |
| Cost Savings | $[X] | $[Y] | $[Z] | [Method] |

**Product Metrics**

| Metric | Baseline | Week 2 | Week 4 | Success Threshold |
|--------|----------|--------|--------|-------------------|
| Adoption Rate | - | [X]% | [Y]% | >[Z]% |
| Daily Active Users | [A] | [B] | [C] | [D] |
| Feature Usage | - | [X]% | [Y]% | >[Z]% |

---

## ⌥ Designs & References

| Type | Document | Status | Link |
|------|----------|--------|------|
| PRD | Product Requirements | Current | [Private - to be added] |
| Design | Feature Set 1 | Complete | [Link - to be added] |
| Design | Feature Set 2 | In Progress | [Link - to be added] |
| Technical | API Specification | Review | [Private - to be added] |
| Technical | Data Model | Approved | [Private - to be added] |

---

# ■ Scope & Features

## ◻️ Complete Feature List

**Core Features (Must Have)**

1. **[Feature Name 1]**
   
   Description: [Detailed explanation of what this feature does and how it works]
   
   User Value: [Clear articulation of why users need this and the problems it solves]
   
   Business Value: [Strategic reasons for building this and expected ROI]
   
   Acceptance Criteria:
   - [Specific measurable criterion that can be tested]
   - [Another specific criterion with clear pass/fail conditions]
   - [Additional criterion ensuring feature completeness]

2. **[Feature Name 2]**
   
   Description: [Comprehensive functionality breakdown including all components]
   
   Components: [List of UI/UX elements and their interactions]
   
   Behavior: [Step-by-step explanation of how the feature operates]
   
   Edge Cases: [Special scenarios and how the system handles them]

**Enhanced Features (Should Have)**

3. **[Feature Name 3]**
   
   Description: [Enhancement that builds upon core features]
   
   Dependencies: [What must exist before this can be implemented]
   
   Value Add: [Additional benefit this provides beyond core functionality]

## ◻️ Platform-Specific Implementation

**Creator Application**

[Feature Area 1]
[Status note: "Design 80% complete, awaiting final review"]

The creator application focuses on empowering content creators with intuitive tools 
for managing their presence and engaging with their audience. Each interface is 
designed with creator workflows in mind, minimizing friction and maximizing 
creative output.

1. **Content Management Dashboard**
   
   Visual specifications include a card-based layout with drag-and-drop functionality, 
   responsive grid system adapting to viewport size, and real-time preview capabilities.
   
   User interactions support bulk operations, inline editing, and keyboard shortcuts 
   for power users. The system maintains state across sessions and provides undo/redo 
   functionality for all destructive actions.

**Partner Application**

[Admin Feature 1]

The partner application provides comprehensive administrative capabilities with 
role-based access control and enterprise-grade security. Designed for scalability, 
it supports multi-tenant architectures and white-label customization options.

1. **Administrative Interface**
   
   Permissions are granularly controlled at the feature level, with inheritance 
   models supporting complex organizational structures. Actions include full CRUD 
   operations with audit trails, batch processing with progress indicators, and 
   scheduled operations with notification systems.

---

# ■ Technical Requirements

## ◻️ Architecture

**System Architecture Overview**

The technical implementation leverages a microservices architecture with event-driven 
communication patterns. Services are containerized and orchestrated using Kubernetes, 
with horizontal scaling based on load metrics. The system maintains backward 
compatibility through API versioning and feature flags.

Services Affected: [List of existing microservices requiring updates]
New Services: [Services to be created with their responsibilities]
Database Changes: [Schema modifications with migration strategies]
API Changes: [Endpoints added/modified with versioning approach]

## ◻️ Integration Points

| System | Integration Type | Data Flow | Criticality |
|--------|-----------------|-----------|-------------|
| External API | REST/GraphQL | Bidirectional | High |
| Internal Service | Event-driven | Publish | Medium |
| Third-party | Webhook | Subscribe | Low |

## ◻️ Performance Requirements

**Response Time Targets**

| Operation | Target | Maximum | Measurement Point |
|-----------|--------|---------|-------------------|
| Page Load | <2s | 3s | First meaningful paint |
| API Response | <200ms | 500ms | Server response time |
| Search | <100ms | 200ms | Results display |

The system must maintain these performance characteristics under expected load 
conditions while gracefully degrading under peak traffic. Caching strategies 
include CDN for static assets, Redis for session data, and database query 
optimization for frequently accessed data.

---

# ■ User Research & Validation

## ◻️ Research Summary

Our research methodology combined quantitative analytics with qualitative user 
interviews to understand pain points and validate our solution approach. The 
research phase included multiple rounds of prototype testing with iterative 
refinements based on user feedback.

**Research Conducted**

Method: In-depth interviews with 25 target users, supplemented by survey data 
from 500+ respondents and analysis of existing usage patterns.

Key Finding: Users struggle with [specific pain point], leading to [measurable 
impact] on their workflow efficiency.

Impact on Design: This insight led us to prioritize [specific feature] and 
simplify [specific workflow] to reduce cognitive load.

---

# ■ Implementation Plan

## ◻️ Development Phases

**Phase 1: Foundation (Weeks 1-4)**

This phase establishes the core infrastructure and fundamental features that 
subsequent phases will build upon. Focus is on architectural soundness and 
establishing patterns that will scale.

Deliverables include core feature implementation, basic analytics integration, 
and foundational API endpoints. The team will establish coding standards, 
testing frameworks, and CI/CD pipelines during this phase.

Exit Criteria:
- All core features functional with unit test coverage >80%
- Automated deployment pipeline operational
- Security review completed with no critical findings

**Phase 2: Enhancement (Weeks 5-8)**

Building on the foundation, this phase adds sophisticated functionality and 
begins optimization work. User feedback from Phase 1 beta testing informs 
priority adjustments.

Deliverables include enhanced features, performance optimizations, and 
expanded platform support. Integration testing becomes the focus, ensuring 
all components work seamlessly together.

## ◻️ Testing Strategy

**Comprehensive Test Coverage**

| Test Type | Coverage Target | Responsibility | Tools |
|-----------|-----------------|----------------|-------|
| Unit | >80% | Engineering | Jest/Mocha |
| Integration | Critical paths | QA | Selenium |
| E2E | User journeys | QA | Cypress |
| Performance | All endpoints | DevOps | K6/JMeter |

Testing philosophy emphasizes shift-left practices with developers writing 
tests alongside code. Automated testing gates prevent regression, while 
manual exploratory testing discovers edge cases.

---

# ■ Stakeholders & Timeline

## ◻️ RACI Matrix

| Area | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| Product Definition | PM | VP Product | Stakeholders | Company |
| Technical Design | Tech Lead | Eng Manager | Architects | PM |
| Implementation | Engineers | Tech Lead | QA | PM |
| Quality Assurance | QA Lead | Eng Manager | PM | Stakeholders |
| Launch | PM | VP Product | All teams | Company |

## ◻️ Milestone Timeline

| Milestone | Date | Deliverable | Owner | Status |
|-----------|------|-------------|-------|--------|
| Kickoff | Week 0 | PRD Approved | PM | Complete |
| Design Complete | Week 2 | All Mockups | Design | In Progress |
| Phase 1 Complete | Week 4 | Core Features | Eng | Not Started |
| Phase 2 Complete | Week 8 | Enhancements | Eng | Not Started |
| Launch Ready | Week 12 | Full Product | All | Not Started |

---

## ∅ Risks & Mitigations

| Risk | Probability | Impact | Mitigation Plan |
|------|-------------|--------|-----------------|
| **Scope Creep** | High | High | Weekly scope reviews with change control process |
| **Technical Debt** | Medium | Medium | Dedicated refactoring sprints and code review standards |
| **Resource Availability** | Low | High | Cross-training and comprehensive documentation |

---
Mode: $prd | Complexity: Initiative | Template: v0.123
```

---

<a id="4-🎯-feature-specification-template"></a>

## 4. 🎯 FEATURE SPECIFICATION TEMPLATE

```markdown
# [Feature Name] PRD

# ⌘ About

[Clear, narrative description of the feature and its purpose. This story explains 
why this feature is being built now, who will use it, what problems it solves, 
and how it creates value for both users and the business. The description weaves 
together user feedback, market demands, and strategic objectives into a compelling 
case for the feature's existence.]

---

## ✦ Success Metrics

| Metric | Week 1 | Week 2 | Month 1 | Target |
|--------|--------|--------|---------|--------|
| Usage | [X]% | [Y]% | [Z]% | >[A]% |
| Errors | <[X]% | <[Y]% | <[Z]% | <[A]% |
| Performance | [X]ms | [Y]ms | [Z]ms | <[A]ms |

---

## ⌥ Designs & References

| Type | Resource | Status | Link |
|------|----------|--------|------|
| Design | Mockups | Complete | [Link - to be added] |
| Design | Prototype | In Review | [Link - to be added] |
| Docs | Spec Document | Approved | [Private - to be added] |
| Technical | API Schema | Draft | [Private - to be added] |

---

# ■ Feature Specification

## ◻️ Functional Requirements

**Core Functionality**

The feature operates through a series of user interactions and system responses 
designed to deliver value efficiently. Each interaction has been carefully 
considered to minimize cognitive load while maximizing utility.

1. **Primary Function**
   
   User Action: [Detailed description of what the user does]
   
   System Response: [Complete explanation of system behavior]
   
   Result: [Clear outcome and value delivered to user]
   
   Data Operations: [What gets created, read, updated, or deleted]

## ◻️ User Interface

**Component Architecture**

The interface consists of modular components that work together to create a 
cohesive user experience. Each component has defined responsibilities and 
clear interaction patterns.

Components include [Component 1] which handles [specific responsibility], 
[Component 2] managing [another responsibility], and [Component 3] providing 
[additional functionality]. These components communicate through well-defined 
interfaces and maintain separation of concerns.

## ◻️ Business Logic

**Validation and Processing Rules**

The system enforces business rules through multiple layers of validation, 
ensuring data integrity and consistent user experience. Rules are applied 
both client-side for immediate feedback and server-side for security.

Validation includes format checking, business constraint enforcement, and 
cross-field dependencies. Each validation failure provides clear, actionable 
error messages guiding users toward successful completion.

---

# ■ Technical Implementation

## ◻️ API Specification

**RESTful Endpoints**

GET /api/[feature]/list
Parameters: page, limit, sort, filter
Response: {items: [], total: number, page: number}
Description: Retrieves paginated list with sorting and filtering

POST /api/[feature]/create
Body: {field1, field2, field3}
Response: {id: string, ...createdObject}
Description: Creates new resource with validation

PUT /api/[feature]/update/{id}
Body: {updatable fields}
Response: {success: boolean, ...updatedObject}
Description: Updates existing resource with partial data

DELETE /api/[feature]/delete/{id}
Response: {success: boolean}
Description: Soft deletes resource maintaining audit trail

---

# ■ Testing & Acceptance

## ◻️ Acceptance Criteria

**Functional Acceptance**

The feature meets acceptance when users can successfully complete all primary 
workflows without errors. System responses are timely and accurate, with all 
data operations maintaining consistency and integrity. User feedback is clear 
and helpful, guiding successful task completion.

**Non-Functional Acceptance**

Performance meets or exceeds targets across all supported platforms. The 
interface is responsive and accessible, meeting WCAG 2.1 AA standards. 
Security measures prevent unauthorized access while maintaining usability.

## ◻️ Test Scenarios

**Comprehensive Test Coverage**

1. **Happy Path Scenario**
   
   User begins with [initial state], performs [series of actions], and 
   achieves [desired outcome]. System maintains consistency throughout 
   and provides appropriate feedback at each step.

2. **Error Recovery Scenario**
   
   User encounters [error condition] through [invalid action]. System 
   provides [clear error message] and [recovery path], allowing user 
   to correct and continue successfully.

---

# ■ Rollout Plan

## ◻️ Phased Deployment Strategy

**Gradual Rollout Approach**

Week 1: Internal testing with company employees to identify critical issues
Week 2: Beta release to 10% of users with feedback collection mechanisms
Week 3: Expand to 50% while monitoring metrics and gathering insights
Week 4: Full launch to 100% with celebration and communication plan

Each phase includes specific success criteria and rollback procedures. 
Monitoring dashboards track key metrics in real-time, with alerts for 
anomalies. Support teams are briefed and prepared for each phase.

---
Mode: $prd | Complexity: Feature | Template: v0.123
```

---

<a id="5-✨-prd-formatting-rules"></a>

## 5. ✨ PRD FORMATTING RULES

### Mandatory Elements

1. **About Section FIRST** with integrated narrative context
2. **Success Metrics AFTER About** (not at top)
3. **Executive Summary** within About section
4. **Designs & References** as table format
5. **Feature-First Structure** with clear specifications
6. **Implementation Details** with technical depth
7. **Status Callouts** where applicable
8. **Minimal Footer** with mode, complexity, template

### Symbol Reference

- **⌘** - About section (H1)
- **■** - Main sections (H1)
- **◻️** - Sub-sections (H2)
- **⌥** - Designs & References (H2)
- **✦** - Success Metrics (H2)
- **∅** - Risks (H2, Complex PRDs only)

### Header Hierarchy

1. **H1 Headers** - Use `#` with symbols
   - `# ⌘ About` - For About section
   - `# ■ [Section Name]` - For main sections

2. **H2 Headers** - Use `##` with symbols
   - `## ⌥ Designs & References` - For references
   - `## ◻️ [Subsection Name]` - For subsections
   - `## ✦ Success Metrics` - For metrics

3. **H3 Headers** - Clean format, no symbols
   - `### [Header Name]` - Standard formatting

4. **H4 Headers** - Clean format, no symbols
   - `#### [Header Name]` - Standard formatting

### Structure Order

1. Title
2. About (⌘) - Context with integrated problems
3. Success Metrics (✦) - Measurable outcomes  
4. Designs & References (⌥) - Table format
5. Scope & Features (■) - Complete inventory
6. Technical Requirements (■) - Architecture
7. User Research (■) - If applicable
8. Implementation Plan (■) - Phases
9. Stakeholders & Timeline (■) - RACI
10. Risks (∅) - When applicable
11. Footer - Minimal single line

### Content Guidelines

**Narrative Style:**
- Use descriptive paragraphs instead of bullet lists where possible
- Integrate context and reasoning into flowing narrative
- Explain the "why" alongside the "what"
- Connect features to user value and business objectives

**Technical Clarity:**
- Provide complete specifications without ambiguity
- Include all edge cases and error scenarios
- Define clear acceptance criteria
- Specify API contracts and data models

**Status Communication:**
- Use [Status note: "Description"] for in-progress items
- Indicate design completion percentages
- Note dependencies and blockers
- Track milestone achievement

### Formatting Standards

- Use consistent spacing between sections
- Tables for metrics, references, and structured data
- Code blocks for API specifications
- Always include "to be added" for placeholder links
- Use `---` dividers between major sections
- Narrative paragraphs for context and description
- Avoid excessive bullet points in favor of prose
- Single-line minimal footer at bottom

---

<a id="6-🗣️-interactive-questions"></a>

## 6. 🗣️ INTERACTIVE QUESTIONS

### PRD Interactive Flow - Single Comprehensive Question

```markdown
User: $prd customer dashboard

System: Let's create your customer dashboard PRD! 📋

**Applying comprehensive ATLAS analysis (10 rounds automatic)...**

Please provide the following information:

1️⃣ **PRD scale:**
   • Feature PRD - single feature specification
   • Initiative PRD - 5-10 features, single team, quarterly
   • Program PRD - 10-20 features, multi-team, half-year
   • Strategic PRD - 20+ features, platform-wide, annual

2️⃣ **Primary platform:**
   • Web only
   • Mobile only (iOS/Android)
   • Web + Mobile
   • All platforms (Web, iOS, Android, API)

3️⃣ **Key requirements & context:**
   • Core features needed
   • Target audience
   • Business objectives
   • Timeline constraints

Please respond with all details (e.g., "1. Initiative PRD, 2. Web + Mobile, 3. Real-time analytics for enterprise customers")

[WAIT FOR USER RESPONSE - DO NOT PROCEED]
```

**After user responds:**

```markdown
User: 1. Initiative PRD, 2. Web + Mobile, 3. Customer self-service portal with analytics

System: Creating your Initiative-level customer dashboard PRD with:
• 5-10 integrated features
• Web and mobile specifications
• Self-service portal focus
• Analytics capabilities
• Success metrics positioned after About
• Implementation roadmap
• 10-round ultrathink applied

Processing now...

[Creates comprehensive PRD document with minimal footer]
```

### PRD Type Differentiation

**Feature PRD:**
- Single feature deep-dive
- Detailed specifications
- Component-level design
- 2-week implementation

**Initiative PRD:**
- Feature collection (5-10)
- Single team ownership
- Quarter-long effort
- Integrated workflows

**Program PRD:**
- Multi-feature platform (10-20)
- Cross-team coordination
- Half-year timeline
- System integration

**Strategic PRD:**
- Platform transformation (20+)
- Company-wide impact
- Annual roadmap
- Ecosystem development