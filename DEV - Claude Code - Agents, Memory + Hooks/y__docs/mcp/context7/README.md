# Context7 MCP Documentation

## Overview

Context7 is a library documentation retrieval MCP that provides access to up-to-date documentation for thousands of libraries and frameworks. It enables Claude to fetch current API references, code examples, and best practices directly from official sources.

## Key Features

- **Real-time Documentation**: Access to the latest library docs
- **Version-specific**: Get docs for specific library versions
- **Topic Filtering**: Focus on specific topics within documentation
- **Token Control**: Manage response size for optimal context usage

## Available Tools

### 1. `mcp__context7__resolve-library-id`
Resolve a library name to a Context7-compatible ID.

**Parameters:**
- `libraryName`: The name of the library to search for

**Returns:**
- List of matching libraries with:
  - Library ID (e.g., `/vercel/next.js`)
  - Description
  - Code snippet count
  - Trust score (1-10)

**Example:**
```python
{
    "libraryName": "react"
}
# Returns: [{"id": "/facebook/react", "description": "React library", ...}]
```

### 2. `mcp__context7__get-library-docs`
Fetch documentation for a specific library.

**Parameters:**
- `context7CompatibleLibraryID`: Exact library ID (e.g., `/mongodb/docs`)
- `tokens`: Maximum tokens to retrieve (default: 10000)
- `topic`: Optional topic to focus on (e.g., "hooks", "routing")

**Example:**
```python
{
    "context7CompatibleLibraryID": "/vercel/next.js",
    "tokens": 5000,
    "topic": "app-router"
}
```

## Usage Workflow

1. **Resolve Library Name**
   ```
   User: "How do I use React hooks?"
   → Call resolve-library-id with "react"
   → Get ID: "/facebook/react"
   ```

2. **Fetch Documentation**
   ```
   → Call get-library-docs with "/facebook/react" and topic "hooks"
   → Receive comprehensive hooks documentation
   ```

## Supported Libraries

Context7 supports thousands of libraries including:

### Frontend Frameworks
- React (`/facebook/react`)
- Vue (`/vuejs/vue`)
- Angular (`/angular/angular`)
- Next.js (`/vercel/next.js`)
- Svelte (`/sveltejs/svelte`)

### Backend Frameworks
- Express (`/expressjs/express`)
- NestJS (`/nestjs/nest`)
- Django (`/django/django`)
- FastAPI (`/tiangolo/fastapi`)

### Databases
- MongoDB (`/mongodb/docs`)
- PostgreSQL (`/postgres/postgres`)
- Redis (`/redis/redis`)

### Cloud Services
- AWS SDK (`/aws/aws-sdk-js`)
- Google Cloud (`/googleapis/google-cloud-node`)
- Supabase (`/supabase/supabase`)

### AI/ML Libraries
- LangChain (`/langchain-ai/langchain`)
- OpenAI (`/openai/openai-node`)
- Hugging Face (`/huggingface/transformers`)

## Best Practices

1. **Always Resolve First**: Don't guess library IDs
   ```
   ❌ get-library-docs("/react/react")  # Wrong
   ✅ resolve-library-id("react") → get-library-docs("/facebook/react")
   ```

2. **Use Topic Filtering**: Focus responses on relevant sections
   ```python
   {
       "context7CompatibleLibraryID": "/vercel/next.js",
       "topic": "middleware"  # Get only middleware docs
   }
   ```

3. **Manage Token Usage**: Balance detail vs context consumption
   - Quick reference: 5000 tokens
   - Detailed guide: 10000 tokens
   - Comprehensive docs: 20000+ tokens

4. **Version-Specific Docs**: Include version when needed
   ```
   "/vercel/next.js/v14.3.0-canary.87"
   ```

## Integration Examples

### With Code Generation
```python
# User asks about Next.js App Router
1. Resolve: "next.js" → "/vercel/next.js"
2. Get docs with topic: "app-router"
3. Generate code following official patterns
```

### With Debugging
```python
# User has MongoDB connection issue
1. Resolve: "mongodb" → "/mongodb/docs"
2. Get docs with topic: "connection"
3. Identify issue using official troubleshooting guide
```

### With Learning
```python
# User learning React hooks
1. Resolve: "react" → "/facebook/react"
2. Get docs with topic: "hooks"
3. Provide examples from official documentation
```

## Common Use Cases

### 1. API Reference
Get specific method signatures and parameters:
```
topic: "api-reference"
tokens: 5000
```

### 2. Migration Guides
Access version migration documentation:
```
topic: "migration"
tokens: 15000
```

### 3. Best Practices
Retrieve official recommendations:
```
topic: "best-practices"
tokens: 10000
```

### 4. Troubleshooting
Access debugging guides:
```
topic: "troubleshooting"
tokens: 8000
```

## Troubleshooting

### Library Not Found
- Try alternative names (e.g., "express" vs "expressjs")
- Check if library is hyphenated (e.g., "react-router")
- Use broader search terms

### Documentation Too Large
- Reduce token limit
- Use specific topic filtering
- Request multiple focused queries

### Outdated Information
- Check for version-specific IDs
- Verify library still maintains Context7 integration
- Cross-reference with library's GitHub

## Tips for Optimal Usage

1. **Cache Results**: Frequently used docs can be stored in memory
2. **Combine Topics**: Make multiple focused requests vs one large request
3. **Cross-Reference**: Use with WebSearch for latest updates
4. **Extract Patterns**: Save commonly used patterns to patterns.json

## Related Tools
- WebSearch: For latest blog posts and tutorials
- WebFetch: For specific documentation pages
- Graphiti: To store important documentation insights