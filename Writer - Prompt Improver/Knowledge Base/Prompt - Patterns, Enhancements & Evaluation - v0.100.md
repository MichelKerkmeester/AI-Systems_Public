# Prompt Improver - Patterns, Enhancements & Evaluation - v0.100

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
15. [🏎️ Quick Reference Card](#15-quick-reference-card)

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

```python
def select_optimal_framework(task_analysis):
    """Enhanced framework selection with pattern recognition"""
    
    # Analyze task characteristics
    characteristics = {
        'complexity': assess_complexity(task_analysis),
        'urgency': detect_urgency(task_analysis),
        'audience_specific': has_audience_requirements(task_analysis),
        'creative_element': requires_creativity(task_analysis),
        'precision_critical': needs_high_precision(task_analysis),
        'iterative_nature': requires_iteration(task_analysis),
        'compliance_needs': has_compliance_requirements(task_analysis),
        'multi_stakeholder': involves_multiple_parties(task_analysis)
    }
    
    # Pattern matching for framework selection
    framework_scores = {}
    
    # RCAF scoring
    framework_scores['RCAF'] = (
        10 - characteristics['complexity'] +  # Better for simple
        (5 if characteristics['complexity'] <= 6 else 0) +  # Sweet spot
        (3 if not characteristics['audience_specific'] else 0)
    )
    
    # COSTAR scoring
    framework_scores['COSTAR'] = (
        (10 if characteristics['audience_specific'] else 3) +
        (5 if characteristics['creative_element'] else 2) +
        (3 if characteristics['multi_stakeholder'] else 0)
    )
    
    # RACE scoring
    framework_scores['RACE'] = (
        (10 if characteristics['urgency'] else 2) +
        (8 if characteristics['complexity'] <= 3 else 0) +
        (-5 if characteristics['precision_critical'] else 0)
    )
    
    # TIDD-EC scoring
    framework_scores['TIDD-EC'] = (
        (10 if characteristics['precision_critical'] else 3) +
        (8 if characteristics['compliance_needs'] else 2) +
        (5 if characteristics['complexity'] >= 6 else 0)
    )
    
    # Select highest scoring framework
    best_framework = max(framework_scores, key=framework_scores.get)
    confidence = framework_scores[best_framework] / 20  # Normalize to 0-1
    
    return {
        'primary': best_framework,
        'confidence': confidence,
        'alternative': sorted(framework_scores, key=framework_scores.get)[-2],
        'reasoning': generate_selection_reasoning(characteristics, best_framework)
    }
```

---

<a id="2-framework-deep-dives"></a>

### 2. 🔧 Framework Deep Dives

#### RCAF Mastery Patterns

**Pattern 1: Layered RCAF for Complex Contexts**
```
Role: [Primary expertise] with [secondary skill] and [domain knowledge]
Context: 
  - Immediate: [Current situation]
  - Historical: [Relevant background]
  - Constraints: [Limitations]
Action: [Primary action] by [method] to achieve [outcome]
Format: 
  - Structure: [Organization]
  - Style: [Tone/approach]
  - Deliverables: [Specific outputs]
```

**Pattern 2: RCAF with Embedded Metrics**
```
Role: [Expert] measured by [KPI]
Context: [Situation] with success defined as [metric]
Action: [Task] achieving minimum [threshold]
Format: [Output] demonstrating [measurable quality]
```

**Pattern 3: Conditional RCAF**
```
Role: [Expert who adapts based on conditions]
Context: If [condition A] then [context A], else [context B]
Action: When [trigger] then [action A], otherwise [action B]
Format: Adapt output based on [criteria]
```

#### COSTAR Enhancement Techniques

**Technique 1: Audience Layering**
```
Audience: 
  Primary: [Main reader - detailed profile]
  Secondary: [Other stakeholders]
  Concerns: [What each group cares about]
  Knowledge level: [Technical understanding]
```

**Technique 2: Style-Tone Matrix**
```
Style × Tone combinations:
- Formal + Empathetic: Crisis communication
- Technical + Enthusiastic: Product launches
- Casual + Authoritative: Educational content
- Creative + Professional: Marketing materials
```

**Technique 3: Response Variants**
```
Response:
  If [condition]: [format A]
  Elif [condition]: [format B]
  Else: [default format]
  Always include: [mandatory elements]
```

#### TIDD-EC Excellence Patterns

**Pattern 1: Cascading Examples**
```
Examples:
  Basic: [Simple case]
  Intermediate: [Typical case]
  Advanced: [Complex case]
  Edge case: [Unusual scenario]
  Anti-pattern: [What not to do]
```

**Pattern 2: Do's and Don'ts Hierarchy**
```
Critical Do's: [Must do - compliance/safety]
Recommended Do's: [Should do - best practice]
Optional Do's: [Nice to have - excellence]

Fatal Don'ts: [Never do - breaks system]
Major Don'ts: [Avoid - causes problems]
Minor Don'ts: [Prefer not - suboptimal]
```

---

<a id="3-advanced-pattern-combinations"></a>

### 3. 🧠 Advanced Pattern Combinations

#### Framework Fusion Patterns

**RCAF + CoT (Chain of Thought)**
```
Role: [Expert] who thinks systematically
Context: [Situation requiring reasoning]
Action: Solve by:
  1. Decompose: [Break down problem]
  2. Analyze: [Examine each component]
  3. Synthesize: [Combine insights]
  4. Validate: [Verify solution]
Format: Show reasoning at each step with final answer highlighted
```

**COSTAR + ReAct (Reasoning-Action)**
```
Context: [Initial situation]
Objective: [Goal requiring iteration]
Style: Analytical with visible reasoning
Tone: Professional problem-solver
Audience: [Stakeholders needing transparency]
Response: 
  Cycle format:
  - Thought: [Reasoning]
  - Action: [What to do]
  - Observation: [Result]
  - Repeat until: [Success criteria]
```

**TIDD-EC + Few-Shot**
```
Task: [Primary objective]
Instructions: Learn from examples then apply
Do's: [Follow patterns from examples]
Don't's: [Avoid anti-patterns shown]
Examples:
  Case 1: Input→Output with explanation
  Case 2: Input→Output with explanation
  Case 3: Input→Output with explanation
Context: Apply learned patterns to new inputs
```

**RACE + ToT (Tree of Thoughts)**
```
Role: Strategic decision maker
Action: Evaluate multiple solution paths
Context: [Decision scenario]
Execute: 
  Branch 1: [Approach A] → Score: X
  Branch 2: [Approach B] → Score: Y
  Branch 3: [Approach C] → Score: Z
  Selection: Highest scoring with rationale
```

#### Nested Framework Patterns

**Master-Detail Pattern**
```
Master (CRAFT):
  Context: [Overall project scope]
  Role: [Project lead]
  Action: [High-level objectives]
  Format: [Deliverable structure]
  Target: [Success metrics]
  
  Detail Tasks (RACE):
    Subtask 1:
      Role: [Specialist]
      Action: [Specific task]
      Context: [From master]
      Execute: [Quick delivery]
```

**Progressive Refinement Pattern**
```
Initial (RACE): Quick first draft
  ↓
Refinement (RCAF): Add structure
  ↓
Enhancement (COSTAR): Optimize for audience
  ↓
Finalization (TIDD-EC): Quality assurance
```

---

<a id="4-framework-optimization-strategies"></a>

### 4. 🎨 Framework Optimization Strategies

#### Token Optimization Techniques

**Compression Strategies by Framework:**

```python
def optimize_framework_tokens(framework, content):
    """Reduce token usage while maintaining effectiveness"""
    
    optimization_strategies = {
        'RCAF': {
            'role': lambda x: extract_key_expertise(x),  # Remove redundant qualifiers
            'context': lambda x: filter_essential_only(x),  # Cut non-critical details
            'action': lambda x: single_clear_verb(x),  # One action, not multiple
            'format': lambda x: structure_only(x)  # Remove style descriptions
        },
        'COSTAR': {
            'merge': combine_style_tone,  # Merge overlapping elements
            'audience': profile_key_traits,  # Essential characteristics only
            'response': simplify_format  # Streamline specifications
        },
        'RACE': {
            'ultra_minimal': True,  # Maximum compression
            'single_line': True,  # Each element one line max
            'abbreviate': True  # Use standard abbreviations
        }
    }
    
    return apply_optimizations(framework, content, optimization_strategies)
```

**Framework Switching for Efficiency:**
```
If token_count > threshold:
  If complexity < 4:
    Switch CRAFT → RCAF (save 15-20%)
  If complexity < 2:
    Switch RCAF → RACE (save additional 5%)
  If precision not critical:
    Switch TIDD-EC → RCAF (save 12-15%)
```

---

## PART 2: ENHANCEMENT PATTERNS

<a id="5-systematic-enhancement-methodology"></a>

### 5. 🚀 Systematic Enhancement Methodology

#### The Enhancement Pipeline

```python
class EnhancementPipeline:
    """Systematic prompt improvement process"""
    
    def __init__(self):
        self.stages = [
            self.structural_enhancement,
            self.clarity_enhancement,
            self.precision_enhancement,
            self.efficiency_enhancement,
            self.reusability_enhancement
        ]
    
    def structural_enhancement(self, prompt):
        """Improve organization and framework"""
        enhancements = []
        
        # Apply framework if missing
        if not has_framework(prompt):
            prompt = apply_best_framework(prompt)
            enhancements.append("Applied RCAF framework")
        
        # Reorganize elements
        if poor_organization(prompt):
            prompt = reorganize_logically(prompt)
            enhancements.append("Restructured for logical flow")
        
        return prompt, enhancements
    
    def clarity_enhancement(self, prompt):
        """Improve expression and understanding"""
        enhancements = []
        
        # Simplify complex sentences
        complex_parts = find_complex_sentences(prompt)
        for part in complex_parts:
            simplified = simplify_sentence(part)
            prompt = prompt.replace(part, simplified)
            enhancements.append(f"Simplified: {part[:30]}...")
        
        # Remove ambiguity
        ambiguous_terms = find_ambiguous_terms(prompt)
        for term in ambiguous_terms:
            clarified = clarify_term(term, context=prompt)
            prompt = prompt.replace(term, clarified)
            enhancements.append(f"Clarified: {term}")
        
        return prompt, enhancements
    
    def precision_enhancement(self, prompt):
        """Improve accuracy and specificity"""
        enhancements = []
        
        # Add measurable outcomes
        if lacks_measurability(prompt):
            prompt = add_success_metrics(prompt)
            enhancements.append("Added measurable success criteria")
        
        # Specify constraints
        if missing_constraints(prompt):
            prompt = add_constraints(prompt)
            enhancements.append("Added explicit constraints")
        
        return prompt, enhancements
```

---

<a id="6-pattern-based-refinements"></a>

### 6. 🔄 Pattern-Based Refinements

#### Common Enhancement Patterns

**Pattern: Vague to Specific Transformation**
```
BEFORE: "Help analyze customer data"
TRANSFORMATION STEPS:
1. Add role: "Data analyst specializing in customer behavior"
2. Specify context: "E-commerce platform, Q4 2024, 50K transactions"
3. Define action: "Identify top 3 purchase patterns and segment customers"
4. Clarify format: "Dashboard with visualizations and executive summary"
AFTER: [Complete RCAF prompt]
IMPROVEMENT: +20 CLEAR points
```

**Pattern: Assumption Elimination**
```
DETECT: Terms assuming knowledge
- "our system" → "Python Django web application"
- "the usual format" → "CSV with headers: date, user_id, amount"
- "standard approach" → "RESTful API design patterns"
IMPACT: +3-5 Correctness points
```

**Pattern: Scope Boundary Definition**
```
ADD BOUNDARIES:
- What's included: [explicit list]
- What's excluded: [explicit list]
- Edge cases: [how to handle]
IMPACT: +4-6 Logic/Coverage points
```

**Pattern: Example Injection**
```
WHEN TO ADD EXAMPLES:
- Complex formatting required
- Specific style needed
- Quality standards important
STRUCTURE:
- Good example with explanation
- Bad example with why it's wrong
- Edge case example
IMPACT: +3-5 Correctness, +2-3 Expression
```

---

<a id="7-excellence-patterns"></a>

### 7. 💎 Excellence Patterns

#### The 45+ CLEAR Score Patterns

**Excellence Pattern 1: Complete Context Layering**
```
Context Structure:
- Environmental: [Where/when this happens]
- Historical: [What led to this]
- Constraints: [Limitations]
- Resources: [Available assets]
- Dependencies: [What this relies on]
- Stakeholders: [Who's involved]
```

**Excellence Pattern 2: Multi-Level Success Criteria**
```
Success Defined:
- Minimum viable: [Baseline acceptability]
- Target: [Expected outcome]
- Excellence: [Exceptional result]
- Metrics: [How measured]
- Timeline: [When evaluated]
```

**Excellence Pattern 3: Adaptive Response Formats**
```
Format Variants:
If [high detail needed]:
  - Comprehensive report with all data
  - Executive summary
  - Technical appendices
Elif [quick review needed]:
  - Bullet point summary
  - Key metrics dashboard
Else:
  - Standard report format
```

**Excellence Pattern 4: Self-Documenting Structure**
```
Each Element Includes:
- What: [The requirement]
- Why: [The reasoning]
- How: [The approach]
- Example: [Illustration]
```

---

<a id="8-recovery--repair-protocols"></a>

### 8. 🛠️ Recovery & Repair Protocols

#### Systematic Error Recovery

**The REPAIR+ Framework**
```python
class RepairFramework:
    """Enhanced REPAIR with pattern learning"""
    
    def recognize(self, prompt):
        """Identify all issues"""
        issues = {
            'critical': [],  # Must fix
            'major': [],     # Should fix
            'minor': [],     # Nice to fix
            'style': []      # Optional
        }
        
        # Pattern-based recognition
        patterns = load_error_patterns()
        for pattern in patterns:
            if pattern.matches(prompt):
                issues[pattern.severity].append(pattern)
        
        return issues
    
    def explain(self, issues):
        """Explain impact with examples"""
        explanations = {}
        for severity, issue_list in issues.items():
            for issue in issue_list:
                explanations[issue] = {
                    'what': issue.description,
                    'why_matters': issue.impact,
                    'example_failure': issue.failure_case,
                    'fix_preview': issue.solution_preview
                }
        return explanations
    
    def propose(self, issues, context):
        """Generate fix proposals"""
        proposals = []
        for issue in flatten(issues.values()):
            proposal = {
                'issue': issue,
                'solutions': generate_solutions(issue, context),
                'effort': estimate_effort(issue),
                'impact': estimate_improvement(issue),
                'priority': calculate_priority(issue)
            }
            proposals.append(proposal)
        return sorted(proposals, key=lambda x: x['priority'])
    
    def apply(self, prompt, proposals, strategy='balanced'):
        """Apply fixes based on strategy"""
        strategies = {
            'minimal': lambda p: p['priority'] > 8,
            'balanced': lambda p: p['impact']/p['effort'] > 2,
            'comprehensive': lambda p: p['priority'] > 3,
            'critical_only': lambda p: p['issue'].severity == 'critical'
        }
        
        selected = filter(strategies[strategy], proposals)
        for proposal in selected:
            prompt = apply_fix(prompt, proposal['solutions'][0])
        
        return prompt
    
    def iterate(self, prompt, target_score=40):
        """Iterate until quality target met"""
        max_iterations = 5
        history = []
        
        for i in range(max_iterations):
            score = calculate_clear_score(prompt)
            history.append({'iteration': i, 'score': score, 'prompt': prompt})
            
            if score >= target_score:
                break
            
            issues = self.recognize(prompt)
            if not issues:
                break
            
            proposals = self.propose(issues, prompt)
            prompt = self.apply(prompt, proposals)
        
        return prompt, history
    
    def record(self, original, final, history):
        """Record for pattern learning"""
        learning_record = {
            'original': original,
            'final': final,
            'improvement': calculate_improvement(original, final),
            'successful_patterns': extract_successful_patterns(history),
            'iterations_needed': len(history),
            'time_taken': calculate_time(history)
        }
        
        save_to_pattern_library(learning_record)
        return learning_record
```

---

## PART 3: EVALUATION & SCORING

<a id="9-clear-evaluation-mastery"></a>

### 9. ✅ CLEAR Evaluation Mastery

#### Advanced CLEAR Scoring Methodology

**Weighted Scoring with Context:**
```python
def calculate_contextual_clear_score(prompt, use_case):
    """Context-aware CLEAR scoring"""
    
    base_weights = {
        'correctness': 0.20,
        'logic': 0.20,
        'expression': 0.30,
        'arrangement': 0.20,
        'reuse': 0.10
    }
    
    # Adjust weights based on use case
    if use_case == 'api_integration':
        base_weights['correctness'] = 0.30  # Precision critical
        base_weights['expression'] = 0.20
    elif use_case == 'creative_writing':
        base_weights['expression'] = 0.35  # Clarity paramount
        base_weights['correctness'] = 0.15
    elif use_case == 'template_creation':
        base_weights['reuse'] = 0.25  # Reusability focus
        base_weights['logic'] = 0.15
    
    # Score each dimension with context
    scores = {}
    for dimension in base_weights:
        scores[dimension] = score_dimension_contextual(prompt, dimension, use_case)
    
    # Calculate weighted total
    weighted_score = sum(scores[d] * base_weights[d] * 50 for d in scores)
    
    return {
        'total': weighted_score,
        'breakdown': scores,
        'weights_used': base_weights,
        'context': use_case
    }
```

**Dimension Interdependencies:**
```
Expression ↔ Arrangement: Clear language needs good structure
Logic ↔ Correctness: Complete coverage ensures accuracy
Arrangement ↔ Reuse: Good structure enables templates
Expression ↔ Correctness: Clarity prevents misinterpretation
```

---

<a id="10-advanced-scoring-techniques"></a>

### 10. 📈 Advanced Scoring Techniques

#### Multi-Pass Scoring

**Pass 1: Surface Evaluation**
- Presence of framework elements
- Basic completeness
- Obvious issues

**Pass 2: Deep Analysis**
- Ambiguity detection
- Hidden assumptions
- Edge case coverage

**Pass 3: Interaction Testing**
- How AI will interpret
- Potential failure modes
- Output predictability

#### Comparative Scoring

```python
def comparative_clear_scoring(prompt_versions):
    """Score multiple versions for optimization"""
    
    results = []
    for version in prompt_versions:
        score = calculate_clear_score(version)
        results.append({
            'version': version,
            'score': score,
            'strengths': identify_strengths(score),
            'weaknesses': identify_weaknesses(score),
            'improvement_potential': calculate_potential(score)
        })
    
    # Analyze patterns
    best = max(results, key=lambda x: x['score']['total'])
    patterns = extract_success_patterns(best)
    
    return {
        'best_version': best,
        'all_results': results,
        'success_patterns': patterns,
        'optimization_path': generate_path(results)
    }
```

---

<a id="11-weakness-detection--analysis"></a>

### 11. 🔍 Weakness Detection & Analysis

#### Automated Weakness Detection

```python
def detect_prompt_weaknesses(prompt):
    """Comprehensive weakness analysis"""
    
    weakness_detectors = {
        'vagueness': [
            check_for_words(['help', 'assist', 'some', 'various']),
            check_unmeasurable_outcomes(),
            check_missing_specifics()
        ],
        'incompleteness': [
            check_missing_framework_elements(),
            check_undefined_terms(),
            check_assumed_knowledge()
        ],
        'ambiguity': [
            check_multiple_interpretations(),
            check_pronoun_clarity(),
            check_modifier_attachment()
        ],
        'structure': [
            check_logical_flow(),
            check_element_organization(),
            check_hierarchy_clarity()
        ],
        'efficiency': [
            check_redundancy(),
            check_token_waste(),
            check_unnecessary_complexity()
        ]
    }
    
    weaknesses = {}
    for category, detectors in weakness_detectors.items():
        issues = []
        for detector in detectors:
            result = detector(prompt)
            if result:
                issues.append(result)
        if issues:
            weaknesses[category] = issues
    
    return {
        'weaknesses': weaknesses,
        'severity': calculate_severity(weaknesses),
        'priority_fixes': prioritize_fixes(weaknesses),
        'estimated_improvement': estimate_clear_gain(weaknesses)
    }
```

---

## PART 4: PRACTICAL IMPLEMENTATION

<a id="12-use-case-templates"></a>

### 12. 📊 Use Case Templates

#### Industry-Specific Excellence Templates

**Software Development Suite**

```
// API Documentation Template (TIDD-EC)
Task: Document REST API endpoint for [resource]
Instructions:
  1. Define endpoint (method, path, version)
  2. List all parameters with types
  3. Show request/response examples
  4. Document error codes
  5. Include rate limits
Do's:
  - Use consistent formatting
  - Include curl examples
  - Specify authentication
  - Version all changes
Don'ts:
  - Expose internal logic
  - Use technical jargon without definition
  - Skip error documentation
Examples: [Include 3 real examples]
Context: [API version, tech stack, audience]

// Code Review Template (RCAF + CoT)
Role: Senior developer reviewing code for production readiness
Context: [Language], [Framework], [Project standards]
Action: Review code thinking through:
  1. Functionality: Does it work as intended?
  2. Performance: Are there bottlenecks?
  3. Security: Any vulnerabilities?
  4. Maintainability: Is it readable and documented?
  5. Testing: Adequate test coverage?
Format: Structured feedback with severity levels and suggested fixes
```

**Data Analysis Suite**

```
// Exploratory Data Analysis (COSTAR)
Context: Dataset with [N] records, [M] features, [quality issues]
Objective: Understand data patterns and prepare for modeling
Style: Technical but accessible to stakeholders
Tone: Objective and data-driven
Audience: Data team and business analysts
Response: Jupyter notebook with:
  - Data quality report
  - Statistical summaries
  - Correlation analysis
  - Feature importance
  - Visualization gallery
  - Next steps recommendations

// A/B Test Analysis (CRAFT)
Context: 
  - Test: [Control vs variant description]
  - Duration: [Time period]
  - Sample size: [N per group]
  - Success metrics: [Primary and secondary KPIs]
Role: Statistical analyst with expertise in experimentation
Action:
  - Validate test setup
  - Check statistical power
  - Analyze results with appropriate tests
  - Segment analysis
  - Draw conclusions
Format: 
  - Executive summary (1 page)
  - Statistical details (appendix)
  - Recommendations
Target:
  - 95% confidence in results
  - Clear go/no-go decision
  - Learning for future tests
```

**Content Creation Suite**

```
// SEO Article Template (RCAF + Layers)
Role: SEO content writer with [industry] expertise
Context:
  Primary: Target keyword: [keyword] with [search volume]
  Competition: [List top 3 competitors]
  Intent: [Informational/Transactional/Navigational]
Action: Create article that:
  - Targets [keyword] naturally (2-3% density)
  - Answers [user intent]
  - Outperforms [competitor URLs]
  - Includes [LSI keywords]
Format:
  - Length: [word count based on competition]
  - Structure: H1, multiple H2s, H3s for detail
  - Elements: Meta description, alt texts, internal links
  - Style: [Brand voice guide]
```

---

<a id="13-framework-combinations"></a>

### 13. ⚙️ Framework Combinations

#### Power Combinations for Specific Scenarios

**Scenario 1: Complex Project Planning**
```
Primary: CRAFT (overall structure)
+ CoT (systematic thinking)
+ ToT (decision points)

Implementation:
Context: [Full project scope] (CRAFT)
Role: Project manager thinking systematically (CRAFT + CoT)
Action: 
  Phase planning with decision trees (CRAFT + ToT):
    If [condition A]: Path 1 → [outcomes]
    If [condition B]: Path 2 → [outcomes]
Format: Gantt chart with decision points marked
Target: [Success metrics] (CRAFT)
```

**Scenario 2: Rapid Iterative Development**
```
Primary: RACE (speed)
+ ReAct (iteration)
+ Few-Shot (learning)

Implementation:
Role: Agile developer
Action: Build feature iteratively
Context: Sprint goal + examples of similar features
Execute:
  Iteration cycle:
    - Think: What's next priority?
    - Act: Implement increment
    - Observe: Test results
    - Repeat: Until acceptance criteria met
```

**Scenario 3: Quality-Critical Documentation**
```
Primary: TIDD-EC (precision)
+ COSTAR (audience optimization)
+ CoT (completeness)

Implementation:
Task: Create compliance documentation (TIDD-EC)
Context + Audience: Regulators and internal teams (COSTAR)
Instructions: Think through each requirement (CoT):
  1. Identify applicable regulations
  2. Map requirements to implementation
  3. Document evidence
  4. Create audit trail
Do's and Don'ts: [Compliance specifics] (TIDD-EC)
Style + Tone: Formal, precise, legally defensible (COSTAR)
```

---

<a id="14-mastery-principles"></a>

### 14. 🎓 Mastery Principles

#### The Ten Commandments of Prompt Excellence

1. **Start Simple, Enhance Gradually**
   - Begin with RACE/RCAF
   - Add complexity only when needed
   - Stop when good enough

2. **Clarity Trumps Completeness**
   - Better to be clear about less
   - Than comprehensive but confusing
   - Expression = 30% of CLEAR score

3. **Framework Fit Over Framework Fancy**
   - Right tool for the job
   - Not the most sophisticated tool
   - RCAF works for 40% of cases

4. **Measure, Don't Guess**
   - CLEAR score everything
   - Track improvements
   - Learn from patterns

5. **Examples Beat Explanations**
   - One good example > paragraph of description
   - Show good and bad examples
   - Include edge cases

6. **Constraints Liberate Creativity**
   - Define boundaries explicitly
   - Include what's NOT wanted
   - Specify limits and thresholds

7. **Token Economy Matters**
   - Every token has cost
   - Balance detail with efficiency
   - Optimize high-frequency prompts

8. **Test with Pessimism**
   - Assume misinterpretation
   - Check edge cases
   - Verify with variations

9. **Iterate Based on Output**
   - Start with v1
   - Refine based on results
   - Stop at diminishing returns

10. **Document for Reuse**
    - Build templates, not one-offs
    - Extract patterns
    - Share knowledge

#### The Excellence Formula Expanded

```
Prompt Excellence = 
    (Right Framework × Clear Requirements)
    × (Complete Coverage × Good Structure)
    × (Concise Expression)
    × (1 + Reasoning Pattern Bonus)
    × (1 - Token Overhead Penalty)
    + DEPTH Processing Bonus
    ────────────────────────────────────
    Target: CLEAR ≥ 40/50
    Excellence: CLEAR ≥ 45/50
    
Where:
- Framework Fit: 0.8-1.0
- Requirement Clarity: 0.7-1.0
- Coverage: 0.6-1.0
- Structure Quality: 0.7-1.0
- Expression: 0.8-1.0
- Reasoning Bonus: 0-0.2
- Token Penalty: 0-0.2
- DEPTH Bonus: +5 points
```

#### Progressive Mastery Path

```
Level 1: Foundation (Weeks 1-2)
- Master RCAF structure
- Achieve consistent CLEAR 35+
- Understand token basics

Level 2: Expansion (Weeks 3-4)
- Learn all 7 frameworks
- Apply basic combinations
- Achieve CLEAR 40+ regularly

Level 3: Refinement (Weeks 5-6)
- Master weakness detection
- Apply enhancement patterns
- Consistent CLEAR 40-45

Level 4: Excellence (Weeks 7-8)
- Complex combinations fluent
- Token optimization mastered
- Regular CLEAR 45+

Level 5: Mastery (Ongoing)
- Intuitive framework selection
- Create novel patterns
- Teach others
- CLEAR 45+ standard
```

---

<a id="15-quick-reference-card"></a>

### 15. 🏎️ Quick Reference Card

### Framework Quick Select
```
Complexity 1-3 + Speed needed → RACE
Complexity 1-4 + Balance → RCAF
Complexity 3-6 + Audience → COSTAR
Complexity 4-6 + Instructions → CIDI
Complexity 5-7 + Creative → CRISPE
Complexity 6-8 + Precision → TIDD-EC
Complexity 7-10 + Comprehensive → CRAFT
```

### Enhancement Priority
```
Score < 25: Complete rewrite (RCAF)
Score 25-30: Framework switch
Score 30-35: Fix 2 weakest dimensions
Score 35-40: Polish weakest dimension
Score 40-45: Optional refinements
Score 45+: Ship it!
```

### Common Fixes
```
Vague → Add specifics (Role, Context)
No structure → Apply RCAF
Too complex → Switch to RACE
Missing metrics → Add success criteria
Poor expression → Simplify language
Not reusable → Extract parameters
```

### Power Combinations
```
RCAF + CoT: Systematic thinking
COSTAR + ReAct: Iterative content
TIDD-EC + Few-Shot: Learning from examples
RACE + ToT: Quick decisions
CRAFT + All: Maximum power
```