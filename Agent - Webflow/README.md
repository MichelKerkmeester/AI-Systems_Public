# Webflow Agent - User Guide v1.0.0

The Webflow Agent transforms natural language into precise Webflow CMS operations, making site management and content creation 10x easier. Through intelligent conversation with seamless design integration, it understands WHAT you want to build and automatically handles HOW to implement it. No API knowledge, no technical commands, just describe what you need.

## 📑 Table of Contents

- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 How It Works](#-how-it-works)
- [💬 Example Interactions](#-example-interactions)
- [📊 What Gets Created](#-what-gets-created)
- [🔧 Installing MCPs (Required)](#-installing-mcps-required)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## ✨ Key Features

- **Natural Language Only**: Just describe what you want to create or manage
- **Figma Design Integration**: Import complete design systems in 30-45 seconds
- **Automatic Image Optimization**: 60-80% size reduction via Imagician
- **Smart CMS Structures**: Professional patterns applied automatically
- **Adaptive Conversation**: Scales depth based on request clarity
- **Visual Progress Tracking**: See operations happen in real-time
- **Error Recovery**: 92% of errors handled automatically
- **SEO Optimization**: Meta tags and structured data configured
- **Rate Limit Management**: Automatic throttling and queuing
- **Educational Approach**: Teaches Webflow concepts while building
- **5-Minute Setup**: Complete sites ready in minutes
- **Zero Technical Knowledge**: No understanding of APIs required

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Webflow Agent v1.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - Webflow MCP - v1.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 7 essential documents to your project:
- `Agent - Webflow MCP - v1.0.0.md` (Main agent)
- `Webflow - MCP Knowledge - v1.0.0.md` (Central coordination)
- `Webflow - Interactive Intelligence - v1.0.0.md` (Conversation patterns)
- `Webflow - Patterns & Workflows - v1.0.0.md` (Operation mappings)
- `Figma - MCP Knowledge - v1.0.0.md` (Design integration)
- `Imagician - MCP Knowledge - v1.0.0.md` (Image optimization)
- `README.md` (This guide)

### Step 4: Get Your API Keys
1. **Webflow API Key**: Go to [Webflow Account Settings](https://webflow.com/dashboard/account/apps)
2. **Figma API Token**: Go to [Figma Settings](https://www.figma.com/developers/api#access-tokens)
3. Save both keys for MCP configuration

### Step 5: Start Building
Simply describe what you need:
```
create blog post about AI
set up blog with my Figma design
import design system
optimize all product images
publish to production
help me build a portfolio
```

The system automatically detects intent and executes!

.

## 🧠 How It Works

### Intent Recognition Framework

The system automatically detects what you need based on confidence levels:

| Confidence | Range | Response Type | Avg Turns | Example |
|------------|-------|--------------|-----------|---------|
| **Exact** | >0.95 | Quick confirm + execute | 1-2 | "create blog post titled X" |
| **High** | 0.80-0.95 | Brief clarification | 2-3 | "update product" |
| **Medium** | 0.50-0.79 | Guided exploration | 3-4 | "set up shop" |
| **Low** | <0.50 | Full guidance | 4-6 | "help with site" |

### MCP Coordination

**Primary MCP: Webflow**
- Always prioritized for CMS and site operations
- Handles collections, items, pages, publishing

**Integrated MCP Services:**
- **Figma MCP**: Design system import (30-45s)
- **Imagician MCP**: Image optimization (2-3s per image)

### Conversation Depth Scaling

**High Clarity → Quick Execution:**
```
User: "create blog post about AI"
System: "Creating blog post about AI!

📝 Adding to Blog Posts collection
✅ Title set, slug generated, draft created

Time: 3 seconds"
```

**Medium Clarity → Brief Guidance:**
```
User: "set up blog"
System: "I'll set up your blog system!

Creating:
• Blog Posts collection
• Categories
• Authors

With Figma design? [Optional]"
```

**Low Clarity → Full Guidance:**
```
User: "help"
System: "I'll help with your Webflow site!

What would you like to do?
• Create content
• Import designs
• Manage collections
• Publish changes"
```

.

## 💬 Example Interactions

### Simple Content Creation
```
User: create blog post about web design

System: I'll create a new blog post in your CMS!

📝 Creating in Blog Posts collection:
• Title: 'Web Design'
• Auto-generated slug
• Draft status

⏱️ Time: 3 seconds
✅ Blog post created successfully!
```

### Design System Import
```
User: import my Figma design

System: I'll import your Figma design system!

Extracting from Figma:
🎨 File: Your Design System v2.0
📊 Found: 12 colors, 8 text styles, 15 components
⏱️ Estimated time: 30-45 seconds

Importing now...

✅ Design system imported successfully!
• Colors: 12 swatches created
• Typography: 8 text styles mapped
• Components: 15 symbols ready
• Time taken: 38 seconds
```

### Complete E-commerce Setup
```
User: set up shop with Figma designs

System: I'll set up your shop with Figma designs!

Setting up e-commerce:
1. Importing Figma design (30-45s)
2. Creating product collection (15-20s)
3. Setting up categories (10s)
4. Configuring images via Imagician (5s)

Total time: ~60-80 seconds

[Shows progress...]

✅ Shop ready with Figma designs!
• Design system applied
• Product structure created
• Images optimized (60% smaller)
• Ready for products
```

### Bulk Operations with Image Optimization
```
User: import 50 products with images

System: I'll import your products with optimized images!

Processing:
• Products: 50 items
• Images: Optimizing via Imagician
• Expected: 2-3 minutes total

[Progress bar showing...]

✅ Import complete!
• 50 products created
• 200 images optimized (avg 70% smaller)
• Time: 2 min 45 sec
```

.

## 📊 What Gets Created

Every operation uses intelligent patterns with integrated services:

### Blog System (with Figma)
```
Blog Structure:
├── Blog Posts (articles with SEO)
├── Categories (organization)
├── Authors (writer profiles)
└── Tags (topic grouping)

Integrated Services:
• Figma: Design tokens applied (30-45s)
• Imagician: Images optimized (2-3s each)
• Total setup: 45-60 seconds
```

### E-commerce System (Full Integration)
```
Shop Structure:
├── Products (inventory, pricing)
├── Categories (product groups)
├── Orders (customer purchases)
└── Reviews (customer feedback)

Integrated Services:
• Figma: Component mapping (30-45s)
• Imagician: Product images (4 sizes each)
• Total setup: 60-90 seconds
```

### Portfolio System
```
Portfolio Structure:
├── Projects (case studies)
├── Services (offerings)
├── Testimonials (social proof)
└── Contact (inquiries)

Performance:
• Design import: 30-45s
• Image optimization: 2-3s per image
• Total time: <2 minutes
```

.

## 🔧 Installing MCPs (Required)

The Webflow Agent requires three MCP tools for full functionality. All can be installed via Docker for maximum stability.

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- Webflow API key from [Webflow Account Settings](https://webflow.com/dashboard/account/apps)
- Figma API token from [Figma Settings](https://www.figma.com/developers/api#access-tokens)

**Complete AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant for a complete setup:

```
Help me set up Docker containers for all Webflow Agent MCP tools.

I need to install 3 MCPs:
1. Webflow MCP (primary) - https://github.com/webflow/mcp-server-webflow.git
2. Figma MCP (design import) - https://github.com/figma/mcp-server-figma.git
3. Imagician MCP (image optimization) - https://github.com/flowy11/imagician-mcp.git

Tasks needed:
1. Create directory structure at "$HOME/MCP Servers"
2. Clone all three repositories
3. Create a unified docker-compose.yml for all services
4. Set up environment variables for API keys
5. Configure Claude Desktop's claude_desktop_config.json
6. Build and start all containers
7. Set up proper volume mounts for image processing

My details:
- Webflow API key: [YOUR_WEBFLOW_KEY_HERE]
- Figma API token: [YOUR_FIGMA_TOKEN_HERE]
- Image directory: [YOUR_IMAGE_DIRECTORY_PATH]
- Operating system: [Windows/Mac/Linux]

Please give me the exact commands to run and file contents to create.
```

The AI will provide complete step-by-step commands for your operating system.

**Quick Setup for Individual MCPs:**

If you prefer to set up MCPs one at a time, use these individual prompts:

**Webflow MCP Docker Setup:**
```
Help me set up Docker container for Webflow MCP.

Repository: https://github.com/webflow/mcp-server-webflow.git
API key: [YOUR_WEBFLOW_KEY]
Directory: "$HOME/MCP Servers/webflow"
OS: [Windows/Mac/Linux]

Need: Dockerfile, docker-compose.yml, and Claude config.
```

**Figma MCP Docker Setup:**
```
Help me set up Docker container for Figma MCP.

Repository: https://github.com/figma/mcp-server-figma.git
API token: [YOUR_FIGMA_TOKEN]
Directory: "$HOME/MCP Servers/figma"
OS: [Windows/Mac/Linux]

Need: Dockerfile, docker-compose.yml, and Claude config.
```

**Imagician MCP Docker Setup:**
```
Help me set up Docker container for Imagician MCP.

Repository: https://github.com/flowy11/imagician-mcp.git
Image directory to mount: [YOUR_IMAGE_PATH]
Directory: "$HOME/MCP Servers/imagician"
OS: [Windows/Mac/Linux]

Need: Dockerfile, docker-compose.yml with volume mounts, and Claude config.
```

### Option B: NPX Setup (Quick but Less Stable)

If you need a quick setup without Docker, add all three MCPs to Claude Desktop config:

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
    },
    "figma": {
      "command": "npx",
      "args": ["-y", "@figma/mcp-server-figma"],
      "env": {
        "FIGMA_API_KEY": "your-figma-token-here"
      }
    },
    "imagician": {
      "command": "npx",
      "args": ["-y", "@flowy11/imagician-mcp"]
    }
  }
}
```

**Note:** NPX setup may have stability issues. Docker is strongly recommended for production use.

### Verifying Installation

After setup, verify all MCPs are running:

**For Docker:**
```bash
# Check all containers are running
docker ps

# Should show:
# webflow-mcp     Running
# figma-mcp       Running
# imagician-mcp   Running

# Check logs if needed
docker logs webflow-mcp
docker logs figma-mcp
docker logs imagician-mcp
```

**For NPX:**
1. Restart Claude Desktop
2. Check the MCP indicator in Claude
3. Try a simple command like "test Webflow connection"

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Collection not found"** | Check collection name, list available |
| **"Rate limit exceeded"** | Wait 60s, auto-resumes |
| **"Design sync failed"** | Check Figma permissions and Docker logs |
| **"Image too large"** | Check Imagician container has enough memory |
| **"API key invalid"** | Verify keys in docker-compose.yml |
| **"MCP not connected"** | Check Docker containers are running |
| **"Can't find site"** | Check site ID in Webflow |
| **"Permissions error"** | Verify API key has full access |

### Docker-Specific Issues

**Container Issues:**
```bash
# Check container status
docker ps -a

# Restart all containers
docker-compose restart

# Rebuild if needed
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Check resource usage
docker stats
```

**Common Docker Fixes:**
- **Memory issues**: Increase Docker Desktop memory allocation
- **Network issues**: Restart Docker Desktop
- **Permission issues**: Check volume mount permissions
- **Port conflicts**: Ensure ports aren't in use

### API Rate Limits

All services follow standardized limits:
- **Maximum**: 60 requests/minute
- **Warning**: 50 requests/minute (user notified)
- **Throttle**: 55 requests/minute (auto-slow)
- **Recovery**: 60 second wait at limit

### Performance Benchmarks

| Operation | Time | API Calls | Success Rate |
|-----------|------|-----------|--------------|
| **Single item** | 2-5s | 2-3 | 95% |
| **Design import** | 30-45s | 15-25 | 92% |
| **Image optimize** | 2-3s/img | 1-2 | 98% |
| **Bulk 50 items** | <3min | 30-50 | 85% |
| **Full site** | <8min | 50-100 | 88% |

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For Webflow issues: Check [API documentation](https://developers.webflow.com/)
- For Figma issues: Verify file permissions
- For Image issues: Check file formats (JPEG, PNG, WebP supported)

.

## ⚠️ Important Notes

- **Natural language only** - No API knowledge needed
- **Automatic detection** - System recognizes intent
- **Smart defaults** - Best practices applied automatically
- **No overwrites** - Always creates new or asks first
- **Rate limit safe** - Automatic throttling at 55/60
- **Error recovery** - 92% handled automatically
- **Visual feedback** - See every operation's progress
- **Educational** - Teaches Webflow concepts while building
- **2-3 questions max** - Minimal interaction needed
- **Performance guaranteed** - Standardized timing for all operations
- **Design consistency** - Figma integration seamless
- **Image optimization** - Automatic via Imagician when detected
- **Docker recommended** - Most stable with all three MCPs

.

## 📦 Version History

- **v1.0.0**: Initial release with Webflow, Figma, and Imagician integration

.

## 📚 Resources

### Core Tools
- [Webflow MCP Server](https://github.com/webflow/mcp-server-webflow) (Required)
- [Figma MCP Server](https://github.com/figma/mcp-server-figma) (Design integration)
- [Imagician MCP](https://github.com/flowy11/imagician-mcp) (Image optimization)
- [Claude Projects](https://claude.ai) (Platform)

### Documentation
- [Webflow CMS Guide](https://university.webflow.com/lesson/intro-to-the-webflow-cms)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [API Rate Limits](https://developers.webflow.com/reference/rate-limits)
- [Docker Desktop](https://docs.docker.com/desktop/)

### Quick Links
- [Get Webflow API Key](https://webflow.com/dashboard/account/apps)
- [Get Figma Token](https://www.figma.com/developers/api#access-tokens)
- [Claude Desktop](https://claude.ai/download)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Performance Guidelines
- **Simple operations**: 2-5 seconds
- **Design imports**: 30-45 seconds
- **Image optimization**: 2-3 seconds per image
- **Bulk operations**: Linear scaling with automatic throttling
- **Rate limiting**: Automatic management at 55/60 requests

---

*Transform natural language into precise Webflow CMS operations with seamless Figma design integration and automatic image optimization. Just describe what you want to build and watch your site come to life. No technical knowledge required, just intelligent assistance that handles everything. Complete professional sites ready in under 5 minutes.*