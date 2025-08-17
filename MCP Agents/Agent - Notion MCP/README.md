# Notion Agent - User Guide v1.2.0

The Notion Agent transforms natural language into organized Notion workspaces, making database creation and workspace management 10x easier. Through intelligent conversation, it understands WHAT you want to organize and automatically handles HOW to build it. No modes, no commands, just describe what you need.

## 📑 Table of Contents

- [🆕 What's New in v1.2.0](#-whats-new-in-v120)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 How It Works](#-how-it-works)
- [💬 Example Interactions](#-example-interactions)
- [📊 What Gets Created](#-what-gets-created)
- [🔧 Installing MCPs (Required & Optional)](#-installing-mcps-required--optional)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

•

## 🆕 What's New in v1.2.0

### Major Simplification
- **Single Unified Approach**: Removed all mode commands ($w, $c, $o)
- **Interactive Intelligence**: One smart system handles everything
- **Reduced to 3 Documents**: From 5 files to just 3 essential references
- **Cleaner System Prompt**: Examples moved to reference docs
- **Automatic Intent Detection**: System recognizes what you need
- **Smarter Conversations**: Better at detecting complexity and adjusting approach

### Maintained Excellence
- All v1.1.0 capabilities preserved
- Enhanced MCP intelligence
- Same 5-minute setup promise
- Professional patterns still applied
- Educational approach retained

•

## ✨ Key Features

- **Natural Language Only**: Just describe what you want to organize
- **Interactive Intelligence**: Adaptive conversation for perfect setup
- **Automatic Detection**: Recognizes workspaces vs pages vs organization tasks
- **Triple MCP Support**: Notion MCP (core), Sequential Thinking (simple), Cascade Thinking (complex)
- **Smart Guidance**: Asks only essential questions (2-3 max)
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
4. Name it "Notion Agent v1.2"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - Notion MCP - v1.2.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 3 streamlined documents to your project:
- `Notion - Interactive Intelligence - v1.2.0.md` (Conversation examples and patterns)
- `Notion - Patterns & Operations - v1.0.0.md` (All patterns and operation mappings)
- `Notion - Workspace Intelligence - v1.0.0.md` (Best practices and error recovery)

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

No modes or commands needed! The system automatically understands your intent.

•

## 🧠 How It Works

### Automatic Intent Detection

The system recognizes what you need and adapts its approach:

| Your Request | System Detects | Response Approach |
|--------------|----------------|-------------------|
| "track projects" | Project management need | Creates full project system |
| "meeting notes" | Content creation | Sets up structured page |
| "organize tasks" | Task management | Builds complete task system |
| "clean up workspace" | Organization task | Archives and reorganizes |
| "CRM for my business" | Complex system | Guides through CRM setup |
| "help" | Uncertain user | Offers guided options |

### Intelligent MCP Selection

| Tool | When Used | Thought Count | Purpose |
|------|-----------|---------------|---------|
| **Notion MCP** | Always | N/A | All actual Notion operations |
| **Sequential Thinking** | Simple operations | 2-3 thoughts | Linear tasks, basic updates |
| **Cascade Thinking** | Complex systems | 5-7 thoughts | Workspace design, exploration |

### Conversation Depth Scaling

The system automatically adjusts based on request clarity:

**High Clarity → Quick Execution:**
```
User: "project tracker"
System: "I'll create a comprehensive project tracker for you!
Quick question: Will you track deadlines and team assignments?"
[Creates with minimal questions]
```

**Medium Clarity → Brief Guidance:**
```
User: "organize my work"
System: "I'll help you organize your work! 
What's most important: tasks, projects, or notes?"
[Asks 1-2 questions then builds]
```

**Low Clarity → Full Guidance:**
```
User: "help"
System: "Welcome! I can help you organize anything.
What would you like to track or manage?"
[Guides through options]
```

•

## 💬 Example Interactions

### Simple Task Management
```
User: I need to track my tasks
System: I'll create a task management system for you!

Quick question: Do you need to track tasks for different projects, 
or is it more about daily to-dos?

[Creates appropriate system based on answer]
```

### Complete Business System
```
User: track everything for my business
System: I'll help you create a complete business system!

This needs several connected components:
1. What's your primary business focus?
2. Team size?
3. Most important metrics to track?

[Builds integrated system with CRM, projects, time tracking, invoicing]
```

### Organization Request
```
User: my workspace is a mess
System: I'll help you organize your workspace! 

Quick assessment:
• What's the main type of content?
• How much are we organizing?
• Want to start fresh or reorganize existing?

[Creates clean structure and organizes content]
```

•

## 📊 What Gets Created

Every workspace uses intelligent patterns:

### Business Systems
```
CRM System:
├── Clients Database (contacts, value tracking)
├── Projects Database (linked to clients)
├── Interactions Log (emails, meetings)
└── Dashboard (pipeline, metrics)
```

### Personal Productivity
```
Task Management:
├── Projects (goals, deadlines)
├── Tasks (linked to projects)
├── Today View (immediate focus)
└── Weekly Reviews (progress)
```

### Team Workspaces
```
Product Development:
├── Sprint Planning (cycles)
├── Features (user stories)
├── Bugs (tracking)
└── Team Wiki (documentation)
```

•

## 🔧 Installing MCPs (Required & Optional)

### Required: Notion MCP

The Notion MCP provides core functionality for all Notion operations.

#### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- Notion API key from [notion.so/my-integrations](https://www.notion.so/my-integrations)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the Notion Agent MCP tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/notionhq/mcp-server-notion.git (main tool)
   - https://github.com/modelcontextprotocol/server-sequential-thinking.git (optional)
   - https://github.com/cascadethinking/cascade-thinking-mcp.git (optional)
3. Set up environment variables for Notion API key
4. Create Dockerfiles if needed
5. Create a docker-compose.yml file with all services
6. Configure Claude Desktop's claude_desktop_config.json
7. Build and start the containers with docker-compose

My Notion API key is: [YOUR_API_KEY_HERE]
I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

#### Option B: NPX Setup (Quick but Less Stable)

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

### Optional: Thinking MCPs (Enhanced Intelligence)

For even better workspace design, add thinking tools:

```json
{
  "mcpServers": {
    "notion": {
      // ... notion config above
    },
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

**Benefits of Thinking MCPs:**
- **Sequential Thinking**: 2x faster simple operations
- **Cascade Thinking**: Smarter workspace design
- **Automatic selection**: Agent chooses the right tool
- **Better patterns**: Explores all options
- **Intelligent decisions**: Evaluates trade-offs

•

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Don't know where to start"** | Just describe your goal, system guides you |
| **"Can't find workspace"** | Share pages with your Notion integration |
| **"Permission denied"** | Check integration has access to workspace |
| **"API key not working"** | Verify key in .env or config file |
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
- For general issues: The AI assistant can help diagnose problems

•

## ⚠️ Important Notes

- **Natural language only** - No commands or modes needed
- **Automatic detection** - System recognizes what you need
- **Share pages required** - Integration needs access
- **No overwrites** - Always creates new or asks
- **Best practices automatic** - Professional patterns applied
- **Works without thinking MCPs** - But enhanced with them
- **Educational by design** - Teaches while building
- **2-3 questions max** - Respects your time
- **Visual feedback always** - See what's created
- **5-minute guarantee** - Complex systems ready fast

•

## 📦 Version History

- **v1.2.0**: Unified to single approach, removed modes, cleaner architecture
- **v1.1.0**: Streamlined to 3 documents, enhanced MCP intelligence
- **v1.0.0**: Initial release with 5 reference documents

•

## 📚 Resources

### Core Tools
- [Notion MCP Server](https://github.com/notionhq/mcp-server-notion) (Required)
- [Sequential Thinking MCP](https://github.com/modelcontextprotocol/server-sequential-thinking) (Optional)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp) (Optional)

### Documentation
- [Notion API Docs](https://developers.notion.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Docker Desktop](https://docs.docker.com/desktop/)

### Quick Links
- [Create Notion Integration](https://www.notion.so/my-integrations)
- [Claude Projects](https://claude.ai)
- [Share with Integration](https://www.notion.so/help/add-and-manage-connections-with-the-api)

---

*Transform ideas into organized Notion workspaces through natural conversation. Just describe what you want to organize and watch your workspace build itself. No modes, no commands, just intelligent assistance.*