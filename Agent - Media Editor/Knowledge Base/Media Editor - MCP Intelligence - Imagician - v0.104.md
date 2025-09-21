# Media Editor - MCP Intelligence - Imagician - v0.104

Complete technical reference for the Imagician MCP server integration for image processing operations with automatic deep thinking.

## Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [🔌 CONNECTION VERIFICATION](#2-🔌-connection-verification)
3. [🛠️ CORE OPERATIONS](#3-🛠️-core-operations)
4. [📊 SUPPORTED FORMATS](#4-📊-supported-formats)
5. [⚙️ OPERATION DETAILS](#5-⚙️-operation-details)
6. [🎯 QUALITY & COMPRESSION](#6-🎯-quality--compression)
7. [📐 RESIZE & CROP](#7-📐-resize--crop)
8. [🔄 ROTATION & FLIPPING](#8-🔄-rotation--flipping)
9. [🚨 ERROR HANDLING](#9-🚨-error-handling)
10. [⚡ USAGE EXAMPLES](#10-⚡-usage-examples)

---

<a id="1-📋-overview"></a>

## 1. 📋 OVERVIEW

### MCP Server Details
- **Name**: Imagician MCP
- **Package**: @flowy11/imagician
- **Repository**: https://github.com/flowy11/imagician
- **Engine**: Sharp (Node.js image processing library)
- **Protocol**: Model Context Protocol (MCP)
- **Installation**: NPX, NPM, or local Node.js
- **Thinking**: Automatic 10-round deep analysis (standard), 1-5 auto-scaled (quick mode)

### Core Capabilities
Based on the actual implementation, Imagician provides:
- High-performance image resizing with various fit options
- Format conversion between JPEG, PNG, WebP, and AVIF
- Image cropping with precise region control
- Compression and quality optimization
- Rotation and flipping operations
- Metadata extraction and handling
- Batch processing support

### Integration with Media Editor
Imagician serves as the primary image processing engine within the Media Editor system, handling all image-specific operations while Video-Audio MCP handles video and audio processing.

**CRITICAL**: Always verify connection before operations.
**AUTOMATIC**: All operations use 10 rounds of deep thinking (no user choice).

---

<a id="2-🔌-connection-verification"></a>

## 2. 🔌 CONNECTION VERIFICATION

### Initial Connection Check

**Required Before Any Operation:**
```python
async def verify_imagician_connection():
    """Check if Imagician MCP server is connected"""
    
    try:
        # Test with list_images tool
        result = await imagician.list_images(folder="Original")
        return {
            'connected': True,
            'status': 'ready',
            'message': 'Imagician connected and ready',
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
✅ Imagician Connected

Image processing available:
• Resize, crop, rotate
• Format conversion (JPEG, PNG, WebP, AVIF)
• Quality optimization
• Batch processing
• **Deep analysis: 10 rounds automatic**
```

**Not Connected:**
```markdown
❌ Imagician Not Connected

Image processing unavailable.

**To enable:**
• Install: npx -y @flowy11/imagician
• Configure Claude Desktop
• Restart application

Need setup help?
```

### Health Check Pattern
```python
def check_imagician_health():
    """Periodic health check"""
    checks = {
        'connection': test_connection(),
        'folders': verify_folders_exist(),
        'permissions': check_write_permissions(),
        'memory': check_available_memory(),
        'thinking_mode': 'automatic_10_rounds'
    }
    return all(checks.values())
```

---

<a id="3-🛠️-core-operations"></a>

## 3. 🛠️ CORE OPERATIONS

### Available MCP Tools with Automatic Thinking

According to the GitHub documentation, Imagician provides these operations:

| Operation | MCP Tool | Description | Parameters | Thinking Applied |
|-----------|----------|-------------|------------|------------------|
| **Resize** | `resize` | Change image dimensions with fit options | width, height, fit, preserveAspectRatio | 10 rounds auto |
| **Convert** | `convert` | Convert between formats with quality control | format, quality | 10 rounds auto |
| **Crop** | `crop` | Extract specific regions from images | x, y, width, height | 10 rounds auto |
| **Compress** | `compress` | Optimize file size with quality settings | quality, strip, optimize | 10 rounds auto |
| **Rotate** | `rotate` | Rotate images by angle | angle, background | 10 rounds auto |
| **Flip** | `flip` | Flip images horizontally or vertically | direction | 10 rounds auto |
| **Metadata** | `getMetadata` | Extract image information | - | 10 rounds auto |
| **Batch** | `batch` | Process multiple images | operations array | 10 rounds auto |
| **List** | `list_images` | List images in folders | folder | 10 rounds auto |

### Operation Priority with Deep Analysis
When multiple operations are needed, Imagician applies them in optimal order:
- Verify connection
- **Apply 10 rounds of thinking automatically**
- Crop (if needed)
- Resize (if needed)
- Rotate/Flip (if needed)
- Format conversion
- Quality optimization

---

<a id="4-📊-supported-formats"></a>

## 4. 📊 SUPPORTED FORMATS

### Confirmed Format Support with Automatic Optimization

From the documentation:

| Format | Extension | Input | Output | Best For | Transparency | Auto-Optimized |
|--------|-----------|-------|--------|----------|--------------|----------------|
| **JPEG** | .jpg, .jpeg | ✅ | ✅ | Photos, complex images | ❌ | 10 rounds |
| **PNG** | .png | ✅ | ✅ | Graphics, screenshots | ✅ | 10 rounds |
| **WebP** | .webp | ✅ | ✅ | Modern web, balanced | ✅ | 10 rounds |
| **AVIF** | .avif | ✅ | ✅ | Next-gen compression | ✅ | 10 rounds |

### Format Selection Logic with Deep Analysis

```python
def select_output_format(input_format, use_case, mode='standard'):
    # Verify connection first
    if not verify_imagician_connection()['connected']:
        return None, "Imagician not connected"
    
    # Apply automatic thinking
    thinking_rounds = 10 if mode == 'standard' else auto_scale_rounds(1, 5)
    
    # Deep analysis for optimal format
    if use_case == 'web':
        return 'webp'  # Best compression, wide support
    elif use_case == 'email':
        return 'jpeg'  # Universal compatibility
    elif use_case == 'archive':
        return 'png'   # Lossless preservation
    elif use_case == 'modern':
        return 'avif'  # Cutting-edge compression
    else:
        return input_format  # Maintain original
```

---

<a id="5-⚙️-operation-details"></a>

## 5. ⚙️ OPERATION DETAILS

### Resize Operation with Automatic Optimization

```javascript
// Parameters from documentation
resize: {
  inputPath: string,       // Path to input image
  outputPath: string,      // Path to save resized image
  width: number,          // Target width (optional)
  height: number,         // Target height (optional)
  fit: string,            // Fit mode
  preserveAspectRatio: boolean, // Default: true
  thinkingRounds: 10      // Automatic deep analysis
}

// Fit options (auto-selected via 10-round analysis)
fit: 'cover' | 'contain' | 'fill' | 'inside' | 'outside'
```

**Fit Mode Explanations (Auto-Selected):**
- **cover**: Crop to cover both dimensions (may lose edges)
- **contain**: Fit within dimensions (may add padding)
- **fill**: Stretch to exact dimensions (may distort)
- **inside**: Resize to fit inside bounds (preserves ratio)
- **outside**: Resize to fit outside bounds (preserves ratio)

### Convert Operation with Deep Thinking

```javascript
// Parameters from documentation
convert: {
  inputPath: string,      // Path to input image
  outputPath: string,     // Path to save converted image
  format: string,         // Target format
  quality: number,        // 1-100 (auto-optimized via 10 rounds)
  thinkingApplied: 10     // Automatic rounds
}

// Supported formats
format: 'jpeg' | 'png' | 'webp' | 'avif'
```

### Crop Operation with Intelligent Analysis

```javascript
// Extract specific region
crop: {
  inputPath: string,      // Source image
  outputPath: string,     // Output path
  x: number,             // X coordinate (from left)
  y: number,             // Y coordinate (from top)
  width: number,         // Crop width
  height: number,        // Crop height
  autoAnalysis: true     // 10-round optimization
}
```

### Compress Operation with Auto-Optimization

```javascript
compress: {
  inputPath: string,
  outputPath: string,
  quality: number,        // 1-100 (auto-determined via deep thinking)
  strip: boolean,        // Remove metadata (auto-decided)
  optimize: boolean,     // Additional optimization (always true)
  thinkingRounds: 10     // Automatic application
}
```

---

<a id="6-🎯-quality--compression"></a>

## 6. 🎯 QUALITY & COMPRESSION

### Quality Settings with Automatic Deep Analysis

From the implementation with auto-optimization:

| Quality | Use Case | File Size Impact | Visual Impact | Auto-Selected When |
|---------|----------|-----------------|---------------|-------------------|
| **100** | Lossless/Archive | Largest | Perfect | Archive detected |
| **90-95** | High quality prints | Large | Excellent | Print use case |
| **80-89** | Default/Web | Moderate | Very good | Standard operations |
| **70-79** | Good compression | Smaller | Good | Size priority |
| **60-69** | Acceptable quality | Small | Acceptable | Heavy compression |
| **<60** | Heavy compression | Smallest | Visible loss | Extreme size limits |

### Compression Best Practices (Automatically Applied)

**For Photos (10 rounds analysis):**
- JPEG: 80-85% quality
- WebP: 85% quality
- AVIF: 75-80% quality (better algorithm)

**For Graphics (10 rounds analysis):**
- PNG: Lossless (100%)
- WebP: 90-95% quality
- Transparency required: PNG or WebP

**For Web (10 rounds optimization):**
- Primary: WebP at 85%
- Fallback: JPEG at 80%
- Modern: AVIF at 75%

### Smart Compression Algorithm with Deep Thinking

```javascript
async function smartCompress(image, targetUseCase, mode='standard') {
  // Check connection
  if (!await verifyConnection()) {
    throw new Error("Imagician not connected");
  }
  
  // Apply automatic thinking
  const thinkingRounds = mode === 'quick' 
    ? autoScale(1, 5) 
    : 10; // Standard: always 10 rounds
  
  const settings = {
    'web': { quality: 85, format: 'webp' },
    'email': { quality: 80, format: 'jpeg' },
    'social': { quality: 90, format: 'jpeg' },
    'archive': { quality: 100, format: 'png' }
  };
  
  // Deep analysis applied automatically
  return optimizeWithThinking(settings[targetUseCase], thinkingRounds);
}
```

---

<a id="7-📐-resize--crop"></a>

## 7. 📐 RESIZE & CROP

### Resize Strategies with Automatic Optimization

| Strategy | Description | When to Use | Aspect Ratio | Thinking Applied |
|----------|-------------|-------------|--------------|------------------|
| **Proportional** | Maintain aspect ratio | Most cases | Preserved | 10 rounds auto |
| **Fixed Width** | Set width, auto height | Responsive design | Preserved | 10 rounds auto |
| **Fixed Height** | Set height, auto width | Gallery rows | Preserved | 10 rounds auto |
| **Exact Dimensions** | Force specific size | Thumbnails | May distort | 10 rounds auto |
| **Max Dimensions** | Fit within bounds | Container limits | Preserved | 10 rounds auto |

### Common Resize Scenarios with Deep Analysis

```javascript
// Thumbnail generation (10 rounds auto)
resize: {
  width: 150,
  height: 150,
  fit: 'cover',  // Square crop
  autoOptimized: true
}

// Web optimization (10 rounds auto)
resize: {
  width: 1920,
  fit: 'inside',  // Max width, maintain ratio
  preserveAspectRatio: true,
  deepAnalysis: 10
}

// Mobile optimization (10 rounds auto)
resize: {
  width: 640,
  fit: 'inside',
  thinkingApplied: 10
}
```

### Smart Crop Features with Auto-Intelligence

```javascript
// Intelligent cropping options (10 rounds analysis)
crop: {
  attention: 'center' | 'entropy' | 'attention',
  autoSelected: true  // System chooses best via deep thinking
  // center: Focus on center
  // entropy: Focus on busiest area
  // attention: Focus on region of interest
}
```

---

<a id="8-🔄-rotation--flipping"></a>

## 8. 🔄 ROTATION & FLIPPING

### Rotation Operation with Auto-Analysis

```javascript
rotate: {
  inputPath: string,
  outputPath: string,
  angle: number,         // Rotation angle in degrees
  background: string,    // Background color (auto-selected)
  thinkingRounds: 10     // Automatic optimization
}

// Common angles
angles: 90 | 180 | 270 | -90 | -180 | -270
```

### Flip Operation with Deep Thinking

```javascript
flip: {
  inputPath: string,
  outputPath: string,
  direction: 'horizontal' | 'vertical',
  autoOptimized: true    // 10 rounds applied
}
```

### Orientation Fixes (Automatic)
Imagician auto-corrects image orientation with deep analysis:
- Reads EXIF orientation flag
- Applies necessary rotation
- Updates or removes EXIF data
- All via 10-round thinking

---

<a id="9-🚨-error-handling"></a>

## 9. 🚨 ERROR HANDLING

### Common Issues with Automatic Recovery

| Issue | Cause | Solution | Fallback | Thinking Applied |
|-------|-------|----------|----------|------------------|
| **Connection lost** | Server crashed | Restart Claude Desktop | Check setup | Auto-retry with 10 rounds |
| **Format not supported** | Invalid format | Use JPEG, PNG, WebP, or AVIF | Convert externally first | Auto-convert via deep analysis |
| **File not found** | Wrong path | Check file path and permissions | Request correct path | Path analysis via thinking |
| **Memory error** | Large image | Reduce size first or increase memory | Process in chunks | Auto-chunk with optimization |
| **Quality out of range** | Invalid quality value | Use 1-100 range | Default to 80 | Auto-adjust via 10 rounds |
| **Sharp not installed** | Missing dependency | Reinstall package | Use alternative MCP | Auto-diagnose |

### Error Recovery Strategies with Deep Thinking

```javascript
async function processWithFallback(operation, mode='standard') {
  // Check connection first
  if (!await verifyConnection()) {
    return {
      error: "Imagician not connected",
      action: "Please setup Imagician MCP"
    };
  }
  
  // Apply automatic thinking
  const thinkingRounds = mode === 'quick' ? autoScale(1, 5) : 10;
  
  try {
    return await imagician.process(operation, {thinking: thinkingRounds});
  } catch (error) {
    // Auto-recovery with deep analysis
    if (error.type === 'MEMORY') {
      // Try with reduced quality (10 rounds analysis)
      operation.quality = Math.min(70, operation.quality);
      return await imagician.process(operation);
    }
    if (error.type === 'FORMAT') {
      // Convert to supported format first (10 rounds)
      operation.format = 'jpeg';
      return await imagician.process(operation);
    }
    throw error;
  }
}
```

### Error Display Format
```markdown
⚠️ Image Processing Error

**Issue:** [Error description]
**Server:** Imagician MCP
**Status:** [Connection status]
**Auto-recovery:** Applying 10 rounds of analysis...

**Solutions:**
• [Primary solution]
• [Alternative approach]
• [Fallback option]

Attempting automatic resolution...
```

---

<a id="10-⚡-usage-examples"></a>

## 10. ⚡ USAGE EXAMPLES

### Example Prompts with Automatic Deep Thinking

**Image Processing (10 rounds auto):**
```
"Resize photo.jpg to 800x600 pixels"
→ System applies 10 rounds of thinking automatically
→ Optimal fit mode selected
→ Quality preserved intelligently

"Convert image.png to WebP format with best quality"
→ Deep analysis determines 85% optimal
→ No user input needed

"Compress large.jpg to reduce file size by 50%"
→ 10 rounds find perfect quality/size balance
→ Multiple algorithms tested automatically
```

**Batch Processing (10 rounds per image):**
```
"Resize all images in folder to 1920px wide"
→ Each image gets full optimization
→ Consistent quality across batch

"Convert all PNGs to WebP format"
→ Deep analysis per file
→ Optimal settings for each
```

**Platform Optimization (10 rounds deep analysis):**
```
"Optimize image for Instagram"
→ 1080x1080 with platform-specific compression
→ All settings auto-determined

"Prepare hero image for website"
→ 1920px wide, WebP with JPEG fallback
→ Complete optimization automatic
```

### Workflow Example with Automatic Thinking

```javascript
// Complete image optimization workflow
async function optimizeForWeb(imagePath) {
  // 0. Verify connection
  const connection = await verifyImagicianConnection();
  if (!connection.connected) {
    throw new Error("Imagician not connected. Please setup MCP server.");
  }
  
  // Automatic 10-round deep analysis applied throughout
  
  // 1. Get metadata (with deep analysis)
  const metadata = await imagician.getMetadata(imagePath);
  
  // 2. Resize if needed (10 rounds determine optimal approach)
  if (metadata.width > 1920) {
    await imagician.resize({
      inputPath: imagePath,
      outputPath: 'temp.jpg',
      width: 1920,
      fit: 'inside'  // Auto-selected via thinking
    });
  }
  
  // 3. Convert to WebP (quality auto-optimized)
  await imagician.convert({
    inputPath: 'temp.jpg',
    outputPath: 'optimized.webp',
    format: 'webp',
    quality: 85  // Determined by 10-round analysis
  });
  
  // 4. Create JPEG fallback (auto-optimized)
  await imagician.convert({
    inputPath: 'temp.jpg',
    outputPath: 'optimized.jpg',
    format: 'jpeg',
    quality: 80  // Determined by deep thinking
  });
}
```

### Integration with Media Editor

When integrated with the Media Editor system:

- Media Editor verifies Imagician connection
- Receives natural language request
- **Applies 10 rounds of thinking automatically**
- Routes to Imagician MCP
- Executes operation with deep optimization
- Returns optimized image with metrics

Example conversation:
```
User: "Optimize this photo for my website"
Media Editor: [Checking Imagician connection...]
→ Connection verified ✔
→ Applying deep analysis (10 rounds)...
→ Imagician: Resize to 1920px max
→ Imagician: Convert to WebP 85%
→ Result: Image optimized, 72% size reduction
```

### Quick Mode Examples

```
User: "$quick resize photo.jpg"
→ Auto-scaling: Simple resize = 2 rounds
→ Fast execution with essential quality

User: "$quick compress batch of images"
→ Auto-scaling: Batch operation = 4 rounds
→ Balanced speed and optimization
```


## Key Differences from Generic Processing

This document reflects the **actual Imagician MCP server** implementation with automatic thinking:

- Connection verification required before all operations
- **10 rounds of deep thinking applied automatically (no user choice)**
- **Quick mode auto-scales 1-5 rounds based on complexity**
- Confirms supported operations: resize, convert, crop, compress, rotate, flip, list
- Accurate format list: JPEG, PNG, WebP, AVIF only
- Correct parameter names and types from documentation
- Actual installation methods from the repository
- Real usage examples with automatic optimization
- Sharp library optimizations and limitations


## Performance Notes

From the Sharp library used by Imagician with auto-optimization:
- High-performance Node.js image processing
- Uses libvips for speed
- Multi-threaded operations
- Memory-efficient streaming
- Supports large images (with memory considerations)
- Hardware acceleration where available
- **All operations enhanced by automatic deep thinking**

### Performance Benchmarks with Thinking Applied

| Operation | Small (<1MB) | Medium (1-5MB) | Large (>5MB) | Thinking Overhead |
|-----------|-------------|----------------|--------------|-------------------|
| Resize | <100ms | 100-300ms | 300-1000ms | +10ms |
| Convert | <150ms | 150-400ms | 400-1500ms | +10ms |
| Compress | <200ms | 200-500ms | 500-2000ms | +15ms |
| Crop | <50ms | 50-150ms | 150-500ms | +5ms |

### Performance Status Display
```markdown
📊 Imagician Performance

**Connection:** Active
**Response time:** 45ms
**Memory usage:** 128MB
**Queue:** 0 operations
**Thinking mode:** 10 rounds automatic
**Processing:** Optimized with deep analysis

Operating at peak efficiency
```

---

*This intelligence document reflects the actual Imagician MCP server implementation with automatic deep thinking. Connection verification is mandatory. All operations receive 10 rounds of optimization automatically in standard mode, or 1-5 auto-scaled rounds in quick mode. No user intervention required for professional results.*
