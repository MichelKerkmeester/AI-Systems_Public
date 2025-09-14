# Media Editor System - User Guide v0.111

The Media Editor is an intelligent media processing system that transforms natural language requests into optimized images, videos, and audio through conversational guidance. It combines two powerful MCP servers (Imagician for images, Video-Audio for media) with smart defaults, challenge mode, and comprehensive pattern learning to deliver professional media operations accessible to everyone.

## 📋 Table of Contents

- [✨ Key Features](#✨-key-features)
- [🚀 Quick Setup](#🚀-quick-setup)
- [🧠 How It Works](#🧠-how-it-works)
- [🎛️ Operating Modes](#🎛️-operating-modes)
- [⚡ Emergency Commands](#⚡-emergency-commands)
- [💬 Example Interactions](#💬-example-interactions)
- [📊 Visual Feedback](#📊-visual-feedback)
- [🔧 Installing MCP Tools](#🔧-installing-mcp-tools)
- [🆘 Troubleshooting](#🆘-troubleshooting)
- [⚠️ Important Notes](#⚠️-important-notes)
- [📚 Resources](#📚-resources)

---

## ✨ Key Features

### Core Capabilities
- **MCP Connection Verification**: Always checks server availability before operations
- **Universal Media Processing**: Images, videos, and audio in one intelligent system
- **Natural Language Understanding**: Describe what you want in plain words
- **MEDIA Framework**: 5-phase thinking methodology (Measure, Evaluate, Decide, Implement, Analyze)
- **User-Controlled Depth**: Choose 1-10 thinking rounds for any operation
- **Challenge Mode**: Automatically questions complexity at 3+ rounds
- **Pattern Learning**: Adapts to your preferences within sessions
- **Past Conversations Search**: Finds relevant previous work for context
- **Visual Feedback**: Real-time progress and results directly in chat
- **Rate Limiting**: Smart API usage management with visual indicators
- **Educational Insights**: Learn why optimizations work

### What It Can Do

**Image Operations (via Imagician MCP):**
- Resize, crop, rotate, flip images
- Convert between JPEG, PNG, WebP, AVIF
- Compress with quality control
- Batch process multiple images
- Extract metadata

**Video Operations (via Video-Audio MCP):**
- Transcode between formats (MP4, MOV, AVI, WebM)
- Compress with bitrate control
- Trim and concatenate videos
- Add text/image overlays
- Extract frames for thumbnails
- Add subtitles

**Audio Operations (via Video-Audio MCP):**
- Extract audio from videos
- Convert between formats (MP3, WAV, AAC, FLAC)
- Normalize audio levels
- Adjust sample rates
- Remove silence

### What It Cannot Do (MCP Limitations)
- ❌ Generate new content with AI
- ❌ Complex editing (color grading, effects)
- ❌ Real-time processing
- ❌ Upload to platforms
- ❌ Files larger than system memory
- ❌ Advanced filters or transformations

---

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Media Editor"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - Media Editor.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 5 essential documents to your project:
- `Media Editor - Interactive Intelligence.md` (Conversation interface)
- `Media Editor - Patterns & Workflows.md` (Pattern recognition)
- `Media Editor - MEDIA Thinking Framework.md` (Thinking methodology)
- `Media Editor - MCP Intelligence - Imagician.md` (Image operations)
- `Media Editor - MCP Intelligence - Video, Audio.md` (Video/audio operations)

### Step 4: Install MCP Tools
See [Installing MCP Tools](#🔧-installing-mcp-tools) section below for detailed setup

### Step 5: Verify Connection
The system will automatically check MCP connections when you start:
```
🔌 Checking MCP Connections...
─────────────────
• Imagician (Images): [Status]
• Video-Audio (Media): [Status]
```

### Step 6: Start Processing
```
optimize my vacation photos          # Interactive discovery
$image resize to 1920px              # Direct image mode
$video compress presentation.mp4     # Direct video mode
$audio extract from interview.mov    # Direct audio mode
$quick resize photo.jpg              # Fast processing
$status                              # Check current patterns
```

---

## 🧠 How It Works

### MCP Connection Verification

The system always verifies MCP server connections before attempting any operation:

```markdown
🔌 MCP Connection Check
─────────────────
• Imagician: ✅ Connected
• Video-Audio: ✅ Connected

All media operations available.
```

### Intent Recognition & Routing

The system analyzes your request and routes to appropriate processing:

| Confidence | Range | Response | Example |
|------------|-------|----------|---------|
| **Exact** | >0.95 | Ask rounds → Execute | "Convert to MP4" |
| **High** | 0.80-0.95 | Clarify → Execute | "Make smaller" → "File size or dimensions?" |
| **Medium** | 0.50-0.79 | Explore → Execute | "Optimize this" → "For web or email?" |
| **Low** | <0.50 | Guide → Execute | "Help" → Show capabilities |

### MEDIA Thinking Framework

Every operation uses the MEDIA methodology:
1. **Pre-Check**: Verify MCP connections
2. **M - Measure & Assess**: Analyze source media
3. **E - Evaluate Options**: Generate processing strategies
4. **D - Decide Strategy**: Select best approach
5. **I - Implement**: Execute with monitoring
6. **A - Analyze & Adapt**: Verify and learn

### Challenge Mode

Automatically activates at 3+ thinking rounds:
```
User: Create social media package with everything

System: That's complex! Let me challenge this:

Full package would include:
• 10+ platform versions
• Multiple formats
• Various dimensions

Simpler alternative:
• Top 3 platforms only
• Standard formats
• Essential sizes

Which approach? (Both available)
```

---

## 🎛️ Operating Modes

| Mode | Command | Purpose | Use When |
|------|---------|---------|----------|
| **Interactive** | DEFAULT | Guided discovery | Not sure what you need |
| **Image** | `$image`/`$img` | Image processing | Working with photos/graphics |
| **Video** | `$video`/`$vid` | Video processing | Video files |
| **Audio** | `$audio`/`$aud` | Audio processing | Audio extraction/conversion |

### Mode Activation Examples

**Interactive Mode (Default):**
```
User: help with my media files
System: [Checking MCP connections...]
✅ Media processing ready!

Let's figure out what you need!

What type of media?
• Images (photos, graphics)
• Videos (movies, clips)
• Audio (music, podcasts)
• Mixed (various types)
```

**Direct Mode:**
```
User: $image resize photo.jpg to 800px
System: [Checking Imagician connection...]
✅ Imagician connected!

I'll resize your image to 800px!

How many thinking rounds? (1-10)
Recommended: 2-3 for simple resize
```

---

## ⚡ Emergency Commands

### Quick Control Commands

| Command | Action | Result | Use When |
|---------|--------|--------|----------|
| **`$reset`** | Clear all context | Fresh start | Switching projects |
| **`$standard`** | Default settings | No patterns | Want clean process |
| **`$quick`** | Fast processing | Minimal questions | Know what you want |
| **`$status`** | Show patterns | Display context | Check what's tracked |
| **`$abort`** | Cancel operation | Stop processing | Something's wrong |
| **`$help`** | Show commands | List options | Need guidance |

### Command Usage Examples

```markdown
$reset
# Clears all patterns and history
# Perfect for starting new project

$quick resize photo.jpg
# Skips discovery, minimal rounds
# Still asks thinking depth

$status
# Shows your patterns and MCP status:
# - MCP Connections: ✅
# - Preferred quality: 85%
# - Common format: WebP
# - Average rounds: 4
```

---

## 💬 Example Interactions

### Simple Image Optimization
```
User: optimize photo for web

System: [Checking MCP connections...]
✅ Imagician connected!

I'll optimize your photo for the web!

How many thinking rounds should I use? (1-10)
Recommended: 4 rounds (standard optimization)

User: 4

System: [Using 4 rounds of MEDIA thinking]

🎬 Image Processing Operation
─────────────────
Thinking: Standard (4 rounds)
Media Type: Image
Operation: Web optimization

📂 Input:
├── File: photo.jpg (4.2 MB)
├── Format: JPEG
└── Dimensions: 4000 × 3000

🔄 Processing:
├── Resize to 1920px width ✓
├── Convert to WebP ✓
└── Optimize quality to 85% ✓

Progress: [████████████████████] 100%
Time: 3 seconds
API calls: 2/60 🟢

✅ Operation Complete!

📊 Results:
├── Size: 4.2 MB → 487 KB (88% reduction)
├── Quality: 85% maintained
├── Format: JPEG → WebP
└── Load time: 5× faster

💡 WebP provides better compression than JPEG
   while maintaining visual quality

📁 Output:
└── Saved to: photo-web.webp
```

### Complex Video Processing
```
User: create instagram versions of my product video

System: [Checking Video-Audio MCP...]
✅ Video-Audio MCP connected!

I'll create Instagram-optimized versions!

How many thinking rounds? (1-10)
This is complex - I recommend 7 rounds

User: 7

System: [Challenge Mode Activated]

Before we process everything:
• Full Instagram suite = 4 formats
• Simpler option = Feed + Reels only

Which approach?

User: Simple version

System: [Processing with 7 rounds of thinking]

Creating Instagram versions:
• Feed: 1:1 square, 60s max
• Reels: 9:16 vertical, 90s max

[Visual progress feedback]

✅ Created 2 optimized versions!
Total size reduction: 72%
```

### Batch Processing
```
User: convert all PNGs to WebP

System: [Checking Imagician connection...]
✅ Imagician connected!

I'll convert all your PNG files to WebP!

Found: 15 PNG files in folder

How many thinking rounds? (1-10)
Recommended: 3 (batch operation)

User: 3

System: [Processing batch]

📊 Batch Processing
─────────────────
Files: 15/15
Format: PNG → WebP
Quality: 85%

Progress: [████████████████████] 100%

✅ Batch Complete!
• 15 files converted
• Total saved: 8.7 MB (68%)
• Average quality: 85%
```

---

## 📊 Visual Feedback

All operations display real-time feedback directly in chat:

### Standard Operation Display
```markdown
🎬 Media Processing Operation
─────────────────
Thinking: [Mode] ([X] rounds)
Media Type: [Type]
Operation: [Description]

📂 Input: [Details]
🔄 Processing: [Steps with checkmarks]
Progress: [Visual bar]
Time: [Duration]
API calls: [X/60] [Status indicator]

✅ Results: [Metrics]
💡 Insight: [Educational tip]
📁 Output: [Location]
```

### MCP Connection Status
```markdown
📊 MCP Status
─────────────────
• Imagician: ✅ Connected
• Video-Audio: ✅ Connected
• FFmpeg: v6.0 installed
• Performance: Normal
```

### API Usage Indicators
- 🟢 **Green (0-30)**: Safe zone
- 🟡 **Yellow (31-45)**: Caution
- 🟠 **Orange (46-50)**: Warning
- 🔴 **Red (51-55)**: Critical
- ⛔ **Limit (60)**: Wait required

---

## 🔧 Installing MCP Tools

The Media Editor requires two MCP servers to function:

### Prerequisites
- Node.js (for Imagician)
- Python 3.8+ (for Video-Audio)
- FFmpeg (for Video-Audio)
- Claude Desktop app

### Option A: Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download](https://claude.ai/download))

**AI-Assisted Installation:**
Copy this prompt to any AI assistant:
```
Help me set up Docker containers for Media Editor MCP tools.

I need to install:
1. Imagician MCP: https://github.com/flowy11/imagician
2. Video-Audio MCP: https://github.com/misbahsy/video-audio-mcp

Create docker-compose.yml for both services.
Configure claude_desktop_config.json.
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
4. Configure:
```json
{
  "mcpServers": {
    "video-audio": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/video-audio-mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```

**Config Location:**
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/claude/claude_desktop_config.json`

### Verification
After installation, restart Claude Desktop and check:
```markdown
🔧 Setup Verification
─────────────────
✓ Imagician: Connected
✓ Video-Audio: Connected
✓ FFmpeg: Installed
✓ Configuration: Valid

Ready for media processing!
```

---

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **MCP not connected** | Server not running | Restart Claude Desktop |
| **FFmpeg not found** | Not installed | Install FFmpeg for your OS |
| **Format not supported** | Invalid format | Check supported list |
| **File not found** | Wrong path | Verify file location |
| **Quality too low** | Over-compression | Increase quality % |
| **Processing slow** | Large file | Use $quick mode |
| **Rate limit hit** | Too many requests | Wait 60 seconds |

### MCP Connection Issues

**If servers won't connect:**
```markdown
⚠️ MCP Connection Failed
─────────────────
1. Check configuration file
2. Verify installation paths
3. Restart Claude Desktop
4. Check server logs
5. Reinstall if needed

Need help? Check the setup guide.
```

### Quick Fixes

**Context Issues:**
```
$status    # Check current state & MCP status
$reset     # Clear if needed
$standard  # Use defaults
```

**Speed Issues:**
```
$quick     # Fast mode
Use 1-2 thinking rounds
Smaller batch sizes
```

**Quality Issues:**
```
Increase quality percentage
Use lossless formats
Challenge compression
```

---

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

---

## 📚 Resources

### MCP Server Documentation
- [Imagician MCP](https://github.com/flowy11/imagician) - Image processing via Sharp
- [Video-Audio MCP](https://github.com/misbahsy/video-audio-mcp) - Media processing via FFmpeg

### Tools & Platforms
- [Claude Desktop](https://claude.ai/download) - Required for MCP
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) - For containerized setup
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html) - Video/audio processing
- [Sharp Documentation](https://sharp.pixelplumbing.com/) - Image processing

### Format References
- [WebP Guide](https://developers.google.com/speed/webp) - Modern image format
- [H.264 Overview](https://en.wikipedia.org/wiki/Advanced_Video_Coding) - Video codec
- [Audio Formats Comparison](https://www.adobe.com/creativecloud/video/discover/audio-file-formats.html)

---

*Transform natural language into professional media operations. MCP connections verified automatically. Intelligent processing for images, video, and audio. Challenge complexity, embrace optimization, deliver quality. Every file processed with the perfect balance of size and fidelity.*