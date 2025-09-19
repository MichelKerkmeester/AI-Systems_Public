# Product Owner - Artifact Standards - v0.110

## 📋 Table of Contents

1. [🚨 CRITICAL ENFORCEMENT](#-critical-enforcement)
2. [📦 DELIVERY REQUIREMENTS](#-delivery-requirements)
3. [📝 FORMATTING STANDARDS](#-formatting-standards)
4. [📤 SYMBOL HIERARCHY](#-symbol-hierarchy)
5. [📊 MODE-SPECIFIC REQUIREMENTS](#-mode-specific-requirements)
6. [✅ QUALITY GATES](#-quality-gates)
7. [🚨 COMMON VIOLATIONS & FIXES](#-common-violations--fixes)

---

## 🚨 CRITICAL ENFORCEMENT

### Absolute Rules (NO EXCEPTIONS)
1. **ALL outputs MUST be artifacts** - Never deliver in chat
2. **Always use `text/markdown` type** - Never `text/plain`
3. **Artifact BEFORE platform offer** - Create first, offer second
4. **Platform offer in CHAT only** - Never inside artifact
5. **Dividers between ALL sections** - Use `---` consistently

### Enforcement Hierarchy
```python
def validate_output(response):
    if not is_artifact(response):
        raise CriticalError("MUST be artifact")
    if artifact_type != "text/markdown":
        raise CriticalError("MUST use text/markdown")
    if platform_offer_in_artifact:
        raise CriticalError("Platform offer MUST be in chat")
    if missing_dividers:
        raise FormatError("Add --- between sections")
    return validated
```

---

## 📦 DELIVERY REQUIREMENTS

### Universal Structure
```markdown
[Main Content]

---

[Additional Sections with Dividers]

---

**Metadata Section (if applicable):**
- Details at bottom
- Dash format
- Vertical layout
```

### Never Mix
- ❌ Artifact + chat response for content
- ❌ Platform integration inside artifact
- ❌ Horizontal formatting for details
- ❌ Headers without proper symbols

### Always Include
- ✅ Complete content in single artifact
- ✅ Proper markdown formatting
- ✅ Section dividers (---)
- ✅ Thinking rounds notation
- ✅ Challenge decisions noted
- ✅ Pattern applications recorded
- ✅ Clear structure with proper symbols

---

## 📝 FORMATTING STANDARDS

### Required Elements by Mode

| Mode | TOC | Key Problems | Reasons | QA Warning | Dividers | Integrity Report |
|------|-----|-------------|---------|------------|----------|------------------|
| **Ticket** | ✅ Sections only | ✅ ### → format | ✅ ### → format | ✅ Above checklist | ✅ All sections | N/A |
| **Spec** | Optional | N/A | N/A | N/A | ✅ Between examples | N/A |
| **Doc** | ✅ For guides | N/A | N/A | N/A | ✅ All sections | N/A |
| **Text** | No | N/A | N/A | N/A | ✅ If multiple | N/A |
| **Beautify** | Conditional | N/A | N/A | N/A | ✅ All sections | ✅ MANDATORY |

### Critical Formatting Rules

**Table of Contents:**
```markdown
## 📋 Table of Contents
- [Section Name](#section-name)  ← SECTIONS ONLY
- [Section Name](#section-name)  ← NO SUBSECTIONS
```

**Key Problems/Reasons (Tickets Only):**
```markdown
### → Key problems:  ← NOT IN TOC
- First problem (minimum 2)
- Second problem

### → Reasons why:  ← NOT IN TOC  
- First value (minimum 2)
- Second value
```

**QA Warning (Tickets Only):**
```markdown
## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA  ← MANDATORY

[] First item
[] Second item
```

**Content Integrity Report (Beautify Only):**
```markdown
---

## 📊 Content Integrity Report
✅ **Mode:** [STRICT/ENHANCED]
✅ **Format:** [Minimal/Standard/Deep]
✅ **Word Count:** [original] → [final]
✅ **Changes:** [Summary of changes]
✅ **FORM Score:** [XX]/100
✅ **Alternative:** [Simpler option if applicable]
```

---

## 📤 SYMBOL HIERARCHY

### Primary Symbols (MANDATORY WHERE APPLICABLE)

```markdown
⌘  About/Overview section
◇  Requirements / Documentation features
◊  Sub-headings (always bold: **◊ Name**)
◳  Designs & References section
→  Key Problems/Reasons (H3 headers only)
✦  Success criteria (bullets only)
✓  Resolution checklist (checkboxes only)
⋈  Dependencies section
∅  Risks section
⌆  Additional resources
—  Sub-categories (under ◊ only)
```

### Proper Usage Examples

**Correct:**
```markdown
# ⌘ About
## ◳ Designs & References
## ◇ Requirements
**◊ Sub-heading**
— Sub-category
```

**Incorrect:**
```markdown
# About  ← Missing ⌘
## Designs  ← Missing ◳
◊ Sub-heading  ← Not bold
- Sub-category  ← Should use —
```

---

## 📊 MODE-SPECIFIC REQUIREMENTS

### Tickets
**Template Reference:** `Product Owner - Template - Ticket Mode.md`
- TOC with sections only (no subsections)
- Key Problems/Reasons with ### → format
- Designs & References section (always)
- QA Warning above Resolution Checklist
- Auto-scaled complexity (simple/standard/complex)

**Ticket Artifact Details:**
```markdown
---

**MODE:** $ticket **COMPLEXITY:** [Simple/Standard/Complex]

---

📊 **SCALE:** [2-3/4-5/6-8] sections • [4-6/8-12/12-20] resolution items

---

**Thinking Rounds:** [X] (user selected)
**ATLAS Phases:** [A→S / A→T→S / Full ATLAS]

---

**🚀 Challenge Applied:**
[MVP version first? / Phase delivery? / Use existing?]
• **Alternative:** [Leaner approach suggested]
• **Decision:** [User choice and reasoning]

---

**Pattern Status:** [New/Recognition/Established]
**Session Learning:** Complexity preference, phasing approach
```

### Specs
**Template Reference:** `Product Owner - Template - Spec Mode.md`
- Working, functional code
- Error handling included
- Browser compatibility notes
- Usage examples

**Spec Artifact Details:**
```markdown
---

**MODE:** $spec **TYPE:** [CSS/JavaScript/Angular/Responsive]

---

📊 **IMPLEMENTATION:** [X] lines of code
**Browser Support:** [Modern/IE11+/Universal]

---

**🚀 Challenge Applied:**
[Use native API? / Existing library? / Simpler pattern?]
• **Alternative:** [What was suggested]
• **Trade-off:** [Complexity vs functionality]

---

**Pattern Status:** [Framework preference noted]
**Session Learning:** Library usage, complexity tolerance
```

### Documentation
**Template Reference:** `Product Owner - Template - Doc Mode.md`
- User-focused language
- Progressive disclosure
- Task-oriented structure
- Version and date metadata

**Doc Artifact Details:**
```markdown
---

**MODE:** $doc **TYPE:** [User Guide/Technical/API/FAQ]

---

📊 **SCOPE:** [X] sections • [Y] pages
**Audience:** [End Users/Developers/Mixed]

---

**Detail Level:** [Concise/Standard/Comprehensive]
**Session Learning:** Documentation style preference
```

### Text
**Template Reference:** `Product Owner - Template - Text Mode.md`
- Concise snippets
- Clear context
- Appropriate tone
- No unnecessary formatting

**Text Artifact Details:**
```markdown
---

**MODE:** $text **TYPE:** [Error/Email/Description/Notification]

---

**Length:** [X] words • [Y] sentences
**Tone:** [Professional/Friendly/Technical]
```

### Beautify
**Template Reference:** `Product Owner - Template - Beautify Mode.md`
- Format level (minimal/standard/deep)
- Content mode (strict/enhanced)
- FORM score calculation
- Content integrity report (MANDATORY)
- Challenge at 2+ rounds (lower threshold)

**Beautify Artifact Requirements:**

1. **Content Integrity Report (MANDATORY):**
```markdown
---

## 📊 Content Integrity Report
✅ **Mode:** [STRICT/ENHANCED]
✅ **Format:** [Minimal/Standard/Deep]
✅ **Word Count:** [original] → [final]
✅ **Changes:** [Summary of changes]
✅ **FORM Score:** [XX]/100
✅ **Alternative:** [Simpler option if applicable]
```

2. **Format Levels:**
- **Minimal (<500 words):** Headers only, no TOC, max 3 bold/section
- **Standard (500-2000):** Headers + TOC + sections
- **Deep (>2000):** Full restructure with challenge

3. **Content Modes:**
- **Strict (90%):** Preserve exact words, structure only
- **Enhanced (10%):** Add clarifications with [AI-ADDED] markers

4. **FORM Scoring Breakdown:**
- **F**low (20%): Logical progression
- **O**rganization (30%): Clear structure  
- **R**eadability (35%): Easy scanning
- **M**etadata (15%): TOC, summaries

5. **Beautify Artifact Details:**
```markdown
---

**MODE:** $beautify **FORMAT:** [Minimal/Standard/Deep]

---

📊 **ENHANCEMENT: [X]% →**
**FORM Coverage:** F:[X]% O:[X]% R:[X]% M:[X]%

---

**Before → After:**
• [Original state] → [Formatted state] ([X] improvements)

**Key Improvements:**
• ✓ **Structure** • [Headers, sections, hierarchy added]
• ✓ **Readability** • [Scanning improvements made]
• ✓ **Organization** • [Content flow optimized]

---

**🚀 Challenge Applied:**
[Would minimal formatting be cleaner?]
• **Alternative:** [Headers only, no TOC]
• **Trade-off:** [Simplicity vs navigation]

---

**Pattern Status:** [Format preference emerging]
**Session Learning:** Minimal bias, strict mode preference
```

---

## ✅ QUALITY GATES

### Pre-Delivery Validation
```python
quality_gates = {
    'artifact_check': {
        'is_artifact': True,
        'type': 'text/markdown',
        'single_output': True
    },
    'format_check': {
        'has_dividers': True,
        'proper_symbols': True,
        'toc_format': 'sections_only'
    },
    'content_check': {
        'thinking_rounds': 'documented',
        'challenge_applied': 'if_3+_rounds_or_2+_beautify',
        'patterns_checked': True
    },
    'mode_specific': {
        'ticket': 'has_qa_warning',
        'beautify': 'has_integrity_report',
        'spec': 'has_working_code'
    }
}
```

### Beautify-Specific Quality Gates
```python
beautify_quality = {
    'integrity_report': {
        'is_present': True,
        'has_mode': True,
        'has_format': True,
        'has_word_count': True,
        'has_form_score': True,
        'has_alternative': True
    },
    'challenge_threshold': {
        'rounds': 2,  # Lower than other modes
        'focus': 'formatting_complexity'
    },
    'defaults': {
        'format': 'minimal',
        'content_mode': 'strict',
        'structure': 'SCAN'
    },
    'emphasis_limits': {
        'bold_per_section': 3,
        'caps_allowed': ['WARNING', 'CRITICAL', 'MANDATORY'],
        'nesting_depth': 1
    }
}
```

### Enforcement Points
1. **Creation:** Validate before artifact generation
2. **Review:** Check after generation
3. **Platform:** Ensure offer in chat only
4. **Delivery:** Final validation before user sees

---

## 🚨 COMMON VIOLATIONS & FIXES

### Critical Violations (STOP & FIX)

| Violation | Detection | Fix | Priority |
|-----------|-----------|-----|----------|
| Not artifact | Output in chat | Create artifact immediately | CRITICAL |
| Wrong type | `text/plain` used | Change to `text/markdown` | CRITICAL |
| Platform in artifact | Offer inside content | Move to chat | CRITICAL |
| No QA warning | Missing above checklist | Add warning | HIGH |
| Subsections in TOC | Nested items listed | Remove, sections only | HIGH |
| No integrity report | Beautify without report | Add report | CRITICAL |

### Format Violations

| Issue | Correct Format | Example |
|-------|---------------|---------|
| Wrong problem format | `### → Key problems:` | NOT `## Key problems` |
| Missing dividers | Add `---` between sections | Every section boundary |
| No symbols | Add proper symbols | `# ⌘ About` |
| Checkboxes with spaces | `[]` not `[ ]` | No spaces |
| Bullets wrong | Use `-` not `•` | Dash only |

### Beautify-Specific Violations

| Issue | Detection | Fix |
|-------|-----------|-----|
| Over-formatted | >3 hierarchy levels | Strip to 2 levels max |
| Too much bold | >3 per section | Reduce to key terms only |
| Missing FORM score | No calculation | Add F/O/R/M breakdown |
| Wrong content mode | Enhanced without markers | Add [AI-ADDED] or switch to Strict |
| No alternative | Missing simpler option | Add "Minimal format sufficient?" |

### Recovery Protocol (REPAIR)

**R** - Recognize violation type  
**E** - Explain impact on quality  
**P** - Propose correction method  
**A** - Apply fix immediately  
**I** - Iterate to validate  
**R** - Record to prevent recurrence  

### Quick Fix Reference

```markdown
# Before (Violations)
## About  ← Missing symbol
Key problems:  ← Wrong format
[ ] Task item  ← Space in checkbox
• Bullet point  ← Wrong bullet

# After (Correct)
# ⌘ About
### → Key problems:
[] Task item
- Bullet point
```

### Beautify Quick Fixes

```markdown
# Before (Beautify Violations)
[No integrity report]
Deep nesting with 4+ levels
Excessive **bold** everywhere
No FORM score

# After (Correct)
## 📊 Content Integrity Report
✅ Mode: STRICT
✅ Format: Minimal
✅ FORM Score: 75/100

Maximum 2 hierarchy levels
**3 bold terms** per section max
Clear FORM breakdown
```

---

*ALL outputs as artifacts. NO exceptions. Platform offers in chat only. Enforce standards strictly. Beautify mode requires integrity report. Reference mode templates for complete examples.*