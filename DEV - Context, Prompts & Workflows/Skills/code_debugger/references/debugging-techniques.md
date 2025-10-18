# Advanced Debugging Techniques

Systematic approaches to finding and fixing complex bugs.

## Binary Search Debugging

**When to Use**: Large codebase, unsure where bug occurs

**Method**:
1. Identify working and broken states
2. Comment out half the code
3. Test - does bug still occur?
4. If yes: bug is in remaining half
5. If no: bug is in commented half
6. Repeat until isolated

**Example**:
```javascript
// Step 1: Full code (bug present)
function process() {
  step1();  // 100 lines
  step2();  // 100 lines
  step3();  // 100 lines (bug here)
  step4();  // 100 lines
}

// Step 2: Comment half
function process() {
  step1();
  step2();
  // step3();  ← Bug still occurs? No
  // step4();  ← Bug is in second half
}

// Step 3: Narrow down
function process() {
  // step1();
  // step2();
  step3();  // Bug still occurs? Yes - bug is here
  // step4();
}

// Step 4: Binary search within step3
```

**Tips**:
- Keep tests quick
- Document working/broken states
- Use version control to manage changes

---

## Hypothesis Testing Framework

**Process**:
1. Generate hypotheses based on symptoms
2. Design test for each hypothesis
3. Execute tests systematically
4. Eliminate false hypotheses
5. Confirm root cause

**Template**:
```markdown
## Hypothesis 1: API returns wrong data

**Evidence Supporting**:
- Error occurs after API call
- Works with mock data

**Test**: Log API response
```javascript
const response = await fetch('/api/data');
const data = await response.json();
console.log('API response:', data);
```

**Result**: ✓ Confirmed - API returns null instead of object
**Root Cause**: Backend returns null for new users
```

**Example Workflow**:
```
Bug: Modal doesn't close on click

Hypothesis 1: Event listener not attached
├─ Test: console.log in handler → Handler fires ✓
├─ Result: ✗ Rejected

Hypothesis 2: Close function has error
├─ Test: Call close() directly → Works ✓
├─ Result: ✗ Rejected

Hypothesis 3: Event target is wrong element
├─ Test: console.log(e.target) → Shows overlay, not modal ✓
├─ Result: ✓ CONFIRMED
└─ Fix: Check if target is overlay, not modal itself
```

---

## Git Bisect for Regressions

**When to Use**: Bug appeared recently, many commits

**Process**:
```bash
# Start bisect
git bisect start

# Mark current as bad
git bisect bad

# Mark last known good commit
git bisect good abc123

# Git checks out middle commit
# Test if bug exists
npm test

# If bug exists
git bisect bad

# If bug doesn't exist
git bisect good

# Repeat until Git identifies first bad commit
# Git shows: "abc123 is the first bad commit"

# End bisect
git bisect reset
```

**Automated Bisect**:
```bash
git bisect start HEAD abc123
git bisect run npm test
```

---

## Root Cause Analysis

### 5 Whys Technique

**Method**: Ask "why" 5 times to find root cause

**Example**:
```
Bug: Form submission fails

Why? → API returns 500 error
Why? → Validation fails on server
Why? → Email field is empty
Why? → Client doesn't send email field
Why? → Form doesn't have email input
Root Cause: Missing email field in form
```

### Causal Chain Analysis

**Method**: Map full causal chain

**Example**:
```
User clicks submit
  ↓
JavaScript validates form
  ↓
Email field missing → FAILS
  ↓
Shows generic error
  ↓
User confused (doesn't know what's wrong)

Root causes:
1. Missing email field (primary)
2. Generic error message (secondary)
```

---

## Logging Strategies

### Strategic Log Placement

**Key Decision Points**:
```javascript
function process_payment(amount, card) {
  console.log('[Payment] START:', { amount, card_last4: card.slice(-4) });

  if (amount <= 0) {
    console.error('[Payment] Invalid amount:', amount);
    return null;
  }

  console.log('[Payment] Validating card...');
  const is_valid = validate_card(card);
  console.log('[Payment] Card valid:', is_valid);

  if (!is_valid) {
    console.error('[Payment] Card validation failed');
    return null;
  }

  console.log('[Payment] Charging card...');
  const result = charge(amount, card);
  console.log('[Payment] Result:', result);

  console.log('[Payment] END: Success');
  return result;
}
```

### Structured Logging

```javascript
const logger = {
  debug: (msg, data) => console.log(`[DEBUG] ${msg}`, data),
  info: (msg, data) => console.log(`[INFO] ${msg}`, data),
  warn: (msg, data) => console.warn(`[WARN] ${msg}`, data),
  error: (msg, data) => console.error(`[ERROR] ${msg}`, data)
};

// Usage
logger.info('User login', { user_id: 123, timestamp: Date.now() });
logger.error('Payment failed', { error: e.message, amount });
```

### Conditional Logging

```javascript
const DEBUG = true;  // Toggle debug mode

function debug_log(...args) {
  if (DEBUG) {
    console.log('[DEBUG]', ...args);
  }
}

// Only logs in debug mode
debug_log('Processing item:', item);
```

---

## Rubber Duck Debugging

**Method**: Explain code line-by-line to rubber duck (or colleague)

**Process**:
1. Start at entry point
2. Explain each line's purpose
3. Explain expected vs. actual behavior
4. Often realize mistake while explaining

**Example Script**:
```
"This function is supposed to calculate total price.
It takes an array of items.
First, it initializes total to 0.
Then it loops through items...
Wait, I'm using forEach but not accumulating the sum!
That's the bug - I need to add each item to total."
```

**Why It Works**:
- Forces slow, careful reading
- Makes assumptions explicit
- Catches logic errors

---

## Time-Travel Debugging

**Using Browser DevTools**:
1. Set breakpoint
2. Execute code
3. Pause at breakpoint
4. Use **Step Over/Into/Out** to control execution
5. Inspect variables at each step
6. Rewind using **Call Stack**

**React DevTools Time Travel**:
1. Record component state changes
2. Scrub through timeline
3. See component state at each point
4. Identify when state becomes incorrect

**Redux DevTools**:
```javascript
// Enable Redux DevTools
const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

// Time travel in browser:
// - See all dispatched actions
// - Jump to any previous state
// - Identify which action caused bug
```

---

## Divide and Conquer

**Method**: Isolate problem by removing dependencies

**Example**:
```javascript
// Original complex code
function buggy_feature() {
  const data = fetch_data();
  const processed = complex_processing(data);
  const result = another_function(processed);
  return result;  // Bug somewhere here
}

// Step 1: Isolate with known good data
function test_with_mock() {
  const mock_data = { /* known good data */ };
  const result = buggy_feature_with_data(mock_data);
  // Works? → Bug is in fetch_data()
  // Fails? → Bug is in processing
}

// Step 2: Test each function independently
test(complex_processing({ /* input */ }));  // Works?
test(another_function({ /* input */ }));    // Works?

// Step 3: Found problematic function, dig deeper
```

---

## Checklist-Driven Debugging

**Systematic Checklist**:

```markdown
## Bug Investigation Checklist

### 1. Understand the Bug
- [ ] Read error message completely
- [ ] Note exact line number
- [ ] Understand expected behavior
- [ ] Understand actual behavior

### 2. Reproduce
- [ ] Can reproduce on demand?
- [ ] Minimal reproduction steps documented
- [ ] Works in some conditions?
- [ ] Fails consistently or intermittently?

### 3. Gather Evidence
- [ ] Console errors/warnings
- [ ] Network requests (check Network tab)
- [ ] Variable values at failure point
- [ ] Stack trace captured

### 4. Form Hypotheses
- [ ] List 3-5 possible causes
- [ ] Rank by likelihood
- [ ] Design test for each

### 5. Test Systematically
- [ ] Test hypothesis #1
- [ ] Document result
- [ ] Move to next if rejected
- [ ] Stop when confirmed

### 6. Verify Fix
- [ ] Fix applied
- [ ] Original bug resolved
- [ ] No regressions introduced
- [ ] Edge cases tested
```

---

## Quick Reference

| Technique | Best For | Time | Difficulty |
|-----------|----------|------|------------|
| Binary Search | Large codebase | Medium | Easy |
| Hypothesis Testing | Complex bugs | Medium | Medium |
| Git Bisect | Recent regressions | Fast | Easy |
| 5 Whys | Root cause | Fast | Easy |
| Logging | Unknown bugs | Slow | Easy |
| Rubber Duck | Logic errors | Fast | Easy |
| Time Travel | State bugs | Fast | Medium |
| Divide & Conquer | Integration bugs | Medium | Medium |
| Checklist | All bugs | N/A | Easy |
