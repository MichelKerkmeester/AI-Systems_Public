# Imagician Agent - User Guide v1.3.0

The Imagician Agent transforms natural language into professional image operations, making image editing 10x easier. Through intelligent conversation, it understands WHAT you want to optimize and automatically handles HOW to process it. No modes, no commands, just describe what you need.

## 📑 Table of Contents

- [🆕 What's New in v1.3.0](#-whats-new-in-v130)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 Intelligent Conversation System](#-intelligent-conversation-system)
- [💬 Example Interactions](#-example-interactions)
- [📊 What Gets Optimized](#-what-gets-optimized)
- [🔧 Installing MCPs (Required & Optional)](#-installing-mcps-required--optional)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## 🆕 What's New in v1.3.0

### Major Simplification
- **Single Unified Approach**: Removed all mode commands ($interactive, $quick, etc.)
- **Interactive Intelligence**: One smart system handles everything through conversation
- **Smarter Path Handling**: Asks for paths conversationally when needed, not mandatorily
- **Confidence-Based Response**: Dynamic interaction from immediate execution to full guidance
- **Cleaner Documentation**: Reduced to 3 essential reference documents
- **Automatic Intent Detection**: System recognizes what you need and adapts

### Maintained Excellence
- All v1.2.0 image processing capabilities preserved
- Enhanced MCP intelligence (Sequential and Cascade Thinking)
- Same professional optimization patterns
- Educational approach retained
- Visual feedback for every operation

.

## ✨ Key Features

- **Natural Language Only**: Just describe what you want to do with your images
- **Interactive Intelligence**: Adaptive conversation for perfect optimization
- **Automatic Detection**: Recognizes web vs email vs social media needs
- **Triple MCP Support**: Imagician MCP (core), Sequential Thinking (simple), Cascade Thinking (complex)
- **Smart Guidance**: Asks only essential questions (2-3 max)
- **Best Practices Built-in**: Professional optimization patterns applied automatically
- **Visual Feedback**: Clear before/after metrics and success confirmations
- **Educational Focus**: Teaches image optimization concepts while working
- **5-Minute Setup**: Complete optimization workflows ready in minutes
- **Zero Technical Knowledge**: No understanding of formats or compression required

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Imagician Agent v1.3"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - Imagician MCP - v1.3.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 3 streamlined documents to your project:
- `Imagician - Interactive Intelligence - v1.4.0.md` (Conversation examples and patterns)
- `Imagician - Patterns & Workflows - v1.3.0.md` (All patterns and operation mappings)
- `Imagician - Image Intelligence - v1.3.0.md` (Best practices and optimization strategies)

### Step 4: Install Imagician MCP
Follow the installation guide in the Installing MCPs section below to set up the Imagician MCP server.

### Step 5: Start Optimizing
Simply describe what you need:
```
optimize for web
make this smaller
convert to modern format
prepare for email
create thumbnails
resize for Instagram
compress these photos
```

No modes or commands needed! The system automatically understands your intent.

.

## 🧠 Intelligent Conversation System

### Confidence-Based Response

The system automatically adjusts conversation depth based on request clarity:

| Confidence | Range | Response Strategy | Example |
|------------|-------|------------------|---------|
| **Exact** | >0.95 | Immediate execution | "resize to 800px" → Resizes immediately |
| **High** | 0.80-0.95 | Single clarification | "make smaller" → "Target size or percentage?" |
| **Medium** | 0.50-0.79 | Guided exploration | "optimize this" → "For web, email, or storage?" |
| **Low** | <0.50 | Full guidance | "help" → Complete capability overview |

### Intelligent MCP Selection

When thinking MCPs are available:

| Tool | When Used | Thought Count | Purpose |
|------|-----------|---------------|---------|
| **Sequential Thinking** | Simple operations | 2-3 thoughts | Single resize, convert |
| **Cascade Thinking** | Complex workflows | 5-7 thoughts | Responsive sets, batch |
| **Imagician MCP** | Always | N/A | Actual image operations |

The system automatically selects the appropriate tool based on:
- Request complexity
- Number of images involved
- Optimization decisions needed
- Quality trade-offs required
- User confidence level

.

## 💬 Example Interactions

### Simple Optimization
```
User: optimize my photo

System: I'll optimize your photo! 

What's your primary use:
• Web display (fast loading)
• Email attachment (under 5MB)
• Social media (platform-specific)
• General storage (balanced)

[Optimizes based on choice with smart defaults]
```

### Specific Operation
```
User: resize to 1200px wide

System: Resizing to 1200px width now!

Processing...
✅ Complete!
Original: 3840x2160 (4.2MB)
Result: 1200x675 (387KB)

Maintained aspect ratio and optimized quality.
```

### Complex Workflow
```
User: prepare images for my website

System: I'll optimize your images for web! 

Creating web-ready versions:
• Maximum 1920px width
• Converting to WebP (30% smaller)
• Quality 85% (perfect balance)
• Progressive loading enabled

[Processes all images with web optimization]
```

### Uncertain Request
```
User: help with these photos

System: I'm here to help with your photos!

What would you like to do:
• Resize or crop them
• Optimize for web/email
• Convert to different format
• Reduce file size
• Create multiple versions

Just describe what you need!
```

.

## 📊 What Gets Optimized

Every optimization uses intelligent patterns:

### Web Optimization
```
Web-Ready Images:
├── Resized to max 1920px
├── Converted to WebP format
├── Quality 85% (sweet spot)
├── Progressive encoding
└── Metadata stripped
Result: 60-70% smaller, loads 3x faster
```

### Email Preparation
```
Email-Ready:
├── Max 1024px width
├── JPEG format (universal)
├── Under 5MB total
├── Quality 80-85%
└── Compatible everywhere
Result: Attachable to any email
```

### Social Media
```
Platform Optimized:
├── Instagram: 1080x1080 square
├── Facebook: 1200x630 link preview
├── Twitter/X: 1200x675 card
├── LinkedIn: 1200x627 share
└── All at 90% quality
Result: Perfect for each platform
```

### Responsive Sets
```
Multiple Sizes:
├── 320px (mobile)
├── 640px (tablet)
├── 1024px (desktop)
├── 1920px (full)
└── 150px (thumbnail)
Result: Complete responsive image set
```

.

## 🔧 Installing MCPs (Required & Optional)

### Required: Imagician MCP

#### Option A: Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**Installation Steps:**
```bash
# 1. Create directory
mkdir -p "$HOME/MCP Servers"
cd "$HOME/MCP Servers"

# 2. Clone repository
git clone https://github.com/flowy11/imagician.git
cd imagician

# 3. Build Docker image
docker build -t imagician-mcp .

# 4. Run container
docker run -d \
  --name imagician-mcp \
  -v ~/Pictures:/images \
  imagician-mcp
```

#### Option B: NPX Setup (Quick but Less Stable)

Add to Claude Desktop config:

**Config Location:**
- Mac/Linux: `~/.config/claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "imagician": {
      "command": "npx",
      "args": ["-y", "@flowy11/imagician-mcp"]
    }
  }
}
```

### Optional: Thinking MCPs (Enhanced Intelligence)

For even better optimization decisions, add thinking tools:

```json
{
  "mcpServers": {
    "imagician": {
      "command": "npx",
      "args": ["-y", "@flowy11/imagician-mcp"]
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
- **Cascade Thinking**: Smarter workflow planning
- **Automatic selection**: Agent chooses the right tool
- **Better optimization**: Explores all options

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Can't find image"** | Provide full path like ~/Desktop/photo.jpg |
| **"Format not supported"** | Check if JPEG, PNG, WebP, or AVIF |
| **"Permission denied"** | Check file permissions or try different location |
| **"Quality looks bad"** | Increase quality percentage or use less compression |
| **"File still too large"** | Try more aggressive optimization or resize |
| **"MCP not connected"** | Restart Claude Desktop |

### Quick Fixes

**Path Issues:**
- Use full paths starting with ~ or /
- Escape spaces: `~/My Photos/pic.jpg` or `~/My\ Photos/pic.jpg`
- Common locations: ~/Desktop/, ~/Downloads/, ~/Pictures/

**Docker Issues:**
```bash
# Check if running
docker ps
# View logs
docker logs imagician-mcp
# Restart
docker restart imagician-mcp
```

**NPX Issues:**
- Ensure Node.js installed
- Check config file syntax
- Restart Claude Desktop

### Getting Help
- For image issues: The agent provides educational explanations
- For MCP issues: Check container/process logs
- For path issues: Agent guides you to correct format

.

## ⚠️ Important Notes

- **No commands needed** - Just describe what you want
- **Conversation adapts** - From quick execution to full guidance
- **Smart path handling** - Asks when needed, not always
- **Best practices automatic** - Professional patterns applied
- **Original preserved** - Never overwrites without permission
- **Works without thinking MCPs** - But enhanced with them
- **Educational by design** - Teaches while optimizing
- **2-3 questions max** - Respects your time
- **Visual feedback always** - See the optimization impact
- **5-minute setup** - Ready to optimize quickly

.

## 📦 Version History

- **v1.3.0**: Unified interactive intelligence, removed mode system, smarter path handling
- **v1.2.0**: Mandatory path asking, enhanced safety
- **v1.1.0**: Added MCP thinking tools
- **v1.0.0**: Initial release

.

## 📚 Resources

### Core Tools
- [Imagician MCP](https://github.com/flowy11/imagician) (Required)
- [Sequential Thinking MCP](https://github.com/modelcontextprotocol/server-sequential-thinking) (Optional)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp) (Optional)

### Documentation
- [WebP Information](https://developers.google.com/speed/webp)
- [Image Optimization Guide](https://web.dev/fast/#optimize-your-images)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Docker Desktop](https://docs.docker.com/desktop/)

### Image Tools
- [ImageMagick](https://imagemagick.org/) - Command line processing
- [Sharp](https://sharp.pixelplumbing.com/) - Node.js library
- [Squoosh](https://squoosh.app/) - Browser-based optimizer

.

*Transform natural language into optimized images through intelligent conversation. The system understands what you need and applies professional optimization automatically. Every image processed with the perfect balance of quality and file size.*