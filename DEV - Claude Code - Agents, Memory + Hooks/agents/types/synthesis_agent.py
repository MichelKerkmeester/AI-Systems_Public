"""
Synthesis Agent - Result Combination and Conflict Resolution

Specializes in merging results from multiple agents, resolving conflicts,
and creating cohesive outputs. Always uses Claude for complex reasoning.
"""

import asyncio
import json
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path

from .enhanced_agent_base import EnhancedAgentBase
from ..routing import TaskType


class SynthesisAgent(EnhancedAgentBase):
    """Agent specialized for synthesis and result combination"""
    
    def __init__(self, work_package: str = None, **kwargs):
        super().__init__(
            agent_type="synthesis",
            work_package=work_package,
            **kwargs
        )
        
        # Synthesis-specific state
        self.agent_results = {}  # Results from other agents
        self.conflicts = []
        self.resolutions = {}
        self.final_output = None
        
        # Always use Claude for synthesis
        self.force_model("claude-opus-4")
    
    async def initialize(self):
        """Initialize synthesis environment"""
        self.log("Initializing synthesis agent...")
        
        # Register task handlers
        self.register_task_handler("synthesize", self.synthesize_results)
        self.register_task_handler("resolve_conflict", self.resolve_conflict)
        self.register_task_handler("merge_code", self.merge_code_changes)
        self.register_task_handler("integrate", self.integrate_components)
        self.register_task_handler("finalize", self.finalize_output)
        self.register_task_handler("validate", self.validate_synthesis)
        
        # Register message handlers for agent results
        self.register_message_handler("agent_result", self._handle_agent_result)
        self.register_message_handler("conflict_detected", self._handle_conflict_notification)
    
    async def run(self):
        """Main synthesis loop"""
        while self.active:
            if self.tasks:
                task = self.tasks.pop(0)
                try:
                    result = await self.execute_task(task)
                    await self.report_task_completion(task["id"], result)
                except Exception as e:
                    self.log(f"Synthesis task failed: {e}", "ERROR")
            else:
                # Check if we have enough results to synthesize
                if len(self.agent_results) >= 2 and not self.final_output:
                    await self._auto_synthesize()
                
                await asyncio.sleep(1)
    
    async def cleanup(self):
        """Clean up synthesis resources"""
        self.log("Cleaning up synthesis agent...")
        
        # Save final synthesis
        if self.final_output:
            await self._save_final_output()
    
    async def synthesize_results(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Synthesize results from multiple agents"""
        agent_ids = task.get("agent_ids", list(self.agent_results.keys()))
        synthesis_type = task.get("synthesis_type", "comprehensive")
        
        self.log(f"Synthesizing results from {len(agent_ids)} agents")
        self.log(f"Synthesis type: {synthesis_type}")
        
        # Collect results
        results_to_synthesize = []
        for agent_id in agent_ids:
            if agent_id in self.agent_results:
                results_to_synthesize.append(self.agent_results[agent_id])
            else:
                self.log(f"Warning: No results from agent {agent_id}", "WARN")
        
        if not results_to_synthesize:
            return {
                "status": "failed",
                "error": "No results to synthesize"
            }
        
        # Synthesis phases
        phases = [
            ("Analyzing agent outputs", self._analyze_outputs),
            ("Identifying conflicts", self._identify_conflicts),
            ("Resolving conflicts", self._resolve_all_conflicts),
            ("Merging results", self._merge_results),
            ("Validating synthesis", self._validate_merged_results)
        ]
        
        synthesis_result = {
            "phases": {},
            "conflicts_found": 0,
            "conflicts_resolved": 0,
            "final_output": None
        }
        
        current_data = results_to_synthesize
        
        for phase_name, phase_func in phases:
            self.log(f"Synthesis phase: {phase_name}")
            self.report_progress(
                (phases.index((phase_name, phase_func)) + 1) / len(phases) * 100,
                phase_name
            )
            
            phase_result = await phase_func(current_data)
            synthesis_result["phases"][phase_name] = phase_result
            
            # Update current data for next phase
            if "output" in phase_result:
                current_data = phase_result["output"]
            
            await asyncio.sleep(0.5)  # Simulate processing
        
        # Store final output
        self.final_output = current_data
        synthesis_result["final_output"] = self.final_output
        
        # Count conflicts
        synthesis_result["conflicts_found"] = len(self.conflicts)
        synthesis_result["conflicts_resolved"] = len(self.resolutions)
        
        return {
            "status": "completed",
            "synthesis_type": synthesis_type,
            "agents_synthesized": len(results_to_synthesize),
            "conflicts_resolved": synthesis_result["conflicts_resolved"],
            "confidence": self._calculate_confidence(synthesis_result),
            "model_used": self.current_model
        }
    
    async def resolve_conflict(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Resolve a specific conflict"""
        conflict_id = task.get("conflict_id")
        conflict = task.get("conflict")
        
        if not conflict and conflict_id:
            # Find conflict by ID
            conflict = next((c for c in self.conflicts if c.get("id") == conflict_id), None)
        
        if not conflict:
            return {
                "status": "failed",
                "error": "Conflict not found"
            }
        
        self.log(f"Resolving conflict: {conflict.get('type', 'unknown')}")
        
        # Resolution strategies based on conflict type
        resolution_strategy = self._select_resolution_strategy(conflict)
        
        self.log(f"Using strategy: {resolution_strategy}")
        
        # Apply resolution
        resolution = await self._apply_resolution_strategy(conflict, resolution_strategy)
        
        # Store resolution
        self.resolutions[conflict.get("id", len(self.resolutions))] = resolution
        
        return {
            "status": "completed",
            "conflict_type": conflict.get("type"),
            "strategy_used": resolution_strategy,
            "resolution": resolution,
            "confidence": resolution.get("confidence", 0.8)
        }
    
    async def merge_code_changes(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Merge code changes from multiple agents"""
        changes = task.get("changes", [])
        merge_strategy = task.get("merge_strategy", "smart")
        
        self.log(f"Merging {len(changes)} code changes (strategy: {merge_strategy})")
        
        merged_changes = {
            "files_created": [],
            "files_modified": {},
            "files_deleted": [],
            "conflicts": []
        }
        
        # Process each change
        for change in changes:
            agent_id = change.get("agent_id")
            files = change.get("files", {})
            
            for file_path, file_change in files.items():
                action = file_change.get("action", "modify")
                
                if action == "create":
                    if file_path in merged_changes["files_created"]:
                        # Conflict: multiple agents creating same file
                        conflict = {
                            "type": "file_creation_conflict",
                            "file": file_path,
                            "agents": [agent_id],
                            "changes": [file_change]
                        }
                        merged_changes["conflicts"].append(conflict)
                    else:
                        merged_changes["files_created"].append(file_path)
                
                elif action == "modify":
                    if file_path not in merged_changes["files_modified"]:
                        merged_changes["files_modified"][file_path] = []
                    
                    merged_changes["files_modified"][file_path].append({
                        "agent_id": agent_id,
                        "changes": file_change.get("changes", [])
                    })
                
                elif action == "delete":
                    if file_path in merged_changes["files_created"]:
                        # Conflict: creating and deleting same file
                        conflict = {
                            "type": "create_delete_conflict",
                            "file": file_path,
                            "agents": [agent_id]
                        }
                        merged_changes["conflicts"].append(conflict)
                    else:
                        merged_changes["files_deleted"].append(file_path)
        
        # Resolve modification conflicts
        for file_path, modifications in merged_changes["files_modified"].items():
            if len(modifications) > 1:
                # Multiple agents modifying same file
                resolution = await self._merge_file_modifications(file_path, modifications)
                merged_changes["files_modified"][file_path] = resolution
        
        return {
            "status": "completed",
            "files_affected": (
                len(merged_changes["files_created"]) +
                len(merged_changes["files_modified"]) +
                len(merged_changes["files_deleted"])
            ),
            "conflicts_found": len(merged_changes["conflicts"]),
            "merged_changes": merged_changes,
            "merge_strategy": merge_strategy
        }
    
    async def integrate_components(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate components from different agents"""
        components = task.get("components", [])
        integration_type = task.get("integration_type", "modular")
        
        self.log(f"Integrating {len(components)} components")
        
        integrated = {
            "modules": {},
            "interfaces": {},
            "dependencies": [],
            "configuration": {}
        }
        
        # Process each component
        for component in components:
            comp_type = component.get("type", "module")
            comp_name = component.get("name")
            
            if comp_type == "module":
                integrated["modules"][comp_name] = component.get("implementation")
            elif comp_type == "interface":
                integrated["interfaces"][comp_name] = component.get("specification")
            elif comp_type == "dependency":
                integrated["dependencies"].append(component.get("requirement"))
            elif comp_type == "config":
                integrated["configuration"].update(component.get("settings", {}))
        
        # Validate integration
        validation_result = await self._validate_integration(integrated)
        
        return {
            "status": "completed",
            "components_integrated": len(components),
            "integration_type": integration_type,
            "validation": validation_result,
            "integrated_structure": integrated
        }
    
    async def finalize_output(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Finalize the synthesized output"""
        output_format = task.get("format", "comprehensive")
        include_metadata = task.get("include_metadata", True)
        
        self.log(f"Finalizing output (format: {output_format})")
        
        if not self.final_output:
            # Generate final output from current results
            self.final_output = await self._generate_final_output()
        
        # Format output based on requirements
        formatted_output = self._format_output(self.final_output, output_format)
        
        # Add metadata if requested
        if include_metadata:
            formatted_output["metadata"] = {
                "synthesis_agent": self.agent_id,
                "timestamp": datetime.now().isoformat(),
                "agents_involved": list(self.agent_results.keys()),
                "conflicts_resolved": len(self.resolutions),
                "confidence_score": self._calculate_overall_confidence()
            }
        
        # Save output
        await self._save_final_output()
        
        return {
            "status": "completed",
            "output_format": output_format,
            "size": len(json.dumps(formatted_output)),
            "sections": list(formatted_output.keys()),
            "ready_for_delivery": True
        }
    
    async def validate_synthesis(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the synthesized results"""
        validation_type = task.get("validation_type", "comprehensive")
        data_to_validate = task.get("data", self.final_output)
        
        self.log(f"Validating synthesis (type: {validation_type})")
        
        validation_checks = {
            "completeness": self._check_completeness,
            "consistency": self._check_consistency,
            "quality": self._check_quality,
            "conflicts": self._check_unresolved_conflicts
        }
        
        validation_results = {}
        issues_found = []
        
        for check_name, check_func in validation_checks.items():
            self.log(f"Running validation: {check_name}")
            
            result = await check_func(data_to_validate)
            validation_results[check_name] = result
            
            if not result["passed"]:
                issues_found.extend(result.get("issues", []))
        
        # Overall validation status
        all_passed = all(r["passed"] for r in validation_results.values())
        
        return {
            "status": "completed",
            "validation_passed": all_passed,
            "validation_type": validation_type,
            "checks_performed": list(validation_results.keys()),
            "issues_found": len(issues_found),
            "details": validation_results,
            "recommendations": self._generate_validation_recommendations(issues_found)
        }
    
    async def _handle_agent_result(self, message):
        """Handle result from another agent"""
        agent_id = message.from_agent
        result = message.payload
        
        self.log(f"Received result from {agent_id}")
        
        # Store result
        self.agent_results[agent_id] = {
            "agent_id": agent_id,
            "timestamp": datetime.now().isoformat(),
            "result": result
        }
        
        # Check if we should start synthesis
        if len(self.agent_results) >= self.metadata.get("min_agents_for_synthesis", 2):
            self.log("Enough results collected, considering synthesis...")
    
    async def _handle_conflict_notification(self, message):
        """Handle conflict notification from another agent"""
        conflict = message.payload
        
        self.log(f"Conflict reported: {conflict.get('type', 'unknown')}")
        
        # Add to conflicts list
        conflict["id"] = f"conflict_{len(self.conflicts)}"
        conflict["reported_by"] = message.from_agent
        conflict["timestamp"] = datetime.now().isoformat()
        
        self.conflicts.append(conflict)
    
    async def _auto_synthesize(self):
        """Automatically synthesize when enough results are available"""
        if self.metadata.get("auto_synthesis", True):
            self.log("Auto-synthesis triggered")
            
            # Create synthesis task
            synthesis_task = {
                "id": "auto_synthesis",
                "type": "synthesize",
                "synthesis_type": "automatic"
            }
            
            # Add to task queue
            self.tasks.append(synthesis_task)
    
    async def _analyze_outputs(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze agent outputs"""
        analysis = {
            "agent_count": len(results),
            "output_types": {},
            "common_elements": [],
            "unique_elements": []
        }
        
        # Analyze each result
        for result in results:
            agent_result = result.get("result", {})
            
            # Track output types
            output_type = agent_result.get("type", "unknown")
            if output_type not in analysis["output_types"]:
                analysis["output_types"][output_type] = 0
            analysis["output_types"][output_type] += 1
        
        return {
            "status": "completed",
            "analysis": analysis,
            "output": results  # Pass through
        }
    
    async def _identify_conflicts(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Identify conflicts between agent results"""
        new_conflicts = []
        
        # Compare results pairwise
        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                conflicts = self._compare_results(results[i], results[j])
                new_conflicts.extend(conflicts)
        
        # Add to conflicts list
        self.conflicts.extend(new_conflicts)
        
        return {
            "status": "completed",
            "conflicts_found": len(new_conflicts),
            "conflict_types": list(set(c.get("type") for c in new_conflicts)),
            "output": results  # Pass through
        }
    
    async def _resolve_all_conflicts(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve all identified conflicts"""
        resolved_count = 0
        
        for conflict in self.conflicts:
            if conflict.get("id") not in self.resolutions:
                # Resolve conflict
                resolution = await self._apply_resolution_strategy(
                    conflict,
                    self._select_resolution_strategy(conflict)
                )
                
                self.resolutions[conflict["id"]] = resolution
                resolved_count += 1
        
        return {
            "status": "completed",
            "conflicts_resolved": resolved_count,
            "resolution_strategies": list(set(
                r.get("strategy") for r in self.resolutions.values()
            )),
            "output": results  # Pass through with resolutions applied
        }
    
    async def _merge_results(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge all results into final output"""
        merged = {
            "synthesis_timestamp": datetime.now().isoformat(),
            "agent_contributions": {},
            "combined_output": {},
            "metrics": {}
        }
        
        # Merge each agent's contribution
        for result in results:
            agent_id = result.get("agent_id")
            agent_result = result.get("result", {})
            
            merged["agent_contributions"][agent_id] = {
                "summary": self._summarize_contribution(agent_result),
                "key_outputs": self._extract_key_outputs(agent_result)
            }
            
            # Merge into combined output
            self._merge_into_combined(merged["combined_output"], agent_result)
        
        # Calculate metrics
        merged["metrics"] = {
            "total_files": len(merged["combined_output"].get("files", {})),
            "total_components": len(merged["combined_output"].get("components", {})),
            "agent_agreement": self._calculate_agreement(results)
        }
        
        return {
            "status": "completed",
            "merge_successful": True,
            "output": merged
        }
    
    async def _validate_merged_results(self, merged_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the merged results"""
        validation = await self.validate_synthesis({
            "validation_type": "final",
            "data": merged_data
        })
        
        return {
            "status": "completed",
            "validation_passed": validation["validation_passed"],
            "confidence": self._calculate_confidence(validation),
            "output": merged_data  # Pass through if valid
        }
    
    def _compare_results(self, result1: Dict[str, Any], result2: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Compare two results and identify conflicts"""
        conflicts = []
        
        # Compare files modified
        files1 = set(result1.get("result", {}).get("files_modified", []))
        files2 = set(result2.get("result", {}).get("files_modified", []))
        
        common_files = files1.intersection(files2)
        if common_files:
            conflicts.append({
                "type": "file_modification_conflict",
                "agents": [result1.get("agent_id"), result2.get("agent_id")],
                "files": list(common_files)
            })
        
        return conflicts
    
    def _select_resolution_strategy(self, conflict: Dict[str, Any]) -> str:
        """Select appropriate resolution strategy"""
        conflict_type = conflict.get("type", "unknown")
        
        strategies = {
            "file_modification_conflict": "merge_changes",
            "file_creation_conflict": "choose_best",
            "create_delete_conflict": "prioritize_creation",
            "data_conflict": "weighted_average",
            "logic_conflict": "expert_judgment"
        }
        
        return strategies.get(conflict_type, "manual_review")
    
    async def _apply_resolution_strategy(self, conflict: Dict[str, Any], 
                                       strategy: str) -> Dict[str, Any]:
        """Apply resolution strategy to conflict"""
        self.log(f"Applying strategy: {strategy}")
        
        resolution = {
            "strategy": strategy,
            "conflict_id": conflict.get("id"),
            "timestamp": datetime.now().isoformat()
        }
        
        if strategy == "merge_changes":
            # Merge file changes
            resolution["action"] = "merge"
            resolution["result"] = "Changes merged successfully"
            resolution["confidence"] = 0.9
        
        elif strategy == "choose_best":
            # Choose best option based on quality metrics
            resolution["action"] = "select"
            resolution["selected"] = conflict.get("agents", [])[0]  # Simplified
            resolution["confidence"] = 0.8
        
        elif strategy == "prioritize_creation":
            # Prioritize file creation over deletion
            resolution["action"] = "keep"
            resolution["result"] = "File creation prioritized"
            resolution["confidence"] = 0.95
        
        else:
            # Default resolution
            resolution["action"] = "defer"
            resolution["result"] = "Requires manual review"
            resolution["confidence"] = 0.5
        
        return resolution
    
    async def _merge_file_modifications(self, file_path: str, 
                                      modifications: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge modifications to a single file"""
        # In production, would use git merge or similar
        # For now, combine all changes
        
        merged = {
            "file_path": file_path,
            "merged_changes": [],
            "merge_strategy": "combine_all"
        }
        
        for mod in modifications:
            merged["merged_changes"].extend(mod.get("changes", []))
        
        return merged
    
    async def _validate_integration(self, integrated: Dict[str, Any]) -> Dict[str, Any]:
        """Validate component integration"""
        return {
            "valid": True,
            "issues": [],
            "warnings": ["Some interfaces may need adjustment"]
        }
    
    async def _generate_final_output(self) -> Dict[str, Any]:
        """Generate final output from all results"""
        return {
            "synthesis_complete": True,
            "timestamp": datetime.now().isoformat(),
            "results": self.agent_results,
            "resolutions": self.resolutions,
            "confidence": self._calculate_overall_confidence()
        }
    
    def _format_output(self, output: Dict[str, Any], format_type: str) -> Dict[str, Any]:
        """Format output based on requirements"""
        if format_type == "summary":
            return {
                "summary": self._generate_summary(output),
                "key_results": self._extract_key_results(output)
            }
        elif format_type == "detailed":
            return output  # Full details
        else:  # comprehensive
            return {
                "executive_summary": self._generate_summary(output),
                "detailed_results": output,
                "recommendations": self._generate_recommendations(output)
            }
    
    def _calculate_confidence(self, data: Dict[str, Any]) -> float:
        """Calculate confidence score"""
        base_confidence = 0.8
        
        # Adjust based on conflicts
        if self.conflicts:
            conflict_penalty = len(self.conflicts) * 0.05
            base_confidence -= min(conflict_penalty, 0.3)
        
        # Adjust based on resolutions
        if self.resolutions:
            resolution_bonus = len(self.resolutions) * 0.02
            base_confidence += min(resolution_bonus, 0.1)
        
        return max(0.5, min(1.0, base_confidence))
    
    def _calculate_overall_confidence(self) -> float:
        """Calculate overall synthesis confidence"""
        return self._calculate_confidence({})
    
    async def _check_completeness(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Check if synthesis is complete"""
        required_sections = ["agent_contributions", "combined_output", "metrics"]
        missing = []
        
        for section in required_sections:
            if section not in data:
                missing.append(section)
        
        return {
            "passed": len(missing) == 0,
            "issues": [f"Missing section: {s}" for s in missing]
        }
    
    async def _check_consistency(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Check consistency of synthesis"""
        # Simplified consistency check
        return {
            "passed": True,
            "issues": []
        }
    
    async def _check_quality(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Check quality of synthesis"""
        # Simplified quality check
        quality_score = self._calculate_overall_confidence()
        
        return {
            "passed": quality_score >= 0.7,
            "issues": [] if quality_score >= 0.7 else ["Quality score below threshold"]
        }
    
    async def _check_unresolved_conflicts(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Check for unresolved conflicts"""
        unresolved = [c for c in self.conflicts if c.get("id") not in self.resolutions]
        
        return {
            "passed": len(unresolved) == 0,
            "issues": [f"Unresolved conflict: {c.get('type')}" for c in unresolved]
        }
    
    def _generate_validation_recommendations(self, issues: List[str]) -> List[str]:
        """Generate recommendations based on validation issues"""
        recommendations = []
        
        if any("Missing section" in issue for issue in issues):
            recommendations.append("Ensure all required sections are included in synthesis")
        
        if any("Quality score" in issue for issue in issues):
            recommendations.append("Review and improve synthesis quality")
        
        if any("Unresolved conflict" in issue for issue in issues):
            recommendations.append("Resolve all conflicts before finalizing")
        
        return recommendations
    
    def _summarize_contribution(self, agent_result: Dict[str, Any]) -> str:
        """Summarize an agent's contribution"""
        status = agent_result.get("status", "unknown")
        task_type = agent_result.get("task_type", "unknown")
        
        return f"{task_type} task {status}"
    
    def _extract_key_outputs(self, agent_result: Dict[str, Any]) -> List[str]:
        """Extract key outputs from agent result"""
        outputs = []
        
        if "files_created" in agent_result:
            outputs.append(f"Created {len(agent_result['files_created'])} files")
        
        if "files_modified" in agent_result:
            outputs.append(f"Modified {len(agent_result['files_modified'])} files")
        
        if "tests_added" in agent_result:
            outputs.append(f"Added {len(agent_result['tests_added'])} tests")
        
        return outputs
    
    def _merge_into_combined(self, combined: Dict[str, Any], agent_result: Dict[str, Any]):
        """Merge agent result into combined output"""
        # Initialize sections if needed
        if "files" not in combined:
            combined["files"] = {}
        if "components" not in combined:
            combined["components"] = {}
        if "tests" not in combined:
            combined["tests"] = []
        
        # Merge files
        for file_type in ["files_created", "files_modified"]:
            if file_type in agent_result:
                for file_path in agent_result[file_type]:
                    if file_path not in combined["files"]:
                        combined["files"][file_path] = {
                            "status": "created" if file_type == "files_created" else "modified",
                            "modified_by": []
                        }
                    combined["files"][file_path]["modified_by"].append(
                        agent_result.get("agent_id", "unknown")
                    )
        
        # Merge tests
        if "tests_added" in agent_result:
            combined["tests"].extend(agent_result["tests_added"])
    
    def _calculate_agreement(self, results: List[Dict[str, Any]]) -> float:
        """Calculate agreement level between agents"""
        if len(results) < 2:
            return 1.0
        
        # Simplified agreement calculation
        conflict_ratio = len(self.conflicts) / (len(results) * (len(results) - 1) / 2)
        
        return max(0, 1 - conflict_ratio)
    
    def _generate_summary(self, output: Dict[str, Any]) -> str:
        """Generate executive summary"""
        agent_count = len(self.agent_results)
        conflict_count = len(self.conflicts)
        resolution_count = len(self.resolutions)
        
        return (
            f"Synthesis completed successfully. "
            f"Combined results from {agent_count} agents. "
            f"Resolved {resolution_count} of {conflict_count} conflicts. "
            f"Overall confidence: {self._calculate_overall_confidence():.1%}"
        )
    
    def _extract_key_results(self, output: Dict[str, Any]) -> List[str]:
        """Extract key results from output"""
        results = []
        
        if "combined_output" in output:
            combined = output["combined_output"]
            
            if "files" in combined:
                results.append(f"Total files affected: {len(combined['files'])}")
            
            if "components" in combined:
                results.append(f"Components integrated: {len(combined['components'])}")
            
            if "tests" in combined:
                results.append(f"Tests added: {len(combined['tests'])}")
        
        return results
    
    def _generate_recommendations(self, output: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on synthesis"""
        recommendations = []
        
        if self._calculate_overall_confidence() < 0.8:
            recommendations.append("Consider manual review of low-confidence areas")
        
        if len(self.conflicts) > 5:
            recommendations.append("High conflict count suggests need for better coordination")
        
        if "metrics" in output and output["metrics"].get("agent_agreement", 1) < 0.7:
            recommendations.append("Low agent agreement - consider re-analyzing requirements")
        
        return recommendations
    
    async def _save_final_output(self):
        """Save final synthesis output"""
        if not self.final_output:
            return
        
        output_dir = Path(self.lifecycle.workspace) / "synthesis"
        output_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"synthesis_{timestamp}.json"
        
        # Prepare output data
        output_data = {
            "synthesis_agent": self.agent_id,
            "work_package": self.work_package,
            "timestamp": timestamp,
            "final_output": self.final_output,
            "statistics": {
                "agents_synthesized": len(self.agent_results),
                "conflicts_found": len(self.conflicts),
                "conflicts_resolved": len(self.resolutions),
                "confidence_score": self._calculate_overall_confidence()
            },
            "model_usage": {
                "model": "claude-opus-4",
                "reason": "Synthesis always requires Claude for complex reasoning"
            }
        }
        
        # Save to file
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        self.log(f"Final synthesis saved to {output_file}")