# Webflow Agent - User Guide v0.411

A full-stack development assistant that creates and manages Webflow sites through natural language. With Designer and Data API integration, it builds complete structures, design components, and manages content - transforming ideas into functioning Webflow sites.

## 📋 Table of Contents

- [✨ What's New in v0.411](#whats-new-in-v0411)
- [🚀 Key Features](#key-features)
- [⚡ Quick Setup](#quick-setup)
- [🔧 Installing Webflow MCP](#installing-webflow-mcp)
- [🎨 Designer API Setup](#designer-api-setup)
- [📌 Connection Verification](#connection-verification)
- [🧠 How It Works](#how-it-works)
- [💬 Example Interactions](#example-interactions)
- [📊 What Gets Created](#what-gets-created)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📦 Version History](#version-history)
- [📚 Resources](#resources)

---

## ✨ What's New in v0.411

### Critical Updates
- **Connection Verification**: System checks MCP connection before operations
- **Native API Only**: NEVER writes custom code, uses only Webflow APIs
- **Consistent Formatting**: Standardized divider style throughout

### Core Capabilities Remain
- Full Designer API integration for visual development
- Complete Data API for structure and content
- Create collections, fields, and relationships
- Build components and design systems
- Manage responsive layouts and SEO

---

## 🚀 Key Features

### Complete Development Capabilities

**Designer API Features (NO CUSTOM CODE):**
- Build elements using native Webflow Designer API
- Apply styles through API calls only
- Create reusable components natively
- Manage breakpoints via API
- Use Webflow's design tokens
- Real-time preview in Designer

**Data API Features:**
- Build complete data structures
- Add any field type to collections
- Create references between collections
- Full CRUD on items
- Manage draft/live states
- SEO optimization

**Important**: The system NEVER writes custom JavaScript, CSS, or HTML code. All operations use native Webflow APIs exclusively.

### User Control Features
- **Choose Your Depth**: Select 1-10 thinking rounds for any operation
- **Emergency Commands**: Quick recovery with $reset, $status, $quick
- **Pattern Learning**: System adapts but never restricts options
- **Clear Feedback**: Visual progress for every operation

---

## ⚡ Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Webflow Agent"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Webflow.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these documents to your project:
- `Webflow - MCP Knowledge.md`
- `Webflow - Interactive Intelligence.md`
- `Webflow - Patterns & Workflows.md`
- `Webflow - ATLAS Thinking Framework.md`

### Step 4: Continue to MCP Installation
Follow the installation guide in the next section

### Step 5: Start Building!
```
Create complete blog with categories
Build hero component with animations
Design responsive navigation
Setup e-commerce catalog
```

---

## 🔧 Installing Webflow MCP

### Recommended: OAuth Remote Setup

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "webflow": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.webflow.com/sse"]
    }
  }
}
```

After saving:
1. Restart Claude Desktop (Cmd/Ctrl + R)
2. Browser opens for OAuth authorization
3. Authorize the sites you want to access
4. MCP Bridge App auto-installs to authorized sites
5. System verifies connection automatically

### Alternative: Token-Based Setup
```json
{
  "mcpServers": {
    "webflow": {
      "command": "npx",
      "args": ["-y", "@webflow/mcp-server"],
      "env": {
        "WEBFLOW_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

Get your token from [Webflow API Settings](https://webflow.com/dashboard/account/apps).

---

## 🎨 Designer API Setup

### Enabling Designer Operations

1. **Open Webflow Designer**
   - Navigate to your project
   - Open in Designer mode

2. **Launch MCP Bridge App**
   - Press 'E' to open Apps panel
   - Find "Webflow MCP Bridge App"
   - Click to launch
   - Keep open during session

3. **Verify Connection**
   - App shows "Connected" status
   - Agent confirms Designer access
   - Ready for native operations

### What Requires the App

**Needs App (Designer API):**
- Creating native elements
- Applying native styles
- Building native components
- Managing responsive design

**Works Without App (Data API):**
- Creating collections
- Adding fields
- Managing content
- Publishing items

---

## 📌 Connection Verification

### Automatic Connection Check

The system automatically verifies MCP connection before operations:

```markdown
🔧 Webflow Connection Check
─────────────────
✔ MCP Server: Connected
✔ Data API: Ready
✔ Designer API: Ready (app required)
✔ Authentication: Valid
```

### Test Query Protocol
- Executes `webflow:sites_list()` to verify connection
- If successful: Proceeds with operations
- If failed: Applies REPAIR protocol

---

## 🧠 How It Works

### Native API Operations Only

```markdown
✅ CORRECT Approach:
─────────────────
• Uses webflow:components_create()
• Uses webflow:pages_update_static_content()
• Uses webflow:collections_items_create_item_live()
• All operations through MCP server

❌ NEVER Does This:
─────────────────
• Write custom JavaScript code
• Create CSS snippets
• Generate HTML templates
• Build code outside Webflow
```

### User-Controlled Thinking

For every operation, you choose the processing depth:

```markdown
How many thinking rounds should I use? (1-10)

Based on your request, I recommend: [X rounds]
- Creating: [what you're building]
- Complexity: [Simple/Standard/Complex]

Or specify your preferred number.
```

### Emergency Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| **$reset** | Clear all context | Start fresh |
| **$status** | Show current state | Check what's happening |
| **$quick** | Skip to execution | Fast mode |

---

## 💬 Example Interactions

### Creating with Connection Check
```
User: Create a blog system

System: 
🔧 Webflow Connection Check
─────────────────
✔ MCP Server: Connected
✔ Data API: Ready

I'll create a complete blog system for you!

How many thinking rounds should I use? (1-10)
Recommended: 4 rounds for structure creation

User: 4

System: [Using 4 rounds of thinking...]

🔧 Webflow Operation
─────────────────
Thinking: 4 rounds
Operation: Blog structure creation

📂 Processing:
├── Creating collections ✔
├── Adding fields ✔
└── Setting relationships ✔

Progress: [████████████████] 100%
API calls: 15/60 🟢

✅ Operation Complete!

📊 Results:
├── Collections: 3 created
├── Fields: 18 added
└── Relationships: 2 configured

💡 Reference fields link your content!
```

---

## 📊 What Gets Created

### Full Stack Example - Blog System

```javascript
// Data Structure (Created via Data API)
Collections: {
  BlogPosts: {
    fields: ['title', 'content', 'excerpt', 'featured_image',
             'author', 'categories', 'published_date']
  },
  Authors: {
    fields: ['name', 'bio', 'avatar']
  },
  Categories: {
    fields: ['name', 'slug', 'description']
  }
}

// Components (Created via Designer API)
Components: {
  BlogCard: 'Native Webflow component',
  AuthorBio: 'Native author block',
  CategoryFilter: 'Native filtering component'
}
```

### Performance by Thinking Depth

| Depth | Speed | Quality | Best For |
|-------|-------|---------|----------|
| 1-2 rounds | Fastest | Basic | Quick fixes |
| 3-4 rounds | Fast | Good | Standard operations |
| 5-6 rounds | Moderate | Better | Complex structures |
| 7-8 rounds | Slower | Best | Full features |
| 9-10 rounds | Slowest | Maximum | Complete systems |

---

## 🆘 Troubleshooting

### REPAIR Protocol

When errors occur, the system uses REPAIR:

**R**ecognize - Identify the issue
**E**xplain - Clear explanation
**P**ropose - Multiple solutions
**A**dapt - Based on your choice
**I**terate - Try the solution
**R**ecord - Learn from it

### Common Issues & Solutions

| Issue | Solution | Command |
|-------|----------|---------|
| **MCP not connected** | Restart Claude | Cmd/Ctrl+R |
| **Confused context** | Clear everything | `$reset` |
| **Want current state** | Check status | `$status` |
| **Need speed** | Fast execution | `$quick` |
| **App disconnected** | Open MCP Bridge App | - |

---

## ⚠️ Important Notes

### System Principles
- **Connection First**: Always verifies MCP connection
- **Native APIs Only**: Never generates custom code
- **User Control**: You always choose thinking depth (1-10)
- **Pattern Learning**: System adapts but never restricts
- **Clear Recovery**: Only 3 emergency commands needed
- **Visual Feedback**: Every operation shows progress

### Requirements
- **MCP Connection**: Must be verified before operations
- **MCP Bridge App**: Must be open for Designer operations
- **Authorization**: Owner/admin access required
- **External Images**: URLs required (no direct upload)
- **Rate Limits**: 60 requests per minute
- **Node.js**: Version 22.3.0+ for MCP server

### Limitations
- Cannot upload images directly (use Cloudinary/S3)
- Cannot write custom code (native APIs only)
- Designer API requires companion app
- Rate limited to 60 API calls/minute
- Must have owner/admin permissions

---

## 📦 Version History

### v0.411 (Current)
- Connection verification - Checks MCP before operations
- Native API emphasis - No custom code generation
- Consistent formatting - Standardized dividers

### v0.410
- User-controlled thinking - Choose 1-10 rounds
- Simplified commands - Only $reset, $status, $quick
- REPAIR protocol - Structured error recovery

### Previous Versions
- v0.400: Designer API integration
- v0.300: Content management only
- v0.200: Reality-based approach

---

## 📚 Resources

### Essential Links
- [Webflow MCP Server](https://github.com/webflow/mcp-server)
- [Designer API Docs](https://developers.webflow.com/designer/reference)
- [Data API Docs](https://developers.webflow.com/data/reference)
- [MCP Protocol](https://modelcontextprotocol.io/)

### Quick References
- [Get API Token](https://webflow.com/dashboard/account/apps)
- [Webflow Designer](https://webflow.com/designer)
- [Claude Desktop](https://claude.ai/download)
- [Cloudinary](https://cloudinary.com/) - Image hosting

---

*Full-stack Webflow development through natural language. Native APIs only - no custom code. Connection verified before operations. You choose the depth. Patterns guide but never restrict.*