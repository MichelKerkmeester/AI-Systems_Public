#!/usr/bin/env python3
"""
Parallel Agent Orchestration Hook

Manages parallel execution of multiple Claude agents for concurrent development
of work packages.
"""

import os
import sys
import json
import time
import uuid
import subprocess
import asyncio
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import base hook functionality
from pathlib import Path
from contextlib import contextmanager

# Simple implementations for now
class HookBase:
    pass

class ToolHook(HookBase):
    def _create_response(self, message: str, style: str = "info") -> dict:
        return {
            "type": "hook_response",
            "message": message,
            "style": style
        }

class MessageFormatter:
    pass

# Placeholder classes for agent coordination
class AgentRegistry:
    def get_agent(self, agent_id: str):
        return None

class MessageQueue:
    def __init__(self, queue_id: str):
        self.queue_id = queue_id
    
    def publish(self, message: Any):
        pass

@dataclass
class Message:
    from_agent: str
    to_agent: str
    message_type: str
    payload: dict

class GlobalResourceManager:
    def can_start_agent(self) -> bool:
        # Simple check - allow up to 3 parallel agents
        return True

class DistributedLockManager:
    def __init__(self, lock_id: str):
        self.lock_id = lock_id
    
    @contextmanager
    def atomic_file_operation(self, operation: str):
        yield


@dataclass
class WorkPackageInfo:
    """Information about a work package"""
    id: str
    name: str
    description: str
    dependencies: List[str]
    estimated_hours: float
    agent_type: str = "development"
    priority: int = 5


@dataclass
class AgentProcess:
    """Information about an agent process"""
    agent_id: str
    work_package: str
    process_id: Optional[int]
    session_id: Optional[str]  # Process session ID
    worktree_path: Optional[str]
    branch_name: str
    status: str = "initializing"
    started_at: float = 0
    progress: float = 0


class ParallelAgentOrchestrator:
    """Orchestrates parallel agent execution"""
    
    def __init__(self):
        self.orchestrator_id = f"orchestrator-{os.getpid()}"
        self.registry = AgentRegistry()
        self.message_queue = MessageQueue(self.orchestrator_id)
        self.resource_manager = GlobalResourceManager()
        self.lock_manager = DistributedLockManager(self.orchestrator_id)
        
        # Agent tracking
        self.agents: Dict[str, AgentProcess] = {}
        self.work_packages: Dict[str, WorkPackageInfo] = {}
        self.completed_packages: List[str] = []
        
        # Paths
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.agents_dir = os.path.join(self.base_dir, "agents")
    
    async def spawn_agent(self, work_package: WorkPackageInfo) -> AgentProcess:
        """Spawn a new agent for a work package"""
        
        # Check resource availability
        if not self.resource_manager.can_start_agent():
            raise RuntimeError("Cannot start new agent - resource limits exceeded")
        
        # Create agent process info
        agent_id = f"claude-{work_package.id}-{uuid.uuid4().hex[:8]}"
        branch_name = f"wp-{work_package.id}"
        worktree_path = os.path.join(self.agents_dir, "worktrees", work_package.id)
        
        agent = AgentProcess(
            agent_id=agent_id,
            work_package=work_package.id,
            branch_name=branch_name,
            worktree_path=worktree_path,
            started_at=time.time()
        )
        
        try:
            # Create git worktree
            await self._create_worktree(work_package.id, branch_name, worktree_path)
            
            # Create agent script
            agent_script_path = await self._create_agent_script(agent, work_package)
            
            # Start agent process
            process = await self._start_agent_subprocess(agent_script_path, agent_id)
            agent.process_id = process.pid
            
            # Update status
            agent.status = "running"
            self.agents[work_package.id] = agent
            
            # Send initialization message
            init_msg = Message(
                from_agent=self.orchestrator_id,
                to_agent=agent_id,
                message_type="task_assignment",
                payload={
                    "id": f"implement-{work_package.id}",
                    "type": "implement",
                    "work_package": work_package.id,
                    "description": work_package.description,
                    "dependencies": work_package.dependencies
                }
            )
            self.message_queue.publish(init_msg)
            
            return agent
            
        except Exception as e:
            agent.status = "failed"
            raise RuntimeError(f"Failed to spawn agent: {e}")
    
    async def _create_worktree(self, wp_id: str, branch_name: str, worktree_path: str):
        """Create git worktree for agent"""
        # Ensure worktrees directory exists
        os.makedirs(os.path.dirname(worktree_path), exist_ok=True)
        
        # Create branch and worktree
        with self.lock_manager.atomic_file_operation("git"):
            # Check if branch exists
            result = subprocess.run(
                ["git", "branch", "--list", branch_name],
                capture_output=True,
                text=True
            )
            
            if not result.stdout.strip():
                # Create branch
                subprocess.run(
                    ["git", "branch", branch_name],
                    check=True
                )
            
            # Create worktree if it doesn't exist
            if not os.path.exists(worktree_path):
                subprocess.run(
                    ["git", "worktree", "add", worktree_path, branch_name],
                    check=True
                )
    
    async def _create_agent_script(self, 
                                   agent: AgentProcess, 
                                   work_package: WorkPackageInfo) -> str:
        """Create agent execution script"""
        script_dir = os.path.join(self.agents_dir, "scripts")
        os.makedirs(script_dir, exist_ok=True)
        
        script_path = os.path.join(script_dir, f"{agent.agent_id}.py")
        
        script_content = f'''#!/usr/bin/env python3
"""
Auto-generated agent script for {work_package.id}
"""

import os
import sys
import asyncio

# Add path for imports
sys.path.insert(0, "{self.base_dir}")

from hooks.shared.agent_base import DevelopmentAgent

async def main():
    agent = DevelopmentAgent(
        agent_id="{agent.agent_id}",
        work_package="{work_package.id}",
        metadata={{
            "description": "{work_package.description}",
            "estimated_hours": {work_package.estimated_hours},
            "priority": {work_package.priority}
        }}
    )
    
    # Change to worktree directory
    os.chdir("{agent.worktree_path}")
    
    # Start agent
    await agent.start()

if __name__ == "__main__":
    asyncio.run(main())
'''
        
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # Make executable
        os.chmod(script_path, 0o755)
        
        return script_path
    
    
    async def _start_agent_subprocess(self, script_path: str, agent_id: str) -> subprocess.Popen:
        """Start agent as subprocess (fallback)"""
        env = os.environ.copy()
        env["CLAUDE_AGENT_ID"] = agent_id
        
        process = subprocess.Popen(
            [sys.executable, script_path],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(script_path)
        )
        
        return process
    
    async def monitor_agents(self):
        """Monitor agent progress and health"""
        while True:
            for wp_id, agent in self.agents.items():
                if agent.status == "running":
                    # Check agent health
                    agent_info = self.registry.get_agent(agent.agent_id)
                    
                    if not agent_info:
                        # Agent not found in registry
                        agent.status = "lost"
                        continue
                    
                    # Update progress from agent info
                    if "progress" in agent_info.metadata:
                        agent.progress = agent_info.metadata["progress"]
                    
                    # Check if complete
                    if agent.progress >= 100:
                        agent.status = "completed"
                        self.completed_packages.append(wp_id)
            
            await asyncio.sleep(5)
    
    async def coordinate_merge(self, work_packages: List[str]):
        """Coordinate merging of completed work packages"""
        for wp_id in work_packages:
            agent = self.agents.get(wp_id)
            if not agent or agent.status != "completed":
                continue
            
            try:
                # Check for conflicts
                has_conflicts = await self._check_conflicts(agent.worktree_path)
                
                if has_conflicts:
                    # Create integration agent to resolve
                    integration_wp = WorkPackageInfo(
                        id=f"{wp_id}-integration",
                        name=f"Integration for {wp_id}",
                        description=f"Resolve conflicts and merge {wp_id}",
                        dependencies=[wp_id],
                        estimated_hours=1,
                        agent_type="integration"
                    )
                    await self.spawn_agent(integration_wp)
                else:
                    # Direct merge
                    await self._merge_worktree(agent)
                    
            except Exception as e:
                print(f"Merge failed for {wp_id}: {e}")
    
    async def _check_conflicts(self, worktree_path: str) -> bool:
        """Check if worktree has conflicts with main branch"""
        result = subprocess.run(
            ["git", "merge", "--no-commit", "--no-ff", "main"],
            cwd=worktree_path,
            capture_output=True
        )
        
        # Reset merge
        subprocess.run(["git", "merge", "--abort"], cwd=worktree_path)
        
        return result.returncode != 0
    
    async def _merge_worktree(self, agent: AgentProcess):
        """Merge agent's work back to main"""
        with self.lock_manager.atomic_file_operation("git"):
            # Switch to main
            subprocess.run(["git", "checkout", "main"], check=True)
            
            # Merge branch
            subprocess.run(
                ["git", "merge", "--no-ff", agent.branch_name,
                 "-m", f"Merge {agent.work_package} implementation"],
                check=True
            )
    
    def get_status(self) -> Dict[str, Any]:
        """Get orchestrator status"""
        return {
            "orchestrator_id": self.orchestrator_id,
            "active_agents": len([a for a in self.agents.values() if a.status == "running"]),
            "completed_packages": len(self.completed_packages),
            "agents": {
                wp_id: {
                    "agent_id": agent.agent_id,
                    "status": agent.status,
                    "progress": agent.progress,
                    "uptime": int(time.time() - agent.started_at) if agent.started_at else 0
                }
                for wp_id, agent in self.agents.items()
            }
        }


class ParallelAgentHook(ToolHook):
    """Hook for parallel agent orchestration"""
    
    def __init__(self):
        super().__init__()
        self.orchestrator = None
        self.formatter = MessageFormatter()
    
    def can_handle(self, request_data: dict) -> bool:
        """Check if this is a parallel task request"""
        # Look for multiple work packages or parallel execution request
        tool_name = request_data.get("name", "")
        
        if tool_name == "logic" and "parallel" in str(request_data.get("arguments", {})):
            return True
        
        # Check for TodoWrite with multiple high-priority tasks
        if tool_name == "TodoWrite":
            todos = request_data.get("arguments", {}).get("todos", [])
            high_priority_count = sum(1 for t in todos if t.get("priority") == "high")
            return high_priority_count >= 3
        
        return False
    
    def process(self, request_data: dict, project_context: dict) -> dict:
        """Process parallel execution request"""
        # Extract work packages
        work_packages = self._extract_work_packages(request_data)
        
        if not work_packages:
            return self._create_response(
                "No work packages identified for parallel execution",
                style="info"
            )
        
        # Check if orchestrator should be started
        if len(work_packages) < 2:
            return self._create_response(
                f"Only {len(work_packages)} work package(s) - parallel execution not beneficial",
                style="info"
            )
        
        # Create response with parallel execution suggestion
        message = self._create_parallel_suggestion(work_packages)
        
        return self._create_response(message, style="warning")
    
    def _extract_work_packages(self, request_data: dict) -> List[WorkPackageInfo]:
        """Extract work packages from request"""
        work_packages = []
        
        # Extract from TodoWrite
        if request_data.get("name") == "TodoWrite":
            todos = request_data.get("arguments", {}).get("todos", [])
            for todo in todos:
                if todo.get("priority") == "high" and todo.get("status") == "pending":
                    wp = WorkPackageInfo(
                        id=todo.get("id", "unknown"),
                        name=todo.get("content", ""),
                        description=todo.get("content", ""),
                        dependencies=[],
                        estimated_hours=2.0  # Default estimate
                    )
                    work_packages.append(wp)
        
        return work_packages
    
    def _create_parallel_suggestion(self, work_packages: List[WorkPackageInfo]) -> str:
        """Create suggestion message for parallel execution"""
        lines = [
            "🚀 **Parallel Execution Opportunity Detected**",
            "",
            f"Found {len(work_packages)} work packages that could be executed in parallel:",
            ""
        ]
        
        for wp in work_packages:
            lines.append(f"  • {wp.name}")
        
        lines.extend([
            "",
            "To execute these in parallel, use:",
            "```",
            "/logic tasks parallel start " + ",".join(wp.id for wp in work_packages),
            "```",
            "",
            "This will:",
            "  • Spawn dedicated agents for each work package",
            "  • Create isolated git worktrees",
            "  • Execute tasks concurrently",
            "  • Automatically merge results",
            "",
            f"Estimated time savings: ~{self._estimate_time_savings(work_packages)}%"
        ])
        
        return "\n".join(lines)
    
    def _estimate_time_savings(self, work_packages: List[WorkPackageInfo]) -> int:
        """Estimate time savings from parallel execution"""
        total_serial = sum(wp.estimated_hours for wp in work_packages)
        total_parallel = max(wp.estimated_hours for wp in work_packages) * 1.2  # 20% overhead
        
        savings = (1 - total_parallel / total_serial) * 100
        return max(0, int(savings))


def main():
    """Main entry point"""
    hook = ParallelAgentHook()
    
    # Read request from stdin
    request_json = sys.stdin.read()
    
    try:
        request_data = json.loads(request_json)
        
        # Process if applicable
        if hook.can_handle(request_data):
            response = hook.process(request_data, {})
            
            # Output response
            print(json.dumps(response))
        
    except Exception as e:
        # Silent failure for hooks
        pass


if __name__ == "__main__":
    main()