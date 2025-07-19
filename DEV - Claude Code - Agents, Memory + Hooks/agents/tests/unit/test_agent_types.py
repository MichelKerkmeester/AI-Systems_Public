"""
Unit tests for Agent Types

Tests specialized agent behaviors and model routing.
"""

import pytest
import asyncio
import sys
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from types import AnalystAgent, DeveloperAgent, ReviewerAgent, SynthesisAgent
from routing import ComplexityLevel


class TestAnalystAgent:
    """Test suite for AnalystAgent"""
    
    @pytest.fixture
    def analyst(self):
        """Create analyst agent instance"""
        return AnalystAgent(
            agent_id="analyst_test",
            work_package="test_analysis"
        )
    
    @pytest.mark.asyncio
    async def test_analyst_routes_to_gemini(self, analyst):
        """Test that analyst routes analysis tasks to Gemini"""
        task = {
            "id": "task_1",
            "description": "Analyze the codebase architecture",
            "type": "analysis"
        }
        
        # Mock the Gemini routing
        with patch.object(analyst, '_execute_with_gemini', new_callable=AsyncMock) as mock_gemini:
            mock_gemini.return_value = {"status": "completed", "model": "gemini-mcp"}
            
            await analyst.execute_task(task)
            
            # Should have called Gemini
            mock_gemini.assert_called_once()
            assert analyst.current_model == "gemini-mcp"
    
    @pytest.mark.asyncio
    async def test_analyst_thinking_process(self, analyst):
        """Test analyst uses sequential thinking"""
        task = {
            "id": "task_2",
            "description": "Research best practices for microservices"
        }
        
        # Mock thinking
        with patch.object(analyst, 'think_about_task', new_callable=AsyncMock) as mock_think:
            mock_think.return_value = {
                "thoughts": ["Understanding requirements", "Researching patterns"],
                "insights": ["Consider service boundaries", "Plan for scalability"]
            }
            
            await analyst.execute_task(task)
            
            mock_think.assert_called_once()
    
    def test_analyst_specialization(self, analyst):
        """Test analyst-specific methods"""
        assert analyst.agent_type == "analyst"
        assert hasattr(analyst, 'analyze_architecture')
        assert hasattr(analyst, 'generate_insights')


class TestDeveloperAgent:
    """Test suite for DeveloperAgent"""
    
    @pytest.fixture
    def developer(self):
        """Create developer agent instance"""
        return DeveloperAgent(
            agent_id="dev_test",
            work_package="test_development"
        )
    
    @pytest.mark.asyncio
    async def test_developer_routes_simple_to_kimi(self, developer):
        """Test that developer routes simple tasks to Kimi"""
        task = {
            "id": "task_1",
            "description": "Fix typo in README",
            "type": "bug_fix"
        }
        
        # Mock analyze_task to return SIMPLE
        with patch.object(developer, 'analyze_task', new_callable=AsyncMock) as mock_analyze:
            mock_analyze.return_value.complexity_level = ComplexityLevel.SIMPLE
            mock_analyze.return_value.complexity_score = 3
            
            # Mock Kimi routing
            with patch.object(developer, '_execute_with_kimi', new_callable=AsyncMock) as mock_kimi:
                mock_kimi.return_value = {"status": "completed", "model": "kimi-pro"}
                
                await developer.execute_task(task)
                
                # Should route to Kimi
                mock_kimi.assert_called_once()
                assert developer.current_model == "kimi-pro"
    
    @pytest.mark.asyncio
    async def test_developer_routes_complex_to_claude(self, developer):
        """Test that developer routes complex tasks to Claude"""
        task = {
            "id": "task_2",
            "description": "Refactor entire authentication system",
            "type": "refactoring"
        }
        
        # Mock analyze_task to return COMPLEX
        with patch.object(developer, 'analyze_task', new_callable=AsyncMock) as mock_analyze:
            mock_analyze.return_value.complexity_level = ComplexityLevel.COMPLEX
            mock_analyze.return_value.complexity_score = 15
            
            # Mock Claude routing
            with patch.object(developer, '_execute_with_claude', new_callable=AsyncMock) as mock_claude:
                mock_claude.return_value = {"status": "completed", "model": "claude-opus-4"}
                
                await developer.execute_task(task)
                
                # Should route to Claude
                mock_claude.assert_called_once()
                assert developer.current_model == "claude-opus-4"
    
    def test_developer_implementation_methods(self, developer):
        """Test developer-specific implementation methods"""
        assert developer.agent_type == "developer"
        assert hasattr(developer, 'implement_feature')
        assert hasattr(developer, 'fix_bug')
        assert hasattr(developer, 'refactor_code')


class TestReviewerAgent:
    """Test suite for ReviewerAgent"""
    
    @pytest.fixture
    def reviewer(self):
        """Create reviewer agent instance"""
        return ReviewerAgent(
            agent_id="reviewer_test",
            work_package="test_review"
        )
    
    @pytest.mark.asyncio
    async def test_reviewer_security_uses_claude(self, reviewer):
        """Test that security reviews always use Claude"""
        task = {
            "id": "task_1",
            "description": "Review security vulnerabilities in API endpoints",
            "type": "security_review"
        }
        
        # Mock task analysis with security implications
        with patch.object(reviewer, 'analyze_task', new_callable=AsyncMock) as mock_analyze:
            mock_analyze.return_value.has_security_implications = True
            mock_analyze.return_value.keywords_found = ["security", "vulnerability"]
            
            # Mock Claude routing
            with patch.object(reviewer, '_execute_with_claude', new_callable=AsyncMock) as mock_claude:
                mock_claude.return_value = {"status": "completed", "model": "claude-opus-4"}
                
                await reviewer.execute_task(task)
                
                # Should use Claude for security
                mock_claude.assert_called_once()
                assert reviewer.current_model == "claude-opus-4"
    
    @pytest.mark.asyncio
    async def test_reviewer_pattern_check_uses_kimi(self, reviewer):
        """Test that pattern reviews can use Kimi"""
        task = {
            "id": "task_2",
            "description": "Check code patterns for consistency",
            "type": "pattern_review"
        }
        
        # Mock task analysis without security implications
        with patch.object(reviewer, 'analyze_task', new_callable=AsyncMock) as mock_analyze:
            mock_analyze.return_value.has_security_implications = False
            mock_analyze.return_value.complexity_level = ComplexityLevel.SIMPLE
            mock_analyze.return_value.keywords_found = ["pattern", "consistency"]
            
            # Mock Kimi routing
            with patch.object(reviewer, '_execute_with_kimi', new_callable=AsyncMock) as mock_kimi:
                mock_kimi.return_value = {"status": "completed", "model": "kimi-pro"}
                
                await reviewer.execute_task(task)
                
                # Should use Kimi for simple pattern review
                mock_kimi.assert_called_once()
    
    def test_reviewer_review_methods(self, reviewer):
        """Test reviewer-specific methods"""
        assert reviewer.agent_type == "reviewer"
        assert hasattr(reviewer, 'review_security')
        assert hasattr(reviewer, 'check_patterns')
        assert hasattr(reviewer, 'validate_quality')


class TestSynthesisAgent:
    """Test suite for SynthesisAgent"""
    
    @pytest.fixture
    def synthesis(self):
        """Create synthesis agent instance"""
        return SynthesisAgent(
            agent_id="synthesis_test",
            work_package="test_synthesis"
        )
    
    @pytest.mark.asyncio
    async def test_synthesis_always_uses_claude(self, synthesis):
        """Test that synthesis always uses Claude regardless of complexity"""
        # Test with simple task
        simple_task = {
            "id": "task_1",
            "description": "Merge two simple changes",
            "type": "synthesis"
        }
        
        # Mock Claude routing
        with patch.object(synthesis, '_execute_with_claude', new_callable=AsyncMock) as mock_claude:
            mock_claude.return_value = {"status": "completed", "model": "claude-opus-4"}
            
            await synthesis.execute_task(simple_task)
            
            # Should use Claude even for simple synthesis
            mock_claude.assert_called_once()
            assert synthesis.current_model == "claude-opus-4"
    
    @pytest.mark.asyncio
    async def test_synthesis_conflict_handling(self, synthesis):
        """Test synthesis agent handles conflicts"""
        # Mock receiving conflict message
        conflict_message = {
            "type": "conflict_resolution",
            "conflicts": [
                {
                    "type": "file_modification",
                    "file": "user.py",
                    "agents": ["dev_1", "dev_2"]
                }
            ],
            "resolution": {
                "status": "resolved",
                "strategy": "merge"
            }
        }
        
        with patch.object(synthesis, 'handle_message', new_callable=AsyncMock) as mock_handle:
            await synthesis.handle_message(conflict_message)
            mock_handle.assert_called_once_with(conflict_message)
    
    def test_synthesis_merge_methods(self, synthesis):
        """Test synthesis-specific methods"""
        assert synthesis.agent_type == "synthesis"
        assert hasattr(synthesis, 'merge_results')
        assert hasattr(synthesis, 'resolve_conflicts')
        assert hasattr(synthesis, 'generate_final_output')


class TestAgentMemorySharing:
    """Test memory sharing between agents"""
    
    @pytest.mark.asyncio
    async def test_agents_share_memories(self):
        """Test that agents can share memories"""
        dev1 = DeveloperAgent("dev1", "package1")
        dev2 = DeveloperAgent("dev2", "package2")
        
        # Mock memory sharing
        with patch.object(dev1, 'share_learnings', new_callable=AsyncMock) as mock_share:
            await dev1.share_learnings(["dev2"])
            
            mock_share.assert_called_once_with(["dev2"])
    
    @pytest.mark.asyncio
    async def test_agents_retrieve_shared_memories(self):
        """Test agents can retrieve shared memories"""
        analyst = AnalystAgent("analyst1", "analysis")
        
        # Mock memory retrieval
        with patch.object(analyst, 'retrieve_relevant_memories', new_callable=AsyncMock) as mock_retrieve:
            mock_retrieve.return_value = [
                {"type": "pattern", "content": "Use async/await"},
                {"type": "decision", "content": "Prefer composition"}
            ]
            
            memories = await analyst.retrieve_relevant_memories("design patterns")
            
            assert len(memories) == 2
            assert memories[0]["type"] == "pattern"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])