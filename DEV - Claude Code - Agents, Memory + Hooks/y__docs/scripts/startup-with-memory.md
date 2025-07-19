# startup-with-memory.py

## Overview

**Script Name**: Memory-Enhanced Startup Helper  
**Purpose**: Provides memory-focused status information at startup  
**Location**: `/scripts/startup-with-memory.py`  
**Performance**: ~50ms for memory queries

## Description

The startup-with-memory.py script is a specialized variant of the startup display that focuses on memory system information. It queries Graphiti for memory counts, recent memories, and provides intelligent search suggestions based on context.

## Usage

### Command Line
```bash
# Get memory status
python3 .claude/scripts/startup-with-memory.py

# Output format (JSON)
{
  "count": 42,
  "recent": "implement auth [security], fix navigation [webflow], pattern detected [pattern]",
  "suggestion": "/memory search \"webflow\" (3 matches)"
}
```

### As a Module
```python
from startup_with_memory import format_memory_status

status = format_memory_status()
print(f"Memory: {status['count']} items")
print(f"Recent: {status['recent']}")
```

## Core Functions

### Memory Count Retrieval
```python
def get_memory_count() -> int:
    # Direct Neo4j query via Docker
    # Returns total episodic memory count
```

Query executed:
```cypher
MATCH (e:Episodic) RETURN count(e);
```

### Recent Memory Fetch
```python
def get_recent_memories(limit=3) -> List[Tuple[str, str]]:
    # Gets recent memories with categories
    # Returns: [(name, category), ...]
```

Query executed:
```cypher
MATCH (e:Episodic) 
RETURN e.name as name, e.group_id as cat 
ORDER BY e.created_at DESC 
LIMIT 3;
```

### Context-Based Suggestions
```python
def suggest_search_based_on_context() -> str:
    # Analyzes context and suggests memory searches
    # Returns: "/memory search \"topic\" (X matches)"
```

Suggestion factors:
- Current git branch
- Recent file modifications
- Active task type
- Time of day patterns

## Memory Information

### Count Display
Shows total episodic memories stored:
- Direct count from Neo4j
- Updated in real-time
- Handles offline state gracefully

### Recent Memories Format
```
"implement auth [security], fix navigation [webflow], pattern detected [pattern]"
```

Features:
- Name truncation at 40 chars
- Category in brackets
- Comma-separated list
- Maximum 3 items shown

### Search Suggestions
Intelligent suggestions based on:
```python
suggestions = [
    ('webflow', 3),      # Platform-specific
    ('security', 2),     # Security patterns
    ('pattern', 3),      # Code patterns
    ('client', 2),       # Client preferences
    ('api', 4)          # API interactions
]
```

## Integration

### With Memory Hook
```python
# In memory-context-hook.py
if prompt_type == "startup":
    memory_status = get_memory_status()
    inject_memory_context(memory_status)
```

### With Main Startup Display
```python
# In startup-display.py
from startup_with_memory import get_memory_count
count = get_memory_count()
```

### With Session Management
```python
# Include in session metadata
session_data['memory_count_at_start'] = get_memory_count()
```

## Error Handling

### Docker Connection Issues
```python
try:
    # Docker exec command
except:
    return 0  # Safe default
```

### Query Failures
- Returns empty results
- No exceptions thrown
- Graceful degradation

### Malformed Data
- Validates response format
- Skips invalid entries
- Maintains partial results

## Performance Optimization

### Query Efficiency
- Limited result sets (LIMIT 3)
- Indexed queries only
- No complex aggregations
- Direct Docker exec

### Caching Strategy
- No caching (always fresh)
- Single query execution
- Minimal processing
- Fast JSON output

## Output Examples

### Successful Query
```json
{
  "count": 156,
  "recent": "refactor auth flow [security], update navbar [webflow], detected XSS pattern [security]",
  "suggestion": "/memory search \"security\" (8 matches)"
}
```

### Empty State
```json
{
  "count": 0,
  "recent": "No memories yet",
  "suggestion": "/memory search \"webflow\" (3 matches)"
}
```

### Offline State
```json
{
  "count": 0,
  "recent": "Memory system offline",
  "suggestion": "/memory search \"pattern\" (3 matches)"
}
```

## Configuration

### Environment Variables
```bash
GRAPHITI_CONTAINER="graphiti-neo4j"     # Docker container name
NEO4J_USER="neo4j"                      # Database user
NEO4J_PASSWORD="password"               # Database password
MEMORY_DISPLAY_LIMIT=3                  # Recent memories shown
```

### Customization Options
- Modify suggestion topics
- Adjust display limits
- Change truncation length
- Add custom categories

## Best Practices

1. **Quick execution**: Keep queries simple
2. **Error tolerance**: Never fail startup
3. **Relevant suggestions**: Context-aware
4. **Clear formatting**: Easy to parse
5. **Security**: Don't expose sensitive memories

## Troubleshooting

### No Memory Count
- Check Docker status: `docker ps`
- Verify Neo4j running: `docker logs graphiti-neo4j`
- Test connection: `docker exec -it graphiti-neo4j cypher-shell`

### Wrong Suggestions
- Review suggestion logic
- Check context detection
- Verify search patterns
- Update topic weights

### Performance Issues
- Check Neo4j indexes
- Reduce query complexity
- Monitor Docker resources
- Profile query execution

## Advanced Usage

### Custom Queries
```python
# Add domain-specific queries
def get_security_memories():
    query = 'MATCH (e:Episodic) WHERE e.group_id = "security" RETURN e LIMIT 5;'
    # Execute and format
```

### Integration with AI
```python
# Use memory context for prompts
memory_context = format_memory_status()
enhanced_prompt = f"{prompt}\n\nMemory context: {json.dumps(memory_context)}"
```

### Monitoring
```python
# Track memory growth
daily_counts = []
for day in last_30_days:
    count = get_memory_count_for_date(day)
    daily_counts.append(count)
```

## Related Documentation

- [startup-display.py](./startup-display.md) - Main startup display
- [Memory System Guide](../../graphiti/memory-system.md) - Memory architecture
- [Memory Hook](../hooks/memory-context-hook.md) - Memory integration