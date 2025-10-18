# Implementation Patterns Reference

Practical patterns for incremental development, testing, and refactoring.

## TDD (Test-Driven Development)

**When to Use**:
- Complex business logic
- Critical algorithms
- API endpoints
- Data transformations

**Pattern**:
```javascript
// 1. Write failing test
test('calculateTotal sums item prices', () => {
  const items = [{ price: 10 }, { price: 20 }];
  expect(calculateTotal(items)).toBe(30);
});

// 2. Write minimal code to pass
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// 3. Refactor if needed
```

---

## Incremental Development

**Pattern**: Build → Test → Commit

**Example** (Building a form):
```
Iteration 1: Basic form structure
- Create HTML form
- Test: Form renders
- Commit: "feat: add basic form structure"

Iteration 2: Add validation
- Add client-side validation
- Test: Validation works
- Commit: "feat: add form validation"

Iteration 3: Add submission
- Add submit handler
- Test: Submission works
- Commit: "feat: add form submission"
```

---

## Error Handling Patterns

### Try-Catch with Specific Handling

```javascript
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    
    return await response.json();
  } catch (error) {
    if (error.name === 'TypeError') {
      console.error('Network error:', error);
      throw new Error('Unable to connect. Please check your internet connection.');
    }
    
    console.error('Failed to fetch user:', error);
    throw error;
  }
}
```

---

## State Management

### React Hook Pattern

```javascript
function useFormState(initialValues) {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleChange = (field, value) => {
    setValues(prev => ({ ...prev, [field]: value }));
    setErrors(prev => ({ ...prev, [field]: null }));
  };

  const validate = () => {
    const newErrors = {};
    if (!values.email) newErrors.email = 'Email required';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  return { values, errors, isSubmitting, handleChange, validate, setIsSubmitting };
}
```

---

## Refactoring Patterns

### Extract Function

```javascript
// Before
function processOrder(order) {
  const total = order.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const tax = total * 0.08;
  const shipping = total > 50 ? 0 : 10;
  return total + tax + shipping;
}

// After
function calculateSubtotal(items) {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

function calculateTax(subtotal) {
  return subtotal * 0.08;
}

function calculateShipping(subtotal) {
  return subtotal > 50 ? 0 : 10;
}

function processOrder(order) {
  const subtotal = calculateSubtotal(order.items);
  const tax = calculateTax(subtotal);
  const shipping = calculateShipping(subtotal);
  return subtotal + tax + shipping;
}
```

---

## Progressive Enhancement

```javascript
// Basic functionality (works everywhere)
const form = document.querySelector('#contact-form');
form.addEventListener('submit', handleSubmit);

// Enhanced functionality (if available)
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(lazyLoadImages);
  images.forEach(img => observer.observe(img));
}

// Advanced functionality (modern browsers)
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

---

## Feature Flags

```javascript
const features = {
  NEW_CHECKOUT: process.env.FEATURE_NEW_CHECKOUT === 'true',
  DARK_MODE: process.env.FEATURE_DARK_MODE === 'true'
};

function renderCheckout() {
  if (features.NEW_CHECKOUT) {
    return <NewCheckout />;
  }
  return <LegacyCheckout />;
}
```

---

## Component Composition

```javascript
// Atomic components
function Button({ children, onClick, variant = 'primary' }) {
  return (
    <button className={`btn btn-${variant}`} onClick={onClick}>
      {children}
    </button>
  );
}

// Composed component
function SaveButton({ onSave, isSaving }) {
  return (
    <Button onClick={onSave} variant="primary" disabled={isSaving}>
      {isSaving ? 'Saving...' : 'Save'}
    </Button>
  );
}
```

---

## Integration Patterns

### API Client Pattern

```javascript
class APIClient {
  constructor(baseURL) {
    this.baseURL = baseURL;
  }

  async request(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      headers: { 'Content-Type': 'application/json' },
      ...options
    };

    const response = await fetch(url, config);
    
    if (!response.ok) {
      throw new APIError(response.status, response.statusText);
    }

    return response.json();
  }

  get(endpoint) {
    return this.request(endpoint);
  }

  post(endpoint, data) {
    return this.request(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }
}

const api = new APIClient('/api');
const users = await api.get('/users');
```

---

## Testing Strategies

### Unit Testing

```javascript
describe('calculateTotal', () => {
  it('sums item prices', () => {
    const items = [{ price: 10 }, { price: 20 }];
    expect(calculateTotal(items)).toBe(30);
  });

  it('handles empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });

  it('ignores items without price', () => {
    const items = [{ price: 10 }, {}, { price: 20 }];
    expect(calculateTotal(items)).toBe(30);
  });
});
```

### Integration Testing

```javascript
test('form submission creates user', async () => {
  render(<SignupForm />);
  
  fireEvent.change(screen.getByLabelText('Email'), {
    target: { value: 'test@example.com' }
  });
  
  fireEvent.click(screen.getByText('Sign Up'));
  
  await waitFor(() => {
    expect(screen.getByText('Success!')).toBeInTheDocument();
  });
});
```
