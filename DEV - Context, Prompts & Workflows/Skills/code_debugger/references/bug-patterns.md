# Common Bug Patterns Catalog

Comprehensive catalog of frequent bug patterns with diagnosis and fix strategies.

## Null/Undefined Errors

### Pattern 1: Accessing Property of Null/Undefined

**Error Message**:
```
TypeError: Cannot read property 'X' of null
TypeError: Cannot read property 'X' of undefined
```

**Common Causes**:
- DOM element not found
- API response missing expected field
- Object not initialized
- Async timing issue

**Example**:
```javascript
// ❌ Bug
const modal = document.querySelector('.modal');
modal.close();  // Error if modal doesn't exist
```

**Diagnosis**:
1. Check console for line number
2. Add breakpoint before error line
3. Inspect variable value in debugger
4. Verify selector or API response structure

**Fixes**:
```javascript
// ✅ Fix 1: Null check
const modal = document.querySelector('.modal');
if (modal) {
  modal.close();
}

// ✅ Fix 2: Optional chaining
modal?.close();

// ✅ Fix 3: Default value
const user_name = user?.name || 'Anonymous';
```

---

### Pattern 2: Undefined Function Call

**Error Message**:
```
TypeError: X is not a function
```

**Common Causes**:
- Typo in function name
- Function not defined yet (order of execution)
- Overwriting function with value
- Wrong context/this binding

**Example**:
```javascript
// ❌ Bug
myObject.doSomething();  // Error if doSomething doesn't exist
```

**Diagnosis**:
1. Check object in console
2. Verify function exists: `console.log(typeof myObject.doSomething)`
3. Check for typos
4. Verify script load order

**Fixes**:
```javascript
// ✅ Fix: Check function exists
if (typeof myObject.doSomething === 'function') {
  myObject.doSomething();
}
```

---

## Race Conditions

### Pattern 3: Async Data Not Ready

**Symptom**: Works sometimes, fails other times

**Common Scenarios**:
- Accessing data before fetch completes
- DOM manipulation before elements render
- Event fired before listener attached

**Example**:
```javascript
// ❌ Bug
fetch('/api/data');
const result = use_data();  // Data not ready yet
```

**Diagnosis**:
1. Add console.logs with timestamps
2. Check Network tab timing
3. Use breakpoints to verify order
4. Add delays to test theory

**Fixes**:
```javascript
// ✅ Fix 1: Use await
const data = await fetch('/api/data').then(r => r.json());
const result = use_data(data);

// ✅ Fix 2: Promise chain
fetch('/api/data')
  .then(r => r.json())
  .then(data => use_data(data));

// ✅ Fix 3: Event-based
document.addEventListener('data-ready', () => {
  use_data();
});
```

---

### Pattern 4: Stale Closure

**Symptom**: Function uses old variable value

**Example**:
```javascript
// ❌ Bug
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Outputs: 3, 3, 3 (expected: 0, 1, 2)
```

**Diagnosis**:
1. Check variable scope
2. Verify closure captures
3. Test with debugger

**Fixes**:
```javascript
// ✅ Fix 1: Use let
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}

// ✅ Fix 2: IIFE
for (var i = 0; i < 3; i++) {
  (function(i) {
    setTimeout(() => console.log(i), 100);
  })(i);
}

// ✅ Fix 3: Bind
for (var i = 0; i < 3; i++) {
  setTimeout(console.log.bind(null, i), 100);
}
```

---

## Memory Leaks

### Pattern 5: Event Listener Not Removed

**Symptom**: Memory grows over time, performance degrades

**Example**:
```javascript
// ❌ Bug
class Component {
  mount() {
    window.addEventListener('resize', this.handle_resize);
  }
  // Missing cleanup
}
```

**Diagnosis**:
1. Take heap snapshots
2. Look for growing DOM nodes
3. Check detached DOM elements
4. Review event listener count

**Fixes**:
```javascript
// ✅ Fix
class Component {
  mount() {
    this.handle_resize = this.handle_resize.bind(this);
    window.addEventListener('resize', this.handle_resize);
  }

  unmount() {
    window.removeEventListener('resize', this.handle_resize);
  }

  handle_resize() {
    // Handler
  }
}
```

---

### Pattern 6: Timer Not Cleared

**Symptom**: Code continues running after component destroyed

**Example**:
```javascript
// ❌ Bug
class Component {
  start_polling() {
    setInterval(() => {
      fetch('/api/status');
    }, 1000);
  }
}
```

**Fixes**:
```javascript
// ✅ Fix
class Component {
  start_polling() {
    this.poll_interval = setInterval(() => {
      fetch('/api/status');
    }, 1000);
  }

  stop_polling() {
    clearInterval(this.poll_interval);
  }
}
```

---

## State Management Bugs

### Pattern 7: Direct State Mutation

**Symptom**: UI doesn't update, or updates unexpectedly

**Example**:
```javascript
// ❌ Bug (React)
this.state.items.push(new_item);  // Direct mutation
```

**Diagnosis**:
1. Check if state updated but UI didn't
2. Look for direct mutations
3. Verify immutable updates

**Fixes**:
```javascript
// ✅ Fix: Immutable update
this.setState({
  items: [...this.state.items, new_item]
});

// Or using state updater function
this.setState(prevState => ({
  items: [...prevState.items, new_item]
}));
```

---

### Pattern 8: Async State Updates

**Symptom**: State shows old value immediately after update

**Example**:
```javascript
// ❌ Bug
this.setState({ count: 5 });
console.log(this.state.count);  // Still shows old value
```

**Diagnosis**:
1. Verify setState is async
2. Check timing of state usage
3. Use callback if needed

**Fixes**:
```javascript
// ✅ Fix: Use callback
this.setState({ count: 5 }, () => {
  console.log(this.state.count);  // Shows updated value
});

// Or useEffect (React Hooks)
useEffect(() => {
  console.log(count);  // Runs after state updates
}, [count]);
```

---

## DOM Manipulation Bugs

### Pattern 9: Selecting Wrong Element

**Symptom**: Changes apply to wrong element or nothing happens

**Example**:
```javascript
// ❌ Bug
document.querySelector('.button').addEventListener('click', handler);
// Only adds listener to first button
```

**Diagnosis**:
1. Log selected elements
2. Use DevTools Elements tab
3. Check selector specificity
4. Verify unique identifiers

**Fixes**:
```javascript
// ✅ Fix 1: Select all elements
document.querySelectorAll('.button').forEach(button => {
  button.addEventListener('click', handler);
});

// ✅ Fix 2: Event delegation
document.addEventListener('click', (e) => {
  if (e.target.matches('.button')) {
    handler(e);
  }
});

// ✅ Fix 3: Unique selector
document.querySelector('#submit-button').addEventListener('click', handler);
```

---

### Pattern 10: Timing - Element Doesn't Exist Yet

**Symptom**: Script runs but elements not found

**Example**:
```javascript
// ❌ Bug (script in <head>)
const button = document.querySelector('#submit');
button.addEventListener('click', handler);  // button is null
```

**Diagnosis**:
1. Check script location in HTML
2. Verify DOM ready
3. Check element creation timing

**Fixes**:
```javascript
// ✅ Fix 1: DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#submit');
  button.addEventListener('click', handler);
});

// ✅ Fix 2: Move script to end of body
<body>
  <!-- content -->
  <script src="app.js"></script>
</body>

// ✅ Fix 3: defer attribute
<script defer src="app.js"></script>
```

---

## Network/API Bugs

### Pattern 11: CORS Error

**Error Message**:
```
Access to fetch at 'X' from origin 'Y' has been blocked by CORS policy
```

**Diagnosis**:
1. Check Network tab for failed request
2. Verify Access-Control-Allow-Origin header
3. Check request method (OPTIONS preflight)

**Fixes**:
```javascript
// Server-side fix (Express)
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Content-Type');
  next();
});

// Or use cors package
const cors = require('cors');
app.use(cors());
```

---

### Pattern 12: Failed to Parse JSON

**Error Message**:
```
SyntaxError: Unexpected token < in JSON at position 0
```

**Cause**: Server returned HTML error page instead of JSON

**Diagnosis**:
1. Check Network tab response
2. Look at actual response content
3. Check HTTP status code

**Fixes**:
```javascript
// ✅ Fix: Check content type
const response = await fetch('/api/data');

if (!response.ok) {
  throw new Error(`HTTP error: ${response.status}`);
}

const content_type = response.headers.get('content-type');
if (content_type && content_type.includes('application/json')) {
  const data = await response.json();
} else {
  const text = await response.text();
  console.error('Non-JSON response:', text);
}
```

---

## Animation/Timing Bugs

### Pattern 13: Animation Jank

**Symptom**: Choppy, stuttering animations

**Causes**:
- Layout thrashing
- Not using requestAnimationFrame
- Heavy JavaScript during animation
- Animating non-compositor properties

**Diagnosis**:
1. Record Performance profile
2. Check FPS meter
3. Look for layout/paint during animation
4. Review animated properties

**Fixes**:
```javascript
// ❌ Bug
setInterval(() => {
  element.style.left = position + 'px';  // Causes layout
  position += 1;
}, 16);

// ✅ Fix 1: Use transform (GPU-accelerated)
function animate() {
  element.style.transform = `translateX(${position}px)`;
  position += 1;
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);

// ✅ Fix 2: CSS animation
@keyframes slide {
  from { transform: translateX(0); }
  to { transform: translateX(100px); }
}

element.style.animation = 'slide 1s ease';
```

---

## Quick Diagnosis Checklist

When debugging, systematically check:

1. **Error Message**
   - [ ] Read full error message
   - [ ] Note line number and file
   - [ ] Check stack trace

2. **Reproduction**
   - [ ] Can reproduce reliably?
   - [ ] What triggers the bug?
   - [ ] Does it happen in all browsers?

3. **Recent Changes**
   - [ ] What changed recently?
   - [ ] Git blame suspicious lines
   - [ ] Review recent commits

4. **Console Inspection**
   - [ ] Any console errors?
   - [ ] Any warnings?
   - [ ] Network failures?

5. **Variable State**
   - [ ] Add console.logs
   - [ ] Use debugger breakpoints
   - [ ] Inspect variables at failure point

6. **Timing**
   - [ ] Is this a race condition?
   - [ ] Async operation?
   - [ ] Event order issue?

7. **Environment**
   - [ ] Browser-specific?
   - [ ] Device-specific?
   - [ ] Network-dependent?

## Bug Pattern Priority Matrix

| Pattern | Frequency | Severity | Detection Difficulty |
|---------|-----------|----------|---------------------|
| Null/undefined | Very High | High | Easy |
| Race conditions | High | High | Hard |
| Memory leaks | Medium | High | Medium |
| State mutations | High | Medium | Medium |
| DOM timing | High | Low | Easy |
| CORS errors | Medium | Medium | Easy |
| Animation jank | Medium | Low | Easy |
| JSON parsing | Medium | Medium | Easy |
| Event listeners | High | Medium | Medium |
| Stale closures | Medium | Medium | Hard |
