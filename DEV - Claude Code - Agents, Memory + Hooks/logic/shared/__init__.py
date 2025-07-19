"""
Shared utilities for hooks and multi-agent system
"""

# Hook components
from .hook_base import HookBase, ToolHook, UserPromptHook
from .hook_settings import SettingsManager, StateManager
from .hook_formatters import MessageFormatter
from .hook_state import SessionStateManager, FileTracker, TestTracker
from .hook_priority import HookPriorityManager, HookMetadata, HookExecution
from .hook_manager import ProcessAwareHookManager as HookManager
from .hook_registry import HookRegistry

# Multi-agent support components
from .distributed_lock_manager import (
    DistributedLock, DistributedLockManager, 
    GitLock, MemoryLock, HookLock
)
from .agent_registry import AgentRegistry, AgentInfo, AgentLifecycle
from .message_queue import Message, MessageQueue, AsyncMessageQueue
from .resource_monitor import (
    ResourceMonitor, ResourceUsage, ResourceLimits,
    GlobalResourceManager
)
from .conflict_resolver import (
    ConflictResolver, Conflict, ConflictType, 
    ConflictResolution, OptimisticLockManager
)

__all__ = [
    # Original hook components
    'HookBase',
    'ToolHook',
    'UserPromptHook',
    'SettingsManager',
    'StateManager',
    'MessageFormatter',
    'SessionStateManager',
    'FileTracker',
    'TestTracker',
    'HookPriorityManager',
    'HookMetadata',
    'HookExecution',
    'ProcessAwareHookManager',
    'HookRegistry',
    
    # Multi-agent components
    'DistributedLock',
    'DistributedLockManager',
    'GitLock',
    'MemoryLock',
    'HookLock',
    'AgentRegistry',
    'AgentInfo',
    'AgentLifecycle',
    'Message',
    'MessageQueue',
    'AsyncMessageQueue',
    'ResourceMonitor',
    'ResourceUsage',
    'ResourceLimits',
    'GlobalResourceManager',
    'ConflictResolver',
    'Conflict',
    'ConflictType',
    'ConflictResolution',
    'OptimisticLockManager'
]