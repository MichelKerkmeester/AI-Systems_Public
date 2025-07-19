#!/usr/bin/env python3
"""
Memory Capture Helper
Formats memory capture instructions for Claude Code to execute
"""

import json
from typing import Dict, Any, List
from datetime import datetime


class MemoryCaptureHelper:
    """Helper class for formatting memory capture instructions"""
    
    @staticmethod
    def format_capture_instruction(episodes: List[Dict[str, Any]]) -> str:
        """
        Format memory capture instructions that Claude can execute
        
        Args:
            episodes: List of episode dictionaries with required fields:
                - name: Short descriptive name
                - episode_body: Full content to capture
                - source: Source identifier (e.g., "hook", "pattern_detection")
                - source_description: Human-readable source description
                
        Returns:
            Formatted instruction string
        """
        if not episodes:
            return None
            
        instructions = []
        instructions.append("\n" + "="*60)
        instructions.append("🧠 MEMORY CAPTURE INSTRUCTIONS")
        instructions.append("="*60)
        instructions.append(f"\n📝 Please capture these {len(episodes)} memories using Graphiti:\n")
        
        for i, episode in enumerate(episodes, 1):
            # Add timestamp if not provided
            if 'valid_at' not in episode:
                episode['valid_at'] = datetime.now().isoformat()
                
            instructions.append(f"{i}. Memory: {episode.get('name', 'Untitled')}")
            instructions.append(f"   Type: {episode.get('source', 'unknown')}")
            
            # Show preview of content
            body = episode.get('episode_body', '')
            preview = body[:100] + "..." if len(body) > 100 else body
            preview = preview.replace('\n', ' ')  # Single line
            instructions.append(f"   Preview: {preview}")
            
            # Format as MCP tool call
            instructions.append(f"\n   Tool Call:")
            instructions.append(f"   mcp__graphiti-gemini__add_episode")
            instructions.append(f"   Parameters:")
            instructions.append(f"   ```json")
            instructions.append(json.dumps({"data": episode}, indent=2))
            instructions.append(f"   ```\n")
        
        instructions.append("="*60 + "\n")
        
        return "\n".join(instructions)
    
    @staticmethod
    def create_episode(name: str, content: str, pattern_type: str = None, 
                      context: str = "conversation") -> Dict[str, Any]:
        """
        Create a properly formatted episode dictionary
        
        Args:
            name: Short descriptive name for the memory
            content: Full content to capture
            pattern_type: Optional pattern type (DECISION, SECURITY, etc.)
            context: Context where this was captured from
            
        Returns:
            Formatted episode dictionary
        """
        if pattern_type:
            formatted_name = f"{pattern_type}: {name}"
        else:
            formatted_name = name
            
        return {
            "name": formatted_name[:100],  # Limit name length
            "episode_body": content,
            "source": "claude_code_hook",
            "source_description": f"Auto-captured from {context}",
            "valid_at": datetime.now().isoformat()
        }
    
    @staticmethod
    def batch_episodes(episodes: List[Dict[str, Any]], batch_size: int = 3) -> List[List[Dict[str, Any]]]:
        """
        Batch episodes for efficient capture
        
        Args:
            episodes: List of episodes to batch
            batch_size: Maximum episodes per batch
            
        Returns:
            List of batches
        """
        batches = []
        for i in range(0, len(episodes), batch_size):
            batches.append(episodes[i:i + batch_size])
        return batches
    
    @staticmethod
    def should_capture(pattern_type: str, automation_level: str) -> bool:
        """
        Determine if a pattern should be captured based on automation level
        
        Args:
            pattern_type: Type of pattern detected
            automation_level: Current automation level (off/manual/semi/full)
            
        Returns:
            Whether to capture this pattern
        """
        if automation_level == "off":
            return False
            
        critical_patterns = ["DECISION", "SECURITY", "BREAKING", "RESOLVED", "PATTERN"]
        
        if automation_level == "manual":
            return False  # Manual mode requires explicit commands
            
        if automation_level == "semi":
            return pattern_type in critical_patterns
            
        if automation_level == "full":
            return True  # Capture everything
            
        return False


# Example usage in hooks:
if __name__ == "__main__":
    # Test the helper
    helper = MemoryCaptureHelper()
    
    # Create test episodes
    episodes = [
        helper.create_episode(
            "Fixed authentication bug",
            "Resolved issue where JWT tokens were not refreshing properly. Added automatic refresh logic.",
            "RESOLVED",
            "code_change"
        ),
        helper.create_episode(
            "Database optimization",
            "Optimized query performance by adding composite index on user_id and timestamp columns.",
            "OPTIMIZATION",
            "code_change"
        )
    ]
    
    # Format instructions
    instructions = helper.format_capture_instruction(episodes)
    print(instructions)