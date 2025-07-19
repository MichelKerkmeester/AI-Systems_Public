#!/usr/bin/env python3
"""
Active Memory Context Hook with Real Graphiti Integration
Queries and captures memories using Graphiti MCP server
"""

import sys
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List
from datetime import datetime

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase, UserPromptHook
from logic.hooks.memory.memory_capture_helper import MemoryCaptureHelper


class MemoryContextHook(UserPromptHook):
    """Memory context hook with real Graphiti MCP integration"""
    
    def __init__(self):
        super().__init__()
        self.memory_loaded = False
        self.session_memories = []  # Track memories from this session
        
        # Load automation settings
        settings_path = Path(__file__).parent.parent.parent / "logic" / "memory" / "settings.json"
        try:
            with open(settings_path) as f:
                self.memory_settings = json.load(f)
        except:
            self.memory_settings = {"automation_level": "semi"}
        
        # Expanded capture patterns
        self.capture_patterns = {
            # Critical patterns (always capture)
            "DECISION": r"decided to|will use|choosing|selected|going with",
            "SECURITY": r"security|auth|token|credential|password|encryption",
            "BREAKING": r"breaking change|migration|upgrade|deprecated",
            "RESOLVED": r"fixed|resolved|solution|workaround|solved",
            "PATTERN": r"pattern|convention|standard|always|never",
            
            # Enhanced patterns for better capture
            "ERROR_FIX": r"error.*fixed|resolved.*issue|bug.*solution|debugged",
            "OPTIMIZATION": r"optimized|improved.*performance|faster|reduced",
            "USER_FEEDBACK": r"user.*said|client.*wants|requirement|asked for",
            "CONFIG_CHANGE": r"configured|setting.*changed|updated.*config",
            "LEARNING": r"learned|discovered|found out|realized|understood",
            "BEST_PRACTICE": r"best practice|recommended|should.*always|avoid",
            "ARCHITECTURE": r"architecture|design.*decision|structure|refactor",
            "API_CHANGE": r"api.*changed|endpoint|interface.*modified",
            "DEPENDENCY": r"installed|upgraded.*package|dependency|library"
        }
        
    def extract_keywords(self, text: str, max_keywords: int = 5) -> List[str]:
        """Extract meaningful keywords from user input"""
        # Remove common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                     'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                     'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                     'could', 'should', 'may', 'might', 'must', 'can', 'how', 'what',
                     'when', 'where', 'why', 'which', 'who', 'whom', 'this', 'that',
                     'these', 'those', 'i', 'you', 'we', 'they', 'it', 'me', 'my',
                     'please', 'help', 'need', 'want', 'like', 'make', 'create'}
        
        # Extract words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter and prioritize
        keywords = []
        seen = set()
        for word in words:
            if word not in stop_words and len(word) > 2 and word not in seen:
                keywords.append(word)
                seen.add(word)
        
        # Return most significant keywords
        return keywords[:max_keywords]
    
    def detect_patterns(self, text: str) -> List[Tuple[str, str]]:
        """Detect capture patterns in text"""
        detected = []
        
        # Check automation level
        level = self.memory_settings.get("automation_level", "semi")
        if level == "off":
            return []
        
        # Critical patterns always captured in semi/full mode
        critical_patterns = ["DECISION", "SECURITY", "BREAKING", "RESOLVED", "PATTERN"]
        
        for pattern_type, pattern in self.capture_patterns.items():
            # Skip non-critical patterns in manual mode
            if level == "manual" and pattern_type not in critical_patterns:
                continue
                
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Get context around the match (50 chars before and after)
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 100)
                context = text[start:end].strip()
                
                detected.append((pattern_type, context))
        
        return detected
    
    def format_memory_capture_prompt(self, patterns: List[Tuple[str, str]]) -> str:
        """Format a prompt that encourages Claude to capture memories"""
        if not patterns:
            return None
            
        # Create episodes from detected patterns
        helper = MemoryCaptureHelper()
        episodes = []
        
        for pattern_type, context in patterns:
            # Create a descriptive name from context
            name = context[:50].strip()
            if '.' in name:
                name = name.split('.')[0]
            elif ':' in name:
                name = name.split(':')[1].strip()
                
            episode = helper.create_episode(
                name=name,
                content=context,
                pattern_type=pattern_type,
                context="user_prompt"
            )
            episodes.append(episode)
        
        # Format capture instructions
        return helper.format_capture_instruction(episodes)
    
    def format_memory_context(self, keywords: List[str], captured: int = 0) -> str:
        """Format memory context display"""
        output = []
        
        # Only show full context on first load
        if not self.memory_loaded:
            output.append("\n" + "="*50)
            output.append("🧠 MEMORY CONTEXT")
            output.append("="*50)
            output.append(f"\n📊 Automation: {self.memory_settings.get('automation_level', 'semi')}")
            
            if keywords:
                output.append(f"🔍 Keywords: {', '.join(keywords[:3])}")
            
            output.append("\n💡 Commands:")
            output.append("   • `/memory search <query>` - Search memories")
            output.append("   • `/memory auto [level]` - Change automation")
            
            output.append("\n" + "="*50 + "\n")
        
        # Always show captures if any
        elif captured > 0:
            output.append(f"\n💾 Auto-captured {captured} memory patterns")
        
        return "\n".join(output) if output else None
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook input with pattern detection"""
        user_input = hook_input.get('user_input', '')
        
        # Skip for certain commands
        skip_patterns = ['/memory', '/test', '/workflow', '/mode', '/pr', '/security', '/save', '/logic']
        if any(user_input.strip().startswith(cmd) for cmd in skip_patterns):
            return 0, None
        
        try:
            # Extract keywords from user input
            keywords = self.extract_keywords(user_input)
            
            # Detect patterns for automatic capture
            detected_patterns = self.detect_patterns(user_input)
            
            # Track detected patterns
            if detected_patterns:
                self.session_memories.extend(detected_patterns)
                
                # In full automation mode, prompt Claude to capture
                if self.memory_settings.get("automation_level") == "full":
                    capture_prompt = self.format_memory_capture_prompt(detected_patterns)
                    if capture_prompt:
                        return 0, capture_prompt
                # In semi mode, only prompt for critical patterns
                elif self.memory_settings.get("automation_level") == "semi":
                    critical_patterns = [p for p in detected_patterns if p[0] in 
                                       ["DECISION", "SECURITY", "BREAKING", "RESOLVED", "PATTERN"]]
                    if critical_patterns:
                        capture_prompt = self.format_memory_capture_prompt(critical_patterns)
                        if capture_prompt:
                            return 0, capture_prompt
            
            # Show standard context on first load
            output = self.format_memory_context(keywords, len(detected_patterns))
            
            # Mark as loaded after first display
            if output and not self.memory_loaded:
                self.memory_loaded = True
            
            return 0, output
                
        except Exception as e:
            # Silently fail - don't disrupt the user experience
            self.logger.error(f"Memory context error: {e}")
        
        return 0, None


# Main entry point
if __name__ == "__main__":
    hook = MemoryContextHook()
    hook.run()