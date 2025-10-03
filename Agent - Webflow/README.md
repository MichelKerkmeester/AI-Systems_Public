# Webflow Agent - User Guide v0.415

A full-stack development assistant that creates and manages Webflow sites through natural language. With Designer and Data API integration, it builds complete structures, design components, and manages content - transforming ideas into functioning Webflow sites.

## 📋 Table of Contents

- [✨ What's New in v0.415](#whats-new-in-v0415)
- [🚀 Key Features](#key-features)
- [⚡ Quick Setup](#quick-setup)
- [🔧 Installing Webflow MCP](#installing-webflow-mcp)
- [🎨 Designer API Setup](#designer-api-setup)
- [🔌 Connection Verification](#connection-verification)
- [🧠 How It Works](#how-it-works)
- [💬 Example Interactions](#example-interactions)
- [📊 What Gets Created](#what-gets-created)
- [📦 Version History](#version-history)
- [📚 Resources](#resources)

.

<a id="whats-new-in-v0415"></a>
## ✨ What's New in v0.415

### Major Update: Simplified Architecture
- **Simplified Logic**: Removed pattern learning for more predictable behavior
- **Connection Verification**: System checks MCP connection before operations
- **Clear Feedback**: Visual progress for every operation

### Core Capabilities Remain
- Full Designer API integration for visual development
- Complete Data API for structure and content
- Create collections, fields, and relationships
- Build components and design systems
- Manage responsive layouts and SEO

.

<a id="key-features"></a>
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

### System Features
- **Connection First**: Always verifies MCP connection
- **Emergency Commands**: Quick recovery with $reset, $status, $quick
- **Clear Feedback**: Visual progress for every operation
- **REPAIR Protocol**: Structured error recovery

.

<a id="quick-setup"></a>
## ⚡ Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Webflow Agent"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Webflow.md` (v0.414)
4. Save the project

### Step 3: Upload Reference Documents
Add these documents to your project:
- `Webflow - MCP Knowledge.md` (v0.314)
- `Webflow - Interactive Intelligence.md` (v0.314)
- `Webflow - Patterns & Workflows.md` (v0.314)
- `Webflow - ATLAS Framework.md` (v0.214)

### Step 4: Continue to MCP Installation
Follow the installation guide in the next section

### Step 5: Start Building!
```
Create complete blog with categories
Build hero component with animations
Design responsive navigation
Setup e-commerce catalog

Note: Use $quick prefix for faster execution when needed.
```

.

<a id="installing-webflow-mcp"></a>
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

.

<a id="designer-api-setup"></a>
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

.

<a id="connection-verification"></a>
## 🔌 Connection Verification

### Automatic Connection Check

The system automatically verifies MCP connection before operations:

```markdown
🔧 Webflow Connection Check

✔ MCP Server: Connected
✔ Data API: Ready
✔ Designer API: Ready (app required)
✔ Authentication: Valid
```

### Test Query Protocol
- Executes `webflow:sites_list()` to verify connection
- If successful: Proceeds with operations
- If failed: Applies REPAIR protocol

.

<a id="how-it-works"></a>
## 🧠 How It Works

### Native API Operations Only

```markdown
✅ CORRECT Approach:

• Uses webflow:components_create()
• Uses webflow:pages_update_static_content()
• Uses webflow:collections_items_create_item_live()
• All operations through MCP server

❌ NEVER Does This:

• Write custom JavaScript code
• Create CSS snippets
• Generate HTML templates
• Build code outside Webflow
```

### Execution Modes

The system provides two execution modes:

```markdown
📊 Standard Mode:

• Default for all operations
• Full processing and verification
• Best for complex tasks
• Shows: "Processing..."

⚡ $quick Mode:
• Type "$quick" before any command
• Minimal processing steps
• Optimized for speed
• Best for simple tasks
```

### Emergency Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| **$reset** | Clear all context | Start fresh |
| **$status** | Show current state | Check what's happening |
| **$quick** | Fast execution | Need speed |

.

<a id="example-interactions"></a>
## 💬 Example Interactions

### Creating a Blog System
```
User: Create a blog system

System: 
🔧 Webflow Connection Check

✔ MCP Server: Connected
✔ Data API: Ready

I'll create a complete blog system for you!

## Processing...

🔧 Webflow Operation

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

### Quick Mode Example
```
User: $quick add product collection

System:
⚡ Quick Mode Active!

✔ Connection verified

Creating Products collection via Data API...

✅ Collection created
✅ Basic fields added

Done! Need additional fields?
```

.

<a id="what-gets-created"></a>
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

### Execution Modes

| Mode | Speed | Best For |
|------|-------|----------|
| **Standard** | Normal | Complex operations, full structures |
| **$quick** | Faster | Simple updates, basic operations |

.

<a id="version-history"></a>
## 📦 Version History

### v0.415 (Current)
- Simplified architecture removing complex thinking mechanisms
- Streamlined execution flow
- Cleaner codebase with direct operations
- Maintained all core Webflow capabilities

### v0.414
- Introduced automatic processing systems
- Enhanced connection verification
- Improved error handling

### v0.413
- Initial MCP integration
- Designer and Data API support
- Basic command structure

.

<a id="resources"></a>
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