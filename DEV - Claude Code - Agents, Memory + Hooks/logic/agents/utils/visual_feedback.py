#!/usr/bin/env python3
"""
Visual Feedback System for Agent Operations
Provides real-time CLI visualization of agent activities
"""

import os
import sys
import time
import threading
from datetime import datetime
from typing import Dict, Any, Optional, List
from collections import deque
from dataclasses import dataclass
from enum import Enum
import json

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Agent colors
    ORCHESTRATOR = '\033[94m'  # Blue
    IMPLEMENTATION = '\033[92m'  # Green  
    ANALYSIS = '\033[93m'  # Yellow
    QA = '\033[96m'  # Cyan
    DOCUMENTATION = '\033[95m'  # Magenta
    
    # Status colors
    SUCCESS = '\033[92m'
    ERROR = '\033[91m'
    WARNING = '\033[93m'
    INFO = '\033[97m'
    
    # Background
    BG_ACTIVE = '\033[42m'
    BG_PENDING = '\033[43m'
    BG_ERROR = '\033[41m'

class AgentType(Enum):
    ORCHESTRATOR = "ORCHESTRATOR"
    IMPLEMENTATION = "IMPLEMENTATION"
    ANALYSIS = "ANALYSIS"
    QA = "QUALITY ASSURANCE"
    DOCUMENTATION = "DOCUMENTATION"

class StatusType(Enum):
    TASK_RECEIVED = "task_received"
    ROUTING_DECISION = "routing_decision"
    PROCESSING_START = "processing_start"
    PROGRESS_UPDATE = "progress_update"
    PROCESSING_COMPLETE = "processing_complete"
    ERROR_OCCURRED = "error_occurred"
    COST_UPDATE = "cost_update"

@dataclass
class AgentStatus:
    agent_id: str
    agent_type: AgentType
    model: str
    task: str
    status: str
    progress: float = 0.0
    context_used: int = 0
    context_limit: int = 0
    cost: float = 0.0
    estimated_cost: float = 0.0
    start_time: float = 0.0
    details: Dict[str, Any] = None

class AgentVisualFeedback:
    """
    Real-time visual feedback system for agent operations
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or self._default_config()
        self.active_agents: Dict[str, AgentStatus] = {}
        self.status_history = deque(maxlen=100)
        self.total_cost = 0.0
        self.total_saved = 0.0
        self.display_lock = threading.Lock()
        self.running = True
        
        # Icons for different agent types
        self.icons = {
            AgentType.ORCHESTRATOR: "🎯",
            AgentType.IMPLEMENTATION: "🔧",
            AgentType.ANALYSIS: "🔍",
            AgentType.QA: "✅",
            AgentType.DOCUMENTATION: "📝"
        }
        
        # Check terminal capabilities
        self.supports_color = self._check_color_support()
        self.terminal_width = self._get_terminal_width()
        
        # Start display thread if enabled
        if self.config['enabled']:
            self.display_thread = threading.Thread(target=self._update_display, daemon=True)
            self.display_thread.start()
    
    def _default_config(self) -> Dict[str, Any]:
        """Default configuration"""
        return {
            'enabled': True,
            'update_frequency_ms': 500,
            'show_token_usage': True,
            'show_cost_tracking': True,
            'show_progress_bars': True,
            'compact_mode': False,
            'color_output': True,
            'clear_screen': True
        }
    
    def _check_color_support(self) -> bool:
        """Check if terminal supports ANSI colors"""
        return sys.stdout.isatty() and os.getenv('TERM') != 'dumb'
    
    def _get_terminal_width(self) -> int:
        """Get terminal width"""
        try:
            import shutil
            return shutil.get_terminal_size().columns
        except:
            return 80
    
    def emit_status(self, agent_id: str, agent_type: AgentType, model: str, 
                   status_type: StatusType, data: Dict[str, Any]):
        """Emit a status update for an agent"""
        timestamp = datetime.now()
        
        with self.display_lock:
            if status_type == StatusType.TASK_RECEIVED:
                self.active_agents[agent_id] = AgentStatus(
                    agent_id=agent_id,
                    agent_type=agent_type,
                    model=model,
                    task=data.get('task', 'Unknown task'),
                    status='Initializing...',
                    start_time=time.time(),
                    context_limit=data.get('context_limit', 0),
                    estimated_cost=data.get('estimated_cost', 0)
                )
            
            elif agent_id in self.active_agents:
                agent = self.active_agents[agent_id]
                
                if status_type == StatusType.PROGRESS_UPDATE:
                    agent.progress = data.get('progress', 0)
                    agent.status = data.get('status', agent.status)
                    agent.context_used = data.get('context_used', agent.context_used)
                    agent.details = data.get('details', {})
                
                elif status_type == StatusType.COST_UPDATE:
                    agent.cost = data.get('cost', 0)
                    self.total_cost = sum(a.cost for a in self.active_agents.values())
                
                elif status_type == StatusType.PROCESSING_COMPLETE:
                    agent.progress = 100
                    agent.status = f"Completed ✓"
                    # Move to history after a delay
                    threading.Timer(2.0, self._move_to_history, args=[agent_id]).start()
                
                elif status_type == StatusType.ERROR_OCCURRED:
                    agent.status = f"Error: {data.get('error', 'Unknown error')}"
                    agent.progress = -1  # Indicates error state
            
            # Add to history
            self.status_history.append({
                'timestamp': timestamp,
                'agent_id': agent_id,
                'agent_type': agent_type,
                'status_type': status_type,
                'data': data
            })
    
    def _move_to_history(self, agent_id: str):
        """Move completed agent to history"""
        with self.display_lock:
            if agent_id in self.active_agents:
                del self.active_agents[agent_id]
    
    def _update_display(self):
        """Background thread to update display"""
        while self.running:
            if self.active_agents and self.config['enabled']:
                self._render_display()
            time.sleep(self.config['update_frequency_ms'] / 1000)
    
    def _render_display(self):
        """Render the current display"""
        with self.display_lock:
            output = []
            
            # Clear screen if configured
            if self.config['clear_screen']:
                output.append('\033[2J\033[H')  # Clear and move to top
            
            # Header
            output.append(self._render_header())
            
            # Active agents
            for agent_id, agent in self.active_agents.items():
                output.append(self._render_agent_status(agent))
            
            # Footer with cost tracking
            if self.config['show_cost_tracking']:
                output.append(self._render_footer())
            
            # Print all at once to reduce flicker
            print(''.join(output), end='', flush=True)
    
    def _render_header(self) -> str:
        """Render header section"""
        header = []
        header.append("═" * self.terminal_width + "\n")
        header.append("🚀 AGENT ORCHESTRATION ACTIVE\n")
        header.append("═" * self.terminal_width + "\n\n")
        return ''.join(header)
    
    def _render_agent_status(self, agent: AgentStatus) -> str:
        """Render individual agent status"""
        lines = []
        
        # Time and agent header
        timestamp = datetime.now().strftime("%H:%M:%S")
        icon = self.icons.get(agent.agent_type, "●")
        color = self._get_agent_color(agent.agent_type)
        
        # Main status line
        header = f"[{timestamp}] {icon} {color}{agent.agent_type.value}{Colors.RESET} [{agent.model}] - {agent.status}"
        lines.append(header + "\n")
        
        # Details
        indent = " " * 11  # Align with timestamp
        
        # Task
        lines.append(f"{indent}├─ Task: {agent.task[:60]}{'...' if len(agent.task) > 60 else ''}\n")
        
        # Progress bar if applicable
        if agent.progress >= 0 and self.config['show_progress_bars']:
            progress_bar = self._render_progress_bar(agent.progress)
            lines.append(f"{indent}├─ Progress: {progress_bar} {agent.progress:.0f}%\n")
        
        # Context usage
        if agent.context_limit > 0 and self.config['show_token_usage']:
            context_pct = (agent.context_used / agent.context_limit) * 100 if agent.context_limit > 0 else 0
            lines.append(f"{indent}├─ Context: {agent.context_used:,}/{agent.context_limit:,} tokens ({context_pct:.0f}%)\n")
        
        # Cost
        if self.config['show_cost_tracking']:
            cost_info = f"${agent.cost:.4f}"
            if agent.estimated_cost > 0:
                cost_info += f" (est: ${agent.estimated_cost:.4f})"
            lines.append(f"{indent}└─ Cost: {cost_info}\n")
        
        # Additional details
        if agent.details:
            for key, value in agent.details.items():
                lines.append(f"{indent}   {key}: {value}\n")
        
        lines.append("\n")
        return ''.join(lines)
    
    def _render_progress_bar(self, progress: float, width: int = 20) -> str:
        """Render a progress bar"""
        filled = int((progress / 100) * width)
        empty = width - filled
        
        if progress < 0:  # Error state
            return Colors.ERROR + "✗" * width + Colors.RESET
        
        bar = Colors.SUCCESS + "█" * filled + Colors.DIM + "░" * empty + Colors.RESET
        return bar
    
    def _render_footer(self) -> str:
        """Render footer with summary"""
        footer = []
        footer.append("═" * self.terminal_width + "\n")
        
        # Calculate savings
        opus_baseline = self.total_cost * 4  # Rough estimate
        saved = opus_baseline - self.total_cost
        
        footer.append(f"💰 Cost Tracking: ${self.total_cost:.4f} (Saved: ${saved:.2f} vs Opus-only)\n")
        
        # Active agents summary
        active_count = len(self.active_agents)
        footer.append(f"⏱️  Active Agents: {active_count}")
        
        footer.append("\n═" * self.terminal_width + "\n")
        return ''.join(footer)
    
    def _get_agent_color(self, agent_type: AgentType) -> str:
        """Get color for agent type"""
        if not self.supports_color or not self.config['color_output']:
            return ""
        
        color_map = {
            AgentType.ORCHESTRATOR: Colors.ORCHESTRATOR,
            AgentType.IMPLEMENTATION: Colors.IMPLEMENTATION,
            AgentType.ANALYSIS: Colors.ANALYSIS,
            AgentType.QA: Colors.QA,
            AgentType.DOCUMENTATION: Colors.DOCUMENTATION
        }
        return color_map.get(agent_type, Colors.INFO)
    
    def show_routing_decision(self, decisions: List[Dict[str, Any]]):
        """Show routing decisions in a formatted way"""
        output = []
        output.append(f"\n{Colors.ORCHESTRATOR}🎯 ROUTING DECISIONS:{Colors.RESET}\n")
        
        for i, decision in enumerate(decisions, 1):
            model = decision.get('model', 'Unknown')
            task = decision.get('task', 'Unknown task')
            cost = decision.get('estimated_cost', 0)
            reason = decision.get('reason', '')
            
            output.append(f"   {i}. {task[:50]}{'...' if len(task) > 50 else ''}\n")
            output.append(f"      → {model} (${cost:.4f})\n")
            if reason:
                output.append(f"      → {reason}\n")
        
        # Total estimates
        total_cost = sum(d.get('estimated_cost', 0) for d in decisions)
        opus_cost = total_cost * 4  # Rough estimate
        savings_pct = ((opus_cost - total_cost) / opus_cost * 100) if opus_cost > 0 else 0
        
        output.append(f"\n   Total estimate: ${total_cost:.4f} ({savings_pct:.0f}% savings vs Opus-only)\n\n")
        
        print(''.join(output))
    
    def shutdown(self):
        """Shutdown the visual feedback system"""
        self.running = False
        if hasattr(self, 'display_thread'):
            self.display_thread.join(timeout=1)

# Singleton instance
_visual_feedback = None

def get_visual_feedback() -> AgentVisualFeedback:
    """Get or create the visual feedback singleton"""
    global _visual_feedback
    if _visual_feedback is None:
        _visual_feedback = AgentVisualFeedback()
    return _visual_feedback

# Convenience functions
def emit_agent_status(agent_id: str, agent_type: AgentType, model: str,
                     status_type: StatusType, data: Dict[str, Any]):
    """Emit status update for an agent"""
    feedback = get_visual_feedback()
    feedback.emit_status(agent_id, agent_type, model, status_type, data)

def show_routing_decisions(decisions: List[Dict[str, Any]]):
    """Display routing decisions"""
    feedback = get_visual_feedback()
    feedback.show_routing_decision(decisions)

# Example usage and testing
if __name__ == "__main__":
    import uuid
    import random
    
    # Create visual feedback system
    vf = AgentVisualFeedback()
    
    # Simulate agent operations
    print("Simulating agent operations...\n")
    time.sleep(1)
    
    # Orchestrator receives task
    orch_id = str(uuid.uuid4())[:8]
    emit_agent_status(
        orch_id, 
        AgentType.ORCHESTRATOR,
        "Opus via MAX",
        StatusType.TASK_RECEIVED,
        {"task": "Implement dark mode toggle for settings page", "context_limit": 20000}
    )
    
    time.sleep(2)
    
    # Show routing decisions
    show_routing_decisions([
        {"task": "Research existing theme system", "model": "Gemini 2.5 Flash", "estimated_cost": 0.02, "reason": "Simple analysis task"},
        {"task": "Implement toggle component", "model": "QWEN3-Coder 35B", "estimated_cost": 0.35, "reason": "Complex implementation"},
        {"task": "Add dark mode styles", "model": "QWEN3-Coder 35B", "estimated_cost": 0.25, "reason": "CSS generation"}
    ])
    
    # Start analysis agent
    analysis_id = str(uuid.uuid4())[:8]
    emit_agent_status(
        analysis_id,
        AgentType.ANALYSIS,
        "Gemini 2.5 Flash",
        StatusType.TASK_RECEIVED,
        {"task": "Research existing theme system", "context_limit": 1000000}
    )
    
    # Simulate progress
    for i in range(0, 101, 20):
        time.sleep(1)
        emit_agent_status(
            analysis_id,
            AgentType.ANALYSIS,
            "Gemini 2.5 Flash",
            StatusType.PROGRESS_UPDATE,
            {
                "progress": i,
                "status": f"Scanning files... ({i}% complete)",
                "context_used": i * 1000,
                "details": {"files_scanned": i * 5}
            }
        )
        
        emit_agent_status(
            analysis_id,
            AgentType.ANALYSIS,
            "Gemini 2.5 Flash",
            StatusType.COST_UPDATE,
            {"cost": i * 0.0001}
        )
    
    # Complete analysis
    emit_agent_status(
        analysis_id,
        AgentType.ANALYSIS,
        "Gemini 2.5 Flash",
        StatusType.PROCESSING_COMPLETE,
        {}
    )
    
    time.sleep(5)
    
    # Shutdown
    vf.shutdown()
    print("\nSimulation complete!")