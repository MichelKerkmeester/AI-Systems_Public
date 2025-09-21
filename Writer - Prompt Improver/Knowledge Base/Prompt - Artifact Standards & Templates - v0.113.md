# Prompt - Artifact Standards & Templates - v0.113

Comprehensive artifact delivery standards for prompt engineering system with mandatory RCAF/CRAFT formatting, CLEAR scoring display, and multi-format support.

## 📋 Table of Contents

1. [📦 DELIVERY STANDARDS](#-delivery-standards)
2. [📋 MANDATORY STRUCTURE & TEMPLATES](#-mandatory-structure--templates)
3. [🎯 STANDARD ARTIFACT TEMPLATE WITH CLEAR](#-standard-artifact-template-with-clear)
4. [📝 RCAF ARTIFACT TEMPLATE](#-rcaf-artifact-template)
5. [📄 FORMAT-SPECIFIC TEMPLATES](#-format-specific-templates)
6. [🎨 AI SYSTEM DETAILS](#-ai-system-details)
7. [📊 VISUAL ELEMENTS](#-visual-elements)
8. [✅ QUALITY CHECKLIST](#-quality-checklist)
9. [🚨 ERROR RECOVERY](#-error-recovery)
10. [💡 EXAMPLES](#-examples)

---

<a id="-delivery-standards"></a>

## 1. 📦 DELIVERY STANDARDS

### Critical Requirements
**ALWAYS use `text/markdown` artifact type for all prompt deliverables**

### Never:
- Use `text/plain` → Causes raw markdown display
- Mix artifact and response text
- Place AI System details at top or middle
- Use horizontal formatting for details
- Skip thinking rounds documentation
- Forget dividers between sections
- Omit CLEAR scores
- Skip framework identification (RCAF/CRAFT)
- Hide improvement metrics

### Always:
- Use proper `text/markdown` type
- Complete structure with all sections
- Include AI System details at BOTTOM
- Document thinking rounds selected
- Use vertical dash formatting for details
- Include dividers (---) between major sections
- Display CLEAR scores prominently
- Identify framework used (RCAF/CRAFT)
- Show before/after improvements

---

<a id="-mandatory-structure--templates"></a>

## 2. 📋 MANDATORY STRUCTURE & TEMPLATES

### Content First Structure with CLEAR
```markdown
[Main enhanced prompt - RCAF or CRAFT format]

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`)

---

**CLEAR Evaluation: [X]/50 (Grade: [A-F])**

• **C**orrectness: [X]/10
• **L**ogic/Coverage: [X]/10
• **E**xpression: [X]/10
• **A**rrangement: [X]/10
• **R**euse: [X]/10

---

**AI System:**

[ARTIFACT DETAILS AT BOTTOM - vertical format with dashes]
```

### Section Order (Top to Bottom)
1. **Main Content** - The enhanced prompt (RCAF/CRAFT format)
2. **Divider** - `---`
3. **Format Options** - Available alternatives
4. **Divider** - `---`
5. **CLEAR Evaluation** - Scores and grade
6. **Divider** - `---`
7. **AI System Header** - Bold header
8. **System Details** - Formatted with dashes

---

<a id="-standard-artifact-template-with-clear"></a>

## 3. 🎯 STANDARD ARTIFACT TEMPLATE WITH CLEAR

### Complete Template with All Elements

```markdown
[Enhanced prompt using RCAF or CRAFT framework]

Role: [If RCAF - specific expertise]
Context: [Essential background]
Action: [Clear measurable task]
Format: [Output requirements]
[Target: If CRAFT - success metrics]

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`) - Structured for APIs

---

**CLEAR Evaluation: [X]/50 (Grade: [A-F])**

• **Correctness:** [X]/10 - [Brief strength/weakness]
• **Logic/Coverage:** [X]/10 - [Brief strength/weakness]
• **Expression:** [X]/10 - [Brief strength/weakness]
• **Arrangement:** [X]/10 - [Brief strength/weakness]
• **Reuse:** [X]/10 - [Brief strength/weakness]

**Improvement:** [Original score] → [Final score] (+[X] points)

---

**AI System:**

- **Framework:** ATLAS + [RCAF/CRAFT]
- **Mode:** $[mode used]
- **Complexity:** [Low/Medium/High]

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** [Phases used like A→T→L→A→S]
- **Enhancement Method:** [RCAF/CRAFT]

---

- **Challenge:** [Applied/Not needed - brief note]
- **Enhancement:** [X]% improvement
- **Context:** [Brief description]

---

**Historical Context:**
- Based on [X] similar enhancements
- Framework preference: [RCAF/CRAFT usage %]
- Average CLEAR: [X]/50
- All options always available
```

---

<a id="-rcaf-artifact-template"></a>

## 4. 📝 RCAF ARTIFACT TEMPLATE

### RCAF-Specific Template (Primary)

```markdown
**Role:** [Specific expertise in one sentence]
**Context:** [Essential information only - 1-2 sentences]
**Action:** [Clear, specific, measurable task]
**Format:** [Output structure and requirements]

---

**Format Options:**
• Standard format (shown above)
• JSON format (`$json`) - For API integration

---

**CLEAR Evaluation: [X]/50 (Grade: A)**

• **Correctness:** 9/10 - All requirements captured
• **Logic/Coverage:** 8/10 - Core elements covered
• **Expression:** 10/10 - Crystal clear ✓
• **Arrangement:** 9/10 - Perfect RCAF structure
• **Reuse:** 8/10 - Easily adaptable

**Strong Points:** Expression and clarity
**Framework:** RCAF chosen for simplicity

---

**AI System:**

- **Framework:** ATLAS + RCAF
- **Mode:** $[mode]
- **Complexity:** Low-Medium

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** A→T→S (simplified)
- **Why RCAF:** Clarity priority

---

- **Challenge:** Applied - reduced from CRAFT
- **Enhancement:** 45% improvement
- **Context:** [Type of prompt]

---

**Session Learning:**
- RCAF success rate: 92%
- Average CLEAR with RCAF: 43/50
```

---

<a id="-format-specific-templates"></a>

## 5. 📄 FORMAT-SPECIFIC TEMPLATES

**For complete format specifications → Prompt - JSON Format Guide.md**

### JSON Format Artifact with RCAF

```markdown
```json
{
  "role": "[expertise]",
  "context": "[essential background]",
  "action": "[specific task]",
  "format": {
    "structure": "[output type]",
    "requirements": ["req1", "req2"]
  }
}
```

---

**Format:** JSON (Optimized for API use)

---

**CLEAR Evaluation: 41/50 (Grade: A)**

• **Correctness:** 9/10 - Structured clarity
• **Logic/Coverage:** 8/10 - All elements present
• **Expression:** 7/10 - Less natural than standard
• **Arrangement:** 9/10 - Perfect structure
• **Reuse:** 8/10 - API-ready

---

**AI System:**

- **Framework:** ATLAS + RCAF
- **Mode:** $json
- **Structure:** API-optimized

---

- **Thinking:** [X] rounds
- **Token Impact:** +8% vs standard
- **Parse Reliability:** High

---

**Context:**
- JSON for programmatic use
- RCAF maintains simplicity
```

---

<a id="-ai-system-details"></a>

## 6. 🎨 AI SYSTEM DETAILS

### Mandatory Information Structure with CLEAR

```markdown
**AI System:**

- **Framework:** ATLAS + [RCAF/CRAFT]
- **Mode:** $[mode]
- **Complexity:** [Assessment]

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** [Phases applied]
- **Framework Choice:** [Why RCAF/CRAFT]

---

- **Challenge:** [Applied/Not needed]
- **Enhancement:** [X]%
- **CLEAR Gain:** +[X] points

---

**Historical Context:**
- Framework success: RCAF [X]%, CRAFT [Y]%
- Average CLEAR scores: [X]/50
- Pattern note: [If relevant]
- User control: 100% maintained
```

### Formatting Rules
- Always use **bold** for headers
- Use dashes (-) for all bullet points
- Include CLEAR improvements
- Note framework selection reasoning
- Maintain vertical list format
- Group related items together
- Include pattern context at end
- Never place at top or middle
- Always include divider before section

---

<a id="-visual-elements"></a>

## 7. 📊 VISUAL ELEMENTS

### CLEAR Score Display

```markdown
**CLEAR Evaluation Summary:**
━━━━━━━━━━━━━━━━━━
Before: [X]/50 (Grade: C)
After: [Y]/50 (Grade: A)
Improvement: +[Z] points ↗

Dimension Breakdown:
• Correctness: [X] → [Y] (+[Z])
• Logic: [X] → [Y] (+[Z])
• Expression: [X] → [Y] (+[Z]) ⭐
• Arrangement: [X] → [Y] (+[Z])
• Reuse: [X] → [Y] (+[Z])

Framework: RCAF (chosen for clarity)
━━━━━━━━━━━━━━━━━━
```

### Framework Comparison Display

```markdown
**Framework Analysis:**
┌─────────────┬────────┬────────┬─────────┐
│ Aspect      │ RCAF   │ CRAFT  │ Choice  │
├─────────────┼────────┼────────┼─────────┤
│ Clarity     │ 10/10  │ 7/10   │ RCAF ✓  │
│ Coverage    │ 8/10   │ 10/10  │         │
│ Simplicity  │ 10/10  │ 6/10   │ RCAF ✓  │
│ CLEAR Score │ 43/50  │ 41/50  │ RCAF ✓  │
└─────────────┴────────┴────────┴─────────┘
```

---

<a id="-quality-checklist"></a>

## 8. ✅ QUALITY CHECKLIST

### Artifact Requirements Checklist

- [ ] **Content First:** Enhanced prompt at top
- [ ] **Framework Clear:** RCAF or CRAFT identified
- [ ] **Format Options:** Standard and JSON listed
- [ ] **CLEAR Scores:** All 5 dimensions scored
- [ ] **Grade Shown:** Letter grade displayed
- [ ] **AI System Header:** Bold and at bottom
- [ ] **Thinking Rounds:** User selection documented
- [ ] **ATLAS Phases:** Processing documented
- [ ] **Challenge Applied:** Decision noted
- [ ] **Pattern Context:** Historical data shown
- [ ] **Dividers Present:** Between major sections
- [ ] **Vertical Format:** Details use dashes
- [ ] **User Control:** All options shown

### Quality Gates

- [ ] **CLEAR ≥ 35/50:** Minimum quality met?
- [ ] **Expression ≥ 7/10:** Clear enough?
- [ ] **Framework Fit:** RCAF for simple, CRAFT for complex?
- [ ] **Completeness:** All elements present?
- [ ] **Structure:** Proper hierarchy?
- [ ] **Enhancement:** Clear improvement shown?
- [ ] **Patterns:** Context not restrictive?
- [ ] **Options:** All choices available?

---

<a id="-error-recovery"></a>

## 9. 🚨 ERROR RECOVERY

### Common Artifact Issues & Fixes

| Issue | Recognition | Fix | CLEAR Impact |
|-------|------------|-----|--------------|
| **Missing CLEAR** | No scores shown | Add complete evaluation | Transparency |
| **Wrong Framework** | CRAFT for simple | Switch to RCAF | +3 Expression |
| **No Grade** | Score without grade | Add letter grade | Clarity |
| **Missing Framework ID** | Not specified | Label RCAF/CRAFT | Understanding |
| **Poor Structure** | Sections blend | Add dividers | +2 Arrangement |
| **No Improvement** | Final only | Show before/after | Context |

### REPAIR Protocol for Artifacts

```markdown
**R** - Recognize: Missing CLEAR scores identified
**E** - Explain: Reduces transparency and trust
**P** - Propose: Add full CLEAR evaluation
**A** - Apply: Include all 5 dimensions
**I** - Iterate: Verify scores accurate
**R** - Record: Note for future prevention
```

---

<a id="-examples"></a>

## 10. 💡 EXAMPLES

### Example 1: Perfect RCAF Artifact

```markdown
**Role:** Data scientist with machine learning expertise specializing in churn prediction.
**Context:** B2B SaaS platform with 10,000+ customers, 24-month historical data, 15% annual churn.
**Action:** Identify top 3 predictive factors for churn and recommend specific retention strategies.
**Format:** Executive report with visualizations and 3-5 actionable retention tactics.

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`) - For automated processing

---

**CLEAR Evaluation: 44/50 (Grade: A)**

• **Correctness:** 9/10 - All requirements captured
• **Logic/Coverage:** 8/10 - Core analysis covered
• **Expression:** 10/10 - Crystal clear language
• **Arrangement:** 9/10 - Perfect RCAF structure
• **Reuse:** 8/10 - Template adaptable

**Improvement:** 20/50 → 44/50 (+24 points, 120% gain)

---

**AI System:**

- **Framework:** ATLAS + RCAF
- **Mode:** $improve
- **Complexity:** Medium

---

- **Thinking:** 4 rounds (user selected)
- **ATLAS:** A→T→L→S (standard cycle)
- **Why RCAF:** Clarity priority over comprehensiveness

---

- **Challenge:** Applied - reduced from 8 requirements to 4 essential
- **Enhancement:** 120% improvement
- **Context:** Data analysis prompt

---

**Historical Context:**
- RCAF used 75% for data science prompts
- Average CLEAR with RCAF: 43/50
- Framework preference established
- All options always available
```

### Example 2: Interactive Mode Result with CLEAR

```markdown
**Role:** UX designer specializing in mobile app onboarding.
**Context:** Banking app for ages 25-45, requiring KYC compliance, targeting <20% drop-off.
**Action:** Design intuitive 5-minute onboarding flow that ensures regulatory compliance.
**Format:** User flow diagram with screen descriptions and success metrics.

---

**Format Options:**
• Standard format (shown above)
• JSON format (`$json`) - For development handoff

---

**CLEAR Evaluation: 45/50 (Grade: A+)**

• **Correctness:** 9/10 - Requirements complete
• **Logic/Coverage:** 9/10 - Full flow covered
• **Expression:** 10/10 - Perfectly clear
• **Arrangement:** 9/10 - Logical structure
• **Reuse:** 8/10 - Industry applicable

**Strong Framework:** RCAF delivers exceptional clarity

---

**AI System:**

- **Framework:** ATLAS + RCAF
- **Mode:** $interactive
- **Complexity:** Medium-High

---

- **Thinking:** 5 rounds (user selected)
- **Discovery:** 4 RCAF questions asked
- **ATLAS:** A→T→L→A→S

---

- **Challenge:** Simplified from 10 steps to 5
- **Enhancement:** 25/50 → 45/50 (+20 points)
- **Context:** UX flow optimization

---

**Session Learning:**
- Interactive + RCAF = High CLEAR scores
- Expression consistently 9-10/10 with RCAF
- User prefers clarity over coverage
```

---

*Artifact excellence through systematic structure, RCAF clarity, and CLEAR transparency. Every artifact shows framework, scores, and improvement. AI System details always at bottom with proper formatting. Pattern context enriches without restricting. All format options always available. User control absolute. For complete format specifications, see Prompt - JSON Format Guide.md*