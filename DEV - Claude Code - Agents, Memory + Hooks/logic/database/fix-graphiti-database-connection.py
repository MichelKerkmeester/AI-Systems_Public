#!/usr/bin/env python3
"""
Fix Graphiti to use the correct database parameter.
The Graphiti constructor needs the database parameter passed.
"""

import os
import re

def fix_graphiti_server():
    """Update Graphiti server to use database parameter."""
    
    server_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/graphiti/graphiti-gemini-mcp/graphiti_gemini_mcp_server.py"
    
    print("🔧 Fixing Graphiti server to use database parameter...")
    
    # Read the file
    with open(server_path, 'r') as f:
        content = f.read()
    
    # Check if database parameter is already there
    if "database=" in content and "graphiti = Graphiti(" in content:
        print("✅ Database parameter already exists in Graphiti initialization")
        return
    
    # Find the Graphiti initialization and add database parameter
    pattern = r'(graphiti = Graphiti\(\s*uri=neo4j_uri,\s*user=neo4j_user,\s*password=neo4j_password,)'
    
    if re.search(pattern, content):
        # Add database parameter after password
        replacement = r'\1\n            database=os.getenv("NEO4J_DATABASE", "graphiti"),'
        new_content = re.sub(pattern, replacement, content)
        
        # Write back
        with open(server_path, 'w') as f:
            f.write(new_content)
        
        print("✅ Added database parameter to Graphiti initialization")
        print("   - Will use NEO4J_DATABASE environment variable")
        print("   - Defaults to 'graphiti' if not set")
    else:
        print("❌ Could not find Graphiti initialization pattern")
        print("   Looking for manual fix location...")
        
        # Find line numbers for manual reference
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "graphiti = Graphiti(" in line:
                print(f"   Found at line {i+1}")
                print(f"   Add: database=os.getenv('NEO4J_DATABASE', 'graphiti'),")

if __name__ == "__main__":
    fix_graphiti_server()