"""
Process-Aware Hook Manager for Claude Code
Integrates with DesktopCommanderMCP for real-time monitoring
"""

import asyncio
import json
import time
import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass
import subprocess
import sys

# Import our priority system
from .hook_priority import HookPriorityManager, HookExecution, HookMetadata


class ProcessAwareHookManager:
    """
    Manages hook execution with process monitoring via DesktopCommanderMCP
    """
    
    def __init__(self, agent_id: Optional[str] = None):
        self.agent_id = agent_id or "main"
        self.priority_manager = HookPriorityManager(agent_id)
        self.process_sessions: Dict[str, str] = {}  # hook_id -> session_id
        self.hook_cache: Dict[str, Any] = {}  # Cache for hook results
        self.performance_log: List[Dict[str, Any]] = []
        
        # Paths
        self.claude_path = Path.home() / "AI & Dev" / "Websites" / "• anobel.nl" / ".claude"
        self.hooks_dir = self.claude_path / "logic" / "hooks"
        
        # Desktop Commander interface (will be initialized when available)
        self.desktop_commander = None
        self._init_desktop_commander()
    
    def _init_desktop_commander(self):
        """Initialize Desktop Commander interface when available"""
        try:
            # This will be available after Claude Desktop restart
            # For now, we'll use subprocess as fallback
            self.desktop_commander = None
        except:
            pass
    
    async def trigger_hooks(self, event_type: str, context: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Trigger hooks for a specific event type with priority management
        
        Args:
            event_type: Type of event (UserPromptSubmit, PreToolUse, PostToolUse)
            context: Event context data
            
        Returns:
            List of hook execution results
        """
        start_time = time.time()
        results = []
        
        # Add agent context
        context['agent_id'] = self.agent_id
        context['event_type'] = event_type
        
        # Get applicable hooks from settings
        applicable_hooks = self._get_applicable_hooks(event_type, context)
        
        # Deduplicate hooks
        hook_names = self.priority_manager.deduplicate_hooks(applicable_hooks, context)
        
        # Queue hooks by priority
        executions = []
        for hook_name in hook_names:
            execution = self.priority_manager.queue_hook(hook_name, context)
            if execution:
                executions.append(execution)
        
        # Execute hooks in priority order
        tasks = []
        while True:
            execution = self.priority_manager.get_next_hook()
            if not execution:
                break
            
            # Check if we can execute concurrently
            config = self.priority_manager.hook_configs.get(
                execution.hook_name,
                HookMetadata(name=execution.hook_name, priority=99)
            )
            
            if config.concurrent_safe and config not in tasks:
                # Execute asynchronously
                task = asyncio.create_task(
                    self._execute_hook_with_monitoring(execution)
                )
                tasks.append(task)
            else:
                # Execute synchronously and wait
                result = await self._execute_hook_with_monitoring(execution)
                results.append(result)
        
        # Wait for async tasks
        if tasks:
            async_results = await asyncio.gather(*tasks, return_exceptions=True)
            results.extend([r for r in async_results if not isinstance(r, Exception)])
        
        # Log performance
        total_time = (time.time() - start_time) * 1000  # Convert to ms
        self._log_performance(event_type, len(hook_names), total_time)
        
        return results
    
    async def _execute_hook_with_monitoring(self, execution: HookExecution) -> Dict[str, Any]:
        """Execute a hook with process monitoring"""
        start_time = time.time()
        hook_path = self._find_hook_path(execution.hook_name)
        
        if not hook_path:
            return {
                "hook": execution.hook_name,
                "status": "error",
                "error": f"Hook not found: {execution.hook_name}"
            }
        
        # Mark as executing
        self.priority_manager.mark_executing(execution)
        
        try:
            # Execute hook
            if self.desktop_commander:
                # Use Desktop Commander for process monitoring
                result = await self._execute_with_desktop_commander(
                    hook_path, execution.context
                )
            else:
                # Fallback to subprocess
                result = await self._execute_with_subprocess(
                    hook_path, execution.context
                )
            
            # Cache result if successful
            if result.get("exit_code") == 0:
                self.hook_cache[execution.hook_name] = result
            
            # Mark completed
            execution_time = (time.time() - start_time) * 1000
            self.priority_manager.mark_completed(
                execution, result, execution_time
            )
            
            return {
                "hook": execution.hook_name,
                "status": "success",
                "execution_time_ms": execution_time,
                "result": result
            }
            
        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            self.priority_manager.mark_completed(execution, None, execution_time)
            
            return {
                "hook": execution.hook_name,
                "status": "error",
                "execution_time_ms": execution_time,
                "error": str(e)
            }
    
    async def _execute_with_desktop_commander(self, hook_path: Path, 
                                            context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute hook using Desktop Commander for monitoring"""
        # This will be implemented when Desktop Commander is available
        # For now, fall back to subprocess
        return await self._execute_with_subprocess(hook_path, context)
    
    async def _execute_with_subprocess(self, hook_path: Path, 
                                      context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute hook using subprocess (fallback)"""
        try:
            # Prepare hook input
            hook_input = json.dumps(context)
            
            # Execute hook
            process = await asyncio.create_subprocess_exec(
                sys.executable,
                str(hook_path),
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Send input and get output
            stdout, stderr = await process.communicate(input=hook_input.encode())
            
            # Parse result
            exit_code = process.returncode
            output = stdout.decode() if stdout else ""
            error = stderr.decode() if stderr else ""
            
            return {
                "exit_code": exit_code,
                "output": output,
                "error": error
            }
            
        except Exception as e:
            return {
                "exit_code": -1,
                "output": "",
                "error": str(e)
            }
    
    def _get_applicable_hooks(self, event_type: str, context: Dict[str, Any]) -> List[str]:
        """Get hooks that should run for this event"""
        # Load settings
        settings_path = self.claude_path / "settings.json"
        if not settings_path.exists():
            return []
        
        try:
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            
            hooks = []
            hook_configs = settings.get("hooks", {}).get(event_type, [])
            
            for config in hook_configs:
                # Check matcher if present
                if "matcher" in config and config["matcher"]:
                    tool_name = context.get("toolName", "")
                    if not any(m in tool_name for m in config["matcher"].split("|")):
                        continue
                
                # Add hooks from this config
                for hook in config.get("hooks", []):
                    if hook.get("type") == "command":
                        # Extract hook name from command
                        command = hook.get("command", "")
                        if "hooks/" in command and ".py" in command:
                            hook_name = Path(command).stem
                            hooks.append(hook_name)
            
            return hooks
            
        except Exception as e:
            print(f"Error loading hooks: {e}")
            return []
    
    def _find_hook_path(self, hook_name: str) -> Optional[Path]:
        """Find the path to a hook file"""
        # Search in all hook directories
        search_dirs = [
            self.claude_path / "logic" / "quality" / "hooks",
            self.claude_path / "logic" / "memory" / "hooks",
            self.claude_path / "logic" / "mode" / "hooks",
            self.claude_path / "logic" / "session" / "hooks",
            self.claude_path / "logic" / "workflow" / "hooks",
            self.claude_path / "logic" / "security" / "hooks",
            self.claude_path / "logic" / "context" / "hooks",
            self.claude_path / "logic" / "notebook" / "hooks",
            self.hooks_dir  # New centralized hooks directory
        ]
        
        for dir_path in search_dirs:
            if dir_path.exists():
                hook_path = dir_path / f"{hook_name}.py"
                if hook_path.exists():
                    return hook_path
        
        return None
    
    def _log_performance(self, event_type: str, hook_count: int, total_time: float):
        """Log performance metrics"""
        log_entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "hook_count": hook_count,
            "total_time_ms": total_time,
            "agent_id": self.agent_id
        }
        
        self.performance_log.append(log_entry)
        
        # Keep only last 1000 entries
        if len(self.performance_log) > 1000:
            self.performance_log = self.performance_log[-1000:]
        
        # Warn if exceeding performance target
        if total_time > 300:  # 300ms target
            print(f"⚠️ Hook execution exceeded 300ms target: {total_time:.1f}ms")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current hook manager status"""
        return {
            "agent_id": self.agent_id,
            "hook_status": self.priority_manager.get_hook_status(),
            "cache_entries": len(self.hook_cache),
            "performance": {
                "recent_executions": len(self.performance_log),
                "avg_time_ms": sum(e["total_time_ms"] for e in self.performance_log[-10:]) / min(10, len(self.performance_log)) if self.performance_log else 0
            }
        }
    
    def clear_cache(self):
        """Clear all caches"""
        self.hook_cache.clear()
        self.priority_manager.clear_cache()
    
    def adjust_hook_priority(self, hook_name: str, new_priority: int):
        """Adjust hook priority dynamically"""
        self.priority_manager.adjust_priority(hook_name, new_priority)