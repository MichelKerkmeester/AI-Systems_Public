# Product Owner System - User Guide v0.900

Transforms requests into professional development tickets, strategic PRDs, and documentation through intelligent interactive guidance with built-in complexity challenging.

## 📋 Table of Contents

- [🆕 What's New In V0.900](#whats-new-in-v0900)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🎫 Ticket Mode](#ticket-mode)
- [🚀 PRD Mode](#prd-mode)
- [📄 Doc Mode](#doc-mode)
- [🧠 Atlas Thinking Framework](#atlas-thinking-framework)
- [🎯 Automatic Complexity Detection](#automatic-complexity-detection)
- [💡 Challenge Mode](#challenge-mode)
- [📝 Symbol & Formatting Reference](#symbol--formatting-reference)
- [🆘 Troubleshooting](#troubleshooting)
- [📦 Version History](#version-history)

.

<a id="whats-new-in-v0900"></a>
## 🆕 What's New In V0.900

### Critical Updates
- **Template Alignment v0.xxx:** Full compliance with latest ticket, PRD, and doc templates
- **Symbol Hierarchy Refined:** H1 (⌘/❖), H2 (◻︎/✦/⌥/✔/⌥/∅), H3 (clean - no symbols)
- **Success Position Enforcement:** Metrics/criteria always at top after title
- **Problem Integration:** Issues woven into About narrative, never listed separately
- **Enhanced Scaling:** Precise complexity detection for tickets (2-3/4-5/6-8), PRDs (5-10/10-20/20+), docs (2-3/4-6/7+)

### Quality Improvements
- Table format mandatory for Designs & References
- Dividers (---) required between all sections
- Checkbox format `[]` without spaces universally
- Status notes format: `[Status note: "X% complete"]`
- Placeholder links: `[Figma - to be added]`

.

<a id="key-features"></a>
## ✨ Key Features

- **🚀 Three Modes**: PRD's, Stories, Tickets & Documentation
- **🧠 ATLAS Framework**: 5-phase thinking methodology with mode-specific adaptations
- **🎯 Smart Complexity**: Automatic detection and template scaling
- **💡 Challenge Mode**: Three-level hierarchy with calibration
- **🚨 REPAIR Protocol**: Structured error recovery
- **📊 Thinking Calibration**: Formula-based recommendations (6-10 rounds)

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
3. Copy and paste: `Writer - Product Owner.md` (v0.301)
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project:

**Core Documents (Latest Versions):**
- `Product Owner - ATLAS Thinking Framework.md` (v0.301)
- `Product Owner - Artifact Standards.md` (v0.301)
- `Product Owner - Interactive Mode.md` (v0.301)

**Template Documents (Current Versions):**
- `Product Owner - Template - Ticket Mode.md` (v0.200)
- `Product Owner - Template - PRD Mode.md` (v0.201)
- `Product Owner - Template - Doc Mode.md` (v0.201)

### Step 4: Start Creating
```
need user authentication         # Interactive discovery flow
$quick auth PRD                 # Immediate PRD creation
$prd payment platform           # Direct PRD mode
$ticket payment integration     # Direct ticket mode
```

.

<a id="operating-modes"></a>
## 🎛️ Operating Modes

**Default Mode:** The system defaults to `$interactive` unless specified.

| Mode | Purpose | Questions | Scaling | Symbol System |
|------|---------|-----------|---------|---------------|
| **Interactive** | Determine what to create | 3-4 adaptive | Auto-detect | Mode-specific |
| **$quick** | Fast creation | NONE | Auto-scale | Mode-appropriate |
| **$ticket** | Dev tickets | 3 questions | 2-3/4-5/6-8 sections | ⌘, ❖, ◻︎, ✦, ⌥, ✔ |
| **$prd** | Product requirements | 3-4 questions | 5-10/10-20/20+ features | ⌘, ❖, ✦, ◻︎, ⌥, ∅ |
| **$ticket or $story** | Dev tickets/stories | 3 questions | 2-3/4-5/6-8 sections | ⌘, ❖, ◻︎, ✦, ⌥, ✔ |
| **$doc** | Documentation | 3 questions | 2-3/4-6/7+ sections | ⌘, ❖, ◻︎, ⌥ |

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
Creating your payments initiative PRD immediately...
- Initiative level detected (5-10 features)
- No questions asked
- Success metrics at top
- Maximum speed delivery

[CREATES ARTIFACT IMMEDIATELY]
```

**$Quick Mode Characteristics:**
- NO thinking rounds question - Always uses 6
- NO challenge presentation - Skips regardless
- NO additional questions - Proceeds immediately
- Works with all modes - Tickets, PRDs, and docs
- Auto-scales to detected complexity
- Uses mode-appropriate formatting automatically

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

### Ticket Complexity Levels (v0.200)
| Type | Sections | Resolution Items | Triggers |
|------|----------|------------------|----------|
| **Simple** | 2-3 | 4-6 items | bug, fix, typo, update |
| **Standard** | 4-5 | 8-12 items | feature, dashboard, api |
| **Complex** | 6-8 with phases | 12-20 items | platform, architecture, migration |

### Ticket Structure & Symbols
- **⌘ About**: Context and background (H1)
- **❖ Requirements**: Main sections (H1)
- **◻︎ Functional/Technical**: Sub-sections (H2)
- **✦ Success Criteria**: At top after title (H2)
- **⌥ Designs & References**: Table format (H2)
- **✔ Resolution Checklist**: Scaled items (H2)
- Clean H3 headers (no symbols)

### List Formatting
```markdown
### ◻︎ Functional Requirements

- First requirement    ✔ (use hyphen for lists)
- Second requirement   ✔

## ✔ Resolution Checklist

[] First item         ✔ (no space in brackets)
[] Second item        ✔
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

### PRD Complexity Levels (v0.201)
| Level | Features | Sections | Timeline | Focus |
|-------|----------|----------|----------|-------|
| **Initiative** | 5-10 | 5-7 | Quarterly | Single-team scope |
| **Program** | 10-20 | 8-10 | Half-year | Multi-team coordination |
| **Strategic** | 20+ | 10+ | Annual | Company-wide platform |

### PRD Structure & Symbols
- **✦ Success Metrics**: At top immediately (H2)
- **⌘ About**: Strategic overview (H1)
- **❖ Scope & Features**: Main sections (H1)
- **◻︎ Feature Details**: Sub-sections (H2)
- **⌥ Designs & References**: Table format (H2)
- **∅ Risks & Mitigations**: When applicable (H2)
- Clean H3 headers (no symbols)

### PRD-Specific Formatting
```markdown
## ✦ Success Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| MAU | 250K | 500K | Q2 2025 |

---

# ⌘ About

[Strategic context with integrated problems and opportunities]
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

### Documentation Types (v0.201)
| Type | Sections | Depth | Format |
|------|----------|-------|--------|
| **Simple** | 2-3 | Quick reference | Essential info |
| **Standard** | 4-6 | Detailed guide | Complete coverage |
| **Complex** | 7+ | Comprehensive | Strategic depth |

### Doc Structure & Symbols
- **⌘ About**: Document overview (H1)
- **❖ Main Sections**: Primary content (H1)
- **◻︎ Subsections**: Secondary content (H2)
- **⌥ References & Resources**: Table format (H2)
- Clean H3 headers (no symbols)
- **`---`**: Major section separators

### Critical Doc Formatting
**Correct Structure:**
```markdown
# ⌘ About

[Purpose and context integrated]

---

## ⌥ References & Resources

| Type | Resource | Status | Link |
|------|----------|--------|------|
| API | Documentation | Current | [Link - to be added] |

---

# ❖ Implementation Guide
```

.

<a id="atlas-thinking-framework"></a>
## 🧠 Atlas Thinking Framework

### User Control Points
| Phase | Purpose | Focus Areas |
|-------|---------|-------------|
| **A** | Assess Reality | Problem integration into narrative |
| **T** | Transform Solutions | Mode-specific approaches |
| **L** | Layer Framework | Template compliance |
| **A** | Assess Impact | Validation against templates |
| **S** | Synthesize & Ship | Format verification |

### Thinking Round Calibration
```
How many thinking rounds should I use? (6-10)

Based on your request, I recommend: [X rounds]
- Complexity: [Low/Medium/High]
- Uncertainty: [Low/Medium/High]
- Stakes: [Low/Medium/High]

[Historical note: You typically use Y rounds]

Your choice?
```

### Phase Application By Rounds
| Rounds | Phases | Use Case |
|--------|--------|----------|
| 6 | A→T→L→S | Standard depth, $quick default |
| 7 | A→T→L→A→S | Standard tickets/PRDs/docs |
| 8-9 | Full Atlas+ | Complex features/programs |
| 10 | Deep Atlas | Strategic analysis/PRDs |

.

<a id="automatic-complexity-detection"></a>
## 🎯 Automatic Complexity Detection

### For Tickets
| Indicators | Complexity | Sections | Resolution Items |
|------------|------------|----------|------------------|
| bug, fix, typo, update | **Simple** | 2-3 | 4-6 |
| feature, dashboard, api | **Standard** | 4-5 | 8-12 |
| platform, architecture, migration | **Complex** | 6-8 | 12-20 |

### For PRDs 
| Indicators | Complexity | Features | Timeline |
|------------|------------|----------|----------|
| initiative, quarterly | **Initiative** | 5-10 | 3 months |
| program, multi-team | **Program** | 10-20 | 6 months |
| strategic, platform | **Strategic** | 20+ | 12+ months |

### For Docs
| Indicators | Complexity | Sections | Focus |
|------------|------------|----------|-------|
| overview, brief, summary | **Simple** | 2-3 | Quick reference |
| guide, specification | **Standard** | 4-6 | Detailed guidance |
| platform, ecosystem, strategy | **Complex** | 7+ | Comprehensive |

**Note:** In $quick mode, complexity is detected and auto-scaled without user interaction.

.

<a id="challenge-mode"></a>
## 💡 Challenge Mode

### Three-Level Hierarchy (6+ Rounds)

**Level 1: Constructive (6-7 rounds)**
- Proposes meaningful alternatives
- Questions scope boundaries
- **WAITS for user decision**

**Level 2: Strong (8-10 rounds)**
- Challenges core assumptions
- Proposes radical simplification
- **WAITS for user decision**

### Example Challenges
```
"This PRD spans multiple quarters. Should we:
- Phase it into quarterly initiatives?
- Focus on highest-impact features first?
- Keep the full strategic scope?"

[WAIT FOR USER RESPONSE]
```

**$Quick Mode Exception:** Never presents challenges regardless of complexity

.

<a id="symbol--formatting-reference"></a>
## 📝 Symbol & Formatting Reference

### Universal Symbol Hierarchy (v0.200-201)
| Level | Symbols | Purpose | Usage |
|-------|---------|---------|-------|
| **H1** | ⌘, ❖ | About, Main sections | Primary structure |
| **H2** | ◻︎, ✦, ⌥, ✔, ⌥, ∅ | Subsections, special elements | Secondary structure |
| **H3** | Clean | Detail headers | No symbols |

### Mode-Specific Symbols

**Ticket Mode (v0.200):**
- ⌘ About (H1)
- ❖ Requirements/Main sections (H1)
- ◻︎ Subsections (H2)
- ✦ Success Criteria (H2)
- ⌥ Designs & References (H2)
- ✔ Resolution Checklist (H2)

**PRD Mode (v0.201):**
- ✦ Success Metrics (H2, at top)
- ⌘ About (H1)
- ❖ Main sections (H1)
- ◻︎ Subsections (H2)
- ⌥ Designs & References (H2)
- ∅ Risks & Mitigations (H2)

**Doc Mode (v0.201):**
- ⌘ About (H1)
- ❖ Main sections (H1)
- ◻︎ Subsections (H2)
- ⌥ References & Resources (H2)
- `---` Section separators

### Universal Formatting Rules
- **Success Position**: Always at top after title
- **Problems**: Integrated in About narrative
- **Lists**: Always use `-` for regular lists
- **Checkboxes**: Always use `[]` (no spaces)
- **Tables**: Required for Designs & References
- **Dividers**: `---` between all major sections
- **Placeholders**: `[Figma - to be added]`
- **Status Notes**: `[Status note: "description"]`

.

<a id="troubleshooting"></a>
## 🆘 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| **Wrong symbols appearing** | Check mode - H1: ⌘/❖, H2: various, H3: clean |
| **Success criteria buried** | Must be at top immediately after title |
| **Problems listed separately** | Integrate into About narrative |
| **Wrong complexity** | Check keywords for auto-scaling triggers |
| **Checkbox format wrong** | Use `[]` without spaces |
| **Missing dividers** | Add `---` between all sections |
| **Want speed** | Use $quick mode for auto-scaling |
| **Confused context** | Use $reset |

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

### v0.900 (Current)
- Full template alignment (v0.200-201)
- Symbol hierarchy enforcement
- Success position mandatory at top
- Problem integration in narratives
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

*Template-compliant formatting ensures professional output. Symbols: H1 (⌘/❖), H2 (◻︎/✦/⌥/✔/⌥/∅), H3 (clean). Revolutionary $quick mode for immediate creation with auto-scaling. Interactive Mode remains the thoughtful default. Choose $quick when speed matters, Interactive when customization matters. Success always at top. Problems always integrated. User autonomy is absolute.*