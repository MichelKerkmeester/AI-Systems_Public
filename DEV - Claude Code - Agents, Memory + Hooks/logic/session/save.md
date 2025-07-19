# /save Command

Manage Claude Code sessions for better organization and tracking.

## Usage

```bash
/save                    # Save and archive current session
/save new [description]  # Create new session (archives current)
/save list              # List all sessions
/save search [query]    # Search session content
/save stats             # Session statistics
```

## Aliases
- `/s` - Short form (legacy compatibility)

## Features

### Automatic Session Management
With hooks configured, sessions are automatically:
- Created after 4-hour timeout
- Named with timestamp and context
- Archived when limit (10) exceeded
- Backed up before deletion

### Manual Control
Use this command to:
- Save current session progress
- Force new session for task changes
- Search across all sessions
- View session statistics
- Check current session status

## Session Structure
```
.claude/project/sessions/
├── current/       # Active session files
├── old/           # Archived sessions (max 10)
├── backups/       # Compressed archives (max 5)
└── .current-session  # State tracking

# Multi-agent structure (when enabled)
.claude/agents/{AGENT_ID}/sessions/
├── current/       # Agent-specific sessions
├── archived/      # Agent archives
└── .session-state.json  # Agent state
```

## Examples

### Save Current Session
```bash
/save
# Archives current session and starts fresh
```

### Start New Feature Session
```bash
/save new authentication-feature
```

### Search Sessions
```bash
/save search "api integration"
# Searches all sessions for content
```

### View Statistics
```bash
/save stats
# Shows:
# - Total sessions: 45
# - Active: 1
# - Archived: 10
# - Total size: 2.3 MB
# - Average session: 3.2 hours
```

### List Recent Sessions
```bash
/save list
# Shows current and last 10 archived sessions
```

## Integration

Works with:
- `/memory` - Links memory captures to sessions
- `/logic notebook` - Extracts patterns per session
- Graphiti - Associates memories with sessions

## Session Enhancement Features

### Auto-Summary Generation
Sessions automatically generate summaries including:
- Files modified/created
- Key decisions made
- Tasks completed
- Patterns discovered

### Memory Linking
Each session is linked to:
- Memory captures during that period
- Extracted patterns and insights
- Related documentation updates

## Implementation

The session management is handled by:
1. **Automatic**: Hook at `.claude/logic/session/hooks/session-hook.py`
2. **Manual**: Command at `.claude/logic/session/commands/save-command.py`
3. **Shell Script**: `.claude/project/sessions/session-manager.sh`

All methods ensure consistent session tracking and organization.