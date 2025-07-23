# Crawl4AI Database Test Plan

## Test Objectives
Verify that the crawl4ai knowledge graph feature correctly populates the Neo4j crawl4ai database after configuration fixes.

## Prerequisites
- [ ] Claude Code CLI restarted after configuration update
- [ ] Docker container `crawl4ai-mcp` running
- [ ] Neo4j accessible at localhost:7687
- [ ] crawl4ai database exists in Neo4j

## Test Cases

### Test 1: Basic Repository Parsing
**Objective**: Verify repository can be parsed into knowledge graph

**Steps**:
1. Use tool: `mcp__crawl4ai-rag__parse_github_repository`
2. Input: `repo_url: https://github.com/michaellatman/mcp-memory-service.git`
3. Wait for parsing to complete

**Expected Results**:
- Success message with parsing statistics
- No git clone errors
- Node count > 0

**Validation**:
```cypher
# In Neo4j Browser (crawl4ai database)
MATCH (r:Repository {name: 'mcp-memory-service'})
RETURN r
```

### Test 2: Query Repository Structure
**Objective**: Verify knowledge graph queries work correctly

**Test 2a: List Repositories**
```
mcp__crawl4ai-rag__query_knowledge_graph
command: repos
```
Expected: List includes "mcp-memory-service"

**Test 2b: Get Classes**
```
mcp__crawl4ai-rag__query_knowledge_graph
command: classes
repo_name: mcp-memory-service
```
Expected: List of Python classes with their methods

**Test 2c: Get File Structure**
```
mcp__crawl4ai-rag__query_knowledge_graph
command: files
repo_name: mcp-memory-service
```
Expected: Directory structure with file paths

### Test 3: Code Search Functionality
**Objective**: Verify code search across parsed repository

**Steps**:
1. Use tool: `mcp__crawl4ai-rag__search_code_examples`
2. Input: 
   - `query: memory storage`
   - `match_count: 5`

**Expected Results**:
- Code snippets related to memory storage
- Results from the parsed repository

### Test 4: Multiple Repository Handling
**Objective**: Verify system can handle multiple repositories

**Steps**:
1. Parse a second repository:
   ```
   mcp__crawl4ai-rag__parse_github_repository
   repo_url: https://github.com/anthropics/anthropic-sdk-python.git
   ```
2. Query both repositories:
   ```
   mcp__crawl4ai-rag__query_knowledge_graph
   command: repos
   ```

**Expected Results**:
- Both repositories listed
- Can query each independently
- No data corruption

### Test 5: Integration with Existing System
**Objective**: Verify no conflicts with Graphiti memory system

**Steps**:
1. Check Graphiti still works:
   ```
   mcp__graphiti-gemini__search
   query: "test memory"
   ```
2. Add a new memory:
   ```
   mcp__graphiti-gemini__add_episode
   ```
3. Verify both databases remain separate

**Expected Results**:
- Graphiti queries work normally
- New memories saved to neo4j database (not crawl4ai)
- No cross-database interference

## Performance Tests

### Test 6: Large Repository Parsing
**Objective**: Test with larger repository

**Steps**:
1. Parse larger repo (if needed):
   ```
   mcp__crawl4ai-rag__parse_github_repository
   repo_url: https://github.com/fastapi/fastapi.git
   ```

**Metrics to Track**:
- Parsing time
- Memory usage (docker stats)
- Node count in database
- Query response times

## Error Scenarios

### Test 7: Invalid Repository URL
**Input**: `repo_url: https://github.com/invalid/repo.git`
**Expected**: Graceful error message

### Test 8: Private Repository
**Input**: Private repository URL
**Expected**: Authentication error or skip

### Test 9: Network Interruption
**Steps**: 
1. Start parsing
2. Disconnect network briefly
**Expected**: Timeout error, partial data handling

## Database Validation

### Final Validation Queries
Run these in Neo4j Browser (crawl4ai database):

```cypher
# Total node count
MATCH (n) RETURN count(n) as total_nodes

# Node type distribution
MATCH (n) 
RETURN labels(n)[0] as node_type, count(n) as count 
ORDER BY count DESC

# Repository relationships
MATCH (r:Repository)-[rel]->(n)
RETURN type(rel), count(rel)
ORDER BY count(rel) DESC

# Complex code relationships
MATCH (c:Class)-[:HAS_METHOD]->(m:Method)
RETURN c.name, collect(m.name) as methods
LIMIT 5
```

## Success Metrics

- [ ] All basic tests pass
- [ ] At least 100 nodes created per repository
- [ ] Query response time < 1 second
- [ ] No errors in Docker logs
- [ ] No impact on Graphiti performance

## Rollback Plan

If issues occur:
1. Revert ~/.claude.json to use 127.0.0.1
2. Restart Claude Code
3. Use setup script to reconfigure
4. Document specific error for troubleshooting

## Test Log Template

```
Date: [DATE]
Tester: [NAME]
Claude Code Version: [VERSION]

Test Results:
- [ ] Test 1: Basic Parsing - PASS/FAIL
- [ ] Test 2: Query Functions - PASS/FAIL
- [ ] Test 3: Code Search - PASS/FAIL
- [ ] Test 4: Multiple Repos - PASS/FAIL
- [ ] Test 5: Integration - PASS/FAIL
- [ ] Test 6: Performance - PASS/FAIL
- [ ] Test 7-9: Error Handling - PASS/FAIL

Issues Found:
[Document any issues]

Database Stats:
- Total Nodes: [COUNT]
- Repositories: [COUNT]
- Files: [COUNT]
- Classes: [COUNT]
- Methods: [COUNT]
```