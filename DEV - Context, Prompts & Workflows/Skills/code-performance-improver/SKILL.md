---
name: code-performance-improver
description: Optimize code and application performance through systematic profiling, analysis, and incremental improvements while preserving all functionality. Use when addressing performance bottlenecks, slow load times, high memory usage, or Core Web Vitals issues. Measures baseline metrics, identifies bottlenecks, applies optimizations incrementally, and verifies improvements without regressions
---

# Performance Improver
Systematically improve application performance through profiling, optimization, and validation while guaranteeing 100% feature preservation.

> Change Notes (2025-10-21)
- Replaced local References with Embedded Reference (Optimization Catalog + Metrics Primer)
- Normalized workflow headings (whole steps only)
- Added YAML → Steps Crosswalk; header-only emoji policy enforced

## 1. 🎯 When to Use

**Use this skill when**:
- Application has slow load times or poor performance
- Core Web Vitals scores need improvement (LCP, FCP, CLS, FID)
- Memory usage is too high or memory leaks suspected
- Animations are choppy or dropping frames below 60 FPS
- Bundle sizes are too large
- Network requests are slow or excessive
- User reports performance issues
- Need to optimize existing working code

**Do NOT use this skill for**:
- Adding new features (focus is optimization only)
- Fixing bugs (use code-debugger skill instead)
- Initial development (performance should come after functionality)
- Code that doesn't work yet (fix functionality first)
- Micro-optimizations without measurable impact

.

## 2. 🛠️ How It Works

This skill follows a 4-step systematic workflow to improve performance while preserving functionality:

1. **Baseline Measurement** - Capture current performance metrics
2. **Analysis** - Identify bottlenecks and prioritize improvements
3. **Optimization** - Apply improvements incrementally with testing
4. **Verification** - Ensure improvements achieved without regressions

**Core Principle**: "Features first, performance second" - Never break functionality for speed

.

## 3. 📊 Inputs

### Required Inputs

**Request**:
- **Description**: What needs to be optimized
- **Format**: Natural language description
- **Examples**:
  - "Improve page load time"
  - "Optimize animation performance"
  - "Reduce memory usage"
  - "Fix choppy scrolling"

### Optional Inputs

**Environment** (staging link):
- **Type**: URL
- **Purpose**: Live environment for browser-based profiling
- **Default**: If empty, skip browser-based profiling steps
- **Example**: `https://staging.example.com`

**Scope** (files):
- **Type**: File path(s) or glob pattern
- **Purpose**: Which files to optimize
- **Default**: All performance-critical files if empty
- **Examples**:
  - `src/animations/*.js`
  - `src/video/video_autoplay_fallback.js`

**Target Folder**:
- **Type**: Directory path
- **Purpose**: Often points to performance plan or optimization spec folder
- **Default**: Current application or infer from request
- **Example**: `specs/005-performance-optimization/`

**Context**:
- **Type**: Text
- **Purpose**: Additional context about the performance issue
- **Default**: Inferred from performance issues and metrics
- **Example**: "Users report slow loading on mobile devices"

**Issues**:
- **Type**: Text
- **Purpose**: Known performance issues
- **Default**: Identified during baseline measurement
- **Example**: "LCP > 4s, main thread blocking 800ms"

.

## YAML → Steps Crosswalk

- Source: b_prompts/code/code_performance_improvement.yaml
- Mapping:
  - Step 1 → Gather User Inputs
  - Step 2 → Baseline Measurement
  - Step 3 → Analysis
  - Step 4 → Optimization
  - Step 5 → Verification

## 4. 🚀 Workflow

### Step 1: Gather User Inputs

**Purpose**: Collect all necessary information before starting optimization

**IMPORTANT**: Before starting the performance improvement workflow, ask the user for the following inputs in a conversational way:

#### Required Inputs:

1. **Request/Performance Goal** (REQUIRED):
   - Ask: "What performance issue would you like me to optimize? Please describe what needs improvement."
   - This is the main optimization goal that drives the workflow.

#### Optional Inputs (with smart defaults):

2. **Issues/Performance Problems**:
   - Ask: "Can you provide details about the performance issues? (Include metrics like 'LCP > 4s' or leave empty to identify during baseline measurement)"
   - Default: Identify during baseline measurement

3. **Environment/Staging Link**:
   - Ask: "Do you have a staging environment URL for browser-based profiling? (Leave empty to skip browser profiling)"
   - Default: Skip browser-based profiling if not provided

4. **Scope/Files**:
   - Ask: "Which files should I optimize? (Leave empty to optimize all performance-critical files)"
   - Default: All performance-critical files

5. **Target Folder**:
   - Ask: "Is there a performance plan or optimization spec folder? (Leave empty to infer from your request)"
   - Default: Current application or infer from request

6. **Context**:
   - Ask: "Any additional context about the performance issue? (Leave empty to infer from metrics)"
   - Default: Infer from performance issues and metrics

**After Collecting Inputs**:
- Confirm all inputs with the user
- Parse and categorize the performance goals
- Identify likely optimization areas

### Step 2: Baseline Measurement

**Purpose**: Measure current performance before any changes

**Actions**:
1. Review target folder plan/spec for performance requirements
2. Capture current metrics using Chrome DevTools
3. Document baseline performance
4. Note specific issues from Issues field
5. Document requirements from Request field

**Metrics to Capture**:
- **Load Time**: Total page load duration
- **Core Web Vitals**:
  - First Contentful Paint (FCP)
  - Largest Contentful Paint (LCP)
  - Cumulative Layout Shift (CLS)
  - First Input Delay (FID)
  - Time to Interactive (TTI)
- **Runtime Performance**: JavaScript execution time, main thread blocking
- **Memory Usage**: Heap size, memory leaks
- **Network**: Request count, waterfall timing, bundle sizes
- **Animation Performance**: FPS for animations (target: 60 FPS)

**Chrome DevTools**:
- Performance tab: Record and analyze page load
- Network tab: Analyze waterfall and request timing
- Memory tab: Heap snapshots for leak detection
- Lighthouse: Run audit for comprehensive metrics

**Documentation**:
- Current metrics table
- Issues discovered or provided
- Performance bottlenecks identified
- Request requirements captured

**Validation**: `baseline_captured_and_documented`

### Step 3: Analysis

**Purpose**: Identify optimization opportunities and prioritize by impact

**Investigation**:
1. Profile critical rendering path
2. Identify main thread bottlenecks
3. Find memory leaks or excessive allocations
4. Analyze bundle sizes and code splitting opportunities
5. Review network waterfall for optimization opportunities

**Prioritization Framework**:

**High Impact** (fix first):
- Critical rendering path blockers
- Main thread blocking (>50ms)
- Memory leaks
- Large unoptimized assets (images, fonts, videos)
- Render-blocking resources

**Medium Impact** (fix next):
- Code splitting opportunities
- Caching improvements (browser, service worker, CDN)
- Image optimization
- Unnecessary re-renders
- Inefficient algorithms

**Low Impact** (fix last):
- Micro-optimizations
- Code cleanup
- Minor bundle size reductions

**Analysis Output**:
- Prioritized list of bottlenecks
- Impact estimation for each issue
- Recommended optimization strategies
- Evidence from profiling tools

**Validation**: `bottlenecks_identified_with_evidence`

### Step 4: Optimization

**Purpose**: Apply improvements incrementally with continuous validation

**Approach**:
- **One optimization at a time**: Apply single change, test, measure
- **Test after each change**: Verify functionality intact
- **Rollback if issues**: Revert if regression occurs
- **Document changes**: Track what was changed and why

**Optimization Strategies**:

**Code Optimizations**:
- Lazy loading: Load resources on-demand
- Code splitting: Split bundles by route or feature
- Tree shaking: Remove unused code
- Debouncing/throttling: Limit expensive operations
- Memoization: Cache expensive computations
- Virtual scrolling: Render only visible items

**Asset Optimizations**:
- Image optimization: Compress, resize, modern formats (WebP, AVIF)
- Font optimization: Subset fonts, use font-display
- CSS optimization: Remove unused styles, minify
- Compression: Enable gzip/brotli

**Runtime Optimizations**:
- Avoid layout thrashing: Batch DOM reads/writes
- Use requestAnimationFrame: Sync with browser refresh
- Web workers: Move heavy computation off main thread
- Request batching: Combine multiple API calls
- Efficient selectors: Optimize DOM queries

**Caching Strategies**:
- Browser caching: Set appropriate cache headers
- Service workers: Offline-first caching
- API response caching: Cache GET requests
- CDN usage: Serve static assets from CDN

**Implementation**:
1. Select highest-priority optimization
2. Apply the change
3. Test functionality (ensure nothing breaks)
4. Measure performance impact
5. Document the change
6. If successful, commit and move to next
7. If regression, rollback and try alternative

**Validation**: `each_optimization_verified`

### Step 5: Verification

**Purpose**: Ensure improvements achieved without any regressions

**Performance Checks**:
- Metrics improved compared to baseline
- No new bottlenecks introduced
- Memory usage stable or reduced
- Better user experience (faster, smoother)

**Functionality Checks**:
- All features working as before
- Animations smooth at 60 FPS
- Business logic preserved
- No visual regressions
- Error handling intact

**Compatibility Checks**:
- Cross-browser testing (Chrome, Firefox, Safari, Edge)
- Mobile performance (test on actual devices or throttling)
- Different network conditions (3G, 4G, WiFi)
- Accessibility preserved (keyboard, screen readers)

**Testing Matrix**:

| Check | Before | After | Status |
|-------|--------|-------|--------|
| Load Time | XXXms | YYYms | ✓/✗ |
| FCP | XXXms | YYYms | ✓/✗ |
| LCP | XXXms | YYYms | ✓/✗ |
| Memory | XXXMB | YYYMB | ✓/✗ |
| Animation FPS | XX | 60 | ✓/✗ |
| Features | Working | Working | ✓/✗ |

**Validation**: `all_checks_pass`

.

## 5. 🔍 Chrome DevTools Integration

### Performance Profiling

**Steps**:
1. Open Chrome DevTools (F12)
2. Go to Performance tab
3. Click Record
4. Perform user actions (page load, scroll, click)
5. Stop recording
6. Analyze flame chart for bottlenecks
7. Export trace for comparison

**What to Look For**:
- Long tasks (yellow/red blocks) blocking main thread
- Excessive layout/paint operations
- JavaScript execution time
- Render-blocking resources

### Network Analysis

**Steps**:
1. Open Network tab
2. Reload page with cache disabled
3. Analyze waterfall visualization
4. Check request timing and sizes
5. Identify optimization opportunities

**What to Look For**:
- Large bundle sizes (>250KB)
- Render-blocking CSS/JS
- Too many requests (>50)
- Slow TTFB (Time to First Byte)
- Missing cache headers

### Memory Profiling

**Steps**:
1. Open Memory tab
2. Take heap snapshot before action
3. Perform user action
4. Take heap snapshot after
5. Compare snapshots for leaks
6. Analyze allocation timeline

**What to Look For**:
- Growing heap size over time
- Detached DOM nodes
- Retained objects after cleanup
- Memory not released after navigation

### Lighthouse Audit

**Steps**:
1. Open Lighthouse tab
2. Select categories (Performance, Best Practices)
3. Run audit
4. Review recommendations
5. Prioritize fixes by impact

**Metrics**:
- Performance score (target: >90)
- Core Web Vitals (all green)
- Opportunities (potential savings)
- Diagnostics (issues found)

### Browser Automation Tool Selection

**Strategy**: Follow this decision tree when browser automation or DevTools access is needed:

1. **Chrome DevTools MCP** (Primary choice)
   - Use available Chrome DevTools MCP servers: `mcp__chrome-devtools__*`
   - Multiple instances available: `chrome-devtools`, `chrome-devtools-2`, `chrome-devtools-3`, `chrome-devtools-4`
   - **If conflicts occur**: Try alternate instances (e.g., switch from -2 to -3)
   - **Why multiple instances**: Each can run with `--isolated` flag to prevent session interference
   - Common functions: `navigate_page`, `take_snapshot`, `evaluate_script`, `performance_start_trace`

2. **Playwright MCP** (Fallback)
   - If Chrome DevTools unavailable or fails repeatedly
   - Use Playwright MCP: `mcp__playwright__*` functions
   - Functions: `playwright_navigate`, `playwright_evaluate`, `playwright_get_visible_html`
   - Provides similar automation with different architecture

3. **Code-Focused Analysis** (Final fallback)
   - If both browser automation MCPs fail or unavailable
   - Use static analysis: Read, Grep, Glob tools
   - Infer behavior from code structure and configuration
   - **Important**: Document assumptions and analysis limitations clearly

**Best Practice**: When browser automation is needed alongside manual development browsing, use an isolated instance to prevent conflicts

.

## 6. 🔒 Preservation Requirements

### Mandatory Preservation

**Features**:
- All functionality remains intact
- Business logic unchanged
- User workflows preserved
- Data integrity maintained
- API contracts unchanged

**Animations**:
- 60 FPS maintained or improved
- Smooth transitions (no jank)
- No visual glitches
- Timing preserved (unless intentionally improved)

**Compatibility**:
- Browser support unchanged
- Mobile functionality preserved
- Accessibility features intact (ARIA, keyboard, focus)
- Responsive design maintained

### Testing Protocol

**After Each Change**:
- Feature still works correctly
- No visual regressions
- Animation performance maintained
- Error handling intact
- User flows unaffected

**Before Commit**:
- Full feature test in target environment
- Cross-browser verification
- Performance improved (with measurements)
- No memory leaks detected
- Lighthouse score improved or maintained

.

## 7. ✅ Success Criteria

### Performance Success

**Metrics**:
- Measurable improvement in target metrics
- Metrics documented with before/after comparison
- Bottlenecks addressed with evidence
- User experience noticeably better
- Lighthouse score improved

### Preservation Success

**Requirements**:
- 100% feature parity confirmed
- Animations smooth at 60 FPS
- Business logic intact
- No regressions in functionality
- Cross-browser compatibility maintained

### Quality Success

**Standards**:
- Code remains maintainable
- Changes documented clearly
- Rollback possible if needed
- Tests updated if applicable
- Future-proof improvements

.

## 8. 📝 Output Format

After completing the workflow, generate a performance optimization report:

```markdown
## Performance Optimization Report

**Date**: [timestamp]
**Target**: [application/feature optimized]
**Request**: [original request]

### Baseline Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Load Time | XXXms | YYYms | -Z% |
| FCP | XXXms | YYYms | -Z% |
| LCP | XXXms | YYYms | -Z% |
| TTI | XXXms | YYYms | -Z% |
| Memory | XXXMB | YYYMB | -Z% |
| Bundle Size | XXXKB | YYYKB | -Z% |

### Optimizations Applied

#### 1. [Optimization Name]
- **Change**: [Description of what was changed]
- **Impact**: [Metric improvements]
- **Files Modified**: [List of files]
- **Verification**: ✓ All features intact

#### 2. [Optimization Name]
- **Change**: [Description]
- **Impact**: [Metrics]
- **Files Modified**: [List]
- **Verification**: ✓ All features intact

### Feature Preservation

- [x] All features tested and working
- [x] Animations at 60 FPS
- [x] No visual regressions
- [x] Business logic intact
- [x] Cross-browser compatible
- [x] Accessibility preserved

### Overall Improvement

- **Performance Gain**: XX% faster
- **User Experience**: [Description of improvement]
- **Risk Level**: Low (all features preserved)
- **Rollback Plan**: [Available if needed]

### Recommendations

[Optional: Future optimization opportunities]
```

.

## 9. 📖 Rules

### ALWAYS

- Measure baseline before any optimization
- Preserve all features and functionality
- Test after each incremental change
- Keep animations at 60 FPS minimum
- Document all improvements with metrics
- Verify no regressions introduced
- Use Chrome DevTools for profiling
- Prioritize high-impact optimizations
- Apply changes incrementally, not all at once

### NEVER

- Break features for speed gains
- Optimize without measuring first
- Skip regression testing
- Ignore edge cases
- Remove functionality
- Apply multiple optimizations simultaneously
- Assume optimization worked without measurement
- Sacrifice maintainability for micro-optimizations

### ROLLBACK IF

- Any feature breaks
- Animation performance drops below 60 FPS
- Visual regression occurs
- Business logic is affected
- User experience degrades
- Memory usage increases
- Accessibility is reduced

### ESCALATE IF

- Performance targets are fundamentally impossible with current architecture
- Optimization requires architectural changes beyond scope
- Performance bottleneck is in external dependencies or platform constraints
- Optimization breaks critical features with no viable workaround
- Memory constraints cannot be resolved without infrastructure changes
- Need specialized performance engineering expertise not available
- Trade-offs between performance and other requirements are unacceptable
- Investigation reveals systemic performance issues requiring team discussion

**When Escalating, Provide**:
- Baseline performance metrics (before optimization attempts)
- All optimization attempts made and their results
- Profiling data and bottleneck analysis
- Identified constraints (architectural, platform, resource)
- Performance targets vs. achievable results
- Recommended architectural changes or infrastructure needs
- Risk assessment if left unresolved

.

## 10. 📚 Embedded Reference

- No External References: This skill is self-contained. Cite only knowledge/*.md when needed.

### Optimization Catalog (condensed)
- Code: lazy loading, code splitting, tree shaking, debouncing/throttling, memoization, virtual scrolling.
- Assets: image compression/resizing/WebP/AVIF, font subsetting/font-display, CSS cleanup/minify.
- Runtime: layout batching, requestAnimationFrame, Web Workers, request batching, efficient selectors.
- Caching: cache headers, service workers, CDN, API response caching.

### Metrics Primer
- Core Web Vitals: LCP, FCP, CLS, INP/TTI/TBT basics.
- Profiling: DevTools Performance/Network/Memory/Lighthouse workflows.

See knowledge/animation_strategy.md and knowledge/webflow_platform_constraints.md for context impacting performance patterns.

.

## 11. 💡 Performance Philosophy

**Core Principle**: "Features first, performance second"

Performance optimization is valuable only when it improves user experience without compromising functionality. This skill ensures every optimization is:

- **Measured**: Backed by metrics, not assumptions
- **Incremental**: One change at a time for clear attribution
- **Validated**: Features preserved, improvements verified
- **Documented**: Changes tracked with before/after evidence

The goal is not just faster code, but better user experience with zero functionality loss.
