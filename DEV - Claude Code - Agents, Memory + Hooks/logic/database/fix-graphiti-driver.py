#!/usr/bin/env python3
"""
Fix the Graphiti server to use custom Neo4jDriver with database parameter
"""

import os

# Read the current server file
server_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/mcp-servers/graphiti/graphiti-gemini-mcp/graphiti_gemini_mcp_server.py"

with open(server_path, 'r') as f:
    content = f.read()

# Replace the imports section to include Neo4jDriver
new_imports = """from graphiti_core import Graphiti
from graphiti_core.driver.neo4j_driver import Neo4jDriver
from graphiti_core.embedder.gemini import GeminiEmbedder, GeminiEmbedderConfig"""

content = content.replace("from graphiti_core import Graphiti", new_imports)

# Replace the Graphiti initialization
old_init = """        # Initialize Graphiti
        graphiti = Graphiti(
            uri=neo4j_uri,
            user=neo4j_user,
            password=neo4j_password,
            database=os.getenv("NEO4J_DATABASE", "graphiti"),
            embedder=embedder,
            llm_client=llm_client,
            cross_encoder=reranker,
        )"""

new_init = """        # Create custom Neo4j driver with database parameter
        neo4j_driver = Neo4jDriver(
            uri=neo4j_uri,
            user=neo4j_user,
            password=neo4j_password,
            database=os.getenv("NEO4J_DATABASE", "graphiti")
        )
        
        # Initialize Graphiti with custom driver
        graphiti = Graphiti(
            graph_driver=neo4j_driver,
            embedder=embedder,
            llm_client=llm_client,
            cross_encoder=reranker,
        )"""

content = content.replace(old_init, new_init)

# Write the updated content
with open(server_path, 'w') as f:
    f.write(content)

print("✅ Updated Graphiti server to use custom Neo4jDriver")
print("📝 The server now properly uses the 'graphiti' database")
print("🔄 Please restart Claude Code for changes to take effect")