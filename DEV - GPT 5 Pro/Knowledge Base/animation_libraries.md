# Animation Libraries - Decision Framework

Consistent animations keep UltraThink interactions smooth. This guide explains the library hierarchy, when to reach for each tool, and how to migrate legacy Miyagi logic without sacrificing performance.

.

## 1. 🎯 Objective

Define a repeatable animation decision process: prefer Webflow Interactions, default to Motion.dev for lightweight custom work, and reserve GSAP only for complex cases. The hierarchy safeguards bundle size, performance, and maintainability.

**Category**: library_constraint  
**Tags**: animation, motion_dev, gsap, webflow  
**Priority**: high

.

## 2. 🧭 Priority Framework

### 2.1 Primary Order (Use in Sequence)

1. **Webflow Interactions** - Always the first choice.
2. **Motion.dev** - Default when native Webflow cannot handle the behavior.
3. **GSAP** - Only when requirements exceed the first two options.

### 2.2 Quick Decision Tree

```
Need Animation?
├─> Can Webflow handle it? -> Use Webflow
├─> Simple animation? -> Use Motion.dev
└─> Complex (3D/morphing)? -> Use GSAP
```

.

## 3. 🛠️ Library Playbooks

### 3.1 Webflow Interactions
- **Use For**: Scroll effects, hover transitions, page-load reveals, lightweight parallax.
- **Init Pattern**:
  ```javascript
  window.Webflow.push(function() {
    Webflow.require('ix2').init();
  });
  ```

### 3.2 Motion.dev
- **Use For**: Element fades, staggers, spring physics, simple timelines.
- **Init Pattern**:
  ```javascript
  import { animate, stagger } from 'motion';

  animate('.card', {
    opacity: [0, 1],
    y: [20, 0]
  }, {
    duration: 0.5,
    delay: stagger(0.1)
  });
  ```

### 3.3 GSAP (Escalation Path)
- **Use For**: 3D transforms, SVG morphing, precision timelines, performance-critical choreographies.
- **Init Pattern**:
  ```javascript
  gsap.timeline()
    .to('.element', { rotation: 360, duration: 1 })
    .to('.element', { scale: 1.5 }, '-=0.5');
  ```

.

## 4. ⚙️ Integration Pattern

Apply the universal animation controller to detect the right library at runtime.

```javascript
// ───────────────────────────────────────────────────────────────
// ANIMATION CONTROLLER (UNIVERSAL INIT)
// ───────────────────────────────────────────────────────────────
(() => {
  function init_animations() {
    const animation_controller = {
      setup_animations() {
        if (this.has_webflow_interaction()) return;
        if (this.is_simple_animation()) {
          this.use_motion_dev();
          return;
        }
        if (this.requires_complex()) {
          this.use_gsap();
        }
      },
      has_webflow_interaction() {
        return document.querySelector('[data-w-id]') !== null;
      },
      is_simple_animation() {
        return true;
      },
      requires_complex() {
        return false;
      },
      use_motion_dev() {
        // Motion.dev implementation
      },
      use_gsap() {
        // GSAP implementation
      }
    };

    animation_controller.setup_animations();
  }

  if (window.Webflow && window.Webflow.push) {
    window.Webflow.push(init_animations);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init_animations);
  } else {
    init_animations();
  }
})();
```

.

## 5. 🚀 Migration: Miyagi -> Motion.dev

### 5.1 Why Move
- Miyagi is deprecated and unsupported.
- Motion.dev ships smaller bundles with better performance.
- Provides modern patterns and TypeScript support.

### 5.2 Conversion Steps

1. **Initialization**
   ```javascript
   // OLD
   window.Miyagi.ready(() => {
     init_component();
   });

   // NEW
   const { animate } = window.Motion || {};
   if (!animate) {
     setTimeout(init_component, 100);
     return;
   }
   ```
2. **Animation Calls**
   ```javascript
   // OLD
   Miyagi.animate(element, { opacity: 1 }, 500);

   // NEW
   animate(element, { opacity: 1 }, { duration: 0.5 });
   ```
3. **Easing**
   ```javascript
   // OLD
   { easing: 'ease-out' }

   // NEW
   { easing: [0.165, 0.84, 0.44, 1] }
   ```
4. **Event Hooks**
   ```javascript
   // OLD
   Miyagi.on('scroll', handle_scroll);

   // NEW
   const { scroll } = window.Motion;
   scroll(handle_scroll);
   ```

.

## 6. 📐 Common Patterns & Testing

### 6.1 Snippets
- **Dropdown Animation**
  ```javascript
  animate(dropdown, {
    height: is_open ? `${natural_height}px` : '0px',
    opacity: is_open ? 1 : 0
  }, {
    duration: 0.3,
    easing: [0.165, 0.84, 0.44, 1]
  });
  ```
- **Hamburger Icon Transition**
  ```javascript
  animate(bar_top, {
    rotate: '45deg',
    y: '8px'
  }, {
    duration: 0.4,
    easing: [0.5, 0.5, 0, 1]
  });
  ```

### 6.2 Test Checklist
1. Trigger all animations to confirm they fire.
2. Validate timing/easing on desktop and mobile.
3. Monitor console for regression warnings (missing Motion.dev, lingering Miyagi).
4. Measure jank using DevTools Performance tab when adopting GSAP.

.

## 7. 📊 Performance Notes

| Library | Approx Bundle Cost | Notes |
|---------|--------------------|-------|
| Webflow Interactions | Built-in | No additional payload |
| Motion.dev | ~15 KB | Default for custom sequences |
| GSAP | 60 KB+ | Only when justified by complexity |

Choose the lightest tool that achieves the desired effect.