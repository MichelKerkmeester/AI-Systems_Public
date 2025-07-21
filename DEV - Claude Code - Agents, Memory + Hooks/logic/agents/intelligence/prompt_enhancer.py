"""
PromptEnhancer: Two-pass prompt enhancement system for Claude-Organizer.

This module implements a sophisticated prompt enhancement system that:
1. Applies general best practices for clarity and effectiveness
2. Injects project-specific rules from CLAUDE.md
3. Analyzes context to determine prompt type and requirements
4. Integrates with pattern libraries for consistency

The two-pass system ensures both general quality and project-specific compliance.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum


class PromptType(Enum):
    """Types of prompts that require different enhancement strategies."""
    CODE_GENERATION = "code_generation"
    CODE_REVIEW = "code_review"
    DEBUGGING = "debugging"
    DOCUMENTATION = "documentation"
    SYSTEM_DESIGN = "system_design"
    TASK_PLANNING = "task_planning"
    GENERAL = "general"


@dataclass
class EnhancementResult:
    """Result of prompt enhancement with metadata."""
    enhanced_prompt: str
    prompt_type: PromptType
    rules_applied: List[str]
    patterns_matched: List[str]
    confidence: float


class PromptEnhancer:
    """
    Two-pass prompt enhancement system that applies best practices
    and injects project-specific rules from CLAUDE.md.
    """
    
    def __init__(self, claude_md_path: Optional[Path] = None):
        """
        Initialize the PromptEnhancer with CLAUDE.md rules and pattern library.
        
        Args:
            claude_md_path: Path to CLAUDE.md file. Defaults to project root.
        """
        self.project_root = Path(__file__).parent.parent.parent.parent.parent
        self.claude_md_path = claude_md_path or self.project_root / "CLAUDE.md"
        self.knowledge_path = self.project_root / ".claude" / "knowledge"
        
        # Load project rules and patterns
        self.claude_md_rules = self.load_claude_md()
        self.patterns = self.load_patterns()
        self.constraints = self.load_constraints()
        
        # Initialize enhancement templates
        self._init_enhancement_templates()
    
    def enhance_prompt(self, original_prompt: str) -> EnhancementResult:
        """
        Main enhancement method - applies two-pass enhancement.
        
        Args:
            original_prompt: The original user prompt
            
        Returns:
            EnhancementResult with enhanced prompt and metadata
        """
        # Analyze context to determine prompt type
        prompt_type, context_info = self.analyze_context(original_prompt)
        
        # Pass 1: Apply general best practices
        enhanced_prompt, best_practices_applied = self.apply_best_practices(
            original_prompt, prompt_type
        )
        
        # Pass 2: Inject project-specific rules
        final_prompt, rules_applied = self.inject_claude_md_rules(
            enhanced_prompt, prompt_type, context_info
        )
        
        # Match relevant patterns
        patterns_matched = self._match_patterns(original_prompt)
        
        # Calculate confidence based on rules applied and pattern matches
        confidence = self._calculate_confidence(
            best_practices_applied, rules_applied, patterns_matched
        )
        
        return EnhancementResult(
            enhanced_prompt=final_prompt,
            prompt_type=prompt_type,
            rules_applied=best_practices_applied + rules_applied,
            patterns_matched=patterns_matched,
            confidence=confidence
        )
    
    def apply_best_practices(self, prompt: str, prompt_type: PromptType) -> Tuple[str, List[str]]:
        """
        Pass 1 - Apply general prompt engineering best practices.
        
        Args:
            prompt: The original prompt
            prompt_type: Detected type of prompt
            
        Returns:
            Tuple of (enhanced_prompt, applied_practices)
        """
        applied_practices = []
        enhanced_prompt = prompt
        
        # Add clarity if prompt is too vague
        if len(prompt.split()) < 10:
            enhanced_prompt = self._add_clarity(enhanced_prompt)
            applied_practices.append("clarity_enhancement")
        
        # Add context for code-related prompts
        if prompt_type in [PromptType.CODE_GENERATION, PromptType.CODE_REVIEW, PromptType.DEBUGGING]:
            enhanced_prompt = self._add_code_context(enhanced_prompt)
            applied_practices.append("code_context_addition")
        
        # Structure complex prompts
        if len(prompt.split('\n')) > 5 or len(prompt.split()) > 50:
            enhanced_prompt = self._structure_complex_prompt(enhanced_prompt)
            applied_practices.append("complex_structure")
        
        # Add output format specification if missing
        if not self._has_output_specification(enhanced_prompt):
            enhanced_prompt = self._add_output_specification(enhanced_prompt, prompt_type)
            applied_practices.append("output_specification")
        
        # Add constraints reminder for system changes
        if self._is_system_change(enhanced_prompt):
            enhanced_prompt = self._add_constraints_reminder(enhanced_prompt)
            applied_practices.append("constraints_reminder")
        
        return enhanced_prompt, applied_practices
    
    def inject_claude_md_rules(self, prompt: str, prompt_type: PromptType, 
                               context_info: Dict[str, Any]) -> Tuple[str, List[str]]:
        """
        Pass 2 - Inject project-specific rules from CLAUDE.md.
        
        Args:
            prompt: The best-practices-enhanced prompt
            prompt_type: Detected type of prompt
            context_info: Additional context information
            
        Returns:
            Tuple of (enhanced_prompt, injected_rules)
        """
        injected_rules = []
        enhanced_prompt = prompt
        
        # Core principles injection
        if prompt_type == PromptType.CODE_GENERATION:
            enhanced_prompt = self._inject_coding_principles(enhanced_prompt)
            injected_rules.append("core_coding_principles")
        
        # Technical constraints injection
        if self._needs_technical_constraints(prompt):
            enhanced_prompt = self._inject_technical_constraints(enhanced_prompt)
            injected_rules.append("technical_constraints")
        
        # Platform limits reminder
        if "webflow" in prompt.lower() or "performance" in prompt.lower():
            enhanced_prompt = self._inject_platform_limits(enhanced_prompt)
            injected_rules.append("platform_limits")
        
        # Task management rules
        if self._is_task_related(prompt):
            enhanced_prompt = self._inject_task_rules(enhanced_prompt)
            injected_rules.append("task_management")
        
        # Automation awareness
        if self._mentions_commands(prompt):
            enhanced_prompt = self._inject_automation_info(enhanced_prompt)
            injected_rules.append("automation_awareness")
        
        # Production checklist for deployment
        if self._is_deployment_related(prompt):
            enhanced_prompt = self._inject_production_checklist(enhanced_prompt)
            injected_rules.append("production_checklist")
        
        return enhanced_prompt, injected_rules
    
    def load_claude_md(self) -> Dict[str, Any]:
        """
        Parse and load rules from CLAUDE.md.
        
        Returns:
            Dictionary of parsed rules and constraints
        """
        rules = {
            "core_principles": [],
            "technical_constraints": {},
            "platform_limits": {},
            "task_management": {},
            "automation": {},
            "production_checklist": []
        }
        
        try:
            with open(self.claude_md_path, 'r') as f:
                content = f.read()
                
            # Extract core principles
            principles_match = re.search(
                r'### Development Philosophy\n(.*?)###', 
                content, re.DOTALL
            )
            if principles_match:
                rules["core_principles"] = [
                    line.strip() for line in principles_match.group(1).split('\n')
                    if line.strip() and line.strip().startswith(('1.', '2.', '3.', '4.'))
                ]
            
            # Extract technical constraints table
            constraints_match = re.search(
                r'\| Category \| ❌ Never \| ✅ Always \|(.*?)\*\*Platform Limits',
                content, re.DOTALL
            )
            if constraints_match:
                for line in constraints_match.group(1).split('\n'):
                    if '|' in line and 'Category' not in line and '---' not in line:
                        parts = [p.strip() for p in line.split('|') if p.strip()]
                        if len(parts) >= 3:
                            rules["technical_constraints"][parts[0]] = {
                                "never": parts[1],
                                "always": parts[2]
                            }
            
            # Extract platform limits
            limits_match = re.search(
                r'\*\*Platform Limits:\*\* (.*?)$',
                content, re.MULTILINE
            )
            if limits_match:
                for limit in limits_match.group(1).split('|'):
                    if '<' in limit:
                        key, value = limit.strip().split('<')
                        rules["platform_limits"][key.strip()] = value.strip()
            
            # Extract production checklist
            checklist_match = re.search(
                r'### Production Checklist\n(.*?)---',
                content, re.DOTALL
            )
            if checklist_match:
                rules["production_checklist"] = [
                    line.strip()[4:] for line in checklist_match.group(1).split('\n')
                    if line.strip().startswith('- [ ]')
                ]
                
        except Exception as e:
            print(f"Warning: Could not fully parse CLAUDE.md: {e}")
            
        return rules
    
    def load_patterns(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load patterns from patterns.json."""
        patterns_file = self.knowledge_path / "patterns.json"
        if patterns_file.exists():
            with open(patterns_file, 'r') as f:
                return json.load(f)
        return {}
    
    def load_constraints(self) -> Dict[str, Any]:
        """Load constraints from constraints.json."""
        constraints_file = self.knowledge_path / "constraints.json"
        if constraints_file.exists():
            with open(constraints_file, 'r') as f:
                return json.load(f)
        return {}
    
    def analyze_context(self, prompt: str) -> Tuple[PromptType, Dict[str, Any]]:
        """
        Determine prompt type and extract context information.
        
        Args:
            prompt: The original prompt
            
        Returns:
            Tuple of (prompt_type, context_info)
        """
        prompt_lower = prompt.lower()
        context_info = {
            "mentions_files": bool(re.search(r'\.(js|css|html|py|md)', prompt_lower)),
            "mentions_webflow": "webflow" in prompt_lower,
            "mentions_testing": any(word in prompt_lower for word in ["test", "spec", "verify"]),
            "mentions_performance": any(word in prompt_lower for word in ["performance", "optimize", "speed"]),
            "line_count": len(prompt.split('\n')),
            "word_count": len(prompt.split())
        }
        
        # Determine prompt type based on keywords and patterns
        if any(keyword in prompt_lower for keyword in ["generate", "create", "implement", "build", "add", "write", "develop", "make"]):
            if any(term in prompt_lower for term in ["code", "component", "function", "class", "module", "feature", "service", "api", "button", "form", "page", "authentication", "auth", "login", "system", "functionality", "integration"]) or context_info["mentions_files"]:
                return PromptType.CODE_GENERATION, context_info
                
        if any(keyword in prompt_lower for keyword in ["review", "check", "audit", "analyze"]):
            if "code" in prompt_lower or context_info["mentions_files"]:
                return PromptType.CODE_REVIEW, context_info
                
        if any(keyword in prompt_lower for keyword in ["debug", "fix", "error", "issue", "problem", "bug", "broken", "not working"]):
            return PromptType.DEBUGGING, context_info
            
        if any(keyword in prompt_lower for keyword in ["document", "explain", "describe", "write"]):
            if "documentation" in prompt_lower or "readme" in prompt_lower:
                return PromptType.DOCUMENTATION, context_info
                
        if any(keyword in prompt_lower for keyword in ["design", "architect", "structure", "plan"]):
            if "system" in prompt_lower or "component" in prompt_lower:
                return PromptType.SYSTEM_DESIGN, context_info
                
        if any(keyword in prompt_lower for keyword in ["task", "todo", "plan", "organize"]):
            return PromptType.TASK_PLANNING, context_info
            
        return PromptType.GENERAL, context_info
    
    # Helper methods for best practices
    def _add_clarity(self, prompt: str) -> str:
        """Add clarity to vague prompts."""
        return f"{prompt}\n\nPlease provide specific details about what you need, including any constraints or requirements."
    
    def _add_code_context(self, prompt: str) -> str:
        """Add code context for code-related prompts."""
        if "webflow" not in prompt.lower():
            return prompt
        return f"{prompt}\n\nContext: This is for a Webflow project (anobel.nl) with specific platform constraints."
    
    def _structure_complex_prompt(self, prompt: str) -> str:
        """Structure complex prompts with clear sections."""
        lines = prompt.split('\n')
        if lines[0].strip() and not lines[0].endswith(':'):
            structured = f"## Request\n{lines[0]}\n\n## Details\n"
            structured += '\n'.join(lines[1:])
            return structured
        return prompt
    
    def _has_output_specification(self, prompt: str) -> bool:
        """Check if prompt specifies desired output format."""
        output_keywords = ["format", "output", "return", "provide", "show", "display"]
        return any(keyword in prompt.lower() for keyword in output_keywords)
    
    def _add_output_specification(self, prompt: str, prompt_type: PromptType) -> str:
        """Add output specification based on prompt type."""
        specs = {
            PromptType.CODE_GENERATION: "\n\nPlease provide well-commented, production-ready code following the project's coding standards.",
            PromptType.CODE_REVIEW: "\n\nPlease provide a detailed review with specific suggestions for improvement.",
            PromptType.DEBUGGING: "\n\nPlease identify the issue and provide a clear fix with explanation.",
            PromptType.DOCUMENTATION: "\n\nPlease provide clear, well-structured documentation with examples where appropriate.",
            PromptType.SYSTEM_DESIGN: "\n\nPlease provide a detailed design with clear architecture and rationale.",
            PromptType.TASK_PLANNING: "\n\nPlease provide a structured task plan with clear steps and priorities.",
            PromptType.GENERAL: "\n\nPlease provide a clear and comprehensive response."
        }
        return prompt + specs.get(prompt_type, specs[PromptType.GENERAL])
    
    def _is_system_change(self, prompt: str) -> bool:
        """Check if prompt involves system changes."""
        system_keywords = ["refactor", "migrate", "update system", "change architecture", "modify structure"]
        return any(keyword in prompt.lower() for keyword in system_keywords)
    
    def _add_constraints_reminder(self, prompt: str) -> str:
        """Add reminder about system constraints."""
        return f"{prompt}\n\nReminder: Follow the project's technical constraints and create a spec folder for major changes."
    
    # Helper methods for CLAUDE.md rule injection
    def _inject_coding_principles(self, prompt: str) -> str:
        """Inject core coding principles."""
        principles = "\n".join([f"- {p}" for p in self.claude_md_rules["core_principles"]])
        return f"{prompt}\n\n## Project Coding Principles:\n{principles}"
    
    def _needs_technical_constraints(self, prompt: str) -> bool:
        """Check if prompt needs technical constraints."""
        return any(cat.lower() in prompt.lower() 
                  for cat in self.claude_md_rules["technical_constraints"].keys())
    
    def _inject_technical_constraints(self, prompt: str) -> str:
        """Inject relevant technical constraints."""
        constraints_text = "\n## Technical Constraints:\n"
        for category, rules in self.claude_md_rules["technical_constraints"].items():
            if category.lower() in prompt.lower():
                constraints_text += f"- {category}: Never {rules['never']}, Always {rules['always']}\n"
        return prompt + constraints_text
    
    def _inject_platform_limits(self, prompt: str) -> str:
        """Inject platform limits."""
        limits_text = "\n## Platform Limits:\n"
        for limit, value in self.claude_md_rules["platform_limits"].items():
            limits_text += f"- {limit}: < {value}\n"
        return prompt + limits_text
    
    def _is_task_related(self, prompt: str) -> bool:
        """Check if prompt is task-related."""
        task_keywords = ["task", "todo", "ticket", "issue", "feature", "bug"]
        return any(keyword in prompt.lower() for keyword in task_keywords)
    
    def _inject_task_rules(self, prompt: str) -> str:
        """Inject task management rules."""
        return f"{prompt}\n\n## Task Management:\n- Create spec folder for major changes\n- Active task limit: 1\n- Task flow: specs → active → completed"
    
    def _mentions_commands(self, prompt: str) -> bool:
        """Check if prompt mentions system commands."""
        return bool(re.search(r'/\w+', prompt))
    
    def _inject_automation_info(self, prompt: str) -> str:
        """Inject automation awareness."""
        return f"{prompt}\n\n## Automation Info:\n- Most commands run automatically via hooks\n- Essential commands: /memory, /save, /logic\n- Check automation status: /logic hooks status"
    
    def _is_deployment_related(self, prompt: str) -> bool:
        """Check if prompt is deployment-related."""
        deploy_keywords = ["deploy", "production", "release", "publish", "launch"]
        return any(keyword in prompt.lower() for keyword in deploy_keywords)
    
    def _inject_production_checklist(self, prompt: str) -> str:
        """Inject production checklist."""
        checklist = "\n".join([f"- [ ] {item}" for item in self.claude_md_rules["production_checklist"]])
        return f"{prompt}\n\n## Production Checklist:\n{checklist}"
    
    # Pattern matching and confidence calculation
    def _match_patterns(self, prompt: str) -> List[str]:
        """Match prompt against known patterns."""
        matched_patterns = []
        
        for category, patterns in self.patterns.items():
            if isinstance(patterns, list):
                for pattern in patterns:
                    if isinstance(pattern, dict) and "pattern" in pattern:
                        if pattern["pattern"].lower() in prompt.lower():
                            matched_patterns.append(f"{category}:{pattern.get('name', pattern['pattern'])}")
                            
        return matched_patterns
    
    def _calculate_confidence(self, best_practices: List[str], 
                            rules: List[str], patterns: List[str]) -> float:
        """Calculate confidence score for enhancement."""
        # Base confidence
        confidence = 0.5
        
        # Add confidence for each enhancement applied
        confidence += len(best_practices) * 0.05
        confidence += len(rules) * 0.08
        confidence += len(patterns) * 0.03
        
        # Cap at 0.95
        return min(confidence, 0.95)
    
    def _init_enhancement_templates(self):
        """Initialize enhancement templates for different scenarios."""
        self.templates = {
            "webflow_code": {
                "prefix": "For this Webflow project (anobel.nl):",
                "suffix": "\nEnsure code follows Webflow best practices and platform limits."
            },
            "system_change": {
                "prefix": "For this system change:",
                "suffix": "\nRemember to create a spec folder with requirements, design, test plan, and rollback plan."
            },
            "performance": {
                "prefix": "For performance optimization:",
                "suffix": "\nConsider platform limits: JS <50KB, CSS <20KB, Load <3s"
            }
        }


# Convenience function for quick enhancement
def enhance_prompt(prompt: str, claude_md_path: Optional[Path] = None) -> str:
    """
    Quick function to enhance a prompt using default settings.
    
    Args:
        prompt: The prompt to enhance
        claude_md_path: Optional path to CLAUDE.md
        
    Returns:
        Enhanced prompt string
    """
    enhancer = PromptEnhancer(claude_md_path)
    result = enhancer.enhance_prompt(prompt)
    return result.enhanced_prompt