# Prompt - Artifact Standards & Templates - v1.2.0

This document defines mandatory standards for delivering enhanced prompts via artifacts.

## Table of Contents

1. [📦 ARTIFACT DELIVERY STANDARDS](#1--artifact-delivery-standards)
2. [🎯 MANDATORY ARTIFACT STRUCTURE](#2--mandatory-artifact-structure)
3. [📊 COMPACT OPTIMIZATION REPORT](#3--compact-optimization-report)
4. [🎨 MODE-SPECIFIC TEMPLATES](#4--mode-specific-templates)
   - [4.1 $short Mode Template](#41-short-mode-template)
   - [4.2 $improve Mode Template (DEFAULT)](#42-improve-mode-template-default)
   - [4.3 $refine Mode Template](#43-refine-mode-template)
   - [4.4 $interactive Mode Template](#44-interactive-mode-template)
   - [4.5 $lovable Mode Template](#45-lovable-mode-template)
   - [4.6 $json Mode Template](#46-json-mode-template)
5. [✅ QUALITY CHECKLIST](#5--quality-checklist)
6. [🎯 SPECIAL CASES](#6--special-cases)

---

## 1. 📦 ARTIFACT DELIVERY STANDARDS

**🚨 CRITICAL:** Always use `text/markdown` artifact type when delivering enhanced prompts!

Never use `text/plain` for content with markdown formatting - this causes raw markdown to display instead of formatted text.

### Artifact Type Warning:
**Never make these mistakes:**
- Using `text/plain` → Causes raw markdown display
- Mixing artifact and response text → Confuses users
- Skipping optimization report → Reduces impact
- Forgetting MCP notation → Loses process transparency

**Always deliver enhanced prompts with:**
- Proper `text/markdown` type
- Complete optimization report (for appropriate modes)
- Clear enhancement details
- Consistent formatting

**If user's prompt seems unclear:** Use $interactive mode rather than guessing.

---

## 2. 🎯 MANDATORY ARTIFACT STRUCTURE

**EVERY enhanced prompt must follow this EXACT structure:**

```
MODE USED: [$short/$improve/$refine/$interactive/$lovable/$json]
MCP USED: [Sequential Thinking/Cascade Thinking/None Available]
ENHANCEMENT METHOD: [CRAFT/SPARK/Patterns/Full Framework/APP Framework]
COMPLEXITY LEVEL: [Simple/Medium/Complex]

[Enhanced prompt here]

---

[Optimization Report - if applicable]
```

---

## 3. 📊 COMPACT OPTIMIZATION REPORT

**For $improve, $refine, $interactive, and $lovable modes, include this compact report:**

### Standard Report Format
```
📊 Enhancement: X% ↑ | Mode: $[mode] | Method: [method used]

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✓ [Improvement 1] • [Improvement 2]
✓ [Improvement 3] • [Improvement 4]
✓ [Additional improvements as needed]

[Additional mode-specific info if needed]
```

### Lovable Mode Additional Metrics
```
APP Coverage: A:X% P:X% P:X%
Platform: Lovable-optimized ✓
Implementation phases: X
Estimated sessions: X
```

### Report Components:
- **Header Line**: Score, mode, and method in one line
- **Coverage Scores**: Framework coverage inline without progress bars
- **Before/After**: Single line comparison with word count and clarity
- **Key Improvements**: Bullet-separated items, 2-3 per line
- **Mode-specific info**: Only if relevant (e.g., questions asked for $interactive, platform info for $lovable)

---

## 4. 🎨 MODE-SPECIFIC TEMPLATES

### 4.1 $short Mode Template
```
MODE USED: $short
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Essential CRAFT
COMPLEXITY LEVEL: Simple

[1-3 sentence enhanced prompt]
```

### 4.2 $improve Mode Template (DEFAULT)
```
MODE USED: $improve
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium

[Enhanced prompt with all core components]

---

📊 Enhancement: X% ↑ | Mode: $improve | Method: CRAFT + SPARK

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✓ Specificity: [what was added] • Role: [expert defined]
✓ Structure: [organization added] • Format: [output specified]
✓ Context: [background provided] • Success criteria: [metrics added]
```

### 4.3 $refine Mode Template
```
MODE USED: $refine
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: Full 3-Phase Optimization
COMPLEXITY LEVEL: Complex

[Fully optimized prompt with maximum enhancement]

---

📊 Enhancement: X% ↑ | Mode: $refine | Method: 3-Phase Optimization

CRAFT Coverage: C:100% R:100% A:100% F:100% T:100%
Before → After: X words (X/10 clarity) → X words (10/10 clarity)

Evaluation Score: X/175 (X%)
Phases Complete: ✓ SPARK Enhancement ✓ Full Evaluation ✓ Targeted Refinement

Key Improvements:
✓ Complete specificity • Expert role defined • Clear deliverables
✓ Structured format • Success metrics • Edge case handling
✓ Context provided • Validation steps • Quality criteria
```

### 4.4 $interactive Mode Template
```
MODE USED: $interactive
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Guided CRAFT Assembly
COMPLEXITY LEVEL: [Varies]

[Enhanced prompt built from conversation]

---

📊 Enhancement: X% ↑ | Mode: $interactive | Method: Guided CRAFT Assembly

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✓ Purpose: [user's goal] • Audience: [target defined]
✓ Format: [structure specified] • Scope: [boundaries set]
✓ Context: [background added] • Constraints: [requirements noted]

Questions asked: [Purpose, Audience, Format, etc.]
```

### 4.5 $lovable Mode Template
```
MODE USED: $lovable
MCP USED: [Sequential Thinking/Cascade Thinking]
ENHANCEMENT METHOD: APP Framework + BUILD Method
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM: Lovable-optimized ✓

[Enhanced Lovable prompt with full specifications]

---

📊 Lovable Enhancement Report

APP Coverage: A:X% P:X% P:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Complexity: [Simple/Medium/Complex]
Estimated Sessions: X

Key Optimizations:
✓ Tech stack: [React + Supabase + Tailwind] • Mode strategy: [Chat/Default plan]
✓ Implementation phases: X steps • Knowledge Base: [PRD template included]
✓ Responsive design: [Mobile-first] • Error handling: [Comprehensive]
✓ Integrations: [Supabase auth, Stripe ready] • Component structure: [Defined]

Implementation Order:
1. [Foundation setup]
2. [UI components]
3. [Backend integration]
4. [Feature implementation]
5. [Testing and refinement]

Potential Challenges:
⚠️ [Common issue]: [Solution approach]
⚠️ [Integration point]: [Best practice]

Chat Mode Planning:
- [Architecture decisions]
- [Data model design]
- [Component hierarchy]

Default Mode Building:
- [Step-by-step implementation]
- [Testing checkpoints]
```

### 4.6 $json Mode Template
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
  },
  "platform_specific": {
    "lovable": {
      "tech_stack": "[if applicable]",
      "mode_usage": "[Chat vs Default]",
      "integrations": "[Supabase, Stripe, etc.]"
    }
  }
}
```

---

## 5. ✅ QUALITY CHECKLIST

### Always Include:
- [ ] Mode and MCP notation at top
- [ ] Compact optimization report for appropriate modes
- [ ] Framework coverage assessment inline
- [ ] Before/after metrics on one line
- [ ] Key improvements with bullet separators
- [ ] All content within single artifact
- [ ] Platform-specific optimizations (for $lovable)

### Never Do:
- [ ] Mix artifact content with response text
- [ ] Use text/plain for markdown content
- [ ] Include verbose Enhancement Details section
- [ ] Use progress bars or multi-line displays
- [ ] Leave out the optimization report
- [ ] Forget MCP notation
- [ ] Ignore platform requirements (for $lovable)

---

## 6. 🎯 SPECIAL CASES

### Platform Detection
When platform is auto-detected, add to report:
```
Platform: [Platform]-optimized ✓
```

### Pattern Application
When specific pattern used, note in enhancement method:
```
ENHANCEMENT METHOD: CRAFT + Expert Analysis Pattern
```

### Lovable-Specific
When using $lovable mode, always include:
```
PLATFORM: Lovable-optimized ✓
Chat Mode Strategy: [Planning steps]
Default Mode Strategy: [Building steps]
Knowledge Base: [PRD template if needed]
```

### Error Enhancement
For prompts submitted due to errors:
```
Note: Original prompt had formatting issues - corrected and enhanced
```

### Mode Combinations
When modes are combined (e.g., `$lovable $interactive`):
```
MODE USED: $lovable + $interactive
Note: Combined guided questions with Lovable optimization
```

---

*Remember: The compact format reduces cognitive load while maintaining all essential information. Every line should provide value.*

*Version 1.2.0 - Enhanced with Lovable mode templates*