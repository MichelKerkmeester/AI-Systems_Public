# Graphiti Practical Examples

## Table of Contents

- [Common Use Cases](#common-use-cases)
  - [1. Project Onboarding](#1-project-onboarding)
  - [2. Decision Documentation](#2-decision-documentation)
  - [3. Bug Resolution Tracking](#3-bug-resolution-tracking)
  - [4. Client Preferences](#4-client-preferences)
- [Pattern Examples](#pattern-examples)
  - [Security Patterns](#security-patterns)
  - [Breaking Changes](#breaking-changes)
  - [Code Patterns](#code-patterns)
- [Search Strategies](#search-strategies)
  - [1. Keyword Search](#1-keyword-search)
  - [2. Group-Based Search](#2-group-based-search)
  - [3. Recent Context](#3-recent-context)
  - [4. Combined Searches](#4-combined-searches)
- [Integration Patterns](#integration-patterns)
  - [1. Hook Integration](#1-hook-integration)
  - [2. Decision Capture Hook](#2-decision-capture-hook)
  - [3. Pattern Extraction](#3-pattern-extraction)
- [Memory Management](#memory-management)
  - [1. Organize by Groups](#1-organize-by-groups)
  - [2. Periodic Review](#2-periodic-review)
  - [3. Export Important Memories](#3-export-important-memories)
  - [4. Memory Templates](#4-memory-templates)
- [Best Practices](#best-practices)
## Common Use Cases

### 1. Project Onboarding
When starting work on a project, load relevant context:
```python
# Search for project-specific patterns
memories = mcp__graphiti-gemini__search(
    query={"query": "anobel webflow patterns"}
)

# Get recent work context
recent = mcp__graphiti-gemini__retrieve_episodes(
    last_n=10,
    group_ids=["anobel-project"]
)
```

### 2. Decision Documentation
Document architectural decisions:
```python
# Automatic capture (in conversation)
"DECISION: Implemented lazy loading for images using Intersection Observer API because it reduces initial page load by 40%"

# Manual capture
mcp__graphiti-gemini__add_episode(
    data={
        "name": "Lazy Loading Implementation",
        "episode_body": "Implemented lazy loading using Intersection Observer. Reduces initial load by 40%. Applied to all product images.",
        "group_id": "performance-optimizations"
    }
)
```

### 3. Bug Resolution Tracking
Track how bugs were resolved:
```python
# Automatic pattern
"RESOLVED: Fixed navigation menu z-index issue by setting position:relative on parent container and z-index:9999 on menu"

# This creates a searchable memory for future similar issues
```

### 4. Client Preferences
Store client-specific requirements:
```python
mcp__graphiti-gemini__add_episode(
    data={
        "name": "Client Color Preferences",
        "episode_body": "Client prefers muted colors. Primary: #2C3E50, Secondary: #E74C3C. Avoid bright yellows and greens.",
        "group_id": "anobel-design-system"
    }
)
```

## Pattern Examples

### Security Patterns
```python
# Automatically captured
"SECURITY: Implemented Content Security Policy headers to prevent XSS attacks"

# Creates memory:
{
    "name": "CSP Implementation",
    "episode_body": "Implemented Content Security Policy headers...",
    "tags": ["security", "xss", "headers"]
}
```

### Breaking Changes
```python
# Automatically captured
"BREAKING: Changed API endpoint from /api/v1/products to /api/v2/products with new response format"

# Future searches for "api products" will find this
```

### Code Patterns
```python
# Semi-auto (prompts for confirmation)
"PATTERN: Use data attributes for JavaScript hooks instead of classes"

# Example implementation
"""
<!-- Good -->
<button data-action="submit-form">Submit</button>

<!-- Avoid -->
<button class="js-submit-form">Submit</button>
"""
```

## Search Strategies

### 1. Keyword Search
```python
# Simple keyword search
results = mcp__graphiti-gemini__search(
    query={"query": "responsive navigation"}
)

# Multiple keywords
results = mcp__graphiti-gemini__search(
    query={"query": "webflow custom code optimization"}
)
```

### 2. Group-Based Search
```python
# Search within specific project
results = mcp__graphiti-gemini__search(
    query={
        "query": "performance",
        "group_ids": ["anobel-project"]
    }
)
```

### 3. Recent Context
```python
# Get last 20 memories
recent = mcp__graphiti-gemini__retrieve_episodes(
    last_n=20
)

# Get recent from specific group
recent = mcp__graphiti-gemini__retrieve_episodes(
    last_n=10,
    group_ids=["bug-fixes"]
)
```

### 4. Combined Searches
```python
# First search for patterns
patterns = mcp__graphiti-gemini__search(
    query={"query": "css pattern"}
)

# Then search for related decisions
decisions = mcp__graphiti-gemini__search(
    query={"query": "styling decision"}
)
```

## Integration Patterns

### 1. Hook Integration
```python
# In memory-context-hook.py
class MemoryContextHook:
    def process(self, request_data, project_context):
        # Auto-search based on user input
        keywords = self.extract_keywords(request_data)
        
        if keywords:
            memories = mcp__graphiti-gemini__search(
                query={"query": " ".join(keywords)}
            )
            
            return {
                "context_memories": memories,
                "keywords_detected": keywords
            }
```

### 2. Decision Capture Hook
```python
# Automatic decision capture
def capture_decision(content):
    if content.startswith("DECISION:"):
        decision_text = content[9:].strip()
        
        mcp__graphiti-gemini__add_episode(
            data={
                "name": f"Decision: {decision_text[:50]}",
                "episode_body": decision_text,
                "group_id": "architectural-decisions"
            }
        )
```

### 3. Pattern Extraction
```python
# Extract and store patterns
def extract_pattern(code_block, description):
    mcp__graphiti-gemini__add_episode(
        data={
            "name": f"Code Pattern: {description}",
            "episode_body": f"{description}\n\nExample:\n```\n{code_block}\n```",
            "group_id": "code-patterns"
        }
    )
```

## Memory Management

### 1. Organize by Groups
```python
# Project-specific memories
project_groups = {
    "anobel-project": "Main project group",
    "anobel-bugs": "Bug fixes and resolutions",
    "anobel-features": "Feature implementations",
    "anobel-design": "Design decisions and patterns"
}

# Add memory with appropriate group
mcp__graphiti-gemini__add_episode(
    data={
        "name": "Feature: Dark Mode",
        "episode_body": "Implemented dark mode using CSS custom properties...",
        "group_id": "anobel-features"
    }
)
```

### 2. Periodic Review
```python
# Review recent memories for quality
recent = mcp__graphiti-gemini__retrieve_episodes(last_n=50)

# Identify memories that need updating or removal
for memory in recent:
    if "deprecated" in memory["content"].lower():
        # Flag for review
        print(f"Review needed: {memory['name']}")
```

### 3. Export Important Memories
```python
# Export critical decisions
decisions = mcp__graphiti-gemini__search(
    query={"query": "DECISION"}
)

# Save to project documentation
with open("docs/decisions.md", "w") as f:
    for decision in decisions:
        f.write(f"## {decision['name']}\n")
        f.write(f"{decision['content']}\n\n")
```

### 4. Memory Templates
```python
# Template for bug fixes
bug_template = {
    "name": "Bug: {issue_description}",
    "episode_body": """
Issue: {issue_description}
Symptoms: {symptoms}
Root Cause: {root_cause}
Solution: {solution}
Prevention: {prevention}
    """,
    "group_id": "bug-fixes"
}

# Template for patterns
pattern_template = {
    "name": "Pattern: {pattern_name}",
    "episode_body": """
Pattern: {pattern_name}
Use Case: {use_case}
Implementation: {implementation}
Benefits: {benefits}
Example: {code_example}
    """,
    "group_id": "code-patterns"
}
```

## Best Practices

1. **Use Consistent Naming**: Start memory names with type (Bug:, Pattern:, Decision:)
2. **Group Logically**: Use groups to organize related memories
3. **Include Examples**: Always include code examples in pattern memories
4. **Regular Cleanup**: Review and update memories periodically
5. **Search Before Adding**: Check if similar memory exists before creating new

---

*See also: [Memory Verification Guide](./memory-verifcation-guide.md) | [Main README](./README.md)*