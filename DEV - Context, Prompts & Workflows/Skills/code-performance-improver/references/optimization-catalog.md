# Performance Optimization Catalog

Comprehensive catalog of 60+ performance optimization techniques with implementation examples and impact estimates.

## Code Optimizations

### 1. Lazy Loading

**What**: Load resources only when needed, not on initial page load

**When to Use**:
- Images below the fold
- Components not visible on initial render
- Heavy libraries used in specific scenarios
- Routes not accessed immediately

**Implementation**:

```javascript
// Lazy load images
const lazy_images = document.querySelectorAll('img[data-src]');
const image_observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
      image_observer.unobserve(img);
    }
  });
});

lazy_images.forEach(img => image_observer.observe(img));

// Lazy load JavaScript modules
async function load_chart_library() {
  const { default: Chart } = await import('./chart.js');
  return new Chart();
}

// Lazy load routes (React example)
const Dashboard = React.lazy(() => import('./Dashboard'));
```

**Impact**: Reduces initial bundle size by 20-40%, improves LCP by 30-50%

---

### 2. Code Splitting

**What**: Split JavaScript bundle into smaller chunks loaded on-demand

**When to Use**:
- Large single-page applications
- Multiple routes or features
- Vendor libraries (React, Lodash, etc.)
- Features used by subset of users

**Implementation**:

```javascript
// Webpack configuration
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10
        },
        common: {
          minChunks: 2,
          priority: 5,
          reuseExistingChunk: true
        }
      }
    }
  }
};

// Dynamic imports
button.addEventListener('click', async () => {
  const module = await import('./heavy-feature.js');
  module.initialize();
});

// Route-based splitting (React Router)
const routes = [
  { path: '/', component: React.lazy(() => import('./Home')) },
  { path: '/dashboard', component: React.lazy(() => import('./Dashboard')) }
];
```

**Impact**: Reduces initial bundle by 40-60%, improves TTI by 1-2s

---

### 3. Tree Shaking

**What**: Remove unused code from final bundle

**When to Use**:
- Using large libraries (Lodash, Moment.js)
- Importing only specific functions
- ES6 modules (required for tree shaking)

**Implementation**:

```javascript
// ❌ BAD - Imports entire library
import _ from 'lodash';
const result = _.debounce(fn, 300);

// ✅ GOOD - Imports only what's needed
import debounce from 'lodash/debounce';
const result = debounce(fn, 300);

// Package.json configuration
{
  "sideEffects": false  // Enables aggressive tree shaking
}

// Webpack configuration
module.exports = {
  mode: 'production',  // Enables tree shaking
  optimization: {
    usedExports: true,
    minimize: true
  }
};
```

**Impact**: Reduces bundle size by 10-30%, depending on library usage

---

### 4. Debouncing & Throttling

**What**: Limit execution frequency of expensive operations

**When to Use**:
- Search input handlers
- Scroll event listeners
- Window resize handlers
- Autocomplete suggestions

**Implementation**:

```javascript
// Debounce - Execute after quiet period
function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

// Throttle - Execute at most once per period
function throttle(func, limit) {
  let in_throttle;
  return function(...args) {
    if (!in_throttle) {
      func.apply(this, args);
      in_throttle = true;
      setTimeout(() => in_throttle = false, limit);
    }
  };
}

// Usage
const search_input = document.querySelector('#search');
const debounced_search = debounce(perform_search, 300);
search_input.addEventListener('input', debounced_search);

const throttled_scroll = throttle(handle_scroll, 100);
window.addEventListener('scroll', throttled_scroll);
```

**Impact**: Reduces JavaScript execution by 70-90%, prevents jank

---

### 5. Memoization

**What**: Cache results of expensive function calls

**When to Use**:
- Pure functions with repeated calls
- Expensive calculations
- React component renders
- API response transformations

**Implementation**:

```javascript
// Simple memoization
function memoize(fn) {
  const cache = new Map();
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache.has(key)) {
      return cache.get(key);
    }
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

// Usage
const expensive_calculation = memoize((n) => {
  let result = 0;
  for (let i = 0; i < n * 1000000; i++) {
    result += i;
  }
  return result;
});

// React memoization
const MemoizedComponent = React.memo(({ data }) => {
  return <div>{expensiveTransform(data)}</div>;
});

const memoized_value = useMemo(() => {
  return expensive_calculation(count);
}, [count]);
```

**Impact**: Reduces computation time by 80-95% for repeated calls

---

### 6. Virtual Scrolling

**What**: Render only visible items in long lists

**When to Use**:
- Lists with 100+ items
- Infinite scroll implementations
- Data tables with many rows
- Chat histories

**Implementation**:

```javascript
// Simple virtual scroll
class VirtualScroll {
  constructor(container, items, item_height) {
    this.container = container;
    this.items = items;
    this.item_height = item_height;
    this.visible_count = Math.ceil(container.clientHeight / item_height);
    this.render();
  }

  render() {
    const scroll_top = this.container.scrollTop;
    const start_index = Math.floor(scroll_top / this.item_height);
    const end_index = start_index + this.visible_count;

    // Render only visible items
    const visible_items = this.items.slice(start_index, end_index);
    this.container.innerHTML = visible_items.map(item =>
      `<div style="height: ${this.item_height}px">${item}</div>`
    ).join('');
  }
}

// Using react-window library
import { FixedSizeList } from 'react-window';

const Row = ({ index, style }) => (
  <div style={style}>Item {index}</div>
);

<FixedSizeList
  height={600}
  itemCount={10000}
  itemSize={50}
  width="100%"
>
  {Row}
</FixedSizeList>
```

**Impact**: Reduces DOM nodes from 10,000 to ~20, improves FPS from 15 to 60

---

## Asset Optimizations

### 7. Image Compression

**What**: Reduce image file sizes without visible quality loss

**When to Use**: All images (photos, graphics, icons)

**Implementation**:

```bash
# Using imagemin CLI
npm install -g imagemin-cli imagemin-mozjpeg imagemin-pngquant

# Compress JPEGs (quality 80)
imagemin input/*.jpg --out-dir=output --plugin=mozjpeg --plugin.quality=80

# Compress PNGs
imagemin input/*.png --out-dir=output --plugin=pngquant --plugin.quality=80-90

# Using sharp (Node.js)
const sharp = require('sharp');

sharp('input.jpg')
  .resize(1920, 1080, { fit: 'inside' })
  .jpeg({ quality: 80, progressive: true })
  .toFile('output.jpg');
```

**Compression Targets**:
- JPEGs: 80-85 quality (visually lossless)
- PNGs: Quantize to 256 colors
- Photos >500KB: Needs compression
- Hero images: Max 200KB

**Impact**: Reduces image sizes by 40-70%, saves 1-3s load time

---

### 8. Modern Image Formats

**What**: Use WebP/AVIF for better compression than JPEG/PNG

**When to Use**: All raster images with browser fallback

**Implementation**:

```html
<!-- Using picture element with fallback -->
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description">
</picture>

<!-- Using server-side detection -->
<img src="/image?format=auto" alt="Description">
```

```javascript
// JavaScript conversion with sharp
sharp('input.jpg')
  .webp({ quality: 80 })
  .toFile('output.webp');

sharp('input.jpg')
  .avif({ quality: 65 })
  .toFile('output.avif');
```

**File Size Comparison** (same quality):
- JPEG: 100KB
- WebP: 60KB (-40%)
- AVIF: 45KB (-55%)

**Impact**: Reduces image bandwidth by 30-60%

---

### 9. Responsive Images

**What**: Serve appropriately-sized images for device/viewport

**When to Use**: Images displayed at different sizes across devices

**Implementation**:

```html
<!-- Using srcset for resolution switching -->
<img
  srcset="
    image-320w.jpg 320w,
    image-640w.jpg 640w,
    image-1280w.jpg 1280w"
  sizes="
    (max-width: 320px) 280px,
    (max-width: 640px) 600px,
    1200px"
  src="image-640w.jpg"
  alt="Description">

<!-- Art direction with picture -->
<picture>
  <source media="(max-width: 640px)" srcset="image-portrait.jpg">
  <source media="(min-width: 641px)" srcset="image-landscape.jpg">
  <img src="image-landscape.jpg" alt="Description">
</picture>
```

**Impact**: Reduces mobile image downloads by 60-80%

---

### 10. Font Optimization

**What**: Optimize web font loading and rendering

**When to Use**: All custom web fonts

**Implementation**:

```css
/* Font display strategy */
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2'),
       url('font.woff') format('woff');
  font-display: swap;  /* Show fallback immediately */
  font-weight: 400;
  font-style: normal;
}

/* Subset fonts (include only needed characters) */
@font-face {
  font-family: 'Heading';
  src: url('heading-latin.woff2') format('woff2');
  unicode-range: U+0020-007F;  /* Latin only */
}

/* Preload critical fonts */
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

**Font Subsetting** (glyphhanger tool):
```bash
# Subset to Latin characters
glyphhanger --LATIN --subset=font.ttf --formats=woff2,woff
```

**Impact**: Reduces font files by 50-80%, eliminates FOIT (flash of invisible text)

---

### 11. CSS Optimization

**What**: Minimize and optimize CSS delivery

**When to Use**: All CSS files

**Implementation**:

```bash
# Remove unused CSS with PurgeCSS
npm install purgecss
purgecss --css style.css --content index.html --output clean.css

# Critical CSS extraction
npm install critical
critical index.html --base . --inline --minify
```

```html
<!-- Inline critical CSS -->
<style>
  /* Critical above-the-fold styles */
  .header { background: #000; }
</style>

<!-- Defer non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```

**Impact**: Reduces CSS from 300KB to 40KB, improves FCP by 0.5-1s

---

## Runtime Optimizations

### 12. Avoid Layout Thrashing

**What**: Batch DOM reads and writes to prevent forced reflows

**When to Use**: Any code that reads and modifies DOM repeatedly

**Implementation**:

```javascript
// ❌ BAD - Causes layout thrashing
for (let i = 0; i < elements.length; i++) {
  const height = elements[i].offsetHeight;  // Read (forces layout)
  elements[i].style.height = height + 10 + 'px';  // Write
}

// ✅ GOOD - Batch reads, then writes
const heights = [];
for (let i = 0; i < elements.length; i++) {
  heights.push(elements[i].offsetHeight);  // Read
}
for (let i = 0; i < elements.length; i++) {
  elements[i].style.height = heights[i] + 10 + 'px';  // Write
}

// ✅ BETTER - Use requestAnimationFrame
function update_layout() {
  requestAnimationFrame(() => {
    // Batch all reads
    const heights = elements.map(el => el.offsetHeight);

    requestAnimationFrame(() => {
      // Batch all writes
      elements.forEach((el, i) => {
        el.style.height = heights[i] + 10 + 'px';
      });
    });
  });
}
```

**Impact**: Reduces layout calculations from 1000+ to 1, improves FPS from 20 to 60

---

### 13. requestAnimationFrame for Animations

**What**: Sync animations with browser refresh rate

**When to Use**: All JavaScript animations

**Implementation**:

```javascript
// ❌ BAD - Not synced with refresh
setInterval(() => {
  element.style.left = position + 'px';
  position += 1;
}, 16);

// ✅ GOOD - Synced with refresh
function animate() {
  element.style.left = position + 'px';
  position += 1;
  if (position < max_position) {
    requestAnimationFrame(animate);
  }
}
requestAnimationFrame(animate);

// ✅ BETTER - With timing control
let start;
function animate(timestamp) {
  if (!start) start = timestamp;
  const progress = timestamp - start;

  element.style.left = Math.min(progress / 10, max_position) + 'px';

  if (progress < 1000) {
    requestAnimationFrame(animate);
  }
}
requestAnimationFrame(animate);
```

**Impact**: Ensures 60 FPS, reduces CPU usage by 30-50%

---

### 14. Web Workers

**What**: Offload heavy computation to background thread

**When to Use**:
- Data processing (parsing, sorting, filtering)
- Image manipulation
- Cryptographic operations
- Complex calculations

**Implementation**:

```javascript
// Main thread
const worker = new Worker('worker.js');

worker.postMessage({ data: large_dataset, action: 'process' });

worker.onmessage = (e) => {
  const processed_data = e.data;
  update_ui(processed_data);
};

// worker.js
self.onmessage = (e) => {
  const { data, action } = e.data;

  if (action === 'process') {
    const result = heavy_processing(data);
    self.postMessage(result);
  }
};

function heavy_processing(data) {
  // CPU-intensive work here
  return data.map(item => complex_calculation(item));
}
```

**Impact**: Keeps main thread responsive, prevents freezing during heavy operations

---

### 15. Request Batching

**What**: Combine multiple API requests into single call

**When to Use**:
- Multiple endpoint calls on page load
- Sequential dependent requests
- Polling multiple resources

**Implementation**:

```javascript
// ❌ BAD - Multiple sequential requests
const user = await fetch('/api/user/123');
const posts = await fetch('/api/posts?user=123');
const comments = await fetch('/api/comments?user=123');

// ✅ GOOD - Parallel requests
const [user, posts, comments] = await Promise.all([
  fetch('/api/user/123'),
  fetch('/api/posts?user=123'),
  fetch('/api/comments?user=123')
]);

// ✅ BETTER - Single batched request
const response = await fetch('/api/batch', {
  method: 'POST',
  body: JSON.stringify({
    requests: [
      { endpoint: 'user', id: 123 },
      { endpoint: 'posts', user: 123 },
      { endpoint: 'comments', user: 123 }
    ]
  })
});
const { user, posts, comments } = await response.json();
```

**Impact**: Reduces network overhead by 60-80%, improves TTI by 0.5-2s

---

## Caching Strategies

### 16. Browser Cache Headers

**What**: Configure HTTP caching for static assets

**When to Use**: All static resources (CSS, JS, images, fonts)

**Implementation**:

```nginx
# Nginx configuration
location ~* \.(css|js|jpg|jpeg|png|gif|ico|woff|woff2)$ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}

location ~* \.(html)$ {
  expires -1;
  add_header Cache-Control "no-cache, no-store, must-revalidate";
}
```

```javascript
// Express.js
app.use('/static', express.static('public', {
  maxAge: '1y',
  immutable: true
}));
```

**Cache Strategy**:
- Versioned assets (app.v123.js): 1 year, immutable
- HTML: no-cache (always revalidate)
- API responses: Short TTL or no-cache

**Impact**: Eliminates repeat downloads, 90%+ cache hit rate

---

### 17. Service Worker Caching

**What**: Programmatic cache control with Service Workers

**When to Use**:
- Offline functionality
- App shell caching
- API response caching
- Background sync

**Implementation**:

```javascript
// service-worker.js
const CACHE_NAME = 'app-v1';
const STATIC_ASSETS = [
  '/',
  '/styles.css',
  '/app.js',
  '/logo.png'
];

// Install - cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(STATIC_ASSETS))
  );
});

// Fetch - cache-first strategy
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});

// Network-first for API calls
self.addEventListener('fetch', (event) => {
  if (event.request.url.includes('/api/')) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME)
            .then(cache => cache.put(event.request, clone));
          return response;
        })
        .catch(() => caches.match(event.request))
    );
  }
});
```

**Impact**: Instant repeat loads, offline functionality

---

### 18. CDN for Static Assets

**What**: Serve static assets from geographically distributed servers

**When to Use**: All static assets (images, CSS, JS, fonts)

**Implementation**:

```html
<!-- Use CDN URLs -->
<link rel="stylesheet" href="https://cdn.example.com/styles.css">
<script src="https://cdn.example.com/app.js"></script>
<img src="https://cdn.example.com/images/logo.png">
```

```javascript
// Configure CDN in build
const CDN_URL = 'https://cdn.example.com';

module.exports = {
  output: {
    publicPath: CDN_URL + '/'
  }
};
```

**CDN Providers**:
- Cloudflare (free tier available)
- CloudFront (AWS)
- Fastly
- Akamai

**Impact**: Reduces latency by 50-200ms, improves global performance

---

## Advanced Optimizations

### 19. Resource Hints

**What**: Give browser hints about future resource needs

**Implementation**:

```html
<!-- DNS prefetch - Resolve DNS early -->
<link rel="dns-prefetch" href="//api.example.com">

<!-- Preconnect - Establish connection early -->
<link rel="preconnect" href="https://fonts.googleapis.com">

<!-- Prefetch - Load resource for next navigation -->
<link rel="prefetch" href="/page2.html">

<!-- Preload - Load critical resource ASAP -->
<link rel="preload" href="hero.jpg" as="image">
<link rel="preload" href="font.woff2" as="font" crossorigin>

<!-- Prerender - Render entire page in background -->
<link rel="prerender" href="/next-page.html">
```

**Impact**: Reduces connection time by 100-300ms, faster page transitions

---

### 20. Compression (Gzip/Brotli)

**What**: Compress text assets before transfer

**When to Use**: All text assets (HTML, CSS, JS, JSON, SVG)

**Implementation**:

```nginx
# Nginx - Enable Brotli
brotli on;
brotli_types text/css text/javascript application/javascript application/json;
brotli_comp_level 6;

# Fallback to Gzip
gzip on;
gzip_types text/css text/javascript application/javascript application/json;
gzip_comp_level 6;
```

**Compression Comparison**:
- Uncompressed: 500KB
- Gzip: 150KB (-70%)
- Brotli: 120KB (-76%)

**Impact**: Reduces transfer size by 70-80% for text assets

---

## Quick Reference Matrix

| Optimization | Complexity | Impact | When to Apply |
|-------------|-----------|--------|---------------|
| Lazy Loading | Low | High | Always for below-fold content |
| Code Splitting | Medium | High | SPAs, large bundles |
| Tree Shaking | Low | Medium | Using large libraries |
| Debouncing | Low | High | Input handlers, scroll |
| Memoization | Low | Medium | Repeated expensive calls |
| Virtual Scroll | Medium | High | Lists >100 items |
| Image Compression | Low | High | All images |
| WebP/AVIF | Low | Medium-High | All raster images |
| Responsive Images | Low | High | Images on mobile |
| Font Optimization | Low | Medium | Custom fonts |
| CSS Optimization | Medium | Medium | Large CSS files |
| Layout Batching | Medium | High | DOM manipulation |
| requestAnimationFrame | Low | High | All animations |
| Web Workers | High | Medium-High | Heavy computation |
| Request Batching | Medium | Medium | Multiple API calls |
| Browser Cache | Low | High | All static assets |
| Service Workers | High | High | Offline, app shell |
| CDN | Low | High | All static assets |
| Resource Hints | Low | Low-Medium | Critical resources |
| Compression | Low | High | All text assets |

## Optimization Prioritization

### Priority 1 (Quick Wins)
1. Image compression
2. Browser cache headers
3. Gzip/Brotli compression
4. Lazy load images
5. Debounce/throttle handlers

### Priority 2 (High Impact)
1. Code splitting
2. Tree shaking
3. Font optimization
4. CDN for static assets
5. Resource hints (preload/preconnect)

### Priority 3 (Advanced)
1. Service Workers
2. Web Workers
3. Virtual scrolling
4. Request batching
5. Layout thrashing prevention

## Measuring Impact

Always measure before and after:

```javascript
// Performance API
const start = performance.now();
expensive_operation();
const duration = performance.now() - start;
console.log(`Operation took ${duration}ms`);

// User Timing API
performance.mark('operation-start');
expensive_operation();
performance.mark('operation-end');
performance.measure('operation', 'operation-start', 'operation-end');

// Get measurement
const measure = performance.getEntriesByName('operation')[0];
console.log(`Duration: ${measure.duration}ms`);
```

Use Chrome DevTools Lighthouse to validate improvements in Core Web Vitals.
