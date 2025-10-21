# Parallel Stage Orchestration - Parallel Execution Stages and Dependencies

Execution blueprint for running multiple agents in parallel with clear stage boundaries, review gates, and approval flow.

---

## 1. 🎯 Stage Overview

The workflow contains three major parallel execution blocks:

1. **Stage A: Planning/Spec** (Step 6) - Technical planning
2. **Stage B: Implementation Prep** (Step 9) - Implementation preparation
3. **Stage C: Quality Review** (Step 12) - Quality validation

Each stage follows the same execution pattern but with different agents and outputs

.

## 2. ⚡ Execution Pattern

### 2.1 Parallel Agent Phase

```
Time →
T0: Launch all agents simultaneously
    ├─ Agent 1: Start execution
    ├─ Agent 2: Start execution
    ├─ Agent 3: Start execution
    └─ Agent 4: Start execution

T1-Tn: Agents work independently
    ├─ Agent 1: Processing...
    ├─ Agent 2: Processing...
    ├─ Agent 3: Processing...
    └─ Agent 4: Processing...

Tn: Collect outputs as agents complete
    ├─ Agent 1: ✓ Complete (output_1)
    ├─ Agent 2: ✓ Complete (output_2)
    ├─ Agent 3: ✓ Complete (output_3)
    └─ Agent 4: ✓ Complete (output_4)
```

**Rules**:
- Maximum concurrency: 3 (configurable)
- Timeout per agent: 30 seconds
- Retry on failure: 2 attempts
- Continue with partial results if needed

### 2.2 Review Phase

```
Inputs: [output_1, output_2, output_3, output_4]
    ↓
Lead Reviewer:
- Reconcile conflicts
- Validate completeness
- Resolve contradictions
- Quality check
    ↓
Output: review_summary + synthesis_guidance
```

**Rules**:
- Single reviewer per stage
- Must wait for all parallel agents
- Can proceed with 75% agent success
- Timeout: 15 seconds

### 2.3 Synthesis Phase

```
Inputs: [all_outputs, review_summary, synthesis_guidance]
    ↓
Lead Synthesizer:
- Create primary artifact (plan.md, etc.)
- Generate summary document
- Integrate findings
- Ensure coherence
    ↓
Output: stage_artifacts
```

**Rules**:
- Single synthesizer per stage
- Must wait for review phase
- Creates final stage outputs
- Timeout: 20 seconds

### 2.4 Main Agent QA Phase

```
Inputs: [stage_artifacts]
    ↓
Main Agent:
- Validate alignment with request
- Check completeness
- Verify format/structure
- Resolve open questions
    ↓
Output: final_artifacts + signoff
```

**Rules**:
- Main agent has final authority
- Can request rework
- Adds final touches
- Timeout: 10 seconds

### 2.5 Approval Gate

```
Present: final_artifacts + summary
    ↓
User Decision:
├─ APPROVE → Continue to next step
├─ REJECT → Document reason + stop
└─ MODIFY → Apply changes + re-approve
```

**Rules**:
- Mandatory user approval
- No automatic progression
- Clear approval prompts
- Document rejection reasons

.

## 3. 📋 Stage A: Planning/Spec Details

**Trigger**: `/speckit.plan` command

**Parallel Agents** (Step 6):
1. Requirements Analyst - Extract requirements
2. Solution Architect - Design architecture
3. Risk/Compliance Analyst - Identify risks
4. Estimation/Scope Analyst - Create timeline

**Review**: Lead Reviewer A
- Focus: Technical coherence
- Priority: Architecture decisions
- Key output: Synthesis guidance

**Synthesis**: Lead Synthesizer A
- Creates: plan.md, planning-summary.md
- Focus: Technical narrative
- Structure: Problem → Solution → Implementation

**QA Check**: Main Agent
- Validates: Alignment with spec.md
- Ensures: All sections present
- Resolves: Open questions

**Approval**: "Planning artifacts synthesized. Approve to proceed?"

.

## 4. 🛠️ Stage B: Implementation Prep Details

**Trigger**: Before `/speckit.implement` (Step 9)

**Parallel Agents**:
1. Core Implementer - Design modules
2. Integrations Engineer - Plan adapters
3. Test Engineer - Create test strategy
4. Docs Engineer - Plan documentation

**Review**: Integration Reviewer B
- Focus: Implementation coherence
- Priority: API consistency
- Key output: Integration guidance

**Synthesis**: Lead Synthesizer B
- Creates: implementation_plan.md
- Focus: Execution strategy
- Structure: Approach → Tasks → Dependencies

**QA Check**: Main Agent
- Validates: Buildable plan
- Ensures: Clear task definitions
- Resolves: Technical ambiguities

**Approval**: "Implementation plan ready. Approve to proceed?"

.

## 5. ✅ Stage C: Quality Review Details

**Trigger**: `/speckit.analyze` command (Step 12)

**Parallel Agents**:
1. Completeness Reviewer - Check coverage
2. Feasibility Reviewer - Validate viability
3. Security Reviewer - Assess vulnerabilities
4. Consistency Reviewer - Find contradictions

**Review**: Lead Reviewer C
- Focus: Issue prioritization
- Priority: Critical findings
- Key output: Action items

**Synthesis**: Lead Synthesizer C
- Creates: quality_report.md
- Focus: Findings and recommendations
- Structure: Issues → Impact → Resolution

**QA Check**: Main Agent
- Validates: Actionable findings
- Ensures: Clear priorities
- Resolves: Conflicting assessments

**Approval**: "Quality review complete. Approve to proceed?"

.

## 6. ⚙️ Orchestration Implementation

### 6.1 Coordinator Pattern

```python
class StageCoordinator:
    def execute_stage(self, stage_config):
        # 1. Launch parallel agents
        agent_futures = []
        for agent in stage_config.parallel_agents:
            future = self.launch_agent(agent)
            agent_futures.append(future)

        # 2. Collect results (with timeout)
        results = self.collect_results(
            agent_futures,
            timeout=30,
            min_success_ratio=0.75
        )

        # 3. Review phase
        review_output = self.run_reviewer(
            stage_config.reviewer,
            results
        )

        # 4. Synthesis phase
        synthesis_output = self.run_synthesizer(
            stage_config.synthesizer,
            results + review_output
        )

        # 5. Main agent QA
        final_output = self.main_agent_qa(
            synthesis_output,
            original_request
        )

        # 6. Approval gate
        if not self.get_user_approval(final_output):
            raise ApprovalDenied()

        return final_output
```

### 6.2 Error Handling

```python
def handle_agent_failure(self, agent, error):
    # 1. Retry with exponential backoff
    for attempt in range(2):
        try:
            return self.retry_agent(agent, backoff=2**attempt)
        except:
            continue

    # 2. Use fallback if available
    if agent.has_fallback():
        return agent.run_fallback()

    # 3. Mark as partial failure
    return PartialResult(agent.id, error)

def handle_stage_failure(self, stage, error):
    # 1. Check if we have minimum viable results
    if self.has_minimum_results(stage):
        return self.continue_with_partial(stage)

    # 2. Attempt sequential execution
    if stage.supports_sequential():
        return self.run_sequential(stage)

    # 3. Escalate to user
    raise StageFailure(stage, error)
```

.

## 7. 🚀 Performance Optimization

### 7.1 Concurrency Control

```yaml
concurrency_limits:
  default: 3
  high_complexity: 2
  resource_constrained: 1

  per_stage:
    stage_a: 3  # CPU-bound analysis
    stage_b: 2  # Memory-intensive
    stage_c: 3  # I/O-bound reviews
```

### 7.2 Resource Management

```yaml
resource_allocation:
  agent_memory:
    default: 256MB
    large_context: 512MB

  agent_timeout:
    default: 30s
    complex_analysis: 60s
    simple_check: 10s

  stage_timeout:
    total: 120s
    review: 15s
    synthesis: 20s
    qa: 10s
```

### 7.3 Caching Strategy

```yaml
caching:
  agent_outputs: 15_minutes
  review_results: 10_minutes
  synthesis_artifacts: 30_minutes

  invalidation:
    - spec_change
    - plan_update
    - manual_refresh
```

.

## 8. 📊 Monitoring & Telemetry

### 8.1 Stage Metrics

```yaml
stage_metrics:
  - stage_duration_ms
  - agent_success_rate
  - retry_count
  - partial_failure_rate
  - approval_rate
  - user_modification_rate
```

### 8.2 Agent Metrics

```yaml
agent_metrics:
  - execution_time_ms
  - output_size_bytes
  - confidence_score
  - retry_attempts
  - failure_reason
```

### 8.3 Quality Metrics

```yaml
quality_metrics:
  - synthesis_coherence_score
  - review_coverage_percent
  - qa_modifications_count
  - approval_first_attempt_rate
```

.

## 9. 🎛️ Adaptive Rules

### 9.1 High Complexity Handling

When complexity score > 80:
```yaml
adjustments:
  concurrency: reduce_to_2
  timeouts: increase_by_50%
  review_depth: exhaustive
  synthesis_iterations: 2
  qa_thoroughness: detailed
```

### 9.2 High Uncertainty Handling

When uncertainty score > 70:
```yaml
adjustments:
  add_discovery_step: true
  increase_clarification: true
  add_validation_gates: true
  require_examples: true
  document_assumptions: explicit
```

### 9.3 Resource Constraints

When resources limited:
```yaml
fallback:
  use_sequential: true
  reduce_concurrency: 1
  enable_caching: aggressive
  simplify_outputs: true
  skip_optional: true
```

.

## 10. 🔗 Stage Dependencies

### 10.1 Input Requirements

```yaml
stage_a_requires:
  - spec.md (validated)
  - context (provided)
  - user_approval (step 5)

stage_b_requires:
  - plan.md (from stage_a)
  - spec.md (unchanged)
  - user_approval (step 8)

stage_c_requires:
  - implementation (complete)
  - all_artifacts (current)
  - user_approval (step 11)
```

### 10.2 Output Contracts

```yaml
stage_a_produces:
  required:
    - plan.md
    - planning-summary.md
  optional:
    - research.md
    - data-model.md
    - contracts/

stage_b_produces:
  required:
    - implementation_plan.md
  optional:
    - test_fixtures/
    - api_mocks/

stage_c_produces:
  required:
    - quality_report.md
  optional:
    - coverage_report.html
    - security_scan.json
```

.

## 11. 💡 Best Practices

### 11.1 DO:

- Always wait for approval gates
- Document partial failures
- Preserve agent outputs for debugging
- Use structured logging
- Monitor resource usage

### 11.2 DON'T:

- Skip review/synthesis phases
- Ignore partial failures
- Exceed concurrency limits
- Bypass approval gates
- Lose context between stages

### 11.3 CONSIDER:

- Pre-warming agents for faster start
- Caching common analyses
- Batching related operations
- Progressive enhancement
