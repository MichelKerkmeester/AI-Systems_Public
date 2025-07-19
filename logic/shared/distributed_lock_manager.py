#!/usr/bin/env python3
"""
Distributed Lock Manager for Multi-Agent Concurrency

Provides file-based distributed locking mechanism to ensure safe concurrent
execution of operations across multiple Claude agents.
"""

import os
import json
import time
import uuid
import fcntl
import errno
from typing import Optional, Dict, Any
from contextlib import contextmanager
from pathlib import Path


class DistributedLock:
    """File-based distributed lock for cross-agent synchronization"""
    
    def __init__(self, resource_name: str, agent_id: str, lock_dir: str = None):
        self.resource_name = resource_name
        self.agent_id = agent_id
        self.lock_dir = lock_dir or os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "locks"
        )
        self.lock_path = os.path.join(self.lock_dir, f"{resource_name}.lock")
        self.lock_timeout = 30  # seconds
        self.lock_fd = None
        
    def acquire(self, timeout: float = 5.0, blocking: bool = True) -> bool:
        """
        Acquire the lock with timeout
        
        Args:
            timeout: Maximum time to wait for lock acquisition
            blocking: Whether to block waiting for lock
            
        Returns:
            True if lock acquired, False otherwise
        """
        start_time = time.time()
        
        # Ensure lock directory exists
        os.makedirs(self.lock_dir, exist_ok=True)
        
        while True:
            try:
                # Try to create lock file
                self.lock_fd = os.open(
                    self.lock_path,
                    os.O_CREAT | os.O_EXCL | os.O_RDWR
                )
                
                # Write lock metadata
                lock_data = {
                    "agent_id": self.agent_id,
                    "timestamp": time.time(),
                    "pid": os.getpid(),
                    "resource": self.resource_name
                }
                os.write(self.lock_fd, json.dumps(lock_data).encode())
                os.fsync(self.lock_fd)
                
                return True
                
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
                
                # Lock file exists, check if stale
                if self._is_lock_stale():
                    self._cleanup_stale_lock()
                    continue
                
                # Not stale, check timeout
                if not blocking or (time.time() - start_time) >= timeout:
                    return False
                
                # Wait before retry
                time.sleep(0.1)
    
    def release(self):
        """Release the lock"""
        if self.lock_fd is not None:
            try:
                os.close(self.lock_fd)
                os.remove(self.lock_path)
            except OSError:
                pass
            finally:
                self.lock_fd = None
    
    def _is_lock_stale(self) -> bool:
        """Check if existing lock is stale"""
        try:
            with open(self.lock_path, 'r') as f:
                lock_data = json.load(f)
            
            # Check if lock has timed out
            lock_age = time.time() - lock_data.get("timestamp", 0)
            if lock_age > self.lock_timeout:
                return True
            
            # Check if process is still alive (same machine only)
            pid = lock_data.get("pid")
            if pid:
                try:
                    # Send signal 0 to check if process exists
                    os.kill(pid, 0)
                except OSError:
                    return True
            
            return False
            
        except (IOError, json.JSONDecodeError):
            # Can't read lock file, consider it stale
            return True
    
    def _cleanup_stale_lock(self):
        """Remove stale lock file"""
        try:
            os.remove(self.lock_path)
        except OSError:
            pass
    
    def __enter__(self):
        """Context manager entry"""
        if not self.acquire():
            raise TimeoutError(f"Could not acquire lock for {self.resource_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.release()


class DistributedLockManager:
    """Manager for distributed locks across agents"""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.locks_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            "agents", "locks"
        )
        self.active_locks: Dict[str, DistributedLock] = {}
    
    def acquire_lock(self, resource_name: str, timeout: float = 5.0) -> Optional[DistributedLock]:
        """
        Acquire a distributed lock
        
        Args:
            resource_name: Name of the resource to lock
            timeout: Maximum time to wait for lock
            
        Returns:
            DistributedLock instance if acquired, None otherwise
        """
        if resource_name in self.active_locks:
            return self.active_locks[resource_name]
        
        lock = DistributedLock(resource_name, self.agent_id, self.locks_dir)
        if lock.acquire(timeout):
            self.active_locks[resource_name] = lock
            return lock
        
        return None
    
    def release_lock(self, resource_name: str):
        """Release a distributed lock"""
        if resource_name in self.active_locks:
            self.active_locks[resource_name].release()
            del self.active_locks[resource_name]
    
    @contextmanager
    def atomic_file_operation(self, file_path: str, timeout: float = 5.0):
        """
        Context manager for atomic file operations
        
        Args:
            file_path: Path to file requiring atomic access
            timeout: Maximum time to wait for lock
        """
        # Create lock name from file path
        import hashlib
        lock_name = f"file_{hashlib.md5(file_path.encode()).hexdigest()[:16]}"
        
        lock = self.acquire_lock(lock_name, timeout)
        if not lock:
            raise TimeoutError(f"Could not acquire lock for {file_path}")
        
        try:
            yield
        finally:
            self.release_lock(lock_name)
    
    def cleanup_all_locks(self):
        """Release all locks held by this manager"""
        for resource_name in list(self.active_locks.keys()):
            self.release_lock(resource_name)
    
    def list_active_locks(self) -> Dict[str, Dict[str, Any]]:
        """List all active locks in the system"""
        active_locks = {}
        
        if not os.path.exists(self.locks_dir):
            return active_locks
        
        for lock_file in os.listdir(self.locks_dir):
            if lock_file.endswith('.lock'):
                lock_path = os.path.join(self.locks_dir, lock_file)
                try:
                    with open(lock_path, 'r') as f:
                        lock_data = json.load(f)
                    resource_name = lock_file[:-5]  # Remove .lock extension
                    active_locks[resource_name] = lock_data
                except (IOError, json.JSONDecodeError):
                    pass
        
        return active_locks
    
    def cleanup_stale_locks(self):
        """Clean up all stale locks in the system"""
        if not os.path.exists(self.locks_dir):
            return
        
        for lock_file in os.listdir(self.locks_dir):
            if lock_file.endswith('.lock'):
                resource_name = lock_file[:-5]
                lock = DistributedLock(resource_name, "cleanup", self.locks_dir)
                if lock._is_lock_stale():
                    lock._cleanup_stale_lock()


# Specialized lock types for common resources
class GitLock(DistributedLock):
    """Specialized lock for git operations"""
    def __init__(self, agent_id: str):
        super().__init__("git", agent_id)
        self.lock_timeout = 60  # Git operations can take longer


class MemoryLock(DistributedLock):
    """Specialized lock for memory system operations"""
    def __init__(self, agent_id: str):
        super().__init__("memory", agent_id)


class HookLock(DistributedLock):
    """Specialized lock for hook executions"""
    def __init__(self, hook_name: str, agent_id: str):
        super().__init__(f"hook_{hook_name}", agent_id)
        self.lock_timeout = 10  # Hooks should be fast


if __name__ == "__main__":
    # Example usage
    import sys
    
    agent_id = f"test-agent-{os.getpid()}"
    manager = DistributedLockManager(agent_id)
    
    print(f"Testing distributed lock manager with agent ID: {agent_id}")
    
    # Test basic lock acquisition
    print("\n1. Testing basic lock acquisition...")
    lock = manager.acquire_lock("test-resource", timeout=2)
    if lock:
        print("✓ Lock acquired successfully")
        time.sleep(1)
        manager.release_lock("test-resource")
        print("✓ Lock released successfully")
    else:
        print("✗ Failed to acquire lock")
    
    # Test context manager
    print("\n2. Testing context manager...")
    try:
        with manager.atomic_file_operation("/tmp/test-file.txt"):
            print("✓ Inside atomic operation")
            time.sleep(1)
        print("✓ Context manager completed")
    except TimeoutError as e:
        print(f"✗ Context manager failed: {e}")
    
    # Test active locks listing
    print("\n3. Testing active locks listing...")
    active = manager.list_active_locks()
    print(f"Active locks: {active}")
    
    # Cleanup
    manager.cleanup_all_locks()
    print("\n✓ All tests completed")