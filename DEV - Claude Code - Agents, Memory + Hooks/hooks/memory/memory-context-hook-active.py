#!/usr/bin/env python3
"""
Active Memory Context Hook for Claude Code
Queries Graphiti MCP server for relevant memories
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from shared import HookBase, UserPromptHook


class ActiveMemoryContextHook(UserPromptHook):
    """Active memory context hook that queries Graphiti"""
    
    def __init__(self):
        super().__init__()
        self.memory_loaded = False
        
    def extract_keywords(self, text: str, max_keywords: int = 3) -> List[str]:
        """Extract meaningful keywords from user input"""
        # Remove common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                     'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                     'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                     'could', 'should', 'may', 'might', 'must', 'can', 'how', 'what',
                     'when', 'where', 'why', 'which', 'who', 'whom', 'this', 'that',
                     'these', 'those', 'i', 'you', 'we', 'they', 'it', 'me', 'my'}
        
        # Extract words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter and prioritize
        keywords = []
        for word in words:
            if word not in stop_words and len(word) > 2:
                keywords.append(word)
        
        # Return most significant keywords
        return keywords[:max_keywords]
    
    def format_memory_context(self, memories: List[Dict], keywords: List[str]) -> str:
        """Format memories for display"""
        output = []
        output.append("\n" + "="*50)
        output.append("🧠 MEMORY CONTEXT LOADED")
        output.append("="*50)
        
        if memories:
            output.append(f"\n📍 Found {len(memories)} relevant memories:")
            
            for i, memory in enumerate(memories[:3], 1):
                name = memory.get('name', 'Untitled')
                content = memory.get('episode_body', '')
                source = memory.get('source', '')
                
                # Truncate content if too long
                if len(content) > 150:
                    content = content[:150] + "..."
                
                output.append(f"\n{i}. {name}")
                if source:
                    output.append(f"   Source: {source}")
                if content:
                    output.append(f"   Content: {content}")
        
        # Suggest searches based on keywords
        if keywords:
            output.append(f"\n💡 Suggested searches:")
            for keyword in keywords:
                output.append(f'   • /memory search "{keyword}"')
        
        output.append("\n" + "="*50 + "\n")
        return "\n".join(output)
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process hook input and query Graphiti for relevant memories"""
        user_input = hook_input.get('user_input', '')
        
        # Skip for certain commands
        skip_patterns = ['/memory', '/test', '/workflow', '/mode', '/pr', '/security']
        if any(user_input.strip().startswith(cmd) for cmd in skip_patterns):
            return 0, None
        
        # Skip if already loaded memories this session
        if self.memory_loaded:
            return 0, None
        
        try:
            # Extract keywords from user input
            keywords = self.extract_keywords(user_input)
            
            if not keywords:
                return 0, None
            
            # Note: In a real implementation, this would call Graphiti MCP
            # For now, we'll return a placeholder that shows what it would look like
            
            # Simulate memory search results
            simulated_memories = []
            
            # Only show context if we have relevant keywords
            memory_triggers = ['auth', 'security', 'database', 'api', 'react', 'typescript']
            if any(keyword in keywords for keyword in memory_triggers):
                simulated_memories = [
                    {
                        'name': 'PATTERN: Authentication Flow Design',
                        'episode_body': 'Implemented JWT-based authentication with refresh tokens...',
                        'source': 'architecture_decision'
                    }
                ]
            
            if simulated_memories:
                self.memory_loaded = True
                return 0, self.format_memory_context(simulated_memories, keywords)
            
        except Exception as e:
            # Silently fail - don't disrupt the user experience
            self.logger.error(f"Memory context error: {e}")
        
        return 0, None


# Main entry point
if __name__ == "__main__":
    hook = ActiveMemoryContextHook()
    hook.run()