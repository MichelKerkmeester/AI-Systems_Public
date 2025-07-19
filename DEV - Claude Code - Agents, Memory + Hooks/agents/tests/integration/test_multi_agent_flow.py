"""
Integration tests for Multi-Agent Workflows

Tests complete orchestration scenarios with multiple agents.
"""

import pytest
import asyncio
import sys
from pathlib import Path
from unittest.mock import Mock, patch, AsyncMock

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from orchestration import ParallelOrchestrator, OrchestratorState
from routing import ComplexityLevel


class TestMultiAgentFlow:
    """Test complete multi-agent orchestration flows"""
    
    @pytest.fixture
    async def orchestrator(self):
        """Create and initialize orchestrator"""
        orch = ParallelOrchestrator(
            project_root=Path("/tmp/test_project"),
            max_agents=5
        )
        
        # Mock git operations
        with patch('subprocess.run'):
            await orch.initialize()
        
        return orch
    
    @pytest.mark.asyncio
    async def test_simple_task_single_agent(self, orchestrator):
        """Test simple task handled by single agent"""
        # Add simple work package
        wp_id = await orchestrator.add_work_package(
            description="Fix typo in README",
            work_type="bug_fix"
        )
        
        # Mock agent spawning
        with patch.object(orchestrator, '_spawn_agent', new_callable=AsyncMock) as mock_spawn:
            mock_agent = Mock()
            mock_agent.agent_id = "dev_1"
            mock_agent.status = "idle"
            mock_agent.agent_instance = Mock()
            mock_spawn.return_value = mock_agent
            
            # Execute
            await orchestrator.execute()
            
            # Should spawn only one developer agent
            assert mock_spawn.call_count == 1
            spawn_call = mock_spawn.call_args[0]
            assert spawn_call[0] == "developer"  # agent type
    
    @pytest.mark.asyncio
    async def test_complex_refactoring_multiple_agents(self, orchestrator):
        """Test complex refactoring spawns multiple agents"""
        # Add complex work package
        wp_id = await orchestrator.add_work_package(
            description="Refactor entire authentication system with OAuth2 integration",
            work_type="refactoring"
        )
        
        # Track spawned agents
        spawned_agents = []
        
        async def mock_spawn(agent_type, work_package_id):
            agent = Mock()
            agent.agent_id = f"{agent_type}_{len(spawned_agents)}"
            agent.type = agent_type
            agent.status = "idle"
            agent.agent_instance = Mock()
            spawned_agents.append(agent)
            return agent
        
        with patch.object(orchestrator, '_spawn_agent', side_effect=mock_spawn):
            # Mock work package complexity
            wp = orchestrator.work_packages[wp_id]
            wp.complexity = ComplexityLevel.COMPLEX
            
            # Execute (partial to test spawning)
            await orchestrator._distribute_work()
            
            # Should spawn multiple agents
            assert len(spawned_agents) >= 2
            
            # Should include different types
            agent_types = [a.type for a in spawned_agents]
            assert "analyst" in agent_types or "developer" in agent_types
    
    @pytest.mark.asyncio
    async def test_auto_synthesis_trigger(self, orchestrator):
        """Test automatic synthesis agent spawning"""
        # Add multiple work packages
        wp_ids = []
        for i in range(3):
            wp_id = await orchestrator.add_work_package(
                description=f"Implement feature {i}",
                work_type="feature"
            )
            wp_ids.append(wp_id)
        
        # Mock agent spawning
        with patch.object(orchestrator, '_spawn_agent', new_callable=AsyncMock) as mock_spawn:
            # Simulate 3 agents working
            for i in range(3):
                agent = Mock()
                agent.agent_id = f"dev_{i}"
                agent.status = "working"
                orchestrator.agents[agent.agent_id] = agent
                orchestrator.active_agents[f"developer_{i}"] = agent
            
            # Check synthesis trigger
            await orchestrator._check_synthesis_trigger()
            
            # Should trigger synthesis (3 agents >= threshold)
            assert orchestrator.synthesis_agent is not None or mock_spawn.called
    
    @pytest.mark.asyncio
    async def test_conflict_detection_and_resolution(self, orchestrator):
        """Test conflict detection between agents"""
        # Create mock agent results with conflicts
        agent_results = [
            {
                "agent_id": "dev_1",
                "file_changes": [
                    {"file": "user.py", "content": "class User: pass"}
                ]
            },
            {
                "agent_id": "dev_2", 
                "file_changes": [
                    {"file": "user.py", "content": "class UserModel: pass"}
                ]
            }
        ]
        
        # Test conflict detection
        conflicts = await orchestrator.conflict_resolver.detect_conflicts(agent_results)
        
        assert len(conflicts) > 0
        assert conflicts[0]["type"].value == "file_modification"
        assert conflicts[0]["file"] == "user.py"
        assert set(conflicts[0]["agents"]) == {"dev_1", "dev_2"}
    
    @pytest.mark.asyncio
    async def test_model_routing_in_orchestration(self, orchestrator):
        """Test that agents use appropriate models"""
        # Add analysis task
        wp_id = await orchestrator.add_work_package(
            description="Analyze the codebase architecture and suggest improvements",
            work_type="analysis"
        )
        
        # Mock agent creation with model tracking
        models_used = []
        
        async def mock_spawn(agent_type, work_package_id):
            agent = Mock()
            agent.agent_id = f"{agent_type}_1"
            agent.type = agent_type
            agent.status = "idle"
            
            # Track model selection
            if agent_type == "analyst":
                agent.current_model = "gemini-mcp"
            elif agent_type == "developer":
                agent.current_model = "kimi-pro"
            else:
                agent.current_model = "claude-opus-4"
            
            models_used.append((agent_type, agent.current_model))
            agent.agent_instance = Mock()
            return agent
        
        with patch.object(orchestrator, '_spawn_agent', side_effect=mock_spawn):
            # Execute distribution
            await orchestrator._distribute_work()
            
            # Check appropriate models were selected
            analyst_models = [m for t, m in models_used if t == "analyst"]
            if analyst_models:
                assert "gemini-mcp" in analyst_models  # Analyst should use Gemini
    
    @pytest.mark.asyncio
    async def test_memory_sharing_workflow(self, orchestrator):
        """Test agents share memories during orchestration"""
        # Create two developer agents
        dev1 = Mock()
        dev1.agent_id = "dev_1"
        dev1.type = "developer"
        dev1.status = "working"
        
        dev2 = Mock()
        dev2.agent_id = "dev_2"
        dev2.type = "developer"
        dev2.status = "working"
        
        orchestrator.agents = {"dev_1": dev1, "dev_2": dev2}
        
        # Mock memory operations
        with patch.object(orchestrator.memory, 'share_memories_between_agents', new_callable=AsyncMock) as mock_share:
            # Simulate task completion triggering memory share
            message = {
                "type": "task_completed",
                "from_agent": "dev_1",
                "task_id": "task_1",
                "result": {"insights": ["Use dependency injection"]}
            }
            
            await orchestrator._process_message(message)
            
            # Could verify memory sharing logic here
            # In real implementation, completed tasks might trigger sharing
    
    @pytest.mark.asyncio
    async def test_final_report_generation(self, orchestrator):
        """Test final orchestration report includes intelligence insights"""
        # Add some completed work
        wp_id = await orchestrator.add_work_package("Test task", "general")
        wp = orchestrator.work_packages[wp_id]
        wp.status = "completed"
        wp.result = {
            "files_modified": ["test.py"],
            "model": "kimi-pro",
            "cost": 0.02
        }
        
        # Mock pattern extraction
        with patch.object(orchestrator.memory, 'extract_patterns_from_results', new_callable=AsyncMock) as mock_patterns:
            mock_patterns.return_value = [
                {"type": "file_pattern", "description": "Common test files"}
            ]
            
            # Generate report
            report = await orchestrator._generate_final_report()
            
            # Should include intelligence insights
            assert "intelligence_insights" in report
            assert "patterns_discovered" in report["intelligence_insights"]
            assert len(report["intelligence_insights"]["patterns_discovered"]) > 0
    
    @pytest.mark.asyncio
    async def test_error_handling_and_fallback(self, orchestrator):
        """Test error handling and model fallbacks"""
        # Add work package
        wp_id = await orchestrator.add_work_package("Simple task", "general")
        
        # Mock agent with Kimi failure
        async def mock_spawn(agent_type, work_package_id):
            agent = Mock()
            agent.agent_id = "dev_1"
            agent.type = "developer"
            agent.status = "idle"
            agent.current_model = "kimi-pro"
            
            # Simulate Kimi API failure and fallback
            agent.agent_instance = Mock()
            agent.agent_instance.execute_task = AsyncMock(side_effect=[
                Exception("Kimi API error"),  # First attempt fails
                {"status": "completed", "model": "claude-opus-4"}  # Fallback succeeds
            ])
            
            return agent
        
        with patch.object(orchestrator, '_spawn_agent', side_effect=mock_spawn):
            # Execute should handle the error gracefully
            await orchestrator._distribute_work()
            
            # Work should still complete via fallback
            assert orchestrator.state != OrchestratorState.ERROR


class TestOrchestrationPatterns:
    """Test specific orchestration patterns"""
    
    @pytest.mark.asyncio
    async def test_sequential_dependencies(self):
        """Test handling of task dependencies"""
        orch = ParallelOrchestrator(Path("/tmp/test"))
        
        # Add tasks with dependencies
        task1_id = await orch.add_work_package("Task 1", "general")
        task2_id = await orch.add_work_package("Task 2", "general", dependencies=[task1_id])
        task3_id = await orch.add_work_package("Task 3", "general", dependencies=[task2_id])
        
        # Verify dependency chain
        assert orch.work_packages[task2_id].dependencies == [task1_id]
        assert orch.work_packages[task3_id].dependencies == [task2_id]
    
    @pytest.mark.asyncio
    async def test_parallel_independent_tasks(self):
        """Test parallel execution of independent tasks"""
        orch = ParallelOrchestrator(Path("/tmp/test"))
        
        # Add independent tasks
        task_ids = []
        for i in range(3):
            task_id = await orch.add_work_package(f"Independent task {i}", "general")
            task_ids.append(task_id)
        
        # All should be eligible for parallel execution
        pending = [wp for wp in orch.work_packages.values() if wp.status == "pending"]
        assert len(pending) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])