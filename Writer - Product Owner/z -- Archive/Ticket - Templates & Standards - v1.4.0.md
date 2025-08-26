# Ticket - Templates & Standards - v1.4.0

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
TICKET TYPE: [Feature/Bug/Improvement/Epic/Implementation Spec]
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
- **⚠︎** - Key problems/changes in descriptions
- **⁉** - Reasons why in descriptions

### Secondary/Organization Symbols
- **—** - Sub-categories under **◊** sub-headings
- **◻︎** - Specific items/components within categories
- **◆** - Alternative major section marker
- **◈** - Document section headers
- **▸** - Sub-items or progressive disclosure
- **•** - Bullet points under items

### Spec Mode Symbols (Simplified)
For $spec mode, use minimal symbols for cleaner technical documentation:
- Standard markdown headers (# ##)
- Code blocks with language specification
- Standard bullet points (-)
- Checkboxes for testing (- [ ])

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

[Brief introduction sentence about the feature or issue]

⚠︎ **Key problems/changes:**
* **Main issue** - Brief description
* **Second issue** - Brief description
* **Third issue** - Brief description

⁉ **Reasons why:**
* Expected outcome and business impact statement

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

[Brief introduction about the feature context and current situation]

⚠︎ **Key problems/changes:**
* **Problem 1** - Detailed description of the issue
* **Problem 2** - Impact on users or system
* **Problem 3** - Technical limitations or gaps
* **Problem 4** - Current workarounds and their issues

⁉ **Reasons why:**
* By implementing [solution approach], we'll achieve [specific benefits] and improve [key metrics]

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
— How to implement?
• Check and follow this implementation spec:
• {Component Implementation Spec}

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
- [ ] Review implementation specs if referenced
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

[Brief overview of the strategic initiative and its importance]

⚠︎ **Key problems/changes:**
* **Current limitation 1** - Impact on business operations
* **Technical debt** - System constraints and scaling issues
* **Competitive gap** - Market positioning challenges
* **User friction** - Experience problems causing churn
* **Performance issues** - Metrics below acceptable thresholds

⁉ **Reasons why:**
* This comprehensive implementation will transform [system/feature] by [approach], positioning us [market advantage] while [user benefits]. The phased approach ensures [risk mitigation] with measurable improvements in [key metrics].

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
— How to implement?
• Check and follow this implementation spec:
• {Infrastructure Setup Spec}

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

[High-level overview of the strategic initiative]

⚠︎ **Key problems/changes:**
* **Market gap** - Missing critical market segment
* **Competitive pressure** - Falling behind competitors
* **Revenue opportunity** - Untapped growth potential
* **User demand** - High volume of feature requests
* **Strategic imperative** - Critical for long-term success

⁉ **Reasons why:**
* This epic encompasses [scope description] that will [transformational impact]. Through [phased approach], we'll capture [market opportunity] while [risk mitigation]. Success means [strategic outcome].

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

### 🔧 Spec Mode ($spec) Template

```markdown
MODE: $spec
TYPE: Implementation Spec
MCP USED: Sequential Thinking

---

# [Feature Name] Implementation Spec

## Objective
[Clear, concise implementation goal in 1-2 sentences]

## [Primary Technical Section]
```[language]
[Code implementation example]
```

[Additional implementation details and explanations]

## Browser Compatibility
- **Chrome/Edge (Chromium)**: ✓ [Specific property/method]
- **Firefox**: ✓ [Specific property/method]
- **Safari**: ✓ [Specific property/method]
- **IE 10+**: [✓/✗] [Notes if needed]

## Key Points
- [Critical implementation detail]
- [Important consideration]
- [Performance note]
- [Accessibility requirement]

## Testing Checklist
- [ ] [Specific test case 1]
- [ ] [Browser compatibility verified]
- [ ] [Edge case handled]
- [ ] [Performance acceptable]
- [ ] [Accessibility compliant]
```

### 🐛 Bug Template

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking

---

# ❖ [SCOPE] Bug: Issue Description

[Brief description of the bug and its impact]

⚠︎ **Key problems:**
* **User impact** - How users are affected
* **Frequency** - How often it occurs
* **Business impact** - Revenue/conversion effects
* **Technical context** - When bug started appearing

⁉ **Reasons why:**
* Fixing this bug will [restore functionality], eliminate [user frustration], and prevent [business impact]

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

[Brief overview of what needs improvement]

⚠︎ **Key problems/changes:**
* **Current limitation** - Performance or functionality issue
* **User pain point** - Workflow inefficiency
* **Technical debt** - Outdated implementation
* **Metric underperformance** - Not meeting targets

⁉ **Reasons why:**
* By optimizing [area], we'll achieve [specific improvements] resulting in [measurable benefits] for both users and the business

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
| **Spec ($spec)** | 5-10 | Testing focus | Implementation verification |

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

**Spec Mode Testing Checklist**
```markdown
## Testing Checklist
- [ ] Implementation works as specified
- [ ] All code examples verified
- [ ] Browser compatibility confirmed
- [ ] Performance benchmarks met
- [ ] Edge cases handled properly
- [ ] Accessibility standards met
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
- Spec mode: Use plain `#` without symbols

### Section Dividers
Always use `---` between ALL major sections

### Text Formatting
- **Bold** for emphasis and key terms (including **◊** in sub-headings)
- *Italics* sparingly for subtle emphasis
- `Code` for technical terms
- Em dashes (—) ONLY for sub-categories under **◊** sub-headings

### Code Blocks (Spec Mode)
```markdown
```language
// Always specify language for syntax highlighting
const example = "code here";
```
```

### Links
```markdown
[Descriptive Text](url)
[Figma - Component Name](figma-url)
[API Documentation](api-url)
```

### Implementation Spec References
When referencing implementation specs within requirements:
```markdown
— How to implement?
• Check and follow this implementation spec:
• {Spec Name}
```

This pattern should be used:
- Under the appropriate requirement sub-heading
- Always as a sub-category with em dash (—)
- Always with the exact phrasing "How to implement?"
- The spec name in curly braces indicates a linked document

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

**Structure:**
1. Brief introduction sentence
2. **⚠︎ Key problems/changes:** bulleted list
3. **⁉ Reasons why:** impact and outcome statement

**Example:**
```markdown
The current search functionality is failing to meet user needs and causing significant business impact.

⚠︎ **Key problems/changes:**
* **Poor relevance** - Results don't match user intent
* **No filtering** - Users can't narrow down results
* **Slow performance** - Search takes 3-5 seconds
* **Mobile issues** - Interface breaks on small screens

⁉ **Reasons why:**
By implementing advanced search with filters, relevance scoring, and performance optimization, we'll dramatically reduce abandonment rates and increase conversion.
```

**Key Icons:**
- ⚠︎ for problems/changes section
- ⁉ for reasons/impact section

### Spec Mode Objective Template

**The objective should be:**
- 1-2 sentences maximum
- Technical goal focused
- Clear and actionable
- No business justification needed

Example:
```markdown
## Objective
Implement a dual-container layout where the left container displays a visible scrollbar and the right container maintains scroll functionality with a hidden scrollbar.
```

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

**Requirements with Implementation Spec Reference**
```markdown
## ◇ Requirements

**◊** Search Filters
— Filter Types
• Category multi-select
• Date range picker
• Price range slider
— How to implement?
• Check and follow this implementation spec:
• {Search Filter Implementation Spec}

**◊** Responsive Layout
— Breakpoints
• Desktop: 4 columns
• Tablet: 2 columns  
• Mobile: 1 column
— How to implement?
• Check and follow this implementation spec:
• {Responsive Grid Implementation Spec}
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

*This document is the single source of truth for all ticket templates and standards. Reference specific sections using anchors like `Ticket - Templates & Standards.md#quick-mode` or `Ticket - Templates & Standards.md#symbols`. Version 1.3.0 updates: 1-paragraph descriptions, "Desired Behavior" for bugs, removed Technical Details sections, added Spec mode template for implementation specifications.*