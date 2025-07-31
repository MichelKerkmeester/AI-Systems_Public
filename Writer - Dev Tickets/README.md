# Dev Ticket Writer - User Guide v2.2

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
- `Ticket - Interactive Mode - v1.2.0.md` (conversational ticket creation with Figma)
- `Ticket - Examples - Quick & Standard - v1.1.0.md` (mode examples)
- `Ticket - Examples - Complex & Epic - v1.1.0.md` (advanced examples)
- `Ticket - Examples - Bugs & Improvements - v1.1.0.md` (specialized types)
- `Ticket - Examples - Partial Input Handling - v1.1.0.md` (enhancement patterns)
- `Ticket - Examples - Figma Context.md` (proper Figma usage examples)
- `Ticket - Patterns & Methodology - v1.1.0.md` (quality patterns)

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

## 🔧 Installing MCP Tools (Recommended)

All three MCP tools can be installed using Docker for easy management. This is the recommended approach for stability and ease of use.

### Prerequisites
- Docker Desktop installed and running ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app installed ([Download Claude](https://claude.ai/download))
- At least 2GB of free disk space

### Quick Docker Setup

1. **Create MCP Servers Directory**
```bash
mkdir -p "$HOME/MCP Servers"
cd "$HOME/MCP Servers"
```

2. **Clone the MCP Repositories**
```bash
# Clone Sequential Thinking MCP
git clone https://github.com/arben-adm/mcp-sequential-thinking.git

# Clone Cascade Thinking MCP
git clone https://github.com/drewdotpro/cascade-thinking-mcp.git

# Clone Figma MCP (if available via Docker)
# Note: Check if Figma MCP has Docker support
```

3. **Create Docker Compose File**
Create `docker-compose.yml` in the MCP Servers directory:

```yaml
services:
  # Sequential Thinking MCP Server
  sequential-thinking:
    build:
      context: ./mcp-sequential-thinking
      dockerfile: Dockerfile
    image: mcp-sequential-thinking:latest
    container_name: mcp-sequential-thinking
    restart: always
    environment:
      - PYTHONUNBUFFERED=1
    volumes:
      - sequential-data:/app/data
    networks:
      - mcp-network

  # Cascade Thinking MCP Server
  cascade-thinking:
    build:
      context: ./cascade-thinking-mcp
      dockerfile: Dockerfile
    image: mcp-cascade-thinking:latest
    container_name: mcp-cascade-thinking
    restart: always
    environment:
      - NODE_ENV=production
    volumes:
      - cascade-data:/app/data
    networks:
      - mcp-network

  # Figma MCP Server (if Docker supported)
  figma:
    build:
      context: ./figma-mcp
      dockerfile: Dockerfile
    image: mcp-figma:latest
    container_name: mcp-figma
    restart: always
    environment:
      - FIGMA_API_KEY=${FIGMA_API_KEY}
    volumes:
      - figma-data:/app/data
    networks:
      - mcp-network

volumes:
  sequential-data:
  cascade-data:
  figma-data:

networks:
  mcp-network:
    driver: bridge
```

4. **Configure Claude Desktop**
Update your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-sequential-thinking", "uv", "run", "--with", "portalocker", "-m", "mcp_sequential_thinking.server"]
    },
    "cascade-thinking": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-cascade-thinking", "node", "dist/index.js"]
    },
    "figma": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-figma", "node", "index.js"]
    }
  }
}
```

5. **Start the MCP Servers**
```bash
cd "$HOME/MCP Servers"

# Build and start all containers
docker-compose up -d

# Or start specific services
docker-compose up -d sequential-thinking cascade-thinking
```

6. **Restart Claude Desktop**
Quit and restart Claude Desktop to load the new MCP server configuration.

### Alternative: NPX Installation (Simpler but less stable)

If you prefer not to use Docker, you can use the original NPX method:

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

### Verification
1. **Check Docker Desktop**: You should see running containers
2. **In Claude Desktop**: Look for the 🔌 icon showing available tools
3. **Test the servers**: Try using the thinking tools in a conversation

### Troubleshooting
- **Containers won't start**: Check Docker Desktop is running
- **Claude can't connect**: Restart Claude Desktop after starting containers
- **View logs**: `docker-compose logs -f [service-name]`
- **Reset everything**: `docker-compose down -v && docker-compose up -d`

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

## 🔧 Installing MCP Tools (Recommended)

All three MCP tools can be installed using Docker for easy management. This is the recommended approach for stability and ease of use.

### Prerequisites
- Docker Desktop installed and running ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app installed ([Download Claude](https://claude.ai/download))
- At least 2GB of free disk space

### Quick Docker Setup

1. **Create MCP Servers Directory**
```bash
mkdir -p "$HOME/MCP Servers"
cd "$HOME/MCP Servers"
```

2. **Clone the MCP Repositories**
```bash
# Clone Sequential Thinking MCP
git clone https://github.com/arben-adm/mcp-sequential-thinking.git

# Clone Cascade Thinking MCP
git clone https://github.com/drewdotpro/cascade-thinking-mcp.git

# Clone Figma MCP (if available via Docker)
# Note: Check if Figma MCP has Docker support
```

3. **Create Docker Compose File**
Create `docker-compose.yml` in the MCP Servers directory:

```yaml
services:
  # Sequential Thinking MCP Server
  sequential-thinking:
    build:
      context: ./mcp-sequential-thinking
      dockerfile: Dockerfile
    image: mcp-sequential-thinking:latest
    container_name: mcp-sequential-thinking
    restart: always
    environment:
      - PYTHONUNBUFFERED=1
    volumes:
      - sequential-data:/app/data
    networks:
      - mcp-network

  # Cascade Thinking MCP Server
  cascade-thinking:
    build:
      context: ./cascade-thinking-mcp
      dockerfile: Dockerfile
    image: mcp-cascade-thinking:latest
    container_name: mcp-cascade-thinking
    restart: always
    environment:
      - NODE_ENV=production
    volumes:
      - cascade-data:/app/data
    networks:
      - mcp-network

  # Figma MCP Server (if Docker supported)
  figma:
    build:
      context: ./figma-mcp
      dockerfile: Dockerfile
    image: mcp-figma:latest
    container_name: mcp-figma
    restart: always
    environment:
      - FIGMA_API_KEY=${FIGMA_API_KEY}
    volumes:
      - figma-data:/app/data
    networks:
      - mcp-network

volumes:
  sequential-data:
  cascade-data:
  figma-data:

networks:
  mcp-network:
    driver: bridge
```

4. **Configure Claude Desktop**
Update your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-sequential-thinking", "uv", "run", "--with", "portalocker", "-m", "mcp_sequential_thinking.server"]
    },
    "cascade-thinking": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-cascade-thinking", "node", "dist/index.js"]
    },
    "figma": {
      "command": "docker",
      "args": ["exec", "-i", "mcp-figma", "node", "index.js"]
    }
  }
}
```

5. **Start the MCP Servers**
```bash
cd "$HOME/MCP Servers"

# Build and start all containers
docker-compose up -d

# Or start specific services
docker-compose up -d sequential-thinking cascade-thinking
```

6. **Restart Claude Desktop**
Quit and restart Claude Desktop to load the new MCP server configuration.

### Alternative: NPX Installation (Simpler but less stable)

If you prefer not to use Docker, you can use the original NPX method:

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

### Verification
1. **Check Docker Desktop**: You should see running containers
2. **In Claude Desktop**: Look for the 🔌 icon showing available tools
3. **Test the servers**: Try using the thinking tools in a conversation

### Troubleshooting MCP Installation
- **Containers won't start**: Check Docker Desktop is running
- **Claude can't connect**: Restart Claude Desktop after starting containers
- **View logs**: `docker-compose logs -f [service-name]`
- **Reset everything**: `docker-compose down -v && docker-compose up -d`

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

### Other Issues:
- **No MCP tools**: System works without them
- **Wrong MCP selection**: Based on complexity
- **Interactive not wanted**: Use explicit mode (`$q`, `$s`, etc.)
- **Ticket too long**: Use simpler mode or break down