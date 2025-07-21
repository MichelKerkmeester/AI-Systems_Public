# Automation Verification Spec for Independent Testing
**Date:** 2025-01-21  
**Time:** 12:00:00  
**Purpose:** Independent verification that spec-driven development is 100% automated without user commands  

## Critical Requirement
**The system MUST create specs automatically without ANY user commands like `/logic`, `/save`, or `/memory`**

## Test Scenarios for Verification

### Scenario 1: Complex Query Test (Should Auto-Create Spec)
**User Input:** 
```
I need to build a comprehensive user management system with the following features:
- User registration with email verification
- Password reset functionality  
- Role-based access control (admin, user, guest)
- User profile management
- Activity logging
- Two-factor authentication
Please analyze the requirements, design the architecture, implement the features, and create comprehensive tests.
```

**Expected Automated Actions:**
1. ✅ Spec document created in `/specs/features/[project-name]/`
2. ✅ Project folder created with sanitized name
3. ✅ `/tests` subfolder created automatically
4. ✅ Test plan template generated with timestamp
5. ✅ User sees notification about spec creation
6. ✅ Session tracked in `.claude/state/session-tracking.json`
7. ✅ NO manual commands required

**Verification Steps:**
```bash
# Check if spec was created
ls -la .claude/project-management/specs/features/

# Verify test folder exists
find .claude/project-management/specs -name "tests" -type d

# Check session tracking
cat .claude/state/session-tracking.json
```

### Scenario 2: Simple Query Test (Should NOT Create Spec)
**User Input:**
```
What is 2 + 2?
```

**Expected Behavior:**
- ❌ No spec created (complexity score < 6)
- ✅ Query tracked in session history
- ✅ Normal response without automation

### Scenario 3: Continuation Query Test
**User Input (after Scenario 1):**
```
Also add logging functionality to that system
```

**Expected Behavior:**
- ❌ No new spec created (continuation detected)
- ✅ Continues in context of active task
- ✅ Session data shows same active_task

### Scenario 4: New Complex Query (Different Topic)
**User Input:**
```
Create a data visualization dashboard with these requirements:
- Real-time data updates
- Multiple chart types (line, bar, pie, scatter)
- Export functionality (PDF, CSV, PNG)
- Responsive design for mobile
- Dark mode support
First analyze existing solutions, then design the component architecture, and implement with tests.
```

**Expected Automated Actions:**
1. ✅ New spec in appropriate category (likely `/features/`)
2. ✅ New project folder with tests directory
3. ✅ Previous task remains in specs
4. ✅ Session updates to new active task

## Verification Checklist

### Pre-Test Setup
- [ ] Ensure Claude Code is restarted (hooks load on startup)
- [ ] Clear any existing test data: `rm -rf .claude/project-management/specs/features/test-*`
- [ ] Verify hook is in settings: `grep "spec-generation-hook" .claude/settings.json`

### During Test Execution
- [ ] NO commands typed (no `/logic`, `/save`, etc.)
- [ ] Only natural language queries used
- [ ] Watch for system notifications about spec creation

### Post-Test Verification
Run these commands to verify automation worked:

```bash
# 1. Check spec files were created
find .claude/project-management/specs -name "*.md" -mmin -10

# 2. Verify folder structure
tree .claude/project-management/specs/features/ -L 3

# 3. Check timestamps in files
grep -E "Date:|Time:" .claude/project-management/specs/features/*/\*.md

# 4. Verify test folders
find .claude/project-management/specs -name "tests" -type d | wc -l

# 5. Check session tracking
cat .claude/state/session-tracking.json | python3 -m json.tool

# 6. Verify hook execution (if logs available)
# Check Claude Code logs for spec-generation-hook execution
```

### Expected File Structure After Tests
```
.claude/project-management/specs/
├── features/
│   ├── build-comprehensive-user-management-system-[timestamp]/
│   │   ├── build-comprehensive-user-management-system-[timestamp].md
│   │   └── tests/
│   │       └── test-plan-[timestamp].md
│   └── create-data-visualization-dashboard-[timestamp]/
│       ├── create-data-visualization-dashboard-[timestamp].md
│       └── tests/
│           └── test-plan-[timestamp].md
```

## Key Files to Examine

1. **Spec Generation Hook:** `.claude/logic/hooks/core/spec-generation-hook.py`
   - Check `_calculate_complexity_score()` method
   - Verify threshold is 6 points
   - Check `_is_continuation_query()` logic

2. **Task Manager:** `.claude/logic/tasks/task_manager.py`
   - Verify `create_task()` creates project folders
   - Check test folder creation logic (lines ~180-200)

3. **Settings:** `.claude/settings.json`
   - Confirm spec-generation-hook is in UserPromptSubmit
   - Should be last hook in the list

## Success Criteria

The automation is working correctly if:
1. ✅ Complex queries create specs WITHOUT any commands
2. ✅ Each spec has its own project folder
3. ✅ Test folders are created automatically
4. ✅ All files have timestamps
5. ✅ Continuation queries don't create duplicate specs
6. ✅ Simple queries don't trigger spec creation
7. ✅ User sees notifications about spec creation

## Failure Indicators

The automation has issues if:
1. ❌ User needs to type any command to create specs
2. ❌ Specs created in root specs/ folder (not in subfolders)
3. ❌ No test folders created
4. ❌ Missing timestamps in files
5. ❌ Every query creates a spec (even simple ones)
6. ❌ No notifications shown to user
7. ❌ Session tracking file not updated

## Additional Tests

### Edge Case 1: Multiple Requirements List
```
Please help me with the following tasks:
1. Fix the login bug in authentication
2. Add user profile pictures
3. Implement password strength checker
4. Create API documentation
5. Set up CI/CD pipeline
```
**Expected:** Should create spec (multiple requirements = higher complexity)

### Edge Case 2: Vague but Complex
```
Build me something amazing for managing my company's data
```
**Expected:** Should NOT create spec (too vague, low complexity score)

### Edge Case 3: Technical Deep Dive
```
Analyze the performance bottlenecks in our React application, 
profile the render cycles, identify unnecessary re-renders, 
implement memoization strategies, and optimize the bundle size
```
**Expected:** Should create spec (analysis + implementation = high complexity)

## Final Verification Script

Create and run this script to do a complete verification:

```bash
#!/bin/bash
# Save as: verify-automation.sh

echo "🔍 Verifying Spec-Driven Development Automation..."

# Check hook configuration
echo -e "\n1. Checking hook configuration..."
if grep -q "spec-generation-hook.py" .claude/settings.json; then
    echo "✅ Spec generation hook is configured"
else
    echo "❌ Spec generation hook NOT found in settings"
fi

# Check hook file exists
echo -e "\n2. Checking hook file..."
if [ -f ".claude/logic/hooks/core/spec-generation-hook.py" ]; then
    echo "✅ Hook file exists"
    # Check key methods
    grep -q "_calculate_complexity_score" .claude/logic/hooks/core/spec-generation-hook.py && echo "  ✅ Complexity scoring implemented"
    grep -q "_is_continuation_query" .claude/logic/hooks/core/spec-generation-hook.py && echo "  ✅ Continuation detection implemented"
else
    echo "❌ Hook file missing"
fi

# Check recent specs
echo -e "\n3. Checking for recent specs..."
recent_specs=$(find .claude/project-management/specs -name "*.md" -mmin -60 2>/dev/null | wc -l)
echo "Found $recent_specs specs created in last hour"

# Check folder structure
echo -e "\n4. Checking folder structure..."
test_folders=$(find .claude/project-management/specs -name "tests" -type d 2>/dev/null | wc -l)
echo "Found $test_folders test folders"

# Check session tracking
echo -e "\n5. Checking session tracking..."
if [ -f ".claude/state/session-tracking.json" ]; then
    echo "✅ Session tracking file exists"
    active_task=$(python3 -c "import json; print(json.load(open('.claude/state/session-tracking.json')).get('active_task', 'None'))" 2>/dev/null)
    echo "  Active task: $active_task"
else
    echo "❌ Session tracking file missing"
fi

echo -e "\n✅ Verification complete!"
```

## Important Notes for Tester

1. **Restart Required:** The spec-generation-hook only loads when Claude Code starts. If you just pulled these changes, restart Claude Code.

2. **Complexity Threshold:** The system uses a 6-point threshold. Queries need to score 6+ points to trigger automation.

3. **No Manual Override:** There's currently no way to force spec creation for low-complexity queries without modifying the threshold.

4. **Session Persistence:** The session tracking persists between conversations, so continuation detection works across sessions.

5. **Notification Visibility:** Spec creation notifications appear as system messages in the conversation.

---

**This spec provides everything needed for independent verification that the automation works 100% without user commands.**