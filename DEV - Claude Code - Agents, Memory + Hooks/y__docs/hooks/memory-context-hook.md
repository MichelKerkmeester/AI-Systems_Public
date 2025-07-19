# Memory Context Hook

## Overview

**Hook Name**: Memory Context Hook  
**Purpose**: Provides contextual memory hints and suggestions during development  
**Location**: `/hooks/memory/memory-context-hook.py`  
**Triggers**: UserPromptSubmit events  
**Priority**: 4 (Context enhancement)  
**Performance**: ~8ms typical execution time

## Description

The Memory Context Hook integrates with the Graphiti memory system to provide relevant context and suggestions based on stored memories. It detects keywords in user prompts and surfaces related patterns, decisions, and constraints from the knowledge base.

## Configuration

Settings are managed through the Memory section in CLAUDE.md:

```python
Memory Configuration:
- auto_context: true         # Enable automatic context
- context_on_startup: true   # Load context at startup
- max_relevant_memories: 5   # Limit displayed memories
- show_suggestions: true     # Show memory-based suggestions
```

## How It Works

1. **Keyword Detection**:
   - Scans prompts for technical terms
   - Identifies project-specific patterns
   - Matches against memory tags

2. **Memory Retrieval**:
   - Queries Graphiti for relevant memories
   - Ranks by relevance score
   - Limits to configured maximum

3. **Context Presentation**:
   - Shows related patterns
   - Displays past decisions
   - Highlights constraints

4. **Smart Suggestions**:
   - Based on similar past scenarios
   - Leverages learned patterns
   - Prevents repeated mistakes

## Example Usage

### Pattern Recognition
```
User: "I need to implement a hero section"

🧠 Memory Context

Found 3 relevant memories:

1. Hero Implementation Pattern (2 weeks ago)
   - Used intersection observer for animations
   - REM units for responsive scaling
   - Webflow class: .hero-wrapper

2. Performance Constraint (1 month ago)
   - Hero images must be <500KB
   - Use WebP format with fallback
   - Lazy load below-fold content

3. Design Decision (3 weeks ago)
   - Maintain 16:9 aspect ratio
   - Mobile-first breakpoints
   - Accessibility: min contrast 4.5:1
```

### Constraint Warnings
```
User: "Let me add a video background"

⚠️ Platform Constraint Detected

Previous memory: "Webflow video limitations"
- Autoplay requires muted attribute
- Mobile fallback image required
- Max file size: 30MB
- Supported formats: MP4, WebM

Consider: Static image with subtle animation
```

## Memory Categories

### Facts
- Technical discoveries
- Platform capabilities
- API specifications
- Performance benchmarks

### Patterns
- Implementation approaches
- Code structures
- Solution templates
- Best practices

### Constraints
- Platform limitations
- Security requirements
- Performance boundaries
- Business rules

## Integration Points

- **Graphiti MCP**: Memory storage and retrieval
- **Pattern Extraction Hook**: Feeds new memories
- **Context Management Hook**: Shares context data
- **Task Management**: Memory linked to tasks

## Performance Optimization

- Keyword indexing for fast lookup
- Caches recent queries
- Async memory fetching
- Relevance threshold filtering

## Advanced Features

### Memory Weighting
```python
relevance_factors = {
    "recency": 0.3,      # Recent memories weighted higher
    "frequency": 0.2,    # Often-accessed memories
    "similarity": 0.4,   # Keyword match strength
    "importance": 0.1    # Manual importance flag
}
```

### Context Filtering
```python
filters = {
    "min_relevance": 0.7,
    "max_age_days": 90,
    "categories": ["patterns", "constraints"],
    "exclude_tags": ["deprecated", "experimental"]
}
```

## Troubleshooting

### No Context Shown
- Check memory system connection
- Verify keywords match stored memories
- Lower relevance threshold
- Ensure memories exist for topic

### Too Much Context
- Increase relevance threshold
- Reduce max_relevant_memories
- Add exclusion filters
- Focus keyword matching

### Outdated Suggestions
- Update memory timestamps
- Archive old memories
- Refresh memory index
- Clear cache

## Manual Memory Control

- Search memories: `/memory search [query]`
- Add memory: `/memory add [content]`
- View all: `/memory list`
- Clear context: `/memory context clear`

## Memory Quality

### Good Memory Entry
```json
{
  "content": "Use data-wf-* attributes for Webflow interactions",
  "type": "pattern",
  "tags": ["webflow", "interactions", "attributes"],
  "context": {
    "file": "components/animations.js",
    "decision_reason": "Maintains platform compatibility"
  }
}
```

### Poor Memory Entry
```json
{
  "content": "Fixed bug",
  "type": "fact"
  // Missing context, tags, and specifics
}
```

## Privacy & Security

- No sensitive data in memories
- API keys never stored
- Personal info excluded
- Memories are project-scoped

## Related Documentation

- [Graphiti Memory System](../../graphiti/README.md)
- [Memory Verification Guide](../../graphiti/memory-verification-guide.md)
- [Pattern Extraction Hook](./pattern-extraction-hook.md)