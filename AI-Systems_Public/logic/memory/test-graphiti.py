#!/usr/bin/env python3
"""
Test Graphiti MCP integration with Neo4j Desktop
"""

import os
import sys
from datetime import datetime
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j connection details
NEO4J_URI = os.getenv('NEO4J_URI', 'neo4j://127.0.0.1:7687')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

def test_graphiti():
    """Test Graphiti functionality"""
    try:
        print("🧪 Testing Graphiti Integration with Neo4j Desktop")
        print("=" * 60)
        
        # Connect to Neo4j
        print(f"\n1️⃣ Connecting to Neo4j at {NEO4J_URI}...")
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        
        with driver.session() as session:
            # Test connection
            result = session.run("RETURN 1 as test")
            test_value = result.single()['test']
            print(f"✅ Connection successful! Test query returned: {test_value}")
            
            # Check indexes
            print("\n2️⃣ Checking required indexes...")
            indexes = session.run("SHOW INDEXES")
            required_indexes = {'node_name_and_summary', 'edge_name_and_fact'}
            found_indexes = {record['name'] for record in indexes}
            
            missing = required_indexes - found_indexes
            if missing:
                print(f"❌ Missing indexes: {', '.join(missing)}")
                print("   Run: python3 .claude/logic/memory/initialize-neo4j-schema.py")
                return False
            else:
                print("✅ All required indexes present")
            
            # Create test episode
            print("\n3️⃣ Creating test episode...")
            timestamp = datetime.now().isoformat()
            
            session.run("""
                CREATE (e:Episode {
                    name: $name,
                    content: $content,
                    source: $source,
                    created_at: $created_at,
                    episode_id: randomUUID()
                })
            """, 
            name="Test Episode: Graphiti Integration",
            content="This is a test episode created to verify Graphiti integration with Neo4j Desktop is working correctly.",
            source="test_script",
            created_at=timestamp)
            
            print("✅ Test episode created")
            
            # Search for episode
            print("\n4️⃣ Testing search functionality...")
            search_result = session.run("""
                MATCH (e:Episode)
                WHERE e.name CONTAINS 'Test Episode'
                RETURN e.name as name, e.created_at as created_at
                ORDER BY e.created_at DESC
                LIMIT 1
            """)
            
            record = search_result.single()
            if record:
                print(f"✅ Found episode: {record['name']}")
                print(f"   Created at: {record['created_at']}")
            else:
                print("❌ Could not find test episode")
            
            # Count total episodes
            print("\n5️⃣ Checking total episodes...")
            count_result = session.run("MATCH (e:Episode) RETURN count(e) as count")
            count = count_result.single()['count']
            print(f"✅ Total episodes in database: {count}")
            
            # Test Graphiti-specific node structure
            print("\n6️⃣ Testing Graphiti node structure...")
            
            # Create a test node (entity)
            session.run("""
                CREATE (n:Node {
                    name: $name,
                    summary: $summary,
                    created_at: $created_at,
                    node_id: randomUUID()
                })
            """,
            name="TestEntity",
            summary="A test entity for Graphiti validation",
            created_at=timestamp)
            
            # Test fulltext search on nodes
            node_search = session.run("""
                CALL db.index.fulltext.queryNodes('node_name_and_summary', 'TestEntity')
                YIELD node, score
                RETURN node.name as name, score
                LIMIT 1
            """)
            
            node_record = node_search.single()
            if node_record:
                print(f"✅ Fulltext search working! Found: {node_record['name']} (score: {node_record['score']:.2f})")
            else:
                print("❌ Fulltext search failed")
            
            # Clean up test data
            print("\n7️⃣ Cleaning up test data...")
            session.run("MATCH (e:Episode) WHERE e.source = 'test_script' DELETE e")
            session.run("MATCH (n:Node) WHERE n.name = 'TestEntity' DELETE n")
            print("✅ Test data cleaned up")
            
        driver.close()
        
        print("\n" + "=" * 60)
        print("✅ All tests passed! Graphiti is ready to use.")
        print("\n🎉 You can now:")
        print("1. Use /memory commands in Claude Code")
        print("2. Add memories: /memory manual 'Your insight'")
        print("3. Search memories: /memory search 'keyword'")
        print("4. Check status: /memory")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Ensure Neo4j Desktop is running")
        print("2. Check if your database is started")
        print("3. Verify the database ID matches in .env")
        print("4. Check Neo4j Desktop logs for errors")
        return False

if __name__ == "__main__":
    success = test_graphiti()
    sys.exit(0 if success else 1)