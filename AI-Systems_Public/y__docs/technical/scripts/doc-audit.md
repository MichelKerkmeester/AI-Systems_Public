# doc-audit.py

## Overview

**Script Name**: Documentation Auditor  
**Purpose**: Performs comprehensive health checks on documentation  
**Location**: `/scripts/doc-audit.py`  
**Performance**: ~3 seconds for full audit

## Description

The doc-audit.py script analyzes the documentation system to calculate health scores, identify issues, and provide improvement recommendations. It checks coverage, staleness, structure, and completeness of documentation.

## Usage

### Command Line
```bash
# Run full audit
python3 .claude/scripts/doc-audit.py

# Generate detailed report
python3 .claude/scripts/doc-audit.py --detailed

# Output to file
python3 .claude/scripts/doc-audit.py --output audit-report.json

# Check specific directory
python3 .claude/scripts/doc-audit.py --path .claude/docs/logic/
```

### Options
- `--detailed` - Include file-level analysis
- `--output` - Save results to file
- `--path` - Audit specific directory
- `--fix` - Attempt automatic fixes
- `--threshold` - Set health score threshold

## Health Score Calculation

### Overall Score (0-100%)
```python
score = weighted_average([
    (doc_coverage, 0.3),      # 30% - Code coverage
    (freshness, 0.2),         # 20% - Up-to-date docs
    (completeness, 0.2),      # 20% - Required sections
    (structure, 0.15),        # 15% - Organization
    (quality, 0.15)           # 15% - Content quality
])
```

### Component Scores

#### Documentation Coverage
- Measures documented vs undocumented code
- Checks hooks, scripts, commands
- Identifies missing documentation

#### Freshness Score
- Compares doc age to code changes
- Flags stale documentation
- Suggests update priorities

#### Completeness Check
- Required files (README, etc.)
- Standard sections presence
- Example availability

## Audit Results

### Metrics
```json
{
  "health_score": 46,
  "metrics": {
    "total_files": 26,
    "coverage": {
      "hooks": "0%",
      "scripts": "0%",
      "logic": "42%"
    },
    "staleness": {
      "outdated_files": 3,
      "average_age_days": 15
    }
  }
}
```

### Issues Detected
- Missing documentation files
- Broken internal links
- Outdated content
- Incomplete sections
- Poor structure

### Recommendations
```json
{
  "recommendations": [
    {
      "priority": "high",
      "type": "missing_docs",
      "action": "Create hook documentation",
      "impact": "+15% health score"
    }
  ]
}
```

## Reports Generated

### Summary Report
```markdown
# Documentation Audit Report

Generated: 2025-01-19 14:55
Health Score: **46%**

## Documentation Metrics
- Total files: 26
- README files: 10
- Guide files: 1
- Reference files: 1
- Example files: 1

## Documentation Coverage
- logic: 42% ❌
- hooks: 0% ❌
- scripts: 0% ❌
```

### Detailed Analysis
- File-by-file staleness check
- Missing section identification
- Link validation results
- Quality metrics per file

## Integration

### With Documentation Hook
The doc-update-hook can trigger audits:
```python
if significant_changes_detected():
    run_audit()
```

### With CI/CD
```yaml
- name: Documentation Health Check
  run: |
    python3 .claude/scripts/doc-audit.py --threshold 70
    if [ $? -ne 0 ]; then
      echo "Documentation health below threshold"
      exit 1
    fi
```

## Quality Checks

### Content Analysis
- Readability score
- Section completeness
- Example presence
- Code block validation

### Structure Validation
- Proper hierarchy
- Consistent formatting
- Navigation integrity
- Index accuracy

### Link Checking
- Internal references
- Anchor validation
- External links (optional)
- Image references

## Automatic Fixes

With `--fix` flag:
- Add missing README files
- Update stale timestamps
- Fix broken internal links
- Generate missing indexes

## Configuration

Default thresholds:
```python
HEALTH_THRESHOLD = 70
STALENESS_DAYS = 30
MIN_SECTION_COUNT = 3
REQUIRED_FILES = ["README.md", "INDEX.md"]
```

## Error Handling

- **Missing directories**: Creates if needed
- **Permission errors**: Logs and continues
- **Parsing failures**: Reports as issues
- **Network timeouts**: Skips external checks

## Performance Optimization

- Parallel file processing
- Cached file metadata
- Incremental updates
- Smart directory traversal

## Troubleshooting

### Low Health Score
1. Check coverage metrics
2. Review recommendations
3. Update stale documentation
4. Add missing files

### Audit Failures
- Verify script permissions
- Check Python dependencies
- Review error logs
- Validate directory structure

### Performance Issues
- Limit scope with `--path`
- Disable external checks
- Use incremental mode
- Check disk I/O

## Best Practices

1. **Regular audits**: Weekly minimum
2. **Act on recommendations**: Prioritize high impact
3. **Set thresholds**: Enforce quality standards
4. **Track trends**: Monitor score over time
5. **Automate fixes**: Use `--fix` for common issues

## Output Formats

### Console Output
- Colored health indicators
- Progress bars
- Summary statistics
- Top recommendations

### JSON Report
```json
{
  "audit_results": {
    "timestamp": "2025-01-19T14:55:00Z",
    "health_score": 46,
    "details": {...}
  }
}
```

### Markdown Report
- Human-readable format
- Actionable sections
- Visual indicators
- Linked references

## Related Documentation

- [doc-updater.py](./doc-updater.md) - Structure updates
- [Documentation Standards](../../standards/documentation.md)
- [Quality Metrics](../../metrics/documentation.md)