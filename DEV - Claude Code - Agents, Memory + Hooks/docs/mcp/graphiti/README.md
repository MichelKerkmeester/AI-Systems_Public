# Graphiti MCP Documentation

## Overview

Graphiti is a memory management MCP server that provides persistent, searchable memory storage using Neo4j. It enables Claude to maintain context across sessions, store facts, and retrieve relevant information when needed.

## Key Features

- **Episodic Memory**: Store conversation episodes with temporal context
- **Knowledge Graph**: Maintain relationships between concepts and facts
- **Semantic Search**: Find relevant memories based on meaning, not just keywords
- **Group Organization**: Organize memories by project or context groups

## Available Tools

### 1. `mcp__graphiti-gemini__add_episode`
Add new memories to the knowledge graph.

**Parameters:**
- `data`: Episode data object containing:
  - `name`: Title or summary of the episode
  - `episode_body`: The content to remember
  - `group_id`: Optional grouping identifier
  - `source`: Source identifier (default: "mcp_client")
  - `source_description`: Source description
  - `valid_at`: ISO timestamp when the episode occurred

**Example:**
```python
{
    "data": {
        "name": "API Rate Limit Discussion",
        "episode_body": "Client confirmed API rate limit is 1000 requests per minute",
        "group_id": "anobel-project",
        "valid_at": "2025-01-19T10:30:00Z"
    }
}
```

### 2. `mcp__graphiti-gemini__search`
Search the knowledge graph for relevant information.

**Parameters:**
- `query`: Search query object containing:
  - `query`: The search string
  - `limit`: Maximum results (default: 10)
  - `group_ids`: Optional array of group IDs to filter by

**Example:**
```python
{
    "query": {
        "query": "API rate limits",
        "limit": 5,
        "group_ids": ["anobel-project"]
    }
}
```

### 3. `mcp__graphiti-gemini__retrieve_episodes`
Retrieve recent episodes from memory.

**Parameters:**
- `last_n`: Number of episodes to retrieve (default: 10)
- `group_ids`: Optional array of group IDs to filter by

## Integration with Claude Code

### Memory Context Hook
The memory-context-hook automatically:
- Searches for relevant memories when queries match patterns
- Provides context from previous sessions
- Suggests when to capture important information

### Pattern Extraction
Works with pattern-extraction-hook to:
- Automatically extract facts, patterns, and constraints
- Update knowledge files (facts.json, patterns.json, constraints.json)
- Build a growing knowledge base over time

### Usage in Hooks

```python
# Example hook integration
from logic.memory import graphiti_client

# Add memory
graphiti_client.add_episode(
    name="Security Pattern Found",
    body="Never store API keys in code",
    group_id=project_name
)

# Search memories
results = graphiti_client.search(
    query="security best practices",
    limit=5
)
```

## Best Practices

1. **Capture Decisions**: Always capture important technical decisions
   ```
   /memory capture "Decided to use REM units instead of pixels for all CSS"
   ```

2. **Group by Project**: Use consistent group_ids for project organization
   ```
   group_id: "anobel-website" or "claude-code-hooks"
   ```

3. **Temporal Context**: Include timestamps for time-sensitive information
   ```
   valid_at: "2025-01-19T14:00:00Z"
   ```

4. **Semantic Titles**: Use descriptive names for easy retrieval
   ```
   name: "Webflow CSS Constraints" not "Note 1"
   ```

## Common Patterns

### Client Preferences
```
DECISION: Client prefers minimal animations
PATTERN: Always use subtle transitions under 300ms
CONSTRAINT: No auto-playing videos
```

### Technical Decisions
```
RESOLVED: Fixed console.log issue with DEBUG wrapper
BREAKING: Changed from pixels to REM units
PATTERN: Use data attributes for component styling
```

### Security Patterns
```
SECURITY: API keys stored in .env file only
API_ENDPOINT: POST /api/v1/auth/login
CONSTRAINT: Rate limit 1000 req/min
```

## Troubleshooting

### Connection Issues
- Ensure Neo4j is running and accessible
- Check MCP server logs for connection errors
- Verify authentication credentials

### Search Not Finding Results
- Use broader search terms
- Check if memories were captured with correct group_id
- Verify temporal filters aren't too restrictive

### Memory Not Persisting
- Confirm add_episode returns success
- Check Neo4j database directly
- Verify episode data structure is correct

## Related Documentation
- [Memory Context Hook](../../hooks/memory/README.md)
- [Pattern Extraction](../../hooks/core/pattern-extraction-hook.md)
- [Memory Commands](/memory)](../../commands/memory.md)