# Crawl4AI Database Setup & Testing Requirements

## Overview
The crawl4ai knowledge graph feature has been fixed but requires Claude Code restart to apply configuration changes. This spec documents the setup, testing procedures, and integration with the existing system.

## Current Status
✅ **Fixed Issues:**
- Docker networking issue resolved (changed from 127.0.0.1 to host.docker.internal)
- Neo4j crawl4ai database exists and schema is ready
- Configuration updated in ~/.claude.json
- Docker container restarted with new settings

## Database Architecture

### Three Separate Storage Systems:
1. **Neo4j `neo4j` database** (3,189 nodes)
   - Purpose: Graphiti conversation memories
   - Status: Working perfectly
   - Connection: Direct from Claude Code

2. **Neo4j `crawl4ai` database** (0 nodes - ready to populate)
   - Purpose: Code knowledge graphs from parsed repositories
   - Status: Fixed, awaiting test after restart
   - Connection: Via Docker container using host.docker.internal

3. **Supabase** (7 sources stored)
   - Purpose: Web content from crawled sites
   - Status: Working
   - Sources: docs.github.com, example.com, etc.

## Testing Requirements After Restart

### 1. Verify Knowledge Graph Parsing
```bash
# Test with a simple repository
mcp__crawl4ai-rag__parse_github_repository
repo_url: https://github.com/michaellatman/mcp-memory-service.git
```

Expected outcome:
- Repository successfully cloned and parsed
- Nodes created in crawl4ai database for:
  - Repository metadata
  - Files
  - Classes
  - Methods
  - Functions
  - Relationships between entities

### 2. Query Parsed Repository
```bash
# List all repositories
mcp__crawl4ai-rag__query_knowledge_graph
command: repos

# Get classes from repository
mcp__crawl4ai-rag__query_knowledge_graph
command: classes
repo_name: mcp-memory-service

# Get methods
mcp__crawl4ai-rag__query_knowledge_graph
command: methods
repo_name: mcp-memory-service
```

### 3. Test AI Hallucination Detection
Once repository is parsed, test the hallucination detection:
```bash
mcp__crawl4ai-rag__check_ai_script_hallucinations
script_path: /path/to/test/script.py
```

## Integration Points

### 1. Memory System Integration
- Crawl4ai should work alongside Graphiti memories
- Both systems use separate Neo4j databases
- No conflicts expected

### 2. Agent System Integration
- Agents can use crawl4ai for code analysis
- Repository knowledge graphs enhance code understanding
- Enables better code reuse detection

### 3. Documentation Automation
- Parsed repositories provide code structure
- Can auto-generate documentation from knowledge graph
- Enhances existing doc automation workflows

## Monitoring & Validation

### Check Database Population
After parsing a repository, verify in Neo4j:
```cypher
# Run in Neo4j Browser, select crawl4ai database
MATCH (n) RETURN labels(n), count(n) ORDER BY count(n) DESC
```

Expected node types:
- Repository
- File
- Class
- Method
- Function
- Module
- Attribute

### Container Health Check
```bash
# Check container logs
docker logs crawl4ai-mcp --tail 50

# Verify container is running
docker ps | grep crawl4ai
```

## Error Handling

### Common Issues & Solutions:

1. **"Repository parsing failed: Command 'git clone' returned non-zero exit status"**
   - Cause: Git not available in container or network issues
   - Solution: Check container has internet access

2. **"Failed to connect to Neo4j"**
   - Cause: Configuration not applied
   - Solution: Ensure Claude Code was restarted

3. **"Database crawl4ai not found"**
   - Cause: Database not created
   - Solution: Run setup-crawl4ai-knowledge-graph.py script

## Success Criteria

1. ✅ Successfully parse at least one repository
2. ✅ Verify nodes created in crawl4ai database
3. ✅ Query knowledge graph returns accurate data
4. ✅ No conflicts with existing Graphiti memory system
5. ✅ Integration with agent system functional

## Next Steps

1. **Immediate**: Restart Claude Code to apply configuration
2. **Test**: Parse test repository as documented above
3. **Verify**: Check Neo4j crawl4ai database has nodes
4. **Integrate**: Use in agent workflows for code analysis
5. **Document**: Update agent system specs with crawl4ai capabilities

## Configuration Reference

Updated configuration in ~/.claude.json:
```json
"crawl4ai-rag": {
  "env": {
    "NEO4J_URI": "neo4j://host.docker.internal:7687",
    "USE_KNOWLEDGE_GRAPH": "true",
    // ... other settings
  }
}
```

## Scripts Created
- `/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/scripts/fix-crawl4ai-neo4j.py`
- `/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/scripts/setup-crawl4ai-knowledge-graph.py`

Both scripts can be re-run if needed for troubleshooting.