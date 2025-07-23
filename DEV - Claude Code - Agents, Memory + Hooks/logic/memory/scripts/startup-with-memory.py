#!/usr/bin/env python3
"""
Startup protocol helper that includes memory information
This can be called at conversation start to show memory status
"""

import subprocess
import json
from datetime import datetime

def get_memory_count():
    """Get total memory count from Graphiti"""
    try:
        # Try using neo4j driver first
        from neo4j import GraphDatabase
        
        uri = "neo4j://127.0.0.1:7687"
        database = "graphiti"
        username = "neo4j"
        password = "AQCIbagraydayAQCIba"
        
        driver = GraphDatabase.driver(uri, auth=(username, password))
        
        with driver.session(database=database) as session:
            result = session.run("MATCH (e:Episodic) RETURN count(e) as count")
            record = result.single()
            if record:
                count = record["count"]
                driver.close()
                return count
        
        driver.close()
    except ImportError:
        # Fallback to cypher-shell if neo4j package not available
        try:
            cmd = 'echo "MATCH (e:Episodic) RETURN count(e);" | cypher-shell -a neo4j://127.0.0.1:7687 -u neo4j -p AQCIbagraydayAQCIba -d graphiti --format plain'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                if len(lines) > 1:
                    return int(lines[1])
        except:
            pass
    except:
        pass
    return 0

def get_recent_memories(limit=3):
    """Get recent memories with categories"""
    memories = []
    try:
        # Try using neo4j driver first
        from neo4j import GraphDatabase
        
        uri = "neo4j://127.0.0.1:7687"
        database = "graphiti"
        username = "neo4j"
        password = "AQCIbagraydayAQCIba"
        
        driver = GraphDatabase.driver(uri, auth=(username, password))
        
        with driver.session(database=database) as session:
            query = f'MATCH (e:Episodic) RETURN e.name as name, e.group_id as cat ORDER BY e.created_at DESC LIMIT {limit}'
            result = session.run(query)
            
            for record in result:
                name = record.get("name", "")
                cat = record.get("cat", "")
                # Truncate long names
                if len(name) > 40:
                    name = name[:37] + "..."
                memories.append((name, cat))
        
        driver.close()
    except ImportError:
        # Fallback to cypher-shell if neo4j package not available
        try:
            query = f'MATCH (e:Episodic) RETURN e.name as name, e.group_id as cat ORDER BY e.created_at DESC LIMIT {limit};'
            cmd = f'echo "{query}" | cypher-shell -a neo4j://127.0.0.1:7687 -u neo4j -p AQCIbagraydayAQCIba -d graphiti --format plain'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                for line in lines[1:]:  # Skip header
                    if line.strip():
                        parts = line.split(', ')
                        if len(parts) >= 2:
                            name = parts[0].strip('"')
                            cat = parts[1].strip('"')
                            # Truncate long names
                            if len(name) > 40:
                                name = name[:37] + "..."
                            memories.append((name, cat))
        except:
            pass
    except:
        pass
    return memories

def suggest_search_based_on_context():
    """Suggest a memory search based on current context"""
    # Could analyze git branch, modified files, etc.
    # For now, return a simple suggestion
    suggestions = [
        ('webflow', 3),
        ('security', 2),
        ('pattern', 3)
    ]
    
    # Pick a random suggestion
    import random
    topic, count = random.choice(suggestions)
    return f'/memory search "{topic}" ({count} matches)'

def format_memory_status():
    """Format memory status for startup display"""
    count = get_memory_count()
    recent = get_recent_memories(3)
    suggestion = suggest_search_based_on_context()
    
    # Format recent memories
    if recent:
        recent_str = []
        for name, cat in recent:
            if cat:
                recent_str.append(f"{name} [{cat}]")
            else:
                recent_str.append(name)
        recent_formatted = ", ".join(recent_str[:3])
    else:
        recent_formatted = "No memories yet"
    
    return {
        'count': count,
        'recent': recent_formatted,
        'suggestion': suggestion
    }

if __name__ == "__main__":
    # Get memory status
    status = format_memory_status()
    
    # Output as JSON for easy parsing
    print(json.dumps(status, indent=2))