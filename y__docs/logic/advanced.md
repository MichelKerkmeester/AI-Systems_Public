# Advanced Configuration

## Table of Contents

  - [Hook Architecture](#hook-architecture)
  - [State Management](#state-management)
  - [Pattern Matching](#pattern-matching)
- [Multi-Agent Configuration](#multi-agent-configuration)
  - [Agent Isolation](#agent-isolation)
  - [Distributed Locking](#distributed-locking)
  - [Agent Communication](#agent-communication)
- [Performance Optimization](#performance-optimization)
  - [Caching Strategy](#caching-strategy)
  - [Async Operations](#async-operations)
- [Security Hardening](#security-hardening)
  - [Input Validation](#input-validation)
  - [Sandboxing](#sandboxing)
- [Custom Automation Rules](#custom-automation-rules)
  - [Rule Engine](#rule-engine)
- [Integration Points](#integration-points)
  - [External Services](#external-services)
  - [Custom Metrics](#custom-metrics)
class AdvancedHook:
    def __init__(self):
        self.project_root = self._find_project_root()
        self.claude_path = self.project_root / ".claude"
        self.config = self._load_config()
        
    def _find_project_root(self) -> Path:
        """Find project root by looking for .claude directory"""
        current = Path.cwd()
        while current != current.parent:
            if (current / ".claude").exists():
                return current
            current = current.parent
        return Path.cwd()
    
    def process(self, hook_input: dict) -> tuple[int, str]:
        """Main processing logic"""
        # Event routing
        event_handlers = {
            "UserPromptSubmit": self.handle_prompt,
            "PreToolUse": self.handle_pre_tool,
            "PostToolUse": self.handle_post_tool,
        }
        
        # Detect event type
        event_type = self._detect_event(hook_input)
        handler = event_handlers.get(event_type)
        
        if handler:
            return handler(hook_input)
        return 0, None
    
    def _detect_event(self, hook_input: dict) -> str:
        """Detect hook event type"""
        if "prompt" in hook_input:
            return "UserPromptSubmit"
        elif "toolName" in hook_input and "toolResult" not in hook_input:
            return "PreToolUse"
        elif "toolName" in hook_input and "toolResult" in hook_input:
            return "PostToolUse"
        return "Unknown"

# Hook entry point
if __name__ == "__main__":
    hook = AdvancedHook()
    hook_input = json.loads(sys.stdin.read())
    exit_code, output = hook.process(hook_input)
    
    if output:
        print(output)
    sys.exit(exit_code)
```

### State Management
```python
class StateManager:
    """Persistent state across hook invocations"""
    
    def __init__(self, state_file: Path):
        self.state_file = state_file
        self._state = self._load_state()
    
    def _load_state(self) -> dict:
        """Load state from file"""
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text())
            except:
                return {}
        return {}
    
    def get(self, key: str, default=None):
        """Get state value"""
        return self._state.get(key, default)
    
    def set(self, key: str, value):
        """Set state value"""
        self._state[key] = value
        self._save_state()
    
    def _save_state(self):
        """Persist state to file"""
        self.state_file.parent.mkdir(exist_ok=True)
        self.state_file.write_text(json.dumps(self._state, indent=2))
```

### Pattern Matching
```python
class PatternMatcher:
    """Advanced pattern matching with regex and scoring"""
    
    def __init__(self):
        self.patterns = {
            "security": {
                "regex": r"(api[_-]?key|secret|token|password|credential)",
                "score": 10,
                "flags": re.IGNORECASE
            },
            "performance": {
                "regex": r"(\d+)\s*(ms|MB|KB|seconds?)",
                "score": 5,
                "extract": True
            },
            "decision": {
                "regex": r"^(DECISION|RESOLVED|BREAKING):\s*(.+)",
                "score": 8,
                "capture_groups": True
            }
        }
    
    def match(self, text: str) -> list[dict]:
        """Match text against all patterns"""
        matches = []
        
        for name, config in self.patterns.items():
            regex = re.compile(config["regex"], config.get("flags", 0))
            
            for match in regex.finditer(text):
                result = {
                    "pattern": name,
                    "score": config["score"],
                    "match": match.group(0),
                    "position": match.span()
                }
                
                if config.get("capture_groups"):
                    result["groups"] = match.groups()
                
                matches.append(result)
        
        return sorted(matches, key=lambda x: x["score"], reverse=True)
```

## Multi-Agent Configuration

### Agent Isolation
```bash
# Each agent gets isolated workspace
export CLAUDE_AGENT_ID=agent1
export CLAUDE_AGENT_WORKSPACE=/tmp/claude-agent1

# Or in settings.json
{
  "agents": {
    "isolation": true,
    "workspace_prefix": "/tmp/claude-",
    "shared_state": "/shared/state"
  }
}
```

### Distributed Locking
```python
import fcntl
import time

class DistributedLock:
    """File-based distributed lock for multi-agent coordination"""
    
    def __init__(self, lock_file: Path, agent_id: str):
        self.lock_file = lock_file
        self.agent_id = agent_id
        self._lock_fd = None
    
    def acquire(self, timeout: float = 5.0) -> bool:
        """Try to acquire lock with timeout"""
        start = time.time()
        
        while time.time() - start < timeout:
            try:
                self._lock_fd = open(self.lock_file, 'w')
                fcntl.flock(self._lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                self._lock_fd.write(json.dumps({
                    "agent_id": self.agent_id,
                    "timestamp": time.time(),
                    "pid": os.getpid()
                }))
                self._lock_fd.flush()
                return True
            except BlockingIOError:
                time.sleep(0.1)
        
        return False
    
    def release(self):
        """Release the lock"""
        if self._lock_fd:
            fcntl.flock(self._lock_fd, fcntl.LOCK_UN)
            self._lock_fd.close()
            self._lock_fd = None
            try:
                os.unlink(self.lock_file)
            except:
                pass
```

### Agent Communication
```python
class AgentRegistry:
    """Central registry for agent coordination"""
    
    def __init__(self, registry_dir: Path):
        self.registry_dir = registry_dir
        self.registry_dir.mkdir(exist_ok=True)
    
    def register(self, agent_id: str, capabilities: dict):
        """Register agent with capabilities"""
        agent_file = self.registry_dir / f"{agent_id}.json"
        agent_file.write_text(json.dumps({
            "id": agent_id,
            "capabilities": capabilities,
            "status": "active",
            "last_seen": time.time()
        }))
    
    def discover(self, capability: str) -> list[str]:
        """Find agents with specific capability"""
        agents = []
        for agent_file in self.registry_dir.glob("*.json"):
            try:
                data = json.loads(agent_file.read_text())
                if capability in data.get("capabilities", []):
                    agents.append(data["id"])
            except:
                pass
        return agents
```

## Performance Optimization

### Caching Strategy
```python
class SmartCache:
    """Intelligent caching with TTL and size limits"""
    
    def __init__(self, max_size: int = 100, ttl: int = 3600):
        self.max_size = max_size
        self.ttl = ttl
        self._cache = {}
        self._access_times = {}
    
    def get(self, key: str):
        """Get from cache if valid"""
        if key in self._cache:
            if time.time() - self._access_times[key] < self.ttl:
                return self._cache[key]
            else:
                del self._cache[key]
                del self._access_times[key]
        return None
    
    def set(self, key: str, value):
        """Set in cache with LRU eviction"""
        if len(self._cache) >= self.max_size:
            # Evict least recently used
            lru_key = min(self._access_times, key=self._access_times.get)
            del self._cache[lru_key]
            del self._access_times[lru_key]
        
        self._cache[key] = value
        self._access_times[key] = time.time()
```

### Async Operations
```python
import asyncio
import concurrent.futures

class AsyncHookProcessor:
    """Process hooks asynchronously for better performance"""
    
    def __init__(self, max_workers: int = 4):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers)
    
    async def process_hooks_async(self, hooks: list, input_data: dict):
        """Process multiple hooks in parallel"""
        tasks = []
        
        for hook in hooks:
            task = asyncio.create_task(
                self._run_hook_async(hook, input_data)
            )
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
    
    async def _run_hook_async(self, hook_cmd: str, input_data: dict):
        """Run single hook asynchronously"""
        loop = asyncio.get_event_loop()
        
        return await loop.run_in_executor(
            self.executor,
            self._run_hook_sync,
            hook_cmd,
            input_data
        )
```

## Security Hardening

### Input Validation
```python
class SecureHookInput:
    """Validate and sanitize hook inputs"""
    
    ALLOWED_TOOLS = [
        "Read", "Write", "Edit", "MultiEdit",
        "Bash", "TodoWrite", "Grep", "Glob"
    ]
    
    MAX_INPUT_SIZE = 1024 * 1024  # 1MB
    
    @classmethod
    def validate(cls, hook_input: dict) -> tuple[bool, str]:
        """Validate hook input for security"""
        # Size check
        input_size = len(json.dumps(hook_input))
        if input_size > cls.MAX_INPUT_SIZE:
            return False, "Input too large"
        
        # Tool whitelist
        tool_name = hook_input.get("toolName")
        if tool_name and tool_name not in cls.ALLOWED_TOOLS:
            return False, f"Unknown tool: {tool_name}"
        
        # Path traversal check
        if "file_path" in hook_input.get("toolInput", {}):
            path = hook_input["toolInput"]["file_path"]
            if ".." in path or path.startswith("/"):
                return False, "Invalid file path"
        
        return True, "Valid"
```

### Sandboxing
```python
import resource
import signal

class HookSandbox:
    """Sandbox for hook execution"""
    
    @staticmethod
    def apply_limits():
        """Apply resource limits to hook process"""
        # Memory limit: 100MB
        resource.setrlimit(resource.RLIMIT_AS, (100 * 1024 * 1024, -1))
        
        # CPU time limit: 5 seconds
        resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
        
        # File descriptor limit
        resource.setrlimit(resource.RLIMIT_NOFILE, (50, 50))
        
        # Timeout handler
        signal.signal(signal.SIGALRM, HookSandbox._timeout_handler)
        signal.alarm(10)  # 10 second wall clock timeout
    
    @staticmethod
    def _timeout_handler(signum, frame):
        """Handle execution timeout"""
        print("Hook execution timeout")
        sys.exit(1)
```

## Custom Automation Rules

### Rule Engine
```python
class AutomationRule:
    """Define custom automation rules"""
    
    def __init__(self, name: str, condition: callable, action: callable):
        self.name = name
        self.condition = condition
        self.action = action
        self.enabled = True
    
    def evaluate(self, context: dict) -> bool:
        """Check if rule should fire"""
        if not self.enabled:
            return False
        
        try:
            return self.condition(context)
        except Exception:
            return False
    
    def execute(self, context: dict):
        """Execute rule action"""
        try:
            return self.action(context)
        except Exception as e:
            return f"Rule {self.name} failed: {e}"

# Example rules
rules = [
    AutomationRule(
        "large_file_warning",
        condition=lambda ctx: ctx.get("lines_changed", 0) > 500,
        action=lambda ctx: "⚠️ Large file change detected. Consider splitting into smaller commits."
    ),
    
    AutomationRule(
        "security_branch_check",
        condition=lambda ctx: "security" in ctx.get("branch", "") and ctx.get("tests_run", False) == False,
        action=lambda ctx: "🔐 Security branch detected. Running security scan..."
    )
]
```

## Integration Points

### External Services
```python
class ServiceIntegration:
    """Integrate with external services"""
    
    def __init__(self, config: dict):
        self.webhooks = config.get("webhooks", {})
        self.apis = config.get("apis", {})
    
    async def notify_webhook(self, event: str, data: dict):
        """Send webhook notification"""
        if event in self.webhooks:
            webhook_url = self.webhooks[event]
            
            async with aiohttp.ClientSession() as session:
                await session.post(
                    webhook_url,
                    json={
                        "event": event,
                        "timestamp": time.time(),
                        "data": data
                    },
                    timeout=5
                )
    
    def sync_to_external(self, service: str, data: dict):
        """Sync data to external service"""
        if service in self.apis:
            api_config = self.apis[service]
            # Implementation depends on service
            pass
```

### Custom Metrics
```python
class MetricsCollector:
    """Collect and aggregate custom metrics"""
    
    def __init__(self, metrics_dir: Path):
        self.metrics_dir = metrics_dir
        self.metrics_dir.mkdir(exist_ok=True)
        self.current_metrics = {}
    
    def record(self, metric_name: str, value: float, tags: dict = None):
        """Record a metric value"""
        timestamp = time.time()
        
        metric_file = self.metrics_dir / f"{metric_name}.jsonl"
        
        with open(metric_file, 'a') as f:
            f.write(json.dumps({
                "timestamp": timestamp,
                "value": value,
                "tags": tags or {}
            }) + '\n')
    
    def aggregate(self, metric_name: str, window: int = 3600) -> dict:
        """Aggregate metrics over time window"""
        metric_file = self.metrics_dir / f"{metric_name}.jsonl"
        
        if not metric_file.exists():
            return {}
        
        cutoff = time.time() - window
        values = []
        
        with open(metric_file) as f:
            for line in f:
                entry = json.loads(line)
                if entry["timestamp"] > cutoff:
                    values.append(entry["value"])
        
        if not values:
            return {}
        
        return {
            "count": len(values),
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values),
            "p95": sorted(values)[int(len(values) * 0.95)]
        }
```