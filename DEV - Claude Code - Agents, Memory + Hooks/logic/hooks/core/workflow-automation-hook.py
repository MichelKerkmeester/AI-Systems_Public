#!/usr/bin/env python3
"""
Workflow Automation Hook for Claude Code
Automatically triggers Sequential Thinking MCP for complex tasks
Automatically detects and handles complex tasks (replaces manual /workflow command)
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, UserPromptHook, SettingsManager, MessageFormatter


class WorkflowAutomationHook(UserPromptHook):
    """Automatically detects complex tasks and triggers workflow automation"""
    
    def __init__(self):
        super().__init__()
        
        # Settings path
        self.settings_path = self.claude_path / "logic" / "workflow" / "workflow-settings.json"
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        
        # Complexity indicators
        self.complexity_patterns = {
            "multi_step": {
                "patterns": [
                    r'\b(?:step|phase|stage)s?\s*\d+',
                    r'\bfirst\b.*\bthen\b.*\bfinally\b',
                    r'\b(?:1\.|one).*\b(?:2\.|two).*\b(?:3\.|three)',
                    r'\bsequence\s+of\b',
                    r'\bmulti[- ]?step\b'
                ],
                "weight": 3
            },
            "architecture": {
                "patterns": [
                    r'\barchitect(?:ure|ural)\b',
                    r'\bdesign\s+pattern\b',
                    r'\bsystem\s+design\b',
                    r'\brefactor(?:ing)?\b',
                    r'\brestructur(?:e|ing)\b'
                ],
                "weight": 4
            },
            "complex_features": {
                "patterns": [
                    r'\bimplement\s+(?:a\s+)?(?:new\s+)?(?:feature|system|module)\b',
                    r'\bbuild\s+(?:a\s+)?(?:complete|full|entire)\b',
                    r'\bcreate\s+(?:a\s+)?(?:comprehensive|complex)\b',
                    r'\bintegrat(?:e|ion)\s+(?:with|multiple)\b'
                ],
                "weight": 3
            },
            "analysis": {
                "patterns": [
                    r'\banalyz[es]?\s+(?:the\s+)?(?:entire|whole|complete)\b',
                    r'\bdeep\s+dive\b',
                    r'\bcomprehensive\s+(?:review|analysis)\b',
                    r'\binvestigat[es]?\s+(?:why|how)\b'
                ],
                "weight": 2
            },
            "multiple_files": {
                "patterns": [
                    r'\b(?:multiple|several|many)\s+files?\b',
                    r'\bacross\s+(?:the\s+)?(?:codebase|project)\b',
                    r'\b(?:all|every)\s+(?:component|module|file)s?\b'
                ],
                "weight": 2
            }
        }
        
        # Keywords that suggest workflow is needed
        self.workflow_keywords = [
            "plan", "design", "architect", "implement", "build", "create",
            "refactor", "restructure", "analyze", "investigate", "debug",
            "optimize", "migrate", "integrate", "automate"
        ]
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "enabled": True,
            "complexity_threshold": 3,  # Minimum complexity score to trigger
            "auto_trigger": True,
            "show_analysis": True,
            "exclude_patterns": [
                r'\b(?:simple|quick|small|minor)\b',
                r'\bjust\s+(?:a\s+)?(?:quick|simple)\b',
                r'\bone[- ]?liner?\b'
            ]
        }
    
    def process_user_prompt(self, prompt: str) -> Tuple[int, Optional[str]]:
        """Process user prompt and detect if workflow automation is needed"""
        if not self.settings.get("enabled"):
            return 0, None
        
        # Check for exclusion patterns
        for pattern in self.settings.get("exclude_patterns", []):
            if re.search(pattern, prompt, re.IGNORECASE):
                return 0, None
        
        # Calculate complexity score
        complexity_score = self._calculate_complexity(prompt)
        
        # Check if threshold is met
        threshold = self.settings.get("complexity_threshold", 3)
        if complexity_score < threshold:
            return 0, None
        
        # Generate output
        output = self._generate_workflow_suggestion(prompt, complexity_score)
        
        # Auto-trigger if enabled
        if self.settings.get("auto_trigger") and complexity_score >= threshold + 2:
            output += self._generate_auto_trigger_notice()
        
        return 0, output
    
    def _calculate_complexity(self, prompt: str) -> int:
        """Calculate complexity score for the prompt"""
        score = 0
        detected_patterns = []
        
        # Check complexity patterns
        for category, config in self.complexity_patterns.items():
            for pattern in config["patterns"]:
                if re.search(pattern, prompt, re.IGNORECASE):
                    score += config["weight"]
                    detected_patterns.append(category)
                    break  # Only count category once
        
        # Check workflow keywords
        prompt_lower = prompt.lower()
        keyword_count = sum(1 for keyword in self.workflow_keywords 
                          if keyword in prompt_lower)
        if keyword_count >= 2:
            score += 2
            detected_patterns.append("workflow_keywords")
        
        # Check length and structure
        if len(prompt) > 200:
            score += 1
            detected_patterns.append("detailed_request")
        
        if prompt.count('\n') > 3:
            score += 1
            detected_patterns.append("structured_request")
        
        # Store detected patterns for analysis
        self._last_analysis = {
            "score": score,
            "patterns": detected_patterns
        }
        
        return score
    
    def _generate_workflow_suggestion(self, prompt: str, score: int) -> str:
        """Generate workflow suggestion output"""
        output = MessageFormatter.header("Workflow Automation Detection", "workflow")
        
        # Complexity analysis
        if self.settings.get("show_analysis"):
            analysis_items = [
                f"Complexity Score: {score}/{self.settings.get('complexity_threshold', 3)} (threshold)",
                f"Detected Patterns: {', '.join(self._last_analysis.get('patterns', []))}"
            ]
            output += MessageFormatter.section("Task Analysis", analysis_items, "analysis")
        
        # Recommendation
        recommendation_items = []
        if score >= self.settings.get("complexity_threshold", 3) + 2:
            recommendation_items.append("🚀 **Highly Recommended**: This task would benefit from Sequential Thinking")
            recommendation_items.append("Auto-triggering workflow automation...")
        else:
            recommendation_items.append("💡 **Suggested**: Consider using Sequential Thinking for this task")
            recommendation_items.append("Sequential Thinking will be triggered automatically if needed")
        
        # Add benefits
        recommendation_items.extend([
            "",
            "Benefits of Sequential Thinking:",
            "• Structured approach with clear stages",
            "• Better handling of complex dependencies",
            "• Comprehensive analysis before implementation",
            "• Reduced errors and rework"
        ])
        
        output += MessageFormatter.section("Recommendation", recommendation_items, "workflow")
        
        # Quick actions
        actions = [
            "🎯 Sequential Thinking: Triggers automatically for complex tasks",
            "⚡ To proceed directly: Just continue with your request",
            "⚙️ To adjust automation: `/logic hooks workflow [settings]`"
        ]
        output += MessageFormatter.section("Actions", actions, "info")
        
        output += MessageFormatter.footer()
        
        return output
    
    def _generate_auto_trigger_notice(self) -> str:
        """Generate notice for auto-triggered workflow"""
        return """
🚀 **Sequential Thinking Auto-Triggered**

I'll use Sequential Thinking to approach this complex task systematically.
This will ensure thorough analysis and optimal implementation.

Starting workflow analysis..."""
    
    def get_trigger_recommendation(self, prompt: str) -> Dict[str, Any]:
        """Get workflow trigger recommendation (for other tools to use)"""
        score = self._calculate_complexity(prompt)
        threshold = self.settings.get("complexity_threshold", 3)
        
        return {
            "should_trigger": score >= threshold,
            "auto_trigger": score >= threshold + 2,
            "complexity_score": score,
            "threshold": threshold,
            "patterns": self._last_analysis.get("patterns", [])
        }


if __name__ == "__main__":
    hook = WorkflowAutomationHook()
    hook.run()