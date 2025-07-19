#!/usr/bin/env python3
"""
Claude Code Bridge for Graphiti Memory
Connects the memory system to Claude's actual execution flow.
"""

import asyncio
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime, timezone

# Since we can't directly modify Claude's internals, this creates
# a wrapper that can be called from CLAUDE.md instructions

class ClaudeMemoryBridge:
    """Bridge between Claude Code and Graphiti memory system"""
    
    def __init__(self):
        self.capture_queue = []
        self.session_memories = []
        self.init_time = datetime.now(timezone.utc)
        
    async def intercept_response(self, response_text: str, context: Dict[str, Any] = None):
        """
        Intercept Claude's responses for memory capture.
        This would be called via CLAUDE.md instructions.
        """
        # Import the integration
        from memory_integration import memory_integration
        
        # Process the response text
        captures = await memory_integration.process_text(response_text, context)
        
        # Handle captures based on automation level
        for capture in captures:
            if capture['action'] == 'capture' and capture.get('auto'):
                # Auto-capture to Graphiti
                await self._send_to_graphiti(capture['data'])
            elif capture['action'] == 'pending':
                # Add to queue for user confirmation
                self.capture_queue.append(capture)
        
        return captures
    
    async def intercept_tool_result(self, tool_name: str, result: Any, context: Dict[str, Any] = None):
        """
        Intercept tool results for memory capture.
        """
        from memory_integration import memory_integration
        
        # Process tool results
        captures = await memory_integration.capture_from_tool_result(tool_name, result, context)
        
        # Send to Graphiti
        for capture in captures:
            await self._send_to_graphiti(capture)
        
        return captures
    
    async def _send_to_graphiti(self, episode_data: Dict[str, Any]):
        """
        Send episode data to Graphiti via MCP tool.
        In practice, this would be called by Claude using the MCP tool.
        """
        # This is a placeholder - in actual use, Claude would call:
        # mcp__graphiti-gemini__add_episode with the episode_data
        
        # For now, log the capture
        self.session_memories.append({
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'data': episode_data
        })
        
        # Update stats
        from memory_integration import memory_integration
        memory_integration.update_stats("auto")
        
        return True
    
    def generate_memory_prompt(self) -> str:
        """
        Generate a prompt snippet for CLAUDE.md to enable memory capture.
        """
        return """
## 🧠 MEMORY CAPTURE HOOKS

After EVERY response that contains any of these patterns, capture to Graphiti:

1. **Auto-Capture Patterns** (Full Auto):
   - DECISION: [architectural decisions]
   - SECURITY: [security updates/fixes]  
   - BREAKING: [breaking changes]

2. **Semi-Auto Patterns** (Prompt for confirmation):
   - RESOLVED: [bug fixes]
   - PATTERN: [new code patterns]
   - OPTIMIZATION: [performance improvements]
   - "Client prefers..." → Update facts.json
   - "API limit..." → Update constraints.json

3. **Tool Result Captures**:
   - Sequential Thinking conclusions
   - Completed TodoWrite tasks
   - Significant file edits

### Memory Command Format:
```
# After detecting a pattern, use:
mcp__graphiti-gemini__add_episode {
  "name": "[Category]: [Brief description]",
  "episode_body": "[Full content]",
  "source": "claude_code_auto",
  "source_description": "Automatic capture from [pattern]",
  "valid_at": "[ISO timestamp]"
}
```

### Automation Level Check:
- Current level is stored in `.claude/logic/memory/settings.json`
- Full Auto: Capture immediately
- Semi Auto: Ask "💭 Capture this to memory? [Y/n]"
- Manual: Only capture on explicit /memory command
"""
    
    def generate_command_handler(self) -> str:
        """
        Generate command handler instructions for CLAUDE.md
        """
        return """
### /memory Command Handler

When user types `/memory [subcommand]`:

1. **`/memory status`** or `/mem`:
   - Read `.claude/logic/memory/stats.json` for statistics
   - Check `.claude/logic/memory/settings.json` for automation level
   - Use `mcp__graphiti-gemini__search` to count total memories
   - Display formatted status

2. **`/memory auto [level]`**:
   - Valid levels: off, manual, semi, full
   - Update `.claude/logic/memory/settings.json`
   - Confirm change to user

3. **`/memory search <query>`**:
   - Call `mcp__graphiti-gemini__search` with query
   - Format and display results

4. **`/memory manual <text>`**:
   - Immediately capture text using `mcp__graphiti-gemini__add_episode`
   - Category: "manual_capture"

5. **`/memory confirm`**:
   - Process any pending captures from semi-auto mode
   - Send all to Graphiti

### Status Display Format:
```
🧠 Memory Status
━━━━━━━━━━━━━━━
Automation: [Semi-Auto 🟡]
Memories: [X] total ([Y] auto, [Z] manual)
Last capture: [time ago]
Pending: [N] awaiting confirmation

Triggers: DECISION:, SECURITY:, BREAKING:, etc.
```
"""
    
    def create_session_summary(self) -> Dict[str, Any]:
        """
        Create a summary of the current session's memories
        """
        return {
            'session_start': self.init_time.isoformat(),
            'session_duration': (datetime.now(timezone.utc) - self.init_time).total_seconds(),
            'memories_captured': len(self.session_memories),
            'pending_captures': len(self.capture_queue),
            'memories': self.session_memories
        }


# Global instance
claude_bridge = ClaudeMemoryBridge()

# Helper function to generate CLAUDE.md updates
def generate_claude_md_updates():
    """Generate the updates needed for CLAUDE.md"""
    bridge = ClaudeMemoryBridge()
    
    updates = f"""
# CLAUDE.md Memory System Updates

Add the following sections to enable automatic memory capture:

{bridge.generate_memory_prompt()}

{bridge.generate_command_handler()}

## Integration Instructions:

1. After every response, check for memory patterns
2. Use automation level from settings.json
3. Call Graphiti MCP tool for captures
4. Update knowledge files when specified
5. Track statistics in stats.json

This enables the memory system to work automatically with minimal manual commands!
"""
    
    return updates


if __name__ == "__main__":
    # Print the updates needed
    print(generate_claude_md_updates())