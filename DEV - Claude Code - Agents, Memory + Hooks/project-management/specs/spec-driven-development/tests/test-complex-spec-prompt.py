#!/usr/bin/env python3
"""
Test the Prompt Improver with a complex, multi-part spec-driven development prompt.

This test analyzes how the Prompt Improver handles:
1. Complex multi-part requests
2. File path references
3. Analysis and implementation requests
4. Parallel sub-agent suggestions
5. Special keywords like "UltraThink ThinkHarder"
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Add the logic directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "logic"))

from prompt_improver.prompt_enhancer import PromptEnhancer, PromptType
from prompt_improver.pattern_library import PatternLibrary


def test_complex_spec_prompt():
    """Test the complex spec-driven development prompt."""
    
    # The complex test prompt
    test_prompt = """- Analyze this spec:*/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/tasks/specs/enhancements/spec-driven-development-proposal.md*
- Suggest your plan and afterwards implement it
- Make sure to analyze the recently completed tasks /Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/tasks/completed, and the whole system, and make sure you don't break anything of it or if you add stuff that wont work together with it.
- Can you use parallel sub-agents to speed up
this task? UltraThink ThinkHarder"""
    
    # Initialize the enhancer
    enhancer = PromptEnhancer()
    
    # Run the enhancement
    result = enhancer.enhance_prompt(test_prompt)
    
    # Analyze the results
    analysis = {
        "timestamp": datetime.now().isoformat(),
        "test_name": "Complex Spec-Driven Development Prompt",
        "original_prompt": test_prompt,
        "enhanced_prompt": result.enhanced_prompt,
        "prompt_type_detected": result.prompt_type.value,
        "rules_applied": result.rules_applied,
        "patterns_matched": result.patterns_matched,
        "confidence_score": result.confidence,
        
        # Detailed analysis
        "analysis": {
            "multi_part_handling": {
                "parts_identified": [],
                "structure_added": False,
                "clarity_improved": False
            },
            "file_path_handling": {
                "paths_detected": [],
                "path_validation": False,
                "context_added": False
            },
            "keyword_handling": {
                "ultrathink_detected": False,
                "thinkharder_detected": False,
                "special_processing": False
            },
            "agent_coordination": {
                "parallel_agents_mentioned": False,
                "coordination_suggested": False,
                "task_breakdown": False
            },
            "safety_considerations": {
                "breaking_changes_warning": False,
                "compatibility_check": False,
                "system_analysis_suggested": False
            }
        }
    }
    
    # Analyze multi-part handling
    prompt_lines = test_prompt.strip().split('\n')
    analysis["analysis"]["multi_part_handling"]["parts_identified"] = [
        line.strip() for line in prompt_lines if line.strip().startswith('-')
    ]
    analysis["analysis"]["multi_part_handling"]["structure_added"] = (
        "complex_structure" in result.rules_applied
    )
    analysis["analysis"]["multi_part_handling"]["clarity_improved"] = (
        "clarity_enhancement" in result.rules_applied
    )
    
    # Analyze file path handling
    import re
    file_paths = re.findall(r'/Users/[^*\s]+', test_prompt)
    analysis["analysis"]["file_path_handling"]["paths_detected"] = file_paths
    analysis["analysis"]["file_path_handling"]["path_validation"] = any(
        "file" in rule.lower() for rule in result.rules_applied
    )
    analysis["analysis"]["file_path_handling"]["context_added"] = (
        "Context:" in result.enhanced_prompt
    )
    
    # Analyze keyword handling
    analysis["analysis"]["keyword_handling"]["ultrathink_detected"] = (
        "ultrathink" in test_prompt.lower()
    )
    analysis["analysis"]["keyword_handling"]["thinkharder_detected"] = (
        "thinkharder" in test_prompt.lower()
    )
    analysis["analysis"]["keyword_handling"]["special_processing"] = any(
        keyword in result.enhanced_prompt.lower() 
        for keyword in ["ultrathink", "thinkharder", "deep analysis", "thorough"]
    )
    
    # Analyze agent coordination
    analysis["analysis"]["agent_coordination"]["parallel_agents_mentioned"] = (
        "parallel sub-agents" in test_prompt.lower()
    )
    analysis["analysis"]["agent_coordination"]["coordination_suggested"] = any(
        "coordination" in rule or "parallel" in rule 
        for rule in result.rules_applied
    )
    analysis["analysis"]["agent_coordination"]["task_breakdown"] = (
        "task_breakdown" in str(result.rules_applied) or
        "Task Management" in result.enhanced_prompt
    )
    
    # Analyze safety considerations
    analysis["analysis"]["safety_considerations"]["breaking_changes_warning"] = (
        "don't break" in test_prompt.lower() or 
        "breaking changes" in result.enhanced_prompt.lower()
    )
    analysis["analysis"]["safety_considerations"]["compatibility_check"] = (
        "won't work together" in test_prompt.lower() or
        "compatibility" in result.enhanced_prompt.lower()
    )
    analysis["analysis"]["safety_considerations"]["system_analysis_suggested"] = (
        "analyze" in test_prompt.lower() and
        "system" in test_prompt.lower()
    )
    
    # Additional insights
    analysis["insights"] = {
        "prompt_complexity": {
            "line_count": len(prompt_lines),
            "word_count": len(test_prompt.split()),
            "character_count": len(test_prompt),
            "bullet_points": len([l for l in prompt_lines if l.strip().startswith('-')])
        },
        "enhancement_effectiveness": {
            "original_length": len(test_prompt),
            "enhanced_length": len(result.enhanced_prompt),
            "expansion_ratio": len(result.enhanced_prompt) / len(test_prompt),
            "rules_count": len(result.rules_applied),
            "patterns_count": len(result.patterns_matched)
        },
        "prompt_type_accuracy": {
            "detected_type": result.prompt_type.value,
            "expected_types": ["task_planning", "system_design", "code_generation"],
            "type_appropriate": result.prompt_type.value in ["task_planning", "system_design", "code_generation"]
        }
    }
    
    # Test with pattern library
    pattern_lib = PatternLibrary()
    pattern_result = pattern_lib.enhance_prompt(test_prompt)
    
    analysis["pattern_library_results"] = {
        "pattern_matched": pattern_result["pattern_matched"],
        "enhancements": pattern_result["enhancements"],
        "enhanced_prompt_different": pattern_result["enhanced"] != test_prompt
    }
    
    # Summary and recommendations
    analysis["summary"] = {
        "overall_handling": "Good" if result.confidence > 0.7 else "Needs Improvement",
        "strengths": [],
        "weaknesses": [],
        "recommendations": []
    }
    
    # Identify strengths
    if analysis["analysis"]["multi_part_handling"]["structure_added"]:
        analysis["summary"]["strengths"].append("Successfully structured complex multi-part prompt")
    
    if analysis["analysis"]["file_path_handling"]["paths_detected"]:
        analysis["summary"]["strengths"].append(f"Detected {len(file_paths)} file paths")
    
    if analysis["analysis"]["agent_coordination"]["task_breakdown"]:
        analysis["summary"]["strengths"].append("Added task management guidance")
    
    if result.confidence > 0.8:
        analysis["summary"]["strengths"].append(f"High confidence score: {result.confidence:.2f}")
    
    # Identify weaknesses
    if not analysis["analysis"]["keyword_handling"]["special_processing"]:
        analysis["summary"]["weaknesses"].append("Did not process special keywords (UltraThink ThinkHarder)")
    
    if not analysis["analysis"]["agent_coordination"]["coordination_suggested"]:
        analysis["summary"]["weaknesses"].append("Did not address parallel sub-agent request")
    
    if not any("spec" in rule.lower() for rule in result.rules_applied):
        analysis["summary"]["weaknesses"].append("Did not apply spec-specific enhancements")
    
    # Recommendations
    analysis["summary"]["recommendations"].append(
        "Add pattern recognition for 'UltraThink' and 'ThinkHarder' keywords"
    )
    analysis["summary"]["recommendations"].append(
        "Implement spec file path validation and context injection"
    )
    analysis["summary"]["recommendations"].append(
        "Add rules for parallel agent coordination suggestions"
    )
    analysis["summary"]["recommendations"].append(
        "Enhance breaking change detection and compatibility warnings"
    )
    
    return analysis


def main():
    """Run the test and save results."""
    print("Testing Prompt Improver with complex spec-driven development prompt...")
    
    # Run the test
    results = test_complex_spec_prompt()
    
    # Save results
    output_path = Path(__file__).parent / "complex-spec-prompt-results.json"
    
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nTest completed! Results saved to: {output_path}")
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Prompt Type Detected: {results['prompt_type_detected']}")
    print(f"Rules Applied: {len(results['rules_applied'])}")
    print(f"Patterns Matched: {len(results['patterns_matched'])}")
    print(f"Confidence Score: {results['confidence_score']:.2f}")
    print(f"Overall Handling: {results['summary']['overall_handling']}")
    
    if results['summary']['strengths']:
        print("\nStrengths:")
        for strength in results['summary']['strengths']:
            print(f"  ✓ {strength}")
    
    if results['summary']['weaknesses']:
        print("\nWeaknesses:")
        for weakness in results['summary']['weaknesses']:
            print(f"  ✗ {weakness}")
    
    print("\nRecommendations:")
    for rec in results['summary']['recommendations']:
        print(f"  • {rec}")


if __name__ == "__main__":
    main()