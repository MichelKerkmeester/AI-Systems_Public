# Webflow - Knowledge - v0.100

The complete unified knowledge system for Webflow CMS operations through natural language conversation, with seamless Figma design integration and Imagician image optimization.

## Table of Contents
1. [📋 Overview](#1--overview)
2. [🎯 Core Knowledge](#2--core-knowledge)
3. [🔄 Conversation Flow](#3--conversation-flow)
4. [🎨 Design Integration](#4--design-integration)
5. [📸 Image Optimization](#5--image-optimization)
6. [📊 CMS Operations](#6--cms-operations)
7. [🚀 Publishing Workflows](#7--publishing-workflows)
8. [🚨 Error Handling](#8--error-handling)
9. [📈 Performance Metrics](#9--performance-metrics)
10. [📌 API Reference](#10--api-reference)

---

## 1. 📋 Overview

This document serves as the central knowledge hub for the Webflow MCP Agent system, coordinating between:
- **Webflow MCP**: CMS and site management
- **Figma MCP**: Design system integration (see Figma MCP - Knowledge - v0.200)
- **Imagician MCP**: Image optimization (see Imagician MCP - Knowledge - v0.200)

**System Architecture:**
```yaml
User Input
    ↓
Intent Recognition
    ↓
MCP Selection
    ├─ Webflow (Primary)
    ├─ Figma (Design)
    └─ Imagician (Images)
    ↓
Operation Execution
    ↓
Visual Feedback
```

**Core Principles:**
- Natural language understanding
- Zero technical knowledge required
- Automatic best practices
- Design-first approach
- Performance optimization
- Educational guidance

**Performance Targets:**
- Task completion: 95%+
- Average operations: <3
- Response time: <5 seconds
- Design accuracy: 98%
- Image optimization: 60-80% size reduction
- API rate limit: 60 requests/minute

---

## 2. 🎯 Core Knowledge

### Intent Recognition Framework

**Confidence Levels:**
| Confidence | Range | Response | Turns | Example |
|------------|-------|----------|-------|---------|
| **Exact** | >0.95 | Immediate | 1-2 | "create blog post titled X" |
| **High** | 0.80-0.95 | Brief check | 2-3 | "update product" |
| **Medium** | 0.50-0.79 | Guided | 3-4 | "set up shop" |
| **Low** | <0.50 | Full guide | 4-6 | "help with site" |

### MCP Knowledge Matrix

**Primary Selection:**
```yaml
Webflow MCP:
  Triggers:
    - CMS operations
    - Site management
    - Publishing
    - SEO optimization
  Confidence: Always primary
  
Figma MCP:
  Triggers:
    - "design", "mockup", "prototype"
    - "import styles", "sync colors"
    - "component", "design system"
  Time: 30-45 seconds for full import
  API Calls: 15-25
  
Imagician MCP:
  Triggers:
    - "optimize image", "resize photo"
    - "compress", "convert format"
    - "batch process images"
  Time: 2-3 seconds per image
  API Calls: 1-2 per image
```

### Smart Defaults System

**Collection Structures:**
```yaml
Blog System:
  Collections: [Posts, Categories, Authors]
  Fields: 28 total configured
  Design: Auto-apply if Figma connected
  Images: Auto-optimize via Imagician
  Setup Time: 15-20 seconds
  API Calls: 10-15
  
E-commerce:
  Collections: [Products, Categories, Orders]
  Fields: 35 total configured
  Product Images: 4 sizes auto-generated
  Design: Component mapping from Figma
  Setup Time: 20-30 seconds
  API Calls: 15-20
```

---

## 3. 🔄 Conversation Flow

### Adaptive Conversation Patterns

**Simple Request Flow:**
```
User: "create blog post"
System: "Creating blog post in your CMS!
        
        📝 Adding to: Blog Posts collection
        ✔ Title: New post
        ✔ Status: Draft
        🎨 Styles: Applied from design system
        
        ⏱️ Time: 3-5 seconds"
```

**Complex Request with Integration:**
```
User: "set up blog with Figma design and optimized images"
System: "I'll set up your blog with Figma design and image optimization!
        
        Step 1: Extracting Figma design (30-45s)
        Step 2: Creating collections (15-20s)
        Step 3: Applying styles (10-15s)
        Step 4: Configuring image optimization (5s)
        
        Total time: ~60-85 seconds
        
        Starting now..."
```

### Context Management

**Session Context:**
```yaml
Active:
  site_id: "abc123"
  collection: "blog-posts"
  figma_file: "file-xyz"
  design_version: "v2.1"
  
Persistent:
  preferences:
    image_quality: 85
    design_sync: automatic
    default_env: staging
    
Temporary:
  current_operation: "import"
  step: 3
  progress: 60%
```

---

## 4. 🎨 Design Integration

### Design Token Application

**Token Categories:**
```yaml
Colors:
  Import: 1s per color
  Format: CSS variables
  Application: Global swatches
  API Calls: 1 per 5 colors
  
Typography:
  Import: 4s per style
  Format: Text classes
  Application: H1-H6, body, captions
  API Calls: 2 per style
  
Components:
  Import: 15s per component
  Format: Webflow symbols
  Application: Reusable elements
  API Calls: 5-8 per component
```

### Design Sync Workflow

**Full Import Process:**
```yaml
1. Connect to Figma (3s)
2. Extract tokens (10-15s)
3. Generate classes (8-10s)
4. Apply to site (5-8s)
5. Document system (async)

Total: 30-45 seconds
Coverage: 95% of design
API Calls: 15-25
Rate Limit: 60/minute
```

**Update Check:**
```yaml
1. Check version (2s)
2. Compare tokens (3s)
3. Identify changes (2s)
4. Apply updates (5-10s)

Total: 10-15 seconds
API Calls: 5-8
Rate Limit: 60/minute
```

---

## 5. 📸 Image Optimization

### Optimization Presets

**Webflow-Specific Settings:**
```yaml
Hero Images:
  Size: 2560x1440
  Format: WebP
  Quality: 90%
  Result: <500KB
  Processing: 3-4s
  API Calls: 1-2
  
Content Images:
  Size: 1920px max
  Format: WebP
  Quality: 85%
  Result: <200KB
  Processing: 2-3s
  API Calls: 1
  
Thumbnails:
  Size: 400x400
  Format: WebP
  Quality: 75%
  Result: <50KB
  Processing: 2s
  API Calls: 1
```

### Batch Processing

**E-commerce Product Set:**
```yaml
Per Product:
  - Main: 1500x1500 @ 85%
  - Thumbnail: 150x150 @ 75%
  - Card: 400x400 @ 80%
  - Detail: 800x800 @ 85%
  
Processing: 10s per product
Total savings: 70-80%
API Calls: 4-6 per product
Rate Limit: 60/minute
```

---

## 6. 📊 CMS Operations

### Collection Knowledge

**Smart Field Selection:**
```yaml
Text Content:
  <256 chars: Plain Text
  256-1000: Plain Text or Rich
  >1000: Rich Text
  
Relationships:
  One-to-one: Reference
  One-to-many: Reference (on many)
  Many-to-many: Multi-reference
  
Media:
  Images: Optimized via Imagician
  Design: Styled via Figma
```

### Performance Optimization

**Query Optimization:**
```yaml
Before: 3.2s load time
Actions:
  - Index filter fields
  - Limit returned fields
  - Implement pagination
  - Cache common queries
After: 0.9s load time (-72%)

API Calls: 3-5 for optimization
Rate Limit: 60/minute
```

---

## 7. 🚀 Publishing Workflows

### Publishing Strategy

**Environment Flow:**
```yaml
Development → Staging → Production

Staging First:
  - Test all changes
  - Verify design
  - Check responsive
  - Validate SEO
  Time: 30-60 seconds
  API Calls: 10-15
  
Production:
  - After staging approval
  - During low traffic
  - With monitoring
  Time: 60-90 seconds
  API Calls: 15-20
```

### Pre-flight Checklist

```yaml
Content:
  ☐ Required fields filled
  ☐ Images optimized
  ☐ Design tokens applied
  
SEO:
  ☐ Meta title (50-60 chars)
  ☐ Meta description (150-155)
  ☐ OG image (1200x630)
  
Performance:
  ☐ Images <500KB average
  ☐ Page <3MB total
  ☐ Load time <3s
```

---

## 8. 🚨 Error Handling

### Recovery Strategies

**Rate Limit:**
```yaml
Detection: 50/60 requests
Action: Automatic throttling at 55
Recovery: Wait 60s at limit
Success: 100%
User Message: "Slowing down to stay within limits"
```

**Design Sync Failed:**
```yaml
Detection: Figma connection error
Action: Use cached design (if available)
Recovery: Retry with new token
Success: 90%
User Message: "Using cached design styles"
```

**Image Too Large:**
```yaml
Detection: >4MB file
Action: Auto-optimize with Imagician
Recovery: Progressive compression
Success: 95%
User Message: "Optimizing image to fit requirements"
```

---

## 9. 📈 Performance Metrics

### System Performance

**Operation Benchmarks:**
```yaml
Simple CMS create: <5s (2-3 API calls)
Design import: 30-45s (15-25 API calls)
Image optimization: 2-3s per image (1-2 API calls)
Bulk operations: <3min for 50 items (30-50 API calls)
Full site setup: <8min (50-100 API calls)

Rate Limits:
  Maximum: 60 requests/minute
  Warning: 50 requests/minute
  Auto-throttle: 55 requests/minute
```

### Integration Performance

**MCP Coordination:**
```yaml
Webflow + Figma: +30-45s for design
Webflow + Imagician: +2-3s per image
All three: +60-90s total
Parallel processing: Where possible
```

### Success Metrics

```yaml
Task Completion: 95%+
Design Accuracy: 98%
Image Optimization: 60-80% reduction
User Satisfaction: 4.5/5
Error Recovery: 90%
API Efficiency: <60 requests/minute
```

---

## 10. 📌 API Reference

### Webflow API Errors

| Error Code | HTTP Status | User Message | Recovery Action |
|------------|-------------|--------------|-----------------|
| collection_not_found | 404 | "Collection doesn't exist" | List available collections |
| validation_error | 400 | "Invalid field value" | Show requirements |
| rate_limit_exceeded | 429 | "Too many requests" | Wait 60 seconds |
| unauthorized | 401 | "Access denied" | Check permissions |
| server_error | 500 | "Webflow service issue" | Retry in 5 minutes |

### Figma API Errors

| Error Code | HTTP Status | User Message | Recovery Action |
|------------|-------------|--------------|-----------------|
| file_not_found | 404 | "Can't find Figma file" | Verify URL |
| no_access | 403 | "No permission to file" | Request access |
| rate_limited | 429 | "Figma rate limit" | Wait 60 seconds |

### Imagician API Errors

| Error Code | HTTP Status | User Message | Recovery Action |
|------------|-------------|--------------|-----------------|
| file_too_large | 413 | "Image too large" | Reduce dimensions |
| invalid_format | 415 | "Format not supported" | Convert format |
| processing_failed | 500 | "Optimization failed" | Retry with defaults |

### Rate Limit Management

```yaml
Global Limits (per minute):
  Webflow API: 60 requests
  Figma API: 60 requests
  Imagician: 60 requests
  
Throttling Strategy:
  50 requests: Warning issued
  55 requests: Auto-throttle
  60 requests: Full stop, wait 60s
  
Best Practices:
  - Batch similar operations
  - Cache frequently used data
  - Use differential updates
  - Monitor usage real-time
```

### Common Workflows

**Blog with Design:**
```yaml
1. Import Figma design (30-45s, 15-25 API calls)
2. Create collections (15-20s, 10-15 API calls)
3. Apply styles (10-15s, 5-8 API calls)
4. Configure images (5s, 2-3 API calls)
Total: 60-85 seconds, 32-51 API calls
```

**E-commerce Setup:**
```yaml
1. Import product design (30-45s, 15-25 API calls)
2. Create product collection (15-20s, 10-15 API calls)
3. Set up variants (10-15s, 5-8 API calls)
4. Configure checkout (20s, 8-10 API calls)
Total: 75-100 seconds, 38-58 API calls
```

---

*This knowledge document coordinates all MCP operations for Webflow site management. It provides unified system for natural language CMS control with standardized performance metrics and comprehensive error handling.*