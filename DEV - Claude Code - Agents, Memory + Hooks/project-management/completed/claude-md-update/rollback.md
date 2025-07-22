# Rollback Plan: CLAUDE.md Update System

## Overview
Comprehensive rollback strategy for safely reverting CLAUDE.md updates and disabling the self-update mechanism if needed.

## Backup Strategy

### Automatic Backups
```
.claude/backups/
├── CLAUDE.md.backup.[timestamp]     # Before each update
├── CLAUDE.md.daily.[date]          # Daily snapshots
├── CLAUDE.md.weekly.[week]         # Weekly archives
└── CLAUDE.md.stable.[version]      # Known good versions
```

### Backup Creation
1. **Pre-update**: Automatic copy before any modification
2. **Scheduled**: Daily at 3 AM local time
3. **Manual**: Via `/logic backup claude-md`
4. **Version tags**: After successful major updates

### Backup Retention
- Hourly: Keep last 24 hours
- Daily: Keep last 30 days
- Weekly: Keep last 12 weeks
- Stable: Keep indefinitely

## Rollback Procedures

### Quick Rollback (Last Known Good)
```bash
# 1. Stop any running updates
/logic emergency disable

# 2. Restore last backup
cp .claude/backups/CLAUDE.md.backup.latest CLAUDE.md

# 3. Verify integrity
/logic verify claude-md

# 4. Re-enable system
/logic emergency enable
```

### Targeted Rollback (Specific Version)
```bash
# 1. List available backups
ls -la .claude/backups/CLAUDE.md.*

# 2. Choose specific version
cp .claude/backups/CLAUDE.md.backup.[timestamp] CLAUDE.md

# 3. Lock version (prevent auto-updates)
touch .claude/locks/CLAUDE.md.lock

# 4. Test functionality
/logic test all
```

### Section-Specific Rollback
```bash
# For reverting only specific sections
# 1. Create diff between versions
diff CLAUDE.md .claude/backups/CLAUDE.md.backup.latest > changes.diff

# 2. Selectively apply reversions
patch -R -p0 < changes.diff

# 3. Manual review and adjustment
# Edit CLAUDE.md to keep wanted changes
```

## Disabling Self-Update

### Temporary Disable
```bash
# Method 1: Emergency disable
/logic emergency disable updates

# Method 2: Lock file
touch .claude/locks/updates.lock

# Method 3: Environment variable
export CLAUDE_MD_AUTO_UPDATE=false
```

### Permanent Disable
```javascript
// In .claude/hooks/claude-md-update.js
const config = {
  enabled: false,  // Change from true to false
  autoUpdate: false,
  manualOnly: true
};
```

### Selective Disable
```json
// In .claude/config/updates.json
{
  "claude-md": {
    "sections": {
      "quick-start": true,
      "principles": false,  // Disable specific section updates
      "task-management": true,
      "memory-ops": false,
      "warnings": true
    }
  }
}
```

## Recovery Procedures

### Corrupted File Recovery
```bash
# 1. Check file integrity
file CLAUDE.md
head -n 50 CLAUDE.md

# 2. If corrupted, use stable version
cp .claude/backups/CLAUDE.md.stable.latest CLAUDE.md

# 3. If all backups corrupted, use Git
git checkout HEAD -- CLAUDE.md

# 4. Last resort: Template recovery
cp .claude/templates/CLAUDE.md.template CLAUDE.md
```

### Hook Failure Recovery
```bash
# 1. Disable problematic hook
mv .claude/hooks/claude-md-update.js .claude/hooks/claude-md-update.js.disabled

# 2. Clear hook cache
rm -rf .claude/cache/hooks/*

# 3. Test without hook
/logic test basic

# 4. Re-enable with fixes
# Fix issues in hook file
mv .claude/hooks/claude-md-update.js.disabled .claude/hooks/claude-md-update.js
```

### Memory State Recovery
```bash
# If memory operations fail after update
# 1. Export current memories
/memory export .claude/backups/memory-backup.json

# 2. Rollback CLAUDE.md
cp .claude/backups/CLAUDE.md.backup.latest CLAUDE.md

# 3. Test memory operations
/memory search "test"

# 4. Re-import if needed
/memory import .claude/backups/memory-backup.json
```

## Rollback Decision Matrix

| Scenario | Severity | Rollback Type | Time Required |
|----------|----------|---------------|---------------|
| Minor formatting issue | Low | None needed | 0 min |
| Command not working | Medium | Section-specific | 5 min |
| Multiple commands broken | High | Full rollback | 2 min |
| System crash on load | Critical | Emergency restore | 30 sec |
| Data corruption | Critical | Git recovery | 10 min |

## Automated Rollback Triggers

### Automatic Rollback Conditions
1. **Syntax errors**: Markdown parsing fails
2. **Command failures**: Core commands return errors
3. **Hook conflicts**: Update breaks existing hooks
4. **Performance degradation**: Load time > 5 seconds
5. **Memory errors**: Can't access Graphiti

### Rollback Script
```bash
#!/bin/bash
# .claude/scripts/auto-rollback.sh

# Function to test CLAUDE.md health
test_claude_md() {
    # Test 1: File exists and readable
    if [ ! -r "CLAUDE.md" ]; then
        return 1
    fi
    
    # Test 2: Basic commands work
    if ! /memory search "test" &>/dev/null; then
        return 1
    fi
    
    # Test 3: No syntax errors
    if ! markdown-lint CLAUDE.md &>/dev/null; then
        return 1
    fi
    
    return 0
}

# Main rollback logic
if ! test_claude_md; then
    echo "CLAUDE.md health check failed. Initiating rollback..."
    cp .claude/backups/CLAUDE.md.backup.latest CLAUDE.md
    
    if test_claude_md; then
        echo "Rollback successful!"
        # Log the incident
        echo "[$(date)] Automatic rollback performed" >> .claude/logs/rollback.log
    else
        echo "Rollback failed! Manual intervention required."
        # Send alert
        /logic alert "CLAUDE.md rollback failed"
    fi
fi
```

## Manual Intervention Points

### When to Intervene
1. Automated rollback fails
2. Multiple rollback attempts needed
3. Git history corruption
4. Backup files missing
5. System-wide hook failures

### Intervention Steps
1. **Stop all automation**: `/logic emergency disable all`
2. **Access manual mode**: `export CLAUDE_MANUAL_MODE=true`
3. **Use Git history**: `git log --oneline CLAUDE.md`
4. **Cherry-pick changes**: Manually apply wanted updates
5. **Test thoroughly**: Run full test suite
6. **Document issues**: Create incident report

## Rollback Verification

### Post-Rollback Checks
```bash
# 1. Verify file integrity
md5sum CLAUDE.md
wc -l CLAUDE.md

# 2. Test all commands
/logic test commands

# 3. Verify hook compatibility
/logic hooks test

# 4. Check memory operations
/memory search "rollback test"

# 5. Performance benchmark
time /logic help
```

### Success Criteria
- [ ] All commands functional
- [ ] No error messages
- [ ] Performance normal
- [ ] Hooks executing properly
- [ ] Memory operations working
- [ ] No data loss

## Communication Plan

### Rollback Notifications
1. **Automatic alert**: System detects and notifies
2. **Status update**: Current state and actions taken
3. **Resolution notice**: When system is stable
4. **Post-mortem**: What went wrong and fixes applied

### Stakeholder Updates
```markdown
Subject: CLAUDE.md Update Rollback - [STATUS]

An issue was detected with the recent CLAUDE.md update.
Status: [Rolled back | In progress | Resolved]
Impact: [None | Minor | Major]
Action required: [None | Please restart | Manual fix needed]

Details: [Brief description]
Timeline: [When it happened and expected resolution]
```

## Preventive Measures

### Pre-Update Validation
1. Test updates in sandbox first
2. Validate markdown syntax
3. Check command compatibility
4. Review hook interactions
5. Benchmark performance

### Gradual Rollout
1. Update test environment first
2. Monitor for 24 hours
3. Update development environment
4. Monitor for 48 hours
5. Update production

### Version Control Integration
```bash
# Before any update
git add CLAUDE.md
git commit -m "Pre-update checkpoint"
git tag -a "claude-md-stable-$(date +%Y%m%d)" -m "Stable version before update"

# After successful update
git add CLAUDE.md
git commit -m "Update CLAUDE.md - [description]"
git tag -a "claude-md-v[version]" -m "Updated version"
```

## Emergency Contacts

### Escalation Path
1. **Level 1**: Automated systems handle
2. **Level 2**: Senior developer review
3. **Level 3**: System architect intervention
4. **Level 4**: External support

### Quick Reference
- Rollback command: `/logic rollback claude-md`
- Emergency disable: `/logic emergency disable`
- Manual restore: `cp .claude/backups/CLAUDE.md.backup.latest CLAUDE.md`
- Git restore: `git checkout HEAD -- CLAUDE.md`