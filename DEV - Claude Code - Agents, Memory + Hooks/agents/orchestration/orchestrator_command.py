"""
Orchestrator Command Handler

Provides high-level commands for orchestrating multi-agent workflows.
"""

import asyncio
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

from .parallel_orchestrator import ParallelOrchestrator, OrchestratorState


class OrchestratorCommand:
    """Command handler for orchestrator operations"""
    
    def __init__(self):
        self.orchestrators: Dict[str, ParallelOrchestrator] = {}
        self.config_path = Path(__file__).parent.parent / "configs" / "orchestrator-config.json"
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load orchestrator configuration"""
        if self.config_path.exists():
            with open(self.config_path) as f:
                return json.load(f)
        return {}
    
    async def start_orchestration(self, task_description: str, 
                                options: Dict[str, Any] = None) -> Dict[str, Any]:
        """Start a new orchestration"""
        options = options or {}
        
        # Create orchestrator
        max_agents = options.get("max_agents", self.config.get("orchestrator", {}).get("max_agents", 5))
        orchestrator = ParallelOrchestrator(max_agents=max_agents)
        
        # Store reference
        self.orchestrators[orchestrator.orchestrator_id] = orchestrator
        
        # Initialize
        await orchestrator.initialize()
        
        # Analyze and decompose main task
        work_packages = await self._decompose_task(task_description, orchestrator)
        
        # Start execution
        asyncio.create_task(self._run_orchestration(orchestrator, work_packages))
        
        return {
            "orchestrator_id": orchestrator.orchestrator_id,
            "status": "started",
            "work_packages": len(work_packages),
            "max_agents": max_agents
        }
    
    async def _decompose_task(self, task_description: str, 
                            orchestrator: ParallelOrchestrator) -> List[Dict[str, Any]]:
        """Decompose task into work packages"""
        # Simple decomposition for demo
        # In production, would use AnalystAgent for this
        
        work_packages = []
        
        # Analyze task type
        task_lower = task_description.lower()
        
        if "refactor" in task_lower:
            work_packages = [
                {"description": "Analyze current implementation", "type": "analysis"},
                {"description": "Design refactored architecture", "type": "design", 
                 "dependencies": ["wp_0"]},
                {"description": "Implement refactoring", "type": "implement",
                 "dependencies": ["wp_1"]},
                {"description": "Review refactored code", "type": "review",
                 "dependencies": ["wp_2"]},
                {"description": "Write tests for refactored code", "type": "test",
                 "dependencies": ["wp_2"]}
            ]
        elif "feature" in task_lower:
            work_packages = [
                {"description": "Research requirements and constraints", "type": "research"},
                {"description": "Design feature architecture", "type": "design",
                 "dependencies": ["wp_0"]},
                {"description": "Implement core functionality", "type": "implement",
                 "dependencies": ["wp_1"]},
                {"description": "Implement edge cases", "type": "implement",
                 "dependencies": ["wp_2"]},
                {"description": "Security review", "type": "security",
                 "dependencies": ["wp_2", "wp_3"]},
                {"description": "Write comprehensive tests", "type": "test",
                 "dependencies": ["wp_2", "wp_3"]}
            ]
        elif "bug" in task_lower or "fix" in task_lower:
            work_packages = [
                {"description": "Reproduce and analyze bug", "type": "analysis"},
                {"description": "Identify root cause", "type": "research",
                 "dependencies": ["wp_0"]},
                {"description": "Implement fix", "type": "fix",
                 "dependencies": ["wp_1"]},
                {"description": "Test fix thoroughly", "type": "test",
                 "dependencies": ["wp_2"]},
                {"description": "Review fix for side effects", "type": "review",
                 "dependencies": ["wp_2"]}
            ]
        else:
            # Generic task breakdown
            work_packages = [
                {"description": f"Analyze: {task_description[:50]}...", "type": "analysis"},
                {"description": f"Implement: {task_description[:50]}...", "type": "implement",
                 "dependencies": ["wp_0"]},
                {"description": f"Review: {task_description[:50]}...", "type": "review",
                 "dependencies": ["wp_1"]}
            ]
        
        # Add IDs
        for i, wp in enumerate(work_packages):
            wp["id"] = f"wp_{i}"
        
        return work_packages
    
    async def _run_orchestration(self, orchestrator: ParallelOrchestrator,
                               work_packages: List[Dict[str, Any]]):
        """Run orchestration in background"""
        try:
            await orchestrator.execute(work_packages)
        except Exception as e:
            print(f"Orchestration error: {e}")
        finally:
            await orchestrator.shutdown()
    
    def get_status(self, orchestrator_id: str = None) -> Dict[str, Any]:
        """Get orchestrator status"""
        if orchestrator_id:
            if orchestrator_id in self.orchestrators:
                return self.orchestrators[orchestrator_id].get_status()
            else:
                return {"error": f"Orchestrator {orchestrator_id} not found"}
        else:
            # Return all orchestrators
            return {
                oid: orch.get_status()
                for oid, orch in self.orchestrators.items()
            }
    
    async def stop_orchestration(self, orchestrator_id: str) -> Dict[str, Any]:
        """Stop an orchestration"""
        if orchestrator_id not in self.orchestrators:
            return {"error": f"Orchestrator {orchestrator_id} not found"}
        
        orchestrator = self.orchestrators[orchestrator_id]
        await orchestrator.shutdown()
        
        # Remove from active list
        del self.orchestrators[orchestrator_id]
        
        return {
            "orchestrator_id": orchestrator_id,
            "status": "stopped"
        }
    
    def list_orchestrations(self) -> List[Dict[str, Any]]:
        """List all orchestrations"""
        return [
            {
                "orchestrator_id": oid,
                "state": orch.state.value,
                "agents": len(orch.agents),
                "work_packages": len(orch.work_packages)
            }
            for oid, orch in self.orchestrators.items()
        ]
    
    async def send_message(self, orchestrator_id: str, message: Dict[str, Any]) -> Dict[str, Any]:
        """Send message to orchestrator"""
        if orchestrator_id not in self.orchestrators:
            return {"error": f"Orchestrator {orchestrator_id} not found"}
        
        orchestrator = self.orchestrators[orchestrator_id]
        await orchestrator.message_queue.put(message)
        
        return {"status": "message_sent"}


# Global instance
orchestrator_command = OrchestratorCommand()