#!/usr/bin/env python3
"""
Initialize Neo4j database schema for Graphiti
Creates required fulltext indexes for nodes and relationships
"""

import os
import sys
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j connection details
NEO4J_URI = os.getenv('NEO4J_URI', 'neo4j://127.0.0.1:7687')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

def initialize_schema():
    """Initialize Neo4j schema with required indexes"""
    try:
        print(f"🔗 Connecting to Neo4j Desktop at {NEO4J_URI}...")
        
        # Connect to Neo4j
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        
        with driver.session() as session:
            # Check existing indexes
            print("\n📊 Checking existing indexes...")
            existing_indexes = session.run("SHOW INDEXES")
            index_names = [record['name'] for record in existing_indexes]
            
            print(f"Found {len(index_names)} existing indexes")
            
            # Create node fulltext index if not exists
            if 'node_name_and_summary' not in index_names:
                print("\n🔨 Creating node fulltext index: node_name_and_summary")
                session.run("""
                    CREATE FULLTEXT INDEX node_name_and_summary IF NOT EXISTS
                    FOR (n:Node) 
                    ON EACH [n.name, n.summary]
                """)
                print("✅ Node index created")
            else:
                print("✅ Node index already exists")
            
            # Create edge fulltext index if not exists
            if 'edge_name_and_fact' not in index_names:
                print("\n🔨 Creating edge fulltext index: edge_name_and_fact")
                session.run("""
                    CREATE FULLTEXT INDEX edge_name_and_fact IF NOT EXISTS
                    FOR ()-[r:RELATES_TO]-() 
                    ON EACH [r.name, r.fact]
                """)
                print("✅ Edge index created")
            else:
                print("✅ Edge index already exists")
            
            # Create additional indexes for Episode nodes
            print("\n🔨 Creating Episode node indexes...")
            
            # Index for Episode nodes by created_at
            session.run("""
                CREATE INDEX episode_created_at IF NOT EXISTS
                FOR (e:Episode) 
                ON (e.created_at)
            """)
            
            # Index for Episode nodes by name
            session.run("""
                CREATE INDEX episode_name IF NOT EXISTS
                FOR (e:Episode) 
                ON (e.name)
            """)
            
            print("✅ Episode indexes created")
            
            # Verify schema
            print("\n🔍 Verifying schema...")
            
            # Check node labels
            labels_result = session.run("CALL db.labels()")
            labels = [record['label'] for record in labels_result]
            print(f"\nNode labels: {', '.join(labels) if labels else 'None'}")
            
            # Check relationship types
            rel_types_result = session.run("CALL db.relationshipTypes()")
            rel_types = [record['relationshipType'] for record in rel_types_result]
            print(f"Relationship types: {', '.join(rel_types) if rel_types else 'None'}")
            
            # Final index check
            print("\n📊 Final index status:")
            final_indexes = session.run("SHOW INDEXES")
            for record in final_indexes:
                print(f"   - {record['name']} ({record['state']})")
            
        driver.close()
        
        print("\n✅ Neo4j schema initialization complete!")
        print("\n🎉 Graphiti is now ready to use!")
        print("\nNext steps:")
        print("1. In Claude Code: /memory manual 'Your first memory'")
        print("2. Or trigger auto-capture: 'DECISION: Important architectural choice'")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error initializing schema: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure Neo4j Desktop is running")
        print("2. Check if the database is started in Neo4j Desktop")
        print("3. Verify credentials in .env file")
        print("4. Check if URI matches Neo4j Desktop settings")
        return False

if __name__ == "__main__":
    success = initialize_schema()
    sys.exit(0 if success else 1)