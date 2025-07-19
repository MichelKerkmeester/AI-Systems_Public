"""
Orchestration Module - Multi-Agent Coordination

Provides parallel orchestration with worktree isolation and intelligent synthesis.
"""

from .parallel_orchestrator import ParallelOrchestrator, OrchestratorState, WorkPackage, AgentInfo
from .orchestrator_command import orchestrator_command

__all__ = [
    "ParallelOrchestrator",
    "OrchestratorState", 
    "WorkPackage",
    "AgentInfo",
    "orchestrator_command"
]