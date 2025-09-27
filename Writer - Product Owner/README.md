# Product Owner System - User Guide v0.903

Transforms requests into professional development tickets, strategic PRDs, and documentation through intelligent interactive guidance with automatic ultrathink processing.

## 📋 Table of Contents

- [🆕 What's New In V0.903](#whats-new-in-v0903)
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

<a id="whats-new-in-v0903"></a>
## 🆕 What's New In V0.903

### Streamlined Footer Implementation
- **Minimal Footer:** Single-line format replacing verbose AI System section
- **80% Size Reduction:** From 15-20 lines to just 1 line
- **Essential Tracking:** Mode, Complexity/Scale, Template version preserved
- **Clean Output:** Significantly reduced visual clutter in artifacts

### Core Updates from V0.902
- **Automatic Ultrathink™:** 10 rounds enforced for all standard operations - no user choice
- **Quick Mode Auto-Scaling:** 1-5 rounds automatically determined by complexity
- **Success Repositioning:** Criteria/metrics now AFTER About section for better flow
- **No Table of Contents:** Removed - external tools (ClickUp/Jira) handle navigation
- **Problem Integration Enforced:** Always woven into About narrative, never listed
- **Template Compliance:** Full v0.xxx standards

### Streamlined Experience
- No thinking round questions - system decides automatically
- Simplified interaction - focus only on content decisions
- Faster creation - 30% reduction in decision points
- Consistent quality - guaranteed depth analysis
- Professional output - 100% template compliance
- Clean minimal footer - essential info only

.

<a id="key-features"></a>
## ✨ Key Features

- **🚀 Three Modes**: PRDs, Stories, Tickets & Documentation
- **🧠 ATLAS Framework**: 5-phase methodology with automatic ultrathink
- **🎯 Smart Complexity**: Automatic detection and template scaling
- **⚡ Quick Mode**: Zero-wait creation with auto-scaled thinking (1-5 rounds)
- **🚨 REPAIR Protocol**: Structured error recovery
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
3. Copy and paste: `Writer - Product Owner - v0.902.md` 
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project (all updated with minimal footer):

**Core Documents (Latest Versions):**
- `Product Owner - ATLAS Thinking Framework - v0.182.md` 
- `Product Owner - Artifact Standards - v0.141.md` 
- `Product Owner - Interactive Mode - v0.282.md` 

**Template Documents (Current Versions):**
- `Product Owner - Template - Ticket Mode - v0.121.md` 
- `Product Owner - Template - PRD Mode - v0.121.md` 
- `Product Owner - Template - Doc Mode - v0.111.md` 

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
| **Interactive** | Determine what to create | 2-3 adaptive | 10 rounds auto | Auto-detect | Minimal |
| **$quick** | Fast creation | NONE | 1-5 auto-scaled | Auto-scale | Minimal |
| **$ticket** | Dev tickets | 3 questions | 10 rounds auto | 2-3/4-5/6-8 sections | Minimal |
| **$prd** | Product requirements | 3-4 questions | 10 rounds auto | 5-10/10-20/20+ features | Minimal |
| **$story** | User stories | 3 questions | 10 rounds auto | 2-3/4-5/6-8 sections | Minimal |
| **$doc** | Documentation | 3 questions | 10 rounds auto | 2-3/4-6/7+ sections | Minimal |

### Interactive Flow (Default)
```
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket - Feature or bug for developers
2. User story - Narrative format without checklist
3. PRD (Product Requirements) - Strategic initiative or detailed specs
4. Product documentation - User guide, feature docs, or strategy

Which best fits? (1-4)
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
[Footer: Mode: $quick | Scale: Initiative | Template: v0.121]
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

### Development Ticket Creation
```
User: $ticket payment integration

System: Let's create your payment integration ticket! 🎯

**Question 1: Is this a ticket or story?**
- Ticket = includes resolution checklist for QA
- Story = narrative format without checklist

Your choice?
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
- **Minimal Footer**: `Mode: $ticket | Complexity: [level] | Template: v0.121`

### Example Ticket Footer
```markdown
[Ticket content...]
---
Mode: $ticket | Complexity: Standard | Template: v0.121
```

.

<a id="prd-mode"></a>
## 🚀 PRD Mode

### Product Requirements Document Creation
```
User: $prd authentication platform

System: Let's structure your authentication platform PRD! 🚀

**Question 1: What type of PRD do you need?**
- Initiative (5-10 features, single team, quarterly)
- Program (10-20 features, multi-team, half-year)
- Strategic (20+ features, company-wide, annual)

Your choice?
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
- **Minimal Footer**: `Mode: $prd | Scale: [level] | Template: v0.121`

### Example PRD Footer
```markdown
[PRD content...]
---
Mode: $prd | Scale: Initiative | Template: v0.121
```

.

<a id="doc-mode"></a>
## 📄 Doc Mode

### Documentation Creation
```
User: $doc API guide

System: Let's create your API documentation! 📚

**Question 1: What type of documentation?**
- Product brief (quick overview)
- Feature specification (detailed design)
- Performance tracking (metrics & KPIs)
- Strategy document (comprehensive guide)

Your choice?
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
- **Minimal Footer**: `Mode: $doc | Complexity: [level] | Template: v0.111`

### Example Doc Footer
```markdown
[Documentation content...]
---
Mode: $doc | Complexity: Complex | Template: v0.111
```

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

**Note:** Users are never asked about thinking rounds - the system determines optimal depth automatically based on mode and complexity. The minimal footer documents the mode and complexity without verbose process details.

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
- **Placeholders**: `[Figma - to be added]`
- **Status Notes**: `[Status note: "description"]`
- **NO Table of Contents**: External tools handle navigation
- **Minimal Footer**: Single line at bottom

.

<a id="minimal-footer-format"></a>
## 📊 Minimal Footer Format

### New Streamlined Footer (v0.903)
All artifacts now include a single-line footer with essential tracking information:

```markdown
Mode: $[mode] | [Complexity/Scale]: [level] | Template: v0.xxx
```

### Footer Examples by Mode

**Ticket Mode:**
```markdown
Mode: $ticket | Complexity: Standard | Template: v0.121
```

**Story Mode:**
```markdown
Mode: $story | Complexity: Simple | Template: v0.121
```

**PRD Mode:**
```markdown
Mode: $prd | Scale: Initiative | Template: v0.121
```

**Doc Mode:**
```markdown
Mode: $doc | Complexity: Complex | Template: v0.111
```

**Quick Mode:**
```markdown
Mode: $quick | Complexity: Auto | Template: v0.xxx
```

### What Changed from v0.902

**Old Footer (REMOVED):**
- 15-20 lines of verbose process documentation
- Detailed thinking rounds and ATLAS phases
- Historical context and session learning
- Extensive framework documentation

**New Footer (CURRENT):**
- Single line with essential info only
- Mode identification
- Complexity/Scale level
- Template version for compliance
- **80% size reduction**
- **100% cleaner output**

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
| **Asked about thinking rounds** | System error - thinking is automatic |
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

### v0.903 (Current)
- **NEW: Minimal footer implementation**
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
[any request without command]    # Interactive mode with discovery flow
```

---

*Template-compliant formatting ensures professional output. Automatic ultrathink guarantees consistent depth. Minimal footer provides essential tracking without clutter. Symbols: H1 (⌘/■), H2 (◻️/✦/⌥/✓/⌥/∅), H3 (clean), H4 (clean). Revolutionary $quick mode for immediate creation with auto-scaled thinking (1-5 rounds). Interactive Mode remains the thoughtful default with 10-round ultrathink. Choose $quick when speed matters, Interactive when customization matters. About always first. Success always after About. Problems always integrated. System thinking is automatic - user control over content remains absolute. Footer always minimal.*