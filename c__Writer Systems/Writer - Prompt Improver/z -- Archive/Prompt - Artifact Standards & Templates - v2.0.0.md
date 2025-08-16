# Prompt - Artifact Standards & Templates - v2.0.0

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
   - [4.5 $lovable Mode Templates](#45-lovable-mode-templates)
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
MODE USED: [$short/$improve/$refine/$interactive/$lovable-prototype/$lovable-website/$lovable-app/$json]
MCP USED: [Sequential Thinking/Cascade Thinking/None Available]
ENHANCEMENT METHOD: [CRAFT/SPARK/Patterns/Full Framework/VISION/CONVERT/SCALE]
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

For Prototype mode, add:
```
VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Visual Focus: [Design/Interaction/Flow]
Fidelity: [Low/Medium/High]
Platform: Lovable-optimized ✓
```

For Website mode, add:
```
CONVERT Coverage: C:X% O:X% N:X% V:X% E:X% R:X% T:X%
SEO Ready: ✓ | Performance Optimized: ✓
Target Audience: [Defined]
Platform: Lovable-optimized ✓
```

For App mode, add:
```
SCALE Coverage: S:X% C:X% A:X% L:X% E:X%
Backend: Supabase ✓ | Auth: Configured ✓
Complexity: [Simple/Medium/Complex]
Implementation Phases: X
Platform: Lovable-optimized ✓
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

### 4.5 $lovable Mode Templates

#### 4.5.1 Lovable Prototype Template
```
MODE USED: $lovable-prototype
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: VISION Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM: Lovable-optimized ✓

[Enhanced prototype prompt with visual specifications]

---

📊 Lovable Prototype Enhancement Report

VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Visual Focus: [Design/Interaction/Flow]
Fidelity: [Low/Medium/High]

Key Optimizations:
✓ Visual style: [Reference/description] • Interactions: [Animations listed]
✓ Screens: [Main views defined] • Responsive: [Mobile-first approach]
✓ Components: [Reusable elements] • Data: [Dummy content strategy]

Implementation Strategy:
- Start with: [Initial screen/component]
- Focus on: [Visual polish over functionality]
- Iterate: [Quick refinement approach]
```

#### 4.5.2 Lovable Website Template
```
MODE USED: $lovable-website
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CONVERT Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM: Lovable-optimized ✓

[Enhanced website prompt with conversion focus]

---

📊 Lovable Website Enhancement Report

CONVERT Coverage: C:X% O:X% N:X% V:X% E:X% R:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
SEO Ready: ✓ | Performance Target: 95+ PageSpeed

Key Optimizations:
✓ Content: [SEO keywords, copy points] • Performance: [Core Web Vitals]
✓ Navigation: [User pathways] • Visual: [Hero, CTAs]
✓ Engagement: [Forms, chat] • Responsive: [Mobile-first]
✓ Testing: [Analytics, A/B] • Integrations: [Stripe, forms]

Implementation Order:
1. [Foundation setup]
2. [Content and SEO]
3. [Interactive elements]
4. [Performance optimization]
```

#### 4.5.3 Lovable App Template
```
MODE USED: $lovable-app
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: SCALE Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM: Lovable-optimized ✓

[Enhanced app prompt with full specifications]

---

📊 Lovable App Enhancement Report

SCALE Coverage: S:X% C:X% A:X% L:X% E:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Complexity: [Simple/Medium/Complex]
Tech Stack: React + Supabase + Tailwind

Key Optimizations:
✓ Structure: [Database schema] • Components: [UI architecture]
✓ Auth: [Strategy defined] • Logic: [Business rules]
✓ Endpoints: [APIs, real-time] • State: [Management approach]

Implementation Phases:
1. Foundation (auth, routing, layout)
2. Core features ([specific functionality])
3. Integrations (Supabase, Stripe)
4. Polish (animations, optimization)

Chat Mode Planning:
- Architecture decisions
- Database design
- Error handling strategy

Default Mode Building:
- Component implementation
- Feature development
- Testing approach
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
      "mode": "[prototype/website/app]",
      "tech_stack": {
        "frontend": "React + Tailwind",
        "backend": "Supabase",
        "styling": "Tailwind + ShadCN",
        "integrations": ["Stripe", "GitHub", "Analytics"]
      },
      "implementation_strategy": {
        "chat_mode": ["planning", "architecture", "debugging"],
        "default_mode": ["building", "implementing", "testing"]
      },
      "phases": [
        "Foundation setup",
        "Core features",
        "Integrations",
        "Polish"
      ],
      "constraints": [
        "Start with blank project",
        "Mobile-first design",
        "Incremental building"
      ]
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
- [ ] Appropriate framework (VISION/CONVERT/SCALE for Lovable)

### Never Do:
- [ ] Mix artifact content with response text
- [ ] Use text/plain for markdown content
- [ ] Include verbose Enhancement Details section
- [ ] Use progress bars or multi-line displays
- [ ] Leave out the optimization report
- [ ] Forget MCP notation
- [ ] Ignore platform requirements (for $lovable)
- [ ] Use conflicting frameworks (APP/BUILD removed)

---

## 6. 🎯 SPECIAL CASES

### Platform Detection
When platform is auto-detected, add to report:
```
Platform: Lovable-optimized ✓
Auto-detected from: [keywords that triggered detection]
```

### Pattern Application
When specific pattern used, note in enhancement method:
```
ENHANCEMENT METHOD: CRAFT + Lovable App Pattern
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
MODE USED: $lovable-app + $interactive
Note: Combined guided questions with Lovable optimization
```

### MCP Unavailable
When MCP tools are not available:
```
MCP USED: None Available
Note: Proceeding with standard enhancement process
```

---

*Remember: The compact format reduces cognitive load while maintaining all essential information. Every line should provide value. Always use the appropriate framework for Lovable modes: VISION (Prototype), CONVERT (Website), or SCALE (App).*