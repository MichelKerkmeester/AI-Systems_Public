---
name: speckit_parallel_feature_research
description: Conduct parallel technical research and investigation for SpecKit features. Orchestrates 6 specialized research sub-agents to produce comprehensive research.md documentation through parallel collection, review, and synthesis phases.
---

# SpecKit Feature Research

Execute parallel technical research workflow to produce comprehensive documentation for feature planning and implementation.

## When to Use This Skill

**Use this skill when**:
- Conducting technical investigation for a new feature
- Researching libraries, frameworks, and ecosystem patterns
- Analyzing vendor solutions and alternatives
- Evaluating technical feasibility and costs
- Documenting platform constraints and limitations
- Creating comprehensive research documentation

**Do NOT use this skill for**:
- Full SpecKit workflow execution (use speckit-parallel-complete)
- Simple command recommendations (use speckit-command-guide)
- Implementation without research
- Writing specs without investigation

## Architecture Overview

This skill implements the sk_p__feature_research.yaml workflow with 6 specialized research sub-agents executing in parallel.

### Research Workflow Steps

1. **Request Analysis** - Define research scope and goals
2. **Pre-work Review** - Review AGENTS.md, code standards
3. **Parallel Research Block** - 4 researchers collect data
4. **Review Phase** - Lead Reviewer deduplicates and ranks
5. **Synthesis Phase** - Lead Synthesizer creates research.md
6. **Main Agent QA** - Final quality review and polish
7. **Solution Design** - Architecture and integration patterns
8. **Research Compilation** - Complete documentation

### The 6 Research Sub-Agents

1. **Web/Ecosystem Researcher**
   - Libraries and frameworks
   - GitHub repos and issues
   - Community patterns
   - Ecosystem trends

2. **Academic/Docs Researcher**
   - Standards and RFCs
   - Official documentation
   - Academic papers
   - Canonical patterns

3. **Competitive/Market Analyst**
   - Vendor solutions
   - Alternative approaches
   - Benchmarks and comparisons
   - Market trends

4. **Feasibility/Cost Analyst**
   - Technical complexity
   - Operational costs
   - Risk assessment
   - Trade-off analysis

5. **Lead Reviewer**
   - Deduplication
   - Relevance ranking
   - Contradiction resolution
   - Citation validation

6. **Lead Synthesizer**
   - Document generation
   - Section organization
   - Findings integration
   - Markdown formatting

## Execution Model

### Parallel Research Pattern

```
┌─────────────────────────────────┐
│   Parallel Research Execution    │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐   │
│  │Web │ │Docs│ │Mkt │ │Feas│   │ ← Execute in parallel
│  └────┘ └────┘ └────┘ └────┘   │
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│         Review Phase             │ ← Lead Reviewer deduplicates
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│        Synthesis Phase           │ ← Lead Synthesizer creates document
└─────────────────────────────────┘
                ↓
┌─────────────────────────────────┐
│      Main Agent QA Phase         │ ← Final polish and validation
└─────────────────────────────────┘
```

## Research Document Structure

The skill produces a comprehensive `research.md` with these sections:

**Note**: This is a high-level overview. For the complete section specifications with all subsections and required fields, see [sk_p__feature_research.yaml lines 217-289](../../../b_prompts/github_spec_kit/parallel_agents/sk_p__feature_research.yaml#L217-L289).

### Core Sections

**Investigation Report**
- Request summary
- Current behavior analysis
- Key findings
- Recommendations

**Architecture Analysis**
- System components
- Data flow patterns
- Integration points
- Dependencies

**Technical Specifications**
- API documentation
- Attribute reference
- Event contracts
- State management

**Implementation Guide**
- Markup requirements
- JavaScript implementation
- CSS specifications
- Configuration options

### Supporting Sections

**Constraints & Limitations**
- Platform limitations
- Security restrictions
- Performance boundaries
- Browser compatibility

**Integration Patterns**
- Third-party services
- Authentication handling
- Error management
- Retry strategies

**Testing & Debugging**
- Test strategies
- Debugging approaches
- E2E examples
- Diagnostic tools

**Performance & Security**
- Optimization tactics
- Benchmarks
- Data protection
- Spam prevention

## Inputs

### Required Inputs
- **request**: Feature description or research goals
- **spec_folder**: Where to save research.md

### Optional Inputs
- **context**: Additional context for research
- **issues**: Known issues to investigate
- **environment**: Staging URL for live analysis
- **scope**: File scope limitations

## Outputs

### Primary Output
- **research.md**: Complete research documentation
  - Location: `[SPEC_FOLDER]/research.md`
  - Format: Structured markdown
  - Sections: 15+ comprehensive sections

### Research Findings Structure

```yaml
finding:
  title: [descriptive title]
  url: [source URL]
  quote: [relevant excerpt]
  finding: [key insight]
  assessment: [evaluation]
  confidence: [high/medium/low]
```

## Parallel Execution Details

### Concurrency Settings
- **Default**: 3 parallel agents
- **High complexity**: 2 parallel agents
- **Fallback**: Sequential execution

### Quality Controls
- Deduplication of findings
- Citation verification
- Contradiction flagging
- Completeness validation

## Integration Points

### With Chrome DevTools
- Test API endpoints
- Validate approaches
- Measure performance impact
- Verify compatibility

### With SpecKit Workflow
- Research before `/speckit.specify`
- Inform technical planning
- Support implementation decisions
- Document constraints early

### With Other Skills
- **speckit-command-guide**: Recommends when to research
- **speckit-parallel-complete**: Uses research for full workflow
- **speckit-plan-spec**: Leverages research for planning

## Adaptive Rules

**Note**: For complete adaptive rule specifications, complexity scoring, and execution mode details, see [references/adaptive-rules.md](references/adaptive-rules.md).

### Low Signal Handling
When research yields limited results:
- Broaden search queries
- Include secondary sources
- Expand to related domains
- Document gaps explicitly

### High Uncertainty
When findings are contradictory:
- Add clarification pass
- Document conflicting sources
- Provide multiple options
- Highlight trade-offs

### Fallback Strategy
If parallel execution fails:
- Run agents sequentially
- Maintain review/synthesis phases
- Document degraded mode
- Continue with partial results

## Quality Standards

### Documentation Requirements
- Production-ready examples
- Defensive programming patterns
- Error handling strategies
- Memory leak prevention
- SPA compatibility

### Code Examples
- Working snippets
- Proper error handling
- Performance optimized
- Accessibility compliant
- Browser compatible

### Analysis Depth
- Edge cases covered
- Failure modes documented
- Recovery strategies defined
- Monitoring approaches specified

## Performance Characteristics

**Note**: Performance varies based on research scope, available sources, and system resources.

- **Execution**: Variable based on research depth and source availability
- **Parallel phase**: Multiple researchers execute concurrently
- **Review/synthesis**: Sequential refinement after parallel collection
- **Document generation**: Comprehensive markdown output
- **Output size**: 50-150KB markdown (typical)

## Error Handling

### Retry Policy
- **Max retries**: 2 per agent
- **Backoff**: Exponential
- **Targeted**: Only failed agents

### Recovery Actions
- Use cached results if available
- Continue with partial findings
- Document missing research areas
- Provide fallback recommendations

## Limitations

- **Research scope**: Technical/implementation focus
- **Sources**: Public information only
- **Language**: English sources primarily
- **Real-time**: No live system monitoring
- **Dependencies**: Requires internet access

## Success Metrics

**Note**: Target quality benchmarks for research completeness and accuracy.

- **Coverage**: >80% of research areas
- **Citations**: >20 validated sources
- **Contradictions**: <10% unresolved
- **Completeness**: All sections populated
- **Quality score**: >85% validation pass

## Version

**Current Version**: 1.0.0
**Based On**: sk_p__feature_research.yaml
**Created**: 2025-10-18
**Architecture**: Parallel research orchestration

---

## References

- Source: `/b_prompts/github_spec_kit/parallel_agents/sk_p__feature_research.yaml`
- Integration: Works with all SpecKit skills
- Output: Comprehensive research.md documentation