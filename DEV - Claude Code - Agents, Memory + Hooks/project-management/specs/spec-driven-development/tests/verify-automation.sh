#!/bin/bash
# Automation Verification Script
# Date: 2025-01-21
# Purpose: Verify spec-driven development works 100% automatically

echo "🔍 Verifying Spec-Driven Development Automation..."
echo "================================================"

# Check hook configuration
echo -e "\n1. Checking hook configuration..."
if grep -q "spec-generation-hook.py" .claude/settings.json; then
    echo "✅ Spec generation hook is configured"
    # Show position in hook list
    hook_position=$(grep -n "spec-generation-hook.py" .claude/settings.json | cut -d: -f1)
    echo "   Position in settings.json: line $hook_position"
else
    echo "❌ Spec generation hook NOT found in settings"
    echo "   ACTION REQUIRED: Restart Claude Code for hooks to load"
fi

# Check hook file exists and contents
echo -e "\n2. Checking hook file..."
HOOK_FILE=".claude/logic/hooks/core/spec-generation-hook.py"
if [ -f "$HOOK_FILE" ]; then
    echo "✅ Hook file exists"
    # Check file size
    file_size=$(wc -c < "$HOOK_FILE")
    echo "   File size: $file_size bytes"
    
    # Check key methods
    echo "   Checking implementation:"
    grep -q "_calculate_complexity_score" "$HOOK_FILE" && echo "   ✅ Complexity scoring implemented" || echo "   ❌ Complexity scoring missing"
    grep -q "_is_continuation_query" "$HOOK_FILE" && echo "   ✅ Continuation detection implemented" || echo "   ❌ Continuation missing"
    grep -q "TaskManager" "$HOOK_FILE" && echo "   ✅ TaskManager integration found" || echo "   ❌ TaskManager integration missing"
    grep -q "spec_threshold = 6" "$HOOK_FILE" && echo "   ✅ Threshold set to 6" || echo "   ❌ Threshold not properly set"
else
    echo "❌ Hook file missing at $HOOK_FILE"
fi

# Check TaskManager updates
echo -e "\n3. Checking TaskManager updates..."
TM_FILE=".claude/logic/tasks/task_manager.py"
if [ -f "$TM_FILE" ]; then
    grep -q "test_dir = project_dir / \"tests\"" "$TM_FILE" && echo "✅ Auto test folder creation implemented" || echo "❌ Test folder creation missing"
    grep -q "test_plan_content = " "$TM_FILE" && echo "✅ Test plan template implemented" || echo "❌ Test plan template missing"
    grep -q "timestamp = datetime.now().strftime" "$TM_FILE" && echo "✅ Timestamp generation implemented" || echo "❌ Timestamp missing"
else
    echo "❌ TaskManager file not found"
fi

# Check recent specs
echo -e "\n4. Checking for recent specs (last 24 hours)..."
if [ -d ".claude/project-management/specs" ]; then
    recent_specs=$(find .claude/project-management/specs -name "*.md" -mtime -1 2>/dev/null)
    spec_count=$(echo "$recent_specs" | grep -c "\.md" 2>/dev/null || echo "0")
    
    if [ "$spec_count" -gt 0 ]; then
        echo "✅ Found $spec_count recent specs:"
        echo "$recent_specs" | head -5 | while read spec; do
            [ -n "$spec" ] && echo "   - $(basename "$spec")"
        done
    else
        echo "⚠️  No recent specs found (this is normal if system was just set up)"
    fi
else
    echo "❌ Specs directory not found"
fi

# Check test folders
echo -e "\n5. Checking test folder structure..."
if [ -d ".claude/project-management/specs" ]; then
    test_folders=$(find .claude/project-management/specs -name "tests" -type d 2>/dev/null)
    test_count=$(echo "$test_folders" | grep -c "tests" 2>/dev/null || echo "0")
    
    if [ "$test_count" -gt 0 ]; then
        echo "✅ Found $test_count test folders:"
        echo "$test_folders" | head -3 | while read folder; do
            [ -n "$folder" ] && echo "   - $folder"
        done
    else
        echo "⚠️  No test folders found yet"
    fi
else
    echo "❌ Unable to check test folders"
fi

# Check session tracking
echo -e "\n6. Checking session tracking..."
SESSION_FILE=".claude/state/session-tracking.json"
if [ -f "$SESSION_FILE" ]; then
    echo "✅ Session tracking file exists"
    
    # Try to parse JSON (will fail gracefully if invalid)
    if command -v python3 &> /dev/null; then
        active_task=$(python3 -c "
import json
try:
    with open('$SESSION_FILE', 'r') as f:
        data = json.load(f)
        print(f\"   Active task: {data.get('active_task', 'None')}\")
        print(f\"   Query history entries: {len(data.get('query_history', []))}\")
except:
    print('   ⚠️  Unable to parse session file')
" 2>/dev/null)
        echo "$active_task"
    else
        echo "   ⚠️  Python3 not available to parse session file"
    fi
else
    echo "⚠️  Session tracking file not found (will be created on first use)"
fi

# Check for manual command usage (anti-pattern)
echo -e "\n7. Checking for manual command dependencies..."
if grep -q "/logic\|/save\|/memory" "$HOOK_FILE" 2>/dev/null; then
    echo "❌ WARNING: Hook contains manual commands (should be automatic)"
else
    echo "✅ No manual commands found in hook (good!)"
fi

# Summary
echo -e "\n================================================"
echo "AUTOMATION VERIFICATION SUMMARY"
echo "================================================"

all_good=true

# Core requirements check
if grep -q "spec-generation-hook.py" .claude/settings.json && [ -f "$HOOK_FILE" ]; then
    echo "✅ Core automation is configured"
else
    echo "❌ Core automation missing - RESTART CLAUDE CODE"
    all_good=false
fi

if [ "$all_good" = true ]; then
    echo -e "\n✅ The spec-driven development system appears to be fully automated!"
    echo "   Complex queries will automatically create specs without any commands."
else
    echo -e "\n⚠️  Some issues detected. Please review the output above."
fi

echo -e "\nTo test automation, try this query (NO COMMANDS):"
echo "\"I need to implement a user authentication system with email verification,"
echo "password reset, and role-based access control. Analyze requirements and create tests.\""
echo -e "\nThis should automatically create a spec if the system is working correctly."