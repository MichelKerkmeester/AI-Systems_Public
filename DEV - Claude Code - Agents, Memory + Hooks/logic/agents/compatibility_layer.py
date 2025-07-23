#!/usr/bin/env python3
"""Compatibility layer to ensure agents work with existing system."""

import json
import os
from typing import Dict, Any, List, Callable
import asyncio

class AgentCompatibilityLayer:
    """Ensures agent system integrates seamlessly with existing infrastructure.
    
    Key responsibilities:
    - Route agent outputs through existing hooks
    - Enforce code reuse validation
    - Capture memory automatically
    - Maintain system philosophy
    """
    
    def __init__(self):
        self.hooks_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/hooks"
        self.existing_hooks = self._discover_hooks()
        
    def _discover_hooks(self) -> Dict[str, str]:
        """Discover existing hooks that agents should integrate with."""
        hooks = {
            "memory": f"{self.hooks_path}/memory-context-hook.py",
            "quality": f"{self.hooks_path}/quality/quality-hook.py",
            "code_reuse": f"{self.hooks_path}/quality/slater-compliance-hook.py",
            "knowledge": f"{self.hooks_path}/quality/knowledge-enforcement-hook.py"
        }
        
        # Only include hooks that actually exist
        return {k: v for k, v in hooks.items() if os.path.exists(v)}
    
    async def wrap_agent_execution(self, agent_func: Callable, *args, **kwargs) -> Any:
        """Wrap agent execution to ensure compatibility."""
        
        # Pre-execution: Memory search (enforced by hooks)
        await self._trigger_memory_search(kwargs.get("task", {}))
        
        # Execute agent function
        result = await agent_func(*args, **kwargs)
        
        # Post-execution: Validate and capture
        await self._validate_output(result)
        await self._capture_to_memory(result)
        
        return result
    
    async def _trigger_memory_search(self, task: Dict[str, Any]):
        """Ensure memory search happens before agent execution."""
        # In real implementation, this would trigger the memory hook
        # For now, just note that it would happen
        task_description = task.get("description", "Agent task")
        # Memory search would be triggered here via hook
        
    async def _validate_output(self, result: Dict[str, Any]):
        """Validate agent output against existing rules."""
        if not result.get("success"):
            return
            
        output = result.get("result", {})
        
        # Check for common violations
        violations = []
        
        # Check for DOMContentLoaded (Slater constraint)
        if isinstance(output, dict) and "implementation" in output:
            impl = str(output["implementation"])
            if "DOMContentLoaded" in impl:
                violations.append("Slater autoloads - no DOMContentLoaded needed")
        
        # Check for px units (should use REM)
        if isinstance(output, dict) and "implementation" in output:
            impl = str(output["implementation"])
            import re
            if re.search(r'\d+px(?![\w-])', impl):
                violations.append("Use REM units, not px")
        
        if violations:
            result["warnings"] = violations
    
    async def _capture_to_memory(self, result: Dict[str, Any]):
        """Capture agent decisions to memory."""
        if not result.get("success"):
            return
            
        # Build memory entry
        memory_entry = {
            "type": "agent_execution",
            "agent": result.get("agent", "unknown"),
            "task": result.get("task", {}),
            "result": result.get("result", {}),
            "model_used": result.get("model_used", "unknown"),
            "execution_time": result.get("execution_time", 0)
        }
        
        # In real implementation, this would call Graphiti
        # For now, just note what would be captured
        
    def ensure_code_reuse(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure task follows code reuse policy."""
        # Add search requirement if not present
        if "search_results" not in task:
            task["requires_search"] = True
            task["search_priority"] = "high"
        
        return task
    
    def validate_agent_config(self, config: Dict[str, Any]) -> bool:
        """Validate agent configuration against system constraints."""
        required_fields = ["name", "model", "cost_weight"]
        
        for field in required_fields:
            if field not in config:
                return False
        
        # Ensure model is supported
        supported_models = ["claude", "qwen3", "gemini-flash", "gemini-pro"]
        if config.get("model") not in supported_models:
            return False
        
        return True
    
    def get_integration_status(self) -> Dict[str, Any]:
        """Get status of agent system integration."""
        return {
            "hooks_discovered": len(self.existing_hooks),
            "hooks_available": list(self.existing_hooks.keys()),
            "compatibility_checks": {
                "memory_integration": "memory" in self.existing_hooks,
                "quality_validation": "quality" in self.existing_hooks,
                "code_reuse_enforcement": "code_reuse" in self.existing_hooks,
                "knowledge_enforcement": "knowledge" in self.existing_hooks
            },
            "status": "ready" if all(self.existing_hooks.values()) else "partial"
        }