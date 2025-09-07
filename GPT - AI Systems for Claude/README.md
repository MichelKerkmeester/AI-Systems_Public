# GPT - AI System Improver for Claude Projects - User Guide v1.0.0

The GPT Improver transforms requests into professional Claude system artifacts through intelligent interactive guidance with built-in complexity challenging. By focusing on WHAT the artifact must achieve and WHY it matters, and by preserving structure and length by default, it produces lean, high-quality outputs that strengthen Claude projects.

.

## 📋 Table of Contents

- [🆕 What's New in v1.0.0 - Initial Release](#-whats-new-in-v100---initial-release)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 ATLAS Thinking Framework](#-atlas-thinking-framework)
- [🎯 Automatic Complexity Detection](#-automatic-complexity-detection)
- [🗃️ Past Chats Integration](#️-past-chats-integration)
- [⚡ Emergency Commands](#-emergency-commands)
- [🔄 Challenge Mode](#-challenge-mode)
- [📦 Version History](#-version-history)
- [📚 Additional Resources](#-additional-resources)

.

## 🆕 What's New in v1.0.0 - Initial Release

### Initial Release Highlights
- **Preservation-first editing**: Keeps original section order and approximate length unless you approve changes.
- **Consent checkpoints**: Asks before removing, adding, or restructuring core sections.
- **Interactive intelligence**: Short, targeted questions, options menu, and clear confirm steps.
- **Canvas delivery**: One ChatGPT Canvas artifact per turn with embedded Markdown and optional status card.
- **History as notes**: Uses patterns as informative context, never as restrictions.
- **Challenge Mode**: Gentle to Strong simplification prompts based on request complexity.

.

## ✨ Key Features

### Core Capabilities
- **Preserve by default**: Improve wording, safety cues, and clarity without structural change.
- **Ask before breaking changes**: Gain explicit approval for structural edits or significant deletions.
- **Options menu**: Minimal, Standard, or Comprehensive pass, with token impact explained when relevant.
- **Canvas-first delivery**: Single artifact per response, Markdown embedded, ready to copy into Claude Projects.
- **History-aware**: Displays helpful notes learned from prior sessions, never reduces available options.
- **REPAIR protocol**: Recognize, Explain, Propose options, Adapt, Iterate, Record for robust error handling.

### Professional Standards
- **Clear vendor semantics**: Uses Claude terminology and refusal patterns, qualifies uncertain capability claims.
- **Outcome focus**: WHAT and WHY over HOW, with optional test prompts for validation.
- **Quality gates**: Consent, preservation, clarity, safety, and traceability checks before delivery.
- **Visual feedback**: Optional status card and “What changed” section on request.

---

## 🚀 Quick Setup

### Step 1: Create a custom GPT in ChatGPT
1. Open ChatGPT, create a new GPT.
2. Name it **GPT - AI System Improver for Claude Projects**.

### Step 2: Add System Instructions
1. Paste the system prompt for the Improver.
2. Enable “Always respond in Canvas” behavior.

### Step 3: Attach Reference Docs
Upload the Claude-related artifacts you want preserved and improved, for example:
- System prompts, safety policies, red teaming rubrics, evaluation sheets, workflows, integration briefs.

### Step 4: Start a Session
Use natural language, no modes required:
```

Improve this Claude system prompt, keep structure and length.
Create a safety addendum, preserve policy intent.
Refactor this workflow for clarity, do not add steps without approval.

```

.


## 🧠 ATLAS Thinking Framework

ATLAS provides the structured reasoning behind improvements and challenges. You will experience ATLAS through:
- Focused questions instead of long forms.
- Clear tradeoffs via the options menu.
- Consent prompts before structural change.
- A concise, high-signal artifact at the end.

For full detail, see the separate **ATLAS Framework** document.

.

## 🎯 Automatic Complexity Detection

The Improver scales its interaction based on the edit type it detects.

| Indicators in your request | Detected scope | Default action | Consent needed |
|---|---|---|---|
| “Tighten wording”, “clarify”, “qualify claims” | **Simple** | Minimal pass, preserve sections and length | No |
| “Improve safety cues”, “add test prompts”, “organize subsections” | **Standard** | Standard pass, improve within existing scaffold | No |
| “Restructure”, “remove sections”, “merge docs”, “split into phases” | **Comprehensive** | Proposes structural change with rationale | Yes, explicit |

**Consent script used for structural changes**
```

Request: \[change type]
Impact: structure, length, semantics
Benefit: \[why this helps]
Proceed yes or no

```

.

## 🗃️ Past Chats Integration

### How It Enhances Interaction
- Surfaces helpful context like “you usually prefer Minimal pass” or “you often keep safety bullets verbatim.”
- Suggests defaults as notes only.
- Never skips questions or removes options due to history.

### Context Journey
| Stage | Interactions | What You See | Options |
|---|---|---|---|
| Learning | 1–3 | Clean interactive flow | All available |
| Adapting | 4–6 | Brief historical notes | All available |
| Enriched | 7–9 | Pattern suggestions | All available |
| Comprehensive | 10+ | Rich context summaries | All available |

.

## ⚡ Emergency Commands

Quick control without leaving the interactive flow.

| Command | Action | Result | Use When |
|---|---|---|---|
| **`$reset`** | Clear historical influence | Fresh session, no context notes | New topic or context feels wrong |
| **`$standard`** | Ignore patterns | Pure interaction, no history suggestions | You want a clean pass |
| **`$quick`** | Fast track | Skips discovery, still asks for consent when needed | You know exactly what you want |
| **`$status`** | Show context | Displays what patterns are influencing notes | Transparency and debugging |

**Hint**: You can use these at any time.

.

## 🔄 Challenge Mode

The Improver challenges complexity when risk of overengineering is detected.

**Levels**
- **Gentle**: “Could we achieve the intent with wording only”
- **Constructive**: “Keep structure, add safety cues and tests, skip new sections”
- **Strong**: “Split or defer, evidence suggests minimal change meets goals”

**Sample challenge**
```

Quick thought before proceeding.

Option A: Minimal pass: qualify claims and tighten safety lines
Option B: Standard pass: A plus refusal phrasing and test prompts
Option C: Comprehensive pass: B plus structural edits and evaluation rubric

Which fits your intent A, B, or C

```

.

## 📦 Version History

### v1.0.0
- Preservation-first editing with consent checkpoints
- Single interactive flow, no modes
- Options menu with Minimal, Standard, Comprehensive passes
- Canvas-first delivery with optional status card
- History as informative notes, never constraints
- Challenge Mode for clarity and scope control
- REPAIR protocol for robust error handling

---

**GPT - AI System Improver for Claude Projects** keeps you in control. It preserves structure and length by default, asks for consent before fundamental changes, challenges unnecessary complexity, and delivers a single, polished Canvas artifact you can drop directly into your Claude project.