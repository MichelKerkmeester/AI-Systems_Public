#!/usr/bin/env python3
"""
Visual Feedback Integration for Agent System
Connects agents to the visual feedback display
"""

import time
import uuid
from typing import Dict, Any, Optional
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.visual_feedback import (
    AgentVisualFeedback, 
    AgentType, 
    StatusType,
    emit_agent_status,
    show_routing_decisions,
    get_visual_feedback
)

class VisualFeedbackMixin:
    """
    Mixin to add visual feedback capabilities to agents
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agent_id = str(uuid.uuid4())[:8]
        self.visual_feedback = get_visual_feedback()
        self._start_time = None
    
    def emit_visual_status(self, status_type: StatusType, data: Dict[str, Any]):
        """Emit status update to visual feedback system"""
        agent_type = self._get_agent_type()
        model = self._get_current_model()
        
        emit_agent_status(
            self.agent_id,
            agent_type,
            model,
            status_type,
            data
        )
    
    def _get_agent_type(self) -> AgentType:
        """Determine agent type from class name"""
        class_name = self.__class__.__name__.lower()
        
        if 'orchestrator' in class_name:
            return AgentType.ORCHESTRATOR
        elif 'implementation' in class_name:
            return AgentType.IMPLEMENTATION
        elif 'analysis' in class_name:
            return AgentType.ANALYSIS
        elif 'qa' in class_name or 'quality' in class_name:
            return AgentType.QA
        elif 'doc' in class_name:
            return AgentType.DOCUMENTATION
        else:
            return AgentType.IMPLEMENTATION  # Default
    
    def _get_current_model(self) -> str:
        """Get the current model being used"""
        # Override in subclasses
        return "Unknown Model"

class VisualOrchestratorMixin(VisualFeedbackMixin):
    """Enhanced orchestrator with visual feedback"""
    
    def decompose_task_visual(self, task: str) -> Any:
        """Decompose task with visual feedback"""
        self._start_time = time.time()
        
        # Emit task received
        self.emit_visual_status(
            StatusType.TASK_RECEIVED,
            {
                "task": task,
                "context_limit": 20000,
                "estimated_cost": 0.10  # Estimate for decomposition
            }
        )
        
        # Update status
        self.emit_visual_status(
            StatusType.PROCESSING_START,
            {"status": "Analyzing task complexity..."}
        )
        
        # Call original method
        result = self.decompose_task(task)
        
        # Show routing decisions if available
        if hasattr(self, 'routing_decisions') and self.routing_decisions:
            show_routing_decisions(self.routing_decisions)
        
        # Complete
        self.emit_visual_status(
            StatusType.PROCESSING_COMPLETE,
            {"duration": time.time() - self._start_time}
        )
        
        return result
    
    def _get_current_model(self) -> str:
        return "Opus via MAX"

class VisualImplementationMixin(VisualFeedbackMixin):
    """Enhanced implementation agent with visual feedback"""
    
    def implement_feature_visual(self, task: str, context: Dict[str, Any]) -> Any:
        """Implement feature with visual feedback"""
        self._start_time = time.time()
        
        # Determine model based on complexity
        model = self._select_implementation_model(context)
        self.current_model = model
        
        # Emit task received
        self.emit_visual_status(
            StatusType.TASK_RECEIVED,
            {
                "task": task,
                "context_limit": self._get_context_limit(model),
                "estimated_cost": self._estimate_cost(task, model)
            }
        )
        
        # Start processing
        self.emit_visual_status(
            StatusType.PROCESSING_START,
            {"status": "Setting up development environment..."}
        )
        
        # Simulate progress updates
        steps = [
            (20, "Analyzing existing code patterns..."),
            (40, "Generating component structure..."),
            (60, "Implementing core functionality..."),
            (80, "Adding error handling and tests..."),
            (95, "Finalizing implementation...")
        ]
        
        for progress, status in steps:
            self.emit_visual_status(
                StatusType.PROGRESS_UPDATE,
                {
                    "progress": progress,
                    "status": status,
                    "context_used": int(progress * 300),  # Simulate token usage
                    "details": {
                        "files_modified": int(progress / 20),
                        "lines_added": int(progress * 5)
                    }
                }
            )
            
            # Update cost
            self.emit_visual_status(
                StatusType.COST_UPDATE,
                {"cost": progress * 0.004}  # Simulate cost accumulation
            )
            
            time.sleep(0.5)  # Simulate work
        
        # Complete
        self.emit_visual_status(
            StatusType.PROCESSING_COMPLETE,
            {
                "duration": time.time() - self._start_time,
                "final_cost": 0.38
            }
        )
        
        # Return mock result
        return {"success": True, "files_created": 3, "tests_passed": 12}
    
    def _get_current_model(self) -> str:
        return getattr(self, 'current_model', 'QWEN3-Coder 35B')
    
    def _select_implementation_model(self, context: Dict[str, Any]) -> str:
        """Select model based on task complexity"""
        complexity = context.get('complexity', 'medium')
        
        if complexity == 'simple':
            return "Gemini 2.5 Flash"
        elif complexity == 'medium':
            return "QWEN3-Coder 35B"
        else:
            return "QWEN3-Coder 35B"  # or fall back to Opus for very complex
    
    def _get_context_limit(self, model: str) -> int:
        """Get context limit for model"""
        limits = {
            "QWEN3-Coder 35B": 50000,
            "Gemini 2.5 Flash": 1000000,
            "Opus via MAX": 20000
        }
        return limits.get(model, 50000)
    
    def _estimate_cost(self, task: str, model: str) -> float:
        """Estimate cost for task and model"""
        # Simple estimation based on task length and model
        base_costs = {
            "QWEN3-Coder 35B": 0.0000075,
            "Gemini 2.5 Flash": 0.00000026,
            "Opus via MAX": 0.00003
        }
        
        cost_per_token = base_costs.get(model, 0.0000075)
        estimated_tokens = len(task) * 100  # Rough estimate
        
        return estimated_tokens * cost_per_token

class VisualAnalysisMixin(VisualFeedbackMixin):
    """Enhanced analysis agent with visual feedback"""
    
    def analyze_code_visual(self, files: list, query: str) -> Any:
        """Analyze code with visual feedback"""
        self._start_time = time.time()
        
        # Emit task received
        self.emit_visual_status(
            StatusType.TASK_RECEIVED,
            {
                "task": f"Analyze {len(files)} files: {query}",
                "context_limit": 1000000,  # Gemini's large context
                "estimated_cost": 0.05
            }
        )
        
        # Progress through files
        for i, file in enumerate(files):
            progress = (i + 1) / len(files) * 100
            
            self.emit_visual_status(
                StatusType.PROGRESS_UPDATE,
                {
                    "progress": progress,
                    "status": f"Analyzing {file}...",
                    "context_used": (i + 1) * 5000,
                    "details": {
                        "current_file": file,
                        "patterns_found": i * 2
                    }
                }
            )
            
            time.sleep(0.3)  # Simulate analysis
        
        # Complete
        self.emit_visual_status(
            StatusType.PROCESSING_COMPLETE,
            {"duration": time.time() - self._start_time}
        )
        
        return {"patterns_found": 8, "recommendations": 3}
    
    def _get_current_model(self) -> str:
        return "Gemini 2.5 Flash"

# Integration helpers
def enhance_orchestrator(orchestrator_class):
    """Enhance orchestrator class with visual feedback"""
    class EnhancedOrchestrator(VisualOrchestratorMixin, orchestrator_class):
        pass
    return EnhancedOrchestrator

def enhance_implementation_agent(agent_class):
    """Enhance implementation agent with visual feedback"""
    class EnhancedImplementation(VisualImplementationMixin, agent_class):
        pass
    return EnhancedImplementation

def enhance_analysis_agent(agent_class):
    """Enhance analysis agent with visual feedback"""
    class EnhancedAnalysis(VisualAnalysisMixin, agent_class):
        pass
    return EnhancedAnalysis

# Example usage
if __name__ == "__main__":
    # Test the visual feedback integration
    print("Testing Visual Feedback Integration...\n")
    
    # Create mock agents with visual feedback
    class MockOrchestrator:
        def decompose_task(self, task):
            time.sleep(2)
            return ["subtask1", "subtask2", "subtask3"]
    
    class MockImplementation:
        def implement_feature(self, task, context):
            time.sleep(3)
            return {"success": True}
    
    # Enhance with visual feedback
    VisualOrchestrator = enhance_orchestrator(MockOrchestrator)
    VisualImplementation = enhance_implementation_agent(MockImplementation)
    
    # Test orchestrator
    orch = VisualOrchestrator()
    orch.routing_decisions = [
        {"task": "Create UI component", "model": "QWEN3-Coder", "estimated_cost": 0.35},
        {"task": "Write tests", "model": "Gemini Flash", "estimated_cost": 0.05}
    ]
    orch.decompose_task_visual("Build user dashboard with charts")
    
    time.sleep(2)
    
    # Test implementation
    impl = VisualImplementation()
    impl.implement_feature_visual("Create chart component", {"complexity": "medium"})
    
    # Let display complete
    time.sleep(2)
    print("\nTest complete!")
    
    # Shutdown
    get_visual_feedback().shutdown()