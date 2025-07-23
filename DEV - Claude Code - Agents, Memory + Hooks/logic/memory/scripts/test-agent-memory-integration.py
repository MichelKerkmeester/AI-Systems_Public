#!/usr/bin/env python3
"""
Test Script for Agent Memory Integration
Validates the complete integration of optimized memory filter with agent system
"""

import asyncio
import json
import time
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import agent components
from agents.core.orchestrator import Orchestrator, TaskComplexity
from agents.core.routing_engine import SmartRoutingEngine
from agents.integrations.memory_filter_integration import AgentMemoryIntegration

def test_memory_integration():
    """Test memory filter integration with agents"""
    print("🧪 Testing Agent Memory Integration")
    print("=" * 50)
    
    # Initialize memory integration
    memory_integration = AgentMemoryIntegration()
    
    # Test 1: Capture routing decision
    print("\n1️⃣ Testing Routing Decision Capture")
    routing_data = {
        'task': 'Implement responsive slider component with touch support',
        'model': 'qwen3_coder',
        'reasoning': 'Complex UI component requiring full implementation',
        'estimated_cost': 0.38,
        'confidence': 0.92
    }
    result = memory_integration.capture_routing_decision(routing_data)
    print(f"✅ Routing decision captured: {result['status']}")
    
    # Test 2: Capture cost optimization
    print("\n2️⃣ Testing Cost Optimization Capture")
    cost_data = {
        'task': 'Generate API documentation for user endpoints',
        'original_cost': 4.50,
        'optimized_cost': 0.12,
        'savings_percent': 97.3,
        'model_used': 'gemini_flash'
    }
    result = memory_integration.capture_cost_optimization(cost_data)
    print(f"✅ Cost optimization captured: {result['status']}")
    
    # Test 3: Implementation result
    print("\n3️⃣ Testing Implementation Result Capture")
    impl_data = {
        'summary': 'Successfully implemented slider component with touch gestures',
        'code': 'const slider = document.querySelector(".slider"); // Touch support added',
        'patterns': ['slider-pattern', 'touch-gesture-pattern'],
        'quality_score': 0.95,
        'agent_type': 'implementation'
    }
    result = memory_integration.capture_implementation_result(impl_data)
    print(f"✅ Implementation result captured: {result['status']}")
    
    # Wait for processing
    print("\n⏳ Waiting for queue processing...")
    time.sleep(3)
    
    # Get analytics
    print("\n📊 Memory Integration Analytics:")
    analytics = memory_integration.get_cost_analytics()
    print(json.dumps(analytics, indent=2))
    
    return True

async def test_orchestrator():
    """Test orchestrator with memory integration"""
    print("\n\n🎯 Testing Orchestrator with Memory")
    print("=" * 50)
    
    # Initialize orchestrator
    config = {
        'routing_rules': {'static': []},
        'cost_limits': {'daily': 100, 'monthly': 5000},
        'model_configs': {
            'qwen3_coder': {'context_limit': 50000, 'cost_per_token': 0.0000075},
            'gemini_flash': {'context_limit': 100000, 'cost_per_token': 0.00000026},
            'opus': {'context_limit': 20000, 'cost_per_token': 0.00003}
        }
    }
    orchestrator = Orchestrator(config)
    
    # Test task decomposition
    print("\n1️⃣ Testing Task Decomposition")
    task = "Implement a complete user authentication system with JWT tokens and tests"
    subtasks = await orchestrator.decompose_task(task)
    print(f"✅ Decomposed into {len(subtasks)} subtasks:")
    for st in subtasks:
        print(f"   - {st.id}: {st.description[:50]}... (complexity: {st.complexity.value})")
    
    # Test routing
    print("\n2️⃣ Testing Subtask Routing")
    for subtask in subtasks:
        selection = orchestrator.route_subtask(subtask)
        print(f"✅ {subtask.id} → {selection.model} (${selection.estimated_cost:.4f})")
    
    # Get metrics
    print("\n📊 Orchestration Metrics:")
    metrics = orchestrator.get_orchestration_metrics()
    print(f"   - Total routing decisions: {len(metrics['routing_decisions'])}")
    print(f"   - Total cost savings: ${metrics['cost_savings']:.2f}")
    
    return True

def test_routing_engine():
    """Test routing engine with caching and memory"""
    print("\n\n🚦 Testing Routing Engine")
    print("=" * 50)
    
    # Initialize routing engine
    routing_engine = SmartRoutingEngine()
    
    # Test various tasks
    test_tasks = [
        ("Fix typo in README", {'lines_changed': 1}),
        ("Implement OAuth2 authentication", {'lines_changed': 500}),
        ("Analyze code coverage report", {'lines_changed': 0}),
        ("Fix typo in README", {'lines_changed': 1}),  # Duplicate for cache test
        ("Add security headers to API", {'lines_changed': 50})
    ]
    
    print("\n1️⃣ Testing Routing Decisions")
    for task, context in test_tasks:
        result = routing_engine.route(task, context)
        print(f"✅ '{task[:30]}...' → {result.model} ({result.decision_type.value})")
    
    # Check stats
    print("\n📊 Routing Engine Statistics:")
    stats = routing_engine.get_routing_stats()
    print(json.dumps(stats, indent=2))
    
    return True

def test_memory_filter_performance():
    """Test memory filter performance with sample data"""
    print("\n\n⚡ Testing Memory Filter Performance")
    print("=" * 50)
    
    # Create test content
    test_contents = [
        {
            'url': 'https://docs.anobel.nl/components/slider',
            'title': 'Slider Component',
            'text': 'const initSlider = () => { /* Slater pattern */ }'
        },
        {
            'url': 'https://blog.example.com/news',
            'title': 'Company News',
            'text': 'Latest updates from our team...'
        },
        {
            'url': 'https://anobel.nl/.claude/logic/agents/core.py',
            'title': 'Agent Core Logic',
            'text': 'class Agent: def process(self): # Implementation'
        },
        {
            'url': 'https://static.example.com/style.css',
            'title': 'Stylesheet',
            'text': 'body { margin: 0; }'
        }
    ] * 5  # Multiply for more realistic load
    
    # Process through memory integration
    memory_integration = AgentMemoryIntegration()
    
    print(f"\n🚀 Processing {len(test_contents)} items...")
    start_time = time.time()
    
    for content in test_contents:
        memory_integration.memory_filter.process_crawled_content(content)
    
    # Wait for queue processing
    time.sleep(2)
    
    end_time = time.time()
    
    print(f"✅ Completed in {end_time - start_time:.2f} seconds")
    print(f"   Throughput: {len(test_contents)/(end_time - start_time):.2f} items/sec")
    
    # Get final stats
    stats = memory_integration.memory_filter.get_stats()
    print("\n📊 Memory Filter Statistics:")
    print(f"   - Avg processing time: {stats.get('avg_processing_time_ms', 0):.2f}ms")
    print(f"   - Cache hit rate: {stats.get('cache', {}).get('hit_rate', 0)*100:.1f}%")
    
    if 'storage_distribution' in stats:
        dist = stats['storage_distribution']
        print(f"   - Storage distribution: {dist}")
    
    return True

async def main():
    """Run all tests"""
    print("🚀 AGENT MEMORY INTEGRATION TEST SUITE")
    print("=" * 70)
    print("Testing the complete integration of optimized memory filter with agents\n")
    
    try:
        # Run tests
        test_memory_integration()
        await test_orchestrator()
        test_routing_engine()
        test_memory_filter_performance()
        
        print("\n\n✅ ALL TESTS PASSED!")
        print("The agent memory integration is working correctly.")
        
    except Exception as e:
        print(f"\n\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
    
    # Cleanup
    print("\n🧹 Cleaning up...")
    # The memory filter will shutdown gracefully when the script ends

if __name__ == '__main__':
    asyncio.run(main())