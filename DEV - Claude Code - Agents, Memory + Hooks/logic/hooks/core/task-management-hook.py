#!/usr/bin/env python3
"""
Task Management Hook for Claude Code
Monitors TodoWrite operations and suggests task lifecycle changes
Also monitors for task document creation and guides proper workflow
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import ToolHook, MessageFormatter
from logic.tasks import TaskManager


class TaskManagementHook(ToolHook):
    """Hook that monitors TodoWrite and manages task lifecycle"""
    
    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()
        self.formatter = MessageFormatter()
    
    def can_handle(self, request_data: dict) -> bool:
        """Check if this is a TodoWrite or task-related file operation"""
        tool_name = request_data.get("name", "")
        
        # Handle TodoWrite operations
        if tool_name == "TodoWrite":
            return True
        
        # Handle task file operations
        if tool_name in ["Write", "Edit", "MultiEdit"]:
            file_path = request_data.get("arguments", {}).get("file_path", "")
            if ".claude/project/tasks/" in file_path:
                return True
        
        return False
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        """Process TodoWrite operations and manage tasks"""
        tool_name = request_data.get("name", "")
        
        # Handle task file operations
        if tool_name in ["Write", "Edit", "MultiEdit"]:
            return self._handle_task_file_operation(request_data)
        
        # Handle TodoWrite operations
        todos = request_data.get("arguments", {}).get("todos", [])
        
        if not todos:
            return {"status": 0}
        
        # Get active task
        active_task = self.task_manager.get_active_task()
        
        # Analyze todos
        completed_count = sum(1 for todo in todos if todo.get("status") == "completed")
        total_count = len(todos)
        progress = int((completed_count / total_count * 100) if total_count > 0 else 0)
        
        # Extract high priority pending tasks
        high_priority_pending = [
            todo for todo in todos 
            if todo.get("status") == "pending" and todo.get("priority") == "high"
        ]
        
        output = None
        
        # Check if we should suggest task completion
        if active_task and progress >= 100:
            output = self._suggest_task_completion(active_task)
        
        # Check if we should suggest new task activation
        elif not active_task and high_priority_pending:
            output = self._suggest_task_activation(high_priority_pending)
        
        # Update task progress if active
        if active_task:
            todo_ids = [todo.get("id") for todo in todos if todo.get("id")]
            self.task_manager.update_task_progress(
                active_task.name,
                progress,
                todo_ids
            )
        
        # Check for task-related patterns in todos
        task_suggestions = self._extract_task_patterns(todos)
        if task_suggestions and not output:
            output = self._suggest_new_tasks(task_suggestions)
        
        return {
            "status": 0,
            "output": output
        }
    
    def _suggest_task_completion(self, task) -> str:
        """Generate task completion suggestion"""
        output = self.formatter.header("Task Complete!", "task")
        
        items = [
            f"✅ Task '{task.name}' appears to be complete",
            f"All todos have been marked as completed",
            "",
            "To archive this task and update records:",
            f"`/logic tasks complete`",
            "",
            "Or continue with any remaining work..."
        ]
        
        output += self.formatter.section("Task Status", items, "success")
        output += self.formatter.footer()
        
        return output
    
    def _suggest_task_activation(self, high_priority_todos: List[Dict]) -> str:
        """Suggest activating a new task"""
        output = self.formatter.header("High Priority Tasks Detected", "task")
        
        items = [
            f"Found {len(high_priority_todos)} high-priority pending task(s):",
            ""
        ]
        
        # List high priority todos
        for todo in high_priority_todos[:3]:  # Show max 3
            items.append(f"• {todo.get('content', 'Unnamed task')}")
        
        if len(high_priority_todos) > 3:
            items.append(f"... and {len(high_priority_todos) - 3} more")
        
        items.extend([
            "",
            "No active task detected. Consider:",
            "1. Create a new task: `/logic tasks new [name]`",
            "2. Activate existing: `/logic tasks activate [name]`",
            "3. List all tasks: `/logic tasks list`"
        ])
        
        output += self.formatter.section("Task Suggestions", items, "info")
        output += self.formatter.footer()
        
        return output
    
    def _extract_task_patterns(self, todos: List[Dict]) -> List[str]:
        """Extract potential task names from todos"""
        task_patterns = []
        
        # Look for WP (work package) patterns
        for todo in todos:
            content = todo.get("content", "")
            
            # Pattern: WP[number]: description
            if "WP" in content and ":" in content:
                task_patterns.append(content.split(":")[0].strip())
            
            # Pattern: "Create X", "Implement Y", "Build Z"
            elif any(word in content for word in ["Create", "Implement", "Build", "Design"]):
                # Extract first few words as potential task name
                words = content.split()[:4]
                task_patterns.append(" ".join(words))
        
        return list(set(task_patterns))  # Remove duplicates
    
    def _suggest_new_tasks(self, suggestions: List[str]) -> str:
        """Suggest creating new tasks"""
        output = self.formatter.header("Task Patterns Detected", "task")
        
        items = [
            "Detected potential tasks in your todos:",
            ""
        ]
        
        for suggestion in suggestions[:5]:  # Max 5 suggestions
            items.append(f"• {suggestion}")
        
        items.extend([
            "",
            "To create tasks from these:",
            "```",
            f"/logic tasks new {suggestions[0] if suggestions else '[task-name]'}",
            "```"
        ])
        
        output += self.formatter.section("Task Creation", items, "info")
        output += self.formatter.footer()
        
        return output
    
    def _handle_task_file_operation(self, request_data: dict) -> dict:
        """Handle task file creation/editing"""
        file_path = request_data.get("arguments", {}).get("file_path", "")
        
        # Check if this is a new task creation in to-do
        if "/to-do/" in file_path and file_path.endswith(".md"):
            output = self._generate_task_creation_guidance(file_path)
            return {"status": 0, "output": output}
        
        # Check if task is being moved between folders
        elif any(folder in file_path for folder in ["/active/", "/x__completed/"]):
            output = self._generate_task_movement_notice(file_path)
            return {"status": 0, "output": output}
        
        return {"status": 0}
    
    def _generate_task_creation_guidance(self, file_path: str) -> str:
        """Generate guidance for new task creation"""
        task_name = Path(file_path).stem
        
        output = self.formatter.header("Task Created Successfully", "task")
        
        items = [
            f"✅ Task '{task_name}' created in /to-do",
            "",
            "**Task Workflow Reminder:**",
            "1. **Review** the task document for completeness",
            "2. **Approve** to begin implementation",
            "3. **Activate** with: `/logic tasks activate {task_name}`",
            "4. **Track** progress with TodoWrite",
            "5. **Complete** when finished: `/logic tasks complete`",
            "",
            "The task will automatically flow through:",
            "`/to-do` → `/active` → `/x__completed` → `/z__archive`"
        ]
        
        output += self.formatter.section("Task Workflow", items, "success")
        
        # Add tips
        tips = [
            "💡 **Tips for Task Management:**",
            "• Only one task can be active at a time",
            "• TodoWrite automatically tracks progress",
            "• Tasks archive after 30 days in completed",
            "• Use `/logic tasks status` to check progress"
        ]
        
        output += self.formatter.section("Tips", tips, "info")
        output += self.formatter.footer()
        
        return output
    
    def _generate_task_movement_notice(self, file_path: str) -> str:
        """Generate notice for task movement"""
        if "/active/" in file_path:
            status = "activated"
            emoji = "🚀"
        elif "/x__completed/" in file_path:
            status = "completed"
            emoji = "✅"
        else:
            status = "moved"
            emoji = "📁"
        
        task_name = Path(file_path).stem
        
        output = self.formatter.header(f"Task {status.title()}", "task")
        
        items = [
            f"{emoji} Task '{task_name}' has been {status}",
            "",
            f"Location: `{Path(file_path).parent.name}`"
        ]
        
        if status == "activated":
            items.extend([
                "",
                "**Next Steps:**",
                "• Use TodoWrite to track implementation progress",
                "• Hook will monitor completion status",
                "• Complete with: `/logic tasks complete`"
            ])
        
        output += self.formatter.section("Status Update", items, "success")
        output += self.formatter.footer()
        
        return output