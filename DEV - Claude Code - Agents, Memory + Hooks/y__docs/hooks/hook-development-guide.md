# Hook Development Guide

## Overview

This guide explains how to create custom hooks for Claude Code, extending its automation capabilities to match your specific workflow needs.

## Table of Contents

1. [Hook Architecture](#hook-architecture)
2. [Creating a New Hook](#creating-a-new-hook)
3. [Hook Types](#hook-types)
4. [Best Practices](#best-practices)
5. [Testing Hooks](#testing-hooks)
6. [Debugging](#debugging)

## Hook Architecture

### Base Classes

All hooks inherit from base classes in `/hooks/shared/`:

```python
from shared import HookBase      # For all hooks
from shared import ToolHook      # For tool-specific hooks
from shared import UserPromptHook # For prompt analysis
```

### Hook Lifecycle

```
1. Registration (settings.json)
     ↓
2. Initialization (__init__)
     ↓
3. Can Handle Check (can_handle)
     ↓
4. Process Request (process)
     ↓
5. Return Result
```

## Creating a New Hook

### Step 1: Choose Hook Type

```python
# For UserPromptSubmit events
class MyPromptHook(UserPromptHook):
    def process_user_prompt(self, prompt: str) -> Tuple[int, Optional[str]]:
        pass

# For tool operations
class MyToolHook(ToolHook):
    def can_handle(self, request_data: dict) -> bool:
        pass
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        pass
```

### Step 2: Implement Core Methods

```python
#!/usr/bin/env python3
"""
My Custom Hook
Purpose: Describe what your hook does
"""

import sys
from pathlib import Path
from typing import Dict, Any, Optional

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared import ToolHook, MessageFormatter

class MyCustomHook(ToolHook):
    """Custom hook for specific functionality"""
    
    def __init__(self):
        super().__init__()
        self.formatter = MessageFormatter()
        
    def can_handle(self, request_data: dict) -> bool:
        """Determine if this hook should process the request"""
        tool_name = request_data.get("name", "")
        
        # Define your trigger conditions
        if tool_name == "TargetTool":
            return True
            
        return False
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        """Process the request and return results"""
        # Your hook logic here
        
        # Generate output if needed
        output = self.formatter.header("Hook Result", "icon")
        output += self.formatter.section("Details", ["Item 1", "Item 2"])
        output += self.formatter.footer()
        
        return {
            "status": 0,  # 0 = success, 1 = warning, 2 = error
            "output": output  # Optional message to user
        }

if __name__ == "__main__":
    hook = MyCustomHook()
    hook.run()
```

### Step 3: Register in settings.json

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "TargetTool",
        "hooks": [
          {
            "type": "command",
            "command": "python3 '/path/to/my-custom-hook.py'"
          }
        ]
      }
    ]
  }
}
```

## Hook Types

### UserPromptSubmit Hooks

Triggered when user submits a prompt:

```python
class PromptAnalysisHook(UserPromptHook):
    def process_user_prompt(self, prompt: str) -> Tuple[int, Optional[str]]:
        # Analyze prompt
        if "complex" in prompt.lower():
            return 0, "Detected complex task!"
        
        return 0, None  # No output
```

### PreToolUse Hooks

Run before tool execution:

```python
class PreprocessHook(ToolHook):
    def process(self, request_data: dict, project_context: dict) -> dict:
        # Modify request before execution
        args = request_data.get("arguments", {})
        args["modified"] = True
        
        return {"status": 0}
```

### PostToolUse Hooks

Run after tool execution:

```python
class PostProcessHook(ToolHook):
    def process(self, request_data: dict, project_context: dict) -> dict:
        # React to tool results
        if request_data.get("name") == "Write":
            path = request_data["arguments"]["file_path"]
            self.log_file_creation(path)
        
        return {"status": 0}
```

## Best Practices

### 1. Performance

```python
# Good - Early exit
def can_handle(self, request_data: dict) -> bool:
    if request_data.get("name") != "TargetTool":
        return False
    # Further checks only if needed
    
# Bad - Expensive operations in can_handle
def can_handle(self, request_data: dict) -> bool:
    # Don't do heavy processing here
    result = self.expensive_analysis(request_data)
    return result
```

### 2. Error Handling

```python
def process(self, request_data: dict, project_context: dict) -> dict:
    try:
        # Your logic
        result = self.do_something()
        return {"status": 0}
    except Exception as e:
        # Log error but don't crash
        self.logger.error(f"Hook error: {e}")
        return {
            "status": 1,
            "output": "Hook encountered an issue but continued"
        }
```

### 3. State Management

```python
from shared import StateManager

class StatefulHook(ToolHook):
    def __init__(self):
        super().__init__()
        self.state = StateManager(
            self.claude_path / "state" / "my-hook-state.json",
            {"count": 0, "last_run": None}
        )
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        # Update state
        self.state.update({
            "count": self.state.get("count", 0) + 1,
            "last_run": datetime.now().isoformat()
        })
        self.state.save()
```

### 4. Configuration

```python
from shared import SettingsManager

class ConfigurableHook(ToolHook):
    def __init__(self):
        super().__init__()
        self.settings = SettingsManager(
            self.claude_path / "hooks" / "my-hook-settings.json",
            self._get_default_settings()
        )
    
    def _get_default_settings(self) -> Dict[str, Any]:
        return {
            "enabled": True,
            "threshold": 10,
            "patterns": []
        }
```

## Testing Hooks

### Unit Testing

```python
# test_my_hook.py
import unittest
from my_custom_hook import MyCustomHook

class TestMyHook(unittest.TestCase):
    def setUp(self):
        self.hook = MyCustomHook()
    
    def test_can_handle(self):
        request = {"name": "TargetTool"}
        self.assertTrue(self.hook.can_handle(request))
    
    def test_process(self):
        request = {"name": "TargetTool", "arguments": {}}
        result = self.hook.process(request, {})
        self.assertEqual(result["status"], 0)
```

### Integration Testing

```bash
# Test hook directly
echo '{"name": "TargetTool", "arguments": {}}' | python3 my-custom-hook.py

# Test with Claude Code
# 1. Register hook in settings.json
# 2. Trigger the target tool
# 3. Verify hook execution
```

## Debugging

### Logging

```python
import logging

class DebugHook(ToolHook):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        
    def process(self, request_data: dict, project_context: dict) -> dict:
        self.logger.debug(f"Processing: {request_data}")
        # Your logic
        self.logger.info("Hook completed successfully")
```

### Debug Output

```python
def process(self, request_data: dict, project_context: dict) -> dict:
    # Debug information to user
    debug_output = f"Hook Debug:\n"
    debug_output += f"Tool: {request_data.get('name')}\n"
    debug_output += f"Args: {request_data.get('arguments')}\n"
    
    return {
        "status": 0,
        "output": debug_output if self.debug_mode else None
    }
```

### Common Issues

1. **Hook not triggering**
   - Check registration in settings.json
   - Verify matcher pattern
   - Ensure hook file is executable

2. **Import errors**
   - Check sys.path additions
   - Verify shared module location
   - Install missing dependencies

3. **Performance issues**
   - Profile with cProfile
   - Add caching
   - Use async operations

## Advanced Topics

### Async Hooks

```python
import asyncio

class AsyncHook(ToolHook):
    async def async_process(self):
        # Async operations
        await asyncio.sleep(1)
        return "Done"
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        # Run async in sync context
        result = asyncio.run(self.async_process())
        return {"status": 0}
```

### Inter-Hook Communication

```python
# Using shared state
from shared import SharedState

class CommunicatingHook(ToolHook):
    def process(self, request_data: dict, project_context: dict) -> dict:
        # Write to shared state
        SharedState.set("my_hook_data", {"processed": True})
        
        # Read from another hook
        other_data = SharedState.get("other_hook_data", {})
```

## Hook Examples

See the existing hooks for reference:
- [Workflow Automation Hook](./workflow-automation-hook.md) - Complex pattern detection
- [Security Scan Hook](./security-scan-hook.md) - Critical blocking hook
- [Pattern Extraction Hook](./pattern-extraction-hook.md) - External API integration
- [Task Management Hook](./task-management-hook.md) - Multi-trigger handling

## Related Documentation

- [Hook System Overview](./README.md)
- [Settings Configuration](../settings.md)
- [Testing Guide](../testing/hooks.md)