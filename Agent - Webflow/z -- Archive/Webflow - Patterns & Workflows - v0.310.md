# Webflow - Patterns & Workflows - v0.310

Pattern library for Webflow operations through natural language.

## 📋 Table of Contents

1. [🎯 OVERVIEW](#1--overview)
2. [💬 INTENT PATTERNS](#2--intent-patterns)
3. [📐 STRUCTURE PATTERNS](#3--structure-patterns)
4. [🎨 COMPONENT PATTERNS](#4--component-patterns)
5. [📊 CONTENT PATTERNS](#5--content-patterns)
6. [🚀 WORKFLOW PATTERNS](#6--workflow-patterns)
7. [🧠 THINKING PATTERNS](#7--thinking-patterns)
8. [⚡ EMERGENCY PATTERNS](#8--emergency-patterns)

---

## 1. 🎯 OVERVIEW

This document defines pattern recognition and workflow orchestration for natural language Webflow requests.

### Pattern Categories
- **Intent Recognition** - What user wants to achieve
- **Structure Creation** - Collections and fields
- **Component Building** - Visual elements
- **Content Management** - CRUD operations
- **Complete Workflows** - Multi-step processes
- **Emergency Recovery** - Quick commands

---

## 2. 💬 INTENT PATTERNS

### Creation Intents

| User Says | Intent | Default Action | Thinking |
|-----------|--------|---------------|----------|
| "create blog" | Blog structure | Collections + fields | 3-4 rounds |
| "build component" | Component | Elements + styles | 5-6 rounds |
| "design page" | Full page | Layout + components | 7-8 rounds |
| "add field" | Field addition | Add to collection | 1-2 rounds |
| "update content" | Content edit | Modify items | 1-2 rounds |
| "publish site" | Publishing | Deploy changes | 2-3 rounds |

### Management Intents

| User Says | Intent | Default Action | Thinking |
|-----------|--------|---------------|----------|
| "edit items" | Content update | Bulk modify | 2-3 rounds |
| "delete old" | Cleanup | Remove items | 1-2 rounds |
| "reorganize" | Structure change | Modify relations | 3-4 rounds |
| "optimize SEO" | SEO update | Meta fields | 2-3 rounds |

---

## 3. 📐 STRUCTURE PATTERNS

### Blog System Pattern
```yaml
Pattern: Complete Blog
Thinking: 3-4 rounds
Collections:
  BlogPosts:
    - title: PlainText
    - slug: Slug
    - content: RichText
    - excerpt: PlainText
    - featured_image: Link
    - author: Reference
    - categories: MultiReference
    - published_date: Date
    - meta_title: PlainText
    - meta_description: PlainText
  Authors:
    - name: PlainText
    - bio: RichText
    - avatar: Link
  Categories:
    - name: PlainText
    - slug: Slug
```

### E-commerce Pattern
```yaml
Pattern: Product Catalog
Thinking: 4-5 rounds
Collections:
  Products:
    - name: PlainText
    - price: Number
    - description: RichText
    - images: Link (multiple)
    - sku: PlainText
    - inventory: Number
    - category: Reference
  Categories:
    - name: PlainText
    - parent: Reference (self)
```

### Portfolio Pattern
```yaml
Pattern: Project Showcase
Thinking: 3-4 rounds
Collections:
  Projects:
    - title: PlainText
    - description: RichText
    - thumbnail: Link
    - gallery: Link (multiple)
    - client: PlainText
    - date: Date
    - featured: Switch
```

---

## 4. 🎨 COMPONENT PATTERNS

### Card Component
```yaml
Pattern: Reusable Card
Thinking: 5-6 rounds
Structure:
  Container:
    - class: card-wrapper
    - children:
      - Image: aspect-ratio, object-fit
      - Content: padding, typography
      - Button: hover-state, cursor
Variants:
  - Default
  - Featured (larger)
  - Compact (no image)
```

### Navigation Component
```yaml
Pattern: Responsive Nav
Thinking: 5-6 rounds
Structure:
  NavWrapper:
    - Logo: link to home
    - MenuItems: flex layout
    - MobileToggle: hamburger
Breakpoints:
  - Desktop: horizontal
  - Mobile: vertical overlay
```

### Hero Section
```yaml
Pattern: Landing Hero
Thinking: 6-7 rounds
Structure:
  HeroContainer:
    - Background: image/video
    - Content: centered/left
    - Headline: h1 styling
    - Subheadline: h2 styling
    - CTAButtons: primary/secondary
```

---

## 5. 📊 CONTENT PATTERNS

### Bulk Operations
```yaml
Pattern: Mass Update
Thinking: 2-3 rounds
Process:
  - Batch by 20 items
  - Monitor rate limits
  - Progress feedback
  - Error handling
Example: Update all prices by 10%
```

### Content Migration
```yaml
Pattern: Data Transfer
Thinking: 4-5 rounds
Process:
  - Export source
  - Transform structure
  - Map relationships
  - Import to target
  - Verify integrity
```

### Publishing Workflow
```yaml
Pattern: Staged Deploy
Thinking: 3-4 rounds
Stages:
  - Draft: work in progress
  - Review: internal check
  - Staging: client preview
  - Production: go live
```

---

## 6. 🚀 WORKFLOW PATTERNS

### Complete Website Setup
```yaml
Pattern: Full Site
Thinking: 9-10 rounds
Steps:
  1. Create all collections
  2. Configure relationships
  3. Build page templates
  4. Design components
  5. Add sample content
  6. Configure SEO
  7. Set up publishing
```

### Design System Creation
```yaml
Pattern: Component Library
Thinking: 7-8 rounds
Steps:
  1. Define typography
  2. Create color system
  3. Build base components
  4. Create variants
  5. Document usage
  6. Register globally
```

### Content Population
```yaml
Pattern: Initial Content
Thinking: 3-4 rounds
Steps:
  1. Import/create items
  2. Set relationships
  3. Add media URLs
  4. Configure SEO
  5. Publish drafts
```

---

## 7. 🧠 THINKING PATTERNS

### Depth Recommendations

| Operation | Quick (1-2) | Standard (3-6) | Thorough (7-10) |
|-----------|------------|----------------|-----------------|
| Simple update | ✓ Default | If multiple | Complex logic |
| Create collection | Basic | ✓ Default | Full system |
| Build component | Single | ✓ Default | Component system |
| Design page | Basic layout | ✓ Default | Full responsive |
| Full site | - | - | ✓ Default |

### When to Ask
**Ask about thinking:**
- Before any execution
- After gathering requirements
- When ready to create

**Don't ask yet:**
- During discovery
- While clarifying
- In error messages

---

## 8. ⚡ EMERGENCY PATTERNS

### Command Patterns

| Pattern | Command | Effect | Example |
|---------|---------|--------|---------|
| **Fresh Start** | $reset | Clear everything | "Things are confused, $reset" |
| **Quick Execute** | $quick | Minimal process | "$quick create blog" |
| **Check State** | $status | Show context | "What's happening? $status" |

### Recovery Workflows

**Pattern: Companion Disconnected**
```yaml
Trigger: Designer API fails
Command Options:
  - $status - Check connection
  - $quick - Try Data API only
  - $reset - Clear and restart
Recovery:
  1. Inform user
  2. Offer alternatives
  3. Queue operations
```

**Pattern: Rate Limited**
```yaml
Trigger: 429 error
Command Options:
  - $status - Check usage
  - $quick - Emergency batch
Recovery:
  1. Show current usage
  2. Wait 60 seconds
  3. Resume with batching
```

**Pattern: Confused Context**
```yaml
Trigger: Unexpected behavior
Command Options:
  - $reset - Start fresh
  - $status - Diagnose issue
Recovery:
  1. Clear patterns
  2. Restart conversation
  3. Rebuild context
```

---

## Pattern Matching Priority

When multiple patterns match:
1. **Explicit parameters** - User specifies details
2. **Emergency commands** - $commands override
3. **Common patterns** - Blog, e-commerce, etc.
4. **General creation** - Collections, components
5. **Content operations** - CRUD, publishing

---

## Smart Defaults

**Structure Creation:**
- Include SEO fields
- Add relationships
- Configure slugs
- Set validation

**Component Building:**
- Responsive by default
- Include hover states
- Apply BEM naming
- Register globally

**Content Operations:**
- Batch by 20
- Monitor rate limits
- Validate before save
- Auto-generate slugs

---

*Pattern library for natural language Webflow operations. Emergency commands always available. User chooses thinking depth.*
