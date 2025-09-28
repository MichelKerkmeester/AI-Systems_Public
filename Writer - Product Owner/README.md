# Product Owner System - User Guide v0.904

Transforms requests into professional development tickets, strategic PRDs, and documentation through intelligent interactive guidance with automatic ultrathink processing.

## 📋 Table of Contents

- [🆕 What's New In V0.904](#whats-new-in-v0904)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🎫 Ticket Mode](#ticket-mode)
- [🚀 PRD Mode](#prd-mode)
- [📄 Doc Mode](#doc-mode)
- [🧠 Atlas Thinking Framework](#atlas-thinking-framework)
- [🎯 Automatic Complexity Detection](#automatic-complexity-detection)
- [📝 Symbol & Formatting Reference](#symbol--formatting-reference)
- [📊 Minimal Footer Format](#minimal-footer-format)
- [🆘 Troubleshooting](#troubleshooting)
- [📦 Version History](#version-history)

.

<a id="whats-new-in-v0904"></a>
## 🆕 What's New In V0.904

### Single Comprehensive Question Flow
- **Consolidated Interaction:** All information gathered in ONE well-formatted prompt
- **60% Fewer Decision Points:** From 3-4 questions to just 1
- **Faster Creation:** 50% reduction in time to artifact
- **Enhanced Formatting:** Numbered sections with emojis for clarity
- **No Figma Dependencies:** Removed all Figma MCP references

### Enhanced User Experience
- **Single Wait Point:** Ask once, wait once, create
- **Clear Response Format:** Examples provided for user input
- **Better Visual Hierarchy:** Numbered points (1️⃣, 2️⃣, 3️⃣)
- **Streamlined Process:** Parse → Process → Create

### Maintained from V0.903
- **Automatic Ultrathink™:** 10 rounds enforced for all standard operations
- **Quick Mode Auto-Scaling:** 1-5 rounds automatically determined
- **Minimal Footer:** Single-line tracking format
- **Template Compliance:** Full v0.xxx standards
- **Success Positioning:** Criteria/metrics after About section

.

<a id="key-features"></a>
## ✨ Key Features

- **🚀 Three Modes**: PRDs, Stories, Tickets & Documentation
- **🧠 ATLAS Framework**: 5-phase methodology with automatic ultrathink
- **🎯 Smart Complexity**: Automatic detection and template scaling
- **⚡ Quick Mode**: Zero-wait creation with auto-scaled thinking (1-5 rounds)
- **💬 Single Question Flow**: All information gathered at once
- **🤖 Automatic Thinking**: System-controlled depth (no user choice)
- **📊 Minimal Footer**: Clean single-line tracking format

.

<a id="quick-setup"></a>
## 🚀 Quick Setup

### Step 1: Create A Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Product Owner"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Product Owner - v0.904.md` 
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project (all updated with single question flow):

**Core Documents (Latest Versions):**
- `Product Owner - ATLAS Thinking Framework - v0.184.md` 
- `Product Owner - Artifact Standards - v0.143.md` 
- `Product Owner - Interactive Mode - v0.284.md` 

**Template Documents (Current Versions):**
- `Product Owner - Template - Ticket Mode - v0.123.md` 
- `Product Owner - Template - PRD Mode - v0.123.md` 
- `Product Owner - Template - Doc Mode - v0.113.md` 

### Step 4: Start Creating
```
need user authentication         # Interactive discovery flow
$quick auth PRD                 # Immediate PRD creation (1-5 rounds auto)
$prd payment platform           # Direct PRD mode (10 rounds auto)
$ticket payment integration     # Direct ticket mode (10 rounds auto)
```

.

<a id="operating-modes"></a>
## 🎛️ Operating Modes

**Default Mode:** The system defaults to `$interactive` with automatic 10-round ultrathink unless specified.

| Mode | Purpose | Questions | Thinking | Scaling | Footer Format |
|------|---------|-----------|----------|---------|---------------|
| **Interactive** | Determine what to create | 1 comprehensive | 10 rounds auto | Auto-detect | Minimal |
| **$quick** | Fast creation | NONE | 1-5 auto-scaled | Auto-scale | Minimal |
| **$ticket** | Dev tickets | 1 comprehensive | 10 rounds auto | 2-3/4-5/6-8 sections | Minimal |
| **$prd** | Product requirements | 1 comprehensive | 10 rounds auto | 5-10/10-20/20+ features | Minimal |
| **$story** | User stories | 1 comprehensive | 10 rounds auto | 2-3/4-5/6-8 sections | Minimal |
| **$doc** | Documentation | 1 comprehensive | 10 rounds auto | 2-3/4-6/7+ sections | Minimal |

### Interactive Flow (Default) - NEW Single Question Format
```
Welcome! Let's create exactly what you need. 🎯

Please provide the following information:

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

Please respond with your choices (e.g., "1. Ticket, 2. BE, 3. User authentication system")

[SYSTEM WAITS FOR SINGLE RESPONSE]
```

### $Quick Mode - Zero-Wait Creation
```
User: $quick - Q1 payments initiative

System: **Quick Mode Activated** ⚡

Auto-Configuration:
- Complexity: Initiative level detected
- Applying: 3 rounds (optimized for speed)
- No questions asked
- Maximum speed delivery

[CREATES ARTIFACT IMMEDIATELY]
[Footer: Mode: $quick | Scale: Initiative | Template: v0.123]
```

**$Quick Mode Characteristics:**
- NO questions whatsoever - Proceeds immediately
- Auto-scaled thinking - 1-5 rounds based on complexity
- Auto-detect type and scale - Smart complexity detection
- Works with all modes - Tickets, PRDs, and docs
- Template compliant - Proper formatting guaranteed
- Minimal footer - Single-line tracking

.

<a id="ticket-mode"></a>
## 🎫 Ticket Mode

### Development Ticket Creation - NEW Single Question Format
```
User: $ticket payment integration

System: Let me help you create your payment integration ticket. 🎯

Please provide the following details:

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

Please respond with all information (e.g., "1. Ticket, 2. BE, 3. Stripe API integration for subscriptions")

[SYSTEM WAITS FOR SINGLE RESPONSE]
```

### Ticket Complexity Levels
| Type | Sections | Resolution Items | Triggers |
|------|----------|------------------|----------|
| **Simple** | 2-3 | 4-6 items | bug, fix, typo, update |
| **Standard** | 4-5 | 8-12 items | feature, dashboard, api |
| **Complex** | 6-8 with phases | 12-20 items | platform, architecture, migration |

### Ticket Structure & Symbols
- **⌘ About**: Context with integrated problems (H1, FIRST)
- **✦ Success Criteria**: Measurable outcomes (H2, AFTER About)
- **⌥ Designs & References**: Table format (H2)
- **■ Requirements**: Main sections (H1)
- **◻️ Functional/Technical**: Sub-sections (H2)
- **✓ Resolution Checklist**: Scaled items (H2)
- Clean H3 headers (no symbols)
- **Minimal Footer**: `Mode: $ticket | Complexity: [level] | Template: v0.123`

.

<a id="prd-mode"></a>
## 🚀 PRD Mode

### Product Requirements Document Creation - NEW Single Question Format
```
User: $prd authentication platform

System: Let's create your authentication platform PRD! 📋

Please provide the following information:

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

Please respond with all details (e.g., "1. Initiative PRD, 2. Web + Mobile, 3. Real-time analytics for enterprise customers")

[SYSTEM WAITS FOR SINGLE RESPONSE]
```

### PRD Complexity Levels
| Level | Features | Sections | Timeline | Focus |
|-------|----------|----------|----------|-------|
| **Initiative** | 5-10 | 5-7 | Quarterly | Single-team scope |
| **Program** | 10-20 | 8-10 | Half-year | Multi-team coordination |
| **Strategic** | 20+ | 10+ | Annual | Company-wide platform |

### PRD Structure & Symbols
- **⌘ About**: Strategic context (H1, FIRST)
- **✦ Success Metrics**: Business/product metrics (H2, AFTER About)
- **⌥ Designs & References**: Table format (H2)
- **■ Scope & Features**: Main sections (H1)
- **◻️ Feature Details**: Sub-sections (H2)
- **∅ Risks & Mitigations**: When applicable (H2)
- Clean H3 headers (no symbols)
- **Minimal Footer**: `Mode: $prd | Scale: [level] | Template: v0.123`

.

<a id="doc-mode"></a>
## 📄 Doc Mode

### Documentation Creation - NEW Single Question Format
```
User: $doc API guide

System: Let's create your documentation! 📚

Please provide the following details:

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

Please respond with all information (e.g., "1. Strategy document, 2. Complex, 3. Platform roadmap for executive team")

[SYSTEM WAITS FOR SINGLE RESPONSE]
```

### Documentation Types
| Type | Sections | Depth | Format |
|------|----------|-------|--------|
| **Simple** | 2-3 | Quick reference | Essential info |
| **Standard** | 4-6 | Detailed guide | Complete coverage |
| **Complex** | 7+ | Comprehensive | Strategic depth |

### Doc Structure & Symbols
- **⌘ About**: Purpose and context (H1, FIRST)
- **■ Main Sections**: Primary content (H1)
- **◻️ Subsections**: Secondary content (H2)
- **⌥ References & Resources**: Table format (H2)
- Clean H3 headers (no symbols)
- Clean H4 headers (no symbols)
- **`---`**: Major section separators
- **Minimal Footer**: `Mode: $doc | Complexity: [level] | Template: v0.113`

.

<a id="atlas-thinking-framework"></a>
## 🧠 Atlas Thinking Framework

### Automatic Ultrathink System
| Mode | Thinking Depth | User Choice | Application |
|------|----------------|-------------|-------------|
| **Standard Modes** | 10 rounds enforced | None | Automatic |
| **$Quick Mode** | 1-5 auto-scaled | None | Complexity-based |

### ATLAS Phases (Applied Automatically)
| Phase | Purpose | Focus Areas | Rounds |
|-------|---------|-------------|--------|
| **A** | Assess Reality | Problem integration | 1-2 (20%) |
| **T** | Transform Solutions | Mode-specific approaches | 3-5 (25%) |
| **L** | Layer Framework | Template compliance | 6-7 (25%) |
| **A** | Assess Impact | Validation | 8-9 (20%) |
| **S** | Synthesize & Ship | Format verification | 10 (10%) |

### Thinking Transparency
```markdown
🎯 Processing your request...

[Processing begins automatically with full depth]
```

**Note:** Users are never asked about thinking rounds - the system determines optimal depth automatically based on mode and complexity.

.

<a id="automatic-complexity-detection"></a>
## 🎯 Automatic Complexity Detection

### For Tickets
| Indicators | Complexity | Sections | Resolution Items | Thinking |
|------------|------------|----------|------------------|----------|
| bug, fix, typo, update | **Simple** | 2-3 | 4-6 | 10 rounds (2 if $quick) |
| feature, dashboard, api | **Standard** | 4-5 | 8-12 | 10 rounds (3 if $quick) |
| platform, architecture, migration | **Complex** | 6-8 | 12-20 | 10 rounds (5 if $quick) |

### For PRDs 
| Indicators | Complexity | Features | Timeline | Thinking |
|------------|------------|----------|----------|----------|
| initiative, quarterly | **Initiative** | 5-10 | 3 months | 10 rounds (3 if $quick) |
| program, multi-team | **Program** | 10-20 | 6 months | 10 rounds (4 if $quick) |
| strategic, platform | **Strategic** | 20+ | 12+ months | 10 rounds (5 if $quick) |

### For Docs
| Indicators | Complexity | Sections | Focus | Thinking |
|------------|------------|----------|-------|----------|
| overview, brief, summary | **Simple** | 2-3 | Quick reference | 10 rounds (2 if $quick) |
| guide, specification | **Standard** | 4-6 | Detailed guidance | 10 rounds (3 if $quick) |
| platform, ecosystem, strategy | **Complex** | 7+ | Comprehensive | 10 rounds (5 if $quick) |

**Note:** Complexity detection is automatic - the system analyzes keywords and context to apply appropriate scaling without user input.

.

<a id="symbol--formatting-reference"></a>
## 📝 Symbol & Formatting Reference

### Universal Symbol Hierarchy
| Level | Symbols | Purpose | Usage |
|-------|---------|---------|-------|
| **H1** | ⌘, ■ | About, Main sections | Primary structure |
| **H2** | ◻️, ✦, ⌥, ✓, ⌥, ∅ | Subsections, special elements | Secondary structure |
| **H3** | Clean | Detail headers | No symbols |
| **H4** | Clean | Detail headers | No symbols |

### Mode-Specific Symbols

**Ticket Mode:**
- ⌘ About (H1) - FIRST
- ✦ Success Criteria (H2) - AFTER About
- ⌥ Designs & References (H2)
- ■ Requirements/Main sections (H1)
- ◻️ Subsections (H2)
- ✓ Resolution Checklist (H2)

**PRD Mode:**
- ⌘ About (H1) - FIRST
- ✦ Success Metrics (H2) - AFTER About
- ⌥ Designs & References (H2)
- ■ Main sections (H1)
- ◻️ Subsections (H2)
- ∅ Risks & Mitigations (H2)

**Doc Mode:**
- ⌘ About (H1) - FIRST
- ■ Main sections (H1)
- ◻️ Subsections (H2)
- ⌥ References & Resources (H2)
- `---` Section separators

### Universal Formatting Rules
- **About Position**: Always FIRST major section
- **Success Position**: Always AFTER About section
- **Problems**: Integrated in About narrative
- **Lists**: Always use `-` for regular lists
- **Checkboxes**: Always use `[]` (no spaces)
- **Tables**: Required for Designs & References
- **Dividers**: `---` between all major sections
- **Placeholders**: `[Link - to be added]`
- **Status Notes**: `[Status note: "description"]`
- **NO Table of Contents**: External tools handle navigation
- **Minimal Footer**: Single line at bottom

.

<a id="minimal-footer-format"></a>
## 📊 Minimal Footer Format

### Streamlined Footer (Maintained from v0.903)
All artifacts include a single-line footer with essential tracking information:

```markdown
Mode: $[mode] | [Complexity/Scale]: [level] | Template: v0.xxx
```

### Footer Examples by Mode

**Ticket Mode:**
```markdown
Mode: $ticket | Complexity: Standard | Template: v0.123
```

**Story Mode:**
```markdown
Mode: $story | Complexity: Simple | Template: v0.123
```

**PRD Mode:**
```markdown
Mode: $prd | Scale: Initiative | Template: v0.123
```

**Doc Mode:**
```markdown
Mode: $doc | Complexity: Complex | Template: v0.113
```

**Quick Mode:**
```markdown
Mode: $quick | Complexity: Auto | Template: v0.xxx
```

.

<a id="troubleshooting"></a>
## 🆘 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| **Wrong symbols appearing** | Check mode - H1: ⌘/■, H2: various, H3: clean, H4: clean |
| **Success criteria at top** | Move to AFTER About section |
| **Problems listed separately** | Integrate into About narrative |
| **Wrong complexity** | Check keywords for auto-scaling triggers |
| **Checkbox format wrong** | Use `[]` without spaces |
| **Missing dividers** | Add `---` between all sections |
| **Want speed** | Use $quick mode (1-5 rounds auto) |
| **Multiple questions asked** | System error - should be single comprehensive question |
| **Verbose footer appearing** | Update to minimal format: Mode \| Complexity \| Template |
| **Missing footer** | Add single-line footer at bottom |

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

### v0.904 (Current)
- **NEW: Single comprehensive question flow**
- All information gathered in one interaction
- 60% reduction in decision points
- 50% faster to artifact creation
- Removed all Figma MCP dependencies
- Enhanced formatting with numbered sections
- Maintained all v0.903 improvements

### v0.903
- Minimal footer implementation
- Single-line footer format
- 80% footer size reduction
- Essential tracking preserved
- Cleaner artifact output
- All templates updated

### v0.902
- Automatic ultrathink (10 rounds enforced)
- Quick mode auto-scaling (1-5 rounds)
- Success repositioned after About
- No Table of Contents
- Problem integration mandatory
- Template v0.xxx compliance

### v0.900
- Full template alignment
- Symbol hierarchy enforcement
- Success position at top (now changed)
- Removed chat history integration

### v0.892
- PRD mode replaced Epic mode
- Enhanced feature specifications
- Improved doc formatting

### v0.850
- ATLAS framework integration
- Challenge mode implementation
- Past chats tool usage

---

## 🎯 Quick Command Reference

### Standard Commands
```markdown
$ticket [request]    # Create ticket with 10-round thinking
$prd [request]       # Create PRD with 10-round thinking
$doc [request]       # Create documentation with 10-round thinking
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

*Template-compliant formatting ensures professional output. Automatic ultrathink guarantees consistent depth. Minimal footer provides essential tracking without clutter. Symbols: H1 (⌘/■), H2 (◻️/✦/⌥/✓/⌥/∅), H3 (clean), H4 (clean). Revolutionary $quick mode for immediate creation with auto-scaled thinking (1-5 rounds). Interactive Mode now uses single comprehensive question with 10-round ultrathink. Choose $quick when speed matters, Interactive when customization matters. About always first. Success always after About. Problems always integrated. System thinking is automatic - user control over content remains absolute. Footer always minimal. Single question flow reduces friction while maintaining quality.*