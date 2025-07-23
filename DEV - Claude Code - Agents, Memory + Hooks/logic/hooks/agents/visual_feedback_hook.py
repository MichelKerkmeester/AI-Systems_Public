#!/usr/bin/env python3
"""
Visual Feedback Hook for Agent Operations
Automatically displays agent activity in Claude Code CLI
No manual intervention required - fully automated
"""

import os
import sys
import json
import threading
from pathlib import Path
from typing import Dict, Any, Optional

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import visual feedback system
from agents.utils.visual_feedback import (
    get_visual_feedback,
    emit_agent_status,
    show_routing_decisions,
    AgentType,
    StatusType
)

# Global flag to track if visual feedback is enabled
VISUAL_FEEDBACK_ENABLED = os.getenv('CLAUDE_VISUAL_FEEDBACK', 'true').lower() == 'true'

# Track active operations
active_operations = {}
visual_feedback_instance = None

def initialize_visual_feedback():
    """Initialize visual feedback system if not already initialized"""
    global visual_feedback_instance
    
    if not VISUAL_FEEDBACK_ENABLED:
        return None
    
    if visual_feedback_instance is None:
        # Configure for seamless CLI integration
        config = {
            'enabled': True,
            'update_frequency_ms': 250,  # Smooth updates
            'show_token_usage': True,
            'show_cost_tracking': True,
            'show_progress_bars': True,
            'compact_mode': False,
            'color_output': True,
            'clear_screen': False  # Don't clear screen in CLI mode
        }
        
        visual_feedback_instance = get_visual_feedback()
        
        # Override config
        visual_feedback_instance.config.update(config)
        
        print("\n🚀 Agent Visual Feedback Active\n", file=sys.stderr)
    
    return visual_feedback_instance

def on_task_received(data: Dict[str, Any]) -> Dict[str, Any]:
    """Hook called when a task is received by any agent"""
    if not VISUAL_FEEDBACK_ENABLED:
        return data
    
    vf = initialize_visual_feedback()
    if not vf:
        return data
    
    # Extract task info
    task = data.get('task', 'Unknown task')
    agent_type = data.get('agent_type', 'ORCHESTRATOR')
    agent_id = data.get('agent_id', 'unknown')
    
    # Map agent type string to enum
    agent_type_map = {
        'orchestrator': AgentType.ORCHESTRATOR,
        'implementation': AgentType.IMPLEMENTATION,
        'analysis': AgentType.ANALYSIS,
        'qa': AgentType.QA,
        'documentation': AgentType.DOCUMENTATION
    }
    
    agent_enum = agent_type_map.get(agent_type.lower(), AgentType.IMPLEMENTATION)
    
    # Determine model based on agent type
    model_map = {
        AgentType.ORCHESTRATOR: "Opus via MAX",
        AgentType.IMPLEMENTATION: "QWEN3-Coder 35B",
        AgentType.ANALYSIS: "Gemini 2.5 Flash",
        AgentType.QA: "Opus",
        AgentType.DOCUMENTATION: "Gemini Flash"
    }
    
    model = data.get('model', model_map.get(agent_enum, 'Unknown'))
    
    # Track active operation
    active_operations[agent_id] = {
        'agent_type': agent_enum,
        'model': model,
        'task': task,
        'start_time': data.get('timestamp')
    }
    
    # Emit status
    emit_agent_status(
        agent_id,
        agent_enum,
        model,
        StatusType.TASK_RECEIVED,
        {
            'task': task,
            'context_limit': data.get('context_limit', 50000),
            'estimated_cost': data.get('estimated_cost', 0.0)
        }
    )
    
    return data

def on_routing_decision(data: Dict[str, Any]) -> Dict[str, Any]:
    """Hook called when orchestrator makes routing decisions"""
    if not VISUAL_FEEDBACK_ENABLED:
        return data
    
    vf = initialize_visual_feedback()
    if not vf:
        return data
    
    # Extract routing decisions
    decisions = data.get('routing_decisions', [])
    
    if decisions:
        # Format decisions for display
        formatted_decisions = []
        for decision in decisions:
            formatted_decisions.append({
                'task': decision.get('task', 'Unknown task'),
                'model': decision.get('model', 'Unknown model'),
                'estimated_cost': decision.get('cost', 0.0),
                'reason': decision.get('reason', '')
            })
        
        # Show routing visualization
        show_routing_decisions(formatted_decisions)
    
    return data

def on_agent_progress(data: Dict[str, Any]) -> Dict[str, Any]:
    """Hook called when agent reports progress"""
    if not VISUAL_FEEDBACK_ENABLED:
        return data
    
    agent_id = data.get('agent_id', 'unknown')
    
    if agent_id in active_operations:
        op = active_operations[agent_id]
        
        # Emit progress update
        emit_agent_status(
            agent_id,
            op['agent_type'],
            op['model'],
            StatusType.PROGRESS_UPDATE,
            {
                'progress': data.get('progress', 0),
                'status': data.get('status', 'Processing...'),
                'context_used': data.get('tokens_used', 0),
                'details': data.get('details', {})
            }
        )
        
        # Update cost if provided
        if 'cost' in data:
            emit_agent_status(
                agent_id,
                op['agent_type'],
                op['model'],
                StatusType.COST_UPDATE,
                {'cost': data['cost']}
            )
    
    return data

def on_agent_complete(data: Dict[str, Any]) -> Dict[str, Any]:
    """Hook called when agent completes a task"""
    if not VISUAL_FEEDBACK_ENABLED:
        return data
    
    agent_id = data.get('agent_id', 'unknown')
    
    if agent_id in active_operations:
        op = active_operations[agent_id]
        
        # Emit completion
        emit_agent_status(
            agent_id,
            op['agent_type'],
            op['model'],
            StatusType.PROCESSING_COMPLETE,
            {
                'duration': data.get('duration', 0),
                'final_cost': data.get('total_cost', 0),
                'success': data.get('success', True)
            }
        )
        
        # Clean up
        del active_operations[agent_id]
    
    return data

def on_agent_error(data: Dict[str, Any]) -> Dict[str, Any]:
    """Hook called when agent encounters an error"""
    if not VISUAL_FEEDBACK_ENABLED:
        return data
    
    agent_id = data.get('agent_id', 'unknown')
    
    if agent_id in active_operations:
        op = active_operations[agent_id]
        
        # Emit error status
        emit_agent_status(
            agent_id,
            op['agent_type'],
            op['model'],
            StatusType.ERROR_OCCURRED,
            {
                'error': data.get('error', 'Unknown error'),
                'recoverable': data.get('recoverable', False)
            }
        )
    
    return data

def on_session_end(data: Dict[str, Any]) -> Dict[str, Any]:
    """Hook called when session ends"""
    if visual_feedback_instance:
        # Show final summary
        total_cost = data.get('total_cost', 0)
        total_saved = data.get('total_saved', 0)
        duration = data.get('duration', 0)
        
        print(f"\n✅ Session Complete", file=sys.stderr)
        print(f"   Total Cost: ${total_cost:.4f}", file=sys.stderr)
        print(f"   Saved: ${total_saved:.4f} vs Opus-only", file=sys.stderr)
        print(f"   Duration: {duration:.1f}s\n", file=sys.stderr)
        
        # Shutdown visual feedback
        visual_feedback_instance.shutdown()
    
    return data

# Hook registration
def register_hooks():
    """Register visual feedback hooks with the system"""
    hook_registry = {
        'agent.task_received': on_task_received,
        'agent.routing_decision': on_routing_decision,
        'agent.progress': on_agent_progress,
        'agent.complete': on_agent_complete,
        'agent.error': on_agent_error,
        'session.end': on_session_end
    }
    
    return hook_registry

# Configuration check
def check_configuration():
    """Check if visual feedback is properly configured"""
    issues = []
    
    # Check terminal support
    if not sys.stdout.isatty():
        issues.append("Not running in a TTY - visual feedback may be limited")
    
    # Check environment
    if os.getenv('TERM') == 'dumb':
        issues.append("Terminal type is 'dumb' - colors disabled")
    
    # Check if explicitly disabled
    if not VISUAL_FEEDBACK_ENABLED:
        issues.append("Visual feedback disabled via CLAUDE_VISUAL_FEEDBACK=false")
    
    return issues

# Auto-initialization on import
if __name__ != "__main__":
    # Only initialize if imported as a module
    if VISUAL_FEEDBACK_ENABLED:
        # Register hooks automatically
        hooks = register_hooks()
        
        # Check for issues
        issues = check_configuration()
        if issues:
            for issue in issues:
                print(f"⚠️  Visual Feedback: {issue}", file=sys.stderr)

# Test mode
if __name__ == "__main__":
    print("Testing Visual Feedback Hook...")
    
    # Initialize
    vf = initialize_visual_feedback()
    
    # Test task received
    on_task_received({
        'task': 'Test task for visual feedback',
        'agent_type': 'orchestrator',
        'agent_id': 'test-001',
        'context_limit': 20000,
        'estimated_cost': 0.10
    })
    
    # Test routing
    on_routing_decision({
        'routing_decisions': [
            {'task': 'Subtask 1', 'model': 'QWEN3', 'cost': 0.35, 'reason': 'Complex implementation'},
            {'task': 'Subtask 2', 'model': 'Gemini', 'cost': 0.05, 'reason': 'Simple analysis'}
        ]
    })
    
    # Test progress
    import time
    for i in range(0, 101, 20):
        time.sleep(0.5)
        on_agent_progress({
            'agent_id': 'test-001',
            'progress': i,
            'status': f'Processing... {i}%',
            'tokens_used': i * 100,
            'cost': i * 0.001
        })
    
    # Test completion
    on_agent_complete({
        'agent_id': 'test-001',
        'duration': 5.2,
        'total_cost': 0.15,
        'success': True
    })
    
    # Test session end
    on_session_end({
        'total_cost': 0.15,
        'total_saved': 0.85,
        'duration': 5.2
    })
    
    print("\nTest complete!")