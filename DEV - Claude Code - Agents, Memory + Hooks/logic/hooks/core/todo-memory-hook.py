#!/usr/bin/env python3
"""
TodoWrite Memory Hook for Claude Code
Enforces mandatory memory operations with TodoWrite tool:
- Before task start: Mandatory memory search
- After completion: Capture task outcome
- Non-blocking execution
"""

import sys
from pathlib import Path
from typing import Dict, Any

# Add parent directories to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from shared.hook_base import ToolHook
from shared.hook_formatters import format_info_box
from shared.hook_priority import HookPriority
from tasks.task_memory_integration import TodoWriteMemoryHandler


class TodoMemoryHook(ToolHook):
    """Hook that enforces memory operations with TodoWrite"""
    
    def __init__(self):
        super().__init__(
            name="TodoMemoryHook",
            priority=HookPriority.CRITICAL  # Run before other hooks
        )
        self.handler = TodoWriteMemoryHandler()
        self._last_todos = None
    
    def can_handle(self, request_data: dict) -> bool:
        """Check if this is a TodoWrite operation"""
        return request_data.get("name") == "TodoWrite"
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        """Process TodoWrite operations with memory integration"""
        todos = request_data.get("arguments", {}).get("todos", [])
        
        if not todos:
            return {
                "hook": self.name,
                "continue": True
            }
        
        # Pre-execution memory operations
        result = self.handler.before_todo_write(todos)
        
        # Store todos for post-execution
        self._last_todos = todos
        
        # Build response
        response = {
            "hook": self.name,
            "continue": True,
            "memory_operations": result
        }
        
        # Add enforcement message if search wasn't performed
        if not result.get("memory_search_performed"):
            response["guidance"] = format_info_box(
                "⚠️ MEMORY SEARCH REQUIRED",
                [
                    "Memory search is MANDATORY before starting new tasks!",
                    "This ensures you don't duplicate work or miss existing solutions.",
                    "",
                    "The system will search memories automatically, but failed this time.",
                    "Please ensure the task has clear content for keyword extraction."
                ],
                style="warning"
            )
        
        # Add informational message about what happened
        elif result.get("memories_found", 0) > 0:
            relevant_count = len(result.get("relevant_memories", []))
            
            lines = [
                f"✅ Searched {result['memories_found']} memories",
                f"📚 Found {relevant_count} relevant memories"
            ]
            
            # Add top relevant memories
            for i, memory in enumerate(result.get("relevant_memories", [])[:3], 1):
                lines.append(f"{i}. {memory['name'][:50]}... (relevance: {memory['relevance']:.2f})")
            
            response["info"] = format_info_box(
                "🔍 Memory Search Complete",
                lines,
                style="success"
            )
        
        return response
    
    def post_process(self, request_data: dict, response_data: dict, project_context: dict) -> dict:
        """Handle post-execution memory capture"""
        if self._last_todos and response_data.get("success", True):
            # Trigger post-execution handler
            self.handler.after_todo_write(self._last_todos, True)
            
            # Check if task was completed
            all_completed = all(t.get("status") == "completed" for t in self._last_todos)
            if all_completed:
                return {
                    "hook": self.name,
                    "info": "📝 Task completion memory scheduled for capture"
                }
        
        # Clear stored todos
        self._last_todos = None
        
        return {"hook": self.name}
    
    def get_stats(self) -> Dict[str, Any]:
        """Get hook statistics"""
        base_stats = super().get_stats()
        memory_stats = self.handler.get_stats()
        
        return {
            **base_stats,
            "memory_operations": memory_stats
        }
    
    def shutdown(self):
        """Clean shutdown"""
        self.handler.shutdown()
        super().shutdown()


# Export hook instance
hook = TodoMemoryHook()