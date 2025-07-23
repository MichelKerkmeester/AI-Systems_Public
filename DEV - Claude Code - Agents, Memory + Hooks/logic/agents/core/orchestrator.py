#!/usr/bin/env python3
"""
Orchestrator Agent for Unified Agent Architecture
Routes tasks intelligently based on complexity and cost optimization
"""

import json
import asyncio
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import logging
from pathlib import Path
import sys

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import memory integration
from integrations.memory_filter_integration import AgentMemoryIntegration

logger = logging.getLogger(__name__)

class TaskComplexity(Enum):
    """Task complexity levels for routing decisions"""
    SIMPLE = "simple"       # <100 lines, single file
    MEDIUM = "medium"       # Multi-file, refactoring
    COMPLEX = "complex"     # Architecture changes, security critical
    ANALYSIS = "analysis"   # Code analysis, pattern detection

@dataclass
class SubTask:
    """Represents a decomposed subtask"""
    id: str
    description: str
    complexity: TaskComplexity
    estimated_tokens: int
    dependencies: List[str] = None
    context_needed: Dict[str, Any] = None

@dataclass
class AgentSelection:
    """Selected agent for a task"""
    agent_type: str
    model: str
    context_limit: int
    estimated_cost: float
    fallback_agent: Optional[str] = None

class Orchestrator:
    """Master coordinator for task routing and result aggregation"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.routing_rules = config.get('routing_rules', {})
        self.cost_limits = config.get('cost_limits', {})
        self.model_configs = config.get('model_configs', {})
        
        # Initialize memory integration
        self.memory_integration = AgentMemoryIntegration(config.get('memory_config', {}))
        
        # Track orchestration metrics
        self.orchestration_metrics = {
            'tasks_processed': 0,
            'total_cost': 0.0,
            'cost_savings': 0.0,
            'routing_decisions': []
        }
        
    async def decompose_task(self, task: str, context: Dict[str, Any] = None) -> List[SubTask]:
        """
        Decompose a complex task into manageable subtasks
        """
        # Analyze task complexity
        complexity = self._assess_complexity(task, context)
        
        if complexity == TaskComplexity.SIMPLE:
            # Single subtask for simple operations
            return [SubTask(
                id="task_1",
                description=task,
                complexity=complexity,
                estimated_tokens=self._estimate_tokens(task),
                context_needed=context
            )]
        
        # For complex tasks, break down into components
        subtasks = []
        
        # Example decomposition logic
        if "implement" in task.lower() and "test" in task.lower():
            subtasks.extend([
                SubTask(
                    id="task_1",
                    description=f"Analyze requirements and existing code for: {task}",
                    complexity=TaskComplexity.ANALYSIS,
                    estimated_tokens=2000,
                    context_needed={"codebase_analysis": True}
                ),
                SubTask(
                    id="task_2", 
                    description=f"Implement core functionality for: {task}",
                    complexity=TaskComplexity.MEDIUM,
                    estimated_tokens=5000,
                    dependencies=["task_1"],
                    context_needed={"implementation": True}
                ),
                SubTask(
                    id="task_3",
                    description=f"Write comprehensive tests for: {task}",
                    complexity=TaskComplexity.MEDIUM,
                    estimated_tokens=3000,
                    dependencies=["task_2"],
                    context_needed={"testing": True}
                )
            ])
        else:
            # Default decomposition
            subtasks.append(SubTask(
                id="task_1",
                description=task,
                complexity=complexity,
                estimated_tokens=self._estimate_tokens(task),
                context_needed=context
            ))
        
        return subtasks
    
    def route_subtask(self, subtask: SubTask) -> AgentSelection:
        """
        Route subtask to appropriate agent based on complexity and cost
        """
        # Get relevant context from memory
        memory_context = self.memory_integration.get_agent_context(
            'orchestrator', 
            subtask.description, 
            limit=3
        )
        
        # Check static routing rules first
        for rule in self.routing_rules.get('static', []):
            if self._matches_rule(subtask, rule):
                selection = self._create_agent_selection(rule['agent'], subtask)
                self._capture_routing_decision(subtask, selection, "static_rule", memory_context)
                return selection
        
        # Dynamic routing based on complexity
        if subtask.complexity == TaskComplexity.SIMPLE:
            selection = AgentSelection(
                agent_type="implementation",
                model="qwen3_simple",
                context_limit=4000,
                estimated_cost=subtask.estimated_tokens * 0.000003,  # $3/1M
                fallback_agent="qwen3_coder"
            )
            reasoning = "Simple task routed to efficient model"
        
        elif subtask.complexity == TaskComplexity.ANALYSIS:
            selection = AgentSelection(
                agent_type="analysis",
                model="gemini_flash",
                context_limit=100000,
                estimated_cost=subtask.estimated_tokens * 0.00000026,  # $0.26/1M
                fallback_agent="qwen3_coder"
            )
            reasoning = "Analysis task routed to fast multimodal model"
        
        elif subtask.complexity == TaskComplexity.MEDIUM:
            selection = AgentSelection(
                agent_type="implementation",
                model="qwen3_coder",
                context_limit=50000,
                estimated_cost=subtask.estimated_tokens * 0.0000075,  # $7.50/1M
                fallback_agent="opus"
            )
            reasoning = "Medium complexity task routed to QWEN3-Coder"
        
        else:  # COMPLEX
            selection = AgentSelection(
                agent_type="quality_assurance",
                model="opus",
                context_limit=20000,
                estimated_cost=subtask.estimated_tokens * 0.00003,  # $30/1M
                fallback_agent=None
            )
            reasoning = "Complex/critical task requires highest quality model"
        
        # Capture routing decision
        self._capture_routing_decision(subtask, selection, reasoning, memory_context)
        
        return selection
    
    async def aggregate_results(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Aggregate results from multiple agents into final output
        """
        if len(results) == 1:
            return results[0]
        
        # Combine results intelligently
        aggregated = {
            "status": "success",
            "components": [],
            "total_cost": sum(r.get('cost', 0) for r in results),
            "total_tokens": sum(r.get('tokens', 0) for r in results),
            "execution_time": sum(r.get('time', 0) for r in results)
        }
        
        # Merge outputs based on task dependencies
        for result in results:
            aggregated["components"].append({
                "task_id": result.get('task_id'),
                "output": result.get('output'),
                "model_used": result.get('model_used')
            })
        
        return aggregated
    
    def validate_quality(self, output: Dict[str, Any]) -> Tuple[float, List[str]]:
        """
        Validate output quality and determine if Opus validation needed
        """
        quality_score = 1.0
        issues = []
        
        # Check for common quality indicators
        if output.get('error_count', 0) > 0:
            quality_score -= 0.2
            issues.append("Errors detected in output")
        
        if output.get('test_coverage', 100) < 80:
            quality_score -= 0.1
            issues.append("Insufficient test coverage")
        
        if output.get('complexity_score', 0) > 50:
            quality_score -= 0.1
            issues.append("High complexity detected")
        
        # Security-critical tasks always need validation
        if output.get('security_critical', False):
            quality_score = min(quality_score, 0.7)
            issues.append("Security-critical code requires validation")
        
        return quality_score, issues
    
    def _assess_complexity(self, task: str, context: Dict[str, Any] = None) -> TaskComplexity:
        """Assess task complexity based on keywords and context"""
        task_lower = task.lower()
        
        # Simple tasks
        if any(keyword in task_lower for keyword in ['fix typo', 'add comment', 'rename', 'simple']):
            return TaskComplexity.SIMPLE
        
        # Analysis tasks
        if any(keyword in task_lower for keyword in ['analyze', 'review', 'check', 'find', 'search']):
            return TaskComplexity.ANALYSIS
        
        # Complex tasks
        if any(keyword in task_lower for keyword in ['architecture', 'security', 'production', 'critical']):
            return TaskComplexity.COMPLEX
        
        # Default to medium
        return TaskComplexity.MEDIUM
    
    def _estimate_tokens(self, task: str) -> int:
        """Estimate token count for a task"""
        # Rough estimation: 4 chars = 1 token
        base_tokens = len(task) // 4
        
        # Add buffer for response
        return base_tokens * 20  # Assume 20x expansion
    
    def _matches_rule(self, subtask: SubTask, rule: Dict[str, Any]) -> bool:
        """Check if subtask matches a routing rule"""
        if 'keywords' in rule:
            task_lower = subtask.description.lower()
            return any(keyword in task_lower for keyword in rule['keywords'])
        return False
    
    def _create_agent_selection(self, agent_config: Dict[str, Any], subtask: SubTask) -> AgentSelection:
        """Create agent selection from configuration"""
        model = agent_config['model']
        model_config = self.model_configs.get(model, {})
        
        return AgentSelection(
            agent_type=agent_config['type'],
            model=model,
            context_limit=model_config.get('context_limit', 10000),
            estimated_cost=subtask.estimated_tokens * model_config.get('cost_per_token', 0.00001),
            fallback_agent=agent_config.get('fallback')
        )
    
    def _capture_routing_decision(self, subtask: SubTask, selection: AgentSelection, 
                                reasoning: str, memory_context: List[Dict]) -> None:
        """Capture routing decision to memory for pattern learning"""
        # Calculate cost savings vs Opus
        opus_cost = subtask.estimated_tokens * 0.00003
        savings_percent = ((opus_cost - selection.estimated_cost) / opus_cost) * 100 if opus_cost > 0 else 0
        
        routing_data = {
            'task': subtask.description,
            'task_id': subtask.id,
            'complexity': subtask.complexity.value,
            'model': selection.model,
            'agent_type': selection.agent_type,
            'reasoning': reasoning,
            'estimated_cost': selection.estimated_cost,
            'opus_cost': opus_cost,
            'savings_percent': savings_percent,
            'confidence': 0.9,  # Default high confidence
            'memory_context_used': len(memory_context) > 0
        }
        
        # Capture to memory
        self.memory_integration.capture_routing_decision(routing_data)
        
        # Update metrics
        self.orchestration_metrics['routing_decisions'].append(routing_data)
        self.orchestration_metrics['cost_savings'] += opus_cost - selection.estimated_cost
        
        # Log decision
        logger.info(f"Routing: {subtask.id} → {selection.model} (saved {savings_percent:.1f}%)")
    
    def get_orchestration_metrics(self) -> Dict[str, Any]:
        """Get current orchestration metrics"""
        return {
            **self.orchestration_metrics,
            'memory_stats': self.memory_integration.get_cost_analytics()
        }