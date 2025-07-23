#!/usr/bin/env python3
"""
Quality Assurance Agent for Unified Agent Architecture v3
Validates code quality, security, and production readiness
"""

import asyncio
import json
import re
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class QualityLevel(Enum):
    """Quality assessment levels"""
    CRITICAL = "critical"    # Security vulnerabilities, major bugs
    HIGH = "high"           # Performance issues, code smells
    MEDIUM = "medium"       # Style violations, minor issues
    LOW = "low"            # Suggestions, improvements

@dataclass
class QualityIssue:
    """Represents a quality issue found"""
    level: QualityLevel
    category: str
    description: str
    file: Optional[str] = None
    line: Optional[int] = None
    suggestion: Optional[str] = None

@dataclass
class QualityReport:
    """Complete quality assessment report"""
    passed: bool
    score: float
    issues: List[QualityIssue]
    security_score: float
    performance_score: float
    maintainability_score: float
    test_coverage: float
    recommendations: List[str]

class QualityAssuranceAgent:
    """Validates code quality and security using Opus for critical paths"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.security_patterns = self._load_security_patterns()
        self.quality_rules = self._load_quality_rules()
        self.opus_client = None  # TODO: Initialize Opus client
        
    async def validate(self, code: str, task_type: str, 
                      context: Dict[str, Any] = None) -> QualityReport:
        """
        Perform comprehensive quality validation
        """
        issues = []
        
        # Run all validators
        security_issues = await self._validate_security(code, context)
        quality_issues = await self._validate_quality(code, context)
        test_issues = await self._validate_tests(code, task_type, context)
        
        issues.extend(security_issues)
        issues.extend(quality_issues)
        issues.extend(test_issues)
        
        # Calculate scores
        security_score = self._calculate_security_score(security_issues)
        performance_score = await self._analyze_performance(code)
        maintainability_score = self._calculate_maintainability(code)
        test_coverage = await self._estimate_test_coverage(code, context)
        
        # Overall assessment
        critical_count = sum(1 for i in issues if i.level == QualityLevel.CRITICAL)
        high_count = sum(1 for i in issues if i.level == QualityLevel.HIGH)
        
        passed = critical_count == 0 and high_count <= 2
        overall_score = (
            security_score * 0.4 +
            performance_score * 0.2 +
            maintainability_score * 0.2 +
            test_coverage * 0.2
        )
        
        # Generate recommendations
        recommendations = self._generate_recommendations(issues, code, context)
        
        # For critical tasks, get Opus validation
        if self._needs_opus_validation(task_type, context, issues):
            opus_feedback = await self._get_opus_validation(code, issues, context)
            recommendations.extend(opus_feedback)
        
        return QualityReport(
            passed=passed,
            score=overall_score,
            issues=issues,
            security_score=security_score,
            performance_score=performance_score,
            maintainability_score=maintainability_score,
            test_coverage=test_coverage,
            recommendations=recommendations
        )
    
    async def _validate_security(self, code: str, context: Dict[str, Any] = None) -> List[QualityIssue]:
        """Validate security aspects of code"""
        issues = []
        
        # Check for hardcoded secrets
        secret_patterns = [
            (r'api[_-]?key\s*=\s*["\'][\w\-]+["\']', "Hardcoded API key detected"),
            (r'password\s*=\s*["\'][^"\']+["\']', "Hardcoded password detected"),
            (r'token\s*=\s*["\'][\w\-]+["\']', "Hardcoded token detected"),
            (r'secret\s*=\s*["\'][^"\']+["\']', "Hardcoded secret detected"),
        ]
        
        for pattern, message in secret_patterns:
            matches = re.finditer(pattern, code, re.IGNORECASE)
            for match in matches:
                line_no = code[:match.start()].count('\n') + 1
                issues.append(QualityIssue(
                    level=QualityLevel.CRITICAL,
                    category="security",
                    description=message,
                    line=line_no,
                    suggestion="Use environment variables or secure key management"
                ))
        
        # SQL injection vulnerabilities
        if re.search(r'(query|execute)\s*\([^)]*%[^)]*\)', code):
            issues.append(QualityIssue(
                level=QualityLevel.CRITICAL,
                category="security",
                description="Potential SQL injection vulnerability",
                suggestion="Use parameterized queries"
            ))
        
        # XSS vulnerabilities
        if 'innerHTML' in code and not 'sanitize' in code:
            issues.append(QualityIssue(
                level=QualityLevel.HIGH,
                category="security",
                description="Potential XSS vulnerability with innerHTML",
                suggestion="Sanitize user input before using innerHTML"
            ))
        
        # Eval usage
        if re.search(r'\beval\s*\(', code):
            issues.append(QualityIssue(
                level=QualityLevel.CRITICAL,
                category="security",
                description="Use of eval() is dangerous",
                suggestion="Refactor to avoid eval()"
            ))
        
        return issues
    
    async def _validate_quality(self, code: str, context: Dict[str, Any] = None) -> List[QualityIssue]:
        """Validate code quality aspects"""
        issues = []
        
        # Check for console.log statements
        console_matches = re.finditer(r'console\.(log|error|warn|info)', code)
        for match in console_matches:
            line_no = code[:match.start()].count('\n') + 1
            issues.append(QualityIssue(
                level=QualityLevel.MEDIUM,
                category="quality",
                description="Console statement found",
                line=line_no,
                suggestion="Remove console statements for production"
            ))
        
        # Check function complexity
        functions = re.findall(r'(def|function|const\s+\w+\s*=\s*\()', code)
        if len(functions) > 0:
            lines = code.split('\n')
            avg_function_length = len(lines) / max(len(functions), 1)
            if avg_function_length > 50:
                issues.append(QualityIssue(
                    level=QualityLevel.HIGH,
                    category="maintainability",
                    description="Functions are too long",
                    suggestion="Break down large functions into smaller ones"
                ))
        
        # Check for proper error handling
        try_blocks = len(re.findall(r'\btry\s*{', code))
        catch_blocks = len(re.findall(r'\bcatch\s*\(', code))
        if try_blocks != catch_blocks:
            issues.append(QualityIssue(
                level=QualityLevel.MEDIUM,
                category="error_handling",
                description="Inconsistent error handling",
                suggestion="Ensure all try blocks have corresponding catch blocks"
            ))
        
        # Check for TODO/FIXME comments
        todo_matches = re.finditer(r'(TODO|FIXME|XXX|HACK):', code)
        for match in todo_matches:
            line_no = code[:match.start()].count('\n') + 1
            issues.append(QualityIssue(
                level=QualityLevel.LOW,
                category="technical_debt",
                description=f"{match.group(1)} comment found",
                line=line_no,
                suggestion="Address technical debt before production"
            ))
        
        return issues
    
    async def _validate_tests(self, code: str, task_type: str, 
                             context: Dict[str, Any] = None) -> List[QualityIssue]:
        """Validate test coverage and quality"""
        issues = []
        
        # Check if tests are included
        has_tests = any(pattern in code for pattern in ['test_', 'describe(', 'it(', '@Test'])
        
        if 'implement' in task_type.lower() and not has_tests:
            issues.append(QualityIssue(
                level=QualityLevel.HIGH,
                category="testing",
                description="No tests found for implementation",
                suggestion="Add comprehensive test coverage"
            ))
        
        # Check test quality if tests exist
        if has_tests:
            # Look for assertions
            assertions = len(re.findall(r'(assert|expect|should)', code))
            test_functions = len(re.findall(r'(test_|it\(|@Test)', code))
            
            if test_functions > 0 and assertions / test_functions < 2:
                issues.append(QualityIssue(
                    level=QualityLevel.MEDIUM,
                    category="testing",
                    description="Tests have insufficient assertions",
                    suggestion="Add more assertions to thoroughly test functionality"
                ))
        
        return issues
    
    def _calculate_security_score(self, issues: List[QualityIssue]) -> float:
        """Calculate security score based on issues"""
        critical_security = sum(1 for i in issues 
                              if i.category == "security" and i.level == QualityLevel.CRITICAL)
        high_security = sum(1 for i in issues 
                          if i.category == "security" and i.level == QualityLevel.HIGH)
        
        # Deduct points for security issues
        score = 1.0
        score -= critical_security * 0.3
        score -= high_security * 0.1
        
        return max(0.0, score)
    
    async def _analyze_performance(self, code: str) -> float:
        """Analyze performance characteristics"""
        score = 1.0
        
        # Check for performance anti-patterns
        if re.search(r'for.*in.*for.*in', code):  # Nested loops
            score -= 0.1
        
        if re.search(r'(\+=|\+\s*=).*loop', code):  # String concatenation in loops
            score -= 0.1
        
        if code.count('await') > 20:  # Too many awaits
            score -= 0.05
        
        return max(0.0, score)
    
    def _calculate_maintainability(self, code: str) -> float:
        """Calculate maintainability score"""
        score = 1.0
        lines = code.split('\n')
        
        # Check line length
        long_lines = sum(1 for line in lines if len(line) > 120)
        if long_lines > len(lines) * 0.1:
            score -= 0.1
        
        # Check nesting depth
        max_indent = max((len(line) - len(line.lstrip())) // 4 
                        for line in lines if line.strip())
        if max_indent > 4:
            score -= 0.15
        
        # Check for documentation
        has_docstrings = '"""' in code or "'''" in code or '/**' in code
        if not has_docstrings:
            score -= 0.1
        
        return max(0.0, score)
    
    async def _estimate_test_coverage(self, code: str, context: Dict[str, Any] = None) -> float:
        """Estimate test coverage percentage"""
        # Simple heuristic-based estimation
        functions = len(re.findall(r'(def\s+\w+|function\s+\w+|const\s+\w+\s*=)', code))
        test_functions = len(re.findall(r'(test_|it\(|describe\()', code))
        
        if functions == 0:
            return 1.0
        
        # Rough estimate: each test function covers one main function
        coverage = min(1.0, test_functions / functions)
        
        # Boost if context indicates good testing
        if context and context.get('has_test_suite'):
            coverage = min(1.0, coverage * 1.2)
        
        return coverage
    
    def _needs_opus_validation(self, task_type: str, context: Dict[str, Any], 
                              issues: List[QualityIssue]) -> bool:
        """Determine if Opus validation is needed"""
        # Always validate security-critical code
        if any(keyword in task_type.lower() 
              for keyword in ['security', 'auth', 'production', 'deploy']):
            return True
        
        # Validate if critical issues found
        if any(i.level == QualityLevel.CRITICAL for i in issues):
            return True
        
        # Validate based on context
        if context and context.get('is_production', False):
            return True
        
        return False
    
    async def _get_opus_validation(self, code: str, issues: List[QualityIssue], 
                                  context: Dict[str, Any]) -> List[str]:
        """Get additional validation from Opus"""
        # TODO: Implement Opus validation
        logger.info("Opus validation requested but not yet implemented")
        return ["Manual review recommended for critical code"]
    
    def _generate_recommendations(self, issues: List[QualityIssue], code: str, 
                                 context: Dict[str, Any]) -> List[str]:
        """Generate actionable recommendations"""
        recommendations = []
        
        # Group issues by category
        categories = {}
        for issue in issues:
            if issue.category not in categories:
                categories[issue.category] = []
            categories[issue.category].append(issue)
        
        # Generate category-specific recommendations
        if 'security' in categories:
            recommendations.append(
                f"🔐 Security: Found {len(categories['security'])} security issues. "
                "Run security scanner and fix all critical vulnerabilities."
            )
        
        if 'testing' in categories:
            recommendations.append(
                f"🧪 Testing: Improve test coverage. "
                "Add unit tests for all new functions and edge cases."
            )
        
        if 'maintainability' in categories:
            recommendations.append(
                f"🛠️ Maintainability: Refactor complex code. "
                "Break down large functions and improve documentation."
            )
        
        # Add general recommendations
        if len(issues) == 0:
            recommendations.append("✅ Code quality is excellent! Ready for review.")
        elif len([i for i in issues if i.level == QualityLevel.CRITICAL]) > 0:
            recommendations.insert(0, "⚠️ CRITICAL issues must be fixed before deployment!")
        
        return recommendations
    
    def _load_security_patterns(self) -> Dict[str, Any]:
        """Load security validation patterns"""
        return {
            'secrets': [
                r'api[_-]?key\s*=',
                r'password\s*=',
                r'token\s*=',
                r'secret\s*='
            ],
            'injections': [
                r'eval\s*\(',
                r'exec\s*\(',
                r'innerHTML\s*=',
                r'dangerouslySetInnerHTML'
            ]
        }
    
    def _load_quality_rules(self) -> Dict[str, Any]:
        """Load quality validation rules"""
        return {
            'max_line_length': 120,
            'max_function_length': 50,
            'max_file_length': 500,
            'max_complexity': 10,
            'required_coverage': 0.8
        }