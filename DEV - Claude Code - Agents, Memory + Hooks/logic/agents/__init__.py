"""
Agent Intelligence Modules

This directory contains intelligence and enhancement modules that work
automatically through the hook system to improve Claude Code's capabilities.

Structure:
- intelligence/: Core intelligence integrations (Sequential Thinking, Graphiti, MCP)
- compatibility_layer.py: Ensures agents integrate with existing hooks
- z__archive/: Archived over-engineered components from v3
"""

# Version info
__version__ = "2.1.0"
__author__ = "Claude Code Assistant"

# Import key components for easy access
# Note: intelligence modules are in integrations directory now
try:
    from .integrations.sequential_thinking_integration import SequentialThinkingIntegration
    from .integrations.graphiti_memory_integration import GraphitiMemoryIntegration
    from .utils.graphiti_memory_bridge import MemoryBridge
except ImportError:
    # Modules may not be fully implemented yet
    SequentialThinkingIntegration = None
    GraphitiMemoryIntegration = None
    MemoryBridge = None

from .compatibility_layer import AgentCompatibilityLayer

# Core agent components
from .core.orchestrator import Orchestrator, TaskComplexity
from .core.routing_engine import SmartRoutingEngine

__all__ = [
    "SequentialThinkingIntegration",
    "GraphitiMemoryIntegration",
    "MemoryBridge",
    "AgentCompatibilityLayer",
    "Orchestrator",
    "TaskComplexity",
    "SmartRoutingEngine"
]