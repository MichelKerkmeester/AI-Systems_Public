# Prompt - Evaluation & Refinement v4.0.0

**Systematic quality assessment and improvement** for optimizing prompts through evaluation and targeted refinement.

## Table of Contents

1. [⚡ Quick Eval (10 Criteria)](#1--quick-eval-10-criteria)
2. [📊 Full Evaluation (35 Criteria)](#2--full-evaluation-35-criteria)
3. [🔄 Refinement Workflow](#3--refinement-workflow)
4. [📝 Refinement Patterns](#4--refinement-patterns)
5. [💡 Examples](#5--examples)
6. [🔑 Key Principles](#6--key-principles)

---

## 1. ⚡ Quick Eval (10 Criteria)

### Core Assessment (5 points each, 50 total)

1. **Clarity & Specificity** - Task clear and specific?
2. **Role & Expertise** - Appropriate expertise defined?
3. **Context Provided** - Background given?
4. **Target Audience** - Reader identified?
5. **Format & Structure** - Output specified?
6. **Success Criteria** - Quality measures defined?
7. **Scope & Boundaries** - Limits clear?
8. **Examples Provided** - Samples included?
9. **Methodology Clear** - Approach specified?
10. **Constraints Stated** - Limitations acknowledged?

### Quick Report Template
```markdown
QUICK EVALUATION: [X]/50 ([X]%)
Strengths: [Top 2]
Fix Now: [Weakest] → [Solution]
Thinking: [X] rounds
```

**Recommended Thinking:** 1-3 rounds for quick eval

---

## 2. 📊 Full Evaluation (35 Criteria)

### Evaluation Groups (175 points total)

#### Group 1: Task Definition (40 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Primary task clarity | 5 | Main objective clear? |
| Specific deliverables | 5 | Outputs defined? |
| Action verbs | 5 | Clear commands? |
| Scope definition | 5 | Boundaries set? |
| Success metrics | 5 | Measurable? |
| Quality standards | 5 | Excellence defined? |
| Completion criteria | 5 | Done clear? |
| Priority elements | 5 | Important highlighted? |

#### Group 2: Context (30 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Situation context | 5 | Current state? |
| Problem/need | 5 | Why matters? |
| Background info | 5 | History provided? |
| Assumptions | 5 | Givens explicit? |
| Dependencies | 5 | Related factors? |
| Timeline | 5 | Time specified? |

#### Group 3: Expertise (25 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Role definition | 5 | Expert persona? |
| Domain expertise | 5 | Skills specified? |
| Experience level | 5 | Seniority? |
| Credibility | 5 | Authority? |
| Perspective | 5 | Viewpoint? |

#### Group 4: Audience (25 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Target audience | 5 | Reader identified? |
| Audience level | 5 | Expertise assumed? |
| Audience needs | 5 | What they seek? |
| Purpose clear | 5 | Why creating? |
| Value proposition | 5 | Benefit defined? |

#### Group 5: Structure (20 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Format specified | 5 | Output structure? |
| Sections defined | 5 | Components? |
| Length/size | 5 | Scope quantified? |
| Style indicated | 5 | Tone specified? |

#### Group 6: Methodology (20 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Method specified | 5 | How to approach? |
| Process steps | 5 | Sequence clear? |
| Tools/resources | 5 | What to use? |
| Framework | 5 | Structure provided? |

#### Group 7: Constraints (15 pts)
| Criterion | Points | Check |
|-----------|--------|-------|
| Limitations | 5 | Boundaries? |
| Requirements | 5 | Must-haves? |
| Exclusions | 5 | What to avoid? |

### Scoring Guide

| Score | Level | Description |
|-------|-------|-------------|
| 5/5 | Excellent | Crystal clear, specific, actionable |
| 4/5 | Good | Clear, minor details missing |
| 3/5 | Adequate | Functional, needs clarity |
| 2/5 | Weak | Vague, lacks detail |
| 1/5 | Poor | Missing or unusable |

### Full Eval Report
```markdown
FULL EVALUATION: [X]/175 ([X]%)
Groups: Task[X/40] Context[X/30] Expert[X/25] Audience[X/25] Structure[X/20] Method[X/20] Constraints[X/15]
Priority Fixes: [Lowest scores with solutions]
Thinking: [X] rounds
```

**Recommended Thinking:** 4-6 rounds for full eval

---

## 3. 🔄 Refinement Workflow

### Step 1: Identify Issues
- Find scores < 3/5 (critical)
- Note pattern weaknesses
- Preserve 4-5/5 elements

### Step 2: Apply Fixes

| Score | Issue | Fix | Thinking |
|-------|-------|-----|----------|
| 1-2 | No role | Add "As a [expert]..." | 1 round |
| 1-2 | Vague task | Specify deliverables | 2 rounds |
| 1-2 | No format | Define structure | 1 round |
| 1-2 | No audience | Identify readers | 1 round |
| 1-2 | No context | Add background | 2 rounds |

### Step 3: Validate
✔ All scores ≥ 3/5?
✔ Critical elements present?
✔ Ambiguity eliminated?
✔ Actionable and clear?

**Recommended Thinking:** 3-5 rounds for refinement

---

## 4. 📝 Refinement Patterns

### 4.1 Role Addition
```markdown
Before: "Write about X"
After: "As a [specific expert] with [experience], write about X"
Thinking: 1 round
```

### 4.2 Context Injection
```markdown
Add: CONTEXT: [situation]
     BACKGROUND: [relevant info]
     OBJECTIVE: [why needed]
Thinking: 2 rounds
```

### 4.3 Structure Definition
```markdown
Add: FORMAT:
     - Section 1: [description] ([X] words)
     - Section 2: [description] ([X] words)
     Include: [specific elements]
Thinking: 1-2 rounds
```

### 4.4 Success Clarification
```markdown
Add: SUCCESS CRITERIA:
     - Achieves: [outcome]
     - Quality: [standard]
     - Impact: [result]
Thinking: 2 rounds
```

### 4.5 Audience Specification
```markdown
Add: TARGET AUDIENCE:
     - Primary: [users]
     - Knowledge: [level]
     - Needs: [what they seek]
Thinking: 1 round
```

### Speed Checklist

**Critical (Must Have):**
1. [ ] Clear task? → Add verb + object
2. [ ] Expert role? → Add "As a..."
3. [ ] Deliverable? → Specify output
4. [ ] Format? → Add structure

**Important (Should Have):**
5. [ ] Context? → Add background
6. [ ] Audience? → Define readers
7. [ ] Success? → Add metrics
8. [ ] Scope? → Add limits

---

## 5. 💡 Examples

### Example 1: Vague → Specific
**Before (15/175):** "Write about management"

**After (160/175):**
```markdown
As a senior project manager (10+ years software), write a 3000-word guide:
"Agile Project Management for Remote Teams"

AUDIENCE: PMs transitioning to remote
FORMAT: Intro (300) + 5 sections (500 each) + Action items (200)
INCLUDE: Tools comparison, case studies, templates
SUCCESS: Reader implements 3 strategies immediately

Thinking: 4 rounds
```

### Example 2: Missing Context → Complete
**Before (25/175):** "Analyze sales data"

**After (165/175):**
```markdown
As a data analyst specializing in e-commerce, analyze Q4 2024 sales:

CONTEXT: 50K SKUs, 15% YoY growth, missed targets by 8%
ANALYSIS: Revenue by category/region, CAC by channel, top/bottom products
DELIVERABLES: Executive summary, 15-page report, PowerPoint, recommendations
SUCCESS: Identify $2M+ Q1 opportunities

Thinking: 5 rounds
```

### Common Improvements

| Issue | Quick Fix | Example |
|-------|-----------|---------|
| No role | Add expertise | "As a [role]..." |
| Vague task | Specify action | "Analyze X to find Y" |
| No audience | Define reader | "For [audience] who..." |
| No format | Structure output | "Provide [format] with..." |
| No context | Add background | "Given [situation]..." |

---

## 6. 🔑 Key Principles

### Evaluation Focus
1. **Clarity** - Ambiguity kills quality
2. **Specificity** - Details drive results
3. **Context** - Background enables excellence
4. **Structure** - Format shapes output
5. **Measurability** - Success must be definable

### Refinement Priority
1. Fix critical gaps (1-2/5) first
2. Enhance weak areas (3/5) next
3. Polish good elements (4/5) last
4. Preserve excellent (5/5) always

### Thinking Allocation
- Quick eval: 1-3 rounds
- Full eval: 4-6 rounds
- Basic refinement: 3-4 rounds
- Deep refinement: 5-8 rounds

---

*For all framework definitions, mode specifications, and quick reference patterns, see Prompt - Core System & Quick Reference. For interactive refinement, see Prompt - Interactive Mode.*