#!/usr/bin/env python3
"""Memory bridge for agent system - integrates with Graphiti ONLY."""

import json
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime

class MemoryBridge:
    """Bridge between agent system and Graphiti memory.
    
    IMPORTANT: This is for Graphiti (Neo4j) ONLY.
    Crawl4AI is a separate system for web knowledge search.
    Do not confuse the two!
    """
    
    def __init__(self):
        self.graphiti_enabled = self._check_graphiti_availability()
        self.capture_patterns = self._load_capture_patterns()
        
    def _check_graphiti_availability(self) -> bool:
        """Check if Graphiti MCP is available."""
        # In real implementation, would check MCP availability
        # For now, assume it's available
        return True
    
    def _load_capture_patterns(self) -> Dict[str, Any]:
        """Load patterns for automatic memory capture."""
        return {
            "agent_decisions": {
                "priority": "high",
                "patterns": ["chose", "decided", "selected", "routing to"],
                "capture_context": True
            },
            "implementation_details": {
                "priority": "medium",
                "patterns": ["implemented", "created", "modified", "fixed"],
                "capture_code": True
            },
            "errors_and_fixes": {
                "priority": "high",
                "patterns": ["error", "failed", "exception", "fixed by"],
                "capture_full": True
            },
            "performance_insights": {
                "priority": "low",
                "patterns": ["took", "cost", "saved", "optimized"],
                "capture_metrics": True
            }
        }
    
    async def search_context(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search Graphiti for relevant context.
        
        This is called BEFORE agent execution to provide context.
        """
        if not self.graphiti_enabled:
            return []
        
        # In real implementation, would call Graphiti search
        # For now, simulate the search
        search_results = {
            "query": query,
            "results": [
                {
                    "type": "previous_implementation",
                    "content": "Similar task was implemented using existing carousel component",
                    "relevance": 0.85
                },
                {
                    "type": "pattern",
                    "content": "Project uses Slater autoload - no DOMContentLoaded",
                    "relevance": 0.92
                }
            ],
            "search_time": 0.05
        }
        
        return search_results["results"]
    
    async def capture_agent_execution(self, agent_data: Dict[str, Any]) -> bool:
        """Capture agent execution details to Graphiti.
        
        This is called AFTER agent execution to save knowledge.
        """
        if not self.graphiti_enabled:
            return False
        
        # Build episode data
        episode_data = self._build_episode_data(agent_data)
        
        # In real implementation, would call Graphiti add_episode
        # For now, simulate the capture
        print(f"[Memory Bridge] Would capture: {episode_data['name']}")
        
        return True
    
    def _build_episode_data(self, agent_data: Dict[str, Any]) -> Dict[str, Any]:
        """Build episode data for Graphiti capture."""
        agent_name = agent_data.get("agent", "unknown")
        task = agent_data.get("task", {})
        result = agent_data.get("result", {})
        
        # Determine capture type based on patterns
        capture_type = self._determine_capture_type(agent_data)
        
        episode = {
            "name": f"Agent {agent_name}: {task.get('description', 'Task')[:50]}",
            "episode_body": self._format_episode_body(agent_data),
            "source": f"agent_{agent_name}",
            "source_description": f"Agent System V3 - {agent_name}",
            "group_id": f"agent-{capture_type}",
            "valid_at": datetime.now().isoformat()
        }
        
        return {"data": episode}
    
    def _determine_capture_type(self, agent_data: Dict[str, Any]) -> str:
        """Determine the type of capture based on content."""
        content = json.dumps(agent_data).lower()
        
        for pattern_type, config in self.capture_patterns.items():
            if any(pattern in content for pattern in config["patterns"]):
                return pattern_type.replace("_", "-")
        
        return "general"
    
    def _format_episode_body(self, agent_data: Dict[str, Any]) -> str:
        """Format the episode body for Graphiti."""
        agent = agent_data.get("agent", "unknown")
        task = agent_data.get("task", {})
        result = agent_data.get("result", {})
        execution_time = agent_data.get("execution_time", 0)
        
        body = f"Agent: {agent}\n"
        body += f"Task: {task.get('description', 'No description')}\n"
        body += f"Complexity: {task.get('complexity', 'unknown')}\n"
        body += f"Execution Time: {execution_time:.2f}s\n\n"
        
        if result.get("success"):
            body += "Result: SUCCESS\n"
            if "model_used" in result:
                body += f"Model Used: {result['model_used']}\n"
            if "cost_estimate" in result.get("result", {}):
                body += f"Cost Estimate: ${result['result']['cost_estimate']:.4f}\n"
        else:
            body += "Result: FAILED\n"
            body += f"Error: {result.get('error', 'Unknown error')}\n"
        
        # Add implementation details if present
        if "implementation" in result.get("result", {}):
            body += f"\nImplementation:\n{result['result']['implementation']}\n"
        
        return body
    
    async def get_agent_history(self, agent_name: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Retrieve agent execution history from Graphiti."""
        if not self.graphiti_enabled:
            return []
        
        # Build search query
        if agent_name:
            query = f"agent {agent_name} execution"
        else:
            query = "agent execution"
        
        # Search for agent-related episodes
        return await self.search_context(query, limit)
    
    def should_capture(self, agent_data: Dict[str, Any]) -> bool:
        """Determine if this agent execution should be captured."""
        # Always capture failures
        if not agent_data.get("success", True):
            return True
        
        # Capture based on patterns
        capture_type = self._determine_capture_type(agent_data)
        if capture_type != "general":
            return True
        
        # Capture if execution time is significant
        if agent_data.get("execution_time", 0) > 1.0:
            return True
        
        return False
    
    def get_capture_stats(self) -> Dict[str, Any]:
        """Get memory capture statistics."""
        return {
            "graphiti_enabled": self.graphiti_enabled,
            "capture_patterns": len(self.capture_patterns),
            "pattern_types": list(self.capture_patterns.keys()),
            "system": "Graphiti (Neo4j)",
            "note": "Crawl4AI is separate - for web search only"
        }