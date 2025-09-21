# Webflow - Patterns & Workflows - v0.313

Pattern library for Webflow operations through natural language using native APIs only with automatic UltraThink processing.

## 📋 Table of Contents

1. [🎯 OVERVIEW](#1--overview)
2. [📌 CONNECTION PATTERNS](#2--connection-patterns)
3. [💬 INTENT PATTERNS](#3--intent-patterns)
4. [📁 STRUCTURE PATTERNS](#4--structure-patterns)
5. [🎨 COMPONENT PATTERNS](#5--component-patterns)
6. [📊 CONTENT PATTERNS](#6--content-patterns)
7. [🚀 WORKFLOW PATTERNS](#7--workflow-patterns)
8. [🧠 THINKING PATTERNS](#8--thinking-patterns)
9. [⚡ EMERGENCY PATTERNS](#9--emergency-patterns)

---

<a id="1--overview"></a>

## 1. 🎯 OVERVIEW

This document defines pattern recognition and workflow orchestration for natural language Webflow requests. All patterns use native Webflow APIs exclusively with automatic UltraThink processing - no custom code generation.

### Pattern Categories
- **Connection Verification** - Always check MCP first
- **Intent Recognition** - What user wants to achieve
- **Structure Creation** - Collections and fields (native)
- **Component Building** - Visual elements (native)
- **Content Management** - CRUD operations
- **Complete Workflows** - Multi-step processes
- **Emergency Recovery** - Quick commands
- **UltraThink Processing** - Automatic 10 rounds

### Core Pattern Principle
```markdown
Every Pattern Follows:

1. Verify MCP connection
2. Apply UltraThink automatically (10 rounds)
3. Identify native API approach
4. Reject custom code requests
5. Execute with Webflow APIs
6. Provide native solutions only
7. Never ask about thinking depth
```

---

<a id="2--connection-patterns"></a>

## 2. 📌 CONNECTION PATTERNS

### Initial Connection Pattern
```yaml
Pattern: Connection Verification
Priority: ALWAYS FIRST
Processing: Before UltraThink
Steps:
  1. Check MCP server status
  2. Run test query (sites_list)
  3. Verify authentication
  4. Check companion app if needed
  5. Begin UltraThink processing
  6. Proceed or apply REPAIR
```

### Connection States

| State | Pattern | Action | Next | Thinking |
|-------|---------|--------|------|----------|
| Connected | Proceed | Execute request | Native ops | UltraThink |
| Disconnected | REPAIR | Restart Claude | Re-verify | N/A |
| Auth Failed | REPAIR | Re-authorize | Re-verify | N/A |
| App Missing | Conditional | Check if Designer needed | Proceed/Launch | UltraThink |

### Recovery Patterns
```markdown
Connection Lost Pattern:

Trigger: Any API call fails
Response:
  1. Immediate connection check
  2. Apply REPAIR protocol
  3. Guide user to fix
  4. Re-verify before retry
  5. Resume with UltraThink
  6. Never attempt without connection
```

---

<a id="3--intent-patterns"></a>

## 3. 💬 INTENT PATTERNS

### Creation Intents (Native Only + UltraThink)

| User Says | Intent | Default Action | Processing | Method |
|-----------|--------|---------------|------------|--------|
| "create blog" | Blog structure | Collections + fields | UltraThink (10) | Native API |
| "build component" | Component | Elements + styles | UltraThink (10) | Native API |
| "design page" | Full page | Layout + components | UltraThink (10) | Native API |
| "add field" | Field addition | Add to collection | UltraThink (10) | Native API |
| "update content" | Content edit | Modify items | UltraThink (10) | Native API |
| "publish site" | Publishing | Deploy changes | UltraThink (10) | Native API |
| "$quick create" | Fast creation | Quick structure | Adaptive (1-5) | Native API |

### Custom Code Intent Handling

| User Says | Intent | Response | Alternative | Processing |
|-----------|--------|----------|-------------|------------|
| "write JavaScript" | Custom code | Reject | Use Designer API | UltraThink |
| "custom CSS" | Custom style | Reject | Use native styles | UltraThink |
| "HTML template" | Custom HTML | Reject | Use components | UltraThink |
| "add script" | Custom script | Reject | Use interactions | UltraThink |

### Management Intents

| User Says | Intent | Default Action | Processing | Pre-Check |
|-----------|--------|---------------|------------|-----------|
| "edit items" | Content update | Bulk modify | UltraThink (10) | Connection ✔ |
| "delete old" | Cleanup | Remove items | UltraThink (10) | Connection ✔ |
| "reorganize" | Structure change | Modify relations | UltraThink (10) | Connection ✔ |
| "optimize SEO" | SEO update | Meta fields | UltraThink (10) | Connection ✔ |

### Intent Recognition Flow
```markdown
User Request
    ↓
Connection Check ─── Failed → REPAIR
    ↓ Success
UltraThink Processing (Automatic)
    ↓
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

### Blog System Pattern (Native API + UltraThink)
```yaml
Pattern: Complete Blog
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
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
User_Prompts: NEVER
```

### E-commerce Pattern (Native API + UltraThink)
```yaml
Pattern: Product Catalog
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
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
Thinking_Questions: NEVER
```

### Portfolio Pattern (Native API + UltraThink)
```yaml
Pattern: Project Showcase
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
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
Depth_Prompts: NEVER
```

### Structure Creation Protocol
```markdown
For Every Structure:

1. Verify MCP connection
2. Apply UltraThink automatically
3. Use webflow:collections_create()
4. Add fields via native API
5. Configure relationships natively
6. No custom validation scripts
7. Apply SEO via native fields
8. Never ask about processing depth
```

---

<a id="5--component-patterns"></a>

## 5. 🎨 COMPONENT PATTERNS

### Card Component (Native Designer API + UltraThink)
```yaml
Pattern: Reusable Card
Connection: Verify + App check
Processing: UltraThink (10 rounds automatic)
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
Ask_User: NEVER
```

### Navigation Component (Native Designer API + UltraThink)
```yaml
Pattern: Responsive Nav
Connection: Verify + App check
Processing: UltraThink (10 rounds automatic)
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
Thinking_Prompt: NEVER
```

### Hero Section (Native Designer API + UltraThink)
```yaml
Pattern: Landing Hero
Connection: Verify + App check
Processing: UltraThink (10 rounds automatic)
Method: Native Designer API only
Structure:
  HeroContainer:
    - Background: native image/video
    - Content: native centered/left
    - Headline: native h1 styling
    - Subheadline: native h2 styling
    - CTAButtons: native primary/secondary
Custom_Code: NEVER
User_Questions: NEVER
```

### Component Creation Protocol
```markdown
For Every Component:

1. Verify MCP connection
2. Check companion app status
3. Apply UltraThink automatically
4. Use webflow:components_create()
5. Apply styles via Designer API
6. Register component natively
7. No custom JavaScript
8. No custom CSS
9. Use native interactions only
10. Never ask about depth
```

### Native Component Alternatives
```markdown
When User Requests Custom:

"Custom animation" → Webflow Interactions + UltraThink
"Custom styling" → Designer API styles + UltraThink
"Custom behavior" → Native components + UltraThink
"Custom layout" → Flexbox/Grid via API + UltraThink
"Custom effects" → Native hover states + UltraThink

All with automatic UltraThink processing
```

---

<a id="6--content-patterns"></a>

## 6. 📊 CONTENT PATTERNS

### Bulk Operations (Native API + UltraThink)
```yaml
Pattern: Mass Update
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
Method: Native Data API only
Process:
  - Check connection status
  - Apply UltraThink processing
  - Batch by 20 items
  - Monitor rate limits
  - Progress feedback
  - Error handling via REPAIR
  - Use webflow:collections_items_update_items()
Example: Update all prices by 10%
Custom_Scripts: NEVER
Depth_Questions: NEVER
```

### Content Migration (Native API + UltraThink)
```yaml
Pattern: Data Transfer
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
Method: Native Data API only
Process:
  - Verify connection
  - Apply UltraThink processing
  - Export source via API
  - Transform structure natively
  - Map relationships via API
  - Import to target via API
  - Verify integrity
  - No custom migration scripts
  - No user prompts
```

### Publishing Workflow (Native API + UltraThink)
```yaml
Pattern: Staged Deploy
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
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
Ask_About_Depth: NEVER
```

### Content Operation Protocol
```markdown
For Every Content Operation:

1. Verify MCP connection
2. Apply UltraThink automatically
3. Check rate limits
4. Use native CRUD APIs
5. Batch operations properly
6. No custom validation
7. No custom scripts
8. Handle errors with REPAIR
9. Never ask about processing
```

---

<a id="7--workflow-patterns"></a>

## 7. 🚀 WORKFLOW PATTERNS

### Complete Website Setup (Native + UltraThink)
```yaml
Pattern: Full Site
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
Method: 100% Native APIs
Steps:
  1. Verify MCP connection
  2. Begin UltraThink processing (silent)
  3. Create all collections (Data API)
  4. Configure relationships (Data API)
  5. Build page templates (Designer API)
  6. Design components (Designer API)
  7. Add sample content (Data API)
  8. Configure SEO (Data API)
  9. Set up publishing (Data API)
Custom_Code: ZERO
User_Prompts: ZERO
```

### Design System Creation (Native + UltraThink)
```yaml
Pattern: Component Library
Connection: Verify + App check
Processing: UltraThink (10 rounds automatic)
Method: Native Designer API only
Steps:
  1. Verify connection + app
  2. Apply UltraThink silently
  3. Define typography (Designer API)
  4. Create color system (Designer API)
  5. Build base components (Designer API)
  6. Create variants (Designer API)
  7. Document usage (native)
  8. Register globally (Designer API)
Custom_CSS_Framework: NEVER
Thinking_Questions: NEVER
```

### Content Population (Native + UltraThink)
```yaml
Pattern: Initial Content
Connection: Verify first
Processing: UltraThink (10 rounds automatic)
Method: Native Data API only
Steps:
  1. Verify connection
  2. UltraThink processes automatically
  3. Import/create items (Data API)
  4. Set relationships (Data API)
  5. Add media URLs (external)
  6. Configure SEO (Data API)
  7. Publish drafts (Publishing API)
Custom_Import_Scripts: NEVER
Depth_Prompts: NEVER
```

### Workflow Execution Protocol
```markdown
Every Workflow Must:

☑ Start with connection check
☑ Apply UltraThink automatically
☑ Use native APIs exclusively
☑ Reject custom code requests
☑ Apply REPAIR for errors
☑ Monitor rate limits
☑ Provide native alternatives
☑ Complete with native operations
☑ Never ask about thinking depth
```

### Multi-Step Workflow Pattern
```markdown
Complex Workflow Structure:

BEGIN
  → Verify MCP Connection
    → Failed? Apply REPAIR
  → Start UltraThink Processing (automatic)
  → Check all required APIs
  → Confirm native approach
  → Execute Step 1 (native)
  → Execute Step 2 (native)
  → ... (all native)
  → Verify completion
END (100% native execution with UltraThink)
```

---

<a id="8--thinking-patterns"></a>

## 8. 🧠 THINKING PATTERNS

### Automatic Depth System (No User Interaction)

| Operation | UltraThink | $quick Mode | Pre-Req |
|-----------|------------|-------------|---------|
| Simple update | 10 rounds | 1-2 rounds | Connection ✔ |
| Create collection | 10 rounds | 2-3 rounds | Connection ✔ |
| Build component | 10 rounds | 3-4 rounds | Connection + App ✔ |
| Design page | 10 rounds | 4-5 rounds | Connection + App ✔ |
| Full site | 10 rounds | 5 rounds (max) | All verified ✔ |

### Processing Display Patterns
```markdown
Standard Processing (Default):

✔ Connection verified
✔ UltraThink activated
✔ Never asks user
✔ Shows: "Processing with UltraThink..."
✔ Executes with 10 rounds
```

```markdown
Quick Mode Processing ($quick):

✔ Connection verified
✔ Adaptive thinking
✔ Never asks user
✔ Shows: "⚡ Quick Mode: Processing..."
✔ Executes with 1-5 rounds
```

### Never Ask Pattern
```markdown
BLOCKED PATTERNS - Never Execute:

✗ "How many thinking rounds?"
✗ "Choose your depth (1-10)"
✗ "Would you like deep analysis?"
✗ "Select processing level"
✗ Any variation of thinking questions

ALWAYS INSTEAD:

✔ Apply UltraThink silently
✔ Show "Processing..." message
✔ Execute immediately
```

### Thinking Pattern Flow
```markdown
Connection Verified
    ↓
UltraThink Activated Automatically
    ↓
"Processing with UltraThink..."
    ↓
Execute with native APIs
    ↓
Deliver results
```

---

<a id="9--emergency-patterns"></a>

## 9. ⚡ EMERGENCY PATTERNS

### Command Patterns

| Pattern | Command | Effect | Example | Connection | Thinking |
|---------|---------|--------|---------|------------|----------|
| **Fresh Start** | $reset | Clear everything | "Things are confused, $reset" | Re-verify | UltraThink |
| **Quick Execute** | $quick | Minimal process | "$quick create blog" | Quick check | Adaptive 1-5 |
| **Check State** | $status | Show context | "What's happening? $status" | Show status | Immediate |

### Recovery Workflows

**Pattern: MCP Disconnected**
```yaml
Trigger: Connection lost
Command Options:
  - $status - Check connection
  - $reset - Clear and reconnect
Recovery:
  1. Inform user immediately
  2. Show connection status
  3. Offer reconnection steps
  4. Apply REPAIR protocol
  5. Re-verify before retry
  6. Resume with UltraThink
```

**Pattern: Companion Disconnected**
```yaml
Trigger: Designer API fails
Command Options:
  - $status - Check app connection
  - $quick - Try Data API only
  - $reset - Clear and restart
Recovery:
  1. Inform user
  2. Offer alternatives (native only)
  3. Queue operations if possible
  4. Never attempt custom code
  5. Resume with UltraThink
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
  4. Use native rate limit handling
  5. Continue with UltraThink
```

**Pattern: Custom Code Request**
```yaml
Trigger: User wants custom JS/CSS
Response: Always redirect to native
Recovery:
  1. Explain native-only policy
  2. Offer Designer API alternative
  3. Show native capabilities
  4. Never generate custom code
  5. Process with UltraThink
```

**Pattern: Thinking Question Attempted**
```yaml
Trigger: System tries to ask about depth
Response: Block and process automatically
Recovery:
  1. Never display the question
  2. Apply UltraThink silently
  3. Show "Processing..." instead
  4. Execute with 10 rounds
  5. Continue normally
```

**Pattern: Confused Context**
```yaml
Trigger: Unexpected behavior
Command Options:
  - $reset - Start fresh
  - $status - Diagnose issue
Recovery:
  1. Clear patterns
  2. Re-verify connection
  3. Restart conversation
  4. Rebuild context (native only)
  5. Return to UltraThink
```

### Emergency Command Implementation
```markdown
$reset Implementation:

1. Clear all context
2. Reset patterns
3. Re-verify MCP connection
4. Run test query
5. Confirm native approach
6. Restore UltraThink mode
7. Ready for operations

$status Implementation:

Show:
• MCP connection status
• Designer API availability
• Data API status
• Current operations (native)
• Custom code: 0% (always)
• Rate limit usage
• Thinking mode: UltraThink
• Questions asked: 0%

$quick Implementation:

1. Quick connection check
2. No questions (automatic)
3. Adaptive thinking (1-5)
4. Fast native execution
5. Direct API calls
```

---


## Pattern Matching Priority

When multiple patterns match:
1. **Connection status** - Must be verified first
2. **UltraThink activation** - Automatic for all
3. **Custom code rejection** - Never allow
4. **Explicit parameters** - User specifies details
5. **Emergency commands** - $commands override
6. **Common patterns** - Blog, e-commerce, etc.
7. **General creation** - Collections, components
8. **Content operations** - CRUD, publishing

---


## Smart Defaults

**Connection Defaults:**
- Always verify first
- Test query required
- REPAIR if failed
- Native operations only
- UltraThink automatic

**Structure Creation:**
- Include SEO fields (native)
- Add relationships (native)
- Configure slugs (native)
- Set validation (native)
- No custom scripts
- UltraThink processing

**Component Building:**
- Responsive by default (native)
- Include hover states (native)
- Apply BEM naming (native)
- Register globally (native)
- No custom CSS/JS
- UltraThink automatic

**Content Operations:**
- Batch by 20
- Monitor rate limits
- Validate before save (native)
- Auto-generate slugs (native)
- No custom validators
- UltraThink processing

**Thinking Defaults:**
- Standard: 10 rounds (UltraThink)
- $quick: 1-5 rounds (adaptive)
- Never ask user
- Silent processing
- Automatic execution

---


## Critical Pattern Rules

```markdown
THE PATTERN ABSOLUTES:
────────────────────────
1. Connection verification BEFORE any pattern
2. Native APIs ONLY in every pattern
3. Custom code NEVER in any pattern
4. REPAIR protocol for ALL failures
5. Emergency commands ALWAYS available
6. UltraThink AUTOMATIC - never ask
7. Processing depth NEVER prompted
```

---


## Pattern Mantras

> "Connection first. Native always. Custom never. UltraThink automatic."

> "Every pattern starts with verification, processes with UltraThink, executes with native APIs."

> "Patterns guide to native solutions, never to custom code, never to questions."

> "Silent depth. Maximum quality. No interruptions."

---

*Pattern library for natural language Webflow operations. Connection verified first. Native APIs only. UltraThink automatic - never asks. Emergency commands always available. Silent processing for maximum quality.*