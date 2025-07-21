# Vite Exclusion Configuration

**Created:** 2025-07-19
**Priority:** Medium
**Type:** Configuration
**Estimated Effort:** 1 day

## Problem Statement

The system should ignore everything related to Vite as we use Slater. Vite is for future setup as an alternative to Slater at a later stage. Currently, Vite-related files may be included in searches, analysis, and operations.

## Current State

### Vite Files Present
- Vite configuration files in project root
- Vite-related dependencies in package.json
- Possible Vite build artifacts

### Current Tool: Slater
- Active deployment platform
- All production builds use Slater
- Vite is NOT in use currently

## Solution Design

### 1. Update .gitignore

```gitignore
# Vite - Future use only, not active
vite.config.js
vite.config.ts
*.vite.*
.vite/
dist-vite/
vite-*.json
```

### 2. Create Exclusion Patterns

**For all search and analysis tools:**
```python
EXCLUDED_PATTERNS = [
    "**/vite*",
    "**/*.vite.*",
    "**/dist-vite/**",
    "vite.config.*"
]
```

### 3. Update Knowledge Files

**facts.json:**
```json
{
  "stack": {
    "platform": "Webflow",
    "deployment": "Slater (active)",
    "future_tools": {
      "vite": "Reserved for future migration from Slater"
    },
    "excluded_from_analysis": ["vite"]
  }
}
```

**constraints.json:**
```json
{
  "tooling": {
    "active_build_tool": "Slater",
    "excluded_tools": ["Vite"],
    "note": "Vite files present but not in use - ignore in all operations"
  }
}
```

### 4. Hook Configuration

**Create exclusion hook:**
```python
# .claude/hooks/tools/vite-exclusion-hook.py
class ViteExclusionHook(HookBase):
    def __init__(self):
        super().__init__("ViteExclusion")
        self.vite_patterns = [
            "vite", "vitest", ".vite", "dist-vite"
        ]
    
    def pre_tool_use(self, tool_name, tool_args):
        if tool_name in ["Glob", "Grep", "Read", "Edit"]:
            # Add exclusion warning
            if self.contains_vite_reference(tool_args):
                return {
                    "warning": "Vite-related file detected. Vite is not active - use Slater instead.",
                    "continue": False
                }
        return {"continue": True}
```

### 5. Search Tool Configuration

**Update search defaults:**
```python
# Add to all search operations
DEFAULT_EXCLUDES = [
    "node_modules",
    ".git",
    "dist",
    "build",
    # Add Vite exclusions
    "vite*",
    ".vite",
    "dist-vite"
]
```

## Implementation Steps

### Phase 1: Documentation (30 min)
1. [ ] Update facts.json with Vite exclusion note
2. [ ] Update constraints.json with tooling constraints
3. [ ] Add comments to any existing Vite files

### Phase 2: Git Configuration (30 min)
1. [ ] Update .gitignore with Vite patterns
2. [ ] Create .claude-ignore file if needed
3. [ ] Document exclusion in README

### Phase 3: Hook Implementation (2 hours)
1. [ ] Create vite-exclusion-hook.py
2. [ ] Add to hook configuration
3. [ ] Test with common operations

### Phase 4: Tool Updates (2 hours)
1. [ ] Update search tool defaults
2. [ ] Add exclusion patterns to file operations
3. [ ] Create helper functions for filtering

## Configuration Examples

### 1. .claude-ignore
```
# Vite - Future use only
vite.config.js
vite.config.ts
vite.*.json
**/.vite/
**/dist-vite/
```

### 2. Search Operations
```python
# Before
files = glob("**/*.js")

# After
files = glob("**/*.js", exclude=["**/vite*"])
```

### 3. File Operations Check
```python
def should_process_file(filepath):
    vite_indicators = ["vite", ".vite", "vitest"]
    return not any(indicator in filepath.lower() for indicator in vite_indicators)
```

## Testing Plan

1. **Verify Exclusions:**
   - Run Glob for JS files - should not include Vite
   - Search for "config" - should not show vite.config
   - List project files - Vite files marked as excluded

2. **Tool Testing:**
   - Test each tool with Vite-related queries
   - Verify warnings/blocks are shown
   - Ensure Slater operations unaffected

3. **Documentation:**
   - Clear notes about Vite being future-only
   - Slater identified as active tool
   - Migration path documented for future

## Success Metrics

1. Zero Vite files in normal operations
2. Clear warnings when Vite accessed
3. No confusion about active build tool
4. Future migration path preserved

## Notes

- Vite files should remain in repository for future use
- Only exclude from active development operations
- Document why Vite present but not used
- Preserve Vite config for future migration

## Future Considerations

When migrating from Slater to Vite:
1. Remove exclusion configurations
2. Update facts.json and constraints.json
3. Disable exclusion hooks
4. Update deployment documentation

## References

- Slater documentation: [Platform docs]
- Current build configuration: package.json scripts
- Deployment guide: `.claude/docs/deployment/`