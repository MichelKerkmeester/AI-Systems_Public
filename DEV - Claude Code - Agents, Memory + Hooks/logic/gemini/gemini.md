# /gemini - AI Analysis Enhancement

## Purpose
Optional Gemini AI integration for advanced code analysis and token reduction.

## Usage
- `/gemini` - Check availability
- `/gemini [mode]` - Specific analysis
- `/g` - Short alias

## Modes
- **review** - Code review with insights
- **optimize** - Performance optimization
- **security** - Security analysis
- **patterns** - Pattern detection
- **compare** - Before/after analysis

## Quick Access
- `/gemini-review` or `/gr`
- `/gemini-optimize` or `/go`
- `/gemini-security` or `/gs`
- `/gemini-patterns` or `/gp`

## Benefits When Available
- 65-85% token reduction
- Cross-file pattern recognition
- Parallel processing
- Intelligent summarization

## Fallback Behavior
When Gemini unavailable:
- Grep/Read tools for analysis
- Rule-based optimization
- Pattern matching for security
- Template-based formatting

## Behavior
1. Check if Gemini MCP available
2. Prompt user for optional enhancement
3. Execute enhanced analysis if approved
4. Fall back to standard tools if declined
5. Maintain full functionality either way