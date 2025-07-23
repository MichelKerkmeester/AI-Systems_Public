# Crawl4AI Database Quick Reference

## 🚀 Quick Start After Restart

### 1. Test Repository Parsing
```bash
# Parse a test repository
mcp__crawl4ai-rag__parse_github_repository
repo_url: https://github.com/michaellatman/mcp-memory-service.git
```

### 2. Verify It Worked
```bash
# Check repositories
mcp__crawl4ai-rag__query_knowledge_graph
command: repos

# Should show: ["mcp-memory-service", "Agent-MCP", "make-it-heavy", "serena"]
```

### 3. Query Code Structure
```bash
# Get all classes
mcp__crawl4ai-rag__query_knowledge_graph
command: classes
repo_name: mcp-memory-service

# Get all methods
mcp__crawl4ai-rag__query_knowledge_graph  
command: methods
repo_name: mcp-memory-service

# Get file structure
mcp__crawl4ai-rag__query_knowledge_graph
command: files
repo_name: mcp-memory-service
```

## 📊 Database Overview

### What's Where:
- **neo4j database**: Graphiti memories (3,189 nodes) 
- **crawl4ai database**: Code knowledge graphs (will populate after parsing)
- **Supabase**: Web content (7 sources already stored)

### Check in Neo4j Browser:
1. Open http://localhost:7474
2. Login: neo4j / AQCIbagraydayAQCIba
3. Switch to crawl4ai database (top left dropdown)
4. Run: `MATCH (n) RETURN labels(n), count(n)`

## 🔧 Troubleshooting

### If parsing fails:
```bash
# Check container logs
docker logs crawl4ai-mcp --tail 50

# Restart container
docker restart crawl4ai-mcp

# Re-run setup script
python3 /Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/scripts/setup-crawl4ai-knowledge-graph.py
```

### Common Issues:
- **"git clone failed"**: Container network issue
- **"Neo4j connection failed"**: Claude Code needs restart
- **"Database not found"**: Run setup script

## 🎯 Use Cases

### 1. Code Analysis
```bash
# Search for specific patterns
mcp__crawl4ai-rag__search_code_examples
query: "authentication implementation"
match_count: 10
```

### 2. AI Hallucination Check
```bash
# After parsing a repo with Python files
mcp__crawl4ai-rag__check_ai_script_hallucinations
script_path: /path/to/script.py
```

### 3. Repository Documentation
```bash
# Get repository overview
mcp__crawl4ai-rag__query_knowledge_graph
command: summary
repo_name: mcp-memory-service
```

## 📝 Integration Notes

### With Agent System:
- Agents can query code structure before implementation
- Enhances code reuse detection
- Provides context for better code generation

### With Memory System:
- Crawl4ai uses separate database (no conflicts)
- Can create memories about parsed repositories
- Both systems complement each other

### With Documentation:
- Auto-generate docs from code structure
- Track API changes across versions
- Create dependency graphs

## 🚦 Status Indicators

✅ **Working**: Supabase web crawling, Graphiti memories
🔧 **Fixed**: Neo4j connection for knowledge graphs
⏳ **Pending**: Test after Claude Code restart
🎯 **Goal**: Populate crawl4ai database with repository data