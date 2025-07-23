# Quality Assurance Agent Specification

## Executive Summary
This specification defines a Claude Opus-powered QA agent that performs final quality checks, validates code against knowledge files, ensures compliance with all system rules, and maintains the highest standards of code quality.

## QA Agent Architecture

### Core Responsibilities
```
┌─────────────────────────────────────────────────┐
│          QA Agent (Claude Opus)                  │
├─────────────────────────────────────────────────┤
│ • Final code review and validation              │
│ • Knowledge file compliance checking            │
│ • Security vulnerability scanning               │
│ • Performance impact analysis                   │
│ • Test generation and validation                │
│ • Cross-agent result verification               │
└─────────────────────────────────────────────────┘
                    │
     ┌──────────────┼──────────────┬───────────────┐
     │              │              │               │
┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐  ┌─────▼────┐
│Knowledge │  │Security  │  │Test      │  │Style     │
│Validator │  │Scanner   │  │Generator │  │Checker   │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
```

### Integration Points
- Reviews output from all other agents
- Validates against knowledge files
- Ensures hook compliance
- Generates comprehensive test suites

## Quality Validation Pipeline

### 1. Knowledge File Compliance
```python
class KnowledgeValidator:
    """Validate code against knowledge files"""
    
    def __init__(self):
        self.facts = self.load_knowledge('facts.json')
        self.patterns = self.load_knowledge('patterns.json')
        self.constraints = self.load_knowledge('constraints.json')
        
    async def validate_compliance(self, code: str, file_path: str) -> dict:
        """Comprehensive knowledge validation"""
        
        violations = []
        
        # 1. Check platform constraints
        platform_violations = self.check_platform_rules(code, file_path)
        violations.extend(platform_violations)
        
        # 2. Validate patterns
        pattern_violations = self.check_patterns(code)
        violations.extend(pattern_violations)
        
        # 3. Check strict rules
        strict_violations = self.check_strict_rules(code, file_path)
        violations.extend(strict_violations)
        
        # 4. Generate fixes
        fixes = await self.generate_fixes(violations)
        
        return {
            'compliant': len(violations) == 0,
            'violations': violations,
            'fixes': fixes,
            'severity': self.calculate_severity(violations)
        }
    
    def check_platform_rules(self, code: str, file_path: str) -> list:
        """Check Slater platform rules"""
        
        violations = []
        
        # NO DOMContentLoaded rule
        if 'DOMContentLoaded' in code:
            # Check if it's the allowed exception
            if not file_path.endswith('/src/B__global/global.html'):
                violations.append({
                    'rule': 'no_domcontentloaded',
                    'severity': 'CRITICAL',
                    'message': 'DOMContentLoaded not allowed - Slater autoloads',
                    'line': self.find_line_number(code, 'DOMContentLoaded'),
                    'fix': self.suggest_slater_pattern(code)
                })
                
        # File size limit
        if len(code.split('\n')) > 500:
            violations.append({
                'rule': 'file_size_limit',
                'severity': 'HIGH',
                'message': 'File exceeds 500 line limit',
                'suggestion': 'Split into modules'
            })
            
        return violations
```

### 2. Security Scanning
```python
class SecurityScanner:
    """Scan for security vulnerabilities"""
    
    VULNERABILITY_PATTERNS = {
        'hardcoded_secrets': [
            r'api[_-]?key\s*[:=]\s*["\'][^"\']+["\']',
            r'password\s*[:=]\s*["\'][^"\']+["\']',
            r'token\s*[:=]\s*["\'][^"\']+["\']'
        ],
        'unsafe_eval': [
            r'eval\s*\(',
            r'new\s+Function\s*\(',
            r'setTimeout\s*\([^,]+,\s*[^0-9]'
        ],
        'xss_vulnerable': [
            r'\.innerHTML\s*=\s*[^`]',
            r'document\.write\s*\(',
            r'\.outerHTML\s*='
        ],
        'sql_injection': [
            r'query\s*\([^?]+\+',
            r'execute\s*\([^?]+\$\{',
        ]
    }
    
    async def scan_security(self, code: str) -> dict:
        """Comprehensive security scan"""
        
        vulnerabilities = []
        
        for vuln_type, patterns in self.VULNERABILITY_PATTERNS.items():
            for pattern in patterns:
                matches = re.finditer(pattern, code, re.IGNORECASE)
                for match in matches:
                    vulnerabilities.append({
                        'type': vuln_type,
                        'pattern': pattern,
                        'location': match.span(),
                        'line': code[:match.start()].count('\n') + 1,
                        'severity': self.get_severity(vuln_type),
                        'fix': await self.generate_secure_alternative(
                            code[match.start():match.end()], 
                            vuln_type
                        )
                    })
                    
        # Additional checks
        vulnerabilities.extend(await self.check_dependencies(code))
        vulnerabilities.extend(await self.check_permissions(code))
        
        return {
            'secure': len(vulnerabilities) == 0,
            'vulnerabilities': vulnerabilities,
            'risk_score': self.calculate_risk_score(vulnerabilities),
            'recommendations': await self.generate_security_recommendations(vulnerabilities)
        }
```

### 3. Test Generation and Validation
```python
class TestGenerator:
    """Generate comprehensive test suites"""
    
    async def generate_tests(self, code: str, context: dict) -> dict:
        """Generate appropriate tests for code"""
        
        # Analyze code structure
        analysis = self.analyze_code_structure(code)
        
        # Determine test framework
        framework = self.detect_test_framework(context)
        
        # Generate test cases
        test_cases = []
        
        # 1. Unit tests for functions
        for func in analysis['functions']:
            test_cases.append(await self.generate_unit_test(func, framework))
            
        # 2. Integration tests for components
        for component in analysis['components']:
            test_cases.append(await self.generate_integration_test(component, framework))
            
        # 3. Edge case tests
        edge_cases = await self.generate_edge_cases(analysis)
        test_cases.extend(edge_cases)
        
        # 4. Security tests
        security_tests = await self.generate_security_tests(code)
        test_cases.extend(security_tests)
        
        return {
            'framework': framework,
            'test_suite': self.format_test_suite(test_cases, framework),
            'coverage_estimate': self.estimate_coverage(test_cases, analysis),
            'run_command': self.get_test_command(framework)
        }
```

### 4. Performance Analysis
```python
class PerformanceAnalyzer:
    """Analyze performance impact of code changes"""
    
    async def analyze_performance(self, code: str, original: str = None) -> dict:
        """Comprehensive performance analysis"""
        
        metrics = {
            'complexity': self.calculate_complexity(code),
            'memory_usage': await self.estimate_memory_usage(code),
            'execution_time': await self.estimate_execution_time(code),
            'bundle_impact': self.calculate_bundle_impact(code)
        }
        
        # Compare with original if provided
        if original:
            metrics['delta'] = {
                'complexity': metrics['complexity'] - self.calculate_complexity(original),
                'memory_usage': metrics['memory_usage'] - await self.estimate_memory_usage(original),
                'bundle_impact': metrics['bundle_impact'] - self.calculate_bundle_impact(original)
            }
            
        # Identify bottlenecks
        bottlenecks = self.identify_bottlenecks(code)
        
        # Generate optimizations
        optimizations = await self.suggest_optimizations(code, bottlenecks)
        
        return {
            'metrics': metrics,
            'bottlenecks': bottlenecks,
            'optimizations': optimizations,
            'performance_score': self.calculate_performance_score(metrics)
        }
```

## Multi-Agent Result Verification

### 1. Cross-Agent Validation
```python
class CrossAgentValidator:
    """Validate results across multiple agents"""
    
    async def validate_agent_results(self, results: dict) -> dict:
        """Verify consistency across agent outputs"""
        
        validations = {}
        
        # 1. Check implementation matches analysis
        if 'analysis' in results and 'implementation' in results:
            validations['analysis_implementation'] = await self.validate_consistency(
                results['analysis'],
                results['implementation']
            )
            
        # 2. Verify documentation matches code
        if 'documentation' in results and 'implementation' in results:
            validations['doc_code_sync'] = await self.validate_doc_accuracy(
                results['documentation'],
                results['implementation']
            )
            
        # 3. Check debug results match fixes
        if 'debug' in results and 'fixes' in results:
            validations['debug_fix_alignment'] = await self.validate_debug_fixes(
                results['debug'],
                results['fixes']
            )
            
        # 4. Overall consistency score
        consistency_score = self.calculate_consistency_score(validations)
        
        return {
            'validations': validations,
            'consistency_score': consistency_score,
            'issues': self.extract_issues(validations),
            'recommendations': await self.generate_recommendations(validations)
        }
```

### 2. Quality Metrics Aggregation
```python
class QualityMetricsAggregator:
    """Aggregate quality metrics across all checks"""
    
    async def aggregate_metrics(self, checks: dict) -> dict:
        """Comprehensive quality score calculation"""
        
        # Weight configuration
        weights = {
            'knowledge_compliance': 0.25,
            'security': 0.25,
            'test_coverage': 0.20,
            'performance': 0.15,
            'consistency': 0.15
        }
        
        # Calculate weighted score
        scores = {
            'knowledge_compliance': checks['knowledge']['compliance_score'],
            'security': 100 - checks['security']['risk_score'],
            'test_coverage': checks['tests']['coverage_estimate'],
            'performance': checks['performance']['performance_score'],
            'consistency': checks['cross_agent']['consistency_score']
        }
        
        overall_score = sum(
            scores[metric] * weight 
            for metric, weight in weights.items()
        )
        
        return {
            'overall_score': overall_score,
            'breakdown': scores,
            'grade': self.calculate_grade(overall_score),
            'passed': overall_score >= 85,
            'improvements': await self.suggest_improvements(scores)
        }
```

## QA Workflows

### 1. Automated QA Pipeline
```python
class AutomatedQAPipeline:
    """Full automated QA workflow"""
    
    async def run_qa_pipeline(self, code_changes: dict) -> dict:
        """Execute comprehensive QA checks"""
        
        # 1. Knowledge validation
        knowledge_results = await KnowledgeValidator().validate_compliance(
            code_changes['code'],
            code_changes['file_path']
        )
        
        # 2. Security scanning
        security_results = await SecurityScanner().scan_security(
            code_changes['code']
        )
        
        # 3. Test generation
        test_results = await TestGenerator().generate_tests(
            code_changes['code'],
            code_changes['context']
        )
        
        # 4. Performance analysis
        perf_results = await PerformanceAnalyzer().analyze_performance(
            code_changes['code'],
            code_changes.get('original')
        )
        
        # 5. Cross-agent validation
        if 'agent_results' in code_changes:
            cross_validation = await CrossAgentValidator().validate_agent_results(
                code_changes['agent_results']
            )
        else:
            cross_validation = None
            
        # 6. Aggregate results
        final_metrics = await QualityMetricsAggregator().aggregate_metrics({
            'knowledge': knowledge_results,
            'security': security_results,
            'tests': test_results,
            'performance': perf_results,
            'cross_agent': cross_validation or {'consistency_score': 100}
        })
        
        return {
            'passed': final_metrics['passed'],
            'score': final_metrics['overall_score'],
            'details': {
                'knowledge': knowledge_results,
                'security': security_results,
                'tests': test_results,
                'performance': perf_results,
                'cross_agent': cross_validation
            },
            'required_fixes': self.extract_required_fixes(final_metrics),
            'optional_improvements': self.extract_improvements(final_metrics)
        }
```

### 2. Interactive QA Session
```python
class InteractiveQASession:
    """Interactive QA with user feedback"""
    
    async def start_qa_session(self, changes: dict) -> dict:
        """Interactive quality review session"""
        
        session = {
            'id': self.generate_session_id(),
            'changes': changes,
            'checks_completed': [],
            'user_decisions': []
        }
        
        # Present findings progressively
        steps = [
            ('knowledge', "Checking knowledge file compliance..."),
            ('security', "Scanning for security issues..."),
            ('tests', "Generating test suite..."),
            ('performance', "Analyzing performance impact...")
        ]
        
        for check_type, message in steps:
            # Run check
            result = await self.run_check(check_type, changes)
            session['checks_completed'].append(result)
            
            # If issues found, get user decision
            if result['issues']:
                decision = await self.get_user_decision(result)
                session['user_decisions'].append(decision)
                
                if decision['action'] == 'fix_now':
                    fixes = await self.apply_fixes(result['fixes'])
                    changes['code'] = fixes['updated_code']
                    
        return session
```

## Integration with Existing Quality Hooks

### Enhanced Quality Hook
```python
class EnhancedQualityHook(QualityHook):
    """Integrate QA agent with existing quality hook"""
    
    def __init__(self):
        super().__init__()
        self.qa_agent = QAAgent()
        
    async def post_tool_use(self, tool: str, result: dict):
        """Run QA checks after code modifications"""
        
        if tool in ['Edit', 'Write', 'MultiEdit']:
            # Get agent context if available
            agent_context = self.get_agent_context()
            
            # Run QA pipeline
            qa_results = await self.qa_agent.run_qa_pipeline({
                'code': result.get('content', ''),
                'file_path': result.get('file_path'),
                'context': agent_context,
                'agent_results': self.get_agent_results()
            })
            
            # Block if critical issues
            if not qa_results['passed']:
                raise QualityCheckFailed(
                    f"Quality check failed: {qa_results['score']}/100",
                    qa_results['required_fixes']
                )
                
            # Store QA results in memory
            await self.capture_qa_results(qa_results)
```

## Success Metrics
- Quality score average: >90%
- Critical issue detection: 100%
- False positive rate: <2%
- Test coverage generation: >80%
- Security vulnerability detection: >95%

## Implementation Priority
1. Knowledge file validation (Critical)
2. Security scanning (Critical)
3. Test generation (High)
4. Performance analysis (Medium)
5. Cross-agent validation (Medium)