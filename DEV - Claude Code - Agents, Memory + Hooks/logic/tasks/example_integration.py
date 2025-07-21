#!/usr/bin/env python3
"""
Example integration showing how task_memory_integration works with task_manager
This demonstrates the full workflow of task creation with mandatory memory search
"""

import sys
from pathlib import Path
from typing import List, Dict, Any

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from tasks.task_manager import TaskManager
from tasks.task_memory_integration import TodoWriteMemoryHandler


class TaskManagerWithMemory:
    """
    Extended TaskManager that integrates memory operations
    This shows how to combine the existing task_manager with memory integration
    """
    
    def __init__(self):
        self.task_manager = TaskManager()
        self.memory_handler = TodoWriteMemoryHandler()
        
    def create_task_with_memory_search(self, name: str, description: str = "") -> Dict[str, Any]:
        """
        Create a task with mandatory memory search
        
        This method:
        1. Creates todos for the task
        2. Performs mandatory memory search
        3. Creates the actual task file
        4. Returns search results for user awareness
        """
        
        # Step 1: Create todo representation
        todos = [
            {
                "id": f"task-{hash(name)}",
                "content": name,
                "status": "pending",
                "priority": "medium"
            }
        ]
        
        # Add description as additional todo if provided
        if description:
            todos.append({
                "id": f"task-desc-{hash(description)}",
                "content": description,
                "status": "pending",
                "priority": "low"
            })
        
        # Step 2: Perform mandatory memory search
        print(f"\n🔍 Performing mandatory memory search for: {name}")
        search_result = self.memory_handler.before_todo_write(todos)
        
        # Display search results
        print(self.memory_handler.memory_integration.display_search_message(search_result))
        
        # Step 3: Create the actual task
        task = self.task_manager.create_task(name, description)
        
        # Step 4: Return combined result
        return {
            "task": task,
            "memory_search": search_result,
            "task_file": self.task_manager._generate_task_filename(name)
        }
    
    def activate_task_with_context(self, name: str) -> bool:
        """
        Activate a task and load its memory context
        """
        # Activate the task
        success = self.task_manager.activate_task(name)
        
        if success:
            # Trigger memory context loading
            todos = [{
                "id": f"task-{hash(name)}",
                "content": f"Working on: {name}",
                "status": "in_progress",
                "priority": "high"
            }]
            
            # This will load relevant context
            self.memory_handler.before_todo_write(todos)
            
        return success
    
    def complete_task_with_capture(self, name: str = None) -> bool:
        """
        Complete a task and capture its outcome as memory
        """
        # Get active task if name not provided
        if name is None:
            active_task = self.task_manager.get_active_task()
            if active_task:
                name = active_task.name
            else:
                return False
        
        # Create completion todos
        todos = [{
            "id": f"task-{hash(name)}",
            "content": f"Completed: {name}",
            "status": "completed",
            "priority": "high"
        }]
        
        # Trigger completion memory capture
        self.memory_handler.after_todo_write(todos, success=True)
        
        # Complete the actual task
        return self.task_manager.complete_task(name)
    
    def get_enhanced_stats(self) -> Dict[str, Any]:
        """Get combined statistics from task manager and memory integration"""
        task_stats = self.task_manager.get_stats()
        memory_stats = self.memory_handler.get_stats()
        
        return {
            "tasks": task_stats,
            "memory_operations": memory_stats
        }


# Example usage
def demonstrate_workflow():
    """Demonstrate the complete workflow"""
    print("🚀 Task Memory Integration Demo")
    print("=" * 60)
    
    # Initialize
    tm = TaskManagerWithMemory()
    
    # 1. Create a task with memory search
    print("\n📝 Step 1: Creating task with mandatory memory search")
    result = tm.create_task_with_memory_search(
        name="Implement user authentication with JWT",
        description="Add secure JWT-based authentication to the API endpoints"
    )
    
    print(f"\n✅ Task created: {result['task'].name}")
    print(f"📄 Task file: {result['task_file']}")
    print(f"🔍 Memories found: {result['memory_search']['memories_found']}")
    
    # 2. Activate the task
    print("\n⚡ Step 2: Activating task")
    if tm.activate_task_with_context(result['task'].name):
        print("✅ Task activated with memory context loaded")
    
    # 3. Simulate work (in real usage, this would be actual TodoWrite operations)
    print("\n💻 Step 3: Working on task...")
    print("(In real usage, TodoWrite operations would track progress)")
    
    # 4. Complete the task
    print("\n✅ Step 4: Completing task with memory capture")
    if tm.complete_task_with_capture():
        print("✅ Task completed and memory captured")
    
    # 5. Show statistics
    print("\n📊 Step 5: Final Statistics")
    stats = tm.get_enhanced_stats()
    print(f"Tasks completed: {stats['tasks']['completed']}")
    print(f"Memory searches: {stats['memory_operations']['searches_performed']}")
    print(f"Memories captured: {stats['memory_operations']['memories_captured']}")
    
    print("\n" + "=" * 60)
    print("✨ Demo complete! Memory operations are now integrated with tasks.")


if __name__ == "__main__":
    demonstrate_workflow()