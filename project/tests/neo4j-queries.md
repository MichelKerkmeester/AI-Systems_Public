# Neo4j Browser Queries for Graphiti

## Access Neo4j Browser
1. Open browser: http://localhost:7474
2. Login with your credentials (default: neo4j/password)

## Useful Cypher Queries

### 1. View All Episodes (Memories)
```cypher
MATCH (e:Episode)
RETURN e
ORDER BY e.created_at DESC
LIMIT 50
```

### 2. View Episodes with Details
```cypher
MATCH (e:Episode)
RETURN e.name as Name, 
       e.created_at as Created,
       e.source as Source,
       e.group_id as Group,
       substring(e.content, 0, 100) + "..." as Preview
ORDER BY e.created_at DESC
```

### 3. Search Specific Memories
```cypher
// Search by pattern type
MATCH (e:Episode)
WHERE e.name STARTS WITH "SECURITY:"
RETURN e

// Search by content
MATCH (e:Episode)
WHERE e.content CONTAINS "API key"
RETURN e

// Search by group
MATCH (e:Episode)
WHERE e.group_id = "security-measures"
RETURN e
```

### 4. View Entity Graph
```cypher
// Show entities and their relationships
MATCH (n:Entity)-[r]-(m:Entity)
RETURN n, r, m
LIMIT 50
```

### 5. View Episode-Entity Connections
```cypher
// See which entities were extracted from episodes
MATCH (e:Episode)-[r:HAS_ENTITY]->(n:Entity)
RETURN e.name as Episode, n.name as Entity, n.summary as Summary
ORDER BY e.created_at DESC
```

### 6. Database Overview
```cypher
// Count all node types
MATCH (n)
RETURN labels(n)[0] as Type, count(*) as Count
ORDER BY Count DESC

// Total relationships
MATCH ()-[r]->()
RETURN type(r) as RelationType, count(*) as Count
ORDER BY Count DESC
```

### 7. Recent Activity
```cypher
// Last 10 episodes added
MATCH (e:Episode)
RETURN e
ORDER BY e.created_at DESC
LIMIT 10
```

### 8. Memory Categories
```cypher
// Group memories by pattern
MATCH (e:Episode)
WITH 
  CASE 
    WHEN e.name STARTS WITH "DECISION:" THEN "Architecture Decisions"
    WHEN e.name STARTS WITH "SECURITY:" THEN "Security Updates"
    WHEN e.name STARTS WITH "PATTERN:" THEN "Code Patterns"
    WHEN e.name STARTS WITH "RESOLVED:" THEN "Bug Fixes"
    WHEN e.name STARTS WITH "OPTIMIZATION:" THEN "Performance"
    ELSE "Other"
  END as Category,
  e
RETURN Category, count(e) as Count, collect(e.name)[0..3] as Examples
ORDER BY Count DESC
```

### 9. Timeline View
```cypher
// Episodes by date
MATCH (e:Episode)
RETURN date(e.created_at) as Date, 
       count(*) as Episodes,
       collect(e.name) as Memories
ORDER BY Date DESC
```

### 10. Knowledge Graph Visualization
```cypher
// Full graph view (careful with large datasets)
MATCH (n)
OPTIONAL MATCH (n)-[r]-(m)
RETURN n, r, m
LIMIT 100
```

## Tips for Neo4j Browser

1. **Visual Graph**: Click the graph icon to see visual representation
2. **Table View**: Click table icon for structured data
3. **Export**: You can export query results as CSV
4. **Save Queries**: Star queries to save them as favorites
5. **Styling**: Click on node labels to customize colors and icons

## Direct Connection Info
- URI: `bolt://localhost:7687` or `neo4j://localhost:7687`
- Default username: `neo4j`
- Password: Check your `.env` file