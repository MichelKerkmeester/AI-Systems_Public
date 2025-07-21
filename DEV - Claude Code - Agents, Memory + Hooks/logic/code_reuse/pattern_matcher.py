#!/usr/bin/env python3
"""
Pattern Matcher - Pattern Reuse Identification Engine
Matches code against established patterns and identifies reuse opportunities
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class PatternViolation:
    """Represents a violation of an established pattern"""
    file_path: Path
    line_number: int
    pattern_name: str
    pattern_rule: str
    actual_code: str
    expected_pattern: str
    severity: str  # 'error', 'warning', 'suggestion'
    fix_suggestion: Optional[str] = None


@dataclass
class PatternMatch:
    """Represents a match with an established pattern"""
    file_path: Path
    line_number: int
    pattern_name: str
    code_snippet: str
    confidence: float  # 0-100
    match_type: str  # 'exact', 'partial', 'similar'


@dataclass
class RefactoringOpportunity:
    """Represents an opportunity to use an existing pattern"""
    file_path: Path
    start_line: int
    end_line: int
    current_code: str
    pattern_name: str
    suggested_code: str
    benefit_score: float  # 0-100
    effort_estimate: str  # 'low', 'medium', 'high'
    description: str


class PatternMatcher:
    """Main pattern matching and reuse identification engine"""
    
    def __init__(self, project_root: Path = None):
        """Initialize pattern matcher"""
        if project_root is None:
            current = Path.cwd()
            while not (current / ".claude").exists() and current != current.parent:
                current = current.parent
            self.project_root = current
        else:
            self.project_root = project_root
            
        self.claude_path = self.project_root / ".claude"
        self.src_path = self.project_root / "src"
        
        # Load patterns
        self.patterns = self._load_patterns()
        self.constraints = self._load_constraints()
        
        # Pattern cache for performance
        self._pattern_cache = {}
        
    def _load_patterns(self) -> Dict[str, Any]:
        """Load patterns from patterns.json"""
        patterns_path = self.claude_path / "knowledge" / "patterns.json"
        
        if patterns_path.exists():
            with open(patterns_path, 'r') as f:
                return json.load(f)
        return {}
    
    def _load_constraints(self) -> Dict[str, Any]:
        """Load constraints from constraints.json"""
        constraints_path = self.claude_path / "knowledge" / "constraints.json"
        
        if constraints_path.exists():
            with open(constraints_path, 'r') as f:
                return json.load(f)
        return {}
    
    def find_pattern_violations(
        self,
        search_paths: Optional[List[Path]] = None,
        pattern_names: Optional[List[str]] = None
    ) -> List[PatternViolation]:
        """
        Find violations of established patterns in the codebase
        
        Args:
            search_paths: Paths to search (defaults to src/)
            pattern_names: Specific patterns to check (defaults to all)
            
        Returns:
            List of pattern violations found
            
        Example:
            matcher = PatternMatcher()
            violations = matcher.find_pattern_violations()
            for v in violations:
                print(f"{v.file_path}:{v.line_number} - {v.pattern_name} violation")
        """
        if search_paths is None:
            search_paths = [self.src_path] if self.src_path.exists() else []
            
        violations = []
        
        # Determine which patterns to check
        patterns_to_check = self.patterns.keys()
        if pattern_names:
            patterns_to_check = [p for p in pattern_names if p in self.patterns]
        
        # Check each file
        for path in search_paths:
            if not path.exists():
                continue
                
            for js_file in path.rglob("*.js"):
                if self._should_skip_file(js_file):
                    continue
                    
                try:
                    content = js_file.read_text()
                    lines = content.split('\n')
                    
                    # Check each pattern
                    for pattern_name in patterns_to_check:
                        pattern_violations = self._check_pattern_in_file(
                            js_file,
                            lines,
                            pattern_name,
                            self.patterns[pattern_name]
                        )
                        violations.extend(pattern_violations)
                        
                except Exception:
                    continue
                    
        return violations
    
    def _check_pattern_in_file(
        self,
        file_path: Path,
        lines: List[str],
        pattern_name: str,
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check a specific pattern in a file"""
        violations = []
        
        # Map pattern names to specific checking functions
        pattern_checkers = {
            'initialization': self._check_initialization_pattern,
            'element_safety': self._check_element_safety_pattern,
            'selectors': self._check_selector_pattern,
            'error_handling': self._check_error_handling_pattern,
            'debugging': self._check_debugging_pattern,
            'animations': self._check_animation_pattern,
        }
        
        if pattern_name in pattern_checkers:
            checker_violations = pattern_checkers[pattern_name](
                file_path,
                lines,
                pattern_config
            )
            violations.extend(checker_violations)
            
        return violations
    
    def _check_initialization_pattern(
        self,
        file_path: Path,
        lines: List[str],
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check initialization pattern violations"""
        violations = []
        avoid_pattern = pattern_config.get('avoid', '')
        
        if not avoid_pattern:
            return violations
            
        for i, line in enumerate(lines):
            if 'DOMContentLoaded' in line and 'addEventListener' in line:
                violations.append(PatternViolation(
                    file_path=file_path,
                    line_number=i + 1,
                    pattern_name='initialization',
                    pattern_rule='Direct init preferred',
                    actual_code=line.strip(),
                    expected_pattern=pattern_config.get('example', ''),
                    severity='warning',
                    fix_suggestion='Use direct initialization: initMyComponent();'
                ))
                
        return violations
    
    def _check_element_safety_pattern(
        self,
        file_path: Path,
        lines: List[str],
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check element safety pattern violations"""
        violations = []
        
        # Look for direct element access without safety check
        for i, line in enumerate(lines):
            # Pattern: element.method() without prior if check
            element_access = re.search(r'(\w+)\.(addEventListener|classList|style|innerHTML)', line)
            if element_access:
                var_name = element_access.group(1)
                
                # Check if there's a safety check in previous lines
                has_safety_check = False
                check_start = max(0, i - 5)  # Look back 5 lines
                
                for j in range(check_start, i):
                    if f'if ({var_name})' in lines[j] or f'if({var_name})' in lines[j]:
                        has_safety_check = True
                        break
                        
                if not has_safety_check and var_name not in ['window', 'document', 'console']:
                    violations.append(PatternViolation(
                        file_path=file_path,
                        line_number=i + 1,
                        pattern_name='element_safety',
                        pattern_rule='Always check element existence',
                        actual_code=line.strip(),
                        expected_pattern='if (element) { element.method(); }',
                        severity='error',
                        fix_suggestion=f'Add safety check: if ({var_name}) {{ {line.strip()} }}'
                    ))
                    
        return violations
    
    def _check_selector_pattern(
        self,
        file_path: Path,
        lines: List[str],
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check selector pattern violations"""
        violations = []
        avoid_patterns = ['.w-', '#w-', 'querySelector(".w-', "querySelector('.w-"]
        
        for i, line in enumerate(lines):
            for avoid in avoid_patterns:
                if avoid in line:
                    violations.append(PatternViolation(
                        file_path=file_path,
                        line_number=i + 1,
                        pattern_name='selectors',
                        pattern_rule='Use data attributes instead of Webflow classes',
                        actual_code=line.strip(),
                        expected_pattern='[data-component="name"]',
                        severity='warning',
                        fix_suggestion='Replace Webflow selector with data attribute'
                    ))
                    break
                    
        return violations
    
    def _check_error_handling_pattern(
        self,
        file_path: Path,
        lines: List[str],
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check error handling pattern violations"""
        violations = []
        
        # Look for try blocks without proper error handling
        in_try_block = False
        try_start_line = 0
        
        for i, line in enumerate(lines):
            if re.search(r'\btry\s*\{', line):
                in_try_block = True
                try_start_line = i
            elif in_try_block and re.search(r'\bcatch\s*\(', line):
                # Check the catch block content
                catch_content = []
                j = i + 1
                brace_count = 1
                
                while j < len(lines) and brace_count > 0:
                    catch_content.append(lines[j])
                    brace_count += lines[j].count('{') - lines[j].count('}')
                    j += 1
                    
                # Check if catch block is empty or only has console.error
                catch_text = ' '.join(catch_content).strip()
                if not catch_text or catch_text == '}':
                    violations.append(PatternViolation(
                        file_path=file_path,
                        line_number=i + 1,
                        pattern_name='error_handling',
                        pattern_rule='Implement graceful degradation',
                        actual_code=f"Empty catch block at line {i + 1}",
                        expected_pattern='catch (error) { /* handle gracefully */ }',
                        severity='warning',
                        fix_suggestion='Add proper error handling or fallback behavior'
                    ))
                    
                in_try_block = False
                
        return violations
    
    def _check_debugging_pattern(
        self,
        file_path: Path,
        lines: List[str],
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check debugging pattern violations"""
        violations = []
        
        for i, line in enumerate(lines):
            # Check for console.log without DEBUG check
            if 'console.log' in line and 'DEBUG' not in line:
                violations.append(PatternViolation(
                    file_path=file_path,
                    line_number=i + 1,
                    pattern_name='debugging',
                    pattern_rule='Wrap console.log in DEBUG check',
                    actual_code=line.strip(),
                    expected_pattern='if (DEBUG) { console.log(...); }',
                    severity='error',
                    fix_suggestion='Wrap in DEBUG check: if (DEBUG) { ' + line.strip() + ' }'
                ))
                
        return violations
    
    def _check_animation_pattern(
        self,
        file_path: Path,
        lines: List[str],
        pattern_config: Dict[str, Any]
    ) -> List[PatternViolation]:
        """Check animation pattern violations"""
        violations = []
        hierarchy = pattern_config.get('hierarchy', [])
        
        # Check for complex animations using basic methods
        for i, line in enumerate(lines):
            # Check for jQuery animate or vanilla JS style animations
            if '.animate(' in line or 'setInterval' in line and 'style' in line:
                violations.append(PatternViolation(
                    file_path=file_path,
                    line_number=i + 1,
                    pattern_name='animations',
                    pattern_rule='Use appropriate animation library',
                    actual_code=line.strip(),
                    expected_pattern='CSS transitions or Motion.dev for animations',
                    severity='suggestion',
                    fix_suggestion='Consider using CSS transitions or Motion.dev'
                ))
                
        return violations
    
    def find_refactoring_opportunities(
        self,
        search_paths: Optional[List[Path]] = None
    ) -> List[RefactoringOpportunity]:
        """
        Find opportunities to refactor code to use existing patterns
        
        Args:
            search_paths: Paths to search (defaults to src/)
            
        Returns:
            List of refactoring opportunities
            
        Example:
            matcher = PatternMatcher()
            opportunities = matcher.find_refactoring_opportunities()
            for opp in opportunities:
                print(f"{opp.file_path} - Use {opp.pattern_name} pattern")
        """
        if search_paths is None:
            search_paths = [self.src_path] if self.src_path.exists() else []
            
        opportunities = []
        
        for path in search_paths:
            if not path.exists():
                continue
                
            for js_file in path.rglob("*.js"):
                if self._should_skip_file(js_file):
                    continue
                    
                try:
                    content = js_file.read_text()
                    
                    # Check for various refactoring opportunities
                    opps = []
                    opps.extend(self._find_initialization_opportunities(js_file, content))
                    opps.extend(self._find_selector_opportunities(js_file, content))
                    opps.extend(self._find_animation_opportunities(js_file, content))
                    opps.extend(self._find_error_handling_opportunities(js_file, content))
                    
                    opportunities.extend(opps)
                    
                except Exception:
                    continue
                    
        # Sort by benefit score
        opportunities.sort(key=lambda x: x.benefit_score, reverse=True)
        
        return opportunities
    
    def _find_initialization_opportunities(
        self,
        file_path: Path,
        content: str
    ) -> List[RefactoringOpportunity]:
        """Find opportunities to improve initialization patterns"""
        opportunities = []
        lines = content.split('\n')
        
        # Look for DOMContentLoaded patterns
        for i, line in enumerate(lines):
            if 'DOMContentLoaded' in line:
                # Find the function being called
                match = re.search(r'addEventListener\([\'"]DOMContentLoaded[\'"]\s*,\s*(\w+)', line)
                if match:
                    func_name = match.group(1)
                    
                    opportunities.append(RefactoringOpportunity(
                        file_path=file_path,
                        start_line=i + 1,
                        end_line=i + 1,
                        current_code=line.strip(),
                        pattern_name='initialization',
                        suggested_code=f'{func_name}();',
                        benefit_score=70,
                        effort_estimate='low',
                        description='Replace DOMContentLoaded with direct initialization'
                    ))
                    
        return opportunities
    
    def _find_selector_opportunities(
        self,
        file_path: Path,
        content: str
    ) -> List[RefactoringOpportunity]:
        """Find opportunities to improve selector patterns"""
        opportunities = []
        lines = content.split('\n')
        
        # Map Webflow classes to suggested data attributes
        webflow_mappings = {
            '.w-nav': '[data-component="nav"]',
            '.w-dropdown': '[data-component="dropdown"]',
            '.w-slider': '[data-component="slider"]',
            '.w-tabs': '[data-component="tabs"]',
            '.w-form': '[data-component="form"]',
        }
        
        for i, line in enumerate(lines):
            for webflow_class, data_attr in webflow_mappings.items():
                if webflow_class in line:
                    # Create suggested replacement
                    suggested = line.replace(webflow_class, data_attr)
                    
                    opportunities.append(RefactoringOpportunity(
                        file_path=file_path,
                        start_line=i + 1,
                        end_line=i + 1,
                        current_code=line.strip(),
                        pattern_name='selectors',
                        suggested_code=suggested.strip(),
                        benefit_score=80,
                        effort_estimate='low',
                        description=f'Replace Webflow class {webflow_class} with data attribute'
                    ))
                    break
                    
        return opportunities
    
    def _find_animation_opportunities(
        self,
        file_path: Path,
        content: str
    ) -> List[RefactoringOpportunity]:
        """Find opportunities to improve animation patterns"""
        opportunities = []
        lines = content.split('\n')
        
        # Look for jQuery animations or manual style animations
        for i, line in enumerate(lines):
            if '.animate(' in line:
                opportunities.append(RefactoringOpportunity(
                    file_path=file_path,
                    start_line=i + 1,
                    end_line=i + 1,
                    current_code=line.strip(),
                    pattern_name='animations',
                    suggested_code='// Use CSS transitions or Motion.dev',
                    benefit_score=60,
                    effort_estimate='medium',
                    description='Replace jQuery animate with modern animation approach'
                ))
            elif 'setInterval' in line and 'style' in line:
                opportunities.append(RefactoringOpportunity(
                    file_path=file_path,
                    start_line=i + 1,
                    end_line=i + 1,
                    current_code=line.strip(),
                    pattern_name='animations',
                    suggested_code='// Use requestAnimationFrame or CSS animations',
                    benefit_score=75,
                    effort_estimate='medium',
                    description='Replace setInterval animation with RAF or CSS'
                ))
                
        return opportunities
    
    def _find_error_handling_opportunities(
        self,
        file_path: Path,
        content: str
    ) -> List[RefactoringOpportunity]:
        """Find opportunities to improve error handling"""
        opportunities = []
        lines = content.split('\n')
        
        # Look for functions without error handling
        function_pattern = r'function\s+(\w+)\s*\([^)]*\)\s*\{'
        async_pattern = r'async\s+function\s+(\w+)\s*\([^)]*\)\s*\{'
        
        for i, line in enumerate(lines):
            # Check for async functions without try-catch
            if re.search(async_pattern, line):
                # Check if function has try-catch
                func_end = self._find_function_end(lines, i)
                func_content = '\n'.join(lines[i:func_end])
                
                if 'try' not in func_content:
                    opportunities.append(RefactoringOpportunity(
                        file_path=file_path,
                        start_line=i + 1,
                        end_line=func_end,
                        current_code=line.strip(),
                        pattern_name='error_handling',
                        suggested_code='// Add try-catch block for async operations',
                        benefit_score=85,
                        effort_estimate='low',
                        description='Add error handling to async function'
                    ))
                    
        return opportunities
    
    def _find_function_end(self, lines: List[str], start_index: int) -> int:
        """Find the end line of a function"""
        brace_count = 0
        for i in range(start_index, len(lines)):
            brace_count += lines[i].count('{') - lines[i].count('}')
            if brace_count == 0 and i > start_index:
                return i + 1
        return len(lines)
    
    def match_code_to_patterns(
        self,
        code_snippet: str,
        pattern_type: Optional[str] = None
    ) -> List[PatternMatch]:
        """
        Match a code snippet against known patterns
        
        Args:
            code_snippet: The code to match
            pattern_type: Optional pattern type to limit matching
            
        Returns:
            List of pattern matches with confidence scores
        """
        matches = []
        
        # Determine which patterns to check
        patterns_to_check = self.patterns
        if pattern_type and pattern_type in self.patterns:
            patterns_to_check = {pattern_type: self.patterns[pattern_type]}
            
        for pattern_name, pattern_config in patterns_to_check.items():
            confidence = self._calculate_pattern_confidence(
                code_snippet,
                pattern_name,
                pattern_config
            )
            
            if confidence > 30:  # Minimum confidence threshold
                match_type = 'exact' if confidence > 90 else 'partial' if confidence > 60 else 'similar'
                
                matches.append(PatternMatch(
                    file_path=Path('snippet'),
                    line_number=1,
                    pattern_name=pattern_name,
                    code_snippet=code_snippet[:100] + '...' if len(code_snippet) > 100 else code_snippet,
                    confidence=confidence,
                    match_type=match_type
                ))
                
        # Sort by confidence
        matches.sort(key=lambda x: x.confidence, reverse=True)
        
        return matches
    
    def _calculate_pattern_confidence(
        self,
        code: str,
        pattern_name: str,
        pattern_config: Dict[str, Any]
    ) -> float:
        """Calculate confidence that code matches a pattern"""
        confidence = 0.0
        
        # Check for pattern example match
        if 'example' in pattern_config:
            example = pattern_config['example']
            if example in code:
                confidence += 50
                
        # Check for avoid patterns (negative match)
        if 'avoid' in pattern_config:
            avoid = pattern_config['avoid']
            if avoid and avoid in code:
                confidence -= 30
                
        # Pattern-specific confidence calculations
        if pattern_name == 'initialization':
            if 'init' in code.lower() and 'function' in code:
                confidence += 30
        elif pattern_name == 'element_safety':
            if 'if (' in code and ('element' in code or 'querySelector' in code):
                confidence += 40
        elif pattern_name == 'selectors':
            if 'data-' in code and 'querySelector' in code:
                confidence += 45
                
        return max(0, min(100, confidence))
    
    def _should_skip_file(self, file_path: Path) -> bool:
        """Check if file should be skipped"""
        skip_patterns = [
            'node_modules',
            '.git',
            'dist',
            'build',
            '.cache',
            'vendor',
            'lib/external',
            'min.js'
        ]
        
        path_str = str(file_path)
        return any(pattern in path_str for pattern in skip_patterns)
    
    def generate_pattern_report(
        self,
        search_paths: Optional[List[Path]] = None
    ) -> Dict[str, Any]:
        """
        Generate a comprehensive pattern usage report
        
        Returns:
            Dict with pattern statistics and recommendations
        """
        if search_paths is None:
            search_paths = [self.src_path] if self.src_path.exists() else []
            
        report = {
            'total_files_analyzed': 0,
            'pattern_violations': {},
            'pattern_adoption': {},
            'refactoring_opportunities': 0,
            'recommendations': []
        }
        
        # Count files
        file_count = 0
        for path in search_paths:
            if path.exists():
                file_count += len(list(path.rglob("*.js")))
        report['total_files_analyzed'] = file_count
        
        # Get violations
        violations = self.find_pattern_violations(search_paths)
        
        # Group violations by pattern
        for violation in violations:
            pattern = violation.pattern_name
            if pattern not in report['pattern_violations']:
                report['pattern_violations'][pattern] = 0
            report['pattern_violations'][pattern] += 1
            
        # Calculate pattern adoption rates
        for pattern_name in self.patterns:
            violations_count = report['pattern_violations'].get(pattern_name, 0)
            adoption_rate = 100 - (violations_count / max(1, file_count)) * 100
            report['pattern_adoption'][pattern_name] = round(adoption_rate, 2)
            
        # Get refactoring opportunities
        opportunities = self.find_refactoring_opportunities(search_paths)
        report['refactoring_opportunities'] = len(opportunities)
        
        # Generate recommendations
        for pattern, adoption in report['pattern_adoption'].items():
            if adoption < 50:
                report['recommendations'].append(
                    f"Low adoption of {pattern} pattern ({adoption}%). "
                    f"Consider team training or automated fixes."
                )
            elif adoption < 80:
                report['recommendations'].append(
                    f"Moderate adoption of {pattern} pattern ({adoption}%). "
                    f"Review and fix remaining violations."
                )
                
        return report