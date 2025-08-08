# Imagician - Platform Specs & Defaults v1.2.0

Complete specifications with proper macOS file handling for Claude Desktop.

## Table of Contents
1. [🖥️ MACOS FILE SYSTEM SPECS](#1-️-macos-file-system-specs)
2. [🌐 PLATFORM SPECIFICATIONS](#2--platform-specifications)
3. [📊 QUALITY & FORMAT DEFAULTS](#3--quality--format-defaults)
4. [🧠 MCP INTELLIGENCE NOTES](#4--mcp-intelligence-notes)
5. [🚨 ERROR HANDLING](#5--error-handling)
6. [💡 BEST PRACTICES](#6--best-practices)

---

## 1. 🖥️ MACOS FILE SYSTEM SPECS

### Critical Understanding
**Imagician MCP operates on your Mac's filesystem, NOT on files uploaded to Claude's chat interface.**

### macOS Directory Structure
```yaml
# Standard user directories
Desktop: /Users/[username]/Desktop/
Downloads: /Users/[username]/Downloads/
Documents: /Users/[username]/Documents/
Pictures: /Users/[username]/Pictures/
Movies: /Users/[username]/Movies/
Music: /Users/[username]/Music/

# Using tilde expansion (recommended)
Desktop: ~/Desktop/
Downloads: ~/Downloads/
Documents: ~/Documents/
Pictures: ~/Pictures/

# Special directories
iCloud Drive: ~/Library/Mobile Documents/com~apple~CloudDocs/
Screenshots: ~/Desktop/ (default)
Applications: /Applications/
Temp: /tmp/ or /var/tmp/
```

### Valid Path Formats
```yaml
absolute_path:
  format: /Users/[username]/[path]/[file].[ext]
  example: /Users/john/Desktop/photo.jpg
  use_when: Clarity needed, scripts, automation

home_path:
  format: ~/[path]/[file].[ext]
  example: ~/Desktop/image.png
  use_when: Most common, portable, recommended

relative_path:
  format: ./[path]/[file].[ext]
  example: ./images/photo.jpg
  use_when: Working within project directory

parent_path:
  format: ../[path]/[file].[ext]
  example: ../Downloads/image.jpg
  use_when: Accessing parent directories
```

### Path Escaping Rules
```yaml
spaces_in_path:
  wrong: ~/Desktop/my photo.jpg
  correct: ~/Desktop/my\ photo.jpg
  alternative: "~/Desktop/my photo.jpg"  # Quote entire path

special_characters:
  apostrophe: John\'s\ Photo.jpg
  parentheses: Photo\ \(1\).jpg
  ampersand: Photo\ \&\ Video.jpg
  
wildcards:
  all_jpg: ~/Desktop/*.jpg
  all_images: ~/Pictures/*.{jpg,png,jpeg,webp}
  recursive: ~/Documents/**/*.jpg
```

### File Permissions
```yaml
check_permissions:
  command: ls -la ~/Desktop/photo.jpg
  output: -rw-r--r--  1 username  staff  2048576 Jan 1 12:00 photo.jpg
  
fix_permissions:
  read: chmod +r ~/Desktop/photo.jpg
  write: chmod +w ~/Desktop/photo.jpg
  execute: chmod +x ~/Desktop/script.sh
```

---

## 2. 🌐 PLATFORM SPECIFICATIONS

### Social Media Platforms (with Path Examples)

#### Instagram
```yaml
post_square:
  dimensions: 1080x1080
  inputPath: ~/Pictures/photo.jpg
  outputPath: ~/Pictures/social/photo-instagram-square.jpg
  
story:
  dimensions: 1080x1920
  inputPath: ~/Pictures/photo.jpg
  outputPath: ~/Pictures/social/photo-instagram-story.jpg
  
example_command:
  resize: inputPath: "~/Desktop/photo.jpg", outputPath: "~/Desktop/photo-ig.jpg", width: 1080, height: 1080
```

#### Output Directory Structure
```yaml
recommended_structure:
  ~/Pictures/social-media/
    ├── instagram/
    │   ├── posts/
    │   ├── stories/
    │   └── reels/
    ├── facebook/
    ├── twitter/
    └── linkedin/
```

---

## 3. 📊 QUALITY & FORMAT DEFAULTS

### Quality Levels with Path Handling

```yaml
archival:
  quality: 100
  format: PNG or TIFF
  typical_path: ~/Pictures/archive/[filename]-master.png
  size_warning: "May create very large files (50MB+)"
  
web_optimized:
  quality: 85
  format: WebP
  typical_path: ~/Desktop/web/[filename]-web.webp
  batch_path: ~/Documents/website/images/optimized/
  
thumbnail:
  quality: 75
  dimensions: 150x150
  typical_path: ~/Desktop/thumbs/[filename]-thumb.jpg
  batch_output: ~/Pictures/gallery/thumbnails/
```

---

## 4. 🧠 MCP INTELLIGENCE NOTES

### Path Validation with MCP

**Sequential Thinking:**
```yaml
valid_path_provided:
  example: "resize ~/Desktop/photo.jpg to 800px"
  process:
    - Direct execution
    - Auto-generate output path
    - 2-3 thoughts total
```

**Cascade Thinking:**
```yaml
no_path_or_complex:
  example: "optimize all my photos"
  process:
    - Ask for directory location
    - Explore subdirectories
    - Plan output structure
    - 5-7 thoughts total
```

### Batch Operations Intelligence

```yaml
cascade_for_batch:
  input_discovery:
    - Find all images in directory
    - Check subdirectories if needed
    - Filter by format if specified
  
  output_planning:
    - Create organized structure
    - Prevent overwrites
    - Generate meaningful names
  
  example:
    input: ~/Pictures/vacation/
    process: Find all .jpg files
    output: ~/Pictures/vacation/web-ready/
```

---

## 5. 🚨 ERROR HANDLING

### File Path Errors

#### File Not Found
```yaml
error: "Cannot locate file"
inputPath: ~/Desktop/photo.jpg

interactive_response: |
  ❌ Can't find: ~/Desktop/photo.jpg
  
  Let's troubleshoot:
  1. Check exact spelling (case-sensitive on Mac)
  2. Verify location - try: ls ~/Desktop/*.jpg
  3. If spaces in name: ~/Desktop/my\ photo.jpg
  
  Common locations to check:
  • Downloads: ~/Downloads/
  • Pictures: ~/Pictures/
  • Documents: ~/Documents/
  • iCloud: ~/Library/Mobile Documents/com~apple~CloudDocs/
  
  What's the correct path?

quick_response: |
  ❌ File not found: ~/Desktop/photo.jpg
  Check: ls ~/Desktop/*.jpg
```

#### Chat Upload Confusion
```yaml
trigger: User uploads image to chat interface

response: |
  💡 I see you've uploaded an image to our chat!
  
  However, I need to work with files saved on your Mac.
  The Imagician tool processes local files, not chat uploads.
  
  Please:
  1. Save the image to your Mac (e.g., Desktop)
  2. Tell me the path: ~/Desktop/yourimage.jpg
  3. Then I can process it
  
  Where did you save the image on your Mac?
```

#### Permission Denied
```yaml
error: "Permission denied"
path: /System/Library/image.jpg

response: |
  ⚠️ Cannot access: /System/Library/image.jpg
  
  This is a protected system directory.
  
  Solutions:
  1. Copy to your Desktop: cp /System/Library/image.jpg ~/Desktop/
  2. Use your user directories: ~/Desktop/, ~/Documents/, ~/Pictures/
  3. Check permissions: ls -la /System/Library/image.jpg
  
  Try copying to: ~/Desktop/image.jpg
```

#### Directory Doesn't Exist
```yaml
error: "Directory not found"
outputPath: ~/Desktop/processed/image.jpg

response: |
  📁 Output directory doesn't exist: ~/Desktop/processed/
  
  Should I:
  1. Create it: mkdir ~/Desktop/processed/
  2. Use Desktop directly: ~/Desktop/image-processed.jpg
  3. Use different location?
  
  What would you prefer?
```

### Path Format Issues

#### Windows Path Provided
```yaml
input: "C:\Users\John\Desktop\photo.jpg"

response: |
  🖥️ That looks like a Windows path!
  
  On Mac, use:
  • ~/Desktop/photo.jpg
  • /Users/[yourusername]/Desktop/photo.jpg
  
  Where is the file on your Mac?
```

#### Missing File Extension
```yaml
input: "~/Desktop/photo"

response: |
  📝 Missing file extension
  
  Is it:
  • ~/Desktop/photo.jpg
  • ~/Desktop/photo.png
  • ~/Desktop/photo.jpeg
  
  Check with: ls ~/Desktop/photo*
```

---

## 6. 💡 BEST PRACTICES

### Path Management Best Practices

```yaml
always_validate:
  before_processing: Check file exists
  after_processing: Confirm output created
  batch_operations: Validate all input files first

organize_outputs:
  single_file: Add suffix (photo-optimized.jpg)
  multiple_files: Create subfolder (/optimized/)
  batch_processing: Maintain structure
  
  example_structure:
    ~/Pictures/
      ├── originals/
      ├── optimized/
      ├── thumbnails/
      └── social-media/

avoid_overwrites:
  check_first: "File exists, overwrite?"
  auto_rename: photo-2.jpg, photo-3.jpg
  use_timestamps: photo-20240108-143022.jpg
```

### Quick Commands Reference

```bash
# List images in directory
ls ~/Desktop/*.{jpg,png,jpeg,webp}

# Find image files
find ~/Pictures -name "*.jpg" -type f

# Check file info
file ~/Desktop/photo.jpg

# Check file size
du -h ~/Desktop/photo.jpg

# Create directory
mkdir -p ~/Desktop/optimized

# Copy file
cp ~/Downloads/photo.jpg ~/Desktop/

# Move file
mv ~/Downloads/photo.jpg ~/Desktop/

# Check permissions
ls -la ~/Desktop/photo.jpg
```

### Common Workflows with Paths

```yaml
single_file_optimization:
  input: ~/Desktop/photo.jpg
  commands:
    - resize: ~/Desktop/photo-1920.jpg
    - convert: ~/Desktop/photo.webp
    - compress: ~/Desktop/photo-compressed.jpg

batch_web_optimization:
  input: ~/Pictures/website/*.jpg
  output: ~/Pictures/website/optimized/
  operations:
    - Resize to max 1920px
    - Convert to WebP
    - 85% quality

social_media_kit:
  input: ~/Pictures/profile.jpg
  output_structure:
    ~/Pictures/social/
      ├── profile-instagram.jpg
      ├── profile-facebook.jpg
      ├── profile-twitter.jpg
      └── profile-linkedin.jpg
```

---

## 📊 Quick Reference Tables

### macOS Directories At-a-Glance
| Directory | Path | Shortcut | Common Use |
|-----------|------|----------|------------|
| Desktop | ~/Desktop/ | ⌘⇧D | Quick access |
| Downloads | ~/Downloads/ | ⌥⌘L | Downloaded files |
| Documents | ~/Documents/ | ⌘⇧O | Project files |
| Pictures | ~/Pictures/ | - | Photo library |
| iCloud | ~/Library/Mobile Documents/com~apple~CloudDocs/ | - | Cloud sync |

### Path Patterns Quick Guide
| Pattern | Example | Meaning |
|---------|---------|---------|
| ~/ | ~/Desktop/ | Home directory |
| ./ | ./images/ | Current directory |
| ../ | ../Pictures/ | Parent directory |
| * | *.jpg | All matching files |
| {a,b} | *.{jpg,png} | Multiple extensions |
| ** | **/*.jpg | Recursive search |

### Error Resolution Quick Guide
| Error | Quick Fix | Command |
|-------|-----------|---------|
| File not found | Check spelling | ls ~/Desktop/*.jpg |
| Permission denied | Copy to Desktop | cp [file] ~/Desktop/ |
| Directory missing | Create it | mkdir -p [path] |
| Wrong path format | Use ~/ notation | ~/Desktop/photo.jpg |

---

*v1.2.0 ensures all operations work with macOS filesystem paths. Never confuse chat uploads with local files. Always validate paths before processing.*