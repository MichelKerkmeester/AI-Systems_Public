#!/usr/bin/env python3
"""
Fix crawl4ai NEO4J_URI for Docker container access
Updates the configuration to use host.docker.internal instead of 127.0.0.1
"""

import json
import os
import sys
from pathlib import Path

def fix_crawl4ai_config():
    """Update crawl4ai configuration for Neo4j Desktop connection"""
    
    config_path = Path.home() / '.claude.json'
    
    # Read current config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Check if crawl4ai-rag exists
    if 'crawl4ai-rag' not in config.get('mcpServers', {}):
        print("❌ crawl4ai-rag not found in configuration")
        return False
    
    # Update NEO4J_URI for Neo4j Desktop
    old_uri = config['mcpServers']['crawl4ai-rag']['env'].get('NEO4J_URI', '')
    
    # Ensure we use 127.0.0.1 for Neo4j Desktop
    if 'localhost' in old_uri or 'host.docker.internal' in old_uri:
        new_uri = old_uri.replace('localhost', '127.0.0.1')
        new_uri = new_uri.replace('host.docker.internal', '127.0.0.1')
    else:
        new_uri = 'neo4j://127.0.0.1:7687'
        
        # Update the configuration
        config['mcpServers']['crawl4ai-rag']['env']['NEO4J_URI'] = new_uri
        
        # Write back the configuration
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Updated NEO4J_URI:")
        print(f"   Old: {old_uri}")
        print(f"   New: {new_uri}")
        
        # Also check if we need to specify the database
        if '/crawl4ai' not in new_uri:
            print("\n⚠️  Note: You may need to create the 'crawl4ai' database in Neo4j")
            print("   Run in Neo4j Browser: CREATE DATABASE crawl4ai")
        
        return True
    else:
        print(f"ℹ️  NEO4J_URI already configured: {old_uri}")
        return True

def restart_container():
    """Restart the crawl4ai container to apply changes"""
    print("\nRestarting crawl4ai container...")
    
    # Stop current container
    os.system("docker stop crawl4ai-mcp")
    
    # Remove it
    os.system("docker rm crawl4ai-mcp")
    
    # Start with updated config
    print("\nTo restart the container, Claude Code will need to be restarted.")
    print("The new configuration will be applied automatically.")

if __name__ == "__main__":
    print("🔧 Fixing crawl4ai Neo4j connection...")
    
    if fix_crawl4ai_config():
        print("\n✅ Configuration updated successfully!")
        print("\n🔄 Please restart Claude Code to apply the changes.")
        print("\nAlternatively, you can manually restart the Docker container:")
        print("  docker restart crawl4ai-mcp")
    else:
        print("\n❌ Failed to update configuration")
        sys.exit(1)