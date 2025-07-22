#!/usr/bin/env python3
"""
State Manager for Code Reuse System
Handles loading, saving, and managing state files with atomic updates and migrations
"""

import json
import os
import shutil
import threading
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List, Callable
try:
    import fcntl
    HAS_FCNTL = True
except ImportError:
    HAS_FCNTL = False
import tempfile


class StateManager:
    """Manages state files for the code reuse system with thread-safe operations"""
    
    def __init__(self, state_dir: Optional[str] = None):
        """Initialize state manager with state directory"""
        if state_dir is None:
            state_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.state_dir = Path(state_dir)
        self.state_files = {
            'code_reuse_state': self.state_dir / 'code_reuse_state.json',
            'reuse_patterns': self.state_dir / 'reuse_patterns.json',
            'compliance_rules': self.state_dir / 'compliance_rules.json'
        }
        
        # Thread locks for each state file
        self._locks = {
            name: threading.Lock() for name in self.state_files
        }
        
        # In-memory cache
        self._cache = {}
        self._cache_timestamps = {}
        
        # Migration handlers
        self._migration_handlers = {
            '1.0.0': self._no_migration,
            '1.1.0': self._migrate_1_0_to_1_1,
            '2.0.0': self._migrate_1_1_to_2_0
        }
        
        # Initialize state files if they don't exist
        self._ensure_state_files_exist()
    
    def _ensure_state_files_exist(self):
        """Ensure all state files exist with proper defaults"""
        for name, path in self.state_files.items():
            if not path.exists():
                print(f"Warning: {name} not found at {path}")
    
    def load_state(self, state_name: str, use_cache: bool = True) -> Dict[str, Any]:
        """
        Load state from file with caching support
        
        Args:
            state_name: Name of the state file to load
            use_cache: Whether to use cached data if available
            
        Returns:
            State data as dictionary
        """
        if state_name not in self.state_files:
            raise ValueError(f"Unknown state file: {state_name}")
        
        # Check cache first
        if use_cache and state_name in self._cache:
            file_mtime = self.state_files[state_name].stat().st_mtime
            if file_mtime <= self._cache_timestamps.get(state_name, 0):
                return self._cache[state_name].copy()
        
        with self._locks[state_name]:
            try:
                with open(self.state_files[state_name], 'r') as f:
                    # Use file locking for read if available
                    if HAS_FCNTL:
                        try:
                            fcntl.flock(f.fileno(), fcntl.LOCK_SH)
                            data = json.load(f)
                            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                        except IOError:
                            # Fallback if locking fails
                            data = json.load(f)
                    else:
                        data = json.load(f)
                
                # Update cache
                self._cache[state_name] = data
                self._cache_timestamps[state_name] = time.time()
                
                # Check for migrations
                self._check_and_migrate(state_name, data)
                
                return data
                
            except FileNotFoundError:
                print(f"State file not found: {state_name}")
                return {}
            except json.JSONDecodeError as e:
                print(f"Error decoding {state_name}: {e}")
                # Try to recover from backup
                return self._recover_from_backup(state_name)
    
    def save_state(self, state_name: str, data: Dict[str, Any], atomic: bool = True):
        """
        Save state to file with atomic write support
        
        Args:
            state_name: Name of the state file to save
            data: State data to save
            atomic: Whether to use atomic write (recommended)
        """
        if state_name not in self.state_files:
            raise ValueError(f"Unknown state file: {state_name}")
        
        with self._locks[state_name]:
            # Update metadata
            data['last_updated'] = datetime.now().isoformat()
            
            if atomic:
                self._atomic_write(self.state_files[state_name], data)
            else:
                with open(self.state_files[state_name], 'w') as f:
                    json.dump(data, f, indent=2)
            
            # Update cache
            self._cache[state_name] = data
            self._cache_timestamps[state_name] = time.time()
            
            # Create backup
            self._create_backup(state_name)
    
    def _atomic_write(self, filepath: Path, data: Dict[str, Any]):
        """Perform atomic write using temporary file and rename"""
        temp_fd, temp_path = tempfile.mkstemp(
            dir=filepath.parent,
            prefix=f'.{filepath.stem}.',
            suffix='.tmp'
        )
        
        try:
            with os.fdopen(temp_fd, 'w') as f:
                json.dump(data, f, indent=2)
                f.flush()
                os.fsync(f.fileno())
            
            # Atomic rename
            os.replace(temp_path, filepath)
            
        except Exception:
            # Clean up temp file on error
            if os.path.exists(temp_path):
                os.unlink(temp_path)
            raise
    
    def update_state(self, state_name: str, update_func: Callable[[Dict[str, Any]], Dict[str, Any]]):
        """
        Update state using a function with automatic load/save
        
        Args:
            state_name: Name of the state file to update
            update_func: Function that takes current state and returns updated state
        """
        with self._locks[state_name]:
            current_state = self.load_state(state_name, use_cache=False)
            updated_state = update_func(current_state)
            self.save_state(state_name, updated_state)
    
    def update_nested(self, state_name: str, path: List[str], value: Any):
        """
        Update a nested value in state
        
        Args:
            state_name: Name of the state file
            path: List of keys to traverse (e.g., ['statistics', 'files_analyzed'])
            value: New value to set
        """
        def updater(state):
            current = state
            for key in path[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            current[path[-1]] = value
            return state
        
        self.update_state(state_name, updater)
    
    def increment_counter(self, state_name: str, counter_path: List[str], amount: int = 1):
        """Increment a numeric counter in state"""
        def incrementer(state):
            current = state
            for key in counter_path[:-1]:
                current = current.get(key, {})
            
            current_value = current.get(counter_path[-1], 0)
            current[counter_path[-1]] = current_value + amount
            return state
        
        self.update_state(state_name, incrementer)
    
    def append_to_list(self, state_name: str, list_path: List[str], item: Any, max_items: int = 100):
        """Append item to a list in state with size limit"""
        def appender(state):
            current = state
            for key in list_path[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            
            if list_path[-1] not in current:
                current[list_path[-1]] = []
            
            current[list_path[-1]].append(item)
            
            # Trim to max size
            if len(current[list_path[-1]]) > max_items:
                current[list_path[-1]] = current[list_path[-1]][-max_items:]
            
            return state
        
        self.update_state(state_name, appender)
    
    def _create_backup(self, state_name: str):
        """Create backup of state file"""
        backup_dir = self.state_dir / 'backups'
        backup_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = backup_dir / f"{state_name}_{timestamp}.json"
        
        try:
            shutil.copy2(self.state_files[state_name], backup_path)
            
            # Clean old backups (keep last 10)
            backups = sorted(backup_dir.glob(f"{state_name}_*.json"))
            for old_backup in backups[:-10]:
                old_backup.unlink()
                
        except Exception as e:
            print(f"Failed to create backup: {e}")
    
    def _recover_from_backup(self, state_name: str) -> Dict[str, Any]:
        """Attempt to recover state from latest backup"""
        backup_dir = self.state_dir / 'backups'
        backups = sorted(backup_dir.glob(f"{state_name}_*.json"))
        
        if backups:
            latest_backup = backups[-1]
            try:
                with open(latest_backup, 'r') as f:
                    print(f"Recovering {state_name} from backup: {latest_backup}")
                    return json.load(f)
            except Exception as e:
                print(f"Failed to recover from backup: {e}")
        
        return {}
    
    def _check_and_migrate(self, state_name: str, data: Dict[str, Any]):
        """Check if state needs migration and apply if necessary"""
        current_version = data.get('version', '1.0.0')
        latest_version = '1.0.0'  # Update this as versions change
        
        if current_version != latest_version:
            print(f"Migrating {state_name} from {current_version} to {latest_version}")
            # Apply migrations sequentially
            # This is a placeholder - implement actual migration logic
            data['version'] = latest_version
            self.save_state(state_name, data)
    
    def _no_migration(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """No migration needed"""
        return data
    
    def _migrate_1_0_to_1_1(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Migrate from version 1.0.0 to 1.1.0"""
        # Example migration logic
        if 'new_field' not in data:
            data['new_field'] = 'default_value'
        return data
    
    def _migrate_1_1_to_2_0(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Migrate from version 1.1.0 to 2.0.0"""
        # Example migration logic
        # Restructure data, rename fields, etc.
        return data
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get current statistics from code reuse state"""
        state = self.load_state('code_reuse_state')
        return state.get('statistics', {})
    
    def get_feature_flags(self) -> Dict[str, bool]:
        """Get current feature flags"""
        state = self.load_state('code_reuse_state')
        return state.get('feature_flags', {})
    
    def set_feature_flag(self, flag_name: str, value: bool):
        """Set a feature flag value"""
        self.update_nested('code_reuse_state', ['feature_flags', flag_name], value)
    
    def get_compliance_rules(self) -> Dict[str, Any]:
        """Get current compliance rules"""
        return self.load_state('compliance_rules')
    
    def get_discovered_patterns(self) -> Dict[str, List[Any]]:
        """Get discovered patterns"""
        state = self.load_state('reuse_patterns')
        return state.get('discovered_patterns', {})
    
    def clear_cache(self):
        """Clear in-memory cache"""
        self._cache.clear()
        self._cache_timestamps.clear()
    
    def export_state(self, output_dir: str):
        """Export all state files to a directory"""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        for name, filepath in self.state_files.items():
            if filepath.exists():
                output_file = output_path / f"{name}_{timestamp}.json"
                shutil.copy2(filepath, output_file)
        
        print(f"State exported to {output_path}")
    
    def get_state_info(self) -> Dict[str, Any]:
        """Get information about all state files"""
        info = {}
        
        for name, filepath in self.state_files.items():
            if filepath.exists():
                stat = filepath.stat()
                state = self.load_state(name)
                
                info[name] = {
                    'path': str(filepath),
                    'size_bytes': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'version': state.get('version', 'unknown'),
                    'last_updated': state.get('last_updated', 'unknown')
                }
            else:
                info[name] = {
                    'path': str(filepath),
                    'status': 'not_found'
                }
        
        return info


# Singleton instance for easy import
_state_manager = None

def get_state_manager() -> StateManager:
    """Get singleton StateManager instance"""
    global _state_manager
    if _state_manager is None:
        _state_manager = StateManager()
    return _state_manager


if __name__ == "__main__":
    # Test the state manager
    manager = get_state_manager()
    
    print("State Manager Test")
    print("-" * 50)
    
    # Display state info
    info = manager.get_state_info()
    for name, details in info.items():
        print(f"\n{name}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    
    # Test basic operations
    print("\n\nTesting operations...")
    
    # Test increment
    manager.increment_counter('code_reuse_state', ['statistics', 'files_analyzed'])
    stats = manager.get_statistics()
    print(f"Files analyzed: {stats.get('files_analyzed', 0)}")
    
    # Test feature flags
    flags = manager.get_feature_flags()
    print(f"Feature flags: {flags}")
    
    # Test compliance rules
    rules = manager.get_compliance_rules()
    print(f"Severity levels: {list(rules.get('severity_levels', {}).keys())}")