# Memory Automation v2 Requirements

**Created:** 2025-07-21
**Priority:** Critical
**Type:** System Enhancement
**Estimated Effort:** 3-4 days

## Problem Statement

Current memory system captures only 1-2 memories per day despite "full" automation setting. The hooks detect patterns but only suggest captures - they don't execute them. This leads to:

- Lost context between sessions
- Repeated problem-solving
- Missing critical decisions and patterns
- Over-reliance on manual memory commands

Target: 50+ automated captures per day with zero manual intervention.

## Current State Analysis

### Working Components
- ✅ Graphiti MCP connection to Neo4j
- ✅ Pattern detection (14+ patterns)
- ✅ Hook infrastructure
- ✅ Memory storage and retrieval

### Not Working
- ❌ Automatic execution of captures
- ❌ Conversation buffer integration
- ❌ CLAUDE.md enforcement
- ❌ Proactive memory search before tasks

## Functional Requirements

### 1. True Automation (Priority: Critical)
- Hooks must directly execute MCP calls, not just suggest them
- No user intervention required for standard patterns
- Batch processing for efficiency (every 5 captures)

### 2. Multi-Layer Enforcement (Priority: High)
- **Layer 1:** Hook-based automatic capture
- **Layer 2:** CLAUDE.md rules requiring memory operations
- **Layer 3:** Pre-task memory search enforcement
- **Layer 4:** Post-task capture verification

### 3. Capture Triggers (Priority: High)
Automatic capture on:
- Pattern detection (existing 14+ patterns)
- Every 5 conversation exchanges
- After significant tool operations
- Task completions
- Error resolutions
- New patterns discovered

### 4. Memory Search Integration (Priority: High)
- Mandatory memory search before starting tasks
- Automatic context loading on startup
- Relevant memory injection during conversations

### 5. User Control (Priority: Medium)
- `/memory auto [off|manual|semi|full]` respected
- Emergency disable option
- Memory privacy settings
- Capture notifications (optional)

## Non-Functional Requirements

### Performance
- Capture latency < 100ms
- No noticeable conversation slowdown
- Batch processing to reduce API calls
- Async capture to prevent blocking

### Reliability
- Graceful handling of Graphiti failures
- Local queue for failed captures
- Retry mechanism with exponential backoff
- No data loss during outages

### Observability
- Daily capture statistics
- Pattern hit rates
- Memory search effectiveness metrics
- Automation success rate tracking

## Success Criteria

1. **Capture Volume:** 50+ memories/day average
2. **Automation Rate:** 95%+ without manual intervention
3. **Pattern Coverage:** All defined patterns captured
4. **Search Usage:** Memory searched before 90% of tasks
5. **Performance:** No user-perceivable latency

## Constraints

- Must work within Claude Code CLI environment
- Cannot modify core Claude behavior
- Must respect user privacy settings
- Neo4j/Graphiti must remain operational
- Backward compatible with existing memories

## Dependencies

- Graphiti MCP server
- Neo4j database
- Python subprocess for MCP execution
- Claude Code hooks system
- CLAUDE.md enforcement mechanism

## Out of Scope

- Memory UI/visualization
- Memory export features
- Cross-project memory sharing
- Memory versioning/history
- Advanced NLP analysis