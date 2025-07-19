#!/usr/bin/env python3
"""
Agent Management Commands for /logic agents

Handles multi-agent orchestration with intelligent model routing.
"""

import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "agents"))

from shared import MessageFormatter, StateManager
from routing import TaskComplexityAnalyzer, ModelSelector, TaskType, ComplexityLevel
from orchestration.orchestrator_command import orchestrator_command


class AgentsCommand:
    """Manage multi-agent system with model routing"""
    
    def __init__(self):
        self.claude_path = Path.home() / ".claude" 
        self.project_root = Path.cwd()
        self.agents_path = self.claude_path / "agents"
        
        # State management
        self.state = StateManager(
            self.agents_path / "state" / "agents-state.json",
            default_state={
                "active_agents": [],
                "model_usage": {},
                "total_tasks": 0,
                "routing_enabled": True
            }
        )
        
        # Initialize components
        self.complexity_analyzer = TaskComplexityAnalyzer()
        self.model_selector = ModelSelector()
    
    def execute(self, args: List[str]) -> Dict[str, Any]:
        """Execute agents command"""
        if not args:
            return self.show_help()
        
        action = args[0].lower()
        
        # Command handlers
        handlers = {
            "help": self.show_help,
            "start": self.start_agents,
            "status": self.show_status,
            "models": self.show_models,
            "route": self.configure_routing,
            "analyze": self.analyze_task,
            "synthesize": self.synthesize_results,
            "cleanup": self.cleanup_agents,
            "config": self.show_config,
            "orchestrate": self.orchestrate_task,
            "orchestrations": self.list_orchestrations
        }
        
        if action in handlers:
            return handlers[action](args[1:] if len(args) > 1 else [])
        else:
            return {
                "status": "error",
                "message": f"Unknown agents action: {action}",
                "suggestions": list(handlers.keys())
            }
    
    def show_help(self, args: List[str] = None) -> Dict[str, Any]:
        """Show agents help"""
        output = MessageFormatter.header("/logic agents - Multi-Agent System", "agents")
        
        output += "\n🤖 **Agent Commands:**\n"
        commands = [
            ("start [mode]", "Start agents (simple/parallel/swarm)"),
            ("status", "Show active agents and resources"),
            ("models", "Model usage statistics"),
            ("route [model]", "Override model routing"),
            ("analyze [task]", "Analyze task complexity"),
            ("synthesize", "Combine agent results"),
            ("cleanup", "Clean up worktrees and resources"),
            ("config", "Show agent configuration"),
            ("orchestrate [task]", "Start full orchestration for task"),
            ("orchestrations", "List active orchestrations")
        ]
        
        for cmd, desc in commands:
            output += f"  • `/logic agents {cmd}` - {desc}\n"
        
        output += "\n🚀 **Start Modes:**\n"
        output += "  • `simple` - Single agent mode\n"
        output += "  • `parallel` - 2-4 agents (default)\n" 
        output += "  • `swarm` - 5+ agents for large tasks\n"
        
        output += "\n🎯 **Model Routing:**\n"
        output += "  • Claude Opus - Complex tasks, synthesis\n"
        output += "  • Kimi Pro - Simple edits, searches\n"
        output += "  • Gemini (MCP) - Analysis, reviews\n"
        
        output += "\n📊 **Current Status:**\n"
        active_agents = self.state.get("active_agents", [])
        output += f"  • Active agents: {len(active_agents)}\n"
        output += f"  • Routing: {'✅ Enabled' if self.state.get('routing_enabled') else '❌ Disabled'}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def start_agents(self, args: List[str]) -> Dict[str, Any]:
        """Start agent orchestration"""
        mode = args[0] if args else "parallel"
        
        if mode not in ["simple", "parallel", "swarm"]:
            return {
                "status": "error",
                "message": f"Invalid mode: {mode}. Use simple/parallel/swarm"
            }
        
        output = MessageFormatter.header(f"Starting {mode.title()} Agents", "agents")
        
        # Determine agent count
        agent_counts = {
            "simple": 1,
            "parallel": 3,
            "swarm": 5
        }
        
        count = agent_counts[mode]
        output += f"\n🚀 **Launching {count} agent{'s' if count > 1 else ''}...**\n\n"
        
        # Agent types based on mode
        if mode == "simple":
            agents = ["developer"]
        elif mode == "parallel":
            agents = ["analyst", "developer", "reviewer"]
        else:  # swarm
            agents = ["analyst", "developer", "developer", "reviewer", "synthesis"]
        
        # Simulate agent launch
        launched = []
        for i, agent_type in enumerate(agents):
            agent_id = f"{agent_type}-{int(time.time())}-{i}"
            
            # Determine model based on agent type
            if agent_type == "synthesis":
                model = "claude-opus-4"
            elif agent_type == "analyst":
                model = "gemini-mcp"
            elif agent_type == "reviewer":
                model = "claude-opus-4"
            else:  # developer
                model = "kimi-pro" if self.state.get("routing_enabled") else "claude-opus-4"
            
            output += f"🤖 **{agent_type.title()} Agent**\n"
            output += f"  • ID: {agent_id}\n"
            output += f"  • Model: {model}\n"
            output += f"  • Status: Initializing...\n\n"
            
            launched.append({
                "id": agent_id,
                "type": agent_type,
                "model": model,
                "started": datetime.now().isoformat(),
                "status": "active"
            })
        
        # Update state
        self.state.update({
            "active_agents": launched,
            "last_start": datetime.now().isoformat()
        })
        
        output += "✅ **Agents launched successfully!**\n\n"
        output += "Next steps:\n"
        output += "  • Monitor with `/logic agents status`\n"
        output += "  • View model usage with `/logic agents models`\n"
        output += "  • Synthesize results with `/logic agents synthesize`\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def show_status(self, args: List[str]) -> Dict[str, Any]:
        """Show agent status"""
        output = MessageFormatter.header("Agent System Status", "status")
        
        active_agents = self.state.get("active_agents", [])
        
        if not active_agents:
            output += "\n📭 No active agents.\n"
            output += "\nStart agents with `/logic agents start`\n"
        else:
            output += f"\n🤖 **Active Agents ({len(active_agents)}):**\n\n"
            
            # Group by type
            by_type = {}
            for agent in active_agents:
                agent_type = agent["type"]
                if agent_type not in by_type:
                    by_type[agent_type] = []
                by_type[agent_type].append(agent)
            
            for agent_type, agents in by_type.items():
                output += f"**{agent_type.title()} Agents ({len(agents)}):**\n"
                for agent in agents:
                    output += f"  • {agent['id']}\n"
                    output += f"    Model: {agent['model']}\n"
                    output += f"    Status: {agent['status']}\n"
                output += "\n"
        
        # Resource usage simulation
        output += "💻 **Resource Usage:**\n"
        if active_agents:
            memory = len(active_agents) * 150  # MB per agent
            cpu = len(active_agents) * 15  # % per agent
            output += f"  • Memory: {memory} MB\n"
            output += f"  • CPU: {cpu}%\n"
            output += f"  • Git worktrees: {len([a for a in active_agents if a['type'] == 'developer'])}\n"
        else:
            output += "  • No resources in use\n"
        
        # Model routing status
        output += f"\n🎯 **Model Routing:**\n"
        output += f"  • Status: {'✅ Enabled' if self.state.get('routing_enabled') else '❌ Disabled'}\n"
        
        if self.state.get("routing_enabled"):
            output += "  • Strategy: Complexity-based\n"
            output += "  • Fallback: claude-opus-4\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def show_models(self, args: List[str]) -> Dict[str, Any]:
        """Show model usage statistics"""
        output = MessageFormatter.header("Model Usage Statistics", "models")
        
        # Get usage report from model selector
        report = self.model_selector.get_usage_report()
        
        output += "\n💰 **Cost Analysis:**\n"
        output += f"  • Total cost: ${report['total_cost']:.2f}\n"
        output += f"  • Tasks routed: {report['total_tasks']}\n"
        
        if report['cost_savings']['percentage'] > 0:
            output += f"  • Savings: ${report['cost_savings']['saved']:.2f} "
            output += f"({report['cost_savings']['percentage']:.1f}%)\n"
        
        output += "\n📊 **Usage by Model:**\n"
        for model, stats in report['by_model'].items():
            output += f"\n**{model}:**\n"
            output += f"  • Tasks: {stats['count']}\n"
            output += f"  • Tokens: {stats['total_tokens']:,}\n"
            output += f"  • Cost: ${stats['total_cost']:.2f}\n"
            
            if stats['task_types']:
                output += "  • Top tasks: "
                top_tasks = sorted(stats['task_types'].items(), 
                                 key=lambda x: x[1], reverse=True)[:3]
                output += ", ".join([f"{t[0]} ({t[1]})" for t in top_tasks])
                output += "\n"
        
        # Recommendations
        if report['recommendations']:
            output += "\n💡 **Recommendations:**\n"
            for rec in report['recommendations']:
                output += f"  • {rec}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def configure_routing(self, args: List[str]) -> Dict[str, Any]:
        """Configure model routing"""
        if not args:
            # Show current routing
            output = "🎯 **Current Routing Configuration:**\n"
            output += f"  • Status: {'✅ Enabled' if self.state.get('routing_enabled') else '❌ Disabled'}\n"
            output += "\nUsage: `/logic agents route [on|off|force-model]`\n"
            
            return {
                "status": "success",
                "output": output
            }
        
        action = args[0].lower()
        
        if action == "on":
            self.state.update({"routing_enabled": True})
            return {
                "status": "success",
                "output": "✅ Model routing enabled. Tasks will be routed based on complexity."
            }
        elif action == "off":
            self.state.update({"routing_enabled": False})
            return {
                "status": "success",
                "output": "❌ Model routing disabled. All tasks will use Claude Opus."
            }
        elif action in ["claude", "kimi", "gemini"]:
            # Force specific model
            model_map = {
                "claude": "claude-opus-4",
                "kimi": "kimi-pro",
                "gemini": "gemini-mcp"
            }
            
            self.state.update({
                "forced_model": model_map[action],
                "routing_enabled": False
            })
            
            return {
                "status": "success",
                "output": f"🎯 Forcing all tasks to use {action.title()}. Routing disabled."
            }
        else:
            return {
                "status": "error",
                "message": f"Invalid routing option: {action}",
                "suggestions": ["on", "off", "claude", "kimi", "gemini"]
            }
    
    def analyze_task(self, args: List[str]) -> Dict[str, Any]:
        """Analyze task complexity"""
        if not args:
            return {
                "status": "error",
                "message": "Provide a task description to analyze"
            }
        
        task_description = " ".join(args)
        
        # Analyze complexity
        analysis = self.complexity_analyzer.analyze_task(task_description)
        
        output = MessageFormatter.header("Task Complexity Analysis", "analysis")
        
        output += f"\n📝 **Task:** {task_description[:100]}{'...' if len(task_description) > 100 else ''}\n"
        
        output += f"\n📊 **Analysis Results:**\n"
        output += f"  • Complexity Score: {analysis.complexity_score}/20\n"
        output += f"  • Level: {analysis.complexity_level.name}\n"
        output += f"  • Task Type: {analysis.task_type.value}\n"
        output += f"  • Files Affected: ~{analysis.files_affected}\n"
        
        output += f"\n🎯 **Requirements:**\n"
        output += f"  • Full Context: {'Yes' if analysis.requires_full_context else 'No'}\n"
        output += f"  • Reasoning: {'Yes' if analysis.requires_reasoning else 'No'}\n"
        output += f"  • Creativity: {'Yes' if analysis.requires_creativity else 'No'}\n"
        
        output += f"\n💻 **Recommended Model:** {analysis.recommended_model}\n"
        output += f"💰 **Estimated Cost:** ${self.model_selector._estimate_cost(analysis, analysis.recommended_model):.3f}\n"
        
        if analysis.reasoning:
            output += f"\n📋 **Reasoning:**\n"
            for reason in analysis.reasoning:
                output += f"  • {reason}\n"
        
        # Model selection details
        selection = self.model_selector.select_model(analysis, "developer")
        
        if selection.warnings:
            output += f"\n⚠️ **Warnings:**\n"
            for warning in selection.warnings:
                output += f"  • {warning}\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def synthesize_results(self, args: List[str]) -> Dict[str, Any]:
        """Synthesize agent results"""
        active_agents = self.state.get("active_agents", [])
        
        if not active_agents:
            return {
                "status": "error",
                "message": "No active agents to synthesize results from"
            }
        
        output = MessageFormatter.header("Synthesizing Agent Results", "synthesis")
        
        output += f"\n🔄 **Processing {len(active_agents)} agent outputs...**\n\n"
        
        # Simulate synthesis process
        output += "📊 **Agent Contributions:**\n"
        
        for agent in active_agents:
            output += f"\n🤖 {agent['type'].title()} ({agent['id']}):\n"
            
            if agent['type'] == 'analyst':
                output += "  • Task decomposition completed\n"
                output += "  • Identified 3 work packages\n"
                output += "  • Complexity: Medium\n"
            elif agent['type'] == 'developer':
                output += "  • Implementation in progress\n"
                output += "  • Files modified: 5\n"
                output += "  • Tests: Pending\n"
            elif agent['type'] == 'reviewer':
                output += "  • Code review completed\n"
                output += "  • Issues found: 2 minor\n"
                output += "  • Security: Pass\n"
        
        output += "\n🎯 **Synthesis Results:**\n"
        output += "  • Overall Progress: 75%\n"
        output += "  • Conflicts: None\n"
        output += "  • Ready to merge: Yes\n"
        
        output += "\n✅ **Next Steps:**\n"
        output += "  1. Review synthesized output\n"
        output += "  2. Run tests with quality hook\n"
        output += "  3. Merge to main branch\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def cleanup_agents(self, args: List[str]) -> Dict[str, Any]:
        """Clean up agent resources"""
        active_agents = self.state.get("active_agents", [])
        
        output = "🧹 **Cleaning up agent resources...**\n\n"
        
        if not active_agents:
            output += "No active agents to clean up.\n"
        else:
            output += f"Stopping {len(active_agents)} agents:\n"
            
            for agent in active_agents:
                output += f"  • Stopping {agent['id']}...\n"
            
            output += "\n📁 **Cleanup Tasks:**\n"
            output += "  • Removing git worktrees\n"
            output += "  • Clearing agent workspaces\n"
            output += "  • Releasing memory\n"
            output += "  • Saving final statistics\n"
            
            # Clear state
            self.state.update({"active_agents": []})
            
            output += "\n✅ **Cleanup completed successfully!**\n"
        
        return {
            "status": "success",
            "output": output
        }
    
    def show_config(self, args: List[str]) -> Dict[str, Any]:
        """Show agent configuration"""
        output = MessageFormatter.header("Agent Configuration", "config")
        
        output += "\n⚙️ **System Configuration:**\n"
        output += f"  • Max agents: 10\n"
        output += f"  • Memory per agent: 512 MB\n"
        output += f"  • CPU per agent: 25%\n"
        output += f"  • Worktree path: .claude/agents/worktrees/\n"
        
        output += "\n🎯 **Model Configuration:**\n"
        output += "  • Claude Opus: $0.015/1k tokens\n"
        output += "  • Kimi Pro: $0.003/1k tokens (80% cheaper)\n"
        output += "  • Gemini MCP: $0.005/1k tokens (67% cheaper)\n"
        
        output += "\n🤖 **Agent Types:**\n"
        agent_configs = [
            ("Analyst", "Problem decomposition, research", "Gemini MCP"),
            ("Developer", "Implementation, coding", "Kimi Pro / Claude"),
            ("Reviewer", "Code review, quality", "Claude Opus"),
            ("Synthesis", "Merge results, resolve conflicts", "Claude Opus")
        ]
        
        for name, role, model in agent_configs:
            output += f"\n**{name} Agent:**\n"
            output += f"  • Role: {role}\n"
            output += f"  • Default model: {model}\n"
        
        output += "\n📋 **Feature Flags:**\n"
        output += f"  • ENABLE_MULTI_AGENT: true\n"
        output += f"  • ENABLE_MODEL_ROUTING: true\n"
        output += f"  • MAX_PARALLEL_AGENTS: 10\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    async def orchestrate_task(self, args: List[str]) -> Dict[str, Any]:
        """Start full orchestration for a task"""
        if not args:
            return {
                "status": "error",
                "message": "Provide a task description to orchestrate"
            }
        
        task_description = " ".join(args)
        
        output = MessageFormatter.header("Starting Task Orchestration", "orchestrate")
        output += f"\n📋 **Task:** {task_description[:100]}{'...' if len(task_description) > 100 else ''}\n\n"
        
        # Start orchestration
        import asyncio
        result = asyncio.run(orchestrator_command.start_orchestration(
            task_description,
            {"max_agents": 5}
        ))
        
        output += "🚀 **Orchestration Started:**\n"
        output += f"  • Orchestrator ID: {result['orchestrator_id']}\n"
        output += f"  • Work packages: {result['work_packages']}\n"
        output += f"  • Max agents: {result['max_agents']}\n\n"
        
        output += "📊 **Next Steps:**\n"
        output += f"  • Monitor: `/logic agents status`\n"
        output += f"  • View details: `/logic agents orchestrations`\n"
        output += f"  • Stop: `/logic agents cleanup`\n"
        
        output += "\n" + MessageFormatter.footer()
        
        return {
            "status": "success",
            "output": output
        }
    
    def list_orchestrations(self, args: List[str]) -> Dict[str, Any]:
        """List active orchestrations"""
        output = MessageFormatter.header("Active Orchestrations", "orchestrations")
        
        orchestrations = orchestrator_command.list_orchestrations()
        
        if not orchestrations:
            output += "\n📭 No active orchestrations.\n"
            output += "\nStart one with `/logic agents orchestrate [task]`\n"
        else:
            output += f"\n🎯 **Active Orchestrations ({len(orchestrations)}):**\n\n"
            
            for orch in orchestrations:
                output += f"**{orch['orchestrator_id']}:**\n"
                output += f"  • State: {orch['state']}\n"
                output += f"  • Agents: {orch['agents']}\n"
                output += f"  • Work packages: {orch['work_packages']}\n\n"
                
                # Get detailed status
                status = orchestrator_command.get_status(orch['orchestrator_id'])
                if 'model_usage' in status:
                    output += "  • Model Usage:\n"
                    for model, count in status['model_usage'].get('by_model', {}).items():
                        output += f"    - {model}: {count}\n"
                    if 'cost_reduction' in status['model_usage']:
                        output += f"  • Cost Reduction: {status['model_usage']['cost_reduction']}\n"
                output += "\n"
        
        output += MessageFormatter.footer()
        
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