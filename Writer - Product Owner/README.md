# Product Owner System v0.920

Transforms requests into professional tickets, epics, and documentation with **concise transparent DEPTH processing**.

## 📋 Table of Contents

1. [🆕 What's New in v0.920](#1-whats-new-in-v0920)
2. [✨ Key Features](#2-key-features)
3. [🚀 Quick Setup](#3-quick-setup)
4. [🎛️ Operating Modes](#4-operating-modes)
5. [📋 Mode Details](#5-mode-details)
6. [🧠 DEPTH Thinking Framework](#6-depth-thinking-framework)
7. [🔬 Cognitive Rigor Techniques](#7-cognitive-rigor-techniques)
8. [⚙️ Automatic Complexity Detection](#8-automatic-complexity-detection)
9. [🏗️ System Architecture](#9-system-architecture)

---

<a id="1-whats-new-in-v0920"></a>
## 1. 🆕 What's New In V0.920

### Major Improvements

**Enhanced Readability & Alignment:**
- **Reduced excessive capitalization** in rules section for improved readability
- **Fixed Section 7 (Quick Reference)** to align with DEPTH v0.105 two-layer transparency model
- **Removed contradictory language** about "showing all rounds to users"
- **Emphasized concise transparency** throughout - full rigor internally, meaningful updates externally
- **Standardized formatting** to match template conventions

### Key Changes

**Improved Self-Contained Templates:**
- All templates now fully self-contained with embedded rules, quality checks, and formatting standards
- Ticket v0.133: Auto-scaling resolution checklists (4-6, 8-12, 12-20 items), mechanism-first validation
- Story v0.133: Narrative format with Given-When-Then criteria, no QA checklist (key differentiator)
- Epic v0.130: Three scale options (Initiative/Program/Strategic) with links to stories/tickets
- Doc v0.119: Three complexity levels with tool-agnostic design principles
- No external rule dependencies - complete error recovery protocols built-in


### Template Structure Now:
```
Knowledge Base/
├── Writer - Product Owner - v0.920.md (System Prompt)
├── Product Owner - DEPTH Thinking Framework - v0.105.md (Methodology)
├── Product Owner - Interactive Mode - v0.306.md (Conversation Flow)
│
├── Product Owner - Template - Ticket Mode - v0.133.md ← Improved self-contained
├── Product Owner - Template - Story Mode - v0.133.md ← Improved self-contained
├── Product Owner - Template - Epic Mode - v0.130.md ← Improved self-contained
└── Product Owner - Template - Doc Mode - v0.119.md ← Improved self-contained
```

**Template Improvements:**
- All formatting rules, quality checks, and standards embedded in each template
- No external dependencies or rule duplication
- Auto-complexity scaling with clear indicators
- Complete error recovery protocols built-in

### 📊 Evolution: v0.913 → v0.914 → v0.915 → v0.920

**v0.913:** Initial multi-perspective framework  
**v0.914:** Two-layer transparency (concise + full rigor)  
**v0.915:** Template separation (dedicated story mode)  
**v0.920:** Readability improvements and transparency model alignment

**Result:** Professional quality + concise transparency + clear separation of concerns

---

<a id="2-key-features"></a>
## 2. ✨ Key Features

- **📋 Improved Self-Contained Templates**: All rules, quality checks, and formatting embedded (v0.133 Ticket/Story, v0.130 Epic, v0.119 Doc)
- **🧠 DEPTH Framework v0.105**: 10-round methodology with two-layer transparency
- **🔒 Mandatory Perspectives**: Minimum 3 perspectives (BLOCKING requirement)
- **🔬 Cognitive Rigor**: 5 techniques (multi-perspective, assumption audit, perspective inversion, constraint reversal, mechanism-first)
- **📊 Two-Layer Model**: Full rigor internally, concise updates externally
- **🚀 Four Modes**: Tickets, Stories, Epics, Documentation
- **⚡ Quick Mode**: Auto-scaled 1-5 rounds
- **💬 Single Question**: All info gathered at once
- **🎯 Auto-Complexity**: Smart detection and scaling

---

<a id="3-quick-setup"></a>
## 3. 🚀 Quick Setup

### Step 1: Create Claude Project
1. Go to claude.ai → Projects → Create "Product Owner"

### Step 2: Add System Instructions
1. Edit project details → Custom instructions
3. Copy and paste: `Writer - Product Owner - v0.920.md` 
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project:

**Core Framework:**
- `Product Owner - DEPTH Thinking Framework - v0.105.md` (two-layer transparency & mandatory perspectives)
- `Product Owner - Interactive Mode - v0.306.md` (conversation flow & smart routing)

**Improved Self-Contained Templates:**
Each template is fully self-contained with embedded rules, quality checks, and formatting standards:

- **`Product Owner - Template - Ticket Mode - v0.133.md`**
  - Development tickets with detailed QA Resolution Checklists
  - Auto-scaling: Simple (4-6 items), Standard (8-12), Complex (12-20)
  - Includes mechanism-first validation and scope discipline
  
- **`Product Owner - Template - Story Mode - v0.133.md`**
  - User stories in narrative format (no QA checklist)
  - Focus on user journey and business value
  - Given-When-Then acceptance criteria
  
- **`Product Owner - Template - Epic Mode - v0.130.md`**
  - High-level summaries with links to stories/tickets
  - Scale options: Initiative (5-10), Program (10-20), Strategic (20+)
  - Includes success metrics and implementation phases
  
- **`Product Owner - Template - Doc Mode - v0.119.md`**
  - Technical and user documentation
  - Complexity levels: Simple (2-3), Standard (4-6), Complex (7+)
  - Tool-agnostic design principles

**Key Advantages:**
- No external rule dependencies - everything embedded in each template
- Automatic complexity scaling based on request keywords
- Complete quality checklists and error recovery built-in
- Consistent DEPTH v0.105 integration across all templates

### Step 4: Start Creating
```
need user authentication        # Interactive discovery flow
$quick auth epic                # Immediate epic creation (1-5 rounds auto)
$epic payment platform          # Direct epic mode (10 rounds auto)
$ticket payment integration     # Direct ticket mode (10 rounds auto)
$story user login               # Direct story mode (10 rounds auto)
```

---

<a id="4-operating-modes"></a>
## 4. 🎛️ Operating Modes

**Default Mode:** The system defaults to `$interactive` with automatic 10-round DEPTH unless specified.

| Mode | Purpose | Questions | DEPTH Processing | Transparency | Template Version | Output |
|------|---------|-----------|------------------|--------------|------------------|---------|
| **Interactive** | Determine what to create | 1 comprehensive | 10 rounds (concise updates) | Two-layer | Auto-selected | Exact request |
| **$quick** | Fast creation | NONE | 1-5 auto-scaled | Summary | Auto-selected | Exact request |
| **$doc** | Documentation | 1 comprehensive | 10 rounds (concise updates) | Two-layer | v0.119 | Requested doc only |
| **$epic** | Epics | 1 comprehensive | 10 rounds (concise updates) | Two-layer | v0.130 | Requested epic only |
| **$story** | User stories | 1 comprehensive | 10 rounds (concise updates) | Two-layer | v0.133 | Requested story only |
| **$ticket** | Dev tickets | 1 comprehensive | 10 rounds (concise updates) | Two-layer | v0.133 | Requested ticket only |

### Interactive Flow (Default)
System asks one comprehensive question gathering all info at once:
- Deliverable type (ticket/story/epic/doc)
- Scope/scale
- Brief description

System waits for complete response before proceeding.

**Note:** In v0.920, tickets and stories are separate templates with distinct formatting and use cases. The system emphasizes concise transparency with two-layer processing.

---

<a id="5-mode-details"></a>
## 5. 📋 Mode Details

### 🎫 Ticket Mode (v0.133)

**Purpose:** Development tickets with detailed QA checklists for implementation tracking

**Format Improvements:**
- **Compressed About sections** - 1-2 lines with bold key-value pairs
- **Streamlined requirements** - Bullet format with inline descriptions
- **Tighter success criteria** - Essential metrics only
- **Detailed QA checklist** - Resolution items for verification
- **Mechanism explanations** - WHY before WHAT structure

**Key Feature:** Includes Resolution Checklist for QA verification (differentiates from stories)

**Complexity Levels:**
| Level | Indicators | Sections | Resolution Items | Use Case |
|-------|-----------|----------|------------------|----------|
| **Simple** | bug, fix, typo, update | 2-3 | 4-6 | Quick fixes and minor updates |
| **Standard** | feature, dashboard, api | 4-5 | 8-12 | Standard features and enhancements |
| **Complex** | platform, architecture, migration | 6-8 | 12-20 | System-wide changes and migrations |

---

### 📖 Story Mode (v0.133) **← Separated in v0.915**

**Purpose:** User stories in narrative format focusing on user journey and experience

**Key Features:**
- **User-centric format:** "As a [user], I want to [action] so that [benefit]"
- **User journey focus:** Emphasizes user perspective and experience throughout
- **Given-When-Then criteria:** Acceptance criteria in standard user story format
- **No Resolution Checklist:** Stories end with acceptance criteria (key differentiator)
- **Business value clear:** Explicit articulation of user and business value

**Complexity Levels:**
| Level | Indicators | Sections | Focus | Use Case |
|-------|-----------|----------|-------|----------|
| **Simple** | simple, basic, quick | 2-3 | Single user action | Simple user interactions |
| **Standard** | feature, capability, flow | 4-5 | Complete user journey | Standard user features |
| **Complex** | platform, system, ecosystem | 6-8 | Multi-step scenarios | Complex user workflows |

**Story vs Ticket Comparison:**
| Feature | Story (v0.133) | Ticket (v0.133) |
|---------|----------------|-----------------|
| **Command** | `$story` | `$ticket` |
| **Focus** | User journey & experience | Technical implementation |
| **Title Format** | "As a [user], I want..." | "[SCOPE] Feature: name" |
| **Acceptance** | Given-When-Then format | Standard criteria |
| **Checklist** | ❌ No Resolution Checklist | ✅ Detailed QA Checklist |
| **Audience** | Stakeholders, product team | Engineering, QA team |
| **Use Case** | Requirements definition | Implementation tracking |

---

### 🚀 Epic Mode (v0.130)

**Purpose:** Epics as summaries with links to stories and tickets

**Self-Contained Features:**
- All formatting standards built-in
- Complete symbol hierarchy defined
- Quality checks embedded
- Links to related stories and tickets

**Complexity Levels:**
| Level | Features | Template Sections | Focus | Use Case |
|-------|----------|-------------------|-------|----------|
| **Initiative** | 5-10 | 5-7 sections | Single team deliverables | Focused features, single-team projects |
| **Program** | 10-20 | 8-10 sections | Multi-team coordination | Cross-team initiatives, platform features |
| **Strategic** | 20+ | 10+ sections | Platform transformation | Company-wide changes, major platforms |

**Standard Epic Sections:**
1. **About** - 3 sentences max on what's being built and why
2. **Success Criteria** - Measurable outcomes
3. **Designs & References** - Links to documentation and designs
4. **Scope Overview** - High-level feature list with story/ticket links
5. **Implementation Plan** - Phases and timeline
6. **Stakeholders** - RACI matrix (if applicable)
7. **Risks & Mitigations** - When criteria met

---

### 📄 Doc Mode (v0.119)

**Purpose:** Technical documentation and user guides

**Self-Contained Features:**
- Complete formatting rules embedded
- Self-contained quality checks
- Standalone operation
- No external dependencies

**Complexity Levels:**
| Type | Main Sections | Depth | Use Case | Examples |
|------|---------------|-------|----------|----------|
| **Simple** | 2-3 | Quick reference | Product briefs, overviews | Feature announcements, quick guides |
| **Standard** | 4-6 | Detailed guide | Feature specs, user guides | API documentation, user manuals |
| **Complex** | 7+ | Comprehensive | Strategy docs, platforms | Architecture docs, system specifications |

**Common Documentation Types:**
- **Feature Documentation** - How features work and how to use them
- **API Documentation** - Endpoint specifications and examples
- **User Guides** - Step-by-step instructions for end users
- **Technical Specifications** - System architecture and design
- **Strategy Documents** - Product vision and roadmaps
- **Process Documentation** - Workflows and procedures

---

<a id="6-depth-thinking-framework"></a>
## 6. 🧠 DEPTH Thinking Framework

### Two-Layer Transparency Processing System
| Mode | Processing Depth | User Visibility | Application | Output |
|------|-----------------|-----------------|-------------|---------|
| **Standard Modes** | 10 rounds enforced | Concise meaningful updates | Real-time progress | Exact request |
| **$Quick Mode** | 1-5 auto-scaled | Summary provided | Complexity-based | Exact request |

**DEPTH Definition:**
DEPTH methodology (Discover, Engineer, Prototype, Test, Harmonize) is automatically applied with **two-layer transparency**. Full rigor applied internally, concise meaningful updates shown externally for optimal user experience.

### DEPTH Phases (v0.105 Two-Layer Model)
| Phase | Purpose | Internal Processing | User Sees (Concise) |
|-------|---------|-------------------|---------------------|
| **D**iscover | Deep understanding | 5 perspectives analyzed, assumption audit, opposition analysis | "🔍 Analyzing (5 perspectives) - Key insight: [finding]" |
| **E**ngineer | Solution generation | 8 approaches evaluated, constraint reversal, mechanism validation | "⚙️ Engineering (optimal approach selected)" |
| **P**rototype | Build framework | Template application, RICCE validation, mechanism-first check | "🔨 Building (template v0.133, mechanism-first validated)" |
| **T**est | Validate quality | 6-dimension self-rating, quality gates, improvement cycles | "✅ Validating (all dimensions 8+, excellence confirmed)" |
| **H**armonize | Final polish | Final validation, cognitive rigor check, delivery prep | "✨ Finalizing (excellence confirmed, ready for delivery)" |

### Concise Transparent Excellence in Action
```markdown
🔄 **Processing (DEPTH v0.105 - Concise Updates):**

🔍 **Analyzing** (5 perspectives: Technical, UX, Business, QA, Strategic)
**Key Insight:** OAuth token validation failure with configuration as primary suspect

⚙️ **Engineering** (8 solution approaches evaluated)
**Non-obvious Insight:** Constraint reversal revealed security pattern opportunity
**Selected:** Configuration validation + enhanced error handling

🔨 **Building** (Template v0.133, mechanism-first validated)
**Structure:** WHY OAuth fails → HOW to diagnose → WHAT to implement

---

<a id="depth-framework"></a>
## 🧠 DEPTH Framework (v0.105)

**Two-Layer Model:**
- **Internal**: Full 10-round methodology, all cognitive rigor, mandatory perspectives (min 3, target 5)
- **External**: Concise phase updates with key insights only

**Example User Communication:**
```markdown
🔍 **Analyzing** (5 perspectives confirmed)
**Key Insight:** [Most important finding]

✅ **Validating** (Quality: 92/100)
**Assumption Flagged:** [Critical dependency]

✨ **Finalizing** (Excellence confirmed)
```

**Full details in:** `Product Owner - DEPTH Thinking Framework - v0.105.md`

---

<a id="7-cognitive-rigor"></a>
## 7. 🔬 Cognitive Rigor Techniques

Five mandatory frameworks applied internally (users see key insights only):

1. **Multi-Perspective Analysis** - BLOCKING requirement (min 3, target 5)
2. **Assumption Audit** - Critical flags shown
3. **Perspective Inversion** - Key opposition insights
4. **Constraint Reversal** - Non-obvious solutions
5. **Mechanism First** - WHY before WHAT validation

**Quality Dimensions:** Completeness, Clarity, Actionability, Accuracy, Relevance, Mechanism Depth (all target 8+)

---

<a id="8-automatic-complexity"></a>
## 8. ⚙️ Automatic Complexity Detection

System auto-detects complexity from keywords:

**For Tickets:**
- **Simple**: bug, fix, typo (2-3 sections, 4-6 items)
- **Standard**: feature, dashboard, api (4-5 sections, 8-12 items)
- **Complex**: platform, architecture, migration (6-8 sections, 12-20 items)

**$quick mode:** Auto-scales to 2/3/5 rounds based on complexity

**Output Guarantee:** Exact request = exact output (no scope expansion)
- "Fix login bug" → That bug only
- "Build dashboard" → That dashboard only
- "Platform migration" → That migration only

---

<a id="9-system-architecture"></a>
## 9. 🏗️ System Architecture

```
AGENTS.md → Entry point with routing logic
    ↓
Writer - Product Owner - v0.920.md (System prompt)
    ↓
DEPTH Framework v0.105 (Methodology)
    ↓
Interactive Mode v0.306 (Conversation flow)
    ↓
Templates (Ticket v0.133, Story v0.133, Epic v0.130, Doc v0.119)
    ↓
Output → /Export/[###]-artifact.md
```