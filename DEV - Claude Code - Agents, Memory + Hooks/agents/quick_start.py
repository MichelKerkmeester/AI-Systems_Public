#!/usr/bin/env python3
"""
Multi-Agent System Quick Start

Test the system with simple examples.
"""

import asyncio
import sys
from pathlib import Path

# Add agents to path
sys.path.insert(0, str(Path(__file__).parent))

from routing import TaskComplexityAnalyzer, ModelSelector
from orchestration.orchestrator_command import handle_analyze, handle_orchestrate


async def main():
    """Run quick start examples"""
    print("🤖 Multi-Agent System Quick Start")
    print("=" * 50)
    
    # Example 1: Analyze task complexity
    print("\n1️⃣ Analyzing Task Complexity...")
    task1 = "Fix typo in README"
    result = await handle_analyze(task1)
    print(f"Task: '{task1}'")
    print(f"Complexity: {result['complexity_level']} (score: {result['complexity_score']}/20)")
    print(f"Recommended Model: {result['recommended_model']}")
    print(f"Estimated Cost: ${result['estimated_cost']:.3f}")
    
    # Example 2: Analyze complex task
    print("\n2️⃣ Analyzing Complex Task...")
    task2 = "Refactor authentication system with OAuth2 integration"
    result = await handle_analyze(task2)
    print(f"Task: '{task2}'")
    print(f"Complexity: {result['complexity_level']} (score: {result['complexity_score']}/20)")
    print(f"Recommended Model: {result['recommended_model']}")
    print(f"Agent Types Needed: {result.get('agent_types', 'multiple')}")
    
    # Example 3: Test model routing
    print("\n3️⃣ Testing Model Routing...")
    analyzer = TaskComplexityAnalyzer()
    selector = ModelSelector()
    
    test_cases = [
        ("Update version number", "developer"),
        ("Analyze codebase architecture", "analyst"),
        ("Review security vulnerabilities", "reviewer")
    ]
    
    for task, agent_type in test_cases:
        analysis = analyzer.analyze_task(task)
        selection = selector.select_model(analysis, agent_type)
        print(f"\nTask: '{task}' (Agent: {agent_type})")
        print(f"  → Model: {selection.primary_model}")
        print(f"  → Savings: {selection.cost_vs_claude:.0%}")
    
    # Example 4: Show orchestration command
    print("\n4️⃣ Orchestration Example (command only)...")
    print("To run a full orchestration, use:")
    print('  /logic agents orchestrate "Your task description"')
    print("\nOr in Python:")
    print('  await handle_orchestrate("Your task description")')
    
    print("\n" + "=" * 50)
    print("✅ Quick Start Complete!")
    print("\nNext steps:")
    print("1. Check API keys in .env file")
    print("2. Run the test suite: ./tests/run_tests.py")
    print("3. Try orchestrating a real task")
    print("4. Monitor cost savings in logs")


if __name__ == "__main__":
    asyncio.run(main())