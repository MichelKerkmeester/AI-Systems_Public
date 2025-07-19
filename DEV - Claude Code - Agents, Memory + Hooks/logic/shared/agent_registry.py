#!/usr/bin/env python3
"""
Agent Registry for Multi-Agent System

Maintains a registry of all active Claude agents, handles registration,
heartbeats, and lifecycle management.
"""

import os
import json
import time
import uuid
import threading
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

from .distributed_lock_manager import DistributedLockManager


class AgentInfo:
    """Information about a registered agent"""
    
    def __init__(self, agent_id: str, metadata: Dict[str, Any] = None):
        self.agent_id = agent_id
        self.pid = os.getpid()
        self.started = time.time()
        self.last_heartbeat = time.time()
        self.status = "active"
        self.metadata = metadata or {}
        self.work_package = metadata.get("work_package") if metadata else None
        self.agent_type = metadata.get("agent_type", "development") if metadata else "development"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "agent_id": self.agent_id,
            "pid": self.pid,
            "started": self.started,
            "last_heartbeat": self.last_heartbeat,
            "status": self.status,
            "metadata": self.metadata,
            "work_package": self.work_package,
            "agent_type": self.agent_type,
            "uptime_seconds": int(time.time() - self.started)
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AgentInfo':
        """Create from dictionary"""
        agent = cls(data["agent_id"], data.get("metadata"))
        agent.pid = data["pid"]
        agent.started = data["started"]
        agent.last_heartbeat = data["last_heartbeat"]
        agent.status = data["status"]
        agent.work_package = data.get("work_package")
        agent.agent_type = data.get("agent_type", "development")
        return agent


class AgentRegistry:
    """Central registry for all active agents"""
    
    def __init__(self, registry_dir: str = None):
        self.registry_dir = registry_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "registry"
        )
        self.registry_file = os.path.join(self.registry_dir, "active-agents.json")
        self.history_file = os.path.join(self.registry_dir, "agent-history.json")
        self.heartbeat_timeout = 60  # seconds
        self.cleanup_interval = 30  # seconds
        self.lock_manager = DistributedLockManager("registry-manager")
        
        # Ensure registry directory exists
        os.makedirs(self.registry_dir, exist_ok=True)
        
        # Start cleanup daemon
        self._start_cleanup_daemon()
    
    def register_agent(self, agent_id: str, metadata: Dict[str, Any] = None) -> bool:
        """
        Register a new agent
        
        Args:
            agent_id: Unique identifier for the agent
            metadata: Additional metadata about the agent
            
        Returns:
            True if registration successful
        """
        agent_info = AgentInfo(agent_id, metadata)
        
        with self.lock_manager.atomic_file_operation(self.registry_file):
            registry = self._load_registry()
            registry[agent_id] = agent_info.to_dict()
            self._save_registry(registry)
            
            # Add to history
            self._add_to_history({
                "event": "registered",
                "agent_id": agent_id,
                "timestamp": time.time(),
                "metadata": metadata
            })
        
        return True
    
    def deregister_agent(self, agent_id: str, reason: str = "shutdown"):
        """Deregister an agent"""
        with self.lock_manager.atomic_file_operation(self.registry_file):
            registry = self._load_registry()
            
            if agent_id in registry:
                agent_info = registry[agent_id]
                del registry[agent_id]
                self._save_registry(registry)
                
                # Add to history
                self._add_to_history({
                    "event": "deregistered",
                    "agent_id": agent_id,
                    "timestamp": time.time(),
                    "reason": reason,
                    "uptime_seconds": int(time.time() - agent_info["started"])
                })
    
    def heartbeat(self, agent_id: str) -> bool:
        """
        Update agent heartbeat
        
        Returns:
            True if heartbeat recorded successfully
        """
        with self.lock_manager.atomic_file_operation(self.registry_file):
            registry = self._load_registry()
            
            if agent_id in registry:
                registry[agent_id]["last_heartbeat"] = time.time()
                registry[agent_id]["status"] = "active"
                self._save_registry(registry)
                return True
            
            return False
    
    def get_agent(self, agent_id: str) -> Optional[AgentInfo]:
        """Get information about a specific agent"""
        registry = self._load_registry()
        if agent_id in registry:
            return AgentInfo.from_dict(registry[agent_id])
        return None
    
    def list_active_agents(self) -> List[AgentInfo]:
        """List all active agents"""
        registry = self._load_registry()
        agents = []
        
        current_time = time.time()
        for agent_data in registry.values():
            agent = AgentInfo.from_dict(agent_data)
            
            # Check if agent is still active
            if current_time - agent.last_heartbeat <= self.heartbeat_timeout:
                agents.append(agent)
        
        return agents
    
    def get_agents_by_type(self, agent_type: str) -> List[AgentInfo]:
        """Get all agents of a specific type"""
        return [
            agent for agent in self.list_active_agents()
            if agent.agent_type == agent_type
        ]
    
    def get_agents_by_work_package(self, work_package: str) -> List[AgentInfo]:
        """Get all agents working on a specific work package"""
        return [
            agent for agent in self.list_active_agents()
            if agent.work_package == work_package
        ]
    
    def cleanup_stale_agents(self):
        """Remove stale agents from registry"""
        with self.lock_manager.atomic_file_operation(self.registry_file):
            registry = self._load_registry()
            current_time = time.time()
            stale_agents = []
            
            for agent_id, agent_data in list(registry.items()):
                if current_time - agent_data["last_heartbeat"] > self.heartbeat_timeout:
                    stale_agents.append(agent_id)
                    del registry[agent_id]
                    
                    # Add to history
                    self._add_to_history({
                        "event": "timeout",
                        "agent_id": agent_id,
                        "timestamp": current_time,
                        "last_heartbeat": agent_data["last_heartbeat"],
                        "uptime_seconds": int(current_time - agent_data["started"])
                    })
            
            if stale_agents:
                self._save_registry(registry)
        
        return stale_agents
    
    def get_registry_stats(self) -> Dict[str, Any]:
        """Get statistics about the agent registry"""
        agents = self.list_active_agents()
        
        stats = {
            "total_active": len(agents),
            "by_type": {},
            "by_work_package": {},
            "oldest_agent": None,
            "newest_agent": None,
            "average_uptime": 0
        }
        
        if agents:
            # Count by type
            for agent in agents:
                agent_type = agent.agent_type
                stats["by_type"][agent_type] = stats["by_type"].get(agent_type, 0) + 1
            
            # Count by work package
            for agent in agents:
                if agent.work_package:
                    wp = agent.work_package
                    stats["by_work_package"][wp] = stats["by_work_package"].get(wp, 0) + 1
            
            # Find oldest and newest
            sorted_agents = sorted(agents, key=lambda a: a.started)
            stats["oldest_agent"] = sorted_agents[0].agent_id
            stats["newest_agent"] = sorted_agents[-1].agent_id
            
            # Calculate average uptime
            current_time = time.time()
            total_uptime = sum(current_time - agent.started for agent in agents)
            stats["average_uptime"] = int(total_uptime / len(agents))
        
        return stats
    
    def _load_registry(self) -> Dict[str, Dict[str, Any]]:
        """Load registry from disk"""
        if os.path.exists(self.registry_file):
            try:
                with open(self.registry_file, 'r') as f:
                    return json.load(f)
            except (IOError, json.JSONDecodeError):
                pass
        return {}
    
    def _save_registry(self, registry: Dict[str, Dict[str, Any]]):
        """Save registry to disk"""
        with open(self.registry_file, 'w') as f:
            json.dump(registry, f, indent=2)
    
    def _add_to_history(self, event: Dict[str, Any]):
        """Add event to agent history"""
        history = []
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
            except (IOError, json.JSONDecodeError):
                pass
        
        history.append(event)
        
        # Keep only last 1000 events
        if len(history) > 1000:
            history = history[-1000:]
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def _start_cleanup_daemon(self):
        """Start background thread for cleaning up stale agents"""
        def cleanup_loop():
            while True:
                try:
                    self.cleanup_stale_agents()
                except Exception:
                    pass
                time.sleep(self.cleanup_interval)
        
        daemon = threading.Thread(target=cleanup_loop, daemon=True)
        daemon.start()


class AgentLifecycle:
    """Manages the lifecycle of an agent"""
    
    def __init__(self, agent_id: str = None, metadata: Dict[str, Any] = None):
        self.agent_id = agent_id or self._generate_agent_id()
        self.metadata = metadata or {}
        self.registry = AgentRegistry()
        self.workspace = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", self.agent_id
        )
        self.heartbeat_interval = 30
        self._heartbeat_thread = None
        self._active = False
    
    def _generate_agent_id(self) -> str:
        """Generate unique agent ID"""
        return f"claude-{os.getpid()}-{uuid.uuid4().hex[:8]}"
    
    def startup(self) -> bool:
        """Initialize agent and register with coordinator"""
        try:
            # Create agent workspace
            os.makedirs(self.workspace, exist_ok=True)
            
            # Create subdirectories
            for subdir in ["sessions", "state", "cache", "logs"]:
                os.makedirs(os.path.join(self.workspace, subdir), exist_ok=True)
            
            # Register with coordinator
            if self.registry.register_agent(self.agent_id, self.metadata):
                self._active = True
                self._start_heartbeat()
                return True
            
            return False
            
        except Exception as e:
            print(f"Agent startup failed: {e}")
            return False
    
    def shutdown(self, reason: str = "normal"):
        """Gracefully shut down agent"""
        self._active = False
        
        # Stop heartbeat
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
        
        # TODO: Complete pending operations
        # TODO: Release all locks
        # TODO: Archive workspace
        
        # Deregister from coordinator
        self.registry.deregister_agent(self.agent_id, reason)
    
    def _start_heartbeat(self):
        """Start heartbeat daemon"""
        def heartbeat_loop():
            while self._active:
                try:
                    self.registry.heartbeat(self.agent_id)
                except Exception:
                    pass
                time.sleep(self.heartbeat_interval)
        
        self._heartbeat_thread = threading.Thread(target=heartbeat_loop, daemon=True)
        self._heartbeat_thread.start()


if __name__ == "__main__":
    # Example usage
    print("Testing Agent Registry...")
    
    # Create test agent
    agent_id = f"test-agent-{os.getpid()}"
    lifecycle = AgentLifecycle(agent_id, {
        "work_package": "test-wp",
        "agent_type": "development"
    })
    
    print(f"\n1. Starting agent: {agent_id}")
    if lifecycle.startup():
        print("✓ Agent started successfully")
    else:
        print("✗ Agent startup failed")
    
    # Test registry operations
    registry = AgentRegistry()
    
    print("\n2. Listing active agents:")
    agents = registry.list_active_agents()
    for agent in agents:
        print(f"  - {agent.agent_id} (type: {agent.agent_type}, uptime: {int(time.time() - agent.started)}s)")
    
    print("\n3. Registry statistics:")
    stats = registry.get_registry_stats()
    print(f"  Total active: {stats['total_active']}")
    print(f"  By type: {stats['by_type']}")
    print(f"  Average uptime: {stats['average_uptime']}s")
    
    # Shutdown
    print("\n4. Shutting down agent...")
    lifecycle.shutdown()
    print("✓ Agent shutdown complete")