# doc-updater.py

## Overview

**Script Name**: Documentation Structure Updater  
**Purpose**: Maintains documentation structure, links, and indexes  
**Location**: `/scripts/doc-updater.py`  
**Performance**: ~5 seconds for full update

## Description

The doc-updater.py script automatically maintains the documentation system by updating directory structures, validating internal links, generating index files, and ensuring cross-references remain accurate. It's the main workhorse for documentation maintenance.

## Usage

### Command Line
```bash
# Update entire documentation
python3 .claude/logic/scripts/doc-updater.py

# Update specific directory
python3 .claude/logic/scripts/doc-updater.py --path .claude/docs/logic/

# Dry run (preview changes)
python3 .claude/logic/scripts/doc-updater.py --dry-run

# Force regeneration
python3 .claude/logic/scripts/doc-updater.py --force
```

### Options
- `--path` - Target directory (default: all docs)
- `--dry-run` - Preview without changes
- `--force` - Regenerate all indexes
- `--fix-links` - Repair broken links
- `--verbose` - Detailed output

## Core Functions

### 1. Directory Structure Update
```python
def update_directory_structure():
    # Creates missing directories
    # Adds README.md to new directories
    # Updates INDEX.md files
    # Maintains hierarchy
```

### 2. Link Validation
```python
def validate_internal_links():
    # Scans all markdown files
    # Checks link targets exist
    # Validates anchor references
    # Reports broken links
```

### 3. Index Generation
```python
def generate_index_files():
    # Creates INDEX.md per directory
    # Lists all documentation files
    # Generates navigation structure
    # Updates cross-references
```

### 4. TOC Updates
```python
def update_table_of_contents():
    # Calls add-toc.py for each file
    # Maintains consistent formatting
    # Updates anchor links
    # Preserves custom TOCs
```

## Update Process

### Phase 1: Analysis
1. Scan documentation tree
2. Build file inventory
3. Create link graph
4. Identify issues

### Phase 2: Structure
1. Create missing directories
2. Add required files
3. Update hierarchy
4. Fix permissions

### Phase 3: Content
1. Update INDEX files
2. Fix broken links
3. Generate TOCs
4. Update timestamps

### Phase 4: Validation
1. Verify all changes
2. Test link integrity
3. Check file access
4. Generate report

## Generated Files

### INDEX.md Format
```markdown
# Directory Name

## Contents

### Guides
- [Getting Started](./getting-started.md)
- [Advanced Usage](./advanced.md)

### Reference
- [API Reference](./api.md)
- [Configuration](./config.md)

### Examples
- [Basic Examples](./examples/basic.md)
- [Advanced Examples](./examples/advanced.md)
```

### README.md Template
```markdown
# [Directory Name]

Brief description of this documentation section.

## Overview

What this section contains and who it's for.

## Contents

See [INDEX.md](./INDEX.md) for complete listing.
```

## Link Management

### Link Types Handled
- Relative paths: `./file.md`
- Parent paths: `../other/file.md`
- Anchors: `#section-name`
- Combined: `../file.md#section`

### Link Fixes Applied
- Update moved files
- Fix case sensitivity
- Correct extensions
- Normalize paths

### Broken Link Handling
```python
if link_broken:
    if can_fix_automatically():
        fix_link()
        log_fix()
    else:
        report_broken_link()
        suggest_fix()
```

## Reports Generated

### Update Report
```markdown
# Documentation Update Report

## Summary
- Files processed: 42
- Indexes updated: 8
- Links fixed: 12
- Issues found: 3

## Changes Made
1. Updated /docs/logic/INDEX.md
2. Fixed broken link in commands.md
3. Added TOC to 5 files

## Remaining Issues
- Dead link in old-guide.md
- Missing examples in api.md
```

### Link Validation Report
```
Broken Links Found:
- commands.md:45 -> ../missing.md (target not found)
- guide.md:23 -> #wrong-anchor (anchor not found)
  
Suggested Fixes:
- ../missing.md -> ../logic/overview.md
- #wrong-anchor -> #correct-anchor
```

## Integration

### With Documentation Hook
Called automatically by doc-update-hook:
```python
# In doc-update-hook.py
if doc_changed:
    subprocess.run(["python3", doc_updater_path])
```

### With Other Scripts
- Calls `add-toc.py` for TOC generation
- Triggers `doc-audit.py` after major updates
- Updates feed into version control

## Error Handling

### Common Issues
- **Permission denied**: Checks permissions first
- **File locks**: Waits and retries
- **Encoding errors**: UTF-8 fallback
- **Circular links**: Detection and warning

### Recovery Mechanisms
- Backup before changes
- Atomic file operations
- Rollback on failure
- Detailed error logs

## Performance Optimization

### Strategies
- Incremental updates (only changed files)
- Parallel processing for large directories
- Cached file metadata
- Smart diff detection

### Benchmarks
- 100 files: ~2 seconds
- 500 files: ~8 seconds
- 1000 files: ~15 seconds

## Configuration

Settings in script:
```python
# Patterns
IGNORE_PATTERNS = [".git", "__pycache__", "*.tmp"]
INDEX_FILENAME = "INDEX.md"
README_TEMPLATE = "templates/README.template.md"

# Behavior
AUTO_FIX_LINKS = True
GENERATE_INDEXES = True
UPDATE_TOCS = True
MAX_DEPTH = 10
```

## Best Practices

1. **Regular runs**: Daily or on changes
2. **Review reports**: Check for issues
3. **Fix immediately**: Don't let issues accumulate
4. **Test links**: Verify fixes work
5. **Commit changes**: Track documentation updates

## Troubleshooting

### Script Not Running
- Check Python version (3.8+)
- Verify script permissions
- Check working directory
- Review error logs

### Wrong Updates
- Use `--dry-run` first
- Check ignore patterns
- Verify template files
- Review configuration

### Performance Issues
- Limit scope with `--path`
- Disable unnecessary features
- Check disk space
- Monitor memory usage

## Advanced Usage

### Custom Templates
```bash
# Use custom README template
DOC_README_TEMPLATE=/path/to/template.md python3 doc-updater.py

# Custom index format
DOC_INDEX_FORMAT=compact python3 doc-updater.py
```

### Automation
```bash
# Cron job for daily updates
0 2 * * * cd /project && python3 .claude/logic/scripts/doc-updater.py

# Git hook for automatic updates
#!/bin/bash
# .git/hooks/pre-commit
python3 .claude/logic/scripts/doc-updater.py --path .claude/docs/
```

## Related Documentation

- [add-toc.py](./add-toc.md) - TOC generation
- [doc-audit.py](./doc-audit.md) - Health checking
- [Documentation Hook](../hooks/doc-update-hook.md) - Automatic triggers