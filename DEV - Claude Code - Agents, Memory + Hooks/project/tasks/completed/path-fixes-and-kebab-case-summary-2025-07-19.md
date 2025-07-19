# Path Fixes and Kebab-Case Enforcement Summary

**Date:** 2025-07-19  
**Status:** ✅ Completed

## Summary

Fixed all hardcoded path references in hooks to use the correct `.claude/logic/hooks/` path and added kebab-case naming convention enforcement for markdown files.

## Path Fixes Completed

### Updated Hook Files:
1. **system-status-update-hook.py**
   - Changed: `.claude/hooks/` → `.claude/logic/hooks/`

2. **claude-md-update-hook.py**
   - Changed: `.claude/hooks/` → `.claude/logic/hooks/`

3. **folder-structure-hook.py** (4 locations)
   - Line 69: Mapping updated
   - Line 179: Path check updated
   - Line 182: Return path updated
   - Line 295: Test path updated

## Kebab-Case Enforcement Added

### Implementation:
1. **Added to folder-structure-hook.py**:
   - `is_kebab_case()` method - validates kebab-case format
   - `to_kebab_case()` method - converts names to kebab-case
   - Pre-tool validation that:
     - Warns about non-kebab-case markdown files
     - Blocks creation of new markdown files in `.claude/` that don't follow convention
     - Excludes `README.md` and `CLAUDE.md` from this rule

2. **Added to constraints.json**:
   ```json
   "naming_conventions": {
     "markdown_files": "kebab-case required (except README.md and CLAUDE.md)",
     "examples": {
       "correct": ["task-summary.md", "memory-automation-guide.md"],
       "incorrect": ["TaskSummary.md", "memory_automation_guide.md"]
     }
   }
   ```

## Behavior:

### For Markdown Files:
- **Outside `.claude/`**: Warning only (non-blocking)
- **Inside `.claude/`**: 
  - Existing files: Warning only
  - New files: Blocked if not kebab-case
- **Exceptions**: `README.md` and `CLAUDE.md` are always allowed

### Kebab-Case Rules:
- Only lowercase letters, numbers, and hyphens
- No spaces, underscores, or capital letters
- No consecutive hyphens
- Must not start or end with hyphen

## Testing

✅ Verified kebab-case validation triggers correctly
✅ All path references updated and working
✅ Constraints documented in knowledge base

## Impact

- Prevents future path reference issues
- Ensures consistent markdown file naming
- Maintains clean, predictable file structure
- Helps with file discovery and organization