# Prompt Improver - Patterns, Enhancements & Evaluation - v0.101

Advanced prompt engineering system with comprehensive frameworks, evaluation methodology, and systematic enhancement patterns.

- **DEPTH PROCESSING:** See → **Prompt - DEPTH Thinking Framework.md** for methodology
- **OUTPUT FORMATS:** See dedicated guides for JSON, YAML, and Markdown specifications

---

## 📚 Table of Contents

### PART 1: FRAMEWORKS & PATTERNS
1. [🎯 Framework Library & Selection](#1-framework-library--selection)
2. [🔧 Framework Deep Dives](#2-framework-deep-dives)
3. [🧠 Advanced Pattern Combinations](#3-advanced-pattern-combinations)
4. [🎨 Framework Optimization Strategies](#4-framework-optimization-strategies)

### PART 2: ENHANCEMENT PATTERNS
5. [🚀 Systematic Enhancement Methodology](#5-systematic-enhancement-methodology)
6. [🔄 Pattern-Based Refinements](#6-pattern-based-refinements)
7. [💎 Excellence Patterns](#7-excellence-patterns)
8. [🛠️ Recovery & Repair Protocols](#8-recovery--repair-protocols)

### PART 3: EVALUATION & SCORING
9. [✅ CLEAR Evaluation Mastery](#9-clear-evaluation-mastery)
10. [📈 Advanced Scoring Techniques](#10-advanced-scoring-techniques)
11. [🔍 Weakness Detection & Analysis](#11-weakness-detection--analysis)

### PART 4: PRACTICAL IMPLEMENTATION
12. [📊 Use Case Templates](#12-use-case-templates)
13. [⚙️ Framework Combinations](#13-framework-combinations)
14. [🎓 Mastery Principles](#14-mastery-principles)
15. [🎏 Quick Reference Card](#15-quick-reference-card)

---

## PART 1: FRAMEWORKS & PATTERNS

<a id="1-framework-library--selection"></a>

### 1. 🎯 Framework Library & Selection

#### Complete Framework Matrix with Use Cases

| Framework | Elements | Best For | Avoid When | Success Rate | Combination Potential |
|-----------|----------|----------|------------|--------------|----------------------|
| **RCAF** | Role, Context, Action, Format | 80% of prompts, general tasks | Over-complex scenarios | 92% | High - base for combinations |
| **COSTAR** | Context, Objective, Style, Tone, Audience, Response | Content creation, communication | Technical specifications | 94% | Medium - specific use |
| **RACE** | Role, Action, Context, Execute | Urgent tasks, quick iterations | Detailed requirements | 88% | High - good for speed |
| **CIDI** | Context, Instructions, Details, Input | Process documentation, tutorials | Creative exploration | 90% | Low - self-contained |
| **TIDD-EC** | Task, Instructions, Do's, Don'ts, Examples, Context | Quality-critical, compliance | Brainstorming | 93% | Medium - pairs with CoT |
| **CRISPE** | Capacity, Insight, Statement, Personality, Experiment | Strategy, exploration | Routine tasks | 87% | High - good for iteration |
| **CRAFT** | Context, Role, Action, Format, Target | Complex projects, planning | Simple queries | 91% | Low - already comprehensive |

#### Intelligent Framework Selection Algorithm

```yaml
select_optimal_framework:
  description: "Enhanced framework selection with pattern recognition"
  input: [task_analysis]
  
  process:
    analyze_characteristics:
      complexity:
        function: assess_complexity
        scale: 1_to_10
      urgency:
        function: detect_urgency
        boolean: true_false
      audience_specific:
        function: has_audience_requirements
        boolean: true_false
      creative_element:
        function: requires_creativity
        boolean: true_false
      precision_critical:
        function: needs_high_precision
        boolean: true_false
      iterative_nature:
        function: requires_iteration
        boolean: true_false
      compliance_needs:
        function: has_compliance_requirements
        boolean: true_false
      multi_stakeholder:
        function: involves_multiple_parties
        boolean: true_false
    
    score_frameworks:
      rcaf:
        base_score: 5
        modifiers:
          - if: "complexity <= 6"
            add: 5
          - if: "not audience_specific"
            add: 3
          - if: "complexity in [4,5,6]"
            add: 2
      
      costar:
        base_score: 3
        modifiers:
          - if: audience_specific
            add: 7
          - if: creative_element
            add: 5
          - if: multi_stakeholder
            add: 3
      
      race:
        base_score: 2
        modifiers:
          - if: urgency
            add: 8
          - if: "complexity <= 3"
            add: 5
          - if: precision_critical
            subtract: 5
      
      tidd_ec:
        base_score: 3
        modifiers:
          - if: precision_critical
            add: 7
          - if: compliance_needs
            add: 5
          - if: "complexity >= 6"
            add: 3
    
    select_best:
      method: highest_score
      normalize_confidence: "score / 20"
      get_alternative: second_highest
    
  output:
    primary: selected_framework
    confidence: normalized_score
    alternative: second_best_framework
    reasoning: selection_logic_explanation
```

---

<a id="2-framework-deep-dives"></a>

### 2. 🔧 Framework Deep Dives

#### RCAF Mastery Patterns

**Pattern 1: Layered RCAF for Complex Contexts**
```yaml
layered_rcaf:
  role:
    primary: "[Main expertise]"
    secondary: "[Supporting skill]"
    domain: "[Specific knowledge area]"
  
  context:
    immediate: "[Current situation]"
    historical: "[Relevant background]"
    constraints: "[Limitations and boundaries]"
  
  action:
    primary: "[Main task]"
    method: "[How to accomplish]"
    outcome: "[Expected result]"
  
  format:
    structure: "[Organization pattern]"
    style: "[Tone and approach]"
    deliverables: "[Specific outputs]"
```

**Pattern 2: RCAF with Embedded Metrics**
```yaml
metric_rcaf:
  role: "[Expert] measured by [KPI]"
  context: "[Situation] with success defined as [metric]"
  action: "[Task] achieving minimum [threshold]"
  format: "[Output] demonstrating [measurable quality]"
```

**Pattern 3: Conditional RCAF**
```yaml
conditional_rcaf:
  role: "[Expert who adapts based on conditions]"
  context:
    if_condition_a: "[context variant A]"
    else: "[context variant B]"
  action:
    when_trigger: "[action variant A]"
    otherwise: "[action variant B]"
  format: "Adapt output based on [criteria]"
```

#### COSTAR Enhancement Techniques

**Technique 1: Audience Layering**
```yaml
audience_layers:
  primary:
    profile: "[Main reader detailed description]"
    concerns: "[Primary interests]"
    knowledge: "[Technical level]"
  
  secondary:
    stakeholders: "[Other involved parties]"
    concerns: "[Secondary interests]"
    influence: "[Decision power]"
  
  adaptation:
    content: "Tailor to primary while acknowledging secondary"
    tone: "Balance formality levels"
    detail: "Adjust technical depth"
```

**Technique 2: Style-Tone Matrix**
```yaml
style_tone_combinations:
  formal_empathetic:
    use_for: "Crisis communication"
    balance: "Authority with understanding"
  
  technical_enthusiastic:
    use_for: "Product launches"
    balance: "Expertise with excitement"
  
  casual_authoritative:
    use_for: "Educational content"
    balance: "Approachability with credibility"
  
  creative_professional:
    use_for: "Marketing materials"
    balance: "Innovation with reliability"
```

#### TIDD-EC Excellence Patterns

**Pattern 1: Cascading Examples**
```yaml
cascading_examples:
  basic:
    description: "Simple case"
    input: "[basic input]"
    output: "[basic output]"
    explanation: "[why this works]"
  
  intermediate:
    description: "Typical case"
    input: "[standard input]"
    output: "[standard output]"
    explanation: "[common patterns]"
  
  advanced:
    description: "Complex case"
    input: "[complex input]"
    output: "[complex output]"
    explanation: "[advanced handling]"
  
  edge_case:
    description: "Unusual scenario"
    input: "[edge input]"
    output: "[edge output]"
    explanation: "[special considerations]"
  
  anti_pattern:
    description: "What not to do"
    input: "[bad input]"
    output: "[bad output]"
    explanation: "[why to avoid]"
```

---

<a id="3-advanced-pattern-combinations"></a>

### 3. 🧠 Advanced Pattern Combinations

#### Framework Fusion Patterns

**RCAF + CoT (Chain of Thought)**
```yaml
rcaf_cot_fusion:
  role: "[Expert] who thinks systematically"
  context: "[Situation requiring reasoning]"
  action:
    solve_by:
      step_1:
        decompose: "[Break down problem]"
        reasoning: "[Why this decomposition]"
      step_2:
        analyze: "[Examine each component]"
        reasoning: "[Analysis approach]"
      step_3:
        synthesize: "[Combine insights]"
        reasoning: "[Integration logic]"
      step_4:
        validate: "[Verify solution]"
        reasoning: "[Validation criteria]"
  format: "Show reasoning at each step with final answer highlighted"
```

**COSTAR + ReAct (Reasoning-Action)**
```yaml
costar_react_fusion:
  context: "[Initial situation]"
  objective: "[Goal requiring iteration]"
  style: "Analytical with visible reasoning"
  tone: "Professional problem-solver"
  audience: "[Stakeholders needing transparency]"
  response:
    cycle_format:
      iteration:
        thought: "[Current reasoning]"
        action: "[What to do based on thought]"
        observation: "[Result of action]"
      repeat_until: "[Success criteria met]"
      max_iterations: 5
```

**TIDD-EC + Few-Shot**
```yaml
tidd_ec_fewshot:
  task: "[Primary objective]"
  instructions: "Learn from examples then apply"
  dos:
    - "Follow patterns from examples"
    - "Maintain consistency"
    - "Adapt to context"
  donts:
    - "Deviate from established patterns"
    - "Ignore edge cases"
  examples:
    case_1:
      input: "[example input]"
      output: "[example output]"
      explanation: "[pattern demonstration]"
    case_2:
      input: "[example input]"
      output: "[example output]"
      explanation: "[pattern reinforcement]"
    case_3:
      input: "[example input]"
      output: "[example output]"
      explanation: "[variation handling]"
  context: "Apply learned patterns to new inputs"
```

---

<a id="4-framework-optimization-strategies"></a>

### 4. 🎨 Framework Optimization Strategies

#### Token Optimization Techniques

```yaml
optimize_framework_tokens:
  description: "Reduce token usage while maintaining effectiveness"
  input: [framework, content]
  
  strategies:
    rcaf_optimization:
      role:
        method: extract_key_expertise
        remove: redundant_qualifiers
      context:
        method: filter_essential_only
        remove: non_critical_details
      action:
        method: single_clear_verb
        remove: multiple_actions
      format:
        method: structure_only
        remove: style_descriptions
    
    costar_optimization:
      merge_overlapping:
        combine: [style, tone]
        into: style_tone
      audience:
        method: profile_key_traits
        limit: 3_essential_characteristics
      response:
        method: simplify_format
        remove: redundant_specifications
    
    race_optimization:
      ultra_minimal: true
      single_line_per_element: true
      abbreviations_allowed: true
      max_tokens_per_element: 10
  
  output: optimized_framework
```

**Framework Switching for Efficiency:**
```yaml
efficiency_switching:
  rules:
    - if: "token_count > threshold"
      and: "complexity < 4"
      then:
        switch: "CRAFT → RCAF"
        savings: "15-20%"
    
    - if: "token_count > threshold"
      and: "complexity < 2"
      then:
        switch: "RCAF → RACE"
        savings: "additional 5-10%"
    
    - if: "token_count > threshold"
      and: "precision not critical"
      then:
        switch: "TIDD-EC → RCAF"
        savings: "12-15%"
```

---

## PART 2: ENHANCEMENT PATTERNS

<a id="5-systematic-enhancement-methodology"></a>

### 5. 🚀 Systematic Enhancement Methodology

#### The Enhancement Pipeline

```yaml
enhancement_pipeline:
  description: "Systematic prompt improvement process"
  
  stages:
    - structural_enhancement
    - clarity_enhancement
    - precision_enhancement
    - efficiency_enhancement
    - reusability_enhancement
  
  methods:
    structural_enhancement:
      description: "Improve organization and framework"
      input: [prompt]
      
      process:
        apply_framework:
          check: has_framework
          if_missing: apply_best_framework
          log: "Applied [framework] framework"
        
        reorganize_elements:
          check: organization_quality
          if_poor: reorganize_logically
          log: "Restructured for logical flow"
      
      output: [enhanced_prompt, enhancement_log]
    
    clarity_enhancement:
      description: "Improve expression and understanding"
      input: [prompt]
      
      process:
        simplify_complex:
          find: complex_sentences
          for_each: sentence
            action: simplify_sentence
            log: "Simplified: [original] → [simplified]"
        
        remove_ambiguity:
          find: ambiguous_terms
          for_each: term
            action: clarify_term
            context: prompt_context
            log: "Clarified: [term] → [clarification]"
      
      output: [enhanced_prompt, enhancement_log]
    
    precision_enhancement:
      description: "Improve accuracy and specificity"
      input: [prompt]
      
      process:
        add_measurability:
          check: has_measurable_outcomes
          if_missing: add_success_metrics
          log: "Added measurable criteria"
        
        specify_constraints:
          check: has_explicit_constraints
          if_missing: add_constraints
          log: "Added explicit constraints"
      
      output: [enhanced_prompt, enhancement_log]
    
    efficiency_enhancement:
      description: "Optimize token usage"
      input: [prompt]
      
      process:
        remove_redundancy:
          find: redundant_elements
          action: consolidate_or_remove
          log: "Removed redundancy"
        
        compress_verbose:
          find: verbose_sections
          action: compress_while_preserving_meaning
          log: "Compressed verbose sections"
      
      output: [enhanced_prompt, enhancement_log]
    
    reusability_enhancement:
      description: "Make prompt template-ready"
      input: [prompt]
      
      process:
        extract_parameters:
          find: specific_values
          action: convert_to_placeholders
          log: "Parameterized: [value] → [placeholder]"
        
        add_flexibility:
          find: rigid_structures
          action: add_conditional_logic
          log: "Added flexibility options"
      
      output: [enhanced_prompt, enhancement_log]
```

---

<a id="6-pattern-based-refinements"></a>

### 6. 🔄 Pattern-Based Refinements

#### Common Enhancement Patterns

**Pattern: Vague to Specific Transformation**
```yaml
vague_to_specific:
  pattern_name: "Vague to Specific Transformation"
  
  detection:
    triggers:
      - vague_verbs: ["help", "assist", "handle", "deal with"]
      - vague_nouns: ["things", "stuff", "data", "information"]
      - missing_metrics: no_measurable_outcomes
      - missing_scope: no_boundaries_defined
  
  transformation:
    steps:
      - add_role:
          from: "Help analyze"
          to: "Data analyst specializing in [domain]"
      
      - specify_context:
          from: "customer data"
          to: "[Platform] data, [Time period], [N] records"
      
      - define_action:
          from: "analyze and provide insights"
          to: "Identify [X] patterns and segment by [criteria]"
      
      - clarify_format:
          from: "provide results"
          to: "[Format type] with [specific sections]"
  
  impact:
    clear_score_gain: "+15 to +20"
    primary_dimension: "Expression and Logic"
```

**Pattern: Assumption Elimination**
```yaml
assumption_elimination:
  pattern_name: "Assumption Elimination"
  
  detection:
    implicit_references:
      - "our system" # What system?
      - "the usual format" # What format?
      - "standard approach" # What standard?
      - "as discussed" # When discussed?
  
  replacement_map:
    our_system: "[Specific tech stack description]"
    usual_format: "[Exact format specification]"
    standard_approach: "[Specific methodology]"
    as_discussed: "[Reference or full context]"
  
  impact:
    clear_score_gain: "+3 to +5"
    primary_dimension: "Correctness"
```

**Pattern: Scope Boundary Definition**
```yaml
scope_boundaries:
  pattern_name: "Scope Boundary Definition"
  
  additions:
    included:
      prefix: "This includes:"
      items: "[Explicit list of what's in scope]"
    
    excluded:
      prefix: "This excludes:"
      items: "[Explicit list of what's out of scope]"
    
    edge_cases:
      prefix: "Edge cases:"
      handling: "[How to handle boundary scenarios]"
  
  impact:
    clear_score_gain: "+4 to +6"
    primary_dimension: "Logic/Coverage"
```

---

<a id="7-excellence-patterns"></a>

### 7. 💎 Excellence Patterns

#### The 45+ CLEAR Score Patterns

**Excellence Pattern 1: Complete Context Layering**
```yaml
complete_context_layering:
  pattern_name: "Complete Context Layering"
  
  layers:
    environmental:
      description: "Where/when this happens"
      elements: [location, timing, platform, environment]
    
    historical:
      description: "What led to this"
      elements: [background, previous_attempts, lessons_learned]
    
    constraints:
      description: "Limitations"
      elements: [technical, resource, time, regulatory]
    
    resources:
      description: "Available assets"
      elements: [tools, data, team, budget]
    
    dependencies:
      description: "What this relies on"
      elements: [upstream, downstream, external, internal]
    
    stakeholders:
      description: "Who's involved"
      elements: [users, approvers, implementers, affected_parties]
  
  implementation:
    for_each_layer: assess_relevance
    if_relevant: add_to_context
    organize: hierarchical_structure
```

**Excellence Pattern 2: Multi-Level Success Criteria**
```yaml
multi_level_success:
  pattern_name: "Multi-Level Success Criteria"
  
  levels:
    minimum_viable:
      description: "Baseline acceptability"
      threshold: "[Specific minimum requirements]"
      measurement: "[How to measure]"
    
    target:
      description: "Expected outcome"
      threshold: "[Standard success level]"
      measurement: "[Metrics and KPIs]"
    
    excellence:
      description: "Exceptional result"
      threshold: "[Stretch goals]"
      measurement: "[Advanced metrics]"
  
  timeline:
    immediate: "[Quick wins]"
    short_term: "[30-day goals]"
    long_term: "[90+ day goals]"
```

---

<a id="8-recovery--repair-protocols"></a>

### 8. 🛠️ Recovery & Repair Protocols

#### Systematic Error Recovery

```yaml
repair_framework:
  description: "Enhanced REPAIR with pattern learning"
  
  methods:
    recognize:
      description: "Identify all issues"
      input: [prompt]
      
      issue_categories:
        critical: []  # Must fix
        major: []     # Should fix
        minor: []     # Nice to fix
        style: []     # Optional
      
      process:
        load_patterns: error_pattern_library
        for_each: pattern
          if_matches: prompt
          then:
            add_to: "issues[pattern.severity]"
      
      output: categorized_issues
    
    explain:
      description: "Explain impact with examples"
      input: [issues]
      
      for_each_issue:
        generate:
          what: issue_description
          why_matters: impact_explanation
          example_failure: failure_scenario
          fix_preview: solution_preview
      
      output: issue_explanations
    
    propose:
      description: "Generate fix proposals"
      input: [issues, context]
      
      for_each_issue:
        create_proposal:
          issue: issue_reference
          solutions: generate_solution_options
          effort: estimate_effort_required
          impact: estimate_improvement_gain
          priority: calculate_priority_score
      
      sort_by: priority_descending
      output: prioritized_proposals
    
    apply:
      description: "Apply fixes based on strategy"
      input: [prompt, proposals, strategy]
      
      strategies:
        minimal:
          filter: "priority > 8"
          description: "Critical fixes only"
        
        balanced:
          filter: "impact/effort > 2"
          description: "Best ROI fixes"
        
        comprehensive:
          filter: "priority > 3"
          description: "All meaningful fixes"
        
        critical_only:
          filter: "severity == 'critical'"
          description: "Must-fix items only"
      
      process:
        select: "filter(proposals, strategies[strategy])"
        for_each_selected:
          apply: "first_solution_option"
      
      output: enhanced_prompt
    
    iterate:
      description: "Iterate until quality target met"
      input: [prompt, target_score]
      
      configuration:
        max_iterations: 5
        target_clear_score: target_score
      
      process:
        while: "iterations < max AND score < target"
          do:
            - calculate_clear_score
            - recognize_issues
            - propose_fixes
            - apply_fixes
            - increment_iteration
      
      output: [final_prompt, iteration_history]
    
    record:
      description: "Record for pattern learning"
      input: [original, final, history]
      
      learning_record:
        original_prompt: original
        final_prompt: final
        improvement: calculate_improvement
        successful_patterns: extract_patterns
        iterations_needed: history_length
        time_taken: calculate_duration
      
      action: save_to_pattern_library
      output: learning_record
```

---

## PART 3: EVALUATION & SCORING

<a id="9-clear-evaluation-mastery"></a>

### 9. ✅ CLEAR Evaluation Mastery

#### Advanced CLEAR Scoring Methodology

```yaml
calculate_contextual_clear_score:
  description: "Context-aware CLEAR scoring"
  input: [prompt, use_case]
  
  base_weights:
    correctness: 0.20
    logic: 0.20
    expression: 0.30
    arrangement: 0.20
    reuse: 0.10
  
  context_adjustments:
    api_integration:
      correctness: 0.30  # Precision critical
      expression: 0.20   # Less important
    
    creative_writing:
      expression: 0.35   # Clarity paramount
      correctness: 0.15  # Less critical
    
    template_creation:
      reuse: 0.25       # Reusability focus
      logic: 0.15       # Reduced weight
  
  process:
    - determine_context: use_case
    - adjust_weights:
        if: "context_adjustments[use_case]"
        then: apply_adjustments
        else: use_base_weights
    
    - score_dimensions:
        for_each: dimension
          score: score_dimension_contextual
          weight: adjusted_weight
    
    - calculate_total:
        method: weighted_sum
        scale: 50_point_scale
  
  output:
    total: weighted_score
    breakdown: dimension_scores
    weights_used: final_weights
    context: use_case
```

**Dimension Interdependencies:**
```yaml
dimension_relationships:
  expression_arrangement:
    relationship: "Clear language needs good structure"
    correlation: 0.7
  
  logic_correctness:
    relationship: "Complete coverage ensures accuracy"
    correlation: 0.8
  
  arrangement_reuse:
    relationship: "Good structure enables templates"
    correlation: 0.6
  
  expression_correctness:
    relationship: "Clarity prevents misinterpretation"
    correlation: 0.5
```

---

<a id="10-advanced-scoring-techniques"></a>

### 10. 📈 Advanced Scoring Techniques

#### Multi-Pass Scoring

```yaml
multi_pass_scoring:
  description: "Three-pass evaluation for depth"
  
  pass_1_surface:
    name: "Surface Evaluation"
    checks:
      - framework_presence
      - basic_completeness
      - obvious_issues
    depth: shallow
    time: quick
  
  pass_2_deep:
    name: "Deep Analysis"
    checks:
      - ambiguity_detection
      - hidden_assumptions
      - edge_case_coverage
    depth: thorough
    time: moderate
  
  pass_3_interaction:
    name: "Interaction Testing"
    checks:
      - ai_interpretation
      - failure_modes
      - output_predictability
    depth: comprehensive
    time: extensive
  
  aggregation:
    method: weighted_average
    weights:
      pass_1: 0.25
      pass_2: 0.40
      pass_3: 0.35
```

#### Comparative Scoring

```yaml
comparative_clear_scoring:
  description: "Score multiple versions for optimization"
  input: [prompt_versions]
  
  process:
    for_each_version:
      - calculate_clear_score
      - identify_strengths
      - identify_weaknesses
      - calculate_improvement_potential
    
    analysis:
      find_best:
        method: max_by_total_score
      
      extract_patterns:
        from: best_version
        identify: success_factors
      
      generate_path:
        from: all_results
        create: optimization_sequence
  
  output:
    best_version: highest_scoring
    all_results: scored_versions
    success_patterns: extracted_patterns
    optimization_path: improvement_sequence
```

---

<a id="11-weakness-detection--analysis"></a>

### 11. 🔍 Weakness Detection & Analysis

#### Automated Weakness Detection

```yaml
detect_prompt_weaknesses:
  description: "Comprehensive weakness analysis"
  input: [prompt]
  
  weakness_detectors:
    vagueness:
      checks:
        - word_list: ["help", "assist", "some", "various"]
        - unmeasurable_outcomes: no_metrics
        - missing_specifics: lacks_detail
    
    incompleteness:
      checks:
        - missing_framework_elements
        - undefined_terms
        - assumed_knowledge
    
    ambiguity:
      checks:
        - multiple_interpretations
        - pronoun_clarity
        - modifier_attachment
    
    structure:
      checks:
        - logical_flow
        - element_organization
        - hierarchy_clarity
    
    efficiency:
      checks:
        - redundancy
        - token_waste
        - unnecessary_complexity
  
  process:
    for_each_category: in_weakness_detectors
      for_each_check: in_category
        result: execute_check
        if_issues_found:
          add_to: weaknesses[category]
  
  output:
    weaknesses: categorized_issues
    severity: calculated_severity
    priority_fixes: prioritized_list
    estimated_improvement: potential_clear_gain
```

---

## PART 4: PRACTICAL IMPLEMENTATION

<a id="12-use-case-templates"></a>

### 12. 📊 Use Case Templates

#### Software Development Suite

```yaml
api_documentation_template:
  framework: TIDD-EC
  
  task: "Document REST API endpoint for [resource]"
  
  instructions:
    - "Define endpoint (method, path, version)"
    - "List all parameters with types"
    - "Show request/response examples"
    - "Document error codes"
    - "Include rate limits"
  
  dos:
    - "Use consistent formatting"
    - "Include curl examples"
    - "Specify authentication"
    - "Version all changes"
  
  donts:
    - "Expose internal logic"
    - "Use technical jargon without definition"
    - "Skip error documentation"
  
  examples: "[Include 3 real examples]"
  context: "[API version, tech stack, audience]"

code_review_template:
  framework: "RCAF + CoT"
  
  role: "Senior developer reviewing code for production readiness"
  context: "[Language], [Framework], [Project standards]"
  
  action:
    review_thinking:
      - "Functionality: Does it work as intended?"
      - "Performance: Are there bottlenecks?"
      - "Security: Any vulnerabilities?"
      - "Maintainability: Is it readable and documented?"
      - "Testing: Adequate test coverage?"
  
  format: "Structured feedback with severity levels and suggested fixes"
```

#### Data Analysis Suite

```yaml
exploratory_data_analysis:
  framework: COSTAR
  
  context: "Dataset with [N] records, [M] features, [quality issues]"
  objective: "Understand data patterns and prepare for modeling"
  style: "Technical but accessible to stakeholders"
  tone: "Objective and data-driven"
  audience: "Data team and business analysts"
  
  response:
    format: "Jupyter notebook"
    sections:
      - "Data quality report"
      - "Statistical summaries"
      - "Correlation analysis"
      - "Feature importance"
      - "Visualization gallery"
      - "Next steps recommendations"

ab_test_analysis:
  framework: CRAFT
  
  context:
    test: "[Control vs variant description]"
    duration: "[Time period]"
    sample_size: "[N per group]"
    success_metrics: "[Primary and secondary KPIs]"
  
  role: "Statistical analyst with expertise in experimentation"
  
  action:
    - "Validate test setup"
    - "Check statistical power"
    - "Analyze results with appropriate tests"
    - "Segment analysis"
    - "Draw conclusions"
  
  format:
    - "Executive summary (1 page)"
    - "Statistical details (appendix)"
    - "Recommendations"
  
  target:
    - "95% confidence in results"
    - "Clear go/no-go decision"
    - "Learning for future tests"
```

---

<a id="13-framework-combinations"></a>

### 13. ⚙️ Framework Combinations

#### Power Combinations for Specific Scenarios

**Scenario 1: Complex Project Planning**
```yaml
complex_project_combination:
  primary_framework: CRAFT
  enhancement: "CoT + ToT"
  
  implementation:
    context: "[Full project scope]"
    role: "Project manager thinking systematically"
    
    action_with_decision_trees:
      phase_planning:
        if_condition_a:
          path_1: "[outcomes and next steps]"
        if_condition_b:
          path_2: "[outcomes and next steps]"
      
      systematic_thinking:
        for_each_phase:
          - decompose_requirements
          - identify_dependencies
          - assess_risks
          - plan_mitigation
    
    format: "Gantt chart with decision points marked"
    target: "[Success metrics]"
```

**Scenario 2: Rapid Iterative Development**
```yaml
rapid_iteration_combination:
  primary_framework: RACE
  enhancement: "ReAct + Few-Shot"
  
  implementation:
    role: "Agile developer"
    action: "Build feature iteratively"
    context: "Sprint goal + examples of similar features"
    
    execute_cycle:
      iteration:
        think: "What's next priority?"
        act: "Implement increment"
        observe: "Test results"
        condition: "repeat until acceptance criteria met"
      
      max_iterations: "sprint_length"
      examples: "3 similar features for pattern learning"
```

---

<a id="14-mastery-principles"></a>

### 14. 🎓 Mastery Principles

#### The Ten Commandments of Prompt Excellence

```yaml
prompt_excellence_commandments:
  1_start_simple:
    principle: "Start Simple, Enhance Gradually"
    guidelines:
      - "Begin with RACE/RCAF"
      - "Add complexity only when needed"
      - "Stop when good enough"
  
  2_clarity_first:
    principle: "Clarity Trumps Completeness"
    guidelines:
      - "Better to be clear about less"
      - "Than comprehensive but confusing"
      - "Expression = 30% of CLEAR score"
  
  3_right_tool:
    principle: "Framework Fit Over Framework Fancy"
    guidelines:
      - "Right tool for the job"
      - "Not the most sophisticated tool"
      - "RCAF works for 80% of cases"
  
  4_measure_everything:
    principle: "Measure, Don't Guess"
    guidelines:
      - "CLEAR score everything"
      - "Track improvements"
      - "Learn from patterns"
  
  5_show_dont_tell:
    principle: "Examples Beat Explanations"
    guidelines:
      - "One good example > paragraph of description"
      - "Show good and bad examples"
      - "Include edge cases"
  
  6_constraints_liberate:
    principle: "Constraints Liberate Creativity"
    guidelines:
      - "Define boundaries explicitly"
      - "Include what's NOT wanted"
      - "Specify limits and thresholds"
  
  7_token_economy:
    principle: "Token Economy Matters"
    guidelines:
      - "Every token has cost"
      - "Balance detail with efficiency"
      - "Optimize high-frequency prompts"
  
  8_test_pessimistic:
    principle: "Test with Pessimism"
    guidelines:
      - "Assume misinterpretation"
      - "Check edge cases"
      - "Verify with variations"
  
  9_iterate_output:
    principle: "Iterate Based on Output"
    guidelines:
      - "Start with v1"
      - "Refine based on results"
      - "Stop at diminishing returns"
  
  10_document_reuse:
    principle: "Document for Reuse"
    guidelines:
      - "Build templates, not one-offs"
      - "Extract patterns"
      - "Share knowledge"
```

#### The Excellence Formula Expanded

```yaml
excellence_formula:
  equation: |
    Prompt Excellence = 
      (Right Framework × Clear Requirements)
      × (Complete Coverage × Good Structure)
      × (Concise Expression)
      × (1 + Reasoning Pattern Bonus)
      × (1 - Token Overhead Penalty)
      + DEPTH Processing Bonus
      ───────────────────────────────────
      Target: CLEAR ≥ 40/50
      Excellence: CLEAR ≥ 45/50
  
  variables:
    framework_fit: [0.8, 1.0]
    requirement_clarity: [0.7, 1.0]
    coverage: [0.6, 1.0]
    structure_quality: [0.7, 1.0]
    expression: [0.8, 1.0]
    reasoning_bonus: [0, 0.2]
    token_penalty: [0, 0.2]
    depth_bonus: 5  # points
```

---

<a id="15-quick-reference-card"></a>

### 15. 🎏 Quick Reference Card

### Framework Quick Select
```yaml
framework_selection:
  complexity_1_3_speed: RACE
  complexity_1_4_balance: RCAF
  complexity_3_6_audience: COSTAR
  complexity_4_6_instructions: CIDI
  complexity_5_7_creative: CRISPE
  complexity_6_8_precision: TIDD-EC
  complexity_7_10_comprehensive: CRAFT
```

### Enhancement Priority
```yaml
enhancement_priority:
  score_below_25: "Complete rewrite (RCAF)"
  score_25_30: "Framework switch"
  score_30_35: "Fix 2 weakest dimensions"
  score_35_40: "Polish weakest dimension"
  score_40_45: "Optional refinements"
  score_45_plus: "Ship it!"
```

### Common Fixes
```yaml
common_fixes:
  vague: "Add specifics (Role, Context)"
  no_structure: "Apply RCAF"
  too_complex: "Switch to RACE"
  missing_metrics: "Add success criteria"
  poor_expression: "Simplify language"
  not_reusable: "Extract parameters"
```

### Power Combinations
```yaml
power_combinations:
  systematic_thinking: "RCAF + CoT"
  iterative_content: "COSTAR + ReAct"
  learning_examples: "TIDD-EC + Few-Shot"
  quick_decisions: "RACE + ToT"
  maximum_power: "CRAFT + All"
```