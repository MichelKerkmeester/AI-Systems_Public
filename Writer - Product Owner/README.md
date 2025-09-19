# Product Owner System - User Guide v0.890

Transforms requests into professional development tickets, strategic epics, and documentation through intelligent interactive guidance with built-in complexity challenging.

## 📋 Table of Contents

- [🆕 What's New In V0.890](#whats-new-in-v0890---mode-specific-formatting)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🎫 Ticket Mode](#ticket-mode)
- [🚀 Epic Mode](#epic-mode)
- [📄 Doc Mode](#doc-mode)
- [🧠 Atlas Thinking Framework](#atlas-thinking-framework)
- [🎯 Automatic Complexity Detection](#automatic-complexity-detection)
- [💡 Challenge Mode](#challenge-mode)
- [🗃️ Past Chats Integration](#past-chats-integration)
- [⚡ Emergency Commands](#emergency-commands)
- [📝 Symbol & Formatting Reference](#symbol--formatting-reference)
- [🆘 Troubleshooting](#troubleshooting)
- [📦 Version History](#version-history)

.

## 🆕 What's New In V0.890 - Mode-Specific Formatting

### Critical Updates: Symbol Systems & Formatting
- **Mode-Specific Symbols**: Each mode now has its own symbol hierarchy
- **Ticket Mode**: ⌘, ❖, ◻︎, ◊, — (streamlined for development)
- **Epic/Doc Mode**: ⌘, ❖, ◻︎, ◊, — (hierarchical for strategy)
- **Doc Mode Fix**: Situation/Action blocks now properly formatted on separate lines
- **List Standardization**: Always `-` for lists, `[ ]` for checkboxes (no hyphens)

### Core Features Maintained
- **5 Intelligent Modes**: Interactive (default), $quick, $ticket, $epic, $doc
- **$Quick Mode**: ZERO questions for maximum speed
- **46 Core Rules**: Updated with mode-specific formatting requirements

.

## ✨ Key Features

- **🧠 ATLAS Framework**: 5-phase thinking methodology
- **⚡ $Quick Mode**: Zero-wait immediate creation
- **🚀 Epic Mode**: Strategic initiative planning with OKR alignment
- **💡 Challenge Mode**: Three-level hierarchy with calibration
- **🎯 Smart Complexity**: Automatic detection and scaling
- **🗃️ Past Chats Integration**: Searches conversation history
- **⚡ Emergency Commands**: $reset, $quick, $status
- **📄 Pattern Learning**: Adapts to preferences
- **🚨 REPAIR Protocol**: Structured error recovery
- **📊 Thinking Calibration**: Formula-based recommendations (6-10 rounds)
- **🖋️ Mode-Specific Formatting**: Each mode uses appropriate symbols

.

## 🚀 Quick Setup

### Step 1: Create A Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Product Owner"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Product Owner - v0.883.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project:

**Core Documents:**
- `Product Owner - ATLAS Thinking Framework - v0.172.md`
- `Product Owner - Artifact Standards - v0.133.md`
- `Product Owner - Interactive Mode - v0.272.md`
- `Product Owner - Quick Reference - v0.113.md`

**Template Documents:**
- `Product Owner - Template - Ticket Mode - v0.110.md`
- `Product Owner - Template - Epic Mode - v0.102.md`
- `Product Owner - Template - Doc Mode - v0.107.md`

### Step 4: Start Creating
```
need user authentication         # Interactive discovery flow
$quick auth epic                # Immediate epic creation
$epic payment platform          # Direct epic mode
$ticket payment integration     # Direct ticket mode
```

.

## 🎛️ Operating Modes

| Mode | Command | Output | Questions | Wait Points | Symbol System |
|------|---------|--------|-----------|-------------|---------------|
| **Interactive** | DEFAULT | Varies | Adaptive | Multiple | Mode-specific |
| **$Quick** | `$quick` | Any type | **NONE** | **NONE** | Mode-appropriate |
| **Epic** | `$epic` | Strategic initiatives | 3-5 | Rounds, Challenge | ⌘, ❖, ◻︎, ◊, —— |
| **Ticket** | `$ticket` | Development tickets | 2-4 | Rounds, Challenge | ⌘, ❖, ◻︎, ◊, — |
| **Documentation** | `$doc` | User guides | 3-4 | Rounds, Format | ⌘, ❖, ◻︎, ◊, —— |

### Interactive Flow (Default)
```
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket - Feature or bug for developers
2. Epic ticket - Strategic initiative or program
3. Product documentation - User guide or format text

Which best fits? (1-3)
```

### $Quick Mode - Zero-Wait Creation
```
User: $quick - Q1 payments initiative

System: **Quick Mode Activated** ⚡
Creating your payments initiative epic immediately...
- Using 6 thinking rounds (auto)
- No challenges applied
- Maximum speed delivery

[CREATES ARTIFACT IMMEDIATELY]
```

**$Quick Mode Characteristics:**
- NO thinking rounds question - Always uses 6
- NO challenge presentation - Skips regardless
- NO additional questions - Proceeds immediately
- Works with all modes - Tickets, epics, and docs
- Uses mode-appropriate formatting automatically

.

## 🎫 Ticket Mode

### Development Ticket Creation
```
User: $ticket payment integration

System: Let's create your payment integration ticket! 🎯

How many thinking rounds should I use? (6-10)
Based on payment integration, I recommend: 8 rounds

Your choice?
```

### Ticket Complexity Levels
| Type | Sections | Resolution Items | Example |
|------|----------|------------------|---------|
| **Simple** | 2-3 | 4-6 items | Bug fix, update |
| **Standard** | 4-5 | 8-12 items | Feature, dashboard |
| **Complex** | 6-8 with phases | 12-20 items | Platform, architecture |

### Ticket Structure & Symbols
- **⌘ About**: Context and background (H1)
- **❖ Requirements**: Main sections (H2)
- **◻︎ Functional/Technical**: Sub-sections (H3)
- **◊ Components**: Detail headers (H4)
- **— Bold sub-headings**: Within H4 sections

### List Formatting
```markdown
### ◻︎ Functional Requirements

- First requirement    ✓ (use hyphen for lists)
- Second requirement   ✓

## ✓ Resolution Checklist

[ ] First item        ✓ (no hyphen before checkbox)
[ ] Second item       ✓
```

.

## 🚀 Epic Mode

### Strategic Initiative Planning
```
User: $epic authentication overhaul

System: Let's structure your authentication overhaul epic! 🚀

How many thinking rounds should I use? (6-10)
Recommended: 7 rounds for quarterly initiative

Your choice?
```

### Epic Complexity Levels
| Level | Sections | Child Tickets | Timeline | Example |
|-------|----------|---------------|----------|---------|
| **Initiative** | 4-5 | 3-5 tickets | Quarterly | Feature rollout |
| **Program** | 6-7 | 6-10 tickets | Half-year | Platform upgrade |
| **Strategic** | 8-10 | 10+ tickets | Annual | Digital transformation |

### Epic Structure & Symbols
- **⌘ About**: Strategic overview (H1)
- **❖ Timeline & Phases**: Main sections (H1)
- **◻︎ Phase Details**: Sub-sections (H2)
- **◊ Components**: Sub-components (H3)
- **—— Details**: Nested details (H4)

### Epic-Specific Formatting
```markdown
### ◊ OKRs

— Objective: [Clear objective]     ✓ (use em dash under ◊)
— KR1: [Measurable result]         ✓
— KR2: [Measurable result]         ✓
```

.

## 📄 Doc Mode

### Documentation Creation
```
User: $doc API guide

System: Let's create your API documentation! 📚

How many thinking rounds should I use? (6-10)
Recommended: 6 rounds for technical guide

Your choice?
```

### Documentation Types
- **User Guides**: Step-by-step instructions
- **Feature Docs**: Capability explanations
- **Technical Specs**: API and integration details
- **Process Docs**: Workflow documentation

### Doc Structure & Symbols
- **⌘ About**: Document overview (H1)
- **❖ Main Sections**: Primary content (H1)
- **◻︎ Subsections**: Secondary content (H2)
- **◊ Components**: Detailed items (H3)
- **—— Details**: Granular content (H4)

### Critical Doc Formatting
**Thresholds & Actions - CORRECT:**
```markdown
1. **[Metric condition]** = [threshold]

**Situation:** [What this indicates]

**Action:** [Step 1] → [Step 2] → [Step 3]
```

**INCORRECT:**
```markdown
Situation: [text] Action: [text]  ✗ (never on one line)
```

.

## 🧠 Atlas Thinking Framework

### User Control Points
| Phase | Purpose | Wait Points |
|-------|---------|-------------|
| **A** | Assess & Challenge | After assessment |
| **T** | Transform & Expand | After options |
| **L** | Layer & Analyze | During analysis |
| **A** | Assess Impact | After validation |
| **S** | Synthesize & Ship | Before creation |

### Thinking Round Calibration
```
How many thinking rounds should I use? (6-10)

Based on your request, I recommend: [X rounds]
- Complexity: [Low/Medium/High]
- Uncertainty: [Low/Medium/High]
- Stakes: [Low/Medium/High]

[Historical note: You typically use 7 rounds]

Your choice?
```

### Phase Application By Rounds
| Rounds | Phases | Use Case |
|--------|--------|----------|
| 6 | A→T→L→S | Standard depth, $quick default |
| 6-7 | A→T→L→A→S | Standard tickets/epics/docs |
| 8-9 | Full Atlas+ | Complex features/programs |
| 10 | Deep Atlas | Strategic analysis/epics |

.

## 🎯 Automatic Complexity Detection

### For Tickets
| Indicators | Complexity | Sections | Challenge Focus |
|------------|------------|----------|-----------------|
| Bug fix, update | **Simple** | 2-3 | "Is this really needed?" |
| Feature, dashboard | **Standard** | 4-5 | "Could we do less?" |
| Platform, architecture | **Complex** | 6-8 | "Can we phase this?" |

### For Epics
| Indicators | Complexity | Sections | Challenge Focus |
|------------|------------|----------|-----------------|
| Single feature | **Initiative** | 4-5 | "Can we deliver faster?" |
| Multi-team | **Program** | 6-7 | "Should we phase this?" |
| Platform | **Strategic** | 8-10 | "Break into quarters?" |

**Note:** In $quick mode, complexity is detected but challenges are never presented.

.

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
"This epic spans multiple quarters. Should we:
- Phase it into quarterly initiatives?
- Focus on highest-impact quarter first?
- Keep the full strategic scope?"

[WAIT FOR USER RESPONSE]
```

**$Quick Mode Exception:** Never presents challenges regardless of complexity

.

## 🗃️ Past Chats Integration

### Tool Usage
- **conversation_search**: Topic/keyword-based search
- **recent_chats**: Time-based retrieval

### Context Enhancement Journey
| Stage | Interactions | Context Level | User Control |
|-------|-------------|---------------|--------------|
| Learning | 1-3 | Building | 100% |
| Adapting | 4-6 | Light notes | 100% |
| Enriched | 7-9 | Detailed | 100% |
| Comprehensive | 10+ | Maximum | 100% |

**Critical Principles:**
- Historical context enriches but never restricts
- All options always available
- Wait points maintained (except $quick mode)
- User autonomy absolute

.

## ⚡ Emergency Commands

| Command | Action | Result | Waits? |
|---------|--------|--------|--------|
| **`$reset`** | Clear all context | Start fresh | YES |
| **`$quick`** | **IMMEDIATE creation** | **NO questions** | **NO** |
| **`$status`** | Show context | Display patterns | N/A |

### Usage Examples
```
$reset
# Clears all historical context and patterns

$quick - Q1 payments epic
# Creates epic immediately with NO questions

$status
# Shows current patterns and preferences
```

.

## 📝 Symbol & Formatting Reference

### Ticket Mode Symbols
| Symbol | Purpose | Header Level |
|--------|---------|--------------|
| **⌘** | About section | H1 |
| **❖** | Main headers | H2 |
| **◻︎** | Sub-headers | H3 |
| **◊** | Components | H4 |
| **—** | Bold sub-headings | Bold text |

### Epic & Doc Mode Symbols
| Symbol | Purpose | Header Level |
|--------|---------|--------------|
| **⌘** | About section | H1 |
| **❖** | Main headers | H1 |
| **◻︎** | Sub-headers | H2 |
| **◊** | Components | H3 |
| **——** | Detail headers | H4 |

### Universal Formatting Rules
- **Lists**: Always use `-` for regular lists
- **Checkboxes**: Always use `[ ]` without hyphens
- **References**: Use → for links and references
- **Success Criteria**: Use ✦ for bullets, ✓ for checkboxes
- **Dependencies**: Use ≈ symbol
- **Doc Formatting**: Situation/Action on separate lines

.

## 🆘 Troubleshooting

### Common Issues
| Issue | Solution |
|-------|----------|
| **Wrong symbols appearing** | Check mode - each has specific symbols |
| **Doc text on one line** | Situation/Action must be on separate lines |
| **Checkbox formatting wrong** | Use `[ ]` without hyphens |
| **Too complex for need** | Reduce thinking rounds |
| **Pattern mismatch** | Override and system learns |
| **Want speed** | Use $quick mode |
| **Confused context** | Use $reset |

### REPAIR Framework for Errors
- **R**ecognize - Identify issue
- **E**xplain - Clear description
- **P**ropose - Multiple solutions
- **A**dapt - Apply chosen fix
- **I**terate - Test and confirm
- **R**ecord - Learn for future

.

## 📦 Version History

### v0.890 (Current)
- **Mode-Specific Symbols**: Each mode has unique hierarchy
- **Doc Mode Fix**: Proper line breaks for Situation/Action
- **List Standardization**: Consistent formatting rules
- **46 Core Rules**: Including mode-specific formatting

### v0.880
- **Epic Mode Added**: Strategic initiatives with OKR/KPI tracking
- **5 Operating Modes**: Interactive, $quick, $ticket, $epic, $doc
- **3 Epic Complexity Levels**: Initiative, Program, Strategic

### v0.875
- Refined focus, removed spec mode
- 4 Operating Modes, clearer purpose

### v0.874
- Streamlined focus, simplified rounds
- Removed text mode

### v0.873
- Revolutionary $quick mode
- 43 Core Rules including $quick override

### Previous Versions
- **v0.860**: Challenge hierarchy, professional approach
- **v0.850**: Past Chats Integration, Emergency Commands
- **v0.830**: Separated template architecture

---

*Mode-specific formatting ensures professional output. Each mode uses appropriate symbols: Ticket (⌘, ❖, ◻︎, ◊, —), Epic/Doc (⌘, ❖, ◻︎, ◊, ——). Revolutionary $quick mode for immediate creation. Interactive Mode remains the thoughtful default. Choose $quick when speed matters, Interactive when customization matters, $epic when strategy matters. User autonomy is absolute.*