# Imagician Agent - User Guide v1.4.0

The Imagician Agent transforms natural language into professional image operations, making image editing 10x easier. Through intelligent conversation with customizable thinking depth, it understands WHAT you want to optimize and automatically handles HOW to process it. No modes, no commands, just describe what you need and choose how thorough the optimization should be.

## 📑 Table of Contents

- [🆕 What's New in v1.4.0](#-whats-new-in-v140)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 Native Claude Thinking](#-native-claude-thinking)
- [💬 Example Interactions](#-example-interactions)
- [📊 What Gets Optimized](#-what-gets-optimized)
- [📦 Installing Imagician MCP](#-installing-imagician-mcp)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## 🆕 What's New in v1.4.0

### Major Enhancement: Native Claude Thinking
- **Native Thinking Integration**: Removed dependency on Sequential/Cascade MCPs
- **User-Controlled Depth**: You choose thinking rounds (2-3, 4-6, or 7+)
- **Always Asks**: System asks about thinking preference before execution
- **Smart Discovery**: Skips thinking question during information gathering
- **Transparent Process**: Shows thinking approach in results

### Maintained Excellence
- All v1.3.0 image processing capabilities preserved
- Same conversational intelligence
- Professional optimization patterns
- Educational approach retained
- Visual feedback for every operation

.

## ✨ Key Features

- **Natural Language Only**: Just describe what you want to do with your images
- **Native Claude Thinking**: Customizable optimization depth (quick/standard/thorough)
- **Interactive Intelligence**: Adaptive conversation for perfect optimization
- **User Control**: You decide how thorough the AI should be
- **Automatic Detection**: Recognizes web vs email vs social media needs
- **Smart Guidance**: Asks only essential questions (2-3 max + thinking preference)
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
4. Name it "Imagician Agent v1.4"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - Imagician MCP - v1.4.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 3 streamlined documents to your project:
- `Imagician - Interactive Intelligence - v1.5.0.md` (Conversation examples with thinking)
- `Imagician - Patterns & Workflows - v1.4.0.md` (Patterns with thinking depth)
- `Imagician - Image Intelligence - v1.3.0.md` (Best practices and optimization)

### Step 4: Install Imagician MCP
Follow the installation guide in the Installing Imagician MCP section below.

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

The system will ask about your preferred thinking depth before executing!

.

## 🧠 Native Claude Thinking

### How It Works

The system uses native Claude thinking capabilities to plan optimizations. Before executing any operation, it asks:

**"How many rounds of thinking should I use?"**
- **Quick (2-3 rounds)**: Fast processing for simple operations
- **Standard (4-6 rounds)**: Balanced optimization for most tasks
- **Thorough (7+ rounds)**: Best results for complex workflows

### When Thinking Happens

**System ASKS about thinking when:**
- Ready to execute an operation
- All information gathered
- About to create output
- Moving from planning to action

**System SKIPS thinking question when:**
- Still gathering information (file location, format preference)
- In discovery phase (understanding what you want)
- Won't produce output after next response
- Still clarifying requirements

### Thinking Depth Examples

| Task | Recommended | Why |
|------|-------------|-----|
| Simple resize | Quick (2-3) | Straightforward operation |
| Format conversion | Quick (2-3) | Direct conversion |
| Web optimization | Standard (4-6) | Multiple factors to balance |
| Email preparation | Standard (4-6) | Size/quality trade-offs |
| Social media set | Thorough (7+) | Platform-specific needs |
| Batch processing | Standard/Thorough | Consistency vs optimization |
| Responsive images | Thorough (7+) | Multiple size calculations |

.

## 💬 Example Interactions

### Simple Operation with Thinking
```
User: resize my photo to 800px

System: I'll resize your photo to 800px width!

How many rounds of thinking should I use?
• Quick (2-3): Simple resize
• Standard (4-6): With optimization
• Thorough (7+): Maximum quality

User: Quick

System: [Using 3 rounds of thinking]

Processing...
✅ Complete!
Original: 3840x2160 (4.2MB)
Result: 800x450 (245KB)

Maintained aspect ratio perfectly!
```

### Discovery Phase (No Thinking Yet)
```
User: help with vacation photos

System: I'll help with your vacation photos!

What would you like to do?
• Optimize for sharing online
• Create photo album
• Reduce file sizes
• Make prints
• Convert formats

User: Share them online

System: Perfect! Where are your photos located?

User: ~/Desktop/Vacation2024/

System: Found your vacation photos!

How thorough should my optimization be?
• Quick (2-3): Basic web prep
• Standard (4-6): Good optimization
• Thorough (7+): Best per-photo results

[Only NOW asking about thinking]
```

### Complex Workflow
```
User: create Instagram and Facebook versions

System: I'll create optimized versions for both platforms!

How many rounds of thinking for this multi-platform optimization?
• Quick (2-3): Basic sizing
• Standard (4-6): Platform optimization
• Thorough (7+): Maximum quality per platform

User: Thorough please

System: [Using 8 rounds of thinking to optimize for each platform]

Creating platform versions:
• Instagram: 1080x1080 at 90% quality
• Facebook: 1200x630 at 85% quality

✅ Both versions created successfully!
```

### Power User Fast Track
```
User: batch convert all PNGs to WebP 85%

System: I'll batch convert your PNGs to WebP at 85% quality!

How many thinking rounds?
• Quick (2-3): Same settings for all
• Standard (4-6): Smart batching
• Thorough (7+): Optimize each file

User: Quick

System: [Using 2 rounds of thinking]

Converting 15 PNG files...
✅ Complete! Reduced total size by 68%
```

.

## 📊 What Gets Optimized

Every optimization uses intelligent patterns with your chosen thinking depth:

### Web Optimization (Standard Thinking)
```
Web-Ready Images:
├── Resized to max 1920px
├── Converted to WebP format
├── Quality 85% (sweet spot)
├── Progressive encoding
└── Metadata stripped
Result: 60-70% smaller, loads 3x faster
```

### Email Preparation (Standard Thinking)
```
Email-Ready:
├── Max 1024px width
├── JPEG format (universal)
├── Under 5MB total
├── Quality 80-85%
└── Compatible everywhere
Result: Attachable to any email
```

### Social Media (Thorough Thinking)
```
Platform Optimized:
├── Instagram: 1080x1080 square
├── Facebook: 1200x630 link preview
├── Twitter/X: 1200x675 card
├── LinkedIn: 1200x627 share
└── All at optimal quality
Result: Perfect for each platform
```

### Responsive Sets (Thorough Thinking)
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

## 📦 Installing Imagician MCP

### Option A: Docker Setup (Recommended)

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

### Option B: NPX Setup (Quick)

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

**Note:** Only the Imagician MCP is required. Native Claude thinking replaces the need for thinking MCPs!

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Can't find image"** | Provide full path like ~/Desktop/photo.jpg |
| **"Format not supported"** | Check if JPEG, PNG, WebP, or AVIF |
| **"Permission denied"** | Check file permissions or try different location |
| **"Quality looks bad"** | Choose "Thorough" thinking for better optimization |
| **"File still too large"** | Try "Thorough" thinking with aggressive compression |
| **"MCP not connected"** | Restart Claude Desktop |

### Thinking-Related Issues

**"Why didn't it ask about thinking?"**
- Still in discovery phase
- Gathering information (path, format, etc.)
- Won't produce output yet

**"Can I change thinking depth?"**
- Yes! Just specify: "Use thorough thinking" or "Quick processing please"

**"What if I'm unsure about thinking depth?"**
- Default to Standard (4-6) for most tasks
- The system will suggest based on complexity

### Quick Fixes

**Path Issues:**
- Use full paths starting with ~ or /
- Escape spaces: `~/My Photos/pic.jpg`
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

.

## ⚠️ Important Notes

- **Native thinking integrated** - Uses Claude's built-in capabilities
- **Always asks thinking preference** - Before execution, not during discovery
- **No additional MCPs needed** - Just Imagician MCP required
- **Smart discovery** - Gathers info first, then asks about thinking
- **Conversation adapts** - From quick execution to full guidance
- **Best practices automatic** - Professional patterns applied
- **Original preserved** - Never overwrites without permission
- **Educational by design** - Teaches while optimizing
- **Visual feedback always** - See the optimization impact
- **User in control** - You choose optimization depth

.

## 📦 Version History

- **v1.4.0**: Native Claude thinking, user-controlled depth, removed MCP dependencies
- **v1.3.0**: Unified interactive intelligence, removed mode system
- **v1.2.0**: Mandatory path asking, enhanced safety
- **v1.1.0**: Added MCP thinking tools
- **v1.0.0**: Initial release

.

## 📚 Resources

### Core Tool
- [Imagician MCP](https://github.com/flowy11/imagician) (Required)

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

*Transform natural language into optimized images through intelligent conversation with customizable thinking depth. The system uses native Claude thinking to understand what you need and applies professional optimization automatically. You control how thorough the optimization should be. Every image processed with the perfect balance of quality and file size.*
