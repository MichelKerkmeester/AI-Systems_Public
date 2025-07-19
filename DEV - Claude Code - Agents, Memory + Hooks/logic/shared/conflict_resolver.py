#!/usr/bin/env python3
"""
Conflict Resolver for Multi-Agent System

Handles conflicts when multiple agents try to access the same resources
or perform conflicting operations.
"""

import os
import json
import time
import hashlib
import difflib
from typing import Dict, Any, List, Optional, Tuple
from enum import Enum
from datetime import datetime

from .distributed_lock_manager import DistributedLockManager
from .message_queue import MessageQueue, Message


class ConflictType(Enum):
    """Types of conflicts that can occur"""
    FILE_EDIT = "file_edit"
    GIT_OPERATION = "git_operation"
    TASK_ASSIGNMENT = "task_assignment"
    RESOURCE_ACCESS = "resource_access"
    HOOK_EXECUTION = "hook_execution"
    MEMORY_UPDATE = "memory_update"


class ConflictResolution(Enum):
    """Possible conflict resolutions"""
    FIRST_WINS = "first_wins"
    LAST_WINS = "last_wins"
    MERGE = "merge"
    QUEUE = "queue"
    REJECT = "reject"
    MANUAL = "manual"


class Conflict:
    """Represents a conflict between agents"""
    
    def __init__(self,
                 conflict_type: ConflictType,
                 resource: str,
                 agent1_id: str,
                 agent2_id: str,
                 details: Dict[str, Any] = None):
        self.id = f"{time.time()}-{hashlib.md5(resource.encode()).hexdigest()[:8]}"
        self.conflict_type = conflict_type
        self.resource = resource
        self.agent1_id = agent1_id
        self.agent2_id = agent2_id
        self.details = details or {}
        self.timestamp = time.time()
        self.resolution = None
        self.resolved = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "type": self.conflict_type.value,
            "resource": self.resource,
            "agent1": self.agent1_id,
            "agent2": self.agent2_id,
            "details": self.details,
            "timestamp": self.timestamp,
            "resolution": self.resolution.value if self.resolution else None,
            "resolved": self.resolved
        }


class ConflictResolver:
    """Resolves conflicts between agents"""
    
    def __init__(self, resolver_dir: str = None):
        self.resolver_dir = resolver_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "conflicts"
        )
        self.lock_manager = DistributedLockManager("conflict-resolver")
        self.conflict_log = os.path.join(self.resolver_dir, "conflict-log.json")
        
        # Resolution strategies by conflict type
        self.strategies = {
            ConflictType.FILE_EDIT: self._resolve_file_edit_conflict,
            ConflictType.GIT_OPERATION: self._resolve_git_conflict,
            ConflictType.TASK_ASSIGNMENT: self._resolve_task_conflict,
            ConflictType.RESOURCE_ACCESS: self._resolve_resource_conflict,
            ConflictType.HOOK_EXECUTION: self._resolve_hook_conflict,
            ConflictType.MEMORY_UPDATE: self._resolve_memory_conflict
        }
        
        # Queue for deferred operations
        self.operation_queue: Dict[str, List[Dict[str, Any]]] = {}
        
        # Ensure directory exists
        os.makedirs(self.resolver_dir, exist_ok=True)
    
    def resolve_conflict(self, conflict: Conflict) -> ConflictResolution:
        """
        Resolve a conflict between agents
        
        Args:
            conflict: The conflict to resolve
            
        Returns:
            The resolution applied
        """
        # Log the conflict
        self._log_conflict(conflict)
        
        # Apply appropriate strategy
        if conflict.conflict_type in self.strategies:
            resolution = self.strategies[conflict.conflict_type](conflict)
        else:
            # Default: first agent wins
            resolution = ConflictResolution.FIRST_WINS
        
        # Mark as resolved
        conflict.resolution = resolution
        conflict.resolved = True
        
        # Update log
        self._update_conflict_log(conflict)
        
        return resolution
    
    def _resolve_file_edit_conflict(self, conflict: Conflict) -> ConflictResolution:
        """Resolve file edit conflicts"""
        file_path = conflict.resource
        
        # Check if we can merge the changes
        if self._can_merge_file_edits(conflict):
            # Attempt three-way merge
            if self._merge_file_edits(conflict):
                return ConflictResolution.MERGE
        
        # If merge not possible, use optimistic locking
        # The agent with the latest file version wins
        agent1_version = conflict.details.get("agent1_version", 0)
        agent2_version = conflict.details.get("agent2_version", 0)
        
        if agent1_version > agent2_version:
            return ConflictResolution.FIRST_WINS
        elif agent2_version > agent1_version:
            return ConflictResolution.LAST_WINS
        else:
            # Same version, queue second operation
            self._queue_operation(conflict.agent2_id, {
                "type": "file_edit",
                "file": file_path,
                "operation": conflict.details.get("agent2_operation")
            })
            return ConflictResolution.QUEUE
    
    def _resolve_git_conflict(self, conflict: Conflict) -> ConflictResolution:
        """Resolve git operation conflicts"""
        # Git operations must be sequential
        # Queue the second operation
        self._queue_operation(conflict.agent2_id, {
            "type": "git_operation",
            "command": conflict.details.get("agent2_command")
        })
        return ConflictResolution.QUEUE
    
    def _resolve_task_conflict(self, conflict: Conflict) -> ConflictResolution:
        """Resolve task assignment conflicts"""
        # First agent to claim task wins
        return ConflictResolution.FIRST_WINS
    
    def _resolve_resource_conflict(self, conflict: Conflict) -> ConflictResolution:
        """Resolve resource access conflicts"""
        # Check if resource allows concurrent access
        if conflict.details.get("concurrent_allowed", False):
            return ConflictResolution.MERGE  # Both can access
        
        # Exclusive resource - first wins
        return ConflictResolution.FIRST_WINS
    
    def _resolve_hook_conflict(self, conflict: Conflict) -> ConflictResolution:
        """Resolve hook execution conflicts"""
        # Check hook priority
        agent1_priority = conflict.details.get("agent1_priority", 5)
        agent2_priority = conflict.details.get("agent2_priority", 5)
        
        if agent1_priority < agent2_priority:  # Lower number = higher priority
            return ConflictResolution.FIRST_WINS
        elif agent2_priority < agent1_priority:
            return ConflictResolution.LAST_WINS
        else:
            # Same priority - check if concurrent safe
            if conflict.details.get("concurrent_safe", True):
                return ConflictResolution.MERGE  # Both can run
            else:
                return ConflictResolution.QUEUE
    
    def _resolve_memory_conflict(self, conflict: Conflict) -> ConflictResolution:
        """Resolve memory update conflicts"""
        # Use transaction-based approach
        # Last write wins with rollback capability
        return ConflictResolution.LAST_WINS
    
    def _can_merge_file_edits(self, conflict: Conflict) -> bool:
        """Check if file edits can be merged"""
        # Check if edits are to different parts of file
        agent1_lines = set(conflict.details.get("agent1_lines", []))
        agent2_lines = set(conflict.details.get("agent2_lines", []))
        
        # If no line overlap, can merge
        return len(agent1_lines.intersection(agent2_lines)) == 0
    
    def _merge_file_edits(self, conflict: Conflict) -> bool:
        """Attempt to merge file edits"""
        try:
            file_path = conflict.resource
            
            # Get original content
            with open(file_path, 'r') as f:
                original = f.readlines()
            
            # Apply both sets of changes
            # This is simplified - real implementation would be more sophisticated
            content = original.copy()
            
            # Apply agent1 changes
            for change in conflict.details.get("agent1_changes", []):
                if change["type"] == "replace":
                    start, end = change["lines"]
                    content[start:end] = change["new_content"]
            
            # Apply agent2 changes
            for change in conflict.details.get("agent2_changes", []):
                if change["type"] == "replace":
                    start, end = change["lines"]
                    content[start:end] = change["new_content"]
            
            # Write merged content
            with open(file_path, 'w') as f:
                f.writelines(content)
            
            return True
            
        except Exception as e:
            print(f"Merge failed: {e}")
            return False
    
    def _queue_operation(self, agent_id: str, operation: Dict[str, Any]):
        """Queue an operation for later execution"""
        if agent_id not in self.operation_queue:
            self.operation_queue[agent_id] = []
        
        operation["queued_at"] = time.time()
        self.operation_queue[agent_id].append(operation)
        
        # Save queue to disk
        queue_file = os.path.join(self.resolver_dir, f"queue_{agent_id}.json")
        with open(queue_file, 'w') as f:
            json.dump(self.operation_queue[agent_id], f, indent=2)
    
    def get_queued_operations(self, agent_id: str) -> List[Dict[str, Any]]:
        """Get queued operations for an agent"""
        queue_file = os.path.join(self.resolver_dir, f"queue_{agent_id}.json")
        
        if os.path.exists(queue_file):
            with open(queue_file, 'r') as f:
                return json.load(f)
        
        return []
    
    def clear_queued_operations(self, agent_id: str):
        """Clear queued operations for an agent"""
        if agent_id in self.operation_queue:
            del self.operation_queue[agent_id]
        
        queue_file = os.path.join(self.resolver_dir, f"queue_{agent_id}.json")
        if os.path.exists(queue_file):
            os.remove(queue_file)
    
    def _log_conflict(self, conflict: Conflict):
        """Log conflict to history"""
        log_entry = {
            **conflict.to_dict(),
            "logged_at": time.time()
        }
        
        # Append to log file
        with self.lock_manager.atomic_file_operation(self.conflict_log):
            log = []
            if os.path.exists(self.conflict_log):
                with open(self.conflict_log, 'r') as f:
                    log = json.load(f)
            
            log.append(log_entry)
            
            # Keep only last 1000 conflicts
            if len(log) > 1000:
                log = log[-1000:]
            
            with open(self.conflict_log, 'w') as f:
                json.dump(log, f, indent=2)
    
    def _update_conflict_log(self, conflict: Conflict):
        """Update conflict resolution in log"""
        with self.lock_manager.atomic_file_operation(self.conflict_log):
            if os.path.exists(self.conflict_log):
                with open(self.conflict_log, 'r') as f:
                    log = json.load(f)
                
                # Find and update the conflict
                for entry in log:
                    if entry["id"] == conflict.id:
                        entry["resolution"] = conflict.resolution.value
                        entry["resolved"] = True
                        entry["resolved_at"] = time.time()
                        break
                
                with open(self.conflict_log, 'w') as f:
                    json.dump(log, f, indent=2)
    
    def get_conflict_stats(self) -> Dict[str, Any]:
        """Get statistics about conflicts"""
        stats = {
            "total_conflicts": 0,
            "resolved_conflicts": 0,
            "by_type": {},
            "by_resolution": {},
            "recent_conflicts": []
        }
        
        if os.path.exists(self.conflict_log):
            with open(self.conflict_log, 'r') as f:
                log = json.load(f)
            
            stats["total_conflicts"] = len(log)
            
            for entry in log:
                # Count by type
                conflict_type = entry["type"]
                stats["by_type"][conflict_type] = stats["by_type"].get(conflict_type, 0) + 1
                
                # Count by resolution
                if entry.get("resolved"):
                    stats["resolved_conflicts"] += 1
                    resolution = entry.get("resolution", "unknown")
                    stats["by_resolution"][resolution] = stats["by_resolution"].get(resolution, 0) + 1
            
            # Get recent conflicts
            stats["recent_conflicts"] = log[-10:] if len(log) > 10 else log
        
        return stats


class OptimisticLockManager:
    """Manages optimistic locking for file edits"""
    
    def __init__(self, lock_dir: str = None):
        self.lock_dir = lock_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "file-versions"
        )
        os.makedirs(self.lock_dir, exist_ok=True)
    
    def get_file_version(self, file_path: str) -> int:
        """Get current version of a file"""
        version_file = self._get_version_file(file_path)
        
        if os.path.exists(version_file):
            with open(version_file, 'r') as f:
                data = json.load(f)
                return data.get("version", 0)
        
        return 0
    
    def update_file_version(self, file_path: str, old_version: int) -> bool:
        """
        Update file version if current version matches expected
        
        Returns:
            True if update successful, False if version mismatch
        """
        version_file = self._get_version_file(file_path)
        
        # Use distributed lock for atomic update
        lock_manager = DistributedLockManager("version-manager")
        
        with lock_manager.atomic_file_operation(version_file):
            current_version = self.get_file_version(file_path)
            
            if current_version != old_version:
                return False
            
            # Update version
            data = {
                "file": file_path,
                "version": current_version + 1,
                "updated_at": time.time()
            }
            
            with open(version_file, 'w') as f:
                json.dump(data, f)
            
            return True
    
    def _get_version_file(self, file_path: str) -> str:
        """Get version file path for a given file"""
        file_hash = hashlib.md5(file_path.encode()).hexdigest()
        return os.path.join(self.lock_dir, f"{file_hash}.json")


if __name__ == "__main__":
    # Example usage
    print("Testing Conflict Resolver...")
    
    resolver = ConflictResolver()
    
    # Test file edit conflict
    print("\n1. Testing file edit conflict:")
    conflict1 = Conflict(
        conflict_type=ConflictType.FILE_EDIT,
        resource="/tmp/test.py",
        agent1_id="agent-1",
        agent2_id="agent-2",
        details={
            "agent1_lines": [10, 11, 12],
            "agent2_lines": [20, 21, 22],
            "agent1_version": 5,
            "agent2_version": 5
        }
    )
    
    resolution1 = resolver.resolve_conflict(conflict1)
    print(f"✓ Resolution: {resolution1.value}")
    
    # Test git conflict
    print("\n2. Testing git operation conflict:")
    conflict2 = Conflict(
        conflict_type=ConflictType.GIT_OPERATION,
        resource="git",
        agent1_id="agent-1",
        agent2_id="agent-2",
        details={
            "agent1_command": "git commit",
            "agent2_command": "git push"
        }
    )
    
    resolution2 = resolver.resolve_conflict(conflict2)
    print(f"✓ Resolution: {resolution2.value}")
    
    # Check queued operations
    print("\n3. Checking queued operations:")
    queued = resolver.get_queued_operations("agent-2")
    print(f"✓ Queued operations for agent-2: {len(queued)}")
    
    # Get conflict stats
    print("\n4. Conflict statistics:")
    stats = resolver.get_conflict_stats()
    print(f"  Total conflicts: {stats['total_conflicts']}")
    print(f"  Resolved: {stats['resolved_conflicts']}")
    print(f"  By type: {stats['by_type']}")
    print(f"  By resolution: {stats['by_resolution']}")
    
    # Test optimistic locking
    print("\n5. Testing optimistic locking:")
    lock_mgr = OptimisticLockManager()
    
    file_path = "/tmp/test-version.txt"
    version = lock_mgr.get_file_version(file_path)
    print(f"  Current version: {version}")
    
    if lock_mgr.update_file_version(file_path, version):
        print("✓ Version updated successfully")
    else:
        print("✗ Version conflict detected")
    
    print("\n✓ Conflict resolver test complete")