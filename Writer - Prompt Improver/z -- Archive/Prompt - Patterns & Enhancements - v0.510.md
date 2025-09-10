# Prompt - Patterns & Enhancements - v0.510

Reusable templates and enhancement techniques with advanced ATLAS thinking, intelligent challenge-based simplification, and adaptive pattern learning for effective prompts across all use cases.

## 📋 Table of Contents

1. [🚀 QUICK TEMPLATES WITH PATTERN LEARNING](#-quick-templates-with-pattern-learning)
2. [📝 CORE PATTERNS](#-core-patterns)
3. [🧠 ATLAS-ENHANCED TECHNIQUES](#-atlas-enhanced-techniques)
4. [📄 PATTERN LEARNING & ADAPTATION](#-pattern-learning--adaptation)
5. [🚀 CHALLENGE-BASED IMPROVEMENTS](#-challenge-based-improvements)
6. [🎯 SELECTION GUIDE](#-selection-guide)
7. [📊 PATTERN PERFORMANCE](#-pattern-performance)
8. [🚨 ERROR RECOVERY](#-error-recovery)
9. [💡 ADVANCED TECHNIQUES](#-advanced-techniques)
10. [🎓 KEY PRINCIPLES](#-key-principles)

---

## 1. 🚀 QUICK TEMPLATES WITH PATTERN LEARNING

### Template Matrix

| Type | Minimal | Standard | Comprehensive | Thinking | Usage Metrics |
|------|---------|----------|---------------|----------|---------------|
| **Analysis** | "Analyze [topic] for [key insight]." | "As [expert], analyze [topic] focusing on [aspects]. Format: [structure]." | "As [expert] with [experience], analyze [topic] considering [factors]. Include [elements], format as [structure], deliver [insights]." | 2-4 | Usage count<br>Success rate<br>Simplification rate |
| **Creation** | "Create [deliverable]." | "Create [deliverable] for [audience] achieving [purpose]." | "Create [deliverable] for [audience] that [purpose]. Include [requirements], format as [structure], ensure [quality]." | 1-4 | Track all metrics |
| **Solution** | "Solve [problem]." | "Solve [problem] with practical approach." | "As [expert], solve [problem] given [constraints]. Provide [deliverable] using [methodology]." | 2-6 | Track all metrics |
| **Research** | "Research [topic]." | "Research [topic] to find [insights]." | "Research [topic] to identify [insights]. Use [methodology], present as [format], focus on [aspects]." | 2-5 | Track all metrics |
| **Explanation** | "Explain [concept]." | "Explain [concept] clearly to [audience]." | "Explain [concept] to [audience]. Use [examples], structure as [format], ensure [understanding level]." | 1-3 | Track all metrics |

### Template Selection Logic

```python
def select_template(type, request, patterns=None):
    template = templates[type]
    
    # Determine complexity preference
    if patterns:
        if patterns.always_minimal:
            return template['minimal']
        elif patterns.always_comprehensive:
            return template['comprehensive']
        else:
            complexity = patterns.complexity_preference or analyze_complexity(request)
    else:
        complexity = analyze_complexity(request)
    
    # Select based on complexity
    if complexity < 3:
        return template['minimal']
    elif complexity < 7:
        return template['standard']
    else:
        return template['comprehensive']
```

### Builder Template Phases

| Type | Phase 1 (MVP) | Phase 2 (Enhanced) | Phase 3 (Full) |
|------|---------------|-------------------|----------------|
| **App** | Simple [app type]<br>Single feature<br>User emotion<br>2-3 rounds | [App type] with goal<br>3-5 features<br>Audience & metrics<br>4-5 rounds | Comprehensive [app type]<br>Full features<br>Integrations<br>6-7 rounds |
| **Website** | Landing page<br>Conversion goal<br>Value prop<br>2 rounds | Multi-page site<br>User journey<br>Trust indicators<br>3-4 rounds | Full website<br>Interactive features<br>Analytics<br>5-6 rounds |

**Phase Selection:**
- MVP rate > 0.7 → Phase 1
- Enhanced rate > 0.5 → Phase 2
- Comprehensive rate > 0.3 → Phase 3
- Default → Phase 1

---

## 2. 📝 CORE PATTERNS

### Expert Analysis Pattern Versions

| Version | Complexity | Template | Elements |
|---------|------------|----------|----------|
| **Minimal** | 1 | "Analyze [subject] for [primary insight]." | task, goal |
| **Balanced** | 2 | "Analyze [subject] to [goal].<br>Focus: [key aspects]<br>Output: [deliverable format]" | task, goal, focus, format |
| **Comprehensive** | 3 | "As [expert] with [experience],<br>analyze [subject] to [goal].<br><br>CONTEXT: [Background]<br>REQUIREMENTS:<br>- [Aspect 1]<br>- [Aspect 2]<br>- [Metrics]<br><br>DELIVERABLES:<br>- Format: [structure]<br>- Length: [size]<br>- Sections: [components]<br><br>SUCCESS: [Measurable outcomes]" | role, task, context, requirements, deliverables, success |

**Version Selection:**
1. Check pattern preference if exists
2. Otherwise use complexity score
3. Apply selected template
4. Track usage

### Content Creation Pattern Building

**Elements to Include (Conditional):**

| Element | Include When | Default Inclusion |
|---------|--------------|-------------------|
| **Role** | Role inclusion rate > 0.5 | Yes |
| **Core Action** | Always | Always |
| **Audience** | Audience specificity > 0.3 | Yes |
| **Purpose** | Always | Always |
| **Requirements** | Detailed requirements rate > 0.4 | No |
| **Format** | Format specification rate > 0.5 | Yes |

**Pattern Assembly:**
1. Start with core action
2. Add conditional elements based on patterns
3. Join with appropriate connectors
4. Return complete pattern

---

## 3. 🧠 ATLAS-ENHANCED TECHNIQUES

### ATLAS Pattern Enhancement Phases

**A1 - Assess Pattern Fit**
- Identify prompt type
- Measure complexity (1-10)
- Find missing elements
- Calculate pattern match scores
- Select matches with score > 0.6

**T - Transform with Patterns**
- Create minimal transformation
- Create standard transformation
- Create comprehensive transformation
- Add pattern-based transformations for matches > 0.6

**L - Layer Pattern Elements**
- Add clarity layer if valuable
- Add structure layer if needed
- Add specificity layer if missing
- Add measurability layer if applicable
- Filter to only valuable layers

**A2 - Assess Pattern Impact**
- Measure clarity improvement
- Calculate complexity change
- Verify completeness
- Evaluate pattern effectiveness

**S - Synthesize Pattern**
- Create final version
- Record pattern application
- Return enhanced prompt

### Progressive Enhancement Strategy

| Level | Name | Action | Complexity | Include |
|-------|------|--------|------------|---------|
| **0** | Base | Original prompt | 1 | Always |
| **1** | Task | Add task clarity | 2 | Always |
| **2** | Role | Add appropriate role | 3 | If patterns suggest |
| **3** | Format | Add format specification | 4 | If patterns suggest |
| **4** | Context | Add relevant context | 5 | If patterns suggest |

**Optimal Level Selection:**
1. Build all applicable levels
2. Evaluate each for value
3. Select level with best clarity/complexity ratio
4. Track selection for pattern learning

---

## 4. 📄 PATTERN LEARNING & ADAPTATION

### Pattern Recognition System

**Recognized Pattern Structure:**
- Occurrences: Count of times seen
- Success rate: Percentage successful
- Average improvement: Mean enhancement value
- Typical domain: Most common domain
- Complexity level: Typical complexity
- Key elements: Essential components

### Pattern Matching Logic

```python
def predict_best_pattern(new_prompt, recognized_patterns):
    candidates = []
    
    for signature, pattern in recognized_patterns.items():
        if pattern['occurrences'] >= 3:  # Minimum confidence
            match_score = calculate_match_score(new_prompt, pattern)
            effectiveness = pattern['success_rate'] * pattern['avg_improvement']
            confidence = match_score * effectiveness
            
            if confidence > 0.6:
                candidates.append({
                    'pattern': pattern,
                    'confidence': confidence
                })
    
    # Return best match or None
    return max(candidates, key=lambda x: x['confidence']) if candidates else None
```

### Pattern Application Process

1. **Check for Pattern Match** (confidence > 0.6)
2. **Apply Key Elements** from successful pattern
3. **Adjust Complexity** to match pattern level
4. **Apply Domain Optimizations** if applicable
5. **Record Outcome** for learning

### Success Metrics Updates

**After Each Application:**
- Increment occurrence count
- Update success rate: `(old_rate * (n-1) + new_result) / n`
- Update average improvement: `(old_avg * (n-1) + new_improvement) / n`
- Cache if improvement > 70%

---

## 5. 🚀 CHALLENGE-BASED IMPROVEMENTS

### Challenge Point Matrix

| Challenge Type | Trigger | Original | Balanced | Minimal | Savings |
|----------------|---------|----------|----------|---------|---------|
| **Excessive Sections** | Sections > 5 | Multiple detailed sections | 3-5 key sections | Simple narrative flow | 2-3 rounds |
| **Over-Specified Role** | Role words > 15 | Detailed expert with qualifications | Domain expert | Knowledgeable perspective | 1-2 rounds |
| **Rigid Word Count** | Exact count specified | Exactly X words | Approximately X words | Comprehensive coverage | 1-2 rounds |
| **Excessive Examples** | Examples > 3 | Multiple detailed examples | 2-3 clear examples | 1 illustrative example | 1-2 rounds |
| **Over-Structured Format** | Format complexity > 7 | Complex multi-level structure | Clear main sections | Natural flow | 2-3 rounds |

### Challenge Intensity Selection

```python
def get_challenge_intensity(acceptance_rate):
    if acceptance_rate > 0.7:
        return 'aggressive'  # Use minimal alternatives
    elif acceptance_rate > 0.3:
        return 'balanced'    # Use balanced alternatives
    else:
        return 'gentle'      # Use gentle suggestions
```

### Challenge Message Generation

**Format:**
```
I found [N] simplification opportunities:

• [Current] → [Simplified]
• [Current] → [Simplified]
• [Current] → [Simplified]

Potential savings: [X] thinking rounds
[If patterns]: (You typically accept X% of simplifications)
```

### Smart Defaults Application

| Element | Standard Default | Technical Default | Creative Default | Business Default |
|---------|-----------------|-------------------|------------------|------------------|
| **Tone** | Professional and clear | Precise and detailed | Engaging and expressive | Concise and actionable |
| **Structure** | Logical sections | Problem-solution format | Narrative flow | Executive summary style |
| **Depth** | Comprehensive coverage | Detailed with examples | Exploratory | Focused on key points |
| **Examples** | Relevant examples | Code/implementation samples | Illustrative scenarios | Case studies |

**Default Selection:**
1. Check patterns for learned defaults
2. Identify domain if no pattern
3. Apply domain-specific default
4. Fall back to standard if unknown

---

## 6. 🎯 SELECTION GUIDE

### Pattern Selection Decision Tree

```python
def select_pattern(user_input, patterns=None):
    # Extract features
    features = {
        'task_type': identify_task_type(user_input),
        'complexity': assess_complexity(user_input),
        'domain': identify_domain(user_input),
        'clarity': assess_clarity(user_input),
        'length': len(user_input.split())
    }
    
    # Check pattern history first
    if patterns and has_historical_match(features, patterns):
        return get_historical_pattern(features, patterns)
    
    # Decision tree fallback
    if features['clarity'] < 3:
        return 'interactive'
    elif features['complexity'] > 7:
        return f"{features['task_type']}_comprehensive"
    elif features['complexity'] > 3:
        return f"{features['task_type']}_standard"
    else:
        return f"{features['task_type']}_minimal"
```

### Feature-Based Selection

| Clarity | Complexity | Result |
|---------|------------|--------|
| < 3 | Any | Interactive mode needed |
| ≥ 3 | > 7 | Comprehensive pattern |
| ≥ 3 | 3-7 | Standard pattern |
| ≥ 3 | < 3 | Minimal pattern |

### Historical Match Criteria

- Feature similarity > 0.7
- Previous success = true
- Confidence score > 0.6

---

## 7. 📊 PATTERN PERFORMANCE

### Pattern Usage Metrics

| Metric | Description | Target | Tracking |
|--------|-------------|--------|----------|
| **Pattern Usage** | Count per pattern type | - | Dictionary by name |
| **Success Rates** | Acceptance percentage | > 70% | List of boolean results |
| **Simplification Impact** | Complexity reduction | 30-50% | Average reduction |
| **User Preferences** | Complexity distribution | Varies | Minimal/Standard/Comprehensive counts |

### Efficiency Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Thinking Rounds Saved** | Average reduction | > 2 |
| **Words Reduced** | Average reduction | 20-40% |
| **Clarity Improvement** | Average increase | > 40% |

### Learning Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Patterns Recognized** | Unique patterns found | > 5 |
| **Successful Predictions** | Correct pattern matches | > 60% |
| **Adaptation Effectiveness** | User acceptance of adaptations | > 75% |
| **Convergence Speed** | Requests to stable patterns | < 5 |

### Insight Generation

**Most Successful Pattern:**
- Minimum 3 uses required
- Highest success rate wins
- Return pattern name and rate

**Preferred Complexity:**
- Analyze complexity distribution
- Find mode of selections
- Return preference level

---

## 8. 🚨 ERROR RECOVERY

### REPAIR Protocol for Patterns

| Failure Type | Recognition | Typical Cause | Recovery Strategy |
|--------------|-------------|---------------|-------------------|
| **Pattern Mismatch** | Wrong pattern applied | Context different than expected | Try minimal version |
| **Over Complexity** | Result too complex | Pattern too comprehensive | Simplify aggressively |
| **Under Specification** | Missing key elements | Pattern too minimal | Add essential elements |
| **Wrong Domain** | Domain mismatch | Incorrect identification | Apply general pattern |

### Recovery Proposal Priority

| Priority | Approach | Description | Confidence |
|----------|----------|-------------|------------|
| 1 | Learned Recovery | Previously successful recovery | 0.95 |
| 2 | Minimal | Simplest possible enhancement | 0.90 |
| 3 | Standard | Balanced enhancement | 0.70 |
| 4 | Different Pattern | Try alternative pattern | 0.60 |

### Failure Recording

**Track for Each Failure:**
- Failure type
- Context details
- Recovery approach used
- Success of recovery
- Timestamp

**Update Patterns:**
- Record failure/recovery pair
- Adjust pattern confidence
- Cache successful recoveries

---

## 9. 💡 ADVANCED TECHNIQUES

### Domain-Specific Optimization

| Domain | Indicators | Structure | Emphasis | Defaults |
|--------|------------|-----------|----------|----------|
| **Technical** | code, API, system, debug, algorithm, database | Problem-solution | Precision, examples, edge cases, performance | Structured with code blocks, precise tone |
| **Creative** | write, design, create, story, content, narrative | Inspiration-execution | Freedom, mood, audience, impact | Flowing narrative, engaging tone |
| **Business** | analyze, ROI, market, strategy, revenue, KPI | Executive summary | Metrics, recommendations, clarity, action | Executive brief, actionable tone |
| **Academic** | research, thesis, study, literature, hypothesis | Methodology-focused | Rigor, citations, methodology, analysis | Scholarly structure, formal tone |

### Domain Identification Process

```python
def identify_domain(prompt):
    scores = {}
    for domain, indicators in domains.items():
        score = sum(1 for ind in indicators if ind.lower() in prompt.lower())
        scores[domain] = score
    
    if max(scores.values()) == 0:
        return 'general'
    
    return max(scores, key=scores.get)
```

### Domain Optimization Steps

1. Apply domain structure
2. Add emphasis elements not present
3. Apply domain defaults for missing specs
4. Return optimized prompt

---

## 10. 🎓 KEY PRINCIPLES

### Enhancement Philosophy

| Principle | Description | Weight | Pattern Adjustable |
|-----------|-------------|--------|-------------------|
| **Start Minimal** | Begin with simplest pattern | 1.0 | No |
| **Challenge Complexity** | Question every addition | 0.9 | Yes |
| **Trust AI Capability** | Avoid over-specification | 0.8 | Yes |
| **Use Smart Defaults** | Reduce explicit requirements | 0.7 | Yes |
| **Stop at Sufficient** | Good enough beats perfect | 0.8 | Yes |
| **Document Efficiency** | Show what was saved | 0.6 | No |
| **Learn Continuously** | Every pattern teaches | 0.9 | No |
| **Adapt Intelligently** | Patterns guide, not dictate | 0.85 | No |

**User Type Adjustments:**
- Expert user: Add "Trust user judgment" (0.95)
- Beginner user: Add "Provide structure" (0.85)
- Minimal preference: Boost "Start minimal" to 1.0

### Pattern Evolution Philosophy

> "The best pattern is the simplest one that worked before in a similar context"

**Evolution Stages:**
1. **Discovery** - Try various patterns, observe outcomes
2. **Recognition** - Identify what works consistently
3. **Prediction** - Match new requests to successful patterns
4. **Optimization** - Refine patterns based on feedback
5. **Mastery** - Seamless pattern application

### Success Criteria

**Pattern Application Success:**
- Pattern match > 0.7
- Complexity appropriate
- User accepts result
- Efficiency gained (rounds saved > 0)
- Clarity improved (delta > 0.2)

### The Pattern Evolution Question

> "Is this pattern teaching us something new, or confirming what we already know?"

**Always Consider:**
- Natural language over rigid templates
- Implicit understanding over explicit specification  
- Simple effectiveness over complex completeness
- Clear communication over perfect formatting
- Fast iteration over slow perfection
- Continuous learning from every application

---

*Excellence through intelligent pattern recognition, adaptive template application, and continuous learning. Every pattern application teaches the system. Every enhancement gets smarter through use.*