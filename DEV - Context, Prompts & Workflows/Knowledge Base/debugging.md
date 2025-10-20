# Webflow Debugging — Quick Guide

Focused, practical debugging for Webflow projects using platform‑specific checks and DevTools MCP workflows.


Concise Webflow debugging playbook. Use these checks first, then apply DevTools MCP workflows (console, network, performance, snapshots) for evidence‑based diagnosis. See also: [../z_prompts/code_debugger.yaml](../z_prompts/code_debugger.yaml).

.

## 1. 🔍 Webflow‑Specific Checks (90‑second sweep)

- Webflow loaded: `!!window.Webflow`
- Interactions queued: `Array.isArray(window.Webflow?.push)`
- Collections present: `document.querySelectorAll('.w-dyn-item').length`
- Editor mode: `!!document.querySelector('.w-editor')`
- Locale: `document.documentElement.lang || 'default'`
- Timing: If collections are 0 on DOMContentLoaded, retry after 500ms (render async)

Helper (optional):
```javascript
(() => {
  console.group('🔍 Webflow Sweep');
  console.log('Webflow:', !!window.Webflow);
  console.log('Push queue:', Array.isArray(window.Webflow?.push));
  console.log('Collections (items):', document.querySelectorAll('.w-dyn-item').length);
  console.log('Editor mode:', !!document.querySelector('.w-editor'));
  console.log('Locale:', document.documentElement.lang || 'default');
  console.groupEnd();
})();
```

.

## 2. 🧰 DevTools MCP Workflows

Use the available DevTools MCP tools to capture facts fast.

- Console logs
  - What: All logs/errors/warnings since last navigation
  - How: list_console_messages
  - Use when: Interactions fail silently; script errors suspected

- Network activity
  - What: Requests, status codes, timing
  - How: list_network_requests (filter by xhr/fetch) and get_network_request(url)
  - Use when: Forms, CMS, or external APIs misbehave

- Performance trace
  - What: Record and surface insights (LCP, long tasks, layout shifts)
  - How: performance_start_trace({ autoStop: true, reload: true }) → performance_analyze_insight('DocumentLatency' | 'LCPBreakdown' | etc.)
  - Use when: Animations jank, delayed interactions, layout thrash

- Page snapshot / screenshot
  - What: DOM snapshot with UIDs or visual capture
  - How: take_snapshot() and take_screenshot({ fullPage: true })
  - Use when: Need stable selectors or to prove visual states

- Page control (as needed)
  - navigate_page(url), resize_page({ width, height }), emulate_network('Fast 3G'|'Offline'), emulate_cpu({ throttlingRate })

.

## 3. 🔧 Browser Automation Tool Selection

When browser automation or DevTools access is needed, follow this decision tree:

### Primary: Chrome DevTools MCP
- **Available servers**: `mcp__chrome-devtools__*` (instances: default, -2, -3, -4)
- **Why multiple instances**: Each can run with `--isolated` flag to prevent session interference
- **If conflicts occur**: Try alternate instances (e.g., switch from -2 to -3)
- **Common functions**: `navigate_page`, `take_snapshot`, `evaluate_script`, `list_console_messages`, `performance_start_trace`

### Fallback: Playwright MCP
- **Use when**: Chrome DevTools unavailable or fails repeatedly
- **Available functions**: `mcp__playwright__*`
- **Functions**: `playwright_navigate`, `playwright_evaluate`, `playwright_get_visible_html`
- **Benefits**: Similar automation with different architecture

### Final Fallback: Code-Focused Analysis
- **Use when**: Both browser automation MCPs fail or unavailable
- **Method**: Static analysis using Read, Grep, Glob tools
- **Approach**: Infer behavior from code structure and configuration
- **Important**: Document assumptions and analysis limitations clearly

**Best Practice**: When browser automation is needed alongside manual development browsing, use an isolated Chrome DevTools instance to prevent conflicts.

.

## 4. 🐛 Common Webflow Root Causes → Checks

- Collections empty intermittently
  - Cause: Async render delay
  - Check: Retry after 500ms or observe DOM mutations

- Interactions don’t fire
  - Cause: Not queued with Webflow.push; element missing
  - Check: Verify `window.Webflow?.push`, confirm target exists

- Duplicate IDs break selectors
  - Cause: Collection items duplicate IDs by design
  - Check: Use classes or data‑attributes + event delegation

- Form success/error blocks missing
  - Cause: Not wrapped in `.w-form`
  - Check: `form.closest('.w-form')`

.

## 5. 🧪 Minimal Helpers (optional)

- Collections quick view
```javascript
(() => {
  const lists = document.querySelectorAll('.w-dyn-list');
  console.table(Array.from(lists).map((l,i)=>({
    list: i+1,
    items: l.querySelectorAll('.w-dyn-item').length,
    nested: l.querySelectorAll('.w-dyn-list').length
  })));
})();
```

- Breakpoints snapshot
```javascript
(() => {
  const bps = [
    { name: 'Desktop', width: 992 },
    { name: 'Tablet', width: 991 },
    { name: 'Mobile Landscape', width: 767 },
    { name: 'Mobile Portrait', width: 478 }
  ];
  console.table(bps.map(bp=>({ name: bp.name, active: innerWidth>=bp.width })));
})();
```

.

## 6. 🔗 References

- MCP flows: console, network, performance, snapshots (see tool descriptions)
- Debug prompt: [../z_prompts/code_debugger.yaml](../z_prompts/code_debugger.yaml)

---

**Remember**: Choose the right tools and remember Webflow's unique constraints during the debugging process.