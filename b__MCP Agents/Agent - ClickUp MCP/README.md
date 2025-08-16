# ClickUp Agent - User Guide v1.0.0

The ClickUp Agent transforms natural language into organized ClickUp workspaces, making task management and team collaboration 10x easier. By focusing on WHAT you want to organize and WHY it matters (not HOW to build it), it bridges the gap between ideas and implementation. Interactive mode guides you through complex setups with 2-3 strategic questions.

.

## ✨ Key Features

- **Natural Language First**: Describe what you want to organize in plain English
- **4 Specialized Modes**: $interactive (default), $workspace, $content, $organize
- **Triple MCP Support**: ClickUp MCP (core), Sequential Thinking (simple), Cascade Thinking (complex)
- **Interactive Guidance**: Default mode asks 2-3 strategic questions for perfect setup
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
4. Name it "ClickUp Agent v1.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - ClickUp MCP - v1.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 3 streamlined documents to your project:
- `ClickUp - Interactive Mode - v1.0.0.md` (Conversational guidance specification)
- `ClickUp - Patterns & Operations - v1.0.0.md` (All patterns and operation mappings)
- `ClickUp - Workspace Intelligence - v1.0.0.md` (Best practices and error recovery)

### Step 4: Enable ClickUp MCP
The ClickUp MCP is already available in Claude Desktop! Just ensure it's enabled:
1. Open Claude Desktop settings
2. Check that ClickUp MCP is active
3. No API key needed - it uses your ClickUp session

### Step 5: Start Creating Workspaces
Simply describe what you need:
```
organize my projects              # Interactive mode (default)
$w complete CRM system           # Workspace mode
$c meeting notes                 # Content mode
$o archive old tasks              # Organize mode
```

.

## 🧠 Intelligent MCP Selection

The v1.0.0 release brings intelligent MCP tool selection:

### Automatic Tool Selection

| Tool | When Used | Thought Count | Purpose |
|------|-----------|---------------|---------|
| **ClickUp MCP** | Always | N/A | All actual ClickUp operations |
| **Sequential Thinking** | Simple operations | 2-3 thoughts | Linear tasks, basic updates |
| **Cascade Thinking** | Complex systems | 5-7 thoughts | Workspace design, exploration |

### Selection by Mode

| Mode | Primary MCP | Complexity | Interactive? |
|------|------------|------------|--------------|
| **Interactive** | Cascade | Adaptive | Yes (Default) |
| **Workspace** | Cascade | High | Optional |
| **Content** | Sequential | Low | No |
| **Organize** | Sequential | Medium | No |

### Example Intelligence

```markdown
User: I need to track my clients

System: [Selects Cascade Thinking for exploration]
I'll help you create a client tracking system!

Quick questions to build this perfectly:
1. What information matters most? (contact, projects, value?)
2. Do you track time for billing?
3. Solo or team use?

[Based on answers, creates complete CRM with linked lists]
```

.

## 🎛️ Operating Modes

| Mode | Command | When to Use | MCP Strategy | Focus |
|------|---------|-------------|--------------|-------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Cascade (3-5) | Conversational setup |
| **Workspace** | `$w` | Complete systems (explicit) | Cascade (5-7) | Full workspace build |
| **Content** | `$c` | Docs and documentation (explicit) | Sequential (2-3) | Content creation |
| **Organize** | `$o` | Restructuring (explicit) | Sequential (3-4) | Archive and organize |

**Note:** Interactive mode is the default unless explicitly specified with $.

.

## 💬 Interactive Mode Flow

The default conversational experience:

### Typical Flow
1. User describes need (no mode specified)
2. System identifies intent and complexity
3. Asks 2-3 strategic questions maximum
4. Shows structure preview
5. Creates complete workspace
6. Provides visual confirmation
7. Suggests logical next steps

### Quality Indicators
```markdown
📊 Workspace Creation Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MCP Used: Cascade Thinking (5 thoughts)
Complexity: Medium-High
Time to Complete: 3 minutes

✅ Created Successfully:
✔ Client space with 3 lists
✔ Project tracking with Gantt view
✔ Task management with dependencies
✔ Time tracking enabled
✔ Invoice preparation views
✔ Dashboard with key metrics

💡 ClickUp Tip: Use the Board view to visualize workflow stages
```

.

## 📍 Workspace Patterns

Every workspace uses intelligent patterns:

### Agency Systems
```markdown
Agency Hub:
├── Clients Space (contacts, projects, value)
├── Projects Lists (linked to clients)
├── Tasks (time tracking enabled)
└── Dashboard (pipeline, metrics, workload)
```

### Sprint Planning
```markdown
Development Space:
├── Sprints Folder (2-week cycles)
├── Product Backlog (prioritized)
├── Bugs List (severity tracking)
└── Velocity Dashboard (burndown, metrics)
```

### Personal Productivity
```markdown
Personal Workspace:
├── Goals & OKRs (quarterly)
├── Projects (linked to goals)
├── Daily Tasks (Me Mode view)
└── Weekly Reviews (templates)
```

.

## 🏷️ Smart Defaults

The system applies best practices automatically:

### List vs Space Decision
- **Related tasks** → Single list
- **Different workflows** → Separate lists  
- **Multiple teams** → Different spaces
- **Department work** → Space organization

### Essential Custom Fields
Every list includes relevant fields:
- **Status** (workflow states)
- **Priority** (urgency levels)
- **Due Date** (deadlines)
- **Assignees** (responsibility)
- **Time Estimate** (planning)
- **Tags** (categorization)

### View Strategy
- **List**: Mobile work, quick scanning
- **Board**: Visual workflow, drag-drop
- **Calendar**: Date-driven, scheduling
- **Gantt**: Dependencies, timeline

.

## 📋 Examples

### Interactive Mode (Default)
```
User: I need to organize my agency work
System: [Starts conversation, selects Cascade Thinking]
What types of projects do you handle? (web design, marketing, consulting?)
```

### Workspace Mode
```
User: $w sprint planning system
System: [Uses Cascade Thinking to design complete system]
Creating comprehensive sprint management workspace...
```

### Content Mode
```
User: $c team meeting notes
System: [Uses Sequential Thinking for simple creation]
Creating meeting notes doc with template...
```

### Complex System Example
```markdown
User: track everything for my startup
System: I'll help you create a complete startup system!

This needs several connected components:
1. What's your primary focus? (product, sales, operations?)
2. Team size?
3. Most important metrics to track?

[Creates integrated system with 4-5 interconnected lists]

✅ Startup Hub Created:
• Product roadmap with timeline
• Sprint planning for development
• Sales pipeline with stages
• Task management across teams
• Time tracking for resources
• Dashboard with KPIs
```

.

## 🔧 Installing MCPs (Required & Optional)

### Required: ClickUp MCP

The ClickUp MCP is **already included** in Claude Desktop! No installation needed.

**To verify it's enabled:**
1. Open Claude Desktop
2. Look for the 🔌 icon showing connected tools
3. ClickUp should appear in the list
4. Test with: "organize my tasks"

### Optional: Thinking MCPs (Enhanced Intelligence)

For even better workspace design, add thinking tools:

#### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the ClickUp Agent MCP thinking tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/modelcontextprotocol/server-sequential-thinking.git
   - https://github.com/cascadethinking/cascade-thinking-mcp.git
3. Create Dockerfiles if needed
4. Create a docker-compose.yml file with both services
5. Configure Claude Desktop's claude_desktop_config.json
6. Build and start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for running containers (sequential-thinking-mcp, cascade-thinking-mcp)
2. Look for the 🔌 icon in Claude Desktop showing connected tools
3. Test with: "create complex workspace"

#### Option B: NPX Setup (Quick but Less Stable)

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

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

**Benefits of Thinking MCPs:**
- **Sequential Thinking**: 2x faster simple operations
- **Cascade Thinking**: Smarter workspace design
- **Automatic selection**: Agent chooses the right tool
- **Better patterns**: Explores all options
- **Intelligent decisions**: Evaluates trade-offs

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Don't know where to start"** | Just describe your goal, Interactive mode guides you |
| **"Can't find my workspace"** | Check you're in the right ClickUp workspace |
| **"Permission denied"** | Verify your ClickUp permissions for that space |
| **"Too many options"** | System limits to essential features first |
| **"Tasks not linking"** | Ensure relationships are enabled in your plan |
| **"MCP not connected"** | Restart Claude Desktop |

### Quick Fixes

**Docker Issues:**
```bash
# Check if running
docker ps
# View logs
docker logs sequential-thinking-mcp
# Restart
docker-compose restart
```

**NPX Issues:**
- Ensure Node.js installed
- Check config file syntax
- Restart Claude Desktop

### Interactive Mode Help
- **Too many questions?** System limits to 2-3 strategic ones
- **Want direct creation?** Use explicit mode ($w, $c, $o)
- **Need to change approach?** System adapts mid-conversation

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **Wrong directory**: Check you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Ensure Node.js is installed for NPX method
- **Containers won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **ClickUp session expired**: Log into ClickUp in your browser

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For ClickUp issues: Verify you're logged in
- For general issues: The AI assistant can help diagnose problems

.

## ⚠️ Important Notes

- **Interactive is default** - No $ prefix needed
- **ClickUp login required** - Be logged into ClickUp
- **No overwrites** - Always creates new or asks
- **Best practices automatic** - Professional patterns applied
- **Works without thinking MCPs** - But enhanced with them
- **Educational by design** - Teaches while building
- **2-3 questions max** - Respects your time
- **Visual feedback always** - See what's created
- **5-minute guarantee** - Complex systems ready fast

.

## 📦 Version History

- **v1.0.0**: Initial release with 3 streamlined documents, ClickUp-optimized architecture

.

## 📚 Resources

### Core Tools
- [ClickUp MCP](https://github.com/clickup/mcp-server-clickup) (Included in Claude)
- [Sequential Thinking MCP](https://github.com/modelcontextprotocol/server-sequential-thinking) (Optional)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp) (Optional)

### Documentation
- [ClickUp API Docs](https://clickup.com/api)
- [ClickUp Help Center](https://help.clickup.com/)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Docker Desktop](https://docs.docker.com/desktop/)

### Quick Links
- [ClickUp Login](https://app.clickup.com)
- [Claude Projects](https://claude.ai)
- [ClickUp Features Guide](https://help.clickup.com/hc/en-us/categories/6314476398999-Features)

.

---

*Transform ideas into organized ClickUp workspaces through natural conversation. Interactive mode guides you with 2-3 questions. Complex systems ready in under 5 minutes. Just describe what you want to organize and watch your workspace build itself.*