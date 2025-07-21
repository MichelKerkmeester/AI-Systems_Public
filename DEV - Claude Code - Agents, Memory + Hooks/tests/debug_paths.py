#!/usr/bin/env python3
"""Debug script to check path resolution."""

from pathlib import Path

# Check various path calculations
prompt_enhancer_file = Path("/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/prompt_improver/prompt_enhancer.py")
project_root_calc = prompt_enhancer_file.parent.parent.parent.parent
claude_md_path = project_root_calc / "CLAUDE.md"

print(f"PromptEnhancer file: {prompt_enhancer_file}")
print(f"Calculated project root: {project_root_calc}")
print(f"CLAUDE.md path: {claude_md_path}")
print(f"CLAUDE.md exists: {claude_md_path.exists()}")
print(f"\nKnowledge path: {project_root_calc / '.claude' / 'knowledge'}")
print(f"Knowledge path exists: {(project_root_calc / '.claude' / 'knowledge').exists()}")

# Try loading patterns
patterns_path = project_root_calc / ".claude" / "knowledge" / "patterns.json"
print(f"\nPatterns path: {patterns_path}")
print(f"Patterns exists: {patterns_path.exists()}")

# Test loading CLAUDE.md
if claude_md_path.exists():
    with open(claude_md_path, 'r') as f:
        content = f.read()
    print(f"\nCLAUDE.md size: {len(content)} chars")
    print(f"Contains 'Development Philosophy': {'Development Philosophy' in content}")