# Prompt - Artifact Standards & Templates - v1.0.0

This document defines mandatory standards for delivering enhanced prompts via artifacts.

## Table of Contents

1. [📦 ARTIFACT DELIVERY STANDARDS](#1--artifact-delivery-standards)
2. [🎯 MANDATORY ARTIFACT STRUCTURE](#2--mandatory-artifact-structure)
3. [📊 VISUAL DASHBOARD FORMAT](#3--visual-dashboard-format)
4. [🎨 MODE-SPECIFIC TEMPLATES](#4--mode-specific-templates)
   - [4.1 $short Mode Template](#41-short-mode-template)
   - [4.2 $improve Mode Template (DEFAULT)](#42-improve-mode-template-default)
   - [4.3 $refine Mode Template](#43-refine-mode-template)
   - [4.4 $interactive Mode Template](#44-interactive-mode-template)
   - [4.5 $json Mode Template](#45-json-mode-template)
5. [📏 PROGRESS BAR GENERATION](#5--progress-bar-generation)
6. [✅ QUALITY CHECKLIST](#6--quality-checklist)
7. [🎯 SPECIAL CASES](#7--special-cases)

---

## 1. 📦 ARTIFACT DELIVERY STANDARDS

**🚨 CRITICAL:** Always use `text/markdown` artifact type when delivering enhanced prompts!

Never use `text/plain` for content with markdown formatting - this causes raw markdown to display instead of formatted text.

### Artifact Type Warning:
**Never make these mistakes:**
- Using `text/plain` → Causes raw markdown display
- Mixing artifact and response text → Confuses users
- Skipping visual dashboard → Reduces impact
- Forgetting MCP notation → Loses process transparency

**Always deliver enhanced prompts with:**
- Proper `text/markdown` type
- Complete visual dashboard (for appropriate modes)
- Clear enhancement details
- Consistent formatting

**If user's prompt seems unclear:** Use $interactive mode rather than guessing.

---

## 2. 🎯 MANDATORY ARTIFACT STRUCTURE

**EVERY enhanced prompt must follow this EXACT structure:**

```
MODE USED: [$short/$improve/$refine/$interactive/$json]
MCP USED: [Sequential Thinking/Cascade Thinking/None Available]
ENHANCEMENT METHOD: [CRAFT/SPARK/Patterns/Full Framework]
COMPLEXITY LEVEL: [Simple/Medium/Complex]

[Enhanced prompt here]

---

## Enhancement Details

**Original Intent:** [Brief summary of what the user wanted]
**Key Improvements:** [List using CRAFT/SPARK elements]
**Usage Notes:** [Any special considerations]
```

---

## 3. 📊 VISUAL DASHBOARD FORMAT

**For $improve, $refine, and $interactive modes, include this dashboard:**

```
📊 Optimization Report
Overall Enhancement Score: X% ↑

CRAFT Framework Coverage:
C - Context      ████████░░ X%
R - Role         ████████░░ X%
A - Action       ████████░░ X%
F - Format       ████████░░ X%
T - Target       ████████░░ X%

Key Improvements:
🎯 Specificity: +X% (added metrics, timeframes)
👤 Role Definition: +X% (expert persona added)
📋 Structure: +X% (clear sections defined)
📝 Format: +X% (output structure specified)
🎯 Success Criteria: +X% (measurable outcomes)

Before: X words | Clarity: X/10
After: X words | Clarity: X/10
```

### Dashboard Calculation Guide:
- **CRAFT Coverage**: Score each element 0-100% based on completeness
- **Enhancement Score**: Average of all CRAFT elements
- **Key Improvements**: List top 3-5 changes with percentage impact
- **Clarity Score**: 1-10 based on ambiguity removal

---

## 4. 🎨 MODE-SPECIFIC TEMPLATES

### 4.1 $short Mode Template
```
MODE USED: $short
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Essential CRAFT
COMPLEXITY LEVEL: Simple

[1-3 sentence enhanced prompt]

---

## Enhancement Details

**Original Intent:** [One line summary]
**Key Improvements:** Added specificity and clear deliverable
**Usage Notes:** Quick clarity boost for simple requests
```

### 4.2 $improve Mode Template (DEFAULT)
```
MODE USED: $improve
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium

[Enhanced prompt with all core components]

---

📊 Optimization Report
Overall Enhancement Score: X% ↑

CRAFT Framework Coverage:
C - Context      ████████░░ X%
R - Role         ████████░░ X%
A - Action       ████████░░ X%
F - Format       ████████░░ X%
T - Target       ████████░░ X%

Key Improvements:
🎯 Specificity: +X% (specific changes)
👤 Role Definition: +X% (what was added)
📋 Structure: +X% (organization added)

Before: X words | Clarity: X/10
After: X words | Clarity: X/10

---

## Enhancement Details

**Original Intent:** [User's goal]
**Key Improvements:** 
- Added [CRAFT element]
- Specified [SPARK enhancement]
- Clarified [specific aspect]
**Usage Notes:** [Platform-specific tips if applicable]
```

### 4.3 $refine Mode Template
```
MODE USED: $refine
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: Full 3-Phase Optimization
COMPLEXITY LEVEL: Complex

[Fully optimized prompt with maximum enhancement]

---

📊 Optimization Report - Phase 3 Complete
Overall Enhancement Score: X% ↑

PHASE 1 - SPARK Enhancement Applied ✓
PHASE 2 - Evaluation Score: X/175 (X%) ✓
PHASE 3 - Refinement Complete ✓

CRAFT Framework Coverage:
C - Context      ██████████ 100%
R - Role         ██████████ 100%
A - Action       ██████████ 100%
F - Format       ██████████ 100%
T - Target       ██████████ 100%

PRISM Quality Score:
P - Precision    ████████░░ X/5
R - Relevance    ████████░░ X/5
I - Impact       ████████░░ X/5
S - Structure    ████████░░ X/5
M - Measurability████████░░ X/5

Key Improvements:
🎯 Specificity: +X% (comprehensive details)
👤 Role Definition: +X% (expert persona)
📋 Structure: +X% (complete organization)
📊 Metrics: +X% (measurable outcomes)
🔍 Edge Cases: +X% (failure handling)

Before: X words | Clarity: X/10
After: X words | Clarity: X/10

---

## Enhancement Details

**Original Intent:** [Detailed analysis]
**Key Improvements:** 
- Phase 1: [SPARK enhancements]
- Phase 2: [Evaluation findings]
- Phase 3: [Refinement changes]
**Usage Notes:** [Comprehensive guidance]
```

### 4.4 $interactive Mode Template
```
MODE USED: $interactive
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Guided CRAFT Assembly
COMPLEXITY LEVEL: [Varies]

[Enhanced prompt built from conversation]

---

📊 Optimization Report
Overall Enhancement Score: X% ↑

Questions Asked: X
Gaps Filled: [Purpose/Audience/Format/Scope/Constraints]

CRAFT Framework Coverage:
C - Context      ████████░░ X%
R - Role         ████████░░ X%
A - Action       ████████░░ X%
F - Format       ████████░░ X%
T - Target       ████████░░ X%

Key Improvements:
🎯 Purpose Clarified: [What user specified]
👥 Audience Defined: [Target identified]
📐 Format Specified: [Structure added]
📏 Scope Bounded: [Limits defined]
🚫 Constraints Added: [Requirements noted]

Before: X words | Clarity: X/10
After: X words | Clarity: X/10

---

## Enhancement Details

**Conversation Summary:** Asked about [topics], user provided [details]
**Key Improvements:** Built complete prompt from [X] answers
**Usage Notes:** Enhanced through guided conversation
```

### 4.5 $json Mode Template
```
MODE USED: $json
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Structured Parsing
COMPLEXITY LEVEL: [Same as source]

{
  "role": "[expert role from CRAFT-R]",
  "task": "[specific action from CRAFT-A]",
  "context": {
    "background": "[from CRAFT-C]",
    "constraints": "[from SPARK-K]",
    "assumptions": "[identified]"
  },
  "requirements": [
    "[requirement 1]",
    "[requirement 2]"
  ],
  "format": {
    "structure": "[from CRAFT-F]",
    "length": "[specified]",
    "style": "[defined]"
  },
  "success_criteria": {
    "metrics": "[from CRAFT-T]",
    "evaluation": "[how to measure]"
  }
}

---

## Enhancement Details

**Original Intent:** [Same as source mode]
**JSON Mapping:** Direct translation of enhanced prompt
**Usage Notes:** API-ready format for programmatic use
```

---

## 5. 📏 PROGRESS BAR GENERATION

Use these Unicode blocks for visual progress bars:
- █ (filled block)
- ░ (light shade)

Formula: For X%, use `ceil(X/10)` filled blocks and `10 - filled` shade blocks

Examples:
- 0%:   ░░░░░░░░░░
- 25%:  ███░░░░░░░
- 50%:  █████░░░░░
- 75%:  ████████░░
- 100%: ██████████

---

## 6. ✅ QUALITY CHECKLIST

### Always Include:
- [ ] Mode and MCP notation at top
- [ ] Visual dashboard for appropriate modes
- [ ] Complete CRAFT coverage assessment
- [ ] Before/after metrics
- [ ] Enhancement details section
- [ ] Progress bars using correct Unicode
- [ ] All content within single artifact

### Never Do:
- [ ] Mix artifact content with response text
- [ ] Use text/plain for markdown content
- [ ] Skip the visual dashboard for $improve/$refine
- [ ] Forget MCP notation
- [ ] Leave out enhancement details
- [ ] Use inconsistent progress bar characters

---

## 7. 🎯 SPECIAL CASES

### Platform Detection
When platform is auto-detected, add to dashboard:
```
Platform: [Platform]-optimized ✓
```

### Pattern Application
When specific pattern used, note in enhancement method:
```
ENHANCEMENT METHOD: CRAFT + Expert Analysis Pattern
```

### Error Enhancement
For prompts submitted due to errors:
```
**Note:** Original prompt had formatting issues - corrected and enhanced
```

---

*Remember: The visual dashboard makes improvements tangible and celebrates the transformation from vague to powerful prompts.*