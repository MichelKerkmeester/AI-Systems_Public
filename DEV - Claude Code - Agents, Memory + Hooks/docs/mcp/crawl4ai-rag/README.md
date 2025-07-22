# CRAWL4AI-RAG MCP Server Documentation

## Overview

CRAWL4AI-RAG is an MCP server that provides web crawling capabilities with optional RAG (Retrieval-Augmented Generation) features. It can crawl websites, extract content, and optionally store it in vector databases for semantic search.

## Installation Status

✅ **Installed**: `/Users/michel_kerkmeester/mcp-servers/crawl4ai-rag`
✅ **Added to**: `~/.claude.json`
✅ **Configuration**: Fully enabled with all features
✅ **Neo4j Database**: Using dedicated `crawl4ai` database
✅ **API Keys**: OpenAI and Supabase configured

## Configuration Options

### Basic Settings

#### `TRANSPORT` (Default: "stdio")
- **Purpose**: Communication method between Claude and the MCP server
- **Options**: 
  - `"stdio"` - Standard input/output (recommended for Claude Code)
  - `"sse"` - Server-sent events (for web-based clients)
- **Current**: `"stdio"` ✅

#### `OPENAI_API_KEY` (Required for advanced features)
- **Purpose**: Authentication for OpenAI embeddings and LLM features
- **Used for**: 
  - Text embeddings (`text-embedding-3-small`)
  - Contextual processing
  - Content summarization
- **How to get**: https://platform.openai.com/api-keys
- **Current**: Empty ⚠️

#### `MODEL_CHOICE` (Default: "gpt-4o-mini")
- **Purpose**: LLM model for content processing
- **Options**: Any OpenAI chat model (gpt-4, gpt-3.5-turbo, etc.)
- **Used when**: Contextual embeddings or agentic RAG enabled
- **Current**: `"gpt-4o-mini"` ✅

### Advanced RAG Features

#### `USE_CONTEXTUAL_EMBEDDINGS` (Default: false)
- **Purpose**: Enhances embeddings with contextual information
- **How it works**: 
  - Adds surrounding context to each text chunk before embedding
  - Improves semantic search accuracy
  - Requires `OPENAI_API_KEY` and `MODEL_CHOICE`
- **Enable when**: You need high-quality semantic search
- **Current**: `false` ❌

#### `USE_HYBRID_SEARCH` (Default: false)
- **Purpose**: Combines vector similarity with keyword search
- **How it works**:
  - Uses both semantic embeddings and BM25 keyword matching
  - Provides better coverage for both semantic and exact matches
- **Enable when**: You need both semantic and keyword-based retrieval
- **Current**: `false` ❌

#### `USE_AGENTIC_RAG` (Default: false)
- **Purpose**: Advanced code-aware content processing
- **Features**:
  - Extracts code examples from crawled content
  - Stores code snippets separately with metadata
  - Enables specialized code search
  - Generates code summaries and documentation
- **Enable when**: Crawling technical documentation or code repositories
- **Current**: `false` ❌

#### `USE_RERANKING` (Default: false)
- **Purpose**: Improves search result relevance
- **How it works**:
  - Uses cross-encoder model to rerank search results
  - More accurate than initial vector similarity
  - Slower but more precise
- **Enable when**: Search result quality is critical
- **Current**: `false` ❌

#### `USE_KNOWLEDGE_GRAPH` (Default: false)
- **Purpose**: Advanced features for code analysis
- **Features**:
  - AI hallucination detection in code
  - Repository structure parsing
  - Code relationship mapping
- **Requires**: Neo4j database setup (see below)
- **Current**: `false` ❌

### Database Configuration

#### Supabase (Vector Storage)

Required for storing crawled content and embeddings.

##### `SUPABASE_URL`
- **Purpose**: Your Supabase project URL
- **Format**: `https://[PROJECT_ID].supabase.co`
- **How to get**: 
  1. Create account at https://supabase.com
  2. Create new project
  3. Go to Settings → API
  4. Copy "Project URL"
- **Current**: Empty ⚠️

##### `SUPABASE_SERVICE_KEY`
- **Purpose**: Admin access to Supabase
- **Security**: Keep secret! Full database access
- **How to get**:
  1. Go to Settings → API
  2. Copy "service_role" key (not anon key!)
- **Current**: Empty ⚠️

#### Neo4j (Knowledge Graph)

Required only if `USE_KNOWLEDGE_GRAPH` is enabled.

##### `NEO4J_URI`
- **Purpose**: Connection endpoint for Neo4j
- **Format**: 
  - Local: `bolt://localhost:7687`
  - Cloud: `neo4j://[instance].databases.neo4j.io`
  - Docker: `bolt://host.docker.internal:7687`
- **Current**: Empty ⚠️

##### `NEO4J_USER`
- **Purpose**: Neo4j username
- **Default**: `neo4j`
- **Current**: Empty ⚠️

##### `NEO4J_PASSWORD`
- **Purpose**: Neo4j database password
- **How to get**: Set during Neo4j installation
- **Current**: Empty ⚠️

## Setup Guide

### 1. Basic Web Crawling (No API Keys Required)

Current configuration works for:
- Crawling websites
- Extracting text content
- Basic scraping

```bash
# Already configured and ready to use!
```

### 2. Enable Semantic Search

```bash
# 1. Get OpenAI API key from https://platform.openai.com/api-keys

# 2. Create Supabase account and project at https://supabase.com

# 3. Update ~/.claude.json:
"env": {
  "OPENAI_API_KEY": "sk-...",
  "SUPABASE_URL": "https://xxxxx.supabase.co",
  "SUPABASE_SERVICE_KEY": "eyJ...",
  "USE_CONTEXTUAL_EMBEDDINGS": "true",
  "USE_HYBRID_SEARCH": "true"
}

# 4. Run the SQL script to create tables:
psql $SUPABASE_CONNECTION_STRING < /Users/michel_kerkmeester/mcp-servers/crawl4ai-rag/crawled_pages.sql
```

### 3. Enable Code-Aware Features

```bash
# Additional to step 2:
"USE_AGENTIC_RAG": "true",
"USE_RERANKING": "true"
```

### 4. Enable Knowledge Graph

```bash
# 1. Install Neo4j Desktop or use cloud instance

# 2. Add to configuration:
"USE_KNOWLEDGE_GRAPH": "true",
"NEO4J_URI": "bolt://localhost:7687",
"NEO4J_USER": "neo4j",
"NEO4J_PASSWORD": "your-password"
```

## Usage Examples

### Basic Crawling
```
User: Crawl https://example.com
Assistant: [Uses crawl_website tool without RAG features]
```

### With RAG Enabled
```
User: Crawl and index https://docs.example.com for searchable documentation
Assistant: [Crawls, extracts, embeds, and stores in Supabase]

User: Search for "authentication" in the crawled docs
Assistant: [Performs semantic search with optional reranking]
```

### With Code Analysis
```
User: Analyze the codebase at https://github.com/example/repo
Assistant: [Uses knowledge graph tools for deeper analysis]
```

## Troubleshooting

### "No OPENAI_API_KEY set"
- Only affects embedding features
- Basic crawling still works
- Add key to enable semantic search

### "Failed to connect to Supabase"
- Check URL format
- Verify service key (not anon key)
- Ensure tables are created

### "Neo4j connection failed"
- Verify Neo4j is running
- Check URI format
- Test credentials

## Cost Considerations

- **OpenAI API**: ~$0.02 per 1M tokens for embeddings
- **Supabase**: Free tier includes 500MB database
- **Neo4j**: Free for local, paid for cloud

## Security Notes

1. **Service Keys**: Never commit to git
2. **API Keys**: Use environment variables
3. **Database Access**: Use least privilege
4. **Crawling Ethics**: Respect robots.txt

## Next Steps

1. **For basic use**: Works as-is
2. **For search**: Add OpenAI + Supabase
3. **For code analysis**: Add all features
4. **For production**: Use dedicated instances