# Common Code Violations & Fixes

**Purpose**: Top 10 most frequently encountered violations with detailed fix guidance
**Based On**: Analysis of 37 JavaScript files and project code standards
**Last Updated**: 2025-10-18

---

## Top 10 Violations (Ranked by Frequency)

### 1. Missing Webflow Initialization Pattern (Rule 4.1)
**Frequency**: Very High
**Severity**: P0 - ERROR (BLOCKING)
**Category**: Initialization Pattern

**Issue**: File does not include the required three-branch Webflow initialization pattern

**Why This Happens**:
- Developers copy initialization from non-Webflow projects
- Using simple `DOMContentLoaded` without Webflow.push check
- Forgetting to add initialization when creating new components

**Incorrect Patterns**:
```javascript
// ❌ WRONG - Direct DOMContentLoaded only
document.addEventListener('DOMContentLoaded', init);

// ❌ WRONG - jQuery ready
$(document).ready(init);

// ❌ WRONG - window.onload (overwrites other handlers)
window.onload = init;

// ❌ WRONG - Separate if statements (should be if-else chain)
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init);
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
}
```

**Correct Pattern**:
```javascript
// ✅ CORRECT - Three-branch pattern
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
```

**Reference**: `knowledge/initialization_pattern.md:17-34`

---

### 2. camelCase Instead of snake_case (Rule 1.1, 1.2)
**Frequency**: High
**Severity**: P0 - ERROR (BLOCKING)
**Category**: Naming Conventions

**Issue**: Functions and variables use camelCase instead of required snake_case

**Why This Happens**:
- Habit from other JavaScript projects
- Auto-complete suggesting camelCase
- Copying code from external sources

**Incorrect Examples**:
```javascript
// ❌ WRONG - Functions
function getData() { ... }
function handleClick() { ... }
function initComponent() { ... }

// ❌ WRONG - Variables
const userData = {};
let isActive = false;
const formData = new FormData();
```

**Correct Examples**:
```javascript
// ✅ CORRECT - Functions
function get_data() { ... }
function handle_click() { ... }
function init_component() { ... }

// ✅ CORRECT - Variables
const user_data = {};
let is_active = false;
const form_data = new FormData();
```

**Quick Fix Strategy**:
1. Use editor's find/replace with regex: `([a-z])([A-Z])` → `$1_$2` (lowercase second capture)
2. Manually review camelCase identifiers
3. Test after renaming to ensure no breakage

**Reference**: `knowledge/code_standards.md:7-24`

---

### 3. Incorrect File Header Format (Rule 2.1, 2.2)
**Frequency**: High
**Severity**: P0 - ERROR (BLOCKING)
**Category**: File Headers

**Issue**: File header not exactly 3 lines or contains metadata

**Why This Happens**:
- Adding extra information (dates, authors, versions)
- Using different comment styles
- Copying headers from other projects

**Incorrect Examples**:
```javascript
// ❌ WRONG - Too many lines with metadata
// ───────────────────────────────────────────────────────────────
// MODAL: WELCOME
// Author: John Doe
// Date: 2024-10-15
// Version: 1.0.0
// ───────────────────────────────────────────────────────────────

// ❌ WRONG - Wrong style (block comment)
/*
 * MODAL: WELCOME
 */

// ❌ WRONG - Not enough separator lines
// MODAL: WELCOME
```

**Correct Format**:
```javascript
// ✅ CORRECT - Exactly 3 lines, no metadata
// ───────────────────────────────────────────────────────────────
// MODAL: WELCOME
// ───────────────────────────────────────────────────────────────
```

**Template** (use exact separator format as in standards):
```javascript
// ───────────────────────────────────────────────────────────────
// [CATEGORY]: [COMPONENT NAME]
// ───────────────────────────────────────────────────────────────
```

**Reference**: `knowledge/code_standards.md:40-65`

---

### 4. Excessive Comment Density (Rule 3.1)
**Frequency**: Medium
**Severity**: P2 - WARNING
**Category**: Commenting

**Issue**: More than 5 comments per 10 lines of code

**Why This Happens**:
- Over-documenting obvious code
- Explaining "what" instead of "why"
- Leaving old commented-out code

**Incorrect Example**:
```javascript
// ❌ WRONG - Too many comments (8 comments in 10 lines)
// Get the user data
const user_data = get_user();
// Check if user exists
if (user_data) {
  // Extract the name
  const name = user_data.name;
  // Log the name
  console.log(name);
  // Update the UI
  update_ui(name);
}
// End of user check
```

**Correct Example**:
```javascript
// ✅ CORRECT - Comments explain "why" only (2 comments in 10 lines)
const user_data = get_user();
if (user_data) {
  const name = user_data.name;
  console.log(name);
  // Update UI optimistically before server confirmation
  update_ui(name);
}
```

**Guidelines**:
- Remove comments that narrate code ("Get the user", "Loop through items")
- Keep comments that explain intent ("Webflow duplicates IDs - use classes", "Retry for slow network connections")
- Remove commented-out code (use version control instead)
- Target: ≤ 5 comments per 10 lines

**Reference**: `knowledge/code_standards.md:80-96`

---

### 5. Using getElementById in Collection Context (Rule 5.1)
**Frequency**: Medium
**Severity**: P1 - ERROR (HIGH)
**Category**: Platform Constraints

**Issue**: Using `getElementById` or `#id` selectors within Webflow collection lists

**Why This Happens**:
- Not aware that Webflow duplicates IDs across collection items
- Assuming IDs are unique (true in standard HTML, false in Webflow collections)

**The Problem**:
Webflow duplicates IDs when rendering collection lists, so multiple elements have the same ID.

**Incorrect Example**:
```javascript
// ❌ WRONG - Targets only first item (ID duplicated across collection)
const button = document.getElementById('action-button');
const card = document.querySelector('#product-card');
```

**Correct Example**:
```javascript
// ✅ CORRECT - Use classes or data attributes
const buttons = document.querySelectorAll('.action-button');
const cards = document.querySelectorAll('[data-product-card]');

// ✅ CORRECT - Event delegation (best for collections)
document.addEventListener('click', (e) => {
  if (e.target.matches('.action-button')) {
    handle_action(e);
  }
});
```

**Reference**: `knowledge/webflow_platform_constraints.md:93-104`

---

### 6. Missing Async Collection Handling (Rule 5.2)
**Frequency**: Medium
**Severity**: P1 - WARNING
**Category**: Platform Constraints

**Issue**: Not handling async rendering of Webflow collection items

**Why This Happens**:
- Assuming collection items exist immediately on DOMContentLoaded
- Not aware of Webflow's async collection rendering

**The Problem**:
Collection items (.w-dyn-item) render asynchronously after page load, so immediate querySelector returns empty.

**Incorrect Example**:
```javascript
// ❌ WRONG - Collection items not loaded yet
function init() {
  const items = document.querySelectorAll('.w-dyn-item');
  items.forEach(setup_item); // items.length === 0
}
```

**Correct Examples**:
```javascript
// ✅ OPTION 1: Fixed delay (simple)
function init() {
  setTimeout(() => {
    const items = document.querySelectorAll('.w-dyn-item');
    items.forEach(setup_item);
  }, 500);
}

// ✅ OPTION 2: Retry pattern (robust)
function init() {
  (function retry(attempts = 10) {
    const items = document.querySelectorAll('.w-dyn-item');
    if (items.length) return setup_items(items);
    if (attempts) setTimeout(() => retry(attempts - 1), 200);
  })();
}

// ✅ OPTION 3: MutationObserver (reactive)
function init() {
  const observer = new MutationObserver(() => {
    const items = document.querySelectorAll('.w-dyn-item');
    if (items.length) {
      setup_items(items);
      observer.disconnect();
    }
  });
  observer.observe(document.body, { childList: true, subtree: true });
}
```

**Reference**: `knowledge/webflow_platform_constraints.md:115-132`

---

### 7. Missing Motion.dev Availability Check (Rule 6.1)
**Frequency**: Medium
**Severity**: P1 - ERROR (HIGH)
**Category**: External Integrations

**Issue**: Using Motion.dev without checking if library is loaded

**Why This Happens**:
- Assuming CDN always loads successfully
- Not considering Designer preview mode (Motion.dev may not load)

**Incorrect Example**:
```javascript
// ❌ WRONG - Motion.dev might not be loaded
window.Motion.animate(element, { opacity: [0, 1] }, { duration: 0.3 });
```

**Correct Example**:
```javascript
// ✅ CORRECT - Check availability first
const motion_available = () => typeof window.Motion?.animate === 'function';

if (motion_available()) {
  window.Motion.animate(element, { opacity: [0, 1] }, { duration: 0.3 });
} else {
  // Fallback: CSS transition or instant change
  element.style.opacity = '1';
}
```

**Pattern for All External Libraries**:
```javascript
// Motion.dev
if (window.Motion?.animate) { ... }

// Lenis
if (window.lenis?.stop) { ... }

// HLS.js
if (window.Hls?.isSupported) { ... }

// Botpoison
if (window.Botpoison) { ... }
```

**Reference**: `specs/claude-skills/analysis/validation-rules.md` (Rule 6.1)

---

### 8. Missing ARIA Attributes on Interactive Elements (Rule 7.1)
**Frequency**: Medium-Low
**Severity**: P2 - WARNING
**Category**: Accessibility

**Issue**: Interactive elements (modals, forms, buttons) lack proper ARIA attributes

**Why This Happens**:
- Focus on visual design over accessibility
- Not aware of screen reader requirements
- Copying code without accessibility considerations

**Common Missing Attributes**:
- **Forms**: `aria-invalid`, `aria-required`, `aria-describedby`
- **Modals**: `aria-label`, `aria-modal`, `role="dialog"`
- **Error Messages**: `role="alert"`, `aria-live="polite"`
- **Accordions**: `aria-expanded`, `aria-controls`

**Incorrect Example**:
```javascript
// ❌ WRONG - No ARIA attributes
const dialog = document.querySelector('.modal');
dialog.show();
```

**Correct Example**:
```javascript
// ✅ CORRECT - Full ARIA support
const dialog = document.querySelector('.modal');
dialog.setAttribute('role', 'dialog');
dialog.setAttribute('aria-modal', 'true');
dialog.setAttribute('aria-label', 'Welcome message');
dialog.setAttribute('aria-describedby', 'modal-description');

// For form fields
field.setAttribute('aria-invalid', is_valid ? 'false' : 'true');
field.setAttribute('aria-required', 'true');
field.setAttribute('aria-describedby', error_container_id);

// For error containers
error_container.setAttribute('role', 'alert');
error_container.setAttribute('aria-live', 'polite');
```

**Reference**: `specs/claude-skills/analysis/patterns.md` (Accessibility Patterns)

---

### 9. Comments Explaining "What" Not "Why" (Rule 3.2)
**Frequency**: Medium-Low
**Severity**: P2 - WARNING
**Category**: Commenting

**Issue**: Comments narrate what code does instead of explaining why

**Why This Happens**:
- Commenting habit from learning phase
- Misunderstanding the purpose of comments

**Incorrect Examples**:
```javascript
// ❌ WRONG - Narrates what code does
// Set price to price times 100
const price_cents = price * 100;

// ❌ WRONG - Obvious from code
// Loop through items
for (const item of items) {
  // Call setup function
  setup_item(item);
}

// ❌ WRONG - Redundant
// Check if user is active
if (user.is_active) { ... }
```

**Correct Examples**:
```javascript
// ✅ CORRECT - Explains why (avoid floating point errors)
const price_cents = price * 100;

// ✅ CORRECT - Explains platform constraint
// Webflow duplicates IDs in collection lists - use classes instead
const items = document.querySelectorAll('.item');

// ✅ CORRECT - Explains technical decision
// Debounce input to avoid overwhelming API (180ms recommended by Codex)
const on_input = debounce(handle_input, 180);

// ✅ CORRECT - Explains workaround
// IntersectionObserver not supported in IE11 - use viewport check fallback
if ('IntersectionObserver' in window) {
  use_intersection_observer();
} else {
  use_scroll_listener();
}
```

**Reference**: `knowledge/code_standards.md:80-96`

---

### 10. No Try-Catch for External API Calls (Rule 8.1)
**Frequency**: Low
**Severity**: P2 - WARNING
**Category**: Error Handling

**Issue**: External API calls (fetch, third-party SDKs) lack error handling

**Why This Happens**:
- Assuming API calls always succeed
- Forgetting edge cases (network failures, timeouts, rate limits)

**Incorrect Example**:
```javascript
// ❌ WRONG - No error handling
async function submit_form(data) {
  const response = await fetch('/api/submit', {
    method: 'POST',
    body: JSON.stringify(data)
  });
  const result = await response.json();
  show_success(result);
}
```

**Correct Example**:
```javascript
// ✅ CORRECT - Comprehensive error handling
async function submit_form(data) {
  try {
    const response = await fetch('/api/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const result = await response.json();
    show_success(result);

  } catch (error) {
    console.error('[FormSubmit] API error:', error);
    show_error('Submission failed. Please try again.');

    // Optional: Report to error tracking service
    if (window.Sentry) {
      Sentry.captureException(error);
    }
  }
}
```

**Graceful Degradation Pattern**:
```javascript
// ✅ CORRECT - Feature works even if external service fails
function enhance_with_analytics() {
  try {
    if (window.gtag) {
      gtag('event', 'page_view', { page_path: window.location.pathname });
    }
  } catch (error) {
    console.warn('[Analytics] Failed to track event:', error);
    // Core functionality continues regardless
  }
}
```

**Reference**: `specs/004-claude-skills/analysis/validation-rules.md` (Rule 8.1-8.3)

---

### Additional: Incorrect Class Naming (Rule 1.11)
**Frequency**: Medium
**Severity**: P0 - ERROR (BLOCKING)
**Category**: Naming Conventions

**Issue**: Class names not using PascalCase (e.g., underscores, hyphens, or starting lowercase)

**Why This Happens**:
- Mixing class and function naming conventions
- Copying class-like utilities from non-ES6 code
- Overusing underscores/hyphens from CSS naming in JS

**Incorrect Examples**:
```javascript
// ❌ WRONG - snake_case class name
class form_validator {}

// ❌ WRONG - hyphenated class name
class hero-video {}

// ❌ WRONG - lowercase start
class usermodel {}
```

**Correct Examples**:
```javascript
// ✅ CORRECT - PascalCase class names
class FormValidator {}
class HeroVideo {}
class UserModel {}
```

**Quick Fix Strategy**:
1. Rename class to start with uppercase and remove underscores/hyphens
2. Ensure exported/imported identifiers are updated accordingly
3. Re-run validator to confirm compliance

**Reference**: `knowledge/code_standards.md:14`

---

## Quick Reference: Violation Severity

| Severity | Impact | Action Required |
|----------|--------|-----------------|
| P0 ERROR | Breaks functionality or violates critical standards | MUST FIX before production |
| P1 ERROR | Platform compatibility issues, integration failures | SHOULD FIX before production |
| P2 WARNING | Code quality, accessibility, maintainability | Recommended to fix |
| P3 INFO | Best practices, optimization opportunities | Consider addressing |

---

## Validation Checklist

Before committing code, verify:
- [ ] Webflow initialization pattern present (Rule 4.1)
- [ ] All naming follows snake_case/kebab-case/UPPER_SNAKE_CASE/PascalCase (Rules 1.1–1.11)
- [ ] File header is exactly 3 lines (Rule 2.1)
- [ ] Comment density ≤ 5 per 10 lines (Rule 3.1)
- [ ] No ID selectors in collection context (Rule 5.1)
- [ ] Collection async rendering handled (Rule 5.2)
- [ ] External library availability checks present (Rules 6.1-6.3)
- [ ] ARIA attributes on interactive elements (Rules 7.1-7.3)
- [ ] Error handling for external API calls (Rule 8.1)

---

## References

- **Complete Rule Catalog**: `references/validation-rules.md`
- **Code Standards**: `knowledge/code_standards.md`
- **Initialization Pattern**: `knowledge/initialization_pattern.md`
- **Platform Constraints**: `knowledge/webflow_platform_constraints.md`
- **Pattern Analysis**: `specs/004-claude-skills/analysis/patterns.md`

---

**End of Common Violations Reference**
