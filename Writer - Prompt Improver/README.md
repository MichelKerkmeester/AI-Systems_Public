# Prompt Engineering Assistant - User Guide v3.0.0

A comprehensive system that transforms vague requests into clear, effective AI prompts using proven frameworks, systematic evaluation, and intelligent refinement. Features 5 operating modes, visual progress tracking, and conversational guidance.

## 🆕 What's New in v3.0.0

- **5 Operating Modes**: From quick fixes ($short) to full optimization ($refine)
- **Interactive Guided Mode**: Conversational prompt building with intelligent questions
- **Visual Dashboard**: Real-time progress bars and enhancement metrics
- **3-Phase Refinement**: Improve → Evaluate → Refine workflow
- **35-Criteria Evaluation**: Comprehensive quality assessment system
- **MCP Integration**: Supports Sequential and Cascade Thinking tools
- **Pattern Library**: Reusable templates for common use cases

.

## Overview

The Prompt Engineering Assistant helps users craft powerful, precise prompts for any AI system. With three core frameworks (CRAFT, SPARK, PRISM) and intelligent enhancement algorithms, it delivers professional-grade prompts that maximize AI performance.

## ✨ Key Features

- **5 Specialized Modes**: $short, $improve (default), $refine, $interactive, $json
- **3 Core Frameworks**: CRAFT (structure), SPARK (enhancement), PRISM (evaluation)
- **Intelligent MCP Selection**: Automatic choice between Sequential and Cascade thinking
- **Visual Progress Tracking**: Unicode-based dashboards showing improvements
- **Platform Optimization**: Tailored for ChatGPT, Claude, and other AI platforms
- **Comprehensive Examples**: 50+ before/after transformations
- **First-Time User Detection**: Automatic onboarding for new users
- **Artifact-Based Delivery**: All prompts delivered in reusable artifacts

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Prompt Engineering Assistant v3.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Prompt Improver - v3.0.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Prompt - Artifact Standards & Templates - v1.0.0.md`
- `Prompt - Evaluation & Refinement - v1.0.0.md`
- `Prompt - Examples & Case Studies - v1.0.0.md`
- `Prompt - Interactive Mode - v1.0.0.md`
- `Prompt - Patterns & Enhancements - v1.0.0.md`

### Step 4: Start Improving Prompts
Simply paste your prompt or describe what you need:
```
write about dogs
$improve analyze customer data
$interactive
$refine create a marketing strategy
```

.

## 🎛️ Operating Modes

| Mode | Activation | Purpose | Best For | MCP Usage |
|------|------------|---------|----------|-----------|
| **$short** | `$short` or `$s` | Quick minimal refinement | Simple clarity boost | Sequential (1-2 thoughts) |
| **$improve** | `$improve` or `$i` (DEFAULT) | Smart enhancement | Most improvements | Sequential (2-3 thoughts) |
| **$refine** | `$full` or `$refine` or `$r` | Full 3-phase optimization | Maximum quality | Cascade (3-5+ thoughts) |
| **$interactive** | `$interactive` | Guided help with Q&A | Learning/exploring | Sequential (1-3 thoughts) |
| **$json** | `$json` or `$j` | API-ready JSON format | Programmatic use | Sequential (2-3 thoughts) |

.

## 🏗️ Core Frameworks

### CRAFT Framework (Structure)
- **C** - Context & Background
- **R** - Role & Expertise
- **A** - Action & Deliverables
- **F** - Format & Structure
- **T** - Target & Success Criteria

### SPARK Method (Enhancement)
- **S** - Specificity (add concrete details)
- **P** - Purpose (clarify intent)
- **A** - Audience (define target users)
- **R** - Results (specify outcomes)
- **K** - Knowledge (include context)

### PRISM Evaluation (Quality)
- **P** - Precision (25%)
- **R** - Relevance (20%)
- **I** - Impact (25%)
- **S** - Structure (15%)
- **M** - Measurability (15%)

.

## 📊 Visual Dashboard Example

```
📊 Optimization Report
Overall Enhancement Score: 85% ↑

CRAFT Framework Coverage:
C - Context      ████████░░ 80%
R - Role         ██████████ 100%
A - Action       ████████░░ 80%
F - Format       ██████░░░░ 60%
T - Target       ██████████ 100%

Key Improvements:
🎯 Specificity: +45% (added metrics, timeframes)
👤 Role Definition: +30% (expert persona added)
📋 Structure: +25% (clear sections defined)

Before: 3 words | Clarity: 2/10
After: 87 words | Clarity: 9/10
```

.

## 🤖 Interactive Mode

Perfect for beginners or when you need guidance:
- Asks 2-3 targeted questions
- Builds prompt from your answers
- Provides explanations
- Shows improvement metrics

Example:
```
User: $interactive "create presentation"
AI: "Let me help! What's the main purpose? Who's your audience?"
```

.

## 📈 Evaluation System

### Quick Evaluation (10 Criteria)
- Clarity & Specificity
- Context Provided
- Task Definition
- Output Format
- And 6 more...

### Full Evaluation (35 Criteria)
- 7 groups of 5 criteria each
- Comprehensive scoring
- Targeted improvement suggestions
- Before/after comparison

.

## 🔧 Technical Details

### MCP Selection Logic
- **Simple/Clear tasks** → Sequential (1-2 thoughts)
- **Standard improvements** → Sequential (2-3 thoughts)
- **Complex/Unclear** → Cascade (3-5 thoughts)
- **Full refinement** → Cascade (5+ thoughts)

### Platform Detection
Automatically optimizes for:
- ChatGPT
- Claude
- Gemini
- Other AI platforms

### Artifact Standards
- Always uses `text/markdown` type
- Includes mode and MCP notation
- Visual dashboard for appropriate modes
- Complete enhancement details

.

## 📚 Example Transformations

### Simple Enhancement
**Before:** "write blog"
**After:** "Write a 1200-word blog post on 'Remote Work Productivity' for tech professionals. Include 5 strategies with examples. Tone: conversational yet authoritative."

### Complex Analysis
**Before:** "analyze data"
**After:** "As a data analyst, identify top 3 customer segments from Q4 sales data. Format: Executive summary with actionable insights prioritized by revenue impact."

### Technical Request
**Before:** "fix bug"
**After:** "Debug React component re-rendering issue causing UI freeze. Provide: root cause analysis, fix implementation, prevention strategies."

.

## 🔧 Installing MCP Tools (Recommended)

The system intelligently selects between these based on task complexity. Choose either Docker (stable) or NPX (quick) installation:

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the Prompt Engineering Assistant MCP tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/arben-adm/mcp-sequential-thinking.git
   - https://github.com/drewdotpro/cascade-thinking-mcp.git
3. Create a docker-compose.yml file with services for both
4. Configure Claude Desktop's claude_desktop_config.json
5. Start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for 2 running containers
2. Look for the 🔌 icon in Claude Desktop showing available tools
3. Test with: "improve this prompt: write about dogs"

### Option B: NPX Installation (Quick but Less Stable)

Add to Claude Desktop config file:
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "cascade-thinking": {
      "command": "npx",
      "args": ["-y", "cascade-thinking-mcp"]
    }
  }
}
```

.

## 🆘 Troubleshooting

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **Wrong directory**: Check you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Ensure Node.js is installed for NPX method
- **Containers won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **Rate limits**: Both tools handle this gracefully with retries

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For general issues: The AI assistant can help diagnose problems

.

## ⚠️ Important Notes

- **Never answers prompts** - Only improves them
- **Always uses artifacts** - Ensures reusability
- **No em dashes** - Uses commas, colons, or periods
- **Works without MCPs** - But enhanced with them

## 📦 Version History

- **v3.0.0**: Complete rewrite with 5 modes, visual dashboards, interactive guidance
- **v2.0.0**: Added evaluation system and refinement workflow
- **v1.0.0**: Initial CRAFT framework implementation

## 🎯 Key Principles

1. **Make prompt engineering accessible** without dumbing it down
2. **Every feature serves both beginners and experts**
3. **Visual feedback makes improvements tangible**
4. **Preserve user intent while maximizing effectiveness**
5. **Scale complexity to match task requirements**

.

## 📚 Other Resources

- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Sequential Thinking MCP](https://github.com/arben-adm/mcp-sequential-thinking)
- [Cascade Thinking MCP](https://github.com/drewdotpro/cascade-thinking-mcp)

---

*Transform vague requests into powerful prompts. Make AI work better for everyone.*