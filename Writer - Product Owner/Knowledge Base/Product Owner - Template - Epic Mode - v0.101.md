# Product Owner - Template - Epic Mode - v0.101

## 📋 TABLE OF CONTENTS

1. [🚀 EPIC MODE OVERVIEW](#1-🚀-epic-mode-overview)
2. [📈 COMPLEXITY AUTO-SCALING](#2-📈-complexity-auto-scaling)
3. [🧩 DETAILED EPIC TEMPLATE](#3-🧩-detailed-epic-template)
4. [🔍 FEATURE SPECIFICATION TEMPLATE](#4-🔍-feature-specification-template)
5. [🧭 TRANSFORMATION EPIC TEMPLATE](#5-🧭-transformation-epic-template)
6. [🗂️ EPIC FORMATTING RULES](#6-🗂️-epic-formatting-rules)
7. [🗣️ INTERACTIVE QUESTIONS](#7-🗣️-interactive-questions)

---

## 1. 🚀 EPIC MODE OVERVIEW

### Command: `$epic`

* **Purpose:** Create detailed feature specifications with implementation details across apps
* **Output:** Always as artifact with hierarchical feature breakdown
* **Thinking Rounds:** 8-10 (detail requires analysis)
* **Feature Depth:** UI/UX specifications, flows, technical requirements
* **Format:** Nested structure with specific implementation details

---

## 2. 📈 COMPLEXITY AUTO-SCALING

| Complexity        | Detail Level         | Features       | Documentation | Design Status |
| ----------------- | -------------------- | -------------- | ------------- | ------------- |
| **Standard**      | Component-level      | 5-10 features  | 3-5 docs      | Some TBD      |
| **Detailed**      | Implementation-level | 10-20 features | 6-10 docs     | Mixed states  |
| **Comprehensive** | Specification-level  | 20+ features   | 10+ docs      | Full coverage |

---

## 3. 🧩 DETAILED EPIC TEMPLATE

* **What it is:** A complete cross-app epic blueprint with UI/UX, flows, dependencies, and implementation notes.
* **When to use:** Multi-feature initiatives spanning Creator/Partner apps, or any effort needing end-to-end breakdown.
* **Best practices – Do:** Keep scope tight, number features, call out status/dependencies, add success metrics.
* **Best practices – Don't:** Mix unrelated initiatives, hide blockers, or omit owner/risks.

```markdown
# → [Epic Name]

# ◘ About
---
[Description of what this phase/epic accomplishes and its impact on user experience]
---
### ◻️ Scope
---
1. **Creator**
    - [Feature category or major improvement]
    - [Specific feature or capability]
    - [System or workflow]
    - [UI/UX enhancement]
    - [New feature area]
    - [Integration or connectivity]
---
2. **Partner**
    - [Admin feature or tool]
    - [Management capability]
    - [Analytics or reporting]
---
### → Designs & References
---
Check out all the Epic's related documentation and designs:

| **Documentation** | **Creator** (Figma) | Partner (Figma) |
| --- | --- | --- |
| Private ([URL with full link]) | [Feature Name](figma-url) | [Feature Name](figma-url) |
| Private ([URL with full link]) | [Feature Name](figma-url) | |
| Private ([URL with full link]) | [Feature Name](figma-url) | |
| Private ([URL with full link]) | Feature Name | |
| Private ([URL with full link]) | | |
| Private ([URL with full link]) | | |

#

# ■ Overview
---
## ◻️ **Partner App**
---
### ◊ **[Feature Area 1]**
---
[Status note if applicable: "This has not been designed yet. But will be ready ASAP!"]

— [High-level capability description]
— [Key functionality or workflow]
— [Integration or sync behavior]
— [User experience outcome]
---
### ◊ **[Feature Area 2]**
---
1. **[Component Name]**
    - [Specific detail or behavior]
---
2. **[Component Name]**
    - [Technical specification]
    - [Format or requirement (e.g., Aspect ratio: 16:9)]
---
3. **[Component Name]**
    - [Feature description with quantity (e.g., up to 12 items)]
    - [Interaction behavior (e.g., When they click X, Y happens)]
---
4. **[Component Name]**
    - [Display specification]
    - [Formatting support details]
    - [UI behavior (e.g., Expandable view)]
---
## ◻️ **Creator App**
---
### ◊ **[Major Feature Area]**
---
#### **— [Sub-feature Category]**
---
1. **[Specific Component]**
    - [Interaction pattern (e.g., Swipe navigation, up or down)]
    - [UI element update (e.g., Updated pagination label)]
---
2. **[Specific Component]: [State or Variant]**
    - [Different interaction (e.g., Swipe navigation, left or right)]
    - [Additional UI element (e.g., Image thumbnail for direct navigation)]
---
3. **[UI Elements]**
    - [Size or styling change (e.g., All buttons increased to base size)]
    - [Specific element update (e.g., Updated styling for 'Cancel' button)]
---
#### **— [Flow or Process]**
---
— [Required field with specifications (e.g., Written motivation field (Required) with rich text)]
— [Screen or view updates]
    - [Specific UI change in context]
    - [Display logic or positioning]
    - [Input requirement (e.g., checkbox (Required))]
---
#### **— [User Flow]**
---
— [Action trigger (e.g., Updated styling for button)]
— [System response (e.g., New modal when user attempts action)]
— [Information display (e.g., Clear explanation of consequences)]
— [User options (e.g., Option to go back without cancelling)]
---
#### **— [Complex Feature]**
---
1. **[Feature Flow]**
    - [Step 1 of process]
    - [Step 2 with outcome]
    - [Step 3 with interaction detail]
---
[Technical dependency note: "Need details on what's possible before we can design the '[Feature]' step."]
---
2. **[Component Name]**
    - [Display capability]
    - [UI overlay or enhancement]
    - [Real-time data (e.g., metrics: likes, comments, shares)]
    - [Technical requirement (e.g., In-app experience, no external redirects)]
---
[Technical dependency note: "Need details on what's possible before we can design the '[Component]' correctly."]
---
#### **— [Action Feature]**
---
— [Feature description]
— [Trigger behavior:]
    - [Option 1 (e.g., Direct link copy)]
    - [Option 2 (e.g., Share on platforms (OS native modal))]
---
### ◊ **[System Feature]**
---
[Status note: "This has not been designed yet. But will be ready ASAP!"]
---
1. **New feature**
    - [Design element]
    - [UI placement (e.g., Button on home screen)]
---
2. **[Feature Types/Categories]**
    - [Type 1 with description]
    - [Type 2 with description]
    - [Type 3 with description]
    - [Type 4 with description]
    - [Type 5 with description]
    - [Type 6 with description]
---
3. **[Automated System]**
    - [System behavior overview]
    - [Trigger conditions:]
        - [Timing 1 (e.g., 3 Days post-event)]
        - [Timing 2 (e.g., 7 Days post-event)]
        - [Timing 3 (e.g., 14 Days (final))]
    - [Technical capability (e.g., Push notification support)]
---
### ◊ **[Content Area]**
---
1. **[UI Component]**
    - [Design change (e.g., Complete re-design)]
    - [Specific detail (e.g., Scheduled dates appear above name)]
---
2. **[Screen Types]**
    - **[Screen Category]:**
        - [Data point 1]
        - [Data point 2]
        - **Complex feature:**
            - [Sub-detail 1]
            - [Sub-detail 2]
            - [Sub-detail 3]
            - [Sub-detail 4]
            - [Sub-detail 5]
    - **[Screen Category 2]:**
        - [Information display]
        - [Navigation element]
---
### ◊ **[User Feature]**
---
1. **General**
    - [Major change (e.g., Complete re-design)]
    - [New capability with spec (e.g., Support for Cover photo's (16:9))]
    - [Enhancement with details (e.g., Rich text support)]
---
2. **[Feature Component]**
    - [New feature flag]
    - [Capability with limit (e.g., Connect up to 12 pieces)]
    - [Edit capability]
    - **Integration details:**
        - [Interaction behavior]
        - [Data display]
        - [UI element]
        - [Technical requirement]
---
3. **[Future Feature]**
    - [Placeholder state (e.g., Coming soon page)]
    - [User interaction (e.g., Interest feedback (Like/Dislike))]
---
4. **[Future Feature 2]**
    - [Placeholder state]
    - [User interaction]
---
### ◊ **[Edit Feature]**
---
— [Scope of change]
— [New capability 1]
— [New capability 2]
— **Formatting options:** Option1, Option2, Option3, Option4
---
### ◊ **[Settings Area]**
---
[Status note: "This has not been finished yet. But will be ready ASAP!"]

— [Change scope]
— [Functionality preservation]
— [Improvement 1]
— [Improvement 2]
---
```

---

## 4. 🔍 FEATURE SPECIFICATION TEMPLATE

* **What it is:** A single-feature implementation spec with flows, UI components, data, APIs, and tests.
* **When to use:** Building or refining one feature; design/engineering handoff; QA planning.
* **Best practices – Do:** Document edge cases, accessibility, analytics, and performance budgets.
* **Best practices – Don't:** Skip error states, mix multiple features, or leave API responses vague.

```markdown
# [Feature Name] Specification

# ◘ About
---
[Detailed description of the feature's purpose, user value, and business impact]

[Context about why this feature is being built now and how it fits into the larger product vision]
---
### → Designs & References
---
Check out all the Feature's related documentation and designs:

| **Documentation** | **Designs** | **Technical Specs** |
| --- | --- | --- |
| Private ([PRD URL]) | [Main Flow](figma-url) | Private ([API Spec]) |
| Private ([User Research]) | [Edge Cases](figma-url) | Private ([Data Model]) |
| Private ([Analytics Plan]) | [Mobile](figma-url) | Private ([Performance]) |

#

# ■ Feature Details
---
## ◻️ **User Flows**
---
### ◊ **Primary Flow**
---
1. **Entry Point**
    - [Where users start]
    - [Trigger conditions]
    - [Prerequisites]
---
2. **Step 1: [Action Name]**
    - [What user sees]
    - [Available actions]
    - [Validation rules]
    - [Error states]
---
3. **Step 2: [Action Name]**
    - [Screen description]
    - **Input requirements:**
        - [Field 1 (Required/Optional)]
        - [Field 2 with format]
        - [Field 3 with validation]
    - [Real-time feedback]
---
4. **Completion**
    - [Success state]
    - [Confirmation display]
    - [Next actions available]
---
### ◊ **Alternative Flows**
---
#### **— [Edge Case 1]**
---
— [Condition that triggers this flow]
— [Different behavior]
— [Resolution path]
---
#### **— [Error Flow]**
---
— [Error trigger]
— [Error message display]
— **Recovery options:**
    - [Option 1]
    - [Option 2]
    - [Option 3]
---
## ◻️ **UI Components**
---
### ◊ **[Component Name]**
---
#### **— Visual Specifications**
---
— **Dimensions:** [Width x Height or responsive rules]
— **Colors:** [Primary, Secondary, States]
— **Typography:** [Font, Size, Weight]
— **Spacing:** [Padding, Margins]
— **Animation:** [Transitions, Duration]
---
#### **— States**
---
1. **Default**
    - [Visual description]
    - [Content shown]
---
2. **Hover/Focus**
    - [Visual changes]
    - [Interaction feedback]
---
3. **Active/Selected**
    - [Visual indication]
    - [Behavior change]
---
4. **Disabled**
    - [Visual treatment]
    - [Tooltip or explanation]
---
5. **Loading**
    - [Loading indicator]
    - [Skeleton or placeholder]
---
6. **Error**
    - [Error styling]
    - [Error message placement]
---
#### **— Interactions**
---
— **Click/Tap:** [Response behavior]
— **Swipe:** [Direction and outcome]
— **Long Press:** [If applicable]
— **Keyboard:** [Shortcuts if any]
— **Accessibility:** [ARIA labels, tab order]
---
## ◻️ **Data & Logic**
---
### ◊ **Data Requirements**
---
#### **— Input Data**
---
— [Data field 1: Type, Source, Validation]
— [Data field 2: Type, Source, Validation]
— [Data field 3: Type, Source, Validation]
---
#### **— Processing Logic**
---
1. **Validation Rules**
    - [Rule 1 with error message]
    - [Rule 2 with error message]
    - [Rule 3 with error message]
---
2. **Business Logic**
    - [Calculation or transformation]
    - [Conditional logic]
    - [Limits or thresholds]
---
#### **— Output Data**
---
— [Result format]
— [Storage location]
— [Sync requirements]
— [Cache strategy]
---
### ◊ **API Integration**
---
[Technical dependency: "Backend team needs to provide [specific API] before implementation."]
---
#### **— Endpoints**
---
— **GET** `/api/feature/list` - [Description]
— **POST** `/api/feature/create` - [Description]
— **PUT** `/api/feature/update/{id}` - [Description]
— **DELETE** `/api/feature/delete/{id}` - [Description]
---
#### **— Response Handling**
---
— **Success (200):** [UI update]
— **Client Error (4xx):** [Error display]
— **Server Error (5xx):** [Retry logic]
— **Timeout:** [Fallback behavior]
---
## ◻️ **Platform Specifics**
---
### ◊ **Mobile (iOS/Android)**
---
#### **— iOS Specific**
---
— [iOS-only feature or behavior]
— [Native integration (e.g., Face ID)]
— [iOS design pattern]
---
#### **— Android Specific**
---
— [Android-only feature]
— [Material Design consideration]
— [Android-specific permission]
---
### ◊ **Web (Desktop/Mobile)**
---
#### **— Responsive Breakpoints**
---
— **Mobile (<768px):** [Layout description]
— **Tablet (768-1024px):** [Layout description]
— **Desktop (>1024px):** [Layout description]
---
#### **— Browser Support**
---
— Chrome 90+
— Safari 14+
— Firefox 88+
— Edge 90+
---
## ◻️ **Analytics & Tracking**
---
### ◊ **Events to Track**
---
1. **[Event Name]**
    - **Trigger:** [When it fires]
    - **Properties:** [Data to capture]
    - **Purpose:** [Why we track this]
---
2. **[Event Name]**
    - **Trigger:** [When it fires]
    - **Properties:** [Data to capture]
    - **Purpose:** [Why we track this]
---
### ◊ **Success Metrics**
---
— **Adoption:** [Target percentage]
— **Usage:** [Frequency target]
— **Completion:** [Success rate target]
— **Performance:** [Speed/reliability target]
---
## ◻️ **Testing Requirements**
---
### ◊ **Test Scenarios**
---
1. **Happy Path**
    - [Scenario description]
    - [Expected outcome]
---
2. **Edge Cases**
    - [Edge case 1]
    - [Edge case 2]
    - [Edge case 3]
---
3. **Error Cases**
    - [Error scenario 1]
    - [Error scenario 2]
---
### ◊ **Performance Criteria**
---
— **Load Time:** <[X]ms
— **Response Time:** <[Y]ms
— **Concurrent Users:** [Z] minimum
— **Error Rate:** <[A]%
```

---

## 5. 🧭 TRANSFORMATION EPIC TEMPLATE

* **What it is:** A vision-to-execution epic that reimagines a system and phases delivery (P1→P3).
* **When to use:** Platform shifts, architecture changes, major strategic bets with multi-team impact.
* **Best practices – Do:** Require platform prerequisites, define phases, and link analytics baselines.
* **Best practices – Don't:** Start delivery without enabling capabilities or clear success metrics.

```markdown
# Epic → [Transformation Name]

# ◘ About
---
[Vision statement that completely reimagines the product/platform]

We've built a [system type] that [primary value], [secondary value], and [business outcome] all at the same time.

Think of it as a [multiple-win scenario]:
- **[User Type 1]** [specific detailed benefit]
- **[User Type 2]** [specific detailed benefit]
- **Business** [strategic outcome]

Every single feature in this [system] serves [multiple] purposes.
This isn't just a [traditional view]. It's a [revolutionary outcome] that happens to be an [amazing experience].
---
### → Designs & References
---
Check out all the Epic's related documentation and designs:

| **Documentation** | **Creator** (Figma) | **Partner** (Figma) |
| --- | --- | --- |
| Private ([Complete URL]) | [System Redesign](url) | [New Platform](url) |
| Private ([Complete URL]) | [Feature Set 1](url) | [Admin Portal](url) |
| Private ([Complete URL]) | [Feature Set 2](url) | [Analytics](url) |
| Private ([Complete URL]) | [Feature Set 3](url) | [Management](url) |
| Private ([Complete URL]) | [Mobile App](url) | — |
| Private ([Complete URL]) | [Web Platform](url) | — |

#

# ■ Dev. Requirements
---
**Notice:** Before development on [Transformation] begins, the backend team is required to complete these prerequisites. Doing so aligns stakeholders and enables further design and product planning.
---
## ◻️ [Critical Platform Capability]
---
### ◊ **What we need**
---
Ability for [specific technical capability that enables the transformation]
---
### ◊ Requirements
---
#### — Functionalities
---
— [Integration capability with specific platforms]
— [Data processing requirement]
— [Real-time synchronization need]
— [Storage and retrieval specification]
---
#### — [Technical Display/Processing]
---
— [Rendering requirement within platform]
— [Real-time data requirement with sources]
— [UI overlay capability]
— [Platform experience requirement (e.g., no external redirects)]
— [Cross-platform compatibility]
— [Infrastructure for future features]
---
## ◻️ Performance Tracking
---
### ◊ **What we need**
---
Product team needs access to all existing analytics and tracked metrics. This needs to be easily accessible in a centralized location so we can monitor current performance, align it with [Transformation] tracking frameworks, and have it readily available for ongoing reference.
---
### ◊ Requirements
---
Centralized page, sheet or dashboard with all current:
— Real-time data
— Historical data
— Documentation of tracked metrics
---
#

# ■ Phase 1: [Foundation Name]
---
The first phase mainly focuses on [specific improvements] that have a direct positive impact on [outcome], and includes the groundwork needed for phase 2, when we begin [next major initiative].
---
- **Epic:** Private ([URL])
- **Task:** [URL or ...]
---
## ◻️ Scope
---
1. **Creator**
    - [Major feature addition]
    - [Technical capability (e.g., Media player for live content)]
    - [System feature (e.g., Notification system)]
    - [UI overhaul (e.g., Re-designed profile)]
    - [Workflow enhancement]
    - [New screens or views]
---
2. **Partner**
    - [Management feature]
    - [UI enhancement]
    - [Integration capability]
---
## ◻️ Problems we're addressing
---
1. [Specific problem with measurable impact]
2. [Technical limitation blocking growth]
3. [User experience gap affecting metrics]
---
## ◻️ Expected Impact
---
1. [Reduce friction in specific workflow]
2. [Increase metric through feature]
3. [Improve rate with enhancement]
4. [Enable capability directly within platform]
---
##

# ■ Phase 2: [Scale Name]
---
...
---
- **Epic:** Private ([URL])
- **Task:** ...
---
## ◻️ Scope
---
1. **Creator**
    - **[Major Feature]**
        - [Component 1]
        - [Component 2 with algorithm note]
    - **[Search/Discovery]**
        - [Prevention feature]
    - **[Filters/Controls]**
        - [Smart feature]
        - [Organization pattern]
    - **[Content Pages]**
        - [Section 1]
        - [Section 2]
        - [Sharing capability]
---
2. **Partner**
    - **[Workflow Area]**
        - [New creation flows]
        - [Settings or configurations]
    - **[Data Structure]**
        - [Reorganization]
        - [Migration pattern]
---
## ◻️ Problems we're addressing
---
...
---
## ◻️ Expected Impact
---
...
---
##

# ■ Phase 3: [Leadership Name]
---
...
---
- **Epic:** Private ([URL])
- **Task:** ...
---
## ◻️ Scope
---
1. **Creator**
    - **[Advanced System]**
        - [New paradigm or approach]
        - [Interaction system]
    - **[Intelligence Layer]**
        - [Algorithm advancement]
        - [Smart/AI feature]
    - **[Discovery]**
        - [Predictive capability]
    - **[Gallery/Showcase]**
        - [Content display innovation]
---
2. **Partner**
    - ...
---
## ◻️ Problems we're addressing
---
...
---
## ◻️ Expected Impact
---
...
---
```

---

## 6. 🗂️ EPIC FORMATTING RULES

### Hierarchical Detail Structure

```markdown
## ◻️ **App Level**
---
### ◊ **Feature Area**
---
#### **— Component or Flow**
---
1. **Specific Element**
    - Implementation detail
    - Technical specification
---
2. **Another Element**: [Variant]
    - Different implementation
    - Additional specification
```

### Feature Status Callouts

```markdown
[Status note: "This has not been designed yet. But will be ready ASAP!"]
[Status note: "This has not been finished yet. But will be ready ASAP!"]
[Technical dependency: "Need details on what's possible before we can design the '[Feature]'."]
```

### Detail Specifications

```markdown
- [Feature with specification (e.g., Aspect ratio: 16:9)]
- [Capability with limit (e.g., up to 12 connected posts)]
- [Field requirement (e.g., Written motivation (Required))]
- [Interaction detail (e.g., Swipe navigation, up or down)]
- [State change (e.g., When they click X, Y opens)]
```

### Complex Nested Lists

```markdown
1. **Category**
    - Main point
    - Sub-detail:
        - Nested item 1
        - Nested item 2
        - Nested item 3
    - Another point
```

### Required Patterns

1. **Dividers:** Always `---` between sections
2. **Bullets:** Always `- ` with 4-space indentation
3. **Status notes:** Italic or bold callouts for design/dev status
4. **Technical notes:** Clear dependencies and requirements
5. **Specifications:** Inline details (e.g., formats, limits, ratios)
6. **Flows:** Step-by-step breakdowns with outcomes
7. **UI Details:** Specific behaviors and interactions

---

## 7. 🗣️ INTERACTIVE QUESTIONS

### Detail-Focused Epic Flow

```markdown
User: $epic creator platform phase 1

System: Let's create your detailed creator platform epic!

**How many thinking rounds should I use? (8-10)**

Based on "creator platform phase 1", I recommend: 9 rounds
- Complexity: High (multiple features and flows)
- Detail level: Implementation specifications needed
- Apps: Both Creator and Partner sides

Your choice?

[WAIT FOR USER INPUT]

User: 9

System: Let me understand the detail level needed:

1. How many major features to specify? (5-10/10-20/20+)
2. Need technical dependencies noted? (Yes/No)
3. Include "not designed yet" callouts? (Yes/No)

[WAIT FOR ANSWERS]

User: 10-20, Yes, Yes

System: Creating a Detailed Epic with:
- 10-20 features with implementation details
- Technical dependency notes where needed
- Design status callouts for incomplete areas

[CREATES DETAILED EPIC WITH FULL SPECIFICATIONS]
```

---

*All epics delivered as artifacts with auto-scaled complexity. Always ask thinking rounds and wait for response. Challenge when 6+ rounds. Use proper symbols and formatting. Include AI System footer with process documentation.*
