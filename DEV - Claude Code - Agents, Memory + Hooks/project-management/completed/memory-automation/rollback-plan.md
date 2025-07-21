# Memory Automation v2 Rollback Plan

## Overview

This plan ensures we can quickly and safely revert to the current memory system if issues arise with v2 automation. All changes are designed to be reversible within 5 minutes.

## Rollback Triggers

Immediate rollback if any of these occur:
1. Memory capture rate drops below baseline (8/day)
2. System latency increases >500ms
3. Queue grows unbounded (>1000 items)
4. Error rate exceeds 5%
5. User reports significant issues
6. Neo4j/Graphiti connection failures >10%

## Pre-Deployment Checklist

### 1. Backup Current System
```bash
# Create timestamped backup
./backup_memory_system.sh
# Creates: .claude/backups/memory-system-[timestamp]/
```

### 2. Document Current State
```bash
# Capture current metrics
python capture_baseline_metrics.py > baseline-metrics.json

# Backup current hooks
cp -r .claude/logic/hooks/memory/ .claude/backups/hooks-memory-v1/

# Save current settings
cp .claude/settings.json .claude/backups/settings-v1.json
```

### 3. Create Rollback Scripts
```bash
# Quick rollback script
cat > rollback_memory_v2.sh << 'EOF'
#!/bin/bash
echo "🔄 Rolling back Memory Automation v2..."

# Restore hooks
cp -r .claude/backups/hooks-memory-v1/* .claude/logic/hooks/memory/

# Restore settings
cp .claude/backups/settings-v1.json .claude/settings.json

# Clear any queued memories
rm -f .claude/state/memory_queue.json

# Restart services
./restart_claude_services.sh

echo "✅ Rollback complete"
EOF

chmod +x rollback_memory_v2.sh
```

## Rollback Procedures

### Level 1: Quick Disable (30 seconds)
For minor issues - disables v2 features while keeping system running

```bash
# Via command
/logic emergency disable memory-v2

# Or manually edit settings.json
{
  "memory": {
    "automation_version": "1.0",  # Revert from 2.0
    "execution_mode": "prompt"     # Revert from "direct"
  }
}
```

### Level 2: Hook Rollback (2 minutes)
For hook-related issues

```bash
# Restore v1 hooks
cp .claude/backups/hooks-memory-v1/memory-context-hook.py \
   .claude/logic/hooks/memory/memory-context-hook.py

# Remove v2 hooks
rm -f .claude/logic/hooks/memory/*-v2.py
rm -f .claude/logic/hooks/tasks/task_memory_integration.py

# Clear hook cache
rm -rf .claude/cache/hooks/
```

### Level 3: Full System Rollback (5 minutes)
For critical failures

```bash
# Run complete rollback
./rollback_memory_v2.sh

# Verify rollback
python verify_rollback.py

# Check metrics
python compare_metrics.py baseline-metrics.json current-metrics.json
```

### Level 4: Emergency Recovery (10 minutes)
If automated rollback fails

```bash
# 1. Stop all Claude processes
pkill -f claude-code

# 2. Restore from full backup
tar -xzf .claude/backups/memory-system-[timestamp].tar.gz -C .claude/

# 3. Reset state files
rm -rf .claude/state/memory_*
rm -rf .claude/cache/

# 4. Restart with clean state
claude-code --reset-state
```

## Feature Flags

Gradual rollback using feature flags:

```json
{
  "memory_v2_features": {
    "direct_execution": false,      # Disable direct MCP calls
    "conversation_buffer": true,    # Keep buffer analysis
    "task_integration": true,       # Keep task hooks
    "batch_processing": false,      # Disable batching
    "auto_queue_retry": false      # Disable auto-retry
  }
}
```

## Data Recovery

### Recover Queued Memories
```python
# If memories are stuck in queue
def recover_queued_memories():
    queue_file = ".claude/state/memory_queue.json"
    if os.path.exists(queue_file):
        with open(queue_file) as f:
            queued = json.load(f)
        
        # Convert to manual capture commands
        for item in queued:
            if item["status"] == "pending":
                print(f"Manual capture needed: {item['data']['name']}")
                print(f"mcp__graphiti-gemini__add_episode")
                print(json.dumps({"data": item['data']}, indent=2))
```

### Export Critical Memories
```bash
# Before rollback, export recent memories
python export_recent_memories.py --days 7 > recent_memories_backup.json
```

## Monitoring During Rollback

```bash
# Watch key metrics
watch -n 5 'python check_memory_health.py'

# Monitor logs
tail -f .claude/logs/memory-system.log

# Check queue status
watch 'ls -la .claude/state/memory_queue.json 2>/dev/null || echo "Queue cleared"'
```

## Post-Rollback Verification

### 1. System Health Checks
```python
def verify_rollback_success():
    checks = {
        "hooks_version": check_hook_version() == "1.0",
        "settings_valid": verify_settings_file(),
        "queue_empty": not os.path.exists(".claude/state/memory_queue.json"),
        "mcp_working": test_mcp_connection(),
        "capture_working": test_memory_capture()
    }
    
    failed = [k for k, v in checks.items() if not v]
    if failed:
        print(f"❌ Rollback incomplete: {failed}")
    else:
        print("✅ Rollback successful")
```

### 2. User Communication
```markdown
## Rollback Notification Template

Memory Automation v2 has been rolled back due to [ISSUE].

**What happened:**
- [Brief description of issue]
- Rollback completed at [TIME]

**Impact:**
- Memory capture returns to semi-automated mode
- No data loss occurred
- Manual memory commands available

**Next steps:**
- Continue using `/memory` command as before
- We'll investigate and fix the issue
- v2 will be re-deployed after testing
```

## Rollback Prevention

To minimize rollback likelihood:

1. **Phased Rollout**
   - 10% users → 25% → 50% → 100%
   - Monitor metrics at each phase

2. **Canary Deployment**
   - Test on single project first
   - Monitor for 24 hours
   - Gradual expansion

3. **Circuit Breakers**
   - Auto-disable if error rate >5%
   - Queue size limits
   - Timeout protection

4. **Graceful Degradation**
   - Fall back to prompt mode
   - Queue memories locally
   - Retry with exponential backoff

## Recovery Timeline

- **T+0**: Issue detected
- **T+30s**: Quick disable applied
- **T+2m**: Hooks rolled back if needed
- **T+5m**: Full rollback complete
- **T+10m**: Verification complete
- **T+15m**: User notification sent
- **T+30m**: Post-mortem started

## Lessons Learned Integration

After any rollback:
1. Document root cause
2. Add test case for issue
3. Update monitoring
4. Improve rollback procedures
5. Share learnings with team