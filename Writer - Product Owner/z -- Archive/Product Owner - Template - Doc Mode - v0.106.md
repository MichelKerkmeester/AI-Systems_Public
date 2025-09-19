# Product Owner – Template: Doc Mode – v0.106

## 📋 TABLE OF CONTENTS

1. [📚 DOC MODE OVERVIEW](#1-📚-doc-mode-overview)
2. [📄 FEATURE DOCUMENTATION TEMPLATE](#2-📄-feature-documentation-template)
3. [🏗️ SYSTEM OVERVIEW TEMPLATE](#3-🏗️-system-overview-template)
4. [🔄 PATTERN/FLOW TEMPLATE](#4-🔄-patternflow-template)
5. [📊 PERFORMANCE METRICS TEMPLATE](#5-📊-performance-metrics-template)
6. [🗺️ USER JOURNEY TEMPLATE](#6-🗺️-user-journey-template)
7. [📦 COMPONENT LIBRARY TEMPLATE](#7-📦-component-library-template)
8. [📢 RELEASE NOTES TEMPLATE](#8-📢-release-notes-template)
9. [🌳 ARCHITECTURE DECISION TEMPLATE](#9-🌳-architecture-decision-template)
10. [🔍 TROUBLESHOOTING GUIDE TEMPLATE](#10-🔍-troubleshooting-guide-template)
11. [🎨 FORMATTING STANDARDS](#11-🎨-formatting-standards)

---

## 1. 📚 DOC MODE OVERVIEW

### Command: `$doc`

* **Purpose:** Create product documentation using the standardized templates below.
* **Output:** Always returned as a single artifact.
* **Thinking Rounds:** 6–10 recommended.
* **Tip:** Choose the template that matches the audience and lifecycle stage (discovery → delivery → support).

---

## 2. 📄 FEATURE DOCUMENTATION TEMPLATE

- **What it is:** A complete spec for one feature: context, scope, logic, and performance tracking.
- **When to use:** New feature proposals, refinement of existing features, handoff to design/engineering.
- **Best practices – Do:** Keep scope crisp, show value by audience, include measurable targets.
- **Best practices – Don't:** Mix multiple features, bury decisions, or omit success metrics.

```markdown
# [Feature Name]

**Parent:** [Parent Feature] | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
[High-level description of what this feature does and why it matters. Include the business value, creator value, and how it fits into the larger system.]

[Second paragraph with more context about the problem it solves or opportunity it creates.]
---
## → Designs & References
---
Here's where you'll find all the [feature]-related designs:
---
*   [Flow | [Feature Name]](figma-link)
*   [Page | [Feature Name]](figma-link)
*   [Modal | [Feature Name]](figma-link)
*   [Component | [Feature Name]](figma-link)
---
## ◻︎ Features
---
1. **[Key Feature 1]**
---
[Description of what this enables and why it matters]
---
2. **[Key Feature 2]**
---
[Description of what this enables and why it matters]
---
3. **[Key Feature 3]**
---
[Description of what this enables and why it matters]
---
4. **[Key Feature 4]**
[Description of what this enables and why it matters]
---
## ◻︎ Overview
---
[Brief technical overview of how the feature works, including key numbers and specifications]
---
Features:
*   **[X] [Components/Options]** [description]
*   **[Y] [States/Modes]** [description]
*   **[Smart/Automatic behavior]** [description]
*   **[Real-time updates]** [description]
---

| [Category] | [Default] | Business Impact | Creator Value |
| ---| ---| ---| --- |
| **[Type 1]** | [Setting] | [Impact description] | [Value description] |
| **[Type 2]** | [Setting] | [Impact description] | [Value description] |
| **[Type 3]** | [Setting] | [Impact description] | [Value description] |

# ❖ [Main Section Name]
---
## ◻︎ [Subsection 1]
---
[Introduction to this subsection]
---
### ◊ [Component/Option Name]
---
[Description of how this works]
---
#### —— [Detail Level]
---
*   [Bullet point detail]
*   [Bullet point detail]
*   [Bullet point detail]
---
### ◊ Logic
---
[Description of the business logic or rules]
---
1. **[Rule 1]**
    *   [Sub-detail]
    *   [Sub-detail]
2. **[Rule 2]**
    *   [Sub-detail]
    *   [Sub-detail]
---
### ◊ Algorithm
---
[High-level description of how the algorithm works]
---
**[Factor 1]** → Weight: [X]%
_[What this measures]_
---
*   **[Sub-factor]** ([Y]%)
    *   [Condition]: [Weight] weight
    *   [Condition]: [Weight] weight
    *   [Condition]: [Weight] weight
---
*   **[Sub-factor]** ([Y]%)
    *   [Condition]: [Weight] weight
    *   [Condition]: [Weight] weight
---
**[Factor 2]** → Weight: [X]%
_[What this measures]_
---
*   **[Sub-factor]** ([Y]%)
    *   [Condition]: [Weight] weight
    *   [Condition]: [Weight] weight
---


# ❖ Performance Tracking
---
We track metrics throughout the [feature] journey to [primary goal], [secondary goal], and [business goal].
---
**Notice:** Check the documentation here for more details on: Private ([link])
---
## ◻︎ Target Metrics Framework
---
This framework helps us measure [what we're measuring] so we can [why we're measuring]. But metrics are only useful if we act on them - here's what we actually do.
---
### ◊ **Engagement**
---
#### **—— Targets**
---
*   [Metric 1]
*   [Metric 2]
*   [Metric 3]
*   [Metric 4]
---
#### **—— Thresholds & Actions**
---
1. **[Metric] drops** = below [X]%
**Situation:** [What this indicates]
**Action:** [Specific action] → [Follow-up action] → [Test & iterate]
---
2. **[Metric] rises** = above [X]%
**Situation:** [What this indicates]
**Action:** [Specific action] → [Follow-up action] → [Test & iterate]
---
### ◊ **Conversion**
---
#### **—— Targets**
---
*   [Step] → [Step] rate
*   [Action] → [Result] rate
*   [Feature] → [Outcome] rate
---
#### **—— Thresholds & Actions**
---
1. **[Conversion metric]** = below [X]%
---
**Situation:** [Problem description]
**Action:** [Solution approach] → [Implementation] → [Measurement]
---
### ◊ **Retention**
---
#### **—— Targets**
---
*   [X]-day retention
*   [Behavior] persistence
*   [Feature] correlation with platform retention
---
#### **—— Thresholds & Actions**
---
1. **[Retention metric] drops** = below [X]%
---
**Situation:** [What this means for the business]
**Action:** [Intervention strategy] → [Tactical implementation] → [Success measurement]
---
```

---

## 3. 🏗️ SYSTEM OVERVIEW TEMPLATE

- **What it is:** An executive-to-technical overview of an entire system (collection of features and services).
- **When to use:** Platform overviews, stakeholder onboarding, pre-architecture reviews.
- **Best practices – Do:** Explain principles, components, and value per audience; link deep docs.
- **Best practices – Don't:** List every detail; avoid feature-level noise here.

```markdown
# [System Name]

**Parent:** [Parent System] | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
[Opening statement about the transformation or reimagining this system represents.]

[Explanation of the multi-stakeholder value proposition - why this is a win-win-win]
*   **[Stakeholder 1]** [benefit description]
*   **[Stakeholder 2]** [benefit description]
*   **Business** [benefit description]

[Closing statement about the system's true nature beyond its surface function]
---
### → References
---
1. **Epic:** Private ([link])
2. **Roadmap:** Private ([link])
3. **Documentation:** Private ([link])
---


# ❖ How It Works
---
The [system] operates on [X] principles, each delivering value to [stakeholders]:
---
1. **[Principle 1 Name]**

[Description of how this principle works, including any hidden mechanics or dual purposes]

**Value by audience**
*   **[Stakeholder 1]:** [Specific value delivered]
*   **[Stakeholder 2]:** [Specific value delivered]
*   **Business:** [Strategic value captured]

---
2. **[Principle 2 Name]**
---

[Description of how this principle works and why it matters]

---
**Value by audience**
*   **[Stakeholder 1]:** [Specific value delivered]
*   **[Stakeholder 2]:** [Specific value delivered]
*   **Business:** [Strategic value captured]
---


# ❖ [Core Component 1]
---
[High-level description of this component's role in the system]
---
**Notice:** Check the documentation here for more details on: Private ([link])
---
## ◻︎ Features
---
1. **[Feature Name]**
---
[What this enables and why it matters]
---
2. **[Feature Name]**
---
[What this enables and why it matters]
---
## ◻︎ Overview
---
[Technical overview with key specifications]

| [Category] | [Property] | [Impact/Value] |
| ---| ---| --- |
| **[Type]** | [Specification] | [Description] |
| **[Type]** | [Specification] | [Description] |
| **[Type]** | [Specification] | [Description] |



# ❖ Performance Tracking
---
[Statement about what metrics reveal and why they matter for the business]
---
**Notice:** Check the documentation here for more details on: Private ([link])
---
## ◻︎ Overview
---
1. **[Tracking principle 1]**
---
[What this measures and why]
---
2. **[Tracking principle 2]**
---
[What this reveals about system health]
---
3. **[Tracking principle 3]**
---
[How this drives decision-making]
---
```

---

## 4. 🔄 PATTERN/FLOW TEMPLATE

- **What it is:** Documentation for reusable UI/behavior patterns and flows that span features.
- **When to use:** Search, onboarding, recommendation loops, retention patterns, etc.
- **Best practices – Do:** Separate fixed vs dynamic elements, show relationships, add algorithm notes.
- **Best practices – Don't:** Hard-code business rules that belong in the feature docs.

```markdown
# [Pattern/Flow Name]

**Parent:** [Parent Feature] | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
[Description of what patterns/flows are and how they create value]
---
## → Designs & References
---
Here's where you'll find all the [pattern]-related designs:
---
*   [Flow | [Name]](figma-link)
*   [Page | [Name]](figma-link)
*   [Component | [Name]](figma-link)
---
## ◻︎ Features
---
1. **[Coordination Feature]**
---
[How patterns work together]
---
2. **[Engagement Feature]**
---
[How patterns create loops]
---
3. **[Adaptation Feature]**
---
[How patterns personalize]
---
## ◻︎ Overview
---
[Number] main patterns power the [experience]:

| Pattern | Type | What it does |
| ---| ---| --- |
| **[Pattern 1]** | [Type] | [Description] |
| **[Pattern 2]** | [Type] | [Description] |
| **[Pattern 3]** | [Type] | [Description] |

## ◻︎ Relationships
---
[How patterns connect and enhance each other]
---
*   **[Pattern A]** [action] → **[Pattern B]** [result]
*   **[Pattern C]** [action] → **[Pattern D]** [result]
*   [How everything works together]
---


# ❖ [Pattern Name]
---
[Description of this specific pattern and its purpose]

[Additional context about business value or user benefit]
---
## ◻︎ Pattern
---
### ◊ **Fixed**
[Elements that always appear]
---
1. **[Component Name]**

[Description of what this shows/does]

---
2. **[Component Name]**

[Description of what this shows/does]

---
3. **Repeat** 🔄
---
### ◊ **Dynamic**
[Elements that change or rotate]
---
1. **[Component Name]**

[Description and variation logic]

---
2. **[Component Name]**

[Description and variation logic]

---
## ◻︎ Expansion States
---
### ◊ **[State Name]**
---
[Description of when and why this state appears]
---
#### —— Logic
---
1. [Step 1 of the flow]
2. [Step 2 of the flow]
3. [Step 3 of the flow]
4. [Result or outcome]
---
> _"[UI copy that appears to the user]" **[CTA Button]**_
---
### ◊ **Algorithm**
---
[Description of the algorithm driving this pattern]
---
**[Factor Name]** → Weight: [X]%
_[What this optimizes for]_
---
*   **[Sub-factor]** ([Y]%)
    *   [Condition and weight]
    *   [Condition and weight]
---
```

---

## 5. 📊 PERFORMANCE METRICS TEMPLATE

- **What it is:** Centralized metric definitions, targets, thresholds, and playbooks for action.
- **When to use:** Establish or revise KPIs; align product, data, and ops on responses.
- **Best practices – Do:** Define ownership, thresholds, and explicit actions on breach.
- **Best practices – Don't:** List vanity metrics or leave actions ambiguous.

```markdown
# Performance Tracking

**Parent:** [Feature/System] | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
This document defines the comprehensive performance tracking framework for [feature/system]. It establishes the metrics teams should monitor, specifies intervention thresholds, and prescribes response protocols for maintaining [platform/feature] health and growth.

[Additional context about why these metrics matter]

This [central/feature] performance tracking document provides:
*   **[Visibility type]** - [What it reveals]
*   **[Intervention clarity]** - [How it guides action]
*   **[Response protocols]** - [What happens when thresholds are hit]
*   **[Alignment]** - [How teams coordinate]
*   **[Intelligence]** - [How data drives decisions]
---
## ◻︎ Metric Definitions
---
[Core metrics description and purpose]
---

| Metric | Description |
| ---| --- |
| **[Acronym]** | [Full name and what it measures] |
| **[Acronym]** | [Full name and what it measures] |
| **[Acronym]** | [Full name and what it measures] |



# ❖ [Metric Category 1]
---
[What we track and why it matters for the business]
---
## ◻︎ Target Metrics Framework
---
[What this framework measures and its purpose]
---
### ◊ [Metric Group]
---
#### —— Targets
---
*   [Metric name and unit]
*   [Metric name and unit]
*   [Metric name and unit]
*   [Metric name and unit]
---
#### —— Thresholds & Actions
---
1. **[Metric condition]** = [threshold]
---
**Situation:** [What this indicates is happening]
**Action:** [Primary intervention] → [Secondary action] → [Tertiary action] → [Measurement]
---
2. **[Metric condition]** = [threshold]
---
**Situation:** [Problem this represents]
**Action:** [Solution pathway] → [Implementation steps] → [Success criteria]
---
### ◊ [Metric Group 2]
---
#### —— Targets
---
*   [Funnel metric with conversion points]
*   [Rate or ratio metrics]
*   [Time-based metrics]
*   [Quality metrics]
---
#### —— Thresholds & Actions
---
1. **[Conversion metric]** = below [X]%
---
**Situation:** [Specific problem this indicates]
**Action:** [Targeted solution] → [Follow-up action] → [Iteration plan]
---
2. **[Complex multi-part threshold]**
**Situation:**
*   [Condition 1] < [threshold]
*   [Condition 2] < [threshold]
*   [Condition 3] < [threshold]

**Action:** [Coordinated response] → [Systematic improvement] → [Validation]
---
```

---

## 6. 🗺️ USER JOURNEY TEMPLATE

- **What it is:** A research-backed narrative of a user's path with phases, pain points, and metrics.
- **When to use:** Strategy, UX planning, growth loops, and cross-team alignment.
- **Best practices – Do:** Quantify phase drop-offs, define interventions, tie to business outcomes.
- **Best practices – Don't:** Treat as static; revisit when behavior or product shifts.

```markdown
# [Journey Name]

**Parent:** [Product Area] | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
[Description of this user journey and its importance]

This journey represents [percentage]% of [user type] and drives [business metric]. Understanding this flow helps us [optimization goal].
---
### → References
---
1. **User Research:** Private ([link])
2. **Analytics Dashboard:** Private ([link])
3. **Journey Map:** Private ([link])
---


# ❖ Journey Overview
---
The [journey name] consists of [X] key phases:
---
## ◻︎ Journey Map
---

| Phase | User Goal | Pain Points | Opportunities |
| ---| ---| ---| --- |
| **Discovery** | [What user wants] | [Friction points] | [Improvement ideas] |
| **Evaluation** | [Decision criteria] | [Blockers] | [Enhancement options] |
| **Action** | [Desired outcome] | [Failure points] | [Success boosters] |
| **Success** | [Value realized] | [Dissatisfaction] | [Retention hooks] |



# ❖ Phase: [Phase Name]
---
[What happens in this phase and why it matters]
---
## ◻︎ Entry Points
---
### ◊ **Primary Entry**
---
[Most common way users enter this phase]
---
*   **Source:** [Where they come from]
*   **Trigger:** [What prompts this]
*   **Context:** [User mindset]
---
### ◊ **Alternative Entries**
---
[Other ways users might arrive here]
---
1. **[Entry type]:** [Description and frequency]
2. **[Entry type]:** [Description and frequency]
---
## ◻︎ User Actions
---
### ◊ **Critical Path**
---
The optimal flow through this phase:
---
1. [Action 1] → [Result]
2. [Action 2] → [Result]
3. [Action 3] → [Result]
4. [Success state]
---
### ◊ **Drop-off Points**
---
Where we lose users and why:
---
| Drop Point | Rate | Reason | Intervention |
| ---| ---| ---| --- |
| **[Step]** | X% | [Why they leave] | [What we do] |
| **[Step]** | X% | [Why they leave] | [What we do] |
---
## ◻︎ Success Metrics
---
### ◊ **Phase Completion**
---
#### —— Targets
---
*   Completion rate: [X]%
*   Time to complete: [X] minutes
*   Error rate: <[X]%
*   Satisfaction: [X]/5
---
#### —— Thresholds & Actions
---
1. **Completion drops** = below [X]%
---
**Situation:** Users abandoning at this phase
**Action:** [Immediate fix] → [Testing approach] → [Long-term solution]
---


# ❖ Optimization Opportunities
---
## ◻︎ Quick Wins
---
### ◊ **[Improvement Name]**
---
**Impact:** High | **Effort:** Low | **Timeline:** 1 sprint
---
[Description of the improvement]
---
*   **Current state:** [Problem]
*   **Future state:** [Solution]
*   **Success metric:** [How we measure]
---
## ◻︎ Strategic Improvements
---
### ◊ **[Major Enhancement]**
---
**Impact:** High | **Effort:** High | **Timeline:** 1 quarter
---
[Description of the enhancement]
---
**Implementation phases:**
1. **Research:** [What we need to learn]
2. **Design:** [What we'll create]
3. **Build:** [Technical requirements]
4. **Measure:** [Success criteria]
---
```

---

## 7. 📦 COMPONENT LIBRARY TEMPLATE

- **What it is:** A canonical reference for UI components with props, usage, states, and a11y.
- **When to use:** Design system documentation, engineering onboarding, code reviews.
- **Best practices – Do:** Include minimal examples, variants, and accessibility guidance.
- **Best practices – Don't:** Embed app-specific logic; keep components generic.

````markdown
# Component Library

**Parent:** Design System | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
This library contains all reusable components that power [product name]. Each component follows our design system principles and includes built-in accessibility, theming, and responsive behavior.

Components are organized by:
*   **Atomic:** Basic building blocks
*   **Molecular:** Combined components
*   **Organisms:** Complex UI patterns
---
### → References
---
1. **Storybook:** Private ([link])
2. **Figma Library:** Private ([link])
3. **Usage Guidelines:** Private ([link])
---


# ❖ [Component Category]
---
[Description of this category of components]
---
## ◻︎ [Component Name]
---
[What this component does and when to use it]
---
### ◊ **Props**
---

| Prop | Type | Default | Required | Description |
| ---| ---| ---| ---| --- |
| **variant** | string | 'primary' | No | Visual style |
| **size** | string | 'medium' | No | Component size |
| **disabled** | boolean | false | No | Interaction state |
| **onClick** | function | - | Yes | Click handler |

---
### ◊ **Usage**
---
```jsx
import { Button } from '@company/components';

// Basic usage
<Button onClick={handleClick}>
  Click me
</Button>

// With options
<Button
  variant="secondary"
  size="large"
  disabled={isLoading}
  onClick={handleSubmit}
>
  Submit Form
</Button>
```
---
### ◊ **Variants**
---
#### —— Primary
---
Default action style for main CTAs
---
```jsx
<Button variant="primary">Primary Action</Button>
```
---
#### —— Secondary
---
Alternative actions and less emphasis
---
```jsx
<Button variant="secondary">Secondary Action</Button>
```
---
### ◊ **States**
---

| State | Trigger | Visual Change | Behavior |
| ---| ---| ---| --- |
| **Default** | Initial | Base styling | Interactive |
| **Hover** | Mouse over | Elevated/highlighted | Cursor pointer |
| **Active** | Click/tap | Pressed appearance | Trigger action |
| **Disabled** | prop | Grayed out | No interaction |
| **Loading** | prop | Spinner shown | No interaction |

---
### ◊ **Accessibility**
---
*   **ARIA:** Proper role and labels
*   **Keyboard:** Full navigation support
*   **Screen reader:** Descriptive announcements
*   **Focus:** Visible focus indicators
---
### ◊ **Performance**
---
*   **Bundle size:** [X]kb minified
*   **Load time:** [X]ms average
*   **Render:** [X]ms average
*   **Memory:** [X]kb footprint
---
````

---

## 8. 📢 RELEASE NOTES TEMPLATE

- **What it is:** A clear, user-facing summary of changes, impact, and actions required.
- **When to use:** Every production release; also for internal pilot notes.
- **Best practices – Do:** Lead with value, show before/after metrics, link migrations.
- **Best practices – Don't:** Dump commit logs; curate and group by audience.

````markdown
# Release [Version Number]

**Parent:** Product | **Version:** [X.Y.Z] | **Release Date:** [Date]
---
# ⌘ About
---
This release [main theme or focus]. We've [high-level summary of changes] based on [user feedback/strategic goals].

Key highlights:
*   **[Major feature 1]** [brief impact]
*   **[Major feature 2]** [brief impact]
*   **[Performance/Quality]** [improvement metric]
---
### → References
---
1. **Full Changelog:** Private ([link])
2. **Migration Guide:** Private ([link])
3. **Known Issues:** Private ([link])
---


# ❖ New Features
---
## ◻︎ [Feature Name]
---
[What this feature does and why we built it]
---
### ◊ **What's New**
---
[Detailed description of the feature]
---
*   **Capability 1:** [Description]
*   **Capability 2:** [Description]
*   **Capability 3:** [Description]
---
### ◊ **How to Use**
---
1. [Step 1 to access/enable]
2. [Step 2 to configure]
3. [Step 3 to use]
---
### ◊ **Impact**
---

| Metric | Before | After | Improvement |
| ---| ---| ---| --- |
| **[Speed]** | [X]ms | [Y]ms | [Z]% faster |
| **[Success]** | [X]% | [Y]% | [Z]% increase |

---


# ❖ Improvements
---
## ◻︎ Performance
---
### ◊ **Optimizations**
---
*   **[Area]:** [X]% faster load times
*   **[Area]:** [X]% reduction in memory usage
*   **[Area]:** [X]% improved render performance
---
## ◻︎ User Experience
---
### ◊ **Enhancements**
---
*   **[Flow]:** Simplified from [X] to [Y] steps
*   **[Interface]:** Improved [specific aspect]
*   **[Accessibility]:** Added [feature] support
---


# ❖ Bug Fixes
---
## ◻︎ Critical
---
*   **Fixed:** [Issue description] that caused [impact]
*   **Fixed:** [Issue description] affecting [X]% of users
---
## ◻︎ Minor
---
*   **Fixed:** [UI issue] in [component/area]
*   **Fixed:** [Edge case] when [condition]
---


# ❖ Breaking Changes
---
## ◻︎ API Changes
---
### ◊ **Deprecated**
---
```javascript
// Old way (deprecated)
client.oldMethod();

// New way
client.newMethod();
```
---
### ◊ **Migration**
---
1. **Update dependencies** to version [X]
2. **Replace calls** to deprecated methods
3. **Test** affected integrations
4. **Deploy** with confidence
---
## ◻︎ Timeline
---

| Phase | Date | Action Required |
| ---| ---| --- |
| **Deprecation** | [Date] | Update warnings appear |
| **Migration** | [Date] | Switch to new methods |
| **Removal** | [Date] | Old methods removed |

---
````

---

## 9. 🌳 ARCHITECTURE DECISION TEMPLATE

- **What it is:** A structured record (ADR) of significant technical decisions and their tradeoffs.
- **When to use:** Any decision that affects architecture, costs, or team constraints.
- **Best practices – Do:** Capture context, options, pros/cons, and measurable success.
- **Best practices – Don't:** Skip consequences; note what becomes harder too.

```markdown
# ADR: [Decision Title]

**Parent:** Architecture | **Version:** 1.0 | **Date:** [Date]
---
# ⌘ About
---
**Status:** [Proposed | Accepted | Deprecated | Superseded]

**Context:** [The issue that motivated this decision and its context]

**Decision:** [The change we're proposing or have agreed to implement]

**Consequences:** [What becomes easier or harder because of this change]
---
### → References
---
1. **RFC Document:** Private ([link])
2. **Technical Spike:** Private ([link])
3. **Related ADRs:** Private ([link])
---


# ❖ Problem Statement
---
[Detailed description of the problem we're solving]
---
## ◻︎ Current State
---
### ◊ **Architecture**
---
[How things work today]
---
*   **Component:** [Current implementation]
*   **Data flow:** [Current pattern]
*   **Dependencies:** [Current structure]
---
### ◊ **Pain Points**
---
1. **[Issue 1]:** [Impact and frequency]
2. **[Issue 2]:** [Impact and frequency]
3. **[Issue 3]:** [Impact and frequency]
---
## ◻︎ Requirements
---
### ◊ **Functional**
---
*   Must [requirement]
*   Must [requirement]
*   Should [requirement]
*   Could [requirement]
---
### ◊ **Non-Functional**
---

| Requirement | Target | Rationale |
| ---| ---| --- |
| **Performance** | <[X]ms response | User experience |
| **Scalability** | [X] concurrent users | Growth projections |
| **Reliability** | [X]% uptime | SLA requirements |

---


# ❖ Options Considered
---
## ◻︎ Option 1: [Name]
---
[Brief description of this approach]
---
### ◊ **Pros**
---
*   ✅ [Advantage]
*   ✅ [Advantage]
*   ✅ [Advantage]
---
### ◊ **Cons**
---
*   ❌ [Disadvantage]
*   ❌ [Disadvantage]
*   ❌ [Disadvantage]
---
### ◊ **Effort & Risk**
---

| Aspect | Assessment | Notes |
| ---| ---| --- |
| **Implementation** | [Low/Medium/High] | [Explanation] |
| **Migration** | [Low/Medium/High] | [Explanation] |
| **Risk** | [Low/Medium/High] | [Mitigation] |

---
## ◻︎ Option 2: [Name]
---
[Brief description of this approach]
---
### ◊ **Pros**
---
*   ✅ [Advantage]
*   ✅ [Advantage]
---
### ◊ **Cons**
---
*   ❌ [Disadvantage]
*   ❌ [Disadvantage]
---


# ❖ Decision
---
We will implement **Option [X]: [Name]** because [primary reasons].
---
## ◻︎ Rationale
---
### ◊ **Technical Factors**
---
*   **[Factor]:** [Why this matters]
*   **[Factor]:** [Why this matters]
---
### ◊ **Business Factors**
---
*   **[Factor]:** [Impact on business]
*   **[Factor]:** [Impact on business]
---
## ◻︎ Implementation Plan
---
### ◊ **Phase 1: Foundation**
---
**Timeline:** [X] weeks
---
1. [Task 1]
2. [Task 2]
3. [Task 3]
---
### ◊ **Phase 2: Migration**
---
**Timeline:** [X] weeks
---
1. [Task 1]
2. [Task 2]
---
## ◻︎ Success Metrics
---
### ◊ **Technical Metrics**
---
*   Response time improved by [X]%
*   Error rate reduced to <[X]%
*   Test coverage increased to [X]%
---
### ◊ **Business Metrics**
---
*   User satisfaction score >[X]
*   Development velocity increased [X]%
*   Incident frequency reduced [X]%
---
```

---

## 10. 🔍 TROUBLESHOOTING GUIDE TEMPLATE

- **What it is:** A symptom-first guide to diagnose, resolve, and prevent issues.
- **When to use:** Support runbooks, on-call readiness, incident response training.
- **Best practices – Do:** Provide quick fixes, deep dives, and prevention.
- **Best practices – Don't:** Hide command outputs; show expected results.

````markdown
# Troubleshooting [Feature/System]

**Parent:** Support | **Version:** 1.0 | **Reading Time:** [X] minutes
---
# ⌘ About
---
This guide helps diagnose and resolve common issues with [feature/system]. It's organized by symptoms to help you quickly find solutions.

For urgent issues, contact:
*   **Support:** [contact method]
*   **Emergency:** [escalation path]
*   **Status Page:** [status.company.com]
---
### → References
---
1. **Known Issues:** Private ([link])
2. **Support Tickets:** Private ([link])
3. **System Status:** Private ([link])
---


# ❖ Common Issues
---
## ◻︎ [Problem Category]
---
### ◊ **[Specific Problem]**
---
**Symptoms:**
*   [What user sees/experiences]
*   [Error messages displayed]
*   [When it typically occurs]
---
#### —— Quick Fix
---
Try these steps first:
---
1. [Simple solution step 1]
2. [Simple solution step 2]
3. [Test if resolved]
---
#### —— Detailed Solution
---
If quick fix doesn't work:
---
1. **Verify [prerequisite]**
   ```bash
   command to check status
   ```
   Expected output: [what should appear]

2. **Check [configuration]**
   ```json
   {
     "setting": "correct_value"
   }
   ```

3. **Clear [cache/data]**
   * Location: [where to find]
   * Command: `clear-cache --all`

4. **Restart [service]**
   ```bash
   service restart [name]
   ```
---
#### —— Root Cause
---
This typically happens when [explanation of why this occurs].
---
#### —— Prevention
---
To avoid this issue:
*   [Preventive measure 1]
*   [Preventive measure 2]
*   [Monitoring recommendation]
---


# ❖ Diagnostic Tools
---
## ◻︎ Health Check
---
### ◊ **System Status**
---
Run comprehensive health check:
---
```bash
curl https://api.company.com/health
```
---
Expected response:
```json
{
  "status": "healthy",
  "services": {
    "api": "operational",
    "database": "operational",
    "cache": "operational"
  }
}
```
---
### ◊ **Component Status**
---

| Component | Check Command | Healthy Response |
| ---| ---| --- |
| **Database** | `db-status` | Connection: OK |
| **Cache** | `redis-cli ping` | PONG |
| **Queue** | `queue-health` | Jobs: 0 pending |

---
## ◻︎ Logs
---
### ◊ **Log Locations**
---

| Service | Location | Useful Grep |
| ---| ---| --- |
| **Application** | `/var/log/app.log` | `grep ERROR` |
| **API** | `/var/log/api.log` | `grep 5[0-9][0-9]` |
| **System** | `/var/log/syslog` | `grep [service]` |

---
### ◊ **Log Analysis**
---
Find errors in last hour:
```bash
grep "ERROR" /var/log/app.log | tail -n 100
```
---
Check for patterns:
```bash
awk '/ERROR/ {print $4}' app.log | sort | uniq -c | sort -rn
```
---


# ❖ Performance Issues
---
## ◻︎ Slow Response
---
### ◊ **Diagnosis**
---
#### —— Identify Bottleneck
---
1. **Check response times**
   ```bash
   curl -w "@curl-format.txt" -o /dev/null -s https://api/endpoint
   ```

2. **Monitor resources**
   ```bash
   top -b -n 1 | head -20
   ```

3. **Database queries**
   ```sql
   SHOW PROCESSLIST;
   ```
---
### ◊ **Solutions**
---
#### —— Quick Optimizations
---
*   **Clear cache:** `cache-clear --all`
*   **Restart services:** `systemctl restart [service]`
*   **Increase limits:** Update configuration
---
#### —— Long-term Fixes
---
*   **Scale horizontally:** Add more instances
*   **Optimize queries:** Add indexes
*   **Upgrade resources:** Increase CPU/RAM
---


# ❖ Escalation
---
## ◻︎ When to Escalate
---

| Severity | Criteria | Response Time | Escalation Path |
| ---| ---| ---| --- |
| **Critical** | System down | 15 minutes | Page on-call |
| **High** | Feature broken | 1 hour | Notify team lead |
| **Medium** | Degraded performance | 4 hours | Create ticket |
| **Low** | Minor issue | Next business day | Log for review |

---
## ◻︎ Information to Provide
---
### ◊ **Required Details**
---
When escalating, always include:
---
*   **Environment:** [Production/Staging/Dev]
*   **User impact:** [Number affected]
*   **Error messages:** [Exact text]
*   **Reproduction steps:** [How to trigger]
*   **Attempted solutions:** [What you tried]
*   **Timeline:** [When it started]
---
````

---

## 11. 🎨 FORMATTING STANDARDS

### Document Structure

1. **Header:** Feature name with no special characters
2. **Metadata bar:** Parent | Version | Reading Time
3. **Separator:** Always use `* * *` between sections
4. **About section:** Always starts with `# ⌘ About`
5. **Main sections:** Use `# ❖ [Section Name]`
6. **Subsections:** Use `## ◻︎ [Subsection Name]`
7. **Components:** Use `### ◊ [Component Name]`
8. **Details:** Use `#### —— [Detail Name]`

### Symbol Hierarchy

* **⌘ (H1):** "About" section
* **❖ (H1):** Main section headers
* **◻︎ (H2):** Sub-section headers
* **◊ (H3):** Component headers
* **—— (H4):** Detail headers
* **→:** References and links

### Formatting Patterns

* **Horizontal rules:** Three asterisks with spaces: `* * *`
* **Tables:** Clean markdown with alignment
* **Lists:** Numbered for sequences, bullets for unordered
* **Emphasis:** Bold for key terms and metrics
* **Quotes:** Use `>` for UI copy or user messages
* **Links:** Always indicate Private/Public status
* **Code blocks:** Use appropriate language syntax highlighting

### Metric Formatting

* **Thresholds:** Always use `=` with comparison
* **Percentages:** Include % symbol
* **Arrows:** Use `→` for flows and connections
* **Weights:** Format as "Weight: X%"
* **Conditions:** Bold the metric name

### Section Conventions

* **Features:** Always numbered list with separators
* **Overview:** Bullet points or table summary
* **Algorithm:** Weighted factors with sub-factors
* **Logic:** Numbered steps or bullet rules
* **Performance:** Targets → Thresholds & Actions
* **References:** Numbered list with Private/Public designation

### Special Characters

* **Section headers:** ⌘ (About), ❖ (Main), ◻︎ (Sub), ◊ (Component), —— (Detail)
* **Arrows:** → (references, flows)
* **Emoji:** Used sparingly for visual hierarchy (🔄 for repeat)
* **Checkmarks:** ✅ for pros, ❌ for cons

---

*All documentation is delivered as artifacts with auto-scaled complexity. Always ask thinking rounds and wait for response. Challenge when 6+ rounds. Use proper symbols and formatting. Include AI System footer with process documentation.*