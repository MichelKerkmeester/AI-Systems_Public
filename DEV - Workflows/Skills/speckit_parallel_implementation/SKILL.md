---
name: speckit_parallel_implementation
description: Execute autonomous spec-driven implementation with parallel preparation agents. Orchestrates 6 specialized sub-agents for implementation planning (core, integrations, tests, docs) through parallel execution, review, and synthesis into implementation_plan.md, then proceeds with development.
---

# SpecKit Implementation

Execute autonomous implementation workflow with parallel preparation and progressive development checkpoints.

## When to Use This Skill

**Use this skill when**:
- Ready to implement a fully specified feature
- Have spec.md and plan.md completed
- Need comprehensive implementation preparation
- Want parallel planning for core, tests, and docs
- Executing actual code changes autonomously

**Do NOT use this skill for**:
- Initial specification creation (use speckit-plan-spec)
- Research and investigation (use speckit-feature-research)
- Simple planning without implementation
- Manual implementation processes

## Architecture Overview

This skill implements the sk_p__implementation.yaml workflow with 6 specialized implementation sub-agents executing in parallel preparation phase.

### Implementation Workflow Steps

**Note**: This workflow covers steps 8-15 of the complete SpecKit process (8 steps total). Steps 1-7 are assumed completed via planning workflow.

1. **Review Plan and Spec** (Step 8) - Understand existing artifacts
2. **Task Breakdown** (Step 9) - Generate actionable tasks
3. **Analysis** (Step 10) - Check consistency and coverage
4. **Quality Checklist** (Step 11) - Generate quality gates
5. **Parallel Implementation Prep** (Step 12) - 4 agents prepare approach
6. **Implementation Check** (Step 13) - Verify prerequisites
7. **Development** (Step 14) - Execute autonomous implementation
8. **Completion** (Step 15) - Document changes and summary

### The 6 Implementation Sub-Agents

**Note**: For detailed agent specifications with complete output formats, see [references/sub-agents.md](references/sub-agents.md).

1. **Core Implementer**
   - Module breakdown
   - Data structures
   - Algorithms
   - Business logic

2. **Integrations/Adapters Engineer**
   - External integrations
   - API surfaces
   - Configuration matrix
   - Error handling

3. **Test Engineer**
   - Test plan creation
   - Test cases definition
   - Fixtures preparation
   - Coverage targets

4. **Docs Engineer**
   - Usage documentation
   - Code examples
   - Migration notes
   - API documentation

5. **Integration Reviewer**
   - Coherence validation
   - API consistency
   - Testability assessment
   - Gap identification

6. **Lead Synthesizer**
   - Implementation strategy
   - Task ordering
   - Dependency mapping
   - Plan document creation

## Execution Model

### Parallel Preparation Pattern

```
┌─────────────────────────────────┐
│  Parallel Implementation Prep    │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │Core│ │Intg│ │Test│ │Docs│   │ ← Execute in parallel
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Integration Review          │ ← Reviewer validates coherence
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Synthesis Phase           │ ← Synthesizer creates plan
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Main Agent QA Phase         │ ← Final validation
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│    Autonomous Implementation     │ ← Execute code changes
└─────────────────────────────────┘
```

## Implementation Plan Structure

The skill produces `implementation_plan.md` with these sections:

### Core Sections

**Module Architecture**
- Component breakdown
- Module responsibilities
- Interface definitions
- Dependency graph

**Data Structures**
- Type definitions
- State management
- Data flow patterns
- Storage schemas

**Integration Points**
- External APIs
- Service contracts
- Configuration requirements
- Error handling strategies

**Test Strategy**
- Unit test plan
- Integration tests
- E2E scenarios
- Coverage targets

### Supporting Sections

**Development Approach**
- Implementation sequence
- Task dependencies
- Risk mitigation
- Checkpoint definitions

**Documentation Plan**
- User guides
- API references
- Migration guides
- Code examples

**Quality Gates**
- Acceptance criteria
- Performance targets
- Security requirements
- Accessibility standards

## Inputs

### Required Inputs
- **spec_folder**: Location with spec.md and plan.md
- **request**: Implementation requirements (or uses default)

### Optional Inputs
- **git_branch**: Feature branch name
- **context**: Additional implementation context
- **issues**: Known issues to address
- **environment**: Staging URL for testing
- **scope**: File scope limitations

### Default Request
If no request provided:
```
"Conduct a comprehensive review of the spec folder and
carry out its implementation fully autonomously."
```

## Outputs

### Primary Outputs

1. **implementation_plan.md**
   - Location: `[SPEC_FOLDER]/implementation_plan.md`
   - Complete implementation strategy
   - All preparation artifacts synthesized

2. **implementation-summary.md**
   - Location: `[SPEC_FOLDER]/implementation-summary.md`
   - Files modified/created
   - Verification steps taken
   - Deviations from plan

3. **Actual Code Changes**
   - Implementation of all tasks
   - Tests and documentation
   - Progressive updates

## Parallel Agent Details

### Core Implementer Output
```yaml
modules:
  - name: [module name]
    responsibility: [purpose]
    exports: [public interface]
    dependencies: [imports]
data_structures:
  - type: [structure]
    purpose: [usage]
    fields: [properties]
algorithms:
  - name: [algorithm]
    complexity: [Big O]
    approach: [description]
```

### Integration Engineer Output
```yaml
integrations:
  - service: [external service]
    protocol: [REST/GraphQL/etc]
    authentication: [method]
api_contracts:
  - endpoint: [path]
    method: [HTTP method]
    request: [schema]
    response: [schema]
error_handling:
  - error_type: [class]
    handling: [strategy]
    recovery: [approach]
```

### Test Engineer Output
```yaml
test_plan:
  unit_tests:
    - module: [name]
      cases: [count]
      coverage: [target%]
  integration_tests:
    - scenario: [description]
      components: [list]
  fixtures:
    - name: [fixture]
      purpose: [usage]
      data: [sample]
```

### Docs Engineer Output
```yaml
documentation:
  usage_guide:
    - section: [title]
      content: [outline]
  api_reference:
    - endpoint: [name]
      description: [purpose]
  examples:
    - scenario: [use case]
      code: [snippet]
  migration:
    - from: [version]
      to: [version]
      steps: [process]
```

## Development Checkpoints

### Major Change Checkpoint
- Log progress to summary
- Update task checklist
- Verify against spec

### Issue Found Checkpoint
- Document issue and resolution
- Update implementation plan if needed
- Continue or escalate

### Architecture Change Checkpoint
- Note deviation from plan
- Document rationale
- Update affected documentation

## Chrome DevTools Integration

### Environment Validation
- Test API endpoints
- Verify authentication
- Check dependencies

### Implementation Testing
- Test in browser
- Verify network calls
- Check console output
- Validate DOM changes
- Measure performance

## Adaptive Rules

**Note**: For complete adaptive rule specifications, complexity assessment, technical debt scoring, and testing strategies, see [references/adaptive-rules.md](references/adaptive-rules.md).

### High Complexity
- Reduce concurrency to 2
- Exhaustive review depth
- Additional validation steps

### High Uncertainty
- Add discovery phase before parallel
- Document assumptions
- Create proof of concepts

### Fallback Strategy
- Sequential execution if parallel fails
- Maintain review/synthesis phases
- Continue with partial results

## Quality Standards

### Implementation Requirements
- Follow code_standards.md
- Progressive task updates
- Test before commit
- No premature optimization

### Documentation Standards
- Developer-facing clarity
- Working code examples
- Migration paths documented
- API contracts complete

### Testing Requirements
- Critical paths covered
- Edge cases identified
- Performance benchmarks
- Security validations

## Performance Characteristics

**Note**: Performance varies based on implementation scope and complexity. Preparation is structured; implementation duration depends on feature requirements.

- **Preparation phase**: Parallel agent execution + review + synthesis
- **Parallel execution**: Multiple agents work concurrently
- **Review/synthesis**: Sequential refinement process
- **Implementation**: Variable based on scope and complexity
- **Checkpoints**: Lightweight validation points

## Error Handling

### Retry Policy
- **Targeted retries**: Only failed components
- **Max attempts**: 2 per agent
- **Backoff**: Exponential

### Recovery Actions
- Document blockers
- Use partial results
- Manual intervention points
- Graceful degradation

## Limitations

- **Prerequisites**: Requires completed spec/plan
- **Scope**: Limited to defined file scope
- **Autonomy**: No user interaction during execution
- **Testing**: Browser testing requires staging URL
- **Complexity**: Best for medium complexity features

## Success Metrics

**Note**: Target quality objectives for implementation execution.

- **Preparation completeness**: All sections populated
- **Review pass rate**: >90% first pass
- **Implementation coverage**: >95% tasks completed
- **Test coverage**: Meets defined targets
- **Documentation**: Complete and accurate

## Version

**Current Version**: 1.0.0
**Based On**: sk_p__implementation.yaml
**Created**: 2025-10-18
**Architecture**: Parallel preparation → Autonomous implementation

---

## References

- Source: `/b_prompts/github_spec_kit/parallel_agents/sk_p__implementation.yaml`
- Prerequisites: spec.md, plan.md, planning-summary.md
- Integration: Works with all SpecKit skills
- Output: implementation_plan.md, implementation-summary.md, code changes