# Ticket - Artifact Standards & Templates

Comprehensive templates and standards for all ticket artifacts. This is the authoritative source for ticket structure and formatting.

## Table of Contents

1. [📋 MANDATORY ARTIFACT STRUCTURE](#1--mandatory-artifact-structure)
2. [🎯 MODE-SPECIFIC TEMPLATES](#2--mode-specific-templates)
3. [✅ RESOLUTION CHECKLIST TEMPLATES](#3--resolution-checklist-templates)
4. [📝 SECTION TEMPLATES](#4--section-templates)
5. [🔤 SYMBOL USAGE GUIDE](#5--symbol-usage-guide)
6. [⚡ QUICK TEMPLATES](#6--quick-templates)

---

## 1. 📋 MANDATORY ARTIFACT STRUCTURE

### Base Template (ALL MODES)

```markdown
MODE: [$interactive] (default) or [$q/$s/$c/$e] (if explicitly requested)
TICKET TYPE: [Feature/Bug/Improvement/Epic]
MCP USED: [Sequential Thinking/Cascade Thinking/Figma/Multiple/None Available]
FIGMA INTEGRATED: [Yes/No] (if applicable)

---

### ❖ [Title with symbol]

**User Value:** [Clear user benefit]

**Business Goal:** [Measurable business outcome]

---

[Mode-specific sections]

---

## ✓ Success Criteria
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]
- [ ] [etc.]

---

## ✓ Resolution Checklist

### [Category 1]
- [ ] [Specific actionable task]
- [ ] [Another actionable task]

### [Category 2]
- [ ] [More actionable items]
- [ ] [Final verification step]

---

## ⊗ Dependencies
- Requires: [Dependency] (#ticket)
- Blocks: [Blocked item] (#ticket)
```

---

## 2. 🎯 MODE-SPECIFIC TEMPLATES

### 🚀 Quick Mode ($q) Template

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking

---

### ❖ [Feature Name]

**User Value:** [One-line user benefit]

**Business Goal:** [Specific metric improvement]

---

## ◇ Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

---

## → Designs & References
- [Figma - Design](link)

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
```

### 📋 Standard Mode ($s) Template

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking

---

### ❖ [Feature Name]

**User Value:** [Detailed user benefit]

**Business Goal:** [Measurable business outcome with current metrics]

---

## ◇ Requirements
- **[Category 1]**
  - [Detailed requirement]
  - [Another requirement]
- **[Category 2]**
  - [More requirements]
  - [Edge case handling]

---

## → Designs & References

### ◻︎ Design Links
- [Figma - Main Flow](link)
- [Figma - Mobile Views](link)

### ◻︎ Technical References
- [API Documentation](link)
- [Related Ticket](link)

**Notice:** [Important design note]

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
- [ ] [State management]

### Testing & QA
- [ ] [Unit tests]
- [ ] [Integration tests]
- [ ] [Cross-browser testing]
- [ ] [Performance testing]

### Documentation
- [ ] [Code documentation]
- [ ] [API updates]
- [ ] [User guide updates]

---

## ⊗ Dependencies
- Requires: [Backend API] (#1234)
- Requires: [Design approval] (#1235)
- Blocks: [Next feature] (#1236)
```

### 🔧 Complex Mode ($c) Template

```markdown
MODE: $c
TICKET TYPE: Feature
MCP USED: Cascade Thinking

---

### ❖ [Complex Feature Name]

---

# ⌘ About

[2-3 paragraphs explaining the context, problem, and strategic importance]

**User Value:** [Comprehensive user benefit]

**Business Goal:** [Strategic business outcome with metrics]

---

[[*TOC*]]

---

## → Designs & References

### ◻︎ User Flows
- [Figma - Complete User Journey](link)
- [Figma - Edge Cases](link)

### ◻︎ Technical Architecture
- [Architecture Diagram](link)
- [API Specification](link)

**Notice:** [Critical implementation notes]

---

## ◇ Phase 1: [Foundation] (Timeline)
- [Foundation element 1]
- [Foundation element 2]
- [Basic functionality]
- [Initial testing]

---

## ◇ Phase 2: [Core Features] (Timeline)
- [Main feature 1]
- [Main feature 2]
- [Integration points]
- [Performance optimization]

---

## ◇ Phase 3: [Enhancement] (Timeline)
- [Advanced features]
- [Polish and refinement]
- [Final testing]
- [Documentation]

---

## ✓ Success Criteria
- [ ] [High-level metric 1]
- [ ] [High-level metric 2]
- [ ] [Performance benchmark]
- [ ] [User adoption metric]
- [ ] [Business impact metric]

---

## ✓ Resolution Checklist

### Phase 1: Foundation
- [ ] [Infrastructure setup]
- [ ] [Basic component creation]
- [ ] [Initial API integration]
- [ ] [Foundation testing]
- [ ] [Phase 1 demo ready]

### Phase 2: Core Features
- [ ] [Feature 1 implementation]
- [ ] [Feature 2 implementation]
- [ ] [Integration complete]
- [ ] [Performance optimization]
- [ ] [Phase 2 review]

### Phase 3: Enhancement
- [ ] [Advanced features added]
- [ ] [UI/UX polish]
- [ ] [Final testing pass]
- [ ] [Documentation complete]
- [ ] [Production ready]

### Launch Preparation
- [ ] [Security review]
- [ ] [Performance benchmarks met]
- [ ] [Monitoring configured]
- [ ] [Rollback plan ready]
- [ ] [Team handoff complete]

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
```

### 🚀 Epic Mode ($e) Template

```markdown
MODE: $e
TICKET TYPE: Epic
MCP USED: Cascade Thinking

---

### ❖ Epic: [Epic Title]

**User Value:** [High-level user outcome]

**Business Goal:** [Strategic business objective]

---

## ⌘ Overview
[1-2 paragraphs describing the epic scope and importance]

---

## ✓ Success Metrics
- [ ] [Epic-level metric 1]
- [ ] [Epic-level metric 2]
- [ ] [Epic-level metric 3]

---

## ◇ Child Tickets

### ◻︎ Phase 1: [Foundation Phase]
- [ ] **[Ticket 1]** - [Brief description]
- [ ] **[Ticket 2]** - [Brief description]
- [ ] **[Ticket 3]** - [Brief description]

### ◻︎ Phase 2: [Core Phase]
- [ ] **[Ticket 4]** - [Brief description]
- [ ] **[Ticket 5]** - [Brief description]
- [ ] **[Ticket 6]** - [Brief description]

### ◻︎ Phase 3: [Enhancement Phase]
- [ ] **[Ticket 7]** - [Brief description]
- [ ] **[Ticket 8]** - [Brief description]
- [ ] **[Ticket 9]** - [Brief description]

---

## ✓ Resolution Checklist

### Epic Coordination
- [ ] All child tickets created
- [ ] Team assignments complete
- [ ] Timeline established
- [ ] Success metrics dashboard created

### Cross-Cutting Concerns
- [ ] Design consistency verified
- [ ] API contracts finalized
- [ ] Security review scheduled
- [ ] Performance targets set

### Launch Readiness
- [ ] Beta testing complete
- [ ] Documentation ready
- [ ] Support team trained
- [ ] Marketing materials prepared
- [ ] Go-live plan approved

---

## ⊗ Dependencies
- Requires: [Strategic prerequisite] (#5001)
- Requires: [Infrastructure upgrade] (#5002)

---

## ⌘ Timeline
[Total timeline with phase breakdowns]
```

---

## 3. ✅ RESOLUTION CHECKLIST TEMPLATES

### By Mode Complexity

| Mode | Items | Structure | Example Categories |
|------|-------|-----------|-------------------|
| **Quick ($q)** | 3-5 | Single list | Core tasks only |
| **Standard ($s)** | 8-15 | 2-3 categories | Implementation, Testing, Docs |
| **Complex ($c)** | 15-30 | Phase-based | Phase 1, Phase 2, Phase 3, Launch |
| **Epic ($e)** | 10-20 | Coordination | Planning, Cross-team, Launch |

### By Ticket Type

#### Feature Checklist Template
```markdown
## ✓ Resolution Checklist

### Implementation
- [ ] Build UI components per design
- [ ] Implement business logic
- [ ] Connect to backend APIs
- [ ] Add error handling

### Testing
- [ ] Write unit tests
- [ ] Complete integration testing
- [ ] Test edge cases
- [ ] Verify on all devices

### Polish
- [ ] Optimize performance
- [ ] Add loading states
- [ ] Implement analytics
- [ ] Update documentation
```

#### Bug Fix Checklist Template
```markdown
## ✓ Resolution Checklist

### Investigation
- [ ] Reproduce the bug consistently
- [ ] Identify root cause
- [ ] Document affected code paths

### Fix Implementation
- [ ] Implement the fix
- [ ] Verify bug is resolved
- [ ] Check for side effects
- [ ] Add regression test

### Verification
- [ ] Test in all environments
- [ ] Verify on affected devices
- [ ] Confirm with reported scenarios
- [ ] Deploy and monitor
```

#### Improvement Checklist Template
```markdown
## ✓ Resolution Checklist

### Analysis
- [ ] Measure current performance
- [ ] Identify bottlenecks
- [ ] Define target metrics

### Implementation
- [ ] Apply optimizations
- [ ] Refactor as needed
- [ ] Update related systems

### Validation
- [ ] Measure improved performance
- [ ] Compare against targets
- [ ] Test under load
- [ ] Document improvements
```

---

## 4. 📝 SECTION TEMPLATES

### Requirements Section Patterns

#### Simple Requirements
```markdown
## ◇ Requirements
- [Clear requirement 1]
- [Clear requirement 2]
- [Clear requirement 3]
```

#### Categorized Requirements
```markdown
## ◇ Requirements

**User Interface**
- [UI requirement 1]
- [UI requirement 2]

**Functionality**
- [Functional requirement 1]
- [Functional requirement 2]

**Performance**
- [Performance requirement 1]
- [Performance requirement 2]
```

#### Flow-Based Requirements
```markdown
## ◇ Requirements
- **User action** → Expected outcome
- **System event** → System response
- **Error occurs** → Error handling
```

### Success Criteria Patterns

#### Basic Success Criteria
```markdown
## ✓ Success Criteria
- [ ] Feature works as designed
- [ ] No regressions introduced
- [ ] Meets performance targets
```

#### Detailed Success Criteria
```markdown
## ✓ Success Criteria
- [ ] [Specific functionality metric]
- [ ] [Performance benchmark: <2s load]
- [ ] [User adoption: 80% usage]
- [ ] [Business metric: 25% improvement]
- [ ] [Quality metric: 0 critical bugs]
```

---

## 5. 🔤 SYMBOL USAGE GUIDE

### Primary Symbols (Required in all tickets)
- **❖** - Title and major features
- **◇** - Requirements and processes
- **→** - Designs and references
- **✓** - Success criteria AND Resolution Checklist
- **⊗** - Dependencies

### Secondary Symbols (Use as needed)
- **⌘** - About/context sections
- **◆** - Alternative major sections
- **◈** - Document subsections
- **◻︎** - List items within sections
- **▸** - Progressive disclosure
- **⚠** - Risks and warnings

### Symbol Hierarchy Example
```markdown
### ❖ Main Feature
## ◇ Requirements
### ◻︎ Component A
- Requirement 1
- Requirement 2
### ◻︎ Component B
- Requirement 3
- Requirement 4
## → Designs
### ◻︎ Figma Files
### ◻︎ Technical Docs
## ✓ Success Criteria
## ✓ Resolution Checklist
```

---

## 6. ⚡ QUICK TEMPLATES

### Minimal Feature Template
```markdown
### ❖ [Feature]
**User Value:** [Benefit]
**Business Goal:** [Metric]
## ◇ Requirements
- [Req 1]
- [Req 2]
## ✓ Success Criteria
- [ ] [Success 1]
- [ ] [Success 2]
## ✓ Resolution Checklist
- [ ] Build feature
- [ ] Test feature
- [ ] Deploy feature
```

### Quick Bug Template
```markdown
### ❖ Bug: [Issue]
**User Value:** [What gets fixed]
**Business Goal:** [Why it matters]
## ◆ Current Behavior
[What's broken]
## ✓ Expected Behavior
[What should happen]
## ✓ Resolution Checklist
- [ ] Fix the bug
- [ ] Test the fix
- [ ] Verify no regressions
```

---

**Remember:** These templates are the standard. Adapt content to fit the specific needs of each ticket while maintaining the required structure and symbols.