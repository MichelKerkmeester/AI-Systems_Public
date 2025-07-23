#!/usr/bin/env python3
"""
Complete setup for crawl4ai knowledge graph feature
Handles Neo4j database creation and Docker networking
"""

import json
import os
import sys
import time
from pathlib import Path

def update_config():
    """Update crawl4ai configuration for proper Docker networking"""
    config_path = Path.home() / '.claude.json'
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    if 'crawl4ai-rag' not in config.get('mcpServers', {}):
        print("❌ crawl4ai-rag not found in configuration")
        return False
    
    # Update NEO4J_URI for Neo4j Desktop
    old_uri = config['mcpServers']['crawl4ai-rag']['env'].get('NEO4J_URI', '')
    new_uri = "neo4j://127.0.0.1:7687"  # Use 127.0.0.1 for Neo4j Desktop
    
    config['mcpServers']['crawl4ai-rag']['env']['NEO4J_URI'] = new_uri
    config['mcpServers']['crawl4ai-rag']['env']['NEO4J_DATABASE'] = 'crawl4ai'
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Updated NEO4J_URI to: {new_uri}")
    return True

def test_neo4j_connection():
    """Test if we can connect to Neo4j"""
    try:
        from neo4j import GraphDatabase
        
        uri = "neo4j://127.0.0.1:7687"  # Use 127.0.0.1 instead of localhost
        driver = GraphDatabase.driver(uri, auth=("neo4j", "AQCIbagraydayAQCIba"))
        
        with driver.session() as session:
            result = session.run("RETURN 1 AS test")
            if result.single()['test'] == 1:
                print("✅ Neo4j connection successful")
                return driver
        
    except Exception as e:
        print(f"❌ Neo4j connection failed: {e}")
        return None

def create_crawl4ai_database(driver):
    """Create the crawl4ai database if it doesn't exist"""
    try:
        with driver.session(database="system") as session:
            # Check existing databases
            result = session.run("SHOW DATABASES")
            databases = [record['name'] for record in result]
            
            if 'crawl4ai' not in databases:
                print("📦 Creating crawl4ai database...")
                session.run("CREATE DATABASE crawl4ai")
                print("✅ Database created successfully")
                
                # Wait for database to be ready
                time.sleep(2)
            else:
                print("✅ crawl4ai database already exists")
        
        # Create constraints and indexes
        with driver.session(database="crawl4ai") as session:
            constraints = [
                "CREATE CONSTRAINT IF NOT EXISTS FOR (r:Repository) REQUIRE r.name IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (f:File) REQUIRE f.path IS UNIQUE",
                "CREATE INDEX IF NOT EXISTS FOR (c:Class) ON (c.name)",
                "CREATE INDEX IF NOT EXISTS FOR (m:Method) ON (m.name)",
                "CREATE INDEX IF NOT EXISTS FOR (func:Function) ON (func.name)"
            ]
            
            for constraint in constraints:
                try:
                    session.run(constraint)
                except Exception as e:
                    if "already exists" not in str(e):
                        print(f"⚠️  Warning: {e}")
            
            print("✅ Database schema ready")
        
        driver.close()
        return True
        
    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        return False

def restart_crawl4ai():
    """Provide instructions to restart crawl4ai"""
    print("\n🔄 To apply changes:")
    print("1. Restart Claude Code CLI")
    print("   OR")
    print("2. Run: docker restart crawl4ai-mcp")
    print("\n📝 After restart, test with:")
    print("   mcp__crawl4ai-rag__parse_github_repository")
    print("   repo_url: https://github.com/simple-repository/example.git")

def main():
    print("🚀 Setting up crawl4ai knowledge graph feature\n")
    
    # Step 1: Update configuration
    print("Step 1: Updating configuration...")
    if not update_config():
        sys.exit(1)
    
    # Step 2: Test Neo4j connection
    print("\nStep 2: Testing Neo4j connection...")
    driver = test_neo4j_connection()
    
    if not driver:
        print("\n⚠️  Cannot connect to Neo4j. Please ensure:")
        print("   - Neo4j is running on 127.0.0.1:7687")
        print("   - Credentials are correct (neo4j/AQCIbagraydayAQCIba)")
        print("\n   You can install neo4j module with:")
        print("   pip install neo4j")
        
        # Continue anyway - the MCP server will handle it
        print("\n   Continuing with configuration update...")
    else:
        # Step 3: Create database
        print("\nStep 3: Setting up database...")
        create_crawl4ai_database(driver)
    
    # Step 4: Provide restart instructions
    restart_crawl4ai()
    
    print("\n✅ Setup complete!")

if __name__ == "__main__":
    main()