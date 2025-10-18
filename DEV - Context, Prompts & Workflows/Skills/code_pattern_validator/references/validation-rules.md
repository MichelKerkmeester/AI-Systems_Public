# Code Standards Validation Rules

**Purpose**: Comprehensive catalog of enforceable rules for validating JavaScript code against project standards
**Sources**:
- `knowledge/code_standards.md`
- `knowledge/initialization_pattern.md`
- `knowledge/webflow_platform_constraints.md`

**Analysis Date**: 2025-10-18

---

## Rule Categories

### Category 1: Naming Conventions

#### Rule 1.1: Function Names (snake_case)
**Severity**: ERROR
**Pattern**: `^[a-z][a-z0-9_]*$`
**Description**: All function names must use snake_case
**Examples**:
- ✅ `get_data()`, `handle_submit()`, `init_component()`
- ❌ `getData()`, `handleSubmit()`, `initComponent()`

**Detection**: Flag identifiers that introduce uppercase characters after the first letter
```javascript
// Function declarations (export optional):
// Regex: /\bfunction\s+([a-z0-9_]*[A-Z][a-zA-Z0-9_]*)\s*\(/

// Variables assigned arrow functions (const/let/var), async optional:
// Regex: /\b(?:const|let|var)\s+([a-z0-9_]*[A-Z][a-zA-Z0-9_]*)\s*=\s*(?:async\s*)?\(/

// Variables assigned function expressions (const/let/var), async optional:
// Regex: /\b(?:const|let|var)\s+([a-z0-9_]*[A-Z][a-zA-Z0-9_]*)\s*=\s*(?:async\s*)?function\b/
```

#### Rule 1.2: Variable Names (snake_case)
**Severity**: ERROR
**Pattern**: `^[a-z][a-z0-9_]*$`
**Description**: All variable names must use snake_case
**Examples**:
- ✅ `user_name`, `form_data`, `is_active`
- ❌ `userName`, `formData`, `isActive`

**Detection**: Flag camelCase variable identifiers in declarations, excluding constants
```javascript
// Any const/let/var with uppercase (but not ALLCAPS constants):
// Regex: /\b(?:const|let|var)\s+(?![A-Z0-9_]+\b)([a-zA-Z0-9_]*[A-Z][a-zA-Z0-9_]*)/ 
```

#### Rule 1.3: Constants (UPPER_SNAKE_CASE)
**Severity**: ERROR
**Pattern**: `^[A-Z][A-Z0-9_]*$`
**Description**: Constants must use UPPER_SNAKE_CASE
**Examples**:
- ✅ `MAX_SIZE`, `API_ENDPOINT`, `INIT_DELAY_MS`
- ❌ `maxSize`, `apiEndpoint`, `initDelayMs`

**Detection**: Scan const declarations that are primitives or frozen objects

#### Rule 1.4: Private Members (_snake_case)
**Severity**: WARNING
**Pattern**: `^_[a-z][a-z0-9_]*$`
**Description**: Private/internal members should start with underscore
**Examples**:
- ✅ `_internal_state`, `_cache`, `_helper_method`
- ❌ `_internalState`, `internalState` (if private)

#### Rule 1.5: Boolean Variables (is_/has_/can_ prefix)
**Severity**: WARNING
**Pattern**: `^(is|has|can)_[a-z][a-z0-9_]*$`
**Description**: Boolean variables should use descriptive prefixes
**Examples**:
- ✅ `is_active`, `has_data`, `can_submit`
- ❌ `active`, `data`, `submit`

#### Rule 1.6: Event Handlers (handle_ prefix)
**Severity**: WARNING
**Pattern**: `^handle_[a-z][a-z0-9_]*$`
**Description**: Event handler functions should use handle_ prefix
**Examples**:
- ✅ `handle_click`, `handle_submit`, `handle_keydown`
- ❌ `onClick`, `onSubmit`, `keydownHandler`

#### Rule 1.7: Callbacks (on_ prefix)
**Severity**: WARNING
**Pattern**: `^on_[a-z][a-z0-9_]*$`
**Description**: Callback functions should use on_ prefix
**Examples**:
- ✅ `on_success`, `on_error`, `on_complete`
- ❌ `success`, `error`, `complete`

#### Rule 1.8: CSS Classes (kebab-case)
**Severity**: ERROR
**Pattern**: `^[a-z][a-z0-9-]*$`
**Description**: CSS class names must use kebab-case
**Examples**:
- ✅ `.card`, `.navigation`, `.hero--section`
- ❌ `.cardItem`, `.Navigation`, `.hero_section`

#### Rule 1.9: BEM Modifiers (-- separator)
**Severity**: WARNING
**Pattern**: `^[a-z][a-z0-9-]*--[a-z][a-z0-9-]*$`
**Description**: BEM modifiers should use -- separator
**Examples**:
- ✅ `.nav--item`, `.card--featured-large`
- ❌ `.nav-item`, `.card_featured_large`

#### Rule 1.10: File Names (snake_case)
**Severity**: ERROR
**Pattern**: `^[a-z][a-z0-9_]*\.js$`
**Description**: JavaScript file names must use snake_case
**Examples**:
- ✅ `form_validator.js`, `modal_welcome.js`
- ❌ `formValidator.js`, `modalWelcome.js`

---

#### Rule 1.11: Class Names (PascalCase)
**Severity**: ERROR
**Pattern**: `^[A-Z][a-zA-Z0-9]*$`
**Description**: Class names must use PascalCase (first letter uppercase, no underscores or hyphens)
**Examples**:
- ✅ `UserModel`, `FormValidator`, `HeroVideo`
- ❌ `user_model`, `form_validator`, `hero-video`, `hero_video`, `usermodel`

**Detection**: Flag class declarations that do not use PascalCase
```javascript
// Class declarations (ES6):
// Regex (invalid class name): /\bclass\s+([a-z][a-zA-Z0-9_\-]*)\b/

// Optional: also flag underscores or hyphens in class names:
// Regex: /\bclass\s+([A-Za-z0-9]*[_-][A-Za-z0-9_-]*)\b/
```

---

### Category 2: File Headers

#### Rule 2.1: Exactly 3 Lines
**Severity**: ERROR
**Description**: File headers must be exactly 3 lines
**Template**:
```javascript
// ───────────────────────────────────────────────────────────────
// COMPONENT: NAME
// ───────────────────────────────────────────────────────────────
```

**Detection**: Check first 3 lines of file
```javascript
// Heuristic approach (illustrative):
// 1) First line matches separator (dashes)
// 2) Second line matches `// [A-Z]+: ` pattern (category, colon, name)
// 3) Third line matches separator (dashes)
// 4) Fourth line is NOT a comment starting with `//` (to avoid extra header lines)
```

#### Rule 2.2: No Metadata
**Severity**: ERROR
**Description**: Headers must not contain metadata (authors, dates, tickets, versions)
**Forbidden Content**:
- Author names
- Dates
- Task/ticket IDs (e.g., PROJ-123)
- Version numbers
- Descriptive paragraphs

**Detection**: Scan first 10 lines for patterns like:
- `@author`, `Author:`
- `@date`, `Date:`, date patterns (`2024-01-15`)
- `PROJ-`, `TASK-`, `#[0-9]+`
- `@version`, `v1.0.0`

#### Rule 2.3: Section Headers (Numbered)
**Severity**: WARNING
**Description**: Section headers should be numbered and follow format
**Template**:
```javascript
/* ─────────────────────────────────────────────────────────────
   1. SECTION NAME
──────────────────────────────────────────────────────────────── */
```

---

### Category 3: Commenting Rules

#### Rule 3.1: Maximum Density
**Severity**: WARNING
**Description**: Maximum 5 comments per 10 lines of code
**Calculation**: Count comment lines, divide by total lines, multiply by 10
**Threshold**: ≤ 5.0

**Detection**: Count lines matching:
- `//` (single-line comments)
- `/* ... */` (multi-line comments, count all lines)
- Exclude file headers and section headers

**How Claude Applies This Rule**:
1. Count total lines in file (including blank lines)
2. Count comment lines:
   - Lines starting with `//` (trim whitespace first)
   - Lines within `/* ... */` blocks (count opening line through closing line)
3. Exclude from count:
   - Lines 1-3 (file header)
   - Section headers matching `/* ───... 1. SECTION ... ───... */`
4. Calculate: `(comment_lines / total_lines) * 10`
5. Flag as WARNING if result > 5.0
6. In report, specify: "X comments in Y lines (Z comments per 10 lines)"

#### Rule 3.2: Explain "Why" Not "What"
**Severity**: WARNING
**Description**: Comments should explain intent/rationale, not narrate code
**Anti-Patterns**:
```javascript
// ❌ Set price to price times 100
const price_cents = price * 100;

// ❌ Loop through items
for (const item of items) {}
```

**Good Examples**:
```javascript
// ✅ Convert to cents to avoid floating point errors
const price_cents = price * 100;

// ✅ Webflow duplicates IDs in collection lists - use class selector
const elements = document.querySelectorAll('.card');
```

**Detection**: Flag comments that:
- Start with action verbs without context (Set, Loop, Call, Add)
- Directly describe the next line's operation

**How Claude Applies This Rule**:
1. Read each comment with the line(s) of code it precedes
2. Check if comment matches narration patterns:
   - Starts with action verbs: "Set", "Get", "Loop", "Call", "Add", "Remove", "Update", "Create", "Delete", "Check", "Return"
   - Can be inferred directly from reading the code (e.g., "Loop through items" before `for` loop)
   - Simply restates variable/function names (e.g., "Get data" before `get_data()`)
3. Flag as WARNING if comment appears to narrate rather than explain
4. In report, suggest: "Explain WHY this approach was chosen, not WHAT the code does"
5. Provide context-aware suggestion when possible (e.g., "Explain why this workaround is needed")

#### Rule 3.3: No Commented-Out Code
**Severity**: WARNING
**Description**: Remove commented-out code instead of leaving it
**Detection**: Multi-line comments containing code patterns:
- Variable declarations: `// const`, `// let`, `// var`
- Function calls: `// function_name(`
- Control flow: `// if (`, `// for (`, `// while (`

#### Rule 3.4: TODO Without Context
**Severity**: WARNING
**Description**: TODO comments must include context or be removed
**Anti-Pattern**: `// TODO: fix this`
**Good Pattern**: `// TODO: Implement retry logic for rate limiting (PROJ-123)`

**Detection**: Flag `// TODO` without explanatory text

---

### Category 4: Initialization Pattern

#### Rule 4.1: Mandatory Pattern Usage
**Severity**: ERROR
**Description**: All files must use the Webflow initialization pattern
**Required Pattern**:
```javascript
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init_function);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init_function);
} else {
  init_function();
}
```

**Detection**:
1. Search for `window.Webflow.push` (should exist)
2. Verify `else if` pattern (NOT separate `if` statements)
3. Check for all three branches

**How Claude Applies This Rule**:
1. Search entire file for `window.Webflow.push` or `window.Webflow?.push`
2. If NOT found → **ERROR** (missing pattern entirely)
3. If found, verify structure:
   - Line must be within an `if (window.Webflow` conditional
   - Must have `else if (document.readyState === 'loading')` branch
   - Must have final `else` branch that calls init function directly
   - All three branches should reference the same init function name
4. Common violations to flag:
   - Separate `if` statements instead of `if...else if...else` chain
   - Missing any of the three branches
   - Direct `DOMContentLoaded` listener without Webflow check
5. In report, provide exact line numbers where pattern starts or note "Pattern not found"

#### Rule 4.2: IIFE Wrapper
**Severity**: WARNING
**Description**: Code should be wrapped in IIFE to avoid global pollution
**Pattern**:
```javascript
(() => {
  // Component code
})();
```

**Detection**: Check file starts with `(() => {` or `(function() {`

#### Rule 4.3: No Direct DOMContentLoaded
**Severity**: ERROR
**Description**: Never use direct DOMContentLoaded without Webflow.push check
**Anti-Pattern**:
```javascript
// ❌ WRONG
document.addEventListener('DOMContentLoaded', init);
```

**Detection**: Flag `DOMContentLoaded` without preceding Webflow.push check

#### Rule 4.4: No jQuery Ready
**Severity**: ERROR
**Description**: Do not use jQuery ready pattern
**Anti-Pattern**: `$(document).ready(function() { ... });`

**Detection**:
```javascript
// Document ready long-form:
// Regex: /\$\(document\)\.ready\(/ 

// Shorthand ready handler:
// Regex: /\$\s*\(\s*function\s*\(/ 
```

**Detection**: Search for `$(document).ready` or `jQuery(document).ready`

#### Rule 4.5: No window.onload
**Severity**: ERROR
**Description**: Do not use window.onload (overwrites other handlers)
**Anti-Pattern**: `window.onload = function() { ... };`

**Detection**: Search for `window.onload =`

---

### Category 5: Webflow Platform Constraints

#### Rule 5.1: No ID Selectors in Collections
**Severity**: ERROR
**Description**: Never use getElementById or #id selectors within collection lists
**Reason**: Webflow duplicates IDs across collection items
**Detection**:
- `getElementById(` inside functions handling collections
- `querySelector('#` inside collection-related code
- Check proximity to `.w-dyn-item`, `.w-dyn-list`

**Correct Approach**:
```javascript
// ✅ Use classes or data attributes
document.querySelectorAll('.action-button')
```

**How Claude Applies This Rule**:
1. Scan file for collection-related indicators:
   - Strings: `.w-dyn-item`, `.w-dyn-list`, `w-dyn-items`, `collection`
   - Comments mentioning "collection" or "CMS"
2. If file handles collections, scan for ID selector usage:
   - `getElementById(`
   - `querySelector('#` or `querySelectorAll('#`
   - `$('#` (jQuery)
3. Flag as **ERROR** if ID selectors found in collection context
4. Context determination:
   - Within 20 lines of collection-related code → definitely related
   - In same function as collection handling → related
   - General utility function → may not be related (use judgment)
5. In report, specify line number and suggest class-based alternative

#### Rule 5.2: Collection Timing Awareness
**Severity**: WARNING
**Description**: Handle async collection rendering with delays or observers
**Required Pattern**: One of:
- `setTimeout(init_items, 500)`
- Retry pattern with decreasing attempts
- MutationObserver

**Detection**: Files mentioning `.w-dyn-item` or `.w-dyn-list` should include timing handling

**How Claude Applies This Rule**:
1. Determine if file handles collections (see Rule 5.1 detection)
2. If yes, scan for timing/async patterns:
   - `setTimeout(` with 300-1000ms delays
   - Retry logic: loops with `attempts--` or similar
   - `MutationObserver` instantiation
   - `requestAnimationFrame` polling
3. Flag as **WARNING** if collection handling found WITHOUT timing consideration
4. Exception: If code runs on user interaction (click handler), timing may not be needed
5. In report, suggest appropriate timing pattern based on use case

#### Rule 5.3: Event Delegation for Collections
**Severity**: WARNING
**Description**: Use event delegation for dynamic collection items
**Pattern**:
```javascript
document.addEventListener('click', (e) => {
  if (e.target.matches('.action-button')) handler(e);
});
```

**Detection**: Check event listeners in collection-related code use delegation

**How Claude Applies This Rule**:
1. Find collection-related code (see Rule 5.1)
2. Scan for event listener patterns:
   - **Good (delegation)**: `document.addEventListener(` or `parent.addEventListener(` with `e.target` checks
   - **Bad (direct)**: `item.addEventListener(` or `button.addEventListener(` on collection items
3. Look for delegation patterns:
   - `e.target.matches(selector)`
   - `e.target.closest(selector)`
   - Manual class/attribute checking on event.target
4. Flag as **WARNING** if direct listeners attached to elements within `.w-dyn-item`
5. Exception: Global singleton elements (outside collections) can use direct listeners
6. In report, show which line uses direct listener and suggest delegation pattern

#### Rule 5.4: No function.name Reliance
**Severity**: ERROR
**Description**: Never rely on function.name (minification breaks it)
**Detection**: Search for `.name` property access on functions

#### Rule 5.5: Collection Limit Awareness
**Severity**: INFO
**Description**: Code should be aware of collection limits
**Limits**:
- 100 items per list
- 40 lists per page
- 10 nested lists per page

**Detection**: Check if code handling many items has safeguards

---

### Category 6: External Integrations

#### Rule 6.1: Motion.dev Availability Check
**Severity**: ERROR
**Description**: Always check Motion.dev availability before use
**Pattern**:
```javascript
if (window.Motion?.animate) {
  // Use Motion.dev
} else {
  // Fallback
}
```

**Detection**: Flag `Motion.animate(` without availability check

#### Rule 6.2: Lenis Availability Check
**Severity**: ERROR
**Description**: Always check Lenis availability before use
**Pattern**:
```javascript
if (window.lenis?.stop) {
  window.lenis.stop();
}
```

**Detection**: Flag `window.lenis.` without optional chaining or existence check

#### Rule 6.3: Third-Party Library Defensive Loading
**Severity**: WARNING
**Description**: Include fallbacks for CDN-loaded libraries
**Libraries**: Botpoison, HLS.js, Swiper, etc.

**Detection**: Check for try-catch or availability checks around library usage

---

### Category 7: Accessibility

#### Rule 7.1: ARIA Attributes on Interactive Elements
**Severity**: WARNING
**Description**: Interactive elements should have appropriate ARIA attributes
**Required**:
- `aria-invalid` on form fields
- `aria-required` on required fields
- `aria-describedby` for error messages
- `role="alert"` for error containers
- `aria-live` for dynamic content

**Detection**: Check form/modal/interactive elements for ARIA attributes

**How Claude Applies This Rule**:
1. Identify interactive element types in file:
   - **Forms**: `querySelector('form')`, `querySelector('input')`, validation code
   - **Modals**: `.modal`, `.dialog`, strings like "modal", "dialog", "popup"
   - **Dynamic content**: DOM manipulation, `innerHTML =`, `textContent =`
2. For each type, check for appropriate ARIA:
   - **Forms**: Look for `setAttribute('aria-invalid'`, `aria-required`, `aria-describedby`
   - **Modals**: Look for `aria-label`, `aria-modal`, `aria-describedby`, `role="dialog"`
   - **Dynamic content**: Look for `aria-live` or `role="alert"`
3. Flag as **WARNING** if element type found but no ARIA attributes set
4. In report, specify which element type and which ARIA attributes are missing
5. Reference existing patterns from specs/004-claude-skills/analysis/patterns.md if available

#### Rule 7.2: Focus Management
**Severity**: WARNING
**Description**: Modals/dialogs should manage focus properly
**Required**:
- Store `document.activeElement` before opening
- Focus first interactive element on open
- Restore focus on close

**Detection**: Modal open/close functions should include focus management

**How Claude Applies This Rule**:
1. Identify modal-related functions (names containing "open", "close", "show", "hide" + "modal"/"dialog")
2. In open/show functions, check for:
   - Storage: `const previous_focus = document.activeElement` or similar
   - Focus setting: `.focus()` called on modal element or first focusable child
3. In close/hide functions, check for:
   - Focus restoration: `previous_focus.focus()` or stored element focus
4. Flag as **WARNING** if modal functions found without focus management
5. In report, specify which functions lack focus management and provide pattern example

#### Rule 7.3: Keyboard Navigation
**Severity**: WARNING
**Description**: Interactive elements should support keyboard navigation
**Required**:
- Escape key closes modals
- Enter/Space activates buttons
- Tab navigation works

**Detection**: Check for keyboard event handlers on interactive components

**How Claude Applies This Rule**:
1. Identify interactive components (modals, custom buttons, forms)
2. Check for keyboard event listeners:
   - `addEventListener('keydown'` or `addEventListener('keyup'`
   - Event handler checking `e.key`, `e.code`, or `e.which`
3. For modals specifically, verify Escape key handling:
   - Check for `e.key === 'Escape'` or `e.code === 'Escape'` or `e.which === 27`
4. Flag as **WARNING** if modal found without Escape key handler
5. **INFO** suggestion if other interactive elements lack keyboard support
6. In report, specify which keyboard interactions are missing

---

### Category 8: Error Handling

#### Rule 8.1: Try-Catch for External APIs
**Severity**: WARNING
**Description**: Wrap external API calls in try-catch
**Examples**: fetch(), third-party SDK calls

**Detection**: Flag fetch() without surrounding try-catch

**How Claude Applies This Rule**:
1. Scan for external API calls:
   - `fetch(` calls
   - `XMLHttpRequest`
   - Third-party library method calls (check for library names)
   - `video.play()`, `audio.play()` (can throw)
2. For each call found, check if it's within try-catch:
   - Look backward from call to find `try {`
   - Verify closing `} catch` exists after the call
   - Check if function is declared `async` and uses `await` (requires try-catch)
3. Flag as **WARNING** if API call not in try-catch
4. Exception: Calls with `.catch()` method chaining (promises) are acceptable
5. In report, specify line number of unprotected call and suggest try-catch pattern

#### Rule 8.2: Graceful Degradation
**Severity**: WARNING
**Description**: Features should degrade gracefully when dependencies fail
**Pattern**:
```javascript
if (feature_available) {
  // Enhanced experience
} else {
  // Basic experience
}
```

#### Rule 8.3: Console Errors for Failures
**Severity**: INFO
**Description**: Log meaningful errors to console
**Pattern**: `console.error('[Component] Error:', error)`

---

## Validation Priority Matrix

| Priority | Severity | Category | Rule Count | Impact |
|----------|----------|----------|------------|--------|
| P0 | ERROR | Initialization Pattern | 5 | Breaks functionality |
| P0 | ERROR | Naming Conventions | 4 | Code consistency |
| P0 | ERROR | File Headers | 2 | Standards compliance |
| P1 | ERROR | Platform Constraints | 5 | Webflow compatibility |
| P1 | ERROR | External Integrations | 2 | Runtime failures |
| P2 | WARNING | Commenting | 4 | Code quality |
| P2 | WARNING | Accessibility | 3 | User experience |
| P2 | WARNING | Error Handling | 3 | Reliability |
| P3 | INFO | Documentation | Various | Maintainability |

---

## Implementation Guidance for Validator

### Quick Validation Checks (< 1 second)
1. File header format (Rule 2.1, 2.2)
2. Initialization pattern presence (Rule 4.1)
3. Naming convention scan (Rule 1.1-1.10)
4. Comment density (Rule 3.1)

### Standard Validation (< 5 seconds)
- All Quick checks
- Platform constraint checks (Rule 5.1-5.5)
- ARIA attribute presence (Rule 7.1-7.3)
- External integration safety (Rule 6.1-6.3)

### Comprehensive Validation (< 15 seconds)
- All Standard checks
- Comment quality analysis (Rule 3.2-3.4)
- Error handling coverage (Rule 8.1-8.3)
- Cross-reference with patterns.md

---

## Validation Report Format

```markdown
# Validation Report: [filename]

**File**: /path/to/file.js
**Date**: [timestamp]
**Validation Level**: [Quick/Standard/Comprehensive]

## Summary
- **Compliance Score**: 85%
- **Errors**: 2
- **Warnings**: 5
- **Info**: 3

## Errors

### ERROR: Missing Initialization Pattern (Rule 4.1)
**Line**: N/A
**Issue**: File does not use required Webflow.push initialization pattern
**Fix**: Add the following pattern at the end of your file:
```javascript
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init_function);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init_function);
} else {
  init_function();
}
```

### ERROR: Naming Convention Violation (Rule 1.1)
**Line**: 42
**Issue**: Function name `getData` uses camelCase instead of snake_case
**Fix**: Rename to `get_data`

## Warnings
[Similar format]

## Info
[Similar format]

## Recommendations
1. Review code_standards.md for naming conventions
2. Consider adding ARIA attributes for accessibility
3. Add error handling for external API calls
```

---

## References

- **Source**: `knowledge/code_standards.md`
- **Source**: `knowledge/initialization_pattern.md`
- **Source**: `knowledge/webflow_platform_constraints.md`
- **Pattern Catalog**: `specs/claude-skills/analysis/patterns.md`

---

**End of Validation Rules Document**
