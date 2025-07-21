# Inline Comment Style Enforcement

**Created:** 2025-07-19
**Priority:** High
**Type:** Code Quality
**Estimated Effort:** 2 days

## Problem Statement

Force the system to use the inline comment style that is already in place in other JavaScript, CSS, etc. files. Currently, there's no enforcement of consistent comment styles across the codebase.

## Current Comment Patterns

### JavaScript Comment Style
```javascript
// ───────────────────────────────────────────────────────────────
// Component: Name
// Description of what this component does
// ───────────────────────────────────────────────────────────────

/* ─────────────────────────────────────────────────────────────
   Section Name
─────────────────────────────────────────────────────────────── */

// Single line comments for inline explanations
```

### CSS Comment Style
```css
/* ───────────────────────────────────────────────────────────────
   Component: Name
   Description
─────────────────────────────────────────────────────────────── */

/*----------------------
  Subsection Name
----------------------*/

/* Single line explanations */
```

## Solution Design

### 1. Update patterns.json

```json
{
  "comment_styles": {
    "javascript": {
      "file_header": [
        "// ───────────────────────────────────────────────────────────────",
        "// {title}",
        "// {description}",
        "// ───────────────────────────────────────────────────────────────"
      ],
      "section": [
        "/* ─────────────────────────────────────────────────────────────",
        "   {section_name}",
        "─────────────────────────────────────────────────────────────── */"
      ],
      "inline": "// {comment}",
      "multiline": [
        "/*",
        " * {line}",
        " */"
      ]
    },
    "css": {
      "file_header": [
        "/* ───────────────────────────────────────────────────────────────",
        "   {title}",
        "   {description}",
        "─────────────────────────────────────────────────────────────── */"
      ],
      "section": [
        "/*----------------------",
        "  {section_name}",
        "----------------------*/"
      ],
      "inline": "/* {comment} */",
      "property": "/* {comment} */"
    }
  }
}
```

### 2. Create Comment Style Hook

```python
# .claude/hooks/code/comment-style-hook.py
class CommentStyleHook(HookBase):
    def __init__(self):
        super().__init__("CommentStyle")
        self.load_comment_patterns()
    
    def pre_edit(self, file_path, content):
        """Apply comment style before editing"""
        if self.needs_comment_formatting(file_path, content):
            return self.format_comments(file_path, content)
        return content
    
    def format_comments(self, file_path, content):
        file_type = self.get_file_type(file_path)
        if file_type in self.comment_patterns:
            # Apply appropriate comment style
            return self.apply_comment_style(content, file_type)
        return content
```

### 3. Create Comment Formatter Utility

```python
# .claude/scripts/comment-formatter.py
class CommentFormatter:
    """Formats comments according to project standards"""
    
    def format_js_file_header(self, title, description):
        return "\n".join([
            "// " + "─" * 63,
            f"// {title}",
            f"// {description}",
            "// " + "─" * 63
        ])
    
    def format_js_section(self, section_name):
        return "\n".join([
            "/* " + "─" * 61,
            f"   {section_name}",
            "─" * 63 + " */"
        ])
    
    def format_css_header(self, title, description):
        return "\n".join([
            "/* " + "─" * 61,
            f"   {title}",
            f"   {description}",
            "─" * 63 + " */"
        ])
```

### 4. Integration with Edit Tools

```python
# Hook into Edit and MultiEdit tools
class EnhancedEdit(Edit):
    def __init__(self):
        super().__init__()
        self.comment_formatter = CommentFormatter()
    
    def pre_process_content(self, file_path, new_content):
        """Process content before writing"""
        # Check if adding new component/section
        if self.is_new_component(new_content):
            return self.add_proper_headers(file_path, new_content)
        return new_content
```

### 5. Create Validation Script

```python
# .claude/scripts/validate-comments.py
def validate_comment_style(file_path):
    """Validate file follows comment conventions"""
    issues = []
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check for improper comment styles
    if file_path.endswith('.js'):
        # Check for missing headers
        if not has_proper_js_header(content):
            issues.append("Missing proper file header")
        
        # Check for inconsistent section markers
        if has_mixed_comment_styles(content):
            issues.append("Mixed comment styles detected")
    
    return issues
```

## Implementation Steps

### Phase 1: Pattern Definition (Day 1 Morning)
1. [ ] Document all comment patterns in patterns.json
2. [ ] Create comment style guide document
3. [ ] Identify files needing updates

### Phase 2: Hook Development (Day 1 Afternoon)
1. [ ] Create comment-style-hook.py
2. [ ] Implement format detection logic
3. [ ] Add pattern matching for different comment types

### Phase 3: Formatter Creation (Day 2 Morning)
1. [ ] Build comment formatter utility
2. [ ] Create conversion functions
3. [ ] Add file type detection

### Phase 4: Integration (Day 2 Afternoon)
1. [ ] Integrate with Edit/MultiEdit tools
2. [ ] Add pre-commit validation
3. [ ] Create batch update script

### Phase 5: Testing & Rollout (Day 2 Evening)
1. [ ] Test on sample files
2. [ ] Update existing files gradually
3. [ ] Document the new system

## Configuration

### Hook Settings
```json
{
  "hooks": {
    "PreEdit": {
      "comment_style": {
        "enabled": true,
        "path": ".claude/hooks/code/comment-style-hook.py",
        "enforce": true,
        "auto_format": true
      }
    }
  }
}
```

### Validation Rules
```json
{
  "comment_validation": {
    "require_file_headers": true,
    "enforce_section_style": true,
    "max_line_length": 65,
    "separator_char": "─",
    "section_separator": "─"
  }
}
```

## Examples

### Before
```javascript
/**
 * Some component
 */
function myComponent() {
    // TODO: implement
}
```

### After
```javascript
// ───────────────────────────────────────────────────────────────
// Component: My Component
// Handles specific functionality for the feature
// ───────────────────────────────────────────────────────────────

function myComponent() {
    // TODO: implement
}
```

## Success Metrics

1. **Consistency:** 100% of new code follows style
2. **Automation:** 95% of comments auto-formatted
3. **Adoption:** No manual formatting needed
4. **Quality:** Clear, readable comment structure

## Testing Plan

1. **Unit Tests:**
   - Pattern matching accuracy
   - Format conversion correctness
   - File type detection

2. **Integration Tests:**
   - Hook activation on edits
   - Proper formatting applied
   - No content corruption

3. **Visual Review:**
   - Comments look consistent
   - Proper alignment maintained
   - Special characters preserved

## Rollback Plan

1. Disable hook in settings.json
2. Keep original files backed up
3. Gradual rollout by file type
4. Manual override option available

## Future Enhancements

1. **Smart Comments:**
   - Auto-generate component descriptions
   - Extract function purposes
   - Link to documentation

2. **IDE Integration:**
   - VSCode snippets
   - Format on save
   - Lint warnings

3. **Documentation:**
   - Auto-generate from comments
   - Maintain comment index
   - Search by component

## References

- Current examples: `src/C__components/grid/cta-hover--departments.js`
- Style patterns: `src/B__global/css/fluid-responsive.css`
- Hook documentation: `.claude/logic/shared/hooks-in-cc.md`