"""
Analyst Agent - Problem Decomposition and Research

Specializes in analyzing problems, breaking them into work packages,
and conducting research using Gemini MCP for deep analysis.
"""

import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime

from .enhanced_agent_base import EnhancedAgentBase
from ..routing import TaskType


class AnalystAgent(EnhancedAgentBase):
    """Agent specialized for analysis and problem decomposition"""
    
    def __init__(self, work_package: str = None, **kwargs):
        super().__init__(
            agent_type="analyst",
            work_package=work_package,
            **kwargs
        )
        
        # Analysis-specific state
        self.analysis_results = {}
        self.work_packages = []
        self.research_cache = {}
    
    async def initialize(self):
        """Initialize analyst environment"""
        self.log("Initializing analyst agent...")
        
        # Register task handlers
        self.register_task_handler("analyze", self.analyze_problem)
        self.register_task_handler("decompose", self.decompose_task)
        self.register_task_handler("research", self.conduct_research)
        self.register_task_handler("pattern_extract", self.extract_patterns)
        self.register_task_handler("complexity_assess", self.assess_complexity)
        
        # Set model preference for analysis
        # Gemini MCP is preferred for its 1M token context
        self.model_selector.preferences["prefer_fast_models"] = True
    
    async def run(self):
        """Main analyst loop"""
        while self.active:
            if self.tasks:
                task = self.tasks.pop(0)
                try:
                    result = await self.execute_task(task)
                    await self.report_task_completion(task["id"], result)
                except Exception as e:
                    self.log(f"Task failed: {e}", "ERROR")
            else:
                await asyncio.sleep(1)
    
    async def cleanup(self):
        """Clean up analyst resources"""
        self.log("Cleaning up analyst agent...")
        
        # Save analysis results
        if self.analysis_results:
            await self._save_analysis_results()
    
    async def analyze_problem(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze a problem and break it into components"""
        problem = task.get("problem", "")
        self.log(f"Analyzing problem: {problem[:100]}...")
        
        # Route to Gemini for deep analysis
        self.force_model("gemini-mcp")
        
        # Simulate analysis phases
        analysis_phases = [
            "Understanding requirements",
            "Identifying constraints",
            "Mapping dependencies",
            "Evaluating complexity",
            "Proposing solutions"
        ]
        
        results = {
            "problem": problem,
            "phases": {},
            "recommendations": [],
            "work_packages": []
        }
        
        for phase in analysis_phases:
            self.log(f"Phase: {phase}")
            self.report_progress(
                (analysis_phases.index(phase) + 1) / len(analysis_phases) * 100,
                phase
            )
            
            # Simulate phase execution
            await asyncio.sleep(0.5)
            
            results["phases"][phase] = {
                "status": "completed",
                "findings": f"Analysis results for {phase}"
            }
        
        # Generate work packages
        work_packages = await self._generate_work_packages(problem)
        results["work_packages"] = work_packages
        self.work_packages.extend(work_packages)
        
        # Store results
        self.analysis_results[task["id"]] = results
        
        return {
            "status": "completed",
            "work_package_count": len(work_packages),
            "complexity": "medium",
            "estimated_effort": "3-5 days",
            "model_used": self.current_model
        }
    
    async def decompose_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Decompose a large task into smaller subtasks"""
        main_task = task.get("main_task", "")
        self.log(f"Decomposing task: {main_task}")
        
        # Analyze task complexity first
        analysis = await self.analyze_task(main_task, task)
        
        subtasks = []
        
        if analysis.complexity_level.value >= 3:  # Complex or Critical
            # Create multiple subtasks
            subtask_count = min(5, analysis.complexity_score // 3)
            
            for i in range(subtask_count):
                subtask = {
                    "id": f"{task['id']}_sub_{i}",
                    "description": f"Subtask {i+1} of {main_task}",
                    "type": "implement",
                    "priority": task.get("priority", "medium"),
                    "dependencies": [f"{task['id']}_sub_{i-1}"] if i > 0 else [],
                    "estimated_complexity": "simple"
                }
                subtasks.append(subtask)
        else:
            # Simple task, minimal decomposition
            subtasks.append({
                "id": f"{task['id']}_impl",
                "description": f"Implement {main_task}",
                "type": "implement",
                "priority": task.get("priority", "medium"),
                "dependencies": [],
                "estimated_complexity": "simple"
            })
        
        self.log(f"Decomposed into {len(subtasks)} subtasks")
        
        return {
            "status": "completed",
            "subtasks": subtasks,
            "total_complexity": analysis.complexity_score,
            "recommended_agents": self._recommend_agents(subtasks)
        }
    
    async def conduct_research(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Conduct research on a topic"""
        topic = task.get("topic", "")
        self.log(f"Researching: {topic}")
        
        # Check cache
        if topic in self.research_cache:
            self.log("Using cached research results")
            return self.research_cache[topic]
        
        # Route to Gemini for research (large context window)
        self.force_model("gemini-mcp")
        
        # Simulate research steps
        research_steps = [
            "Searching documentation",
            "Analyzing code patterns",
            "Reviewing best practices", 
            "Checking constraints",
            "Compiling findings"
        ]
        
        findings = []
        
        for step in research_steps:
            self.log(f"Research step: {step}")
            await asyncio.sleep(0.3)
            
            findings.append({
                "step": step,
                "finding": f"Research finding from {step}",
                "confidence": 0.85
            })
        
        result = {
            "status": "completed",
            "topic": topic,
            "findings": findings,
            "sources": ["codebase", "documentation", "patterns"],
            "recommendations": self._generate_recommendations(findings)
        }
        
        # Cache results
        self.research_cache[topic] = result
        
        return result
    
    async def extract_patterns(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Extract patterns from analysis results"""
        self.log("Extracting patterns from analysis...")
        
        patterns = []
        
        # Extract from all analysis results
        for analysis_id, results in self.analysis_results.items():
            # Look for common patterns
            if "work_packages" in results:
                for wp in results["work_packages"]:
                    pattern = {
                        "type": wp.get("type", "unknown"),
                        "complexity": wp.get("complexity", "medium"),
                        "frequency": 1
                    }
                    
                    # Check if pattern exists
                    existing = next((p for p in patterns if p["type"] == pattern["type"]), None)
                    if existing:
                        existing["frequency"] += 1
                    else:
                        patterns.append(pattern)
        
        # Sort by frequency
        patterns.sort(key=lambda p: p["frequency"], reverse=True)
        
        # Store patterns for Graphiti
        graphiti_patterns = [
            {
                "pattern": p["type"],
                "frequency": p["frequency"],
                "complexity": p["complexity"],
                "extracted_at": datetime.now().isoformat()
            }
            for p in patterns[:10]  # Top 10 patterns
        ]
        
        return {
            "status": "completed",
            "patterns_found": len(patterns),
            "top_patterns": patterns[:5],
            "graphiti_ready": graphiti_patterns
        }
    
    async def assess_complexity(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Assess overall project complexity"""
        self.log("Assessing overall complexity...")
        
        # Aggregate complexity from all work packages
        total_complexity = 0
        complexity_breakdown = {
            "trivial": 0,
            "simple": 0,
            "medium": 0,
            "complex": 0,
            "critical": 0
        }
        
        for wp in self.work_packages:
            # Analyze each work package
            analysis = await self.analyze_task(
                wp.get("description", ""),
                wp
            )
            
            total_complexity += analysis.complexity_score
            complexity_breakdown[analysis.complexity_level.name.lower()] += 1
        
        # Calculate metrics
        avg_complexity = total_complexity / len(self.work_packages) if self.work_packages else 0
        
        # Determine overall level
        if avg_complexity > 12:
            overall_level = "critical"
        elif avg_complexity > 8:
            overall_level = "complex"
        elif avg_complexity > 5:
            overall_level = "medium"
        elif avg_complexity > 3:
            overall_level = "simple"
        else:
            overall_level = "trivial"
        
        return {
            "status": "completed",
            "total_work_packages": len(self.work_packages),
            "total_complexity_score": total_complexity,
            "average_complexity": round(avg_complexity, 2),
            "overall_level": overall_level,
            "breakdown": complexity_breakdown,
            "recommendations": {
                "parallel_agents": 3 if overall_level in ["complex", "critical"] else 1,
                "estimated_time": f"{len(self.work_packages) * 2} hours",
                "risk_level": "high" if overall_level == "critical" else "medium"
            }
        }
    
    def _generate_work_packages(self, problem: str) -> List[Dict[str, Any]]:
        """Generate work packages from problem analysis"""
        # Simple heuristic for demo
        work_packages = []
        
        # Common work package patterns
        if "refactor" in problem.lower():
            work_packages.extend([
                {"id": "wp_analysis", "type": "analysis", "description": "Analyze current implementation"},
                {"id": "wp_design", "type": "design", "description": "Design refactored structure"},
                {"id": "wp_implement", "type": "implement", "description": "Implement refactoring"},
                {"id": "wp_test", "type": "test", "description": "Test refactored code"}
            ])
        elif "feature" in problem.lower():
            work_packages.extend([
                {"id": "wp_spec", "type": "specification", "description": "Define feature specifications"},
                {"id": "wp_implement", "type": "implement", "description": "Implement feature"},
                {"id": "wp_integrate", "type": "integration", "description": "Integrate with existing code"},
                {"id": "wp_document", "type": "document", "description": "Document feature"}
            ])
        else:
            work_packages.append({
                "id": "wp_general",
                "type": "general",
                "description": f"Complete task: {problem[:50]}..."
            })
        
        return work_packages
    
    def _recommend_agents(self, subtasks: List[Dict[str, Any]]) -> Dict[str, int]:
        """Recommend agents for subtasks"""
        recommendations = {
            "developer": 0,
            "reviewer": 0,
            "synthesis": 0
        }
        
        for subtask in subtasks:
            if subtask["type"] in ["implement", "refactor"]:
                recommendations["developer"] += 1
            elif subtask["type"] in ["test", "review"]:
                recommendations["reviewer"] += 1
        
        # Always need synthesis for multiple subtasks
        if len(subtasks) > 1:
            recommendations["synthesis"] = 1
        
        return recommendations
    
    def _generate_recommendations(self, findings: List[Dict[str, Any]]) -> List[str]:
        """Generate recommendations from research findings"""
        recommendations = []
        
        for finding in findings:
            if finding["confidence"] > 0.8:
                recommendations.append(
                    f"Consider {finding['step']} results: {finding['finding']}"
                )
        
        return recommendations[:5]  # Top 5 recommendations
    
    async def _save_analysis_results(self):
        """Save analysis results to file"""
        import json
        from pathlib import Path
        
        results_dir = Path(self.lifecycle.workspace) / "results"
        results_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = results_dir / f"analysis_{timestamp}.json"
        
        with open(results_file, 'w') as f:
            json.dump({
                "agent_id": self.agent_id,
                "work_package": self.work_package,
                "analysis_results": self.analysis_results,
                "work_packages": self.work_packages,
                "model_stats": self.get_model_stats()
            }, f, indent=2)
        
        self.log(f"Analysis results saved to {results_file}")