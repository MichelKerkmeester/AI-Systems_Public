# Comment Auto-Fix Examples

## What `--fix` Does

The `python3 .claude/logic/validation/validate-comments.py --fix` command automatically corrects comment formatting issues based on patterns defined in `/knowledge/patterns.json`.

## Examples of Auto-Fixes

### 1. JavaScript Inline Comments
**Before:**
```javascript
// this is a bad comment
// another bad comment
// TODO fix this later
```

**After `--fix`:**
```javascript
// NOTE: This is a bad comment
// NOTE: Another bad comment
// TODO: Fix this later
```

### 2. File Headers
**Before:**
```javascript
// Navigation Component
const nav = document.querySelector('.nav');
```

**After `--fix`:**
```javascript
// ─────────────────────────────────────────────────────────────────
// Navigation Component
// ─────────────────────────────────────────────────────────────────
const nav = document.querySelector('.nav');
```

### 3. Section Dividers
**Before:**
```javascript
// Initialization
function init() { }

// Event Handlers
function handleClick() { }
```

**After `--fix`:**
```javascript
/* ─── Initialization ──────────────────────────────────────────── */
function init() { }

/* ─── Event Handlers ──────────────────────────────────────────── */
function handleClick() { }
```

### 4. CSS Comments
**Before:**
```css
/* navigation styles */
.nav { }

/* button styles */
.btn { }
```

**After `--fix`:**
```css
/* ─────────────────────────────────────────────────────────────── */
/* NAVIGATION STYLES                                                */
/* ─────────────────────────────────────────────────────────────── */
.nav { }

/* ─── BUTTON STYLES ───────────────────────────────────────────── */
.btn { }
```

## Rules Applied

1. **Inline comments** must start with:
   - Uppercase letter (transforms to sentence case)
   - OR prefix: `TODO:`, `NOTE:`, `FIXME:`, `HACK:`, `WARNING:`, `ERROR:`, `IMPORTANT:`

2. **File headers** get full divider lines (65 dashes for JS, 63 for CSS)

3. **Section comments** get formatted dividers with title

4. **Consistency** across entire codebase

## Usage

```bash
# Check only (no changes)
python3 .claude/logic/validation/validate-comments.py src/

# Auto-fix all issues
python3 .claude/logic/validation/validate-comments.py --fix src/

# Fix specific file
python3 .claude/logic/validation/validate-comments.py --fix src/components/nav.js
```

## When NOT to Use --fix

- When comments contain code examples (might break formatting)
- When special formatting is intentional
- In third-party or vendor files

The `--fix` flag saves time by automatically applying consistent comment formatting across the codebase without manual edits.