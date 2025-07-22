# Superdesign Canvas Integration Test Plan

## Test Objectives
Verify canvas viewer functionality while ensuring no regression in existing viteflow components.

## Test Categories

### 1. Component Isolation Tests
**Purpose**: Ensure new canvas components don't break existing ones

#### Tests:
- [ ] All existing viteflow components still initialize
- [ ] stateModal continues to function independently
- [ ] No global namespace conflicts
- [ ] GSAP animations don't interfere

#### Verification:
```bash
npm test -- --testPathPattern=viteflow/components
```

### 2. Canvas Viewer Tests

#### 2.1 Initialization
- [ ] Canvas viewer renders on route `/canvas`
- [ ] Data attributes properly assigned
- [ ] WebSocket connection established
- [ ] Initial empty state displays correctly

#### 2.2 File Watching
- [ ] Detects new files in `.claude-designs/`
- [ ] Updates canvas on file changes
- [ ] Handles file deletions gracefully
- [ ] Processes metadata.json updates

#### 2.3 Canvas Interactions
- [ ] Pan functionality (mouse drag)
- [ ] Zoom controls (+/- buttons, scroll)
- [ ] Grid/hierarchy layout toggle
- [ ] Frame selection highlights
- [ ] Responsive viewport switching

### 3. Integration Tests

#### 3.1 CLI Launch Flow
```bash
# Test sequence
1. Run: claude-code canvas
2. Verify: Server starts on specified port
3. Verify: Browser opens to canvas URL
4. Verify: WebSocket connects
```

#### 3.2 Design Generation Flow
1. Generate test design via Claude Code
2. Verify file appears in `.claude-designs/`
3. Confirm canvas updates within 500ms
4. Check frame renders correctly

#### 3.3 Performance Tests
- [ ] Load 50 design frames
- [ ] Measure pan/zoom FPS (target: 60fps)
- [ ] Test memory usage over time
- [ ] Verify lazy loading works

### 4. Browser Compatibility

#### Browsers to Test:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

#### Features per Browser:
- [ ] Canvas rendering
- [ ] WebSocket connection
- [ ] GSAP animations
- [ ] File watching updates

### 5. Error Handling Tests

#### 5.1 File System Errors
- [ ] Missing `.claude-designs/` directory
- [ ] Corrupted HTML files
- [ ] Invalid metadata.json
- [ ] File permission issues

#### 5.2 Network Errors
- [ ] WebSocket disconnection
- [ ] Server restart recovery
- [ ] Port conflicts
- [ ] Timeout handling

### 6. Security Tests

#### 6.1 Sandbox Verification
- [ ] Generated designs can't access parent frame
- [ ] No script execution from designs
- [ ] CSP headers properly set
- [ ] No file system access from browser

#### 6.2 Input Validation
- [ ] Malformed design files handled
- [ ] XSS prevention in metadata
- [ ] Path traversal prevention
- [ ] Safe iframe src handling

## Test Data

### Sample Design Files
```html
<!-- .claude-designs/iterations/test_001.html -->
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../assets/styles.css">
</head>
<body>
  <div class="test-design">
    <h1>Test Design 001</h1>
    <button>Test Button</button>
  </div>
</body>
</html>
```

### Metadata Structure
```json
{
  "designs": [
    {
      "id": "test_001",
      "name": "Test Design 001",
      "created": "2024-01-20T10:00:00Z",
      "parent": null,
      "viewport": "desktop"
    }
  ]
}
```

## Automated Test Suite

### Setup
```bash
# Install test dependencies
npm install --save-dev @playwright/test

# Run canvas tests
npm run test:canvas
```

### Key Test Files
```
tests/
├── canvas/
│   ├── viewer.spec.js
│   ├── interactions.spec.js
│   ├── file-watching.spec.js
│   └── integration.spec.js
└── regression/
    └── existing-components.spec.js
```

## Manual Test Checklist

### Pre-Implementation
- [ ] Document current component behavior
- [ ] Capture performance baseline
- [ ] Note existing console errors

### Post-Implementation
- [ ] Compare component behavior
- [ ] Verify no new console errors
- [ ] Check performance metrics
- [ ] Validate build size increase < 50KB

## Success Criteria
1. All existing tests pass (100%)
2. New canvas tests pass (100%)
3. No performance regression
4. Browser compatibility verified
5. Security tests pass
6. Error handling works as designed

## Test Schedule
1. **Unit Tests**: During development
2. **Integration Tests**: After feature complete
3. **Browser Tests**: Before deployment
4. **Performance Tests**: Final validation
5. **Security Tests**: Pre-release