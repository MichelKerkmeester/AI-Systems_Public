# Document Beautifier - Quick Reference Card v1.1.0

Daily companion for transforming unstructured text into professional documents.

## 📋 Table of Contents

1. [Quick Start](#1-quick-start)
2. [Mode Selection](#2-mode-selection)
3. [Native Thinking Selection](#3-native-thinking-selection)
4. [Formatting Standards](#4-formatting-standards)
5. [Common Transformations](#5-common-transformations)
6. [Quality Checklist](#6-quality-checklist)

---

## 1. Quick Start

### Decision Tree
```
Document received
├─ ASK: "How many thinking rounds?" (1-5)
└─ After user responds
   ├─ Document type clear?
   │  ├─ NO → $interactive (default) + Exploratory (3-5)
   │  └─ YES → Specific mode + Linear (2-3)
   │     ├─ Technical → $technical
   │     ├─ Academic → $academic
   │     └─ Business → $business
   └─ Apply format
```

### 30-Second Process
1. Receive document → Ask thinking rounds
2. User specifies rounds → Analyze with thinking
3. Apply mode or default to $interactive
4. Structure with framework (SCAN/HIERARCHY/PREP)
5. Deliver markdown artifact with notation

---

## 2. Mode Selection

| Mode | Command | Use When | Thinking Type | Default Rounds | Output |
|------|---------|----------|---------------|----------------|---------|
| **Interactive** | `$interactive` (DEFAULT) | Unclear/mixed | Exploratory | 3-5 | User choice: Quick/Standard/Deep |
| **Technical** | `$technical` | Code, APIs, docs | Linear | 2-3 | Decimal numbering, code blocks |
| **Academic** | `$academic` | Papers, research | Linear | 2-3 | Abstract, citations, chapters |
| **Business** | `$business` | Reports, proposals | Linear | 2-3 | Executive summary, action items |

### Interactive Sub-Levels
- **Quick**: 5 min read (user chooses rounds)
- **Standard**: 15 min read (user chooses rounds)  
- **Deep**: 30+ min read (user chooses rounds)

---

## 3. Native Thinking Selection

### ALWAYS ASK FIRST
```
"How many thinking rounds should I use? (1-5)
- 1-2: Simple structure
- 3-4: Standard complexity  
- 5: Complete restructuring
(I recommend X for your document)"
```

### Quick Selection Guide
```
Clear structure → Linear (1-3 rounds)
Multiple options → Exploratory (3-5 rounds)
```

### Round Scaling
| Complexity | Linear | Exploratory |
|------------|--------|-------------|
| Simple | 1 | 3 |
| Standard | 2 | 4 |
| Complex | 3 | 5 |

### Exception
Don't ask for rounds when:
- Still gathering requirements
- In discovery questions
- Not producing final output yet

---

## 4. Formatting Standards

### Heading Hierarchy
```markdown
# Title
## 1. Section
### 1.1 Subsection
#### 1.1.1 Detail
```

### Emphasis Hierarchy
1. **Bold** - Key terms, warnings
2. *Italic* - Definitions, first use
3. `Code` - Technical terms, commands
4. > Blockquote - Important notes
5. CAPS - Only WARNING/CRITICAL

### List Standards

**Unordered (concepts):**
- Main point
  - Supporting detail
    - Example

**Ordered (sequences):**
1. First step
   a. Sub-step
   b. Sub-step
2. Second step

### Callout Boxes
```markdown
> 💡 **TIP:** Helpful suggestion
> ⚠️ **WARNING:** Critical alert
> 📝 **NOTE:** Additional context
```

---

## 5. Common Transformations

### Quick Patterns

| Problem | Solution | Thinking Approach |
|---------|----------|-------------------|
| Wall of text (500+ words) | Add headers every 200-300 words, break paragraphs | 3-4 rounds exploratory |
| Random points | Group by theme, create sections | 1-2 rounds linear |
| No emphasis | Bold key terms, italicize definitions | Any rounds |
| Inconsistent lists | Apply parallel construction | 1-2 rounds linear |
| Mixed content | Hybrid structure with clear parts | 4-5 rounds exploratory |

### Structure Frameworks

**SCAN (Universal)**
- **S**ummary (10%)
- **C**ore content (70%)
- **A**dditional details (15%)
- **N**avigation/Next steps (5%)

**HIERARCHY (Complex)**
- Headers → Information → Examples → References → Actions

**PREP (Business/Academic)**
- **P**urpose/Problem
- **R**esearch/Results
- **E**vidence/Examples
- **P**lan/Proposal

---

## 6. Quality Checklist

### Pre-Delivery ✓
- [ ] Asked for thinking rounds (1-5)
- [ ] Thinking analysis complete
- [ ] Original content preserved
- [ ] Mode applied correctly
- [ ] TOC if >500 words
- [ ] Headers properly nested
- [ ] Lists consistent
- [ ] Emphasis appropriate
- [ ] Artifact structured
- [ ] Thinking rounds noted

### FORM Score Targets
| Mode | Min Score |
|------|-----------|
| Interactive Quick | 70% |
| Interactive Standard | 85% |
| Interactive Deep | 95% |
| Technical/Academic | 90% |
| Business | 85% |

### Red Flags → Quick Fixes
- No headers in 1000+ words → Add sections
- Paragraphs >150 words → Break at natural pauses
- No white space → Add line breaks
- Inconsistent format → Standardize
- No emphasis → Bold key terms

---

## 🎯 Quick Commands

```markdown
# Interactive (default) - Always asks rounds
[paste document]

# Specific modes - Still asks rounds
$technical [document]
$academic [document]
$business [document]
```

---

## 🤔 Thinking Rounds Reference

**Always Ask:** "How many rounds?" (1-5)

**Recommendations by Type:**
- Simple lists/notes: 1-2 rounds
- Standard documents: 2-3 rounds
- Mixed content: 3-4 rounds
- Complex restructure: 4-5 rounds

**Remember:** User always chooses final count!

---

*Remember: Always ask for thinking rounds before final output. Linear for clarity (1-3), Exploratory for options (3-5). Every document deserves user-controlled analysis depth.*