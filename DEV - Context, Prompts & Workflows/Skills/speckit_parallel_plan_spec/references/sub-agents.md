# Planning & Specification Sub-Agents

Detailed specifications for the 6 specialized planning and specification sub-agents.

## 1. Requirements Analyst

**Role**: Extract and structure requirements from specifications and context

**Responsibilities**:
- Parse functional requirements
- Identify non-functional requirements
- Define constraints and boundaries
- Map dependencies
- Create measurable success metrics

**Analysis Focus**:
- User stories and scenarios
- Acceptance criteria
- Business rules
- Compliance requirements
- Performance targets

**Output Format**:
```yaml
requirements_dossier:
  objectives:
    - id: "OBJ-001"
      description: "Primary objective"
      priority: "P0"  # P0=Critical, P1=High, P2=Medium, P3=Low
      rationale: "Business justification"
      success_criteria:
        - criterion: "Measurable outcome"
          metric: "How to measure"
          target: "Specific value"

  functional_requirements:
    - id: "FR-001"
      category: "Feature area"
      description: "What the system must do"
      acceptance_criteria:
        - "Given [context], When [action], Then [outcome]"
      priority: "P0"
      dependencies: ["FR-002", "NFR-001"]

  non_functional_requirements:
    - id: "NFR-001"
      category: "performance|security|usability|reliability"
      description: "Quality attribute"
      metric: "Measurable criteria"
      target: "Specific goal"
      validation: "How to verify"

  constraints:
    - type: "technical|business|regulatory|resource"
      description: "Limitation or restriction"
      impact: "How it affects design"
      mitigation: "How to work within it"

  dependencies:
    internal:
      - component: "System component"
        type: "data|api|library"
        status: "existing|required|planned"
    external:
      - service: "Third-party service"
        type: "api|data|authentication"
        criticality: "critical|important|nice-to-have"

  success_metrics:
    - category: "user|business|technical"
      metric: "KPI name"
      current_baseline: "Current value"
      target: "Goal value"
      measurement_method: "How to measure"
      frequency: "How often to measure"
```

**Quality Criteria**:
- Complete requirement coverage
- Clear acceptance criteria
- Measurable success metrics
- Traced dependencies
- Prioritized objectives

---

## 2. Solution Architect

**Role**: Design technical architecture and system components

**Responsibilities**:
- Define system architecture
- Design component interfaces
- Map data flows
- Select design patterns
- Evaluate alternatives

**Architecture Focus**:
- System decomposition
- Component responsibilities
- Interface contracts
- Data models
- Integration patterns

**Output Format**:
```yaml
architecture_proposal:
  overview:
    approach: "Architectural style"
    rationale: "Why this approach"
    key_principles:
      - "Principle and explanation"

  components:
    - id: "COMP-001"
      name: "ComponentName"
      type: "service|module|library"
      responsibility: "Single responsibility"
      technology: "Tech stack"
      interfaces:
        provided:
          - name: "InterfaceName"
            type: "REST|GraphQL|Event"
            contract: "API specification"
        required:
          - name: "DependencyInterface"
            from: "ComponentName"
            type: "Interface type"

  data_flow:
    - flow_id: "DF-001"
      description: "User action flow"
      steps:
        - step: 1
          source: "Component/Actor"
          action: "What happens"
          destination: "Component"
          data: "Data transferred"
          protocol: "HTTP|WebSocket|Event"

  data_models:
    - entity: "EntityName"
      attributes:
        - name: "attribute"
          type: "datatype"
          constraints: ["required", "unique"]
      relationships:
        - type: "one-to-many|many-to-many"
          target: "OtherEntity"

  design_patterns:
    - pattern: "Pattern name"
      application: "Where/how used"
      benefits: "Why chosen"
      implementation: "How to implement"

  alternatives_considered:
    - option: "Alternative architecture"
      pros:
        - "Advantage"
      cons:
        - "Disadvantage"
      rejection_reason: "Why not selected"

  trade_offs:
    - decision: "Architectural decision"
      trade_off: "What we gain vs lose"
      rationale: "Why acceptable"
```

**Quality Criteria**:
- Clear component boundaries
- Well-defined interfaces
- Documented patterns
- Justified decisions
- Scalability consideration

---

## 3. Risk/Compliance Analyst

**Role**: Identify and assess risks, ensure compliance

**Responsibilities**:
- Identify technical risks
- Assess business risks
- Check regulatory compliance
- Define mitigation strategies
- Document edge cases

**Risk Focus**:
- Security vulnerabilities
- Performance bottlenecks
- Scalability limits
- Compliance requirements
- Data privacy

**Output Format**:
```yaml
risk_assessment:
  risk_register:
    - id: "RISK-001"
      category: "technical|business|security|operational"
      description: "Risk description"
      trigger: "What causes this risk"
      impact:
        severity: "critical|high|medium|low"
        description: "What happens if realized"
        affected_areas: ["Components affected"]
      likelihood:
        probability: "percentage"
        factors: ["Contributing factors"]
      mitigation:
        strategy: "avoid|reduce|transfer|accept"
        actions:
          - "Specific mitigation action"
        residual_risk: "Risk after mitigation"
      owner: "Responsible party"
      monitoring: "How to detect"

  edge_cases:
    - scenario: "Edge case description"
      conditions: "When this occurs"
      current_handling: "How system handles now"
      recommended_handling: "Improved approach"
      test_approach: "How to validate"

  compliance_requirements:
    - regulation: "GDPR|CCPA|HIPAA|PCI-DSS"
      applicable: boolean
      requirements:
        - requirement: "Specific requirement"
          implementation: "How to comply"
          validation: "How to verify"

  non_functional_analysis:
    security:
      authentication: "Method and requirements"
      authorization: "Access control approach"
      data_protection: "Encryption and security"
      vulnerabilities:
        - type: "OWASP category"
          mitigation: "Prevention approach"

    performance:
      - metric: "Response time|Throughput|Concurrency"
        requirement: "Target value"
        current: "Baseline if known"
        gap: "Improvement needed"
        approach: "How to achieve"

    accessibility:
      - standard: "WCAG 2.1 Level AA"
        requirement: "Specific requirement"
        implementation: "How to meet"
        testing: "Validation approach"

  contingency_planning:
    - scenario: "Failure scenario"
      detection: "How to detect"
      response: "Immediate actions"
      recovery: "Recovery process"
      communication: "Stakeholder notification"
```

**Quality Criteria**:
- Comprehensive risk coverage
- Quantified impact/likelihood
- Actionable mitigations
- Compliance verification
- Edge case documentation

---

## 4. Estimation/Scope Analyst

**Role**: Create project timeline and effort estimates

**Responsibilities**:
- Define project phases
- Create milestones
- Estimate effort ranges
- Sequence dependencies
- Document assumptions

**Estimation Focus**:
- Task decomposition
- Effort estimation
- Resource planning
- Timeline creation
- Dependency mapping

**Output Format**:
```yaml
estimation_breakdown:
  project_phases:
    - phase_id: "PHASE-1"
      name: "Foundation"
      description: "Base infrastructure"
      deliverables:
        - "Deliverable with acceptance criteria"
      tasks:
        - task_id: "T-001"
          description: "Task description"
          effort_range:
            optimistic: "hours"
            realistic: "hours"
            pessimistic: "hours"
          dependencies: ["T-000"]
          assigned_to: "Role/Team"
      duration_range:
        min: "days"
        expected: "days"
        max: "days"

  milestones:
    - id: "M-001"
      name: "Milestone name"
      description: "What's achieved"
      target_date: "YYYY-MM-DD"
      dependencies: ["PHASE-1"]
      success_criteria:
        - "Measurable criterion"
      risks:
        - "Risk to achieving"

  dependency_map:
    critical_path:
      - sequence: ["T-001", "T-002", "T-005"]
        total_duration: "days"
    parallel_tracks:
      - track: "Frontend"
        tasks: ["T-003", "T-004"]
      - track: "Backend"
        tasks: ["T-006", "T-007"]

  resource_requirements:
    - role: "Developer|Designer|QA"
      quantity: "number"
      duration: "weeks"
      skills: ["Required skills"]
      availability: "percentage"

  effort_summary:
    total_effort:
      optimistic: "person-days"
      realistic: "person-days"
      pessimistic: "person-days"
    confidence_level: "percentage"
    contingency: "percentage buffer"

  assumptions:
    - category: "scope|resources|technical|timeline"
      assumption: "What we're assuming"
      impact_if_invalid: "What happens if wrong"
      validation: "How to verify"

  constraints:
    - type: "deadline|budget|resource|technical"
      description: "Constraint"
      impact: "How it affects plan"
      mitigation: "How to manage"
```

**Quality Criteria**:
- Realistic estimates
- Clear dependencies
- Identified critical path
- Documented assumptions
- Risk-adjusted timeline

---

## 5. Lead Reviewer

**Role**: Consolidate and validate parallel analysis outputs

**Responsibilities**:
- Reconcile conflicting recommendations
- Identify gaps in analysis
- Validate completeness
- Ensure consistency
- Provide synthesis guidance

**Review Focus**:
- Cross-validation
- Conflict resolution
- Gap analysis
- Quality assurance
- Integration points

**Output Format**:
```yaml
review_summary:
  reconciliation:
    conflicts_identified:
      - conflict_id: "C-001"
        source_1:
          agent: "Requirements"
          finding: "Requirement X"
        source_2:
          agent: "Architecture"
          finding: "Contradicting design Y"
        resolution:
          decision: "Chosen approach"
          rationale: "Why this resolution"
          impact: "Effect on plan"

  completeness_check:
    covered_areas:
      - area: "Requirements"
        completeness: "percentage"
        quality: "high|medium|low"
      - area: "Architecture"
        completeness: "percentage"
        quality: "high|medium|low"

    gaps_identified:
      - gap: "Missing analysis area"
        severity: "critical|high|medium|low"
        recommendation: "How to address"
        owner: "Who should address"

  consistency_validation:
    - check: "Requirement-Architecture alignment"
      status: "aligned|misaligned"
      issues:
        - "Specific inconsistency"
      resolution:
        - "How to fix"

  quality_assessment:
    overall_score: "percentage"
    strengths:
      - "Well-analyzed area"
    weaknesses:
      - "Area needing improvement"
    recommendations:
      - priority: "high|medium|low"
        action: "Specific improvement"

  synthesis_guidance:
    structure_recommendations:
      - "How to organize plan.md"
    priority_order:
      - "Most important findings first"
    emphasis_areas:
      - "Critical points to highlight"
    integration_notes:
      - "How to merge parallel outputs"

  open_questions:
    - question: "Unresolved issue"
      context: "Why important"
      options: ["Possible approaches"]
      recommendation: "Suggested resolution"
```

**Quality Criteria**:
- All conflicts resolved
- Gaps clearly identified
- Consistency verified
- Quality standards met
- Clear synthesis guidance

---

## 6. Lead Synthesizer

**Role**: Create unified planning artifacts from parallel analyses

**Responsibilities**:
- Generate plan.md document
- Create planning-summary.md
- Integrate all findings
- Ensure narrative coherence
- Apply formatting standards

**Synthesis Focus**:
- Document structure
- Content integration
- Narrative flow
- Visual presentation
- Cross-referencing

**Output Format**:

### plan.md Structure
```markdown
# Technical Plan

## Executive Summary
[High-level overview of approach]

## Requirements Analysis
[From Requirements Analyst]

## Architecture Design
### System Architecture
[From Solution Architect]

### Component Design
[Detailed component specifications]

### Data Model
[Entity relationships and schemas]

## Risk Assessment
### Identified Risks
[From Risk Analyst]

### Mitigation Strategies
[Detailed mitigation plans]

## Implementation Plan
### Phase 1: [Name]
[From Estimation Analyst]
- Duration: X weeks
- Deliverables: [List]
- Dependencies: [List]

### Phase 2: [Name]
[Continued phases]

## Success Metrics
[Measurable objectives and KPIs]

## Dependencies
[Internal and external dependencies]

## Timeline
[Gantt chart or timeline visualization]

## Appendices
### A. Alternative Approaches
### B. Technical Specifications
### C. Compliance Requirements
```

### planning-summary.md Structure
```markdown
# Planning Summary

## Feature Overview
[Brief description]

## Key Decisions
- Decision 1: [What and why]
- Decision 2: [What and why]

## Critical Risks
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [Impact] | [Mitigation] |

## Timeline Summary
- Start: [Date]
- Phase 1 Complete: [Date]
- Phase 2 Complete: [Date]
- Final Delivery: [Date]

## Resource Requirements
- Team: [Size and skills]
- Duration: [Total time]
- Dependencies: [Critical dependencies]

## Recommended Next Steps
1. [Immediate action]
2. [Following action]
3. [Subsequent action]

## Open Questions
- [ ] Question requiring resolution
- [ ] Decision needed

## Approval Status
- [ ] Requirements approved
- [ ] Architecture approved
- [ ] Timeline approved
- [ ] Resources allocated
```

**Quality Criteria**:
- Complete integration
- Logical flow
- Clear formatting
- All sections populated
- Executive-friendly summary

---

## Agent Coordination

### Execution Flow

```
1. PARALLEL PHASE (45-60 seconds)
   ├─ Requirements Analyst: Extract requirements
   ├─ Solution Architect: Design architecture
   ├─ Risk Analyst: Assess risks
   └─ Estimation Analyst: Create timeline

2. REVIEW PHASE (15-20 seconds)
   └─ Lead Reviewer: Reconcile and validate

3. SYNTHESIS PHASE (20-30 seconds)
   └─ Lead Synthesizer: Create documents

4. QA PHASE (10-15 seconds)
   └─ Main Agent: Final validation

5. APPROVAL GATE
   └─ User: Manual approval
```

### Communication Protocol

```yaml
inter_agent_communication:
  shared_context:
    - spec.md
    - quality_checklist
    - request_summary
    - context

  message_format:
    from: "agent_id"
    to: "agent_id|reviewer|synthesizer"
    type: "output|query|clarification"
    content: "message_body"
    priority: "high|medium|low"
```

### Quality Gates

Each agent must meet minimum thresholds:

- **Requirements**: All requirements extracted and prioritized
- **Architecture**: Complete component design
- **Risk**: All major risks identified with mitigations
- **Estimation**: Timeline with confidence levels
- **Review**: >90% completeness score
- **Synthesis**: All sections populated

---

## Success Metrics

### Individual Agent Success

- **Requirements Analyst**: 100% requirement coverage
- **Solution Architect**: Complete architecture definition
- **Risk Analyst**: All critical risks identified
- **Estimation Analyst**: Timeline with dependencies
- **Lead Reviewer**: All conflicts resolved
- **Lead Synthesizer**: Documents generated

### Overall Success

- **Completeness**: >95% coverage of planning aspects
- **Quality**: >85% quality score from reviewer
- **Timeliness**: <5 minutes total execution
- **Approval Rate**: >80% first-pass approval
- **Documentation**: Publication-ready artifacts