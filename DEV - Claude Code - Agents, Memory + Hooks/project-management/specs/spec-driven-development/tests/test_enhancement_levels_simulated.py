#!/usr/bin/env python3
"""
Test different enhancement levels for the Prompt Improver system.
This simulates what different enhancement levels would do.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Add project paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "logic"))

from logic.prompt_improver.prompt_enhancer import PromptEnhancer, PromptType


def simulate_enhancement_level(prompt: str, level: str, enhancer: PromptEnhancer):
    """Simulate different enhancement levels."""
    
    # Analyze prompt type first
    prompt_type, context_info = enhancer.analyze_context(prompt)
    
    if level == "minimal":
        # Only add clarity if extremely vague (< 5 words)
        enhanced_prompt = prompt
        rules_applied = []
        
        if len(prompt.split()) < 5:
            enhanced_prompt = f"{prompt}\n\nPlease provide specific details about what you need."
            rules_applied.append("basic_clarity")
            
    elif level == "moderate":
        # Apply basic best practices
        enhanced_prompt = prompt
        rules_applied = []
        
        # Add clarity for short prompts
        if len(prompt.split()) < 10:
            enhanced_prompt = f"{enhanced_prompt}\n\nPlease provide specific details about what you need, including any constraints or requirements."
            rules_applied.append("clarity_enhancement")
        
        # Add output specification for code tasks
        if prompt_type in [PromptType.CODE_GENERATION, PromptType.CODE_REVIEW]:
            if "validation" in prompt.lower() or "validate" in prompt.lower():
                enhanced_prompt += "\n\nFor validation implementation, please include:"
                enhanced_prompt += "\n- Input validation rules"
                enhanced_prompt += "\n- Error handling"
                enhanced_prompt += "\n- User feedback messages"
                rules_applied.append("validation_context")
            else:
                enhanced_prompt += "\n\nPlease provide well-commented code following best practices."
                rules_applied.append("code_standards")
                
    else:  # aggressive
        # Full enhancement with all possible rules
        enhanced_prompt = prompt
        rules_applied = []
        
        # Always add clarity
        enhanced_prompt = f"{enhanced_prompt}\n\nPlease provide specific details about what you need, including any constraints or requirements."
        rules_applied.append("clarity_enhancement")
        
        # Add context for validation
        if "validation" in prompt.lower():
            enhanced_prompt += "\n\n## Validation Context:"
            enhanced_prompt += "\n- Input validation rules"
            enhanced_prompt += "\n- Error handling and edge cases"
            enhanced_prompt += "\n- User feedback messages"
            enhanced_prompt += "\n- Security considerations"
            enhanced_prompt += "\n- Performance impact"
            rules_applied.append("validation_context_comprehensive")
        
        # Add project-specific rules
        enhanced_prompt += "\n\n## Project Coding Principles:"
        enhanced_prompt += "\n- Elite JavaScript & CSS specialist - Fix root causes, not symptoms"
        enhanced_prompt += "\n- Production-grade code - DRY, KISS, secure, performant"
        enhanced_prompt += "\n- Webflow enhancement - Work with platform, never against it"
        rules_applied.append("core_coding_principles")
        
        # Add technical constraints
        enhanced_prompt += "\n\n## Technical Constraints:"
        enhanced_prompt += "\n- DOM: Never modify structure, Always use existing elements"
        enhanced_prompt += "\n- CSS: Never pixels, Always REM units + data attributes"
        enhanced_prompt += "\n- JS: Never console.log or globals, Always namespaces and element checks"
        rules_applied.append("technical_constraints")
        
        # Add output specification
        enhanced_prompt += "\n\n## Expected Output:"
        enhanced_prompt += "\n- Well-commented, production-ready code"
        enhanced_prompt += "\n- Follow all project standards and constraints"
        enhanced_prompt += "\n- Include error handling and edge cases"
        enhanced_prompt += "\n- Provide implementation notes and rationale"
        rules_applied.append("output_specification_detailed")
        
        # Add production checklist reminder
        enhanced_prompt += "\n\n## Production Checklist:"
        enhanced_prompt += "\n- [ ] No console.log statements"
        enhanced_prompt += "\n- [ ] No hardcoded API keys"
        enhanced_prompt += "\n- [ ] All tests passing"
        enhanced_prompt += "\n- [ ] Performance budgets met"
        enhanced_prompt += "\n- [ ] Security scan clean"
        rules_applied.append("production_checklist")
    
    return enhanced_prompt, rules_applied


def test_enhancement_levels():
    """Test the same prompt with different enhancement levels."""
    
    # The test prompt - simple validation request
    test_prompt = "add validation"
    
    # Results storage
    results = {
        "test_timestamp": datetime.now().isoformat(),
        "test_prompt": test_prompt,
        "enhancement_levels": {}
    }
    
    # Create enhancer instance
    enhancer = PromptEnhancer()
    
    # Test each enhancement level
    enhancement_levels = ["minimal", "moderate", "aggressive"]
    
    for level in enhancement_levels:
        print(f"\n{'='*60}")
        print(f"Testing Enhancement Level: {level}")
        print('='*60)
        
        # Simulate enhancement based on level
        enhanced_prompt, rules_applied = simulate_enhancement_level(test_prompt, level, enhancer)
        
        # Store results
        results["enhancement_levels"][level] = {
            "enhanced_prompt": enhanced_prompt,
            "rules_applied": rules_applied,
            "prompt_length_increase": len(enhanced_prompt) - len(test_prompt),
            "enhancement_ratio": round(len(enhanced_prompt) / len(test_prompt), 2),
            "line_count": len(enhanced_prompt.split('\n'))
        }
        
        # Display results
        print(f"\nOriginal prompt: '{test_prompt}'")
        print(f"\nEnhanced prompt:\n{'-'*40}\n{enhanced_prompt}\n{'-'*40}")
        print(f"\nRules applied ({len(rules_applied)}): {', '.join(rules_applied)}")
        print(f"Length increase: {results['enhancement_levels'][level]['prompt_length_increase']} chars")
        print(f"Enhancement ratio: {results['enhancement_levels'][level]['enhancement_ratio']}x")
        print(f"Line count: {results['enhancement_levels'][level]['line_count']} lines")
    
    # Save results to JSON file
    output_path = Path(__file__).parent / "enhancement-levels-results.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Results saved to: {output_path}")
    print('='*60)
    
    # Summary comparison
    print("\n## Summary Comparison")
    print(f"{'Level':<12} {'Rules':<6} {'Chars Added':<12} {'Ratio':<8} {'Lines'}")
    print("-" * 50)
    for level, data in results["enhancement_levels"].items():
        print(f"{level:<12} {len(data['rules_applied']):<6} {data['prompt_length_increase']:<12} {data['enhancement_ratio']}x{'':<5} {data['line_count']}")
    
    # Show differences in approach
    print("\n## Enhancement Level Differences")
    print("\n### Minimal:")
    print("- Only adds basic clarity for extremely vague prompts (< 5 words)")
    print("- No project-specific rules or constraints")
    print("- Lightest touch possible")
    
    print("\n### Moderate:")
    print("- Adds clarity for short prompts (< 10 words)")
    print("- Includes context-specific guidance (e.g., validation tips)")
    print("- Basic code standards reminders")
    print("- Balanced enhancement without being overwhelming")
    
    print("\n### Aggressive:")
    print("- Always adds comprehensive clarity")
    print("- Injects all project-specific rules from CLAUDE.md")
    print("- Includes technical constraints and platform limits")
    print("- Adds production checklist")
    print("- Maximum assistance and structure")


if __name__ == "__main__":
    test_enhancement_levels()