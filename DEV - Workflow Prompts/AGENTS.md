## ⚠️ DO NOT MODIFY THIS FILE UNLESS SPECIFICALLY INSTRUCTED.

## 📚 Required Documentation

**Required Reading** - These documents define our non-negotiable standards:

### Core Development Standards
1. **[knowledge/code_standards.md](./knowledge/code_standards.md)**
2. **[knowledge/initialization_pattern.md](./knowledge/initialization_pattern.md)**
3. **[knowledge/platform_constraints.md](./knowledge/platform_constraints.md)**
4. **[knowledge/collection_lists.md](./knowledge/collection_lists.md)**
5. **[knowledge/debugging.md](./knowledge/debugging.md)**
6. **[knowledge/animation_libraries.md](./knowledge/animation_libraries.md)**

.

## 🚨 CRITICAL: AI Behavior Guardrails & Anti-Patterns

### Common Failure Patterns & Root Causes

#### 1. The Rush to Code
**Pattern**: Jumping directly to implementation without proper analysis
**Root Cause**: Overconfidence in understanding the problem
**Prevention**: Enforce investigation → documentation → approval gates
**Example**: Asked to investigate, but starts changing code immediately

#### 2. Assumption-Based Changes
**Pattern**: Modifying code based on assumptions rather than evidence
**Root Cause**: Not reading existing implementation thoroughly
**Prevention**: Require full code trace before any modifications
**Example**: "Fixing" S3 upload that wasn't actually broken

#### 3. Task Misinterpretation
**Pattern**: Implementing features when asked to investigate/document
**Root Cause**: Not carefully parsing the actual request
**Prevention**: Explicit request type classification
**Example**: Creating code when asked for a task document

#### 4. Cascading Breaks
**Pattern**: "Fixing" non-existent problems and breaking working code
**Root Cause**: Not testing assumptions before making changes
**Prevention**: Verify problem exists through reproduction first

.

### 📝 Investigation Protocol (Pre-Spec Activity)

**IMPORTANT**: Investigation happens BEFORE entering Spec Kit workflow

#### When to Investigate (NOT implement)
- User asks "why is X broken?"
- User asks to "investigate", "debug", or "analyze"
- User requests a "task document" or "findings report"
- You're unsure if a problem actually exists

#### Investigation Phase (READ-ONLY)
```markdown
INVESTIGATION RULES:
1. Read request carefully - what is ACTUALLY being asked?
2. Examine all related files WITHOUT modifying
3. Trace execution paths and data flow
4. Document findings in structured format
5. DO NOT CHANGE ANY CODE during investigation
6. After investigation → Use /specify if implementation needed
```

#### Investigation Output → Spec Kit Input
```markdown
## Investigation Report
### Request: [What was asked]
### Current Behavior: [How it works now]
### Findings: [What was discovered]
### Recommendation:
- Bug confirmed → Run: /specify "Fix [specific issue found]"
- Feature gap → Run: /specify "Add [needed capability]"
- Working correctly → Close with documentation

Note: Investigation findings become the input for /specify command
```

.

### ✅ Pre-Code Checklist

**Before writing ANY code, verify:**

```markdown
□ Not an investigation/research request
□ Not a documentation-only request
□ Either:
   - For fixes: Investigation completed and documented
   - For features: User explicitly requested implementation
□ Spec Kit workflow status:
   - /specify completed (branch + spec.md exist)
   - /plan completed (plan.md exists)
   - /tasks completed (checklist.md exists)
   - /implement run (optional but recommended)
```

**If ANY unchecked → STOP and complete missing steps**

.

### 🔄 Core Mantras & Decision Points

#### Remember These Always:
- **"Read the request twice, implement once"**
- **"Investigation means ZERO code changes"**
- **"Document findings, not assumptions"**
- **"Test the problem exists before fixing"**
- **"Task docs before code changes"**
- **"When uncertain, use /specify"**

#### When Uncertain, Ask Yourself:
1. "Was I explicitly asked to change code?"
2. "Do I have evidence this is actually broken?"
3. "Have I documented my understanding first?"
4. "Would a task document be more appropriate?"
5. "Am I solving the requested problem or a different one?"

.

## 🔍 Chrome DevTools MCP Debugging Workflow

### Core Debugging Principles
**ALWAYS** follow this sequence when debugging frontend issues:
1. **Navigate** → Go to the target page
2. **Snapshot** → Capture current DOM state
3. **Analyze** → Identify elements with unique selectors
4. **Investigate** → Evaluate JavaScript state
5. **Act** → Make targeted fixes based on evidence

### Chrome DevTools MCP Best Practices

#### Element Selection Strategy
```markdown
□ Use unique element IDs when available
□ Prefer data attributes over classes for targeting
□ Use UIDs from snapshots for precise interactions
□ Avoid fragile selectors (nth-child, complex paths)
```

#### Debugging Workflow Example
```javascript
// 1. Navigate to page
chrome_navigate({ url: "https://site.com/page" })

// 2. Take snapshot for analysis
chrome_snapshot() // Returns DOM with UIDs

// 3. Use UIDs for precise targeting
chrome_evaluate({
  code: "document.querySelector('[uid=\"ABC123\"]').textContent"
})

// 4. Investigate state
chrome_console_logs() // Check for errors
chrome_network() // Review API calls
```

#### Common Debug Patterns
- **Form Issues**: Snapshot → Find form UID → Evaluate validation state
- **Event Handlers**: Use console logs to trace execution
- **Async Issues**: Monitor network tab for timing problems
- **Style Problems**: Evaluate computed styles directly

.

## 🌳 Post-Completion Branch Integration

After any workflow that creates a branch completes and checks are green, ask for permission to integrate to main to keep main current and minimize conflicts.

Final permission prompt:
"All checks passed. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?"

Applicability:
- This final permission prompt applies to all branch-creating workflows
- For otherwise autonomous prompts, a single final integration approval prompt is permitted; all other steps remain non-interactive
