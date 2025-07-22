# Logic System Documentation

## Table of Contents

- [Directory Structure](#directory-structure)
- [Overview](#overview)
- [Quick Navigation](#quick-navigation)
  - [Essential Guides](#essential-guides)
- [Documentation Index](#documentation-index)
  - [commands.md](#commandsmd)
  - [automation.md](#automationmd)
  - [hooks.md](#hooksmd)
  - [migration.md](#migrationmd)
  - [troubleshooting.md](#troubleshootingmd)
  - [advanced.md](#advancedmd)
- [Command Quick Reference](#command-quick-reference)
- [Common Tasks](#common-tasks)
  - [Check What's Automated](#check-whats-automated)
  - [Get Help on a Topic](#get-help-on-a-topic)
  - [Temporarily Disable Automation](#temporarily-disable-automation)
  - [Find Old Command Equivalent](#find-old-command-equivalent)
  - [Debug Hook Issues](#debug-hook-issues)
## Directory Structure

```
logic/
├── README.md # Overview and navigation
├── automation.md # Automation patterns
├── commands.md # Command reference
└── troubleshooting.md # Common issues and solutions
```
## Overview

The Logic system is the heart of Claude Code's automation and command infrastructure. It manages hooks, commands, and intelligent automation to streamline your development workflow.

## Quick Navigation

### Essential Guides
- 🚀 **[Commands Reference](./commands.md)** - All `/logic` command variations
- 🤖 **[Automation Guide](./automation.md)** - How automation works
- 🪝 **[Hooks Documentation](./hooks.md)** - Understanding the hook system
- 🔄 **[Migration Guide](./migration.md)** - Moving from old commands
- 🔧 **[Troubleshooting](./troubleshooting.md)** - Fix common issues
- 🎯 **[Advanced Features](./advanced.md)** - Power user features

## Documentation Index

### commands.md
Complete reference for the `/logic` command system:
- `/logic help` - Access help topics
- `/logic hooks` - Manage hook system
- `/logic emergency` - Emergency controls
- `/logic notebook` - Notebook operations
- `/logic migrate` - Migration assistance

### automation.md
Understanding Claude Code's automation:
- How hooks trigger automatically
- Automation levels and control
- Pattern detection and responses
- Performance considerations
- Customization options

### hooks.md
Deep dive into the hook system:
- Hook architecture and lifecycle
- Available hooks and their triggers
- Creating custom hooks
- Hook priorities and execution order
- Debugging hook issues

### migration.md
Transitioning from the old command system:
- Command mapping (old → new)
- What's automated now
- Step-by-step migration guide
- Common migration issues
- Verification steps

### troubleshooting.md
Solutions for common problems:
- Hooks not triggering
- Command not found errors
- Performance issues
- Session problems
- Emergency recovery

### advanced.md
Advanced features and customization:
- Custom hook development
- Performance tuning
- Multi-agent workflows
- System internals
- Extension points

## Command Quick Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `/logic help` | Get help on any topic | `/logic help hooks` |
| `/logic hooks status` | Check hook system | `/logic hooks status` |
| `/logic emergency disable` | Disable all automation | `/logic emergency disable` |
| `/logic migrate` | Get migration help | `/logic migrate workflow` |
| `/logic notebook` | Access notebook | `/logic notebook` |

## Common Tasks

### Check What's Automated
```bash
/logic hooks status
```

### Get Help on a Topic
```bash
/logic help [topic]
# Examples:
/logic help automation
/logic help migration
/logic help troubleshooting
```

### Temporarily Disable Automation
```bash
/logic emergency disable
# Re-enable with:
/logic emergency enable
```

### Find Old Command Equivalent
```bash
/logic migrate [old-command]
# Example:
/logic migrate workflow
```

### Debug Hook Issues
```bash
/logic hooks status
/logic hooks test [hook-name]
```

---

*Navigation tip: Each document has its own table of contents for easy navigation within that guide.*