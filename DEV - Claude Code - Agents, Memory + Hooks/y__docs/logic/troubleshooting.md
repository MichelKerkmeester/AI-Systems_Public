# Troubleshooting Guide

## Table of Contents

  - [🚫 Hooks Not Running](#-hooks-not-running)
  - [🔒 Hook Blocking Operations](#-hook-blocking-operations)
  - [💾 Session Issues](#-session-issues)
  - [🧠 Memory Problems](#-memory-problems)
  - [⚡ Performance Issues](#-performance-issues)
  - [🔐 Security Warnings](#-security-warnings)
  - [📝 Pattern Extraction Issues](#-pattern-extraction-issues)
  - [🔄 Multi-Agent Conflicts](#-multi-agent-conflicts)
- [Debug Commands](#debug-commands)
  - [Information Gathering](#information-gathering)
  - [Reset Commands](#reset-commands)
  - [Emergency Recovery](#emergency-recovery)
- [Error Messages](#error-messages)
  - ["Session timeout exceeded"](#session-timeout-exceeded)
  - ["Hook execution failed"](#hook-execution-failed)
  - ["Pattern already exists"](#pattern-already-exists)
  - ["Lock acquisition timeout"](#lock-acquisition-timeout)
- [Getting Help](#getting-help)
**Symptoms:**
- Expected automation not happening
- No session creation after 4 hours
- Memory not loading automatically

**Solutions:**
1. Check hook status:
   ```bash
   /logic hooks status
   ```

2. Verify hooks enabled in settings:
   ```json
   {
     "hooks": {
       "enabled": true
     }
   }
   ```

3. Check for path issues (spaces need quotes):
   ```json
   {
     "command": "python3 '/path with spaces/hook.py'"
   }
   ```

4. Run with debug mode:
   ```bash
   claude --debug
   ```

### 🔒 Hook Blocking Operations

**Symptoms:**
- "Hook blocked this operation" messages
- Can't save files
- Operations failing unexpectedly

**Solutions:**
1. Check hook output for specific errors
2. Temporarily disable problematic hook:
   ```bash
   /logic hooks disable [hook-name]
   ```
3. Emergency disable all hooks:
   ```bash
   /logic emergency disable
   ```

### 💾 Session Issues

**Symptoms:**
- Sessions not saving
- Lost work after crash
- Session files corrupted

**Solutions:**
1. Check current session:
   ```bash
   cat .claude/project/state/.current-session
   ```

2. Manually create new session:
   ```bash
   /save new recovery-session
   ```

3. Check session directory permissions:
   ```bash
   ls -la .claude/project/sessions/current/
   ```

4. Recovery from backup:
   ```bash
   cd .claude/project/sessions/backups/
   tar -xzf backup-*.tar.gz
   ```

### 🧠 Memory Problems

**Symptoms:**
- Memory context not loading
- Graphiti connection errors
- Captures not working

**Solutions:**
1. Check memory status:
   ```bash
   /memory
   ```

2. Test Graphiti connection:
   ```bash
   python3 .claude/logic/memory/check-neo4j.py
   ```

3. Reset automation level:
   ```bash
   /memory auto manual
   /memory auto semi  # Set back to desired
   ```

4. Check memory settings:
   ```bash
   cat .claude/logic/memory/settings.json
   ```

### ⚡ Performance Issues

**Symptoms:**
- Slow response times
- Hooks timing out
- System feels sluggish

**Solutions:**
1. Check metrics:
   ```bash
   /logic metrics
   ```

2. Disable non-critical hooks:
   ```bash
   /logic hooks disable pattern-extraction-hook
   /logic hooks disable quality-hook
   ```

3. Reduce automation level:
   ```bash
   /memory auto manual
   ```

4. Clear old sessions:
   ```bash
   rm .claude/project/sessions/old/*
   ```

### 🔐 Security Warnings

**Symptoms:**
- API key detection alerts
- Security scan blocking writes
- Unexpected security messages

**Solutions:**
1. Never store keys in code/docs
2. Use environment variables:
   ```bash
   export API_KEY=your-key
   ```

3. If false positive, add to exceptions:
   ```json
   {
     "security": {
       "exclude_patterns": ["test_api_key"]
     }
   }
   ```

### 📝 Pattern Extraction Issues

**Symptoms:**
- Patterns not being captured
- Knowledge files not updating
- Duplicate entries

**Solutions:**
1. Force manual extraction:
   ```bash
   /logic notebook
   ```

2. Check pattern files:
   ```bash
   ls -la .claude/project/knowledge/*.json
   ```

3. Validate JSON syntax:
   ```bash
   python3 -m json.tool .claude/project/knowledge/patterns.json
   ```

### 🔄 Multi-Agent Conflicts

**Symptoms:**
- Lock acquisition timeouts
- Conflicting session names
- Agent isolation not working

**Solutions:**
1. Check agent status:
   ```bash
   /logic agents status
   ```

2. Clear stale locks:
   ```bash
   rm .claude/project/state/locks/*.lock
   ```

3. Set unique agent ID:
   ```bash
   export CLAUDE_AGENT_ID=agent2
   ```

## Debug Commands

### Information Gathering
```bash
# System status
/logic emergency report

# Hook configuration
/logic hooks list

# Session information
/save stats

# Memory status
/memory
```

### Reset Commands
```bash
# Reset test state
rm .claude/project/state/test-state.json

# Clear session state
rm .claude/project/state/.current-session

# Reset all tracking
rm -rf .claude/project/state/*
```

### Emergency Recovery
```bash
# Disable all automation
/logic emergency disable

# Restore from recovery point
python3 .claude/logic/shared/hook_state.py --recover

# Full system reset
/logic emergency reset
```

## Error Messages

### "Session timeout exceeded"
- **Cause**: Session older than 4 hours
- **Fix**: Automatic - new session will be created
- **Manual**: `/save new`

### "Hook execution failed"
- **Cause**: Python error in hook script
- **Fix**: Check hook file syntax
- **Debug**: Run hook manually with test input

### "Pattern already exists"
- **Cause**: Duplicate pattern detection
- **Fix**: Normal - prevents duplicates
- **Override**: Edit knowledge JSON directly

### "Lock acquisition timeout"
- **Cause**: Another agent has lock
- **Fix**: Wait and retry
- **Force**: Remove lock file manually

## Getting Help

1. **Built-in help**:
   ```bash
   /logic help troubleshooting
   ```

2. **Debug mode**:
   ```bash
   claude --debug
   ```

3. **Check documentation**:
   - `.claude/logic/global/hooks-in-cc.md`
   - `.claude/docs/logic-help/`

4. **Emergency recovery**:
   ```bash
   /logic emergency
   ```