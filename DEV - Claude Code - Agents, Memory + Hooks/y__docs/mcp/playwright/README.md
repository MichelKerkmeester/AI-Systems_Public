# Playwright MCP Documentation

## Overview

Playwright MCP provides browser automation capabilities for testing, web scraping, and interaction with web applications. It offers a robust, cross-browser automation solution with advanced features like auto-waiting, network interception, and parallel execution.

## Key Features

- **Cross-Browser Support**: Chromium, Firefox, WebKit
- **Auto-Waiting**: Intelligent wait for elements to be ready
- **Network Control**: Intercept and modify requests/responses
- **Screenshots & PDFs**: Capture visual states
- **Session Recording**: Generate test code from interactions
- **Parallel Execution**: Run multiple browser contexts

## Available Tools

### Session Management

#### `mcp__playwright__start_codegen_session`
Start recording browser interactions to generate test code.

**Parameters:**
- `options`:
  - `outputPath`: Directory for generated tests (absolute path)
  - `includeComments`: Add descriptive comments (boolean)
  - `testNamePrefix`: Prefix for test names (default: "GeneratedTest")

#### `mcp__playwright__end_codegen_session`
Stop recording and generate test file.

**Parameters:**
- `sessionId`: ID of the session to end

### Navigation & Interaction

#### `mcp__playwright__playwright_navigate`
Navigate to a URL with browser configuration.

**Parameters:**
- `url`: Target URL (required)
- `browserType`: "chromium", "firefox", or "webkit" (default: "chromium")
- `headless`: Run without UI (default: false)
- `width`: Viewport width (default: 1280)
- `height`: Viewport height (default: 720)
- `timeout`: Navigation timeout in ms
- `waitUntil`: Navigation wait condition

**Example:**
```python
{
    "url": "https://example.com",
    "browserType": "chromium",
    "headless": false,
    "width": 1920,
    "height": 1080
}
```

#### `mcp__playwright__playwright_click`
Click an element on the page.

**Parameters:**
- `selector`: CSS selector for target element

#### `mcp__playwright__playwright_fill`
Fill out an input field.

**Parameters:**
- `selector`: CSS selector for input
- `value`: Text to enter

#### `mcp__playwright__playwright_select`
Select an option from a dropdown.

**Parameters:**
- `selector`: CSS selector for select element
- `value`: Option value to select

### Screenshots & Visual Capture

#### `mcp__playwright__playwright_screenshot`
Capture page or element screenshot.

**Parameters:**
- `name`: Screenshot filename
- `selector`: Optional CSS selector for specific element
- `fullPage`: Capture entire page (default: false)
- `savePng`: Save as PNG file (default: false)
- `storeBase64`: Store in base64 format (default: true)
- `downloadsDir`: Custom download directory

### Content Extraction

#### `mcp__playwright__playwright_get_visible_text`
Get all visible text content from the page.

**Parameters:** None

#### `mcp__playwright__playwright_get_visible_html`
Get HTML content with filtering options.

**Parameters:**
- `selector`: Limit to specific container
- `removeScripts`: Remove script tags (default: true)
- `removeStyles`: Remove style tags (default: false)
- `removeMeta`: Remove meta tags (default: false)
- `removeComments`: Remove HTML comments (default: false)
- `cleanHtml`: Comprehensive cleaning (default: false)
- `minify`: Minify output (default: false)
- `maxLength`: Character limit (default: 20000)

### Network Operations

#### `mcp__playwright__playwright_expect_response`
Start waiting for a specific HTTP response.

**Parameters:**
- `id`: Unique identifier for this wait operation
- `url`: URL pattern to match

#### `mcp__playwright__playwright_assert_response`
Validate a previously expected response.

**Parameters:**
- `id`: Identifier from expect_response
- `value`: Optional expected response body content

### Advanced Features

#### `mcp__playwright__playwright_evaluate`
Execute JavaScript in the browser context.

**Parameters:**
- `script`: JavaScript code to execute

**Example:**
```python
{
    "script": "document.querySelector('.price').innerText"
}
```

#### `mcp__playwright__playwright_console_logs`
Retrieve browser console logs.

**Parameters:**
- `type`: Log type filter ("all", "error", "warning", etc.)
- `search`: Text to search for in logs
- `limit`: Maximum logs to return
- `clear`: Clear logs after retrieval (default: false)

#### `mcp__playwright__playwright_upload_file`
Upload a file to an input element.

**Parameters:**
- `selector`: File input selector
- `filePath`: Absolute path to file

## Common Use Cases

### 1. Web Testing
```python
# Navigate to application
playwright_navigate(url="https://app.example.com")

# Login flow
playwright_fill(selector="#username", value="testuser")
playwright_fill(selector="#password", value="password123")
playwright_click(selector="#login-button")

# Verify login success
text = playwright_get_visible_text()
assert "Welcome testuser" in text
```

### 2. Form Automation
```python
# Fill complex form
playwright_fill(selector="#name", value="John Doe")
playwright_fill(selector="#email", value="john@example.com")
playwright_select(selector="#country", value="US")
playwright_upload_file(
    selector="#resume", 
    filePath="/path/to/resume.pdf"
)
playwright_click(selector="#submit")
```

### 3. Web Scraping
```python
# Navigate to data source
playwright_navigate(url="https://data.example.com")

# Extract structured data
playwright_evaluate(script="""
    Array.from(document.querySelectorAll('.item')).map(item => ({
        title: item.querySelector('.title').textContent,
        price: item.querySelector('.price').textContent,
        link: item.querySelector('a').href
    }))
""")
```

### 4. Visual Testing
```python
# Capture states for comparison
playwright_navigate(url="https://app.example.com")
playwright_screenshot(name="homepage-desktop", fullPage=true)

# Mobile viewport
playwright_navigate(
    url="https://app.example.com",
    width=375,
    height=667
)
playwright_screenshot(name="homepage-mobile")
```

### 5. API Testing with UI
```python
# Set up response expectation
playwright_expect_response(
    id="api-call",
    url="*/api/users"
)

# Trigger API call via UI
playwright_click(selector="#load-users")

# Validate response
playwright_assert_response(
    id="api-call",
    value='{"users": []}'
)
```

## Best Practices

### 1. Use Auto-Waiting
Playwright automatically waits for elements to be ready:
```python
# ❌ Don't add manual waits
time.sleep(2)
playwright_click("#button")

# ✅ Let Playwright handle timing
playwright_click("#button")  # Auto-waits for clickability
```

### 2. Robust Selectors
```python
# ❌ Fragile selectors
playwright_click("div > span:nth-child(3)")

# ✅ Semantic selectors
playwright_click("[data-testid='submit-button']")
playwright_click("button:has-text('Submit')")
```

### 3. Error Handling
```python
# Check element existence before interaction
exists = playwright_evaluate(
    script="!!document.querySelector('#optional-element')"
)
if exists:
    playwright_click("#optional-element")
```

### 4. Network Efficiency
```python
# Block unnecessary resources
playwright_navigate(
    url="https://example.com",
    # Configure via browser context for blocking images, fonts, etc.
)
```

## Troubleshooting

### Element Not Found
- Verify selector specificity
- Check if element is in iframe (use `playwright_iframe_click`)
- Ensure page is fully loaded
- Look for dynamic content loading

### Timeout Issues
- Increase timeout for slow pages
- Check network conditions
- Verify element visibility
- Use more specific wait conditions

### Console Errors
- Check `playwright_console_logs(type="error")`
- Look for JavaScript errors blocking functionality
- Verify all resources loaded successfully

## Advanced Patterns

### Iframe Handling
```python
# Click element inside iframe
playwright_iframe_click(
    iframeSelector="#payment-iframe",
    selector="#card-number"
)

# Fill iframe form field
playwright_iframe_fill(
    iframeSelector="#payment-iframe",
    selector="#card-number",
    value="4111111111111111"
)
```

### Multi-Tab Workflows
```python
# Click link that opens new tab
playwright_click_and_switch_tab(selector="a[target='_blank']")

# Continue automation in new tab
playwright_fill(selector="#form-field", value="data")
```

### Session Recording
```python
# Start recording user interactions
session = playwright_start_codegen_session(options={
    "outputPath": "/path/to/tests",
    "includeComments": true
})

# Perform interactions...
playwright_navigate(url="https://example.com")
playwright_click("#button")

# Generate test code
playwright_end_codegen_session(sessionId=session.id)
```

## Performance Tips

1. **Reuse Browser Context**: Keep browser open for multiple operations
2. **Parallel Execution**: Run independent tests concurrently
3. **Headless Mode**: Use for CI/CD and faster execution
4. **Resource Blocking**: Disable images/fonts when not needed
5. **Smart Waiting**: Use Playwright's built-in wait strategies

## Related Tools
- **Puppeteer MCP**: Alternative browser automation
- **Chrome Debug MCP**: Direct Chrome DevTools access