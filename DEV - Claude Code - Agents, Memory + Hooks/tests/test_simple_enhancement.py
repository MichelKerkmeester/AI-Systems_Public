#!/usr/bin/env python3
"""Simple test to verify prompt enhancement is working."""

import sys
from pathlib import Path

# Add project paths
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "logic"))

from agents.intelligence.prompt_enhancer import PromptEnhancer, PromptType

# Create enhancer
enhancer = PromptEnhancer()

# Test basic enhancement
print("Testing PromptEnhancer...")
print(f"CLAUDE.md loaded: {bool(enhancer.claude_md_rules)}")
print(f"Patterns loaded: {bool(enhancer.patterns)}")
print(f"Constraints loaded: {bool(enhancer.constraints)}")

# Test simple prompt
test_prompt = "Create a button component"
result = enhancer.enhance_prompt(test_prompt)

print(f"\nOriginal: {test_prompt}")
print(f"Enhanced: {result.enhanced_prompt[:200]}...")
print(f"Type: {result.prompt_type}")
print(f"Rules Applied: {result.rules_applied}")
print(f"Confidence: {result.confidence}")

# Test vague prompt
vague_prompt = "make it better"
vague_result = enhancer.enhance_prompt(vague_prompt)
print(f"\nVague prompt: {vague_prompt}")
print(f"Enhanced: {vague_result.enhanced_prompt[:200]}...")

# Test code generation prompt
code_prompt = "implement user authentication"
code_result = enhancer.enhance_prompt(code_prompt)
print(f"\nCode generation: {code_prompt}")
print(f"Type detected: {code_result.prompt_type}")
print(f"Rules applied: {code_result.rules_applied}")