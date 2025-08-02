# Dev Ticket Writer - User Guide v3.0.0

## 🚀 What is This?

The Dev Ticket Writer system transforms any request into clear, actionable development tickets. Instead of vague requirements or technical jargon, you get tickets that communicate user value and business outcomes, letting developers focus on HOW to implement.

**Key Benefits:**
- Transform unclear requests into actionable tickets
- Communicate user value and business impact clearly
- Get consistent ticket format across your team
- Focus on WHAT and WHY, not HOW
- Save time with structured templates
- Professional presentation with abstract symbols throughout
- **Interactive mode for guided ticket creation (DEFAULT)**
- **Intelligent partial input enhancement**
- **Enhanced MCP tool selection for optimal analysis**
- **NEW: Figma integration for better design understanding**

**Key Principle:** If a ticket takes more than 2 minutes to read, it's too long.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v2.2"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Writer - Dev Tickets - v2.2.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Upload all reference documents to your project:
- `Ticket - Interactive Mode - v1.3.0.md` (conversational ticket creation with Figma)
- `Ticket - Examples Library - v1.0.0.md` (comprehensive examples for all modes)
- `Ticket - Templates & Standards - v1.0.0.md` (core templates and formatting)
- `Ticket - Quick Reference Card - v1.0.0.md` (daily reference guide)

### Step 4: Start Writing Tickets!
Begin any conversation in the project, and Claude will default to Interactive Mode, guiding you through creating professional tickets.

.

## 🧠 Enhanced Intelligence: Triple MCP Support

### What's New in v2.2?
The Dev Ticket Writer now intelligently chooses between three tools based on your needs:

1. **Sequential Thinking MCP** - For straightforward, linear analysis
2. **Cascade Thinking MCP** - For complex scenarios requiring exploration
3. **Figma MCP** - For understanding designs to write better requirements (NEW)

The system automatically selects the best tool(s) and adapts the analysis approach.

### Intelligent Selection Logic

**Sequential Thinking is chosen for:**
- Simple feature requests with clear scope
- Quick (`$q`) and Standard (`$s`) mode tickets
- Bug fixes and performance improvements
- Single-feature implementations

**Cascade Thinking is chosen for:**
- Interactive mode conversations (`$interactive`)
- Complex (`$c`) and Epic (`$e`) mode tickets
- Multi-phase implementations
- Features with interconnected dependencies

**Figma MCP is used when:**
- User has Figma designs available
- Creating tickets for any UI features
- Need to understand user flows and interactions
- Want to identify all states (error, success, loading)
- Assessing feature complexity from designs
- User explicitly asks for design details

### Adaptive Thought Process

The system uses a flexible approach:
- **Simple requests:** 1-2 thoughts
- **Standard features:** 2-3 thoughts
- **Interactive conversations:** 3-5 thoughts
- **Complex analysis:** 3-5 thoughts with branching
- **Epic breakdown:** 5+ thoughts with exploration

.

## 🎯 How to Use

### Basic Usage (Interactive Mode - DEFAULT)
Simply describe what you need:
```
We need a team dashboard for our collaboration tool
```

The system will:
1. Start Interactive Mode by default
2. Guide you through key questions
3. Offer Figma review for UI features (if available)
4. Choose appropriate MCP tools
5. Generate the perfect ticket

### With Figma Designs:
```
User: Create a ticket for our new onboarding flow
System: [Asks key questions about the feature]
System: I notice this involves multiple screens. Do you have Figma designs I can review?
User: Yes, here's the link: figma.com/file/ABC123
System: [Reviews designs to understand flow, states, and complexity]
System: [Creates comprehensive ticket based on full understanding]
```

### Mode Selection
| Mode | Command | Use For | Typical MCPs Used |
|------|---------|---------|-------------------|
| **Interactive** | `$interactive` or `$int` | DEFAULT - Guided creation | Cascade + Figma |
| **Quick** | `$q` | Simple features (explicit only) | Sequential |
| **Standard** | `$s` | Most features (explicit only) | Sequential |
| **Complex** | `$c` | Multi-phase work (explicit only) | Cascade + Figma |
| **Epic** | `$e` | Major initiatives (explicit only) | Cascade + Figma |

.

## ✅ Output Format

### Every Ticket Includes:
1. **Always in an artifact** (for easy copying)
2. **MCP tools notation** (which tools were used)
3. **Mode notation** (which mode was used)
4. **Figma integration status** (if applicable)
5. **User Value statement** (why it matters)
6. **Business Goal** (measurable impact)
7. **Requirements** (outcome-focused)
8. **Success Criteria** (measurable)
9. **Design References** (Figma links when available)
10. **Dependencies** (related tickets)

### Example with Figma Context:
```markdown
MODE: $interactive → $standard
TICKET TYPE: Feature
MCP USED: Cascade Thinking + Figma
FIGMA INTEGRATED: Yes (for context)

### ❖ Team Dashboard

**User Value:** See your team's progress and collaborate effectively in one place

**Business Goal:** Increase team collaboration by 40%

---

## → Designs & References
- [Figma - Team Dashboard](figma://file/ABC123)
- **Notice:** Design shows 3 main sections with real-time updates

---

## ◇ Requirements
- Display team activity feed with recent updates
- Show performance metrics in scannable cards
- List active projects with progress
- Support filtering by member and time
- Handle empty states gracefully
- Auto-refresh without losing context

---

## ✓ Success Criteria
- [ ] Dashboard loads in <2 seconds
- [ ] 50% reduction in status meetings
- [ ] All data updates within 30 seconds
- [ ] Works on tablet and desktop
```

.

## 🎨 Figma Integration (NEW in v2.2)

### How Figma Helps
Figma MCP helps the ticket writer **understand designs** to write better requirements. It does NOT extract technical specifications.

### When Figma Adds Value:
- **Any UI features** - Even simple ones, if designs exist
- **Complex UI flows** - Multiple screens with interactions
- **New features** - Understanding the complete user journey
- **Major redesigns** - Seeing all the changes in context
- **Component updates** - Knowing what specifically changed
- **Multi-state interfaces** - Forms with validation, wizards, etc.

### When to Skip Figma:
- Backend-only features
- Performance improvements
- Database changes
- API development
- When user says not to use it

### Special Cases:
- **If user requests specs**: System will extract technical details
- **Simple UI features**: Can still use Figma if it helps understand context
- **Component updates**: References changes without extracting specs (unless requested)

### First-Time Setup:
1. When offered Figma integration, you'll need an API key
2. Go to Figma → Account Settings → Personal Access Tokens
3. Create a new token and share it with the system
4. This is a one-time setup per environment

### What Figma Provides:
- Understanding of complete user flows
- Identification of all necessary states
- Complexity assessment
- Better requirement completeness
- Technical specifications when explicitly requested
- Component change references

.

## 🔧 Installing MCP Tools (Recommended)

The system intelligently selects between these based on task complexity. Choose either Docker (stable) or NPX (quick) installation:

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the Dev Ticket Writer MCP tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/arben-adm/mcp-sequential-thinking.git
   - https://github.com/drewdotpro/cascade-thinking-mcp.git
   - https://github.com/modelcontextprotocol/servers/tree/main/src/figma
3. Create a docker-compose.yml file with services for all three
4. Configure Claude Desktop's claude_desktop_config.json
5. Start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for 3 running containers
2. Look for the 🔌 icon in Claude Desktop showing available tools
3. Test with: "Create a ticket for user login"

### Option B: NPX Installation (Quick but Less Stable)

Add to Claude Desktop config file:
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
    },
    "figma": {
      "command": "npx",
      "args": ["-y", "@figma/mcp-server"]
    }
  }
}
```

.

## 🆘 Troubleshooting

### "Should I use Figma for this ticket?"
- Use for complex UI features with multiple screens
- Skip for backend, bugs, or simple changes
- It's always optional - never required

### "Figma asks for an API key"
- One-time setup: Figma → Settings → Personal Access Tokens
- Create token and share with system
- Stored securely in local configuration

### "Can't access Figma file"
- Check file permissions
- Ensure URL is complete
- Can always proceed without Figma

### "Ticket includes technical specs"
- This shouldn't happen in v2.2
- Figma is for understanding, not spec extraction
- Requirements should focus on WHAT, not HOW

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **Wrong directory**: Check you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Ensure Node.js is installed for NPX method
- **Containers won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **Rate limits**: All tools handle this gracefully with retries

### Other Issues:
- **No MCP tools**: System works without them
- **Wrong MCP selection**: Based on complexity
- **Interactive not wanted**: Use explicit mode (`$q`, `$s`, etc.)
- **Ticket too long**: Use simpler mode or break down

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For general issues: The AI assistant can help diagnose problems

.

## ⚠️ Important Notes

- **Interactive mode is DEFAULT** - Unless explicitly specified otherwise
- **Never include HOW** - Focus on WHAT and WHY
- **Always under 2 minutes** - Break down if longer
- **No em dashes** - Uses commas, colons, or periods
- **Works without MCPs** - But enhanced with them

## 📦 Version History

- **v2.2.0**: Figma integration, enhanced MCP selection
- **v2.1.0**: Interactive mode as default, partial input handling
- **v2.0.0**: Added MCP integration and visual dashboards
- **v1.0.0**: Initial ticket writing system

## 🎯 Key Principles

1. **Democratize product thinking** - Anyone can write great tickets
2. **Focus on user value** - Every ticket starts with user benefit
3. **Measurable outcomes** - Success criteria must be specific
4. **Developer freedom** - Define WHAT, let them decide HOW
5. **2-minute readability** - Respect everyone's time

.

## 📚 Other Resources

- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Sequential Thinking MCP](https://github.com/arben-adm/mcp-sequential-thinking)
- [Cascade Thinking MCP](https://github.com/drewdotpro/cascade-thinking-mcp)
- [Figma MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/figma)

---

*Transform vague requests into clear, actionable tickets. Make product thinking accessible to everyone.*