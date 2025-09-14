# Media Editor - Patterns & Workflows - v0.101

Complete pattern library and workflow specifications for natural language media processing operations (images, video, and audio) with native Claude thinking integration.

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

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the Media Editor with native Claude thinking. Each pattern maps natural language to specific operations with smart defaults and appropriate thinking depth across images, video, and audio.

**Critical Requirements:**
- **MCP Verification First**: Always check server connections before operations
- **Visual Consistency**: Use standardized dividers throughout
- **Pattern Adaptability**: All patterns flexible based on user preference

**Pattern Categories:**
- **Connection Verification**: MCP server availability checks
- **Intent Recognition**: What the user wants to achieve
- **Parameter Extraction**: Dimensions, quality, formats, codecs, bitrates
- **Workflow Selection**: Single vs multi-step operations
- **Platform Optimization**: Target-specific settings
- **Thinking Depth**: Native Claude thinking rounds
- **Media Detection**: Automatic file type recognition

**Integration Points:**
- MCP verification → Natural language → Pattern matching → MCP operation
- Thinking rounds → Processing depth → Quality outcome
- Platform detection → Preset application → Optimized output

---

## 2. 🔌 MCP VERIFICATION PATTERNS

### Initial Connection Check Pattern

**Pattern: Verify Before Processing**
```yaml
Trigger: Any media operation request
Priority: ALWAYS FIRST
Steps:
  1. Check Imagician connection
  2. Check Video-Audio connection
  3. Report status
  4. Guide if not connected
```

### Connection Status Displays

**All Connected:**
```markdown
✅ MCP Servers Ready
─────────────────
• Imagician: Connected
• Video-Audio: Connected

All media operations available.
```

**Partial Connection:**
```markdown
⚠️ Partial MCP Connection
─────────────────
• Imagician: ✅ Connected
• Video-Audio: ❌ Not connected

Available: Image processing only
Unavailable: Video/audio operations

Continue with images or setup video/audio?
```

**No Connection:**
```markdown
❌ MCP Setup Required
─────────────────
No media processing servers connected.

To enable:
1. Install MCP servers
2. Configure Claude Desktop
3. Restart application

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

---

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

### Quality Optimization Intents

| User Says | Quality Target | Size Priority | Thinking Depth | Use Case |
|-----------|---------------|---------------|----------------|----------|
| "best quality" | 95-100% | Low | Thorough (7+) | Archival |
| "balanced" | 85-90% | Medium | Standard (4-6) | General use |
| "compress more" | 75-85% | High | Standard (4-6) | Web/email |
| "maximum compression" | 60-75% | Maximum | Thorough (7+) | Bandwidth limited |
| "lossless" | 100% | None | Quick (2-3) | Preservation |

### Media-Specific Operation Intents

| User Says | Operation | Media | Thinking Depth | MCP Server | Output |
|-----------|-----------|-------|----------------|------------|--------|
| "extract audio" | Extract | Video | Quick (2-3) | Video-Audio | Audio file |
| "remove audio" | Mute | Video | Quick (2-3) | Video-Audio | Silent video |
| "add subtitles" | Subtitle | Video | Standard (4-6) | Video-Audio | Subtitled video |
| "create thumbnail" | Extract frame | Video | Quick (2-3) | Video-Audio | Image |
| "add watermark" | Overlay | Image/Video | Standard (4-6) | Video-Audio | Watermarked media |
| "normalize volume" | Normalize | Audio | Standard (4-6) | Video-Audio | Consistent audio |

---

## 4. 🔄 WORKFLOW PATTERNS

### Pre-Workflow Verification

**Pattern: MCP Check First**
```yaml
Every Workflow:
  1. Verify required MCP servers
  2. If not connected:
     - Explain limitation
     - Offer setup help
  3. If connected:
     - Proceed with workflow
```

### Single-Step Workflows

**Pattern: Universal Format Convert**
```yaml
Trigger: Format name mentioned
Pre-check: Verify MCP connection
Thinking: Ask user (default: Quick 2-3)
Steps:
  1. Detect source media type
  2. Select appropriate converter
  3. Apply optimal settings
  4. Convert and save
Example: "convert to webp" → WebP at 85% (image)
Example: "convert to mp4" → MP4 with H.264 (video)
```

**Pattern: Smart Compress**
```yaml
Trigger: "compress", "smaller"
Pre-check: Verify MCP connection
Thinking: Ask user (default: Standard 4-6)
Steps:
  1. Analyze media type and size
  2. Calculate target size/quality
  3. Apply appropriate compression
  4. Verify quality maintained
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
    1. Resize to max 1920px
    2. Convert to WebP
    3. Set quality to 85%
    4. Enable progressive
  Videos (Video-Audio):
    1. Resize to 1080p max
    2. H.264 codec
    3. 5 Mbps bitrate
    4. Web-optimized container
  Audio (Video-Audio):
    1. Convert to MP3
    2. 192 kbps bitrate
    3. Normalize levels
Result: Web-ready media
```

**Pattern: Email Preparation**
```yaml
Trigger: "email", "attach", "send"
Pre-check: Verify MCP connection
Thinking: Ask user (default: Standard 4-6)
Steps:
  Images (Imagician):
    1. Resize to max 1024px
    2. JPEG format
    3. Under 5MB total
  Videos (Video-Audio):
    1. Compress to under 25MB
    2. 720p resolution
    3. Lower bitrate
  Mixed:
    1. Apply limits per type
    2. Create zip if needed
Result: Email-ready attachments
```

**Pattern: Social Media Suite**
```yaml
Trigger: Platform name mentioned
Pre-check: Verify both MCP servers
Thinking: Ask user (default: Thorough 7+)
Steps:
  1. Identify media type
  2. Apply platform dimensions
  3. Optimize quality/size
  4. Create platform versions
  5. Generate thumbnails
Result: Platform-optimized package
```

---

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
  - 320px (mobile)
  - 640px (tablet)
  - 1024px (desktop)
  - 1920px (full)
  - 150px (thumbnail)
Formats: WebP with JPEG fallback
```

**Pattern: Video Quality Set**
```yaml
Pre-check: Video-Audio connected
Thinking: Ask user (recommend: Thorough 7+)
Qualities:
  - 2160p (4K) - if source supports
  - 1080p (Full HD)
  - 720p (HD)
  - 480p (SD)
  - 360p (Mobile)
Codec: H.264 for compatibility
```

---

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

### Quality Presets by Media Type

| Media | Web | Email | Archive | Thumbnail | Thinking | MCP |
|-------|-----|-------|---------|-----------|----------|-----|
| **Image** | 85% | 80% | Lossless | 75% | Standard | Imagician |
| **Video** | 5 Mbps | 2 Mbps | 25+ Mbps | N/A | Standard | Video-Audio |
| **Audio** | 192 kbps | 128 kbps | Lossless | N/A | Standard | Video-Audio |

---

## 7. ⚡ OPTIMIZATION PATTERNS

### Universal Optimization Strategies

**Pattern: Balanced Optimization**
```yaml
Pre-check: Verify MCP servers
Goal: Quality vs Size balance
Thinking: Standard (4-6)
Images (Imagician):
  - Quality: 85%
  - Format: WebP
  - Max: 1920px
Videos (Video-Audio):
  - Bitrate: 5 Mbps (1080p)
  - Codec: H.264
  - FPS: 30
Audio (Video-Audio):
  - Bitrate: 192 kbps
  - Format: MP3
Result: 50-70% size reduction
```

**Pattern: Maximum Compression**
```yaml
Pre-check: Verify MCP servers
Goal: Minimum file size
Thinking: Thorough (7+)
Images (Imagician):
  - Quality: 65-70%
  - Dimensions: -25%
Videos (Video-Audio):
  - CRF: 28-32
  - Resolution: 720p
  - FPS: 24-30
Audio (Video-Audio):
  - Bitrate: 96-128 kbps
  - Mono if acceptable
Result: 75-85% size reduction
```

### Performance Metrics with Thinking

| Operation | Reduction | Quality Impact | Speed Gain | Thinking | MCP |
|-----------|-----------|----------------|------------|----------|-----|
| Image → WebP | 30-50% | None | 30% faster | Standard | Imagician |
| Video H.264→H.265 | 50% | None if done right | Slower encode | Thorough | Video-Audio |
| Audio WAV→MP3 | 90% | Minimal at 192kbps | Much smaller | Quick | Video-Audio |
| Same settings all files | Varies | Consistent | Fast | Standard | Both |
| Individual optimization | Varies | Per-file optimal | Slower | Thorough | Both |

---

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
  1. Create platform-specific dimensions
  2. Optimize quality for platform
  3. Apply duration limits
  4. Generate thumbnails/covers
  5. Package by platform
Output:
  /instagram/
  /tiktok/
  /youtube/
  /twitter/
```

---

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
  1. ~/Desktop/
  2. ~/Downloads/
  3. ~/Pictures/ or ~/Images/
  4. ~/Movies/ or ~/Videos/
  5. ~/Music/ or ~/Audio/
Ask: If not found
```

**Pattern: Output Organization**
```yaml
Default: Same as input
Organization:
  - By type: /images/, /videos/, /audio/
  - By operation: /compressed/, /converted/
  - By platform: /instagram/, /youtube/
Thinking: Quick (2-3)
Naming: Add operation suffix
```

---

## 10. 🚀 COMPLETE WORKFLOWS

### Workflow: Complete Web Presence

```yaml
Name: Web Media Optimization
Trigger: "prepare for website"
Pre-check: Both MCP servers required
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  Images (Imagician):
    1. Create responsive set (320-1920px)
    2. Convert to WebP with JPEG fallback
    3. Optimize quality (85%)
    4. Generate HTML picture elements
  Videos (Video-Audio):
    1. Create quality tiers (360p-1080p)
    2. H.264 codec for compatibility
    3. Generate poster frames
    4. Create preview clips
  Audio (Video-Audio):
    1. Convert to MP3 (192 kbps)
    2. Create low-bandwidth version
    3. Normalize levels
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
  1. Analyze source content
  2. Create platform versions:
     - YouTube: Full + Shorts
     - Instagram: Feed + Stories + Reels
     - TikTok: Vertical optimized
     - Twitter: Preview optimized
  3. Generate thumbnails for each
  4. Create teaser clips
  5. Extract key frames
  6. Prepare audio podcast version
Output: Complete creator package
```

### Workflow: Professional Archive

```yaml
Name: Master Archive Creation
Trigger: "create archive"
Pre-check: Both MCP servers required
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  Images (Imagician):
    1. Save as PNG/TIFF
    2. Preserve all metadata
    3. Create contact sheet
  Videos (Video-Audio):
    1. ProRes or H.265 lossless
    2. Keep all audio tracks
    3. Preserve subtitles
  Audio (Video-Audio):
    1. FLAC or WAV format
    2. Preserve sample rate
    3. Keep all channels
  All:
    1. Generate checksums
    2. Create catalog file
    3. Package with metadata
Output: Professional archive package
```

### Workflow: Email Campaign Media

```yaml
Name: Email-Ready Media
Trigger: "email campaign"
Pre-check: MCP servers as needed
Thinking: Ask user (recommend: Standard 4-6)
Steps:
  Images (Imagician):
    1. Max 600px width
    2. JPEG format
    3. Under 100KB each
  Videos (Video-Audio):
    1. Create GIF preview
    2. Link to hosted version
    3. Thumbnail generation
  Package:
    1. Total under 5MB
    2. HTML template ready
    3. Alt text included
Output: Email-optimized package
```

---

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
- After MCP verification
- Before any execution
- When ready to process
- After gathering all info
- Before creating output

**Never Ask:**
- During MCP check
- During discovery phase
- When gathering paths
- While identifying media type
- In error messages (offer retry with different depth)

### Thinking Recommendations by Media Mix

| Media Mix | Default | Reasoning | MCP Required |
|-----------|---------|-----------|--------------|
| **Single image** | Quick (2-3) | Simple operation | Imagician |
| **Single video** | Standard (4-6) | Codec decisions | Video-Audio |
| **Single audio** | Quick (2-3) | Direct processing | Video-Audio |
| **Mixed files** | Thorough (7+) | Per-type optimization | Both |
| **Platform package** | Thorough (7+) | Multiple outputs | Both |
| **Archive set** | Thorough (7+) | Quality critical | Both |

### Thinking Recommendations by User Type

| User Type | Default | Reasoning | Applies To |
|-----------|---------|-----------|------------|
| **New user** | Standard (4-6) | Balance of speed and quality | All media |
| **Power user** | Quick (2-3) | They know what they want | All media |
| **Quality focus** | Thorough (7+) | Best results matter | All media |
| **Time sensitive** | Quick (2-3) | Speed priority | All media |
| **Professional** | Thorough (7+) | Quality critical | All media |

---

## Pattern Matching Priority

When multiple patterns match, use this priority:
1. **MCP availability** (can operation be performed?)
2. **Explicit parameters** (dimensions, codecs, quality specified)
3. **Platform specific** (social media platforms mentioned)
4. **Use case specific** (web, email, archive)
5. **Media type specific** (image, video, audio)
6. **Format specific** (WebP, MP4, MP3)
7. **General optimization** (compress, smaller)

Always verify MCP connections first, then ask about thinking depth before execution unless in discovery phase.

---

## Smart Default Selection

When parameters aren't specified:

**Images (Imagician required):**
- Quality: 85% (sweet spot)
- Format: WebP for web, JPEG for compatibility
- Dimensions: Maintain ratio, max 1920px

**Videos (Video-Audio required):**
- Codec: H.264 for compatibility, H.265 for storage
- Bitrate: 5 Mbps for 1080p30
- Container: MP4
- Frame rate: Maintain source

**Audio (Video-Audio required):**
- Format: MP3 for sharing, WAV for editing
- Bitrate: 192 kbps MP3
- Sample rate: 44.1 kHz

**All Media:**
- MCP Check: Always verify first
- Thinking: Ask user, suggest based on complexity
- Output location: Same folder with suffix
- Metadata: Strip for web, keep for archive

---

## MCP Error Handling Patterns

### Connection Lost During Operation
```markdown
⚠️ MCP Connection Lost
─────────────────
Lost connection to [Server Name] during processing.

Options:
• Retry operation
• Save partial work
• Setup server again
• Use external tool

What would you prefer?
```

### Server Not Responding
```markdown
⚠️ Server Timeout
─────────────────
[Server Name] is not responding.

Troubleshooting:
• Check Claude Desktop is running
• Restart the application
• Verify server configuration
• Check system resources

Need help troubleshooting?
```

---

*This pattern library enables natural language understanding of all media processing requests with native Claude thinking. MCP verification is always performed first. Patterns cascade from specific to general, with thinking depth adapted to operation complexity and media type.*