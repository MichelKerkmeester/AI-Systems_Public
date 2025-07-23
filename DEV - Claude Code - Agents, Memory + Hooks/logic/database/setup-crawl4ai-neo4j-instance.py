#!/usr/bin/env python3
"""
Setup a dedicated Neo4j instance for crawl4ai knowledge graphs.
This creates a separate Neo4j container on port 7688 to avoid conflicts.
"""

import subprocess
import sys
import time
import os

def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    print("=== Setting up dedicated Neo4j instance for crawl4ai ===\n")
    
    # 1. Stop any existing crawl4ai-neo4j container
    print("1. Checking for existing crawl4ai-neo4j container...")
    result = run_command("docker ps -a | grep crawl4ai-neo4j", check=False)
    if result.stdout:
        print("   Found existing container, removing...")
        run_command("docker stop crawl4ai-neo4j", check=False)
        run_command("docker rm crawl4ai-neo4j", check=False)
    
    # 2. Create a dedicated Neo4j container for crawl4ai
    print("\n2. Creating new Neo4j instance for crawl4ai...")
    neo4j_password = "crawl4ai123"  # Different password from main instance
    
    cmd = f"""docker run -d \
        --name crawl4ai-neo4j \
        -p 7688:7687 \
        -p 7475:7474 \
        -e NEO4J_AUTH=neo4j/{neo4j_password} \
        -e NEO4J_PLUGINS='["apoc"]' \
        -e NEO4J_apoc_export_file_enabled=true \
        -e NEO4J_apoc_import_file_enabled=true \
        -e NEO4J_apoc_import_file_use__neo4j__config=true \
        -v crawl4ai-neo4j-data:/data \
        -v crawl4ai-neo4j-logs:/logs \
        -v crawl4ai-neo4j-import:/var/lib/neo4j/import \
        -v crawl4ai-neo4j-plugins:/plugins \
        neo4j:5.26.0"""
    
    run_command(cmd)
    
    # 3. Wait for Neo4j to start
    print("\n3. Waiting for Neo4j to start...")
    time.sleep(10)
    
    # Check if it's running
    result = run_command("docker ps | grep crawl4ai-neo4j")
    if "crawl4ai-neo4j" in result.stdout:
        print("   ✅ Neo4j instance is running!")
    else:
        print("   ❌ Failed to start Neo4j instance")
        sys.exit(1)
    
    # 4. Update crawl4ai configuration
    print("\n4. Updating crawl4ai configuration...")
    
    # Read current config
    config_path = os.path.expanduser("~/.claude.json")
    with open(config_path, 'r') as f:
        import json
        config = json.load(f)
    
    # Update crawl4ai-rag environment
    if 'crawl4ai-rag' in config['mcpServers']:
        config['mcpServers']['crawl4ai-rag']['env']['NEO4J_URI'] = 'neo4j://host.docker.internal:7688'
        config['mcpServers']['crawl4ai-rag']['env']['NEO4J_PASSWORD'] = neo4j_password
        config['mcpServers']['crawl4ai-rag']['env']['NEO4J_USER'] = 'neo4j'
        # Remove database specification since we'll use the default
        if 'NEO4J_DATABASE' in config['mcpServers']['crawl4ai-rag']['env']:
            del config['mcpServers']['crawl4ai-rag']['env']['NEO4J_DATABASE']
        
        # Write updated config
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print("   ✅ Configuration updated")
    else:
        print("   ❌ crawl4ai-rag not found in config")
        sys.exit(1)
    
    # 5. Restart crawl4ai container to apply new config
    print("\n5. Restarting crawl4ai-mcp container...")
    run_command("docker restart crawl4ai-mcp")
    time.sleep(5)
    
    # 6. Display connection info
    print("\n=== Setup Complete! ===")
    print(f"\nNeo4j Browser: http://localhost:7475")
    print(f"Username: neo4j")
    print(f"Password: {neo4j_password}")
    print(f"Bolt URL: neo4j://localhost:7688")
    print("\n⚠️  IMPORTANT: Restart Claude Code to apply the configuration changes!")
    print("\nThe crawl4ai knowledge graph now has its own dedicated Neo4j instance.")
    print("This keeps it completely separate from your Graphiti memory database.")

if __name__ == "__main__":
    main()