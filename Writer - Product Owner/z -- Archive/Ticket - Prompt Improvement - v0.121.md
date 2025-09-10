# Ticket - Prompt Improvement - v0.121

**Lightweight request clarity enhancement** for Dev Ticket Writer system. Rules and patterns for improving developer request clarity without adding assumptions.

## Table of Contents

1. [🎯 CORE PRINCIPLES](#1--core-principles)
2. [📝 ENHANCEMENT RULES](#2--enhancement-rules)
3. [📤 ABBREVIATION DICTIONARY](#3--abbreviation-dictionary)
4. [📄 STRUCTURE PATTERNS](#4--structure-patterns)
5. [✅ ENHANCEMENT EXAMPLES](#5--enhancement-examples)
6. [❌ WHAT NOT TO DO](#6--what-not-to-do)
7. [🚦 BYPASS CONDITIONS](#7--bypass-conditions)
8. [📊 QUALITY METRICS](#8--quality-metrics)
9. [🧪 TESTING & VALIDATION](#9--testing--validation)
10. [🔧 IMPLEMENTATION GUIDE](#10--implementation-guide)

---

## 1. 🎯 CORE PRINCIPLES

1. **Clarity Only**: Improve structure/phrasing, never add implementation
2. **Preserve Intent**: Keep all original keywords/meaning
3. **No Technical Assumptions**: Never infer architecture/complexity
4. **Invisible Process**: User unaware of enhancement
5. **Interactive Integrity**: All questions/offers still asked
6. **Spec Detection**: Recognize implementation requests
7. **Concise Enhancement**: Keep improvements brief

---

## 2. 📝 ENHANCEMENT RULES

### Rule 1: Expand Abbreviations
Only from approved dictionary. Never guess unlisted.

### Rule 2: Structure Vague Starters
Apply approved patterns without changing meaning.

### Rule 3: Preserve Keywords
Every original word appears (except replaced abbreviations).

### Rule 4: Minimal Additions
Only add: "ticket for", "issue", "about", "regarding"
Never add technical descriptors.

### Rule 5: Grammar Only
Fix only clarity-impeding issues.

### Rule 6: Detect Implementation
Recognize $spec mode patterns.

---

## 3. 📤 ABBREVIATION DICTIONARY

### Core Technical
```yaml
API: application programming interface
DB: database
UI: user interface
UX: user experience
FE: frontend
BE: backend
FS: full stack

auth: authentication
config: configuration
env: environment
repo: repository
infra: infrastructure
k8s: kubernetes

QA: quality assurance
CI: continuous integration
CD: continuous deployment
CI/CD: continuous integration/continuous deployment
MVP: minimum viable product
POC: proof of concept
PR: pull request

perf: performance
opt: optimization
mem: memory

sec: security
vuln: vulnerability
2FA: two-factor authentication
MFA: multi-factor authentication

JS: JavaScript
TS: TypeScript
ctx: context
props: properties

e2e: end-to-end
```

### Ticket Types (Implicit)
```yaml
bug: bug fix
feat: feature
docs: documentation
test: testing
perf: performance
sec: security
impl: implementation
spec: specification
```

**Note**: Only expand exact matches.

---

## 4. 📄 STRUCTURE PATTERNS

### Bug Patterns
```yaml
"fix X": "create bug fix ticket for X"
"X broken": "create bug ticket for X issue"
"X not working": "create bug ticket for X"
"error in X": "create bug ticket for error in X"
"X fails": "create bug ticket for X failure"
```

### Feature Patterns
```yaml
"need X": "create feature ticket for X"
"add X": "create feature ticket for X"
"want X": "create feature ticket for X"
"implement X": "create feature ticket for X"
"build X": "create feature ticket for X"
```

### Improvement Patterns
```yaml
"improve X": "create improvement ticket for X"
"optimize X": "create optimization ticket for X"
"update X": "create update ticket for X"
"enhance X": "create enhancement ticket for X"
"X slow": "create performance ticket for X"
```

### Implementation/Spec Patterns
```yaml
"how to X": "create implementation spec for X"
"CSS for X": "create implementation spec for X styling"
"JS for X": "create implementation spec for X JavaScript"
"code for X": "create implementation spec for X"
"hide X": "create implementation spec for hiding X"
"center X": "create implementation spec for centering X"
```

### General Patterns
```yaml
"something about X": "create ticket about X"
"help with X": "create ticket for X"
"work on X": "create ticket for X"
```

### Preserve Context
- "urgently fix login" → "urgently create bug fix ticket for login"
- "need better API docs" → "create feature ticket for better application programming interface documentation"
- "how to hide scrollbar" → "create implementation spec for hiding scrollbar"

---

## 5. ✅ ENHANCEMENT EXAMPLES

### Simple Abbreviations
```
"update API docs" → "update application programming interface documentation"
"fix auth bug" → "fix authentication bug"
"improve DB perf" → "improve database performance"
"add 2FA" → "add two-factor authentication"
```

### Vague Structures
```
"fix login" → "create bug fix ticket for login"
"need search" → "create feature ticket for search"
"checkout broken" → "create bug ticket for checkout issue"
"API slow" → "create performance ticket for application programming interface"
```

### Implementation Requests
```
"how to hide scrollbar" → "create implementation spec for hiding scrollbar"
"CSS for sticky header" → "create implementation spec for sticky header styling"
"center div vertically" → "create implementation spec for centering div vertically"
```

### Combined Issues
```
"fix auth API" → "create bug fix ticket for authentication application programming interface"
"need DB optimization" → "create feature ticket for database optimization"
"improve FE perf" → "create improvement ticket for frontend performance"
```

### Context Preservation
```
"customers complaining about slow DB" 
→ "customers complaining about create performance ticket for slow database"

"high priority: add MFA" 
→ "high priority: create feature ticket for multi-factor authentication"

"need CSS for responsive grid"
→ "create implementation spec for responsive grid styling"
```

### No Change Needed
```
"create feature ticket for user profiles" → (no change)
"$s implement payment processing" → (no change - mode)
"bug: login throws 500 error" → (no change - structured)
```

---

## 6. ❌ WHAT NOT TO DO

### Never Add Implementation
```
❌ "fix login" → "create ticket to refactor authentication"
❌ "DB slow" → "create ticket to add database indexes"
❌ "need API" → "create ticket for RESTful API"
```

### Never Add Priority
```
❌ "fix bug" → "create high-priority bug ticket"
❌ "add feature" → "create small feature ticket"
```

### Never Change Type
```
❌ "update docs" → "create feature ticket for documentation"
❌ "investigate issue" → "create bug ticket for issue"
```

### Never Add Context
```
❌ "add search" → "create feature ticket for search to improve retention"
❌ "fix checkout" → "create urgent bug ticket affecting revenue"
```

### Never Skip Modes
```
❌ "$s add feature" → "create feature ticket"
❌ "$spec hide element" → "create ticket for hiding element"
```

---

## 7. 🚦 BYPASS CONDITIONS

Skip enhancement when:

### 1. **Already Clear**
- Proper ticket structure
- Clear action and object
- Over 30 words with requirements

### 2. **Mode Commands**
- Contains $q, $s, $c, $interactive, $spec
- Example: "$s user authentication"

### 3. **Explicit Types**
- "bug:", "feature:", "task:"
- Already categorized

### 4. **External References**
- Jira tickets (PROJ-123)
- GitHub issues (#123)
- PR references

### 5. **Detailed Specs**
- Contains acceptance criteria
- Has requirements
- Multiple bullet points

### 6. **Interactive Triggers**
- "help", "guide me", "not sure"
- Questions about tickets

### 7. **Direct Specs**
- "$spec [anything]"
- Clear technical request with mode

---

## 8. 📊 QUALITY METRICS

### Clarity Triggers (enhance if 2+)
- [ ] Vague starter (-2)
- [ ] Technical abbreviations (-1 each)
- [ ] No ticket type (-2)
- [ ] Under 5 words (-1)
- [ ] Missing action (-2)
- [ ] Implementation without $spec (-2)

### Success Metrics
- Processing: <0.5 seconds
- Keywords preserved: 100%
- Implementation added: 0
- Assumptions: 0
- Spec detection: 95%+

### Score Examples
```
"fix auth" 
- Score: 3/10 (vague, abbreviation, short)
- Enhanced: "create bug fix ticket for authentication"
- New: 8/10

"how to hide scrollbar"
- Score: 4/10 (implementation, no mode)
- Enhanced: "create implementation spec for hiding scrollbar"
- New: 9/10

"need to add user profile management with avatar"
- Score: 8/10 (clear, good length)
- Enhanced: (no change)
- New: 8/10
```

---

## 9. 🧪 TESTING & VALIDATION

### Test Structure
```
tests/
├── abbreviations/
│   ├── technical.yaml
│   ├── frontend.yaml
│   └── edge_cases.yaml
├── patterns/
│   ├── bug.yaml
│   ├── feature.yaml
│   ├── improvement.yaml
│   └── spec.yaml
├── preservation/
│   ├── context.yaml
│   ├── urgency.yaml
│   └── modes.yaml
└── bypass/
    ├── mode_commands.yaml
    ├── clear_requests.yaml
    └── specs.yaml
```

### Critical Tests

#### Abbreviations
```yaml
test_basic:
  - input: "fix API"
    expected: "fix application programming interface"
  - input: "update DB"
    expected: "update database"
    
test_multiple:
  - input: "integrate FE with BE API"
    expected: "integrate frontend with backend application programming interface"
```

#### Patterns
```yaml
test_bug:
  - input: "login broken"
    expected: "create bug ticket for login issue"
    
test_spec:
  - input: "how to center div"
    expected: "create implementation spec for centering div"
```

#### Mode Preservation
```yaml
test_modes:
  - input: "$s authentication"
    expected: "$s authentication" # no change
  - input: "$spec virtual table"
    expected: "$spec virtual table" # no change
```

### Performance Benchmarks
- Average: <200ms
- 95th percentile: <400ms
- 99th percentile: <500ms
- Memory: <10MB

---

## 10. 🔧 IMPLEMENTATION GUIDE

### Integration Point
Operates in Section 5 of Writer - Dev Tickets system:
- After: MCP Selection (Section 4)
- Before: Request Analysis (Section 6)

### Process Flow
```
1. User Input
   ↓
2. MCP Selection
   ↓
3. Clarity Check ← HERE
   ↓
4. Enhancement if needed
   ↓
5. Request Analysis
   ↓
6. Mode Detection
   ↓
7. Normal flow
```

### Implementation Checklist
- [ ] Abbreviations expand correctly
- [ ] Patterns maintain intent
- [ ] Context preserved
- [ ] No implementation added
- [ ] Bypass conditions work
- [ ] Mode commands preserved
- [ ] Spec patterns detected
- [ ] Interactive unaffected
- [ ] Performance <500ms

### Monitoring
Track:
- Enhancement trigger rate
- Common abbreviations
- Pattern matches
- Spec detection rate
- Bypass rate
- User satisfaction

### Common Issues

**Over-Enhancement**
Solution: Tighten bypass conditions

**Wrong Pattern**
Solution: Check full context

**Lost Intent**
Solution: Preserve original words

**Breaking Interactive**
Solution: Never modify $s/$c

**Missing Spec**
Solution: Expand detection patterns

---

## Success Indicators

### Quantitative
- 30% fewer clarifications
- 50% faster for vague requests
- 95% intent preservation
- 95% spec detection
- <500ms processing

### Qualitative
- Users unaware
- Interactive flows naturally
- Spec properly triggered
- Clearer tickets
- Educational value preserved

---

## Version History

- **v0.421**: Maintained conciseness standards
- **v0.420**: 20% more concise documentation, streamlined patterns
- **v0.400**: Added spec mode detection, updated for 5 modes
- **v0.100**: Initial implementation

---

*Goal: Clarity without assumption. When in doubt, preserve original. Interactive mode handles remaining ambiguity. Spec mode catches implementation requests.*