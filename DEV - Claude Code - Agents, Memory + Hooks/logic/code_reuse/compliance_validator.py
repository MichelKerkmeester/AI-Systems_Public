#!/usr/bin/env python3
"""
Compliance Validator - Rule Enforcement System
Validates that new code follows established patterns and principles
"""

import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ValidationIssue:
    """Represents a compliance validation issue"""
    severity: str  # 'error', 'warning', 'info'
    category: str  # 'pattern', 'principle', 'security', 'performance'
    rule: str
    message: str
    file_path: Optional[Path] = None
    line_number: Optional[int] = None
    code_snippet: Optional[str] = None
    fix_suggestion: Optional[str] = None


@dataclass
class ValidationResult:
    """Result of compliance validation"""
    is_compliant: bool
    issues: List[ValidationIssue] = field(default_factory=list)
    score: float = 100.0  # Compliance score 0-100
    summary: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    @property
    def error_count(self) -> int:
        return len([i for i in self.issues if i.severity == 'error'])
    
    @property
    def warning_count(self) -> int:
        return len([i for i in self.issues if i.severity == 'warning'])


class ComplianceValidator:
    """Rule enforcement system for code compliance"""
    
    def __init__(self, claude_path: Path = None):
        """Initialize compliance validator"""
        if claude_path is None:
            # Find .claude directory
            current = Path.cwd()
            while not (current / ".claude").exists() and current != current.parent:
                current = current.parent
            self.claude_path = current / ".claude"
        else:
            self.claude_path = claude_path
            
        self.project_root = self.claude_path.parent
        
        # Load rules and patterns
        self._load_compliance_rules()
        
    def _load_compliance_rules(self):
        """Load compliance rules from various sources"""
        # Load from patterns.json
        patterns_path = self.claude_path / "knowledge" / "patterns.json"
        if patterns_path.exists():
            with open(patterns_path, 'r') as f:
                self.patterns = json.load(f)
        else:
            self.patterns = {}
            
        # Load from constraints.json
        constraints_path = self.claude_path / "knowledge" / "constraints.json"
        if constraints_path.exists():
            with open(constraints_path, 'r') as f:
                self.constraints = json.load(f)
        else:
            self.constraints = {}
            
        # Load from CLAUDE.md principles
        self._load_claude_md_rules()
        
    def _load_claude_md_rules(self):
        """Extract rules from CLAUDE.md"""
        self.claude_rules = {
            'principles': {
                'dry': 'DRY (Don\'t Repeat Yourself) - Reuse existing code',
                'kiss': 'KISS (Keep It Simple) - Avoid unnecessary complexity',
                'ownership': 'Full ownership - Complete solutions, not patches',
                'root_cause': 'Fix root causes, not symptoms'
            },
            'file_creation': {
                'prefer_editing': 'ALWAYS prefer editing existing files',
                'exhaustive_search': 'Search exhaustively before creating new files',
                'justification': 'New files require explicit justification'
            },
            'webflow': {
                'no_dom_modify': 'NO modifying DOM structure',
                'data_attributes': 'Use data attributes for selectors',
                'work_with_platform': 'Work with Webflow, never against it'
            }
        }
        
    def validate_code(
        self,
        code: str,
        file_path: Path,
        context: Optional[Dict[str, Any]] = None
    ) -> ValidationResult:
        """
        Validate code against all compliance rules
        
        Args:
            code: The code to validate
            file_path: Path where code will be saved
            context: Optional context (e.g., 'is_new_file', 'component_type')
            
        Returns:
            ValidationResult with all issues found
        """
        issues = []
        
        # Run all validators
        issues.extend(self._validate_patterns(code, file_path))
        issues.extend(self._validate_constraints(code, file_path))
        issues.extend(self._validate_principles(code, file_path, context))
        issues.extend(self._validate_security(code, file_path))
        issues.extend(self._validate_performance(code, file_path))
        
        # Calculate compliance score
        score = self._calculate_compliance_score(issues)
        
        # Determine if compliant (no errors)
        is_compliant = all(issue.severity != 'error' for issue in issues)
        
        # Generate summary
        summary = self._generate_validation_summary(issues, score)
        
        return ValidationResult(
            is_compliant=is_compliant,
            issues=issues,
            score=score,
            summary=summary
        )
    
    def _validate_patterns(self, code: str, file_path: Path) -> List[ValidationIssue]:
        """Validate against established patterns"""
        issues = []
        
        # Check initialization pattern
        if 'DOMContentLoaded' in code and self.patterns.get('initialization'):
            issues.append(ValidationIssue(
                severity='error',
                category='pattern',
                rule='initialization',
                message='Use direct initialization, not DOMContentLoaded',
                code_snippet=self._extract_snippet(code, 'DOMContentLoaded'),
                fix_suggestion='Remove DOMContentLoaded wrapper and call function directly'
            ))
            
        # Check element safety
        if re.search(r'element\.\w+(?!\s*\?\?|\s*&&|\s*\?)', code):
            potential_unsafe = re.findall(r'(element\.\w+)(?!\s*\?\?|\s*&&|\s*\?)', code)
            if potential_unsafe and 'if (element)' not in code:
                issues.append(ValidationIssue(
                    severity='warning',
                    category='pattern',
                    rule='element_safety',
                    message='Always check element existence before use',
                    code_snippet=potential_unsafe[0],
                    fix_suggestion='Add: if (element) { ... } or use optional chaining'
                ))
                
        # Check selector patterns
        if re.search(r'querySelector.*[\'"][#.]\w+-\w+', code):
            issues.append(ValidationIssue(
                severity='warning',
                category='pattern',
                rule='selectors',
                message='Use data attributes instead of class/id selectors',
                fix_suggestion='Use: querySelector(\'[data-component="name"]\')'
            ))
            
        return issues
    
    def _validate_constraints(self, code: str, file_path: Path) -> List[ValidationIssue]:
        """Validate against technical constraints"""
        issues = []
        
        constraints = self.constraints.get('code', {})
        
        # Check for console.log
        if 'console.log' in code and not 'if (DEBUG)' in code:
            issues.append(ValidationIssue(
                severity='error',
                category='constraint',
                rule='no_console',
                message='No console.log in production code',
                code_snippet=self._extract_snippet(code, 'console.log'),
                fix_suggestion='Remove or wrap in: if (DEBUG) { console.log(...) }'
            ))
            
        # Check file size
        lines = code.count('\n')
        max_lines = constraints.get('file_size', '500 lines')
        if lines > 500:
            issues.append(ValidationIssue(
                severity='error',
                category='constraint',
                rule='file_size',
                message=f'File exceeds {max_lines} limit ({lines} lines)',
                fix_suggestion='Split into smaller modules'
            ))
            
        # Check for jQuery usage
        if '$(' in code or 'jQuery' in code:
            # Check if it's necessary
            jquery_uses = re.findall(r'\$\([\'"].*?[\'"]\)', code)
            unnecessary = [use for use in jquery_uses if not self._is_jquery_necessary(use)]
            if unnecessary:
                issues.append(ValidationIssue(
                    severity='warning',
                    category='constraint',
                    rule='no_jquery',
                    message='Avoid jQuery unless necessary',
                    code_snippet=unnecessary[0],
                    fix_suggestion='Use native JavaScript methods'
                ))
                
        # Check CSS units
        css_pixels = re.findall(r'\d+px(?![a-zA-Z])', code)
        if css_pixels and file_path.suffix == '.css':
            issues.append(ValidationIssue(
                severity='error',
                category='constraint',
                rule='css_units',
                message='Use REM units instead of pixels',
                code_snippet=css_pixels[0],
                fix_suggestion='Convert to rem units (1rem = 16px base)'
            ))
            
        return issues
    
    def _validate_principles(
        self,
        code: str,
        file_path: Path,
        context: Optional[Dict[str, Any]]
    ) -> List[ValidationIssue]:
        """Validate against core principles"""
        issues = []
        
        # Check for new file creation
        if context and context.get('is_new_file'):
            if not context.get('justification'):
                issues.append(ValidationIssue(
                    severity='error',
                    category='principle',
                    rule='file_creation',
                    message='New file creation requires explicit justification',
                    fix_suggestion='Provide justification or extend existing file'
                ))
                
        # Check for code duplication (simplified check)
        if context and context.get('similar_code_found'):
            issues.append(ValidationIssue(
                severity='error',
                category='principle',
                rule='dry',
                message='Similar code already exists - violates DRY principle',
                fix_suggestion='Extend or reuse existing component'
            ))
            
        # Check for unnecessary complexity
        complexity_indicators = [
            (r'eval\(', 'Avoid eval() - security risk'),
            (r'with\s*\(', 'Avoid with statement - confusing scope'),
            (r'document\.write', 'Avoid document.write - use modern DOM methods'),
            (r'innerHTML\s*=', 'Consider textContent or createElement for safety')
        ]
        
        for pattern, message in complexity_indicators:
            if re.search(pattern, code):
                issues.append(ValidationIssue(
                    severity='warning',
                    category='principle',
                    rule='kiss',
                    message=message,
                    code_snippet=self._extract_snippet(code, pattern)
                ))
                
        return issues
    
    def _validate_security(self, code: str, file_path: Path) -> List[ValidationIssue]:
        """Validate security compliance"""
        issues = []
        
        security_rules = self.constraints.get('security', {})
        blocked_patterns = security_rules.get('patterns_blocked', [])
        
        # Check for API keys and secrets
        for pattern in blocked_patterns:
            matches = re.findall(pattern, code)
            if matches:
                issues.append(ValidationIssue(
                    severity='error',
                    category='security',
                    rule='api_keys',
                    message='Potential API key or secret detected',
                    code_snippet=f'[REDACTED: {pattern}]',
                    fix_suggestion='Store in .env file, never in code'
                ))
                
        # Check for common security issues
        security_checks = [
            (r'innerHTML\s*=\s*[^\'"]', 'Potential XSS vulnerability with innerHTML'),
            (r'eval\s*\(', 'eval() is a security risk'),
            (r'Function\s*\(.*\)', 'Function constructor is like eval()'),
            (r'setTimeout\s*\([\'"]', 'String argument to setTimeout is evaluated')
        ]
        
        for pattern, message in security_checks:
            if re.search(pattern, code):
                issues.append(ValidationIssue(
                    severity='error',
                    category='security',
                    rule='security_risk',
                    message=message,
                    code_snippet=self._extract_snippet(code, pattern),
                    fix_suggestion='Use safer alternatives'
                ))
                
        return issues
    
    def _validate_performance(self, code: str, file_path: Path) -> List[ValidationIssue]:
        """Validate performance compliance"""
        issues = []
        
        performance_rules = self.constraints.get('performance', {})
        
        # Check for performance anti-patterns
        perf_checks = [
            (r'forEach.*querySelector', 'Avoid querySelector in loops - cache selectors'),
            (r'for.*innerHTML', 'Avoid innerHTML in loops - batch DOM updates'),
            (r'style\.\w+\s*=.*for\s*\(', 'Avoid style changes in loops - use CSS classes'),
            (r'document\.ready.*document\.ready', 'Multiple document ready handlers')
        ]
        
        for pattern, message in perf_checks:
            if re.search(pattern, code, re.DOTALL):
                issues.append(ValidationIssue(
                    severity='warning',
                    category='performance',
                    rule='performance',
                    message=message,
                    code_snippet=self._extract_snippet(code, pattern),
                    fix_suggestion='Optimize for better performance'
                ))
                
        # Check file size against budgets
        if file_path.suffix == '.js':
            size_kb = len(code) / 1024
            js_budget = performance_rules.get('js_budget', '50KB')
            if size_kb > 50:
                issues.append(ValidationIssue(
                    severity='warning',
                    category='performance',
                    rule='file_size_budget',
                    message=f'File size ({size_kb:.1f}KB) exceeds {js_budget} budget',
                    fix_suggestion='Consider code splitting or optimization'
                ))
                
        return issues
    
    def _extract_snippet(self, code: str, pattern: str, context_lines: int = 2) -> str:
        """Extract code snippet around pattern match"""
        lines = code.split('\n')
        
        # Find matching line
        for i, line in enumerate(lines):
            if (isinstance(pattern, str) and pattern in line) or \
               (isinstance(pattern, str) and re.search(pattern, line)):
                # Extract context
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                snippet_lines = lines[start:end]
                
                # Mark the problematic line
                relative_index = i - start
                if relative_index < len(snippet_lines):
                    snippet_lines[relative_index] = f">>> {snippet_lines[relative_index]}"
                    
                return '\n'.join(snippet_lines)
                
        return pattern if isinstance(pattern, str) else ''
    
    def _is_jquery_necessary(self, jquery_usage: str) -> bool:
        """Check if jQuery usage is necessary"""
        # Some jQuery methods don't have simple native equivalents
        necessary_patterns = [
            r'\$\.ajax',
            r'\$\.post',
            r'\$\.get',
            r'\.animate\(',
            r'\.fadeIn\(',
            r'\.fadeOut\(',
            r'\.slideUp\(',
            r'\.slideDown\('
        ]
        
        return any(re.search(pattern, jquery_usage) for pattern in necessary_patterns)
    
    def _calculate_compliance_score(self, issues: List[ValidationIssue]) -> float:
        """Calculate overall compliance score"""
        if not issues:
            return 100.0
            
        # Start with 100 and deduct points
        score = 100.0
        
        # Deduct points based on severity
        for issue in issues:
            if issue.severity == 'error':
                score -= 10
            elif issue.severity == 'warning':
                score -= 5
            else:  # info
                score -= 1
                
        return max(0.0, score)
    
    def _generate_validation_summary(self, issues: List[ValidationIssue], score: float) -> str:
        """Generate validation summary"""
        if not issues:
            return "✅ All compliance checks passed!"
            
        error_count = sum(1 for i in issues if i.severity == 'error')
        warning_count = sum(1 for i in issues if i.severity == 'warning')
        info_count = sum(1 for i in issues if i.severity == 'info')
        
        summary = f"Compliance Score: {score:.1f}/100\n\n"
        
        if error_count > 0:
            summary += f"❌ {error_count} error(s) - must be fixed\n"
        if warning_count > 0:
            summary += f"⚠️  {warning_count} warning(s) - should be addressed\n"
        if info_count > 0:
            summary += f"ℹ️  {info_count} info message(s)\n"
            
        # Group issues by category
        categories = {}
        for issue in issues:
            if issue.category not in categories:
                categories[issue.category] = []
            categories[issue.category].append(issue)
            
        summary += "\nIssues by category:\n"
        for category, category_issues in categories.items():
            summary += f"\n{category.upper()}:\n"
            for issue in category_issues[:3]:  # Show top 3 per category
                summary += f"  - [{issue.severity}] {issue.message}\n"
                
        return summary
    
    def validate_file_creation(
        self,
        file_path: Path,
        justification: Optional[str] = None,
        reuse_analysis: Optional[Dict[str, Any]] = None
    ) -> ValidationResult:
        """
        Validate whether file creation is justified
        
        Args:
            file_path: Path where new file will be created
            justification: Reason for creating new file
            reuse_analysis: Results from reuse analyzer
            
        Returns:
            ValidationResult
        """
        issues = []
        
        # Check if justification provided
        if not justification:
            issues.append(ValidationIssue(
                severity='error',
                category='principle',
                rule='file_creation',
                message='New file creation requires explicit justification',
                fix_suggestion='Provide detailed justification or find existing file to extend'
            ))
            
        # Check if reuse analysis was performed
        if not reuse_analysis:
            issues.append(ValidationIssue(
                severity='error',
                category='principle',
                rule='exhaustive_search',
                message='Must perform reuse analysis before creating new file',
                fix_suggestion='Run reuse analyzer to find existing components'
            ))
        elif reuse_analysis.get('best_match') and reuse_analysis['best_match'].get('score', 0) > 60:
            issues.append(ValidationIssue(
                severity='error',
                category='principle',
                rule='dry',
                message=f"Existing component with {reuse_analysis['best_match']['score']}% match found",
                fix_suggestion='Extend existing component instead of creating new file'
            ))
            
        # Check file naming
        if not self._validate_file_naming(file_path):
            issues.append(ValidationIssue(
                severity='warning',
                category='pattern',
                rule='naming_convention',
                message='File name should follow project conventions',
                fix_suggestion='Use kebab-case for files (e.g., my-component.js)'
            ))
            
        is_compliant = all(issue.severity != 'error' for issue in issues)
        score = 100.0 - (len(issues) * 20)
        
        return ValidationResult(
            is_compliant=is_compliant,
            issues=issues,
            score=max(0, score),
            summary=f"File creation {'approved' if is_compliant else 'blocked'}"
        )
    
    def _validate_file_naming(self, file_path: Path) -> bool:
        """Validate file naming conventions"""
        name = file_path.stem
        
        # Check for kebab-case (allowing some exceptions)
        if file_path.suffix in ['.md', '.MD']:
            # Special files allowed
            allowed_names = ['README', 'CLAUDE', 'CHANGELOG', 'LICENSE']
            if name in allowed_names:
                return True
                
        # General rule: kebab-case
        return re.match(r'^[a-z]+(-[a-z]+)*$', name) is not None