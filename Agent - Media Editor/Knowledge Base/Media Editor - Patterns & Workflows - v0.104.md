# Media Editor - Patterns & Workflows - v0.104

Complete pattern library and workflow specifications for natural language media processing operations (images, video, and audio) with automatic deep thinking.

## Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [🔌 MCP VERIFICATION PATTERNS](#2-🔌-mcp-verification-patterns)
3. [🎯 INTENT PATTERNS](#3-🎯-intent-patterns)
4. [🔄 WORKFLOW PATTERNS](#4-🔄-workflow-patterns)
5. [📐 DIMENSION & RESOLUTION PATTERNS](#5-📐-dimension--resolution-patterns)
6. [🎨 FORMAT & CODEC PATTERNS](#6-🎨-format--codec-patterns)
7. [⚡ OPTIMIZATION PATTERNS](#7-⚡-optimization-patterns)
8. [📱 PLATFORM PATTERNS](#8-📱-platform-patterns)
9. [💾 PATH PATTERNS](#9-💾-path-patterns)
10. [🚀 COMPLETE WORKFLOWS](#10-🚀-complete-workflows)
11. [🧠 THINKING PATTERNS](#11-🧠-thinking-patterns)

---

<a id="1-📋-overview"></a>

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the Media Editor with automatic deep thinking. Each pattern maps natural language to specific operations with smart defaults and automatic optimization across images, video, and audio.

**Critical Requirements:**
- **MCP Verification First**: Always check server connections before operations
- **Visual Consistency**: Use clean bullet lists throughout (NO DIVIDERS)
- **Pattern Adaptability**: All patterns flexible based on user preference
- **Clean Formatting**: Present information without decorative elements
- **Automatic Thinking**: 10 rounds standard, 1-5 auto-scaled for quick mode

**Pattern Categories:**
- **Connection Verification**: MCP server availability checks
- **Intent Recognition**: What the user wants to achieve
- **Parameter Extraction**: Dimensions, quality, formats, codecs, bitrates
- **Workflow Selection**: Single vs multi-step operations
- **Platform Optimization**: Target-specific settings
- **Automatic Depth**: System-determined thinking rounds
- **Media Detection**: Automatic file type recognition

**Integration Points:**
- MCP verification → Natural language → Pattern matching → MCP operation
- Automatic thinking → Processing depth → Quality outcome
- Platform detection → Preset application → Optimized output

---

<a id="2-🔌-mcp-verification-patterns"></a>

## 2. 🔌 MCP VERIFICATION PATTERNS

### Initial Connection Check Pattern

**Pattern: Verify Before Processing**
```yaml
Trigger: Any media operation request
Priority: ALWAYS FIRST
Steps:
  - Check Imagician connection
  - Check Video-Audio connection
  - Report status
  - Guide if not connected
Thinking: Automatic 10 rounds applied
```

### Connection Status Displays

**All Connected:**
```markdown
✅ MCP Servers Ready

• Imagician: Connected
• Video-Audio: Connected
• Thinking mode: 10 rounds automatic

All media operations available with deep optimization.
```

**Partial Connection:**
```markdown
⚠️ Partial MCP Connection

• Imagician: ✅ Connected
• Video-Audio: ❌ Not connected

Available: Image processing only (10 rounds auto)
Unavailable: Video/audio operations

Continue with images or setup video/audio?
```

**No Connection:**
```markdown
❌ MCP Setup Required

No media processing servers connected.

**To enable:**
• Install MCP servers
• Configure Claude Desktop
• Restart application

Would you like setup instructions?
```

### Operation Capability Check

| User Request | Required MCP | Fallback if Unavailable | Thinking Applied |
|-------------|--------------|------------------------|------------------|
| "Resize image" | Imagician | Provide setup guide | 10 rounds auto |
| "Convert video" | Video-Audio | Provide setup guide | 10 rounds auto |
| "Extract audio" | Video-Audio | Provide setup guide | 10 rounds auto |
| "Compress photo" | Imagician | Provide setup guide | 10 rounds auto |
| "Add watermark" | Video-Audio | Provide setup guide | 10 rounds auto |
| "Batch images" | Imagician | Provide setup guide | 10 rounds auto |

---

<a id="3-🎯-intent-patterns"></a>

## 3. 🎯 INTENT PATTERNS

### Universal Compression Intents with Automatic Optimization

| User Says | Media Type | Default Action | Thinking Applied | Parameters |
|-----------|------------|---------------|------------------|------------|
| "make smaller" | Auto-detect | 50% reduction | 10 rounds auto | Smart settings |
| "reduce size" | Auto-detect | Quality/size balance | 10 rounds auto | Maintain quality |
| "compress" | Auto-detect | Format-specific | 10 rounds auto | Optimal compression |
| "$quick shrink" | Auto-detect | 75% of original | 2-3 rounds auto | Basic reduction |
| "too big" | Auto-detect | Smart reduce | 10 rounds auto | Context-aware |
| "email size" | Auto-detect | Email limits | 10 rounds auto | Under 5MB/25MB |
| "web size" | Auto-detect | Web optimize | 10 rounds auto | Fast loading |

### Format Conversion Intents with Deep Analysis

| User Says | Target | Quality | Thinking Applied | MCP Required |
|-----------|--------|---------|------------------|--------------|
| **Images:** |
| "to jpg/jpeg" | JPEG | 90% | 10 rounds auto | Imagician |
| "to png" | PNG | Lossless | 10 rounds auto | Imagician |
| "to webp" | WebP | 85% | 10 rounds auto | Imagician |
| "$quick to jpeg" | JPEG | 85% | 2 rounds auto | Imagician |
| **Video:** |
| "to mp4" | MP4 | Maintain | 10 rounds auto | Video-Audio |
| "to mov" | MOV | Maintain | 10 rounds auto | Video-Audio |
| "to webm" | WebM | VP9 | 10 rounds auto | Video-Audio |
| "$quick to mp4" | MP4 | Basic | 3 rounds auto | Video-Audio |
| **Audio:** |
| "to mp3" | MP3 | 192 kbps | 10 rounds auto | Video-Audio |
| "to wav" | WAV | Lossless | 10 rounds auto | Video-Audio |
| "to aac" | AAC | 128 kbps | 10 rounds auto | Video-Audio |
| "$quick to mp3" | MP3 | 128 kbps | 2 rounds auto | Video-Audio |

---

<a id="4-🔄-workflow-patterns"></a>

## 4. 🔄 WORKFLOW PATTERNS

### Pre-Workflow Verification

**Pattern: MCP Check First**
```yaml
Every Workflow:
  - Verify required MCP servers
  - If not connected:
     - Explain limitation
     - Offer setup help
  - If connected:
     - Apply automatic thinking
     - Proceed with workflow
```

### Single-Step Workflows with Automatic Depth

**Pattern: Universal Format Convert**
```yaml
Trigger: Format name mentioned
Pre-check: Verify MCP connection
Thinking: 10 rounds automatic (or 1-5 if $quick)
Steps:
  - Detect source media type
  - Select appropriate converter
  - Apply optimal settings via deep analysis
  - Convert and save
Example: "convert to webp" → WebP at 85% (10 rounds optimization)
Example: "$quick convert to mp4" → MP4 basic (3 rounds)
```

**Pattern: Smart Compress**
```yaml
Trigger: "compress", "smaller"
Pre-check: Verify MCP connection
Thinking: 10 rounds automatic (standard)
Steps:
  - Analyze media type and size
  - Calculate target size/quality via deep thinking
  - Apply appropriate compression
  - Verify quality maintained
Example: Image → 85% JPEG/WebP (10 rounds)
Example: $quick compress → 75% quality (3 rounds)
```

### Multi-Step Workflows with Deep Analysis

**Pattern: Universal Web Optimization**
```yaml
Trigger: "for website", "web", "online"
Pre-check: Verify all MCP servers
Thinking: 10 rounds automatic
Steps:
  Images (Imagician):
    - Resize to max 1920px
    - Convert to WebP
    - Set quality to 85%
    - Enable progressive
  Videos (Video-Audio):
    - Resize to 1080p max
    - H.264 codec
    - 5 Mbps bitrate
    - Web-optimized container
  Audio (Video-Audio):
    - Convert to MP3
    - 192 kbps bitrate
    - Normalize levels
Result: Web-ready media (fully optimized)
```

**Pattern: Social Media Suite**
```yaml
Trigger: Platform name mentioned
Pre-check: Verify both MCP servers
Thinking: 10 rounds automatic (deep platform analysis)
Steps:
  - Identify media type
  - Apply platform dimensions
  - Optimize quality/size via deep thinking
  - Create platform versions
  - Generate thumbnails
Result: Platform-optimized package
```

---

<a id="5-📐-dimension--resolution-patterns"></a>

## 5. 📐 DIMENSION & RESOLUTION PATTERNS

### Universal Dimension Recognition with Auto-Optimization

| Pattern | Interpretation | Example | Result | Thinking Applied | MCP |
|---------|---------------|---------|--------|------------------|-----|
| `{number}px` | Width in pixels | "800px" | 800 pixels wide | 10 rounds auto | Imagician |
| `{width}x{height}` | Exact dimensions | "1920x1080" | Full HD | 10 rounds auto | Both |
| `{height}p` | Video resolution | "1080p" | 1920x1080 | 10 rounds auto | Video-Audio |
| `{number}%` | Percentage | "50%" | Half size | 10 rounds auto | Both |
| `4K/8K/HD` | Standard sizes | "4K" | 3840x2160 | 10 rounds auto | Both |
| `{ratio}` | Aspect ratio | "16:9" | Maintain ratio | 10 rounds auto | Both |
| `$quick {dim}` | Quick resize | "$quick 800px" | Fast resize | 1-2 rounds auto | Both |

### Common Media Dimensions with Automatic Optimization

| Use Case | Images | Videos | Thinking Applied | MCP Required |
|----------|--------|--------|------------------|--------------|
| **Web Hero** | 1920x1080 | 1920x1080 | 10 rounds auto | Both |
| **Thumbnail** | 150x150 | 320x180 | 10 rounds auto | Both |
| **Mobile** | 640x960 | 720x1280 | 10 rounds auto | Both |
| **Social Square** | 1080x1080 | 1080x1080 | 10 rounds auto | Both |
| **Social Vertical** | 1080x1920 | 1080x1920 | 10 rounds auto | Both |
| **Email Max** | 1024x768 | 1280x720 | 10 rounds auto | Both |

### Responsive Set Patterns with Deep Analysis

**Pattern: Image Responsive Set**
```yaml
Pre-check: Imagician connected
Thinking: 10 rounds automatic (comprehensive optimization)
Sizes:
  - 320px (mobile)
  - 640px (tablet)
  - 1024px (desktop)
  - 1920px (full)
  - 150px (thumbnail)
Formats: WebP with JPEG fallback
Quality: Auto-optimized per size
```

---

<a id="6-🎨-format--codec-patterns"></a>

## 6. 🎨 FORMAT & CODEC PATTERNS

### Format Selection Logic with Automatic Analysis

| Condition | Image Format | Video Container | Audio Format | Thinking Applied | MCP |
|-----------|-------------|-----------------|--------------|------------------|-----|
| Has transparency | PNG/WebP | N/A | N/A | 10 rounds auto | Imagician |
| Photography | JPEG/WebP | MP4 | N/A | 10 rounds auto | Both |
| Web use | WebP | MP4/WebM | MP3 | 10 rounds auto | Both |
| Email | JPEG | MP4 | MP3 | 10 rounds auto | Both |
| Archival | PNG | MOV/MKV | FLAC/WAV | 10 rounds auto | Both |
| Streaming | WebP | MP4 | AAC | 10 rounds auto | Both |
| Professional | RAW/PNG | ProRes | WAV | 10 rounds auto | Both |
| $quick mode | JPEG | MP4 | MP3 | 1-5 rounds auto | Both |

### Codec Selection Intelligence with Deep Thinking

| Intent | Video Codec | Audio Codec | Container | Thinking Applied | Use Case | MCP |
|--------|------------|-------------|-----------|------------------|----------|-----|
| Universal | H.264 | AAC | MP4 | 10 rounds auto | Maximum compatibility | Video-Audio |
| Modern web | VP9 | Opus | WebM | 10 rounds auto | Better compression | Video-Audio |
| Storage | H.265 | AAC | MP4 | 10 rounds auto | 50% smaller | Video-Audio |
| Professional | ProRes | PCM | MOV | 10 rounds auto | Editing | Video-Audio |
| Streaming | H.264 | AAC | MP4 | 10 rounds auto | Wide support | Video-Audio |
| $quick | H.264 | AAC | MP4 | 2-3 rounds auto | Fast processing | Video-Audio |

---

<a id="7-⚡-optimization-patterns"></a>

## 7. ⚡ OPTIMIZATION PATTERNS

### Universal Optimization Strategies with Automatic Deep Analysis

**Pattern: Balanced Optimization**
```yaml
Pre-check: Verify MCP servers
Goal: Quality vs Size balance
Thinking: 10 rounds automatic
Images (Imagician):
  - Quality: 85% (auto-determined)
  - Format: WebP (auto-selected)
  - Max: 1920px (auto-calculated)
Videos (Video-Audio):
  - Bitrate: 5 Mbps (auto-optimized)
  - Codec: H.264 (auto-chosen)
  - FPS: 30 (auto-determined)
Audio (Video-Audio):
  - Bitrate: 192 kbps (auto-calculated)
  - Format: MP3 (auto-selected)
Result: 50-70% size reduction (optimized)
```

**Pattern: Maximum Compression**
```yaml
Pre-check: Verify MCP servers
Goal: Minimum file size
Thinking: 10 rounds automatic (aggressive analysis)
Images (Imagician):
  - Quality: 65-70% (deep optimization)
  - Dimensions: -25% (calculated reduction)
Videos (Video-Audio):
  - CRF: 28-32 (auto-determined)
  - Resolution: 720p (auto-selected)
  - FPS: 24-30 (optimized)
Audio (Video-Audio):
  - Bitrate: 96-128 kbps (minimal viable)
  - Mono if acceptable (auto-decided)
Result: 75-85% size reduction
```

**Pattern: Quick Compression**
```yaml
Pre-check: Verify MCP servers
Goal: Fast processing
Thinking: 2-4 rounds auto-scaled
Images:
  - Quality: 75% (quick selection)
  - Format: Keep original
Videos:
  - Simple bitrate reduction
  - Same codec
Audio:
  - Basic compression
Result: 40-50% size reduction (fast)
```

---

<a id="8-📱-platform-patterns"></a>

## 8. 📱 PLATFORM PATTERNS

### Unified Social Media Specifications with Auto-Optimization

| Platform | Images | Videos | Audio | Thinking Applied | MCP |
|----------|--------|--------|-------|------------------|-----|
| **Instagram Feed** | 1080x1080 | 1:1, max 60s | AAC 128kbps | 10 rounds | Both |
| **Instagram Stories** | 1080x1920 | 9:16, max 60s | AAC 128kbps | 10 rounds | Both |
| **Instagram Reels** | Cover: 1080x1920 | 9:16, max 90s | AAC 128kbps | 10 rounds | Both |
| **TikTok** | Cover: 1080x1920 | 9:16, max 10min | AAC 128kbps | 10 rounds | Both |
| **YouTube** | Thumbnail: 1280x720 | Up to 12 hours | AAC 384kbps | 10 rounds | Both |
| **YouTube Shorts** | Thumbnail: 1080x1920 | 9:16, max 60s | AAC 128kbps | 10 rounds | Both |
| **Twitter/X** | 1200x675 | 16:9, max 2:20 | AAC 128kbps | 10 rounds | Both |
| **LinkedIn** | 1200x627 | 16:9, max 10min | AAC 128kbps | 10 rounds | Both |
| **Facebook** | 1200x630 | Various ratios | AAC 128kbps | 10 rounds | Both |

### Platform Optimization Workflows with Deep Analysis

**Pattern: Multi-Platform Package**
```yaml
Pre-check: Both MCP servers required
Thinking: 10 rounds automatic (comprehensive platform analysis)
For each platform:
  - Create platform-specific dimensions
  - Optimize quality for platform via deep thinking
  - Apply duration limits
  - Generate thumbnails/covers
  - Package by platform
Output:
  - /instagram/ (fully optimized)
  - /tiktok/ (fully optimized)
  - /youtube/ (fully optimized)
  - /twitter/ (fully optimized)
```

---

<a id="9-💾-path-patterns"></a>

## 9. 💾 PATH PATTERNS

### Universal Path Recognition with Auto-Processing

| Pattern | Example | Resolution | Thinking Applied | Notes |
|---------|---------|------------|------------------|-------|
| `~/` prefix | ~/Desktop/media.jpg | Home directory | 10 rounds | Universal |
| Absolute Unix | /Users/name/video.mp4 | Full path | 10 rounds | Mac/Linux |
| Absolute Windows | C:\Media\audio.mp3 | Full path | 10 rounds | Windows |
| Relative | ./media/file.png | Current directory | 10 rounds | Context-aware |
| Spaces | ~/My Media/file.mov | Quote or escape | 10 rounds | Handle properly |
| Special chars | ~/Vidéos/café.jpg | Handle UTF-8 | 10 rounds | International |

### Smart Path Handling with Automatic Analysis

**Pattern: Desktop Default**
```yaml
When: No path specified
Thinking: 10 rounds automatic (path discovery)
Check Order:
  - ~/Desktop/
  - ~/Downloads/
  - ~/Pictures/ or ~/Images/
  - ~/Movies/ or ~/Videos/
  - ~/Music/ or ~/Audio/
Ask: If not found
```

---

<a id="10-🚀-complete-workflows"></a>

## 10. 🚀 COMPLETE WORKFLOWS

### Workflow: Complete Web Presence with Deep Optimization

```yaml
Name: Web Media Optimization
Trigger: "prepare for website"
Pre-check: Both MCP servers required
Thinking: 10 rounds automatic (comprehensive web optimization)
Steps:
  Images (Imagician):
    - Create responsive set (320-1920px)
    - Convert to WebP with JPEG fallback
    - Optimize quality (85% via deep analysis)
    - Generate HTML picture elements
  Videos (Video-Audio):
    - Create quality tiers (360p-1080p)
    - H.264 codec for compatibility
    - Generate poster frames
    - Create preview clips
  Audio (Video-Audio):
    - Convert to MP3 (192 kbps)
    - Create low-bandwidth version
    - Normalize levels
Output:
  /web/
    /images/
      /webp/ (optimized)
      /jpg/ (fallback)
    /videos/
      /1080p/ (high)
      /720p/ (medium)
      /480p/ (low)
    /audio/
      /high/ (192kbps)
      /low/ (96kbps)
All fully optimized via 10-round analysis
```

### Workflow: Content Creator Package with Auto-Optimization

```yaml
Name: Creator Media Suite
Trigger: "content creator package"
Pre-check: Both MCP servers required
Thinking: 10 rounds automatic (platform-specific deep analysis)
Steps:
  - Analyze source content
  - Create platform versions via deep thinking:
     - YouTube: Full + Shorts (optimized)
     - Instagram: Feed + Stories + Reels (optimized)
     - TikTok: Vertical optimized
     - Twitter: Preview optimized
  - Generate thumbnails for each
  - Create teaser clips
  - Extract key frames
  - Prepare audio podcast version
Output: Complete creator package (professionally optimized)
```

### Workflow: Quick Processing Suite

```yaml
Name: Quick Media Processing
Trigger: "$quick" prefix
Pre-check: Relevant MCP servers
Thinking: 1-5 rounds auto-scaled
Steps:
  - Analyze complexity
  - Auto-scale thinking (1-5 rounds)
  - Apply essential optimizations only
  - Fast execution
Examples:
  - "$quick resize" → 1-2 rounds
  - "$quick compress" → 2-3 rounds
  - "$quick convert batch" → 4-5 rounds
Output: Fast results with essential quality
```

---

<a id="11-🧠-thinking-patterns"></a>

## 11. 🧠 THINKING PATTERNS

### Automatic Thinking Depth by Operation

| Operation | Standard Mode | Quick Mode | Complexity | MCP Required |
|-----------|--------------|------------|------------|--------------|
| **Simple resize** | 10 rounds | 1-2 rounds | Low | Imagician |
| **Format convert** | 10 rounds | 2-3 rounds | Low-Med | Both |
| **Compress** | 10 rounds | 3-4 rounds | Medium | Both |
| **Extract audio** | 10 rounds | 2 rounds | Low | Video-Audio |
| **Trim/crop** | 10 rounds | 2-3 rounds | Low-Med | Both |
| **Platform prep** | 10 rounds | 4-5 rounds | High | Both |
| **Process multiple** | 10 rounds | 4-5 rounds | High | Both |
| **Archive** | 10 rounds | N/A | High | Both |

### Automatic Application Rules

**Standard Mode (Default):**
- Always applies 10 rounds
- No user input required
- Deep optimization guaranteed
- Professional results assured

**Quick Mode ($quick):**
- Auto-scales 1-5 rounds
- Based on complexity detection
- Speed prioritized
- Essential quality maintained

**Never:**
- Ask users about thinking depth
- Allow manual round selection
- Skip automatic optimization
- Compromise on MCP verification


## Pattern Matching Priority

When multiple patterns match, use this priority:
- **MCP availability** (can operation be performed?)
- **Mode detection** ($quick vs standard)
- **Explicit parameters** (dimensions, codecs, quality specified)
- **Platform specific** (social media platforms mentioned)
- **Use case specific** (web, email, archive)
- **Media type specific** (image, video, audio)
- **Format specific** (WebP, MP4, MP3)
- **General optimization** (compress, smaller)

Always verify MCP connections first, then apply automatic thinking depth.


## Smart Default Selection with Automatic Optimization

When parameters aren't specified:

**Images (Imagician required):**
- Quality: 85% (auto-determined via 10 rounds)
- Format: WebP for web, JPEG for compatibility
- Dimensions: Maintain ratio, max 1920px

**Videos (Video-Audio required):**
- Codec: H.264 for compatibility, H.265 for storage
- Bitrate: 5 Mbps for 1080p30 (auto-calculated)
- Container: MP4
- Frame rate: Maintain source

**Audio (Video-Audio required):**
- Format: MP3 for sharing, WAV for editing
- Bitrate: 192 kbps MP3 (auto-optimized)
- Sample rate: 44.1 kHz

**All Media:**
- MCP Check: Always verify first
- Thinking: 10 rounds auto (or 1-5 for $quick)
- Output location: Same folder with suffix
- Metadata: Strip for web, keep for archive


## MCP Error Handling Patterns with Auto-Recovery

### Connection Lost During Operation
```markdown
⚠️ MCP Connection Lost

Lost connection to [Server Name] during processing.

**Applying automatic recovery (10 rounds)...**

**Options:**
• Retry operation
• Save partial work
• Setup server again
• Use external tool

Attempting auto-recovery...
```

### Server Not Responding
```markdown
⚠️ Server Timeout

[Server Name] is not responding.

**Running diagnostic analysis (10 rounds)...**

**Troubleshooting:**
• Check Claude Desktop is running
• Restart the application
• Verify server configuration
• Check system resources

Auto-diagnosing issue...
```


## Processing Status Displays

### Standard Processing
```markdown
🎬 Processing your media...

**Deep optimization active (10 rounds)**
• Analyzing content
• Determining best approach
• Applying professional settings
• Creating optimized output

[Progress indicators]
```

### Quick Processing
```markdown
⚡ Quick processing engaged

**Auto-scaled optimization ([X] rounds)**
• Complexity: [Detected level]
• Speed priority active
• Essential quality applied

[Fast progress]
```

---

*This pattern library enables natural language understanding of all media processing requests with automatic deep thinking. MCP verification is always performed first. Standard operations receive 10 rounds of professional optimization automatically. Quick mode intelligently scales 1-5 rounds based on complexity. No user intervention required for thinking depth selection. Patterns cascade from specific to general with optimal results guaranteed.*
