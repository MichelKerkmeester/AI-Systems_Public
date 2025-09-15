# Media Editor System - User Guide v0.111

An intelligent media processing system that transforms natural language requests into optimized images, videos, and audio through conversational guidance. Combines two MCP servers (Imagician for images, Video-Audio for media) with smart defaults and pattern learning.

## 📋 Table of Contents

- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🔧 Installing MCP Tools](#installing-mcp-tools)
- [🧠 How It Works](#how-it-works)
- [🎛️ Operating Modes](#operating-modes)
- [💬 Example Interactions](#example-interactions)
- [📊 Visual Feedback](#visual-feedback)
- [⚡ Emergency Commands](#emergency-commands)
- [🆘 Troubleshooting](#troubleshooting)
- [⚠️ Important Notes](#important-notes)
- [📚 Resources](#resources)



## ✨ Key Features

### Core Capabilities
- **MCP Connection Verification**: Always checks server availability first
- **Universal Media Processing**: Images, videos, and audio in one system
- **Natural Language Understanding**: Describe what you want in plain words
- **MEDIA Framework**: 5-phase thinking methodology
- **User-Controlled Depth**: Choose 1-10 thinking rounds
- **Challenge Mode**: Automatically questions complexity at 3+ rounds
- **Pattern Learning**: Adapts to your preferences
- **Visual Feedback**: Real-time progress directly in chat
- **Rate Limiting**: Smart API usage management
- **Educational Insights**: Learn why optimizations work

### What It Can Do

**Image Operations:**
- Resize, crop, rotate, flip
- Convert between JPEG, PNG, WebP, AVIF
- Compress with quality control
- Batch process multiple images
- Extract metadata

**Video Operations:**
- Transcode between formats (MP4, MOV, AVI, WebM)
- Compress with bitrate control
- Trim and concatenate videos
- Add text/image overlays
- Extract frames for thumbnails

**Audio Operations:**
- Extract audio from videos
- Convert between formats (MP3, WAV, AAC, FLAC)
- Normalize audio levels
- Adjust sample rates
- Remove silence

### What It Cannot Do
- ❌ Generate new content with AI
- ❌ Complex editing (color grading, effects)
- ❌ Real-time processing
- ❌ Upload to platforms
- ❌ Files larger than system memory



## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Media Editor"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Media Editor.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these documents to your project:
- `Media Editor - Interactive Intelligence.md`
- `Media Editor - Patterns & Workflows.md`
- `Media Editor - MEDIA Thinking Framework.md`
- `Media Editor - MCP Intelligence - Imagician.md`
- `Media Editor - MCP Intelligence - Video, Audio.md`

### Step 4: Install MCP Tools
See next section for detailed setup

### Step 5: Start Processing
```
optimize my vacation photos          # Interactive discovery
$image resize to 1920px              # Direct image mode
$video compress presentation.mp4     # Direct video mode
$quick resize photo.jpg              # Fast processing
```



## 🔧 Installing MCP Tools

The Media Editor requires two MCP servers:

### Prerequisites
- Node.js (for Imagician)
- Python 3.8+ (for Video-Audio)
- FFmpeg (for Video-Audio)
- Claude Desktop app

### Option A: Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed
- Claude Desktop app

**Quick Setup:**
Ask any AI assistant:
```
Help me set up Docker containers for Media Editor MCP tools:
1. Imagician MCP: https://github.com/flowy11/imagician
2. Video-Audio MCP: https://github.com/misbahsy/video-audio-mcp

Create docker-compose.yml and configure claude_desktop_config.json.
I'm on [Windows/Mac/Linux].
```

### Option B: Direct Installation

**Imagician (NPX):**
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

**Video-Audio (Python/UV):**
1. Install FFmpeg first
2. Clone the repository
3. Install UV package manager
4. Configure as shown in documentation

**Config Location:**
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/claude/claude_desktop_config.json`

### Verification
After installation, restart Claude Desktop and check:
```
🔧 Setup Verification

✔ Imagician: Connected
✔ Video-Audio: Connected
✔ FFmpeg: Installed
✔ Configuration: Valid

Ready for media processing!
```



## 🧠 How It Works

### MCP Connection Verification

System always verifies MCP connections first:
```
📌 MCP Connection Check

• Imagician: ✅ Connected
• Video-Audio: ✅ Connected

All media operations available.
```

### Intent Recognition & Routing

| Confidence | Range | Response | Example |
|------------|-------|----------|---------|
| **Exact** | >0.95 | Ask rounds → Execute | "Convert to MP4" |
| **High** | 0.80-0.95 | Clarify → Execute | "Make smaller" → "File size or dimensions?" |
| **Medium** | 0.50-0.79 | Explore → Execute | "Optimize this" → "For web or email?" |
| **Low** | <0.50 | Guide → Execute | "Help" → Show capabilities |

### MEDIA Thinking Framework
1. **Pre-Check**: Verify MCP connections
2. **M - Measure**: Analyze source media
3. **E - Evaluate**: Generate processing strategies
4. **D - Decide**: Select best approach
5. **I - Implement**: Execute with monitoring
6. **A - Analyze**: Verify and learn

### Challenge Mode
Automatically activates at 3+ thinking rounds:
```
Full package would include:
• 10+ platform versions
• Multiple formats

Simpler alternative:
• Top 3 platforms only
• Standard formats

Which approach?
```

.

## 🎛️ Operating Modes

| Mode | Command | Purpose | Use When |
|------|---------|---------|----------|
| **Interactive** | DEFAULT | Guided discovery | Not sure what you need |
| **Image** | `$image`/`$img` | Image processing | Working with photos |
| **Video** | `$video`/`$vid` | Video processing | Video files |
| **Audio** | `$audio`/`$aud` | Audio processing | Audio extraction |

### Mode Activation

**Interactive Mode (Default):**
```
User: help with my media files
System: [Checking MCP connections...]
✅ Media processing ready!

What type of media?
• Images (photos, graphics)
• Videos (movies, clips)
• Audio (music, podcasts)
```

**Direct Mode:**
```
User: $image resize photo.jpg to 800px
System: [Checking Imagician...]
✅ Connected!

How many thinking rounds? (1-10)
Recommended: 2-3 for simple resize
```

.

## 💬 Example Interactions

### Simple Image Optimization
```
User: optimize photo for web

System: I'll optimize your photo for the web!

How many thinking rounds? (1-10)
Recommended: 4 rounds

User: 4

System: [Using 4 rounds of MEDIA thinking]

🎬 Image Processing Operation

Thinking: Standard (4 rounds)
Operation: Web optimization

📂 Input:
├── File: photo.jpg (4.2 MB)
└── Format: JPEG

📄 Processing:
├── Resize to 1920px ✔
├── Convert to WebP ✔
└── Optimize quality to 85% ✔

Progress: [████████████████] 100%
API calls: 2/60 🟢

✅ Operation Complete!

📊 Results:
├── Size: 4.2 MB → 487 KB (88% reduction)
├── Quality: 85% maintained
└── Load time: 5× faster

💡 WebP provides better compression than JPEG

📝 Output: photo-web.webp
```

.

## 📊 Visual Feedback

All operations display real-time feedback:

### Standard Operation Display
```
🎬 Media Processing Operation

Thinking: [Mode] ([X] rounds)
Media Type: [Type]
Operation: [Description]

📂 Input: [Details]
📄 Processing: [Steps with checkmarks]
Progress: [Visual bar]
API calls: [X/60] [Status indicator]

✅ Results: [Metrics]
💡 Insight: [Educational tip]
📝 Output: [Location]
```

### API Usage Indicators
- 🟢 **Green (0-30)**: Safe zone
- 🟡 **Yellow (31-45)**: Caution
- 🟠 **Orange (46-50)**: Warning
- 🔴 **Red (51-55)**: Critical
- ⛔ **Limit (60)**: Wait required

.

## ⚡ Emergency Commands

| Command | Action | Result | Use When |
|---------|--------|--------|----------|
| **`$reset`** | Clear all context | Fresh start | Switching projects |
| **`$quick`** | Fast processing | Minimal questions | Know what you want |
| **`$status`** | Show patterns | Display context | Check what's tracked |
| **`$abort`** | Cancel operation | Stop processing | Something's wrong |

### Command Examples
```
$reset
# Clears all patterns and history

$quick resize photo.jpg
# Skips discovery, minimal rounds

$status
# Shows MCP status and patterns
```

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **MCP not connected** | Server not running | Restart Claude Desktop |
| **FFmpeg not found** | Not installed | Install FFmpeg |
| **Format not supported** | Invalid format | Check supported list |
| **File not found** | Wrong path | Verify file location |
| **Processing slow** | Large file | Use $quick mode |
| **Rate limit hit** | Too many requests | Wait 60 seconds |

### MCP Connection Issues
```
⚠️ MCP Connection Failed

1. Check configuration file
2. Verify installation paths
3. Restart Claude Desktop
4. Check server logs
```

### Quick Fixes
```
$status    # Check current state
$reset     # Clear if needed
$quick     # Fast mode
```

.

## ⚠️ Important Notes

### Best Practices
- **Check connections**: System verifies MCP servers automatically
- **Start simple**: Use fewer thinking rounds for basic operations
- **Accept challenges**: They often lead to better results
- **Watch rate limits**: Monitor API usage indicator
- **Use appropriate formats**: WebP for web, MP4 for video
- **Batch wisely**: Process similar files together

### Performance Guidelines
- **MCP Check**: <1 second
- **Images**: <5 seconds for most operations
- **Videos**: 30-120 seconds depending on size
- **Audio**: 5-30 seconds for extraction
- **Batch**: 1-2 seconds per file
- **Rate limit**: 60 requests per minute

### Quality Recommendations
- **Web images**: 85% quality, WebP format
- **Email attachments**: 80% quality, smaller dimensions
- **Social media**: Platform-specific settings
- **Archival**: Lossless formats, maximum quality
- **General use**: 85-90% quality balance

.

## 📚 Resources

### MCP Server Documentation
- [Imagician MCP](https://github.com/flowy11/imagician) - Image processing
- [Video-Audio MCP](https://github.com/misbahsy/video-audio-mcp) - Media processing

### Tools & Platforms
- [Claude Desktop](https://claude.ai/download) - Required for MCP
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - Container setup
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html) - Video/audio
- [Sharp Documentation](https://sharp.pixelplumbing.com/) - Image processing

### Format References
- [WebP Guide](https://developers.google.com/speed/webp) - Modern images
- [H.264 Overview](https://en.wikipedia.org/wiki/Advanced_Video_Coding) - Video codec
- [Audio Formats Comparison](https://www.adobe.com/creativecloud/video/discover/audio-file-formats.html)

---

*Transform natural language into professional media operations. MCP connections verified automatically. Intelligent processing for images, video, and audio. Challenge complexity, embrace optimization, deliver quality.*