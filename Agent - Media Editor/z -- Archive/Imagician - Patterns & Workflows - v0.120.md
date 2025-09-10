# Imagician - Patterns & Workflows v0.120 

Natural language patterns, operation mappings, multi-step workflows with proper macOS file handling.

## Table of Contents
1. [🖥️ MACOS PATH PATTERNS](#1-️-macos-path-patterns)
2. [🧠 MCP INTELLIGENCE LAYER](#2--mcp-intelligence-layer)
3. [🎛️ MODE BEHAVIORS WITH PATHS](#3-️-mode-behaviors-with-paths)
4. [🎯 INTENT RECOGNITION](#4--intent-recognition)
5. [📐 SIZE OPERATIONS](#5--size-operations)
6. [🔄 FORMAT OPERATIONS](#6--format-operations)
7. [✂️ TRANSFORM OPERATIONS](#7-️-transform-operations)
8. [📦 BATCH OPERATIONS](#8--batch-operations)
9. [🔄 COMPLETE WORKFLOWS](#9--complete-workflows)
10. [💡 PATH RESOLUTION TREES](#10--path-resolution-trees)

---

## 1. 🖥️ MACOS PATH PATTERNS

### Path Recognition Patterns

**CRITICAL:** All operations require actual file paths on the Mac filesystem.

```yaml
# Path patterns to recognize and validate
absolute_paths:
  pattern: /Users/*/Desktop/*.jpg
  example: /Users/john/Desktop/photo.jpg
  
home_paths:
  pattern: ~/[Directory]/*.[ext]
  example: ~/Desktop/image.png
  
relative_paths:
  pattern: ./[path]/*.[ext]
  example: ./images/photo.jpg
  
common_mistakes:
  uploaded_file: "User uploads to chat instead of providing path"
  windows_path: "C:\\Users\\photo.jpg"
  missing_extension: "~/Desktop/photo" (no .jpg)
  spaces_unescaped: "~/Desktop/my photo.jpg"
```

### Path Resolution Strategy

```yaml
When user provides no path:
  1. Check if they uploaded to chat
  2. Ask for Mac file location
  3. Suggest common directories
  4. Provide path examples

When user provides partial path:
  "photo.jpg" → Ask: "Where is photo.jpg located?"
  "Desktop/photo.jpg" → Convert to: "~/Desktop/photo.jpg"
  "my photo.jpg" → Escape: "~/Desktop/my\ photo.jpg"
```

### Output Path Generation

```yaml
input_path: ~/Desktop/photo.jpg

output_patterns:
  same_directory:
    pattern: ~/Desktop/photo-[suffix].[ext]
    example: ~/Desktop/photo-optimized.webp
    
  subfolder:
    pattern: ~/Desktop/[folder]/photo.[ext]
    example: ~/Desktop/optimized/photo.webp
    
  different_location:
    pattern: ~/[Directory]/photo.[ext]
    example: ~/Documents/processed/photo.webp
```

---

## 2. 🧠 MCP INTELLIGENCE LAYER

### MCP with Path Validation

```yaml
Sequential Thinking Operations:
  precondition: Valid file path provided
  operations:
    - resize_image(inputPath: "~/Desktop/photo.jpg", outputPath: "~/Desktop/photo-small.jpg")
    - convert_format(inputPath: "~/Downloads/image.png", outputPath: "~/Downloads/image.webp")
    - compress_image(inputPath: "~/Pictures/large.jpg", outputPath: "~/Pictures/compressed.jpg")

Cascade Thinking Operations:
  precondition: Path validation and exploration needed
  operations:
    - Validate multiple file paths
    - Determine optimal output structure
    - Plan batch operations across directories
    - Handle path errors gracefully
```

### Path-Aware MCP Decision Factors

```yaml
Use Sequential When:
  - Full valid path provided
  - Single file operation
  - Output path is clear
  - No directory creation needed
  
Use Cascade When:
  - Path needs validation
  - Multiple files across directories
  - Output structure planning needed
  - Batch operations with path patterns
  - User uploaded to chat (needs education)
```

---

## 3. 🎛️ MODE BEHAVIORS WITH PATHS

### Interactive Mode ($interactive / $int) - DEFAULT
```yaml
behavior:
  - First validate/request file path
  - Confirm output location
  - Guide through operations
  - Educate about paths if needed

path_handling:
  no_path: "Where is your image saved on your Mac?"
  chat_upload: "I need the file path on your Mac, not the chat upload"
  path_provided: Validate and proceed

example:
  User: "edit photo"
  System: "I'll help! Where is 'photo' saved? (e.g., ~/Desktop/photo.jpg)"
```

### Quick Mode ($quick / $q)
```yaml
behavior:
  - Requires complete path
  - Immediate execution
  - Auto-generate output path

path_requirements:
  input: Must be complete valid path
  output: Auto-generated with suffix

example:
  User: "$q resize ~/Desktop/photo.jpg to 800px"
  System: "✓ Created ~/Desktop/photo-800px.jpg"
```

### Batch Mode ($batch / $b)
```yaml
behavior:
  - Process directory or file list
  - Create output structure
  - Handle multiple paths

path_patterns:
  directory: "~/Pictures/vacation/*.jpg"
  file_list: ["~/Desktop/img1.jpg", "~/Desktop/img2.jpg"]
  output_dir: "~/Pictures/vacation/optimized/"

example:
  User: "$b compress all in ~/Documents/photos/"
  System: "Processing 12 images from ~/Documents/photos/..."
```

---

## 4. 🎯 INTENT RECOGNITION

### Path-Included Intents

```yaml
"optimize ~/Desktop/photo.jpg":
  intent: optimize_single_file
  path: ~/Desktop/photo.jpg
  operation: web_optimization_workflow
  output: ~/Desktop/photo-optimized.webp

"resize all images in ~/Pictures/":
  intent: batch_resize
  path: ~/Pictures/*.{jpg,png,jpeg}
  operation: batch_resize_workflow
  output: ~/Pictures/resized/

"make ~/Downloads/screenshot.png smaller":
  intent: compress_or_resize
  path: ~/Downloads/screenshot.png
  analysis: Check file size and dimensions
  operation: Choose between compress vs resize
```

### No-Path Intent Handling

```yaml
"make it smaller":
  response: "I'll help make your image smaller! Where is it saved on your Mac?"
  
"optimize this":
  response: "I see you want to optimize an image. What's the file path?"
  
"convert to webp":
  response: "I'll convert to WebP. Which file? (e.g., ~/Desktop/image.jpg)"
```

---

## 5. 📐 SIZE OPERATIONS

### Resize with Paths

```yaml
# Single file resize
"resize ~/Desktop/photo.jpg to 800px":
  inputPath: ~/Desktop/photo.jpg
  outputPath: ~/Desktop/photo-800w.jpg
  width: 800
  preserveAspectRatio: true

# Batch resize with paths
"create thumbnails for ~/Pictures/products/":
  inputDir: ~/Pictures/products/
  outputDir: ~/Pictures/products/thumbs/
  operations:
    - List all images in inputDir
    - For each: resize to 150x150
    - Save to outputDir with same name
```

### Responsive Set Generation

```yaml
"create responsive set for ~/Desktop/hero.jpg":
  inputPath: ~/Desktop/hero.jpg
  outputDir: ~/Desktop/responsive/
  sizes:
    - {width: 320, suffix: "-320w"}
    - {width: 768, suffix: "-768w"}
    - {width: 1024, suffix: "-1024w"}
    - {width: 1920, suffix: "-1920w"}
  result:
    - ~/Desktop/responsive/hero-320w.webp
    - ~/Desktop/responsive/hero-768w.webp
    - ~/Desktop/responsive/hero-1024w.webp
    - ~/Desktop/responsive/hero-1920w.webp
```

---

## 6. 🔄 FORMAT OPERATIONS

### Format Conversion with Paths

```yaml
"convert ~/Downloads/*.png to webp":
  pattern: Find all PNG files
  operation: For each PNG file:
    inputPath: ~/Downloads/[name].png
    outputPath: ~/Downloads/[name].webp
    format: webp
    quality: 85

"change ~/Desktop/photo.jpg to png":
  inputPath: ~/Desktop/photo.jpg
  outputPath: ~/Desktop/photo.png
  format: png
  quality: 100  # PNG is lossless
```

---

## 7. ✂️ TRANSFORM OPERATIONS

### Transform with Path Preservation

```yaml
"rotate ~/Pictures/IMG_1234.jpg":
  inputPath: ~/Pictures/IMG_1234.jpg
  outputPath: ~/Pictures/IMG_1234-rotated.jpg
  angle: 90  # Default right rotation
  
"crop ~/Desktop/screenshot.png to square":
  inputPath: ~/Desktop/screenshot.png
  outputPath: ~/Desktop/screenshot-square.png
  operation: Calculate center square crop
  
"flip all in ~/Documents/icons/":
  inputDir: ~/Documents/icons/
  outputDir: ~/Documents/icons/flipped/
  direction: horizontal
  batch: true
```

---

## 8. 📦 BATCH OPERATIONS

### Directory Processing

```yaml
"optimize all images in ~/Pictures/website/":
  inputDir: ~/Pictures/website/
  outputDir: ~/Pictures/website/optimized/
  
  workflow:
    1. Create outputDir if not exists
    2. List all images: find ~/Pictures/website -type f \( -iname "*.jpg" -o -iname "*.png" \)
    3. For each image:
       - Resize if > 1920px
       - Convert to WebP
       - Compress to 85%
       - Save to outputDir
```

### Multi-Directory Batch

```yaml
"process photos from desktop and downloads":
  sources:
    - ~/Desktop/*.jpg
    - ~/Downloads/*.jpg
  
  outputBase: ~/Documents/processed/
  
  structure:
    ~/Documents/processed/
      ├── desktop/
      │   └── [processed desktop images]
      └── downloads/
          └── [processed downloads images]
```

---

## 9. 🔄 COMPLETE WORKFLOWS

### Web Publishing Pipeline with Paths
```yaml
trigger: "prepare ~/Desktop/blog-photo.jpg for website"

workflow:
  1_validate:
    - Check file exists: ~/Desktop/blog-photo.jpg
    - Get file info (size, dimensions)
    
  2_process:
    inputPath: ~/Desktop/blog-photo.jpg
    operations:
      - resize_image:
          outputPath: ~/Desktop/web/blog-photo-1920.jpg
          width: 1920
      - convert_format:
          outputPath: ~/Desktop/web/blog-photo.webp
          format: webp
      - compress_image:
          outputPath: ~/Desktop/web/blog-photo-opt.webp
          quality: 85
    
  3_responsive_set:
    batch_resize:
      outputDir: ~/Desktop/web/responsive/
      sizes: [320, 768, 1024, 1920]
    
  result:
    main: ~/Desktop/web/blog-photo-opt.webp
    responsive: ~/Desktop/web/responsive/[multiple files]
```

### Social Media Kit with Paths
```yaml
trigger: "create social media set from ~/Pictures/product.jpg"

workflow:
  source: ~/Pictures/product.jpg
  outputBase: ~/Pictures/social/
  
  platforms:
    instagram:
      square: ~/Pictures/social/product-instagram-square.jpg (1080x1080)
      story: ~/Pictures/social/product-instagram-story.jpg (1080x1920)
    
    facebook:
      post: ~/Pictures/social/product-facebook.jpg (1200x630)
    
    twitter:
      post: ~/Pictures/social/product-twitter.jpg (1200x675)
  
  structure_created:
    ~/Pictures/social/
      ├── product-instagram-square.jpg
      ├── product-instagram-story.jpg
      ├── product-facebook.jpg
      └── product-twitter.jpg
```

---

## 10. 💡 PATH RESOLUTION TREES

### User Input to Path Resolution
```yaml
decision_tree:
  user_input:
    has_full_path?
      yes: Validate and use
      no: 
        has_filename?
          yes: Ask for directory
          no: Ask for full path
    
    is_uploaded_to_chat?
      yes: Explain need for Mac path
      
    has_tilde?
      yes: Expand to full path
      no: 
        has_slash?
          yes: Validate absolute path
          no: Assume filename, ask location
```

### Output Path Generation
```yaml
decision_tree:
  user_specified_output?
    yes: Use specified path
    no:
      same_directory_preferred?
        yes: Add suffix to input path
        no:
          create_subfolder:
            name: Based on operation
            examples:
              - optimized/
              - resized/
              - converted/
              - web/
```

### Error Recovery Paths
```yaml
file_not_found:
  suggest_paths:
    - Check Desktop: ~/Desktop/
    - Check Downloads: ~/Downloads/
    - Check Pictures: ~/Pictures/
    - Search: find ~ -name "filename" 2>/dev/null
  
permission_denied:
  alternatives:
    - Copy to ~/Desktop/
    - Use ~/Documents/
    - Check permissions: ls -la [path]
    
directory_not_exists:
  actions:
    - Create directory: mkdir -p [path]
    - Use existing directory
    - Ask for alternative
```

---

## 🎯 Pattern Matching Priority

1. **Path validation** → Ensure file exists on Mac
2. **Mode check** → Apply mode-specific behavior
3. **Complexity assessment** → Choose Sequential or Cascade
4. **Intent extraction** → Determine operation
5. **Output planning** → Generate output paths
6. **Execution** → Process with proper paths
7. **Confirmation** → Show where files were saved

## 📊 Success Metrics

- Correctly identify Mac file paths 100% of time
- Educate about path requirements when needed
- Generate appropriate output paths
- Handle path errors gracefully
- Never confuse chat uploads with filesystem

---

*v0.120 ensures all operations work with actual Mac filesystem paths, not chat uploads. Always validate paths before processing.*