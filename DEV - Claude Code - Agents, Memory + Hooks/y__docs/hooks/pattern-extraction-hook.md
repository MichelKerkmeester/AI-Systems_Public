# Pattern Extraction Hook

## Overview

**Hook Name**: Pattern Extraction Hook  
**Purpose**: Automatically extracts and categorizes patterns using Gemini integration  
**Location**: `/hooks/core/pattern-extraction-hook.py`  
**Triggers**: PostToolUse events, session saves  
**Priority**: 4 (Knowledge extraction)  
**Performance**: ~50ms typical (includes Gemini API call)

## Description

The Pattern Extraction Hook uses Gemini AI to automatically identify, extract, and categorize patterns from your development session. It replaces the manual `/notebook` command by intelligently analyzing code changes, decisions, and solutions to build a knowledge base of reusable patterns.

## Configuration

Settings file: `/hooks/core/notebook-settings.json`

```json
{
  "enabled": true,
  "auto_extract": true,
  "min_content_threshold": 100,  // Min chars for extraction
  "gemini_model": "gemini-pro",
  "extraction_triggers": {
    "session_save": true,
    "significant_changes": true,
    "pattern_keywords": true
  },
  "categories": ["facts", "patterns", "constraints"]
}
```

## How It Works

1. **Monitors Activity**:
   - Tracks code changes and decisions
   - Identifies pattern indicators
   - Collects context for analysis

2. **Triggers Extraction**:
   - On session saves
   - After significant code changes
   - When pattern keywords detected

3. **Gemini Analysis**:
   - Sends context to Gemini
   - Extracts structured patterns
   - Categorizes into facts/patterns/constraints

4. **Updates Knowledge Base**:
   - Adds to `facts.json`, `patterns.json`, `constraints.json`
   - Prevents duplicates
   - Maintains relationships

## Example Usage

### Automatic Pattern Detection
```python
# User implements a new validation pattern
class EmailValidator:
    def validate(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

# Hook detects and extracts:
Pattern Extracted: "Email Validation"
Category: patterns
Tags: ["validation", "regex", "email"]
Context: Implementation of email validation using regex
```

### Knowledge Base Update
```json
// Added to patterns.json
{
  "id": "email-validation-2025-01-19",
  "name": "Email Validation Pattern",
  "category": "validation",
  "code": "pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'",
  "usage": "EmailValidator class for form validation",
  "context": {
    "file": "validators.py",
    "session": "2025-01-19-session",
    "tags": ["email", "regex", "validation"]
  }
}
```

## Gemini Integration

### Prompt Engineering
The hook uses optimized prompts for pattern extraction:

```python
prompt = """
Analyze this code change and extract:
1. Reusable patterns
2. Technical decisions (facts)
3. Platform constraints discovered

Context: {context}
Change: {change}

Return structured JSON with categories.
"""
```

### Response Processing
- Validates Gemini responses
- Ensures proper categorization
- Handles API errors gracefully
- Falls back to local extraction

## Categories

### Facts
- Technical discoveries
- Platform capabilities
- API limitations
- Performance findings

### Patterns
- Code patterns
- Architecture patterns
- Solution templates
- Best practices

### Constraints
- Platform limits
- Security requirements
- Performance boundaries
- Compatibility issues

## Integration Points

- **Gemini MCP**: API integration for analysis
- **Memory System**: Patterns stored in Graphiti
- **Session Management**: Triggered on saves
- **Context Hook**: Uses context for better extraction

## Performance Optimization

- Batches extractions to reduce API calls
- Caches similar patterns
- Async processing to avoid blocking
- Local fallback for common patterns

## Advanced Features

### Custom Extraction Rules
```json
{
  "custom_patterns": {
    "webflow_integration": {
      "triggers": ["Webflow", "wf-", "data-wf"],
      "extract": ["selectors", "events", "constraints"]
    }
  }
}
```

### Pattern Relationships
```json
{
  "pattern_links": {
    "validation-base": ["email-validation", "phone-validation"],
    "form-patterns": ["validation-base", "error-handling"]
  }
}
```

## Troubleshooting

### Patterns Not Extracting
- Check content threshold
- Verify Gemini API key
- Ensure triggers are enabled
- Check session content size

### Duplicate Patterns
- Pattern deduplication is automatic
- Check pattern IDs in JSON files
- Clear cache if needed

### API Errors
- Fallback to local extraction
- Check API quotas
- Verify network connectivity
- Review error logs

## Manual Control

While automatic, you can:
- Force extraction: `/logic notebook extract`
- View patterns: `/logic notebook list`
- Search patterns: `/memory search patterns`

## Related Documentation

- [Gemini MCP Integration](../mcp/gemini/README.md)
- [Memory System Guide](../../graphiti/practical-examples.md)
- [Knowledge Base Structure](../../project/knowledge/README.md)