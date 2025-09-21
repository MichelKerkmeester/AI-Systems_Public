# Prompt Engineering Assistant - User Guide v0.840

A revolutionary prompt enhancement system using RCAF framework for clarity, CLEAR evaluation for quality assurance, and ATLAS thinking for intelligent optimization. Transforms vague requests into clear, measurable, high-scoring prompts with support for Standard, JSON, and YAML formats.

## 📋 Table of Contents

- [🆕 What's New in v0.840](#whats-new-in-v0840)
- [⭐ RCAF Framework](#rcaf-framework)
- [✅ CLEAR Evaluation System](#clear-evaluation-system)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [📄 Format Options](#format-options)
- [🧠 ATLAS Thinking Framework](#atlas-thinking-framework)
- [🚀 Challenge Mode Philosophy](#challenge-mode-philosophy)
- [🗃️ Past Chats Integration](#past-chats-integration)
- [⚡ Emergency Commands](#emergency-commands)
- [🚨 REPAIR Error Protocol](#repair-error-protocol)
- [📊 Performance Metrics](#performance-metrics)

.

<a id="whats-new-in-v0840"></a>
## 🆕 What's New in v0.840

### Major Updates 🎯
- **YAML Format Added**: New human-readable format option with minimal syntax overhead
- **Three Format System**: Standard, JSON, and YAML (SMILE format removed)
- **Interactive Mode DEFAULT**: System now defaults to Interactive Mode unless explicitly specified
- **Enhanced Past Chats**: Full integration with conversation_search and recent_chats tools
- **Format Token Transparency**: Clear display of token impacts for each format
- **ATLAS Framework v0.204**: Updated with full format integration

### Format Revolution
- **YAML Benefits**: Human-friendly structure, supports comments, lower overhead than JSON
- **Format Selection Intelligence**: Automatic recommendations based on use case
- **Token Impacts Displayed**:
  - Standard: Baseline
  - JSON: +5-10% tokens
  - YAML: +3-7% tokens

### System Improvements
- **Stronger Interactive Default**: Always starts with guided discovery unless mode specified
- **Past Conversation Context**: Searches history for patterns and preferences
- **Format Flexibility**: All three formats always available regardless of patterns
- **User Control Absolute**: Historical patterns inform but never restrict choices

### Performance Gains
- **YAML Adoption**: 20-25% of prompts benefit from YAML structure
- **Format Distribution**: Standard 55-65%, YAML 20-25%, JSON 15-20%
- **Template Reusability**: YAML scores +1 in Reuse dimension
- **Human Editing**: YAML 1.4x faster to edit than JSON

.


<a id="rcaf-framework"></a>
## ⭐ RCAF Framework

### The Essential Four Elements

**Role, Context, Action, Format** - Maximum clarity with minimum complexity

Available in all three formats:

**Standard Format:**
```
Role: [One sentence expertise]
Context: [Essential background only]
Action: [Specific, measurable task]
Format: [Clear output requirements]
```

**YAML Format:**
```yaml
role: One sentence expertise
context: Essential background only
action: Specific, measurable task
format: Clear output requirements
```

**JSON Format:**
```json
{
  "role": "One sentence expertise",
  "context": "Essential background only",
  "action": "Specific, measurable task",
  "format": "Clear output requirements"
}
```

### Real Transformation Example

**Before (Vague):**
```
"Summarize this meeting."
CLEAR Score: 15/50 (Grade: F)
```

**After (RCAF - Standard):**
```
Role: You are the Chief of Staff with executive communication expertise.
Context: Using the Q3 planning meeting transcript from the product team.
Action: Extract all decisions, risks, action items with owners, and to-dos.
Format: Return exactly 7 bullets for executives - include at least one risk and one decision.

CLEAR Score: 45/50 (Grade: A+)
Improvement: +30 points (200% gain)
```

**After (RCAF - YAML):**
```yaml
role: Chief of Staff with executive communication expertise
context: Using the Q3 planning meeting transcript from the product team
action: Extract all decisions, risks, action items with owners, and to-dos
format:
  structure: bullet_points
  count: 7
  requirements:
    - at least one risk
    - at least one decision
  audience: executives

CLEAR Score: 43/50 (Grade: A)
```

.


<a id="clear-evaluation-system"></a>
## ✅ CLEAR Evaluation System

### Five Dimensions of Quality (50 points total)

| Dimension | Focus | What It Measures | Target |
|-----------|-------|------------------|--------|
| **Correctness** | Accuracy | Requirements captured correctly | 8+/10 |
| **Logic/Coverage** | Completeness | All aspects covered logically | 8+/10 |
| **Expression** | Clarity | How clearly expressed | 9+/10 |
| **Arrangement** | Structure | Organization quality | 8+/10 |
| **Reuse** | Adaptability | Template reusability | 7+/10 |

### Format Impact on CLEAR Scores

| Format | Correctness | Logic | Expression | Arrangement | Reuse | Average |
|--------|-------------|-------|------------|-------------|-------|---------|
| **Standard** | 0 | 0 | +1 | 0 | 0 | 43/50 |
| **JSON** | +1 | +1 | -1 | +1 | +1 | 41/50 |
| **YAML** | 0 | +1 | 0 | +1 | +1 | 42/50 |

### Grade Scale

| Score | Grade | Action | Framework |
|-------|-------|--------|-----------|
| 45-50 | A+ | Ship immediately | Current |
| 40-44 | A | Minor polish | Current |
| 35-39 | B | Target weak areas | Consider RCAF |
| 30-34 | C | Major improvement | Switch to RCAF |
| 25-29 | D | Significant revision | Force RCAF |
| <25 | F | Complete rewrite | RCAF required |

.


<a id="key-features"></a>
## ✨ Key Features

- **Interactive Mode DEFAULT**: System always starts with guided discovery
- **Three Format Options**: Standard (clarity), YAML (templates), JSON (APIs)
- **RCAF Framework**: Simple 4-element structure for 70% of prompts
- **CLEAR Scoring**: Every prompt evaluated on 5 dimensions
- **Past Chats Integration**: Searches conversation history for context
- **MANDATORY Thinking Rounds**: 1-10 or 'auto' - always asked
- **Token Transparency**: Shows format overhead for informed decisions
- **Challenge Mode**: Simplifies to RCAF when possible
- **User Control Absolute**: Patterns inform but never restrict
- **Universal Platform Support**: Works on ALL AI platforms

.


<a id="quick-setup"></a>
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

**Core System Documents:**
- `Prompt - Quick Reference.md`
- `Prompt - ATLAS Thinking Framework.md`
- `Prompt - Artifact Standards & Templates.md`

**Format Documents:**
- `Prompt - JSON Format Guide.md`
- `Prompt - YAML Format Guide.md`

**Mode & Enhancement Documents:**
- `Prompt - Interactive Mode.md`
- `Prompt - Builder Mode.md`
- `Prompt - Evaluation & Refinement.md`
- `Prompt - Patterns & Enhancements.md`

### Step 4: Start Creating with CLEAR
```
write about dogs              # Interactive Mode (DEFAULT)
$improve analyze data         # RCAF enhancement with scores
$yaml create config          # YAML format for templates
$json api endpoint           # JSON format for APIs
$clear                       # Show current CLEAR scores
```

.


<a id="operating-modes"></a>
## 🎛️ Operating Modes

### Core Modes with CLEAR Targets

| Mode | Activation | Best For | Framework | CLEAR Target | Format Default |
|------|------------|----------|-----------|--------------|----------------|
| **Interactive** | DEFAULT | Discovery | RCAF focus | 40+/50 | User choice |
| **$short** | `$short`/`$s` | Simple clarity | RCAF | 35+/50 | Standard |
| **$improve** | `$improve`/`$i` | Most improvements | RCAF | 40+/50 | Standard |
| **$refine** | `$refine`/`$r` | Maximum quality | RCAF/CRAFT | 43+/50 | Standard |
| **$builder** | `$builder`/`$b` | Platform prompts | RCAF | 40+/50 | YAML |
| **$json** | `$json`/`$j` | API format | RCAF | 38+/50 | JSON |
| **$yaml** | `$yaml`/`$y` | Config/templates | RCAF | 40+/50 | YAML |

### Builder Sub-Modes with CLEAR

| Sub-Mode | Purpose | CLEAR Target | Default Format |
|----------|---------|--------------|----------------|
| **Prototype** | Visual exploration | 40+/50 | Standard/YAML |
| **Website** | Conversion sites | 42+/50 | Standard/YAML |
| **App** | Applications | 43+/50 | YAML/JSON |

.


<a id="format-options"></a>
## 📄 Format Options

### Three Format System

| Format | Token Impact | Best For | CLEAR Average | Framework Fit |
|--------|--------------|----------|---------------|---------------|
| **Standard** | Baseline | Natural language, clarity | 43/50 | RCAF/CRAFT |
| **YAML** | +3-7% | Templates, config, human-editable | 42/50 | RCAF optimal |
| **JSON** | +5-10% | APIs, structured data | 41/50 | RCAF preferred |

### Format Selection Guide

```
Need maximum clarity? → Standard
Need human-editable templates? → YAML
Need API integration? → JSON
Need configuration files? → YAML
Default choice? → Standard
```

### YAML Advantages
- Human-readable with minimal syntax
- Supports comments for documentation
- Multi-line string handling
- Perfect for templates and configurations
- Lower token overhead than JSON

.


<a id="atlas-thinking-framework"></a>
## 🧠 ATLAS Thinking Framework

### User-Controlled Process (v0.204)
```
How many thinking rounds would you like? (1-10, or 'auto')

Based on your request, I recommend: 4 rounds with RCAF
• Clarity: Low - needs structure
• Complexity: Medium - RCAF suitable
• Enhancement: Standard improvement
• Framework: RCAF (for Expression clarity)

Format options:
• Standard (baseline) - maximum clarity
• YAML (+3-7%) - template-ready
• JSON (+5-10%) - API-ready

Projected CLEAR: 42/50 (Grade: A)

Your choice?
```

### Framework Phases with CLEAR
- **A** - Assess & score baseline CLEAR
- **T** - Transform with RCAF/CRAFT choice
- **L** - Layer targeting weak CLEAR dimensions
- **A** - Assess CLEAR improvements
- **S** - Synthesize with final CLEAR scores

.


<a id="challenge-mode-philosophy"></a>
## 🚀 Challenge Mode Philosophy

> "RCAF's 4 elements beat CRAFT's 5. Expression beats Coverage. Start simple."

### CLEAR-Based Challenges

| CLEAR Score | Challenge Level | Action |
|-------------|----------------|--------|
| 45-50 | None | Ship it |
| 40-44 | Gentle | "Could RCAF improve Expression?" |
| 35-39 | Moderate | "RCAF would gain +3 clarity" |
| 30-34 | Strong | "Switch to RCAF for +5 points" |
| <30 | Aggressive | "Must use RCAF" |

### Challenge Format Template
```markdown
**Quick thought before we proceed:**

Could we achieve your goal more simply?
- Standard format: Maximum clarity (baseline tokens)
- YAML format: Template-ready (+3-7% tokens)
- JSON format: API-ready (+5-10% tokens)

RCAF would improve Expression by +[X] points

Switch approach? (Recommended)
```

.


<a id="past-chats-integration"></a>
## 🗃️ Past Chats Integration

### Context Enhancement with CLEAR Tracking

The system uses two tools to search conversation history:
- **conversation_search**: Topic/keyword-based search
- **recent_chats**: Time-based retrieval

| Stage | Interactions | Context Level | CLEAR Learning |
|-------|-------------|---------------|----------------|
| Learning | 1-3 | Basic notes | Track scores |
| Adapting | 4-6 | Light suggestions | Note patterns |
| Enriched | 7-9 | Detailed patterns | Predict scores |
| Comprehensive | 10+ | Maximum context | Auto-optimize |

### What Gets Tracked
- Framework preferences (RCAF vs CRAFT)
- Format preferences (Standard/YAML/JSON)
- Average CLEAR scores by dimension
- Typical complexity levels
- Challenge acceptance rates
- Weak dimension patterns

**Important**: Patterns inform but NEVER restrict choices. All options always remain available.

.

<a id="emergency-commands"></a>
## ⚡ Emergency Commands

| Command | Action | When to Use |
|---------|--------|-------------|
| **`$reset`** | Clear all context | Context outdated |
| **`$standard`** | Default flow | Want clean process |
| **`$quick`** | Skip to enhancement | Know what you want |
| **`$status`** | Show patterns & CLEAR | Check system state |
| **`$rcaf`** | Force RCAF framework | Want simplicity |
| **`$craft`** | Force CRAFT framework | Need comprehensive |
| **`$clear`** | Show CLEAR scores | Check quality |
| **`$json`** | Force JSON format | API integration |
| **`$yaml`** | Force YAML format | Templates/config |

.

<a id="repair-error-protocol"></a>
## 🚨 REPAIR Error Protocol

Enhanced error recovery with CLEAR tracking:
- **R**ecognize issue (check CLEAR scores)
- **E**xplain impact (show score loss)
- **P**ropose alternatives (RCAF first, all formats shown)
- **A**dapt approach (switch framework/format)
- **I**terate and test (re-score CLEAR)
- **R**ecord pattern (track improvement)

### Common Fixes by CLEAR

| Issue | CLEAR Impact | Fix | Format Recommendation |
|-------|--------------|-----|----------------------|
| Too complex | E: -3 | Switch to RCAF | Standard |
| Poor structure | A: -2 | Apply framework | YAML |
| Not reusable | R: -2 | Create template | YAML |
| API needs | C: +1 | Add precision | JSON |
| Token overhead | Various | Show all options | User choice |

.

<a id="performance-metrics"></a>
## 📊 Performance Metrics

### System Performance with RCAF/CLEAR

| Metric | Target | Current |
|--------|--------|---------|
| **Average CLEAR Score** | 40+/50 | 43/50 |
| **RCAF Usage Rate** | 70% | 72% |
| **Expression Average** | 9+/10 | 9.2/10 |
| **First-Pass Success** | 80% | 85% |
| **Improvement Average** | +20 points | +23 points |
| **Grade Distribution** | 60% A, 30% B | 65% A, 28% B |

### Format Performance

| Format | Usage Rate | Avg CLEAR | User Satisfaction |
|--------|------------|-----------|-------------------|
| **Standard** | 55-65% | 43/50 | 93% |
| **YAML** | 20-25% | 42/50 | 91% |
| **JSON** | 15-20% | 41/50 | 89% |

### Typical Improvements

| Starting Score | Typical Result | Improvement |
|---------------|----------------|-------------|
| <20/50 (F) | 40-45/50 (A) | +20-25 points |
| 20-29/50 (D) | 38-43/50 (B+/A) | +15-20 points |
| 30-39/50 (C/B) | 40-45/50 (A) | +8-12 points |

---

*Transform vague requests into clear, high-scoring prompts! RCAF for simplicity. CLEAR for quality. Three formats for flexibility. Interactive Mode is DEFAULT. Every prompt measured. Every improvement quantified. User control is absolute.*