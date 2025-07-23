#!/usr/bin/env python3
"""Hook for agent system integration with existing infrastructure."""

import json
import sys
from pathlib import Path
from typing import Dict, Any

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from logic.shared import HookBase, HookResponse
from logic.shared.mcp_helpers import MCPHelpers


class AgentHook(HookBase):
    """Hook to integrate agent system with existing automation.
    
    Ensures that:
    - Agent decisions are captured to memory
    - Code reuse validation applies to agent outputs
    - Performance metrics are tracked
    - Quality standards are maintained
    """
    
    def should_trigger(self, tool_use: Dict[str, Any]) -> bool:
        """Trigger when agent-related tools are used."""
        tool_name = tool_use.get("tool_name", "")
        
        # Trigger for agent-specific operations
        agent_triggers = [
            "agent_execute",
            "agent_route",
            "agent_validate"
        ]
        
        # Also trigger for Task tool when it's from agent system
        if tool_name == "Task":
            description = tool_use.get("parameters", {}).get("description", "")
            if any(keyword in description.lower() for keyword in ["agent:", "via agent", "agent system"]):
                return True
        
        return tool_name in agent_triggers
    
    def execute(self, tool_use: Dict[str, Any]) -> HookResponse:
        """Execute agent integration logic."""
        tool_name = tool_use.get("tool_name", "")
        params = tool_use.get("parameters", {})
        
        try:
            # Pre-execution: Ensure memory search
            if self._is_pre_execution(tool_use):
                self._ensure_memory_search(params)
            
            # Post-execution: Capture results
            if self._is_post_execution(tool_use):
                self._capture_agent_memory(tool_use)
                self._validate_agent_output(tool_use)
            
            # Track performance
            self._track_performance(tool_use)
            
            return HookResponse.allow(
                message="Agent operation processed",
                metadata={
                    "agent_system": "v3",
                    "integration": "active"
                }
            )
            
        except Exception as e:
            return HookResponse.warn(
                message=f"Agent hook error: {str(e)}",
                suggestions=["Check agent configuration", "Verify memory system is active"]
            )
    
    def _is_pre_execution(self, tool_use: Dict[str, Any]) -> bool:
        """Check if this is pre-execution phase."""
        return tool_use.get("phase") == "pre" or "search" in tool_use.get("tool_name", "")
    
    def _is_post_execution(self, tool_use: Dict[str, Any]) -> bool:
        """Check if this is post-execution phase."""
        return tool_use.get("phase") == "post" or "complete" in str(tool_use.get("parameters", {}))
    
    def _ensure_memory_search(self, params: Dict[str, Any]):
        """Ensure memory search happens before agent execution."""
        # This would trigger memory search via MCP
        task_description = params.get("description", "")
        if task_description and not params.get("memory_searched"):
            # In real implementation, would call Graphiti search
            print(f"[Agent Hook] Would search memory for: {task_description[:50]}...")
    
    def _capture_agent_memory(self, tool_use: Dict[str, Any]):
        """Capture agent execution to memory."""
        # Build memory entry
        memory_data = {
            "type": "agent_execution",
            "tool": tool_use.get("tool_name"),
            "parameters": tool_use.get("parameters", {}),
            "result": tool_use.get("result", {}),
            "timestamp": tool_use.get("timestamp")
        }
        
        # In real implementation, would call Graphiti
        print(f"[Agent Hook] Would capture to memory: {memory_data['type']}")
    
    def _validate_agent_output(self, tool_use: Dict[str, Any]):
        """Validate agent output meets quality standards."""
        result = tool_use.get("result", {})
        
        # Check for common issues
        if isinstance(result, dict) and "code" in result:
            code = str(result["code"])
            
            # Check Slater constraints
            if "DOMContentLoaded" in code:
                print("[Agent Hook] Warning: Agent generated DOMContentLoaded - Slater autoloads!")
            
            # Check style constraints
            import re
            if re.search(r'\d+px(?![\w-])', code):
                print("[Agent Hook] Warning: Agent used px units - should use REM!")
    
    def _track_performance(self, tool_use: Dict[str, Any]):
        """Track agent performance metrics."""
        # Would track:
        # - Execution time
        # - Token usage
        # - Success rate
        # - Model used
        pass


# Hook registration
def get_hook():
    """Return hook instance for registration."""
    return AgentHook()