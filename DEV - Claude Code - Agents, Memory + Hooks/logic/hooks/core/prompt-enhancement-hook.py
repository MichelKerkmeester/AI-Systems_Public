#!/usr/bin/env python3
"""
Prompt Enhancement Hook for Claude-Organizer
Integrates with UserPromptSubmit pipeline to enhance user prompts
based on project best practices and CLAUDE.md rules
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import (
    HookBase, UserPromptHook,
    SettingsManager, StateManager,
    MessageFormatter
)
from logic.prompt_improver import PromptEnhancer, EnhancementResult


class PromptEnhancementHook(UserPromptHook):
    """Hook for enhancing user prompts with best practices and project rules"""
    
    def __init__(self):
        super().__init__()
        
        # Settings path
        self.settings_path = self.claude_path / "logic" / "hooks" / "core" / "prompt-enhancement-settings.json"
        
        # Initialize managers
        self.settings = SettingsManager(self.settings_path, self._get_default_settings())
        
        # Initialize prompt enhancer
        self.enhancer = PromptEnhancer()
        
        # Bypass patterns
        self._init_bypass_patterns()
        
        # Enhancement tracking
        self.state_path = self.claude_path / "state" / "prompt-enhancement-state.json"
        self.state = StateManager(self.state_path, self._get_default_state())
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """Get default settings for prompt enhancement"""
        return {
            "enabled": True,
            "enhancement_level": "moderate",  # minimal, moderate, aggressive
            "show_enhancement_notice": True,
            "show_enhancement_details": False,
            "bypass_prefixes": ["raw:", "exact:", "no-enhance:"],
            "always_enhance_types": ["code_generation", "code_review"],
            "never_enhance_types": [],
            "log_enhancements": True,
            "max_prompt_length": 10000,  # Skip enhancement for very long prompts
            "enhancement_thresholds": {
                "minimal": {
                    "min_word_count": 5,
                    "add_context": False,
                    "inject_rules": "essential"
                },
                "moderate": {
                    "min_word_count": 3,
                    "add_context": True,
                    "inject_rules": "relevant"
                },
                "aggressive": {
                    "min_word_count": 1,
                    "add_context": True,
                    "inject_rules": "comprehensive"
                }
            }
        }
    
    def _get_default_state(self) -> Dict[str, Any]:
        """Get default state for tracking"""
        return {
            "enhancement_count": 0,
            "bypass_count": 0,
            "rules_applied": {},
            "prompt_types": {},
            "recent_enhancements": [],
            "last_enhancement": None,
            "errors": []
        }
    
    def _init_bypass_patterns(self):
        """Initialize patterns that bypass enhancement"""
        self.bypass_patterns = [
            # Direct bypass prefixes
            r"^(raw|exact|no-enhance):\s*",
            # Command patterns
            r"^/\w+\s+",  # Commands like /memory, /save
            # System messages
            r"^(error|warning|info):\s*",
            # Code blocks (don't enhance if prompt is mainly code)
            r"^```[\s\S]+```$",
            # Simple confirmations
            r"^(yes|no|ok|cancel|continue|stop)$"
        ]
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process user prompt for enhancement"""
        # Check if enhancement is enabled
        if not self.settings.get("enabled"):
            return 0, None
        
        # Get user message
        user_message = self.get_user_message()
        if not user_message:
            return 0, None
        
        # Check for bypass conditions
        if self._should_bypass(user_message):
            if self.settings.get("log_enhancements"):
                self._log_bypass(user_message)
            return 0, None
        
        # Check prompt length
        if len(user_message) > self.settings.get("max_prompt_length", 10000):
            return 0, None
        
        try:
            # Enhance the prompt
            enhancement_result = self._enhance_prompt(user_message)
            
            # Check if enhancement actually changed anything
            if enhancement_result.enhanced_prompt == user_message:
                return 0, None
            
            # Update the hook input with enhanced prompt
            self.hook_input["userMessage"] = enhancement_result.enhanced_prompt
            
            # Log enhancement if enabled
            if self.settings.get("log_enhancements"):
                self._log_enhancement(user_message, enhancement_result)
            
            # Generate output message if configured
            output = self._generate_output(user_message, enhancement_result)
            
            # Return with modified input (exit code 0 to continue)
            return 0, output
            
        except Exception as e:
            # Log error but don't block
            if self.settings.get("log_enhancements"):
                self.state.update({
                    "last_error": str(e),
                    "error_timestamp": self.state.get_timestamp()
                })
            return 0, None
    
    def _should_bypass(self, prompt: str) -> bool:
        """Check if prompt should bypass enhancement"""
        prompt_lower = prompt.lower().strip()
        
        # Check bypass prefixes
        for prefix in self.settings.get("bypass_prefixes", []):
            if prompt_lower.startswith(prefix.lower()):
                return True
        
        # Check bypass patterns
        for pattern in self.bypass_patterns:
            if re.match(pattern, prompt, re.IGNORECASE):
                return True
        
        # Check if it's a simple query
        word_count = len(prompt.split())
        if word_count < 3 and "?" not in prompt:
            return True
        
        return False
    
    def _enhance_prompt(self, prompt: str) -> EnhancementResult:
        """Enhance the prompt based on settings"""
        # Get enhancement level
        level = self.settings.get("enhancement_level", "moderate")
        
        # Apply enhancement
        result = self.enhancer.enhance_prompt(prompt)
        
        # Filter based on level settings
        if level == "minimal":
            # For minimal, only apply essential enhancements
            result = self._apply_minimal_enhancement(prompt, result)
        elif level == "moderate":
            # Moderate is the default behavior
            pass
        elif level == "aggressive":
            # For aggressive, add extra context
            result = self._apply_aggressive_enhancement(result)
        
        # Check type-based rules
        if result.prompt_type.value in self.settings.get("never_enhance_types", []):
            result.enhanced_prompt = prompt  # Revert to original
        
        return result
    
    def _apply_minimal_enhancement(self, original: str, result: EnhancementResult) -> EnhancementResult:
        """Apply minimal enhancement - only essential changes"""
        # For minimal, we might want to skip some injected rules
        # but keep clarity improvements
        essential_rules = ["core_coding_principles", "security", "critical_constraints"]
        
        # Filter rules to only essential ones
        filtered_rules = [r for r in result.rules_applied if any(e in r for e in essential_rules)]
        
        # If too many rules were applied, revert to a simpler enhancement
        if len(result.rules_applied) > 3:
            # Re-run with just clarity enhancement
            enhanced = original
            if len(original.split()) < 10:
                enhanced = f"{original}\n\nPlease provide specific details about what you need."
            
            return EnhancementResult(
                enhanced_prompt=enhanced,
                prompt_type=result.prompt_type,
                rules_applied=["clarity_enhancement"],
                patterns_matched=result.patterns_matched,
                confidence=0.6
            )
        
        return result
    
    def _apply_aggressive_enhancement(self, result: EnhancementResult) -> EnhancementResult:
        """Apply aggressive enhancement - add extra context"""
        # Add extra context based on prompt type
        extra_context = {
            "code_generation": "\n\n## Additional Context:\n- Follow DRY and KISS principles\n- Include comprehensive error handling\n- Add detailed comments for complex logic\n- Consider edge cases and input validation",
            "code_review": "\n\n## Review Focus:\n- Security vulnerabilities\n- Performance bottlenecks\n- Code maintainability\n- Best practices compliance\n- Test coverage",
            "debugging": "\n\n## Debugging Approach:\n- Reproduce the issue first\n- Check browser console and network logs\n- Verify all assumptions\n- Test fix thoroughly before claiming resolution"
        }
        
        # Add type-specific context
        type_context = extra_context.get(result.prompt_type.value, "")
        if type_context and type_context not in result.enhanced_prompt:
            result.enhanced_prompt += type_context
            result.rules_applied.append("aggressive_context_injection")
        
        return result
    
    def _log_bypass(self, prompt: str):
        """Log bypass event"""
        self.state.update({
            "last_bypass": {
                "prompt_preview": prompt[:100] + "..." if len(prompt) > 100 else prompt,
                "timestamp": self.state.get_timestamp(),
                "reason": "bypass_pattern_matched"
            },
            "bypass_count": self.state.get("bypass_count", 0) + 1
        })
    
    def _log_enhancement(self, original: str, result: EnhancementResult):
        """Log enhancement details"""
        enhancement_data = {
            "timestamp": self.state.get_timestamp(),
            "original_length": len(original),
            "enhanced_length": len(result.enhanced_prompt),
            "prompt_type": result.prompt_type.value,
            "rules_applied": result.rules_applied,
            "patterns_matched": result.patterns_matched,
            "confidence": result.confidence,
            "level": self.settings.get("enhancement_level")
        }
        
        # Update state
        self.state.update({
            "last_enhancement": enhancement_data,
            "enhancement_count": self.state.get("enhancement_count", 0) + 1,
            "total_rules_applied": self.state.get("total_rules_applied", 0) + len(result.rules_applied)
        })
        
        # Keep history of recent enhancements
        history = self.state.get("recent_enhancements", [])
        history.append(enhancement_data)
        # Keep only last 10
        if len(history) > 10:
            history = history[-10:]
        self.state.set("recent_enhancements", history)
    
    def _generate_output(self, original: str, result: EnhancementResult) -> Optional[str]:
        """Generate output message about enhancement"""
        if not self.settings.get("show_enhancement_notice"):
            return None
        
        output_parts = []
        
        # Header
        output_parts.append(MessageFormatter.header("Prompt Enhanced", "ai"))
        
        # Basic notice
        if self.settings.get("show_enhancement_details"):
            # Detailed view
            items = [
                f"Type detected: {result.prompt_type.value.replace('_', ' ').title()}",
                f"Confidence: {result.confidence:.0%}",
                f"Rules applied: {len(result.rules_applied)}",
                f"Length change: {len(original)} → {len(result.enhanced_prompt)} chars"
            ]
            
            # Add rules if not too many
            if len(result.rules_applied) <= 5:
                items.append("Applied: " + ", ".join(result.rules_applied))
            
            output_parts.append(MessageFormatter.section(
                "Enhancement Details",
                items,
                "info"
            ))
            
            # Add patterns if any
            if result.patterns_matched:
                output_parts.append(MessageFormatter.section(
                    "Patterns Recognized",
                    result.patterns_matched[:5],  # Limit to 5
                    "pattern"
                ))
        else:
            # Simple notice
            items = [
                f"Your prompt has been enhanced for clarity and effectiveness ({result.prompt_type.value})",
                f"To bypass enhancement, prefix with 'raw:' or 'exact:'"
            ]
            output_parts.append(MessageFormatter.section(
                "Notice",
                items,
                "info"
            ))
        
        # Add tip based on confidence
        if result.confidence < 0.7:
            output_parts.append(MessageFormatter.section(
                "Tip",
                ["Consider adding more details to your request for better results"],
                "tip"
            ))
        
        output_parts.append(MessageFormatter.footer())
        
        return "\n".join(output_parts)


def create_default_settings():
    """Create default settings file if it doesn't exist"""
    settings_path = Path(__file__).parent / "prompt-enhancement-settings.json"
    if not settings_path.exists():
        default_settings = {
            "enabled": True,
            "enhancement_level": "moderate",
            "show_enhancement_notice": True,
            "show_enhancement_details": False,
            "bypass_prefixes": ["raw:", "exact:", "no-enhance:"],
            "always_enhance_types": ["code_generation", "code_review"],
            "never_enhance_types": [],
            "log_enhancements": True,
            "max_prompt_length": 10000,
            "enhancement_thresholds": {
                "minimal": {
                    "min_word_count": 5,
                    "add_context": False,
                    "inject_rules": "essential"
                },
                "moderate": {
                    "min_word_count": 3,
                    "add_context": True,
                    "inject_rules": "relevant"
                },
                "aggressive": {
                    "min_word_count": 1,
                    "add_context": True,
                    "inject_rules": "comprehensive"
                }
            }
        }
        
        with open(settings_path, 'w') as f:
            json.dump(default_settings, f, indent=2)
        
        print(f"Created default settings at: {settings_path}")


if __name__ == "__main__":
    # Check if running with --init flag
    if len(sys.argv) > 1 and sys.argv[1] == "--init":
        create_default_settings()
    else:
        hook = PromptEnhancementHook()
        hook.run()