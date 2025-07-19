# Desktop Commander MCP Documentation (Optional)

## Table of Contents

- [Important Note](#important-note)
- [Overview](#overview)
- [Installation Notes](#installation-notes)
  - [For CLI Users (This Project)](#for-cli-users-this-project)
  - [For Desktop App Users](#for-desktop-app-users)
- [CLI vs Desktop Clarification](#cli-vs-desktop-clarification)
  - [Claude Code CLI (This Project)](#claude-code-cli-this-project)
  - [Claude Desktop App](#claude-desktop-app)
- [Feature Comparison](#feature-comparison)
- [When to Use](#when-to-use)
  - [Use Built-in Tools (Recommended)](#use-built-in-tools-recommended)
  - [Consider Desktop Commander MCP If:](#consider-desktop-commander-mcp-if)
  - [CLI Users: Equivalent Features](#cli-users-equivalent-features)
- [Summary](#summary)
## Important Note

**Desktop Commander MCP is OPTIONAL and only relevant for Claude Desktop app users.**

This project uses Claude Code CLI in the terminal, where Desktop Commander is not needed. All file operations, process management, and system commands work perfectly through standard Claude Code tools.

## Overview

Desktop Commander MCP provides enhanced file system and process management capabilities for Claude Desktop app users. It offers:

- Advanced file operations with granular permissions
- Process and terminal session management
- Security-focused command execution
- Performance monitoring

## Installation Notes

### For CLI Users (This Project)
**No installation needed.** Claude Code CLI already has all necessary file and command capabilities.

### For Desktop App Users
If you're using Claude Desktop app and want enhanced capabilities:

1. The MCP is pre-configured in `.claude/settings.json`
2. Restart Claude Desktop to activate
3. Configure security settings as prompted

## CLI vs Desktop Clarification

### Claude Code CLI (This Project)
- **Built-in Tools**: Read, Write, Edit, Bash, etc.
- **No MCP Needed**: Full functionality out of the box
- **Terminal-Based**: Direct command execution
- **No Restart Required**: Immediate availability

### Claude Desktop App
- **Basic Tools**: Same as CLI
- **Optional MCP**: Adds advanced features
- **GUI-Based**: Visual interface
- **Restart Required**: For MCP activation

## Feature Comparison

| Feature | CLI (Built-in) | Desktop Commander MCP |
|---------|----------------|----------------------|
| Read files | ✅ Read tool | ✅ Enhanced with line limits |
| Write files | ✅ Write tool | ✅ With chunking support |
| Edit files | ✅ Edit tool | ✅ Block editing |
| Run commands | ✅ Bash tool | ✅ Process management |
| File search | ✅ Grep/Glob | ✅ Ripgrep integration |
| Permissions | Standard | ✅ Granular control |
| Process control | Basic | ✅ Advanced sessions |

## When to Use

### Use Built-in Tools (Recommended)
For 99% of tasks, the built-in Claude Code tools are sufficient:
```python
# Reading files
content = Read(file_path="/path/to/file")

# Writing files
Write(file_path="/path/to/file", content="...")

# Running commands
Bash(command="npm test")
```

### Consider Desktop Commander MCP If:
1. Using Claude Desktop app (not CLI)
2. Need advanced process management
3. Require granular security controls
4. Want ripgrep-powered search
5. Need performance monitoring

### CLI Users: Equivalent Features
Desktop Commander features and their CLI equivalents:

```bash
# File operations - Use built-in tools
Read, Write, Edit, MultiEdit

# Process management - Use Bash
Bash(command="ps aux | grep node")
Bash(command="kill -9 <pid>")

# Code search - Use Grep
Grep(pattern="TODO", path=".")

# File search - Use Glob
Glob(pattern="**/*.js")
```

## Summary

Desktop Commander MCP is an optional enhancement for desktop app users. This project uses Claude Code CLI, where all necessary functionality is available through built-in tools. No additional setup or MCP activation is required for CLI users.

---

*This documentation is included for completeness. CLI users can safely ignore Desktop Commander MCP.*

*See also: [CLI Context](../../CLI-CONTEXT.md) | [MCP Overview](../README.md)*