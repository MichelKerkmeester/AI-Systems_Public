# Prompt - Artifact Standards & Templates - v0.114

Comprehensive artifact delivery standards for prompt engineering system with mandatory RCAF/CRAFT formatting, CLEAR scoring display, and multi-format support including Standard, JSON, and YAML.

## 📋 Table of Contents

1. [📦 DELIVERY STANDARDS](#-delivery-standards)
2. [📋 MANDATORY STRUCTURE & TEMPLATES](#-mandatory-structure--templates)
3. [🎯 STANDARD ARTIFACT TEMPLATE WITH CLEAR](#-standard-artifact-template-with-clear)
4. [📝 RCAF ARTIFACT TEMPLATE](#-rcaf-artifact-template)
5. [🔄 FORMAT-SPECIFIC TEMPLATES](#-format-specific-templates)
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
- Forget to show all format options

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
- Display all three format options (Standard/JSON/YAML)

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
• YAML format available (`$yaml`)

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
3. **Format Options** - All three alternatives with token impacts
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
• JSON format available (`$json`) - Structured for APIs (+5-10% tokens)
• YAML format available (`$yaml`) - Human-editable templates (+3-7% tokens)

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
- Format preference: [Standard/JSON/YAML usage %]
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
• JSON format (`$json`) - For API integration (+5-10% tokens)
• YAML format (`$yaml`) - For configuration templates (+3-7% tokens)

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
- Format distribution: Standard 60%, YAML 25%, JSON 15%
- Average CLEAR with RCAF: 43/50
```

---

<a id="-format-specific-templates"></a>

## 5. 🔄 FORMAT-SPECIFIC TEMPLATES

**For complete format specifications:**
- → **Prompt - JSON Format Guide.md**
- → **Prompt - YAML Format Guide.md**

### Standard Format Artifact

```markdown
Role: [expertise]
Context: [essential background]
Action: [specific task]
Format: [output requirements]

---

**Format:** Standard (Natural language)

---

**CLEAR Evaluation: 43/50 (Grade: A)**

• **Correctness:** 9/10 - Full accuracy
• **Logic/Coverage:** 8/10 - Complete coverage
• **Expression:** 10/10 - Maximum clarity
• **Arrangement:** 8/10 - Natural flow
• **Reuse:** 8/10 - Template ready

---

[AI System details...]
```

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
**Token Impact:** +5-10% overhead

---

**CLEAR Evaluation: 41/50 (Grade: A)**

• **Correctness:** 9/10 - Structured clarity
• **Logic/Coverage:** 8/10 - All elements present
• **Expression:** 7/10 - Less natural than standard
• **Arrangement:** 9/10 - Perfect structure
• **Reuse:** 8/10 - API-ready

---

[AI System details...]
```

### YAML Format Artifact with RCAF

```markdown
```yaml
role: [expertise]
context: [essential background]
action: [specific task]
format:
  structure: [output type]
  requirements:
    - requirement one
    - requirement two
```

---

**Format:** YAML (Optimized for human-editable templates)
**Token Impact:** +3-7% overhead

---

**CLEAR Evaluation: 42/50 (Grade: A)**

• **Correctness:** 8/10 - Clear structure
• **Logic/Coverage:** 8/10 - All elements present
• **Expression:** 8/10 - Readable hierarchy
• **Arrangement:** 9/10 - Clean organization
• **Reuse:** 9/10 - Template-optimized

---

[AI System details...]
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

- **Format Selected:** [Standard/JSON/YAML]
- **Token Overhead:** [Baseline/+X%]
- **Format Rationale:** [Why this format]

---

**Historical Context:**
- Framework success: RCAF [X]%, CRAFT [Y]%
- Format usage: Standard [X]%, JSON [Y]%, YAML [Z]%
- Average CLEAR scores: [X]/50
- Pattern note: [If relevant]
- User control: 100% maintained
```

### Formatting Rules
- Always use **bold** for headers
- Use dashes (-) for all bullet points
- Include CLEAR improvements
- Note framework selection reasoning
- Note format selection reasoning
- Display token impacts
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
━━━━━━━━━━━━━━━━━
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
Format: [Standard/JSON/YAML] (chosen for [reason])
━━━━━━━━━━━━━━━━━
```

### Framework & Format Comparison Display

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

**Format Analysis:**
┌─────────────┬──────────┬────────┬────────┬─────────┐
│ Aspect      │ Standard │ JSON   │ YAML   │ Choice  │
├─────────────┼──────────┼────────┼────────┼─────────┤
│ Readability │ 10/10    │ 7/10   │ 9/10   │ Std ✓   │
│ Structure   │ 7/10     │ 10/10  │ 9/10   │         │
│ Tokens      │ Baseline │ +5-10% │ +3-7%  │ Std ✓   │
│ Reusability │ 7/10     │ 9/10   │ 10/10  │         │
└─────────────┴──────────┴────────┴────────┴─────────┘
```

---

<a id="-quality-checklist"></a>

## 8. ✅ QUALITY CHECKLIST

### Artifact Requirements Checklist

- [ ] **Content First:** Enhanced prompt at top
- [ ] **Framework Clear:** RCAF or CRAFT identified
- [ ] **Format Options:** Standard, JSON, and YAML listed
- [ ] **Token Impacts:** Shown for each format
- [ ] **CLEAR Scores:** All 5 dimensions scored
- [ ] **Grade Shown:** Letter grade displayed
- [ ] **AI System Header:** Bold and at bottom
- [ ] **Thinking Rounds:** User selection documented
- [ ] **ATLAS Phases:** Processing documented
- [ ] **Challenge Applied:** Decision noted
- [ ] **Format Selection:** Choice and rationale shown
- [ ] **Pattern Context:** Historical data shown
- [ ] **Dividers Present:** Between major sections
- [ ] **Vertical Format:** Details use dashes
- [ ] **User Control:** All options shown

### Quality Gates

- [ ] **CLEAR ≥ 35/50:** Minimum quality met?
- [ ] **Expression ≥ 7/10:** Clear enough?
- [ ] **Framework Fit:** RCAF for simple, CRAFT for complex?
- [ ] **Format Appropriate:** Matches use case?
- [ ] **Token Overhead Acceptable:** Under 10% average?
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
| **Missing Format Options** | Only one shown | Show all three | User choice |
| **No Token Impact** | Format without overhead | Add percentages | Informed decision |

### REPAIR Protocol for Artifacts

```markdown
**R** - Recognize: Missing format options identified
**E** - Explain: Reduces user choice and transparency
**P** - Propose: Add all three format options with impacts
**A** - Apply: Include Standard/JSON/YAML
**I** - Iterate: Verify token percentages accurate
**R** - Record: Note for future prevention
```

---

<a id="-examples"></a>

## 10. 💡 EXAMPLES

### Example 1: Perfect RCAF Artifact with Format Options

```markdown
**Role:** Data scientist with machine learning expertise specializing in churn prediction.
**Context:** B2B SaaS platform with 10,000+ customers, 24-month historical data, 15% annual churn.
**Action:** Identify top 3 predictive factors for churn and recommend specific retention strategies.
**Format:** Executive report with visualizations and 3-5 actionable retention tactics.

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`) - For automated processing (+7% tokens)
• YAML format available (`$yaml`) - For template systems (+5% tokens)

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

- **Format Selected:** Standard
- **Token Overhead:** Baseline
- **Format Rationale:** Maximum clarity for human review

---

**Historical Context:**
- RCAF used 75% for data science prompts
- Format preference: Standard 60%, YAML 25%, JSON 15%
- Average CLEAR with RCAF: 43/50
- Framework preference established
- All options always available
```

### Example 2: YAML Format Selection

```markdown
```yaml
role: UX designer specializing in mobile app onboarding
context: Banking app for ages 25-45, requiring KYC compliance, targeting <20% drop-off
action:
  primary: Design intuitive 5-minute onboarding flow
  requirements:
    - ensure regulatory compliance
    - minimize friction points
format:
  type: user_flow_diagram
  include:
    - screen descriptions
    - success metrics
    - drop-off analysis
```

---

**Format Options:**
• Standard format - Natural language
• JSON format (`$json`) - API integration (+8% tokens)
• YAML format (shown above) - Template-ready (+4% tokens) ✓

---

**CLEAR Evaluation: 43/50 (Grade: A)**

• **Correctness:** 9/10 - Requirements complete
• **Logic/Coverage:** 8/10 - Full flow covered
• **Expression:** 8/10 - Clear hierarchy
• **Arrangement:** 9/10 - Logical structure
• **Reuse:** 9/10 - Perfect for templates ⭐

**Strong Framework:** RCAF delivers clarity in YAML format

---

**AI System:**

- **Framework:** ATLAS + RCAF
- **Mode:** $yaml
- **Complexity:** Medium

---

- **Thinking:** 4 rounds (user selected)
- **ATLAS:** A→T→L→A→S
- **Why RCAF:** Structured simplicity

---

- **Challenge:** Simplified from 10 steps to 5
- **Enhancement:** 25/50 → 43/50 (+18 points)
- **Context:** UX flow optimization

---

- **Format Selected:** YAML
- **Token Overhead:** +4%
- **Format Rationale:** Reusable template structure

---

**Session Learning:**
- YAML + RCAF = High reusability (9/10)
- Expression maintains 8/10 with YAML
- User prefers templates for UX flows
```

### Example 3: Format Comparison in Artifact

```markdown
**Role:** Marketing analyst with SEO expertise.
**Context:** Tech blog with 50K monthly visitors needing traffic growth.
**Action:** Audit content and identify top 5 improvement opportunities.
**Format:** Actionable report with priority rankings.

---

**Alternative Formats Available:**

**Standard (shown above):**
- Clarity: 10/10
- Tokens: Baseline
- Best for: Executive review

**JSON:**
```json
{
  "role": "Marketing analyst with SEO expertise",
  "context": "Tech blog with 50K monthly visitors needing traffic growth",
  "action": "Audit content and identify top 5 improvement opportunities",
  "format": "Actionable report with priority rankings"
}
```
- Structure: 10/10
- Tokens: +6%
- Best for: API integration

**YAML:**
```yaml
role: Marketing analyst with SEO expertise
context: Tech blog with 50K monthly visitors needing traffic growth
action: Audit content and identify top 5 improvement opportunities
format: Actionable report with priority rankings
```
- Readability: 9/10
- Tokens: +3%
- Best for: Template systems

---

**CLEAR Evaluation: 42/50 (Grade: A)**
[Standard format scores shown]

• **Correctness:** 9/10 - Complete requirements
• **Logic/Coverage:** 8/10 - All aspects covered
• **Expression:** 9/10 - Very clear
• **Arrangement:** 8/10 - Well structured
• **Reuse:** 8/10 - Adaptable

---

[AI System details...]
```

---

*Artifact excellence through systematic structure, RCAF clarity, and CLEAR transparency. Every artifact shows framework, scores, and improvement. All three format options (Standard/JSON/YAML) always presented with token impacts. AI System details always at bottom with proper formatting. Pattern context enriches without restricting. User control absolute. For complete format specifications, see Prompt - JSON Format Guide.md and Prompt - YAML Format Guide.md*