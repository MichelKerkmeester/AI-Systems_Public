# Webflow Agent - User Guide v0.300

The Webflow Agent is a reality-based content management assistant that works within actual MCP capabilities. It excels at managing content in existing Webflow structures while transparently guiding you to Designer when structural changes are needed. No false promises, just genuine value within real constraints.

## 📋 Table of Contents

- [🆕 What's New in v0.300](#whats-new-in-v300)
- [✨ Key Features](#key-features)
- [⚠️ Reality Check](#reality-check)
- [🚀 Quick Setup](#quick-setup)
- [🧠 How It Works](#how-it-works)
- [💬 Example Interactions](#example-interactions)
- [📊 What Gets Managed](#what-gets-managed)
- [🔧 Installing Webflow MCP (Required)](#installing-webflow-mcp-required)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📦 Version History](#version-history)
- [📚 Resources](#resources)

.

## 🆕 What's New in v0.300

### Document Architecture Overhaul
- **Cleaner Python Usage**: Reduced to essential logic only (not for lists/descriptions)
- **Aligned with Best Practices**: Follows Document Beautifier formatting standards
- **Improved Organization**: Better structured reference documents
- **Enhanced Readability**: Clearer separation of concepts

### Refined ATLAS Framework
- **Reality-First Thinking**: Every phase checks MCP capabilities
- **Smarter Round Calculation**: More accurate complexity assessment
- **Pattern Learning**: Better adaptation to user preferences
- **REPAIR Protocol**: Enhanced error recovery

### Better User Experience
- **Clearer Visual Feedback**: Shows what's happening in real-time
- **Improved Error Messages**: More helpful guidance when things can't be done
- **Streamlined Conversations**: Fewer unnecessary questions
- **Consistent Responses**: Predictable patterns across operations

.

## ✨ Key Features

### What This System Actually Does
- **Manages Content**: Create, update, delete items in existing collections
- **Handles Publishing**: Draft/live states, staging/production deployment
- **Optimizes SEO**: Meta tags, descriptions, slugs at scale
- **Bulk Operations**: Process multiple items efficiently
- **Script Management**: Add and manage site scripts
- **Localization**: Update content across locales
- **Visual Progress**: Real-time operation feedback
- **Error Recovery**: 95% success rate for possible operations
- **Rate Limit Management**: Automatic throttling and queuing
- **Educational Approach**: Explains limitations and guides to Designer
- **Pattern Learning**: Remembers your structure and preferences
- **Transparent Communication**: Always clear about capabilities

### What It Cannot Do (Designer Required)
- ❌ **Create fields** in collections
- ❌ **Upload images** directly (external URLs only)
- ❌ **Build collection structures**
- ❌ **Create new pages**
- ❌ **Apply CSS or design systems**
- ❌ **Set up relationships between collections**
- ❌ **Create components or symbols**
- ❌ **Modify field types**

.

## ⚠️ Reality Check

### The Truth About Webflow MCP
The Webflow MCP is a powerful **content management tool**, not a **site builder**. It excels at managing content within existing structures but cannot create those structures.

**Correct Positioning:**
> "I manage your Webflow content brilliantly after you've set up the structure in Designer."

### Version 3.0 Improvements
- More transparent about limitations upfront
- Better guidance when Designer is needed
- Clearer workaround suggestions
- Improved pattern recognition

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Webflow Agent"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Webflow - v0.300.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 5 essential documents to your project:
- `Agent - MCP - Webflow - v0.300.md` (Main agent)
- `Webflow - MCP Knowledge - v0.300.md` (Central knowledge)
- `Webflow - Interactive Intelligence - v0.300.md` (Conversation patterns)
- `Webflow - Patterns & Workflows - v0.300.md` (Operation mappings)
- `Webflow - ATLAS Thinking Framework - v0.200.md` (Reality-based thinking)
- `README.md` (This guide)

### Step 4: Prepare Your Webflow Structure
**IMPORTANT: Before using the agent:**
1. Create your collections in Webflow Designer
2. Add all needed fields to collections
3. Set up any relationships
4. Publish the structure
5. Get your API key from [Webflow Account Settings](https://webflow.com/dashboard/account/apps)

### Step 5: Start Managing Content
With structure ready, you can now:
```
update all blog posts
create product in existing collection
publish to production
update SEO metadata
manage draft content
```

The system will transparently tell you if something needs Designer first!

.

## 🧠 How It Works

### Reality-Based Intent Recognition

The system checks every request against actual capabilities:

| Request Type | Can Do? | Response | Action |
|-------------|---------|----------|--------|
| **Content Update** | ✅ Yes | "I can update that!" | Execute |
| **Field Creation** | ❌ No | "Add in Designer first" | Guide |
| **Publishing** | ✅ Yes | "Publishing now!" | Execute |
| **Image Upload** | ❌ No | "Use external URLs" | Workaround |
| **SEO Update** | ✅ Yes | "Updating metadata!" | Execute |
| **Page Creation** | ❌ No | "Create in Designer" | Guide |

### Capability-Aware Conversation

**High Clarity → Quick Execution (if possible):**
```
User: "update product prices"
System: "I can update prices in your existing products!

Processing...
✅ Updated 47 products
Time: 23 seconds"
```

**Structural Request → Designer Guidance:**
```
User: "add featured image field"
System: "I cannot create fields through the API.

To add a featured image field:
1. Open Webflow Designer
2. Go to your collection settings
3. Add new field → Image type
4. Name it 'featured_image'
5. Publish changes

Once added, I can populate it with image URLs!"
```

**Workaround Offered:**
```
User: "upload product images"
System: "I cannot upload images directly. Here are your options:

1. Use external hosting (Cloudinary/S3)
2. Upload via Designer's Asset Manager
3. Provide direct URLs

Which approach works for you?"
```

.

## 💬 Example Interactions

### Successful Content Management
```
User: update all blog post meta descriptions

System: How many thinking rounds should I use? (1-10)
Recommended: 3 rounds (bulk operation)

User: 3

System: I can update all meta descriptions!

Checking your Blog Posts collection...
✅ Found: 52 posts
✅ Field exists: meta_description

Updating all posts...
[████████████] 100%

✅ Updated 52 meta descriptions
Time: 26 seconds
API calls: 52/60

Ready to publish these changes?
```

### Structure Creation (Not Possible)
```
User: create a blog with categories and authors

System: I need to clarify my capabilities:

❌ What I CANNOT do:
• Create new collections
• Add fields to collections
• Set up relationships

✅ What I CAN do (after Designer setup):
• Create and manage blog posts
• Assign categories and authors
• Handle publishing
• Optimize SEO

To proceed, first create in Designer:
1. Blog Posts collection with fields
2. Categories collection
3. Authors collection
4. Reference fields linking them

Then I can manage all your content!
```

### Bulk Operations (Within Limits)
```
User: import 50 products

System: I can create products in your existing collection!

Checking Products collection...
✅ Collection exists
✅ Required fields present

Note: Images must be external URLs (I cannot upload files)

Creating 50 products...
[████████████] 100%

✅ Import complete!
• 50 products created
• All in draft status
• Time: 90 seconds

Ready to publish?
```

.

## 📊 What Gets Managed

### Content Within Existing Structures

**Blog Management (structure must exist):**
```
Prerequisites (Designer):
✅ Blog Posts collection exists
✅ All fields created
✅ Categories collection exists
✅ Relationships defined

What I Can Do:
• Create new posts (3s each)
• Update existing posts (2s each)
• Assign categories (1s)
• Update SEO metadata (2s)
• Publish to live (3s)
• Bulk operations (1-2s per item)
```

**E-commerce Management:**
```
Prerequisites (Designer):
✅ Products collection exists
✅ All product fields created
✅ Categories set up
✅ Images hosted externally

What I Can Do:
• Update product information
• Manage inventory
• Update pricing
• Assign categories
• Publish changes

Cannot Do:
• Upload product images
• Create variant fields
• Add new attributes
```

.

## 🔧 Installing Webflow MCP (Required)

The Webflow Agent requires the Webflow MCP tool to function.

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- Webflow API key from [Webflow Account Settings](https://webflow.com/dashboard/account/apps)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker container for Webflow MCP.

Repository: https://github.com/webflow/mcp-server-webflow.git
API key: [YOUR_WEBFLOW_KEY]
Directory: "$HOME/MCP Servers/webflow"
OS: [Windows/Mac/Linux]

Need: Dockerfile, docker-compose.yml, and Claude Desktop config.
```

### Option B: NPX Setup (Quick but Less Stable)

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "webflow": {
      "command": "npx",
      "args": ["-y", "@webflow/mcp-server-webflow"],
      "env": {
        "WEBFLOW_API_KEY": "your-webflow-key-here"
      }
    }
  }
}
```

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Reality | Solution |
|-------|---------|----------|
| **"Cannot create field"** | MCP limitation | Create in Designer first |
| **"Cannot upload image"** | MCP limitation | Use external URL |
| **"Collection not found"** | Doesn't exist | Create in Designer |
| **"Field doesn't exist"** | Not created yet | Add field in Designer |
| **"Rate limit exceeded"** | API limit | Wait 60s, auto-resumes |
| **"Structure needed"** | No collections | Set up in Designer |

### API Rate Limits

Standardized limits:
- **Maximum**: 60 requests/minute
- **Warning**: 50 requests/minute
- **Throttle**: 55 requests/minute
- **Recovery**: 60 second wait

### Performance Benchmarks

| Operation | Time | API Calls | Success Rate |
|-----------|------|-----------|--------------|
| **Create item** | 2-3s | 1-2 | 95% |
| **Update item** | 1-2s | 1 | 98% |
| **Bulk 50 items** | 60-90s | 50 | 90% |
| **Publish** | 3-5s | 2-3 | 95% |
| **Field creation** | N/A | N/A | 0% (impossible) |
| **Image upload** | N/A | N/A | 0% (use URLs) |

.

## ⚠️ Important Notes

### Reality-Based Operation
- **Structure first** - Collections and fields must exist in Designer
- **Content management** - Agent excels at managing existing content
- **No field creation** - Cannot create or modify field structures
- **No image upload** - Use external URLs only
- **Transparent limits** - Always clear about what's not possible
- **Designer guidance** - Clear steps when structure changes needed
- **Workarounds offered** - Creative solutions within constraints
- **Pattern learning** - Remembers your structure
- **Rate limit safe** - Automatic throttling
- **Error recovery** - 95% success for possible operations

### Best Practices
1. Set up complete structure in Designer first
2. Prepare content with external image URLs
3. Use agent for content management
4. Return to Designer for structural changes
5. Accept workarounds when offered

.

## 📦 Version History

### v0.300 (Current)
- **Document overhaul**: Cleaner Python usage, better organization
- **Improved ATLAS**: Reality-first thinking at every phase
- **Enhanced patterns**: Better learning and adaptation
- **Refined conversations**: Fewer questions, clearer responses
- **Visual improvements**: Better progress and error feedback

### v0.200
- **Reality alignment**: Corrected capability claims
- **Transparent limitations**: Clear about what's not possible
- **Enhanced guidance**: Better Designer coordination
- **Workaround documentation**: Creative solutions
- **Removed false claims**: No field creation, no image upload

### v0.100 (Deprecated)
- Initial release with incorrect capability claims
- Claimed field creation (not possible)
- Claimed image upload (not possible)
- Claimed design system application (not possible)

.

## 📚 Resources

### Core Tools
- [Webflow MCP Server](https://github.com/webflow/mcp-server-webflow) (Required)
- [Claude Projects](https://claude.ai) (Platform)

### Documentation
- [Webflow Designer Guide](https://university.webflow.com/lesson/intro-to-webflow-designer)
- [Webflow CMS Guide](https://university.webflow.com/lesson/intro-to-the-webflow-cms)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [API Rate Limits](https://developers.webflow.com/reference/rate-limits)

### Quick Links
- [Get Webflow API Key](https://webflow.com/dashboard/account/apps)
- [Webflow Designer](https://webflow.com/designer)
- [Claude Desktop](https://claude.ai/download)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### External Image Hosting
- [Cloudinary](https://cloudinary.com/) - Free tier available
- [Amazon S3](https://aws.amazon.com/s3/) - Pay as you go
- [Imgur](https://imgur.com/) - Free image hosting
- [ImageKit](https://imagekit.io/) - CDN with optimization

### Performance Guidelines
- **Content operations**: 2-5 seconds
- **Bulk operations**: 1-2 seconds per item
- **Publishing**: 3-5 seconds
- **Rate limiting**: Automatic at 55/60 requests
- **Designer tasks**: Manual, then content management

---

*Reality-based Webflow content management. Excel at what's possible within existing structures. Transparent about limitations. Clear guidance to Designer when needed. No false promises, just genuine value within real constraints.*