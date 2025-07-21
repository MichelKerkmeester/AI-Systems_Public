#!/usr/bin/env python3
"""
MCP Bridge for executing MCP tools via subprocess.

This module provides a thread-safe interface to execute MCP tools
through the Claude Code CLI, particularly for Graphiti memory operations.
"""

import json
import subprocess
import threading
import logging
from typing import Dict, Any, Optional, List
from pathlib import Path
import shlex
from datetime import datetime

# Configure logging
logger = logging.getLogger(__name__)


class MCPBridgeError(Exception):
    """Base exception for MCP Bridge errors."""
    pass


class MCPTimeoutError(MCPBridgeError):
    """Raised when MCP tool execution times out."""
    pass


class MCPExecutionError(MCPBridgeError):
    """Raised when MCP tool execution fails."""
    pass


class MCPBridge:
    """
    Thread-safe bridge for executing MCP tools via subprocess.
    
    This class provides methods to execute MCP tools through the Claude Code CLI,
    with a focus on Graphiti memory operations but extensible to other MCP servers.
    """
    
    def __init__(self, timeout: int = 5):
        """
        Initialize the MCP Bridge.
        
        Args:
            timeout: Default timeout in seconds for tool execution (default: 5)
        """
        self.timeout = timeout
        self._lock = threading.Lock()
        self._logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    def execute_tool(
        self,
        server_name: str,
        tool_name: str,
        parameters: Dict[str, Any],
        timeout: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Execute an MCP tool via subprocess.
        
        Args:
            server_name: Name of the MCP server (e.g., "mcp__graphiti-gemini")
            tool_name: Name of the tool to execute (e.g., "add_episode")
            parameters: Dictionary of parameters to pass to the tool
            timeout: Optional timeout override in seconds
        
        Returns:
            Dictionary containing the tool execution result
            
        Raises:
            MCPTimeoutError: If execution times out
            MCPExecutionError: If execution fails
            MCPBridgeError: For other errors
        """
        with self._lock:
            # Construct the full tool name
            full_tool_name = f"{server_name}__{tool_name}"
            
            # Prepare the command
            json_params = json.dumps(parameters)
            
            # Build command as list for proper subprocess handling
            cmd = [
                "claude",
                "code",
                "exec",
                "--tool",
                full_tool_name,
                "--params",
                json_params
            ]
            
            # Log the execution attempt
            self._logger.info(
                f"Executing MCP tool: {full_tool_name} with params: "
                f"{json.dumps(parameters, indent=2)}"
            )
            
            try:
                # Execute the command
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=timeout or self.timeout,
                    check=False  # We'll handle errors manually
                )
                
                # Check for execution errors
                if result.returncode != 0:
                    error_msg = (
                        f"MCP tool execution failed with code {result.returncode}. "
                        f"Stderr: {result.stderr}"
                    )
                    self._logger.error(error_msg)
                    raise MCPExecutionError(error_msg)
                
                # Parse the output
                try:
                    output = json.loads(result.stdout) if result.stdout else {}
                except json.JSONDecodeError:
                    # If output isn't JSON, return it as a string
                    output = {"result": result.stdout, "raw": True}
                
                self._logger.info(f"MCP tool execution successful: {output}")
                return output
                
            except subprocess.TimeoutExpired:
                error_msg = (
                    f"MCP tool execution timed out after "
                    f"{timeout or self.timeout} seconds"
                )
                self._logger.error(error_msg)
                raise MCPTimeoutError(error_msg)
            
            except Exception as e:
                error_msg = f"Unexpected error during MCP tool execution: {str(e)}"
                self._logger.error(error_msg, exc_info=True)
                raise MCPBridgeError(error_msg) from e
    
    def add_memory(
        self,
        name: str,
        episode_body: str,
        source: str = "mcp_bridge",
        source_description: str = "MCP Bridge",
        group_id: Optional[str] = None,
        valid_at: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Add a memory episode to Graphiti.
        
        Args:
            name: Name or title of the episode
            episode_body: The content of the episode
            source: Source of the episode (default: "mcp_bridge")
            source_description: Description of the source (default: "MCP Bridge")
            group_id: Optional group ID for organizing episodes
            valid_at: Optional ISO timestamp when the episode occurred
        
        Returns:
            Dictionary containing the result of the memory addition
            
        Raises:
            MCPTimeoutError: If execution times out
            MCPExecutionError: If execution fails
        """
        parameters = {
            "data": {
                "name": name,
                "episode_body": episode_body,
                "source": source,
                "source_description": source_description
            }
        }
        
        if group_id is not None:
            parameters["data"]["group_id"] = group_id
            
        if valid_at is not None:
            parameters["data"]["valid_at"] = valid_at
        else:
            # Default to current timestamp
            parameters["data"]["valid_at"] = datetime.utcnow().isoformat() + "Z"
        
        return self.execute_tool(
            server_name="mcp__graphiti-gemini",
            tool_name="add_episode",
            parameters=parameters
        )
    
    def search_memories(
        self,
        query: str,
        limit: int = 10,
        group_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Search for memories in Graphiti.
        
        Args:
            query: Search query string
            limit: Maximum number of results to return (default: 10)
            group_ids: Optional list of group IDs to filter by
        
        Returns:
            Dictionary containing search results
            
        Raises:
            MCPTimeoutError: If execution times out
            MCPExecutionError: If execution fails
        """
        parameters = {
            "query": {
                "query": query,
                "limit": limit
            }
        }
        
        if group_ids is not None:
            parameters["query"]["group_ids"] = group_ids
        
        return self.execute_tool(
            server_name="mcp__graphiti-gemini",
            tool_name="search",
            parameters=parameters
        )
    
    def retrieve_episodes(
        self,
        last_n: int = 10,
        group_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Retrieve recent episodes from Graphiti.
        
        Args:
            last_n: Number of episodes to retrieve (default: 10)
            group_ids: Optional list of group IDs to filter by
        
        Returns:
            Dictionary containing retrieved episodes
            
        Raises:
            MCPTimeoutError: If execution times out
            MCPExecutionError: If execution fails
        """
        parameters = {
            "last_n": last_n
        }
        
        if group_ids is not None:
            parameters["group_ids"] = group_ids
        
        return self.execute_tool(
            server_name="mcp__graphiti-gemini",
            tool_name="retrieve_episodes",
            parameters=parameters
        )


# Example usage and testing
if __name__ == "__main__":
    # Configure logging for testing
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create bridge instance
    bridge = MCPBridge()
    
    # Example: Add a memory
    try:
        result = bridge.add_memory(
            name="Test Memory",
            episode_body="This is a test memory created by the MCP Bridge",
            source="test_script",
            group_id="test-group"
        )
        print(f"Memory added successfully: {json.dumps(result, indent=2)}")
    except MCPBridgeError as e:
        print(f"Failed to add memory: {e}")
    
    # Example: Search memories
    try:
        results = bridge.search_memories(
            query="test memory",
            limit=5
        )
        print(f"Search results: {json.dumps(results, indent=2)}")
    except MCPBridgeError as e:
        print(f"Failed to search memories: {e}")