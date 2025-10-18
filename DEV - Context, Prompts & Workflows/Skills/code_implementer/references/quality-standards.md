# Quality Standards Reference

Comprehensive standards for code quality, functionality, and testing.

## Code Readability

### Naming Conventions

**Variables**:
```javascript
// ❌ Bad
const d = new Date();
const x = getUserData();

// ✅ Good
const currentDate = new Date();
const userData = getUserData();
```

**Functions**:
```javascript
// ❌ Bad
function proc(data) { }
function x() { }

// ✅ Good
function processUserData(data) { }
function calculateTotalPrice() { }
```

**Boolean Variables**:
```javascript
// ✅ Good - Use is/has/can prefix
const isValid = true;
const hasPermission = false;
const canEdit = true;
```

---

## DRY (Don't Repeat Yourself)

```javascript
// ❌ Bad - Repetition
function validateEmail(email) {
  return email.includes('@') && email.includes('.');
}

function validateUsername(username) {
  return username.length >= 3 && username.length <= 20;
}

function validatePassword(password) {
  return password.length >= 8 && password.length <= 128;
}

// ✅ Good - Extract common logic
function validateLength(value, min, max) {
  return value.length >= min && value.length <= max;
}

function validateEmail(email) {
  return email.includes('@') && email.includes('.');
}

function validateUsername(username) {
  return validateLength(username, 3, 20);
}

function validatePassword(password) {
  return validateLength(password, 8, 128);
}
```

---

## Error Handling

### Input Validation

```javascript
function createUser(data) {
  // Validate required fields
  if (!data.email) {
    throw new ValidationError('Email is required');
  }
  
  if (!data.password) {
    throw new ValidationError('Password is required');
  }
  
  // Validate format
  if (!isValidEmail(data.email)) {
    throw new ValidationError('Invalid email format');
  }
  
  // Continue with creation
  return saveUser(data);
}
```

### Graceful Degradation

```javascript
async function loadUserPreferences(userId) {
  try {
    return await fetch(`/api/preferences/${userId}`).then(r => r.json());
  } catch (error) {
    console.warn('Failed to load preferences, using defaults:', error);
    return getDefaultPreferences();
  }
}
```

---

## Performance Standards

### Acceptable Response Times

- **UI Interactions**: <100ms (feels instant)
- **Page Loads**: <3s (acceptable)
- **API Calls**: <500ms (good)
- **Search**: <200ms (feels responsive)

### Optimization Techniques

```javascript
// Debounce expensive operations
const debouncedSearch = debounce(performSearch, 300);
input.addEventListener('input', debouncedSearch);

// Memoize expensive calculations
const memoizedCalculation = memoize(expensiveFunction);

// Lazy load components
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));
```

---

## Security Standards

### Input Sanitization

```javascript
// Sanitize HTML
function sanitizeHTML(input) {
  const div = document.createElement('div');
  div.textContent = input;
  return div.innerHTML;
}

// Validate and sanitize SQL inputs (use parameterized queries)
const query = 'SELECT * FROM users WHERE id = ?';
db.execute(query, [userId]);  // ✅ Parameterized

// const query = `SELECT * FROM users WHERE id = ${userId}`;  // ❌ SQL injection risk
```

### Secrets Management

```javascript
// ❌ Bad - Hardcoded secret
const API_KEY = 'sk_live_12345...';

// ✅ Good - Environment variable
const API_KEY = process.env.API_KEY;

// ✅ Good - Check if set
if (!API_KEY) {
  throw new Error('API_KEY environment variable not set');
}
```

---

## Testing Standards

### Test Coverage

**Critical Paths**: 100% coverage required
- Authentication/authorization
- Payment processing
- Data validation
- Security-critical code

**Standard Paths**: 80%+ coverage recommended
- Business logic
- API endpoints
- Component rendering

**Low Priority**: 50%+ coverage acceptable
- Simple utilities
- UI formatting
- Static content

### Test Quality

```javascript
// ✅ Good test - Independent, deterministic
test('calculateTotal sums prices correctly', () => {
  const items = [{ price: 10 }, { price: 20 }];
  const result = calculateTotal(items);
  expect(result).toBe(30);
});

// ❌ Bad test - Depends on external state
test('user count increases', () => {
  const before = db.users.count();  // Depends on DB state
  createUser({ email: 'test@example.com' });
  const after = db.users.count();
  expect(after).toBe(before + 1);  // Brittle, depends on DB
});
```

---

## Edge Case Checklist

- [ ] Empty array/object/string
- [ ] Null/undefined values
- [ ] Very large numbers
- [ ] Very long strings
- [ ] Special characters (`, &, <, >, etc.)
- [ ] Concurrent operations
- [ ] Network failures
- [ ] Out-of-memory conditions
- [ ] Browser compatibility (if web)
- [ ] Mobile vs desktop (if responsive)
