# Webflow - Patterns & Workflows - v0.300

Complete pattern library for Webflow design and content operations leveraging full Designer and Data API capabilities.

## 📋 Table of Contents

1. [🎯 Overview](#1--overview)
2. [🎯 Intent Patterns](#2--intent-patterns)
3. [📝 Structure Creation Patterns](#3--structure-creation-patterns)
4. [🎨 Design System Patterns](#4--design-system-patterns)
5. [🚀 Component Building Patterns](#5--component-building-patterns)
6. [📊 Content Operation Patterns](#6--content-operation-patterns)
7. [🚀 Publishing Patterns](#7--publishing-patterns)
8. [🧠 ATLAS Thinking Patterns](#8--atlas-thinking-patterns)
9. [🚨 Recovery Patterns](#9--recovery-patterns)
10. [📈 Performance Patterns](#10--performance-patterns)
11. [📄 Pattern Learning](#11--pattern-learning)

---

## 1. 🎯 Overview

This document defines complete creation and management patterns for the Webflow MCP, leveraging both Designer API (for elements, styles, components) and Data API (for collections, fields, content).

### Core Capabilities
- ✅ **CREATE:** Collections, fields, elements, styles, components
- ✅ **DESIGN:** Visual layouts, responsive systems, design tokens
- ✅ **MANAGE:** Content, publishing, SEO, relationships
- ⚠️ **LIMITATION:** Image uploads require external URLs

### Performance Baseline
- Pattern recognition: <1 second
- Collection creation: 3-5 seconds
- Component building: 5-10 seconds
- Content operations: 2-5 seconds
- Bulk operations: 1-2 seconds per item
- API rate limit: 60 requests/minute

---

## 2. 🎯 Intent Patterns

### Full Stack Development Intents

| User Says | Can Do? | APIs Used | Response Pattern | Thinking Rounds |
|-----------|---------|-----------|------------------|-----------------|
| "Create blog structure" | ✅ Yes | Data | Create collections and fields | 3-4 |
| "Build card component" | ✅ Yes | Designer | Create elements and styles | 5-6 |
| "Design landing page" | ✅ Yes | Both | Structure + components | 7-8 |
| "Update product prices" | ✅ Yes | Data | Bulk content update | 2-3 |
| "Add featured image field" | ✅ Yes | Data | Add field to collection | 1-2 |
| "Create navigation menu" | ✅ Yes | Designer | Build nav component | 5-6 |
| "Upload images" | ⚠️ Partial | External | Guide to URL usage | 1 |
| "Setup e-commerce" | ✅ Yes | Both | Full commerce structure | 9-10 |

### Response Patterns by Intent

**Structure Creation Pattern:**
```markdown
Trigger: "Create blog with categories"
Response: "I'll create the blog structure now!"
Execute: Create collections → Add fields → Set relationships
Result: "✅ Blog structure ready with 3 collections and 24 fields"
```

**Component Building Pattern:**
```markdown
Trigger: "Build hero section"
Response: "Creating hero component..."
Execute: Create elements → Apply styles → Register component
Result: "✅ Hero component created and registered"
```

---

## 3. 📝 Structure Creation Patterns

### Pattern: Blog System

**Pattern Name:** Complete Blog Structure
**Capability:** ✅ FULL
**Time:** 10-15 seconds
**APIs:** Data API

**Structure Created:**
```javascript
BlogPosts: {
  title: PlainText,
  slug: Slug,
  content: RichText,
  excerpt: PlainText,
  featured_image: Link,  // URL for image
  author: Reference → Authors,
  categories: MultiReference → Categories,
  published_date: Date,
  meta_title: PlainText,
  meta_description: PlainText
}

Authors: {
  name: PlainText,
  bio: RichText,
  avatar: Link,  // URL for image
  social_links: PlainText
}

Categories: {
  name: PlainText,
  slug: Slug,
  description: PlainText
}
```

### Pattern: E-commerce Catalog

**Pattern Name:** Product Catalog System
**Capability:** ✅ FULL
**Time:** 15-20 seconds
**APIs:** Data API

**Structure Created:**
```javascript
Products: {
  name: PlainText,
  slug: Slug,
  price: Number,
  description: RichText,
  images: MultiImage,  // URLs
  sku: PlainText,
  inventory: Number,
  category: Reference → Categories,
  variants: MultiReference → Variants,
  featured: Switch
}

Categories: {
  name: PlainText,
  parent: Reference → Categories  // Self-reference
}

Variants: {
  name: PlainText,
  price_modifier: Number,
  sku_suffix: PlainText
}
```

---

## 4. 🎨 Design System Patterns

### Pattern: Typography System

**Pattern Name:** Complete Typography Scale
**Capability:** ✅ FULL
**Time:** 8-10 seconds
**APIs:** Designer API

**Styles Created:**
```css
.heading-xxl { font-size: 4rem; line-height: 1.1; }
.heading-xl { font-size: 3rem; line-height: 1.2; }
.heading-lg { font-size: 2.25rem; line-height: 1.25; }
.heading-md { font-size: 1.875rem; line-height: 1.3; }
.heading-sm { font-size: 1.5rem; line-height: 1.35; }
.body-lg { font-size: 1.125rem; line-height: 1.6; }
.body-md { font-size: 1rem; line-height: 1.65; }
.body-sm { font-size: 0.875rem; line-height: 1.7; }
```

### Pattern: Color System

**Pattern Name:** Brand Color Tokens
**Capability:** ✅ FULL
**Time:** 5-7 seconds
**APIs:** Designer API with Variables

**Variables Created:**
```javascript
Colors: {
  primary: { 500: "#0066CC", 600: "#0052A3", 700: "#003D7A" },
  secondary: { 500: "#6C757D", 600: "#545B62", 700: "#3D4347" },
  success: { 500: "#28A745", 600: "#208637", 700: "#186429" },
  danger: { 500: "#DC3545", 600: "#B02A37", 700: "#842029" },
  neutral: { 100: "#F8F9FA", 200: "#E9ECEF", ... 900: "#212529" }
}
```

---

## 5. 🚀 Component Building Patterns

### Pattern: Card Component

**Pattern Name:** Reusable Card System
**Capability:** ✅ FULL
**Time:** 10-12 seconds
**APIs:** Designer API

**Component Structure:**
```javascript
Card: {
  Container: {
    styles: "padding: 1.5rem; border-radius: 0.5rem; shadow",
    children: [
      Image: { aspectRatio: "16:9", objectFit: "cover" },
      Content: {
        children: [
          Title: { tag: "h3", class: "heading-sm" },
          Description: { tag: "p", class: "body-md" },
          CTAButton: { tag: "a", class: "button-primary" }
        ]
      }
    ]
  }
}
```

**Variants Created:**
- Default card
- Featured card (larger)
- Compact card (no image)
- Horizontal card

### Pattern: Navigation Component

**Pattern Name:** Responsive Navigation
**Capability:** ✅ FULL
**Time:** 15-20 seconds
**APIs:** Designer API

**Component Structure:**
```javascript
Navigation: {
  NavWrapper: {
    Logo: { link: "/", image: "logo" },
    MenuItems: {
      desktop: "flex-row, gap-2rem",
      mobile: "flex-column, fullscreen-overlay"
    },
    MobileToggle: {
      hamburger: "three-lines",
      interaction: "toggle-menu"
    }
  }
}
```

---

## 6. 📊 Content Operation Patterns

### Pattern: Bulk Import

**Pattern Name:** Efficient Content Import
**Capability:** ✅ FULL
**Time:** 1-2 seconds per item
**APIs:** Data API

**Process:**
```python
def bulk_import(items):
    batches = chunk(items, size=20)
    for batch in batches:
        if api_calls > 50:
            throttle(1)  # Slow down near limit
        create_items(batch)
        if api_calls >= 55:
            wait(60)  # Pause at limit
```

### Pattern: Content Migration

**Pattern Name:** Cross-Collection Migration
**Capability:** ✅ FULL
**Time:** Variable
**APIs:** Data API

**Workflow:**
1. Read source items
2. Transform data structure
3. Map relationships
4. Create in target collection
5. Verify integrity
6. Update references

---

## 7. 🚀 Publishing Patterns

### Pattern: Staged Publishing

**Pattern Name:** Development → Production
**Capability:** ✅ FULL
**Time:** 5-10 seconds
**APIs:** Data API

**Workflow:**
```javascript
stages: {
  development: {
    items: "draft",
    preview: "enabled",
    robots: "noindex"
  },
  staging: {
    items: "draft",
    preview: "password",
    robots: "noindex"
  },
  production: {
    items: "live",
    preview: "disabled",
    robots: "index"
  }
}
```

---

## 8. 🧠 ATLAS Thinking Patterns

### Pattern: Full Stack Creation

**Pattern Name:** Complete Feature Development
**Thinking Rounds:** 7-9

**Process:**
- **Assess:** "User wants blog with design"
- **Transform:** "Collections + Components approach"
- **Layer:** "Create data structure, then design system"
- **Apply:** "Best practices for both APIs"
- **Synthesize:** "Integrated blog ready for content"

### Thinking Round Allocation
```python
def allocate_thinking_rounds(request_type):
    patterns = {
        'simple_update': 1,
        'collection_creation': 3,
        'component_building': 5,
        'full_page_design': 7,
        'complete_feature': 9
    }
    return patterns.get(request_type, 4)
```

---

## 9. 🚨 Recovery Patterns

### Pattern: Companion App Disconnection

**Error:** Designer API unavailable
**User Impact:** Cannot create visual elements

**REPAIR Protocol:**
- **Recognize:** Designer operations failing
- **Explain:** "MCP Bridge App disconnected"
- **Propose:** Open Designer, launch app, or continue with Data API
- **Adapt:** Switch to available operations
- **Iterate:** Resume when connected
- **Record:** Track connection status

### Pattern: Image Upload Request

**Error:** Direct upload not supported
**User Impact:** Cannot add images directly

**Recovery:**
1. Suggest Cloudinary/S3
2. Provide upload guidance
3. Accept image URLs
4. Continue with URLs

**Example:**
```markdown
Cannot upload directly, but I can work with URLs!
Options:
1. Cloudinary (free tier available)
2. Amazon S3
3. Direct URLs
```

---

## 10. 📈 Performance Patterns

### Optimization Strategies

| Operation | Optimization | Impact |
|-----------|-------------|---------|
| Collection creation | Create with fields in one call | 50% faster |
| Bulk updates | Batch by 20 items | Avoid rate limits |
| Component building | Reuse base styles | 30% faster |
| Publishing | Queue then batch | More efficient |

### API Efficiency

**Rate Limit Management:**
```javascript
rateLimitStrategy: {
  safe: 50,      // Normal operation
  warning: 55,   // Start throttling
  limit: 60,     // Hard stop
  recovery: 60   // Wait time in seconds
}
```

**Batching Strategy:**
- Collections: Create with all fields at once
- Components: Build complete then register
- Content: Process in chunks of 20
- Publishing: Queue then batch publish

---

## 11. 📄 Pattern Learning

### Pattern Recognition

```python
class PatternLibrary:
    def __init__(self):
        self.creation_patterns = {
            'blog_system': 0,
            'ecommerce': 0,
            'portfolio': 0,
            'landing_page': 0
        }
        
        self.component_patterns = {
            'cards': [],
            'heroes': [],
            'navigations': [],
            'footers': []
        }
        
        self.optimization_patterns = {
            'batching_preference': None,
            'naming_convention': None,
            'style_approach': None
        }
```

### Adaptive Behaviors

**Pattern Detected: Blog Creation**
- Apply standard blog structure
- Suggest proven field set
- Recommend component templates
- Offer content templates

**Pattern Detected: Component System**
- Suggest design tokens
- Create style guide
- Build component library
- Document usage patterns

### Learning Rules

1. **After 2 similar requests** → Apply template
2. **After 3 components** → Suggest system
3. **After 5 operations** → Optimize workflow
4. **After patterns emerge** → Create library

---

## Quick Reference

### Can Do ✅
**Structure:**
- Create collections with all fields
- Build complete relationships
- Design component systems
- Apply responsive styles

**Operations:**
- Full CRUD on content
- Bulk processing
- Publishing workflows
- SEO optimization

### Cannot Do ❌
- Upload images directly (use URLs)
- Work without companion app (Designer)
- Exceed rate limits (60/min)

### Optimal Patterns

| Task | Pattern | Time | Success Rate |
|------|---------|------|--------------|
| Blog creation | Structure + Components | 20s | 95% |
| E-commerce setup | Full catalog system | 30s | 90% |
| Component library | Design system approach | 45s | 90% |
| Content import | Batched operations | Variable | 95% |

---

*Complete patterns for full Webflow development. Structure creation, component building, and content management working in harmony.*