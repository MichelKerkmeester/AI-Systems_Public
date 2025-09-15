# ClickUp & Notion Agent - User Guide v0.100

An intelligent productivity system that transforms natural language requests into precise workspace operations through conversational guidance. Seamlessly coordinates between Notion (knowledge management) and ClickUp (task management) with smart defaults and pattern learning.

## 📋 Table of Contents

- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🔧 Installing MCP Tools](#installing-mcp-tools)
- [🧠 How It Works](#how-it-works)
- [🎛️ Operating Modes](#operating-modes)
- [💬 Example Interactions](#example-interactions)
- [📊 Visual Feedback](#visual-feedback)
- [⚡ Emergency Commands](#emergency-commands)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📚 Resources](#resources)

.

## ✨ Key Features

### Core Capabilities
- **MCP Connection Verification**: Always checks server availability first
- **Intelligent Platform Selection**: Recommends Notion or ClickUp based on use case
- **Natural Language Understanding**: Describe what you want in plain words
- **SYNC Framework**: 4-phase thinking methodology
- **User-Controlled Depth**: Choose 1-10 thinking rounds
- **Challenge Mode**: Questions complexity at 3+ rounds
- **Pattern Learning**: Adapts to your preferences
- **Visual Feedback**: Real-time progress in chat
- **Rate Limiting**: Smart API usage management
- **Educational Insights**: Learn why certain approaches work

### What It Can Do

**Notion Operations:**
- Create pages and hierarchical structures
- Build databases with custom properties
- Design multiple views (table, board, calendar)
- Manage blocks and rich text content
- Handle comments and collaboration
- Search across workspace
- Create templates and relations

**ClickUp Operations:**
- Create and manage tasks with custom fields
- Build list, folder, and space hierarchies
- Track time with native timers
- Bulk operations for efficiency
- Manage team assignments
- Create documents and wikis
- Add file attachments (via URLs)
- Configure automations

### What It Cannot Do
- ❌ Real-time sync between platforms
- ❌ Direct file uploads (URLs only)
- ❌ Modify workspace settings
- ❌ Complex automations
- ❌ Cross-platform webhooks
- ❌ Advanced permissions management

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "ClickUp & Notion Helper"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - ClickUp & Notion.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these documents to your project:
- `ClickUp & Notion - Interactive Intelligence.md`
- `ClickUp & Notion - Patterns & Workflows.md`
- `ClickUp & Notion - SYNC Thinking Framework.md`
- `Notion - MCP Intelligence.md`
- `ClickUp - MCP Intelligence.md`

### Step 4: Continue to MCP Installation
See next section for detailed setup

### Step 5: Start Working
```
create a project management system    # Interactive platform selection
$notion build knowledge base          # Direct Notion mode
$clickup setup sprint tasks          # Direct ClickUp mode
organize my work                     # Interactive discovery
```

.

## 🔧 Installing MCP Tools

The system requires two MCP servers:

### Prerequisites
- Node.js 18+
- Claude Desktop app
- Notion integration token
- ClickUp API token

### Getting API Tokens

**Notion Integration Token:**
1. Go to https://www.notion.so/my-integrations
2. Create new integration
3. Copy the token
4. Share pages/databases with your integration

**ClickUp API Token:**
1. Go to ClickUp Settings
2. Click "Apps"
3. Click "Generate" under API Token
4. Copy the token

### Option A: NPM Installation (Recommended)

**Install both servers:**
```bash
npm install -g @makenotion/notion-mcp-server
npm install -g @clickup/mcp-server-clickup
```

**Configure Claude Desktop:**
```json
{
  "mcpServers": {
    "notion": {
      "command": "notion-mcp-server",
      "env": {
        "NOTION_API_TOKEN": "your-notion-token"
      }
    },
    "clickup": {
      "command": "clickup-mcp-server",
      "env": {
        "CLICKUP_API_TOKEN": "your-clickup-token"
      }
    }
  }
}
```

### Option B: Local Installation
1. Clone repositories
2. Install dependencies
3. Configure with local paths

**Config Location:**
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/claude/claude_desktop_config.json`

### Verification
After installation, restart Claude Desktop and check:
```
🔧 Setup Verification

✔ Notion: Connected
✔ ClickUp: Connected
✔ Tokens: Valid
✔ Configuration: Complete

Ready for productivity operations!
```

.

## 🧠 How It Works

### MCP Connection Verification
System always verifies connections first:
```
📌 MCP Connection Check

• Notion: ✅ Connected
• ClickUp: ✅ Connected

All productivity operations available.
```

### Platform Selection (Interactive Mode)
When no mode specified, system helps choose:
```
Which platform would work better?

🎯 **Notion** - Choose for:
• Knowledge bases and wikis
• Documentation with formatting
• Databases with multiple views
• Content that needs hierarchy

📊 **ClickUp** - Choose for:
• Task and project management
• Time tracking needs
• Team assignments
• Workflow automation
```

### SYNC Thinking Framework
1. **Pre-Check**: Verify MCP connections
2. **S - Survey**: Analyze requirements
3. **Y - Yield**: Generate optimal solutions
4. **N - Navigate**: Select best path
5. **C - Create**: Execute and confirm

### Challenge Mode
Activates at 3+ thinking rounds:
```
Full system would include:
• 20 custom fields
• Multiple automations

Simpler alternative:
• 5 essential fields
• Basic workflow

Which approach?
```

.

## 🎛️ Operating Modes

| Mode | Command | Purpose | Use When |
|------|---------|---------|----------|
| **Interactive** | DEFAULT | Platform selection + guided | Not sure which tool |
| **Notion** | `$notion` | Notion operations | Knowledge management |
| **ClickUp** | `$clickup` | ClickUp operations | Task management |

### Mode Activation

**Interactive Mode (Default):**
```
User: help organize my work
System: I can help you organize!

Which platform would suit better?

🎯 **Notion** - Best for:
• Documentation
• Knowledge base
• Meeting notes

📊 **ClickUp** - Best for:
• Task tracking
• Project management
• Time tracking
```

**Direct Mode:**
```
User: $notion create project documentation
System: ✅ Notion connected!

How many thinking rounds? (1-10)
Recommended: 4 for structured documentation
```

.

## 💬 Example Interactions

### Creating a Knowledge Base
```
User: build team knowledge base

System: For a knowledge base, I'd recommend **Notion** because:
• Superior rich text editing
• Nested page hierarchies
• Better for documentation

Would you like to proceed with Notion?

User: Notion is perfect

System: How many thinking rounds? (1-10)
Recommended: 4 rounds

User: 4

System: [Using 4 rounds of SYNC thinking]

🎯 Productivity Operation

Platform: Notion
Operation: Knowledge base creation

📂 Processing:
├── Creating main workspace page ✔
├── Setting up category structure ✔
├── Building article database ✔
└── Adding templates ✔

Progress: [████████████████] 100%
API calls: 5/60 🟢

✅ Operation Complete!

📊 Results:
├── Main page created
├── 5 category sections
├── Article database with views
└── Templates ready

💡 Use database views to filter by category

🎯 Next Steps:
• Add your first articles
• Invite team members
• Customize templates
```

.

## 📊 Visual Feedback

All operations display real-time feedback:

### Standard Operation Display
```
🎯 Productivity Operation

Thinking: [X rounds]
Platform: [Notion/ClickUp/Both]
Operation: [Description]

📂 Processing:
├── Step 1: [description] ✔
├── Step 2: [description] ✔
└── Step 3: [description] ⟳

Progress: [████████████████] 100%
API calls: [X/60] [Status]

✅ Results: [Metrics]
💡 Tip: [Educational insight]
📝 Location: [Where to find it]
```

### API Usage Indicators
- 🟢 **Green (0-30)**: Safe zone
- 🟡 **Yellow (31-45)**: Caution
- 🟠 **Orange (46-50)**: Warning
- 🔴 **Red (51-55)**: Critical
- ⛔ **Limit (60)**: Wait required

.

## ⚡ Emergency Commands

| Command | Action | Result | Use When |
|---------|--------|--------|----------|
| **`$reset`** | Clear all context | Fresh start | Switching projects |
| **`$quick`** | Fast processing | Minimal questions | Know what you want |
| **`$status`** | Show patterns | Display context | Check what's tracked |

### Command Examples
```
$reset
# Clears all patterns and history

$quick add task "Review proposal"
# Skips discovery, minimal rounds

$status
# Shows patterns and MCP status
```

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **MCP not connected** | Server not running | Restart Claude Desktop |
| **Auth failed** | Invalid token | Check and update tokens |
| **Not found** | Wrong ID/name | Verify workspace access |
| **Rate limited** | Too many requests | Wait 60 seconds |
| **Wrong platform** | Operation mismatch | Switch to correct platform |
| **No access** | Permission issue | Check integration access |

### MCP Connection Issues
```
⚠️ MCP Connection Failed

1. Verify API tokens
2. Check configuration file
3. Restart Claude Desktop
4. Test tokens in API playground
```

### Quick Fixes
```
$status    # Check current state
$reset     # Clear if needed
$quick     # Fast mode
```

.

## ⚠️ Important Notes

### Best Practices
- **Check connections**: System verifies MCP servers automatically
- **Choose right platform**: Notion for docs, ClickUp for tasks
- **Start simple**: Accept challenge suggestions
- **Watch rate limits**: Monitor API usage indicator
- **Use templates**: Create once, reuse often
- **Batch operations**: Process similar items together

### Platform Selection Guide
| Use Case | Best Platform | Why |
|----------|--------------|-----|
| Documentation | Notion | Rich text, hierarchy |
| Task Management | ClickUp | Native features |
| Knowledge Base | Notion | Better organization |
| Time Tracking | ClickUp | Built-in timers |
| Meeting Notes | Notion | Formatting options |
| Sprint Planning | ClickUp | Agile features |

### Performance Guidelines
- **MCP Check**: <1 second
- **Page/Task creation**: 1-3 seconds
- **Database/List setup**: 3-5 seconds
- **Bulk operations**: 1-2 seconds per item
- **Search operations**: 2-5 seconds
- **Rate limit**: 60-100 requests per minute

.

## 📚 Resources

### MCP Server Documentation
- [Notion MCP Server](https://github.com/makenotion/notion-mcp-server)
- [ClickUp MCP Server](https://github.com/clickup/mcp-server-clickup)

### Platform Documentation
- [Notion API Documentation](https://developers.notion.com/)
- [ClickUp API Documentation](https://clickup.com/api)
- [Notion Help Center](https://www.notion.so/help)
- [ClickUp Help Center](https://help.clickup.com/)

### Productivity Methodologies
- [Getting Things Done (GTD)](https://gettingthingsdone.com/)
- [PARA Method](https://fortelabs.co/blog/para/)
- [Agile/Scrum Guide](https://www.scrum.org/resources/scrum-guide)
- [Zettelkasten Method](https://zettelkasten.de/)

### Tools & Platforms
- [Claude Desktop](https://claude.ai/download)
- [Notion](https://www.notion.so/)
- [ClickUp](https://clickup.com/)
- [Make (Integromat)](https://www.make.com/)

---

*Transform natural language into professional productivity operations. MCP connections verified automatically. Intelligent platform selection between Notion and ClickUp. Challenge complexity, embrace simplicity, deliver organization.*