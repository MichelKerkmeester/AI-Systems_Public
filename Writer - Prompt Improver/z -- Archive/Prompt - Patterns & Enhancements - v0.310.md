# Patterns & Enhancement Techniques - v0.310

**Reusable templates and enhancement methods** for crafting effective prompts across common use cases, with primary focus on normal prompt improvement. Now with native Claude thinking integration for user-controlled analysis depth.

## Table of Contents

1. [🚀 QUICK TEMPLATES](#1--quick-templates)
2. [⚡ QUICK ENHANCEMENT CHECKLIST](#2--quick-enhancement-checklist)
3. [📝 CORE PATTERNS](#3--core-patterns)
4. [💡 PATTERN COMBINATIONS](#4--pattern-combinations)
5. [🎯 SELECTION GUIDE](#5--selection-guide)
6. [🔍 ENHANCEMENT TECHNIQUES](#6--enhancement-techniques)
7. [🌐 BUILDER PATTERNS (SECONDARY)](#7--builder-patterns-secondary)
8. [📄 COMMON IMPROVEMENTS](#8--common-improvements)
9. [🧠 THINKING DEPTH GUIDE](#9--thinking-depth-guide)

---

## 1. 🚀 QUICK TEMPLATES

### Primary Templates (Normal Prompts)

**Analysis:** "As a [expert role], analyze [specific topic] focusing on [key aspects]. Provide [format] including [specific elements]."
*Thinking: 3-4 rounds typical*

**Creation:** "Create [specific deliverable] for [target audience] that [achieves purpose]. Include [requirements], formatted as [structure]."
*Thinking: 2-4 rounds typical*

**Solution:** "As a [problem-solving expert], solve [specific problem] given [constraints]. Think step-by-step, then provide [deliverable format]."
*Thinking: 4-6 rounds typical*

**Research:** "Research [topic] to identify [specific insights]. Use [methodology] and present findings as [format]."
*Thinking: 3-5 rounds typical*

**Explanation:** "Explain [complex topic] to [audience level]. Use [examples/analogies] and structure as [format]."
*Thinking: 2-3 rounds typical*

### Secondary Templates (Builder Modes)

**App PROMPT:** "Create prompt for [app type] that enables [user goal]. Include phased approach and creative direction."
*Thinking: 4-6 rounds typical*

**Website PROMPT:** "Create prompt for [site type] achieving [conversion goal]. Focus on user journey and impact."
*Thinking: 3-5 rounds typical*

**Prototype PROMPT:** "Create prompt exploring [concept] with emphasis on [learning goals]."
*Thinking: 2-4 rounds typical*

---

## 2. ⚡ QUICK ENHANCEMENT CHECKLIST

### Primary Checks (All Prompts)
- [ ] **Role/Expertise** - Expert role defined?
- [ ] **Specific Task** - Clear action verb and deliverable?
- [ ] **Context** - Background information provided?
- [ ] **Audience** - Target reader identified?
- [ ] **Format** - Structure and style specified?
- [ ] **Success Criteria** - Quality measures defined?
- [ ] **Examples** - 1-3 samples included?
- [ ] **Constraints** - Limitations stated?
- [ ] **Thinking Depth** - User preference asked?

### Secondary Checks (When Applicable)
- [ ] **Methodology** - Approach specified?
- [ ] **Edge Cases** - Uncertainties handled?
- [ ] **Tone** - Voice and style defined?
- [ ] **Length** - Size/scope clarified?

**Thinking Guide:**
- Simple checks: 1-2 rounds per item
- Complex checks: 2-3 rounds per item

---

## 3. 📝 CORE PATTERNS

### 3.1 Expert Analysis Pattern
**Best for:** Data interpretation, research evaluation, strategic assessment, technical analysis
**Recommended Thinking:** 4-6 rounds

```
[Ask user: "How many thinking rounds would you like? (1-10, or 'auto')"]

As a [specific expert role] with [years] experience in [domain],
analyze [specific subject/data] to [achieve goal].

CONTEXT:
[Relevant background information]
[Current situation or problem]
[Why this analysis is needed]

ANALYSIS REQUIREMENTS:
1. [Specific aspect to examine]
2. [Key metrics or factors to consider]
3. [Comparisons or benchmarks needed]
4. [Trends or patterns to identify]

DELIVERABLES:
- [Format: report/presentation/memo]
- [Length: word count or page limit]
- [Sections: executive summary, findings, recommendations]
- [Visuals: charts/graphs/tables needed]

SUCCESS CRITERIA:
- [What makes this analysis valuable]
- [Key insights that must be uncovered]
- [Decisions this will inform]

If data is incomplete or assumptions are needed, clearly state them.

Thinking rounds used: [X]
```

### 3.2 Content Creation Pattern
**Best for:** Articles, documentation, creative writing, marketing content
**Recommended Thinking:** 3-5 rounds

```
[Ask user: "How many thinking rounds would you like? (1-10, or 'auto')"]

As a [content expert role], create [specific type of content]
for [target audience] that [achieves specific purpose].

AUDIENCE PROFILE:
- Knowledge level: [beginner/intermediate/expert]
- Interests: [relevant topics]
- Needs: [what they're looking for]

CONTENT REQUIREMENTS:
- Topic: [specific subject matter]
- Length: [word count or time to read]
- Tone: [professional/casual/academic/conversational]
- Style: [descriptive/persuasive/informative/entertaining]

MUST INCLUDE:
□ [Essential element 1]
□ [Essential element 2]
□ [Essential element 3]

STRUCTURE:
1. [Opening: hook/introduction approach]
2. [Body: main sections or points]
3. [Conclusion: call-to-action or summary]

EXAMPLES TO MATCH:
[Provide 1-2 examples of desired style or quality]

AVOID:
- [Common mistakes or unwanted elements]
- [Topics or approaches to exclude]

Thinking rounds used: [X]
```

### 3.3 Problem-Solving Pattern
**Best for:** Troubleshooting, optimization, process improvement, debugging
**Recommended Thinking:** 5-7 rounds

```
[Ask user: "How many thinking rounds would you like? (1-10, or 'auto')"]

As a [problem-solving expert] specializing in [domain],
diagnose and solve [specific problem].

CURRENT SITUATION:
- Symptoms: [what's going wrong]
- Impact: [consequences of the problem]
- Timeline: [when it started, urgency]
- Previous attempts: [what's been tried]

CONSTRAINTS:
- Resources: [available tools/budget/time]
- Limitations: [technical/organizational/legal]
- Dependencies: [related systems or processes]

SOLUTION REQUIREMENTS:
1. Root cause analysis
2. Multiple solution options (minimum 3)
3. Pros/cons for each option
4. Recommended approach with justification
5. Implementation plan
6. Risk mitigation strategies

FORMAT:
- Structured problem-solving framework
- Clear action steps
- Decision matrix if applicable
- Timeline for implementation

SUCCESS METRICS:
- [How to measure if problem is solved]
- [Expected improvements]
- [Key performance indicators]

Thinking rounds used: [X]
```

### 3.4 Research & Investigation Pattern
**Best for:** Market research, literature reviews, competitive analysis, fact-finding
**Recommended Thinking:** 4-6 rounds

```
[Ask user: "How many thinking rounds would you like? (1-10, or 'auto')"]

As a [research specialist] in [field],
conduct comprehensive research on [topic] to [achieve objective].

RESEARCH SCOPE:
- Primary focus: [main area of investigation]
- Secondary areas: [related topics to explore]
- Time period: [historical range or current]
- Geographic scope: [if applicable]

RESEARCH QUESTIONS:
1. [Primary question to answer]
2. [Secondary question]
3. [Supporting questions]

METHODOLOGY:
- Approach: [qualitative/quantitative/mixed]
- Sources: [types of sources to use]
- Analysis method: [how to process findings]

DELIVERABLES:
- Format: [research report/brief/presentation]
- Length: [page count or word limit]
- Sections:
  * Executive summary
  * Methodology
  * Key findings
  * Analysis
  * Recommendations
  * References

QUALITY STANDARDS:
- Evidence-based conclusions
- Multiple source verification
- Clear citations
- Objective analysis
- Actionable insights

Thinking rounds used: [X]
```

### 3.5 Teaching & Explanation Pattern
**Best for:** Tutorials, guides, educational content, complex explanations
**Recommended Thinking:** 2-4 rounds

```
[Ask user: "How many thinking rounds would you like? (1-10, or 'auto')"]

As an expert educator in [subject],
explain [complex topic] to [audience level].

LEARNING OBJECTIVES:
By the end, learners should:
1. Understand [core concept 1]
2. Be able to [practical skill]
3. Know how to [apply knowledge]

AUDIENCE BACKGROUND:
- Current knowledge: [what they already know]
- Common misconceptions: [what to clarify]
- Learning style: [visual/textual/examples]

EXPLANATION APPROACH:
- Start with: [familiar concept or analogy]
- Build up to: [complex understanding]
- Use examples: [concrete, relatable examples]
- Include: [diagrams/illustrations if needed]

STRUCTURE:
1. Introduction: Why this matters
2. Foundation: Basic concepts
3. Core content: Main explanation
4. Examples: Practical applications
5. Summary: Key takeaways
6. Practice: Exercises or questions

CLARITY TECHNIQUES:
- Define technical terms when first used
- Use analogies to familiar concepts
- Provide step-by-step breakdowns
- Include common questions and answers

Thinking rounds used: [X]
```

---

## 4. 💡 PATTERN COMBINATIONS

### 4.1 Analysis + Recommendations
**Thinking:** 5-7 rounds total
```
Part 1: Analyze [current state] using [methodology] (3-4 rounds)
Part 2: Identify [key issues or opportunities] (1 round)
Part 3: Provide [specific recommendations] with implementation plan (1-2 rounds)
```

### 4.2 Research + Content Creation
**Thinking:** 6-8 rounds total
```
Part 1: Research [topic] from [sources] (3-4 rounds)
Part 2: Synthesize findings into [content type] (2-3 rounds)
Part 3: Adapt for [specific audience] (1 round)
```

### 4.3 Problem + Solution + Implementation
**Thinking:** 7-9 rounds total
```
Part 1: Diagnose [problem] with root cause analysis (3 rounds)
Part 2: Design [solution] with multiple options (2-3 rounds)
Part 3: Create [implementation roadmap] with milestones (2-3 rounds)
```

---

## 5. 🎯 SELECTION GUIDE

### By Task Type
| User Says | Best Pattern | Key Additions | Thinking |
|-----------|-------------|---------------|----------|
| "analyze..." | Expert Analysis | Role, methodology, metrics | 4-6 rounds |
| "write..." | Content Creation | Audience, tone, structure | 3-5 rounds |
| "solve..." | Problem-Solving | Constraints, options, plan | 5-7 rounds |
| "research..." | Research & Investigation | Questions, sources, methodology | 4-6 rounds |
| "explain..." | Teaching & Explanation | Audience level, examples, analogies | 2-4 rounds |
| "create report..." | Analysis + Format | Structure, sections, visuals | 5-7 rounds |
| "fix issue..." | Problem-Solving | Symptoms, root cause, solutions | 5-7 rounds |

### By Complexity Level
- **Simple (1-2 requirements)** → Single pattern + basic enhancements (1-3 rounds)
- **Medium (3-4 requirements)** → Pattern + full CRAFT framework (4-5 rounds)
- **Complex (5+ requirements)** → Multiple patterns + detailed specifications (6-10 rounds)

### By Industry/Domain
- **Business** → Focus on ROI, stakeholders, metrics (4-6 rounds)
- **Technical** → Include specifications, constraints, edge cases (5-7 rounds)
- **Creative** → Emphasize tone, style, inspiration (3-5 rounds)
- **Academic** → Add methodology, citations, rigor (5-7 rounds)
- **Marketing** → Include audience, conversion, messaging (4-5 rounds)

---

## 6. 🔍 ENHANCEMENT TECHNIQUES

### 6.1 Adding Specificity
**From vague to specific (1-2 thinking rounds):**
```
Vague: "Write about marketing"
Better: "Write about digital marketing strategies"
Best: "Write a 2000-word guide on content marketing strategies for B2B SaaS companies, focusing on lead generation through educational content"
```

### 6.2 Defining Expertise
**Adding role and authority (1 thinking round):**
```
Basic: "Explain machine learning"
Better: "As a data scientist, explain machine learning"
Best: "As a senior data scientist with 10 years experience in predictive analytics, explain machine learning concepts to business stakeholders"
```

### 6.3 Structuring Output
**Clear format specifications (2-3 thinking rounds):**
```
Unstructured: "Give me information about project management"
Structured: "Provide a structured guide with:
- Executive summary (200 words)
- 5 key principles (100 words each)
- 3 case studies (300 words each)
- Action plan template
- Recommended resources list"
```

### 6.4 Setting Quality Standards
**Measurable success criteria (2-3 thinking rounds):**
```
No standards: "Write a good article"
With standards: "Write an article that:
- Engages readers within first 50 words
- Provides 5 actionable takeaways
- Includes data from 3+ credible sources
- Maintains 8th-grade reading level
- Achieves SEO optimization for [keyword]"
```

---

## 7. 🌐 BUILDER PATTERNS (SECONDARY)

*Note: Builder patterns are for creating prompts for development platforms. They remain secondary to normal prompt patterns.*

### 7.1 Universal App Pattern
**Thinking:** 4-6 rounds typical
```
[Ask user: "How many thinking rounds for this app prompt?"]

Create PROMPT for developing [app type]:

FUNCTIONAL REQUIREMENTS:
- Core purpose: [what users accomplish]
- Key features: [main functionality]
- Target users: [audience]

TECHNICAL APPROACH:
- Platform-agnostic design
- Phased implementation:
  * Phase 1: Core MVP (1-2 thinking rounds)
  * Phase 2: Enhanced features (2-3 thinking rounds)
  * Phase 3: Advanced capabilities (3-4 thinking rounds)

SUCCESS CRITERIA:
- Users can: [key actions]
- Performance: [metrics]
- Quality: [standards]

Note: This creates a development PROMPT, not the actual application
Thinking rounds used: [X]
```

### 7.2 Universal Website Pattern
**Thinking:** 3-5 rounds typical
```
[Ask user: "How many thinking rounds for this website prompt?"]

Create PROMPT for [website type]:

STRATEGIC GOALS:
- Primary objective: [conversion/information/engagement]
- Target audience: [visitor profile]
- Key message: [value proposition]

CONTENT STRUCTURE:
- Main sections: [pages/areas]
- User journey: [flow]
- Calls to action: [desired actions]

CREATIVE DIRECTION:
- Brand personality: [adjectives]
- User experience: [feelings/emotions]
- Success metrics: [measurements]

Note: This creates a website PROMPT, not the actual site
Thinking rounds used: [X]
```

### 7.3 Universal Prototype Pattern
**Thinking:** 2-4 rounds typical
```
[Ask user: "How many thinking rounds for this prototype prompt?"]

Create PROMPT for exploring [concept]:

EXPLORATION GOALS:
- What to investigate: [concepts to test]
- Target users: [who will use this]
- Success metrics: [what to learn]

CREATIVE FREEDOM:
- Mood and tone: [adjectives]
- User feelings: [emotional targets]
- Areas to explore: [design directions]

PHASED APPROACH:
- Phase 1: Basic concepts (1-2 thinking rounds)
- Phase 2: Refined ideas (2-3 thinking rounds)
- Phase 3: Polish if needed (3-4 thinking rounds)

Note: This creates an exploration PROMPT, not the actual prototype
Thinking rounds used: [X]
```

---

## 8. 📄 COMMON IMPROVEMENTS

### Before/After Examples

#### Example 1: Report Request
**Before:** "Create a sales report"
**Thinking:** 5 rounds requested

**After:** 
```
As a senior sales analyst, create a comprehensive Q4 2024 sales report for the executive team. Include:
- Revenue analysis by product line and region
- Year-over-year comparisons with trend analysis
- Top 10 customer performance metrics
- Competitive market share analysis
- Forecast for Q1 2025 with confidence intervals
- Executive summary with 5 key insights
Format: 10-page PDF with charts and data tables

Thinking rounds used: 5
```

#### Example 2: Content Writing
**Before:** "Write about productivity"
**Thinking:** Auto (3 rounds)

**After:**
```
As a productivity coach with expertise in time management, write a 1500-word article titled 'The 5-Hour Workday: Achieving More by Doing Less' for busy professionals. Include:
- Opening hook with surprising statistic
- 5 evidence-based productivity techniques
- Real-world case study
- Common pitfalls to avoid
- Action plan template
Tone: Authoritative yet approachable, with practical examples

Thinking rounds used: 3 (auto)
```

#### Example 3: Technical Documentation
**Before:** "Document the API"
**Thinking:** 6 rounds requested

**After:**
```
As a technical writer specializing in developer documentation, create comprehensive API documentation for our RESTful payment processing API. Include:
- Quick start guide with curl examples
- Authentication methods and security
- Endpoint reference with request/response schemas
- Error codes and handling
- Rate limiting details
- SDKs and code examples in Python, JavaScript, and Java
- Postman collection
Format: Searchable HTML docs with interactive examples

Thinking rounds used: 6
```

#### Example 4: Data Analysis
**Before:** "Look at customer data"
**Thinking:** Auto (5 rounds)

**After:**
```
As a customer analytics specialist, analyze Q4 2024 customer behavior data to optimize retention strategies. Focus on:
- Segmentation by purchase frequency and value
- Churn prediction indicators
- Customer lifetime value calculations
- Engagement patterns across channels
- Recommendations for personalization

Deliverables:
- Dashboard with key metrics
- Detailed report (15 pages)
- Action plan with priorities
- ROI projections for recommendations

Success: Identify opportunities to reduce churn by 20%

Thinking rounds used: 5 (auto)
```

#### Example 5: Educational Content
**Before:** "Explain blockchain"
**Thinking:** 3 rounds requested

**After:**
```
As a technology educator, explain blockchain technology to business executives with no technical background.

Structure:
1. Real-world analogy (shared ledger concept)
2. Core components in plain language
3. Business applications with examples
4. Benefits and limitations
5. Implementation considerations

Use banking and supply chain examples throughout.
Avoid technical jargon, focus on business value.
Length: 2000 words with diagrams

Thinking rounds used: 3
```

---

## 9. 🧠 THINKING DEPTH GUIDE

### How to Choose Thinking Rounds

**By Task Complexity:**
| Complexity | Characteristics | Recommended Rounds | Auto Default |
|------------|----------------|-------------------|--------------|
| Very Simple | Clear task, single requirement | 1-2 rounds | 1 |
| Simple | Basic task, few requirements | 2-3 rounds | 2 |
| Standard | Multiple requirements, some context | 4-5 rounds | 4 |
| Complex | Many requirements, detailed context | 6-7 rounds | 6 |
| Very Complex | Multiple constraints, edge cases | 8-10 rounds | 8 |

**By Pattern Type:**
| Pattern | Minimum | Standard | Maximum | Auto |
|---------|---------|----------|---------|-----|
| Teaching | 2 rounds | 3 rounds | 4 rounds | 3 |
| Content | 3 rounds | 4 rounds | 5 rounds | 4 |
| Analysis | 4 rounds | 5 rounds | 6 rounds | 5 |
| Problem-Solving | 5 rounds | 6 rounds | 7 rounds | 6 |
| Research | 4 rounds | 5 rounds | 6 rounds | 5 |
| Builder (App) | 4 rounds | 5 rounds | 6 rounds | 5 |
| Builder (Website) | 3 rounds | 4 rounds | 5 rounds | 4 |
| Builder (Prototype) | 2 rounds | 3 rounds | 4 rounds | 3 |

**User Interaction Protocol:**
1. Always ask: "How many thinking rounds would you like? (1-10, or 'auto')"
2. If 'auto': Use complexity assessment to recommend
3. Document rounds used in final output
4. Exception: During discovery phases, ask before final output only

### Impact of Thinking Depth

**1-2 Rounds (Surface):**
- Basic role addition
- Simple clarifications
- Format specification
- Quick fixes

**3-4 Rounds (Standard):**
- Full CRAFT framework
- Context development
- Audience analysis
- Success criteria

**5-6 Rounds (Detailed):**
- Multiple perspectives
- Edge case handling
- Comprehensive structure
- Quality metrics

**7-8 Rounds (Deep):**
- Complex constraints
- Multiple stakeholders
- Risk analysis
- Alternative approaches

**9-10 Rounds (Maximum):**
- Full framework application
- Exhaustive specifications
- Complete methodology
- Contingency planning

---

## 💡 Key Principles

### Focus Areas
1. **Normal prompts are primary** - 80% of patterns for standard tasks
2. **Clarity over complexity** - Simple, clear improvements
3. **Specificity drives quality** - Concrete details improve output
4. **Structure enables success** - Clear format specifications
5. **Context informs approach** - Background shapes response
6. **User controls thinking** - They decide analysis depth

### Enhancement Priorities
1. Add expert role and credibility (1 round)
2. Specify exact deliverables (1-2 rounds)
3. Define target audience (1 round)
4. Include format and structure (2 rounds)
5. Set success criteria (2 rounds)
6. Provide examples when helpful (1 round)
7. State constraints clearly (1 round)
8. Ask for thinking preference (always)

### Quality Indicators
- **Clear objective** ✓
- **Defined expertise** ✓
- **Target audience** ✓
- **Specific format** ✓
- **Success metrics** ✓
- **Thinking depth** ✓
- **User control** ✓

---

*These patterns focus primarily on enhancing normal prompts for everyday AI tasks, with Builder patterns available as a secondary capability when needed. Users control thinking depth for optimal results through native Claude thinking.*