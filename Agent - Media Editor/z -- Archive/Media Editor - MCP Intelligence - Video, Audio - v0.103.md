# Media Editor - MCP Intelligence - Video, Audio - v0.103

Complete technical reference for the Video-Audio MCP server integration for video and audio processing operations with automatic deep thinking.

## Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [🔌 CONNECTION VERIFICATION](#2-🔌-connection-verification)
3. [🛠️ CORE OPERATIONS](#3-🛠️-core-operations)
4. [🎬 VIDEO OPERATIONS](#4-🎬-video-operations)
5. [🎵 AUDIO OPERATIONS](#5-🎵-audio-operations)
6. [🎨 ADVANCED FEATURES](#6-🎨-advanced-features)
7. [📊 SUPPORTED FORMATS](#7-📊-supported-formats)
8. [💾 INSTALLATION & SETUP](#8-💾-installation--setup)
9. [⚙️ CONFIGURATION](#9-⚙️-configuration)
10. [🚨 ERROR HANDLING](#10-🚨-error-handling)
11. [⚡ USAGE EXAMPLES](#11-⚡-usage-examples)

---

## 1. 📋 OVERVIEW

### MCP Server Details
- **Name**: Video-Audio MCP Server
- **Package**: @misbahsy/video-audio-mcp
- **Repository**: https://github.com/misbahsy/video-audio-mcp
- **Engine**: FFmpeg (comprehensive media framework)
- **Protocol**: Model Context Protocol (MCP)
- **Language**: Python
- **Installation**: UV (recommended) or Python pip
- **Thinking**: Automatic 10-round deep analysis (standard), 1-5 auto-scaled (quick mode)

### Core Capabilities
Based on the actual GitHub documentation:
- Professional video format conversion and codec changes
- Audio extraction and format conversion
- Video trimming with precise timing control
- Text overlays and image watermarks
- Subtitle burning and management
- Video concatenation with transitions
- Speed adjustment and aspect ratio changes
- Silence removal and audio processing
- B-roll insertion capabilities

### Integration with Media Editor
Video-Audio MCP serves as the video and audio processing engine within the Media Editor system, complementing Imagician's image processing capabilities.

**CRITICAL**: Always verify connection before operations.
**AUTOMATIC**: All operations use 10 rounds of deep thinking (no user choice).

---

## 2. 🔌 CONNECTION VERIFICATION

### Initial Connection Check

**Required Before Any Operation:**
```python
async def verify_video_audio_connection():
    """Check if Video-Audio MCP server is connected"""
    
    try:
        # Test with health_check tool
        result = await video_audio_mcp.health_check()
        return {
            'connected': True,
            'status': 'ready',
            'message': 'Video-Audio MCP connected and ready',
            'ffmpeg': result.get('ffmpeg_version', 'unknown'),
            'thinking': '10 rounds automatic'
        }
    except Exception as e:
        return {
            'connected': False,
            'status': 'error',
            'message': str(e),
            'action': 'setup_required'
        }
```

### Connection Status Displays

**Connected:**
```markdown
✅ Video-Audio MCP Connected

Media processing available:
• Video conversion and transcoding
• Audio extraction and processing
• Trimming, overlays, subtitles
• FFmpeg version: [version]
• **Deep analysis: 10 rounds automatic**
```

**Not Connected:**
```markdown
❌ Video-Audio MCP Not Connected

Video/audio processing unavailable.

**To enable:**
• Install FFmpeg on your system
• Clone video-audio-mcp repository
• Install with UV: uv sync
• Configure Claude Desktop
• Restart application

Need setup help?
```

### Dependency Check Pattern
```python
def check_dependencies():
    """Verify all dependencies are available"""
    checks = {
        'connection': test_mcp_connection(),
        'ffmpeg': verify_ffmpeg_installed(),
        'python': check_python_version(),
        'permissions': check_file_permissions(),
        'temp_dir': verify_temp_directory(),
        'thinking_mode': 'automatic_10_rounds'
    }
    return all(checks.values())
```

### FFmpeg Verification
```markdown
🔧 FFmpeg Status Check

**FFmpeg:** [Installed/Not Found]
**Version:** [version info]
**Codecs:** [available codecs count]
**Path:** [installation path]
**Optimization:** 10-round automatic

[If not installed: Installation instructions]
```

---

## 3. 🛠️ CORE OPERATIONS

### Available MCP Tools with Automatic Thinking

From the GitHub repository documentation:

| Tool Name | Description | Primary Use | Thinking Applied |
|-----------|-------------|-------------|------------------|
| **health_check** | Returns server running status | System verification | 10 rounds auto |
| **extract_audio_from_video** | Extract audio tracks from video files | Audio separation | 10 rounds auto |
| **trim_video** | Cut video segments with precise timing | Clip creation | 10 rounds auto |
| **convert_video_format** | Convert between video formats | Format compatibility | 10 rounds auto |
| **convert_video_properties** | Comprehensive video property conversion | Full transcoding | 10 rounds auto |
| **change_aspect_ratio** | Adjust video aspect ratios | Platform optimization | 10 rounds auto |
| **set_video_resolution** | Change video resolution | Quality adjustment | 10 rounds auto |
| **set_video_codec** | Switch video codecs | Codec optimization | 10 rounds auto |
| **set_video_bitrate** | Adjust video quality and file size | Size optimization | 10 rounds auto |
| **set_video_frame_rate** | Change playback frame rates | FPS adjustment | 10 rounds auto |
| **convert_audio_format** | Convert between audio formats | Audio compatibility | 10 rounds auto |
| **convert_audio_properties** | Comprehensive audio property conversion | Audio optimization | 10 rounds auto |
| **add_text_overlay** | Add text to videos | Titles/captions | 10 rounds auto |
| **add_image_overlay** | Add image watermarks or logos | Branding | 10 rounds auto |
| **concatenate_videos** | Join multiple videos together | Compilation | 10 rounds auto |
| **add_transition_effect** | Add transitions between clips | Smooth editing | 10 rounds auto |
| **add_subtitle** | Burn subtitles into video | Accessibility | 10 rounds auto |
| **adjust_video_speed** | Speed up or slow down playback | Time effects | 10 rounds auto |
| **fade_in_out** | Add fade effects | Professional polish | 10 rounds auto |
| **insert_broll** | Insert B-roll footage | Content enhancement | 10 rounds auto |
| **remove_silence** | Automatically remove silent portions | Audio cleanup | 10 rounds auto |

---

## 4. 🎬 VIDEO OPERATIONS

### Video Format Conversion with Deep Analysis

```python
convert_video_format:
  video_path: str           # Input video path
  output_video_path: str    # Output path
  target_format: str        # Target format (mp4, mov, avi, webm, etc.)
  thinking_rounds: 10       # Automatic optimization
```

**Supported Formats (Auto-Optimized):**
- **MP4**: Universal compatibility, H.264/H.265 (10 rounds analysis)
- **MOV**: QuickTime, ProRes support (10 rounds analysis)
- **AVI**: Legacy compatibility (10 rounds analysis)
- **WebM**: Web optimization, VP8/VP9 (10 rounds analysis)
- **MKV**: Container flexibility (10 rounds analysis)

### Video Properties Conversion with Automatic Optimization

```python
convert_video_properties:
  input_video_path: str     # Source video
  output_video_path: str    # Output path
  target_format: str        # Optional format change
  resolution: str          # e.g., "1920x1080" (auto-optimized)
  video_codec: str         # e.g., "libx264" (auto-selected)
  audio_codec: str         # e.g., "aac" (auto-selected)
  video_bitrate: str       # e.g., "5M" (auto-calculated)
  audio_bitrate: str       # e.g., "192k" (auto-calculated)
  frame_rate: int          # e.g., 30 (auto-determined)
  thinking_applied: 10     # Automatic deep analysis
```

### Video Trimming with Intelligent Analysis

```python
trim_video:
  video_path: str          # Input video
  output_video_path: str   # Output path
  start_time: str         # Format: "HH:MM:SS" or seconds
  end_time: str           # Format: "HH:MM:SS" or seconds
  auto_optimization: True  # 10 rounds applied
```

**Time Format Examples (Auto-Validated):**
- "00:01:30" - 1 minute 30 seconds
- "90" - 90 seconds
- "01:30:00" - 1 hour 30 minutes

### Resolution and Aspect Ratio with Deep Thinking

```python
set_video_resolution:
  video_path: str
  output_video_path: str
  width: int              # Target width (auto-optimized)
  height: int             # Target height (auto-optimized)
  thinking: 10            # Automatic application

change_aspect_ratio:
  video_path: str
  output_video_path: str
  aspect_ratio: str       # e.g., "16:9", "4:3", "1:1"
  auto_analysis: True     # 10 rounds optimization
```

**Common Aspect Ratios (Auto-Selected):**
| Ratio | Use Case | Resolution Examples | Auto-Optimized |
|-------|----------|-------------------|----------------|
| 16:9 | Standard video | 1920x1080, 1280x720 | 10 rounds |
| 4:3 | Legacy content | 640x480, 800x600 | 10 rounds |
| 1:1 | Social media | 1080x1080, 720x720 | 10 rounds |
| 9:16 | Vertical video | 1080x1920, 720x1280 | 10 rounds |
| 21:9 | Cinematic | 2560x1080, 3440x1440 | 10 rounds |

### Video Speed Adjustment with Automatic Analysis

```python
adjust_video_speed:
  video_path: str
  output_video_path: str
  speed_factor: float     # Auto-determined via deep analysis
  thinking_rounds: 10     # Automatic
```

**Speed Guidelines (Auto-Applied):**
- 0.25x - 0.5x: Slow motion effects (10 rounds analysis)
- 0.75x: Slight slowdown (10 rounds analysis)
- 1.0x: Normal speed (10 rounds analysis)
- 1.25x - 1.5x: Slight speedup (10 rounds analysis)
- 2.0x - 4.0x: Time-lapse effect (10 rounds analysis)

---

## 5. 🎵 AUDIO OPERATIONS

### Audio Extraction with Deep Optimization

```python
extract_audio_from_video:
  video_path: str
  output_audio_path: str
  audio_codec: str        # Auto-selected via 10 rounds
  thinking_applied: 10    # Automatic optimization
```

### Audio Format Conversion with Automatic Analysis

```python
convert_audio_format:
  input_audio_path: str
  output_audio_path: str
  target_format: str      # Auto-optimized
  bitrate: str           # Auto-calculated via deep thinking
  sample_rate: int       # Auto-determined
  channels: int          # Auto-selected
  thinking_rounds: 10    # Automatic
```

### Audio Properties Conversion with Deep Thinking

```python
convert_audio_properties:
  input_audio_path: str
  output_audio_path: str
  target_format: str      # Auto-selected
  bitrate: str           # Auto-optimized via 10 rounds
  sample_rate: int       # Auto-determined
  channels: int          # Auto-selected
  auto_analysis: True    # 10 rounds applied
```

### Audio Quality Settings (Auto-Applied)

| Bitrate | Quality | Use Case | File Size | Auto-Selected When |
|---------|---------|----------|-----------|-------------------|
| 96k | Low | Voice only | Smallest | Voice detected |
| 128k | Standard | General audio | Small | Standard use |
| 192k | Good | Music streaming | Moderate | Music detected |
| 256k | High | Quality music | Large | High quality need |
| 320k | Maximum | Archival | Largest | Archive mode |

### Sample Rate Guidelines (Auto-Determined)

| Rate | Use Case | Notes | Thinking Applied |
|------|----------|-------|------------------|
| 22050 Hz | Voice/Speech | Minimal quality | 10 rounds |
| 44100 Hz | CD Quality | Standard for music | 10 rounds |
| 48000 Hz | Professional | Video production | 10 rounds |
| 96000 Hz | High-res audio | Specialized use | 10 rounds |

---

## 6. 🎨 ADVANCED FEATURES

### Text Overlay with Intelligent Positioning

```python
add_text_overlay:
  video_path: str
  output_video_path: str
  text: str               # Text to display
  position: str          # Auto-positioned via 10 rounds
  font_size: int         # Auto-sized via deep analysis
  font_color: str        # Auto-selected for visibility
  start_time: str        # When to show text
  duration: str          # How long to display
  thinking_applied: 10   # Automatic optimization
```

**Position Options (Auto-Selected):**
- top-left, top-center, top-right
- center-left, center, center-right
- bottom-left, bottom-center, bottom-right
- All positions optimized via 10-round analysis

### Image Overlay (Watermark) with Auto-Optimization

```python
add_image_overlay:
  video_path: str
  output_video_path: str
  image_path: str        # Watermark/logo path
  position: str          # Auto-positioned for best visibility
  scale: float           # Auto-scaled via 10 rounds
  start_time: str        # When to show
  duration: str          # How long to show
  auto_optimized: True   # 10 rounds applied
```

### Video Concatenation with Automatic Transitions

```python
concatenate_videos:
  video_paths: List[str]  # List of videos to join
  output_video_path: str
  transition: str         # Auto-selected via deep analysis
  thinking_rounds: 10     # Automatic optimization
```

**Transition Types (Auto-Selected):**
- fade - Crossfade between clips (10 rounds optimization)
- dissolve - Dissolve transition (10 rounds optimization)
- wipe - Wipe effect (10 rounds optimization)
- none - Direct cut (when appropriate)

### Transitions with Deep Analysis

```python
add_transition_effect:
  video1_path: str
  video2_path: str
  output_video_path: str
  transition_type: str    # Auto-selected via 10 rounds
  transition_duration: float  # Auto-calculated
  thinking_applied: 10    # Automatic
```

### Subtitle Burning with Intelligent Styling

```python
add_subtitle:
  video_path: str
  output_video_path: str
  subtitle_path: str      # SRT or ASS file
  style: dict            # Auto-styled via 10 rounds
  auto_optimization: True # Deep thinking applied
```

**Subtitle Style Options (Auto-Optimized):**
```python
style = {
  'Fontsize': 24,        # Auto-sized via analysis
  'PrimaryColour': '&H00FFFFFF',  # Auto-selected
  'OutlineColour': '&H00000000',   # Auto-contrasted
  'BorderStyle': 1,      # Auto-determined
  'Outline': 2,          # Auto-calculated
  'Shadow': 0            # Auto-applied
}
```

### B-Roll Insertion with Automatic Timing

```python
insert_broll:
  main_video_path: str
  broll_video_path: str
  output_video_path: str
  insert_points: List[str]  # Auto-calculated via 10 rounds
  broll_duration: float     # Auto-optimized
  thinking_rounds: 10       # Automatic
```

### Silence Removal with Intelligent Detection

```python
remove_silence:
  video_path: str
  output_video_path: str
  silence_threshold: float  # Auto-calculated via deep analysis
  minimum_silence_duration: float  # Auto-determined
  auto_optimized: True     # 10 rounds applied
```

---

## 7. 📊 SUPPORTED FORMATS

### Video Formats with Automatic Optimization
Based on FFmpeg capabilities:

| Container | Extensions | Video Codecs | Audio Codecs | Best For | Auto-Optimized |
|-----------|-----------|--------------|--------------|----------|----------------|
| **MP4** | .mp4, .m4v | H.264, H.265 | AAC, MP3 | Universal compatibility | 10 rounds |
| **MOV** | .mov, .qt | H.264, ProRes | AAC, PCM | Apple ecosystem | 10 rounds |
| **AVI** | .avi | Various | Various | Legacy systems | 10 rounds |
| **MKV** | .mkv | Any | Any | Flexibility | 10 rounds |
| **WebM** | .webm | VP8, VP9 | Opus, Vorbis | Web streaming | 10 rounds |

### Audio Formats with Deep Analysis

| Format | Extension | Codec | Quality | Use Case | Auto-Selected |
|--------|-----------|-------|---------|----------|---------------|
| **MP3** | .mp3 | MPEG-1 Layer 3 | Lossy | Universal playback | 10 rounds |
| **WAV** | .wav | PCM | Lossless | Editing/Production | 10 rounds |
| **AAC** | .aac, .m4a | Advanced Audio | Lossy | Modern devices | 10 rounds |
| **FLAC** | .flac | Free Lossless | Lossless | Archival | 10 rounds |
| **OGG** | .ogg | Vorbis | Lossy | Open source | 10 rounds |

### Codec Selection Guide (Automatic via Deep Thinking)

**Video Codecs (Auto-Selected):**
- **H.264 (libx264)**: Best compatibility (10 rounds analysis)
- **H.265 (libx265)**: 50% smaller files (10 rounds analysis)
- **VP9**: Web optimization (10 rounds analysis)
- **ProRes**: Professional editing (10 rounds analysis)
- **DNxHD**: Broadcast quality (10 rounds analysis)

**Audio Codecs (Auto-Selected):**
- **AAC**: Modern standard (10 rounds analysis)
- **MP3**: Universal support (10 rounds analysis)
- **PCM**: Uncompressed (10 rounds analysis)
- **FLAC**: Lossless compression (10 rounds analysis)
- **Opus**: Best for streaming (10 rounds analysis)

---

## 8. 🚨 ERROR HANDLING

### Common Issues with Automatic Recovery

| Issue | Cause | Solution | Fallback | Thinking Applied |
|-------|-------|----------|----------|------------------|
| **Connection lost** | Server crashed | Restart MCP server | Check setup | Auto-retry with 10 rounds |
| **FFmpeg not found** | FFmpeg not installed | Install FFmpeg for platform | Use Docker image | Auto-diagnose |
| **Format not supported** | Invalid codec/format | Check FFmpeg codec support | Convert to standard | Auto-convert via deep analysis |
| **File not found** | Wrong path | Verify file path and permissions | Request correct path | Path analysis via thinking |
| **Memory error** | Large file processing | Process in segments | Reduce quality settings | Auto-segment with optimization |
| **Codec error** | Missing codec | Install full FFmpeg | Use alternative codec | Auto-select alternative |
| **Timeout** | Long processing | Increase timeout | Split into smaller operations | Auto-split via deep analysis |

### Error Recovery Strategies with Deep Thinking

```python
async def process_with_fallback(operation, mode='standard'):
    # Check connection first
    connection = await verify_video_audio_connection()
    if not connection['connected']:
        return {
            'error': 'Video-Audio MCP not connected',
            'action': 'Please setup the MCP server',
            'guide': 'See installation instructions'
        }
    
    # Apply automatic thinking
    thinking_rounds = 10 if mode == 'standard' else auto_scale(1, 5)
    
    try:
        return await video_audio_mcp.process(operation, {'thinking': thinking_rounds})
    except Exception as error:
        # Auto-recovery with deep analysis
        if 'memory' in str(error).lower():
            # Reduce quality for memory issues (10 rounds analysis)
            operation['video_bitrate'] = '2M'
            operation['resolution'] = '1280x720'
            return await video_audio_mcp.process(operation)
        
        if 'codec' in str(error).lower():
            # Fallback to standard codec (10 rounds)
            operation['video_codec'] = 'libx264'
            operation['audio_codec'] = 'aac'
            return await video_audio_mcp.process(operation)
        
        raise error
```

### Error Display Format
```markdown
⚠️ Media Processing Error

**Issue:** [Error description]
**Server:** Video-Audio MCP
**FFmpeg:** [Status]
**Connection:** [Status]
**Auto-recovery:** Applying 10 rounds of analysis...

**Solutions:**
• [Primary solution]
• [Alternative approach]
• [Fallback option]

Attempting automatic resolution...
```

### Debugging

```bash
# Test FFmpeg installation
ffmpeg -version
ffmpeg -codecs
ffmpeg -formats

# Test server directly
python server.py

# Check Python dependencies
pip list | grep mcp
```

---

## 9. ⚡ USAGE EXAMPLES

### Example Prompts with Automatic Deep Thinking

**Video Processing (10 rounds auto):**
```
"Extract audio from video.mp4 and save as MP3"
→ System applies 10 rounds automatically
→ Optimal codec and bitrate selected
→ No user input needed

"Trim video from 1:30 to 5:45"
→ Deep analysis for lossless trim
→ Smart re-encoding if needed

"Convert movie.avi to MP4 with H.264"
→ 10 rounds determine best settings
→ Automatic quality/size balance
```

**Audio Processing (10 rounds auto):**
```
"Convert podcast.wav to MP3"
→ Bitrate auto-optimized to 192kbps
→ Sample rate intelligently preserved

"Extract audio from presentation.mp4"
→ Format auto-selected based on content
→ Quality maximized automatically
```

**Advanced Operations (10 rounds deep analysis):**
```
"Join intro.mp4, main.mp4, and outro.mp4"
→ Transitions auto-selected
→ Encoding parameters unified
→ Seamless output created

"Add subtitles.srt to video"
→ Style auto-optimized for readability
→ Position and size calculated

"Remove silence from lecture.mp4"
→ Threshold auto-detected
→ Natural pacing preserved
```

### Workflow Example with Automatic Thinking

```python
# Complete video production workflow
async def produce_final_video(raw_footage, mode='standard'):
    # 0. Verify connection
    connection = await verify_video_audio_connection()
    if not connection['connected']:
        raise Exception("Video-Audio MCP not connected. Please setup.")
    
    # Automatic deep thinking applied throughout
    thinking = 10 if mode == 'standard' else auto_scale(1, 5)
    
    # 1. Extract and process audio (10 rounds optimization)
    audio = await extract_audio_from_video(raw_footage)
    audio_cleaned = await remove_silence(audio)  # Threshold auto-calculated
    
    # 2. Trim to desired length (10 rounds for precision)
    trimmed = await trim_video(raw_footage, "00:00:30", "00:05:30")
    
    # 3. Add text overlays (position/size auto-optimized)
    with_title = await add_text_overlay(trimmed, "Product Demo", 
                                       position="auto",  # 10 rounds determine best
                                       duration="5")
    
    # 4. Insert B-roll (timing auto-calculated)
    with_broll = await insert_broll(with_title, broll_path,
                                   insert_points="auto")  # 10 rounds optimize
    
    # 5. Add transitions (type auto-selected)
    final_clips = await add_transitions(clips, transition_type="auto")
    
    # 6. Add watermark (scale/position auto-determined)
    with_watermark = await add_image_overlay(final_clips, logo_path,
                                            position="auto",
                                            scale="auto")
    
    # 7. Burn subtitles (style auto-optimized)
    with_subtitles = await add_subtitle(with_watermark, subtitle_path)
    
    # 8. Export in multiple formats (settings auto-optimized)
    await export_formats(with_subtitles, ['mp4', 'webm'])
```

### Integration with Media Editor

When integrated with the Media Editor system:

- Media Editor verifies Video-Audio MCP connection
- Receives natural language request
- **Applies 10 rounds of thinking automatically**
- Routes to Video-Audio MCP
- Executes operation with FFmpeg
- Returns processed media with metrics

Example conversation:
```
User: "Make this video Instagram-ready"
Media Editor: [Checking Video-Audio MCP connection...]
→ Connection verified ✔
→ FFmpeg available ✔
→ Applying deep optimization (10 rounds)...
→ Video-Audio MCP: Change aspect ratio to 1:1
→ Video-Audio MCP: Trim to 60 seconds max
→ Video-Audio MCP: Add subtitles for silent viewing
→ Result: Instagram-optimized video ready
```

### Quick Mode Examples

```
User: "$quick compress video.mp4"
→ Auto-scaling: Video compression = 3 rounds
→ Fast bitrate reduction applied
→ 60% size reduction in half the time

User: "$quick extract audio from presentation.mp4"
→ Auto-scaling: Simple extraction = 2 rounds
→ Direct stream copy when possible
→ Completed in seconds
```

## Performance Notes

- Uses FFmpeg for all operations
- Supports hardware acceleration where available
- Handles large files through FFmpeg's streaming
- Python-based server for cross-platform compatibility
- Multi-threaded processing support
- **All operations enhanced by automatic deep thinking**

### Performance Benchmarks with Thinking Applied

| Operation | Small (<100MB) | Medium (100MB-1GB) | Large (>1GB) | Thinking Overhead |
|-----------|---------------|-------------------|--------------|-------------------|
| Trim | 1-5s | 5-20s | 20-60s | +20ms |
| Convert | 5-15s | 30-120s | 2-10min | +25ms |
| Compress | 10-30s | 60-300s | 5-20min | +30ms |
| Add overlay | 5-20s | 20-60s | 1-5min | +20ms |
| Concatenate | 10-30s | 30-90s | 2-10min | +25ms |

### Performance Status Display
```markdown
📊 Video-Audio MCP Performance

**Connection:** Active
**FFmpeg:** Running
**CPU Usage:** 45%
**Memory:** 512MB
**Queue:** 1 operation
**Progress:** 67%
**Thinking mode:** 10 rounds automatic
**Processing:** Optimized with deep analysis

Operating at peak efficiency
```

### Quick Mode Performance
```markdown
⚡ Quick Mode Performance

**Connection:** Active
**FFmpeg:** Running
**Thinking:** 3 rounds (auto-scaled)
**Speed boost:** 40-60% faster
**Quality:** Essential optimization only

Fast processing engaged
```

---

*This intelligence document reflects the actual Video-Audio MCP server implementation with automatic deep thinking. Connection verification is mandatory. All operations receive 10 rounds of optimization automatically in standard mode, or 1-5 auto-scaled rounds in quick mode. FFmpeg powers all operations with professional-grade results, no user intervention required for thinking depth selection.*
