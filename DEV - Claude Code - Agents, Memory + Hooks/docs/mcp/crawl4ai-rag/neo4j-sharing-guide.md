# Using Neo4j with Both Graphiti and CRAWL4AI-RAG

## Current Setup
- **Graphiti**: Already using Neo4j at `neo4j://127.0.0.1:7687`
- **CRAWL4AI-RAG**: Can share the same instance

## Can They Share? Yes, BUT...

### ✅ Pros of Sharing
1. **Single database** to manage
2. **Cost efficient** (one Neo4j instance)
3. **Potential synergies** between knowledge graphs

### ⚠️ Cons of Sharing
1. **Namespace conflicts** - Different node/relationship types
2. **Schema differences** - Each uses different graph structures
3. **Query performance** - Larger graph = slower queries
4. **Backup complexity** - Mixed data in backups

## How They Use Neo4j Differently

### Graphiti (Memory/Knowledge Graph)
```cypher
// Focuses on episodic memory and concepts
(Episode)-[:MENTIONS]->(Entity)
(Entity)-[:RELATES_TO]->(Entity)
(Episode)-[:OCCURRED_AT]->(Timestamp)
```

### CRAWL4AI-RAG (Code Analysis)
```cypher
// Focuses on code structure
(File)-[:CONTAINS]->(Class)
(Class)-[:HAS_METHOD]->(Method)
(File)-[:IMPORTS]->(Module)
(Method)-[:CALLS]->(Method)
```

## Recommended Approaches

### Option 1: Share with Namespacing (Recommended)
```json
// In ~/.claude.json for crawl4ai-rag:
"NEO4J_URI": "neo4j://127.0.0.1:7687",
"NEO4J_USER": "neo4j",
"NEO4J_PASSWORD": "AQCIbagraydayAQCIba"
```

**Why this works:**
- Different node labels prevent conflicts
- Graphiti: `Episode`, `Entity`, `Fact`
- CRAWL4AI: `File`, `Class`, `Method`, `Function`

### Option 2: Separate Databases (Cleaner)
```bash
# Create a new database in Neo4j Desktop
CREATE DATABASE crawl4ai;

# Then use different database in connection
"NEO4J_URI": "neo4j://localhost:7687/crawl4ai"
```

### Option 3: Different Ports (Most Isolated)
```bash
# Run second Neo4j instance on different port
docker run -p 7688:7687 neo4j:latest

# Configure CRAWL4AI to use it
"NEO4J_URI": "bolt://localhost:7688"
```

## Quick Decision Guide

**Share the database if:**
- You want simplicity ✅
- You might want to query across both graphs
- You're comfortable with mixed data

**Separate if:**
- You need clean separation
- Performance is critical
- You want independent backups

## Implementation for Sharing

Since you're already using Neo4j with Graphiti, the easiest approach:

```json
// Update ~/.claude.json for crawl4ai-rag:
"crawl4ai-rag": {
  "env": {
    // ... other settings ...
    "USE_KNOWLEDGE_GRAPH": "true",
    "NEO4J_URI": "neo4j://127.0.0.1:7687",
    "NEO4J_USER": "neo4j",
    "NEO4J_PASSWORD": "AQCIbagraydayAQCIba"
  }
}
```

## Testing Compatibility

After enabling, test with:
```cypher
// In Neo4j Browser, check what's there:
MATCH (n) 
RETURN DISTINCT labels(n) as NodeTypes, count(*) as Count

// Should show both:
// - Graphiti types: Episode, Entity, etc.
// - CRAWL4AI types: File, Class, Method (after first code analysis)
```

## Monitoring Tips

1. **Watch graph size**: 
   ```cypher
   MATCH (n) RETURN count(n) as TotalNodes
   ```

2. **Check for conflicts**:
   ```cypher
   // Find nodes with multiple labels (shouldn't happen)
   MATCH (n)
   WHERE size(labels(n)) > 1
   RETURN n LIMIT 10
   ```

3. **Performance baseline**:
   - Note current Graphiti query speeds
   - Monitor after adding CRAWL4AI data

## Recommendation

**For your use case**: Share the database initially. The node types are different enough that conflicts are unlikely. If you notice performance issues or data confusion later, you can always migrate to a separate database.