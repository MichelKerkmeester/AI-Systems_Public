# Webflow Platform Constraints

Webflow's non-negotiable platform constraints and production settings that every developer must respect. These limits are enforced by the platform and cannot be overridden.

.

## 1. ⚙️ Production Settings

### 1.1 Performance Configuration
```javascript
// Default Webflow production settings
{
  javascript: 'sync',          // Scripts load synchronously
  css: 'per_page',             // CSS isolated per page
  minification: true,          // HTML/CSS/JS minified
  gzip: true,                  // Content compressed
  cdn: true                    // Assets served via CDN
}
```

### 1.2 Security Settings
```javascript
{
  ssl: 'enforced',             // HTTPS required
  hsts: true,                  // Strict Transport Security
  frame_options: 'SAMEORIGIN', // Clickjacking protection
  mixed_content: 'blocked'     // HTTP resources blocked on HTTPS
}
```

### 1.3 Impact on Development
- **No global CSS cascade** - Style each page independently
- **Function names minified** - Never rely on `function.name`
- **Inline handlers removed** - Use addEventListener only

.

## 2. 🔒 Platform Limits

### 2.1 Hard Limits Table

#### CMS Limits
```javascript
const WEBFLOW_LIMITS_NEXTGEN = {
  // Collection Limits - Dramatically Increased
  collections_per_site: 40,              
  total_items_all_collections: 1000000,  
  items_per_collection: 1000000,         
  collection_lists_per_page: 40,        
  items_per_list: 100,                  
  nested_lists_per_page: 10,            
  items_in_nested_list: 100,            
  nesting_depth: 3,                     
  
  // Field Limits - Doubled
  fields_per_collection: 'doubled',      
  reference_fields: 10,                  
  multi_reference_fields: 10,           
  rich_text_length: 10000,             
  plain_text_length: 2000,            

  // API Limits - Enhanced
  content_delivery_api: true,           
  api_cdn_delivery: true,               
  api_calls_per_minute: 60,             
  api_payload_size: '4MB',              

  // Page Limits
  pages_per_site: 100,                  
  page_size: '10MB',                    
  custom_code: '10000 chars'             
};
```

### 2.2 Publishing Constraints

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

## 3. 📚 Collection List Patterns & Solutions

### 3.1 ID Duplication
Webflow duplicates IDs across Collection items. Never target by #id inside Collection Lists.

```javascript
// ✅ Use classes or data attributes
document.querySelectorAll('.action-button').forEach(btn => btn.addEventListener('click', handler));

// ✅ Delegation (recommended)
document.addEventListener('click', (e) => {
  if (e.target.matches('.action-button')) handler(e)
});
```

### 3.2 Data Attributes as Handles
Attach stable handles for per‑item behavior.
```javascript
function init_collection_items() {
  document.querySelectorAll('.w-dyn-item').forEach((item, i) => {
    item.dataset.itemIndex = String(i);
  });
}
```

### 3.3 Rendering Delays
Collection items render async after DOM ready. Use one of:
```javascript
// Fixed delay (simple)
setTimeout(init_items, 500);

// Retry pattern (robust)
(function retry(attempts = 10){
  const items = document.querySelectorAll('.w-dyn-item');
  if (items.length) return init_items(items);
  if (attempts) setTimeout(() => retry(attempts-1), 200);
})();

// MutationObserver (reactive)
const obs = new MutationObserver(() => init_items());
obs.observe(document.body, { childList: true, subtree: true });
```

### 3.4 Event Delegation
Delegate to document to support dynamic additions.
```javascript
function setup_collection_events() {
  document.addEventListener('click', (e) => {
    const item = e.target.closest('.w-dyn-item');
    if (!item) return;
    if (e.target.matches('.expand-button')) toggle_item(item);
  });
}
```

### 3.5 Progressive Enhancement
Initialize what exists, then observe for additions.
```javascript
function progressive_init() {
  init_existing_items();
  const obs = new MutationObserver(init_existing_items);
  const list = document.querySelector('.w-dyn-list');
  if (list) obs.observe(list, { childList: true });
}
```

.

## 4. 🧩 Development Implications

- Design components around the 100‑items per list display limit
- Budget for 40 lists per page when composing complex layouts (tabs, sliders, etc.)
- Prefer event delegation over per‑item event binding
- Treat nested lists conservatively even though up to 10 are allowed

### 4.1 Quick Validation Script
```javascript
(() => {
  const lists = document.querySelectorAll('.w-dyn-list');
  const nested = document.querySelectorAll('.w-dyn-list .w-dyn-list');
  const maxItems = Math.max(0, ...Array.from(lists).map(l => l.querySelectorAll('.w-dyn-item').length));
  console.table({
    'Collection Lists': `${lists.length}/40`,
    'Nested Lists': `${nested.length}/10`,
    'Max Items in a List': `${maxItems}/100`
  });
})();
```

.

## 5. ✅ Testing Checklist

- [ ] 0 items, 1 item, 100 items in a list
- [ ] Multiple lists on a page (approach 40)
- [ ] Nested lists up to 3 levels with up to 10 nested lists
- [ ] Slow connection: confirm delayed rendering strategies function
- [ ] All breakpoints

---

**Remember**: These constraints are enforced by Webflow and cannot be overridden. Design your architecture to work within them from the start.