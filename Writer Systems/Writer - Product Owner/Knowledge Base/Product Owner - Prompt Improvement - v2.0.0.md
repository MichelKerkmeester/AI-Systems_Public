# Product Owner - Prompt Improvement - v6.0.0

Lightweight request clarity enhancement for Product Owner system with 5 intelligent modes.

## 📑 Table of Contents

1. [🎯 CORE PRINCIPLES](#-core-principles)
2. [📝 ENHANCEMENT RULES](#-enhancement-rules)
3. [📤 ABBREVIATION DICTIONARY](#-abbreviation-dictionary)
4. [🔄 STRUCTURE PATTERNS](#-structure-patterns)
5. [🔗 MODE DETECTION](#-mode-detection)
6. [⚡ QUICK EXAMPLES](#-quick-examples)
7. [🚦 BYPASS CONDITIONS](#-bypass-conditions)
8. [📊 IMPLEMENTATION](#-implementation)

---

## 🎯 CORE PRINCIPLES

1. **Clarity Only** - Improve structure, never add implementation
2. **Preserve Intent** - Keep all original meaning/keywords
3. **No Assumptions** - Never infer complexity or architecture
4. **Mode Aware** - Detect $ticket, $spec, $doc, $text patterns
5. **Invisible Process** - User unaware of enhancement

---

## 📝 ENHANCEMENT RULES

### Primary Rules
- **Expand abbreviations** - Only from approved dictionary
- **Structure for clarity** - Apply minimal patterns
- **Preserve keywords** - Every original word appears
- **Minimal additions** - Only: "create", "for", "about"
- **Grammar only** - Fix clarity-impeding issues

### Never Add
- ❌ Technical descriptors or implementation details
- ❌ Complexity indicators (simple/complex/standard)
- ❌ Platform terms (sprint/kanban/ClickUp)
- ❌ Thinking suggestions (rounds/depth)
- ❌ Mode assumptions beyond patterns

---

## 📤 ABBREVIATION DICTIONARY

### Core Technical
```yaml
# Common
API: application programming interface
DB: database
UI/UX: user interface/experience
FE/BE/FS: frontend/backend/full stack
QA: quality assurance
auth: authentication
config: configuration

# Development
CI/CD: continuous integration/deployment
MVP: minimum viable product
POC: proof of concept
2FA/MFA: two/multi-factor authentication

# Performance
perf: performance
opt: optimization
mem: memory

# Languages
JS/TS: JavaScript/TypeScript
```

### Keep As-Is
```yaml
# Don't expand these:
sprint, kanban, workspace, epic, story
simple, complex, standard
rounds, thinking
```

---

## 🔄 STRUCTURE PATTERNS

### Ticket Patterns
```yaml
"fix X" → "create ticket for X fix"
"X broken" → "create ticket for X issue"
"need X" → "create ticket for X"
"add X" → "create ticket for X feature"
```

### Spec Patterns
```yaml
"how to X" → "create spec for X"
"build X component" → "create spec for X component"
"CSS/JS for X" → "create spec for X [language]"
```

### Documentation Patterns
```yaml
"document X" → "create documentation for X"
"explain X" → "create documentation for X"
"guide for X" → "create documentation for X"
```

### Text Patterns (NEW)
```yaml
"error message for X" → "create text for X error"
"description of X" → "create text describing X"
"copy for X" → "create text for X"
```

---

## 🔗 MODE DETECTION

### Direct Commands (No Enhancement)
| Command | Mode | Thinking |
|---------|------|----------|
| `$ticket` | Direct ticket | After command |
| `$spec` | Direct spec | After command |
| `$doc` | Direct doc | After command |
| `$text` | Direct text | After command |

### Pattern → Discovery Flow
| Pattern | Enhanced To | Leads To |
|---------|------------|----------|
| "fix X" | "create ticket for X fix" | Discovery → Ticket |
| "how to X" | "create spec for X" | Discovery → Spec |
| "document X" | "create documentation for X" | Discovery → Doc |
| "message for X" | "create text for X" | Discovery → Text |
| Unclear | Minimal clarity | Discovery flow |

---

## ⚡ QUICK EXAMPLES

### Simple Enhancements
```
"fix auth bug" → "fix authentication bug"
"API docs" → "application programming interface documentation"
"need 2FA" → "need two-factor authentication"
"error msg" → "error message"
```

### Mode Preservation
```
"$ticket payment" → (no change)
"$spec modal" → (no change)
"$doc API" → "$doc application programming interface"
"$text welcome msg" → "$text welcome message"
```

### Structure Improvements
```
"login broken" → "create ticket for login issue"
"center div" → "create spec for centering div"
"explain dashboard" → "create documentation for dashboard"
"404 text" → "create text for 404 error"
```

### Never Do
```
❌ "fix bug" → "create simple bug ticket"
❌ "add feature" → "complex feature with phases"
❌ "docs" → "ClickUp documentation"
❌ "quick fix" → "1-2 thinking rounds fix"
```

---

## 🚦 BYPASS CONDITIONS

Skip enhancement when:

1. **Mode commands present** - $ticket, $spec, $doc, $text
2. **Already structured** - Over 30 words, has requirements
3. **External references** - JIRA-123, #456, URLs
4. **Platform specified** - "add to ClickUp", "create in workspace"
5. **Detailed specs** - Bullet points, acceptance criteria

---

## 📊 IMPLEMENTATION

### Process Flow
```
User Input
    ↓
Clarity Check (<500ms)
    ↓
Enhancement (if needed)
    ↓
Mode Detection
    ↓
Interactive Flow
    ↓
Content Creation
```

### Quality Metrics
- Processing: <0.5 seconds
- Keywords preserved: 100%
- Assumptions added: 0
- Mode detection: 95%+

### Integration Point
- **After:** User input received
- **Before:** Mode routing begins
- **Invisible:** No user awareness

---

*Clarity without assumptions. Five modes supported. Interactive flow ready.*