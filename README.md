# AI Magic ✨

Some of my non-client AI systems that I made available to the public. They were designed to work with Claude, but you can tweak them to fit with other AI setups too.

> - 99.999% of people won’t try these systems. Beat the odds?
> - Don’t reward me with unwanted coffee: https://buymeacoffee.com/michelkerkmeester

-----

## 📋 Table of Contents

<<<<<<< HEAD
### 💬 MCP Agents

1. [Media Editor Agent](#1-media-editor-agent)
1. [Webflow Agent](#2-webflow-agent)
1. [ClickUp & Notion Agent](#3-clickup--notion-agent)

### ✏️ Writer Systems

1. [Product Owner Writer](#4-product-owner-writer)
1. [Branded Content Writer](#5-branded-content-writer)
1. [Prompt Engineering Assistant](#6-prompt-engineering-assistant)
1. [GPT - AI System Improver](#7-gpt---ai-system-improver)

### ⚡ Automation Agents

1. [GPT - Scheduled Tasks](#8-gpt---scheduled-tasks)

### 🔧 Additional Sections

- [Common Features](#common-features)
- [Resources](#resources)

-----
=======
### ✏️ Writer Systems
1. [Branded Content Writer](#1--branded-content-writer)
2. [Product Owner Writer](#2--product-owner-writer)
3. [Prompt Engineering Assistant](#3--prompt-engineering-assistant)
4. [GPT - AI System Improver](#4--gpt---ai-system-improver)

### ⚡ Automation Agents  
5. [GPT - Scheduled Tasks](#5--gpt---scheduled-tasks)

### 💬 MCP Agents
6. [Media Editor Agent](#6--media-editor)
7. [Webflow Agent](#7--webflow-agent)
8. [ClickUp Agent](#8--clickup-agent)
9. [Notion Agent](#9--notion-agent)

### 🔧 Additional Sections
- [Common Features](#-common-features)
- [Installation](#-installation)
- [Choosing the Right System](#-choosing-the-right-system)
- [Resources](#-resources)

---

## ✏️ Writer Systems
##### Automated content, documentation & prompt writing systems
——

#### 1. ✏️ Branded Content Writer - v5.6.0 
**Flexible content system with historical context enrichment, adaptable for any brand, profession, or personal writing**

- **Adaptable System & Current Configuration**: 
  - Currently set for Product Designers: case studies, process docs, design insights
  - Easily reconfigured for: Marketing, engineering, education, healthcare, personal blogs
  - Built-in knowledge base (currently Product Design - replaceable with your domain)

- **5 Interactive Modes & 6 Tone Variations (All Always Available)**: 
  - Modes: $interactive (guided default), $write (general), $share (knowledge), $teach (educational), $reflect (analysis)
  - Tones: $natural (conversational), $technical (precise), $collaborative (team), $educational (clear), $reflective (thoughtful), $minimal (essential)

- **DEPTH Framework & Context Enhancement**: 
  - User-controlled thinking depth (1-10 rounds) - always asked, never automated
  - Challenge Mode at 3+ thinking rounds for simplification (both options always shown)
  - Emergency commands: $reset (clear context), $standard (default flow), $quick (fast creation), $status (show patterns)

.

#### 2. 📋 Product Owner Writer - v8.7.0 
**Transform vague requests into professional dev tickets, specs, docs, and beautifully formatted documents with built-in complexity challenging**

- **5 Intelligent Modes & Auto-Scaling**: 
  - Core modes: $ticket (dev), $spec (frontend), $doc (guides), $text (snippets), $beautify (document formatting)
  - Auto-complexity: Simple (bugs 2-3 sections), Standard (features 4-5), Complex (platforms 6-8)
  - Feature complete: 6 core system files + 5 dedicated mode templates for comprehensive coverage

- **Professional Standards & Platform Integration**: 
  - Strict formatting: TOC sections only, dividers (---), Key Problems ### → format
  - Symbols: ◆ (sections), ◇ (requirements), ◳ (designs), ✦ (success), ✓ (checklist)
  - ClickUp MCP direct workspace creation with preserved formatting

- **ATLAS Framework & Challenge Mode**: 
  - 5-phase thinking (Assess/Transform/Layer/Assess/Synthesize) with 1-10 rounds
  - Auto-challenges at 3+ rounds: Gentle (1-2), Constructive (3-5), Strong (6-10)
  - REPAIR protocol: Recognize/Explain/Propose/Adapt/Iterate/Record errors

.

#### 3. 🎯 Prompt Engineering Assistant - v8.3.0
**Transform vague requests into powerful AI prompts for ANY platform with multi-format support including SMILE format**

- **8 Specialized Modes + Format Options**: 
  - Core modes: $short (minimal), $improve (default), $refine (maximum), $interactive (guided)
  - Builder modes: $prototype (exploration), $website (conversion), $app (functionality)
  - Format outputs: Standard (natural language) $smile (emoticon-structured for better instruction following, $json (API)
  - Auto-detection with pattern learning including format preferences

- **Multi-Format Enhancement Engine**: 
  - Standard format: Natural language clarity (baseline tokens)
  - JSON format: Structured for APIs (-5% to +5% tokens)
  - SMILE format: ((: format) with emoticon brackets for complex instructions (+20-30% tokens)
  - Format recommendation based on complexity and use case
  - Always shows token impact, never forces format choice

- **ATLAS Framework with Format Transform**: 
  - 6-phase thinking: Assess/Transform/Layer/Assess/Synthesize + Format Transform
  - Challenge Mode at 3+ rounds includes format necessity ("SMILE worth +25% tokens?")
  - REPAIR protocol handles format-related issues

- **SMILE Format Features**: 
  - Research-backed for better instruction following (Dr. Thomas Ager, Cardiff University)
  - Semantic brackets: `(: :)` sections, `[: :]` rigid rules, `[= =]` exact following, `[! !]` emphasis
  - Depth control: Minimal/Moderate/Heavy based on complexity

.

#### 4. 🔧 GPT - AI System Improver - v1.1.0 
**Improves Claude system artifacts through GPT-5 High Deep Reasoning mode and preservation-first editing (ChatGPT)**

- **Deep Reasoning & ATLAS Framework**: 
  - Always uses maximum thinking depth (GPT-5 High mode)
  - Interactive Discovery for unclear requests, Direct mode for clear ones
  - ATLAS phases scale automatically based on complexity

- **Preservation & Professional Delivery**: 
  - Structural changes need consent, always returns complete files
  - Emergency commands: $quick, $standard, $reset, $status
  - Session tracking (ChatGPT only) - resets each chat

---

## ⚡ Automation Agents
##### Transform natural language into intelligent automation workflows
——

#### 5. ⏰ GPT - Scheduled Tasks - v2.0.0
**Maximize ChatGPT's 10 scheduled task slots through intelligent optimization with ATLAS Framework**

- **20+ Template Library & Natural Language**: 
  - Core patterns: Morning Command (5 functions/1 slot), Weekly Intelligence (4 functions/1 slot)
  - Thinking depth selection: Quick (2-3), Standard (4-6), Thorough (7-10), Deep (10-15), Maximum (15-20+)
  - No commands needed - describe outcomes in natural language
  - Test protocol with "run in 1 minute" validation before committing

- **Smart Optimization & Canvas Documentation**: 
  - Mandatory canvas README: Auto-sent after first task, offered with every response
  - Visual slot tracking: ▓▓▓▓▓▓░░░░ (6/10 slots) with efficiency metrics
  - Consolidation suggestions: Same-time merging, topic bundling, workflow chaining
  - 2.0+ outcomes/slot target with respectful optimization

- **ATLAS Framework & Pattern Learning**: 
  - 5-phase thinking: Assess/Transform/Layer/Assess/Synthesize with 1-20+ rounds
  - Pattern detection after 3 similar requests for personalized defaults
  - Slot verification protocol before every task creation
  - REPAIR error recovery: Recognize/Explain/Propose/Adapt/Iterate/Record

---
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

## 💬 MCP Agents

<<<<<<< HEAD
→ MCPs made easy with conversational systems
=======
#### 6. 🎬 Media Editor Agent - v1.0.0 (NEW)
**Unified intelligent media editing image, video, and audio files through natural conversation**
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

#### 1. 🎬 Media Editor Agent

Edit image, video, and audio files via natural language.

- **Universal Media Operations & Intelligence**:
  - Image: Resize, convert, compress, crop, batch
  - Video: Transcode, trim, overlay, subtitles
  - Audio: Extract, convert, normalize

- **MEDIA Framework & Challenge Mode**:
  - 5-phase: Measure/Evaluate/Decide/Implement/Analyze
  - Challenge at 3+ rounds (“85% quality, 50% smaller”)
  - Commands: $reset, $standard, $quick, $status

- **Dual MCP Integration & Visual Feedback**:
  - Imagician MCP (Sharp), Video-Audio MCP (FFmpeg)
  - Progress bars, API indicators (🟢🟡🟠🔴)
  - Educational optimization insights

.

<<<<<<< HEAD
#### 2. 🌐 Webflow Agent
=======
#### 7. 🌐 Webflow Agent - v3.0.0
**Reality-based content management for existing Webflow structures**
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

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

<<<<<<< HEAD
#### 3. 📚 ClickUp & Notion Agent
=======
#### 8. 🚀 ClickUp Agent - v2.1.0
**Transform natural language into organized ClickUp workspaces while actively challenging unnecessary complexity**
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

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

## ✏️ Writer Systems

→ Automate prompt, content, documentation, and ticket writing 

#### 4. 📋 Product Owner Writer

Create professional dev tickets and enhanced documentation.

- **4 Intelligent Modes & Auto-Scaling**:
  - Modes: $ticket & $epic (dev work), $doc (guides/formatting), $interactive (discovery), $quick (instant)
  - Auto-complexity for tickets: Simple (2-3), Standard (4-5), Complex (6-8 sections)

- **ATLAS Framework & Challenge Mode**:
  - 5-phase thinking with 6-10 rounds (user-controlled)
  - Auto-challenges at 6+ rounds: Constructive or Strong based on history
  - $quick mode: Zero waiting, 6 rounds auto, no challenges

.

<<<<<<< HEAD
#### 5. ✏️ Branded Content Writer
=======
#### 9. 📓 Notion Agent - v1.3.0
**Natural language control of Notion workspaces**
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

Content writing system, fully reconfigurable for any domain: marketing, engineering, education

- **Interactive Modes & Tone Variations**:  
  - **7 Operating Modes**: $interactive (DEFAULT), $write, $share, $teach, $reflect, $improve, $quick  
  - **6 Tone Variations**: $natural, $technical, $collaborative, $educational, $reflective, $minimal

- **ATLAS Thinking Framework**:  
  - 5-phase adaptive methodology (replaces DEPTH)  
  - User-controlled depth (1-10 rounds) – always asked  
  - Challenge Mode at exactly 6+ rounds (not 3+)  

- **Web Verification & Variation Scaling**:  
  - Mandatory web verification for all market intelligence claims  
  - Scaled variations: 9/6/3 based on word count (1-30/31-150/151+)

.

#### 6. 🎯 Prompt Engineering Assistant

Generate powerful AI prompts with multi-format support.

- **8 Specialized Modes + Format Options**:
  - Core: $short, $improve, $refine, $interactive
  - Builder: $prototype, $website, $app
  - Formats: Standard, $smile (emoticon-structured), $json

- **Multi-Format Enhancement Engine**:
  - Standard: Natural language (baseline tokens)
  - JSON: API-structured (-5% to +5% tokens)
  - SMILE: Emoticon brackets (+20-30% tokens)

- **ATLAS Framework with Format Transform**:
  - 6-phase thinking + Format Transform
  - Challenge at 3+ rounds (“SMILE worth +25% tokens?”)
  - REPAIR handles format issues

.

#### 7. 🔧 GPT - AI System Improver

Improve Claude systems via GPT-5 deep reasoning and preservation-first editing.

- **Deep Reasoning & ATLAS Framework**:
  - Always maximum thinking (GPT-5 High)
  - Interactive Discovery or Direct mode
  - ATLAS auto-scaling

- **Preservation & Professional Delivery**:
  - Structural changes need consent
  - Commands: $quick, $standard, $reset, $status
  - Session tracking (ChatGPT only)

-----

## ⚡ Automation Agents

→ Create automated workflows with ease 

#### 8. ⏰ GPT - Scheduled Tasks

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

-----

## 📚 Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Docker Desktop](https://docker.com/products/docker-desktop)
- [Claude Desktop](https://claude.ai/desktop)
- Individual system READMEs for detailed setup