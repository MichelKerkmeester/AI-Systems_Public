# Ticket - Templates & Standards - v0.130

Comprehensive templates, symbols, and formatting standards for all ticket types with developer-first clarity. This is the single source of truth for ticket structure.

## Table of Contents

1. [📋 ARTIFACT STANDARDS](#1--artifact-standards)
2. [🔤 SYMBOL REFERENCE](#2--symbol-reference)
3. [📐 BASE TEMPLATES BY MODE](#3--base-templates-by-mode)
4. [✅ RESOLUTION CHECKLIST TEMPLATES](#4--resolution-checklist-templates)
5. [📝 FORMATTING STANDARDS](#5--formatting-standards)
6. [🎯 SECTION TEMPLATES](#6--section-templates)

---

## 1. 📋 ARTIFACT STANDARDS

### Critical Requirements

**🚨 CRITICAL:** Always use `text/markdown` artifact type when delivering structured content!

Never use `text/plain` for content with markdown formatting. This causes raw markdown to display instead of formatted text.

### Mandatory Header

Every ticket artifact MUST start with:

```markdown
MODE: [mode used]
TICKET TYPE: [Feature/Bug/Improvement/Epic]
MCP USED: [Sequential Thinking/Cascade Thinking/Figma/Multiple/None Available]
```

### Standard Structure

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking

---

[Ticket content follows standard template]
```

---

## 2. 🔤 SYMBOL REFERENCE

### Primary Section Symbols (Required)
- **❖** - Title and major feature sections
- **⌘** - About/contextual sections
- **◇** - Process/workflow sections and requirements
- **◊** - Sub-headings within sections (for organizing complex requirements)
- **→** - Designs & References sections
- **✓** - Success criteria sections AND Resolution Checklist
- **⊗** - Dependencies or out of scope
- **⚠** - Risks and important notices

### Secondary/Organization Symbols
- **—** - Sub-categories under **◊** sub-headings
- **◻︎** - Specific items/components within categories
- **◆** - Alternative major section marker
- **◈** - Document section headers
- **▸** - Sub-items or progressive disclosure
- **•** - Bullet points under items

### Symbol Hierarchy Example
```markdown
# ❖ [SCOPE] Main Feature
## ◇ Requirements
**◊** Component Name
— Category
• Specific requirement
• Another requirement
— Another Category
• More requirements

**◊** Another Component
— Logic
• Business logic item
• Another logic item
```

---

## 3. 📐 BASE TEMPLATES BY MODE

### 🚀 Quick Mode ($q) Template

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking

---

# ❖ [SCOPE] Feature Name

[1 paragraph description explaining the context, problem, and proposed solution. Include bullet points for key impacts or benefits if appropriate.]

**User Value:** [One-line user benefit]

**Business Goal:** [Specific metric improvement without percentages]

---

## ◇ Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
- [Requirement 4]

---

## ✓ Success Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

---

## ✓ Resolution Checklist
- [ ] [Implementation task 1]
- [ ] [Implementation task 2]
- [ ] [Testing task]
- [ ] [Mobile verification]
- [ ] [Code review]

---

## Labels
`[Component]`, `[Type]`, `feature`
```

### 📋 Standard Mode ($s) Template

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking

---

# ❖ [SCOPE] Feature Name

[Comprehensive paragraph describing the current situation, problem, and proposed solution. Include specific pain points, impacts, expected outcomes, and key benefits. Can use bullet points within the paragraph for clarity.]

**User Value:** [Detailed user benefit]

**Business Goal:** [Measurable business outcome without percentages]

---

## ◇ Requirements

**◊** [Component/Area 1]
— [Category]
• [Detailed requirement]
• [Another requirement]
— [Another Category]
• [More requirements]
• [Edge case handling]

**◊** [Component/Area 2]
— [Category]
• [Requirements for this area]
• [Additional details]

---

## → Designs & References
- [Figma - Main Flow](link)
- [API Documentation](link)

**Notice:** [Important implementation note]

---

## ✓ Success Criteria
- [ ] [Detailed criterion 1]
- [ ] [Performance metric]
- [ ] [User experience metric]
- [ ] [Business metric]

---

## ✓ Resolution Checklist

### Implementation
- [ ] [Core feature task 1]
- [ ] [Core feature task 2]
- [ ] [API integration]

### Testing & QA
- [ ] [Unit tests]
- [ ] [Integration tests]
- [ ] [Cross-browser testing]

### Documentation
- [ ] [Code documentation]
- [ ] [API updates]

---

## ⊗ Dependencies
- Requires: [Backend API] (#1234)
- Blocks: [Next feature] (#1235)

---

## Labels
`[Component]`, `[Feature-Area]`, `feature`
```

### 🔧 Complex Mode ($c) Template

```markdown
MODE: $c
TICKET TYPE: Feature
MCP USED: Cascade Thinking

---

# ❖ [SCOPE] Complex Feature Name

[Comprehensive paragraph describing the business context, current challenges, strategic importance, technical approach, key innovations, and expected transformational outcomes. Include specific metrics and impacts where relevant. Reference competing solutions and why this approach is superior.]

---

# ⌘ About

[1 paragraph explaining context and strategic importance]

**User Value:** [Comprehensive user benefit]

**Business Goal:** [Strategic outcome without percentages]

---

[[*TOC*]]

---

## → Designs & References

### ◻︎ User Flows
- [Figma - Complete Journey](link)
- [Figma - Edge Cases](link)

### ◻︎ Technical Architecture
- [Architecture Diagram](link)
- [API Specification](link)

---

## ◇ Phase 1: [Foundation] (Timeline)

**◊** Infrastructure Setup
— Backend
• API endpoint creation
• Database schema updates
• Authentication integration
— Frontend
• Component scaffolding
• State management setup
• Routing configuration

**◊** Core Components
— UI Components
• Base component library
• Design system integration
— Business Logic
• Validation rules
• Data transformation
• Error handling

---

## ◇ Phase 2: [Core Features] (Timeline)

**◊** Main Feature Implementation
— User Interface
• Primary workflow screens
• Interactive elements
• Responsive design
— Functionality
• Core business logic
• API integration
• Real-time updates

**◊** Integration Points
— External Systems
• Third-party API connections
• Webhook handlers
• Event synchronization

---

## ◇ Phase 3: [Enhancement] (Timeline)

**◊** Advanced Features
— Performance
• Caching implementation
• Query optimization
• Lazy loading
— User Experience
• Animations and transitions
• Accessibility improvements
• Error recovery flows

---

## ✓ Success Criteria
- [ ] [High-level metric 1]
- [ ] [Performance benchmark]
- [ ] [User adoption metric]
- [ ] [Business impact metric]

---

## ✓ Resolution Checklist

### Phase 1: Foundation
- [ ] [Infrastructure setup]
- [ ] [Basic components]
- [ ] [Initial testing]
- [ ] [Phase 1 demo]

### Phase 2: Core Features
- [ ] [Feature implementation]
- [ ] [Integration complete]
- [ ] [Performance optimization]
- [ ] [Phase 2 review]

### Phase 3: Enhancement
- [ ] [Advanced features]
- [ ] [UI/UX polish]
- [ ] [Final testing]
- [ ] [Production ready]

### Launch Preparation
- [ ] [Security review]
- [ ] [Monitoring configured]
- [ ] [Rollback plan]
- [ ] [Team handoff]

---

## ⊗ Dependencies
- Requires: [Major dependency 1] (#3001)
- Blocks: [Future initiative] (#3100)

---

## ⚠ Risks
- **[Risk 1]:** [Description and mitigation]
- **[Risk 2]:** [Description and mitigation]

---

## Labels
`[Primary-Component]`, `[Secondary-Component]`, `feature`, `complex`
```

### 🚀 Epic Mode ($e) Template

```markdown
MODE: $e
TICKET TYPE: Epic
MCP USED: Cascade Thinking

---

# ❖ [SCOPE] Epic: Epic Title

[Comprehensive paragraph describing the market opportunity, competitive landscape, strategic importance, high-level approach, major milestones, and transformational impact on the business and users. Include business drivers, urgency, and phased approach overview.]

**User Value:** [High-level user outcome]

**Business Goal:** [Strategic business objective]

---

## ⌘ Overview
[1 paragraph describing scope and importance]

---

## ✓ Success Metrics
- [ ] [Epic-level metric 1]
- [ ] [Epic-level metric 2]
- [ ] [Epic-level metric 3]

---

## ◇ Child Tickets

### ◻︎ Phase 1: [Foundation]
- [ ] **[SCOPE] Ticket 1** - [Brief description]
- [ ] **[SCOPE] Ticket 2** - [Brief description]

### ◻︎ Phase 2: [Core]
- [ ] **[SCOPE] Ticket 3** - [Brief description]
- [ ] **[SCOPE] Ticket 4** - [Brief description]

### ◻︎ Phase 3: [Enhancement]
- [ ] **[SCOPE] Ticket 5** - [Brief description]
- [ ] **[SCOPE] Ticket 6** - [Brief description]

---

## ✓ Resolution Checklist

### Epic Coordination
- [ ] All child tickets created
- [ ] Team assignments complete
- [ ] Timeline established
- [ ] Success metrics dashboard

### Cross-Cutting Concerns
- [ ] Design consistency verified
- [ ] API contracts finalized
- [ ] Security review scheduled
- [ ] Performance targets set

### Launch Readiness
- [ ] Beta testing complete
- [ ] Documentation ready
- [ ] Support team trained
- [ ] Go-live plan approved

---

## ⊗ Dependencies
- Requires: [Strategic prerequisite] (#5001)

---

## ⌘ Timeline
[Total timeline with phase breakdowns]

---

## Labels
`epic`, `[Program-Name]`
```

### 🐛 Bug Template

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking

---

# ❖ [SCOPE] Bug: Issue Description

[Comprehensive paragraph describing user impact, frequency of occurrence, business consequences, specific examples of user frustration, technical context about when the bug started appearing, and initial investigation findings.]

**User Value:** [What gets fixed for users]

**Business Goal:** [Why this fix matters to the business]

---

## ◆ Current Behavior
[What's happening now - the bug]

---

## ✓ Desired Behavior
[What should happen instead]

---

## ◈ Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Observe bug]

---

## → Evidence
- [Screenshot - Bug](link)
- [Error logs](link)

---

## ✓ Success Criteria
- [ ] Bug no longer reproducible
- [ ] No regression in related features
- [ ] Works across all supported browsers

---

## ✓ Resolution Checklist

### Investigation
- [ ] Reproduce bug locally
- [ ] Identify root cause
- [ ] Check for related issues

### Fix Implementation
- [ ] Implement fix
- [ ] Verify bug resolved
- [ ] Add regression test

### Verification
- [ ] Test on all browsers
- [ ] Deploy to staging
- [ ] Monitor for recurrence

---

## Labels
`bug`, `[Component]`, `[Severity]`
```

### 📈 Improvement Template

```markdown
MODE: $s
TICKET TYPE: Improvement
MCP USED: Sequential Thinking

---

# ❖ [SCOPE] Improvement: Enhancement Description

[Comprehensive paragraph describing current limitations, their impact on users and business, specific pain points and inefficiencies, the improvement approach, expected benefits, measurable outcomes, and user experience gains.]

**User Value:** [How this improves user experience]

**Business Goal:** [Measurable improvement target]

---

## ◈ Current State
- [Current metric/behavior]
- [Pain points]
- [Limitations]

---

## ◆ Target State
- [Improved metric/behavior]
- [Benefits achieved]
- [New capabilities]

---

## ◇ Requirements

**◊** Performance Improvements
— Backend
• Query optimization
• Caching strategy
• Connection pooling
— Frontend
• Bundle size reduction
• Lazy loading
• Code splitting

**◊** User Experience
— Visual
• Loading states
• Progress indicators
• Smooth transitions
— Functionality
• Improved workflows
• Better error handling

---

## ✓ Success Criteria
- [ ] [Performance target met]
- [ ] [User metric improved]
- [ ] [No negative side effects]

---

## ✓ Resolution Checklist

### Analysis
- [ ] Baseline measurements taken
- [ ] Improvement targets defined
- [ ] Impact assessment complete

### Implementation
- [ ] Apply optimizations
- [ ] Update related systems
- [ ] Add monitoring

### Validation
- [ ] Measure improvements
- [ ] Compare to targets
- [ ] Document results

---

## Labels
`improvement`, `[Component]`, `performance`
```

---

## 4. ✅ RESOLUTION CHECKLIST TEMPLATES

### Sizing by Mode

| Mode | Items | Structure | Focus |
|------|-------|-----------|-------|
| **Quick ($q)** | 3-5 | Single list | Essential tasks |
| **Standard ($s)** | 8-15 | 2-3 categories | Balanced coverage |
| **Complex ($c)** | 15-30 | Phase-based | Progressive work |
| **Epic ($e)** | 10-20 | Coordination | High-level tasks |

### Category Templates

**Implementation Category**
```markdown
### Implementation
- [ ] Build UI components per design
- [ ] Implement business logic
- [ ] Connect to backend APIs
- [ ] Add error handling
- [ ] Implement state management
```

**Testing Category**
```markdown
### Testing & QA
- [ ] Write unit tests (high coverage)
- [ ] Create integration tests
- [ ] Test on all browsers
- [ ] Verify mobile responsiveness
- [ ] Performance testing
```

**Documentation Category**
```markdown
### Documentation
- [ ] Update API documentation
- [ ] Add inline code comments
- [ ] Update team wiki
- [ ] Create user guide
- [ ] Document configuration
```

**Deployment Category**
```markdown
### Deployment
- [ ] Update deployment scripts
- [ ] Configure environment variables
- [ ] Set up monitoring
- [ ] Create rollback plan
- [ ] Verify in staging
```

### SMART Criteria for Checklist Items

Every item should be:
- **S**pecific - Clear what needs to be done
- **M**easurable - Can mark as complete or not
- **A**ctionable - Developer knows how to start
- **R**elevant - Contributes to ticket completion
- **T**ime-bound - Fits within ticket scope

---

## 5. 📝 FORMATTING STANDARDS

### Titles
- Always use `# ❖` (h1) for main ticket titles
- Include `[SCOPE]` prefix before feature name
- Keep titles clear and descriptive

### Section Dividers
Always use `---` between ALL major sections

### Text Formatting
- **Bold** for emphasis and key terms (including **◊** in sub-headings)
- *Italics* sparingly for subtle emphasis
- `Code` for technical terms
- Em dashes (—) ONLY for sub-categories under **◊** sub-headings

### Links
```markdown
[Descriptive Text](url)
[Figma - Component Name](figma-url)
[API Documentation](api-url)
```

### Lists
- Use `-` for unordered lists
- Use `1.` for ordered lists
- Use `- [ ]` for checkboxes
- Indent with 2 spaces for nested items
- Use `•` for bullet points under sub-categories

### Arrows & Flow
- Use `→` for cause/effect or flow
- Example: `User clicks → Modal opens`

### Notices
```markdown
**Notice:** Important information that could be missed
```

---

## 6. 🎯 SECTION TEMPLATES

### Description Template

**The single paragraph should cover:**
- Current situation and problem
- Specific pain points
- User/business impact
- Proposed solution approach
- Expected benefits
- Key improvements
- Success indicators
- Data or examples (without percentages)

**Use bullet points within the paragraph for:**
- Multiple impacts or problems
- Key benefits or features
- Important considerations

### Requirements Patterns

**Simple Requirements**
```markdown
## ◇ Requirements
- Clear requirement 1
- Clear requirement 2
- Clear requirement 3
```

**Complex Requirements with Sub-headings**
```markdown
## ◇ Requirements

**◊** User Interface
— Components
• Header updates
• Navigation changes
• Footer modifications
— Interactions
• Click handlers
• Hover states
• Keyboard navigation

**◊** Backend Logic
— API Changes
• New endpoints
• Updated responses
• Error handling
— Database
• Schema updates
• Migration scripts
• Index optimization
```

**Flow-Based Requirements**
```markdown
## ◇ Requirements
- **User uploads file** → System validates format
- **Validation fails** → Show specific error message
- **Validation passes** → Process and store file
```

### Success Criteria Patterns

Always use checkboxes and be specific:

```markdown
## ✓ Success Criteria
- [ ] Feature works as designed on all devices
- [ ] Page loads quickly within acceptable time
- [ ] Majority of users complete task successfully
- [ ] Zero critical bugs in production
- [ ] Analytics tracking implemented
```

### Designs & References Section

```markdown
## → Designs & References

### ◻︎ Design Files
- [Figma - Desktop Flow](link)
- [Figma - Mobile Flow](link)

### ◻︎ Technical Documentation
- [API Specification](link)
- [Database Schema](link)

**Notice:** Mobile uses different navigation pattern
```

---

*This document is the single source of truth for all ticket templates and standards. Reference specific sections using anchors like `Ticket - Templates & Standards.md#quick-mode` or `Ticket - Templates & Standards.md#symbols`. Version 1.3.0 updates: 1-paragraph descriptions, "Desired Behavior" for bugs, removed Technical Details sections.*