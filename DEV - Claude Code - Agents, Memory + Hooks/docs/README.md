# 🚀 Claude Code Automation System Documentation

## Table of Contents

- [System Overview](#system-overview)
- [Automated Features & Commands](#automated-features--commands)
- [Directory Structure](#directory-structure)
- [Quick Command Reference](#quick-command-reference)
- [Automation Components](#automation-components)
  - [Hooks System](#hooks-system)
  - [MCP Integrations](#mcp-integrations)
  - [Logic & Commands](#logic--commands)
  - [Scripts & Tools](#scripts--tools)
- [Navigation Guide](#navigation-guide)
  - [Quick Start](#quick-start)
  - [By Feature](#by-feature)
  - [By Use Case](#by-use-case)
- [Documentation Standards](#documentation-standards)
- [Contributing](#contributing)

## System Overview

The Claude Code automation system for anobel.nl provides comprehensive automation through intelligent hooks, MCP integrations, and a powerful command system. This documentation covers all automated features, commands, and integration points.

### 🎯 Core Philosophy
- **Automation First**: Everything that can be automated, is automated
- **Code Reuse**: Search existing code before creating new files
- **Quality Control**: Automatic security scans, testing reminders, and pattern enforcement
- **Knowledge Management**: Automatic memory capture and retrieval

## Automated Features & Commands

### 📍 Primary Commands (Just 2!)

| Command | Purpose | Syntax | Details |
|---------|---------|--------|---------|
| `/memory` | Knowledge management | `/memory [search\|manual\|auto]` | [→ Memory Guide](./memory/README.md) |
| `/logic` | System control & help | `/logic [help\|hooks\|emergency]` | [→ Logic Commands](./logic/commands.md) |

### ⚡ Automated Features (13+ Active Hooks)

| Feature | What It Does | When It Runs | Learn More |
|---------|--------------|--------------|------------|
| **Quality Control** | Enforces code standards, file size limits | On every file edit | [→ Quality Hook](./hooks/quality-hook.md) |
| **Security Scanning** | Detects exposed secrets, API keys | On file changes | [→ Security Hook](./hooks/security-scan-hook.md) |
| **Memory Capture** | Auto-saves decisions, errors, patterns | After tool use, decisions | [→ Memory Hook](./hooks/memory-context-hook.md) |
| **Task Management** | Limits 1 active task, tracks progress | On TodoWrite calls | [→ Task Hook](./hooks/task-management-hook.md) |
| **Pattern Extraction** | Identifies and saves coding patterns | On pattern discovery | [→ Pattern Hook](./hooks/pattern-extraction-hook.md) |
| **Doc Updates** | Maintains documentation TOCs | On .md file changes | [→ Doc Hook](./hooks/doc-update-hook.md) |

### 🤖 MCP Integrations (8 Active)

| Integration | Purpose | Key Functions | Documentation |
|-------------|---------|---------------|---------------|
| **Graphiti** | Knowledge graph & memory | `search`, `add_episode` | [→ Graphiti Docs](./mcp/graphiti/README.md) |
| **Sequential Thinking** | Structured reasoning | `process_thought` | [→ Sequential Docs](./mcp/sequential-thinking/README.md) |
| **GitHub** | Repository automation | PR/issue management | [→ GitHub Docs](./mcp/github/README.md) |
| **Playwright** | Browser automation | Testing, scraping | [→ Playwright Docs](./mcp/playwright/README.md) |
| **n8n** | Workflow automation | Node management | [→ n8n Docs](./mcp/n8n/README.md) |
| **Context7** | Documentation retrieval | Library docs | [→ Context7 Docs](./mcp/context7/README.md) |
| **Figma** | Design integration | Code generation | [→ Figma Docs](./mcp/figma/README.md) |
| **Chrome Debug** | Browser debugging | Console access | [→ Chrome Docs](./mcp/chrome-debug/README.md) |

## Quick Command Reference

```bash
# Essential Commands
/memory search "pattern"    # Search knowledge base
/memory manual             # Switch to manual capture mode
/memory auto               # Enable auto-capture (default)


/logic help                # Get help on any topic
/logic help automation     # Learn about automation
/logic hooks status        # Check hook status
/logic emergency disable   # Emergency automation disable

# Common Tasks
/logic help code-reuse     # Code reuse workflow
/logic help troubleshooting # Fix common issues
/logic help migration      # Migrate from old commands
```

## Automation Components

### Hooks System

The hook system provides intelligent automation through 16+ specialized hooks:

| Hook Category | Hooks | Purpose |
|--------------|-------|---------|
| **Core Hooks** | doc-update, folder-structure, spec-generation | System maintenance |
| **Quality Hooks** | quality, security-scan, pattern-extraction | Code quality & security |
| **Memory Hooks** | memory-context, context-management | Knowledge management |
| **Workflow Hooks** | task-management, workflow-automation | Process automation |
| **Enhancement Hooks** | prompt-enhancement, query-planning | AI assistance |
| **Tool Hooks** | parallel-agent | Performance optimization |

[→ Complete Hook Documentation](./hooks/README.md)

### MCP Integrations

Model Context Protocol servers extend Claude's capabilities:

| Server | Key Features | Common Uses |
|--------|--------------|-------------|
| **Graphiti** | Neo4j knowledge graph | Memory storage, pattern recognition |
| **GitHub** | Full GitHub API | PRs, issues, workflow automation |
| **Playwright** | Browser control | Testing, web scraping, automation |
| **n8n** | Workflow builder | Complex automations, integrations |
| **Figma** | Design-to-code | UI component generation |
| **Context7** | Library docs | Up-to-date documentation retrieval |

[→ MCP Server Documentation](./mcp/README.md)

### Logic & Commands

The logic system provides:
- **3 Primary Commands**: Simple, powerful interface
- **Help System**: Contextual help for every feature
- **Emergency Controls**: Safety mechanisms
- **Mode Management**: Auto/manual operation modes

[→ Logic System Documentation](./logic/README.md)

### Scripts & Tools

Utility scripts that power automation:
- **doc-updater.py**: Maintains documentation structure
- **add-toc.py**: Generates table of contents
- **startup-display.py**: Shows system status
- **doc-audit.py**: Validates documentation

[→ Scripts Documentation](./scripts/README.md)

## Directory Structure

```
docs/
├── hooks/
│   ├── README.md # Overview and navigation
│   ├── claude-code-hooks-reference.md
│   ├── context-management-hook.md
│   ├── doc-update-hook.md
│   ├── hook-development-guide.md
│   ├── memory-context-hook.md
│   ├── parallel-agent-hook.md
│   ├── pattern-extraction-hook.md
│   ├── prompt-enhancement-hook.md
│   ├── quality-hook.md
│   ├── query-planning-hook.md
│   ├── security-scan-hook.md
│   ├── session-hook.md
│   ├── task-management-hook.md
│   └── workflow-automation-hook.md
├── logic/
│   ├── README.md # Overview and navigation
│   ├── automation.md # Automation patterns
│   ├── commands.md # Command reference
│   └── troubleshooting.md # Common issues and solutions
├── mcp/
│   ├── chrome-debug/
│   │   └── README.md # Overview and navigation
│   ├── context7/
│   │   └── README.md # Overview and navigation
│   ├── figma/
│   │   └── README.md # Overview and navigation
│   ├── github/
│   │   └── README.md # Overview and navigation
│   ├── graphiti/
│   │   └── README.md # Overview and navigation
│   ├── n8n/
│   │   └── README.md # Overview and navigation
│   ├── playwright/
│   │   └── README.md # Overview and navigation
│   ├── puppeteer/
│   │   └── README.md # Overview and navigation
│   ├── sequential-thinking/
│   │   └── README.md # Overview and navigation
│   └── README.md # Overview and navigation
├── memory/
│   ├── README.md # Overview and navigation
│   ├── memory-verifcation-guide.md # Testing and verification
│   └── practical-examples.md # Real-world usage examples
├── project-management/
│   └── project-structure-standard.md
├── scripts/
│   ├── README.md # Overview and navigation
│   ├── add-toc.md
│   ├── doc-audit.md
│   ├── doc-updater.md
│   ├── startup-display.md
│   └── startup-with-memory.md
└── README.md # Overview and navigation
```
## Navigation Guide

### Quick Start
- **New to the system?** Start with [logic/README.md](./logic/README.md)
- **Understanding hooks?** See [hooks/README.md](./hooks/README.md)
- **Need help?** Check [logic/troubleshooting.md](./logic/troubleshooting.md)
- **Quick reference?** Use `/logic help`

### By Feature

#### 🎯 Core Commands
- **Commands Reference**: [logic/commands.md](./logic/commands.md)
- **Automation Overview**: [logic/automation.md](./logic/automation.md)
- **Troubleshooting**: [logic/troubleshooting.md](./logic/troubleshooting.md)

#### ⚡ Hook System
- **All Hooks Overview**: [hooks/README.md](./hooks/README.md)
- **Hook Reference**: [hooks/claude-code-hooks-reference.md](./hooks/claude-code-hooks-reference.md)
- **Development Guide**: [hooks/hook-development-guide.md](./hooks/hook-development-guide.md)
- **Individual Hook Docs**: Browse [hooks/](./hooks/) directory

#### 🧠 Memory & Knowledge
- **Memory System**: [memory/README.md](./memory/README.md)
- **Graphiti Integration**: [mcp/graphiti/README.md](./mcp/graphiti/README.md)
- **Practical Examples**: [memory/practical-examples.md](./memory/practical-examples.md)
- **Verification Guide**: [memory/memory-verifcation-guide.md](./memory/memory-verifcation-guide.md)

#### 🤖 MCP Integrations
- **All MCP Servers**: [mcp/README.md](./mcp/README.md)
- **Individual Server Docs**: Browse [mcp/](./mcp/) subdirectories

#### 📜 Scripts & Tools
- **Script Overview**: [scripts/README.md](./scripts/README.md)
- **Doc Updater**: [scripts/doc-updater.md](./scripts/doc-updater.md)
- **TOC Generator**: [scripts/add-toc.md](./scripts/add-toc.md)

### By Use Case
- **Setting up automation**: Start with [logic/automation.md](./logic/automation.md)
- **Creating custom hooks**: Read [hooks/hook-development-guide.md](./hooks/hook-development-guide.md)
- **Managing memory**: See [memory/README.md](./memory/README.md)
- **Using MCP servers**: Browse [mcp/](./mcp/) for specific integrations
- **Debugging issues**: Check [logic/troubleshooting.md](./logic/troubleshooting.md)
- **Understanding project structure**: See [project-management/project-structure-standard.md](./project-management/project-structure-standard.md)

## 🔄 Automation Triggers

### What Happens Automatically

#### On File Changes
- ✅ Security scan for exposed secrets
- ✅ Quality checks (file size, patterns)
- ✅ Documentation TOC updates
- ✅ Memory capture of changes

#### On Decisions/Discoveries
- ✅ Auto-capture when you say "decided to", "will use", "choosing"
- ✅ Pattern extraction when discovering conventions
- ✅ Error solutions saved when fixing issues

#### On Task Management
- ✅ Spec folder creation for complex tasks (score ≥ 6)
- ✅ One active task enforcement
- ✅ Progress tracking and suggestions

#### On Communication
- ✅ Conversation buffer after 5 exchanges
- ✅ Context preservation
- ✅ Important decisions highlighted

#### Periodic Tasks
- ✅ Daily documentation validation
- ✅ Memory optimization

### Manual Triggers Available
- 🔧 `/memory search` - Search knowledge base
- 🔧 `/logic help [topic]` - Get specific help
- 🔧 Run any script manually from `.claude/logic/scripts/` and subdirectories

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
2. Run the TOC generator: `python3 .claude/logic/documentation/scripts/add-toc.py`
3. Update relevant README files
4. Add cross-references from related docs
5. Test all links and code examples

---

*Last updated: 2025-01-22*
*Comprehensive automation overview for Claude Code CLI system*