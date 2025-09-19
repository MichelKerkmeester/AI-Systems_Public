# Media Editor - MCP Intelligence - Video, Audio - v0.100

Complete technical reference for the Video-Audio MCP server integration for video and audio processing operations.

## Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [🛠️ CORE OPERATIONS](#2-🛠️-core-operations)
3. [🎬 VIDEO OPERATIONS](#3-🎬-video-operations)
4. [🎵 AUDIO OPERATIONS](#4-🎵-audio-operations)
5. [🎨 ADVANCED FEATURES](#5-🎨-advanced-features)
6. [📊 SUPPORTED FORMATS](#6-📊-supported-formats)
7. [💾 INSTALLATION & SETUP](#7-💾-installation--setup)
8. [⚙️ CONFIGURATION](#8-⚙️-configuration)
9. [🚨 ERROR HANDLING](#9-🚨-error-handling)
10. [⚡ USAGE EXAMPLES](#10-⚡-usage-examples)

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

---

## 2. 🛠️ CORE OPERATIONS

### Available MCP Tools

From the GitHub repository documentation:

| Tool Name | Description | Primary Use |
|-----------|-------------|-------------|
| **health_check** | Returns server running status | System verification |
| **extract_audio_from_video** | Extract audio tracks from video files | Audio separation |
| **trim_video** | Cut video segments with precise timing | Clip creation |
| **convert_video_format** | Convert between video formats | Format compatibility |
| **convert_video_properties** | Comprehensive video property conversion | Full transcoding |
| **change_aspect_ratio** | Adjust video aspect ratios | Platform optimization |
| **set_video_resolution** | Change video resolution | Quality adjustment |
| **set_video_codec** | Switch video codecs | Codec optimization |
| **set_video_bitrate** | Adjust video quality and file size | Size optimization |
| **set_video_frame_rate** | Change playback frame rates | FPS adjustment |
| **convert_audio_format** | Convert between audio formats | Audio compatibility |
| **convert_audio_properties** | Comprehensive audio property conversion | Audio optimization |
| **add_text_overlay** | Add text to videos | Titles/captions |
| **add_image_overlay** | Add image watermarks or logos | Branding |
| **concatenate_videos** | Join multiple videos together | Compilation |
| **add_transition_effect** | Add transitions between clips | Smooth editing |
| **add_subtitle** | Burn subtitles into video | Accessibility |
| **adjust_video_speed** | Speed up or slow down playback | Time effects |
| **fade_in_out** | Add fade effects | Professional polish |
| **insert_broll** | Insert B-roll footage | Content enhancement |
| **remove_silence** | Automatically remove silent portions | Audio cleanup |

---

## 3. 🎬 VIDEO OPERATIONS

### Video Format Conversion

```python
convert_video_format:
  video_path: str           # Input video path
  output_video_path: str    # Output path
  target_format: str        # Target format (mp4, mov, avi, webm, etc.)
```

**Supported Formats:**
- **MP4**: Universal compatibility, H.264/H.265
- **MOV**: QuickTime, ProRes support
- **AVI**: Legacy compatibility
- **WebM**: Web optimization, VP8/VP9
- **MKV**: Container flexibility

### Video Properties Conversion

```python
convert_video_properties:
  input_video_path: str     # Source video
  output_video_path: str    # Output path
  target_format: str        # Optional format change
  resolution: str          # e.g., "1920x1080"
  video_codec: str         # e.g., "libx264"
  audio_codec: str         # e.g., "aac"
  video_bitrate: str       # e.g., "5M"
  audio_bitrate: str       # e.g., "192k"
  frame_rate: int          # e.g., 30
```

### Video Trimming

```python
trim_video:
  video_path: str          # Input video
  output_video_path: str   # Output path
  start_time: str         # Format: "HH:MM:SS" or seconds
  end_time: str           # Format: "HH:MM:SS" or seconds
```

**Time Format Examples:**
- "00:01:30" - 1 minute 30 seconds
- "90" - 90 seconds
- "01:30:00" - 1 hour 30 minutes

### Resolution and Aspect Ratio

```python
set_video_resolution:
  video_path: str
  output_video_path: str
  width: int              # Target width in pixels
  height: int             # Target height in pixels

change_aspect_ratio:
  video_path: str
  output_video_path: str
  aspect_ratio: str       # e.g., "16:9", "4:3", "1:1"
```

**Common Aspect Ratios:**
| Ratio | Use Case | Resolution Examples |
|-------|----------|-------------------|
| 16:9 | Standard video | 1920x1080, 1280x720 |
| 4:3 | Legacy content | 640x480, 800x600 |
| 1:1 | Social media | 1080x1080, 720x720 |
| 9:16 | Vertical video | 1080x1920, 720x1280 |
| 21:9 | Cinematic | 2560x1080, 3440x1440 |

### Video Speed Adjustment

```python
adjust_video_speed:
  video_path: str
  output_video_path: str
  speed_factor: float     # e.g., 0.5 for half speed, 2.0 for double
```

**Speed Guidelines:**
- 0.25x - 0.5x: Slow motion effects
- 0.75x: Slight slowdown
- 1.0x: Normal speed
- 1.25x - 1.5x: Slight speedup
- 2.0x - 4.0x: Time-lapse effect

---

## 4. 🎵 AUDIO OPERATIONS

### Audio Extraction

```python
extract_audio_from_video:
  video_path: str
  output_audio_path: str
  audio_codec: str        # Default: 'mp3' (options: mp3, aac, wav, flac)
```

### Audio Format Conversion

```python
convert_audio_format:
  input_audio_path: str
  output_audio_path: str
  target_format: str      # e.g., 'mp3', 'wav', 'aac', 'flac'
  bitrate: str           # Optional: '128k', '192k', '320k'
  sample_rate: int       # Optional: 44100, 48000
  channels: int          # Optional: 1 (mono), 2 (stereo)
```

### Audio Properties Conversion

```python
convert_audio_properties:
  input_audio_path: str
  output_audio_path: str
  target_format: str
  bitrate: str
  sample_rate: int
  channels: int
```

### Audio Quality Settings

| Bitrate | Quality | Use Case | File Size |
|---------|---------|----------|-----------|
| 96k | Low | Voice only | Smallest |
| 128k | Standard | General audio | Small |
| 192k | Good | Music streaming | Moderate |
| 256k | High | Quality music | Large |
| 320k | Maximum | Archival | Largest |

### Sample Rate Guidelines

| Rate | Use Case | Notes |
|------|----------|-------|
| 22050 Hz | Voice/Speech | Minimal quality |
| 44100 Hz | CD Quality | Standard for music |
| 48000 Hz | Professional | Video production |
| 96000 Hz | High-res audio | Specialized use |

---

## 5. 🎨 ADVANCED FEATURES

### Text Overlay

```python
add_text_overlay:
  video_path: str
  output_video_path: str
  text: str               # Text to display
  position: str          # Position on video
  font_size: int         # Font size in pixels
  font_color: str        # Color (e.g., "white", "#FFFFFF")
  start_time: str        # When to show text
  duration: str          # How long to display
```

**Position Options:**
- top-left, top-center, top-right
- center-left, center, center-right
- bottom-left, bottom-center, bottom-right

### Image Overlay (Watermark)

```python
add_image_overlay:
  video_path: str
  output_video_path: str
  image_path: str        # Watermark/logo path
  position: str          # Position on video
  scale: float           # Size scale factor (0.1 to 1.0)
  start_time: str        # When to show
  duration: str          # How long to show
```

### Video Concatenation

```python
concatenate_videos:
  video_paths: List[str]  # List of videos to join
  output_video_path: str
  transition: str         # Optional transition type
```

**Transition Types:**
- fade - Crossfade between clips
- dissolve - Dissolve transition
- wipe - Wipe effect
- none - Direct cut

### Transitions

```python
add_transition_effect:
  video1_path: str
  video2_path: str
  output_video_path: str
  transition_type: str    # e.g., "fade", "crossfade"
  transition_duration: float  # Duration in seconds
```

### Subtitle Burning

```python
add_subtitle:
  video_path: str
  output_video_path: str
  subtitle_path: str      # SRT or ASS file
  style: dict            # Optional styling parameters
```

**Subtitle Style Options:**
```python
style = {
  'Fontsize': 24,
  'PrimaryColour': '&H00FFFFFF',  # White
  'OutlineColour': '&H00000000',   # Black outline
  'BorderStyle': 1,
  'Outline': 2,
  'Shadow': 0
}
```

### B-Roll Insertion

```python
insert_broll:
  main_video_path: str
  broll_video_path: str
  output_video_path: str
  insert_points: List[str]  # Times to insert B-roll
  broll_duration: float     # Duration of each insert
```

### Silence Removal

```python
remove_silence:
  video_path: str
  output_video_path: str
  silence_threshold: float  # dB threshold (e.g., -30)
  minimum_silence_duration: float  # Seconds (e.g., 0.5)
```

---

## 6. 📊 SUPPORTED FORMATS

### Video Formats
Based on FFmpeg capabilities:

| Container | Extensions | Video Codecs | Audio Codecs | Best For |
|-----------|-----------|--------------|--------------|----------|
| **MP4** | .mp4, .m4v | H.264, H.265 | AAC, MP3 | Universal compatibility |
| **MOV** | .mov, .qt | H.264, ProRes | AAC, PCM | Apple ecosystem |
| **AVI** | .avi | Various | Various | Legacy systems |
| **MKV** | .mkv | Any | Any | Flexibility |
| **WebM** | .webm | VP8, VP9 | Opus, Vorbis | Web streaming |

### Audio Formats

| Format | Extension | Codec | Quality | Use Case |
|--------|-----------|-------|---------|----------|
| **MP3** | .mp3 | MPEG-1 Layer 3 | Lossy | Universal playback |
| **WAV** | .wav | PCM | Lossless | Editing/Production |
| **AAC** | .aac, .m4a | Advanced Audio | Lossy | Modern devices |
| **FLAC** | .flac | Free Lossless | Lossless | Archival |
| **OGG** | .ogg | Vorbis | Lossy | Open source |

### Codec Selection Guide

**Video Codecs:**
- **H.264 (libx264)**: Best compatibility
- **H.265 (libx265)**: 50% smaller files
- **VP9**: Web optimization
- **ProRes**: Professional editing
- **DNxHD**: Broadcast quality

**Audio Codecs:**
- **AAC**: Modern standard
- **MP3**: Universal support
- **PCM**: Uncompressed
- **FLAC**: Lossless compression
- **Opus**: Best for streaming

---

## 7. 💾 INSTALLATION & SETUP

### Prerequisites

**1. Install FFmpeg:**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
# Add to system PATH
```

**2. Install UV (Recommended):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation Methods

**Method 1: UV with Claude Desktop**
```json
{
  "mcpServers": {
    "VideoAudioServer": {
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

**Method 2: Python with Claude Desktop**
```json
{
  "mcpServers": {
    "VideoAudioServer": {
      "command": "python",
      "args": ["/path/to/video-audio-mcp/server.py"]
    }
  }
}
```

### Clone and Setup

```bash
# Clone repository
git clone https://github.com/misbahsy/video-audio-mcp.git
cd video-audio-mcp

# Install dependencies with UV
uv sync

# Or with pip
pip install -r requirements.txt

# Verify FFmpeg
ffmpeg -version
```

---

## 8. ⚙️ CONFIGURATION

### Configuration Locations

- **Claude Desktop Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Claude Desktop Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Cursor**: File → Preferences → Cursor Settings → MCP
- **Windsurf**: IDE-specific configuration

### Environment Variables

```json
{
  "mcpServers": {
    "VideoAudioServer": {
      "command": "uv",
      "args": ["--directory", "/path/to/server", "run", "server.py"],
      "env": {
        "FFMPEG_PATH": "/usr/local/bin/ffmpeg",
        "OUTPUT_DIR": "/path/to/output",
        "TEMP_DIR": "/tmp/video-audio",
        "MAX_FILE_SIZE": "5GB",
        "TIMEOUT": "3600"
      }
    }
  }
}
```

### Performance Tuning

```python
# Optimal FFmpeg settings for different scenarios
settings = {
  'fast_encode': {
    'preset': 'ultrafast',
    'threads': 0  # Use all available
  },
  'balanced': {
    'preset': 'medium',
    'threads': 4
  },
  'best_quality': {
    'preset': 'slow',
    'threads': 2
  }
}
```

---

## 9. 🚨 ERROR HANDLING

### Common Issues

| Issue | Cause | Solution | Fallback |
|-------|-------|----------|----------|
| **FFmpeg not found** | FFmpeg not installed | Install FFmpeg for platform | Use Docker image |
| **Format not supported** | Invalid codec/format | Check FFmpeg codec support | Convert to standard format |
| **File not found** | Wrong path | Verify file path and permissions | Request correct path |
| **Memory error** | Large file processing | Process in segments | Reduce quality settings |
| **Codec error** | Missing codec | Install full FFmpeg | Use alternative codec |
| **Timeout** | Long processing | Increase timeout | Split into smaller operations |

### Error Recovery Strategies

```python
async def process_with_fallback(operation):
    try:
        return await video_audio_mcp.process(operation)
    except Exception as error:
        if 'memory' in str(error).lower():
            # Reduce quality for memory issues
            operation['video_bitrate'] = '2M'
            operation['resolution'] = '1280x720'
            return await video_audio_mcp.process(operation)
        
        if 'codec' in str(error).lower():
            # Fallback to standard codec
            operation['video_codec'] = 'libx264'
            operation['audio_codec'] = 'aac'
            return await video_audio_mcp.process(operation)
        
        raise error
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

## 10. ⚡ USAGE EXAMPLES

### Example Prompts for Media Editor

**Video Processing:**
```
"Extract audio from video.mp4 and save as MP3"
"Trim video from 1:30 to 5:45"
"Convert movie.avi to MP4 with H.264"
"Resize video to 1920x1080"
"Add 'Sample Text' overlay at top center"
"Speed up video by 2x"
```

**Audio Processing:**
```
"Convert podcast.wav to MP3 192kbps"
"Extract audio from presentation.mp4"
"Change audio to mono 44100Hz"
"Normalize audio levels"
```

**Advanced Operations:**
```
"Join intro.mp4, main.mp4, and outro.mp4 with fade transitions"
"Add subtitles.srt to video"
"Insert b-roll.mp4 at 2:00 in main video"
"Remove silence from lecture.mp4"
"Add company logo watermark to bottom right"
```

### Workflow Example

```python
# Complete video production workflow
async def produce_final_video(raw_footage):
    # 1. Extract and process audio
    audio = await extract_audio_from_video(raw_footage)
    audio_cleaned = await remove_silence(audio)
    
    # 2. Trim to desired length
    trimmed = await trim_video(raw_footage, "00:00:30", "00:05:30")
    
    # 3. Add text overlays
    with_title = await add_text_overlay(trimmed, "Product Demo", 
                                       position="top-center",
                                       duration="5")
    
    # 4. Insert B-roll
    with_broll = await insert_broll(with_title, broll_path,
                                   insert_points=["00:01:00", "00:03:00"])
    
    # 5. Add transitions
    final_clips = await add_transitions(clips, transition_type="fade")
    
    # 6. Add watermark
    with_watermark = await add_image_overlay(final_clips, logo_path,
                                            position="bottom-right",
                                            scale=0.15)
    
    # 7. Burn subtitles
    with_subtitles = await add_subtitle(with_watermark, subtitle_path)
    
    # 8. Export in multiple formats
    await export_formats(with_subtitles, ['mp4', 'webm'])
```

### Integration with Media Editor

When integrated with the Media Editor system:

1. Media Editor receives natural language request
2. Identifies video/audio operation needed
3. Routes to Video-Audio MCP
4. Applies smart defaults based on use case
5. Executes operation with FFmpeg
6. Returns processed media with metrics

Example conversation:
```
User: "Make this video Instagram-ready"
Media Editor: [Detects video, Instagram target]
→ Video-Audio MCP: Change aspect ratio to 1:1
→ Video-Audio MCP: Trim to 60 seconds max
→ Video-Audio MCP: Add subtitles for silent viewing
→ Result: Instagram-optimized video ready
```

---

## Performance Notes

- Uses FFmpeg for all operations
- Supports hardware acceleration where available
- Handles large files through FFmpeg's streaming
- Python-based server for cross-platform compatibility
- Multi-threaded processing support

### Performance Benchmarks

| Operation | Small (<100MB) | Medium (100MB-1GB) | Large (>1GB) |
|-----------|---------------|-------------------|--------------|
| Trim | 1-5s | 5-20s | 20-60s |
| Convert | 5-15s | 30-120s | 2-10min |
| Compress | 10-30s | 60-300s | 5-20min |
| Add overlay | 5-20s | 20-60s | 1-5min |
| Concatenate | 10-30s | 30-90s | 2-10min |

---

*This intelligence document reflects the actual Video-Audio MCP server implementation as documented in the GitHub repository. All operations are powered by FFmpeg for professional-grade media processing.*