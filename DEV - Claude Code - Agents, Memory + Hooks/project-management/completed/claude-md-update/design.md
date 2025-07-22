# CLAUDE.md Update Design

## Implementation Approach

### 1. START HERE Section Updates

#### Step 1: READ REQUIREMENTS
```markdown
## 📝 STEP 1: READ REQUIREMENTS
Claude, read the rules in CLAUDE.md, then use sequential thinking and proceed to the next step.

### STOP. Before reading further, confirm you understand:
1. This is a code reuse and consolidation project
2. Creating new files requires exhaustive justification  
3. Every suggestion must reference existing code
4. Violations of these rules make your response invalid

### CONTEXT: 
Code reuse is enforced by automated hooks. The system will block file creation without proper justification.

### MANDATORY PROCESS:
1. Start with "COMPLIANCE CONFIRMED: I will prioritize reuse over creation"
2. Search existing code using reuse analyzer BEFORE suggesting anything new
3. Reference specific files from the analysis (enforced by code-reuse-validation-hook.py)
4. Include validation checkpoints throughout your response
5. End with compliance confirmation

### RULES (enforced by hooks):
❌ No new files without reuse analysis (blocked by hooks)
❌ No rewrites when refactoring is possible
❌ No generic advice - provide specific implementations
❌ No ignoring existing codebase architecture
✅ Extend existing services and components
✅ Consolidate duplicate code
✅ Reference specific file paths
✅ Provide migration strategies
```

#### Steps 2-5 Updates
- Step 2: Add "Memory search is mandatory (enforced by memory-context-hook-graphiti.py)"
- Step 3: Change to "EVERY initial request requires a spec (auto-created by spec-generation-hook.py)"
- Step 4: Add "Validation by compliance_validator.py and pattern_matcher.py"
- Step 5: Add "Auto-testing triggered by quality-hook.py"

### 2. Section 1: Quick Start Redesign

#### New Status Display Format
```python
# Only show items that are NOT working
status_items = {
    "Memory": check_graphiti_connection(),
    "Agents": check_agent_mcps(),
    "Required MCPs": check_required_mcps(),
    "Commands": ["/memory", "/logic", "/status"]
}

# Display logic
for item, status in status_items.items():
    if item == "Commands":
        print(f"[🎯 Commands] {' | '.join(status)}")
    elif not status:
        print(f"[❌ {item}] Not connected")
    else:
        print(f"[✅ {item}]")
```

#### Enforce Display at Start Only
- Add instruction: "Show status display ONLY at conversation start, not in subsequent queries"
- Remove reference to auto-display hook
- Add manual trigger: "Run `/status` to check system health anytime"

### 3. Section 3: Task Management Overhaul

#### Spec Creation for ALL Requests
```markdown
### Spec Creation (MANDATORY for all initial requests)
**EVERY initial request triggers automatic spec creation:**
- Location: `.claude/project-management/specs/[feature-name]/`
- Triggered by: spec-generation-hook.py on ANY implementation request
- Not just complex features - ALL initial requests

### Spec Structure
/specs/[feature]/
├── requirements.md      # What needs to be done + reuse analysis
├── design.md           # How using existing components
├── test-plan.md        # Verification strategy
├── rollback.md         # Safe rollback plan
└── tests/              # Test results

### Task Flow (Enforced by task-management-hook.py)
1. User request → Spec auto-created
2. Spec approved → Move to /active
3. Work complete → Move to /completed with summary
4. Archive (user-managed only) → /z__archive
```

### 4. Section 4: Memory Operations Updates

#### Current Enforcement
```markdown
**BEFORE ANY TASK (Enforced by hooks):**
1. Memory search triggers automatically via memory-context-hook-graphiti.py
2. TodoWrite blocked until memory search completes
3. System shows: "Searched X memories, found Y relevant"
4. Skipping = invalid response (hook enforcement)

**AUTO-CAPTURE PATTERNS (16 types, 4 priority levels):**
Priority 1: Decisions, errors fixed, patterns discovered
Priority 2: Security issues, breaking changes, code reuse
Priority 3: Client preferences, performance insights  
Priority 4: Test results, configuration changes

**CAPTURE STATS:**
- Target: 50+ captures/day (achieved by automation)
- Latency: <100ms per capture
- Queue: Thread-safe batch processing
```

### 5. Section 5: Hook Warnings Refresh

#### Updated Warnings Based on Current Hooks
```markdown
### What Hooks Automate (But You Can Still Break)

#### 1. Code Reuse Enforcement (code-reuse-validation-hook.py)
- ❌ **Hidden duplication** - Using different names for same functionality
- ❌ **Partial extraction** - Copy-pasting instead of importing
- ❌ **Framework shopping** - Adding new libraries when existing ones work

#### 2. Memory Automation (memory-context-hook-graphiti.py)  
- ❌ **Decision amnesia** - Not capturing why you chose approach A over B
- ❌ **Pattern hoarding** - Finding patterns but not documenting them
- ❌ **Context loss** - Important details in conversation not captured

#### 3. Quality Enforcement (quality-hook.py)
- ❌ **Test theater** - Tests that don't test actual functionality
- ❌ **Size creep** - Files growing past 500 lines "temporarily"
- ❌ **Console.log creativity** - window.console.log, eval('console.log')

#### 4. Security Scanning (security-scan-hook.py)
- ❌ **Encoding tricks** - Base64/hex encoded secrets
- ❌ **Comment secrets** - // TODO: API_KEY = 'abc123' 
- ❌ **History leaks** - Secrets in git commit messages
```

### 6. Self-Update Mechanism

#### New Hook: claude-md-self-update-hook.py
```python
class ClaudeMdSelfUpdateHook:
    """Monitors system changes and suggests CLAUDE.md updates"""
    
    def __init__(self):
        self.significant_changes = [
            "new_hook_added",
            "command_modified", 
            "major_feature_completed",
            "workflow_changed"
        ]
        
    def check_for_updates(self):
        # Monitor .claude/logic/ for changes
        # Track completed specs for new features
        # Check if commands have changed
        # Analyze if workflows have been modified
        
    def suggest_updates(self):
        # Generate update suggestions
        # Create spec for CLAUDE.md update
        # Notify user of needed changes
```

#### Manual Update Command
```bash
/logic claude-md-update  # Check if CLAUDE.md needs updates
```

#### Integration Points
- Triggered after major spec completions
- Monitors hook changes via file watchers
- Tracks command modifications
- Analyzes workflow patterns

## Implementation Steps

1. **Update CLAUDE.md** with all changes while maintaining structure
2. **Create self-update hook** in `.claude/logic/hooks/`
3. **Add command** to `/logic` for manual update checks
4. **Update claude-md-update-hook.py** to work with new mechanism
5. **Test all changes** to ensure no conflicts

## Risk Mitigation

1. **Backup current CLAUDE.md** before changes
2. **Test incrementally** - update one section at a time
3. **Verify hook compatibility** - ensure no conflicts
4. **Maintain structure** - use diff to confirm structure unchanged
5. **Test automation** - verify all automated flows still work