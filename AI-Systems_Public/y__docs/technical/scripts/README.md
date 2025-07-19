# Script Documentation

This directory contains comprehensive documentation for all utility scripts in the Claude Code system.

## Table of Contents

### Documentation Scripts
- [add-toc.py](./add-toc.md) - Generates table of contents for markdown files
- [doc-audit.py](./doc-audit.md) - Audits documentation health and coverage
- [doc-updater.py](./doc-updater.md) - Updates documentation structure and links

### System Scripts
- [mode-manager.py](./mode-manager.md) - Manages working mode transitions
- [startup-display.py](./startup-display.md) - Shows system status on startup
- [startup-with-memory.py](./startup-with-memory.md) - Enhanced startup with memory integration

## Script System Overview

Scripts in Claude Code provide utility functions that support the main system operations. They are designed to be:

- **Standalone**: Can be run independently
- **Integrated**: Work with hooks and commands
- **Efficient**: Optimized for performance
- **Maintainable**: Clear, documented code

### Running Scripts

All scripts can be run directly:

```bash
python3 .claude/scripts/script-name.py [arguments]
```

Or through the system:
```bash
/logic scripts run [script-name]
```

### Script Categories

1. **Documentation Management**
   - Maintain documentation quality
   - Generate TOCs and indexes
   - Validate links and structure

2. **System Utilities**
   - Mode management
   - Startup sequences
   - State management

3. **Analysis Tools**
   - Code analysis
   - Performance metrics
   - Health checks

### Creating New Scripts

See the [Script Development Guide](./script-development-guide.md) for creating custom scripts.