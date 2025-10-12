# Animation Strategy & Standards

Defines our animation strategy across the project: CSS is the default for simple interactions; Motion.dev is the only JavaScript animation library we use for sequences that CSS cannot express ergonomically. This keeps payloads small, performance high, and behavior predictable.

.

## 1. 🧭 Decision Framework

### 1.1 Primary Order (Use in Sequence)

1. CSS transitions/keyframes — first choice for hover, focus, small reveals, and state changes
2. Motion.dev — used when we need programmatic control, in‑view triggers, or coordinated sequences

### 1.2 Quick Decision Tree

```
Need animation?
├─> Can CSS express it (transform/opacity/clip/mask)? -> Use CSS
└─> Requires sequencing/stagger/scroll/in‑view logic? -> Use Motion.dev
```

.

## 2. 🧰 CSS‑First Playbook

- Prefer transform and opacity over layout properties
  - translate/scale/rotate + opacity are GPU‑friendly and avoid layout thrash
- Keep durations short; ease on enter, linear on continuous motion
- Respect user settings
  - Use `@media (prefers-reduced-motion: reduce)` to shorten/disable where appropriate
- Co-locate CSS variables for timing/easing on the component root
- Dropdown/open‑close pattern (no layout jump):
  ```css
  .dropdown { overflow: hidden; height: 0; opacity: 0; transition: height .3s var(--ease-out), opacity .2s var(--ease-out); }
  .dropdown[open] { height: auto; opacity: 1; }
  /* JS measures natural height once and transitions height from 0px -> measured px, then sets height:auto at end */
  ```

.

## 3. ⚙️ Motion.dev Integration

### 3.1 How we load it

We load Motion.dev once, as an ES module, and expose it globally for components:

```html
<!-- src/1_html/global.html -->
<script type="module">
  const lib = await import('https://cdn.jsdelivr.net/npm/motion@12.15.0/+esm');
  window.Motion = lib; // { animate, inView, scroll, stagger, ... }
</script>
```

### 3.2 Defensive loading in components

```javascript
// Pattern used throughout the repo
(() => {
  function init() {
    const { animate, inView } = window.Motion || {};
    if (!animate || !inView) { setTimeout(init, 100); return; }
    // ...use animate/inView here
  }
  if (window.Webflow?.push) window.Webflow.push(init);
  else if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
```

### 433 Parameters we standardize

- From/to arrays for properties: `{ opacity: [0, 1], x: ['-7.5rem', '0rem'] }`
- Easing curves (keep consistent with Webflow):
  - `easeOut = [0.22, 1, 0.36, 1]`
  - `expoOut = [0.16, 1, 0.3, 1]`
- Clean up `will-change`/temporary styles on `onComplete`
- Use `inView()` for one‑time entrance per block

### 3.4 In‑repo examples (authoritative patterns)

- `/src/hero/hero_general.js` — inView‑based, multi‑phase sequence with easing maps; loader fadeout; will‑change cleanup
- `/src/hero/hero_blog_article.js` — content‑first then overlay; short durations and expoOut
- `/src/navigation/language_selector.js` — dropdown open/close measured height with animate()

.

## 4. 🚦 Performance & Accessibility

- Set initial states to prevent flicker before animating (opacity 0, transforms off‑screen)
- Minimize reflows; batch style writes and avoid toggling layout properties mid‑animation
- Remove `will-change` after transitions to avoid keeping layers promoted
- Respect `prefers-reduced-motion`; when reduced, skip sequences and set end states directly

.

## 5. 🧪 Testing & Debugging

1. Verify desktop/tablet/mobile timing; keep animations brief on mobile
2. Confirm no layout jumps (measure before animate; `height: auto` after)
3. Run with `prefers-reduced-motion: reduce` to ensure graceful behavior
4. Use DevTools Performance to look for long main‑thread tasks and forced reflows