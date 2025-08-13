# Evaluation & Refinement - v2.1.0

**Systematic quality assessment and improvement workflows** for optimizing prompts through structured evaluation and targeted refinement, with credit optimization and visual matching support.

**Note:** The Full Mode (`$refine`) automatically applies this evaluation and refinement framework in a three-phase process. Use manual evaluation/refinement when you need more control or want to skip phases.

## Table of Contents

1. [⚡ QUICK EVAL MODE (10 CRITERIA)](#1--quick-eval-mode-10-criteria)
2. [📊 FULL EVALUATION MODE (35 CRITERIA)](#2--full-evaluation-mode-35-criteria)
3. [🎨 LOVABLE-SPECIFIC EVALUATION](#3--lovable-specific-evaluation)
4. [💰 CREDIT OPTIMIZATION EVALUATION](#4--credit-optimization-evaluation)
5. [🎯 VISUAL REFERENCE EVALUATION](#5--visual-reference-evaluation)
6. [📊 SCORING GUIDE](#6--scoring-guide)
7. [🔄 REFINEMENT WORKFLOW](#7--refinement-workflow)
8. [📝 REFINEMENT EXAMPLES](#8--refinement-examples)
9. [🎯 COMMON REFINEMENT PATTERNS](#9--common-refinement-patterns)
10. [⚡ SPEED REFINEMENT CHECKLIST](#10--speed-refinement-checklist)

---

## 1. ⚡ QUICK EVAL MODE (10 CRITERIA)

For rapid assessments, evaluate these core criteria:

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

### Groups 1-7: Standard Criteria
[Previous 35 criteria remain the same...]

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

**CRITICAL:** Remember we're evaluating PROMPTS for building things, not actual implementations!

When evaluating Lovable prompts, add these specialized criteria:

### 3.1 Prototype Mode Criteria ($prototype)

**Visual Design PROMPT Quality (10 points each):**
1. **Visual Hierarchy Clarity** - Does PROMPT specify layout priorities?
2. **Interaction Design Quality** - Are animations described purposefully?
3. **Mobile Responsiveness** - Does PROMPT include responsive requirements?
4. **Animation Purposefulness** - Are animation needs clearly stated?
5. **Component Reusability** - Does PROMPT encourage modular elements?
6. **Credit Optimization** - Are phases clearly defined?
7. **Visual Reference Matching** - Are extracted details included?

**Evaluation Template:**
```markdown
LOVABLE PROTOTYPE PROMPT EVALUATION
Visual Score: X/70 (X%)
Credit Strategy: ✓ Included / ✗ Missing

Strengths:
- [Visual aspect well-specified]
- [Credit phases clearly defined]

Needs Improvement:
- Visual hierarchy: [specify in PROMPT]
- Credit optimization: [add phased approach]
- Visual matching: [extract from reference]

Note: Evaluating the PROMPT quality, not an actual prototype
```

### 3.2 Website Mode Criteria ($website)

**Conversion & Performance PROMPT Quality (10 points each):**
1. **SEO Optimization Completeness** - PROMPT includes meta tags, schema?
2. **Performance Metrics** - Core Web Vitals targets specified?
3. **Conversion Path Clarity** - User journey defined in PROMPT?
4. **Content Structure** - Information architecture described?
5. **Analytics Integration** - Tracking requirements stated?
6. **Credit Phasing** - Core vs. enhancement features separated?
7. **Visual Design Specs** - Layout/colors extracted if reference provided?

**Evaluation Template:**
```markdown
LOVABLE WEBSITE PROMPT EVALUATION
Conversion Score: X/70 (X%)
Credit Strategy: ✓ Phased / ✗ Missing

Strengths:
- [SEO requirements covered]
- [Credit optimization included]

Needs Improvement:
- SEO: [add to PROMPT]
- Credit phases: [separate features]
- Visual specs: [extract from reference]

Note: Evaluating the PROMPT quality, not an actual website
```

### 3.3 App Mode Criteria ($app)

**Technical Architecture PROMPT Quality (10 points each):**
1. **Database Schema Efficiency** - Well-structured data in PROMPT?
2. **Authentication Robustness** - Security approach specified?
3. **State Management Clarity** - Data flow defined in PROMPT?
4. **API Design Quality** - Endpoints described logically?
5. **Real-time Features Implementation** - Subscriptions planned?
6. **Credit Optimization** - MVP vs. complex features separated?
7. **Visual UI Specifications** - Component details from reference?

**Evaluation Template:**
```markdown
LOVABLE APP PROMPT EVALUATION
Technical Score: X/70 (X%)
Credit Strategy: ✓ MVP-first / ✗ Missing

Strengths:
- [Database design specified]
- [Credit phases defined]

Needs Improvement:
- Schema: [add to PROMPT]
- Credit strategy: [flag high-cost features]
- UI specs: [extract from visual reference]

Note: Evaluating the PROMPT quality, not an actual app
```

---

## 4. 💰 CREDIT OPTIMIZATION EVALUATION

**New criteria for all Lovable prompts:**

### Credit Strategy Scoring (0-50 points)
1. **Phased Implementation** (10 pts) - Are phases clearly defined?
2. **Feature Prioritization** (10 pts) - Core vs. nice-to-have separated?
3. **High-Cost Warnings** (10 pts) - Complex features flagged?
4. **Reuse Strategy** (10 pts) - Existing components identified?
5. **Incremental Approach** (10 pts) - Build progressively stated?

**Credit Evaluation Template:**
```markdown
CREDIT OPTIMIZATION EVALUATION
Score: X/50 (X%)

✓ Phased approach (Phase 1/2/3 defined)
✓ Feature prioritization (MVP identified)
✓ Cost warnings (High-credit features flagged)
✓ Reuse strategy (Components to leverage)
✓ Incremental building (Start simple)

Missing:
- [Specific credit optimization needed]
```

---

## 5. 🎯 VISUAL REFERENCE EVALUATION

**When visual references are provided (0-50 points):**

### Visual Matching Scoring
1. **Color Extraction** (10 pts) - Hex codes identified?
2. **Layout Structure** (10 pts) - Grid/flex patterns described?
3. **Component Identification** (10 pts) - UI elements listed?
4. **Spacing System** (10 pts) - Measurements specified?
5. **Responsive Strategy** (10 pts) - Adaptation approach stated?

**Visual Reference Template:**
```markdown
VISUAL REFERENCE EVALUATION
Score: X/50 (X%)

Extracted from reference:
✓ Colors: [hex codes listed]
✓ Layout: [structure identified]
✓ Components: [elements listed]
✓ Spacing: [system defined]
✓ Responsive: [strategy stated]

Missing extractions:
- [Details not captured from reference]
```

---

## 6. 📊 SCORING GUIDE

**5/5 - Excellent:** Clear, specific, with examples, phases, and credit optimization
**4/5 - Good:** Clear and specific, minor improvements possible
**3/5 - Adequate:** Functional but lacks precision or credit strategy
**2/5 - Weak:** Vague or ambiguous, missing credit optimization
**1/5 - Poor:** Unclear, contradictory, or missing entirely

**Lovable-Specific Calibration:**
- **5/5:** Complete PROMPT with phased implementation and visual matching
- **4/5:** Good PROMPT with minor credit optimization gaps
- **3/5:** Basic PROMPT without credit strategy
- **2/5:** Generic prompt not optimized for Lovable
- **1/5:** Missing critical Lovable requirements

**Credit Optimization Calibration:**
- **5/5:** Clear 3-phase approach with cost warnings
- **4/5:** Phases defined, some warnings missing
- **3/5:** Basic separation of features
- **2/5:** Minimal credit consideration
- **1/5:** No credit optimization

---

## 7. 🔄 REFINEMENT WORKFLOW

**Note:** This workflow is automated in Full Mode (`$refine`). Use manual refinement for targeted improvements.

### 7.1 Step 1: Analyze Evaluation
- Identify scores below 3/5 (critical issues)
- Check for missing credit optimization
- Verify visual reference extraction
- Note patterns in weaknesses
- Preserve elements scoring 4-5/5

### 7.2 Step 2: Apply Targeted Fixes

**For each low-scoring criterion:**

| Issue | Quick Fix | Example |
|-------|-----------|---------|
| Unclear task (1-2/5) | Add action verb + deliverable | "build..." → "Create PROMPT for building..." |
| Missing role (1-2/5) | Add expertise definition | Add: "As a [role]..." |
| No format (1-2/5) | Specify structure | Add: "Format: [structure]" |
| No credit strategy | Add phased approach | Add: "Phase 1 (Low): [features]" |
| No visual match | Extract from reference | Add: "Match [screenshot] with colors: [hex]" |
| Missing "PROMPT" note | Clarify output | Add: "Note: This is a PROMPT for..." |

### 7.3 Step 3: Enhancement Patterns

**Pattern: Missing Credit Optimization**
```
Add:
PHASE 1 - Core (Low Credit):
- Essential features only
- Basic structure
- Simple styling

PHASE 2 - Enhancement (Medium Credit):
- Nice-to-have features
- Interactions
- Forms

PHASE 3 - Premium (High Credit - Confirm):
⚠️ Complex features - implement now?
- Real-time
- Integrations
- Advanced animations
```

**Pattern: Missing Visual Reference Extraction**
```
Add:
VISUAL REFERENCE:
- Colors: #[hex1], #[hex2]
- Layout: [grid/flex structure]
- Components: [buttons, cards, forms]
- Spacing: [8px/16px system]
- Typography: [fonts and sizes]
```

### 7.4 Step 4: Validation
- ✅ Re-score against failed criteria
- ✅ Verify credit optimization included
- ✅ Check visual reference matched
- ✅ Ensure "PROMPT not implementation" clear
- ✅ Validate phased approach present

---

## 8. 📝 REFINEMENT EXAMPLES

### 8.1 Example: Adding Credit Optimization
**Before (2/5):** "Build a todo app with React and Supabase"
**After (5/5):** 
```
Create a PROMPT for developing a todo app:

💰 CREDIT OPTIMIZATION:
Phase 1 (Low): Basic CRUD, simple auth
Phase 2 (Medium): Categories, due dates
Phase 3 (High - Confirm): Real-time sync, notifications

Tech: React + Supabase + Tailwind
Start with: Dashboard component

Note: This is a PROMPT for developing an app, not the app itself
```

### 8.2 Example: Visual Reference Enhancement
**Before (2/5):** "Make this design [screenshot]"
**After (5/5):**
```
Create a PROMPT for building this interface:

VISUAL REFERENCE MATCHED:
- Colors: #6366F1 (primary), #F3F4F6 (background)
- Layout: 3-column grid with sidebar
- Components: Card-based with shadows
- Spacing: 16px grid system
- Typography: Inter headings, system body

💰 Phase 1: Static layout matching screenshot
Phase 2: Add interactions
Phase 3: Complex animations (confirm first)

Note: This is a PROMPT for implementation
```

### 8.3 Example: Lovable App Enhancement
**Before (2/5):** "Create project management tool"
**After (5/5):**
```
Create a PROMPT for developing a project management app:

💰 CREDIT OPTIMIZATION STRATEGY:

PHASE 1 - MVP Core (Low Credit):
- Project CRUD operations
- Basic task management
- Simple email/password auth
- Static Kanban board view

PHASE 2 - Enhanced Features (Medium Credit):
- Drag-and-drop functionality
- User assignments
- Due dates and priorities
- Activity feed

PHASE 3 - Premium Features (High Credit - Needs Confirmation):
⚠️ The following will significantly increase credit usage:
- Real-time collaboration
- File uploads to Supabase Storage
- Email notifications
- Advanced permissions
Ask: "Should I implement these now or defer?"

Tech Stack: React + Supabase + Tailwind + ShadCN
Database Schema:
- projects (id, name, owner_id)
- tasks (id, project_id, title, status, assignee_id)
- comments (id, task_id, user_id, content)

Start with: Project dashboard with task list

REUSE STRATEGY:
- Use ShadCN components for UI
- Leverage Supabase Auth templates
- Copy Kanban patterns from examples
- Use Tailwind utilities exclusively

Note: This is a PROMPT for developing an app, not the actual application
```

---

## 9. 🎯 COMMON REFINEMENT PATTERNS

### 9.1 The Credit-Unconscious Request
**Indicators:** Lovable request without phasing
**Fix:** Add 3-phase implementation with cost warnings
**Template:** 
```
Phase 1: [Essentials] - Low Credit
Phase 2: [Enhancements] - Medium Credit
Phase 3: [Complex] - High Credit (Confirm)
```

### 9.2 The Visual-Ignorant Request
**Indicators:** Screenshot provided but not referenced
**Fix:** Extract and specify visual details
**Template:**
```
Match provided [screenshot]:
- Colors: [extract hex codes]
- Layout: [identify structure]
- Components: [list elements]
```

### 9.3 The Implementation Confusion
**Indicators:** Seems to want actual build, not PROMPT
**Fix:** Clarify we create PROMPTS only
**Template:**
```
Create a PROMPT for [building/developing]:
[specifications]
Note: This creates a PROMPT, not the actual [app/website/prototype]
```

### 9.4 The Lovable Request
**Indicators:** Platform development without specifications
**Fix:** Add tech stack + features + phases + credit strategy
**Template:**
```
Create PROMPT for [type] with React + Supabase:
Phase 1: [MVP features] - Low Credit
Phase 2: [Enhancements] - Medium Credit
Phase 3: [Complex] - High Credit (Confirm)
Start with: [component]
```

---

## 10. ⚡ SPEED REFINEMENT CHECKLIST

For quick improvements, check these in order:

### Universal Checks
1. [ ] Is it clear this is a PROMPT? If not → Add "Create PROMPT for..."
2. [ ] Is the task crystal clear? If not → Add specifics
3. [ ] Is there a defined role? If not → Add expertise
4. [ ] Is output format specified? If not → Add structure
5. [ ] Is context provided? If not → Add background
6. [ ] Are there examples? If not → Add 1-2 samples

### Lovable-Specific Checks
7. [ ] Credit strategy defined? If not → Add 3 phases
8. [ ] High-cost features flagged? If not → Add warnings
9. [ ] Reuse strategy stated? If not → Add component reuse
10. [ ] Tech stack specified? If not → Add React + Supabase
11. [ ] Starting point clear? If not → Add initial component
12. [ ] Visual reference matched? If not → Extract details

### Final Verification
13. [ ] "This is a PROMPT" note included? If not → Add clarification
14. [ ] Phases clearly separated? If not → Structure Phase 1/2/3
15. [ ] User can make credit decisions? If not → Add confirmation points

**Stop when prompt reaches "good enough" - not every prompt needs all enhancements.**

---

*Remember: We evaluate and refine PROMPTS for building things, not actual implementations. Credit optimization and visual matching are essential for Lovable modes.*