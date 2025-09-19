# Ticket - Templates & Standards - v2.2.0

Comprehensive templates, symbols, and formatting standards for all ticket types with developer-first clarity. This is the single source of truth for ticket structure.

## Table of Contents

1. [📋 ARTIFACT STANDARDS](#1--artifact-standards)
2. [🔤 SYMBOL REFERENCE](#2--symbol-reference)
3. [📐 BASE TEMPLATES BY MODE](#3--base-templates-by-mode)
4. [✦ RESOLUTION CHECKLIST TEMPLATES](#4--resolution-checklist-templates)
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
TICKET TYPE: [Feature/Bug/Improvement/Complex/Implementation Brief]
MCP USED: [Sequential Thinking/Cascade Thinking/Figma/Multiple/None Available]
INTERACTIVE OFFERED: [Yes/No/N/A]
```

### Standard Structure

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

[Ticket content follows standard template]
```

---

## 2. 🔤 SYMBOL REFERENCE

### Primary Section Symbols (Required for Tickets)
- **❖** - Title and major feature sections
- **⌘** - About/contextual sections (Complex mode)
- **◇** - Process/workflow sections and requirements
- **◊** - Sub-headings within sections (for organizing complex requirements)
- **→** - Designs & References sections
- **✦** - Success criteria sections (bullets only, no checkboxes)
- **✓** - Resolution Checklist sections (checkboxes only, no bullets)
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

### Symbol Usage Rules
- **✦** is EXCLUSIVELY for Success Criteria (bullets only, no checkboxes)
- **✓** is EXCLUSIVELY for Resolution Checklist sections (checkboxes only, no bullets)
- Never mix these formats - maintain clear distinction

### Spec Mode Approach (Minimal Symbols)
For $spec mode, use conversational format with minimal symbols:
- Standard markdown headers (# ##)
- Code blocks with language specification
- Clean formatting for technical content
- Focus on clarity over decoration

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

## ✦ Success Criteria
- Success metric 1
- Success metric 2

## ✓ Resolution Checklist
### Work Stream
[ ] Deliverable 1
[ ] Deliverable 2
```

---

## 3. 📐 BASE TEMPLATES BY MODE

### 🚀 Quick Mode ($q) Template

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A

---

# ❖ [SCOPE] Feature Name

[Brief introduction sentence about the feature or issue]

⚠︎ **Key problems/changes:**
* **Main issue** - Brief description
* **Second issue** - Brief description
* **Third issue** - Brief description

⁉ **Reasons why:**
[Expected outcome and business impact statement]

**User Value:** [One-line user benefit]

**Business Goal:** [Specific metric improvement without percentages]

---

## ◇ Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
- [Requirement 4]

---

## ✦ Success Criteria
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

---

## ✓ Resolution Checklist

### Implementation
[ ] Build core functionality
[ ] Apply styling and responsive behavior

### Verification
[ ] Test across browsers and devices
[ ] Validate against requirements

---

## Labels
`[Component]`, `[Type]`, `feature`
```

### 📋 Standard Mode ($s) Template

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - [Accepted/Declined]

---

# ❖ [SCOPE] Feature Name

[Brief introduction about the feature context and current situation]

⚠︎ **Key problems/changes:**
* **Problem 1** - Detailed description of the issue
* **Problem 2** - Impact on users or system
* **Problem 3** - Technical limitations or gaps
* **Problem 4** - Current workarounds and their issues

⁉ **Reasons why:**
By implementing [solution approach], we'll achieve [specific benefits] and improve [key metrics]

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

## ✦ Success Criteria
- [Detailed criterion 1]
- [Performance metric]
- [User experience metric]
- [Business metric]

---

## ✓ Resolution Checklist

### Foundation Work
[ ] Set up architecture and dependencies
[ ] Configure necessary integrations

### Core Development
[ ] Implement primary functionality
[ ] Add secondary features
[ ] Apply UI/UX requirements

### Testing & Validation
[ ] Complete functional testing
[ ] Verify cross-browser compatibility
[ ] Validate performance metrics

### Documentation
[ ] Update technical documentation
[ ] Create user guides if needed

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
TICKET TYPE: Complex
MCP USED: Cascade Thinking
INTERACTIVE OFFERED: Yes - [Accepted/Declined]

---

# ❖ [SCOPE] Complex Feature/Initiative Name

[Brief overview of the strategic initiative and its importance]

⚠︎ **Key problems/changes:**
* **Current limitation 1** - Impact on business operations
* **Technical debt** - System constraints and scaling issues
* **Competitive gap** - Market positioning challenges
* **User friction** - Experience problems causing churn
* **Performance issues** - Metrics below acceptable thresholds

⁉ **Reasons why:**
This comprehensive implementation will transform [system/feature] by [approach], positioning us [market advantage] while [user benefits]. The structured approach ensures [risk mitigation] with measurable improvements in [key metrics].

---

# ⌘ About

[1 paragraph explaining context and strategic importance]

**User Value:** [High-level user outcome]

**Business Goal:** [Strategic business objective]

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

## ◇ Implementation Approach

[Choose ONE of the following approaches based on the feature needs]

### Option A: Phased Development
[Use for incremental building of a single large feature]

#### Phase 1: [Foundation] (Timeline)

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

#### Phase 2: [Core Features] (Timeline)

**◊** Main Feature Implementation
— User Interface
• Primary workflow screens
• Interactive elements
• Responsive design
— Functionality
• Core business logic
• API integration
• Real-time updates

#### Phase 3: [Enhancement] (Timeline)

**◊** Advanced Features
— Performance
• Caching implementation
• Query optimization
• Lazy loading
— User Experience
• Animations and transitions
• Accessibility improvements
• Error recovery flows

### Option B: Child Ticket Breakdown
[Use for multi-team coordination or when discrete components exist]

#### ◻︎ Core Infrastructure
- [ ] **[BE] API Development** (#child-1) - Service layer and data models
- [ ] **[FE] Component Library** (#child-2) - Reusable UI components
- [ ] **[DevOps] Infrastructure Setup** (#child-3) - Deployment and monitoring

#### ◻︎ Feature Implementation
- [ ] **[FS] User Management** (#child-4) - Complete user flow
- [ ] **[FE] Dashboard** (#child-5) - Analytics and reporting
- [ ] **[BE] Integration Layer** (#child-6) - Third-party connections

#### ◻︎ Quality & Polish
- [ ] **[QA] Test Automation** (#child-7) - E2E test suite
- [ ] **[FE] Performance Optimization** (#child-8) - Speed improvements
- [ ] **[FS] Security Hardening** (#child-9) - Security audit and fixes

---

## ✦ Success Criteria
- [High-level metric 1]
- [Performance benchmark]
- [User adoption metric]
- [Business impact metric]
- [Quality metric]

---

## ✓ Resolution Checklist

### Foundation & Architecture
[ ] Establish technical foundation
[ ] Set up infrastructure and dependencies
[ ] Configure integrations

### Core Feature Development
[ ] Implement primary functionality
[ ] Build secondary features
[ ] Complete third-tier features

### Integration & Testing
[ ] Connect all components
[ ] Complete comprehensive testing
[ ] Validate against requirements

### Performance & Polish
[ ] Optimize performance
[ ] Apply UI/UX polish
[ ] Fix edge cases

### Documentation & Training
[ ] Complete technical documentation
[ ] Create user guides
[ ] Conduct team training

### Launch Preparation
[ ] Complete security audit
[ ] Finalize deployment plan
[ ] Prepare rollback strategy

---

## ⊗ Dependencies
- Requires: [Major dependency 1] (#3001)
- Requires: [Major dependency 2] (#3002)
- Blocks: [Future initiative] (#3100)

---

## ⚠ Risks
- **[Risk 1]:** [Description and mitigation]
- **[Risk 2]:** [Description and mitigation]
- **[Risk 3]:** [Description and mitigation]

---

## ⌘ Timeline
[Total timeline with phase/ticket breakdowns]

---

## Labels
`[Primary-Component]`, `[Secondary-Component]`, `complex`, `[priority-level]`
```

### 💻 Spec Mode ($spec) Template - CONCISE

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A (Minimal conversation)

---

# [Feature] Implementation

## Objective
[1-2 sentences describing what needs to be built]

## Implementation
```typescript/css/javascript
// Actual working code - no placeholders
const Component = ({ data }: Props) => {
  return <div className="component">{data}</div>;
};
```

## Browser Compatibility
- **Chrome/Edge**: ✓ [Feature support]
- **Firefox**: ✓ [Feature support]
- **Safari**: ✓ [Feature support]

## Key Points
- [Essential implementation note]
- [Performance consideration if relevant]
- [Accessibility note if relevant]

## Testing (Only if requested)
```typescript
test('should work', () => {
  // Actual test code
});
```
```

### 🐛 Bug Template

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - [Accepted/Declined]

---

# ❖ [SCOPE] Bug: Issue Description

[Brief description of the bug and its impact]

⚠︎ **Key problems:**
* **User impact** - How users are affected
* **Frequency** - How often it occurs
* **Business impact** - Revenue/conversion effects
* **Technical context** - When bug started appearing

⁉ **Reasons why:**
Fixing this bug will [restore functionality], eliminate [user frustration], and prevent [business impact]

**User Value:** [What gets fixed for users]

**Business Goal:** [Why this fix matters to the business]

---

## ◆ Current Behavior
[What's happening now - the bug]

---

## ✦ Desired Behavior
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

## ✦ Success Criteria
- Bug no longer reproducible
- No regression in related features
- Works across all supported browsers

---

## ✓ Resolution Checklist

### Investigation
[ ] Identify root cause and affected areas
[ ] Document findings

### Fix Implementation
[ ] Apply fix to all instances
[ ] Add regression prevention

### Verification
[ ] Test fix across all scenarios
[ ] Validate no regressions

---

## Labels
`bug`, `[Component]`, `[Severity]`
```

### 📈 Improvement Template

```markdown
MODE: $s
TICKET TYPE: Improvement
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - [Accepted/Declined]

---

# ❖ [SCOPE] Improvement: Enhancement Description

[Brief overview of what needs improvement]

⚠︎ **Key problems/changes:**
* **Current limitation** - Performance or functionality issue
* **User pain point** - Workflow inefficiency
* **Technical debt** - Outdated implementation
* **Metric underperformance** - Not meeting targets

⁉ **Reasons why:**
By optimizing [area], we'll achieve [specific improvements] resulting in [measurable benefits] for both users and the business

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

## ✦ Success Criteria
- [Performance target met]
- [User metric improved]
- [No negative side effects]

---

## ✓ Resolution Checklist

### Analysis & Planning
[ ] Baseline measurements and target definition
[ ] Impact assessment complete

### Implementation
[ ] Apply optimizations
[ ] Update related systems
[ ] Add monitoring

### Validation
[ ] Measure improvements against targets
[ ] Verify no regressions
[ ] Document results

---

## Labels
`improvement`, `[Component]`, `performance`
```

---

## 4. ✓ RESOLUTION CHECKLIST TEMPLATES

### 🚨 DISTINCT FORMAT APPROACH

**Core Philosophy:**
- Use **✓** symbol for Resolution Checklist sections
- Use **✦** symbol for Success Criteria
- Resolution Checklist: **Checkboxes only, no bullets**
- Success Criteria: **Bullets only, no checkboxes**
- Think in **work streams**, not tasks
- Each checkbox = **meaningful deliverable**
- Sections = **logical groupings** of related work
- Focus on **WHAT gets delivered**, not HOW
- Maximum **3 items per section**

### Sizing by Mode

| Mode | Total Sections | Items per Section | Total Items |
|------|---------------|-------------------|-------------|
| **Quick ($q)** | 2-3 | 2-3 | 4-6 |
| **Standard ($s)** | 4-5 | 2-3 | 8-12 |
| **Complex ($c) - Phased** | 6-8 | 2-3 | 12-20 |
| **Complex ($c) - Child Tickets** | 5-6 | 2-3 | 10-15 |
| **Bug** | 3-4 | 2-3 | 6-10 |
| **Improvement** | 4-5 | 2-3 | 8-12 |
| **Spec ($spec)** | N/A | N/A | Key Points |

### Quick Mode Checklist
```markdown
## ✓ Resolution Checklist

### Implementation
[ ] Build core functionality
[ ] Apply styling and responsive behavior

### Verification
[ ] Test across browsers and devices
[ ] Validate against requirements
```

### Standard Mode Checklist
```markdown
## ✓ Resolution Checklist

### Foundation Work
[ ] Set up architecture and dependencies
[ ] Configure necessary integrations

### Core Development
[ ] Implement primary functionality
[ ] Add secondary features
[ ] Apply UI/UX requirements

### Testing & Validation
[ ] Complete functional testing
[ ] Verify cross-browser compatibility

### Documentation
[ ] Update technical documentation
[ ] Create user guides if needed
```

### Complex Mode Checklist (Phased)
```markdown
## ✓ Resolution Checklist

### Foundation & Architecture
[ ] Establish technical foundation
[ ] Set up infrastructure
[ ] Configure integrations

### Core Feature Development
[ ] Implement primary functionality
[ ] Build secondary features
[ ] Complete third-tier features

### Integration & Testing
[ ] Connect all components
[ ] Complete comprehensive testing
[ ] Validate against requirements

### Performance & Polish
[ ] Optimize performance
[ ] Apply UI/UX polish
[ ] Fix edge cases

### Documentation & Training
[ ] Complete technical documentation
[ ] Create user guides
[ ] Conduct team training

### Launch Preparation
[ ] Complete security audit
[ ] Finalize deployment plan
[ ] Prepare rollback strategy
```

### Complex Mode Checklist (Child Tickets)
```markdown
## ✓ Resolution Checklist

### Ticket Creation & Planning
[ ] Create all child tickets
[ ] Assign team owners
[ ] Map dependencies

### Cross-Team Coordination
[ ] Establish sync meetings
[ ] Define integration points
[ ] Align testing strategy

### Development Tracking
[ ] Monitor child ticket progress
[ ] Resolve blockers
[ ] Maintain timeline

### Integration & Testing
[ ] Complete integration testing
[ ] Validate end-to-end flows
[ ] Performance verification

### Launch Coordination
[ ] All child tickets complete
[ ] Final integration verified
[ ] Go-live checklist complete
```

### Bug Fix Checklist
```markdown
## ✓ Resolution Checklist

### Investigation
[ ] Identify root cause and affected areas
[ ] Document findings

### Fix Implementation
[ ] Apply fix to all instances
[ ] Add regression prevention

### Verification
[ ] Test fix across all scenarios
[ ] Validate no regressions
```

### Improvement Checklist
```markdown
## ✓ Resolution Checklist

### Analysis & Planning
[ ] Baseline measurements and target definition
[ ] Impact assessment complete

### Implementation
[ ] Apply optimizations
[ ] Update related systems
[ ] Add monitoring

### Validation
[ ] Measure improvements against targets
[ ] Verify no regressions

### Documentation
[ ] Document changes and results
[ ] Update team guides
```

### SMART Criteria for Checklist Items

Every item should be:
- **S**pecific - Clear deliverable
- **M**easurable - Binary completion (done/not done)
- **A**ctionable - Developer knows what to deliver
- **R**elevant - Contributes to ticket completion
- **T**ime-bound - Represents 2-8 hours minimum work

### Grouping Rules

**Group by:**
1. **System layer** (Foundation, Components, Pages)
2. **Feature area** (Authentication, Payment, Profile)
3. **Work type** (Development, Testing, Documentation)
4. **Team ownership** (Frontend, Backend, QA)

**Never group by:**
- Individual files or components
- Specific properties or methods
- Small UI elements
- Technical implementation details

---

## 5. 📝 FORMATTING STANDARDS

### Titles
- Always use `# ❖` (h1) for main ticket titles
- Include `[SCOPE]` prefix before feature name (user-specified)
- Keep titles clear and descriptive
- Spec mode: Use `# Frontend Implementation Brief: [Feature]`

### Section Dividers
Always use `---` between ALL major sections

### Text Formatting
- **Bold** for emphasis and key terms (including **◊** in sub-headings)
- *Italics* sparingly for subtle emphasis
- `Code` for technical terms
- Em dashes (—) ONLY for sub-categories under **◊** sub-headings

### Code Blocks (Spec Mode)
```markdown
```typescript
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

### Lists
- Use `-` for unordered lists (Success Criteria)
- Use `1.` for ordered lists
- Use `[ ]` for checkboxes (Resolution Checklist only)
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

### Success Criteria vs Resolution Checklist

**Success Criteria (✦):**
```markdown
## ✦ Success Criteria
- Feature works as designed on all devices
- Page loads within target time
- Majority of users complete task successfully
- Zero critical bugs in production
- Analytics tracking implemented
```

**Resolution Checklist (✓):**
```markdown
## ✓ Resolution Checklist

### Work Stream Name
[ ] Deliverable 1
[ ] Deliverable 2
[ ] Deliverable 3
```

### Complex Mode Implementation Approaches

**Phased Development Pattern:**
```markdown
## ◇ Implementation Approach

### Option A: Phased Development

#### Phase 1: Foundation (Week 1-2)
[Infrastructure and setup]

#### Phase 2: Core (Week 3-4)
[Main functionality]

#### Phase 3: Polish (Week 5-6)
[Optimization and enhancement]
```

**Child Ticket Pattern:**
```markdown
## ◇ Implementation Approach

### Option B: Child Ticket Breakdown

#### ◻︎ Infrastructure
- [ ] **[BE] Backend Setup** - APIs and database
- [ ] **[FE] UI Framework** - Component library

#### ◻︎ Features
- [ ] **[FS] Core Feature** - Main functionality
- [ ] **[FE] Dashboard** - User interface
```

### Spec Mode Concise Format

**Minimal Structure:**
```markdown
# [Feature] Implementation

## Objective
[1-2 sentences max]

## Implementation
[Working code]

## Key Points
[Bullets only if essential]
```

**Auto-Detection Examples:**
```markdown
"hide scrollbar" → CSS pattern → 0 questions
"data table" → Component pattern → 2 questions max
"state management" → Architecture → 3-4 questions
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

### Interactive Offer Tracking

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Accepted ← Track this

[When accepted, note gained insights]
INSIGHTS GAINED:
- Clarified scope as Full Stack
- Identified performance requirements
- Added accessibility needs
```

---

## Version History

- **v2.2.0**: Updated formatting - Success Criteria (bullets only), Resolution Checklist (checkboxes only)
- **v2.1.0**: Major update - Resolution Checklists now use global approach (max 3 items per section, outcome-focused)
- **v2.0.0**: Merged Complex/Epic templates, added concise Spec mode
- **v1.0.0**: Initial template standards

---

*This document is the single source of truth for all ticket templates and standards. Reference specific sections using anchors like `Ticket - Templates & Standards.md#complex-mode`.*