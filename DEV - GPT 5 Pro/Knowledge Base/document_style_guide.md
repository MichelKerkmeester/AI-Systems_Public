# Document Style Guide

Define the canonical documentation format for all documents. Follow these conventions to ensure documentation remains accessible, maintainable, and professional. All documents must start with a short Description section and should not include metadata blocks like Category, Tags, or Priority.

.

## 1. 📄 Document Structure

### 1.1 Standard Layout
```markdown
# Title - Descriptive Subtitle

Brief introduction paragraph explaining the document's purpose and value.

## 📋 Table of Contents

- [1. 📄 Description](#description)
- [2. 🧭 Second Section](#second-section)
- [3. 🛠️ Third Section](#third-section)

.

## 1. 📄 Description

Content here...

.

## 2. 🧭 Second Section

Content here...
```

### 1.2 Section Separators
- Use a single period (`.`) on its own line between major sections
- Creates visual breathing room without cluttering
- Place before and after section breaks

.

## 2. 📝 Headers & Hierarchy

| Level | Format | Example | Usage |
|-------|--------|---------|-------|
| H1 | Title - Subtitle | `# Animation Libraries - Decision Framework` | Document title only |
| H2 | Number + Emoji + Title | `## 1. 📄 Description` | Major sections |
| H3 | Decimal + Title | `### 2.1 Primary Order` | Subsections |
| H4-H6 | Avoid | - | Reserve for exceptional cases |

.

## 3. 🎨 Visual Elements

### 4.1 Emoji Usage
Stand3rd emoji assignments for consistency:

| Emoji | Purpose | Common Usage |
|-------|---------|--------------|
| 🎯 | Objective/Goal | Section headers |
| 📋 | Table of Contents | TOC header |
| 🧭 | Navigation/Priority | Framework sections |
| 🛠️ | Tools/Implementation | Technical sections |
| ✅ | Best Practices/Done | Validation sections |
| ❌ | Anti-patterns/Wrong | Bad examples |
| 🔒 | Security/Quality | Gate sections |
| 📊 | Data/Performance | Metrics sections |
| 🚀 | Quick Start/Migration | Getting started |
| 💬 | Comments/Discussion | Commentary sections |
| 🧾 | Templates/Reference | Documentation sections |
| 🧩 | Components/Parts | Architecture sections |
| ⚙️ | Configuration/Settings | Setup sections |
| 🔍 | Search/Analysis | Investigation sections |

### 3.2 Visual Markers
```markdown
✅ Good practice
❌ Bad practice
□ Checkbox item
```

.

## 4. 💻 Code Formatting

### 4.1 Code Blocks
```javascript
// Always specify language for syntax highlighting
function example_function() {
  // Use consistent indentation (2 spaces)
  return true;
}
```

### 4.2 Good vs Bad Examples
```javascript
// ✅ CORRECT
const user_name = 'John';

// ❌ WRONG
const userName = 'John';
```

### 4.3 Inline Code
- Use backticks for `inline_code`
- Include file paths: `src/component/file.js`
- Mark commands: `npm run build`

### 4.4 Section Headers in Code
```javascript
// ───────────────────────────────────────────────────────────────
// COMPONENT: NAME
// ───────────────────────────────────────────────────────────────
```

.

## 5. 📊 Tables & Lists

### 5.1 Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1 | Data 2 | Data 3 |
```
- Always include header row
- Use alignment pipes consistently
- Keep columns readable width

### 5.2 Lists
- **Bullet points**: For unordered information
- **Numbered lists**: For sequential steps
- **Nested lists**: Indent with 2 spaces
  - Like this nested item
  - And this one

### 5.3 Quick Decision Trees
```
Need Animation?
├─> Can Webflow handle it? -> Use Webflow
├─> Simple animation? -> Use Motion.dev
└─> Complex (3D/morphing)? -> Use GSAP
```

.

## 6. ✍️ Writing Style

### 6.1 Core Principles
- **Concise**: Get to the point quickly
- **Technical**: Use precise terminology
- **Actionable**: Focus on what to do
- **Present tense**: Write in active voice
- **Imperative mood**: Use commands for instructions

### 6.2 Sentence Structure
```markdown
✅ "Use REM units for all measurements."
❌ "You should be using REM units when you're measuring things."

✅ "Define the mandatory code conventions."
❌ "This document will help define what the mandatory conventions are."
```

### 6.3 Technical Writing Rules
1. Start with the outcome or objective
2. Provide context only when necessary
3. Use examples to clarify complex concepts
4. Include rationale for important decisions
5. Link to related documentation

.


.

## 7. 📐 Templates

### 7.1 Knowledge Article Template
```markdown
# [Topic] - [Descriptive Subtitle]

[Brief introduction explaining purpose and value]

## 📋 Table of Contents

- [1. 📄 Description](#description)
- [2. 🧭 [Section Name]](#section-name)
- [3. 🛠️ Implementation](#implementation)
- [4. ✅ Best Practices](#best-practices)

.

## 1. 📄 Description

[Brief description of the document’s purpose and scope]

.

[Continue sections...]
```

### 7.2 Section Patterns
- **Description**: Define purpose and goals
- **Core Concepts**: Explain fundamental ideas
- **Implementation**: Show how to apply
- **Examples**: Provide concrete usage
- **Best Practices**: List do's and don'ts
- **Troubleshooting**: Common issues and solutions
- **Reference**: Quick lookup information


---

**Remember**: Apply these standards to maintain professional, consistent documentation across the project.