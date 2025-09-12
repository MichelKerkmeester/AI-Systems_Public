# Product Owner - Template: Spec Mode - v0.102

## 📋 Table Of Contents

1. [🔧 Spec Mode Overview](#1-🔧-spec-mode-overview)
2. [📊 Spec Types & Frameworks](#2-📊-spec-types--frameworks)
3. [🎯 Minimal Spec Template](#3-🎯-minimal-spec-template)
4. [📝 Standard Spec Template](#4-📝-standard-spec-template)
5. [🏗️ Complex Spec Template](#5-🏗️-complex-spec-template)
6. [💻 Code Examples By Type](#6-💻-code-examples-by-type)
7. [🎨 Formatting Standards](#7-🎨-formatting-standards)
8. [💬 Interactive Questions](#8-💬-interactive-questions)

---

## 1. 🔧 Spec Mode Overview

### Command: `$spec`

- **Purpose:** Create implementation specifications for frontend components/features
- **Output:** Always as artifact
- **Thinking Rounds:** 6-10
- **Challenge Activation:** 6+ rounds (lean implementation vs full)

### Default Approach
1. **Minimal first** - Start with simplest solution
2. **Native when possible** - Use platform capabilities
3. **Dependencies last** - Only add when essential

---

## 2. 📊 Spec Types & Frameworks

### Supported Frameworks
| Framework | Common Use | Default Approach |
|-----------|------------|------------------|
| **React** | Components, Hooks | Functional, minimal state |
| **Vue** | Components, Stores | Composition API |
| **Angular** | Services, Components | Standalone components |
| **Vanilla JS** | Utilities, DOM | Modern ES6+, no build |
| **CSS/Tailwind** | Styling, Layouts | Utility-first |

### Complexity Levels
| Level | Lines of Code | Dependencies | Use Case |
|-------|--------------|--------------|----------|
| **Minimal** | <50 | 0 | Single responsibility |
| **Standard** | 50-150 | 1-2 | Feature component |
| **Complex** | 150+ | 3+ | Full system |

---

## 3. 🎯 Minimal Spec Template

```markdown
# Minimal Implementation: [Component Name]

## Objective
[One-line description of what we're building]

## Approach
Using [native/framework] with zero dependencies for maximum simplicity.

## Implementation

### Core Structure
```javascript
// [Framework] - [Component Name]
// Zero dependencies, ~30 lines

[Core implementation code]
```

### Usage Example
```javascript
[Simple usage example]
```

## Testing Approach
- Unit test for [core functionality]
- Integration test for [user flow]

## Deployment Notes
- No build step required
- Compatible with [browsers/versions]

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $spec
- **Type:** [React/Vue/Vanilla/etc]
- **Complexity:** Minimal

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** A→T→L→S

---

- **Challenge:** Applied - Reduced from library to native solution
- **Context:** Minimal implementation requested
```

---

## 4. 📝 Standard Spec Template

```markdown
# Standard Implementation: [Feature Name]

## Executive Summary
[Brief description of the feature and its value proposition]

## Technical Approach

### Architecture Decision
- **Framework:** [React/Vue/Angular/Vanilla]
- **State Management:** [Local/Context/Store]
- **Styling:** [CSS Modules/Tailwind/Styled Components]
- **Testing:** [Jest/Vitest/Testing Library]

### Key Design Principles
1. [Principle 1 - e.g., Single Responsibility]
2. [Principle 2 - e.g., Composability]
3. [Principle 3 - e.g., Accessibility First]

## Implementation Details

### Component Structure
```
ComponentName/
├── index.js          # Main component
├── styles.css        # Styles
├── utils.js          # Helper functions
└── tests/
    └── Component.test.js
```

### Core Implementation
```javascript
// Main Component Implementation
[50-100 lines of well-commented code]
```

### State Management
```javascript
// State logic (if applicable)
[State management code]
```

### Styling Approach
```css
/* Component styles */
[CSS/Tailwind classes]
```

## Api Interface

### Props/Inputs
| Prop | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| [prop1] | string | Yes | - | [description] |
| [prop2] | boolean | No | false | [description] |

### Events/Outputs
| Event | Payload | Description |
|-------|---------|-------------|
| [onEvent] | {data} | [when triggered] |

## Testing Strategy

### Unit Tests
```javascript
// Example test case
[Test example]
```

### Integration Tests
- User flow 1: [description]
- User flow 2: [description]

## Performance Considerations
- Bundle size: ~[X]kb
- Render time: <[X]ms
- Accessibility score: [X]/100

## Deployment & Integration

### Installation
```bash
# Installation steps
[Commands]
```

### Usage
```javascript
// Integration example
[Usage code]
```

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $spec
- **Type:** [Framework]
- **Complexity:** Standard

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** A→T→L→A→S

---

- **Challenge:** [Applied/Not applied]
- **Context:** [Brief context]

---

**Historical Context:**
- Similar components: [X]
- Pattern consistency maintained
```

---

## 5. 🏗️ Complex Spec Template

```markdown
# Complex System: [System Name]

## Executive Summary
[Comprehensive overview of the system being built]

## System Architecture

### High-Level Design
```mermaid
graph TD
    A[User Interface] --> B[State Management]
    B --> C[API Layer]
    C --> D[Data Processing]
    D --> E[External Services]
```

### Technology Stack
- **Frontend:** [Framework + version]
- **State:** [Redux/MobX/Zustand]
- **API:** [REST/GraphQL]
- **Build:** [Webpack/Vite/Rollup]
- **Testing:** [Complete testing stack]

## Detailed Specifications

### Module 1: [Module Name]

#### Purpose
[What this module does]

#### Implementation
```javascript
// Module implementation
[100-200 lines of code]
```

#### Interfaces
```typescript
// TypeScript interfaces
interface ModuleName {
  [properties]
}
```

### Module 2: [Module Name]

#### Purpose
[What this module does]

#### Implementation
```javascript
// Module implementation
[100-200 lines of code]
```

## State Management

### Store Structure
```javascript
// Store configuration
[Store setup code]
```

### Actions & Reducers
```javascript
// State management logic
[Actions and reducers]
```

## Api Integration

### Endpoints
| Method | Endpoint | Purpose | Request | Response |
|--------|----------|---------|---------|----------|
| GET | /api/items | List items | - | Item[] |
| POST | /api/items | Create item | Item | Item |

### Service Layer
```javascript
// API service implementation
[Service code]
```

## Error Handling

### Error Boundaries
```javascript
// Error boundary implementation
[Error handling code]
```

### Fallback Strategies
1. Network failures: [strategy]
2. Invalid data: [strategy]
3. Auth errors: [strategy]

## Testing Comprehensive

### Unit Test Coverage
- Target: >90%
- Critical paths: 100%

### E2E Test Scenarios
```javascript
// E2E test example
[E2E test code]
```

## Performance Optimization

### Code Splitting
```javascript
// Dynamic imports
[Code splitting example]
```

### Caching Strategy
- Browser cache: [strategy]
- API cache: [strategy]
- State persistence: [strategy]

## Security Considerations

### Input Validation
```javascript
// Validation logic
[Validation code]
```

### Xss Prevention
- Content Security Policy
- Input sanitization
- Output encoding

## Deployment Strategy

### Build Configuration
```javascript
// Build config
[Webpack/Vite config]
```

### Ci/Cd Pipeline
```yaml
# CI/CD configuration
[Pipeline config]
```

### Monitoring
- Error tracking: [Sentry/etc]
- Analytics: [GA/etc]
- Performance: [Web Vitals]

## Migration Plan

### Phase 1: Foundation
- Set up infrastructure
- Core modules implementation

### Phase 2: Features
- Complete feature set
- Integration testing

### Phase 3: Optimization
- Performance tuning
- Production readiness

---

**AI System:**

- **Framework:** ATLAS
- **Mode:** $spec
- **Type:** [Framework]
- **Complexity:** Complex

---

- **Thinking:** [X] rounds (user selected)
- **ATLAS:** Full ATLAS with iterations

---

- **Challenge:** [Phasing strategy applied]
- **Context:** [System context]

---

**Historical Context:**
- Architecture patterns from [X] projects
- Lessons learned applied
```

---

## 6. 💻 Code Examples By Type

### React Component (Minimal)
```javascript
// Minimal React Modal - 0 dependencies
const Modal = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={e => e.stopPropagation()}>
        <button onClick={onClose}>×</button>
        {children}
      </div>
    </div>
  );
};
```

### Vue Component (Minimal)
```vue
<!-- Minimal Vue Modal -->
<template>
  <div v-if="isOpen" class="modal-overlay" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <button @click="$emit('close')">×</button>
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
defineProps(['isOpen'])
defineEmits(['close'])
</script>
```

### Vanilla Js (Minimal)
```javascript
// Vanilla JS Modal - Zero dependencies
class Modal {
  constructor(selector) {
    this.element = document.querySelector(selector);
    this.overlay = this.element.querySelector('.overlay');
    this.bindEvents();
  }

  open() { this.element.style.display = 'block'; }
  close() { this.element.style.display = 'none'; }

  bindEvents() {
    this.overlay?.addEventListener('click', () => this.close());
  }
}
```

### Css/Tailwind Utility
```css
/* Utility-first modal styles */
.modal-overlay {
  @apply fixed inset-0 bg-black bg-opacity-50 z-50;
}

.modal-content {
  @apply absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2;
  @apply bg-white rounded-lg p-6 max-w-md w-full;
}
```

---

## 7. 🎨 Formatting Standards

### Code Style Guidelines
1. **Consistency:** Same style throughout
2. **Comments:** Explain why, not what
3. **Naming:** Descriptive and consistent
4. **Structure:** Logical grouping
5. **Length:** Prefer multiple small files

### Documentation Requirements
- **Purpose:** Clear explanation of why
- **Usage:** Complete examples
- **API:** Full interface documentation
- **Testing:** Test case descriptions
- **Performance:** Metrics and benchmarks

### Artifact Formatting
- Always use `text/markdown` type
- Include all code in markdown blocks
- Add language hints for syntax highlighting
- Keep line length under 100 characters
- Use consistent indentation (2 spaces)

---

## 8. 💬 Interactive Questions

### Initial Flow (With Waits)
```markdown
User: $spec modal component

System: Let's build your modal component! 🔧

**How many thinking rounds should I use? (6-10)**

Based on modal component, I recommend: 6 rounds
- Complexity: Low (standard UI pattern)
- Uncertainty: Low (well-defined)
- Stakes: Low (isolated component)

Your choice?

[WAIT FOR USER INPUT]

User: 6

System: Great! Let me challenge the approach:

For this modal, we could:
- **Option A:** Native <dialog> element (0 dependencies, 20 lines)
- **Option B:** React component (minimal, 30 lines)
- **Option C:** Full library (react-modal, complete features)

Which approach? (A/B/C)

[WAIT FOR USER RESPONSE]

User: B

System: Perfect! React minimal approach.

Quick questions:
1. Animation needed? (yes/no)
2. Backdrop click to close? (yes/no)
3. ESC key to close? (yes/no)

[WAIT FOR ANSWERS]

[THEN CREATE SPEC]
```

### Framework Detection
```python
def detect_framework(request):
    """Auto-detect framework from request"""
    frameworks = {
        'react': ['react', 'hook', 'jsx', 'component'],
        'vue': ['vue', 'composition', 'template'],
        'angular': ['angular', 'service', 'directive'],
        'vanilla': ['vanilla', 'pure', 'no framework', 'native']
    }

    request_lower = request.lower()
    for framework, keywords in frameworks.items():
        if any(k in request_lower for k in keywords):
            return framework

    return 'vanilla'  # Default to vanilla JS
```

### Challenge Patterns
```markdown
# Standard Challenges (6+ rounds)

"Could we use native browser APIs instead of a library?"
"Would CSS-only work for this interaction?"
"Can we achieve this with 50% less code?"
"Is there a simpler pattern that works?"
```

---

*All specs delivered as artifacts. Minimal implementation preferred. Always ask thinking rounds and wait. Challenge at 6+ rounds for simpler approaches. Include working code examples. Document with clear usage instructions.*
