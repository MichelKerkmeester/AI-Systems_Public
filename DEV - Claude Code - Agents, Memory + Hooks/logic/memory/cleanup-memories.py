#!/usr/bin/env python3
"""
Clean up all memories from Neo4j database
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

def cleanup_memories():
    """Delete all memories from Neo4j database"""
    try:
        print("🧹 Cleaning up Graphiti memories...")
        print("=" * 60)
        
        # Connect to Neo4j
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        
        with driver.session() as session:
            # Count current memories
            count_result = session.run("MATCH (e:Episode) RETURN count(e) as count")
            initial_count = count_result.single()['count']
            
            print(f"\n📊 Found {initial_count} memories to delete")
            
            if initial_count == 0:
                print("✅ Database is already empty!")
                return True
            
            # Show memories that will be deleted
            print("\n📝 Memories to be deleted:")
            print("-" * 60)
            
            episodes = session.run("""
                MATCH (e:Episode)
                RETURN e.name as name, e.source as source, e.created_at as created_at
                ORDER BY e.created_at DESC
            """)
            
            for i, record in enumerate(episodes, 1):
                print(f"{i}. {record['name']}")
                print(f"   Source: {record['source']}")
                print(f"   Created: {record['created_at']}")
            
            print("-" * 60)
            
            # Confirm deletion
            response = input("\n⚠️  Delete all memories? This cannot be undone! [y/N]: ")
            
            if response.lower() != 'y':
                print("\n❌ Cleanup cancelled")
                return False
            
            # Delete all Episode nodes
            print("\n🗑️  Deleting all Episode nodes...")
            session.run("MATCH (e:Episode) DELETE e")
            
            # Also clean up any orphaned Node entities
            print("🗑️  Cleaning up orphaned entities...")
            session.run("MATCH (n:Node) WHERE NOT (n)-[:RELATES_TO]-() DELETE n")
            
            # Verify deletion
            final_count_result = session.run("MATCH (e:Episode) RETURN count(e) as count")
            final_count = final_count_result.single()['count']
            
            if final_count == 0:
                print(f"\n✅ Successfully deleted {initial_count} memories!")
                print("🎯 Database is now empty and ready for fresh memories")
            else:
                print(f"\n⚠️  Warning: {final_count} memories still remain")
                
        driver.close()
        
        print("\n" + "=" * 60)
        print("✅ Cleanup complete!")
        print("\nNext steps:")
        print("1. Start adding real project memories")
        print("2. Use: /memory manual 'Your first real memory'")
        print("3. Or let auto-capture work with patterns like DECISION:")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during cleanup: {e}")
        return False

if __name__ == "__main__":
    success = cleanup_memories()
    sys.exit(0 if success else 1)