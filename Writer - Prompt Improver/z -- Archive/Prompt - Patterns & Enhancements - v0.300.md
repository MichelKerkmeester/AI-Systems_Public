# Patterns & Enhancement Techniques - v0.300

**Reusable templates and enhancement methods** for crafting effective prompts across common use cases, with primary focus on normal prompt improvement.

## Table of Contents

1. [🚀 QUICK TEMPLATES](#1--quick-templates)
2. [⚡ QUICK ENHANCEMENT CHECKLIST](#2--quick-enhancement-checklist)
3. [🔍 CORE PATTERNS](#3--core-patterns)
4. [💡 PATTERN COMBINATIONS](#4--pattern-combinations)
5. [🎯 SELECTION GUIDE](#5--selection-guide)
6. [📝 ENHANCEMENT TECHNIQUES](#6--enhancement-techniques)
7. [🌍 BUILDER PATTERNS (SECONDARY)](#7--builder-patterns-secondary)
8. [🔄 COMMON IMPROVEMENTS](#8--common-improvements)

---

## 1. 🚀 QUICK TEMPLATES

### Primary Templates (Normal Prompts)

**Analysis:** "As a [expert role], analyze [specific topic] focusing on [key aspects]. Provide [format] including [specific elements]."

**Creation:** "Create [specific deliverable] for [target audience] that [achieves purpose]. Include [requirements], formatted as [structure]."

**Solution:** "As a [problem-solving expert], solve [specific problem] given [constraints]. Think step-by-step, then provide [deliverable format]."

**Research:** "Research [topic] to identify [specific insights]. Use [methodology] and present findings as [format]."

**Explanation:** "Explain [complex topic] to [audience level]. Use [examples/analogies] and structure as [format]."

### Secondary Templates (Builder Modes)

**App PROMPT:** "Create prompt for [app type] that enables [user goal]. Include phased approach and creative direction."

**Website PROMPT:** "Create prompt for [site type] achieving [conversion goal]. Focus on user journey and impact."

**Prototype PROMPT:** "Create prompt exploring [concept] with emphasis on [learning goals]."

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

### Secondary Checks (When Applicable)
- [ ] **Methodology** - Approach specified?
- [ ] **Edge Cases** - Uncertainties handled?
- [ ] **Tone** - Voice and style defined?
- [ ] **Length** - Size/scope clarified?

---

## 3. 🔍 CORE PATTERNS

### 3.1 Expert Analysis Pattern
**Best for:** Data interpretation, research evaluation, strategic assessment, technical analysis

```
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
```

### 3.2 Content Creation Pattern
**Best for:** Articles, documentation, creative writing, marketing content

```
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
```

### 3.3 Problem-Solving Pattern
**Best for:** Troubleshooting, optimization, process improvement, debugging

```
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
```

### 3.4 Research & Investigation Pattern
**Best for:** Market research, literature reviews, competitive analysis, fact-finding

```
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
```

### 3.5 Teaching & Explanation Pattern
**Best for:** Tutorials, guides, educational content, complex explanations

```
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
```

---

## 4. 💡 PATTERN COMBINATIONS

### 4.1 Analysis + Recommendations
```
Part 1: Analyze [current state] using [methodology]
Part 2: Identify [key issues or opportunities]
Part 3: Provide [specific recommendations] with implementation plan
```

### 4.2 Research + Content Creation
```
Part 1: Research [topic] from [sources]
Part 2: Synthesize findings into [content type]
Part 3: Adapt for [specific audience]
```

### 4.3 Problem + Solution + Implementation
```
Part 1: Diagnose [problem] with root cause analysis
Part 2: Design [solution] with multiple options
Part 3: Create [implementation roadmap] with milestones
```

---

## 5. 🎯 SELECTION GUIDE

### By Task Type
| User Says | Best Pattern | Key Additions |
|-----------|-------------|---------------|
| "analyze..." | Expert Analysis | Role, methodology, metrics |
| "write..." | Content Creation | Audience, tone, structure |
| "solve..." | Problem-Solving | Constraints, options, plan |
| "research..." | Research & Investigation | Questions, sources, methodology |
| "explain..." | Teaching & Explanation | Audience level, examples, analogies |
| "create report..." | Analysis + Format | Structure, sections, visuals |
| "fix issue..." | Problem-Solving | Symptoms, root cause, solutions |

### By Complexity Level
- **Simple (1-2 requirements)** → Single pattern + basic enhancements
- **Medium (3-4 requirements)** → Pattern + full CRAFT framework
- **Complex (5+ requirements)** → Multiple patterns + detailed specifications

### By Industry/Domain
- **Business** → Focus on ROI, stakeholders, metrics
- **Technical** → Include specifications, constraints, edge cases
- **Creative** → Emphasize tone, style, inspiration
- **Academic** → Add methodology, citations, rigor
- **Marketing** → Include audience, conversion, messaging

---

## 6. 📝 ENHANCEMENT TECHNIQUES

### 6.1 Adding Specificity
**From vague to specific:**
```
Vague: "Write about marketing"
Better: "Write about digital marketing strategies"
Best: "Write a 2000-word guide on content marketing strategies for B2B SaaS companies, focusing on lead generation through educational content"
```

### 6.2 Defining Expertise
**Adding role and authority:**
```
Basic: "Explain machine learning"
Better: "As a data scientist, explain machine learning"
Best: "As a senior data scientist with 10 years experience in predictive analytics, explain machine learning concepts to business stakeholders"
```

### 6.3 Structuring Output
**Clear format specifications:**
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
**Measurable success criteria:**
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

## 7. 🌍 BUILDER PATTERNS (SECONDARY)

*Note: Builder patterns are for creating prompts for development platforms. They remain secondary to normal prompt patterns.*

### 7.1 Universal App Pattern
```
Create PROMPT for developing [app type]:

FUNCTIONAL REQUIREMENTS:
- Core purpose: [what users accomplish]
- Key features: [main functionality]
- Target users: [audience]

TECHNICAL APPROACH:
- Platform-agnostic design
- Phased implementation:
  * Phase 1: Core MVP
  * Phase 2: Enhanced features
  * Phase 3: Advanced capabilities

SUCCESS CRITERIA:
- Users can: [key actions]
- Performance: [metrics]
- Quality: [standards]

Note: This creates a development PROMPT, not the actual application
```

### 7.2 Universal Website Pattern
```
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
```

---

## 8. 🔄 COMMON IMPROVEMENTS

### Before/After Examples

#### Example 1: Report Request
**Before:** "Create a sales report"

**After:** 
"As a senior sales analyst, create a comprehensive Q4 2024 sales report for the executive team. Include:
- Revenue analysis by product line and region
- Year-over-year comparisons with trend analysis
- Top 10 customer performance metrics
- Competitive market share analysis
- Forecast for Q1 2025 with confidence intervals
- Executive summary with 5 key insights
Format: 10-page PDF with charts and data tables"

#### Example 2: Content Writing
**Before:** "Write about productivity"

**After:**
"As a productivity coach with expertise in time management, write a 1500-word article titled 'The 5-Hour Workday: Achieving More by Doing Less' for busy professionals. Include:
- Opening hook with surprising statistic
- 5 evidence-based productivity techniques
- Real-world case study
- Common pitfalls to avoid
- Action plan template
Tone: Authoritative yet approachable, with practical examples"

#### Example 3: Technical Documentation
**Before:** "Document the API"

**After:**
"As a technical writer specializing in developer documentation, create comprehensive API documentation for our RESTful payment processing API. Include:
- Quick start guide with curl examples
- Authentication methods and security
- Endpoint reference with request/response schemas
- Error codes and handling
- Rate limiting details
- SDKs and code examples in Python, JavaScript, and Java
- Postman collection
Format: Searchable HTML docs with interactive examples"

---

## 💡 Key Principles

### Focus Areas
1. **Normal prompts are primary** - 80% of patterns for standard tasks
2. **Clarity over complexity** - Simple, clear improvements
3. **Specificity drives quality** - Concrete details improve output
4. **Structure enables success** - Clear format specifications
5. **Context informs approach** - Background shapes response

### Enhancement Priorities
1. Add expert role and credibility
2. Specify exact deliverables
3. Define target audience
4. Include format and structure
5. Set success criteria
6. Provide examples when helpful
7. State constraints clearly

---

*These patterns focus primarily on enhancing normal prompts for everyday AI tasks, with Builder patterns available as a secondary capability when needed.*