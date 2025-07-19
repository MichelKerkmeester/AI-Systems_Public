# Gemini MCP Documentation

## Table of Contents

- [Overview](#overview)
  - [Key Features](#key-features)
- [Configuration](#configuration)
  - [API Key Setup](#api-key-setup)
  - [MCP Configuration](#mcp-configuration)
- [API Usage](#api-usage)
  - [Quick Query](#quick-query)
  - [Code Analysis](#code-analysis)
  - [Codebase Analysis](#codebase-analysis)
- [Best Practices](#best-practices)
  - [1. Query Optimization](#1-query-optimization)
  - [2. Code Analysis](#2-code-analysis)
  - [3. Codebase Analysis](#3-codebase-analysis)
  - [4. Rate Limiting](#4-rate-limiting)
- [Integration Examples](#integration-examples)
  - [Hook Integration](#hook-integration)
  - [Security Scanning](#security-scanning)
  - [Code Review Assistant](#code-review-assistant)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
  - [Debug Tips](#debug-tips)
  - [Performance Optimization](#performance-optimization)
## Overview

Gemini MCP provides AI-powered code analysis and understanding capabilities through Google's Gemini API. It excels at pattern recognition, code review, and providing development insights.

### Key Features
- Quick code analysis and understanding
- Pattern recognition across codebases
- Security vulnerability detection
- Code quality suggestions
- Natural language code queries

## Configuration

### API Key Setup
1. Obtain a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Store in environment or configuration:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

### MCP Configuration
In `.claude/settings.json`:
```json
{
  "mcpServers": {
    "gemini-mcp": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gemini"],
      "env": {
        "GEMINI_API_KEY": "${GEMINI_API_KEY}"
      }
    }
  }
}
```

## API Usage

### Quick Query
For quick development questions:
```python
response = mcp__gemini-mcp__gemini_quick_query(
    query="How do I implement rate limiting in Express?",
    context="Building a REST API with Node.js"
)
```

### Code Analysis
Analyze specific code sections:
```python
analysis = mcp__gemini-mcp__gemini_analyze_code(
    code_content='''
    function processPayment(amount, card) {
        // Payment logic here
        console.log(card.number); // Security issue?
        return charge(amount, card);
    }
    ''',
    analysis_type="security"
)
```

Analysis types:
- `comprehensive`: Full analysis
- `security`: Security vulnerabilities
- `performance`: Performance issues
- `architecture`: Design patterns

### Codebase Analysis
Analyze entire directories (uses 1M token context):
```python
analysis = mcp__gemini-mcp__gemini_codebase_analysis(
    directory_path="/path/to/project",
    analysis_scope="security"
)
```

Analysis scopes:
- `structure`: Project organization
- `security`: Security audit
- `performance`: Performance bottlenecks
- `patterns`: Design patterns
- `all`: Comprehensive analysis

## Best Practices

### 1. Query Optimization
- Be specific in queries for better results
- Provide context when asking questions
- Use appropriate analysis types

### 2. Code Analysis
```python
# Good: Specific analysis with context
analysis = mcp__gemini-mcp__gemini_analyze_code(
    code_content=auth_middleware_code,
    analysis_type="security"
)

# Better: Include surrounding context
full_file = read_file("middleware/auth.js")
analysis = mcp__gemini-mcp__gemini_analyze_code(
    code_content=full_file,
    analysis_type="security"
)
```

### 3. Codebase Analysis
- Start with specific scopes before using "all"
- Use for periodic audits
- Combine with git hooks for PR reviews

### 4. Rate Limiting
- Implement caching for repeated queries
- Batch related analyses
- Use quick_query for simple questions

## Integration Examples

### Hook Integration
```python
# In pattern-extraction-hook.py
class PatternExtractionHook(ToolHook):
    def process(self, request_data, project_context):
        if self._should_analyze_pattern(request_data):
            # Use Gemini for pattern analysis
            code_content = self._extract_code(request_data)
            analysis = mcp__gemini-mcp__gemini_analyze_code(
                code_content=code_content,
                analysis_type="architecture"
            )
            
            # Extract patterns
            patterns = self._extract_patterns(analysis)
            return {
                "patterns": patterns,
                "suggestions": analysis.get("suggestions", [])
            }
```

### Security Scanning
```python
# Automated security scan
def security_scan_pr(pr_files):
    vulnerabilities = []
    
    for file in pr_files:
        if file.endswith(('.js', '.py', '.java')):
            content = read_file(file)
            result = mcp__gemini-mcp__gemini_analyze_code(
                code_content=content,
                analysis_type="security"
            )
            
            if result.get("vulnerabilities"):
                vulnerabilities.extend(result["vulnerabilities"])
    
    return vulnerabilities
```

### Code Review Assistant
```python
# Automated code review
def review_code_changes(diff):
    review = mcp__gemini-mcp__gemini_quick_query(
        query="Review this code diff for issues",
        context=diff
    )
    
    return {
        "summary": review.get("summary"),
        "suggestions": review.get("suggestions"),
        "severity": review.get("severity", "info")
    }
```

## Troubleshooting

### Common Issues

1. **API Key Invalid**
   - Verify key in Google AI Studio
   - Check environment variable is set
   - Ensure key has necessary permissions

2. **Rate Limits**
   ```python
   # Implement exponential backoff
   import time
   
   def retry_gemini_call(func, *args, max_retries=3):
       for i in range(max_retries):
           try:
               return func(*args)
           except RateLimitError:
               wait_time = 2 ** i
               time.sleep(wait_time)
       raise Exception("Max retries exceeded")
   ```

3. **Context Too Large**
   - Break large codebases into chunks
   - Use specific file filtering
   - Focus analysis scope

4. **Timeout Errors**
   - Reduce analysis scope
   - Process files individually
   - Implement async processing

### Debug Tips
```python
# Enable verbose logging
import os
os.environ["GEMINI_DEBUG"] = "true"

# Test connection
test = mcp__gemini-mcp__gemini_quick_query(
    query="Hello, are you working?",
    context="Testing connection"
)
print(f"Connection status: {test}")
```

### Performance Optimization
1. Cache frequent queries
2. Batch similar analyses
3. Use quick_query for simple tasks
4. Schedule heavy analyses during off-hours

---

*See also: [Pattern Extraction Hook](../../logic/hooks.md) | [MCP Overview](../README.md)*