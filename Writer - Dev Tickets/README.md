# Dev Ticket Writer - User Guide v4.3.0

The Dev Ticket Writer helps teams create professional development tickets that are "clear at first glance" for developers while teaching product thinking principles. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it bridges the communication gap between product and development. **Now with seamless ClickUp and Notion integration** for instant workspace management.

## 🆕 What's New in v4.3.0

### Platform Integration 🚀
- **ClickUp Integration**: Automatically create tasks, lists, and sprints
- **Notion Integration**: Instantly generate databases, pages, and wikis
- **Smart Handoff**: Platform MCPs detect patterns and create appropriate structures
- **Post-Ticket Workflow**: Always offers platform integration after ticket creation

### Maintained from v4.2.1
- **About Icon**: All tickets start with `# ◘ About` in the body
- **Checkbox Format**: Resolution checklists use `[]` format
- **Requirements Dividers**: Visual separation between subsections
- **20% More Concise**: Streamlined while maintaining clarity
- **Interactive Default**: Guidance-first approach

.

## ✨ Key Features

- **Platform Integration**: Direct ClickUp/Notion workspace creation
- **Developer-First Clarity**: User-specified scope prefixes, structured descriptions
- **5 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $spec
- **Interactive Offers**: Automatic guidance for $standard and $complex modes
- **Global Resolution Approach**: Max 3 items per section, outcome-focused
- **Concise Spec Mode**: 1-3 questions, working code examples
- **Enhanced Symbol System**: Professional symbols (◘, ◇, **◊**, →, ✦, ✓, ⊗, ⚠️, ≈)
- **Educational Focus**: Interactive mode teaches through practice
- **2-Minute Rule**: All tickets readable in under 2 minutes

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v4.3.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v4.3.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Templates & Standards - v2.3.1.md`
- `Ticket - Examples Library - v2.3.1.md`
- `Ticket - Interactive Mode - v2.0.0.md`
- `Ticket - Platform Integration - v1.0.0.md`
- `Ticket - Quick Reference Card - v2.4.0.md`
- `Ticket - Spec Mode - v1.1.1.md`
- `Ticket - Prompt Improvement - v1.3.0.md`

### Step 4: Install MCP Tools (Recommended)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating Tickets
```
fix login bug                    # Interactive mode (default)
$q user profiles                 # Quick mode
$s dashboard feature             # Standard (offers Interactive)
$c payment integration           # Complex (offers Interactive)
$spec hide scrollbar             # Spec mode (instant generation)
```

After any ticket, you'll see:
```
📦 Add to your workspace?
1. ClickUp - Task management, sprints
2. Notion - Documentation, wikis
3. Skip - Keep as artifact only
```

.

## 🎛️ Operating Modes

| Mode | Command | When | Sections | Offer | Focus | Platform |
|------|---------|------|----------|-------|-------|----------|
| **Interactive** | DEFAULT | No mode | Adaptive | N/A | Guidance | ✅ |
| **Quick** | `$q` | Simple | 2-3 | No | Essential | ✅ |
| **Standard** | `$s` | Full | 4-5 | **YES** | Complete | ✅ |
| **Complex** | `$c` | Major | 6-8 | **YES** | Phases | ✅ |
| **Spec** | `$spec` | Frontend | N/A | No | Code | ✅ |

## 📦 Platform Integration Flow

### After Ticket Creation
```markdown
Your ticket is ready!
[Ticket displayed]

📦 Add to your workspace?
1. **ClickUp** - Task management, sprints, time tracking
2. **Notion** - Documentation, knowledge base, wikis
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

### Smart Platform Detection
- **ClickUp detects**: Sprint planning, bug tracking, time tracking
- **Notion detects**: Documentation, wikis, knowledge bases
- **Both handle**: General features, project management

### What Happens Next
1. **You choose platform** → System passes ticket to MCP
2. **MCP analyzes content** → Detects patterns automatically
3. **Creates structure** → Appropriate workspace setup
4. **Confirms completion** → Link to new workspace item

.

## 🔧 Installing MCP Tools

### Docker Setup (AI-Assisted)

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))

**Installation:**

Copy this prompt to any AI assistant for complete setup instructions:
```
Help me set up Docker containers for Dev Ticket Writer MCP tools v4.3.0.

I need to:
1. Create directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/sequentialthinking/sequential-thinking-mcp
   - https://github.com/cascadethinking/cascade-thinking-mcp
   - https://github.com/taazkareem/clickup-mcp-server
   - https://github.com/makenotion/notion-mcp-server
3. Create docker-compose.yml for all 4 services
4. Configure claude_desktop_config.json
5. Set up environment variables for ClickUp/Notion API keys
6. Start all containers

I'm on [Windows/Mac/Linux]. Give me exact commands with proper error handling.
```

The AI will provide step-by-step commands specific to your operating system.

### Getting API Keys

**ClickUp:**
1. Go to Settings → Apps → API Token
2. Generate Personal Token
3. Copy and add to `.env`

**Notion:**
1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Create new integration
3. Copy Internal Integration Token
4. Add to `.env`

### MCP Tool Selection

| Mode | Primary Tool | Thoughts | Platform Tools |
|------|--------------|----------|----------------|
| **Interactive** | Cascade | 3-5 | ClickUp/Notion |
| **Quick** | Sequential | 1-2 | ClickUp/Notion |
| **Standard** | Sequential | 2-3 | ClickUp/Notion |
| **Complex** | Cascade | 3-5 | ClickUp/Notion |
| **Spec** | Sequential | 1-2 | Optional |

.

## 🆘 Troubleshooting

### Platform Integration
- **Not seeing offer?** - Appears after every ticket in chat
- **MCP unavailable?** - Check Docker containers running
- **API errors?** - Verify API keys in `.env`
- **Wrong workspace?** - MCPs auto-detect patterns

### Ticket Issues
- **Not seeing "About"?** - First heading always `# ◘ About`
- **Too verbose?** - v4.3 maintains 20% concision
- **Wrong scope?** - System asks, never assumes
- **Missing labels?** - System prompts for them

### Interactive Offers
- **Not seeing?** - Only for $s and $c
- **Want direct?** - Choose option 2
- **Changed mind?** - Can switch mid-flow

### Docker/MCP Issues
- **Docker not running**: Start Docker Desktop
- **Container errors**: Check logs with `docker-compose logs`
- **Permission denied**: Use admin/sudo
- **Port conflicts**: Change ports in docker-compose.yml

.

## ⚠️ Important Notes

### Core Features
- **Platform integration** - Always offered after ticket creation
- **First heading "About"** - Uses ◘ icon, feature name in title only
- **20% more concise** - All tickets streamlined
- **Global checklists** - Max 3 items/section
- **Interactive default** - No mode = conversational guidance
- **Scope/labels required** - User always specifies
- **No assumptions** - System asks when unclear

### Platform Integration
- **Always in chat** - Never in ticket artifact
- **Three options** - ClickUp, Notion, or Skip
- **Smart detection** - MCPs analyze content patterns
- **No mapping needed** - Trust platform intelligence
- **Graceful fallback** - Works without MCPs

### Technical Details
- **Complex flexible** - Phases OR child tickets
- **Spec concise** - 1-3 questions, working code
- **Always artifacts** - Every ticket in markdown
- **Checkbox format** - Uses `[]` without space
- **Requirements dividers** - Between subsections

.

## 📦 Version History

- **v4.3.0**: Platform integration (ClickUp/Notion), MCP handoff
- **v4.2.1**: Updated About icon (◘), checkbox format `[]`
- **v4.2.0**: First heading "About", 20% more concise
- **v4.1.0**: Global Resolution Checklists (max 3/section)
- **v4.0.0**: 5 modes, Interactive offers, concise Spec
- **v3.5.0**: User-specified scope and labels
- **v3.4.0**: Structured descriptions (⚠️/≈)
- **v3.0.0**: Mandatory Resolution Checklists
- **v2.0.0**: Interactive mode default
- **v1.0.0**: WHAT/WHY philosophy

.

## 📚 Additional Resources

### Product Management
- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)

### Platform Documentation
- [ClickUp API Docs](https://clickup.com/api)
- [Notion API Guide](https://developers.notion.com/)
- [MCP Protocol Guide](https://modelcontextprotocol.io/)

### Technical Resources
- [MDN Web Docs](https://developer.mozilla.org/) (for spec mode)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Claude Desktop Setup](https://claude.ai/docs/desktop)

---

*Transform vague requests into crystal-clear tickets with instant workspace integration. Interactive guidance by default. Platform intelligence handles ClickUp/Notion creation. Complex mode adapts to your needs. Resolution Checklists use outcome-focused approach. Every ticket scannable in under 2 minutes, then seamlessly added to your workspace.*