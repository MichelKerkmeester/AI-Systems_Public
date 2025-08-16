# Product & Dev Writer - User Guide v4.4.0

The Product & Dev Writer helps teams create professional development tickets and product documentation that are "clear at first glance" while teaching product thinking principles. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it bridges the communication gap between product and development. **Now with Documentation mode** for creating user-focused product guides alongside development tickets.

## 🆕 What's New in v4.4.0

### Documentation Mode 📚
- **New $doc mode**: Create user-focused product documentation
- **Interactive guidance**: Audience, features, and depth questions
- **◻️ Feature sections**: New symbol for documentation structure
- **Visual references**: Screenshot and tutorial integration
- **Platform ready**: Optimized for Notion knowledge bases
- **User guides**: From onboarding to feature documentation

### Maintained from v4.3.0
- **Platform Integration**: ClickUp/Notion workspace creation
- **About Icon**: All tickets start with `# ⌘ About` in the body
- **Checkbox Format**: Resolution checklists use `[]` format
- **Requirements Dividers**: Visual separation between subsections
- **20% More Concise**: Streamlined while maintaining clarity
- **Interactive Default**: Guidance-first approach

## ✨ Key Features

- **6 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $spec, **$doc**
- **Platform Integration**: Direct ClickUp/Notion workspace creation
- **Developer-First Clarity**: User-specified scope prefixes, structured descriptions
- **User Documentation**: Product guides with ◻️ feature sections
- **Interactive Offers**: Automatic guidance for $standard and $complex modes
- **Global Resolution Approach**: Max 3 items per section, outcome-focused
- **Concise Spec Mode**: 1-3 questions, working code examples
- **Enhanced Symbol System**: Professional symbols (⌘, ◇, ◻️, **◊**, →, ✦, ✓, ⊗, ⚠️, ≈, 📚)
- **Educational Focus**: Interactive mode teaches through practice
- **2-Minute Rule**: All tickets and docs readable in under 2 minutes

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Product & Dev Writer v4.4.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Product & Dev - Writer - v4.4.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Product & Dev - Templates, Standards & Examples - v3.0.0.md`
- `Product & Dev - Interactive Mode - v2.1.0.md`
- `Product & Dev - Documentation Mode - v1.0.0.md` **(NEW)**
- `Product & Dev - Platform Integration - v1.0.0.md`
- `Product & Dev - Quick Reference Card - v2.5.0.md`
- `Product & Dev - Spec Mode - v1.1.1.md`
- `Product & Dev - Prompt Improvement - v1.3.0.md`

### Step 4: Install MCP Tools (Recommended)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating Tickets & Documentation
```
fix login bug                    # Interactive mode (default)
$q user profiles                 # Quick mode
$s dashboard feature             # Standard (offers Interactive)
$c payment integration           # Complex (offers Interactive)
$spec hide scrollbar             # Spec mode (instant generation)
$doc analytics dashboard         # Documentation mode (NEW)
```

After any ticket or documentation, you'll see:
```
📦 Add to your workspace?
1. ClickUp - Task management, sprints
2. Notion - Documentation, wikis
3. Skip - Keep as artifact only
```

## 🎛️ Operating Modes

| Mode | Command | When | Output | Offer | Focus | Platform |
|------|---------|------|--------|-------|-------|----------|
| **Interactive** | DEFAULT | No mode | Adaptive | N/A | Guidance | ✅ |
| **Quick** | `$q` | Simple tickets | 2-3 sections | No | Essential | ✅ |
| **Standard** | `$s` | Full tickets | 4-5 sections | **YES** | Complete | ✅ |
| **Complex** | `$c` | Major features | 6-8 sections | **YES** | Phases | ✅ |
| **Spec** | `$spec` | Frontend code | Code blocks | No | Implementation | ✅ |
| **Documentation** | `$doc` | User guides | Feature docs | No | HOW to use | ✅ |

## 📚 Documentation Mode

### Creating Product Documentation

**Start with:**
```
$doc [feature name]
```

**Interactive questions:**
1. Who will read this? (end users/internal/both)
2. What feature are we documenting?
3. How many main features? (1-5)
4. List the features
5. Documentation depth? (overview/detailed/comprehensive)
6. Include visual references? (none/key/all)

**Output structure:**
- ⌘ Overview with audience and version
- ◻️ Feature sections with ◊ components
- → Related materials and resources
- ⚠️ Important notes and limitations
- 📚 Additional resources

### Documentation Examples

**User onboarding:**
```
$doc getting started guide
```

**Feature documentation:**
```
$doc analytics dashboard
```

**Product updates:**
```
$doc new features v2.0
```

### Platform Preferences

Documentation typically goes to:
- **Notion** (preferred) - Knowledge bases, wikis
- **ClickUp** - Help center articles
- **Skip** - Standalone documentation

## 📦 Platform Integration Flow

### After Ticket/Documentation Creation
```markdown
Your [ticket/documentation] is ready!
[Content displayed]

📦 Add to your workspace?
1. **ClickUp** - Task management, sprints, time tracking
2. **Notion** - Documentation, knowledge base, wikis
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

### Smart Platform Detection
- **ClickUp detects**: Sprint planning, bug tracking, time tracking, tasks
- **Notion detects**: Documentation, wikis, knowledge bases, guides
- **Both handle**: General features, project management

### What Happens Next
1. **You choose platform** → System passes content to MCP
2. **MCP analyzes content** → Detects patterns automatically
3. **Creates structure** → Appropriate workspace setup
4. **Confirms completion** → Link to new workspace item

## 🔧 Installing MCP Tools

### Docker Setup (AI-Assisted)

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))

**Installation:**

Copy this prompt to any AI assistant for complete setup instructions:
```
Help me set up Docker containers for Product & Dev Writer MCP tools v4.4.0.

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
| **Documentation** | Sequential | 2-3 | Notion preferred |

## 🆘 Troubleshooting

### Documentation Mode
- **Not working?** - Use `$doc` command
- **Questions missing?** - Interactive asks audience, features, depth
- **Wrong symbols?** - ◻️ for features, ◊ for components
- **Platform choice?** - Notion preferred for docs

### Platform Integration
- **Not seeing offer?** - Appears after every ticket/doc in chat
- **MCP unavailable?** - Check Docker containers running
- **API errors?** - Verify API keys in `.env`
- **Wrong workspace?** - MCPs auto-detect patterns

### Ticket Issues
- **Not seeing "About"?** - First heading always `# ⌘ About`
- **Too verbose?** - v4.4 maintains 20% concision
- **Wrong scope?** - System asks, never assumes
- **Missing labels?** - System prompts for them

### Interactive Offers
- **Not seeing?** - Only for $s and $c modes
- **Want direct?** - Choose option 2
- **Changed mind?** - Can switch mid-flow

### Docker/MCP Issues
- **Docker not running**: Start Docker Desktop
- **Container errors**: Check logs with `docker-compose logs`
- **Permission denied**: Use admin/sudo
- **Port conflicts**: Change ports in docker-compose.yml

## ⚠️ Important Notes

### Core Features
- **6 operating modes** - Including new $doc for documentation
- **Platform integration** - Always offered after creation
- **First heading** - "About" (⌘) for tickets, "Overview" (⌘) for docs
- **20% more concise** - All content streamlined
- **Global checklists** - Max 3 items/section (tickets)
- **Interactive default** - No mode = conversational guidance
- **Scope/labels required** - User always specifies (tickets)
- **No assumptions** - System asks when unclear

### Documentation Features
- **User-focused** - Product documentation, not technical specs
- **◻️ symbols** - For feature sections
- **Interactive questions** - Audience, depth, visuals
- **Platform preference** - Notion for knowledge bases
- **Visual references** - Screenshots and tutorials described
- **Tips & practices** - User-friendly guidance

### Platform Integration
- **Always in chat** - Never in ticket/doc artifact
- **Three options** - ClickUp, Notion, or Skip
- **Smart detection** - MCPs analyze content patterns
- **No mapping needed** - Trust platform intelligence
- **Graceful fallback** - Works without MCPs
- **Doc preference** - Notion for documentation

### Technical Details
- **Complex flexible** - Phases OR child tickets
- **Spec concise** - 1-3 questions, working code
- **Doc structured** - ◻️ features with ◊ components
- **Always artifacts** - Every ticket/doc in markdown
- **Checkbox format** - Uses `[]` without space
- **Requirements dividers** - Between subsections

## 📦 Version History

- **v4.4.0**: Documentation mode ($doc), user guides, ◻️ feature sections
- **v4.3.0**: Platform integration (ClickUp/Notion), MCP handoff
- **v4.2.1**: Updated About icon (⌘), checkbox format `[]`
- **v4.2.0**: First heading "About", 20% more concise
- **v4.1.0**: Global Resolution Checklists (max 3/section)
- **v4.0.0**: 5 modes, Interactive offers, concise Spec
- **v3.5.0**: User-specified scope and labels
- **v3.4.0**: Structured descriptions (⚠️/≈)
- **v3.0.0**: Mandatory Resolution Checklists
- **v2.0.0**: Interactive mode default
- **v1.0.0**: WHAT/WHY philosophy

## 📚 Additional Resources

### Product Management
- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [Documentation Best Practices](https://www.writethedocs.org/guide/)

### Platform Documentation
- [ClickUp API Docs](https://clickup.com/api)
- [Notion API Guide](https://developers.notion.com/)
- [MCP Protocol Guide](https://modelcontextprotocol.io/)

### Technical Resources
- [MDN Web Docs](https://developer.mozilla.org/) (for spec mode)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Claude Desktop Setup](https://claude.ai/docs/desktop)
- [Technical Writing Guide](https://developers.google.com/tech-writing)

---

*Transform vague requests into crystal-clear tickets and create user-focused documentation with instant workspace integration. Interactive guidance by default. Platform intelligence handles ClickUp/Notion creation. Documentation mode for product guides. Complex mode adapts to your needs. Resolution Checklists use outcome-focused approach. Every ticket and doc scannable in under 2 minutes, then seamlessly added to your workspace.*