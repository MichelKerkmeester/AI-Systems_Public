# Media Editor - MCP Intelligence - Imagician - v0.102

Complete technical reference for the Imagician MCP server integration for image processing operations.

## Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [📌 CONNECTION VERIFICATION](#2-📌-connection-verification)
3. [🛠️ CORE OPERATIONS](#3-🛠️-core-operations)
4. [📊 SUPPORTED FORMATS](#4-📊-supported-formats)
5. [⚙️ OPERATION DETAILS](#5-⚙️-operation-details)
6. [🎯 QUALITY & COMPRESSION](#6-🎯-quality--compression)
7. [📐 RESIZE & CROP](#7-📐-resize--crop)
8. [🔄 ROTATION & FLIPPING](#8-🔄-rotation--flipping)
9. [💾 INSTALLATION & SETUP](#9-💾-installation--setup)
10. [🚨 ERROR HANDLING](#10-🚨-error-handling)
11. [⚡ USAGE EXAMPLES](#11-⚡-usage-examples)

## 1. 📋 OVERVIEW

### MCP Server Details
• **Name**: Imagician MCP
• **Package**: @flowy11/imagician
• **Repository**: https://github.com/flowy11/imagician
• **Engine**: Sharp (Node.js image processing library)
• **Protocol**: Model Context Protocol (MCP)
• **Installation**: NPX, NPM, or local Node.js

### Core Capabilities
Based on the actual implementation, Imagician provides:
• High-performance image resizing with various fit options
• Format conversion between JPEG, PNG, WebP, and AVIF
• Image cropping with precise region control
• Compression and quality optimization
• Rotation and flipping operations
• Metadata extraction and handling
• Batch processing support

### Integration with Media Editor
Imagician serves as the primary image processing engine within the Media Editor system, handling all image-specific operations while Video-Audio MCP handles video and audio processing.

**CRITICAL**: Always verify connection before operations.

## 2. 📌 CONNECTION VERIFICATION

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
            'message': 'Imagician connected and ready'
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
        'memory': check_available_memory()
    }
    return all(checks.values())
```

## 3. 🛠️ CORE OPERATIONS

### Available MCP Tools

According to the GitHub documentation, Imagician provides these operations:

| Operation | MCP Tool | Description | Parameters | Pre-check |
|-----------|----------|-------------|------------|-----------|
| **Resize** | `resize` | Change image dimensions with fit options | width, height, fit, preserveAspectRatio | Connection required |
| **Convert** | `convert` | Convert between formats with quality control | format, quality | Connection required |
| **Crop** | `crop` | Extract specific regions from images | x, y, width, height | Connection required |
| **Compress** | `compress` | Optimize file size with quality settings | quality, strip, optimize | Connection required |
| **Rotate** | `rotate` | Rotate images by angle | angle, background | Connection required |
| **Flip** | `flip` | Flip images horizontally or vertically | direction | Connection required |
| **Metadata** | `getMetadata` | Extract image information | - | Connection required |
| **Batch** | `batch` | Process multiple images | operations array | Connection required |
| **List** | `list_images` | List images in folders | folder | Connection required |

### Operation Priority
When multiple operations are needed, Imagician applies them in optimal order:
• Verify connection
• Crop (if needed)
• Resize (if needed)
• Rotate/Flip (if needed)
• Format conversion
• Quality optimization

## 4. 📊 SUPPORTED FORMATS

### Confirmed Format Support

From the documentation:

| Format | Extension | Input | Output | Best For | Transparency |
|--------|-----------|-------|--------|----------|-------------|
| **JPEG** | .jpg, .jpeg | ✅ | ✅ | Photos, complex images | ❌ |
| **PNG** | .png | ✅ | ✅ | Graphics, screenshots | ✅ |
| **WebP** | .webp | ✅ | ✅ | Modern web, balanced | ✅ |
| **AVIF** | .avif | ✅ | ✅ | Next-gen compression | ✅ |

### Format Selection Logic

```python
def select_output_format(input_format, use_case):
    # Verify connection first
    if not verify_imagician_connection()['connected']:
        return None, "Imagician not connected"
    
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

## 5. ⚙️ OPERATION DETAILS

### Resize Operation

```javascript
// Parameters from documentation
resize: {
  inputPath: string,       // Path to input image
  outputPath: string,      // Path to save resized image
  width: number,          // Target width (optional)
  height: number,         // Target height (optional)
  fit: string,            // Fit mode
  preserveAspectRatio: boolean // Default: true
}

// Fit options
fit: 'cover' | 'contain' | 'fill' | 'inside' | 'outside'
```

**Fit Mode Explanations:**
• **cover**: Crop to cover both dimensions (may lose edges)
• **contain**: Fit within dimensions (may add padding)
• **fill**: Stretch to exact dimensions (may distort)
• **inside**: Resize to fit inside bounds (preserves ratio)
• **outside**: Resize to fit outside bounds (preserves ratio)

### Convert Operation

```javascript
// Parameters from documentation
convert: {
  inputPath: string,      // Path to input image
  outputPath: string,     // Path to save converted image
  format: string,         // Target format
  quality: number         // 1-100 (default: 80)
}

// Supported formats
format: 'jpeg' | 'png' | 'webp' | 'avif'
```

### Crop Operation

```javascript
// Extract specific region
crop: {
  inputPath: string,      // Source image
  outputPath: string,     // Output path
  x: number,             // X coordinate (from left)
  y: number,             // Y coordinate (from top)
  width: number,         // Crop width
  height: number         // Crop height
}
```

### Compress Operation

```javascript
compress: {
  inputPath: string,
  outputPath: string,
  quality: number,        // 1-100
  strip: boolean,        // Remove metadata
  optimize: boolean      // Additional optimization
}
```

## 6. 🎯 QUALITY & COMPRESSION

### Quality Settings

From the implementation:

| Quality | Use Case | File Size Impact | Visual Impact |
|---------|----------|-----------------|---------------|
| **100** | Lossless/Archive | Largest | Perfect |
| **90-95** | High quality prints | Large | Excellent |
| **80-89** | Default/Web | Moderate | Very good |
| **70-79** | Good compression | Smaller | Good |
| **60-69** | Acceptable quality | Small | Acceptable |
| **<60** | Heavy compression | Smallest | Visible loss |

### Compression Best Practices

**For Photos:**
• JPEG: 80-85% quality
• WebP: 85% quality
• AVIF: 75-80% quality (better algorithm)

**For Graphics:**
• PNG: Lossless (100%)
• WebP: 90-95% quality
• Transparency required: PNG or WebP

**For Web:**
• Primary: WebP at 85%
• Fallback: JPEG at 80%
• Modern: AVIF at 75%

### Smart Compression Algorithm

```javascript
async function smartCompress(image, targetUseCase) {
  // Check connection
  if (!await verifyConnection()) {
    throw new Error("Imagician not connected");
  }
  
  const settings = {
    'web': { quality: 85, format: 'webp' },
    'email': { quality: 80, format: 'jpeg' },
    'social': { quality: 90, format: 'jpeg' },
    'archive': { quality: 100, format: 'png' }
  };
  
  return settings[targetUseCase] || settings['web'];
}
```

## 7. 📐 RESIZE & CROP

### Resize Strategies

| Strategy | Description | When to Use | Aspect Ratio |
|----------|-------------|-------------|--------------|
| **Proportional** | Maintain aspect ratio | Most cases | Preserved |
| **Fixed Width** | Set width, auto height | Responsive design | Preserved |
| **Fixed Height** | Set height, auto width | Gallery rows | Preserved |
| **Exact Dimensions** | Force specific size | Thumbnails | May distort |
| **Max Dimensions** | Fit within bounds | Container limits | Preserved |

### Common Resize Scenarios

```javascript
// Thumbnail generation
resize: {
  width: 150,
  height: 150,
  fit: 'cover'  // Square crop
}

// Web optimization
resize: {
  width: 1920,
  fit: 'inside',  // Max width, maintain ratio
  preserveAspectRatio: true
}

// Mobile optimization
resize: {
  width: 640,
  fit: 'inside'
}
```

### Smart Crop Features

```javascript
// Intelligent cropping options
crop: {
  attention: 'center' | 'entropy' | 'attention'
  // center: Focus on center
  // entropy: Focus on busiest area
  // attention: Focus on region of interest
}
```

### Crop Calculations

```javascript
// Center crop calculation
function centerCrop(imageWidth, imageHeight, targetWidth, targetHeight) {
  const x = Math.max(0, (imageWidth - targetWidth) / 2);
  const y = Math.max(0, (imageHeight - targetHeight) / 2);
  return { x, y, width: targetWidth, height: targetHeight };
}
```

## 8. 🔄 ROTATION & FLIPPING

### Rotation Operation

```javascript
rotate: {
  inputPath: string,
  outputPath: string,
  angle: number,         // Rotation angle in degrees
  background: string     // Background color for empty areas
}

// Common angles
angles: 90 | 180 | 270 | -90 | -180 | -270
```

### Flip Operation

```javascript
flip: {
  inputPath: string,
  outputPath: string,
  direction: 'horizontal' | 'vertical'
}
```

### Orientation Fixes
Imagician can auto-correct image orientation based on EXIF data:
• Reads EXIF orientation flag
• Applies necessary rotation
• Updates or removes EXIF data

## 9. 💾 INSTALLATION & SETUP

### Installation Methods

**1. NPX (Recommended for Claude Desktop):**
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

**2. Global NPM Installation:**
```bash
npm install -g @flowy11/imagician

# Then in config:
{
  "mcpServers": {
    "imagician": {
      "command": "imagician"
    }
  }
}
```

**3. Local Installation:**
```bash
npm install @flowy11/imagician

# Then in config:
{
  "mcpServers": {
    "imagician": {
      "command": "node",
      "args": ["/path/to/imagician/dist/index.js"]
    }
  }
}
```

### Configuration Locations

• **Claude Desktop Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
• **Claude Desktop Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
• **Cursor**: Settings → MCP
• **Windsurf**: Configuration file

### Verification
After installation, verify Imagician is working:
• Restart Claude Desktop
• Check MCP server status
• Test with list_images operation
• Confirm connection with simple resize

### Setup Verification Display
```markdown
🔧 Imagician Setup Check

• Installation: Complete
• Configuration: Valid
• Connection: Active
• Test operation: Success

Ready for image processing!
```

## 10. 🚨 ERROR HANDLING

### Common Issues

| Issue | Cause | Solution | Fallback |
|-------|-------|----------|----------|
| **Connection lost** | Server crashed | Restart Claude Desktop | Check setup |
| **Format not supported** | Invalid format | Use JPEG, PNG, WebP, or AVIF | Convert externally first |
| **File not found** | Wrong path | Check file path and permissions | Request correct path |
| **Memory error** | Large image | Reduce size first or increase memory | Process in chunks |
| **Quality out of range** | Invalid quality value | Use 1-100 range | Default to 80 |
| **Sharp not installed** | Missing dependency | Reinstall package | Use alternative MCP |

### Error Recovery Strategies

```javascript
async function processWithFallback(operation) {
  // Check connection first
  if (!await verifyConnection()) {
    return {
      error: "Imagician not connected",
      action: "Please setup Imagician MCP"
    };
  }
  
  try {
    return await imagician.process(operation);
  } catch (error) {
    if (error.type === 'MEMORY') {
      // Try with reduced quality
      operation.quality = Math.min(70, operation.quality);
      return await imagician.process(operation);
    }
    if (error.type === 'FORMAT') {
      // Convert to supported format first
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

**Solutions:**
• [Primary solution]
• [Alternative approach]
• [Fallback option]

Need help troubleshooting?
```

## 11. ⚡ USAGE EXAMPLES

### Example Prompts for Media Editor

**Image Processing:**
```
"Resize photo.jpg to 800x600 pixels"
"Convert image.png to WebP format with 85% quality"
"Crop profile.jpg to 500x500 square from center"
"Compress large.jpg to reduce file size by 50%"
"Rotate landscape.jpg 90 degrees clockwise"
```

**Batch Processing:**
```
"Resize all images in folder to 1920px wide"
"Convert all PNGs to WebP format"
"Compress all JPEGs to 80% quality"
"Create thumbnails for all images"
```

**Platform Optimization:**
```
"Optimize image for Instagram (1080x1080)"
"Prepare hero image for website (1920px wide, WebP)"
"Create email-friendly version (max 1024px, JPEG)"
"Generate responsive image set (320, 640, 1024, 1920)"
```

### Workflow Example

```javascript
// Complete image optimization workflow
async function optimizeForWeb(imagePath) {
  // 0. Verify connection
  const connection = await verifyImagicianConnection();
  if (!connection.connected) {
    throw new Error("Imagician not connected. Please setup MCP server.");
  }
  
  // 1. Get metadata
  const metadata = await imagician.getMetadata(imagePath);
  
  // 2. Resize if needed
  if (metadata.width > 1920) {
    await imagician.resize({
      inputPath: imagePath,
      outputPath: 'temp.jpg',
      width: 1920,
      fit: 'inside'
    });
  }
  
  // 3. Convert to WebP
  await imagician.convert({
    inputPath: 'temp.jpg',
    outputPath: 'optimized.webp',
    format: 'webp',
    quality: 85
  });
  
  // 4. Create JPEG fallback
  await imagician.convert({
    inputPath: 'temp.jpg',
    outputPath: 'optimized.jpg',
    format: 'jpeg',
    quality: 80
  });
}
```

### Integration with Media Editor

When integrated with the Media Editor system:

• Media Editor verifies Imagician connection
• Receives natural language request
• Identifies image operation needed
• Routes to Imagician MCP
• Applies smart defaults based on use case
• Executes operation with progress tracking
• Returns optimized image with metrics

Example conversation:
```
User: "Optimize this photo for my website"
Media Editor: [Checking Imagician connection...]
→ Connection verified ✓
→ Imagician: Resize to 1920px max
→ Imagician: Convert to WebP 85%
→ Result: Image optimized, 72% size reduction
```

## Key Differences from Generic Processing

This document reflects the **actual Imagician MCP server** implementation:

• Connection verification required before all operations
• Confirms supported operations: resize, convert, crop, compress, rotate, flip, list
• Accurate format list: JPEG, PNG, WebP, AVIF only
• Correct parameter names and types from documentation
• Actual installation methods from the repository
• Real usage examples from the documentation
• Sharp library optimizations and limitations

## Performance Notes

From the Sharp library used by Imagician:
• High-performance Node.js image processing
• Uses libvips for speed
• Multi-threaded operations
• Memory-efficient streaming
• Supports large images (with memory considerations)
• Hardware acceleration where available

### Performance Benchmarks

| Operation | Small (<1MB) | Medium (1-5MB) | Large (>5MB) |
|-----------|-------------|----------------|--------------|
| Resize | <100ms | 100-300ms | 300-1000ms |
| Convert | <150ms | 150-400ms | 400-1500ms |
| Compress | <200ms | 200-500ms | 500-2000ms |
| Crop | <50ms | 50-150ms | 150-500ms |

### Performance Status Display
```markdown
📊 Imagician Performance

**Connection:** Active
**Response time:** 45ms
**Memory usage:** 128MB
**Queue:** 0 operations

Operating normally
```

*This intelligence document reflects the actual Imagician MCP server implementation as documented in the GitHub repository. Connection verification is mandatory. All operations and parameters are based on the real capabilities of the server.*