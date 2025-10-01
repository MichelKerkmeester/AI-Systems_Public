# Product Owner System - User Guide v0.910

Transforms requests into professional development tickets, strategic PRDs, and documentation through intelligent interactive guidance with automatic DEPTH processing.

## 📋 Table of Contents

- [🆕 What's New In V0.910](#whats-new-in-v0910)
- [🔧 What's Fixed in Latest Update](#whats-fixed-in-latest-update)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🎫 Ticket Mode](#ticket-mode)
- [🚀 PRD Mode](#prd-mode)
- [📄 Doc Mode](#doc-mode)
- [🧠 DEPTH Thinking Framework](#depth-thinking-framework)
- [🎯 Automatic Complexity Detection](#automatic-complexity-detection)
- [🔍 Symbol & Formatting Reference](#symbol--formatting-reference)
- [📊 Header Format](#header-format)
- [🆘 Troubleshooting](#troubleshooting)
- [📦 Version History](#version-history)

---

<a id="whats-new-in-v0910"></a>
## 🆕 What's New In V0.910

### Major Framework Alignment
- **DEPTH Methodology:** Replaced all "ultrathink" references with proper DEPTH terminology
- **Silent Excellence:** Enhanced emphasis on hidden complexity, user sees simple messages
- **Interactive Flow Fixed:** Single comprehensive question with explicit WAIT markers
- **Output Constraints:** Strong enforcement of exact request = exact output
- **Critical Rules:** NEVER answer own questions, ALWAYS wait for user response

### Updated Template Versions
- **Artifact Standards:** v0.147 (was v0.145)
- **DEPTH Framework:** v0.100 (NEW - replaces ATLAS)
- **Interactive Mode:** v0.300 (was v0.286)
- **Ticket Template:** v0.128 (was v0.125)
- **PRD Template:** v0.128 (was v0.125)
- **Doc Template:** v0.117 (was v0.115)
- **Writer:** v0.910 (was v0.907)

### Processing Standards
- **Standard Modes:** 10-round DEPTH automatic (not user choice)
- **Quick Mode:** 1-5 rounds auto-scaled based on complexity
- **Multiple Perspectives:** All analyze the SAME requirement
- **Convergent Output:** Many approaches considered, ONE delivered
- **No Scope Expansion:** Template scaling affects structure, not content

### Maintained from V0.907
- **Header at Top:** System metadata as first line of artifact
- **Single Question Flow:** All information in ONE prompt
- **Enhanced Formatting:** Clear structure with proper symbols
- **Template Compliance:** Full v0.xxx standards

---

<a id="whats-fixed-in-latest-update"></a>
## 🔧 What's Fixed in Latest Update

### Critical Terminology Update ✅
**Changed "ultrathink" → "DEPTH methodology" throughout all files**
- All 4 template files updated with correct terminology
- Processing descriptions now reference DEPTH rounds
- Automatic application emphasized (no user choice)

**Files affected:** All templates (Ticket, PRD, Doc, Artifact Standards)

### Interactive Question Format Fixed ✅
**Corrected to single comprehensive question pattern:**
- Added `[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]` markers
- Emphasized gathering ALL information at once
- Fixed examples to show proper wait behavior

**Before (Wrong):**
```markdown
1️⃣ What type?
2️⃣ What scope?
3️⃣ Description
[Multiple interactions implied]
```

**After (Correct):**
```markdown
Please provide ALL of the following:
1️⃣ Type
2️⃣ Scope  
3️⃣ Description
[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]
```

### DEPTH Processing Documentation ✅
**Added clear processing standards:**
- 10 rounds automatic for standard modes
- 1-5 auto-scaled for $quick
- Silent processing (methodology hidden)
- Multiple perspectives analyze SAME requirement
- Single output matching exact request

### Output Constraint Enforcement ✅
**Strengthened throughout all templates:**
- "Contains ONLY what user requested"
- "No invented features or scope expansion"
- "Template structure, not content expansion"
- Added examples showing exact request = exact output

### Critical Rule Reinforcement ✅
**Enhanced enforcement of key principles:**
- **NEVER answer own questions** - multiple reinforcements added
- **WAIT for user response** - explicit markers throughout
- **Silent excellence** - methodology details hidden from users
- **Single output** - one deliverable matching exact request

### Quality Improvements

**Before Update:**
- Mixed terminology (ultrathink/DEPTH)
- Multi-step question patterns
- Missing wait markers
- Weak output constraints
- Unclear processing standards

**After Update:**
- Consistent DEPTH terminology
- Single comprehensive questions
- Clear WAIT markers throughout
- Strong output constraints
- Explicit processing documentation

---

<a id="key-features"></a>
## ✨ Key Features

- **🚀 Three Modes**: PRDs, Stories, Tickets & Documentation
- **🧠 DEPTH Framework**: 5-phase methodology with automatic processing
- **🎯 Smart Complexity**: Automatic detection and template scaling
- **⚡ Quick Mode**: Zero-wait creation with auto-scaled thinking (1-5 rounds)
- **💬 Single Question Flow**: ALL information gathered at once
- **🤖 Automatic Processing**: System-controlled depth (no user choice)
- **📊 Header at Top**: Clean first-line metadata format
- **🔒 Output Constraints**: Exact request = exact output
- **🛡️ Silent Excellence**: Complex processing hidden from users

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
3. Copy and paste: `Writer - Product Owner - v0.910.md` 
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project (all updated with DEPTH framework):

**Core Documents (Latest Versions):**
- `Product Owner - DEPTH Thinking Framework - v0.100.md` (NEW)
- `Product Owner - Interactive Mode - v0.300.md` 
- `Product Owner - Artifact Standards - v0.147.md` 

**Template Documents (Current Versions):**
- `Product Owner - Template - Ticket Mode - v0.128.md` 
- `Product Owner - Template - PRD Mode - v0.128.md` 
- `Product Owner - Template - Doc Mode - v0.117.md` 

### Step 4: Start Creating
```
need user authentication         # Interactive discovery flow
$quick auth PRD                 # Immediate PRD creation (1-5 rounds auto)
$prd payment platform           # Direct PRD mode (10 rounds auto)
$ticket payment integration     # Direct ticket mode (10 rounds auto)
```

---

<a id="operating-modes"></a>
## 🎛️ Operating Modes

**Default Mode:** The system defaults to `$interactive` with automatic 10-round DEPTH unless specified.

| Mode | Purpose | Questions | DEPTH Processing | Scaling | Output |
|------|---------|-----------|-----------------|---------|---------|
| **Interactive** | Determine what to create | 1 comprehensive | 10 rounds auto | Auto-detect | Exact request |
| **$quick** | Fast creation | NONE | 1-5 auto-scaled | Auto-scale | Exact request |
| **$ticket** | Dev tickets | 1 comprehensive | 10 rounds auto | 2-3/4-5/6-8 sections | Requested ticket only |
| **$prd** | Product requirements | 1 comprehensive | 10 rounds auto | 5-10/10-20/20+ features | Requested PRD only |
| **$story** | User stories | 1 comprehensive | 10 rounds auto | 2-3/4-5/6-8 sections | Requested story only |
| **$doc** | Documentation | 1 comprehensive | 10 rounds auto | 2-3/4-6/7+ sections | Requested doc only |

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

### $Quick Mode - Zero-Wait Creation
```
User: $quick - Q1 payments initiative

System: **Quick Mode Activated** ⚡

Creating immediately...
• Auto-detecting type and complexity
• Applying 3 rounds DEPTH (optimized)
• No questions needed

[CREATES ARTIFACT IMMEDIATELY WITH HEADER AT TOP]
```

**Example Artifact Output:**
```markdown
Mode: $quick | Scale: Initiative | Template: v0.128
---
# Q1 Payments Initiative PRD

# ☘ About
[Strategic context with integrated problems...]
```

**$Quick Mode Characteristics:**
- NO questions whatsoever - Proceeds immediately
- Auto-scaled DEPTH - 1-5 rounds based on complexity
- Auto-detect type and scale - Smart complexity detection
- Works with all modes - Tickets, PRDs, and docs
- Output constraints - ONLY what user requested
- Header at top - First line of artifact

---

<a id="ticket-mode"></a>
## 🎫 Ticket Mode

### Development Ticket Creation - Single Question Format
```
User: $ticket payment integration

System: Let me help you create your payment integration ticket. 🎯

Please provide ALL of the following details:

1️⃣ **Format type:**
   • Ticket - Development task with resolution checklist for QA
   • Story - User story format without checklist

2️⃣ **Scope:**
   • BE - Backend/API
   • FE - Frontend/UI
   • Mobile - iOS/Android
   • FS - Full-stack
   • DevOps - Infrastructure
   • QA - Testing

3️⃣ **Requirements & context:**
   • What needs to be built/fixed?
   • Key features or integration points
   • Timeline or dependencies

Please respond with complete information (e.g., "1. Ticket, 2. BE, 3. Stripe API integration for subscriptions")

[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]
```

### Ticket Complexity Levels
| Type | Sections | Resolution Items | Triggers | Output Scope |
|------|----------|------------------|----------|--------------|
| **Simple** | 2-3 | 4-6 items | bug, fix, typo, update | Exact bug/fix only |
| **Standard** | 4-5 | 8-12 items | feature, dashboard, api | Requested feature only |
| **Complex** | 6-8 with phases | 12-20 items | platform, architecture, migration | Specified platform only |

### Ticket Structure & Symbols
```markdown
Mode: $ticket | Complexity: Standard | Template: v0.128
---
[SCOPE] Feature: [Name]

# ☘ About
[Context with integrated problems - FIRST]
[ONLY the requested feature/fix]

---

## ✦ Success Criteria
[Measurable outcomes - AFTER About]

---

## ⌥ Designs & References
[Table format]

---

## ■ Requirements
### ◻ Functional Requirements
[For requested feature ONLY]

---

## ✓ Resolution Checklist
[Scaled items]
```

---

<a id="prd-mode"></a>
## 🚀 PRD Mode

### Product Requirements Document Creation - Single Question Format
```
User: $prd authentication platform

System: Let's create your authentication platform PRD! 📋

Please provide ALL of the following information:

1️⃣ **PRD scale:**
   • Feature PRD - single feature specification
   • Initiative PRD - 5-10 features, single team, quarterly
   • Program PRD - 10-20 features, multi-team, half-year
   • Strategic PRD - 20+ features, platform-wide, annual

2️⃣ **Primary platform:**
   • Web only
   • Mobile only (iOS/Android)
   • Web + Mobile
   • All platforms (Web, iOS, Android, API)

3️⃣ **Key requirements & context:**
   • Core features needed
   • Target audience
   • Business objectives
   • Timeline constraints

Please respond with complete information (e.g., "1. Initiative PRD, 2. Web + Mobile, 3. Real-time analytics for enterprise customers")

[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]
```

### PRD Complexity Levels
| Level | Features | Timeline | DEPTH | Output |
|-------|----------|----------|-------|---------|
| **Initiative** | 5-10 | Quarterly | 10 rounds | User's features only |
| **Program** | 10-20 | Half-year | 10 rounds | Requested platform only |
| **Strategic** | 20+ | Annual | 10 rounds | Specified ecosystem only |

---

<a id="doc-mode"></a>
## 📄 Doc Mode

### Documentation Creation - Single Question Format
```
User: $doc API guide

System: Let's create your documentation! 📚

Please provide ALL of the following details:

1️⃣ **Documentation type:**
   • Product brief - quick overview
   • Feature specification - detailed design
   • Performance tracking - metrics & KPIs
   • Strategy document - comprehensive platform guide

2️⃣ **Complexity level:**
   • Simple - 2-3 main sections, quick reference
   • Standard - 4-6 main sections, detailed guide
   • Complex - 7+ main sections, comprehensive docs

3️⃣ **Focus areas & requirements:**
   • Target audience
   • Key topics to cover
   • Specific sections needed

Please respond with complete information (e.g., "1. Strategy document, 2. Complex, 3. Platform roadmap for executive team")

[SYSTEM MUST STOP HERE AND WAIT FOR USER INPUT - DO NOT PROCEED]
```

### Documentation Output Constraints
| Type | Sections | Coverage | Scope |
|------|----------|----------|-------|
| **Simple** | 2-3 | Essential info | Requested topic only |
| **Standard** | 4-6 | Complete coverage | Specified system only |
| **Complex** | 7+ | Strategic depth | User's platform only |

---

<a id="depth-thinking-framework"></a>
## 🧠 DEPTH Thinking Framework

### Automatic DEPTH Processing System
| Mode | Processing Depth | User Choice | Application | Output |
|------|-----------------|-------------|-------------|---------|
| **Standard Modes** | 10 rounds enforced | None | Automatic | Exact request |
| **$Quick Mode** | 1-5 auto-scaled | None | Complexity-based | Exact request |

**DEPTH Definition:**
DEPTH methodology (Discover, Engineer, Prototype, Test, Harmonize) is automatically applied to ensure quality while maintaining output constraints. The system executes all 5 phases silently.

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

[DEPTH processing happens invisibly]
[Multiple perspectives analyze the SAME requirement]
[Output contains ONLY what was requested]
```

**Note:** Users never see methodology details or choose processing depth - the system handles everything automatically.

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

---

<a id="symbol--formatting-reference"></a>
## 🔍 Symbol & Formatting Reference

### Universal Symbol Hierarchy
| Level | Symbols | Purpose | Usage |
|-------|---------|---------|-------|
| **Header** | N/A | Mode metadata | First line always |
| **H1** | ☘, ■ | About, Main sections | Primary structure |
| **H2** | ◻, ✦, ⌥, ✓, ∅ | Subsections, special elements | Secondary structure |
| **H3** | Clean | Detail headers | No symbols |
| **H4** | Clean | Detail headers | No symbols |

### Universal Formatting Rules
- **Header Position**: Always first line of artifact
- **About Position**: Always FIRST major section (after header)
- **Success Position**: Always AFTER About section
- **Problems**: Integrated in About narrative
- **Lists**: Always use `-` for regular lists
- **Checkboxes**: Always use `[]` (no spaces)
- **Status Notes**: `[Status note: "description"]` (standardized format)
- **NO Table of Contents**: External tools handle navigation
- **Output Constraints**: Content = exactly what user requested

---

<a id="header-format"></a>
## 📊 Header Format

### Streamlined Header (Standard)
All artifacts begin with a single-line header as the first line:

```markdown
Mode: $[mode] | [Complexity/Scale]: [level] | Template: v0.xxx
---
[Main content begins here - ONLY what user requested]
```

### Header Benefits
- **Immediate Clarity**: Know artifact type at a glance
- **Processing Transparency**: Shows DEPTH was applied
- **Version Tracking**: Template compliance noted
- **Clean Separation**: Divider separates metadata from content

---

<a id="troubleshooting"></a>
## 🆘 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| **System answering own questions** | Critical error - should wait for user |
| **Multiple questions asked** | Should be single comprehensive question |
| **Extra features in output** | Output must match exact request |
| **DEPTH details shown to user** | Processing should be silent |
| **Wrong terminology (ultrathink)** | Should use "DEPTH methodology" |
| **Missing WAIT markers** | Must have explicit wait instructions |
| **Scope expansion** | Template scaling affects structure, not content |
| **Header at bottom** | Move to top as first line |
| **Success criteria at top** | Move to AFTER About section |
| **Problems listed separately** | Integrate into About narrative |

### Critical Principles
**System MUST:**
- NEVER answer own questions
- ALWAYS wait for complete user response
- Apply DEPTH silently (hide methodology)
- Deliver EXACTLY what was requested
- Use single comprehensive question format

### REPAIR Framework for Errors
- **R**ecognize - Identify issue
- **E**xplain - Clear description
- **P**ropose - Multiple solutions
- **A**dapt - Apply chosen fix
- **I**terate - Test and confirm
- **R**ecord - Learn for future

---

<a id="version-history"></a>
## 📦 Version History

### v0.910 (Latest - DEPTH Framework Alignment)
**Date:** Current
**Type:** Major framework update and terminology alignment

**What Changed:**
1. **DEPTH Terminology** - Replaced all "ultrathink" references with DEPTH methodology
2. **Interactive Format** - Fixed to single comprehensive question with WAIT markers
3. **Silent Processing** - Enhanced emphasis on hidden complexity
4. **Output Constraints** - Strengthened "exact request = exact output" enforcement
5. **Critical Rules** - NEVER answer own questions, ALWAYS wait for user
6. **Template Updates** - All 4 template files aligned with new framework

**Key Improvements:**
- Multiple perspectives analyze SAME requirement
- Various approaches considered for SAME deliverable
- Single output matching exact request
- No scope expansion beyond user's request
- Processing methodology completely hidden from users

**Files Updated:** 
- Artifact Standards (v0.147)
- Doc Mode (v0.117)
- PRD Mode (v0.128)
- Ticket Mode (v0.128)

**New Framework:** DEPTH Thinking Framework v0.100 (replaces ATLAS)

### v0.907.1
**Date:** Previous
**Type:** System refinement and bug fixes

**What Was Fixed:**
- Cleaner output (removed thinking announcements)
- Smarter template selection with tie-breaking
- Expanded error scenarios (8→12)
- Standardized status note format
- Clear Risks symbol criteria
- Input validation framework

### v0.907
- Header at top positioning
- System metadata first line of artifact
- Enhanced artifact organization

### v0.905
- Single comprehensive question flow
- 60% reduction in decision points
- 50% faster to artifact creation

### v0.903
- Minimal footer implementation
- 80% footer size reduction
- Cleaner artifact output

### v0.902
- Automatic processing (10 rounds enforced)
- Quick mode auto-scaling (1-5 rounds)
- Success repositioned after About

---

## 🎯 Quick Command Reference

### Standard Commands
```markdown
$ticket [request]    # Create ticket with 10-round DEPTH
$prd [request]       # Create PRD with 10-round DEPTH
$doc [request]       # Create documentation with 10-round DEPTH
$story [request]     # Create user story (no checklist)
```

### Speed Command
```markdown
$quick [request]     # Immediate creation, 1-5 rounds auto-scaled
```

### Default Behavior
```markdown
[any request without command]    # Interactive mode with single comprehensive question
```

---

## 📚 Core Principles Summary

### DEPTH Processing Guarantee
```
User Request: "Build auth system"
↓
Internal DEPTH Analysis:
- 5 perspectives analyze the SAME auth system
- 8 approaches considered for the SAME auth system
- Quality optimized for the SAME auth system
↓
Output: ONE auth system deliverable
- Exactly what user requested
- No additional features
- No scope expansion
- Perfect template format
```

### Best Practices
- Use $quick for speed, Interactive for customization
- Provide complete response to single comprehensive question
- Trust automatic complexity detection
- Let system handle DEPTH processing silently
- Expect output to match request exactly