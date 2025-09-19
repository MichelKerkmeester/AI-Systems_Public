# Artifact Standards & Templates - v0.210

This document defines mandatory standards for delivering enhanced prompts via artifacts, with credit optimization and visual reference matching support.

## Table of Contents

1. [📦 ARTIFACT DELIVERY STANDARDS](#1--artifact-delivery-standards)
2. [🎯 MANDATORY ARTIFACT STRUCTURE](#2--mandatory-artifact-structure)
3. [📊 COMPACT OPTIMIZATION REPORT](#3--compact-optimization-report)
4. [🎨 MODE-SPECIFIC TEMPLATES](#4--mode-specific-templates)
   - [4.1 $short Mode Template](#41-short-mode-template)
   - [4.2 $improve Mode Template (DEFAULT)](#42-improve-mode-template-default)
   - [4.3 $refine Mode Template](#43-refine-mode-template)
   - [4.4 $interactive Mode Template](#44-interactive-mode-template)
   - [4.5 $lovable Mode Templates](#45-lovable-mode-templates)
   - [4.6 $json Mode Template](#46-json-mode-template)
5. [✅ QUALITY CHECKLIST](#5--quality-checklist)
6. [🎯 SPECIAL CASES](#6--special-cases)

---

## 1. 📦 ARTIFACT DELIVERY STANDARDS

**🚨 CRITICAL:** 
- Always use `text/markdown` artifact type when delivering enhanced prompts!
- Every Lovable prompt is a PROMPT for building things, NOT the actual implementation!
- Include credit optimization strategies in all Lovable prompts!

Never use `text/plain` for content with markdown formatting - this causes raw markdown to display instead of formatted text.

### Artifact Type Warning:
**Never make these mistakes:**
- Using `text/plain` → Causes raw markdown display
- Creating actual implementations → We create PROMPTS only
- Skipping credit optimization → Reduces value for Lovable users
- Forgetting visual reference notes → Misses design requirements
- Missing "This is a PROMPT" clarification → Causes confusion

**Always deliver enhanced prompts with:**
- Proper `text/markdown` type
- Complete optimization report (for appropriate modes)
- Clear enhancement details
- Credit optimization strategy (for Lovable)
- Visual reference matching (when provided)
- Explicit "PROMPT not implementation" notes

**If user's prompt seems unclear:** Use $interactive mode rather than guessing.

---

## 2. 🎯 MANDATORY ARTIFACT STRUCTURE

**EVERY enhanced prompt must follow this EXACT structure:**

```
MODE USED: [$short/$improve/$refine/$interactive/$prototype/$website/$app/$json]
MCP USED: [Sequential Thinking/Cascade Thinking/None Available]
ENHANCEMENT METHOD: [CRAFT/SPARK/Patterns/Full Framework/VISION/CONVERT/SCALE]
COMPLEXITY LEVEL: [Simple/Medium/Complex]
VISUAL REFERENCE: [Matched/None Provided]

[Enhanced prompt here]

---

[Optimization Report - if applicable]
[Credit Strategy - for Lovable modes]
```

---

## 3. 📊 COMPACT OPTIMIZATION REPORT

**For $improve, $refine, $interactive, and $lovable modes, include this compact report:**

### Standard Report Format
```
📊 Enhancement: X% ↗ | Mode: $[mode] | Method: [method used]

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✓ [Improvement 1] • [Improvement 2]
✓ [Improvement 3] • [Improvement 4]
✓ [Additional improvements as needed]

[Additional mode-specific info if needed]
```

### Lovable Mode Additional Metrics

For Prototype mode, add:
```
VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Visual Focus: [Design/Interaction/Flow]
Credit Usage: Low-Medium
Credit Strategy: Static first, animations optional
Visual Reference: [Matched/Extracted if provided]
Note: This is a PROMPT for creating a prototype, not the prototype itself
```

For Website mode, add:
```
CONVERT Coverage: C:X% O:X% N:X% V:X% E:X% R:X% T:X%
SEO Ready: ✓ | Performance Optimized: ✓
Credit Usage: Medium
Credit Strategy: Core pages first, features incremental
Visual Reference: [Matched/Extracted if provided]
Note: This is a PROMPT for building a website, not the website itself
```

For App mode, add:
```
SCALE Coverage: S:X% C:X% A:X% L:X% E:X%
Backend: Supabase ✓ | Auth: Configured ✓
Complexity: [Simple/Medium/Complex]
Credit Usage: Medium-High
Credit Strategy: MVP core, complex features flagged
Visual Reference: [Matched/Extracted if provided]
Implementation Phases: X (with credit indicators)
Note: This is a PROMPT for developing an app, not the app itself
```

---

## 4. 🎨 MODE-SPECIFIC TEMPLATES

### 4.1 $short Mode Template
```
MODE USED: $short
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Essential CRAFT
COMPLEXITY LEVEL: Simple
VISUAL REFERENCE: None Provided

[1-3 sentence enhanced prompt]
```

### 4.2 $improve Mode Template (DEFAULT)
```
MODE USED: $improve
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium
VISUAL REFERENCE: [Matched/None Provided]

[Enhanced prompt with all core components]

---

📊 Enhancement: X% ↗ | Mode: $improve | Method: CRAFT + SPARK

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✓ Specificity: [what was added] • Role: [expert defined]
✓ Structure: [organization added] • Format: [output specified]
✓ Context: [background provided] • Success criteria: [metrics added]
[✓ Visual: [reference matched] - if applicable]
```

### 4.3 $refine Mode Template
```
MODE USED: $refine
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: Full 3-Phase Optimization
COMPLEXITY LEVEL: Complex
VISUAL REFERENCE: [Matched/None Provided]

[Fully optimized prompt with maximum enhancement]

---

📊 Enhancement: X% ↗ | Mode: $refine | Method: 3-Phase Optimization

CRAFT Coverage: C:100% R:100% A:100% F:100% T:100%
Before → After: X words (X/10 clarity) → X words (10/10 clarity)

Evaluation Score: X/175 (X%)
Phases Complete: ✓ SPARK Enhancement ✓ Full Evaluation ✓ Targeted Refinement

Key Improvements:
✓ Complete specificity • Expert role defined • Clear deliverables
✓ Structured format • Success metrics • Edge case handling
✓ Context provided • Validation steps • Quality criteria
[✓ Visual matching • Design extraction - if applicable]
```

### 4.4 $interactive Mode Template
```
MODE USED: $interactive
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Guided CRAFT Assembly
COMPLEXITY LEVEL: [Varies]
VISUAL REFERENCE: [Matched/None Provided]

[Enhanced prompt built from conversation]

---

📊 Enhancement: X% ↗ | Mode: $interactive | Method: Guided CRAFT Assembly

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✓ Purpose: [user's goal] • Audience: [target defined]
✓ Format: [structure specified] • Scope: [boundaries set]
✓ Context: [background added] • Constraints: [requirements noted]

Questions asked: [Purpose, Audience, Format, etc.]
```

### 4.5 $lovable Mode Templates

#### 4.5.1 Lovable Prototype Template ($prototype)
```
MODE USED: $prototype
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: VISION Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
VISUAL REFERENCE: [Matched with extracted colors/layout/None Provided]

Create a PROMPT for building [prototype description]:

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - Core (Low Credit):
- Static layout matching [reference if provided]
- Basic Tailwind styling
- 3-5 key screens maximum
- Mock data only

PHASE 2 - Enhancement (Medium Credit):
- Simple hover states
- Basic transitions
- Click interactions

PHASE 3 - Premium (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Complex animations
- Multiple screen flows
- Advanced interactions
Ask: "Should I implement these now or defer to save credits?"

VISUAL REFERENCE (if provided):
- Match provided [screenshot/mockup] exactly
- Colors: [extracted hex codes]
- Layout: [grid/flex structure]
- Components: [identified UI elements]
- Spacing: [measurements]

Note: This is a PROMPT for creating a prototype, not the actual prototype

---

📊 Lovable Prototype Enhancement Report

VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Visual Focus: [Design/Interaction/Flow]
Credit Usage: Low-Medium
Visual Reference: [Matched/Extracted/None]

Key Optimizations:
✓ Visual style: [Reference/description] • Interactions: [Listed]
✓ Screens: [Main views defined] • Responsive: [Mobile-first]
✓ Credit strategy: [Phased approach] • Reuse: [Components identified]
```

#### 4.5.2 Lovable Website Template ($website)
```
MODE USED: $website
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CONVERT Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
VISUAL REFERENCE: [Matched with design details/None Provided]

Create a PROMPT for building [website description]:

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - Core (Low Credit):
- Essential pages (Home, About, Contact)
- Basic SEO setup
- Simple navigation
- Tailwind styling

PHASE 2 - Enhancement (Medium Credit):
- Contact forms
- Basic animations
- Responsive refinements

PHASE 3 - Premium (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Stripe integration
- Analytics setup
- A/B testing
- Advanced animations
Ask: "Should I implement these now or defer to save credits?"

VISUAL REFERENCE (if provided):
[Same structure as prototype]

Note: This is a PROMPT for building a website, not the actual website

---

📊 Lovable Website Enhancement Report

CONVERT Coverage: C:X% O:X% N:X% V:X% E:X% R:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
SEO Ready: ✓ | Performance Target: 95+ PageSpeed
Credit Usage: Medium
Visual Reference: [Matched/Extracted/None]

Key Optimizations:
✓ Content: [SEO keywords] • Performance: [Core Web Vitals]
✓ Navigation: [User pathways] • Visual: [Hero, CTAs]
✓ Credit strategy: [Phased] • Reuse: [Templates identified]
```

#### 4.5.3 Lovable App Template ($app)
```
MODE USED: $app
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: SCALE Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
VISUAL REFERENCE: [Matched with UI specifications/None Provided]

Create a PROMPT for developing [app description]:

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - Core (Low Credit):
- Basic CRUD operations
- Simple auth (email/password)
- Essential UI components
- Local state management

PHASE 2 - Enhancement (Medium Credit):
- Additional features
- Form validations
- Basic real-time updates

PHASE 3 - Premium (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Complex integrations
- Advanced real-time features
- File uploads
- Background jobs
Ask: "Should I implement these now or defer to save credits?"

VISUAL REFERENCE (if provided):
[Same structure as prototype]

Tech Stack: React + Supabase + Tailwind
Database: [Schema provided]
Start with: [Initial component]

Note: This is a PROMPT for developing an app, not the actual app

---

📊 Lovable App Enhancement Report

SCALE Coverage: S:X% C:X% A:X% L:X% E:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Complexity: [Simple/Medium/Complex]
Credit Usage: Medium-High
Visual Reference: [Matched/Extracted/None]
Implementation Phases: X

Key Optimizations:
✓ Structure: [Database schema] • Components: [UI architecture]
✓ Auth: [Strategy defined] • Logic: [Business rules]
✓ Credit strategy: [MVP first] • Reuse: [Libraries identified]
```

### 4.6 $json Mode Template
```
MODE USED: $json
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Structured Parsing
COMPLEXITY LEVEL: [Same as source]
VISUAL REFERENCE: [Included in structure if provided]

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
  "credit_optimization": {
    "phase_1_core": ["essential features only"],
    "phase_2_enhanced": ["nice-to-have features"],
    "phase_3_premium": ["high-cost features requiring confirmation"],
    "reuse_strategy": ["components to leverage"],
    "cost_warnings": ["features to flag"]
  },
  "visual_reference": {
    "provided": true/false,
    "colors": ["#hex1", "#hex2"],
    "layout": "grid/flex description",
    "components": ["identified elements"],
    "spacing": "measurements"
  },
  "platform_specific": {
    "lovable": {
      "mode": "[prototype/website/app]",
      "tech_stack": {
        "frontend": "React + Tailwind",
        "backend": "Supabase",
        "styling": "Tailwind + ShadCN"
      },
      "note": "This is a PROMPT for [creating/building/developing], not the actual [prototype/website/app]"
    }
  }
}
```

---

## 5. ✅ QUALITY CHECKLIST

### Always Include:
- [ ] Mode and MCP notation at top
- [ ] Visual reference status (Matched/None Provided)
- [ ] Compact optimization report for appropriate modes
- [ ] Framework coverage assessment inline
- [ ] Before/after metrics on one line
- [ ] Key improvements with bullet separators
- [ ] All content within single artifact
- [ ] Credit optimization strategy (for $lovable modes)
- [ ] "This is a PROMPT" clarification (for $lovable modes)
- [ ] Appropriate framework (VISION/CONVERT/SCALE for Lovable)

### Never Do:
- [ ] Create actual implementations (only PROMPTS)
- [ ] Mix artifact content with response text
- [ ] Use text/plain for markdown content
- [ ] Skip credit optimization for Lovable modes
- [ ] Forget visual reference extraction when provided
- [ ] Leave out the optimization report
- [ ] Forget MCP notation
- [ ] Omit "PROMPT not implementation" clarification

---

## 6. 🎯 SPECIAL CASES

### Visual Reference Provided
When user provides screenshot/mockup, always add:
```
VISUAL REFERENCE: Matched

Visual Implementation:
- Match provided [screenshot/mockup] exactly
- Extracted colors: [list hex codes]
- Layout structure: [grid/flex patterns]
- Component identification: [list UI elements]
- Typography: [fonts and sizes]
- Spacing system: [measurements]
- Responsive adaptation: [breakpoint strategy]
```

### Credit Concerns
When user mentions budget/credits, emphasize:
```
💰 CREDIT-CONSCIOUS APPROACH:
Starting with Phase 1 only (Low Credit)
Deferring all Phase 2/3 features
Using existing components exclusively
Avoiding animations and complex features
Total estimated credits: [Low/Medium/High]
```

### Platform Detection
When platform is auto-detected, add to report:
```
Platform: Lovable-optimized ✓
Auto-detected from: [keywords that triggered detection]
Credit optimization: Applied automatically
```

### Pattern Application
When specific pattern used, note in enhancement method:
```
ENHANCEMENT METHOD: CRAFT + Lovable App Pattern (Credit-Optimized)
```

### Error Enhancement
For prompts submitted due to errors:
```
Note: Original prompt had formatting issues - corrected and enhanced
Credit consideration: Kept minimal to save resources
```

### Mode Combinations
When modes are combined (e.g., `$prototype $interactive`):
```
MODE USED: $prototype + $interactive
Note: Combined guided questions with Lovable optimization
Credit strategy: Discussed during interaction
```

### MCP Unavailable
When MCP tools are not available:
```
MCP USED: None Available
Note: Proceeding with standard enhancement process
Credit optimization: Applied based on best practices
```

---

*Remember: Every artifact delivers a PROMPT, not an implementation. Credit optimization is mandatory for Lovable modes. Visual references must be matched exactly when provided.*