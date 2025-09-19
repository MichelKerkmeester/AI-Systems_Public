# Imagician - Platform Specs & Defaults v0.100

Complete specifications for platforms, quality settings, and error handling.

## Table of Contents
1. [🌐 PLATFORM SPECIFICATIONS](#1--platform-specifications)
2. [📊 QUALITY & FORMAT DEFAULTS](#2--quality--format-defaults)
3. [🚨 ERROR HANDLING](#3--error-handling)
4. [💡 BEST PRACTICES](#4--best-practices)

---

## 1. 🌐 PLATFORM SPECIFICATIONS

### Social Media Platforms

#### Instagram
```yaml
post_square:
  dimensions: 1080x1080
  aspect: 1:1
  format: JPEG
  quality: 90
  max_size: 30MB
  
post_portrait:
  dimensions: 1080x1350
  aspect: 4:5
  format: JPEG
  quality: 90
  
post_landscape:
  dimensions: 1080x566
  aspect: 1.91:1
  format: JPEG
  quality: 90
  
story:
  dimensions: 1080x1920
  aspect: 9:16
  format: JPEG
  quality: 90
  max_size: 30MB
  
reel_cover:
  dimensions: 1080x1920
  aspect: 9:16
  format: JPEG
  quality: 85
  
profile_picture:
  dimensions: 320x320
  aspect: 1:1
  format: JPEG
  quality: 85
  note: "Displays at 110x110 on mobile"
```

#### Facebook
```yaml
cover_photo:
  dimensions: 820x312
  aspect: 2.63:1
  format: JPEG
  quality: 85
  note: "Displays 820x312 on desktop, 640x360 on mobile"
  
post:
  dimensions: 1200x630
  aspect: 1.91:1
  format: JPEG
  quality: 85
  
profile_picture:
  dimensions: 400x400
  aspect: 1:1
  format: JPEG
  quality: 90
  note: "Displays at 170x170 on desktop"
  
event_cover:
  dimensions: 1920x1080
  aspect: 16:9
  format: JPEG
  quality: 85
```

#### Twitter/X
```yaml
header:
  dimensions: 1500x500
  aspect: 3:1
  format: JPEG
  quality: 85
  max_size: 2MB
  
post_single_image:
  dimensions: 1200x675
  aspect: 16:9
  format: JPEG
  quality: 85
  max_size: 5MB
  
post_two_images:
  dimensions: 700x800
  aspect: 7:8
  format: JPEG
  quality: 85
  
profile_picture:
  dimensions: 400x400
  aspect: 1:1
  format: JPEG
  quality: 90
  max_size: 2MB
```

#### LinkedIn
```yaml
personal_banner:
  dimensions: 1584x396
  aspect: 4:1
  format: JPEG
  quality: 85
  max_size: 8MB
  
company_banner:
  dimensions: 1128x191
  aspect: 5.9:1
  format: JPEG
  quality: 85
  
article_image:
  dimensions: 1200x627
  aspect: 1.91:1
  format: JPEG
  quality: 85
  
post:
  dimensions: 1200x1200
  aspect: 1:1
  format: JPEG
  quality: 85
  
profile_picture:
  dimensions: 400x400
  aspect: 1:1
  format: JPEG
  quality: 90
  max_size: 8MB
```

#### YouTube
```yaml
thumbnail:
  dimensions: 1280x720
  aspect: 16:9
  format: JPEG
  quality: 90
  max_size: 2MB
  note: "Must be 16:9 for best results"
  
channel_art:
  dimensions: 2560x1440
  aspect: 16:9
  format: JPEG
  quality: 85
  max_size: 6MB
  safe_area: "1546x423 center for all devices"
  
channel_icon:
  dimensions: 800x800
  aspect: 1:1
  format: JPEG
  quality: 90
  note: "Displays at 98x98"
```

#### Pinterest
```yaml
standard_pin:
  dimensions: 1000x1500
  aspect: 2:3
  format: JPEG
  quality: 90
  note: "Optimal 2:3 ratio"
  
square_pin:
  dimensions: 1000x1000
  aspect: 1:1
  format: JPEG
  quality: 90
  
long_pin:
  dimensions: 1000x2100
  aspect: 1:2.1
  format: JPEG
  quality: 90
  max_aspect: "1:2.1"
  
story_pin:
  dimensions: 1080x1920
  aspect: 9:16
  format: JPEG
  quality: 90
```

### Web Standards

```yaml
hero_image:
  dimensions: 1920x1080
  aspect: 16:9
  format: WebP
  fallback: JPEG
  quality: 85
  
blog_featured:
  dimensions: 1200x630
  aspect: 1.91:1
  format: WebP
  quality: 85
  
thumbnail_grid:
  small: 150x150
  medium: 300x300
  large: 500x500
  format: JPEG or WebP
  quality: 80
  
responsive_breakpoints:
  mobile: 320-767
  tablet: 768-1023
  desktop: 1024-1919
  wide: 1920+
  
common_widths:
  mobile: [320, 375, 414]
  tablet: [768, 834, 1024]
  desktop: [1280, 1440, 1920]
  4k: [2560, 3840]
```

### Email Standards

```yaml
email_attachment:
  max_dimension: 1024
  max_file_size: 5MB
  format: JPEG
  quality: 85
  note: "Gmail limit 25MB total"
  
email_inline:
  max_width: 600
  format: JPEG
  quality: 80
  note: "Outlook safe width"
  
newsletter_hero:
  dimensions: 600x300
  format: JPEG
  quality: 85
```

---

## 2. 📊 QUALITY & FORMAT DEFAULTS

### Quality Levels by Use Case

```yaml
archival:
  quality: 100
  format: PNG or TIFF
  compression: lossless
  use_for: "Long-term storage, print masters"
  
professional:
  quality: 95-100
  format: JPEG or PNG
  use_for: "Portfolio, gallery, print"
  
high_quality_web:
  quality: 85-90
  format: WebP or JPEG
  use_for: "Hero images, product photos"
  
standard_web:
  quality: 80-85
  format: WebP or JPEG
  use_for: "Blog posts, general content"
  
optimized:
  quality: 75-80
  format: WebP
  use_for: "Fast-loading pages, mobile"
  
thumbnail:
  quality: 70-75
  format: JPEG or WebP
  use_for: "Previews, galleries"
  
aggressive:
  quality: 60-70
  format: WebP or AVIF
  use_for: "High-traffic, bandwidth-limited"
```

### Format Selection Guide

```yaml
JPEG:
  best_for: "Photos without transparency"
  pros: "Universal support, good compression"
  cons: "No transparency, generation loss"
  quality_sweet_spot: 85
  
PNG:
  best_for: "Graphics, text, transparency"
  pros: "Lossless, transparency, sharp edges"
  cons: "Large files for photos"
  compression: 9 (max)
  
WebP:
  best_for: "Modern web, all purposes"
  pros: "30% smaller, transparency, animation"
  cons: "95% browser support"
  quality_sweet_spot: 85
  
AVIF:
  best_for: "Cutting-edge web"
  pros: "50% smaller, HDR support"
  cons: "75% browser support"
  quality_sweet_spot: 80
```

### Fit Mode Selection

```yaml
cover:
  behavior: "Fill frame, crop excess"
  use_when: "Exact dimensions needed"
  common: "Thumbnails, hero images"
  
contain:
  behavior: "Show entire image, add padding"
  use_when: "Complete image must show"
  common: "Product photos, logos"
  
fill:
  behavior: "Stretch to fit"
  use_when: "Exact fit required"
  warning: "May distort image"
  
inside:
  behavior: "Fit within bounds"
  use_when: "Maximum size constraint"
  common: "Email attachments"
  
outside:
  behavior: "Cover minimum dimensions"
  use_when: "Responsive images"
  common: "Srcset generation"
```

---

## 3. 🚨 ERROR HANDLING

### File Errors

#### File Not Found
```yaml
error: "Cannot locate file"

interactive_response: |
  ❌ I can't find: [filename]
  
  Let's troubleshoot together:
  1. Check spelling (photo.jpg vs photo.jpeg?)
  2. Is it in the current folder?
  3. Want to try the full path?
  
  What would you like to try?

quick_response: |
  ❌ File not found: [filename]
  Check spelling or use full path
```

#### Permission Denied
```yaml
error: "Cannot access file"
user_message: |
  ⚠️ Cannot access this file
  
  Possible causes:
  • File is open in another app
  • Located in protected folder
  • Insufficient permissions
  
solutions:
  - "Close other apps using this file"
  - "Copy to Downloads folder"
  - "Check file permissions"
```

### Quality Warnings

#### Upscaling Alert
```yaml
trigger: target_size > source_size

interactive_response: |
  ⚠️ Quality Warning
  
  You're trying to enlarge from [source] to [target].
  This will make the image blurry/pixelated.
  
  What would you prefer:
  1. Keep original size (recommended)
  2. Find a higher resolution version
  3. Proceed anyway (quality will suffer)
  4. Try AI upscaling service
  
  Which option works for you?

quick_response: |
  ⚠️ Upscaling will reduce quality
  [source] → [target]
  Proceed? (Y/N)
```

#### Heavy Compression
```yaml
trigger: quality < 70
user_message: |
  ⚠️ Compression Warning
  
  Quality setting: [quality]%
  Impact: Visible quality loss
  
  Consider:
  • Reducing dimensions instead
  • Using 75-80% quality
  • Converting to WebP
```

### Format Issues

#### Unsupported Format
```yaml
error: "Format not supported"
formats: [RAW, PSD, AI, EPS]
user_message: |
  ❌ Cannot process [format] directly
  
  Solution:
  1. Export as JPEG/PNG from photo editor
  2. Use online converter
  3. Process exported version
```

#### Transparency Loss
```yaml
trigger: PNG/WebP → JPEG
user_message: |
  💡 Transparency Notice
  
  Converting to JPEG removes transparency
  Background will become: [color]
  
  Options:
  1. White background (default)
  2. Black background
  3. Custom color
  4. Keep PNG/WebP format
```

### Storage Issues

#### Overwrite Protection
```yaml
trigger: output_exists
user_message: |
  ⚠️ File exists: [filename]
  
  Options:
  1. Auto-rename: [filename-2]
  2. Replace existing
  3. Choose new name
  4. Cancel
  
default: option_1
```

#### Insufficient Space
```yaml
error: "Not enough disk space"
user_message: |
  ❌ Need [required]MB, have [available]MB
  
  Solutions:
  1. Free up space
  2. Save elsewhere
  3. Use more compression
  4. Process fewer images
```

---

## 4. 💡 BEST PRACTICES

### Performance Tips

```yaml
batch_processing:
  - Group similar operations
  - Process large files individually
  - Use consistent settings
  - Monitor memory usage
  
optimization_order:
  1. Resize first (reduces data)
  2. Then convert format
  3. Finally compress
  reason: "Each step works with less data"
  
caching:
  - Reuse calculated dimensions
  - Store format preferences
  - Remember quality settings
```

### Quality Guidelines

```yaml
never_upscale:
  reason: "Always degrades quality"
  alternative: "Use original or AI upscaling"
  
progressive_compression:
  start: 90
  reduce_by: 5
  until: target_size_reached
  minimum: 60
  
format_progression:
  modern: AVIF → WebP → JPEG
  compatible: JPEG → PNG
  quality: PNG → TIFF
```

### Web Optimization

```yaml
responsive_images:
  always_include:
    - Mobile size (320-640)
    - Tablet size (768-1024)
    - Desktop size (1920)
  
  naming:
    pattern: "image-[width]w.ext"
    example: "hero-320w.webp"
    
loading_performance:
  - Use progressive encoding
  - Optimize above the fold first
  - Lazy load below fold
  - Provide size hints
```

### User Experience

```yaml
feedback_principles:
  - Always show before/after
  - Display size savings
  - Explain quality trade-offs
  - Suggest next steps
  
error_handling:
  - Never fail silently
  - Provide alternatives
  - Explain in simple terms
  - Preserve originals
  
educational_moments:
  - Why WebP is better for web
  - When PNG beats JPEG
  - Platform requirements reasoning
  - Optimization impact
```

---

## 📊 Quick Reference Tables

### Platform Dimensions At-a-Glance
| Platform | Post | Story | Profile | Cover |
|----------|------|-------|---------|-------|
| Instagram | 1080x1080 | 1080x1920 | 320x320 | - |
| Facebook | 1200x630 | 1080x1920 | 400x400 | 820x312 |
| Twitter | 1200x675 | - | 400x400 | 1500x500 |
| LinkedIn | 1200x627 | - | 400x400 | 1584x396 |
| YouTube | - | - | 800x800 | 2560x1440 |
| Pinterest | 1000x1500 | 1080x1920 | - | - |

### Format Quick Guide
| Use Case | Best Format | Quality | Reason |
|----------|-------------|---------|--------|
| Web Photo | WebP | 85% | 30% smaller |
| Email | JPEG | 85% | Universal |
| Print | PNG/TIFF | 100% | Lossless |
| Transparency | WebP/PNG | 85-100% | Preserves alpha |
| Archive | PNG | 100% | Future-proof |

---

*Complete reference for platform specifications, quality settings, and error handling to ensure optimal image processing.*