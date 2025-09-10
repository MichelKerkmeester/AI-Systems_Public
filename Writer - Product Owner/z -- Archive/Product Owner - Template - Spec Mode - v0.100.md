# Product Owner - Spec Mode Template

## 📋 Table of Contents

1. [🔧 SPEC MODE OVERVIEW](#-spec-mode-overview)
2. [🎨 COMPONENT TYPES](#-component-types)
3. [⚛️ REACT COMPONENT TEMPLATE](#️-react-component-template)
4. [🎯 VANILLA JS TEMPLATE](#-vanilla-js-template)
5. [🖼️ CSS/STYLING TEMPLATE](#️-cssstyling-template)
6. [🔌 API INTEGRATION TEMPLATE](#-api-integration-template)
7. [📱 RESPONSIVE DESIGN TEMPLATE](#-responsive-design-template)
8. [⚡ PERFORMANCE OPTIMIZATION TEMPLATE](#-performance-optimization-template)
9. [🎯 SPEC FORMATTING RULES](#-spec-formatting-rules)
10. [💬 INTERACTIVE QUESTIONS](#-interactive-questions)
11. [📦 PLATFORM INTEGRATION](#-platform-integration)

---

## 🔧 SPEC MODE OVERVIEW

### Command: `$spec`

- **Purpose:** Create frontend implementation specs with code
- **Output:** Always as artifact
- **Thinking Rounds:** 1-5 (typically 2-3)
- **Challenge Activation:** 3+ rounds
- **Focus:** HOW to implement (not WHAT or WHY)
- **Typical Length:** 50-300 lines of code with documentation

---

## 🎨 COMPONENT TYPES

### Quick Reference

| Type | Framework | Use Case | Complexity |
|------|-----------|----------|------------|
| UI Component | React/Vue | Interactive elements | Low-Medium |
| Form | Any | Data input/validation | Medium |
| Modal/Dialog | Any | Overlays, popups | Low |
| Data Display | Any | Tables, lists, cards | Medium |
| Navigation | Any | Menus, breadcrumbs | Low-Medium |
| Layout | CSS/Framework | Page structure | Low |
| Animation | CSS/JS | Transitions, effects | Medium-High |
| Integration | Any | API connections | High |

---

## 🎨 CSS LAYOUT FIX TEMPLATE

```markdown
# ⌘ CSS Layout Issue Fix

## Problem
[Description of the layout issue]

## Solution
\`\`\`css
/* Fix for [specific issue] */
.container {
  /* Reset problematic styles */
  position: relative;
  overflow: hidden;
  
  /* Apply fix */
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

/* Handle edge cases */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
    align-items: stretch;
  }
}

/* Fallback for older browsers */
@supports not (gap: 1rem) {
  .container > * + * {
    margin-left: 1rem;
  }
}
\`\`\`

## Why This Works
- [Explanation of the fix]
- [Browser compatibility notes]
- [Performance impact if any]

## Testing
- Chrome/Edge ✓
- Firefox ✓
- Safari ✓
- Mobile ✓
```

---

## 🔧 TYPESCRIPT WEB COMPONENT TEMPLATE

```markdown
# ⌘ TypeScript Web Component Implementation

## Component
\`\`\`typescript
// [ComponentName].ts
export class [ComponentName] {
  private element: HTMLElement;
  private config: ComponentConfig;
  private isActive = false;

  constructor(selector: string, options: Partial<ComponentConfig> = {}) {
    const el = document.querySelector(selector);
    if (!el) throw new Error(\`Element \${selector} not found\`);
    
    this.element = el as HTMLElement;
    this.config = { ...this.defaultConfig, ...options };
    this.init();
  }

  private defaultConfig: ComponentConfig = {
    animationDuration: 300,
    autoStart: false,
    onComplete: () => {}
  };

  private init(): void {
    this.attachListeners();
    if (this.config.autoStart) {
      this.activate();
    }
  }

  private attachListeners(): void {
    this.element.addEventListener('click', this.handleClick);
    
    // Cleanup on element removal
    const observer = new MutationObserver(() => {
      if (!document.contains(this.element)) {
        this.destroy();
      }
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  private handleClick = (e: Event): void => {
    e.preventDefault();
    this.toggle();
  };

  public toggle(): void {
    this.isActive ? this.deactivate() : this.activate();
  }

  public activate(): void {
    this.isActive = true;
    this.element.classList.add('active');
    this.element.setAttribute('aria-expanded', 'true');
    
    setTimeout(() => {
      this.config.onComplete?.();
    }, this.config.animationDuration);
  }

  public deactivate(): void {
    this.isActive = false;
    this.element.classList.remove('active');
    this.element.setAttribute('aria-expanded', 'false');
  }

  public destroy(): void {
    this.element.removeEventListener('click', this.handleClick);
    this.element.classList.remove('active');
  }
}

// Types
interface ComponentConfig {
  animationDuration: number;
  autoStart: boolean;
  onComplete?: () => void;
}

// Usage
const instance = new [ComponentName]('#target', {
  animationDuration: 500,
  onComplete: () => console.log('Animation complete')
});
\`\`\`

## Error Handling
\`\`\`typescript
try {
  const component = new [ComponentName]('#element');
} catch (error) {
  console.error('Component initialization failed:', error);
  // Fallback behavior
}
\`\`\`
```

---

## 🎯 VANILLA JS TEMPLATE

```markdown
# ⌘ [Feature Name] Vanilla JS Implementation

## Overview
[Description of functionality]

**Type:** [Component/Module/Utility]  
**Browser Support:** Modern browsers (ES6+)  
**Dependencies:** None  
**Size:** ~[X]KB minified

---

## ◇ Implementation

### Module Structure
\`\`\`javascript
// IIFE Pattern for encapsulation
const [ModuleName] = (function() {
  'use strict';
  
  // Private variables
  const config = {
    animationDuration: 300,
    defaultClass: 'module-name',
    // ... other config
  };
  
  // Private methods
  function privateMethod(param) {
    // Internal logic
    return processedValue;
  }
  
  // Constructor/Factory
  function Module(element, options = {}) {
    // Merge options
    this.settings = Object.assign({}, config, options);
    this.element = element;
    this.init();
  }
  
  // Public methods
  Module.prototype = {
    init() {
      this.bindEvents();
      this.render();
    },
    
    bindEvents() {
      this.element.addEventListener('click', this.handleClick.bind(this));
    },
    
    handleClick(event) {
      event.preventDefault();
      // Handle interaction
    },
    
    render() {
      // DOM manipulation
      this.element.innerHTML = this.template();
    },
    
    template() {
      return \`
        <div class="\${this.settings.defaultClass}">
          <!-- HTML structure -->
        </div>
      \`;
    },
    
    destroy() {
      // Cleanup
      this.element.removeEventListener('click', this.handleClick);
    }
  };
  
  // Public API
  return Module;
})();

// Usage
const instance = new [ModuleName](document.getElementById('target'), {
  animationDuration: 500
});
\`\`\`

### CSS (if needed)
\`\`\`css
.module-name {
  /* Styles */
}
\`\`\`

---

## ◇ Alternative: ES6 Class

\`\`\`javascript
class [ModuleName] {
  constructor(element, options = {}) {
    this.element = element;
    this.options = { ...this.defaults, ...options };
    this.init();
  }
  
  defaults = {
    // Default configuration
  }
  
  init() {
    // Initialization
  }
  
  // Methods...
}

export default [ModuleName];
\`\`\`

---

## ✦ Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

**Polyfills needed:** None for modern browsers
\`\`\`

---

## 🖼️ CSS/STYLING TEMPLATE

```markdown
# ⌘ [Component/Page] Styling Spec

## Overview
[Visual design implementation details]

**Approach:** [CSS/SCSS/CSS-in-JS/Tailwind]  
**Design System:** [If applicable]  
**Responsive:** Yes  
**Browser Support:** Modern + IE11 (if needed)

---

## ◇ Design Tokens

### Colors
\`\`\`css
:root {
  /* Primary palette */
  --color-primary: #007bff;
  --color-primary-dark: #0056b3;
  --color-primary-light: #e7f3ff;
  
  /* Neutral palette */
  --color-text: #212529;
  --color-text-muted: #6c757d;
  --color-bg: #ffffff;
  --color-border: #dee2e6;
  
  /* Semantic colors */
  --color-success: #28a745;
  --color-warning: #ffc107;
  --color-error: #dc3545;
}
\`\`\`

### Typography
\`\`\`css
:root {
  /* Font families */
  --font-primary: -apple-system, system-ui, sans-serif;
  --font-mono: 'Monaco', 'Courier New', monospace;
  
  /* Font sizes */
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px */
  --text-lg: 1.25rem;   /* 20px */
  --text-xl: 1.5rem;    /* 24px */
  --text-2xl: 2rem;     /* 32px */
  
  /* Line heights */
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  --leading-loose: 1.75;
}
\`\`\`

### Spacing
\`\`\`css
:root {
  /* Spacing scale */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-12: 3rem;    /* 48px */
  --space-16: 4rem;    /* 64px */
}
\`\`\`

---

## ◇ Component Styles

### Base Structure
\`\`\`css
.component {
  /* Layout */
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  
  /* Spacing */
  padding: var(--space-4);
  margin: 0;
  
  /* Visual */
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 0.25rem;
  
  /* Typography */
  font-family: var(--font-primary);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text);
}

/* Element styles */
.component__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--color-border);
}

.component__body {
  flex: 1;
  min-height: 0; /* Enable scrolling */
}

.component__footer {
  padding-top: var(--space-3);
  border-top: 1px solid var(--color-border);
}
\`\`\`

### States
\`\`\`css
/* Hover */
.component:hover {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Active */
.component:active {
  transform: translateY(1px);
}

/* Focus */
.component:focus-within {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Disabled */
.component--disabled {
  opacity: 0.6;
  cursor: not-allowed;
  pointer-events: none;
}

/* Loading */
.component--loading {
  position: relative;
  overflow: hidden;
}

.component--loading::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.3),
    transparent
  );
  animation: shimmer 2s infinite;
}

@keyframes shimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}
\`\`\`

---

## ◇ Responsive Design

### Breakpoints
\`\`\`css
/* Mobile First Approach */
.component {
  /* Base mobile styles */
  padding: var(--space-2);
}

/* Tablet */
@media (min-width: 768px) {
  .component {
    padding: var(--space-4);
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .component {
    padding: var(--space-6);
  }
}

/* Large Desktop */
@media (min-width: 1440px) {
  .component {
    max-width: 1200px;
    margin: 0 auto;
  }
}
\`\`\`

---

## ✦ Utility Classes

\`\`\`css
/* Display */
.hidden { display: none; }
.block { display: block; }
.flex { display: flex; }
.grid { display: grid; }

/* Spacing */
.mt-0 { margin-top: 0; }
.mt-1 { margin-top: var(--space-1); }
.mt-2 { margin-top: var(--space-2); }
/* ... etc */

/* Text */
.text-center { text-align: center; }
.font-bold { font-weight: 700; }
.truncate { 
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
\`\`\`
\`\`\`

---

## 🔌 API INTEGRATION TEMPLATE

```markdown
# ⌘ [API/Service] Integration Spec

## Overview
[Description of API integration purpose]

**API Endpoint:** \`https://api.example.com/v1\`  
**Authentication:** [Type - Bearer/API Key/OAuth]  
**Rate Limit:** [Requests per minute]  
**Error Handling:** Exponential backoff with retry

---

## ◇ Service Implementation

### API Service Class
\`\`\`javascript
class [ServiceName]API {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseURL = 'https://api.example.com/v1';
    this.headers = {
      'Content-Type': 'application/json',
      'Authorization': \`Bearer \${apiKey}\`
    };
  }
  
  // Generic request method
  async request(endpoint, options = {}) {
    const url = \`\${this.baseURL}\${endpoint}\`;
    
    try {
      const response = await fetch(url, {
        ...options,
        headers: {
          ...this.headers,
          ...options.headers
        }
      });
      
      if (!response.ok) {
        throw new Error(\`HTTP \${response.status}: \${response.statusText}\`);
      }
      
      return await response.json();
    } catch (error) {
      this.handleError(error);
    }
  }
  
  // GET request
  async get(endpoint, params = {}) {
    const queryString = new URLSearchParams(params).toString();
    const url = queryString ? \`\${endpoint}?\${queryString}\` : endpoint;
    
    return this.request(url, { method: 'GET' });
  }
  
  // POST request
  async post(endpoint, data) {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }
  
  // Error handling
  handleError(error) {
    console.error('[API Error]:', error);
    
    if (error.status === 429) {
      // Rate limited - implement retry
      return this.retryWithBackoff();
    }
    
    throw error;
  }
  
  // Retry logic
  async retryWithBackoff(retries = 3, delay = 1000) {
    // Implementation
  }
}
\`\`\`

### Usage in Component
\`\`\`javascript
// Initialize
const api = new [ServiceName]API(process.env.API_KEY);

// React Hook Example
function use[ServiceName]() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const fetchData = async (params) => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await api.get('/endpoint', params);
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  return { data, loading, error, fetchData };
}
\`\`\`

---

## ✦ Error States

### Error Response Format
\`\`\`javascript
{
  error: {
    code: 'ERROR_CODE',
    message: 'Human readable message',
    details: {}
  }
}
\`\`\`

### Error Handling UI
\`\`\`jsx
{error && (
  <div className="error-message">
    <p>{error.message}</p>
    <button onClick={retry}>Try Again</button>
  </div>
)}
\`\`\`
\`\`\`

---

## 📱 RESPONSIVE DESIGN TEMPLATE

```markdown
# ⌘ Responsive [Component/Layout] Spec

## Overview
[Description of responsive behavior]

**Breakpoints:** Mobile (< 768px) | Tablet (768-1024px) | Desktop (> 1024px)  
**Approach:** Mobile-first  
**Grid System:** CSS Grid / Flexbox  
**Testing:** Chrome DevTools + Real devices

---

## ◇ Layout Structure

### Mobile Layout (< 768px)
\`\`\`css
.container {
  display: flex;
  flex-direction: column;
  padding: 1rem;
  gap: 1rem;
}

.sidebar { order: 2; }
.main { order: 1; }
.aside { order: 3; }
\`\`\`

### Tablet Layout (768-1024px)
\`\`\`css
@media (min-width: 768px) {
  .container {
    display: grid;
    grid-template-columns: 200px 1fr;
    padding: 1.5rem;
    gap: 1.5rem;
  }
  
  .sidebar { order: initial; }
  .main { order: initial; }
  .aside { grid-column: 1 / -1; }
}
\`\`\`

### Desktop Layout (> 1024px)
\`\`\`css
@media (min-width: 1024px) {
  .container {
    grid-template-columns: 250px 1fr 300px;
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem;
    gap: 2rem;
  }
  
  .aside { grid-column: auto; }
}
\`\`\`

---

## ◇ Component Adaptations

### Navigation
\`\`\`css
/* Mobile: Hamburger menu */
.nav-mobile {
  display: block;
}

.nav-desktop {
  display: none;
}

/* Desktop: Horizontal nav */
@media (min-width: 768px) {
  .nav-mobile { display: none; }
  .nav-desktop { display: flex; }
}
\`\`\`

### Typography Scaling
\`\`\`css
h1 {
  font-size: clamp(1.5rem, 4vw, 3rem);
  line-height: 1.2;
}

p {
  font-size: clamp(0.875rem, 2vw, 1rem);
  line-height: 1.6;
}
\`\`\`

### Images
\`\`\`css
img {
  max-width: 100%;
  height: auto;
  object-fit: cover;
}

/* Art direction with picture element */
<picture>
  <source media="(min-width: 1024px)" srcset="large.jpg">
  <source media="(min-width: 768px)" srcset="medium.jpg">
  <img src="small.jpg" alt="Description">
</picture>
\`\`\`

---

## ✦ Performance Considerations

- Lazy load images below the fold
- Use srcset for responsive images
- Minimize CSS for critical rendering path
- Consider container queries for component-based responsiveness
\`\`\`



---

## 🎯 SPEC FORMATTING RULES

### Essential Standards

- ✅ **Implementation Focus:** HOW, not WHAT or WHY
- ✅ **Working Code:** All code should be functional
- ✅ **Modern Patterns:** Use current best practices
- ✅ **Error Handling:** Include try/catch and edge cases
- ✅ **Performance:** Consider optimization from start
- ✅ **Accessibility:** ARIA labels, keyboard navigation
- ✅ **Testing:** Include test approach or examples

### Code Standards

| Element | Standard | Example |
|---------|----------|---------|
| Naming | camelCase/PascalCase | `userName`, `UserComponent` |
| Comments | Explain why, not what | `// Prevent race condition` |
| Functions | Single responsibility | One function, one task |
| Files | <300 lines | Split if larger |
| Dependencies | Minimize | Prefer native over library |

### Documentation Requirements

- Component purpose and usage
- Props/parameters with types
- Return values
- Side effects
- Error states
- Examples

---

## 💬 Interactive Questions

Questions to ask during spec creation.

**Reference:** Full interactive flows → `Product Owner - Interactive Mode.md`

```markdown
1. "What framework/library? [React/Vue/Vanilla/Other]"
2. "Component type? [UI/Form/Data/Integration]"
3. "Need responsive design? [Yes/No]"
4. [If yes] "Target devices? [Mobile/Tablet/Desktop/All]"
5. "Browser support needed? [Modern only/IE11+]"
6. "Existing design system? [Yes/No/Custom]"
```

---

## 📦 Platform Integration

After spec creation, offer platform options.

**Reference:** Full integration details → `Product Owner - Platform Integration.md`

```markdown
📦 **Add to your workspace?**

1. **ClickUp** - As technical documentation
2. **Skip** - Keep as artifact only

Which option? (1 or 2)
```

**Pattern Tracking:** Specs often kept as artifacts for direct implementation (60% skip rate).

---

*Implementation-focused specs with working code. All outputs as artifacts. Challenge over-engineering.*