# Webflow - Patterns & Workflows - v0.314

Pattern library for Webflow operations through natural language using native APIs only.

## 📋 Table of Contents

1. [🎯 OVERVIEW](#1--overview)
2. [🔌 CONNECTION PATTERNS](#2--connection-patterns)
3. [💬 INTENT PATTERNS](#3--intent-patterns)
4. [📁 STRUCTURE PATTERNS](#4--structure-patterns)
5. [🎨 COMPONENT PATTERNS](#5--component-patterns)
6. [📊 CONTENT PATTERNS](#6--content-patterns)
7. [🚀 WORKFLOW PATTERNS](#7--workflow-patterns)

---

<a id="1--overview"></a>

## 1. 🎯 OVERVIEW

This document defines pattern recognition and workflow orchestration for natural language Webflow requests. All patterns use native Webflow APIs exclusively - no custom code generation.

### Pattern Categories
- **Connection Verification** - Always check MCP first
- **Intent Recognition** - What user wants to achieve
- **Structure Creation** - Collections and fields (native)
- **Component Building** - Visual elements (native)
- **Content Management** - CRUD operations
- **Complete Workflows** - Multi-step processes

### Core Pattern Principle
```markdown
Every Pattern Follows:

1. Verify MCP connection
2. Identify native API approach
3. Reject custom code requests
4. Execute with Webflow APIs
5. Provide native solutions only
```

---

<a id="2--connection-patterns"></a>

## 2. 🔌 CONNECTION PATTERNS

### Initial Connection Pattern
```yaml
Pattern: Connection Verification
Priority: ALWAYS FIRST
Steps:
  1. Check MCP server status
  2. Run test query (sites_list)
  3. Verify authentication
  4. Check companion app if needed
  5. Proceed or apply REPAIR
```

### Connection States

| State | Pattern | Action | Next |
|-------|---------|--------|------|
| Connected | Proceed | Execute request | Native ops |
| Disconnected | REPAIR | Restart Claude | Re-verify |
| Auth Failed | REPAIR | Re-authorize | Re-verify |
| App Missing | Conditional | Check if Designer needed | Proceed/Launch |

### Recovery Patterns
```markdown
Connection Lost Pattern:

Trigger: Any API call fails
Response:
  1. Immediate connection check
  2. Apply REPAIR protocol
  3. Guide user to fix
  4. Re-verify before retry
  5. Never attempt without connection
```

---

<a id="3--intent-patterns"></a>

## 3. 💬 INTENT PATTERNS

### Creation Intents (Native Only)

| User Says | Intent | Default Action | Method |
|-----------|--------|---------------|--------|
| "create blog" | Blog structure | Collections + fields | Native API |
| "build component" | Component | Elements + styles | Native API |
| "design page" | Full page | Layout + components | Native API |
| "add field" | Field addition | Add to collection | Native API |
| "update content" | Content edit | Modify items | Native API |
| "publish site" | Publishing | Deploy changes | Native API |

### Custom Code Intent Handling

| User Says | Intent | Response | Alternative |
|-----------|--------|----------|-------------|
| "write JavaScript" | Custom code | Reject | Use Designer API |
| "custom CSS" | Custom style | Reject | Use native styles |
| "HTML template" | Custom HTML | Reject | Use components |
| "add script" | Custom script | Reject | Use interactions |

### Management Intents

| User Says | Intent | Default Action | Pre-Check |
|-----------|--------|---------------|-----------|
| "edit items" | Content update | Bulk modify | Connection ✓ |
| "delete old" | Cleanup | Remove items | Connection ✓ |
| "reorganize" | Structure change | Modify relations | Connection ✓ |
| "optimize SEO" | SEO update | Meta fields | Connection ✓ |

### Intent Recognition Flow
```markdown
User Request
    ↓
Connection Check ─── Failed → REPAIR
    ↓ Success
Custom Code? ─── Yes → Offer Native Alternative
    ↓ No
Identify Intent
    ↓
Select Native API
    ↓
Execute
```

---

<a id="4--structure-patterns"></a>

## 4. 📁 STRUCTURE PATTERNS

### Blog System Pattern (Native API)
```yaml
Pattern: Complete Blog
Connection: Verify first
Method: Native Data API only
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
Custom_Code: NEVER
```

### E-commerce Pattern (Native API)
```yaml
Pattern: Product Catalog
Connection: Verify first
Method: Native Data API only
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
Custom_Code: NEVER
```

### Portfolio Pattern (Native API)
```yaml
Pattern: Project Showcase
Connection: Verify first
Method: Native Data API only
Collections:
  Projects:
    - title: PlainText
    - description: RichText
    - thumbnail: Link
    - gallery: Link (multiple)
    - client: PlainText
    - date: Date
    - featured: Switch
Custom_Code: NEVER
```

### Structure Creation Protocol
```markdown
For Every Structure:

1. Verify MCP connection
2. Use webflow:collections_create()
3. Add fields via native API
4. Configure relationships natively
5. No custom validation scripts
6. Apply SEO via native fields
```

---

<a id="5--component-patterns"></a>

## 5. 🎨 COMPONENT PATTERNS

### Card Component (Native Designer API)
```yaml
Pattern: Reusable Card
Connection: Verify + App check
Method: Native Designer API only
Structure:
  Container:
    - API: webflow:components_create()
    - class: card-wrapper (native)
    - children:
      - Image: native aspect-ratio
      - Content: native padding
      - Button: native hover-state
Variants:
  - Default (native)
  - Featured (native larger)
  - Compact (native no image)
Custom_JavaScript: NEVER
```

### Navigation Component (Native Designer API)
```yaml
Pattern: Responsive Nav
Connection: Verify + App check
Method: Native Designer API only
Structure:
  NavWrapper:
    - Logo: native link element
    - MenuItems: native flex layout
    - MobileToggle: native hamburger
Breakpoints:
  - Desktop: native horizontal
  - Mobile: native vertical overlay
Custom_CSS: NEVER
```

### Hero Section (Native Designer API)
```yaml
Pattern: Landing Hero
Connection: Verify + App check
Method: Native Designer API only
Structure:
  HeroContainer:
    - Background: native image/video
    - Content: native centered/left
    - Headline: native h1 styling
    - Subheadline: native h2 styling
    - CTAButtons: native primary/secondary
Custom_Code: NEVER
```

### Component Creation Protocol
```markdown
For Every Component:

1. Verify MCP connection
2. Check companion app status
3. Use webflow:components_create()
4. Apply styles via Designer API
5. Register component natively
6. No custom JavaScript
7. No custom CSS
8. Use native interactions only
```

### Native Component Alternatives
```markdown
When User Requests Custom:

"Custom animation" → Webflow Interactions
"Custom styling" → Designer API styles
"Custom behavior" → Native components
"Custom layout" → Flexbox/Grid via API
"Custom effects" → Native hover states
```

---

<a id="6--content-patterns"></a>

## 6. 📊 CONTENT PATTERNS

### Bulk Operations (Native API)
```yaml
Pattern: Mass Update
Connection: Verify first
Method: Native Data API only
Process:
  - Check connection status
  - Batch by 20 items
  - Monitor rate limits
  - Progress feedback
  - Error handling via REPAIR
  - Use webflow:collections_items_update_items()
Example: Update all prices by 10%
Custom_Scripts: NEVER
```

### Content Migration (Native API)
```yaml
Pattern: Data Transfer
Connection: Verify first
Method: Native Data API only
Process:
  - Verify connection
  - Export source via API
  - Transform structure natively
  - Map relationships via API
  - Import to target via API
  - Verify integrity
  - No custom migration scripts
```

### Publishing Workflow (Native API)
```yaml
Pattern: Staged Deploy
Connection: Verify first
Method: Native Publishing API
Stages:
  - Draft: work in progress (native)
  - Review: internal check (native)
  - Staging: client preview (native)
  - Production: go live (native)
API_Calls:
  - webflow:collections_items_create_item()
  - webflow:collections_items_publish_items()
  - webflow:sites_publish()
Custom_Deploy_Scripts: NEVER
```

### Content Operation Protocol
```markdown
For Every Content Operation:

1. Verify MCP connection
2. Check rate limits
3. Use native CRUD APIs
4. Batch operations properly
5. No custom validation
6. No custom scripts
7. Handle errors with REPAIR
```

---

<a id="7--workflow-patterns"></a>

## 7. 🚀 WORKFLOW PATTERNS

### Complete Website Setup (Native)
```yaml
Pattern: Full Site
Connection: Verify first
Method: 100% Native APIs
Steps:
  1. Verify MCP connection
  2. Create all collections (Data API)
  3. Configure relationships (Data API)
  4. Build page templates (Designer API)
  5. Design components (Designer API)
  6. Add sample content (Data API)
  7. Configure SEO (Data API)
  8. Set up publishing (Data API)
Custom_Code: ZERO
```

### Design System Creation (Native)
```yaml
Pattern: Component Library
Connection: Verify + App check
Method: Native Designer API only
Steps:
  1. Verify connection + app
  2. Define typography (Designer API)
  3. Create color system (Designer API)
  4. Build base components (Designer API)
  5. Create variants (Designer API)
  6. Document usage (native)
  7. Register globally (Designer API)
Custom_CSS_Framework: NEVER
```

### Content Population (Native)
```yaml
Pattern: Initial Content
Connection: Verify first
Method: Native Data API only
Steps:
  1. Verify connection
  2. Import/create items (Data API)
  3. Set relationships (Data API)
  4. Add media URLs (external)
  5. Configure SEO (Data API)
  6. Publish drafts (Publishing API)
Custom_Import_Scripts: NEVER
```

### Workflow Execution Protocol
```markdown
Every Workflow Must:

☑ Start with connection check
☑ Use native APIs exclusively
☑ Reject custom code requests
☑ Apply REPAIR for errors
☑ Monitor rate limits
☑ Provide native alternatives
☑ Complete with native operations
```

### Multi-Step Workflow Pattern
```markdown
Complex Workflow Structure:

BEGIN
  → Verify MCP Connection
    → Failed? Apply REPAIR
  → Check all required APIs
  → Confirm native approach
  → Execute Step 1 (native)
  → Execute Step 2 (native)
  → ... (all native)
  → Verify completion
END (100% native execution)
```

---

## Smart Defaults

**Connection Defaults:**
- Always verify first
- Test query required
- REPAIR if failed
- Native operations only

**Structure Creation:**
- Include SEO fields (native)
- Add relationships (native)
- Configure slugs (native)
- Set validation (native)
- No custom scripts

**Component Building:**
- Responsive by default (native)
- Include hover states (native)
- Apply BEM naming (native)
- Register globally (native)
- No custom CSS/JS

**Content Operations:**
- Batch by 20
- Monitor rate limits
- Validate before save (native)
- Auto-generate slugs (native)
- No custom validators

---

## Critical Pattern Rules

```markdown
THE PATTERN ABSOLUTES:
────────────────────────
1. Connection verification BEFORE any pattern
2. Native APIs ONLY in every pattern
3. Custom code NEVER in any pattern
4. REPAIR protocol for ALL failures
5. Native solutions for ALL requests
```

---

## Pattern Mantras

> "Connection first. Native always. Custom never."

> "Every pattern starts with verification, executes with native APIs."

> "Patterns guide to native solutions, never to custom code."