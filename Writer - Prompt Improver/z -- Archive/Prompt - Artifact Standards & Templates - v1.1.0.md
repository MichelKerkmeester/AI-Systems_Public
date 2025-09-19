# Prompt - Artifact Standards & Templates - v1.1.0

Comprehensive artifact delivery standards for prompt engineering system with mandatory formatting requirements, AI System details, and multi-format support.

## 📋 Table of Contents

1. [📦 DELIVERY STANDARDS](#-delivery-standards)
2. [📋 MANDATORY STRUCTURE & TEMPLATES](#-mandatory-structure--templates)
3. [🎯 STANDARD ARTIFACT TEMPLATE](#-standard-artifact-template)
4. [📄 FORMAT-SPECIFIC TEMPLATES](#-format-specific-templates)
5. [🎨 AI SYSTEM DETAILS](#-ai-system-details)
6. [📊 VISUAL ELEMENTS](#-visual-elements)
7. [✅ QUALITY CHECKLIST](#-quality-checklist)
8. [🚨 ERROR RECOVERY](#-error-recovery)
9. [💡 EXAMPLES](#-examples)

---

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
- Omit pattern context when available
- Restrict options based on patterns

### Always:
- Use proper `text/markdown` type
- Complete structure with all sections
- Include AI System details at BOTTOM
- Document thinking rounds selected
- Use vertical dash formatting for details
- Include dividers (---) between major sections
- Show historical context as notes
- Display all format options

---

## 2. 📋 MANDATORY STRUCTURE & TEMPLATES

### Content First Structure
```markdown
[Main enhanced prompt - clean and focused]

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`)
• SMILE format available (`$smile`)

---

**AI System:**

[ARTIFACT DETAILS AT BOTTOM - vertical format with dashes]
```

### Section Order (Top to Bottom)
1. **Main Content** - The enhanced prompt itself
2. **Divider** - `---`
3. **Format Options** - Available alternatives
4. **Divider** - `---`
5. **AI System Header** - Bold header
6. **System Details** - Formatted with dashes

### Mode-Specific Templates

#### Interactive Mode Template
```markdown
[Enhanced prompt created through guided conversation]

[Content reflecting discovered requirements]

---

**Format Options:**
• Standard format (shown above)
• JSON format (`$json`) - For API integration
• SMILE format (`$smile`) - For complex instructions

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $interactive
- **Complexity:** [Low/Medium/High]

---

- **Thinking:** [X] rounds (user selected)
- **Discovery:** [X] questions asked
- **ATLAS:** [Phases applied]

---

- **Challenge:** [If complexity reduced]
- **Enhancement:** [X]% improvement
- **Context:** [Brief description]

---

**Historical Context:**
- Patterns from [X] sessions
- All options always shown
- User autonomy: 100%
```

#### Builder Mode Template
```markdown
[Universal creative brief for platform development]

**GOAL:** [What users accomplish]
**AUDIENCE:** [Target users]
**SUCCESS:** [Measurable outcomes]

Phase 1 - Core MVP:
[Essential functionality only]

Phase 2 - Enhanced Experience:
[If validated by users]

Phase 3 - Premium Features:
[Only if needed]

---

**Format Options:**
• Standard format (shown above)
• SMILE format (`$smile`) - For structured workflow

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $builder
- **Sub-mode:** [prototype/website/app]

---

- **Thinking:** [X] rounds
- **Platform:** Universal (works on all)
- **Phase Recommended:** [1/2/3]

---

- **Challenge:** [MVP simplification applied]
- **Alternative:** [Simpler approach if suggested]
- **Context:** [Brief description]

---

**Historical Context:**
- Builder mode frequency: [X]%
- Typical phase selection: [1/2/3]
- Platform preferences: [if any]
```

---

## 3. 🎯 STANDARD ARTIFACT TEMPLATE

### Complete Template with All Elements

```markdown
[Enhanced prompt content here]

As a [role/expertise], [main task/action] for [audience/purpose].

Context: [relevant background]
Requirements: [specific needs]
Output: [expected format/structure]
Success Criteria: [measurable outcomes]

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`) - Structured for APIs
• SMILE format available (`$smile`) - Better instruction following (+25% tokens)

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $[mode used]
- **Complexity:** [Low/Medium/High]

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** [Phases used like A→T→L→A→S]

---

- **Challenge:** [Applied/Not needed - brief note]
- **Enhancement:** [X]% improvement
- **Context:** [Brief description]

---

**Historical Context:**
- Based on [X] similar enhancements
- Format preference: [Standard/JSON/SMILE usage %]
- Typical thinking rounds: [X]
- All options always available
```

---

## 4. 📄 FORMAT-SPECIFIC TEMPLATES

### JSON Format Artifact

```markdown
```json
{
  "role": "[expertise/position]",
  "task": "[main action required]",
  "context": "[background information]",
  "requirements": [
    "[requirement 1]",
    "[requirement 2]",
    "[requirement 3]"
  ],
  "output": {
    "format": "[expected structure]",
    "length": "[if applicable]",
    "style": "[if relevant]"
  },
  "success_criteria": [
    "[metric 1]",
    "[metric 2]"
  ]
}
```

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $json
- **Structure:** Optimized for API use

---

- **Thinking:** [X] rounds (user selected)
- **Token Impact:** [+/-X]% vs standard
- **Parse Reliability:** High

---

**Historical Context:**
- JSON used [X]% for technical prompts
- Previous JSON success rate: [X]%
```

### SMILE Format Artifact

```markdown
(: Enhanced Prompt
  [: Role [
    [expertise definition]
  ] :]
  
  [= Task =] [specific action required]
  
  [: Context (
    [background information]
    [relevant details]
  ) :]
  
  [: Requirements [
    [! Priority: [critical element] !]
    • [requirement 1]
    • [requirement 2]
    • [requirement 3]
  ] :]
  
  [: Output Format [
    {Expected structure here}
    {User provides details}
  ] :]
  
  [! Success: [measurable criteria] !]
) :)

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $smile
- **SMILE Depth:** [minimal/moderate/heavy]

---

- **Thinking:** [X] rounds (user selected)
- **Token Impact:** +[X]% (typical for SMILE)
- **Instruction Following:** Enhanced

---

- **Symbols Used:** [List key symbols]
- **Nesting Levels:** [X]
- **Best For:** Complex multi-step prompts

---

**Historical Context:**
- SMILE preferred [X]% for complex prompts
- Typical depth: [minimal/moderate/heavy]
- Token tolerance: [High/Medium/Low]
```

---

## 5. 🎨 AI SYSTEM DETAILS

### Mandatory Information Structure

```markdown
**AI System:**

- **Framework:** ATLAS
- **Mode:** $[mode]
- **Complexity:** [Assessment]

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** [Phases applied]

---

- **Challenge:** [Applied/Not needed]
- **Enhancement:** [X]%
- **Context:** [Brief description]

---

**Historical Context:**
- Historical data: [X] similar prompts
- Patterns shown: As context only
- User control: 100% maintained
```

### Formatting Rules for AI System Details
- Always use **bold** for "AI System:" header
- Use dashes (-) for all bullet points
- Maintain vertical list format
- Group related items together
- Include pattern context at end
- Never place at top or middle
- Always include divider before section

---

## 6. 📊 VISUAL ELEMENTS

### Enhancement Metrics Display

```markdown
**Enhancement Summary:**
━━━━━━━━━━━━━━━━━━━━━
Before: [X] words • Clarity: [X]/10
After: [Y] words • Clarity: [Y]/10
Improvement: [Z]% ↗

CRAFT Coverage:
• Context: [X]%
• Role: [X]%
• Action: [X]%
• Format: [X]%
• Target: [X]%
━━━━━━━━━━━━━━━━━━━━━
```

### Format Comparison Table

```markdown
**Format Options Comparison:**
┌─────────────┬────────┬───────┬─────────┐
│ Format      │ Tokens │ Clear │ Use For │
├─────────────┼────────┼───────┼─────────┤
│ Standard    │ Base   │ High  │ Most    │
│ JSON        │ +5%    │ V.High│ APIs    │
│ SMILE       │ +25%   │ High  │ Complex │
└─────────────┴────────┴───────┴─────────┘
```

---

## 7. ✅ QUALITY CHECKLIST

### Artifact Requirements Checklist

- [ ] **Content First:** Enhanced prompt at top
- [ ] **Format Options:** All available formats listed
- [ ] **AI System Header:** Bold and at bottom
- [ ] **Thinking Rounds:** User selection documented
- [ ] **ATLAS Phases:** Processing documented
- [ ] **Challenge Applied:** Decision noted
- [ ] **Pattern Context:** Historical data shown
- [ ] **Dividers Present:** Between major sections
- [ ] **Vertical Format:** Details use dashes
- [ ] **User Control:** All options shown

### Quality Gates

- [ ] **Clarity:** Immediate understanding?
- [ ] **Completeness:** All elements present?
- [ ] **Structure:** Proper hierarchy?
- [ ] **Format:** Markdown type used?
- [ ] **Enhancement:** Clear improvement?
- [ ] **Patterns:** Context not restrictive?
- [ ] **Options:** All choices available?

---

## 8. 🚨 ERROR RECOVERY

### Common Artifact Issues & Fixes

| Issue | Recognition | Fix | Prevention |
|-------|------------|-----|------------|
| **Missing AI System** | No header at bottom | Add complete section | Use template |
| **Wrong Position** | Details at top/middle | Move to bottom | Follow structure |
| **No Thinking Rounds** | Undocumented rounds | Add user selection | Always ask first |
| **Missing Dividers** | Sections blend together | Add --- between | Use template |
| **Horizontal Format** | Details in one line | Convert to vertical | Use dashes |
| **No Pattern Context** | Missing historical data | Add context section | Search history |
| **Format Missing** | No alternatives shown | List all options | Include always |

### REPAIR Protocol for Artifacts

```markdown
**R** - Recognize: Artifact structure issue identified
**E** - Explain: Impact on clarity and professionalism
**P** - Propose: Correct structure with template
**A** - Apply: Implement proper formatting
**I** - Iterate: Verify all requirements met
**R** - Record: Note for future prevention
```

---

## 9. 💡 EXAMPLES

### Example 1: Perfect Standard Artifact

```markdown
As a data scientist with machine learning expertise, analyze customer churn patterns in the SaaS subscription dataset to identify key predictive factors and recommend retention strategies.

Context: B2B SaaS platform with 10,000+ customers, 24-month historical data
Requirements: Statistical significance testing, feature importance ranking, actionable recommendations
Output: Executive report with visualizations and 3-5 specific retention tactics
Success Criteria: Model accuracy >85%, insights applicable within 30 days

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`) - For automated processing
• SMILE format available (`$smile`) - For complex analysis workflow

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $improve
- **Complexity:** Medium

---

- **Thinking:** 5 rounds (user selected)
- **ATLAS:** A→T→L→A→S (full cycle)

---

- **Challenge:** Applied - reduced from 10 requirements to 5 essential
- **Enhancement:** 73% improvement
- **Context:** Data analysis prompt

---

**Historical Context:**
- Based on 8 similar data science prompts
- Format preference: Standard 75%, JSON 25%
- Typical thinking rounds: 4-6
- All options always available
```

### Example 2: Interactive Mode Result

```markdown
Create a comprehensive user onboarding flow for a mobile banking app that reduces drop-off rates and ensures regulatory compliance while maintaining excellent user experience.

Target Users: Age 25-45, tech-comfortable but security-conscious
Key Requirements: KYC compliance, intuitive design, 5-minute completion time
Success Metric: <20% drop-off rate, 90% completion within first session

---

**Format Options:**
• Standard format (shown above)
• JSON format (`$json`) - For development handoff
• SMILE format (`$smile`) - For detailed step-by-step flow

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $interactive
- **Complexity:** High

---

- **Thinking:** 6 rounds (user selected)
- **Discovery:** 4 questions asked
- **ATLAS:** A→T→L→A→S

---

- **Challenge:** Simplified from 10 steps to 6
- **Enhancement:** 65% improvement
- **Context:** UX flow optimization

---

**Historical Context:**
- Interactive mode used 40% of time
- Onboarding prompts typically need 5-7 rounds
- Format split: Standard 60%, SMILE 40%
```

---

*Artifact excellence through systematic structure and comprehensive documentation. AI System details always at bottom with proper formatting. Pattern context enriches without restricting. All format options always available. User control absolute.*