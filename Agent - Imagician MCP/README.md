# Imagician Agent - User Guide v1.1.0

## 🆕 What's New in v1.1.0

- **Enhanced Intelligence**: Added Sequential and Cascade Thinking MCP support
- **Smarter Decisions**: Automatic selection between simple (Sequential) and complex (Cascade) thinking
- **Improved Workflows**: Complex operations now use Cascade Thinking for better optimization
- **Faster Simple Tasks**: Quick mode uses Sequential Thinking for immediate results
- **Intelligent Exploration**: Interactive mode uses Cascade to explore best approaches
- **Maintained Simplicity**: All v1.0.0 features preserved with added intelligence

## 🚀 What is This?

The Imagician Agent transforms natural language into professional image operations, making image editing 10x easier. Instead of learning complex photo editing software, just describe what you want in plain English. **Now with enhanced intelligence through MCP thinking tools!**

**Key Benefits:**
- Transform conversations into optimized images
- No need to understand formats, dimensions, or compression
- Get intelligent optimization with best practices built-in
- Interactive mode guides you through editing decisions (DEFAULT)
- Educational system teaches image optimization while you work
- Automatic format selection and quality optimization
- Professional results for web, email, and social media
- **NEW: Enhanced decision-making with Sequential and Cascade Thinking**

**Key Principle:** If you can describe it, the agent can edit it intelligently.

---

## 🧠 Intelligent MCP System (NEW)

### How It Works
The v1.1.0 update adds two thinking tools that make the agent smarter:

**Sequential Thinking (2-3 thoughts):**
- Used for simple, single operations
- Fast execution for clear requests
- Direct path from request to result
- Example: "Resize to 800px" → Immediate execution

**Cascade Thinking (5-7 thoughts):**
- Used for complex workflows and exploration
- Evaluates multiple options and trade-offs
- Plans multi-step operations intelligently
- Example: "Optimize for my website" → Explores format options, sizes, quality balance

### Automatic Selection
The agent automatically chooses the right thinking tool:

| Your Request | MCP Selected | Why |
|--------------|--------------|-----|
| "Resize to 800px" | Sequential | Single clear operation |
| "Make it smaller" | Cascade | Needs to explore resize vs compress |
| "For my website" | Cascade | Multiple optimization decisions |
| "Convert to JPEG" | Sequential | Direct format conversion |
| "All social media" | Cascade | Complex multi-platform workflow |

---

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Imagician Agent v1.1"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Agent - Imagician MCP - v1.1.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Upload all reference documents to your project:
- `Imagician - Interactive Mode - v1.1.0.md` (conversational guidance with MCP)
- `Imagician - Patterns & Workflows - v1.1.0.md` (operation mappings with MCP logic)
- `Imagician - Platform Specs & Defaults - v1.1.0.md` (platform specifications with MCP notes)

### Step 4: Start Using Natural Language!
Begin any conversation in the project, and Claude will guide you through image editing conversationally with enhanced intelligence.

---

## 🎨 Core Capabilities

### What the Agent Can Do
The Imagician Agent provides 8 powerful image operations through natural language:

1. **Resize** - Change dimensions intelligently
2. **Convert** - Transform between JPEG, PNG, WebP, AVIF
3. **Compress** - Reduce file size while maintaining quality
4. **Crop** - Extract specific regions or aspect ratios
5. **Rotate** - Rotate by any angle
6. **Flip** - Mirror horizontally or vertically
7. **Get Info** - Extract metadata and specifications
8. **Batch Process** - Apply operations to multiple images

### Smart Understanding with MCP
- "Make it smaller" → **Cascade explores** resize vs compress options
- "For my website" → **Cascade plans** complete optimization workflow
- "Instagram ready" → **Sequential applies** 1080x1080 directly
- "Email this" → **Sequential reduces** to under 5MB
- "Create thumbnails" → **Cascade generates** multiple sizes efficiently

---

## 🎯 How to Use

### Basic Usage (Interactive Mode - DEFAULT)
Simply describe what you need:
```
I need to optimize this photo
```

The system will:
1. **Activate Cascade Thinking** for exploration
2. Ask clarifying questions (web, email, social?)
3. Apply smart defaults based on analysis
4. Show visual before/after comparison
5. Explain why certain choices were made
6. Suggest next steps based on workflow

### Example Conversations with MCP

**Simple Request (Sequential):**
```
User: Make this image smaller
System: [Cascade Thinking explores options]
I'll help make that smaller! Let me analyze the best approach...

Are you looking to:
1. Reduce file size (for faster loading)
2. Change dimensions (resize)
3. Both

What matters most for your use?
```

**Platform Specific (Sequential):**
```
User: Prepare for Instagram
System: [Sequential Thinking - direct application]
Perfect! I'll optimize for Instagram.

Creating:
• Feed post (1080x1080 square)
• Quality: 90% JPEG
• Optimized for mobile viewing

Ready to proceed?
```

**Complex Workflow (Cascade):**
```
User: Optimize for my website
System: [Cascade Thinking - exploring options]
I'll optimize for web use! Let me analyze the best approach...

🧠 Planning optimization strategy...
• Evaluating format options (WebP vs JPEG)
• Calculating optimal dimensions
• Balancing quality vs file size

Ready to create a fast-loading web image?
```

### Mode Selection with MCP Integration
| Mode | Command | Use For | MCP Strategy | Example |
|------|---------|---------|--------------|---------|
| **Interactive** | `$interactive` or `$int` | DEFAULT - Guided editing | Cascade (5-7) | "edit photo" → exploration |
| **Quick** | `$quick` or `$q` | Fast single operations | Sequential (2-3) | "$q resize 800px" → instant |
| **Batch** | `$batch` or `$b` | Multiple images | Cascade (5-7) | "$b compress all" → workflow |
| **Platform** | `$platform` or `$p` | Social media | Varies (3-5) | "$p instagram" → direct |
| **Web** | `$web` or `$w` | Website optimization | Cascade (5-7) | "$w optimize" → complete |

---

## ✅ Output Format with MCP

### Visual Feedback for Every Operation
```
📸 Processing: vacation.jpg
🧠 Using: Cascade Thinking (optimal workflow)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before: 3840x2160 (4.2MB) JPEG
After:  1920x1080 (1.1MB) WebP

✅ Reduced by 74%!
💡 WebP loads 30% faster than JPEG on websites

🧠 Cascade evaluated 5 optimization strategies

Suggestions:
• Create thumbnail version
• Generate responsive set
• Apply to other images
```

### Platform Optimization with Intelligence
- **Instagram**: Sequential applies 1080x1080, 90% JPEG
- **Multiple platforms**: Cascade plans optimal workflow
- **Web responsive**: Cascade creates complete set
- **Email**: Sequential optimizes to <5MB

### Educational Integration with MCP
Every operation teaches you optimization:
```
💡 "I chose WebP format because Cascade analysis showed 
it's 30% smaller than JPEG with the same visual quality. 
All modern browsers support it!"

🧠 "The intelligent workflow compared 6 different approaches
and selected the best balance of quality and performance."
```

---

## 🔧 Installing Required MCPs

### Core MCP: Imagician (Required)

The Imagician MCP provides the core image editing capabilities.

#### Option A: Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))

**Quick Setup:**
1. Create directory and clone:
```bash
mkdir -p "$HOME/MCP Servers" && cd "$HOME/MCP Servers"
git clone https://github.com/flowy11/imagician.git
cd imagician
```

2. Create docker-compose.yml:
```yaml
version: '3.8'
services:
  imagician:
    build: .
    restart: unless-stopped
```

3. Start container:
```bash
docker-compose up -d
```

#### Option B: NPX Installation

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "imagician": {
      "command": "npx",
      "args": ["-y", "@flowy11/imagician"]
    }
  }
}
```

### Intelligence MCPs: Thinking Tools (Recommended)

For enhanced intelligence, add Sequential and Cascade Thinking tools:

#### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the Imagician MCP tools with enhanced intelligence.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/flowy11/imagician.git (main tool)
   - https://github.com/modelcontextprotocol/server-sequential-thinking.git
   - https://github.com/cascadethinking/cascade-thinking-mcp.git
3. Create Dockerfiles for each service if needed
4. Create a docker-compose.yml file with all three services
5. Configure Claude Desktop's claude_desktop_config.json
6. Build and start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for 3 running containers (imagician-mcp, sequential-thinking-mcp, cascade-thinking-mcp)
2. Look for the 🔌 icon in Claude Desktop showing all 3 tools
3. Test with: "optimize my image intelligently"

#### Option B: NPX Setup (Quick but Less Stable)

Add these to Claude Desktop config:

```json
{
  "mcpServers": {
    "imagician": {
      "command": "npx",
      "args": ["-y", "@flowy11/imagician"]
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

**Benefits of Thinking MCPs:**
- **Sequential Thinking**: 2x faster simple operations
- **Cascade Thinking**: Smarter complex workflows
- **Automatic selection**: Agent chooses the right tool
- **Better optimization**: Explores all options
- **Intelligent decisions**: Evaluates trade-offs

**Verification:**
1. Restart Claude Desktop
2. Look for 🔌 icon showing all 3 tools
3. Test with: "optimize my image intelligently"

---

## 🆘 Troubleshooting

### "I don't know what to do with my image"
- Just describe your goal in plain language
- Interactive mode (with Cascade Thinking) will guide you
- Try: "Help me optimize this" or "Make it better for web"

### "System seems slower with v1.1.0"
- Complex operations use Cascade Thinking for better results
- Simple operations still use Sequential for speed
- Use Quick mode ($q) for fastest execution
- Benefits: Better optimization, smarter decisions

### MCP Not Available Messages
```
💡 Intelligence Enhancement Available

The system is operating without thinking tools.
For enhanced optimization, consider adding:
• Sequential Thinking MCP (fast operations)
• Cascade Thinking MCP (complex workflows)
```
- System still works without thinking MCPs
- Adding them enables smarter optimization
- Follow installation instructions above

### Common Issues
- **File not found**: Check spelling and location
- **Quality concerns**: System warns before degradation
- **Large files**: Cascade finds optimal compression
- **Multiple platforms**: Cascade plans efficiently

### MCP-Specific Issues
- **Tools not showing**: Restart Claude Desktop
- **Thinking seems wrong**: Agent auto-selects appropriately
- **Want different MCP**: Specify mode explicitly
- **No MCP available**: System uses structured fallback

---

## ⚠️ Important Notes

- **Interactive mode is DEFAULT** - Now with Cascade Thinking
- **Original files preserved** - Never overwrites without permission
- **Smart quality selection** - Enhanced by MCP analysis
- **Platform awareness** - Knows all social media specifications
- **Educational approach** - Teaches optimization concepts as you work
- **MCP intelligence** - Automatic selection of thinking strategy

## 📦 Version History

- **v1.1.0**: Added Sequential and Cascade Thinking MCP support
- **v1.0.0**: Initial release with 5 operational modes

---

## 🎯 Key Principles

1. **Natural language first** - Describe what you want, not how
2. **Intelligent processing** - MCP tools enhance decision-making
3. **Learn while editing** - Every operation teaches optimization
4. **Best practices built-in** - Professional settings automatically applied
5. **Quality preservation** - Warns before degrading quality
6. **Progressive disclosure** - Starts simple, reveals advanced features

---

## 📚 Quick Reference

### Common Operations with MCP
| What You Say | MCP Used | What Happens | Result |
|--------------|----------|--------------|--------|
| "make it smaller" | Cascade | Explores options | 50-75% size reduction |
| "resize to 800px" | Sequential | Direct resize | Exact dimension |
| "for my website" | Cascade | Full optimization | WebP, 85%, responsive |
| "email attachment" | Sequential | Simple reduction | Under 5MB |
| "social media ready" | Cascade/Sequential | Platform optimization | Perfect specs |
| "create thumbnail" | Sequential | Small preview | 150x150px |

### MCP Selection Guide
| Request Type | MCP Choice | Why |
|--------------|------------|-----|
| Clear single operation | Sequential | Direct path |
| Vague request | Cascade | Needs exploration |
| Multiple options | Cascade | Evaluate choices |
| Batch same operation | Sequential | Repeated task |
| Batch with conditions | Cascade | Complex logic |
| Web optimization | Cascade | Multiple decisions |

### Platform Specifications
| Platform | Post | Story/Reel | Profile | Cover/Header | MCP |
|----------|------|------------|---------|--------------|-----|
| Instagram | 1080x1080 | 1080x1920 | 320x320 | - | Sequential |
| Facebook | 1200x630 | 1080x1920 | 400x400 | 820x312 | Sequential |
| Twitter | 1200x675 | - | 400x400 | 1500x500 | Sequential |
| LinkedIn | 1200x627 | - | 400x400 | 1584x396 | Sequential |
| Multiple | Varies | Varies | Varies | Varies | Cascade |

### Quality Guidelines with MCP
- **95-100%**: Archival/print (Sequential - clear need)
- **85-90%**: Web/social (Cascade - balance analysis)
- **75-80%**: Thumbnails (Sequential - standard)
- **60-70%**: High compression (Cascade - optimization)
- **<60%**: Maximum compression (Cascade - trade-offs)

---

## 📚 Resources

### Core Tools
- [Imagician MCP GitHub](https://github.com/flowy11/imagician) (Required)
- [Sequential Thinking MCP](https://github.com/modelcontextprotocol/server-sequential-thinking) (Recommended)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp) (Recommended)

### Documentation
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Claude Desktop](https://claude.ai/download)

### Image Optimization
- [WebP Information](https://developers.google.com/speed/webp)
- [Image Optimization Guide](https://web.dev/fast/#optimize-your-images)
- [Social Media Image Sizes](https://sproutsocial.com/insights/social-media-image-sizes-guide/)

---

*Transform natural language into perfectly optimized images with v1.1.0's enhanced intelligence. Sequential Thinking provides lightning-fast simple operations while Cascade Thinking explores complex optimizations. Just describe what you need, and watch your images transform intelligently while learning optimization best practices.*