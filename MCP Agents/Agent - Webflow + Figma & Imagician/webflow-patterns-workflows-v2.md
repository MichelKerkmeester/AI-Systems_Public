# Webflow - Patterns & Workflows - v2.0.0

Complete pattern library and workflow specifications for natural language Webflow CMS operations with Figma design integration, standardized performance metrics, and recovery strategies.

## Table of Contents
1. [📋 Overview](#1--overview)
2. [🎯 Intent Patterns](#2--intent-patterns)
3. [📝 CMS Operation Patterns](#3--cms-operation-patterns)
4. [🚀 Publishing Patterns](#4--publishing-patterns)
5. [🔗 Collection Patterns](#5--collection-patterns)
6. [📊 Bulk Operation Patterns](#6--bulk-operation-patterns)
7. [🎨 Design Integration Patterns](#7--design-integration-patterns)
8. [🔧 Recovery Patterns](#8--recovery-patterns)
9. [⚠️ API Error Handling](#9--api-error-handling)
10. [📈 Performance Metrics](#10--performance-metrics)

---

## 1. 📋 Overview

This document defines all pattern recognition and workflow orchestration logic for the Webflow MCP agent with Figma design integration. Each pattern maps natural language to specific Webflow API operations and Figma design extractions with smart defaults, standardized performance metrics, and recovery strategies.

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
- Design import: 30-45 seconds
- Recovery from errors: <10 seconds
- API rate limit: 60 requests/minute

---

## 2. 🎯 Intent Patterns

### Content Management Intents with Design

| User Says | Intent | Frequency | Complexity | API Calls | Time Est. | Success Rate |
|-----------|--------|-----------|------------|-----------|-----------|--------------|
| "create blog post" | Create CMS item | Common (35%) | ⭐⭐ | 2-3 | 3-5s | 95% |
| "apply design system" | Import Figma | Common (20%) | ⭐⭐⭐⭐ | 15-25 | 30-45s | 92% |
| "update product" | Modify item | Common (20%) | ⭐⭐ | 2-4 | 3-5s | 92% |
| "sync design changes" | Update tokens | Occasional (10%) | ⭐⭐⭐ | 8-12 | 10-15s | 90% |
| "import content" | Bulk create | Occasional (8%) | ⭐⭐⭐⭐ | 20-50 | 60-180s | 85% |
| "map components" | Figma to Webflow | Occasional (5%) | ⭐⭐⭐⭐ | 10-15 | 20-30s | 88% |
| "delete old content" | Remove items | Rare (2%) | ⭐⭐⭐ | 5-20 | 10-30s | 88% |

### Design Integration Intents

| User Says | Target Action | Frequency | Prerequisites | Performance Impact | Fallback |
|-----------|--------------|-----------|---------------|-------------------|----------|
| "import Figma design" | Extract all tokens | Common | Figma access | 30-45s | Manual styles |
| "sync typography" | Update text styles | Common | Design file | 10-15s | Keep current |
| "get color palette" | Import colors | Common | Color styles | 10-15s | Default palette |
| "map components" | Convert to symbols | Occasional | Components exist | 20-30s | Create manually |
| "check design updates" | Differential sync | Occasional | Previous import | 10-15s | Full reimport |

---

## 3. 📝 CMS Operation Patterns

### Create Operations with Design

#### Pattern: Single Item with Styling
```yaml
Pattern Name: Styled Item Creation
Frequency: Very Common (75% of creates)
Complexity: Low
API Calls: 2-3
Time Estimate: 3-5 seconds
Success Rate: 94%

Trigger: "create", "add" + collection + optional "styled"
Prerequisites:
  - Collection exists
  - Design system imported (optional)
  - User has write access

Process:
  1. Identify target collection (1s)
  2. Extract field values (0.5s)
  3. Apply design classes if available (1s)
  4. Generate styled slug (0.5s)
  5. Validate fields (0.5s)
  6. Create item (1.5s)
  
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
Complexity: High
API Calls: 15-25
Time Estimate: 30-45 seconds
Success Rate: 90%

Trigger: "create collection with Figma"
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
  - Figma frames: Collection templates
  - Text styles: Field formatting
  - Components: Item structure
  - Variants: Field options
```

---

## 4. 🚀 Publishing Patterns

### Publishing with Design Validation

#### Pattern: Design-Checked Publish
```yaml
Pattern Name: Styled Content Publish
Frequency: Common (60% of publishes)
Complexity: Medium
API Calls: 5-8
Time Estimate: 10-15 seconds
Success Rate: 92%

Trigger: "publish with design check"
Prerequisites:
  - Content complete
  - Design tokens applied (optional)
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

## 5. 🔗 Collection Patterns

### Collection Creation with Figma

#### Pattern: Design-First Collection
```yaml
Pattern Name: Figma-Driven Structure
Frequency: Weekly
Complexity: High
API Calls: 15-25
Time Estimate: 30-45 seconds
Success Rate: 88%

Process:
  1. Connect to Figma (3s)
  2. Analyze component structure (8s)
  3. Extract field requirements (5s)
  4. Map to Webflow fields (5s)
  5. Create collection (10s)
  6. Apply all styling (10s)
  7. Generate symbols (4s)

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

## 6. 📊 Bulk Operation Patterns

### Import with Design Application

#### Pattern: Styled Bulk Import
```yaml
Pattern Name: Bulk Import with Design
Frequency: Weekly
Complexity: High
API Calls: 30-50
Time Estimate: 90-240 seconds
Success Rate: 85%

Process:
  1. Parse import data (5s)
  2. Load design system (3s)
  3. Map fields to styles (5s)
  4. Validate against design (10s)
  5. Import in batches (3s per 20 items)
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
  - Rate limit safe: 50 requests/minute max
```

---

## 7. 🎨 Design Integration Patterns

### Design System Import

#### Pattern: Complete Design Extraction
```yaml
Pattern Name: Full Figma Import
Frequency: Project start
Complexity: High
API Calls: 15-25
Time Estimate: 30-45 seconds
Success Rate: 88%

Extraction Process:
  1. Connect to Figma API (3s)
  2. Scan file structure (5s)
  3. Extract color styles (5s)
  4. Import typography (10s)
  5. Map components (10s)
  6. Get spacing system (5s)
  7. Extract effects (5s)
  8. Generate Webflow classes (2s)

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
Complexity: Medium
API Calls: 5-8
Time Estimate: 15-20 seconds
Success Rate: 85%

Mapping Process:
  1. Analyze Figma component (3s)
  2. Extract properties (5s)
  3. Map to Webflow structure (4s)
  4. Create symbol (5s)
  5. Apply variants (3s)

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
Complexity: Low
API Calls: 5-8
Time Estimate: 10-15 seconds
Success Rate: 92%

Sync Process:
  1. Check Figma version (2s)
  2. Compare with cache (3s)
  3. Identify changes (2s)
  4. Extract updates only (5s)
  5. Apply to Webflow (3s)

Change Types:
  - Color updates: Instant
  - Typography: 5s per style
  - New components: 15s each
  - Deleted items: 2s each
  - Spacing changes: 10s total
```

---

## 8. 🔧 Recovery Patterns

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

#### Pattern: Rate Limit Recovery
```yaml
Pattern Name: API Rate Limit Management
Trigger: 50+ requests/minute
Frequency: Common with bulk operations
Recovery Time: 60 seconds

Strategy:
  1. Detect approaching limit (continuous)
  2. Throttle at 55 requests
  3. Pause at 60 requests
  4. Wait 60 seconds
  5. Auto-resume operations
  6. Complete remaining

User Experience:
  - Warning at 50 requests
  - Auto-throttle at 55
  - Clear wait message at 60
  - Progress preserved

Success Rate: 100% recovered
```

---

## 9. ⚠️ API Error Handling

### Webflow API Errors

| Error Code | HTTP | User Message | Recovery | Success Rate |
|------------|------|--------------|----------|--------------|
| collection_not_found | 404 | "Collection doesn't exist" | List available | 95% |
| validation_error | 400 | "Invalid field value" | Show requirements | 90% |
| rate_limit_exceeded | 429 | "Too many requests" | Wait 60s | 100% |
| unauthorized | 401 | "Access denied" | Check permissions | 85% |
| server_error | 500 | "Service issue" | Retry 3x | 80% |
| duplicate_slug | 409 | "Slug exists" | Auto-generate | 100% |

### Figma API Errors

| Error Code | HTTP | User Message | Recovery | Success Rate |
|------------|------|--------------|----------|--------------|
| file_not_found | 404 | "Can't find file" | Verify URL | 90% |
| no_access | 403 | "No permission" | Request access | 85% |
| rate_limited | 429 | "Too many requests" | Wait 60s | 100% |
| invalid_token | 401 | "Token expired" | Refresh token | 95% |

### Error Recovery Matrix

| Problem | Quick Solution | Alternative | Success Rate | Time |
|---------|---------------|-------------|--------------|------|
| No access | Check permissions | Share link | 90% | 10s |
| Token expired | Refresh token | New connection | 95% | 15s |
| File not found | Check URL | Browse files | 85% | 20s |
| Sync failed | Retry once | Manual import | 88% | 25s |
| Style conflict | Merge options | Override all | 92% | 15s |
| Rate limited | Wait 60s | Queue for later | 100% | 60s |

---

## 10. 📈 Performance Metrics

### Operation Performance Standards

| Operation Type | Target Time | API Calls | Rate Limit Safe | Cache Used |
|---------------|-------------|-----------|-----------------|------------|
| Single Create | <5s | 2-3 | ✅ Yes | No |
| Styled Create | <8s | 3-5 | ✅ Yes | Yes |
| Design Import | 30-45s | 15-25 | ✅ Yes (throttled) | No |
| Component Sync | 15-20s | 5-8 | ✅ Yes | Yes |
| Bulk 50 items | <3min | 30-50 | ✅ Yes (batched) | Yes |
| Update Tokens | 10-15s | 5-8 | ✅ Yes | Yes |
| Full Site Setup | <8min | 50-100 | ✅ Yes (managed) | Partial |

### Design Integration Performance

```yaml
Current Performance:
  - Token cache hit rate: 78%
  - Component reuse: 85%
  - Style consistency: 96%
  - Sync accuracy: 98%
  - Import success: 92%
  
Rate Limit Management:
  - Maximum: 60 requests/minute
  - Warning: 50 requests/minute
  - Throttle: 55 requests/minute
  - Batch size: 15 items max
  - Pause duration: 60 seconds

Optimization Opportunities:
  - Increase token caching
  - Batch component imports
  - Preload common styles
  - Progressive design loading
```

### Quick Operations Reference

| Task | Command | API Calls | Time | Result |
|------|---------|-----------|------|--------|
| **Import all** | "import Figma design" | 15-25 | 30-45s | Complete design |
| **Get colors** | "extract color palette" | 5-8 | 10-15s | Swatches created |
| **Sync text** | "import typography" | 8-12 | 10-15s | Classes ready |
| **Get component** | "import button" | 5-8 | 15-20s | Symbol created |
| **Check updates** | "check for changes" | 5-8 | 10-15s | Change log |
| **Bulk import** | "import 50 items" | 30-50 | 90-180s | Items created |

### Pattern Matching Priority

```yaml
Priority Order:
  1. Exact match: Component/token names
  2. Design system: Figma file specified
  3. Collection match: With styling needs
  4. Operation match: CRUD + design
  5. Context match: Previous design ops
  6. General match: Any terms

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

*This pattern library enables natural language understanding of all Webflow CMS operations with complete Figma design integration. All patterns include standardized performance metrics, API rate limit management, and comprehensive error recovery strategies.*