# Session Documentation

This directory contains session summaries and documentation for significant work sessions.

## Directory Structure

```
sessions/
├── current/     # Active and recent session documentation
├── old/         # Archived sessions (moved after 7+ days)
└── README.md    # This file
```

## Session Naming Convention

`[topic]-[YYYY-MM-DD].md`

Examples:
- `graphiti-memory-implementation-2025-01-17.md`
- `api-integration-2025-01-15.md`
- `performance-optimization-2025-01-10.md`

## Session Content Structure

Each session file should include:

1. **Header**
   - Date
   - Project
   - Focus/Topic

2. **Objectives**
   - What problems are being solved
   - Expected outcomes

3. **Implementation**
   - Files created/modified
   - Key code changes
   - Architecture decisions

4. **Decisions** (marked with DECISION:)
   - Important choices made
   - Rationale behind decisions

5. **Outcomes**
   - What was accomplished
   - Next steps
   - Any blockers

## Creating Sessions

Use `/notebook session` to generate a session markdown based on current work.

## Archiving

Sessions older than 7 days should be moved to the `old/` directory. This can be done:
- Manually when starting a new conversation
- Using `/notebook archive` command
- During context refresh operations

## Purpose

These session files serve as:
- Knowledge persistence between conversations
- Documentation of major changes
- Decision history
- Implementation reference