# Product Owner System - User Guide v5.0.0

The Product Owner system helps teams create professional development tickets, implementation specs, and product documentation through intelligent interactive guidance. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it bridges the communication gap between product and development teams.

## 📑 Table of Contents

- [🆕 What's New in v5.0.0](#-whats-new-in-v500)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
- [🎯 Automatic Complexity Detection](#-automatic-complexity-detection)
- [💻 Implementation Specs](#-implementation-specs-spec)
- [📚 Documentation](#-documentation-doc)
- [🔗 Platform Integration](#-platform-integration)
- [🔧 Installing MCP Tools](#-installing-mcp-tools)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Additional Resources](#-additional-resources)

.

## 🆕 What's New in v5.0.0

### Unified & Intelligent System 🎯
- **Unified $ticket mode**: Replaces $quick/$standard/$complex with intelligent auto-scaling
- **All modes interactive**: Every creation flow uses conversational guidance
- **Smart complexity detection**: System automatically scales ticket complexity
- **Skip discovery**: $ticket, $spec, and $doc skip the "what to create" phase
- **Symbol update**: ⌥ replaces ≈ for "Reasons why"
- **Streamlined experience**: Less choices, better outcomes

### Maintained Excellence
- **Platform Integration**: Direct ClickUp/Notion workspace creation
- **Professional formatting**: Consistent symbols and structure
- **Educational focus**: Teaches best practices through interaction
- **2-minute rule**: All content readable in under 2 minutes

.

## ✨ Key Features

- **4 Intelligent Modes**: Discovery (default), $ticket (auto-scaling), $spec (implementation), $doc (documentation)
- **Interactive Everything**: All modes guide users through creation
- **Automatic Complexity**: Tickets scale from simple (2-3 sections) to complex (6-8 sections)
- **Platform Ready**: Direct ClickUp/Notion integration after creation
- **Smart Detection**: System recognizes intent and adjusts accordingly
- **Professional Symbols**: ⌘, ◇, ◻️, ◊, →, ✦, ✓, ⊗, ⚠️, ⌥, 📚
- **Developer Clarity**: User-specified scope, structured descriptions
- **Copy-paste Code**: Spec mode delivers working implementations

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Product Owner v5.0.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Product Owner - Writer - v5.0.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Product Owner - Templates, Standards & Examples - v5.0.0.md`
- `Product Owner - Interactive Mode - v5.0.0.md`
- `Product Owner - Documentation Mode - v5.0.0.md`
- `Product Owner - Spec Mode - v5.0.0.md`
- `Product Owner - Platform Integration - v5.0.0.md`
- `Product Owner - Quick Reference Card - v5.0.0.md`
- `Product Owner - Prompt Improvement - v5.0.0.md`

### Step 4: Install MCP Tools (Recommended)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating
```
need user authentication         # Discovery flow
$ticket payment integration      # Direct ticket (auto-scales)
$spec modal component           # Direct implementation
$doc analytics dashboard        # Direct documentation
```

After any creation:
```
📦 Add to your workspace?
1. ClickUp - Task management, sprints
2. Notion - Documentation, wikis
3. Skip - Keep as artifact only
```

.

## 🎛️ Operating Modes

| Mode | Command | Purpose | Output | Complexity |
|------|---------|---------|--------|------------|
| **Discovery** | DEFAULT | Figure out what to create | Varies | N/A |
| **Ticket** | `$ticket` | Development tickets | Auto-scales 2-8 sections | Automatic |
| **Spec** | `$spec` | Frontend implementations | Code blocks | N/A |
| **Documentation** | `$doc` | User guides | Feature docs | N/A |

### The New Flow

**No mode specified:**
```
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket
2. Implementation spec
3. Product documentation
```

**With mode specified:**
- `$ticket` → Straight to ticket questions
- `$spec` → Straight to implementation questions
- `$doc` → Straight to documentation questions

.

## 🎯 Automatic Complexity Detection

### For $ticket Mode

The system intelligently detects complexity based on your responses:

| Indicators | Complexity | Sections | Resolution Items |
|------------|------------|----------|------------------|
| Bug fix, small change | **Simple** | 2-3 | 4-6 |
| Feature, clear scope | **Standard** | 4-5 | 8-12 |
| Platform, integration | **Complex** | 6-8 | 12-20 |

### Example Flow
```
User: $ticket payment platform

System: Let's create your payment platform ticket! 🎯

Tell me about this payment platform:
- What payment methods?
- New or updating?
- Compliance needs?

[System detects "platform" + multiple requirements = Complex ticket]
[Automatically creates 6-8 section ticket with phases]
```

.

## 💻 Implementation Specs ($spec)

### Interactive & Focused
```
User: $spec data table

System: Let's build your data table! 🔧

Quick setup:
1. Framework? (React/Vue/Vanilla)
2. Features? (sorting, filtering, pagination)
3. Data size?

[Generates optimized, working code]
```

.

## 📚 Documentation ($doc)

### User-Focused Guides
```
User: $doc user dashboard

System: Let's document the user dashboard! 📚

1. Who will read this? (end users/internal/both)
2. How many features to cover?
3. Documentation depth?

[Creates structured user documentation]
```

.

## 🔗 Platform Integration

### After Every Creation
```markdown
📦 **Add to your workspace?**

1. **ClickUp** - Task management, sprints, time tracking
2. **Notion** - Documentation, knowledge base, wikis
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

### Smart Detection
- **ClickUp** detects: Sprints, bugs, tasks, time tracking
- **Notion** detects: Documentation, wikis, knowledge bases
- **Both** handle: General features, project management

.

## 🔧 Installing MCP Tools

### Docker Setup (AI-Assisted)

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))

**Installation:**

Copy this prompt to any AI assistant:
```
Help me set up Docker containers for Product Owner MCP tools v5.0.0.

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

I'm on [Windows/Mac/Linux]. Give me exact commands.
```

### Getting API Keys

**ClickUp:**
1. Settings → Apps → API Token
2. Generate Personal Token
3. Add to `.env`

**Notion:**
1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Create integration
3. Copy token
4. Add to `.env`

.

## 🆘 Troubleshooting

### Mode Issues
- **Discovery not working?** - That's the default, no command needed
- **Ticket complexity wrong?** - System auto-detects, provide more context
- **Spec/Doc discovery?** - They skip discovery, go straight to questions

### Platform Integration
- **Not seeing offer?** - Appears after every creation in chat
- **MCP unavailable?** - Check Docker containers
- **Wrong workspace?** - MCPs auto-detect patterns

### Common Issues
- **Too many choices?** - v5.0 reduced choices, trust the system
- **Missing ⌥ symbol?** - Replaces ≈ for "Reasons why"
- **Want old modes?** - $ticket now handles all complexities

.

## ⚠️ Important Notes

### Core Changes in v5.0.0
- **Unified ticket mode** - One command, intelligent scaling
- **All interactive** - Every mode guides users
- **Skips discovery** - Modes know their purpose
- **Symbol update** - ⌥ for "Reasons why"
- **Smarter system** - Less user choice, better outcomes

### Key Principles
- **Interactive always** - Guidance for quality
- **Auto-detection** - System recognizes patterns
- **Platform neutral** - User chooses destination
- **Outcome focused** - Resolution not tasks
- **2-minute readable** - Concise and clear

.

## 📦 Version History

- **v5.0.0**: Unified $ticket mode, all modes interactive, auto-scaling complexity, ⌥ symbol
- **v4.4.0**: Documentation mode, user guides
- **v4.3.0**: Platform integration
- **v4.2.0**: First heading "About", 20% more concise
- **v4.0.0**: Multiple modes, interactive offers
- **v3.0.0**: Resolution checklists
- **v2.0.0**: Interactive default
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
- [MDN Web Docs](https://developer.mozilla.org/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Claude Desktop Setup](https://claude.ai/docs/desktop)

---

*Product Owner v5.0.0: Unified, intelligent, interactive. One ticket mode that scales automatically. All creation flows guide users to quality. Platform integration seamless. Less choices, better outcomes.*