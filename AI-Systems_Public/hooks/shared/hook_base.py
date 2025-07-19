#!/usr/bin/env python3
"""
Base class and utilities for all Claude hooks
Provides common functionality for JSON I/O, error handling, and exit codes
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from abc import ABC, abstractmethod


class HookBase(ABC):
    """Base class for all Claude hooks"""
    
    def __init__(self):
        """Initialize base hook with common properties"""
        self.project_root = self._find_project_root()
        self.claude_path = self.project_root / ".claude"
        self.hook_input = None
        
    def _find_project_root(self) -> Path:
        """Find project root by looking for .claude directory"""
        current = Path(__file__).resolve()
        # Start from hook file location and go up
        for parent in current.parents:
            if (parent / ".claude").exists():
                return parent
        # Fallback to parents[5] if .claude not found
        return Path(__file__).resolve().parents[5]
    
    def read_input(self) -> Dict[str, Any]:
        """Read and parse JSON input from stdin"""
        try:
            self.hook_input = json.loads(sys.stdin.read())
            return self.hook_input
        except json.JSONDecodeError as e:
            self.error_exit(f"Invalid JSON input: {e}")
        except Exception as e:
            self.error_exit(f"Failed to read input: {e}")
    
    @abstractmethod
    def process(self, hook_input: Dict[str, Any]) -> Tuple[int, Optional[str]]:
        """
        Process hook input and return exit code and optional output
        
        Args:
            hook_input: The parsed hook input data
            
        Returns:
            Tuple of (exit_code, output_message)
            exit_code: 0 for success, 2 to block
            output_message: Optional message to display
        """
        pass
    
    def run(self):
        """Main entry point for hook execution"""
        try:
            # Read input
            hook_input = self.read_input()
            
            # Process with implemented logic
            exit_code, output = self.process(hook_input)
            
            # Output if any
            if output:
                print(output)
            
            # Exit with code
            sys.exit(exit_code)
            
        except SystemExit:
            # Re-raise system exit
            raise
        except Exception as e:
            # Log error but don't block
            self.error_exit(f"Hook error: {e}", block=False)
    
    def error_exit(self, message: str, block: bool = False):
        """
        Exit with error message
        
        Args:
            message: Error message to display
            block: Whether to block (exit 2) or continue (exit 0)
        """
        print(f"⚠️  {message}")
        sys.exit(2 if block else 0)
    
    def success_exit(self, message: Optional[str] = None):
        """Exit successfully with optional message"""
        if message:
            print(message)
        sys.exit(0)


class ToolHook(HookBase):
    """Base class for hooks that process tool usage"""
    
    def get_tool_info(self) -> Tuple[str, Dict[str, Any]]:
        """Extract tool name and input from hook data"""
        tool_name = self.hook_input.get("toolName", "")
        tool_input = self.hook_input.get("toolInput", {})
        return tool_name, tool_input
    
    def is_relevant_tool(self, tool_names: list) -> bool:
        """Check if current tool is in the relevant list"""
        tool_name, _ = self.get_tool_info()
        return tool_name in tool_names


class UserPromptHook(HookBase):
    """Base class for hooks that process user prompts"""
    
    def get_user_message(self) -> str:
        """Extract user message from hook data"""
        return self.hook_input.get("userMessage", "")