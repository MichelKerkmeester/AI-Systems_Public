# Webflow - Patterns & Workflows with Figma - Enhanced v2.0.0

Complete pattern library and workflow specifications for natural language Webflow CMS operations with Figma design integration, performance metrics, and recovery strategies.

**Intelligence References:**
- **Webflow - Intelligence - v1.0.0.md** → Central coordination
- **Figma MCP - Intelligence - v1.0.0.md** → Design extraction patterns
- **Imagician MCP - Intelligence - v1.0.0.md** → Image optimization patterns

## Table of Contents
1. [📋 OVERVIEW](#1--overview)
2. [🎯 INTENT PATTERNS](#2--intent-patterns)
3. [📁 CMS OPERATION PATTERNS](#3--cms-operation-patterns)
4. [🚀 PUBLISHING PATTERNS](#4--publishing-patterns)
5. [🔍 SEO PATTERNS](#5--seo-patterns)
6. [🔗 COLLECTION PATTERNS](#6--collection-patterns)
7. [📊 BULK OPERATION PATTERNS](#7--bulk-operation-patterns)
8. [🔎 QUERY PATTERNS](#8--query-patterns)
9. [🖼️ ASSET PATTERNS](#9--asset-patterns)
10. [🎨 DESIGN INTEGRATION PATTERNS](#10--design-integration-patterns)
11. [⚡ COMPOSITE WORKFLOWS](#11--composite-workflows)
12. [🔧 RECOVERY PATTERNS](#12--recovery-patterns)
13. [📈 OPTIMIZATION PATTERNS](#13--optimization-patterns)

---

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the Webflow MCP agent with Figma design integration. Each pattern maps natural language to specific Webflow API operations and Figma design extractions with smart defaults, performance metrics, and recovery strategies.

**Pattern Categories:**
- **Intent Recognition**: What the user wants to achieve
- **Parameter Extraction**: Collections, fields, values, relationships, design tokens
- **Workflow Selection**: Single vs multi-step operations
- **Design Integration**: Figma extraction and application
- **Publishing Management**: Staging vs production deployment
- **Batch Processing**: Multiple item handling
- **Recovery & Optimization**: Error handling and performance tuning

**Performance Baseline:**
- Pattern recognition: <1 second
- Simple operations: 2-5 seconds
- Complex workflows: 30-120 seconds
- Design import: 20-60 seconds
- Recovery from errors: <10 seconds

---

## 2. 🎯 INTENT PATTERNS

### Content Management Intents with Design

| User Says | Intent | Frequency | Complexity | API Calls | Time Est. | Success Rate |
|-----------|--------|-----------|------------|-----------|-----------|--------------|
| "create blog post" | Create CMS item | Common (35%) | ⭐⭐ | 2-3 | 3-5s | 95% |
| "apply design system" | Import Figma | Common (20%) | ⭐⭐⭐⭐ | 15-30 | 30-45s | 92% |
| "update product" | Modify item | Common (20%) | ⭐⭐ | 2-4 | 3-5s | 92% |
| "sync design changes" | Update tokens | Occasional (10%) | ⭐⭐⭐ | 10-20 | 15-25s | 90% |
| "import content" | Bulk create | Occasional (8%) | ⭐⭐⭐⭐ | 20-100 | 60-180s | 85% |
| "map components" | Figma to Webflow | Occasional (5%) | ⭐⭐⭐⭐⭐ | 20-40 | 30-60s | 88% |
| "delete old content" | Remove items | Rare (2%) | ⭐⭐⭐ | 5-20 | 10-30s | 88% |

### Design Integration Intents

| User Says | Target Action | Frequency | Prerequisites | Performance Impact | Fallback |
|-----------|--------------|-----------|---------------|-------------------|----------|
| "import Figma design" | Extract all tokens | Common | Figma access | Medium | Manual styles |
| "sync typography" | Update text styles | Common | Design file | Low | Keep current |
| "get color palette" | Import colors | Common | Color styles | Low | Default palette |
| "map components" | Convert to symbols | Occasional | Components exist | High | Create manually |
| "check design updates" | Differential sync | Occasional | Previous import | Low | Full reimport |

---

## 3. 📁 CMS OPERATION PATTERNS

### Create Operations with Design

#### Pattern: Single Item with Styling
```yaml
Pattern Name: Styled Item Creation
Frequency: Very Common (75% of creates)
Complexity: ⭐⭐⭐ (3/5)
API Calls: 3-5
Time Estimate: 5-8 seconds
Success Rate: 94%

Trigger: "create", "add" + collection + "styled"
APIs: 
  - POST /collections/{collection_id}/items
  - GET Figma design tokens (cached)
Prerequisites:
  - Collection exists
  - Design system imported
  - User has write access

Process:
  1. Identify target collection (1s)
  2. Extract field values (0.5s)
  3. Apply design classes (1s)
  4. Generate styled slug (0.5s)
  5. Validate with design rules (1s)
  6. Create with styling (3s)
  
Design Integration:
  - Typography classes applied
  - Color tokens used
  - Spacing consistent
  - Component structure maintained

Example: "add team member with our design"
```

#### Pattern: Collection with Design System
```yaml
Pattern Name: Design-Aware Collection
Frequency: Common (30% of collections)
Complexity: ⭐⭐⭐⭐ (4/5)
API Calls: 15-25
Time Estimate: 30-45 seconds
Success Rate: 90%

Trigger: "create collection with Figma"
APIs:
  - Figma API for token extraction
  - POST /collections
  - POST /collections/{id}/fields
Prerequisites:
  - Figma file accessible
  - Site has capacity
  - Design tokens available

Process:
  1. Extract Figma structure (10s)
  2. Map to collection fields (3s)
  3. Create collection (5s)
  4. Add fields with validation (10s)
  5. Apply design classes (8s)
  6. Generate templates (5s)

Design Mapping:
  - Figma frames → Collection templates
  - Text styles → Field formatting
  - Components → Item structure
  - Variants → Field options
```

---

## 4. 🚀 PUBLISHING PATTERNS

### Publishing with Design Validation

#### Pattern: Design-Checked Publish
```yaml
Pattern Name: Styled Content Publish
Frequency: Common (60% of publishes)
Complexity: ⭐⭐⭐ (3/5)
API Calls: 5-8
Time Estimate: 10-15 seconds
Success Rate: 92%

Trigger: "publish with design check"
APIs:
  - Design validation endpoint
  - POST /sites/{site_id}/publish
Prerequisites:
  - Content complete
  - Design tokens applied
  - No style conflicts

Process:
  1. Validate design consistency (3s)
  2. Check token coverage (2s)
  3. Verify responsive styles (2s)
  4. Select environment (1s)
  5. Publish with styles (5s)
  6. Clear CDN cache (2s)

Design Checks:
  - All tokens applied: 95%+
  - Typography consistent: Yes
  - Colors match palette: Yes
  - Spacing grid aligned: Yes
```

---

## 5. 🔍 SEO PATTERNS

### SEO with Design Consistency

#### Pattern: Styled SEO Setup
```yaml
Pattern Name: SEO with Design System
Frequency: Common (Daily)
Complexity: ⭐⭐⭐ (3/5)
API Calls: 8-12
Time Estimate: 15-25 seconds
Success Rate: 91%

Fields Generated:
  - metaTitle: With brand typography
  - metaDescription: Formatted text
  - ogImage: Designed template
  - Schema: With design tokens

Process:
  1. Analyze current metadata (2s)
  2. Apply typography rules (3s)
  3. Generate styled previews (5s)
  4. Check design consistency (2s)
  5. Apply to pages (10s)
  6. Validate appearance (3s)

Design Integration:
  - Font families in meta
  - Brand colors in schema
  - Image templates styled
  - Preview cards designed
```

---

## 6. 🔗 COLLECTION PATTERNS

### Collection Creation with Figma

#### Pattern: Design-First Collection
```yaml
Pattern Name: Figma-Driven Structure
Frequency: Weekly
Complexity: ⭐⭐⭐⭐⭐ (5/5)
API Calls: 25-40
Time Estimate: 45-60 seconds
Success Rate: 88%

Process:
  1. Connect to Figma (3s)
  2. Analyze component structure (8s)
  3. Extract field requirements (5s)
  4. Map to Webflow fields (5s)
  5. Create collection (10s)
  6. Apply all styling (15s)
  7. Generate symbols (10s)
  8. Test responsive (4s)

Figma Analysis:
  - Components found: 5-10
  - Text styles: 8-12
  - Color usage: 10-15
  - Spacing patterns: 8px grid

Webflow Generation:
  - Collections: 1-3
  - Fields: 15-25
  - Classes: 30-50
  - Symbols: 5-10
```

---

## 7. 📊 BULK OPERATION PATTERNS

### Import with Design Application

#### Pattern: Styled Bulk Import
```yaml
Pattern Name: Bulk Import with Design
Frequency: Weekly
Complexity: ⭐⭐⭐⭐ (4/5)
API Calls: 30-150
Time Estimate: 90-240 seconds
Success Rate: 85%

Process:
  1. Parse import data (5s)
  2. Load design system (3s)
  3. Map fields to styles (5s)
  4. Validate against design (10s)
  5. Import in batches (3s per 20)
  6. Apply styling per item (1s each)
  7. Report results (3s)

Design Application:
  - Text formatted per typography
  - Images sized to grid
  - Colors from palette only
  - Spacing standardized

Performance:
  - Batch size: 15 (with styling)
  - Style caching: Active
  - Token reuse: 95%
```

---

## 8. 🔎 QUERY PATTERNS

### Query with Design Filters

| Natural Language | API Filter | Design Check | Performance | Example |
|-----------------|------------|--------------|-------------|---------|
| "styled posts" | has_class | Typography applied | Fast | Blog items |
| "brand colors only" | color_token | Palette match | Medium | Branded content |
| "with hero image" | image_styled | Aspect ratio | Medium | Featured items |
| "responsive ready" | breakpoints | All sizes | Slow | Mobile-first |
| "design v2 items" | design_version | Token version | Fast | Updated content |

---

## 9. 🖼️ ASSET PATTERNS

### Asset Upload with Design Specs

#### Pattern: Design-Compliant Assets
```yaml
Pattern Name: Styled Asset Pipeline
Frequency: Daily
Complexity: ⭐⭐⭐⭐ (4/5)
API Calls: 5-8 per asset
Time Estimate: 15-20s per asset
Success Rate: 91%

Process:
  1. Check Figma specs:
     - Required dimensions (2s)
     - Aspect ratios (1s)
     - Color profiles (1s)
  2. Trigger Imagician:
     - Resize to spec (3s)
     - Apply filters (2s)
     - Optimize format (2s)
  3. Upload to Webflow (5s)
  4. Apply design classes (2s)
  5. Update references (2s)

Design Compliance:
  - Size: Match Figma exactly
  - Format: Per component spec
  - Quality: Design standard
  - Naming: Component-based
```

---

## 10. 🎨 DESIGN INTEGRATION PATTERNS

### Design System Import

#### Pattern: Complete Design Extraction
```yaml
Pattern Name: Full Figma Import
Frequency: Project start
Complexity: ⭐⭐⭐⭐⭐ (5/5)
API Calls: 40-80
Time Estimate: 60-90 seconds
Success Rate: 88%

Extraction Process:
  1. Connect to Figma API (3s)
  2. Scan file structure (5s)
  3. Extract color styles (8s)
  4. Import typography (15s)
  5. Map components (20s)
  6. Get spacing system (5s)
  7. Extract effects (8s)
  8. Generate Webflow classes (15s)
  9. Create documentation (5s)
  10. Validate import (6s)

Results:
  Colors: 10-20 swatches
  Typography: 8-15 styles
  Components: 5-15 symbols
  Spacing: Grid system
  Effects: 3-8 shadows
```

#### Pattern: Component Mapping
```yaml
Pattern Name: Figma to Webflow Symbol
Frequency: Per component
Complexity: ⭐⭐⭐⭐ (4/5)
API Calls: 8-15
Time Estimate: 20-30 seconds
Success Rate: 85%

Mapping Process:
  1. Analyze Figma component (3s)
  2. Extract properties (5s)
  3. Map to Webflow structure (4s)
  4. Create symbol (6s)
  5. Apply variants (5s)
  6. Set interactions (4s)
  7. Test responsive (3s)

Component Types:
  - Buttons: 95% accuracy
  - Cards: 90% accuracy
  - Navigation: 85% accuracy
  - Forms: 88% accuracy
  - Modals: 82% accuracy
```

#### Pattern: Design Update Sync
```yaml
Pattern Name: Differential Design Sync
Frequency: Daily/Weekly
Complexity: ⭐⭐⭐ (3/5)
API Calls: 10-25
Time Estimate: 15-30 seconds
Success Rate: 92%

Sync Process:
  1. Check Figma version (2s)
  2. Compare with cache (3s)
  3. Identify changes (4s)
  4. Extract updates only (5s)
  5. Apply to Webflow (8s)
  6. Update documentation (3s)
  7. Clear old cache (2s)
  8. Notify completion (1s)

Change Types:
  - Color updates: Instant
  - Typography: 5s per style
  - New components: 15s each
  - Deleted items: 2s each
  - Spacing changes: 10s total
```

---

## 11. ⚡ COMPOSITE WORKFLOWS

### Workflow: Site Launch with Figma
```yaml
Workflow Name: Complete Site Setup
Frequency: Project start
Total Complexity: ⭐⭐⭐⭐⭐ (5/5)
Total API Calls: 100-200
Total Time: 5-8 minutes
Success Rate: 85%

Steps with Design:
  1. Import Figma Design (60s, 40 API calls)
     - Extract all tokens
     - Map components
     - Generate classes
  
  2. Create Collections (45s, 20 API calls)
     - Blog Posts with styling
     - Products with templates
     - Team with layouts
  
  3. Apply Design System (30s, 15 API calls)
     - Typography to all text
     - Colors to elements
     - Spacing grid active
  
  4. Import Content (120s, 60 API calls)
     - Sample posts styled
     - Products with images
     - Team profiles designed
  
  5. Configure SEO (20s, 10 API calls)
     - Meta with branding
     - Schema with tokens
     - Previews designed
  
  6. Create Pages (40s, 20 API calls)
     - Homepage with hero
     - Category pages styled
     - Contact with form
  
  7. Test & Publish (60s, 25 API calls)
     - Responsive check
     - Design validation
     - Deploy to staging

Recovery Checkpoints:
  - After design import
  - After collections
  - Before publishing
```

---

## 12. 🔧 RECOVERY PATTERNS

### Design-Specific Recovery

#### Pattern: Design Sync Recovery
```yaml
Pattern Name: Figma Connection Recovery
Trigger: Sync failure
Frequency: Occasional
Recovery Time: 15-30 seconds

Strategy:
  1. Check connection (2s)
  2. Try cached version (instant)
  3. Refresh token (5s)
  4. Retry with delay (10s)
  5. Manual fallback (guided)
  6. Continue with defaults

Fallback Options:
  - Use last successful sync
  - Apply partial updates
  - Manual style input
  - Skip design temporarily

Success Rate: 90% recovered
```

#### Pattern: Token Conflict Resolution
```yaml
Pattern Name: Design Token Conflicts
Trigger: Duplicate or conflicting tokens
Frequency: Common with updates
Recovery Time: 10-20 seconds

Strategy:
  1. Detect conflicts (2s)
  2. Show comparison (3s)
  3. Offer merge options:
     - Keep Figma (newest)
     - Keep Webflow (current)
     - Merge both (combine)
     - Manual selection
  4. Apply resolution (5s)
  5. Update references (5s)

Success Rate: 95% resolved
```

---

## 13. 📈 OPTIMIZATION PATTERNS

### Design Performance Optimization

#### Pattern: Token Optimization
```yaml
Pattern Name: Design Token Efficiency
Trigger: >100 tokens or slow performance
Frequency: Monthly
Impact: 30-50% improvement

Optimizations:
  1. Consolidate similar colors
  2. Merge duplicate text styles
  3. Simplify component variants
  4. Cache frequently used
  5. Lazy load rare tokens

Before: 150 tokens, 3s load
After: 85 tokens, 1s load
```

#### Pattern: Component Performance
```yaml
Pattern Name: Symbol Optimization
Trigger: Slow component rendering
Frequency: As needed
Impact: 40-60% faster

Actions:
  1. Simplify nesting
  2. Reduce variants
  3. Optimize interactions
  4. Cache rendered states
  5. Preload common uses

Metrics:
  - Render time: -45%
  - Memory usage: -30%
  - Interaction delay: -50%
```

---

## 14. 🎯 Quick Operations Reference

### Instant Design Operations

| Command | Operation | API Calls | Time | Success |
|---------|-----------|-----------|------|---------|
| "import colors" | Get palette | 3-5 | 5s | 98% |
| "sync typography" | Update text | 5-8 | 8s | 95% |
| "check design" | Version check | 1-2 | 2s | 99% |
| "apply styles" | Use cached | 5-10 | 10s | 92% |
| "map component" | Single symbol | 8-12 | 15s | 88% |

### Pattern Matching with Design

```yaml
Priority Order with Design:
  1. Exact match - Component/token names
  2. Design system - Figma file specified
  3. Collection match - With styling needs
  4. Operation match - CRUD + design
  5. Context match - Previous design ops
  6. General match - Any terms

Confidence Scoring:
  Base: Intent match (0-50 points)
  + Figma file identified (+15)
  + Design tokens available (+10)
  + Component specified (+10)
  + Style system active (+5)
  + Collection identified (+10)
  
  >95: Execute immediately
  80-95: One clarification
  50-79: Guided process
  <50: Full exploration
```

---

## 15. 📊 Performance Dashboard

### Operation Performance with Design

| Operation Type | Target Time | Current Avg | Status |
|---------------|-------------|-------------|--------|
| Single Create | <5s | 3.2s | ✅ Optimal |
| Styled Create | <8s | 6.5s | ✅ Good |
| Design Import | <60s | 48s | ✅ Good |
| Component Sync | <20s | 16s | ✅ Good |
| Bulk + Design | <3min | 2.5min | ✅ Good |
| Update Tokens | <15s | 12s | ✅ Optimal |
| Full Site Setup | <8min | 6.5min | ✅ Good |

### Design Efficiency Metrics

```yaml
Current Performance:
  - Token cache hit rate: 78%
  - Component reuse: 85%
  - Style consistency: 96%
  - Sync accuracy: 98%
  - Import success: 92%

Optimization Opportunities:
  - Increase token caching
  - Batch component imports
  - Preload common styles
  - Progressive design loading
```

---

*This pattern library enables natural language understanding of all Webflow CMS operations with complete Figma design integration. Patterns include design token extraction, component mapping, and style application while maintaining performance optimization, error recovery, and detailed metrics.*