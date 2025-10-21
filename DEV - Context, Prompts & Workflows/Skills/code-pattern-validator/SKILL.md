---
name: code-pattern-validator
description: Validate JavaScript files against Webflow project code standards, naming conventions, initialization patterns, and platform constraints. Use when reviewing code quality, catching violations before bugs occur, or enforcing consistency. Validates snake_case naming, 3-line file headers, Webflow.push initialization, comment density, ARIA attributes, and platform-specific patterns like collection handling
---

# Code Pattern Validator
Automated Code Standards Compliance

> Change Notes (2025-10-21)
- Removed dependency on references/* and embedded full 37-rule catalog inline
- Added YAML → Steps Crosswalk (canonical sources: SKILL.md + knowledge/*.md)
- Normalized workflow headings and updated token budget note

## 1. 🎯 When to Use

**Use this skill when**:
- Reviewing code for standards compliance before committing
- Validating generated code from Webflow Component Generator
- Auditing existing files for quality issues
- Catching initialization pattern violations (most common Webflow bug)
- Enforcing naming conventions (snake_case, kebab-case, UPPER_SNAKE_CASE)
- Checking platform constraint awareness (collection handling, async rendering)
- Verifying accessibility compliance (ARIA attributes, focus management)

**Do NOT use this skill for**:
- Runtime error debugging - use `knowledge/debugging.md` instead
- Functional/logic testing - this validates code style and patterns only
- Performance profiling - this checks for performance anti-patterns but doesn't profile
- Webflow Designer issues - this validates JavaScript only

.

## 2. 🛠️ How It Works

This skill analyzes JavaScript files against 37 validation rules organized into 8 categories (Naming, Headers, Comments, Initialization, Platform Constraints, Integrations, Accessibility, Error Handling). It detects violations, provides specific line numbers, suggests fixes, and generates a compliance score.

**Process Overview**:
1. Load target file(s) and determine validation level (quick/standard/comprehensive)
2. Execute validation passes based on level, checking rules by category
3. Collect violations with severity (ERROR/WARNING/INFO), line numbers, and context
4. Generate detailed validation report with compliance score and fix suggestions
5. Reference knowledge base documents for complete rule explanations

.

## 3. 📥 Inputs

### Required Inputs

**File Path(s)**:
- **Type**: String or array of strings
- **Format**: Absolute or relative paths to JavaScript files
- **Description**: Files to validate (supports glob patterns)
- **Examples**:
  - Single file: `/path/to/src/modal/modal_welcome.js`
  - Multiple files: `/path/to/src/**/*.js`
  - Specific files: `['file1.js', 'file2.js', 'file3.js']`

### Optional Inputs

**Validation Level**:
- **Type**: String (enum)
- **Default**: `standard`
- **Options**:
  - `quick` - Fast validation (18 rules): Headers, initialization pattern, naming conventions only
  - `standard` - Balanced validation (31 rules): Quick checks + platform constraints + ARIA + integrations
  - `comprehensive` - Thorough validation (37 rules): All checks + comment quality + error handling
- **Description**: Controls depth of validation
- **Example**: `comprehensive`

**Report Format**:
- **Type**: String (enum)
- **Default**: `detailed`
- **Options**:
  - `detailed` - Full report with all violations and fix suggestions
  - `summary` - Compliance score and violation counts only
  - `json` - Machine-readable JSON format
- **Description**: Output format preference
- **Example**: `detailed`

.

## 4. ✅ Outputs

### Primary Output

**Validation Report**:
- **Format**: Markdown (or JSON if requested)
- **Location**: Console output (or file if specified)
- **Structure**:
```markdown
# Validation Report: [filename]

**File**: /path/to/file.js
**Date**: [timestamp]
**Validation Level**: [Quick/Standard/Comprehensive]
**Compliance Score**: 85%

## Summary
- **Errors**: 2 (BLOCKING - must fix before production)
- **Warnings**: 5 (Recommended fixes for code quality)
- **Info**: 3 (Best practice suggestions)

## Errors (Must Fix)

### ERROR: Missing Initialization Pattern (Rule 4.1)
**Severity**: P0 - BLOCKING
**Category**: Initialization Pattern
**Line**: N/A (pattern not found in file)
**Issue**: File does not use required Webflow.push initialization pattern
**Impact**: Code may not execute correctly in Webflow environment
**Fix**:
```javascript
// Add this at the end of your file:
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init_function);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init_function);
} else {
  init_function();
}
```
**References**: knowledge/initialization_pattern.md:17-34

### ERROR: Naming Convention Violation (Rule 1.1)
**Severity**: P0 - BLOCKING
**Category**: Naming Conventions
**Line**: 42
**Current Code**: `function getData() { ... }`
**Issue**: Function name uses camelCase instead of required snake_case
**Impact**: Violates project naming standards
**Fix**: Rename to `function get_data() { ... }`
**References**: knowledge/code_standards.md:10-13

## Warnings (Should Fix)

### WARNING: Comment Density Exceeded (Rule 3.1)
**Severity**: P2
**Category**: Commenting
**Lines**: 15-45
**Issue**: 8 comments in 10 lines (limit: 5 comments per 10 lines)
**Impact**: Reduces code readability
**Fix**: Remove redundant comments that explain "what" code does. Keep only comments explaining "why"
**References**: knowledge/code_standards.md:80-89

### WARNING: Missing ARIA Attributes (Rule 7.1)
**Severity**: P2
**Category**: Accessibility
**Line**: 156
**Element**: Modal dialog element
**Issue**: Interactive modal lacks aria-label and aria-describedby
**Impact**: Poor screen reader experience
**Fix**:
```javascript
dialog.setAttribute('aria-label', 'Welcome modal');
dialog.setAttribute('aria-describedby', 'modal-description-id');
```
**References**: specs/004-claude-skills/analysis/patterns.md - Accessibility Patterns

## Info (Best Practices)

### INFO: Consider Event Delegation (Rule 5.3)
**Severity**: P3
**Category**: Platform Constraints
**Line**: 89
**Current**: Direct event listener on collection item
**Suggestion**: Use event delegation for Webflow collection items
**Why**: Collection items render async; delegation handles dynamic content
**Example**:
```javascript
// Instead of:
item.addEventListener('click', handler);

// Use:
document.addEventListener('click', (e) => {
  if (e.target.closest('.w-dyn-item')) handler(e);
});
```
**References**: knowledge/webflow_platform_constraints.md:133-144

## Recommendations
1. **Critical**: Fix 2 errors (BLOCKING) before production deployment
2. **High Priority**: Address 5 warnings to improve code quality
3. **Review**: knowledge/code_standards.md for complete naming convention guide
4. **Consider**: Adding ARIA attributes for improved accessibility

## Next Steps
- Fix ERROR violations (blocks production)
- Address WARNING violations (improves quality)
- Review INFO suggestions (best practices)
- Re-run validator to confirm all issues resolved
```

.

## YAML → Steps Crosswalk

- Source: No dedicated YAML file. Canonical sources are this SKILL.md and knowledge documents:
  - knowledge/code_standards.md
  - knowledge/initialization_pattern.md
  - knowledge/webflow_platform_constraints.md
- Mapping:
  - Step 1 → Rule Loading & Categorization (Sections: 5.1 + Rules Catalog)
  - Step 2 → File Reading & Parsing
  - Step 3 → Validation Execution (Levels: quick/standard/comprehensive)
  - Step 4 → Report Generation

## 5. 🚀 Workflow

### Step 1: Rule Loading & Categorization

Load the inlined Rules Catalog and organize by:
- **Category**: Naming, Headers, Comments, Initialization, Platform, Integrations, Accessibility, Errors
- **Priority**: P0 (ERROR - blocking), P1 (ERROR - high), P2 (WARNING), P3 (INFO)
- **Validation Level**: quick / standard / comprehensive

**Rules Loaded**:
- P0 Rules (12 total): Initialization pattern, naming conventions, file headers
- P1 Rules (7 total): Platform constraints, external integrations
- P2 Rules (14 total): Comments, accessibility, error handling
- P3 Rules (Various): Best practices and suggestions

Note: This skill is self-contained (No External References). See knowledge/code_standards.md and knowledge/webflow_platform_constraints.md for detailed guidance.

### Step 2: File Reading & Parsing

Read target file(s) and perform initial analysis:
- Line-by-line tokenization
- Comment extraction and categorization
- Function/variable name extraction
- Pattern matching for code structures

**Actions Taken**:
- Read file content
- Split into lines with line numbers
- Extract code elements (functions, variables, constants, classes)
- Identify comment blocks and inline comments
- Detect code patterns (initialization, imports, exports)

### Step 3: Validation Execution

Execute validation rules based on selected level:

#### Validation Level to Rules Mapping

| Rule | Category | Quick | Standard | Comprehensive |
|------|----------|:-----:|:--------:|:-------------:|
| 1.1 | Function names (snake_case) | ✓ | ✓ | ✓ |
| 1.2 | Variable names (snake_case) | ✓ | ✓ | ✓ |
| 1.3 | Constants (UPPER_SNAKE_CASE) | ✓ | ✓ | ✓ |
| 1.4 | Private members (_prefix) | ✓ | ✓ | ✓ |
| 1.5 | Boolean prefixes (is_/has_/can_) | ✓ | ✓ | ✓ |
| 1.6 | Event handlers (handle_) | ✓ | ✓ | ✓ |
| 1.7 | Callbacks (on_) | ✓ | ✓ | ✓ |
| 1.8 | CSS classes (kebab-case) | ✓ | ✓ | ✓ |
| 1.9 | BEM modifiers (--) | ✓ | ✓ | ✓ |
| 1.10 | File names (snake_case) | ✓ | ✓ | ✓ |
| 1.11 | Class names (PascalCase) | ✓ | ✓ | ✓ |
| 2.1 | File header (3 lines) | ✓ | ✓ | ✓ |
| 2.2 | No metadata in header | ✓ | ✓ | ✓ |
| 2.3 | Section headers (numbered) | - | ✓ | ✓ |
| 3.1 | Comment density (≤5/10 lines) | ✓ | ✓ | ✓ |
| 3.2 | Comments explain "why" | - | - | ✓ |
| 3.3 | No commented-out code | - | - | ✓ |
| 3.4 | TODO with context | - | - | ✓ |
| 4.1 | Webflow init pattern | ✓ | ✓ | ✓ |
| 4.2 | IIFE wrapper | - | ✓ | ✓ |
| 4.3 | No direct DOMContentLoaded | ✓ | ✓ | ✓ |
| 4.4 | No jQuery ready | ✓ | ✓ | ✓ |
| 4.5 | No window.onload | ✓ | ✓ | ✓ |
| 5.1 | No ID selectors in collections | - | ✓ | ✓ |
| 5.2 | Collection timing awareness | - | ✓ | ✓ |
| 5.3 | Event delegation | - | ✓ | ✓ |
| 5.4 | No function.name reliance | - | ✓ | ✓ |
| 5.5 | Collection limit awareness | - | - | ✓ |
| 6.1 | Motion.dev availability check | - | ✓ | ✓ |
| 6.2 | Lenis availability check | - | ✓ | ✓ |
| 6.3 | Third-party defensive loading | - | ✓ | ✓ |
| 7.1 | ARIA attributes | - | ✓ | ✓ |
| 7.2 | Focus management | - | ✓ | ✓ |
| 7.3 | Keyboard navigation | - | ✓ | ✓ |
| 8.1 | Try-catch for APIs | - | - | ✓ |
| 8.2 | Graceful degradation | - | - | ✓ |
| 8.3 | Console errors | - | - | ✓ |

**Rule Count by Level**:
- **Quick**: 18 rules (critical naming, headers, initialization)
- **Standard**: 31 rules (Quick + platform constraints + integrations + accessibility)
- **Comprehensive**: 37 rules (All rules including comment quality + error handling)

**Validation Methods**:
- Pattern matching (regex-based detection)
- Line-by-line scanning (comment density, headers)
- Semantic analysis (context-aware platform constraints)
- Reference cross-checking (patterns.md for comprehensive)

#### Rules Catalog (Inline)

- This catalog replaces external references and is the canonical rule set (37 rules). Each rule lists detection and fix guidance. See knowledge/code_standards.md, knowledge/initialization_pattern.md, knowledge/webflow_platform_constraints.md for deeper examples.

Naming (1.x)
- 1.1 Function names (snake_case)
  - Detect: camelCase function declarations; Fix: rename to snake_case
- 1.2 Variable names (snake_case)
  - Detect: camelCase/ PascalCase variables; Fix: snake_case
- 1.3 Constants (UPPER_SNAKE_CASE)
  - Detect: const not UPPER_SNAKE_CASE; Fix: rename
- 1.4 Private members (_prefix)
  - Detect: internal helpers without _; Fix: add _ prefix where applicable
- 1.5 Boolean prefixes (is_/has_/can_)
  - Detect: boolean names without prefixes; Fix: rename
- 1.6 Event handlers (handle_*)
  - Detect: handlers without handle_ prefix; Fix: rename
- 1.7 Callbacks (on_*)
  - Detect: callback props/args not prefixed; Fix: rename
- 1.8 CSS classes (kebab-case)
  - Detect: non-kebab CSS class strings; Fix: kebab-case
- 1.9 BEM modifiers (--modifier)
  - Detect: missing -- modifiers; Fix: apply BEM
- 1.10 File names (snake_case)
  - Detect: non-snake file names; Fix: rename file
- 1.11 Class names (PascalCase)
  - Detect: non-Pascal classes; Fix: rename

Headers (2.x)
- 2.1 File header (3 lines)
  - Detect: missing/invalid 3-line header; Fix: add per standards
- 2.2 No metadata in header
  - Detect: extra fields in header; Fix: remove metadata
- 2.3 Section headers (numbered)
  - Detect: missing numbered section headers when applicable; Fix: add

Comments (3.x)
- 3.1 Comment density (≤5/10 lines)
  - Detect: >5 comments per 10 lines; Fix: remove narration
- 3.2 Comments explain "why"
  - Detect: “what” narration; Fix: explain intent/why
- 3.3 No commented-out code
  - Detect: large commented code blocks; Fix: delete or move to docs
- 3.4 TODO with context
  - Detect: TODO without owner/context; Fix: add context or remove

Initialization (4.x)
- 4.1 Webflow init pattern
  - Detect: missing pattern; Fix: add push/DOMContentLoaded/else template
- 4.2 IIFE wrapper
  - Detect: missing IIFE for scoping; Fix: wrap
- 4.3 No direct DOMContentLoaded
  - Detect: direct listeners used instead of pattern; Fix: migrate to pattern
- 4.4 No jQuery ready
  - Detect: $(document).ready usage; Fix: migrate
- 4.5 No window.onload
  - Detect: window.onload usage; Fix: migrate

Platform Constraints (5.x)
- 5.1 No ID selectors in collections
  - Detect: #id inside .w-dyn-*; Fix: use class or data-attr
- 5.2 Collection timing awareness
  - Detect: assumes immediate render; Fix: handle async rendering
- 5.3 Event delegation
  - Detect: direct listeners on dynamic items; Fix: delegate from parent
- 5.4 No function.name reliance
  - Detect: code relying on function.name; Fix: explicit mapping
- 5.5 Collection limit awareness
  - Detect: logic breaking with pagination/limits; Fix: guard for limits

Integrations (6.x)
- 6.1 Motion.dev availability check
  - Detect: using Motion without guard; Fix: if (window.Motion) ...
- 6.2 Lenis availability check
  - Detect: using Lenis without guard; Fix: if (window.Lenis) ...
- 6.3 Third-party defensive loading
  - Detect: assuming globals; Fix: null-checks and fallbacks

Accessibility (7.x)
- 7.1 ARIA attributes
  - Detect: interactive elements missing ARIA; Fix: add aria-*
- 7.2 Focus management
  - Detect: modals/menus without focus trap/return; Fix: implement
- 7.3 Keyboard navigation
  - Detect: Enter/Escape/Arrow handling missing; Fix: add handlers

Error Handling (8.x)
- 8.1 Try-catch for APIs
  - Detect: external ops without try-catch; Fix: wrap and log
- 8.2 Graceful degradation
  - Detect: no fallback when feature/library absent; Fix: add fallback
- 8.3 Console errors
  - Detect: console.error in shipped code or unhandled errors; Fix: handle and remove noisy logs

### Step 4: Report Generation

Collect all violations and generate structured report:

**Compliance Score Calculation**:
```
Score = 100% - (error_count × 10%) - (warning_count × 3%) - (info_count × 1%)
Minimum score: 0%
```

**Report Sections**:
1. Summary (file info, compliance score, violation counts)
2. Errors (P0, P1 - must fix)
3. Warnings (P2 - should fix)
4. Info (P3 - best practices)
5. Recommendations
6. Next Steps

**Output Generation**:
- Format according to requested output type (detailed/summary/JSON)
- Include line numbers and code snippets
- Provide fix suggestions with examples
- Reference knowledge base documents

.

## 6. 🔍 Examples

### Example 1: Validate Single File (Standard Level)

**Input**:
```
Validate /Users/username/project/src/modal/modal_welcome.js
Use standard validation level
```

**Process**:
1. Load validation rules (P0, P1, P2 for standard level)
2. Read modal_welcome.js and parse code
3. Check initialization pattern → ✅ PASS
4. Check naming conventions → ✅ PASS (all snake_case)
5. Check file header → ✅ PASS (3-line format correct)
6. Check platform constraints → ✅ PASS (event delegation used)
7. Check ARIA attributes → ⚠️ WARNING (missing aria-describedby on line 156)
8. Check Motion.dev availability → ✅ PASS (has availability check)
9. Calculate compliance: 97% (1 warning)
10. Generate detailed report

**Output**:
```markdown
# Validation Report: modal_welcome.js

**Compliance Score**: 97%

## Summary
- Errors: 0
- Warnings: 1
- Info: 0

## Warnings

### WARNING: Missing ARIA Attribute (Rule 7.1)
**Line**: 156
**Fix**: Add aria-describedby attribute
...
```

**Explanation**:
This demonstrates standard validation catching an accessibility issue while confirming the file follows all critical patterns correctly.

### Example 2: Quick Validation of Multiple Files

**Input**:
```
Validate all files in src/contact/*.js
Use quick validation level
Generate summary report
```

**Process**:
1. Glob pattern matches 3 files: form_handler.js, form_submit.js, form_validation.js
2. Run quick validation on each (headers, init, naming, comments)
3. Aggregate results across all 3 files
4. Generate summary report

**Output**:
```markdown
# Validation Summary: 3 files

**Overall Compliance**: 88%

| File | Score | Errors | Warnings | Info |
|------|-------|--------|----------|------|
| form_handler.js | 95% | 0 | 1 | 2 |
| form_submit.js | 100% | 0 | 0 | 0 |
| form_validation.js | 71% | 2 | 3 | 1 |

## Critical Issues
- form_validation.js: Missing initialization pattern (Rule 4.1)
- form_validation.js: camelCase function name (Rule 1.1)
```

**Explanation**:
Quick validation across multiple files provides fast feedback on critical issues without deep analysis.

### Example 3: Comprehensive Validation with JSON Output

**Input**:
```
Validate src/video/video_autoplay_fallback.js
Use comprehensive validation level
Output JSON format
```

**Process**:
1. Load all validation rules (P0, P1, P2, P3)
2. Perform deep analysis including comment quality and error handling
3. Generate machine-readable JSON output

**Output**:
```json
{
  "file": "src/video/video_autoplay_fallback.js",
  "date": "2025-10-18T10:30:00Z",
  "level": "comprehensive",
  "compliance_score": 92,
  "summary": {
    "errors": 0,
    "warnings": 2,
    "info": 1
  },
  "violations": [
    {
      "severity": "WARNING",
      "category": "Commenting",
      "rule": "3.2",
      "line": 45,
      "message": "Comment narrates code instead of explaining intent",
      "current": "// Set fallback to true",
      "suggestion": "// Fallback required when autoplay blocked by browser policy"
    },
    {
      "severity": "WARNING",
      "category": "Error Handling",
      "rule": "8.1",
      "line": 78,
      "message": "External API call lacks try-catch",
      "fix": "Wrap video.play() in try-catch for autoplay failures"
    },
    {
      "severity": "INFO",
      "category": "Best Practices",
      "rule": "Performance",
      "line": 23,
      "message": "Consider adding willChange for smoother animations"
    }
  ]
}
```

**Explanation**:
Comprehensive validation with JSON output enables integration with CI/CD pipelines and automated quality gates

## 7. 📚 Embedded Rules & Notes

- No External References: This skill is self-contained. The rules catalog is embedded in this document (see Section "Validation Level to Rules Mapping").
- For deeper context, cite knowledge/code_standards.md, knowledge/initialization_pattern.md, knowledge/webflow_platform_constraints.md.
- Optional: Maintain a short "Common Violations" list here sourced from real findings as the project evolves.

## 8. 🧾 Quick Reference

### Common Usage Patterns

#### Pattern 1: Pre-Commit Validation
```
Validate all changed files before committing:
- Run quick validation on staged files
- Fix any ERROR violations
- Commit only if compliance score > 90%
```

#### Pattern 2: Generated Code Verification
```
After using Webflow Component Generator:
1. Generate component with generator skill
2. Run standard validation on generated file
3. Verify 100% compliance (no errors/warnings)
4. Deploy with confidence
```

#### Pattern 3: Codebase Audit
```
Audit entire codebase for quality:
- Run comprehensive validation on src/**/*.js
- Generate summary report
- Prioritize fixes by severity
- Track compliance score over time
```

### Validation Level Selection Guide

**Use Quick** when:
- Pre-commit checks (speed matters)
- CI/CD pipeline validation
- Validating many files (bulk scan)
- Only care about blocking issues

**Use Standard** when:
- Code review preparation
- Pull request validation
- Generated code verification
- Balanced speed and coverage

**Use Comprehensive** when:
- Preparing for production deployment
- Quarterly code quality audits
- Learning code standards
- Maximum assurance needed

### Validation Checklist

Before finalizing code, verify:
- [ ] Compliance score ≥ 90% (production ready)
- [ ] Zero P0/P1 errors (no blocking issues)
- [ ] P2 warnings addressed or justified
- [ ] File follows initialization pattern
- [ ] All naming conventions correct
- [ ] Platform constraints respected

### Troubleshooting

**Issue**: "Cannot find initialization pattern"
**Solution**: Add the required Webflow.push pattern at the end of your file. See `knowledge/initialization_pattern.md:17-34` for exact template.

**Issue**: "Too many naming violations"
**Solution**: Use search/replace to convert camelCase to snake_case systematically. Check `knowledge/code_standards.md:7-24` for complete naming table.

**Issue**: "Comment density too high"
**Solution**: Remove comments that narrate what code does. Keep only comments explaining WHY decisions were made. Target: ≤ 5 comments per 10 lines.

**Issue**: "Missing ARIA attributes on modal"
**Solution**: Reference `specs/004-claude-skills/analysis/patterns.md` Accessibility Patterns section for complete ARIA implementation examples from existing modals

## 9. ⚙️ Edge Case Handling

This section provides guidance for special scenarios and edge cases encountered during validation.

### When to Skip Validation

**Skip validation entirely for**:
- **Minified files**: Files with `.min.js` extension or single-line code
- **node_modules**: Third-party dependencies (not project code)
- **Vendor libraries**: CDN-loaded libraries in `/vendor` or `/lib` directories
- **Build artifacts**: Files in `/dist`, `/build`, or `.cache` directories
- **Explicitly excluded**: Files with `// @no-validate` comment in first 10 lines

**Example**:
```javascript
// @no-validate - Third-party integration code
// This file follows external library conventions
```

#### Mixed Naming Conventions

**Scenario**: File contains both camelCase and snake_case
**Resolution**:
1. Identify which convention is dominant (count occurrences)
2. Flag minority convention as violations
3. If 50/50 split, flag all camelCase as violations (project standard is snake_case)
4. Note in report: "File uses mixed naming conventions - recommend converting all to snake_case"

**Exception**: External library method calls (e.g., `Motion.animate()`) are not violations

#### Partially Compliant Files

**Scenario**: File meets some but not all requirements
**Resolution**:
1. Generate report showing all violations
2. Calculate compliance score normally
3. Prioritize fixes by severity: ERROR → WARNING → INFO
4. Document which patterns are correct to avoid over-fixing

#### Third-Party Code Integration

**Scenario**: File integrates third-party library with different conventions
**Resolution**:
1. **Library API calls**: Exempt from naming rules (e.g., `gsap.to()` is fine)
2. **Wrapper functions**: Must follow project conventions
3. **Callbacks to library**: Follow library's convention if required by API
4. Flag only project code, not library usage

**Example**:
```javascript
// ✅ CORRECT - Library call exempt, wrapper follows project standard
function animate_hero() {
  gsap.to(element, { duration: 1 }); // gsap is library - OK
}
```

#### Collection Context Ambiguity

**Scenario**: Unclear if code handles Webflow collections
**Resolution**:
1. Search for explicit indicators: `.w-dyn-item`, `.w-dyn-list`, "collection" in comments
2. If found → apply collection rules strictly
3. If not found but code selects multiple items → suggest collection-safe patterns as INFO
4. If general utility function → skip collection-specific rules

#### Incomplete Initialization Pattern

**Scenario**: File has Webflow.push but missing one branch
**Resolution**:
1. Flag as ERROR (pattern must be complete)
2. Specify which branch is missing
3. Provide full correct pattern in fix suggestion
4. Common issue: Missing final `else` branch

#### Comment Quality Judgment Calls

**Scenario**: Borderline comment - could be "what" or "why"
**Resolution**:
1. If comment adds context not obvious from code → PASS
2. If comment merely restates code → WARNING
3. When uncertain, err on the side of not flagging (avoid false positives)
4. Focus on clear violations: "// Set x to 5" before `x = 5`

**Examples**:
```javascript
// ⚠️ BORDERLINE - Could go either way
// Convert to cents
const price_cents = price * 100;

// ✅ CLEARLY GOOD - Explains why
// Stripe requires amounts in cents to avoid float errors
const price_cents = price * 100;

// ❌ CLEARLY BAD - Restates code
// Multiply price by 100
const price_cents = price * 100;
```

#### Multiple Files with Shared Code

**Scenario**: Validating multiple files that share utilities
**Resolution**:
1. Validate each file independently
2. If utility file has violations, flag them only once
3. In multi-file summary, consolidate duplicate issues
4. Note: "Issue appears in 3 files - fix utility function"

#### Generated vs Hand-Written Code

**Scenario**: Code generated by Webflow Component Generator or similar tool
**Resolution**:
1. Apply same standards (generated code should be compliant)
2. If generator produces non-compliant code → high-priority fix to generator
3. Flag violations normally but note in report if code is generated
4. Generated code should achieve 100% compliance

#### Conflicts Between Rules

**Scenario**: Following one rule appears to violate another
**Resolution**:
1. **Priority**: ERROR rules override WARNING rules
2. **Specificity**: More specific rule takes precedence
3. **Document**: If genuine conflict found, document and report to skill maintainer
4. **Common case**: No actual conflicts exist in rule set (designed to be compatible)

#### Legacy Code Gradual Migration

**Scenario**: Large codebase with legacy code being migrated to standards
**Resolution**:
1. Run validation at appropriate level (likely Quick for legacy)
2. Prioritize fixing ERROR violations first
3. Create migration plan based on WARNING count
4. Track compliance score over time
5. Set incremental targets: 70% → 80% → 90% → 95%

## 10. 📊 Performance & Limitations

**Performance**:
- Quick validation: Fast - minimal rule set (18 rules), simple pattern matching
- Standard validation: Moderate - expanded rule set (31 rules), context-aware checks
- Comprehensive validation: Thorough - complete rule set (37 rules), deep analysis
- Bulk validation: Processes multiple files sequentially
- Performance varies based on file size and complexity

**Limitations**:
- JavaScript only (does not validate HTML, CSS, or other languages)
- Pattern-based detection (may not catch all semantic issues)
- Does not execute code (cannot detect runtime errors)
- Platform constraints based on documented limits (may not reflect latest Webflow changes)
- Comment quality analysis is heuristic-based (may flag some valid comments)

**Token Budget**:
- This SKILL.md includes the embedded rules catalog and examples.
- Use summary or JSON output for large scans to keep responses concise.

## 11. 📈 Success Metrics

**Accuracy Targets**:
- 100% detection of P0 errors (initialization, naming)
- 95%+ detection of P1 errors (platform constraints)
- 90%+ detection of P2 warnings (comments, accessibility)

**Value Delivery**:
- 90%+ reduction in double-initialization bugs reaching production
- 85%+ reduction in naming violations reaching production
- 70%+ reduction in code review time for standards compliance
- 50%+ improvement in overall code consistency