# ClickUp Agent - User Guide v1.2.0

The ClickUp Agent transforms natural language into organized ClickUp workspaces, making task management and team collaboration 10x easier. Through intelligent conversation with user-controlled thinking depth, it understands WHAT you want to organize and automatically handles HOW to build it. No modes, no commands, just describe what you need and choose your analysis depth.

## 📑 Table of Contents

- [🆕 What's New in v1.2.0](#-whats-new-in-v120)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 Native Thinking System](#-native-thinking-system)
- [💬 Interactive Intelligence](#-interactive-intelligence)
- [📊 Workspace Patterns](#-workspace-patterns)
- [🎨 Smart Defaults](#-smart-defaults)
- [📋 Examples](#-examples)
- [🔧 Installing ClickUp MCP](#-installing-clickup-mcp)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## 🆕 What's New in v1.2.0

### Major Updates
- **Native Claude Thinking**: Removed dependency on external thinking MCPs
- **User-Controlled Depth**: Always asks users how many thinking rounds to use
- **Thinking Throughout**: Applied to ALL operations, not just complex ones
- **Smarter Prompts**: Context-aware thinking recommendations
- **Discovery Exception**: Only skips thinking question during exploration phase

### Key Improvements
- No external MCP dependencies needed
- Full control over analysis depth
- Better performance with native thinking
- Clearer user guidance
- Maintained all v1.1.0 capabilities

.

## ✨ Key Features

- **Natural Language First**: Describe what you want in plain English, no commands needed
- **User-Controlled Thinking**: You choose analysis depth for every operation
- **Interactive Intelligence**: Adaptive conversation that understands intent and guides when needed
- **Native Claude Thinking**: Uses Claude's built-in reasoning capabilities
- **Smart Guidance**: Asks only essential questions (2-3 max) for perfect setup
- **Best Practices Built-in**: Professional workspace patterns applied automatically
- **Visual Feedback**: Clear structure previews and success confirmations
- **Educational Focus**: Teaches ClickUp concepts through successful creation
- **5-Minute Setup**: Complete workspace systems ready in minutes
- **Zero Technical Knowledge**: No understanding of ClickUp's interface required

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "ClickUp Agent v1.2"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - ClickUp MCP - v1.2.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 4 streamlined documents to your project:
- `ClickUp - Interactive Intelligence - v1.2.0.md` (Conversational guidance specification)
- `ClickUp - Patterns & Operations - v1.2.0.md` (All patterns and operation mappings)
- `ClickUp - Workspace Intelligence - v1.2.0.md` (Best practices and error recovery)
- `README.md` (This guide)

### Step 4: Get Your ClickUp API Key
1. Go to [ClickUp Settings](https://app.clickup.com/settings/apps)
2. Click "Apps" in the left sidebar
3. Generate a personal API token
4. Copy the token for MCP configuration

### Step 5: Install ClickUp MCP
Follow the installation guide in the Installing ClickUp MCP section below.

### Step 6: Start Creating Workspaces
Simply describe what you need:
```
organize my projects              # Guided conversation begins
I need a CRM system              # Creates complete CRM
track sprints for my team        # Sets up agile workspace
help me with task management     # Interactive guidance
```

.

## 🧠 Native Thinking System

### How It Works

The v1.2.0 release uses Claude's native thinking capabilities with user control:

**You Always Choose the Depth:**
```
System: "How many rounds of thinking should I use?
        • Quick (2-3) - Simple operations
        • Standard (4-6) - Most requests
        • Thorough (7-10) - Complex systems
        • Maximum (10+) - Comprehensive analysis
        
        Or just tell me a specific number!"
```

### Thinking Depth Guidelines

| Depth | Rounds | Best For | Analysis Time |
|-------|--------|----------|---------------|
| **Quick** | 2-3 | Single tasks, simple lists | ~30 seconds |
| **Standard** | 4-6 | Team workspaces, templates | ~1 minute |
| **Thorough** | 7-10 | Multi-team systems, integration | ~2 minutes |
| **Maximum** | 10+ | Enterprise architecture | 2+ minutes |

### When You're Asked

**Always asked before execution:**
- After understanding your request
- When ready to build
- Before any operation

**Only skipped during:**
- Initial discovery questions
- Clarification phase
- When output isn't immediate

.

## 💬 Interactive Intelligence

All operations use intelligent conversation that adapts to your needs:

### Typical Flow
1. You describe what you need in natural language
2. System identifies intent and complexity
3. Asks 1-3 strategic questions if needed
4. **Asks for your thinking preference**
5. Shows structure preview
6. Creates complete workspace
7. Provides visual confirmation
8. Suggests logical next steps

### Example Interactions

**Simple Request:**
```
User: create a task list
System: I'll create a task management list for you!
        Personal tasks or team collaboration?
User: team
System: Perfect! How many thinking rounds should I use?
        • Quick (2-3) - Basic list
        • Standard (4-6) - Full features (recommended)
User: standard
[Creates with 5 rounds of thinking]
```

**Complex System:**
```
User: I need to track everything for my agency
System: I'll help you create a complete agency management system!
        
        Quick questions:
        1. How many active clients typically?
        2. Do you bill hourly or by project?
        3. Team size?
        
User: 15 clients, both billing, team of 5
System: This is comprehensive! Thinking depth?
        • Standard (4-6) - Core features
        • Thorough (7-10) - Full integration (recommended)
        • Maximum (10+) - Enterprise scale
        
[Creates based on chosen depth]
```

**Vague Request:**
```
User: help me organize
System: I'll help you get organized! Let's start with what matters most:
        • Task management for daily work
        • Project tracking for bigger initiatives
        • Team collaboration system
        • Complete workspace for everything
        
        What would have the biggest impact for you?
[No thinking rounds yet - still discovering]
```

.

## 📊 Workspace Patterns

Every workspace uses intelligent patterns automatically applied based on your thinking choice:

### Common Systems Created

**Agency Management (Default: Thorough 7-10):**
```
Agency Hub:
├── Clients Space (contacts, projects, value)
├── Projects Lists (linked to clients)
├── Tasks (time tracking enabled)
└── Dashboard (pipeline, metrics, workload)
```

**Sprint Planning (Default: Standard 4-6):**
```
Development Space:
├── Sprints Folder (2-week cycles)
├── Product Backlog (prioritized)
├── Bugs List (severity tracking)
└── Velocity Dashboard (burndown, metrics)
```

**Personal Productivity (Default: Quick 2-3):**
```
Personal Workspace:
├── Goals & OKRs (quarterly)
├── Projects (linked to goals)
├── Daily Tasks (Me Mode view)
└── Weekly Reviews (templates)
```

.

## 🎨 Smart Defaults

The system applies best practices automatically, scaled by thinking depth:

### Automatic Decisions by Thinking Depth
- **List vs Space**: Based on scale and relationships
- **Custom Fields**: Essential fields for use case (more with depth)
- **Views**: Optimized for desktop/mobile (more with depth)
- **Automations**: Common patterns enabled (complex with depth)
- **Templates**: Created for repeated work (advanced with depth)

### Field Intelligence by Depth
| Task Type | Quick (2-3) | Standard (4-6) | Thorough (7-10) |
|-----------|-------------|----------------|-----------------|
| Tasks | Priority, Due Date | + Status, Assignee, Time | + Dependencies, Categories |
| Projects | Timeline, Owner | + Budget, Phase, Risk | + Resources, Milestones |
| Bugs | Severity, Status | + Environment, Reporter | + Components, Test Cases |
| Content | Publish Date | + Channel, Author | + Campaign, Analytics |

.

## 📋 Examples

### Simple Tasks
```
User: I need to track my daily tasks
System: I'll create a task management system for you!
        Do you work with deadlines frequently?
User: yes
System: How many thinking rounds?
        • Quick (2-3) - Simple list
        • Standard (4-6) - Full tracking (recommended)
User: quick
[Creates with 3 rounds]
```

### Complete Systems
```
User: set up project management for my team
System: Perfect! I'll create a comprehensive project system.
        Quick question: How many people on the team?
User: 8 people
System: Great! Thinking depth for this system?
        • Standard (4-6) - Good for most teams
        • Thorough (7-10) - Full features (recommended for 8 people)
User: thorough
[Creates with 8 rounds of analysis]
```

### Organization
```
User: archive old completed stuff
System: I'll help you archive completed tasks!
        Should I keep them for reference or prepare for deletion?
User: keep for reference
System: How thorough should the archiving be?
        • Quick (2-3) - Simple move
        • Standard (4-6) - Organized structure
User: standard
[Archives with 4 rounds of thinking]
```

### Emergency Response
```
User: everything is on fire help NOW
System: I'll help you get control immediately!
        What's the biggest fire: overdue tasks, project deadlines, or team confusion?
User: overdue tasks everywhere
System: Creating emergency triage system!
        Given urgency, thinking depth?
        • Quick (2-3) - Immediate basic fix
        • Standard (4-6) - Organized solution (recommended)
User: standard but hurry
[Creates with 5 rapid rounds]
```

.

## 🔧 Installing ClickUp MCP

The ClickUp MCP provides all task management and workspace operations.

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- ClickUp API token from [ClickUp Settings](https://app.clickup.com/settings/apps)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker container for the ClickUp Agent MCP tool.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone this repo: https://github.com/clickup/mcp-server-clickup.git
3. Create Dockerfile for the ClickUp MCP
4. Create docker-compose.yml file
5. Configure Claude Desktop's claude_desktop_config.json
6. Build and start the container
7. Set up environment variables for API authentication

My details:
- ClickUp API token: [YOUR_CLICKUP_API_TOKEN]
- Operating system: [Windows/Mac/Linux]

Please give me the exact commands to run, including:
- Dockerfile with Node.js environment
- docker-compose.yml with proper configuration
- Claude Desktop configuration for Docker
```

The AI will provide step-by-step commands for your operating system.

**Docker Setup Template:**

The AI will help you create something like:

```yaml
# docker-compose.yml example structure
version: '3.8'
services:
  clickup-mcp:
    build: .
    environment:
      - CLICKUP_API_TOKEN=your-token-here
      - NODE_ENV=production
    restart: unless-stopped
    ports:
      - "3000:3000"  # If needed for MCP communication
```

### Option B: NPM Global Install (Alternative)

**Prerequisites:**
- Node.js 18+ installed ([Download Node.js](https://nodejs.org/))
- Claude Desktop app

**Installation Steps:**
```bash
# 1. Install globally
npm install -g @clickup/mcp-server-clickup

# 2. Verify installation
clickup-mcp --version

# 3. Set up API token
export CLICKUP_API_TOKEN="your-token-here"
```

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "clickup": {
      "command": "clickup-mcp",
      "env": {
        "CLICKUP_API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

### Option C: NPX Setup (Quick but Less Stable)

For quick testing without installation:

```json
{
  "mcpServers": {
    "clickup": {
      "command": "npx",
      "args": ["-y", "@clickup/mcp-server-clickup"],
      "env": {
        "CLICKUP_API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

**Note:** NPX may have connection stability issues. Docker is recommended for production use.

### Option D: Built-in Claude Desktop Support

**Note:** ClickUp MCP may already be available in Claude Desktop. Check if it's pre-installed:
1. Open Claude Desktop settings
2. Look for ClickUp in available MCPs
3. If present, just add your API token

### Verifying Installation

**For Docker:**
```bash
# Check container is running
docker ps | grep clickup

# Check logs
docker logs clickup-mcp

# Test API connection
docker exec clickup-mcp curl -H "Authorization: YOUR_TOKEN" \
  https://api.clickup.com/api/v2/user
```

**For NPM/NPX:**
```bash
# Test API token
curl -H "Authorization: YOUR_TOKEN" \
  https://api.clickup.com/api/v2/user

# Should return your user info if token is valid
```

Then restart Claude Desktop and test with: "create a test task"

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"How many rounds?"** | Choose based on complexity (Quick for simple, Standard for most) |
| **"Don't know what depth"** | System provides recommendations based on request |
| **"Can't find workspace"** | Check you're in the right ClickUp workspace |
| **"Permission denied"** | Verify your API token has full access |
| **"Too many options"** | Choose "Quick" to start simple |
| **"Taking too long"** | Use fewer thinking rounds next time |
| **"MCP not connected"** | Check Docker container or restart Claude Desktop |
| **"Invalid API token"** | Regenerate token in ClickUp settings |

### Docker-Specific Issues

**Container Problems:**
```bash
# Check container status
docker ps -a | grep clickup

# View detailed logs
docker logs --tail 50 clickup-mcp

# Restart container
docker restart clickup-mcp

# Rebuild if needed
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

**Common Docker Fixes:**
- **Connection issues**: Check API token in docker-compose.yml
- **Port conflicts**: Ensure port 3000 isn't in use
- **Memory issues**: Usually minimal, ClickUp MCP is lightweight
- **Network issues**: Restart Docker Desktop

### API Token Issues

**Getting a Valid Token:**
1. Go to [ClickUp Settings](https://app.clickup.com/settings/apps)
2. Click "Apps" → "Generate Token"
3. Copy the entire token string
4. Test with: `curl -H "Authorization: pk_YOUR_TOKEN" https://api.clickup.com/api/v2/user`

### Thinking Depth Selection

**Quick Guide:**
- **Unsure?** Start with Standard (4-6)
- **Urgent?** Use Quick (2-3)
- **Complex?** Go Thorough (7-10)
- **Can always adjust** in next request

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPM issues: Check Claude Desktop logs
- For ClickUp issues: Verify you're logged into ClickUp
- For thinking questions: Ask for recommendation
- For API issues: Check [ClickUp API Docs](https://clickup.com/api)

.

## ⚠️ Important Notes

- **No commands needed** - Just describe what you want
- **You control thinking** - Always your choice on depth
- **Conversation adapts** - From quick execution to full guidance
- **API token required** - Get from ClickUp settings
- **No overwrites** - Always creates new or asks
- **Best practices automatic** - Professional patterns applied
- **Thinking scales features** - More depth = more features
- **Educational by design** - Teaches while building
- **2-3 questions max** - Respects your time
- **Visual feedback always** - See what's created
- **Docker recommended** - Most stable connection

.

## 📦 Version History

- **v1.2.0**: Native Claude thinking, user-controlled depth, removed MCP dependencies
- **v1.1.0**: Unified interactive intelligence, removed mode system
- **v1.0.0**: Initial release with multiple modes

.

## 📚 Resources

### Core Tools
- [ClickUp MCP Server](https://github.com/clickup/mcp-server-clickup) (Required)
- [Claude Projects](https://claude.ai) (Platform)

### Documentation
- [ClickUp API Docs](https://clickup.com/api)
- [ClickUp Help Center](https://help.clickup.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Docker Desktop](https://docs.docker.com/desktop/)

### Quick Links
- [ClickUp Login](https://app.clickup.com)
- [Get API Token](https://app.clickup.com/settings/apps)
- [Claude Desktop](https://claude.ai/download)
- [ClickUp Features Guide](https://help.clickup.com/hc/en-us/categories/6314476398999-Features)

### Performance Guidelines
- **Simple operations**: 2-3 thinking rounds
- **Standard workspaces**: 4-6 thinking rounds
- **Complex systems**: 7-10 thinking rounds
- **Enterprise architecture**: 10+ thinking rounds
- **Emergency fixes**: Quick (2-3) with follow-up

---

*Transform ideas into organized ClickUp workspaces through natural conversation with user-controlled thinking depth. The system understands what you need and guides appropriately. You choose how thoroughly to analyze. Complex systems ready in under 5 minutes. Just describe what you want to organize and select your thinking preference!*