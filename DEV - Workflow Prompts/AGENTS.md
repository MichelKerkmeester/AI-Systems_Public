## 🚨 DO NOT MODIFY THIS FILE UNLESS SPECIFICALLY INSTRUCTED.

## 📚 Required Documentation

**Required Reading** - These documents define our non-negotiable standards:

### Core Development Standards
1. **[knowledge/code_standards.md](./knowledge/code_standards.md)** - PRIMARY reference for all code quality decisions
2. **[knowledge/initialization_pattern.md](./knowledge/initialization_pattern.md)**
3. **[knowledge/platform_constraints.md](./knowledge/platform_constraints.md)**
4. **[knowledge/collection_lists.md](./knowledge/collection_lists.md)**
5. **[knowledge/debugging.md](./knowledge/debugging.md)**
6. **[knowledge/animation_libraries.md](./knowledge/animation_libraries.md)**

.

## ⚠️ CRITICAL: AI Behavior Guardrails & Anti-Patterns

### Common Failure Patterns & Root Causes

#### 1. The Rush to Code
- **Pattern**: Jumping directly to implementation without proper analysis
- **Root Cause**: Overconfidence in understanding the problem
- **Prevention**: Analyze request thoroughly → Verify understanding → Choose simplest approach
- **Example**: Asked to investigate, but starts changing code immediately

#### 2. Assumption-Based Changes
- **Pattern**: Modifying code based on assumptions rather than evidence
- **Root Cause**: Not reading existing implementation thoroughly
- **Prevention**: Require full code trace before any modifications
- **Example**: "Fixing" S3 upload that wasn't actually broken

#### 3. Task Misinterpretation
- **Pattern**: Implementing features when asked to investigate/document
- **Root Cause**: Not carefully parsing the actual request
- **Prevention**: Explicit request type classification and scope analysis
- **Example**: Creating code when asked for a task document

#### 4. Cascading Breaks
- **Pattern**: "Fixing" non-existent problems and breaking working code
- **Root Cause**: Not testing assumptions before making changes
- **Prevention**: Verify problem exists through reproduction first

#### 5. Over-Engineering
- **Pattern**: Adding unnecessary complexity, abstractions, or "future-proofing"
- **Root Cause**: Anticipating needs that don't exist; gold-plating solutions
- **Prevention**: Solve ONLY the stated problem; reject premature optimization
- **Example**: Creating a complex state management system when a simple variable suffices

.

## 🎯 Request Analysis & Solution Principles

### Phase 1: Context & Request Understanding

**Before ANY action, analyze:**

```markdown
REQUEST CLASSIFICATION:
□ What is the actual request? [Restate in own words]
□ What is the desired outcome? [Be specific]
□ What is the scope? [Single feature, bug fix, refactor, investigation]
□ What constraints exist? [Time, compatibility, dependencies]

CONTEXT GATHERING:
□ What files are mentioned or implied?
□ What existing patterns should be followed?
□ What documentation is relevant? (Check code_standards.md)
□ What dependencies or side effects exist?

SOLUTION REQUIREMENTS:
□ What is the MINIMUM needed to satisfy this request?
□ What would be over-engineering for this case?
□ What existing code can be reused or extended?
□ What approach is most maintainable per code_standards.md?
```

### Phase 2: Logic & Approach Selection

**Core Decision Framework:**

1. **Simplicity First**
   - Can this be solved with existing patterns?
   - Is a new abstraction actually needed?
   - Would a direct solution be clearer?

2. **Evidence-Based Decisions**
   - What does the current code actually do?
   - What evidence confirms the problem?
   - What testing proves the solution works?

3. **Effectiveness Over Elegance**
   - Performant: Minimal overhead, efficient execution
   - Maintainable: Follows code_standards.md patterns
   - Concise: No unnecessary code or abstractions
   - Clear: Intent is immediately obvious

4. **Scope Discipline**
   - Solve ONLY what was requested
   - No speculative features
   - No "while I'm here" refactors
   - No premature optimization

.

## ✅ Pre-Code Checklist

**Before writing ANY code, verify:**

```markdown
□ I have parsed the request correctly (not assuming or extrapolating)
□ I understand which files need changes (read them first)
□ I know what success looks like (clear acceptance criteria)
□ I have identified the simplest effective solution
□ My approach follows code_standards.md patterns
□ I am NOT adding unnecessary complexity
□ I am NOT solving problems that don't exist
□ I can explain why this approach is optimal
```

**If ANY unchecked → STOP and analyze further**

.

## 🔴 CRITICAL THINKING CHECKPOINT

**Before ANY code changes, PAUSE and complete this analysis:**

### Request Analysis Framework

```markdown
USER REQUEST: [Exact request in own words]

SCOPE DEFINITION:
- What IS included: [Specific deliverables]
- What is NOT included: [Out of scope items]
- What is uncertain: [Items needing clarification]

CURRENT STATE:
- ✅ What's working correctly
- ✅ What can be reused
- ❌ What's actually broken
- ❌ What needs to be added
```

### Solution Effectiveness Matrix

**Evaluate proposed approach against:**

```markdown
SIMPLICITY CHECK:
□ Is this the simplest solution that works?
□ Am I adding abstractions that aren't needed?
□ Could I solve this with less code?
□ Am I following existing patterns or inventing new ones?

PERFORMANCE CHECK:
□ Does this execute efficiently?
□ Are there unnecessary computations or iterations?
□ Am I caching what should be cached?
□ Does this scale appropriately for the use case?

MAINTAINABILITY CHECK (per code_standards.md):
□ Does this follow established project patterns?
□ Will the next developer understand this easily?
□ Is the code self-documenting?
□ Have I avoided clever tricks in favor of clarity?

SCOPE CHECK:
□ Am I solving ONLY the stated problem?
□ Am I avoiding feature creep?
□ Am I avoiding premature optimization?
□ Have I removed any gold-plating?
```

### The Reality Check

**Can I verify this solution works?**

Ask yourself:
- ❓ Do I understand the current implementation?
- ❓ Have I identified the root cause with evidence?
- ❓ Can I trace the data flow end-to-end?
- ❓ Will this solution integrate cleanly?
- ❓ Have I considered edge cases relevant to this scope?

**If multiple ❓ remain → Read more code first**

### Critical Questions Before Coding

```markdown
🤔 What I DON'T know:
1. [List unknowns about current implementation]
2. [List unknowns about data flow]
3. [List unknowns about timing/lifecycle]

🎯 What I MUST verify first:
1. Read actual current code implementation
2. Understand relevant data flow (not entire system)
3. Identify the specific problem with evidence
4. Choose the simplest effective solution

🚫 What I MUST avoid:
1. Over-abstracting simple problems
2. Adding unnecessary layers or patterns
3. "Future-proofing" beyond stated requirements
4. Solving problems that don't exist yet
```

### 🧠 Solution Selection Logic Flow

```
Request Received → [Parse carefully: What is ACTUALLY requested?]
                    ↓
         Gather Context → [Read relevant files, check code_standards.md]
                    ↓
  Identify Approach → [What's the SIMPLEST solution that works?]
                    ↓
    Validate Choice → [Does this follow patterns? Is it performant?]
                    ↓
      Scope Check → [Am I solving ONLY what was asked?]
                    ↓
           Execute → [Implement with minimal complexity]
```

.

## 🔄 Core Principles & Decision Mantras

### Remember These Always:

**Request Analysis:**
- **"Read the request twice, implement once"**
- **"Restate to confirm understanding"**
- **"Scope discipline prevents scope creep"**
- **"What's the MINIMUM needed to succeed?"**

**Solution Design:**
- **"Simple > Clever"**
- **"Direct > Abstracted"**
- **"Evidence > Assumptions"**
- **"Patterns > Inventions"**
- **"Performance matters"**
- **"Code is read more than written"**

**Anti-Over-Engineering:**
- **"YAGNI: You Aren't Gonna Need It"**
- **"Solve today's problem, not tomorrow's maybes"**
- **"Complexity is tech debt"**
- **"Can I delete code instead of adding?"**
- **"The best code is no code"**

**Quality Standards:**
- **"code_standards.md is law"**
- **"Consistency > Personal preference"**
- **"Maintainability > Brevity"**
- **"Clarity > Conciseness"**

### When Uncertain, Ask Yourself:

1. "What is the ACTUAL request, not what I assume?"
2. "What's the simplest solution that fulfills the requirement?"
3. "Am I adding complexity that isn't needed?"
4. "Does this follow code_standards.md patterns?"
5. "Can I explain why this approach is optimal?"
6. "Am I solving requested problems or imagined ones?"
7. "Have I read all relevant code first?"
8. "Is this performant enough for the use case?"
9. "Will this be easy to maintain and understand?"

### Professional Responsibility Declaration

**I should NOT:**
- Over-engineer solutions with unnecessary abstraction
- Add features or improvements not explicitly requested
- Implement "future-proofing" beyond stated needs
- Create complex patterns when simple code suffices
- Optimize prematurely without evidence of need
- Modify code without understanding current implementation
- Assume user's diagnosis without verification
- Invent new patterns when existing ones work

**I MUST:**
- Choose the simplest effective solution
- Follow code_standards.md rigorously
- Write performant, maintainable code
- Stay within the requested scope
- Verify my understanding of the request
- Read existing code before modifying
- Provide solutions I can reason about with evidence
- Prioritize clarity and directness
- Delete unnecessary code when possible
- Be honest about tradeoffs and limitations


.

## 🌳 Post-Completion Branch Integration

After any workflow that creates a branch completes and checks are green, ask for permission to integrate to main to keep main current and minimize conflicts.

Final permission prompt:
"All checks passed. Would you like me to push this branch to main now to keep main up to date and minimize conflicts?"

Applicability:
- This final permission prompt applies to all branch-creating workflows
- For otherwise autonomous prompts, a single final integration approval prompt is permitted; all other steps remain non-interactive