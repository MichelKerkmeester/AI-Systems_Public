#!/usr/bin/env python3
"""Test different enhancement levels for the Prompt Improver system."""

import sys
import json
from pathlib import Path
from datetime import datetime

# Add project paths
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "logic"))

from logic.prompt_improver.prompt_enhancer import PromptEnhancer, PromptType


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
    
    # Test each enhancement level
    enhancement_levels = ["minimal", "moderate", "aggressive"]
    
    for level in enhancement_levels:
        print(f"\n{'='*60}")
        print(f"Testing Enhancement Level: {level}")
        print('='*60)
        
        # Create enhancer (in production, this would read from settings)
        enhancer = PromptEnhancer()
        
        # Simulate different enhancement levels by controlling which methods are called
        if level == "minimal":
            # Only basic clarity enhancement
            enhanced_prompt = test_prompt
            if len(test_prompt.split()) < 10:
                enhanced_prompt = f"{test_prompt}\n\nPlease provide specific details about what you need, including any constraints or requirements."
            rules_applied = ["clarity_enhancement"] if enhanced_prompt != test_prompt else []
            
        elif level == "moderate":
            # Apply best practices but no rule injection
            result = enhancer.enhance_prompt(test_prompt)
            enhanced_prompt = result.enhanced_prompt
            # Filter out CLAUDE.md specific rules
            rules_applied = [rule for rule in result.rules_applied 
                           if rule in ["clarity_enhancement", "code_context_addition", 
                                     "output_specification", "complex_structure"]]
            
        else:  # aggressive
            # Full enhancement with all rules
            result = enhancer.enhance_prompt(test_prompt)
            enhanced_prompt = result.enhanced_prompt
            rules_applied = result.rules_applied
        
        # Store results
        results["enhancement_levels"][level] = {
            "enhanced_prompt": enhanced_prompt,
            "rules_applied": rules_applied,
            "prompt_length_increase": len(enhanced_prompt) - len(test_prompt),
            "enhancement_ratio": round(len(enhanced_prompt) / len(test_prompt), 2)
        }
        
        # Display results
        print(f"\nOriginal prompt: '{test_prompt}'")
        print(f"Enhanced prompt:\n{enhanced_prompt}")
        print(f"\nRules applied: {rules_applied}")
        print(f"Length increase: {results['enhancement_levels'][level]['prompt_length_increase']} chars")
        print(f"Enhancement ratio: {results['enhancement_levels'][level]['enhancement_ratio']}x")
    
    # Save results to JSON file
    output_path = Path(__file__).parent / "enhancement-levels-results.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Results saved to: {output_path}")
    print('='*60)
    
    # Summary comparison
    print("\n## Summary Comparison")
    print(f"{'Level':<12} {'Rules Applied':<8} {'Length Increase':<16} {'Enhancement Ratio'}")
    print("-" * 60)
    for level, data in results["enhancement_levels"].items():
        print(f"{level:<12} {len(data['rules_applied']):<8} {data['prompt_length_increase']:<16} {data['enhancement_ratio']}x")


if __name__ == "__main__":
    test_enhancement_levels()