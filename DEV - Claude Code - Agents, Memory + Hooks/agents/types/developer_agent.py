"""
Developer Agent - Implementation and Coding

Specializes in implementing features, refactoring code, and managing
git worktrees for isolated development. Routes simple tasks to Kimi Pro.
"""

import os
import asyncio
import subprocess
from typing import Dict, Any, List, Optional
from pathlib import Path

from .enhanced_agent_base import EnhancedAgentBase
from ..routing import TaskType, ComplexityLevel


class DeveloperAgent(EnhancedAgentBase):
    """Agent specialized for development and implementation tasks"""
    
    def __init__(self, work_package: str = None, **kwargs):
        super().__init__(
            agent_type="developer",
            work_package=work_package,
            **kwargs
        )
        
        # Development-specific state
        self.worktree_path = None
        self.current_branch = None
        self.files_modified = []
        self.tests_added = []
        self.commits_made = []
    
    async def initialize(self):
        """Initialize developer environment"""
        self.log("Initializing developer agent...")
        
        # Set up git worktree if enabled
        if self.metadata.get("use_worktree", True):
            await self._setup_worktree()
        
        # Register task handlers
        self.register_task_handler("implement", self.implement_feature)
        self.register_task_handler("refactor", self.refactor_code)
        self.register_task_handler("fix", self.fix_bug)
        self.register_task_handler("test", self.write_tests)
        self.register_task_handler("edit", self.edit_file)
        self.register_task_handler("search", self.search_codebase)
        
        # Set model preferences
        # Prefer Kimi for simple edits
        self.model_selector.preferences["enable_kimi"] = True
    
    async def run(self):
        """Main developer loop"""
        while self.active:
            if self.tasks:
                task = self.tasks.pop(0)
                try:
                    # Pre-task setup
                    await self._prepare_for_task(task)
                    
                    # Execute task
                    result = await self.execute_task(task)
                    
                    # Post-task cleanup
                    await self._finalize_task(task, result)
                    
                    await self.report_task_completion(task["id"], result)
                except Exception as e:
                    self.log(f"Task failed: {e}", "ERROR")
                    await self._handle_task_failure(task, e)
            else:
                await asyncio.sleep(1)
    
    async def cleanup(self):
        """Clean up developer resources"""
        self.log("Cleaning up developer agent...")
        
        # Save work summary
        await self._save_work_summary()
        
        # Clean up worktree if used
        if self.worktree_path:
            await self._cleanup_worktree()
    
    async def implement_feature(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Implement a new feature"""
        feature = task.get("feature", "")
        self.log(f"Implementing feature: {feature}")
        
        # Analyze feature complexity
        analysis = await self.analyze_task(f"implement {feature}", task)
        
        # Route based on complexity
        if analysis.complexity_level == ComplexityLevel.TRIVIAL:
            # Simple feature - use Kimi
            self.force_model("kimi-pro")
            result = await self._implement_simple_feature(task)
        else:
            # Complex feature - use Claude
            self.force_model("claude-opus-4")
            result = await self._implement_complex_feature(task)
        
        # Track modifications
        self.files_modified.extend(result.get("files_created", []))
        self.files_modified.extend(result.get("files_modified", []))
        
        return result
    
    async def refactor_code(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Refactor existing code"""
        target = task.get("target", "")
        refactor_type = task.get("refactor_type", "general")
        
        self.log(f"Refactoring {target} (type: {refactor_type})")
        
        # Refactoring usually requires understanding - use Claude
        self.force_model("claude-opus-4")
        
        # Simulate refactoring steps
        steps = [
            "Analyzing current structure",
            "Identifying improvement areas",
            "Planning refactoring approach",
            "Implementing changes",
            "Updating tests"
        ]
        
        modified_files = []
        
        for i, step in enumerate(steps):
            self.log(f"Refactoring step: {step}")
            self.report_progress((i + 1) / len(steps) * 100, step)
            await asyncio.sleep(0.5)
            
            if "Implementing" in step:
                # Simulate file modifications
                modified_files = [
                    f"{target}/module.py",
                    f"{target}/utils.py",
                    f"{target}/__init__.py"
                ]
        
        self.files_modified.extend(modified_files)
        
        return {
            "status": "completed",
            "refactor_type": refactor_type,
            "files_modified": modified_files,
            "improvements": [
                "Reduced complexity",
                "Improved modularity",
                "Better naming conventions"
            ],
            "model_used": self.current_model
        }
    
    async def fix_bug(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Fix a bug"""
        bug_id = task.get("bug_id", "unknown")
        description = task.get("description", "")
        
        self.log(f"Fixing bug {bug_id}: {description[:50]}...")
        
        # Bug fixes vary in complexity
        analysis = await self.analyze_task(f"fix bug: {description}", task)
        
        if analysis.complexity_level.value <= 1:  # Trivial or Simple
            self.force_model("kimi-pro")
            fix_approach = "Quick fix"
        else:
            self.force_model("claude-opus-4")
            fix_approach = "Deep analysis and fix"
        
        # Simulate bug fix process
        self.log(f"Approach: {fix_approach}")
        
        steps = [
            "Reproducing issue",
            "Identifying root cause",
            "Implementing fix",
            "Testing fix",
            "Updating documentation"
        ]
        
        for step in steps:
            self.log(f"Bug fix step: {step}")
            await asyncio.sleep(0.3)
        
        fix_details = {
            "status": "completed",
            "bug_id": bug_id,
            "root_cause": "Identified issue in error handling",
            "files_modified": ["src/module.py", "tests/test_module.py"],
            "tests_added": ["test_bug_fix.py"],
            "model_used": self.current_model,
            "approach": fix_approach
        }
        
        self.files_modified.extend(fix_details["files_modified"])
        self.tests_added.extend(fix_details["tests_added"])
        
        return fix_details
    
    async def write_tests(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Write tests for code"""
        target = task.get("target", "")
        test_type = task.get("test_type", "unit")
        
        self.log(f"Writing {test_type} tests for {target}")
        
        # Test writing can often use Kimi for simple cases
        if test_type == "unit" and "simple" in task.get("description", "").lower():
            self.force_model("kimi-pro")
        
        # Generate test files
        test_files = []
        
        if test_type == "unit":
            test_files = [
                f"tests/test_{Path(target).stem}.py",
                f"tests/conftest.py"
            ]
        elif test_type == "integration":
            test_files = [
                f"tests/integration/test_{Path(target).stem}_integration.py"
            ]
        
        self.tests_added.extend(test_files)
        
        return {
            "status": "completed",
            "test_type": test_type,
            "tests_created": test_files,
            "coverage_increase": "15%",
            "model_used": self.current_model
        }
    
    async def edit_file(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Edit a specific file"""
        file_path = task.get("file_path", "")
        edit_type = task.get("edit_type", "modify")
        
        self.log(f"Editing file: {file_path} ({edit_type})")
        
        # Simple edits can use Kimi
        if edit_type in ["typo", "comment", "format"]:
            self.force_model("kimi-pro")
        
        # Track edit
        self.files_modified.append(file_path)
        
        return {
            "status": "completed",
            "file_path": file_path,
            "edit_type": edit_type,
            "lines_changed": 10,
            "model_used": self.current_model
        }
    
    async def search_codebase(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Search through codebase"""
        query = task.get("query", "")
        search_type = task.get("search_type", "text")
        
        self.log(f"Searching for: {query} (type: {search_type})")
        
        # Searches are perfect for Kimi
        self.force_model("kimi-pro")
        
        # Simulate search
        await asyncio.sleep(0.5)
        
        return {
            "status": "completed",
            "query": query,
            "results_found": 5,
            "files_matched": [
                "src/module.py",
                "src/utils.py",
                "tests/test_module.py"
            ],
            "model_used": self.current_model
        }
    
    async def _setup_worktree(self):
        """Set up git worktree for isolated development"""
        self.log("Setting up git worktree...")
        
        # Create worktree directory
        worktree_base = Path.home() / ".claude" / "agents" / "worktrees"
        worktree_base.mkdir(parents=True, exist_ok=True)
        
        # Create unique worktree
        worktree_name = f"{self.agent_id}-{self.work_package or 'dev'}"
        self.worktree_path = worktree_base / worktree_name
        
        # Branch name
        self.current_branch = f"agent/{worktree_name}"
        
        # In production, would run:
        # git worktree add {self.worktree_path} -b {self.current_branch}
        
        self.log(f"Worktree created at: {self.worktree_path}")
        self.log(f"Branch: {self.current_branch}")
    
    async def _cleanup_worktree(self):
        """Clean up git worktree"""
        if not self.worktree_path:
            return
        
        self.log("Cleaning up worktree...")
        
        # In production, would run:
        # git worktree remove {self.worktree_path}
        
        self.log("Worktree cleaned up")
    
    async def _prepare_for_task(self, task: Dict[str, Any]):
        """Prepare environment for task execution"""
        # Could include:
        # - Switching branches
        # - Setting up dependencies
        # - Clearing caches
        pass
    
    async def _finalize_task(self, task: Dict[str, Any], result: Dict[str, Any]):
        """Finalize task after execution"""
        # Could include:
        # - Committing changes
        # - Running tests
        # - Updating documentation
        
        if result.get("status") == "completed" and self.files_modified:
            # Simulate commit
            commit_msg = f"Complete task {task['id']}: {task.get('description', '')[:50]}"
            self.commits_made.append({
                "message": commit_msg,
                "files": list(self.files_modified),
                "timestamp": datetime.now().isoformat()
            })
            self.log(f"Committed: {commit_msg}")
    
    async def _handle_task_failure(self, task: Dict[str, Any], error: Exception):
        """Handle task failure"""
        self.log(f"Handling task failure: {error}", "ERROR")
        
        # Could include:
        # - Reverting changes
        # - Notifying other agents
        # - Creating recovery task
    
    async def _implement_simple_feature(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Implement a simple feature (routed to Kimi)"""
        self.log("Implementing simple feature with Kimi Pro")
        
        await asyncio.sleep(1)  # Simulate implementation
        
        return {
            "status": "completed",
            "complexity": "simple",
            "files_created": ["src/simple_feature.py"],
            "files_modified": ["src/__init__.py"],
            "tests_added": ["tests/test_simple_feature.py"],
            "model_used": "kimi-pro",
            "cost_saved": "60%"
        }
    
    async def _implement_complex_feature(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Implement a complex feature (uses Claude)"""
        self.log("Implementing complex feature with Claude")
        
        # Complex features need more steps
        steps = [
            "Designing architecture",
            "Creating base classes",
            "Implementing core logic",
            "Adding error handling",
            "Writing comprehensive tests"
        ]
        
        files_created = []
        
        for step in steps:
            self.log(f"Feature step: {step}")
            await asyncio.sleep(0.5)
            
            if "Creating" in step or "Implementing" in step:
                files_created.extend([
                    f"src/feature/{step.lower().replace(' ', '_')}.py"
                ])
        
        return {
            "status": "completed",
            "complexity": "complex",
            "files_created": files_created,
            "files_modified": ["src/__init__.py", "src/config.py"],
            "tests_added": [
                "tests/test_feature.py",
                "tests/integration/test_feature_integration.py"
            ],
            "model_used": "claude-opus-4"
        }
    
    async def _save_work_summary(self):
        """Save summary of development work"""
        import json
        
        summary = {
            "agent_id": self.agent_id,
            "work_package": self.work_package,
            "statistics": {
                "files_modified": len(set(self.files_modified)),
                "tests_added": len(self.tests_added),
                "commits_made": len(self.commits_made)
            },
            "files": {
                "modified": list(set(self.files_modified)),
                "tests": self.tests_added
            },
            "commits": self.commits_made,
            "model_usage": self.get_model_stats()
        }
        
        # Save to workspace
        if self.lifecycle.workspace:
            summary_path = Path(self.lifecycle.workspace) / "development_summary.json"
            with open(summary_path, 'w') as f:
                json.dump(summary, f, indent=2)
            
            self.log(f"Work summary saved to {summary_path}")