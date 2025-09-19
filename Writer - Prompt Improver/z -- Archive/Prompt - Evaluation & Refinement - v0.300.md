# Evaluation & Refinement - v0.300

**Systematic quality assessment and improvement workflows** for optimizing prompts through structured evaluation and targeted refinement.

## Table of Contents

1. [⚡ QUICK EVAL MODE (10 CRITERIA)](#1--quick-eval-mode-10-criteria)
2. [📊 FULL EVALUATION MODE (35 CRITERIA)](#2--full-evaluation-mode-35-criteria)
3. [🎯 SCORING GUIDE](#3--scoring-guide)
4. [🔄 REFINEMENT WORKFLOW](#4--refinement-workflow)
5. [🔍 REFINEMENT EXAMPLES](#5--refinement-examples)
6. [📝 COMMON REFINEMENT PATTERNS](#6--common-refinement-patterns)
7. [⚡ SPEED REFINEMENT CHECKLIST](#7--speed-refinement-checklist)
8. [🎨 BUILDER MODE EVALUATION (SECONDARY)](#8--builder-mode-evaluation-secondary)

---

## 1. ⚡ QUICK EVAL MODE (10 CRITERIA)

For rapid assessments of standard prompts, evaluate these core criteria:

1. **Clarity & Specificity** - Is the task clear and specific?
2. **Role & Expertise** - Is appropriate expertise defined?
3. **Context Provided** - Sufficient background given?
4. **Target Audience** - Reader/user clearly identified?
5. **Format & Structure** - Output format specified?
6. **Success Criteria** - Quality measures defined?
7. **Scope & Boundaries** - Limits and extent clear?
8. **Examples Provided** - Samples or references included?
9. **Methodology Clear** - Approach specified (if needed)?
10. **Constraints Stated** - Limitations acknowledged?

**Quick Eval Template:**
```markdown
QUICK EVALUATION REPORT
Total Score: X/50 (X%)

Top Strengths:
1. [Strongest element - e.g., "Clear role definition"]
2. [Second strength - e.g., "Specific deliverables"]

Critical Improvements:
1. [Weakest area] → [Specific fix]
2. [Second weakness] → [Specific fix]
3. [Third weakness] → [Specific fix]
```

---

## 2. 📊 FULL EVALUATION MODE (35 CRITERIA)

### Group 1: Task Definition (40 points)
1. **Primary Task Clarity** (5) - Main objective crystal clear?
2. **Specific Deliverables** (5) - Exact outputs defined?
3. **Action Verbs Used** (5) - Clear commands (analyze, create, solve)?
4. **Scope Definition** (5) - Boundaries established?
5. **Success Metrics** (5) - Measurable outcomes?
6. **Quality Standards** (5) - Excellence defined?
7. **Completion Criteria** (5) - When done is clear?
8. **Priority Elements** (5) - Most important aspects highlighted?

### Group 2: Context & Background (30 points)
9. **Situation Context** (5) - Current state described?
10. **Problem/Need Clear** (5) - Why this matters?
11. **Background Info** (5) - Relevant history provided?
12. **Assumptions Stated** (5) - Givens made explicit?
13. **Dependencies Clear** (5) - Related factors identified?
14. **Timeline/Urgency** (5) - Time factors specified?

### Group 3: Expertise & Authority (25 points)
15. **Role Definition** (5) - Expert persona clear?
16. **Domain Expertise** (5) - Relevant skills specified?
17. **Experience Level** (5) - Seniority indicated?
18. **Credibility Markers** (5) - Authority established?
19. **Perspective Clear** (5) - Viewpoint defined?

### Group 4: Audience & Purpose (25 points)
20. **Target Audience** (5) - Reader/user identified?
21. **Audience Level** (5) - Expertise assumed?
22. **Audience Needs** (5) - What they seek?
23. **Purpose Clear** (5) - Why creating this?
24. **Value Proposition** (5) - Benefit defined?

### Group 5: Structure & Format (20 points)
25. **Format Specified** (5) - Output structure clear?
26. **Sections Defined** (5) - Components listed?
27. **Length/Size** (5) - Scope quantified?
28. **Style Indicated** (5) - Tone/voice specified?

### Group 6: Methodology & Approach (20 points)
29. **Method Specified** (5) - How to approach?
30. **Process Steps** (5) - Sequence clear?
31. **Tools/Resources** (5) - What to use?
32. **Analysis Framework** (5) - Structure provided?

### Group 7: Constraints & Requirements (15 points)
33. **Limitations Stated** (5) - Boundaries set?
34. **Requirements Listed** (5) - Must-haves clear?
35. **Exclusions Noted** (5) - What to avoid?

**Full Eval Template:**
```markdown
FULL EVALUATION REPORT
Total Score: X/175 (X%)

Group Scores:
- Task Definition: X/40
- Context & Background: X/30
- Expertise & Authority: X/25
- Audience & Purpose: X/25
- Structure & Format: X/20
- Methodology: X/20
- Constraints: X/15

Top Strengths:
1. [Highest scoring element]
2. [Second highest]
3. [Third highest]

Priority Improvements:
1. [Lowest scoring] → [Specific enhancement]
2. [Second lowest] → [Specific enhancement]
3. [Third lowest] → [Specific enhancement]
[Continue for significant gaps]
```

---

## 3. 🎯 SCORING GUIDE

### Standard Calibration

**5/5 - Excellent:**
- Crystal clear and specific
- Includes examples or templates
- Measurable and actionable
- No ambiguity possible

**4/5 - Good:**
- Clear and specific
- Minor details could be added
- Generally actionable
- Minimal ambiguity

**3/5 - Adequate:**
- Functional but could be clearer
- Some specificity missing
- Basically actionable
- Some interpretation needed

**2/5 - Weak:**
- Vague or unclear
- Lacks important details
- Difficult to action
- Significant ambiguity

**1/5 - Poor:**
- Missing or extremely vague
- No useful detail
- Not actionable
- Highly ambiguous

### Evaluation Priorities
1. **Task clarity** - Most critical
2. **Deliverables** - High importance
3. **Context** - Important
4. **Format** - Important
5. **Constraints** - Moderate importance

---

## 4. 🔄 REFINEMENT WORKFLOW

### Step 1: Analyze Evaluation Scores
- Identify all scores below 3/5 (critical issues)
- Note patterns in weaknesses
- Preserve elements scoring 4-5/5
- Prioritize improvements by impact

### Step 2: Apply Targeted Improvements

**For each low-scoring criterion:**

| Score | Issue | Fix Approach | Example |
|-------|-------|--------------|---------|
| 1-2/5 | No role | Add expert definition | "As a [specific expert]..." |
| 1-2/5 | Vague task | Add specifics | "Analyze..." → "Analyze Q4 sales data to identify..." |
| 1-2/5 | No format | Define structure | "Provide a report with [sections]" |
| 1-2/5 | No audience | Identify readers | "For [specific audience] who need..." |
| 1-2/5 | No context | Add background | "Given [situation], considering [factors]..." |

### Step 3: Enhancement Patterns

**Pattern: Missing Context**
```
Add:
CONTEXT:
- Current situation: [what's happening]
- Background: [relevant history]
- Why this matters: [importance]
```

**Pattern: Unclear Deliverables**
```
Add:
DELIVERABLES:
- Primary: [main output]
- Format: [structure]
- Length: [size/scope]
- Includes: [components]
```

**Pattern: No Success Criteria**
```
Add:
SUCCESS CRITERIA:
- Must achieve: [primary goals]
- Quality indicators: [what makes it good]
- Measurable outcomes: [metrics]
```

### Step 4: Validation Checklist
- ✅ All scores now 3/5 or higher?
- ✅ Critical elements present?
- ✅ Ambiguity eliminated?
- ✅ Actionable and clear?
- ✅ Examples included where helpful?

---

## 5. 🔍 REFINEMENT EXAMPLES

### Example 1: Vague to Specific
**Before (Score: 2/5):** 
"Write about project management"

**After (Score: 5/5):**
```
As a senior project manager with 10+ years experience in software development,
write a comprehensive guide titled "Agile Project Management for Remote Teams."

TARGET AUDIENCE: Project managers transitioning to remote work
LENGTH: 3000 words
FORMAT: 
- Introduction (300 words)
- 5 main sections (500 words each)
- Conclusion with action items (200 words)

MUST INCLUDE:
- Tool recommendations with pros/cons
- Real case studies from tech companies
- Common pitfalls and solutions
- Templates for sprint planning and retrospectives
- Metrics for measuring remote team performance

TONE: Professional yet conversational, with practical examples
SUCCESS: Reader can implement at least 3 strategies immediately
```

### Example 2: Missing Context to Complete
**Before (Score: 2/5):**
"Analyze our sales data"

**After (Score: 5/5):**
```
As a senior data analyst specializing in e-commerce analytics,
analyze Q4 2024 sales data to identify growth opportunities for Q1 2025.

CONTEXT:
- Company: Online retail, 50K SKUs across 12 categories
- Current situation: 15% YoY growth but missed Q4 targets by 8%
- Data available: 3 months of transactions, customer data, marketing spend
- Stakeholders: C-suite presentation on Monday

ANALYSIS REQUIREMENTS:
1. Revenue breakdown by category, region, and customer segment
2. Customer acquisition cost by channel
3. Product performance (top/bottom 10%)
4. Seasonal patterns and trends
5. Competitive benchmarking where possible

DELIVERABLES:
- Executive summary (1 page)
- Detailed analysis (10-15 pages)
- PowerPoint deck (15 slides)
- Raw data tables in appendix
- 5 actionable recommendations with projected ROI

SUCCESS METRICS:
- Identify opportunities worth $2M+ in Q1
- Find 3 quick wins implementable within 2 weeks
- Provide data supporting 2025 strategy decisions
```

### Example 3: Technical Enhancement
**Before (Score: 3/5):**
"Debug the application performance issues"

**After (Score: 5/5):**
```
As a senior performance engineer specializing in web applications,
diagnose and resolve critical performance degradation in our e-commerce checkout flow.

CURRENT SITUATION:
- Issue: Checkout time increased from 2s to 8-12s over past month
- Impact: 35% increase in cart abandonment, $500K weekly revenue loss
- Environment: React frontend, Node.js backend, PostgreSQL database
- Traffic: 100K daily users, peaks during flash sales

DIAGNOSTIC APPROACH:
1. Frontend Analysis
   - Bundle size and code splitting
   - React render performance
   - Third-party script impact
   - Memory leaks

2. Backend Investigation
   - API response times
   - Database query performance
   - Caching effectiveness
   - Service communication overhead

3. Infrastructure Review
   - Server resources and scaling
   - CDN configuration
   - Load balancer settings
   - Network latency

DELIVERABLES:
1. Root cause analysis document
2. Performance metrics dashboard
3. Prioritized fix list with effort estimates
4. Implementation plan with rollback procedures
5. Monitoring strategy to prevent recurrence

CONSTRAINTS:
- Budget: $50K for immediate fixes
- Timeline: Critical fixes within 48 hours
- Team: 3 engineers available
- Must maintain backward compatibility

SUCCESS CRITERIA:
- Checkout time < 3 seconds (P95)
- Cart abandonment back to baseline
- No degradation under 2x current load
- Automated alerts for future issues
```

---

## 6. 📝 COMMON REFINEMENT PATTERNS

### 6.1 The Role Addition
**Problem:** No expertise defined
**Solution:** Add specific expert role
```
"As a [specific role] with expertise in [domain],
[original prompt content]"
```

### 6.2 The Context Injection
**Problem:** Missing background
**Solution:** Add situation and why it matters
```
"CONTEXT: [Current situation]
BACKGROUND: [Relevant information]
OBJECTIVE: [Why this is needed]

[original prompt content]"
```

### 6.3 The Structure Definition
**Problem:** No format specified
**Solution:** Add clear output structure
```
"[original prompt content]

FORMAT:
- Section 1: [description] (X words)
- Section 2: [description] (X words)
- Section 3: [description] (X words)
Include: [specific elements]"
```

### 6.4 The Success Clarification
**Problem:** No quality criteria
**Solution:** Add measurable success metrics
```
"[original prompt content]

SUCCESS CRITERIA:
- Achieves: [specific outcome]
- Includes: [required elements]
- Quality: [measurable standard]
- Impact: [expected result]"
```

### 6.5 The Audience Specification
**Problem:** Unknown target reader
**Solution:** Define who will use this
```
"[original prompt content]

TARGET AUDIENCE:
- Primary: [main users]
- Knowledge level: [expertise]
- Needs: [what they're looking for]
- Use case: [how they'll use it]"
```

---

## 7. ⚡ SPEED REFINEMENT CHECKLIST

For quick improvements, check these in priority order:

### Critical Elements (Must Have)
1. [ ] Clear task/action? If not → Add specific verb and object
2. [ ] Expert role? If not → Add "As a [role]..."
3. [ ] Deliverable defined? If not → Specify exact output
4. [ ] Format clear? If not → Add structure/sections

### Important Elements (Should Have)
5. [ ] Context provided? If not → Add background
6. [ ] Audience identified? If not → Define readers
7. [ ] Success criteria? If not → Add quality measures
8. [ ] Scope bounded? If not → Add limits/size

### Nice to Have (When Time Allows)
9. [ ] Examples included? If not → Add 1-2 samples
10. [ ] Methodology specified? If not → Add approach
11. [ ] Constraints stated? If not → List limitations
12. [ ] Timeline indicated? If not → Add deadlines

**Stop when prompt reaches "good enough" - perfect is often unnecessary.**

---

## 8. 🎨 BUILDER MODE EVALUATION (SECONDARY)

*Note: Builder mode evaluation is secondary. Focus primarily on normal prompt evaluation.*

### When Evaluating Builder Prompts

Additional criteria to consider:
- Creative direction provided?
- Goals and outcomes clear?
- Phased approach included?
- Platform flexibility maintained?
- User experience defined?

### Builder-Specific Scoring
Apply standard evaluation first, then consider:
- Does it avoid prescriptive specifications?
- Does it focus on outcomes over implementation?
- Does it enable creative freedom?
- Is it platform-agnostic?

### Builder Refinement Patterns
When improving Builder prompts:
1. Replace specifications with goals
2. Add mood and feeling descriptions
3. Include phased implementation
4. Ensure universal compatibility
5. Focus on user outcomes

---

## 💡 Key Principles

### Evaluation Focus
1. **Clarity is king** - Ambiguity kills quality
2. **Specificity drives results** - Vague in, vague out
3. **Context enables excellence** - Background matters
4. **Structure guides success** - Format shapes output
5. **Expertise adds authority** - Roles matter

### Refinement Priorities
1. Fix critical gaps first (scores 1-2/5)
2. Enhance weak areas next (score 3/5)
3. Polish good elements last (score 4/5)
4. Preserve excellent components (score 5/5)
5. Validate improvements consistently

---

*This evaluation system focuses primarily on assessing and improving normal prompts, with secondary capabilities for Builder mode evaluation when needed.*