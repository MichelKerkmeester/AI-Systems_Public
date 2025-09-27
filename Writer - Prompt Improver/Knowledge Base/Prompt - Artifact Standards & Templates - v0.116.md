# Prompt - Artifact Standards & Templates - v0.116

Comprehensive artifact delivery standards for prompt engineering system with automatic ultrathink processing, MANDATORY artifact delivery, RCAF/CRAFT formatting, CLEAR scoring display, and multi-format support including Standard, JSON, and YAML.

## 📋 Table of Contents

1. [📴 CRITICAL REQUIREMENTS](#-critical-requirements)
2. [📦 DELIVERY STANDARDS](#-delivery-standards)
3. [📋 MANDATORY STRUCTURE & TEMPLATES](#-mandatory-structure--templates)
4. [🎯 STANDARD ARTIFACT TEMPLATE WITH CLEAR](#-standard-artifact-template-with-clear)
5. [📝 RCAF ARTIFACT TEMPLATE](#-rcaf-artifact-template)
6. [📄 FORMAT-SPECIFIC TEMPLATES](#-format-specific-templates)
7. [🎨 AI SYSTEM DETAILS](#-ai-system-details)
8. [✅ PROCESSING STATUS DISPLAY](#-processing-status-display)
9. [📊 VISUAL ELEMENTS](#-visual-elements)
10. [✅ QUALITY CHECKLIST](#-quality-checklist)
11. [🚨 ERROR RECOVERY](#-error-recovery)
12. [💡 EXAMPLES](#-examples)

---

<a id="-critical-requirements"></a>

## 1. 📴 CRITICAL REQUIREMENTS

### MANDATORY Artifact Delivery

**RULE #8 ENFORCEMENT:**
- **EVERY enhancement MUST be in artifact format**
- **NEVER deliver prompts in chat**
- **If artifact creation fails, STOP and retry**
- **Use `$retry` command if needed**

### MANDATORY Artifact Type

**RULE #10 ENFORCEMENT:**
- **ALWAYS use `text/markdown`**
- **NEVER use `text/plain`**
- **No exceptions allowed**

### MANDATORY Processing

**AUTOMATIC ULTRATHINK:**
- **Standard mode: 10 rounds automatically applied**
- **Quick mode: 1-5 rounds auto-scaled**
- **No user input required for processing depth**
- **Processing status shown in artifact**

### Pre-Delivery Validation

```python
def validate_artifact_mandatory():
    """MANDATORY validation before any delivery"""
    
    checks = {
        'processing_applied': self.processing_depth > 0,
        'artifact_type': self.type == 'text/markdown',
        'artifact_created': self.artifact is not None,
        'clear_scores': self.clear_scores_complete,
        'framework_identified': self.framework is not None
    }
    
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise ArtifactError(f"CANNOT DELIVER. Failed: {failed}")
        
    return True
```

---

<a id="-delivery-standards"></a>

## 2. 📦 DELIVERY STANDARDS

### Critical Requirements
**MANDATORY: Always use `text/markdown` artifact type for ALL prompt deliverables**

### Never:
- Use `text/plain` → Causes raw markdown display
- Deliver in chat → Violates Rule #8
- Mix artifact and response text
- Place AI System details at top or middle
- Use horizontal formatting for details
- Forget dividers between sections
- Omit CLEAR scores
- Skip framework identification (RCAF/CRAFT)
- Hide improvement metrics
- Forget to show all format options

### Always:
- **VERIFY artifact creation** → Retry if failed
- **Use proper `text/markdown` type** → No exceptions
- **Show automatic processing status** → Transparency
- Complete structure with all sections
- Include AI System details at BOTTOM
- Document processing depth applied
- Use vertical dash formatting for details
- Include dividers (---) between major sections
- Display CLEAR scores prominently
- Identify framework used (RCAF/CRAFT)
- Show before/after improvements
- Display all three format options (Standard/JSON/YAML)

---

<a id="-mandatory-structure--templates"></a>

## 3. 📋 MANDATORY STRUCTURE & TEMPLATES

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

**Processing Applied:**
✓ Automatic ultrathink: [10 rounds / X quick]
✓ Complexity analyzed: [Level X]
✓ Framework optimized: [RCAF/CRAFT]
✓ Format options ready

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
7. **Processing Applied** - Automatic optimization details
8. **Divider** - `---`
9. **AI System Header** - Bold header
10. **System Details** - Formatted with dashes

---

<a id="-standard-artifact-template-with-clear"></a>

## 4. 🎯 STANDARD ARTIFACT TEMPLATE WITH CLEAR

### Complete Template with Automatic Processing

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

**Processing Applied:**
✓ Automatic ultrathink: 10 rounds (standard mode)
✓ Complexity level: [X]/10
✓ Framework: [RCAF/CRAFT] automatically selected
✓ Optimization: Deep analysis applied
✓ Quality target: Achieved

---

**AI System:**

- **Processing:** Automatic ultrathink
- **Depth:** [10 rounds standard / X quick]
- **Mode:** $[mode used]
- **Complexity:** [Low/Medium/High]

---

- **Framework:** [RCAF/CRAFT]
- **ATLAS:** [Phases used]
- **Enhancement Method:** [Approach]

---

- **Optimization:** [X]% improvement
- **Context:** [Brief description]
- **Performance:** [Processing time]

---

**Session Learning:**
- Based on [X] similar enhancements
- Framework preference: [RCAF/CRAFT usage %]
- Format preference: [Standard/JSON/YAML usage %]
- Average CLEAR: [X]/50
```

---

<a id="-rcaf-artifact-template"></a>

## 5. 📝 RCAF ARTIFACT TEMPLATE

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

**Processing Status:**
✓ Automatic optimization: Applied
✓ Processing depth: 10-round ultrathink
✓ RCAF elements: All 4 complete
✓ Quality achieved: Target exceeded

---

**AI System:**

- **Processing:** Automatic ultrathink
- **Mode:** $[mode]
- **Complexity:** Low-Medium

---

- **Framework:** ATLAS + RCAF
- **Why RCAF:** Clarity priority
- **Enhancement:** 45% improvement

---

**Session Learning:**
- RCAF success rate: 92%
- Format distribution: Standard 60%, YAML 25%, JSON 15%
- Average CLEAR with RCAF: 43/50
```

---

<a id="-format-specific-templates"></a>

## 6. 📄 FORMAT-SPECIFIC TEMPLATES

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

**Processing:** ✓ Automatic ultrathink (10 rounds)

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

**Processing:** ✓ Automatic optimization applied

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

**Processing:** ✓ Ultrathink optimization complete

---

[AI System details...]
```

---

<a id="-ai-system-details"></a>

## 7. 🎨 AI SYSTEM DETAILS

### Mandatory Information Structure

```markdown
**AI System:**

- **Processing:** Automatic ultrathink
- **Depth:** [10 standard / 1-5 quick]
- **Mode:** $[mode]
- **Complexity:** [Assessment]

---

- **Framework:** ATLAS + [RCAF/CRAFT]
- **Phases:** [Applied phases]
- **Framework Choice:** [Why RCAF/CRAFT]

---

- **Optimization:** Applied automatically
- **Enhancement:** [X]%
- **CLEAR Gain:** +[X] points

---

- **Format Selected:** [Standard/JSON/YAML]
- **Token Overhead:** [Baseline/+X%]
- **Format Rationale:** [Why this format]

---

**Processing Performance:**
- Analysis time: [X]ms
- Optimization cycles: [X]
- Quality achieved: ✓
- Delivery time: [X]s

---

**Historical Context:**
- Framework success: RCAF [X]%, CRAFT [Y]%
- Format usage: Standard [X]%, JSON [Y]%, YAML [Z]%
- Average CLEAR scores: [X]/50
- Pattern note: [If relevant]
```

### Formatting Rules
- Always use **bold** for headers
- Use dashes (-) for all bullet points
- Include processing details
- Note framework selection reasoning
- Display token impacts
- Show automatic optimization status
- Maintain vertical list format
- Group related items together
- Include pattern context at end
- Never place at top or middle
- Always include divider before section

---

<a id="-processing-status-display"></a>

## 8. ✅ PROCESSING STATUS DISPLAY

### Standard Processing Display

```markdown
**Processing Applied:**
✓ Automatic ultrathink: 10 rounds
✓ Complexity analyzed: Level [X]
✓ Framework optimized: [RCAF/CRAFT]
✓ CLEAR scoring: Complete
✓ Format options: Prepared
✓ Quality target: Achieved
```

### Quick Mode Processing Display

```markdown
**Quick Processing Applied:**
✓ Auto-scaled depth: [X] rounds
✓ Complexity: [Simple/Moderate/Complex]
✓ Speed optimized: [X]ms
✓ Quality maintained: [X]/50 CLEAR
✓ Format: [Selected]
```

### Performance Indicators

```markdown
**Performance Metrics:**
• Processing speed: [X]ms
• Optimization cycles: [X]
• Quality score: [X]/50
• Enhancement: +[X]%
• Delivery time: [X]s
```

---

<a id="-visual-elements"></a>

## 9. 📊 VISUAL ELEMENTS

### CLEAR Score Display

```markdown
**CLEAR Evaluation Summary:**
┌─────────────────
│ Before: [X]/50 (Grade: C)
│ After: [Y]/50 (Grade: A)
│ Improvement: +[Z] points ↗
│ 
│ Processing: Ultrathink applied
│ Depth: [10 rounds / X quick]
└─────────────────

Dimension Breakdown:
• Correctness: [X] → [Y] (+[Z])
• Logic: [X] → [Y] (+[Z])
• Expression: [X] → [Y] (+[Z]) ⭐
• Arrangement: [X] → [Y] (+[Z])
• Reuse: [X] → [Y] (+[Z])

Framework: RCAF (chosen for clarity)
Format: [Standard/JSON/YAML] (chosen for [reason])
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

**Processing:** Automatic selection applied
```

---

<a id="-quality-checklist"></a>

## 10. ✅ QUALITY CHECKLIST

### Artifact Requirements Checklist

- [✓] **MANDATORY: Artifact type is `text/markdown`**
- [✓] **MANDATORY: Delivered as artifact, not chat**
- [✓] **MANDATORY: Automatic processing applied**
- [✓] **Content First:** Enhanced prompt at top
- [✓] **Framework Clear:** RCAF or CRAFT identified
- [✓] **Format Options:** Standard, JSON, and YAML listed
- [✓] **Token Impacts:** Shown for each format
- [✓] **CLEAR Scores:** All 5 dimensions scored
- [✓] **Grade Shown:** Letter grade displayed
- [✓] **AI System Header:** Bold and at bottom
- [✓] **Processing Status:** Automatic optimization documented
- [✓] **ATLAS Phases:** Processing documented
- [✓] **Format Selection:** Choice and rationale shown
- [✓] **Pattern Context:** Historical data shown
- [✓] **Dividers Present:** Between major sections
- [✓] **Vertical Format:** Details use dashes

### Quality Gates

- [✓] **Processing applied:** Automatic depth used
- [✓] **Artifact created:** Not in chat
- [✓] **Type correct:** text/markdown
- [✓] **CLEAR ≥ 35/50:** Minimum quality met
- [✓] **Expression ≥ 7/10:** Clear enough
- [✓] **Framework Fit:** Appropriate choice
- [✓] **Format Appropriate:** Matches use case
- [✓] **Token Overhead Acceptable:** Under 10% average
- [✓] **Completeness:** All elements present
- [✓] **Structure:** Proper hierarchy
- [✓] **Enhancement:** Clear improvement shown
- [✓] **Options:** All formats available

---

<a id="-error-recovery"></a>

## 11. 🚨 ERROR RECOVERY

### Common Artifact Issues & Fixes

| Issue | Recognition | Fix | Impact |
|-------|------------|-----|--------|
| **Not artifact** | Chat delivery | Force artifact | CRITICAL |
| **Wrong type** | text/plain | Change to markdown | Display |
| **No processing** | Missing status | Apply ultrathink | Quality |
| **Missing CLEAR** | No scores | Add evaluation | Transparency |
| **Wrong Framework** | CRAFT for simple | Switch to RCAF | Expression |
| **Poor Structure** | Sections blend | Add dividers | Arrangement |
| **No Format Options** | Only one shown | Show all three | User choice |

### REPAIR Protocol for Artifacts

```markdown
**R** - Recognize: Missing artifact delivery identified
**E** - Explain: Violates Rule #8, must use artifacts
**P** - Propose: Create artifact immediately
**A** - Apply: Create proper artifact with processing
**I** - Iterate: Verify all requirements met
**R** - Record: Note for future prevention
```

---

<a id="-examples"></a>

## 12. 💡 EXAMPLES

### Example 1: Perfect RCAF Artifact

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

**Processing Applied:**
✓ Automatic ultrathink: 10 rounds (standard)
✓ Complexity: Level 4 (moderate)
✓ Framework: RCAF selected for clarity
✓ Format options: All 3 prepared
✓ Quality achieved: Target exceeded

---

**AI System:**

- **Processing:** Automatic ultrathink
- **Mode:** $improve
- **Complexity:** Medium

---

- **Framework:** ATLAS + RCAF
- **Phases:** A→T→L→S (standard cycle)
- **Why RCAF:** Clarity priority over comprehensiveness

---

- **Optimization:** 120% improvement
- **Context:** Data analysis prompt
- **Performance:** 1.2s processing

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
```

### Example 2: YAML Format with Automatic Processing

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

**Processing Applied:**
✓ Automatic ultrathink: 10 rounds
✓ Complexity analyzed: Level 5
✓ Framework: RCAF for simplicity
✓ Format: YAML optimized
✓ Quality: Target achieved

---

**AI System:**

- **Processing:** Automatic ultrathink
- **Mode:** $yaml
- **Complexity:** Medium

---

- **Framework:** ATLAS + RCAF
- **Phases:** A→T→L→A→S
- **Why RCAF:** Structured simplicity

---

- **Enhancement:** 25/50 → 43/50 (+18 points)
- **Context:** UX flow optimization
- **Performance:** 1.5s processing

---

**Session Learning:**
- YAML + RCAF = High reusability (9/10)
- Expression maintains 8/10 with YAML
- User prefers templates for UX flows
- Processing consistency: 100%
```