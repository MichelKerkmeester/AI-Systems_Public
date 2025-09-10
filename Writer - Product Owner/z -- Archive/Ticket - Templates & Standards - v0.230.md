# Ticket - Templates & Standards - v0.230

Comprehensive templates, symbols, and formatting standards for concise development tickets. Single source of truth for ticket structure.

## Table of Contents

1. [📋 ARTIFACT STANDARDS](#1--artifact-standards)
2. [📤 SYMBOL REFERENCE](#2--symbol-reference)
3. [📝 BASE TEMPLATES BY MODE](#3--base-templates-by-mode)
4. [✓ RESOLUTION CHECKLIST TEMPLATES](#4--resolution-checklist-templates)
5. [📏 FORMATTING STANDARDS](#5--formatting-standards)
6. [🎯 SECTION TEMPLATES](#6--section-templates)

---

## 1. 📋 ARTIFACT STANDARDS

### Critical Requirements

**🚨 CRITICAL:** Always use `text/markdown` artifact type!

### Mandatory Header

Every ticket artifact MUST start with:

```markdown
MODE: [mode used]
TICKET TYPE: [Feature/Bug/Improvement/Complex/Implementation Brief]
MCP USED: [Sequential Thinking/Cascade Thinking/Figma/Multiple/None Available]
INTERACTIVE OFFERED: [Yes/No/N/A]
```

### Artifact Title vs Body

- **Artifact Title**: `[SCOPE] Feature Name`
- **First Body Heading**: `# ■ About`

---

## 2. 📤 SYMBOL REFERENCE

### Primary Symbols (Required)
- **■** - "About" heading and major sections
- **◇** - Requirements and process sections
- **◊** - Sub-headings within sections (bold)
- **→** - Designs & References
- **✦** - Success criteria (bullets only, NO checkboxes)
- **✓** - Resolution Checklist (checkboxes only, NO bullets)
- **⊗** - Dependencies
- **⚠** - Risks and notices
- **⚠️** - Key problems in descriptions
- **≈** - Reasons why in descriptions

### Secondary Symbols
- **—** - Sub-categories under **◊**
- **•** - Bullet points
- **◆** - Alternative sections
- **◈** - Document headers

### Usage Rules
- ✦ EXCLUSIVELY for Success Criteria (bullets)
- ✓ EXCLUSIVELY for Resolution Checklist (checkboxes)
- Never mix these formats

### Hierarchy Example
```markdown
# ■ About
## ◇ Requirements
**◊** Component
— Category
• Requirement

## ✦ Success Criteria
- Metric

## ✓ Resolution Checklist
### Stream
[ ] Outcome
```

---

## 3. 📝 BASE TEMPLATES BY MODE

### 🚀 Quick Mode ($q) Template

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A

---

# ■ About

[Brief context sentence]

⚠️ **Key problems:**
* **Issue** - Description
* **Problem** - Impact
* **Gap** - Current state

≈ **Reasons why:**
[Solution and impact statement]

**User Value:** [One-line benefit]

**Business Goal:** [Specific metric]

---

## ◇ Requirements
- Requirement 1
- Requirement 2
- Requirement 3

---

## ✦ Success Criteria
- Criterion 1
- Criterion 2
- Criterion 3

---

## ✓ Resolution Checklist

### Implementation
[ ] Build core functionality
[ ] Apply styling

### Verification
[ ] Test across devices
[ ] Validate requirements

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

# ■ About

[Context and current situation]

⚠️ **Key problems:**
* **Problem 1** - Description
* **Problem 2** - User impact
* **Problem 3** - Technical gap

≈ **Reasons why:**
By implementing [solution], we'll achieve [benefits] improving [metrics]

**User Value:** [User benefit]

**Business Goal:** [Measurable outcome]

---

## ◇ Requirements

**◊** [Component 1]
— Category
• Requirement
• Edge case
— Another Category
• Requirement

**◊** [Component 2]
— Category
• Requirements

---

## → Designs & References
- [Figma - Flow](link)
- [API Docs](link)

**Notice:** [Important note]

---

## ✦ Success Criteria
- Criterion 1
- Performance metric
- User metric
- Business metric

---

## ✓ Resolution Checklist

### Foundation
[ ] Set up architecture
[ ] Configure integrations

### Development
[ ] Implement primary features
[ ] Add secondary features

### Testing
[ ] Complete functional testing
[ ] Verify compatibility

### Documentation
[ ] Update technical docs
[ ] Create user guides

---

## ⊗ Dependencies
- Requires: [API] (#1234)
- Blocks: [Feature] (#1235)

---

## Labels
`[Component]`, `[Area]`, `feature`
```

### 🔧 Complex Mode ($c) Template

```markdown
MODE: $c
TICKET TYPE: Complex
MCP USED: Cascade Thinking
INTERACTIVE OFFERED: Yes - [Accepted/Declined]

---

# ■ About

[Strategic overview and importance]

⚠️ **Key problems:**
* **Limitation** - Business impact
* **Technical debt** - Scaling issues
* **Competitive gap** - Market position
* **User friction** - Experience problems

≈ **Reasons why:**
This implementation transforms [system] through [approach], positioning us [advantage] while [benefits]. Ensures [risk mitigation] with improvements in [metrics].

**User Value:** [High-level outcome]

**Business Goal:** [Strategic objective]

---

[[*TOC*]]

---

## → Designs & References

### ◻️ User Flows
- [Figma - Journey](link)
- [Figma - Edge Cases](link)

### ◻️ Technical
- [Architecture](link)
- [API Spec](link)

---

## ◇ Implementation Approach

### Option A: Phased Development

#### Phase 1: Foundation (Week 1-2)

**◊** Infrastructure
— Backend
• API endpoints
• Database schema
• Authentication
— Frontend
• Components
• State management
• Routing

#### Phase 2: Core (Week 3-4)

**◊** Features
— Interface
• Workflow screens
• Interactive elements
— Functionality
• Business logic
• API integration
• Real-time updates

#### Phase 3: Polish (Week 5-6)

**◊** Optimization
— Performance
• Caching
• Query optimization
— Experience
• Animations
• Accessibility

### Option B: Child Tickets

#### ◻️ Infrastructure
- [ ] **[BE] APIs** (#child-1) - Services
- [ ] **[FE] Components** (#child-2) - UI library
- [ ] **[DevOps] Setup** (#child-3) - Deployment

#### ◻️ Features
- [ ] **[FS] User Flow** (#child-4) - Complete journey
- [ ] **[FE] Dashboard** (#child-5) - Analytics
- [ ] **[BE] Integration** (#child-6) - Third-party

---

## ✦ Success Criteria
- High-level metric
- Performance benchmark
- Adoption metric
- Business impact
- Quality metric

---

## ✓ Resolution Checklist

### Foundation
[ ] Establish technical base
[ ] Set up infrastructure
[ ] Configure integrations

### Development
[ ] Implement primary features
[ ] Build secondary features

### Integration
[ ] Connect components
[ ] Complete testing

### Performance
[ ] Optimize performance
[ ] Apply polish

### Documentation
[ ] Complete technical docs
[ ] Create user guides

### Launch
[ ] Security audit
[ ] Deployment plan

---

## ⊗ Dependencies
- Requires: [Dependency 1] (#3001)
- Requires: [Dependency 2] (#3002)
- Blocks: [Future] (#3100)

---

## ⚠ Risks
- **Risk 1:** Description and mitigation
- **Risk 2:** Description and mitigation

---

## Labels
`[Component]`, `complex`, `[priority]`
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
[1-2 sentences max]

## Implementation
```typescript
// Working code
const Component = ({ data }: Props) => {
  return <div>{data}</div>;
};
```

## Browser Compatibility
- **Chrome/Edge**: ✓
- **Firefox**: ✓
- **Safari**: ✓

## Key Points
- Essential note
- Performance consideration
```

### 🐛 Bug Template

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - [Accepted/Declined]

---

# ■ About

[Bug description and impact]

⚠️ **Key problems:**
* **User impact** - How affected
* **Frequency** - How often
* **Business impact** - Revenue/conversion

≈ **Reasons why:**
Fixing this restores [functionality], eliminates [frustration], prevents [impact]

**User Value:** [What gets fixed]

**Business Goal:** [Why fix matters]

---

## ◆ Current Behavior
[What's happening - the bug]

---

## ✦ Desired Behavior
[What should happen]

---

## ◈ Steps to Reproduce
1. Step 1
2. Step 2
3. Observe bug

---

## → Evidence
- [Screenshot](link)
- [Logs](link)

---

## ✦ Success Criteria
- Bug not reproducible
- No regressions
- Works across browsers

---

## ✓ Resolution Checklist

### Investigation
[ ] Identify root cause
[ ] Document findings

### Fix
[ ] Apply fix
[ ] Add prevention

### Verification
[ ] Test scenarios
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

# ■ About

[What needs improvement]

⚠️ **Key problems:**
* **Limitation** - Performance issue
* **Pain point** - Workflow inefficiency
* **Technical debt** - Outdated implementation

≈ **Reasons why:**
Optimizing [area] achieves [improvements] resulting in [benefits]

**User Value:** [How improves experience]

**Business Goal:** [Improvement target]

---

## ◈ Current State
- Current metric
- Pain points
- Limitations

---

## ◆ Target State
- Improved metric
- Benefits
- New capabilities

---

## ◇ Requirements

**◊** Performance
— Backend
• Query optimization
• Caching
— Frontend
• Bundle reduction
• Lazy loading

**◊** Experience
— Visual
• Loading states
• Transitions
— Functionality
• Improved workflows
• Error handling

---

## ✦ Success Criteria
- Performance target met
- User metric improved
- No side effects

---

## ✓ Resolution Checklist

### Analysis
[ ] Baseline measurements
[ ] Impact assessment

### Implementation
[ ] Apply optimizations
[ ] Update systems

### Validation
[ ] Measure improvements
[ ] Verify no regressions

---

## Labels
`improvement`, `[Component]`, `performance`
```

---

## 4. ✓ RESOLUTION CHECKLIST TEMPLATES

### 🚨 CORE PHILOSOPHY

- **✓** symbol for Resolution Checklist
- **✦** symbol for Success Criteria
- Resolution: **Checkboxes only, NO bullets**
- Success: **Bullets only, NO checkboxes**
- Think **work streams**, not tasks
- Each checkbox = **meaningful deliverable**
- Maximum **3 items per section**
- Focus on **WHAT**, not HOW

### Sizing by Mode

| Mode | Sections | Items/Section | Total |
|------|----------|---------------|-------|
| **Quick** | 2-3 | 2-3 | 4-6 |
| **Standard** | 4-5 | 2-3 | 8-12 |
| **Complex - Phased** | 6-8 | 2-3 | 12-20 |
| **Complex - Child** | 5-6 | 2-3 | 10-15 |
| **Bug** | 3-4 | 2-3 | 6-10 |
| **Improvement** | 4-5 | 2-3 | 8-12 |

### Templates by Mode

#### Quick Mode
```markdown
## ✓ Resolution Checklist

### Implementation
[ ] Build functionality
[ ] Apply styling

### Verification
[ ] Test across devices
[ ] Validate requirements
```

#### Standard Mode
```markdown
## ✓ Resolution Checklist

### Foundation
[ ] Set up architecture
[ ] Configure integrations

### Development
[ ] Implement primary features
[ ] Add secondary features

### Testing
[ ] Complete functional testing
[ ] Verify compatibility

### Documentation
[ ] Update technical docs
[ ] Create user guides
```

#### Complex Mode (Phased)
```markdown
## ✓ Resolution Checklist

### Foundation
[ ] Establish technical base
[ ] Set up infrastructure

### Development
[ ] Implement primary features
[ ] Build secondary features

### Integration
[ ] Connect components
[ ] Complete testing

### Performance
[ ] Optimize performance
[ ] Apply polish

### Documentation
[ ] Complete docs
[ ] Create guides

### Launch
[ ] Security audit
[ ] Deployment plan
```

### SMART Criteria

Every item should be:
- **S**pecific - Clear deliverable
- **M**easurable - Binary completion
- **A**ctionable - Developer knows what
- **R**elevant - Contributes to completion
- **T**ime-bound - 2-8 hours minimum

---

## 5. 📏 FORMATTING STANDARDS

### Titles
- Artifact title: `[SCOPE] Feature Name`
- First body heading: `# ■ About`
- Keep clear and descriptive
- Spec mode: `# Frontend Implementation Brief: [Feature]`

### Section Dividers
Use `---` between ALL major sections

### Text Formatting
- **Bold** for emphasis and **◊** sub-headings
- *Italics* sparingly
- `Code` for technical terms
- Em dashes (—) ONLY for sub-categories under **◊**

### Code Blocks (Spec Mode)
```markdown
```typescript
// Specify language
const example = "code";
```
```

### Links
```markdown
[Descriptive Text](url)
[Figma - Component](figma-url)
[API Documentation](api-url)
```

### Lists
- `-` for unordered (Success Criteria)
- `1.` for ordered
- `[ ]` for checkboxes (Resolution only)
- `•` for sub-category points

### Notices
```markdown
**Notice:** Important information
```

---

## 6. 🎯 SECTION TEMPLATES

### Description Template

**Structure:**
1. Brief intro sentence
2. **⚠️ Key problems:** bulleted list (3-4 max)
3. **≈ Reasons why:** impact statement

**Example:**
```markdown
Current search functionality fails user needs causing business impact.

⚠️ **Key problems:**
* **Poor relevance** - Results miss intent
* **No filtering** - Can't narrow results
* **Slow performance** - 3-5 second searches

≈ **Reasons why:**
Advanced search with filters and optimization reduces abandonment and increases conversion.
```

### Success vs Resolution

**Success Criteria (✦):**
```markdown
## ✦ Success Criteria
- Feature works on all devices
- Page loads within target
- Users complete task successfully
- Zero critical bugs
```

**Resolution Checklist (✓):**
```markdown
## ✓ Resolution Checklist

### Work Stream
[ ] Deliverable 1
[ ] Deliverable 2
```

### Complex Approaches

**Phased Pattern:**
```markdown
## ◇ Implementation Approach

### Option A: Phased Development

#### Phase 1: Foundation (Week 1-2)
[Infrastructure]

#### Phase 2: Core (Week 3-4)
[Main functionality]

#### Phase 3: Polish (Week 5-6)
[Optimization]
```

**Child Ticket Pattern:**
```markdown
### Option B: Child Tickets

#### ◻️ Infrastructure
- [ ] **[BE] Backend** - APIs
- [ ] **[FE] UI** - Components

#### ◻️ Features
- [ ] **[FS] Core** - Main functionality
```

### Requirements Pattern

**Simple:**
```markdown
## ◇ Requirements
- Requirement 1
- Requirement 2
- Requirement 3
```

**Complex with Sub-headings:**
```markdown
## ◇ Requirements

**◊** Interface
— Components
• Updates
• Changes
— Interactions
• Handlers
• States

**◊** Backend
— API
• Endpoints
• Responses
— Database
• Schema
• Migrations
```

---

## Version History

- **v0.420**: First heading now "About", 20% more concise, reduced examples
- **v0.410**: Updated formatting distinctions
- **v0.400**: Merged Complex/Epic, added concise Spec

---

*Single source of truth for all ticket templates. Reference sections using anchors like `Templates & Standards.md#complex-mode`.*