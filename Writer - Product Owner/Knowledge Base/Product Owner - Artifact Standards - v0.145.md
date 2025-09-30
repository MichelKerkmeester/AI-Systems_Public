# Product Owner - Artifact Standards - v0.145

## 📋 TABLE OF CONTENTS
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
- **AUTOMATIC ULTRATHINK:** Apply 10 rounds for standard, 1-5 auto-scaled for $quick
- **NEVER create artifact until user responds to comprehensive question**
- **NO TABLE OF CONTENTS** - ClickUp/Jira provide native TOC functionality
- **HEADER AT TOP:** System metadata appears as first line of artifact

**Template Compliance:**
- Use templates v0.xxx exactly
- Symbol hierarchy: H1 (⌘/❖), H2 (◻︎/✦/⌥/✓/⌥/∅), H3: clean, H4: clean
- About section always first (after header)
- Success criteria/metrics after About
- Problems integrated in About narrative
- Designs & References as tables

**Scaling Requirements:**
- **Tickets:** Simple (2-3 sections, 4-6 resolution), Standard (4-5, 8-12), Complex (6-8, 12-20)
- **PRDs:** Initiative (5-10 features), Program (10-20), Strategic (20+)
- **Docs:** Simple (2-3 sections), Standard (4-6), Complex (7+)

**Thinking Requirements:**
- **Standard modes:** 10-round ultrathink automatic
- **Quick mode:** 1-5 rounds auto-scaled
- **No user choice:** System determines depth
- **Document in header:** Note mode and template applied

### Never:
- Use `text/plain` → Causes raw markdown display
- Mix artifact and response text
- Ask about thinking rounds (automatic now)
- Place artifact details at bottom or middle
- Use horizontal formatting for details
- Skip ATLAS phase documentation
- Hide process transparency
- **Create before user responds to comprehensive question**
- **Include Table of Contents**
- **Use H3/H4 symbols**
- **Put Success Criteria at top**
- **Place header at bottom**

### Always:
- Use proper `text/markdown` type
- Document mode and scaling applied
- Use dash bullet formatting vertically
- Note template version compliance
- Apply ultrathink consistently
- **Wait for user input on content (not thinking)**
- **Position About first (after header)**
- **Position Success Criteria after About**
- **Integrate problems in About**
- **Use clean H3/H4 headers**
- **Place header at top of artifact**

---

<a id="2-📋-mandatory-structure--format"></a>

## 2. 📋 MANDATORY STRUCTURE & FORMAT

### Universal Artifact Format For All Modes

**🚨 ONLY CREATE AFTER USER HAS RESPONDED TO COMPREHENSIVE QUESTION**

```markdown
Mode: $[mode] | Complexity: [level] | Template: v0.xxx
---
[Main content - ticket/PRD/doc with template v0.xxx structure]
```

### Structure Order Requirements:

**For Tickets/Stories:**
1. Header (Mode | Complexity | Template)
2. Title with [SCOPE]
3. About (⌘) - Context and integrated problems
4. Success Criteria (✦) - Measurable outcomes
5. Designs & References (⌥) - Table format
6. Requirements (❖) - Specifications
7. Resolution Checklist (✓) - If ticket

**For PRDs:**
1. Header (Mode | Complexity | Template)
2. Title
3. About (⌘) - Strategic context
4. Success Metrics (✦) - Business/product metrics
5. Designs & References (⌥) - Table format
6. Scope & Features (❖) - Feature inventory
7. Technical Requirements (❖)
8. Implementation Plan (❖)
9. Risks (∅) - When applicable

**For Docs:**
1. Header (Mode | Complexity | Template)
2. Title with metadata
3. About (⌘) - Purpose and context
4. References & Resources (⌥) - Table format
5. Main sections (❖) - Content areas

### Mode-Specific Complexity Labels:
- **Ticket Mode:** Simple/Standard/Complex (2-3/4-5/6-8 sections)
- **PRD Mode:** Initiative/Program/Strategic (5-10/10-20/20+ features)
- **Doc Mode:** Simple/Standard/Complex (2-3/4-6/7+ sections)
- **Quick Mode:** Shows "Auto-scaled" with detected level

### Symbol Hierarchy:
- **H1:** ⌘ (About), ❖ (Main sections)
- **H2:** ◻︎ (Subsections), ✦ (Success), ⌥ (Designs), ✓ (Checklist), ⌥ (References), ∅ (Risks)
- **H3:** Clean headers (no symbols)
- **H4:** Clean headers (no symbols)

### Formatting Rules:
1. **Header at top** - Single line with essential info
2. **Dash bullets** - Use `-` not `*` or `•`
3. **Vertical layout** - Never horizontal lists
4. **Top placement** - Header always at artifact top
5. **Dividers** - Use `---` between header and content, and between sections
6. **User confirmation** - Note user approved content
7. **No Table of Contents** - External tools handle this
8. **About first** - Always start with context (after header)
9. **Success after About** - Never at document top
10. **Problems integrated** - In About narrative

---

<a id="3-📄-section-dividers"></a>

## 3. 📄 SECTION DIVIDERS

### Horizontal Dividers (`---`)
**Use Between:**
- Header and title
- Title and About section
- About and Success Criteria/Metrics
- Success Criteria and Designs & References
- All major content sections

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

### Example Structure (Correct Order):
```markdown
Mode: $ticket | Complexity: Standard | Template: v0.145
---
[SCOPE] Feature: [Name]

# ⌘ About
[Integrated narrative with problems]

---

## ✦ Success Criteria
[Content - positioned AFTER About]

---

## ⌥ Designs & References
[Table format]

---

## ❖ Requirements
[Content]
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
- Header at top with mode info
- About section first with integrated problems
- Success criteria measurable (after About)
- Scope clearly labeled
- Resolution checklist scaled (4-6/8-12/12-20)
- Designs as table with placeholders
- **10-round ultrathink applied**

**PRD Mode:**
- Header at top with scale info
- About section first with strategic context
- Success metrics quantified (after About)
- Feature inventory complete (5-10/10-20/20+)
- Implementation phases defined
- Platform specifications clear
- **10-round ultrathink applied**

**Doc Mode:**
- Header at top with complexity
- About section first with purpose
- Structure scaled to complexity
- References in table format
- `---` separators used appropriately
- Content appropriate for audience
- **10-round ultrathink applied**

### Visual Hierarchy
- **H1 Headers:**
  - ⌘ - About section
  - ❖ - Main sections
- **H2 Headers:**
  - ◻︎ - Subsections
  - ✦ - Success Criteria/Metrics
  - ✓ - Resolution Checklist
  - ⌥ - Designs & References (All Modes)
  - ∅ - Risks (when applicable)
- **H3 Headers:**
  - Clean text (no symbols)
  - Standard markdown formatting
- **H4 Headers:**
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
- Placeholder links: `[Link - to be added]`

**Content Integration:**
- Problems never listed separately
- Always woven into About narrative
- Success positioned after About (not at top)
- Status notes where applicable: `[Status note: "80% complete"]`

**Header Documentation:**
- Always note mode, complexity, and template
- Single line format at top
- Never mention user choice (doesn't exist)

---

<a id="5-🎯-mode-template-references"></a>

## 5. 🎯 MODE TEMPLATE REFERENCES

### Ticket Mode
**Template:** `Product Owner - Template - Ticket Mode.md`
**Structure:**
1. Header (Mode | Complexity | Template)
2. [SCOPE] + Title
3. About (⌘) - Integrated problems (FIRST)
4. Success Criteria (✦) - Measurable (AFTER About)
5. Designs & References (⌥) - Table
6. Requirements (❖) - Scaled
7. Resolution Checklist (✓) - Scaled items
8. Optional: Risks (∅) for Complex

**Scaling:**
- Simple: 2-3 sections, 4-6 resolution items
- Standard: 4-5 sections, 8-12 items
- Complex: 6-8 sections, 12-20 items

**Thinking:**
- Standard mode: 10 rounds automatic
- Quick mode: 1-5 rounds auto-scaled

**Key Rules:**
- Header at top
- Use H1: ⌘/❖, H2: ◻︎/✦/⌥/✓, H3: clean, H4: clean
- Checkboxes: `[]` format
- NO TABLE OF CONTENTS
- Dividers between all sections
- Ultrathink applied automatically
- **About first, Success after**

### PRD Mode
**Template:** `Product Owner - Template - PRD Mode.md`
**Structure:**
1. Header (Mode | Scale | Template)
2. Title
3. About (⌘) - Strategic context (FIRST)
4. Success Metrics (✦) - Metrics (AFTER About)
5. Designs & References (⌥) - Table
6. Scope & Features (❖) - Complete inventory
7. Technical Requirements (❖)
8. Implementation Plan (❖)
9. Optional: Risks (∅)

**Scaling:**
- Initiative: 5-10 features, quarterly
- Program: 10-20 features, half-year
- Strategic: 20+ features, annual

**Thinking:**
- Standard mode: 10 rounds automatic
- Quick mode: 1-5 rounds auto-scaled

**Key Rules:**
- Header at top
- Use H1: ⌘/❖, H2: ✦/◻︎/⌥/∅, H3: clean, H4: clean
- Focus on implementation details
- Status notes where applicable
- NO TABLE OF CONTENTS
- Ultrathink applied automatically
- **About first, Success after**

### Doc Mode
**Template:** `Product Owner - Template - Doc Mode.md`
**Structure:**
1. Header (Mode | Complexity | Template)
2. Title with metadata
3. About (⌘) - Purpose (FIRST)
4. References & Resources (⌥) - Table
5. Main sections (❖) - Scaled
6. Additional sections as needed

**Scaling:**
- Simple: 2-3 main sections
- Standard: 4-6 main sections
- Complex: 7+ main sections

**Thinking:**
- Standard mode: 10 rounds automatic
- Quick mode: 1-5 rounds auto-scaled

**Key Rules:**
- Header at top
- Use H1: ⌘/❖, H2: ◻︎/⌥, H3: clean, H4: clean
- Use `---` for major separators
- Clear section hierarchy
- NO TABLE OF CONTENTS
- Line breaks for readability
- Ultrathink applied automatically
- **About first always**

---

<a id="6-✅-quality-checklist"></a>

## 6. ✅ QUALITY CHECKLIST

### Pre-Creation (Critical)
- [] Ultrathink applied automatically? (10 rounds standard, 1-5 quick)
- [] User responded to comprehensive question? (not thinking)
- [] Complexity/scaling determined?
- [] Template version confirmed (v0.xxx)?
- [] All required inputs received from single response?
- [] User made final content selection?

### Content Validation

**Structure Check:**
- [] Header at top with mode/complexity/template?
- [] About section positioned FIRST (after header)?
- [] Success criteria/metrics AFTER About?
- [] Problems integrated in About narrative?
- [] Correct artifact type (`text/markdown`)?
- [] Scaling documented in header?
- [] NO TABLE OF CONTENTS?

**Symbol Hierarchy Validation:**
- [] H1: ⌘ for About sections?
- [] H1: ❖ for main sections?
- [] H2: ◻︎ for subsections?
- [] H2: ✦ for success criteria/metrics?
- [] H2: ⌥ for designs & references?
- [] H2: ✓ for resolution checklist (tickets)?
- [] H2: ⌥ for references (docs)?
- [] H2: ∅ for risks (when needed)?
- [] H3: Clean headers (no symbols)?
- [] H4: Clean headers (no symbols)?

**Position Validation:**
- [] Header is first line?
- [] About is first major section (after header)?
- [] Success comes after About?
- [] Designs after Success?
- [] Requirements follow logical flow?

### Format Validation

**Lists & Tables:**
- [] Lists use `-` bullets?
- [] Checkboxes use `[]` format?
- [] Designs in table format?
- [] Placeholders added where needed?

**Dividers & Spacing:**
- [] `---` between header and content?
- [] `---` between all major sections?
- [] Proper spacing around dividers?
- [] No extra dividers?

### Mode-Specific Validation

**Tickets:**
- [] Header at top?
- [] [SCOPE] label present?
- [] About first with integrated problems?
- [] Success Criteria after About?
- [] Resolution checklist scaled (4-6/8-12/12-20)?
- [] Requirements structured?
- [] Story format excludes checklist?
- [] 10-round ultrathink applied?

**PRDs:**
- [] Header at top?
- [] About first with strategic context?
- [] Success Metrics after About?
- [] Feature inventory complete (5-10/10-20/20+)?
- [] Implementation phases clear?
- [] Platform specifications included?
- [] 10-round ultrathink applied?

**Docs:**
- [] Header at top?
- [] About first with purpose?
- [] Complexity appropriate (2-3/4-6/7+)?
- [] Structure logical?
- [] References complete?
- [] Separators used correctly?
- [] 10-round ultrathink applied?

### Delivery Check
- [] Single artifact?
- [] No mixed content?
- [] User confirmation noted (for content)?
- [] Template compliance noted?
- [] Process transparent?
- [] NO TABLE OF CONTENTS?
- [] Success positioned correctly (after About)?
- [] Header at top?

---

<a id="7-🚨-error-recovery"></a>

## 7. 🚨 ERROR RECOVERY

### Common Errors & Fixes

#### Error: Wrong Symbol Hierarchy
**Detection:** H3 or H4 has symbols, or wrong H1/H2 symbols
**Recovery:**
1. Update hierarchy
2. H1: ⌘/❖ only
3. H2: ◻︎/✦/⌥/✓/∅
4. H3: Clean text only
5. H4: Clean text only
6. Verify all headers updated

#### Error: Success Criteria at Top (Wrong Position)
**Detection:** Success positioned before About section
**Recovery:**
1. Move About section to first position (after header)
2. Position Success Criteria immediately after About
3. Add divider between About and Success
4. Update all subsequent sections
5. Verify correct flow

#### Error: About Section Not First
**Detection:** Other sections appear before About (after header)
**Recovery:**
1. Move About to first position after header
2. Reorder all sections appropriately
3. Ensure Success follows About
4. Update dividers

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
**Detection:** Artifact created before single response
**Recovery:**
1. Acknowledge critical error
2. Delete or modify based on preference
3. Restart with comprehensive question
4. Document violation

#### Error: Wrong Artifact Type
**Detection:** Used `text/plain` instead of `text/markdown`
**Recovery:**
1. Recreate with correct type
2. Preserve content
3. Verify formatting

#### Error: Header at Bottom
**Detection:** System metadata at bottom instead of top
**Recovery:**
1. Move header to top of artifact
2. Add divider after header
3. Preserve all content
4. Verify formatting

### Prevention Strategies
1. **Apply ultrathink automatically** (10 rounds standard, 1-5 quick)
2. **Never ask thinking questions** to users
3. **Wait for comprehensive response** (except $quick)
4. **Check template version** for latest standards
5. **Verify symbol hierarchy** before creation
6. **Apply correct scaling** based on keywords
7. **Position About first** (after header) always
8. **Position Success after About** always
9. **Integrate problems** in narrative
10. **Exclude ToC** - external tools handle
11. **Include header at top** for tracking
12. **Place header at top** of artifact