# Code Reuse Process - Project Structure

## Overview

This project implements a comprehensive code reuse system for Claude Code that automatically enforces the 5-step workflow from CLAUDE.md.

## Directory Structure

```
code-reuse-process/
├── README.md                          # Project overview
├── project-structure.md               # This file
├── code-reuse-process-proposal.md     # Original specification
├── design.md                          # Technical design document
├── requirements.md                    # Detailed requirements
├── rollback-plan.md                   # Rollback procedures
├── test-plan.md                       # Testing strategy
└── tests/
    ├── results/
    │   └── code-reuse-implementation-summary.md  # Test results
    ├── test_automated.py              # Automated test suite
    ├── test_5step_workflow.py         # Workflow validation tests
    ├── test_real_scenario.py          # Real-world scenario tests
    ├── test_integration.py            # Integration tests
    ├── test_reuse_system.py           # System tests
    └── test_simple.py                 # Basic functionality tests
```

## Implementation Location

The actual implementation code resides in:
```
.claude/logic/code_reuse/
├── __init__.py                        # Package initialization
├── README.md                          # Module documentation
├── reuse_analyzer.py                  # Core analysis engine
├── compliance_validator.py            # Pattern enforcement
├── justification_system.py            # File creation justification
├── similarity_detector.py             # AST-based similarity detection
├── pattern_matcher.py                 # Pattern matching logic
├── consolidation_analyzer.py          # Code consolidation tools
├── state_manager.py                   # State management
└── justifications/                    # Justification storage
```

## Hook Integration

The system is enforced through:
```
.claude/logic/hooks/code_reuse/
└── code-reuse-validation-hook.py      # Main enforcement hook
```

Integrated into:
- UserPromptSubmit pipeline
- PostToolUse pipeline (Write, Edit, MultiEdit)

## Test Results

All test results are saved as markdown summaries in `tests/results/`:
- **Success Rate**: 92.3% (12/13 tests passed)
- **Automation**: Fully automated via hooks
- **Performance**: <100ms average execution time

## Key Features

1. **Automatic Enforcement**: No manual commands required
2. **Real-time Validation**: Blocks unjustified file creation
3. **Pattern Learning**: Captures reusable components
4. **Smart Exceptions**: Allows test/doc files
5. **Memory Integration**: Stores patterns for future searches

## Status

✅ **Production Ready** - The system is fully implemented, tested, and actively enforcing code reuse principles.