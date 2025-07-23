#!/usr/bin/env python3
"""
Agent Management Commands - V3 Simplified System

A lightweight agent system that works WITH existing automation,
not replacing it. Uses Claude's Task tool for parallelism.
"""

import sys
import asyncio
import json
from pathlib import Path
from typing import Dict, List, Any

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from logic.shared import MessageFormatter

# Import v3 agents if available
try:
    from logic.agents.v3.orchestrator import OrchestratorAgent
    from logic.agents.v3.implementation_agent import ImplementationAgent
    from logic.agents.v3.compatibility_layer import AgentCompatibilityLayer
    V3_AVAILABLE = True
except ImportError:
    V3_AVAILABLE = False


class AgentsCommand:
    """Agent command handler - supports both legacy info and v3 system"""
    
    def __init__(self):
        self.compatibility_layer = AgentCompatibilityLayer() if V3_AVAILABLE else None
        self.orchestrator = None
        self.agents = {}
        
    def execute(self, args: List[str]) -> Dict[str, Any]:
        """Execute agents command with v3 support"""
        if not args:
            return self._show_help()
        
        subcommand = args[0]
        
        if subcommand == "help":
            return self._show_help()
        elif subcommand == "run" and V3_AVAILABLE:
            return self._run_agent(args[1:])
        elif subcommand == "status" and V3_AVAILABLE:
            return self._show_status()
        elif subcommand == "legacy":
            return self._show_legacy_info()
        else:
            return self._show_help()
    
    def _show_help(self) -> Dict[str, Any]:
        """Show agent system help"""
        output = MessageFormatter.header("Agent System V3", "info")
        
        if V3_AVAILABLE:
            output += "\n🤖 **Simplified Agent System Active**\n\n"
            output += "Commands:\n"
            output += "  • `/agent run <task>` - Run task through agent system\n"
            output += "  • `/agent status` - Show agent system status\n"
            output += "  • `/agent legacy` - Show legacy system info\n\n"
            
            output += "Features:\n"
            output += "  • Uses Claude's Task tool for parallelism\n"
            output += "  • Integrates with existing hooks\n"
            output += "  • QWEN3 support for cost optimization\n"
            output += "  • Automatic memory capture\n\n"
            
            output += "The system runs invisibly - just use normal commands!\n"
        else:
            output += "\n⚠️ **Agent System V3 Not Available**\n\n"
            output += "The v3 agent modules are not properly installed.\n"
            output += "Showing legacy information instead.\n\n"
            output += self._show_legacy_info()["output"]
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def _show_legacy_info(self) -> Dict[str, Any]:
        """Show legacy agent system info"""
        output = ""
        output += "\n⚠️ **Legacy Agent System Info**\n\n"
        
        output += "The `.claude/logic/agents/` directory contains:\n"
        output += "  • **intelligence/** - Enhancement and integration modules\n"
        output += "    - prompt_enhancer.py - Claude-Organizer prompt enhancement\n"
        output += "    - pattern_library.py - Pattern matching for prompts\n"
        output += "    - graphiti_memory_integration.py - Memory system integration\n"
        output += "    - sequential_thinking_integration.py - Thinking tool integration\n"
        output += "    - conflict_resolution.py - Conflict handling utilities\n\n"
        
        output += "These modules work automatically through hooks.\n"
        
        return {
            "status": "success",
            "output": output
        }
    
    def _run_agent(self, args: List[str]) -> Dict[str, Any]:
        """Run a task through the agent system"""
        if not args:
            return {
                "status": "error",
                "output": "❌ Please provide a task description"
            }
        
        task_description = " ".join(args)
        
        # Run async task
        result = asyncio.run(self._execute_agent_task(task_description))
        
        output = MessageFormatter.header("Agent Execution Result", "success")
        output += f"\n📋 **Task**: {task_description}\n\n"
        output += f"**Result**: {json.dumps(result, indent=2)}\n"
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    async def _execute_agent_task(self, task_description: str) -> Dict[str, Any]:
        """Execute task through agent system"""
        # Initialize agents if needed
        if not self.orchestrator:
            self.orchestrator = OrchestratorAgent()
            self.orchestrator.register_agent("implementation", ImplementationAgent())
        
        # Create task
        task = {
            "description": task_description,
            "source": "cli"
        }
        
        # Execute through compatibility layer
        if self.compatibility_layer:
            result = await self.compatibility_layer.wrap_agent_execution(
                self.orchestrator.execute,
                task=task
            )
        else:
            result = await self.orchestrator.execute(task)
        
        return result
    
    def _show_status(self) -> Dict[str, Any]:
        """Show agent system status"""
        output = MessageFormatter.header("Agent System Status", "info")
        
        # Get compatibility status
        if self.compatibility_layer:
            status = self.compatibility_layer.get_integration_status()
            
            output += "\n🔧 **Integration Status**\n"
            output += f"  • Hooks discovered: {status['hooks_discovered']}\n"
            output += f"  • Available hooks: {', '.join(status['hooks_available'])}\n"
            output += f"  • Overall status: {status['status']}\n\n"
            
            output += "**Compatibility Checks**:\n"
            for check, result in status['compatibility_checks'].items():
                emoji = "✅" if result else "❌"
                output += f"  {emoji} {check.replace('_', ' ').title()}\n"
        
        # Get orchestrator stats if available
        if self.orchestrator:
            stats = asyncio.run(self.orchestrator.get_routing_stats())
            output += f"\n📊 **Routing Statistics**\n"
            output += f"  • Total routed: {stats['total_routed']}\n"
            output += f"  • Registered agents: {', '.join(stats['registered_agents'])}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }


def main():
    """Main entry point for agents command"""
    command = AgentsCommand()
    
    # Get arguments
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    # Execute command
    result = command.execute(args)
    
    # Output result
    if result.get("output"):
        print(result["output"])
    elif result.get("message"):
        print(result["message"])
    
    # Exit code
    sys.exit(0 if result.get("status") == "success" else 1)


if __name__ == "__main__":
    main()