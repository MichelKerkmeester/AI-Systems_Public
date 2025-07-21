#!/usr/bin/env python3
"""
Direct Neo4j queries to check Graphiti memories
"""

from neo4j import GraphDatabase
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Neo4jGraphitiExplorer:
    def __init__(self):
        self.uri = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
        self.user = os.getenv('NEO4J_USER', 'neo4j')
        self.password = os.getenv('NEO4J_PASSWORD', 'password')
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
    
    def close(self):
        self.driver.close()
    
    def check_episodes(self):
        """Get all episodes with their details"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (e:Episode)
                RETURN e.name as name, 
                       e.created_at as created_at,
                       e.source as source,
                       e.group_id as group_id,
                       e.content as content
                ORDER BY e.created_at DESC
                LIMIT 20
            """)
            
            print("\n📚 EPISODES IN GRAPHITI")
            print("=" * 80)
            
            for record in result:
                print(f"\n🔹 {record['name']}")
                print(f"   Created: {record['created_at']}")
                print(f"   Source: {record['source']}")
                print(f"   Group: {record['group_id'] or 'none'}")
                if record['content']:
                    print(f"   Content: {record['content'][:100]}...")
    
    def check_entities(self):
        """Get all entities (extracted from episodes)"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n:Entity)
                RETURN n.name as name, 
                       n.summary as summary,
                       labels(n) as types
                ORDER BY n.name
                LIMIT 20
            """)
            
            print("\n🧠 ENTITIES EXTRACTED")
            print("=" * 80)
            
            for record in result:
                print(f"\n🔸 {record['name']}")
                print(f"   Types: {', '.join(record['types'])}")
                if record['summary']:
                    print(f"   Summary: {record['summary'][:100]}...")
    
    def check_relationships(self):
        """Get relationships between entities"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (n1:Entity)-[r]-(n2:Entity)
                RETURN n1.name as source, 
                       type(r) as relationship,
                       n2.name as target,
                       r.fact as fact
                LIMIT 20
            """)
            
            print("\n🔗 RELATIONSHIPS")
            print("=" * 80)
            
            for record in result:
                print(f"\n{record['source']} --[{record['relationship']}]--> {record['target']}")
                if record.get('fact'):
                    print(f"   Fact: {record['fact']}")
    
    def check_database_stats(self):
        """Get database statistics"""
        with self.driver.session() as session:
            # Count nodes by type
            node_counts = session.run("""
                MATCH (n)
                RETURN labels(n)[0] as label, count(n) as count
                ORDER BY count DESC
            """)
            
            # Count relationships
            rel_count = session.run("""
                MATCH ()-[r]->()
                RETURN count(r) as count
            """).single()['count']
            
            print("\n📊 DATABASE STATISTICS")
            print("=" * 80)
            
            for record in node_counts:
                print(f"{record['label']}: {record['count']} nodes")
            
            print(f"\nTotal relationships: {rel_count}")
    
    def search_memories(self, query):
        """Search for specific memories"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (e:Episode)
                WHERE e.name CONTAINS $query OR e.content CONTAINS $query
                RETURN e.name as name, e.created_at as created_at
                ORDER BY e.created_at DESC
                LIMIT 10
            """, query=query)
            
            print(f"\n🔍 SEARCH RESULTS FOR: '{query}'")
            print("=" * 80)
            
            for record in result:
                print(f"• {record['name']}")
                print(f"  Created: {record['created_at']}")


def main():
    print("🚀 Graphiti Neo4j Explorer")
    print("Connecting to Neo4j database...\n")
    
    explorer = Neo4jGraphitiExplorer()
    
    try:
        # Check database stats first
        explorer.check_database_stats()
        
        # Show episodes
        explorer.check_episodes()
        
        # Show extracted entities
        explorer.check_entities()
        
        # Show relationships
        explorer.check_relationships()
        
        # Example searches
        print("\n" + "=" * 80)
        explorer.search_memories("security")
        explorer.search_memories("pattern")
        
    finally:
        explorer.close()
        print("\n✅ Done!")


if __name__ == "__main__":
    main()