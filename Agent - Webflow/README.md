# Webflow Agent - User Guide v0.411

The Webflow Agent is a full-stack development assistant that creates and manages Webflow sites through natural language. With Designer and Data API integration, it can build complete structures, design components, and manage content - transforming ideas into functioning Webflow sites.

## 📋 Table of Contents

- [✨ What's New in v0.411](#whats-new-in-v0411)
- [🚀 Key Features](#key-features)
- [⚡ Quick Setup](#quick-setup)
- [🔌 Connection Verification](#connection-verification)
- [🧠 How It Works](#how-it-works)
- [💬 Example Interactions](#example-interactions)
- [📊 What Gets Created](#what-gets-created)
- [🔧 Installing Webflow MCP](#installing-webflow-mcp)
- [🎨 Designer API Setup](#designer-api-setup)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📦 Version History](#version-history)
- [📚 Resources](#resources)

---

## ✨ What's New in v0.411

### Critical Updates
- **Connection Verification**: System now checks MCP connection before any operations
- **Native API Only**: Explicit clarification - NEVER writes custom code, uses only Webflow APIs
- **Consistent Formatting**: Standardized divider style throughout (─────────────────)

### Improved User Experience
- **User-Controlled Thinking**: You choose processing depth (1-10 rounds)
- **Simplified Commands**: Just 3 emergency commands for quick recovery
- **Cleaner Architecture**: Reduced redundancy, focused documentation
- **REPAIR Protocol**: Structured error recovery with clear alternatives
- **Visual Standardization**: Consistent feedback format across all operations

### Core Capabilities Remain
- Full Designer API integration for visual development
- Complete Data API for structure and content
- Create collections, fields, and relationships
- Build components and design systems
- Manage responsive layouts and SEO

### What Changed from v0.410
- ✅ **Connection check first** - Verifies MCP before operations
- ✅ **Native API emphasis** - No custom code generation ever
- ✅ **Consistent dividers** - Clean visual formatting
- ✅ **Test query protocol** - Validates connection with simple query

---

## 🚀 Key Features

### Complete Development Capabilities

**Designer API Features (NO CUSTOM CODE):**
- **Element Creation**: Build elements using native Webflow Designer API
- **Style Management**: Apply styles through API calls only
- **Component Building**: Create reusable components natively
- **Responsive Control**: Manage breakpoints via API
- **Variable System**: Use Webflow's design tokens
- **Real-time Preview**: See changes instantly in Designer

**Important**: The system NEVER writes custom JavaScript, CSS, or HTML code. All operations use native Webflow APIs exclusively.

**Data API Features:**
- **Collection Creation**: Build complete data structures
- **Field Management**: Add any field type to collections
- **Relationship Design**: Create references between collections
- **Content Operations**: Full CRUD on items
- **Publishing Control**: Manage draft/live states
- **SEO Optimization**: Meta tags and structured data

**Integrated Workflows:**
- Create blog with structure and templates
- Build e-commerce catalogs with components
- Design landing pages with dynamic content
- Establish complete design systems
- Develop responsive layouts
- Manage multi-language sites

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
3. Click "Create project"
4. Name it "Webflow Agent"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Webflow.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 4 essential documents to your project:
- `Webflow - MCP Knowledge.md` (Single source of truth)
- `Webflow - Interactive Intelligence.md` (Conversation patterns)
- `Webflow - Patterns & Workflows.md` (Development patterns)
- `Webflow - ATLAS Thinking Framework.md` (Adaptive thinking)

### Step 4: Install Webflow MCP Server
Follow the installation guide in the [Installing Webflow MCP](#installing-webflow-mcp) section below.

### Step 5: Setup Designer Access
1. Open your site in Webflow Designer
2. Press 'E' to open Apps panel
3. Launch "Webflow MCP Bridge App"
4. Keep it open for Designer operations

### Step 6: Verify Connection
The system will automatically check connection on first use:
```
🔧 Webflow Connection Check
─────────────────
✓ MCP Server: Connected
✓ Data API: Ready
✓ Designer API: Ready (app required)
✓ Authentication: Valid
```

### Step 7: Start Building!
```
Create complete blog with categories
Build hero component with animations
Design responsive navigation
Setup e-commerce catalog
Create design system
Build landing pages
```

---

## 🔌 Connection Verification

### Automatic Connection Check

The system now automatically verifies MCP connection before any operations:

```markdown
🔧 Webflow Connection Check
─────────────────
Verifying MCP server connection...

✓ MCP Server: Connected
✓ Data API: Available
✓ Designer API: Available (requires app)
✓ Authentication: Valid

Connection established successfully!
```

### Test Query Protocol

Before executing operations, the system runs a simple test query:
- Executes `webflow:sites_list()` to verify connection
- If successful: Proceeds with operations
- If failed: Applies REPAIR protocol

### Connection Troubleshooting

| Issue | Solution | Action |
|-------|----------|--------|
| **MCP not connected** | Restart Claude | Cmd/Ctrl+R |
| **Auth failed** | Re-authorize | Check OAuth |
| **Config issue** | Check config file | See installation |
| **App disconnected** | Open Bridge App | Press 'E' in Designer |

---

## 🧠 How It Works

### Native API Operations Only

**CRITICAL**: The system uses ONLY native Webflow APIs:

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

### Thinking Depth Guide

| Rounds | Best For | Example Operations |
|--------|----------|-------------------|
| **1-2** | Simple updates | Edit content, update field |
| **3-4** | Structure creation | Create collection with fields |
| **5-6** | Component building | Design cards, navigation |
| **7-8** | Page design | Full layouts with components |
| **9-10** | Complete systems | Design systems, full sites |

### Emergency Commands

Only 3 commands for quick recovery:

| Command | Purpose | When to Use |
|---------|---------|-------------|
| **$reset** | Clear all context | Start completely fresh |
| **$status** | Show current state | Check what's happening |
| **$quick** | Skip to execution | Fast mode, minimal questions |

---

## 💬 Example Interactions

### Creating with Connection Check
```
User: Create a blog system

System: 
🔧 Webflow Connection Check
─────────────────
✓ MCP Server: Connected
✓ Data API: Ready

I'll create a complete blog system for you!

How many thinking rounds should I use? (1-10)
Recommended: 4 rounds for structure creation

User: 4

System: [Using 4 rounds of thinking...]

🔧 Webflow Operation
─────────────────
Thinking: 4 rounds
Operation: Blog structure creation
APIs: Data API

📂 Processing:
├── Creating collections ✔
├── Adding fields ✔
└── Setting relationships ✔

Progress: [████████████████] 100%
Time: 12 seconds
API calls: 15/60 🟢

✅ Operation Complete!

📊 Results:
├── Collections: 3 created
├── Fields: 18 added
├── Relationships: 2 configured
└── Performance: Optimal

💡 Insight:
Reference fields link your content for dynamic relationships!

🎯 Next Steps:
• Add sample content
• Create page templates
• Build components
```

### Using Emergency Commands
```
User: $status

System: 
🔧 Current System Status
─────────────────
• MCP Connection: Connected ✅
• Collections created: 3
• Components built: 2
• Thinking patterns: Blog structures
• API usage: 23/60 🟢
• Companion app: Connected

All options available.
```

```
User: $quick - add product collection

System: 
Quick Mode Active!
─────────────────
How many thinking rounds? (1-10)
[Quick mode suggests: 2 rounds]

User: 2

System: [Using 2 rounds - fast execution]
Creating Products collection...
✅ Collection created with basic fields
Done! Need additional customization?
```

---

## 📊 What Gets Created

### Full Stack Example - Blog System (Native APIs Only)

```javascript
// Data Structure (4 rounds thinking) - Created via Data API
Collections: {
  BlogPosts: {
    fields: ['title', 'content', 'excerpt', 'featured_image',
             'author', 'categories', 'published_date', 'meta_fields']
  },
  Authors: {
    fields: ['name', 'bio', 'avatar', 'social_links']
  },
  Categories: {
    fields: ['name', 'slug', 'description']
  }
}

// Components (5-6 rounds thinking) - Created via Designer API
Components: {
  BlogCard: 'Native Webflow component with image, title, excerpt',
  AuthorBio: 'Native author information block',
  CategoryFilter: 'Native dynamic filtering component'
}

// Complete Page (7-8 rounds thinking) - Built with both APIs
Page: {
  Hero: 'Native featured post section',
  Grid: 'Native blog post grid layout',
  Sidebar: 'Native categories and archives',
  Responsive: 'Native mobile-optimized design'
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

### Enabling Designer Operations (Native API Only)

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

### Important: No Custom Code

The Designer API creates elements using Webflow's native capabilities only:
- ✅ Uses Webflow's element creation API
- ✅ Applies styles through native API calls
- ✅ Builds components with Webflow's system
- ❌ Never writes custom JavaScript
- ❌ Never creates custom CSS
- ❌ Never generates HTML templates

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
| **Rate limited** | Wait 60 seconds | - |
| **Images failing** | Use external URLs | - |

### Connection Issues

**If MCP connection fails:**
```markdown
⚠️ MCP Connection Issue
─────────────────
1. Restart Claude Desktop (Cmd/Ctrl+R)
2. Check config file location
3. Verify OAuth authorization
4. Run test query again
```

### Designer Connection

**If Designer operations fail:**
```markdown
⚠️ Designer API Unavailable
─────────────────
1. Check MCP Bridge App is open
2. Look for "Connected" status
3. Refresh Designer if needed
4. Re-launch app from Apps panel
```

---

## ⚠️ Important Notes

### System Principles
- **Connection First**: Always verifies MCP connection before operations
- **Native APIs Only**: Never generates custom code, uses Webflow APIs exclusively
- **User Control**: You always choose thinking depth (1-10)
- **Pattern Learning**: System adapts but never restricts options
- **Clear Recovery**: Only 3 emergency commands needed
- **Visual Feedback**: Every operation shows progress
- **Best Practices**: Applied automatically unless overridden

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

### v0.411 (Current - Connection & Clarity Update)
- **Connection verification** - Checks MCP before operations
- **Native API emphasis** - No custom code generation
- **Consistent formatting** - Standardized dividers
- **Test query protocol** - Validates connection

### v0.410 (UX Update)
- **User-controlled thinking** - Choose 1-10 rounds
- **Simplified commands** - Only $reset, $status, $quick
- **REPAIR protocol** - Structured error recovery
- **Cleaner architecture** - Reduced redundancy
- **Pattern clarity** - Inform but never restrict

### v0.400
- Designer API integration
- Full visual development
- Component building
- Style management

### v0.300
- Content management only
- Could not create structures
- Many limitations

### Earlier Versions
- v0.200: Reality-based approach
- v0.100: Initial release

---

## 📚 Resources

### Essential Links
- [Webflow MCP Server](https://github.com/webflow/mcp-server) - Official repository
- [Designer API Docs](https://developers.webflow.com/designer/reference) - Visual operations
- [Data API Docs](https://developers.webflow.com/data/reference) - Data operations
- [MCP Protocol](https://modelcontextprotocol.io/) - Protocol documentation

### Quick References
- [Get API Token](https://webflow.com/dashboard/account/apps)
- [Webflow Designer](https://webflow.com/designer)
- [Claude Desktop](https://claude.ai/download)
- [Cloudinary](https://cloudinary.com/) - Image hosting

### Support
- [Webflow Support](https://support.webflow.com)
- [Developer Forum](https://forum.webflow.com)
- Email: developers@webflow.com

---

*Full-stack Webflow development through natural language. Native APIs only - no custom code. Connection verified before operations. You choose the depth. Patterns guide but never restrict.*