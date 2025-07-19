#!/usr/bin/env python3
"""
Work Distribution Engine for Multi-Agent System

Analyzes work packages, identifies dependencies, and creates optimal
distribution plans for parallel agent execution.
"""

import os
import json
import time
from typing import Dict, List, Any, Set, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict, deque
from enum import Enum


class TaskType(Enum):
    """Types of tasks agents can perform"""
    IMPLEMENT = "implement"
    REFACTOR = "refactor"
    TEST = "test"
    DOCUMENT = "document"
    REVIEW = "review"
    INTEGRATE = "integrate"
    CLEANUP = "cleanup"


@dataclass
class Task:
    """Represents a single task"""
    id: str
    type: TaskType
    description: str
    estimated_hours: float
    dependencies: List[str]
    required_capabilities: List[str]
    files_affected: List[str]
    priority: int = 5


@dataclass
class WorkPackage:
    """Represents a work package"""
    id: str
    name: str
    description: str
    tasks: List[Task]
    dependencies: List[str]  # Other work package IDs
    estimated_hours: float
    priority: int = 5
    
    def __post_init__(self):
        # Calculate total estimated hours if not provided
        if not self.estimated_hours and self.tasks:
            self.estimated_hours = sum(task.estimated_hours for task in self.tasks)


@dataclass
class AgentCapabilities:
    """Defines what an agent can do"""
    agent_type: str
    supported_tasks: List[TaskType]
    max_concurrent_tasks: int = 1
    performance_multiplier: float = 1.0  # Speed relative to baseline
    specializations: List[str] = None


@dataclass
class AgentAssignment:
    """Assignment of work to an agent"""
    agent_type: str
    work_package: WorkPackage
    tasks: List[Task]
    estimated_duration: float
    parallel_group: int


@dataclass
class DistributionPlan:
    """Complete work distribution plan"""
    parallel_groups: List[List[AgentAssignment]]
    total_agents_needed: int
    estimated_total_duration: float
    critical_path: List[str]
    dependencies_graph: Dict[str, List[str]]


class WorkDistributionEngine:
    """Analyzes and distributes work across agents"""
    
    def __init__(self):
        self.work_packages: Dict[str, WorkPackage] = {}
        self.agent_capabilities: Dict[str, AgentCapabilities] = {}
        self.dependency_graph: Dict[str, Set[str]] = defaultdict(set)
        self.file_conflicts: Dict[str, List[str]] = defaultdict(list)
        
        # Default agent capabilities
        self._register_default_capabilities()
    
    def _register_default_capabilities(self):
        """Register default agent types and capabilities"""
        # Development agent
        self.agent_capabilities["development"] = AgentCapabilities(
            agent_type="development",
            supported_tasks=[
                TaskType.IMPLEMENT,
                TaskType.REFACTOR,
                TaskType.TEST
            ],
            max_concurrent_tasks=1,
            performance_multiplier=1.0
        )
        
        # Review agent
        self.agent_capabilities["review"] = AgentCapabilities(
            agent_type="review",
            supported_tasks=[
                TaskType.REVIEW,
                TaskType.DOCUMENT
            ],
            max_concurrent_tasks=2,
            performance_multiplier=1.5
        )
        
        # Integration agent
        self.agent_capabilities["integration"] = AgentCapabilities(
            agent_type="integration",
            supported_tasks=[
                TaskType.INTEGRATE,
                TaskType.TEST
            ],
            max_concurrent_tasks=1,
            performance_multiplier=0.8
        )
        
        # Cleanup agent
        self.agent_capabilities["cleanup"] = AgentCapabilities(
            agent_type="cleanup",
            supported_tasks=[
                TaskType.CLEANUP,
                TaskType.DOCUMENT
            ],
            max_concurrent_tasks=3,
            performance_multiplier=1.2
        )
    
    def add_work_package(self, work_package: WorkPackage):
        """Add a work package to analyze"""
        self.work_packages[work_package.id] = work_package
        
        # Build dependency graph
        for dep_id in work_package.dependencies:
            self.dependency_graph[work_package.id].add(dep_id)
        
        # Track file conflicts
        for task in work_package.tasks:
            for file in task.files_affected:
                self.file_conflicts[file].append(work_package.id)
    
    def analyze_dependencies(self) -> Dict[str, List[str]]:
        """
        Analyze dependencies and return a clean dependency graph
        
        Returns:
            Dict mapping work package ID to list of dependencies
        """
        # Convert sets to lists for JSON serialization
        return {
            wp_id: list(deps)
            for wp_id, deps in self.dependency_graph.items()
        }
    
    def detect_circular_dependencies(self) -> List[List[str]]:
        """Detect circular dependencies in work packages"""
        cycles = []
        visited = set()
        rec_stack = set()
        
        def dfs(node: str, path: List[str]) -> bool:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            
            for neighbor in self.dependency_graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, path.copy()):
                        return True
                elif neighbor in rec_stack:
                    # Found cycle
                    cycle_start = path.index(neighbor)
                    cycle = path[cycle_start:] + [neighbor]
                    cycles.append(cycle)
                    return True
            
            rec_stack.remove(node)
            return False
        
        for wp_id in self.work_packages:
            if wp_id not in visited:
                dfs(wp_id, [])
        
        return cycles
    
    def topological_sort(self) -> List[str]:
        """
        Perform topological sort on work packages
        
        Returns:
            List of work package IDs in execution order
        """
        # Count incoming edges
        in_degree = defaultdict(int)
        for wp_id in self.work_packages:
            for dep in self.dependency_graph[wp_id]:
                in_degree[dep] += 1
        
        # Find nodes with no incoming edges
        queue = deque([
            wp_id for wp_id in self.work_packages
            if in_degree[wp_id] == 0
        ])
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            # Remove edges from this node
            for wp_id in self.work_packages:
                if node in self.dependency_graph[wp_id]:
                    in_degree[wp_id] -= 1
                    if in_degree[wp_id] == 0:
                        queue.append(wp_id)
        
        return result
    
    def identify_parallel_groups(self) -> List[List[str]]:
        """
        Identify groups of work packages that can run in parallel
        
        Returns:
            List of parallel groups, each containing work package IDs
        """
        # Perform topological sort to get levels
        sorted_packages = self.topological_sort()
        
        # Calculate levels based on dependencies
        levels = {}
        for wp_id in sorted_packages:
            # Find maximum level of dependencies
            max_dep_level = -1
            for dep_id in self.dependency_graph[wp_id]:
                if dep_id in levels:
                    max_dep_level = max(max_dep_level, levels[dep_id])
            
            levels[wp_id] = max_dep_level + 1
        
        # Group by level
        groups = defaultdict(list)
        for wp_id, level in levels.items():
            groups[level].append(wp_id)
        
        # Check for file conflicts within groups
        parallel_groups = []
        for level in sorted(groups.keys()):
            group = groups[level]
            
            # Split group if there are file conflicts
            subgroups = self._split_by_file_conflicts(group)
            parallel_groups.extend(subgroups)
        
        return parallel_groups
    
    def _split_by_file_conflicts(self, group: List[str]) -> List[List[str]]:
        """Split a group based on file conflicts"""
        if len(group) <= 1:
            return [group]
        
        # Build conflict graph
        conflicts = defaultdict(set)
        for i, wp1 in enumerate(group):
            for j, wp2 in enumerate(group[i+1:], i+1):
                if self._have_file_conflict(wp1, wp2):
                    conflicts[wp1].add(wp2)
                    conflicts[wp2].add(wp1)
        
        # Color the conflict graph (simple greedy algorithm)
        colors = {}
        color_groups = defaultdict(list)
        
        for wp_id in group:
            # Find first available color
            used_colors = {colors[neighbor] for neighbor in conflicts[wp_id] if neighbor in colors}
            color = 0
            while color in used_colors:
                color += 1
            
            colors[wp_id] = color
            color_groups[color].append(wp_id)
        
        return list(color_groups.values())
    
    def _have_file_conflict(self, wp1: str, wp2: str) -> bool:
        """Check if two work packages have file conflicts"""
        wp1_files = set()
        wp2_files = set()
        
        for task in self.work_packages[wp1].tasks:
            wp1_files.update(task.files_affected)
        
        for task in self.work_packages[wp2].tasks:
            wp2_files.update(task.files_affected)
        
        return bool(wp1_files.intersection(wp2_files))
    
    def assign_agents(self, parallel_groups: List[List[str]]) -> List[List[AgentAssignment]]:
        """Assign appropriate agents to work packages"""
        assigned_groups = []
        
        for group_idx, group in enumerate(parallel_groups):
            assignments = []
            
            for wp_id in group:
                work_package = self.work_packages[wp_id]
                
                # Determine best agent type
                agent_type = self._select_agent_type(work_package)
                
                # Create assignment
                assignment = AgentAssignment(
                    agent_type=agent_type,
                    work_package=work_package,
                    tasks=work_package.tasks,
                    estimated_duration=self._estimate_duration(
                        work_package,
                        agent_type
                    ),
                    parallel_group=group_idx
                )
                
                assignments.append(assignment)
            
            assigned_groups.append(assignments)
        
        return assigned_groups
    
    def _select_agent_type(self, work_package: WorkPackage) -> str:
        """Select the best agent type for a work package"""
        # Count task types
        task_type_counts = defaultdict(int)
        for task in work_package.tasks:
            task_type_counts[task.type] += 1
        
        # Find agent type that can handle most tasks
        best_agent = "development"  # Default
        best_coverage = 0
        
        for agent_type, capabilities in self.agent_capabilities.items():
            coverage = sum(
                count for task_type, count in task_type_counts.items()
                if task_type in capabilities.supported_tasks
            )
            
            if coverage > best_coverage:
                best_coverage = coverage
                best_agent = agent_type
        
        return best_agent
    
    def _estimate_duration(self, work_package: WorkPackage, agent_type: str) -> float:
        """Estimate duration for an agent to complete work package"""
        capabilities = self.agent_capabilities[agent_type]
        
        # Base duration
        duration = work_package.estimated_hours
        
        # Apply performance multiplier
        duration /= capabilities.performance_multiplier
        
        # Add overhead for unsupported tasks
        unsupported_hours = sum(
            task.estimated_hours for task in work_package.tasks
            if task.type not in capabilities.supported_tasks
        )
        
        # Unsupported tasks take 2x longer
        duration += unsupported_hours
        
        return duration
    
    def calculate_critical_path(self) -> Tuple[List[str], float]:
        """
        Calculate the critical path through work packages
        
        Returns:
            Tuple of (path, duration)
        """
        # Dynamic programming to find longest path
        durations = {}
        predecessors = {}
        
        # Topological sort ensures we process in correct order
        sorted_packages = self.topological_sort()
        
        for wp_id in sorted_packages:
            wp = self.work_packages[wp_id]
            
            # Find maximum duration from dependencies
            max_pred_duration = 0
            max_pred = None
            
            for dep_id in self.dependency_graph[wp_id]:
                if dep_id in durations and durations[dep_id] > max_pred_duration:
                    max_pred_duration = durations[dep_id]
                    max_pred = dep_id
            
            durations[wp_id] = max_pred_duration + wp.estimated_hours
            predecessors[wp_id] = max_pred
        
        # Find the end of critical path
        max_duration = 0
        end_node = None
        
        for wp_id, duration in durations.items():
            if duration > max_duration:
                max_duration = duration
                end_node = wp_id
        
        # Reconstruct path
        path = []
        current = end_node
        while current:
            path.append(current)
            current = predecessors.get(current)
        
        path.reverse()
        
        return path, max_duration
    
    def create_distribution_plan(self) -> DistributionPlan:
        """Create complete distribution plan"""
        # Check for circular dependencies
        cycles = self.detect_circular_dependencies()
        if cycles:
            raise ValueError(f"Circular dependencies detected: {cycles}")
        
        # Identify parallel groups
        parallel_groups_ids = self.identify_parallel_groups()
        
        # Assign agents
        parallel_groups = self.assign_agents(parallel_groups_ids)
        
        # Calculate critical path
        critical_path, critical_duration = self.calculate_critical_path()
        
        # Calculate total agents needed
        total_agents = max(len(group) for group in parallel_groups)
        
        # Calculate estimated duration (max duration of any parallel group)
        estimated_duration = max(
            max(assignment.estimated_duration for assignment in group)
            for group in parallel_groups
        )
        
        return DistributionPlan(
            parallel_groups=parallel_groups,
            total_agents_needed=total_agents,
            estimated_total_duration=estimated_duration,
            critical_path=critical_path,
            dependencies_graph=self.analyze_dependencies()
        )
    
    def optimize_distribution(self, plan: DistributionPlan, 
                              max_agents: int) -> DistributionPlan:
        """Optimize distribution plan given agent constraints"""
        if plan.total_agents_needed <= max_agents:
            return plan
        
        # Need to reduce parallelism
        # Merge parallel groups to fit within agent limit
        optimized_groups = []
        
        for group in plan.parallel_groups:
            if len(group) <= max_agents:
                optimized_groups.append(group)
            else:
                # Split group into smaller groups
                for i in range(0, len(group), max_agents):
                    subgroup = group[i:i + max_agents]
                    optimized_groups.append(subgroup)
        
        # Recalculate metrics
        total_agents = max(len(group) for group in optimized_groups)
        estimated_duration = sum(
            max(assignment.estimated_duration for assignment in group)
            for group in optimized_groups
        )
        
        return DistributionPlan(
            parallel_groups=optimized_groups,
            total_agents_needed=total_agents,
            estimated_total_duration=estimated_duration,
            critical_path=plan.critical_path,
            dependencies_graph=plan.dependencies_graph
        )


if __name__ == "__main__":
    # Example usage
    print("Testing Work Distribution Engine...")
    
    engine = WorkDistributionEngine()
    
    # Create test work packages
    wp1 = WorkPackage(
        id="wp1-hooks",
        name="Hook Infrastructure",
        description="Implement hook system",
        tasks=[
            Task(
                id="t1",
                type=TaskType.IMPLEMENT,
                description="Create base hook class",
                estimated_hours=2,
                dependencies=[],
                required_capabilities=["python"],
                files_affected=["hook_base.py"]
            )
        ],
        dependencies=[],
        estimated_hours=2
    )
    
    wp2 = WorkPackage(
        id="wp2-session",
        name="Session Management",
        description="Fix session management",
        tasks=[
            Task(
                id="t2",
                type=TaskType.REFACTOR,
                description="Refactor session manager",
                estimated_hours=3,
                dependencies=[],
                required_capabilities=["python"],
                files_affected=["session_manager.py"]
            )
        ],
        dependencies=[],
        estimated_hours=3
    )
    
    wp3 = WorkPackage(
        id="wp3-docs",
        name="Documentation",
        description="Update documentation",
        tasks=[
            Task(
                id="t3",
                type=TaskType.DOCUMENT,
                description="Update CLAUDE.md",
                estimated_hours=1,
                dependencies=[],
                required_capabilities=["markdown"],
                files_affected=["CLAUDE.md"]
            )
        ],
        dependencies=["wp1-hooks", "wp2-session"],
        estimated_hours=1
    )
    
    # Add work packages
    engine.add_work_package(wp1)
    engine.add_work_package(wp2)
    engine.add_work_package(wp3)
    
    # Create distribution plan
    plan = engine.create_distribution_plan()
    
    print(f"\n✓ Distribution plan created:")
    print(f"  Total agents needed: {plan.total_agents_needed}")
    print(f"  Estimated duration: {plan.estimated_total_duration} hours")
    print(f"  Critical path: {' → '.join(plan.critical_path)}")
    
    print(f"\n  Parallel groups:")
    for i, group in enumerate(plan.parallel_groups):
        print(f"    Group {i+1}:")
        for assignment in group:
            print(f"      - {assignment.work_package.name} ({assignment.agent_type})")
    
    # Optimize for limited agents
    print(f"\n  Optimizing for max 2 agents...")
    optimized = engine.optimize_distribution(plan, max_agents=2)
    print(f"  New duration: {optimized.estimated_total_duration} hours")