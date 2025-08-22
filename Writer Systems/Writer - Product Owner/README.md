# Product Owner System - User Guide v6.2.0

The Product Owner system helps teams create professional development tickets, implementation specs, product documentation, and text snippets through intelligent interactive guidance. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it bridges the communication gap between product and development teams.

## 📑 Table of Contents

- [🆕 What's New in v6.2.0](#-whats-new-in-v620)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
- [🎯 Automatic Complexity Detection](#-automatic-complexity-detection)
- [💻 Implementation Specs](#-implementation-specs-spec)
- [📚 Documentation](#-documentation-doc)
- [✏️ Text Snippets](#️-text-snippets-text)
- [📗 Platform Integration](#-platform-integration)
- [🔧 Installing MCP Tools](#-installing-mcp-tools)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Additional Resources](#-additional-resources)

---

## 🆕 What's New in v6.2.0

### Critical Updates 🔴

**Stricter Formatting Standards:**
- **Table of Contents** - Now MANDATORY for ALL tickets (no exceptions)
- **Section Dividers** - Required between ALL sections (---)
- **Key Problems Format** - Must use `### → Key problems:` with minimum 2 items
- **Reasons Why Format** - Must use `### → Reasons why:` with minimum 2 items
- **Bullet Format** - Always use `- text` format, never bullet symbols
- **Designs & References** - Required section with ◳ symbol (placeholders ok)

**Updated Symbols:**
- **◳** - Designs & References section (was ◘ in v6.0)
- **⋈** - Dependencies section (was ⊗ in v6.0)

**Enhanced Quality Control:**
- **Automatic format validation** - System ensures all requirements met
- **Improved troubleshooting** - Specific fixes for common formatting issues
- **Clearer standards** - No ambiguity in requirements
- **Better examples** - All examples show proper formatting

### Maintained Excellence
- **Native thinking** - User-controlled rounds (1-10)
- **Unified $ticket mode** - Intelligent auto-scaling
- **All modes interactive** - Conversational guidance
- **Platform Integration** - Direct ClickUp workspace creation
- **Professional formatting** - Consistent symbols and structure
- **$text mode** - Quick snippets without elaborate process

---

## ✨ Key Features

- **5 Intelligent Modes**: Discovery (default), $ticket (auto-scaling), $spec (implementation), $doc (documentation), $text (snippets)
- **Native Thinking**: User-controlled thinking rounds for quality output
- **Interactive Everything**: All modes guide users through creation
- **Automatic Complexity**: Tickets scale from simple (2-3 sections) to complex (6-8 sections)
- **Platform Ready**: Direct ClickUp integration after creation
- **Smart Detection**: System recognizes intent and adjusts accordingly
- **Professional Symbols**: ◘, ◇, ◻️, ◊, ◳, →, ✦, ✓, ⋈, ⚡, 📚
- **Strict Formatting**: TOC, dividers, proper Key Problems/Reasons format
- **Developer Clarity**: User-specified scope, structured descriptions
- **Copy-paste Code**: Spec mode delivers working implementations
- **Quick Content**: Text mode for rapid snippet generation

---

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Product Owner v6.2.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Product Owner - v6.2.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these **5 core documents** to your project's knowledge base:
- `Product Owner - Reference Guide - v1.1.0.md` (symbols, templates, standards)
- `Product Owner - Interactive Flows - v1.1.0.md` (all mode interactions)
- `Product Owner - Quick Reference Card - v4.1.0.md` (daily command reference)
- `Product Owner - Platform Integration - v2.1.0.md` (ClickUp handoff)
- `Product Owner - Prompt Improvement - v2.1.0.md` (request clarity enhancement)

### Step 4: Install MCP Tools (Optional - for ClickUp only)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating
```
need user authentication         # Discovery flow
$ticket payment integration      # Direct ticket (auto-scales)
$spec modal component           # Direct implementation
$doc analytics dashboard        # Direct documentation
$text error message            # Direct snippet
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
- `$text` → Minimal questions for quick content

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

### Mandatory Formatting (ALL Tickets)

Every ticket MUST include:
- **Table of Contents** - Complete navigation structure
- **Dividers** - Between ALL sections (---)
- **Key Problems** - `### → Key problems:` with 2+ items using `- text`
- **Reasons Why** - `### → Reasons why:` with 2+ items using `- text`
- **Designs & References** - Section with ◳ symbol (placeholders if no links)
- **Dependencies** - Section with ⋈ symbol when applicable

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

### Example Flow with Proper Formatting
```markdown
[BE] Authentication Fix

## 📑 Table of Contents
- [◘ About](#-about)
- [Key Problems & Reasons](#key-problems--reasons)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)

# ◘ About

Users cannot log in due to token validation error.

---

### → Key problems:
- Authentication tokens expiring prematurely
- All users blocked from platform access

### → Reasons why:
- Critical blocker preventing all user access
- Revenue impact of $50K per hour of downtime

---

## ◳ Designs & References
- [System architecture diagram - to be added]
- [Error logs dashboard - link pending]

---

[Continues with all sections and dividers]
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

### Documentation Symbol Usage
- **◻️** - Feature sections (never in tickets)
- **◊** - Sub-headings (bold)
- **→** - References
- **📚** - Additional resources

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

## ✏️ Text Snippets ($text)

### Quick Content Generation

Perfect for:
- Component descriptions
- Error messages
- Marketing copy
- UX writing
- Email templates

### Minimal Process
```
User: $text error message for payment failure

System: Let's write your error message! ✏️

How many thinking rounds should I use? (1-2 typical)

User: 1

System: Quick context - is this for:
- Customer-facing UI
- Internal logging
- Email notification

User: Customer-facing UI

System: "We couldn't process your payment. Please check your 
card details and try again. If the problem persists, 
contact support."

[Direct response, no artifact needed for single items]
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
- System creates content with proper structure (TOC, dividers, etc.)
- User chooses platform
- MCP handles workspace creation
- All formatting preserved
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

**Formatting Issues:**
- **Missing TOC?** - Required for ALL tickets, no exceptions
- **No dividers?** - Add `---` between ALL sections
- **Wrong Key Problems?** - Use `### → Key problems:` with 2+ items
- **Wrong Reasons Why?** - Use `### → Reasons why:` with 2+ items
- **Bullet symbols?** - Always use `- text` format
- **No Designs section?** - Add with ◳ symbol and placeholders

**Symbol Issues:**
- **Wrong symbols?** - ◳ for Designs, ⋈ for Dependencies
- **Missing symbols?** - Every major section needs its symbol
- **Old symbols?** - Update from v6.0 symbols

**Mode Selection:**
- **Discovery not working?** - That's the default, no command needed
- **Wrong mode triggered?** - Use $ prefix for direct mode
- **Complexity wrong?** - Provide more context for better detection

**Thinking Rounds:**
- **Not sure how many?** - System suggests based on complexity
- **Too many/few rounds?** - Adjust based on quality needs
- **Skipped thinking?** - Only skipped during discovery questions

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

### Critical Requirements in v6.2.0
- **Table of Contents** - MANDATORY for all tickets
- **Dividers** - REQUIRED between all sections
- **Key Problems/Reasons** - MUST use ### → format with 2+ items
- **Bullet Format** - ONLY use `- text` never symbols
- **Designs Section** - ALWAYS include with ◳ symbol
- **Dependencies** - Include with ⋈ when needed

### Core Architecture
- **5 documents** - Optimized and consolidated
- **Native thinking** - No external tools needed
- **User-controlled rounds** - Choose thinking depth (1-10)
- **Unified ticket mode** - One command, intelligent scaling
- **$text mode** - Quick snippets without process
- **Strict standards** - Consistent formatting enforced

### Key Principles
- **Interactive always** - Guidance for quality
- **Auto-detection** - System recognizes patterns
- **Platform neutral** - User chooses destination
- **Outcome focused** - Resolution not tasks
- **Format compliance** - Strict standards maintained
- **Thinking transparency** - User controls depth
- **Single source of truth** - No redundancy

### Migration from v6.0.0
- Update symbols (◳ for Designs, ⋈ for Dependencies)
- Ensure TOC in all tickets
- Add dividers between all sections
- Use ### → format for Key Problems/Reasons
- Replace bullet symbols with `- text`

---

## 📦 Version History

- **v6.2.0**: Stricter formatting standards, updated symbols (◳, ⋈), mandatory TOC/dividers, enforced Key Problems/Reasons format
- **v6.1.0**: Enhanced troubleshooting, improved examples, format validation
- **v6.0.0**: New $text mode, 52% size reduction, 5-doc architecture, decision trees
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

### System Documents (v6.2.0)
- Writer - Product Owner - v6.2.0 (Core system prompt)
- Reference Guide - v1.1.0 (Symbols, templates, standards)
- Interactive Flows - v1.1.0 (All mode interactions)
- Quick Card - v4.1.0 (Daily command reference)
- Platform Integration - v2.1.0 (ClickUp handoff)
- Prompt Improvement - v2.1.0 (Request clarity)

---

*Product Owner v6.2.0: Stricter formatting standards. Updated symbols (◳, ⋈). Mandatory TOC and dividers. Enforced Key Problems/Reasons format. Five intelligent modes. Native thinking with user control. Unified ticket scaling. Single source of truth for consistent, professional outcomes.*