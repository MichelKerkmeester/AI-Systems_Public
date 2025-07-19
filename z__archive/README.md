# Archive Directory

This directory contains deprecated documentation and files from the old command system.

## Contents

### old-docs/
Documentation for deprecated commands that are now automated via hooks:
- `workflow.md` - Old /workflow command (now automatic via Sequential Thinking)
- `test.md` - Old /test command (now automatic after file changes)
- `security.md` - Old /security command (now automatic on sensitive patterns)
- `context.md` - Old /context command (now automatic tracking)
- `mode.md` - Old /mode command (now automatic suggestions)
- `pr.md` - Old /pr command (now automatic on git operations)
- `notebook.md` - Old /notebook command (now automatic pattern extraction)

## Migration Guide

See `/logic help migration` or `.claude/docs/logic-help/migration.md` for how to use the new system.

## Why Archived?

These commands were replaced by intelligent automation hooks that:
- Detect when functionality is needed
- Run automatically based on context
- Reduce cognitive load
- Improve consistency

The new system uses just 3 commands:
- `/memory` - Knowledge management
- `/save` - Session management
- `/logic` - System control & help

Everything else runs automatically!