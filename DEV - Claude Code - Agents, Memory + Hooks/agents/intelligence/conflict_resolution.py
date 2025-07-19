"""
Advanced Conflict Resolution for Multi-Agent System

Handles conflicts when multiple agents work on overlapping areas.
"""

import json
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from enum import Enum


class ConflictType(Enum):
    """Types of conflicts that can occur"""
    FILE_MODIFICATION = "file_modification"
    LOGIC_CONTRADICTION = "logic_contradiction"  
    PATTERN_VIOLATION = "pattern_violation"
    DEPENDENCY_CONFLICT = "dependency_conflict"
    RESOURCE_CONTENTION = "resource_contention"


class ConflictSeverity(Enum):
    """Severity levels for conflicts"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class ConflictResolution:
    """Advanced conflict resolution system"""
    
    def __init__(self):
        self.conflict_history = []
        self.resolution_strategies = {
            ConflictType.FILE_MODIFICATION: self._resolve_file_conflict,
            ConflictType.LOGIC_CONTRADICTION: self._resolve_logic_conflict,
            ConflictType.PATTERN_VIOLATION: self._resolve_pattern_conflict,
            ConflictType.DEPENDENCY_CONFLICT: self._resolve_dependency_conflict,
            ConflictType.RESOURCE_CONTENTION: self._resolve_resource_conflict
        }
    
    async def detect_conflicts(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Detect conflicts between multiple agent results
        
        Args:
            agent_results: Results from multiple agents
            
        Returns:
            List of detected conflicts
        """
        
        conflicts = []
        
        # Check for file modification conflicts
        file_conflicts = self._detect_file_conflicts(agent_results)
        conflicts.extend(file_conflicts)
        
        # Check for logic contradictions
        logic_conflicts = self._detect_logic_conflicts(agent_results)
        conflicts.extend(logic_conflicts)
        
        # Check for pattern violations
        pattern_conflicts = self._detect_pattern_conflicts(agent_results)
        conflicts.extend(pattern_conflicts)
        
        # Check for dependency conflicts
        dependency_conflicts = self._detect_dependency_conflicts(agent_results)
        conflicts.extend(dependency_conflicts)
        
        return conflicts
    
    async def resolve_conflicts(self, conflicts: List[Dict[str, Any]], 
                              agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Resolve detected conflicts
        
        Args:
            conflicts: List of conflicts to resolve
            agent_results: Original agent results
            
        Returns:
            Resolution result with merged/reconciled outputs
        """
        
        resolution = {
            "status": "success",
            "resolved_conflicts": [],
            "failed_resolutions": [],
            "merged_result": {},
            "resolution_log": []
        }
        
        # Sort conflicts by severity
        conflicts.sort(key=lambda c: c["severity"].value, reverse=True)
        
        # Resolve each conflict
        for conflict in conflicts:
            conflict_type = conflict["type"]
            
            if conflict_type in self.resolution_strategies:
                try:
                    resolved = await self.resolution_strategies[conflict_type](
                        conflict, agent_results
                    )
                    
                    resolution["resolved_conflicts"].append({
                        "conflict": conflict,
                        "resolution": resolved
                    })
                    
                    # Apply resolution to merged result
                    self._apply_resolution(resolution["merged_result"], resolved)
                    
                except Exception as e:
                    resolution["failed_resolutions"].append({
                        "conflict": conflict,
                        "error": str(e)
                    })
                    resolution["status"] = "partial"
        
        # Store in history
        self.conflict_history.append({
            "timestamp": datetime.now().isoformat(),
            "conflicts_count": len(conflicts),
            "resolved_count": len(resolution["resolved_conflicts"]),
            "failed_count": len(resolution["failed_resolutions"])
        })
        
        return resolution
    
    def _detect_file_conflicts(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect conflicts in file modifications"""
        
        conflicts = []
        file_modifications = {}
        
        # Collect all file modifications
        for i, result in enumerate(agent_results):
            agent_id = result.get("agent_id", f"agent_{i}")
            
            for file_change in result.get("file_changes", []):
                filepath = file_change["file"]
                
                if filepath not in file_modifications:
                    file_modifications[filepath] = []
                
                file_modifications[filepath].append({
                    "agent_id": agent_id,
                    "change": file_change
                })
        
        # Find conflicts
        for filepath, changes in file_modifications.items():
            if len(changes) > 1:
                # Multiple agents modified same file
                conflicts.append({
                    "type": ConflictType.FILE_MODIFICATION,
                    "severity": self._assess_file_conflict_severity(changes),
                    "file": filepath,
                    "agents": [c["agent_id"] for c in changes],
                    "changes": changes
                })
        
        return conflicts
    
    def _detect_logic_conflicts(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect logical contradictions between agent outputs"""
        
        conflicts = []
        
        # Check for contradictory decisions
        decisions = []
        for result in agent_results:
            agent_decisions = result.get("decisions", [])
            for decision in agent_decisions:
                decisions.append({
                    "agent_id": result.get("agent_id"),
                    "decision": decision
                })
        
        # Find contradictions
        for i, dec1 in enumerate(decisions):
            for dec2 in decisions[i+1:]:
                if self._are_contradictory(dec1["decision"], dec2["decision"]):
                    conflicts.append({
                        "type": ConflictType.LOGIC_CONTRADICTION,
                        "severity": ConflictSeverity.HIGH,
                        "agents": [dec1["agent_id"], dec2["agent_id"]],
                        "contradiction": {
                            "decision1": dec1["decision"],
                            "decision2": dec2["decision"]
                        }
                    })
        
        return conflicts
    
    def _detect_pattern_conflicts(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect violations of established patterns"""
        
        conflicts = []
        
        # Check each result against known patterns
        for result in agent_results:
            violations = []
            
            # Check code patterns
            for change in result.get("file_changes", []):
                if "console.log" in change.get("content", ""):
                    violations.append("console_log_usage")
                if "var " in change.get("content", ""):
                    violations.append("var_keyword_usage")
            
            if violations:
                conflicts.append({
                    "type": ConflictType.PATTERN_VIOLATION,
                    "severity": ConflictSeverity.MEDIUM,
                    "agent_id": result.get("agent_id"),
                    "violations": violations
                })
        
        return conflicts
    
    def _detect_dependency_conflicts(self, agent_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect dependency conflicts between agent outputs"""
        
        conflicts = []
        dependency_changes = {}
        
        # Collect dependency changes
        for result in agent_results:
            agent_id = result.get("agent_id")
            
            for dep_change in result.get("dependency_changes", []):
                dep_name = dep_change["name"]
                
                if dep_name not in dependency_changes:
                    dependency_changes[dep_name] = []
                
                dependency_changes[dep_name].append({
                    "agent_id": agent_id,
                    "change": dep_change
                })
        
        # Find conflicts
        for dep_name, changes in dependency_changes.items():
            if len(changes) > 1:
                # Check for version conflicts
                versions = [c["change"].get("version") for c in changes]
                if len(set(versions)) > 1:
                    conflicts.append({
                        "type": ConflictType.DEPENDENCY_CONFLICT,
                        "severity": ConflictSeverity.HIGH,
                        "dependency": dep_name,
                        "agents": [c["agent_id"] for c in changes],
                        "versions": versions
                    })
        
        return conflicts
    
    async def _resolve_file_conflict(self, conflict: Dict[str, Any], 
                                   agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve file modification conflicts"""
        
        filepath = conflict["file"]
        changes = conflict["changes"]
        
        # Strategy: Merge non-overlapping changes, prioritize by agent expertise
        merged_content = None
        
        # Check if changes overlap
        if self._changes_overlap(changes):
            # Use agent with highest expertise for this file type
            expert_agent = self._find_expert_agent(filepath, changes)
            merged_content = expert_agent["change"]["content"]
            
            resolution = {
                "strategy": "expert_selection",
                "selected_agent": expert_agent["agent_id"],
                "reason": f"Agent has expertise in {self._get_file_type(filepath)}"
            }
        else:
            # Merge non-overlapping changes
            merged_content = self._merge_changes(changes)
            
            resolution = {
                "strategy": "merge",
                "merged_from": [c["agent_id"] for c in changes],
                "reason": "Changes don't overlap"
            }
        
        resolution["file"] = filepath
        resolution["content"] = merged_content
        
        return resolution
    
    async def _resolve_logic_conflict(self, conflict: Dict[str, Any],
                                    agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve logical contradictions"""
        
        contradiction = conflict["contradiction"]
        
        # Strategy: Use consensus or synthesis agent judgment
        resolution = {
            "strategy": "synthesis_required",
            "contradiction": contradiction,
            "recommendation": "Synthesis agent should reconcile these contradictory decisions"
        }
        
        # Try to find middle ground
        if "performance" in str(contradiction) and "readability" in str(contradiction):
            resolution["suggested_resolution"] = "Balance performance and readability"
        
        return resolution
    
    async def _resolve_pattern_conflict(self, conflict: Dict[str, Any],
                                      agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve pattern violations"""
        
        violations = conflict["violations"]
        agent_id = conflict["agent_id"]
        
        # Strategy: Auto-fix known violations
        fixes = []
        
        for violation in violations:
            if violation == "console_log_usage":
                fixes.append({
                    "violation": violation,
                    "fix": "Remove console.log statements",
                    "auto_fixable": True
                })
            elif violation == "var_keyword_usage":
                fixes.append({
                    "violation": violation,
                    "fix": "Replace 'var' with 'const' or 'let'",
                    "auto_fixable": True
                })
        
        resolution = {
            "strategy": "auto_fix",
            "agent_id": agent_id,
            "fixes": fixes
        }
        
        return resolution
    
    async def _resolve_dependency_conflict(self, conflict: Dict[str, Any],
                                         agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve dependency version conflicts"""
        
        dependency = conflict["dependency"]
        versions = conflict["versions"]
        
        # Strategy: Use latest compatible version
        latest_version = max(versions, key=lambda v: self._parse_version(v))
        
        resolution = {
            "strategy": "latest_compatible",
            "dependency": dependency,
            "selected_version": latest_version,
            "reason": "Using latest version for compatibility"
        }
        
        return resolution
    
    async def _resolve_resource_conflict(self, conflict: Dict[str, Any],
                                       agent_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Resolve resource contention"""
        
        # Strategy: Queue or prioritize based on task importance
        resolution = {
            "strategy": "queue",
            "order": conflict.get("agents", []),
            "reason": "Agents will access resource sequentially"
        }
        
        return resolution
    
    def _assess_file_conflict_severity(self, changes: List[Dict[str, Any]]) -> ConflictSeverity:
        """Assess severity of file conflicts"""
        
        # Critical if changes to same lines
        if self._changes_overlap(changes):
            return ConflictSeverity.CRITICAL
        
        # High if structural changes
        if any("class" in c["change"].get("content", "") for c in changes):
            return ConflictSeverity.HIGH
        
        # Medium for function changes
        if any("function" in c["change"].get("content", "") for c in changes):
            return ConflictSeverity.MEDIUM
        
        return ConflictSeverity.LOW
    
    def _changes_overlap(self, changes: List[Dict[str, Any]]) -> bool:
        """Check if changes overlap in the same file"""
        
        # In real implementation, would check line ranges
        # For now, simple heuristic
        contents = [c["change"].get("content", "") for c in changes]
        
        # Check if modifying same functions/classes
        for i, content1 in enumerate(contents):
            for content2 in contents[i+1:]:
                if self._content_overlaps(content1, content2):
                    return True
        
        return False
    
    def _content_overlaps(self, content1: str, content2: str) -> bool:
        """Check if two content changes overlap"""
        
        # Extract function/class names
        import re
        
        pattern = r'(?:function|class|const|let|var)\s+(\w+)'
        names1 = set(re.findall(pattern, content1))
        names2 = set(re.findall(pattern, content2))
        
        # Overlap if modifying same named entities
        return bool(names1 & names2)
    
    def _are_contradictory(self, decision1: str, decision2: str) -> bool:
        """Check if two decisions are contradictory"""
        
        # Simple keyword-based contradiction detection
        contradictions = [
            ("synchronous", "asynchronous"),
            ("mutable", "immutable"),
            ("client-side", "server-side"),
            ("monolithic", "microservices")
        ]
        
        for word1, word2 in contradictions:
            if (word1 in decision1 and word2 in decision2) or \
               (word2 in decision1 and word1 in decision2):
                return True
        
        return False
    
    def _find_expert_agent(self, filepath: str, changes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Find the agent with most expertise for a file type"""
        
        file_type = self._get_file_type(filepath)
        
        # Simple heuristic: developer agents are experts for code files
        for change in changes:
            if "developer" in change["agent_id"]:
                return change
        
        # Otherwise, return first
        return changes[0]
    
    def _get_file_type(self, filepath: str) -> str:
        """Get file type from filepath"""
        
        if filepath.endswith(".py"):
            return "python"
        elif filepath.endswith(".js"):
            return "javascript"
        elif filepath.endswith(".ts"):
            return "typescript"
        else:
            return "unknown"
    
    def _merge_changes(self, changes: List[Dict[str, Any]]) -> str:
        """Merge non-overlapping changes"""
        
        # In real implementation, would use proper merge algorithm
        # For now, concatenate
        merged = []
        
        for change in changes:
            content = change["change"].get("content", "")
            merged.append(f"# Changes from {change['agent_id']}\n{content}")
        
        return "\n\n".join(merged)
    
    def _parse_version(self, version: str) -> Tuple[int, ...]:
        """Parse version string for comparison"""
        
        try:
            return tuple(map(int, version.split(".")))
        except:
            return (0, 0, 0)
    
    def _apply_resolution(self, merged_result: Dict[str, Any], resolution: Dict[str, Any]):
        """Apply resolution to merged result"""
        
        if "file" in resolution and "content" in resolution:
            if "file_changes" not in merged_result:
                merged_result["file_changes"] = []
            
            merged_result["file_changes"].append({
                "file": resolution["file"],
                "content": resolution["content"],
                "resolution_strategy": resolution.get("strategy", "unknown")
            })


# Singleton instance
_conflict_resolution = None

def get_conflict_resolution() -> ConflictResolution:
    """Get or create conflict resolution instance"""
    global _conflict_resolution
    if _conflict_resolution is None:
        _conflict_resolution = ConflictResolution()
    return _conflict_resolution