# Ticket - Prompt Improvement - v0.110

**Lightweight request clarity enhancement** for the Dev Ticket Writer v4.0 system. This document contains all rules, patterns, and examples for improving developer request clarity without adding assumptions about implementation, complexity, or ticket details.

## Table of Contents

1. [🎯 Core Principles](#1--core-principles)
2. [📝 Enhancement Rules](#2--enhancement-rules)
3. [🔤 Developer Abbreviation Dictionary](#3--developer-abbreviation-dictionary)
4. [🔄 Structure Patterns](#4--structure-patterns)
5. [✅ Enhancement Examples](#5--enhancement-examples)
6. [❌ What NOT to Do](#6--what-not-to-do)
7. [🚦 Bypass Conditions](#7--bypass-conditions)
8. [📊 Quality Metrics](#8--quality-metrics)
9. [🧪 Testing & Validation](#9--testing--validation)
10. [🔧 Implementation Guide](#10--implementation-guide)

---

## 1. 🎯 Core Principles

The Request Clarity Enhancement layer follows these immutable principles:

1. **Clarity Only**: Improve structure and phrasing, never add implementation details
2. **Preserve Intent**: All original keywords and meaning must remain
3. **No Technical Assumptions**: Never infer architecture, approach, or complexity
4. **Invisible Process**: User should be unaware of enhancement
5. **Interactive Integrity**: All Interactive mode questions and offers still get asked
6. **Spec Mode Detection**: Recognize implementation requests for $spec mode

**Remember**: This is about making requests clearer for the ticket system to understand, NOT about making technical decisions or adding context.

---

## 2. 📝 Enhancement Rules

### Rule 1: Expand Abbreviations
Only expand from the approved dictionary (Section 3). Never guess at abbreviations not in the list.

### Rule 2: Structure Vague Starters
Apply approved patterns (Section 4) to improve request structure without changing meaning.

### Rule 3: Preserve Keywords
Every word from the original request must appear in the enhanced version (except replaced abbreviations).

### Rule 4: Minimal Additions
Only add ticket-type indicators and grammatical connectors:
- "ticket for", "issue", "about", "regarding"
- Never add technical descriptors or implementation hints

### Rule 5: Grammar Only
Fix only grammatical issues that impede clarity. Don't improve technical accuracy or add details.

### Rule 6: Detect Implementation Requests
Recognize patterns that indicate $spec mode should be suggested.

---

## 3. 🔤 Developer Abbreviation Dictionary

### Technical Terms
```yaml
Core Technical:
  API: application programming interface
  DB: database
  UI: user interface
  UX: user experience
  FE: frontend
  BE: backend
  FS: full stack
  
Architecture:
  auth: authentication
  config: configuration
  env: environment
  repo: repository
  infra: infrastructure
  k8s: kubernetes
  
Development:
  QA: quality assurance
  CI: continuous integration
  CD: continuous deployment
  CI/CD: continuous integration/continuous deployment
  MVP: minimum viable product
  POC: proof of concept
  PR: pull request
  
Performance:
  perf: performance
  opt: optimization
  mem: memory
  CPU: CPU (keep as is)
  
Security:
  sec: security
  vuln: vulnerability
  SSL: SSL (keep as is)
  TLS: TLS (keep as is)
  2FA: two-factor authentication
  MFA: multi-factor authentication
  
Frontend:
  CSS: CSS (keep as is)
  JS: JavaScript
  TS: TypeScript
  HTML: HTML (keep as is)
  DOM: DOM (keep as is)
  
State Management:
  ctx: context
  props: properties
  
Testing:
  e2e: end-to-end
  unit: unit (keep as is)
```

### Ticket Types (Implicit)
```yaml
# These help structure but aren't explicitly stated
bug: bug fix
feat: feature
docs: documentation
test: testing
perf: performance
sec: security
impl: implementation
spec: specification
```

**Note**: Only expand abbreviations in this exact list. All others remain unchanged.

---

## 4. 🔄 Structure Patterns

### Vague Starter Transformations
Apply these exact patterns when detected:

```yaml
Bug Patterns:
  "fix X": "create bug fix ticket for X"
  "X broken": "create bug ticket for X issue"
  "X not working": "create bug ticket for X"
  "error in X": "create bug ticket for error in X"
  "X fails": "create bug ticket for X failure"
  
Feature Patterns:
  "need X": "create feature ticket for X"
  "add X": "create feature ticket for X"
  "want X": "create feature ticket for X"
  "implement X": "create feature ticket for X"
  "build X": "create feature ticket for X"
  
Improvement Patterns:
  "improve X": "create improvement ticket for X"
  "optimize X": "create optimization ticket for X"
  "update X": "create update ticket for X"
  "enhance X": "create enhancement ticket for X"
  "X slow": "create performance ticket for X"
  
Implementation/Spec Patterns:
  "how to X": "create implementation spec for X"
  "CSS for X": "create implementation spec for X styling"
  "JS for X": "create implementation spec for X JavaScript"
  "code for X": "create implementation spec for X"
  "hide X": "create implementation spec for hiding X"
  "center X": "create implementation spec for centering X"
  "animate X": "create implementation spec for X animation"
  
General Patterns:
  "something about X": "create ticket about X"
  "help with X": "create ticket for X"
  "work on X": "create ticket for X"
  "X stuff": "create ticket for X"
```

### Preserve All Context
When applying patterns, preserve ALL modifiers and context:
- "urgently fix login" → "urgently create bug fix ticket for login"
- "need better API docs" → "create feature ticket for better application programming interface documentation"
- "customer reported DB slow" → "customer reported create performance ticket for database"
- "how to hide scrollbar" → "create implementation spec for hiding scrollbar"

---

## 5. ✅ Enhancement Examples

### Category 1: Simple Abbreviations
```
"update API docs" → "update application programming interface documentation"
"fix auth bug" → "fix authentication bug"
"improve DB perf" → "improve database performance"
"add 2FA to login" → "add two-factor authentication to login"
"FS feature needed" → "full stack feature needed"
```

### Category 2: Vague Structures
```
"fix login" → "create bug fix ticket for login"
"need search" → "create feature ticket for search"
"checkout broken" → "create bug ticket for checkout issue"
"API slow" → "create performance ticket for application programming interface"
```

### Category 3: Implementation Requests (NEW)
```
"how to hide scrollbar" → "create implementation spec for hiding scrollbar"
"CSS for sticky header" → "create implementation spec for sticky header styling"
"JS debounce function" → "create implementation spec for JavaScript debounce function"
"center div vertically" → "create implementation spec for centering div vertically"
"animate button hover" → "create implementation spec for button hover animation"
```

### Category 4: Combined Issues
```
"fix auth API" → "create bug fix ticket for authentication application programming interface"
"need DB optimization" → "create feature ticket for database optimization"
"improve FE perf" → "create improvement ticket for frontend performance"
"urgent: fix UI bug" → "urgent: create bug fix ticket for user interface bug"
"how to implement virtual scroll" → "create implementation spec for virtual scroll"
```

### Category 5: Context Preservation
```
"customers complaining about slow DB queries" 
→ "customers complaining about create performance ticket for slow database queries"

"high priority: add MFA" 
→ "high priority: create feature ticket for multi-factor authentication"

"regression: auth not working after deploy"
→ "regression: create bug ticket for authentication not working after deploy"

"need CSS for responsive grid"
→ "create implementation spec for responsive grid styling"
```

### Category 6: No Change Needed
```
"create feature ticket for user profiles" → (no change)
"$s implement payment processing" → (no change - mode command)
"$spec virtual table" → (no change - mode command)
"bug: login throws 500 error" → (no change - already structured)
"$c real-time collaboration" → (no change - mode command)
```

---

## 6. ❌ What NOT to Do

### Never Add Implementation Details
```
❌ "fix login" → "create ticket to refactor authentication module"
   (Added technical approach)

❌ "DB slow" → "create ticket to add database indexes"
   (Added specific solution)

❌ "need API" → "create ticket for RESTful API implementation"
   (Added architecture decision)

❌ "hide scrollbar" → "create spec using CSS webkit properties"
   (Added specific technical approach)
```

### Never Add Priority or Sizing
```
❌ "fix bug" → "create high-priority bug fix ticket"
   (Added priority assumption)

❌ "add feature" → "create small feature ticket"
   (Added size assumption)

❌ "improve performance" → "create complex performance optimization ticket"
   (Added complexity assumption)
```

### Never Change Core Request Type
```
❌ "update docs" → "create feature ticket for documentation"
   (Changed from update to feature)

❌ "investigate issue" → "create bug ticket for issue"
   (Changed from investigation to bug)

❌ "prototype solution" → "create POC feature ticket"
   (Changed from prototype to full feature)

❌ "how to implement" → "create feature ticket"
   (Changed from spec to feature)
```

### Never Add Business Context
```
❌ "add search" → "create feature ticket for search to improve user retention"
   (Added business goal)

❌ "fix checkout" → "create urgent bug ticket for checkout affecting revenue"
   (Added impact assumption)
```

### Never Skip Mode Detection
```
❌ "$s add feature" → "create feature ticket"
   (Removed mode command)

❌ "$spec hide element" → "create ticket for hiding element"
   (Ignored spec mode)
```

---

## 7. 🚦 Bypass Conditions

Skip enhancement entirely when:

### 1. **Already Clear**
- Contains proper ticket structure
- Has clear action verb and object
- Over 30 words with requirements
- Includes "create ticket" or similar

### 2. **Mode Commands**
- Contains $q, $s, $c, $interactive, $spec
- Mode overrides need for enhancement
- Example: "$s user authentication"
- Example: "$spec virtual scroll"

### 3. **Explicit Ticket Types**
- "bug:", "feature:", "task:", "epic:"
- "story:", "spike:", "chore:"
- Already categorized requests

### 4. **External References**
- Jira ticket numbers (PROJ-123)
- GitHub issue references (#123)
- PR references
- Customer ticket IDs

### 5. **Detailed Specifications**
- Contains acceptance criteria
- Has technical requirements
- Includes user stories
- Multiple bullet points

### 6. **Interactive Mode Triggers**
- "help", "guide me", "not sure"
- Questions about ticket creation
- Requests for examples

### 7. **Direct Implementation Specs**
- "$spec [anything]"
- Already indicates implementation need
- Clear technical request with mode

---

## 8. 📊 Quality Metrics

### Internal Scoring (Not Shown to User)

**Clarity Triggers (enhance if 2+ present):**
- [ ] Contains vague starter (-2 points)
- [ ] Has technical abbreviations (-1 point each)
- [ ] Lacks ticket type indicator (-2 points)
- [ ] Under 5 words (-1 point)
- [ ] Missing clear action (-2 points)
- [ ] Implementation request without $spec (-2 points)

**Enhancement Success Metrics:**
- Processing time: <0.5 seconds
- Original keywords preserved: 100%
- Implementation details added: 0
- Technical assumptions: 0
- User awareness: None
- Spec mode detection accuracy: 95%+

### Pre/Post Examples with Scores

```
"fix auth" 
- Score: 3/10 (vague starter, abbreviation, too short)
- Enhanced: "create bug fix ticket for authentication"
- New Score: 8/10 (clear action, expanded, structured)

"how to hide scrollbar"
- Score: 4/10 (implementation request, no mode)
- Enhanced: "create implementation spec for hiding scrollbar"
- New Score: 9/10 (proper spec mode routing)

"need to add user profile management with avatar upload"
- Score: 8/10 (already clear, good length)
- Enhanced: (no change needed)
- New Score: 8/10

"urgent DB perf issue"
- Score: 4/10 (abbreviations, no clear action)
- Enhanced: "urgent create performance ticket for database issue"
- New Score: 9/10 (maintains urgency, clear structure)
```

---

## 9. 🧪 Testing & Validation

### Test Suite Structure
```
tests/
├── abbreviations/
│   ├── technical_terms.yaml
│   ├── dev_processes.yaml
│   ├── frontend_terms.yaml
│   └── edge_cases.yaml
├── patterns/
│   ├── bug_patterns.yaml
│   ├── feature_patterns.yaml
│   ├── improvement_patterns.yaml
│   └── spec_patterns.yaml
├── preservation/
│   ├── context_preservation.yaml
│   ├── urgency_markers.yaml
│   ├── mode_commands.yaml
│   └── user_intent.yaml
└── bypass/
    ├── mode_commands.yaml
    ├── clear_requests.yaml
    ├── spec_mode.yaml
    └── external_refs.yaml
```

### Critical Test Cases

#### 1. **Abbreviation Expansion**
```yaml
test_basic_abbreviations:
  - input: "fix API"
    expected: "fix application programming interface"
  - input: "update DB schema"
    expected: "update database schema"
  - input: "FE performance"
    expected: "frontend performance"
    
test_multiple_abbreviations:
  - input: "integrate FE with BE API"
    expected: "integrate frontend with backend application programming interface"
```

#### 2. **Pattern Application**
```yaml
test_bug_patterns:
  - input: "login broken"
    expected: "create bug ticket for login issue"
  - input: "search fails with 500"
    expected: "create bug ticket for search failure with 500"
    
test_spec_patterns:
  - input: "how to center div"
    expected: "create implementation spec for centering div"
  - input: "CSS for animation"
    expected: "create implementation spec for animation styling"
```

#### 3. **Mode Preservation**
```yaml
test_mode_commands:
  - input: "$s authentication"
    expected: "$s authentication" # no change
  - input: "$spec virtual table"
    expected: "$spec virtual table" # no change
  - input: "$c payment system"
    expected: "$c payment system" # no change
```

#### 4. **Context Preservation**
```yaml
test_urgency_preservation:
  - input: "URGENT: fix payment bug"
    expected: "URGENT: create bug fix ticket for payment bug"
    
test_detail_preservation:
  - input: "customer reported checkout broken on mobile"
    expected: "customer reported create bug ticket for checkout issue on mobile"
```

#### 5. **Spec Mode Detection**
```yaml
test_implementation_detection:
  - input: "how to implement infinite scroll"
    expected: "create implementation spec for infinite scroll"
  - input: "JS code for debounce"
    expected: "create implementation spec for JavaScript debounce"
  - input: "hide element CSS"
    expected: "create implementation spec for hiding element styling"
```

### Performance Benchmarks
- Average processing time: <200ms
- 95th percentile: <400ms
- 99th percentile: <500ms
- Memory overhead: <10MB

---

## 10. 🔧 Implementation Guide

### Integration Point
This enhancement layer operates in Section 5 of the Writer - Dev Tickets system, positioned between:
- Section 4: MCP Selection (completed)
- Section 6: Request Analysis (begins)

### Process Flow
```
1. User Input
   ↓
2. MCP Selection (Section 4)
   ↓
3. Clarity Check (Section 5) ← YOU ARE HERE
   ↓
4. Enhancement if needed
   ↓
5. Request Analysis (Section 6)
   ↓
6. Mode Detection & Interactive Offers
   ↓
7. Normal ticket creation flow
```

### Implementation Checklist
Before activation, verify:
- [ ] All abbreviations expand correctly
- [ ] Patterns maintain user intent
- [ ] Context always preserved
- [ ] No implementation details added
- [ ] Bypass conditions work correctly
- [ ] Mode commands preserved
- [ ] Spec mode patterns detected
- [ ] Interactive offers unaffected
- [ ] Performance under 500ms

### Monitoring & Iteration
Track these metrics post-deployment:
- Enhancement trigger rate
- Most common abbreviations
- Pattern match frequency
- Spec mode detection rate
- Bypass rate
- User satisfaction with clarity

### Future Enhancements
- Team-specific abbreviation dictionaries
- Context-aware pattern matching
- Machine learning for vague request detection
- Integration with historical tickets

---

## Common Issues & Solutions

### Issue: Over-Enhancement
**Solution**: Tighten bypass conditions, especially for longer requests

### Issue: Wrong Pattern Match
**Solution**: Ensure patterns check full context, not just keywords

### Issue: Lost User Intent
**Solution**: Always preserve original words except abbreviations

### Issue: Breaking Interactive Offers
**Solution**: Never modify $s or $c commands

### Issue: Missing Spec Mode
**Solution**: Expand implementation detection patterns

---

## Success Indicators

### Quantitative
- 30-40% reduction in clarification questions
- 50% faster ticket creation for vague requests
- 95% user intent preservation
- 95%+ spec mode detection accuracy
- <500ms processing time

### Qualitative
- Users unaware of enhancement
- Interactive mode flows naturally
- Spec mode properly triggered
- Interactive offers work correctly
- Clearer tickets without assumptions
- Preserved educational value

---

## Version History

- **v0.200**: Added spec mode detection, updated for v4.0 system with 5 modes
- **v0.100**: Initial implementation for v3.x system

---

*Remember: The goal is clarity without assumption. When in doubt, preserve the original. The Interactive mode and offers will handle any remaining ambiguity through their educational conversation flow. Spec mode detection ensures implementation requests are properly routed.*