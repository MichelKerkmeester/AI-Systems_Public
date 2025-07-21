# 🚀 Claude Code Assistant - anobel.nl

## 🖥️ Environment: Claude Code CLI
**Important:** This project uses Claude Code CLI in the terminal (Warp), NOT the Claude Desktop app.  
All commands and automation are designed for CLI usage. Desktop-specific features are optional.

## 1. 🎯 QUICK START

### System Status Display
```
=== 🚀 Claude Code System Status ===
[🧠 Memory] Graphiti: ✅ Active | Neo4j Connected
[📚 Knowledge] facts ✅ | patterns ✅ | constraints ✅ | security ✅  
[🤖 MCPs] Sequential ✅ | Graphiti ✅ | Gemini ✅ | GitHub ✅ | Context7 ✅ | Notion ✅ | Shadcn ✅ | Webflow ✅
[⚡ Hooks] 13 active hooks | Quality ✅ | Security ✅ | Memory ✅ | Session ✅
[🎯 Commands] /memory | /save | /logic
[📂 System] Project: anobel.nl | Git: main | Mode: Auto 🚀
=====================================
```

### Essential Commands (Just 3!)
```bash
/memory [search|manual|auto]  # Knowledge management
/save [new|list|search|stats] # Session management  
/logic [help|hooks|emergency] # System control & help

# Everything else runs automatically via hooks!
```

**Get detailed help:** `/logic help [topic]`  
**See what's automated:** `/logic hooks status`

---

## 2. 🛠️ CORE PRINCIPLES

### Development Philosophy
1. **Elite JavaScript & CSS specialist** - Fix root causes, not symptoms
2. **Production-grade code** - DRY, KISS, secure, performant
3. **Webflow enhancement** - Work with platform, never against it
4. **Full ownership** - Complete solutions, not patches

### Technical Constraints
| Category | ❌ Never | ✅ Always |
|----------|----------|-----------|
| **DOM** | Modify structure | Use existing elements |
| **CSS** | Pixels | REM units + data attributes |
| **JS** | console.log, globals | Namespaces, element checks |
| **Files** | >500 lines | Module pattern |

**Platform Limits:** JS <50KB | CSS <20KB | Load <3s | Assets 30MB/file

---

## 3. 📋 TASK MANAGEMENT

### Task Lifecycle
Tasks flow through stages:
```
/specs → /active → /completed → /z__archive (user-managed only)
```
**Note:** z__archive folders are user-managed. AI agents should organize completed tasks in topic-specific sub-folders.

### Before System Changes
**IMPORTANT:** Create a spec folder before any major system changes:
```
.claude/tasks/specs/
└── [feature-name]/
    ├── requirements.md     # What needs to be done
    ├── design.md          # How it will be implemented
    ├── test-plan.md       # How to verify it works
    └── rollback-plan.md   # How to undo if needed
```

### Task Commands
- Tasks are managed automatically via TodoWrite integration
- Active task limit: 1 (enforced by system)
- Progress tracked in real-time
- Completion suggestions when all todos done

---

## 4. 🤖 AUTOMATION & HOOKS

### What Runs Automatically
| Old Command | Triggers | Manual Override |
|-------------|----------|-----------------|
| `/workflow` | Complex tasks (3+ steps) | Sequential Thinking tool |
| `/test` | 3+ files changed | Run tests manually |
| `/security` | Sensitive patterns | `/logic emergency` |
| `/notebook` | Session saves | `/logic notebook` |
| `/mode` | Task complexity | Respond to suggestions |

### Memory Automation Levels
```bash
/memory auto off     # No automation
/memory auto manual  # Explicit capture only
/memory auto semi    # Critical auto, others prompt (default)
/memory auto full    # Capture everything
```

**Patterns captured:** DECISION, SECURITY, BREAKING, RESOLVED, PATTERN, client preferences, API limits

---

## 🚨 HOOK AUTOMATION WARNINGS

### What Hooks Automate (But You Might Still Break)

Even with hooks enabled, these mistakes can still happen:

#### 1. Quality Hook Pitfalls
- ❌ **Claiming work is complete without testing** - Hook reminds but can't force
- ❌ **Writing fake tests** - Tests that don't actually verify functionality  
- ❌ **Bypass attempts** - Using `window.console.log` or eval to avoid detection
- ❌ **Ignoring file size warnings** - Creating 500+ line files despite reminders

#### 2. Security Hook Blind Spots
- ❌ **Base64 encoded secrets** - Hook might miss encoded credentials
- ❌ **Secrets in comments** - `// API_KEY: abc123` still exposes secrets
- ❌ **Git commit messages** - Secrets in commit descriptions bypass file scanning
- ❌ **Minified/obfuscated code** - Hidden secrets in compressed code

#### 3. Memory Hook Gaps
- ❌ **Not capturing decisions** - Important choices lost between sessions
- ❌ **Skipping memory search** - Re-solving already solved problems
- ❌ **Outdated memories** - Not updating when patterns change

#### 4. Pattern Extraction Misses
- ❌ **Context-specific patterns** - Regex can't catch nuanced patterns
- ❌ **Conflicting patterns** - Auto-extraction might create duplicates
- ❌ **Client requirements** - Manual patterns often needed for preferences

#### 5. Task Management Workarounds
- ❌ **Direct file creation** - Making tasks without commands
- ❌ **Multiple active tasks** - Editing files to bypass one-task limit
- ❌ **Skipping task flow** - Moving files between folders manually

**Remember:** Hooks are safety nets, not guarantees. They catch obvious mistakes but can't enforce good judgment or thorough testing.

---

## 5. 📂 PROJECT STRUCTURE

```
.claude/
├── docs/                   # All documentation (renamed from y__docs)
│   ├── logic/             # Logic system docs
│   ├── graphiti/          # Memory system docs
│   ├── technical/         # Implementation details
│   └── mcp/               # MCP server docs
├── logic/                  # Hooks and automation
│   ├── session/           # Session management
│   ├── memory/            # Memory context
│   ├── tasks/             # Task lifecycle
│   └── quality/           # Code quality
├── knowledge/              # facts.json, patterns.json, constraints.json (moved from project/)
├── state/                  # System state (moved from project/)
├── tasks/                  # Task organization (moved from project/)
│   ├── specs/            # Task specifications (pending)
│   ├── active/           # Current task (max 1)
│   ├── completed/        # Finished tasks
│   └── z__archive/       # User-managed archive (excluded from AI operations)
├── tests/                  # Tests (moved from project/)
├── agents/                 # Agent system
├── scripts/                # Utility scripts
└── settings.json          # Configuration
```

### Key Files
- **facts.json** - Project requirements, client preferences
- **patterns.json** - Code conventions, established patterns
- **constraints.json** - Technical limits, platform rules
- **settings.json** - Hook configuration, automation levels

---

## 6. 🆘 HELP & TROUBLESHOOTING

### Get Help
```bash
/logic help              # List all help topics
/logic help automation   # How automation works
/logic help hooks        # Understanding hooks
/logic help migration    # Migrate from old commands
/logic help troubleshooting  # Fix common issues
```

### Quick Fixes
- **Hooks not running?** `/logic hooks status`
- **Too much automation?** `/memory auto manual`
- **Emergency disable:** `/logic emergency disable`
- **Session issues?** `/save new recovery-session`

### Production Checklist
- [ ] No console.log statements
- [ ] No hardcoded API keys  
- [ ] All tests passing
- [ ] Performance budgets met
- [ ] Security scan clean

---

**Remember:** Focus on coding, not commands. The system handles the rest! 🚀