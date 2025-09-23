# Product Owner - Template - PRD Mode - v0.110

## 📋 TABLE OF CONTENTS

1. [🚀 EPIC MODE OVERVIEW](#1-🚀-epic-mode-overview)
2. [📈 COMPLEXITY AUTO-SCALING](#2-📈-complexity-auto-scaling)
3. [🧩 DETAILED EPIC TEMPLATE](#3-🧩-detailed-epic-template)
4. [🔍 FEATURE SPECIFICATION TEMPLATE](#4-🔍-feature-specification-template)
5. [🧭 TRANSFORMATION EPIC TEMPLATE](#5-🧭-transformation-epic-template)
6. [🗂️ EPIC FORMATTING RULES](#6-🗂️-epic-formatting-rules)
7. [🗣️ INTERACTIVE QUESTIONS](#7-🗣️-interactive-questions)

---

## 1. 🚀 PRD MODE OVERVIEW

### Command: `$prd`

* **Purpose:** Create comprehensive Product Requirements Documents with clear scope and implementation details
* **Output:** Always as artifact with feature-focused structure
* **Thinking Rounds:** 8-10 (comprehensive specification requires depth)
* **Focus:** Problem context, detailed features, implementation approach, success metrics
* **Format:** Problem → Scope → Implementation → Validation structure

---

## 2. 📈 COMPLEXITY AUTO-SCALING

| Complexity        | Scope Level          | Features       | Documentation | Implementation Depth |
| ----------------- | -------------------- | -------------- | ------------- | -------------------- |
| **Initiative**    | Single team/quarter  | 5-10 features  | 3-5 docs      | Component level      |
| **Program**       | Multi-team/half-year | 10-20 features | 6-10 docs     | System level         |
| **Strategic**     | Company-wide/annual  | 20+ features   | 10+ docs      | Platform level       |

---

## 3. 🧩 DETAILED PRD TEMPLATE

* **What it is:** A comprehensive PRD focusing on scope, features, and implementation details with clear success metrics.
* **When to use:** Product initiatives requiring detailed specifications, cross-functional coordination, or significant development effort.
* **Best practices – Do:** Define clear scope, detail all features, specify implementation approach, set measurable criteria.
* **Best practices – Don't:** Leave features vague, skip technical requirements, omit dependencies, or forget acceptance criteria.

```markdown
# → [PRD Name]

# ⌘ About
---
[Clear description of what we're building and why it matters to the business and users]

[Context about the opportunity, current state, and desired future state]
---
### ◻︎ Problem & Opportunity
---
**Problem:** [Concise problem statement]

**Opportunity:** [Market/user opportunity this addresses]

**Impact if solved:** 
- [Business impact metric 1]
- [User impact metric 2]
- [Technical capability unlocked]

**Strategic alignment:** [How this fits company goals]
---
### → Designs & References
---
Check out all the PRD's related documentation and designs:

| **Documentation** | **Creator App** (Figma) | **Partner App** (Figma) | **Technical** |
| --- | --- | --- | --- |
| Private ([PRD URL]) | [Feature Set 1](figma-url) | [Admin Portal](figma-url) | Private ([API Spec]) |
| Private ([Roadmap URL]) | [Feature Set 2](figma-url) | [Dashboard](figma-url) | Private ([Data Model]) |
| Private ([Analytics URL]) | [Mobile Views](figma-url) | [Analytics](figma-url) | Private ([Architecture]) |



# ❖ Scope & Features
---
## ◻︎ **Complete Feature List**
---
### ◊ **Core Features** (Must Have)
---
1. **[Feature Name 1]**
    - **Description:** [What this feature does]
    - **User Value:** [Why users need this]
    - **Business Value:** [Why we're building it]
    - **Acceptance Criteria:**
        - [Specific measurable criterion 1]
        - [Specific measurable criterion 2]
        - [Specific measurable criterion 3]
---
2. **[Feature Name 2]**
    - **Description:** [Detailed functionality]
    - **Components:** [UI/UX elements involved]
    - **Behavior:** [How it works]
    - **Edge Cases:** [Special scenarios handled]
---
3. **[Feature Name 3]**
    - **Description:** [Complete specification]
    - **Input:** [What user provides]
    - **Processing:** [What system does]
    - **Output:** [What user receives]
---
### ◊ **Enhanced Features** (Should Have)
---
4. **[Feature Name 4]**
    - **Description:** [Enhancement details]
    - **Dependencies:** [What must exist first]
    - **Value Add:** [Additional benefit provided]
---
5. **[Feature Name 5]**
    - **Description:** [Capability description]
    - **Integration:** [Systems it connects with]
    - **Data Flow:** [How information moves]
---
### ◊ **Future Features** (Nice to Have)
---
6. **[Feature Name 6]** - Phase 2
    - **Placeholder:** [Temporary solution]
    - **Future State:** [What it becomes]
---
## ◻︎ **Platform-Specific Implementation**
---
### ◊ **Creator App**
---
#### **–– [Feature Area 1]**
---
[Status note if applicable: "Design 80% complete, awaiting final review"]

1. **[Screen/Component Name]**
    - Visual specs: [Dimensions, layout]
    - Interactions: [User actions and system responses]
    - States: [Default, active, error, loading]
    - Data displayed: [What information shown]
---
2. **[Workflow Name]**
    - Step 1: [User action] → [System response]
    - Step 2: [User action] → [System response]  
    - Step 3: [User action] → [System response]
    - Completion: [Final state]
---
3. **[Navigation Updates]**
    - Menu changes: [What's added/modified]
    - Deep linking: [URL structure]
    - Back navigation: [Behavior]
---
#### **–– [Feature Area 2]**
---
1. **[Form/Input Component]**
    - Fields: [All inputs with validation]
    - Required vs Optional: [Clear marking]
    - Error handling: [Validation messages]
    - Submit behavior: [What happens on save]
---
2. **[Display Component]**
    - Layout: [Grid, list, cards]
    - Sorting: [Available options]
    - Filtering: [Available parameters]
    - Pagination: [Items per page]
---
### ◊ **Partner App**
---
#### **–– [Admin Feature 1]**
---
1. **[Management Interface]**
    - Permissions required: [Admin level needed]
    - Actions available: [CRUD operations]
    - Bulk operations: [Multi-select capabilities]
    - Audit logging: [What gets tracked]
---
2. **[Analytics Dashboard]**
    - Metrics displayed: [KPIs shown]
    - Date ranges: [Filtering options]
    - Export options: [CSV, PDF, API]
    - Real-time vs cached: [Data freshness]
---
#### **–– [Configuration Area]**
---
1. **[Settings Panel]**
    - Global settings: [System-wide configs]
    - User settings: [Per-account options]
    - Feature flags: [Toggleable features]
    - Environments: [Dev/Stage/Prod]
---
### ◊ **Mobile Specifics**
---
#### **–– iOS**
---
- Native integrations: [Face ID, Apple Pay, etc.]
- Gestures: [Swipe, pinch, long-press behaviors]
- Offline mode: [What works without connection]
---
#### **–– Android**
---
- Material design: [Compliance with guidelines]
- Hardware variations: [Screen sizes, capabilities]
- Background services: [Notifications, sync]
---
### ◊ **Web Responsive**
---
- Breakpoints: [Mobile <768px, Tablet 768-1024px, Desktop >1024px]
- Progressive disclosure: [What shows/hides per viewport]
- Touch vs mouse: [Interaction differences]



# ❖ Technical Requirements
---
## ◻︎ **Architecture**
---
### ◊ **System Architecture**
---
- **Services Affected:** [List of microservices]
- **New Services:** [What needs to be created]
- **Database Changes:** [Schema modifications]
- **API Changes:** [Endpoints added/modified]
---
### ◊ **Integration Points**
---
| System | Integration Type | Data Flow | Criticality |
| --- | --- | --- | --- |
| **[External API]** | REST/GraphQL | Bidirectional | High |
| **[Internal Service]** | Event-driven | Publish | Medium |
| **[Third-party]** | Webhook | Subscribe | Low |
---
## ◻︎ **Data Requirements**
---
### ◊ **Data Model**
---
1. **[Entity Name]**
    - Fields: [Complete field list with types]
    - Relations: [Foreign keys, joins]
    - Indexes: [Performance optimization]
    - Constraints: [Validation rules]
---
2. **[Entity Name]**
    - Storage estimate: [Volume projections]
    - Retention policy: [How long kept]
    - Privacy classification: [PII, sensitive, public]
---
### ◊ **Data Flow**
---
- **Input:** [Source systems and formats]
- **Processing:** [Transformations, validations]
- **Storage:** [Where and how stored]
- **Output:** [Consumption patterns]
---
## ◻︎ **Performance Requirements**
---
### ◊ **Response Times**
---
| Operation | Target | Maximum | Measurement Point |
| --- | --- | --- | --- |
| **Page Load** | <2s | 3s | First meaningful paint |
| **API Response** | <200ms | 500ms | Server response time |
| **Search** | <100ms | 200ms | Results display |
---
### ◊ **Scale Requirements**
---
- **Concurrent Users:** [Expected number]
- **Requests/Second:** [Peak load]
- **Data Volume:** [Storage needs]
- **Growth Rate:** [Projected scaling]
---
## ◻︎ **Security & Compliance**
---
### ◊ **Security Requirements**
---
- **Authentication:** [Method required]
- **Authorization:** [Permission model]
- **Encryption:** [At rest, in transit]
- **Audit:** [What gets logged]
---
### ◊ **Compliance**
---
- **Standards:** [GDPR, CCPA, SOC2, etc.]
- **Data Residency:** [Geographic requirements]
- **Retention:** [Legal requirements]



# ❖ User Research & Validation (Optional)
---
[Include this section if user research has been conducted]

## ◻︎ **Research Summary**
---
### ◊ **Research Conducted**
---
- **Method:** [Interviews, surveys, analytics]
- **Sample Size:** [N=X participants]
- **Key Finding:** [Most important insight]
- **Impact on Design:** [How this shaped features]
---
### ◊ **User Feedback**
---
- **Positive Signals:** [What users loved]
- **Concerns Raised:** [What needs addressing]
- **Feature Requests:** [Additional wants]



# ❖ Implementation Plan
---
## ◻︎ **Development Phases**
---
### ◊ **Phase 1: Foundation** (Weeks 1-4)
---
**Deliverables:**
- [Core feature 1]
- [Core feature 2]
- [Basic analytics setup]

**Exit Criteria:**
- All core features functional
- Automated tests passing
- Security review complete
---
### ◊ **Phase 2: Enhancement** (Weeks 5-8)
---
**Deliverables:**
- [Enhanced feature 1]
- [Enhanced feature 2]
- [Performance optimizations]

**Exit Criteria:**
- Performance targets met
- User acceptance testing passed
- Documentation complete
---
### ◊ **Phase 3: Polish** (Weeks 9-12)
---
**Deliverables:**
- [Remaining features]
- [Mobile optimizations]
- [Admin tools]

**Exit Criteria:**
- All platforms tested
- Load testing passed
- Launch readiness confirmed
---
## ◻︎ **Testing Strategy**
---
### ◊ **Test Coverage**
---
| Test Type | Coverage Target | Responsibility | Tools |
| --- | --- | --- | --- |
| **Unit** | >80% | Engineering | Jest/Mocha |
| **Integration** | Critical paths | QA | Selenium |
| **E2E** | User journeys | QA | Cypress |
| **Performance** | All endpoints | DevOps | K6/JMeter |
---
### ◊ **Acceptance Testing**
---
1. **Functional Testing**
    - All features work as specified
    - Edge cases handled gracefully
    - Error messages helpful
---
2. **Cross-platform Testing**
    - Desktop browsers (Chrome, Safari, Firefox, Edge)
    - Mobile (iOS Safari, Android Chrome)
    - Native apps (iOS, Android)
---
3. **Accessibility Testing**
    - WCAG 2.1 AA compliance
    - Screen reader compatibility
    - Keyboard navigation
---
## ◻︎ **Dependencies & Risks**
---
### ◊ **Dependencies**
---
| Dependency | Owner | Needed By | Status | Risk |
| --- | --- | --- | --- | --- |
| **[API Development]** | Backend Team | Week 2 | In Progress | Medium |
| **[Design Assets]** | Design Team | Week 1 | Complete | Low |
| **[Infrastructure]** | DevOps | Week 4 | Planning | High |
---
### ◊ **Risk Mitigation**
---
| Risk | Probability | Impact | Mitigation Plan |
| --- | --- | --- | --- |
| **Scope Creep** | High | High | Weekly scope reviews, change control process |
| **Technical Debt** | Medium | Medium | Refactoring sprints, code review standards |
| **Resource Availability** | Low | High | Cross-training, documentation |



# ❖ Success Metrics
---
## ◻︎ **Key Performance Indicators**
---
### ◊ **Business Metrics**
---
| Metric | Current | Target (Q1) | Target (Q2) | Measurement |
| --- | --- | --- | --- | --- |
| **[Primary KPI]** | [X] | [Y] | [Z] | [How tracked] |
| **[Revenue Impact]** | $[X] | $[Y] | $[Z] | [System] |
| **[Cost Savings]** | $[X] | $[Y] | $[Z] | [Method] |
---
### ◊ **Product Metrics**
---
| Metric | Baseline | Week 2 | Week 4 | Success Threshold |
| --- | --- | --- | --- | --- |
| **Adoption Rate** | - | [X]% | [Y]% | >[Z]% |
| **Daily Active Users** | [A] | [B] | [C] | [D] |
| **Feature Usage** | - | [X]% | [Y]% | >[Z]% |
| **User Satisfaction** | [A]/5 | [B]/5 | [C]/5 | >[D]/5 |
---
### ◊ **Technical Metrics**
---
- **Uptime:** >99.9%
- **Error Rate:** <0.1%
- **Response Time:** P95 <200ms
- **Test Coverage:** >80%
---
## ◻︎ **Launch Criteria**
---
### ◊ **Go/No-Go Checklist**
---
**Must Have (Go):**
- [ ] All core features complete and tested
- [ ] Performance requirements met
- [ ] Security review passed
- [ ] Documentation complete

**Should Have (Conditional):**
- [ ] Enhanced features operational
- [ ] Mobile apps approved
- [ ] Marketing materials ready

**Launch Decision Meeting:** [Date]



# ❖ Stakeholders & Timeline
---
## ◻︎ **RACI Matrix**
---
| Area | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| **Product Definition** | PM | VP Product | Stakeholders | Company |
| **Technical Design** | Tech Lead | Eng Manager | Architects | PM |
| **Implementation** | Engineers | Tech Lead | QA | PM |
| **Quality Assurance** | QA Lead | Eng Manager | PM | Stakeholders |
| **Launch** | PM | VP Product | All teams | Company |
---
## ◻︎ **Milestone Timeline**
---
| Milestone | Date | Deliverable | Owner | Status |
| --- | --- | --- | --- | --- |
| **Kickoff** | Week 0 | PRD Approved | PM | Complete |
| **Design Complete** | Week 2 | All Mockups | Design | In Progress |
| **Phase 1 Complete** | Week 4 | Core Features | Eng | Not Started |
| **Phase 2 Complete** | Week 8 | Enhancements | Eng | Not Started |
| **Launch Ready** | Week 12 | Full Product | All | Not Started |
---
## ◻︎ **Resource Allocation**
---
### ◊ **Team Composition**
---
- **Product:** 1 PM, 1 Product Designer
- **Engineering:** 2 Backend, 3 Frontend, 1 Mobile
- **QA:** 1 QA Engineer
- **DevOps:** 0.5 FTE support
```

---

## 4. 🔍 FEATURE-FOCUSED PRD TEMPLATE

* **What it is:** A focused PRD for specific features with detailed implementation specifications.
* **When to use:** Single feature development, incremental improvements, or focused enhancements.
* **Best practices – Do:** Deep dive on implementation details, include all states and edge cases, specify acceptance criteria.
* **Best practices – Don't:** Scope creep, mix multiple features, leave behaviors ambiguous.

```markdown
# [Feature Name] PRD

# ⌘ About
---
[Clear description of the feature and its purpose]

[Context about why this feature is being built now]
---
### ◻︎ Feature Summary
---
**Feature:** [One-sentence description]

**Users:** [Who will use this]

**Value Proposition:** [Why they need it]

**Success Metric:** [Primary measure of success]
---
### → Designs & References
---
| **Design** | **Documentation** | **Technical** |
| --- | --- | --- |
| [Mockups](figma-url) | Private ([Spec Doc]) | Private ([API]) |
| [Prototype](figma-url) | Private ([Analytics]) | Private ([Schema]) |



# ❖ Feature Specification
---
## ◻︎ **Functional Requirements**
---
### ◊ **Core Functionality**
---
1. **[Primary Function]**
    - **User Action:** [What user does]
    - **System Response:** [What happens]
    - **Result:** [Outcome for user]
    - **Data:** [What gets saved/modified]
---
2. **[Secondary Function]**
    - **Trigger:** [How activated]
    - **Process:** [Steps involved]
    - **Output:** [What user sees]
    - **Constraints:** [Limitations]
---
3. **[Supporting Function]**
    - **Purpose:** [Why needed]
    - **Behavior:** [How it works]
    - **Integration:** [What it connects to]
---
### ◊ **User Interface**
---
#### **–– Components**
---
- **[Component 1]:** [Description and behavior]
- **[Component 2]:** [Description and behavior]
- **[Component 3]:** [Description and behavior]
---
#### **–– States**
---
| State | Visual | Behavior | Transition |
| --- | --- | --- | --- |
| **Default** | [Appearance] | [What user can do] | [How to change] |
| **Active** | [Appearance] | [What's happening] | [Next state] |
| **Success** | [Appearance] | [Feedback shown] | [Duration] |
| **Error** | [Appearance] | [Error message] | [Recovery] |
| **Loading** | [Appearance] | [Indicator type] | [Timeout] |
---
### ◊ **Business Logic**
---
1. **Validation Rules**
    - [Field 1]: [Rule and error message]
    - [Field 2]: [Rule and error message]
    - [Field 3]: [Rule and error message]
---
2. **Calculations**
    - [Formula 1]: [Description and formula]
    - [Formula 2]: [Description and formula]
---
3. **Permissions**
    - [User Type 1]: [What they can do]
    - [User Type 2]: [What they can do]
    - [Admin]: [Additional capabilities]
---
## ◻︎ **Edge Cases & Error Handling**
---
### ◊ **Edge Cases**
---
| Scenario | Behavior | Message |
| --- | --- | --- |
| **[Edge case 1]** | [How handled] | [User feedback] |
| **[Edge case 2]** | [How handled] | [User feedback] |
| **[Edge case 3]** | [How handled] | [User feedback] |
---
### ◊ **Error Scenarios**
---
1. **[Error Type 1]**
    - Cause: [What triggers]
    - Message: "[Exact error text]"
    - Recovery: [How to fix]
---
2. **[Error Type 2]**
    - Cause: [What triggers]
    - Message: "[Exact error text]"
    - Recovery: [How to fix]



# ❖ Technical Implementation
---
## ◻︎ **API Specification**
---
### ◊ **Endpoints**
---
```
GET /api/[feature]/list
- Parameters: [page, limit, sort, filter]
- Response: {items: [], total: number, page: number}

POST /api/[feature]/create
- Body: {[field1], [field2], [field3]}
- Response: {id: string, ...createdObject}

PUT /api/[feature]/update/{id}
- Body: {[updatable fields]}
- Response: {success: boolean, ...updatedObject}

DELETE /api/[feature]/delete/{id}
- Response: {success: boolean}
```
---
### ◊ **Data Model**
---
```json
{
  "id": "string",
  "field1": "type",
  "field2": "type",
  "field3": {
    "nested1": "type",
    "nested2": "type"
  },
  "createdAt": "timestamp",
  "updatedAt": "timestamp"
}
```
---
## ◻︎ **Dependencies**
---
- **[Service 1]:** Required for [functionality]
- **[Library]:** Version X.Y needed
- **[Infrastructure]:** [Specific requirements]



# ❖ Testing & Acceptance
---
## ◻︎ **Acceptance Criteria**
---
### ◊ **Functional Acceptance**
---
- [ ] User can [primary action]
- [ ] System [expected response]
- [ ] Data is [saved/updated/deleted]
- [ ] Notifications [sent/displayed]
- [ ] Analytics [tracked]
---
### ◊ **Non-Functional Acceptance**
---
- [ ] Response time <[X]ms
- [ ] Works on all supported browsers
- [ ] Mobile responsive
- [ ] Accessible (WCAG 2.1 AA)
- [ ] No console errors
---
## ◻︎ **Test Scenarios**
---
1. **Happy Path**
    - Step 1: [Action]
    - Step 2: [Action]
    - Expected: [Result]
---
2. **Error Path**
    - Step 1: [Invalid action]
    - Expected: [Error handling]
---
3. **Edge Case**
    - Scenario: [Description]
    - Expected: [Behavior]



# ❖ Success & Rollout
---
## ◻︎ **Success Metrics**
---
| Metric | Week 1 | Week 2 | Month 1 | Target |
| --- | --- | --- | --- | --- |
| **Usage** | [X]% | [Y]% | [Z]% | >[A]% |
| **Errors** | <[X]% | <[Y]% | <[Z]% | <[A]% |
| **Performance** | [X]ms | [Y]ms | [Z]ms | <[A]ms |
---
## ◻︎ **Rollout Plan**
---
- **Week 1:** Internal testing
- **Week 2:** Beta users (10%)
- **Week 3:** Gradual rollout (50%)
- **Week 4:** Full launch (100%)
```

---

## 5. 🗂️ PRD FORMATTING RULES

### Structure Hierarchy

```markdown
# ⌘ About
---
[Product/feature overview]
---
### ◻︎ Problem & Opportunity
---
**Problem:** [Brief statement]
**Opportunity:** [Market/user opportunity]
**Impact:** [Measurable outcomes]
```

### Feature Specification Format

```markdown
### ◊ **Feature Name**
---
1. **Component/Function**
    - **Description:** [What it does]
    - **User Value:** [Why needed]
    - **Acceptance Criteria:**
        - [Specific criterion 1]
        - [Specific criterion 2]
```

### Implementation Details

```markdown
#### **–– Sub-feature**
---
- Specification: [Detailed requirement]
- Behavior: [How it works]
- Edge cases: [Special handling]
- Status: [Design/Dev status if applicable]
```

### Technical Requirements

```markdown
| Requirement | Specification | Priority | Status |
| --- | --- | --- | --- |
| **Performance** | <200ms | P0 | Not Started |
| **Scale** | 10k users | P1 | Planning |
```

### Required Patterns

1. **No Table of Contents** - Removed per ClickUp/Jira integration
2. **Feature-First Structure** - Clear scope and implementation details
3. **Status Callouts** - [Status note: "Design in progress"] where applicable
4. **Acceptance Criteria** - Specific, measurable requirements
5. **Technical Specs** - API, data model, dependencies
6. **Success Metrics** - Clear targets and measurement methods
7. **No Child Tickets** - Removed to maintain focus on requirements

---

## 6. 🗣️ INTERACTIVE QUESTIONS FOR PRD MODE

### Implementation-Focused Flow

```markdown
User: $prd customer dashboard

System: Let's create your customer dashboard PRD! 🎯

**How many thinking rounds should I use? (8-10)**

Based on "customer dashboard", I recommend: 8 rounds
- Complexity: Medium (multiple views and features)
- Feature Count: Estimating 8-12 components
- Technical: API and data requirements

Your choice?

[WAIT FOR USER INPUT]

User: 8

System: Let me understand your PRD scope:

1. How many main features/views? (5-10/10-20/20+)
2. Platforms needed? (Web/Mobile/Both)
3. Any integrations? (APIs/Services/None)
4. Timeline? (4 weeks/8 weeks/12 weeks)

[WAIT FOR ANSWERS]

User: 
1. 5-10 features
2. Web and mobile
3. Salesforce API
4. 8 weeks

System: Creating Initiative-level PRD with:
- 5-10 dashboard features
- Web + mobile specifications  
- Salesforce integration requirements
- 8-week phased delivery plan

[CREATES FEATURE-FOCUSED PRD]
```

### Quick Feature PRD

```markdown
User: $prd export functionality

System: Let's create your export functionality PRD! 🎯

**How many thinking rounds should I use? (8-10)**

Based on single feature scope, I recommend: 8 rounds
- Complexity: Low-Medium (focused feature)
- Specifications: Export formats, permissions
- Edge Cases: Error handling, large files

Your choice?

[WAIT FOR USER INPUT]

User: 8

System: Quick scope questions:

1. Export formats? (CSV/PDF/Excel/All)
2. Data types? (Reports/Users/Analytics)
3. Permissions needed? (Yes/No)

[WAIT FOR ANSWERS]

System: Creating Feature-Focused PRD with:
- Multi-format export specifications
- Data type handling details
- Permission requirements
- Complete acceptance criteria

[CREATES FOCUSED FEATURE PRD]
```

---

*All PRDs delivered as artifacts with auto-scaled complexity. Always ask thinking rounds and wait for response. Challenge when 6+ rounds. Focus on detailed scope, features, and implementation specifications. User research optional. Include AI System footer with process documentation. No Table of Contents per tool integration. Enhanced focus on what we're building with clear acceptance criteria.*