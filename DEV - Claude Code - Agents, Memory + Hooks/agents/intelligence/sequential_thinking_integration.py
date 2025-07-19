"""
Sequential Thinking Integration for Multi-Agent System

Connects agents to the Sequential Thinking MCP for structured reasoning.
"""

import json
from typing import Dict, Any, List, Optional
from pathlib import Path


class SequentialThinkingIntegration:
    """Integrates Sequential Thinking MCP with agents for structured reasoning"""
    
    def __init__(self):
        self.thinking_stages = [
            "Problem Definition",
            "Research", 
            "Analysis",
            "Synthesis",
            "Conclusion"
        ]
        self.thought_history = []
    
    async def think_through_task(self, task_description: str, 
                                agent_type: str,
                                context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Guide agent through sequential thinking process
        
        Args:
            task_description: What the agent needs to think about
            agent_type: Type of agent (analyst, developer, etc.)
            context: Additional context for thinking
            
        Returns:
            Structured thinking result with insights and decisions
        """
        
        thinking_result = {
            "agent_type": agent_type,
            "task": task_description,
            "thoughts": [],
            "insights": [],
            "decisions": [],
            "next_actions": []
        }
        
        # Problem Definition Stage
        problem_thought = await self._process_thought(
            thought=f"Understanding the task: {task_description}",
            stage="Problem Definition",
            agent_type=agent_type
        )
        thinking_result["thoughts"].append(problem_thought)
        
        # Research Stage - What do we need to know?
        if context and context.get("files"):
            research_thought = await self._process_thought(
                thought=f"Analyzing {len(context['files'])} files for relevant patterns",
                stage="Research",
                agent_type=agent_type,
                context=context
            )
            thinking_result["thoughts"].append(research_thought)
        
        # Analysis Stage - Break down the problem
        analysis_thought = await self._process_thought(
            thought=self._generate_analysis_thought(task_description, agent_type),
            stage="Analysis", 
            agent_type=agent_type
        )
        thinking_result["thoughts"].append(analysis_thought)
        thinking_result["insights"] = analysis_thought.get("insights", [])
        
        # Synthesis Stage - Combine insights
        synthesis_thought = await self._process_thought(
            thought="Combining insights to form a complete solution approach",
            stage="Synthesis",
            agent_type=agent_type,
            previous_thoughts=thinking_result["thoughts"]
        )
        thinking_result["thoughts"].append(synthesis_thought)
        thinking_result["decisions"] = synthesis_thought.get("decisions", [])
        
        # Conclusion Stage - Final recommendations
        conclusion_thought = await self._process_thought(
            thought="Finalizing approach and identifying next steps",
            stage="Conclusion",
            agent_type=agent_type
        )
        thinking_result["thoughts"].append(conclusion_thought)
        thinking_result["next_actions"] = conclusion_thought.get("next_actions", [])
        
        # Store in history
        self.thought_history.append(thinking_result)
        
        return thinking_result
    
    async def _process_thought(self, thought: str, stage: str, 
                             agent_type: str,
                             context: Dict[str, Any] = None,
                             previous_thoughts: List[Dict] = None) -> Dict[str, Any]:
        """
        Process a single thought through Sequential Thinking
        
        In real implementation, this would call the Sequential Thinking MCP
        """
        
        # Simulate Sequential Thinking MCP call
        # In production: await mcp_sequential_thinking.process_thought(...)
        
        result = {
            "thought": thought,
            "stage": stage,
            "agent_type": agent_type,
            "timestamp": self._get_timestamp()
        }
        
        # Stage-specific processing
        if stage == "Problem Definition":
            result["problem_components"] = self._extract_problem_components(thought)
            
        elif stage == "Research":
            if context and context.get("files"):
                result["relevant_files"] = list(context["files"].keys())
                result["patterns_found"] = self._find_patterns(context["files"])
                
        elif stage == "Analysis":
            result["insights"] = self._generate_insights(thought, agent_type)
            result["complexity_factors"] = self._analyze_complexity(thought)
            
        elif stage == "Synthesis":
            result["decisions"] = self._synthesize_decisions(previous_thoughts)
            result["approach"] = self._determine_approach(agent_type)
            
        elif stage == "Conclusion":
            result["next_actions"] = self._generate_next_actions(agent_type)
            result["success_criteria"] = self._define_success_criteria()
        
        return result
    
    def _generate_analysis_thought(self, task: str, agent_type: str) -> str:
        """Generate agent-specific analysis thought"""
        
        if agent_type == "analyst":
            return f"Analyzing architectural implications and system-wide impact of: {task}"
        elif agent_type == "developer":
            return f"Breaking down implementation requirements for: {task}"
        elif agent_type == "reviewer":
            return f"Identifying potential issues and quality concerns in: {task}"
        elif agent_type == "synthesis":
            return f"Analyzing how to merge multiple perspectives on: {task}"
        else:
            return f"Analyzing task requirements: {task}"
    
    def _extract_problem_components(self, thought: str) -> List[str]:
        """Extract key components from problem definition"""
        components = []
        
        # Keywords that indicate problem components
        keywords = ["implement", "fix", "refactor", "analyze", "create", "update", "review"]
        
        for keyword in keywords:
            if keyword in thought.lower():
                components.append(f"{keyword}_required")
        
        return components
    
    def _find_patterns(self, files: Dict[str, str]) -> List[str]:
        """Find patterns in provided files"""
        patterns = []
        
        for filepath, content in files.items():
            if "class" in content:
                patterns.append("object_oriented_design")
            if "async" in content:
                patterns.append("asynchronous_code")
            if "test" in filepath.lower():
                patterns.append("test_coverage_exists")
                
        return list(set(patterns))
    
    def _generate_insights(self, thought: str, agent_type: str) -> List[str]:
        """Generate insights based on agent type"""
        insights = []
        
        if agent_type == "analyst":
            insights.extend([
                "Consider system-wide implications",
                "Evaluate performance impact",
                "Check for architectural consistency"
            ])
        elif agent_type == "developer":
            insights.extend([
                "Follow existing code patterns",
                "Ensure backward compatibility",
                "Add appropriate error handling"
            ])
        elif agent_type == "reviewer":
            insights.extend([
                "Verify security best practices",
                "Check for potential vulnerabilities",
                "Ensure code quality standards"
            ])
            
        return insights
    
    def _analyze_complexity(self, thought: str) -> Dict[str, Any]:
        """Analyze complexity factors"""
        return {
            "technical_debt": "low" if "simple" in thought else "medium",
            "dependencies": "few" if "isolated" in thought else "multiple",
            "risk_level": "low" if "typo" in thought else "medium"
        }
    
    def _synthesize_decisions(self, previous_thoughts: List[Dict]) -> List[str]:
        """Synthesize decisions from previous thoughts"""
        decisions = []
        
        # Extract insights from all thoughts
        all_insights = []
        for thought in previous_thoughts:
            all_insights.extend(thought.get("insights", []))
        
        # Generate decisions
        if "system-wide implications" in str(all_insights):
            decisions.append("Requires comprehensive testing")
        if "security" in str(all_insights):
            decisions.append("Needs security review before deployment")
            
        decisions.append("Proceed with implementation following established patterns")
        
        return decisions
    
    def _determine_approach(self, agent_type: str) -> str:
        """Determine approach based on agent type"""
        approaches = {
            "analyst": "Deep analysis with focus on system architecture",
            "developer": "Incremental implementation with testing",
            "reviewer": "Comprehensive review focusing on security and quality",
            "synthesis": "Merge and reconcile different perspectives"
        }
        return approaches.get(agent_type, "Standard approach")
    
    def _generate_next_actions(self, agent_type: str) -> List[str]:
        """Generate next actions"""
        base_actions = [
            "Execute planned approach",
            "Document findings",
            "Report results to orchestrator"
        ]
        
        if agent_type == "developer":
            base_actions.append("Write unit tests")
        elif agent_type == "reviewer":
            base_actions.append("Create review report")
            
        return base_actions
    
    def _define_success_criteria(self) -> List[str]:
        """Define success criteria"""
        return [
            "Task completed without errors",
            "All tests passing",
            "Code follows established patterns",
            "Documentation updated"
        ]
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
    
    def get_thinking_summary(self, orchestration_id: str = None) -> Dict[str, Any]:
        """Get summary of thinking processes"""
        
        if orchestration_id:
            relevant_thoughts = [
                t for t in self.thought_history 
                if t.get("orchestration_id") == orchestration_id
            ]
        else:
            relevant_thoughts = self.thought_history
        
        return {
            "total_thinking_sessions": len(relevant_thoughts),
            "stages_covered": list(set(
                thought["stage"] 
                for session in relevant_thoughts 
                for thought in session["thoughts"]
            )),
            "insights_generated": sum(
                len(session.get("insights", [])) 
                for session in relevant_thoughts
            ),
            "decisions_made": sum(
                len(session.get("decisions", [])) 
                for session in relevant_thoughts
            )
        }


# Singleton instance
_thinking_integration = None

def get_thinking_integration() -> SequentialThinkingIntegration:
    """Get or create thinking integration instance"""
    global _thinking_integration
    if _thinking_integration is None:
        _thinking_integration = SequentialThinkingIntegration()
    return _thinking_integration