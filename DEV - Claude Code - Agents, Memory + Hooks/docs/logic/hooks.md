# Understanding Automation Hooks

## Table of Contents

- [Hook Events](#hook-events)
  - [🎯 UserPromptSubmit](#-userpromptsubmit)
  - [🔧 PreToolUse](#-pretooluse)
  - [📊 PostToolUse](#-posttooluse)
- [Hook Configuration](#hook-configuration)
  - [Enable/Disable Hooks](#enabledisable-hooks)
  - [Hook Settings Locations](#hook-settings-locations)
- [Common Hook Patterns](#common-hook-patterns)
  - [1. Auto-Session Management](#1-auto-session-management)
  - [2. Memory Context Loading](#2-memory-context-loading)
  - [3. Pattern Extraction](#3-pattern-extraction)
  - [4. Quality Enforcement](#4-quality-enforcement)
  - [5. Security Scanning](#5-security-scanning)
- [Troubleshooting Hooks](#troubleshooting-hooks)
  - [Hook Not Running?](#hook-not-running)
  - [Hook Blocking Operations?](#hook-blocking-operations)
  - [Performance Issues?](#performance-issues)
- [Creating Custom Hooks](#creating-custom-hooks)
  - [Basic Hook Structure](#basic-hook-structure)
  - [Hook Best Practices](#hook-best-practices)
- [Advanced Hook Features](#advanced-hook-features)
  - [Conditional Execution](#conditional-execution)
  - [Hook Chaining](#hook-chaining)
  - [Recovery Mechanisms](#recovery-mechanisms)
## Hook Events

### 🎯 UserPromptSubmit
Triggered when you submit a prompt to Claude.

**Active hooks:**
- **quality-hook** - Enforces code quality and CLAUDE.md compliance
- **memory-context-hook** - Loads relevant memories from Graphiti
- **mode-suggestion-hook** - Suggests optimal mode for your task
- **workflow-automation-hook** - Triggers Sequential Thinking for complex tasks

### 🔧 PreToolUse
Triggered before any tool executes.

**Active hooks:**
- **session-hook** - Creates new sessions after 4-hour timeout

### 📊 PostToolUse
Triggered after tool execution completes.

**Active hooks:**
- **session-hook** - Updates session with tool usage
- **context-management-hook** - Maintains context state
- **pattern-extraction-hook** - Extracts patterns from code/conversation
- **quality-hook** - Checks code quality after edits
- **security-scan-hook** - Scans for security issues

## Hook Configuration

### Enable/Disable Hooks

```bash
# Via command
/logic hooks disable pattern-extraction-hook
/logic hooks enable memory-context-hook

# Via settings.json
{
  "hooks": {
    "enabled": false  # Disable all hooks
  }
}

# Via environment variable
CLAUDE_HOOKS_DISABLED=1 claude code
```

### Hook Settings Locations

```
.claude/
├── settings.json              # Global hook configuration
├── logic/
│   ├── session/hooks/
│   │   └── session-settings.json    # Session-specific settings
│   ├── memory/
│   │   └── settings.json            # Memory automation settings
│   └── quality/hooks/
│       └── quality-settings.json    # Quality check thresholds
```

## Common Hook Patterns

### 1. Auto-Session Management
- Creates new session after 4-hour timeout
- Archives old sessions when limit reached
- Generates session summaries automatically

### 2. Memory Context Loading
- Analyzes your prompts for keywords
- Searches Graphiti for relevant memories
- Shows context before Claude responds

### 3. Pattern Extraction
- Scans for client preferences, constraints, patterns
- Updates knowledge files automatically
- Deduplicates against existing entries

### 4. Quality Enforcement
- Reminds about testing after multiple file changes
- Enforces DRY principles
- Suggests refactoring for large files

### 5. Security Scanning
- Detects API keys and secrets
- Blocks unsafe file writes
- Alerts on security patterns

## Troubleshooting Hooks

### Hook Not Running?
1. Check if hooks are enabled: `/logic hooks status`
2. Verify hook file exists and is executable
3. Check for path issues (spaces in path need quotes)
4. Run with debug: `claude --debug`

### Hook Blocking Operations?
1. Check hook output for error messages
2. Disable problematic hook: `/logic hooks disable [name]`
3. Use emergency disable: `/logic emergency disable`

### Performance Issues?
1. Check metrics: `/logic metrics`
2. Disable non-critical hooks
3. Adjust hook settings for less frequent runs

## Creating Custom Hooks

### Basic Hook Structure
```python
#!/usr/bin/env python3
import sys
import json

# Read input
hook_input = json.loads(sys.stdin.read())

# Process based on event
if hook_input.get("toolName") == "Edit":
    # Custom logic here
    pass

# Exit codes:
# 0 = success, continue
# 2 = block operation
# Any output = show to user
sys.exit(0)
```

### Hook Best Practices
1. **Fast execution** - Keep under 100ms
2. **Fail gracefully** - Don't break on errors
3. **Minimal output** - Only show important info
4. **State management** - Use proper state files
5. **Security** - Never log sensitive data

## Advanced Hook Features

### Conditional Execution
Hooks can check conditions before running:
- Branch name
- File patterns  
- Time of day
- User preferences

### Hook Chaining
Multiple hooks can work together:
1. Memory hook finds context
2. Pattern extractor updates knowledge
3. Session hook records activity

### Recovery Mechanisms
Hooks include crash recovery:
- Recovery points before critical operations
- State restoration after crashes
- Automatic cleanup of incomplete operations