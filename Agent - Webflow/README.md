<<<<<<< HEAD
# Webflow Agent - User Guide v0.414
=======
# Webflow Agent - User Guide v3.0.0
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

A full-stack development assistant that creates and manages Webflow sites through natural language. With Designer and Data API integration, it builds complete structures, design components, and manages content - transforming ideas into functioning Webflow sites with automatic UltraThink processing.

## 📋 Table of Contents

<<<<<<< HEAD
- [✨ What's New in v0.413](#whats-new-in-v0413)
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

.

## ✨ What's New in v0.414
=======
- [🆕 What's New in v3.0.0](#-whats-new-in-v300)
- [✨ Key Features](#-key-features)
- [⚠️ Reality Check](#️-reality-check)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 How It Works](#-how-it-works)
- [💬 Example Interactions](#-example-interactions)
- [📊 What Gets Managed](#-what-gets-managed)
- [🔧 Installing MCPs (Required)](#-installing-mcps-required)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## 🆕 What's New in v3.0.0
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

### Major Update: Automatic UltraThink Processing
- **UltraThink Automatic**: System now uses 10 rounds of thinking automatically - no user prompts
- **No More Questions**: Removed all "How many thinking rounds?" prompts
- **$quick Mode Enhanced**: Adaptive 1-5 rounds based on automatic complexity analysis
- **Silent Processing**: Maximum depth analysis without interrupting workflow

### Core Updates
- **Connection Verification**: System checks MCP connection before operations
- **Native API Only**: NEVER writes custom code, uses only Webflow APIs
- **Consistent Formatting**: Standardized divider style throughout

### Core Capabilities Remain
- Full Designer API integration for visual development
- Complete Data API for structure and content
- Create collections, fields, and relationships
- Build components and design systems
- Manage responsive layouts and SEO

.

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

### Automatic Processing Features
- **UltraThink by Default**: Automatic 10-round deep analysis for all operations
- **No User Prompting**: Never asks about thinking depth
- **$quick Mode**: Fast execution with adaptive 1-5 rounds
- **Emergency Commands**: Quick recovery with $reset, $status, $quick
- **Pattern Learning**: System adapts but never restricts options
- **Clear Feedback**: Visual progress for every operation

.

## ⚡ Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Webflow Agent"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
<<<<<<< HEAD
3. Copy and paste: `Agent - MCP - Webflow.md` (v0.413)
4. Save the project

### Step 3: Upload Reference Documents
Add these documents to your project:
- `Webflow - MCP Knowledge.md` (v0.313)
- `Webflow - Interactive Intelligence.md` (v0.313)
- `Webflow - Patterns & Workflows.md` (v0.313)
- `Webflow - ATLAS Thinking Framework.md` (v0.213)
=======
3. Copy and paste: `Agent - MCP - Webflow - v3.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 5 essential documents to your project:
- `Agent - MCP - Webflow - v3.0.0.md` (Main agent)
- `Webflow - MCP Knowledge - v3.0.0.md` (Central knowledge)
- `Webflow - Interactive Intelligence - v3.0.0.md` (Conversation patterns)
- `Webflow - Patterns & Workflows - v3.0.0.md` (Operation mappings)
- `Webflow - ATLAS Thinking Framework - v2.0.0.md` (Reality-based thinking)
- `README.md` (This guide)
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

### Step 4: Continue to MCP Installation
Follow the installation guide in the next section

### Step 5: Start Building!
```
Create complete blog with categories
Build hero component with animations
Design responsive navigation
Setup e-commerce catalog

Note: All operations now use automatic UltraThink processing!
Use $quick prefix for faster execution when needed.
```

.

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

## 📌 Connection Verification

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

### Automatic UltraThink Processing

The system now automatically applies maximum depth analysis:

```markdown
🧠 UltraThink Processing:

• Standard Operations: Automatic 10 rounds
• Never asks user about depth
• Silent processing for best results
• Shows: "Processing with UltraThink..."

⚡ $quick Mode:
• Type "$quick" before any command
• Adaptive 1-5 rounds based on complexity
• Optimized for speed when needed
```

### Emergency Commands

| Command | Purpose | When to Use | Processing |
|---------|---------|-------------|------------|
| **$reset** | Clear all context | Start fresh | Returns to UltraThink |
| **$status** | Show current state | Check what's happening | Immediate |
| **$quick** | Fast execution | Need speed | Adaptive 1-5 rounds |

.

## 💬 Example Interactions

### Creating with UltraThink (Automatic)
```
User: Create a blog system

System: 
🔧 Webflow Connection Check

✔ MCP Server: Connected
✔ Data API: Ready

I'll create a complete blog system for you!

## Processing with UltraThink...

🔧 Webflow Operation

Processing: UltraThink (10 rounds)
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

Processing with adaptive thinking...
Complexity: Basic structure (2 rounds)

Creating Products collection via Data API...

✅ Collection created
✅ Basic fields added

Done! Need additional fields?
```

.

## 📊 What Gets Created

### Full Stack Example - Blog System

```javascript
// Data Structure (Created via Data API with UltraThink)
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

// Components (Created via Designer API with UltraThink)
Components: {
  BlogCard: 'Native Webflow component',
  AuthorBio: 'Native author block',
  CategoryFilter: 'Native filtering component'
}
```

### Processing Modes

| Mode | Processing | Speed | Quality | When to Use |
|------|------------|-------|---------|-------------|
| **UltraThink** | 10 rounds (automatic) | Slower | Maximum | Default for all operations |
| **$quick** | 1-5 rounds (adaptive) | Faster | Good | When speed matters |

### $quick Mode Complexity Analysis

| Request Type | Adaptive Rounds | Example |
|--------------|-----------------|---------|
| Simple update | 1 round | $quick update title |
| Basic creation | 2 rounds | $quick add field |
| Standard structure | 3 rounds | $quick create collection |
| Complex operation | 4 rounds | $quick build component |
| Multi-step task | 5 rounds | $quick setup page |

.

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
| **Need faster execution** | Use quick mode | `$quick [command]` |
| **App disconnected** | Open MCP Bridge App | - |

.

## ⚠️ Important Notes

### System Principles
- **Connection First**: Always verifies MCP connection
- **Native APIs Only**: Never generates custom code
- **UltraThink Automatic**: Always applies 10 rounds unless $quick
- **No User Prompting**: Never asks about thinking depth
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

<<<<<<< HEAD
### Limitations
- Cannot upload images directly (use Cloudinary/S3)
- Cannot write custom code (native APIs only)
- Designer API requires companion app
- Rate limited to 60 API calls/minute
- Must have owner/admin permissions
=======
.

## 📦 Version History

### v3.0.0 (Current)
- **Document overhaul**: Cleaner Python usage, better organization
- **Improved ATLAS**: Reality-first thinking at every phase
- **Enhanced patterns**: Better learning and adaptation
- **Refined conversations**: Fewer questions, clearer responses
- **Visual improvements**: Better progress and error feedback

### v2.0.0
- **Reality alignment**: Corrected capability claims
- **Transparent limitations**: Clear about what's not possible
- **Enhanced guidance**: Better Designer coordination
- **Workaround documentation**: Creative solutions
- **Removed false claims**: No field creation, no image upload

### v1.0.0 (Deprecated)
- Initial release with incorrect capability claims
- Claimed field creation (not possible)
- Claimed image upload (not possible)
- Claimed design system application (not possible)
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

.

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

*Full-stack Webflow development through natural language. Native APIs only - no custom code. Connection verified before operations. **UltraThink processing automatic - maximum depth, no questions asked.** Patterns guide but never restrict.*