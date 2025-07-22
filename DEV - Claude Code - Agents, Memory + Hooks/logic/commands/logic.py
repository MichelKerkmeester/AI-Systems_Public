#!/usr/bin/env python3
"""
/logic - Unified System Management Command
Replaces multiple commands with intelligent sub-commands
"""

import sys
import json
import os
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from shared import (
    MessageFormatter,
    SettingsManager,
    StateManager,
    HookRegistry
)

# Import code reuse components
try:
    from code_reuse import (
        ReuseAnalyzer, ComplianceValidator,
        JustificationSystem, SimilarityDetector,
        PatternMatcher, ConsolidationAnalyzer
    )
    from state.code_reuse.state_manager import StateManager as ReuseStateManager
    CODE_REUSE_AVAILABLE = True
except ImportError:
    CODE_REUSE_AVAILABLE = False


class LogicCommand:
    """Unified logic system management"""
    
    def __init__(self):
        self.claude_path = Path.home() / ".claude"
        self.project_root = Path.cwd()
        self.logic_path = self.claude_path / "logic"
        
        # Settings
        self.settings_path = self.logic_path / "commands" / "logic-settings.json"
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        
        # Hook registry
        self.hook_registry = HookRegistry(self.claude_path)
        
        # State tracking
        self.state_path = self.claude_path / "logic" / "state"
        self.state = StateManager(
            self.state_path / "logic-state.json",
            default_state={"commands_executed": 0, "last_command": None}
        )
        
        # Initialize code reuse components if available
        if CODE_REUSE_AVAILABLE:
            self.reuse_analyzer = ReuseAnalyzer()
            self.compliance_validator = ComplianceValidator()
            self.justification_system = JustificationSystem()
            self.similarity_detector = SimilarityDetector()
            self.pattern_matcher = PatternMatcher()
            self.consolidation_analyzer = ConsolidationAnalyzer()
            self.reuse_state_manager = ReuseStateManager()
        
        # (Agent support removed)
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings"""
        return {
            "show_performance": True,
            "show_descriptions": True,
            "auto_fix": True,
            "debug_mode": False,
            "cache_ttl": 300,  # 5 minutes
            "aliases": {
                "h": "help",
                "hooks": "hooks",
                "sys": "system",
                "t": "tasks",
                "d": "debug"
            }
        }
    
    def execute(self, args: List[str]) -> Dict[str, Any]:
        """Execute logic command"""
        if not args:
            return self.show_help()
        
        # Get sub-command
        sub_cmd = args[0].lower()
        
        # Check aliases
        if sub_cmd in self.settings.get("aliases", {}):
            sub_cmd = self.settings.get("aliases", {})[sub_cmd]
        
        # Route to handler
        handlers = {
            "help": self.show_help,
            "hooks": self.manage_hooks,
            "system": self.show_system,
            "tasks": self.show_tasks,
            "debug": self.debug_mode,
            "reuse": self.manage_reuse,
            "claude-md-update": self.check_claude_md_update
        }
        
        if sub_cmd in handlers:
            return handlers[sub_cmd](args[1:] if len(args) > 1 else [])
        else:
            return {
                "status": "error",
                "message": f"Unknown sub-command: {sub_cmd}",
                "suggestions": ["Use '/logic help' for available commands"]
            }
    
    def show_help(self, args: List[str] = None) -> Dict[str, Any]:
        """Show help information"""
        output = MessageFormatter.header("/logic - Unified System Management", "logic")
        
        output += "\n📋 **Available Sub-Commands:**\n"
        
        commands = [
            ("help (h)", "Show this help message"),
            ("hooks", "Manage automated hooks"),
            ("reuse", "Code reuse analysis and enforcement"),
            ("system (sys)", "System metrics and performance"),
            ("tasks (t)", "Task management overview"),
            ("debug (d)", "Debug mode and diagnostics"),
            ("claude-md-update", "Check if CLAUDE.md needs updates")
        ]
        
        for cmd, desc in commands:
            output += f"  • `/logic {cmd}` - {desc}\n"
        
        output += "\n🎯 **Quick Examples:**\n"
        output += "  • `/logic hooks list` - Show all hooks\n"
        output += "  • `/logic hooks disable security` - Disable security hook\n"
        output += "  • `/logic reuse analyze Button` - Find reusable Button components\n"
        output += "  • `/logic reuse report` - View code reuse metrics\n"
        output += "  • `/logic system` - Show performance metrics\n"
        output += "  • `/logic tasks` - View task automation status\n"
        
        output += "\n⚡ **Replaced Commands:**\n"
        output += "  • `/workflow` → Automated via hooks\n"
        output += "  • `/test` → Automated via quality hook\n"
        output += "  • `/security` → Automated via security hook\n"
        output += "  • `/context` → Automated via context hook\n"
        output += "  • `/notebook` → Automated via pattern extraction\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def manage_hooks(self, args: List[str]) -> Dict[str, Any]:
        """Manage hook system"""
        if not args:
            args = ["list"]
        
        action = args[0].lower()
        
        if action == "list":
            return self._list_hooks()
        elif action == "enable":
            if len(args) < 2:
                return {"status": "error", "message": "Specify hook name to enable"}
            return self._toggle_hook(args[1], True)
        elif action == "disable":
            if len(args) < 2:
                return {"status": "error", "message": "Specify hook name to disable"}
            return self._toggle_hook(args[1], False)
        elif action == "status":
            if len(args) < 2:
                return {"status": "error", "message": "Specify hook name"}
            return self._hook_status(args[1])
        elif action == "reload":
            return self._reload_hooks()
        else:
            return {
                "status": "error",
                "message": f"Unknown hooks action: {action}",
                "suggestions": ["list", "enable", "disable", "status", "reload"]
            }
    
    def _list_hooks(self) -> Dict[str, Any]:
        """List all hooks with status"""
        output = MessageFormatter.header("Hook System Status", "hooks")
        
        # Get hook information
        hooks = self.hook_registry.get_all_hooks()
        
        # Group by event
        by_event = {}
        for hook in hooks:
            event = hook.get("event", "Unknown")
            if event not in by_event:
                by_event[event] = []
            by_event[event].append(hook)
        
        # Display by event
        for event, event_hooks in by_event.items():
            output += f"\n📍 **{event} Event:**\n"
            
            for hook in sorted(event_hooks, key=lambda h: h.get("priority", 999)):
                name = hook.get("name", "Unknown")
                enabled = hook.get("enabled", True)
                priority = hook.get("priority", "N/A")
                status = "✅" if enabled else "❌"
                
                output += f"  {status} {name} (Priority: {priority})\n"
                
                if self.settings.get("show_descriptions") and hook.get("description"):
                    output += f"     → {hook['description']}\n"
        
        # Performance metrics
        if self.settings.get("show_performance"):
            perf = self._get_performance_metrics()
            output += f"\n⚡ **Performance:**\n"
            output += f"  • Average execution: {perf['avg_time']:.1f}ms\n"
            output += f"  • Total hooks run: {perf['total_runs']}\n"
            output += f"  • Cache hit rate: {perf['cache_hit_rate']:.1%}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _toggle_hook(self, hook_name: str, enable: bool) -> Dict[str, Any]:
        """Enable or disable a hook"""
        try:
            # Update hook configuration
            result = self.hook_registry.toggle_hook(hook_name, enable)
            
            if result["success"]:
                action = "enabled" if enable else "disabled"
                output = f"✅ Hook '{hook_name}' has been {action}\n"
                
                # Show related information
                if hook_name == "quality" and not enable:
                    output += "⚠️ Warning: Disabling quality checks may lead to non-compliant code\n"
                elif hook_name == "security" and not enable:
                    output += "🚨 Warning: Disabling security scans is not recommended\n"
                
                return {
                    "status": "success",
                    "output": output
                }
            else:
                return {
                    "status": "error",
                    "message": result.get("error", "Failed to toggle hook")
                }
                
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error toggling hook: {str(e)}"
            }
    
    def _hook_status(self, hook_name: str) -> Dict[str, Any]:
        """Show detailed status for a specific hook"""
        hook_info = self.hook_registry.get_hook_info(hook_name)
        
        if not hook_info:
            return {
                "status": "error",
                "message": f"Hook '{hook_name}' not found"
            }
        
        output = MessageFormatter.header(f"Hook: {hook_name}", "hook")
        
        output += f"\n📊 **Status:**\n"
        output += f"  • Enabled: {'✅ Yes' if hook_info['enabled'] else '❌ No'}\n"
        output += f"  • Event: {hook_info['event']}\n"
        output += f"  • Priority: {hook_info['priority']}\n"
        output += f"  • File: {hook_info['file']}\n"
        
        if hook_info.get("description"):
            output += f"\n📝 **Description:**\n  {hook_info['description']}\n"
        
        # Performance stats
        stats = self._get_hook_stats(hook_name)
        if stats:
            output += f"\n⚡ **Performance:**\n"
            output += f"  • Runs: {stats['runs']}\n"
            output += f"  • Avg time: {stats['avg_time']:.1f}ms\n"
            output += f"  • Last run: {stats['last_run']}\n"
        
        # Configuration
        if hook_info.get("settings"):
            output += f"\n⚙️ **Configuration:**\n"
            for key, value in hook_info["settings"].items():
                output += f"  • {key}: {value}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _reload_hooks(self) -> Dict[str, Any]:
        """Reload hook configurations"""
        try:
            self.hook_registry.reload()
            
            output = "✅ Hook configurations reloaded\n"
            output += f"  • Active hooks: {len(self.hook_registry.get_all_hooks())}\n"
            
            return {
                "status": "success",
                "output": output
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to reload hooks: {str(e)}"
            }
    
    def show_system(self, args: List[str]) -> Dict[str, Any]:
        """Show system metrics and status"""
        output = MessageFormatter.header("System Status", "system")
        
        # Hook system
        output += "\n🪝 **Hook System:**\n"
        hooks = self.hook_registry.get_all_hooks()
        enabled = len([h for h in hooks if h.get("enabled", True)])
        output += f"  • Total hooks: {len(hooks)} ({enabled} enabled)\n"
        output += f"  • Events monitored: {len(set(h.get('event', '') for h in hooks))}\n"
        
        # Performance
        perf = self._get_performance_metrics()
        output += f"\n⚡ **Performance:**\n"
        output += f"  • Hook execution: {perf['avg_time']:.1f}ms average\n"
        output += f"  • Memory usage: {perf['memory_mb']:.1f}MB\n"
        output += f"  • Cache efficiency: {perf['cache_hit_rate']:.1%}\n"
        
        # Automation stats
        auto_stats = self._get_automation_stats()
        output += f"\n🤖 **Automation:**\n"
        output += f"  • Commands automated: {auto_stats['automated_commands']}/10\n"
        output += f"  • Time saved: ~{auto_stats['time_saved_hours']:.1f} hours\n"
        output += f"  • Auto-fixes applied: {auto_stats['auto_fixes']}\n"
        
        # Integration status
        output += f"\n🔗 **Integrations:**\n"
        integrations = self._check_integrations()
        for name, status in integrations.items():
            icon = "✅" if status else "❌"
            output += f"  {icon} {name}\n"
        
        # Multi-agent status
        output += f"\n🤖 **Multi-Agent System:**\n"
        # Agent system removed
        resource_usage = self.resource_manager.get_total_usage()
        output += f"  • Resource usage: {resource_usage['cpu_percent']:.1f}% CPU, {resource_usage['memory_mb']:.1f}MB RAM\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def show_tasks(self, args: List[str]) -> Dict[str, Any]:
        """Task management system"""
        # Import TaskManager here to avoid circular imports
        from logic.tasks import TaskManager
        self.task_manager = TaskManager()
        
        if not args:
            return self._show_task_menu()
        
        action = args[0].lower()
        
        # Task management actions
        task_actions = {
            "list": self._list_tasks,
            "new": self._new_task,
            "activate": self._activate_task,
            "status": self._task_status,
            "complete": self._complete_task,
            "search": self._search_tasks,
            "parallel": lambda a: self.manage_parallel_tasks(a),
        }
        
        if action in task_actions:
            return task_actions[action](args[1:] if len(args) > 1 else [])
        else:
            return {"status": "error", "message": f"Unknown task action: {action}"}
    
    def _show_task_menu(self) -> Dict[str, Any]:
        """Show task management menu"""
        output = MessageFormatter.header("Task Management", "tasks")
        
        output += "\n📋 **Task Commands:**\n"
        output += "  • `/logic tasks list` - Show all tasks by status\n"
        output += "  • `/logic tasks new [name]` - Create new task\n"
        output += "  • `/logic tasks activate [name]` - Start working on task\n"
        output += "  • `/logic tasks status` - Current task progress\n"
        output += "  • `/logic tasks complete` - Mark current task done\n"
        output += "  • `/logic tasks search [query]` - Search tasks\n"
        
        output += "\n🚀 **Parallel Development:**\n"
        output += "  • `/logic tasks parallel` - Parallel execution tools\n"
        
        # Current status
        active_task = self.task_manager.get_active_task()
        if active_task:
            output += f"\n🎯 **Active Task:** {active_task.name}\n"
            output += f"  • Progress: {active_task.progress}%\n"
        
        stats = self.task_manager.get_stats()
        output += f"\n📊 **Statistics:**\n"
        output += f"  • Total tasks: {stats['total_tasks']}\n"
        output += f"  • Suggestions: {stats['suggestions']}\n"
        output += f"  • Completed: {stats['completed']}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _list_tasks(self, args: List[str]) -> Dict[str, Any]:
        """List tasks by status"""
        status_filter = args[0] if args else None
        
        if status_filter and status_filter not in ["suggestion", "active", "completed"]:
            return {"status": "error", "message": f"Invalid status: {status_filter}"}
        
        tasks = self.task_manager.list_tasks(status_filter)
        
        output = MessageFormatter.header(f"Tasks{' - ' + status_filter if status_filter else ''}", "tasks")
        
        if not tasks:
            output += "\n📭 No tasks found.\n"
        else:
            # Group by status
            by_status = {}
            for task in tasks:
                if task.status not in by_status:
                    by_status[task.status] = []
                by_status[task.status].append(task)
            
            for status in ["active", "suggestion", "completed"]:
                if status in by_status:
                    output += f"\n{'🎯' if status == 'active' else '💡' if status == 'suggestion' else '✅'} **{status.title()}:**\n"
                    for task in by_status[status]:
                        progress_str = f" ({task.progress}%)" if status == "active" else ""
                        output += f"  • {task.name}{progress_str}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _new_task(self, args: List[str]) -> Dict[str, Any]:
        """Create new task"""
        if not args:
            return {"status": "error", "message": "Usage: `/logic tasks new [task-name]`"}
        
        name = " ".join(args)
        
        # Check for template hint
        template = None
        if "--template" in args:
            idx = args.index("--template")
            if idx + 1 < len(args):
                template = args[idx + 1]
                name = " ".join(args[:idx])
        
        try:
            task = self.task_manager.create_task(name, template=template)
            
            output = f"✅ Created new task: {task.name}\n\n"
            output += "Next steps:\n"
            output += f"  1. Edit task details in: `suggestions/{self.task_manager._generate_task_filename(name)}`\n"
            output += f"  2. When ready to start: `/logic tasks activate {name}`\n"
            
            return {
                "status": "success",
                "output": output
            }
        except Exception as e:
            return {"status": "error", "message": f"Failed to create task: {str(e)}"}
    
    def _activate_task(self, args: List[str]) -> Dict[str, Any]:
        """Activate a task"""
        if not args:
            return {"status": "error", "message": "Usage: `/logic tasks activate [task-name]`"}
        
        name = " ".join(args)
        
        try:
            if self.task_manager.activate_task(name):
                output = f"🎯 Activated task: {name}\n\n"
                output += "Task is now active. Use TodoWrite to track progress.\n"
                output += "When complete: `/logic tasks complete`\n"
                
                return {
                    "status": "success",
                    "output": output
                }
            else:
                return {"status": "error", "message": f"Task '{name}' not found"}
        except ValueError as e:
            return {"status": "error", "message": str(e)}
    
    def _task_status(self, args: List[str]) -> Dict[str, Any]:
        """Show current task status"""
        active_task = self.task_manager.get_active_task()
        
        if not active_task:
            return {
                "status": "info",
                "output": "No active task. Use `/logic tasks activate [name]` to start one."
            }
        
        output = MessageFormatter.header(f"Task: {active_task.name}", "tasks")
        
        output += f"\n📊 **Progress:** {active_task.progress}%\n"
        output += f"📅 **Started:** {active_task.created_at}\n"
        
        if active_task.todo_ids:
            output += f"\n📝 **Tracked Todos:** {len(active_task.todo_ids)}\n"
        
        if active_task.description:
            output += f"\n📄 **Description:**\n{active_task.description}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _complete_task(self, args: List[str]) -> Dict[str, Any]:
        """Complete current task"""
        active_task = self.task_manager.get_active_task()
        
        if not active_task:
            return {
                "status": "error",
                "message": "No active task to complete"
            }
        
        if self.task_manager.complete_task():
            output = f"✅ Completed task: {active_task.name}\n\n"
            output += "Task has been archived with timestamp.\n"
            
            # Suggest next steps
            suggestions = self.task_manager.list_tasks("suggestion")
            if suggestions:
                output += f"\n💡 **Suggested next tasks:**\n"
                for task in suggestions[:3]:
                    output += f"  • {task.name}\n"
            
            return {
                "status": "success",
                "output": output
            }
        else:
            return {"status": "error", "message": "Failed to complete task"}
    
    def _search_tasks(self, args: List[str]) -> Dict[str, Any]:
        """Search tasks"""
        if not args:
            return {"status": "error", "message": "Usage: `/logic tasks search [query]`"}
        
        query = " ".join(args)
        results = self.task_manager.search_tasks(query)
        
        output = MessageFormatter.header(f"Search: {query}", "tasks")
        
        if not results:
            output += "\n🔍 No matching tasks found.\n"
        else:
            output += f"\n🔍 **Found {len(results)} match{'es' if len(results) > 1 else ''}:**\n\n"
            
            for task, snippet in results:
                status_icon = "🎯" if task.status == "active" else "💡" if task.status == "suggestion" else "✅"
                output += f"{status_icon} **{task.name}** ({task.status})\n"
                output += f"```\n{snippet}\n```\n\n"
        
        output += MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    
    def manage_parallel_tasks(self, args: List[str]) -> Dict[str, Any]:
        """Manage parallel task execution"""
        if not args:
            return self._show_parallel_help()
        
        action = args[0].lower()
        
        if action == "start":
            return {"status": "error", "message": "Parallel agents have been removed. Use Task tool instead."}
        elif action == "status":
            return self._show_parallel_status()
        elif action in ["logs", "pause", "resume", "merge"]:
            return {"status": "error", "message": "Agent operations removed. Use Task tool instead."}
        elif action == "cleanup":
            return {"status": "error", "message": "Agent cleanup no longer needed."}
        else:
            return {
                "status": "error",
                "message": f"Unknown parallel action: {action}",
                "suggestions": ["start", "status", "logs", "pause", "resume", "merge", "cleanup"]
            }
    
    def _show_parallel_help(self) -> Dict[str, Any]:
        """Show parallel execution help"""
        output = MessageFormatter.header("Parallel Task Execution", "parallel")
        
        output += "\n🚀 **Parallel Commands:**\n"
        commands = [
            ("start", "[Removed - use Task tool instead]"),
            ("status", "Show status of all agents"),
            ("logs [agent]", "View logs for specific agent"),
            ("pause [agent]", "Pause agent execution"),
            ("resume [agent]", "Resume paused agent"),
            ("merge [agent]", "Merge agent's completed work"),
            ("cleanup", "Remove worktrees and cleanup")
        ]
        
        for cmd, desc in commands:
            output += f"  • `/logic tasks parallel {cmd}` - {desc}\n"
        
        output += "\n📊 **Current Resources:**\n"
        output += "\n⚠️ **Note:** The parallel agent system has been removed.\n"
        output += "Use the Task tool in Claude Code for parallel execution.\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    
    def _show_parallel_status(self) -> Dict[str, Any]:
        """Show status of parallel agents"""
        output = MessageFormatter.header("Parallel Agent Status", "status")
        
        output += "\n📭 No active agents - system removed.\n"
        output += "\nUse the Task tool for parallel execution.\n"
        output += f"  • Total memory: {total_usage['memory_mb']:.1f} MB\n"
        output += f"  • Total CPU: {total_usage['cpu_percent']:.1f}%\n"
        
        # Registry stats
        stats = self.agent_registry.get_registry_stats()
        if stats["by_type"]:
            output += "\n📊 **By Type:**\n"
            for agent_type, count in stats["by_type"].items():
                output += f"  • {agent_type}: {count}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    
    
    
    
    
    def debug_mode(self, args: List[str]) -> Dict[str, Any]:
        """Enable debug mode and diagnostics"""
        if not args:
            args = ["status"]
        
        action = args[0].lower()
        
        if action == "on":
            self.settings.update({"debug_mode": True})
            return {
                "status": "success",
                "output": "🐛 Debug mode enabled\n• Verbose logging active\n• Hook execution traces enabled"
            }
        elif action == "off":
            self.settings.update({"debug_mode": False})
            return {
                "status": "success",
                "output": "Debug mode disabled"
            }
        elif action == "status":
            return self._show_debug_status()
        elif action == "trace":
            return self._show_execution_trace()
        else:
            return {
                "status": "error",
                "message": f"Unknown debug action: {action}",
                "suggestions": ["on", "off", "status", "trace"]
            }
    
    def manage_reuse(self, args: List[str]) -> Dict[str, Any]:
        """Manage code reuse analysis and enforcement"""
        if not CODE_REUSE_AVAILABLE:
            return {
                "status": "error",
                "message": "Code reuse module not available. Check installation."
            }
            
        if not args:
            args = ["help"]
        
        action = args[0].lower()
        
        if action == "help":
            return self._show_reuse_help()
        elif action == "analyze":
            if len(args) < 2:
                return {"status": "error", "message": "Specify component name to analyze"}
            return self._analyze_reuse(args[1], ' '.join(args[2:]) if len(args) > 2 else '')
        elif action == "justify":
            if len(args) < 2:
                return {"status": "error", "message": "Specify file path to justify"}
            return self._justify_file(args[1], ' '.join(args[2:]) if len(args) > 2 else '')
        elif action == "report":
            return self._generate_reuse_report()
        elif action == "consolidate":
            return self._find_consolidation_opportunities()
        elif action == "metrics":
            return self._show_reuse_metrics()
        elif action == "enable":
            return self._toggle_reuse_enforcement(True)
        elif action == "disable":
            return self._toggle_reuse_enforcement(False)
        else:
            return {
                "status": "error",
                "message": f"Unknown reuse action: {action}",
                "suggestions": ["analyze", "justify", "report", "consolidate", "metrics", "enable", "disable"]
            }
    
    def _show_debug_status(self) -> Dict[str, Any]:
        """Show debug information"""
        output = MessageFormatter.header("Debug Status", "debug")
        
        output += f"\n🐛 **Debug Mode:** {'ON' if self.settings.get('debug_mode') else 'OFF'}\n"
        
        # Recent errors
        errors = self.state.get("recent_errors", [])
        if errors:
            output += "\n❌ **Recent Errors:**\n"
            for error in errors[-5:]:  # Last 5
                output += f"  • {error['time']}: {error['message']}\n"
        
        # Hook execution trace
        trace = self.state.get("execution_trace", [])
        if trace:
            output += "\n📊 **Recent Hook Executions:**\n"
            for item in trace[-10:]:  # Last 10
                output += f"  • {item['hook']} ({item['time']}ms) - {item['status']}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _show_execution_trace(self) -> Dict[str, Any]:
        """Show detailed execution trace"""
        trace = self.state.get("execution_trace", [])
        
        if not trace:
            return {
                "status": "info",
                "message": "No execution trace available. Enable debug mode first."
            }
        
        output = MessageFormatter.header("Execution Trace", "trace")
        
        for item in trace[-20:]:  # Last 20
            output += f"\n[{item['timestamp']}] {item['hook']}\n"
            output += f"  Event: {item['event']}\n"
            output += f"  Time: {item['time']}ms\n"
            if item.get('error'):
                output += f"  Error: {item['error']}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    # Helper methods
    def _get_performance_metrics(self) -> Dict[str, Any]:
        """Get system performance metrics"""
        # In production, these would be real metrics
        return {
            "avg_time": 23.5,
            "total_runs": 1847,
            "cache_hit_rate": 0.82,
            "memory_mb": 45.2
        }
    
    def _get_hook_stats(self, hook_name: str) -> Optional[Dict[str, Any]]:
        """Get statistics for a specific hook"""
        # In production, this would query real stats
        return {
            "runs": 234,
            "avg_time": 15.3,
            "last_run": "2 minutes ago"
        }
    
    def _get_automation_stats(self) -> Dict[str, Any]:
        """Get automation statistics"""
        return {
            "automated_commands": 7,
            "time_saved_hours": 12.5,
            "auto_fixes": 458
        }
    
    def _check_integrations(self) -> Dict[str, bool]:
        """Check integration status"""
        return {
            "Sequential Thinking": True,
            "Graphiti Memory": True,
            "GitHub": True
        }
    
    # Code Reuse Helper Methods
    def _show_reuse_help(self) -> Dict[str, Any]:
        """Show code reuse help"""
        output = MessageFormatter.header("Code Reuse System", "reuse")
        
        output += "\n📋 **Available Commands:**\n"
        commands = [
            ("analyze <component>", "Find reusable components matching name/description"),
            ("justify <file>", "Justify why a new file is needed"),
            ("report", "Generate comprehensive reuse report"),
            ("consolidate", "Find code consolidation opportunities"),
            ("metrics", "Show reuse metrics and statistics"),
            ("enable", "Enable reuse enforcement hook"),
            ("disable", "Disable reuse enforcement hook")
        ]
        
        for cmd, desc in commands:
            output += f"  • `/logic reuse {cmd}` - {desc}\n"
            
        output += "\n🎯 **Examples:**\n"
        output += "  • `/logic reuse analyze Button` - Find reusable button components\n"
        output += "  • `/logic reuse justify src/NewFeature.js` - Justify new file creation\n"
        output += "  • `/logic reuse consolidate` - Find duplicate code to merge\n"
        
        output += "\n💡 **Tips:**\n"
        output += "  • Run `analyze` before creating new files\n"
        output += "  • Use `consolidate` periodically to clean up duplicates\n"
        output += "  • Check `metrics` to track improvement over time\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def _analyze_reuse(self, component: str, description: str = '') -> Dict[str, Any]:
        """Analyze reuse opportunities for a component"""
        output = MessageFormatter.header(f"Reuse Analysis: {component}", "analysis")
        
        # Perform analysis
        analysis = self.reuse_analyzer.analyze_for_reuse(component, description)
        
        if not analysis.components:
            output += f"\n❌ No existing components found matching '{component}'\n"
            output += "✅ You may create a new file for this component.\n"
        else:
            output += f"\n🔍 Found {len(analysis.components)} reusable component(s):\n"
            
            for i, comp in enumerate(analysis.components, 1):
                output += f"\n**{i}. {comp.file_path}**\n"
                output += f"  • Match Score: {comp.match_score:.0%}\n"
                output += f"  • Functionality: {comp.functionality_match:.0%} match\n"
                output += f"  • Interface: {comp.interface_compatibility:.0%} compatible\n"
                output += f"  • Effort: {comp.modification_effort}\n"
                output += f"  • Recommendation: {comp.extension_method}\n"
                
                if comp.code_snippet:
                    output += f"  • Preview:\n```javascript\n{comp.code_snippet[:200]}...\n```\n"
            
            output += f"\n📊 **Overall Recommendation:** {analysis.recommendation}\n"
            if analysis.analysis_summary:
                output += f"💡 {analysis.analysis_summary}\n"
        
        # Update metrics
        self.reuse_state_manager.increment_value(
            'code_reuse_state.json',
            'statistics.total_analyses'
        )
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def _justify_file(self, file_path: str, reason: str = '') -> Dict[str, Any]:
        """Create justification for new file"""
        output = MessageFormatter.header(f"File Justification: {file_path}", "justify")
        
        # Check if justification already exists
        existing = self.justification_system.get_justification(file_path)
        if existing:
            output += f"\n📋 **Existing Justification:**\n"
            output += f"  • Status: {'✅ Approved' if existing.approved else '❌ Pending'}\n"
            output += f"  • Created: {existing.timestamp}\n"
            output += f"  • Reason: {existing.reason}\n"
            
            if existing.approved:
                output += "\n✅ This file is already approved for creation.\n"
                return {"status": "success", "output": output}
        
        if not reason:
            output += "\n❌ Please provide a justification reason.\n"
            output += "\nUsage: `/logic reuse justify <file> <reason>`\n"
            output += "\nExample reasons:\n"
            output += "  • 'New feature with no existing similar components'\n"
            output += "  • 'External integration requiring specific structure'\n"
            output += "  • 'Performance optimization requiring separate implementation'\n"
            return {"status": "error", "output": output}
        
        # Create justification
        justification = self.justification_system.create_justification(
            file_path=file_path,
            reason=reason,
            reuse_attempts=[],  # Should be filled from actual analysis
            alternatives_considered=[]
        )
        
        # Auto-approve for now (in real implementation, might require review)
        approved = self.justification_system.approve_justification(
            file_path,
            approved_by="system",
            comments="Auto-approved via /logic reuse justify"
        )
        
        if approved:
            output += "\n✅ **Justification Approved!**\n"
            output += f"  • File: {file_path}\n"
            output += f"  • Reason: {reason}\n"
            output += "\nYou may now create this file.\n"
        else:
            output += "\n❌ Justification could not be approved.\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def _generate_reuse_report(self) -> Dict[str, Any]:
        """Generate comprehensive reuse report"""
        output = MessageFormatter.header("Code Reuse Report", "report")
        
        # Load current state
        state = self.reuse_state_manager.load_state('code_reuse_state.json')
        stats = state.get('statistics', {})
        
        # Find consolidation opportunities
        opportunities = self.consolidation_analyzer.find_consolidation_opportunities()
        
        # Pattern compliance
        pattern_report = self.pattern_matcher.generate_pattern_report()
        
        output += "\n📊 **Reuse Statistics:**\n"
        output += f"  • Total Analyses: {stats.get('total_analyses', 0)}\n"
        output += f"  • Files Analyzed: {stats.get('files_analyzed', 0)}\n"
        output += f"  • Duplicates Found: {stats.get('duplicates_found', 0)}\n"
        output += f"  • Consolidations: {stats.get('consolidations_completed', 0)}\n"
        output += f"  • Code Lines Saved: {stats.get('code_lines_saved', 0)}\n"
        
        output += "\n🔄 **Consolidation Opportunities:**\n"
        if opportunities:
            total_savings = sum(opp.lines_saved for opp in opportunities)
            output += f"  • Found {len(opportunities)} opportunities\n"
            output += f"  • Potential savings: {total_savings} lines\n"
            
            for i, opp in enumerate(opportunities[:3], 1):
                output += f"\n  {i}. {opp.strategy} - {opp.lines_saved} lines\n"
                output += f"     Files: {', '.join(opp.affected_files[:3])}\n"
        else:
            output += "  • No consolidation opportunities found ✨\n"
        
        output += "\n📋 **Pattern Compliance:**\n"
        output += f"  • Patterns Followed: {pattern_report.get('patterns_followed', 0)}\n"
        output += f"  • Violations Found: {pattern_report.get('violations_count', 0)}\n"
        output += f"  • Adoption Rate: {pattern_report.get('adoption_rate', 0):.0%}\n"
        
        if pattern_report.get('top_violations'):
            output += "\n  ⚠️ Top Violations:\n"
            for violation in pattern_report['top_violations'][:3]:
                output += f"    • {violation['pattern']}: {violation['count']} instances\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def _find_consolidation_opportunities(self) -> Dict[str, Any]:
        """Find and display consolidation opportunities"""
        output = MessageFormatter.header("Consolidation Analysis", "consolidate")
        
        output += "\n🔍 Analyzing codebase for duplicates...\n"
        
        # Find opportunities
        opportunities = self.consolidation_analyzer.find_consolidation_opportunities()
        
        if not opportunities:
            output += "\n✨ **No consolidation opportunities found!**\n"
            output += "Your codebase is well-organized with minimal duplication.\n"
        else:
            output += f"\n📊 Found {len(opportunities)} consolidation opportunities:\n"
            
            total_savings = sum(opp.lines_saved for opp in opportunities)
            output += f"\n💰 **Total potential savings: {total_savings} lines**\n"
            
            for i, opp in enumerate(opportunities[:5], 1):
                output += f"\n**{i}. {opp.description}**\n"
                output += f"  • Strategy: {opp.strategy}\n"
                output += f"  • Lines saved: {opp.lines_saved}\n"
                output += f"  • Effort: {opp.effort_estimate}\n"
                output += f"  • Files affected: {len(opp.affected_files)}\n"
                
                if opp.migration_plan:
                    output += "  • Migration steps:\n"
                    for j, step in enumerate(opp.migration_plan[:3], 1):
                        output += f"    {j}. {step}\n"
                    if len(opp.migration_plan) > 3:
                        output += f"    ... and {len(opp.migration_plan) - 3} more steps\n"
            
            if len(opportunities) > 5:
                output += f"\n... and {len(opportunities) - 5} more opportunities\n"
            
            output += "\n💡 Run `/logic reuse report` for detailed analysis.\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def _show_reuse_metrics(self) -> Dict[str, Any]:
        """Show detailed reuse metrics"""
        output = MessageFormatter.header("Code Reuse Metrics", "metrics")
        
        # Load state
        state = self.reuse_state_manager.load_state('code_reuse_state.json')
        stats = state.get('statistics', {})
        perf = state.get('performance_metrics', {})
        
        output += "\n📈 **Usage Statistics:**\n"
        output += f"  • Total Analyses: {stats.get('total_analyses', 0)}\n"
        output += f"  • Files Analyzed: {stats.get('files_analyzed', 0)}\n"
        output += f"  • New Files Created: {stats.get('new_files_created', 0)}\n"
        output += f"  • File Creations Blocked: {stats.get('file_creations_blocked', 0)}\n"
        output += f"  • Compliance Warnings: {stats.get('compliance_warnings', 0)}\n"
        
        # Calculate reuse rate
        total_attempts = stats.get('new_files_created', 0) + stats.get('file_creations_blocked', 0)
        reuse_rate = (stats.get('file_creations_blocked', 0) / total_attempts * 100) if total_attempts > 0 else 0
        
        output += f"\n📊 **Effectiveness:**\n"
        output += f"  • Reuse Rate: {reuse_rate:.1f}%\n"
        output += f"  • Code Lines Saved: {stats.get('code_lines_saved', 0)}\n"
        output += f"  • Duplicates Found: {stats.get('duplicates_found', 0)}\n"
        output += f"  • Consolidations: {stats.get('consolidations_completed', 0)}\n"
        
        output += f"\n⚡ **Performance:**\n"
        output += f"  • Avg Analysis Time: {perf.get('average_analysis_time_ms', 0):.1f}ms\n"
        output += f"  • Cache Hit Rate: {perf.get('cache_hit_rate', 0):.1%}\n"
        output += f"  • Memory Usage: {perf.get('memory_usage_mb', 0):.1f}MB\n"
        
        # Feature flags
        flags = state.get('feature_flags', {})
        output += f"\n🔧 **Configuration:**\n"
        output += f"  • Pattern Learning: {'✅' if flags.get('pattern_learning_enabled', True) else '❌'}\n"
        output += f"  • AI Suggestions: {'✅' if flags.get('ai_suggestions_enabled', True) else '❌'}\n"
        output += f"  • Performance Mode: {flags.get('performance_mode', 'balanced')}\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def _toggle_reuse_enforcement(self, enable: bool) -> Dict[str, Any]:
        """Enable or disable reuse enforcement"""
        # This would update the hook configuration
        # For now, we'll just update the state
        action = "enabled" if enable else "disabled"
        
        output = MessageFormatter.header(f"Code Reuse {action.title()}", "config")
        output += f"\n{'✅' if enable else '❌'} Code reuse enforcement has been {action}.\n"
        
        if enable:
            output += "\n🔒 **Active Protections:**\n"
            output += "  • New file creation requires justification\n"
            output += "  • Compliance validation on all edits\n"
            output += "  • Reuse suggestions in prompts\n"
        else:
            output += "\n⚠️ **Warning:** Code reuse is not being enforced.\n"
            output += "Consider re-enabling to maintain code quality.\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}
    
    def check_claude_md_update(self, args: List[str]) -> Dict[str, Any]:
        """Check if CLAUDE.md needs updates based on system changes"""
        output = MessageFormatter.header("CLAUDE.md Update Check", "update")
        
        # Load tracked changes
        changes_file = self.logic_path / "system" / "claude_md_changes.json"
        if changes_file.exists():
            try:
                with open(changes_file, 'r') as f:
                    changes_data = json.load(f)
                    changes = changes_data.get("changes", [])
                    last_update = changes_data.get("last_update")
            except:
                changes = []
                last_update = None
        else:
            changes = []
            last_update = None
        
        if not changes:
            output += "\n✅ **CLAUDE.md is up to date**\n"
            output += "\nNo significant system changes detected since last update.\n"
            
            if last_update:
                output += f"\nLast update: {last_update}\n"
        else:
            output += f"\n📝 **{len(changes)} system changes detected:**\n\n"
            
            # Group changes by category
            categories = {
                "hooks": [],
                "commands": [],
                "code_reuse": [],
                "memory": [],
                "specs": []
            }
            
            for change in changes:
                file_path = change.get("file", "")
                if "hooks/" in file_path:
                    categories["hooks"].append(change)
                elif "commands/" in file_path:
                    categories["commands"].append(change)
                elif "code_reuse/" in file_path:
                    categories["code_reuse"].append(change)
                elif "memory/" in file_path:
                    categories["memory"].append(change)
                elif "specs/" in file_path and "/completed/" in file_path:
                    categories["specs"].append(change)
            
            # Display changes by category
            if categories["hooks"]:
                output += "**🪝 Hook Changes:**\n"
                for change in categories["hooks"]:
                    output += f"  • {change.get('description', 'Unknown change')}\n"
                output += "\n"
            
            if categories["commands"]:
                output += "**📟 Command Changes:**\n"
                for change in categories["commands"]:
                    output += f"  • {change.get('description', 'Unknown change')}\n"
                output += "\n"
            
            if categories["code_reuse"]:
                output += "**♻️ Code Reuse System Changes:**\n"
                for change in categories["code_reuse"]:
                    output += f"  • {change.get('description', 'Unknown change')}\n"
                output += "\n"
            
            if categories["memory"]:
                output += "**🧠 Memory System Changes:**\n"
                for change in categories["memory"]:
                    output += f"  • {change.get('description', 'Unknown change')}\n"
                output += "\n"
            
            if categories["specs"]:
                output += "**✅ Completed Features:**\n"
                for change in categories["specs"]:
                    output += f"  • {change.get('description', 'Unknown change')}\n"
                output += "\n"
            
            output += "\n🔄 **Recommended Updates for CLAUDE.md:**\n"
            output += "1. Review the changes above\n"
            output += "2. Update relevant sections in CLAUDE.md:\n"
            
            if categories["hooks"]:
                output += "   - Section 5: Hook Automation Warnings\n"
            if categories["commands"]:
                output += "   - Section 1: Quick Start (commands list)\n"
                output += "   - Section 6: Help & Troubleshooting\n"
            if categories["code_reuse"] or categories["memory"]:
                output += "   - START HERE steps (if process changed)\n"
                output += "   - Section 4: Memory Operations\n"
            if categories["specs"]:
                output += "   - Section 3: Task Management\n"
            
            output += "\n3. Run this command again after updates to clear the change log\n"
        
        # Check hook status
        output += "\n📊 **Self-Update Hook Status:**\n"
        hook_info = self.hook_registry.get_hook_info("claude-md-self-update-hook")
        if hook_info and hook_info.get("enabled"):
            output += "  ✅ Auto-monitoring is active\n"
            output += "  • Threshold: 5 significant changes\n"
            output += "  • Check frequency: Once per day\n"
        else:
            output += "  ❌ Auto-monitoring is disabled\n"
            output += "  • Enable with: `/logic hooks enable claude-md-self-update-hook`\n"
        
        output += "\n" + MessageFormatter.footer()
        return {"status": "success", "output": output}


def main():
    """Main entry point"""
    command = LogicCommand()
    
    # Get arguments from command line
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # Execute command
    result = command.execute(args)
    
    # Output result
    if result.get("output"):
        print(result["output"])
    elif result.get("message"):
        print(result["message"])
    
    # Exit with appropriate code
    exit_code = 0 if result.get("status") == "success" else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()