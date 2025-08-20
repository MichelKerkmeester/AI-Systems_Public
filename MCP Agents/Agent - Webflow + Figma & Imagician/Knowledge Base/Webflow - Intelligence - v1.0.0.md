# Webflow - Intelligence - v1.0.0

The complete unified intelligence system for Webflow CMS operations through natural language conversation, with seamless Figma design integration and Imagician image optimization.

## Table of Contents
1. [📋 OVERVIEW](#1--overview)
2. [🎯 CORE INTELLIGENCE](#2--core-intelligence)
3. [🔄 CONVERSATION FLOW](#3--conversation-flow)
4. [🎨 DESIGN INTEGRATION](#4--design-integration)
5. [📸 IMAGE OPTIMIZATION](#5--image-optimization)
6. [📊 CMS OPERATIONS](#6--cms-operations)
7. [🚀 PUBLISHING WORKFLOWS](#7--publishing-workflows)
8. [💬 INTERACTION PATTERNS](#8--interaction-patterns)
9. [🚨 ERROR HANDLING](#9--error-handling)
10. [📈 PERFORMANCE METRICS](#10--performance-metrics)

---

## 1. 📋 OVERVIEW

This document serves as the central intelligence hub for the Webflow MCP Agent system, coordinating between:
- **Webflow MCP** - CMS and site management
- **Figma MCP - Intelligence - v1.0.0.md** - Design system integration
- **Imagician MCP - Intelligence - v1.0.0.md** - Image optimization
- **Webflow - Intelligence - v1.0.0.md** - This central intelligence document
- **Supporting documents** - Patterns, workflows, and CMS intelligence

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

---

## 2. 🎯 CORE INTELLIGENCE

### Intent Recognition Framework

**Confidence Levels:**
| Confidence | Range | Response | Turns | Example |
|------------|-------|----------|-------|---------|
| **Exact** | >0.95 | Immediate | 1-2 | "create blog post titled X" |
| **High** | 0.80-0.95 | Brief check | 2-3 | "update product" |
| **Medium** | 0.50-0.79 | Guided | 3-4 | "set up shop" |
| **Low** | <0.50 | Full guide | 4-6 | "help with site" |

### MCP Intelligence Matrix

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
  Reference: Figma MCP - Intelligence - v1.0.0.md
  
Imagician MCP:
  Triggers:
    - "optimize image", "resize photo"
    - "compress", "convert format"
    - "batch process images"
  Reference: Imagician MCP - Intelligence - v1.0.0.md
```

### Smart Defaults System

**Collection Structures:**
```yaml
Blog System:
  Collections: [Posts, Categories, Authors]
  Fields: 28 total configured
  Design: Auto-apply if Figma connected
  Images: Auto-optimize via Imagician
  
E-commerce:
  Collections: [Products, Categories, Orders]
  Fields: 35 total configured
  Product Images: 4 sizes auto-generated
  Design: Component mapping from Figma
```

---

## 3. 🔄 CONVERSATION FLOW

### Adaptive Conversation Patterns

**Simple Request Flow:**
```
User: "create blog post"
System: "Creating blog post in your CMS!
        
        📁 Adding to: Blog Posts collection
        ✓ Title: New post
        ✓ Status: Draft
        🎨 Styles: Applied from design system
        
        ⏱️ Time: 3 seconds"
```

**Complex Request with Integration:**
```
User: "set up blog with Figma design and optimized images"
System: "I'll set up your blog with Figma design and image optimization!
        
        Step 1: Extracting Figma design (15s)
        Step 2: Creating collections (20s)
        Step 3: Applying styles (10s)
        Step 4: Configuring image optimization (5s)
        
        Total time: ~50 seconds
        
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

## 4. 🎨 DESIGN INTEGRATION

*References: Figma MCP - Intelligence - v1.0.0.md*

### Design Token Application

**Token Categories:**
```yaml
Colors:
  Import: 0.5s per color
  Format: CSS variables
  Application: Global swatches
  
Typography:
  Import: 2s per style
  Format: Text classes
  Application: H1-H6, body, captions
  
Components:
  Import: 5s per component
  Format: Webflow symbols
  Application: Reusable elements
```

### Design Sync Workflow

**Full Import Process:**
```yaml
1. Connect to Figma (3s)
2. Extract tokens (15s)
3. Generate classes (10s)
4. Apply to site (8s)
5. Document system (5s)

Total: 40-45 seconds
Coverage: 95% of design
```

**Update Check:**
```yaml
1. Check version (2s)
2. Compare tokens (3s)
3. Identify changes (2s)
4. Apply updates (5-10s)

Total: 12-17 seconds
```

---

## 5. 📸 IMAGE OPTIMIZATION

*References: Imagician MCP - Intelligence - v1.0.0.md*

### Optimization Presets

**Webflow-Specific Settings:**
```yaml
Hero Images:
  Size: 2560x1440
  Format: WebP
  Quality: 90%
  Result: <500KB
  
Content Images:
  Size: 1920px max
  Format: WebP
  Quality: 85%
  Result: <200KB
  
Thumbnails:
  Size: 400x400
  Format: WebP
  Quality: 75%
  Result: <50KB
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
```

---

## 6. 📊 CMS OPERATIONS

### Collection Intelligence

**Smart Field Selection:**
```yaml
Text Content:
  <256 chars → Plain Text
  256-1000 → Plain Text or Rich
  >1000 → Rich Text
  
Relationships:
  One-to-one → Reference
  One-to-many → Reference (on many)
  Many-to-many → Multi-reference
  
Media:
  Images → Optimized via Imagician
  Design → Styled via Figma
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
```

---

## 7. 🚀 PUBLISHING WORKFLOWS

### Publishing Strategy

**Environment Flow:**
```yaml
Development → Staging → Production

Staging First:
  - Test all changes
  - Verify design
  - Check responsive
  - Validate SEO
  
Production:
  - After staging approval
  - During low traffic
  - With monitoring
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

## 8. 💬 INTERACTION PATTERNS

### Common Patterns

| User Intent | System Response | Actions | Time |
|------------|----------------|---------|------|
| "create blog" | "Setting up blog system!" | 3 collections, 28 fields | 30s |
| "import design" | "Extracting from Figma!" | Full token import | 45s |
| "optimize images" | "Processing with Imagician!" | Batch optimization | 2s/image |
| "publish site" | "Publishing to production!" | Full site deploy | 60s |

### Educational Moments

**Automatic Teaching:**
```yaml
After collection creation:
  "💡 Tip: Reference fields connect your content automatically"
  
After image optimization:
  "📊 Saved 70% file size with no visible quality loss"
  
After design import:
  "🎨 Design tokens are now CSS variables for consistency"
```

---

## 9. 🚨 ERROR HANDLING

### Recovery Strategies

**Rate Limit:**
```yaml
Detection: 55/60 requests
Action: Automatic throttling
Recovery: Wait 45s, resume
Success: 100%
```

**Design Sync Failed:**
```yaml
Detection: Figma connection error
Action: Use cached design (if available)
Recovery: Retry with new token
Success: 90%
Reference: Figma MCP - Intelligence - v1.0.0.md
```

**Image Too Large:**
```yaml
Detection: >4MB file
Action: Auto-optimize with Imagician
Recovery: Progressive compression
Success: 95%
Reference: Imagician MCP - Intelligence - v1.0.0.md
```

---

## 10. 📈 PERFORMANCE METRICS

### System Performance

**Operation Benchmarks:**
```yaml
Simple CMS create: <5s
Design import: <60s
Image optimization: 2-3s per image
Bulk operations: <3min for 50 items
Full site setup: <8min
```

### Integration Performance

**MCP Coordination:**
```yaml
Webflow + Figma: +15-20s for design
Webflow + Imagician: +2-3s per image
All three: +45-60s total
Parallel processing: Where possible
```

### Success Metrics

```yaml
Task Completion: 95%+
Design Accuracy: 98%
Image Optimization: 60-80% reduction
User Satisfaction: 4.5/5
Error Recovery: 90%
```

---

## Quick Reference

### File Structure
```
Intelligence Documents:
├── Webflow - Intelligence - v1.0.0.md (this file)
├── Figma MCP - Intelligence - v1.0.0.md
├── Imagician MCP - Intelligence - v1.0.0.md
└── Supporting documents
```

### Priority Matrix

| Operation | Primary MCP | Secondary | Time |
|-----------|------------|-----------|------|
| CMS Create | Webflow | - | 3-5s |
| Design Import | Webflow | Figma | 45-60s |
| Image Upload | Webflow | Imagician | 5-10s |
| Full Setup | Webflow | Both | 5-8min |

### Common Workflows

**Blog with Design:**
1. Import Figma design (45s)
2. Create collections (20s)
3. Apply styles (10s)
4. Configure images (5s)
Total: ~80 seconds

**E-commerce Setup:**
1. Import product design (30s)
2. Create product collection (15s)
3. Set up variants (10s)
4. Configure checkout (20s)
Total: ~75 seconds

---

*This intelligence document coordinates all MCP operations for Webflow site management. It references Figma MCP - Intelligence - v1.0.0.md for design operations and Imagician MCP - Intelligence - v1.0.0.md for image optimization, providing a unified system for natural language CMS control.*