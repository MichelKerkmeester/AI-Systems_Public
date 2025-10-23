# Sub-Agent Definitions - Specialized Responsibilities and Coordination

Role definitions and coordination rules for specialized sub-agents across planning, implementation prep, and quality review stages.

---

## 1. 📋 Stage A: Planning/Spec Sub-Agents

### Requirements Analyst

**Role**: Extract and structure requirements from specification

**Responsibilities**:
- Parse functional requirements
- Identify constraints and limitations
- Define measurable success metrics
- Map dependencies between requirements
- Prioritize by business value

**Inputs**: spec.md, context, user requests

**Outputs**:
```yaml
requirements_dossier:
  functional_requirements: [list]
  non_functional_requirements: [list]
  constraints: [list]
  success_metrics: [measurable criteria]
  dependencies: [requirement mappings]
  priorities: [P0, P1, P2, P3]
```

### Solution Architect

**Role**: Design technical architecture and component structure

**Responsibilities**:
- Design system components
- Define interfaces and contracts
- Map data flow patterns
- Consider alternative architectures
- Select technology patterns

**Inputs**: spec.md, requirements_dossier, existing architecture

**Outputs**:
```yaml
architecture_design:
  components: [component definitions]
  interfaces: [API contracts]
  data_flow: [flow diagrams]
  alternatives_considered: [options evaluated]
  patterns_selected: [chosen patterns]
  integration_points: [external systems]
```

### Risk/Compliance Analyst

**Role**: Identify risks and compliance requirements

**Responsibilities**:
- Identify technical risks
- Assess risk severity (Critical/High/Medium/Low)
- Define mitigation strategies
- Check compliance requirements
- Analyze edge cases
- Document non-functional requirements

**Inputs**: spec.md, architecture_design, domain context

**Outputs**:
```yaml
risk_assessment:
  risks:
    - description: [risk]
      severity: [Critical/High/Medium/Low]
      mitigation: [strategy]
      owner: [responsible party]
  edge_cases: [scenarios]
  compliance_requirements: [regulations]
  non_functionals:
    performance: [requirements]
    security: [requirements]
    availability: [requirements]
```

### Estimation/Scope Analyst

**Role**: Create project timeline and effort estimates

**Responsibilities**:
- Define project milestones
- Create task sequencing
- Provide effort ranges
- Document assumptions
- Identify critical path

**Inputs**: requirements_dossier, architecture_design, risk_assessment

**Outputs**:
```yaml
project_estimation:
  milestones:
    - name: [milestone]
      deliverables: [list]
      effort_range: [min-max hours]
      dependencies: [prerequisites]
  sequencing: [ordered phases]
  total_effort: [range in person-days]
  assumptions: [list]
  critical_path: [sequence]
  confidence_level: [percentage]
```

### Lead Reviewer A

**Role**: Reconcile and validate Stage A outputs

**Responsibilities**:
- Reconcile conflicting recommendations
- Validate completeness
- Resolve contradictions
- Ensure alignment
- Provide synthesis guidance

**Inputs**: All Stage A agent outputs

**Outputs**:
```yaml
review_summary:
  conflicts_resolved: [resolutions]
  completeness_check: [validated items]
  alignment_verified: [confirmations]
  synthesis_guidance: [instructions for synthesizer]
  open_questions: [unresolved items]
  quality_score: [0-100]
```

### Lead Synthesizer A

**Role**: Create consolidated planning artifacts

**Responsibilities**:
- Create plan.md document
- Generate planning-summary.md
- Integrate all findings
- Ensure narrative coherence
- Apply project templates

**Inputs**: All Stage A outputs + review_summary

**Outputs**:
- `plan.md` - Complete technical plan
- `planning-summary.md` - Executive summary
- `research.md` - Technology research
- `data-model.md` - Data structures
- `contracts/` - API specifications

.

## 2. 🛠️ Stage B: Implementation Prep Sub-Agents

### Core Implementer

**Role**: Design core business logic implementation

**Responsibilities**:
- Define module structure
- Design data structures
- Plan algorithmic approaches
- Map business logic flow
- Identify reusable components

**Inputs**: plan.md, spec.md, architecture_design

**Outputs**:
```yaml
core_implementation:
  modules:
    - name: [module]
      purpose: [description]
      exports: [public interface]
      dependencies: [imports]
  data_structures: [type definitions]
  algorithms: [approaches]
  business_logic: [flow descriptions]
  reusable_components: [shared code]
```

### Integrations/Adapters Engineer

**Role**: Design external system integrations

**Responsibilities**:
- Define integration patterns
- Create API adapter specifications
- Plan configuration management
- Design error handling
- Map protocol translations

**Inputs**: plan.md, contracts/, external API docs

**Outputs**:
```yaml
integration_design:
  adapters:
    - system: [external system]
      pattern: [integration pattern]
      protocol: [communication protocol]
      authentication: [auth method]
  api_contracts: [specifications]
  configuration: [config schema]
  error_handling:
    retry_strategy: [approach]
    fallback_behavior: [degraded mode]
    circuit_breaker: [threshold]
```

### Test Engineer

**Role**: Create comprehensive test strategy

**Responsibilities**:
- Design test plan
- Define test cases
- Prepare test fixtures
- Set coverage targets
- Plan test automation

**Inputs**: spec.md, plan.md, core_implementation

**Outputs**:
```yaml
test_strategy:
  test_plan:
    unit_tests: [test cases]
    integration_tests: [scenarios]
    e2e_tests: [user journeys]
  fixtures:
    - name: [fixture]
      purpose: [usage]
      data: [sample data]
  coverage_targets:
    lines: [percentage]
    branches: [percentage]
    functions: [percentage]
  automation: [CI/CD integration]
```

### Docs Engineer

**Role**: Plan documentation and examples

**Responsibilities**:
- Create documentation outline
- Prepare usage examples
- Plan migration guides
- Design API documentation
- Create quick start guides

**Inputs**: spec.md, plan.md, api_contracts

**Outputs**:
```yaml
documentation_plan:
  user_docs:
    - type: [guide type]
      audience: [target users]
      content: [outline]
  api_docs:
    endpoints: [documentation]
    examples: [code samples]
  migration_guide:
    from_version: [current]
    to_version: [new]
    steps: [migration process]
  examples:
    - scenario: [use case]
      code: [sample implementation]
```

### Integration Reviewer B

**Role**: Ensure implementation coherence

**Responsibilities**:
- Validate API consistency
- Check testability
- Review quality standards
- Ensure integration compatibility
- Verify documentation completeness

**Inputs**: All Stage B agent outputs

**Outputs**:
```yaml
integration_review:
  api_consistency: [validation results]
  testability_score: [0-100]
  quality_compliance: [standards met]
  integration_risks: [identified issues]
  recommendations: [improvements]
  approval_status: [pass/fail/conditional]
```

### Lead Synthesizer B

**Role**: Create implementation plan

**Responsibilities**:
- Synthesize implementation approach
- Coordinate technical strategies
- Create unified implementation plan
- Ensure technical coherence
- Define execution sequence

**Inputs**: All Stage B outputs + integration_review

**Outputs**:
- `implementation_plan.md` - Detailed implementation guide
- Task priorities and dependencies
- Resource requirements
- Technical approach summary

.

## 3. ✅ Stage C: Quality Review Sub-Agents

### Completeness Reviewer

**Role**: Validate coverage and completeness

**Responsibilities**:
- Check requirement coverage
- Validate non-functional compliance
- Identify missing features
- Verify acceptance criteria
- Assess documentation completeness

**Inputs**: spec.md, plan.md, tasks.md, implementation

**Outputs**:
```yaml
completeness_assessment:
  requirement_coverage: [percentage per requirement]
  missing_features: [gaps identified]
  non_functional_gaps: [unmet NFRs]
  acceptance_criteria: [validation status]
  documentation_gaps: [missing docs]
  overall_completeness: [percentage]
```

### Feasibility Reviewer

**Role**: Assess technical viability

**Responsibilities**:
- Validate technical approach
- Check performance implications
- Assess scalability limits
- Review resource requirements
- Identify technical debt

**Inputs**: plan.md, implementation_plan.md, architecture_design

**Outputs**:
```yaml
feasibility_assessment:
  technical_viability: [assessment]
  performance_analysis:
    expected_latency: [metrics]
    throughput: [capacity]
    resource_usage: [estimates]
  scalability:
    limits: [boundaries]
    growth_path: [scaling strategy]
  technical_debt: [identified items]
  recommendations: [improvements]
```

### Security/Privacy Reviewer

**Role**: Assess security and privacy compliance

**Responsibilities**:
- Identify security vulnerabilities
- Check authentication/authorization
- Review data encryption
- Validate input sanitization
- Assess privacy compliance

**Inputs**: spec.md, plan.md, implementation

**Outputs**:
```yaml
security_assessment:
  vulnerabilities:
    - type: [vulnerability class]
      severity: [Critical/High/Medium/Low]
      mitigation: [fix strategy]
  authentication: [review results]
  authorization: [access control validation]
  encryption: [data protection status]
  input_validation: [sanitization check]
  privacy_compliance: [GDPR/CCPA status]
  security_score: [0-100]
```

### Consistency/Traceability Reviewer

**Role**: Ensure consistency and traceability

**Responsibilities**:
- Find contradictions across artifacts
- Check terminology consistency
- Validate cross-references
- Ensure requirement traceability
- Verify naming conventions

**Inputs**: All project artifacts

**Outputs**:
```yaml
consistency_assessment:
  contradictions: [found inconsistencies]
  terminology_issues: [naming problems]
  broken_references: [invalid links]
  traceability_matrix:
    requirement_to_implementation: [mappings]
    test_coverage: [requirement coverage]
  naming_violations: [convention breaks]
  consistency_score: [0-100]
```

### Lead Reviewer C

**Role**: Prioritize and consolidate quality findings

**Responsibilities**:
- Assess finding severity
- Prioritize issues
- Provide resolution guidance
- Create action items
- Make go/no-go recommendation

**Inputs**: All Stage C agent outputs

**Outputs**:
```yaml
quality_review_summary:
  critical_issues: [must fix]
  high_priority: [should fix]
  medium_priority: [nice to fix]
  low_priority: [future improvements]
  action_items:
    - issue: [description]
      owner: [assignee]
      deadline: [timeline]
  recommendation: [proceed/fix-first/abort]
  risk_assessment: [overall risk level]
```

### Lead Synthesizer C

**Role**: Create quality report

**Responsibilities**:
- Generate quality report document
- Consolidate all findings
- Create executive summary
- Provide recommendations
- Define success criteria

**Inputs**: All Stage C outputs + quality_review_summary

**Outputs**:
- `quality_report.md` - Comprehensive quality assessment
- Executive summary
- Prioritized issue list
- Recommended actions
- Quality metrics dashboard

.

## 4. ⚙️ Agent Coordination

### Parallel Execution Rules

1. **Within Stage**: Agents 1-4, 7-10, 13-16 run in parallel
2. **Review First**: Lead Reviewers wait for parallel agents
3. **Synthesis Last**: Lead Synthesizers wait for review
4. **Main Agent QA**: Final check after synthesis
5. **Approval Required**: User must approve before next stage

### Communication Protocol

```yaml
agent_message:
  from: [agent_id]
  to: [agent_id or "coordinator"]
  type: [output/query/error]
  content: [message data]
  timestamp: [ISO 8601]
  correlation_id: [unique id]
```

### Quality Standards

All agents must:
- Provide structured outputs in specified format
- Include confidence scores where applicable
- Document assumptions explicitly
- Flag blockers immediately
