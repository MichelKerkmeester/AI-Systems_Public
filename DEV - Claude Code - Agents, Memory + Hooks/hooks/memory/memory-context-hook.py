#!/usr/bin/env python3
"""
Memory Context Hook for Claude Code
Simplified version that works with Graphiti MCP server
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any, Tuple, Optional

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared import HookBase, UserPromptHook


class MemoryContextHook(UserPromptHook):
    """Simplified memory context hook for Graphiti integration"""
    
    def __init__(self):
        super().__init__()
        # Note: This hook now serves as a reminder to use memory features
        # Actual memory operations are handled by Graphiti MCP tools
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook input - currently just provides memory usage hints"""
        user_input = hook_input.get('user_input', '').lower()
        
        # Skip for certain commands
        skip_patterns = ['/memory', '/test', '/workflow', '/mode', '/pr', '/security']
        if any(user_input.strip().startswith(cmd) for cmd in skip_patterns):
            return 0, None
        
        # Check for memory-related keywords
        memory_keywords = ['remember', 'recall', 'memory', 'previous', 'earlier', 'last time', 'before']
        
        if any(keyword in user_input for keyword in memory_keywords):
            hint = "\n💡 Memory Hint: Use `/memory search <query>` to search the knowledge graph\n"
            return 0, hint
        
        # For now, return no output until Graphiti is properly connected
        return 0, None


# Main entry point
if __name__ == "__main__":
    hook = MemoryContextHook()
    hook.run()