# Skills Directory

Complete documentation of all Claude Code skills available in this project.

## Overview

This project contains **10 specialized skills** organized into three categories:

1. **Code Development Skills** (5) - General code development, validation, debugging, and optimization
2. **SpecKit Skills** (4) - High-performance parallel workflow execution
3. **Meta Skills** (1) - Skill creation and management

## Skills Catalog

### Code Development Skills

#### 1. code_debugger
**Purpose**: Systematically reproduce, diagnose, fix, and verify bugs through evidence-based investigation and root cause analysis.

**Use when**:
- Investigating unexpected behavior, runtime errors, visual glitches
- Bug reports from users or QA
- Features not working as expected
- Need systematic bug reproduction and minimal fixes

**Location**: `.claude/skills/code_debugger/`

---

#### 2. code_implementer
**Purpose**: Build features incrementally using 3-step workflow (Understand → Build → Polish). Implements from specs or plans with continuous testing, incremental delivery, and pragmatic approach.

**Use when**:
- Implementing features from specifications
- Building from detailed plans
- Converting designs to code
- Need implementation.md documentation

**Location**: `.claude/skills/code_implementer/`

---

#### 3. code_pattern_validator
**Purpose**: Validate JavaScript files against Webflow project code standards, naming conventions, initialization patterns, and platform constraints.

**Use when**:
- Reviewing code for standards compliance before committing
- Validating generated code
- Enforcing naming conventions (snake_case, kebab-case)
- Checking platform constraint awareness
- Verifying accessibility compliance (ARIA attributes)

**Location**: `.claude/skills/code_pattern_validator/`

---

#### 4. code_performance_improver
**Purpose**: Optimize code and application performance through systematic profiling, analysis, and incremental improvements while preserving all functionality.

**Use when**:
- Application has slow load times or poor performance
- Core Web Vitals scores need improvement (LCP, FCP, CLS, FID)
- Memory usage is too high or memory leaks suspected
- Animations are choppy or dropping frames
- Bundle sizes are too large

**Location**: `.claude/skills/code_performance_improver/`

---

#### 5. code_planner
**Purpose**: Create comprehensive project plans using 5 parallel autonomous planning agents (Scope, Breakdown, Resource, Timeline, Quality).

**Use when**:
- Need comprehensive project plan
- Breaking down complex features
- Estimating timeline and resources
- Identifying risks and dependencies
- Planning multi-phase projects

**Location**: `.claude/skills/code_planner/`

---

### SpecKit Skills

High-performance workflow execution with multiple specialized sub-agents running concurrently.

#### 6. speckit_complete
**Purpose**: Execute the complete 14-step SpecKit workflow with 18 specialized sub-agents running in 3 parallel stages.

**Complexity**: Very High (18 sub-agents in 3 stages)

**Use when**:
- Need full end-to-end automated feature development
- Complex workflows require orchestration of multiple agents
- Want maximum parallelization for speed

**Location**: `.claude/skills/speckit_complete/`
**Based on**: `z_prompts/github_spec_kit/parallel_agents/sk_p__complete.yaml`

---

#### 7. speckit_feature_research
**Purpose**: Conduct parallel technical research and investigation for SpecKit features. Orchestrates 6 specialized research sub-agents to produce comprehensive research.md documentation.

**Complexity**: Medium (6 sub-agents)

**Use when**:
- Conducting technical investigation for a new feature
- Researching libraries, frameworks, and ecosystem patterns
- Analyzing vendor solutions and alternatives
- Evaluating technical feasibility and costs

**Location**: `.claude/skills/speckit_feature_research/`
**Based on**: `z_prompts/github_spec_kit/parallel_agents/sk_p__feature_research.yaml`

---

#### 8. speckit_implementation
**Purpose**: Execute autonomous spec-driven implementation with parallel preparation agents. Orchestrates 6 specialized sub-agents for implementation planning (core, integrations, tests, docs).

**Complexity**: Medium (6 sub-agents)

**Use when**:
- Ready to implement a fully specified feature
- Have spec.md and plan.md completed
- Need comprehensive implementation preparation
- Want parallel planning for core, tests, and docs

**Location**: `.claude/skills/speckit_implementation/`
**Based on**: `z_prompts/github_spec_kit/parallel_agents/sk_p__implementation.yaml`

---

#### 9. speckit_spec_plan
**Purpose**: Execute spec-driven planning workflow with parallel specialist analyses. Orchestrates 6 specialized planning sub-agents through parallel execution, review, and synthesis.

**Complexity**: Medium (6 sub-agents)

**Use when**:
- Creating technical plans from specifications
- Need parallel analysis from multiple specialists
- Require comprehensive risk and architecture assessment
- Want estimation and milestone planning

**Location**: `.claude/skills/speckit_spec_plan/`
**Based on**: `z_prompts/github_spec_kit/parallel_agents/sk_p__spec_plan.yaml`

---

### Meta Skills

#### 10. create_skills
**Purpose**: Guide for creating effective skills. This skill should be used when users want to create a new skill or update an existing skill.

**Use when**:
- Creating a new skill from scratch
- Updating an existing skill
- Need guidance on skill structure and best practices
- Want to extend Claude's capabilities with specialized knowledge

**Location**: `.claude/skills/create_skills/`

---

## Skill Selection Guide

### Decision Tree

```
Need to debug existing code?
└─ YES → code_debugger

Need to validate code quality?
└─ YES → code_pattern_validator

Need to optimize performance?
└─ YES → code_performance_improver

Need to implement a feature?
├─ Have specs/plan? → code_implementer
└─ Need plan first? → code_planner

Need research for new feature?
└─ YES → speckit_feature_research

Need technical plan from spec?
└─ YES → speckit_spec_plan

Ready to implement with specs?
└─ YES → speckit_implementation

Want complete automated workflow?
└─ YES → speckit_complete

Need to create/update skills?
└─ YES → create_skills
```

### Quick Reference

| Task | Recommended Skill |
|------|-------------------|
| Fix a bug | code_debugger |
| Validate code quality | code_pattern_validator |
| Optimize performance | code_performance_improver |
| Create project plan | code_planner |
| Implement feature | code_implementer |
| Research feature | speckit_feature_research |
| Plan from spec | speckit_spec_plan |
| Implement from plan | speckit_implementation |
| Complete workflow | speckit_complete |
| Create new skill | create_skills |

---

## SpecKit Command Integration

### Commands and Their Associated Skills

| SpecKit Command | Associated Skill |
|-----------------|------------------|
| `/speckit.specify` | (built-in) |
| `/speckit.clarify` | (built-in) |
| `/speckit.plan` | speckit_spec_plan |
| `/speckit.tasks` | (built-in) |
| `/speckit.implement` | speckit_implementation |
| `/speckit.analyze` | (built-in) |
| `/speckit.checklist` | (built-in) |
| `/speckit.constitution` | (built-in) |
| (research workflow) | speckit_feature_research |
| (complete workflow) | speckit_complete |

---

## Architecture Overview

### Code Development Skills Architecture

```
User Request
     ↓
┌────────────────────────────────────┐
│   Code Development Skills          │
│                                    │
├─ Debugging? → code_debugger       │
├─ Planning? → code_planner         │
├─ Implementing? → code_implementer │
├─ Validating? → code_pattern_validator
└─ Optimizing? → code_performance_improver
└────────────────────────────────────┘
     ↓
Production Code
```

### SpecKit Skills Architecture

```
           User Request
                ↓
    ┌───────────────────────┐
    │    SpecKit Skills     │
    │                       │
    │ • Complete            │
    │ • Research            │
    │ • Planning            │
    │ • Implementation      │
    └───────────────────────┘
                ↓
    Feature Artifacts & Code
```

---

## Shared Artifacts

Skills communicate through standardized artifacts:

```yaml
shared_artifacts:
  specifications:
    - spec.md
    - clarifications.md
  planning:
    - plan.md
    - planning-summary.md
    - research.md
  implementation:
    - implementation_plan.md
    - implementation-summary.md
    - implementation.md
  tasks:
    - tasks.md
    - checklists/*.md
  quality:
    - analysis/consistency-report.md
    - quality_report.md
```

---

## Best Practices

### DO:
- Use specialized skills for their intended purpose
- Check artifacts between skill executions
- Allow skills to share context through files
- Monitor token usage with parallel skills
- Select appropriate skill for task complexity

### DON'T:
- Load all skills simultaneously
- Mix skill responsibilities
- Ignore approval gates in workflows
- Skip prerequisite validation
- Use complex SpecKit workflows for simple tasks

### ALWAYS:
- Verify prerequisites before skill execution
- Document skill handoffs through artifacts
- Maintain artifact consistency
- Provide user visibility into progress
- Enable manual override when needed

---

## Token Usage & Performance

### Token Usage by Skill Type

| Skill Category | Initial Load | Full Context | Recommendation |
|----------------|--------------|--------------|----------------|
| Code Skills | Low (~1-2K) | Medium (~3-5K) | Load as needed |
| SpecKit | High (~5-8K) | Very High (~15-25K) | On-demand only |
| Meta Skills | Low (~1K) | Low (~2K) | Load as needed |

### Concurrency Management

```yaml
recommended_concurrency:
  code_debugger: 1           # Sequential debugging
  code_implementer: 1        # Sequential implementation
  code_pattern_validator: 3  # Can validate multiple files
  code_performance_improver: 1  # Sequential optimization
  code_planner: 2            # Can plan multiple aspects

  speckit_*: 3               # Designed for parallelism

  create_skills: 1           # Single skill creation
```

---

## Troubleshooting

### Common Issues

**Issue**: Skills not loading or triggering
**Solution**: Check skill name matches exactly; verify SKILL.md exists

**Issue**: Workflow execution timeout
**Solution**: Reduce concurrency, break into smaller tasks, or use simpler code skills

**Issue**: Artifact mismatch between skills
**Solution**: Verify file paths and naming conventions in spec directory

**Issue**: Token limit exceeded
**Solution**: Use skills one at a time; prefer simpler code skills for simple tasks

**Issue**: Approval gates blocking in workflows
**Solution**: Ensure explicit user approval at each gate; don't skip steps

---

## Version Information

| Skill | Version | Last Updated | Status |
|-------|---------|--------------|--------|
| code_debugger | 1.0.0 | 2025-10-18 | Active |
| code_implementer | 1.0.0 | 2025-10-18 | Active |
| code_pattern_validator | 1.0.0 | 2025-10-18 | Active |
| code_performance_improver | 1.0.0 | 2025-10-18 | Active |
| code_planner | 1.0.0 | 2025-10-18 | Active |
| speckit_complete | 1.0.0 | 2025-10-18 | Active |
| speckit_feature_research | 1.0.0 | 2025-10-18 | Active |
| speckit_implementation | 1.0.0 | 2025-10-18 | Active |
| speckit_spec_plan | 1.0.0 | 2025-10-18 | Active |
| create_skills | 1.0.0 | 2025-10-18 | Active |

---

## Integration with AGENTS.md

Skills follow the principles and standards defined in `/AGENTS.md`:

- All skills adhere to the Clarification Rule (confidence < 80% → ask questions)
- All skills use Explicit Uncertainty markers when appropriate
- All skills follow the REQUEST ANALYSIS & SOLUTION FRAMEWORK
- All skills maintain evidence-based decision making
- All skills prioritize simplicity and maintainability

**Reference**: See `AGENTS.md:500-665` for detailed skill integration guidance.

---

## Summary

This project provides a comprehensive skill ecosystem:

- **5 Code Skills** for general development, debugging, validation, and optimization
- **4 SpecKit Skills** for high-performance automated workflows with parallel execution
- **1 Meta Skill** for skill creation and management

Together, these 10 skills enable efficient development workflows while maintaining clarity, control, and quality standards.
