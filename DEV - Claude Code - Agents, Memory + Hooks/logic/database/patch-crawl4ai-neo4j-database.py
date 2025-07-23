#!/usr/bin/env python3
"""
Patch DirectNeo4jExtractor to support database parameter.
This ensures crawl4ai uses the correct database in Neo4j Desktop.
"""

import os
import re
from pathlib import Path

def patch_direct_neo4j_extractor():
    """Update DirectNeo4jExtractor to support database parameter"""
    
    file_path = Path("/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag/knowledge_graphs/parse_repo_into_neo4j.py")
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return False
    
    print(f"🔧 Patching {file_path.name}...")
    
    # Read the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if already patched
    if "self.database = database" in content:
        print("✅ File already patched with database support")
        return True
    
    # Patch 1: Update __init__ to accept database parameter
    init_pattern = r'(def __init__\(self, neo4j_uri: str, neo4j_user: str, neo4j_password: str\):)'
    init_replacement = r'def __init__(self, neo4j_uri: str, neo4j_user: str, neo4j_password: str, database: str = "neo4j"):'
    content = re.sub(init_pattern, init_replacement, content)
    
    # Patch 2: Store database in instance
    store_pattern = r'(self\.neo4j_password = neo4j_password)'
    store_replacement = r'\1\n        self.database = database'
    content = re.sub(store_pattern, store_replacement, content)
    
    # Patch 3: Update all session() calls to use database parameter
    # First pattern: async with self.driver.session() as session:
    session_pattern1 = r'async with self\.driver\.session\(\) as session:'
    session_replacement1 = r'async with self.driver.session(database=self.database) as session:'
    content = re.sub(session_pattern1, session_replacement1, content)
    
    # Second pattern: self.driver.session()
    session_pattern2 = r'self\.driver\.session\(\)'
    session_replacement2 = r'self.driver.session(database=self.database)'
    content = re.sub(session_pattern2, session_replacement2, content)
    
    # Write back the patched content
    with open(file_path, 'w') as f:
        f.write(content)
    
    print("✅ Patched DirectNeo4jExtractor to support database parameter")
    return True

def patch_crawl4ai_mcp():
    """Update crawl4ai_mcp.py to pass database parameter"""
    
    file_path = Path("/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/crawl4ai-rag/src/crawl4ai_mcp.py")
    
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return False
    
    print(f"🔧 Patching {file_path.name}...")
    
    # Read the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check if already patched
    if 'os.getenv("NEO4J_DATABASE", "crawl4ai")' in content:
        print("✅ File already patched with database support")
        return True
    
    # Find the DirectNeo4jExtractor initialization
    pattern = r'(repo_extractor = DirectNeo4jExtractor\(neo4j_uri, neo4j_user, neo4j_password\))'
    
    # Replace with version that includes database parameter
    replacement = r'repo_extractor = DirectNeo4jExtractor(neo4j_uri, neo4j_user, neo4j_password, database=os.getenv("NEO4J_DATABASE", "crawl4ai"))'
    
    content = re.sub(pattern, replacement, content)
    
    # Write back the patched content
    with open(file_path, 'w') as f:
        f.write(content)
    
    print("✅ Patched crawl4ai_mcp.py to pass database parameter")
    return True

def main():
    print("=== Patching crawl4ai for Neo4j database support ===\n")
    
    # Patch both files
    success1 = patch_direct_neo4j_extractor()
    success2 = patch_crawl4ai_mcp()
    
    if success1 and success2:
        print("\n✅ All patches applied successfully!")
        print("\n📝 The crawl4ai service will now:")
        print("   - Accept NEO4J_DATABASE environment variable")
        print("   - Use the specified database (default: 'crawl4ai')")
        print("   - Work correctly with Neo4j Desktop multi-database setup")
        print("\n🔄 Please restart Claude Code to apply these changes.")
    else:
        print("\n⚠️  Some patches failed. Please check the output above.")

if __name__ == "__main__":
    main()