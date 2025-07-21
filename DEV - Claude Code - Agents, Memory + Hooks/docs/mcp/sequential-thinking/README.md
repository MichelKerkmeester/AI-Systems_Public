# Sequential Thinking MCP Documentation

## Table of Contents

- [Overview](#overview)
  - [Key Features](#key-features)
- [Setup Guide](#setup-guide)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Verification](#verification)
- [Usage Examples](#usage-examples)
  - [Basic Thought Processing](#basic-thought-processing)
  - [Generating Summary](#generating-summary)
  - [Session Management](#session-management)
- [Integration with Hooks](#integration-with-hooks)
  - [Workflow Automation Hook](#workflow-automation-hook)
  - [Custom Hook Integration](#custom-hook-integration)
- [API Reference](#api-reference)
  - [process_thought](#process_thought)
  - [generate_summary](#generate_summary)
  - [clear_history](#clear_history)
  - [export_session](#export_session)
  - [import_session](#import_session)
- [Best Practices](#best-practices)
  - [1. Structured Thinking](#1-structured-thinking)
  - [2. Metadata Usage](#2-metadata-usage)
  - [3. Session Management](#3-session-management)
  - [4. Integration Patterns](#4-integration-patterns)
  - [5. Performance Considerations](#5-performance-considerations)
## Overview

Sequential Thinking MCP provides structured problem-solving capabilities, allowing Claude to break down complex problems into manageable thoughts with metadata tracking.

### Key Features
- Step-by-step reasoning with numbered thoughts
- Metadata tracking (axioms, assumptions, tags)
- Thought export/import for session persistence
- Stage-based thinking (Problem Definition → Research → Analysis → Synthesis → Conclusion)

## Setup Guide

### Installation
Sequential Thinking is pre-installed with Claude Code. No additional setup required.

### Configuration
The MCP is configured in `.claude/settings.json`:
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

### Verification
Test the installation:
```python
# Process a test thought
result = mcp__sequential-thinking__process_thought(
    thought="Testing Sequential Thinking MCP",
    thought_number=1,
    total_thoughts=1,
    next_thought_needed=False,
    stage="Problem Definition"
)
```

## Usage Examples

### Basic Thought Processing
```python
# Start a thinking sequence
mcp__sequential-thinking__process_thought(
    thought="Understanding the user's requirement for a responsive navigation menu",
    thought_number=1,
    total_thoughts=5,
    next_thought_needed=True,
    stage="Problem Definition",
    tags=["ui", "navigation", "responsive"]
)

# Continue with analysis
mcp__sequential-thinking__process_thought(
    thought="The navigation needs to work on mobile (hamburger), tablet (condensed), and desktop (full)",
    thought_number=2,
    total_thoughts=5,
    next_thought_needed=True,
    stage="Research",
    axioms_used=["Mobile-first design", "Progressive enhancement"]
)
```

### Generating Summary
```python
# After completing thoughts
summary = mcp__sequential-thinking__generate_summary()
print(summary["summary"])
print(summary["key_insights"])
```

### Session Management
```python
# Export thinking session
mcp__sequential-thinking__export_session(
    file_path="/path/to/session.json"
)

# Import previous session
mcp__sequential-thinking__import_session(
    file_path="/path/to/session.json"
)

# Clear current session
mcp__sequential-thinking__clear_history()
```

## Integration with Hooks

### Workflow Automation Hook
```python
# In workflow-automation-hook.py
class WorkflowAutomationHook(ToolHook):
    def process(self, request_data, project_context):
        if self._is_complex_task(request_data):
            # Trigger sequential thinking
            return {
                "output": "Complex task detected. Starting sequential thinking...",
                "sequential_thinking": True
            }
```

### Custom Hook Integration
```python
# Example: Design decision hook
def make_design_decision(options):
    # Use sequential thinking for decision
    thoughts = []
    
    # Define the problem
    thoughts.append(mcp__sequential-thinking__process_thought(
        thought=f"Choosing between {len(options)} design options",
        thought_number=1,
        total_thoughts=len(options) + 2,
        next_thought_needed=True,
        stage="Problem Definition"
    ))
    
    # Analyze each option
    for i, option in enumerate(options):
        thoughts.append(mcp__sequential-thinking__process_thought(
            thought=f"Option {i+1}: {option['description']}",
            thought_number=i+2,
            total_thoughts=len(options) + 2,
            next_thought_needed=i < len(options)-1,
            stage="Analysis",
            tags=option.get('tags', [])
        ))
    
    # Synthesize
    summary = mcp__sequential-thinking__generate_summary()
    return summary
```

## API Reference

### process_thought
Process a single thought with metadata.

**Parameters:**
- `thought` (str): The content of the thought
- `thought_number` (int): Sequence number
- `total_thoughts` (int): Expected total thoughts
- `next_thought_needed` (bool): Whether more thoughts follow
- `stage` (str): Current thinking stage
- `tags` (list, optional): Keywords/categories
- `axioms_used` (list, optional): Principles applied
- `assumptions_challenged` (list, optional): Challenged assumptions

**Returns:**
- Analysis of the processed thought

### generate_summary
Generate a summary of the thinking process.

**Returns:**
- Dictionary with summary, key insights, and metadata

### clear_history
Clear the current thinking session.

### export_session
Export session to a file.

**Parameters:**
- `file_path` (str): Path to save the session

### import_session
Import a previous thinking session.

**Parameters:**
- `file_path` (str): Path to the session file

## Best Practices

### 1. Structured Thinking
- Always specify the stage appropriately
- Use consistent numbering for thoughts
- Set `total_thoughts` realistically

### 2. Metadata Usage
- Tag thoughts for easy retrieval
- Document axioms for transparency
- Challenge assumptions explicitly

### 3. Session Management
- Export important thinking sessions
- Clear history between unrelated problems
- Import relevant past sessions for context

### 4. Integration Patterns
- Use for complex problem decomposition
- Trigger from hooks for automated reasoning
- Combine with other MCPs for comprehensive analysis

### 5. Performance Considerations
- Limit thoughts to necessary depth
- Use summaries for long sessions
- Clear history to free memory

---

*See also: [Workflow Automation](../../logic/automation.md) | [MCP Overview](../README.md)*