# Product Owner System - User Guide v0.912

Transforms requests into professional development tickets, strategic PRDs, and documentation through intelligent interactive guidance with automatic DEPTH processing.

## 📋 Table of Contents

- [🆕 What's New In V0.912](#whats-new-in-v0912)
- [🔧 What's Improved](#whats-improved)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🎫 Ticket Mode](#ticket-mode)
- [🚀 PRD Mode](#prd-mode)
- [📄 Doc Mode](#doc-mode)
- [🧠 DEPTH Thinking Framework](#depth-thinking-framework)
- [🎯 Automatic Complexity Detection](#automatic-complexity-detection)

---

<a id="whats-new-in-v0912"></a>
## 🆕 What's New In V0.912

### DEPTH Framework Enhancements (v0.102)
- **Structured Phase Distribution:** Standardized 10-round flow (D→H) with explicit internal state tracking
- **Formal Quality Gates:** Detection signals, severity scoring, and action matrices across all phases
- **Robust Error Recovery:** Retry policies, rollback strategies, and escalation paths with minimal user disruption
- **Output Discipline:** Strict constraints prevent scope expansion; multiple perspectives converge to single deliverable
- **Configurable Visibility:** Internals hidden by default with optional brief summaries when explicitly enabled

### Interactive Mode Improvements (v0.302)
- **Critical Formatting Enforcement:** Validation rules prevent emoji bullets and single-line compression
- **Pre-Response Checklist:** 6-point quality gate ensures markdown compliance before every response
- **Multi-Line Preservation:** Strict enforcement of proper bullet structure and spacing
- **Format Validation Gates:** CRITICAL severity checks for markdown compliance and line break preservation

### Updated Files in v0.912
- **Writer:** v0.912 - Visibility configurable DEPTH alignment; streamlined without redundant rules
- **DEPTH Framework:** v0.102 - Improved clarity; reduced redundancy; YAML/Markdown specs; visibility configurable
- **Interactive Mode:** v0.302 - Enhanced formatting enforcement with validation rules and pre-response checklist

---

<a id="whats-improved"></a>
## 🔧 What's Improved

### DEPTH Framework Enhancements ✅
**Clarity & Discipline:**
- Standardized 10-round phase distribution (D→H) with explicit internal state and context layers
- Strict output constraints and template compliance; no scope expansion

**Quality & Recovery:**
- Formal quality gates with detection signals and severity scoring
- Structured recovery protocol (action matrix, retry, rollback, escalation)

### Interactive Mode Enhancements ✅
**Formatting Enforcement:**
- Enhanced validation rules for markdown formatting
- Pre-response checklist to prevent formatting errors
- Strict multi-line bullet preservation
- Prohibited emoji bullet detection

---

<a id="key-features"></a>
## ✨ Key Features

- **🚀 Three Modes**: Documentation, PRDs, Tickets & Stories
- **🧠 DEPTH Framework**: 5-phase methodology with automatic processing
- **🎯 Smart Complexity**: Automatic detection and template scaling
- **⚡ Quick Mode**: Zero-wait creation with auto-scaled thinking (1-5 rounds)
- **💬 Single Question Flow**: ALL information gathered at once
- **🔒 Output Constraints**: Exact request = exact output
- **📦 Self-Contained Templates**: Each template includes all its own rules

---

<a id="quick-setup"></a>
## 🚀 Quick Setup

### Step 1: Create A Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Product Owner"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Product Owner - v0.912.md` 
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project:

**Core Documents (Latest Versions):**
- `Product Owner - DEPTH Thinking Framework - v0.102.md`
- `Product Owner - Interactive Mode - v0.302.md` 

**Self-Contained Templates (Current Versions):**
- `Product Owner - Template - Ticket Mode - v0.131.md` 
- `Product Owner - Template - PRD Mode - v0.129.md` 
- `Product Owner - Template - Doc Mode - v0.118.md` 

**Note:** Artifact Standards file no longer needed - all rules embedded in templates

### Step 4: Start Creating
```
need user authentication        # Interactive discovery flow
$quick auth PRD                 # Immediate PRD creation (1-5 rounds auto)
$prd payment platform           # Direct PRD mode (10 rounds auto)
$ticket payment integration     # Direct ticket mode (10 rounds auto)
```

---

<a id="operating-modes"></a>
## 🎛️ Operating Modes

**Default Mode:** The system defaults to `$interactive` with automatic 10-round DEPTH unless specified.

| Mode | Purpose | Questions | DEPTH Processing | Template Version | Output |
|------|---------|-----------|-----------------|------------------|---------|
| **Interactive** | Determine what to create | 1 comprehensive | 10 rounds auto | Auto-selected | Exact request |
| **$quick** | Fast creation | NONE | 1-5 auto-scaled | Auto-selected | Exact request |
| **$doc** | Documentation | 1 comprehensive | 10 rounds auto | v0.118 | Requested doc only |
| **$prd** | Product requirements | 1 comprehensive | 10 rounds auto | v0.129 | Requested PRD only |
| **$story** | User stories | 1 comprehensive | 10 rounds auto | v0.131 | Requested story only |
| **$ticket** | Dev tickets | 1 comprehensive | 10 rounds auto | v0.131 | Requested ticket only |

### Interactive Flow (Default) - Single Question Format
```
Welcome! Let's create exactly what you need. 🎯

Please provide ALL of the following information:

1️⃣ **What type of deliverable?**
   • Development ticket - Feature or bug with QA checklist
   • User story - Narrative format without checklist
   • PRD - Strategic initiative or detailed specs
   • Documentation - User guide, feature docs, or strategy

2️⃣ **What's the scope or platform?**
   • For tickets: BE, FE, Mobile, FS, DevOps, or QA
   • For PRDs: Web, Mobile, Web+Mobile, or All platforms
   • For docs: Simple (2-3 sections), Standard (4-6), or Complex (7+)

3️⃣ **Brief description of what you need**
   • What are you building/fixing?
   • Any specific requirements or context?

Please respond with complete information (e.g., "1. Ticket, 2. BE, 3. User authentication system")

[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]
```

---

<a id="ticket-mode"></a>
## 🎫 Ticket Mode (v0.131 - More Concise)

### Improved Concise Format
The new v0.131 templates feature:
- **Compressed About sections** - 1-2 lines with bold key-value pairs
- **Streamlined requirements** - Bullet format with inline descriptions
- **Tighter success criteria** - Essential metrics only
- **Cleaner checklists** - Optimized for scannability

### Example of New Concise Format
```markdown
Mode: $ticket | Complexity: Standard | Template: v0.131
---
[FEATURE] Service: Authentication

# ⌘ About

**Purpose:** Enable secure user login via OAuth  
**Value:** Reduce password fatigue, improve security  
**Users:** All platform users

---

## ✦ Success Criteria

- Users complete login in <3 seconds
- OAuth providers integrate successfully
- Zero security vulnerabilities
- 99.9% authentication uptime

---

## ❖ Requirements

### ◻ Functional
- Core: OAuth 2.0 login flow
- Providers: Google, GitHub, Microsoft
- Security: Token refresh, session management
- UX: One-click authentication

---

## ✓ Resolution Checklist

⚠️ Complete all items before moving to QA

[] OAuth flow implemented
[] Provider integration tested
[] Security review passed
[] Performance validated
[] Documentation updated
[] Monitoring configured
```

### Ticket Complexity Levels
| Type | Sections | Resolution Items | Template Focus |
|------|----------|------------------|----------------|
| **Simple** | 2-3 | 4-6 items | Bug fixes, small updates |
| **Standard** | 4-5 | 8-12 items | Features, enhancements |
| **Complex** | 6-8 | 12-20 items | Platforms, migrations |

---

<a id="prd-mode"></a>
## 🚀 PRD Mode (v0.129)

### Product Requirements with Embedded Rules
The v0.129 template includes:
- All formatting standards built-in
- Complete symbol hierarchy defined
- Quality checks embedded
- Error recovery included

### PRD Complexity Levels
| Level | Features | Timeline | Template Sections | Focus |
|-------|----------|----------|-------------------|-------|
| **Initiative** | 5-10 | Quarterly | 5-7 sections | Single team deliverables |
| **Program** | 10-20 | Half-year | 8-10 sections | Multi-team coordination |
| **Strategic** | 20+ | Annual | 10+ sections | Platform transformation |

---

<a id="doc-mode"></a>
## 📄 Doc Mode (v0.118)

### Documentation with Integrated Standards
The v0.118 template features:
- Complete formatting rules embedded
- Self-contained quality checks
- Standalone operation
- No external dependencies

### Documentation Complexity
| Type | Main Sections | Depth | Use Case |
|------|---------------|-------|----------|
| **Simple** | 2-3 | Quick reference | Product briefs, overviews |
| **Standard** | 4-6 | Detailed guide | Feature specs, user guides |
| **Complex** | 7+ | Comprehensive | Strategy docs, platforms |

---

<a id="depth-thinking-framework"></a>
## 🧠 DEPTH Thinking Framework

### Automatic DEPTH Processing System
| Mode | Processing Depth | User Choice | Application | Output |
|------|-----------------|-------------|-------------|---------|
| **Standard Modes** | 10 rounds enforced | None | Automatic | Exact request |
| **$Quick Mode** | 1-5 auto-scaled | None | Complexity-based | Exact request |

**DEPTH Definition:**
DEPTH methodology (Discover, Engineer, Prototype, Test, Harmonize) is automatically applied to ensure quality while maintaining output constraints. Internals are hidden by default; visibility is configurable when explicitly enabled.

### DEPTH Phases (Applied Automatically)
| Phase | Purpose | Internal Process | User Sees |
|-------|---------|-----------------|-----------|
| **D**iscover | Deep understanding | Multiple perspectives analyze SAME requirement | "Analyzing requirements..." |
| **E**ngineer | Solution generation | Various approaches for SAME deliverable | "Optimizing approach..." |
| **P**rototype | Build framework | Template structure for exact request | "Building deliverable..." |
| **T**est | Validate quality | Quality checks on requested content | "Ensuring quality..." |
| **H**armonize | Final polish | Excellence for specific output | Final polished artifact |

### Silent Excellence Principles
```markdown
🎯 Processing your request...

[DEPTH processing runs internally (hidden by default)]
[Multiple perspectives analyze the SAME requirement]
[Output contains ONLY what was requested]
```

**Note:** Users don't choose processing depth. Internals remain hidden by default; optional brief summaries can be enabled without exposing step-by-step analysis.

### DEPTH v0.102 Improvements (Summary)
- Clearer phase distribution and state: standardized 10-round flow (D→H) with explicit internal state, perspectives, metrics, and context layers; templates referenced (Ticket v0.131, PRD v0.129, Doc v0.118).
- Stronger output discipline: strict output constraints prevent scope expansion; templates are followed exactly; multiple approaches considered internally but converge to one deliverable.
- Robust QA and recovery: formal quality gates across phases, detailed detection signals, severity-based action matrix, retry and rollback strategies, and escalation with minimal user-facing messaging.
- Configurable visibility: internals hidden by default with optional brief summaries; performance metrics tracked (template compliance, wait compliance, verification success) to ensure consistent excellence.

---

<a id="automatic-complexity-detection"></a>
## 🎯 Automatic Complexity Detection

### For Tickets
| Indicators | Complexity | Sections | Resolution Items | DEPTH | Output |
|------------|------------|----------|------------------|-------|---------|
| bug, fix, typo, update | **Simple** | 2-3 | 4-6 | 10 rounds (2 if $quick) | That specific bug only |
| feature, dashboard, api | **Standard** | 4-5 | 8-12 | 10 rounds (3 if $quick) | Requested feature only |
| platform, architecture, migration | **Complex** | 6-8 | 12-20 | 10 rounds (5 if $quick) | Specified platform only |

### Enhanced Template Selection with Tie-Breaking
System includes intelligent tie-breaking for ambiguous cases:
- "bug platform" → Analyzes context, typically Standard template for that bug
- "feature migration" → Complex template for that feature
- Complex keywords override simpler ones
- Defaults to Standard when unclear
- **Important:** Complexity affects TEMPLATE SIZE, not content scope

### Output Guarantee Examples
```
User: "Fix login bug"
→ Simple template for THAT login bug only
NOT: Simple template with multiple bugs

User: "Build dashboard"
→ Standard template for THAT dashboard only
NOT: Standard template with extra features

User: "Platform migration"
→ Complex template for THAT migration only
NOT: Complex template with multiple platforms
```