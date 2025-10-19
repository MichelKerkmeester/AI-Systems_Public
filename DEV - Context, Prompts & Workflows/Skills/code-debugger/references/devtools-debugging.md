# Chrome DevTools Debugging Reference

Complete guide to debugging with Chrome DevTools.

## Breakpoints

### Line Breakpoints

**Set**:
- Click line number in Sources tab
- Or add `debugger;` statement in code

**Usage**:
```javascript
function calculate_total(items) {
  debugger;  // Execution pauses here
  let total = 0;
  items.forEach(item => {
    total += item.price;
  });
  return total;
}
```

**Controls When Paused**:
- **Resume** (F8): Continue execution
- **Step Over** (F10): Execute line, don't enter functions
- **Step Into** (F11): Enter function call
- **Step Out** (Shift+F11): Exit current function
- **Step** (F9): Step to next line

---

### Conditional Breakpoints

**Set**:
1. Right-click line number
2. Select "Add conditional breakpoint"
3. Enter condition

**Examples**:
```javascript
// Pause only when user_id is 123
user_id === 123

// Pause only when array is empty
items.length === 0

// Pause after 10th iteration
i > 10
```

**Use Case**: Debugging loops - pause on specific iteration

---

### DOM Breakpoints

**Set**:
1. Right-click element in Elements tab
2. "Break on" → Choose type:
   - **Subtree modifications**: Child element changes
   - **Attributes modifications**: Attribute changes
   - **Node removal**: Element is deleted

**Use Case**: Find what code modifies a specific element

**Example Scenario**:
```
Problem: Modal class changes unexpectedly
Solution:
1. Right-click modal element
2. Break on → Attribute modifications
3. Trigger bug
4. DevTools pauses where class is changed
5. See call stack to identify culprit
```

---

### XHR/Fetch Breakpoints

**Set**:
1. Sources tab → XHR/fetch Breakpoints
2. Click + to add
3. Enter URL substring

**Example**:
```
Break when URL contains: /api/users
Pauses on: fetch('/api/users/123')
```

**Use Case**: Debug API call timing or parameters

---

### Event Listener Breakpoints

**Set**:
1. Sources tab → Event Listener Breakpoints
2. Expand category
3. Check event type

**Categories**:
- **Mouse**: click, mousedown, mouseup
- **Keyboard**: keydown, keyup, keypress
- **Touch**: touchstart, touchmove, touchend
- **Control**: resize, scroll, zoom
- **Load**: load, DOMContentLoaded

**Use Case**: Find where event handler is attached

---

## Stepping Through Code

### Step Over (F10)

**Behavior**: Execute current line, move to next (don't enter functions)

**Use**: When you don't care about function internals

**Example**:
```javascript
function main() {
  const data = fetch_data();  // ← Paused here
  // Press F10
  process(data);  // ← Moves here (doesn't enter fetch_data)
}
```

---

### Step Into (F11)

**Behavior**: Enter function call

**Use**: When you want to debug inside function

**Example**:
```javascript
function main() {
  const data = fetch_data();  // ← Paused here, press F11
}

function fetch_data() {  // ← Enters here
  return api.get('/data');
}
```

---

### Step Out (Shift+F11)

**Behavior**: Finish current function, return to caller

**Use**: When you've entered function but want to exit

**Example**:
```javascript
function fetch_data() {
  return api.get('/data');  // ← Accidentally stepped in
  // Press Shift+F11
}

function main() {
  const data = fetch_data();  // ← Returns here
}
```

---

## Watch Expressions

**Add Watch**:
1. Pause at breakpoint
2. Right panel → Watch
3. Click + to add expression

**Examples**:
```javascript
// Watch variable
user.name

// Watch expression
items.length > 0

// Watch function call
calculate_total(items)

// Watch complex expression
items.filter(i => i.price > 100).length
```

**Use Case**: Monitor values as you step through code

---

## Call Stack Analysis

**View**: Right panel → Call Stack (when paused)

**Reading Call Stack**:
```
calculate_total        ← Current function (top)
  ↓
process_cart          ← Called from here
  ↓
handle_checkout       ← Called from here
  ↓
(anonymous)           ← Event handler
```

**Navigation**: Click any frame to see code at that point

**Use Case**: Understand how execution reached current point

---

## Scope Variables

**View**: Right panel → Scope (when paused)

**Sections**:
- **Local**: Variables in current function
- **Closure**: Variables from outer scopes
- **Global**: Global variables

**Modify Variables**:
1. Double-click variable value
2. Enter new value
3. Press Enter
4. Continue execution with new value

**Use Case**: Test fixes without reloading

---

## Console Debugging

### Console Methods

**Basic Logging**:
```javascript
console.log('Message');
console.info('Info message');
console.warn('Warning');
console.error('Error');
```

**Styled Logging**:
```javascript
console.log('%cStyled!', 'color: red; font-size: 20px;');
```

**Object Logging**:
```javascript
const user = { id: 1, name: 'John' };

// Expands object
console.log(user);

// Table format
console.table(user);

// Formatted JSON
console.log(JSON.stringify(user, null, 2));
```

**Conditional Logging**:
```javascript
console.assert(user.age > 18, 'User must be adult');
// Only logs if condition false
```

---

### Console Shortcuts

**$0-$4**: Recently inspected elements
```javascript
$0  // Currently selected element in Elements tab
$1  // Previously selected element
```

**$()**: Alias for querySelector
```javascript
$('.button')  // Same as document.querySelector('.button')
$$('.button')  // Same as document.querySelectorAll('.button')
```

**$x()**: XPath selector
```javascript
$x('//button')  // All button elements via XPath
```

**copy()**: Copy to clipboard
```javascript
copy(object)  // Copies JSON to clipboard
```

---

### console.trace()

**Usage**: Show call stack

```javascript
function c() {
  console.trace('How did we get here?');
}

function b() {
  c();
}

function a() {
  b();
}

a();

// Output:
// How did we get here?
// c @ script.js:2
// b @ script.js:6
// a @ script.js:10
// (anonymous) @ script.js:13
```

---

### console.time()

**Usage**: Measure execution time

```javascript
console.time('data processing');

// ... expensive operation ...

console.timeEnd('data processing');
// Output: data processing: 234.567ms
```

---

## Network Debugging

### Inspect Request

**View**:
1. Network tab
2. Click request
3. See tabs:
   - **Headers**: Request/response headers
   - **Preview**: Formatted response
   - **Response**: Raw response
   - **Timing**: Request timing breakdown

**Headers Analysis**:
```
General:
  Request URL: https://api.example.com/users
  Request Method: GET
  Status Code: 200 OK

Response Headers:
  Content-Type: application/json
  Cache-Control: max-age=3600

Request Headers:
  Authorization: Bearer xyz
```

---

### Request Blocking

**Block Requests**:
1. Network tab → Right-click request
2. "Block request URL"
3. Request will fail

**Use Case**: Test error handling

---

### Throttling

**Simulate Slow Network**:
1. Network tab → Throttling dropdown
2. Select preset:
   - Fast 3G
   - Slow 3G
   - Offline

**Use Case**: Test loading states on slow connections

---

## Sources Panel Features

### Local Overrides

**Setup**:
1. Sources → Overrides
2. Select folder
3. Enable overrides

**Usage**:
1. Edit file in Sources
2. Save (Cmd+S)
3. Changes persist across reloads

**Use Case**: Test fixes without deploying

---

### Snippets

**Create**:
1. Sources → Snippets
2. Right-click → New
3. Write code
4. Run (Cmd+Enter)

**Example Snippet**:
```javascript
// Debug helper
(function() {
  const user = document.querySelector('.user');
  console.log('User element:', user);
  console.log('User data:', user.dataset);
  debugger;
})();
```

**Use Case**: Reusable debugging scripts

---

### Search Across Files

**Search**:
- `Cmd+Shift+F` / `Ctrl+Shift+F`
- Enter search term
- See all occurrences across all files

**Regex Search**:
- Click `.*` button
- Use regex: `function\s+\w+`

**Use Case**: Find where function is called

---

## Debugging Async Code

### Async Stack Traces

**Enable**: Settings → "Capture async stack traces"

**Benefit**: See full chain including async calls

**Example**:
```
Without async traces:
  handler @ file.js:10

With async traces:
  handler @ file.js:10
  async setTimeout
  init @ file.js:5
  onclick @ (index):1
```

---

### Promise Debugging

**See Promise State**:
```javascript
const promise = fetch('/api/data');

// Pause execution
debugger;

// Inspect promise in console
promise  // Shows pending/fulfilled/rejected
```

**Catch Rejection**:
```javascript
// Pause on uncaught exceptions
Settings → "Pause on exceptions"

// Pause on caught exceptions too
Settings → "Pause on caught exceptions"
```

---

## Quick Reference

| Action | Shortcut | Description |
|--------|----------|-------------|
| Open DevTools | `F12` or `Cmd+Option+I` | Open/close DevTools |
| Resume | `F8` or `Cmd+\` | Continue execution |
| Step Over | `F10` | Execute line, skip functions |
| Step Into | `F11` | Enter function call |
| Step Out | `Shift+F11` | Exit current function |
| Search files | `Cmd+P` | Quick file open |
| Search all | `Cmd+Shift+F` | Search across files |
| Command | `Cmd+Shift+P` | Command palette |
| Console | `Cmd+Option+J` | Open Console |

---

## Debugging Workflow

**Standard Flow**:
1. **Reproduce bug** in browser
2. **Check Console** for errors
3. **Set breakpoint** near suspected issue
4. **Trigger bug** to hit breakpoint
5. **Inspect variables** in Scope panel
6. **Step through code** to find issue
7. **Test fix** with Local Overrides
8. **Verify** original issue resolved

**Quick Debug** (1-2 minutes):
- Check Console for errors
- Add `debugger;` statement
- Reload page
- Inspect variables when paused

**Deep Debug** (10-30 minutes):
- Set multiple breakpoints
- Use conditional breakpoints
- Watch key expressions
- Step through execution carefully
- Analyze call stack
- Test edge cases
