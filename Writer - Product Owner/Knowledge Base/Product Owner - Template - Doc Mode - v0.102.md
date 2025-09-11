# Product Owner - Template - Doc Mode - v0.102

## 📋 Table of Contents

1. [📚 DOC MODE OVERVIEW](#-doc-mode-overview)
2. [📖 DOCUMENTATION TYPES](#-documentation-types)
3. [📦 PRODUCT DOCUMENTATION TEMPLATE](#-product-documentation-template)
4. [⚙️ FEATURE DOCUMENTATION TEMPLATE](#-feature-documentation-template)
5. [🧮 ALGORITHM DOCUMENTATION TEMPLATE](#-algorithm-documentation-template)
6. [🔌 API DOCUMENTATION TEMPLATE](#-api-documentation-template)
7. [📊 PERFORMANCE TRACKING TEMPLATE](#-performance-tracking-template)
8. [📘 USER GUIDE TEMPLATE](#-user-guide-template)
9. [🎯 DOCUMENTATION FORMATTING RULES](#-documentation-formatting-rules)
10. [💬 INTERACTIVE QUESTIONS](#-interactive-questions)

* * *

## 📚 DOC MODE OVERVIEW

### Command: `$doc`

- **Purpose:** Create product documentation, feature specs, and technical guides
- **Output:** Always as artifact
- **Thinking Rounds:** 6-10
- **Challenge Activation:** If complex or over-documented
- **Focus:** Clear structure, actionable information, business alignment

* * *

## 📖 DOCUMENTATION TYPES

### Quick Reference

| Type | Audience | Purpose | Structure |
|------|----------|---------|-----------|
| **Product Doc** | Product team | Feature specifications | About, Features, Overview, Patterns |
| **Feature Doc** | Dev team | Implementation details | About, Designs, Algorithm, Tracking |
| **Algorithm Doc** | Engineers | Technical logic | Weights, calculations, thresholds |
| **API Reference** | Developers | Endpoint documentation | Standard API format |
| **Performance Doc** | Analytics team | Metrics tracking | Targets, thresholds, actions |
| **User Guide** | End users | How to use | Progressive disclosure |

* * *

## 📦 PRODUCT DOCUMENTATION TEMPLATE

```markdown
# • [Feature Name]

**Parent:** [Parent Feature] | **Version:** 1.0 | **Reading Time:** [X] minutes
* * *
# ◘ About
* * *
[Brief description of the feature, its purpose, and value proposition. 2-3 paragraphs explaining what it does and why it matters to users and the business.]
* * *
## ◻︎ Designs & References
* * *
Here's where you'll find all the [feature]-related designs:
* * *
*   [Flow | [Context]](figma-link)
*   [Page | [Context]](figma-link)
*   [Component | [Context]](figma-link)
*   [Modal | [Context]](figma-link)
* * *
## ◻︎ Features
* * *
1. **[Feature Name]**
* * *
[Description of the feature and its business value]
* * *
2. **[Feature Name]**
* * *
[Description of the feature and its business value]
* * *
3. **[Feature Name]**
* * *
[Description of the feature and its business value]
* * *
## ◻︎ Overview
* * *
[High-level explanation of how the feature works, including key components and user journey]

| Component | Purpose | Business Value | User Value |
|-----------|---------|----------------|------------|
| **[Component]** | [What it does] | [Business impact] | [User benefit] |
| **[Component]** | [What it does] | [Business impact] | [User benefit] |

#

# ▪ [Section Name]
* * *
## ◻︎ Pattern
* * *
### ◊ **[Pattern Name]**
* * *
[Description of the pattern or behavior]
* * *
1. **[Step/Component]**

[Details about this step or component]

* * *
2. **[Step/Component]**

[Details about this step or component]

* * *
3. **Repeat** 🔄
* * *
### ◊ Algorithm
* * *
[Description of how the algorithm works]
* * *
**[Factor Name]** → Weight: [X]%
_[Description of what this factor measures]_
* * *
*   **[Sub-factor]** ([X]%)
    *   [Condition]: [weight multiplier]
    *   [Condition]: [weight multiplier]
* * *
*   **[Sub-factor]** ([X]%)
    *   [Condition]: [weight multiplier]
    *   [Condition]: [weight multiplier]
* * *
#

# ▪ Performance Tracking
* * *
We track metrics throughout the [feature] journey to [primary goal], [secondary goal], and [tertiary goal].
* * *
**Notice:** Check the documentation here for more details on: Private ([link])
* * *
## ◻︎ Target Metrics Framework
* * *
This framework helps us measure [what we're measuring] so we can [why we're measuring]. But metrics are only useful if we act on them - here's what we actually do.
* * *
### ◊ **[Metric Category]**
* * *
#### **– Targets**
* * *
*   [Metric name]
*   [Metric name]
*   [Metric name]
* * *
#### **– Thresholds & Actions**
* * *
1. **[Metric condition]** = [threshold]
* * *
**Situation:** [What this means]
**Action:** [What we do] → [Next step] → [Final step]
* * *
2. **[Metric condition]** = [threshold]
* * *
**Situation:** [What this means]
**Action:** [What we do] → [Next step] → [Final step]
* * *
```

* * *

## ⚙️ FEATURE DOCUMENTATION TEMPLATE

```markdown
# • [Feature Name]

**Parent:** [Parent] | **Version:** 1.0 | **Reading Time:** [X] minutes
* * *
# ◘ About
* * *
[Core description of what this feature does and why it exists]
* * *
## ◻︎ Key Benefits
* * *
1. **[Benefit Name]**
* * *
[How this benefit works and why it matters]
* * *
2. **[Benefit Name]**
* * *
[How this benefit works and why it matters]
* * *
## ◻︎ How It Works
* * *
### ◊ **[Component/Phase Name]**
* * *
#### **– Logic**
* * *
1. [First step in the process]
2. [Second step in the process]
3. [Result or outcome]
* * *
#### **– Algorithm**
* * *
**[Primary Factor]** → Weight: [X]%
_[What this measures and why]_
* * *
*   **[Component]** ([X]%)
    *   [Condition A]: [weight]
    *   [Condition B]: [weight]
    *   [Condition C]: [weight]
* * *
### ◊ **Edge Cases**
* * *
*   **[Scenario]:** [How it's handled]
*   **[Scenario]:** [How it's handled]
* * *
## ◻︎ Expansion States
* * *
### ◊ **[State Name]**
* * *
[Description of when this state occurs]
* * *
#### **– Logic**
* * *
1. [Trigger condition]
2. [System response]
3. [User sees]
4. [Next action]
* * *
> _"[User-facing message]" **[CTA Button]**_
* * *
```

* * *

## 🧮 ALGORITHM DOCUMENTATION TEMPLATE

```markdown
# • [Algorithm Name]

**Parent:** [Feature] | **Version:** 1.0 | **Reading Time:** [X] minutes
* * *
# ◘ About
* * *
[High-level description of what this algorithm does and its business purpose]
* * *
## ◻︎ Algorithm Overview
* * *
[Explanation of the core logic and approach]
* * *
### ◊ **Weighting System**
* * *
| Factor | Weight | Purpose | Impact |
|--------|--------|---------|--------|
| **[Factor]** | [X]% | [Why included] | [What it affects] |
| **[Factor]** | [X]% | [Why included] | [What it affects] |
| **[Factor]** | [X]% | [Why included] | [What it affects] |

#

# ▪ Algorithm Details
* * *
## ◻︎ Primary Algorithm
* * *
### ◊ **[Factor Category 1]** → Weight: [X]%
_[Description of what this category optimizes for]_
* * *
*   **[Sub-factor A]** ([X]%)
    *   [Specific condition]: [multiplier]x weight
    *   [Specific condition]: [multiplier]x weight
    *   [Specific condition]: [multiplier]x weight
* * *
*   **[Sub-factor B]** ([X]%)
    *   **[Tier/Level]:** [Description]: [multiplier]x weight
    *   **[Tier/Level]:** [Description]: [multiplier]x weight
    *   **[Tier/Level]:** [Description]: [multiplier]x weight
* * *
### ◊ **[Factor Category 2]** → Weight: [X]%
_[Description of what this category optimizes for]_
* * *
*   **[Metric Type]** ([X]%)
    *   [Range/Condition]: [multiplier]x weight
    *   [Range/Condition]: [multiplier]x weight
    *   [Range/Condition]: [multiplier]x weight
* * *
## ◻︎ Fallback Logic
* * *
When primary algorithm conditions aren't met:
* * *
1. **Tier 1 Fallback:** [What happens]
2. **Tier 2 Fallback:** [What happens]
3. **Default State:** [Final fallback]
* * *
```

* * *

## 🔌 API DOCUMENTATION TEMPLATE

```markdown
# • [API Name] Documentation

**Parent:** Platform APIs | **Version:** 1.0 | **Reading Time:** [X] minutes
* * *
# ◘ About
* * *
[API purpose and capabilities]
* * *
**Base URL:** `https://api.example.com/v1`
**Authentication:** [Type]
**Rate Limit:** [Requests/minute]
* * *
## ◻︎ Endpoints
* * *
### ◊ GET /[resource]
* * *
[Description of what this endpoint does]
* * *
**Parameters:**
*   `param1` (type, required/optional): [Description]
*   `param2` (type, required/optional): [Description]
* * *
**Response:**
```json
{
  "data": {
    "field1": "value",
    "field2": 123
  },
  "meta": {
    "total": 100
  }
}
```
* * *
### ◊ POST /[resource]
* * *
[Description of what this endpoint does]
* * *
**Request Body:**
```json
{
  "field1": "value",
  "field2": 123
}
```
* * *
**Response:**
```json
{
  "data": {
    "id": "123",
    "status": "created"
  }
}
```
* * *
## ◻︎ Error Handling
* * *
| Code | Status | Description | Action |
|------|--------|-------------|--------|
| `ERROR_CODE` | 400 | [Description] | [What to do] |
| `ERROR_CODE` | 401 | [Description] | [What to do] |
| `ERROR_CODE` | 404 | [Description] | [What to do] |
```

* * *

## 📊 PERFORMANCE TRACKING TEMPLATE

```markdown
# • Performance Tracking

**Parent:** [Feature] | **Version:** 1.0 | **Reading Time:** [X] minutes
* * *
# ◘ About
* * *
This document defines the performance tracking framework for [feature/product]. It establishes metrics to monitor, intervention thresholds, and response protocols for maintaining health and growth.
* * *
## ◻︎ Metric Definitions
* * *
Core metrics for tracking [what we're tracking].
* * *
| Metric | Description | Target | Current |
|--------|-------------|--------|---------|
| **[Metric]** | [What it measures] | [Goal] | [Actual] |
| **[Metric]** | [What it measures] | [Goal] | [Actual] |

#

# ▪ [Category] Performance
* * *
We track [description of what and why we track].
* * *
## ◻︎ Target Metrics Framework
* * *
### ◊ **[Metric Category]**
* * *
#### – Targets
* * *
*   [Specific metric]
*   [Specific metric]
*   [Specific metric]
* * *
#### – Thresholds & Actions
* * *
1. **[Metric name]** = below [X]%
* * *
**Situation:** [What this indicates]
**Action:** [Immediate action] → [Follow-up action] → [Long-term solution]
* * *
2. **[Metric name]** = above [X]
* * *
**Situation:** [What this indicates]
**Action:** [Immediate action] → [Follow-up action] → [Long-term solution]
* * *
### ◊ **[Metric Category]**
* * *
#### – Targets
* * *
*   [Metric] → [Metric] conversion rate
*   [Metric] → [Metric] rate
*   [Time-based metric]
* * *
#### – Thresholds & Actions
* * *
1. **[Conversion metric]** = below [X]%
* * *
**Situation:** [Problem description]
**Action:** [Solution steps with arrows between them]
* * *
```

* * *

## 📘 USER GUIDE TEMPLATE

```markdown
# • [Feature] User Guide

**Parent:** User Guides | **Version:** 1.0 | **Reading Time:** [X] minutes
* * *
# ◘ About
* * *
[User-friendly description of what this feature does and how it helps]
* * *
## ◻︎ Getting Started
* * *
### ◊ Prerequisites
* * *
*   [What user needs before starting]
*   [Access requirements]
*   [Technical requirements]
* * *
### ◊ Quick Start
* * *
1. **[Action]:** [How to do it]
2. **[Action]:** [How to do it]
3. **[Action]:** [How to do it]
* * *
✅ **Success:** [What user should see when done]
* * *
## ◻︎ Key Features
* * *
### ◊ [Feature Name]
* * *
[What it does and why user cares]
* * *
**How to use:**
1. [Step one]
2. [Step two]
3. [Expected result]
* * *
## ◻︎ Common Tasks
* * *
### ◊ [Task Name]
* * *
**Goal:** [What user accomplishes]
* * *
1. **[Step name]:** [Detailed instruction]
   * [Sub-detail if needed]
   * [Sub-detail if needed]
* * *
2. **[Step name]:** [Detailed instruction]
* * *
3. **Verify:** [How to confirm success]
* * *
## ◻︎ Troubleshooting
* * *
| Problem | Solution |
|---------|----------|
| [Issue description] | [Step-by-step fix] |
| [Issue description] | [Step-by-step fix] |
* * *
## ◻︎ Need Help?
* * *
* 📺 [Video Tutorial](link) - [Duration]
* 📚 [Full Documentation](link)
* 💬 [Support](link)
```

* * *

## 🎯 DOCUMENTATION FORMATTING RULES

### Essential Standards

- ✅ **Structure:** Parent | Version | Reading Time header
- ✅ **Symbols:** ◘ for main sections, ◻︎ for subsections, ◊ for details, ▪ for major divisions
- ✅ **Dividers:** Use `* * *` between sections, not `---`
- ✅ **Headers:** Single `#` for document title with bullet (•), `#` with ◘ for About
- ✅ **Algorithms:** Always show weights and percentages
- ✅ **Tables:** Use for comparisons, metrics, thresholds
- ✅ **Performance:** Include thresholds and actions
- ✅ **Cross-references:** Link to related docs with privacy notices

### Structure Guidelines

| Element | Usage | Example |
|---------|-------|---------|
| Title | `# • [Name]` | `# • Filters` |
| About | `# ◘ About` | Main description |
| Sections | `## ◻︎ [Name]` | `## ◻︎ Features` |
| Subsections | `### ◊ [Name]` | `### ◊ Algorithm` |
| Major breaks | `# ▪ [Name]` | `# ▪ Performance` |
| Dividers | `* * *` | Between all sections |
| Emphasis | Bold for terms | `**Weight:** 50%` |

### Algorithm Documentation

- **Weight format:** `**[Factor]** → Weight: [X]%`
- **Description:** Italics under weight `_[What this measures]_`
- **Sub-factors:** Bulleted with percentages in parentheses
- **Conditions:** Sub-bullets with multipliers

### Performance Metrics

- **Targets:** Bulleted list of metrics
- **Thresholds:** Numbered with condition and equals sign
- **Actions:** **Situation:** and **Action:** with arrow chains

* * *

## 💬 Interactive Questions

Questions to ask during documentation creation.

**Reference:** Full interactive flows → `Product Owner - Interactive Mode.md`

```markdown
1. "Documentation type? [product/feature/algorithm/api/performance/user guide]"
2. "Target audience? [product team/developers/end users/analytics team]"
3. "Scope? [single feature/full product/integration/system]"
4. [If algorithm] "Include weight breakdowns? [yes/no]"
5. [If performance] "Include thresholds and actions? [yes/no]"
6. [If user guide] "Technical level? [beginner/intermediate/advanced]"
```

* * *

*Documentation with consistent structure and business alignment. All outputs as artifacts. Use actual documentation patterns.*
