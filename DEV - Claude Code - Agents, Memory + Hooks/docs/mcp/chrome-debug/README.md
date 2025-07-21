# Chrome Debug MCP Documentation

## Overview

Chrome Debug MCP provides direct access to Chrome DevTools Protocol, enabling low-level browser debugging, performance profiling, and advanced Chrome automation features not available through higher-level automation tools.

## Key Features

- **DevTools Protocol Access**: Direct CDP (Chrome DevTools Protocol) commands
- **Console Log Monitoring**: Real-time access to browser console
- **Performance Profiling**: CPU, memory, and rendering metrics
- **Network Inspection**: Request/response monitoring and modification
- **JavaScript Debugging**: Breakpoints and execution control

## Available Tools

### `mcp__chrome-debug__launch_chrome`
Launch Chrome in debug mode with custom configuration.

**Parameters:**
- `url`: Initial URL to navigate to (optional)
- `executablePath`: Path to Chrome executable (optional, uses bundled)
- `userDataDir`: Chrome profile directory (optional)
- `loadExtension`: Path to unpacked extension (optional)
- `userscriptPath`: Path to userscript to inject (optional)
- `disableAutomationControlled`: Hide automation indicators (default: false)
- `disableExtensionsExcept`: Keep specific extension enabled

**Example:**
```python
{
    "url": "https://example.com",
    "disableAutomationControlled": true,
    "userDataDir": "/path/to/profile",
    "loadExtension": "/path/to/extension"
}
```

### `mcp__chrome-debug__get_console_logs`
Retrieve console logs from the browser.

**Parameters:**
- `clear`: Clear logs after retrieval (default: false)

**Returns:**
Array of console entries with:
- `level`: Log level (log, warn, error, info)
- `text`: Log message
- `timestamp`: When logged
- `source`: Origin of log

### `mcp__chrome-debug__evaluate`
Execute JavaScript in the browser context.

**Parameters:**
- `expression`: JavaScript code to evaluate

**Example:**
```python
{
    "expression": "document.title"
}
```

## Advanced Use Cases

### 1. Performance Profiling
```python
# Start performance recording
chrome_debug_evaluate(expression="""
    performance.mark('task-start');
""")

# Execute operations...

# Measure performance
chrome_debug_evaluate(expression="""
    performance.mark('task-end');
    performance.measure('task-duration', 'task-start', 'task-end');
    const measures = performance.getEntriesByType('measure');
    return measures[measures.length - 1].duration;
""")
```

### 2. Memory Analysis
```python
# Get memory usage
memory_info = chrome_debug_evaluate(expression="""
    if (performance.memory) {
        return {
            usedJSHeapSize: performance.memory.usedJSHeapSize,
            totalJSHeapSize: performance.memory.totalJSHeapSize,
            jsHeapSizeLimit: performance.memory.jsHeapSizeLimit
        };
    }
""")

# Force garbage collection
chrome_debug_evaluate(expression="gc && gc()")
```

### 3. Network Monitoring
```python
# Monitor fetch requests
chrome_debug_evaluate(expression="""
    const originalFetch = window.fetch;
    window.fetchLog = [];
    
    window.fetch = async (...args) => {
        const startTime = performance.now();
        const response = await originalFetch(...args);
        const endTime = performance.now();
        
        window.fetchLog.push({
            url: args[0],
            method: args[1]?.method || 'GET',
            status: response.status,
            duration: endTime - startTime
        });
        
        return response;
    };
""")

# Get network log
network_log = chrome_debug_evaluate(expression="window.fetchLog")
```

### 4. Extension Development
```python
# Launch with extension
chrome_debug_launch_chrome(
    loadExtension="/path/to/extension",
    url="chrome://extensions"
)

# Test extension functionality
chrome_debug_evaluate(expression="""
    // Access extension APIs
    chrome.runtime.sendMessage({action: 'test'});
""")

# Check console for extension logs
logs = chrome_debug_get_console_logs()
```

### 5. Debugging Production Issues
```python
# Launch with production site
chrome_debug_launch_chrome(
    url="https://production.example.com",
    disableAutomationControlled=true
)

# Monitor errors
chrome_debug_evaluate(expression="""
    window.addEventListener('error', (e) => {
        console.error('Runtime error:', {
            message: e.message,
            filename: e.filename,
            line: e.lineno,
            column: e.colno,
            stack: e.error?.stack
        });
    });
""")

# Get error logs
errors = chrome_debug_get_console_logs()
error_logs = [log for log in errors if log['level'] == 'error']
```

## DevTools Protocol Examples

### Page Domain
```python
# Navigate with DevTools protocol
chrome_debug_evaluate(expression="""
    // Equivalent to Page.navigate
    window.location.href = 'https://example.com';
""")

# Get page metrics
chrome_debug_evaluate(expression="""
    JSON.stringify({
        url: window.location.href,
        title: document.title,
        readyState: document.readyState,
        documentHeight: document.documentElement.scrollHeight
    })
""")
```

### Runtime Domain
```python
# Evaluate with return value
result = chrome_debug_evaluate(expression="""
    // Complex evaluation
    (() => {
        const data = Array.from(document.querySelectorAll('a'))
            .map(link => ({
                href: link.href,
                text: link.textContent.trim()
            }));
        return JSON.stringify(data);
    })()
""")
```

### Console Domain
```python
# Monitor console API calls
chrome_debug_evaluate(expression="""
    const methods = ['log', 'warn', 'error', 'info'];
    methods.forEach(method => {
        const original = console[method];
        console[method] = (...args) => {
            original.apply(console, [`[${method.toUpperCase()}]`, ...args]);
        };
    });
""")
```

## Security Testing

### 1. CSP Violation Detection
```python
chrome_debug_evaluate(expression="""
    document.addEventListener('securitypolicyviolation', (e) => {
        console.error('CSP Violation:', {
            blockedURI: e.blockedURI,
            violatedDirective: e.violatedDirective,
            originalPolicy: e.originalPolicy
        });
    });
""")
```

### 2. Mixed Content Detection
```python
chrome_debug_evaluate(expression="""
    // Check for mixed content
    const insecureElements = Array.from(document.querySelectorAll('*'))
        .filter(el => {
            const src = el.src || el.href;
            return src && src.startsWith('http://') && 
                   window.location.protocol === 'https:';
        });
    console.warn('Mixed content found:', insecureElements.length);
""")
```

### 3. XSS Testing
```python
# Test XSS filters (safely)
chrome_debug_evaluate(expression="""
    // Test if inline scripts are blocked
    const testScript = document.createElement('script');
    testScript.textContent = 'console.log("XSS Test - This should be blocked")';
    try {
        document.head.appendChild(testScript);
    } catch (e) {
        console.log('Good: Inline scripts blocked', e.message);
    }
""")
```

## Performance Optimization

### 1. Render Performance
```python
chrome_debug_evaluate(expression="""
    // Monitor long tasks
    const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
            if (entry.duration > 50) {
                console.warn('Long task detected:', {
                    duration: entry.duration,
                    startTime: entry.startTime
                });
            }
        }
    });
    observer.observe({ entryTypes: ['longtask'] });
""")
```

### 2. Resource Timing
```python
chrome_debug_evaluate(expression="""
    const resources = performance.getEntriesByType('resource');
    const slowResources = resources
        .filter(r => r.duration > 1000)
        .map(r => ({
            name: r.name,
            duration: r.duration,
            size: r.transferSize
        }));
    return JSON.stringify(slowResources);
""")
```

## Troubleshooting

### Chrome Won't Launch
- Check Chrome installation path
- Verify no other Chrome instances running
- Check firewall/antivirus blocking
- Try with `--no-sandbox` flag

### Evaluation Errors
- Ensure valid JavaScript syntax
- Check for undefined variables
- Use try-catch for error handling
- Return serializable values (JSON)

### Console Logs Missing
- Verify console methods not overridden
- Check log level filtering
- Ensure logs happen after connection
- Use `clear: false` to preserve logs

## Best Practices

### 1. Resource Cleanup
```python
# Always evaluate cleanup code
chrome_debug_evaluate(expression="""
    // Remove event listeners
    window.removeEventListener('error', window.errorHandler);
    
    // Clear intervals/timeouts
    for (let i = 1; i < 9999; i++) {
        clearInterval(i);
        clearTimeout(i);
    }
    
    // Reset modifications
    window.fetch = window.originalFetch || window.fetch;
""")
```

### 2. Error Handling
```python
# Wrap evaluations in try-catch
chrome_debug_evaluate(expression="""
    try {
        // Your code here
        return JSON.stringify({ success: true, data: result });
    } catch (error) {
        return JSON.stringify({ 
            success: false, 
            error: error.message,
            stack: error.stack 
        });
    }
""")
```

### 3. State Management
```python
# Use namespaced globals
chrome_debug_evaluate(expression="""
    window.__DEBUG__ = window.__DEBUG__ || {};
    window.__DEBUG__.startTime = Date.now();
    window.__DEBUG__.logs = [];
""")
```

## Integration with Other Tools

### With Playwright/Puppeteer
Use Chrome Debug for advanced debugging while using Playwright/Puppeteer for automation:
1. Launch Chrome with remote debugging port
2. Connect Playwright/Puppeteer to existing Chrome
3. Use Chrome Debug for low-level access

### With Performance Tools
Export performance data for analysis:
```python
perf_data = chrome_debug_evaluate(expression="""
    JSON.stringify({
        navigation: performance.getEntriesByType('navigation')[0],
        resources: performance.getEntriesByType('resource'),
        marks: performance.getEntriesByType('mark'),
        measures: performance.getEntriesByType('measure')
    })
""")
```

## Related Documentation
- [Playwright MCP](../playwright/README.md) - High-level automation
- [Puppeteer MCP](../puppeteer/README.md) - Chrome automation
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)