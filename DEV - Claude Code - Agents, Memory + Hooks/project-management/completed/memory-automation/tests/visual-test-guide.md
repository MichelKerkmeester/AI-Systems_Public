# Memory v2 - Visual Testing Guide 📊

## What You'll See When It's Working

### 1. 🟢 During Pattern Detection
When you mention decisions, fixes, or patterns, you'll see subtle feedback:
```
🧠 Memory Context v2: Pattern detected - DECISION (PostgreSQL choice)
```

### 2. 🔍 Before Task Creation
When using TodoWrite or creating tasks:
```
=== 🔍 Memory Search Results ===
Searched 47 memories, found 3 relevant:
• [AUTH]: "JWT tokens with refresh mechanism"
• [SECURITY]: "Never store secrets in frontend"  
• [PATTERN]: "Use middleware for auth checks"
==================================
```

### 3. 📈 Statistics Output
Running `/memory stats` shows:
```
=== 📊 Memory Statistics ===
Today's Captures: 12
Automation Rate: 91.7%
By Pattern:
  • DECISION: 3
  • ERROR_RESOLVED: 2
  • SECURITY: 2
  • PATTERN: 3
  • REUSABLE_COMPONENT: 2
===========================
```

### 4. 🔄 Queue Status
Background processing indicator:
```
Memory Queue: 2 pending, 8 processed
```

## Visual Indicators by Feature

### ✅ Working Correctly

**Pattern Detection**
```diff
+ 🧠 Memory Context v2: Pattern detected - ERROR_RESOLVED
```

**Task Integration**  
```diff
+ Searched 23 memories, found 5 relevant
```

**Critical Patterns**
```diff
+ 🚨 SECURITY: Immediate capture - API key exposure
```

**Conversation Buffer**
```diff
+ 💬 Conversation analyzed: 3 insights captured
```

### ❌ Not Working

**No Pattern Feedback**
```diff
- [No memory feedback after obvious patterns]
```

**Manual Prompts**
```diff
- 💡 Would you like me to capture this decision?
```

**Task Without Search**
```diff
- [Task created without showing memory search]
```

## Live Testing Dashboard

### Terminal 1: Main Chat
```bash
claude code
# Run your test prompts here
```

### Terminal 2: Queue Monitor
```bash
watch -n 2 'python3 -c "from claude.logic.memory.memory_capture_queue import MemoryCaptureQueue; import json; print(json.dumps(MemoryCaptureQueue().get_stats(), indent=2))"'
```

### Terminal 3: Stats Monitor
```bash
watch -n 5 'tail -20 .claude/state/memory_stats.json | python3 -m json.tool'
```

## Pattern Testing Cheatsheet

| Pattern | Trigger Phrase | Expected Response |
|---------|---------------|-------------------|
| DECISION | "I've decided to..." | Pattern detected - DECISION |
| ERROR_RESOLVED | "Fixed it by..." | Pattern detected - ERROR_RESOLVED |
| SECURITY | "API_KEY" or "exposed" | 🚨 Immediate capture |
| PATTERN | "convention" or "always" | Pattern detected - PATTERN |
| BREAKING | "migration required" | Pattern detected - BREAKING_CHANGE |
| REUSABLE | "existing code" | Pattern detected - REUSABLE_COMPONENT |

## Success Metrics Visualization

### After 10 Minutes
```
📊 Memory Automation v2 - Performance
├── Captures: ████████████████████ 95%
├── Automated: ███████████████████░ 92%
├── Patterns: ████████████████████ 100%
├── Tasks: ████████████████████ 100%
└── Buffer: █████████████████░░░ 85%

Total: 12 memories | 0 manual prompts
```

### Pattern Distribution
```
DECISION        ████ 25%
ERROR_RESOLVED  ███  20%
SECURITY        ██   15%
PATTERN         ████ 25%
REUSABLE        ██   15%
```

## Quick Health Check

Run this to see a visual health status:
```bash
python3 -c "
from claude.logic.memory.memory_capture_queue import MemoryCaptureQueue
from claude.logic.memory.memory_stats_tracker import MemoryStatsTracker
q = MemoryCaptureQueue().get_stats()
s = MemoryStatsTracker().get_daily_stats()
print('=== 🏥 Memory v2 Health Check ===')
print(f'✅ Queue: {q[\"pending\"]} pending, {q[\"processed\"]} processed')
print(f'✅ Today: {s[\"total_captures\"]} captures')
print(f'✅ Auto Rate: {s[\"automation_rate\"]}%')
print(f'✅ Status: {'🟢 Healthy' if s['total_captures'] > 0 else '🔴 No captures'}')
print('================================')
"
```

## What Success Looks Like

### Good Session (30 min)
- 🟢 10-15 captures
- 🟢 No manual prompts
- 🟢 All patterns detected
- 🟢 Task searches working
- 🟢 95%+ automation

### Bad Session (Issues)
- 🔴 <5 captures
- 🔴 Manual capture prompts
- 🔴 Missing pattern detection
- 🔴 No task searches
- 🔴 <50% automation

---

**Visual Guide Version**: 1.0  
**Last Updated**: 2025-07-21