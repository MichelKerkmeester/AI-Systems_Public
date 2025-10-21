---
name: code-debugger
description: Systematically reproduce, diagnose, fix, and verify bugs through evidence-based investigation and root cause analysis. Use when investigating unexpected behavior, runtime errors, visual glitches, or functionality issues. Reproduces bugs reliably, identifies root causes with evidence, implements minimal fixes, and verifies complete resolution without regressions
---

# Code Debugger
Systematic Bug Investigation & Resolution

> Change Notes (2025-10-21)
- Replaced local References with Embedded Reference quick catalogs
- Normalized workflow headings (whole steps only)
- Added YAML → Steps Crosswalk; header-only emoji policy enforced

## 1. 🎯 When to Use

**Use this skill when**:
- Bug reports from users or QA
- Unexpected behavior or functionality issues
- Runtime errors or exceptions
- Visual glitches or layout problems
- Features not working as expected
- Intermittent or hard-to-reproduce issues
- Performance degradation (when cause is unknown)
- Need to investigate and fix problems systematically

**Do NOT use this skill for**:
- Adding new features (use development workflow instead)
- Performance optimization (use performance-improver skill instead)
- Code refactoring without a bug
- Preventive code quality improvements (use code-pattern-validator)
- Design changes or enhancements

## 2. 🛠️ How It Works

This skill follows a 4-step systematic debugging workflow:

1. **Reproduce** - Confirm the issue exists and can be triggered reliably
2. **Diagnose** - Find the root cause through evidence-based investigation
3. **Fix** - Implement minimal solution that addresses root cause
4. **Verify** - Ensure fix works completely without introducing regressions

**Core Principle**: "Fix the root cause, not the symptom"

**Approach**: Systematic elimination with evidence at every step

## 3. 📊 Inputs

### 3.1 Required Inputs

**Request**:
- **Description**: Bug to investigate and fix
- **Format**: Natural language description
- **Examples**:
  - "Modal doesn't close when clicking outside"
  - "Form submission fails with 500 error"
  - "Animation is choppy on mobile"
  - "Memory leak after navigation"

### 3.2 Optional Inputs

**Environment** (staging link):
- **Type**: URL
- **Purpose**: Live environment for reproducing and testing
- **Default**: If empty, skip browser testing steps
- **Example**: `https://staging.example.com`

**Scope** (files):
- **Type**: File path(s) or glob pattern
- **Purpose**: Which files are suspected to contain the bug
- **Default**: All relevant files if empty
- **Examples**:
  - `src/modal/*.js`
  - `src/contact/form_submit.js`

**Target Folder**:
- **Type**: Directory path
- **Purpose**: Often points to issue document or bug report folder
- **Default**: Inferred from issues or request
- **Example**: `specs/007-modal-bug-fix/`

**Context**:
- **Type**: Text
- **Purpose**: Additional context about when/how bug occurs
- **Default**: Inferred from issue description and environment
- **Example**: "Only happens on Safari, after form submission"

**Issues**:
- **Type**: Text
- **Purpose**: Detailed bug description, error messages, steps to reproduce
- **Default**: Parsed from request if available
- **Example**: "TypeError: Cannot read property 'close' of null at modal.js:42"

## YAML → Steps Crosswalk

- Source: b_prompts/code/code_debugger.yaml
- Mapping:
  - Step 1 → Gather User Inputs
  - Step 2 → Reproduce
  - Step 3 → Diagnose
  - Step 4 → Fix
  - Step 5 → Verify

## 4. 🚀 Workflow

### Step 1: Gather User Inputs

**Purpose**: Collect all necessary information before starting debugging

**IMPORTANT**: Before starting the debugging workflow, ask the user for the following inputs in a conversational way:

#### Required Inputs:

1. **Request/Bug Description** (REQUIRED):
   - Ask: "What bug would you like me to investigate and fix? Please describe the issue you're experiencing."
   - This is the main bug description that drives the debugging workflow.

#### Optional Inputs (with smart defaults):

2. **Issues/Details**:
   - Ask: "Can you provide detailed information about the bug? (Include error messages, reproduction steps, or leave empty to parse from your request)"
   - Default: Parse from request if available

3. **Environment/Staging Link**:
   - Ask: "Do you have a staging environment URL where I can reproduce the bug? (Leave empty to skip browser testing)"
   - Default: Skip DevTools/browser testing if not provided

4. **Scope/Files**:
   - Ask: "Which files are suspected to contain the bug? (Leave empty to search all relevant files)"
   - Default: All relevant files

5. **Target Folder**:
   - Ask: "Is there a specific folder for bug documentation? (Leave empty to infer from your request)"
   - Default: Infer from issues or request

6. **Context**:
   - Ask: "Any additional context about when/how the bug occurs? (Leave empty to infer from issue description)"
   - Default: Infer from issue description and environment

**After Collecting Inputs**:
- Confirm all inputs with the user
- Parse and categorize the bug information
- Identify likely affected areas

### Step 2: Reproduce

**Purpose**: Confirm the issue exists and can be triggered reliably

**Actions**:
1. Review target folder for issue documentation
2. Parse issues from Issues field
3. Follow reproduction steps from Request field
4. Document actual behavior vs. expected behavior
5. Capture error messages and stack traces
6. Take screenshots for visual issues
7. Note environment details (browser, device, network)

**Reproduction Checklist**:
- [ ] Understand expected behavior
- [ ] Perform steps to trigger bug
- [ ] Observe actual behavior
- [ ] Capture error messages/logs
- [ ] Document conditions (when it happens, when it doesn't)
- [ ] Can reproduce reliably (>80% success rate)

**Chrome DevTools** (for browser issues):
- **Console**: Check for JavaScript errors
- **Network**: Check for failed requests or timeouts
- **Elements**: Inspect DOM state when bug occurs
- **Sources**: Set breakpoints to pause execution
- **Performance**: Profile if performance-related

**Evidence Collection**:
- Error messages and stack traces
- Console logs
- Network request/response data
- Screenshots or screen recordings
- DOM state snapshots
- Variable values at failure point

**Documentation**:
```markdown
## Bug Reproduction

**Expected Behavior**: [What should happen]
**Actual Behavior**: [What actually happens]

**Steps to Reproduce**:
1. [Step 1]
2. [Step 2]
3. [Bug occurs]

**Environment**:
- Browser: [Chrome 118, Safari 17, etc.]
- Device: [Desktop, iPhone 14, etc.]
- Network: [Fast 3G, WiFi, etc.]

**Evidence**:
- Error: [Error message and stack trace]
- Screenshot: [Link or embedded image]
```

**Validation**: `can_reliably_reproduce_issue`

### Step 3: Diagnose

**Purpose**: Find the root cause through systematic investigation

**Investigation Process**:
1. Generate hypotheses based on evidence
2. Test each hypothesis systematically
3. Gather supporting or contradicting evidence
4. Eliminate false leads
5. Identify root cause with confidence

**Diagnostic Techniques**:

**Binary Search for Complexity**:
- Comment out half the code
- Determine which half contains the bug
- Repeat until isolated

**Git Bisect for Regressions**:
- Identify when bug was introduced
- Use `git bisect` to find commit
- Review changes in that commit

**Console Debugging**:
- Add console.log at key points
- Track variable values through execution
- Identify where values become incorrect

**Network Analysis**:
- Inspect request/response in DevTools
- Check status codes and error responses
- Verify request payload and headers

**Code Inspection**:
- Read code carefully around error location
- Check for logic errors, off-by-one, null handling
- Review recent changes (git blame)

**Hypothesis Testing Framework**:

```markdown
## Hypothesis 1: [Description]
**Supporting Evidence**: [What suggests this]
**Test**: [How to verify]
**Result**: ✓ Confirmed / ✗ Rejected
**Conclusion**: [Next steps]
```

**Chrome DevTools Debugging**:

**Set Breakpoints**:
1. Go to Sources tab
2. Find file with suspected issue
3. Click line number to set breakpoint
4. Reproduce bug
5. Execution pauses at breakpoint
6. Inspect variables in Scope panel

**Step Through Execution**:
- Step Over (F10): Execute current line, move to next
- Step Into (F11): Enter function call
- Step Out (Shift+F11): Exit current function
- Resume (F8): Continue execution

**Watch Expressions**:
- Add variables to Watch panel
- Track how values change
- Identify where values become incorrect

**Call Stack Analysis**:
- Review function call chain
- Identify where execution entered bug path
- Trace back to original cause

**Evidence Collection**:
```markdown
## Root Cause Analysis

**Hypothesis Tested**: [Number tested]
**Root Cause**: [Identified cause]

**Evidence**:
- [Stack trace showing error origin]
- [Variable value: expected X, got Y]
- [Timeline: works until action Z]

**Why It Happens**:
[Clear explanation of mechanism]
```

**Validation**: `root_cause_identified_with_evidence`

### Step 4: Fix

**Purpose**: Implement minimal solution that addresses the root cause

**Fix Design**:
1. Design minimal fix targeting root cause
2. Preserve all existing functionality
3. Handle edge cases properly
4. Add error handling if missing
5. Consider performance impact

**Implementation Approach**:

**Minimal Fix**:
- Change only what's necessary
- Don't refactor working code
- Fix the cause, not symptoms
- Avoid scope creep

**Edge Case Handling**:
- Null/undefined checks
- Empty array/object handling
- Boundary conditions
- Error states

**Error Handling**:
- Try-catch for external operations
- Graceful degradation
- User-friendly error messages
- Logging for debugging

**Implementation Steps**:
1. Apply fix incrementally
2. Test after each change
3. Document complex logic with comments
4. Add preventive measures if appropriate

**Fix Documentation**:
```markdown
## Fix Applied

**Root Cause**: [What was broken]

**Solution**: [How it's fixed]

**Code Changes**:
```javascript
// Before
function buggy_code() {
  const element = document.querySelector('.modal');
  element.close(); // Error: element is null
}

// After
function fixed_code() {
  const element = document.querySelector('.modal');
  if (element && typeof element.close === 'function') {
    element.close();
  }
}
```

**Why This Works**: [Explanation]
```

**Testing During Fix**:
- Test fix resolves original issue
- Test edge cases
- Test error handling
- Verify no side effects

**Validation**: `fix_resolves_issue`

### Step 5: Verify

**Purpose**: Ensure fix works completely without introducing regressions

**Verification Checklist**:

**Original Issue**:
- [ ] Bug no longer occurs
- [ ] Fix works in all scenarios (not just happy path)
- [ ] Error messages no longer appear
- [ ] Expected behavior now happens

**No Regressions**:
- [ ] Related features still work
- [ ] No new errors introduced
- [ ] Performance not degraded
- [ ] No visual regressions
- [ ] Accessibility maintained

**Edge Cases**:
- [ ] Null/undefined handled
- [ ] Empty states handled
- [ ] Boundary conditions tested
- [ ] Error states handled gracefully

**Cross-Environment**:
- [ ] Works in target browsers (Chrome, Firefox, Safari, Edge)
- [ ] Works on mobile devices
- [ ] Works in different network conditions
- [ ] Works with different data states

**Code Quality**:
- [ ] Code follows project standards
- [ ] Error handling is robust
- [ ] No console warnings
- [ ] Documentation updated if needed

**Testing Protocol**:

```markdown
## Verification Report

### Original Issue
- [x] Modal closes when clicking outside
- [x] No console errors
- [x] Works on first click and subsequent clicks

### Regression Testing
- [x] Modal still opens correctly
- [x] Close button still works
- [x] Keyboard (ESC) close still works
- [x] Form submission still works

### Edge Cases
- [x] Multiple modals (if applicable)
- [x] Rapid clicking handled
- [x] Modal already closed when clicking outside

### Cross-Browser
- [x] Chrome 118+
- [x] Firefox 119+
- [x] Safari 17+
- [x] Edge 118+

### Performance
- [x] No performance degradation
- [x] No memory leaks
```

**Final Validation**: `all_tests_pass`

## 5. 🧩 Debug Modes

Select appropriate mode based on issue complexity:

### Quick Fix Mode

**When to Use**:
- Simple, obvious issues
- Typos or logic errors
- Missing null checks
- Clear from error message

**Approach**: Direct fix with basic testing
**Time**: 5-15 minutes

**Example**: Missing semicolon, undefined variable, typo in selector

### Standard Mode

**When to Use**:
- Typical bugs
- Clear reproduction steps
- Moderate complexity
- Single component issue

**Approach**: Full reproduce → diagnose → fix → verify cycle
**Time**: 30-60 minutes

**Example**: Event handler not firing, API request failing, layout issue

### Deep Investigation Mode

**When to Use**:
- Complex issues
- Intermittent bugs
- Multi-component interaction
- Unclear root cause

**Approach**: Extended analysis with multiple hypotheses
**Time**: 2-4 hours

**Example**: Race condition, timing issue, memory leak, state management bug

### 5.4 Performance Mode

**When to Use**:
- Speed or memory issues
- Need profiling
- Unclear cause

**Approach**: Profile → analyze → optimize → measure
**Time**: 1-3 hours

**Example**: Slow rendering, memory growth, janky animations

## 6. 🔍 Diagnostic Toolkit

### 6.1 Browser Issues

**Tools**:
- DevTools Console: JavaScript errors and logs
- Network Tab: Failed requests, slow responses
- Elements Tab: DOM inspection and modification
- Sources Tab: Debugging with breakpoints
- Performance Tab: Profiling and bottlenecks

**Common Patterns**:
- `Uncaught TypeError`: Usually null/undefined access
- `404 Not Found`: Wrong URL or missing resource
- `CORS error`: Cross-origin request blocked
- `Uncaught ReferenceError`: Variable not defined

### 6.2 Backend Issues

**Investigation**:
- Server logs analysis
- Database query inspection
- API endpoint testing (Postman, curl)
- Request/response validation

### 6.3 State Issues

**Investigation**:
- Component state inspection (React DevTools)
- Redux/Vuex store debugging
- Local storage review
- Session data analysis

### 6.4 Timing Issues

**Investigation**:
- Race condition detection
- Async flow analysis (Promise chains, async/await)
- Event order verification
- Debouncing/throttling checks

### 6.5 Chrome DevTools Integration

#### Essential Actions

**Navigate to Environment**:
1. Open staging URL in Chrome
2. Open DevTools (F12 or Cmd+Option+I)
3. Prepare to reproduce bug

**Console for Errors**:
1. Clear console (Cmd+K)
2. Reproduce bug
3. Check for errors (red messages)
4. Expand error for stack trace

**Network Monitoring**:
1. Open Network tab
2. Clear previous requests
3. Reproduce bug
4. Check for failed requests (red status)
5. Inspect request/response

**DOM Inspection**:
1. Go to Elements tab
2. Reproduce bug
3. Inspect affected elements
4. Check classes, attributes, computed styles

**JavaScript Debugging**:
1. Go to Sources tab
2. Find relevant file
3. Set breakpoint (click line number)
4. Reproduce bug
5. Step through execution
6. Inspect variables

#### Evidence Capture

**Screenshots**:
- Use DevTools screenshot (Cmd+Shift+P → "screenshot")
- Capture bug state in Elements tab
- Save network HAR file

**Export Data**:
- Console logs: Right-click → Save as
- Network HAR: Network tab → Export HAR
- Performance profile: Performance tab → Save profile

### 6.6 Browser Automation Tool Selection

**Strategy**: Follow this decision tree when browser automation or DevTools access is needed:

1. **Chrome DevTools MCP** (Primary choice)
   - Use available Chrome DevTools MCP servers: `mcp__chrome-devtools__*`
   - Multiple instances available: `chrome-devtools`, `chrome-devtools-2`, `chrome-devtools-3`, `chrome-devtools-4`
   - **If conflicts occur**: Try alternate instances (e.g., switch from -2 to -3)
   - **Why multiple instances**: Each can run with `--isolated` flag to prevent session interference
   - Common functions: `navigate_page`, `take_snapshot`, `evaluate_script`, `list_console_messages`

2. **Playwright MCP** (Fallback)
   - If Chrome DevTools unavailable or fails repeatedly
   - Use Playwright MCP: `mcp__playwright__*` functions
   - Functions: `playwright_navigate`, `playwright_evaluate`, `playwright_get_visible_html`
   - Provides similar automation with different architecture

3. **Code-Focused Analysis** (Final fallback)
   - If both browser automation MCPs fail or unavailable
   - Use static analysis: Read, Grep, Glob tools
   - Infer behavior from code structure and configuration
   - **Important**: Document assumptions and analysis limitations clearly

**Best Practice**: When browser automation is needed alongside manual development browsing, use an isolated instance to prevent conflicts

## 7. ✅ Output Format

After completing the workflow, generate a bug fix report:

```markdown
## Bug Fix Report

**Date**: [timestamp]
**Issue**: [Original bug description]
**Status**: ✓ Fixed and Verified

### Issue Summary

**Expected Behavior**: [What should happen]
**Actual Behavior**: [What was happening]
**Impact**: [Who/what was affected]

### Root Cause

[Clear explanation of why the bug occurred]

**Evidence**:
- [Stack trace or error message]
- [Variable state showing problem]
- [Timeline of events leading to bug]

### Fix Applied

**File**: `path/to/file.js:line`

```javascript
// Changes made
[Code diff or description]
```

**Why This Works**: [Explanation of how fix addresses root cause]

### Testing Completed

- [x] Original issue resolved
- [x] No regressions introduced
- [x] Edge cases handled
- [x] Cross-browser tested
- [x] Performance maintained

### Prevention

**How to Prevent Similar Issues**:
[Recommendations for avoiding this class of bug]

**Suggested Improvements**:
[Optional: Preventive measures to add]
```

## 8. 📖 Rules

### 8.1 ALWAYS

- Reproduce the bug reliably before attempting to fix
- Find root cause with evidence (not assumptions)
- Test the fix thoroughly in all relevant scenarios
- Check for regressions in related functionality
- Document complex fixes with comments
- Verify edge cases are handled
- Test cross-browser if applicable
- Capture evidence (errors, logs, screenshots)
- Fix the cause, not the symptom

### 8.2 NEVER

- Fix symptoms without understanding root cause
- Apply fixes without testing first
- Ignore edge cases or error handling
- Skip verification step
- Leave debugging code (console.log) in production
- Assume fix works without measurement
- Introduce regressions for a fix
- Skip documentation for complex fixes

### 8.3 ESCALATE IF

- Cannot reproduce the issue consistently
- Root cause remains unclear after investigation
- Fix would break other features
- Requires architectural changes
- Has security implications
- Affects critical production systems
- Need domain expertise not available

## 9. 🛠️ Troubleshooting

### 9.1 Cannot Reproduce Bug

**Actions**:
- Verify environment matches reported conditions
- Check browser version, device type, network speed
- Review exact steps from bug report
- Try different data states
- Check if already fixed in newer version

### 9.2 Multiple Potential Causes

**Actions**:
- List all hypotheses
- Test each systematically
- Gather evidence for/against each
- Eliminate one at a time
- May be multiple bugs (fix separately)

### 9.3 Intermittent Bug

**Actions**:
- Increase reproduction attempts
- Look for timing issues (race conditions)
- Check async operations
- Monitor for state changes
- Add extensive logging
- Use performance profiling

### 9.4 Fix Doesn't Work

**Actions**:
- Re-verify root cause
- Check if fix actually applied
- Clear cache and reload
- Check for competing code paths
- Review for logical errors in fix

## 10. 📚 Embedded Reference

- No External References: This skill is self-contained. Cite only knowledge/*.md when needed.

### Quick Catalogs

- Common Bug Patterns: Null/undefined access, race conditions, memory leaks, state bugs, DOM timing issues, network/API failures, animation jank.
- DevTools Workflows: Console, Network, Elements, Sources, Performance; breakpoints (line, conditional, DOM, XHR/event); watch expressions; call stack; HAR/profile export.
- Diagnostic Techniques: Binary search isolation, git bisect, hypothesis testing, logging strategy, time-travel debugging.

See knowledge/debugging.md, knowledge/initialization_pattern.md, knowledge/code_standards.md for deeper guidance.

## 11. 💡 Debug Philosophy

**Core Principle**: "Fix the root cause, not the symptom"

**Systematic Approach**: Evidence over assumptions

Effective debugging is methodical, not magical. This skill ensures every fix is:

- **Reproducible**: Can trigger the bug reliably
- **Evidence-based**: Root cause identified with proof
- **Minimal**: Smallest change that fixes the issue
- **Verified**: Tested thoroughly without regressions
- **Documented**: Clear explanation of cause and fix

The goal is not just to make errors disappear, but to understand and solve the underlying problem.
