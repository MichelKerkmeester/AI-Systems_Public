# Imagician Agent - User Guide v1.2.0

## 🆕 What's New in v1.2.0

- **🚨 MANDATORY PATH ASKING**: System now ALWAYS asks for file paths before ANY operation
- **📁 Path-First Protocol**: Every interaction starts with "Where is your image located on your Mac?"
- **✅ Explicit Confirmation**: Always confirms paths before processing
- **🖥️ macOS Optimization**: Perfect integration with Mac filesystem
- **🎯 Zero Ambiguity**: Never processes without knowing exact input and output locations
- **📚 Path Education**: Teaches proper Mac file path usage
- **All v1.1.0 features preserved**: Sequential and Cascade Thinking still included

## ⚠️ CRITICAL CHANGE IN v1.2.0

**The system now ALWAYS asks for file paths first - NO EXCEPTIONS**

This means:
- Even if you say "edit photo.jpg", it asks "Where is photo.jpg located?"
- Even in quick mode, it asks for paths
- It never assumes files are on Desktop
- It always asks where to save results

**Why this change?** 100% accuracy, zero confusion, perfect file tracking

---

## 🚀 What is This?

The Imagician Agent transforms natural language into professional image operations, making image editing 10x easier. **v1.2.0 ensures perfect accuracy by always asking for file paths first.**

**Key Benefits:**
- **NEW: Always knows exactly which file to process**
- Transform conversations into optimized images
- No confusion between chat uploads and local files
- Clear tracking of input and output locations
- Interactive mode guides you through editing decisions
- Professional results for web, email, and social media
- Enhanced intelligence through MCP thinking tools

**Key Principle:** The agent will ALWAYS ask where your files are before processing.

---

## 🖥️ How It Works on Mac

### The Path-First Workflow (NEW in v1.2.0)

**EVERY operation follows this sequence:**

1. **You request something**: "optimize my photo"
2. **Agent asks for path**: "Where is your photo located on your Mac?"
3. **You provide path**: "~/Desktop/vacation.jpg"
4. **Agent confirms**: "Found vacation.jpg (4.2MB). Is this correct?"
5. **Agent asks output**: "Where should I save the result?"
6. **You choose**: "Same folder" or custom path
7. **Agent processes**: Shows exactly what it's doing
8. **Agent confirms**: "Saved to ~/Desktop/vacation-optimized.jpg"

### Understanding Mac File Paths

**Valid path formats the agent accepts:**
```bash
~/Desktop/photo.jpg          # Most common - home directory shorthand
~/Downloads/image.png        # Downloads folder
~/Pictures/vacation/pic.jpg  # Nested folders
/Users/john/Desktop/pic.jpg  # Full absolute path
./images/photo.jpg           # Relative to current directory
```

**Common Mac directories:**
- `~/Desktop/` - Your desktop
- `~/Downloads/` - Downloaded files
- `~/Documents/` - Document storage
- `~/Pictures/` - Photo library
- `~/Library/Mobile Documents/com~apple~CloudDocs/` - iCloud Drive

---

## 📋 Quick Setup in Claude Desktop

### Step 1: Install Imagician MCP
1. Install Claude Desktop from [claude.ai/download](https://claude.ai/download)
2. Install Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
3. Set up Imagician (see installation section below)

### Step 2: Create a New Project in Claude
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Imagician Agent v1.2"

### Step 3: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste: `Agent - Imagician MCP - v1.2.0.md`
4. Save the project

### Step 4: Upload Reference Documents
Upload these to your project:
- `Imagician - Interactive Mode - v1.2.0.md` (conversational guidance with path-first)
- `Imagician - Patterns & Workflows - v1.2.0.md` (operation mappings with macOS paths)
- `Imagician - Platform Specs & Defaults - v1.2.0.md` (platform specifications with path handling)

### Step 5: Save Your Images Locally
**IMPORTANT**: Save any images you want to edit to your Mac FIRST (Desktop, Downloads, etc.)

### Step 6: Start Editing!
Begin any conversation, and Claude will ALWAYS ask for file paths first.

---

## 🎨 Core Capabilities

### What the Agent Can Do
1. **Resize** - Change dimensions (always asks where file is first)
2. **Convert** - Transform formats (asks for input/output paths)
3. **Compress** - Reduce file size (confirms paths before processing)
4. **Crop** - Extract regions (validates file location)
5. **Rotate** - Rotate by angle (asks where to save)
6. **Flip** - Mirror image (confirms both paths)
7. **Get Info** - Extract metadata (asks for file path)
8. **Batch Process** - Multiple images (asks for directory)

### The Path-First Approach (v1.2.0)
- **EVERY operation** starts with asking for file location
- **NO assumptions** about where files are
- **EXPLICIT confirmation** before processing
- **CLEAR output paths** always specified

---

## 🎯 How to Use (v1.2.0 Workflow)

### Basic Usage - Path First!

**Example 1: Simple Optimization**
```
You: optimize my photo

Agent: I'll help you optimize your photo! First, I need to know:

📁 Where is your photo located on your Mac?

Common locations:
• Desktop: ~/Desktop/filename.jpg
• Downloads: ~/Downloads/filename.jpg
• Pictures: ~/Pictures/filename.jpg

Please provide the complete path:

You: ~/Desktop/sunset.jpg

Agent: Great! I found sunset.jpg on your Desktop.

📍 Input: ~/Desktop/sunset.jpg
✓ Size: 5.2MB
✓ Dimensions: 3840x2160

Is this correct? (yes/no)

You: yes

Agent: Perfect! Now, where should I save the optimized version?

Options:
1. Same folder: ~/Desktop/sunset-optimized.jpg
2. New subfolder: ~/Desktop/optimized/sunset.jpg
3. Custom location (specify path)

Your choice (1/2/3):
```

**Example 2: Even with Filename Provided**
```
You: resize photo.jpg to 800px

Agent: I'll help you resize photo.jpg! To ensure I'm working with the right file:

📁 What's the complete path to photo.jpg on your Mac?

For example:
• ~/Desktop/photo.jpg
• ~/Downloads/photo.jpg
• ~/Documents/photo.jpg

Please provide the full path:
```

### Mode Selection - All Require Paths!

| Mode | Command | Path Requirement | First Question |
|------|---------|------------------|----------------|
| **Interactive** | Default | ALWAYS asks | "Where is your image located?" |
| **Quick** | `$q` | STILL asks | "Where is your image located?" |
| **Batch** | `$b` | Asks for directory | "Where are your images located?" |
| **Platform** | `$p` | Asks first | "Where is your image located?" |
| **Web** | `$w` | Asks first | "Where is your image located?" |

**NO MODE SKIPS PATH COLLECTION IN v1.2.0**

---

## 🧠 Intelligent MCP System

### How It Works
The v1.2.0 system includes two thinking tools that enhance decision-making:

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
The agent automatically chooses the right thinking tool AFTER collecting paths:

| Your Request | MCP Selected | Why |
|--------------|--------------|-----|
| "Resize to 800px" | Sequential | Single clear operation |
| "Make it smaller" | Cascade | Needs to explore resize vs compress |
| "For my website" | Cascade | Multiple optimization decisions |
| "Convert to JPEG" | Sequential | Direct format conversion |
| "All social media" | Cascade | Complex multi-platform workflow |

**Note:** Path collection ALWAYS happens first, before MCP selection.

---

## ❌ Common Mistakes (What NOT to Do)

### Mistake 1: Uploading to Chat
```
❌ WRONG: [Upload image to Claude chat] "optimize this"
✅ RIGHT: Save to Desktop first, then say "optimize ~/Desktop/photo.jpg"
```

### Mistake 2: Assuming Agent Knows Location
```
❌ WRONG: "edit photo.jpg" (expecting it to find the file)
✅ RIGHT: Wait for agent to ask "Where is photo.jpg located?"
```

### Mistake 3: Using Windows Paths
```
❌ WRONG: "C:\Users\John\photo.jpg"
✅ RIGHT: "~/Desktop/photo.jpg" or "/Users/john/Desktop/photo.jpg"
```

---

## ✅ Output Format (v1.2.0)

### Every Operation Shows Full Paths
```
📸 Processing Image
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Reading from: ~/Desktop/vacation.jpg
🔄 Applying optimizations...
📍 Saving to: ~/Desktop/vacation-web.webp
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before: ~/Desktop/vacation.jpg (4.2MB, JPEG)
After: ~/Desktop/vacation-web.webp (1.1MB, WebP)

✅ Complete! Your optimized image is at:
~/Desktop/vacation-web.webp
```

---

## 🔧 Installing MCPs (Required & Optional)

### Required: Imagician MCP

The Imagician MCP provides core image editing capabilities.

#### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- macOS (Intel or Apple Silicon)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the Imagician MCP image editing tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/flowy11/imagician.git (main tool)
   - https://github.com/modelcontextprotocol/server-sequential-thinking.git (optional)
   - https://github.com/cascadethinking/cascade-thinking-mcp.git (optional)
3. Set up volume mounts for Mac directories (Desktop, Downloads, Documents, Pictures)
4. Create Dockerfiles if needed
5. Create a docker-compose.yml file with all services
6. Configure Claude Desktop's claude_desktop_config.json
7. Build and start the containers with docker-compose

I'm on macOS. Please give me the exact commands to run, including how to:
- Mount my Mac folders so Imagician can access them
- Set up the proper permissions
- Configure Claude Desktop to use the Docker containers
```

The AI will provide step-by-step commands for your Mac.

**Verification:**
1. Check Docker Desktop for running containers (imagician-mcp, and optionally sequential-thinking-mcp, cascade-thinking-mcp)
2. Look for the 🔌 icon in Claude Desktop showing connected tools
3. Test with: "I want to optimize an image" (agent should ask for file path)

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
      "args": ["-y", "@flowy11/imagician"]
    }
  }
}
```

### Optional: Thinking MCPs (Enhanced Intelligence)

For better optimization decisions, add thinking tools:

```json
{
  "mcpServers": {
    "imagician": {
      // ... imagician config above
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
- **Cascade Thinking**: Smarter optimization workflows
- **Automatic selection**: Agent chooses the right tool
- **Better decisions**: Explores all optimization options
- **Intelligent analysis**: Evaluates quality trade-offs

### Quick Verification
1. Look for 🔌 icon in Claude Desktop showing all tools
2. Test with: "optimize my photo" (should ask for path)
3. Check Docker Desktop for running containers

---

## 🆘 Troubleshooting v1.2.0

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Why does it always ask for paths?"** | This is intentional in v1.2.0 for 100% accuracy |
| **"I uploaded to chat"** | Save to Mac first, then provide path like ~/Desktop/image.jpg |
| **"File not found"** | Check spelling (case-sensitive), include extension (.jpg) |
| **"Too many questions"** | Path questions ensure accuracy: location → confirm → output → proceed |
| **"MCP not connected"** | Restart Claude Desktop, check Docker is running |
| **"Permission denied"** | Check file permissions, try copying to Desktop |

### Quick Fixes

**Docker Issues:**
```bash
# Check if running
docker ps
# View logs
docker logs imagician-mcp
# Restart
docker-compose restart
```

**NPX Issues:**
- Ensure Node.js installed
- Check config file syntax
- Restart Claude Desktop

### Path Finding Commands
```bash
# List images on Desktop
ls ~/Desktop/*.{jpg,png,jpeg,webp}

# Find a specific image
find ~ -name "photo.jpg" 2>/dev/null

# Check current directory
pwd

# Check file permissions
ls -la ~/Desktop/photo.jpg
```

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop first
- **Can't connect**: Restart Claude Desktop after config changes
- **Wrong directory**: Ensure you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)
- **Containers won't build**: Check Docker Desktop has enough resources allocated

### Common Setup Problems
- **"Command not found"**: Install Node.js for NPX method
- **Tools not showing**: Restart Claude Desktop after config changes
- **Volume mount issues**: Ensure Docker has permission to access your Mac folders
- **Path not accessible**: Check Docker Desktop file sharing settings

### AI Assistant Help
If you encounter issues, ask an AI assistant:
```
I'm trying to set up Imagician MCP on Mac but getting [ERROR].
Docker shows [STATUS].
Claude Desktop shows [WHAT YOU SEE].
Help me fix this.
```

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop console logs
- For path issues: Verify file exists with `ls` command
- For general issues: The AI assistant can help diagnose problems

---

## ⚠️ Important Notes

- **v1.2.0 ALWAYS asks for paths** - This is not optional
- **Files must be on your Mac** - Not in chat uploads
- **Original files preserved** - Never overwrites without permission
- **Full paths shown** - Always know where files are
- **macOS optimized** - Works with Mac filesystem
- **MCP intelligence** - Sequential and Cascade Thinking enhance operations

---

## 📦 Version History

- **v1.2.0**: MANDATORY path asking, zero ambiguity operations, macOS optimization
- **v1.1.0**: Added Sequential and Cascade Thinking MCP support
- **v1.0.0**: Initial release with 5 operational modes

---

## 🎯 Key Principles (v1.2.0)

1. **Paths first, always** - Never process without explicit paths
2. **Zero assumptions** - Always confirm file locations
3. **Full transparency** - Show input and output paths
4. **Education focus** - Teach proper Mac path usage
5. **Error prevention** - Path validation prevents all file errors
6. **User control** - You always know what's being processed
7. **Intelligent processing** - MCP tools optimize decisions after paths confirmed

---

## 📚 Quick Reference

### The v1.2.0 Workflow (ALWAYS)
1. **ASK** → "Where is your image located?"
2. **VALIDATE** → Check file exists
3. **CONFIRM** → "Is this correct?"
4. **ASK OUTPUT** → "Where to save?"
5. **PROCESS** → With confirmed paths
6. **CONFIRM** → "Saved to [path]"

### Common Operations (All Ask Paths First)
| Request | First Question | Then What |
|---------|---------------|-----------|
| "make it smaller" | "Where is your image?" | Size/compress options |
| "for my website" | "Where is your image?" | Web optimization |
| "Instagram ready" | "Where is your image?" | 1080x1080 square |
| "create thumbnail" | "Where is your image?" | 150x150 preview |
| "batch process" | "Where are your images?" | Folder operations |

### Mac Path Cheat Sheet
| What You Want | Use This Path |
|---------------|---------------|
| Desktop file | `~/Desktop/filename.jpg` |
| Downloads | `~/Downloads/filename.jpg` |
| Pictures folder | `~/Pictures/filename.jpg` |
| iCloud Drive | `~/Library/Mobile Documents/com~apple~CloudDocs/` |
| Current folder | `./filename.jpg` |

### Platform Specifications Quick Reference
| Platform | Post | Story/Reel | Profile | Cover/Header |
|----------|------|------------|---------|--------------|
| Instagram | 1080x1080 | 1080x1920 | 320x320 | - |
| Facebook | 1200x630 | 1080x1920 | 400x400 | 820x312 |
| Twitter | 1200x675 | - | 400x400 | 1500x500 |
| LinkedIn | 1200x627 | - | 400x400 | 1584x396 |
| YouTube | - | - | 800x800 | 2560x1440 |
| Pinterest | 1000x1500 | 1080x1920 | - | - |

---

## 📚 Resources

### Core Tools
- [Imagician MCP GitHub](https://github.com/flowy11/imagician) (Required)
- [Claude Desktop](https://claude.ai/download) (Required)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Required)

### Optional Intelligence MCPs
- [Sequential Thinking MCP](https://github.com/modelcontextprotocol/server-sequential-thinking)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp)

### Documentation
- [MCP Protocol](https://modelcontextprotocol.io/)
- [macOS Terminal Guide](https://support.apple.com/guide/terminal/welcome/mac)
- [Understanding File Paths](https://www.howtogeek.com/181774/htg-explains-what-is-the-path-variable/)
- [Web Image Optimization](https://web.dev/fast/#optimize-your-images)
- [Social Media Image Sizes](https://sproutsocial.com/insights/social-media-image-sizes-guide/)

---

*v1.2.0 ensures perfect accuracy by always asking for file paths first. Every operation starts with "Where is your image located on your Mac?" - no exceptions. This guarantees you always know exactly what's being processed and where results are saved.*