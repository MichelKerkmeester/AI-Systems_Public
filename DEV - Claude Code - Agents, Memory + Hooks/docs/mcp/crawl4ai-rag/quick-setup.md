# CRAWL4AI-RAG Quick Setup Guide

## Current Status
✅ Installed and configured for basic web crawling
❌ Advanced RAG features disabled (no API keys)

## Quick Enable Options

### Option 1: Basic Crawling Only (Current Setup)
```json
// No changes needed - works as-is
// Can crawl websites and extract content
```

### Option 2: Add Semantic Search
```bash
# 1. Get OpenAI API key: https://platform.openai.com/api-keys
# 2. Create Supabase project: https://supabase.com
# 3. Update ~/.claude.json:

"crawl4ai-rag": {
  "env": {
    "OPENAI_API_KEY": "sk-proj-xxxxx",
    "SUPABASE_URL": "https://xxxxx.supabase.co",
    "SUPABASE_SERVICE_KEY": "eyJxxxxx",
    "USE_CONTEXTUAL_EMBEDDINGS": "true",
    "USE_HYBRID_SEARCH": "true"
  }
}
```

### Option 3: Use with Existing Gemini (Alternative)
Since you already have Gemini API keys, you could:
1. Keep current setup for basic crawling
2. Use your existing `graphiti-gemini` MCP for semantic search
3. Combine both tools:
   - CRAWL4AI for web scraping
   - Graphiti for knowledge storage

Example workflow:
```
1. Crawl with CRAWL4AI → Get content
2. Store in Graphiti → Semantic search ready
```

### Option 4: Full Setup (All Features)
```json
{
  "OPENAI_API_KEY": "sk-xxx",
  "SUPABASE_URL": "https://xxx.supabase.co",
  "SUPABASE_SERVICE_KEY": "eyJxxx",
  "NEO4J_URI": "bolt://localhost:7687",
  "NEO4J_USER": "neo4j",
  "NEO4J_PASSWORD": "password",
  "USE_CONTEXTUAL_EMBEDDINGS": "true",
  "USE_HYBRID_SEARCH": "true",
  "USE_AGENTIC_RAG": "true",
  "USE_RERANKING": "true",
  "USE_KNOWLEDGE_GRAPH": "true"
}
```

## Recommended Next Steps

For your use case with anobel.nl project:

1. **Keep as-is** for now (basic crawling works)
2. **If you need search**, either:
   - Add OpenAI key + Supabase, OR
   - Use with your existing Graphiti setup
3. **Document any sites** you crawl in project notes

## Testing the Installation

```bash
# Restart Claude Code
# Then in a new conversation:
"List MCP servers"
# Should see: crawl4ai-rag ✅

"Crawl https://example.com"
# Should work without API keys
```