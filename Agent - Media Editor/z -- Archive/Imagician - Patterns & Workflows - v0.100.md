# Imagician - Patterns & Workflows v0.100

Natural language patterns, operation mappings, multi-step workflows, and mode-specific behaviors.

## Table of Contents
1. [🎛️ MODE BEHAVIORS](#1-️-mode-behaviors)
2. [🎯 INTENT RECOGNITION](#2--intent-recognition)
3. [📐 SIZE OPERATIONS](#3--size-operations)
4. [🔄 FORMAT OPERATIONS](#4--format-operations)
5. [✂️ TRANSFORM OPERATIONS](#5-️-transform-operations)
6. [📦 BATCH OPERATIONS](#6--batch-operations)
7. [🔄 COMPLETE WORKFLOWS](#7--complete-workflows)
8. [💡 SMART DECISION TREES](#8--smart-decision-trees)

---

## 1. 🎛️ MODE BEHAVIORS

### Interactive Mode ($interactive / $int) - DEFAULT
```yaml
behavior:
  - Conversational guidance
  - Ask clarifying questions
  - Explain operations before executing
  - Teach best practices
  - Suggest next steps

triggers:
  - No mode specified
  - Vague requests
  - First-time users
  - Help keywords

example:
  User: "edit photo"
  System: "I'll help you edit that photo! What's your goal?"
```

### Quick Mode ($quick / $q)
```yaml
behavior:
  - Immediate execution
  - Minimal questions
  - Fast results
  - Brief confirmation

triggers:
  - "$quick" prefix
  - Simple operations
  - Clear intent

example:
  User: "$q resize to 800px"
  System: [Executes immediately] "✓ Resized to 800px!"
```

### Batch Mode ($batch / $b)
```yaml
behavior:
  - Process multiple files
  - Show progress
  - Consistent settings
  - Bulk operations

triggers:
  - "$batch" prefix
  - Multiple files mentioned
  - "all images" keywords

example:
  User: "$b compress all images"
  System: "Processing 12 images..." [Progress bar]
```

### Platform Mode ($platform / $p)
```yaml
behavior:
  - Social media focus
  - Platform presets
  - Multiple versions
  - Optimal specs

triggers:
  - "$platform" prefix
  - Platform names
  - "social media"

example:
  User: "$p instagram"
  System: "Creating Instagram-optimized versions..."
```

### Web Mode ($web / $w)
```yaml
behavior:
  - Web optimization
  - Responsive sets
  - Modern formats
  - Performance focus

triggers:
  - "$web" prefix
  - "website" keywords
  - "responsive" mentions

example:
  User: "$w optimize"
  System: "Optimizing for web: WebP, 85%, responsive set..."
```

---

## 2. 🎯 INTENT RECOGNITION

### Ambiguous Intent Mapping

**"Make it smaller"**
```yaml
decision_tree:
  check_file_size:
    if > 5MB: compress_image(quality: 80)
    elif > 2MB: compress_image(quality: 85)
  
  check_dimensions:
    if width > 3000: resize_image(width: 1920)
    elif width > 2000: resize_image(width: 1600)
  
  default:
    compress_image(quality: 85)
```

**"Optimize this"**
```yaml
for_web:
  - resize_image(max: 1920)
  - convert_format("webp")
  - compress_image(85)

for_email:
  - resize_image(max: 1024)
  - compress_image(until < 5MB)

for_social:
  - resize to platform specs
  - optimize quality
```

**"Fix this image"**
```yaml
analyze:
  - Check if too large (>10MB)
  - Check if wrong format
  - Check if poor quality
  - Ask user for specific issue
```

---

## 3. 📐 SIZE OPERATIONS

### Resize Patterns

**Thumbnail Variations**
```yaml
"thumbnail" | "thumb" | "small preview":
  micro: 50x50
  small: 100x100
  standard: 150x150
  medium: 200x200
  large: 300x300
  default: 150x150, fit: cover

"icon" | "avatar":
  standard: 512x512
  small: 256x256
  tiny: 64x64
```

**Responsive Image Sets**
```yaml
"responsive" | "srcset" | "multiple sizes":
  mobile: 320w, suffix: "-xs"
  mobile_2x: 640w, suffix: "-sm"
  tablet: 768w, suffix: "-md"
  desktop: 1024w, suffix: "-lg"
  full_hd: 1920w, suffix: "-xl"
  retina: 2560w, suffix: "-2xl"
  4k: 3840w, suffix: "-4k"
```

**Relative Sizing**
```yaml
"half size": resize_image(width * 0.5, height * 0.5)
"quarter size": resize_image(width * 0.25, height * 0.25)
"double size": resize_image(width * 2, height * 2) + warning
"10% smaller": resize_image(width * 0.9, height * 0.9)
```

**Smart Constraints**
```yaml
"fit in 800x600":
  resize_image(800, 600, fit: "inside")

"fill 1920x1080":
  resize_image(1920, 1080, fit: "cover")

"max 1000 pixels":
  resize_image(max_dimension: 1000)
```

---

## 4. 🔄 FORMAT OPERATIONS

### Format Selection Logic

**By Use Case**
```yaml
"for web" | "website ready":
  format: WebP
  quality: 85
  reason: "30% smaller than JPEG"

"for email" | "email attachment":
  format: JPEG
  quality: 85
  reason: "Universal compatibility"

"for print" | "high quality":
  format: PNG or TIFF
  quality: 100
  reason: "Lossless quality"

"for archive" | "backup":
  format: PNG
  quality: 100
  reason: "Future-proof, lossless"
```

**By Characteristic**
```yaml
"needs transparency" | "transparent background":
  modern: WebP
  compatible: PNG

"smallest file" | "maximum compression":
  order: [AVIF, WebP, JPEG]
  quality: 70-80

"best quality" | "no compression":
  format: PNG
  quality: 100
```

---

## 5. ✂️ TRANSFORM OPERATIONS

### Crop Patterns

**Aspect Ratios**
```yaml
"square" | "1:1":
  crop to 1:1 ratio
  common: profile pictures

"landscape" | "wide" | "16:9":
  crop to 16:9 ratio
  common: videos, presentations

"portrait" | "tall" | "9:16":
  crop to 9:16 ratio
  common: stories, reels

"golden ratio":
  crop to 1.618:1
  aesthetic composition
```

**Smart Cropping**
```yaml
"crop to center":
  extract center 80%
  maintain aspect ratio

"remove borders":
  detect uniform edges
  auto-trim borders

"focus on subject":
  center on main content
  add 10% padding
```

### Rotation Patterns

```yaml
"rotate right" | "clockwise": rotate_image(90)
"rotate left" | "counter-clockwise": rotate_image(-90)
"upside down" | "180": rotate_image(180)
"straighten" | "level": detect and correct angle
"flip horizontal" | "mirror": flip_image("horizontal")
"flip vertical": flip_image("vertical")
```

---

## 6. 📦 BATCH OPERATIONS

### Multi-File Processing

**Same Operation to All**
```yaml
"resize all to 800px":
  for_each_image:
    resize_image(800, maintain_aspect)

"convert all to WebP":
  for_each_image:
    convert_format("webp", quality: 85)

"compress everything":
  for_each_image:
    compress_image(quality: 80)
```

**Conditional Batch**
```yaml
"optimize large images":
  for_each_image:
    if size > 2MB:
      compress_image(80)
    if width > 2000:
      resize_image(1920)

"prepare photos for web":
  for_each_image:
    if not webp:
      convert_format("webp")
    if width > 1920:
      resize_image(1920)
```

**Organized Output**
```yaml
batch_with_structure:
  input: /original/
  output: /processed/
    /thumbnails/
    /web/
    /social/
```

---

## 7. 🔄 COMPLETE WORKFLOWS

### Web Publishing Pipeline
```yaml
trigger: "prepare for website" | "web ready" | "optimize for web"

steps:
  1_analyze:
    - Check current format
    - Check dimensions
    - Check file size
    
  2_resize:
    if width > 1920:
      resize_image(1920, maintain_aspect)
    
  3_convert:
    if not webp:
      convert_format("webp")
    
  4_compress:
    compress_image(quality: 85, progressive: true)
    
  5_responsive (optional):
    batch_resize([320, 768, 1024, 1920])
    
result: "Web-optimized with optional responsive set"
```

### Social Media Kit
```yaml
trigger: "social media set" | "all platforms" | "social kit"

platforms:
  instagram:
    square: 1080x1080
    story: 1080x1920
    
  facebook:
    post: 1200x630
    cover: 820x312
    
  twitter:
    post: 1200x675
    header: 1500x500
    
  linkedin:
    post: 1200x627
    banner: 1584x396

workflow:
  for_each_platform:
    1. crop_image(aspect_ratio)
    2. resize_image(dimensions)
    3. compress_image(quality: 90)
    4. save_with_suffix("-platform")
```

### Email Optimization
```yaml
trigger: "email size" | "attachment ready" | "send via email"

workflow:
  1_check_size:
    if > 10MB:
      aggressive: true
      
  2_resize:
    max_dimension: 1024
    maintain_aspect: true
    
  3_compress:
    if aggressive:
      quality: 70
    else:
      quality: 85
      
  4_verify:
    ensure size < 5MB
    if not: reduce_quality further
    
  5_format:
    if not jpeg:
      convert_format("jpeg")
```

### Print Preparation
```yaml
trigger: "for print" | "print quality" | "high resolution"

workflow:
  1_check_resolution:
    ensure >= 300 DPI
    warn if < 300 DPI
    
  2_format:
    convert_format("png" or "tiff")
    
  3_color:
    maintain color profile
    suggest CMYK for professional
    
  4_quality:
    maximum quality (100)
    no compression
```

### Thumbnail Generation
```yaml
trigger: "create thumbnails" | "preview images" | "gallery thumbs"

workflow:
  1_determine_size:
    default: 150x150
    options: [50, 100, 150, 200, 300]
    
  2_crop:
    fit: "cover"
    center: true
    
  3_resize:
    to selected size
    
  4_optimize:
    quality: 80
    format: keep or convert to jpeg
    
  5_naming:
    add suffix: "-thumb"
```

---

## 8. 💡 SMART DECISION TREES

### Format Selection
```yaml
decision_tree:
  has_transparency?
    yes:
      need_smallest?
        yes: WebP
        no: PNG
    no:
      is_photo?
        yes:
          for_web?
            yes: WebP or JPEG
            no: JPEG
        no:
          has_text_or_lines?
            yes: PNG
            no: WebP or JPEG
```

### Quality Selection
```yaml
decision_tree:
  use_case?
    archive: 100
    print: 95-100
    portfolio: 90-95
    web_hero: 85-90
    web_standard: 80-85
    thumbnail: 75-80
    placeholder: 60-70
```

### Compression Strategy
```yaml
target_size?
  under_100KB:
    - Resize to thumbnail
    - Quality 60-70
    
  under_500KB:
    - Max 800px
    - Quality 70-80
    
  under_1MB:
    - Max 1200px
    - Quality 80-85
    
  under_5MB:
    - Max 1920px
    - Quality 85-90
```

---

## 🎯 Pattern Matching Priority

1. **Mode check** → Apply mode-specific behavior
2. **Exact match** → Platform-specific requests
3. **Category match** → Web, email, print
4. **Intent match** → Smaller, optimize, prepare
5. **Smart default** → Common scenarios
6. **Interactive fallback** → Ask user when unclear

## 📊 Success Metrics

- Match intent correctly 95% of time
- Apply optimal settings automatically
- Complete workflows without interruption
- Preserve quality when possible
- Educate through action (in interactive mode)

---

*This pattern library enables natural language understanding and intelligent workflow execution for all image editing requests across all operational modes.*