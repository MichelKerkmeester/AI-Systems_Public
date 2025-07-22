# Unified Slater Compliance & Code Quality Specification

## Overview
This specification combines three critical areas for maintaining code quality and preventing platform conflicts:
1. **Comment Style Enforcement** - Consistent documentation across the codebase
2. **Vite Exclusion** - Clear separation between active (Slater) and future (Vite) tools
3. **DOMContentLoaded Prevention** - Enhanced enforcement through CLAUDE.md and knowledge integration

## Background & Current State

### Existing Issues
1. **Comment Styles**: No enforcement mechanism for consistent comment formatting
2. **Vite Confusion**: Vite files present but not used, causing potential confusion
3. **DOMContentLoaded**: While source code is clean, the system lacks preventive measures
4. **Knowledge Integration**: `/knowledge` files exist but are sometimes ignored by AI

### Recent System Changes
- CLAUDE.md updated with 5-step enforcement process
- Memory automation v2 implemented (50+ captures/day)
- Code reuse enforcement active
- Config auto-sync attempted (hooks created but not automated)

## Requirements

### 1. Comment Style Enforcement
- Force consistent inline comment styles across JS, CSS, and other files
- Use existing patterns found in codebase:
  ```javascript
  // ─────────────────────────────────────────────────────────────
  // Component Name
  // ─────────────────────────────────────────────────────────────
  
  /* ─── Section Divider ────────────────────────────────────── */
  ```

### 2. Vite Exclusion
- Completely ignore Vite files in searches and operations
- Preserve for future migration
- Clear documentation that Slater is the active tool

### 3. DOMContentLoaded Prevention
- Prevent future occurrences of DOMContentLoaded in new code
- Enhance CLAUDE.md enforcement
- Integrate with knowledge system for better compliance

### 4. Knowledge Integration Enhancement
- Ensure AI references knowledge files before making decisions
- Add explicit checks in CLAUDE.md steps
- Create validation patterns

## Implementation Plan

### Phase 1: CLAUDE.md Enhancement (Day 1)

#### Update START HERE Steps
```markdown
## 📋 STEP 1: READ REQUIREMENTS
Claude, read the rules in CLAUDE.md, then use sequential thinking and proceed to the next step.

### MANDATORY CHECKS:
1. ✅ Read /knowledge files: facts.json, patterns.json, constraints.json
2. ✅ Check for Slater constraints (NO DOMContentLoaded)
3. ✅ Search memories for relevant patterns
4. ✅ Verify code reuse opportunities

### STOP. Before reading further, confirm you understand:
1. This is a code reuse and consolidation project
2. Creating new files requires exhaustive justification  
3. Every suggestion must reference existing code
4. Slater autoloads - NO DOMContentLoaded needed
5. Violations of these rules make your response invalid
```

#### Add Slater-Specific Section
```markdown
## 🚨 SLATER PLATFORM RULES

### NEVER Use:
- ❌ `DOMContentLoaded` - Slater autoloads everything
- ❌ `document.addEventListener('DOMContentLoaded')` 
- ❌ `$(document).ready()` - No jQuery ready patterns
- ❌ Vite references - Use Slater only

### ALWAYS Use:
- ✅ Direct initialization: `const init = () => { /* code */ }; init();`
- ✅ Webflow.push() for dependencies
- ✅ Module pattern with immediate execution
- ✅ Check existing components for patterns

### Enforcement:
- Hook blocks DOMContentLoaded patterns
- Memory captures violations for learning
- Tests verify Slater compliance
```

### Phase 2: Knowledge Files Update (Day 1)

#### Update constraints.json
```json
{
  "slater_constraints": {
    "no_domcontentloaded": {
      "rule": "NEVER use DOMContentLoaded - Slater autoloads",
      "severity": "critical",
      "patterns": [
        "DOMContentLoaded",
        "document.addEventListener(['\"]DOMContentLoaded",
        "$(document).ready",
        "jQuery(document).ready"
      ],
      "correct_pattern": "Direct initialization or Webflow.push()",
      "example": "const init = () => { /* code */ }; init();"
    },
    "no_vite": {
      "rule": "Vite is for future use only",
      "severity": "high",
      "active_tool": "Slater"
    }
  }
}
```

#### Update patterns.json
```json
{
  "comment_styles": {
    "javascript": {
      "file_header": "// ─────────────────────────────────────────────────────────────",
      "section": "/* ─── {name} ─────────────────────────────────────────────── */",
      "inline": "// {comment}"
    },
    "css": {
      "file_header": "/* ─────────────────────────────────────────────────────────── */",
      "section": "/*------ {name} ------*/",
      "inline": "/* {comment} */"
    }
  },
  "initialization_patterns": {
    "slater_compatible": [
      "const init = () => { /* code */ }; init();",
      "Webflow.push(() => { /* code */ });",
      "(function() { /* code */ })();"
    ]
  }
}
```

### Phase 3: Validation Scripts (Day 1)

#### Create validation utilities
1. **Comment Style Validator** (`validate-comments.py`)
   - Scan files for non-compliant comments
   - Auto-format using patterns.json
   - Report violations

2. **Slater Compliance Checker** (`check-slater-compliance.py`)
   - Scan for DOMContentLoaded patterns
   - Validate initialization patterns
   - Block commits with violations

3. **Vite Exclusion List** (`.claude-ignore`)
   ```
   # Vite files (reserved for future)
   **/vite*
   **/*.vite.*
   **/dist-vite/**
   vite.config.js
   ```

### Phase 4: Hook Integration (Day 2)

Since auto-hooks don't work with current system:

1. **Add to CLAUDE.md Pre-Edit Checklist**:
   ```markdown
   ### Before ANY File Edit:
   1. Run: `python3 .claude/validation/check-slater-compliance.py [file]`
   2. Run: `python3 .claude/validation/validate-comments.py [file]`
   3. Check: No Vite imports or references
   4. Verify: Pattern compliance with patterns.json
   ```

2. **Create Manual Validation Command**:
   ```bash
   /logic validate [file] - Run all compliance checks
   ```

### Phase 5: Testing & Rollout (Day 2)

1. **Test Cases**:
   - Attempt to add DOMContentLoaded (should fail)
   - Try to import Vite (should warn)
   - Add non-compliant comments (should auto-format)
   - Reference knowledge files (should be enforced)

2. **Success Metrics**:
   - Zero new DOMContentLoaded patterns
   - 100% comment compliance in new code
   - No Vite confusion
   - Knowledge files referenced in every implementation

## Automation Strategy

### Since hooks don't auto-execute:

1. **Enforce through CLAUDE.md**:
   - Mandatory steps that reference validation
   - Clear failure conditions
   - Memory captures for violations

2. **Manual Commands**:
   - `/logic validate` - Run all checks
   - `/logic format-comments` - Fix comment styles
   - `/memory search slater` - Find Slater patterns

3. **Git Pre-commit** (Optional):
   ```bash
   #!/bin/bash
   python3 .claude/validation/check-slater-compliance.py
   python3 .claude/validation/validate-comments.py
   ```

## Risk Mitigation

1. **Gradual Rollout**:
   - Start with new files only
   - Gradually update existing files
   - Monitor for false positives

2. **Clear Documentation**:
   - Update README with Slater requirements
   - Add examples to each component
   - Create migration guide from DOMContentLoaded

3. **Escape Hatches**:
   - Allow overrides with justification
   - Document exceptions in facts.json
   - Provide rollback procedures

## Implementation Checklist

- [ ] Update CLAUDE.md with Slater rules and knowledge checks
- [ ] Enhance knowledge files (constraints.json, patterns.json)
- [ ] Create validation scripts
- [ ] Add .claude-ignore for Vite exclusion
- [ ] Update existing component examples
- [ ] Test all validation scenarios
- [ ] Document in README
- [ ] Create manual validation commands
- [ ] Set up memory captures for violations
- [ ] Train system through pattern examples

## Expected Outcomes

1. **Zero DOMContentLoaded** in all new code
2. **Consistent comments** across entire codebase
3. **Clear tool separation** (Slater active, Vite future)
4. **Knowledge integration** in every implementation
5. **Automated compliance** through CLAUDE.md enforcement

## Timeline

- **Day 1**: CLAUDE.md updates, knowledge files, validation scripts
- **Day 2**: Testing, documentation, rollout
- **Ongoing**: Monitor compliance, refine patterns, capture violations