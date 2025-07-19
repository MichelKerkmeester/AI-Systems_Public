# Hook Documentation

This directory contains comprehensive documentation for all hooks in the Claude Code system.

## Table of Contents

### Core Hooks
- [Context Management Hook](./context-management-hook.md) - Auto-saves context state
- [Doc Update Hook](./doc-update-hook.md) - Updates documentation on changes
- [Mode Suggestion Hook](./mode-suggestion-hook.md) - Suggests mode changes
- [Parallel Agent Hook](./parallel-agent-hook.md) - Manages parallel agents
- [Pattern Extraction Hook](./pattern-extraction-hook.md) - Extracts patterns with Gemini
- [Query Planning Hook](./query-planning-hook.md) - Creates tasks for complex queries
- [Security Scan Hook](./security-scan-hook.md) - Blocks sensitive operations
- [Task Management Hook](./task-management-hook.md) - Manages task lifecycle
- [Workflow Automation Hook](./workflow-automation-hook.md) - Triggers on complexity

### Specialized Hooks
- [Memory Context Hook](./memory-context-hook.md) - Memory system integration
- [Quality Hook](./quality-hook.md) - Code quality checks
- [Session Hook](./session-hook.md) - Session management

## Hook System Overview

Hooks in Claude Code are automated scripts that run in response to specific events. They enable the system to react intelligently to user actions without manual intervention.

### Hook Types

1. **UserPromptSubmit Hooks** - Run when the user submits a prompt
2. **PreToolUse Hooks** - Run before a tool is executed
3. **PostToolUse Hooks** - Run after a tool completes
4. **Tool-Specific Hooks** - Run for specific tools (e.g., TodoWrite)

### Hook Priority System

Hooks execute in priority order (1 = highest):
- Priority 1: Security and critical checks
- Priority 2: Quality and validation
- Priority 3: Workflow and automation
- Priority 4: Context and patterns
- Priority 5: Suggestions and UI

### Performance Guidelines

- Each hook should execute in < 100ms
- Total hook execution time should be < 300ms
- Use caching where possible
- Avoid blocking operations

### Creating New Hooks

See the [Hook Development Guide](./hook-development-guide.md) for instructions on creating new hooks.