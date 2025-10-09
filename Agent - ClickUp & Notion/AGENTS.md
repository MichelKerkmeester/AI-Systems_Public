# 🚨 CRITICAL - MANDATORY READING ORDER

**FOLLOW THE INSTRUCTIONS BELOW IMMEDIATELY.**

---

## ⚠️ SMART READING SEQUENCE - CONNECTION AWARE

This file serves as a redirect with intelligent routing based on user input and MCP connection status.
Follow this dynamic sequence:

### STEP 1: READ SYSTEM PROMPT FIRST ✅
MANDATORY: Read 
"/Knowledge Base/Agent - MCP - ClickUp & Notion - v0.101.md" COMPLETELY before proceeding.

This is your PRIMARY instruction set. Everything else supports this core system.

---

### STEP 2: VERIFY MCP CONNECTION BEFORE ANY OPERATION 🎯

ALWAYS FIRST: CONNECTION VERIFICATION
- BEFORE ANY OPERATION → Verify Notion and ClickUp MCP connections
- Test queries required → notion:API-get-self and clickup:get_workspace_hierarchy must succeed
- Failed connection → Apply REPAIR protocol immediately
- Success → Proceed with operation

CONNECTION STATE ROUTING:
- Connected ✓ → Proceed with operations
- Disconnected ✗ → Apply REPAIR → Cannot proceed
- Partial (only Notion or only ClickUp) → Offer scope-limited operations
- Auth/Setup failed → Re-authorization or installation required

---

### STEP 3: READ CORE FRAMEWORKS BASED ON NEED 📚

Read documents progressively as needed:

1) SYNC Thinking Framework — 
"/Knowledge Base/ClickUp & Notion - SYNC Thinking Framework - v0.101.md"
- ALWAYS READ (required for all operations)
- Automatic deep thinking: 10-round standard, 1–5 quick scaling

2) Interactive Intelligence — 
"/Knowledge Base/ClickUp & Notion - Interactive Intelligence - v0.101.md"
- DEFAULT conversational flow and UI patterns
- Adaptive questioning and feedback formats

3) MCP Intelligence — 
"/Knowledge Base/Notion - MCP Intelligence - v0.100.md"
"/Knowledge Base/ClickUp - MCP Intelligence - v0.100.md"
- Capabilities and limits of Notion and ClickUp servers
- Tool names, parameters, supported entities

4) Patterns & Workflows — 
"/Knowledge Base/ClickUp & Notion - Patterns & Workflows - v0.101.md"
- Operation templates, platform presets, and multi-step orchestration

---

## 🔁 READING FLOW DIAGRAM

```
START
	↓
[Read System Prompt v0.101]
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
[Read SYNC Framework]
	↓
[Read Interactive Intelligence] (if interactive/default)
	↓
[Read MCP Intelligence] (Notion and/or ClickUp)
	↓
[Read Patterns & Workflows] (if complex)
	↓
[Execute with MCP tools]
	↓
[Deliver Results]
```

---

## 🎯 OPERATION ROUTING GUIDE

### MCP/Platform Type Detection
| Request Type | Platform/MCP Needed | Requirements | Read |
|--------------|---------------------|--------------|------|
| "Create page/database" | Notion | Connection ✓ | MCP Intelligence (Notion) → Patterns |
| "Create tasks/project" | ClickUp | Connection ✓ | MCP Intelligence (ClickUp) → Patterns |
| "Knowledge base/wiki" | Notion | Connection ✓ | SYNC → MCP (Notion) → Patterns |
| "Project tracking" | ClickUp | Connection ✓ | SYNC → MCP (ClickUp) → Patterns |
| "Hybrid workflow" | Both | Connections ✓ | SYNC → Interactive → Patterns & Workflows |
| "Real-time sync" | REJECT | Native automation not supported | Offer alternatives |

### EXAMPLES

Simple Notion Operation:
```
User: "Create a database for content calendar"
→ Verify connections → SYNC → Notion doc → Patterns → Execute with 10-round deep thinking
```

ClickUp Project Setup:
```
User: "Set up a new project with lists and custom fields"
→ Verify connections → SYNC → ClickUp doc → Patterns → Execute with deep thinking
```

Connection Lost:
```
User: "Build a task system in ClickUp"
→ Verify connections → ClickUp ✗ → Apply REPAIR protocol → Cannot proceed → Offer setup guide and Notion-based alternative template
```

Unsupported Automation:
```
User: "Make Notion auto-sync with ClickUp in real time"
→ Verify connections → Detect unsupported request → REJECT
→ Offer native alternatives: mirrored structures, export/import flows, manual sync checklist
```

---

## 🎯 MODE/SHORTCUT DETECTION GUIDE

Recognize these commands:
| Command | Action | Resources to Read |
|---------|--------|-------------------|
| `$notion` | Notion operations | SYNC → MCP (Notion) → Patterns |
| `$clickup` | ClickUp operations | SYNC → MCP (ClickUp) → Patterns |
| `$quick` | Fast processing | SYNC (1–5 rounds) → MCP only |
| `$int`, `$interactive` | Force interactive mode | SYNC → Interactive → MCP |
| (no command) | Interactive default | SYNC → Interactive → MCP → Patterns |

Precedence when multiple commands provided:
1) Connection checks (always first)
2) Platform command ($notion/$clickup)
3) Speed mode ($quick)
4) Interactive default (when no mode)

---

## 📁 FILE ORGANIZATION - MANDATORY

ALL OUTPUT ARTIFACTS MUST BE PLACED IN:
```
/export/
```

File naming convention:
```
/export/[###] - cn-[platform]-[operation]-[description].md
```

Numbering Rules:
- ALWAYS prefix files with a 3-digit sequential number (001, 002, 003, …)
- Check existing files in /export/ to determine the next number
- Numbers must be zero-padded to 3 digits
- Use space-dash-space " - " separator after number

Examples:
- /export/001 - cn-notion-database-content-calendar.md
- /export/002 - cn-clickup-project-setup-marketing.md
- /export/003 - cn-notion-wiki-knowledge-base.md
- /export/004 - cn-hybrid-workflow-docs-and-tasks.md

---

## ⛔ ABSOLUTE REQUIREMENTS

DO NOT:
- ✗ Skip the system prompt ("/Knowledge Base/Agent - MCP - ClickUp & Notion - v0.101.md")
- ✗ Proceed without successful MCP connection checks
- ✗ Promise real-time cross-platform sync
- ✗ Use horizontal dividers in user-facing responses
- ✗ Exceed 60 API/tool calls per minute
- ✗ Ignore REPAIR protocol on errors
- ✗ Promise operations not supported by MCP servers

ALWAYS:
- ✓ Verify MCP connections BEFORE any operation
- ✓ Run test queries (notion:API-get-self, clickup:get_workspace_hierarchy)
- ✓ Apply SYNC methodology (10-round standard; 1–5 quick)
- ✓ Use ONLY native MCP tools (Notion, ClickUp)
- ✓ Provide clean bullet-list visual feedback and metrics
- ✓ Respect rate limits (50/60 safe operating)
- ✓ Place artifacts in /export with correct numbering

---

## ☑️ QUICK VERIFICATION

Before responding to ANY request, confirm:

- [ ] Have I read the system prompt completely?
- [ ] Did I verify MCP connections FIRST?
- [ ] Did the test queries succeed (or was the user guided to setup)?
- [ ] Did I apply SYNC methodology at the correct depth?
- [ ] Am I using ONLY Notion/ClickUp MCP tools?
- [ ] Will I provide bullet-list feedback with metrics?
- [ ] Will artifacts go in /export with the next sequential number (###)?

IF ANY ANSWER IS NO → GO BACK TO STEP 1

---

## 🚀 EFFICIENCY BENEFITS

This smart routing ensures:
- Connection reliability — Verify before every operation
- Automatic excellence — SYNC deep thinking by default
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
4) SYNC Framework — Structured automatic thinking
5) Interactive Intelligence — Default flow when conversational
6) MCP Intelligence — Tool capabilities and parameters
7) Patterns & Workflows — For complex or multi-step tasks
8) Native MCP Tools ONLY — No real-time sync generation
9) Output to /export — Every artifact goes here

→ GO TO: "/Knowledge Base/Agent - MCP - ClickUp & Notion - v0.101.md" NOW
