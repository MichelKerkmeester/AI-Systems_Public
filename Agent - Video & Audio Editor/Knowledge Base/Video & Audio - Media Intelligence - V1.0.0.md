# Video Audio - Media Intelligence - v1.0.0

Best practices, optimization strategies, and error handling for intelligent media processing.

## Table of Contents
1. [📋 OVERVIEW](#1--overview)
2. [🎯 OPTIMIZATION STRATEGIES](#2--optimization-strategies)
3. [📊 CODEC INTELLIGENCE](#3--codec-intelligence)
4. [⚖️ QUALITY VS SIZE](#4--quality-vs-size)
5. [🚨 ERROR RECOVERY](#5--error-recovery)
6. [💡 BEST PRACTICES](#6--best-practices)
7. [📱 PLATFORM SPECIFICS](#7--platform-specifics)
8. [🔬 TECHNICAL DETAILS](#8--technical-details)
9. [📈 PERFORMANCE METRICS](#9--performance-metrics)
10. [🎓 EDUCATIONAL INSIGHTS](#10--educational-insights)

---

## 1. 📋 OVERVIEW

This document contains the intelligence layer for making optimal media processing decisions. It provides the knowledge base for automatic codec selection, quality optimization, and error handling for both video and audio processing.

**Core Principles:**
- Quality preservation while minimizing file size
- Codec selection based on content and use case
- Graceful degradation and error recovery
- Educational guidance during processing
- Performance-conscious decisions
- Platform-specific optimization

---

## 2. 🎯 OPTIMIZATION STRATEGIES

### Strategy Selection Matrix

| Goal | Priority | Approach | Typical Result |
|------|----------|----------|----------------|
| **Maximum Quality** | Visual/audio fidelity | Minimal compression, high bitrate | Large files, perfect quality |
| **Balanced** | Quality + Size | Smart codecs, optimal bitrate | 50-70% smaller, great quality |
| **Streaming** | Smooth playback | Adaptive bitrate, buffering | Consistent streaming |
| **Minimum Size** | File size | Maximum compression | 80-90% smaller, acceptable quality |
| **Archival** | Preservation | Lossless/ProRes, metadata kept | Original quality, large files |

### Optimization Decision Tree

```
Start → Analyze Media Type
├─ Video with motion?
│  ├─ High motion → Higher bitrate needed
│  └─ Low motion → Lower bitrate acceptable
├─ Audio importance?
│  ├─ Critical → High bitrate audio (192+ kbps)
│  └─ Background → Standard audio (128 kbps)
├─ Resolution needs?
│  ├─ Must preserve → Keep original
│  └─ Can reduce → Scale to 720p/1080p
└─ Platform target?
   ├─ Streaming → H.264/AAC standard
   └─ Archive → ProRes/PCM lossless
```

### Content-Aware Optimization

**For Action/Sports:**
- Higher bitrate required (8-12 Mbps for 1080p)
- Maintain frame rate (60fps if source)
- Two-pass encoding recommended
- Motion blur considerations

**For Talking Head/Presentations:**
- Lower bitrate acceptable (3-5 Mbps for 1080p)
- Can reduce frame rate (30fps fine)
- Focus on audio quality
- Static background compression

**For Music/Concerts:**
- Prioritize audio bitrate (256+ kbps)
- Preserve dynamic range
- Consider 5.1 surround if available
- Visual can be slightly lower quality

**For Screen Recording:**
- Low motion = low bitrate
- Maintain text sharpness
- Can use lower frame rate (15-30fps)
- Consider lossless for tutorials

---

## 3. 📊 CODEC INTELLIGENCE

### Video Codec Selection Guide

| Codec | Best For | Avoid For | Compression | Compatibility |
|-------|----------|-----------|------------|---------------|
| **H.264** | Universal playback | Archival | Good, mature | Universal |
| **H.265** | Storage, 4K+ | Quick sharing | 50% better than H.264 | Modern devices |
| **VP9** | YouTube, web | Apple devices | Better than H.264 | Browsers |
| **AV1** | Future streaming | Current use | Best compression | Limited |
| **ProRes** | Editing, master | Distribution | Minimal | Professional |

### Audio Codec Selection Guide

| Codec | Best For | Bitrate | Quality | Use Case |
|-------|----------|---------|---------|----------|
| **AAC** | General use | 128-320 kbps | Excellent | Streaming, mobile |
| **MP3** | Compatibility | 128-320 kbps | Good | Podcasts, music |
| **Opus** | Modern web | 32-256 kbps | Best efficiency | WebM, streaming |
| **FLAC** | Archival | Lossless | Perfect | Master audio |
| **AC3** | Surround | 384-640 kbps | Good | Home theater |

### Container Format Matrix

| Container | Video Codecs | Audio Codecs | Use Case |
|-----------|-------------|--------------|----------|
| **MP4** | H.264, H.265 | AAC, MP3 | Universal standard |
| **MOV** | ProRes, H.264 | PCM, AAC | Apple ecosystem |
| **WebM** | VP9, VP8 | Opus, Vorbis | Web streaming |
| **MKV** | Any | Any | Flexible, archival |
| **AVI** | Legacy | Legacy | Avoid for new content |

### Smart Codec Decisions

```yaml
Has Subtitles?
  Yes: MP4 or MKV container
  No: Continue →

Is Streaming?
  Yes: H.264 + AAC in MP4
  No: Continue →

Is Archival?
  Yes: ProRes or H.265 + FLAC
  No: Continue →

Is Web Only?
  Yes: VP9 + Opus in WebM
  No: Default to H.264 + AAC in MP4
```

---

## 4. ⚖️ QUALITY VS SIZE

### Video Bitrate Guidelines

| Resolution | Frame Rate | Low Quality | Standard | High Quality | Archive |
|------------|------------|-------------|----------|--------------|---------|
| **4K (2160p)** | 30fps | 15 Mbps | 25 Mbps | 45 Mbps | 100+ Mbps |
| **4K (2160p)** | 60fps | 25 Mbps | 40 Mbps | 65 Mbps | 150+ Mbps |
| **1080p** | 30fps | 3 Mbps | 5 Mbps | 8 Mbps | 25+ Mbps |
| **1080p** | 60fps | 5 Mbps | 8 Mbps | 12 Mbps | 35+ Mbps |
| **720p** | 30fps | 1.5 Mbps | 2.5 Mbps | 4 Mbps | 10+ Mbps |
| **480p** | 30fps | 0.5 Mbps | 1 Mbps | 2 Mbps | 5+ Mbps |

### Audio Bitrate Guidelines

| Quality Level | Bitrate | Use Case | File Size Impact |
|--------------|---------|----------|------------------|
| **Low** | 64-96 kbps | Voice only | Minimal |
| **Standard** | 128 kbps | General use | ~1MB/min |
| **High** | 192-256 kbps | Music | ~2MB/min |
| **Premium** | 320 kbps | Audiophile | ~2.5MB/min |
| **Lossless** | 1000+ kbps | Archive | ~10MB/min |

### The Golden Rules

**For Video:**
- 5 Mbps for 1080p30 is the sweet spot
- Double bitrate for double frame rate
- Add 50% for high motion content
- H.265 = 50% of H.264 bitrate for same quality

**For Audio:**
- 128 kbps AAC = 192 kbps MP3
- Voice needs only 64-96 kbps
- Music should be 192+ kbps
- Always preserve original for archives

### Size Reduction Strategies

**Progressive Approach:**
1. Try standard bitrate first
2. If still too large, reduce resolution
3. Then reduce frame rate if possible
4. Consider two-pass encoding
5. Last resort: aggressive compression

**Aggressive Approach:**
1. Drop to 720p immediately
2. Reduce frame rate to 30fps
3. Use efficient codec (H.265)
4. Minimize audio bitrate
5. Strip unnecessary tracks

---

## 5. 🚨 ERROR RECOVERY

### Common Errors and Solutions

**File Not Found:**
```yaml
Error: Cannot locate media file
Recovery:
  1. Suggest checking path spelling
  2. Offer common media locations
  3. Provide path examples
  4. Guide to file browser
```

**Codec Not Installed:**
```yaml
Error: Missing codec support
Recovery:
  1. Identify missing codec
  2. Suggest alternative codec
  3. Offer installation guidance
  4. Provide conversion workaround
```

**Insufficient Memory:**
```yaml
Error: Out of memory during processing
Recovery:
  1. Suggest closing other applications
  2. Process in smaller segments
  3. Reduce working resolution
  4. Use disk-based processing
```

**Corrupted Media:**
```yaml
Error: File appears corrupted
Recovery:
  1. Attempt repair with ffmpeg
  2. Try alternative decoder
  3. Extract salvageable portions
  4. Suggest re-download/capture
```

**Duration Limit Exceeded:**
```yaml
Concern: Platform duration limit
Response:
  1. Explain platform limits
  2. Offer splitting options
  3. Suggest highlight creation
  4. Provide trim guidance
```

### Graceful Degradation

**When optimal codec unavailable:**
```
H.265 not supported?
→ Fall back to H.264
→ Adjust bitrate up 50%
→ Maintain similar file size
```

**When resolution too high:**
```
Can't handle 8K video?
→ Process at 4K first
→ Then upscale if needed
→ Or process in tiles
```

**When operation fails:**
```
Conversion failed?
→ Try alternative method
→ Suggest manual steps
→ Provide helpful resources
```

---

## 6. 💡 BEST PRACTICES

### Universal Best Practices

1. **Always keep originals**
   - Never overwrite source files
   - Create processed copies
   - Use clear naming conventions

2. **Two-Pass Encoding**
   - First pass analyzes
   - Second pass optimizes
   - Better quality/size ratio
   - Worth the extra time

3. **Audio Sync**
   - Maintain A/V sync
   - Check after processing
   - Use constant frame rate
   - Avoid variable frame rate for editing

4. **Metadata Handling**
   - Preserve for archives
   - Strip for web distribution
   - Keep copyright info
   - Maintain creation date

5. **Color Space**
   - Rec. 709 for HD
   - Rec. 2020 for 4K HDR
   - sRGB for web
   - Convert when needed

### Streaming-Specific Best Practices

**Adaptive Bitrate:**
- Create multiple qualities
- Let platform handle switching
- Include low bandwidth option
- Test on various connections

**Keyframe Interval:**
```
- Streaming: 2 seconds (60 frames at 30fps)
- Download: 10 seconds (300 frames at 30fps)
- Live: 1 second (30 frames at 30fps)
```

**Buffer Considerations:**
- Smaller segments for live
- Larger segments for VOD
- Consider CDN caching
- Enable fast start

---

## 7. 📱 PLATFORM SPECIFICS

### Streaming Platforms

**YouTube:**
- Recommended: 1080p60, H.264, 8-12 Mbps
- 4K: H.265 or VP9, 35-45 Mbps
- Audio: AAC 128-384 kbps
- Container: MP4
- Max file: 128GB or 12 hours

**Twitch:**
- Max: 1080p60, 6 Mbps
- Recommended: 720p60, 3-4 Mbps
- Audio: AAC 128-160 kbps
- Keyframe: Every 2 seconds
- No B-frames for live

**Vimeo:**
- Accepts: Most formats
- Preferred: H.264 in MP4
- Quality: Higher bitrate than YouTube
- 4K: Supported with Plus/Pro
- HDR: Supported

### Social Media Optimization

**Instagram:**
- Feed: 1:1, max 60 seconds, 30fps
- Stories: 9:16, max 60 seconds
- IGTV: Up to 60 minutes
- Reels: 9:16, max 90 seconds
- Max: 4GB file size

**Twitter/X:**
- Max: 2:20 duration
- Size: 512MB
- Resolution: Up to 1920x1200
- Aspect: 1:2.39 - 2.39:1
- Codecs: H.264 + AAC

**TikTok:**
- Aspect: 9:16 vertical
- Duration: Up to 10 minutes
- Resolution: 1080x1920
- Format: MP4 or MOV
- Size: Up to 287.6MB

**Facebook:**
- Max: 240 minutes
- Size: 10GB
- Resolution: Up to 4K
- Aspect: 9:16 to 16:9
- Best: H.264 + AAC

### Professional Platforms

**For Broadcast:**
- ProRes 422 HQ or DNxHD
- 1080i or 1080p
- Specific frame rates (29.97, 59.94)
- Broadcast safe colors
- Loudness standards (-23 LUFS)

**For Cinema:**
- DCP format
- 2K or 4K resolution
- 24fps or 48fps
- XYZ color space
- Separate audio tracks

---

## 8. 🔬 TECHNICAL DETAILS

### Encoding Parameters

**x264 (H.264) Settings:**
```bash
CRF Values:
- 18-22: Visually lossless
- 23: Default (good quality)
- 24-28: Acceptable quality
- 29+: Lower quality

Presets:
- ultrafast: Real-time encoding
- medium: Balanced (default)
- slow: Better compression
- veryslow: Best compression
```

**x265 (H.265) Settings:**
```bash
CRF Values:
- 20-24: Visually lossless
- 28: Default (good quality)
- 29-32: Acceptable quality
- 33+: Lower quality

Similar presets to x264
50% smaller at same CRF
```

### Audio Processing

**Normalization Types:**
| Type | Use Case | Target | Impact |
|------|----------|--------|--------|
| **Peak** | Prevent clipping | 0 dBFS | Simple, may be quiet |
| **RMS** | Consistent volume | -20 dBFS | Better perceived loudness |
| **LUFS** | Broadcast/streaming | -16 to -23 | Industry standard |
| **Dynamic** | Music | Varies | Preserves dynamics |

### Frame Rate Conversion

**Common Conversions:**
- 60fps → 30fps: Drop every other frame
- 30fps → 24fps: 3:2 pulldown
- 24fps → 30fps: 3:2 pulldown reverse
- Variable → Constant: Re-encode required
- PAL ↔ NTSC: Speed change (4% faster/slower)

### Resolution Scaling

| From → To | Method | Quality | Speed |
|-----------|--------|---------|-------|
| 4K → 1080p | Lanczos | Best | Slow |
| 1080p → 720p | Bicubic | Good | Medium |
| Any → Smaller | Bilinear | Fair | Fast |
| Smaller → Larger | Lanczos | Limited by source | Slow |

---

## 9. 📈 PERFORMANCE METRICS

### Processing Performance Impact

| Operation | Processing Time | Quality Impact | File Size Impact |
|-----------|----------------|----------------|------------------|
| H.264 → H.265 | 2-5x real-time | None if done right | 50% reduction |
| Two-pass encode | 2x single pass | 10-15% better | 20% smaller |
| 4K → 1080p | 0.5-2x real-time | Acceptable | 75% reduction |
| Audio extraction | 0.1x real-time | None | 95% reduction |
| Frame rate halving | 0.5x real-time | Smoother → less smooth | 10-20% reduction |

### File Size Benchmarks

**Typical 1080p30 video (1 minute):**
- ProRes 422: 1.5GB
- H.264 High: 60MB
- H.264 Medium: 35MB
- H.265 Medium: 18MB
- H.264 Low: 15MB

**Typical audio (1 minute):**
- WAV/FLAC: 10MB
- 320 kbps MP3: 2.4MB
- 192 kbps MP3: 1.4MB
- 128 kbps AAC: 1MB
- 64 kbps AAC: 0.5MB

### Bandwidth Requirements

**For Streaming:**
- 4K60: 25-50 Mbps
- 4K30: 15-25 Mbps
- 1080p60: 8-12 Mbps
- 1080p30: 5-8 Mbps
- 720p30: 2.5-4 Mbps
- 480p30: 1-2 Mbps

---

## 10. 🎓 EDUCATIONAL INSIGHTS

### Key Concepts to Teach Users

**Why H.265?**
"H.265 is like H.264's smarter sibling. It achieves the same quality at half the file size by using more advanced compression techniques. The trade-off is it takes longer to encode and needs newer devices to play."

**Bitrate vs Quality:**
"Bitrate is like the bandwidth of quality. Higher bitrate means more data per second, which usually means better quality. But there's a sweet spot: doubling bitrate doesn't double quality."

**Two-Pass Encoding:**
"First pass is like scouting the terrain, second pass is the optimized journey. The encoder learns where to spend its 'quality budget' for best results."

**Frame Rate Reality:**
"Movies use 24fps and look great because of motion blur. Games need 60fps for responsiveness. Video calls work at 15fps. More isn't always better: it depends on content."

**Codec Evolution:**
```
1991: MPEG-1 (VCD quality)
1996: MPEG-2 (DVD/broadcast)
2003: H.264 (HD revolution)
2013: H.265 (4K enabler)
2018: AV1 (future royalty-free)
```

### Common Misconceptions

**"Higher resolution always better"**
- Truth: 720p with high bitrate can look better than 1080p with low bitrate

**"Lossless is necessary"**
- Truth: Visually lossless (CRF 18-22) is indistinguishable for most content

**"60fps for everything"**
- Truth: Only beneficial for sports/gaming; films look unnatural

**"Bigger file = better quality"**
- Truth: Efficient encoding can maintain quality at smaller sizes

**"Converting improves quality"**
- Truth: You can never improve beyond source quality

---

## Quick Decision Matrix

| If You Need... | Use This... | With These Settings... |
|---------------|-------------|------------------------|
| Universal playback | H.264 + AAC | MP4, 5 Mbps, 128 kbps |
| Best compression | H.265 + AAC | MP4, 2.5 Mbps, 128 kbps |
| YouTube upload | H.264 high bitrate | 8-12 Mbps for 1080p |
| Quick sharing | H.264 medium | 3-5 Mbps, single pass |
| Professional edit | ProRes 422 | MOV, preserve everything |
| Web streaming | VP9 + Opus | WebM, adaptive bitrate |
| Archive master | ProRes/H.265 | Highest quality possible |

---

*This intelligence layer ensures every media operation is optimized for its intended use while maintaining the best possible quality.*