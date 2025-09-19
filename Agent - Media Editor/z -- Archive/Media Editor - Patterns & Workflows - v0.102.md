# Media Editor - Patterns & Workflows - v0.102

Complete pattern library and workflow specifications for natural language media processing operations (images, video, and audio) with native Claude thinking integration.

## Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [📌 MCP VERIFICATION PATTERNS](#2-📌-mcp-verification-patterns)
3. [🎯 INTENT PATTERNS](#3-🎯-intent-patterns)
4. [🔄 WORKFLOW PATTERNS](#4-🔄-workflow-patterns)
5. [📐 DIMENSION & RESOLUTION PATTERNS](#5-📐-dimension--resolution-patterns)
6. [🎨 FORMAT & CODEC PATTERNS](#6-🎨-format--codec-patterns)
7. [⚡ OPTIMIZATION PATTERNS](#7-⚡-optimization-patterns)
8. [📱 PLATFORM PATTERNS](#8-📱-platform-patterns)
9. [💾 PATH PATTERNS](#9-💾-path-patterns)
10. [🚀 COMPLETE WORKFLOWS](#10-🚀-complete-workflows)
11. [🧠 THINKING PATTERNS](#11-🧠-thinking-patterns)

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the Media Editor with native Claude thinking. Each pattern maps natural language to specific operations with smart defaults and appropriate thinking depth across images, video, and audio.

**Critical Requirements:**
• **MCP Verification First**: Always check server connections before operations
• **Visual Consistency**: Use clean bullet lists throughout (NO DIVIDERS)
• **Pattern Adaptability**: All patterns flexible based on user preference
• **Clean Formatting**: Present information without decorative elements

**Pattern Categories:**
• **Connection Verification**: MCP server availability checks
• **Intent Recognition**: What the user wants to achieve
• **Parameter Extraction**: Dimensions, quality, formats, codecs, bitrates
• **Workflow Selection**: Single vs multi-step operations
• **Platform Optimization**: Target-specific settings
• **Thinking Depth**: Native Claude thinking rounds
• **Media Detection**: Automatic file type recognition

**Integration Points:**
• MCP verification → Natural language → Pattern matching → MCP operation
• Thinking rounds → Processing depth → Quality outcome
• Platform detection → Preset application → Optimized output

## 2. 📌 MCP VERIFICATION PATTERNS

### Initial Connection Check Pattern

**Pattern: Verify Before Processing**
```yaml
Trigger: Any media operation request
Priority: ALWAYS FIRST
Steps:
  • Check Imagician connection
  • Check Video-Audio connection
  • Report status
  • Guide if not connected
```

### Connection Status Displays

**All Connected:**
```markdown
✅ MCP Servers Ready

• Imagician: Connected
• Video-Audio: Connected

All media operations available.
```

**Partial Connection:**
```markdown
⚠️ Partial MCP Connection

• Imagician: ✅ Connected
• Video-Audio: ❌ Not connected

Available: Image processing only
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

| User Request | Required MCP | Fallback if Unavailable |
|-------------|--------------|------------------------|
| "Resize image" | Imagician | Provide setup guide |
| "Convert video" | Video-Audio | Provide setup guide |
| "Extract audio" | Video-Audio | Provide setup guide |
| "Compress photo" | Imagician | Provide setup guide |
| "Add watermark" | Video-Audio | Provide setup guide |
| "Batch images" | Imagician | Provide setup guide |

## 3. 🎯 INTENT PATTERNS

### Universal Compression Intents

| User Says | Media Type | Default Action | Thinking Depth | Parameters |
|-----------|------------|---------------|----------------|------------|
| "make smaller" | Auto-detect | 50% reduction | Ask user (2-6) | Smart settings |
| "reduce size" | Auto-detect | Quality/size balance | Ask user (2-6) | Maintain quality |
| "compress" | Auto-detect | Format-specific | Standard (4-6) | Optimal compression |
| "shrink" | Auto-detect | 75% of original | Quick (2-3) | Basic reduction |
| "too big" | Auto-detect | Smart reduce | Standard (4-6) | Context-aware |
| "email size" | Auto-detect | Email limits | Standard (4-6) | Under 5MB/25MB |
| "web size" | Auto-detect | Web optimize | Standard (4-6) | Fast loading |

### Format Conversion Intents

| User Says | Target | Quality | Thinking Depth | MCP Required |
|-----------|--------|---------|----------------|--------------|
| **Images:** |
| "to jpg/jpeg" | JPEG | 90% | Quick (2-3) | Imagician |
| "to png" | PNG | Lossless | Quick (2-3) | Imagician |
| "to webp" | WebP | 85% | Standard (4-6) | Imagician |
| **Video:** |
| "to mp4" | MP4 | Maintain | Quick (2-3) | Video-Audio |
| "to mov" | MOV | Maintain | Quick (2-3) | Video-Audio |
| "to webm" | WebM | VP9 | Standard (4-6) | Video-Audio |
| **Audio:** |
| "to mp3" | MP3 | 192 kbps | Quick (2-3) | Video-Audio |
| "to wav" | WAV | Lossless | Quick (2-3) | Video-Audio |
| "to aac" | AAC | 128 kbps | Quick (2-3) | Video-Audio |

## 4. 🔄 WORKFLOW PATTERNS

### Pre-Workflow Verification

**Pattern: MCP Check First**
```yaml
Every Workflow:
  • Verify required MCP servers
  • If not connected:
     - Explain limitation
     - Offer setup help
  • If connected:
     - Proceed with workflow
```

### Single-Step Workflows

**Pattern: Universal Format Convert**
```yaml
Trigger: Format name mentioned
Pre-check: Verify MCP connection
Thinking: Ask user (default: Quick 2-3)
Steps:
  • Detect source media type
  • Select appropriate converter
  • Apply optimal settings
  • Convert and save
Example: "convert to webp" → WebP at 85% (image)
Example: "convert to mp4" → MP4 with H.264 (video)
```

**Pattern: Smart Compress**
```yaml
Trigger: "compress", "smaller"
Pre-check: Verify MCP connection
Thinking: Ask user (default: Standard 4-6)
Steps:
  • Analyze media type and size
  • Calculate target size/quality
  • Apply appropriate compression
  • Verify quality maintained
Example: Image → 85% JPEG/WebP
Example: Video → CRF 23-28 H.264
```

### Multi-Step Workflows

**Pattern: Universal Web Optimization**
```yaml
Trigger: "for website", "web", "online"
Pre-check: Verify all MCP servers
Thinking: Ask user (default: Standard 4-6)
Steps:
  Images (Imagician):
    • Resize to max 1920px
    • Convert to WebP
    • Set quality to 85%
    • Enable progressive
  Videos (Video-Audio):
    • Resize to 1080p max
    • H.264 codec
    • 5 Mbps bitrate
    • Web-optimized container
  Audio (Video-Audio):
    • Convert to MP3
    • 192 kbps bitrate
    • Normalize levels
Result: Web-ready media
```

**Pattern: Social Media Suite**
```yaml
Trigger: Platform name mentioned
Pre-check: Verify both MCP servers
Thinking: Ask user (default: Thorough 7+)
Steps:
  • Identify media type
  • Apply platform dimensions
  • Optimize quality/size
  • Create platform versions
  • Generate thumbnails
Result: Platform-optimized package
```

## 5. 📐 DIMENSION & RESOLUTION PATTERNS

### Universal Dimension Recognition

| Pattern | Interpretation | Example | Result | Thinking | MCP |
|---------|---------------|---------|--------|----------|-----|
| `{number}px` | Width in pixels | "800px" | 800 pixels wide | Quick (2-3) | Imagician |
| `{width}x{height}` | Exact dimensions | "1920x1080" | Full HD | Quick (2-3) | Both |
| `{height}p` | Video resolution | "1080p" | 1920x1080 | Quick (2-3) | Video-Audio |
| `{number}%` | Percentage | "50%" | Half size | Quick (2-3) | Both |
| `4K/8K/HD` | Standard sizes | "4K" | 3840x2160 | Standard (4-6) | Both |
| `{ratio}` | Aspect ratio | "16:9" | Maintain ratio | Standard (4-6) | Both |

### Common Media Dimensions

| Use Case | Images | Videos | Thinking | MCP Required |
|----------|--------|--------|----------|--------------|
| **Web Hero** | 1920x1080 | 1920x1080 | Standard (4-6) | Both |
| **Thumbnail** | 150x150 | 320x180 | Quick (2-3) | Both |
| **Mobile** | 640x960 | 720x1280 | Standard (4-6) | Both |
| **Social Square** | 1080x1080 | 1080x1080 | Standard (4-6) | Both |
| **Social Vertical** | 1080x1920 | 1080x1920 | Standard (4-6) | Both |
| **Email Max** | 1024x768 | 1280x720 | Standard (4-6) | Both |

### Responsive Set Patterns

**Pattern: Image Responsive Set**
```yaml
Pre-check: Imagician connected
Thinking: Ask user (recommend: Thorough 7+)
Sizes:
  • 320px (mobile)
  • 640px (tablet)
  • 1024px (desktop)
  • 1920px (full)
  • 150px (thumbnail)
Formats: WebP with JPEG fallback
```

## 6. 🎨 FORMAT & CODEC PATTERNS

### Format Selection Logic

| Condition | Image Format | Video Container | Audio Format | Thinking | MCP |
|-----------|-------------|-----------------|--------------|----------|-----|
| Has transparency | PNG/WebP | N/A | N/A | Standard (4-6) | Imagician |
| Photography | JPEG/WebP | MP4 | N/A | Standard (4-6) | Both |
| Web use | WebP | MP4/WebM | MP3 | Standard (4-6) | Both |
| Email | JPEG | MP4 | MP3 | Quick (2-3) | Both |
| Archival | PNG | MOV/MKV | FLAC/WAV | Thorough (7+) | Both |
| Streaming | WebP | MP4 | AAC | Standard (4-6) | Both |
| Professional | RAW/PNG | ProRes | WAV | Thorough (7+) | Both |

### Codec Selection Intelligence

| Intent | Video Codec | Audio Codec | Container | Thinking | Use Case | MCP |
|--------|------------|-------------|-----------|----------|----------|-----|
| Universal | H.264 | AAC | MP4 | Quick (2-3) | Maximum compatibility | Video-Audio |
| Modern web | VP9 | Opus | WebM | Standard (4-6) | Better compression | Video-Audio |
| Storage | H.265 | AAC | MP4 | Standard (4-6) | 50% smaller | Video-Audio |
| Professional | ProRes | PCM | MOV | Thorough (7+) | Editing | Video-Audio |
| Streaming | H.264 | AAC | MP4 | Standard (4-6) | Wide support | Video-Audio |

## 7. ⚡ OPTIMIZATION PATTERNS

### Universal Optimization Strategies

**Pattern: Balanced Optimization**
```yaml
Pre-check: Verify MCP servers
Goal: Quality vs Size balance
Thinking: Standard (4-6)
Images (Imagician):
  • Quality: 85%
  • Format: WebP
  • Max: 1920px
Videos (Video-Audio):
  • Bitrate: 5 Mbps (1080p)
  • Codec: H.264
  • FPS: 30
Audio (Video-Audio):
  • Bitrate: 192 kbps
  • Format: MP3
Result: 50-70% size reduction
```

**Pattern: Maximum Compression**
```yaml
Pre-check: Verify MCP servers
Goal: Minimum file size
Thinking: Thorough (7+)
Images (Imagician):
  • Quality: 65-70%
  • Dimensions: -25%
Videos (Video-Audio):
  • CRF: 28-32
  • Resolution: 720p
  • FPS: 24-30
Audio (Video-Audio):
  • Bitrate: 96-128 kbps
  • Mono if acceptable
Result: 75-85% size reduction
```

## 8. 📱 PLATFORM PATTERNS

### Unified Social Media Specifications

| Platform | Images | Videos | Audio | Thinking | MCP |
|----------|--------|--------|-------|----------|-----|
| **Instagram Feed** | 1080x1080 | 1:1, max 60s | AAC 128kbps | Standard | Both |
| **Instagram Stories** | 1080x1920 | 9:16, max 60s | AAC 128kbps | Standard | Both |
| **Instagram Reels** | Cover: 1080x1920 | 9:16, max 90s | AAC 128kbps | Standard | Both |
| **TikTok** | Cover: 1080x1920 | 9:16, max 10min | AAC 128kbps | Standard | Both |
| **YouTube** | Thumbnail: 1280x720 | Up to 12 hours | AAC 384kbps | Thorough | Both |
| **YouTube Shorts** | Thumbnail: 1080x1920 | 9:16, max 60s | AAC 128kbps | Standard | Both |
| **Twitter/X** | 1200x675 | 16:9, max 2:20 | AAC 128kbps | Standard | Both |
| **LinkedIn** | 1200x627 | 16:9, max 10min | AAC 128kbps | Standard | Both |
| **Facebook** | 1200x630 | Various ratios | AAC 128kbps | Standard | Both |

### Platform Optimization Workflows

**Pattern: Multi-Platform Package**
```yaml
Pre-check: Both MCP servers required
Thinking: Ask user (recommend: Thorough 7+)
For each platform:
  • Create platform-specific dimensions
  • Optimize quality for platform
  • Apply duration limits
  • Generate thumbnails/covers
  • Package by platform
Output:
  • /instagram/
  • /tiktok/
  • /youtube/
  • /twitter/
```

## 9. 💾 PATH PATTERNS

### Universal Path Recognition

| Pattern | Example | Resolution | Thinking | Notes |
|---------|---------|------------|----------|-------|
| `~/` prefix | ~/Desktop/media.jpg | Home directory | Quick | Universal |
| Absolute Unix | /Users/name/video.mp4 | Full path | Quick | Mac/Linux |
| Absolute Windows | C:\Media\audio.mp3 | Full path | Quick | Windows |
| Relative | ./media/file.png | Current directory | Quick | Context-aware |
| Spaces | ~/My Media/file.mov | Quote or escape | Quick | Handle properly |
| Special chars | ~/Vidéos/café.jpg | Handle UTF-8 | Standard | International |

### Smart Path Handling

**Pattern: Desktop Default**
```yaml
When: No path specified
Thinking: Not needed (discovery)
Check Order:
  • ~/Desktop/
  • ~/Downloads/
  • ~/Pictures/ or ~/Images/
  • ~/Movies/ or ~/Videos/
  • ~/Music/ or ~/Audio/
Ask: If not found
```

## 10. 🚀 COMPLETE WORKFLOWS

### Workflow: Complete Web Presence

```yaml
Name: Web Media Optimization
Trigger: "prepare for website"
Pre-check: Both MCP servers required
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  Images (Imagician):
    • Create responsive set (320-1920px)
    • Convert to WebP with JPEG fallback
    • Optimize quality (85%)
    • Generate HTML picture elements
  Videos (Video-Audio):
    • Create quality tiers (360p-1080p)
    • H.264 codec for compatibility
    • Generate poster frames
    • Create preview clips
  Audio (Video-Audio):
    • Convert to MP3 (192 kbps)
    • Create low-bandwidth version
    • Normalize levels
Output:
  /web/
    /images/
      /webp/
      /jpg/
    /videos/
      /1080p/
      /720p/
      /480p/
    /audio/
      /high/
      /low/
```

### Workflow: Content Creator Package

```yaml
Name: Creator Media Suite
Trigger: "content creator package"
Pre-check: Both MCP servers required
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  • Analyze source content
  • Create platform versions:
     - YouTube: Full + Shorts
     - Instagram: Feed + Stories + Reels
     - TikTok: Vertical optimized
     - Twitter: Preview optimized
  • Generate thumbnails for each
  • Create teaser clips
  • Extract key frames
  • Prepare audio podcast version
Output: Complete creator package
```

## 11. 🧠 THINKING PATTERNS

### Thinking Depth by Operation

| Operation | Quick (2-3) | Standard (4-6) | Thorough (7+) | MCP Required |
|-----------|-------------|-----------------|---------------|--------------|
| **Simple resize** | ✓ Default | If quality critical | For multiple files | Imagician |
| **Format convert** | ✓ Default | Multiple formats | Complex requirements | Both |
| **Compress** | Basic | ✓ Default | Per-file optimization | Both |
| **Extract audio** | ✓ Default | With processing | Enhancement suite | Video-Audio |
| **Trim/crop** | ✓ Default | Smart crop | Face detection | Both |
| **Platform prep** | Single | ✓ Default | Multiple platforms | Both |
| **Process multiple** | Same settings | ✓ Default | Individual optimization | Both |
| **Archive** | Basic | Standard quality | ✓ Default (lossless) | Both |

### When to Ask About Thinking

**Always Ask:**
• After MCP verification
• Before any execution
• When ready to process
• After gathering all info
• Before creating output

**Never Ask:**
• During MCP check
• During discovery phase
• When gathering paths
• While identifying media type
• In error messages (offer retry with different depth)

## Pattern Matching Priority

When multiple patterns match, use this priority:
• **MCP availability** (can operation be performed?)
• **Explicit parameters** (dimensions, codecs, quality specified)
• **Platform specific** (social media platforms mentioned)
• **Use case specific** (web, email, archive)
• **Media type specific** (image, video, audio)
• **Format specific** (WebP, MP4, MP3)
• **General optimization** (compress, smaller)

Always verify MCP connections first, then ask about thinking depth before execution unless in discovery phase.

## Smart Default Selection

When parameters aren't specified:

**Images (Imagician required):**
• Quality: 85% (sweet spot)
• Format: WebP for web, JPEG for compatibility
• Dimensions: Maintain ratio, max 1920px

**Videos (Video-Audio required):**
• Codec: H.264 for compatibility, H.265 for storage
• Bitrate: 5 Mbps for 1080p30
• Container: MP4
• Frame rate: Maintain source

**Audio (Video-Audio required):**
• Format: MP3 for sharing, WAV for editing
• Bitrate: 192 kbps MP3
• Sample rate: 44.1 kHz

**All Media:**
• MCP Check: Always verify first
• Thinking: Ask user, suggest based on complexity
• Output location: Same folder with suffix
• Metadata: Strip for web, keep for archive

## MCP Error Handling Patterns

### Connection Lost During Operation
```markdown
⚠️ MCP Connection Lost

Lost connection to [Server Name] during processing.

**Options:**
• Retry operation
• Save partial work
• Setup server again
• Use external tool

What would you prefer?
```

### Server Not Responding
```markdown
⚠️ Server Timeout

[Server Name] is not responding.

**Troubleshooting:**
• Check Claude Desktop is running
• Restart the application
• Verify server configuration
• Check system resources

Need help troubleshooting?
```

*This pattern library enables natural language understanding of all media processing requests with native Claude thinking. MCP verification is always performed first. Patterns cascade from specific to general, with thinking depth adapted to operation complexity and media type. No dividers are used, only clean bullet lists for information display.*