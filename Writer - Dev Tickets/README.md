# Dev Ticket Writer - User Guide v4.1.0

The Dev Ticket Writer helps teams create professional development tickets that are "clear at first glance" for developers while teaching product thinking principles. By focusing on WHAT needs to be done and WHY it matters (not HOW to implement), it bridges the communication gap between product and development. When implementation details are needed, the concise Spec mode provides focused, copy-paste ready solutions.

## 🆕 What's New in v4.1.0

- **Global Resolution Checklists**: Maximum 3 items per section, outcome-focused approach
- **Clearer Work Streams**: Think in deliverables, not tasks
- **Improved Readability**: Checklists scannable in seconds
- **Better Developer Experience**: High-level guidance without micromanagement
- **Maintained Features**: All v4.0.0 features preserved with enhanced clarity

## ✨ Key Features

- **Developer-First Clarity**: User-specified scope prefixes, structured descriptions
- **5 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $spec
- **Interactive Offers**: Automatic guidance offers for $standard and $complex modes
- **Global Resolution Approach**: Max 3 items per section, outcome-focused checklists
- **Concise Spec Mode**: Minimal conversation (1-3 questions), working code examples
- **Enhanced Symbol System**: Professional symbols (❖, ◇, **◊**, →, ✓, ⊗, ⚠︎, ⁉) for visual hierarchy
- **Prompt Improvement**: Clarifies vague requests without adding assumptions
- **Educational Focus**: Interactive mode teaches product management through practice
- **2-Minute Rule**: All tickets readable in under 2 minutes

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v4.1"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v4.1.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Quick Reference Card - v3.0.0.md` (Updated with global checklist sizing)
- `Ticket - Templates & Standards - v3.0.0.md` (Major update to Resolution Checklists)
- `Ticket - Examples Library - v3.0.0.md` (All examples updated with global approach)
- `Ticket - Interactive Mode - v1.7.0.md` (Updated for global checklists)
- `Ticket - Spec Mode Frontend Guide - v1.0.0.md` (Concise implementation focus)
- `Ticket - Prompt Improvement - v1.1.0.md` (Request clarification)

### Step 4: Start Creating Tickets
Simply describe what you need:
```
fix login bug                    # Interactive mode (default)
$q user profiles                 # Quick mode
$s dashboard feature             # Standard (offers Interactive)
$c payment integration           # Complex (offers Interactive)
$spec hide scrollbar             # Spec mode (instant generation)
```

## 🎯 Resolution Checklist Philosophy (NEW)

The v4.1.0 update revolutionizes how Resolution Checklists work:

### Core Changes
- **Think in work streams**, not tasks
- **Maximum 3 items per section**
- **Each checkbox = meaningful deliverable**
- **Focus on WHAT gets delivered**, not HOW
- **Each item represents 2-8 hours minimum work**

### Sizing by Mode

| Mode | Total Sections | Items per Section | Total Items |
|------|---------------|-------------------|-------------|
| **Quick** | 2-3 | 2-3 | 4-6 |
| **Standard** | 4-5 | 2-3 | 8-12 |
| **Complex** | 6-8 | 2-3 | 12-20 |

### Example Transformation

**Old Style (Too Detailed):**
```markdown
### Frontend Implementation
- [ ] Create Button.tsx component
- [ ] Add hover state styles
- [ ] Add active state styles
- [ ] Add disabled state styles
- [ ] Import design tokens
- [ ] Set up onClick handlers
- [ ] Add loading spinner
```

**New Style (Global Outcome):**
```markdown
### Component Development
- [ ] Build Button component with all states
- [ ] Add complete test coverage
- [ ] Integrate with component library
```

## 🎯 Interactive Offers

When users specify `$standard` or `$complex`, the system ALWAYS offers Interactive assistance first:

```markdown
User: $s user authentication

System: I see you want a standard ticket for user authentication.

Would you like me to:
1. **Guide you through creating it interactively** - I'll ask questions to ensure we capture everything
2. **Create it directly** - I'll use my best judgment

Which would you prefer? (1 or 2)
```

This ensures users get the best possible ticket quality while respecting their autonomy.

## 🎛️ Operating Modes

| Mode | Command | When to Use | Resolution Sections | Interactive Offer | Focus |
|------|---------|-------------|-------------------|-------------------|-------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Adaptive | N/A (Default) | Conversational guidance |
| **Quick** | `$q` | Simple features (explicit) | 2-3 sections | No | Essential requirements |
| **Standard** | `$s` | Full features (explicit) | 4-5 sections | **YES - Always** | Complete context |
| **Complex** | `$c` | Major features/initiatives | 6-8 sections | **YES - Always** | Phases OR child tickets |
| **Spec** | `$spec` | Frontend implementation | N/A | No | Concise code solutions |

**Note:** Interactive mode is the default unless explicitly specified.

## 🔧 Complex Mode (Enhanced)

Complex mode now offers two approaches for major features:

### Option A: Phased Development
For incremental building of a single large feature:
- Phase 1: Foundation
- Phase 2: Core Features
- Phase 3: Enhancement

### Option B: Child Ticket Breakdown
For multi-team coordination:
- Infrastructure tickets
- Feature implementation tickets
- Quality & polish tickets

The system helps you choose the right approach during ticket creation.

## 💻 Spec Mode (Transformed)

The new Spec mode is concise and efficient:

### Fast Paths (0-1 Questions)
```markdown
User: $spec hide scrollbar
System: Browser compatibility needed?
User: yes
[Generates 20-line CSS solution immediately]
```

### Component Patterns (2-3 Questions)
```markdown
User: $spec virtual scroll table
System: Quick setup:
1. Row count?
2. React/Vue?
User: 50k, React
[Generates 40-line working implementation]
```

### Key Features
- **Auto-detection** of common patterns
- **1-3 questions maximum**
- **20-30 lines for simple, 40-60 for complex**
- **Copy-paste ready code**
- **No placeholders or comments**

## 🎯 Scope Prefixes

Every ticket title includes a user-specified scope prefix:

| Prefix | Use For | Example |
|--------|---------|---------|
| **[BE]** | Backend features | `# ❖ [BE] User Authentication` |
| **[FE]** | Frontend features | `# ❖ [FE] Dashboard Redesign` |
| **[Mobile]** | Mobile app features | `# ❖ [Mobile] Push Notifications` |
| **[FS]** | Full stack features | `# ❖ [FS] Real-time Chat` |
| **[DevOps]** | Infrastructure | `# ❖ [DevOps] CI/CD Pipeline` |
| **[QA]** | Testing features | `# ❖ [QA] Test Automation` |

**Note:** System asks users to specify scope - never assumes.

## 📝 Structured Descriptions

Every ticket uses a concise, structured description format:

```markdown
# ❖ [FE] Advanced Search Filters

Our search functionality is failing to meet user needs and causing lost revenue.

⚠︎ **Key problems/changes:**
* **High abandonment rate** - Users give up before finding what they need
* **No filtering options** - Users scroll through irrelevant results
* **Poor relevance** - Basic keyword matching returns unrelated items

⁉ **Reasons why:**
By implementing comprehensive filtering capabilities, we'll dramatically improve product discovery and increase conversion.

**User Value:** Find exactly what you need with powerful filters
**Business Goal:** Dramatically reduce search abandonment rate
```

## 🏷️ Label System

The system asks users to specify appropriate labels:

### Common Label Categories
- **Type**: feature, bug, improvement, technical-debt
- **Component**: authentication, payments, search, UI
- **Priority**: high, medium, low (if your team uses these)

Example:
```markdown
System: What labels should I add to this ticket?
User: feature, search, filters, high-priority
```

## 💬 Interactive Mode Flow

The default conversational mode:

### Typical Flow
1. User describes feature (no mode specified)
2. System asks about user needs and problems
3. System asks for scope ([BE], [FE], etc.)
4. System asks for labels
5. System asks about success metrics
6. Creates comprehensive ticket with global checklist
7. Delivers with quality dashboard

### Quality Dashboard
```markdown
📊 Interactive Mode Report
Overall Quality Score: 4.5/5 ⭐

✅ Ticket Structure Checklist:
✓ User value clearly stated
✓ Scope properly identified: [FS]
✓ Labels added: feature, search, filters
✓ Business goal measurable
✓ Requirements outcome-focused
✓ Resolution checklist global (max 3 items/section)
✓ 2-minute read test: PASS (1:45)

📋 Resolution Checklist Quality:
Global Approach   ██████████ 100%
Outcome Focus     █████████░ 95%
Section Count     4 sections ✓
Items per Section 2-3 items ✓
```

## 📋 Examples

### Interactive Mode (Default)
```
User: need user profiles
System: [Starts conversation about user needs, then asks for scope and labels]
```

### Standard with Interactive Offer
```
User: $s authentication system
System: Would you like me to:
1. Guide you through creating it interactively
2. Create it directly
User: 1
System: [Starts Interactive flow]
```

### Complex with Phased Approach
```
User: $c real-time collaboration
System: [Offers Interactive, then helps choose between phases or child tickets]
```

### Spec Mode (Concise)
```
User: $spec debounced search input
System: React or Vanilla JS?
User: React
System: [Generates 25-line working implementation]
```

### Global Resolution Checklist Example
```markdown
## ✓ Resolution Checklist

### Foundation Work
- [ ] Set up architecture and dependencies
- [ ] Configure necessary integrations

### Core Development
- [ ] Implement primary functionality
- [ ] Add secondary features
- [ ] Apply UI/UX requirements

### Testing & Validation
- [ ] Complete functional testing
- [ ] Verify cross-browser compatibility

### Documentation
- [ ] Update technical documentation
- [ ] Create user guides if needed
```

## 🔧 Installing MCP Tools (Recommended)

The system intelligently selects between Sequential and Cascade Thinking based on task complexity. Choose either Docker (stable) or NPX (quick) installation:

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
   - https://github.com/sequentialthinking/sequential-thinking-mcp
   - https://github.com/cascadethinking/cascade-thinking-mcp
3. Create a docker-compose.yml file with services for both
4. Configure Claude Desktop's claude_desktop_config.json
5. Start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for 2 running containers
2. Look for the 🔌 icon in Claude Desktop showing available tools
3. Test with: "$q fix login bug"

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
    }
  }
}
```

### MCP Tool Selection

The system intelligently selects thinking tools based on mode:

| Mode | Tool Selection | Thoughts Used |
|------|---------------|---------------|
| **Interactive** | Cascade Thinking | 3-5+ thoughts with branching |
| **Quick ($q)** | Sequential Thinking | 1-3 thoughts for analysis |
| **Standard ($s)** | Sequential Thinking | 1-3 thoughts for analysis |
| **Complex ($c)** | Cascade Thinking | 3-5+ thoughts with branching |
| **Spec ($spec)** | Sequential Thinking | 1-3 thoughts for analysis |

### Figma MCP (Optional)
For UI feature tickets, the system can integrate with Figma to:
- Extract design specifications
- Reference component libraries
- Link to design files

While never required, Figma integration enhances UI-related tickets with direct design references.

## 🆘 Troubleshooting

### Resolution Checklists
- **Too many items?** - Think in work streams, not tasks
- **Too detailed?** - Each item should be a deliverable
- **Not sure how to group?** - Use system layers or feature areas

### Interactive Offers
- **Not seeing offer?** - Only appears for $s and $c modes
- **Want to skip?** - Choose option 2 for direct creation
- **Changed mind?** - System can switch to Interactive mid-flow

### Complex Mode
- **Phases vs Child tickets?** - System helps you choose
- **Too many requirements?** - Consider child ticket approach
- **Need both?** - Hybrid approach possible

### Spec Mode
- **Too many questions?** - Should be 1-3 max
- **Code not working?** - All examples are tested
- **Need more sections?** - Spec mode stays minimal by design

### Scope & Labels
- **Forgot to specify?** - System will ask
- **Wrong scope chosen?** - Be specific about work location
- **Too many labels?** - Keep to 3-5 most relevant

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **Wrong directory**: Check you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Ensure Node.js is installed for NPX method
- **Containers won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **Rate limits**: Both tools handle this gracefully with retries

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For general issues: The AI assistant can help diagnose problems

## ⚠️ Important Notes

- **Global checklists required** - Max 3 items per section, outcome-focused
- **Interactive offers required** - System always offers for $s and $c
- **Scope/labels required** - System asks users to specify
- **No assumptions** - System never guesses
- **Complex mode flexible** - Handles phases OR child tickets
- **Spec mode concise** - 1-3 questions, working code only
- **No percentages** - Use descriptive language
- **Always uses artifacts** - Every ticket/spec in markdown
- **Works without MCPs** - But enhanced with them

## 📦 Version History

- **v4.1.0**: Global Resolution Checklists (max 3 items/section, outcome-focused)
- **v4.0.0**: 5 modes (merged Complex/Epic), Interactive offers, concise Spec mode
- **v3.5.0**: User-specified scope and labels, enhanced Interactive mode
- **v3.4.0**: Structured descriptions (⚠︎/⁉), Spec mode, implementation references
- **v3.0.0**: Introduced mandatory Resolution Checklists
- **v2.0.0**: Interactive mode as default, educational focus
- **v1.0.0**: Initial WHAT/WHY philosophy implementation

## 📚 Additional Resources

- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [MDN Web Docs](https://developer.mozilla.org/) (for spec mode)
- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Sequential Thinking MCP](https://github.com/sequentialthinking/sequential-thinking-mcp)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp)

---

*Transform vague requests into crystal-clear tickets with Interactive guidance. Create concise implementation specs with minimal conversation. Complex mode adapts to your needs. Resolution Checklists now use global, outcome-focused approach for maximum clarity. Make every ticket scannable in under 2 minutes.*