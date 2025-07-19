"""
Unit tests for TaskComplexityAnalyzer

Tests the accuracy of task complexity scoring and categorization.
"""

import pytest
import json
import sys
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from routing import TaskComplexityAnalyzer, ComplexityLevel


class TestTaskComplexityAnalyzer:
    """Test suite for TaskComplexityAnalyzer"""
    
    @pytest.fixture
    def analyzer(self):
        """Create analyzer instance"""
        return TaskComplexityAnalyzer()
    
    @pytest.fixture
    def sample_tasks(self):
        """Load sample tasks from fixtures"""
        fixture_path = Path(__file__).parent.parent / "fixtures" / "sample_tasks.json"
        with open(fixture_path, 'r') as f:
            return json.load(f)
    
    def test_trivial_task_scoring(self, analyzer, sample_tasks):
        """Test scoring of trivial tasks"""
        for task in sample_tasks["trivial_tasks"]:
            result = analyzer.analyze_task(task["description"])
            
            assert result.complexity_level == ComplexityLevel.TRIVIAL
            assert result.complexity_score <= 2
            assert task["expected_complexity"] == result.complexity_level.name
    
    def test_simple_task_scoring(self, analyzer, sample_tasks):
        """Test scoring of simple tasks"""
        for task in sample_tasks["simple_tasks"]:
            result = analyzer.analyze_task(task["description"])
            
            assert result.complexity_level == ComplexityLevel.SIMPLE
            assert 3 <= result.complexity_score <= 6
            assert task["expected_complexity"] == result.complexity_level.name
    
    def test_medium_task_scoring(self, analyzer, sample_tasks):
        """Test scoring of medium tasks"""
        for task in sample_tasks["medium_tasks"]:
            result = analyzer.analyze_task(task["description"])
            
            assert result.complexity_level == ComplexityLevel.MEDIUM
            assert 7 <= result.complexity_score <= 12
            assert task["expected_complexity"] == result.complexity_level.name
    
    def test_complex_task_scoring(self, analyzer, sample_tasks):
        """Test scoring of complex tasks"""
        for task in sample_tasks["complex_tasks"]:
            result = analyzer.analyze_task(task["description"])
            
            assert result.complexity_level == ComplexityLevel.COMPLEX
            assert 13 <= result.complexity_score <= 17
            assert task["expected_complexity"] == result.complexity_level.name
    
    def test_critical_task_scoring(self, analyzer, sample_tasks):
        """Test scoring of critical tasks"""
        for task in sample_tasks["critical_tasks"]:
            result = analyzer.analyze_task(task["description"])
            
            assert result.complexity_level == ComplexityLevel.CRITICAL
            assert result.complexity_score >= 18
            assert task["expected_complexity"] == result.complexity_level.name
    
    def test_edge_cases(self, analyzer, sample_tasks):
        """Test edge cases and unusual inputs"""
        for task in sample_tasks["edge_cases"]:
            # Should not crash on any input
            result = analyzer.analyze_task(task["description"])
            
            assert result is not None
            assert result.complexity_score >= 0
            assert result.complexity_score <= 20
            assert result.complexity_level in ComplexityLevel
    
    def test_context_influence(self, analyzer):
        """Test how context affects complexity scoring"""
        base_task = "Update user profile"
        
        # Without context
        result_no_context = analyzer.analyze_task(base_task)
        
        # With file context
        result_with_files = analyzer.analyze_task(
            base_task,
            context={"files": ["user.py", "profile.py", "database.py"]}
        )
        
        # With constraints
        result_with_constraints = analyzer.analyze_task(
            base_task,
            context={"constraints": ["maintain backward compatibility", "zero downtime"]}
        )
        
        # Context should increase complexity
        assert result_with_files.complexity_score >= result_no_context.complexity_score
        assert result_with_constraints.complexity_score > result_no_context.complexity_score
    
    def test_keyword_detection(self, analyzer):
        """Test specific keyword detection"""
        # Refactor keywords
        result = analyzer.analyze_task("refactor the authentication module")
        assert "refactor" in result.keywords_found
        assert result.complexity_score >= 7  # Refactoring is at least medium
        
        # Security keywords
        result = analyzer.analyze_task("fix security vulnerability in login")
        assert "security" in result.keywords_found
        assert "vulnerability" in result.keywords_found
        assert result.has_security_implications
        
        # Performance keywords
        result = analyzer.analyze_task("optimize database query performance")
        assert "optimize" in result.keywords_found
        assert "performance" in result.keywords_found
    
    def test_task_type_detection(self, analyzer):
        """Test task type identification"""
        # Bug fix
        result = analyzer.analyze_task("fix bug in payment processing")
        assert result.task_type == "bug_fix"
        
        # Feature
        result = analyzer.analyze_task("implement new dashboard feature")
        assert result.task_type == "feature"
        
        # Refactoring
        result = analyzer.analyze_task("refactor user service")
        assert result.task_type == "refactoring"
        
        # Analysis
        result = analyzer.analyze_task("analyze system performance")
        assert result.task_type == "analysis"
    
    def test_breaking_change_detection(self, analyzer):
        """Test detection of breaking changes"""
        # Breaking change indicators
        breaking_tasks = [
            "migrate database schema",
            "change API response format",
            "update authentication flow"
        ]
        
        for task in breaking_tasks:
            result = analyzer.analyze_task(task)
            assert result.potential_breaking_change
            assert result.complexity_score >= 10  # Breaking changes are at least medium
    
    def test_consistency(self, analyzer):
        """Test analyzer consistency"""
        task = "implement user authentication with OAuth2"
        
        # Run multiple times
        results = [analyzer.analyze_task(task) for _ in range(5)]
        
        # All results should be identical
        first_result = results[0]
        for result in results[1:]:
            assert result.complexity_score == first_result.complexity_score
            assert result.complexity_level == first_result.complexity_level
            assert result.task_type == first_result.task_type


if __name__ == "__main__":
    pytest.main([__file__, "-v"])