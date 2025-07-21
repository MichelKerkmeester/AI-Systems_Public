# Hooks reference

## Table of Contents

- [Configuration](#configuration)
  - [Structure](#structure)
- [Hook Events](#hook-events)
  - [PreToolUse](#pretooluse)
  - [PostToolUse](#posttooluse)
  - [Notification](#notification)
  - [UserPromptSubmit](#userpromptsubmit)
  - [Stop](#stop)
  - [SubagentStop](#subagentstop)
  - [PreCompact](#precompact)
- [Hook Input](#hook-input)
  - [PreToolUse Input](#pretooluse-input)
  - [PostToolUse Input](#posttooluse-input)
  - [Notification Input](#notification-input)
  - [UserPromptSubmit Input](#userpromptsubmit-input)
  - [Stop and SubagentStop Input](#stop-and-subagentstop-input)
  - [PreCompact Input](#precompact-input)
- [Hook Output](#hook-output)
  - [Simple: Exit Code](#simple-exit-code)
    - [Exit Code 2 Behavior](#exit-code-2-behavior)
  - [Advanced: JSON Output](#advanced-json-output)
    - [Common JSON Fields](#common-json-fields)
    - [`PreToolUse` Decision Control](#pretooluse-decision-control)
    - [`PostToolUse` Decision Control](#posttooluse-decision-control)
    - [`UserPromptSubmit` Decision Control](#userpromptsubmit-decision-control)
    - [`Stop`/`SubagentStop` Decision Control](#stopsubagentstop-decision-control)
    - [JSON Output Example: Bash Command Editing](#json-output-example-bash-command-editing)
    - [UserPromptSubmit Example: Adding Context and Validation](#userpromptsubmit-example-adding-context-and-validation)
- [Working with MCP Tools](#working-with-mcp-tools)
  - [MCP Tool Naming](#mcp-tool-naming)
  - [Configuring Hooks for MCP Tools](#configuring-hooks-for-mcp-tools)
- [Examples](#examples)
- [Security Considerations](#security-considerations)
  - [Disclaimer](#disclaimer)
  - [Security Best Practices](#security-best-practices)
  - [Configuration Safety](#configuration-safety)
- [Hook Execution Details](#hook-execution-details)
- [Debugging](#debugging)
  - [Basic Troubleshooting](#basic-troubleshooting)
  - [Advanced Debugging](#advanced-debugging)
  - [Debug Output Example](#debug-output-example)
- [Multi-Agent Concurrency Support](#multi-agent-concurrency-support)
  - [Hook Concurrency Metadata](#hook-concurrency-metadata)
  - [Agent-Aware Hook Execution](#agent-aware-hook-execution)
  - [Parallel Execution Commands](#parallel-execution-commands)
  - [Hook Implementation for Multi-Agent](#hook-implementation-for-multi-agent)
  - [Conflict Resolution](#conflict-resolution)
  - [Resource Limits](#resource-limits)
  - [Example: Parallel-Safe Hook](#example-parallel-safe-hook)
  - [Performance Optimization](#performance-optimization)
  - [Monitoring & Debugging](#monitoring-debugging)
- [Command System Refactoring - New Hook Specifications](#command-system-refactoring---new-hook-specifications)
  - [Overview](#overview)
  - [New Hooks Implemented](#new-hooks-implemented)
    - [1. workflow-automation-hook.py](#1-workflow-automation-hookpy)
    - [2. security-scan-hook.py](#2-security-scan-hookpy)
    - [3. context-management-hook.py](#3-context-management-hookpy)
    - [4. pattern-extraction-hook.py (Enhanced)](#4-pattern-extraction-hookpy-enhanced)
    - [5. task-management-hook.py](#5-task-management-hookpy)
    - [6. parallel-agent-hook.py](#6-parallel-agent-hookpy)
  - [Hook Integration with Commands](#hook-integration-with-commands)
  - [Performance Metrics](#performance-metrics)
  - [Hook Management](#hook-management)
  - [Multi-Agent Considerations](#multi-agent-considerations)
  - [Future Enhancements](#future-enhancements)
> This page provides reference documentation for implementing hooks in Claude Code.

<Tip>
  For a quickstart guide with examples, see [Get started with Claude Code hooks](https://docs.anthropic.com/en/docs/claude-code/hooks).
</Tip>

## Configuration

Claude Code hooks are configured in your
[settings files](https://docs.anthropic.com/en/docs/claude-code/settings):

* `~/.claude/settings.json` - User settings
* `.claude/settings.json` - Project settings
* `.claude/settings.local.json` - Local project settings (not committed)
* Enterprise managed policy settings

### Structure

Hooks are organized by matchers, where each matcher can have multiple hooks:

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

* **matcher**: Pattern to match tool names, case-sensitive (only applicable for
  `PreToolUse` and `PostToolUse`)
  * Simple strings match exactly: `Write` matches only the Write tool
  * Supports regex: `Edit|Write` or `Notebook.*`
  * If omitted or empty string, hooks run for all matching events
* **hooks**: Array of commands to execute when the pattern matches
  * `type`: Currently only `"command"` is supported
  * `command`: The bash command to execute
  * `timeout`: (Optional) How long a command should run, in seconds, before
    canceling that specific command.

For events like `UserPromptSubmit`, `Notification`, `Stop`, and `SubagentStop` that don't use matchers, you can omit the matcher field:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/prompt-validator.py"
          }
        ]
      }
    ]
  }
}
```

<Warning>
  `"matcher": "*"` is invalid. Instead, omit "matcher" or use `"matcher": ""`.
</Warning>

## Hook Events

### PreToolUse

Runs after Claude creates tool parameters and before processing the tool call.

**Common matchers:**

* `Task` - Agent tasks
* `Bash` - Shell commands
* `Glob` - File pattern matching
* `Grep` - Content search
* `Read` - File reading
* `Edit`, `MultiEdit` - File editing
* `Write` - File writing
* `WebFetch`, `WebSearch` - Web operations

### PostToolUse

Runs immediately after a tool completes successfully.

Recognizes the same matcher values as PreToolUse.

### Notification

Runs when Claude Code sends notifications. Notifications are sent when:

1. Claude needs your permission to use a tool. Example: "Claude needs your permission to use Bash"
2. The prompt input has been idle for at least 60 seconds. "Claude is waiting for your input"

### UserPromptSubmit

Runs when the user submits a prompt, before Claude processes it. This allows you to add additional context based on the prompt/conversation, validate prompts, or block certain types of prompts.

### Stop

Runs when the main Claude Code agent has finished responding. Does not run if the stoppage occurred due to a user interrupt.

### SubagentStop

Runs when a Claude Code subagent (Task tool call) has finished responding.

### PreCompact

Runs before Claude Code is about to run a compact operation.

**Matchers:**

* `manual` - Invoked from `/compact`
* `auto` - Invoked from auto-compact (due to full context window)

## Hook Input

Hooks receive JSON data via stdin containing session information and
event-specific data:

```typescript
{
  // Common fields
  session_id: string
  transcript_path: string  // Path to conversation JSON
  cwd: string              // The current working directory when the hook is invoked

  // Event-specific fields
  hook_event_name: string
  ...
}
```

### PreToolUse Input

The exact schema for `tool_input` depends on the tool.

```json
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  }
}
```

### PostToolUse Input

The exact schema for `tool_input` and `tool_response` depends on the tool.

```json
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "PostToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content"
  },
  "tool_response": {
    "filePath": "/path/to/file.txt",
    "success": true
  }
}
```

### Notification Input

```json
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "Notification",
  "message": "Task completed successfully"
}
```

### UserPromptSubmit Input

```json
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Write a function to calculate the factorial of a number"
}
```

### Stop and SubagentStop Input

`stop_hook_active` is true when Claude Code is already continuing as a result of
a stop hook. Check this value or process the transcript to prevent Claude Code
from running indefinitely.

```json
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "Stop",
  "stop_hook_active": true
}
```

### PreCompact Input

For `manual`, `custom_instructions` comes from what the user passes into
`/compact`. For `auto`, `custom_instructions` is empty.

```json
{
  "session_id": "abc123",
  "transcript_path": "~/.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "hook_event_name": "PreCompact",
  "trigger": "manual",
  "custom_instructions": ""
}
```

## Hook Output

There are two ways for hooks to return output back to Claude Code. The output
communicates whether to block and any feedback that should be shown to Claude
and the user.

### Simple: Exit Code

Hooks communicate status through exit codes, stdout, and stderr:

* **Exit code 0**: Success. `stdout` is shown to the user in transcript mode
  (CTRL-R).
* **Exit code 2**: Blocking error. `stderr` is fed back to Claude to process
  automatically. See per-hook-event behavior below.
* **Other exit codes**: Non-blocking error. `stderr` is shown to the user and
  execution continues.

<Warning>
  Reminder: Claude Code does not see stdout if the exit code is 0.
</Warning>

#### Exit Code 2 Behavior

| Hook Event         | Behavior                                                           |
| ------------------ | ------------------------------------------------------------------ |
| `PreToolUse`       | Blocks the tool call, shows stderr to Claude                       |
| `PostToolUse`      | Shows stderr to Claude (tool already ran)                          |
| `Notification`     | N/A, shows stderr to user only                                     |
| `UserPromptSubmit` | Blocks prompt processing, erases prompt, shows stderr to user only |
| `Stop`             | Blocks stoppage, shows stderr to Claude                            |
| `SubagentStop`     | Blocks stoppage, shows stderr to Claude subagent                   |
| `PreCompact`       | N/A, shows stderr to user only                                     |

### Advanced: JSON Output

Hooks can return structured JSON in `stdout` for more sophisticated control:

#### Common JSON Fields

All hook types can include these optional fields:

```json
{
  "continue": true, // Whether Claude should continue after hook execution (default: true)
  "stopReason": "string" // Message shown when continue is false
  "suppressOutput": true, // Hide stdout from transcript mode (default: false)
}
```

If `continue` is false, Claude stops processing after the hooks run.

* For `PreToolUse`, this is different from `"decision": "block"`, which only
  blocks a specific tool call and provides automatic feedback to Claude.
* For `PostToolUse`, this is different from `"decision": "block"`, which
  provides automated feedback to Claude.
* For `UserPromptSubmit`, this prevents the prompt from being processed.
* For `Stop` and `SubagentStop`, this takes precedence over any
  `"decision": "block"` output.
* In all cases, `"continue" = false` takes precedence over any
  `"decision": "block"` output.

`stopReason` accompanies `continue` with a reason shown to the user, not shown
to Claude.

#### `PreToolUse` Decision Control

`PreToolUse` hooks can control whether a tool call proceeds.

* "approve" bypasses the permission system. `reason` is shown to the user but
  not to Claude.
* "block" prevents the tool call from executing. `reason` is shown to Claude.
* `undefined` leads to the existing permission flow. `reason` is ignored.

```json
{
  "decision": "approve" | "block" | undefined,
  "reason": "Explanation for decision"
}
```

#### `PostToolUse` Decision Control

`PostToolUse` hooks can control whether a tool call proceeds.

* "block" automatically prompts Claude with `reason`.
* `undefined` does nothing. `reason` is ignored.

```json
{
  "decision": "block" | undefined,
  "reason": "Explanation for decision"
}
```

#### `UserPromptSubmit` Decision Control

`UserPromptSubmit` hooks can control whether a user prompt is processed.

* `"block"` prevents the prompt from being processed. The submitted prompt is erased from context. `"reason"` is shown to the user but not added to context.
* `undefined` allows the prompt to proceed normally. `"reason"` is ignored.

```json
{
  "decision": "block" | undefined,
  "reason": "Explanation for decision"
}
```

#### `Stop`/`SubagentStop` Decision Control

`Stop` and `SubagentStop` hooks can control whether Claude must continue.

* "block" prevents Claude from stopping. You must populate `reason` for Claude
  to know how to proceed.
* `undefined` allows Claude to stop. `reason` is ignored.

```json
{
  "decision": "block" | undefined,
  "reason": "Must be provided when Claude is blocked from stopping"
}
```

#### JSON Output Example: Bash Command Editing

```python
#!/usr/bin/env python3
import json
import re
import sys

# Define validation rules as a list of (regex pattern, message) tuples
VALIDATION_RULES = [
    (
        r"\bgrep\b(?!.*\|)",
        "Use 'rg' (ripgrep) instead of 'grep' for better performance and features",
    ),
    (
        r"\bfind\s+\S+\s+-name\b",
        "Use 'rg --files | rg pattern' or 'rg --files -g pattern' instead of 'find -name' for better performance",
    ),
]


def validate_command(command: str) -> list[str]:
    issues = []
    for pattern, message in VALIDATION_RULES:
        if re.search(pattern, command):
            issues.append(message)
    return issues


try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})
command = tool_input.get("command", "")

if tool_name != "Bash" or not command:
    sys.exit(1)

# Validate the command
issues = validate_command(command)

if issues:
    for message in issues:
        print(f"• {message}", file=sys.stderr)
    # Exit code 2 blocks tool call and shows stderr to Claude
    sys.exit(2)
```

#### UserPromptSubmit Example: Adding Context and Validation

```python
#!/usr/bin/env python3
import json
import sys
import re
import datetime

# Load input from stdin
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
    sys.exit(1)

prompt = input_data.get("prompt", "")

# Check for sensitive patterns
sensitive_patterns = [
    (r"(?i)\b(password|secret|key|token)\s*[:=]", "Prompt contains potential secrets"),
]

for pattern, message in sensitive_patterns:
    if re.search(pattern, prompt):
        # Use JSON output to block with a specific reason
        output = {
            "decision": "block",
            "reason": f"Security policy violation: {message}. Please rephrase your request without sensitive information."
        }
        print(json.dumps(output))
        sys.exit(0)

# Add current time to context
context = f"Current time: {datetime.datetime.now()}"
print(context)

# Allow the prompt to proceed with the additional context
sys.exit(0)
```

## Working with MCP Tools

Claude Code hooks work seamlessly with
[Model Context Protocol (MCP) tools](https://docs.anthropic.com/en/docs/claude-code/mcp). When MCP servers
provide tools, they appear with a special naming pattern that you can match in
your hooks.

### MCP Tool Naming

MCP tools follow the pattern `mcp__<server>__<tool>`, for example:

* `mcp__memory__create_entities` - Memory server's create entities tool
* `mcp__filesystem__read_file` - Filesystem server's read file tool
* `mcp__github__search_repositories` - GitHub server's search tool

### Configuring Hooks for MCP Tools

You can target specific MCP tools or entire MCP servers:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Memory operation initiated' >> ~/mcp-operations.log"
          }
        ]
      },
      {
        "matcher": "mcp__.*__write.*",
        "hooks": [
          {
            "type": "command",
            "command": "/home/user/scripts/validate-mcp-write.py"
          }
        ]
      }
    ]
  }
}
```

## Examples

<Tip>
  For practical examples including code formatting, notifications, and file protection, see [More Examples](https://docs.anthropic.com/en/docs/claude-code/hooks) in the get started guide.
</Tip>

## Security Considerations

### Disclaimer

**USE AT YOUR OWN RISK**: Claude Code hooks execute arbitrary shell commands on
your system automatically. By using hooks, you acknowledge that:

* You are solely responsible for the commands you configure
* Hooks can modify, delete, or access any files your user account can access
* Malicious or poorly written hooks can cause data loss or system damage
* Anthropic provides no warranty and assumes no liability for any damages
  resulting from hook usage
* You should thoroughly test hooks in a safe environment before production use

Always review and understand any hook commands before adding them to your
configuration.

### Security Best Practices

Here are some key practices for writing more secure hooks:

1. **Validate and sanitize inputs** - Never trust input data blindly
2. **Always quote shell variables** - Use `"$VAR"` not `$VAR`
3. **Block path traversal** - Check for `..` in file paths
4. **Use absolute paths** - Specify full paths for scripts
5. **Skip sensitive files** - Avoid `.env`, `.git/`, keys, etc.

### Configuration Safety

Direct edits to hooks in settings files don't take effect immediately. Claude
Code:

1. Captures a snapshot of hooks at startup
2. Uses this snapshot throughout the session
3. Warns if hooks are modified externally
4. Requires review in `/hooks` menu for changes to apply

This prevents malicious hook modifications from affecting your current session.

## Hook Execution Details

* **Timeout**: 60-second execution limit by default, configurable per command.
  * A timeout for an individual command does not affect the other commands.
* **Parallelization**: All matching hooks run in parallel
* **Environment**: Runs in current directory with Claude Code's environment
* **Input**: JSON via stdin
* **Output**:
  * PreToolUse/PostToolUse/Stop: Progress shown in transcript (Ctrl-R)
  * Notification: Logged to debug only (`--debug`)

## Debugging

### Basic Troubleshooting

If your hooks aren't working:

1. **Check configuration** - Run `/hooks` to see if your hook is registered
2. **Verify syntax** - Ensure your JSON settings are valid
3. **Test commands** - Run hook commands manually first
4. **Check permissions** - Make sure scripts are executable
5. **Review logs** - Use `claude --debug` to see hook execution details

Common issues:

* **Quotes not escaped** - Use `\"` inside JSON strings
* **Wrong matcher** - Check tool names match exactly (case-sensitive)
* **Command not found** - Use full paths for scripts

### Advanced Debugging

For complex hook issues:

1. **Inspect hook execution** - Use `claude --debug` to see detailed hook execution
2. **Validate JSON schemas** - Test hook input/output with external tools
3. **Check environment variables** - Verify Claude Code's environment is correct
4. **Test edge cases** - Try hooks with unusual file paths or inputs
5. **Monitor system resources** - Check for resource exhaustion during hook execution
6. **Use structured logging** - Implement logging in your hook scripts

### Debug Output Example

Use `claude --debug` to see hook execution details:

```
[DEBUG] Executing hooks for PostToolUse:Write
[DEBUG] Getting matching hook commands for PostToolUse with query: Write
[DEBUG] Found 1 hook matchers in settings
[DEBUG] Matched 1 hooks for query "Write"
[DEBUG] Found 1 hook commands to execute
[DEBUG] Executing hook command: <Your command> with timeout 60000ms
[DEBUG] Hook command completed with status 0: <Your stdout>
```

Progress messages appear in transcript mode (Ctrl-R) showing:

* Which hook is running
* Command being executed
* Success/failure status
* Output or error messages

## Multi-Agent Concurrency Support

Claude Code hooks now support safe concurrent execution across multiple Claude agents running in separate terminals. This enables parallel development of work packages with automatic coordination.

### Hook Concurrency Metadata

Hooks can declare their concurrency capabilities through metadata:

```python
class HookMetadata:
    name: str                           # Hook identifier
    priority: int                       # Execution priority (1=highest)
    concurrent_safe: bool = True        # Can multiple agents run simultaneously
    exclusive_resources: List[str] = [] # Resources requiring exclusive access
    max_parallel: int = None            # Max parallel executions (None = unlimited)
```

### Agent-Aware Hook Execution

When multiple agents are active, the hook infrastructure:

1. **Automatic Agent ID**: Each Claude instance gets a unique agent ID
2. **Distributed Locking**: File-based locks prevent resource conflicts
3. **Priority Queuing**: Hooks execute in priority order with deduplication
4. **Resource Management**: Monitors CPU/memory usage per agent

### Parallel Execution Commands

Use the `/logic tasks parallel` commands to manage multi-agent execution:

```bash
# Start parallel agents for work packages
/logic tasks parallel start wp1,wp2,wp3

# Monitor agent status
/logic tasks parallel status

# View agent logs
/logic tasks parallel logs agent-id

# Merge completed work
/logic tasks parallel merge agent-id
```

### Hook Implementation for Multi-Agent

Hooks receive agent context in their input:

```json
{
  "session_id": "abc123",
  "hook_event_name": "PostToolUse",
  "agent_id": "claude-wp1-a1b2c3d4",
  "agent_context": {
    "work_package": "wp1-hooks",
    "agent_type": "development",
    "parallel_group": 1
  }
}
```

### Conflict Resolution

The system automatically handles conflicts when multiple agents access the same resource:

| Conflict Type | Resolution Strategy |
|--------------|-------------------|
| File Edit | Optimistic locking with version checking |
| Git Operation | Sequential queue with operation ordering |
| Task Assignment | First agent wins, others queued |
| Hook Execution | Priority-based with concurrency metadata |
| Memory Update | Transaction-based with rollback |

### Resource Limits

Per-agent resource limits prevent system exhaustion:

```json
{
  "memory_mb": 512,        // Max memory per agent
  "cpu_percent": 25.0,     // Max CPU percentage
  "open_files": 100,       // Max file handles
  "disk_write_mb_per_min": 100  // Write rate limit
}
```

### Example: Parallel-Safe Hook

```python
#!/usr/bin/env python3
from shared import HookBase, DistributedLockManager

class MyParallelHook(HookBase):
    def __init__(self):
        super().__init__()
        # Declare concurrency metadata
        self.metadata = {
            "concurrent_safe": True,
            "max_parallel": 5,
            "exclusive_resources": []
        }
        
    def process(self, request_data, project_context):
        # Get agent context
        agent_id = request_data.get("agent_id", "default")
        
        # Use distributed lock for shared resources
        lock_manager = DistributedLockManager(agent_id)
        with lock_manager.atomic_file_operation("shared-config.json"):
            # Safe concurrent file access
            self.update_shared_config()
        
        return {"status": "success"}
```

### Performance Optimization

Multi-agent hooks benefit from:

1. **Shared Cache**: Agent-local caches with global invalidation
2. **Lazy Loading**: Hook modules loaded on-demand
3. **Batch Operations**: Grouped file operations reduce I/O
4. **Background Processing**: Predictable triggers pre-computed

### Monitoring & Debugging

Monitor multi-agent execution:

```bash
# Real-time agent status
/logic agents status

# Resource usage by agent
/logic agents monitor

# Agent-specific logs
/logic agents logs [agent-id]

# Emergency cleanup
/logic agents emergency clean
```

Debug output includes agent context:

```
[DEBUG] Agent claude-wp1-a1b2c3d4 executing hook: quality-hook
[DEBUG] Acquiring lock for resource: git
[DEBUG] Lock acquired, executing hook command
[DEBUG] Hook completed, releasing lock
```

## Command System Refactoring - New Hook Specifications

### Overview

The command system refactoring introduced several new automated hooks that replace manual commands, reducing the command set from 10+ to just 3 (`/memory`, `/save`, `/logic`).

### New Hooks Implemented

#### 1. workflow-automation-hook.py

**Purpose**: Automatically triggers Sequential Thinking for complex tasks

**Location**: `.claude/hooks/core/workflow-automation-hook.py`

**Triggers**:
- Query complexity score > 3
- Multiple steps detected in user request
- 3+ distinct actions mentioned

**Configuration**:
```json
{
  "enabled": true,
  "complexity_threshold": 3,
  "keywords": ["refactor", "implement", "design", "architecture"],
  "min_steps": 3
}
```

**Priority**: WORKFLOW (3)

**Performance**: ~2ms detection time

#### 2. security-scan-hook.py

**Purpose**: Blocks operations that might expose sensitive data

**Location**: `.claude/hooks/core/security-scan-hook.py`

**Triggers**:
- File write operations
- Bash commands
- Environment variable access

**Patterns Detected**:
- API keys (sk-, pk-, api_key)
- AWS credentials
- Private keys
- Passwords in plain text
- OAuth tokens

**Configuration**:
```json
{
  "enabled": true,
  "block_on_detection": true,
  "scan_patterns": {
    "api_keys": ["sk-", "pk-", "api_key", "API_KEY"],
    "aws": ["AKIA", "aws_access_key"],
    "secrets": ["password", "secret", "token"]
  }
}
```

**Priority**: CRITICAL (1)

**Performance**: ~10ms scan time

#### 3. context-management-hook.py

**Purpose**: Automatically saves context at regular intervals

**Location**: `.claude/hooks/core/context-management-hook.py`

**Triggers**:
- Every 5 minutes
- After 10 file operations
- On significant state changes

**Features**:
- Incremental context updates
- State persistence
- Recovery mechanism

**Configuration**:
```json
{
  "enabled": true,
  "time_interval": 300,
  "operation_threshold": 10,
  "auto_save": true
}
```

**Priority**: CONTEXT (4)

**Performance**: ~5ms check time

#### 4. pattern-extraction-hook.py (Enhanced)

**Purpose**: Extracts patterns, facts, and constraints from sessions

**Location**: `.claude/hooks/core/pattern-extraction-hook.py`

**Triggers**:
- Session save operations
- Significant file changes (5+ files or 100+ lines)
- Memory capture events

**Features**:
- Enhanced regex extraction
- Gemini integration (when available)
- Automatic knowledge file updates
- Duplicate prevention

**Configuration**:
```json
{
  "enabled": true,
  "auto_extract": true,
  "min_content_length": 100,
  "gemini_integration": {
    "enabled": true,
    "model": "gemini-2.0-flash-thinking-exp"
  }
}
```

**Priority**: PATTERN (5)

**Performance**: ~50ms with enhanced extraction

#### 5. task-management-hook.py

**Purpose**: Monitors task lifecycle and suggests task state changes

**Location**: `.claude/hooks/core/task-management-hook.py`

**Triggers**:
- TodoWrite operations
- Task completion (100% progress)
- High-priority task detection

**Features**:
- Automatic task suggestions
- Progress tracking
- Task pattern extraction
- Single active task enforcement

**Configuration**:
```json
{
  "enabled": true,
  "auto_suggest": true,
  "high_priority_keywords": ["urgent", "critical", "fix", "bug"],
  "completion_threshold": 100
}
```

**Priority**: CONTEXT (4)

**Performance**: ~15ms processing time

#### 6. parallel-agent-hook.py

**Purpose**: Suggests parallel execution for multi-package work

**Location**: `.claude/hooks/core/parallel-agent-hook.py`

**Triggers**:
- Multiple high-priority todos
- Work package mentions
- Large refactoring tasks

**Features**:
- Work distribution analysis
- Time savings estimation
- Dependency detection
- Agent type suggestions

**Configuration**:
```json
{
  "enabled": true,
  "min_tasks_for_parallel": 2,
  "time_savings_threshold": 0.3,
  "max_agents": 10
}
```

**Priority**: WORKFLOW (3)

**Performance**: ~20ms analysis time

### Hook Integration with Commands

| Old Command | New Hook | Automation Level |
|-------------|----------|------------------|
| `/workflow` | workflow-automation-hook | Fully Automated |
| `/test` | Enhanced quality-hook | Fully Automated |
| `/security` | security-scan-hook | Fully Automated |
| `/context` | context-management-hook | Fully Automated |
| `/notebook` | pattern-extraction-hook | Fully Automated |
| `/pr` | documentation-generation-hook | Semi-Automated |

### Performance Metrics

Total hook execution target: **< 300ms**

Typical execution times:
- Security scan: ~10ms
- Context check: ~5ms
- Workflow detection: ~2ms
- Pattern extraction: ~50ms
- Task management: ~15ms
- Parallel analysis: ~20ms

**Total typical: ~102ms** ✅

### Hook Management

Control hooks via `/logic hooks`:

```bash
# List all hooks and status
/logic hooks list

# Enable/disable specific hooks
/logic hooks enable workflow-automation
/logic hooks disable pattern-extraction

# View hook statistics
/logic hooks status

# Reset hook state
/logic hooks reset [hook-name]
```

### Multi-Agent Considerations

All new hooks support multi-agent concurrency:

1. **Workflow Automation**: Concurrent-safe, unlimited parallel
2. **Security Scan**: Exclusive access to scan results
3. **Context Management**: Agent-specific contexts
4. **Pattern Extraction**: Shared knowledge with locking
5. **Task Management**: Distributed task assignment
6. **Parallel Agent**: Orchestration coordination

### Future Enhancements

- Enhanced process monitoring for hook execution
- Real-time output streaming
- Performance profiling
- Auto-recovery mechanisms
