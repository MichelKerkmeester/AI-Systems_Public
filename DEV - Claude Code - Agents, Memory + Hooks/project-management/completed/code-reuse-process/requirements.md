# Code Reuse Process Requirements

## Overview
Implement a strict 5-step code reuse workflow that enforces systematic validation and prevents duplicate code creation.

## Functional Requirements

### Core Workflow
1. **5-Step Compliance Process**
   - Step 1: Read requirements and confirm understanding
   - Step 2: Analyze current system for existing implementations
   - Step 3: Create implementation plan with reuse focus
   - Step 4: Provide technical details referencing existing code
   - Step 5: Finalize deliverables with testing strategies

### Enforcement Rules
1. **Search Before Coding**
   - Use Grep/Glob/Task tools to find existing implementations
   - Document search results before creating new code

2. **Justification System**
   - Exhaustive analysis required before creating new files
   - Must explain why existing files cannot be extended
   - Reference specific files and line numbers

3. **Pattern Compliance**
   - Follow patterns.json conventions
   - Extend existing services and components
   - Consolidate duplicate functionality

### Integration Requirements
1. **Hook System Compatibility**
   - Work with existing quality, security, and memory hooks
   - Trigger Sequential Thinking for complex tasks
   - Capture reuse patterns in memory system

2. **Memory Pattern Capture**
   - REUSABLE_COMPONENT: When creating shareable code
   - EXISTING_SOLUTION: When finding reusable code
   - REFACTOR_OPPORTUNITY: When spotting duplication

3. **Production Checklist Updates**
   - Verify no duplicate functionality
   - Confirm existing code searched and reused
   - Validate pattern compliance
   - Justify any new files created

## Non-Functional Requirements

### Performance
- Code search must complete within 5 seconds
- Workflow should not slow down development significantly

### Compatibility
- Preserve all existing system functionality
- Allow exceptions for hook-generated files, MCP outputs, tests
- Support external analysis tools (Gemini, etc.)

### Usability
- Clear error messages when rules are violated
- Helpful suggestions for finding reusable code
- Integration with existing `/logic` command structure