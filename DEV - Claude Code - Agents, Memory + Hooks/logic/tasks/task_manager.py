#!/usr/bin/env python3
"""
Task Management System for Claude Code
Manages task lifecycle: suggestion → active → completed
Integrates with TodoWrite for progress tracking
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from .task_summarizer import TaskSummarizer


@dataclass
class Task:
    """Represents a task in the system"""
    name: str
    description: str
    created_at: str
    status: str = "suggestion"  # suggestion, active, completed
    agent_id: Optional[str] = None
    todo_ids: List[str] = None
    progress: int = 0
    completed_at: Optional[str] = None
    
    def __post_init__(self):
        if self.todo_ids is None:
            self.todo_ids = []


class TaskManager:
    """Manages task lifecycle and state"""
    
    def __init__(self, claude_path: Path = None):
        """Initialize task manager"""
        if claude_path is None:
            # Find .claude directory
            self.project_root = Path.cwd()
            while not (self.project_root / ".claude").exists() and self.project_root != self.project_root.parent:
                self.project_root = self.project_root.parent
            self.claude_path = self.project_root / ".claude"
        else:
            self.claude_path = claude_path
        
        # Task directories
        self.tasks_dir = self.claude_path / "project" / "tasks"
        self.to_do_dir = self.tasks_dir / "to-do"
        self.active_dir = self.tasks_dir / "active"
        self.completed_dir = self.tasks_dir / "x__completed"
        self.archive_dir = self.tasks_dir / "z__archive"
        self.templates_dir = self.tasks_dir / "y__templates"
        
        # Legacy support - merge suggestions into to-do
        self.suggestions_dir = self.tasks_dir / "suggestions"
        
        # Task registry
        self.registry_path = self.tasks_dir / ".task-registry.json"
        
        # Initialize task summarizer
        self.summarizer = TaskSummarizer()
        
        # Ensure directories exist
        for dir_path in [self.to_do_dir, self.active_dir, self.completed_dir, 
                        self.archive_dir, self.templates_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Migrate suggestions to to-do if needed
        self._migrate_suggestions_to_todo()
    
    def _load_registry(self) -> Dict[str, Any]:
        """Load task registry"""
        if self.registry_path.exists():
            with open(self.registry_path, 'r') as f:
                return json.load(f)
        return {
            "active_task": None,
            "tasks": {},
            "completed_count": 0
        }
    
    def _save_registry(self, registry: Dict[str, Any]):
        """Save task registry"""
        with open(self.registry_path, 'w') as f:
            json.dump(registry, f, indent=2)
    
    def _migrate_suggestions_to_todo(self):
        """Migrate any remaining files from suggestions to to-do"""
        if self.suggestions_dir.exists():
            for file_path in self.suggestions_dir.glob("*.md"):
                dest_path = self.to_do_dir / file_path.name
                if not dest_path.exists():
                    shutil.move(str(file_path), str(dest_path))
            
            # Remove suggestions directory if empty
            try:
                self.suggestions_dir.rmdir()
            except OSError:
                pass  # Directory not empty or other error
    
    def _generate_task_filename(self, name: str) -> str:
        """Generate safe filename from task name"""
        # Replace unsafe characters
        safe_name = name.lower()
        safe_name = safe_name.replace(' ', '-')
        safe_name = ''.join(c for c in safe_name if c.isalnum() or c in '-_')
        return f"{safe_name}.md"
    
    def create_task(self, name: str, description: str = "", template: Optional[str] = None) -> Task:
        """Create a new task in to-do"""
        # Create task object
        task = Task(
            name=name,
            description=description,
            created_at=datetime.now().isoformat(),
            status="to-do"
        )
        
        # Generate filename
        filename = self._generate_task_filename(name)
        filepath = self.to_do_dir / filename
        
        # Use template if provided
        if template and (self.templates_dir / f"{template}.md").exists():
            template_content = (self.templates_dir / f"{template}.md").read_text()
            content = template_content.format(
                name=name,
                description=description,
                created_at=task.created_at
            )
        else:
            # Default content
            content = f"""# Task: {name}

## Description
{description or "No description provided."}

## Created
{task.created_at}

## Status
- [ ] Not started
- [ ] In progress  
- [ ] Completed

## Notes
<!-- Add implementation notes here -->

## Progress
<!-- Updated by TodoWrite integration -->
"""
        
        # Write task file
        with open(filepath, 'w') as f:
            f.write(content)
        
        # Update registry
        registry = self._load_registry()
        registry["tasks"][name] = asdict(task)
        self._save_registry(registry)
        
        return task
    
    def activate_task(self, name: str) -> bool:
        """Move task from to-do to active"""
        registry = self._load_registry()
        
        # Check if task exists
        if name not in registry["tasks"]:
            return False
        
        # Check if there's already an active task
        if registry["active_task"]:
            raise ValueError(f"Task '{registry['active_task']}' is already active. Complete it first.")
        
        # Move file
        filename = self._generate_task_filename(name)
        source = self.to_do_dir / filename
        
        if not source.exists():
            # Try legacy suggestions directory
            source = self.suggestions_dir / filename
            if not source.exists():
                # Try to find in completed
                source = self.completed_dir / filename
                if not source.exists():
                    return False
        
        dest = self.active_dir / filename
        shutil.move(str(source), str(dest))
        
        # Update registry
        task_data = registry["tasks"][name]
        task_data["status"] = "active"
        registry["active_task"] = name
        self._save_registry(registry)
        
        return True
    
    def complete_task(self, name: Optional[str] = None) -> bool:
        """Complete the active task or specified task"""
        registry = self._load_registry()
        
        # Use active task if name not provided
        if name is None:
            name = registry.get("active_task")
            if not name:
                return False
        
        # Check if task exists
        if name not in registry["tasks"]:
            return False
        
        # Move file
        filename = self._generate_task_filename(name)
        source = self.active_dir / filename
        
        if not source.exists():
            return False
        
        # Add timestamp to completed filename
        timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        dest_filename = f"{timestamp}-{filename}"
        dest = self.completed_dir / dest_filename
        
        shutil.move(str(source), str(dest))
        
        # Update registry
        task_data = registry["tasks"][name]
        task_data["status"] = "completed"
        task_data["completed_at"] = datetime.now().isoformat()
        
        if registry.get("active_task") == name:
            registry["active_task"] = None
        
        registry["completed_count"] += 1
        self._save_registry(registry)
        
        return True
    
    def get_active_task(self) -> Optional[Task]:
        """Get the currently active task"""
        registry = self._load_registry()
        active_name = registry.get("active_task")
        
        if active_name and active_name in registry["tasks"]:
            task_data = registry["tasks"][active_name]
            return Task(**task_data)
        
        return None
    
    def list_tasks(self, status: Optional[str] = None) -> List[Task]:
        """List all tasks, optionally filtered by status"""
        registry = self._load_registry()
        tasks = []
        
        for name, task_data in registry["tasks"].items():
            if status is None or task_data.get("status") == status:
                tasks.append(Task(**task_data))
        
        # Sort by created_at
        tasks.sort(key=lambda t: t.created_at)
        return tasks
    
    def search_tasks(self, query: str) -> List[Tuple[Task, str]]:
        """Search tasks by content"""
        results = []
        query_lower = query.lower()
        
        # Search in all directories except archive
        for dir_path in [self.to_do_dir, self.active_dir, self.completed_dir]:
            if not dir_path.exists():
                continue
            for filepath in dir_path.glob("*.md"):
                content = filepath.read_text()
                
                if query_lower in content.lower():
                    # Extract task name from content or filename
                    lines = content.split('\n')
                    task_name = None
                    
                    for line in lines:
                        if line.startswith("# Task:"):
                            task_name = line.replace("# Task:", "").strip()
                            break
                    
                    if not task_name:
                        task_name = filepath.stem
                    
                    # Find matching lines
                    matching_lines = []
                    for i, line in enumerate(lines):
                        if query_lower in line.lower():
                            matching_lines.append(f"Line {i+1}: {line.strip()}")
                    
                    # Get task from registry if exists
                    registry = self._load_registry()
                    if task_name in registry["tasks"]:
                        task = Task(**registry["tasks"][task_name])
                    else:
                        # Create temporary task object
                        task = Task(
                            name=task_name,
                            description="",
                            created_at="",
                            status=self._get_status_from_path(filepath)
                        )
                    
                    snippet = "\n".join(matching_lines[:3])
                    if len(matching_lines) > 3:
                        snippet += f"\n... and {len(matching_lines) - 3} more matches"
                    
                    results.append((task, snippet))
        
        return results
    
    def _get_status_from_path(self, filepath: Path) -> str:
        """Determine task status from file path"""
        if self.to_do_dir in filepath.parents:
            return "to-do"
        elif self.suggestions_dir in filepath.parents:
            return "to-do"  # Legacy support
        elif self.active_dir in filepath.parents:
            return "active"
        elif self.completed_dir in filepath.parents:
            return "completed"
        elif self.archive_dir in filepath.parents:
            return "archived"
        return "unknown"
    
    def update_task_progress(self, name: str, progress: int, todo_ids: List[str] = None):
        """Update task progress from TodoWrite"""
        registry = self._load_registry()
        
        if name in registry["tasks"]:
            registry["tasks"][name]["progress"] = progress
            if todo_ids:
                registry["tasks"][name]["todo_ids"] = todo_ids
            self._save_registry(registry)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get task statistics"""
        registry = self._load_registry()
        tasks = registry["tasks"]
        
        return {
            "total_tasks": len(tasks),
            "suggestions": len([t for t in tasks.values() if t["status"] == "suggestion"]),
            "active": 1 if registry.get("active_task") else 0,
            "completed": registry.get("completed_count", 0),
            "active_task_name": registry.get("active_task"),
            "avg_completion_time": self._calculate_avg_completion_time(tasks)
        }
    
    def _calculate_avg_completion_time(self, tasks: Dict[str, Any]) -> Optional[float]:
        """Calculate average completion time in hours"""
        completed_tasks = [t for t in tasks.values() if t["status"] == "completed" and t.get("completed_at")]
        
        if not completed_tasks:
            return None
        
        total_hours = 0
        count = 0
        
        for task in completed_tasks:
            try:
                created = datetime.fromisoformat(task["created_at"])
                completed = datetime.fromisoformat(task["completed_at"])
                hours = (completed - created).total_seconds() / 3600
                total_hours += hours
                count += 1
            except:
                continue
        
        return total_hours / count if count > 0 else None
    
    def archive_old_tasks(self, days: int = 30) -> int:
        """Archive completed tasks older than specified days"""
        from datetime import timedelta
        
        archived_count = 0
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Check completed directory
        for filepath in self.completed_dir.glob("*.md"):
            # Try to get completion date from filename or content
            try:
                # Extract timestamp from filename if present
                filename_parts = filepath.stem.split('-')
                if len(filename_parts) >= 3:
                    date_str = '-'.join(filename_parts[:3])
                    file_date = datetime.strptime(date_str, '%Y-%m-%d')
                    
                    if file_date < cutoff_date:
                        # Archive the file
                        archive_path = self.archive_dir / filepath.name
                        shutil.move(str(filepath), str(archive_path))
                        archived_count += 1
            except:
                # If we can't parse the date, check file modification time
                stat = filepath.stat()
                mod_time = datetime.fromtimestamp(stat.st_mtime)
                if mod_time < cutoff_date:
                    archive_path = self.archive_dir / filepath.name
                    shutil.move(str(filepath), str(archive_path))
                    archived_count += 1
        
        return archived_count
    
    def should_exclude_path(self, path: Path) -> bool:
        """Check if a path should be excluded from Claude operations"""
        # Convert to string for comparison
        path_str = str(path)
        archive_str = str(self.archive_dir)
        
        # Check if path is in or under archive directory
        return archive_str in path_str or path.is_relative_to(self.archive_dir)