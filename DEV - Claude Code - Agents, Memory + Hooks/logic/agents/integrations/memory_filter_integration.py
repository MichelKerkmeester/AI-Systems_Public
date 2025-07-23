#!/usr/bin/env python3
"""
Memory Filter Integration for Agent System
Connects the optimized Crawl4AI memory filter with the agent architecture
"""

import json
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path
import sys

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import the optimized memory filter using importlib
import importlib.util
spec = importlib.util.spec_from_file_location(
    "crawl4ai_memory_filter_optimized",
    str(Path(__file__).parent.parent.parent / "memory" / "crawl4ai-memory-filter-optimized.py")
)
crawl4ai_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(crawl4ai_module)
OptimizedCrawl4AIMemoryFilter = crawl4ai_module.OptimizedCrawl4AIMemoryFilter

logger = logging.getLogger(__name__)

class AgentMemoryIntegration:
    """
    Integrates the optimized memory filter with the agent system
    Provides agent-specific memory storage and retrieval
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize memory integration with agent-specific configuration"""
        # Default agent-optimized configuration
        default_config = {
            'thresholds': {
                'neo4j': 0.8,           # High threshold for graph storage
                'supabase': 0.2,        # Lower threshold for RAG
                'entity_extraction': 0.7 # Only extract for promising content
            },
            'performance': {
                'batch_size': 20,       # Optimized for agent parallel processing
                'max_queue_size': 1000,
                'worker_threads': 4,
                'cache_size': 1000,
                'circuit_breaker_threshold': 5
            },
            'features': {
                'use_batching': True,
                'use_caching': True,
                'use_circuit_breaker': True,
                'collect_metrics': True
            },
            'agent_specific': {
                'capture_decisions': True,
                'capture_routing': True,
                'capture_cost_data': True,
                'agent_memory_prefix': 'agent_'
            }
        }
        
        self.config = {**default_config, **(config or {})}
        
        # Initialize the optimized memory filter
        self.memory_filter = OptimizedCrawl4AIMemoryFilter(self.config)
        
        # Agent-specific memory patterns
        self.agent_patterns = {
            'orchestrator': {
                'task_decomposition': r'decomposed.*into.*subtasks',
                'routing_decision': r'routed.*to.*agent',
                'cost_optimization': r'cost.*reduced.*by'
            },
            'implementation': {
                'code_generation': r'generated.*code|implemented.*function',
                'refactoring': r'refactored.*to|improved.*performance',
                'bug_fix': r'fixed.*issue|resolved.*error'
            },
            'analysis': {
                'pattern_detection': r'detected.*pattern|found.*similarity',
                'code_review': r'reviewed.*code|analyzed.*implementation',
                'security_scan': r'security.*vulnerability|potential.*risk'
            },
            'quality_assurance': {
                'test_validation': r'validated.*tests|coverage.*achieved',
                'quality_check': r'quality.*score|code.*standards',
                'security_audit': r'security.*audit|vulnerability.*scan'
            }
        }
        
        # Track agent-specific metrics
        self.agent_metrics = {
            'memories_per_agent': {},
            'routing_patterns': {},
            'cost_patterns': {}
        }
    
    def capture_agent_memory(self, agent_type: str, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Capture memory specific to an agent's operation
        
        Args:
            agent_type: Type of agent (orchestrator, implementation, etc.)
            content: Memory content to capture
            
        Returns:
            Processing result from memory filter
        """
        # Enhance content with agent metadata
        enhanced_content = {
            **content,
            'agent_type': agent_type,
            'agent_timestamp': content.get('timestamp'),
            'url': f"agent://{agent_type}/{content.get('task_id', 'unknown')}"
        }
        
        # Add agent-specific patterns to boost relevance
        if agent_type in self.agent_patterns:
            patterns = self.agent_patterns[agent_type]
            text = content.get('text', '')
            
            # Check for pattern matches
            matched_patterns = []
            for pattern_name, pattern_regex in patterns.items():
                if self._matches_pattern(text, pattern_regex):
                    matched_patterns.append(f"agent_{agent_type}_{pattern_name}")
            
            if matched_patterns:
                enhanced_content['matched_agent_patterns'] = matched_patterns
        
        # Process through memory filter
        result = self.memory_filter.process_crawled_content(enhanced_content)
        
        # Track metrics
        self._update_agent_metrics(agent_type, result)
        
        return result
    
    def capture_routing_decision(self, routing_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Capture routing decisions for pattern learning
        
        Args:
            routing_data: Contains task, selected model, reasoning, cost estimate
        """
        content = {
            'text': f"Routing Decision: {routing_data.get('task', 'Unknown task')} → {routing_data.get('model', 'Unknown model')}",
            'routing_details': routing_data,
            'type': 'routing_decision',
            'relevance_boost': 0.2  # Boost relevance for routing decisions
        }
        
        return self.capture_agent_memory('orchestrator', content)
    
    def capture_cost_optimization(self, cost_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Capture cost optimization data for analysis
        
        Args:
            cost_data: Contains original cost, optimized cost, savings percentage
        """
        content = {
            'text': f"Cost Optimization: Saved {cost_data.get('savings_percent', 0):.1f}% on {cost_data.get('task', 'task')}",
            'cost_details': cost_data,
            'type': 'cost_optimization',
            'relevance_boost': 0.3  # High relevance for cost data
        }
        
        return self.capture_agent_memory('orchestrator', content)
    
    def capture_implementation_result(self, impl_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Capture implementation results and patterns
        
        Args:
            impl_data: Contains code generated, patterns used, quality metrics
        """
        content = {
            'text': impl_data.get('summary', 'Implementation completed'),
            'code_snippet': impl_data.get('code', '')[:500],  # Limit code size
            'patterns_used': impl_data.get('patterns', []),
            'quality_score': impl_data.get('quality_score', 0),
            'type': 'implementation_result'
        }
        
        agent_type = impl_data.get('agent_type', 'implementation')
        return self.capture_agent_memory(agent_type, content)
    
    def get_agent_context(self, agent_type: str, task: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context for an agent
        
        Args:
            agent_type: Type of agent requesting context
            task: Current task description
            limit: Maximum number of memories to retrieve
            
        Returns:
            List of relevant memories
        """
        # This would integrate with Graphiti MCP for actual retrieval
        # For now, return placeholder
        logger.info(f"Retrieving context for {agent_type} agent: {task[:50]}...")
        
        # Simulate context retrieval
        return [
            {
                'type': 'previous_implementation',
                'relevance': 0.9,
                'content': 'Similar task implemented using pattern X'
            }
        ]
    
    def get_routing_history(self, task_pattern: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get historical routing decisions for similar tasks
        
        Args:
            task_pattern: Pattern to match against previous tasks
            limit: Maximum results
            
        Returns:
            List of routing decisions with performance data
        """
        # This would query Neo4j for routing patterns
        logger.info(f"Retrieving routing history for pattern: {task_pattern}")
        
        return self.agent_metrics.get('routing_patterns', {}).get(task_pattern, [])[:limit]
    
    def get_cost_analytics(self) -> Dict[str, Any]:
        """
        Get cost analytics across all agents
        
        Returns:
            Cost breakdown by agent type, model, and task type
        """
        return {
            'total_memories': sum(self.agent_metrics['memories_per_agent'].values()),
            'by_agent': self.agent_metrics['memories_per_agent'],
            'cost_patterns': self.agent_metrics['cost_patterns'],
            'memory_filter_stats': self.memory_filter.get_stats()
        }
    
    def _matches_pattern(self, text: str, pattern: str) -> bool:
        """Check if text matches a pattern"""
        import re
        try:
            return bool(re.search(pattern, text, re.IGNORECASE))
        except:
            return False
    
    def _update_agent_metrics(self, agent_type: str, result: Dict[str, Any]):
        """Update agent-specific metrics"""
        # Update memory count
        if agent_type not in self.agent_metrics['memories_per_agent']:
            self.agent_metrics['memories_per_agent'][agent_type] = 0
        self.agent_metrics['memories_per_agent'][agent_type] += 1
        
        # Track routing patterns if applicable
        if result.get('metadata', {}).get('routing_details'):
            routing = result['metadata']['routing_details']
            pattern_key = f"{routing.get('task_type', 'unknown')}_{routing.get('model', 'unknown')}"
            
            if pattern_key not in self.agent_metrics['routing_patterns']:
                self.agent_metrics['routing_patterns'][pattern_key] = []
            
            self.agent_metrics['routing_patterns'][pattern_key].append({
                'timestamp': result.get('timestamp'),
                'cost': routing.get('estimated_cost', 0),
                'confidence': routing.get('confidence', 0)
            })
    
    def shutdown(self):
        """Graceful shutdown of memory integration"""
        logger.info("Shutting down Agent Memory Integration...")
        
        # Print final metrics
        print("Agent Memory Metrics:")
        print(json.dumps(self.get_cost_analytics(), indent=2))
        
        # Shutdown memory filter
        self.memory_filter.shutdown()


# Integration helper functions
def create_agent_memory_integration(config: Optional[Dict[str, Any]] = None) -> AgentMemoryIntegration:
    """Factory function to create memory integration"""
    return AgentMemoryIntegration(config)


def capture_agent_decision(agent_type: str, decision_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convenience function to capture agent decisions
    Uses a singleton memory integration instance
    """
    global _memory_integration
    if '_memory_integration' not in globals():
        _memory_integration = create_agent_memory_integration()
    
    return _memory_integration.capture_agent_memory(agent_type, decision_data)


# Example usage
if __name__ == '__main__':
    # Create integration
    memory_integration = create_agent_memory_integration()
    
    # Example: Capture routing decision
    routing_decision = {
        'task': 'Implement slider component with animations',
        'model': 'qwen3_coder',
        'reasoning': 'Complex implementation requiring 50K context',
        'estimated_cost': 0.38,
        'confidence': 0.92
    }
    result = memory_integration.capture_routing_decision(routing_decision)
    print("Routing capture result:", result)
    
    # Example: Capture cost optimization
    cost_data = {
        'task': 'Generate API documentation',
        'original_cost': 4.50,
        'optimized_cost': 0.12,
        'savings_percent': 97.3,
        'model_used': 'gemini_flash'
    }
    result = memory_integration.capture_cost_optimization(cost_data)
    print("Cost capture result:", result)
    
    # Get analytics
    print("\nCost Analytics:")
    print(json.dumps(memory_integration.get_cost_analytics(), indent=2))
    
    # Shutdown
    memory_integration.shutdown()