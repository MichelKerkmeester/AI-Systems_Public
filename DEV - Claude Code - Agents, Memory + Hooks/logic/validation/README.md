# Validation Scripts

This directory contains validation scripts for enforcing code standards and compliance checks.

## Scripts

### 1. validate-comments.py

Validates comment patterns in JavaScript and CSS files according to project standards.

**Features:**
- Checks for proper file headers in JS and CSS
- Validates section comment formatting
- Ensures inline comments follow conventions
- Detects forbidden patterns (console.log, pixel units, global variables)
- Auto-fix capability for common issues

**Usage:**
```bash
# Check all files in src directory
python3 .claude/logic/validation/validate-comments.py

# Check specific directory
python3 .claude/logic/validation/validate-comments.py src/C__components

# Auto-fix violations where possible
python3 .claude/logic/validation/validate-comments.py --fix

# Custom file pattern
python3 .claude/logic/validation/validate-comments.py --pattern "**/button/*.js"
```

**Comment Standards:**

**JavaScript:**
```javascript
// ───────────────────────────────────────────────────────────────
// Component Name
// Brief description
// ───────────────────────────────────────────────────────────────

/* ─────────────────────────────────────────────────────────────
   Section Name
  ───────────────────────────────────────────────────────────── */

// TODO: Task description
// NOTE: Important information
// FIXME: Issue to fix
```

**CSS:**
```css
/* ───────────────────────────────────────────────────────────────
   Component: Name
   ─────────────────────────────────────────────────────────────── */

/* SECTION NAME */
/* Section Name */
```

### 2. check-slater-compliance.py

Checks JavaScript files for Slater framework compliance and initialization patterns.

**Features:**
- Detects DOMContentLoaded usage (not needed with Slater)
- Finds jQuery ready patterns (should be removed)
- Validates proper initialization patterns
- Checks for console.log statements
- Generates migration guides

**Usage:**
```bash
# Check all JS files in src
python3 .claude/logic/validation/check-slater-compliance.py

# Check specific file or directory
python3 .claude/logic/validation/check-slater-compliance.py src/C__components/navigation/

# Generate migration guide
python3 .claude/logic/validation/check-slater-compliance.py --guide

# Exclude additional paths
python3 .claude/logic/validation/check-slater-compliance.py --exclude vendor libs
```

**Slater Compliance Rules:**
1. **No DOMContentLoaded** - Slater auto-loads scripts after DOM ready
2. **No jQuery ready** - Not needed with Slater
3. **Use IIFE pattern** - Wrap code in immediately invoked functions
4. **Element checks** - Always check element existence before use
5. **No console.log** - Remove in production code

**Proper Patterns:**
```javascript
// ✅ IIFE Pattern
(() => {
  const element = document.querySelector('.my-element');
  if (!element) return;
  
  // Initialize immediately (Slater auto-loads)
})();

// ✅ Namespace Pattern
window.MyApp = window.MyApp || {};
window.MyApp.init = function() {
  // Your code
};
```

## Integration with Hooks

These validation scripts can be integrated with the existing hook system:

1. **Pre-commit validation** - Run before committing changes
2. **Quality checks** - Part of quality-hook.py workflow
3. **CI/CD pipeline** - Automated compliance checks

## Exit Codes

Both scripts follow standard exit codes:
- `0` - All validations passed
- `1` - Validation failures found

This allows integration with shell scripts and CI/CD pipelines:

```bash
# Example: Run both validations
python3 .claude/logic/validation/validate-comments.py && \
python3 .claude/logic/validation/check-slater-compliance.py
```

## Exclusions

Both scripts automatically exclude:
- `node_modules/`
- `vendor/`
- `dist/`
- `build/`
- `.min.js` files
- Test files

The Slater compliance checker specifically excludes:
- `/src/B__global/global.html` (Slater loader)