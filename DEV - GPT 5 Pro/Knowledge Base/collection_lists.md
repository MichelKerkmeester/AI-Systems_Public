# Webflow Collection Lists - Patterns & Solutions

Master the quirks and patterns of Webflow's collection list system. Handle ID duplication, rendering delays, and dynamic content with proven solutions.

> **📢 Next-Gen CMS Update (2025)**: New limits allow 40 lists per page, 10 nested lists, and 100 items in nested lists. See [platform_constraints.md](./platform_constraints.md) for details.

.

## 1. 🎯 Objective

Provide battle-tested patterns for working with Webflow collection lists, addressing common pitfalls like duplicate IDs, async rendering, and event handling for dynamic items.

**Category**: critical
**Tags**: webflow, collections, cms, dynamic_content, event_delegation
**Priority**: critical

.

## 2. 🔍 ID Duplication Problem

### 2.1 The Core Issue
Webflow duplicates IDs when rendering collection items. Every item in a collection list will have identical IDs for nested elements.

```html
<!-- What you design -->
<div class="collection-item">
  <button id="action-button">Click</button>
</div>

<!-- What Webflow renders (PROBLEM!) -->
<div class="collection-item">
  <button id="action-button">Click</button> <!-- Duplicate ID -->
</div>
<div class="collection-item">
  <button id="action-button">Click</button> <!-- Duplicate ID -->
</div>
```

### 2.2 Solutions

```javascript
// ❌ WRONG - Only gets first element
document.getElementById('action-button').addEventListener('click', handler);

// ✅ CORRECT - Use classes instead
document.querySelectorAll('.action-button').forEach(button => {
  button.addEventListener('click', handler);
});

// ✅ BETTER - Use event delegation
document.addEventListener('click', (e) => {
  if (e.target.matches('.action-button')) {
    handler(e);
  }
});
```

### 2.3 Data Attributes Pattern
```javascript
// Use data attributes for unique identification
function init_collection_items() {
  const items = document.querySelectorAll('.w-dyn-item');

  items.forEach((item, index) => {
    // Add unique identifier
    item.dataset.itemIndex = index;

    // Find child elements by class
    const button = item.querySelector('.action-button');
    if (button) {
      button.dataset.itemId = item.dataset.itemId || index;
    }
  });
}
```

.

## 3. ⏱️ Rendering Delays

### 3.1 The Timing Problem
Collection lists render asynchronously after the DOM loads. Your code may run before items exist.

```javascript
// ❌ WRONG - Items might not exist yet
document.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('.w-dyn-item');
  console.log(items.length); // Often 0!
});
```

### 3.2 Delay Solutions

```javascript
// ✅ SOLUTION 1: Fixed delay
function init_with_delay() {
  setTimeout(() => {
    const items = document.querySelectorAll('.w-dyn-item');
    if (items.length > 0) {
      items.forEach(init_item);
    }
  }, 500); // 500ms usually sufficient
}

// ✅ SOLUTION 2: Retry pattern
function init_with_retry(attempts = 10) {
  const items = document.querySelectorAll('.w-dyn-item');

  if (items.length > 0) {
    items.forEach(init_item);
  } else if (attempts > 0) {
    setTimeout(() => init_with_retry(attempts - 1), 200);
  }
}

// ✅ SOLUTION 3: MutationObserver
function init_with_observer() {
  const observer = new MutationObserver((mutations, obs) => {
    const items = document.querySelectorAll('.w-dyn-item');
    if (items.length > 0) {
      items.forEach(init_item);
      obs.disconnect(); // Stop observing
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
}
```

.

## 4. 🎯 Event Delegation

### 4.1 Why Delegation?
Event delegation handles dynamically added items without rebinding events.

```javascript
// ❌ WRONG - Won't work for new items
document.querySelectorAll('.item-button').forEach(btn => {
  btn.addEventListener('click', handle_click);
});

// ✅ CORRECT - Works for all current and future items
document.addEventListener('click', (event) => {
  // Check if clicked element matches selector
  if (event.target.matches('.item-button')) {
    handle_click(event);
  }

  // Or check if clicked inside an item
  const item = event.target.closest('.w-dyn-item');
  if (item && event.target.matches('.item-button')) {
    handle_item_click(event, item);
  }
});
```

### 4.2 Delegation Patterns

```javascript
// Complete delegation setup
function setup_collection_events() {
  // Single listener for all collection interactions
  document.addEventListener('click', handle_collection_clicks);
  document.addEventListener('change', handle_collection_changes);
  document.addEventListener('input', handle_collection_inputs);
}

function handle_collection_clicks(event) {
  // Get the collection item context
  const item = event.target.closest('.w-dyn-item');
  if (!item) return;

  // Route based on element class
  if (event.target.matches('.expand-button')) {
    toggle_item_expansion(item);
  } else if (event.target.matches('.delete-button')) {
    handle_item_deletion(item);
  } else if (event.target.matches('.share-button')) {
    handle_item_share(item);
  }
}
```

.

## 5. 🛠️ Initialization Patterns

### 5.1 Progressive Enhancement
```javascript
// Initialize items as they become available
function progressive_init() {
  // Initialize existing items
  init_existing_items();

  // Watch for new items
  observe_new_items();

  // Setup delegation for interactions
  setup_event_delegation();
}

function init_existing_items() {
  document.querySelectorAll('.w-dyn-item:not([data-initialized])').forEach(item => {
    item.dataset.initialized = 'true';
    enhance_item(item);
  });
}

function observe_new_items() {
  const observer = new MutationObserver(() => {
    init_existing_items(); // Re-run for new items
  });

  const list = document.querySelector('.w-dyn-list');
  if (list) {
    observer.observe(list, { childList: true });
  }
}
```

### 5.2 Collection-Aware Component
```javascript
class CollectionManager {
  constructor(selector) {
    this.selector = selector;
    this.items = new Map();
    this.init();
  }

  init() {
    // Wait for Webflow to render
    if (window.Webflow && window.Webflow.push) {
      window.Webflow.push(() => this.setup());
    } else {
      setTimeout(() => this.setup(), 500);
    }
  }

  setup() {
    this.find_items();
    this.setup_delegation();
    this.observe_changes();
  }

  find_items() {
    document.querySelectorAll(this.selector).forEach((item, index) => {
      const id = item.dataset.itemId || `item-${index}`;
      this.items.set(id, item);
      this.enhance_item(item, id);
    });
  }

  enhance_item(item, id) {
    // Add enhancements
    item.dataset.enhanced = 'true';
    item.dataset.internalId = id;
  }
}
```

.

## 6. ✅ Best Practices

### 6.1 Do's
```javascript
// ✅ Use classes for selection
document.querySelectorAll('.collection-button')

// ✅ Use event delegation
document.addEventListener('click', handler)

// ✅ Wait for rendering
setTimeout(init, 500)

// ✅ Check for existence
if (items && items.length > 0)

// ✅ Mark processed items
item.dataset.initialized = 'true'
```

### 6.2 Don'ts
```javascript
// ❌ Never use IDs in collections
document.getElementById('item-button')

// ❌ Don't bind directly to items
item.addEventListener('click', handler)

// ❌ Don't assume immediate availability
document.querySelectorAll('.w-dyn-item')[0]

// ❌ Don't process items twice
// Always check: if (!item.dataset.initialized)
```

### 6.3 Testing Checklist

#### Universal Tests (All CMS Versions)
- [ ] Test with 0 collection items
- [ ] Test with 1 item (edge case)
- [ ] Test with 100 items (max per list)
- [ ] Test adding items dynamically
- [ ] Test in all breakpoints
- [ ] Test with slow connection (rendering delay)

#### Legacy CMS Specific
- [ ] Test with 20 collection lists per page (max)
- [ ] Test with 1 nested list (max)
- [ ] Test with 5 items in nested list (max)
- [ ] Test reference fields (5 max)

#### Next-Gen CMS Specific (2025+)
- [ ] Test with 40 collection lists per page (new max)
- [ ] Test with 10 nested lists (new max)
- [ ] Test with 100 items in nested list (new max)
- [ ] Test multi-level nesting (up to 3 levels deep)
- [ ] Test reference fields (10 max)
- [ ] Test Content Delivery API integration
- [ ] Test with large datasets (1M+ items per collection)

### 6.4 Debug Helper
```javascript
// Add to console for collection diagnostics
window.debug_collections = () => {
  // Detect CMS version
  const isNextGen = document.querySelector('[data-wf-version="next-gen"]') !== null;
  const maxLists = isNextGen ? 40 : 20;
  const maxNested = isNextGen ? 10 : 1;
  const maxItemsInNested = isNextGen ? 100 : 5;

  const lists = document.querySelectorAll('.w-dyn-list');
  const nestedLists = document.querySelectorAll('.w-dyn-list .w-dyn-list');

  console.log(`CMS Version: ${isNextGen ? 'Next-Gen' : 'Legacy'}`);
  console.log(`Collection Lists: ${lists.length}/${maxLists}`);
  console.log(`Nested Lists: ${nestedLists.length}/${maxNested}`);
  console.log('---');

  lists.forEach((list, i) => {
    const items = list.querySelectorAll('.w-dyn-item');
    const isNested = list.closest('.w-dyn-item') !== null;
    const itemLimit = isNested ? maxItemsInNested : 100;

    console.log(`List ${i + 1}:`, {
      type: isNested ? 'nested' : 'top-level',
      items: `${items.length}/${itemLimit}`,
      initialized: list.querySelectorAll('[data-initialized]').length,
      visible: list.offsetParent !== null,
      nestingLevel: list.closest('.w-dyn-list .w-dyn-list .w-dyn-list') ? 3 :
                   list.closest('.w-dyn-list .w-dyn-list') ? 2 : 1
    });
  });
};
```

## 📚 Related Documentation

- [webflow_platform_constraints.md](./webflow_platform_constraints.md) - Collection limits
- [initialization_pattern.md](./initialization_pattern.md) - Proper init timing
- [webflow_debugging.md](./webflow_debugging.md) - Debug collection issues

---

**Remember**: Always use classes, never IDs. Always use delegation, never direct binding. Always wait for rendering, never assume immediate availability.