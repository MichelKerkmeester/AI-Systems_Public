#!/usr/bin/env python3
"""
Settings management utilities for Claude hooks
Handles loading, merging, and saving JSON configuration files
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class SettingsManager:
    """Manages settings for hooks with defaults and persistence"""
    
    def __init__(self, settings_path: Path, defaults: Dict[str, Any]):
        """
        Initialize settings manager
        
        Args:
            settings_path: Path to settings JSON file
            defaults: Default settings dictionary
        """
        self.settings_path = settings_path
        self.defaults = defaults
        self._settings = None
    
    @property
    def settings(self) -> Dict[str, Any]:
        """Lazy load settings with defaults"""
        if self._settings is None:
            self._settings = self.load()
        return self._settings
    
    def load(self) -> Dict[str, Any]:
        """Load settings from file, merging with defaults"""
        if self.settings_path.exists():
            try:
                with open(self.settings_path, 'r', encoding='utf-8') as f:
                    file_settings = json.load(f)
                    # Merge with defaults (file settings override defaults)
                    return {**self.defaults, **file_settings}
            except (json.JSONDecodeError, IOError):
                # Fall back to defaults on error
                pass
        
        return self.defaults.copy()
    
    def save(self, settings: Optional[Dict[str, Any]] = None):
        """
        Save settings to file
        
        Args:
            settings: Settings to save (uses current if None)
        """
        if settings is None:
            settings = self._settings or self.defaults
        
        # Ensure directory exists
        os.makedirs(self.settings_path.parent, exist_ok=True)
        
        # Write settings
        with open(self.settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value with optional default"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a setting value"""
        self.settings[key] = value
    
    def update(self, updates: Dict[str, Any]):
        """Update multiple settings"""
        self.settings.update(updates)
    
    def reload(self):
        """Reload settings from file"""
        self._settings = None
        return self.settings


class StateManager:
    """Manages persistent state for hooks"""
    
    def __init__(self, state_path: Path, default_state: Dict[str, Any]):
        """
        Initialize state manager
        
        Args:
            state_path: Path to state JSON file
            default_state: Default state dictionary
        """
        self.state_path = state_path
        self.default_state = default_state
        self._state = None
    
    @property
    def state(self) -> Dict[str, Any]:
        """Get current state"""
        if self._state is None:
            self._state = self.load()
        return self._state
    
    def load(self) -> Dict[str, Any]:
        """Load state from file or return defaults"""
        if self.state_path.exists():
            try:
                with open(self.state_path, 'r', encoding='utf-8') as f:
                    file_state = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return {**self.default_state, **file_state}
            except (json.JSONDecodeError, IOError):
                pass
        
        return self.default_state.copy()
    
    def save(self, state: Optional[Dict[str, Any]] = None):
        """Save state to file"""
        if state is None:
            state = self._state or self.default_state
        
        # Ensure directory exists
        os.makedirs(self.state_path.parent, exist_ok=True)
        
        # Write state
        with open(self.state_path, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2)
        
        self._state = state
    
    def update(self, updates: Dict[str, Any]):
        """Update state and save"""
        self.state.update(updates)
        self.save()
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get state value"""
        return self.state.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set state value and save"""
        self.state[key] = value
        self.save()
    
    def increment(self, key: str, amount: int = 1):
        """Increment a numeric state value"""
        current = self.get(key, 0)
        self.set(key, current + amount)
    
    def reset(self):
        """Reset state to defaults"""
        self._state = self.default_state.copy()
        self.save()