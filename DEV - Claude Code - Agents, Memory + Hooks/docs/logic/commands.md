# Command Reference Guide

## Table of Contents

  - [🧠 `/memory` - Knowledge Graph Management](#-memory---knowledge-graph-management)
  - [💾 `/save` - Session Management](#-save---session-management)
  - [🎯 `/logic` - System Logic & Help](#-logic---system-logic-help)
- [Automated Commands (Via Hooks)](#automated-commands-via-hooks)
  - [🔄 Workflow Automation](#-workflow-automation)
  - [🧪 Testing Automation](#-testing-automation)
  - [🔐 Security Scanning](#-security-scanning)
  - [📓 Pattern Extraction](#-pattern-extraction)
  - [🎯 Mode Suggestions](#-mode-suggestions)
  - [📋 Context Management](#-context-management)
  - [📝 Documentation Generation](#-documentation-generation)
- [Quick Tips](#quick-tips)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Environment Variables](#environment-variables)
**Subcommands:**
- `/memory` or `/mem` - Show status and recent memories
- `/memory search <query>` - Search knowledge graph
- `/memory manual <text>` - Capture specific insight
- `/memory auto [level]` - Set automation level (off/manual/semi/full)
- `/memory confirm` - Process pending captures

**Examples:**
```
/memory search "API limits"
/memory manual "Client prefers blue color scheme"
/memory auto semi
```

### 💾 `/save` - Session Management
Save and manage development sessions (replaces `/session`).

**Subcommands:**
- `/save` - Save current session with auto-summary
- `/save new [description]` - Start new session
- `/save list [--all]` - List sessions (--all includes archived)
- `/save search <query>` - Search session content
- `/save stats` - Session statistics

**Examples:**
```
/save new authentication-feature
/save search "database migration"
/save stats
```

### 🎯 `/logic` - System Logic & Help
Unified access to help, configuration, and system tools.

**Subcommands:**
- `/logic` - Show main menu
- `/logic help [topic]` - Access detailed help
- `/logic hooks` - Manage automation hooks
- `/logic tasks` - Task management tools
- `/logic agents` - Multi-agent support
- `/logic metrics` - Performance metrics
- `/logic emergency` - Recovery tools
- `/logic notebook` - Force pattern extraction
- `/logic migrate` - Migration guide from old commands

**Examples:**
```
/logic help automation
/logic hooks status
/logic tasks parallel
```

## Automated Commands (Via Hooks)

These commands now run automatically based on context:

### 🔄 Workflow Automation
- **Triggers**: Complex tasks (3+ steps), architecture decisions, debugging >10min
- **Old command**: `/workflow`
- **Override**: Use Sequential Thinking MCP tool directly

### 🧪 Testing Automation
- **Triggers**: After 3+ files changed, security patterns detected
- **Old command**: `/test`
- **Override**: Run tests manually with `npm test` or similar

### 🔐 Security Scanning
- **Triggers**: Sensitive file patterns, API key detection, production keywords
- **Old command**: `/security`
- **Override**: `/logic emergency disable` to turn off

### 📓 Pattern Extraction
- **Triggers**: Session saves, significant changes, memory captures
- **Old command**: `/notebook`
- **Override**: `/logic notebook` to force extraction

### 🎯 Mode Suggestions
- **Triggers**: Based on branch, file count, task complexity
- **Old command**: `/mode`
- **Override**: Set mode manually in response to suggestions

### 📋 Context Management
- **Triggers**: File operations, tool usage
- **Old command**: `/context`
- **Override**: Automatic, no manual control needed

### 📝 Documentation Generation
- **Triggers**: Git operations, PR creation
- **Old command**: `/pr`
- **Override**: Use git/gh commands directly

## Quick Tips

1. **Most functionality is automated** - Let hooks handle repetitive tasks
2. **Use `/logic hooks status`** to see what's active
3. **Disable specific hooks** with `/logic hooks disable [name]`
4. **Check automation level** with `/memory` status
5. **Emergency recovery** available via `/logic emergency`

## Keyboard Shortcuts

While using Claude Code CLI in the terminal:
- `Ctrl+C` - Cancel current operation
- `Ctrl+D` - Exit Claude Code
- `Ctrl+L` - Clear screen
- `Tab` - Command completion (if available)

## Environment Variables

Control behavior without editing settings:
```bash
CLAUDE_AGENT_ID=agent1    # Set agent identity
CLAUDE_HOOKS_DISABLED=1   # Disable all hooks
CLAUDE_DEBUG=1           # Enable debug output
```