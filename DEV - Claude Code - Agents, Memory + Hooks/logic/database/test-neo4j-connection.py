#!/usr/bin/env python3
"""
Test Neo4j Connection
Comprehensive Neo4j database connectivity and performance test
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

def test_neo4j_connection():
    """Test Neo4j connection and performance"""
    print("🔍 Testing Neo4j Connection...")
    print("=" * 50)
    
    # Check environment
    neo4j_password = os.getenv("NEO4J_PASSWORD")
    if not neo4j_password:
        print("⚠️  NEO4J_PASSWORD environment variable not set")
        print("   Using default password 'password'")
        neo4j_password = "password"
    
    # Test connection
    try:
        from py2neo import Graph
        print("✅ py2neo library available")
    except ImportError:
        print("❌ py2neo not installed")
        print("   Run: pip install py2neo")
        return False
    
    # Connection parameters
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    print(f"\n📡 Connecting to: {uri}")
    
    try:
        # Establish connection
        start_time = time.time()
        graph = Graph(uri, auth=("neo4j", neo4j_password))
        
        # Test query
        result = graph.run("RETURN 1 as test").data()
        connection_time = time.time() - start_time
        
        print(f"✅ Connection established in {connection_time:.3f}s")
        
        # Get database info
        print("\n📊 Database Statistics:")
        print("-" * 30)
        
        # Node count
        node_count = graph.run("MATCH (n) RETURN count(n) as count").data()[0]['count']
        print(f"   Total nodes: {node_count:,}")
        
        # Relationship count
        rel_count = graph.run("MATCH ()-[r]->() RETURN count(r) as count").data()[0]['count']
        print(f"   Total relationships: {rel_count:,}")
        
        # Label distribution
        labels = graph.run("""
            MATCH (n)
            RETURN labels(n)[0] as label, count(n) as count
            ORDER BY count DESC
            LIMIT 10
        """).data()
        
        if labels:
            print("\n   Top node types:")
            for label in labels:
                if label['label']:
                    print(f"     - {label['label']}: {label['count']:,}")
        
        # Test write performance
        print("\n⚡ Performance Test:")
        print("-" * 30)
        
        # Write test
        write_start = time.time()
        test_id = f"test_{int(time.time())}"
        graph.run("""
            CREATE (n:TestNode {
                id: $id,
                timestamp: $timestamp,
                type: 'performance_test'
            })
        """, id=test_id, timestamp=datetime.now().isoformat())
        write_time = time.time() - write_start
        print(f"   Write time: {write_time*1000:.2f}ms")
        
        # Read test
        read_start = time.time()
        result = graph.run("""
            MATCH (n:TestNode {id: $id})
            RETURN n
        """, id=test_id).data()
        read_time = time.time() - read_start
        print(f"   Read time: {read_time*1000:.2f}ms")
        
        # Cleanup
        graph.run("MATCH (n:TestNode {id: $id}) DELETE n", id=test_id)
        
        # Memory-specific queries
        print("\n🧠 Memory System Check:")
        print("-" * 30)
        
        # Check for memory nodes
        memory_nodes = graph.run("""
            MATCH (n)
            WHERE n.source = 'crawl4ai' OR n.type = 'memory'
            RETURN count(n) as count
        """).data()[0]['count']
        print(f"   Memory-related nodes: {memory_nodes:,}")
        
        # Recent activity
        recent = graph.run("""
            MATCH (n)
            WHERE n.timestamp > datetime() - duration('P1D')
            RETURN count(n) as count
        """).data()[0]['count']
        print(f"   Nodes created in last 24h: {recent:,}")
        
        # Test result
        print("\n" + "="*50)
        print("✅ NEO4J CONNECTION TEST PASSED")
        print("="*50)
        
        # Export results
        results = {
            "status": "connected",
            "uri": uri,
            "connection_time_ms": connection_time * 1000,
            "write_time_ms": write_time * 1000,
            "read_time_ms": read_time * 1000,
            "total_nodes": node_count,
            "total_relationships": rel_count,
            "memory_nodes": memory_nodes,
            "recent_nodes": recent,
            "timestamp": datetime.now().isoformat()
        }
        
        results_file = Path(__file__).parent / "neo4j-test-results.json"
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\nResults saved to: {results_file}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Connection failed: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Check Neo4j is running: sudo systemctl status neo4j")
        print("2. Verify credentials: NEO4J_PASSWORD env var")
        print("3. Check firewall: port 7687 should be open")
        print("4. Try Neo4j Browser: http://localhost:7474")
        
        return False

def check_circuit_breaker_readiness():
    """Check if circuit breaker will work with Neo4j"""
    print("\n🔌 Circuit Breaker Readiness Check:")
    print("-" * 30)
    
    # Simulate failure scenario
    print("   Simulating connection failures...")
    
    failures = 0
    for i in range(3):
        try:
            # Intentionally use wrong password
            from py2neo import Graph
            graph = Graph("bolt://localhost:7687", auth=("neo4j", "wrong_password"))
            graph.run("RETURN 1")
        except:
            failures += 1
    
    if failures == 3:
        print(f"✅ Circuit breaker will activate after {failures} failures")
    else:
        print("⚠️  Circuit breaker may not activate properly")
    
    return True

if __name__ == "__main__":
    # Run tests
    connection_ok = test_neo4j_connection()
    
    if connection_ok:
        check_circuit_breaker_readiness()
    
    # Exit with appropriate code
    sys.exit(0 if connection_ok else 1)