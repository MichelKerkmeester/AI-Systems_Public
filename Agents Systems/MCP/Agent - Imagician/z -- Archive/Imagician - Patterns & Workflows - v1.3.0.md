# Imagician - Patterns & Workflows - v1.3.0

Complete pattern library and workflow specifications for natural language image processing operations.

## Table of Contents
1. [📋 OVERVIEW](#1--overview)
2. [🎯 INTENT PATTERNS](#2--intent-patterns)
3. [🔄 WORKFLOW PATTERNS](#3--workflow-patterns)
4. [📐 DIMENSION PATTERNS](#4--dimension-patterns)
5. [🎨 FORMAT PATTERNS](#5--format-patterns)
6. [⚡ OPTIMIZATION PATTERNS](#6--optimization-patterns)
7. [📱 PLATFORM PATTERNS](#7--platform-patterns)
8. [🔧 BATCH PATTERNS](#8--batch-patterns)
9. [💾 PATH PATTERNS](#9--path-patterns)
10. [🚀 COMPLETE WORKFLOWS](#10--complete-workflows)

---

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the Imagician agent. Each pattern maps natural language to specific operations with smart defaults.

**Pattern Categories:**
- **Intent Recognition**: What the user wants to achieve
- **Parameter Extraction**: Dimensions, quality, format preferences
- **Workflow Selection**: Single vs multi-step operations
- **Platform Optimization**: Target-specific settings
- **Batch Processing**: Multiple file handling

---

## 2. 🎯 INTENT PATTERNS

### Size Reduction Intents

| User Says | Intent | Default Action | Parameters |
|-----------|--------|---------------|------------|
| "make smaller" | Resize | 50% reduction | Maintain ratio |
| "reduce size" | Compress | Quality 85% | Same dimensions |
| "shrink" | Resize | 75% of original | Maintain ratio |
| "too big" | Smart reduce | Resize or compress | Context-aware |
| "email size" | Email optimize | Max 5MB, 1024px | JPEG format |
| "web size" | Web optimize | Max 1920px | WebP format |

### Format Conversion Intents

| User Says | Target Format | Quality | Notes |
|-----------|--------------|---------|-------|
| "to jpg/jpeg" | JPEG | 90% | Remove transparency |
| "to png" | PNG | Lossless | Preserve transparency |
| "to webp" | WebP | 85% | Modern browsers |
| "universal format" | JPEG | 90% | Maximum compatibility |
| "transparent" | PNG/WebP | Lossless | Keep alpha channel |
| "for web" | WebP | 85% | Optimal for web |

### Quality Optimization Intents

| User Says | Quality Target | Size Priority | Use Case |
|-----------|---------------|---------------|----------|
| "best quality" | 95-100% | Low | Archival |
| "balanced" | 85-90% | Medium | General use |
| "compress" | 75-85% | High | Web/email |
| "maximum compression" | 60-75% | Maximum | Bandwidth limited |
| "lossless" | 100% | None | Preservation |

---

## 3. 🔄 WORKFLOW PATTERNS

### Single-Step Workflows

**Pattern: Simple Resize**
```yaml
Trigger: Specific dimensions mentioned
Steps:
  1. Parse dimensions
  2. Maintain aspect ratio
  3. Apply Lanczos resampling
  4. Save with suffix
Example: "resize to 800px" → 800px width, auto height
```

**Pattern: Format Convert**
```yaml
Trigger: Format name mentioned
Steps:
  1. Detect target format
  2. Apply optimal quality
  3. Handle transparency
  4. Convert and save
Example: "convert to webp" → WebP at 85%
```

### Multi-Step Workflows

**Pattern: Web Optimization**
```yaml
Trigger: "for website", "web", "online"
Steps:
  1. Resize to max 1920px
  2. Convert to WebP
  3. Set quality to 85%
  4. Enable progressive
  5. Strip metadata
Result: Fast-loading web image
```

**Pattern: Email Preparation**
```yaml
Trigger: "email", "attach", "send"
Steps:
  1. Check current size
  2. If >5MB, resize to 1024px
  3. Convert to JPEG
  4. Compress to 80-85%
  5. Ensure <5MB final
Result: Email-ready attachment
```

**Pattern: Social Media Set**
```yaml
Trigger: Platform name mentioned
Steps:
  1. Identify platform
  2. Apply platform dimensions
  3. Crop to aspect ratio
  4. Optimize quality
  5. Create platform-specific version
Result: Platform-optimized image
```

---

## 4. 📐 DIMENSION PATTERNS

### Dimension Recognition

| Pattern | Interpretation | Example | Result |
|---------|---------------|---------|--------|
| `{number}px` | Exact pixels | "800px" | 800 pixels |
| `{number}x{number}` | Width x Height | "1920x1080" | Exact dimensions |
| `{number}%` | Percentage | "50%" | Half size |
| `{ratio}` | Aspect ratio | "16:9" | Maintain ratio |
| `half/double` | Relative | "half size" | 50% or 200% |

### Common Dimensions Library

| Use Case | Dimensions | Aspect | Notes |
|----------|------------|--------|-------|
| **Web Hero** | 1920x1080 | 16:9 | Full HD |
| **Web Standard** | 1200x800 | 3:2 | Content width |
| **Thumbnail** | 150x150 | 1:1 | Square crop |
| **Email Max** | 1024x768 | 4:3 | Universal |
| **Mobile** | 640x960 | 2:3 | Portrait |
| **Desktop BG** | 2560x1440 | 16:9 | 2K resolution |

### Responsive Set Patterns

**Pattern: Standard Web Set**
```yaml
Sizes:
  - 320px (mobile)
  - 640px (tablet)
  - 1024px (desktop)
  - 1920px (full)
  - 150px (thumbnail)
Naming: {name}-{size}.{ext}
```

**Pattern: E-commerce Set**
```yaml
Sizes:
  - thumbnail: 150x150
  - gallery: 500x500
  - zoom: 1500x1500
  - original: As-is
Format: JPEG for all
```

---

## 5. 🎨 FORMAT PATTERNS

### Format Selection Logic

| Condition | Recommended | Reason |
|-----------|------------|--------|
| Has transparency | PNG/WebP | Preserve alpha |
| Photography | JPEG/WebP | Better compression |
| Line art/logos | PNG | Sharp edges |
| Web use | WebP | 30% smaller |
| Email | JPEG | Universal support |
| Archival | PNG | Lossless |
| Modern web | AVIF | 50% smaller than JPEG |

### Quality Presets by Format

| Format | Web | Email | Archive | Thumbnail |
|--------|-----|-------|---------|-----------|
| **JPEG** | 85% | 80% | 95% | 75% |
| **PNG** | Optimized | Optimized | Lossless | Optimized |
| **WebP** | 85% | 80% | 95% | 75% |
| **AVIF** | 80% | 75% | 90% | 70% |

---

## 6. ⚡ OPTIMIZATION PATTERNS

### Optimization Strategies

**Pattern: Balanced Optimization**
```yaml
Goal: Quality vs Size balance
Steps:
  - Quality: 85%
  - Format: WebP if supported
  - Dimensions: Max 1920px
  - Progressive: Enabled
Result: 60-70% size reduction
```

**Pattern: Maximum Compression**
```yaml
Goal: Minimum file size
Steps:
  - Quality: 65-70%
  - Format: JPEG or WebP
  - Dimensions: Reduce by 25%
  - Strip all metadata
Result: 80-90% size reduction
```

**Pattern: Quality Priority**
```yaml
Goal: Best visual quality
Steps:
  - Quality: 95%
  - Format: PNG or high-quality JPEG
  - Dimensions: Maintain original
  - Keep color profile
Result: Minimal compression
```

### Performance Metrics

| Operation | Typical Reduction | Quality Impact | Speed Gain |
|-----------|------------------|----------------|------------|
| WebP conversion | 30% | None | 30% faster |
| 85% quality | 50% | Minimal | 2x faster |
| Resize 50% | 75% | None | 4x faster |
| Progressive | 0% | None | Perceived faster |
| Metadata strip | 5-10% | None | Slight |

---

## 7. 📱 PLATFORM PATTERNS

### Social Media Specifications

| Platform | Feed | Story | Profile | Cover |
|----------|------|-------|---------|-------|
| **Instagram** | 1080x1080 | 1080x1920 | 320x320 | N/A |
| **Facebook** | 1200x630 | 1080x1920 | 180x180 | 1200x630 |
| **Twitter/X** | 1200x675 | N/A | 400x400 | 1500x500 |
| **LinkedIn** | 1200x627 | N/A | 400x400 | 1128x191 |
| **YouTube** | 1280x720 | N/A | 800x800 | 2560x1440 |

### Platform Optimization Workflows

**Pattern: Instagram Post**
```yaml
Dimensions: 1080x1080 (square)
Format: JPEG
Quality: 90%
Color: sRGB
Special: No EXIF rotation
```

**Pattern: Twitter/X Share**
```yaml
Dimensions: 1200x675 (16:9)
Format: JPEG or PNG
Quality: 85%
Size limit: <5MB
Special: Preview optimization
```

**Pattern: LinkedIn Article**
```yaml
Dimensions: 1200x627
Format: JPEG
Quality: 85%
Aspect: 1.91:1
Special: Professional appearance
```

---

## 8. 🔧 BATCH PATTERNS

### Batch Processing Patterns

**Pattern: Uniform Resize**
```yaml
Trigger: Multiple files + same operation
Process:
  - Apply same settings to all
  - Maintain folder structure
  - Add consistent suffix
Example: "resize all to 800px"
```

**Pattern: Responsive Set Generation**
```yaml
Trigger: "responsive", "multiple sizes"
Process:
  - Generate predefined sizes
  - Create size folders
  - Optimize each size
Output:
  /small/image.jpg (320px)
  /medium/image.jpg (640px)
  /large/image.jpg (1024px)
  /xlarge/image.jpg (1920px)
```

**Pattern: Format Migration**
```yaml
Trigger: "convert all to"
Process:
  - Convert each file
  - Preserve names
  - Optional: Keep originals
Example: "convert all PNGs to WebP"
```

### Batch Naming Conventions

| Pattern | Example | Use Case |
|---------|---------|----------|
| `{name}-{size}` | photo-800px.jpg | Size variants |
| `{name}-{platform}` | photo-instagram.jpg | Platform specific |
| `{name}-optimized` | photo-optimized.jpg | General optimization |
| `{date}-{name}` | 2024-01-photo.jpg | Timestamped |
| `thumb-{name}` | thumb-photo.jpg | Thumbnails |

---

## 9. 💾 PATH PATTERNS

### macOS Path Recognition

| Pattern | Example | Resolution |
|---------|---------|------------|
| `~/` prefix | ~/Desktop/pic.jpg | Home directory |
| Absolute | /Users/name/pic.jpg | Full path |
| Relative | ./images/pic.jpg | Current directory |
| Spaces | ~/My Photos/pic.jpg | Quote or escape |
| Special chars | ~/Photos/café.jpg | Handle UTF-8 |

### Smart Path Handling

**Pattern: Desktop Default**
```yaml
When: No path specified
Check: ~/Desktop/ first
Fallback: ~/Downloads/
Ask: If not found
```

**Pattern: Output Location**
```yaml
Default: Same as input
Suffix: Add operation descriptor
Options:
  - Same folder with suffix
  - New subfolder
  - Custom location
```

### Common macOS Locations

| Location | Path | Typical Use |
|----------|------|-------------|
| Desktop | ~/Desktop/ | Quick access |
| Downloads | ~/Downloads/ | Browser downloads |
| Documents | ~/Documents/ | User documents |
| Pictures | ~/Pictures/ | Photo library |
| iCloud | ~/Library/Mobile Documents/com~apple~CloudDocs/ | Cloud sync |
| Screenshots | ~/Desktop/ or ~/Pictures/Screenshots/ | System captures |

---

## 10. 🚀 COMPLETE WORKFLOWS

### Workflow: Professional Web Presence

```yaml
Name: Complete Web Optimization
Trigger: "prepare for website"
Steps:
  1. Analyze original (dimensions, format, size)
  2. Create responsive set:
     - 320px (mobile)
     - 640px (tablet)  
     - 1024px (desktop)
     - 1920px (full)
     - 150px (thumbnail)
  3. Convert all to WebP
  4. Optimize quality (85%)
  5. Generate fallback JPEGs
  6. Create picture element HTML
Output:
  /images/
    /webp/
      image-320.webp
      image-640.webp
      image-1024.webp
      image-1920.webp
      image-thumb.webp
    /jpg/
      [same structure].jpg
```

### Workflow: E-commerce Product

```yaml
Name: Product Image Set
Trigger: "product photos"
Steps:
  1. Create square crop (maintain focus)
  2. Generate sizes:
     - Thumbnail: 150x150
     - Grid: 300x300
     - Product: 600x600
     - Zoom: 1500x1500
  3. White background if needed
  4. Consistent lighting/color
  5. Optimize for fast loading
Output: Complete product image set
```

### Workflow: Email Campaign

```yaml
Name: Email-Ready Images
Trigger: "email newsletter"
Steps:
  1. Resize to max 600px width
  2. Convert to JPEG
  3. Compress to <100KB each
  4. Maintain brand colors
  5. Test in email clients
Constraints:
  - Total email <5MB
  - Universal compatibility
  - Fast loading
```

### Workflow: Social Media Suite

```yaml
Name: Multi-Platform Social
Trigger: "all social media"
Steps:
  1. Analyze subject/composition
  2. Create platform versions:
     - Instagram: 1080x1080 square
     - Facebook: 1200x630 link
     - Twitter: 1200x675 card
     - LinkedIn: 1200x627 share
     - Stories: 1080x1920 vertical
  3. Optimize each for platform
  4. Maintain brand consistency
Output: Ready-to-post set
```

---

## Pattern Matching Priority

When multiple patterns match, use this priority:
1. **Explicit dimensions** (highest priority)
2. **Platform specific** 
3. **Use case specific**
4. **Format specific**
5. **General optimization** (lowest priority)

---

## Smart Default Selection

When parameters aren't specified:
- **Quality**: 85% (sweet spot)
- **Format**: WebP for web, JPEG for email
- **Dimensions**: Maintain ratio, max 1920px
- **Progressive**: Enabled for JPEG
- **Metadata**: Strip for web, keep for archive

---

*This pattern library enables natural language understanding of image editing requests. Patterns cascade from specific to general, ensuring optimal handling of every request.*