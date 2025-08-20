# Document Beautifier - Quick Reference Card v1.0.0

Daily companion for transforming unstructured text into professional documents.

## 📋 Table of Contents

1. [Quick Start](#1-quick-start)
2. [Mode Selection](#2-mode-selection)
3. [MCP Tool Selection](#3-mcp-tool-selection)
4. [Formatting Standards](#4-formatting-standards)
5. [Common Transformations](#5-common-transformations)
6. [Quality Checklist](#6-quality-checklist)

---

## 1. Quick Start

### Decision Tree
```
Document type clear?
├─ NO → $interactive (default) + Cascade MCP (3-5)
└─ YES → Specific mode + Sequential MCP (2-3)
   ├─ Technical → $technical
   ├─ Academic → $academic
   └─ Business → $business
```

### 30-Second Process
1. Receive document → MCP analyzes
2. Apply mode or default to $interactive
3. Structure with framework (SCAN/HIERARCHY/PREP)
4. Deliver markdown artifact with MCP notation

---

## 2. Mode Selection

| Mode | Command | Use When | MCP Type | Thoughts | Output |
|------|---------|----------|----------|----------|---------|
| **Interactive** | `$interactive` (DEFAULT) | Unclear/mixed | Cascade | 3-5 | User choice: Quick/Standard/Deep |
| **Technical** | `$technical` | Code, APIs, docs | Sequential | 2-3 | Decimal numbering, code blocks |
| **Academic** | `$academic` | Papers, research | Sequential | 2-3 | Abstract, citations, chapters |
| **Business** | `$business` | Reports, proposals | Sequential | 2-3 | Executive summary, action items |

### Interactive Sub-Levels
- **Quick**: 5 min read (3 thoughts)
- **Standard**: 15 min read (4 thoughts)  
- **Deep**: 30+ min read (5 thoughts)

---

## 3. MCP Tool Selection

**See Main Document Section 4 for complete MCP integration details**

### Quick Selection
```
Clear structure → Sequential (1-3 thoughts)
Multiple options → Cascade (3-5 thoughts)
```

### Thought Scaling
| Complexity | Sequential | Cascade |
|------------|------------|---------|
| Simple | 1 | 3 |
| Standard | 2 | 4 |
| Complex | 3 | 5 |

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

| Problem | Solution | MCP Approach |
|---------|----------|--------------|
| Wall of text (500+ words) | Add headers every 200-300 words, break paragraphs | Cascade 3-4 |
| Random points | Group by theme, create sections | Sequential 1-2 |
| No emphasis | Bold key terms, italicize definitions | Either MCP |
| Inconsistent lists | Apply parallel construction | Sequential |
| Mixed content | Hybrid structure with clear parts | Cascade 4-5 |

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
- [ ] MCP analysis complete
- [ ] Original content preserved
- [ ] Mode applied correctly
- [ ] TOC if >500 words
- [ ] Headers properly nested
- [ ] Lists consistent
- [ ] Emphasis appropriate
- [ ] Artifact structured
- [ ] MCP type noted

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
# Interactive (default)
[paste document]

# Specific modes
$technical [document]
$academic [document]
$business [document]
```

---

*Remember: MCP analyzes structure before formatting. Sequential for clarity, Cascade for exploration. Every document deserves intelligent analysis.*