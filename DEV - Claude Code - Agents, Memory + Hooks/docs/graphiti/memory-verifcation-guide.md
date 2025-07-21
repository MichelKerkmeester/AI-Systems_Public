# Graphiti Memory Verification Guide

## Table of Contents

- [How to Verify Memory in Neo4j](#how-to-verify-memory-in-neo4j)
  - [1. Access Neo4j Browser](#1-access-neo4j-browser)
  - [2. Query Commands to Find Your Memory](#2-query-commands-to-find-your-memory)
  - [3. Verify Episode Properties](#3-verify-episode-properties)
  - [4. Check Entity Extraction](#4-check-entity-extraction)
  - [5. Verify in Graphiti Logs](#5-verify-in-graphiti-logs)
  - [6. Using Graphiti Studio (if available)](#6-using-graphiti-studio-if-available)
- [Why Episodes May Not Appear Immediately](#why-episodes-may-not-appear-immediately)
- [Troubleshooting](#troubleshooting)
- [Test Memory Details for Reference](#test-memory-details-for-reference)
## How to Verify Memory in Neo4j

### 1. Access Neo4j Browser

If running locally:
- Open: http://localhost:7474
- Default credentials: neo4j/password (check your .env)

If using cloud:
- Access your Neo4j Aura Console
- Open the database browser

### 2. Query Commands to Find Your Memory

```cypher
// Find episode by exact name
MATCH (e:Episode {name: "TEST-MEMORY-2025-01-18-CLAUDE"})
RETURN e

// Find all episodes from Claude Code
MATCH (e:Episode)
WHERE e.source = "claude_code_verification"
RETURN e ORDER BY e.created_at DESC

// Find episodes by group
MATCH (e:Episode {group_id: "claude-test-verification"})
RETURN e

// Search episode content
MATCH (e:Episode)
WHERE e.content CONTAINS "Claude Code Graphiti MCP"
RETURN e.name, e.content, e.created_at

// Get full episode details with relationships
MATCH (e:Episode {name: "TEST-MEMORY-2025-01-18-CLAUDE"})
OPTIONAL MATCH (e)-[r]-(connected)
RETURN e, r, connected
```

### 3. Verify Episode Properties

The episode should have these properties:
- `name`: "TEST-MEMORY-2025-01-18-CLAUDE"
- `content`: The full episode_body text
- `source`: "claude_code_verification"
- `source_description`: "Claude Code Graphiti MCP Verification Test"
- `group_id`: "claude-test-verification"
- `created_at`: Timestamp
- `valid_at`: "2025-01-18T13:15:00Z"
- `uuid`: Auto-generated unique ID

### 4. Check Entity Extraction

Graphiti should have extracted entities from the content:
```cypher
// Find entities connected to the episode
MATCH (e:Episode {name: "TEST-MEMORY-2025-01-18-CLAUDE"})-[:MENTIONS]-(entity:Entity)
RETURN entity.name, labels(entity)
```

### 5. Verify in Graphiti Logs

Check the Graphiti server logs for:
- Episode addition confirmation
- Entity extraction results
- Any processing errors

### 6. Using Graphiti Studio (if available)

Some Graphiti installations include a web UI:
- Access: http://localhost:8000 (or configured port)
- Search for "TEST-MEMORY-2025-01-18-CLAUDE"
- View the knowledge graph visualization

## Why Episodes May Not Appear Immediately

1. **Async Processing**: Graphiti processes episodes asynchronously
2. **Indexing Delay**: Neo4j may need time to index new nodes
3. **Cache**: The retrieve_episodes endpoint might use cached results
4. **Different Views**: Search vs retrieve may query different indexes

## Troubleshooting

If you can't find the memory:
1. Check Neo4j is running: `neo4j status`
2. Verify connection in .env file
3. Look for errors in Graphiti logs
4. Try a direct Neo4j query (most reliable)
5. Wait 30-60 seconds for processing

## Test Memory Details for Reference

```json
{
  "name": "TEST-MEMORY-2025-01-18-CLAUDE",
  "episode_body": "This is a test memory created at 2025-01-18 13:15 UTC by Claude Code to verify Graphiti MCP integration. This memory includes a unique identifier (TEST-MEMORY-2025-01-18-CLAUDE) to make it easy to search for in the Neo4j database. The memory also tests the full functionality including group_id assignment and timestamp handling.",
  "source": "claude_code_verification",
  "source_description": "Claude Code Graphiti MCP Verification Test",
  "valid_at": "2025-01-18T13:15:00Z",
  "group_id": "claude-test-verification"
}
```