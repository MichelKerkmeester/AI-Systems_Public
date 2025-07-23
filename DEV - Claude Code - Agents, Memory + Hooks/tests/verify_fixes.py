#!/usr/bin/env python3
"""Verify Graphiti and Crawl4AI fixes after restarting Claude Code."""

import asyncio
from datetime import datetime
from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "AQCIbagraydayAQCIba"
DATABASE = "memory"

print("🔍 Verifying Neo4j Integration Fixes...")
print("=" * 60)

async def verify_fixes():
    """Check if data exists in Neo4j after running MCP tools."""
    
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    try:
        with driver.session(database=DATABASE) as session:
            print(f"\n✅ Connected to database: {DATABASE}")
            
            # Check for any nodes
            result = session.run("MATCH (n) RETURN count(n) as total, labels(n)[0] as label LIMIT 10")
            total = 0
            labels_found = []
            
            for record in result:
                if record["total"] > 0:
                    total = record["total"]
                if record["label"]:
                    labels_found.append(record["label"])
            
            print(f"\n📊 Database Statistics:")
            print(f"   Total nodes: {total}")
            
            if total > 0:
                # Get all labels
                result = session.run("CALL db.labels() YIELD label RETURN label ORDER BY label")
                all_labels = [record["label"] for record in result]
                print(f"   Node types: {', '.join(all_labels)}")
                
                # Check for Graphiti data
                print("\n🧠 Graphiti Data:")
                result = session.run("MATCH (e:Episode) RETURN count(e) as count")
                episode_count = result.single()["count"]
                print(f"   Episodes: {episode_count}")
                
                if episode_count > 0:
                    result = session.run("MATCH (e:Episode) RETURN e.name as name ORDER BY e.created_at DESC LIMIT 3")
                    print("   Recent episodes:")
                    for record in result:
                        print(f"     - {record['name']}")
                
                # Check for Crawl4AI data
                print("\n🕷️ Crawl4AI Data:")
                result = session.run("MATCH (r:Repository) RETURN count(r) as count")
                repo_count = result.single()["count"]
                print(f"   Repositories: {repo_count}")
                
                if repo_count > 0:
                    result = session.run("MATCH (r:Repository) RETURN r.name as name, r.url as url LIMIT 3")
                    print("   Repositories:")
                    for record in result:
                        print(f"     - {record['name']} ({record['url']})")
                    
                    # Get file count
                    result = session.run("MATCH (f:File) RETURN count(f) as count")
                    file_count = result.single()["count"]
                    print(f"   Files analyzed: {file_count}")
                
                print("\n✅ Database is receiving data from MCP tools!")
            else:
                print("\n⚠️  Database is empty. Please run the following MCP tools:")
                print("   1. mcp__graphiti-gemini__add_episode - to add test memories")
                print("   2. mcp__crawl4ai-rag__parse_github_repository - to parse a GitHub repo")
                
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        driver.close()
    
    print(f"\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    asyncio.run(verify_fixes())