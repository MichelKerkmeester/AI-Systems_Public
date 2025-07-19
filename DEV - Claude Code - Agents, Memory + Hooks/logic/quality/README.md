# CLAUDE.md Enforcement System

## Overview

The CLAUDE.md enforcement system helps ensure code quality and adherence to project standards by automatically checking code changes against the rules defined in CLAUDE.md.

## Features

### 1. Code Quality Checks
- **Console statements**: Detects `console.log/error/warn/info` in production code
- **CSS units**: Warns about pixel units instead of REM
- **DOM safety**: Checks for missing null checks on DOM queries
- **Global scope**: Detects potential global variable pollution
- **File size**: Warns when files exceed 500 lines

### 2. Security Checks
- **API keys**: Critical alert for hardcoded secrets (blocks execution)
- **Passwords**: Detects potential password strings
- **Tokens**: Identifies authentication tokens

### 3. "Actually Works" Protocol
Reminds you to test code after significant changes:
- Triggered after 20+ lines changed
- Triggered after 3+ files modified
- Always triggers for critical files (auth, api, payment, security)
- Tracks if tests were run in current session

## Configuration

Edit `.claude/logic/quality/quality-settings.json` to customize:

```json
{
  "enforcement_level": "balanced",  // off, minimal, balanced, strict
  "auto_test_reminder": true,       // Show test reminders
  "show_suggestions": true,         // Show fix suggestions
  "reminder_threshold": {
    "lines_changed": 20,
    "files_changed": 3,
    "critical_files": ["auth", "api", "payment", "security"]
  }
}
```

## Hook Output Examples

### Clean Code
```
=== 📋 CLAUDE.md Compliance Check ===
✅ Following CLAUDE.md best practices
=====================================
```

### Warnings (Non-blocking)
```
=== 📋 CLAUDE.md Compliance Check ===
⚠️  Code Quality Reminders:
  • Found console.log in production code (line 45)
    → Use debug wrapper: if (DEBUG) console.log(...)
  • CSS uses px units (style.css:23)
    → Convert to REM: 16px = 1rem

🧪 Actually Works Protocol:
  → Run `/test quick` to validate changes
  → Verify functionality before claiming completion
  📖 Testing is not optional - it's professional
=====================================
```

### Critical Issues (Blocking)
```
=== 📋 CLAUDE.md Compliance Check ===
🚨 CRITICAL ISSUES:
  • Potential API key or secret detected (line 14)
    → Use environment variables (.env file)
    📖 See CLAUDE.md: Security & API Key Protection
=====================================
```

## How It Works

1. **Automatic Triggering**: Runs after Edit, MultiEdit, or Write operations
2. **Pattern Matching**: Uses regex to detect violations
3. **Severity Levels**: 
   - Critical: Blocks operation (exit code 2)
   - Warning: Shows reminder but allows operation
4. **Session Tracking**: Remembers test runs and accumulates change stats
5. **Smart Suggestions**: Provides context-aware test commands

## Disabling

To temporarily disable:
1. Set `"enforcement_level": "off"` in quality-settings.json
2. Or disable hooks in .claude/settings.json

## Integration with CLAUDE.md

The hook enforces these CLAUDE.md sections:
- Technical Constraints (console, px units, DOM checks)
- Security & API Key Protection
- Production Checklist
- Core Philosophy (test before claiming completion)