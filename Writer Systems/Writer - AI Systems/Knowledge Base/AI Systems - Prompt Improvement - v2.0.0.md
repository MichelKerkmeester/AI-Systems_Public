# AI Systems - Prompt Improvement - v2.0.0

**Lightweight request clarity enhancement** for the AI Systems Spec Writer. This document contains all rules, patterns, and examples for improving specification request clarity without adding assumptions.

## Table of Contents

1. [🎯 CORE PRINCIPLES](#1--core-principles)
2. [📝 ENHANCEMENT RULES](#2--enhancement-rules)
3. [🔤 ABBREVIATION DICTIONARY](#3--abbreviation-dictionary)
4. [🔄 STRUCTURE PATTERNS](#4--structure-patterns)
5. [✅ ENHANCEMENT EXAMPLES](#5--enhancement-examples)
6. [❌ WHAT NOT TO DO](#6--what-not-to-do)
7. [🚦 BYPASS CONDITIONS](#7--bypass-conditions)
8. [📊 QUALITY METRICS](#8--quality-metrics)
9. [🧪 TESTING & VALIDATION](#9--testing--validation)
10. [🔧 IMPLEMENTATION GUIDE](#10--implementation-guide)

---

## 1. 🎯 CORE PRINCIPLES

The Request Clarity Enhancement layer follows these immutable principles:

1. **Clarity Only**: Improve structure and phrasing, never add architectural assumptions
2. **Preserve Intent**: All original keywords and meaning must remain
3. **No Technical Assumptions**: Never infer patterns, complexity, or approach
4. **Invisible Process**: User should be unaware of enhancement
5. **Mode Integrity**: All mode selections and flows remain unchanged

**Remember**: This is about making requests clearer for the spec writer to understand, NOT about making technical decisions or adding context.

---

## 2. 📝 ENHANCEMENT RULES

### Rule 1: Expand Abbreviations
Only expand from the approved dictionary (Section 3). Never guess at abbreviations not in the list.

### Rule 2: Structure Vague Starters
Apply approved patterns (Section 4) to improve request structure without changing meaning.

### Rule 3: Preserve Keywords
Every word from the original request must appear in the enhanced version (except replaced abbreviations).

### Rule 4: Minimal Additions
Only add specification-type indicators and grammatical connectors:
- "specification for", "system", "architecture", "documentation"
- Never add technical descriptors or complexity hints

### Rule 5: Grammar Only
Fix only grammatical issues that impede clarity. Don't improve technical accuracy or add details.

---

## 3. 🔤 ABBREVIATION DICTIONARY

### Technical Terms
```yaml
Core Technical:
  AI: artificial intelligence
  ML: machine learning
  API: application programming interface
  DB: database
  UI: user interface
  UX: user experience
  
Architecture:
  auth: authentication
  config: configuration
  env: environment
  repo: repository
  k8s: kubernetes
  
Development:
  CI/CD: continuous integration/continuous deployment
  MVP: minimum viable product
  POC: proof of concept
  QA: quality assurance
  
Patterns:
  MCP: Model Context Protocol
  CRUD: create, read, update, delete
  REST: representational state transfer
  SPA: single page application
```

### System Types (Implicit)
```yaml
# These help structure but aren't explicitly stated
spec: specification
docs: documentation
arch: architecture
impl: implementation
```

**Note**: Only expand abbreviations in this exact list. All others remain unchanged.

---

## 4. 🔄 STRUCTURE PATTERNS

### Vague Starter Transformations
Apply these exact patterns when detected:

```yaml
Analysis Patterns:
  "analyze X": "analyze X system"
  "review X": "analyze X system"
  "check X": "analyze X system"
  "look at X": "analyze X"
  
Creation Patterns:
  "need X": "create specification for X"
  "want X": "create specification for X"
  "build X": "create specification for X"
  "make X": "create specification for X"
  "design X": "create specification for X"
  
Update Patterns:
  "improve X": "update specification for X"
  "enhance X": "update specification for X"
  "fix X": "update specification for X"
  "change X": "update specification for X"
  
General Patterns:
  "something about X": "create specification about X"
  "help with X": "create specification for X"
  "work on X": "create specification for X"
  "X stuff": "specification for X"
  "X system": "X system" (no change if already has system)
```

### Preserve All Context
When applying patterns, preserve ALL modifiers and context:
- "urgently need auth" → "urgently create specification for authentication"
- "simple AI chatbot" → "create specification for simple artificial intelligence chatbot"
- "analyze existing ML pipeline" → "analyze existing machine learning pipeline system"

---

## 5. ✅ ENHANCEMENT EXAMPLES

### Category 1: Simple Abbreviations
```
"analyze AI system" → "analyze artificial intelligence system"
"ML model spec" → "machine learning model specification"
"update API docs" → "update application programming interface documentation"
"auth flow design" → "authentication flow design"
```

### Category 2: Vague Structures
```
"need chatbot" → "create specification for chatbot"
"analyze payment" → "analyze payment system"
"something for ML" → "create specification for machine learning"
"help with AI" → "create specification for artificial intelligence"
```

### Category 3: Combined Issues
```
"need AI/ML system" → "create specification for artificial intelligence/machine learning system"
"analyze auth API" → "analyze authentication application programming interface system"
"update DB architecture" → "update database architecture"
"want k8s deployment" → "create specification for kubernetes deployment"
```

### Category 4: Context Preservation
```
"complex AI system for healthcare" 
→ "create specification for complex artificial intelligence system for healthcare"

"urgently need simple chatbot MVP"
→ "urgently create specification for simple chatbot minimum viable product"

"analyze our existing ML pipeline architecture"
→ "analyze our existing machine learning pipeline architecture"
```

### Category 5: No Change Needed
```
"$analyze authentication system" → (no change - mode command)
"create specification for user management" → (no change - already clear)
"analyze the payment processing system" → (no change - already structured)
```

---

## 6. ❌ WHAT NOT TO DO

### Never Add Architecture Details
```
❌ "need AI" → "create specification for microservices-based AI system"
   (Added architecture assumption)

❌ "chatbot" → "create specification for NLP-powered chatbot"
   (Added technical approach)

❌ "payment system" → "create specification for scalable payment system"
   (Added quality assumption)
```

### Never Add Complexity or Scope
```
❌ "analyze system" → "analyze complex enterprise system"
   (Added complexity assumption)

❌ "need API" → "create specification for RESTful API"
   (Added implementation detail)

❌ "update spec" → "create minor update specification"
   (Added scope assumption)
```

### Never Change Core Request Type
```
❌ "review architecture" → "create new architecture specification"
   (Changed from review to create)

❌ "questions about AI" → "create AI system specification"
   (Changed from question to creation)

❌ "fix documentation" → "create new documentation"
   (Changed from fix to create)
```

### Never Add Pattern Assumptions
```
❌ "user system" → "create specification using Mode System Pattern"
   (Added pattern decision)

❌ "need quality" → "create specification with SPACE framework"
   (Added framework assumption)
```

---

## 7. 🚦 BYPASS CONDITIONS

Skip enhancement entirely when:

### 1. **Already Clear**
- Contains proper specification structure
- Has clear action verb and system/specification object
- Over 20 words with requirements
- Includes "create specification" or similar

### 2. **Mode Commands**
- Contains $analyze, $create, $update, $integrate, $readme, $full, $evaluate, $interactive
- Mode overrides need for enhancement
- Example: "$analyze user authentication"

### 3. **Explicit System Types**
- "microservices architecture"
- "event-driven system"
- "monolithic application"
- Already has architectural context

### 4. **Existing Analysis**
- References to current systems
- "our", "existing", "current" keywords
- Version numbers mentioned
- Previous specification references

### 5. **Detailed Specifications**
- Contains requirements lists
- Has success criteria
- Includes use cases
- Multiple components mentioned

### 6. **Interactive Mode Triggers**
- "help", "guide me", "not sure"
- Questions about the process
- Requests for examples

---

## 8. 📊 QUALITY METRICS

### Internal Scoring (Not Shown to User)

**Clarity Triggers (enhance if 2+ present):**
- [ ] Contains vague starter (-2 points)
- [ ] Has technical abbreviations (-1 point each)
- [ ] Lacks specification indicator (-2 points)
- [ ] Under 5 words (-1 point)
- [ ] Missing clear action (-2 points)

**Enhancement Success Metrics:**
- Processing time: <0.5 seconds
- Original keywords preserved: 100%
- Architectural assumptions added: 0
- Technical decisions made: 0
- User awareness: None

### Pre/Post Examples with Scores

```
"need AI" 
- Score: 2/10 (vague starter, abbreviation, too short)
- Enhanced: "create specification for artificial intelligence"
- New Score: 8/10 (clear action, expanded, structured)

"analyze the user authentication and authorization system"
- Score: 9/10 (already clear, good length)
- Enhanced: (no change needed)
- New Score: 9/10

"ML/AI stuff for data"
- Score: 3/10 (abbreviations, vague structure)
- Enhanced: "create specification for machine learning/artificial intelligence for data"
- New Score: 8/10 (expanded, clear structure)
```

---

## 9. 🧪 TESTING & VALIDATION

### Test Suite Structure
```
tests/
├── abbreviations/
│   ├── technical_terms.yaml
│   ├── architecture_terms.yaml
│   └── edge_cases.yaml
├── patterns/
│   ├── analysis_patterns.yaml
│   ├── creation_patterns.yaml
│   └── update_patterns.yaml
├── preservation/
│   ├── context_preservation.yaml
│   ├── modifier_preservation.yaml
│   └── intent_preservation.yaml
└── bypass/
    ├── mode_commands.yaml
    ├── clear_requests.yaml
    └── existing_systems.yaml
```

### Critical Test Cases

#### 1. **Abbreviation Expansion**
```yaml
test_basic_abbreviations:
  - input: "AI system"
    expected: "artificial intelligence system"
  - input: "ML/AI integration"
    expected: "machine learning/artificial intelligence integration"
    
test_architecture_abbreviations:
  - input: "k8s deployment spec"
    expected: "kubernetes deployment specification"
```

#### 2. **Pattern Application**
```yaml
test_creation_patterns:
  - input: "need chatbot"
    expected: "create specification for chatbot"
  - input: "want AI assistant"
    expected: "create specification for artificial intelligence assistant"
    
test_analysis_patterns:
  - input: "analyze payment"
    expected: "analyze payment system"
  - input: "review auth flow"
    expected: "analyze authentication flow system"
```

#### 3. **Context Preservation**
```yaml
test_modifier_preservation:
  - input: "simple AI chatbot"
    expected: "create specification for simple artificial intelligence chatbot"
    
test_detail_preservation:
  - input: "complex multi-tenant SaaS platform"
    expected: "create specification for complex multi-tenant SaaS platform"
```

#### 4. **Bypass Validation**
```yaml
test_mode_bypass:
  - input: "$analyze authentication system"
    expected: "$analyze authentication system" # no change
    
test_clear_bypass:
  - input: "create specification for user management system"
    expected: "create specification for user management system" # no change
```

### Performance Benchmarks
- Average processing time: <200ms
- 95th percentile: <400ms
- 99th percentile: <500ms
- Memory overhead: <10MB

---

## 10. 🔧 IMPLEMENTATION GUIDE

### Integration Point
This enhancement layer operates between:
- MCP Selection (completed)
- Mode Activation (begins)

### Process Flow
```
1. User Input
   ↓
2. MCP Selection
   ↓
3. Clarity Check ← YOU ARE HERE
   ↓
4. Enhancement if needed
   ↓
5. Mode Activation
   ↓
6. Normal specification flow
```

### Implementation Checklist
Before activation, verify:
- [ ] All abbreviations expand correctly
- [ ] Patterns maintain user intent
- [ ] Context always preserved
- [ ] No architectural assumptions added
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
- Domain-specific abbreviation sets
- Context-aware pattern matching
- Machine learning for vague request detection
- Integration with pattern library

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
- 50% faster specification creation for vague requests
- 95% user intent preservation
- <500ms processing time

### Qualitative
- Users unaware of enhancement
- Interactive mode flows naturally
- Clearer specifications without assumptions
- Preserved educational value

---

*Remember: The goal is clarity without assumption. When in doubt, preserve the original. The Interactive mode will handle any remaining ambiguity through its educational conversation flow.*