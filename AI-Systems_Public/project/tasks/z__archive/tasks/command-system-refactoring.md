# Command System Refactoring - Project Task Document

**Project:** Command System Refactoring  
**Created:** 2025-01-19  
**Status:** In Progress (WP0 & WP1 Complete)  
**Total Estimated Effort:** 63-74 hours (includes DesktopCommanderMCP + MCP integrations)  
**Multi-Agent Support:** ✅ Fully concurrent with distributed locking and agent isolation

## Executive Summary

This project aims to simplify and streamline the Claude Code command system by reducing the number of commands, converting many to hooks, fixing session management issues, and removing redundant code. The work is divided into 7 work packages, with a Pre-Implementation phase for documentation baseline and Work Package 0 (DesktopCommanderMCP installation) as prerequisites.

**Key Changes:**
- Generate AI-friendly documentation baseline with Claude Conductor
- Install DesktopCommanderMCP for advanced automation capabilities
- Reduce from 10+ commands to just 3: `/memory`, `/save`, `/logic`
- Convert most functionality to automated hooks with process monitoring
- Add parallel development orchestration with full multi-agent support
- Fix session management 4-hour timeout bug
- Streamline CLAUDE.md documentation by 50%+
- Add intelligent task management system integrated with `/logic`
- Implement architecture review checkpoints with Make-It-Heavy
- **Enable safe concurrent execution by multiple Claude agents**

**Multi-Agent Benefits:**
- 🚀 **Parallel Development**: Multiple developers can work simultaneously
- 🔒 **No Conflicts**: Distributed locking prevents resource contention
- 📂 **Agent Isolation**: Each agent has its own workspace and state
- 🔄 **Automatic Coordination**: Agents communicate and coordinate seamlessly
- 💾 **Zero Data Loss**: All operations are atomic with automatic recovery
- 📊 **Better Resource Utilization**: Work distributed across available agents
- 🛡️ **Fault Tolerance**: Agent failures don't affect other agents

---

## Multi-Agent Concurrency Support

### Overview
This specification has been designed to support multiple Claude agents running concurrently in separate terminal instances without conflicts. All components implement distributed locking, agent isolation, and conflict resolution mechanisms.

### Agent Architecture

#### 1. Agent Identification
Every Claude agent instance receives a unique identifier:
```python
AGENT_ID = f"claude-{os.getpid()}-{uuid.uuid4().hex[:8]}"
# Example: "claude-12345-a1b2c3d4"
```

#### 2. Resource Isolation
Each agent operates with isolated resources:
```
.claude/
├── agents/
│   ├── {AGENT_ID}/           # Agent-specific workspace
│   │   ├── sessions/         # Isolated session files
│   │   ├── state/            # Agent state files
│   │   ├── cache/            # Agent-specific cache
│   │   └── logs/             # Agent execution logs
│   ├── shared/               # Shared resources (read-only)
│   │   ├── knowledge/        # Global knowledge base
│   │   └── hooks/            # Shared hook definitions
│   └── locks/                # Distributed lock files
│       ├── git.lock          # Git operation mutex
│       ├── memory.lock       # Memory system mutex
│       └── hooks/            # Per-hook execution locks
```

#### 3. Distributed Locking Mechanism
File-based locking with automatic cleanup:
```python
class DistributedLock:
    def __init__(self, resource_name, agent_id):
        self.lock_path = f".claude/agents/locks/{resource_name}.lock"
        self.agent_id = agent_id
        self.lock_timeout = 30  # seconds
        
    def acquire(self, timeout=5):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                # Atomic file creation with agent ID and timestamp
                with open(self.lock_path, 'x') as f:
                    lock_data = {
                        "agent_id": self.agent_id,
                        "timestamp": time.time(),
                        "pid": os.getpid()
                    }
                    json.dump(lock_data, f)
                return True
            except FileExistsError:
                # Check if lock is stale
                if self._is_lock_stale():
                    self._cleanup_stale_lock()
                else:
                    time.sleep(0.1)
        return False
    
    def _is_lock_stale(self):
        try:
            with open(self.lock_path, 'r') as f:
                lock_data = json.load(f)
            return time.time() - lock_data["timestamp"] > self.lock_timeout
        except:
            return True
```

#### 4. Conflict Resolution Strategies

| Resource Type | Conflict Strategy | Implementation |
|--------------|-------------------|----------------|
| **Git Operations** | Sequential queue | Git lock with operation queue |
| **File Edits** | Optimistic locking | Version checking before write |
| **Memory Updates** | Transaction-based | Atomic commits with rollback |
| **Hook Execution** | Priority-based queue | Agent-aware priority scheduling |
| **Session Files** | Agent isolation | Separate directories per agent |
| **Configuration** | Copy-on-write | Agent-specific overlays |

#### 5. Agent Communication Protocol
Agents communicate through a lightweight message passing system:
```python
# Message queue for agent coordination
.claude/agents/messages/
├── broadcast/        # All agents receive
├── {AGENT_ID}/      # Agent-specific messages
└── orchestrator/    # Central coordinator messages

# Message format
{
    "from": "claude-12345-a1b2c3d4",
    "to": "broadcast",
    "type": "status_update",
    "payload": {
        "task": "hook_execution",
        "status": "completed",
        "resource": "security-scan-hook"
    },
    "timestamp": 1737303600
}
```

### Concurrency Safety Guarantees

1. **No Data Loss**: All operations use atomic writes with backup
2. **No Deadlocks**: Timeout-based lock acquisition with automatic cleanup
3. **Progress Guarantee**: At least one agent makes progress (livelock prevention)
4. **Consistency**: Eventual consistency for all shared resources
5. **Isolation**: Agent failures don't affect other agents

### Agent Lifecycle Management

```python
class AgentLifecycle:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.workspace = f".claude/agents/{agent_id}"
        
    def startup(self):
        # 1. Create agent workspace
        os.makedirs(self.workspace, exist_ok=True)
        
        # 2. Register with coordinator
        self._register_agent()
        
        # 3. Initialize agent-specific resources
        self._init_workspace()
        
        # 4. Start heartbeat
        self._start_heartbeat()
        
    def shutdown(self):
        # 1. Complete pending operations
        self._finish_pending_work()
        
        # 2. Release all locks
        self._release_locks()
        
        # 3. Archive agent data
        self._archive_workspace()
        
        # 4. Deregister from coordinator
        self._deregister_agent()
```

### Performance Considerations

1. **Lock Contention**: Minimize lock hold time (< 100ms target)
2. **Queue Processing**: Batch operations where possible
3. **Cache Efficiency**: Agent-local caches with shared invalidation
4. **Resource Quotas**: Per-agent limits to prevent resource exhaustion

---

## Current State Analysis

### Existing System Overview

The current system has 10 manual commands and 4 active hooks with varying automation levels:

| Feature | Current Implementation | Automation Level | User Interaction Required |
|---------|----------------------|------------------|---------------------------|
| **Mode Management** | mode-suggestion-hook.py | Semi-Auto | Shows suggestion, user types `/mode [mode]` |
| **Quality Checks** | quality-hook.py | Fully Auto (warnings) / Semi-Auto (critical) | None for warnings; blocks on violations |
| **Memory Context** | memory-context-hook.py | Fully Auto | Shows hints when keywords detected |
| **Session Management** | session-hook.py | Fully Auto | None - creates/archives automatically |
| **Workflow** | `/workflow` command | Manual | User must type command |
| **Testing** | `/test` command | Manual | User must type command |
| **Memory Search** | `/memory` command | Manual | User must type command + query |
| **PR Docs** | `/pr` command | Manual | User must type command |
| **Security** | `/security` command | Manual | User must type command |
| **Context** | `/context` command | Manual | User must type command |
| **Notebook** | `/notebook` command | Manual | User must type command |

### Automation Potential Analysis

Based on usage patterns and technical feasibility:

**High Automation Potential** (can be fully automated):
- Workflow → Triggers on task complexity
- Testing → Triggers on file changes
- Security → Triggers on sensitive patterns
- Context → Updates automatically
- Notebook → Triggers on session events

**Partial Automation** (requires some user input):
- PR Documentation → Can generate, but needs user review
- Mode → Already semi-automated (working well)

**Must Remain Manual** (requires explicit user input):
- Memory operations → User-specific search queries
- Save/Session → Explicit user decision to archive
- Logic/Help → User requesting information

---

## Pre-Implementation: Documentation & Analysis Baseline

### Objective
Generate comprehensive AI-friendly documentation baseline before refactoring to inform pattern extraction and documentation streamlining efforts.

### Claude Conductor Baseline (1-2 hours)
1. **Installation & Setup**
   - Install Claude Conductor via npm/npx
   - Configure for the anobel.nl project
   - Run initial codebase scan (2-3 seconds quick scan)

2. **Documentation Generation**
   - Generate ARCHITECTURE.md for system overview
   - Generate CLAUDE.md with AI-optimized patterns
   - Generate BUILD.md with setup instructions
   - Extract error patterns and common issues

3. **Pattern Extraction**
   - Identify code patterns for `pattern-extraction-hook.py`
   - Extract line number reference system
   - Capture searchable anchor patterns
   - Document task templates structure

4. **Integration Analysis**
   - Compare with existing CLAUDE.md structure
   - Identify features to incorporate
   - Use as baseline for 50% reduction goal
   - Extract AI-friendly documentation patterns

### Benefits
- **Line number references**: `file:123-145` for precise code navigation
- **Searchable anchors**: HTML-style anchors for quick jumping
- **Error tracking**: Structured error ledger format
- **Task templates**: Reusable patterns for common tasks
- **Keywords sections**: Improved AI discoverability
- **Anti-patterns**: Clear ❌ markers for what to avoid

### Deliverables
- [ ] Generated documentation files in `.claude/conductor-baseline/`
- [ ] Pattern analysis report for WP3 documentation streamlining
- [ ] Feature comparison matrix with existing system
- [ ] Integration recommendations document

### Estimated Effort: 1-2 hours

---

## Work Package 0: DesktopCommanderMCP Installation & Configuration

### Objective
Install and configure DesktopCommanderMCP as a foundational prerequisite to enable advanced automation capabilities required by the subsequent work packages.

### Background
DesktopCommanderMCP provides critical capabilities that enable the advanced automation described in this refactoring:
- **Process Management**: Start, monitor, and control long-running processes
- **In-Memory Execution**: Run Python/Node.js/R code without creating files
- **Advanced Search**: Ripgrep integration for ultra-fast code search
- **Surgical Edits**: `edit_block` for precise code modifications
- **Audit Logging**: Automatic logging of all operations

### Deliverables
1. **Installation in .claude.json**
   - Add DesktopCommanderMCP configuration to `/Users/michel_kerkmeester/.claude.json`
   - Use npx method for automatic updates (consistent with existing MCPs)
   - Configuration entry:
     ```json
     "desktop-commander": {
       "command": "npx",
       "args": [
         "-y",
         "@wonderwhy-er/desktop-commander"
       ],
       "env": {}
     }
     ```

2. **Security Configuration**
   - Restrict file operations to project directory only
   - Configure appropriate shell (zsh for macOS)
   - Set file operation limits
   - Disable telemetry if desired
   - Configuration commands:
     ```javascript
     set_config_value({ 
       "key": "allowedDirectories", 
       "value": ["/Users/michel_kerkmeester/AI & Dev/Websites/• anobel.nl"] 
     })
     set_config_value({ "key": "defaultShell", "value": "/bin/zsh" })
     set_config_value({ "key": "fileWriteLineLimit", "value": 100 })
     set_config_value({ "key": "telemetryEnabled", "value": false })
     ```

3. **Verification & Testing**
   - Test all Desktop Commander tools
   - Verify audit logging functionality
   - Confirm process management capabilities
   - Test file operations within allowed directories

### Acceptance Criteria
- [x] DesktopCommanderMCP entry added to .claude.json
- [ ] Claude Desktop restarted and MCP loaded successfully
- [ ] Security configuration completed (allowed directories set)
- [ ] All Desktop Commander tools verified working
- [ ] Audit logging confirmed operational
- [ ] Process management tested with sample commands

### Technical Integration Points
1. **Enhanced Hook Infrastructure** (WP1)
   - Hooks will use `start_process` for execution monitoring
   - Real-time output streaming via `read_process_output`
   - Performance tracking with `get_usage_stats`

2. **Automated Testing** (WP1)
   - Tests run via `start_process` with live monitoring
   - Auto-fix capabilities using `edit_block`
   - Parallel test execution support

3. **Security Scanning** (WP1)
   - Leverage `search_code` with ripgrep patterns
   - Instant pattern matching across codebase
   - Real-time blocking of sensitive operations

4. **Documentation Generation** (WP3)
   - Use `search_code` to find all functions/classes
   - Generate docs without temporary files
   - Execute analysis in-memory

### Estimated Effort: 2-3 hours
- Installation & configuration: 1 hour
- Security setup & testing: 1 hour
- Integration verification: 0.5-1 hour

### Dependencies
- Must be completed before any other work packages
- Enables advanced automation in WP1-WP5
- Required for process-aware hook infrastructure

---

## Work Package 1: Command Reduction & Hook Conversion System

### Objective
Transform the current 10+ command system into a lean 3-command structure by converting most functionality to automated hooks.

### Deliverables
1. **Core Command Retention**
   - `/memory` - Memory management (search, status, manual capture)
   - `/save` - Session management (new, list, archive) [renamed from /session]
   - `/logic` - System logic, help & hook management [merged /help + /hook]

2. **Hook Conversions**
   
   **Fully Automated Hooks** (no user interaction - powered by DesktopCommanderMCP):
   - Convert `/workflow` → `workflow-automation-hook.py`
     - Triggers: Query complexity > threshold, 3+ steps detected
     - Action: Automatically uses Sequential Thinking
     - Desktop Commander: Uses `search_code` for complexity analysis
   - Convert `/test` → Enhanced `quality-check-hook.py` 
     - Triggers: Already active on file changes
     - Enhancement: Add auto-test execution for critical paths
     - Desktop Commander: `start_process` for test execution, `edit_block` for auto-fix
   - Convert `/security` → `security-scan-hook.py`
     - Triggers: API keys, secrets, sensitive patterns detected
     - Action: Block operations, show warnings
     - Desktop Commander: `search_code` with ripgrep patterns for instant scanning
   - Convert `/context` → `context-management-hook.py`
     - Triggers: Every N operations or time interval
     - Action: Auto-save context state
     - Desktop Commander: Process state tracking and persistence
   - Convert `/notebook` → `pattern-extraction-hook.py`
     - Triggers: Session save, significant insights detected
     - Action: Extract and categorize patterns with Gemini
     - Desktop Commander: In-memory Python execution for analysis
   
   **Semi-Automated Hooks** (minimal user interaction):
   - Convert `/pr` → `documentation-generation-hook.py`
     - Triggers: Git operations, deployment prep
     - Action: Generate docs, prompt for review
   - Keep `/mode` → Already exists as `mode-suggestion-hook.py`
     - Current behavior is optimal
   
   **New Hooks**:
   - Create → `task-management-hook.py` (for task lifecycle)
     - Triggers: Todo completion, task mentions
     - Action: Suggest task state changes

3. **Hook Infrastructure**
   - Unified hook configuration in `.claude/settings.json`
   - Hook enable/disable toggles via `/logic hooks [enable|disable] [name]`
   - Hook execution logging and debugging
   - Hook status dashboard in `/logic hooks status`
   - **Hook Priority System**:
     - Priority levels: Critical (1) > Quality (2) > Workflow (3) > Context (4)
     - Conflict resolution for simultaneous triggers
     - Execution order management
     - Deduplication of similar actions
   - **Hook Concurrency Metadata**:
     ```python
     # Hook definition with concurrency settings
     class HookMetadata:
         name: str
         priority: int
         concurrent_safe: bool = True  # Can multiple agents run simultaneously
         exclusive_resources: List[str] = []  # Resources requiring locks
         max_parallel: int = None  # Max parallel executions (None = unlimited)
         
     # Example hook configurations
     HOOK_CONFIGS = {
         "workflow-automation": HookMetadata(
             name="workflow-automation",
             priority=3,
             concurrent_safe=True,
             max_parallel=10
         ),
         "security-scan": HookMetadata(
             name="security-scan",
             priority=1,
             concurrent_safe=False,  # Exclusive access to scan results
             exclusive_resources=["security-report.json"]
         ),
         "git-operations": HookMetadata(
             name="git-operations",
             priority=2,
             concurrent_safe=False,  # Git operations must be sequential
             exclusive_resources=["git"]
         )
     }
     ```

### Acceptance Criteria
- [x] All hooks execute automatically based on context
- [x] Manual override available via `/logic hooks disable [name]`
- [x] Zero regression in functionality
- [x] Performance impact < 100ms per hook (< 200ms total)
- [ ] All hooks documented in `hooks-in-cc.md`
- [x] `/logic` command provides unified access to all system functions
- [x] Hook priority system prevents conflicts
- [x] Async execution for non-blocking operations

### Technical Approach (Enhanced with DesktopCommanderMCP + Multi-Agent Support)
```python
# Hook execution with priority, performance optimization, process monitoring, and multi-agent concurrency
class ConcurrentProcessAwareHookManager:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.hook_cache = {}  # Agent-specific cache
        self.priority_queue = PriorityQueue()
        self.desktop_commander = DesktopCommanderInterface()
        self.process_sessions = {}
        self.lock_manager = DistributedLockManager(agent_id)
        
    async def trigger_hooks(self, context):
        # Add agent context
        context['agent_id'] = self.agent_id
        
        # Collect applicable hooks
        hooks = self.get_applicable_hooks(context)
        
        # Sort by priority and deduplicate
        for hook in self.deduplicate(hooks):
            # Check if hook can run concurrently or needs exclusive access
            if hook.concurrent_safe:
                if hook.is_async:
                    asyncio.create_task(self.execute_with_monitoring(hook, context))
                else:
                    self.priority_queue.put((hook.priority, hook))
            else:
                # Queue for exclusive execution
                await self.queue_exclusive_hook(hook, context)
        
        # Execute in priority order with process monitoring
        while not self.priority_queue.empty():
            _, hook = self.priority_queue.get()
            await self.execute_with_monitoring(hook, context)
    
    async def execute_with_monitoring(self, hook, context):
        # Acquire lock if hook requires exclusive access
        lock = None
        if not hook.concurrent_safe:
            lock = self.lock_manager.acquire_lock(f"hook_{hook.name}")
            if not lock:
                # Queue for retry
                await self.queue_hook_retry(hook, context)
                return
        
        try:
            # Start hook as a process for real-time monitoring
            session_id = await self.desktop_commander.start_process(
                f"python3 {hook.path} --agent-id {self.agent_id}",
                timeout=30000,
                env={"CLAUDE_AGENT_ID": self.agent_id}
            )
            self.process_sessions[f"{self.agent_id}_{hook.name}"] = session_id
            
            # Monitor output stream
            output = await self.desktop_commander.read_process_output(session_id)
            
            # Update agent-specific cache
            cache_key = f"{self.agent_id}_{hook.name}"
            self.hook_cache[cache_key] = output
            
            # Broadcast hook completion to other agents
            await self.broadcast_hook_completion(hook.name, output)
            
            stats = await self.desktop_commander.get_usage_stats()
            return process_hook_output(output, stats)
        finally:
            if lock:
                self.lock_manager.release_lock(f"hook_{hook.name}")
    
    async def queue_exclusive_hook(self, hook, context):
        # Add to distributed queue for exclusive hooks
        queue_path = f".claude/agents/queues/hooks/{hook.name}.queue"
        async with self.lock_manager.atomic_file_operation(queue_path):
            queue_entry = {
                "agent_id": self.agent_id,
                "hook": hook.name,
                "context": context,
                "timestamp": time.time(),
                "priority": hook.priority
            }
            await self.append_to_queue(queue_path, queue_entry)

# Performance optimizations
- Lazy loading for hook modules
- Shared git status cache across hooks  
- Batched file operations
- Background pre-computation for predictable triggers

# /logic command structure
/logic              # Interactive menu
├── system         # System management
│   ├── hooks      # Hook configuration
│   ├── settings   # Global settings
│   └── diagnostics # Performance metrics
├── tasks          # Task management
├── help           # Documentation
└── debug          # Troubleshooting
```

### Estimated Effort: 12-14 hours ✅ COMPLETED
- Hook implementation: 6 hours ✅
- `/logic` command development: 2 hours ✅
- Hook priority system: 2 hours ✅
- Testing & integration: 3 hours (partial)
- Documentation: 1 hour (pending)

### Automation Matrix

| Feature | Before | After | Automation Type | User Action |
|---------|--------|-------|-----------------|-------------|
| **Workflow** | Manual `/workflow` | Auto hook | Fully Automated | None - triggers on complexity |
| **Testing** | Manual `/test` | Auto hook | Fully Automated | Sees suggestions only |
| **Security** | Manual `/security` | Auto hook | Fully Automated | Blocked on violations |
| **Context** | Manual `/context` | Auto hook | Fully Automated | None - saves automatically |
| **Notebook** | Manual `/notebook` | Auto hook | Fully Automated | None - extracts on events |
| **PR Docs** | Manual `/pr` | Semi-auto hook | Semi-Automated | Reviews generated docs |
| **Mode** | Semi-auto hook | No change | Semi-Automated | Accepts/rejects suggestion |
| **Session** | Auto hook | No change | Fully Automated | None - 4hr cycle |
| **Memory** | Manual `/memory` | Stays manual | Manual Required | Searches, captures |
| **Save** | Manual `/session` | Manual `/save` | Manual Required | Explicit save decision |
| **Logic** | Manual `/help` | Manual `/logic` | Manual Required | Requests help/config |

**Automation Summary**: 
- 7 features become fully automated
- 2 remain semi-automated 
- 3 must stay manual (require user input)

---

## Work Package 2: Session Management Fixes & Notebook Mode (Multi-Agent Safe)

### Objective
Fix session management issues (with new `/save` command) and upgrade notebook extraction to intelligent mode using Gemini integration, with full multi-agent concurrency support.

### Deliverables
1. **Session Management Fixes with Agent Isolation**
   - Update all references from `/session` to `/save`
   - Fix 4-hour timeout bug in `session-management-hook.py`
   - Implement proper session state persistence with agent isolation
   - Add session recovery mechanism with agent awareness
   - Fix archive rotation logic with distributed locking
   - **Agent-Specific Session Structure**:
     ```
     .claude/agents/{AGENT_ID}/sessions/
     ├── current/
     │   └── YYYY-MM-DD-HHMMSS-{AGENT_ID}-description.md
     ├── archived/
     │   └── [older sessions]
     └── .session-state.json  # Agent-specific state
     
     .claude/sessions/  # Global session registry
     ├── registry.json  # All active sessions across agents
     └── shared/        # Shared session data (read-only)
     ```

2. **Notebook Mode Upgrade**
   - Convert `/notebook` to automated hook with Gemini
   - Automatic pattern detection and extraction
   - Smart categorization into facts/patterns/constraints
   - Incremental updates to knowledge files
   - Triggered by session saves or manual `/logic notebook`

3. **Session Enhancement**
   - Auto-generate session summaries on save
   - Link sessions to memory captures
   - Session search functionality via `/save search [query]`
   - Session metrics dashboard via `/save stats`

### Acceptance Criteria
- [x] Sessions persist correctly across 4-hour boundaries (fixed by another agent)
- [x] `/save` command works for all session operations (renamed by another agent)
- [ ] No data loss during archival
- [x] Notebook hook extracts patterns with 90%+ accuracy (already existed)
- [ ] Knowledge files update incrementally (no duplicates)
- [ ] Session search returns relevant results

### Technical Approach
```python
# Updated session commands with agent awareness
/save              # Save and archive current agent's session
/save new [desc]   # Start new session for current agent
/save list         # List all sessions (agent's + global view)
/save list --all   # List sessions from all agents
/save search [q]   # Search session content across all agents
/save stats        # Session statistics per agent

# Agent-aware session manager
class MultiAgentSessionManager:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.session_path = f".claude/agents/{agent_id}/sessions"
        self.global_registry = ".claude/sessions/registry.json"
        self.lock_manager = DistributedLockManager(agent_id)
        
    async def create_session(self, description=""):
        timestamp = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        session_name = f"{timestamp}-{self.agent_id}-{description}.md"
        
        # Create agent-specific session
        session_file = f"{self.session_path}/current/{session_name}"
        
        # Update global registry with lock
        async with self.lock_manager.atomic_file_operation(self.global_registry):
            registry = await self.load_registry()
            registry["active_sessions"][self.agent_id] = {
                "file": session_file,
                "started": timestamp,
                "description": description
            }
            await self.save_registry(registry)
            
        return session_file
    
    async def archive_session(self):
        # Agent-specific archival with global registry update
        current_sessions = glob.glob(f"{self.session_path}/current/*.md")
        if not current_sessions:
            return
            
        async with self.lock_manager.atomic_file_operation(self.global_registry):
            for session in current_sessions:
                archive_path = session.replace("/current/", "/archived/")
                shutil.move(session, archive_path)
                
            # Update registry
            registry = await self.load_registry()
            if self.agent_id in registry["active_sessions"]:
                registry["archived_sessions"].append(registry["active_sessions"][self.agent_id])
                del registry["active_sessions"][self.agent_id]
            await self.save_registry(registry)

# Notebook automation with Gemini and concurrency
async def extract_patterns_hook(session_content, agent_id):
    if len(session_content) > MIN_CONTENT_THRESHOLD:
        analysis = await gemini_analyze(session_content, 
            prompt="Extract code patterns, facts, and constraints",
            context={"agent_id": agent_id})
        
        # Use distributed lock for knowledge file updates
        lock_manager = DistributedLockManager(agent_id)
        async with lock_manager.atomic_file_operation(".claude/project/knowledge"):
            await update_knowledge_files(categorize_insights(analysis))
```

### Estimated Effort: 8-10 hours
- Session fixes & `/save` implementation: 3 hours
- Notebook automation hook: 4 hours
- Testing & refinement: 1-3 hours

---

## Work Package 3: CLAUDE.md Documentation Streamlining

### Objective
Reduce CLAUDE.md from 10+ sections to 5 focused sections while maintaining all critical information and updating for new command structure.

### Deliverables
1. **Consolidated Structure**
   ```
   1. STARTUP & STATUS (merged sections 1 & 2)
   2. TECHNICAL RULES (merged sections 3 & constraints)
   3. COMMANDS (simplified to just /memory, /save, /logic)
   4. AUTOMATION (hooks, memory, sessions - all automatic)
   5. PRODUCTION CHECKLIST (security & deployment)
   ```

2. **Content Migration**
   - Update all command references to new names
   - Move verbose explanations to `/logic help` system
   - Create quick reference cards
   - Implement progressive disclosure
   - Add visual indicators and emojis

3. **Dynamic Content**
   - Auto-generated command list from available hooks
   - Live status indicators from hook states
   - Context-aware help suggestions
   - Minimal manual command documentation

### Acceptance Criteria
- [ ] Document < 50% original size
- [ ] All references updated to new commands
- [ ] No loss of critical information
- [ ] Improved readability score
- [ ] Load time < 100ms
- [ ] Help content accessible via `/logic help`

### Technical Approach
```markdown
## 3. COMMANDS (Simplified)
Just 3 commands - everything else runs automatically:

- `/memory` - Knowledge graph management
- `/save` - Session management  
- `/logic` - System help & configuration

Most features now run automatically via hooks.
Use `/logic hooks status` to see what's active.

[Previous 10+ commands are now automatic hooks]
```

### Estimated Effort: 6-8 hours
- Content restructuring: 3 hours
- Command reference updates: 2 hours
- Testing & validation: 1-3 hours

---

## Work Package 4: Codebase Cleanup & Redundancy Removal

### Objective
Remove duplicate files, obsolete code, and reorganize the `.claude` directory structure to support the new streamlined system.

### Deliverables
1. **File Consolidation**
   - Remove old command implementation files
   - Merge duplicate hook implementations
   - Consolidate configuration files
   - Archive deprecated features
   - Update all imports for new structure

2. **Directory Restructure**
   ```
   .claude/
   ├── hooks/           # All hooks in one place
   │   ├── workflow/
   │   ├── quality/
   │   ├── security/
   │   └── ...
   ├── knowledge/       # Facts, patterns, constraints
   ├── sessions/        # Current and archived
   ├── config/          # All configuration files
   │   ├── settings.json
   │   ├── hook-config.json
   │   └── ...
   └── docs/            # Documentation
       ├── hooks-in-cc.md
       └── logic-help/  # Help content for /logic
   ```

3. **Code Optimization**
   - Remove dead code paths from old commands
   - Consolidate utility functions
   - Optimize import statements
   - Implement shared hook libraries
   - Create hook base classes

### Acceptance Criteria
- [ ] 30%+ reduction in file count
- [ ] No broken dependencies
- [ ] All paths updated in code
- [ ] Improved directory navigation
- [ ] Full test suite passes
- [ ] All old command code removed

### Technical Approach
```bash
# Cleanup script
# Remove old command files
rm -rf .claude/commands/
rm -rf .claude/logic/*/commands/

# Update imports
find .claude -name "*.py" -exec sed -i 's|/session|/save|g' {} \;
find .claude -name "*.py" -exec sed -i 's|/help|/logic|g' {} \;

# Consolidate hooks
mv .claude/logic/*/hooks/* .claude/hooks/
```

### Estimated Effort: 8-10 hours
- File analysis & mapping: 2 hours
- Consolidation & cleanup: 4 hours
- Testing & validation: 2-4 hours

---

## Work Package 5: Task Management System (Multi-Agent Coordination)

### Objective
Create an intelligent task management system integrated with `/logic` that automates task lifecycle tracking and provides clear visibility into project progress, with support for multiple agents working on different tasks concurrently.

### Deliverables
1. **Task Folder Restructure with Agent Support**
   ```
   .claude/project/tasks/
   ├── suggestions/           # New plans/ideas (global pool)
   ├── active/               # Currently working tasks
   │   ├── {AGENT_ID}-current.md  # Agent-specific active tasks
   │   └── .task-registry.json     # Task assignment registry
   ├── completed/            # Finished tasks with timestamps
   │   └── YYYY-MM-DD-{AGENT_ID}-taskname.md
   ├── task-manager.py       # Automation script
   └── locks/                # Task assignment locks
       └── task-assignment.lock
   ```

2. **Task Management Hook**
   - `task-management-hook.py` - Monitors task lifecycle
   - Auto-moves tasks between folders based on status
   - Integrates with TodoWrite for progress tracking
   - Archives completed tasks with timestamps
   - Enforces single active task constraint

3. **Task Commands via `/logic tasks`**
   ```
   /logic tasks              # Task management menu
   /logic tasks list         # Show all tasks by folder
   /logic tasks new [name]   # Create new task in suggestions
   /logic tasks activate [name]  # Move from suggestions to active
   /logic tasks status       # Show active task progress (from TodoWrite)
   /logic tasks complete     # Archive current active task
   /logic tasks search [query]   # Search across all tasks
   ```

4. **Integration Features**
   - Task templates for common project types
   - Progress visualization from TodoWrite data
   - Task status in startup protocol display
   - Automatic task rotation based on completion
   - Task history and metrics tracking

### Acceptance Criteria
- [ ] Each agent can have one active task (no conflicts between agents)
- [ ] Tasks automatically move between folders based on lifecycle
- [ ] TodoWrite integration shows real-time progress per agent
- [ ] Completed tasks are timestamped and archived with agent ID
- [ ] Task search works across all folders and agents
- [ ] Task status appears in startup display showing all active tasks
- [ ] Zero data loss during task transitions
- [ ] Task assignment is atomic (no double assignment)

### Technical Approach
```python
# Multi-agent task lifecycle management
class MultiAgentTaskManager:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.folders = {
            'suggestions': '.claude/project/tasks/suggestions/',
            'active': '.claude/project/tasks/active/',
            'completed': '.claude/project/tasks/completed/'
        }
        self.registry_path = '.claude/project/tasks/active/.task-registry.json'
        self.lock_manager = DistributedLockManager(agent_id)
    
    async def activate_task(self, task_name):
        # Atomic task assignment with distributed lock
        async with self.lock_manager.atomic_file_operation(self.registry_path):
            registry = await self.load_registry()
            
            # Check if task already assigned
            if task_name in registry.get('assigned_tasks', {}):
                assigned_to = registry['assigned_tasks'][task_name]['agent_id']
                if assigned_to != self.agent_id:
                    raise ValueError(f"Task already assigned to agent {assigned_to}")
            
            # Check if agent has active task
            agent_tasks = [t for t, info in registry.get('assigned_tasks', {}).items() 
                          if info['agent_id'] == self.agent_id]
            if agent_tasks:
                raise ValueError(f"Agent already has active task: {agent_tasks[0]}")
            
            # Assign task to agent
            source_path = f"{self.folders['suggestions']}{task_name}.md"
            dest_path = f"{self.folders['active']}{self.agent_id}-current.md"
            
            shutil.move(source_path, dest_path)
            
            # Update registry
            registry['assigned_tasks'][task_name] = {
                'agent_id': self.agent_id,
                'assigned_at': time.time(),
                'file': dest_path
            }
            await self.save_registry(registry)
    
    async def complete_task(self):
        # Archive with timestamp and agent ID
        timestamp = datetime.now().strftime('%Y-%m-%d')
        
        async with self.lock_manager.atomic_file_operation(self.registry_path):
            registry = await self.load_registry()
            
            # Find agent's active task
            agent_task = None
            for task_name, info in registry.get('assigned_tasks', {}).items():
                if info['agent_id'] == self.agent_id:
                    agent_task = (task_name, info)
                    break
            
            if not agent_task:
                raise ValueError("No active task for agent")
            
            task_name, task_info = agent_task
            source_path = task_info['file']
            dest_path = f"{self.folders['completed']}{timestamp}-{self.agent_id}-{task_name}.md"
            
            shutil.move(source_path, dest_path)
            
            # Update registry
            del registry['assigned_tasks'][task_name]
            registry['completed_tasks'].append({
                'task': task_name,
                'agent_id': self.agent_id,
                'completed_at': time.time(),
                'file': dest_path
            })
            await self.save_registry(registry)

# Hook integration with agent awareness
def on_todo_complete(todo_data, agent_id):
    if all_todos_complete():
        suggest_task_completion(agent_id)
```

### Estimated Effort: 6-8 hours
- Task manager implementation: 3 hours
- `/logic tasks` commands: 2 hours
- Hook integration & testing: 1-3 hours

---

## Work Package 6: Parallel Development Orchestration (Enhanced Multi-Agent System)

### Objective
Implement advanced parallel agent execution capabilities with full coordination, building upon the multi-agent concurrency infrastructure to enable simultaneous development of multiple work packages.

### Background
This work package leverages the distributed locking and agent isolation mechanisms introduced earlier to create a sophisticated parallel development system. Unlike simple concurrent execution, this provides orchestrated parallel development with intelligent work distribution.

### Deliverables
1. **Parallel Agent Infrastructure**
   - Create `parallel-agent-hook.py` for agent orchestration
   - Leverage DesktopCommanderMCP's process management
   - Spawn specialized Task agents per work package
   - Implement agent communication protocol
   - Add agent state tracking and recovery

2. **Git Worktree Integration**
   ```bash
   # Automatic worktree creation per agent
   git worktree add -b wp1-hooks .claude/agents/wp1
   git worktree add -b wp2-session .claude/agents/wp2
   # ... for each work package
   ```
   - Isolated development branches per work package
   - Automatic merge coordination system
   - Conflict detection and resolution
   - Progress synchronization across worktrees

3. **Command Structure**
   ```
   /logic tasks parallel              # Parallel execution menu
   ├── start [wp1,wp2,...]           # Launch specific agents
   ├── start all                     # Launch all available agents
   ├── status                        # Monitor all agent progress
   ├── logs [agent]                  # View agent-specific logs
   ├── pause [agent]                 # Pause specific agent
   ├── resume [agent]                # Resume paused agent
   ├── merge [agent]                 # Merge agent's work
   └── cleanup                       # Remove worktrees and cleanup
   ```

4. **Agent Types & Specialization**
   - **Development Agents**: Focus on implementation
   - **Review Agents**: Validate and test changes
   - **Integration Agents**: Handle merging and conflicts
   - **Documentation Agents**: Update docs in parallel

### Technical Approach
```python
# Enhanced parallel agent orchestrator with full concurrency support
class EnhancedParallelAgentOrchestrator:
    def __init__(self, orchestrator_id="main"):
        self.orchestrator_id = orchestrator_id
        self.desktop_commander = DesktopCommanderInterface()
        self.agents = {}
        self.worktrees = {}
        self.message_queue = MessageQueue()
        self.coordinator_socket = "/tmp/claude-orchestrator.sock"
        self.work_distribution = WorkDistributionEngine()
        
    async def spawn_agent(self, work_package_id, agent_type="development"):
        # Create isolated worktree
        worktree_path = f".claude/agents/{work_package_id}"
        await self.create_worktree(work_package_id, worktree_path)
        
        # Start agent process with Desktop Commander
        agent_script = f"""
        cd {worktree_path}
        python3 .claude/agents/agent-runner.py \\
            --package {work_package_id} \\
            --type {agent_type} \\
            --orchestrator-socket /tmp/claude-orchestrator.sock
        """
        
        session_id = await self.desktop_commander.start_process(
            agent_script,
            timeout=None  # Long-running process
        )
        
        # Create unique agent ID for this work package
        agent_id = f"claude-{work_package_id}-{agent_type}-{uuid.uuid4().hex[:8]}"
        
        self.agents[work_package_id] = {
            "agent_id": agent_id,
            "session_id": session_id,
            "type": agent_type,
            "worktree": worktree_path,
            "status": "running",
            "progress": 0,
            "lock_holdings": [],
            "message_buffer": []
        }
        
        # Register agent in global coordinator
        await self.register_agent_globally(agent_id, work_package_id)
        
    async def coordinate_merge(self, agent_ids):
        # Intelligent merge coordination
        for agent_id in agent_ids:
            agent = self.agents[agent_id]
            
            # Check for conflicts
            conflicts = await self.check_conflicts(agent["worktree"])
            
            if conflicts:
                # Spawn integration agent to resolve
                await self.spawn_agent(
                    f"{agent_id}-integration",
                    "integration"
                )
            else:
                # Direct merge
                await self.merge_agent_work(agent_id)

# Enhanced agent runner with coordination
class CoordinatedTaskAgent:
    def __init__(self, agent_id, work_package, orchestrator):
        self.agent_id = agent_id
        self.work_package = work_package
        self.orchestrator = orchestrator
        self.todo_items = []
        self.lock_manager = DistributedLockManager(agent_id)
        self.health_check_interval = 30  # seconds
        
    async def run(self):
        # Initialize agent workspace
        await self.initialize_workspace()
        
        # Start health check daemon
        asyncio.create_task(self.health_check_daemon())
        
        # Load and claim work package tasks
        await self.load_and_claim_tasks()
        
        # Execute tasks with coordination
        for task in self.todo_items:
            # Check for dependencies on other agents
            await self.wait_for_dependencies(task)
            
            # Execute with progress reporting
            await self.execute_task(task)
            await self.report_progress()
            
            # Notify dependent agents
            await self.notify_dependents(task)
            
        # Signal completion with merge readiness
        await self.orchestrator.agent_complete(self.agent_id, self.work_package)
    
    async def health_check_daemon(self):
        """Maintain agent liveness in coordinator"""
        while self.active:
            await self.orchestrator.heartbeat(self.agent_id)
            await asyncio.sleep(self.health_check_interval)

# Work distribution engine
class WorkDistributionEngine:
    def __init__(self):
        self.dependency_graph = {}
        self.agent_capabilities = {}
        self.work_queue = PriorityQueue()
        
    def analyze_work_packages(self, work_packages):
        """Build dependency graph and optimal distribution plan"""
        for wp in work_packages:
            dependencies = self.extract_dependencies(wp)
            self.dependency_graph[wp.id] = dependencies
            
        return self.create_distribution_plan()
    
    def create_distribution_plan(self):
        """Create optimal agent assignment considering dependencies"""
        plan = {
            "parallel_groups": [],  # Groups that can run in parallel
            "agent_assignments": {},
            "estimated_duration": 0
        }
        
        # Topological sort to identify parallel opportunities
        groups = self.topological_grouping(self.dependency_graph)
        
        for group in groups:
            parallel_agents = []
            for work_package in group:
                agent_type = self.determine_agent_type(work_package)
                parallel_agents.append({
                    "work_package": work_package,
                    "agent_type": agent_type,
                    "estimated_time": self.estimate_time(work_package)
                })
            plan["parallel_groups"].append(parallel_agents)
            
        return plan
```

### Integration Points
1. **With Existing Hooks**
   - Agents trigger existing hooks in their worktrees
   - Hook outputs collected and coordinated
   - Shared cache across agents via Desktop Commander

2. **With Task Management (WP5)**
   - Each agent has sub-tasks from main task
   - Progress aggregated to main task tracker
   - TodoWrite integration per agent

3. **With Session Management**
   - Each agent maintains own session
   - Sessions linked to main orchestrator session
   - Parallel session archival on completion

### Acceptance Criteria
- [ ] Multiple agents can work on different WPs simultaneously without conflicts
- [ ] Distributed locking prevents resource contention
- [ ] Progress visible in real-time via `/logic tasks parallel status`
- [ ] Successful automatic merge of all agent work
- [ ] Performance improvement of 70%+ for multi-WP work
- [ ] Clean worktree cleanup after completion
- [ ] Automatic recovery from agent failures with work redistribution
- [ ] Zero data loss during parallel operations
- [ ] Agent health monitoring and automatic restart
- [ ] Dependency-aware task distribution
- [ ] Resource usage limits enforced per agent
- [ ] Merge conflict detection and resolution

### Estimated Effort: 8-10 hours
- Parallel agent infrastructure: 4 hours
- Git worktree integration: 2 hours
- Command implementation: 2 hours
- Testing & optimization: 2 hours

---

## Implementation Strategy

### Progressive Automation Approach

To ensure smooth transition and user adoption, implement in 3 phases:

**Phase 1: Hybrid Mode (Week 1-2)**
- Keep all existing commands functional
- Add automation flags: `/test auto on`, `/workflow auto on`
- Hooks run in parallel with manual commands
- Users can toggle automation per feature
- Collect usage metrics for optimization

**Phase 2: Deprecation (Week 3-4)**
- Show deprecation notices for manual commands
- Suggest hook alternatives
- Provide `/logic migrate` command for easy transition
- Maintain fallback to manual mode
- Monitor adoption rates

**Phase 3: Final Structure (Week 5)**
- Switch to 3-command structure
- Legacy commands show migration help
- Full automation active by default
- Emergency rollback available

### Development Plan (Updated with Pre-Implementation + WP0-6)
1. **Pre-Implementation** (Day -1): Documentation Baseline
   - Install and run Claude Conductor
   - Generate AI-friendly documentation
   - Extract patterns for integration

2. **Day 0**: DesktopCommanderMCP Installation
   - WP0: Install and configure DesktopCommanderMCP
   - Verify all tools working
   - Configure security settings

3. **Week 1**: Core Development (Days 1-7)
   - WP1: Enhanced hook infrastructure with process monitoring
   - WP2: Command conversions leveraging Desktop Commander
   - WP3: Begin documentation streamlining
   - WP4: Start codebase analysis for cleanup
   - **Architecture Review 1**: Post-WP1 hook analysis

4. **Week 2**: Implementation & Testing (Days 8-14)
   - WP2: Complete session management fixes
   - WP4: Execute codebase cleanup
   - WP5: Implement task management system
   - WP6: Parallel development orchestration
   - **Architecture Review 2**: Post-WP5 task system analysis
   - Integration testing with Desktop Commander
   - Performance optimization
   - Final documentation updates

5. **Week 3**: Final Integration (Days 15-16)
   - Complete parallel agent testing
   - **Final Architecture Review**: Complete system analysis
   - Deploy and monitor

### Architecture Review Checkpoints (Make-It-Heavy Analysis)

#### Review Points
Architecture reviews using Make-It-Heavy's multi-agent analysis approach provide deep insights at critical milestones:

1. **Post-WP1 Review: Hook Infrastructure Analysis** (2 hours)
   - **Focus**: Hook interaction patterns and priority system
   - **Agents**: Performance Agent, Security Agent, Architecture Agent, Integration Agent
   - **Analysis Areas**:
     - Hook execution order optimization
     - Performance bottlenecks in hook chains
     - Security implications of automated hooks
     - Integration points between hooks
   - **Deliverables**: Optimization recommendations, performance benchmarks

2. **Post-WP5 Review: Task Management Architecture** (2 hours)
   - **Focus**: Task lifecycle and automation effectiveness
   - **Agents**: Workflow Agent, Data Flow Agent, UX Agent, Scalability Agent
   - **Analysis Areas**:
     - Task state machine correctness
     - TodoWrite integration efficiency
     - User experience of automated workflows
     - Scalability for large projects
   - **Deliverables**: Architecture improvements, UX enhancements

3. **Final Architecture Review: Complete System Analysis** (3 hours)
   - **Focus**: Holistic system evaluation
   - **Agents**: All available agents for comprehensive coverage
   - **Analysis Areas**:
     - Command reduction effectiveness (10+ → 3)
     - Automation success rate (target: 80%)
     - Performance against benchmarks
     - Security audit of final system
     - Documentation quality assessment
     - Future extensibility analysis
   - **Deliverables**: Final report, optimization roadmap, success metrics validation

#### Implementation Approach
```python
# Make-It-Heavy integration for reviews
async def conduct_architecture_review(review_type, focus_areas):
    # Configure Make-It-Heavy with specific agents
    agents = select_agents_for_review(review_type)
    
    # Prepare context from current implementation
    context = {
        "codebase": analyze_current_state(),
        "metrics": gather_performance_metrics(),
        "focus": focus_areas
    }
    
    # Run multi-agent analysis
    analysis = await make_it_heavy.analyze(
        agents=agents,
        context=context,
        depth="comprehensive"
    )
    
    # Generate actionable recommendations
    return format_recommendations(analysis)
```

#### Review Benefits
- **Multi-perspective insights**: Different agents catch different issues
- **Depth of analysis**: Goes beyond surface-level code review
- **Actionable recommendations**: Specific improvements with examples
- **Performance validation**: Ensures targets are met
- **Security assurance**: Identifies potential vulnerabilities

### Total Review Effort: 7 hours

### Risk Mitigation
- **Backup Strategy**: Full `.claude` backup before changes
- **Rollback Plan**: Git tags at each milestone
- **Testing**: Automated test suite for each package
- **Communication**: Daily sync on integration points

### Error Handling & Recovery

**Hook Failure Strategy**:
1. **Graceful Degradation**
   - If hook fails, log error but continue operation
   - Fallback to manual command if critical hook fails
   - Show non-intrusive error notifications

2. **Self-Healing Capabilities**
   - Auto-retry with exponential backoff
   - Reset hook state on persistent failures
   - Automatic cache clearing on errors

3. **Emergency Recovery**
   ```
   /logic emergency          # Emergency menu
   /logic emergency restore  # Restore last working state
   /logic emergency disable  # Disable all hooks
   /logic emergency report   # Generate diagnostic report
   ```

4. **Error Reporting**
   - Clear, actionable error messages
   - Suggested fixes for common issues
   - Optional telemetry for improvement

### Monitoring & Metrics

**Performance Tracking**:
```python
# Hook execution metrics
{
  "hook_name": "security-scan",
  "executions": 1247,
  "avg_duration_ms": 45,
  "errors": 3,
  "last_error": "2025-01-19T10:30:00Z",
  "cache_hit_rate": 0.78
}
```

**User Experience Metrics**:
- Commands saved by automation
- Time saved per session
- User satisfaction scores
- Feature adoption rates

**Dashboard Access**:
```
/logic metrics           # Overall system metrics
/logic metrics hooks     # Hook-specific stats
/logic metrics export    # Export for analysis
```

### Success Metrics
- 70% reduction in manual commands (10+ → 3)
- 50% reduction in CLAUDE.md size
- 30% reduction in codebase size
- < 300ms total hook execution time (with process monitoring)
- Zero functionality regression
- Improved user experience through automation
- 100% task visibility and tracking with live progress
- Automated task lifecycle management
- **80% automation rate** (8/10 features fully/semi automated)
- **70% reduction in user interruptions** (only 3 manual commands)
- **90% of actions require zero user input** (7 fully automated)
- **Real-time process monitoring** for all automated operations
- **Complete audit trail** via Desktop Commander logging
- **100x faster code search** with ripgrep integration
- **Parallel execution capability** for future large refactorings
- **AI-optimized documentation** with line references and searchable anchors
- **Multi-perspective architecture validation** at key milestones
- **90% faster multi-package development** via parallel agents
- **3 comprehensive architecture reviews** ensuring quality
- **Pattern extraction** from Claude Conductor for improved AI understanding

### Migration Guide
```
Old Command → New Approach
/session → /save
/help → /logic help
/hook → /logic hooks
/workflow → Automatic (workflow-automation-hook)
/test → Automatic (quality-check-hook)
/security → Automatic (security-scan-hook)
/mode → Automatic (mode-suggestion-hook)
/pr → Automatic (documentation-generation-hook)
/context → Automatic (context-management-hook)
/notebook → Automatic (pattern-extraction-hook)
```

---

## Agent Coordination Infrastructure

### Overview
The Agent Coordination Infrastructure provides the foundational services required for safe multi-agent execution. This infrastructure is automatically initialized when multiple Claude instances are detected.

### Core Components

#### 1. Agent Registry Service
Maintains a live registry of all active agents:
```python
class AgentRegistry:
    def __init__(self):
        self.registry_path = ".claude/agents/registry/active-agents.json"
        self.heartbeat_timeout = 60  # seconds
        
    async def register_agent(self, agent_id, metadata):
        """Register new agent with metadata"""
        entry = {
            "agent_id": agent_id,
            "pid": os.getpid(),
            "started": time.time(),
            "last_heartbeat": time.time(),
            "status": "active",
            "metadata": metadata
        }
        
    async def cleanup_stale_agents(self):
        """Remove agents that haven't sent heartbeat"""
        current_time = time.time()
        for agent_id, info in self.agents.items():
            if current_time - info["last_heartbeat"] > self.heartbeat_timeout:
                await self.deregister_agent(agent_id)
```

#### 2. Distributed Lock Manager
Provides atomic operations across agents:
```python
class DistributedLockManager:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.locks_dir = ".claude/agents/locks"
        
    @contextmanager
    async def atomic_file_operation(self, resource_path):
        """Context manager for atomic file operations"""
        lock_name = hashlib.md5(resource_path.encode()).hexdigest()
        lock = DistributedLock(lock_name, self.agent_id)
        
        if await lock.acquire():
            try:
                yield
            finally:
                await lock.release()
        else:
            raise LockAcquisitionError(f"Could not acquire lock for {resource_path}")
```

#### 3. Message Queue System
Inter-agent communication without direct coupling:
```python
class MessageQueue:
    def __init__(self):
        self.queue_dir = ".claude/agents/messages"
        
    async def publish(self, channel, message):
        """Publish message to channel"""
        message_id = f"{time.time()}-{uuid.uuid4().hex[:8]}"
        message_path = f"{self.queue_dir}/{channel}/{message_id}.json"
        
        async with aiofiles.open(message_path, 'w') as f:
            await f.write(json.dumps({
                "id": message_id,
                "channel": channel,
                "timestamp": time.time(),
                "message": message
            }))
            
    async def subscribe(self, channel, callback):
        """Subscribe to channel messages"""
        # Watch directory for new messages
        async for message in self.watch_channel(channel):
            await callback(message)
```

#### 4. Resource Monitor
Prevents resource exhaustion:
```python
class ResourceMonitor:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.limits = {
            "memory_mb": 512,
            "cpu_percent": 25,
            "file_handles": 100,
            "process_count": 10
        }
        
    async def check_limits(self):
        """Check if agent is within resource limits"""
        usage = await self.get_agent_usage()
        
        for resource, limit in self.limits.items():
            if usage[resource] > limit:
                await self.throttle_agent()
                return False
        return True
```

#### 5. Conflict Resolution Engine
Handles conflicts when they occur:
```python
class ConflictResolver:
    def __init__(self):
        self.strategies = {
            "file_edit": self.resolve_file_edit_conflict,
            "git_operation": self.resolve_git_conflict,
            "task_assignment": self.resolve_task_conflict
        }
        
    async def resolve_conflict(self, conflict_type, conflict_data):
        """Apply appropriate resolution strategy"""
        if conflict_type in self.strategies:
            return await self.strategies[conflict_type](conflict_data)
        else:
            # Default: First agent wins, queue others
            return await self.queue_for_retry(conflict_data)
```

### Initialization Sequence

When a Claude agent starts:
1. Generate unique agent ID
2. Create agent workspace
3. Register with coordinator
4. Initialize message subscriptions
5. Start heartbeat daemon
6. Load agent-specific configuration
7. Begin normal operations

### Shutdown Sequence

When a Claude agent stops:
1. Complete in-progress operations
2. Release all held locks
3. Archive agent workspace
4. Deregister from coordinator
5. Clean up temporary files
6. Log shutdown reason

### Monitoring Dashboard

Access real-time agent status:
```
/logic agents status     # Show all active agents
/logic agents monitor    # Live monitoring mode
/logic agents logs [id]  # View agent-specific logs
/logic agents resources  # Resource usage by agent
```

### Emergency Procedures

For system recovery:
```
/logic agents emergency clean   # Clean up stale locks/agents
/logic agents emergency stop    # Stop all agents gracefully
/logic agents emergency reset   # Full system reset
```

---

## Appendix: Technical Dependencies

### Required Tools
- DesktopCommanderMCP (process management & advanced automation)
- Python 3.8+ (hooks and concurrency)
  - asyncio for async operations
  - aiofiles for async file I/O
  - multiprocessing for agent isolation
- Gemini API (notebook automation)
- Neo4j (memory system with transaction support)
- Git (version control with worktree support)
- Node.js/npm (for npx installation of Desktop Commander)

### Concurrency-Specific Dependencies
- **File Locking**: OS-level file locking (fcntl on Unix, msvcrt on Windows)
- **Process Management**: psutil for process monitoring
- **IPC**: Unix domain sockets for agent communication
- **Atomic Operations**: filelock library for cross-platform file locking
- **Message Queue**: watchdog for directory monitoring
- **Resource Monitoring**: resource library for usage tracking

### Optional Tools (for enhanced capabilities)
- Claude Conductor (AI-friendly documentation generation) - Pre-implementation only
- Make-It-Heavy (multi-agent architecture analysis) - Review checkpoints only
- Parallax concepts (adapted, not installed directly) - For parallel orchestration

### Integration Points
- `settings.json` - Central configuration
- `hooks-in-cc.md` - Hook documentation
- Session state files
- Knowledge JSON files

### Testing Requirements
- Unit tests for each hook with concurrency scenarios
- Integration tests for multi-agent workflows
- Performance benchmarks under concurrent load
- User acceptance scenarios with multiple agents
- Migration testing for existing users
- **Concurrency-Specific Tests**:
  - Lock contention tests
  - Resource exhaustion tests
  - Agent failure recovery tests
  - Message queue reliability tests
  - Merge conflict resolution tests
  - Race condition detection
  - Deadlock prevention verification