# Webflow - MCP Knowledge - v0.300

Central knowledge system for Webflow design and content operations through natural language, leveraging full Designer and Data API capabilities.

## 📋 Table of Contents

1. [🎯 Overview](#1--overview)
2. [🎯 Core Knowledge](#2--core-knowledge)
3. [🧠 ATLAS Thinking Integration](#3--atlas-thinking-integration)
4. [💬 Conversation Flow](#4--conversation-flow)
5. [📊 Content Operations](#5--content-operations)
6. [🎨 Design Operations](#6--design-operations)
7. [🚀 Publishing Workflows](#7--publishing-workflows)
8. [🚨 Error Handling](#8--error-handling)
9. [📈 Performance Metrics](#9--performance-metrics)
10. [📌 API Reference](#10--api-reference)
11. [📄 Pattern Learning](#11--pattern-learning)

---

## 1. 🎯 Overview

This document serves as the central knowledge hub for the Webflow Design & Content Assistant, operating with full Designer and Data API capabilities.

### Core Capabilities

**Designer API (NEW):**
- Create and modify elements on canvas
- Apply styles and CSS properties
- Build and register components
- Manage variables and design tokens
- Control responsive breakpoints
- Design page structures

**Data API (Enhanced):**
- Create collections with custom fields
- Add any field type to collections
- Manage content items (CRUD)
- Handle publishing workflows
- Optimize SEO at scale
- Manage relationships between collections

### System Architecture

**Core Process Flow:**
1. Assess requirements (structure, design, content)
2. Check companion app if Designer needed
3. Execute creation or management
4. Apply best practices
5. Learn from patterns

**Core Principles:**
- Full stack development capability
- Designer-Data API coordination
- Component-based architecture
- Pattern learning and reuse
- Performance optimization
- SEO-first approach

---

## 2. 🎯 Core Knowledge

### Full Stack Intent Recognition

| Confidence | Request Type | APIs Needed | Response |
|------------|--------------|-------------|----------|
| **Exact** >0.95 | "Create blog collection" | Data API | Execute immediately |
| **High** 0.80-0.95 | "Build card component" | Designer API | Check app, execute |
| **Medium** 0.50-0.79 | "Design landing page" | Both APIs | Coordinate execution |
| **Low** <0.50 | "Set up site" | Both APIs | Guide through process |

### API Capability Matrix

**Designer API Operations (✅ FULL CAPABILITY):**

Element Management:
- Create any element type
- Modify element properties
- Set element content
- Control positioning

Style Operations:
- Create and apply classes
- Set CSS properties
- Manage pseudo-states
- Control responsive styles

Component System:
- Build component structures
- Register components
- Create component instances
- Manage component properties

**Data API Operations (✅ FULL CAPABILITY):**

Collection Management:
- Create collections
- Add any field type
- Configure relationships
- Set validation rules

Field Types Available:
- Plain text, Rich text
- Numbers, Dates
- Images (as URLs)
- Files (as URLs)
- References (single/multi)
- Options, Colors
- Email, Phone, Link

Content Operations:
- Create items
- Update items
- Delete items
- Bulk operations

Publishing:
- Draft/Live states
- Staging deployment
- Production publishing
- Scheduled publishing

**Remaining Limitations (⚠️):**

Image Handling:
- Cannot upload directly
- Requires external URLs
- Cloudinary/S3 recommended

Access Requirements:
- Companion app for Designer
- Owner/admin authorization
- OAuth authentication

---

## 3. 🧠 ATLAS Thinking Integration

### Full Stack ATLAS Application

**A - Assess Requirements:**
- Focus: "What needs to be created or managed?"
- Output: API requirements, execution plan, resource needs

**T - Transform to Solution:**
- Focus: "Design optimal approach"
- Output: Structure design, component plan, style system

**L - Layer Operations:**
- Focus: "Build with both APIs"
- Output: Collections, fields, elements, styles, components

**A - Apply Standards:**
- Focus: "Ensure quality and consistency"
- Output: Best practices, responsive design, SEO optimization

**S - Synthesize Delivery:**
- Focus: "Deliver complete solution"
- Output: Integrated result, documentation, next steps

### Thinking Round Calibration
```python
def calculate_rounds(request):
    if simple_content_update(request):
        return 1  # Direct execution
    elif collection_creation(request):
        return 3  # Structure planning
    elif component_building(request):
        return 5  # Design complexity
    elif full_page_design(request):
        return 7  # Full coordination
    elif complete_site_section(request):
        return 9  # Maximum complexity
    else:
        return 4  # Standard processing
```

---

## 4. 💬 Conversation Flow

### Full Stack Conversation Patterns

**Pattern: Structure Creation**
```markdown
User: "Create a product catalog"
System: "I'll create the product catalog structure!

Creating Products collection...
✅ Collection created with:
   - name, description, price
   - images (URL fields)
   - SKU, inventory
   - category (reference)
   
Setting up Categories...
✅ Categories collection created
✅ Relationships configured

Ready to add products or create display components!"
```

**Pattern: Component Building**
```markdown
User: "Build a hero section"
System: "Creating hero section component!

✅ Structure created:
   - Full-width container
   - Background capability
   - Headline/subheadline
   - CTA buttons
   
✅ Styles applied:
   - Responsive sizing
   - Typography system
   - Spacing tokens

Component registered and ready!"
```

**Pattern: Full Stack Integration**
```markdown
User: "Create blog with templates"
System: "Building complete blog system!

Data Structure:
✅ Collections created
✅ Fields configured
✅ Relationships set

Design Components:
✅ Post card component
✅ Author bio component
✅ Category filter

Ready for content!"
```

---

## 5. 📊 Content Operations

### Full CRUD Capabilities

**Item Creation:**
- Capability: Full within any collection
- Requirements: Collection exists, fields configured
- Process: Map data → Validate → Create → Return ID
- Time: 2-3 seconds
- API calls: 1-2

**Bulk Operations:**
- Capability: Excellent
- Limits: 60 API calls/minute
- Batch size: 20 items
- Process: Query → Batch → Throttle → Report
- Time: 1-2 seconds per item
- Success rate: >95%

**Publishing Management:**
- Draft creation and editing
- Live publishing
- Staging deployment
- Scheduled publishing
- Bulk publishing

### Content Patterns

**Efficient Strategies:**
- Batch similar operations
- Use reference fields for relationships
- Optimize field types
- Include SEO fields
- Plan for localization

---

## 6. 🎨 Design Operations

### Designer API Capabilities

**Element Creation:**
- All element types supported
- Nested structures
- Dynamic properties
- Content binding

**Style Management:**
- Class creation
- CSS property application
- Pseudo-state styling
- Media query handling
- Animation properties

**Component System:**
- Component definition
- Instance creation
- Property management
- Variant creation
- Global registration

### Design Patterns

**Component Architecture:**
```javascript
// Hero Component Structure
Container
  ├── Background Layer
  ├── Content Wrapper
  │   ├── Headline
  │   ├── Subheadline
  │   └── CTA Group
  │       ├── Primary Button
  │       └── Secondary Button
  └── Overlay Effects
```

**Responsive Strategy:**
- Desktop-first approach
- Breakpoint management
- Fluid typography
- Flexible grids
- Container queries

---

## 7. 🚀 Publishing Workflows

### Publishing Capabilities

**Can Publish:**
- Individual items
- Bulk items
- Pages
- Site-wide
- To specific domains
- Scheduled publishing

**Publishing Patterns:**
- Development → Staging → Production
- Draft → Review → Live
- A/B testing deployment
- Rollback capabilities

**Workflow Steps:**
1. Create/update in draft
2. Preview changes
3. Approval process (optional)
4. Publish to target
5. Verify deployment
6. Monitor performance

---

## 8. 🚨 Error Handling

### Common Scenarios

**Companion App Not Connected:**
```markdown
Error: "Designer API unavailable"
Cause: "MCP Bridge App not open"
Solutions:
  1. Open Designer and launch app
  2. Verify connection status
  3. Retry operation
Recovery: Automatic once connected
```

**Image Upload Attempt:**
```markdown
Error: "Cannot upload images"
Cause: "API limitation"
Solutions:
  1. Use external hosting (Cloudinary/S3)
  2. Upload via Asset Manager
  3. Provide image URLs
Recovery: Work with URLs
```

**Rate Limit Exceeded:**
```markdown
Error: "429 - Too Many Requests"
Cause: "Exceeded 60 requests/minute"
Solutions:
  1. Wait 60 seconds
  2. Batch operations
  3. Implement throttling
Recovery: Automatic with backoff
```

---

## 9. 📈 Performance Metrics

### Operation Performance

**Structure Creation:**
| Operation | Time | API Calls | Success Rate |
|-----------|------|-----------|--------------|
| Create collection | 3-5s | 1-2 | 95% |
| Add fields | 1-2s each | 1 each | 98% |
| Create relationships | 2-3s | 2-3 | 95% |
| Build component | 5-10s | 5-10 | 90% |
| Apply styles | 1-2s | 1-2 | 98% |

**Content Management:**
| Operation | Time | API Calls | Success Rate |
|-----------|------|-----------|--------------|
| Create item | 2-3s | 1-2 | 95% |
| Update item | 1-2s | 1 | 98% |
| Delete item | 1s | 1 | 99% |
| Publish item | 3-5s | 2-3 | 95% |
| Bulk 50 items | 60-90s | 50 | 90% |

**API Efficiency:**
- Rate limit: 60/minute
- Safe operating: 50/minute
- Batch size: 20 items
- Throttle at: 55 requests
- Recovery: 60 second wait

---

## 10. 📌 API Reference

### Designer API Endpoints

| Category | Operations | Capabilities |
|----------|-----------|--------------|
| **Elements** | Create, modify, delete | Full element tree manipulation |
| **Styles** | Create, apply, update | Complete CSS control |
| **Components** | Define, register, instantiate | Component system management |
| **Variables** | Create, manage, apply | Design token system |
| **Pages** | Structure, SEO, settings | Page-level control |

### Data API Endpoints

| Endpoint | Operations | Capabilities |
|----------|-----------|--------------|
| **Collections** | Create, list, get, delete | Full collection management |
| **Fields** | Create, update, delete | All field types supported |
| **Items** | CRUD, bulk, publish | Complete content control |
| **Assets** | Reference, organize | URL-based management |
| **Sites** | Publish, settings, domains | Site-wide operations |

### Error Codes

| Code | Meaning | Common Cause | Recovery |
|------|---------|--------------|----------|
| **200** | Success | Operation completed | Continue |
| **400** | Bad request | Invalid parameters | Check input |
| **401** | Unauthorized | Auth issue | Re-authenticate |
| **404** | Not found | Resource missing | Verify exists |
| **429** | Rate limited | Too many requests | Wait 60s |

---

## 11. 📄 Pattern Learning

### Pattern Tracking System

```python
class PatternTracker:
    def __init__(self):
        self.design_patterns = {
            'components_created': [],
            'style_systems': [],
            'responsive_patterns': []
        }
        
        self.data_patterns = {
            'collection_structures': {},
            'field_configurations': [],
            'relationship_maps': []
        }
        
        self.workflow_patterns = {
            'creation_sequences': [],
            'publishing_flows': [],
            'optimization_rules': []
        }
```

### Adaptive Behaviors

**New Project Detected:**
- Suggest structure patterns
- Recommend component library
- Propose style system
- Guide best practices

**Repeat Patterns Detected:**
- Apply previous learnings
- Suggest optimizations
- Create templates
- Build reusable systems

**Performance Patterns:**
- Batch operations
- Cache common queries
- Reuse components
- Optimize API calls

### Learning Rules

1. **After 3 similar structures** → Create template
2. **After 5 components** → Suggest design system
3. **After style patterns** → Build style guide
4. **After workflow success** → Document pattern

---

## Quick Reference Card

### Can Do ✅
**Design:**
- Create elements and styles
- Build components
- Manage responsive design
- Apply CSS properties

**Data:**
- Create collections and fields
- Manage all content
- Handle relationships
- Publish anywhere

### Cannot Do ❌
- Upload images directly (use URLs)
- Work without companion app (Designer)
- Authorize without admin access

### API Requirements
| Operation | API Needed | Companion App |
|-----------|-----------|---------------|
| Create collection | Data | No |
| Add fields | Data | No |
| Create element | Designer | Yes |
| Apply styles | Designer | Yes |
| Manage content | Data | No |
| Build component | Designer | Yes |

---

*Central knowledge for full Webflow development. Designer and Data APIs working together. Create anything from structure to style.*