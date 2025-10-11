# DEV - GPT 5 Pro - User Guide v0.100

A ChatGPT Projects system that simulates a complete development environment with enforced guardrails (AGENTS.md), comprehensive standards (Knowledge Base), and structured workflows (GitHub Spec Kit). Transforms requests into production-ready, properly numbered deliverables through a gated phase system.

## 📋 Table of Contents

- [Overview](#overview)
- [The Three Pillars](#the-three-pillars)
- [Environment Setup](#environment-setup)
- [How It Works](#how-it-works)
- [Workflow Phases](#workflow-phases)
- [Deliverable Standards](#deliverable-standards)
- [Version History](#version-history)

---

<a id="overview"></a>
## 🎯 Overview

This system replicates a professional development environment inside ChatGPT Projects by establishing:

1. **Behavioral Guardrails** (AGENTS.md) — Critical thinking checkpoints, anti-patterns, and decision frameworks
2. **Knowledge Standards** (Knowledge Base) — Code standards, patterns, platform constraints, and debugging guides
3. **Workflow Structure** (GitHub Spec Kit) — Templates and phases that ensure completeness from spec to summary

**Key Principle**: Output-only environment. No filesystem/terminal access. All deliverables as downloadable attachments (⬇️) with optional Canvas (📝) for review.

---

<a id="the-three-pillars"></a>
## 🏛️ The Three Pillars

### 1. AGENTS.md — Behavioral Guardrails

The "operating system" of the AI agent. Enforces:

- **Critical thinking checkpoints** before any code generation
- **Anti-pattern prevention** (rush to code, assumption-based changes, over-engineering)
- **Confidence gating** — Must ask clarifying questions if confidence < 80%
- **Scope discipline** — Solve only stated problems; no future-proofing
- **Evidence-based decisions** — Read code first, verify assumptions

**Rule Precedence**: AGENTS.md > System Instructions > Code Standards > User Requests

### 2. Knowledge Base — Development Standards

The "documentation library" that defines quality and patterns:

| Document | Purpose |
|----------|---------|
| `code_standards.md` | PRIMARY reference for all code quality decisions |
| `initialization_pattern.md` | Component/module initialization standards |
| `platform_constraints.md` | Webflow/platform-specific requirements |
| `collection_lists.md` | Data structure and collection patterns |
| `debugging.md` | Debugging strategies and troubleshooting |
| `animation_libraries.md` | Animation implementation standards |

**Core Principle**: code_standards.md is law. Consistency > personal preference.

### 3. GitHub Spec Kit — Workflow Templates

The "process framework" that structures all work:

```
Request → Spec → Plan → Tasks → Analysis → Code → Summary
  ↓        ↓      ↓       ↓        ↓         ↓       ↓
Phase   3-4    5      6       7      8-9    10-11
```

Each phase has a template that ensures completeness, traceability, and quality gates.

---

<a id="environment-setup"></a>
## 🚀 Environment Setup

### Prerequisites
- ChatGPT Plus or Enterprise account
- Access to Projects or Custom GPTs

### Installation Steps

**1. Create the Project**
```
ChatGPT → Projects → Create New Project
Name: "DEV - GPT 5 Pro" (or your preference)
```

**2. Upload AGENTS.md (Behavioral Guardrails)**
```
Knowledge Base/AGENTS.md → Upload to Project
```
This becomes the "operating system" that governs all AI behavior.

**3. Upload Knowledge Base (Development Standards)**
```
Knowledge Base/code_standards.md
Knowledge Base/initialization_pattern.md
Knowledge Base/platform_constraints.md
Knowledge Base/collection_lists.md
Knowledge Base/debugging.md
Knowledge Base/animation_libraries.md
```
These define what "quality" means for this project.

**4. Upload GitHub Spec Kit (Workflow Templates)**
```
Github Spec Kit/spec-template.md
Github Spec Kit/clarify.md
Github Spec Kit/plan-template.md
Github Spec Kit/tasks-template.md
Github Spec Kit/analyze.md
Github Spec Kit/agent-file-template.md
```
These structure the development workflow.

**5. Add Project Instructions**
```
Project Instructions - DEV - GPT 5 Pro.md → Upload to Project
```
This ties everything together and defines the execution model.

**6. Verify Setup**
Start a conversation with: "Status check: What documents do you have access to?"

---

<a id="how-it-works"></a>
## 🧠 How It Works

### Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Request Received                                         │
│    ↓                                                         │
│ 2. STOP - READ AGENTS.md FIRST (if not read this session)  │
│    ↓                                                         │
│ 3. Analyze Request (Parse, Context, Scope)                  │
│    ↓                                                         │
│ 4. Confidence Check                                         │
│    ├─ < 80%: Ask clarifying question                       │
│    └─ ≥ 80%: Proceed                                       │
│    ↓                                                         │
│ 5. Execute Workflow Phases (3-11)                          │
│    ├─ Each phase uses Spec Kit template                    │
│    ├─ Each deliverable follows code_standards.md           │
│    └─ Each file delivered as attachment (⬇️) + Canvas (📝) │
│    ↓                                                         │
│ 6. Integration Instructions & Completion Report            │
└─────────────────────────────────────────────────────────────┘
```

### Core Behaviors

**Always:**
- Read AGENTS.md before first action in session
- Follow code_standards.md for all code decisions
- Use Spec Kit templates for structured deliverables
- Deliver complete files only (line 1 → EOF)
- Include filepath header comment in all files
- Ask clarifying questions if confidence < 80%

**Never:**
- Provide code snippets or diffs
- Assume requirements without verification
- Over-engineer or future-proof beyond stated needs
- Skip phases or templates
- Access filesystem or terminal (output-only environment)

---

<a id="workflow-phases"></a>
## 📊 Workflow Phases

| Phase | Template | Deliverable | Format | Description |
|-------|----------|-------------|--------|-------------|
| **1-2** | — | Analysis | Chat | Parse request, gather context, assess scope |
| **3** | `spec-template.md` | `001 - spec-[name].md` | ⬇️📝 | Requirements specification |
| **4** | `clarify.md` | Updated `001` | ⬇️📝 | Clarifications and refinements |
| **5** | `plan-template.md` | `002 - plan-[name].md` | ⬇️📝 | Implementation plan + research docs |
| | | `002a - research-[topic].md` | ⬇️📝 | Supporting research (if needed) |
| | | `002b - data-model-[name].md` | ⬇️📝 | Data structures (if needed) |
| **6** | `tasks-template.md` | `003 - tasks-[name].md` | ⬇️📝 | Granular task breakdown |
| **7** | `analyze.md` | `004 - analysis-[name].md` | ⬇️📝 | Code analysis and architecture |
| **8** | — | Approval Gate | Chat | Review analysis, confirm approach |
| **9** | `agent-file-template.md` | `005+` code files | ⬇️📝 | Implementation files |
| **10** | — | `### - summary-[name].md` | ⬇️📝 | Implementation summary |
| **11** | — | Integration Guide | Chat | How to integrate into repo |

### Phase Gates

- **Phase 4**: User reviews spec, provides clarifications
- **Phase 8**: User approves analysis before implementation
- **Phase 11**: User receives integration instructions
---

<a id="version-history"></a>
## 📚 Version History

**v0.100** — Initial Release
- Established three-pillar architecture (AGENTS.md, Knowledge Base, Spec Kit)
- Defined 11-phase workflow with templates
- Implemented confidence gating and anti-pattern prevention
- Standardized deliverable numbering and file structure
- Output-only environment model with attachment delivery