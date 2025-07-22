# Run Hook Removal Test Plan

## Pre-Removal Verification

### 1. Check for Dependencies
```bash
# Search for any references to run-hook.py
grep -r "run-hook.py" .claude/
grep -r "run-hook" .claude/docs/
grep -r "run-hook" .claude/project-management/
```

Expected: No references found

### 2. Test Direct Hook Execution
```bash
# Test that code-reuse-validation-hook.py works independently
cd .claude/logic/hooks/code_reuse/
python3 code-reuse-validation-hook.py --test
```

Expected: Hook runs successfully without wrapper

### 3. Verify Automation Status
```bash
# Confirm hook is already automated
grep "code-reuse-validation-hook.py" .claude/settings.json
```

Expected: Found in settings.json PostToolUse section

## Removal Process

### 1. Backup (Just in Case)
```bash
cp .claude/logic/hooks/code_reuse/run-hook.py /tmp/run-hook.py.backup
```

### 2. Remove File
```bash
rm .claude/logic/hooks/code_reuse/run-hook.py
```

### 3. Verify Removal
```bash
ls .claude/logic/hooks/code_reuse/
```

Expected: run-hook.py not listed

## Post-Removal Validation

### 1. Test Hook Automation
Create a test file to trigger code reuse validation:
```bash
echo "test_component = Button()" > /tmp/test_reuse.py
```

Expected: Hook triggers and validates code reuse

### 2. Check System Status
```bash
/logic hooks status
```

Expected: All hooks show as active, no errors

### 3. Memory Capture
Ensure this change is captured in memory system

## Rollback Plan

If issues discovered:
```bash
cp /tmp/run-hook.py.backup .claude/logic/hooks/code_reuse/run-hook.py
```

## Success Criteria
- [ ] No dependencies on run-hook.py found
- [ ] code-reuse-validation-hook.py works independently  
- [ ] File successfully removed
- [ ] No system errors after removal
- [ ] Change documented in memory system