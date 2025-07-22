# Documentation Automation Test Plan

## Test Environment Setup

### 1. Create Test Documentation Structure
```bash
mkdir -p /tmp/test-docs/{guides,reference,examples}
cp -r .claude/docs/* /tmp/test-docs/
```

### 2. Test Data Preparation
Create files with various documentation patterns:
- Files with TOCs
- Files with broken links
- Files with custom sections
- Files without structure

## Test Scenarios

### 1. TOC Auto-Update Tests

#### Test 1.1: New Heading Added
```markdown
# Original File
## Section 1
## Section 2

# Modified File  
## Section 1
## New Section
## Section 2
```
**Expected**: TOC updates automatically to include "New Section"

#### Test 1.2: Heading Text Changed
```markdown
## Old Heading Name → ## New Heading Name
```
**Expected**: TOC reflects new heading text

#### Test 1.3: Custom TOC Section
```markdown
<!-- BEGIN-CUSTOM-SECTION -->
## Table of Contents
- Custom entry 1
- Custom entry 2
<!-- END-CUSTOM-SECTION -->
```
**Expected**: Custom TOC preserved, not auto-generated

### 2. Structure Update Tests

#### Test 2.1: New File Added
```bash
touch /tmp/test-docs/guides/new-guide.md
```
**Expected**: README structure updates to show new file

#### Test 2.2: File Removed
```bash
rm /tmp/test-docs/guides/old-guide.md
```
**Expected**: Structure updates, removed file not shown

#### Test 2.3: Directory Reorganization
```bash
mkdir /tmp/test-docs/guides/advanced
mv /tmp/test-docs/guides/complex-*.md /tmp/test-docs/guides/advanced/
```
**Expected**: Structure reflects new organization

### 3. Safety Tests

#### Test 3.1: Preserve Custom Content
```markdown
<!-- DO-NOT-AUTO-UPDATE -->
This content should never change
Even with automation
<!-- END-DO-NOT-AUTO-UPDATE -->
```
**Expected**: Content remains unchanged

#### Test 3.2: Large Content Removal Protection
Create file with 1000 lines, try update that would leave 100 lines
**Expected**: Update rejected, warning shown

#### Test 3.3: Concurrent Edit Protection
1. Open file in editor
2. Trigger documentation update
**Expected**: Update detects file in use, defers

### 4. Link Validation Tests

#### Test 4.1: Internal Link Broken
```markdown
[Link to missing file](./missing.md)
```
**Expected**: Warning generated, link reported but not auto-fixed

#### Test 4.2: Valid Link Preservation  
```markdown
[Valid link](./existing-file.md)
```
**Expected**: Link remains unchanged

#### Test 4.3: External Link Handling
```markdown
[External](https://example.com)
```
**Expected**: External links ignored (not validated)

### 5. Performance Tests

#### Test 5.1: Large Documentation Set
- Create 100 documentation files
- Modify 5 files
**Expected**: Only 5 files processed, <2 seconds

#### Test 5.2: Deep Nesting
- Create 10-level deep directory structure
**Expected**: Structure updates correctly, depth limited in display

#### Test 5.3: Circular References
```markdown
File A links to → File B links to → File A
```
**Expected**: Circular reference detected, handled gracefully

### 6. Integration Tests

#### Test 6.1: Hook Triggering
```bash
echo "# New Section" >> .claude/docs/test.md
```
**Expected**: Hook triggers, appropriate updates made

#### Test 6.2: Multiple File Changes
```bash
for i in {1..5}; do
  echo "## Section $i" >> .claude/docs/test$i.md
done
```
**Expected**: All files processed in single batch

#### Test 6.3: Non-Documentation Changes
```bash
echo "code" >> .claude/logic/test.py
```
**Expected**: No documentation updates triggered

### 7. Error Handling Tests

#### Test 7.1: Malformed Markdown
```markdown
## Heading without closing
[Broken link syntax(./file.md)
```
**Expected**: Graceful handling, file skipped with warning

#### Test 7.2: Permission Errors
```bash
chmod 444 /tmp/test-docs/readonly.md
```
**Expected**: Error logged, other files still processed

#### Test 7.3: Missing Configuration
Remove doc_maintenance section from settings
**Expected**: Defaults used, operation continues

## Validation Checklist

### Pre-Implementation
- [ ] Test scripts created
- [ ] Test data prepared
- [ ] Backup of real docs made

### Core Functionality
- [ ] TOC updates work correctly
- [ ] Structure updates work correctly
- [ ] Custom content preserved
- [ ] Safety checks functioning

### Edge Cases
- [ ] Large files handled
- [ ] Circular references handled
- [ ] Malformed content handled
- [ ] Permission errors handled

### Performance
- [ ] Incremental updates working
- [ ] Caching functioning
- [ ] Batch processing efficient

### Integration
- [ ] Hook triggers correctly
- [ ] Settings respected
- [ ] Error reporting clear

## Rollback Test

### Disable Automation
1. Set `"enabled": false` in settings
2. Make documentation change
**Expected**: No automatic updates

### Manual Execution Still Works
```bash
python3 .claude/logic/scripts/doc-updater.py
```
**Expected**: Manual execution successful

## Success Criteria

1. **All tests pass** without manual intervention
2. **No data loss** in any test scenario
3. **Performance targets** met (<2s for typical updates)
4. **Error handling** graceful and informative
5. **Integration** seamless with existing workflow

## Test Execution Log

| Test ID | Date | Result | Notes |
|---------|------|--------|-------|
| 1.1 | - | - | - |
| 1.2 | - | - | - |
| ... | - | - | - |

## Post-Test Cleanup

```bash
rm -rf /tmp/test-docs
# Restore any modified files
git checkout .claude/docs/
```