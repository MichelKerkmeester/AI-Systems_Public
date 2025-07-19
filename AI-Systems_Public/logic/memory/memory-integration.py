#!/usr/bin/env python3
"""
Memory Integration Layer
Bridges Claude Code with Graphiti through automatic capture and commands.
"""

import asyncio
import json
import re
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone
import logging

from memory_hook import memory_hook, AutomationLevel

logger = logging.getLogger(__name__)

class MemoryIntegration:
    """Main integration class for Graphiti memory system"""
    
    def __init__(self):
        self.hook = memory_hook
        self.pending_captures = []
        self.memory_stats = {
            "total_memories": 0,
            "auto_captured": 0,
            "manual_captured": 0,
            "last_capture": None
        }
        self._load_stats()
    
    def _load_stats(self):
        """Load memory statistics"""
        try:
            with open(".claude/logic/memory/stats.json", 'r') as f:
                self.memory_stats = json.load(f)
        except FileNotFoundError:
            self._save_stats()
    
    def _save_stats(self):
        """Save memory statistics"""
        with open(".claude/logic/memory/stats.json", 'w') as f:
            json.dump(self.memory_stats, f, indent=2)
    
    async def process_text(self, text: str, context: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Process text for memory-worthy content"""
        captures = []
        
        # Detect patterns
        matches = self.hook.detect_patterns(text)
        
        for pattern_name, content, pattern_config in matches:
            if self.hook.should_capture(pattern_config):
                # Prepare memory data
                memory_data = await self.hook.capture_memory(
                    content,
                    pattern_config['category'],
                    {
                        'pattern': pattern_name,
                        'priority': pattern_config['priority'],
                        'update_facts': pattern_config.get('update_facts', False),
                        'update_patterns': pattern_config.get('update_patterns', False),
                        'update_constraints': pattern_config.get('update_constraints', False),
                        'context': context
                    }
                )
                
                # Check automation level
                if self.hook.automation_level == AutomationLevel.FULL_AUTO:
                    # Capture immediately
                    captures.append({
                        'action': 'capture',
                        'data': memory_data,
                        'auto': True
                    })
                elif self.hook.automation_level == AutomationLevel.SEMI_AUTO:
                    # Queue for confirmation
                    self.pending_captures.append({
                        'data': memory_data,
                        'pattern': pattern_name,
                        'content': content
                    })
                    captures.append({
                        'action': 'pending',
                        'data': memory_data,
                        'requires_confirmation': True
                    })
        
        return captures
    
    async def capture_from_tool_result(self, tool_name: str, result: Any, context: Dict[str, Any] = None):
        """Capture memories from tool results"""
        captures = []
        
        # Special handling for specific tools
        if tool_name == "mcp__sequential-thinking__process_thought":
            # Capture completed thinking sessions
            if isinstance(result, dict) and result.get('stage') == 'Conclusion':
                memory_data = await self.hook.capture_memory(
                    f"Sequential thinking conclusion: {result.get('thought', '')}",
                    "thinking_conclusion",
                    {'tool': tool_name, 'context': context}
                )
                captures.append(memory_data)
        
        elif tool_name == "TodoWrite" and isinstance(result, str):
            # Capture completed todos
            if "completed" in result.lower():
                memory_data = await self.hook.capture_memory(
                    f"Completed task: {result}",
                    "task_completion",
                    {'tool': tool_name, 'context': context}
                )
                captures.append(memory_data)
        
        elif tool_name in ["Edit", "MultiEdit", "Write"]:
            # Capture significant code changes
            if context and context.get('significant_change'):
                memory_data = await self.hook.capture_memory(
                    f"Code change in {context.get('file_path', 'unknown')}: {context.get('description', '')}",
                    "code_change",
                    {'tool': tool_name, 'context': context}
                )
                captures.append(memory_data)
        
        return captures
    
    async def handle_command(self, command: str, args: List[str] = None) -> Dict[str, Any]:
        """Handle memory-related commands"""
        if command == "status":
            return await self._get_status()
        
        elif command == "auto":
            if args and len(args) > 0:
                level = args[0]
                if self.hook.set_automation_level(level):
                    return {
                        "success": True,
                        "message": f"Automation level set to: {level}",
                        "level": level
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Invalid automation level: {level}",
                        "valid_levels": ["off", "manual", "semi", "full"]
                    }
            else:
                return {
                    "success": False,
                    "message": "Please specify automation level: off, manual, semi, or full"
                }
        
        elif command == "search":
            if args and len(args) > 0:
                query = " ".join(args)
                # This would call the Graphiti search
                return {
                    "success": True,
                    "message": f"Search for: {query}",
                    "query": query
                }
            else:
                return {
                    "success": False,
                    "message": "Please provide a search query"
                }
        
        elif command == "manual":
            if args and len(args) > 0:
                text = " ".join(args)
                memory_data = await self.hook.capture_memory(
                    text,
                    "manual_capture",
                    {'source': 'manual_command'}
                )
                return {
                    "success": True,
                    "message": "Memory captured",
                    "data": memory_data
                }
            else:
                return {
                    "success": False,
                    "message": "Please provide text to capture"
                }
        
        elif command == "confirm":
            # Confirm pending captures
            if self.pending_captures:
                confirmed = self.pending_captures.copy()
                self.pending_captures.clear()
                return {
                    "success": True,
                    "message": f"Confirmed {len(confirmed)} pending memories",
                    "captures": confirmed
                }
            else:
                return {
                    "success": True,
                    "message": "No pending captures"
                }
        
        else:
            return {
                "success": False,
                "message": f"Unknown memory command: {command}",
                "available_commands": ["status", "auto", "search", "manual", "confirm"]
            }
    
    async def _get_status(self) -> Dict[str, Any]:
        """Get comprehensive memory status"""
        hook_status = self.hook.get_status()
        
        # Get Graphiti stats (would call the MCP tool)
        graphiti_stats = {
            "connected": True,
            "total_nodes": 0,  # Would query actual count
            "total_edges": 0   # Would query actual count
        }
        
        return {
            "success": True,
            "automation": {
                "level": hook_status["automation_level"],
                "patterns": hook_status["patterns_loaded"],
                "triggers": hook_status["trigger_keywords"]
            },
            "statistics": self.memory_stats,
            "pending": len(self.pending_captures),
            "graphiti": graphiti_stats
        }
    
    def update_stats(self, capture_type: str = "auto"):
        """Update memory statistics"""
        self.memory_stats["total_memories"] += 1
        if capture_type == "auto":
            self.memory_stats["auto_captured"] += 1
        else:
            self.memory_stats["manual_captured"] += 1
        self.memory_stats["last_capture"] = datetime.now(timezone.utc).isoformat()
        self._save_stats()


# Global instance
memory_integration = MemoryIntegration()