#!/usr/bin/env python3
"""
Test Suite for Multi-Agent System

Tests distributed locking, agent lifecycle, message passing,
resource monitoring, and conflict resolution.
"""

import os
import sys
import json
import time
import asyncio
import unittest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from logic.shared import (
    DistributedLock, DistributedLockManager,
    AgentRegistry, AgentInfo, AgentLifecycle,
    Message, MessageQueue,
    ResourceMonitor, ResourceLimits,
    ConflictResolver, Conflict, ConflictType, ConflictResolution
)


class TestDistributedLocking(unittest.TestCase):
    """Test distributed locking mechanism"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.lock_dir = os.path.join(self.temp_dir, "locks")
        os.makedirs(self.lock_dir)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_basic_lock_acquisition(self):
        """Test basic lock acquisition and release"""
        lock = DistributedLock("test-resource", "agent-1", self.lock_dir)
        
        # Acquire lock
        self.assertTrue(lock.acquire(timeout=1))
        
        # Try to acquire again (should fail)
        lock2 = DistributedLock("test-resource", "agent-2", self.lock_dir)
        self.assertFalse(lock2.acquire(timeout=0.1, blocking=False))
        
        # Release and try again
        lock.release()
        self.assertTrue(lock2.acquire(timeout=1))
        lock2.release()
    
    def test_lock_timeout(self):
        """Test lock timeout mechanism"""
        # Create lock with short timeout
        lock = DistributedLock("test-resource", "agent-1", self.lock_dir)
        lock.lock_timeout = 0.5  # 500ms
        
        self.assertTrue(lock.acquire())
        
        # Wait for lock to become stale
        time.sleep(0.6)
        
        # Another agent should be able to acquire
        lock2 = DistributedLock("test-resource", "agent-2", self.lock_dir)
        self.assertTrue(lock2.acquire())
        lock2.release()
    
    def test_context_manager(self):
        """Test lock as context manager"""
        lock = DistributedLock("test-resource", "agent-1", self.lock_dir)
        
        with lock:
            # Lock should be held
            lock2 = DistributedLock("test-resource", "agent-2", self.lock_dir)
            self.assertFalse(lock2.acquire(timeout=0.1, blocking=False))
        
        # Lock should be released
        self.assertTrue(lock2.acquire())
        lock2.release()
    
    def test_distributed_lock_manager(self):
        """Test distributed lock manager"""
        manager = DistributedLockManager("agent-1")
        manager.locks_dir = self.lock_dir
        
        # Acquire multiple locks
        lock1 = manager.acquire_lock("resource-1")
        lock2 = manager.acquire_lock("resource-2")
        
        self.assertIsNotNone(lock1)
        self.assertIsNotNone(lock2)
        
        # List active locks
        active = manager.list_active_locks()
        self.assertEqual(len(active), 2)
        
        # Cleanup
        manager.cleanup_all_locks()
        active = manager.list_active_locks()
        self.assertEqual(len(active), 0)


class TestAgentRegistry(unittest.TestCase):
    """Test agent registry and lifecycle"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.registry = AgentRegistry(self.temp_dir)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_agent_registration(self):
        """Test agent registration and deregistration"""
        agent_id = "test-agent-1"
        metadata = {"work_package": "wp1", "agent_type": "development"}
        
        # Register agent
        self.assertTrue(self.registry.register_agent(agent_id, metadata))
        
        # Get agent info
        agent = self.registry.get_agent(agent_id)
        self.assertIsNotNone(agent)
        self.assertEqual(agent.agent_id, agent_id)
        self.assertEqual(agent.work_package, "wp1")
        
        # List active agents
        agents = self.registry.list_active_agents()
        self.assertEqual(len(agents), 1)
        
        # Deregister
        self.registry.deregister_agent(agent_id)
        self.assertIsNone(self.registry.get_agent(agent_id))
    
    def test_heartbeat_mechanism(self):
        """Test agent heartbeat"""
        agent_id = "test-agent-1"
        self.registry.register_agent(agent_id)
        
        # Initial heartbeat
        agent = self.registry.get_agent(agent_id)
        first_heartbeat = agent.last_heartbeat
        
        # Wait and update heartbeat
        time.sleep(0.1)
        self.assertTrue(self.registry.heartbeat(agent_id))
        
        # Check updated
        agent = self.registry.get_agent(agent_id)
        self.assertGreater(agent.last_heartbeat, first_heartbeat)
    
    def test_stale_agent_cleanup(self):
        """Test cleanup of stale agents"""
        # Set very short timeout
        self.registry.heartbeat_timeout = 0.1
        
        # Register agent
        agent_id = "stale-agent"
        self.registry.register_agent(agent_id)
        
        # Wait for timeout
        time.sleep(0.2)
        
        # Cleanup stale agents
        stale = self.registry.cleanup_stale_agents()
        self.assertIn(agent_id, stale)
        
        # Agent should be gone
        self.assertIsNone(self.registry.get_agent(agent_id))
    
    def test_agent_lifecycle(self):
        """Test complete agent lifecycle"""
        lifecycle = AgentLifecycle(metadata={"test": True})
        lifecycle.registry = self.registry
        
        # Startup
        self.assertTrue(lifecycle.startup())
        self.assertTrue(os.path.exists(lifecycle.workspace))
        
        # Check registered
        agent = self.registry.get_agent(lifecycle.agent_id)
        self.assertIsNotNone(agent)
        
        # Shutdown
        lifecycle.shutdown("test complete")
        
        # Check deregistered
        self.assertIsNone(self.registry.get_agent(lifecycle.agent_id))


class TestMessageQueue(unittest.TestCase):
    """Test inter-agent message passing"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.agent1 = "agent-1"
        self.agent2 = "agent-2"
        self.queue1 = MessageQueue(self.agent1, self.temp_dir)
        self.queue2 = MessageQueue(self.agent2, self.temp_dir)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_direct_messaging(self):
        """Test direct agent-to-agent messaging"""
        received = []
        
        def handler(msg):
            received.append(msg)
        
        # Subscribe to messages
        self.queue2.subscribe("test_message", handler)
        self.queue2.start()
        
        # Send message
        msg = Message(
            from_agent=self.agent1,
            to_agent=self.agent2,
            message_type="test_message",
            payload={"content": "Hello Agent 2"}
        )
        self.assertTrue(self.queue1.publish(msg))
        
        # Wait for processing
        time.sleep(0.5)
        
        # Check received
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0].payload["content"], "Hello Agent 2")
        
        self.queue2.stop()
    
    def test_broadcast_messaging(self):
        """Test broadcast messaging"""
        received1 = []
        received2 = []
        
        # Both agents subscribe
        self.queue1.subscribe("broadcast_test", lambda m: received1.append(m))
        self.queue2.subscribe("broadcast_test", lambda m: received2.append(m))
        
        self.queue1.start()
        self.queue2.start()
        
        # Send broadcast
        msg = Message(
            from_agent="orchestrator",
            to_agent="broadcast",
            message_type="broadcast_test",
            payload={"announcement": "System update"}
        )
        
        orchestrator_queue = MessageQueue("orchestrator", self.temp_dir)
        self.assertTrue(orchestrator_queue.publish(msg))
        
        # Wait for processing
        time.sleep(0.5)
        
        # Both should receive
        self.assertEqual(len(received1), 1)
        self.assertEqual(len(received2), 1)
        
        self.queue1.stop()
        self.queue2.stop()
    
    def test_message_priority(self):
        """Test message priority handling"""
        # Create high and low priority messages
        high_priority = Message(
            from_agent=self.agent1,
            to_agent=self.agent2,
            message_type="urgent",
            payload={"content": "High priority"},
            priority=1
        )
        
        low_priority = Message(
            from_agent=self.agent1,
            to_agent=self.agent2,
            message_type="normal",
            payload={"content": "Low priority"},
            priority=5
        )
        
        # Both should publish successfully
        self.assertTrue(self.queue1.publish(high_priority))
        self.assertTrue(self.queue1.publish(low_priority))


class TestResourceMonitor(unittest.TestCase):
    """Test resource monitoring and limits"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.monitor = ResourceMonitor("test-agent", self.temp_dir)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_resource_usage_capture(self):
        """Test capturing resource usage"""
        usage = self.monitor.get_current_usage()
        
        # Should have basic metrics
        self.assertGreaterEqual(usage.memory_mb, 0)
        self.assertGreaterEqual(usage.cpu_percent, 0)
        self.assertGreaterEqual(usage.open_files, 0)
        self.assertGreaterEqual(usage.num_threads, 1)
    
    def test_resource_limits(self):
        """Test resource limit checking"""
        # Set very low limits
        self.monitor.set_limits({
            "memory_mb": 1,  # 1MB (will definitely exceed)
            "cpu_percent": 0.001  # Very low
        })
        
        # Should exceed limits
        self.assertFalse(self.monitor.check_limits())
    
    def test_throttling(self):
        """Test agent throttling"""
        self.assertFalse(self.monitor.is_throttled())
        
        # Throttle for 1 second
        self.monitor.throttle_agent(1)
        self.assertTrue(self.monitor.is_throttled())
        
        # Wait for throttle to expire
        time.sleep(1.1)
        self.assertFalse(self.monitor.is_throttled())
    
    @patch('psutil.Process')
    def test_monitoring_loop(self, mock_process):
        """Test background monitoring loop"""
        # Mock process metrics
        mock_proc = MagicMock()
        mock_proc.memory_info.return_value.rss = 100 * 1024 * 1024  # 100MB
        mock_proc.memory_percent.return_value = 5.0
        mock_proc.cpu_percent.return_value = 10.0
        mock_proc.open_files.return_value = [1, 2, 3]
        mock_proc.num_threads.return_value = 4
        mock_process.return_value = mock_proc
        
        # Start monitoring
        self.monitor.start_monitoring()
        
        # Let it run
        time.sleep(0.1)
        
        # Check stats
        stats = self.monitor.get_usage_stats()
        self.assertGreater(stats["samples"], 0)
        
        # Stop monitoring
        self.monitor.stop_monitoring()


class TestConflictResolver(unittest.TestCase):
    """Test conflict resolution mechanisms"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.resolver = ConflictResolver(self.temp_dir)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_file_edit_conflict_no_overlap(self):
        """Test file edit conflict with no line overlap"""
        conflict = Conflict(
            conflict_type=ConflictType.FILE_EDIT,
            resource="test.py",
            agent1_id="agent-1",
            agent2_id="agent-2",
            details={
                "agent1_lines": [1, 2, 3],
                "agent2_lines": [10, 11, 12]
            }
        )
        
        resolution = self.resolver.resolve_conflict(conflict)
        # No overlap, should merge
        self.assertEqual(resolution, ConflictResolution.MERGE)
    
    def test_file_edit_conflict_with_overlap(self):
        """Test file edit conflict with line overlap"""
        conflict = Conflict(
            conflict_type=ConflictType.FILE_EDIT,
            resource="test.py",
            agent1_id="agent-1",
            agent2_id="agent-2",
            details={
                "agent1_lines": [1, 2, 3],
                "agent2_lines": [2, 3, 4],
                "agent1_version": 5,
                "agent2_version": 5
            }
        )
        
        resolution = self.resolver.resolve_conflict(conflict)
        # Same version with overlap, should queue
        self.assertEqual(resolution, ConflictResolution.QUEUE)
    
    def test_git_conflict(self):
        """Test git operation conflict"""
        conflict = Conflict(
            conflict_type=ConflictType.GIT_OPERATION,
            resource="git",
            agent1_id="agent-1",
            agent2_id="agent-2"
        )
        
        resolution = self.resolver.resolve_conflict(conflict)
        # Git operations must be sequential
        self.assertEqual(resolution, ConflictResolution.QUEUE)
    
    def test_task_assignment_conflict(self):
        """Test task assignment conflict"""
        conflict = Conflict(
            conflict_type=ConflictType.TASK_ASSIGNMENT,
            resource="task-123",
            agent1_id="agent-1",
            agent2_id="agent-2"
        )
        
        resolution = self.resolver.resolve_conflict(conflict)
        # First agent wins
        self.assertEqual(resolution, ConflictResolution.FIRST_WINS)
    
    def test_queued_operations(self):
        """Test operation queueing"""
        # Create conflict that results in queue
        conflict = Conflict(
            conflict_type=ConflictType.GIT_OPERATION,
            resource="git",
            agent1_id="agent-1",
            agent2_id="agent-2",
            details={
                "agent2_command": "git push"
            }
        )
        
        self.resolver.resolve_conflict(conflict)
        
        # Check queued operations
        queued = self.resolver.get_queued_operations("agent-2")
        self.assertEqual(len(queued), 1)
        self.assertEqual(queued[0]["type"], "git_operation")
        
        # Clear queue
        self.resolver.clear_queued_operations("agent-2")
        queued = self.resolver.get_queued_operations("agent-2")
        self.assertEqual(len(queued), 0)


class TestIntegration(unittest.TestCase):
    """Integration tests for multi-agent system"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        os.environ['CLAUDE_AGENT_ID'] = 'test-integration-agent'
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    async def test_concurrent_file_access(self):
        """Test concurrent file access with locking"""
        results = []
        
        async def agent_task(agent_id, value):
            manager = DistributedLockManager(agent_id)
            file_path = os.path.join(self.temp_dir, "shared.json")
            
            async with manager.atomic_file_operation(file_path):
                # Read current value
                data = {"counter": 0}
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                
                # Increment
                data["counter"] += value
                
                # Write back
                with open(file_path, 'w') as f:
                    json.dump(data, f)
                
                results.append(data["counter"])
        
        # Run multiple agents concurrently
        tasks = [
            agent_task(f"agent-{i}", i) 
            for i in range(1, 6)
        ]
        
        await asyncio.gather(*tasks)
        
        # Check final value
        with open(os.path.join(self.temp_dir, "shared.json"), 'r') as f:
            data = json.load(f)
        
        # 1 + 2 + 3 + 4 + 5 = 15
        self.assertEqual(data["counter"], 15)
    
    def test_agent_coordination(self):
        """Test agent coordination through messaging"""
        # Create registry and queues
        registry = AgentRegistry(self.temp_dir)
        
        # Register multiple agents
        for i in range(3):
            registry.register_agent(
                f"worker-{i}",
                {"agent_type": "development", "work_package": f"wp{i}"}
            )
        
        # Check registry stats
        stats = registry.get_registry_stats()
        self.assertEqual(stats["total_active"], 3)
        self.assertEqual(stats["by_type"]["development"], 3)


# Run async tests
class AsyncTestRunner:
    """Helper to run async tests"""
    
    @staticmethod
    def run_async_test(test_func):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(test_func())
        finally:
            loop.close()


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)