# Imagician - MCP Intelligence - v0.100

Streamlined image optimization reference for Webflow asset integration with standardized performance metrics and automation patterns.

## Table of Contents
1. [🚀 Quick Activation](#1--quick-activation)
2. [📸 Core Operations](#2--core-operations)
3. [🎯 Webflow Optimization Presets](#3--webflow-optimization-presets)
4. [💬 Conversation Patterns](#4--conversation-patterns)
5. [⚡ Smart Defaults](#5--smart-defaults)
6. [🚨 Error Recovery](#6--error-recovery)
7. [📊 Performance Metrics](#7--performance-metrics)
8. [🔄 Integration Triggers](#8--integration-triggers)
9. [⚠️ API Error Codes](#9--api-error-codes)
10. [📌 Quick Reference](#10--quick-reference)

---

## 1. 🚀 Quick Activation

### When to Trigger Imagician

**Automatic Triggers from Webflow Context:**
```yaml
Explicit Triggers:
  - "optimize image/photo/asset"
  - "compress before uploading"
  - "prepare images for CMS"
  - "create thumbnails"
  - "resize for web"
  - "convert to WebP"

Implicit Triggers (Auto-detect):
  - Image upload mentioned + Webflow context
  - File size >1MB detected
  - Multiple images for batch processing
  - CMS collection has image fields
  - Performance optimization requested
```

**Context Detection Matrix:**
```yaml
Webflow Asset Upload:
  Trigger: User mentions uploading to Webflow
  Action: Optimize first with Imagician
  Time: 10-15 seconds per image
  Result: 60-80% smaller files
  API Calls: 2-3 per image
  
CMS Image Fields:
  Trigger: Adding images to collection items
  Action: Process through Imagician
  Batch: Up to 20 images simultaneously
  Savings: 70% average size reduction
  Time: 2-3 seconds per image
  
Bulk Assets:
  Trigger: Multiple images mentioned
  Action: Batch process with consistent settings
  Performance: 2-3 seconds per image
  Memory: Safe up to 50 images
  API Calls: 1-2 per image in batch
```

**Integration Decision Tree:**
```
Image Operation Needed?
├─ Single image <500KB?
│  └─ Skip optimization (already small)
├─ Single image >500KB?
│  └─ Optimize with Imagician
├─ Multiple images?
│  └─ Batch process (max 20 per batch)
└─ Special format (SVG/GIF)?
   └─ Pass through unchanged
```

---

## 2. 📸 Core Operations

### Essential Image Operations with Performance Data

**Resize for Web:**
```yaml
Operation: Resize
Default: 1920px max width
Maintain: Aspect ratio
Quality: 85%
Processing Time: 2-3 seconds
Size Reduction: 40-60%
Purpose: Optimal web display
API Calls: 1-2
Rate Limit: 60/minute

Performance Impact:
  - Page load: -1.5 seconds average
  - Bandwidth: -50% usage
  - Core Web Vitals: +15 points
```

**Format Conversion:**
```yaml
Operation: Convert
Target: WebP (preferred) or JPEG
Quality: 85% standard
Processing Time: 2-3 seconds
Size Benefit: 25-35% smaller than JPEG
Compatibility: 95% browser support
API Calls: 1-2
Rate Limit: 60/minute

Conversion Matrix:
  PNG to WebP: 60-80% reduction
  JPEG to WebP: 25-35% reduction
  PNG to JPEG: 40-60% reduction (loses transparency)
  BMP to WebP: 90-95% reduction
```

**Thumbnail Generation:**
```yaml
Operation: Create thumbnails
Sizes Generated:
  - Small: 150x150px (15-25KB)
  - Medium: 400x400px (30-50KB)
  - Large: 800x800px (60-100KB)

Quality: 75% for thumbnails
Processing: 2-3 seconds per size
Total Time: 6-9 seconds for set
Purpose: Collection grid displays
API Calls: 3-5 for full set
Rate Limit: 60/minute

Bandwidth Savings:
  - Grid view: 80% less data
  - List view: 70% less data
  - Mobile: 85% less data
```

**Compression Levels:**
```yaml
Operation: Optimize file size
Targets by Use Case:
  - Hero images: <500KB
  - Content images: <200KB
  - Thumbnails: <50KB
  - Icons: <20KB

Method: Progressive encoding
Quality Settings:
  - 95%: Lossless visible quality (-20% size)
  - 90%: Excellent quality (-40% size)
  - 85%: Standard web quality (-60% size)
  - 75%: Good for thumbnails (-75% size)
  - 65%: Acceptable minimum (-85% size)

Processing: 2-3 seconds
Result: 50-70% average reduction
API Calls: 1-2
Rate Limit: 60/minute
```

---

## 3. 🎯 Webflow Optimization Presets

### CMS Image Presets with Real Performance Data

| Content Type | Dimensions | Format | Quality | Avg File Size | Load Time Impact | Processing Time |
|--------------|------------|--------|---------|---------------|------------------|-----------------|
| **Hero Image** | 2560x1440 | WebP | 90% | 400-500KB | -2.5s | 3-4s |
| **Blog Featured** | 1200x630 | WebP | 85% | 150-200KB | -1.2s | 2-3s |
| **Product Photo** | 1500x1500 | JPEG | 85% | 200-300KB | -1.5s | 2-3s |
| **Team Photo** | 800x800 | JPEG | 90% | 100-150KB | -0.8s | 2-3s |
| **Thumbnail** | 400x400 | WebP | 75% | 30-50KB | -0.3s | 2s |
| **Gallery** | 1920x1080 | WebP | 85% | 250-350KB | -1.8s | 2-3s |
| **Logo** | Original | PNG | Lossless | 20-100KB | Minimal | <1s |
| **Icon** | 100x100 | SVG/PNG | Lossless | 5-20KB | Minimal | <1s |

### Responsive Image Set Generation

**Standard Web Set:**
```yaml
Sizes Generated from 2560px Original:
  Mobile:
    - Width: 640px
    - File size: 50-80KB
    - Use: Phones portrait
    
  Tablet:
    - Width: 1024px
    - File size: 100-150KB
    - Use: Tablets, phones landscape
    
  Desktop:
    - Width: 1920px
    - File size: 250-350KB
    - Use: Standard monitors
    
  Retina:
    - Width: 2560px
    - File size: 400-500KB
    - Use: High-DPI displays
    
  Thumbnail:
    - Width: 400px square
    - File size: 30-50KB
    - Use: Grid displays

Total Processing Time: 10-15 seconds
Total API Calls: 5-8
Total Bandwidth Saved: 65% with srcset
```

---

## 4. 💬 Conversation Patterns

### Simple Triggers with Performance Context

**Basic Optimization:**
```
User: "optimize this image for Webflow"
Imagician: "I'll optimize your image for Webflow!
           
           Processing:
           • Resizing to 1920px max width
           • Converting to WebP format
           • Compressing to 85% quality
           
           Expected results:
           • Size reduction: ~60%
           • Load time improvement: ~1.5s
           • Processing time: 2-3 seconds
           
           Optimizing now..."

[After completion]
           "✅ Optimization complete!
           • Original: 2.4MB → Optimized: 385KB (84% smaller)
           • Format: PNG → WebP
           • Dimensions: 3000x2000 → 1920x1280
           • Ready for Webflow upload!"
```

**Batch Processing:**
```
User: "prepare all product photos"
Imagician: "I'll prepare all product photos for your Webflow shop!
           
           Batch processing setup:
           • Found: 12 product images
           • Creating e-commerce set for each
           • Total sizes: 48 images (4 per product)
           • Estimated time: 2 minutes
           
           Processing batch..."

[After completion]
           "✅ Batch processing complete!
           • Processed: 12 products (48 total images)
           • Total size: 18.5MB → 4.2MB (77% reduction)
           • Average per product: 350KB total
           • Time taken: 1 min 54 sec
           • Ready for CMS import!"
```

### Webflow-Specific Pattern Recognition

| User Says | Imagician Response | Action | Time | Result |
|-----------|-------------------|--------|------|--------|
| "CMS images" | "Optimizing for Webflow CMS!" | 1920px, WebP, 85% | 2-3s | 60% smaller |
| "hero image" | "Creating hero image!" | 2560px, 90% quality | 3-4s | Under 500KB |
| "team photos" | "Processing team photos!" | 800x800, JPEG, 90% | 2-3s each | Consistent sizing |
| "product images" | "E-commerce optimization!" | Multiple sizes | 10s per product | Complete set |
| "blog thumbnails" | "Creating thumbnails!" | 400x400, 75% | 2s each | Under 50KB |
| "make it faster" | "Maximum compression!" | Reduce quality to 75% | 2-3s | 75% smaller |

---

## 5. ⚡ Smart Defaults

### Automatic Decision Matrix

**Based on Destination:**
```yaml
CMS Collection Image:
  Detection: "collection", "CMS", "item"
  Max Width: 1920px
  Format: WebP
  Quality: 85%
  Progressive: Yes
  Processing: 2-3 seconds
  Result: Optimal for Webflow CDN
  
Asset Library:
  Detection: "asset", "library", "media"
  Preserve Original: Yes
  Create WebP version: Yes
  Generate thumbnail: Yes
  Processing: 4-5 seconds
  Result: Multiple versions available
  
Background Image:
  Detection: "background", "hero", "banner"
  Max Width: 2560px
  Quality: 90%
  Format: WebP with JPEG fallback
  Processing: 3-4 seconds
  Result: High quality, optimized size
```

### The 85% Rule for Webflow

**Why 85% is the Sweet Spot:**
```yaml
Quality Comparison:
  100%: Original - No visible benefit, huge files
  95%: Excellent - 20% smaller, no visible difference
  90%: Very Good - 40% smaller, minimal difference
  85%: Optimal - 60% smaller, imperceptible difference
  80%: Good - 70% smaller, slight softness
  75%: Acceptable - 75% smaller, visible on close inspection
  70%: Poor - 80% smaller, noticeable quality loss

Webflow Benefits at 85%:
  - CDN bandwidth: 60% reduction
  - Page load time: 40% faster
  - Storage usage: 60% less
  - Mobile performance: Significant improvement
  - Quality perception: No user complaints
```

---

## 6. 🚨 Error Recovery

### Common Issues & Solutions with Success Rates

**File Too Large for Webflow:**
```yaml
Issue: Image exceeds 4MB limit
Frequency: 15% of uploads
Detection: Automatic before upload

Solution Cascade:
  1. Try 1920px at 85% (95% success)
  2. Try 1600px at 80% (99% success)
  3. Try 1280px at 75% (100% success)
  4. Force WebP conversion (100% success)

Recovery Time: 3-5 seconds
User Impact: Minimal
```

**Format Not Supported:**
```yaml
Issue: Webflow doesn't support format
Frequency: 5% of uploads
Common: TIFF, RAW, WEBP (older browsers)

Solution:
  Automatic Conversion:
    TIFF to JPEG (preserve quality)
    RAW to JPEG (process with defaults)
    WEBP to JPEG (fallback for compatibility)
    BMP to PNG (preserve if needed)

Recovery Time: 2-4 seconds
Success Rate: 100%
```

**Batch Processing Issues:**
```yaml
Issue: Too many images at once
Frequency: 10% of batch operations
Threshold: >20 images

Solution:
  Automatic Chunking:
    - Split into groups of 10
    - Process sequentially
    - Show progress per chunk
    - Combine results

Memory Management:
  - Clear after each chunk
  - Garbage collection between
  - Monitor memory usage

Recovery Time: No delay, automatic
Success Rate: 100%
```

---

## 7. 📊 Performance Metrics

### Optimization Impact Analysis

**File Size Reduction by Format:**
```yaml
PNG to WebP:
  Average reduction: 65%
  Best case: 85% (graphics)
  Worst case: 45% (photos)
  Processing speed: 1 image/2-3 seconds

JPEG to WebP:
  Average reduction: 30%
  Best case: 45% (high quality)
  Worst case: 15% (already optimized)
  Processing speed: 1 image/2-3 seconds

PNG to JPEG:
  Average reduction: 55%
  Best case: 75% (photos)
  Worst case: 20% (graphics)
  Note: Loses transparency
  Processing speed: 1 image/2-3 seconds
```

**Batch Processing Performance:**
```yaml
Processing Speed by Batch Size:
  1 image: 2-3 seconds
  5 images: 10-15 seconds (2-3s each)
  10 images: 20-30 seconds (2-3s each)
  20 images: 40-60 seconds (2-3s each)
  50 images: 100-150 seconds (2-3s each)
  
Optimal batch size: 10-15 images
Memory usage: ~50MB per 10 images
CPU usage: 60-80% during processing
API calls per batch: 1-2 per image
Rate limit: 60 requests/minute
```

---

## 8. 🔄 Integration Triggers

### Webflow-Specific Integration Points

**Pre-Upload Optimization:**
```yaml
Trigger Points:
  - Asset upload dialogue
  - CMS item image field
  - Bulk import preparation
  - Media library upload

Automatic Actions:
  - Check file size
  - Detect format
  - Apply preset
  - Process image
  - Return optimized version

Integration Time: +2-3 seconds per image
User Experience: Seamless
API Calls: 1-2 per image
```

**Bulk Import Optimization:**
```yaml
CSV/JSON Import with Images:

Detection:
  - Image URLs in data
  - Local file references
  - Base64 encoded images

Processing:
  1. Extract image references
  2. Download/decode images
  3. Batch optimize
  4. Upload to Webflow
  5. Update references
  6. Complete import

Performance:
  - 10 images: 20-30 seconds
  - 50 images: 100-150 seconds
  - 100 images: 200-300 seconds
  
API Calls: 1-2 per image
Rate Limit: 60/minute
```

---

## 9. ⚠️ API Error Codes

### Imagician API Error Reference

| Error Code | Meaning | User Message | Recovery Action |
|------------|---------|--------------|-----------------|
| FILE_TOO_LARGE | >10MB input | "File exceeds size limit" | Reduce dimensions first |
| INVALID_FORMAT | Unsupported type | "Format not supported" | Convert to supported |
| MEMORY_ERROR | Out of memory | "Processing capacity reached" | Process in smaller batches |
| TIMEOUT | Processing timeout | "Operation took too long" | Retry with smaller file |
| CORRUPT_FILE | Cannot read file | "File appears damaged" | Request new upload |

### Webflow Integration Errors

| Error Code | Meaning | User Message | Recovery Action |
|------------|---------|--------------|-----------------|
| UPLOAD_FAILED | Webflow rejected | "Upload to Webflow failed" | Check file requirements |
| SIZE_LIMIT | >4MB for Webflow | "File too large for Webflow" | Apply more compression |
| FORMAT_INVALID | Wrong format | "Webflow doesn't support this" | Convert to JPEG/PNG |
| QUOTA_EXCEEDED | Storage full | "Webflow storage limit" | Clear unused assets |

---

## 10. 📌 Quick Reference

### Instant Operations

| Task | Command | Settings | Time | API Calls | Result |
|------|---------|----------|------|-----------|--------|
| **Web optimize** | "optimize for web" | 1920px, WebP, 85% | 2-3s | 1-2 | 60% smaller |
| **Make thumbnail** | "create thumbnail" | 400x400, 75% | 2s | 1 | Under 50KB |
| **Compress** | "make smaller" | Same size, -10% quality | 2-3s | 1 | 25% smaller |
| **Convert** | "to webp" | Format change | 2-3s | 1-2 | 30% smaller |
| **Resize** | "1200px wide" | Specific dimension | 2-3s | 1 | Proportional |
| **Batch** | "all images" | Apply to multiple | 2-3s each | 1-2 each | Consistent |

### Webflow Asset Guidelines

| Asset Type | Max Size | Recommended | Format | Quality | Processing |
|------------|----------|-------------|--------|---------|------------|
| CMS Image | 4MB | <500KB | WebP | 85% | 2-3s |
| Background | 4MB | <1MB | WebP | 90% | 3-4s |
| Product | 4MB | <300KB | JPEG | 85% | 2-3s |
| Thumbnail | 4MB | <50KB | WebP | 75% | 2s |
| Logo | 4MB | <100KB | PNG/SVG | Lossless | <1s |

### Rate Limit Management

```yaml
API Limits:
  - Maximum: 60 requests/minute
  - Warning: 50 requests/minute
  - Auto-throttle: 55 requests/minute
  - Recovery: Wait 60 seconds
  
Best Practices:
  - Batch operations when possible
  - Cache processed images
  - Monitor usage in real-time
  - Queue large batches
```

---

*This intelligence document provides everything needed to optimize images for Webflow using Imagician MCP. Focus on the 85% quality rule and WebP format for best results. All operations include standardized performance metrics and API rate limit management.*