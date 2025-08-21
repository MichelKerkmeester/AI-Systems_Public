# Product Owner System - User Guide v6.0.0

The Product Owner system helps teams create professional development tickets, implementation specs, product documentation, and text snippets through intelligent interactive guidance. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it bridges the communication gap between product and development teams.

## 📑 Table of Contents

- [🆕 What's New in v6.0.0](#-whats-new-in-v600)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
- [🎯 Automatic Complexity Detection](#-automatic-complexity-detection)
- [💻 Implementation Specs](#-implementation-specs-spec)
- [📚 Documentation](#-documentation-doc)
- [✍️ Text Snippets](#️-text-snippets-text-new)
- [📗 Platform Integration](#-platform-integration)
- [🔧 Installing MCP Tools](#-installing-mcp-tools)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Additional Resources](#-additional-resources)

---

## 🆕 What's New in v6.0.0

### Major Enhancements 🚀

**New $text Mode:**
- Quick snippets and descriptions without elaborate process
- Perfect for component descriptions
- 1-3 thinking rounds typical
- Direct response or simple artifact

**Optimized Architecture:**
- **Reduced from 8 to 5 documents** - Better organization
- **52% smaller token footprint** - Faster processing
- **Single source of truth** - No more redundancy
- **Inline prompt improvement** - Smarter request handling

**Enhanced Features:**
- **Expanded examples** - Real-world tickets and documentation
- **Complete troubleshooting guide** - Self-service problem solving
- **Decision trees** - Faster mode routing
- **Recovery strategies** - Better error handling
- **Smart patterns** - Context-aware responses

### Maintained Excellence
- **Native thinking** - User-controlled rounds (1-10)
- **Unified $ticket mode** - Intelligent auto-scaling
- **All modes interactive** - Conversational guidance
- **Platform Integration** - Direct ClickUp workspace creation
- **Professional formatting** - Consistent symbols and structure

---

## ✨ Key Features

- **5 Intelligent Modes**: Discovery (default), $ticket (auto-scaling), $spec (implementation), $doc (documentation), $text (snippets)
- **Native Thinking**: User-controlled thinking rounds for quality output
- **Interactive Everything**: All modes guide users through creation
- **Automatic Complexity**: Tickets scale from simple (2-3 sections) to complex (6-8 sections)
- **Platform Ready**: Direct ClickUp integration after creation
- **Smart Detection**: System recognizes intent and adjusts accordingly
- **Professional Symbols**: ⌘, ◇, ◻️, ◊, →, ✦, ✔, ⊗, ⚠️, ⌥, 📚
- **Developer Clarity**: User-specified scope, structured descriptions
- **Copy-paste Code**: Spec mode delivers working implementations
- **Quick Content**: Text mode for rapid snippet generation

---

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Product Owner v6.0.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Product Owner - v6.1.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these **5 streamlined documents** to your project's knowledge base:
- `Product Owner - Reference Guide.md` (symbols, templates, standards)
- `Product Owner - Interactive Flows.md` (all mode interactions)
- `Product Owner - Quick Card.md` (daily command reference)
- `Product Owner - Platform Integration.md` (ClickUp handoff)

### Step 4: Install MCP Tools (Optional - for ClickUp only)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating
```
need user authentication         # Discovery flow
$ticket payment integration      # Direct ticket (auto-scales)
$spec modal component           # Direct implementation
$doc analytics dashboard        # Direct documentation
$text error message            # Direct snippet (NEW!)
```

After any creation:
```
📦 Add to your workspace?
1. ClickUp - Task management, sprints
2. Skip - Keep as artifact only
```

---

## 🎛️ Operating Modes

| Mode | Command | Purpose | Output | Thinking |
|------|---------|---------|--------|----------|
| **Discovery** | DEFAULT | Figure out what to create | Varies | 1-10 |
| **Ticket** | `$ticket` | Development tickets | Auto-scales 2-8 sections | 1-10 |
| **Spec** | `$spec` | Frontend implementations | Code blocks | 1-5 |
| **Documentation** | `$doc` | User guides | Feature docs | 1-5 |
| **Text** | `$text` | Quick snippets | Direct/Simple | 1-2 |

### The Enhanced Flow

**No mode specified:**
```
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket - Feature or bug for developers
2. Implementation spec - Frontend code/styling solution
3. Product documentation - User guide or feature docs
4. Text snippet - Quick description or copy

Which best fits? (1-4)
```

**With mode specified:**
- `$ticket` → Straight to ticket questions (auto-scales complexity)
- `$spec` → Straight to implementation questions
- `$doc` → Straight to documentation questions
- `$text` → Minimal questions for quick content (NEW!)

**Thinking Rounds (asked after mode selection):**
```
How many thinking rounds should I use? (1-10)
• Simple requests: 1-2 rounds
• Standard features: 3-5 rounds  
• Complex initiatives: 6-10 rounds

Suggested for your request: [X-Y rounds]
```

---

## 🎯 Automatic Complexity Detection

### For $ticket Mode

The system intelligently detects complexity based on your responses:

| Indicators | Complexity | Sections | Resolution Items | Suggested Thinking |
|------------|------------|----------|------------------|-------------------|
| Bug fix, small change | **Simple** | 2-3 | 4-6 | 1-2 rounds |
| Feature, clear scope | **Standard** | 4-5 | 8-12 | 3-5 rounds |
| Platform, integration | **Complex** | 6-8 | 12-20 with phases | 6-10 rounds |

### Enhanced Detection Keywords

**Simple Triggers:**
- "fix", "bug", "broken", "error", "typo"
- "update", "change", "modify", "adjust"
- Single component, < 1 week timeline

**Standard Triggers:**
- "feature", "dashboard", "workflow", "process"
- "integration" (single), "redesign"
- Multiple components, 1-3 week timeline

**Complex Triggers:**
- "platform", "architecture", "migration", "enterprise"
- "compliance", "security", "multi-tenant"
- Multiple teams, > 1 month timeline

### Example Flow with Phases (Complex)
```
User: $ticket payment platform

System: Let's create your payment platform ticket! 🎯

How many thinking rounds should I use? (1-10)
Suggested for payment platform: 6-8 rounds

User: 7

System: Tell me about this payment platform:
- What payment methods?
- New or updating?
- Compliance needs?

[System detects "platform" + compliance = Complex ticket]
[Automatically creates 6-8 section ticket with:]
- Phase 1: Foundation (Week 1-3)
- Phase 2: Core Features (Week 4-6)
- Phase 3: Advanced Features (Week 7-9)
- Dependencies section (⊗)
- Risks section (⚡)
```

---

## 💻 Implementation Specs ($spec)

### Enhanced Pattern Detection

**Quick Patterns (1-2 questions):**
- CSS utilities, simple components
- Animations, layouts

**Standard Patterns (2-3 questions):**
- Data tables, forms, modals
- State management

**Complex Patterns (3-4 questions):**
- Performance optimization
- Real-time features
- Accessibility compliance

### Example with Full Flow
```
User: $spec infinite scroll

System: Let's build your infinite scroll implementation! 🔧

How many thinking rounds should I use? (1-10)
Suggested: 2-3 for scroll features

User: 3

System: Quick setup:
1. **Framework?** (React/Vue/Vanilla)
2. **Data source?** (API/Local)
3. **Approximate item count?**

User: React, API, thousands

System: Additional details:
4. **Virtual scrolling needed?** (for performance)
5. **Loading indicators?**
6. **Error handling approach?**

User: Yes, skeleton loaders, retry logic

[Generates complete, optimized implementation]
```

---

## 📚 Documentation ($doc)

### Depth-Based Structure

**Three Depth Levels:**
1. **Overview** - High-level, 1-2 paragraphs per feature
2. **Detailed** - Step-by-step, 3-4 paragraphs
3. **Comprehensive** - All details, tips, workflows

### Interactive Documentation Flow
```
User: $doc API authentication

System: Let's document API authentication! 📚

How many thinking rounds should I use? (1-10)
Suggested: 2-3 for API docs

User: 3

System: I'll help create clear API documentation.

1. **Who will read this?** (developers/end users/both)
2. **Authentication methods?** (OAuth/API keys/JWT)
3. **Current state?** (live/beta/planned)

[Continues with depth questions]
[Creates structured documentation with code examples]
```

---

## ✍️ Text Snippets ($text) - NEW!

### Quick Content Generation

Perfect for:
- Error messages
- Component descriptions
- Marketing copy
- UI text
- Email templates
- Status messages

### Minimal Process
```
User: $text error message for payment failure

System: Let's write your error message! ✍️

How many thinking rounds should I use? (1-2 typical)

User: 1

System: Quick context - is this for:
- Customer-facing UI
- Internal logging
- Email notification

User: Customer-facing UI

System: "We couldn't process your payment. Please check your 
card details and try again. If the problem persists, 
contact support at help@example.com"

[Direct response, no artifact needed for single items]
```

### Multiple Snippets
```
User: $text form validation messages

System: Let's write your validation messages! ✍️

How many thinking rounds should I use? (1-2 typical)

User: 2

System: What type of form and tone?

User: User registration, friendly

[Creates artifact with multiple messages]
```

---

## 📗 Platform Integration

### After Every Creation
```markdown
📦 **Add to your workspace?**

1. **ClickUp** - Task management, sprints, time tracking
2. **Skip** - Keep as artifact only

Which option? (1 or 2)
```

### Smart Handoff
- System creates content with proper structure
- User chooses platform
- MCP handles workspace creation
- No manual configuration needed

---

## 🔧 Installing MCP Tools

### Docker Setup (AI-Assisted) - For ClickUp Integration Only

**Prerequisites:**
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop/))
- Claude Desktop ([Download](https://claude.ai/download))

**Installation:**

Copy this prompt to any AI assistant:
```
Help me set up Docker container for ClickUp MCP tool.

I need to:
1. Create directory at "$HOME/MCP Servers"
2. Clone: https://github.com/taazkareem/clickup-mcp-server
3. Create docker-compose.yml for the service
4. Configure claude_desktop_config.json
5. Set up environment variables for ClickUp API key
6. Start container

I'm on [Windows/Mac/Linux]. Give me exact commands.
```

### Getting API Keys

**ClickUp:**
1. Settings → Apps → API Token
2. Generate Personal Token
3. Add to `.env` file

---

## 🆘 Troubleshooting

### Common Issues & Solutions

**Mode Selection:**
- **Discovery not working?** - That's the default, no command needed
- **Wrong mode triggered?** - Use $ prefix for direct mode
- **Complexity wrong?** - Provide more context for better detection

**Thinking Rounds:**
- **Not sure how many?** - System suggests based on complexity
- **Too many/few rounds?** - Adjust based on quality needs
- **Skipped thinking?** - Only skipped during discovery questions

**Output Issues:**
- **Symbols not showing?** - Check markdown artifact type
- **Wrong structure?** - Verify mode and complexity
- **Missing sections?** - May need higher complexity

**Platform Integration:**
- **Not seeing offer?** - Appears after creation in chat
- **MCP unavailable?** - Check Docker container status
- **Wrong workspace?** - MCP auto-detects from content

**Recovery Options:**
- Return to discovery mode
- Ask for clarification
- Use manual copy option
- Restart with different mode

---

## ⚠️ Important Notes

### Core Architecture in v6.0.0
- **5 documents total** - Down from 8, better organized
- **52% smaller** - ~20K tokens vs original 35K
- **Native thinking** - No external tools needed
- **User-controlled rounds** - Choose thinking depth (1-10)
- **Unified ticket mode** - One command, intelligent scaling
- **New $text mode** - Quick snippets without process
- **Tables of contents** - All docs have navigation

### Key Principles
- **Interactive always** - Guidance for quality
- **Auto-detection** - System recognizes patterns
- **Platform neutral** - User chooses destination
- **Outcome focused** - Resolution not tasks
- **2-minute readable** - Concise and clear
- **Thinking transparency** - User controls depth
- **Single source of truth** - No redundancy

### Migration from v5.1.0
- All existing commands work
- New $text mode available
- Better performance (smaller system)
- Enhanced examples and troubleshooting
- Simplified document structure

---

## 📦 Version History

- **v6.0.0**: New $text mode, 52% size reduction, 5-doc architecture, enhanced troubleshooting, decision trees
- **v5.1.0**: Native Claude thinking, user-controlled rounds, removed external MCPs
- **v5.0.0**: Unified $ticket mode, all modes interactive, auto-scaling complexity
- **v4.4.0**: Documentation mode, user guides
- **v4.3.0**: Platform integration
- **v4.2.0**: First heading "About", 20% more concise
- **v4.0.0**: Multiple modes, interactive offers
- **v3.0.0**: Resolution checklists
- **v2.0.0**: Interactive default
- **v1.0.0**: WHAT/WHY philosophy

---

## 📚 Additional Resources

### Product Management
- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [Agile Methodology](https://www.atlassian.com/agile)

### Platform Documentation
- [ClickUp API Docs](https://clickup.com/api)
- [Claude Projects Guide](https://claude.ai/docs/projects)
- [MCP Protocol](https://modelcontextprotocol.io/docs)

### Technical Resources
- [MDN Web Docs](https://developer.mozilla.org/)
- [React Documentation](https://react.dev/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Claude Desktop Setup](https://claude.ai/docs/desktop)

### System Documents
- Writer - Product Owner (Core system prompt)
- Reference Guide (Symbols, templates, standards)
- Interactive Flows (All mode interactions)
- Quick Card (Daily command reference)
- Platform Integration (ClickUp handoff)

---

*Product Owner v6.0.0: Optimized architecture. Five intelligent modes including new $text. Native thinking with user control. Unified ticket scaling. Enhanced troubleshooting. 52% smaller, 100% powerful. Single source of truth for better, faster outcomes.*