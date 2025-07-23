# Documentation Automation Design

## Architecture Overview

### Unified Hook Approach
Create a single `doc-maintenance-hook.py` that combines audit and update functionality with smart triggering.

```
.claude/logic/hooks/core/doc-maintenance-hook.py
├── Triggers on doc changes
├── Performs incremental updates
├── Runs periodic audits
└── Generates reports
```

## Detailed Design

### 1. Hook Structure

```python
class DocMaintenanceHook(HookBase):
    def __init__(self):
        super().__init__("DocMaintenance")
        self.doc_auditor = DocAuditor()
        self.doc_updater = DocUpdater()
        self.settings = self.load_settings()
        
    def should_trigger(self, tool_name, args):
        """Determine if documentation maintenance needed"""
        if tool_name not in ["Write", "Edit", "MultiEdit"]:
            return False
            
        file_path = args.get("file_path", "")
        
        # Trigger on documentation changes
        if ".claude/docs/" in file_path and file_path.endswith(".md"):
            return True
            
        # Trigger on hook/command changes (affects docs)
        if any(x in file_path for x in ["/hooks/", "/commands/"]):
            return True
            
        return False
```

### 2. Update Strategy

#### A. Immediate Updates (Automatic)
- **TOC Generation**: Update when headings change
- **Directory Structure**: Update when files added/removed  
- **Timestamp Updates**: Mark "last updated" automatically

#### B. Deferred Updates (Notification)
- **Broken Links**: Notify but don't auto-fix (might break intentionally)
- **Content Changes**: Suggest updates for stale content
- **Cross-references**: Validate but require approval

#### C. Smart Detection
```python
def detect_update_type(self, file_path, changes):
    """Determine what updates are needed"""
    updates_needed = []
    
    # TOC updates
    if self.has_heading_changes(changes):
        updates_needed.append(("toc", "auto"))
        
    # Structure updates  
    if self.is_structural_change(file_path):
        updates_needed.append(("structure", "auto"))
        
    # Link validation
    if self.has_link_changes(changes):
        updates_needed.append(("links", "notify"))
        
    return updates_needed
```

### 3. Incremental Processing

#### Change Detection
```python
class ChangeTracker:
    def __init__(self):
        self.cache_file = ".claude/state/doc_cache.json"
        self.file_hashes = self.load_cache()
        
    def has_changed(self, file_path):
        """Check if file has changed since last scan"""
        current_hash = self.calculate_hash(file_path)
        cached_hash = self.file_hashes.get(str(file_path))
        return current_hash != cached_hash
```

#### Selective Updates
- Only process changed files
- Update only affected sections
- Preserve unchanged content

### 4. Safety Mechanisms

#### Preserve Markers
```python
# In documentation files:
<!-- BEGIN-CUSTOM-SECTION -->
Custom content here...
<!-- END-CUSTOM-SECTION -->

<!-- DO-NOT-AUTO-UPDATE -->
This section is manually maintained
<!-- END-DO-NOT-AUTO-UPDATE -->
```

#### Validation Before Write
```python
def validate_update(self, original, updated):
    """Ensure update is safe"""
    # Check custom sections preserved
    custom_sections = self.extract_custom_sections(original)
    for section in custom_sections:
        if section not in updated:
            return False, "Custom section would be lost"
            
    # Check not removing too much
    if len(updated) < len(original) * 0.5:
        return False, "Update removes too much content"
        
    return True, "Update validated"
```

### 5. Configuration Schema

```json
{
  "doc_maintenance": {
    "enabled": true,
    "triggers": {
      "on_doc_change": true,
      "on_structure_change": true,
      "periodic_audit": true
    },
    "auto_updates": {
      "toc": true,
      "structure": true,
      "timestamps": true,
      "broken_links": false,
      "cross_references": false
    },
    "audit": {
      "check_staleness": true,
      "staleness_days": 30,
      "validate_links": true,
      "check_completeness": true
    },
    "preserve_markers": [
      "BEGIN-CUSTOM-SECTION",
      "DO-NOT-AUTO-UPDATE",
      "MANUAL-CONTENT"
    ],
    "excluded_paths": [
      ".claude/z__archive/",
      ".claude/project-management/completed/"
    ]
  }
}
```

### 6. Integration Points

#### PostToolUse Hook
```json
{
  "matcher": "Write|Edit|MultiEdit",
  "hooks": [{
    "type": "command",
    "command": "python3 '.claude/logic/hooks/core/doc-maintenance-hook.py'"
  }]
}
```

#### Scheduled Execution (Future)
```python
# Could be triggered by:
# 1. Startup hook checking last audit time
# 2. External cron job
# 3. Manual command with --audit flag
```

### 7. User Feedback

#### Progress Reporting
```python
def report_progress(self, action, status):
    """Keep user informed of documentation updates"""
    icons = {
        "scanning": "🔍",
        "updating": "📝", 
        "complete": "✅",
        "warning": "⚠️"
    }
    print(f"{icons.get(status, '•')} Documentation: {action}")
```

#### Summary Report
```
📚 Documentation Maintenance Complete
  ✅ Updated 3 TOCs
  ✅ Fixed 2 directory structures
  ⚠️  Found 4 broken links (manual review needed)
  ℹ️  2 files older than 30 days
```

## Implementation Phases

### Phase 1: Core Automation (Week 1)
1. Create unified hook file
2. Implement TOC auto-updates
3. Add structure updates
4. Basic testing

### Phase 2: Smart Features (Week 2)
1. Add change detection
2. Implement caching
3. Add preserve markers
4. Enhanced validation

### Phase 3: Advanced Features (Week 3)
1. Link validation
2. Staleness detection
3. Audit reporting
4. Performance optimization

## Risk Mitigation

1. **Start Conservative**: Auto-update only safe operations
2. **Dry Run Mode**: Test without writing
3. **Rollback Support**: Keep backup of changes
4. **Easy Disable**: Single flag to turn off
5. **Clear Logging**: Track all automated changes

## Success Metrics

- 90% reduction in manual TOC updates
- Zero broken TOCs after changes
- All READMEs stay current with structure
- No loss of manual content
- Developer satisfaction with automation