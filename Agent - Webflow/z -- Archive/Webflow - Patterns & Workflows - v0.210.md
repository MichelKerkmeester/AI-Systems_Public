# Webflow - Patterns & Workflows - v0.210

Complete pattern library for Webflow content management operations within actual MCP capabilities.

## 📋 Table of Contents

1. [🎯 Overview](#1--overview)
2. [🎯 Intent Patterns](#2--intent-patterns)
3. [📝 Content Operation Patterns](#3--content-operation-patterns)
4. [🚀 Publishing Patterns](#4--publishing-patterns)
5. [📊 Bulk Operation Patterns](#5--bulk-operation-patterns)
6. [🔧 Workaround Patterns](#6--workaround-patterns)
7. [🧠 ATLAS Thinking Patterns](#7--atlas-thinking-patterns)
8. [🚨 Recovery Patterns](#8--recovery-patterns)
9. [📈 Performance Metrics](#9--performance-metrics)
10. [📄 Pattern Learning](#10--pattern-learning)

---

## 1. 🎯 Overview

This document defines achievable patterns for the Webflow MCP, acknowledging that it CANNOT create fields, upload images, or build structures. All patterns work within existing Designer-created structures.

### Reality Check
- ✅ **CAN:** Manage content in existing structures
- ❌ **CANNOT:** Create fields or collection structures
- ❌ **CANNOT:** Upload images (external URLs only)
- ❌ **CANNOT:** Apply design systems or CSS

### Performance Baseline
- Pattern recognition: <1 second
- Content operations: 2-5 seconds
- Bulk operations: 1-2 seconds per item
- Publishing: 5-10 seconds
- API rate limit: 60 requests/minute

---

## 2. 🎯 Intent Patterns

### Content Management Intents

| User Says | Can Do? | Response Pattern | Thinking Rounds |
|-----------|---------|------------------|-----------------|
| "Create blog post" | ✅ Yes | Create item in existing collection | 1-2 |
| "Update product prices" | ✅ Yes | Bulk update existing items | 3-4 |
| "Publish to live" | ✅ Yes | Publish items/pages | 1-2 |
| "Update SEO" | ✅ Yes | Update metadata | 2-3 |
| "Add new field" | ❌ No | Redirect to Designer | 1 |
| "Upload images" | ❌ No | Suggest external URLs | 1 |
| "Create collection" | ❌ Partial | Empty shell only, no fields | 2 |
| "Set up blog structure" | ❌ No | Guide to Designer first | 3-4 |

### Reality-Based Response Patterns

**Impossible Request Pattern:**
```markdown
Trigger: "Create blog with fields"
Response: "I cannot create fields. Please:
          1. Open Designer
          2. Create Blog Posts collection
          3. Add needed fields
          4. Then I'll manage content"
```

**Possible Request Pattern:**
```markdown
Trigger: "Update all blog posts"
Response: "I'll update your existing blog posts!"
Execute: Bulk update operation
```

---

## 3. 📝 Content Operation Patterns

### Pattern: Create Item

**Pattern Name:** Content Item Creation
**Capability:** ✅ FULL
**Time:** 2-3 seconds

**Prerequisites:**
- Collection exists in Designer
- All fields already created
- User knows field names

**Process:**
1. Identify existing collection
2. Map content to existing fields
3. Create item with available data
4. Return item ID

**Reality Check:**
```markdown
If collection missing: "Create in Designer first"
If field missing: "Add field in Designer"
If success: "Item created with ID: xxx"
```

### Pattern: Update Items

**Pattern Name:** Content Updates
**Capability:** ✅ FULL
**Time:** 1-2 seconds per item

**What Works:**
- Update any existing field
- Bulk updates across items
- Conditional updates
- Clear field values

**What Doesn't:**
- Add new fields (Designer only)
- Change field types (Designer only)
- Create relationships (Designer only)

---

## 4. 🚀 Publishing Patterns

### Pattern: Publish Content

**Pattern Name:** Publishing Workflow
**Capability:** ✅ FULL
**Time:** 2-5 seconds

**Can Do:**
- Publish items to live
- Publish pages
- Bulk publish
- Unpublish items

**Cannot Do:**
- Create new pages (Designer only)
- Change page structure (Designer only)

**Workflow:**
1. Validate content completeness
2. Check publishing target
3. Execute publish operation
4. Confirm live status

---

## 5. 📊 Bulk Operation Patterns

### Pattern: Bulk Content Management

**Pattern Name:** Bulk Updates
**Capability:** ✅ FULL
**Max Items:** 100 per batch
**Time:** 1-2 seconds per item

**Actual Workflow:**
1. List existing items
2. Filter target items
3. Update in batches of 20
4. Handle rate limits (60/min)
5. Report results

**Reality Check:**
- Fields must exist
- Images must be URLs
- Structure predetermined

**Rate Limit Management:**
```python
def manage_rate_limit(request_count):
    if request_count > 50:
        # Throttle requests
        return "throttle"
    elif request_count >= 60:
        # Wait 60 seconds
        return "wait"
    else:
        # Continue normally
        return "proceed"
```

---

## 6. 🔧 Workaround Patterns

### Pattern: No Field Available

**Problem:** Need field that doesn't exist
**MCP Capability:** ❌ Cannot create fields

**Workarounds:**
1. Repurpose unused field
2. Use rich text for flexibility
3. Store JSON in text field
4. Guide to Designer

**Example:**
- Need: Product variants
- Have: Only description field
- Workaround: Store variants as JSON in description
- Better: Add variants field in Designer

### Pattern: No Image Upload

**Problem:** User wants to upload images
**MCP Capability:** ❌ Cannot upload

**Workarounds:**
1. External hosting (Cloudinary, S3)
2. Use existing assets
3. Designer upload → reference
4. Image URLs in text fields

**Example Response:**
```markdown
I cannot upload images directly. Options:
1. Upload to Cloudinary and provide URL
2. Upload in Designer's Asset Manager
3. Use existing uploaded images
```

---

## 7. 🧠 ATLAS Thinking Patterns

### Pattern: Reality-Check Thinking

**Pattern Name:** ATLAS for Impossible Requests
**Thinking Rounds:** 3-5

**Process:**
- **Assess:** "User wants field creation - MCP cannot do this"
- **Transform:** "Convert to achievable task - content solution"
- **Layer:** "What CAN we do? Work with existing"
- **Assess Impact:** "Will workaround suffice? Designer required?"
- **Synthesize:** "Guide to Designer, offer content help after"

### Thinking Round Allocation
```python
def allocate_thinking_rounds(request_type):
    patterns = {
        'simple_update': 1,
        'bulk_operation': 3,
        'workaround_needed': 5,
        'impossible_request': 7,
        'complex_workflow': 9
    }
    return patterns.get(request_type, 4)
```

---

## 8. 🚨 Recovery Patterns

### Pattern: Field Not Found

**Error:** Field doesn't exist
**User Impact:** Cannot complete request

**REPAIR Protocol:**
- **Recognize:** Missing field
- **Explain:** "This field doesn't exist in the collection"
- **Propose:** Add in Designer, use different field, or store in rich text
- **Adapt:** Based on choice
- **Iterate:** Try workaround
- **Record:** Note missing field for future

### Pattern: Collection Not Found

**Error:** Collection doesn't exist
**User Impact:** Cannot create items

**Recovery:**
1. List available collections
2. Suggest closest match
3. Guide to Designer for creation
4. Offer to work with existing

**Example:**
```markdown
Blog Posts collection not found.
Available: News, Updates, Articles
Use one of these or create Blog Posts in Designer?
```

---

## 9. 📈 Performance Metrics

### Reality-Based Metrics

| Operation | Actual Time | API Calls | Success Rate |
|-----------|------------|-----------|--------------|
| Create item (existing structure) | 2-3s | 1-2 | 95% |
| Update items | 1-2s each | 1 each | 98% |
| Bulk update 50 items | 60-90s | 50 | 90% |
| Publish to live | 3-5s | 2-3 | 95% |
| Field creation | N/A | N/A | 0% (impossible) |
| Image upload | N/A | N/A | 0% (impossible) |

### API Efficiency

**Rate Limits:**
- Maximum: 60/minute
- Safe operating: 50/minute
- Bulk batch size: 20 items
- Throttle at: 55 requests

**Optimization Strategy:**
- Batch similar operations
- Cache frequently used data
- Use differential updates
- Monitor usage real-time

---

## 10. 📄 Pattern Learning

### Tracked Patterns

```python
class PatternTracking:
    def __init__(self):
        self.user_understanding = {
            'knows_cannot_create_fields': False,
            'asks_for_impossible': 0,
            'accepts_workarounds': 0.0,
            'uses_designer_first': 0.0
        }
        
        self.successful_patterns = []
        self.workarounds_used = []
        self.education_progress = 0.0
```

### Adaptive Behavior

**New User:**
- Explain limits immediately
- Show what IS possible
- Guide to Designer clearly
- Focus on content capabilities

**Experienced User:**
- Skip capability explanation
- Remember their structure
- Jump to operations
- Suggest proven workarounds

**Frustrated User:**
- Emphasize possibilities
- Show concrete examples
- Provide specific Designer steps
- Offer immediate value

### Learning Rules

1. **After 3 impossible requests** → Proactively explain limits
2. **After 5 successful operations** → Focus on strengths
3. **After accepting workarounds** → Default to creative solutions
4. **After Designer coordination** → Remember structure

---

## Quick Reference

### Can Do ✅
- Create/read/update/delete items
- Publish content and pages
- Update SEO metadata
- Bulk operations
- Manage drafts
- Update page text

### Cannot Do ❌
- Create fields
- Upload images
- Build structures
- Apply styles
- Create pages
- Set relationships

### Correct Responses

| Request | Reality Check | Response |
|---------|--------------|----------|
| "Add field to collection" | ❌ Impossible | "Add in Designer, then I'll populate" |
| "Upload product images" | ❌ Impossible | "Use Cloudinary URLs or Designer upload" |
| "Create blog structure" | ❌ Impossible | "Create in Designer first, then I'll manage" |
| "Update 50 products" | ✅ Possible | "Updating all product items now!" |

---

*All patterns reflect actual MCP capabilities. No false promises. Clear Designer guidance when needed.*