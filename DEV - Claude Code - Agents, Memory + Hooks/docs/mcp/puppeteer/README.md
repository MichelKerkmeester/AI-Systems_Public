# Puppeteer MCP Documentation

## Overview

Puppeteer MCP provides browser automation through Google's Puppeteer library, offering a simpler alternative to Playwright for Chrome/Chromium-specific automation tasks. It excels at PDF generation, screenshot capture, and Chrome-specific features.

## Key Features

- **Chrome/Chromium Focus**: Optimized for Chrome DevTools Protocol
- **Headless Operation**: Efficient server-side rendering
- **PDF Generation**: High-quality PDF exports
- **Performance Metrics**: Access to Chrome performance data
- **Simple API**: Straightforward automation commands

## Available Tools

### Core Navigation & Interaction

#### `mcp__puppeteer__puppeteer_navigate`
Navigate to a URL with launch options.

**Parameters:**
- `url`: Target URL (required)
- `allowDangerous`: Allow dangerous launch options (default: false)
- `launchOptions`: PuppeteerJS launch options object
  - `headless`: Run without UI
  - `args`: Chrome command line arguments

**Example:**
```python
{
    "url": "https://example.com",
    "launchOptions": {
        "headless": true,
        "args": ["--no-sandbox", "--disable-setuid-sandbox"]
    }
}
```

#### `mcp__puppeteer__puppeteer_click`
Click an element.

**Parameters:**
- `selector`: CSS selector for element

#### `mcp__puppeteer__puppeteer_fill`
Fill an input field.

**Parameters:**
- `selector`: CSS selector for input
- `value`: Text to enter

#### `mcp__puppeteer__puppeteer_select`
Select dropdown option.

**Parameters:**
- `selector`: CSS selector for select element
- `value`: Option value to select

#### `mcp__puppeteer__puppeteer_hover`
Hover over an element.

**Parameters:**
- `selector`: CSS selector for element

### Screenshot Capture

#### `mcp__puppeteer__puppeteer_screenshot`
Capture screenshot with options.

**Parameters:**
- `name`: Screenshot filename (required)
- `selector`: Optional element selector
- `width`: Viewport width (default: 800)
- `height`: Viewport height (default: 600)
- `encoded`: Return base64 data URI (default: false)

**Example:**
```python
{
    "name": "homepage",
    "width": 1920,
    "height": 1080,
    "encoded": true  # Returns base64 string
}
```

### JavaScript Execution

#### `mcp__puppeteer__puppeteer_evaluate`
Execute JavaScript in page context.

**Parameters:**
- `script`: JavaScript code to execute

**Example:**
```python
{
    "script": """
        const prices = Array.from(document.querySelectorAll('.price')).map(el => el.textContent);
        return prices;
    """
}
```

## Puppeteer vs Playwright

### When to Use Puppeteer

1. **Chrome-Specific Features**
   - Need Chrome DevTools Protocol
   - Chrome extension testing
   - Chrome performance profiling

2. **Simple Automation**
   - Basic form filling
   - Screenshot generation
   - PDF exports

3. **Existing Puppeteer Code**
   - Maintaining legacy scripts
   - Team familiarity with Puppeteer

### When to Use Playwright

1. **Cross-Browser Testing**
   - Firefox/Safari support needed
   - Browser compatibility testing

2. **Advanced Features**
   - Network interception
   - Multiple contexts
   - Video recording
   - Mobile emulation

3. **Modern Projects**
   - New test automation
   - Complex workflows

## Common Use Cases

### 1. PDF Generation
```python
# Navigate to document
puppeteer_navigate(url="https://example.com/invoice")

# Wait for content
puppeteer_evaluate(script="document.readyState === 'complete'")

# Generate PDF (via Page.printToPDF in actual implementation)
puppeteer_screenshot(name="invoice", width=800, height=1100)
```

### 2. Form Automation
```python
# Simple form filling
puppeteer_navigate(url="https://forms.example.com")
puppeteer_fill(selector="#name", value="John Doe")
puppeteer_fill(selector="#email", value="john@example.com")
puppeteer_select(selector="#country", value="US")
puppeteer_click(selector="#submit")
```

### 3. Data Extraction
```python
# Extract table data
puppeteer_navigate(url="https://data.example.com")
data = puppeteer_evaluate(script="""
    const rows = document.querySelectorAll('table tr');
    return Array.from(rows).map(row => {
        const cells = row.querySelectorAll('td');
        return Array.from(cells).map(cell => cell.textContent.trim());
    });
""")
```

### 4. Performance Testing
```python
# Measure page load performance
puppeteer_navigate(url="https://example.com")
metrics = puppeteer_evaluate(script="""
    const perfData = window.performance.timing;
    return {
        loadTime: perfData.loadEventEnd - perfData.navigationStart,
        domReady: perfData.domContentLoadedEventEnd - perfData.navigationStart,
        firstPaint: perfData.responseStart - perfData.navigationStart
    };
""")
```

### 5. Screenshot Comparison
```python
# Capture screenshots for visual regression
puppeteer_navigate(url="https://app.example.com/dashboard")
puppeteer_screenshot(
    name="dashboard-baseline",
    width=1920,
    height=1080
)

# After changes
puppeteer_navigate(url="https://app.example.com/dashboard")
puppeteer_screenshot(
    name="dashboard-updated",
    width=1920,
    height=1080
)
```

## Best Practices

### 1. Launch Options
```python
# Development
{
    "headless": false,
    "devtools": true,
    "slowMo": 100  # Slow down for debugging
}

# Production
{
    "headless": true,
    "args": ["--no-sandbox", "--disable-setuid-sandbox"]
}
```

### 2. Wait Strategies
```python
# Wait for specific element
puppeteer_evaluate(script="""
    new Promise(resolve => {
        const checkElement = () => {
            if (document.querySelector('.loaded')) {
                resolve(true);
            } else {
                setTimeout(checkElement, 100);
            }
        };
        checkElement();
    });
""")
```

### 3. Error Handling
```python
# Check element existence
exists = puppeteer_evaluate(
    script="!!document.querySelector('#element')"
)
if exists:
    puppeteer_click("#element")
```

### 4. Memory Management
```python
# Clean up after operations
puppeteer_evaluate(script="""
    // Clear large data structures
    window.largeData = null;
    // Trigger garbage collection if available
    if (window.gc) window.gc();
""")
```

## Troubleshooting

### Launch Failures
- **Sandbox Issues**: Use `--no-sandbox` flag for Docker/CI
- **Missing Dependencies**: Install Chrome/Chromium
- **Permission Errors**: Check file system permissions

### Timeout Errors
- Increase navigation timeout
- Add explicit waits for dynamic content
- Check for JavaScript errors blocking page

### Selector Issues
- Use DevTools to verify selectors
- Account for shadow DOM elements
- Check for dynamically generated content

### Memory Leaks
- Close pages after use
- Limit concurrent operations
- Monitor Chrome process memory

## Chrome-Specific Features

### 1. DevTools Protocol
```python
# Access Chrome DevTools features
puppeteer_evaluate(script="""
    // Get performance metrics
    chrome.loadTimes()
""")
```

### 2. Console Access
```python
# Monitor console output
# Browser console logs accessible via resource
# console://logs
```

### 3. Network Control
```python
# Basic request blocking
puppeteer_evaluate(script="""
    // Override fetch for simple blocking
    const originalFetch = window.fetch;
    window.fetch = (url, ...args) => {
        if (url.includes('analytics')) {
            return Promise.reject('Blocked');
        }
        return originalFetch(url, ...args);
    };
""")
```

## Performance Optimization

### 1. Resource Blocking
```python
# Block images and fonts
launchOptions = {
    "args": [
        "--disable-images",
        "--disable-fonts"
    ]
}
```

### 2. Viewport Optimization
```python
# Use smaller viewport for faster rendering
puppeteer_screenshot(
    name="thumbnail",
    width=400,
    height=300
)
```

### 3. Parallel Operations
```python
# Note: Puppeteer MCP runs single browser instance
# For parallel operations, use multiple tool calls
# or consider Playwright for better concurrency
```

## Integration Examples

### With Testing Frameworks
```python
# Capture test failure screenshots
if test_failed:
    puppeteer_screenshot(
        name=f"failure-{test_name}",
        encoded=true
    )
```

### With CI/CD
```python
# Headless configuration for CI
puppeteer_navigate(
    url="https://staging.example.com",
    launchOptions={
        "headless": true,
        "args": ["--no-sandbox"]
    }
)
```

### With Monitoring
```python
# Regular screenshot captures
puppeteer_navigate(url="https://app.example.com")
puppeteer_screenshot(
    name=f"monitor-{timestamp}",
    fullPage=true
)
```

## Limitations

1. **Chrome/Chromium Only**: No Firefox/Safari support
2. **Single Browser Instance**: Limited concurrency
3. **Basic API**: Fewer features than Playwright
4. **Limited Mobile Emulation**: Basic viewport changes only

## Migration to Playwright

If you need more features, consider migrating:

```python
# Puppeteer
puppeteer_navigate(url="...")
puppeteer_click(selector="...")

# Playwright equivalent
playwright_navigate(url="...", browserType="chromium")
playwright_click(selector="...")
```

## Related Tools
- **Playwright MCP**: Full-featured browser automation
- **Chrome Debug MCP**: Direct Chrome DevTools access
- **WebFetch**: Simple URL content fetching