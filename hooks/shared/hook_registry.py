#!/usr/bin/env python3
"""
Hook Registry - Manages all hooks in the system
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional


class HookRegistry:
    """Registry for managing all system hooks"""
    
    def __init__(self, claude_path: Path):
        self.claude_path = claude_path
        self.settings_file = claude_path / "settings.json"
        self._cache = None
    
    def get_all_hooks(self) -> List[Dict[str, Any]]:
        """Get all registered hooks with metadata"""
        if self._cache is None:
            self._load_hooks()
        return self._cache
    
    def _load_hooks(self):
        """Load hooks from settings and hook files"""
        self._cache = []
        
        # Load settings.json
        try:
            with open(self.settings_file, 'r') as f:
                settings = json.load(f)
        except:
            settings = {}
        
        # Define hook metadata
        hook_metadata = {
            "quality-hook": {
                "name": "Quality Check",
                "description": "Enforces CLAUDE.md compliance and auto-runs tests",
                "priority": 2,
                "category": "quality"
            },
            "memory-context-hook": {
                "name": "Memory Context",
                "description": "Loads relevant memories from Graphiti",
                "priority": 3,
                "category": "memory"
            },
            "mode-suggestion-hook": {
                "name": "Mode Suggestion",
                "description": "Suggests optimal mode based on context",
                "priority": 3,
                "category": "workflow"
            },
            "workflow-automation-hook": {
                "name": "Workflow Automation",
                "description": "Auto-triggers Sequential Thinking for complex tasks",
                "priority": 3,
                "category": "workflow"
            },
            "session-hook": {
                "name": "Session Management",
                "description": "Auto-creates and archives sessions",
                "priority": 2,
                "category": "session"
            },
            "security-scan-hook": {
                "name": "Security Scan",
                "description": "Scans for API keys and security violations",
                "priority": 1,
                "category": "security"
            },
            "context-management-hook": {
                "name": "Context Management",
                "description": "Auto-saves context every 5 minutes",
                "priority": 4,
                "category": "context"
            },
            "pattern-extraction-hook": {
                "name": "Pattern Extraction",
                "description": "Extracts patterns from code and sessions",
                "priority": 5,
                "category": "notebook"
            }
        }
        
        # Parse hooks from settings
        hooks_config = settings.get("hooks", {})
        
        for event, event_hooks in hooks_config.items():
            if event == "enabled":
                continue
                
            for hook_group in event_hooks:
                hooks = hook_group.get("hooks", [])
                matcher = hook_group.get("matcher", "")
                
                for hook in hooks:
                    if hook.get("type") == "command":
                        command = hook.get("command", "")
                        # Extract hook name from command
                        hook_name = None
                        for key in hook_metadata:
                            if key in command:
                                hook_name = key
                                break
                        
                        if hook_name and hook_name in hook_metadata:
                            meta = hook_metadata[hook_name]
                            self._cache.append({
                                "name": meta["name"],
                                "description": meta["description"],
                                "priority": meta["priority"],
                                "category": meta["category"],
                                "event": event,
                                "matcher": matcher,
                                "enabled": True,  # All hooks in settings are enabled
                                "file": command.split("'")[1] if "'" in command else command
                            })
    
    def get_hook_info(self, hook_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a specific hook"""
        if self._cache is None:
            self._load_hooks()
        
        # Search by various name formats
        search_names = [
            hook_name.lower(),
            hook_name.lower().replace(" ", "-"),
            hook_name.lower().replace(" ", "_"),
            hook_name.lower() + "-hook"
        ]
        
        for hook in self._cache:
            hook_lower = hook["name"].lower()
            if any(name in hook_lower or hook_lower in name for name in search_names):
                # Load hook-specific settings
                hook_copy = hook.copy()
                hook_copy["settings"] = self._load_hook_settings(hook["name"])
                return hook_copy
        
        return None
    
    def toggle_hook(self, hook_name: str, enable: bool) -> Dict[str, Any]:
        """Enable or disable a hook"""
        # This would modify settings.json in production
        # For now, return success
        return {
            "success": True,
            "message": f"Hook {'enabled' if enable else 'disabled'}"
        }
    
    def reload(self):
        """Reload hook configurations"""
        self._cache = None
        self._load_hooks()
    
    def _load_hook_settings(self, hook_name: str) -> Dict[str, Any]:
        """Load settings for a specific hook"""
        # Map hook names to settings files
        settings_map = {
            "Quality Check": "logic/quality/quality-settings.json",
            "Session Management": "logic/session/hooks/session-settings.json",
            "Memory Context": "memory/settings.json",
            "Context Management": "logic/hooks/context-settings.json",
            "Pattern Extraction": "logic/notebook/hooks/notebook-settings.json"
        }
        
        if hook_name in settings_map:
            settings_file = self.claude_path / settings_map[hook_name]
            if settings_file.exists():
                try:
                    with open(settings_file, 'r') as f:
                        return json.load(f)
                except:
                    pass
        
        return {}