# Chrome DevTools Performance Workflows

Step-by-step workflows for using Chrome DevTools to profile, analyze, and optimize performance.

## Performance Tab Workflow

### Step-by-Step Profiling

**1. Open DevTools**
- Press `F12` or `Cmd+Option+I` (Mac) / `Ctrl+Shift+I` (Windows)
- Navigate to **Performance** tab

**2. Configure Recording Settings**
- Click **gear icon** for settings
- Enable:
  - [x] Screenshots
  - [x] Memory
  - [x] Web Vitals
- Network throttling: **Fast 3G** (for realistic testing)
- CPU throttling: **4x slowdown** (for realistic testing)

**3. Start Recording**
- Click **Record** button (●)
- **OR** `Cmd+E` / `Ctrl+E`
- Page will automatically reload if "reload" icon clicked

**4. Perform User Actions**
- Load the page
- Scroll through content
- Click interactive elements
- Navigate between sections

**5. Stop Recording**
- Click **Stop** button
- **OR** `Cmd+E` / `Ctrl+E`
- DevTools analyzes and displays results

**6. Analyze Results** (see sections below)

---

### Reading the Flame Chart

**Layout**:
```
├─ Network (top)      Timeline of resource loading
├─ Main Thread        JavaScript execution, rendering, painting
├─ Compositor         GPU operations
├─ Raster             Tile rasterization
└─ GPU                Hardware acceleration
```

**Color Coding**:
- **Yellow**: JavaScript execution
- **Purple**: Rendering (style calculation, layout)
- **Green**: Painting
- **Light Blue**: Loading (parse HTML, CSS)
- **Gray**: Idle time
- **Red Corners**: Long tasks (>50ms)

**Interaction**:
- **Zoom**: `W` to zoom in, `S` to zoom out
- **Pan**: `A` to move left, `D` to move right
- **Select**: Click and drag to select time range
- **Fit**: Double-click background to fit all

---

### Identifying Bottlenecks

**1. Long Tasks** (Yellow with red corner)

**What to Look For**:
- Tasks >50ms block main thread
- Red triangles in top-right corner
- Large yellow blocks

**Analysis**:
1. Click on the long task
2. Check **Bottom-Up** tab
3. Identify function consuming most time
4. Review call stack

**Example**:
```
Task: 287ms
├─ Function Call: 245ms
│  └─ expensive_calculation: 240ms  ← BOTTLENECK
└─ Layout: 42ms
```

**Solution**: Break into chunks, optimize algorithm, or move to Web Worker

---

**2. Excessive Layout/Reflow** (Purple blocks)

**What to Look For**:
- Multiple purple "Layout" blocks
- Layout triggered repeatedly
- Layout during scroll/animation

**Analysis**:
1. Select purple "Layout" block
2. Check **Summary** panel
3. Look for "Layout forced" warning
4. Review stack trace

**Forced Synchronous Layout Pattern**:
```javascript
// ❌ Causes forced reflow
for (let i = 0; i < elements.length; i++) {
  const height = element[i].offsetHeight;  // Read - forces layout
  element[i].style.height = height + 10 + 'px';  // Write
}
```

**Solution**: Batch reads and writes, use requestAnimationFrame

---

**3. Excessive Painting** (Green blocks)

**What to Look For**:
- Large green "Paint" blocks
- Paint during scroll/animation
- Repeated painting of same area

**Analysis**:
1. Enable **Rendering** tab (More Tools → Rendering)
2. Check **Paint flashing**
3. Green highlights show painted areas
4. Identify unnecessarily repainted elements

**Common Causes**:
- Elements without `will-change` or `transform`
- Complex CSS (shadows, gradients)
- Large paint areas

**Solution**: Use CSS `will-change`, GPU acceleration, reduce paint complexity

---

**4. JavaScript Execution Time**

**Analysis Using Bottom-Up Tab**:
1. Select time range
2. Go to **Bottom-Up** tab
3. Sort by **Self Time** (descending)
4. Identify heaviest functions

**Metrics**:
- **Self Time**: Time spent in function itself
- **Total Time**: Time including called functions

**Optimization Priority**:
- Functions with high self time
- Functions called many times
- Functions on critical path

---

### Performance Insights Panel

**Access**: Performance panel → **Insights** tab (new in Chrome 102+)

**Automatic Detection**:
- ✓ Long tasks
- ✓ Layout shifts
- ✓ Render-blocking resources
- ✓ Forced reflows
- ✓ Long interaction times

**Usage**:
1. Record performance profile
2. Switch to **Insights** tab
3. Review categorized issues
4. Click issue to see code causing it
5. Follow suggested fixes

---

## Network Tab Workflow

### Analyzing Waterfall

**1. Open Network Tab**
- Go to **Network** tab
- Enable **Preserve log**
- Disable cache: **Disable cache** checkbox

**2. Record Network Activity**
- Reload page
- Observe waterfall loading pattern

**3. Waterfall Chart Reading**

**Colors**:
- **Queueing** (light gray): Waiting in queue
- **Stalled** (gray): Waiting for connection
- **DNS Lookup** (green): Resolving domain
- **Initial connection** (orange): TCP handshake
- **SSL** (orange): TLS negotiation
- **Request sent** (green): Sending request
- **TTFB** (green): Waiting for first byte
- **Content Download** (blue): Downloading response

**Key Metrics**:
```
Request 1: ========|--------|==========|########
           Queuing  TTFB    Download   Total
```

**Analysis Checklist**:
- [ ] Long queueing? → Reduce concurrent requests
- [ ] Long TTFB? → Optimize server performance
- [ ] Long download? → Compress response, use CDN
- [ ] Many requests? → Bundle resources
- [ ] Large sizes? → Optimize assets

---

### Critical Resource Identification

**Find Render-Blocking Resources**:
1. Filter: **CSS** or **JS**
2. Look for resources in **Initiator** chain before First Paint
3. Check **Priority** column (High = render-blocking)

**Optimization**:
```html
<!-- Render-blocking (bad) -->
<link rel="stylesheet" href="styles.css">
<script src="app.js"></script>

<!-- Non-blocking (good) -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<script defer src="app.js"></script>
```

---

### Resource Timing Analysis

**Export HAR File** (for offline analysis):
1. Right-click network log
2. **Save all as HAR with content**
3. Analyze with tools like WebPageTest

**Analyze Specific Resources**:
1. Click resource
2. **Timing** tab shows breakdown
3. **Headers** tab shows cache headers
4. **Preview** tab shows content

**Timing Breakdown**:
- **Queueing**: <100ms ideal
- **DNS**: <50ms (use dns-prefetch)
- **TCP**: <100ms (use preconnect)
- **TTFB**: <600ms (optimize server)
- **Download**: Varies by size

---

## Memory Tab Workflow

### Heap Snapshot Analysis

**1. Take Initial Snapshot**
- Go to **Memory** tab
- Select **Heap snapshot**
- Click **Take snapshot**

**2. Perform Actions**
- Navigate page
- Open/close modals
- Load/unload content

**3. Take Second Snapshot**
- Click **Take snapshot** again
- Now you have before/after comparison

**4. Compare Snapshots**
- Select second snapshot
- Change view to **Comparison**
- Sort by **Delta** (descending)
- Look for unexpected growth

**5. Investigate Leaks**
- Objects with positive delta are potential leaks
- Click object to see retainer path
- Identify what's holding reference

**Leak Indicators**:
- Detached DOM nodes (should be garbage collected)
- Growing arrays/objects
- Event listeners not removed
- Timers not cleared

**Example Leak Pattern**:
```javascript
// ❌ Memory leak - event listener not removed
class Component {
  constructor() {
    window.addEventListener('resize', this.handleResize);
  }

  handleResize() {
    // Handler keeps component in memory
  }
}

// ✅ Fixed - remove listener
class Component {
  constructor() {
    this.handleResize = this.handleResize.bind(this);
    window.addEventListener('resize', this.handleResize);
  }

  destroy() {
    window.removeEventListener('resize', this.handleResize);
  }

  handleResize() {
    // Handler properly cleaned up
  }
}
```

---

### Allocation Timeline

**Usage** (find when allocations occur):
1. Select **Allocation instrumentation on timeline**
2. Click **Start**
3. Perform actions
4. Click **Stop**
5. Blue bars show allocations over time

**Analysis**:
- Tall blue bars = large allocations
- Many small bars = frequent allocations
- Select time range to see allocated objects
- Useful for finding allocation hot spots

---

## Lighthouse Workflow

### Running Audits

**1. Open Lighthouse**
- Go to **Lighthouse** tab
- Or `Cmd+Shift+P` → "Lighthouse"

**2. Configure Audit**
- Categories:
  - [x] Performance
  - [ ] Accessibility (optional)
  - [ ] Best Practices (optional)
  - [ ] SEO (optional)
- Mode: **Navigation** (default)
- Device: **Mobile** or **Desktop**

**3. Run Audit**
- Click **Analyze page load**
- Wait 30-60 seconds
- Review results

**4. Interpret Results**

**Performance Score** (0-100):
- 90-100: Good (green)
- 50-89: Needs improvement (orange)
- 0-49: Poor (red)

**Metrics Breakdown**:
- FCP (10%)
- LCP (25%)
- TBT (30%)
- CLS (15%)
- Speed Index (10%)
- TTI (10%)

**5. Prioritize Fixes**

**Review Sections**:
1. **Opportunities**: Biggest impact (shows estimated savings)
2. **Diagnostics**: Issues to investigate
3. **Passed audits**: What's working well

**Priority Order**:
1. Opportunities with >1s savings
2. Render-blocking resources
3. Unused JavaScript/CSS
4. Image optimizations
5. Diagnostic warnings

---

### Interpreting Opportunities

**Example Opportunities & Fixes**:

| Opportunity | Potential Savings | Fix |
|-------------|-------------------|-----|
| Properly size images | 2.1s | Serve responsive images |
| Defer offscreen images | 1.8s | Add lazy loading |
| Eliminate render-blocking | 1.2s | Defer/async non-critical CSS/JS |
| Unused JavaScript | 0.9s | Code split, remove dead code |
| Use modern formats | 0.7s | Convert to WebP/AVIF |
| Minify JavaScript | 0.4s | Enable minification in build |

**Click Opportunity** to see:
- Specific resources affected
- Current vs. potential size
- Implementation guidance
- Learn more link

---

## Rendering Tab Tools

**Access**: More Tools → Rendering

### Paint Flashing

**Enable**: Check **Paint flashing**

**Usage**:
- Green highlights = areas being painted
- More flashing = more painting (bad)
- Should only flash on actual content changes

**Optimization**:
- Reduce paint area
- Use CSS containment
- Promote to compositor layer

---

### Layout Shift Regions

**Enable**: Check **Layout Shift Regions**

**Usage**:
- Blue = elements shifted
- Highlights during CLS events
- Helps identify cause of layout shifts

**Fix Checklist**:
- [ ] Add dimensions to images
- [ ] Reserve space for ads/embeds
- [ ] Use aspect-ratio CSS
- [ ] Avoid dynamic content injection

---

### Frame Rendering Stats

**Enable**: Check **Frame Rendering Stats**

**Metrics Shown**:
- **Frames** (FPS): Target 60 FPS
- **GPU memory**: Memory used by GPU
- **Duration**: Frame render time

**Usage**:
- Monitor during scroll/animation
- Drops below 60 FPS = jank
- Spikes in GPU memory = potential issue

---

## Coverage Tab Workflow

**Access**: More Tools → Coverage

**Usage**:
1. Click **Start instrumenting coverage**
2. Load page and interact
3. Stop recording
4. Review unused code (red bars)

**Metrics**:
- **Total bytes**: File size
- **Unused bytes**: Not executed
- **Usage visualization**: Red (unused) / Blue (used)

**Optimization**:
- Remove files with >70% unused code
- Code split to load on-demand
- Defer non-critical scripts

---

## Quick Workflow Checklist

**Performance Audit** (15 minutes):
1. [ ] Run Lighthouse audit (Mobile & Desktop)
2. [ ] Record Performance profile of page load
3. [ ] Identify long tasks (>50ms)
4. [ ] Check Network waterfall for bottlenecks
5. [ ] Review render-blocking resources
6. [ ] Check Coverage tab for unused code
7. [ ] Take Heap snapshot for memory leaks
8. [ ] Enable Paint flashing to check repaints
9. [ ] Document findings with screenshots
10. [ ] Prioritize fixes by impact

**Deep Performance Analysis** (1-2 hours):
1. [ ] Run Lighthouse for baseline
2. [ ] Record full page load in Performance tab
3. [ ] Analyze flame chart for bottlenecks
4. [ ] Review all network requests in Network tab
5. [ ] Check memory usage with heap snapshots
6. [ ] Monitor for memory leaks with allocation timeline
7. [ ] Use Coverage tab to find unused code
8. [ ] Enable all Rendering tab options for visual debugging
9. [ ] Test with network/CPU throttling
10. [ ] Compare before/after metrics
11. [ ] Document all optimizations applied
12. [ ] Re-run Lighthouse to verify improvements

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Open DevTools | `F12` or `Cmd+Option+I` |
| Performance record/stop | `Cmd+E` / `Ctrl+E` |
| Take screenshot | `Cmd+Shift+P` → "screenshot" |
| Clear console | `Cmd+K` / `Ctrl+L` |
| Search files | `Cmd+P` / `Ctrl+P` |
| Search all | `Cmd+Shift+F` / `Ctrl+Shift+F` |
| Command palette | `Cmd+Shift+P` / `Ctrl+Shift+P` |
| Toggle device mode | `Cmd+Shift+M` / `Ctrl+Shift+M` |

## DevTools Settings

**Recommended Settings**:
- [ ] Disable cache (when DevTools open)
- [ ] Preserve log
- [ ] Show timestamps (Console)
- [ ] Enable JavaScript source maps
- [ ] Enable CSS source maps
- [ ] Dark theme (optional)
