# Run Hook Rollback Plan

## Scenario: Removal Causes Issues

If removing `run-hook.py` causes unexpected problems, follow this rollback procedure.

## Immediate Rollback Steps

### 1. Restore from Backup
```bash
# If backup was created
cp /tmp/run-hook.py.backup .claude/logic/hooks/code_reuse/run-hook.py

# If no backup exists, recreate the file
cat > .claude/logic/hooks/code_reuse/run-hook.py << 'EOF'
#!/usr/bin/env python3
"""Simple hook runner for testing"""

import sys
import json
import subprocess

def main():
    # Get the actual hook script
    hook_script = sys.argv[0].replace('run-hook.py', 'code-reuse-validation-hook.py')
    
    # Forward all arguments
    result = subprocess.run(
        [sys.executable, hook_script] + sys.argv[1:],
        capture_output=True,
        text=True
    )
    
    # Output the result
    print(result.stdout)
    
    # Exit with hook's exit code
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
EOF

chmod +x .claude/logic/hooks/code_reuse/run-hook.py
```

### 2. Verify Restoration
```bash
ls -la .claude/logic/hooks/code_reuse/run-hook.py
python3 .claude/logic/hooks/code_reuse/run-hook.py --test
```

### 3. Document the Issue
Create an issue report:
```bash
cat > .claude/project-management/issues/run-hook-removal-failed.md << 'EOF'
# Run Hook Removal Issue

## Date: [Current Date]

## Issue Description
Removing run-hook.py caused: [describe issue]

## Root Cause
[Explain why the file was actually needed]

## Resolution
File was restored. Need to:
1. Document its purpose
2. Add to automation if needed
3. Refactor to be more useful

## Lessons Learned
[What we learned from this]
EOF
```

## Investigation Steps

If rollback is needed, investigate:

1. **Check Error Logs**
   ```bash
   grep -r "run-hook" /tmp/*.log
   tail -100 .claude/logs/*.log | grep -i error
   ```

2. **Identify Dependencies**
   ```bash
   # More thorough search
   find .claude -type f -name "*.py" -exec grep -l "run-hook" {} \;
   find .claude -type f -name "*.json" -exec grep -l "run-hook" {} \;
   ```

3. **Test Hook System**
   ```bash
   /logic hooks test
   python3 .claude/logic/hooks/code_reuse/code-reuse-validation-hook.py
   ```

## Prevention

To prevent future issues:

1. **Add Deprecation Notice**
   ```python
   # At top of run-hook.py
   """
   DEPRECATED: This file is scheduled for removal.
   Use code-reuse-validation-hook.py directly.
   If you're using this file, please update your workflow.
   """
   ```

2. **Monitor Usage**
   Add logging to track if it's being used

3. **Gradual Removal**
   - Week 1: Add deprecation warning
   - Week 2: Log usage statistics  
   - Week 3: Remove if no usage

## Long-term Solution

If the file is actually needed:
1. Rename to `test-hook-runner.py` for clarity
2. Extend to support all hooks, not just code-reuse
3. Add proper documentation
4. Include in automation settings if frequently used

## Contact
If issues persist, check:
- Memory system for related patterns
- Git history for original purpose
- Documentation for hidden dependencies