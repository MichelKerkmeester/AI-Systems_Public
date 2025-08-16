# Artifact Standards & Templates - v2.2.0

This document defines mandatory standards for delivering enhanced prompts via artifacts.

## Table of Contents

1. [📦 ARTIFACT DELIVERY STANDARDS](#1--artifact-delivery-standards)
2. [🎯 MANDATORY ARTIFACT STRUCTURE](#2--mandatory-artifact-structure)
3. [📊 COMPACT OPTIMIZATION REPORT](#3--compact-optimization-report)
4. [🎨 MODE-SPECIFIC TEMPLATES](#4--mode-specific-templates)
5. [✅ QUALITY CHECKLIST](#5--quality-checklist)
6. [🎯 SPECIAL CASES](#6--special-cases)

---

## 1. 📦 ARTIFACT DELIVERY STANDARDS

**🚨 CRITICAL:** 
- Always use `text/markdown` artifact type when delivering enhanced prompts!
- Every Lovable prompt is a creative brief, NOT prescriptive specifications!
- Include goals and mood, NOT specific HTML/CSS or rigid designs!

Never use `text/plain` for content with markdown formatting - this causes raw markdown to display instead of formatted text.

### Artifact Type Warning:
**Never make these mistakes:**
- Using `text/plain` → Causes raw markdown display
- Creating prescriptive implementations → We create creative briefs
- Specifying exact designs → We provide direction and goals
- Including HTML/CSS → We describe outcomes, not code
- Missing "This is a PROMPT" clarification → Causes confusion

**Always deliver enhanced prompts with:**
- Proper `text/markdown` type
- Creative direction and mood
- Goals and success criteria
- Credit optimization strategy
- Freedom areas for AI exploration
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
CREATIVE APPROACH: [Goals-Focused/Exploration-Based/Outcome-Driven]

[Enhanced prompt here - with creative direction, not specifications]

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
✔ [Improvement 1] • [Improvement 2]
✔ [Improvement 3] • [Improvement 4]
✔ [Additional improvements as needed]

[Additional mode-specific info if needed]
```

### Lovable Mode Additional Metrics (v3.0)

For Prototype mode, add:
```
VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Creative Focus: [Exploration/Concept/Experience]
Credit Usage: Low-Medium
Credit Strategy: Explore first, enhance what works
Creative Freedom: [Areas for experimentation]
Note: This is a creative exploration brief, not prescriptive specs
```

For Website mode, add:
```
CONVERT Coverage: C:X% O:X% N:X% V:X% E:X% R:X% T:X%
Strategic Focus: [Conversion/Engagement/Brand]
Credit Usage: Medium
Credit Strategy: Core message first, enhance engagement
Creative Direction: [Mood, personality, feelings]
Note: This is a strategic brief for goals, not a template
```

For App mode, add:
```
SCALE Coverage: S:X% C:X% A:X% L:X% E:X%
Functional Focus: [Workflows/Experience/Value]
Complexity: [Simple/Medium/Complex]
Credit Usage: Medium-High
Credit Strategy: MVP functionality, enhance based on usage
User Experience Goals: [Feelings and outcomes]
Note: This is a requirements brief with creative freedom
```

---

## 4. 🎨 MODE-SPECIFIC TEMPLATES

### 4.1 $short Mode Template
```
MODE USED: $short
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Essential CRAFT
COMPLEXITY LEVEL: Simple
CREATIVE APPROACH: Goals-Focused

[1-3 sentence enhanced prompt with clear goals]
```

### 4.2 $improve Mode Template (DEFAULT)
```
MODE USED: $improve
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium
CREATIVE APPROACH: [Outcome-Driven/Goals-Focused]

[Enhanced prompt with goals and direction, not specifications]

---

📊 Enhancement: X% ↗ | Mode: $improve | Method: CRAFT + SPARK

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✔ Goals clarified • Success defined
✔ Mood established • Freedom areas identified
✔ Context provided • Outcomes specified
```

### 4.3 $refine Mode Template
```
MODE USED: $refine
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: Full 3-Phase Optimization
COMPLEXITY LEVEL: Complex
CREATIVE APPROACH: Comprehensive Goals & Direction

[Fully optimized prompt with complete creative brief]

---

📊 Enhancement: X% ↗ | Mode: $refine | Method: 3-Phase Optimization

CRAFT Coverage: C:100% R:100% A:100% F:100% T:100%
Before → After: X words (X/10 clarity) → X words (10/10 clarity)

Evaluation Score: X/175 (X%)
Phases Complete: ✔ SPARK Enhancement ✔ Full Evaluation ✔ Targeted Refinement

Key Improvements:
✔ Complete creative direction • Clear success metrics
✔ User experience goals • Phased implementation
✔ Mood and personality • Freedom for innovation
```

### 4.4 $interactive Mode Template
```
MODE USED: $interactive
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Guided CRAFT Assembly
COMPLEXITY LEVEL: [Varies]
CREATIVE APPROACH: User-Guided Direction

[Enhanced prompt built from conversation with creative goals]

---

📊 Enhancement: X% ↗ | Mode: $interactive | Method: Guided Assembly

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✔ Purpose: [user's goal] • Audience: [target defined]
✔ Success: [outcomes] • Mood: [feelings established]
✔ Context: [background] • Freedom: [exploration areas]

Questions asked: [Purpose, Audience, Success Criteria, etc.]
```

### 4.5 $lovable Mode Templates (v3.0)

#### 4.5.1 Lovable Prototype Template ($prototype)
```
MODE USED: $prototype
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: VISION Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
CREATIVE APPROACH: Exploration-Based

Create a PROMPT for exploring [concept description]:

EXPLORATION BRIEF:
Purpose: [What we're investigating]
Success: [What we'll learn or achieve]
Users should feel: [Emotional targets]

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - Concept Exploration (Low Credit):
- Explore different approaches to [core need]
- Test various [interaction/layout] patterns
- Focus on [primary goal]
- Keep simple for rapid iteration

PHASE 2 - Enhancement (Medium Credit):
- Build on successful patterns from Phase 1
- Add personality and polish
- Refine based on insights

PHASE 3 - Premium (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Complex animations
- Advanced interactions
- Multiple user flows
Ask: "Should we explore these premium features?"

CREATIVE DIRECTION:
- Mood: [Adjectives describing desired feel]
- Inspiration: [Concepts, not specific designs]
- Users should feel: [Emotional journey]
- Freedom to explore: [Areas for creativity]

SUCCESS CRITERIA:
- Users can: [Functional outcomes]
- Users feel: [Emotional outcomes]
- We learn: [Discovery goals]

Note: This is a creative exploration brief, not design specifications

---

📊 Lovable Prototype Enhancement Report

VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Creative Focus: [Exploration/Concept/Experience]
Credit Usage: Low-Medium
Creative Freedom: High

Key Optimizations:
✔ Exploration goals defined • User feelings targeted
✔ Mood established • Freedom areas identified
✔ Credit phasing clear • Success criteria set
```

#### 4.5.2 Lovable Website Template ($website)
```
MODE USED: $website
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: CONVERT Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
CREATIVE APPROACH: Goal-Oriented

Create a PROMPT for building [website description]:

STRATEGIC BRIEF:
Primary goal: [Conversion/engagement metric]
Target audience: [User description]
Success criteria: [Measurable outcomes]

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - Core Foundation (Low Credit):
- Essential message and value
- Clear user pathways
- Trust indicators
- Mobile-responsive approach

PHASE 2 - Engagement (Medium Credit):
- Enhanced storytelling
- Interactive elements
- Social proof
- Conversion optimization

PHASE 3 - Premium (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Advanced analytics
- Personalization
- A/B testing framework
- Marketing automation
Ask: "Implement these premium features now?"

BRAND PERSONALITY:
- Feel: [Emotional qualities]
- Tone: [Communication style]
- Values: [What to convey]

CREATIVE DIRECTION:
- Mood: [Visual and emotional direction]
- User journey: [Emotional progression]
- Freedom to explore: [Design areas]
- Optimize for: [Primary objectives]

SUCCESS METRICS:
- Immediate: [First impression goals]
- Engagement: [Interaction metrics]
- Conversion: [Action targets]

Note: This is a strategic brief for achieving goals, not a rigid template

---

📊 Lovable Website Enhancement Report

CONVERT Coverage: C:X% O:X% N:X% V:X% E:X% R:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Strategic Focus: [Goals/Conversion/Brand]
Credit Usage: Medium
Creative Direction: Complete

Key Optimizations:
✔ Goals clarified • Brand personality defined
✔ User journey mapped • Success metrics set
✔ Credit strategy phased • Creative freedom preserved
```

#### 4.5.3 Lovable App Template ($app)
```
MODE USED: $app
MCP USED: Cascade Thinking
ENHANCEMENT METHOD: SCALE Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
CREATIVE APPROACH: Functionality-Focused

Create a PROMPT for developing [app description]:

FUNCTIONAL BRIEF:
Core purpose: [What users accomplish]
Key workflows: [Main user tasks]
Success criteria: [Measurable outcomes]

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - MVP Core (Low Credit):
- Essential functionality
- Core user workflows
- Simple, effective interface
- Focus on primary value

PHASE 2 - Enhanced Experience (Medium Credit):
- Improved workflows based on usage
- Additional valuable features
- Better user experience
- Refined interactions

PHASE 3 - Premium Features (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Complex integrations
- Real-time features
- Advanced analytics
- Automation features
Ask: "Should we add these premium features?"

USER EXPERIENCE GOALS:
- Users should feel: [Emotional targets]
- Interface should be: [Qualities]
- Workflows should: [Characteristics]
- Success looks like: [User outcomes]

CREATIVE FREEDOM:
- Explore approaches to: [UI/UX challenges]
- Experiment with: [Interaction patterns]
- Consider: [Modern best practices]
- Optimize for: [User needs]

TECHNICAL GUIDANCE:
- Core requirements: [Must-haves]
- Performance targets: [If relevant]
- Constraints: [Any limitations]

Note: This is a requirements brief with room for creative solutions

---

📊 Lovable App Enhancement Report

SCALE Coverage: S:X% C:X% A:X% L:X% E:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)
Functional Focus: [Workflows/Experience/Value]
Complexity: [Simple/Medium/Complex]
Credit Usage: Medium-High
User Experience: Defined

Key Optimizations:
✔ Workflows clarified • User feelings defined
✔ Success criteria set • Phased approach clear
✔ Creative freedom areas • Technical guidance balanced
```

### 4.6 $json Mode Template (v3.0)
```
MODE USED: $json
MCP USED: Sequential Thinking
ENHANCEMENT METHOD: Structured Parsing
COMPLEXITY LEVEL: [Same as source]
CREATIVE APPROACH: Structured Goals

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
    "outcomes": "[what success looks like]",
    "user_impact": "[how users should feel/benefit]"
  },
  "creative_direction": {
    "mood": "[adjectives describing feel]",
    "personality": "[brand/product character]",
    "user_feelings": "[emotional targets]",
    "exploration_areas": "[where AI has freedom]"
  },
  "credit_optimization": {
    "phase_1_core": {
      "features": ["essential capabilities"],
      "approach": "explore and validate",
      "credits": "low"
    },
    "phase_2_enhanced": {
      "features": ["improvements based on Phase 1"],
      "approach": "build on success",
      "credits": "medium"
    },
    "phase_3_premium": {
      "features": ["complex capabilities"],
      "requires_confirmation": true,
      "credits": "high"
    }
  },
  "platform_specific": {
    "lovable": {
      "mode": "[prototype/website/app]",
      "philosophy": "goals over specifications",
      "creative_freedom": "high",
      "note": "This is a creative brief, not prescriptive implementation"
    }
  }
}
```

---

## 5. ✅ QUALITY CHECKLIST

### Always Include:
- [ ] Mode and MCP notation at top
- [ ] Creative approach classification
- [ ] Goals and success criteria (not specifications)
- [ ] Mood and personality (not exact designs)
- [ ] User feelings and emotions
- [ ] Compact optimization report for appropriate modes
- [ ] Framework coverage assessment inline
- [ ] Before/after metrics on one line
- [ ] Key improvements with bullet separators
- [ ] All content within single artifact
- [ ] Credit optimization strategy (for $lovable modes)
- [ ] Creative freedom areas (for $lovable modes)
- [ ] "This is a PROMPT" clarification

### Never Do:
- [ ] Include specific HTML/CSS code
- [ ] Specify exact colors or measurements
- [ ] Define rigid layouts or components
- [ ] Create prescriptive implementations
- [ ] Mix artifact content with response text
- [ ] Use text/plain for markdown content
- [ ] Skip creative direction for Lovable modes
- [ ] Forget exploration areas
- [ ] Leave out the optimization report
- [ ] Forget MCP notation
- [ ] Omit "PROMPT not implementation" clarification

---

## 6. 🎯 SPECIAL CASES

### Creative Direction Provided
When user wants specific mood/feel:
```
CREATIVE DIRECTION: Provided

Mood & Personality:
- Overall feeling: [User's description]
- Brand character: [Defined traits]
- Emotional targets: [User's goals]

Freedom Areas:
- Explore different approaches to achieve [mood]
- Experiment with [relevant design elements]
- Consider modern interpretations of [style]
```

### Extreme Budget Constraints
When user emphasizes minimal credits:
```
💰 BUDGET-CONSCIOUS APPROACH:
Phase 1 Only Implementation
- Core functionality only
- Simplest effective solutions
- No enhancements
- Defer all non-essentials

Success with constraints:
- Still achieves: [primary goal]
- Users still feel: [core emotion]
- Value delivered: [essential benefit]
```

### Platform Auto-Detection
When Lovable platform detected:
```
Platform: Lovable-optimized ✔
Auto-detected from: [keywords that triggered]
Approach: Creative brief with goals
Freedom level: High
```

### Pattern Application
When specific pattern used:
```
ENHANCEMENT METHOD: CRAFT + Creative Direction Pattern
Focus: Goals and outcomes over specifications
```

### Exploration Request
When user wants to explore concepts:
```
EXPLORATION MODE: Active
Purpose: Discover what works
Approach: Multiple simple concepts first
Strategy: Enhance only validated ideas
```

### Mode Combinations
When modes are combined:
```
MODE USED: $prototype + $interactive
Approach: Guided exploration brief
Creative input: Gathered through conversation
Freedom: Preserved throughout
```

### MCP Unavailable
When MCP tools are not available:
```
MCP USED: None Available
Note: Proceeding with standard enhancement
Creative direction: Applied based on best practices
```

---

*Remember: Every artifact delivers a creative brief with goals and direction, not prescriptive implementations. Focus on outcomes, mood, and user experience while giving AI freedom to innovate.*