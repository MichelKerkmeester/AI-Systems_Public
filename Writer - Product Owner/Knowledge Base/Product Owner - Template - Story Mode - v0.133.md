# Product Owner - Template - Story Mode - v0.133

User story templates with integrated formatting rules and quality standards. All delivery logic consolidated for self-contained operation.

---

## 📋 TABLE OF CONTENTS
1. [📖 STORY MODE OVERVIEW](#1-story-mode-overview)
2. [📦 DELIVERY STANDARDS](#2-delivery-standards)
3. [📏 COMPLEXITY AUTO-SCALING](#3-complexity-auto-scaling)
4. [✅ QUALITY CHECKLIST](#4-quality-checklist)
5. [🚨 ERROR RECOVERY](#5-error-recovery)
6. [🔵 SIMPLE STORY TEMPLATE](#6-simple-story-template)
7. [🟠 STANDARD STORY TEMPLATE](#7-standard-story-template)
8. [🔴 COMPLEX STORY TEMPLATE](#8-complex-story-template)
9. [⚡ QUICK MODE TEMPLATES](#9-quick-mode-templates)

---

## 1. 📖 STORY MODE OVERVIEW

### Command: `$story`

- **Purpose:** Create user stories in narrative format that auto-scale complexity
- **Output:** Always as `text/markdown` artifact
- **Thinking:** 10 rounds automatic (DEPTH methodology), 1-5 auto-scaled for $quick
- **Interactive Mode:** Single comprehensive question gathering ALL requirements
- **Key Difference:** Stories omit Resolution Checklist, focus on user journey and narrative
- **Header Position:** Always at top as first line
- **Output Constraints:** Story contains ONLY the requested feature/capability

### Critical Rules
- **NEVER create artifact until user responds to comprehensive questions**
- **NEVER answer own questions - always wait for user response**
- **NO TABLE OF CONTENTS** - ClickUp/Jira provide native TOC functionality
- **HEADER AT TOP:** System metadata appears as first line of artifact
- **NO RESOLUTION CHECKLIST:** Stories use narrative format with acceptance criteria
- **SHORT DESCRIPTION:** 1-2 concise sentences after title explaining WHAT was built/changed
- **FEATURES SECTION:** Bulleted list of key features immediately after description
- **INTERACTIVE QUESTIONS:** Handled by Interactive Mode v0.305 file, not in template

### Note on Development Tickets
For development tickets with QA checklists and resolution tracking, use `$ticket` command which references **Product Owner - Template - Ticket Mode - v0.133.md**

---

## 2. 📦 DELIVERY STANDARDS

### Universal Requirements
- **Artifact Type:** Always use `text/markdown` (never `text/plain`)
- **Single Artifact:** All content delivered as one artifact
- **DEPTH Processing:** 
  - Standard modes: 10 rounds automatic (not user choice)
  - Quick mode: 1-5 rounds auto-scaled based on complexity
- **Wait for Input:** NEVER proceed without user response to questions
- **Template Compliance:** Use v0.133 structure exactly

### Story-Specific Standards
- **Scaling:** 
  - Simple: 2-3 sections, focused narrative
  - Standard: 4-5 sections, detailed journey
  - Complex: 6-8 sections, comprehensive scenarios
- **Output Focus:** ONLY deliver what user requested
- **No Scope Expansion:** Template scaling affects structure, not content scope
- **Multiple Perspectives:** All analyze the SAME requirement
- **Convergent Output:** Many approaches considered, ONE delivered
- **User Journey Focus:** Emphasize user perspective and experience
- **No QA Checklist:** Stories end with change summary, not resolution checklists

### Mandatory Structure Elements

#### Symbol Hierarchy
- **H1:** ⌘ (About), ❖ (Requirements), ❖ (Change Summary)
- **H2:** ✦ (Success), ⌥ (Designs)
- **H3:** Clean headers (no symbols)
- **H4:** #### (Subsections within Requirements and Change Summary)

#### Structure Order
1. About (⌘) - Context narrative only (no separate User Need/Business Value/Scope)
2. Short description (1-2 sentences) - WHAT was built/changed
3. Features - Bulleted list of key features
4. User Need (numbered) - What problem this solves
5. Business Value (numbered) - Why it matters to business
6. Success Criteria (✦) - After Business Value
7. Designs & References (⌥) - Bulleted list with categories
8. Requirements (❖) - Implementation requirements with H4 subsections
9. Change Summary (❖) - Section documenting all changes with H4 subsections

#### Formatting Standards
- **Dividers:** Use `---` between all sections (not between description and User Need)
- **Lists:** Always use `-` for bullets, `[]` for checkboxes
- **Designs & References:** Bulleted list organized by categories (Flows, Components, Related Stories)
- **Links:** Use `[Description](URL)` format with actual URLs
- **Requirements:** Use H4 (####) for subsections, not H3
- **Change Summary:** Use H4 (####) for individual change items
- **Priority:** Format as `**→ Priority:** Critical/High/Medium/Low` in About section

### Visual Hierarchy Rules
- Use `---` as section separators
- H1 for title, major sections (⌘ About, ❖ Requirements, ❖ Change Summary)
- H2 for secondary sections (✦ Success, ⌥ Designs)
- H3 NEVER used in current pattern
- H4 for subsections within Requirements and Change Summary
- No blank lines between dividers and section headers
- Clean headers at H4 level (no symbols)

### Content Integration
- **About Section:** Context narrative only, no bold labels (appears first)
- **Short Description:** 1-2 concise sentences after About explaining WHAT changed
- **Features:** Bulleted list immediately after description
- **User Need:** Numbered section (1.) after Features (no divider before)
- **Business Value:** Numbered section (2.) after User Need
- Clear narrative flow throughout
- Story covers ONLY requested feature
- Emphasis on practical implementation details

### Story Focus Areas

**Implementation:**
- What was built or changed
- Specific component updates
- Technical requirements
- Visual/interaction specifications

**Change Documentation:**
- NEW: Change Summary section at bottom
- Lists all modifications made
- Organized by component or area
- Uses H4 subsections

**Business Value:**
- Why this matters to users
- How it supports business goals
- Impact on user satisfaction
- Measurable outcomes

---

## 3. 📏 COMPLEXITY AUTO-SCALING

| Keywords | Complexity | Sections | Focus | DEPTH Processing |
|----------|------------|----------|-------|------------------|
| simple, basic, quick | Simple | 2-3 | Single component update | 10 rounds (1-2 if $quick) |
| feature, capability, page | Standard | 4-5 | Complete page/feature | 10 rounds (3 if $quick) |
| platform, system, ecosystem | Complex | 6-8 | Multi-component system | 10 rounds (5 if $quick) |

**Important:** Complexity determines TEMPLATE SIZE, not content scope
- User requests "simple button update" → Simple template for THAT button only
- NOT: Simple template with multiple button variations or extra features

### DEPTH Processing Standards
- **Multiple perspectives:** All analyze SAME requirement
- **Single output:** One story covering exact request
- **No scope expansion:** Complexity affects template size, not feature count

---

## 4. � COMPLEXITY AUTO-SCALING

### Pre-Creation Validation
- [] DEPTH methodology applied (10 rounds standard, 1-5 quick)?
- [] User responded to comprehensive question?
- [] System waited for response (never answered own questions)?
- [] Complexity determined correctly?
- [] Template version confirmed (v0.133)?
- [] Output scope limited to user request?

### Structure Validation
- [] About section positioned first?
- [] Short description (1-2 sentences) after About?
- [] Features section present after description?
- [] User Need numbered section after Features (no divider before)?
- [] Business Value numbered section after User Need?
- [] Success criteria after Business Value?
- [] Designs & References in bulleted list format with categories?
- [] Requirements section with H4 subsections?
- [] Change Summary section at bottom with H4 subsections?
- [] Correct symbol hierarchy applied (H1: ⌘/❖, H2: ✦/⌥, H4: ####)?
- [] Using `* * *` dividers between sections?
- [] NO H3 headers used?
- [] NO Resolution Checklist (story-specific)?

### Format Validation
- [] Using `text/markdown` artifact type?
- [] Lists use `*` bullets?
- [] Checkboxes use `[]` format?
- [] Dividers (`* * *`) between all sections?
- [] Clean H4 headers for subsections?
- [] Actual links included (not placeholders)?
- [] No Table of Contents?
- [] No unrequested features?
- [] Content limited to requested feature?

### Story-Specific Validation (v0.133)
- [] Short description explains WHAT was built/changed?
- [] Features section present and concise?
- [] About section is narrative only (no bold labels)?
- [] User Need and Business Value as numbered sections?
- [] Designs organized by category (Flows, Components, etc.)?
- [] Requirements use H4 subsections (not H3)?
- [] Change Summary section present at bottom?
- [] Change Summary organized by component/area?
- [] Implementation focus maintained?
- [] Practical details included?

---

## 5. 🚨 ERROR RECOVERY

### Common Errors & Fixes

#### Wrong Symbol Hierarchy
**Fix:** Update to H1: ⌘/❖, H2: ✦/⌥, H4: ####, NEVER H3

#### Using H3 Headers
**Fix:** Replace all H3 with H4 for subsections

#### Wrong Divider Type
**Fix:** Replace `* * *` with `---` between all sections

#### Success Criteria at Top
**Fix:** Move after About section, add divider

#### Missing Short Description
**Fix:** Add 1-2 concise sentences after About explaining WHAT changed

#### Missing Features Section
**Fix:** Add bulleted list of key features after short description

#### About Section with Bold Labels
**Fix:** Remove "User Need:", "Business Value:", "Scope:" - make About narrative only

#### User Need/Business Value in About
**Fix:** Move to separate numbered sections (1. User Need, 2. Business Value) after Features

#### Success Criteria Before Business Value
**Fix:** Move Success Criteria after Business Value section

#### Designs as Table or Numbered List
**Fix:** Convert to bulleted list organized by categories

#### Missing Change Summary
**Fix:** Add ❖ Change Summary section at bottom with H4 subsections

#### Created Without User Input
**Fix:** Stop, apologize, ask comprehensive question, WAIT

#### Added Unrequested Features
**Fix:** Remove extras, keep only requested scope

#### Wrong Artifact Type
**Fix:** Recreate with `text/markdown`

#### Missing Separators
**Fix:** Add `---` between major sections

#### Table of Contents Included
**Fix:** Remove ToC, rely on external tools

#### Resolution Checklist Included (Wrong for Stories)
**Fix:** Remove checklist, ensure Change Summary is present

### Prevention Strategies
1. Apply DEPTH automatically (10 rounds standard, 1-5 quick)
2. Wait for comprehensive response
3. Check template version (v0.133)
4. Verify symbol hierarchy (no H3)
5. Position sections correctly
7. Include short description after title
8. Use bulleted list for Designs & References
9. Add Change Summary at bottom
10. Use `---` dividers
10. Limit output to request
11. Use correct artifact type
12. NEVER answer own questions

---

## 6. 🔵 SIMPLE STORY TEMPLATE

```markdown
# ⌘ About

[Narrative context: Current situation, what changed, and how it improves things]

**→ Priority:** Medium

[1-2 concise sentences explaining WHAT was built or changed and WHY it matters]

**Features**
- [Key feature 1]
- [Key feature 2]
- [Key feature 3]

1. **User Need**
   [What problem this solves for the user and why it matters]

2. **Business Value**
   [Why this matters to the business and expected impact]

---

## ✦ Success Criteria

- [Component] matches Figma specifications
- [Functionality] works correctly
- [Measurable outcome] achieved

---

## ⌥ Designs & References

**Flows**
- [Flow name with link]

**Components**
- [Component name with link]

---

# ❖ Requirements

#### **1. [Component/Area Name]**

- [Specific requirement]
- [Implementation detail]
- [Visual/interaction specification]

---

#### **2. [Another Component/Area]**

- [Specific requirement]
- [Implementation detail]

---

# ❖ Change Summary

#### 1. [Component/Area Name]

- [Specific change made]
- [Update implemented]
- [Modification completed]
---
```

---

## 7. 🟠 STANDARD STORY TEMPLATE

```markdown
# ⌘ About

[Extended narrative: Current state challenges, what was changed, how solution addresses needs, and expected outcomes]

**→ Priority:** Medium

[2-3 concise sentences explaining WHAT was built or changed, WHY it matters, and the key improvements delivered]

**Features**
- [Key feature 1 with brief detail]
- [Key feature 2 with brief detail]
- [Key feature 3 with brief detail]
- [Key feature 4 with brief detail]

1. **User Need**
   [Detailed problem this solves for users, including pain points and why quick navigation and contextual information matters for informed decisions]

2. **Business Value**
   [Detailed value to business including how improved usability reduces time, enhances satisfaction, and achieves goals through specific improvements]

---

## ✦ Success Criteria

- All UI components match Figma specifications
- All flows function correctly with updated interactions
- [Specific performance metric] achieved
- [Measurable user outcome] realized
- Related stories successfully implemented

---

## ⌥ Designs & References

**Flows**
- [Flow name](URL)
- [Another flow](URL)

**Components**
- [Component name](URL)
- [Another component](URL)

**Related Stories**
- [Story name with link]

---

# ❖ Requirements

## Global

#### **1. [Global Component/Feature]**

- [Requirement detail]
- [Implementation specification]
- [Visual/interaction requirement]

**[Subsection if needed]**
- [Detailed requirement]
- [Specific implementation]

---

#### **2. [Another Global Component]**

- [Requirement detail]
- [Implementation specification]

---

## [Major Section Name]

#### **1. [Component Name]**

**[Sub-feature Name]**
- [Requirement detail]
- [Implementation specification]

**[Another Sub-feature]**
- [Requirement detail]
- [Implementation specification]

---

#### **2. [Another Component]**

- [Requirement detail]
- [Implementation specification]
- [Visual/interaction specification]

---

# ❖ Change Summary

#### 1. [Component/Area Name]

- [Specific change made]
- [Technical detail of update]
- [Visual/interaction modification]

---

#### 2. [Another Component/Area]

**[Sub-area]**
- [Specific change made]
- [Implementation detail]

**[Another Sub-area]**
- [Specific change made]
- [Update detail]
---
```

---

## 8. 🔴 COMPLEX STORY TEMPLATE

```markdown
# ⌘ About

[Extended comprehensive narrative: Current state challenges across segments, user impact, research findings, solution approach, expected outcomes, and strategic alignment]

**→ Priority:** Critical

[3 sentences providing comprehensive overview of WHAT was built/changed, WHY it matters, and the strategic value delivered]

**Features**
- [Key feature 1 with detail]
- [Key feature 2 with detail]
- [Key feature 3 with detail]
- [Key feature 4 with detail]
- [Key feature 5 with detail]

1. **User Need**
   [Comprehensive problem this solves for users across different segments, including detailed pain points, impacts, and why contextual information matters for informed collaboration decisions]

2. **Business Value**
   [Comprehensive value to business including how improvements support strategic goals, reduce costs, enhance satisfaction, and achieve measurable business objectives]

---

## ✦ Success Criteria

- All UI components match Figma specifications
- All flows function correctly with smooth transitions
- [Technical requirement] implemented per specifications
- [Performance metric] meets or exceeds target
- Related stories successfully integrated
- [User adoption metric] achieved within timeframe
- [Business metric] improved by target percentage

---

## ⌥ Designs & References

**Flows**
- [Primary flow](URL)
- [Secondary flow](URL)
- [Edge case flow](URL)

**Components**
- [Core component](URL)
- [Supporting component](URL)
- [Related component](URL)

**Technical Specs**
- [API specification](URL)
- [Data model](URL)

**Related Stories**
- [Related story 1](URL)
- [Related story 2](URL)

**Additional Resources**
- [Epic or other documentation](URL)

---

# ❖ Requirements

## Data Migration

- [Migration requirement]
- [Data preservation specification]
- [Rollback capability]
- [Validation requirement]

---

## [Major Feature Area 1]

[Brief description of what this section covers]

#### **1. [Component/Feature Name]**

- [Core requirement]
- [Implementation detail]

**[Sub-feature A]**
- [Detailed requirement]
- [Specific implementation]
- [Validation criteria]

**[Sub-feature B]**
- [Detailed requirement]
- [Specific implementation]

---

#### **2. [Another Component/Feature]**

**[Sub-feature]**
- [Requirement detail]
- [Implementation specification]
- [Edge case handling]

**[Another Sub-feature]**
- [Requirement detail]
- [Implementation specification]
---

## [Major Feature Area 2]

[Brief description of what this section covers]

#### **1. [State/Logic Name]**

- [State definition]
- [Business rules]
- [User impact]

**Implement [specific logic]:**
- [Condition 1]: [Behavior]
- [Condition 2]: [Behavior]
- [Condition 3]: [Behavior]

**Implement [transition logic]:**
- [Transition 1]: [From] → [To] with [conditions]
- [Transition 2]: [From] → [To] with [validation]

---

## Component Changes

Overview of all existing components that have been changed or updated.

#### **1. [Component Name]**

**[Section A]**
- [Change detail]
- [Update specification]

**[Section B]**
- [Change detail]
- [Update specification]

---

#### **2. [Another Component]**

- [Change detail]
- [Implementation specification]
- [Interaction update]

---

#### **3. [Third Component]**

- [Change detail]
- [CSS/styling update]
- [New pattern implementation]

---

# ❖ Change Summary

#### 1. [Major Area/Component 1]

**[Sub-component A]**
- [Specific change implemented]
- [Technical modification detail]
- [New functionality added]

**[Sub-component B]**
- [State management update]
- [Logic implementation detail]
- [Validation requirement added]

---

#### 2. [Major Area/Component 2]

**[Section A]**
- [Component update detail]
- [Styling modification]
- [Interaction pattern change]

**[Section B]**
- [Feature addition]
- [Logic update]
- [UI enhancement]

---

#### 3. [Major Area/Component 3]

- [Migration detail]
- [Data structure change]
- [System integration update]
- [Performance optimization]
---
#### 4. [Additional Changes]
---
**[Area A]**
- [Change detail]
- [Update specification]

**[Area B]**
- [Change detail]
- [Implementation detail]
---
```

---

## 9. ⚡ QUICK MODE TEMPLATES

### Quick Mode Rules
- **NO questions asked** - System proceeds immediately
- **Auto-detection** - Complexity determined from keywords
- **1-5 round scaling** - Based on detected complexity
- **Minimal format** - Essential sections only
- **Same scope discipline** - Only requested content
- **Simplified structure** - No resolution checklist

### $quick story
```markdown
# [Feature Name]

[1-2 sentences explaining what changed and why]

**Features**
- [Key feature]
- [Key feature]

# ⌘ About
---
[Brief narrative context]

1. **User Need**

   [What problem this solves]

2. **Business Value**

   [Why it matters]

---
## ✦ Success
- [Primary outcome]
- [Secondary outcome]
---
## ⌥ Designs
- [Key design link]
---

# ❖ Requirements
#### 1. [Component]
- [Requirement]
- [Implementation detail]
---

# ❖ Change Summary
#### 1. [Area]
- [Change made]
---
```

---

## 10. 🎯 FINAL REMINDERS

1. **Always wait** for user response (except $quick)
2. **Never answer** own questions
3. **Short description** required after title (1-2 sentences explaining WHAT)
4. **Features section** required (bulleted list of key features)
5. **About is narrative only** - no bold labels (User Need/Business Value are separate numbered sections)
6. **User Need and Business Value** as numbered sections (1. and 2.) after About
7. **NO "As a user"** format in title - use simple feature name
8. **Designs as bullets** organized by category (Flows, Components, etc.)
9. **H4 subsections** in Requirements (NEVER H3)
10. **Change Summary** at bottom (mandatory in v0.133)
11. **Use `---` dividers** between all sections
12. **Interactive questions** handled by Interactive Mode v0.305 file
13. **Header at top** as first line
14. **No Table of Contents**
15. **Only requested features** - no scope expansion
16. **DEPTH methodology** applied automatically (10 rounds standard, 1-5 quick)