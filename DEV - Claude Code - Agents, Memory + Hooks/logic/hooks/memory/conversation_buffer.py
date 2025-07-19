#!/usr/bin/env python3
"""
Conversation Buffer for Continuous Memory Analysis
Analyzes conversation exchanges and captures significant patterns
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple
from .memory_capture_helper import MemoryCaptureHelper


class ConversationBuffer:
    """Buffer and analyze conversation exchanges for memory capture"""
    
    def __init__(self, threshold: int = 5, settings_path: Path = None):
        """
        Initialize conversation buffer
        
        Args:
            threshold: Number of exchanges before analysis triggers
            settings_path: Path to memory settings
        """
        self.threshold = threshold
        self.buffer = []
        self.analyzed_count = 0
        
        # Load settings
        if settings_path and settings_path.exists():
            with open(settings_path) as f:
                self.settings = json.load(f)
        else:
            self.settings = {"automation_level": "semi"}
            
        # Analysis patterns
        self.analysis_patterns = {
            # Learning patterns
            "LEARNING": r"(now i understand|makes sense|got it|i see|learned that|discovered)",
            
            # Problem solving
            "PROBLEM_SOLVED": r"(that fixed it|works now|solved|resolved the issue|found the problem)",
            
            # Decision rationale
            "RATIONALE": r"(because|reason is|this way because|chose.*because|decided.*since)",
            
            # Best practices
            "BEST_PRACTICE": r"(should always|never.*should|best to|recommended approach|proper way)",
            
            # Workarounds
            "WORKAROUND": r"(workaround|alternative approach|instead of|can\'t.*so.*instead)",
            
            # Configuration
            "CONFIG": r"(set.*to|configure.*as|change.*setting|update.*config)",
            
            # Performance insights
            "PERFORMANCE": r"(faster|slower|performance|optimiz|bottleneck|improve.*speed)",
            
            # Integration patterns
            "INTEGRATION": r"(works with|compatible|integrates|connects to|interfaces with)"
        }
        
        self.helper = MemoryCaptureHelper()
        
    def add_exchange(self, user_msg: str, assistant_msg: str) -> List[Dict[str, Any]]:
        """
        Add an exchange to the buffer and analyze if threshold met
        
        Args:
            user_msg: User's message
            assistant_msg: Assistant's response
            
        Returns:
            List of memory episodes to capture (empty if threshold not met)
        """
        # Add to buffer
        self.buffer.append({
            "user": user_msg,
            "assistant": assistant_msg,
            "timestamp": datetime.now().isoformat()
        })
        
        # Check if we should analyze
        if len(self.buffer) >= self.threshold:
            episodes = self.analyze_and_clear()
            return episodes
            
        return []
        
    def analyze_and_clear(self) -> List[Dict[str, Any]]:
        """
        Analyze buffered conversation and extract memories
        
        Returns:
            List of memory episodes to capture
        """
        if not self.buffer:
            return []
            
        episodes = []
        
        # Analyze each exchange
        for exchange in self.buffer:
            # Combine user and assistant messages for context
            full_context = f"User: {exchange['user']}\\nAssistant: {exchange['assistant']}"
            
            # Check for patterns
            for pattern_type, pattern in self.analysis_patterns.items():
                matches = re.finditer(pattern, full_context, re.IGNORECASE)
                for match in matches:
                    # Get surrounding context
                    start = max(0, match.start() - 100)
                    end = min(len(full_context), match.end() + 100)
                    context = full_context[start:end].strip()
                    
                    # Check if we should capture based on automation level
                    if self.helper.should_capture(pattern_type, self.settings.get("automation_level")):
                        # Extract a meaningful name
                        name = self._extract_name(context, pattern_type)
                        
                        episode = self.helper.create_episode(
                            name=name,
                            content=context,
                            pattern_type=pattern_type,
                            context="conversation_buffer"
                        )
                        episodes.append(episode)
        
        # Analyze cross-exchange patterns
        cross_episodes = self._analyze_cross_exchanges()
        episodes.extend(cross_episodes)
        
        # Clear buffer after analysis
        self.analyzed_count += len(self.buffer)
        self.buffer = []
        
        return episodes
        
    def _extract_name(self, context: str, pattern_type: str) -> str:
        """Extract a meaningful name from context"""
        # Clean up context
        context = context.replace("\\n", " ").strip()
        
        # Try to extract key phrases based on pattern type
        if pattern_type == "PROBLEM_SOLVED":
            # Look for what was fixed
            if "fixed" in context.lower():
                parts = context.lower().split("fixed")
                if len(parts) > 1:
                    return parts[1].strip()[:50]
                    
        elif pattern_type == "LEARNING":
            # Look for what was learned
            if "learned that" in context.lower():
                parts = context.lower().split("learned that")
                if len(parts) > 1:
                    return parts[1].strip()[:50]
                    
        elif pattern_type == "CONFIG":
            # Look for what was configured
            if "set" in context.lower():
                parts = context.lower().split("set")
                if len(parts) > 1:
                    return f"Set {parts[1].strip()[:40]}"
        
        # Default: use first meaningful phrase
        sentences = context.split(".")
        for sentence in sentences:
            if len(sentence.strip()) > 10:
                return sentence.strip()[:50]
                
        return context[:50]
        
    def _analyze_cross_exchanges(self) -> List[Dict[str, Any]]:
        """Analyze patterns across multiple exchanges"""
        episodes = []
        
        if len(self.buffer) < 2:
            return episodes
            
        # Look for iterative problem solving
        problem_mentions = 0
        solution_found = False
        problem_context = []
        
        for exchange in self.buffer:
            full_text = f"{exchange['user']} {exchange['assistant']}".lower()
            
            if any(word in full_text for word in ["error", "issue", "problem", "failing", "broken"]):
                problem_mentions += 1
                problem_context.append(full_text[:100])
                
            if any(word in full_text for word in ["fixed", "solved", "works now", "resolved"]):
                solution_found = True
                
        # If we saw a problem evolve to a solution
        if problem_mentions >= 2 and solution_found:
            episode = self.helper.create_episode(
                name="Iterative problem solving process",
                content=f"Problem solving across {len(self.buffer)} exchanges. Initial issues: {'; '.join(problem_context[:2])}",
                pattern_type="PROBLEM_SOLVED",
                context="conversation_analysis"
            )
            episodes.append(episode)
            
        return episodes
        
    def get_stats(self) -> Dict[str, Any]:
        """Get buffer statistics"""
        return {
            "current_buffer_size": len(self.buffer),
            "threshold": self.threshold,
            "total_analyzed": self.analyzed_count,
            "automation_level": self.settings.get("automation_level"),
            "pending_analysis": len(self.buffer) > 0
        }
        
    def force_analyze(self) -> List[Dict[str, Any]]:
        """Force analysis regardless of threshold"""
        if not self.buffer:
            return []
            
        return self.analyze_and_clear()


# Example usage
if __name__ == "__main__":
    buffer = ConversationBuffer(threshold=3)
    
    # Simulate conversation
    exchanges = [
        ("How do I fix the authentication error?", 
         "The authentication error is likely due to expired JWT tokens. Let me check the auth configuration."),
        ("I see the tokens expire after 1 hour", 
         "That's quite short. I recommend extending the token lifetime to 24 hours and implementing refresh tokens."),
        ("How do I implement refresh tokens?",
         "I'll add a refresh token mechanism. This involves creating a new endpoint and updating the auth middleware. That fixed it - the authentication now works properly with automatic token refresh.")
    ]
    
    for user, assistant in exchanges:
        episodes = buffer.add_exchange(user, assistant)
        if episodes:
            print(f"Captured {len(episodes)} memories!")
            for ep in episodes:
                print(f"  - {ep['name']}")
                
    print(f"\nBuffer stats: {buffer.get_stats()}")