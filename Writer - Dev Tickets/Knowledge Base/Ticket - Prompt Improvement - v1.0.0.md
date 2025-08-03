# Ticket - Prompt Improvement - v1.0.0

**Lightweight request clarity enhancement** for the Dev Ticket Writer system. This document contains all rules, patterns, and examples for improving developer request clarity without adding implementation assumptions.

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
5. **Interactive Integrity**: All Interactive mode questions still get asked

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
  2FA: two-factor authentication
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

---

## 5. ✅ Enhancement Examples

### Category 1: Simple Abbreviations
```
"update API docs" → "update application programming interface documentation"
"fix auth bug" → "fix authentication bug"
"improve DB perf" → "improve database performance"
"add 2FA to login" → "add two-factor authentication to login"
```

### Category 2: Vague Structures
```
"fix login" → "create bug fix ticket for login"
"need search" → "create feature ticket for search"
"checkout broken" → "create bug ticket for checkout issue"
"API slow" → "create performance ticket for application programming interface"
```

### Category 3: Combined Issues
```
"fix auth API" → "create bug fix ticket for authentication application programming interface"
"need DB optimization" → "create feature ticket for database optimization"
"improve FE perf" → "create improvement ticket for frontend performance"
"urgent: fix UI bug" → "urgent: create bug fix ticket for user interface bug"
```

### Category 4: Context Preservation
```
"customers complaining about slow DB queries" 
→ "customers complaining about create performance ticket for slow database queries"

"high priority: add 2FA" 
→ "high priority: create feature ticket for two-factor authentication"

"regression: auth not working after deploy"
→ "regression: create bug ticket for authentication not working after deploy"
```

### Category 5: No Change Needed
```
"create feature ticket for user profiles" → (no change)
"$s implement payment processing" → (no change - mode command)
"bug: login throws 500 error" → (no change - already structured)
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
```

### Never Add Business Context
```
❌ "add search" → "create feature ticket for search to improve user retention"
   (Added business goal)

❌ "fix checkout" → "create urgent bug ticket for checkout affecting revenue"
   (Added impact assumption)
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
- Contains $q, $s, $c, $e, $interactive
- Mode overrides need for enhancement
- Example: "$s user authentication"

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

---

## 8. 📊 Quality Metrics

### Internal Scoring (Not Shown to User)

**Clarity Triggers (enhance if 2+ present):**
- [ ] Contains vague starter (-2 points)
- [ ] Has technical abbreviations (-1 point each)
- [ ] Lacks ticket type indicator (-2 points)
- [ ] Under 5 words (-1 point)
- [ ] Missing clear action (-2 points)

**Enhancement Success Metrics:**
- Processing time: <0.5 seconds
- Original keywords preserved: 100%
- Implementation details added: 0
- Technical assumptions: 0
- User awareness: None

### Pre/Post Examples with Scores

```
"fix auth" 
- Score: 3/10 (vague starter, abbreviation, too short)
- Enhanced: "create bug fix ticket for authentication"
- New Score: 8/10 (clear action, expanded, structured)

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
│   └── edge_cases.yaml
├── patterns/
│   ├── bug_patterns.yaml
│   ├── feature_patterns.yaml
│   └── improvement_patterns.yaml
├── preservation/
│   ├── context_preservation.yaml
│   ├── urgency_markers.yaml
│   └── user_intent.yaml
└── bypass/
    ├── mode_commands.yaml
    ├── clear_requests.yaml
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
    
test_feature_patterns:
  - input: "need dashboard"
    expected: "create feature ticket for dashboard"
  - input: "add reporting"
    expected: "create feature ticket for reporting"
```

#### 3. **Context Preservation**
```yaml
test_urgency_preservation:
  - input: "URGENT: fix payment bug"
    expected: "URGENT: create bug fix ticket for payment bug"
    
test_detail_preservation:
  - input: "customer reported checkout broken on mobile"
    expected: "customer reported create bug ticket for checkout issue on mobile"
```

#### 4. **Bypass Validation**
```yaml
test_mode_bypass:
  - input: "$s authentication system"
    expected: "$s authentication system" # no change
    
test_clear_bypass:
  - input: "create feature ticket for user management"
    expected: "create feature ticket for user management" # no change
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
6. Normal ticket creation flow
```

### Implementation Checklist
Before activation, verify:
- [ ] All abbreviations expand correctly
- [ ] Patterns maintain user intent
- [ ] Context always preserved
- [ ] No implementation details added
- [ ] Bypass conditions work correctly
- [ ] Interactive mode unaffected
- [ ] Performance under 500ms

### Monitoring & Iteration
Track these metrics post-deployment:
- Enhancement trigger rate
- Most common abbreviations
- Pattern match frequency
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

### Issue: Breaking Interactive Mode
**Solution**: Never enhance requests with help keywords

---

## Success Indicators

### Quantitative
- 30-40% reduction in clarification questions
- 50% faster ticket creation for vague requests
- 95% user intent preservation
- <500ms processing time

### Qualitative
- Users unaware of enhancement
- Interactive mode flows naturally
- Clearer tickets without assumptions
- Preserved educational value

---

*Remember: The goal is clarity without assumption. When in doubt, preserve the original. The Interactive mode will handle any remaining ambiguity through its educational conversation flow.*