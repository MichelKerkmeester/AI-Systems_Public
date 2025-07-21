# Memory Context Hook v2 Documentation

## Overview

The Enhanced Memory Context Hook v2 is a significant upgrade to the memory management system, introducing background processing, priority-based capture, and enhanced pattern detection for code reuse scenarios.

## Key Features

### 1. **Background Processing with MemoryCaptureQueue**
- Non-blocking memory capture using Python's threading and queue modules
- Priority queue ensures critical memories (security, breaking changes) are processed first
- Daemon thread handles processing without blocking user interaction

### 2. **MCPBridge Abstraction**
- Clean interface for MCP tool communication
- Simulated mode for testing without actual MCP connection
- Easy integration with Graphiti memory system

### 3. **Enhanced Pattern Detection**
New patterns specifically for code reuse:
- `REUSABLE_COMPONENT`: Detects mentions of reusable code elements
- `EXISTING_SOLUTION`: Identifies references to existing implementations
- `REFACTOR_OPPORTUNITY`: Catches suggestions for code consolidation

### 4. **Priority System**
Four priority levels ensure important memories are captured first:
1. **CRITICAL**: Security issues, breaking changes
2. **HIGH**: Decisions, patterns, reusable components
3. **MEDIUM**: Bug fixes, optimizations, refactor opportunities
4. **LOW**: General learnings, configuration changes

### 5. **Enhanced Context Extraction**
- Captures 150 characters of context around detected patterns
- Extracts file paths and line numbers when mentioned
- Preserves surrounding context for better memory retrieval

## Configuration

The hook uses settings from `.claude/settings.json`:

```json
{
  "memory": {
    "auto_context": true,
    "context_on_startup": true,
    "max_relevant_memories": 5,
    "show_suggestions": true,
    "v2_features": {
      "background_processing": true,
      "enhanced_patterns": true,
      "context_extraction": true,
      "priority_queue": true,
      "file_context_tracking": true
    }
  }
}
```

## Pattern Categories

### Critical Patterns (Priority 1)
- **SECURITY**: API keys, tokens, credentials, authentication
- **BREAKING**: Breaking changes, migrations, deprecations

### High Priority Patterns (Priority 2)
- **DECISION**: Architecture decisions, technology choices
- **PATTERN**: Coding patterns, conventions, standards
- **REUSABLE_COMPONENT**: Existing components that can be reused
- **EXISTING_SOLUTION**: Already implemented solutions

### Medium Priority Patterns (Priority 3)
- **RESOLVED**: Bug fixes, issue resolutions
- **ERROR_FIX**: Specific error corrections
- **OPTIMIZATION**: Performance improvements
- **REFACTOR_OPPORTUNITY**: Code that could be consolidated

### Low Priority Patterns (Priority 4)
- **USER_FEEDBACK**: Client requirements, user requests
- **CONFIG_CHANGE**: Configuration updates
- **LEARNING**: Discoveries, insights
- **ARCHITECTURE**: System design decisions
- **API_CHANGE**: Interface modifications
- **DEPENDENCY**: Package updates, library changes

## Implementation Details

### Memory Item Structure
```python
@dataclass
class MemoryItem:
    content: str
    memory_type: str
    context: str
    priority: MemoryPriority
    timestamp: datetime
    file_path: Optional[str] = None
    line_number: Optional[int] = None
```

### Queue Statistics
The hook tracks:
- Queued items waiting for processing
- Successfully processed memories
- Failed capture attempts
- Session memory count by type

### Thread Safety
- Uses thread-safe `queue.PriorityQueue`
- Daemon thread ensures clean shutdown
- No shared mutable state between threads

## Usage Examples

### Example 1: Detecting Reusable Components
```
User: "Found existing authentication component we can reuse instead of creating new"
Hook: Captures with EXISTING_SOLUTION and REUSABLE_COMPONENT patterns
```

### Example 2: File Context Extraction
```
User: "Fixed bug in /src/utils/helper.js:42 by adding validation"
Hook: Captures with file_path="/src/utils/helper.js", line_number=42
```

### Example 3: Priority Processing
```
User: "The API key was exposed, need to rotate it and update security"
Hook: CRITICAL priority ensures immediate processing
```

## Testing

Run the test suite:
```bash
python3 .claude/tests/test-memory-hook-v2.py
```

Tests verify:
- Pattern detection accuracy
- Command skipping (e.g., `/memory` commands)
- Context extraction
- Priority assignment
- Background processing

## Migration from v1

To upgrade from the original memory-context-hook:

1. Update `settings.json` to point to the new hook
2. No data migration needed - uses same Graphiti backend
3. Enhanced features are automatically enabled

## Performance Considerations

- Non-blocking design ensures no UI lag
- Background thread uses minimal resources
- Queue has no hard size limit but processes continuously
- Simulated mode available for testing without MCP overhead

## Future Enhancements

Potential improvements:
- Batch processing for multiple memories
- Persistent queue for crash recovery
- Memory deduplication
- Smart context merging for related patterns
- Integration with other hooks for richer context