#!/usr/bin/env python3
"""
Reuse Analyzer - Component Discovery and Scoring Engine
Searches for existing components that match requirements and provides reuse recommendations
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ComponentMatch:
    """Represents a potential component match for reuse"""
    file_path: Path
    component_name: str
    match_score: float  # 0-100
    functionality_score: float  # How well it matches the required functionality
    interface_score: float  # How compatible the interfaces are
    modification_effort: float  # Estimated effort to modify (0=easy, 100=hard)
    match_details: Dict[str, Any] = field(default_factory=dict)
    code_snippet: Optional[str] = None
    
    @property
    def reuse_recommendation(self) -> str:
        """Generate recommendation based on scores"""
        if self.match_score >= 80:
            return "STRONG_MATCH: Extend this component"
        elif self.match_score >= 60:
            return "GOOD_MATCH: Consider extending with modifications"
        elif self.match_score >= 40:
            return "PARTIAL_MATCH: Significant modifications needed"
        else:
            return "WEAK_MATCH: New component may be justified"


@dataclass
class ReuseScore:
    """Overall reuse analysis score"""
    best_match: Optional[ComponentMatch] = None
    all_matches: List[ComponentMatch] = field(default_factory=list)
    justification_required: bool = True
    analysis_summary: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class ReuseAnalyzer:
    """Main component discovery and scoring engine"""
    
    def __init__(self, project_root: Path = None):
        """Initialize reuse analyzer"""
        if project_root is None:
            # Find project root by looking for .claude directory
            current = Path.cwd()
            while not (current / ".claude").exists() and current != current.parent:
                current = current.parent
            self.project_root = current
        else:
            self.project_root = project_root
            
        self.claude_path = self.project_root / ".claude"
        self.src_path = self.project_root / "src"
        
        # Load patterns and constraints
        self._load_project_patterns()
        
    def _load_project_patterns(self):
        """Load project patterns and constraints"""
        patterns_path = self.claude_path / "knowledge" / "patterns.json"
        constraints_path = self.claude_path / "knowledge" / "constraints.json"
        
        self.patterns = {}
        self.constraints = {}
        
        if patterns_path.exists():
            with open(patterns_path, 'r') as f:
                self.patterns = json.load(f)
                
        if constraints_path.exists():
            with open(constraints_path, 'r') as f:
                self.constraints = json.load(f)
    
    def analyze_reuse_potential(
        self,
        requirements: Dict[str, Any],
        search_paths: Optional[List[Path]] = None
    ) -> ReuseScore:
        """
        Analyze existing codebase for reuse potential
        
        Args:
            requirements: Dict with keys like 'functionality', 'type', 'interface', etc.
            search_paths: Optional list of paths to search (defaults to src/)
            
        Returns:
            ReuseScore with analysis results
        """
        if search_paths is None:
            search_paths = [self.src_path] if self.src_path.exists() else []
            
        # Extract requirement details
        functionality = requirements.get('functionality', '')
        component_type = requirements.get('type', '')
        interface_needs = requirements.get('interface', {})
        
        # Search for matching components
        matches = self._search_components(
            functionality,
            component_type,
            search_paths
        )
        
        # Score each match
        scored_matches = []
        for match in matches:
            scored = self._score_component(match, requirements)
            if scored.match_score > 20:  # Only include relevant matches
                scored_matches.append(scored)
        
        # Sort by score
        scored_matches.sort(key=lambda x: x.match_score, reverse=True)
        
        # Determine if new file is justified
        best_match = scored_matches[0] if scored_matches else None
        justification_required = True
        
        if best_match and best_match.match_score >= 60:
            justification_required = False
            
        # Generate analysis summary
        summary = self._generate_summary(scored_matches, requirements)
        
        return ReuseScore(
            best_match=best_match,
            all_matches=scored_matches[:10],  # Top 10 matches
            justification_required=justification_required,
            analysis_summary=summary
        )
    
    def _search_components(
        self,
        functionality: str,
        component_type: str,
        search_paths: List[Path]
    ) -> List[Dict[str, Any]]:
        """Search for components matching the criteria"""
        matches = []
        
        # Define search patterns based on component type
        patterns = self._get_search_patterns(functionality, component_type)
        
        for path in search_paths:
            if not path.exists():
                continue
                
            # Search JavaScript files
            for js_file in path.rglob("*.js"):
                # Skip node_modules and other excluded paths
                if self._should_skip_file(js_file):
                    continue
                    
                try:
                    content = js_file.read_text()
                    
                    # Check for pattern matches
                    for pattern in patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            matches.append({
                                'file_path': js_file,
                                'content': content,
                                'pattern_matched': pattern
                            })
                            break
                            
                except Exception:
                    continue
                    
        return matches
    
    def _get_search_patterns(self, functionality: str, component_type: str) -> List[str]:
        """Generate search patterns based on requirements"""
        patterns = []
        
        # Functionality-based patterns
        func_words = functionality.lower().split()
        for word in func_words:
            if len(word) > 3:  # Skip short words
                patterns.append(rf'\b{word}\b')
        
        # Component type patterns
        type_patterns = {
            'animation': [r'animate', r'motion', r'gsap', r'transition'],
            'navigation': [r'nav', r'menu', r'dropdown', r'toggle'],
            'form': [r'form', r'input', r'submit', r'validate'],
            'modal': [r'modal', r'dialog', r'popup', r'overlay'],
            'carousel': [r'carousel', r'slider', r'swipe', r'slide'],
            'accordion': [r'accordion', r'collapse', r'expand', r'toggle'],
            'tabs': [r'tab', r'panel', r'switch', r'active'],
            'filter': [r'filter', r'sort', r'search', r'category'],
            'scroll': [r'scroll', r'waypoint', r'intersect', r'sticky'],
            'loader': [r'load', r'spinner', r'progress', r'wait']
        }
        
        if component_type.lower() in type_patterns:
            patterns.extend(type_patterns[component_type.lower()])
            
        return patterns
    
    def _should_skip_file(self, file_path: Path) -> bool:
        """Check if file should be skipped"""
        skip_patterns = [
            'node_modules',
            '.git',
            'dist',
            'build',
            '.cache',
            'vendor',
            'lib/external'
        ]
        
        path_str = str(file_path)
        return any(pattern in path_str for pattern in skip_patterns)
    
    def _score_component(
        self,
        match: Dict[str, Any],
        requirements: Dict[str, Any]
    ) -> ComponentMatch:
        """Score a component match"""
        file_path = match['file_path']
        content = match['content']
        
        # Extract component name
        component_name = self._extract_component_name(file_path, content)
        
        # Calculate scores
        functionality_score = self._calculate_functionality_score(
            content,
            requirements.get('functionality', '')
        )
        
        interface_score = self._calculate_interface_score(
            content,
            requirements.get('interface', {})
        )
        
        modification_effort = self._calculate_modification_effort(
            content,
            requirements
        )
        
        # Calculate overall match score
        match_score = (
            functionality_score * 0.5 +
            interface_score * 0.3 +
            (100 - modification_effort) * 0.2
        )
        
        # Extract relevant code snippet
        snippet = self._extract_relevant_snippet(content, match['pattern_matched'])
        
        return ComponentMatch(
            file_path=file_path,
            component_name=component_name,
            match_score=match_score,
            functionality_score=functionality_score,
            interface_score=interface_score,
            modification_effort=modification_effort,
            match_details={
                'pattern_matched': match['pattern_matched'],
                'file_size': len(content),
                'complexity': self._estimate_complexity(content)
            },
            code_snippet=snippet
        )
    
    def _extract_component_name(self, file_path: Path, content: str) -> str:
        """Extract component name from file or content"""
        # Try to find function/class name
        func_match = re.search(r'function\s+(\w+)', content)
        class_match = re.search(r'class\s+(\w+)', content)
        export_match = re.search(r'export\s+(?:default\s+)?(?:function|class|const)\s+(\w+)', content)
        
        if export_match:
            return export_match.group(1)
        elif class_match:
            return class_match.group(1)
        elif func_match:
            return func_match.group(1)
        else:
            # Use filename without extension
            return file_path.stem
    
    def _calculate_functionality_score(self, content: str, functionality: str) -> float:
        """Calculate how well the component matches required functionality"""
        if not functionality:
            return 50.0
            
        score = 0.0
        func_words = functionality.lower().split()
        content_lower = content.lower()
        
        # Check for keyword matches
        matched_words = 0
        for word in func_words:
            if len(word) > 3 and word in content_lower:
                matched_words += 1
                
        if func_words:
            score = (matched_words / len(func_words)) * 100
            
        # Bonus for exact phrase matches
        if functionality.lower() in content_lower:
            score = min(100, score + 20)
            
        return score
    
    def _calculate_interface_score(self, content: str, interface_needs: Dict[str, Any]) -> float:
        """Calculate interface compatibility score"""
        if not interface_needs:
            return 70.0  # Default score if no specific interface needs
            
        score = 0.0
        checks = 0
        
        # Check for required methods
        if 'methods' in interface_needs:
            for method in interface_needs['methods']:
                checks += 1
                if re.search(rf'\b{method}\s*\(', content):
                    score += 100
                    
        # Check for required properties
        if 'properties' in interface_needs:
            for prop in interface_needs['properties']:
                checks += 1
                if re.search(rf'\b{prop}\b', content):
                    score += 100
                    
        # Check for required events
        if 'events' in interface_needs:
            for event in interface_needs['events']:
                checks += 1
                if event in content:
                    score += 100
                    
        return (score / checks) if checks > 0 else 70.0
    
    def _calculate_modification_effort(self, content: str, requirements: Dict[str, Any]) -> float:
        """Estimate effort required to modify component (0=easy, 100=hard)"""
        effort = 0.0
        
        # File size factor
        lines = content.count('\n')
        if lines > 500:
            effort += 30
        elif lines > 200:
            effort += 15
        elif lines > 100:
            effort += 5
            
        # Complexity factors
        complexity = self._estimate_complexity(content)
        effort += complexity * 0.5
        
        # Dependencies factor
        import_count = content.count('import ')
        require_count = content.count('require(')
        dependency_score = (import_count + require_count) * 2
        effort += min(20, dependency_score)
        
        # Tight coupling factor
        if 'webflow' in content.lower():
            effort += 10  # Webflow-specific code is harder to modify
            
        return min(100, effort)
    
    def _estimate_complexity(self, content: str) -> float:
        """Estimate code complexity (0-100)"""
        complexity = 0.0
        
        # Count complex patterns
        patterns = [
            (r'if\s*\(', 2),  # Conditionals
            (r'for\s*\(', 3),  # Loops
            (r'while\s*\(', 3),  # While loops
            (r'switch\s*\(', 4),  # Switch statements
            (r'try\s*\{', 3),  # Try-catch blocks
            (r'=>', 1),  # Arrow functions
            (r'async\s+', 2),  # Async functions
            (r'Promise', 2),  # Promises
            (r'setTimeout|setInterval', 2),  # Timers
        ]
        
        for pattern, weight in patterns:
            matches = len(re.findall(pattern, content))
            complexity += matches * weight
            
        # Normalize to 0-100
        return min(100, complexity)
    
    def _extract_relevant_snippet(self, content: str, pattern: str) -> str:
        """Extract relevant code snippet around the matched pattern"""
        lines = content.split('\n')
        
        # Find line with pattern match
        match_line = -1
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                match_line = i
                break
                
        if match_line == -1:
            return ""
            
        # Extract context (10 lines before and after)
        start = max(0, match_line - 10)
        end = min(len(lines), match_line + 11)
        
        snippet_lines = lines[start:end]
        return '\n'.join(snippet_lines)
    
    def _generate_summary(self, matches: List[ComponentMatch], requirements: Dict[str, Any]) -> str:
        """Generate analysis summary"""
        if not matches:
            return f"No existing components found matching '{requirements.get('functionality', 'requirements')}'. New file creation may be justified."
            
        best = matches[0]
        summary = f"Found {len(matches)} potential matches for reuse.\n\n"
        
        if best.match_score >= 80:
            summary += f"✅ STRONG MATCH: {best.component_name} in {best.file_path.relative_to(self.project_root)}\n"
            summary += f"   - Functionality match: {best.functionality_score:.0f}%\n"
            summary += f"   - Interface compatibility: {best.interface_score:.0f}%\n"
            summary += f"   - Modification effort: {best.modification_effort:.0f}% (lower is better)\n"
            summary += f"   - Recommendation: Extend this component instead of creating new file\n"
        elif best.match_score >= 60:
            summary += f"⚠️  GOOD MATCH: {best.component_name} in {best.file_path.relative_to(self.project_root)}\n"
            summary += f"   - Consider extending with modifications\n"
            summary += f"   - Estimated effort: {best.modification_effort:.0f}%\n"
        else:
            summary += f"❌ WEAK MATCHES: Best match only {best.match_score:.0f}% compatible\n"
            summary += f"   - New file creation may be justified with proper documentation\n"
            
        # Add other notable matches
        if len(matches) > 1:
            summary += f"\nOther matches to consider:\n"
            for match in matches[1:4]:  # Show top 3 alternatives
                summary += f"   - {match.component_name}: {match.match_score:.0f}% match\n"
                
        return summary
    
    def get_extension_recommendations(self, component_match: ComponentMatch) -> Dict[str, Any]:
        """
        Provide specific recommendations for extending a component
        
        Args:
            component_match: The component to extend
            
        Returns:
            Dict with extension strategy and code examples
        """
        recommendations = {
            'strategy': '',
            'steps': [],
            'code_examples': {},
            'warnings': []
        }
        
        # Determine extension strategy based on component structure
        content = component_match.file_path.read_text()
        
        if 'class' in content:
            recommendations['strategy'] = 'CLASS_EXTENSION'
            recommendations['steps'] = [
                'Create a new class that extends the existing component',
                'Override only the methods that need different behavior',
                'Call super() to reuse parent functionality',
                'Export the extended class for use'
            ]
            recommendations['code_examples']['class_extension'] = """
// Extend existing component
import { OriginalComponent } from './path/to/component';

class ExtendedComponent extends OriginalComponent {
    constructor(options) {
        super(options);
        // Add new properties
    }
    
    // Override specific method
    methodToChange() {
        // New behavior
        super.methodToChange(); // Call parent if needed
    }
}

export default ExtendedComponent;
"""
        elif 'export' in content and 'function' in content:
            recommendations['strategy'] = 'FUNCTION_WRAPPER'
            recommendations['steps'] = [
                'Import the existing function',
                'Create a wrapper function that calls the original',
                'Add pre/post processing as needed',
                'Export the wrapper function'
            ]
            recommendations['code_examples']['function_wrapper'] = """
// Wrap existing function
import { originalFunction } from './path/to/function';

export function enhancedFunction(params) {
    // Pre-processing
    const processedParams = { ...params, newOption: true };
    
    // Call original
    const result = originalFunction(processedParams);
    
    // Post-processing
    return { ...result, enhanced: true };
}
"""
        else:
            recommendations['strategy'] = 'MODULE_COMPOSITION'
            recommendations['steps'] = [
                'Import the existing module',
                'Create a new module that uses the original',
                'Compose new functionality with existing',
                'Export a unified interface'
            ]
            
        # Add warnings based on modification effort
        if component_match.modification_effort > 70:
            recommendations['warnings'].append(
                "High modification effort detected. Consider careful planning before extending."
            )
            
        if 'webflow' in content.lower():
            recommendations['warnings'].append(
                "Webflow-specific code detected. Ensure extensions maintain platform compatibility."
            )
            
        return recommendations