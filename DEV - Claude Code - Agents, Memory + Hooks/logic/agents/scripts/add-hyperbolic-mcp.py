#!/usr/bin/env python3
"""
Add Hyperbolic QWEN MCP configuration to ~/.claude.json
"""

import json
import os
from pathlib import Path

def add_hyperbolic_mcp():
    claude_json_path = Path.home() / '.claude.json'
    
    # Read the current configuration
    print(f"Reading {claude_json_path}...")
    with open(claude_json_path, 'r') as f:
        config = json.load(f)
    
    # Add Hyperbolic QWEN configuration
    hyperbolic_config = {
        "command": "node",
        "args": [
            "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/mcp-servers/hyperbolic-wrapper/index.js"
        ],
        "env": {
            "HYPERBOLIC_API_KEY": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtaWNoZWxrZXJrbWVlc3RlckBwbS5tZSIsImlhdCI6MTc1MzI2MzUzM30.NVN8JRakXjouAvE2G841dmZgNbEtvTubCey17Ez1azo",
            "HYPERBOLIC_BASE_URL": "https://api.hyperbolic.xyz/v1",
            "MODEL_NAME": "Qwen/Qwen3-Coder-480B-A35B-Instruct"
        }
    }
    
    # Check if mcpServers exists
    if 'mcpServers' not in config:
        config['mcpServers'] = {}
    
    # Check if hyperbolic-qwen already exists
    if 'hyperbolic-qwen' in config['mcpServers']:
        print("Hyperbolic QWEN MCP already configured. Updating...")
    else:
        print("Adding Hyperbolic QWEN MCP configuration...")
    
    # Add or update the configuration
    config['mcpServers']['hyperbolic-qwen'] = hyperbolic_config
    
    # Create backup
    backup_path = claude_json_path.with_suffix('.json.backup')
    print(f"Creating backup at {backup_path}...")
    with open(backup_path, 'w') as f:
        with open(claude_json_path, 'r') as original:
            f.write(original.read())
    
    # Write the updated configuration
    print(f"Writing updated configuration to {claude_json_path}...")
    with open(claude_json_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Hyperbolic QWEN MCP configuration added successfully!")
    print("\nNext steps:")
    print("1. Install dependencies:")
    print("   cd /Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/mcp-servers/hyperbolic-wrapper")
    print("   npm install")
    print("\n2. Restart Claude Code to load the new MCP server")
    print("\n3. Test with: mcp__hyperbolic-qwen__qwen_complete")

if __name__ == "__main__":
    add_hyperbolic_mcp()