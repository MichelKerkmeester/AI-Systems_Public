# Imagician Agent - User Guide v1.0.0

## 🚀 What is This?

The Imagician Agent transforms natural language into professional image operations, making image editing 10x easier. Instead of learning complex photo editing software, just describe what you want in plain English.

**Key Benefits:**
- Transform conversations into optimized images
- No need to understand formats, dimensions, or compression
- Get intelligent optimization with best practices built-in
- Interactive mode guides you through editing decisions (DEFAULT)
- Educational system teaches image optimization while you work
- Automatic format selection and quality optimization
- Professional results for web, email, and social media

**Key Principle:** If you can describe it, the agent can edit it.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Imagician Agent v1.0"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Agent - Imagician MCP - v1.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Upload all reference documents to your project:
- `Imagician - Interactive Mode - v1.0.0.md` (conversational guidance)
- `Imagician - Patterns & Workflows - v1.0.0.md` (operation mappings)
- `Imagician - Platform Specs & Defaults - v1.0.0.md` (platform specifications)

### Step 4: Start Using Natural Language!
Begin any conversation in the project, and Claude will guide you through image editing conversationally.

.

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

### Smart Understanding
- "Make it smaller" → Chooses resize vs compress based on context
- "For my website" → Complete web optimization workflow
- "Instagram ready" → Perfect 1080x1080 with optimal quality
- "Email this" → Reduces to under 5MB automatically
- "Create thumbnails" → Generates multiple sizes efficiently

.

## 🎯 How to Use

### Basic Usage (Interactive Mode - DEFAULT)
Simply describe what you need:
```
I need to optimize this photo
```

The system will:
1. Start Interactive Mode automatically
2. Ask clarifying questions (web, email, social?)
3. Apply smart defaults
4. Show visual before/after comparison
5. Explain why certain choices were made
6. Suggest next steps

### Example Conversations

**Simple Request:**
```
User: Make this image smaller
System: I'll help make that smaller! Are you looking to:
1. Reduce file size (for faster loading)
2. Change dimensions (resize)
3. Both

What matters most for your use?
```

**Platform Specific:**
```
User: Prepare for Instagram
System: Perfect! I'll optimize for Instagram.

Creating:
• Feed post (1080x1080 square)
• Quality: 90% JPEG
• Optimized for mobile viewing

Ready to proceed?
```

### Mode Selection
| Mode | Command | Use For | Example |
|------|---------|---------|---------|
| **Interactive** | `$interactive` or `$int` | DEFAULT - Guided editing | "edit photo" → conversation |
| **Quick** | `$quick` or `$q` | Fast single operations | "$q resize 800px" → instant |
| **Batch** | `$batch` or `$b` | Multiple images | "$b compress all" → bulk |
| **Platform** | `$platform` or `$p` | Social media | "$p instagram" → 1080x1080 |
| **Web** | `$web` or `$w` | Website optimization | "$w optimize" → WebP + responsive |

.

## ✅ Output Format

### Visual Feedback for Every Operation
```
📸 Processing: vacation.jpg
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Before: 3840x2160 (4.2MB) JPEG
After:  1920x1080 (1.1MB) WebP

✅ Reduced by 74%!
💡 WebP loads 30% faster than JPEG on websites

Suggestions:
• Create thumbnail version
• Generate responsive set
• Apply to other images
```

### Platform Optimization
- **Instagram**: 1080x1080 square, 90% JPEG quality
- **Twitter**: 1200x675 landscape, optimized for timeline
- **Facebook**: 1200x630 for posts, 820x312 for covers
- **LinkedIn**: 1200x627 professional quality
- **YouTube**: 1280x720 thumbnails with high impact

### Educational Integration
Every operation teaches you optimization:
```
💡 "I chose WebP format because it's 30% smaller than JPEG 
with the same visual quality. All modern browsers support it!"
```

.

## 🔧 Installing Imagician MCP (Required)

The Imagician MCP provides the core image editing capabilities. Choose either Docker (stable) or NPX (quick) installation:

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- Node.js installed for the image processing

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up a Docker container for the Imagician MCP tool.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone this repo:
   - https://github.com/flowy11/imagician.git
3. Create a Dockerfile for the Imagician service
4. Create a docker-compose.yml file
5. Configure Claude Desktop's claude_desktop_config.json
6. Build and start the container with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for running imagician container
2. Look for the 🔌 icon in Claude Desktop showing Imagician tools
3. Test with: "Resize an image to 800px width"

### Option B: NPX Installation (Quick Setup)

Add to Claude Desktop config file:

**Mac/Linux:** `~/.config/claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

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

Or for global installation:
```bash
npm install -g @flowy11/imagician
```

Then use in config:
```json
{
  "mcpServers": {
    "imagician": {
      "command": "imagician"
    }
  }
}
```

**Verification:**
1. Restart Claude Desktop
2. Check for Imagician in available tools
3. Test with a simple resize operation

.

## 🆘 Troubleshooting

### "I don't know what to do with my image"
- Just describe your goal in plain language
- Interactive mode will guide you step by step
- Try: "Help me optimize this" or "Make it better for web"

### "Can't find image file"
- Check file name spelling (photo.jpg vs photo.jpeg)
- Ensure file is in current directory
- Try using the full path to the file
- System will suggest alternatives

### "Quality looks bad after editing"
- System warns before quality-reducing operations
- Upscaling always reduces quality (warned)
- Choose higher quality settings if needed
- Keep originals for future edits

### "File size still too large"
- Try more aggressive compression (70-80%)
- Reduce dimensions first, then compress
- Convert to WebP or AVIF for better compression
- System suggests optimal approach

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **NPX issues**: Ensure Node.js is installed
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Install Node.js first for NPX method
- **Container won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **Image not processing**: Check file exists and is valid image format

### Format Issues
- **RAW files**: Not supported directly, export to JPEG/PNG first
- **HEIC files**: Convert to JPEG first (iPhone photos)
- **Transparency lost**: JPEG doesn't support transparency, use PNG/WebP
- **WebP compatibility**: 95% browser support, JPEG fallback for older browsers

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For image issues: Verify file format and integrity
- For general issues: The AI assistant can help diagnose problems

.

## ⚠️ Important Notes

- **Interactive mode is DEFAULT** - Unless explicitly specified otherwise
- **Original files preserved** - Never overwrites without permission
- **Smart quality selection** - Balances file size and visual quality
- **Platform awareness** - Knows all social media specifications
- **Educational approach** - Teaches optimization concepts as you work

## 📦 Version History

- **v1.0.0**: Initial release with 5 operational modes and complete platform support

## 🎯 Key Principles

1. **Natural language first** - Describe what you want, not how
2. **Learn while editing** - Every operation teaches optimization
3. **Best practices built-in** - Professional settings automatically applied
4. **Quality preservation** - Warns before degrading quality
5. **Progressive disclosure** - Starts simple, reveals advanced features

.

## 📚 Quick Reference

### Common Operations
| What You Say | What Happens | Result |
|--------------|--------------|--------|
| "make it smaller" | Compress or resize based on context | 50-75% size reduction |
| "for my website" | Full web optimization | WebP, 85%, responsive ready |
| "email attachment" | Resize and compress | Under 5MB, universal format |
| "social media ready" | Platform-specific optimization | Perfect dimensions and quality |
| "create thumbnail" | Small preview image | 150x150px, optimized |

### Platform Specifications
| Platform | Post | Story/Reel | Profile | Cover/Header |
|----------|------|------------|---------|--------------|
| Instagram | 1080x1080 | 1080x1920 | 320x320 | - |
| Facebook | 1200x630 | 1080x1920 | 400x400 | 820x312 |
| Twitter | 1200x675 | - | 400x400 | 1500x500 |
| LinkedIn | 1200x627 | - | 400x400 | 1584x396 |
| YouTube | - | - | 800x800 | 2560x1440 |

### Quality Guidelines
- **95-100%**: Archival/print quality
- **85-90%**: Web/social media (sweet spot)
- **75-80%**: Thumbnails
- **60-70%**: High compression
- **<60%**: Maximum compression (visible loss)

.

## 📚 Other Resources

- [Imagician MCP GitHub](https://github.com/flowy11/imagician)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Claude Desktop Download](https://claude.ai/download)
- [WebP Information](https://developers.google.com/speed/webp)
- [Image Optimization Guide](https://web.dev/fast/#optimize-your-images)
- [Social Media Image Sizes](https://sproutsocial.com/insights/social-media-image-sizes-guide/)

---

*Transform natural language into perfectly optimized images. Just describe what you need, and watch your images transform while learning optimization best practices.*