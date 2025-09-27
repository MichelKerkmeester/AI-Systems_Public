# Prompt Engineering Assistant - User Guide v0.884

A revolutionary prompt enhancement system using RCAF framework for clarity, CLEAR evaluation for quality assurance, and ATLAS thinking for intelligent optimization. Transforms vague requests into clear, measurable, high-scoring prompts with support for Standard, JSON, and YAML formats. **Now with 100% user autonomy through mandatory wait states at all decision points.**

## 📋 Table of Contents

- [🆕 What's New in v0.884](#whats-new-in-v0884)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🔄 Format Options](#format-options)
- [🧠 ATLAS Thinking Framework](#atlas-thinking-framework)
- [🚀 Challenge Mode Philosophy](#challenge-mode-philosophy)
- [⭐ RCAF Framework](#rcaf-framework)
- [✅ CLEAR Evaluation System](#clear-evaluation-system)
- [🚨 REPAIR Error Protocol](#repair-error-protocol)
- [📊 Performance Metrics](#performance-metrics)
- [🗃️ Past Chats Integration](#past-chats-integration)

.

<a id="whats-new-in-v0884"></a>
## 🆕 What's New in v0.884

### CRITICAL UPDATE: 100% User Autonomy 🎯
**The system now WAITS for explicit user input at EVERY decision point. No automatic selections. No pattern-based assumptions. Complete user control.**

### Mandatory Wait States Implemented
- **Thinking Rounds**: ALWAYS waits for user input (1-10)
- **Challenge Response**: ALWAYS waits when presenting options (3+ rounds)
- **Framework Selection**: ALWAYS waits for user choice (5-6 rounds)
- **Format Preference**: ALWAYS waits for user selection

### User Control Enhancements
- **Patterns as Suggestions Only**: Historical patterns NEVER force choices
- **Override Always Available**: User can ignore all suggestions
- **Explicit Wait Messages**: Clear "[WAITING FOR YOUR INPUT]" indicators
- **No Auto-Progression**: System blocks until user responds

### Framework Selection at Complexity 5-6
```
**Framework Selection Required:**

Option A: RCAF (4 elements, clearer)
Option B: CRAFT (5 elements, comprehensive)

Which framework? (A or B)
[WAITING FOR YOUR FRAMEWORK CHOICE]
```

### Challenge Mode Always Waits
```
**Enhancement Options:**

Option A: Minimal (1-2 rounds)
Option B: Standard (3-4 rounds)  
Option C: Comprehensive (5+ rounds)

Please select: (A, B, or C)
[WAITING FOR YOUR SELECTION]
```

### System Improvements from v0.840
- **Enforced Checkpoints**: Cannot proceed without user input
- **Pattern Override Safeguards**: Suggestions never restrict options
- **Enhanced Error Recovery**: Detects missing wait states
- **Compliance Tracking**: 100% wait state enforcement

.

<a id="key-features"></a>
## ✨ Key Features

### NEW: Mandatory Wait States
- **100% User Control**: System WAITS at every decision point
- **No Auto-Selection**: Patterns suggest but NEVER choose
- **Explicit Confirmations**: Clear wait messages at each step
- **Override Always Available**: Ignore any suggestion freely

### Core Features
- **Interactive Mode DEFAULT**: System always starts with guided discovery
- **Three Format Options**: Standard (clarity), YAML (templates), JSON (APIs)
- **RCAF Framework**: Simple 4-element structure for 70% of prompts
- **CLEAR Scoring**: Every prompt evaluated on 5 dimensions
- **Past Chats Integration**: Searches conversation history for context (suggestions only)
- **MANDATORY Thinking Rounds**: 1-10 - always asked, always waits
- **Token Transparency**: Shows format overhead for informed decisions
- **Challenge Mode**: Simplifies to RCAF when possible (waits for acceptance)
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
3. Copy and paste: `Writer - Prompt Improver - v0.884.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project's knowledge base:

**Core System Documents:**
- `Prompt - ATLAS Thinking Framework - v0.206.md`
- `Prompt - Interactive Mode - v0.616.md`
- `Prompt - Artifact Standards & Templates.md`
- `Prompt - Patterns & Enhancements.md`
- `Prompt - Evaluation & Refinement.md`

**Format Documents:**
- `Prompt - JSON Format Guide.md`
- `Prompt - YAML Format Guide.md`

**Mode Documents:**
- `Prompt - Builder Mode.md`

### Step 4: Experience User Control
```
write about dogs              # Interactive Mode - ALL waits enforced
$improve analyze data         # Will wait for rounds, challenge, format
$yaml create config          # Will wait for rounds and confirmation
$json api endpoint           # Will wait for all inputs
$clear                       # Show current CLEAR scores
```

.

<a id="operating-modes"></a>
## 🎛️ Operating Modes

### Core Modes with Wait States

| Mode | Activation | Best For | Framework | CLEAR Target | Wait States Required |
|------|------------|----------|-----------|--------------|---------------------|
| **Interactive** | DEFAULT | Discovery | RCAF focus | 40+/50 | ALL: rounds, challenge, framework, format |
| **$short** | `$short`/`$s` | Simple clarity | RCAF | 35+/50 | Rounds + Format |
| **$improve** | `$improve`/`$i` | Most improvements | RCAF | 40+/50 | Rounds + Challenge + Format |
| **$refine** | `$refine`/`$r` | Maximum quality | RCAF/CRAFT | 43+/50 | Rounds + Challenge + Format |
| **$builder** | `$builder`/`$b` | Platform prompts | RCAF | 40+/50 | Rounds + Challenge + Format |
| **$json** | `$json`/`$j` | API format | RCAF | 38+/50 | Rounds + Challenge (3+) |
| **$yaml** | `$yaml`/`$y` | Config/templates | RCAF | 40+/50 | Rounds + Challenge (3+) |

### User Input Flow Example
```
User: $improve my prompt
System: How many thinking rounds? (1-10)
        [WAITING FOR YOUR INPUT]
User: 4
System: Since you chose 4 rounds, enhancement options:
        A: Minimal  B: Standard  C: Comprehensive
        [WAITING FOR YOUR SELECTION]
User: B
System: Which format would you prefer?
        1: Standard  2: YAML  3: JSON
        [WAITING FOR YOUR FORMAT PREFERENCE]
User: 1
System: [Creates enhancement with all user choices]
```

.

<a id="format-options"></a>
## 🔄 Format Options

### Three Format System - User Selects

| Format | Token Impact | Best For | CLEAR Average | User Wait |
|--------|--------------|----------|---------------|-----------|
| **Standard** | Baseline | Natural language, clarity | 43/50 | Always |
| **YAML** | +3-7% | Templates, config, human-editable | 42/50 | Always |
| **JSON** | +5-10% | APIs, structured data | 41/50 | Always |

### Format Selection Process
```
System presents all three options
↓
Shows token impact and use cases
↓
[WAITING FOR YOUR FORMAT PREFERENCE]
↓
User selects 1, 2, or 3
↓
System applies chosen format
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

### User-Controlled Process (v0.206)
```
How many thinking rounds would you like? (1-10)
[WAITING FOR YOUR INPUT - Cannot proceed]

Based on your request, I recommend: 5 rounds
• Clarity: Medium - needs structure
• Complexity: Moderate - borderline
• Enhancement: Standard improvement

Your choice: 5

At 5 rounds, you must choose framework:
A: RCAF (4 elements, clearer)
B: CRAFT (5 elements, comprehensive)
[WAITING FOR YOUR FRAMEWORK CHOICE]

Your choice: A

Format options:
1. Standard (baseline) - maximum clarity
2. YAML (+3-7%) - template-ready
3. JSON (+5-10%) - API-ready
[WAITING FOR YOUR FORMAT PREFERENCE]

Your choice: 1

Projected CLEAR: 42/50 (Grade: A)
```

### Framework Phases with CLEAR
- **A** - Assess & score baseline CLEAR
- **T** - Transform with RCAF/CRAFT choice (WAITS at 5-6)
- **L** - Layer targeting weak CLEAR dimensions
- **A** - Assess CLEAR improvements
- **S** - Synthesize with final CLEAR scores

.

<a id="challenge-mode-philosophy"></a>
## 🚀 Challenge Mode Philosophy

> "RCAF's 4 elements beat CRAFT's 5. Expression beats Coverage. Start simple. **User decides.**"

### CLEAR-Based Challenges with Wait States

| CLEAR Score | Challenge Level | Action | Wait Required |
|-------------|----------------|--------|---------------|
| 45-50 | None | Ship it | No |
| 40-44 | Gentle | "Could RCAF improve Expression?" | Yes |
| 35-39 | Moderate | "RCAF would gain +3 clarity" | Yes |
| 30-34 | Strong | "Switch to RCAF for +5 points" | Yes |
| <30 | Aggressive | "Must use RCAF" | Yes |

### Challenge Format Template
```markdown
**Enhancement Options:**

Option A: Minimal (RCAF essential)
Option B: Standard (RCAF full)
Option C: Comprehensive (CRAFT if needed)

[Pattern suggests Option B - suggestion only]

Please select: (A, B, or C)
[WAITING FOR YOUR SELECTION]
```

.

<a id="rcaf-framework"></a>
## ⭐ RCAF Framework

### The Essential Four Elements

**Role, Context, Action, Format** - Maximum clarity with minimum complexity

**User Choice at Complexity 5-6**: System WAITS for explicit RCAF vs CRAFT selection

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
| 30-34 | C | Major improvement | Switch to RCAF (with user consent) |
| 25-29 | D | Significant revision | Force RCAF |
| <25 | F | Complete rewrite | RCAF required |


.

<a id="repair-error-protocol"></a>
## 🚨 REPAIR Error Protocol

Enhanced error recovery with wait state validation:
- **R**ecognize issue (check for missing waits)
- **E**xplain impact (show what's missing)
- **P**ropose alternatives (request missing input)
- **A**dapt approach (WAIT for response)
- **I**terate and test (verify all collected)
- **R**ecord pattern (track for future)

### Common Fixes with Wait States

| Issue | Recognition | Fix | Wait State |
|-------|------------|-----|------------|
| No thinking rounds | Missing input | STOP & ASK | ENFORCED |
| No challenge response | Missing at 3+ | STOP & ASK | ENFORCED |
| No framework choice | Missing at 5-6 | STOP & ASK | ENFORCED |
| No format selection | Missing preference | STOP & ASK | ENFORCED |
| Pattern forcing | Auto-selection | Present as suggestion | Override available |

.

<a id="performance-metrics"></a>
## 📊 Performance Metrics

### System Performance with User Control

| Metric | Target | Current | Notes |
|--------|--------|---------|-------|
| **Wait State Compliance** | 100% | 100% | All decisions wait |
| **User Override Rate** | Available | 100% | Always can override |
| **Average CLEAR Score** | 40+/50 | 43/50 | With user choices |
| **RCAF Usage Rate** | 70% | 72% | User selected |
| **Expression Average** | 9+/10 | 9.2/10 | RCAF benefit |
| **First-Pass Success** | 80% | 85% | After all inputs |

### Wait State Performance

| Decision Point | Wait Enforcement | User Control | Compliance |
|----------------|-----------------|--------------|------------|
| **Thinking Rounds** | 100% | Full | 100% |
| **Challenge (3+)** | 100% | Full | 100% |
| **Framework (5-6)** | 100% | Full | 100% |
| **Format Selection** | 100% | Full | 100% |

### Format Performance with User Choice

| Format | Usage Rate | Avg CLEAR | Selected By User |
|--------|------------|-----------|------------------|
| **Standard** | 55-65% | 43/50 | 100% explicit |
| **YAML** | 20-25% | 42/50 | 100% explicit |
| **JSON** | 15-20% | 41/50 | 100% explicit |

### Typical Improvements (After User Inputs)

| Starting Score | Typical Result | Improvement | User Decisions |
|---------------|----------------|-------------|----------------|
| <20/50 (F) | 40-45/50 (A) | +20-25 points | 3-4 choices |
| 20-29/50 (D) | 38-43/50 (B+/A) | +15-20 points | 3-4 choices |
| 30-39/50 (C/B) | 40-45/50 (A) | +8-12 points | 2-3 choices |

.

<a id="past-chats-integration"></a>
## 🗃️ Past Chats Integration

### Context Enhancement - SUGGESTIONS ONLY

The system uses two tools to search conversation history:
- **conversation_search**: Topic/keyword-based search
- **recent_chats**: Time-based retrieval

| Stage | Interactions | Context Level | User Override |
|-------|-------------|---------------|---------------|
| Learning | 1-3 | Basic notes | Always available |
| Adapting | 4-6 | Light suggestions | Always available |
| Enriched | 7-9 | Detailed patterns | Always available |
| Comprehensive | 10+ | Maximum context | Always available |

### What Gets Tracked (Suggestions Only)
- Framework preferences (RCAF vs CRAFT) - never forces
- Format preferences (Standard/YAML/JSON) - never defaults
- Average CLEAR scores by dimension - for reference
- Typical complexity levels - as context
- Challenge acceptance rates - for calibration
- Weak dimension patterns - to help improve

**CRITICAL**: Patterns are ALWAYS presented as suggestions. User can always:
1. Follow suggestions
2. Make fresh choices
3. Disable pattern display

---

*Transform vague requests into clear, high-scoring prompts with 100% user control! System WAITS at every decision point. Patterns suggest but NEVER force. RCAF for simplicity. CLEAR for quality. Three formats for flexibility. Interactive Mode is DEFAULT. Every prompt measured. Every improvement quantified. **User autonomy is absolute through enforced wait states.***