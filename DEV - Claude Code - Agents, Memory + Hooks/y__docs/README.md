# Claude Code Documentation

## Table of Contents

- [Directory Structure](#directory-structure)
- [Overview](#overview)
- [Documentation Structure](#documentation-structure)
- [Navigation Guide](#navigation-guide)
  - [Quick Start](#quick-start)
  - [By Topic](#by-topic)
  - [By Use Case](#by-use-case)
- [Documentation Standards](#documentation-standards)
  - [File Organization](#file-organization)
  - [Content Guidelines](#content-guidelines)
  - [Markdown Standards](#markdown-standards)
- [Contributing](#contributing)
## Directory Structure

```
y__docs/
├── agents/          # Multi-agent system documentation
├── graphiti/        # Memory system documentation
├── hooks/           # Hook system documentation
├── logic/           # Logic commands and automation
├── mcp/             # MCP server integrations
├── memory/          # Memory management guides
├── scripts/         # Script documentation
├── technical/       # Technical references
├── cli-context.md   # CLI environment guide
└── README.md        # This file
```

## Overview

Welcome to the Claude Code documentation for the anobel.nl project. This documentation is organized to provide easy access to all system components, automation features, and integration guides.

## Documentation Structure

### Core Documentation
- **agents/** - Multi-agent system architecture and implementation
- **graphiti/** - Memory management with Neo4j integration
- **hooks/** - Individual hook documentation and guides
- **logic/** - Logic system, commands, and automation
- **mcp/** - MCP server documentation for all integrations
- **memory/** - Memory patterns and best practices
- **scripts/** - Utility scripts and tools
- **technical/** - Technical references and specifications

### Key Files
- **cli-context.md** - CLI environment specifics and workflow
- **README.md** - Main documentation index (this file)

## Navigation Guide

### Quick Start
- New to Claude Code? Start with [cli-context.md](./cli-context.md)
- Understanding hooks? See [hooks/README.md](./hooks/README.md)
- Need help? Check [logic/troubleshooting.md](./logic/troubleshooting.md)

### By Topic
- **Commands & Usage**: [logic/commands.md](./logic/commands.md)
- **Automation**: [logic/automation.md](./logic/automation.md)
- **Hook System**: [hooks/README.md](./hooks/README.md)
- **Memory Management**: [graphiti/README.md](./graphiti/README.md)
- **MCP Servers**: [mcp/README.md](./mcp/README.md)
- **Scripts & Tools**: [scripts/README.md](./scripts/README.md)
- **Multi-Agent System**: [agents/README.md](./agents/README.md)

### By Use Case
- **Setting up automation**: Start with [logic/automation.md](./logic/automation.md)
- **Creating custom hooks**: Read [hooks/hook-development-guide.md](./hooks/hook-development-guide.md)
- **Managing memory**: See [graphiti/README.md](./graphiti/README.md) and [memory/](./memory/)
- **Using MCP servers**: Browse [mcp/](./mcp/) for specific integrations
- **Debugging issues**: Check [logic/troubleshooting.md](./logic/troubleshooting.md)

## Documentation Standards

### File Organization
- Each major component gets its own directory
- README.md files provide overviews and navigation
- Detailed guides use descriptive filenames
- Technical specs go in the `technical/` directory

### Content Guidelines
1. **Table of Contents**: All documents must have a TOC
2. **Clear Headers**: Use descriptive, hierarchical headers
3. **Code Examples**: Include practical, working examples
4. **Cross-References**: Link to related documentation
5. **Versioning**: Note when features were added/changed

### Markdown Standards
- Use ATX-style headers (`#`, `##`, etc.)
- Code blocks with language hints (` ```python `)
- Tables for comparisons and feature matrices
- Anchor links for navigation

## Contributing

When adding new documentation:
1. Place it in the appropriate directory
2. Run the TOC generator: `python3 .claude/scripts/add-toc.py`
3. Update relevant README files
4. Add cross-references from related docs
5. Test all links and code examples

---

*Last updated: 2025-01-19*
*Part of the Claude Code documentation organization initiative*