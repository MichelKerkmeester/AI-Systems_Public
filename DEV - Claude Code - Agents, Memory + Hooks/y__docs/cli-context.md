# Claude Code CLI Context

## Table of Contents

- [Environment Details](#environment-details)
- [Key Points](#key-points)
  - [CLI-First Design](#cli-first-design)
  - [What This Means](#what-this-means)
  - [Desktop App vs CLI](#desktop-app-vs-cli)
- [Workflow](#workflow)
  - [Typical CLI Session](#typical-cli-session)
  - [Hook Automation](#hook-automation)
- [Optional Components](#optional-components)
  - [DesktopCommanderMCP](#desktopcommandermcp)
  - [Other MCPs](#other-mcps)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
  - ["Desktop restart required"](#desktop-restart-required)
  - [Hook not triggering](#hook-not-triggering)
  - [Command not found](#command-not-found)
- [Summary](#summary)
## Environment Details

- **Primary Interface**: Claude Code CLI
- **Terminal**: Warp
- **Shell**: zsh (macOS)
- **Working Directory**: `/Users/michel_kerkmeester/AI & Dev/Websites/• anobel.nl`

## Key Points

### CLI-First Design
1. All commands (`/memory`, `/save`, `/logic`) work in the terminal
2. Hooks run automatically based on your CLI actions
3. No desktop app restart required for functionality
4. All automation triggers from terminal activity

### What This Means
- **No GUI**: Everything happens in your terminal
- **No restarts**: Changes take effect immediately
- **Direct feedback**: Results appear in your terminal
- **Session persistence**: Works across terminal sessions

### Desktop App vs CLI

| Feature | CLI (This Project) | Desktop App |
|---------|-------------------|-------------|
| Commands | ✅ All work | ✅ All work |
| Hooks | ✅ Automatic | ✅ Automatic |
| DesktopCommanderMCP | ❌ Not needed | ✅ Optional enhancement |
| Restart required | ❌ Never | ✅ For MCP changes |
| Interface | Terminal | GUI |

## Workflow

### Typical CLI Session
```bash
# Start working in Warp terminal
cd "/Users/michel_kerkmeester/AI & Dev/Websites/• anobel.nl"

# Claude Code CLI is ready - no setup needed
# Just start coding - hooks handle automation

# Use commands when needed
/memory search "api limits"
/save new feature-branch
/logic hooks status
```

### Hook Automation
Hooks monitor your terminal activity and trigger automatically:
- File changes → Quality checks
- Complex tasks → Workflow suggestions
- Security patterns → Automatic scanning
- Session timeouts → Auto-save

## Optional Components

### DesktopCommanderMCP
- **Status**: Configured but not required for CLI
- **Purpose**: Enhanced automation for desktop app users
- **CLI Impact**: None - full functionality without it

### Other MCPs
All other MCP servers (Graphiti, Gemini, GitHub, etc.) work perfectly in CLI environment.

## Best Practices

1. **Trust the automation** - Hooks handle most tasks
2. **Use 3 commands** - `/memory`, `/save`, `/logic`
3. **Check hook status** - `/logic hooks status`
4. **Emergency control** - `/logic emergency` if needed

## Troubleshooting

### "Desktop restart required"
- **Ignore for CLI** - This only applies to desktop app users
- All features work immediately in terminal

### Hook not triggering
1. Check status: `/logic hooks status`
2. Verify automation: `/memory` (check level)
3. Manual trigger available for most hooks

### Command not found
- Only 3 commands remain: `/memory`, `/save`, `/logic`
- Old commands are automated - check `/logic help migration`

## Summary

This is a CLI-first project. All references to "Claude Desktop" or "restart required" can be safely ignored when using Claude Code CLI in your terminal. The system is designed to work seamlessly in your Warp terminal without any desktop application dependencies.