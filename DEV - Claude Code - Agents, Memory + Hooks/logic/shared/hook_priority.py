"""
Hook Priority System for Claude Code
Manages hook execution order and conflict resolution
"""

import asyncio
import time
from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Dict, List, Any, Optional, Callable, Tuple
from pathlib import Path
import json
import hashlib


@dataclass
class HookMetadata:
    """Metadata for hook configuration with priority and concurrency settings"""
    name: str
    priority: int  # Lower number = higher priority (1=highest)
    concurrent_safe: bool = True
    exclusive_resources: List[str] = field(default_factory=list)
    max_parallel: Optional[int] = None
    timeout: int = 30000  # milliseconds
    retry_on_failure: bool = True
    retry_attempts: int = 3
    cache_ttl: int = 300  # seconds


@dataclass
class HookExecution:
    """Represents a hook execution request"""
    hook_name: str
    priority: int
    context: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    execution_id: str = field(default_factory=lambda: f"{time.time()}-{hashlib.md5(str(time.time()).encode()).hexdigest()[:8]}")
    
    def __lt__(self, other):
        """For priority queue ordering - lower priority number = higher priority"""
        return self.priority < other.priority


class HookPriorityManager:
    """Manages hook execution priority and concurrency"""
    
    # Default hook configurations
    DEFAULT_HOOKS = {
        "security-scan": HookMetadata(
            name="security-scan",
            priority=1,  # Highest priority
            concurrent_safe=False,
            exclusive_resources=["security-report.json"],
            timeout=10000
        ),
        "quality-check": HookMetadata(
            name="quality-check",
            priority=2,
            concurrent_safe=True,
            max_parallel=5,
            timeout=5000
        ),
        "workflow-automation": HookMetadata(
            name="workflow-automation",
            priority=3,
            concurrent_safe=True,
            max_parallel=10,
            timeout=30000
        ),
        "context-management": HookMetadata(
            name="context-management",
            priority=4,
            concurrent_safe=True,
            timeout=5000
        ),
        "pattern-extraction": HookMetadata(
            name="pattern-extraction",
            priority=5,
            concurrent_safe=True,
            timeout=60000  # May take longer with Gemini
        ),
        "session-management": HookMetadata(
            name="session-management",
            priority=2,
            concurrent_safe=False,
            exclusive_resources=["session-state.json"],
            timeout=10000
        ),
        "mode-suggestion": HookMetadata(
            name="mode-suggestion",
            priority=3,
            concurrent_safe=True,
            timeout=2000
        ),
        "memory-context": HookMetadata(
            name="memory-context",
            priority=3,
            concurrent_safe=True,
            timeout=5000
        )
    }
    
    def __init__(self, agent_id: Optional[str] = None):
        self.agent_id = agent_id or "main"
        self.hook_configs: Dict[str, HookMetadata] = self.DEFAULT_HOOKS.copy()
        self.priority_queue = PriorityQueue()
        self.executing_hooks: Dict[str, HookExecution] = {}
        self.hook_cache: Dict[str, Tuple[float, Any]] = {}
        self.performance_stats: Dict[str, List[float]] = {}
        
        # Load custom configurations if they exist
        self._load_custom_configs()
    
    def _load_custom_configs(self):
        """Load custom hook configurations from settings"""
        config_path = Path.home() / ".claude" / "logic" / "shared" / "hook-priority-config.json"
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    custom_configs = json.load(f)
                    for hook_name, config in custom_configs.items():
                        if hook_name in self.hook_configs:
                            # Update existing config
                            for key, value in config.items():
                                setattr(self.hook_configs[hook_name], key, value)
                        else:
                            # Add new hook config
                            self.hook_configs[hook_name] = HookMetadata(**config)
            except Exception as e:
                print(f"Error loading custom hook configs: {e}")
    
    def register_hook(self, hook_metadata: HookMetadata):
        """Register a new hook or update existing hook configuration"""
        self.hook_configs[hook_metadata.name] = hook_metadata
    
    def should_execute(self, hook_name: str, context: Dict[str, Any]) -> bool:
        """Determine if a hook should execute based on context and current state"""
        if hook_name not in self.hook_configs:
            return True  # Unknown hooks execute by default
        
        config = self.hook_configs[hook_name]
        
        # Check cache
        if hook_name in self.hook_cache:
            cache_time, cache_result = self.hook_cache[hook_name]
            if time.time() - cache_time < config.cache_ttl:
                # Skip execution if result is cached
                return False
        
        # Check if hook is already executing
        if not config.concurrent_safe and hook_name in self.executing_hooks:
            return False
        
        # Check max parallel executions
        if config.max_parallel:
            current_count = sum(1 for exec in self.executing_hooks.values() 
                              if exec.hook_name == hook_name)
            if current_count >= config.max_parallel:
                return False
        
        return True
    
    def queue_hook(self, hook_name: str, context: Dict[str, Any]) -> Optional[HookExecution]:
        """Queue a hook for execution"""
        if not self.should_execute(hook_name, context):
            return None
        
        config = self.hook_configs.get(hook_name, HookMetadata(name=hook_name, priority=99))
        execution = HookExecution(
            hook_name=hook_name,
            priority=config.priority,
            context=context
        )
        
        self.priority_queue.put(execution)
        return execution
    
    def get_next_hook(self) -> Optional[HookExecution]:
        """Get the next hook to execute from the priority queue"""
        if self.priority_queue.empty():
            return None
        
        return self.priority_queue.get()
    
    def mark_executing(self, execution: HookExecution):
        """Mark a hook as currently executing"""
        self.executing_hooks[execution.execution_id] = execution
    
    def mark_completed(self, execution: HookExecution, result: Any = None, 
                      execution_time: float = 0):
        """Mark a hook execution as completed"""
        if execution.execution_id in self.executing_hooks:
            del self.executing_hooks[execution.execution_id]
        
        # Update cache if result is provided
        if result is not None:
            self.hook_cache[execution.hook_name] = (time.time(), result)
        
        # Track performance
        if execution.hook_name not in self.performance_stats:
            self.performance_stats[execution.hook_name] = []
        self.performance_stats[execution.hook_name].append(execution_time)
        
        # Keep only last 100 measurements
        if len(self.performance_stats[execution.hook_name]) > 100:
            self.performance_stats[execution.hook_name] = \
                self.performance_stats[execution.hook_name][-100:]
    
    def get_performance_stats(self) -> Dict[str, Dict[str, float]]:
        """Get performance statistics for all hooks"""
        stats = {}
        for hook_name, times in self.performance_stats.items():
            if times:
                stats[hook_name] = {
                    "avg_ms": sum(times) / len(times),
                    "min_ms": min(times),
                    "max_ms": max(times),
                    "executions": len(times)
                }
        return stats
    
    def deduplicate_hooks(self, hook_list: List[str], context: Dict[str, Any]) -> List[str]:
        """Remove duplicate hook executions based on context"""
        seen = set()
        deduplicated = []
        
        for hook_name in hook_list:
            # Create a context hash for deduplication
            context_key = f"{hook_name}:{self._hash_context(context)}"
            if context_key not in seen:
                seen.add(context_key)
                deduplicated.append(hook_name)
        
        return deduplicated
    
    def _hash_context(self, context: Dict[str, Any]) -> str:
        """Create a hash of the context for deduplication"""
        # Extract key fields that determine uniqueness
        key_fields = {
            "toolName": context.get("toolName", ""),
            "file_path": context.get("toolInput", {}).get("file_path", ""),
            "userMessage": context.get("userMessage", "")[:100] if "userMessage" in context else ""
        }
        return hashlib.md5(json.dumps(key_fields, sort_keys=True).encode()).hexdigest()[:16]
    
    def get_hook_status(self) -> Dict[str, Any]:
        """Get current status of all hooks"""
        return {
            "queued": self.priority_queue.qsize(),
            "executing": len(self.executing_hooks),
            "executing_hooks": [exec.hook_name for exec in self.executing_hooks.values()],
            "performance": self.get_performance_stats(),
            "cache_size": len(self.hook_cache)
        }
    
    def clear_cache(self, hook_name: Optional[str] = None):
        """Clear hook result cache"""
        if hook_name:
            self.hook_cache.pop(hook_name, None)
        else:
            self.hook_cache.clear()
    
    def adjust_priority(self, hook_name: str, new_priority: int):
        """Dynamically adjust hook priority"""
        if hook_name in self.hook_configs:
            self.hook_configs[hook_name].priority = new_priority