# Documentation Automation Requirements

## Overview
Automate `doc-audit.py` and `doc-updater.py` to maintain documentation quality without manual intervention.

## Current State

### doc-audit.py
- **Purpose**: Audits documentation health, checks for broken links, stale content
- **Features**:
  - Counts documentation files by type
  - Checks for outdated content (>30 days)
  - Validates internal links
  - Identifies missing documentation
  - Generates health report
- **Manual execution only**

### doc-updater.py  
- **Purpose**: Updates README files, TOCs, and cross-references
- **Features**:
  - Generates directory structures
  - Updates TOCs automatically
  - Fixes broken internal links
  - Updates README files with structure
  - Maintains cross-references
- **Manual execution only**

## Automation Requirements

### 1. Trigger Conditions
Documentation updates should trigger when:
- New files added to `.claude/docs/`
- Documentation files edited
- Hook or command files added/removed (affects references)
- Weekly scheduled audit (stale content check)
- Project structure changes significantly

### 2. Integration Points

#### A. PostToolUse Hook
Trigger after Write/Edit/MultiEdit operations on:
- `*.md` files in `.claude/docs/`
- Hook files (update hook documentation)
- Command files (update command references)
- Knowledge files (update facts/patterns docs)

#### B. Scheduled Execution
- Daily: Quick link validation
- Weekly: Full audit with staleness check
- Monthly: Comprehensive documentation review

#### C. Pre-commit Hook
- Validate documentation before commits
- Ensure TOCs are up-to-date
- Check for broken links

### 3. Smart Updates

#### Incremental Processing
- Only update affected sections
- Cache previous scan results
- Minimize file rewrites

#### Conflict Prevention
- Check if file is being edited
- Use atomic updates
- Preserve manual edits

#### Performance Optimization
- Batch updates together
- Async processing for large scans
- Progress reporting for long operations

### 4. Safety Requirements

#### Preserve Manual Content
- Never overwrite custom sections
- Respect "DO NOT AUTO-UPDATE" markers
- Maintain hand-crafted examples

#### Validation Before Updates
- Dry-run mode for testing
- Diff preview before applying
- Rollback capability

#### Error Handling
- Graceful failure on parse errors
- Clear error messages
- Recovery suggestions

## Proposed Architecture

### 1. Unified Documentation Hook
Combine audit and update functionality:
```
.claude/logic/hooks/core/doc-maintenance-hook.py
```

### 2. Configuration
```json
{
  "doc_maintenance": {
    "enabled": true,
    "auto_update_toc": true,
    "fix_broken_links": true,
    "update_readmes": true,
    "audit_interval_days": 7,
    "preserve_sections": ["Examples", "Notes", "Custom"],
    "excluded_paths": [".claude/z__archive/"]
  }
}
```

### 3. Trigger Integration
```json
{
  "PostToolUse": [{
    "matcher": "Write|Edit|MultiEdit",
    "hooks": [{
      "type": "command",
      "command": "python3 '.claude/logic/hooks/core/doc-maintenance-hook.py'"
    }]
  }]
}
```

## Success Criteria

1. **Automated Maintenance**
   - TOCs update automatically
   - Broken links fixed without intervention
   - Structure updates reflected immediately

2. **Quality Improvement**
   - No stale documentation (>30 days)
   - All internal links valid
   - Consistent formatting

3. **Developer Experience**
   - Zero manual documentation tasks
   - Clear audit reports
   - Fast incremental updates

4. **Safety**
   - No loss of manual content
   - Predictable behavior
   - Easy to disable if needed

## Implementation Priority

1. **Phase 1**: Basic automation (High Priority)
   - TOC updates on file changes
   - README structure updates
   - Simple broken link fixes

2. **Phase 2**: Smart updates (Medium Priority)
   - Incremental processing
   - Caching system
   - Conflict detection

3. **Phase 3**: Advanced features (Low Priority)
   - Scheduled audits
   - Staleness detection
   - Cross-reference validation

## Decision Point
Should we proceed with full automation or start with semi-automated approach where the hook notifies about needed updates but requires confirmation?

**Recommendation**: Start with full automation for low-risk updates (TOCs, structure) and notification-only for high-risk updates (content changes, link fixes).