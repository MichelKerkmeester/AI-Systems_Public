# Webflow Debugging - Tools & Techniques

Debug Webflow projects effectively with specialized console methods, state inspection tools, and testing strategies for the platform's unique behaviors.

.

## 1. 🎯 Objective

Provide a comprehensive debugging toolkit specifically for Webflow's environment, including console helpers, state inspection methods, and systematic testing approaches.

**Category**: tooling
**Tags**: webflow, debugging, console, testing, troubleshooting
**Priority**: high

.

## 2. 🛠️ Console Toolkit

### 2.1 Enhanced Console Methods
```javascript
// Create color-coded console for better visibility
const console_enhanced = {
  webflow: (message, data) => {
    console.log(`%c[Webflow] ${message}`, 'color: #146EF5', data);
  },
  collection: (message, data) => {
    console.log(`%c[Collection] ${message}`, 'color: #9B59B6', data);
  },
  timing: (message, data) => {
    console.log(`%c[Timing] ${message}`, 'color: #E67E22', data);
  },
  error: (message, data) => {
    console.error(`%c[Error] ${message}`, 'color: #E74C3C', data);
  },
  success: (message, data) => {
    console.log(`%c[Success] ${message}`, 'color: #27AE60', data);
  },
  warning: (message, data) => {
    console.warn(`%c[Warning] ${message}`, 'color: #F39C12', data);
  }
};

// Usage
console_enhanced.webflow('IX2 loaded', { status: 'ready' });
console_enhanced.collection('Items found', { count: 42 });
console_enhanced.error('Form submission failed', { code: 500 });
```

### 2.2 Debug Mode Toggle
```javascript
// Global debug mode for verbose logging
window.WEBFLOW_DEBUG = {
  enabled: false,
  verbose: false,

  enable() {
    this.enabled = true;
    console_enhanced.success('Debug mode enabled', {
      timestamp: new Date().toISOString()
    });
    return this;
  },

  disable() {
    this.enabled = false;
    console.log('Debug mode disabled');
    return this;
  },

  log(category, message, data) {
    if (!this.enabled) return;
    console_enhanced[category] ?
      console_enhanced[category](message, data) :
      console.log(`[${category}] ${message}`, data);
  }
};

// Enable from console: WEBFLOW_DEBUG.enable()
```

### 2.3 Performance Profiling
```javascript
// Track component initialization times
class PerformanceTracker {
  constructor() {
    this.marks = new Map();
  }

  start(label) {
    this.marks.set(label, performance.now());
    console_enhanced.timing(`Started: ${label}`, {
      timestamp: new Date().toISOString()
    });
  }

  end(label) {
    const start = this.marks.get(label);
    if (!start) {
      console_enhanced.error('No start mark found', { label });
      return;
    }

    const duration = performance.now() - start;
    const status = duration > 100 ? '⚠️ SLOW' : '✅ OK';

    console_enhanced.timing(`Completed: ${label}`, {
      duration: `${duration.toFixed(2)}ms`,
      status
    });

    this.marks.delete(label);
    return duration;
  }
}

const perf = new PerformanceTracker();
```

.

## 3. 🔍 State Inspection

### 3.1 Webflow State Inspector
```javascript
function check_webflow_state() {
  console.group('🔍 Webflow State Check');

  // Core object
  console.log('Webflow object:', typeof window.Webflow !== 'undefined' ? '✅ Loaded' : '❌ Missing');

  // Modules
  if (window.Webflow) {
    console.log('IX2 (Interactions):', window.Webflow.ix2 ? '✅' : '❌');
    console.log('Commerce:', window.Webflow.commerce ? '✅' : '❌');
    console.log('Require:', window.Webflow.require ? '✅' : '❌');
    console.log('Push queue:', Array.isArray(window.Webflow.push) ? '✅' : '❌');
  }

  // Collections
  const lists = document.querySelectorAll('.w-dyn-list');
  const items = document.querySelectorAll('.w-dyn-item');
  console.log('Collection lists:', lists.length);
  console.log('Collection items:', items.length);

  // Forms
  const forms = document.querySelectorAll('.w-form');
  console.log('Forms:', forms.length);

  // Locale
  const locale = document.documentElement.lang || 'default';
  console.log('Current locale:', locale);

  // Editor mode
  const isEditor = document.querySelector('.w-editor') !== null;
  console.log('Editor mode:', isEditor ? '⚠️ Yes' : '✅ No');

  console.groupEnd();
}

// Add to window for easy access
window.wf_state = check_webflow_state;
```

### 3.2 Collection Inspector
```javascript
function inspect_collections() {
  console.group('🔍 Collection Inspector');

  const lists = document.querySelectorAll('.w-dyn-list');

  lists.forEach((list, index) => {
    const items = list.querySelectorAll('.w-dyn-item');
    const empty = list.querySelector('.w-dyn-empty');

    console.group(`Collection List ${index + 1}`);
    console.log('Items:', items.length);
    console.log('Empty state:', empty ? 'Present' : 'None');
    console.log('Visible:', list.offsetParent !== null);
    console.log('Classes:', Array.from(list.classList).join(', '));

    // Sample first item structure
    if (items.length > 0) {
      console.log('First item structure:', items[0]);
    }

    console.groupEnd();
  });

  console.groupEnd();
}

window.wf_collections = inspect_collections;
```

### 3.3 Form State Inspector
```javascript
function inspect_forms() {
  console.group('🔍 Form Inspector');

  document.querySelectorAll('form').forEach((form, index) => {
    console.group(`Form ${index + 1}`);
    console.log('Name:', form.name || 'unnamed');
    console.log('Action:', form.action || 'none');
    console.log('Method:', form.method || 'GET');
    console.log('Fields:', form.elements.length);
    console.log('Valid:', form.checkValidity() ? '✅' : '❌');

    // Check for Webflow form wrapper
    const wrapper = form.closest('.w-form');
    console.log('Webflow wrapper:', wrapper ? '✅' : '❌');

    // Check for success/error blocks
    if (wrapper) {
      const done = wrapper.querySelector('.w-form-done');
      const fail = wrapper.querySelector('.w-form-fail');
      console.log('Success block:', done ? '✅' : '❌');
      console.log('Error block:', fail ? '✅' : '❌');
    }

    console.groupEnd();
  });

  console.groupEnd();
}

window.wf_forms = inspect_forms;
```

.

## 4. 🧪 Testing Patterns

### 4.1 Breakpoint Testing
```javascript
// Test across all Webflow breakpoints
function test_breakpoints() {
  const breakpoints = [
    { name: 'Desktop', width: 1920 },
    { name: 'Tablet', width: 991 },
    { name: 'Mobile Landscape', width: 767 },
    { name: 'Mobile Portrait', width: 478 }
  ];

  console.group('🧪 Breakpoint Tests');

  const current = window.innerWidth;
  console.log(`Current: ${current}px`);

  breakpoints.forEach(bp => {
    const status = current >= bp.width ? 'Active' : 'Inactive';
    console.log(`${bp.name} (${bp.width}px): ${status}`);
  });

  console.groupEnd();
}
```

### 4.2 Locale Testing
```javascript
// Test locale-specific content
function test_locales() {
  const locales = ['/', '/en', '/de', '/fr', '/es'];

  console.group('🧪 Locale Testing');

  locales.forEach(locale => {
    console.log(`Testing ${locale}:`, {
      url: `${window.location.origin}${locale}`,
      current: window.location.pathname.startsWith(locale)
    });
  });

  console.groupEnd();
}
```

### 4.3 Collection Limit Testing
```javascript
function test_collection_limits() {
  console.group('🧪 Collection Limit Tests');

  const lists = document.querySelectorAll('.w-dyn-list');
  const results = [];

  // Test list count
  const listTest = {
    test: 'Collection lists per page',
    limit: 20,
    actual: lists.length,
    status: lists.length <= 20 ? '✅ PASS' : '❌ FAIL'
  };
  results.push(listTest);

  // Test items per list
  lists.forEach((list, i) => {
    const items = list.querySelectorAll('.w-dyn-item');
    results.push({
      test: `List ${i + 1} item count`,
      limit: 100,
      actual: items.length,
      status: items.length <= 100 ? '✅ PASS' : '❌ FAIL'
    });
  });

  // Test nested lists
  const nested = document.querySelectorAll('.w-dyn-list .w-dyn-list');
  results.push({
    test: 'Nested lists',
    limit: 1,
    actual: nested.length,
    status: nested.length <= 1 ? '✅ PASS' : '❌ FAIL'
  });

  console.table(results);
  console.groupEnd();
}
```

.

## 5. 🐛 Common Issues

### 5.1 Quick Diagnostics
```javascript
// One-click diagnostic suite
function diagnose_issues() {
  console.group('🐛 Webflow Diagnostics');

  // Check initialization
  if (!window.Webflow) {
    console_enhanced.error('Webflow not loaded', {
      solution: 'Check script loading order'
    });
  }

  // Check collections
  const items = document.querySelectorAll('.w-dyn-item');
  if (items.length === 0) {
    console_enhanced.warning('No collection items', {
      solution: 'Check CMS content or wait for rendering'
    });
  }

  // Check duplicate IDs
  const ids = {};
  document.querySelectorAll('[id]').forEach(el => {
    if (ids[el.id]) {
      console_enhanced.error(`Duplicate ID: ${el.id}`, {
        solution: 'Use classes in collection lists'
      });
    }
    ids[el.id] = true;
  });

  // Check form setup
  document.querySelectorAll('form').forEach(form => {
    const wrapper = form.closest('.w-form');
    if (!wrapper) {
      console_enhanced.warning('Form missing .w-form wrapper', {
        form: form,
        solution: 'Wrap form in .w-form div'
      });
    }
  });

  console.groupEnd();
}

window.wf_diagnose = diagnose_issues;
```

### 5.2 Event Listener Audit
```javascript
// Check what events are attached
function audit_events(element) {
  const events = getEventListeners(element); // Chrome DevTools only

  console.group('🔍 Event Listeners');
  Object.keys(events).forEach(type => {
    console.log(`${type}:`, events[type].length, 'listeners');
    events[type].forEach(listener => {
      console.log('  →', listener);
    });
  });
  console.groupEnd();
}
```

### 5.3 Chrome DevTools MCP Integration
```javascript
// Chrome DevTools MCP provides advanced debugging capabilities
// Configuration: mcp_servers.json

/**
 * Chrome DevTools MCP Workflow:
 * 1. Navigate → Go to target page
 * 2. Snapshot → Capture DOM state with UIDs
 * 3. Analyze → Use UIDs for precise targeting
 * 4. Act → Execute fixes based on evidence
 */

// Example: Debugging Webflow with Chrome DevTools MCP
async function debugWebflowWithMCP() {
  console.group('🔧 Chrome DevTools MCP Workflow');

  // Step 1: Navigate to the page
  // chrome_navigate({ url: "https://site.webflow.io/page" });

  // Step 2: Take snapshot for DOM analysis
  // const snapshot = chrome_snapshot();
  // Returns DOM structure with unique UIDs for each element

  // Step 3: Use UIDs for precise element targeting
  // chrome_evaluate({
  //   code: `document.querySelector('[uid="ABC123"]').textContent`
  // });

  // Step 4: Monitor console for errors
  // chrome_console_logs(); // Get all console output

  // Step 5: Check network activity
  // chrome_network(); // Review API calls and resource loading

  console_enhanced.success('Chrome DevTools MCP Workflow', {
    tips: [
      'Use UIDs from snapshots for stable selectors',
      'Prefer data attributes over classes',
      'Avoid nth-child or complex paths',
      'Monitor console logs for runtime errors',
      'Check network tab for failed requests'
    ]
  });

  console.groupEnd();
}

/**
 * Chrome DevTools MCP Best Practices:
 *
 * Element Selection:
 * - ✅ Use: [uid="XYZ"], #unique-id, [data-attribute]
 * - ❌ Avoid: .class:nth-child(3), complex selectors
 *
 * Debugging Patterns:
 * - Form Issues: Snapshot → Find form UID → Evaluate validation
 * - Event Issues: Console logs → Trace execution flow
 * - Async Issues: Network tab → Check timing/order
 * - Style Issues: Evaluate computed styles directly
 *
 * Configuration Tips:
 * - Use --headless=true for CI/CD workflows
 * - Use --isolated=true for clean sessions
 * - Configure permissions in CLAUDE.md for tool access
 */

// Advanced: Create reusable debug workflows
const WebflowDebugWorkflows = {
  // Debug form submission issues
  async debugForm(formSelector) {
    // 1. Navigate to page
    // 2. Take snapshot
    // 3. Find form by UID
    // 4. Fill form fields
    // 5. Submit and monitor network
    // 6. Check console for errors
    console.log('Form debug workflow for:', formSelector);
  },

  // Debug collection rendering
  async debugCollection(listSelector) {
    // 1. Navigate to page
    // 2. Wait for collection to load
    // 3. Snapshot DOM state
    // 4. Count items and check structure
    // 5. Verify event handlers
    console.log('Collection debug workflow for:', listSelector);
  },

  // Debug interactions/animations
  async debugInteraction(triggerSelector) {
    // 1. Navigate and snapshot initial state
    // 2. Trigger interaction
    // 3. Snapshot after state
    // 4. Compare DOM changes
    // 5. Check for console errors
    console.log('Interaction debug workflow for:', triggerSelector);
  }
};
```

.

## 6. ✅ Debug Checklist

### 6.1 Initial Setup
```javascript
// Add all debug helpers to window
(() => {
  // Make all tools globally available
  window.wf_debug = {
    state: check_webflow_state,
    collections: inspect_collections,
    forms: inspect_forms,
    diagnose: diagnose_issues,
    breakpoints: test_breakpoints,
    limits: test_collection_limits,

    // Run all checks
    all() {
      this.state();
      this.collections();
      this.forms();
      this.diagnose();
      this.limits();
    }
  };

  console_enhanced.success('Debug tools loaded', {
    usage: 'Run wf_debug.all() for complete diagnostic'
  });
})();
```

### 6.2 Quick Commands
| Command | Purpose |
|---------|---------|
| `wf_state()` | Check Webflow object state |
| `wf_collections()` | Inspect all collections |
| `wf_forms()` | Inspect all forms |
| `wf_diagnose()` | Run diagnostic checks |
| `wf_debug.all()` | Run everything |
| `WEBFLOW_DEBUG.enable()` | Enable verbose logging |

### 6.3 Debug Workflow
1. Open browser console (F12)
2. Run `wf_debug.all()` for overview
3. Check for red error messages
4. Review yellow warnings
5. Use specific inspectors for deep dive
6. Enable verbose logging if needed
7. Test in different breakpoints
8. Verify in published site

## 📚 Related Documentation

- [webflow_platform_constraints.md](./webflow_platform_constraints.md) - Understanding limits
- [webflow_collection_lists.md](./webflow_collection_lists.md) - Collection-specific issues
- [initialization_pattern.md](./initialization_pattern.md) - Timing issues

---

**Pro tip**: Bookmark this snippet for instant debugging:
```javascript
javascript:(function(){const s=document.createElement('script');s.src='[YOUR_DEBUG_SCRIPT_URL]';document.head.appendChild(s)})();
```