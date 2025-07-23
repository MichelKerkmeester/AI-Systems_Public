#!/usr/bin/env python3
"""
Update Graphiti and Crawl4AI configurations to use Neo4j Desktop instance.
Both will connect to 127.0.0.1:7687 but use different databases.
"""

import json
import os
import sys

def main():
    print("=== Updating configurations for Neo4j Desktop ===\n")
    
    # Neo4j Desktop connection details
    neo4j_uri = "neo4j://127.0.0.1:7687"
    neo4j_user = "neo4j"
    neo4j_password = "AQCIbagraydayAQCIba"  # Based on your screenshot
    neo4j_id = "26e43a06-ddc5-4a75-af47-8725b98085d6"
    neo4j_path = "/Users/michel_kerkmeester/Library/Application Support/neo4j-desktop/Application/Data/dbmss/dbms-26e43a06-ddc5-4a75-af47-8725b98085d6"
    
    # Read current config
    config_path = os.path.expanduser("~/.claude.json")
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # 1. Update Graphiti configuration (already local, just update connection)
    print("1. Updating Graphiti configuration...")
    if 'graphiti-gemini' in config['mcpServers']:
        config['mcpServers']['graphiti-gemini']['env'].update({
            'NEO4J_URI': neo4j_uri,
            'NEO4J_USER': neo4j_user,
            'NEO4J_PASSWORD': neo4j_password,
            'NEO4J_ID': neo4j_id,
            'NEO4J_PATH': neo4j_path,
            'NEO4J_DATABASE': 'graphiti'  # Specify the graphiti database
        })
        print("   ✅ Graphiti updated to use Neo4j Desktop (graphiti database)")
    
    # 2. Update Crawl4AI to run locally instead of Docker
    print("\n2. Converting Crawl4AI from Docker to local...")
    if 'crawl4ai-rag' in config['mcpServers']:
        # Check if venv exists
        venv_python = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag/.venv/bin/python"
        if not os.path.exists(venv_python):
            print("   ⚠️  Virtual environment not found. Creating it...")
            os.system('cd "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag" && python3 -m venv .venv')
            os.system('cd "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag" && .venv/bin/pip install -e .')
        
        # Update configuration to run locally
        old_env = config['mcpServers']['crawl4ai-rag']['env']
        config['mcpServers']['crawl4ai-rag'] = {
            'command': venv_python,
            'args': [
                '/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag/src/crawl4ai_rag_mcp_server/server.py'
            ],
            'env': {
                # Keep existing API keys and settings
                'OPENAI_API_KEY': old_env.get('OPENAI_API_KEY', ''),
                'MODEL_CHOICE': old_env.get('MODEL_CHOICE', 'gpt-4o-mini'),
                'USE_CONTEXTUAL_EMBEDDINGS': old_env.get('USE_CONTEXTUAL_EMBEDDINGS', 'true'),
                'USE_HYBRID_SEARCH': old_env.get('USE_HYBRID_SEARCH', 'true'),
                'USE_AGENTIC_RAG': old_env.get('USE_AGENTIC_RAG', 'true'),
                'USE_RERANKING': old_env.get('USE_RERANKING', 'true'),
                'USE_KNOWLEDGE_GRAPH': 'true',
                'SUPABASE_URL': old_env.get('SUPABASE_URL', ''),
                'SUPABASE_SERVICE_KEY': old_env.get('SUPABASE_SERVICE_KEY', ''),
                # Neo4j Desktop connection
                'NEO4J_URI': neo4j_uri,
                'NEO4J_USER': neo4j_user,
                'NEO4J_PASSWORD': neo4j_password,
                'NEO4J_DATABASE': 'crawl4ai'  # Specify the crawl4ai database
            }
        }
        print("   ✅ Crawl4AI converted to local execution (crawl4ai database)")
    
    # 3. Write updated config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print("\n3. Configuration updated successfully!")
    
    # 4. Stop crawl4ai Docker container if running
    print("\n4. Cleaning up Docker containers...")
    os.system("docker stop crawl4ai-mcp 2>/dev/null")
    os.system("docker rm crawl4ai-mcp 2>/dev/null")
    print("   ✅ Docker containers cleaned up")
    
    # 5. Display summary
    print("\n=== Configuration Summary ===")
    print(f"\nNeo4j Desktop Instance:")
    print(f"  URI: {neo4j_uri}")
    print(f"  User: {neo4j_user}")
    print(f"  Password: {neo4j_password}")
    print(f"\nDatabases:")
    print(f"  - graphiti: For conversation memories (Graphiti)")
    print(f"  - crawl4ai: For code knowledge graphs (Crawl4AI)")
    print(f"\nBoth services now run locally - no Docker needed!")
    print("\n⚠️  IMPORTANT: Restart Claude Code to apply these changes!")

if __name__ == "__main__":
    main()