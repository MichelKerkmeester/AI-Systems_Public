#!/usr/bin/env python3
"""
Post Tool Use Memory Hook
Captures memories after significant tool operations
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, List
from datetime import datetime

# Add parent directories to path for imports
claude_path = Path(__file__).resolve().parents[3]  # Get to .claude directory
sys.path.insert(0, str(claude_path))

from logic.shared import HookBase
from logic.hooks.memory.memory_capture_helper import MemoryCaptureHelper


class PostToolUseMemoryHook(HookBase):
    """Capture memories after significant tool uses"""
    
    def __init__(self):
        super().__init__()
        
        # Tools that trigger memory capture
        self.significant_tools = {
            # File operations
            "Edit": "code_change",
            "MultiEdit": "code_change", 
            "Write": "file_creation",
            "NotebookEdit": "notebook_change",
            
            # Git operations
            "mcp__github-mcp-server__create_pull_request": "pr_created",
            "mcp__github-mcp-server__merge_pull_request": "pr_merged",
            "mcp__github-mcp-server__create_issue": "issue_created",
            
            # System operations
            "Bash": "command_execution"
        }
        
        # Patterns to detect in tool results
        self.result_patterns = {
            "ERROR_FIXED": r"error.*fixed|resolved|debugged|solution found",
            "PERFORMANCE": r"optimized|faster|reduced.*time|improved.*performance",
            "SECURITY_FIX": r"vulnerability.*fixed|security.*patched|sanitized",
            "API_CREATED": r"endpoint.*created|api.*added|route.*implemented",
            "TEST_ADDED": r"test.*added|test.*created|coverage.*increased",
            "REFACTOR": r"refactored|cleaned up|simplified|reorganized",
            "DEPENDENCY": r"installed|upgraded|added.*dependency|package.*updated"
        }
        
        # Load memory settings
        settings_path = Path(__file__).parent.parent.parent / "logic" / "memory" / "settings.json"
        try:
            with open(settings_path) as f:
                self.memory_settings = json.load(f)
        except:
            self.memory_settings = {"automation_level": "semi"}
            
        # Buffer for collecting operation context
        self.operation_buffer = []
        self.pending_captures = []  # Episodes waiting to be captured
        
    def should_capture(self, tool_name: str, tool_args: Dict, result: Any) -> bool:
        """Determine if this tool use should trigger memory capture"""
        # Check automation level
        level = self.memory_settings.get("automation_level", "semi")
        if level == "off":
            return False
            
        # Check if it's a significant tool
        if tool_name not in self.significant_tools:
            return False
            
        # For manual mode, only capture critical operations
        if level == "manual":
            critical_tools = ["mcp__github-mcp-server__create_pull_request", 
                            "mcp__github-mcp-server__merge_pull_request"]
            return tool_name in critical_tools
            
        # For semi/full mode, check additional criteria
        # Skip small edits (less than 5 lines)
        if tool_name in ["Edit", "MultiEdit"]:
            content = tool_args.get("new_string", "")
            if content.count('\n') < 5:
                return False
                
        return True
        
    def extract_operation_context(self, tool_name: str, tool_args: Dict, result: Any) -> Dict[str, Any]:
        """Extract meaningful context from the operation"""
        context = {
            "tool": tool_name,
            "type": self.significant_tools.get(tool_name, "unknown"),
            "timestamp": datetime.now().isoformat(),
            "success": True  # Assume success if we got here
        }
        
        # Extract file paths
        if "file_path" in tool_args:
            context["file"] = tool_args["file_path"]
        elif "path" in tool_args:
            context["file"] = tool_args["path"]
            
        # Extract operation details
        if tool_name == "Edit" or tool_name == "MultiEdit":
            context["changes"] = {
                "old": tool_args.get("old_string", "")[:100] + "...",
                "new": tool_args.get("new_string", "")[:100] + "..."
            }
        elif tool_name == "Write":
            context["content_preview"] = tool_args.get("content", "")[:200] + "..."
        elif tool_name == "Bash":
            context["command"] = tool_args.get("command", "")
            context["output"] = str(result).get("output", "")[:200] if isinstance(result, dict) else str(result)[:200]
        elif "github" in tool_name:
            context["repo"] = f"{tool_args.get('owner', '')}/{tool_args.get('repo', '')}"
            context["details"] = tool_args
            
        # Detect patterns in results
        result_str = str(result) if result else ""
        for pattern_type, pattern in self.result_patterns.items():
            if re.search(pattern, result_str, re.IGNORECASE):
                context["pattern_detected"] = pattern_type
                break
                
        return context
        
    def format_memory_episode(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Format context into a memory episode for Graphiti"""
        # Create a descriptive name
        name_parts = []
        if context.get("pattern_detected"):
            name_parts.append(context["pattern_detected"])
        name_parts.append(context["type"].replace("_", " ").title())
        if context.get("file"):
            name_parts.append(f"in {Path(context['file']).name}")
            
        name = ": ".join(name_parts)
        
        # Build episode body
        body_parts = []
        body_parts.append(f"Tool: {context['tool']}")
        body_parts.append(f"Type: {context['type']}")
        
        if context.get("file"):
            body_parts.append(f"File: {context['file']}")
            
        if context.get("changes"):
            body_parts.append("Changes made:")
            body_parts.append(f"  Old: {context['changes']['old']}")
            body_parts.append(f"  New: {context['changes']['new']}")
            
        if context.get("command"):
            body_parts.append(f"Command: {context['command']}")
            if context.get("output"):
                body_parts.append(f"Output: {context['output']}")
                
        if context.get("repo"):
            body_parts.append(f"Repository: {context['repo']}")
            
        episode_body = "\n".join(body_parts)
        
        return {
            "name": name,
            "episode_body": episode_body,
            "source": "post_tool_use_hook",
            "source_description": f"Auto-captured from {context['tool']} operation",
            "valid_at": context["timestamp"]
        }
        
    def capture_to_graphiti(self, episode: Dict[str, Any]) -> bool:
        """Send memory to Graphiti (simulated for now)"""
        try:
            # Store for later prompt
            self.pending_captures.append(episode)
            return True
        except Exception as e:
            self.logger.error(f"Failed to capture memory: {e}")
            return False
    
    def format_capture_prompt(self, episodes: List[Dict[str, Any]]) -> str:
        """Format a prompt that encourages Claude to capture memories"""
        helper = MemoryCaptureHelper()
        return helper.format_capture_instruction(episodes)
    
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """Process post tool use events"""
        tool_name = hook_input.get('tool_name', '')
        tool_args = hook_input.get('tool_args', {})
        result = hook_input.get('result', {})
        
        try:
            # Check if we should capture this operation
            if not self.should_capture(tool_name, tool_args, result):
                return 0, None
                
            # Extract operation context
            context = self.extract_operation_context(tool_name, tool_args, result)
            
            # Add to operation buffer for potential batch processing
            self.operation_buffer.append(context)
            
            # Format as memory episode
            episode = self.format_memory_episode(context)
            
            # Capture to Graphiti
            if self.capture_to_graphiti(episode):
                # In full automation mode, prompt for batch capture
                if self.memory_settings.get("automation_level") == "full":
                    # Batch captures every 3 operations
                    if len(self.pending_captures) >= 3:
                        prompt = self.format_capture_prompt(self.pending_captures)
                        self.pending_captures = []  # Clear after prompting
                        return 0, prompt
                # In semi mode, only prompt for patterns
                elif context.get("pattern_detected"):
                    prompt = self.format_capture_prompt([episode])
                    self.pending_captures = []  # Clear after prompting  
                    return 0, prompt
                    
                return 0, None  # Silent capture otherwise
                    
        except Exception as e:
            self.logger.error(f"PostToolUseMemory error: {e}")
            
        return 0, None


# Main entry point
if __name__ == "__main__":
    hook = PostToolUseMemoryHook()
    hook.run()