# Notebook - Automated Knowledge Extraction

## Purpose
Automatically extract and store project knowledge in persistent JSON files through intelligent pattern recognition.

## Status: Fully Automated
The notebook functionality is now **fully automated** via the pattern-extraction-hook.py.

## Automation Triggers
1. **Session Save** - When using `/save` command
2. **Significant Changes** - After 5+ files or 100+ lines modified
3. **Memory Capture** - When capturing to Graphiti
4. **Manual** - Via `/logic notebook`

## Legacy Command (Deprecated)
The `/notebook` command has been replaced by automated extraction.
Use `/logic notebook` if manual extraction is needed.

## Auto-Captured Patterns
- Client preferences ("client prefers...")
- Technical constraints ("must use...")
- Performance targets (KB/MB limits)
- API endpoints
- Deadlines
- Design tokens

## Knowledge Files Updated
- `facts.json` - Project facts, requirements
- `patterns.json` - Code patterns, conventions
- `constraints.json` - Technical limits

## Behavior
1. Scan conversation and code for patterns
2. Extract relevant information
3. Deduplicate against existing entries
4. Update appropriate knowledge files
5. Maintain persistence across sessions

## Session Management
- **session**: Creates timestamped markdown in `.claude/project/sessions/current/`
- **archive**: Moves sessions older than 7 days to `.claude/project/sessions/old/`
- Session format: `[topic]-[YYYY-MM-DD].md`
- Includes: objectives, decisions, implementations, outcomes