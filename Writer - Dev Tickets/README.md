# Dev Ticket Writer - User Guide v4.0.0

A comprehensive system that transforms development requests into clear, actionable tickets with developer-first clarity. Features user-specified scope and labels, structured problem/solution descriptions, concise frontend implementation specs, and 5 operating modes including educational Interactive mode.

## 🆕 What's New in v4.0.0

- **5 Modes Instead of 6**: Complex mode now handles both phased development AND child tickets
- **Interactive Offers**: System ALWAYS offers Interactive guidance when users specify $s or $c modes
- **Concise Spec Mode**: 1-3 questions max, 20-60 lines output, copy-paste ready code
- **Smart Pattern Detection**: Instant generation for common patterns like "hide scrollbar"
- **Enhanced Complex Mode**: Choose between phased approach or child ticket breakdown

## Overview

The Dev Ticket Writer helps teams create professional development tickets that are "clear at first glance" for developers while teaching product thinking principles. By focusing on WHAT needs to be done and WHY it matters (not HOW to implement), it bridges the communication gap between product and development. When implementation details are needed, the concise Spec mode provides focused, copy-paste ready solutions.

## ✨ Key Features

- **Developer-First Clarity**: User-specified scope prefixes, structured descriptions
- **5 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $spec
- **Interactive Offers**: Automatic guidance offers for $standard and $complex modes
- **Concise Spec Mode**: Minimal conversation (1-3 questions), working code examples
- **Enhanced Symbol System**: Professional symbols (❖, ◇, **◊**, →, ✓, ⊗, ⚠︎, ⁉) for visual hierarchy
- **Prompt Improvement**: Clarifies vague requests without adding assumptions
- **Educational Focus**: Interactive mode teaches product management through practice
- **Resolution Checklists**: Required actionable steps scaled by complexity
- **2-Minute Rule**: All tickets readable in under 2 minutes
- **Artifact Delivery**: Every ticket in reusable markdown artifacts

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v4.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v4.0.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Quick Reference Card - v2.0.0.md` (Updated with Interactive offers)
- `Ticket - Templates & Standards - v2.0.0.md` (Merged Complex mode templates)
- `Ticket - Examples Library - v2.0.0.md` (New concise Spec examples)
- `Ticket - Interactive Mode - v1.6.0.md` (Enhanced with offer system)
- `Ticket - Spec Mode Frontend Guide - v2.0.0.md` (Concise implementation focus)
- `Ticket - Prompt Improvement - v1.0.0.md` (Request clarification)

### Step 4: Start Creating Tickets
Simply describe what you need:
```
fix login bug                    # Interactive mode (default)
$q user profiles                 # Quick mode
$s dashboard feature             # Standard (offers Interactive)
$c payment integration           # Complex (offers Interactive)
$spec hide scrollbar             # Spec mode (instant generation)
```

## 🎯 Interactive Offers (NEW)

When users specify `$standard` or `$complex`, the system ALWAYS offers Interactive assistance first:

```markdown
User: $s user authentication

System: I see you want a standard ticket for user authentication.

Would you like me to:
1. **Guide you through creating it interactively** - I'll ask questions to ensure we capture everything
2. **Create it directly** - I'll use my best judgment

Which would you prefer? (1 or 2)
```

This ensures users get the best possible ticket quality while respecting their autonomy.

## 🎛️ Operating Modes

| Mode | Command | When to Use | Resolution Checklist | Interactive Offer | Focus |
|------|---------|-------------|---------------------|-------------------|-------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Adaptive | N/A (Default) | Conversational guidance |
| **Quick** | `$q` | Simple features (explicit) | 3-5 items | No | Essential requirements |
| **Standard** | `$s` | Full features (explicit) | 8-15 items | **YES - Always** | Complete context |
| **Complex** | `$c` | Major features/initiatives | 15-30 items | **YES - Always** | Phases OR child tickets |
| **Spec** | `$spec` | Frontend implementation | 20-60 lines | No | Concise code solutions |

**Note:** Interactive mode is the default unless explicitly specified.

## 🔧 Complex Mode (Enhanced)

Complex mode now offers two approaches for major features:

### Option A: Phased Development
For incremental building of a single large feature:
- Phase 1: Foundation
- Phase 2: Core Features
- Phase 3: Enhancement

### Option B: Child Ticket Breakdown
For multi-team coordination:
- Infrastructure tickets
- Feature implementation tickets
- Quality & polish tickets

The system helps you choose the right approach during ticket creation.

## 💻 Spec Mode (Transformed)

The new Spec mode is concise and efficient:

### Fast Paths (0-1 Questions)
```markdown
User: $spec hide scrollbar
System: Browser compatibility needed?
User: yes
[Generates 20-line CSS solution immediately]
```

### Component Patterns (2-3 Questions)
```markdown
User: $spec virtual scroll table
System: Quick setup:
1. Row count?
2. React/Vue?
User: 50k, React
[Generates 40-line working implementation]
```

### Key Features
- **Auto-detection** of common patterns
- **1-3 questions maximum**
- **20-30 lines for simple, 40-60 for complex**
- **Copy-paste ready code**
- **No placeholders or comments**

## 🎯 Scope Prefixes

Every ticket title includes a user-specified scope prefix:

| Prefix | Use For | Example |
|--------|---------|---------|
| **[BE]** | Backend features | `# ❖ [BE] User Authentication` |
| **[FE]** | Frontend features | `# ❖ [FE] Dashboard Redesign` |
| **[Mobile]** | Mobile app features | `# ❖ [Mobile] Push Notifications` |
| **[FS]** | Full stack features | `# ❖ [FS] Real-time Chat` |
| **[DevOps]** | Infrastructure | `# ❖ [DevOps] CI/CD Pipeline` |
| **[QA]** | Testing features | `# ❖ [QA] Test Automation` |

**Note:** System asks users to specify scope - never assumes.

## 📝 Structured Descriptions

Every ticket uses a concise, structured description format:

```markdown
# ❖ [FE] Advanced Search Filters

Our search functionality is failing to meet user needs and causing lost revenue.

⚠︎ **Key problems/changes:**
* **High abandonment rate** - Users give up before finding what they need
* **No filtering options** - Users scroll through irrelevant results
* **Poor relevance** - Basic keyword matching returns unrelated items

⁉ **Reasons why:**
By implementing comprehensive filtering capabilities, we'll dramatically improve product discovery and increase conversion.

**User Value:** Find exactly what you need with powerful filters
**Business Goal:** Dramatically reduce search abandonment rate
```

## 🏷️ Label System

The system asks users to specify appropriate labels:

### Common Label Categories
- **Type**: feature, bug, improvement, technical-debt
- **Component**: authentication, payments, search, UI, database
- **Priority**: high, medium, low (if your team uses these)

Example:
```markdown
System: What labels should I add to this ticket?
User: feature, search, filters, high-priority
```

## 💬 Interactive Mode Flow

The default conversational mode:

### Typical Flow
1. User describes feature (no mode specified)
2. System asks about user needs and problems
3. System asks for scope ([BE], [FE], etc.)
4. System asks for labels
5. System asks about success metrics
6. Creates comprehensive ticket
7. Delivers with quality dashboard

### Quality Dashboard
```markdown
📊 Interactive Mode Report
Overall Quality Score: 4.5/5 ⭐

✅ Ticket Structure Checklist:
✓ User value clearly stated
✓ Scope properly identified: [FS]
✓ Labels added: feature, search, filters
✓ Business goal measurable
✓ Requirements outcome-focused
✓ 2-minute read test: PASS (1:45)
```

## 📋 Examples

### Interactive Mode (Default)
```
User: need user profiles
System: [Starts conversation about user needs, then asks for scope and labels]
```

### Standard with Interactive Offer
```
User: $s authentication system
System: Would you like me to:
1. Guide you through creating it interactively
2. Create it directly
User: 1
System: [Starts Interactive flow]
```

### Complex with Phased Approach
```
User: $c real-time collaboration
System: [Offers Interactive, then helps choose between phases or child tickets]
```

### Spec Mode (Concise)
```
User: $spec debounced search input
System: React or Vanilla JS?
User: React
System: [Generates 25-line working implementation]
```

## 🔧 MCP Tools Integration

The system intelligently selects thinking tools:

### Sequential Thinking MCP
- Quick ($q), Standard ($s), and Spec ($spec) modes
- 1-3 thoughts for analysis

### Cascade Thinking MCP
- Interactive mode (always)
- Complex ($c) mode
- 3-5+ thoughts with branching

### Figma MCP (Optional)
- UI feature tickets
- Design extraction
- Never required, always beneficial

## 📚 Example Outputs

### Standard Ticket (After Interactive Offer)
```markdown
# ❖ [FS] User Authentication System

[Comprehensive description with ⚠︎ problems and ⁉ reasons]
[User value and business goal]
[Detailed requirements with **◊** sub-headings]
[Success criteria]
[Resolution checklist 8-15 items]
[User-specified labels]
```

### Complex Ticket (Phased Approach)
```markdown
# ❖ [FS] Real-time Collaboration Platform

[Strategic overview]
[Phase 1: Foundation]
[Phase 2: Core Features]
[Phase 3: Enhancement]
[Resolution checklist 15-30 items organized by phase]
```

### Spec Implementation
```markdown
# Virtual Scroll Table

## Objective
Efficiently render 50k rows without performance issues.

## Implementation
```typescript
[40 lines of working React code]
```

## Key Points
- Only renders visible rows
- Smooth scrolling
- Add memo() for optimization
```

## ⚠️ Important Notes

- **Interactive offers required** - System always offers for $s and $c
- **Scope/labels required** - System asks users to specify
- **No assumptions** - System never guesses
- **Complex mode flexible** - Handles phases OR child tickets
- **Spec mode concise** - 1-3 questions, working code only
- **No percentages** - Use descriptive language
- **Always uses artifacts** - Every ticket/spec in markdown

## 📦 Version History

- **v4.0.0**: 5 modes (merged Complex/Epic), Interactive offers, concise Spec mode
- **v3.5.0**: User-specified scope and labels, enhanced Interactive mode
- **v3.4.0**: Structured descriptions (⚠︎/⁉), Spec mode, implementation references
- **v3.0.0**: Introduced mandatory Resolution Checklists
- **v2.0.0**: Interactive mode as default, educational focus
- **v1.0.0**: Initial WHAT/WHY philosophy implementation

## 🎯 Key Principles

1. **User empowerment** through Interactive offers for better tickets
2. **No assumptions** - always ask for scope and labels
3. **Flexibility** - Complex mode adapts to feature needs
4. **Conciseness** - Spec mode delivers focused solutions
5. **Education** - Learn product thinking through practice
6. **Developer clarity** - Structured, scannable tickets
7. **2-minute readability** for all tickets

## 🆘 Troubleshooting

### Interactive Offers
- **Not seeing offer?** - Only appears for $s and $c modes
- **Want to skip?** - Choose option 2 for direct creation
- **Changed mind?** - System can switch to Interactive mid-flow

### Complex Mode
- **Phases vs Child tickets?** - System helps you choose
- **Too many requirements?** - Consider child ticket approach
- **Need both?** - Hybrid approach possible

### Spec Mode
- **Too many questions?** - Should be 1-3 max
- **Code not working?** - All examples are tested
- **Need more sections?** - Spec mode stays minimal by design

### Scope & Labels
- **Forgot to specify?** - System will ask
- **Wrong scope chosen?** - Be specific about work location
- **Too many labels?** - Keep to 3-5 most relevant

## 📚 Additional Resources

- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [MDN Web Docs](https://developer.mozilla.org/) (for spec mode)

---

*Transform vague requests into crystal-clear tickets with Interactive guidance. Create concise implementation specs with minimal conversation. Complex mode adapts to your needs. Make every ticket scannable in under 2 minutes.*