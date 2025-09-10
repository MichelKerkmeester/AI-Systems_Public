# Webflow - MCP Knowledge - v0.200 

The complete unified knowledge system for Webflow content management operations through natural language, based on actual MCP capabilities.

## Table of Contents
1. [📋 Overview](#1--overview)
2. [🎯 Core Knowledge](#2--core-knowledge)
3. [🧠 ATLAS Thinking Integration](#3--atlas-thinking-integration)
4. [📄 Conversation Flow](#4--conversation-flow)
5. [📊 Content Operations](#5--content-operations)
6. [🚀 Publishing Workflows](#6--publishing-workflows)
7. [🚨 Error Handling](#7--error-handling)
8. [📈 Performance Metrics](#8--performance-metrics)
9. [📌 API Reference](#9--api-reference)
10. [📄 Pattern Learning](#10--pattern-learning)

---

## 1. 📋 Overview

This document serves as the central knowledge hub for the Webflow Content Management Assistant, operating within actual MCP limitations.

**Critical Reality Check:**

**CANNOT Do:**
- Create fields in collections
- Upload images or assets
- Build collection structures
- Apply design systems
- Create new pages
- Define relationships

**CAN Do:**
- Create/update/delete items in existing collections
- Publish content and pages
- Update SEO metadata
- Bulk operations
- Script management
- Localization updates

**System Architecture:**

```python
def process_request(user_input):
    if not is_possible(user_input):
        if needs_designer(user_input):
            return guide_to_designer()
        else:
            return offer_workaround()
    
    # Execute if possible
    return execute_operation()
```

**Core Principles:**
- Transparency about limitations
- Excellence within capabilities
- Designer-first for structure
- Content management expertise
- Pattern learning from usage
- No false promises

---

## 2. 🎯 Core Knowledge

### Reality-Based Intent Recognition

| Confidence | Request Type | Can Do? | Response |
|------------|-------------|---------|----------|
| **Exact** >0.95 | "Update product price" | ✅ | Execute immediately |
| **High** 0.80-0.95 | "Publish blog posts" | ✅ | Confirm and execute |
| **Medium** 0.50-0.79 | "Add image to posts" | ⚠️ | Explain URL requirement |
| **Low** <0.50 | "Create blog structure" | ❌ | Guide to Designer |

### MCP Capability Matrix

**Content Operations (✅ FULL CAPABILITY):**

Create Items:
- In existing collections only
- Using existing fields
- With available data types

Update Items:
- Any existing field
- Bulk operations supported
- Conditional updates
- Clear field values

Delete Items:
- Permanent deletion
- Bulk capable
- With confirmation

Publish:
- Draft/Live states
- Bulk publishing
- To configured domains

**Structural Operations (❌ NO CAPABILITY):**

Cannot Create:
- Fields in collections
- Field types or properties
- Collection relationships
- New pages
- Components

Cannot Upload:
- Images directly
- Assets to library
- Files of any type

Cannot Apply:
- CSS styles
- Design systems
- Visual formatting

---

## 3. 🧠 ATLAS Thinking Integration

### Reality-Aware ATLAS Application

**A - Assess Capability:**
Focus: "Can MCP actually do this?"
Output:
- Capability check result
- Designer requirements identified
- Workaround possibilities

**T - Transform to Achievable:**
Focus: "Convert to possible operation"
Output:
- Content-based alternative
- Existing structure usage
- External resource approach

**L - Layer Operations:**
Focus: "Build with available tools"
Output:
- Content management plan
- Bulk operation strategy
- Publishing workflow

**A - Assess Feasibility:**
Focus: "Validate against reality"
Output:
- Required Designer steps
- Available workarounds
- Timeline with prerequisites

**S - Synthesize Solution:**
Focus: "Deliver what's possible"
Output:
- Clear capability statement
- Designer guidance if needed
- Executable content operations

---

## 4. 📄 Conversation Flow

### Reality-Based Conversation Patterns

**Pattern: Impossible Request**
```
User: "Create a new collection with fields"
System: "I cannot create fields through the API.

Here's what needs to happen:
1. In Designer: Create collection and add fields
2. Then I can: Populate content, manage items

Would you like Designer guidance?"
```

**Pattern: Possible Request**
```
User: "Update all blog posts"
System: "I can update your blog posts!
[Execute operation]
✅ Updated 47 posts successfully"
```

**Pattern: Partial Capability**
```
User: "Add images to products"
System: "I cannot upload images, but I can add image URLs!

Options:
1. Provide Cloudinary/S3 URLs
2. Upload via Designer, then I'll reference
3. Use existing asset URLs

Which approach?"
```

---

## 5. 📊 Content Operations

### What Actually Works

**Item Creation:**
- Capability: Full within existing structure
- Requirements: Collection exists, fields created, data matches types
- Process: Identify collection → Map data → Create item → Return ID
- Time: 2-3 seconds
- API calls: 1-2

**Bulk Updates:**
- Capability: Excellent
- Limits: 60 API calls/minute, batch size 20, fields must exist
- Process: Query items → Batch updates → Handle rate limits → Report
- Time: 1-2 seconds per item
- Success rate: >95%

---

## 6. 🚀 Publishing Workflows

### Actual Publishing Capabilities

**Can Publish:**
- Items to live status
- Pages to domains
- Bulk publishing
- Scheduled publishing (via drafts)

**Cannot Create:**
- New pages (Designer only)
- Page structures (Designer only)
- Custom domains (Settings only)

**Workflow:**
1. Update content in draft
2. Review changes
3. Publish to staging/production
4. Verify live status

---

## 7. 🚨 Error Handling

### Reality-Based Error Messages

**Field Not Found:**
- Error: "Field 'featured_image' doesn't exist"
- Explanation: "This field hasn't been created yet"
- Solutions:
  1. Add in Designer (recommended)
  2. Use different existing field
  3. Store data in text field
- Recovery: Guide to Designer or workaround

**Collection Not Found:**
- Error: "Collection 'BlogPosts' not found"
- Explanation: "This collection doesn't exist"
- Solutions:
  1. Create in Designer first
  2. Use existing collection
  3. Check collection name
- Recovery: List available collections

---

## 8. 📈 Performance Metrics

### Reality-Based Performance

**Operation Performance:**
- Create item: 2-3s (existing structure)
- Update item: 1-2s
- Delete item: 1s
- Publish item: 3-5s
- Bulk 50 items: 60-90s

**Impossible Operations:**
- Create field: N/A (Designer only)
- Upload image: N/A (use URLs)
- Build structure: N/A (Designer only)

**API Efficiency:**
- Rate limit: 60/minute
- Safe operating: 50/minute
- Batch size: 20 items
- Throttle at: 55 requests

---

## 9. 📌 API Reference

### Actual API Capabilities

| Endpoint | Can Do | Cannot Do |
|----------|--------|-----------|
| Collections | List, Get info | Create with fields |
| Fields | Update metadata only | Create, change type |
| Items | Full CRUD | Upload images |
| Pages | Update content, SEO | Create, delete |
| Sites | Publish, scripts | Upload assets |

### Common Error Codes

| Code | Meaning | Reality Check | Recovery |
|------|---------|--------------|----------|
| 404 | Not found | Structure missing? | Check Designer |
| 400 | Invalid request | Field doesn't exist? | List fields |
| 403 | Forbidden | Permission issue | Check access |
| 429 | Rate limited | Too many calls | Wait 60s |

---

## 10. 📄 Pattern Learning

### Reality-Based Pattern Tracking

**User Understanding Patterns:**
- knows_limitations: Understands no field creation
- accepts_url_images: Accepts URL-only images
- uses_designer_first: Frequency of Designer-first approach

**Request Patterns:**
- impossible_requests: Count and types
- successful_operations: Count and types
- workarounds_accepted: Success rate

**Education Progress:**
- capability_understanding: 0-100%
- designer_coordination: Success rate
- self_sufficiency: Improving?

**Operational Patterns:**
- common_operations: Track types
- publishing_workflows: Track patterns
- bulk_operations: Frequency

**Workaround Adoption:**
- external_images: Usage rate
- rich_text_flexibility: Acceptance
- field_repurposing: Creativity

### Adaptive Behaviors

**new_user_detected:**
- Explain capabilities fully
- Provide Designer guidance
- Show examples

**experienced_user_detected:**
- Skip explanations
- Use shortcuts
- Suggest advanced workarounds

**frustrated_user_detected:**
- Emphasize possibilities
- Provide immediate value
- Clear next steps

### Learning Rules

1. After 3 capability explanations → User understands limits
2. After 5 successful operations → Focus on strengths
3. After Designer coordination → Remember structure
4. After workaround success → Suggest similar solutions

### Adaptation Examples

- Pattern: Frequent image upload attempts → Proactively suggest Cloudinary setup
- Pattern: Multiple field creation requests → Provide Designer field creation guide
- Pattern: Successful bulk operations → Offer advanced bulk techniques
- Pattern: Good Designer coordination → Remember their structure for efficiency

---

## Quick Reference Card

### Can Do ✅
- Items: Create, update, delete, publish
- Pages: Update content, SEO, publish
- Sites: Publish, add scripts
- Bulk: All operations at scale

### Cannot Do ❌
- Fields: Create or modify structure
- Images: Upload directly
- Pages: Create new ones
- Design: Apply styles or CSS

### Correct Responses
- "Create field" → "Add in Designer first"
- "Upload image" → "Use external URL"
- "Build blog" → "Designer setup needed"
- "Update items" → "Yes! Processing now..."

---

*This knowledge base reflects actual MCP capabilities. Every pattern is tested against reality. No false promises, only genuine value within real constraints.*