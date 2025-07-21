# Memory Automation v2 Design

## Architecture Overview

The enhanced memory system uses a 4-layer enforcement approach to ensure consistent, automatic memory capture without user intervention.

```
┌─────────────────────────────────────────────┐
│          Layer 4: CLAUDE.md Rules           │
│    (Behavioral enforcement via prompts)      │
├─────────────────────────────────────────────┤
│        Layer 3: Pre/Post Task Hooks         │
│    (Workflow integration & validation)       │
├─────────────────────────────────────────────┤
│       Layer 2: Conversation Buffer          │
│    (Continuous analysis & batching)          │
├─────────────────────────────────────────────┤
│        Layer 1: Direct MCP Execution        │
│    (Core capture mechanism via hooks)        │
└─────────────────────────────────────────────┘
```

## Layer 1: Direct MCP Execution

### Enhanced Memory Hook Implementation

```python
# .claude/logic/hooks/memory/memory-context-hook-v2.py
import subprocess
import json
from datetime import datetime
from .memory_capture_queue import MemoryCaptureQueue

class MemoryContextHookV2(HookBase):
    def __init__(self):
        super().__init__("MemoryContextV2")
        self.queue = MemoryCaptureQueue()
        self.batch_size = 5
        
    def execute_mcp_call(self, tool_name, params):
        """Direct MCP execution via subprocess"""
        mcp_command = {
            "tool": tool_name,
            "parameters": params
        }
        
        try:
            # Execute via Claude Code's MCP bridge
            result = subprocess.run(
                ["claude-code", "mcp", "call"],
                input=json.dumps(mcp_command),
                capture_output=True,
                text=True
            )
            return json.loads(result.stdout)
        except Exception as e:
            self.queue.add_failed_capture(params, str(e))
            return None
    
    def capture_memory_direct(self, content, metadata):
        """Directly capture memory without user intervention"""
        episode_data = {
            "name": f"{metadata['type']}: {metadata['summary'][:50]}",
            "episode_body": content,
            "source": "claude_code_automation_v2",
            "source_description": f"Auto-captured from {metadata['trigger']}",
            "valid_at": datetime.now().isoformat(),
            "group_id": metadata.get('group_id', 'auto-capture')
        }
        
        # Queue for batch processing
        self.queue.add(episode_data)
        
        # Process batch if threshold reached
        if self.queue.size() >= self.batch_size:
            self.process_batch()
    
    def process_batch(self):
        """Process queued memories in batch"""
        batch = self.queue.get_batch(self.batch_size)
        for episode in batch:
            self.execute_mcp_call(
                "mcp__graphiti-gemini__add_episode",
                {"data": episode}
            )
```

### Memory Capture Queue

```python
# .claude/logic/hooks/memory/memory_capture_queue.py
import json
from pathlib import Path
from threading import Lock

class MemoryCaptureQueue:
    def __init__(self):
        self.queue_file = Path(".claude/state/memory_queue.json")
        self.lock = Lock()
        self._ensure_queue_file()
    
    def add(self, episode_data):
        """Add memory to queue"""
        with self.lock:
            queue = self._load_queue()
            queue.append({
                "data": episode_data,
                "timestamp": datetime.now().isoformat(),
                "status": "pending"
            })
            self._save_queue(queue)
    
    def get_batch(self, size):
        """Get batch of memories for processing"""
        with self.lock:
            queue = self._load_queue()
            pending = [m for m in queue if m["status"] == "pending"]
            batch = pending[:size]
            
            # Mark as processing
            for item in batch:
                item["status"] = "processing"
            
            self._save_queue(queue)
            return [item["data"] for item in batch]
```

## Layer 2: Conversation Buffer Integration

### Active Conversation Analysis

```python
# .claude/logic/hooks/memory/conversation_buffer_v2.py
class ConversationBufferV2:
    def __init__(self, memory_hook):
        self.memory_hook = memory_hook
        self.buffer = []
        self.exchange_threshold = 5
        self.pattern_threshold = 2
        
    def add_exchange(self, user_msg, assistant_msg):
        """Add and analyze conversation exchange"""
        self.buffer.append({
            "user": user_msg,
            "assistant": assistant_msg,
            "timestamp": datetime.now()
        })
        
        # Immediate pattern detection
        patterns_found = self.detect_immediate_patterns(user_msg, assistant_msg)
        if len(patterns_found) >= self.pattern_threshold:
            self.capture_immediate(patterns_found)
        
        # Buffer analysis
        if len(self.buffer) >= self.exchange_threshold:
            self.analyze_and_capture()
    
    def detect_immediate_patterns(self, user_msg, assistant_msg):
        """Detect high-priority patterns for immediate capture"""
        immediate_patterns = {
            "CRITICAL_DECISION": r"decided to|final decision|going with",
            "ERROR_RESOLVED": r"fixed the|resolved|solution works",
            "BREAKING_CHANGE": r"breaking change|migration required",
            "SECURITY_ISSUE": r"security|vulnerability|exposed"
        }
        
        found = []
        combined = f"{user_msg} {assistant_msg}"
        for pattern_type, regex in immediate_patterns.items():
            if re.search(regex, combined, re.I):
                found.append((pattern_type, combined))
        
        return found
```

## Layer 3: Pre/Post Task Integration

### Task Lifecycle Hooks

```python
# .claude/logic/hooks/tasks/task_memory_integration.py
class TaskMemoryIntegration(HookBase):
    def __init__(self):
        super().__init__("TaskMemoryIntegration")
        self.memory_searcher = MemorySearcher()
        
    def pre_task_hook(self, task_description):
        """Enforce memory search before tasks"""
        # Search for relevant memories
        relevant_memories = self.memory_searcher.search(task_description)
        
        if not relevant_memories:
            # Force a broader search
            keywords = self.extract_keywords(task_description)
            for keyword in keywords:
                relevant_memories.extend(
                    self.memory_searcher.search(keyword)
                )
        
        # Inject memories into context
        if relevant_memories:
            return {
                "action": "inject_context",
                "memories": relevant_memories,
                "message": f"Found {len(relevant_memories)} relevant memories"
            }
        
        return {
            "action": "warn",
            "message": "No relevant memories found. Proceeding with fresh context."
        }
    
    def post_task_hook(self, task_result):
        """Capture task outcomes"""
        if task_result.get("completed"):
            self.capture_task_completion(task_result)
        
        if task_result.get("errors"):
            self.capture_error_resolution(task_result)
        
        if task_result.get("patterns_discovered"):
            self.capture_new_patterns(task_result)
```

## Layer 4: CLAUDE.md Enforcement

### Enhanced CLAUDE.md Rules

```markdown
## 🧠 MANDATORY MEMORY OPERATIONS

### BEFORE ANY TASK:
1. **ALWAYS** search memories using: `mcp__graphiti-gemini__search`
2. **ALWAYS** mention relevant memories found (or explicitly state none found)
3. **NEVER** skip this step - it's not optional

### DURING TASKS:
When you encounter any of these patterns, you MUST capture immediately:
- Decisions made (capture within 2 exchanges)
- Errors resolved (capture solution immediately)
- Patterns discovered (capture before moving on)
- Security considerations (capture immediately)
- Performance optimizations (capture metrics)

### AFTER TASKS:
1. Capture task summary with lessons learned
2. Update any outdated memories
3. Create reusable patterns from solutions

### ENFORCEMENT:
- The system tracks your memory operations
- Skipping memory operations = invalid response
- Each session starts with: "Searched X memories, found Y relevant"
- Each task ends with: "Captured N new memories"

### MEMORY CAPTURE TEMPLATE:
When capturing, use this format:
```
mcp__graphiti-gemini__add_episode
{
  "data": {
    "name": "[TYPE]: Brief description",
    "episode_body": "Detailed content with context",
    "source": "task_completion|conversation|error_fix|pattern",
    "group_id": "project-name-category"
  }
}
```
```

## Implementation Components

### 1. Memory Automation Service

```python
# .claude/logic/memory/memory_automation_service.py
class MemoryAutomationService:
    def __init__(self):
        self.direct_executor = DirectMCPExecutor()
        self.conversation_buffer = ConversationBufferV2()
        self.task_integrator = TaskMemoryIntegration()
        self.stats_tracker = MemoryStatsTracker()
        
    def start(self):
        """Initialize all automation layers"""
        # Start queue processor
        self.queue_processor = QueueProcessor(self.direct_executor)
        self.queue_processor.start()
        
        # Initialize hooks
        self.register_hooks()
        
        # Load startup context
        self.load_startup_memories()
```

### 2. Statistics Tracking

```python
# .claude/logic/memory/memory_stats_tracker.py
class MemoryStatsTracker:
    def track_capture(self, memory_type, trigger):
        """Track memory capture statistics"""
        stats = self.load_stats()
        today = datetime.now().date().isoformat()
        
        if today not in stats:
            stats[today] = {
                "total": 0,
                "by_type": {},
                "by_trigger": {},
                "automation_rate": 0
            }
        
        stats[today]["total"] += 1
        stats[today]["by_type"][memory_type] = \
            stats[today]["by_type"].get(memory_type, 0) + 1
        stats[today]["by_trigger"][trigger] = \
            stats[today]["by_trigger"].get(trigger, 0) + 1
```

### 3. Subprocess MCP Bridge

```python
# .claude/logic/memory/mcp_bridge.py
class MCPBridge:
    """Bridge to execute MCP tools via subprocess"""
    
    @staticmethod
    def call_tool(tool_name, parameters):
        """Execute MCP tool and return result"""
        command = [
            "python", "-m", "claude_mcp_client",
            "--tool", tool_name,
            "--params", json.dumps(parameters)
        ]
        
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                raise Exception(f"MCP call failed: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            raise Exception("MCP call timed out")
```

## Configuration Updates

### settings.json
```json
{
  "memory": {
    "automation_version": "2.0",
    "execution_mode": "direct",
    "batch_size": 5,
    "queue_retry_attempts": 3,
    "conversation_buffer": {
      "enabled": true,
      "threshold": 5,
      "immediate_patterns": true
    },
    "task_integration": {
      "pre_search": "mandatory",
      "post_capture": "automatic"
    },
    "statistics": {
      "track_captures": true,
      "daily_target": 50
    }
  }
}
```

## Migration Strategy

1. **Phase 1:** Deploy queue system (no breaking changes)
2. **Phase 2:** Activate direct execution for test group
3. **Phase 3:** Enable conversation buffer
4. **Phase 4:** Enforce CLAUDE.md rules
5. **Phase 5:** Full rollout with monitoring

## Monitoring & Alerts

- Daily capture count vs target (50)
- Queue processing delays
- Failed capture retry rates
- Pattern hit rates
- Memory search usage stats