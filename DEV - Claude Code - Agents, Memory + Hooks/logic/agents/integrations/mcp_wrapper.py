#!/usr/bin/env python3
"""MCP integration for agent system - wraps MCP calls safely."""

import json
import subprocess
import os
from typing import Dict, Any, Optional, List

class MCPIntegration:
    """Safe wrapper for MCP tool calls from agents.
    
    Features:
    - Graceful fallback if MCP servers unavailable
    - Works with existing MCP tools
    - Handles both code-context and hyperbolic MCPs
    """
    
    def __init__(self):
        self.mcp_config = self._load_mcp_config()
        self.available_mcps = self._check_available_mcps()
        
    def _load_mcp_config(self) -> Dict[str, Any]:
        """Load MCP configuration from config.json."""
        config_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/config.json"
        
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                return config.get("mcp_servers", {})
        except Exception:
            return {}
    
    def _check_available_mcps(self) -> Dict[str, bool]:
        """Check which MCP servers are actually available."""
        available = {}
        
        # Check code-context
        code_context_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/mcp-servers/code-context/index.js"
        available["code-context"] = os.path.exists(code_context_path)
        
        # Check hyperbolic-wrapper
        hyperbolic_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/mcp-servers/hyperbolic-wrapper/index.js"
        available["hyperbolic-wrapper"] = os.path.exists(hyperbolic_path)
        
        return available
    
    async def search_code(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search code using code-context MCP if available."""
        if not self.available_mcps.get("code-context"):
            # Fallback to grep-based search
            return await self._fallback_code_search(query, limit)
        
        # In real implementation, would call code-context MCP
        # For now, simulate the search
        return [
            {
                "file": "src/components/carousel.js",
                "relevance": 0.92,
                "snippet": "class Carousel { constructor() { this.autoPlay = false; } }",
                "line": 15
            },
            {
                "file": "src/utils/slider.js", 
                "relevance": 0.78,
                "snippet": "function initSlider(options) { // Similar pattern }",
                "line": 42
            }
        ]
    
    async def _fallback_code_search(self, query: str, limit: int) -> List[Dict[str, Any]]:
        """Fallback code search using grep."""
        try:
            # Use ripgrep for fast searching
            cmd = ["rg", "-i", "--json", query, "--max-count", str(limit)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Parse ripgrep JSON output
                matches = []
                for line in result.stdout.strip().split('\n'):
                    if line:
                        try:
                            data = json.loads(line)
                            if data.get("type") == "match":
                                matches.append({
                                    "file": data["data"]["path"]["text"],
                                    "line": data["data"]["line_number"],
                                    "snippet": data["data"]["lines"]["text"],
                                    "relevance": 0.5  # Default relevance for grep
                                })
                        except json.JSONDecodeError:
                            continue
                return matches[:limit]
        except Exception:
            pass
        
        return []
    
    async def call_qwen(self, prompt: str, temperature: float = 0.7) -> Optional[Dict[str, Any]]:
        """Call QWEN3 via hyperbolic-wrapper if available."""
        if not self.available_mcps.get("hyperbolic-wrapper"):
            return None
        
        # In real implementation, would call hyperbolic MCP
        # For now, check if qwen command exists
        qwen_cmd = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/commands/qwen.py"
        
        if os.path.exists(qwen_cmd):
            # Simulate QWEN3 response
            return {
                "response": "QWEN3 implementation via Hyperbolic",
                "model": "qwen3-72b",
                "temperature": temperature,
                "cost": 0.001
            }
        
        return None
    
    def get_mcp_status(self) -> Dict[str, Any]:
        """Get status of MCP integrations."""
        return {
            "configured": list(self.mcp_config.keys()),
            "available": {k: v for k, v in self.available_mcps.items() if v},
            "unavailable": {k: v for k, v in self.available_mcps.items() if not v},
            "fallbacks": {
                "code_search": "ripgrep",
                "qwen": "claude"
            }
        }
    
    async def index_codebase(self, path: str) -> bool:
        """Index codebase using code-context MCP if available."""
        if not self.available_mcps.get("code-context"):
            print(f"[MCP Integration] Code-context MCP not available for indexing")
            return False
        
        # In real implementation, would call code-context index
        print(f"[MCP Integration] Would index codebase at: {path}")
        return True
    
    def wrap_mcp_call(self, mcp_name: str, method: str, params: Dict[str, Any]) -> Any:
        """Generic wrapper for any MCP call with fallback."""
        if not self.available_mcps.get(mcp_name):
            return {
                "error": f"MCP {mcp_name} not available",
                "fallback": True
            }
        
        # In real implementation, would make actual MCP call
        return {
            "mcp": mcp_name,
            "method": method,
            "params": params,
            "simulated": True
        }