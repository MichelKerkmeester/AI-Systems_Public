# add-toc.py

## Overview

**Script Name**: Table of Contents Generator  
**Purpose**: Automatically generates and updates table of contents in markdown files  
**Location**: `/scripts/add-toc.py`  
**Performance**: ~2 seconds for all documentation files

## Description

The add-toc.py script scans markdown files and generates table of contents based on the header structure. It intelligently handles existing TOCs, code blocks, and special formatting while maintaining proper anchor links for navigation.

## Usage

### Command Line
```bash
# Process single file
python3 .claude/logic/scripts/add-toc.py path/to/file.md

# Process directory
python3 .claude/logic/scripts/add-toc.py .claude/docs/

# Process with options
python3 .claude/logic/scripts/add-toc.py --update --recursive .claude/docs/
```

### Options
- `--update` - Update existing TOCs (default: add only if missing)
- `--recursive` - Process subdirectories
- `--min-headers` - Minimum headers required for TOC (default: 3)
- `--max-depth` - Maximum heading depth to include (default: 3)

## Features

### Smart Header Detection
- Skips headers inside code blocks
- Ignores the main title (first H1)
- Excludes existing TOC headers
- Handles special characters in anchors

### TOC Formatting
```markdown
## Table of Contents

- [Section 1](#section-1)
  - [Subsection 1.1](#subsection-11)
  - [Subsection 1.2](#subsection-12)
- [Section 2](#section-2)
  - [Subsection 2.1](#subsection-21)
```

### Anchor Generation
Converts headers to GitHub-compatible anchors:
- Lowercase all text
- Replace spaces with hyphens
- Remove special characters
- Handle duplicates with numbering

## Integration

### With Documentation Hooks
The doc-update-hook.py automatically calls this script when documentation changes are detected.

### With CI/CD
Can be integrated into build pipelines:
```yaml
- name: Generate TOCs
  run: python3 .claude/logic/scripts/add-toc.py --update --recursive docs/
```

## Code Structure

### Main Functions
```python
extract_headers(content: str) -> List[Tuple[int, str]]
# Extracts headers from markdown content

generate_toc(headers: List[Tuple[int, str]]) -> str
# Generates TOC from header list

update_file_toc(file_path: Path) -> bool
# Updates TOC in a single file

process_directory(dir_path: Path, recursive: bool) -> int
# Processes all markdown files in directory
```

### Algorithm
1. Read markdown file
2. Extract headers (excluding code blocks)
3. Generate TOC with proper indentation
4. Insert after first H1 or at beginning
5. Preserve existing content

## Examples

### Before
```markdown
# My Document

This is the introduction.

## First Section

Content here.

### Subsection

More content.
```

### After
```markdown
# My Document

## Table of Contents

- [First Section](#first-section)
  - [Subsection](#subsection)

This is the introduction.

## First Section

Content here.

### Subsection

More content.
```

## Error Handling

- **File not found**: Logs error and continues
- **Permission denied**: Skips file with warning
- **Invalid markdown**: Best effort parsing
- **Encoding issues**: Falls back to UTF-8

## Performance Optimization

- Regex compilation cached
- Single file pass for read/write
- Minimal string operations
- Efficient anchor generation

## Configuration

Default settings in script:
```python
MIN_HEADERS_FOR_TOC = 3
MAX_TOC_DEPTH = 3
TOC_MARKER = "## Table of Contents"
EXCLUDE_PATTERNS = ["README.md", "CHANGELOG.md"]
```

## Troubleshooting

### TOC Not Generated
- Check minimum header count
- Verify file is markdown (.md)
- Ensure headers use proper syntax
- Check for code block interference

### Wrong Anchors
- GitHub uses specific anchor rules
- Special characters are stripped
- Duplicates get numeric suffixes
- Case is always lowercase

### Performance Issues
- Large files may take longer
- Use `--max-depth` to limit TOC size
- Consider parallel processing for many files

## Best Practices

1. **Run regularly**: Keep TOCs updated
2. **Review changes**: Verify anchor links work
3. **Consistent headers**: Use proper markdown syntax
4. **Avoid special characters**: In header text
5. **Test navigation**: Click TOC links

## Related Documentation

- [doc-updater.py](./doc-updater.md) - Calls this script
- [Documentation Standards](../../standards/documentation.md)
- [Markdown Guide](../../guides/markdown.md)