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
        self.tasks_dir = self.claude_path / "project-management"
        self.to_do_dir = self.tasks_dir / "specs"
        self.active_dir = self.tasks_dir / "active"
        self.completed_dir = self.tasks_dir / "completed"
        self.archive_dir = self.tasks_dir / "z__archive"
        self.templates_dir = self.tasks_dir / "y__templates"
        
        # Legacy support - merge suggestions into specs
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
    
    def get_task_registry(self) -> Dict[str, Any]:
        """Get the current task registry (public method)"""
        return self._load_registry()
    
    def _migrate_suggestions_to_todo(self):
        """Migrate any remaining files from suggestions to specs"""
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
    
    def _determine_task_subfolder(self, name: str, task_type: str = "specs") -> str:
        """Determine appropriate sub-folder based on task name"""
        name_lower = name.lower()
        
        # Category mappings - Order matters! More specific patterns first
        
        # Security patterns (check before bugs)
        if any(word in name_lower for word in ["security", "auth", "permission", "vulnerability", "secure", "encryption", "access"]):
            return "security"
        
        # Documentation patterns (check before update)
        elif any(word in name_lower for word in ["doc", "documentation", "readme", "guide", "manual", "help", "tutorial", "instructions"]):
            return "documentation"
        
        # Testing patterns (check before create/spec)
        elif any(word in name_lower for word in ["test", "testing", "unittest", "integration test", "e2e", "verify", "validate", "qa"]):
            return "testing"
        
        # Bug patterns
        elif any(word in name_lower for word in ["bug", "fix", "issue", "error", "problem", "broken", "crash"]):
            return "bugs"
        
        # Performance patterns (check before optimize in refactoring)
        elif any(word in name_lower for word in ["performance", "speed", "slow", "optimize performance", "cache", "latency"]):
            return "performance"
        
        # Feature patterns
        elif any(word in name_lower for word in ["feature", "add", "implement", "create", "new", "build"]):
            return "features"
        
        # Enhancement patterns
        elif any(word in name_lower for word in ["enhance", "improve", "upgrade", "update", "better"]):
            return "enhancements"
        
        # Refactoring patterns
        elif any(word in name_lower for word in ["refactor", "clean", "reorganize", "restructure", "optimize code"]):
            return "refactoring"
        
        # Integration patterns
        elif any(word in name_lower for word in ["integrate", "connect", "api", "webhook", "integration", "third-party"]):
            return "integrations"
        
        else:
            return "general"
    
    def create_task(self, name: str, description: str = "", template: Optional[str] = None) -> Task:
        """Create a new task in specs with automatic sub-folder organization"""
        # Create task object
        task = Task(
            name=name,
            description=description,
            created_at=datetime.now().isoformat(),
            status="to-do"
        )
        
        # Determine sub-folder
        subfolder = self._determine_task_subfolder(name)
        task_dir = self.to_do_dir / subfolder
        
        # Ensure sub-folder exists
        task_dir.mkdir(parents=True, exist_ok=True)
        
        # Create project folder with task name (sanitized)
        safe_project_name = ''.join(c for c in name.lower() if c.isalnum() or c in ' -_')
        safe_project_name = safe_project_name.replace(' ', '-')
        project_dir = task_dir / safe_project_name
        project_dir.mkdir(parents=True, exist_ok=True)
        
        # Create test folder automatically
        test_dir = project_dir / "tests"
        test_dir.mkdir(parents=True, exist_ok=True)
        
        # Create test plan template
        test_plan_content = f"""# Test Plan: {name}
**Date:** {datetime.now().strftime("%Y-%m-%d")}
**Time:** {datetime.now().strftime("%H:%M:%S")}

## Test Objectives
<!-- Define what needs to be tested -->

## Test Cases
<!-- List specific test cases -->

## Test Results
<!-- Document test results here -->
"""
        test_plan_path = test_dir / f"test-plan-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.md"
        with open(test_plan_path, 'w') as f:
            f.write(test_plan_content)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        base_filename = self._generate_task_filename(name).replace('.md', '')
        filename = f"{base_filename}-{timestamp}.md"
        filepath = project_dir / filename
        
        # Use template if provided
        if template and (self.templates_dir / f"{template}.md").exists():
            template_content = (self.templates_dir / f"{template}.md").read_text()
            content = template_content.format(
                name=name,
                description=description,
                created_at=task.created_at
            )
        else:
            # Default content with date and time
            content = f"""# Task: {name}
**Date:** {datetime.now().strftime("%Y-%m-%d")}  
**Time:** {datetime.now().strftime("%H:%M:%S")}  

## Description
{description or "No description provided."}

## Created
{task.created_at}

## Status
- [ ] Not started
- [ ] In progress  
- [ ] Completed

## Requirements
<!-- Define specific requirements here -->

## Implementation Plan
<!-- Outline the implementation approach -->

## Test Strategy
<!-- Link to test plan in /tests folder -->
See: [Test Plan](./tests/test-plan-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.md)

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
        
        # Find the file (could be in a sub-folder)
        filename = self._generate_task_filename(name)
        source = None
        
        # First try direct path
        if (self.to_do_dir / filename).exists():
            source = self.to_do_dir / filename
        else:
            # Search in sub-folders
            for subdir in self.to_do_dir.iterdir():
                if subdir.is_dir() and (subdir / filename).exists():
                    source = subdir / filename
                    break
        
        # Try legacy locations if not found
        if not source:
            if (self.suggestions_dir / filename).exists():
                source = self.suggestions_dir / filename
            else:
                # Search in completed sub-folders
                for subdir in self.completed_dir.iterdir():
                    if subdir.is_dir() and (subdir / filename).exists():
                        source = subdir / filename
                        break
        
        if not source:
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
        
        # Determine sub-folder for completed task
        subfolder = self._determine_task_subfolder(name)
        completed_subdir = self.completed_dir / subfolder
        
        # Ensure sub-folder exists
        completed_subdir.mkdir(parents=True, exist_ok=True)
        
        # Add timestamp to completed filename
        timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        dest_filename = f"{timestamp}-{filename}"
        dest = completed_subdir / dest_filename
        
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
        
        # Search in all directories except archive (including sub-folders)
        for dir_path in [self.to_do_dir, self.active_dir, self.completed_dir]:
            if not dir_path.exists():
                continue
            for filepath in dir_path.rglob("*.md"):
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
    
    def suggest_tasks_for_archival(self, days: int = 30) -> List[Tuple[Path, datetime]]:
        """
        Suggest completed tasks that could be archived (user-managed only).
        
        IMPORTANT: z__archive folders are user-managed only. This method only
        suggests files for archival - it does NOT move files automatically.
        Only the user should move files to z__archive folders.
        
        Returns:
            List of tuples (filepath, completion_date) for tasks older than specified days
        """
        from datetime import timedelta
        
        suggestions = []
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Check completed directory and subdirectories
        for filepath in self.completed_dir.rglob("*.md"):
            # Skip files already in z__archive
            if "z__archive" in str(filepath):
                continue
                
            try:
                # Try to get completion date from filename
                filename_parts = filepath.stem.split('-')
                if len(filename_parts) >= 3:
                    date_str = '-'.join(filename_parts[:3])
                    file_date = datetime.strptime(date_str, '%Y-%m-%d')
                    
                    if file_date < cutoff_date:
                        suggestions.append((filepath, file_date))
            except:
                # If we can't parse the date, check file modification time
                stat = filepath.stat()
                mod_time = datetime.fromtimestamp(stat.st_mtime)
                if mod_time < cutoff_date:
                    suggestions.append((filepath, mod_time))
        
        # Sort by date (oldest first)
        suggestions.sort(key=lambda x: x[1])
        return suggestions
    
    def archive_old_tasks(self, days: int = 30) -> int:
        """
        DEPRECATED: This method is disabled to ensure z__archive is user-managed only.
        Use suggest_tasks_for_archival() instead to get a list of candidates.
        
        Raises:
            NotImplementedError: Always raised as automatic archival is disabled
        """
        raise NotImplementedError(
            "Automatic archival is disabled. z__archive folders are user-managed only. "
            "Use suggest_tasks_for_archival() to get a list of archival candidates."
        )
    
    def should_exclude_path(self, path: str) -> bool:
        """Check if a path should be excluded from Claude operations"""
        # Convert to string for comparison
        path_str = str(path)
        
        # Check if path contains z__archive
        return "z__archive" in path_str