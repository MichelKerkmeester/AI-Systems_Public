#!/usr/bin/env python3
"""
Analysis Agent for Unified Agent Architecture v3
Fast code analysis and pattern detection using Gemini Flash
"""

import asyncio
import json
import re
from typing import Dict, List, Optional, Tuple, Any, Set
from dataclasses import dataclass
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

@dataclass
class CodePattern:
    """Represents a detected code pattern"""
    pattern_type: str
    description: str
    files: List[str]
    occurrences: int
    recommendation: Optional[str] = None

@dataclass
class DependencyInfo:
    """Information about a code dependency"""
    name: str
    version: Optional[str]
    usage_count: int
    files: List[str]

@dataclass
class AnalysisResult:
    """Complete analysis result"""
    summary: str
    patterns: List[CodePattern]
    dependencies: List[DependencyInfo]
    metrics: Dict[str, Any]
    suggestions: List[str]
    reusable_components: List[Dict[str, str]]

class AnalysisAgent:
    """Fast analysis using Gemini Flash for pattern detection and code understanding"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.gemini_client = None  # TODO: Initialize Gemini client
        self.pattern_cache = {}
        
    async def analyze(self, code_or_path: str, analysis_type: str = "general",
                     context: Dict[str, Any] = None) -> AnalysisResult:
        """
        Perform code analysis based on type
        """
        if analysis_type == "pattern_detection":
            return await self._analyze_patterns(code_or_path, context)
        elif analysis_type == "dependency_mapping":
            return await self._analyze_dependencies(code_or_path, context)
        elif analysis_type == "performance":
            return await self._analyze_performance(code_or_path, context)
        elif analysis_type == "reusability":
            return await self._analyze_reusability(code_or_path, context)
        else:
            return await self._general_analysis(code_or_path, context)
    
    async def _analyze_patterns(self, code: str, context: Dict[str, Any] = None) -> AnalysisResult:
        """Detect code patterns and anti-patterns"""
        patterns = []
        
        # Common patterns to detect
        pattern_definitions = [
            {
                'regex': r'class\s+(\w+).*:\s*\n\s*def\s+__init__',
                'type': 'class_definition',
                'description': 'Class with constructor'
            },
            {
                'regex': r'async\s+def\s+\w+.*await',
                'type': 'async_function',
                'description': 'Asynchronous function pattern'
            },
            {
                'regex': r'try:.*except.*finally:',
                'type': 'error_handling',
                'description': 'Complete error handling pattern'
            },
            {
                'regex': r'@\w+\s*\n\s*def\s+\w+',
                'type': 'decorator_usage',
                'description': 'Decorated function pattern'
            },
            {
                'regex': r'if\s+__name__\s*==\s*["\']__main__["\']',
                'type': 'main_guard',
                'description': 'Main execution guard'
            }
        ]
        
        # Detect patterns
        for pattern_def in pattern_definitions:
            matches = re.finditer(pattern_def['regex'], code, re.MULTILINE | re.DOTALL)
            occurrences = sum(1 for _ in matches)
            
            if occurrences > 0:
                patterns.append(CodePattern(
                    pattern_type=pattern_def['type'],
                    description=pattern_def['description'],
                    files=[context.get('file_path', 'unknown')] if context else [],
                    occurrences=occurrences
                ))
        
        # Anti-patterns
        anti_patterns = self._detect_anti_patterns(code)
        patterns.extend(anti_patterns)
        
        # Calculate metrics
        metrics = self._calculate_code_metrics(code)
        
        # Generate suggestions
        suggestions = self._generate_pattern_suggestions(patterns, metrics)
        
        return AnalysisResult(
            summary=f"Found {len(patterns)} patterns in code",
            patterns=patterns,
            dependencies=[],
            metrics=metrics,
            suggestions=suggestions,
            reusable_components=[]
        )
    
    async def _analyze_dependencies(self, code: str, context: Dict[str, Any] = None) -> AnalysisResult:
        """Analyze code dependencies and imports"""
        dependencies = []
        import_pattern = re.compile(
            r'(?:from\s+(\S+)\s+)?import\s+([^#\n]+)'
        )
        
        imports = {}
        for match in import_pattern.finditer(code):
            module = match.group(1) or match.group(2).split()[0]
            if module and not module.startswith('.'):
                base_module = module.split('.')[0]
                if base_module not in imports:
                    imports[base_module] = {
                        'count': 0,
                        'files': set()
                    }
                imports[base_module]['count'] += 1
                if context and 'file_path' in context:
                    imports[base_module]['files'].add(context['file_path'])
        
        # Convert to DependencyInfo objects
        for name, info in imports.items():
            dependencies.append(DependencyInfo(
                name=name,
                version=None,  # TODO: Extract from requirements.txt or package.json
                usage_count=info['count'],
                files=list(info['files'])
            ))
        
        # Analyze dependency health
        suggestions = []
        if len(dependencies) > 20:
            suggestions.append("Consider reducing the number of dependencies")
        
        stdlib_modules = {'os', 'sys', 'json', 're', 'asyncio', 'logging'}
        external_deps = [d for d in dependencies if d.name not in stdlib_modules]
        if len(external_deps) > 10:
            suggestions.append(f"High number of external dependencies ({len(external_deps)})")
        
        return AnalysisResult(
            summary=f"Found {len(dependencies)} dependencies",
            patterns=[],
            dependencies=dependencies,
            metrics={'total_imports': len(dependencies), 'external_deps': len(external_deps)},
            suggestions=suggestions,
            reusable_components=[]
        )
    
    async def _analyze_performance(self, code: str, context: Dict[str, Any] = None) -> AnalysisResult:
        """Analyze performance characteristics"""
        metrics = {}
        suggestions = []
        
        # Check for performance anti-patterns
        performance_checks = [
            {
                'pattern': r'for.*in.*:\s*for.*in.*:',
                'issue': 'Nested loops detected',
                'suggestion': 'Consider optimizing nested loops or using more efficient algorithms'
            },
            {
                'pattern': r'\+=.*(?:for|while)',
                'issue': 'String concatenation in loop',
                'suggestion': 'Use list append and join for better performance'
            },
            {
                'pattern': r'sleep\s*\(',
                'issue': 'Blocking sleep detected',
                'suggestion': 'Use asyncio.sleep for non-blocking delays'
            },
            {
                'pattern': r'global\s+\w+',
                'issue': 'Global variable usage',
                'suggestion': 'Minimize global variable usage for better performance and maintainability'
            }
        ]
        
        issues_found = []
        for check in performance_checks:
            if re.search(check['pattern'], code):
                issues_found.append(check['issue'])
                suggestions.append(check['suggestion'])
        
        # Analyze complexity
        cyclomatic_complexity = self._calculate_cyclomatic_complexity(code)
        if cyclomatic_complexity > 10:
            suggestions.append("High cyclomatic complexity detected. Consider refactoring")
        
        metrics = {
            'cyclomatic_complexity': cyclomatic_complexity,
            'performance_issues': len(issues_found),
            'async_usage': code.count('async') + code.count('await'),
            'loop_count': len(re.findall(r'(?:for|while)\s+', code))
        }
        
        return AnalysisResult(
            summary=f"Performance analysis complete. Found {len(issues_found)} potential issues",
            patterns=[],
            dependencies=[],
            metrics=metrics,
            suggestions=suggestions,
            reusable_components=[]
        )
    
    async def _analyze_reusability(self, code: str, context: Dict[str, Any] = None) -> AnalysisResult:
        """Analyze code for reusable components"""
        reusable_components = []
        
        # Find classes
        class_pattern = re.compile(r'class\s+(\w+).*?(?=class\s+\w+|$)', re.DOTALL)
        for match in class_pattern.finditer(code):
            class_name = match.group(1)
            class_code = match.group(0)
            
            # Check if it's a good candidate for reuse
            if self._is_reusable_class(class_name, class_code):
                reusable_components.append({
                    'type': 'class',
                    'name': class_name,
                    'description': self._extract_docstring(class_code),
                    'file': context.get('file_path', 'unknown') if context else 'unknown'
                })
        
        # Find utility functions
        function_pattern = re.compile(r'def\s+(\w+)\s*\([^)]*\).*?(?=def\s+\w+|class\s+|$)', re.DOTALL)
        for match in function_pattern.finditer(code):
            func_name = match.group(1)
            func_code = match.group(0)
            
            if self._is_reusable_function(func_name, func_code):
                reusable_components.append({
                    'type': 'function',
                    'name': func_name,
                    'description': self._extract_docstring(func_code),
                    'file': context.get('file_path', 'unknown') if context else 'unknown'
                })
        
        # Find constants and configurations
        const_pattern = re.compile(r'^([A-Z_]+)\s*=\s*(.+)$', re.MULTILINE)
        for match in const_pattern.finditer(code):
            const_name = match.group(1)
            reusable_components.append({
                'type': 'constant',
                'name': const_name,
                'description': f'Configuration constant: {const_name}',
                'file': context.get('file_path', 'unknown') if context else 'unknown'
            })
        
        suggestions = []
        if len(reusable_components) > 0:
            suggestions.append(f"Found {len(reusable_components)} reusable components")
            suggestions.append("Consider extracting these to a shared module")
        
        return AnalysisResult(
            summary=f"Identified {len(reusable_components)} reusable components",
            patterns=[],
            dependencies=[],
            metrics={'reusable_count': len(reusable_components)},
            suggestions=suggestions,
            reusable_components=reusable_components
        )
    
    async def _general_analysis(self, code: str, context: Dict[str, Any] = None) -> AnalysisResult:
        """Perform general code analysis"""
        # Combine all analysis types
        pattern_result = await self._analyze_patterns(code, context)
        dep_result = await self._analyze_dependencies(code, context)
        perf_result = await self._analyze_performance(code, context)
        reuse_result = await self._analyze_reusability(code, context)
        
        # Merge results
        all_patterns = pattern_result.patterns
        all_deps = dep_result.dependencies
        all_suggestions = (
            pattern_result.suggestions +
            dep_result.suggestions +
            perf_result.suggestions +
            reuse_result.suggestions
        )
        
        all_metrics = {
            **pattern_result.metrics,
            **dep_result.metrics,
            **perf_result.metrics,
            **reuse_result.metrics
        }
        
        summary = (
            f"Complete analysis: {len(all_patterns)} patterns, "
            f"{len(all_deps)} dependencies, "
            f"{len(reuse_result.reusable_components)} reusable components"
        )
        
        return AnalysisResult(
            summary=summary,
            patterns=all_patterns,
            dependencies=all_deps,
            metrics=all_metrics,
            suggestions=list(set(all_suggestions)),  # Remove duplicates
            reusable_components=reuse_result.reusable_components
        )
    
    def _detect_anti_patterns(self, code: str) -> List[CodePattern]:
        """Detect common anti-patterns"""
        anti_patterns = []
        
        # God class/function
        lines = code.split('\n')
        if len(lines) > 500:
            anti_patterns.append(CodePattern(
                pattern_type='god_object',
                description='File/class too large',
                files=[],
                occurrences=1,
                recommendation='Consider splitting into smaller modules'
            ))
        
        # Deeply nested code
        max_indent = max((len(line) - len(line.lstrip())) for line in lines if line.strip())
        if max_indent > 16:  # 4 levels of indentation
            anti_patterns.append(CodePattern(
                pattern_type='deep_nesting',
                description='Deeply nested code detected',
                files=[],
                occurrences=1,
                recommendation='Refactor to reduce nesting levels'
            ))
        
        # Magic numbers
        magic_numbers = re.findall(r'(?<![a-zA-Z0-9_])\d{2,}(?![a-zA-Z0-9_])', code)
        if len(magic_numbers) > 5:
            anti_patterns.append(CodePattern(
                pattern_type='magic_numbers',
                description='Multiple magic numbers found',
                files=[],
                occurrences=len(magic_numbers),
                recommendation='Extract magic numbers to named constants'
            ))
        
        return anti_patterns
    
    def _calculate_code_metrics(self, code: str) -> Dict[str, Any]:
        """Calculate various code metrics"""
        lines = code.split('\n')
        
        return {
            'total_lines': len(lines),
            'code_lines': len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
            'blank_lines': len([l for l in lines if not l.strip()]),
            'functions': len(re.findall(r'def\s+\w+', code)),
            'classes': len(re.findall(r'class\s+\w+', code)),
            'imports': len(re.findall(r'^(?:from|import)\s+', code, re.MULTILINE))
        }
    
    def _calculate_cyclomatic_complexity(self, code: str) -> int:
        """Simple cyclomatic complexity calculation"""
        # Count decision points
        complexity = 1  # Base complexity
        
        # Add complexity for each decision point
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b',
            r'\bor\b'
        ]
        
        for pattern in decision_patterns:
            complexity += len(re.findall(pattern, code))
        
        return complexity
    
    def _generate_pattern_suggestions(self, patterns: List[CodePattern], 
                                    metrics: Dict[str, Any]) -> List[str]:
        """Generate suggestions based on detected patterns"""
        suggestions = []
        
        # Check for missing patterns
        pattern_types = {p.pattern_type for p in patterns}
        
        if 'error_handling' not in pattern_types and metrics.get('functions', 0) > 3:
            suggestions.append("Consider adding error handling to functions")
        
        if 'main_guard' not in pattern_types and metrics.get('functions', 0) > 0:
            suggestions.append("Add if __name__ == '__main__' guard for script execution")
        
        if 'async_function' in pattern_types and 'error_handling' not in pattern_types:
            suggestions.append("Async functions should have proper error handling")
        
        return suggestions
    
    def _is_reusable_class(self, name: str, code: str) -> bool:
        """Check if a class is a good candidate for reuse"""
        # Skip test classes
        if name.startswith('Test') or name.endswith('Test'):
            return False
        
        # Skip private classes
        if name.startswith('_'):
            return False
        
        # Check for generic functionality
        generic_indicators = ['Base', 'Abstract', 'Mixin', 'Helper', 'Util', 'Manager']
        return any(indicator in name for indicator in generic_indicators)
    
    def _is_reusable_function(self, name: str, code: str) -> bool:
        """Check if a function is a good candidate for reuse"""
        # Skip test functions
        if name.startswith('test_'):
            return False
        
        # Skip private functions
        if name.startswith('_'):
            return False
        
        # Skip very short functions
        if len(code.split('\n')) < 5:
            return False
        
        # Check for utility indicators
        util_indicators = ['parse', 'format', 'validate', 'convert', 'calculate', 'get', 'set']
        return any(indicator in name.lower() for indicator in util_indicators)
    
    def _extract_docstring(self, code: str) -> str:
        """Extract docstring from code"""
        docstring_match = re.search(r'"""(.*?)"""', code, re.DOTALL)
        if docstring_match:
            return docstring_match.group(1).strip()
        
        docstring_match = re.search(r"'''(.*?)'''", code, re.DOTALL)
        if docstring_match:
            return docstring_match.group(1).strip()
        
        return "No description available"