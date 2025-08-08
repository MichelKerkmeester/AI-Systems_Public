# Notion Agent - User Guide v1.1.0

The Notion Agent transforms natural language into organized Notion workspaces, making database creation and workspace management 10x easier. By focusing on WHAT you want to organize and WHY it matters (not HOW to build it), it bridges the gap between ideas and implementation. Interactive mode guides you through complex setups with 2-3 strategic questions.

## 🆕 What's New in v1.1.0

- **Streamlined Architecture**: Reduced from 5 to 3 lean reference documents
- **Enhanced MCP Intelligence**: Smarter selection between Sequential and Cascade Thinking
- **Faster Processing**: 60-70% reduction in document size
- **Clearer Patterns**: Consolidated operations and patterns into single reference
- **Maintained Features**: All v1.0.0 features preserved with improved efficiency

## ✨ Key Features

- **Natural Language First**: Describe what you want to organize in plain English
- **4 Specialized Modes**: $interactive (default), $workspace, $content, $organize
- **Triple MCP Support**: Notion MCP (core), Sequential Thinking (simple), Cascade Thinking (complex)
- **Interactive Guidance**: Default mode asks 2-3 strategic questions for perfect setup
- **Best Practices Built-in**: Professional workspace patterns applied automatically
- **Visual Feedback**: Clear structure previews and success confirmations
- **Educational Focus**: Teaches Notion concepts through successful creation
- **5-Minute Setup**: Complete workspace systems ready in minutes
- **Zero Technical Knowledge**: No understanding of Notion's interface required

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Notion Agent v1.1"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - Notion MCP - v1.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 3 streamlined documents to your project:
- `Notion - Interactive Mode - v1.0.0.md` (Conversational guidance specification)
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
organize my projects              # Interactive mode (default)
$w complete CRM system           # Workspace mode
$c meeting notes                 # Content mode
$o archive old tasks              # Organize mode
```

## 🧠 Intelligent MCP Selection

The v1.1.0 update revolutionizes how MCP tools work together:

### Automatic Tool Selection

| Tool | When Used | Thought Count | Purpose |
|------|-----------|---------------|---------|
| **Notion MCP** | Always | N/A | All actual Notion operations |
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
2. Do you track interactions or just contacts?
3. Solo or team use?

[Based on answers, creates complete CRM with linked databases]
```

## 🎛️ Operating Modes

| Mode | Command | When to Use | MCP Strategy | Focus |
|------|---------|-------------|--------------|-------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Cascade (3-5) | Conversational setup |
| **Workspace** | `$w` | Complete systems (explicit) | Cascade (5-7) | Full workspace build |
| **Content** | `$c` | Pages and writing (explicit) | Sequential (2-3) | Content creation |
| **Organize** | `$o` | Restructuring (explicit) | Sequential (3-4) | Archive and organize |

**Note:** Interactive mode is the default unless explicitly specified with $.

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
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MCP Used: Cascade Thinking (5 thoughts)
Complexity: Medium-High
Time to Complete: 3 minutes

✅ Created Successfully:
✓ Project database with 8 properties
✓ Task database linked to projects
✓ 3 views per database (Table, Board, Calendar)
✓ Dashboard with key metrics
✓ Templates for consistency
✓ Archive system configured

💡 Notion Tip: Use the Board view to visualize workflow stages
```

## 📝 Workspace Patterns

Every workspace uses intelligent patterns:

### Business Systems
```markdown
CRM System:
├── Clients Database (contacts, industry, value)
├── Projects Database (linked to clients)
├── Interactions Log (emails, meetings, calls)
└── Dashboard (pipeline, metrics, activity)
```

### Personal Productivity
```markdown
Task Management:
├── Projects (goals, deadlines, status)
├── Tasks (linked to projects, priorities)
├── Daily Notes (capture, reflection)
└── Weekly Reviews (progress, planning)
```

### Team Workspaces
```markdown
Product Development:
├── Sprint Planning (2-week cycles)
├── Features (user stories, points)
├── Bugs (severity, assignment)
└── Team Wiki (documentation)
```

## 🏷️ Smart Defaults

The system applies best practices automatically:

### Database vs Page Decision
- **Multiple similar items** → Database
- **Need filtering/sorting** → Database  
- **Unique content** → Page
- **Static information** → Page

### Essential Properties
Every database includes:
- **Title** (always required)
- **Status** (workflow states)
- **Date** (relevant timeline)
- **Owner** (responsibility)
- **Category** (organization)

### View Strategy
- **Table**: Desktop work, data comparison
- **Board**: Visual workflow, drag-drop
- **Calendar**: Date-driven, scheduling
- **List**: Mobile-friendly, simple

## 📋 Examples

### Interactive Mode (Default)
```
User: I need to organize my research
System: [Starts conversation, selects Cascade Thinking]
What kind of research? (academic, market, personal?)
```

### Workspace Mode
```
User: $w project management system
System: [Uses Cascade Thinking to design complete system]
Creating comprehensive project management workspace...
```

### Content Mode
```
User: $c team meeting notes
System: [Uses Sequential Thinking for simple creation]
Creating meeting notes page with template...
```

### Complex System Example
```markdown
User: track everything for my business
System: I'll help you create a complete business system!

This needs several connected components:
1. What's your primary business focus?
2. Team size?
3. Most important metrics to track?

[Creates integrated system with 4-5 databases]

✅ Business Hub Created:
• CRM for client management
• Projects linked to clients
• Tasks linked to projects
• Time tracking with invoicing
• Dashboard with business metrics
```

## 🔧 Installing Notion MCP (Required)

The Notion MCP provides core functionality. Choose your installation method:

### Option A: Docker Setup (Recommended - Stable)

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))
- Notion API key from [notion.so/my-integrations](https://www.notion.so/my-integrations)

**Quick Docker Setup:**

1. Create directory and clone:
```bash
mkdir -p "$HOME/MCP Servers" && cd "$HOME/MCP Servers"
git clone https://github.com/notionhq/mcp-server-notion.git
cd mcp-server-notion
```

2. Add your API key:
```bash
echo "NOTION_API_KEY=your-key-here" > .env
```

3. Create docker-compose.yml:
```yaml
version: '3.8'
services:
  notion-mcp:
    build: .
    environment:
      - NOTION_API_KEY=${NOTION_API_KEY}
    restart: unless-stopped
```

4. Start container:
```bash
docker-compose up -d
```

5. Configure Claude Desktop (see config location below)

### Option B: NPX Installation (Quick Setup)

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

**Verification:**
1. Restart Claude Desktop
2. Look for 🔌 icon showing connected tools
3. Test with: "organize my tasks"

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Don't know where to start"** | Just describe your goal, Interactive mode guides you |
| **"Can't find workspace"** | Share pages with your Notion integration |
| **"Permission denied"** | Check integration has access to workspace |
| **"API key not working"** | Verify key in .env or config file |
| **"Rate limited"** | System auto-retries with backoff |
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

### Interactive Mode Help
- **Too many questions?** System limits to 2-3 strategic ones
- **Want direct creation?** Use explicit mode ($w, $c, $o)
- **Need to change approach?** System adapts mid-conversation

### Getting Help
- Docker logs: `docker logs notion-mcp`
- Config issues: Check JSON syntax
- Notion issues: Verify integration settings
- General help: System provides clear error messages

## ⚠️ Important Notes

- **Interactive is default** - No $ prefix needed
- **Share pages required** - Integration needs access
- **No overwrites** - Always creates new or asks
- **Best practices automatic** - Professional patterns applied
- **Works without thinking MCPs** - But enhanced with them
- **Educational by design** - Teaches while building
- **2-3 questions max** - Respects your time
- **Visual feedback always** - See what's created
- **5-minute guarantee** - Complex systems ready fast

## 📦 Version History

- **v1.1.0**: Streamlined to 3 documents, enhanced MCP intelligence, 60% faster
- **v1.0.0**: Initial release with 5 reference documents

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

*Transform ideas into organized Notion workspaces through natural conversation. Interactive mode guides you with 2-3 questions. Complex systems ready in under 5 minutes. Just describe what you want to organize and watch your workspace build itself.*