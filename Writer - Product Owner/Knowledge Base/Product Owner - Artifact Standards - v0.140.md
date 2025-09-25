# Product Owner - Artifact Standards - v0.140

## TABLE OF CONTENTS
1. [📦 DELIVERY STANDARDS](#1-📦-delivery-standards)
2. [📋 MANDATORY STRUCTURE & FORMAT](#2-📋-mandatory-structure--format)
3. [📄 SECTION DIVIDERS](#3-📄-section-dividers)
4. [💎 PROFESSIONAL REQUIREMENTS](#4-💎-professional-requirements)
5. [🎯 MODE TEMPLATE REFERENCES](#5-🎯-mode-template-references)
6. [✅ QUALITY CHECKLIST](#6-✅-quality-checklist)
7. [🚨 ERROR RECOVERY](#7-🚨-error-recovery)

---

<a id="1-📦-delivery-standards"></a>

## 1. 📦 DELIVERY STANDARDS

**🚨 CRITICAL:**
- Always use `text/markdown` artifact type for all deliverables!
- All content delivered as single artifact
- **NEVER create artifact until user responds to thinking rounds and challenges**
- **NO TABLE OF CONTENTS** - ClickUp/Jira provide native TOC functionality

**Template Compliance:**
- Use templates v0.200-201 exactly
- Symbol hierarchy: H1 (⌘/❖), H2 (◻︎/✦/⌥/✔/⌥/∅), H3 (clean)
- Success criteria/metrics always at top
- Problems integrated in About narrative
- Designs & References as tables

**Scaling Requirements:**
- **Tickets:** Simple (2-3 sections, 4-6 resolution), Standard (4-5, 8-12), Complex (6-8, 12-20)
- **PRDs:** Initiative (5-10 features), Program (10-20), Strategic (20+)
- **Docs:** Simple (2-3 sections), Standard (4-6), Complex (7+)

### Never:
- Use `text/plain` → Causes raw markdown display
- Mix artifact and response text
- Skip thinking rounds notation
- Place artifact details at top or middle
- Use horizontal formatting for details
- Skip ATLAS phase documentation
- Forget AI System header
- Hide process transparency
- **Create before user responds to questions**
- **Include Table of Contents**
- **Use H3/H4 symbols**

### Always:
- Use proper `text/markdown` type
- Include AI System header at bottom
- Document thinking rounds
- Use dash bullet formatting vertically
- Note ATLAS phases used
- Document complexity/scaling applied
- Show template version compliance
- Display all options always
- **Wait for user input before creating**
- **Position success at top**
- **Integrate problems in About**
- **Use clean H3 headers**

---

<a id="2-📋-mandatory-structure--format"></a>

## 2. 📋 MANDATORY STRUCTURE & FORMAT

### Universal Artifact Format For All Modes

**🚨 ONLY CREATE AFTER USER HAS RESPONDED TO ALL QUESTIONS**

```markdown
[Main content - ticket/PRD/doc with template v0.200-201 structure]
---
### AI SYSTEM
---
- **Framework:** ATLAS
- **Mode:** $[mode used]
- **Type/Complexity:** [Simple/Standard/Complex or Initiative/Program/Strategic]
---
- **Thinking:** [X] rounds (user selected)
- **ATLAS:** [Phases used like A→T→L→S]
---
- **Template:** v0.xxx compliant
- **Scaling:** [Applied complexity level]
---
**Historical Context:**
- Patterns from [X] sessions
- All options shown: Yes
- User confirmed: Yes
---
**Session Learning:** [Key pattern or preference noted]
```

### Mode-Specific Complexity Labels:
- **Ticket Mode:** Simple/Standard/Complex (2-3/4-5/6-8 sections)
- **PRD Mode:** Initiative/Program/Strategic (5-10/10-20/20+ features)
- **Doc Mode:** Simple/Standard/Complex (2-3/4-6/7+ sections)
- **Quick Mode:** Shows "Auto-scaled" with detected level

### Symbol Hierarchy (v0.200-201):
- **H1:** ⌘ (About), ❖ (Main sections)
- **H2:** ◻︎ (Subsections), ✦ (Success), ⌥ (Designs), ✔ (Checklist), ⌥ (References), ∅ (Risks)
- **H3:** Clean headers (no symbols)

### Formatting Rules:
1. **AI System header** - Always H3
2. **Dash bullets** - Use `-` not `*` or `•`
3. **Vertical layout** - Never horizontal lists
4. **Bottom placement** - Details always at artifact bottom
5. **Dividers** - Use `---` between each section
6. **User confirmation** - Note that user approved before creation
7. **No Table of Contents** - External tools handle this
8. **Success at top** - Immediately after title
9. **Problems integrated** - In About narrative

---

<a id="3-📄-section-dividers"></a>

## 3. 📄 SECTION DIVIDERS

### Horizontal Dividers (`---`)
**Use Between:**
- Title and Success Criteria/Metrics
- Success Criteria and About
- All major content sections
- Content and AI System footer
- Each footer section

### Doc Mode Separators (`---`)
**Use For:**
- Major document divisions
- Between main content areas
- Logical section breaks
- As specified in Doc template

### Spacing Rules:
- One blank line before divider
- One blank line after divider
- Exception: No blank line after final divider

### Example Structure:
```markdown
[SCOPE] Feature: [Name]

## ✦ Success Criteria
[Content]

---

# ⌘ About
[Integrated narrative with problems]

---

## ⌥ Designs & References
[Table format]

---

## ❖ Requirements
[Content]

---

### AI SYSTEM
[Footer details]
```

---

<a id="4-💎-professional-requirements"></a>

## 4. 💎 PROFESSIONAL REQUIREMENTS

### Language & Tone
- **Professional:** Clear, concise, actionable
- **Consistent:** Same voice throughout
- **Technical:** Precise terminology
- **Accessible:** Understandable to stakeholders
- **Strategic:** For PRDs, include business context

### Content Quality by Mode

**Ticket Mode:**
- Success criteria measurable at top
- Problems integrated in About
- Scope clearly labeled
- Resolution checklist scaled (4-6/8-12/12-20)
- Designs as table with placeholders

**PRD Mode:**
- Success metrics quantified at top
- Strategic context in About narrative
- Feature inventory complete (5-10/10-20/20+)
- Implementation phases defined
- Platform specifications clear

**Doc Mode:**
- Purpose clear in About
- Structure scaled to complexity
- References in table format
- `---` separators used appropriately
- Content appropriate for audience

### Visual Hierarchy (Updated v0.200-201)
- **H1 Headers:**
  - ⌘ - About section
  - ❖ - Main sections
- **H2 Headers:**
  - ◻︎ - Subsections
  - ✦ - Success Criteria/Metrics
  - ⌥ - Designs & References
  - ✔ - Resolution Checklist
  - ⌥ - References & Resources (Doc mode)
  - ∅ - Risks (when applicable)
- **H3 Headers:**
  - Clean text (no symbols)
  - Standard markdown formatting

### Critical Formatting Requirements

**Lists:**
- Always use `-` for bullet points
- Never use `*` or `•` or other bullets
- Checkboxes: `[]` format (no spaces)
- Each item on its own line

**Tables:**
- Always for Designs & References
- Always for metrics/KPIs
- Consistent column structure
- Placeholder links: `[Figma - to be added]`

**Content Integration:**
- Problems never listed separately
- Always woven into About narrative
- Success always positioned at top
- Status notes where applicable: `[Status note: "80% complete"]`

---

<a id="5-🎯-mode-template-references"></a>

## 5. 🎯 MODE TEMPLATE REFERENCES

### Ticket Mode
**Template:** `Product Owner - Template - Ticket Mode.md`
**Structure:**
1. [SCOPE] + Title
2. Success Criteria (✦) - At top
3. About (⌘) - Integrated problems
4. Designs & References (⌥) - Table
5. Requirements (❖) - Scaled
6. Resolution Checklist (✔) - Scaled items
7. Optional: Risks (∅) for Complex

**Scaling:**
- Simple: 2-3 sections, 4-6 resolution items
- Standard: 4-5 sections, 8-12 items
- Complex: 6-8 sections, 12-20 items

**Key Rules:**
- Use H1: ⌘/❖, H2: ◻︎/✦/⌥/✔, H3: clean
- Checkboxes: `[]` format
- NO TABLE OF CONTENTS
- Dividers between all sections

### PRD Mode
**Template:** `Product Owner - Template - PRD Mode.md`
**Structure:**
1. Title
2. Success Metrics (✦) - At top
3. About (⌘) - Strategic context
4. Designs & References (⌥) - Table
5. Scope & Features (❖) - Complete inventory
6. Technical Requirements (❖)
7. Implementation Plan (❖)
8. Optional: Risks (∅)

**Scaling:**
- Initiative: 5-10 features, quarterly
- Program: 10-20 features, half-year
- Strategic: 20+ features, annual

**Key Rules:**
- Use H1: ⌘/❖, H2: ✦/◻︎/⌥/∅, H3: clean
- Focus on implementation details
- Status notes where applicable
- NO TABLE OF CONTENTS

### Doc Mode
**Template:** `Product Owner - Template - Doc Mode.md`
**Structure:**
1. Title with metadata
2. About (⌘) - Purpose
3. References & Resources (⌥) - Table
4. Main sections (❖) - Scaled
5. Additional sections as needed

**Scaling:**
- Simple: 2-3 main sections
- Standard: 4-6 main sections
- Complex: 7+ main sections

**Key Rules:**
- Use H1: ⌘/❖, H2: ◻︎/⌥, H3: clean
- Use `---` for major separators
- Clear section hierarchy
- NO TABLE OF CONTENTS
- Line breaks for readability

---

<a id="6-✅-quality-checklist"></a>

## 6. ✅ QUALITY CHECKLIST

### Pre-Creation (Critical)
- [] User responded to thinking rounds?
- [] User responded to all mode questions?
- [] Complexity/scaling determined?
- [] Template version confirmed (v0.200-201)?
- [] All required inputs received?
- [] User made final selection?

### Content Validation

**Structure Check:**
- [] Success criteria/metrics at top?
- [] Problems integrated in About narrative?
- [] Correct artifact type (`text/markdown`)?
- [] AI System header at bottom?
- [] Thinking rounds documented?
- [] ATLAS phases noted?
- [] Scaling documented?
- [] NO TABLE OF CONTENTS?

**Symbol Hierarchy Validation:**
- [] H1: ⌘ for About sections?
- [] H1: ❖ for main sections?
- [] H2: ◻︎ for subsections?
- [] H2: ✦ for success criteria/metrics?
- [] H2: ⌥ for designs & references?
- [] H2: ✔ for resolution checklist (tickets)?
- [] H2: ⌥ for references (docs)?
- [] H2: ∅ for risks (when needed)?
- [] H3: Clean headers (no symbols)?

### Format Validation

**Lists & Tables:**
- [] Lists use `-` bullets?
- [] Checkboxes use `[]` format?
- [] Designs in table format?
- [] Placeholders added where needed?

**Dividers & Spacing:**
- [] `---` between all major sections?
- [] Proper spacing around dividers?
- [] No extra dividers?

### Mode-Specific Validation

**Tickets:**
- [] [SCOPE] label present?
- [] Resolution checklist scaled (4-6/8-12/12-20)?
- [] Requirements structured?
- [] Story format excludes checklist?

**PRDs:**
- [] Feature inventory complete (5-10/10-20/20+)?
- [] Implementation phases clear?
- [] Platform specifications included?
- [] Strategic value in About?

**Docs:**
- [] Complexity appropriate (2-3/4-6/7+)?
- [] Structure logical?
- [] References complete?
- [] Separators used correctly?

### Delivery Check
- [] Single artifact?
- [] No mixed content?
- [] User confirmation noted?
- [] Template compliance noted?
- [] Process transparent?
- [] NO TABLE OF CONTENTS?

---

<a id="7-🚨-error-recovery"></a>

## 7. 🚨 ERROR RECOVERY

### Common Errors & Fixes

#### Error: Wrong Symbol Hierarchy
**Detection:** H3 has symbols, or wrong H1/H2 symbols
**Recovery:**
1. Update hierarchy
2. H1: ⌘/❖ only
3. H2: ◻︎/✦/⌥/✔/⌥/∅
4. H3: Clean text only
5. Verify all headers updated

#### Error: Success Criteria Not at Top
**Detection:** Success buried in document
**Recovery:**
1. Move success section immediately after title
2. Add divider after success section
3. Ensure About follows success
4. Update all section positions

#### Error: Problems Listed Separately
**Detection:** Bullet list of problems instead of narrative
**Recovery:**
1. Rewrite About section
2. Weave problems into narrative
3. Include context and impact
4. Remove separate problem lists

#### Error: Wrong Scaling Applied
**Detection:** Section count doesn't match complexity
**Recovery:**
1. Identify correct scale (Simple/Standard/Complex)
2. Adjust section count (2-3/4-5/6-8)
3. Scale resolution items (4-6/8-12/12-20)
4. Update feature count for PRDs (5-10/10-20/20+)

#### Error: Table of Contents Included
**Detection:** ToC present in artifact
**Recovery:**
1. Remove entire ToC section
2. Ensure headers properly structured
3. Verify external tools can parse
4. Note: ClickUp/Jira handle navigation

#### Error: Created Without User Input
**Detection:** Artifact created before responses
**Recovery:**
1. Acknowledge critical error
2. Delete or modify based on preference
3. Restart with proper flow
4. Document violation

#### Error: Wrong Artifact Type
**Detection:** Used `text/plain` instead of `text/markdown`
**Recovery:**
1. Recreate with correct type
2. Preserve content
3. Verify formatting

#### Error: Missing AI System Footer
**Detection:** No process documentation
**Recovery:**
1. Add footer to existing artifact
2. Document all process steps
3. Include scaling applied
4. Note template version

### Prevention Strategies
1. **Always wait** for user input (except $quick)
2. **Check template version** for latest standards
3. **Verify symbol hierarchy** before creation
4. **Apply correct scaling** based on keywords
5. **Position success at top** always
6. **Integrate problems** in narrative
7. **Exclude ToC** - external tools handle
8. **Review against checklist** before delivery