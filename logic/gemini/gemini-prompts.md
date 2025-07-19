# Gemini Enhancement Prompts Helper

## Purpose
This file contains the logic for when and how to prompt users about optional Gemini enhancements.

## Prompt Function Logic

### shouldPromptForGemini(command, context)
```javascript
function shouldPromptForGemini(command, context) {
  // Check if Gemini is optional (from config)
  if (!config.settings.gemini_optional) return false;
  
  // Check command-specific triggers
  const triggers = config.gemini_enhancement_triggers[command];
  if (!triggers) return false;
  
  // Evaluate conditions
  return triggers.conditions.some(condition => {
    // Parse and evaluate condition
    // Examples: "files_count > 20", "test_type === 'full'"
    return evaluateCondition(condition, context);
  });
}
```

### showGeminiPrompt(command)
```javascript
function showGeminiPrompt(command) {
  const trigger = config.gemini_enhancement_triggers[command];
  
  console.log(`
[🤖 Optional Enhancement Available]
${trigger.prompt}
Enable Gemini analysis? [y/N]: _
  `);
  
  // Default to 'n' if no response or invalid input
  const response = getUserInput();
  return response.toLowerCase() === 'y';
}
```

## Integration Points

### 1. /workflow command
**When to prompt**: 
- Files count > 20
- Complexity is medium or higher
- User specifically requests optimization

**Benefits shown**:
- ~70% token reduction
- Cross-file pattern analysis
- Parallel processing

### 2. /test command
**When to prompt**:
- Running full test suite
- 10+ files to analyze
- Complex validation needed

**Benefits shown**:
- Pattern detection
- Optimization insights
- Comprehensive security analysis

### 3. /context command
**When to prompt**:
- Export operation
- Context score > 80
- Large session data

**Benefits shown**:
- 80% smaller export size
- Intelligent summarization
- Key insights extraction

### 4. /notebook command
**When to prompt**:
- Extract operation
- 5+ patterns found
- Complex knowledge base

**Benefits shown**:
- Enhanced pattern recognition
- Relationship mapping
- Automated categorization

## Fallback Behaviors

When Gemini is not used (user declines or unavailable):

### Code Analysis Fallback
```javascript
function analyzeCodeWithoutGemini(files) {
  // Use Grep for pattern matching
  const patterns = config.fallback_behaviors.code_analysis.patterns;
  const results = [];
  
  for (const pattern of patterns) {
    const matches = grep(pattern, files);
    results.push(processMatches(matches));
  }
  
  return consolidateResults(results);
}
```

### Optimization Fallback
```javascript
function optimizeWithoutGemini(code) {
  const checks = config.fallback_behaviors.optimization.checks;
  const suggestions = [];
  
  // Rule-based checks
  if (checkBundleSize(code) > threshold) {
    suggestions.push("Consider code splitting");
  }
  
  if (findUnusedImports(code).length > 0) {
    suggestions.push("Remove unused imports");
  }
  
  return suggestions;
}
```

### Security Fallback
```javascript
function securityCheckWithoutGemini(files) {
  const patterns = config.fallback_behaviors.security.patterns;
  const issues = [];
  
  for (const pattern of patterns) {
    const matches = grep(pattern, files);
    if (matches.length > 0) {
      issues.push({
        type: pattern,
        locations: matches,
        severity: getSeverity(pattern)
      });
    }
  }
  
  return issues;
}
```

## User Experience Guidelines

1. **Non-intrusive**: Only prompt when significant benefit exists
2. **Clear benefits**: Always show what user gains
3. **Quick default**: Default to 'n' for fast workflow
4. **Remember choice**: Cache decision for session
5. **No pressure**: Work perfectly without Gemini

## Implementation Notes

- Prompts should appear BEFORE the operation starts
- Show progress indicators for both paths
- Cache Gemini availability check
- Log user choices for analytics
- Ensure graceful degradation