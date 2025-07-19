#!/usr/bin/env python3
"""
Quick script to check Neo4j memories directly
"""

import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Neo4j connection details
NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'password')

def check_memories():
    """Check memories in Neo4j database"""
    try:
        # Connect to Neo4j
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        
        print(f"🔗 Connecting to Neo4j at {NEO4J_URI}...")
        
        with driver.session() as session:
            # Count total episodes
            count_result = session.run("MATCH (e:Episode) RETURN count(e) as count")
            count = count_result.single()['count']
            
            print(f"\n📊 Total Memories: {count}")
            
            if count > 0:
                print("\n📝 Recent Memories:")
                print("-" * 80)
                
                # Get recent episodes
                result = session.run("""
                    MATCH (e:Episode)
                    RETURN e.name as name, 
                           e.content as content,
                           e.source as source,
                           e.created_at as created_at
                    ORDER BY e.created_at DESC
                    LIMIT 5
                """)
                
                for i, record in enumerate(result, 1):
                    print(f"\n{i}. {record['name'] or 'Untitled'}")
                    print(f"   Source: {record['source'] or 'Unknown'}")
                    print(f"   Created: {record['created_at'] or 'Unknown'}")
                    if record['content']:
                        preview = record['content'][:100] + "..." if len(record['content']) > 100 else record['content']
                        print(f"   Content: {preview}")
                
                print("\n" + "-" * 80)
                
                # Show category breakdown
                category_result = session.run("""
                    MATCH (e:Episode)
                    RETURN e.source as category, count(e) as count
                    ORDER BY count DESC
                """)
                
                print("\n📈 Memories by Category:")
                for record in category_result:
                    print(f"   {record['category']}: {record['count']}")
            else:
                print("\n❌ No memories found in Neo4j")
                print("\n💡 To add memories:")
                print("   1. Restart Claude Code CLI")
                print("   2. Use: /memory manual Your first memory")
                print("   3. Or trigger patterns like 'DECISION: ...'")
        
        driver.close()
        print("\n✅ Neo4j check complete")
        
    except Exception as e:
        print(f"\n❌ Error connecting to Neo4j: {e}")
        print("\n🔧 Troubleshooting:")
        print("   1. Check if Neo4j is running: neo4j status")
        print("   2. Verify credentials in .env file")
        print("   3. Check connection URI (default: bolt://localhost:7687)")

if __name__ == "__main__":
    check_memories()