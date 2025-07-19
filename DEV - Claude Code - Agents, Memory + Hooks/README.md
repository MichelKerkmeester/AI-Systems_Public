> OUTDATED README — Work in progress!
> > To be added: 
> - Dynamic long-term memory ([Graphiti](https://github.com/getzep/graphiti) & [Crawl4AI RAG](https://github.com/coleam00/mcp-crawl4ai-rag))
> - Parallel agents that work with Gemini & Kimi
> - Testing with Puppeteer, Playwright / Chrome Debug, accessible by Agents like Gemini
> - Automated spec writing and task completion summaries

# Claude Code - AI-Enhanced Development System

> 🚀 **Supercharge your development with 77% documentation reduction** through intelligent system design, persistent memory, and automated workflows. Transform your Webflow projects with AI-powered efficiency.

Transform your development workflow with intelligent commands, automated validation, and cross-session memory for any project.

> [!NOTE]  
> While this system is optimized for **Webflow + Slater** workflow, its principles and commands adapt easily to any development environment.

## ⚡ Key Features

- **💰 77% Size Reduction** - Compact documentation with knowledge files
- **🧠 Persistent Memory** - Graphiti knowledge graph across sessions
- **🤖 Sequential Thinking** - Automatic structured problem-solving
- **📊 Real-time Monitoring** - Context staleness tracking and metrics
- **🔍 Unified Testing** - Comprehensive validation with auto-fixes
- **🛡️ Security-First** - Built-in patterns and production hardening
- **⚡ Performance Focus** - <50KB JS, 60 FPS animations, <3s load
- **🎭 Multi-Mode Operation** - Strict/Auto/Hybrid intelligent switching
- **📚 Knowledge Management** - Auto-updating JSON knowledge base

.

## 🚀 Quick Install via Claude Code

The easiest way to install is through Claude Code itself. Simply paste this request:
```
Please install the Claude Code System from:
https://github.com/MichelKerkmeester/AI-Systems-Public/tree/main/DEV%20-%20Claude%20Code%20-%20Instructions%20%2B%20Commands
```

Claude will automatically:
- ✅ Backup existing configuration
- ✅ Install CLAUDE.md with focused instructions  
- ✅ Create .claude directory structure
- ✅ Install all command modules
- ✅ Configure project settings
- ✅ Set up documentation templates
- ✅ Initialize knowledge files

.


.

## 📋 What You Get

### Commands & Quick Access
| Command | Alias | Purpose | Quick Access |
|---------|-------|---------|--------------|
| **`/workflow`** | `/w` | Development phases | `/wa` (auto), `/wp` (plan), `/wi` (implement) |
| **`/test`** | `/t` | Testing & validation | `/tq` (quick), `/tf` (full), `/ts` (security) |
| **`/memory`** | `/mem` | Memory management | `/memory status`, `/memory auto [level]` |
| **`/mode`** | `/m` | Switch operation modes | `/mode strict`, `/mode auto`, `/mode hybrid` |
| **`/pr`** | `/p` | Documentation generation | - |
| **`/gemini`** | `/g` | AI analysis (optional) | Various analysis modes |
| **`/context`** | `/c` | Context management | `/cr` (refresh), `/cs` (status), `/cc` (checkpoint) |
| **`/notebook`** | `/n` | Extract patterns | `/notebook extract`, `/notebook summary` |

### Enhanced Project Structure
```
your-project/
├── CLAUDE.md              # AI assistant instructions (195 lines!)
├── .claude/               # System configuration
│   ├── commands/          # Command definitions
│   ├── knowledge/         # Auto-updating knowledge base
│   │   ├── facts.json     # Project facts & requirements
│   │   ├── patterns.json  # Code patterns & conventions
│   │   └── constraints.json # Technical limits & rules
│   ├── sessions/          # Markdown summaries
│   ├── tasks/             # Task management
│   ├── gemini/            # AI analysis outputs
│   ├── user guide/        # User documentation
│   ├── templates/         # Reference formats
│   └── config.json        # System configuration
```

.

## 🎯 Operation Modes

### Mode System Overview
Claude Code adapts its behavior based on your work context through three operation modes:

| Mode | Icon | Purpose | Auto-Triggers |
|------|------|---------|---------------|
| **Strict** | 🔒 | Production/critical work | main/master branch, keywords: "production", "deploy" |
| **Auto** | 🚀 | Regular development (default) | Feature branches, normal work |
| **Hybrid** | ⚖️ | Complex multi-file work | 10+ files, keywords: "refactor", "optimize" |

### Mode Behaviors

#### 🔒 Strict Mode
- **Validation**: Maximum, aborts on warnings
- **Checkpoints**: After every action
- **Context refresh**: Every 50 points
- **Use for**: Production deployments, critical fixes, security work

#### 🚀 Auto Mode (Default)
- **Validation**: Standard with auto-fixes
- **Checkpoints**: Smart triggers (errors, completions)
- **Context refresh**: Every 120 points
- **Use for**: Regular development, feature work, debugging

#### ⚖️ Hybrid Mode
- **Validation**: Balanced approach
- **Checkpoints**: At milestones only
- **Context refresh**: Every 80 points
- **Use for**: Large refactors, optimization, complex features

### Mode Commands
```bash
# Check current mode
/mode

# Switch modes
/mode strict    # Production work
/mode auto      # Regular development
/mode hybrid    # Complex tasks
```

.

## 🧠 Memory System

### Graphiti Knowledge Graph
Persistent memory across sessions using Neo4j database:

**Automation Levels:**
- 🟢 **Full Auto**: Captures critical decisions, security choices, breaking changes
- 🟡 **Semi-Auto**: Suggests capture for bug fixes, optimizations (default)
- 🔵 **Manual**: User-initiated captures

**Memory Commands:**
```bash
/memory status              # Check memory stats
/memory auto full          # Set to full automation
/memory search "API"       # Search memories
/memory manual "Decision: Use TypeScript for all components"
```

### Knowledge Files
Auto-updating JSON files that persist project knowledge:

| File | Updates When | Contains |
|------|--------------|----------|
| `facts.json` | "Client prefers...", requirements | Project facts, stack info |
| `patterns.json` | New code patterns discovered | Code conventions, patterns |
| `constraints.json` | API limits found | Technical limits, budgets |

.

## 🤖 Sequential Thinking

### Automatic Activation
Structured problem-solving activates automatically for:
- Complex tasks (3+ steps)
- Architecture decisions
- Debugging > 10 minutes
- Performance optimization
- Security implementation

### Thinking Stages
1. **Problem Definition** - Understand the task
2. **Research** - Gather information
3. **Analysis** - Break down complexity
4. **Synthesis** - Combine insights
5. **Conclusion** - Final approach

### Visual Indicators
```
[🧠 Sequential Thinking: Active]
[🧠 Stage: Analysis]
[🧠 Thinking Complete]
```

.

## 🎯 How Commands Work

### 📂 `/workflow` - Development Phase Management
Guides you through development phases with intelligent mode selection based on project state analysis.

**Available Modes:**
| Mode | Purpose | When to Use |
|------|---------|-------------|
| `auto` | AI decides entire path | Starting new work |
| `explore` | Understand existing structure | First time in codebase |
| `plan` | Design architecture | Before implementation |
| `code` | Implementation guidance | Ready to build |
| `research` | Analysis only | Information gathering |
| `iterate` | Incremental improvements | Optimization cycles |

---

### 🧪 `/test` - Unified Testing System
Comprehensive validation system with auto-fixing capabilities.

**Testing Modes:**
- **Quick** (`/tq`): 5-minute essential scan
- **Full** (`/tf`): 15-minute comprehensive audit
- **Security** (`/ts`): Security-focused scan
- **Performance** (`/tp`): Performance analysis

**Enforces Constraints:**
```
❌ No DOM manipulation      ✅ Data attributes required
❌ No pixel units (→REM)    ✅ Element existence checks
❌ No generic selectors     ✅ Direct initialization
```

---

### 🔄 `/context` - Intelligent Context Management
Manages context freshness through sophisticated scoring.

**Staleness Scoring (0-120+ points):**
- 🟢 **0-49**: Fresh context
- 🟡 **50-79**: Aging context
- 🟠 **80-119**: Stale, refresh recommended
- 🔴 **120+**: Critical, refresh required

---

### 📝 `/memory` - Memory Management
Interfaces with Graphiti knowledge graph for persistent memory.

**Sub-commands:**
- `status` - Current memory statistics
- `auto [level]` - Set automation (off/semi/full)
- `search <query>` - Search knowledge graph
- `manual <text>` - Explicit memory save

---

### 📔 `/notebook` - Pattern Extraction
Extracts patterns and updates knowledge files automatically.

**Detects:**
- Client preferences ("client prefers...")
- Technical constraints ("must use...")
- Performance targets (KB/MB limits)
- API endpoints
- Deadlines

.

## 📊 Context & Performance

### Real-time Staleness Tracking
| Score | Status | Visual | Action |
|-------|--------|--------|--------|
| 0-49 | Fresh | 🟢 | Optimal |
| 50-79 | Aging | 🟡 | Gentle reminder |
| 80-119 | Stale | 🟠 | Refresh recommended |
| 120+ | Critical | 🔴 | Refresh required |

### Performance Metrics
**Documentation Reduction:**
- Original: 803 lines
- Optimized: 195 lines
- **Savings: 77%**

**Token Efficiency:**
- Small tasks: ~67% reduction
- Large analysis: ~85% reduction
- Average: ~75% savings

.

## 🔧 Active MCP Servers

### Currently Active (9 servers)
| Server | Purpose | Status |
|--------|---------|--------|
| **Sequential Thinking** | Structured problem-solving | ✅ Active |
| **Graphiti Memory** | Persistent knowledge graph | ✅ Active |
| **Gemini AI** | Code analysis & optimization | ✅ Active |
| **GitHub** | Repository management | ✅ Active |
| **n8n** | Workflow automation (528 nodes) | ✅ Active |
| **Webflow** | Platform API integration | ✅ Active |
| **Figma Dev Mode** | Design specifications | ✅ Active |
| **Playwright** | Browser automation | ✅ Active |
| **Chrome Debug** | Browser debugging | ✅ Active |

.

## 💻 Development Workflow

### 1. Start with Status
```bash
# View system status (automatic at start)
=== 🚀 Claude Code System Status ===
[🧠 Memory] Graphiti: ✅ Active | 127 memories
[📚 Knowledge] All files loaded ✅
[🤖 MCPs] 9 servers ready
[🎯 Mode] Auto Mode 🚀
```

### 2. Development Flow
```bash
# Understand structure
/workflow explore

# Plan implementation
/workflow plan

# Start coding
/workflow code

# Quick validation
/test quick
```

### 3. Memory & Context
```bash
# Check context freshness
/context status

# Refresh if needed
/context refresh

# Save important decision
/memory manual "DECISION: Use event delegation for dynamic elements"
```

.

## 🛡️ Security & Production

### Development Constraints
**❌ FORBIDDEN:**
- DOM structure modifications
- Pixels in CSS (auto→REM)
- Generic selectors
- console.log in production
- DOMContentLoaded usage
- Files > 500 lines

**✅ REQUIRED:**
- Element existence checks
- CSS transitions first
- Data attribute selectors
- Direct initialization
- Module pattern
- Batch DOM updates

### Production Checklist
- [ ] Run `/test full` comprehensive audit
- [ ] Check mode is Strict for production
- [ ] Remove all debug statements
- [ ] Verify no hardcoded secrets
- [ ] Test performance budgets
- [ ] Validate accessibility

.

## ⚙️ Customization

### Knowledge Files
Located in `.claude/knowledge/`:
- `facts.json` - Project-specific information
- `patterns.json` - Code conventions
- `constraints.json` - Technical limits

These auto-update based on your work!

### Configuration
`.claude/config.json`:
```json
{
  "current_mode": "auto",
  "sequential_thinking": {
    "enabled": true,
    "mandatory": true
  },
  "memory": {
    "automation": "semi"
  }
}
```

.

## 🔍 Troubleshooting

### Common Issues

#### Context Stale Warning
```bash
/context refresh    # Quick refresh
/context status    # Check details
```

#### Memory Not Capturing
```bash
/memory status     # Check if active
/memory auto full  # Increase automation
```

#### Wrong Mode Active
```bash
/mode             # Check current
/mode auto        # Switch to auto
```

#### Sequential Thinking Not Activating
- Check if task complexity >= 3 steps
- Verify not in simple file operations
- Use `/think` to force activation

.

## 📚 Learn More

- **System Status**: Shown at conversation start
- **Command Help**: Type `/[command] help`
- **Knowledge Files**: Check `.claude/knowledge/`
- **Session Summaries**: See `.claude/sessions/`

---

*Built for developers who value intelligent automation, persistent memory, and clean code.*
