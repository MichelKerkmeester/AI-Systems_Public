#!/usr/bin/env python3
"""
Multi-Agent Session Manager
Provides distributed locking and agent isolation for concurrent sessions
"""

import os
import sys
import json
import time
import uuid
import fcntl
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple
from contextlib import contextmanager

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))


class DistributedLock:
    """File-based distributed lock for multi-agent coordination"""
    
    def __init__(self, resource_name: str, agent_id: str, lock_dir: Path):
        self.resource_name = resource_name
        self.agent_id = agent_id
        self.lock_path = lock_dir / f"{resource_name}.lock"
        self.lock_timeout = 30  # seconds
        self.lock_dir = lock_dir
        self._lock_file = None
        
    def acquire(self, timeout: float = 5.0) -> bool:
        """Acquire lock with timeout"""
        os.makedirs(self.lock_dir, exist_ok=True)
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                # Try to create lock file atomically
                self._lock_file = open(self.lock_path, 'x')
                
                # Write lock info
                lock_data = {
                    "agent_id": self.agent_id,
                    "timestamp": time.time(),
                    "pid": os.getpid()
                }
                json.dump(lock_data, self._lock_file)
                self._lock_file.flush()
                
                # Use file locking for extra safety
                fcntl.flock(self._lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                
                return True
                
            except FileExistsError:
                # Lock exists, check if stale
                if self._is_lock_stale():
                    self._cleanup_stale_lock()
                else:
                    time.sleep(0.1)
            except IOError:
                # File locking failed
                if self._lock_file:
                    self._lock_file.close()
                    self._lock_file = None
                time.sleep(0.1)
        
        return False
    
    def release(self):
        """Release the lock"""
        if self._lock_file:
            try:
                fcntl.flock(self._lock_file.fileno(), fcntl.LOCK_UN)
                self._lock_file.close()
                self._lock_file = None
                
                if self.lock_path.exists():
                    self.lock_path.unlink()
            except:
                pass
    
    def _is_lock_stale(self) -> bool:
        """Check if lock is stale"""
        try:
            with open(self.lock_path, 'r') as f:
                lock_data = json.load(f)
            return time.time() - lock_data["timestamp"] > self.lock_timeout
        except:
            return True
    
    def _cleanup_stale_lock(self):
        """Remove stale lock file"""
        try:
            self.lock_path.unlink()
        except:
            pass
    
    def __enter__(self):
        if not self.acquire():
            raise RuntimeError(f"Could not acquire lock for {self.resource_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()


class MultiAgentSessionManager:
    """Manages sessions with multi-agent support"""
    
    def __init__(self, agent_id: Optional[str] = None):
        # Generate agent ID if not provided
        if not agent_id:
            agent_id = os.environ.get("CLAUDE_AGENT_ID")
        if not agent_id:
            agent_id = f"claude-{os.getpid()}-{uuid.uuid4().hex[:8]}"
        
        self.agent_id = agent_id
        
        # Get project root
        self.project_root = Path(__file__).resolve()
        while not (self.project_root / ".claude").exists() and self.project_root != self.project_root.parent:
            self.project_root = self.project_root.parent
        
        self.claude_path = self.project_root / ".claude"
        
        # Agent-specific paths
        self.agents_dir = self.claude_path / "agents"
        self.agent_dir = self.agents_dir / self.agent_id
        self.agent_sessions_dir = self.agent_dir / "sessions"
        
        # Global paths
        self.global_sessions_dir = self.claude_path / "sessions"
        self.global_registry_file = self.global_sessions_dir / "registry.json"
        self.locks_dir = self.agents_dir / "locks"
        
        # Initialize directories
        self._init_directories()
        
    def _init_directories(self):
        """Initialize directory structure"""
        os.makedirs(self.agent_sessions_dir / "current", exist_ok=True)
        os.makedirs(self.agent_sessions_dir / "archived", exist_ok=True)
        os.makedirs(self.global_sessions_dir, exist_ok=True)
        os.makedirs(self.locks_dir, exist_ok=True)
        
        # Agent state file
        self.agent_state_file = self.agent_dir / ".session-state.json"
        
    @contextmanager
    def distributed_lock(self, resource: str):
        """Context manager for distributed locking"""
        lock = DistributedLock(resource, self.agent_id, self.locks_dir)
        try:
            yield lock
        finally:
            lock.release()
    
    def create_session(self, description: str = "") -> str:
        """Create a new session with agent awareness"""
        timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        session_name = f"{timestamp}-{self.agent_id}-{description}.md" if description else f"{timestamp}-{self.agent_id}.md"
        
        # Create agent-specific session
        session_file = self.agent_sessions_dir / "current" / session_name
        
        # Initial content
        content = f"""# Session: {description or 'development'}
**Started:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Agent:** {self.agent_id}
**Status:** Active

## Summary
New session started by agent {self.agent_id}.

## Tools Used

## Files Modified

## Key Decisions

## Notes

---

### Activity Log
"""
        
        # Write session file
        session_file.write_text(content, encoding='utf-8')
        
        # Update agent state
        self._update_agent_state({
            "current_session": session_name,
            "session_created": timestamp,
            "description": description
        })
        
        # Update global registry with lock
        with self.distributed_lock("registry"):
            self._update_global_registry("create", session_name, description)
        
        return session_name
    
    def archive_session(self, session_name: Optional[str] = None) -> bool:
        """Archive a session with agent awareness"""
        if not session_name:
            # Get current session from agent state
            state = self._load_agent_state()
            session_name = state.get("current_session")
        
        if not session_name:
            return False
        
        current_path = self.agent_sessions_dir / "current" / session_name
        if not current_path.exists():
            return False
        
        # Archive the session
        archive_path = self.agent_sessions_dir / "archived" / session_name
        shutil.move(str(current_path), str(archive_path))
        
        # Update agent state
        self._update_agent_state({
            "current_session": None,
            "last_archived": session_name,
            "archived_at": datetime.now().isoformat()
        })
        
        # Update global registry
        with self.distributed_lock("registry"):
            self._update_global_registry("archive", session_name)
        
        return True
    
    def get_session_status(self) -> Dict[str, Any]:
        """Get current session status for this agent"""
        state = self._load_agent_state()
        current = state.get("current_session")
        
        status = {
            "agent_id": self.agent_id,
            "current_session": current,
            "has_active": bool(current)
        }
        
        if current:
            session_file = self.agent_sessions_dir / "current" / current
            if session_file.exists():
                # Get session age
                created = state.get("session_created")
                if created:
                    created_dt = datetime.strptime(created[:19], '%Y-%m-%d-%H%M%S')
                    age_hours = (datetime.now() - created_dt).total_seconds() / 3600
                    status["age_hours"] = age_hours
                    status["timeout_in"] = max(0, 4.0 - age_hours)
                
                # Get session size
                status["size_kb"] = session_file.stat().st_size / 1024
        
        return status
    
    def list_all_sessions(self) -> Dict[str, List[Dict[str, Any]]]:
        """List sessions from all agents"""
        sessions = {
            "current": [],
            "archived": []
        }
        
        # Read global registry
        with self.distributed_lock("registry"):
            registry = self._load_global_registry()
        
        # Get active sessions
        for agent_id, session_info in registry.get("active_sessions", {}).items():
            sessions["current"].append({
                "agent_id": agent_id,
                "session": session_info.get("file", "").split("/")[-1],
                "started": session_info.get("started"),
                "description": session_info.get("description", "")
            })
        
        # Get recent archived sessions
        archived = registry.get("archived_sessions", [])[-20:]  # Last 20
        for session_info in archived:
            sessions["archived"].append({
                "agent_id": session_info.get("agent_id"),
                "session": session_info.get("file", "").split("/")[-1],
                "archived_at": session_info.get("archived_at", "")
            })
        
        return sessions
    
    def _load_agent_state(self) -> Dict[str, Any]:
        """Load agent-specific state"""
        if self.agent_state_file.exists():
            try:
                with open(self.agent_state_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {}
    
    def _update_agent_state(self, updates: Dict[str, Any]):
        """Update agent-specific state"""
        state = self._load_agent_state()
        state.update(updates)
        state["last_updated"] = datetime.now().isoformat()
        
        with open(self.agent_state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _load_global_registry(self) -> Dict[str, Any]:
        """Load global session registry"""
        if self.global_registry_file.exists():
            try:
                with open(self.global_registry_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "active_sessions": {},
            "archived_sessions": [],
            "total_sessions": 0
        }
    
    def _update_global_registry(self, action: str, session_name: str, description: str = ""):
        """Update global registry (must be called within lock)"""
        registry = self._load_global_registry()
        
        if action == "create":
            registry["active_sessions"][self.agent_id] = {
                "file": str(self.agent_sessions_dir / "current" / session_name),
                "started": datetime.now().isoformat(),
                "description": description
            }
            registry["total_sessions"] = registry.get("total_sessions", 0) + 1
            
        elif action == "archive":
            if self.agent_id in registry["active_sessions"]:
                session_info = registry["active_sessions"].pop(self.agent_id)
                session_info["archived_at"] = datetime.now().isoformat()
                session_info["agent_id"] = self.agent_id
                registry["archived_sessions"].append(session_info)
                
                # Keep only last 100 archived entries
                if len(registry["archived_sessions"]) > 100:
                    registry["archived_sessions"] = registry["archived_sessions"][-100:]
        
        # Save registry
        with open(self.global_registry_file, 'w') as f:
            json.dump(registry, f, indent=2)
    
    def cleanup_stale_agents(self):
        """Clean up stale agent data"""
        # This would be called periodically to clean up after crashed agents
        pass


def main():
    """Test multi-agent session manager"""
    agent_id = sys.argv[1] if len(sys.argv) > 1 else None
    manager = MultiAgentSessionManager(agent_id)
    
    print(f"Agent ID: {manager.agent_id}")
    print(f"Status: {json.dumps(manager.get_session_status(), indent=2)}")


if __name__ == "__main__":
    main()