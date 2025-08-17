# Imagician - Patterns & Workflows v1.1.0

Natural language patterns, operation mappings, multi-step workflows, mode-specific behaviors, and MCP intelligence integration.

## Table of Contents
1. [🧠 MCP INTELLIGENCE LAYER](#1--mcp-intelligence-layer)
2. [🎛️ MODE BEHAVIORS WITH MCP](#2-️-mode-behaviors-with-mcp)
3. [🎯 INTENT RECOGNITION](#3--intent-recognition)
4. [📐 SIZE OPERATIONS](#4--size-operations)
5. [🔄 FORMAT OPERATIONS](#5--format-operations)
6. [✂️ TRANSFORM OPERATIONS](#6-️-transform-operations)
7. [📦 BATCH OPERATIONS](#7--batch-operations)
8. [🔄 COMPLETE WORKFLOWS WITH MCP](#8--complete-workflows-with-mcp)
9. [💡 SMART DECISION TREES](#9--smart-decision-trees)

---

## 1. 🧠 MCP INTELLIGENCE LAYER

### MCP Selection by Complexity

| Complexity | MCP Choice | Thought Count | Characteristics |
|------------|------------|---------------|-----------------|
| **Simple** | Sequential | 2-3 | Single file, single operation, clear intent |
| **Medium** | Sequential | 3-4 | Single file, 2-3 operations, defined workflow |
| **Complex** | Cascade | 5-7 | Multiple files, conditional logic, exploration |
| **Exploratory** | Cascade | 5-7 | Vague request, multiple options, discovery needed |

### Operation to MCP Mapping

```yaml
Sequential Thinking Operations:
  - resize_image (single dimension)
  - convert_format (single format)
  - compress_image (target quality)
  - crop_image (defined region)
  - rotate_image (specific angle)
  - flip_image (direction)
  - get_image_info

Cascade Thinking Operations:
  - batch_resize (responsive sets)
  - Multi-platform optimization
  - Conditional batch processing
  - Web optimization workflow
  - Quality vs size exploration
  - Format selection analysis
```

### MCP Decision Factors

```yaml
Use Sequential When:
  - User intent is clear
  - Single operation requested
  - No exploration needed
  - Speed is priority
  - Path is deterministic
  
Use Cascade When:
  - Multiple possible approaches
  - Trade-offs need evaluation
  - Workflow planning required
  - Batch with conditions
  - User needs guidance
  - Quality optimization needed
```

---

## 2. 🎛️ MODE BEHAVIORS WITH MCP

### Interactive Mode ($interactive / $int) - DEFAULT
```yaml
behavior:
  - Conversational guidance
  - Ask clarifying questions
  - Explain operations before executing
  - Teach best practices
  - Suggest next steps

mcp_strategy:
  primary: Cascade Thinking (5-7 thoughts)
  fallback: Sequential (when path becomes clear)
  
triggers:
  - No mode specified
  - Vague requests
  - First-time users
  - Help keywords

example:
  User: "edit photo"
  System: [Cascade - 5 thoughts] "I'll help you edit that photo! What's your goal?"
```

### Quick Mode ($quick / $q)
```yaml
behavior:
  - Immediate execution
  - Minimal questions
  - Fast results
  - Brief confirmation

mcp_strategy:
  primary: Sequential Thinking (2-3 thoughts)
  never: Cascade (speed is priority)

triggers:
  - "$quick" prefix
  - Simple operations
  - Clear intent

example:
  User: "$q resize to 800px"
  System: [Sequential - 2 thoughts] "✓ Resized to 800px!"
```

### Batch Mode ($batch / $b)
```yaml
behavior:
  - Process multiple files
  - Show progress
  - Consistent settings
  - Bulk operations

mcp_strategy:
  simple_batch: Sequential (3-4 thoughts)
  complex_batch: Cascade (5-7 thoughts)
  conditional: Always Cascade

triggers:
  - "$batch" prefix
  - Multiple files mentioned
  - "all images" keywords

example:
  User: "$b compress all images"
  System: [Cascade if conditional] "Processing 12 images..." [Progress bar]
```

### Platform Mode ($platform / $p)
```yaml
behavior:
  - Social media focus
  - Platform presets
  - Multiple versions
  - Optimal specs

mcp_strategy:
  single_platform: Sequential (2-3 thoughts)
  multiple_platforms: Cascade (5-7 thoughts)

triggers:
  - "$platform" prefix
  - Platform names
  - "social media"

example:
  User: "$p instagram"
  System: [Sequential] "Creating Instagram-optimized versions..."
```

### Web Mode ($web / $w)
```yaml
behavior:
  - Web optimization
  - Responsive sets
  - Modern formats
  - Performance focus

mcp_strategy:
  primary: Cascade (5-7 thoughts)
  reason: Multiple sizes and formats

triggers:
  - "$web" prefix
  - "website" keywords
  - "responsive" mentions

example:
  User: "$w optimize"
  System: [Cascade] "Optimizing for web: WebP, 85%, responsive set..."
```

---

## 3. 🎯 INTENT RECOGNITION

### Ambiguous Intent Mapping with MCP

**"Make it smaller" (Sequential or Cascade)**
```yaml
mcp_selection:
  if_file_size_focus: Sequential (2 thoughts)
  if_unclear: Cascade (5 thoughts explore options)

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

**"Optimize this" (Cascade)**
```yaml
mcp: Cascade Thinking (6 thoughts)
explore:
  - Current use case
  - Size vs quality trade-offs
  - Format options
  - Platform requirements

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

**"Fix this image" (Cascade)**
```yaml
mcp: Cascade Thinking (5 thoughts)
analyze:
  - Check if too large (>10MB)
  - Check if wrong format
  - Check if poor quality
  - Explore correction options
  - Ask user for specific issue
```

---

## 4. 📐 SIZE OPERATIONS

### Resize Patterns with MCP

**Thumbnail Variations (Sequential)**
```yaml
mcp: Sequential (2-3 thoughts)
"thumbnail" | "thumb" | "small preview":
  micro: 50x50
  small: 100x100
  standard: 150x150
  medium: 200x200
  large: 300x300
  default: 150x150, fit: cover
```

**Responsive Image Sets (Cascade)**
```yaml
mcp: Cascade (5-7 thoughts)
"responsive" | "srcset" | "multiple sizes":
  planning_phase: Analyze breakpoints
  execution_phase:
    mobile: 320w, suffix: "-xs"
    mobile_2x: 640w, suffix: "-sm"
    tablet: 768w, suffix: "-md"
    desktop: 1024w, suffix: "-lg"
    full_hd: 1920w, suffix: "-xl"
    retina: 2560w, suffix: "-2xl"
    4k: 3840w, suffix: "-4k"
```

**Relative Sizing (Sequential)**
```yaml
mcp: Sequential (2 thoughts)
"half size": resize_image(width * 0.5, height * 0.5)
"quarter size": resize_image(width * 0.25, height * 0.25)
"double size": resize_image(width * 2, height * 2) + warning
"10% smaller": resize_image(width * 0.9, height * 0.9)
```

**Smart Constraints (Sequential or Cascade)**
```yaml
simple_constraint: Sequential (2 thoughts)
  "fit in 800x600":
    resize_image(800, 600, fit: "inside")

complex_constraint: Cascade (5 thoughts)
  "optimize for mobile":
    - Analyze current dimensions
    - Determine optimal mobile size
    - Consider retina displays
    - Apply smart cropping
```

---

## 5. 🔄 FORMAT OPERATIONS

### Format Selection Logic with MCP

**By Use Case (Cascade for exploration)**
```yaml
mcp: Cascade when multiple options exist

"for web" | "website ready":
  mcp: Cascade (explore WebP vs JPEG)
  format: WebP
  quality: 85
  reason: "30% smaller than JPEG"

"for email" | "email attachment":
  mcp: Sequential (clear choice)
  format: JPEG
  quality: 85
  reason: "Universal compatibility"

"for print" | "high quality":
  mcp: Sequential (clear requirement)
  format: PNG or TIFF
  quality: 100
  reason: "Lossless quality"

"for archive" | "backup":
  mcp: Sequential (preservation focus)
  format: PNG
  quality: 100
  reason: "Future-proof, lossless"
```

**By Characteristic (Sequential or Cascade)**
```yaml
"needs transparency" | "transparent background":
  mcp: Cascade if multiple formats possible
  modern: WebP
  compatible: PNG

"smallest file" | "maximum compression":
  mcp: Cascade (evaluate options)
  order: [AVIF, WebP, JPEG]
  quality: 70-80

"best quality" | "no compression":
  mcp: Sequential (clear requirement)
  format: PNG
  quality: 100
```

---

## 6. ✂️ TRANSFORM OPERATIONS

### Crop Patterns with MCP

**Aspect Ratios (Sequential)**
```yaml
mcp: Sequential (2 thoughts)

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

**Smart Cropping (Cascade)**
```yaml
mcp: Cascade (5 thoughts)

"crop to center":
  - Analyze image composition
  - Find visual center
  - Extract center 80%
  - Maintain aspect ratio

"remove borders":
  - Detect uniform edges
  - Calculate trim amount
  - Auto-trim borders

"focus on subject":
  - Identify main content
  - Calculate optimal crop
  - Center on main content
  - Add 10% padding
```

### Rotation Patterns (Sequential)

```yaml
mcp: Sequential (2 thoughts)

"rotate right" | "clockwise": rotate_image(90)
"rotate left" | "counter-clockwise": rotate_image(-90)
"upside down" | "180": rotate_image(180)
"straighten" | "level": detect and correct angle
"flip horizontal" | "mirror": flip_image("horizontal")
"flip vertical": flip_image("vertical")
```

---

## 7. 📦 BATCH OPERATIONS

### Multi-File Processing with MCP

**Same Operation to All (Sequential)**
```yaml
mcp: Sequential (3 thoughts)

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

**Conditional Batch (Cascade)**
```yaml
mcp: Cascade (6-7 thoughts)

"optimize large images":
  cascade_analysis:
    - Evaluate each image
    - Determine optimization needs
    - Apply conditional logic
  
  for_each_image:
    if size > 2MB:
      compress_image(80)
    if width > 2000:
      resize_image(1920)

"prepare photos for web":
  cascade_workflow:
    - Analyze format distribution
    - Plan conversion strategy
    - Optimize individually
  
  for_each_image:
    if not webp:
      convert_format("webp")
    if width > 1920:
      resize_image(1920)
```

**Organized Output (Cascade)**
```yaml
mcp: Cascade (5 thoughts)

batch_with_structure:
  planning:
    - Determine folder structure
    - Plan naming convention
    - Set up processing pipeline
    
  execution:
    input: /original/
    output: /processed/
      /thumbnails/
      /web/
      /social/
```

---

## 8. 🔄 COMPLETE WORKFLOWS WITH MCP

### Web Publishing Pipeline (Cascade)
```yaml
mcp: Cascade Thinking (6-7 thoughts)
trigger: "prepare for website" | "web ready" | "optimize for web"

cascade_planning:
  1_explore: Analyze image characteristics
  2_evaluate: Consider format options
  3_plan: Design optimization workflow
  4_decide: Choose best approach

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

### Social Media Kit (Cascade)
```yaml
mcp: Cascade Thinking (7 thoughts)
trigger: "social media set" | "all platforms" | "social kit"

cascade_analysis:
  - Identify required platforms
  - Map specifications
  - Plan crop strategies
  - Optimize for each

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

### Email Optimization (Sequential or Cascade)
```yaml
simple_email: Sequential (3 thoughts)
complex_email: Cascade (5 thoughts)

trigger: "email size" | "attachment ready" | "send via email"

workflow:
  1_check_size:
    if > 10MB:
      mcp: Cascade (needs strategy)
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

### Print Preparation (Sequential)
```yaml
mcp: Sequential (3 thoughts)
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

### Thumbnail Generation (Sequential or Cascade)
```yaml
simple_thumb: Sequential (2 thoughts)
gallery_thumbs: Cascade (5 thoughts)

trigger: "create thumbnails" | "preview images" | "gallery thumbs"

simple_workflow:
  1_determine_size:
    default: 150x150
    
  2_crop_and_resize:
    crop(fit: "cover")
    resize(150, 150)

gallery_workflow:
  cascade_planning:
    - Analyze image set
    - Determine optimal sizes
    - Plan generation strategy
    
  execution:
    sizes: [50, 100, 150, 200, 300]
    for_each_size:
      crop_resize_optimize
```

---

## 9. 💡 SMART DECISION TREES

### Format Selection with MCP
```yaml
decision_tree:
  cascade_when: Multiple viable options
  sequential_when: Clear best choice
  
  has_transparency?
    yes:
      need_smallest?
        cascade: Evaluate WebP vs PNG
        yes: WebP
        no: PNG
    no:
      is_photo?
        yes:
          for_web?
            cascade: Compare formats
            yes: WebP or JPEG
            no: JPEG
        no:
          has_text_or_lines?
            yes: PNG
            no: WebP or JPEG
```

### Quality Selection with MCP
```yaml
decision_tree:
  cascade_for: Trade-off evaluation
  sequential_for: Clear requirements
  
  use_case?
    archive: 100 [Sequential]
    print: 95-100 [Sequential]
    portfolio: 90-95 [Cascade - balance]
    web_hero: 85-90 [Cascade - optimize]
    web_standard: 80-85 [Sequential]
    thumbnail: 75-80 [Sequential]
    placeholder: 60-70 [Sequential]
```

### Compression Strategy with MCP
```yaml
cascade_when: Need optimal balance
sequential_when: Target is clear

target_size?
  under_100KB:
    mcp: Cascade (aggressive optimization)
    - Explore dimension reduction
    - Test quality levels
    - Find best approach
    
  under_500KB:
    mcp: Sequential (standard approach)
    - Max 800px
    - Quality 70-80
    
  under_1MB:
    mcp: Sequential
    - Max 1200px
    - Quality 80-85
    
  under_5MB:
    mcp: Sequential
    - Max 1920px
    - Quality 85-90
```

---

## 🎯 Pattern Matching Priority with MCP

1. **Mode check** → Apply mode-specific behavior and MCP
2. **Complexity assessment** → Choose Sequential or Cascade
3. **Exact match** → Platform-specific requests
4. **Category match** → Web, email, print
5. **Intent match** → Smaller, optimize, prepare
6. **Smart default** → Common scenarios
7. **Interactive fallback** → Ask user when unclear (Cascade)

## 📊 Success Metrics with MCP

- Match intent correctly 95% of time
- Select appropriate MCP 90% of time
- Apply optimal settings automatically
- Complete workflows without