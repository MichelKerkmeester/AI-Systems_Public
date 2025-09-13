# Webflow - MCP Knowledge - v0.310

Central knowledge system and single source of truth for Webflow capabilities through the MCP server.

## 📋 Table of Contents

1. [🎯 OVERVIEW](#1--overview)
2. [🔌 CORE CAPABILITIES](#2--core-capabilities)
3. [🎨 DESIGNER API OPERATIONS](#3--designer-api-operations)
4. [📊 DATA API OPERATIONS](#4--data-api-operations)
5. [🚀 PUBLISHING WORKFLOWS](#5--publishing-workflows)
6. [⚠️ LIMITATIONS](#6--limitations)
7. [📈 PERFORMANCE METRICS](#7--performance-metrics)
8. [📌 API REFERENCE](#8--api-reference)
9. [🚨 ERROR CODES](#9--error-codes)
10. [⚡ EMERGENCY COMMANDS](#10--emergency-commands)

---

## 1. 🎯 OVERVIEW

This document is the single source of truth for all Webflow MCP capabilities, API operations, and technical specifications.

### MCP Server Details
- **Repository:** https://github.com/webflow/mcp-server
- **Protocol:** Model Context Protocol
- **APIs:** Designer API + Data API
- **Authentication:** OAuth with owner/admin scope

### System Architecture
```
User Request → Intent Recognition → API Selection → Operation → Feedback
                                          ↓
                              Designer API / Data API
                                          ↓
                              Companion App (if Designer)
```

---

## 2. 🔌 CORE CAPABILITIES

### What You CAN Do ✅

**Designer API:**
- Create and modify elements on canvas
- Apply styles and CSS properties
- Build and register components
- Manage variables and design tokens
- Control responsive breakpoints
- Design page structures

**Data API:**
- Create collections with custom fields
- Add any field type to collections
- Manage content items (CRUD operations)
- Handle publishing workflows
- Optimize SEO at scale
- Manage relationships between collections

### What You CANNOT Do ❌

**System Limitations:**
- **Cannot upload images directly** - Requires external URLs (Cloudinary/S3)
- **Cannot work without companion app** - Designer API requires MCP Bridge App
- **Cannot authorize without admin** - Owner/admin access required
- **Cannot exceed rate limits** - 60 API calls per minute maximum
- **Cannot access private assets** - Only public or authorized resources
- **Cannot modify locked elements** - Webflow's protected components

---

## 3. 🎨 DESIGNER API OPERATIONS

### Element Management

| Operation | Description | Parameters | Time |
|-----------|-------------|------------|------|
| createElement | Add element to canvas | type, parent, position | 1-2s |
| modifyElement | Change properties | id, properties | <1s |
| deleteElement | Remove from canvas | id | <1s |
| moveElement | Reposition | id, parent, position | <1s |

### Style Operations

| Operation | Description | Parameters | Time |
|-----------|-------------|------------|------|
| createClass | New style class | name, properties | <1s |
| applyClass | Add to element | element, class | <1s |
| modifyStyles | Update CSS | class, properties | <1s |
| createBreakpoint | Responsive rule | breakpoint, styles | 1-2s |

### Component System

| Operation | Description | Parameters | Time |
|-----------|-------------|------------|------|
| createComponent | Build reusable | elements, name | 5-10s |
| registerComponent | Make available | component | 1-2s |
| createInstance | Use component | component, parent | 1-2s |
| updateComponent | Modify definition | id, changes | 2-3s |

### Requirements
- **Companion App:** Must be open in Designer
- **Connection:** Real-time sync required
- **Permissions:** Write access to project

---

## 4. 📊 DATA API OPERATIONS

### Collection Management

| Operation | Description | Parameters | Time |
|-----------|-------------|------------|------|
| createCollection | New collection | name, fields | 3-5s |
| modifyCollection | Update structure | id, changes | 2-3s |
| deleteCollection | Remove collection | id | 1-2s |
| listCollections | Get all | - | <1s |

### Field Types Available

| Type | Description | Use Case |
|------|-------------|----------|
| PlainText | Single line text | Titles, names |
| RichText | Formatted content | Articles, descriptions |
| Number | Numeric values | Prices, quantities |
| Date | Date/time values | Publishing dates |
| Link | URL field | External links |
| Email | Email addresses | Contact info |
| Phone | Phone numbers | Contact info |
| Image | Image URL | Media (URL only) |
| File | File URL | Documents (URL only) |
| Reference | Link to item | Relationships |
| MultiReference | Multiple links | Categories, tags |
| Option | Single choice | Status, type |
| Switch | Boolean | Featured, active |
| Color | Color value | Theming |

### Content Operations

| Operation | Description | Parameters | Time |
|-----------|-------------|------------|------|
| createItem | Add content | collection, data | 2-3s |
| updateItem | Modify content | id, changes | 1-2s |
| deleteItem | Remove content | id | <1s |
| bulkCreate | Multiple items | items[] | 1-2s each |
| bulkUpdate | Mass changes | items[] | 1s each |

---

## 5. 🚀 PUBLISHING WORKFLOWS

### Publishing States

| State | Description | Visibility |
|-------|-------------|------------|
| Draft | Work in progress | Designers only |
| Staged | Ready for review | Internal team |
| Published | Live content | Public |

### Publishing Operations

| Operation | Description | Scope | Time |
|-----------|-------------|-------|------|
| publishItem | Single item | Item | 3-5s |
| publishCollection | All items | Collection | 5-10s |
| publishSite | Everything | Site | 10-30s |
| schedulePublish | Future publish | Items | 2-3s |

### Publishing Patterns
```
Development → Staging → Production
Draft → Review → Live
A/B Testing → Analysis → Deploy
```

---

## 6. ⚠️ LIMITATIONS

### Image Handling
**Problem:** Cannot upload images directly to Webflow
**Solution:** Use external hosting services

| Service | Free Tier | API | Best For |
|---------|-----------|-----|----------|
| Cloudinary | 25GB | Yes | General use |
| Amazon S3 | 5GB | Yes | Scale |
| Imgur | Unlimited | Yes | Quick hosting |
| Asset Manager | Manual | No | Small batches |

### Rate Limiting
```python
rate_limits = {
    'per_minute': 60,
    'safe_operating': 50,
    'warning_threshold': 55,
    'cooldown_period': 60  # seconds
}
```

### Access Requirements
- **Authentication:** OAuth 2.0
- **Scope:** Owner or Admin only
- **Companion App:** Required for Designer API
- **Network:** Stable connection required

---

## 7. 📈 PERFORMANCE METRICS

### Operation Benchmarks

| Operation | Small | Medium | Large |
|-----------|-------|--------|-------|
| **Structure Creation** |
| Collection | 3-5s | 5-8s | 8-12s |
| Fields (per field) | 1s | 1-2s | 2s |
| Relationships | 2-3s | 3-5s | 5-8s |
| **Design Operations** |
| Component | 5-10s | 10-15s | 15-20s |
| Styles | 1-2s | 2-3s | 3-5s |
| Page layout | 10-15s | 15-25s | 25-40s |
| **Content Operations** |
| Single item | 2-3s | 3-5s | 5-8s |
| Bulk (per item) | 1s | 1-2s | 2s |
| Publishing | 3-5s | 5-10s | 10-20s |

### Success Rates
- Collection creation: 95%
- Component building: 90%
- Content operations: 98%
- Publishing success: 95%
- API availability: 99.5%

---

## 8. 📌 API REFERENCE

### Designer API Endpoints

| Category | Operations | Authentication |
|----------|------------|----------------|
| Elements | Create, modify, delete, move | OAuth + App |
| Styles | Create, apply, modify classes | OAuth + App |
| Components | Define, register, instantiate | OAuth + App |
| Variables | Create, manage, apply | OAuth + App |
| Pages | Structure, SEO, settings | OAuth + App |

### Data API Endpoints

| Category | Operations | Authentication |
|----------|------------|----------------|
| Collections | CRUD operations | OAuth |
| Fields | Create, modify, delete | OAuth |
| Items | CRUD, bulk, publish | OAuth |
| Assets | Reference, organize | OAuth |
| Sites | Publish, settings | OAuth |

### Request Format
```javascript
{
  method: 'POST',
  headers: {
    'Authorization': 'Bearer {token}',
    'Content-Type': 'application/json'
  },
  body: {
    operation: 'createCollection',
    parameters: {...}
  }
}
```

---

## 9. 🚨 ERROR CODES

| Code | Meaning | Common Cause | Recovery |
|------|---------|--------------|----------|
| 200 | Success | Operation completed | Continue |
| 400 | Bad request | Invalid parameters | Check input |
| 401 | Unauthorized | Auth issue | Re-authenticate |
| 403 | Forbidden | Insufficient permissions | Check scope |
| 404 | Not found | Resource missing | Verify exists |
| 429 | Rate limited | Too many requests | Wait 60s |
| 500 | Server error | Webflow issue | Retry later |
| 503 | Unavailable | Maintenance | Wait and retry |

### Error Recovery Patterns
```javascript
if (error.code === 429) {
  await wait(60);
  retry();
} else if (error.code === 401) {
  await reauthorize();
  retry();
} else if (error.code >= 500) {
  await wait(10);
  retry(maxAttempts: 3);
}
```

---

## 10. ⚡ EMERGENCY COMMANDS

### System Commands

| Command | Function | Scope | Result |
|---------|----------|-------|--------|
| **$reset** | Clear all context | Global | Fresh start |
| **$status** | Show current state | Session | Display info |
| **$quick** | Fast execution | Current op | Skip steps |
| **$abort** | Cancel operation | Current | Stop safely |

### Command Effects on APIs

| Command | Designer API | Data API | Patterns |
|---------|-------------|----------|----------|
| $reset | Clears cache | Clears cache | Removes all |
| $status | Shows connection | Shows usage | Lists patterns |
| $quick | Minimal calls | Batch mode | Skip patterns |

### Usage Examples
```markdown
$reset - Start completely fresh
$status - Check API usage and patterns
$quick - Execute with minimal setup
```

---

## Quick Reference Card

### Decision Tree
```
Request received
    ↓
Needs visual elements? → Yes → Designer API (check app)
    ↓ No
Needs data structure? → Yes → Data API
    ↓ No
Content management? → Yes → Data API
    ↓ No
Ask for clarification
```

### Capability Check
```python
can_do = {
    'collections': True,
    'fields': True,
    'elements': True,  # with app
    'styles': True,    # with app
    'components': True, # with app
    'content': True,
    'publishing': True,
    'image_upload': False,  # URLs only
}
```

---

*Single source of truth for Webflow MCP capabilities. Reference this document for all technical specifications.*
