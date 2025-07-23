# Documentation Automation Rollback Plan

## Emergency Shutdown

### Immediate Disable
If documentation automation causes issues:

```bash
# Method 1: Disable in settings
sed -i '' 's/"doc_maintenance":.*{.*"enabled":.*true/"doc_maintenance": {"enabled": false/' .claude/settings.json

# Method 2: Remove from hooks
grep -v "doc-maintenance-hook.py" .claude/settings.json > .claude/settings.json.tmp
mv .claude/settings.json.tmp .claude/settings.json

# Method 3: Emergency flag file
touch .claude/.disable-doc-automation
```

## Common Issues and Fixes

### Issue 1: Infinite Loop
**Symptom**: Hook triggers on its own changes
**Fix**:
```python
# Add to hook
if "auto-generated" in file_content:
    return  # Skip files we generated
```

### Issue 2: Content Loss
**Symptom**: Custom content overwritten
**Fix**:
1. Restore from git
2. Add preserve markers
3. Update safety checks

### Issue 3: Performance Degradation
**Symptom**: Editing slows down significantly
**Fix**:
1. Disable real-time updates
2. Switch to batch mode
3. Increase cache time

### Issue 4: Broken Documentation
**Symptom**: TOCs point to wrong sections
**Fix**:
```bash
# Revert all TOCs
git checkout -- '.claude/docs/**/*.md'

# Run manual fix
python3 .claude/logic/documentation/scripts/doc-updater.py --fix-tocs
```

## Rollback Procedures

### Level 1: Disable Automation
Keep hook installed but disabled:
```json
{
  "doc_maintenance": {
    "enabled": false
  }
}
```

### Level 2: Remove Hook
Complete removal from system:
```bash
# Remove from settings.json
# Remove hook file
rm .claude/logic/hooks/core/doc-maintenance-hook.py

# Clear cache
rm -rf .claude/state/doc_cache.json
```

### Level 3: Restore Original Scripts
Revert to manual scripts:
```bash
# Ensure original scripts still work
python3 .claude/logic/documentation/scripts/doc-audit.py
python3 .claude/logic/documentation/scripts/doc-updater.py
```

## Data Recovery

### Git Recovery
```bash
# View history of doc changes
git log -p -- '.claude/docs/'

# Restore specific file to previous version
git checkout <commit-hash> -- .claude/docs/specific-file.md

# Bulk restore to specific date
git checkout `git rev-list -n 1 --before="2024-01-01" HEAD` -- '.claude/docs/'
```

### Backup Recovery
If backups were created:
```bash
# Restore from backup
cp -r .claude/docs.backup/* .claude/docs/

# Or from time-stamped backup
tar -xzf .claude/backups/docs-2024-01-15.tar.gz
```

### Manual Recreation
If all else fails:
1. List all affected files
2. Use file history to identify changes
3. Manually recreate important sections
4. Re-run doc-audit to identify gaps

## Prevention Measures

### 1. Gradual Rollout
```python
# Start with notify-only mode
"auto_updates": {
  "toc": false,  # Just notify
  "structure": false,  # Just notify
  "timestamps": true  # Safe to automate
}
```

### 2. Backup Before Major Updates
```python
def create_backup(self):
    """Always backup before bulk updates"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = self.base_path / f".claude/backups/docs_{timestamp}"
    shutil.copytree(self.docs_path, backup_dir)
```

### 3. Validation Requirements
```python
def validate_safety(self):
    """Ensure safety checks are functioning"""
    test_file = self.create_test_file_with_custom_section()
    result = self.try_update(test_file)
    assert "custom section preserved" in result
```

## Communication Plan

### If Issues Occur
1. **Immediate**: Add warning to CLAUDE.md
   ```markdown
   ⚠️ AUTOMATED DOC UPDATES DISABLED DUE TO ISSUES
   Manual updates required until resolved
   ```

2. **Team Notification**: 
   ```bash
   echo "Doc automation issues detected. Rollback initiated." > .claude/alerts/doc-automation-issue.txt
   ```

3. **Memory System**: Capture the issue
   ```python
   capture_memory(
       "ISSUE: Documentation automation rollback",
       "Reason: [specific issue]",
       "Time: [timestamp]",
       "Impact: [what was affected]"
   )
   ```

## Recovery Validation

After rollback:
1. **Test Manual Tools**
   ```bash
   python3 .claude/logic/documentation/scripts/doc-audit.py --test
   python3 .claude/logic/documentation/scripts/doc-updater.py --dry-run
   ```

2. **Verify Documentation Intact**
   ```bash
   # Check line counts
   find .claude/docs -name "*.md" -exec wc -l {} \; | sort -n

   # Check for missing sections
   grep -r "BEGIN-CUSTOM-SECTION" .claude/docs/
   ```

3. **Confirm No Active Hooks**
   ```bash
   grep -c "doc-maintenance-hook" .claude/settings.json
   # Should return 0
   ```

## Lessons Learned Template

Create post-mortem:
```markdown
# Documentation Automation Post-Mortem

## Date: [Date]

## What Happened
[Description of issue]

## Root Cause
[Why it happened]

## Impact
- Files affected: X
- Time to recover: Y
- Data lost: None/Some/Details

## Fixes Applied
1. [Fix 1]
2. [Fix 2]

## Prevention
- [ ] Add test for this case
- [ ] Update safety checks
- [ ] Improve validation

## Next Steps
[Plan for re-enabling or abandoning]
```

## Re-enabling Checklist

Before turning back on:
- [ ] Root cause identified and fixed
- [ ] New tests added for failure case
- [ ] Backup system verified
- [ ] Gradual rollout plan created
- [ ] Team notified of changes
- [ ] Memory system updated with fixes