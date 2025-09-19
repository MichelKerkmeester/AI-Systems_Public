<<<<<<< HEAD
# Media Editor System - User Guide v0.114
=======
# Media Editor System - User Guide v1.0.0
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

An intelligent media processing system that transforms natural language requests into optimized images, videos, and audio through conversational guidance. Features automatic deep analysis with 10 rounds of professional optimization, ensuring every media operation achieves optimal results without manual configuration.

## 📋 Table of Contents

<<<<<<< HEAD
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
=======
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 How It Works](#-how-it-works)
- [🎛️ Operating Modes](#️-operating-modes)
- [⚡ Emergency Commands](#-emergency-commands)
- [💬 Example Interactions](#-example-interactions)
- [📊 Visual Feedback](#-visual-feedback)
- [🔧 Installing MCP Tools](#-installing-mcp-tools)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📚 Resources](#-resources)
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

.

## ✨ Key Features

### Core Capabilities
- **MCP Connection Verification**: Always checks server availability first
- **Universal Media Processing**: Images, videos, and audio in one system
- **Natural Language Understanding**: Describe what you want in plain words
- **MEDIA Framework**: 5-phase thinking methodology with automatic depth
- **Automatic Deep Thinking**: 10 rounds of optimization for every operation
- **Quick Mode**: Auto-scaled 1-5 rounds for speed-critical tasks
- **Challenge Mode**: Automatically optimizes complexity
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

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Media Editor"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
<<<<<<< HEAD
3. Copy and paste: `Agent - MCP - Media Editor.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these documents to your project:
- `Media Editor - Interactive Intelligence.md`
- `Media Editor - Patterns & Workflows.md`
- `Media Editor - MEDIA Thinking Framework.md`
- `Media Editor - MCP Intelligence - Imagician.md`
- `Media Editor - MCP Intelligence - Video, Audio.md`
=======
3. Copy and paste: `Agent - MCP - Media Editor - v1.1.1.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these 7 essential documents to your project:
- `Agent - MCP - Media Editor - v1.1.1.md` (Main system)
- `Media Editor - Core System Rules & Quick Reference.md` (Emergency commands)
- `Media Editor - Interactive Intelligence.md` (Conversation interface)
- `Media Editor - Patterns & Workflows.md` (Pattern recognition)
- `Media Editor - MEDIA Thinking Framework.md` (Thinking methodology)
- `Media Editor - MCP Intelligence - Imagician.md` (Image operations)
- `Media Editor - MCP Intelligence - Video, Audio.md` (Video/audio operations)
- `README.md` (This guide)
>>>>>>> parent of 77d4afb (Owner = Lean + Versioning)

### Step 4: Install MCP Tools
See next section for detailed setup

### Step 5: Start Processing
```
optimize my vacation photos          # Interactive with auto optimization
$image resize to 1920px              # Direct mode with deep thinking
$video compress presentation.mp4     # Video processing with 10 rounds
$quick resize photo.jpg              # Fast mode with 1-5 auto-scaled rounds
```

.

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
✔ Thinking Mode: 10 rounds automatic

Ready for professional media processing!
```

.

## 🧠 How It Works

### MCP Connection Verification

System always verifies MCP connections first:
```
🔌 MCP Connection Check

• Imagician: ✅ Connected
• Video-Audio: ✅ Connected

All media operations available with automatic optimization.
```

### Intent Recognition & Routing

| Confidence | Range | Response | Processing |
|------------|-------|----------|------------|
| **Exact** | >0.95 | Direct execution | 10 rounds auto |
| **High** | 0.80-0.95 | Clarify → Execute | 10 rounds auto |
| **Medium** | 0.50-0.79 | Explore → Execute | 10 rounds auto |
| **Low** | <0.50 | Guide → Execute | 10 rounds auto |

### MEDIA Thinking Framework (Automatic)
1. **Pre-Check**: Verify MCP connections
2. **M - Measure**: Analyze source media (deep analysis)
3. **E - Evaluate**: Generate processing strategies (10 rounds)
4. **D - Decide**: Select best approach (automatic optimization)
5. **I - Implement**: Execute with monitoring
6. **A - Analyze**: Verify and learn

### Automatic Optimization
The system automatically applies:
- **Standard Mode**: 10 rounds of deep thinking for professional results
- **Quick Mode ($quick)**: 1-5 rounds auto-scaled based on complexity
- **No User Input**: System determines optimal depth automatically
- **Challenge Mode**: Automatically simplifies overly complex requests

.

## 🎛️ Operating Modes

| Mode | Command | Thinking Applied | Use When |
|------|---------|-----------------|----------|
| **Interactive** | DEFAULT | 10 rounds auto | Guided discovery |
| **Image** | `$image`/`$img` | 10 rounds auto | Direct image processing |
| **Video** | `$video`/`$vid` | 10 rounds auto | Direct video processing |
| **Audio** | `$audio`/`$aud` | 10 rounds auto | Direct audio processing |
| **Quick** | `$quick` | 1-5 rounds auto | Speed is priority |

### Mode Activation

**Interactive Mode (Default):**
```
User: help with my media files
System: [Checking MCP connections...]
✅ Media processing ready!

Applying deep analysis (10 rounds)...

What type of media?
• Images (photos, graphics)
• Videos (movies, clips)
• Audio (music, podcasts)
```

**Quick Mode:**
```
User: $quick resize photo.jpg
System: ⚡ Quick mode activated

Auto-scaling optimization...
• Complexity: Simple resize
• Using: 2 rounds (optimized for speed)

Processing immediately...
```

.

## 💬 Example Interactions

### Simple Image Optimization
```
User: optimize photo for web

System: I'll optimize your photo for the web!

Applying professional optimization (10 rounds of deep analysis)...

🎬 Image Processing Operation

Thinking: Deep analysis (10 rounds applied)
Operation: Web optimization

📂 Input:
• File: photo.jpg (4.2 MB)
• Format: JPEG

🔄 Processing:
• Resize to 1920px ✔
• Convert to WebP ✔
• Optimize quality to 85% ✔

Progress: [████████████████] 100%
API calls: 2/60 🟢

✅ Operation Complete!

📊 Results:
• Size: 4.2 MB → 487 KB (88% reduction)
• Quality: 85% maintained
• Load time: 5× faster

💡 WebP provides better compression than JPEG
   Optimization determined via deep analysis

📁 Output: photo-web.webp
```

### Quick Processing Example
```
User: $quick compress video.mp4

System: ⚡ Quick processing engaged

Auto-scaling optimization (3 rounds detected)...
• Complexity: Medium (video compression)
• Speed priority active

🎬 Fast Processing

Results:
• Size reduced by 60%
• Processing time: 50% faster
• Essential quality maintained

📁 Output: video-compressed.mp4
```

.

## 📊 Visual Feedback

All operations display real-time feedback:

### Standard Operation Display
```
🎬 Media Processing Operation

Thinking: Deep analysis (10 rounds automatic)
Media Type: [Type]
Operation: [Description]

📂 Input: [Details]
🔄 Processing: [Steps with checkmarks]
Progress: [Visual bar]
API calls: [X/60] [Status indicator]

✅ Results: [Metrics]
💡 Insight: [Educational tip]
📁 Output: [Location]
```

### Quick Mode Display
```
⚡ Quick Processing

Thinking: Auto-scaled ([X] rounds)
Complexity: [Detected level]
Speed boost: [Percentage faster]

[Simplified progress indicators]

✅ Complete: [Results]
```

### API Usage Indicators
- 🟢 **Green (0-30)**: Safe zone
- 🟡 **Yellow (31-45)**: Caution
- 🟠 **Orange (46-50)**: Warning
- 🔴 **Red (51-55)**: Critical
- ⛔ **Limit (60)**: Wait required

.

## ⚡ Emergency Commands

| Command | Action | Result | Thinking Impact |
|---------|--------|--------|-----------------|
| **`$reset`** | Clear all context | Fresh start | Returns to 10-round auto |
| **`$quick`** | Fast processing | Speed priority | 1-5 rounds auto-scaled |
| **`$status`** | Show patterns | Display context | Shows current mode |
| **`$abort`** | Cancel operation | Stop processing | Cancels current task |

### Command Examples
```
$reset
# Clears patterns, returns to automatic 10-round thinking

$quick resize photo.jpg
# Auto-scales 1-5 rounds based on complexity

$status
# Shows MCP status and current thinking mode
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
| **Processing slow** | Standard mode active | Use $quick for speed |
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
$status    # Check current state and thinking mode
$reset     # Clear patterns, reset to standard
$quick     # Switch to fast mode (1-5 rounds)
```

.

## ⚠️ Important Notes

### Best Practices
- **Automatic optimization**: System applies 10 rounds automatically
- **Use $quick wisely**: Only when speed matters more than quality
- **Trust the system**: Deep analysis ensures optimal results
- **Watch rate limits**: Monitor API usage indicator
- **Use appropriate formats**: WebP for web, MP4 for video
- **Batch processing**: Each file gets full optimization

### Performance Guidelines
- **MCP Check**: <1 second
- **Standard mode (10 rounds)**: Optimal quality, normal speed
- **Quick mode (1-5 rounds)**: 40-60% faster, essential quality
- **Images**: <5 seconds for most operations
- **Videos**: 30-120 seconds depending on size
- **Audio**: 5-30 seconds for extraction
- **Batch**: Full optimization per file
- **Rate limit**: 60 requests per minute

### Quality Recommendations (Automatically Applied)
- **Web images**: 85% quality, WebP format (10 rounds determine)
- **Email attachments**: 80% quality, smaller dimensions (auto-optimized)
- **Social media**: Platform-specific settings (deep analysis)
- **Archival**: Lossless formats, maximum quality (10 rounds ensure)
- **General use**: 85-90% quality balance (automatically selected)

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

*Transform natural language into professional media operations with automatic deep thinking. Every operation receives 10 rounds of optimization automatically. Quick mode intelligently scales 1-5 rounds for speed. MCP connections verified automatically. Intelligent processing for images, video, and audio with no manual configuration required.*