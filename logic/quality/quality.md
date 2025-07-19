# Quality Enforcement Module

## Overview

The Quality module enforces CLAUDE.md guidelines and best practices through automated hooks that run after file modifications. It provides helpful reminders and suggestions to maintain code quality.

## Components

### claude-md-enforcement-hook.py

A PostToolUse hook that analyzes code changes and provides real-time feedback on:
- Console.log statements in production code
- Hardcoded API keys or secrets
- Missing element existence checks
- Pixel units instead of REM in CSS
- Files exceeding 500 lines
- Global scope pollution in JavaScript

### quality-settings.json

Configuration file for the enforcement hook:
- `enabled`: Toggle enforcement on/off
- `enforcement_level`: "helpful" (default) or "strict"
- `show_reminders`: Display helpful suggestions
- `track_tests`: Monitor test execution
- `max_file_lines`: Maximum recommended file size
- `api_key_patterns`: Regex patterns for API key detection
- `custom_patterns`: Additional patterns to check
- `test_tracking`: Track when tests were last run

## Features

### 1. Code Quality Checks

```javascript
// ❌ Detected
console.log("Debug info");

// ✅ Suggested
if (DEBUG) console.log("Debug info");
```

### 2. Security Alerts

```javascript
// 🚨 Blocked
const API_KEY = "sk-1234567890abcdef";

// ✅ Suggested
const API_KEY = process.env.API_KEY;
```

### 3. CSS Best Practices

```css
/* ❌ Detected */
.container { padding: 16px; }

/* ✅ Suggested */
.container { padding: 1rem; }
```

### 4. "Actually Works" Protocol

After significant changes, the hook reminds you to test:
- 3+ files changed → Suggests `/test quick`
- 5+ files changed → Suggests `/test full`
- Security violations → Immediate test reminder

## Usage

The hook runs automatically after Edit, MultiEdit, and Write operations. No manual intervention needed.

### Disable Temporarily
```bash
# Edit quality-settings.json
"enabled": false
```

### Adjust Thresholds
```json
{
  "max_file_lines": 500,
  "reminder_thresholds": {
    "files_before_test_reminder": 3,
    "files_before_urgent_reminder": 5
  }
}
```

## Output Format

```
=== 📋 CLAUDE.md Compliance Check ===
⚠️ Code Quality Reminders:
  • Found console.log (line 45)
    → Use debug wrapper: if (DEBUG) console.log(...)
  
🧪 Actually Works Protocol:
  → Run `/test quick` to validate changes
  
✅ Following CLAUDE.md best practices
=====================================
```

## Integration

Works seamlessly with:
- Session management hooks (tracks changes)
- Memory system (captures patterns)
- Mode system (respects current mode)

## Customization

Add custom patterns in quality-settings.json:
```json
"custom_patterns": {
  "todo_comments": "TODO:|FIXME:|HACK:",
  "deprecated_apis": "document.write|eval\\("
}
```