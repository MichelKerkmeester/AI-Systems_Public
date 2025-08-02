# Notion Agent - User Guide v2.0

## 🚀 What is This?

The Notion Agent transforms natural language into Notion operations, making workspace management 10x easier. Instead of clicking through menus and learning Notion's interface, just describe what you want in plain English.

**Key Benefits:**
- Transform conversations into complete Notion structures
- No need to understand Notion's interface or terminology
- Get intelligent workspace organization with best practices built-in
- Interactive mode guides you through complex setups (DEFAULT)
- Educational system teaches Notion concepts while you work
- Automatic error recovery with helpful suggestions
- Professional patterns applied to every creation

**Key Principle:** If you can describe it, the agent can build it in Notion.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Notion Agent v2.0"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Agent - Notion MCP - v1.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Upload all reference documents to your project:
- `Notion - Best Practices - v1.0.0.md` (workspace design patterns)
- `Notion - Error Handling - v1.0.0.md` (graceful recovery)
- `Notion - Interactive Mode - v1.0.0.md` (conversational guidance)
- `Notion - Pattern Library - v1.0.0.md` (pre-built structures)
- `Notion - Quick Operations - v1.0.0.md` (common operations)

### Step 4: Get Your Notion API Key
1. Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Click "New integration"
3. Give it a name (e.g., "Claude Assistant")
4. Copy the API key for MCP setup

### Step 5: Start Using Natural Language!
Begin any conversation in the project, and Claude will guide you through creating Notion workspaces conversationally.

.

## 🧠 Enhanced Intelligence: Triple MCP Support

### What's New in v2.0?
The Notion Agent intelligently chooses between three tools based on your needs:

1. **Notion MCP** - Core tool for all Notion operations
2. **Sequential Thinking MCP** - For straightforward, linear operations
3. **Cascade Thinking MCP** - For complex workspace design and exploration

The system automatically selects the best tool(s) and adapts the analysis approach.

### Intelligent Selection Logic

**Sequential Thinking is chosen for:**
- Simple page or task creation
- Basic content updates
- Clear, single-step operations
- Quick organization tasks

**Cascade Thinking is chosen for:**
- Interactive mode conversations (DEFAULT)
- Complex workspace setup
- Multi-database systems
- Exploring design options
- Pattern selection decisions

**Notion MCP is always used for:**
- All actual Notion operations
- Workspace navigation
- Content creation and updates
- Database and page management

### Adaptive Thought Process

The system uses a flexible approach:
- **Simple requests:** 2-3 thoughts
- **Standard operations:** 3-4 thoughts
- **Interactive guidance:** 3-5 thoughts
- **Complex systems:** 5-7 thoughts with exploration

.

## 🎯 How to Use

### Basic Usage (Interactive Mode - DEFAULT)
Simply describe what you need:
```
I need to organize my projects
```

The system will:
1. Start Interactive Mode automatically
2. Ask 2-3 clarifying questions
3. Choose appropriate MCP tools
4. Design the perfect structure
5. Create everything in Notion
6. Teach you why it works

### Example Conversations

**Simple Request:**
```
User: Create a task list
System: I'll help you set up a task management system! 

What types of tasks will you track? (work, personal, or both?)
```

**Complex System:**
```
User: I need a complete CRM for my business
System: Excellent! Let's build a comprehensive CRM system together.

Quick questions to customize this perfectly:
1. What information is most important about each client?
2. Do you track interactions or just contact info?
3. Will this be used by a team or just you?
```

### Mode Selection
| Mode | Command | Use For | Typical MCPs Used |
|------|---------|---------|-------------------|
| **Interactive** | `$interactive` or `$int` | DEFAULT - Guided creation | Cascade + Notion |
| **Workspace** | `$workspace` or `$w` | Complete systems (explicit only) | Cascade + Notion |
| **Content** | `$content` or `$c` | Writing and pages (explicit only) | Sequential + Notion |
| **Organize** | `$organize` or `$o` | Restructuring (explicit only) | Sequential + Notion |

.

## ✅ Output Format

### Visual Feedback for Every Operation
```
MODE: $interactive → $workspace
OPERATION TYPE: Database Creation
MCP USED: Cascade Thinking + Notion

📊 Creating: Project Tracker Database
📍 Location: /Workspace/Projects/
⏳ Setting up structure...

✅ Created successfully!
• 8 properties configured
• 3 views created (Active, Timeline, Archive)
• Template ready for new projects

💡 Pro tip: Use the Timeline view to visualize project deadlines

Try: "Add first project" or "Show me the timeline"
```

### Intelligent Pattern Application
- **Project Trackers**: Status workflow, timeline views, templates
- **Task Systems**: Priority sorting, due date tracking, assignments
- **Knowledge Bases**: Tags, search optimization, relations
- **Team Spaces**: Permission management, shared resources
- **CRM Systems**: Contact linking, interaction history, pipelines

### Educational Integration
Every operation teaches you Notion:
```
💡 "I used a database instead of pages because it lets you filter, 
sort, and create different views of your projects. This scales 
better as you add more items."
```

.

## 🔧 Installing MCP Tools (Recommended)

The system intelligently selects between these based on task complexity. Choose either Docker (stable) or NPX (quick) installation:

### Option A: AI-Powered Docker Setup (Recommended)

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
   - https://github.com/arben-adm/mcp-sequential-thinking.git
   - https://github.com/drewdotpro/cascade-thinking-mcp.git
   - https://github.com/notionhq/mcp-server-notion.git
3. Create a docker-compose.yml file with services for all three
4. Set up a .env file with NOTION_API_KEY=[my key]
5. Configure Claude Desktop's claude_desktop_config.json
6. Start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for 3 running containers
2. Look for the 🔌 icon in Claude Desktop showing available tools
3. Test with: "Create a simple task list in Notion"

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
    },
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

**Important:** Don't forget to share pages with your Notion integration!

.

## 🆘 Troubleshooting

### "I don't know where to start"
- Just describe your goal in plain language
- Interactive mode will guide you step by step
- Try: "Help me get organized" or "I need to track [anything]"

### "Can't find my workspace / Permission denied"
- Check workspace access settings
- Share pages with Notion integration
- System suggests alternatives automatically
- Can create in personal space if needed

### "Notion API key issues"
- One-time setup: [notion.so/my-integrations](https://www.notion.so/my-integrations)
- Create new integration and copy API key
- Add to Docker .env file or NPX config

### "Operation failed or rate limited"
- System queues and retries automatically
- Handles sync problems gracefully
- Suggests optimization for large databases
- Breaks complex formulas into simpler parts

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop  
- **Wrong directory**: Check you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Ensure Node.js is installed for NPX method
- **Containers won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **Rate limits**: All tools handle this gracefully with retries

### Other Issues
- **No MCP tools**: System works without them (reduced functionality)
- **Wrong MCP selection**: Based on complexity automatically
- **Interactive not wanted**: Use explicit mode (`$w`, `$c`, etc.)
- **Too complex**: System adapts to your expertise level

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For Notion issues: Check API integration settings
- For general issues: The AI assistant can help diagnose problems

.

## ⚠️ Important Notes

- **Interactive mode is DEFAULT** - Unless explicitly specified otherwise
- **Never overwrites data** - Always creates new or asks permission
- **Works without MCPs** - But significantly enhanced with them
- **Respects permissions** - Only accesses shared pages
- **Educational approach** - Teaches Notion concepts as you work

## 📦 Version History

- **v2.0.0**: Enhanced MCP selection, updated setup guides
- **v1.0.0**: Initial Notion agent with interactive mode

## 🎯 Key Principles

1. **Natural language first** - Describe what you want, not how
2. **Learn while doing** - Every operation teaches Notion concepts
3. **Best practices built-in** - Professional patterns automatically applied
4. **Graceful error handling** - Never leaves you stuck
5. **Progressive complexity** - Starts simple, grows with your needs

.

## 📚 Other Resources

- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Sequential Thinking MCP](https://github.com/arben-adm/mcp-sequential-thinking)
- [Cascade Thinking MCP](https://github.com/drewdotpro/cascade-thinking-mcp)
- [Notion MCP Server](https://github.com/notionhq/mcp-server-notion)
- [Notion API Documentation](https://developers.notion.com/)
- [Notion Integration Setup](https://www.notion.so/my-integrations)

---

*Transform natural language into organized Notion workspaces. Just describe what you want to organize, and watch your workspace build itself while you learn.*