# Memory v2 - Quick Test Script (10 minutes)

## 🚀 Rapid Testing Guide

Copy and paste these prompts in order to quickly test all memory automation features:

### 1. Start New Chat
```bash
cd /Users/michel_kerkmeester/AI\ \&\ Dev/Websites/anobel.nl
claude code
```

### 2. Test Prompts (Copy & Paste)

#### Round 1: Decision Pattern
```
I need to choose between MongoDB and PostgreSQL for my project. MongoDB offers flexibility but PostgreSQL has better consistency. I've decided to use PostgreSQL for this project because data integrity is critical.
```
*Wait 5 seconds for background capture*

#### Round 2: Error Fix Pattern  
```
I was getting "TypeError: Cannot read property 'map' of undefined" in my React component. The issue was that I wasn't checking if the array existed before mapping. I fixed it by adding a null check: items?.map() and now it works perfectly!
```
*Wait 5 seconds*

#### Round 3: Security Critical (Immediate)
```
I accidentally committed my AWS_SECRET_KEY to git! How do I remove it from history and what should I do about the exposed key?
```
*Should capture immediately due to critical pattern*

#### Round 4: Pattern Discovery
```
Show me a good pattern for implementing retry logic in API calls. I want something reusable that I can apply as a convention across all my API functions.
```
*Wait for response, then:*
```
Perfect! I'll use this exponential backoff pattern as our standard convention for all API calls going forward.
```

#### Round 5: Task Creation (Auto Search)
```
Create a task to implement user authentication with JWT tokens
```
*Should see "Searched X memories, found Y relevant" before task creation*

#### Round 6: Code Reuse Test
```
I need to create a new form validation utility. We might already have something similar in our codebase. What existing validation code can I reuse?
```
*Should trigger REUSABLE_COMPONENT pattern*

#### Round 7: Conversation Buffer Test (5 exchanges)
```
Let's discuss API design best practices
```
*Then have 4 more exchanges about APIs to trigger buffer analysis*

### 3. Verify Results

#### Check Capture Count
```
/memory stats
```
*Should show 7+ captures*

#### View Statistics Report  
```
python3 -c "from claude.logic.memory.memory_stats_tracker import MemoryStatsTracker; print(MemoryStatsTracker().export_formatted_report())"
```

#### Search for Specific Captures
```
/memory search PostgreSQL
/memory search security  
/memory search pattern
```

### 4. Success Checklist

- [ ] No manual capture prompts appeared
- [ ] Security pattern captured immediately
- [ ] Task showed memory search results
- [ ] Stats show 95%+ automation rate
- [ ] All captures happened in background
- [ ] Conversation buffer triggered after 5 exchanges

## 🎯 Expected Output

You should see:
- **7-10 memories** captured automatically
- **Zero** manual intervention prompts
- **Task search** showing relevant memories
- **Stats** showing high automation rate

## ⚡ Quick Verification

Run this one-liner to check if it's working:
```bash
python3 -c "from claude.logic.memory.memory_capture_queue import MemoryCaptureQueue; q=MemoryCaptureQueue(); s=q.get_stats(); print(f'✅ Memory v2 Working!' if s['processed'] > 0 or s['pending'] > 0 else '❌ No captures detected')"
```

## 🔧 Troubleshooting

If not working:
```bash
# 1. Check hooks enabled
grep -c "memory-context-hook-v2" .claude/settings.json
# Should return 1 or more

# 2. Check automation level  
grep -A3 '"memory"' .claude/settings.json | grep level
# Should show "full"

# 3. Check queue file exists
ls -la .claude/state/memory_queue.json
# Should exist after first capture
```

---

**Time Required**: 10 minutes  
**Expected Captures**: 7-10  
**Manual Actions**: 0