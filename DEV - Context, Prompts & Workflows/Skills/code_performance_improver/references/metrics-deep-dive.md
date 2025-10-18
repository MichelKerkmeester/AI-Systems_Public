# Performance Metrics Deep Dive

Comprehensive guide to measuring, interpreting, and optimizing web performance metrics.

## Core Web Vitals

Google's Core Web Vitals are the essential metrics that measure real user experience.

### Largest Contentful Paint (LCP)

**What**: Time until largest visible content element renders

**Target**: <2.5s (good), 2.5-4s (needs improvement), >4s (poor)

**What Counts as LCP**:
- `<img>` elements
- `<image>` inside `<svg>`
- `<video>` poster images
- Background images loaded via `url()`
- Block-level elements containing text nodes

**What Doesn't Count**:
- Elements with `opacity: 0`
- Elements outside viewport
- Elements less than 3% of viewport
- Elements added via JavaScript after DOMContentLoaded + 2s

**Measurement**:

```javascript
// Performance Observer API
const lcp_observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const last_entry = entries[entries.length - 1];

  console.log('LCP:', last_entry.renderTime || last_entry.loadTime);
  console.log('Element:', last_entry.element);
  console.log('URL:', last_entry.url);
});

lcp_observer.observe({ type: 'largest-contentful-paint', buffered: true });

// web-vitals library
import { getLCP } from 'web-vitals';

getLCP(console.log);
// Output: { name: 'LCP', value: 2341.5, id: '...', ... }
```

**Common Issues & Fixes**:

| Issue | Symptom | Fix |
|-------|---------|-----|
| Slow server | TTFB >600ms | Optimize backend, use CDN |
| Render-blocking resources | LCP delayed by CSS/JS | Defer non-critical, inline critical |
| Large images | LCP >4s | Compress, use WebP, responsive images |
| Client-side rendering | LCP happens after JS | Use SSR or prerendering |

**Optimization Checklist**:
- [ ] Optimize server response time (TTFB <600ms)
- [ ] Eliminate render-blocking CSS/JS
- [ ] Compress and optimize LCP image
- [ ] Preload LCP resource (`<link rel="preload">`)
- [ ] Use CDN for faster delivery
- [ ] Enable text compression (gzip/brotli)
- [ ] Implement lazy loading for below-fold images
- [ ] Use adaptive serving based on connection speed

---

### First Contentful Paint (FCP)

**What**: Time until first text or image renders

**Target**: <1.8s (good), 1.8-3s (needs improvement), >3s (poor)

**What Counts as FCP**:
- Text with web fonts loaded
- `<img>` elements
- `<svg>` elements
- Non-white `<canvas>` elements
- Background images

**Measurement**:

```javascript
const fcp_observer = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  entries.forEach((entry) => {
    if (entry.name === 'first-contentful-paint') {
      console.log('FCP:', entry.startTime);
    }
  });
});

fcp_observer.observe({ type: 'paint', buffered: true });

// web-vitals library
import { getFCP } from 'web-vitals';
getFCP(console.log);
```

**Optimization Strategies**:

1. **Eliminate render-blocking resources**
```html
<!-- Defer non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">

<!-- Defer non-critical JavaScript -->
<script defer src="app.js"></script>
```

2. **Inline critical CSS**
```html
<style>
  /* Critical above-the-fold styles only */
  .header { ... }
  .hero { ... }
</style>
```

3. **Optimize font loading**
```css
@font-face {
  font-family: 'Custom';
  src: url('font.woff2') format('woff2');
  font-display: swap; /* Show fallback immediately */
}
```

---

### Cumulative Layout Shift (CLS)

**What**: Sum of all unexpected layout shifts during page lifetime

**Target**: <0.1 (good), 0.1-0.25 (needs improvement), >0.25 (poor)

**Calculation**:
```
CLS = Impact Fraction × Distance Fraction
```

- **Impact Fraction**: % of viewport affected by shift
- **Distance Fraction**: Distance elements moved / viewport height

**Measurement**:

```javascript
let cls_value = 0;

const cls_observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) {
      cls_value += entry.value;
      console.log('CLS:', cls_value);
      console.log('Shift:', entry.value, entry.sources);
    }
  }
});

cls_observer.observe({ type: 'layout-shift', buffered: true });

// web-vitals library
import { getCLS } from 'web-vitals';
getCLS(console.log);
```

**Common Causes & Fixes**:

| Cause | Fix |
|-------|-----|
| Images without dimensions | Add `width` and `height` attributes |
| Ads/embeds without space | Reserve space with `min-height` |
| Fonts causing FOIT/FOUT | Use `font-display: swap` |
| Dynamically injected content | Reserve space before injection |
| Web fonts loaded late | Preload fonts, use system font stack |

**Prevention**:

```html
<!-- Reserve space for images -->
<img src="hero.jpg" width="1200" height="600" alt="Hero">

<!-- Reserve space for ads -->
<div class="ad-container" style="min-height: 250px;">
  <!-- Ad loads here -->
</div>
```

```css
/* Aspect ratio box for dynamic content */
.video-container {
  aspect-ratio: 16 / 9;
  width: 100%;
}

/* Or traditional padding hack */
.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 */
  height: 0;
}
```

---

### First Input Delay (FID)

**What**: Time from user's first interaction to browser response

**Target**: <100ms (good), 100-300ms (needs improvement), >300ms (poor)

**Note**: Replaced by INP (Interaction to Next Paint) in March 2024

**Measurement**:

```javascript
const fid_observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    const fid = entry.processingStart - entry.startTime;
    console.log('FID:', fid);
    console.log('Event type:', entry.name);
  }
});

fid_observer.observe({ type: 'first-input', buffered: true });

// web-vitals library
import { getFID } from 'web-vitals';
getFID(console.log);
```

**Optimization Strategies**:

1. **Break up long tasks**
```javascript
// ❌ Long task blocks main thread
function process_data(data) {
  data.forEach(item => heavy_processing(item)); // Blocks for 500ms
}

// ✅ Break into chunks with yielding
async function process_data_chunked(data) {
  const chunk_size = 50;
  for (let i = 0; i < data.length; i += chunk_size) {
    const chunk = data.slice(i, i + chunk_size);
    chunk.forEach(item => heavy_processing(item));

    // Yield to browser
    await new Promise(resolve => setTimeout(resolve, 0));
  }
}
```

2. **Use Web Workers**
```javascript
const worker = new Worker('processor.js');
worker.postMessage(heavy_data);
worker.onmessage = (e) => {
  update_ui(e.data); // Main thread stays responsive
};
```

3. **Defer non-essential JavaScript**
```html
<script defer src="analytics.js"></script>
<script defer src="chat-widget.js"></script>
```

---

### Interaction to Next Paint (INP)

**What**: Measures ALL interactions (not just first), replacing FID

**Target**: <200ms (good), 200-500ms (needs improvement), >500ms (poor)

**Measurement**:

```javascript
const inp_observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    const inp = entry.processingStart - entry.startTime + entry.duration;
    console.log('Interaction latency:', inp);
    console.log('Target:', entry.target);
  }
});

inp_observer.observe({ type: 'event', buffered: true });

// web-vitals library
import { getINP } from 'web-vitals';
getINP(console.log);
```

**Optimization**: Same as FID, but affects all interactions

---

### Time to Interactive (TTI)

**What**: Time until page is fully interactive

**Target**: <3.8s (good), 3.8-7.3s (needs improvement), >7.3s (poor)

**Requirements for TTI**:
1. FCP has occurred
2. Most visible elements have event handlers attached
3. Page responds to user input within 50ms

**Measurement**:

```javascript
// Using Lighthouse
import lighthouse from 'lighthouse';

const result = await lighthouse(url);
const tti = result.lhr.audits['interactive'].numericValue;
console.log('TTI:', tti);
```

**Optimization**:
- Reduce JavaScript execution time
- Code split and lazy load
- Defer third-party scripts
- Use server-side rendering
- Optimize critical rendering path

---

### Total Blocking Time (TBT)

**What**: Sum of time main thread was blocked (>50ms tasks)

**Target**: <200ms (good), 200-600ms (needs improvement), >600ms (poor)

**Calculation**:
```
For each task > 50ms:
  Blocking time = task duration - 50ms
TBT = sum of all blocking times
```

**Measurement**:

```javascript
const long_tasks = new PerformanceObserver((list) => {
  let tbt = 0;
  for (const entry of list.getEntries()) {
    if (entry.duration > 50) {
      tbt += entry.duration - 50;
    }
  }
  console.log('TBT:', tbt);
});

long_tasks.observe({ type: 'longtask', buffered: true });
```

**Optimization**: Same as FID/INP - break up long tasks

---

## Performance API

### Navigation Timing

**What**: Detailed timing of page navigation and loading

**Measurement**:

```javascript
const nav_timing = performance.getEntriesByType('navigation')[0];

console.log('DNS lookup:', nav_timing.domainLookupEnd - nav_timing.domainLookupStart);
console.log('TCP connection:', nav_timing.connectEnd - nav_timing.connectStart);
console.log('Request time:', nav_timing.responseStart - nav_timing.requestStart);
console.log('Response time:', nav_timing.responseEnd - nav_timing.responseStart);
console.log('DOM processing:', nav_timing.domComplete - nav_timing.domLoading);
console.log('Load complete:', nav_timing.loadEventEnd - nav_timing.fetchStart);
```

**Key Metrics**:

```javascript
// Time to First Byte (TTFB)
const ttfb = nav_timing.responseStart - nav_timing.requestStart;

// DOM Content Loaded
const dcl = nav_timing.domContentLoadedEventEnd - nav_timing.fetchStart;

// Full page load
const load = nav_timing.loadEventEnd - nav_timing.fetchStart;
```

**Targets**:
- TTFB: <600ms
- DOM Content Loaded: <1.5s
- Load: <3s

---

### Resource Timing

**What**: Timing for individual resources (CSS, JS, images)

**Measurement**:

```javascript
const resources = performance.getEntriesByType('resource');

resources.forEach(resource => {
  console.log('Name:', resource.name);
  console.log('Type:', resource.initiatorType);
  console.log('Size:', resource.transferSize);
  console.log('Duration:', resource.duration);
  console.log('Cache:', resource.transferSize === 0 ? 'HIT' : 'MISS');
});

// Find slow resources
const slow_resources = resources
  .filter(r => r.duration > 1000)
  .sort((a, b) => b.duration - a.duration);

console.table(slow_resources);
```

**Analysis**:

```javascript
// Group by type
const by_type = resources.reduce((acc, r) => {
  const type = r.initiatorType;
  if (!acc[type]) acc[type] = [];
  acc[type].push(r);
  return acc;
}, {});

// Calculate stats per type
Object.entries(by_type).forEach(([type, items]) => {
  const total_size = items.reduce((sum, r) => sum + r.transferSize, 0);
  const total_time = items.reduce((sum, r) => sum + r.duration, 0);

  console.log(`${type}:`, {
    count: items.length,
    size: `${(total_size / 1024).toFixed(2)} KB`,
    time: `${total_time.toFixed(2)} ms`
  });
});
```

---

### User Timing API

**What**: Custom performance marks and measures

**Usage**:

```javascript
// Mark points in time
performance.mark('script-start');

// ... code execution ...

performance.mark('script-end');

// Measure between marks
performance.measure('script-execution', 'script-start', 'script-end');

// Get measurement
const measure = performance.getEntriesByName('script-execution')[0];
console.log('Duration:', measure.duration);

// Clear marks/measures
performance.clearMarks();
performance.clearMeasures();
```

**Real-world Example**:

```javascript
// Measure component render time
performance.mark('render-start');
render_component();
performance.mark('render-end');
performance.measure('component-render', 'render-start', 'render-end');

// Measure API call time
performance.mark('api-start');
const data = await fetch('/api/data').then(r => r.json());
performance.mark('api-end');
performance.measure('api-call', 'api-start', 'api-end');

// Report all custom measurements
const measures = performance.getEntriesByType('measure');
console.table(measures);
```

---

## Real User Monitoring (RUM)

### Collecting Metrics

**Implementation**:

```javascript
// Collect all Core Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

function send_to_analytics({ name, value, id }) {
  const body = JSON.stringify({ name, value, id });

  // Use sendBeacon for reliability
  navigator.sendBeacon('/analytics', body);
}

getCLS(send_to_analytics);
getFID(send_to_analytics);
getFCP(send_to_analytics);
getLCP(send_to_analytics);
getTTFB(send_to_analytics);

// Include context
function send_with_context(metric) {
  const data = {
    ...metric,
    url: window.location.href,
    user_agent: navigator.userAgent,
    connection: navigator.connection?.effectiveType,
    device_memory: navigator.deviceMemory
  };

  navigator.sendBeacon('/analytics', JSON.stringify(data));
}
```

### Analyzing RUM Data

**Percentile Analysis**:

```javascript
// Don't use averages - use percentiles!
function calculate_percentile(values, percentile) {
  const sorted = values.slice().sort((a, b) => a - b);
  const index = Math.ceil((percentile / 100) * sorted.length) - 1;
  return sorted[index];
}

const lcp_values = [1200, 1400, 1600, 2100, 2300, 2800, 3100, 5200];

console.log('P50 (median):', calculate_percentile(lcp_values, 50)); // 2200
console.log('P75:', calculate_percentile(lcp_values, 75)); // 2950
console.log('P95:', calculate_percentile(lcp_values, 95)); // 5200
```

**Why Percentiles Matter**:
- Average: 2475ms (misleading - doesn't show distribution)
- P50: 2200ms (typical user)
- P75: 2950ms (75% of users faster than this)
- P95: 5200ms (worst-case for most users)

Google recommends optimizing for **P75** (75th percentile).

---

## Custom Metrics

### Long Task Detection

```javascript
// Monitor tasks >50ms
const long_task_observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.warn('Long task detected:', {
      duration: entry.duration,
      start: entry.startTime,
      attribution: entry.attribution
    });

    // Send to analytics
    if (entry.duration > 100) {
      send_alert('Long task', entry);
    }
  }
});

long_task_observer.observe({ type: 'longtask', buffered: true });
```

### Memory Usage

```javascript
// Check memory usage (Chrome only)
if (performance.memory) {
  setInterval(() => {
    const used = performance.memory.usedJSHeapSize;
    const total = performance.memory.totalJSHeapSize;
    const limit = performance.memory.jsHeapSizeLimit;

    console.log('Memory:', {
      used: `${(used / 1024 / 1024).toFixed(2)} MB`,
      total: `${(total / 1024 / 1024).toFixed(2)} MB`,
      limit: `${(limit / 1024 / 1024).toFixed(2)} MB`,
      percentage: `${((used / limit) * 100).toFixed(1)}%`
    });

    // Alert if memory usage >80%
    if (used / limit > 0.8) {
      console.warn('High memory usage!');
    }
  }, 5000);
}
```

### FPS Monitoring

```javascript
// Monitor frame rate
let last_frame_time = performance.now();
let fps_values = [];

function measure_fps() {
  requestAnimationFrame(() => {
    const now = performance.now();
    const fps = 1000 / (now - last_frame_time);
    fps_values.push(fps);

    // Keep last 60 samples (1 second at 60fps)
    if (fps_values.length > 60) fps_values.shift();

    const avg_fps = fps_values.reduce((a, b) => a + b) / fps_values.length;

    // Alert if FPS drops below 30
    if (avg_fps < 30) {
      console.warn('Low FPS:', avg_fps.toFixed(1));
    }

    last_frame_time = now;
    measure_fps();
  });
}

measure_fps();
```

---

## Interpretation Guide

### Performance Budget

Set budgets for each metric:

```javascript
const BUDGET = {
  LCP: 2500,
  FID: 100,
  CLS: 0.1,
  FCP: 1800,
  TTI: 3800,
  TBT: 200
};

function check_budget(metrics) {
  const violations = [];

  Object.entries(metrics).forEach(([name, value]) => {
    if (value > BUDGET[name]) {
      violations.push({
        metric: name,
        value,
        budget: BUDGET[name],
        over_by: value - BUDGET[name]
      });
    }
  });

  if (violations.length > 0) {
    console.error('Budget violations:', violations);
  }

  return violations.length === 0;
}
```

### Scoring

**Lighthouse Performance Score** (weighted):
- FCP: 10%
- SI (Speed Index): 10%
- LCP: 25%
- TTI: 10%
- TBT: 30%
- CLS: 15%

**Passing Criteria**:
- 90-100: Good (green)
- 50-89: Needs improvement (orange)
- 0-49: Poor (red)

---

## Quick Reference

| Metric | Good | Needs Improvement | Poor | Weight |
|--------|------|-------------------|------|--------|
| LCP | <2.5s | 2.5-4s | >4s | 25% |
| FID | <100ms | 100-300ms | >300ms | - |
| INP | <200ms | 200-500ms | >500ms | Replacing FID |
| CLS | <0.1 | 0.1-0.25 | >0.25 | 15% |
| FCP | <1.8s | 1.8-3s | >3s | 10% |
| TTI | <3.8s | 3.8-7.3s | >7.3s | 10% |
| TBT | <200ms | 200-600ms | >600ms | 30% |
| TTFB | <600ms | 600-1s | >1s | - |

## Monitoring Checklist

- [ ] Set up Core Web Vitals tracking (getCLS, getFID/getINP, getLCP, getFCP)
- [ ] Implement Real User Monitoring (RUM)
- [ ] Track P75 (75th percentile), not averages
- [ ] Set performance budgets
- [ ] Monitor long tasks (>50ms)
- [ ] Track memory usage
- [ ] Monitor FPS for animations
- [ ] Set up alerts for budget violations
- [ ] Create performance dashboard
- [ ] Review metrics weekly
