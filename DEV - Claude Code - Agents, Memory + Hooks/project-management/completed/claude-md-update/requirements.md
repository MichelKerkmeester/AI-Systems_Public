# CLAUDE.md Update Requirements

## Overview
Update CLAUDE.md to align with current system implementations while maintaining the exact structure and section numbering as requested.

## Critical Constraints
1. **KEEP STRUCTURE 1:1** - Maintain exact section structure with START HERE and 5 steps
2. **DON'T BREAK EXISTING SYSTEMS** - Must work with code-reuse and memory-automation-v2
3. **ALIGN WITH CURRENT REALITY** - Update to match actual hooks, commands, and workflows

## Specific Requirements

### START HERE Section (Keep 5 Steps)
1. **Step 1: READ REQUIREMENTS**
   - Keep as compliance-focused step
   - Update to reflect current code reuse enforcement system
   - Reference actual hooks that enforce this (code-reuse-validation-hook.py)

2. **Step 2: ANALYZE CURRENT SYSTEM**  
   - Update to use current search tools and reuse analyzer
   - Must trigger memory search (enforced by memory-context-hook-graphiti.py)

3. **Step 3: CREATE IMPLEMENTATION PLAN**
   - Must create spec for EVERY initial request (not just complex ones)
   - Reference spec-generation-hook.py automation

4. **Step 4: PROVIDE TECHNICAL DETAILS**
   - Update to reference current pattern matching and validation

5. **Step 5: FINALIZE DELIVERABLES**
   - Include current test automation and completion flow

### Section 1: Quick Start
- **Lean Status Display**:
  - Only show if NOT working (everything else shows ✅)
  - Items: Memory, Agents, Required MCPs, Commands (list all)
  - Remove auto-display hook (doesn't work)
  - Enforce display through CLAUDE.md instructions only
  - Display only at conversation start, not in subsequent queries

### Section 2: Core Principles
- Keep as-is but verify technical constraints match current hooks

### Section 3: Task Management  
- **EVERY initial request must create a spec** (not just complex ones)
- Update spec-driven process to match current implementation:
  - Reference spec-generation-hook.py
  - Include actual folder structure from completed specs
  - Update workflow to match task-management-hook.py
  - Include code reuse requirements in every spec

### Section 4: Memory Operations
- Update to match memory-automation-v2 implementation
- Include actual capture patterns from hooks
- Reference enforcement by memory-context-hook-graphiti.py

### Section 5: Hook Automation Warnings
- Review all warnings for current relevance
- Update based on actual hook implementations
- Remove outdated warnings
- Add new warnings based on claude-md-update-hook.py findings

### New Addition: Self-Update Mechanism
- Create mechanism for CLAUDE.md to stay updated:
  - Hook that triggers on significant changes
  - Command to manually trigger update review
  - Integration with claude-md-update-hook.py
  - Track what sections need updates based on system changes

## Success Criteria
1. CLAUDE.md structure remains exactly the same (numbered sections, START HERE with 5 steps)
2. All content reflects current system reality
3. No conflicts with existing automation
4. Status display is lean and only shows at conversation start
5. Every initial request triggers spec creation
6. Self-update mechanism is implemented

## Testing Requirements
1. Verify all commands referenced actually exist
2. Confirm all hooks mentioned are active
3. Test spec creation triggers on initial requests
4. Validate status display behavior
5. Ensure memory operations are enforced
6. Test self-update mechanism