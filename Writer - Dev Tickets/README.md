# Dev Ticket Writer - User Guide v3.1.0

A comprehensive system that transforms development requests into clear, actionable tickets focusing on user value and business outcomes. Features 5 operating modes, intelligent prompt clarification, and educational Interactive mode that teaches product thinking.

## 🆕 What's New in v3.1.0

- **Prompt Improvement Layer**: Automatically clarifies vague requests like "fix auth" → "create bug fix ticket for authentication"
- **Developer Abbreviation Support**: Understands API, DB, UI, auth, and other common dev terms
- **Invisible Enhancement**: <0.5 second processing preserves Interactive mode's educational flow
- **Smart Pattern Recognition**: Transforms "need login" → "create feature ticket for login"
- **30-40% Fewer Clarifications**: Better first-attempt ticket creation
- **Maintained Philosophy**: Still focuses on WHAT and WHY, never HOW

## Overview

The Dev Ticket Writer helps teams create professional development tickets that communicate user value and business outcomes. By focusing on WHAT needs to be done and WHY it matters (not HOW to implement), it bridges the communication gap between product and development while teaching product thinking principles.

## ✨ Key Features

- **5 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $epic
- **Prompt Improvement**: Clarifies vague requests without adding assumptions
- **Educational Focus**: Interactive mode teaches product management through practice
- **Professional Symbols**: Mandatory abstract symbols (❖, ◇, →, ✓, ⊗) for visual hierarchy
- **Resolution Checklists**: Required actionable steps scaled by complexity
- **Figma Integration**: Optional design extraction for UI features
- **2-Minute Rule**: All tickets readable in under 2 minutes
- **Artifact Delivery**: Every ticket in reusable markdown artifacts

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v3.1"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v3.1.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Quick Reference Card - v1.1.0.md` (Daily companion)
- `Ticket - Templates & Standards - v1.0.0.md` (All templates and symbols)
- `Ticket - Examples Library - v1.0.0.md` (Real-world examples)
- `Ticket - Interactive Mode - v1.3.0.md` (Conversational spec)
- `Ticket - Prompt Improvement - v1.0.0.md` (Request clarification)

### Step 4: Start Creating Tickets
Simply describe what you need:
```
fix login bug
need user profiles  
$s dashboard feature
add API endpoint
```

## 🎛️ Operating Modes

| Mode | Command | When to Use | Resolution Checklist | MCP Usage |
|------|---------|-------------|---------------------|-----------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Adaptive | Cascade (3-5 thoughts) |
| **Quick** | `$q` | Simple features (explicit request) | 3-5 items | Sequential (1-2 thoughts) |
| **Standard** | `$s` | Full features (explicit request) | 8-15 items | Sequential (2-3 thoughts) |
| **Complex** | `$c` | Multi-phase implementations | 15-30 items | Cascade (3-5 thoughts) |
| **Epic** | `$e` | Major initiatives | 10-20 items | Cascade (5+ thoughts) |

**Note:** Interactive mode is the default unless explicitly specified otherwise.

## 📝 How Prompt Improvement Works

The system invisibly enhances vague requests before processing:

### What Gets Enhanced
```
"fix auth" → "create bug fix ticket for authentication"
"DB slow" → "create performance ticket for database"
"need API docs" → "create feature ticket for application programming interface documentation"
```

### Common Developer Abbreviations
- **Technical**: API, DB, UI, UX, FE, BE, auth, config, env, repo
- **Process**: QA, CI/CD, MVP, POC, PR
- **Performance**: perf, opt, mem
- **Security**: sec, vuln, 2FA

### What DOESN'T Change
- Implementation details (never added)
- Priority or complexity (never assumed)
- Mode commands ($q, $s, etc.)
- Already clear requests
- The need for Interactive mode questions

## 🏗️ Core Components

### WHAT/WHY Philosophy
- **WHAT**: Clear description of the feature/fix needed
- **WHY**: User value and business outcomes
- **NOT HOW**: Leave implementation to developers

### Symbol System (Required)
- **❖** - Titles and major features
- **◇** - Requirements and processes
- **→** - Designs & References
- **✓** - Success criteria AND Resolution Checklist
- **⊗** - Dependencies

### Ticket Structure
1. Title with ❖ symbol
2. User Value statement
3. Business Goal (measurable)
4. Requirements (outcome-focused)
5. Success Criteria (checkboxes)
6. Resolution Checklist (REQUIRED)
7. Dependencies (if any)

## 📊 Interactive Mode Example

```
User: need login
System: [Invisibly enhances to "create feature ticket for login"]

System: Great! Let's create a clear ticket together. I'll help you think through the key aspects:

1. What specific problem does login solve for your users?
2. What type of login do you need (email/password, social, both)?
3. How will we measure if this feature is successful?

User: Users can't save preferences. Email/password. 80% registration rate.

System: Perfect! Do you have any Figma designs for the login flow?

[Creates complete ticket with all sections, symbols, and resolution checklist]
```

## 🤖 Educational Focus

Interactive mode teaches product thinking by:
- Asking strategic questions about user value
- Focusing on business outcomes
- Showing quality metrics and scores
- Providing learning points
- Building skills through practice

## 📈 Quality Assurance

### 2-Minute Readability
All tickets must be scannable and understood in under 2 minutes.

### Resolution Checklist Scaling
- **Quick**: 3-5 simple tasks
- **Standard**: 8-15 tasks in categories
- **Complex**: 15-30 phase-based tasks
- **Epic**: 10-20 coordination tasks

### Success Metrics
- 85% of users complete ticket creation
- 95% meet quality standards
- <5 minute average conversation
- 100% maintain readability standards

## 🔧 MCP Tools Integration

The system intelligently selects thinking tools based on complexity:

### Sequential Thinking MCP
- Simple requests and clear requirements
- Quick ($q) and Standard ($s) modes
- 1-3 thoughts for analysis

### Cascade Thinking MCP
- Interactive mode (always)
- Complex ($c) and Epic ($e) modes
- Unclear requirements needing exploration
- 3-5+ thoughts with branching

### Figma MCP (Optional)
- UI feature tickets
- Design extraction and understanding
- Never required, always beneficial

## 📚 Example Transformations

### Bug Fix
**Input:** "fix checkout bug"
**Enhanced:** "create bug fix ticket for checkout issue"
**Result:** Complete bug ticket with reproduction steps, expected behavior, and fix checklist

### Feature Request
**Input:** "need API"
**Enhanced:** "create feature ticket for application programming interface"
**Interactive:** Asks about API purpose, consumers, and success metrics
**Result:** Structured feature ticket with clear requirements and business value

### Performance Issue
**Input:** "DB queries slow"
**Enhanced:** "create performance ticket for database queries"
**Result:** Performance ticket with current metrics, target metrics, and optimization checklist

## ⚠️ Important Notes

- **Never provides implementation advice** - Only creates tickets
- **Always uses artifacts** - Every ticket in markdown artifact
- **No em dashes** - Uses alternatives for readability
- **Interactive is default** - Unless mode explicitly specified
- **Figma optional** - Never blocks ticket creation
- **Quick Reference Card** - Keep open for daily use

## 📦 Version History

- **v3.1.0**: Added prompt improvement layer and developer abbreviations
- **v3.0.0**: Introduced mandatory Resolution Checklists
- **v2.0.0**: Interactive mode as default, enhanced educational focus
- **v1.0.0**: Initial WHAT/WHY philosophy implementation

## 🎯 Key Principles

1. **Democratize product thinking** through guided ticket creation
2. **Focus on user value** not technical implementation
3. **Teach through practice** with Interactive mode
4. **Maintain 2-minute readability** for all tickets
5. **Scale complexity appropriately** with different modes
6. **Preserve user intent** while clarifying requests

## 🆘 Troubleshooting

### Prompt Improvement Issues
- **Abbreviation not expanding**: Not in dictionary, will be preserved
- **Wrong enhancement**: Check bypass conditions
- **Mode not working**: Explicit mode commands bypass enhancement

### Interactive Mode
- **Too many questions**: System limits to 3-4 maximum
- **Not getting guidance**: Ensure no mode specified
- **Figma not connecting**: It's optional, continue without

### Common Problems
- **Missing symbols**: Required in all sections
- **No Resolution Checklist**: Required for every ticket
- **Too long to read**: Violates 2-minute rule
- **Implementation details**: Remove HOW, keep WHAT/WHY

## 📚 Additional Resources

- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [SMART Goals](https://www.atlassian.com/blog/productivity/how-to-write-smart-goals)
- [Figma for Developers](https://help.figma.com/hc/en-us/articles/360040028273)

---

*Transform vague requests into clear tickets. Teach product thinking through practice. Focus on WHAT and WHY, never HOW.*