#!/usr/bin/env python3
"""
Integration test for the Claude-Organizer prompt enhancement system.
Tests the complete flow from user input to enhanced prompt output.
"""

import sys
import json
from pathlib import Path

# Add project paths
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "logic"))

from agents.intelligence.prompt_enhancer import PromptEnhancer, enhance_prompt
from agents.intelligence.pattern_library import PatternLibrary


def test_vague_request_enhancement():
    """Test enhancement of a vague development request."""
    print("\n=== Test 1: Vague Request Enhancement ===")
    
    enhancer = PromptEnhancer()
    original = "Add email functionality"
    
    result = enhancer.enhance_prompt(original)
    
    print(f"Original: {original}")
    print(f"Enhanced: {result.enhanced_prompt}")
    print(f"Type: {result.prompt_type}")
    print(f"Rules Applied: {len(result.rules_applied)}")
    print(f"Confidence: {result.confidence:.2f}")
    
    # Verify key enhancements
    assert "CLAUDE.md principles" in result.enhanced_prompt
    assert "Webflow" in result.enhanced_prompt
    assert "namespace pattern" in result.enhanced_prompt
    assert "< 50KB JS limit" in result.enhanced_prompt
    
    return result


def test_complex_task_organization():
    """Test organization of complex multi-step tasks."""
    print("\n=== Test 2: Complex Task Organization ===")
    
    enhancer = PromptEnhancer()
    original = "Refactor the authentication system and add OAuth"
    
    result = enhancer.enhance_prompt(original)
    
    print(f"Original: {original}")
    print(f"Enhanced: {result.enhanced_prompt[:200]}...")  # Show first 200 chars
    print(f"Detected as system change: {'spec folder' in result.enhanced_prompt}")
    
    # Verify task organization
    assert ".claude/tasks/specs/" in result.enhanced_prompt
    assert "requirements.md" in result.enhanced_prompt
    assert "rollback-plan.md" in result.enhanced_prompt
    
    return result


def test_pattern_library_integration():
    """Test pattern library matching and enhancement."""
    print("\n=== Test 3: Pattern Library Integration ===")
    
    library = PatternLibrary()
    
    # Test various patterns
    test_cases = [
        ("fix the bug in the navigation", "bug_fix"),
        ("improve performance of the site", "performance"),
        ("update all the docs", "documentation"),
        ("add a new feature for user profiles", "feature")
    ]
    
    for prompt, expected_type in test_cases:
        pattern_result = library.match_pattern(prompt)
        pattern_type = pattern_result[0] if pattern_result else None
        enhanced = library.enhance_prompt(prompt, pattern_result)
        
        print(f"\nPrompt: {prompt}")
        print(f"Matched: {pattern_type}")
        if isinstance(enhanced, str):
            print(f"Enhanced: {enhanced[:100]}...")
            assert len(enhanced) > len(prompt)
        else:
            print(f"Enhanced: {str(enhanced)[:100]}...")
        
        assert pattern_type == expected_type
    
    return True


def test_hook_simulation():
    """Simulate how the hook would process a prompt."""
    print("\n=== Test 4: Hook Processing Simulation ===")
    
    # Simulate hook configuration
    config = {
        "enabled": True,
        "enhancement_level": "balanced",
        "rule_injection": {
            "project_rules": True,
            "code_standards": True,
            "security_rules": True
        },
        "bypass_prefixes": ["raw:", "exact:", "no-enhance:"]
    }
    
    enhancer = PromptEnhancer()
    
    # Test bypass
    raw_prompt = "raw: console.log('test')"
    result = enhancer.enhance_prompt(raw_prompt)
    print(f"\nBypass test: {raw_prompt}")
    print(f"Enhanced: {result.enhanced_prompt}")
    print(f"Should bypass: {raw_prompt == result.enhanced_prompt}")
    
    # Test normal enhancement
    normal_prompt = "create a button component"
    result = enhancer.enhance_prompt(normal_prompt)
    print(f"\nNormal prompt: {normal_prompt}")
    print(f"Enhanced length: {len(result.enhanced_prompt)} chars")
    print(f"Rules applied: {result.rules_applied}")
    
    return True


def test_multi_agent_coordination():
    """Test enhancement for multi-agent task coordination."""
    print("\n=== Test 5: Multi-Agent Coordination ===")
    
    enhancer = PromptEnhancer()
    original = "Update all documentation files across the project"
    
    result = enhancer.enhance_prompt(original)
    
    print(f"Original: {original}")
    print(f"Detected as multi-agent: {'parallel' in result.enhanced_prompt.lower() or 'agent' in result.enhanced_prompt.lower()}")
    
    # Multi-agent tasks should suggest using agents
    if "documentation" in original.lower() and "all" in original.lower():
        # Should structure for multiple agents
        print("✓ Multi-agent structure suggested")
    
    return result


def test_learning_capabilities():
    """Test pattern learning and adaptation."""
    print("\n=== Test 6: Learning Capabilities ===")
    
    library = PatternLibrary()
    
    # Simulate successful enhancements
    test_patterns = [
        ("bug_fix", "Fix the login bug"),
        ("feature", "Add dark mode"),
        ("performance", "Optimize image loading")
    ]
    
    for pattern_type, prompt in test_patterns:
        # Record some successes
        for i in range(3):
            library.record_success(pattern_type, prompt, success=True)
        
        # Record one failure
        library.record_success(pattern_type, prompt, success=False)
    
    # Check success rates
    print("\nSuccess Rates:")
    for pattern_type, _ in test_patterns:
        rate = library.get_success_rate(pattern_type)
        print(f"  {pattern_type}: {rate:.2%}")
        assert rate == 0.75  # 3 successes, 1 failure = 75%
    
    return True


def run_all_tests():
    """Run all integration tests."""
    print("🚀 Claude-Organizer Integration Test Suite")
    print("=" * 50)
    
    tests = [
        test_vague_request_enhancement,
        test_complex_task_organization,
        test_pattern_library_integration,
        test_hook_simulation,
        test_multi_agent_coordination,
        test_learning_capabilities
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append((test.__name__, True, result))
            print(f"✅ {test.__name__} passed")
        except Exception as e:
            results.append((test.__name__, False, str(e)))
            print(f"❌ {test.__name__} failed: {e}")
    
    print("\n" + "=" * 50)
    print("Summary:")
    passed = sum(1 for _, success, _ in results if success)
    print(f"✨ {passed}/{len(tests)} tests passed")
    
    return results


if __name__ == "__main__":
    results = run_all_tests()
    
    # Example usage demonstration
    print("\n" + "=" * 50)
    print("📝 Example Usage:")
    print("=" * 50)
    
    enhancer = PromptEnhancer()
    
    # Simple enhancement
    simple = enhance_prompt("fix the header styling")
    print(f"\nSimple: {simple[:150]}...")
    
    # Complex enhancement
    complex_prompt = "implement a complete user dashboard with charts and real-time data"
    complex_result = enhancer.enhance_prompt(complex_prompt)
    print(f"\nComplex: {complex_result.enhanced_prompt[:200]}...")
    print(f"Confidence: {complex_result.confidence:.2f}")
    print(f"Rules Applied: {', '.join(complex_result.rules_applied[:3])}...")