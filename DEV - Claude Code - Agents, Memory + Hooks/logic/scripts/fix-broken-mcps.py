#!/usr/bin/env python3
"""
Fix broken MCP servers by adding missing configurations to Claude Desktop config
"""

import json
import os
from pathlib import Path

def main():
    """Add missing MCP servers to Claude Desktop config"""
    
    # Path to Claude Desktop config
    config_path = Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    
    # Read current config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Add missing MCP servers
    missing_servers = {
        "code-context-simple": {
            "command": "node",
            "args": [
                "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/code-context-simple/index.js"
            ],
            "env": {
                "INDEX_PATH": "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/.code-context-index"
            }
        },
        "hyperbolic-wrapper": {
            "command": "node",
            "args": [
                "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/hyperbolic-wrapper/index.js"
            ],
            "env": {
                "HYPERBOLIC_API_KEY": os.getenv("HYPERBOLIC_API_KEY", "")
            }
        }
    }
    
    # Check which servers are missing
    added = []
    for server_name, server_config in missing_servers.items():
        if server_name not in config.get("mcpServers", {}):
            if "mcpServers" not in config:
                config["mcpServers"] = {}
            config["mcpServers"][server_name] = server_config
            added.append(server_name)
    
    if added:
        # Write updated config
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Added {len(added)} missing MCP servers:")
        for server in added:
            print(f"   - {server}")
        print("\n⚠️  IMPORTANT:")
        print("1. Set HYPERBOLIC_API_KEY environment variable for Qwen/hyperbolic support")
        print("2. Restart Claude Desktop app for changes to take effect")
    else:
        print("✅ All MCP servers already configured")
    
    # Check if MCP server files exist
    print("\n📁 Checking MCP server files...")
    for server_name, server_config in missing_servers.items():
        if server_config["command"] == "node":
            script_path = server_config["args"][0]
            if Path(script_path).exists():
                print(f"   ✅ {server_name}: {script_path} exists")
            else:
                print(f"   ❌ {server_name}: {script_path} NOT FOUND")

if __name__ == "__main__":
    main()