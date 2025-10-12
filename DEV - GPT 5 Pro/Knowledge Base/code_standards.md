# Code Standards & Naming Conventions

Defines the mandatory code conventions for JavaScript, CSS, and inline documentation. Keep naming predictable across languages and layers, keep comments focused on intent and platform constraints, and enforce minimal headers without metadata or ticket references.

.

## 1. 🧾 Naming Reference

| Type | Rule | Example |
|------|------|---------|
| Variables (JS/Python) | `snake_case` | `user_name`, `form_data` |
| Functions | `snake_case` | `get_data()`, `handle_submit()` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_SIZE`, `API_ENDPOINT` |
| Classes | PascalCase | `UserModel`, `FormValidator` |
| Private Members | `_snake_case` | `_internal_state`, `_cache` |
| Booleans | `is_` / `has_` / `can_` prefix | `is_active`, `has_data` |
| Event Handlers | `handle_` prefix | `handle_click`, `handle_submit` |
| Callbacks | `on_` prefix | `on_success`, `on_error` |
| CSS Classes | `kebab-case` | `.card`, `.navigation` |
| CSS BEM Block | `kebab-case` | `.nav--item`, `.hero--section` |
| CSS BEM Modifier | `-` separator | `.card--featured-large` |
| JS Files | `snake_case` | `form_validator.js` |
| Directories | `snake_case` | `src/components/` |

.

## 2. 🗂️ File & Section Headers

### 2.1 JavaScript File Header
```javascript
// ───────────────────────────────────────────────────────────────
// COMPONENT: NAME
// ───────────────────────────────────────────────────────────────
```

### 2.2 CSS File Header
```css
/* ───────────────────────────────────────────────────────────────
   COMPONENT - NAME
─────────────────────────────────────────────────────────────── */
```

### 2.3 Never Include
- Task IDs or ticket numbers
- Author names or dates
- Version numbers or release info
- Project management metadata
- Descriptive paragraphs (headers stay minimal)

### 2.4 Section Headers (Numbered)
```javascript
/* ─────────────────────────────────────────────────────────────
   1. INITIALIZATION
──────────────────────────────────────────────────────────────── */
```

```css
/* ───────────────────────────────────────────────────────────────
   2. BASE STYLES
─────────────────────────────────────────────────────────────── */
```

### 2.5 Initialization Pattern (Webflow)
```javascript
/* ─────────────────────────────────────────────────────────────
   INITIALIZATION
──────────────────────────────────────────────────────────────── */
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init_function);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init_function);
} else {
  init_function();
}
```
**Required**: Use `else if` to prevent double initialization. Never use separate `if` statements.

.

## 3. 💬 Commenting Rules

### 3.1 Quantity & Focus
- Maximum five comments per ten lines of code.
- Explain **why** logic exists or reference Webflow constraints.
- Avoid narrating implementation details.

### 3.2 Configuration Comments
Comments above constants explain their purpose and constraints:

```javascript
// Cache Botpoison client instances per public key to avoid recreation
const botpoison_clients = new Map();

// Timeout values for various fallback mechanisms
const HERO_FALLBACK_MS = 3000;
const WELCOME_FALLBACK_MS = 4500;

// Selector for forms using Formspark endpoints
const FORMSPARK_SELECTOR = 'form[action*="submit-form.com"]';

// Default to 100px offset if invalid
return { enable, offset: isNaN(offset) ? 100 : offset };
```

### 3.3 Function Purpose Comments
Single-line comment above function describes intent and return behavior:

```javascript
// Load Botpoison SDK from CDN if not already loaded
// Returns promise resolving to true on success, false on failure
function load_botpoison_sdk() {}

// Read cookie value with fallback to manual parsing when js-cookie library unavailable
function read_cookie(name) {}

// Show modal with entrance animation using Motion.dev
// Make container visible before animating to avoid layout jumps
async function show_modal() {}

// Extract Dutch mobile digits from a raw string
// Normalize user input to digits and strip Dutch prefixes
function extract_nl_mobile_digits(raw) {}
```

### 3.4 Inline Logic Comments
Explain **why** decisions are made, not what the code does:

```javascript
// Prevent background scroll while modal is open
if (window.lenis) {
  window.lenis.stop();
}

// Warn if endpoint doesn't appear to be Formspark
if (endpoint && !endpoint.includes('submit-form.com')) {
  console.warn(`${LOG_PREFIX} Form endpoint may not be Formspark:`, endpoint);
}

// Add 10 second timeout to prevent infinite hang
const timeout = new Promise((_, reject) =>
  setTimeout(() => reject(new Error('Botpoison timeout')), 10000)
);

// Use modern Array.from or fallback to slice
return Array.from ? Array.from(node_list) : Array.prototype.slice.call(node_list);
```

### 3.5 Platform/Library-Specific Comments
Reference external constraints or integration details:

```javascript
// WEBFLOW: collection list constraint (max 100 items)
// BOTPOISON: Challenge may take several seconds on slow connections
// MIYAGI: requires Miyagi.ready() initialization

// Detect debug mode from URL query parameter (?debug=true)
const debug_enabled = (() => {
  try {
    return new URLSearchParams(window.location.search).has('debug');
  } catch (e) {
    return false;
  }
})();

// Conditional logging for debug mode
function log(...args) {
  if (debug_enabled) {
    console.log(LOG_PREFIX, ...args);
  }
}
```

### 3.6 Error Handling & Fallback Comments
Explain recovery strategies and graceful degradation:

```javascript
// Ensure usable end state on animation failure
modal.style.opacity = '1';
modal.style.transform = 'scale(1) translateY(0)';

// Animate when Motion.dev is available, otherwise set end states
if (window.Motion?.animate) {
  // animation code
} else {
  // fallback code
}

// Retry on rate limiting with exponential backoff
if (response.status === 429 && attempt <= MAX_RETRIES) {
  const delay = 1000 * Math.pow(2, attempt - 1);
  console.warn(`Rate limited. Retrying in ${delay}ms`);
  await new Promise((resolve) => setTimeout(resolve, delay));
}
```

### 3.7 Data Transformation Comments
Explain complex data processing steps:

```javascript
// Format digits into +31 mobile layout and capture caret positions
function format_nl_mobile_value(raw) {}

// Map a digit index back to the formatted caret position
function caret_from_digit_positions(result, digit_count) {}

// Support both comma and pipe separators
const parts = attr
  .split(/[|,]/)
  .map((s) => s.trim())
  .filter(Boolean);
```

### 3.8 Guard Clause & Early Return Comments
Explain validation checks when not obvious:

```javascript
// Check if scope itself is a form
if (scope.matches && scope.matches('form')) return scope;

// Skip if already initialized
if (dialog.dataset.welcomeInitialized === 'true') return;
```

### 3.9 Performance & Optimization Comments
Explain caching, debouncing, or optimization choices:

```javascript
// Cache Botpoison client instances per public key to avoid recreation
const botpoison_clients = new Map();

// Debounce utility for performance
const debounce = (fn, d=300) => {
  let t;
  return (...a) => {
    clearTimeout(t);
    t = setTimeout(() => fn(...a), d);
  };
};

// Query elements fresh each time to handle DOM changes
function get_elements() {
  const dialog = document.querySelector(CONFIG.selectors.dialog);
  return { dialog, modal, background };
}
```

### 3.10 State Management Comments
Explain state structure and purpose:

```javascript
// Gate structure tracks interception state for FsCC banner and manager modals
function create_gate(selector) {
  return {
    selector,
    element: null,
    original_open: null,
    release_requested: false
  };
}

// Visitor state determines sequencing flow (welcome → cookie consent)
const state = {
  has_seen_welcome: false,
  has_consent: false,
  awaiting_welcome_close: false
};
```

### 3.11 CSS Inline Comments
```css
.component { /* compact inline CSS comment */ }

/* Override FsCC inline styles with !important */
el.style.setProperty('display', 'none', 'important');
```

### 3.12 JSDoc Usage (Minimal)
```javascript
/**
 * Process user data and return formatted result
 * @param {Object} data - Raw user data
 * @returns {Object} Formatted user object
 */
function process_user_data(data) {}
```
Use JSDoc only for public APIs or complex shared utilities.

### 3.13 Bad Examples (Anti-Patterns)
```javascript
// ❌ Narrating what code does
// Set price to price times 100
const price_cents = price * 100;

// ❌ Obvious comments
// Loop through items
for (const item of items) {}

// ❌ Commented-out code (delete instead)
// const old_value = calculate_old_way();

// ❌ TODO without context
// TODO: fix this

// ✅ GOOD: Explains WHY
// Convert to cents to avoid floating point errors
const price_cents = price * 100;

// ✅ GOOD: Adds context for non-obvious code
// Webflow duplicates IDs in collection lists - use class selector
const elements = document.querySelectorAll('.card');

// ✅ GOOD: Explains constraint
// PERFORMANCE: Cache result - recalculation is expensive (10k+ items)
const cached_result = compute_heavy_operation();
```

.

## 4. 🔖 Special Markers

### 4.1 Priority Flags
Use uppercase markers for critical information:

```javascript
// CRITICAL: handles authentication - do not modify
// PERFORMANCE: optimized for 10k+ items
// SECURITY: sanitizes user input
// DEPRECATED: use new_function() instead
// BREAKING: this change requires migration
```

### 4.2 Platform/Integration Markers
Reference external systems and constraints:

```javascript
// WEBFLOW: collection list constraint (max 100 items)
// WEBFLOW: Designer API limitation - cannot modify locked elements
// MIYAGI: requires Miyagi.ready() initialization
// BOTPOISON: Challenge may take several seconds
// FORMSPARK: API rate limit is 100 requests/hour
// MOTION: Animation requires Motion.dev library
// LENIS: Smooth scroll integration point
```

### 4.3 Temporary Markers (Use Sparingly)
```javascript
// FIXME: memory leak in event listener - track down source
// HACK: workaround for Safari bug - remove when iOS 18 ships
// NOTE: this approach was chosen over X because Y
```

Avoid generic TODO comments without context or ownership.

.

## 5. ✅ Enforcement & Tooling

### 5.1 Validation Rules
- File headers are exactly three lines.
- No metadata in comments.
- Follow naming table for all identifiers.
- Keep comments intentional and concise.

### 5.2 Common Violations
```javascript
// ❌ WRONG
// Task: PROJ-123
// Author: Developer
// Date: 2024-01-15

// ✅ RIGHT
// ───────────────────────────────────────────────────────────────
// NAVIGATION: MAIN
// ───────────────────────────────────────────────────────────────
```

### 5.3 Tool Support
- **ESLint** enforces snake_case and header constraints.
- **Stylelint** validates CSS naming patterns.

---

**Rembember**:  Keep naming predictable across languages and layers, keep comments focused on intent and platform constraints