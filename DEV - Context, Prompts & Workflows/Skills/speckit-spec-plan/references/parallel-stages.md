# Parallel Planning Orchestration - Parallel Execution Stages and Dependencies

Parallel orchestration for planning analysis with clear stages, review gates, and approval checkpoints.

---

## 1. 🎯 Stage Overview

The planning workflow contains one major parallel execution block:

**Planning Analysis Stage** (Step 6) - Parallel specialist analyses for requirements, architecture, risk, and estimation

This stage follows a specific execution pattern optimized for comprehensive planning with manual approval gates

.

## 2. ⚡ Execution Pattern

### 2.1 Parallel Analysis Phase

```
Launch →
T0: Launch all analyst agents simultaneously
    ├─ Requirements Analyst: Start
    ├─ Solution Architect: Start
    ├─ Risk/Compliance Analyst: Start
    └─ Estimation/Scope Analyst: Start

Analyze →
    ├─ Requirements: Extracting requirements, constraints...
    ├─ Architecture: Designing components, interfaces...
    ├─ Risk: Identifying risks, mitigations...
    └─ Estimation: Creating milestones, estimates...

Complete →
    ├─ Requirements: ✓ (requirements_dossier)
    ├─ Architecture: ✓ (architecture_design)
    ├─ Risk: ✓ (risk_assessment)
    └─ Estimation: ✓ (estimation_breakdown)
```

**Rules**:
- Maximum concurrency: 3 (configurable)
- Retry on failure: 2 attempts
- Continue with partial results if needed
- Minimum viable: 3 of 4 analysts (requirements + 2 others)

### 2.2 Review Phase

```
Inputs: [requirements, architecture, risks, estimates]
    ↓
Lead Reviewer:
- Reconcile conflicts
- Validate completeness
- Ensure consistency
- Identify open questions
- Quality check
    ↓
Output: synthesis_guidance + review_notes + reconciliation
```

**Rules**:
- Single reviewer reconciles all analyses
- Must wait for all parallel analysts
- Can proceed with 75% analyst success
- Focus: Conflict resolution and completeness

### 2.3 Synthesis Phase

```
Inputs: [all_analyses, review_guidance, reconciliation_notes]
    ↓
Lead Synthesizer:
- Create plan.md
- Generate planning-summary.md
- Integrate findings
- Ensure coherence
- Structure narrative
    ↓
Output: plan.md + planning-summary.md
```

**Rules**:
- Single synthesizer creates documents
- Must wait for review phase
- Creates cohesive planning artifacts
- Follows SpecKit template structure

### 2.4 Main Agent QA Phase

```
Inputs: [plan.md, planning-summary.md]
    ↓
Main Agent:
- Validate alignment with spec
- Check completeness
- Verify format/sections
- Resolve open questions
- Final polish
    ↓
Output: final_planning_artifacts + signoff
```

**Rules**:
- Main agent has final authority
- Ensures all sections present
- Validates technical soundness
- Prepares for user approval

### 2.5 Approval Gate

```
Present: [plan.md, planning-summary.md]
    ↓
User Decision:
├─ APPROVE → Continue to implementation
├─ REJECT → Document reason + stop
└─ MODIFY → Apply changes + re-approve
```

**Rules**:
- Mandatory user approval before proceeding
- No automatic progression
- Clear approval prompts
- Document rejection reasons

.

## 3. 🔀 Planning Analysis Stage Details

**Parallel Analysts** (Step 6):

1. **Requirements Analyst**
   - Focus: Requirements, constraints, dependencies
   - Output: Requirements dossier with success metrics
   - Deliverables: Acceptance criteria, dependency map

2. **Solution Architect**
   - Focus: Components, interfaces, data flow
   - Output: Architecture design with alternatives
   - Deliverables: Component diagrams, pattern selection

3. **Risk/Compliance Analyst**
   - Focus: Risks, edge cases, non-functionals
   - Output: Risk assessment with mitigations
   - Deliverables: Risk register, compliance requirements

4. **Estimation/Scope Analyst**
   - Focus: Milestones, sequencing, effort ranges
   - Output: Project estimation with phases
   - Deliverables: Timeline, resource needs, assumptions

**Review**: Lead Reviewer
- Focus: Cross-analysis reconciliation
- Priority: Conflict resolution
- Key output: Synthesis guidance

**Synthesis**: Lead Synthesizer
- Creates: plan.md, planning-summary.md
- Focus: Cohesive planning narrative
- Structure: Problem → Approach → Phases → Risks

**QA Check**: Main Agent
- Validates: Planning completeness
- Ensures: Alignment with specification
- Resolves: Outstanding questions

**Approval**: User
- Reviews: Complete planning package
- Decides: Proceed, modify, or reject
- Controls: Workflow progression

.

## 4. ⚙️ Orchestration Implementation

### 4.1 Coordinator Pattern

```python
class PlanningCoordinator:
    def execute_planning(self, planning_config):
        # 1. Launch parallel analysts
        analyst_futures = []
        for analyst in planning_config.parallel_analysts:
            future = self.launch_analyst(analyst)
            analyst_futures.append(future)

        # 2. Collect analyses
        analyses = self.collect_analyses(
            analyst_futures,
            min_success_ratio=0.75
        )

        # 3. Review phase (reconcile)
        review_output = self.run_lead_reviewer(
            planning_config.reviewer,
            analyses
        )

        # 4. Synthesis phase (create artifacts)
        planning_docs = self.run_synthesizer(
            planning_config.synthesizer,
            analyses + review_output
        )

        # 5. Main agent QA
        final_docs = self.main_agent_qa(
            planning_docs,
            spec_md
        )

        # 6. User approval gate
        if not self.get_user_approval(final_docs):
            raise ApprovalDenied()

        return final_docs
```

### 4.2 Error Handling

```python
def handle_analyst_failure(self, analyst, error):
    # 1. Retry with clarified scope
    for attempt in range(2):
        try:
            return self.retry_analyst(
                analyst,
                clarify_scope=True
            )
        except:
            continue

    # 2. Use simplified analysis
    return SimplifiedAnalysis(analyst.id, error)

def handle_conflicting_analyses(self, analyses):
    # 1. Check if conflicts are reconcilable
    if self.can_reconcile(analyses):
        return self.reconcile_automatically(analyses)

    # 2. Document conflicts for review
    if self.has_major_conflicts(analyses):
        return self.escalate_to_reviewer(analyses)

    # 3. Proceed with documented conflicts
    return self.proceed_with_conflicts_noted(analyses)
```

.

## 5. 🚀 Performance Optimization

### 5.1 Concurrency Control

```yaml
concurrency_limits:
  default: 3
  high_complexity: 2
  low_complexity: 4

  per_analyst:
    requirements: 3  # Document analysis
    architecture: 2  # Design-intensive
    risk: 3  # Checklist-based
    estimation: 2  # Calculation-heavy
```

### 5.2 Analysis Depth

```yaml
depth_by_complexity:
  low_complexity:
    requirements: basic
    architecture: standard
    risk: basic
    estimation: ranges_only

  medium_complexity:
    requirements: thorough
    architecture: comprehensive
    risk: detailed
    estimation: phased_estimates

  high_complexity:
    requirements: exhaustive
    architecture: with_alternatives
    risk: comprehensive_mitigations
    estimation: detailed_breakdown
```

.

## 6. 📊 Monitoring & Telemetry

### 6.1 Planning Metrics

```yaml
planning_metrics:
  - analysis_completeness
  - conflict_resolution_rate
  - approval_rate
  - iteration_count
  - requirement_coverage
```

### 6.2 Analyst Metrics

```yaml
analyst_metrics:
  - analysis_depth
  - conflict_generation
  - completeness_score
  - retry_attempts
  - coherence_rating
```

### 6.3 Quality Metrics

```yaml
quality_metrics:
  - requirement_alignment
  - architectural_soundness
  - risk_coverage
  - estimation_confidence
  - stakeholder_satisfaction
```
.


## 7. 🎛️ Adaptive Rules

### 7.1 High Complexity Handling

When complexity > 70:
```yaml
adjustments:
  concurrency: 2
  analysis_depth: exhaustive
  iterations: 2
  approval_gates: strict
  review_depth: comprehensive
```

### 7.2 Low Clarity Handling

When requirement_clarity < 40:
```yaml
adjustments:
  add_discovery_phase: true
  clarification: comprehensive
  validation: extensive
  iterations: 2+
  stakeholder_involvement: high
```

### 7.3 High Uncertainty

When uncertainty > 70:
```yaml
adjustments:
  add_prototyping: recommended
  document_assumptions: explicit
  provide_options: multiple_paths
  risk_analysis: deep
  contingency_planning: detailed
```

.

## 8. 🔗 Planning Dependencies

### 8.1 Input Requirements

```yaml
planning_requires:
  - spec.md (validated)
  - context (provided)
  - quality_checklist.md
  - user_approval (step 4)
  optional:
    - research.md
    - existing_architecture
    - stakeholder_input
```

### 8.2 Output Contract

```yaml
planning_produces:
  required:
    - plan.md (technical approach)
    - planning-summary.md (executive summary)
  sections_plan_md:
    - technical_approach
    - implementation_phases
    - risk_assessment
    - success_metrics
    - dependencies
    - assumptions
  sections_summary:
    - feature_overview
    - technical_approach
    - dependencies_identified
    - risks_and_mitigation
    - recommended_next_steps
```

.

## 9. 🏁 Workflow Termination

This workflow terminates after planning (step 7):

```yaml
termination:
  after_step: 7
  message: "Planning phase completed successfully"
  next_steps:
    - Review planning documentation
    - Approve technical approach
    - Use implementation workflow for execution
```

.

## 10. ✅ Best Practices

### 10.1 DO:

- Start with why (business value)
- Involve stakeholders early
- Document assumptions explicitly
- Consider alternatives
- Define success metrics

### 10.2 DON'T:

- Skip stakeholder alignment
- Ignore constraints
- Over-commit on estimates
- Leave risks unmitigated
- Assume requirements are static

### 10.3 CONSIDER:

- Iterative refinement for uncertain areas
- Proof-of-concepts for risky approaches
- Phased planning for large initiatives
- External review for critical decisions
- Progressive detail as clarity increases
