# Quality Hook

## Overview

**Hook Name**: Quality Hook  
**Purpose**: Enforces code quality standards and best practices  
**Location**: `/hooks/quality/quality-hook.py`  
**Triggers**: UserPromptSubmit, PostToolUse (Edit/Write operations)  
**Priority**: 2 (Quality enforcement)  
**Performance**: ~10ms typical execution time

## Description

The Quality Hook monitors code changes and user prompts to enforce project-specific quality standards. It provides warnings for quality issues and can block critical violations, ensuring consistent code quality throughout the development process.

## Configuration

Settings managed in hook configuration:

```python
Quality Rules:
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- Consistent naming conventions
- File size limits (<500 lines)
- Function complexity limits
- Required documentation
```

## How It Works

1. **Prompt Analysis**:
   - Detects quality-related keywords
   - Identifies potential anti-patterns
   - Checks against project standards

2. **Code Inspection**:
   - Monitors file modifications
   - Validates against rules
   - Calculates complexity metrics

3. **Enforcement Levels**:
   - **Info**: Best practice suggestions
   - **Warning**: Quality concerns
   - **Error**: Blocking violations

4. **Feedback Delivery**:
   - Clear, actionable messages
   - Suggested improvements
   - Links to documentation

## Quality Checks

### Code Structure
```python
checks = {
    "file_length": 500,          # Max lines per file
    "function_length": 50,       # Max lines per function
    "cyclomatic_complexity": 10, # Max complexity score
    "nesting_depth": 4,         # Max nesting levels
    "line_length": 100          # Max characters per line
}
```

### Naming Conventions
```python
patterns = {
    "functions": "camelCase",
    "classes": "PascalCase",
    "constants": "UPPER_SNAKE_CASE",
    "files": "kebab-case",
    "css_classes": "kebab-case",
    "data_attributes": "data-*"
}
```

### Project-Specific Rules
```python
webflow_rules = {
    "no_dom_manipulation": "Use data attributes only",
    "rem_units_only": "No pixel values in CSS",
    "no_console_logs": "Remove all console statements",
    "namespace_required": "All JS must be namespaced"
}
```

## Example Usage

### Quality Warning
```javascript
User writes: console.log("Debug info");

⚠️ Code Quality Warning

Detected: Console statement in production code
File: components/hero.js
Line: 45

Project Rule: No console.log statements
Reason: Performance and security

Suggested Fix:
// Remove or use conditional logging
if (DEBUG_MODE) {
  console.log("Debug info");
}
```

### Blocking Violation
```css
User writes: .hero { margin-top: 24px; }

❌ Quality Check Failed

Violation: Pixel units used
File: styles/hero.css
Line: 12

Project Requirement: Use REM units only
Current: 24px
Suggested: 1.5rem (24px ÷ 16px base)

This change is blocked. Please fix and retry.
```

## Integration Points

- **Security Hook**: Coordinates for secure code
- **Mode System**: Different standards per mode
- **Task Management**: Quality tracked in tasks
- **Documentation**: Links to style guides

## Performance Considerations

- Incremental checking (only changed code)
- Caches validation results
- Async for non-blocking checks
- Early exit on first critical error

## Advanced Features

### Custom Rules
```json
{
  "custom_rules": [
    {
      "name": "webflow_class_prefix",
      "pattern": "^wf-|^w-",
      "message": "Webflow classes should use wf- prefix",
      "severity": "warning"
    }
  ]
}
```

### Mode-Specific Standards
```json
{
  "mode_rules": {
    "deep-work": {
      "allow_todos": true,
      "relaxed_naming": true
    },
    "review": {
      "strict_quality": true,
      "require_tests": true
    }
  }
}
```

## Common Violations

### JavaScript
1. Global variables without namespace
2. Direct DOM manipulation
3. Synchronous loops over large data
4. Missing error handling
5. Console statements

### CSS
1. Pixel units instead of REM
2. !important overuse
3. Inline styles
4. Non-semantic class names
5. Deep nesting (>3 levels)

### General
1. Files too large (>500 lines)
2. Functions too complex
3. Copy-pasted code (DRY violation)
4. Missing documentation
5. Inconsistent formatting

## Troubleshooting

### Too Many Warnings
- Adjust severity thresholds
- Focus on critical issues
- Enable gradual enforcement
- Use mode-specific rules

### False Positives
- Add exceptions for specific cases
- Update pattern matching
- Use inline disable comments
- Report to improve rules

### Performance Impact
- Enable incremental checking
- Cache validation results
- Limit check scope
- Use async validation

## Quality Commands

- `/logic quality check` - Run full check
- `/logic quality report` - Generate report
- `/logic quality fix` - Auto-fix issues
- `/logic quality config` - Adjust settings

## Best Practices

1. **Fix as you go**: Address warnings immediately
2. **Understand why**: Learn from quality feedback
3. **Configure appropriately**: Adjust rules to project
4. **Document exceptions**: Explain rule overrides
5. **Regular reviews**: Audit quality trends

## Related Documentation

- [Code Style Guide](../../standards/style-guide.md)
- [Webflow Best Practices](../../webflow/best-practices.md)
- [Security Hook](./security-scan-hook.md)