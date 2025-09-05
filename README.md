# AI Magic ✨

Some of my non-client AI systems that I made available to the public. They were designed to work with Claude, but you can tweak them to fit with other AI setups too.

> - 99.999% of people won't try these systems. Beat the odds?
> - Don't reward me with unwanted coffee: https://buymeacoffee.com/michelkerkmeester

---

## 📋 Table of Contents

### ✏️ Writer Systems
1. [Branded Content Writer](#1--branded-content-writer)
2. [Product Owner Writer](#2--product-owner-writer)
3. [Prompt Engineering Assistant](#3--prompt-engineering-assistant)

### ⚡ Automation Agents  
4. [GPT - Scheduled Tasks](#4--gpt---scheduled-tasks)

### 💬 MCP Agents
5. [Media Editor Agent](#5--media-editor)
6. [Webflow Agent](#6--webflow-agent)
7. [ClickUp Agent](#7--clickup-agent)
8. [Notion Agent](#8--notion-agent)

### 🔧 Additional Sections
- [Common Features](#-common-features)
- [Installation](#-installation)
- [Choosing the Right System](#-choosing-the-right-system)
- [Resources](#-resources)

---

## ✏️ Writer Systems
##### Automated content, documentation & prompt writing systems
——

#### 1. ✏️ Branded Content Writer - v5.4.0 
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

#### 2. 📋 Product Owner Writer - v8.4.0 
**Transform vague requests into professional dev tickets, specs, docs, and beautifully formatted documents with built-in complexity challenging**

- **5 Intelligent Modes & Auto-Scaling**: 
  - Core modes: $ticket (dev), $spec (frontend), $doc (guides), $text (snippets), $beautify (document formatting)
  - Auto-complexity: Simple (bugs 2-3 sections), Standard (features 4-5), Complex (platforms 6-8)
  - Feature complete: 6 core system files + 5 dedicated mode templates for comprehensive coverage

- **Professional Standards & Platform Integration**: 
  - Strict formatting: TOC sections only, dividers (---), Key Problems ### → format
  - Symbols: ◆ (sections), ◇ (requirements), ◳ (designs), ✦ (success), ✔ (checklist)
  - ClickUp MCP direct workspace creation with preserved formatting

- **ATLAS Framework & Challenge Mode**: 
  - 5-phase thinking (Assess/Transform/Layer/Assess/Synthesize) with 1-10 rounds
  - Auto-challenges at 3+ rounds: Gentle (1-2), Constructive (3-5), Strong (6-10)
  - REPAIR protocol: Recognize/Explain/Propose/Adapt/Iterate/Record errors

.

#### 3. 🎯 Prompt Engineering Assistant - v8.1.0
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

---

## ⚡ Automation Agents
##### Transform natural language into intelligent automation workflows
——

#### 4. ⏰ GPT - Scheduled Tasks - v2.0.0
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

## 💬 MCP Agents
##### MCP tools made easy with conversational systems
——

#### 5. 🎬 Media Editor Agent - v1.0.0 (NEW)
**Unified intelligent media editing image, video, and audio files through natural conversation**

- **Universal Media Operations & Intelligence**: 
  - Image processing: Resize, convert (JPEG/PNG/WebP/AVIF), compress, crop, rotate, batch
  - Video operations: Transcode, trim, overlay, concatenate, subtitles, extract frames
  - Audio handling: Extract from video, convert formats, normalize, remove silence
  - Natural language: "Make it smaller" → Smart context analysis

- **MEDIA Framework & Challenge Mode**: 
  - 5-phase thinking: Measure/Evaluate/Decide/Implement/Analyze with 1-10 rounds
  - Challenge at 3+ rounds: "85% quality visually identical but 50% smaller"
  - Pattern learning: Adapts to quality preferences and workflow patterns
  - Emergency commands: $reset, $standard, $quick, $status for instant control

- **Dual MCP Integration & Visual Feedback**: 
  - Imagician MCP: High-performance image processing via Sharp
  - Video-Audio MCP: Comprehensive media handling via FFmpeg
  - Real-time progress: Visual bars, API usage indicators (🟢🟡🟠🔴)
  - Educational insights: Explains why optimizations work

.

#### 6. 🌐 Webflow Agent - v3.0.0
**Reality-based content management for existing Webflow structures**

- **Content Excellence & Operations**: 
  - CMS management within existing collections, SEO publishing
  - Batch operations with rollback capability
  - ATLAS Framework with 1-10 thinking rounds
  - Intelligent fallbacks for platform limitations

- **Transparent Limitations & Workarounds**: 
  - Clear limits: Designer for fields, URLs only for images
  - Rich text flex for complex content, external images integration
  - Field repurposing strategies, multi-reference solutions
  - Alternative paths for each limitation

- **Pattern Learning System**: 
  - Remembers collection structures and naming conventions
  - Learns operations and suggests optimizations
  - Workflow adaptation to your preferences
  - Progressive efficiency improvements

.

#### 7. 🚀 ClickUp Agent - v2.1.0
**Transform natural language into organized ClickUp workspaces while actively challenging unnecessary complexity**

- **Simplicity-First Design & Pattern Learning**: 
  - Defaults to minimal viable structures (3-5 fields, not 15)
  - Phased rollouts: Start simple, expand based on actual use
  - Session learning: After 2 simplifications → defaults to minimal
  - Performance limits: <5000 items/list, <8 fields recommended

- **Smart Structure & Natural Language**: 
  - "Organize my projects" → Challenges if over-complex, suggests phases
  - Workspace creation with adoption focus over features
  - Automation only when manual process proven
  - Educational insights: Explains why simpler often works better

- **ATLAS Framework & Challenge Mode**: 
  - 5-phase thinking (Assess/Transform/Layer/Assess/Synthesize) with 1-10 rounds
  - 3-level challenges: Gentle (1-2 rounds), Constructive (3-6), Strong (7-10)
  - Questions complexity before building: "Single space clearer?" "Essential fields only?"
  - REPAIR protocol for graceful error recovery

.

#### 8. 📓 Notion Agent - v1.3.0
**Natural language control of Notion workspaces**

- **Natural Language Processing**: 
  - "Organize my projects" → Database with views and relations
  - Multi-database relationship detection from descriptions
  - Template generation and schema optimization
  - Complex requirements understanding

- **Smart Structure & Best Practices**: 
  - Database properties with filtered/sorted views
  - Cross-database relations and rollup strategies
  - Formula fields with explanations
  - Permission setup for teams

- **Error Recovery & Education**: 
  - Graceful failures with alternative approaches
  - Partial success with rollback capabilities
  - Design principles and optimization tips
  - Migration guidance from other platforms

---

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

---

## 📦 Installation

### Quick Start (Any System)
1. Create a Claude project
2. Add system instructions
3. Upload reference documents
4. Configure MCP tools (optional but recommended)

### MCP Setup (Docker Recommended)
```bash
# Create MCP directory
mkdir "$HOME/MCP Servers"
cd "$HOME/MCP Servers"

# Clone needed tools (examples)
git clone https://github.com/webflow/mcp-server-webflow.git  # For Webflow Agent
git clone https://github.com/flowy11/imagician.git  # For Media Editor
git clone https://github.com/misbahsy/video-audio-mcp.git  # For Media Editor

# Use AI to generate docker-compose.yml
# Start containers
docker-compose up -d
```

---

## 📚 Resources
- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Docker Desktop](https://docker.com/products/docker-desktop)
- [Claude Desktop](https://claude.ai/desktop)
- [Lovable Platform](https://lovable.dev)
- Individual system READMEs for detailed setup