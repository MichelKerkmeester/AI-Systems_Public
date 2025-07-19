"""
Parallel Orchestrator - Enhanced Multi-Agent Coordination

Manages parallel execution of multiple agents with:
- Git worktree isolation for conflict-free development
- Inter-agent messaging with model tracking
- Automatic synthesis agent spawning
- Intelligent work distribution
"""

import os
import asyncio
import subprocess
import uuid
import json
from typing import Dict, Any, List, Optional, Set
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "logic" / "shared"))

from types import AnalystAgent, DeveloperAgent, ReviewerAgent, SynthesisAgent
from routing import TaskComplexityAnalyzer, ModelSelector, ComplexityLevel
from intelligence import get_memory_integration, get_conflict_resolution
from intelligence.conflict_resolution import ConflictType


class OrchestratorState(Enum):
    """Orchestrator lifecycle states"""
    INITIALIZING = "initializing"
    READY = "ready"
    RUNNING = "running"
    SYNTHESIZING = "synthesizing"
    COMPLETING = "completing"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class WorkPackage:
    """Work package for agent assignment"""
    id: str
    description: str
    type: str
    complexity: ComplexityLevel
    dependencies: List[str] = field(default_factory=list)
    assigned_agent: Optional[str] = None
    status: str = "pending"
    result: Optional[Dict[str, Any]] = None
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None


@dataclass
class AgentInfo:
    """Agent registration information"""
    agent_id: str
    agent_type: str
    agent_instance: Any
    worktree_path: Optional[str] = None
    branch_name: Optional[str] = None
    status: str = "idle"
    current_task: Optional[str] = None
    tasks_completed: int = 0
    model_stats: Dict[str, int] = field(default_factory=dict)


class ParallelOrchestrator:
    """Enhanced orchestrator for multi-agent parallel execution"""
    
    def __init__(self, project_root: str = None, max_agents: int = 5):
        self.orchestrator_id = f"orchestrator_{uuid.uuid4().hex[:8]}"
        self.project_root = project_root or os.getcwd()
        self.max_agents = max_agents
        
        # State management
        self.state = OrchestratorState.INITIALIZING
        self.agents: Dict[str, AgentInfo] = {}
        self.work_packages: Dict[str, WorkPackage] = {}
        self.message_queue: asyncio.Queue = asyncio.Queue()
        
        # Agent pools by type
        self.agent_pools = {
            "analyst": [],
            "developer": [],
            "reviewer": [],
            "synthesis": []
        }
        
        # Model routing components
        self.complexity_analyzer = TaskComplexityAnalyzer()
        self.model_selector = ModelSelector()
        
        # Intelligence components
        self.memory = get_memory_integration()
        self.conflict_resolver = get_conflict_resolution()
        
        # Worktree management
        self.worktree_base = Path.home() / ".claude" / "agents" / "worktrees"
        self.worktree_base.mkdir(parents=True, exist_ok=True)
        
        # Synthesis configuration
        self.auto_synthesis = True
        self.synthesis_threshold = 3  # Min agents for auto-synthesis
        self.synthesis_agent = None
        
        # Logging
        self.log_file = Path(self.project_root) / ".claude" / "agents" / "logs" / f"{self.orchestrator_id}.log"
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
    
    def log(self, message: str, level: str = "INFO"):
        """Log orchestrator events"""
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        print(f"🎯 {log_entry}")
        
        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")
    
    async def initialize(self):
        """Initialize orchestrator"""
        self.log(f"Initializing ParallelOrchestrator {self.orchestrator_id}")
        
        # Start message handler
        asyncio.create_task(self._handle_messages())
        
        # Initialize agent pools
        await self._initialize_agent_pools()
        
        self.state = OrchestratorState.READY
        self.log("Orchestrator ready")
    
    async def add_work_package(self, description: str, work_type: str = "general",
                              dependencies: List[str] = None) -> str:
        """Add a work package to the queue"""
        # Analyze complexity
        analysis = self.complexity_analyzer.analyze_task(description)
        
        # Create work package
        wp_id = f"wp_{uuid.uuid4().hex[:8]}"
        work_package = WorkPackage(
            id=wp_id,
            description=description,
            type=work_type,
            complexity=analysis.complexity_level,
            dependencies=dependencies or []
        )
        
        self.work_packages[wp_id] = work_package
        self.log(f"Added work package {wp_id}: {description[:50]}... (complexity: {analysis.complexity_level.name})")
        
        return wp_id
    
    async def execute(self, work_packages: List[Dict[str, Any]] = None):
        """Execute work packages in parallel"""
        self.state = OrchestratorState.RUNNING
        self.log("Starting parallel execution")
        
        # Add provided work packages
        if work_packages:
            for wp in work_packages:
                await self.add_work_package(
                    wp.get("description", ""),
                    wp.get("type", "general"),
                    wp.get("dependencies", [])
                )
        
        # Main execution loop
        try:
            while self._has_pending_work():
                # Assign work to available agents
                await self._assign_work()
                
                # Check for synthesis opportunities
                if self.auto_synthesis:
                    await self._check_synthesis_trigger()
                
                # Brief pause
                await asyncio.sleep(0.5)
            
            # Final synthesis if needed
            await self._final_synthesis()
            
            self.state = OrchestratorState.COMPLETED
            self.log("Orchestration completed successfully")
            
        except Exception as e:
            self.state = OrchestratorState.ERROR
            self.log(f"Orchestration error: {e}", "ERROR")
            raise
    
    async def shutdown(self):
        """Gracefully shutdown orchestrator"""
        self.log("Shutting down orchestrator...")
        
        # Stop all agents
        for agent_info in self.agents.values():
            await self._stop_agent(agent_info)
        
        # Generate final report
        await self._generate_final_report()
        
        self.log("Orchestrator shutdown complete")
    
    async def _initialize_agent_pools(self):
        """Initialize agent pools with minimum agents"""
        # Start with one analyst
        analyst = await self._spawn_agent("analyst")
        self.agent_pools["analyst"].append(analyst)
        
        # Start with two developers
        for _ in range(2):
            dev = await self._spawn_agent("developer")
            self.agent_pools["developer"].append(dev)
        
        # One reviewer
        reviewer = await self._spawn_agent("reviewer")
        self.agent_pools["reviewer"].append(reviewer)
        
        self.log(f"Initialized {len(self.agents)} agents")
    
    async def _spawn_agent(self, agent_type: str, work_package: str = None) -> AgentInfo:
        """Spawn a new agent"""
        agent_id = f"{agent_type}_{uuid.uuid4().hex[:8]}"
        
        # Create agent instance
        if agent_type == "analyst":
            agent = AnalystAgent(work_package=work_package)
        elif agent_type == "developer":
            agent = DeveloperAgent(work_package=work_package)
        elif agent_type == "reviewer":
            agent = ReviewerAgent(work_package=work_package)
        elif agent_type == "synthesis":
            agent = SynthesisAgent(work_package=work_package)
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        # Set up worktree if needed
        worktree_path = None
        branch_name = None
        
        if agent_type == "developer" and agent.metadata.get("use_worktree", True):
            worktree_path, branch_name = await self._create_worktree(agent_id)
        
        # Create agent info
        agent_info = AgentInfo(
            agent_id=agent_id,
            agent_type=agent_type,
            agent_instance=agent,
            worktree_path=worktree_path,
            branch_name=branch_name
        )
        
        # Register agent
        self.agents[agent_id] = agent_info
        
        # Initialize agent
        await agent.initialize()
        
        # Start agent task
        asyncio.create_task(self._run_agent(agent_info))
        
        self.log(f"Spawned {agent_type} agent: {agent_id}")
        
        return agent_info
    
    async def _create_worktree(self, agent_id: str) -> tuple[str, str]:
        """Create git worktree for agent"""
        worktree_path = self.worktree_base / agent_id
        branch_name = f"agent/{agent_id}"
        
        try:
            # Create worktree
            cmd = f"git worktree add {worktree_path} -b {branch_name}"
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                self.log(f"Worktree creation failed: {result.stderr}", "WARN")
                return None, None
            
            self.log(f"Created worktree for {agent_id} at {worktree_path}")
            return str(worktree_path), branch_name
            
        except Exception as e:
            self.log(f"Worktree error: {e}", "ERROR")
            return None, None
    
    async def _run_agent(self, agent_info: AgentInfo):
        """Run agent lifecycle"""
        agent = agent_info.agent_instance
        
        try:
            # Run agent
            await agent.run()
        except Exception as e:
            self.log(f"Agent {agent_info.agent_id} error: {e}", "ERROR")
            agent_info.status = "error"
        finally:
            # Cleanup
            await agent.cleanup()
            
            # Remove worktree if exists
            if agent_info.worktree_path:
                await self._remove_worktree(agent_info)
    
    async def _assign_work(self):
        """Assign pending work packages to available agents"""
        # Get available work packages
        pending = [
            wp for wp in self.work_packages.values()
            if wp.status == "pending" and self._dependencies_met(wp)
        ]
        
        if not pending:
            return
        
        # Sort by complexity (complex first for better parallelization)
        pending.sort(key=lambda wp: wp.complexity.value, reverse=True)
        
        for work_package in pending:
            # Find suitable agent
            agent = await self._find_suitable_agent(work_package)
            
            if agent:
                # Assign work
                await self._assign_to_agent(work_package, agent)
            else:
                # Spawn new agent if under limit
                if len(self.agents) < self.max_agents:
                    agent_type = self._determine_agent_type(work_package)
                    new_agent = await self._spawn_agent(agent_type, work_package.id)
                    await self._assign_to_agent(work_package, new_agent)
    
    def _dependencies_met(self, work_package: WorkPackage) -> bool:
        """Check if work package dependencies are met"""
        for dep_id in work_package.dependencies:
            if dep_id in self.work_packages:
                dep = self.work_packages[dep_id]
                if dep.status != "completed":
                    return False
        return True
    
    async def _find_suitable_agent(self, work_package: WorkPackage) -> Optional[AgentInfo]:
        """Find suitable available agent for work package"""
        preferred_type = self._determine_agent_type(work_package)
        
        # Check preferred type pool first
        for agent in self.agent_pools.get(preferred_type, []):
            agent_info = self.agents.get(agent.agent_id)
            if agent_info and agent_info.status == "idle":
                return agent_info
        
        # Check other compatible agents
        for agent_info in self.agents.values():
            if agent_info.status == "idle" and self._is_compatible(agent_info, work_package):
                return agent_info
        
        return None
    
    def _determine_agent_type(self, work_package: WorkPackage) -> str:
        """Determine best agent type for work package"""
        wp_type = work_package.type.lower()
        
        if wp_type in ["analysis", "research", "decompose"]:
            return "analyst"
        elif wp_type in ["implement", "refactor", "fix"]:
            return "developer" 
        elif wp_type in ["review", "test", "security"]:
            return "reviewer"
        elif wp_type in ["synthesis", "merge", "integrate"]:
            return "synthesis"
        else:
            # Default based on complexity
            if work_package.complexity.value >= 3:
                return "analyst"
            else:
                return "developer"
    
    def _is_compatible(self, agent_info: AgentInfo, work_package: WorkPackage) -> bool:
        """Check if agent can handle work package"""
        # Synthesis agents are specialized
        if agent_info.agent_type == "synthesis":
            return work_package.type in ["synthesis", "merge", "integrate"]
        
        # Other agents have some flexibility
        return True
    
    async def _assign_to_agent(self, work_package: WorkPackage, agent_info: AgentInfo):
        """Assign work package to agent"""
        # Update work package
        work_package.assigned_agent = agent_info.agent_id
        work_package.status = "in_progress"
        
        # Update agent
        agent_info.status = "working"
        agent_info.current_task = work_package.id
        
        # Create task for agent
        task = {
            "id": work_package.id,
            "type": work_package.type,
            "description": work_package.description,
            "complexity": work_package.complexity.name,
            "dependencies": work_package.dependencies
        }
        
        # Send to agent
        agent_info.agent_instance.add_task(task)
        
        self.log(f"Assigned {work_package.id} to {agent_info.agent_id}")
    
    async def _handle_messages(self):
        """Handle inter-agent messages"""
        while True:
            try:
                message = await asyncio.wait_for(self.message_queue.get(), timeout=1.0)
                await self._process_message(message)
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                self.log(f"Message handling error: {e}", "ERROR")
    
    async def _process_message(self, message: Dict[str, Any]):
        """Process inter-agent message"""
        msg_type = message.get("type")
        from_agent = message.get("from_agent")
        
        self.log(f"Message from {from_agent}: {msg_type}")
        
        if msg_type == "task_completed":
            await self._handle_task_completion(message)
        elif msg_type == "agent_result":
            await self._forward_to_synthesis(message)
        elif msg_type == "request_help":
            await self._handle_help_request(message)
    
    async def _handle_task_completion(self, message: Dict[str, Any]):
        """Handle task completion message"""
        agent_id = message.get("from_agent")
        task_id = message.get("task_id")
        result = message.get("result", {})
        
        # Update work package
        if task_id in self.work_packages:
            wp = self.work_packages[task_id]
            wp.status = "completed"
            wp.result = result
            wp.completed_at = datetime.now()
        
        # Update agent
        if agent_id in self.agents:
            agent_info = self.agents[agent_id]
            agent_info.status = "idle"
            agent_info.current_task = None
            agent_info.tasks_completed += 1
            
            # Update model stats
            model_used = result.get("model_used")
            if model_used:
                agent_info.model_stats[model_used] = agent_info.model_stats.get(model_used, 0) + 1
        
        self.log(f"Task {task_id} completed by {agent_id}")
    
    async def _check_synthesis_trigger(self):
        """Check if synthesis should be triggered"""
        if self.synthesis_agent:
            return  # Already running
        
        # Count completed work packages
        completed = [wp for wp in self.work_packages.values() if wp.status == "completed"]
        
        if len(completed) >= self.synthesis_threshold:
            # Check if we have results from multiple agents
            unique_agents = set(wp.assigned_agent for wp in completed)
            
            if len(unique_agents) >= 2:
                self.log(f"Triggering synthesis: {len(completed)} packages from {len(unique_agents)} agents")
                await self._start_synthesis()
    
    async def _start_synthesis(self):
        """Start synthesis agent"""
        if self.synthesis_agent:
            return
        
        self.state = OrchestratorState.SYNTHESIZING
        
        # Spawn synthesis agent
        self.synthesis_agent = await self._spawn_agent("synthesis", "synthesis")
        
        # Send completed results to synthesis
        completed = [wp for wp in self.work_packages.values() if wp.status == "completed"]
        
        for wp in completed:
            message = {
                "type": "agent_result",
                "from_agent": wp.assigned_agent,
                "payload": {
                    "work_package_id": wp.id,
                    "description": wp.description,
                    "result": wp.result
                }
            }
            
            await self.synthesis_agent.agent_instance.handle_message(message)
        
        # Create synthesis task
        synthesis_task = {
            "id": "final_synthesis",
            "type": "synthesize",
            "description": "Synthesize all agent results",
            "agent_ids": list(set(wp.assigned_agent for wp in completed))
        }
        
        self.synthesis_agent.agent_instance.add_task(synthesis_task)
    
    async def _forward_to_synthesis(self, message: Dict[str, Any]):
        """Forward message to synthesis agent"""
        if self.synthesis_agent:
            await self.synthesis_agent.agent_instance.handle_message(message)
    
    async def _handle_help_request(self, message: Dict[str, Any]):
        """Handle agent help request"""
        # Could spawn additional agent or reassign work
        self.log(f"Help requested by {message.get('from_agent')}: {message.get('reason')}")
    
    async def _final_synthesis(self):
        """Perform final synthesis if needed"""
        if not self.synthesis_agent:
            # Check if synthesis is needed
            completed = [wp for wp in self.work_packages.values() if wp.status == "completed"]
            if len(completed) > 1:
                await self._start_synthesis()
        
        # Wait for synthesis to complete
        if self.synthesis_agent:
            while self.synthesis_agent.status == "working":
                await asyncio.sleep(1)
    
    def _has_pending_work(self) -> bool:
        """Check if there's pending work"""
        # Check for pending work packages
        has_pending = any(wp.status in ["pending", "in_progress"] 
                         for wp in self.work_packages.values())
        
        # Check if agents are still working
        agents_working = any(agent.status == "working" 
                           for agent in self.agents.values())
        
        return has_pending or agents_working
    
    async def _stop_agent(self, agent_info: AgentInfo):
        """Stop an agent"""
        self.log(f"Stopping agent {agent_info.agent_id}")
        
        # Signal agent to stop
        agent_info.agent_instance.active = False
        
        # Wait briefly for cleanup
        await asyncio.sleep(1)
        
        # Remove worktree if exists
        if agent_info.worktree_path:
            await self._remove_worktree(agent_info)
    
    async def _remove_worktree(self, agent_info: AgentInfo):
        """Remove agent's git worktree"""
        if not agent_info.worktree_path:
            return
        
        try:
            cmd = f"git worktree remove {agent_info.worktree_path}"
            subprocess.run(
                cmd,
                shell=True,
                cwd=self.project_root,
                capture_output=True
            )
            
            self.log(f"Removed worktree for {agent_info.agent_id}")
        except Exception as e:
            self.log(f"Worktree removal error: {e}", "ERROR")
    
    async def _generate_final_report(self):
        """Generate final orchestration report"""
        report = {
            "orchestrator_id": self.orchestrator_id,
            "state": self.state.value,
            "statistics": {
                "total_agents": len(self.agents),
                "work_packages": len(self.work_packages),
                "completed": len([wp for wp in self.work_packages.values() if wp.status == "completed"]),
                "failed": len([wp for wp in self.work_packages.values() if wp.status == "error"])
            },
            "agent_performance": {},
            "model_usage": self._aggregate_model_usage(),
            "timing": self._calculate_timing_stats()
        }
        
        # Agent performance
        for agent_id, agent_info in self.agents.items():
            report["agent_performance"][agent_id] = {
                "type": agent_info.agent_type,
                "tasks_completed": agent_info.tasks_completed,
                "model_stats": agent_info.model_stats
            }
        
        # Save report
        report_path = self.log_file.parent / f"orchestration_report_{self.orchestrator_id}.json"
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2, default=str)
        
        self.log(f"Final report saved to {report_path}")
    
    def _aggregate_model_usage(self) -> Dict[str, Any]:
        """Aggregate model usage across all agents"""
        total_usage = {}
        
        for agent_info in self.agents.values():
            for model, count in agent_info.model_stats.items():
                total_usage[model] = total_usage.get(model, 0) + count
        
        # Calculate cost savings
        claude_tasks = total_usage.get("claude-opus-4", 0)
        kimi_tasks = total_usage.get("kimi-pro", 0)
        gemini_tasks = total_usage.get("gemini-mcp", 0)
        
        total_tasks = sum(total_usage.values())
        
        if total_tasks > 0:
            # Estimate cost savings
            kimi_savings = kimi_tasks * 0.6  # 60% cost reduction
            gemini_savings = gemini_tasks * 0.75  # 75% cost reduction
            
            total_cost_reduction = (kimi_savings + gemini_savings) / total_tasks
            
            return {
                "by_model": total_usage,
                "total_tasks": total_tasks,
                "cost_reduction": f"{total_cost_reduction:.1%}"
            }
        
        return {"by_model": {}, "total_tasks": 0, "cost_reduction": "0%"}
    
    def _calculate_timing_stats(self) -> Dict[str, Any]:
        """Calculate timing statistics"""
        completed_wps = [wp for wp in self.work_packages.values() if wp.completed_at]
        
        if not completed_wps:
            return {}
        
        # Calculate average completion time
        completion_times = [
            (wp.completed_at - wp.created_at).total_seconds()
            for wp in completed_wps
        ]
        
        return {
            "average_completion_seconds": sum(completion_times) / len(completion_times),
            "min_completion_seconds": min(completion_times),
            "max_completion_seconds": max(completion_times)
        }
    
    def get_status(self) -> Dict[str, Any]:
        """Get current orchestrator status"""
        return {
            "orchestrator_id": self.orchestrator_id,
            "state": self.state.value,
            "agents": {
                agent_id: {
                    "type": info.agent_type,
                    "status": info.status,
                    "current_task": info.current_task,
                    "tasks_completed": info.tasks_completed
                }
                for agent_id, info in self.agents.items()
            },
            "work_packages": {
                wp_id: {
                    "description": wp.description[:50] + "...",
                    "status": wp.status,
                    "assigned_to": wp.assigned_agent,
                    "complexity": wp.complexity.name
                }
                for wp_id, wp in self.work_packages.items()
            },
            "model_usage": self._aggregate_model_usage()
        }