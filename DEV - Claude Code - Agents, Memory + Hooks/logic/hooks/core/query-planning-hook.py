#!/usr/bin/env python3
"""
Query Planning Hook for Claude Code
Automatically creates task documents for complex queries that require planning
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, UserPromptHook, SettingsManager, MessageFormatter
from logic.tasks import TaskManager


class QueryPlanningHook(UserPromptHook):
    """Automatically creates task documents for queries requiring planning"""
    
    def __init__(self):
        super().__init__()
        
        # Settings path
        self.settings_path = self.claude_path / "hooks" / "core" / "query-planning-settings.json"
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        
        # Task manager
        self.task_manager = TaskManager()
        
        # Planning indicators
        self.planning_indicators = {
            "analysis_request": {
                "patterns": [
                    r'\banalyz[es]?\s+(?:the\s+)?(?:completion|summary|state)\b',
                    r'\bwhat\s+(?:was|has been)\s+(?:accomplished|completed|done)\b',
                    r'\breview\s+(?:the\s+)?(?:project|work|tasks?)\b',
                    r'\bassess\s+(?:the\s+)?(?:current|overall)\s+(?:state|status)\b'
                ],
                "weight": 3
            },
            "enhancement_request": {
                "patterns": [
                    r'\b(?:enhance|improve|optimize|upgrade)\s+(?:the\s+)?(?:system|project)\b',
                    r'\bdo\s+(?:all|everything)\s+including\s+optional\b',
                    r'\bcomprehensive\s+(?:improvement|enhancement|upgrade)\b',
                    r'\bpost[- ]?refactoring\s+(?:tasks?|work)\b'
                ],
                "weight": 4
            },
            "planning_keywords": {
                "patterns": [
                    r'\b(?:plan|planning|roadmap|strategy)\b',
                    r'\b(?:phases?|stages?|steps?)\s+(?:of|for)\b',
                    r'\bwhat\s+(?:should|needs to)\s+(?:be\s+)?(?:done|implemented)\b',
                    r'\bnext\s+steps?\b'
                ],
                "weight": 3
            },
            "task_creation": {
                "patterns": [
                    r'\bcreate\s+(?:a\s+)?task\b',
                    r'\bmake\s+(?:a\s+)?plan\b',
                    r'\bdocument\s+(?:the\s+)?(?:plan|approach)\b'
                ],
                "weight": 5
            }
        }
        
        # Task template patterns
        self.task_templates = {
            "analysis": "analysis-",
            "enhancement": "enhancement-",
            "refactoring": "refactoring-",
            "implementation": "implementation-",
            "optimization": "optimization-"
        }
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "enabled": True,
            "planning_threshold": 6,  # Score needed to trigger planning
            "auto_create_task": True,
            "require_approval": True,
            "task_folder": "to-do",
            "include_timeline": True,
            "include_metrics": True
        }
    
    def process_user_prompt(self, prompt: str) -> Tuple[int, Optional[str]]:
        """Process user prompt and create task if planning is needed"""
        if not self.settings.get("enabled"):
            return 0, None
        
        # Calculate planning score
        planning_score, detected_types = self._calculate_planning_score(prompt)
        
        # Check if threshold is met
        threshold = self.settings.get("planning_threshold", 6)
        if planning_score < threshold:
            return 0, None
        
        # Check if we're already in a task context
        if self._is_in_task_context(prompt):
            return 0, None
        
        # Generate task suggestion
        output = self._generate_task_suggestion(prompt, planning_score, detected_types)
        
        return 0, output
    
    def _calculate_planning_score(self, prompt: str) -> Tuple[int, List[str]]:
        """Calculate planning score for the prompt"""
        score = 0
        detected_types = []
        
        # Check planning indicators
        for category, config in self.planning_indicators.items():
            for pattern in config["patterns"]:
                if re.search(pattern, prompt, re.IGNORECASE):
                    score += config["weight"]
                    detected_types.append(category)
                    break  # Only count category once
        
        # Additional scoring based on prompt structure
        if len(prompt) > 300:
            score += 2
            detected_types.append("detailed_request")
        
        # Check for multiple questions or requirements
        if prompt.count('?') > 2 or prompt.count('\n-') > 3:
            score += 2
            detected_types.append("multi_requirement")
        
        return score, detected_types
    
    def _is_in_task_context(self, prompt: str) -> bool:
        """Check if we're already working within a task"""
        # Check for active task
        active_task = self.task_manager.get_active_task()
        if active_task:
            return True
        
        # Check for task-related commands in prompt
        task_commands = ['/logic tasks', '/save', 'task document']
        return any(cmd in prompt.lower() for cmd in task_commands)
    
    def _generate_task_suggestion(self, prompt: str, score: int, types: List[str]) -> str:
        """Generate task creation suggestion"""
        output = MessageFormatter.header("Planning Detected", "task")
        
        # Analysis section
        analysis_items = [
            f"Planning Score: {score}/{self.settings.get('planning_threshold', 6)}",
            f"Query Type: {', '.join(set(types))}",
            "",
            "This query requires systematic planning and execution."
        ]
        output += MessageFormatter.section("Analysis", analysis_items, "analysis")
        
        # Recommendation
        recommendation_items = [
            "📋 **Recommended Action**: Create a structured task document",
            "",
            "A task document will:",
            "• Organize all requirements clearly",
            "• Track progress systematically",
            "• Ensure nothing is missed",
            "• Document decisions and rationale",
            "",
            "The task lifecycle will automatically manage:",
            "• `/to-do` → Planning and approval",
            "• `/active` → Implementation tracking",
            "• `/x__completed` → Documentation of results",
            "• `/z__archive` → Long-term reference"
        ]
        output += MessageFormatter.section("Task Management", recommendation_items, "task")
        
        # Next steps
        task_name = self._suggest_task_name(prompt, types)
        next_steps = [
            "I'll create a comprehensive task document that includes:",
            "• Current state analysis",
            "• Detailed implementation plan",
            "• Success metrics",
            "• Testing scenarios",
            "• Timeline and deliverables",
            "",
            f"Suggested task name: `{task_name}`",
            "",
            "Once you approve the task, implementation can begin systematically."
        ]
        output += MessageFormatter.section("Next Steps", next_steps, "info")
        
        output += MessageFormatter.footer()
        
        return output
    
    def _suggest_task_name(self, prompt: str, types: List[str]) -> str:
        """Suggest a task name based on the query"""
        # Try to extract key terms from prompt
        prompt_lower = prompt.lower()
        
        # Determine prefix based on detected types
        prefix = "task-"
        for type_key, type_prefix in self.task_templates.items():
            if any(type_key in t for t in types):
                prefix = type_prefix
                break
        
        # Extract key terms
        if "enhancement" in prompt_lower or "improve" in prompt_lower:
            suffix = "system-enhancement"
        elif "analyz" in prompt_lower or "review" in prompt_lower:
            suffix = "completion-analysis"
        elif "refactor" in prompt_lower:
            suffix = "refactoring"
        elif "implement" in prompt_lower:
            suffix = "implementation"
        else:
            # Use date as fallback
            suffix = datetime.now().strftime("%Y%m%d")
        
        return prefix + suffix
    
    def should_create_task(self, prompt: str) -> Dict[str, Any]:
        """Check if task should be created (for other tools to use)"""
        score, types = self._calculate_planning_score(prompt)
        threshold = self.settings.get("planning_threshold", 6)
        
        return {
            "should_create": score >= threshold and not self._is_in_task_context(prompt),
            "planning_score": score,
            "threshold": threshold,
            "detected_types": types,
            "suggested_name": self._suggest_task_name(prompt, types) if score >= threshold else None
        }


if __name__ == "__main__":
    hook = QueryPlanningHook()
    hook.run()