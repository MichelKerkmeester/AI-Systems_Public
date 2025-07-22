#!/usr/bin/env python3
"""
Knowledge Enforcement Hook

This hook automatically loads and enforces rules from the /knowledge directory:
- facts.json: Platform facts and project context
- patterns.json: Code patterns and conventions
- constraints.json: Strict rules and validations

It ensures that all AI operations respect the knowledge base without
duplicating rules in CLAUDE.md.
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any, Optional, List

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[2]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, UserPromptHook, MessageFormatter


class KnowledgeEnforcementHook(UserPromptHook):
    """Loads and enforces knowledge base rules on every user prompt"""
    
    def __init__(self):
        super().__init__()
        self.name = "Knowledge Base Enforcement"
        self.priority = 95  # Very high priority - runs early
        self.knowledge_dir = Path(__file__).resolve().parents[3] / "knowledge"
        self.knowledge_cache = {}
        
    def load_knowledge_files(self) -> Dict[str, Any]:
        """Load all knowledge files into memory"""
        knowledge_files = ['facts.json', 'patterns.json', 'constraints.json']
        
        for filename in knowledge_files:
            filepath = self.knowledge_dir / filename
            if filepath.exists():
                try:
                    with open(filepath, 'r') as f:
                        self.knowledge_cache[filename] = json.load(f)
                except Exception as e:
                    self.formatter.error(f"Failed to load {filename}: {str(e)}")
                    
        return self.knowledge_cache
        
    def generate_knowledge_summary(self) -> str:
        """Generate a concise summary of key rules for the AI"""
        summary_lines = [
            "\n🧠 KNOWLEDGE BASE LOADED:",
            "→ See /knowledge/ for complete rules and patterns",
            "\nKEY ENFORCEMENTS:"
        ]
        
        # Extract key constraints
        if 'constraints.json' in self.knowledge_cache:
            constraints = self.knowledge_cache['constraints.json']
            if 'strict_rules' in constraints:
                summary_lines.append("\n⚠️ STRICT RULES:")
                for rule_name, rule_data in constraints['strict_rules'].items():
                    if isinstance(rule_data, dict) and 'rule' in rule_data:
                        summary_lines.append(f"  • {rule_data['rule']}")
                        if 'exception' in rule_data:
                            summary_lines.append(f"    Exception: {rule_data['exception'].get('file', 'N/A')}")
                            
        # Extract key patterns
        if 'patterns.json' in self.knowledge_cache:
            patterns = self.knowledge_cache['patterns.json']
            summary_lines.append("\n📋 CODE PATTERNS:")
            summary_lines.append("  • Comment styles defined in patterns.json")
            summary_lines.append("  • Module patterns: IIFE with direct execution")
            summary_lines.append("  • See /knowledge/patterns.json for examples")
            
        # Extract key facts
        if 'facts.json' in self.knowledge_cache:
            facts = self.knowledge_cache['facts.json']
            if 'platform' in facts:
                summary_lines.append("\n📌 PLATFORM FACTS:")
                platform = facts['platform']
                if 'slater' in platform:
                    summary_lines.append(f"  • Slater v{platform['slater'].get('version', 'unknown')} is active")
                    summary_lines.append("  • Slater autoloads - no DOMContentLoaded needed")
                    
        summary_lines.append("\n💡 All rules enforced automatically via hooks")
        return '\n'.join(summary_lines)
        
    def validate_against_knowledge(self, prompt: str) -> List[Dict[str, str]]:
        """Check if prompt might violate knowledge base rules"""
        violations = []
        
        # Check for common anti-patterns mentioned in prompt
        prompt_lower = prompt.lower()
        
        # Check for DOMContentLoaded requests
        if 'domcontentloaded' in prompt_lower or 'document ready' in prompt_lower:
            violations.append({
                'type': 'warning',
                'rule': 'no_domcontentloaded',
                'message': 'Reminder: Slater autoloads scripts - DOMContentLoaded is not needed',
                'reference': '/knowledge/constraints.json → strict_rules.no_domcontentloaded'
            })
            
        # Check for Vite references
        if 'vite' in prompt_lower:
            violations.append({
                'type': 'warning',
                'rule': 'no_vite_references',
                'message': 'Reminder: Slater is the active build tool, not Vite',
                'reference': '/knowledge/constraints.json → strict_rules.no_vite_references'
            })
            
        # Check for console.log requests
        if 'console.log' in prompt_lower or 'console log' in prompt_lower:
            violations.append({
                'type': 'info',
                'rule': 'no_console_log',
                'message': 'Note: console.log not allowed - use console.warn/error for critical cases only',
                'reference': '/knowledge/constraints.json → strict_rules.no_console_log'
            })
            
        return violations
        
    def run(self, user_input: str, **kwargs) -> Tuple[str, Optional[Dict[str, Any]]]:
        """Process user prompt and inject knowledge base context"""
        # Load knowledge files
        self.load_knowledge_files()
        
        # Generate summary for AI context
        knowledge_summary = self.generate_knowledge_summary()
        
        # Check for potential violations
        violations = self.validate_against_knowledge(user_input)
        
        # Build response
        response_parts = []
        
        # Add violations if any
        if violations:
            response_parts.append("📚 Knowledge Base Reminders:")
            for violation in violations:
                icon = "⚠️" if violation['type'] == 'warning' else "ℹ️"
                response_parts.append(f"{icon} {violation['message']}")
                response_parts.append(f"   → {violation['reference']}")
            response_parts.append("")
            
        # Add knowledge summary
        response_parts.append(knowledge_summary)
        
        # Create metadata
        metadata = {
            'knowledge_loaded': list(self.knowledge_cache.keys()),
            'violations_found': len(violations),
            'hook': 'knowledge-enforcement'
        }
        
        # If we have content to add, format it nicely
        if response_parts:
            return '\n'.join(response_parts) + '\n', metadata
        else:
            return "", metadata
            
    def get_tools(self) -> List[str]:
        """This hook runs on user prompts, not tool use"""
        return []


if __name__ == "__main__":
    # Test the hook
    hook = KnowledgeEnforcementHook()
    
    # Test various prompts
    test_prompts = [
        "Add a DOMContentLoaded listener to initialize the component",
        "Set up Vite for the project",
        "Add console.log statements for debugging",
        "Create a new navigation component"
    ]
    
    for prompt in test_prompts:
        print(f"\n{'='*60}")
        print(f"Testing prompt: {prompt}")
        print('='*60)
        response, metadata = hook.run(prompt)
        if response:
            print(response)
        print(f"Metadata: {metadata}")