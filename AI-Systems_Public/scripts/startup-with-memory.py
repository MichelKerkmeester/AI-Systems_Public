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
        cmd = 'echo "MATCH (e:Episodic) RETURN count(e);" | docker exec -i graphiti-neo4j cypher-shell -u neo4j -p password -d neo4j --format plain'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                return int(lines[1])
    except:
        pass
    return 0

def get_recent_memories(limit=3):
    """Get recent memories with categories"""
    memories = []
    try:
        query = f'MATCH (e:Episodic) RETURN e.name as name, e.group_id as cat ORDER BY e.created_at DESC LIMIT {limit};'
        cmd = f'echo "{query}" | docker exec -i graphiti-neo4j cypher-shell -u neo4j -p password -d neo4j --format plain'
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