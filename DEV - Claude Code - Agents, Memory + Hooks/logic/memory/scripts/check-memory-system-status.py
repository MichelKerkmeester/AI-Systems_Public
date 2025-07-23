#!/usr/bin/env python3
"""
Check Memory System Status
Verifies the current state of the memory filter system before deployment
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def check_memory_filter_version():
    """Check which memory filter is currently active"""
    filter_path = Path(__file__).parent.parent / "crawl4ai-memory-filter.py"
    
    if not filter_path.exists():
        print("❌ Memory filter not found at expected location")
        return None
    
    with open(filter_path, 'r') as f:
        content = f.read()
    
    # Check for optimized version markers
    if "OptimizedCrawl4AIMemoryFilter" in content:
        print("✅ Optimized memory filter detected")
        
        # Extract threshold
        import re
        neo4j_match = re.search(r"'neo4j':\s*([\d.]+)", content)
        if neo4j_match:
            threshold = float(neo4j_match.group(1))
            print(f"   Neo4j threshold: {threshold}")
            return "optimized", threshold
    else:
        print("⚠️  Original memory filter detected")
        # Check original threshold
        import re
        neo4j_match = re.search(r"neo4j.*?0\.([\d]+)", content)
        if neo4j_match:
            threshold = float(f"0.{neo4j_match.group(1)}")
            print(f"   Neo4j threshold: {threshold}")
            return "original", threshold
    
    return "unknown", 0.0

def check_neo4j_connection():
    """Verify Neo4j database connectivity"""
    try:
        from py2neo import Graph
        
        # Try to connect
        graph = Graph("bolt://localhost:7687", auth=("neo4j", os.getenv("NEO4J_PASSWORD", "password")))
        
        # Run test query
        result = graph.run("MATCH (n) RETURN count(n) as count LIMIT 1").data()
        if result:
            print(f"✅ Neo4j connection successful (nodes: {result[0]['count']})")
            return True
    except ImportError:
        print("⚠️  py2neo not installed - Neo4j connection not tested")
        return None
    except Exception as e:
        print(f"❌ Neo4j connection failed: {e}")
        return False

def check_supabase_connection():
    """Verify Supabase connectivity"""
    if not os.getenv("SUPABASE_URL") or not os.getenv("SUPABASE_KEY"):
        print("⚠️  Supabase credentials not configured")
        return None
    
    print("✅ Supabase credentials found")
    return True

def check_running_processes():
    """Check if memory processing threads are running"""
    try:
        import psutil
        
        python_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                cmdline = proc.info.get('cmdline', [])
                if any('memory' in str(arg) for arg in cmdline):
                    python_processes.append(proc)
        
        if python_processes:
            print(f"✅ Found {len(python_processes)} memory-related Python processes")
            return True
        else:
            print("⚠️  No active memory processing detected")
            return False
    except ImportError:
        print("⚠️  psutil not installed - process check skipped")
        return None

def check_recent_activity():
    """Check for recent memory processing activity"""
    # Check for log files
    log_locations = [
        "/var/log/claude-memory.log",
        Path.home() / ".claude" / "logs" / "memory.log",
        Path(__file__).parent.parent.parent.parent / "logs" / "memory.log"
    ]
    
    for log_path in log_locations:
        if Path(log_path).exists():
            stat = os.stat(log_path)
            last_modified = datetime.fromtimestamp(stat.st_mtime)
            age_minutes = (datetime.now() - last_modified).total_seconds() / 60
            
            if age_minutes < 60:
                print(f"✅ Recent activity in {log_path} ({age_minutes:.0f} min ago)")
                return True
            else:
                print(f"⚠️  No recent activity in {log_path} ({age_minutes:.0f} min ago)")
    
    return False

def generate_status_report():
    """Generate comprehensive status report"""
    print("\n" + "="*60)
    print("MEMORY SYSTEM STATUS REPORT")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("="*60 + "\n")
    
    # Check filter version
    print("1. Memory Filter Version")
    print("-" * 30)
    version, threshold = check_memory_filter_version()
    
    # Check connections
    print("\n2. Database Connections")
    print("-" * 30)
    neo4j_ok = check_neo4j_connection()
    supabase_ok = check_supabase_connection()
    
    # Check processes
    print("\n3. Running Processes")
    print("-" * 30)
    processes_ok = check_running_processes()
    
    # Check activity
    print("\n4. Recent Activity")
    print("-" * 30)
    activity_ok = check_recent_activity()
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    status = "READY" if all([
        version in ["original", "optimized"],
        neo4j_ok is not False,
        supabase_ok is not False
    ]) else "NOT READY"
    
    print(f"\nDeployment Status: {status}")
    
    if version == "original" and threshold < 0.8:
        print("\n📌 Recommendation: Deploy optimized filter to reduce Neo4j costs")
    elif version == "optimized" and threshold >= 0.8:
        print("\n✅ Optimized filter already deployed!")
    
    # Export status
    status_data = {
        "timestamp": datetime.now().isoformat(),
        "filter_version": version,
        "neo4j_threshold": threshold,
        "neo4j_connected": neo4j_ok,
        "supabase_configured": supabase_ok,
        "processes_running": processes_ok,
        "recent_activity": activity_ok,
        "deployment_ready": status == "READY"
    }
    
    status_file = Path(__file__).parent / "memory-status.json"
    with open(status_file, 'w') as f:
        json.dump(status_data, f, indent=2)
    
    print(f"\nStatus exported to: {status_file}")
    
    return status == "READY"

if __name__ == "__main__":
    ready = generate_status_report()
    sys.exit(0 if ready else 1)