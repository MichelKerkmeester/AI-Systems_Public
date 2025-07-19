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
docs/
├── graphiti/
│   ├── README.md # Overview and navigation
│   ├── memory-verifcation-guide.md # Testing and verification
│   └── practical-examples.md # Real-world usage examples
├── logic/
│   ├── README.md # Overview and navigation
│   ├── advanced.md
│   ├── automation.md # Automation patterns
│   ├── commands.md # Command reference
│   ├── hooks.md # Hook system docs
│   ├── migration.md # Migration guide
│   └── troubleshooting.md # Common issues and solutions
├── mcp/
│   ├── desktop-commander/
│   │   └── README.md # Overview and navigation
│   ├── gemini/
│   │   └── README.md # Overview and navigation
│   ├── github/
│   │   └── README.md # Overview and navigation
│   ├── n8n/
│   │   └── README.md # Overview and navigation
│   ├── sequential-thinking/
│   │   └── README.md # Overview and navigation
│   └── README.md # Overview and navigation
├── technical/
│   └── hooks-in-cc.md
├── CLI-CONTEXT.md
└── README.md # Overview and navigation
```

## Overview

Welcome to the Claude Code documentation for the anobel.nl project. This documentation is organized to provide easy access to all system components, automation features, and integration guides.

## Documentation Structure

```
docs/
├── README.md                # This file
├── CLI-CONTEXT.md          # CLI environment and workflow guide
├── graphiti/               # Graphiti memory system documentation
│   ├── README.md
│   └── memory-verifcation-guide.md
├── logic/                  # Logic system and hooks documentation
│   ├── advanced.md         # Advanced features and customization
│   ├── automation.md       # Automation patterns and workflows
│   ├── commands.md         # Command reference guide
│   ├── hooks.md           # Hook system documentation
│   ├── migration.md       # Migration from old commands
│   └── troubleshooting.md # Common issues and solutions
├── technical/             # Technical implementation details
│   └── hooks-in-cc.md    # Hook implementation in Claude Code
└── mcp/                   # MCP server documentation (coming soon)
    ├── sequential-thinking/
    ├── gemini/
    ├── github/
    ├── n8n/
    └── desktop-commander/
```

## Navigation Guide

### Quick Start
- New to Claude Code? Start with [CLI-CONTEXT.md](./CLI-CONTEXT.md)
- Migrating from old commands? See [logic/migration.md](./logic/migration.md)
- Need help? Check [logic/troubleshooting.md](./logic/troubleshooting.md)

### By Topic
- **Commands & Usage**: [logic/commands.md](./logic/commands.md)
- **Automation**: [logic/automation.md](./logic/automation.md)
- **Hooks System**: [logic/hooks.md](./logic/hooks.md)
- **Memory Management**: [graphiti/README.md](./graphiti/README.md)
- **Advanced Features**: [logic/advanced.md](./logic/advanced.md)

### By Use Case
- **Setting up automation**: Start with [logic/automation.md](./logic/automation.md)
- **Understanding hooks**: Read [logic/hooks.md](./logic/hooks.md)
- **Managing memory**: See [graphiti/README.md](./graphiti/README.md)
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