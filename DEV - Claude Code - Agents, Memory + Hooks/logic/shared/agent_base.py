#!/usr/bin/env python3
"""
Base Agent Class for Multi-Agent System

Provides the foundation for all Claude agents with built-in lifecycle management,
messaging, and coordination capabilities.
"""

import os
import sys
import json
import time
import uuid
import asyncio
import threading
from typing import Dict, Any, List, Optional, Callable
from abc import ABC, abstractmethod
from datetime import datetime

from .agent_registry import AgentLifecycle
from .message_queue import MessageQueue, Message
from .resource_monitor import ResourceMonitor
from .distributed_lock_manager import DistributedLockManager


class AgentBase(ABC):
    """Base class for all Claude agents"""
    
    def __init__(self, 
                 agent_id: str = None,
                 agent_type: str = "development",
                 work_package: str = None,
                 metadata: Dict[str, Any] = None):
        # Agent identification
        self.agent_id = agent_id or self._generate_agent_id()
        self.agent_type = agent_type
        self.work_package = work_package
        self.metadata = metadata or {}
        
        # Agent components
        self.lifecycle = AgentLifecycle(self.agent_id, {
            "agent_type": agent_type,
            "work_package": work_package,
            **self.metadata
        })
        self.message_queue = MessageQueue(self.agent_id)
        self.resource_monitor = ResourceMonitor(self.agent_id)
        self.lock_manager = DistributedLockManager(self.agent_id)
        
        # Agent state
        self.active = False
        self.tasks = []
        self.dependencies = []
        self.completed_tasks = []
        self.start_time = None
        self.log_file = None
        
        # Callbacks
        self.message_handlers = {}
        self.task_handlers = {}
    
    def _generate_agent_id(self) -> str:
        """Generate unique agent ID"""
        return f"claude-{self.agent_type}-{os.getpid()}-{uuid.uuid4().hex[:8]}"
    
    async def start(self):
        """Start the agent"""
        print(f"[{self.agent_id}] Starting agent...")
        
        # Initialize lifecycle
        if not self.lifecycle.startup():
            raise RuntimeError("Failed to start agent lifecycle")
        
        # Start monitoring
        self.resource_monitor.start_monitoring()
        
        # Start message queue
        self.message_queue.start()
        self._register_default_handlers()
        
        # Set up logging
        self._setup_logging()
        
        # Mark as active
        self.active = True
        self.start_time = time.time()
        
        # Send discovery message
        self.message_queue.broadcast_discovery([
            self.agent_type,
            self.work_package or "general"
        ])
        
        # Run agent-specific initialization
        await self.initialize()
        
        # Start main loop
        await self.run()
    
    async def stop(self, reason: str = "normal"):
        """Stop the agent"""
        print(f"[{self.agent_id}] Stopping agent ({reason})...")
        
        self.active = False
        
        # Run agent-specific cleanup
        await self.cleanup()
        
        # Stop components
        self.message_queue.stop()
        self.resource_monitor.stop_monitoring()
        
        # Release all locks
        self.lock_manager.cleanup_all_locks()
        
        # Shutdown lifecycle
        self.lifecycle.shutdown(reason)
        
        print(f"[{self.agent_id}] Agent stopped")
    
    @abstractmethod
    async def initialize(self):
        """Initialize agent-specific resources"""
        pass
    
    @abstractmethod
    async def run(self):
        """Main agent execution loop"""
        pass
    
    @abstractmethod
    async def cleanup(self):
        """Clean up agent-specific resources"""
        pass
    
    async def execute_task(self, task: Dict[str, Any]):
        """Execute a task"""
        task_id = task.get("id", "unknown")
        self.log(f"Executing task: {task_id}")
        
        try:
            # Check resource limits
            if not self.resource_monitor.check_limits():
                self.log("Resource limits exceeded, throttling...")
                await asyncio.sleep(5)
            
            # Check dependencies
            await self.wait_for_dependencies(task)
            
            # Execute task handler
            if task["type"] in self.task_handlers:
                result = await self.task_handlers[task["type"]](task)
            else:
                result = await self.default_task_handler(task)
            
            # Mark complete
            self.completed_tasks.append(task_id)
            
            # Notify completion
            self.message_queue.send_task_complete(task_id, result)
            
            return result
            
        except Exception as e:
            self.log(f"Task {task_id} failed: {e}")
            raise
    
    async def default_task_handler(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Default task handler - override in subclasses"""
        self.log(f"No handler for task type: {task['type']}")
        return {"status": "unsupported"}
    
    async def wait_for_dependencies(self, task: Dict[str, Any]):
        """Wait for task dependencies to complete"""
        dependencies = task.get("dependencies", [])
        
        for dep in dependencies:
            self.log(f"Waiting for dependency: {dep}")
            
            # Check if dependency is already complete
            if dep in self.completed_tasks:
                continue
            
            # Wait for dependency completion message
            timeout = 300  # 5 minutes
            start_time = time.time()
            
            while dep not in self.completed_tasks:
                if time.time() - start_time > timeout:
                    raise TimeoutError(f"Dependency {dep} timed out")
                
                await asyncio.sleep(1)
    
    def register_message_handler(self, message_type: str, handler: Callable):
        """Register a message handler"""
        self.message_handlers[message_type] = handler
        self.message_queue.subscribe(message_type, self._message_wrapper(handler))
    
    def register_task_handler(self, task_type: str, handler: Callable):
        """Register a task handler"""
        self.task_handlers[task_type] = handler
    
    def _message_wrapper(self, handler: Callable) -> Callable:
        """Wrap message handler for async execution"""
        def wrapper(message: Message):
            # Run async handler in event loop
            loop = asyncio.get_event_loop()
            loop.create_task(handler(message))
        return wrapper
    
    def _register_default_handlers(self):
        """Register default message handlers"""
        # Status request
        self.register_message_handler("status_request", self._handle_status_request)
        
        # Task assignment
        self.register_message_handler("task_assignment", self._handle_task_assignment)
        
        # Dependency notification
        self.register_message_handler("task_complete", self._handle_task_complete)
    
    async def _handle_status_request(self, message: Message):
        """Handle status request"""
        status = {
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "work_package": self.work_package,
            "active": self.active,
            "uptime": int(time.time() - self.start_time) if self.start_time else 0,
            "completed_tasks": len(self.completed_tasks),
            "resource_usage": self.resource_monitor.get_usage_stats()
        }
        
        # Send status response
        response = Message(
            from_agent=self.agent_id,
            to_agent=message.from_agent,
            message_type="status_response",
            payload=status
        )
        self.message_queue.publish(response)
    
    async def _handle_task_assignment(self, message: Message):
        """Handle task assignment"""
        task = message.payload
        self.log(f"Received task assignment: {task.get('id')}")
        
        # Add to task queue
        self.tasks.append(task)
    
    async def _handle_task_complete(self, message: Message):
        """Handle task completion notification"""
        task_id = message.payload.get("task_id")
        if task_id and task_id not in self.completed_tasks:
            # Track external task completion for dependencies
            self.completed_tasks.append(task_id)
    
    def _setup_logging(self):
        """Set up agent-specific logging"""
        log_dir = os.path.join(self.lifecycle.workspace, "logs")
        os.makedirs(log_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(log_dir, f"{timestamp}.log")
        
        self.log(f"Agent {self.agent_id} started")
        self.log(f"Type: {self.agent_type}")
        self.log(f"Work package: {self.work_package}")
    
    def log(self, message: str, level: str = "INFO"):
        """Log a message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"
        
        # Print to console
        print(f"[{self.agent_id}] {message}")
        
        # Write to log file
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
    
    async def request_resource(self, resource_name: str, exclusive: bool = False) -> bool:
        """Request access to a resource"""
        self.log(f"Requesting resource: {resource_name} (exclusive: {exclusive})")
        
        # Try to acquire lock
        lock = self.lock_manager.acquire_lock(resource_name, timeout=10)
        if lock:
            self.log(f"Acquired resource: {resource_name}")
            return True
        else:
            self.log(f"Failed to acquire resource: {resource_name}")
            return False
    
    def release_resource(self, resource_name: str):
        """Release a resource"""
        self.lock_manager.release_lock(resource_name)
        self.log(f"Released resource: {resource_name}")
    
    def report_progress(self, progress: float, status: str = None):
        """Report task progress"""
        self.message_queue.send_status_update(
            status=status or f"Progress: {progress:.1f}%",
            details={
                "progress": progress,
                "completed_tasks": len(self.completed_tasks),
                "total_tasks": len(self.tasks)
            }
        )


class DevelopmentAgent(AgentBase):
    """Agent specialized for development tasks"""
    
    def __init__(self, work_package: str, **kwargs):
        super().__init__(
            agent_type="development",
            work_package=work_package,
            **kwargs
        )
    
    async def initialize(self):
        """Initialize development environment"""
        self.log("Initializing development environment...")
        
        # Set up workspace
        self.workspace_dir = os.path.join(self.lifecycle.workspace, "workspace")
        os.makedirs(self.workspace_dir, exist_ok=True)
        
        # Register task handlers
        self.register_task_handler("implement", self.implement_feature)
        self.register_task_handler("refactor", self.refactor_code)
        self.register_task_handler("test", self.run_tests)
    
    async def run(self):
        """Main development loop"""
        while self.active:
            # Process tasks
            if self.tasks:
                task = self.tasks.pop(0)
                await self.execute_task(task)
            else:
                # Wait for new tasks
                await asyncio.sleep(1)
    
    async def cleanup(self):
        """Clean up development resources"""
        self.log("Cleaning up development environment...")
    
    async def implement_feature(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Implement a new feature"""
        self.log(f"Implementing feature: {task.get('feature')}")
        
        # Simulate implementation
        await asyncio.sleep(2)
        
        return {
            "status": "completed",
            "files_created": ["feature.py"],
            "tests_added": ["test_feature.py"]
        }
    
    async def refactor_code(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Refactor existing code"""
        self.log(f"Refactoring: {task.get('target')}")
        
        # Simulate refactoring
        await asyncio.sleep(1)
        
        return {
            "status": "completed",
            "files_modified": ["module.py"]
        }
    
    async def run_tests(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Run tests"""
        self.log("Running tests...")
        
        # Simulate test execution
        await asyncio.sleep(1)
        
        return {
            "status": "completed",
            "tests_passed": 10,
            "tests_failed": 0
        }


if __name__ == "__main__":
    # Example usage
    async def main():
        print("Testing Agent Base...")
        
        # Create test agent
        agent = DevelopmentAgent(
            work_package="test-wp",
            metadata={"test": True}
        )
        
        # Run for a few seconds
        try:
            # Start agent in background
            agent_task = asyncio.create_task(agent.start())
            
            # Wait a bit
            await asyncio.sleep(5)
            
            # Stop agent
            await agent.stop("test complete")
            
        except Exception as e:
            print(f"Error: {e}")
    
    # Run test
    asyncio.run(main())