# Webflow - MCP Knowledge - v0.314

Central knowledge system and single source of truth for Webflow capabilities through the MCP server.

## 📋 Table of Contents

1. [🎯 OVERVIEW](#1--overview)
2. [🔌 CONNECTION VERIFICATION](#2--connection-verification)
3. [📌 CORE CAPABILITIES](#3--core-capabilities)
4. [🎨 DESIGNER API OPERATIONS](#4--designer-api-operations)
5. [📊 DATA API OPERATIONS](#5--data-api-operations)
6. [🚀 PUBLISHING WORKFLOWS](#6--publishing-workflows)
7. [⚠️ LIMITATIONS](#7--limitations)
8. [📈 PERFORMANCE METRICS](#8--performance-metrics)
9. [📌 API REFERENCE](#9--api-reference)
10. [🚨 ERROR CODES](#10--error-codes)

---

<a id="1--overview"></a>

## 1. 🎯 OVERVIEW

This document is the single source of truth for all Webflow MCP capabilities, API operations, and technical specifications. All operations use native Webflow APIs exclusively - no custom code generation.

### MCP Server Details
- **Repository:** https://github.com/webflow/mcp-server
- **Protocol:** Model Context Protocol
- **APIs:** Designer API + Data API (native only)
- **Authentication:** OAuth with owner/admin scope
- **Custom Code:** NEVER generated (0%)

### System Architecture
```
Connection Check → User Request → Intent Recognition → API Selection → Native Operation → Feedback
                                                            ↓
                                            Designer API / Data API (Native Only)
                                                            ↓
                                                Companion App (if Designer)
```

### Core Principle
```markdown
✅ ALWAYS: Native Webflow Operations

• webflow:collections_create()
• webflow:components_create()
• webflow:pages_update_static_content()
• All official Webflow API calls

❌ NEVER: Custom Code

• No JavaScript generation
• No CSS creation
• No HTML templates
• Zero custom code
```

---

<a id="2--connection-verification"></a>

## 2. 🔌 CONNECTION VERIFICATION

### Required Before ANY Operation

```markdown
🔧 Connection Protocol

1. Check MCP server status
2. Run test query (sites_list)
3. Verify authentication
4. Check companion app (if Designer)
5. Proceed with operations
```

### Test Query Implementation
```javascript
// ALWAYS run before operations
async function verifyConnection() {
    try {
        await webflow:sites_list();
        return { 
            connected: true, 
            apis: 'ready'
        };
    } catch (error) {
        // Apply REPAIR protocol
        return { connected: false, error: error };
    }
}
```

### Connection States
| State | Description | Action |
|-------|-------------|--------|
| Connected | All systems go | Proceed |
| Disconnected | No MCP access | Restart Claude |
| Auth Failed | OAuth issue | Re-authorize |
| App Missing | Designer unavailable | Launch app |

---

<a id="3--core-capabilities"></a>

## 3. 📌 CORE CAPABILITIES

### What You CAN Do ✅

**Designer API (Native Only):**
- Create elements using native API calls
- Apply styles through Designer API
- Build components with Webflow's system
- Manage variables via native operations
- Control breakpoints programmatically
- Design pages using API methods

**Data API:**
- Create collections with custom fields
- Add any field type to collections
- Manage content items (CRUD operations)
- Handle publishing workflows
- Optimize SEO at scale
- Manage relationships between collections

### What You CANNOT Do ❌

**System Limitations:**
- **Cannot generate custom code** - Native APIs only
- **Cannot upload images directly** - Requires external URLs
- **Cannot work without connection** - MCP must be verified
- **Cannot work without companion app** - Designer API requires MCP Bridge App
- **Cannot authorize without admin** - Owner/admin access required
- **Cannot exceed rate limits** - 60 API calls per minute maximum
- **Cannot access private assets** - Only public or authorized resources
- **Cannot modify locked elements** - Webflow's protected components

---

<a id="4--designer-api-operations"></a>

## 4. 🎨 DESIGNER API OPERATIONS

### Native Element Management

| Operation | Description | Parameters | Time | Method |
|-----------|-------------|------------|------|--------|
| createElement | Add element via API | type, parent, position | 1-2s | Native |
| modifyElement | Change via API | id, properties | <1s | Native |
| deleteElement | Remove via API | id | <1s | Native |
| moveElement | Reposition via API | id, parent, position | <1s | Native |

### Native Style Operations

| Operation | Description | Parameters | Time | Method |
|-----------|-------------|------------|------|--------|
| createClass | New style via API | name, properties | <1s | Native |
| applyClass | Add via API | element, class | <1s | Native |
| modifyStyles | Update via API | class, properties | <1s | Native |
| createBreakpoint | Responsive via API | breakpoint, styles | 1-2s | Native |

### Native Component System

| Operation | Description | Parameters | Time | Method |
|-----------|-------------|------------|------|--------|
| createComponent | Build via API | elements, name | 5-10s | Native |
| registerComponent | Register natively | component | 1-2s | Native |
| createInstance | Use via API | component, parent | 1-2s | Native |
| updateComponent | Modify via API | id, changes | 2-3s | Native |

### Requirements
- **Connection:** MCP verified first
- **Companion App:** Must be open in Designer
- **Connection:** Real-time sync required
- **Permissions:** Write access to project
- **Method:** Native API calls only

---

<a id="5--data-api-operations"></a>

## 5. 📊 DATA API OPERATIONS

### Collection Management (After Connection Verification)

| Operation | Description | Parameters | Time | Pre-Check |
|-----------|-------------|------------|------|-----------|
| createCollection | New collection | name, fields | 3-5s | Connection ✓ |
| modifyCollection | Update structure | id, changes | 2-3s | Connection ✓ |
| deleteCollection | Remove collection | id | 1-2s | Connection ✓ |
| listCollections | Get all | - | <1s | Connection ✓ |

### Field Types Available

| Type | Description | Use Case | Native |
|------|-------------|----------|---------|
| PlainText | Single line text | Titles, names | ✓ |
| RichText | Formatted content | Articles | ✓ |
| Number | Numeric values | Prices | ✓ |
| Date | Date/time values | Publishing | ✓ |
| Link | URL field | External links | ✓ |
| Email | Email addresses | Contact info | ✓ |
| Phone | Phone numbers | Contact info | ✓ |
| Image | Image URL | Media (URL only) | ✓ |
| File | File URL | Documents (URL only) | ✓ |
| Reference | Link to item | Relationships | ✓ |
| MultiReference | Multiple links | Categories | ✓ |
| Option | Single choice | Status, type | ✓ |
| Switch | Boolean | Featured, active | ✓ |
| Color | Color value | Theming | ✓ |

### Content Operations

| Operation | Description | Parameters | Time | Method |
|-----------|-------------|------------|------|--------|
| createItem | Add content | collection, data | 2-3s | Native API |
| updateItem | Modify content | id, changes | 1-2s | Native API |
| deleteItem | Remove content | id | <1s | Native API |
| bulkCreate | Multiple items | items[] | 1-2s each | Native API |
| bulkUpdate | Mass changes | items[] | 1s each | Native API |

### Operation Prerequisites
```markdown
Before ANY Data Operation:

☑ MCP connection verified
☑ Test query successful
☑ Authentication valid
☑ Collection exists
☑ Fields configured
☑ Using native API calls
```

---

<a id="6--publishing-workflows"></a>

## 6. 🚀 PUBLISHING WORKFLOWS

### Publishing States

| State | Description | Visibility | Connection Required |
|-------|-------------|------------|-------------------|
| Draft | Work in progress | Designers only | ✓ |
| Staged | Ready for review | Internal team | ✓ |
| Published | Live content | Public | ✓ |

### Publishing Operations

| Operation | Description | Scope | Time | Pre-Check |
|-----------|-------------|-------|------|-----------|
| publishItem | Single item | Item | 3-5s | Connection ✓ |
| publishCollection | All items | Collection | 5-10s | Connection ✓ |
| publishSite | Everything | Site | 10-30s | Connection ✓ |
| schedulePublish | Future publish | Items | 2-3s | Connection ✓ |

### Publishing Patterns (Native Only)
```
Connection Check → Development → Staging → Production
Draft → Review → Live (all native operations)
A/B Testing → Analysis → Deploy (via API)
```

### Publishing Protocol
```markdown
🔧 Publishing Checklist

☑ Connection verified
☑ Content validated
☑ SEO fields complete
☑ Relationships set
☑ Using native publish API
☑ No custom scripts
```

---

<a id="7--limitations"></a>

## 7. ⚠️ LIMITATIONS

### Critical Limitations

**Custom Code Generation**
```markdown
❌ ABSOLUTE RESTRICTION

Problem: User requests custom JavaScript/CSS
Solution: Use native Webflow APIs exclusively

Native Alternatives:
• Designer API for all visual elements
• Data API for all content operations
• Webflow's built-in interactions
• Native component system

Custom code generated: 0% (NEVER)
```

### Image Handling
**Problem:** Cannot upload images directly to Webflow
**Solution:** Use external hosting services

| Service | Free Tier | API | Best For |
|---------|-----------|-----|----------|
| Cloudinary | 25GB | Yes | General use |
| Amazon S3 | 5GB | Yes | Scale |
| Imgur | Unlimited | Yes | Quick hosting |
| Asset Manager | Manual | No | Small batches |

### Connection Requirements
```markdown
Connection Dependencies:

• MCP server must be connected
• OAuth must be authorized
• Test query must pass
• Companion app for Designer
• Rate limits respected
```

### Rate Limiting
```python
rate_limits = {
    'per_minute': 60,
    'safe_operating': 50,
    'warning_threshold': 55,
    'cooldown_period': 60,  # seconds
    'requires_connection': True
}
```

### Access Requirements
- **Connection:** Must verify first
- **Authentication:** OAuth 2.0
- **Scope:** Owner or Admin only
- **Companion App:** Required for Designer API
- **Network:** Stable connection required
- **Custom Code:** Never allowed (0%)

---

<a id="8--performance-metrics"></a>

## 8. 📈 PERFORMANCE METRICS

### Operation Benchmarks (With Connection)

| Operation | Small | Medium | Large | Pre-Check |
|-----------|-------|--------|-------|-----------|
| **Connection Verification** |
| Test query | 1-2s | 1-2s | 1-2s | Always |
| Auth check | <1s | <1s | <1s | Always |
| **Structure Creation** |
| Collection | 3-5s | 5-8s | 8-12s | Connection ✓ |
| Fields (per field) | 1s | 1-2s | 2s | Connection ✓ |
| Relationships | 2-3s | 3-5s | 5-8s | Connection ✓ |
| **Design Operations (Native)** |
| Component | 5-10s | 10-15s | 15-20s | Connection + App ✓ |
| Styles | 1-2s | 2-3s | 3-5s | Connection + App ✓ |
| Page layout | 10-15s | 15-25s | 25-40s | Connection + App ✓ |
| **Content Operations** |
| Single item | 2-3s | 3-5s | 5-8s | Connection ✓ |
| Bulk (per item) | 1s | 1-2s | 2s | Connection ✓ |
| Publishing | 3-5s | 5-10s | 10-20s | Connection ✓ |

### Success Rates
```markdown
Performance Metrics:

• Connection verification: 99%
• Collection creation: 95%
• Component building: 90% (native)
• Content operations: 98%
• Publishing success: 95%
• API availability: 99.5%
• Custom code usage: 0% (never)
• Native operations: 100%
```

### Connection Impact on Performance
| Metric | With Connection | Without | Impact |
|--------|----------------|---------|--------|
| Operations | Full speed | None | 100% required |
| Response time | 1-2s overhead | N/A | Minimal |
| Success rate | 95%+ | 0% | Critical |
| Recovery | REPAIR protocol | Restart | Managed |

---

<a id="9--api-reference"></a>

## 9. 📌 API REFERENCE

### Designer API Endpoints (Native Only)

| Category | Operations | Authentication | Method |
|----------|------------|----------------|--------|
| Elements | Create, modify, delete, move | OAuth + App | Native API |
| Styles | Create, apply, modify classes | OAuth + App | Native API |
| Components | Define, register, instantiate | OAuth + App | Native API |
| Variables | Create, manage, apply | OAuth + App | Native API |
| Pages | Structure, SEO, settings | OAuth + App | Native API |

### Data API Endpoints

| Category | Operations | Authentication | Method |
|----------|------------|----------------|--------|
| Collections | CRUD operations | OAuth | Native API |
| Fields | Create, modify, delete | OAuth | Native API |
| Items | CRUD, bulk, publish | OAuth | Native API |
| Assets | Reference, organize | OAuth | Native API |
| Sites | Publish, settings | OAuth | Native API |

### Request Format (Native Operations)
```javascript
// ALWAYS verify connection first
await verifyConnection();

// Then execute native operation
{
  method: 'POST',
  headers: {
    'Authorization': 'Bearer {token}',
    'Content-Type': 'application/json'
  },
  body: {
    operation: 'createCollection',  // Native API operation
    parameters: {...},
    custom_code: false  // Always false
  }
}
```

### Native API Call Examples
```markdown
✅ CORRECT Native Calls:

webflow:collections_create()
webflow:components_create()
webflow:pages_update_static_content()
webflow:collections_items_create_item_live()

❌ NEVER These:

custom_javascript_function()
document.createElement()
style.innerHTML = 
Any custom code generation
```

---

<a id="10--error-codes"></a>

## 10. 🚨 ERROR CODES

### Connection-Related Errors

| Code | Meaning | Common Cause | Recovery |
|------|---------|--------------|----------|
| 000 | No connection | MCP not connected | Verify connection first |
| 001 | Test failed | Query unsuccessful | Check config |
| 002 | Auth expired | Token timeout | Re-authorize |

### Standard API Errors

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

### Custom Code Prevention Errors

| Code | Meaning | Prevention | Solution |
|------|---------|------------|----------|
| CUS01 | Custom JS requested | Block generation | Use Designer API |
| CUS02 | Custom CSS requested | Block generation | Use native styles |
| CUS03 | HTML template requested | Block generation | Use components |

### Error Recovery Patterns
```javascript
// Connection check FIRST
if (!connection.verified) {
  await applyREPAIR('connection');
  return;
}

// Then handle API errors
if (error.code === 429) {
  await wait(60);
  retry();
} else if (error.code === 401) {
  await reauthorize();
  retry();
} else if (error.code >= 500) {
  await wait(10);
  retry(maxAttempts: 3);
} else if (error.code.startsWith('CUS')) {
  // Custom code requested - use native
  useNativeAPI();
}
```

### REPAIR Protocol for Errors
```markdown
Connection Lost (000):

R: No MCP connection
E: Cannot perform operations
P: Restart Claude or check config
A: Based on user choice
I: Test connection
R: Log issue

Custom Code Request (CUS01-03):

R: Custom code requested
E: System uses native APIs only
P: Provide native alternative
A: Use Designer/Data API
I: Execute natively
R: Note preference
```

---

## Quick Reference Card

### Decision Tree
```
Request received
    ↓
Verify MCP connection → Failed → Apply REPAIR
    ↓ Success
Check for custom code → Requested → Use native APIs instead
    ↓ None
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
    'connection_required': True,  # Always
    'collections': True,
    'fields': True,
    'elements': True,  # with app
    'styles': True,    # with app
    'components': True, # with app
    'content': True,
    'publishing': True,
    'image_upload': False,  # URLs only
    'custom_code': False,   # NEVER
    'native_operations': True  # ALWAYS
}
```

### Pre-Operation Protocol
```markdown
Every Operation Requires:

1. Connection verification ✓
2. Test query successful ✓
3. Native approach confirmed ✓
4. No custom code ✓
5. APIs identified ✓
6. Ready to execute ✓
```

### Native API Quick Reference
```javascript
// Collections (Data API)
webflow:collections_create(site_id, {displayName, singularName})
webflow:collections_list(site_id)
webflow:collections_get(collection_id)

// Fields (Data API)
webflow:collection_fields_create_static(collection_id, {type, displayName})
webflow:collection_fields_create_option(collection_id, {metadata})
webflow:collection_fields_create_reference(collection_id, {metadata})

// Components (Designer API - requires app)
webflow:components_create(site_id, {structure})
webflow:components_get_content(site_id, component_id)
webflow:components_update_content(site_id, component_id, {nodes})

// Pages (Designer API - requires app)
webflow:pages_list(site_id)
webflow:pages_update_static_content(page_id, {nodes})
webflow:pages_update_page_settings(page_id, {body})

// Publishing (Data API)
webflow:collections_items_create_item_live(collection_id, {items})
webflow:collections_items_publish_items(collection_id, itemIds)
webflow:sites_publish(site_id, {domains})
```

### Critical Rules Summary
```markdown
THE FIVE ABSOLUTES:

1. Connection verified before EVERY operation
2. Native APIs ONLY - zero custom code
3. Test query must pass before proceeding
4. Companion app required for Designer
5. REPAIR protocol for all errors
```

---

## System Mantras

> "Connection first. Native operations only."

> "Verify, test, execute - all through native Webflow APIs."

> "MCP connected → Native APIs → Success. Always this path."