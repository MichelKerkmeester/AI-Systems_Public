# Prompt Engineering Assistant - User Guide v0.820

A system that transforms vague requests into clear, effective AI prompts using the ATLAS framework, challenge-based simplification, and intelligent refinement.

## 📋 Table of Contents

- [🆕 What's New in v0.820](#whats-new-in-v0820)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [📄 Format Options](#format-options)
- [🧠 ATLAS Thinking Framework](#atlas-thinking-framework)
- [🚀 Challenge Mode Philosophy](#challenge-mode-philosophy)
- [🗃️ Past Chats Integration](#past-chats-integration)
- [⚡ Emergency Commands](#emergency-commands)
- [🚨 REPAIR Error Protocol](#repair-error-protocol)
- [🆘 Troubleshooting](#troubleshooting)
- [📦 Version History](#version-history)

.

## 🆕 What's New in v0.820

### Major Enhancements 🚀
- **Emergency Commands**: `$reset`, `$standard`, `$quick`, `$status` for quick recovery
- **Enhanced Past Chats**: Sophisticated conversation search with context stages
- **Context Enhancement Journey**: Progressive learning (Learning → Adapting → Enriched → Comprehensive)
- **Status Command**: Shows all tracked patterns
- **Challenge Calibration**: Adapts intensity based on your acceptance history

.

## ✨ Key Features

- **MANDATORY Thinking Rounds**: 1-10 or 'auto' - always asked
- **Emergency Commands**: Quick system control
- **Progressive Context Learning**: Stages from Learning to Comprehensive
- **Multi-Format Output**: Standard, JSON, and SMILE formats
- **ATLAS Framework**: 5-phase systematic enhancement
- **Challenge Mode**: Auto-calibrates based on acceptance
- **Smart Defaults**: Reduces questions by 60%
- **REPAIR Protocol**: Enhanced error recovery
- **30-50% Complexity Reduction**: Measurable simplification
- **Universal Platform Support**: Works on ALL AI platforms

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Prompt Engineering Assistant"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Prompt Improver.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project's knowledge base:

**Critical Documents:**
- `Prompt - Core System & Quick Reference.md`
- `Prompt - Artifact Standards & Templates.md`
- `Prompt - ATLAS Thinking Framework.md`

**Mode Documents:**
- `Prompt - Interactive Mode.md`
- `Prompt - Builder Mode.md`
- `Prompt - Evaluation & Refinement.md`
- `Prompt - Patterns & Enhancements.md`
- `Prompt - Quick Reference.md`

### Step 4: Start Creating
```
write about dogs              # Asks thinking rounds, then enhances
$improve analyze data         # Asks thinking rounds, offers formats
$interactive                  # Guided with professional formatting
$status                      # See your current patterns
```

.

## 🎛️ Operating Modes

### Core Modes

| Mode | Activation | Best For | Thinking Rounds |
|------|------------|----------|-----------------|
| **$interactive** | DEFAULT | Learning | Variable |
| **$short** | `$short` | Simple clarity | 1-2 |
| **$improve** | `$improve` | Most improvements | 3-4 |
| **$refine** | `$refine` | Maximum quality | 5-8 |
| **$json** | `$json` | API format | 2-3 |
| **$smile** | `$smile` | Complex instructions | 2-3 |
| **$builder** | `$builder` | Platform prompts | Auto |

### Builder Sub-Modes

| Sub-Mode | Purpose | Default Phase |
|----------|---------|---------------|
| **Prototype** | Visual exploration | MVP exploration |
| **Website** | Conversion sites | Core message |
| **App** | Applications | Essential only |

### Supported Platforms
Bolt.new, MagicPatterns, v0 by Vercel, Cursor/Windsurf, Replit, Lovable, and ANY AI platform

.

## 📄 Format Options

### Standard Format (Default)
Natural language clarity, maximum readability
```
As a data analyst, analyze Q4 sales data focusing on revenue drivers. 
Create an executive summary with actionable insights.
```

### JSON Format
Structured for APIs and programmatic use (+/- 5% tokens)
```json
{
  "role": "data_analyst",
  "task": "analyze_q4_sales",
  "focus": ["revenue_drivers"],
  "output": "executive_summary"
}
```

### SMILE Format
Enhanced instruction following (+20-30% tokens)
```
(: Sales Analysis Task
  [: Role [ Data analyst ] :]
  [= Task =] Analyze Q4 sales data
  [: Output [ Executive Summary ] :]
) :)
```

.

## 🧠 ATLAS Thinking Framework

### User-Controlled Process
```
How many thinking rounds would you like? (1-10, or 'auto')

Based on your request, I recommend: 5 rounds
• Clarity: Low - needs structure
• Complexity: High - multi-step process
• Enhancement: Comprehensive

[Previous patterns: You typically choose 5 rounds]

Your choice?
```

### Framework Phases
- **A** - Assess & Challenge (check complexity, search patterns)
- **T** - Transform & generate alternatives (3 versions)
- **L** - Layer & build improvements (structure for format)
- **A** - Assess impact of changes (verify value)
- **S** - Synthesize & deliver optimal version
- **F** - Format Transform (apply Standard/JSON/SMILE)

.

## 🚀 Challenge Mode Philosophy

> "Every feature has a cost. Start with the minimum that delivers value."

### Calibrated Challenge Levels
| Acceptance History | Approach | Example |
|-------------------|----------|---------|
| < 30% | Gentle | "Could this be simpler?" |
| 30-70% | Constructive | "Simpler might work better..." |
| > 70% | Strong | "Let's focus on the core ask" |

.

## 🗃️ Past Chats Integration

### Context Enhancement Journey
| Stage | Interactions | Context Level |
|-------|-------------|---------------|
| Learning | 1-3 | Basic notes |
| Adapting | 4-6 | Light suggestions |
| Enriched | 7-9 | Detailed patterns |
| Comprehensive | 10+ | Maximum context |

### Tool Usage
- **conversation_search**: Topic/keyword-based search
- **recent_chats**: Time-based retrieval (1-20 chats)

.

## ⚡ Emergency Commands

| Command | Action | When to Use |
|---------|--------|-------------|
| **`$reset`** | Clear all context | Context outdated |
| **`$standard`** | Default flow | Want clean process |
| **`$quick`** | Skip to enhancement | Know what you want |
| **`$status`** | Show patterns | Check system state |

.

## 🚨 REPAIR Error Protocol

Enhanced error recovery with historical context tracking:
- Recognize issue with historical context
- Explain impact on clarity
- Alternatives (provide 3 options)
- Refine approach
- Note pattern for future

.

## 🆘 Troubleshooting

**Context seems wrong:**
```
$status → Check what's tracked
$reset → Clear if needed
```

**Too many suggestions:**
```
$standard → Clean process
$quick → Skip to essentials
```

**Lost in the system:**
```
$status → See current state
Interactive Mode → Default exploration
```

.

## 📦 Version History

- **v0.820**: Emergency commands, enhanced past chats, context journey stages
- **v0.810**: MANDATORY thinking rounds, professional standards
- **v0.800**: SMILE format integration, multi-format support
- **v0.700**: ATLAS framework, Challenge mode, REPAIR protocol

---

*Transform vague requests into clear, professional prompts! Interactive Mode is DEFAULT. Thinking rounds are MANDATORY. User control is absolute.*