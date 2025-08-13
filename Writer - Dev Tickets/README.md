# Dev Ticket Writer - User Guide v4.2.0

The Dev Ticket Writer helps teams create professional development tickets that are "clear at first glance" for developers while teaching product thinking principles. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it bridges the communication gap between product and development. When implementation details are needed, the concise Spec mode provides focused, copy-paste ready solutions.

## 🆕 What's New in v4.2.0

- **First Heading "About"**: All tickets now start with `# ■ About` in the body (feature name in artifact title only)
- **20% More Concise**: All tickets reduced by 20% while maintaining clarity
- **Streamlined Documentation**: Cleaner, more focused instructions throughout
- **Enhanced Readability**: Faster ticket scanning with improved structure
- **Maintained Features**: All v4.1 features preserved with better clarity

.

## ✨ Key Features

- **Developer-First Clarity**: User-specified scope prefixes, structured descriptions
- **5 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $spec
- **Interactive Offers**: Automatic guidance offers for $standard and $complex modes
- **Global Resolution Approach**: Max 3 items per section, outcome-focused checklists
- **Concise Spec Mode**: Minimal conversation (1-3 questions), working code examples
- **Enhanced Symbol System**: Professional symbols (■, ◇, **◊**, →, ✦, ✓, ⊗, ⚠️, ≈)
- **Prompt Improvement**: Clarifies vague requests without assumptions
- **Educational Focus**: Interactive mode teaches product management through practice
- **2-Minute Rule**: All tickets readable in under 2 minutes

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v4.2"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v4.2.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Templates & Standards - v4.2.0.md`
- `Ticket - Examples Library - v4.2.0.md`
- `Ticket - Interactive Mode - v4.2.0.md`
- `Ticket - Quick Reference Card - v4.2.0.md`
- `Ticket - Spec Mode - v4.2.0.md`
- `Ticket - Prompt Improvement - v4.2.0.md`

### Step 4: Start Creating Tickets
Simply describe what you need:
```
fix login bug                    # Interactive mode (default)
$q user profiles                 # Quick mode
$s dashboard feature             # Standard (offers Interactive)
$c payment integration           # Complex (offers Interactive)
$spec hide scrollbar             # Spec mode (instant generation)
```

.

## 🎛️ Operating Modes

| Mode | Command | When | Sections | Offer | Focus |
|------|---------|------|----------|-------|-------|
| **Interactive** | DEFAULT | No mode | Adaptive | N/A | Guidance |
| **Quick** | `$q` | Simple | 2-3 | No | Essential |
| **Standard** | `$s` | Full | 4-5 | **YES** | Complete |
| **Complex** | `$c` | Major | 6-8 | **YES** | Phases/Child |
| **Spec** | `$spec` | Frontend | N/A | No | Code |

## 🔧 Complex Mode Options

### Option A: Phased Development
- Phase 1: Foundation
- Phase 2: Core Features
- Phase 3: Enhancement

### Option B: Child Tickets
- Infrastructure tickets
- Feature implementation
- Quality & polish

## 💻 Spec Mode (Concise)

### Fast Paths (0-1 Questions)
```markdown
User: $spec hide scrollbar
System: Browser compatibility?
User: yes
[Generates 20-line CSS immediately]
```

### Components (2-3 Questions)
```markdown
User: $spec virtual table
System: Quick setup:
1. Row count?
2. React/Vue?
User: 50k, React
[Generates 40-line implementation]
```

.


## 🔧 Installing MCP Tools (Recommended)

### Option A: Docker Setup (Stable)

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))

**AI-Assisted Installation:**

Copy to any AI assistant:
```
Help me set up Docker containers for Dev Ticket Writer MCP tools.

I need to:
1. Create directory at "$HOME/MCP Servers"
2. Clone repos:
   - https://github.com/sequentialthinking/sequential-thinking-mcp
   - https://github.com/cascadethinking/cascade-thinking-mcp
3. Create docker-compose.yml
4. Configure claude_desktop_config.json
5. Start containers

I'm on [Windows/Mac/Linux]. Give exact commands.
```

### Option B: NPX (Quick)

Add to Claude Desktop config:
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "cascade-thinking": {
      "command": "npx",
      "args": ["-y", "cascade-thinking-mcp"]
    }
  }
}
```

### MCP Selection

| Mode | Tool | Thoughts |
|------|------|----------|
| **Interactive** | Cascade | 3-5 branching |
| **Quick** | Sequential | 1-2 |
| **Standard** | Sequential | 2-3 |
| **Complex** | Cascade | 3-5 branching |
| **Spec** | Sequential | 1-2 |

.

## 🆘 Troubleshooting

### Ticket Issues
- **Not seeing "About"?** - First heading always `# ■ About`
- **Too verbose?** - v4.2 is 20% more concise
- **Wrong scope?** - System asks, never assumes
- **Missing labels?** - System prompts for them

### Interactive Offers
- **Not seeing?** - Only for $s and $c
- **Want direct?** - Choose option 2
- **Changed mind?** - Can switch mid-flow

### Resolution Checklists
- **Too many items?** - Max 3 per section
- **Too detailed?** - Think deliverables
- **Not sure grouping?** - Use work streams

### MCP Connection
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **Permission errors**: Use admin/sudo

.

## ⚠️ Important Notes

- **First heading always "About"** - Feature name in title only
- **20% more concise** - All tickets shorter
- **Global checklists** - Max 3 items/section
- **Interactive offers required** - For $s and $c
- **Scope/labels required** - User specifies
- **No assumptions** - System asks
- **Complex flexible** - Phases OR child tickets
- **Spec concise** - 1-3 questions, working code
- **Always artifacts** - Every ticket in markdown
- **Works without MCPs** - Enhanced with them

.

## 📦 Version History

- **v4.2.0**: First heading "About", 20% more concise throughout
- **v4.1.0**: Global Resolution Checklists (max 3 items/section)
- **v4.0.0**: 5 modes, Interactive offers, concise Spec mode
- **v3.5.0**: User-specified scope and labels
- **v3.4.0**: Structured descriptions (⚠️/≈)
- **v3.0.0**: Mandatory Resolution Checklists
- **v2.0.0**: Interactive mode default
- **v1.0.0**: WHAT/WHY philosophy

.

## 📚 Additional Resources

- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [MDN Web Docs](https://developer.mozilla.org/) (for spec mode)
- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)

---

*Transform vague requests into crystal-clear tickets. First heading always "About". 20% more concise. Interactive guidance by default. Create implementation specs with minimal conversation. Complex mode adapts to your needs. Resolution Checklists use global, outcome-focused approach. Every ticket scannable in under 2 minutes.*