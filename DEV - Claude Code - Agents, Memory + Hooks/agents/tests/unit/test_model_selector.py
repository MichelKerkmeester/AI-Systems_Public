"""
Unit tests for ModelSelector

Tests model routing logic and cost calculations.
"""

import pytest
import sys
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from routing import ModelSelector, TaskComplexityAnalyzer, ComplexityLevel, TaskAnalysis


class TestModelSelector:
    """Test suite for ModelSelector"""
    
    @pytest.fixture
    def selector(self):
        """Create selector instance"""
        return ModelSelector()
    
    @pytest.fixture
    def analyzer(self):
        """Create analyzer for generating task analyses"""
        return TaskComplexityAnalyzer()
    
    def create_task_analysis(self, complexity_level, score, task_type="general"):
        """Helper to create TaskAnalysis objects"""
        return TaskAnalysis(
            complexity_level=complexity_level,
            complexity_score=score,
            task_type=task_type,
            keywords_found=[],
            has_security_implications=False,
            requires_context_understanding=False,
            estimated_tokens=1000,
            potential_breaking_change=False
        )
    
    def test_trivial_task_routing(self, selector):
        """Test routing for trivial tasks"""
        analysis = self.create_task_analysis(ComplexityLevel.TRIVIAL, 1)
        
        selection = selector.select_model(analysis)
        
        assert selection.primary_model == "kimi-pro"
        assert selection.fallback_model == "claude-opus-4"
        assert selection.reasoning == "Simple task suitable for Kimi Pro"
        assert selection.confidence >= 0.9
    
    def test_simple_task_routing(self, selector):
        """Test routing for simple tasks"""
        analysis = self.create_task_analysis(ComplexityLevel.SIMPLE, 5)
        
        selection = selector.select_model(analysis)
        
        assert selection.primary_model == "kimi-pro"
        assert selection.fallback_model == "claude-opus-4"
        assert selection.confidence >= 0.8
    
    def test_medium_task_routing(self, selector):
        """Test routing for medium tasks"""
        analysis = self.create_task_analysis(ComplexityLevel.MEDIUM, 10)
        
        selection = selector.select_model(analysis)
        
        assert selection.primary_model == "claude-opus-4"
        assert selection.reasoning == "Medium complexity requires Claude's capabilities"
    
    def test_complex_task_routing(self, selector):
        """Test routing for complex tasks"""
        analysis = self.create_task_analysis(ComplexityLevel.COMPLEX, 15)
        
        selection = selector.select_model(analysis)
        
        assert selection.primary_model == "claude-opus-4"
        assert selection.confidence >= 0.95
    
    def test_analyst_agent_routing(self, selector):
        """Test routing for analyst agents"""
        # Analyst should use Gemini for analysis tasks
        analysis = self.create_task_analysis(ComplexityLevel.MEDIUM, 10, "analysis")
        
        selection = selector.select_model(analysis, agent_type="analyst")
        
        assert selection.primary_model == "gemini-mcp"
        assert selection.fallback_model == "claude-opus-4"
        assert "Deep analysis" in selection.reasoning
    
    def test_developer_agent_routing(self, selector):
        """Test routing for developer agents"""
        # Simple developer task -> Kimi
        simple_analysis = self.create_task_analysis(ComplexityLevel.SIMPLE, 4, "bug_fix")
        selection = selector.select_model(simple_analysis, agent_type="developer")
        assert selection.primary_model == "kimi-pro"
        
        # Complex developer task -> Claude
        complex_analysis = self.create_task_analysis(ComplexityLevel.COMPLEX, 15, "feature")
        selection = selector.select_model(complex_analysis, agent_type="developer")
        assert selection.primary_model == "claude-opus-4"
    
    def test_reviewer_agent_routing(self, selector):
        """Test routing for reviewer agents"""
        # Security review -> Claude
        security_analysis = TaskAnalysis(
            complexity_level=ComplexityLevel.MEDIUM,
            complexity_score=10,
            task_type="review",
            keywords_found=["security"],
            has_security_implications=True,
            requires_context_understanding=True,
            estimated_tokens=1000,
            potential_breaking_change=False
        )
        
        selection = selector.select_model(security_analysis, agent_type="reviewer")
        assert selection.primary_model == "claude-opus-4"
        assert "security" in selection.reasoning.lower()
    
    def test_synthesis_agent_routing(self, selector):
        """Test routing for synthesis agents"""
        # Synthesis always uses Claude
        analysis = self.create_task_analysis(ComplexityLevel.SIMPLE, 3)
        
        selection = selector.select_model(analysis, agent_type="synthesis")
        
        assert selection.primary_model == "claude-opus-4"
        assert "critical synthesis" in selection.reasoning.lower()
    
    def test_force_model_override(self, selector):
        """Test forced model selection"""
        analysis = self.create_task_analysis(ComplexityLevel.TRIVIAL, 1)
        
        # Force Gemini even for trivial task
        selection = selector.select_model(analysis, force_model="gemini-mcp")
        
        assert selection.primary_model == "gemini-mcp"
        assert "forced" in selection.reasoning.lower()
    
    def test_cost_estimation(self, selector):
        """Test cost estimation accuracy"""
        # Create analysis with specific token count
        analysis = TaskAnalysis(
            complexity_level=ComplexityLevel.SIMPLE,
            complexity_score=4,
            task_type="general",
            keywords_found=[],
            has_security_implications=False,
            requires_context_understanding=False,
            estimated_tokens=2000,  # 2k tokens
            potential_breaking_change=False
        )
        
        # Kimi costs: $0.003/1k input, $0.012/1k output
        selection = selector.select_model(analysis)
        assert selection.primary_model == "kimi-pro"
        
        # Rough estimate: 2k input + 2k output
        expected_cost = (2 * 0.003) + (2 * 0.012)  # $0.03
        assert 0.01 < selection.estimated_cost < 0.05  # Reasonable range
    
    def test_confidence_levels(self, selector):
        """Test confidence scoring"""
        # High confidence for clear cases
        trivial = self.create_task_analysis(ComplexityLevel.TRIVIAL, 1)
        selection = selector.select_model(trivial)
        assert selection.confidence >= 0.9
        
        # Lower confidence for edge cases
        edge = self.create_task_analysis(ComplexityLevel.SIMPLE, 6)  # Near boundary
        selection = selector.select_model(edge)
        assert 0.7 <= selection.confidence <= 0.85
    
    def test_usage_statistics(self, selector):
        """Test usage tracking"""
        # Make several selections
        analyses = [
            self.create_task_analysis(ComplexityLevel.TRIVIAL, 1),
            self.create_task_analysis(ComplexityLevel.SIMPLE, 5),
            self.create_task_analysis(ComplexityLevel.MEDIUM, 10),
        ]
        
        for analysis in analyses:
            selector.select_model(analysis)
        
        # Get usage report
        report = selector.get_usage_report()
        
        assert report["total_selections"] == 3
        assert "kimi-pro" in report["model_usage"]
        assert "claude-opus-4" in report["model_usage"]
        assert report["model_usage"]["kimi-pro"]["count"] == 2
        assert report["model_usage"]["claude-opus-4"]["count"] == 1
    
    def test_cost_savings_calculation(self, selector):
        """Test cost savings calculations"""
        # Analyst using Gemini
        analysis = self.create_task_analysis(ComplexityLevel.MEDIUM, 10, "analysis")
        selection = selector.select_model(analysis, agent_type="analyst")
        
        assert selection.primary_model == "gemini-mcp"
        assert selection.cost_vs_claude > 0  # Should show savings
        
        # Calculate expected savings (Gemini is ~75% cheaper)
        claude_cost = selection.estimated_cost / 0.25  # If Gemini is 25% of Claude
        expected_savings = claude_cost - selection.estimated_cost
        
        assert abs(selection.cost_vs_claude - expected_savings) < 0.01


if __name__ == "__main__":
    pytest.main([__file__, "-v"])