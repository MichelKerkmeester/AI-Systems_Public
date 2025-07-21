# Test Cleanup Hook

Automated test file cleanup system that removes test scripts and results after test execution.

## How It Works

1. **Monitors Bash commands** for test execution patterns:
   - `pytest`, `python test`, `npm test`, `yarn test`
   - Test completion messages: "test passed", "test complete", etc.

2. **Identifies test files** to clean up:
   - `test_*.py`, `*_test.py`
   - `test-*.py`, `*-test.py`
   - `test*.json`, `*test-results*.json`
   - Test output files

3. **Protection mechanisms**:
   - Never deletes from protected directories (node_modules, .git, z__archive)
   - Skips active spec test folders with requirements.md
   - Waits 5 minutes before cleaning regular test files
   - Cleans test result JSON files immediately

## Activation

The hook is already integrated in `.claude/settings.json` under PostToolUse for Bash commands.

## Manual Cleanup

To manually trigger cleanup of old test files:

```bash
find . -name "test*.py" -o -name "*test*.json" | grep -v node_modules | grep -v .git | xargs rm -f
```

## Configuration

Edit the hook file to adjust:
- Test execution patterns
- File cleanup patterns
- Protected directories
- Age threshold for cleanup

## Testing

Create a test file and run it:
```bash
echo "print('test complete')" > test_example.py
python test_example.py
# File will be cleaned up after 5 minutes
```