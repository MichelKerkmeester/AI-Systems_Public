## 🚨 CRITICAL - MANDATORY READING ORDER

FOLLOW THE INSTRUCTIONS BELOW IMMEDIATELY.

---

## ⚠️ SMART READING SEQUENCE - CONNECTION AWARE

This file serves as a redirect with intelligent routing based on user intent and system state.
Follow this dynamic sequence:

### STEP 1: READ SYSTEM PROMPT FIRST ✅
MANDATORY: Read 
"/Knowledge Base/Agent - MCP - Media Editor - v0.114.md" COMPLETELY before proceeding.

This is your PRIMARY instruction set. Everything else supports this core system.

---

### STEP 2: VERIFY MCP CONNECTION BEFORE ANY OPERATION 🎯

ALWAYS FIRST: CONNECTION VERIFICATION
- BEFORE ANY OPERATION → Verify MCP server connections
- Test queries required → imagician:list_images and video-audio:health_check must succeed
- Failed connection → Apply REPAIR protocol immediately
- Success → Proceed with operation

CONNECTION STATE ROUTING:
- Connected ✓ → Proceed with operations
- Disconnected ✗ → Apply REPAIR → Cannot proceed
- Partial (only images or only video/audio) → Offer scope-limited operations
- Auth/Setup failed → Re-authorization or installation required

---

### STEP 3: READ CORE FRAMEWORKS BASED ON NEED 📚

Read documents progressively as needed:

1) MEDIA Thinking Framework — 
"/Knowledge Base/Media Editor - MEDIA Thinking Framework - v0.104.md"
- ALWAYS READ (required for all operations)
- Automatic deep thinking: 10-round standard, 1–5 quick scaling

2) Interactive Intelligence — 
"/Knowledge Base/Media Editor - Interactive Intelligence - v0.104.md"
- DEFAULT conversational flow and UI patterns
- Adaptive questioning and feedback formats

3) MCP Intelligence — 
"/Knowledge Base/Media Editor - MCP Intelligence - Imagician - v0.104.md"
"/Knowledge Base/Media Editor - MCP Intelligence - Video, Audio - v0.104.md"
- Capabilities and limits of image (Imagician) and media (Video-Audio) servers
- Tool names, parameters, supported formats

4) Patterns & Workflows — 
"/Knowledge Base/Media Editor - Patterns & Workflows - v0.104.md"
- Operation templates, platform presets, and multi-step orchestration

---

## 🔁 READING FLOW DIAGRAM

```
START
	↓
[Read System Prompt v0.114]
	↓
[VERIFY MCP CONNECTION] ← CRITICAL FIRST STEP
	↓
Connection OK? —— NO ——→ [Apply REPAIR Protocol]
	│                         ↓
	│                    [Cannot Proceed]
	│
	YES
	↓
[Detect Mode / User Intent]
	↓
[Read MEDIA Framework]
	↓
[Read Interactive Intelligence] (if interactive/default)
	↓
[Read MCP Intelligence] (Imagician and/or Video-Audio)
	↓
[Read Patterns & Workflows] (if complex)
	↓
[Execute with MCP tools]
	↓
[Deliver Results]
```

---

## 🎯 MODE/SHORTCUT DETECTION GUIDE

Recognize these commands:
| Command | Action | Resources to Read |
|---------|--------|-------------------|
| `$image`, `$img` | Image operations | MEDIA → MCP (Imagician) → Patterns |
| `$video`, `$vid` | Video operations | MEDIA → MCP (Video-Audio) → Patterns |
| `$audio`, `$aud` | Audio operations | MEDIA → MCP (Video-Audio) → Patterns |
| `$quick` | Fast processing | MEDIA (1–5 rounds) → MCP only |
| `$int`, `$interactive` | Force interactive mode | MEDIA → Interactive → MCP |
| (no command) | Interactive default | MEDIA → Interactive → MCP → Patterns |

Precedence when multiple commands provided:
1) Connection checks (always first)
2) Mode command ($image/$video/$audio)
3) Speed mode ($quick)
4) Interactive default (when no mode)

### EXAMPLES

Format-Specific Mode:
```
User: "$image convert to webp and optimize"
→ Verify connections → MEDIA → Imagician → Patterns → Execute → Report
```

Quick Mode:
```
User: "$quick compress this mp4"
→ Verify connections → MEDIA (auto 1–5 rounds) → Video-Audio → Execute → Report
```

Interactive Default:
```
User: "make this smaller"
→ Verify connections → MEDIA → Interactive questions → MCP tools → Report
```

Partial Connectivity:
```
User: "extract audio and create thumbnails"
→ Verify connections → Only Imagician ✓, Video-Audio ✗
→ Offer: proceed with thumbnails now; provide setup guide for audio
```

---

## 📁 FILE ORGANIZATION - MANDATORY

ALL OUTPUT ARTIFACTS MUST BE PLACED IN:
```
/export/
```

File naming convention:
```
/export/[###] - media-[type]-[operation]-[description].md
```

Numbering Rules:
- ALWAYS prefix files with a 3-digit sequential number (001, 002, 003, …)
- Check existing files in /export/ to determine the next number
- Numbers must be zero-padded to 3 digits
- Use space-dash-space " - " separator after number

Examples:
- /export/001 - media-image-convert-webp-hero.md
- /export/002 - media-video-compress-1080p-web.md
- /export/003 - media-audio-extract-mp3-podcast.md
- /export/004 - media-multipack-social-instagram-tiktok.md

---

## ⛔ ABSOLUTE REQUIREMENTS

DO NOT:
- ✗ Skip the system prompt ("/Knowledge Base/Agent - MCP - Media Editor - v0.114.md")
- ✗ Proceed without successful MCP connection checks
- ✗ Generate new content (no AI image/video/audio generation)
- ✗ Use horizontal dividers in user-facing responses
- ✗ Exceed 60 API/tool calls per minute
- ✗ Ignore REPAIR protocol on errors
- ✗ Promise operations not supported by MCP servers

ALWAYS:
- ✓ Verify MCP connections BEFORE any operation
- ✓ Run test queries (imagician:list_images, video-audio:health_check)
- ✓ Apply MEDIA methodology (10-round standard; 1–5 quick)
- ✓ Use ONLY native MCP tools (Imagician, Video-Audio)
- ✓ Provide clean bullet-list visual feedback and metrics
- ✓ Respect safe operating rate limits (target ≤50/60)
- ✓ Place artifacts in /export with correct numbering

---

## ☑️ QUICK VERIFICATION

Before responding to ANY request, confirm:

- [ ] Have I read the system prompt completely?
- [ ] Did I verify MCP connections FIRST?
- [ ] Did the test queries succeed (or was the user guided to setup)?
- [ ] Did I apply MEDIA methodology at the correct depth?
- [ ] Am I using ONLY Imagician/Video-Audio MCP tools?
- [ ] Will I provide bullet-list feedback with metrics?
- [ ] Will artifacts go in /export with the next sequential number (###)?

IF ANY ANSWER IS NO → GO BACK TO STEP 1

---

## 🚀 EFFICIENCY BENEFITS

This smart routing ensures:
- Connection reliability — Verify before every operation
- Automatic excellence — MEDIA deep thinking by default
- Faster processing — Only read what’s needed
- Error recovery — Structured REPAIR protocol
- Better UX — Clear, consistent feedback
- Quality assurance — Professional defaults and safeguards

Failure to follow this smart sequence will result in:
- Connection failures and broken operations
- Unsupported promises and user frustration
- Rate-limit violations
- Poor error handling
- Artifacts in wrong location or misnumbered

---

## ⚠️ REMEMBER THE HIERARCHY

1) Connection Verification FIRST — Always before operations
2) System Prompt — Read completely
3) Test Queries — Must pass before proceeding
4) MEDIA Framework — Structured automatic thinking
5) Interactive Intelligence — Default flow when conversational
6) MCP Intelligence — Tool capabilities and parameters
7) Patterns & Workflows — For complex or multi-step tasks
8) Native MCP Tools ONLY — No content generation
9) Output to /export — Every artifact goes here

→ GO TO: "/Knowledge Base/Agent - MCP - Media Editor - v0.114.md" NOW
