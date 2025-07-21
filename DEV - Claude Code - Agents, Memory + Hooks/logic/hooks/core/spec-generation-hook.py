#\!/usr/bin/env python3
"""
Spec Generation Hook - Automatic specification creation for complex features
Enforces code reuse analysis and structured planning
"""

import os
import json
import re
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# Hook metadata
HOOK_TYPE = "UserPromptSubmit"
PRIORITY = 5  # Run early to create specs before other hooks

def analyze_complexity(prompt: str) -> Tuple[int, Dict[str, int]]:
    """
    Calculate complexity score based on various factors
    Returns: (total_score, breakdown)
    """
    breakdown = {
        'keywords': 0,
        'steps': 0,
        'scope': 0,
        'integration': 0,
        'refactoring': 0
    }
    
    # Keywords indicating feature creation (2 points each)
    creation_keywords = ['implement', 'create', 'build', 'develop', 'add', 'feature', 'functionality']
    for keyword in creation_keywords:
        if keyword in prompt.lower():
            breakdown['keywords'] += 2
    
    # Multi-step indicators (1 point each)
    step_indicators = ['then', 'after', 'next', 'finally', 'also', 'and then', 'step']
    for indicator in step_indicators:
        if indicator in prompt.lower():
            breakdown['steps'] += 1
    
    # Scope indicators (3 points for system-wide)
    if any(word in prompt.lower() for word in ['system', 'global', 'entire', 'all', 'architecture']):
        breakdown['scope'] = 3
    elif any(word in prompt.lower() for word in ['module', 'component', 'section']):
        breakdown['scope'] = 2
    else:
        breakdown['scope'] = 1
    
    # Integration complexity (2 points)
    if any(word in prompt.lower() for word in ['integrate', 'connect', 'sync', 'api', 'webhook']):
        breakdown['integration'] = 2
    
    # Refactoring vs new code (1 point for refactoring, 3 for new)
    if any(word in prompt.lower() for word in ['refactor', 'improve', 'optimize', 'enhance']):
        breakdown['refactoring'] = 1
    elif any(word in prompt.lower() for word in ['new', 'from scratch', 'greenfield']):
        breakdown['refactoring'] = 3
    
    total = sum(breakdown.values())
    return total, breakdown

def extract_feature_name(prompt: str) -> str:
    """Extract a meaningful feature name from the prompt"""
    # Try to find quoted names first
    quoted = re.search(r'["\'](.*?)["\']', prompt)
    if quoted:
        return quoted.group(1).lower().replace(' ', '-')
    
    # Look for patterns like "implement X", "create Y"
    patterns = [
        r'implement\s+(?:a\s+)?(\w+(?:\s+\w+){0,2})',
        r'create\s+(?:a\s+)?(\w+(?:\s+\w+){0,2})',
        r'build\s+(?:a\s+)?(\w+(?:\s+\w+){0,2})',
        r'add\s+(?:a\s+)?(\w+(?:\s+\w+){0,2})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, prompt.lower())
        if match:
            return match.group(1).replace(' ', '-')
    
    # Fallback: use first few significant words
    words = prompt.lower().split()[:5]
    filtered = [w for w in words if len(w) > 3 and w not in ['that', 'this', 'with', 'from']]
    if filtered:
        return '-'.join(filtered[:3])
    
    return f"feature-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

def create_requirements_md(feature_name: str, prompt: str, complexity: Dict[str, int], is_code_reuse: bool) -> str:
    """Create requirements.md content"""
    content = f"""# Requirements: {feature_name}

## Overview
**Request Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Complexity Score:** {sum(complexity.values())} (Breakdown: {complexity})
**Type:** {'Code Reuse Implementation' if is_code_reuse else 'Standard Implementation'}

## Original Request
```
{prompt}
```

## Core Requirements
1. [TODO: Extract specific requirements from prompt]
2. [TODO: Define success criteria]
3. [TODO: Identify constraints]

"""
    
    if is_code_reuse:
        content += """## 🔄 MANDATORY Code Reuse Analysis

### Step 1: Compliance Confirmation
COMPLIANCE CONFIRMED: I will prioritize reuse over creation

### Step 2: Existing Code Search
**Search Commands to Execute:**
```bash
# Pattern search
grep -r "PATTERN" src/

# Component search  
glob "**/*component*.js"

# Similar functionality
grep -r "KEYWORDS" .claude/
```

**Files to Analyze:**
- [ ] src/C__components/ - Check for reusable components
- [ ] src/B__global/ - Check for global utilities
- [ ] src/D__services/ - Check for existing services

### Step 3: Reuse Opportunities
| Existing File | Can Extend? | Reason |
|--------------|-------------|---------|
| [TODO] | Yes/No | [Justification] |

### Step 4: New File Justification
**IF new files needed, explain why existing cannot be extended:**
1. [File path] - [Why it cannot be extended]

### Step 5: Pattern Compliance
- [ ] Follows patterns.json conventions
- [ ] Uses established naming patterns
- [ ] Extends existing services where possible
"""
    
    content += """
## Dependencies
- External libraries: [TODO]
- Internal modules: [TODO]
- Platform constraints: [TODO]

## Acceptance Criteria
- [ ] All tests passing
- [ ] No console.log statements
- [ ] Performance within budgets
- [ ] Security scan clean
"""
    
    if is_code_reuse:
        content += """- [ ] Code reuse analysis complete
- [ ] Existing components leveraged
- [ ] No unnecessary duplication
"""
    
    return content

def create_design_md(feature_name: str, is_code_reuse: bool) -> str:
    """Create design.md content"""
    content = f"""# Design: {feature_name}

## Architecture Overview
[TODO: High-level design description]

"""
    
    if is_code_reuse:
        content += """## 🔄 Code Reuse Architecture

### Components to Reuse
| Component | Location | Modifications Needed |
|-----------|----------|---------------------|
| [TODO] | src/path/file.js | [Changes] |

### Extensions to Existing Code
```javascript
// File: src/existing/file.js
// Extension: Add new method to existing class/module
```

### New Components (Justified)
Only if absolutely necessary after reuse analysis:
"""
    
    content += """
## Technical Design

### Data Flow
1. [TODO: Step by step data flow]

### API Design
```javascript
// Interface definitions
```

### State Management
[TODO: How state will be managed]

## Implementation Plan
1. [ ] Phase 1: [Description]
2. [ ] Phase 2: [Description]
3. [ ] Phase 3: [Description]

## Performance Considerations
- Load time impact: [Estimate]
- Memory usage: [Estimate]
- Bundle size: [Estimate]

## Security Considerations
- [ ] No hardcoded credentials
- [ ] Input validation
- [ ] XSS prevention
"""
    
    return content

def create_test_plan_md(feature_name: str, is_code_reuse: bool) -> str:
    """Create test-plan.md content"""
    content = f"""# Test Plan: {feature_name}

## Test Strategy
- Unit tests: [Coverage target]
- Integration tests: [Scope]
- E2E tests: [Critical paths]

"""
    
    if is_code_reuse:
        content += """## 🔄 Code Reuse Verification

### Reuse Compliance Tests
1. **No Duplication Test**
   - Verify no duplicate functionality created
   - Check component catalog usage

2. **Pattern Compliance Test**
   - Verify patterns.json adherence
   - Check naming conventions

3. **Extension Verification**
   - Confirm existing code properly extended
   - Verify no breaking changes

"""
    
    content += """## Test Cases

### Unit Tests
```javascript
describe('{feature_name}', () => {
  test('should [behavior]', () => {
    // Test implementation
  });
});
```

### Integration Tests
1. [ ] Test with existing components
2. [ ] Test data flow
3. [ ] Test error handling

### Manual Testing
1. [ ] Visual regression
2. [ ] Cross-browser testing
3. [ ] Performance testing

## Test Data
- Valid inputs: [Examples]
- Invalid inputs: [Examples]
- Edge cases: [Examples]

## Success Criteria
- [ ] All automated tests pass
- [ ] Manual testing complete
- [ ] No regressions in existing functionality
"""
    
    if is_code_reuse:
        content += """- [ ] Code reuse verified
- [ ] No unnecessary duplication
"""
    
    return content

def create_rollback_md(feature_name: str, is_code_reuse: bool) -> str:
    """Create rollback-plan.md content"""
    content = f"""# Rollback Plan: {feature_name}

## Risk Assessment
- **Impact Level:** [Low/Medium/High]
- **Affected Systems:** [List]
- **User Impact:** [Description]

"""
    
    if is_code_reuse:
        content += """## 🔄 Reusable Component Preservation

### Components to Preserve
These components should be preserved even during rollback:
1. [Component] - Used by [other features]
2. [Utility] - Shared dependency

### Safe Rollback Strategy
- Preserve shared components
- Only remove feature-specific code
- Maintain backward compatibility

"""
    
    content += """## Rollback Steps

### Immediate Rollback (< 1 hour)
1. [ ] Git revert to commit: [SHA]
2. [ ] Clear CDN cache
3. [ ] Verify rollback in staging
4. [ ] Deploy to production

### Gradual Rollback (Feature flags)
1. [ ] Disable feature flag: [flag_name]
2. [ ] Monitor for 24 hours
3. [ ] Remove code in next release

## Verification Steps
1. [ ] All tests pass on previous version
2. [ ] No 404s or console errors
3. [ ] Performance metrics restored
4. [ ] User flows working

## Communication Plan
- [ ] Notify team via Slack
- [ ] Update status page if needed
- [ ] Document lessons learned

## Post-Rollback Actions
1. [ ] Root cause analysis
2. [ ] Update test coverage
3. [ ] Improve deployment process
"""
    
    return content

def create_spec_folder(feature_name: str, prompt: str, complexity: Dict[str, int], is_code_reuse: bool) -> str:
    """Create the spec folder structure and return the path"""
    base_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/project-management/specs"
    
    if is_code_reuse:
        spec_path = os.path.join(base_path, "code-reuse", feature_name)
    else:
        spec_path = os.path.join(base_path, feature_name)
    
    # Create directories
    os.makedirs(spec_path, exist_ok=True)
    os.makedirs(os.path.join(spec_path, "tests"), exist_ok=True)
    
    # Create files
    files = {
        "requirements.md": create_requirements_md(feature_name, prompt, complexity, is_code_reuse),
        "design.md": create_design_md(feature_name, is_code_reuse),
        "test-plan.md": create_test_plan_md(feature_name, is_code_reuse),
        "rollback-plan.md": create_rollback_md(feature_name, is_code_reuse)
    }
    
    for filename, content in files.items():
        filepath = os.path.join(spec_path, filename)
        with open(filepath, 'w') as f:
            f.write(content)
    
    # Create a status file
    status = {
        "created": datetime.now().isoformat(),
        "feature_name": feature_name,
        "complexity_score": sum(complexity.values()),
        "complexity_breakdown": complexity,
        "is_code_reuse": is_code_reuse,
        "status": "spec",
        "original_prompt": prompt[:500] + "..." if len(prompt) > 500 else prompt
    }
    
    with open(os.path.join(spec_path, "status.json"), 'w') as f:
        json.dump(status, f, indent=2)
    
    return spec_path

def format_user_instructions(feature_name: str, spec_path: str, complexity_score: int, is_code_reuse: bool) -> str:
    """Format instructions for the user"""
    instructions = f"""
📋 **SPEC CREATED**: Complex feature detected (score: {complexity_score})

**Feature:** `{feature_name}`
**Location:** `{spec_path}`

"""
    
    if is_code_reuse:
        instructions += """🔄 **CODE REUSE REQUIRED** - Follow the 5-step process:

1. **READ**: Review requirements.md and confirm compliance
2. **ANALYZE**: Search existing code (documented in requirements.md)
3. **PLAN**: Update design.md with reuse strategy
4. **IMPLEMENT**: Code changes referencing existing files
5. **FINALIZE**: Complete with test results

**Next Steps:**
```bash
# 1. Search for existing code
grep -r "relevant_pattern" src/
glob "**/*component*.js"

# 2. Review spec files
cat "{spec_path}/requirements.md"
cat "{spec_path}/design.md"

# 3. Begin implementation following the spec
```

**Remember:** Every new file requires exhaustive justification\!
""".format(spec_path=spec_path)
    else:
        instructions += """**Next Steps:**
1. Review the generated spec files
2. Complete the [TODO] sections
3. Begin implementation following the plan
4. Move to active/ when starting work
5. Move to completed/ with summary when done

**Quick Review:**
```bash
cat "{spec_path}/requirements.md"
cat "{spec_path}/design.md"
```
""".format(spec_path=spec_path)
    
    return instructions

def process_prompt(prompt: str, context: Optional[Dict] = None) -> Optional[str]:
    """Main hook function"""
    # Skip if prompt is too short or is a command
    if len(prompt) < 20 or prompt.startswith('/'):
        return None
    
    # Calculate complexity
    complexity_score, complexity_breakdown = analyze_complexity(prompt)
    
    # Check if this is a code reuse scenario
    code_reuse_keywords = ['refactor', 'consolidate', 'duplicate', 'reuse', 'existing', 'merge']
    is_code_reuse = any(keyword in prompt.lower() for keyword in code_reuse_keywords)
    
    # Boost score for code reuse scenarios to ensure spec creation
    if is_code_reuse and complexity_score < 6:
        complexity_score = 6
        complexity_breakdown['refactoring'] += 3
    
    # Only create spec if complexity >= 6
    if complexity_score < 6:
        return None
    
    # Extract feature name
    feature_name = extract_feature_name(prompt)
    
    # Create spec folder
    try:
        spec_path = create_spec_folder(feature_name, prompt, complexity_breakdown, is_code_reuse)
        instructions = format_user_instructions(feature_name, spec_path, complexity_score, is_code_reuse)
        
        # Log the spec creation
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "feature_name": feature_name,
            "complexity_score": complexity_score,
            "is_code_reuse": is_code_reuse,
            "spec_path": spec_path
        }
        
        log_path = "/Users/michel_kerkmeester/AI & Dev/Websites/anobel.nl/.claude/logic/hooks/spec-generation.log"
        with open(log_path, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        return instructions
        
    except Exception as e:
        return f"⚠️ **Spec Generation Error**: {str(e)}\n\nProceed with manual planning for this complex feature."

# Hook entry point
def hook(prompt: str, **kwargs) -> Optional[str]:
    """Hook entry point for the system"""
    return process_prompt(prompt, kwargs.get('context'))
EOF < /dev/null