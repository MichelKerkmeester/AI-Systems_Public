# Webflow Platform Constraints - Limits & Configuration

Understand the hard limits and production settings that impact every Webflow project. These constraints define what's possible and guide architectural decisions.

> **📢 Next-Gen CMS Update (2025)**: Webflow is rolling out significant CMS improvements with dramatically increased limits. See section 3.1 for details.

.

## 1. 🎯 Objective

Document Webflow's non-negotiable platform constraints and production settings that every developer must respect. These limits are enforced by the platform and cannot be overridden.

**Category**: critical
**Tags**: webflow, constraints, limits, production, configuration
**Priority**: critical

.

## 2. ⚙️ Production Settings

### 2.1 Performance Configuration
```javascript
// Default Webflow production settings
{
  javascript: 'async',          // Scripts load asynchronously
  css: 'per_page',             // CSS isolated per page
  minification: true,          // HTML/CSS/JS minified
  gzip: true,                  // Content compressed
  cdn: true                    // Assets served via CDN
}
```

### 2.2 Security Settings
```javascript
{
  ssl: 'enforced',             // HTTPS required
  hsts: true,                  // Strict Transport Security
  frame_options: 'SAMEORIGIN', // Clickjacking protection
  mixed_content: 'blocked'     // HTTP resources blocked on HTTPS
}
```

### 2.3 Impact on Development
- **Script order not guaranteed** - Use initialization patterns
- **No global CSS cascade** - Style each page independently
- **Function names minified** - Never rely on `function.name`
- **Inline handlers removed** - Use addEventListener only

.

## 3. 🔒 Platform Limits

### 3.1 Hard Limits Table

#### Current Limits (Legacy CMS)
```javascript
const WEBFLOW_LIMITS_LEGACY = {
  // Collection Limits
  collections_per_site: 40,
  items_per_collection: 10000,
  collection_lists_per_page: 20,
  items_per_list: 100,
  nested_lists_per_page: 1,
  items_in_nested_list: 5,

  // Field Limits
  reference_fields: 5,
  multi_reference_fields: 5,
  rich_text_length: 10000,
  plain_text_length: 2000,

  // API Limits
  api_calls_per_minute: 60,
  api_payload_size: '4MB',

  // Page Limits
  pages_per_site: 100,        // Static pages
  page_size: '10MB',           // HTML size
  custom_code: '10000 chars'   // Per page/site
};
```

#### Next-Gen CMS Limits (2025+)
```javascript
const WEBFLOW_LIMITS_NEXTGEN = {
  // Collection Limits - Dramatically Increased
  collections_per_site: 40,              // Unchanged
  total_items_all_collections: 1000000,  // NEW: 1M+ total items
  items_per_collection: 1000000,         // 100X increase (was 10,000)
  collection_lists_per_page: 40,         // 2X increase (was 20)
  items_per_list: 100,                   // Unchanged
  nested_lists_per_page: 10,             // 10X increase (was 1)
  items_in_nested_list: 100,             // 20X increase (was 5)
  nesting_depth: 3,                      // NEW: Multi-level nesting

  // Field Limits - Doubled
  fields_per_collection: 'doubled',      // 2X increase (exact number TBD)
  reference_fields: 10,                  // 2X increase (was 5)
  multi_reference_fields: 10,            // 2X increase (was 5)
  rich_text_length: 10000,               // TBD if changed
  plain_text_length: 2000,               // TBD if changed

  // API Limits - Enhanced
  content_delivery_api: true,            // NEW: Available to all customers
  api_cdn_delivery: true,                // NEW: CDN-served, cached
  api_calls_per_minute: 60,              // TBD if changed
  api_payload_size: '4MB',               // TBD if changed

  // Page Limits
  pages_per_site: 100,                   // TBD if changed
  page_size: '10MB',                     // TBD if changed
  custom_code: '10000 chars'             // TBD if changed
};
```

**Migration Timeline**: Next-Gen CMS rollout planned for later in 2025. Check your site settings to see which version you're using.

### 3.2 Common Constraint Violations

```javascript
// ❌ WRONG - Assumes legacy limits
const lists = document.querySelectorAll('.w-dyn-list');
// Fails if > 20 lists on legacy CMS or > 40 on next-gen

// ✅ CORRECT - Version-aware limit checking
function validate_collection_limits() {
  const lists = document.querySelectorAll('.w-dyn-list');

  // Next-gen CMS detection (adjust based on actual detection method)
  const isNextGen = document.querySelector('[data-wf-version="next-gen"]') !== null;
  const maxLists = isNextGen ? 40 : 20;
  const maxNestedLists = isNextGen ? 10 : 1;
  const maxItemsInNested = isNextGen ? 100 : 5;

  console.assert(lists.length <= maxLists,
    `Collection list limit exceeded: ${lists.length}/${maxLists}`);

  lists.forEach((list) => {
    const items = list.querySelectorAll('.w-dyn-item');
    console.assert(items.length <= 100,
      `Items per list limit exceeded: ${items.length}/100`);

    // Check nested lists
    if (isNextGen) {
      const nestedLists = list.querySelectorAll('.w-dyn-list');
      console.assert(nestedLists.length <= maxNestedLists,
        `Nested list limit exceeded: ${nestedLists.length}/${maxNestedLists}`);
    }
  });
}
```

### 3.3 Publishing Constraints

#### Legacy CMS
| Action | Limit | Consequence if Exceeded |
|--------|-------|-------------------------|
| Publish | 100 pages | Publishing fails |
| API Update | 60/min | Rate limited (429 error) |
| Collection Items | 10,000 per collection | Cannot add more items |
| Collection Lists | 20 per page | Designer prevents adding |
| Nested Lists | 1 per page | Designer prevents adding |
| Items in Nested | 5 | Display truncated |
| Reference Fields | 5 per collection | Cannot add more |

#### Next-Gen CMS (2025+)
| Action | Limit | Consequence if Exceeded |
|--------|-------|-------------------------|
| Publish | 100 pages | Publishing fails (TBD if changed) |
| API Update | 60/min | Rate limited (429 error, TBD if changed) |
| Collection Items | 1M per collection | Cannot add more items |
| Total CMS Items | 1M+ across all collections | System-wide limit |
| Collection Lists | 40 per page | Designer prevents adding |
| Nested Lists | 10 per page | Designer prevents adding |
| Items in Nested | 100 | Display truncated |
| Nesting Depth | 3 levels | Deeper nesting not supported |
| Reference Fields | 10 per collection | Cannot add more |

.

## 4. 🧩 Development Implications

### 4.1 Architecture Decisions

```javascript
// Design around constraints
if (total_items > 100) {
  // ✅ Implement pagination or filtering
  use_pagination();
} else {
  // ✅ Safe to display all items
  display_all();
}
```

### 4.2 Performance Boundaries
```javascript
// Monitor constraint usage
function check_resource_usage() {
  return {
    collections: document.querySelectorAll('.w-dyn-list').length,
    total_items: document.querySelectorAll('.w-dyn-item').length,
    page_size: document.documentElement.outerHTML.length,
    custom_code: document.querySelectorAll('script').length
  };
}
```

### 4.3 Workaround Strategies

#### Legacy CMS
| Constraint | Workaround Strategy |
|------------|-------------------|
| 100 items per list | Implement pagination or load more |
| 20 collection lists | Combine lists or use tabs |
| 1 nested list | Use alternative UI patterns |
| 5 items in nested | Implement "view more" functionality |
| 5 reference fields | Denormalize data structure |
| 10,000 items per collection | Split into multiple collections |
| 10,000 char custom code | External script files |

#### Next-Gen CMS (2025+)
| Constraint | Workaround Strategy |
|------------|-------------------|
| 100 items per list | Still implement pagination for UX |
| 40 collection lists | Rarely reached; consider performance |
| 10 nested lists | Multi-level nesting now supported |
| 100 items in nested | Pagination still recommended for UX |
| 10 reference fields | Doubled capacity reduces need for workarounds |
| 1M items per collection | Consider API-driven delivery for scale |
| Content Delivery API | Leverage for multi-channel publishing |

.

## 5. ✅ Configuration Checklist

### 5.1 Pre-Development
- [ ] Review collection structure against limits
- [ ] Plan for pagination if > 100 items
- [ ] Verify nested list requirements (max 1)
- [ ] Check total collections needed (max 40)

### 5.2 During Development
- [ ] Monitor collection list count per page
- [ ] Test with maximum expected items
- [ ] Validate API call frequency
- [ ] Check custom code character count

### 5.3 Before Publishing
- [ ] Run constraint validation
- [ ] Test in all breakpoints
- [ ] Verify HTTPS compatibility
- [ ] Check total page count

### 5.4 Quick Validation Script
```javascript
// Add to console for quick constraint check
(() => {
  // Detect CMS version (adjust detection method as needed)
  const isNextGen = document.querySelector('[data-wf-version="next-gen"]') !== null;

  const limits = {
    lists: document.querySelectorAll('.w-dyn-list').length,
    max_items: Math.max(...Array.from(
      document.querySelectorAll('.w-dyn-list')
    ).map(l => l.querySelectorAll('.w-dyn-item').length)),
    nested: document.querySelectorAll('.w-dyn-list .w-dyn-list').length
  };

  const maxLists = isNextGen ? 40 : 20;
  const maxNested = isNextGen ? 10 : 1;
  const version = isNextGen ? 'Next-Gen CMS' : 'Legacy CMS';

  console.table({
    'CMS Version': version,
    'Collection Lists': `${limits.lists}/${maxLists}`,
    'Max Items in List': `${limits.max_items}/100`,
    'Nested Lists': `${limits.nested}/${maxNested}`,
    'Status': limits.lists <= maxLists && limits.max_items <= 100 && limits.nested <= maxNested ? '✅' : '❌'
  });

  if (isNextGen) {
    console.log('ℹ️ Next-Gen CMS features:', {
      'Max items per collection': '1M',
      'Total CMS items': '1M+',
      'Reference fields': 10,
      'Nesting depth': 3,
      'Content Delivery API': 'Available'
    });
  }
})();
```

## 📚 Related Documentation

- [initialization_pattern.md](./initialization_pattern.md) - Handle async script loading
- [webflow_collection_lists.md](./webflow_collection_lists.md) - Collection-specific patterns
- [webflow_performance.md](./webflow_performance.md) - Work within constraints

---

**Remember**: These limits are enforced by Webflow and cannot be overridden. Design your architecture to work within them from the start.