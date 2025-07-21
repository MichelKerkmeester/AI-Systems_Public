# Project Structure Standard

## Required Folder Structure

All projects in `/specs/`, `/active/`, or `/completed/` must follow this structure:

```
project-name/
├── tests/
│   ├── results/          # All test output files (*.json, *.txt, etc.)
│   └── test_*.py         # Test scripts
├── design.md             # Design document
├── test-plan.md          # Test plan
├── requirements.md       # Requirements specification
└── README.md             # Project overview (optional)
```

## Key Rules

1. **Test Results**: Always save to `tests/results/` subdirectory
2. **Test Scripts**: Place in `tests/` directory
3. **No Top-Level Test Files**: Don't save test results in project root
4. **Consistent Naming**: Use descriptive prefixes + timestamps for results

## Test Result Format

Test results should be saved as **markdown files** for better readability:

```
{prefix}-summary.md
```

Examples:
- `code-reuse-test-results-summary.md`
- `integration-test-summary.md`
- `performance-test-summary.md`

### Markdown Format Structure
```markdown
# Test Results Title

**Date:** YYYY-MM-DD
**Time:** HH:MM:SS
**Test Type:** [Type of test]

## Summary

| Metric | Value |
|--------|-------|
| Total Tests | X |
| Passed | Y |
| Failed | Z |
| Success Rate | XX.X% |

## ✅ Passed Tests
1. **Test Name**
   - Details about the test

## ❌ Failed Tests  
1. **Test Name**
   - Issue: Description of failure

---
*Generated on YYYY-MM-DD at HH:MM:SS*
```

## Helper Function Available

Use `test_helpers.py` for consistent test result management:

```python
from ..shared.test_helpers import save_test_results

# Automatically saves as markdown to correct location
save_test_results(results, filename_prefix="my-test", test_type="unit")

# Or explicitly specify format
save_test_results(results, filename_prefix="my-test", format="markdown")
```

This ensures all projects maintain consistent structure regardless of their location in the project management hierarchy.