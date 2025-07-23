#!/usr/bin/env python3
"""
Update crawl4ai configuration to use the correct Neo4j Desktop instance.
Ensures connection to neo4j://127.0.0.1:7687 with the correct database.
"""

import json
import os
import sys
from pathlib import Path

def update_crawl4ai_config():
    """Update crawl4ai configuration for Neo4j Desktop"""
    
    # Neo4j Desktop connection details
    neo4j_uri = "neo4j://127.0.0.1:7687"
    neo4j_user = "neo4j"
    neo4j_password = "AQCIbagraydayAQCIba"
    neo4j_database_id = "26e43a06-ddc5-4a75-af47-8725b98085d6"
    neo4j_path = "/Users/michel_kerkmeester/Library/Application Support/neo4j-desktop/Application/Data/dbmss/dbms-26e43a06-ddc5-4a75-af47-8725b98085d6"
    
    config_path = Path.home() / '.claude.json'
    
    # Read current config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Check if crawl4ai-rag exists
    if 'crawl4ai-rag' not in config.get('mcpServers', {}):
        print("❌ crawl4ai-rag not found in configuration")
        return False
    
    # Update crawl4ai-rag environment variables
    crawl4ai_config = config['mcpServers']['crawl4ai-rag']
    
    # Update Neo4j connection details
    crawl4ai_config['env']['NEO4J_URI'] = neo4j_uri
    crawl4ai_config['env']['NEO4J_USER'] = neo4j_user
    crawl4ai_config['env']['NEO4J_PASSWORD'] = neo4j_password
    
    # Add database-specific environment variables
    crawl4ai_config['env']['NEO4J_DATABASE'] = 'crawl4ai'
    crawl4ai_config['env']['NEO4J_DATABASE_ID'] = neo4j_database_id
    crawl4ai_config['env']['NEO4J_PATH'] = neo4j_path
    
    # Write back the configuration
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Updated crawl4ai configuration:")
    print(f"   NEO4J_URI: {neo4j_uri}")
    print(f"   NEO4J_USER: {neo4j_user}")
    print(f"   NEO4J_PASSWORD: {neo4j_password}")
    print(f"   NEO4J_DATABASE: crawl4ai")
    print(f"   NEO4J_DATABASE_ID: {neo4j_database_id}")
    
    return True

def check_neo4j_database():
    """Check if the crawl4ai database exists in Neo4j"""
    try:
        from neo4j import GraphDatabase
        
        uri = "neo4j://127.0.0.1:7687"
        driver = GraphDatabase.driver(uri, auth=("neo4j", "AQCIbagraydayAQCIba"))
        
        with driver.session(database="system") as session:
            result = session.run("SHOW DATABASES")
            databases = [record['name'] for record in result]
            
            if 'crawl4ai' not in databases:
                print("\n⚠️  The 'crawl4ai' database doesn't exist yet.")
                print("   Creating it now...")
                session.run("CREATE DATABASE crawl4ai")
                print("   ✅ Database created successfully")
            else:
                print("\n✅ The 'crawl4ai' database already exists")
        
        driver.close()
        return True
        
    except Exception as e:
        print(f"\n⚠️  Cannot verify database: {e}")
        print("   The database will be created when crawl4ai first connects.")
        return False

def main():
    print("🔧 Updating crawl4ai Neo4j configuration...")
    
    if update_crawl4ai_config():
        print("\n✅ Configuration updated successfully!")
        
        # Try to check/create the database
        check_neo4j_database()
        
        print("\n🔄 Please restart Claude Code to apply the changes.")
        print("\nThe crawl4ai service will now connect to:")
        print("  - Neo4j Desktop instance at 127.0.0.1:7687")
        print("  - Database: crawl4ai")
        print("  - Database ID: 26e43a06-ddc5-4a75-af47-8725b98085d6")
    else:
        print("\n❌ Failed to update configuration")
        sys.exit(1)

if __name__ == "__main__":
    main()