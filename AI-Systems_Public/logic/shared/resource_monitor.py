#!/usr/bin/env python3
"""
Resource Monitor for Multi-Agent System

Monitors and manages resource usage across agents to prevent exhaustion
and ensure fair resource allocation.
"""

import os
import json
import time
import psutil
import threading
from typing import Dict, Any, List, Optional, Callable
from collections import defaultdict
from datetime import datetime

from .distributed_lock_manager import DistributedLockManager


class ResourceUsage:
    """Resource usage snapshot for an agent"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.timestamp = time.time()
        self.pid = os.getpid()
        
        # Get process info
        try:
            process = psutil.Process(self.pid)
            
            # Memory usage
            memory_info = process.memory_info()
            self.memory_mb = memory_info.rss / 1024 / 1024
            self.memory_percent = process.memory_percent()
            
            # CPU usage
            self.cpu_percent = process.cpu_percent(interval=0.1)
            
            # File handles
            self.open_files = len(process.open_files())
            self.num_threads = process.num_threads()
            
            # Disk I/O
            io_counters = process.io_counters()
            self.read_bytes = io_counters.read_bytes
            self.write_bytes = io_counters.write_bytes
            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Process doesn't exist or no access
            self.memory_mb = 0
            self.memory_percent = 0
            self.cpu_percent = 0
            self.open_files = 0
            self.num_threads = 1
            self.read_bytes = 0
            self.write_bytes = 0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "agent_id": self.agent_id,
            "timestamp": self.timestamp,
            "pid": self.pid,
            "memory_mb": round(self.memory_mb, 2),
            "memory_percent": round(self.memory_percent, 2),
            "cpu_percent": round(self.cpu_percent, 2),
            "open_files": self.open_files,
            "num_threads": self.num_threads,
            "read_bytes": self.read_bytes,
            "write_bytes": self.write_bytes
        }


class ResourceLimits:
    """Resource limits for agents"""
    
    def __init__(self, limits: Dict[str, Any] = None):
        default_limits = {
            "memory_mb": 512,        # Max memory in MB
            "memory_percent": 5.0,   # Max memory percentage
            "cpu_percent": 25.0,     # Max CPU percentage
            "open_files": 100,       # Max open file handles
            "num_threads": 10,       # Max threads
            "disk_write_mb_per_min": 100  # Max disk write rate
        }
        
        self.limits = {**default_limits, **(limits or {})}
    
    def check_usage(self, usage: ResourceUsage) -> Dict[str, bool]:
        """
        Check if usage exceeds limits
        
        Returns:
            Dict mapping resource name to whether limit exceeded
        """
        violations = {}
        
        if usage.memory_mb > self.limits["memory_mb"]:
            violations["memory_mb"] = True
        
        if usage.memory_percent > self.limits["memory_percent"]:
            violations["memory_percent"] = True
        
        if usage.cpu_percent > self.limits["cpu_percent"]:
            violations["cpu_percent"] = True
        
        if usage.open_files > self.limits["open_files"]:
            violations["open_files"] = True
        
        if usage.num_threads > self.limits["num_threads"]:
            violations["num_threads"] = True
        
        return violations


class ResourceMonitor:
    """Monitors resource usage across agents"""
    
    def __init__(self, agent_id: str, monitor_dir: str = None):
        self.agent_id = agent_id
        self.monitor_dir = monitor_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "monitoring"
        )
        self.usage_file = os.path.join(self.monitor_dir, f"{agent_id}_usage.json")
        self.limits = ResourceLimits()
        self.lock_manager = DistributedLockManager(agent_id)
        
        # Monitoring state
        self.monitor_interval = 5  # seconds
        self.history_size = 100  # Keep last N measurements
        self.usage_history: List[ResourceUsage] = []
        self.violation_callbacks: List[Callable] = []
        self._monitoring = False
        self._monitor_thread = None
        
        # Throttling state
        self.throttled = False
        self.throttle_until = 0
        
        # Ensure directory exists
        os.makedirs(self.monitor_dir, exist_ok=True)
    
    def set_limits(self, limits: Dict[str, Any]):
        """Update resource limits"""
        self.limits = ResourceLimits(limits)
    
    def add_violation_callback(self, callback: Callable[[str, Dict[str, bool]], None]):
        """Add callback for limit violations"""
        self.violation_callbacks.append(callback)
    
    def start_monitoring(self):
        """Start resource monitoring"""
        if self._monitoring:
            return
        
        self._monitoring = True
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()
    
    def stop_monitoring(self):
        """Stop resource monitoring"""
        self._monitoring = False
        if self._monitor_thread:
            self._monitor_thread.join(timeout=5)
    
    def get_current_usage(self) -> ResourceUsage:
        """Get current resource usage"""
        return ResourceUsage(self.agent_id)
    
    def check_limits(self) -> bool:
        """
        Check if agent is within resource limits
        
        Returns:
            True if within limits, False if any limit exceeded
        """
        usage = self.get_current_usage()
        violations = self.limits.check_usage(usage)
        
        if violations:
            # Notify callbacks
            for callback in self.violation_callbacks:
                try:
                    callback(self.agent_id, violations)
                except Exception as e:
                    print(f"Violation callback error: {e}")
            
            return False
        
        return True
    
    def throttle_agent(self, duration: int = 30):
        """Throttle agent for specified duration"""
        self.throttled = True
        self.throttle_until = time.time() + duration
        
        # Could implement actual throttling here
        # For now, just set the flag
    
    def is_throttled(self) -> bool:
        """Check if agent is currently throttled"""
        if self.throttled and time.time() > self.throttle_until:
            self.throttled = False
        return self.throttled
    
    def get_usage_stats(self) -> Dict[str, Any]:
        """Get usage statistics"""
        if not self.usage_history:
            return {}
        
        # Calculate averages
        avg_memory = sum(u.memory_mb for u in self.usage_history) / len(self.usage_history)
        avg_cpu = sum(u.cpu_percent for u in self.usage_history) / len(self.usage_history)
        max_memory = max(u.memory_mb for u in self.usage_history)
        max_cpu = max(u.cpu_percent for u in self.usage_history)
        
        return {
            "samples": len(self.usage_history),
            "avg_memory_mb": round(avg_memory, 2),
            "avg_cpu_percent": round(avg_cpu, 2),
            "max_memory_mb": round(max_memory, 2),
            "max_cpu_percent": round(max_cpu, 2),
            "throttled": self.throttled,
            "limits": self.limits.limits
        }
    
    def _monitor_loop(self):
        """Background monitoring loop"""
        while self._monitoring:
            try:
                # Take measurement
                usage = self.get_current_usage()
                
                # Add to history
                self.usage_history.append(usage)
                if len(self.usage_history) > self.history_size:
                    self.usage_history.pop(0)
                
                # Check limits
                violations = self.limits.check_usage(usage)
                if violations and not self.throttled:
                    self.throttle_agent()
                
                # Save current usage
                self._save_usage(usage)
                
            except Exception as e:
                print(f"Monitor loop error: {e}")
            
            time.sleep(self.monitor_interval)
    
    def _save_usage(self, usage: ResourceUsage):
        """Save usage data to disk"""
        try:
            with self.lock_manager.atomic_file_operation(self.usage_file):
                data = {
                    "current": usage.to_dict(),
                    "stats": self.get_usage_stats(),
                    "throttled": self.throttled
                }
                
                with open(self.usage_file, 'w') as f:
                    json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Failed to save usage data: {e}")


class GlobalResourceManager:
    """Manages resources across all agents"""
    
    def __init__(self, manager_dir: str = None):
        self.manager_dir = manager_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "monitoring"
        )
        self.global_limits = {
            "total_memory_mb": 2048,     # Total memory for all agents
            "total_cpu_percent": 80.0,   # Total CPU for all agents
            "max_agents": 10             # Maximum concurrent agents
        }
        self.lock_manager = DistributedLockManager("resource-manager")
    
    def get_total_usage(self) -> Dict[str, Any]:
        """Get total resource usage across all agents"""
        total = {
            "memory_mb": 0,
            "cpu_percent": 0,
            "agent_count": 0,
            "agents": {}
        }
        
        # Read all agent usage files
        if os.path.exists(self.manager_dir):
            for filename in os.listdir(self.manager_dir):
                if filename.endswith("_usage.json"):
                    agent_id = filename[:-11]  # Remove _usage.json
                    
                    try:
                        with open(os.path.join(self.manager_dir, filename), 'r') as f:
                            data = json.load(f)
                        
                        current = data.get("current", {})
                        total["memory_mb"] += current.get("memory_mb", 0)
                        total["cpu_percent"] += current.get("cpu_percent", 0)
                        total["agent_count"] += 1
                        total["agents"][agent_id] = current
                        
                    except Exception:
                        pass
        
        return total
    
    def can_start_agent(self) -> bool:
        """Check if a new agent can be started"""
        usage = self.get_total_usage()
        
        # Check agent count
        if usage["agent_count"] >= self.global_limits["max_agents"]:
            return False
        
        # Check total memory
        if usage["memory_mb"] > self.global_limits["total_memory_mb"] * 0.8:
            return False
        
        # Check total CPU
        if usage["cpu_percent"] > self.global_limits["total_cpu_percent"]:
            return False
        
        return True
    
    def get_resource_allocation(self, agent_id: str) -> ResourceLimits:
        """Get resource limits for a specific agent"""
        usage = self.get_total_usage()
        agent_count = max(1, usage["agent_count"])
        
        # Divide resources fairly among agents
        per_agent_memory = self.global_limits["total_memory_mb"] / agent_count
        per_agent_cpu = self.global_limits["total_cpu_percent"] / agent_count
        
        return ResourceLimits({
            "memory_mb": min(512, per_agent_memory),
            "cpu_percent": min(25.0, per_agent_cpu)
        })


if __name__ == "__main__":
    # Example usage
    print("Testing Resource Monitor...")
    
    agent_id = f"test-agent-{os.getpid()}"
    monitor = ResourceMonitor(agent_id)
    
    # Set up violation callback
    def on_violation(agent: str, violations: Dict[str, bool]):
        print(f"\n⚠️  Resource violations for {agent}:")
        for resource, exceeded in violations.items():
            if exceeded:
                print(f"  - {resource} limit exceeded")
    
    monitor.add_violation_callback(on_violation)
    
    print(f"\n1. Current resource usage:")
    usage = monitor.get_current_usage()
    for key, value in usage.to_dict().items():
        if key not in ["agent_id", "timestamp", "pid"]:
            print(f"  {key}: {value}")
    
    print(f"\n2. Checking limits...")
    if monitor.check_limits():
        print("✓ All resources within limits")
    else:
        print("✗ Some resources exceed limits")
    
    print(f"\n3. Starting monitoring...")
    monitor.start_monitoring()
    print("✓ Monitoring started")
    
    # Test global manager
    print(f"\n4. Testing global resource manager...")
    global_mgr = GlobalResourceManager()
    
    if global_mgr.can_start_agent():
        print("✓ Can start new agent")
    else:
        print("✗ Cannot start new agent")
    
    total_usage = global_mgr.get_total_usage()
    print(f"\nTotal usage across {total_usage['agent_count']} agents:")
    print(f"  Memory: {total_usage['memory_mb']:.1f} MB")
    print(f"  CPU: {total_usage['cpu_percent']:.1f}%")
    
    # Stop monitoring
    time.sleep(2)
    monitor.stop_monitoring()
    print("\n✓ Resource monitor test complete")