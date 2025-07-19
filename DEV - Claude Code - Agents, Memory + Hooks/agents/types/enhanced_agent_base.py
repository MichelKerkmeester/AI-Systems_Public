"""
Enhanced Agent Base with Model Selection

Extends the base agent with intelligent model routing capabilities.
"""

import sys
import asyncio
from typing import Dict, Any, Optional, List
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "logic" / "shared"))

from logic.shared.agent_base import AgentBase
from routing import TaskComplexityAnalyzer, ModelSelector, TaskType
from intelligence import get_thinking_integration, get_memory_integration


class EnhancedAgentBase(AgentBase):
    """Enhanced agent base with model selection capabilities"""
    
    def __init__(self, agent_id: str = None, agent_type: str = "development",
                 work_package: str = None, metadata: Dict[str, Any] = None):
        super().__init__(agent_id, agent_type, work_package, metadata)
        
        # Model routing components
        self.complexity_analyzer = TaskComplexityAnalyzer()
        self.model_selector = ModelSelector()
        
        # Intelligence components
        self.thinking = get_thinking_integration()
        self.memory = get_memory_integration()
        
        # Current model and routing state
        self.current_model = "claude-opus-4"  # Default
        self.routing_enabled = True
        self.model_override = None
        
        # Task analysis cache
        self.task_analysis_cache = {}
        self.thinking_results = []
    
    async def execute_task(self, task: Dict[str, Any]):
        """Execute task with model selection and intelligence"""
        task_id = task.get("id", "unknown")
        task_description = task.get("description", "")
        
        # Think through the task first
        thinking_result = await self.think_about_task(task_description, task)
        self.thinking_results.append(thinking_result)
        
        # Retrieve relevant memories
        memories = await self.retrieve_relevant_memories(task_description)
        
        # Analyze task complexity
        analysis = await self.analyze_task(task_description, task)
        
        # Select model based on analysis
        model_selection = self.model_selector.select_model(
            analysis, 
            self.agent_type,
            force_model=self.model_override
        )
        
        # Update current model
        self.current_model = model_selection.primary_model
        
        # Log model selection
        self.log(f"Task {task_id} routed to {self.current_model}")
        self.log(f"Reasoning: {', '.join(model_selection.reasoning[:2])}")
        
        if model_selection.warnings:
            for warning in model_selection.warnings:
                self.log(f"Warning: {warning}", "WARN")
        
        # Add model info to task metadata
        task["model_selection"] = {
            "model": self.current_model,
            "complexity": analysis.complexity_level.name,
            "estimated_cost": model_selection.estimated_cost
        }
        
        # Execute with selected model
        return await super().execute_task(task)
    
    async def analyze_task(self, description: str, task: Dict[str, Any]) -> Any:
        """Analyze task complexity with caching"""
        # Check cache
        cache_key = f"{description[:50]}_{task.get('type', 'unknown')}"
        if cache_key in self.task_analysis_cache:
            return self.task_analysis_cache[cache_key]
        
        # Build context for analysis
        context = {
            "files_affected": task.get("files_affected", 0),
            "task_type": task.get("type"),
            "priority": task.get("priority", "medium"),
            "dependencies": len(task.get("dependencies", []))
        }
        
        # Analyze
        analysis = self.complexity_analyzer.analyze_task(description, context)
        
        # Cache result
        self.task_analysis_cache[cache_key] = analysis
        
        return analysis
    
    def set_routing_enabled(self, enabled: bool):
        """Enable or disable model routing"""
        self.routing_enabled = enabled
        self.log(f"Model routing {'enabled' if enabled else 'disabled'}")
    
    def force_model(self, model: Optional[str]):
        """Force a specific model for all tasks"""
        self.model_override = model
        if model:
            self.log(f"Forcing all tasks to use {model}")
        else:
            self.log("Model override cleared")
    
    async def route_to_model(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Route task execution to the selected model"""
        model = task.get("model_selection", {}).get("model", self.current_model)
        
        if model == "kimi-pro":
            return await self._execute_with_kimi(task)
        elif model == "gemini-mcp":
            return await self._execute_with_gemini(task)
        else:
            return await self._execute_with_claude(task)
    
    async def _execute_with_claude(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task with Claude (native)"""
        # This is the default execution path
        return await self.default_task_handler(task)
    
    async def _execute_with_kimi(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task with Kimi Pro"""
        self.log(f"Routing to Kimi Pro: {task.get('id')}")
        
        # Import here to avoid circular dependencies
        from ..clients import route_to_kimi
        
        try:
            # Prepare task context
            context = {
                "files": task.get("context_files", {}),
                "agent_type": self.agent_type,
                "task_type": task.get("type", "general")
            }
            
            # Route to Kimi
            result = await route_to_kimi(
                task.get("description", ""),
                context
            )
            
            self.log(f"Kimi completed task: {task.get('id')} (cost: ${result['cost']})")
            
            return result
            
        except Exception as e:
            self.log(f"Kimi routing failed: {e}, falling back to Claude", "WARN")
            # Fall back to Claude
            return await self._execute_with_claude(task)
    
    async def _execute_with_gemini(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task with Gemini"""
        self.log(f"Routing to Gemini: {task.get('id')}")
        
        # Import here to avoid circular dependencies
        from ..clients import route_to_gemini
        
        try:
            # Prepare task context
            context = {
                "files": task.get("context_files", {}),
                "agent_type": self.agent_type,
                "task_type": task.get("type", "analysis")
            }
            
            # Route to Gemini
            result = await route_to_gemini(
                task.get("description", ""),
                context
            )
            
            self.log(f"Gemini completed task: {task.get('id')} (cost: ${result['cost']})")
            
            return result
            
        except Exception as e:
            self.log(f"Gemini routing failed: {e}, falling back to Claude", "WARN")
            # Fall back to Claude
            return await self._execute_with_claude(task)
    
    def get_model_stats(self) -> Dict[str, Any]:
        """Get model usage statistics"""
        return self.model_selector.get_usage_report()
    
    async def report_task_completion(self, task_id: str, result: Dict[str, Any]):
        """Report task completion with model metrics"""
        # Update model selector stats
        if task_id in self.task_analysis_cache:
            analysis = self.task_analysis_cache[task_id]
            self.model_selector._update_usage_stats(self.current_model, analysis)
        
        # Report progress with model info
        self.report_progress(
            100,
            f"Task {task_id} completed using {self.current_model}"
        )
    
    async def think_about_task(self, task_description: str, task: Dict[str, Any]) -> Dict[str, Any]:
        """Use Sequential Thinking to reason about the task"""
        
        # Prepare context from task
        context = {
            "files": task.get("context_files", {}),
            "constraints": task.get("constraints", []),
            "priority": task.get("priority", "medium")
        }
        
        # Think through the task
        thinking_result = await self.thinking.think_through_task(
            task_description=task_description,
            agent_type=self.agent_type,
            context=context
        )
        
        # Store insights as memories
        for insight in thinking_result.get("insights", []):
            await self.memory.store_agent_memory(
                agent_id=self.agent_id,
                agent_type=self.agent_type,
                memory_type="insight",
                content={
                    "task": task_description,
                    "insight": insight,
                    "thinking_stage": "analysis"
                }
            )
        
        return thinking_result
    
    async def retrieve_relevant_memories(self, query: str) -> List[Dict[str, Any]]:
        """Retrieve memories relevant to current task"""
        
        memories = await self.memory.retrieve_relevant_memories(
            query=query,
            agent_type=self.agent_type,
            limit=5
        )
        
        self.log(f"Retrieved {len(memories)} relevant memories")
        
        return memories
    
    async def share_learnings(self, target_agents: List[str]):
        """Share learnings with other agents"""
        
        # Share recent insights and patterns
        await self.memory.share_memories_between_agents(
            from_agent=self.agent_id,
            to_agents=target_agents,
            memory_filter={
                "type": "insight",
                "agent_type": self.agent_type
            }
        )
        
        self.log(f"Shared learnings with {len(target_agents)} agents")
    
    async def extract_patterns_from_work(self, work_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract patterns from completed work"""
        
        # Store work results as facts
        await self.memory.store_agent_memory(
            agent_id=self.agent_id,
            agent_type=self.agent_type,
            memory_type="fact",
            content={
                "work_completed": work_results.get("description", ""),
                "files_modified": work_results.get("files_modified", []),
                "outcome": work_results.get("outcome", "success")
            }
        )
        
        # Extract patterns if multiple similar tasks
        agent_results = [work_results]  # In real use, would aggregate multiple results
        patterns = await self.memory.extract_patterns_from_results(agent_results)
        
        return patterns