#!/usr/bin/env python3
"""
Consolidation Analyzer - Duplicate Detection and Consolidation Engine
Finds consolidation opportunities and generates migration strategies
"""

import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict
import json
from datetime import datetime

from .similarity_detector import SimilarityDetector, SimilarityMatch, CodeBlock


@dataclass
class ConsolidationOpportunity:
    """Represents an opportunity to consolidate duplicate code"""
    duplicate_blocks: List[CodeBlock]
    consolidation_type: str  # 'extract_function', 'extract_class', 'shared_utility', 'merge'
    estimated_loc_saved: int
    complexity_reduction: float  # 0-100
    effort_estimate: str  # 'low', 'medium', 'high'
    priority: str  # 'high', 'medium', 'low'
    suggested_name: str
    suggested_location: Path
    migration_steps: List[str] = field(default_factory=list)
    benefits: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)


@dataclass
class ConsolidationPlan:
    """Complete consolidation plan for a codebase"""
    opportunities: List[ConsolidationOpportunity]
    total_loc_saved: int
    total_files_affected: int
    estimated_effort_hours: float
    roi_score: float  # Return on investment score
    execution_order: List[int]  # Indices of opportunities in recommended order


@dataclass
class MigrationStep:
    """Detailed migration step for consolidation"""
    step_number: int
    description: str
    code_before: Optional[str] = None
    code_after: Optional[str] = None
    affected_files: List[Path] = field(default_factory=list)
    validation_steps: List[str] = field(default_factory=list)


class ConsolidationAnalyzer:
    """Main consolidation analysis and planning engine"""
    
    def __init__(self, project_root: Path = None):
        """Initialize consolidation analyzer"""
        if project_root is None:
            current = Path.cwd()
            while not (current / ".claude").exists() and current != current.parent:
                current = current.parent
            self.project_root = current
        else:
            self.project_root = project_root
            
        self.src_path = self.project_root / "src"
        self.similarity_detector = SimilarityDetector(project_root)
        
        # Consolidation thresholds
        self.min_duplicate_lines = 10
        self.min_similarity_for_consolidation = 70
        
        # Cache for analysis results
        self._analysis_cache = {}
        
    def analyze_consolidation_opportunities(
        self,
        search_paths: Optional[List[Path]] = None,
        min_similarity: float = None
    ) -> ConsolidationPlan:
        """
        Analyze codebase for consolidation opportunities
        
        Args:
            search_paths: Paths to analyze (defaults to src/)
            min_similarity: Minimum similarity threshold (defaults to 70%)
            
        Returns:
            Complete consolidation plan with prioritized opportunities
            
        Example:
            analyzer = ConsolidationAnalyzer()
            plan = analyzer.analyze_consolidation_opportunities()
            print(f"Found {len(plan.opportunities)} consolidation opportunities")
            print(f"Potential savings: {plan.total_loc_saved} lines of code")
        """
        if search_paths is None:
            search_paths = [self.src_path] if self.src_path.exists() else []
            
        if min_similarity is None:
            min_similarity = self.min_similarity_for_consolidation
            
        # Find all similar code blocks
        similar_blocks = self.similarity_detector.detect_similar_code(
            search_paths=search_paths,
            min_lines=self.min_duplicate_lines
        )
        
        # Group similar blocks for consolidation
        consolidation_groups = self._group_similar_blocks(similar_blocks, min_similarity)
        
        # Analyze each group for consolidation opportunities
        opportunities = []
        for group in consolidation_groups:
            opportunity = self._analyze_consolidation_group(group)
            if opportunity:
                opportunities.append(opportunity)
                
        # Calculate plan metrics
        plan = self._create_consolidation_plan(opportunities)
        
        return plan
    
    def _group_similar_blocks(
        self,
        similar_blocks: List[SimilarityMatch],
        min_similarity: float
    ) -> List[List[CodeBlock]]:
        """Group similar blocks that can be consolidated together"""
        # Filter by minimum similarity
        eligible_matches = [
            match for match in similar_blocks
            if match.similarity_score >= min_similarity
        ]
        
        # Group blocks using union-find algorithm
        groups = defaultdict(set)
        block_to_group = {}
        
        for match in eligible_matches:
            block1_id = id(match.block1)
            block2_id = id(match.block2)
            
            # Find or create groups
            group1 = block_to_group.get(block1_id)
            group2 = block_to_group.get(block2_id)
            
            if group1 is None and group2 is None:
                # Create new group
                group_id = len(groups)
                groups[group_id].add(match.block1)
                groups[group_id].add(match.block2)
                block_to_group[block1_id] = group_id
                block_to_group[block2_id] = group_id
            elif group1 is not None and group2 is None:
                # Add block2 to group1
                groups[group1].add(match.block2)
                block_to_group[block2_id] = group1
            elif group1 is None and group2 is not None:
                # Add block1 to group2
                groups[group2].add(match.block1)
                block_to_group[block1_id] = group2
            elif group1 != group2:
                # Merge groups
                groups[group1].update(groups[group2])
                for block in groups[group2]:
                    block_to_group[id(block)] = group1
                del groups[group2]
                
        # Convert to list of lists
        return [list(blocks) for blocks in groups.values() if len(blocks) >= 2]
    
    def _analyze_consolidation_group(
        self,
        blocks: List[CodeBlock]
    ) -> Optional[ConsolidationOpportunity]:
        """Analyze a group of similar blocks for consolidation"""
        if len(blocks) < 2:
            return None
            
        # Determine consolidation type
        consolidation_type = self._determine_consolidation_type(blocks)
        
        # Calculate metrics
        total_lines = sum(block.line_count for block in blocks)
        consolidated_lines = max(block.line_count for block in blocks)
        loc_saved = total_lines - consolidated_lines - (len(blocks) * 3)  # Account for calls
        
        if loc_saved < 10:  # Not worth consolidating
            return None
            
        # Calculate complexity reduction
        complexity_reduction = self._calculate_complexity_reduction(blocks)
        
        # Estimate effort
        effort = self._estimate_consolidation_effort(blocks, consolidation_type)
        
        # Determine priority
        priority = self._calculate_priority(loc_saved, complexity_reduction, effort)
        
        # Generate suggested name and location
        suggested_name = self._generate_consolidated_name(blocks)
        suggested_location = self._determine_best_location(blocks)
        
        # Create migration steps
        migration_steps = self._generate_migration_steps(
            blocks,
            consolidation_type,
            suggested_name,
            suggested_location
        )
        
        # Identify benefits and risks
        benefits = self._identify_benefits(blocks, loc_saved)
        risks = self._identify_risks(blocks, consolidation_type)
        
        return ConsolidationOpportunity(
            duplicate_blocks=blocks,
            consolidation_type=consolidation_type,
            estimated_loc_saved=loc_saved,
            complexity_reduction=complexity_reduction,
            effort_estimate=effort,
            priority=priority,
            suggested_name=suggested_name,
            suggested_location=suggested_location,
            migration_steps=migration_steps,
            benefits=benefits,
            risks=risks
        )
    
    def _determine_consolidation_type(self, blocks: List[CodeBlock]) -> str:
        """Determine the best consolidation strategy"""
        # Check block types
        block_types = set(block.block_type for block in blocks)
        
        if len(block_types) == 1:
            block_type = list(block_types)[0]
            
            if block_type == 'function':
                # Check if functions are similar enough to merge
                if self._are_functions_mergeable(blocks):
                    return 'merge'
                else:
                    return 'extract_function'
            elif block_type == 'class':
                return 'extract_class'
            elif block_type == 'method':
                return 'extract_function'
            else:
                return 'shared_utility'
        else:
            # Mixed types - extract to utility
            return 'shared_utility'
    
    def _are_functions_mergeable(self, blocks: List[CodeBlock]) -> bool:
        """Check if functions can be merged into one parameterized function"""
        # Simple heuristic: check if functions have similar structure
        # but different constants/parameters
        
        if len(blocks) < 2:
            return False
            
        # Extract function signatures
        signatures = []
        for block in blocks:
            sig_match = re.search(r'function\s+\w+\s*\(([^)]*)\)', block.content)
            if sig_match:
                signatures.append(sig_match.group(1))
                
        # If signatures are identical, likely mergeable
        if len(set(signatures)) == 1:
            return True
            
        # Check for pattern differences
        # TODO: More sophisticated analysis
        return False
    
    def _calculate_complexity_reduction(self, blocks: List[CodeBlock]) -> float:
        """Calculate how much complexity is reduced by consolidation"""
        # Factors:
        # - Number of duplicates (more = higher reduction)
        # - Size of duplicated code (larger = higher reduction)
        # - Spread across files (more spread = higher reduction)
        
        num_duplicates = len(blocks)
        avg_size = sum(block.line_count for block in blocks) / num_duplicates
        unique_files = len(set(block.file_path for block in blocks))
        
        # Calculate score
        duplicate_factor = min(100, num_duplicates * 10)
        size_factor = min(100, avg_size * 2)
        spread_factor = min(100, unique_files * 15)
        
        complexity_reduction = (duplicate_factor + size_factor + spread_factor) / 3
        
        return min(100, complexity_reduction)
    
    def _estimate_consolidation_effort(
        self,
        blocks: List[CodeBlock],
        consolidation_type: str
    ) -> str:
        """Estimate effort required for consolidation"""
        # Factors affecting effort
        num_files = len(set(block.file_path for block in blocks))
        total_lines = sum(block.line_count for block in blocks)
        
        # Base effort by consolidation type
        base_effort = {
            'merge': 1,
            'extract_function': 2,
            'extract_class': 3,
            'shared_utility': 2.5
        }
        
        effort_score = base_effort.get(consolidation_type, 2)
        
        # Adjust for scale
        if num_files > 5:
            effort_score += 1
        if total_lines > 200:
            effort_score += 1
            
        # Check for complex dependencies
        for block in blocks:
            if 'import' in block.content or 'require' in block.content:
                effort_score += 0.5
                break
                
        # Convert to category
        if effort_score <= 2:
            return 'low'
        elif effort_score <= 3.5:
            return 'medium'
        else:
            return 'high'
    
    def _calculate_priority(
        self,
        loc_saved: int,
        complexity_reduction: float,
        effort: str
    ) -> str:
        """Calculate consolidation priority"""
        # High benefit + low effort = high priority
        benefit_score = (loc_saved / 10) + complexity_reduction
        
        effort_multiplier = {
            'low': 1.5,
            'medium': 1.0,
            'high': 0.5
        }
        
        priority_score = benefit_score * effort_multiplier.get(effort, 1.0)
        
        if priority_score >= 100:
            return 'high'
        elif priority_score >= 50:
            return 'medium'
        else:
            return 'low'
    
    def _generate_consolidated_name(self, blocks: List[CodeBlock]) -> str:
        """Generate a name for the consolidated code"""
        # Try to find common patterns in existing names
        names = [block.name for block in blocks if block.name]
        
        if not names:
            return 'consolidatedUtility'
            
        # Find common prefix/suffix
        common_prefix = self._find_common_prefix(names)
        common_suffix = self._find_common_suffix(names)
        
        if common_prefix and len(common_prefix) > 3:
            return common_prefix + 'Shared'
        elif common_suffix and len(common_suffix) > 3:
            return 'shared' + common_suffix.capitalize()
        else:
            # Use most descriptive name
            return max(names, key=len) + 'Shared'
    
    def _find_common_prefix(self, strings: List[str]) -> str:
        """Find common prefix of strings"""
        if not strings:
            return ""
            
        prefix = strings[0]
        for string in strings[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
    def _find_common_suffix(self, strings: List[str]) -> str:
        """Find common suffix of strings"""
        if not strings:
            return ""
            
        suffix = strings[0]
        for string in strings[1:]:
            while not string.endswith(suffix):
                suffix = suffix[1:]
                if not suffix:
                    return ""
        return suffix
    
    def _determine_best_location(self, blocks: List[CodeBlock]) -> Path:
        """Determine best location for consolidated code"""
        # Find common directory
        paths = [block.file_path for block in blocks]
        common_dir = self._find_common_directory(paths)
        
        # Suggest utils or shared directory
        utils_dir = common_dir / 'utils'
        shared_dir = common_dir / 'shared'
        
        if utils_dir.exists():
            return utils_dir / 'consolidated.js'
        elif shared_dir.exists():
            return shared_dir / 'consolidated.js'
        else:
            return common_dir / 'shared' / 'consolidated.js'
    
    def _find_common_directory(self, paths: List[Path]) -> Path:
        """Find common parent directory of paths"""
        if not paths:
            return self.src_path
            
        common_parts = paths[0].parts
        
        for path in paths[1:]:
            path_parts = path.parts
            new_common = []
            
            for i, part in enumerate(common_parts):
                if i < len(path_parts) and part == path_parts[i]:
                    new_common.append(part)
                else:
                    break
                    
            common_parts = new_common
            
        return Path(*common_parts) if common_parts else self.src_path
    
    def _generate_migration_steps(
        self,
        blocks: List[CodeBlock],
        consolidation_type: str,
        suggested_name: str,
        suggested_location: Path
    ) -> List[str]:
        """Generate step-by-step migration plan"""
        steps = []
        
        if consolidation_type == 'extract_function':
            steps.extend([
                f"1. Create new function '{suggested_name}' in {suggested_location}",
                "2. Identify parameters needed to generalize the function",
                "3. Implement the generalized function with proper parameters",
                "4. Add comprehensive tests for the new function",
                "5. Replace each duplicate with a call to the new function",
                "6. Update imports in affected files",
                "7. Run tests to ensure functionality is preserved",
                "8. Remove old duplicate code blocks"
            ])
        elif consolidation_type == 'extract_class':
            steps.extend([
                f"1. Create new class '{suggested_name}' in {suggested_location}",
                "2. Design the class interface to handle all use cases",
                "3. Implement the class with necessary methods",
                "4. Add unit tests for the class",
                "5. Replace duplicate classes with the new shared class",
                "6. Update imports and instantiation in affected files",
                "7. Verify inheritance and method overrides work correctly",
                "8. Remove duplicate class definitions"
            ])
        elif consolidation_type == 'shared_utility':
            steps.extend([
                f"1. Create utility module at {suggested_location}",
                "2. Extract common functionality into utility functions",
                "3. Ensure utilities are properly parameterized",
                "4. Add tests for each utility function",
                "5. Replace duplicates with utility function calls",
                "6. Add utility imports to affected files",
                "7. Test all affected components",
                "8. Clean up duplicate code"
            ])
        elif consolidation_type == 'merge':
            steps.extend([
                "1. Analyze differences between similar functions",
                "2. Create parameterized version that handles all cases",
                "3. Add configuration options or parameters as needed",
                "4. Test merged function with all original use cases",
                "5. Replace all instances with the merged function",
                "6. Update function calls with appropriate parameters",
                "7. Verify behavior matches original in all cases",
                "8. Remove redundant function definitions"
            ])
            
        return steps
    
    def _identify_benefits(self, blocks: List[CodeBlock], loc_saved: int) -> List[str]:
        """Identify benefits of consolidation"""
        benefits = [
            f"Reduces codebase by {loc_saved} lines",
            f"Eliminates {len(blocks)} duplicate implementations",
            "Improves maintainability - single source of truth",
            "Reduces testing effort - test once, use everywhere"
        ]
        
        # Add specific benefits based on context
        unique_files = len(set(block.file_path for block in blocks))
        if unique_files > 3:
            benefits.append(f"Simplifies code across {unique_files} files")
            
        if any('bug' in block.content.lower() or 'fix' in block.content.lower() for block in blocks):
            benefits.append("Ensures bug fixes are applied consistently")
            
        return benefits
    
    def _identify_risks(self, blocks: List[CodeBlock], consolidation_type: str) -> List[str]:
        """Identify risks of consolidation"""
        risks = []
        
        # General risks
        if len(blocks) > 5:
            risks.append("High number of dependencies to update")
            
        # Check for subtle differences
        contents = [block.content for block in blocks]
        if not all(content == contents[0] for content in contents):
            risks.append("Subtle differences between implementations may be important")
            
        # Type-specific risks
        if consolidation_type == 'merge':
            risks.append("Merged function may become too complex")
        elif consolidation_type == 'extract_class':
            risks.append("May introduce unnecessary abstraction")
            
        # Check for external dependencies
        for block in blocks:
            if 'webflow' in block.content.lower():
                risks.append("Webflow-specific code may not generalize well")
                break
                
        return risks if risks else ["Minimal risk - straightforward consolidation"]
    
    def _create_consolidation_plan(
        self,
        opportunities: List[ConsolidationOpportunity]
    ) -> ConsolidationPlan:
        """Create comprehensive consolidation plan"""
        # Calculate totals
        total_loc_saved = sum(opp.estimated_loc_saved for opp in opportunities)
        
        # Count unique files
        all_files = set()
        for opp in opportunities:
            for block in opp.duplicate_blocks:
                all_files.add(block.file_path)
        total_files_affected = len(all_files)
        
        # Estimate total effort
        effort_hours = {
            'low': 2,
            'medium': 5,
            'high': 10
        }
        total_effort = sum(effort_hours.get(opp.effort_estimate, 5) for opp in opportunities)
        
        # Calculate ROI
        roi_score = (total_loc_saved / max(1, total_effort)) * 10
        
        # Determine execution order (high priority first, dependencies considered)
        execution_order = self._calculate_execution_order(opportunities)
        
        return ConsolidationPlan(
            opportunities=opportunities,
            total_loc_saved=total_loc_saved,
            total_files_affected=total_files_affected,
            estimated_effort_hours=total_effort,
            roi_score=roi_score,
            execution_order=execution_order
        )
    
    def _calculate_execution_order(
        self,
        opportunities: List[ConsolidationOpportunity]
    ) -> List[int]:
        """Calculate optimal execution order considering dependencies"""
        # Simple priority-based ordering for now
        # TODO: Add dependency analysis
        
        priority_order = {
            'high': 0,
            'medium': 1,
            'low': 2
        }
        
        indexed_opps = [(i, opp) for i, opp in enumerate(opportunities)]
        indexed_opps.sort(
            key=lambda x: (priority_order.get(x[1].priority, 2), -x[1].estimated_loc_saved)
        )
        
        return [i for i, _ in indexed_opps]
    
    def generate_consolidation_report(
        self,
        plan: ConsolidationPlan,
        output_format: str = 'markdown'
    ) -> str:
        """
        Generate a detailed consolidation report
        
        Args:
            plan: Consolidation plan to report on
            output_format: 'markdown' or 'json'
            
        Returns:
            Formatted report string
        """
        if output_format == 'json':
            return self._generate_json_report(plan)
        else:
            return self._generate_markdown_report(plan)
    
    def _generate_markdown_report(self, plan: ConsolidationPlan) -> str:
        """Generate markdown-formatted report"""
        report = [
            "# Code Consolidation Analysis Report",
            f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\n## Executive Summary",
            f"- **Total Opportunities Found**: {len(plan.opportunities)}",
            f"- **Potential Lines Saved**: {plan.total_loc_saved:,}",
            f"- **Files Affected**: {plan.total_files_affected}",
            f"- **Estimated Effort**: {plan.estimated_effort_hours:.1f} hours",
            f"- **ROI Score**: {plan.roi_score:.1f}/10",
            "\n## Consolidation Opportunities\n"
        ]
        
        # Add opportunities in execution order
        for idx in plan.execution_order:
            opp = plan.opportunities[idx]
            report.extend([
                f"### {idx + 1}. {opp.suggested_name}",
                f"- **Type**: {opp.consolidation_type.replace('_', ' ').title()}",
                f"- **Priority**: {opp.priority.upper()}",
                f"- **Lines Saved**: {opp.estimated_loc_saved}",
                f"- **Complexity Reduction**: {opp.complexity_reduction:.0f}%",
                f"- **Effort**: {opp.effort_estimate}",
                f"- **Location**: `{opp.suggested_location}`",
                "\n**Affected Files**:"
            ])
            
            for block in opp.duplicate_blocks[:5]:  # Show first 5
                report.append(f"- `{block.file_path}` (lines {block.start_line}-{block.end_line})")
            
            if len(opp.duplicate_blocks) > 5:
                report.append(f"- ... and {len(opp.duplicate_blocks) - 5} more")
                
            report.append("\n**Benefits**:")
            for benefit in opp.benefits:
                report.append(f"- {benefit}")
                
            report.append("\n**Risks**:")
            for risk in opp.risks:
                report.append(f"- {risk}")
                
            report.append("\n**Migration Steps**:")
            for step in opp.migration_steps[:3]:  # Show first 3 steps
                report.append(f"- {step}")
            if len(opp.migration_steps) > 3:
                report.append(f"- ... and {len(opp.migration_steps) - 3} more steps")
                
            report.append("\n---\n")
            
        return '\n'.join(report)
    
    def _generate_json_report(self, plan: ConsolidationPlan) -> str:
        """Generate JSON-formatted report"""
        report_data = {
            'generated': datetime.now().isoformat(),
            'summary': {
                'total_opportunities': len(plan.opportunities),
                'total_loc_saved': plan.total_loc_saved,
                'total_files_affected': plan.total_files_affected,
                'estimated_effort_hours': plan.estimated_effort_hours,
                'roi_score': plan.roi_score
            },
            'opportunities': []
        }
        
        for idx in plan.execution_order:
            opp = plan.opportunities[idx]
            opp_data = {
                'index': idx + 1,
                'suggested_name': opp.suggested_name,
                'consolidation_type': opp.consolidation_type,
                'priority': opp.priority,
                'estimated_loc_saved': opp.estimated_loc_saved,
                'complexity_reduction': opp.complexity_reduction,
                'effort_estimate': opp.effort_estimate,
                'suggested_location': str(opp.suggested_location),
                'affected_files': [
                    {
                        'path': str(block.file_path),
                        'lines': f"{block.start_line}-{block.end_line}"
                    }
                    for block in opp.duplicate_blocks
                ],
                'benefits': opp.benefits,
                'risks': opp.risks,
                'migration_steps': opp.migration_steps
            }
            report_data['opportunities'].append(opp_data)
            
        return json.dumps(report_data, indent=2)
    
    def clear_cache(self):
        """Clear analysis caches"""
        self._analysis_cache.clear()
        self.similarity_detector.clear_cache()