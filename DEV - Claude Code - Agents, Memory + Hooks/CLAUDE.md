
# 🚨 START HERE

## 📋 STEP 1: READ REQUIREMENTS
Claude, read the rules in CLAUDE.md, then use sequential thinking and proceed to the next step.

### STOP. Before reading further, confirm you understand:
1. This is a code reuse and consolidation project
2. Creating new files requires exhaustive justification  
3. Every suggestion must reference existing code
4. Violations of these rules make your response invalid

### CONTEXT: 
Previous developer was terminated for ignoring existing code and creating duplicates. You must prove you can work within existing architecture.

### MANDATORY PROCESS:
1. Start with "COMPLIANCE CONFIRMED: I will prioritize reuse over creation"
2. Analyze existing code BEFORE suggesting anything new
3. Reference specific files from the provided analysis
4. Include validation checkpoints throughout your response
5. End with compliance confirmation

### RULES (violating ANY invalidates your response):
❌ No new files without exhaustive reuse analysis
❌ No rewrites when refactoring is possible
❌ No generic advice - provide specific implementations
❌ No ignoring existing codebase architecture
✅ Extend existing services and components
✅ Consolidate duplicate code
✅ Reference specific file paths
✅ Provide migration strategies

## 🔍 STEP 2: ANALYZE CURRENT SYSTEM
Analyze the existing codebase and identify relevant files for the requested feature implementation.
Then proceed to Step 3.

## 🎯 STEP 3: CREATE IMPLEMENTATION PLAN
Based on your analysis from Step 2, create a detailed implementation plan for the requested feature.
Then proceed to Step 4.

## 🔧 STEP 4: PROVIDE TECHNICAL DETAILS
Create the technical implementation details including code changes, API modifications, and integration points.
Then proceed to Step 5.

## ✅ STEP 5: FINALIZE DELIVERABLES
Complete the implementation plan with testing strategies, deployment considerations, and final recommendations.

### Code Reuse Enforcement Rules

**Strict Requirements:**
1. **Search before coding** - Use Grep/Glob/Task to find existing implementations
2. **Justify new files** - Explain why existing files cannot be extended
3. **Reference existing code** - Every suggestion must cite specific files/lines
4. **Pattern compliance** - Follow patterns.json and established conventions
5. **Component catalog** - Check for reusable components before creating new ones

**Exceptions (Allowed File Creation):**
- Spec folders for task planning
- Hook-generated files (automated)
- MCP tool outputs
- Test files and results
- Documentation when explicitly requested

**Integration with External Analysis:**
- Consider using Gemini or other tools to analyze codebase before planning
- After planning, get external validation for improvement ideas
- Cross-reference multiple sources for comprehensive understanding

---

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

### AI Environment: Claude Code CLI
**Important:** This project uses Claude Code CLI in the terminal (Warp), NOT the Claude Desktop app.  
All commands and automation are designed for CLI usage. Desktop-specific features are optional.

### Development Philosophy
1. **Elite JavaScript & CSS specialist** - Fix root causes using proven patterns
2. **Production-grade code** - DRY, KISS, secure, performant
3. **Webflow enhancement** - Work with platform, never against it
4. **Code reuse first** - Search existing code before writing new
5. **Full ownership** - Complete solutions built from existing components

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
.claude/project-management/specs/
└── [feature-name]/
    ├── requirements.md     # What needs to be done
    ├── design.md          # How it will be implemented
    ├── test-plan.md       # How to verify it works
    └── rollback-plan.md   # How to undo if needed
```

**Automatic Spec Creation**: Complex requests (score ≥ 6) trigger automatic spec generation with code reuse analysis included.

### Task Commands
- Tasks are managed automatically via TodoWrite integration
- Active task limit: 1 (enforced by system)
- Progress tracked in real-time
- Completion suggestions when all todos done

### Spec-Driven Code Reuse Process

For complex features (complexity score ≥ 6), the system automatically creates a specification:

#### Automatic Spec Creation
1. **Triggered by**: Keywords like "implement", "create", "build" + complex requirements
2. **Location**: `/specs/code-reuse/[feature-name]/`
3. **Contents**: 4 mandatory documents + test folder
4. **Workflow**: Spec → Active → Completed with summary

#### Spec Structure for Code Reuse
```
/specs/code-reuse/[feature]/
├── requirements.md      # Include reuse analysis requirements
├── design.md           # Reference existing components
├── test-plan.md        # Test reuse compliance
├── rollback.md         # Preserve reusable components
└── tests/              # Verification results
```

#### Integration with 5-Step Process
- **Step 1**: If complex, create spec automatically
- **Step 2**: Save search results to spec
- **Step 3**: Document in design.md
- **Step 4**: Track in active task
- **Step 5**: Generate completion summary

---

## 4. 🧠 MANDATORY MEMORY OPERATIONS (v2 Enforcement)

**BEFORE ANY TASK:**
1. **ALWAYS** search memories using `mcp__graphiti-gemini__search` with relevant keywords
2. **ALWAYS** state: "Searched X memories, found Y relevant" at task start
3. **NEVER** skip this - enforced by hooks before TodoWrite tasks
4. **Memory search is mandatory** - violations make your response invalid

**DURING CONVERSATIONS:**
Auto-capture triggers (immediate capture required):
- **Decisions**: "decided to", "will use", "choosing", "selected"
- **Errors fixed**: "resolved", "fixed", "solution works", "workaround"
- **Patterns**: "always", "convention", "best practice", "standard"
- **Security**: Any auth/token/credential/API key discussion
- **Breaking changes**: Migration, deprecation, or backwards compatibility
- **Code reuse**: Found components, existing solutions, refactor opportunities
- **Client preferences**: User feedback, requirements, constraints
- **Performance**: Optimization discoveries, bottlenecks identified

**AFTER TOOL USE:**
Automatic capture after:
- File edits (Edit/MultiEdit/Write) - captures changes made
- Task completions (TodoWrite status changes)
- Error resolutions (any fix applied)
- Pattern discoveries (new conventions found)
- Test results (successes and failures)
- Security scans (vulnerabilities found/fixed)

**CONVERSATION BUFFER:**
- System auto-captures after 5 exchanges to prevent memory loss
- Buffer includes full context and decisions made

**CAPTURE FORMAT:**
```json
mcp__graphiti-gemini__add_episode
{
  "data": {
    "name": "[TYPE]: Brief description",
    "episode_body": "Detailed content with context, code snippets, file paths",
    "source": "task|conversation|error_fix|pattern|code_reuse|security",
    "group_id": "project-category",
    "valid_at": "ISO timestamp (optional)"
  }
}
```

**ENFORCEMENT:** 
- Skipping memory operations = invalid response
- System now captures 50+ memories per day automatically
- Each session must end with: "Captured N memories this session"
- Memory search is enforced by hooks before any TodoWrite task creation

---

## 5. ⚠️ HOOK AUTOMATION WARNINGS

### What Hooks Automate (But You Might Still Break)

Even with hooks enabled, these mistakes can still happen:

#### 1. Quality Hook Pitfalls
- ❌ **Claiming work is complete without testing** - Hook reminds but can't force
- ❌ **Writing fake tests** - Tests that don't actually verify functionality  
- ❌ **Bypass attempts** - Using `window.console.log` or eval to avoid detection
- ❌ **Ignoring file size warnings** - Creating 500+ line files despite reminders
- ❌ **Creating duplicate code** - Not searching for existing implementations
- ❌ **Ignoring reusable patterns** - Writing from scratch instead of extending

#### 2. Security Hook Blind Spots
- ❌ **Base64 encoded secrets** - Hook might miss encoded credentials
- ❌ **Secrets in comments** - `// API_KEY: abc123` still exposes secrets
- ❌ **Git commit messages** - Secrets in commit descriptions bypass file scanning
- ❌ **Minified/obfuscated code** - Hidden secrets in compressed code

#### 3. Memory Hook Gaps
- ❌ **Not capturing decisions** - Important choices lost between sessions
- ❌ **Skipping memory search** - Re-solving already solved problems
- ❌ **Outdated memories** - Not updating when patterns change
- ❌ **Missing code reuse patterns** - Not documenting found components

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

## 5. 🆘 HELP & TROUBLESHOOTING

### Get Help
```bash
/logic help              # List all help topics
/logic help automation   # How automation works
/logic help hooks        # Understanding hooks
/logic help migration    # Migrate from old commands
/logic help troubleshooting  # Fix common issues
/logic help code-reuse   # Spec-driven code reuse workflow
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
- [ ] No duplicate functionality
- [ ] Existing code searched and reused
- [ ] Pattern compliance verified
- [ ] New files justified if created

---

**Remember:** Focus on coding, not commands. The system handles the rest! 🚀