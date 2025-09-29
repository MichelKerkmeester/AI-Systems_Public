# AI Magic ✨

Some of my non-client AI systems that I made available to the public. They were designed to work with Claude, but you can tweak them to fit with other AI setups too.

> - 99.999% of people won't try these systems. Beat the odds?
> - Don't reward me with unwanted coffee: https://buymeacoffee.com/michelkerkmeester

-----

## 📋 Table of Contents

### 📝 Prompts

1. [DEV Workflows](#1-dev-workflows)
2. [Effective GPT](#2-effective-gpt)

### ✏️ Writer Systems

3. [Product Owner Writer](#3-product-owner-writer)
4. [Prompt Engineering Assistant](#4-prompt-engineering-assistant)
5. [AI System Improver (GPT & Claude)](#5-ai-system-improver-gpt--claude)

### 💬 MCP Agents

6. [Media Editor Agent](#6-media-editor-agent)
7. [Webflow Agent](#7-webflow-agent)
8. [ClickUp & Notion Agent](#8-clickup--notion-agent)

### ⚡ Automation Agents

9. [GPT - Scheduled Tasks](#9-gpt---scheduled-tasks)

### 🔧 Additional Sections

- [Common Features](#common-features)
- [Resources](#resources)

-----

## 📝 Prompts

→ Professional development workflows and system instructions

<a id="1-dev-workflows"></a>
#### 1. 📜 DEV Workflows

Systematic development workflows with Github SpecKit integration for reliable development.

- **Context Extractor**:
  - Auto-transforms user requests into structured CONTEXT/REQUEST snippets
  - Automatic workflow.yaml integration with [CONTEXT] and [REQUEST] replacements
  - Pattern recognition for URLs, file paths, error keywords, technical terms

- **Development Workflows**:
  - **Multiple Execution Modes**: Manual (full approvals), Automated (critical-only), Re-run (resume from any stage)
  - **SpecKit Commands**: /specify → /clarify → /plan → /tasks → /analyze → /implement
  - Progressive task checklists with validation checkpoints
  - Operating modes: Standard, Investigation, Hotfix, Performance (auto-selected by complexity)

- **Code Review & Debugger**:
  - **Debug-Test-Review Workflow**: Understand → Investigate → Debug → Fix → Test → Review
  - Chrome DevTools MCP integration for browser-based debugging
  - Evidence-based approach: Never assumes, validates everything with MCP tools
  - Mandatory staging verification before approval

.

<a id="2-effective-gpt"></a>
#### 2. 💬 Effective GPT

System instructions for direct, efficient AI communication without filler.

- **Core Communication Principles**:
  - Eliminates emojis, filler, hype, and conversational transitions
  - Blunt, directive phrasing focused on cognitive clarity
  - No engagement-boosting or sentiment-softening behaviors
  - Immediate termination after information delivery

- **Session Isolation & Privacy**:
  - Each conversation treated as new user
  - No continuity between sessions
  - No memory of past interactions

- **Language & Cultural Adaptations**:
  - Dutch exception: Softened rules with je/u formality
  - Responds in user's language automatically

-----

## ✏️ Writer Systems

→ Automate prompt, documentation, and ticket writing 

<a id="3-product-owner-writer"></a>
#### 3. 📋 Product Owner Writer

Create professional dev tickets and enhanced documentation.

- **4 Intelligent Modes & Auto-Scaling**:
  - Modes: $ticket & $prd (dev work), $doc (guides/formatting), $interactive (discovery), $quick (instant)
  - Auto-complexity for tickets: Simple (2-3), Standard (4-5), Complex (6-8 sections)

- **ATLAS Framework & Challenge Mode**:
  - 5-phase thinking with 6-10 rounds (user-controlled)
  - Auto-challenges at 6+ rounds: Constructive or Strong based on history
  - $quick mode: Zero waiting, 6 rounds auto, no challenges

.

<a id="4-prompt-engineering-assistant"></a>
#### 4. 🎯 Prompt Engineering Assistant

Transform vague requests into clear, measurable, high-scoring AI prompts with three format options.

- **RCAF Framework & CLEAR Evaluation**:
  - **RCAF**: Simple 4-element structure (Role, Context, Action, Format) - 70% usage
  - **CLEAR Scoring**: 5 dimensions (Correctness, Logic, Expression, Arrangement, Reuse)
  - Every prompt gets a score (0-50) and grade (F to A+)
  - Typical improvement: +20-25 points (100-200% gains)

- **7 Specialized Modes + Three Formats**:
  - Core: $interactive (DEFAULT), $short, $improve, $refine
  - Builder: $prototype, $website, $app (phased approach)
  - **Format Options**: Standard (baseline), YAML (templates, +3-7%), JSON (APIs, +5-10%)
  - Past chats integration for context-aware suggestions

- **ATLAS Framework with Challenge Mode**:
  - User-controlled thinking (1-10 rounds, always asked)
  - Challenge at 3+ rounds: "Could RCAF be simpler?"
  - Real example: "Summarize meeting" → 45/50 RCAF prompt (+30 points)
  - Commands: $rcaf (force simple), $craft (comprehensive), $yaml (templates), $json (APIs)
  
.

<a id="5-ai-system-improver-gpt--claude"></a>
#### 5. 🔧 AI System Improver (GPT & Claude)

Transform and improve AI system prompts across both GPT and Claude platforms with preservation-first editing.

- **Dual Platform Support**:
  - **GPT Version**: Uses GPT-5 High Deep Reasoning mode with ChatGPT custom instructions
  - **Claude Version**: Uses Ultrathink mode with Claude Projects knowledge base
  - Both versions share core ATLAS Framework and principles

- **Intelligent Analysis & Interactive Discovery**:
  - Auto-activates discovery for unclear requests (2-4 questions)
  - Complexity scoring determines ATLAS phases (A→S to Full ATLAS)
  - Challenge Mode at 6+ complexity score

- **Professional Delivery & Preservation**:
  - Complete files only (never excerpts)
  - Structural changes require explicit consent
  - Session tracking enriches but never restricts

-----


## 💬 MCP Agents

→ MCPs made easy with conversational systems

<a id="6-media-editor-agent"></a>
#### 6. 🎬 Media Editor Agent

Edit image, video, and audio files via natural language.

- **Universal Media Operations & Intelligence**:
  - Image: Resize, convert, compress, crop, batch
  - Video: Transcode, trim, overlay, subtitles
  - Audio: Extract, convert, normalize

- **MEDIA Framework & Challenge Mode**:
  - 5-phase: Measure/Evaluate/Decide/Implement/Analyze
  - Challenge at 3+ rounds ("85% quality, 50% smaller")
  - Commands: $reset, $standard, $quick, $status

- **Dual MCP Integration & Visual Feedback**:
  - Imagician MCP (Sharp), Video-Audio MCP (FFmpeg)
  - Progress bars, API indicators (🟢🟡🟠🔴)
  - Educational optimization insights

.

<a id="7-webflow-agent"></a>
#### 7. 🌐 Webflow Agent

Full-stack Webflow development through natural language with Designer and Data APIs.

- **Complete Development Capabilities**:
  - Create collections, fields, and relationships
  - Build components and design systems
  - User-controlled thinking depth (1-10 rounds)
  - ATLAS Framework with emergency commands ($reset, $status, $quick)

- **Designer + Data API Coordination**:
  - Visual elements with companion app
  - Structure creation without leaving Claude
  - Responsive designs and SEO optimization
  - REPAIR protocol for structured error recovery

- **Intelligent Pattern Learning**:
  - Adapts to your workflow preferences
  - Patterns inform but never restrict options
  - All capabilities always available
  - User autonomy is absolute

.

<a id="8-clickup--notion-agent"></a>
#### 8. 📊 ClickUp & Notion Agent

Seamlessly coordinate task management (ClickUp) and knowledge management (Notion) through natural language.

- **Dual-Platform Intelligence & MCP Verification**:
  - Notion: Databases, pages, rich content, wikis
  - ClickUp: Tasks, time tracking, sprints, projects
  - Always verifies MCP connections before operations

- **Platform Selection & SYNC Framework**:
  - Interactive mode asks which platform fits best
  - User-controlled thinking (1-10 rounds)
  - Challenge Mode at 3+ rounds for simplicity

- **Pattern Learning & Emergency Commands**:
  - Learns preferences but never restricts options
  - Commands: $reset, $quick, $status
  - Past chats integration for context

-----

## ⚡ Automation Agents

→ Create automated workflows with ease 

<a id="9-gpt---scheduled-tasks"></a>
#### 9. ⏰ GPT - Scheduled Tasks

Create scheduled tasks with intelligent optimization.

- **20+ Template Library & Natural Language**:
  - Morning Command (5 functions/1 slot), Weekly Intelligence (4/1)
  - Thinking: Quick (2-3), Standard (4-6), Deep (10-15), Maximum (15-20+)
  - Natural language input, test before commit

- **Smart Optimization & Canvas Documentation**:
  - Mandatory canvas README after first task
  - Visual tracking: ▓▓▓▓▓▓░░░░ (6/10 slots)
  - 2.0+ outcomes/slot target

- **ATLAS Framework & Pattern Learning**:
  - 5-phase thinking with 1-20+ rounds
  - Pattern detection after 3 similar requests
  - REPAIR error recovery

-----

<a id="common-features"></a>
## 🔧 Common Features

### MCP Integration

All systems support Model Context Protocol tools:

- **Domain-Specific**: Webflow, ClickUp, Notion, Media processing tools

### Intelligent Modes

- **Interactive Default**: Conversational guidance
- **Specialized Modes**: Task-specific approaches
- **Adaptive Complexity**: Scales to expertise

### Professional Output

- **Artifact Delivery**: Reusable, structured outputs
- **Visual Dashboards**: Progress and quality metrics
- **Documentation**: Every output includes guidance

.

<a id="resources"></a>
## 📚 Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Docker Desktop](https://docker.com/products/docker-desktop)
- [Claude Desktop](https://claude.ai/desktop)
- Individual system READMEs for detailed setup