# Prompt Evaluation & Refinement - v2.0.0

**Systematic quality assessment and improvement workflows** for optimizing prompts through structured evaluation and targeted refinement.

**Note:** The Full Mode (`$full`) automatically applies this evaluation and refinement framework in a three-phase process. Use manual evaluation/refinement when you need more control or want to skip phases.

## Table of Contents

1. [⚡ QUICK EVAL MODE (10 CRITERIA)](#1--quick-eval-mode-10-criteria)
2. [📊 FULL EVALUATION MODE (35 CRITERIA)](#2--full-evaluation-mode-35-criteria)
   - [2.1 Group 1: Clarity (1-5)](#21-group-1-clarity-1-5)
   - [2.2 Group 2: Context (6-10)](#22-group-2-context-6-10)
   - [2.3 Group 3: Reasoning (11-15)](#23-group-3-reasoning-11-15)
   - [2.4 Group 4: Advanced (16-20)](#24-group-4-advanced-16-20)
   - [2.5 Group 5: Thinking (21-25)](#25-group-5-thinking-21-25)
   - [2.6 Group 6: Output (26-30)](#26-group-6-output-26-30)
   - [2.7 Group 7: Meta (31-35)](#27-group-7-meta-31-35)
3. [🎨 LOVABLE-SPECIFIC EVALUATION](#3--lovable-specific-evaluation)
   - [3.1 Prototype Mode Criteria](#31-prototype-mode-criteria)
   - [3.2 Website Mode Criteria](#32-website-mode-criteria)
   - [3.3 App Mode Criteria](#33-app-mode-criteria)
4. [📊 SCORING GUIDE](#4--scoring-guide)
5. [🔄 REFINEMENT WORKFLOW](#5--refinement-workflow)
   - [5.1 Step 1: Analyze Evaluation](#51-step-1-analyze-evaluation)
   - [5.2 Step 2: Apply Targeted Fixes](#52-step-2-apply-targeted-fixes)
   - [5.3 Step 3: Enhancement Patterns](#53-step-3-enhancement-patterns)
   - [5.4 Step 4: Validation](#54-step-4-validation)
6. [📝 REFINEMENT EXAMPLES](#6--refinement-examples)
   - [6.1 Example 1: Clarity Enhancement](#61-example-1-clarity-enhancement)
   - [6.2 Example 2: Format Enhancement](#62-example-2-format-enhancement)
   - [6.3 Example 3: Context Enhancement](#63-example-3-context-enhancement)
   - [6.4 Example 4: Lovable Enhancement](#64-example-4-lovable-enhancement)
7. [🎯 COMMON REFINEMENT PATTERNS](#7--common-refinement-patterns)
   - [7.1 The Vague Request](#71-the-vague-request)
   - [7.2 The Formatless Output](#72-the-formatless-output)
   - [7.3 The Contextless Task](#73-the-contextless-task)
   - [7.4 The Lovable Request](#74-the-lovable-request)
   - [7.5 🎯 MANUAL VS FULL MODE DECISION GUIDE](#75--manual-vs-full-mode-decision-guide)
8. [⚡ SPEED REFINEMENT CHECKLIST](#8--speed-refinement-checklist)

---

## 1. ⚡ QUICK EVAL MODE (10 CRITERIA)

For Sonnet or rapid assessments, evaluate these core criteria:

1. **Clarity & Specificity** - Is the task clear and specific?
2. **Context / Background Provided** - Sufficient context given?
3. **Explicit Task Definition** - Clear what to do?
4. **Feasibility within Model Constraints** - Realistic request?
5. **Avoiding Ambiguity or Contradictions** - No conflicts?
6. **Model Fit / Scenario Appropriateness** - Right tool for job?
7. **Desired Output Format / Style** - Format specified?
8. **Use of Role or Persona** - Role defined?
9. **Step-by-Step Reasoning Encouraged** - Process clear?
10. **Structured / Numbered Instructions** - Well organized?

**Quick Eval Template:**
```markdown
QUICK EVALUATION REPORT
Total Score: X/50 (X%)

Top Strengths:
1. [Highest scoring aspect]
2. [Second highest]

Critical Improvements:
1. [Lowest scoring] → [Specific fix]
2. [Second lowest] → [Specific fix]
3. [Third lowest] → [Specific fix]
```

---

## 2. 📊 FULL EVALUATION MODE (35 CRITERIA)

### 2.1 Group 1: Clarity (1-5)
1. **Clarity & Specificity**
2. **Context / Background Provided**
3. **Explicit Task Definition**
4. **Feasibility within Model Constraints**
5. **Avoiding Ambiguity or Contradictions**

### 2.2 Group 2: Context (6-10)
6. **Model Fit / Scenario Appropriateness**
7. **Desired Output Format / Style**
8. **Use of Role or Persona**
9. **Step-by-Step Reasoning Encouraged**
10. **Structured / Numbered Instructions**

### 2.3 Group 3: Reasoning (11-15)
11. **Brevity vs. Detail Balance**
12. **Iteration / Refinement Potential**
13. **Examples or Demonstrations**
14. **Handling Uncertainty / Gaps**
15. **Hallucination Minimization**

### 2.4 Group 4: Advanced (16-20)
16. **Knowledge Boundary Awareness**
17. **Audience Specification**
18. **Style Emulation or Imitation**
19. **Memory Anchoring (Multi-Turn Systems)**
20. **Meta-Cognition Triggers**

### 2.5 Group 5: Thinking (21-25)
21. **Divergent vs. Convergent Thinking Management**
22. **Hypothetical Frame Switching**
23. **Safe Failure Mode**
24. **Progressive Complexity**
25. **Alignment with Evaluation Metrics**

### 2.6 Group 6: Output (26-30)
26. **Calibration Requests**
27. **Output Validation Hooks**
28. **Time/Effort Estimation Request**
29. **Ethical Alignment or Bias Mitigation**
30. **Limitations Disclosure**

### 2.7 Group 7: Meta (31-35)
31. **Compression / Summarization Ability**
32. **Cross-Disciplinary Bridging**
33. **Emotional Resonance Calibration**
34. **Output Risk Categorization**
35. **Self-Repair Loops**

**Full Eval Template:**
```markdown
FULL EVALUATION REPORT
Total Score: X/175 (X%)

[Groups 1-7 with scores]

Top Strengths:
1. [Highest scoring aspect]
2. [Second highest]
3. [Third highest]

Critical Improvements:
1. [Lowest scoring] → [Specific fix]
2. [Second lowest] → [Specific fix]
3. [Third lowest] → [Specific fix]
[Continue to 7-10 suggestions]
```

---

## 3. 🎨 LOVABLE-SPECIFIC EVALUATION

When evaluating Lovable prompts, add these specialized criteria:

### 3.1 Prototype Mode Criteria

**Visual Design (10 points each):**
1. **Visual Hierarchy Clarity** - Are layout priorities clear?
2. **Interaction Design Quality** - Are animations purposeful?
3. **Mobile Responsiveness** - Does it adapt to all screens?
4. **Animation Purposefulness** - Do animations enhance UX?
5. **Component Reusability** - Are elements modular?

**Evaluation Template:**
```markdown
LOVABLE PROTOTYPE EVALUATION
Visual Score: X/50 (X%)

Strengths:
- [Visual aspect done well]
- [Interaction highlight]

Needs Improvement:
- Visual hierarchy: [specific fix]
- Animations: [enhancement needed]
- Mobile design: [responsive issue]
```

### 3.2 Website Mode Criteria

**Conversion & Performance (10 points each):**
1. **SEO Optimization Completeness** - Meta tags, schema, sitemap?
2. **Performance Metrics** - Core Web Vitals targets?
3. **Conversion Path Clarity** - Clear user journey?
4. **Content Structure** - Information architecture solid?
5. **Analytics Integration** - Tracking specified?

**Evaluation Template:**
```markdown
LOVABLE WEBSITE EVALUATION
Conversion Score: X/50 (X%)

Strengths:
- [SEO aspect covered]
- [Performance consideration]

Needs Improvement:
- SEO: [missing elements]
- Performance: [optimization needed]
- Conversion: [CTA improvements]
```

### 3.3 App Mode Criteria

**Technical Architecture (10 points each):**
1. **Database Schema Efficiency** - Well-structured data?
2. **Authentication Robustness** - Security considered?
3. **State Management Clarity** - Data flow defined?
4. **API Design Quality** - Endpoints logical?
5. **Real-time Features Implementation** - Subscriptions planned?

**Evaluation Template:**
```markdown
LOVABLE APP EVALUATION
Technical Score: X/50 (X%)

Strengths:
- [Database design aspect]
- [Auth implementation]

Needs Improvement:
- Schema: [normalization needed]
- State: [management approach]
- Real-time: [subscription strategy]
```

---

## 4. 📊 SCORING GUIDE

**5/5 - Excellent:** Clear, specific, with examples and edge cases handled
**4/5 - Good:** Clear and specific, minor improvements possible
**3/5 - Adequate:** Functional but lacks precision or detail
**2/5 - Weak:** Vague or ambiguous, needs significant improvement
**1/5 - Poor:** Unclear, contradictory, or missing entirely

**Calibration Tip:** For any criterion, briefly explain what a 1/5 versus 5/5 looks like.

**Lovable-Specific Calibration:**
- **5/5:** Complete platform optimization with all technical details
- **4/5:** Good coverage with minor platform-specific gaps
- **3/5:** Basic Lovable structure without optimization
- **2/5:** Generic prompt not optimized for Lovable
- **1/5:** Missing critical Lovable requirements

---

## 5. 🔄 REFINEMENT WORKFLOW

**Note:** This workflow is automated in Full Mode (`$full`). Use manual refinement for targeted improvements.

### 5.1 Step 1: Analyze Evaluation
- Identify scores below 3/5 (critical issues)
- Note patterns in weaknesses
- Preserve elements scoring 4-5/5
- Check for Lovable-specific gaps

### 5.2 Step 2: Apply Targeted Fixes
**For each low-scoring criterion:**

| Issue | Quick Fix | Example |
|-------|-----------|---------|
| Unclear task (1-2/5) | Add action verb + specific deliverable | "Analyze..." → "Analyze customer churn data to identify top 3 causes" |
| Missing role (1-2/5) | Add expertise definition | "You are a [role]..." → "You are a data scientist specializing in retention" |
| No format (1-2/5) | Specify structure | Add: "Format: Executive summary + detailed findings + recommendations" |
| Vague context (1-2/5) | Add relevant background | Add: "Context: B2B SaaS with 20% monthly churn, target <5%" |
| No examples (1-2/5) | Include 1-2 samples | Add: "Example insight: 'Users who don't activate feature X within 7 days churn 3x more'" |
| No Lovable specs | Add platform details | Add: "Tech: React + Supabase, Start with: Dashboard component" |

### 5.3 Step 3: Enhancement Patterns
Based on evaluation patterns, apply these enhancements:

**Pattern: Low Clarity Scores (1-5 avg)**
- Break into numbered steps
- Add specific metrics/quantities
- Include concrete deliverables

**Pattern: Low Context Scores (6-10 avg)**
- Add output format specifications
- Include role and audience definition
- Define structure and organization

**Pattern: Low Advanced Scores (11+ avg)**
- Add reasoning requirements
- Include validation steps
- Specify edge case handling

**Pattern: Low Lovable Scores**
- Add framework coverage (VISION/CONVERT/SCALE)
- Include tech stack specifications
- Define implementation phases
- Add Chat vs Default mode strategy

### 5.4 Step 4: Validation
Before finalizing:
- ✅ Re-score against failed criteria
- ✅ Ensure original intent preserved
- ✅ Verify improvements don't add unnecessary complexity
- ✅ Check enhancement maintains appropriate scope
- ✅ Validate Lovable optimizations if applicable

---

## 6. 📝 REFINEMENT EXAMPLES

### 6.1 Example 1: Clarity Enhancement
**Before (2/5):** "Help with marketing"
**After (5/5):** "As a digital marketing strategist, create a 90-day campaign plan to increase B2B software trials by 25%. Include channel mix, budget allocation, and weekly KPIs."

### 6.2 Example 2: Format Enhancement
**Before (2/5):** "Analyze this data and tell me what you find"
**After (4/5):** "Analyze this sales data to identify trends and anomalies. Format: 1) Executive summary (3 key findings), 2) Detailed analysis with charts, 3) Action recommendations"

### 6.3 Example 3: Context Enhancement
**Before (2/5):** "Write about productivity"
**After (5/5):** "Write a 1000-word guide on productivity for remote software developers. Cover: time management, deep work strategies, and tool recommendations. Tone: practical and encouraging."

### 6.4 Example 4: Lovable Enhancement
**Before (2/5):** "Build a todo app"
**After (5/5):** "Create a todo application using React + Supabase. Features: user auth (email/password), CRUD operations with real-time sync, task categories with colors. Start with dashboard component showing task list and stats. Database: todos table with user_id, title, completed, category. Mobile-first responsive design using Tailwind."

---

## 7. 🎯 COMMON REFINEMENT PATTERNS

### 7.1 The Vague Request
**Indicators:** Scores 1-2 on criteria 1-3
**Fix:** Add WHO + WHAT + WHY + HOW
**Template:** "As a [role], [do what] for [purpose] using [approach]"

### 7.2 The Formatless Output
**Indicators:** Low scores on criteria 7, format specs
**Fix:** Add structure + examples + specifications
**Template:** "Format: [structure]. Example: [sample]. Length: [range]"

### 7.3 The Contextless Task
**Indicators:** Low scores on criteria 2, 5, 8
**Fix:** Add background + audience + constraints
**Template:** "Context: [situation]. For: [audience]. Constraints: [limits]"

### 7.4 The Lovable Request
**Indicators:** Platform development without specifications
**Fix:** Add tech stack + features + implementation order
**Template:** "Build [type] with React + Supabase. Features: [list]. Start with: [component]. Implement: [phases]"

---

### 7.5 🎯 MANUAL VS FULL MODE DECISION GUIDE

**Use Manual Evaluation/Refinement when:**
- You only need to check quality (evaluate only)
- You have specific evaluation feedback to address
- You want to control which improvements to make
- Time is critical and you need quick fixes
- You're learning prompt engineering and want to understand the process
- Evaluating Lovable-specific aspects only

**Use Full Mode when:**
- You want comprehensive optimization automatically
- Quality is more important than speed
- You're creating reusable prompt templates
- The prompt will be used frequently
- You want the best possible result without manual work
- Need both standard and Lovable optimization

---

## 8. ⚡ SPEED REFINEMENT CHECKLIST

For quick improvements, check these in order:
1. [ ] Is the task crystal clear? If not → Add specifics
2. [ ] Is there a defined role? If not → Add expertise
3. [ ] Is output format specified? If not → Add structure
4. [ ] Is context provided? If not → Add background
5. [ ] Are there examples? If not → Add 1-2 samples
6. [ ] For Lovable: Tech stack defined? If not → Add React + Supabase
7. [ ] For Lovable: Starting point clear? If not → Add initial component
8. [ ] For Lovable: Features listed? If not → Add core functionality

**Stop when prompt reaches "good enough" - not every prompt needs all enhancements.**