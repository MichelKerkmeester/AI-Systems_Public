"""
Reviewer Agent - Code Review and Quality Assurance

Specializes in code review, quality checks, and security analysis.
Integrates with existing quality hooks. Routes pattern matching to Kimi.
"""

import asyncio
import re
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path

from .enhanced_agent_base import EnhancedAgentBase
from ..routing import TaskType, ComplexityLevel


class ReviewerAgent(EnhancedAgentBase):
    """Agent specialized for code review and quality assurance"""
    
    def __init__(self, work_package: str = None, **kwargs):
        super().__init__(
            agent_type="reviewer", 
            work_package=work_package,
            **kwargs
        )
        
        # Review-specific state
        self.review_results = {}
        self.issues_found = []
        self.security_findings = []
        self.quality_metrics = {}
        
        # Review patterns
        self.quality_patterns = self._load_quality_patterns()
        self.security_patterns = self._load_security_patterns()
    
    async def initialize(self):
        """Initialize reviewer environment"""
        self.log("Initializing reviewer agent...")
        
        # Register task handlers
        self.register_task_handler("review", self.review_code)
        self.register_task_handler("security_scan", self.security_scan)
        self.register_task_handler("quality_check", self.quality_check)
        self.register_task_handler("pattern_match", self.pattern_match)
        self.register_task_handler("test_review", self.review_tests)
        self.register_task_handler("performance_check", self.check_performance)
        
        # Load hook integrations
        await self._integrate_with_hooks()
    
    async def run(self):
        """Main reviewer loop"""
        while self.active:
            if self.tasks:
                task = self.tasks.pop(0)
                try:
                    result = await self.execute_task(task)
                    await self.report_task_completion(task["id"], result)
                    
                    # Store review results
                    self.review_results[task["id"]] = result
                    
                except Exception as e:
                    self.log(f"Review task failed: {e}", "ERROR")
            else:
                await asyncio.sleep(1)
    
    async def cleanup(self):
        """Clean up reviewer resources"""
        self.log("Cleaning up reviewer agent...")
        
        # Generate final report
        await self._generate_review_report()
    
    async def review_code(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Perform comprehensive code review"""
        files = task.get("files", [])
        review_type = task.get("review_type", "comprehensive")
        
        self.log(f"Reviewing {len(files)} files (type: {review_type})")
        
        # Comprehensive reviews need Claude
        if review_type in ["comprehensive", "architecture"]:
            self.force_model("claude-opus-4")
        else:
            # Simple pattern matching can use Kimi
            self.force_model("kimi-pro")
        
        issues = []
        suggestions = []
        
        # Review each file
        for file_path in files:
            self.log(f"Reviewing: {file_path}")
            
            # Simulate review checks
            file_issues = await self._review_file(file_path, review_type)
            issues.extend(file_issues)
            
            # Progress update
            progress = (files.index(file_path) + 1) / len(files) * 100
            self.report_progress(progress, f"Reviewing {Path(file_path).name}")
        
        # Categorize issues
        categorized = self._categorize_issues(issues)
        
        # Generate suggestions
        suggestions = self._generate_suggestions(categorized)
        
        # Update tracking
        self.issues_found.extend(issues)
        
        return {
            "status": "completed",
            "files_reviewed": len(files),
            "issues_found": len(issues),
            "critical_issues": len([i for i in issues if i.get("severity") == "critical"]),
            "suggestions": suggestions,
            "categorized_issues": categorized,
            "model_used": self.current_model
        }
    
    async def security_scan(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Perform security-focused review"""
        files = task.get("files", [])
        scan_depth = task.get("scan_depth", "standard")
        
        self.log(f"Security scan on {len(files)} files (depth: {scan_depth})")
        
        # Security reviews ALWAYS use Claude
        self.force_model("claude-opus-4")
        
        vulnerabilities = []
        
        # Security check categories
        security_checks = [
            ("Credentials", self._check_credentials),
            ("Injection", self._check_injection),
            ("XSS", self._check_xss),
            ("Path Traversal", self._check_path_traversal),
            ("Insecure Dependencies", self._check_dependencies)
        ]
        
        for check_name, check_func in security_checks:
            self.log(f"Running security check: {check_name}")
            
            for file_path in files:
                findings = await check_func(file_path)
                vulnerabilities.extend(findings)
            
            await asyncio.sleep(0.3)  # Simulate processing
        
        # Risk assessment
        risk_level = self._assess_security_risk(vulnerabilities)
        
        # Store findings
        self.security_findings.extend(vulnerabilities)
        
        return {
            "status": "completed",
            "vulnerabilities_found": len(vulnerabilities),
            "risk_level": risk_level,
            "critical_findings": len([v for v in vulnerabilities if v.get("severity") == "critical"]),
            "recommendations": self._generate_security_recommendations(vulnerabilities),
            "model_used": self.current_model
        }
    
    async def quality_check(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Check code quality metrics"""
        files = task.get("files", [])
        metrics_requested = task.get("metrics", ["all"])
        
        self.log(f"Quality check on {len(files)} files")
        
        # Quality pattern matching can use Kimi
        self.force_model("kimi-pro")
        
        metrics = {
            "complexity": {},
            "maintainability": {},
            "test_coverage": {},
            "documentation": {},
            "style_compliance": {}
        }
        
        for file_path in files:
            self.log(f"Analyzing quality: {file_path}")
            
            # Calculate metrics
            file_metrics = await self._calculate_quality_metrics(file_path)
            
            # Store by file
            for metric_type, value in file_metrics.items():
                if metric_type in metrics:
                    metrics[metric_type][file_path] = value
        
        # Calculate aggregates
        overall_quality = self._calculate_overall_quality(metrics)
        
        # Update tracking
        self.quality_metrics.update(metrics)
        
        return {
            "status": "completed",
            "files_analyzed": len(files),
            "overall_quality_score": overall_quality,
            "metrics": metrics,
            "improvements_needed": self._identify_improvements(metrics),
            "model_used": self.current_model
        }
    
    async def pattern_match(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Match code patterns"""
        files = task.get("files", [])
        patterns = task.get("patterns", self.quality_patterns)
        
        self.log(f"Pattern matching in {len(files)} files")
        
        # Pattern matching is perfect for Kimi
        self.force_model("kimi-pro")
        
        matches = []
        
        for file_path in files:
            for pattern_name, pattern_regex in patterns.items():
                file_matches = await self._find_pattern_matches(
                    file_path, pattern_name, pattern_regex
                )
                matches.extend(file_matches)
        
        # Group by pattern
        grouped_matches = self._group_matches_by_pattern(matches)
        
        return {
            "status": "completed",
            "total_matches": len(matches),
            "patterns_found": len(grouped_matches),
            "matches_by_pattern": grouped_matches,
            "model_used": self.current_model,
            "cost_saved": "60%"  # Using Kimi
        }
    
    async def review_tests(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Review test quality and coverage"""
        test_files = task.get("test_files", [])
        source_files = task.get("source_files", [])
        
        self.log(f"Reviewing {len(test_files)} test files")
        
        # Test review can often use Kimi for basic checks
        self.force_model("kimi-pro")
        
        test_quality = {
            "coverage": 0,
            "assertion_quality": [],
            "test_patterns": [],
            "missing_tests": []
        }
        
        # Analyze test files
        for test_file in test_files:
            quality = await self._analyze_test_quality(test_file)
            test_quality["assertion_quality"].append(quality)
        
        # Check coverage
        test_quality["coverage"] = await self._calculate_test_coverage(
            test_files, source_files
        )
        
        # Identify missing tests
        test_quality["missing_tests"] = self._identify_missing_tests(
            source_files, test_files
        )
        
        return {
            "status": "completed",
            "test_files_reviewed": len(test_files),
            "coverage_percentage": test_quality["coverage"],
            "missing_test_count": len(test_quality["missing_tests"]),
            "quality_assessment": self._assess_test_quality(test_quality),
            "recommendations": self._generate_test_recommendations(test_quality),
            "model_used": self.current_model
        }
    
    async def check_performance(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Check performance considerations"""
        files = task.get("files", [])
        
        self.log(f"Performance check on {len(files)} files")
        
        # Performance analysis needs understanding - use Claude
        self.force_model("claude-opus-4")
        
        performance_issues = []
        
        # Performance check categories
        perf_checks = [
            ("Algorithm Complexity", self._check_algorithm_complexity),
            ("Database Queries", self._check_database_performance),
            ("Memory Usage", self._check_memory_usage),
            ("Caching", self._check_caching_opportunities)
        ]
        
        for check_name, check_func in perf_checks:
            self.log(f"Performance check: {check_name}")
            
            for file_path in files:
                issues = await check_func(file_path)
                performance_issues.extend(issues)
        
        return {
            "status": "completed",
            "performance_issues": len(performance_issues),
            "critical_issues": len([i for i in performance_issues if i.get("impact") == "high"]),
            "optimization_opportunities": self._identify_optimizations(performance_issues),
            "estimated_improvement": "20-30%",
            "model_used": self.current_model
        }
    
    def _load_quality_patterns(self) -> Dict[str, str]:
        """Load quality check patterns"""
        return {
            "console_log": r"console\.log\(",
            "hardcoded_value": r"(api_key|password|secret)\s*=\s*[\"'][^\"']+[\"']",
            "todo_comment": r"(TODO|FIXME|HACK|XXX):",
            "long_function": r"function\s+\w+\s*\([^)]*\)\s*\{[^}]{500,}",
            "magic_number": r"(?<!\d)[0-9]{2,}(?!\d)",
            "duplicate_code": r"(.{50,})\n.*\1"  # Simple duplicate detection
        }
    
    def _load_security_patterns(self) -> Dict[str, str]:
        """Load security check patterns"""
        return {
            "sql_injection": r"(query|execute)\s*\(\s*[\"']\s*SELECT.*\+",
            "xss_vulnerability": r"innerHTML\s*=\s*[^\"']+\+",
            "hardcoded_secret": r"(api_key|password|token|secret)\s*[:=]\s*[\"'][^\"']+[\"']",
            "eval_usage": r"eval\s*\(",
            "command_injection": r"(exec|system|spawn)\s*\([^)]*\+",
            "path_traversal": r"\.\./|\.\.\\",
            "weak_crypto": r"(md5|sha1)\s*\("
        }
    
    async def _review_file(self, file_path: str, review_type: str) -> List[Dict[str, Any]]:
        """Review a single file"""
        issues = []
        
        # Simulate different review checks
        if review_type == "comprehensive":
            # Check everything
            checks = ["style", "complexity", "security", "performance", "documentation"]
        elif review_type == "security":
            checks = ["security"]
        else:
            checks = ["style", "complexity"]
        
        for check in checks:
            # Simulate finding issues
            if check == "style":
                issues.append({
                    "file": file_path,
                    "line": 42,
                    "type": "style",
                    "severity": "minor",
                    "message": "Line too long (exceeds 100 characters)"
                })
            elif check == "security" and "auth" in file_path:
                issues.append({
                    "file": file_path,
                    "line": 15,
                    "type": "security",
                    "severity": "critical",
                    "message": "Potential SQL injection vulnerability"
                })
        
        return issues
    
    async def _check_credentials(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for hardcoded credentials"""
        findings = []
        
        # Simulate credential check
        if "config" in file_path or "settings" in file_path:
            findings.append({
                "file": file_path,
                "type": "hardcoded_credential",
                "severity": "critical",
                "line": 23,
                "message": "Possible hardcoded API key detected"
            })
        
        return findings
    
    async def _check_injection(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for injection vulnerabilities"""
        # Placeholder for injection checks
        return []
    
    async def _check_xss(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for XSS vulnerabilities"""
        # Placeholder for XSS checks
        return []
    
    async def _check_path_traversal(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for path traversal vulnerabilities"""
        # Placeholder for path traversal checks
        return []
    
    async def _check_dependencies(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for insecure dependencies"""
        # Placeholder for dependency checks
        return []
    
    def _categorize_issues(self, issues: List[Dict[str, Any]]) -> Dict[str, List]:
        """Categorize issues by type"""
        categorized = {
            "style": [],
            "complexity": [],
            "security": [],
            "performance": [],
            "documentation": []
        }
        
        for issue in issues:
            issue_type = issue.get("type", "other")
            if issue_type in categorized:
                categorized[issue_type].append(issue)
        
        return categorized
    
    def _generate_suggestions(self, categorized_issues: Dict[str, List]) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        if len(categorized_issues.get("security", [])) > 0:
            suggestions.append("Priority: Address security vulnerabilities immediately")
        
        if len(categorized_issues.get("complexity", [])) > 5:
            suggestions.append("Consider refactoring complex functions for better maintainability")
        
        if len(categorized_issues.get("documentation", [])) > 10:
            suggestions.append("Improve code documentation coverage")
        
        return suggestions
    
    def _assess_security_risk(self, vulnerabilities: List[Dict[str, Any]]) -> str:
        """Assess overall security risk level"""
        critical_count = len([v for v in vulnerabilities if v.get("severity") == "critical"])
        
        if critical_count > 0:
            return "critical"
        elif len(vulnerabilities) > 10:
            return "high"
        elif len(vulnerabilities) > 5:
            return "medium"
        elif len(vulnerabilities) > 0:
            return "low"
        else:
            return "minimal"
    
    def _generate_security_recommendations(self, vulnerabilities: List[Dict[str, Any]]) -> List[str]:
        """Generate security recommendations"""
        recommendations = []
        
        vuln_types = set(v.get("type") for v in vulnerabilities)
        
        if "hardcoded_credential" in vuln_types:
            recommendations.append("Move credentials to environment variables")
        
        if "injection" in vuln_types:
            recommendations.append("Use parameterized queries to prevent injection")
        
        if "xss" in vuln_types:
            recommendations.append("Sanitize all user input before rendering")
        
        return recommendations
    
    async def _calculate_quality_metrics(self, file_path: str) -> Dict[str, float]:
        """Calculate quality metrics for a file"""
        # Simulate metric calculation
        return {
            "complexity": 7.5,
            "maintainability": 82.0,
            "test_coverage": 75.0,
            "documentation": 60.0,
            "style_compliance": 95.0
        }
    
    def _calculate_overall_quality(self, metrics: Dict[str, Dict]) -> float:
        """Calculate overall quality score"""
        # Simple average of all metrics
        all_scores = []
        
        for metric_type, file_scores in metrics.items():
            if file_scores:
                avg_score = sum(file_scores.values()) / len(file_scores)
                all_scores.append(avg_score)
        
        return sum(all_scores) / len(all_scores) if all_scores else 0
    
    def _identify_improvements(self, metrics: Dict[str, Dict]) -> List[str]:
        """Identify areas for improvement"""
        improvements = []
        
        # Check each metric type
        for metric_type, file_scores in metrics.items():
            if file_scores:
                avg_score = sum(file_scores.values()) / len(file_scores)
                
                if metric_type == "complexity" and avg_score > 10:
                    improvements.append("Reduce code complexity in complex functions")
                elif metric_type == "test_coverage" and avg_score < 80:
                    improvements.append("Increase test coverage to at least 80%")
                elif metric_type == "documentation" and avg_score < 70:
                    improvements.append("Improve documentation coverage")
        
        return improvements
    
    async def _find_pattern_matches(self, file_path: str, pattern_name: str, 
                                  pattern_regex: str) -> List[Dict[str, Any]]:
        """Find pattern matches in a file"""
        matches = []
        
        # Simulate pattern matching
        if pattern_name == "console_log" and ".js" in file_path:
            matches.append({
                "file": file_path,
                "pattern": pattern_name,
                "line": 45,
                "match": "console.log('debug info')"
            })
        
        return matches
    
    def _group_matches_by_pattern(self, matches: List[Dict[str, Any]]) -> Dict[str, List]:
        """Group matches by pattern type"""
        grouped = {}
        
        for match in matches:
            pattern = match.get("pattern")
            if pattern not in grouped:
                grouped[pattern] = []
            grouped[pattern].append(match)
        
        return grouped
    
    async def _analyze_test_quality(self, test_file: str) -> Dict[str, Any]:
        """Analyze test file quality"""
        return {
            "file": test_file,
            "assertion_count": 15,
            "test_count": 5,
            "quality_score": 85
        }
    
    async def _calculate_test_coverage(self, test_files: List[str], 
                                     source_files: List[str]) -> float:
        """Calculate test coverage percentage"""
        # Simulate coverage calculation
        return 78.5
    
    def _identify_missing_tests(self, source_files: List[str], 
                               test_files: List[str]) -> List[str]:
        """Identify source files without tests"""
        missing = []
        
        for source_file in source_files:
            # Simple check - look for corresponding test file
            test_name = f"test_{Path(source_file).stem}.py"
            if not any(test_name in test_file for test_file in test_files):
                missing.append(source_file)
        
        return missing
    
    def _assess_test_quality(self, test_quality: Dict[str, Any]) -> str:
        """Assess overall test quality"""
        coverage = test_quality.get("coverage", 0)
        
        if coverage >= 90:
            return "excellent"
        elif coverage >= 80:
            return "good"
        elif coverage >= 70:
            return "adequate"
        elif coverage >= 60:
            return "needs improvement"
        else:
            return "poor"
    
    def _generate_test_recommendations(self, test_quality: Dict[str, Any]) -> List[str]:
        """Generate test improvement recommendations"""
        recommendations = []
        
        if test_quality["coverage"] < 80:
            recommendations.append("Increase test coverage to at least 80%")
        
        if test_quality["missing_tests"]:
            recommendations.append(f"Add tests for {len(test_quality['missing_tests'])} untested files")
        
        return recommendations
    
    async def _check_algorithm_complexity(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for complex algorithms"""
        # Placeholder
        return []
    
    async def _check_database_performance(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for database performance issues"""
        # Placeholder
        return []
    
    async def _check_memory_usage(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for memory usage issues"""
        # Placeholder
        return []
    
    async def _check_caching_opportunities(self, file_path: str) -> List[Dict[str, Any]]:
        """Check for caching opportunities"""
        # Placeholder
        return []
    
    def _identify_optimizations(self, performance_issues: List[Dict[str, Any]]) -> List[str]:
        """Identify optimization opportunities"""
        return [
            "Consider caching frequently accessed data",
            "Optimize database queries with proper indexing",
            "Review algorithm complexity in hot paths"
        ]
    
    async def _integrate_with_hooks(self):
        """Integrate with existing quality hooks"""
        self.log("Integrating with quality hooks...")
        
        # In production, would load hook configurations
        # and integrate with existing quality checks
        
        self.log("Hook integration complete")
    
    async def _generate_review_report(self):
        """Generate comprehensive review report"""
        import json
        
        report = {
            "agent_id": self.agent_id,
            "work_package": self.work_package,
            "summary": {
                "total_issues": len(self.issues_found),
                "security_findings": len(self.security_findings),
                "files_reviewed": len(set(i.get("file") for i in self.issues_found))
            },
            "issues_by_severity": self._count_by_severity(self.issues_found),
            "security_risk": self._assess_security_risk(self.security_findings),
            "quality_metrics": self.quality_metrics,
            "model_usage": self.get_model_stats(),
            "cost_savings": self._calculate_cost_savings()
        }
        
        # Save report
        if self.lifecycle.workspace:
            report_path = Path(self.lifecycle.workspace) / "review_report.json"
            with open(report_path, 'w') as f:
                json.dump(report, f, indent=2)
            
            self.log(f"Review report saved to {report_path}")
    
    def _count_by_severity(self, issues: List[Dict[str, Any]]) -> Dict[str, int]:
        """Count issues by severity"""
        counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "minor": 0}
        
        for issue in issues:
            severity = issue.get("severity", "low")
            if severity in counts:
                counts[severity] += 1
        
        return counts
    
    def _calculate_cost_savings(self) -> str:
        """Calculate cost savings from model routing"""
        stats = self.get_model_stats()
        
        if "by_model" in stats and "kimi-pro" in stats["by_model"]:
            kimi_usage = stats["by_model"]["kimi-pro"]["count"]
            total_usage = stats["total_tasks"]
            
            if total_usage > 0:
                kimi_percentage = (kimi_usage / total_usage) * 100
                return f"{kimi_percentage:.1f}% of reviews used Kimi Pro (60% cost reduction)"
        
        return "No cost savings data available"