"""Pattern Library for Claude-Organizer Prompt Enhancement

This module provides pattern recognition and enhancement templates for common
user requests. It includes learning capabilities to track successful patterns
and improve over time.
"""

import json
import os
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from pathlib import Path


class PatternLibrary:
    """Manages prompt patterns and enhancement templates"""
    
    def __init__(self, learning_file: Optional[Path] = None):
        """Initialize the pattern library
        
        Args:
            learning_file: Path to store learning data (pattern success metrics)
        """
        self.learning_file = learning_file or Path.home() / ".claude" / "pattern_learning.json"
        self.patterns = self._initialize_patterns()
        self.learning_data = self._load_learning_data()
    
    def _initialize_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Initialize the pattern library with common request patterns"""
        return {
            # Vague Development Requests
            "vague_development": {
                "patterns": [
                    r"make it better",
                    r"improve the code",
                    r"fix the issues",
                    r"clean this up",
                    r"optimize performance",
                    r"refactor this"
                ],
                "enhancement_template": {
                    "clarifications": [
                        "What specific aspects should be improved?",
                        "Are there performance metrics to target?",
                        "Which code quality issues are most important?"
                    ],
                    "suggestions": [
                        "Code organization and structure",
                        "Performance optimization (load time, memory usage)",
                        "Error handling and edge cases",
                        "Code readability and documentation",
                        "Security vulnerabilities",
                        "Test coverage"
                    ],
                    "automated_analysis": [
                        "Run code quality checks",
                        "Identify potential bugs",
                        "Check for security issues",
                        "Analyze performance bottlenecks"
                    ]
                }
            },
            
            # Complex Multi-Step Tasks
            "complex_task": {
                "patterns": [
                    r"implement .+ with .+ and .+",
                    r"create a system that",
                    r"build .+ that integrates",
                    r"set up .+ including",
                    r"develop a complete"
                ],
                "enhancement_template": {
                    "task_breakdown": {
                        "planning": "Create detailed specification",
                        "architecture": "Design system architecture",
                        "implementation": "Build core functionality",
                        "integration": "Connect components",
                        "testing": "Verify functionality",
                        "documentation": "Document usage"
                    },
                    "coordination_needed": [
                        "Multiple file changes",
                        "Cross-system integration",
                        "External service setup",
                        "Database schema changes"
                    ],
                    "risk_assessment": [
                        "Breaking changes",
                        "Performance impact",
                        "Security implications",
                        "Rollback strategy"
                    ]
                }
            },
            
            # Documentation Updates
            "documentation": {
                "patterns": [
                    r"update the docs",
                    r"document this",
                    r"add documentation for",
                    r"improve the readme",
                    r"explain how .+ works"
                ],
                "enhancement_template": {
                    "documentation_types": [
                        "API documentation",
                        "User guides",
                        "Code comments",
                        "Architecture diagrams",
                        "Examples and tutorials",
                        "Troubleshooting guides"
                    ],
                    "quality_checks": [
                        "Accuracy with current code",
                        "Completeness of coverage",
                        "Clarity for target audience",
                        "Proper formatting",
                        "Working examples"
                    ]
                }
            },
            
            # Bug Fixes
            "bug_fix": {
                "patterns": [
                    r"fix the bug",
                    r"something is broken",
                    r"not working properly",
                    r"getting an error",
                    r"crashes when",
                    r"fails to"
                ],
                "enhancement_template": {
                    "diagnostic_steps": [
                        "Reproduce the issue",
                        "Identify root cause",
                        "Check related systems",
                        "Review recent changes"
                    ],
                    "fix_verification": [
                        "Test the fix",
                        "Check for regressions",
                        "Verify edge cases",
                        "Update tests"
                    ],
                    "context_needed": [
                        "Error messages or logs",
                        "Steps to reproduce",
                        "Expected vs actual behavior",
                        "Environment details"
                    ]
                }
            },
            
            # Feature Additions
            "feature_addition": {
                "patterns": [
                    r"add .+ feature",
                    r"implement .+ functionality",
                    r"create a new .+",
                    r"add support for",
                    r"enable .+ capability"
                ],
                "enhancement_template": {
                    "planning_questions": [
                        "User stories and requirements",
                        "Integration with existing features",
                        "UI/UX considerations",
                        "Performance requirements",
                        "Security implications"
                    ],
                    "implementation_phases": [
                        "Design and specification",
                        "Core implementation",
                        "Integration points",
                        "Testing strategy",
                        "Documentation updates"
                    ]
                }
            },
            
            # Performance Optimizations
            "performance": {
                "patterns": [
                    r"make it faster",
                    r"optimize performance",
                    r"reduce load time",
                    r"improve efficiency",
                    r"speed up"
                ],
                "enhancement_template": {
                    "analysis_tools": [
                        "Profile current performance",
                        "Identify bottlenecks",
                        "Measure baseline metrics",
                        "Set performance targets"
                    ],
                    "optimization_strategies": [
                        "Algorithm improvements",
                        "Caching strategies",
                        "Database query optimization",
                        "Asset optimization",
                        "Code splitting",
                        "Lazy loading"
                    ],
                    "verification": [
                        "Before/after benchmarks",
                        "Load testing",
                        "Memory profiling",
                        "User experience metrics"
                    ]
                }
            }
        }
    
    def _load_learning_data(self) -> Dict[str, Any]:
        """Load learning data from file"""
        if self.learning_file.exists():
            try:
                with open(self.learning_file, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "pattern_success": {},
            "enhancement_history": [],
            "user_preferences": {}
        }
    
    def _save_learning_data(self):
        """Save learning data to file"""
        self.learning_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.learning_file, 'w') as f:
            json.dump(self.learning_data, f, indent=2)
    
    def match_pattern(self, prompt: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Match a prompt against known patterns
        
        Args:
            prompt: User's input prompt
            
        Returns:
            Tuple of (pattern_type, enhancement_template) or None
        """
        import re
        
        prompt_lower = prompt.lower()
        
        # Check each pattern category
        for pattern_type, pattern_data in self.patterns.items():
            for pattern in pattern_data["patterns"]:
                if re.search(pattern, prompt_lower):
                    return pattern_type, pattern_data["enhancement_template"]
        
        return None
    
    def enhance_prompt(self, prompt: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Enhance a user prompt with clarifications and structure
        
        Args:
            prompt: Original user prompt
            context: Optional context (current file, project state, etc.)
            
        Returns:
            Enhanced prompt with suggestions and structure
        """
        match_result = self.match_pattern(prompt)
        
        if not match_result:
            return {
                "original": prompt,
                "enhanced": prompt,
                "pattern_matched": None,
                "enhancements": []
            }
        
        pattern_type, template = match_result
        
        # Build enhanced prompt
        enhancements = []
        
        # Add clarification questions if vague
        if pattern_type == "vague_development":
            enhancements.append({
                "type": "clarification",
                "content": template["clarifications"],
                "suggestions": template["suggestions"]
            })
        
        # Add task breakdown for complex tasks
        elif pattern_type == "complex_task":
            enhancements.append({
                "type": "task_breakdown",
                "content": template["task_breakdown"],
                "coordination": template["coordination_needed"]
            })
        
        # Add diagnostic steps for bugs
        elif pattern_type == "bug_fix":
            enhancements.append({
                "type": "diagnostic",
                "content": template["diagnostic_steps"],
                "context_needed": template["context_needed"]
            })
        
        # Build enhanced prompt text
        enhanced_parts = [prompt]
        
        for enhancement in enhancements:
            if enhancement["type"] == "clarification":
                enhanced_parts.append("\n\nTo better assist you, consider:")
                for question in enhancement["content"]:
                    enhanced_parts.append(f"- {question}")
            
            elif enhancement["type"] == "task_breakdown":
                enhanced_parts.append("\n\nThis task will involve:")
                for phase, description in enhancement["content"].items():
                    enhanced_parts.append(f"- {phase.title()}: {description}")
            
            elif enhancement["type"] == "diagnostic":
                enhanced_parts.append("\n\nDiagnostic approach:")
                for step in enhancement["content"]:
                    enhanced_parts.append(f"- {step}")
        
        return {
            "original": prompt,
            "enhanced": "\n".join(enhanced_parts),
            "pattern_matched": pattern_type,
            "enhancements": enhancements,
            "template": template
        }
    
    def record_success(self, pattern_type: str, enhancement_used: Dict[str, Any], success: bool):
        """Record the success of a pattern enhancement
        
        Args:
            pattern_type: Type of pattern that was matched
            enhancement_used: The enhancement that was applied
            success: Whether the enhancement was successful
        """
        # Update pattern success metrics
        if pattern_type not in self.learning_data["pattern_success"]:
            self.learning_data["pattern_success"][pattern_type] = {
                "total": 0,
                "successful": 0
            }
        
        self.learning_data["pattern_success"][pattern_type]["total"] += 1
        if success:
            self.learning_data["pattern_success"][pattern_type]["successful"] += 1
        
        # Record in history
        self.learning_data["enhancement_history"].append({
            "timestamp": datetime.now().isoformat(),
            "pattern_type": pattern_type,
            "success": success,
            "enhancement_summary": str(enhancement_used)[:200]  # Truncate for storage
        })
        
        # Keep only last 1000 history entries
        if len(self.learning_data["enhancement_history"]) > 1000:
            self.learning_data["enhancement_history"] = self.learning_data["enhancement_history"][-1000:]
        
        self._save_learning_data()
    
    def get_success_rate(self, pattern_type: str) -> float:
        """Get the success rate for a pattern type
        
        Args:
            pattern_type: Type of pattern
            
        Returns:
            Success rate as a float between 0 and 1
        """
        if pattern_type not in self.learning_data["pattern_success"]:
            return 0.0
        
        data = self.learning_data["pattern_success"][pattern_type]
        if data["total"] == 0:
            return 0.0
        
        return data["successful"] / data["total"]
    
    def add_custom_pattern(self, pattern_type: str, patterns: List[str], 
                          enhancement_template: Dict[str, Any]):
        """Add a custom pattern to the library
        
        Args:
            pattern_type: Name for the pattern type
            patterns: List of regex patterns to match
            enhancement_template: Template for enhancing matched prompts
        """
        self.patterns[pattern_type] = {
            "patterns": patterns,
            "enhancement_template": enhancement_template
        }
    
    def get_pattern_stats(self) -> Dict[str, Any]:
        """Get statistics about pattern usage and success
        
        Returns:
            Dictionary with pattern statistics
        """
        stats = {
            "total_patterns": len(self.patterns),
            "pattern_types": list(self.patterns.keys()),
            "success_rates": {},
            "total_enhancements": sum(
                data["total"] 
                for data in self.learning_data["pattern_success"].values()
            )
        }
        
        for pattern_type in self.patterns:
            stats["success_rates"][pattern_type] = self.get_success_rate(pattern_type)
        
        return stats


# Example usage and testing
if __name__ == "__main__":
    # Initialize the library
    library = PatternLibrary()
    
    # Test various prompts
    test_prompts = [
        "make it better",
        "fix the bug in the login system",
        "create a system that handles user authentication with OAuth and email verification",
        "optimize performance of the dashboard",
        "add documentation for the API endpoints",
        "implement user profile feature"
    ]
    
    print("Pattern Library Test Results:\n")
    
    for prompt in test_prompts:
        print(f"Original: {prompt}")
        result = library.enhance_prompt(prompt)
        print(f"Pattern Matched: {result['pattern_matched']}")
        print(f"Enhanced:\n{result['enhanced']}\n")
        print("-" * 80 + "\n")
    
    # Show statistics
    stats = library.get_pattern_stats()
    print("Pattern Library Statistics:")
    print(json.dumps(stats, indent=2))