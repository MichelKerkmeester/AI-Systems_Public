# Webflow - MCP Knowledge - v0.313

Central knowledge system and single source of truth for Webflow capabilities through the MCP server with automatic UltraThink processing.

## 📋 Table of Contents

1. [🎯 OVERVIEW](#1--overview)
2. [📌 CONNECTION VERIFICATION](#2--connection-verification)
3. [📌 CORE CAPABILITIES](#3--core-capabilities)
4. [🎨 DESIGNER API OPERATIONS](#4--designer-api-operations)
5. [📊 DATA API OPERATIONS](#5--data-api-operations)
6. [🚀 PUBLISHING WORKFLOWS](#6--publishing-workflows)
7. [⚠️ LIMITATIONS](#7--limitations)
8. [📈 PERFORMANCE METRICS](#8--performance-metrics)
9. [📌 API REFERENCE](#9--api-reference)
10. [🚨 ERROR CODES](#10--error-codes)
11. [⚡ EMERGENCY COMMANDS](#11--emergency-commands)
12. [🧠 ULTRATHINK PROCESSING](#12--ultrathink-processing)

---

<a id="1--overview"></a>

## 1. 🎯 OVERVIEW

This document is the single source of truth for all Webflow MCP capabilities, API operations, and technical specifications. All operations use native Webflow APIs exclusively with automatic UltraThink processing - no custom code generation.

### MCP Server Details
- **Repository:** https://github.com/webflow/mcp-server
- **Protocol:** Model Context Protocol
- **APIs:** Designer API + Data API (native only)
- **Authentication:** OAuth with owner/admin scope
- **Custom Code:** NEVER generated (0%)
- **Thinking Mode:** UltraThink automatic (10 rounds)

### System Architecture
```
Connection Check → User Request → Intent Recognition → UltraThink Processing → API Selection → Native Operation → Feedback
                                                            ↓
                                            Designer API / Data API (Native Only)
                                                            ↓
                                                Companion App (if Designer)
```

### Core Principle
```markdown
✅ ALWAYS: Native Webflow Operations + UltraThink

• webflow:collections_create()
• webflow:components_create()
• webflow:pages_update_static_content()
• All official Webflow API calls
• Automatic UltraThink (10 rounds)

❌ NEVER: Custom Code or Thinking Questions

• No JavaScript generation
• No CSS creation
• No HTML templates
• Zero custom code
• Never ask about thinking depth
```

---

<a id="2--connection-verification"></a>

## 2. 📌 CONNECTION VERIFICATION

### Required Before ANY Operation

```markdown
🔧 Connection Protocol

1. Check MCP server status
2. Run test query (sites_list)
3. Verify authentication
4. Check companion app (if Designer)
5. Begin UltraThink processing
6. Proceed with operations
```

### Test Query Implementation
```javascript
// ALWAYS run before operations
async function verifyConnection() {
    try {
        await webflow:sites_list();
        return { 
            connected: true, 
            apis: 'ready',
            thinking: 'ultrathink' // Always 10 rounds
        };
    } catch (error) {
        // Apply REPAIR protocol
        return { connected: false, error: error };
    }
}
```

### Connection States
| State | Description | Action | Thinking |
|-------|-------------|--------|----------|
| Connected | All systems go | Proceed | UltraThink |
| Disconnected | No MCP access | Restart Claude | N/A |
| Auth Failed | OAuth issue | Re-authorize | N/A |
| App Missing | Designer unavailable | Launch app | UltraThink |

---

<a id="3--core-capabilities"></a>

## 3. 📌 CORE CAPABILITIES

### What You CAN Do ✅

**Designer API (Native Only + UltraThink):**
- Create elements using native API calls
- Apply styles through Designer API
- Build components with Webflow's system
- Manage variables via native operations
- Control breakpoints programmatically
- Design pages using API methods
- All with automatic UltraThink processing

**Data API (With UltraThink):**
- Create collections with custom fields
- Add any field type to collections
- Manage content items (CRUD operations)
- Handle publishing workflows
- Optimize SEO at scale
- Manage relationships between collections
- All with automatic UltraThink depth

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
- **Cannot ask about thinking depth** - UltraThink is automatic

---

<a id="4--designer-api-operations"></a>

## 4. 🎨 DESIGNER API OPERATIONS

### Native Element Management (With UltraThink)

| Operation | Description | Parameters | Time | Method | Thinking |
|-----------|-------------|------------|------|--------|----------|
| createElement | Add element via API | type, parent, position | 1-2s | Native | UltraThink |
| modifyElement | Change via API | id, properties | <1s | Native | UltraThink |
| deleteElement | Remove via API | id | <1s | Native | UltraThink |
| moveElement | Reposition via API | id, parent, position | <1s | Native | UltraThink |

### Native Style Operations (With UltraThink)

| Operation | Description | Parameters | Time | Method | Thinking |
|-----------|-------------|------------|------|--------|----------|
| createClass | New style via API | name, properties | <1s | Native | UltraThink |
| applyClass | Add via API | element, class | <1s | Native | UltraThink |
| modifyStyles | Update via API | class, properties | <1s | Native | UltraThink |
| createBreakpoint | Responsive via API | breakpoint, styles | 1-2s | Native | UltraThink |

### Native Component System (With UltraThink)

| Operation | Description | Parameters | Time | Method | Thinking |
|-----------|-------------|------------|------|--------|----------|
| createComponent | Build via API | elements, name | 5-10s | Native | UltraThink |
| registerComponent | Register natively | component | 1-2s | Native | UltraThink |
| createInstance | Use via API | component, parent | 1-2s | Native | UltraThink |
| updateComponent | Modify via API | id, changes | 2-3s | Native | UltraThink |

### Requirements
- **Connection:** MCP verified first
- **Companion App:** Must be open in Designer
- **Connection:** Real-time sync required
- **Permissions:** Write access to project
- **Method:** Native API calls only
- **Processing:** UltraThink automatic (10 rounds)

---

<a id="5--data-api-operations"></a>

## 5. 📊 DATA API OPERATIONS

### Collection Management (After Connection Verification + UltraThink)

| Operation | Description | Parameters | Time | Pre-Check | Thinking |
|-----------|-------------|------------|------|-----------|----------|
| createCollection | New collection | name, fields | 3-5s | Connection ✔ | UltraThink |
| modifyCollection | Update structure | id, changes | 2-3s | Connection ✔ | UltraThink |
| deleteCollection | Remove collection | id | 1-2s | Connection ✔ | UltraThink |
| listCollections | Get all | - | <1s | Connection ✔ | UltraThink |

### Field Types Available

| Type | Description | Use Case | Native | Processing |
|------|-------------|----------|---------|------------|
| PlainText | Single line text | Titles, names | ✔ | UltraThink |
| RichText | Formatted content | Articles | ✔ | UltraThink |
| Number | Numeric values | Prices | ✔ | UltraThink |
| Date | Date/time values | Publishing | ✔ | UltraThink |
| Link | URL field | External links | ✔ | UltraThink |
| Email | Email addresses | Contact info | ✔ | UltraThink |
| Phone | Phone numbers | Contact info | ✔ | UltraThink |
| Image | Image URL | Media (URL only) | ✔ | UltraThink |
| File | File URL | Documents (URL only) | ✔ | UltraThink |
| Reference | Link to item | Relationships | ✔ | UltraThink |
| MultiReference | Multiple links | Categories | ✔ | UltraThink |
| Option | Single choice | Status, type | ✔ | UltraThink |
| Switch | Boolean | Featured, active | ✔ | UltraThink |
| Color | Color value | Theming | ✔ | UltraThink |

### Content Operations

| Operation | Description | Parameters | Time | Method | Thinking |
|-----------|-------------|------------|------|--------|----------|
| createItem | Add content | collection, data | 2-3s | Native API | UltraThink |
| updateItem | Modify content | id, changes | 1-2s | Native API | UltraThink |
| deleteItem | Remove content | id | <1s | Native API | UltraThink |
| bulkCreate | Multiple items | items[] | 1-2s each | Native API | UltraThink |
| bulkUpdate | Mass changes | items[] | 1s each | Native API | UltraThink |

### Operation Prerequisites
```markdown
Before ANY Data Operation:

☑ MCP connection verified
☑ Test query successful
☑ Authentication valid
☑ Collection exists
☑ Fields configured
☑ Using native API calls
☑ UltraThink processing ready (automatic)
```

---

<a id="6--publishing-workflows"></a>

## 6. 🚀 PUBLISHING WORKFLOWS

### Publishing States (With UltraThink)

| State | Description | Visibility | Connection Required | Processing |
|-------|-------------|------------|-------------------|------------|
| Draft | Work in progress | Designers only | ✔ | UltraThink |
| Staged | Ready for review | Internal team | ✔ | UltraThink |
| Published | Live content | Public | ✔ | UltraThink |

### Publishing Operations

| Operation | Description | Scope | Time | Pre-Check | Thinking |
|-----------|-------------|-------|------|-----------|----------|
| publishItem | Single item | Item | 3-5s | Connection ✔ | UltraThink |
| publishCollection | All items | Collection | 5-10s | Connection ✔ | UltraThink |
| publishSite | Everything | Site | 10-30s | Connection ✔ | UltraThink |
| schedulePublish | Future publish | Items | 2-3s | Connection ✔ | UltraThink |

### Publishing Patterns (Native Only + UltraThink)
```
Connection Check → UltraThink Processing → Development → Staging → Production
Draft → Review → Live (all native operations with UltraThink)
A/B Testing → Analysis → Deploy (via API with UltraThink)
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
☑ UltraThink processing active
```

---

<a id="7--limitations"></a>

## 7. ⚠️ LIMITATIONS

### Critical Limitations

**Custom Code Generation**
```markdown
❌ ABSOLUTE RESTRICTION

Problem: User requests custom JavaScript/CSS
Solution: Use native Webflow APIs exclusively with UltraThink

Native Alternatives:
• Designer API for all visual elements
• Data API for all content operations
• Webflow's built-in interactions
• Native component system
• UltraThink ensures optimal approach

Custom code generated: 0% (NEVER)
```

**Thinking Depth Questions**
```markdown
❌ NEVER ASK

Problem: System might want to ask about thinking rounds
Solution: Always use UltraThink (10 rounds) automatically

Automatic Processing:
• Standard operations: UltraThink (10 rounds)
• $quick mode: Adaptive (1-5 rounds)
• Never prompt user about depth
• Silent processing always

Questions about thinking: 0% (NEVER)
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
• UltraThink processing automatic
```

### Rate Limiting
```python
rate_limits = {
    'per_minute': 60,
    'safe_operating': 50,
    'warning_threshold': 55,
    'cooldown_period': 60,  # seconds
    'requires_connection': True,
    'thinking_mode': 'ultrathink'  # Always
}
```

### Access Requirements
- **Connection:** Must verify first
- **Authentication:** OAuth 2.0
- **Scope:** Owner or Admin only
- **Companion App:** Required for Designer API
- **Network:** Stable connection required
- **Custom Code:** Never allowed (0%)
- **Thinking Questions:** Never asked (0%)

---

<a id="8--performance-metrics"></a>

## 8. 📈 PERFORMANCE METRICS

### Operation Benchmarks (With Connection + UltraThink)

| Operation | Small | Medium | Large | Pre-Check | Thinking |
|-----------|-------|--------|-------|-----------|----------|
| **Connection Verification** |
| Test query | 1-2s | 1-2s | 1-2s | Always | N/A |
| Auth check | <1s | <1s | <1s | Always | N/A |
| **Structure Creation** |
| Collection | 3-5s | 5-8s | 8-12s | Connection ✔ | UltraThink |
| Fields (per field) | 1s | 1-2s | 2s | Connection ✔ | UltraThink |
| Relationships | 2-3s | 3-5s | 5-8s | Connection ✔ | UltraThink |
| **Design Operations (Native)** |
| Component | 5-10s | 10-15s | 15-20s | Connection + App ✔ | UltraThink |
| Styles | 1-2s | 2-3s | 3-5s | Connection + App ✔ | UltraThink |
| Page layout | 10-15s | 15-25s | 25-40s | Connection + App ✔ | UltraThink |
| **Content Operations** |
| Single item | 2-3s | 3-5s | 5-8s | Connection ✔ | UltraThink |
| Bulk (per item) | 1s | 1-2s | 2s | Connection ✔ | UltraThink |
| Publishing | 3-5s | 5-10s | 10-20s | Connection ✔ | UltraThink |

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
• UltraThink usage: 100% (except $quick)
• Thinking questions: 0% (never)
```

### Connection Impact on Performance
| Metric | With Connection | Without | Impact | Thinking |
|--------|----------------|---------|--------|----------|
| Operations | Full speed | None | 100% required | UltraThink |
| Response time | 1-2s overhead | N/A | Minimal | Automatic |
| Success rate | 95%+ | 0% | Critical | UltraThink |
| Recovery | REPAIR protocol | Restart | Managed | N/A |

---

<a id="9--api-reference"></a>

## 9. 📌 API REFERENCE

### Designer API Endpoints (Native Only + UltraThink)

| Category | Operations | Authentication | Method | Processing |
|----------|------------|----------------|--------|------------|
| Elements | Create, modify, delete, move | OAuth + App | Native API | UltraThink |
| Styles | Create, apply, modify classes | OAuth + App | Native API | UltraThink |
| Components | Define, register, instantiate | OAuth + App | Native API | UltraThink |
| Variables | Create, manage, apply | OAuth + App | Native API | UltraThink |
| Pages | Structure, SEO, settings | OAuth + App | Native API | UltraThink |

### Data API Endpoints

| Category | Operations | Authentication | Method | Processing |
|----------|------------|----------------|--------|------------|
| Collections | CRUD operations | OAuth | Native API | UltraThink |
| Fields | Create, modify, delete | OAuth | Native API | UltraThink |
| Items | CRUD, bulk, publish | OAuth | Native API | UltraThink |
| Assets | Reference, organize | OAuth | Native API | UltraThink |
| Sites | Publish, settings | OAuth | Native API | UltraThink |

### Request Format (Native Operations with UltraThink)
```javascript
// ALWAYS verify connection first
await verifyConnection();

// UltraThink processes automatically
// No user prompt needed

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
    custom_code: false,  // Always false
    thinking_mode: 'ultrathink'  // Automatic 10 rounds
  }
}
```

### Native API Call Examples
```markdown
✅ CORRECT Native Calls (With UltraThink):

webflow:collections_create()
webflow:components_create()
webflow:pages_update_static_content()
webflow:collections_items_create_item_live()

All processed with UltraThink automatically

❌ NEVER These:

custom_javascript_function()
document.createElement()
style.innerHTML = 
Any custom code generation
Asking about thinking depth
```

---

<a id="10--error-codes"></a>

## 10. 🚨 ERROR CODES

### Connection-Related Errors

| Code | Meaning | Common Cause | Recovery | Processing |
|------|---------|--------------|----------|------------|
| 000 | No connection | MCP not connected | Verify connection first | N/A |
| 001 | Test failed | Query unsuccessful | Check config | N/A |
| 002 | Auth expired | Token timeout | Re-authorize | N/A |

### Standard API Errors

| Code | Meaning | Common Cause | Recovery | Processing |
|------|---------|--------------|----------|------------|
| 200 | Success | Operation completed | Continue | UltraThink |
| 400 | Bad request | Invalid parameters | Check input | UltraThink |
| 401 | Unauthorized | Auth issue | Re-authenticate | N/A |
| 403 | Forbidden | Insufficient permissions | Check scope | N/A |
| 404 | Not found | Resource missing | Verify exists | UltraThink |
| 429 | Rate limited | Too many requests | Wait 60s | Pause |
| 500 | Server error | Webflow issue | Retry later | UltraThink |
| 503 | Unavailable | Maintenance | Wait and retry | N/A |

### Custom Code Prevention Errors

| Code | Meaning | Prevention | Solution | Processing |
|------|---------|------------|----------|------------|
| CUS01 | Custom JS requested | Block generation | Use Designer API | UltraThink |
| CUS02 | Custom CSS requested | Block generation | Use native styles | UltraThink |
| CUS03 | HTML template requested | Block generation | Use components | UltraThink |

### Thinking Question Prevention Errors

| Code | Meaning | Prevention | Solution |
|------|---------|------------|----------|
| THK01 | Thinking question attempted | Block question | Use UltraThink automatically |
| THK02 | Depth prompt attempted | Block prompt | Apply 10 rounds silently |
| THK03 | User choice requested | Block request | Process automatically |

### Error Recovery Patterns
```javascript
// Connection check FIRST
if (!connection.verified) {
  await applyREPAIR('connection');
  return;
}

// Then handle API errors with UltraThink
if (error.code === 429) {
  await wait(60);
  retry();  // With UltraThink
} else if (error.code === 401) {
  await reauthorize();
  retry();
} else if (error.code >= 500) {
  await wait(10);
  retry(maxAttempts: 3);  // With UltraThink
} else if (error.code.startsWith('CUS')) {
  // Custom code requested - use native with UltraThink
  useNativeAPI();
} else if (error.code.startsWith('THK')) {
  // Thinking question blocked - use UltraThink silently
  processWithUltraThink();
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
P: Provide native alternative with UltraThink
A: Use Designer/Data API
I: Execute natively with UltraThink
R: Note preference

Thinking Question Attempt (THK01-03):

R: System attempted to ask about thinking
E: UltraThink is automatic
P: Process with 10 rounds silently
A: Apply UltraThink
I: Execute without prompting
R: Maintain automatic processing
```

---

<a id="11--emergency-commands"></a>

## 11. ⚡ EMERGENCY COMMANDS

### System Commands

| Command | Function | Scope | Result | Thinking |
|---------|----------|-------|--------|----------|
| **$reset** | Clear all context | Global | Fresh start + reconnect | Returns to UltraThink |
| **$status** | Show current state | Session | Display info + connection | Immediate |
| **$quick** | Fast execution | Current op | Skip steps (verify first) | Adaptive 1-5 |
| **$abort** | Cancel operation | Current | Stop safely | N/A |

### Command Effects on APIs

| Command | Connection | Designer API | Data API | Patterns | Thinking Mode |
|---------|------------|--------------|----------|----------|---------------|
| $reset | Re-verify | Clears cache | Clears cache | Removes all | UltraThink |
| $status | Shows status | Shows connection | Shows usage | Lists patterns | Shows mode |
| $quick | Quick verify | Minimal calls | Batch mode | Skip patterns | Adaptive 1-5 |

### Usage Examples
```markdown
$reset - Start completely fresh

✔ Context cleared
✔ Patterns removed
✔ Connection re-verified
✔ UltraThink restored
✔ Ready for native operations

$status - Check system state

• MCP Connection: Connected ✅
• Designer API: Ready (app open)
• Data API: Available
• Operations: 100% native
• Custom code: 0% (never)
• Thinking mode: UltraThink (10 rounds)
• Questions asked: 0% (never)

$quick - Execute with minimal setup

✔ Quick connection check
✔ No questions (automatic)
✔ Adaptive thinking (1-5 rounds)
✔ Fast native execution
```

---

<a id="12--ultrathink-processing"></a>

## 12. 🧠 ULTRATHINK PROCESSING

### Automatic Depth System

```markdown
Default Processing (No User Interaction):

• Standard operations: 10 rounds (UltraThink)
• Never asks user about depth
• Silent processing always
• Maximum quality results
```

### $quick Mode Adaptation

```markdown
When user types "$quick":

• Analyzes complexity automatically
• Applies 1-5 rounds based on:
  - Simple updates: 1 round
  - Basic operations: 2 rounds
  - Standard tasks: 3 rounds
  - Complex structures: 4 rounds
  - Multi-step processes: 5 rounds
• No user prompting
• Optimized for speed
```

### Processing Architecture

```python
class ThinkingSystem:
    def __init__(self):
        self.default_mode = 'ultrathink'
        self.default_rounds = 10
        self.quick_mode = False
        self.asks_user = False  # NEVER True
        
    def process_request(self, request):
        if request.startswith('$quick'):
            self.quick_mode = True
            rounds = self.analyze_complexity(request)  # 1-5
        else:
            rounds = self.default_rounds  # Always 10
        
        # Never ask user
        return self.execute_with_thinking(rounds)
```

### UltraThink Benefits

```markdown
Automatic 10-Round Processing Ensures:

✔ Comprehensive requirement analysis
✔ Optimal API selection
✔ Best practice application
✔ Error prevention
✔ Performance optimization
✔ Complete validation
✔ No user interruption
✔ Consistent quality
```

---


## Quick Reference Card

### Decision Tree
```
Request received
    ↓
Verify MCP connection → Failed → Apply REPAIR
    ↓ Success
Apply UltraThink (10 rounds) automatically
    ↓
Check for custom code → Requested → Use native APIs instead
    ↓ None
Needs visual elements? → Yes → Designer API (check app)
    ↓ No
Needs data structure? → Yes → Data API
    ↓ No
Content management? → Yes → Data API
    ↓ No
Ask for clarification (never about thinking)
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
    'native_operations': True,  # ALWAYS
    'ultrathink': True,  # AUTOMATIC
    'ask_thinking_depth': False  # NEVER
}
```

### Pre-Operation Protocol
```markdown
Every Operation Requires:

1. Connection verification ✔
2. Test query successful ✔
3. Native approach confirmed ✔
4. No custom code ✔
5. APIs identified ✔
6. UltraThink processing (automatic) ✔
7. Ready to execute ✔
```

### Native API Quick Reference (With UltraThink)
```javascript
// Collections (Data API + UltraThink)
webflow:collections_create(site_id, {displayName, singularName})
webflow:collections_list(site_id)
webflow:collections_get(collection_id)

// Fields (Data API + UltraThink)
webflow:collection_fields_create_static(collection_id, {type, displayName})
webflow:collection_fields_create_option(collection_id, {metadata})
webflow:collection_fields_create_reference(collection_id, {metadata})

// Components (Designer API + UltraThink - requires app)
webflow:components_create(site_id, {structure})
webflow:components_get_content(site_id, component_id)
webflow:components_update_content(site_id, component_id, {nodes})

// Pages (Designer API + UltraThink - requires app)
webflow:pages_list(site_id)
webflow:pages_update_static_content(page_id, {nodes})
webflow:pages_update_page_settings(page_id, {body})

// Publishing (Data API + UltraThink)
webflow:collections_items_create_item_live(collection_id, {items})
webflow:collections_items_publish_items(collection_id, itemIds)
webflow:sites_publish(site_id, {domains})

// All operations use UltraThink automatically
```

### Critical Rules Summary
```markdown
THE SIX ABSOLUTES:

1. Connection verified before EVERY operation
2. Native APIs ONLY - zero custom code
3. Test query must pass before proceeding
4. Companion app required for Designer
5. REPAIR protocol for all errors
6. UltraThink automatic - NEVER ask about depth
```

---


## System Mantras

> "Connection first. Native operations only. UltraThink automatic."

> "Verify, test, execute - all through native Webflow APIs with UltraThink."

> "MCP connected → UltraThink processing → Native APIs → Success. Always this path."

> "Never ask about thinking. Always process with maximum depth."

---

*Single source of truth for Webflow MCP capabilities. Connection required. Native APIs only. UltraThink automatic - never asks. Reference this document for all technical specifications.*