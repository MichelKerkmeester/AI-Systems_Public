# Video Audio - Patterns & Workflows - v1.0.0

Complete pattern library and workflow specifications for natural language video and audio processing operations with native Claude thinking integration.

## Table of Contents
1. [📋 OVERVIEW](#1--overview)
2. [🎯 INTENT PATTERNS](#2--intent-patterns)
3. [🔄 WORKFLOW PATTERNS](#3--workflow-patterns)
4. [📐 DIMENSION PATTERNS](#4--dimension-patterns)
5. [🎵 AUDIO PATTERNS](#5--audio-patterns)
6. [⚡ OPTIMIZATION PATTERNS](#6--optimization-patterns)
7. [📱 PLATFORM PATTERNS](#7--platform-patterns)
8. [📦 BATCH PATTERNS](#8--batch-patterns)
9. [💾 PATH PATTERNS](#9--path-patterns)
10. [🚀 COMPLETE WORKFLOWS](#10--complete-workflows)
11. [🧠 THINKING PATTERNS](#11--thinking-patterns)

---

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the Video-Audio agent with native Claude thinking. Each pattern maps natural language to specific operations with smart defaults and appropriate thinking depth.

**Pattern Categories:**
- **Intent Recognition**: What the user wants to achieve
- **Parameter Extraction**: Resolution, bitrate, codec preferences
- **Workflow Selection**: Single vs multi-step operations
- **Platform Optimization**: Target-specific settings
- **Batch Processing**: Multiple file handling
- **Thinking Depth**: Native Claude thinking rounds

---

## 2. 🎯 INTENT PATTERNS

### Compression Intents

| User Says | Intent | Default Action | Thinking Depth | Parameters |
|-----------|--------|---------------|----------------|------------|
| "make smaller" | Compress | 50% reduction | Ask user (2-6) | Smart bitrate |
| "compress video" | Compress | CRF 23-28 | Ask user (2-6) | H.264/H.265 |
| "reduce file size" | Compress | Target 50% | Standard (4-6) | Maintain quality |
| "too big" | Smart reduce | Analyze best method | Standard (4-6) | Context-aware |
| "email size" | Email optimize | Under 25MB | Standard (4-6) | Aggressive |
| "for streaming" | Stream optimize | 5 Mbps 1080p | Standard (4-6) | H.264 + AAC |

### Format Conversion Intents

| User Says | Target Format | Quality | Thinking Depth | Notes |
|-----------|--------------|---------|----------------|-------|
| "to mp4" | MP4 | Maintain | Quick (2-3) | H.264 + AAC |
| "to mov" | MOV | Maintain | Quick (2-3) | QuickTime compatible |
| "to webm" | WebM | VP9 | Standard (4-6) | For web |
| "to avi" | Discourage | N/A | Quick (2-3) | Suggest MP4 |
| "for iPhone" | MP4/HEVC | High | Standard (4-6) | Apple optimized |
| "for editing" | ProRes | Highest | Thorough (7+) | Professional |

### Audio Operation Intents

| User Says | Operation | Output | Thinking Depth | Use Case |
|-----------|-----------|--------|----------------|----------|
| "extract audio" | Extract | MP3/AAC | Quick (2-3) | Standalone audio |
| "remove audio" | Mute | Silent video | Quick (2-3) | Visual only |
| "improve audio" | Enhance | Normalized | Standard (4-6) | Better quality |
| "to mp3" | Convert audio | MP3 | Quick (2-3) | Universal |
| "podcast audio" | Optimize | -16 LUFS | Standard (4-6) | Podcast ready |
| "remove noise" | Denoise | Clean audio | Thorough (7+) | Professional |

### Editing Intents

| User Says | Operation | Parameters | Thinking Depth | Notes |
|-----------|-----------|------------|----------------|-------|
| "trim" / "cut" | Trim | Time range | Quick (2-3) | Preserve quality |
| "first 5 minutes" | Trim start | 0:00-5:00 | Quick (2-3) | Keep beginning |
| "remove last minute" | Trim end | Cut final 60s | Quick (2-3) | Remove ending |
| "speed up" | Change speed | 1.5x-2x | Standard (4-6) | Adjust pitch |
| "slow down" | Change speed | 0.5x-0.75x | Standard (4-6) | Maintain audio |
| "add subtitles" | Subtitle | SRT/VTT | Standard (4-6) | Embedded |

---

## 3. 🔄 WORKFLOW PATTERNS

### Single-Step Workflows

**Pattern: Simple Convert**
```yaml
Trigger: Format name mentioned
Thinking: Ask user (default: Quick 2-3)
Steps:
  1. Detect target format
  2. Select appropriate codec
  3. Maintain quality
  4. Convert and save
Example: "convert to mp4" → MP4 with H.264
```

**Pattern: Quick Compress**
```yaml
Trigger: "compress", "smaller"
Thinking: Ask user (default: Standard 4-6)
Steps:
  1. Analyze current size
  2. Calculate target bitrate
  3. Apply compression
  4. Verify quality
Example: "compress this video" → 50% size reduction
```

### Multi-Step Workflows

**Pattern: Platform Optimization**
```yaml
Trigger: Platform name mentioned
Thinking: Ask user (default: Standard 4-6)
Steps:
  1. Identify platform requirements
  2. Adjust resolution/aspect ratio
  3. Set appropriate bitrate
  4. Apply platform codec
  5. Add platform metadata
Result: Platform-ready video
```

**Pattern: Podcast Preparation**
```yaml
Trigger: "podcast", "audio show"
Thinking: Ask user (default: Standard 4-6)
Steps:
  1. Extract audio track
  2. Normalize to -16 LUFS
  3. Apply EQ for voice
  4. Remove background noise
  5. Export as MP3/AAC
Result: Podcast-ready audio
```

**Pattern: Social Media Suite**
```yaml
Trigger: "all social media"
Thinking: Ask user (default: Thorough 7+)
Steps:
  1. Analyze source aspect ratio
  2. Create platform versions:
     - Instagram: Square + Vertical
     - TikTok: 9:16 vertical
     - YouTube: 16:9 + Shorts
     - Twitter: 16:9 optimized
  3. Optimize each for platform
Result: Complete social media set
```

---

## 4. 📐 DIMENSION PATTERNS

### Resolution Recognition

| Pattern | Interpretation | Example | Result | Thinking |
|---------|---------------|---------|--------|----------|
| `{width}x{height}` | Exact resolution | "1920x1080" | Full HD | Quick (2-3) |
| `{height}p` | Standard resolution | "1080p" | 1920x1080 | Quick (2-3) |
| `4K/8K` | UHD resolutions | "4K" | 3840x2160 | Standard (4-6) |
| `HD/SD` | Quality level | "HD" | 1280x720+ | Quick (2-3) |
| `vertical/portrait` | Aspect change | "vertical" | 9:16 ratio | Standard (4-6) |

### Common Video Resolutions

| Name | Resolution | Aspect | Bitrate (H.264) | Thinking | Use Case |
|------|------------|--------|-----------------|----------|----------|
| **8K** | 7680x4320 | 16:9 | 80-100 Mbps | Thorough (7+) | Future/Cinema |
| **4K UHD** | 3840x2160 | 16:9 | 25-45 Mbps | Standard (4-6) | Premium content |
| **1080p FHD** | 1920x1080 | 16:9 | 5-8 Mbps | Standard (4-6) | Standard HD |
| **720p HD** | 1280x720 | 16:9 | 2.5-4 Mbps | Quick (2-3) | Web standard |
| **480p SD** | 854x480 | 16:9 | 1-2 Mbps | Quick (2-3) | Mobile/Low bandwidth |
| **360p** | 640x360 | 16:9 | 0.5-1 Mbps | Quick (2-3) | Minimal bandwidth |

### Aspect Ratio Patterns

**Pattern: Standard Aspects**
```yaml
Thinking: Ask user (recommend: Standard 4-6)
Ratios:
  - 16:9 (Standard widescreen)
  - 4:3 (Classic TV)
  - 1:1 (Square - Instagram)
  - 9:16 (Vertical - Stories)
  - 21:9 (Ultrawide)
  - 2.39:1 (Cinematic)
```

### Frame Rate Patterns

| Source FPS | Target FPS | Method | Quality Impact | Thinking |
|------------|------------|--------|----------------|----------|
| 60 → 30 | Half | Drop frames | Smoother → normal | Quick (2-3) |
| 30 → 60 | Double | Interpolation | May look artificial | Standard (4-6) |
| 30 → 24 | Film | 3:2 pulldown | Slight judder | Standard (4-6) |
| Variable → Constant | Stabilize | Re-encode | Improved compatibility | Standard (4-6) |

---

## 5. 🎵 AUDIO PATTERNS

### Audio Format Selection

| Condition | Recommended | Bitrate | Thinking | Reason |
|-----------|------------|---------|----------|--------|
| Music quality | FLAC/WAV | Lossless | Thorough (7+) | Perfect quality |
| Music sharing | MP3 320 | 320 kbps | Standard (4-6) | Universal |
| Podcast | MP3/AAC | 128-192 kbps | Standard (4-6) | Voice optimized |
| Streaming | AAC | 128 kbps | Quick (2-3) | Efficient |
| Archival | WAV/FLAC | Lossless | Thorough (7+) | Preservation |
| Voice only | MP3 | 64-96 kbps | Quick (2-3) | Small size |

### Audio Processing Patterns

**Pattern: Podcast Optimization**
```yaml
Goal: Podcast-ready audio
Thinking: Standard (4-6)
Steps:
  - Normalize: -16 LUFS (podcast standard)
  - EQ: Boost voice frequencies
  - Compress: 3:1 ratio
  - Gate: Remove silence
  - Format: MP3 192 kbps
```

**Pattern: Music Mastering**
```yaml
Goal: Professional audio
Thinking: Thorough (7+)
Steps:
  - Normalize: -14 LUFS (streaming)
  - EQ: Balanced frequency
  - Compress: Gentle 2:1
  - Limiter: Prevent clipping
  - Format: FLAC or 320 MP3
```

**Pattern: Voice Enhancement**
```yaml
Goal: Clear speech
Thinking: Standard (4-6)
Steps:
  - Noise reduction
  - De-essing (reduce sibilance)
  - Compression for consistency
  - EQ for presence
  - Normalize levels
```

---

## 6. ⚡ OPTIMIZATION PATTERNS

### Compression Strategies

**Pattern: Balanced Compression**
```yaml
Goal: Quality vs Size balance
Thinking: Standard (4-6)
Video:
  - CRF: 23 (H.264) or 28 (H.265)
  - Preset: medium
  - Two-pass: Optional
Audio:
  - Bitrate: 128 kbps AAC
Result: 50-60% size reduction
```

**Pattern: Maximum Compression**
```yaml
Goal: Minimum file size
Thinking: Thorough (7+)
Video:
  - CRF: 28-32
  - Preset: slow/veryslow
  - Resolution: Reduce 25%
  - Frame rate: Reduce if possible
Audio:
  - Bitrate: 96 kbps
Result: 70-85% size reduction
```

**Pattern: Quality Priority**
```yaml
Goal: Best visual quality
Thinking: Thorough (7+)
Video:
  - CRF: 18-20
  - Preset: slow
  - Two-pass: Yes
Audio:
  - Bitrate: 256+ kbps
Result: Minimal compression
```

### Bitrate Calculation Patterns

| Content Type | Motion Level | Base Bitrate (1080p) | Multiplier | Thinking |
|--------------|--------------|---------------------|------------|----------|
| Talking head | Low | 3 Mbps | 1x | Quick (2-3) |
| Presentation | Minimal | 2 Mbps | 1x | Quick (2-3) |
| Sports | High | 8 Mbps | 1.5x | Standard (4-6) |
| Action | Very high | 10 Mbps | 2x | Standard (4-6) |
| Animation | Medium | 5 Mbps | 1x | Standard (4-6) |
| Nature | Variable | 6 Mbps | 1.2x | Standard (4-6) |

---

## 7. 📱 PLATFORM PATTERNS

### Social Media Specifications

| Platform | Video Specs | Audio Specs | Duration | Thinking |
|----------|------------|-------------|----------|----------|
| **YouTube** | 1080p+, H.264, 8-12 Mbps | AAC 128-384 kbps | Unlimited* | Standard |
| **Instagram Feed** | 1:1, 1080x1080, H.264 | AAC 128 kbps | 60 seconds | Standard |
| **Instagram Stories** | 9:16, 1080x1920 | AAC 128 kbps | 60 seconds | Standard |
| **Instagram Reels** | 9:16, 1080x1920 | AAC 128 kbps | 90 seconds | Standard |
| **TikTok** | 9:16, 1080x1920 | AAC 128 kbps | 10 minutes | Standard |
| **Twitter/X** | 16:9, 1280x720 | AAC 128 kbps | 2:20 | Standard |
| **LinkedIn** | 16:9, 1920x1080 | AAC 128 kbps | 10 minutes | Standard |

### Platform Optimization Workflows

**Pattern: YouTube Upload**
```yaml
Resolution: Up to 4K
Codec: H.264 (or H.265 for 4K+)
Bitrate: 8-12 Mbps (1080p), 35-45 Mbps (4K)
Audio: AAC 384 kbps
Container: MP4
Thinking: Standard (4-6)
Special: HDR metadata if available
```

**Pattern: Instagram Reels**
```yaml
Resolution: 1080x1920 (9:16)
Codec: H.264 baseline
Bitrate: 5 Mbps
Audio: AAC 128 kbps
Duration: Max 90 seconds
Thinking: Standard (4-6)
Special: Loop consideration
```

**Pattern: TikTok Vertical**
```yaml
Resolution: 1080x1920 (9:16)
Codec: H.264
Bitrate: 6-8 Mbps (higher for algorithm)
Audio: AAC 128 kbps
Duration: Up to 10 minutes
Thinking: Standard (4-6)
Special: First 3 seconds crucial
```

---

## 8. 📦 BATCH PATTERNS

### Batch Processing Patterns

**Pattern: Uniform Settings**
```yaml
Trigger: Multiple files + same operation
Thinking: Ask user (recommend: Standard 4-6)
Process:
  - Apply identical settings
  - Maintain folder structure
  - Consistent naming scheme
Example: "compress all videos to 720p"
```

**Pattern: Adaptive Batch**
```yaml
Trigger: "optimize each"
Thinking: Ask user (recommend: Thorough 7+)
Process:
  - Analyze each file
  - Apply optimal settings per file
  - Group similar content
  - Report individual results
Example: "optimize folder for streaming"
```

**Pattern: Platform Set Generation**
```yaml
Trigger: "create all formats"
Thinking: Ask user (recommend: Thorough 7+)
Process:
  - Generate multiple versions
  - Create platform folders
  - Optimize per platform
Output:
  /youtube/video-1080p.mp4
  /instagram/video-square.mp4
  /tiktok/video-vertical.mp4
  /twitter/video-720p.mp4
```

### Batch Naming Conventions

| Pattern | Example | Use Case | Thinking |
|---------|---------|----------|----------|
| `{name}-{resolution}` | video-1080p.mp4 | Resolution variants | Quick |
| `{name}-{platform}` | video-youtube.mp4 | Platform specific | Standard |
| `{name}-{codec}` | video-h265.mp4 | Codec variants | Standard |
| `{name}-compressed` | video-compressed.mp4 | General compression | Standard |
| `{date}-{name}` | 2024-01-video.mp4 | Timestamped | Standard |

---

## 9. 💾 PATH PATTERNS

### Path Recognition (Cross-Platform)

| Pattern | Example | Resolution | Thinking |
|---------|---------|------------|----------|
| `~/` prefix | ~/Movies/video.mp4 | Home directory | Quick |
| Absolute Unix | /Users/name/video.mp4 | Full path | Quick |
| Absolute Windows | C:\Videos\video.mp4 | Full path | Quick |
| Relative | ./videos/video.mp4 | Current directory | Quick |
| Spaces | ~/My Videos/clip.mp4 | Quote or escape | Quick |

### Smart Path Handling

**Pattern: Desktop Default**
```yaml
When: No path specified
Thinking: Not needed (discovery)
Check Order:
  1. ~/Desktop/
  2. ~/Downloads/
  3. ~/Movies/ or ~/Videos/
Ask: If not found
```

**Pattern: Output Location**
```yaml
Default: Same as input
Suffix: Add operation descriptor
Thinking: Quick (2-3)
Options:
  - Same folder with suffix
  - New subfolder by operation
  - Custom location
Examples:
  - video-compressed.mp4
  - /compressed/video.mp4
  - ~/Output/video.mp4
```

---

## 10. 🚀 COMPLETE WORKFLOWS

### Workflow: YouTube Content Creation

```yaml
Name: Complete YouTube Optimization
Trigger: "prepare for YouTube"
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  1. Analyze source (resolution, fps, bitrate)
  2. Optimize for YouTube:
     - 1080p or higher
     - H.264 high profile
     - 8-12 Mbps (1080p)
     - Two-pass encoding
  3. Create additional formats:
     - Thumbnail (1280x720)
     - Shorts version (9:16)
     - Trailer (30-60s)
  4. Audio optimization:
     - Normalize to -14 LUFS
     - AAC 384 kbps
  5. Add metadata
Output:
  /youtube/
    video-main.mp4
    video-short.mp4
    video-trailer.mp4
    thumbnail.jpg
```

### Workflow: Podcast Production

```yaml
Name: Complete Podcast Pipeline
Trigger: "podcast production"
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  1. Extract audio from video
  2. Process audio:
     - Remove noise
     - Normalize to -16 LUFS
     - EQ for voice clarity
     - Compress dynamics
  3. Create formats:
     - MP3 192 kbps (distribution)
     - WAV (archive)
     - M4A (Apple Podcasts)
  4. Generate clips:
     - 1-minute highlights
     - Audiogram videos
  5. Create transcription
Output: Complete podcast package
```

### Workflow: Multi-Platform Social

```yaml
Name: Social Media Distribution
Trigger: "all social platforms"
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  1. Analyze content type
  2. Create versions:
     Instagram:
       - Feed (1:1, 60s)
       - Stories (9:16, 60s)
       - Reels (9:16, 90s)
     TikTok:
       - Main (9:16, full)
       - Teaser (9:16, 15s)
     YouTube:
       - Full (16:9)
       - Shorts (9:16, 60s)
     Twitter:
       - Post (16:9, 2:20)
  3. Optimize each for platform
  4. Add captions where needed
Output: Ready-to-post package
```

### Workflow: Archive Master Creation

```yaml
Name: Professional Archive
Trigger: "create master"
Thinking: Ask user (recommend: Thorough 7+)
Steps:
  1. Analyze source quality
  2. Create preservation copy:
     - ProRes 422 HQ or
     - H.265 lossless
     - Original resolution
     - Original frame rate
  3. Keep all tracks:
     - All audio tracks
     - All subtitle tracks
     - All metadata
  4. Create access copies:
     - H.264 high quality
     - H.264 proxy (low res)
  5. Generate checksums
Output: Complete archive package
```

---

## 11. 🧠 THINKING PATTERNS

### Thinking Depth by Operation

| Operation | Quick (2-3) | Standard (4-6) | Thorough (7+) |
|-----------|-------------|-----------------|---------------|
| **Format convert** | ✓ Default | Complex formats | Multiple outputs |
| **Simple trim** | ✓ Default | With re-encoding | Frame-accurate |
| **Compress** | Basic CRF | ✓ Default | Scene analysis |
| **Extract audio** | ✓ Default | With processing | Enhancement |
| **Platform optimize** | Single | ✓ Default | Multiple platforms |
| **Batch process** | Same settings | ✓ Default | Per-file optimization |
| **Subtitles** | Basic embed | ✓ Default | Multi-language |

### When to Ask About Thinking

**Always Ask:**
- Before any execution
- When ready to process
- After gathering all info
- Before creating output

**Never Ask:**
- During discovery phase
- When gathering paths
- While clarifying intent
- In error messages (offer retry with different depth)

### Thinking Recommendations by Content

| Content Type | Default | Reasoning |
|--------------|---------|-----------|
| **Talking head** | Standard (4-6) | Predictable content |
| **Action/Sports** | Thorough (7+) | Complex motion |
| **Screen recording** | Quick (2-3) | Low complexity |
| **Music video** | Thorough (7+) | Quality critical |
| **Presentation** | Standard (4-6) | Balance needed |
| **Nature/Documentary** | Thorough (7+) | Detail preservation |

### Thinking Recommendations by Goal

| User Goal | Default | Reasoning |
|-----------|---------|-----------|
| **Quick share** | Quick (2-3) | Speed priority |
| **Professional** | Thorough (7+) | Quality critical |
| **Storage** | Standard (4-6) | Balanced approach |
| **Streaming** | Standard (4-6) | Platform requirements |
| **Archive** | Thorough (7+) | Preservation focus |

---

## Pattern Matching Priority

When multiple patterns match, use this priority:
1. **Explicit parameters** (codec, bitrate specified)
2. **Platform specific** (YouTube, TikTok mentioned)
3. **Use case specific** (streaming, email)
4. **Format specific** (MP4, MOV)
5. **General optimization** (compress, smaller)

Always ask about thinking depth before execution unless in discovery phase.

---

## Smart Default Selection

When parameters aren't specified:
- **Codec**: H.264 for compatibility, H.265 for efficiency
- **Bitrate**: 5 Mbps for 1080p30
- **Audio**: AAC 128 kbps
- **Container**: MP4
- **Frame rate**: Maintain source
- **Resolution**: Maintain source unless too large
- **Thinking**: Ask user, suggest based on complexity

---

## Time Range Patterns

### Time Specification Recognition

| Pattern | Example | Interpretation | Thinking |
|---------|---------|---------------|----------|
| `MM:SS` | "5:30" | 5 minutes 30 seconds | Quick |
| `HH:MM:SS` | "1:05:30" | 1 hour 5 min 30 sec | Quick |
| `X to Y` | "5:00 to 10:00" | Range extraction | Quick |
| `first X` | "first 5 minutes" | 0:00 to 5:00 | Quick |
| `last X` | "last minute" | -1:00 to end | Quick |
| `remove X` | "remove 2:00-3:00" | Cut section | Standard |

---

*This pattern library enables natural language understanding of video and audio processing requests with native Claude thinking. Patterns cascade from specific to general, with thinking depth adapted to operation complexity.*