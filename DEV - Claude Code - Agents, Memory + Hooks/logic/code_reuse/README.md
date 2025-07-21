# Code Reuse Analysis Engine

The Code Reuse Analysis Engine enforces DRY (Don't Repeat Yourself) principles and prevents unnecessary file creation by analyzing existing code for reuse potential.

## Components

### 1. ReuseAnalyzer (`reuse_analyzer.py`)
Searches for existing components that match requirements and provides reuse recommendations.

**Key Features:**
- Searches codebase for matching components
- Calculates reuse scores based on:
  - Functionality match (50% weight)
  - Interface compatibility (30% weight)
  - Modification effort (20% weight)
- Provides specific extension recommendations
- Generates detailed analysis summaries

**Usage:**
```python
from code_reuse import ReuseAnalyzer

analyzer = ReuseAnalyzer()
requirements = {
    'functionality': 'modal dialog with animations',
    'type': 'modal',
    'interface': {
        'methods': ['open', 'close'],
        'events': ['onOpen', 'onClose']
    }
}

score = analyzer.analyze_reuse_potential(requirements)
if score.best_match and score.best_match.match_score > 60:
    print(f"Extend {score.best_match.file_path} instead of creating new file")
```

### 2. ComplianceValidator (`compliance_validator.py`)
Validates that code follows established patterns and principles from CLAUDE.md, patterns.json, and constraints.json.

**Validation Categories:**
- **Patterns**: Initialization, element safety, selectors
- **Constraints**: File size, console.log, jQuery usage, CSS units
- **Principles**: DRY, KISS, file creation rules
- **Security**: API keys, XSS vulnerabilities
- **Performance**: DOM manipulation, file size budgets

**Usage:**
```python
from code_reuse import ComplianceValidator

validator = ComplianceValidator()
result = validator.validate_code(
    code_content,
    file_path,
    {'is_new_file': True}
)

if not result.is_compliant:
    print(f"Code failed validation: {result.summary}")
```

### 3. JustificationSystem (`justification_system.py`)
Manages justifications for new file creation with full audit trail.

**Features:**
- Requires detailed justification for new files
- Tracks reuse attempts and why they failed
- Maintains audit log of all decisions
- Supports approval/rejection workflow
- Generates reports on file creation patterns

**Usage:**
```python
from code_reuse import JustificationSystem

justifier = JustificationSystem()
justification = justifier.create_justification(
    file_path=Path('src/new-component.js'),
    purpose="Create specialized animation controller",
    functionality="Manages complex timeline animations",
    why_needed="Existing animation utilities don't support timeline control",
    reuse_analysis=reuse_score
)

# Validate and enforce
allowed, message = justifier.enforce_justification(file_path)
if not allowed:
    raise Exception(f"File creation blocked: {message}")
```

## Integration with Hooks

The code reuse system can be integrated with existing hooks to automatically:

1. **Before file creation**: Run reuse analysis
2. **During TodoWrite**: Check for similar components
3. **In quality hooks**: Validate compliance
4. **In Write/MultiEdit tools**: Enforce justification

## Scoring System

### Reuse Score Interpretation
- **80-100%**: Strong match - extend this component
- **60-79%**: Good match - consider extending with modifications
- **40-59%**: Partial match - significant modifications needed
- **0-39%**: Weak match - new component may be justified

### Compliance Score
- **100**: Perfect compliance
- **90-99**: Minor issues (info messages only)
- **70-89**: Warnings that should be addressed
- **<70**: Errors that must be fixed

## Best Practices

1. **Always run reuse analysis first** before creating any new file
2. **Document why existing code won't work** if creating new file
3. **Follow extension recommendations** when match score > 60%
4. **Fix all compliance errors** before committing code
5. **Keep justifications detailed** for future reference

## Reports and Auditing

Generate reports on file creation patterns:

```python
report = justifier.generate_justification_report()
print(f"Approval rate: {report['approved']/report['total_justifications']*100:.1f}%")
print(f"Common rejections: {report['common_rejection_reasons']}")
```

View audit trail for specific files:

```python
audit_trail = justifier.get_audit_trail(file_path)
for entry in audit_trail:
    print(f"{entry['timestamp']}: {entry['action']} - {entry['status']}")
```