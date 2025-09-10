# Notion Agent - User Guide v0.200

The Notion Agent transforms natural language into organized Notion workspaces, making database creation and workspace management 10x easier. Through intelligent conversation with transparent thinking, it understands WHAT you want to organize and automatically handles HOW to build it. No modes, no commands, just describe what you need and choose how thoroughly to plan it.

## 📑 Table of Contents

- [🆕 What's New in v0.200](#whats-new-in-v200)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🧠 How It Works](#how-it-works)
- [💬 Example Interactions](#example-interactions)
- [📊 What Gets Created](#what-gets-created)
- [🔧 Installing Notion MCP (Required)](#installing-notion-mcp-required)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📦 Version History](#version-history)
- [📚 Resources](#resources)

•

## 🆕 What's New in v0.200

### Major Enhancement: Native Claude Thinking
- **Removed MCP Dependencies**: No longer requires Sequential or Cascade Thinking MCPs
- **Native Thinking Integration**: Uses Claude's built-in thinking capabilities
- **User-Controlled Depth**: Always asks users how many thinking rounds to use
- **Transparent Process**: Shows thinking progress and approach
- **Adaptive Recommendations**: Suggests optimal thinking rounds based on complexity

### Maintained Excellence
- All v0.120 capabilities preserved
- Same natural language interface
- Professional patterns still applied
- Educational approach retained
- 5-minute setup promise

•

## ✨ Key Features

- **Natural Language Only**: Just describe what you want to organize
- **Interactive Intelligence**: Adaptive conversation for perfect setup
- **User-Controlled Thinking**: You decide how thoroughly to plan (2-10 rounds)
- **Transparent Planning**: See the thinking process as it happens
- **Automatic Detection**: Recognizes workspaces vs pages vs organization tasks
- **Smart Guidance**: Asks only essential questions (2-3 max + thinking preference)
- **Best Practices Built-in**: Professional workspace patterns applied automatically
- **Visual Feedback**: Clear structure previews and success confirmations
- **Educational Focus**: Teaches Notion concepts while building
- **5-Minute Setup**: Complete workspace systems ready in minutes
- **Zero Technical Knowledge**: No understanding of Notion's interface required

•

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Notion Agent"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - Notion - v0.200.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 4 streamlined documents to your project:
- `Notion - Interactive Intelligence - v0.200.md` (Conversation examples and patterns)
- `Notion - Patterns & Operations - v0.200.md` (All patterns and operation mappings)
- `Notion - Workspace Intelligence - v0.200.md` (Best practices and error recovery)
- `README - v0.200.md` (This guide)

### Step 4: Get Your Notion API Key
1. Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click "New integration"
3. Give it a name (e.g., "Claude Assistant")
4. Copy the API key
5. **Important**: Share your Notion pages with this integration

### Step 5: Start Creating Workspaces
Simply describe what you need:
```
organize my projects
create a CRM system
meeting notes for tomorrow
clean up old tasks
track everything for my business
help me get organized
```

The system will ask how many thinking rounds to use for optimal design!

•

## 🧠 How It Works

### Thinking Framework

The system always asks about thinking depth before creating anything:

| Complexity | Recommended Rounds | Use Case |
|------------|-------------------|----------|
| **Quick** | 2-3 rounds | Simple pages, basic updates |
| **Standard** | 4-6 rounds | Databases, standard systems |
| **Thorough** | 7-10 rounds | Complex workspaces, full systems |

### Automatic Intent Detection

The system recognizes what you need and adapts its approach:

| Your Request | System Detects | Thinking Suggestion | Response |
|--------------|----------------|-------------------|----------|
| "track projects" | Project management | 4-6 rounds | Creates full system |
| "meeting notes" | Content creation | 2-3 rounds | Sets up page |
| "organize tasks" | Task management | 5-7 rounds | Builds task system |
| "clean up workspace" | Organization | 7-8 rounds | Archives and reorganizes |
| "CRM for my business" | Complex system | 8-10 rounds | Guides through setup |
| "help" | Uncertain user | Asks after understanding | Offers guided options |

### Conversation Depth Scaling

**High Clarity → Quick Execution:**
```
User: "project tracker"
System: "I'll create a comprehensive project tracker for you!

Two quick questions:
1. Will you track deadlines and team assignments?
2. How many thinking rounds? (4-6 recommended for this)"

[Creates with specified thinking depth]
```

**Medium Clarity → Brief Guidance:**
```
User: "organize my work"
System: "I'll help you organize your work! 

What's most important: tasks, projects, or notes?
Once I understand, I'll ask how thoroughly to plan it."

[Asks 1-2 questions, then thinking preference]
```

**Low Clarity → Full Guidance:**
```
User: "help"
System: "Welcome! I can help you organize anything.
What would you like to track or manage?"

[Guides through options, asks about thinking when ready to build]
```

•

## 💬 Example Interactions

### Simple Task Management
```
User: I need to track my tasks

System: I'll create a task management system for you!

Two quick questions:
1. Do you need to track tasks for different projects, or daily to-dos?
2. How many rounds of thinking should I use? (3-5 recommended)

User: Daily tasks, 4 rounds please

System: Perfect! Using 4 rounds to design your task system...

[Round 1: Analyzing requirements...]
[Round 2: Designing properties...]
[Round 3: Planning views...]
[Round 4: Optimizing workflow...]

✅ Task system created with 4 rounds of optimization!
```

### Complete Business System
```
User: track everything for my business

System: I'll help you create a complete business system!

Let me understand your needs:
1. What's your primary business focus?
2. Team size?
3. Most important metrics?

User: Consulting, just me, revenue and time

System: Perfect! This is complex, so I recommend 8-10 rounds of thinking.
How many would you prefer?

User: Let's do 9

System: Excellent! Using 9 rounds to design your consulting system...

[Detailed thinking rounds shown...]

✅ Complete business system created!
Optimized with 9 rounds of careful planning.
```

### Organization Request
```
User: my workspace is a mess
System: I'll help you organize your workspace! 

Quick assessment:
• What's the main type of content?
• How much are we organizing?
• Want to start fresh or reorganize?

User: Mix of everything, hundreds of items, reorganize

System: This needs careful planning to preserve everything.
How many thinking rounds? (8-10 recommended for safe reorganization)

User: 10 rounds, want to be thorough

System: Perfect! Using 10 rounds for complete reorganization...

[Shows all 10 thinking rounds...]

✅ Workspace beautifully organized with 10 rounds of careful planning!
```

•

## 📊 What Gets Created

Every workspace uses intelligent patterns with user-controlled thinking:

### Business Systems (8-10 thinking rounds)
```
CRM System:
├── Clients Database (contacts, value tracking)
├── Projects Database (linked to clients)
├── Interactions Log (emails, meetings)
└── Dashboard (pipeline, metrics)
Thinking: Optimized relationships and automation
```

### Personal Productivity (5-7 thinking rounds)
```
Task Management:
├── Projects (goals, deadlines)
├── Tasks (linked to projects)
├── Today View (immediate focus)
└── Weekly Reviews (progress)
Thinking: Balanced for sustainability
```

### Team Workspaces (7-9 thinking rounds)
```
Product Development:
├── Sprint Planning (cycles)
├── Features (user stories)
├── Bugs (tracking)
└── Team Wiki (documentation)
Thinking: Collaboration and permissions optimized
```

•

## 🔧 Installing Notion MCP (Required)

The Notion MCP provides core functionality for all Notion operations.

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- Notion API key from [notion.so/my-integrations](https://www.notion.so/my-integrations)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker container for the Notion Agent MCP tool.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone this repo: https://github.com/notionhq/mcp-server-notion.git
3. Set up environment variables for Notion API key
4. Create Dockerfile if needed
5. Create docker-compose.yml file
6. Configure Claude Desktop's claude_desktop_config.json
7. Build and start the container

My Notion API key is: [YOUR_API_KEY_HERE]
I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

### Option B: NPX Setup (Quick but Less Stable)

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/mcp-server-notion"],
      "env": {
        "NOTION_API_KEY": "your-notion-api-key"
      }
    }
  }
}
```

•

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Don't know where to start"** | Just describe your goal, system guides you |
| **"How many rounds?"** | Start with recommended, adjust if needed |
| **"Can't find workspace"** | Share pages with your Notion integration |
| **"Permission denied"** | Check integration has access to workspace |
| **"API key not working"** | Verify key in config file |
| **"MCP not connected"** | Restart Claude Desktop, check Docker |

### Quick Fixes

**Docker Issues:**
```bash
# Check if running
docker ps
# View logs
docker logs notion-mcp
# Restart
docker-compose restart
```

**NPX Issues:**
- Ensure Node.js installed
- Check config file syntax
- Restart Claude Desktop

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For Notion issues: Verify integration settings
- For thinking depth: Start with recommended, experiment

•

## ⚠️ Important Notes

- **Natural language only** - No commands or modes needed
- **Thinking transparency** - Always asks how many rounds
- **User control** - You decide optimization depth
- **Automatic detection** - System recognizes what you need
- **Share pages required** - Integration needs access
- **No overwrites** - Always creates new or asks
- **Best practices automatic** - Professional patterns applied
- **Educational by design** - Teaches while building
- **3-4 questions max** - Including thinking preference
- **Visual feedback always** - See what's created
- **5-minute guarantee** - Complex systems ready fast

•

## 📦 Version History

- **v0.200**: Native Claude thinking, user-controlled rounds, removed MCP dependencies
- **v0.120**: Unified to single approach, removed modes, cleaner architecture
- **v0.110**: Streamlined to 3 documents, enhanced MCP intelligence
- **v0.100**: Initial release with 5 reference documents

•

## 📚 Resources

### Core Tools
- [Notion MCP Server](https://github.com/notionhq/mcp-server-notion) (Required)
- [Claude Projects](https://claude.ai) (Platform)

### Documentation
- [Notion API Docs](https://developers.notion.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Docker Desktop](https://docs.docker.com/desktop/)

### Quick Links
- [Create Notion Integration](https://www.notion.so/my-integrations)
- [Claude Projects](https://claude.ai)
- [Share with Integration](https://www.notion.so/help/add-and-manage-connections-with-the-api)

### Thinking Guidelines
- **Simple operations**: 2-3 rounds
- **Standard databases**: 4-6 rounds
- **Complex systems**: 7-10 rounds
- **Complete reorganization**: 9-10 rounds
- **Always ask user**: Let them control depth

---

*Transform ideas into organized Notion workspaces through natural conversation with transparent, user-controlled thinking. Just describe what you want to organize, choose how thoroughly to plan it, and watch your workspace build itself. No modes, no commands, just intelligent assistance with the depth you choose.*
