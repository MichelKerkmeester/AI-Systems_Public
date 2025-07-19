# /test - Unified Testing & Validation

## Purpose
Comprehensive validation for Webflow projects with auto-fixing capabilities.

## Usage
- `/test` - Interactive mode
- `/test [mode]` - Direct mode selection
- `/t` - Short alias

## Modes
- **quick** - 5-minute essentials scan
- **full** - 15-minute comprehensive audit
- **security** - Security-focused validation
- **performance** - Performance analysis
- **fix** - Generate fixes for found issues

## Quick Access
- `/test-quick` or `/tq`
- `/test-full` or `/tf`
- `/test-security` or `/ts`
- `/test-performance` or `/tp`

## Validation Rules
### Auto-Enforced
- ❌ No DOM manipulation
- ❌ No pixels (auto-converts to REM)
- ❌ No generic selectors
- ❌ No console.log in production
- ❌ No DOMContentLoaded (Slater autoloads)

### Required Patterns
- ✅ Data attributes for selectors
- ✅ Element existence checks
- ✅ Webflow.push() for dependencies
- ✅ Respect prefers-reduced-motion
- ✅ Module pattern usage

## Behavior
1. Scan codebase based on selected mode
2. Apply validation rules from constraints.json
3. Auto-fix violations where possible
4. Generate report with remaining issues
5. Suggest manual fixes for complex problems