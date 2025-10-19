---
name: code-implementer
description: Build features incrementally using 3-step workflow (Understand → Build → Polish). Implements from specs or plans with continuous testing, incremental delivery, and pragmatic approach. Creates implementation.md documentation. Use for feature development, coding from specifications, and delivering production-ready code.
---

# Code Implementer

Feature development through pragmatic, incremental implementation - understand requirements, build iteratively, polish for production.

## When to Use This Skill

**Use this skill when**:
- Implementing features from specifications
- Building from detailed plans
- Converting designs to code
- Developing new functionality
- Creating production-ready code
- Need implementation documentation

**Do NOT use this skill for**:
- Creating specifications (use code_planner instead)
- Quick bug fixes (use code_debugger instead)
- Performance optimization (use code_performance_improver instead)
- Code validation (use code_pattern_validator instead)

## How It Works

This skill follows a pragmatic 3-step implementation workflow:

1. **Understand** - Grasp requirements and plan approach
2. **Build** - Implement incrementally with continuous testing
3. **Polish** - Refine, validate, and document

**Philosophy**: "Ship working code that solves real problems"

**Approach**: Incremental over big bang, pragmatic over perfect, working over elegant

**Output**: Working code + `implementation.md` documentation

## Inputs

### Required Inputs

**Request**:
- **Description**: What to build
- **Format**: Natural language or reference to spec/plan
- **Examples**:
  - "Implement user authentication as specified in /specs/auth-system/"
  - "Build the checkout flow from the plan"
  - "Create the dashboard components"

### Optional Inputs

**Environment** (staging link):
- **Type**: URL
- **Purpose**: Where to test implementation
- **Default**: Skip browser testing if empty
- **Example**: `https://staging.example.com`

**Scope** (files):
- **Type**: File paths or glob pattern
- **Purpose**: Which files to modify/create
- **Default**: All relevant project files
- **Examples**:
  - `src/auth/*.js`
  - `src/components/Dashboard.tsx`

**Target Folder**:
- **Type**: Directory path
- **Purpose**: Often points to plan/spec folder, also where implementation.md is written
- **Default**: Current directory or inferred from request
- **Example**: `/specs/auth-system/`

**Context**:
- **Type**: Text
- **Purpose**: Additional implementation details
- **Default**: Inferred from target plan/specification
- **Example**: "Use existing authentication hooks, follow component patterns"

## Knowledge References

**IMPORTANT**: All implementations MUST follow these project standards:

### Code Standards
**Location**: `knowledge/code_standards.md`
**Purpose**: Mandatory naming conventions and code quality rules

**Key Requirements**:
- **Naming**: `snake_case` for variables/functions, PascalCase for classes
- **File Headers**: 3-line format with component name only (no metadata)
- **Initialization**: Use `Webflow.push()` pattern with `else if` for DOMContentLoaded
- **Comments**: Max 5 per 10 lines, explain WHY not WHAT
- **Platform Markers**: Use `// WEBFLOW:`, `// MIYAGI:` prefixes for constraints

```javascript
// ───────────────────────────────────────────────────────────────
// COMPONENT: FORM VALIDATOR
// ───────────────────────────────────────────────────────────────

// Webflow.push initialization pattern
if (window.Webflow && window.Webflow.push) {
  window.Webflow.push(init_function);
} else if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init_function);
} else {
  init_function();
}
```

### Animation Strategy
**Location**: `knowledge/animation_strategy.md`
**Purpose**: Animation library selection and implementation patterns

**Decision Framework**:
1. **CSS First**: Use CSS transitions/keyframes for hover, focus, simple state changes
2. **Motion.dev Only**: Use for programmatic control, in-view triggers, coordinated sequences
3. **Never GSAP/Framer**: Keep single animation library

**Key Patterns**:
- Prefer `transform` and `opacity` (GPU-accelerated)
- Use `@media (prefers-reduced-motion: reduce)` for accessibility
- Motion.dev loaded globally: `window.Motion.animate()`, `window.Motion.inView()`
- Clean up `will-change` on `onComplete`

### Documentation Style
**Location**: `knowledge/document_style_guide.md`
**Purpose**: Standard format for all documentation including implementation.md

**Required Structure**:
- H1: `# Title - Descriptive Subtitle`
- H2: `## 1. 📄 Section Name` (numbered with emoji)
- H3: `### 1.1 Subsection` (decimal numbering)
- Section separators: Single `.` on own line
- Table of Contents with anchor links
- Concise, technical, actionable writing

**When Creating implementation.md**: Follow this format exactly (see references/documentation-templates.md for full template aligned with style guide)

---

## Workflow

### Step 1: Gather User Inputs

**Purpose**: Collect all necessary information before starting implementation

**IMPORTANT**: Before starting the implementation workflow, ask the user for the following inputs in a conversational way:

#### Required Inputs:

1. **Request/Feature Description** (REQUIRED):
   - Ask: "What feature would you like me to implement? Please describe what you want to build, or reference a spec/plan."
   - This is the main feature description that drives the implementation.

#### Optional Inputs (with smart defaults):

2. **Target Folder**:
   - Ask: "Which folder contains the plan or spec for this feature? (Leave empty to use current directory or infer from your request)"
   - Default: Current directory or inferred from request

3. **Environment/Staging Link**:
   - Ask: "Do you have a staging environment URL for testing? (Leave empty to skip browser testing)"
   - Default: Skip DevTools/browser testing if not provided

4. **Scope/Files**:
   - Ask: "Which files should I modify or create? (Leave empty to use all relevant project files)"
   - Default: All relevant project files

5. **Context**:
   - Ask: "Any additional implementation context? (Leave empty to infer from plan/spec)"
   - Default: Infer from target plan/specification

**After Collecting Inputs**:
- Confirm all inputs with the user
- Locate and review spec/plan documents
- Identify implementation scope

---

### Step 2: Understand

**Purpose**: Grasp what needs to be built before writing code

**Activities**:
1. **Review Specifications**
   - Read target folder plan/specification
   - Parse requirements and success criteria
   - Note constraints and dependencies
   - Identify existing patterns to follow

2. **Plan Technical Approach**
   - Choose technologies/libraries
   - Identify files to create/modify
   - Determine architecture/structure
   - Consider error handling
   - Plan testing strategy

3. **Set Up Environment**
   - Verify development environment
   - Install dependencies if needed
   - Configure staging link if provided
   - Prepare for testing

**Outputs**:
- Clear objectives understood
- Technical approach defined
- Success metrics identified
- Environment ready

**Validation**: `understand_requirements_and_approach`

---

### Step 3: Build

**Purpose**: Implement the feature incrementally with quality

**Iterative Approach**:
1. **Start with Core**: Build essential functionality first
2. **Add Incrementally**: Add features piece by piece
3. **Test Continuously**: Verify each piece works
4. **Keep Working**: Never leave code broken
5. **Refactor as Needed**: Improve structure when appropriate

**Milestones**:

**Milestone 1: Basic Functionality**
- Goal: Core feature working
- Deliverable: Happy path implemented
- Validation: Basic case works end-to-end

**Milestone 2: Complete Functionality**
- Goal: All features implemented
- Deliverable: All requirements met
- Validation: All user stories work

**Milestone 3: Production Ready**
- Goal: Polished and robust
- Deliverable: Error handling, edge cases covered
- Validation: Ready for deployment

**Quality Standards**:

**Code Quality**:
- Readable and maintainable
- Follows project conventions
- Properly structured
- Well-named variables/functions
- Appropriate comments

**Functionality**:
- Works as specified
- Handles edge cases
- Error handling robust
- Performance acceptable
- Security considered

**Testing**:
- Critical paths tested
- Edge cases covered
- Integration verified
- Manual testing completed
- No regressions introduced

**Implementation Techniques**:
- **TDD when helpful**: Write tests first for critical logic
- **Incremental commits**: Commit working code frequently
- **Feature flags**: Toggle new features on/off
- **Progressive enhancement**: Basic → Advanced features

**Outputs**:
- Working code that meets requirements
- Tests (if applicable)
- Inline documentation (comments)

**Validation**: `feature_complete_and_tested`

---

### Step 4: Polish

**Purpose**: Refine code for production readiness

**Activities**:

1. **Code Cleanup**
   - Remove debug code
   - Improve variable names
   - Refactor complex logic
   - Add missing comments
   - Format consistently

2. **Performance Check**
   - Test with realistic data volumes
   - Profile if performance-critical
   - Optimize bottlenecks
   - Verify acceptable load times

3. **Error Handling**
   - Add try-catch blocks
   - Handle edge cases
   - Validate user inputs
   - Provide helpful error messages
   - Log errors appropriately

4. **Edge Cases**
   - Test empty states
   - Test maximum limits
   - Test invalid inputs
   - Test error conditions
   - Test browser compatibility (if web)

5. **Create implementation.md**
   - Document what was built
   - List files modified/created
   - Describe technical approach
   - Document testing completed
   - Note deployment steps

**Validation Checklist**:
- [ ] Feature complete per requirements
- [ ] All tests passing
- [ ] No regressions in existing features
- [ ] Performance acceptable
- [ ] Error handling robust
- [ ] Edge cases handled
- [ ] Code follows standards
- [ ] Comments added where needed
- [ ] implementation.md created
- [ ] Ready for code review

**Outputs**:
- Production-ready code
- All tests passing
- implementation.md document
- Ready for deployment

**Validation**: `implementation_complete_and_documented`

---

## Incremental Delivery Milestones

### Milestone 1: Basic Functionality (30% complete)

**Goal**: Core feature working
**Timeline**: 30% of total time

**Deliverable**:
- Happy path implemented
- Basic UI/logic working
- Core functionality demonstrated

**Validation**:
- Can demo basic feature
- Main use case works
- No critical bugs

**Example** (E-commerce checkout):
- Cart displays items
- User can enter shipping address
- Basic form validation

---

### Milestone 2: Complete Functionality (70% complete)

**Goal**: All features implemented
**Timeline**: 70% of total time

**Deliverable**:
- All requirements met
- All user stories working
- Integration points connected

**Validation**:
- All test cases pass
- All features work as specified
- Integration tested

**Example** (E-commerce checkout):
- Payment processing works
- Order confirmation sent
- Inventory updated
- Analytics tracked

---

### Milestone 3: Production Ready (100% complete)

**Goal**: Polished and robust
**Timeline**: 100% of total time

**Deliverable**:
- Error handling complete
- Edge cases covered
- Performance optimized
- Documentation written

**Validation**:
- No known bugs
- Performance acceptable
- Error handling robust
- Ready to ship

**Example** (E-commerce checkout):
- Handles payment failures gracefully
- Works with empty cart
- Validates all inputs
- Loads quickly with 100+ items
- Mobile-responsive

---

## Output Format

### Primary Deliverable: Working Code

**Code Characteristics**:
- Follows project conventions
- Well-structured and maintainable
- Properly commented
- Error handling implemented
- Tests included (where applicable)

### Secondary Deliverable: implementation.md

**Location**: `[TARGET_FOLDER]/implementation.md`

**Structure** (following knowledge/document_style_guide.md):
```markdown
# Implementation - [Feature Name]

## Description
[What was built and why]

## Implementation Details

### Technical Approach
[How it was built]

### Architecture Decisions
[Key choices made]

### Dependencies
[Libraries/services used]

## Components & Changes

### Files Modified
| File | Purpose | Changes |
|------|---------|---------|
| path/to/file1.js | Component | Added feature X |
| path/to/file2.js | API | Updated endpoints |

### New Components
[New files created]

## Testing & Validation

### Test Coverage
- [x] Unit tests
- [x] Integration tests
- [x] Manual testing
- [x] Edge cases

### Validation Results
[Summary of testing]

## Deployment & Next Steps

### Deployment Checklist
- [ ] Environment variables
- [ ] Build optimization
- [ ] Documentation updated

### Next Steps
1. Code review
2. Staging deployment
3. Production release
```

**Metadata**:
- Status: Implementation Complete
- Date: [Current Date]
- Developer: Claude

---

## Standards & Quality

### Code Quality Standards

**Readability**:
- Clear variable/function names
- Consistent formatting
- Logical organization
- Appropriate abstraction level

**Maintainability**:
- DRY (Don't Repeat Yourself)
- SOLID principles where applicable
- Modular structure
- Loosely coupled components

**Comments**:
- Complex logic explained
- Why, not what (code shows what)
- Public APIs documented
- TODOs for known limitations

**Project Conventions**:
- Follow existing patterns
- Match naming conventions
- Use same libraries/tools
- Respect file organization

### Functionality Standards

**Correctness**:
- Meets all requirements
- Produces correct results
- No logical errors
- Handles all cases

**Robustness**:
- Error handling comprehensive
- Edge cases covered
- Input validation thorough
- Graceful degradation

**Performance**:
- Acceptable response times
- Efficient algorithms
- No memory leaks
- Scales appropriately

**Security**:
- Input sanitization
- SQL injection prevention
- XSS protection
- Authentication/authorization
- Secrets not hardcoded

### Testing Standards

**Coverage**:
- Critical paths 100% tested
- Happy path verified
- Edge cases covered
- Error conditions tested

**Types**:
- Unit tests (individual functions)
- Integration tests (components together)
- End-to-end tests (full user flows)
- Manual testing (UI/UX)

**Quality**:
- Tests are deterministic
- Tests are independent
- Tests are fast
- Tests are maintainable

---

## Rules

### ALWAYS
- Understand requirements before coding
- Test as you build (don't write all code then test)
- Keep code working (commit often)
- Follow project standards and conventions
- Handle errors gracefully
- Validate inputs
- Write clean, readable code
- Create implementation.md documentation
- Test edge cases
- Consider performance and security

### NEVER
- Over-engineer solutions
- Skip testing
- Ignore edge cases
- Leave code broken
- Commit untested code
- Hardcode secrets/credentials
- Skip error handling
- Forget documentation
- Ignore project conventions
- Sacrifice readability for cleverness

### PREFER
- Simple over complex
- Clear over clever
- Working over perfect
- Incremental over big bang
- Pragmatic over theoretical
- Tested over assumed
- Refactored over duplicated
- Documented over mysterious

---

## Implementation Philosophy

**Core Principle**: "Ship working code that solves real problems"

**Pragmatic Approach**:
- Focus on solving the actual problem
- Don't over-engineer for hypothetical futures
- Build incrementally, ship frequently
- Refactor when needed, not preemptively
- Test what matters, not everything
- Document for humans, not just machines

**Quality Mindset**:
- Working > Perfect
- Maintainable > Elegant
- Clear > Concise
- Tested > Assumed
- Pragmatic > Purist

By following this philosophy, implementations are:
- **Delivered faster**: Incremental approach ships sooner
- **More reliable**: Continuous testing catches bugs early
- **Easier to maintain**: Clear, simple code ages better
- **Lower risk**: Small changes are safer than big rewrites

## Bundled Resources

### References

**`references/implementation-patterns.md`** (~300 lines):
- **Purpose**: Practical patterns for incremental development, testing, and refactoring
- **When to Load**: When implementing specific functionality or need coding examples
- **Contents**:
  - TDD (Test-Driven Development) patterns
  - Incremental development workflow
  - Error handling patterns (try-catch, validation)
  - State management patterns (React hooks)
  - Refactoring patterns (extract function, simplify)
  - Progressive enhancement techniques
  - Feature flag implementations
  - Component composition patterns
  - Integration patterns (API clients)
  - Testing strategies (unit, integration, e2e)

**`references/quality-standards.md`** (~250 lines):
- **Purpose**: Comprehensive standards for code quality, functionality, and testing
- **When to Load**: When ensuring code meets quality standards or reviewing code
- **Contents**:
  - Code readability (naming, structure, comments)
  - DRY principle (avoiding repetition)
  - Error handling standards (validation, graceful degradation)
  - Performance standards (acceptable response times, optimization)
  - Security standards (input sanitization, secrets management)
  - Testing standards (coverage requirements, test quality)
  - Edge case checklist

**`references/documentation-templates.md`** (~200 lines):
- **Purpose**: Templates and examples for implementation documentation
- **When to Load**: When creating implementation.md or need documentation examples
- **Contents**:
  - Complete implementation.md template with all sections
  - Section-by-section guidance and examples
  - Inline comment examples (function docs, complex logic)
  - TODO/FIXME/HACK comment patterns
  - Markdown formatting examples
  - Deployment checklist template
  - Testing results format

---


## Version Information

**Current Version**: 1.0.0
**Created**: 2025-10-18
**Based On**: `code_implementer.yaml`
**Architecture**: Sequential 3-step workflow (Understand → Build → Polish)
**Compatible With**: Spec-driven development, plan-based implementation
