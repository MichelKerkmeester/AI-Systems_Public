# Product Owner System - User Guide v7.0.0

The Product Owner system transforms requests into professional development tickets, implementation specs, documentation, and text snippets through intelligent interactive guidance with built-in complexity challenging. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it creates lean, actionable artifacts that bridge the communication gap between product and development teams.

## 📑 Table of Contents

- [🆕 What's New in v7.0.0](#-whats-new-in-v700)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
- [🎯 Automatic Complexity Detection](#-automatic-complexity-detection)
- [💻 Implementation Specs](#-implementation-specs-spec)
- [📚 Documentation](#-documentation-doc)
- [✏️ Text Snippets](#️-text-snippets-text)
- [🔗 Platform Integration](#-platform-integration)
- [🧠 ATLAS Thinking Framework](#-atlas-thinking-framework)
- [💡 Challenge Mode](#-challenge-mode)
- [🚨 REPAIR Error Recovery](#-repair-error-recovery)
- [🔧 Installing MCP Tools](#-installing-mcp-tools)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Additional Resources](#-additional-resources)

.

## 🆕 What's New in v7.0.0

### Revolutionary Features 🚀

**ATLAS Thinking Framework:**
- Universal thinking methodology with 5-phase structured approach
- Adaptive depth calibration (1-10 rounds)
- User-controlled thinking for optimal output quality
- Different phases activate based on complexity

**Challenge Mode:**
- Automatic activation at 3+ thinking rounds
- Constructive pushback against unnecessary complexity
- Three intensity levels based on thinking depth
- Always proposes simpler, leaner alternatives

**REPAIR Error Recovery:**
- Structured recovery protocol for handling errors
- Multiple solution paths offered
- Pattern learning from errors
- Graceful degradation maintaining functionality

**Advanced Intelligence:**
- Pattern learning and adaptation within sessions
- Context preservation across interactions
- Smart calibration based on complexity factors
- Session awareness with preference tracking

**Streamlined Documentation:**
- 50% reduction in system documentation size
- Improved maintainability and clarity
- Smart references between documents
- Balanced detail with external references

### Enhanced from v6.2.0
- All formatting standards maintained (TOC, dividers, Key Problems/Reasons)
- Symbol consistency (◳ for Designs, ⋈ for Dependencies)
- Platform integration with ClickUp MCP
- 5 operating modes with interactive guidance
- Professional output standards

.

## ✨ Key Features

- **🧠 ATLAS Framework**: 5-phase universal thinking methodology with adaptive depth
- **💡 Challenge Mode**: Active complexity challenging with lean alternatives
- **🎯 Smart Complexity**: Automatic detection and scaling (Simple/Standard/Complex)
- **🔄 Pattern Learning**: Adapts to user preferences and successful patterns
- **🚨 REPAIR Protocol**: Structured error recovery with learning
- **📊 Thinking Calibration**: Formula-based recommendations (1-10 rounds)
- **🎛️ 5 Intelligent Modes**: Discovery, $ticket, $spec, $doc, $text
- **🔗 Platform Ready**: Direct ClickUp integration after creation
- **📝 Professional Symbols**: 📘, ◇, ◻️, ◊, ◳, →, ✦, ✓, ⋈, ⚡, 📚
- **📋 Strict Formatting**: TOC, dividers, proper Key Problems/Reasons format
- **⚡ Phased Delivery**: Automatic breakdown of large initiatives
- **🎪 Session Context**: Tracks preferences and adapts behavior

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Product Owner v7.0.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `product-owner-main-updated.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these **6 essential documents** to your project's knowledge base:
- `Product Owner - ATLAS Thinking Framework.md` (ATLAS thinking methodology)
- `Product Owner - Reference Guide.md` (symbols, templates, standards)
- `Product Owner - Interactive Flows.md` (all mode interactions with Challenge Mode)
- `Product Owner - Quick Card.md` (daily command reference)
- `Product Owner - Platform Integration.md` (ClickUp handoff)
- `Product Owner - Prompt Improvement.md` (request clarity enhancement)

### Step 4: Install MCP Tools (Optional - for ClickUp only)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating
```
need user authentication         # Discovery flow with intelligent guidance
$ticket payment integration      # Direct ticket with auto-scaling
$spec modal component           # Direct implementation spec
$doc analytics dashboard        # Direct documentation
$text error message            # Direct snippet (always artifact)
```

.

## 🎛️ Operating Modes

| Mode | Command | Purpose | Output | Interactive |
|------|---------|---------|--------|-------------|
| **Discovery** | DEFAULT | Figure out what to create | Varies | Yes |
| **Ticket** | `$ticket` | Development tickets | Auto-scales 2-8 sections | Yes |
| **Spec** | `$spec` | Frontend implementations | Code blocks | Yes |
| **Documentation** | `$doc` | User guides | Feature docs | Yes |
| **Text** | `$text` | Quick snippets | Artifact always | Minimal |

### Discovery Flow (Default)
When no mode is specified, the system helps determine what to create:

```
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket - Feature or bug for developers
2. Implementation spec - Frontend code/styling solution
3. Product documentation - User guide or feature docs
4. Text snippet - Quick description or copy

Which best fits? (1-4)
```

### Direct Mode Activation
Use $ prefix to skip discovery:
- `$ticket` → Straight to ticket questions
- `$spec` → Straight to implementation questions
- `$doc` → Straight to documentation questions
- `$text` → Minimal questions for quick content

.

## 🎯 Automatic Complexity Detection

### For $ticket Mode

The system intelligently detects complexity based on your responses:

| Indicators | Complexity | Sections | Resolution Items |
|------------|------------|----------|------------------|
| Bug fix, update | **Simple** | 2-3 | 4-6 |
| Feature, dashboard | **Standard** | 4-5 | 8-12 |
| Platform, architecture | **Complex** | 6-8 with phases | 12-20 |

### Mandatory Formatting (ALL Tickets)

Every ticket MUST include:
- **Table of Contents** - Sections only (no subsections)
- **Dividers** - Between ALL sections (---)
- **Key Problems** - `### → Key problems:` with 2+ items, NOT in TOC
- **Reasons Why** - `### → Reasons why:` with 2+ items, NOT in TOC
- **QA Warning** - Above Resolution Checklist
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

### Example Structure
```markdown
[BE] Authentication Fix

## 📋 Table of Contents
- [📘 About](#-about)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)

# 📘 About

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

## ✓ Resolution Checklist

⚠️ Complete all Resolution Checklist items before moving to QA

[] Fix token validation logic
[] Add comprehensive test coverage
[] Deploy hotfix to production

[Continues with all sections and dividers]
```

.

## 💻 Implementation Specs ($spec)

### Pattern Detection

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

### Example Flow
```
User: $spec infinite scroll

System: Let's build your infinite scroll implementation! 🔧

How many thinking rounds should I use? (1-10)
Based on your request, I recommend: 2-3 rounds

User: 2

Quick setup:
1. **Framework?** (React/Vue/Vanilla)
2. **Data source?** (API/Local)

[Generates complete, optimized implementation as artifact]
```

.

## 📚 Documentation ($doc)

### Depth-Based Structure

**Three Depth Levels:**
1. **Overview** - High-level, 1-2 paragraphs per feature
2. **Detailed** - Step-by-step, 3-4 paragraphs
3. **Comprehensive** - All details, tips, workflows

### Documentation Symbol Usage
- **◻️** - Feature sections
- **◊** - Sub-headings (bold)
- **→** - References
- **📚** - Additional resources

### Interactive Flow
```
User: $doc API authentication

System: Let's document API authentication! 📚

How many thinking rounds should I use? (1-10)
Based on documentation, I recommend: 2-3 rounds

User: 3

I'll help create clear API documentation.

1. **Who will read this?** (developers/end users/both)
2. **Authentication methods?** (OAuth/API keys/JWT)

[Creates structured documentation artifact]
```

.

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

How many thinking rounds should I use? (1-2 typical for snippets)

User: 1

Quick context - is this for:
- Customer-facing UI
- Internal logging

User: Customer-facing UI

[Creates artifact with error message]
```

.

## 🔗 Platform Integration

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
- All formatting preserved
- Pattern learning tracks preferences

.

## 🧠 ATLAS Thinking Framework

### The Five Phases

| Phase | Name | Purpose | When Active |
|-------|------|---------|-------------|
| **A** | Assess & Challenge | Map reality, challenge | Always |
| **T** | Transform & Expand | Generate solutions | 3+ rounds |
| **L** | Layer & Analyze | Build frameworks | 5+ rounds |
| **A** | Assess Impact | Red team | 7+ rounds |
| **S** | Synthesize & Ship | Decide and deliver | Always |

### Thinking Round Calibration

**System asks after mode selection:**
```
How many thinking rounds should I use? (1-10)

Based on your request, I recommend: [X rounds]
- Complexity: [Low/Medium/High] - [reason]
- Uncertainty: [Low/Medium/High] - [reason]
- Stakes: [Low/Medium/High] - [reason]

Or specify your preferred number.
```

**Automatic Calibration Formula:**
```python
total = 1 + complexity + uncertainty + stakes
# Adjusted by pattern learning
```

### Phase Activation by Rounds
- **1-2 rounds:** A → S (Quick assess and ship)
- **3-4 rounds:** A → T → S (Add exploration)
- **5-6 rounds:** A → T → L → S (Add analysis)
- **7-8 rounds:** Full ATLAS cycle
- **9-10 rounds:** Deep ATLAS with iterations

.

## 💡 Challenge Mode

### Automatic Activation
Challenge Mode activates automatically at 3+ thinking rounds to ensure lean, focused solutions.

### Challenge Hierarchy

**Level 1: Gentle (1-2 rounds)**
```
"Could this be simpler?"
"What's the minimal version?"
```

**Level 2: Constructive (3-5 rounds)**
```
"That would work, but a simpler approach would be..."
"The lean approach here would be to..."
```

**Level 3: Strong (6-10 rounds)**
```
"Are we solving the right problem?"
"This adds unnecessary complexity. We can achieve the same with..."
```

### Common Challenge Patterns

**Scope Challenges:**
- Start with fewer features
- Phase the delivery
- Focus on core value

**Build vs Buy:**
- Use existing solutions
- Leverage libraries
- Consider platforms

**Phasing Example:**
```
Original: Complete payment platform (6 months)
Challenge: Phase it?
Result: 
- Phase 1: Cards only (2 weeks)
- Phase 2: Alternative payments (2 weeks)
- Phase 3: Optimization (2 weeks)
```

### User Response Handling
- **Acceptance:** Reduce complexity, deliver faster
- **Rejection:** Document justification, proceed
- **Negotiation:** Create phased approach

.

## 🚨 REPAIR Error Recovery

### The REPAIR Framework

**R**ecognize - Detect error pattern  
**E**xplain - Plain language impact  
**P**ropose - Three solution options  
**A**dapt - Adjust to user choice  
**I**terate - Test and improve  
**R**ecord - Prevent recurrence  

### Common Recovery Scenarios

**Over-Complex Solution:**
- Recognize: Too many sections for simple need
- Propose: Core sections only
- Result: Simplified, focused ticket

**Scope Creep:**
- Recognize: Requirements expanded during creation
- Propose: Phase delivery
- Result: Manageable sprints

**Unclear Requirements:**
- Recognize: High uncertainty
- Propose: Prototype, gather details, or start minimal
- Result: Validated approach

.

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

.

## 🆘 Troubleshooting

### Challenge Mode Issues
- **Too aggressive?** - Specify lower thinking rounds
- **Not challenging?** - Check if 3+ rounds selected
- **Wrong alternatives?** - Provide more context

### ATLAS Framework
- **Phase confusion?** - Check thinking round mapping
- **Skipped phases?** - Normal for low-round requests
- **Too much thinking?** - Reduce rounds

### Pattern Learning
- **Not adapting?** - Patterns establish after 3 similar requests
- **Wrong defaults?** - Will adjust after 2 overrides
- **Too rigid?** - System learns from rejections

### REPAIR Protocol
- **Not recognizing errors?** - Flag explicitly
- **Wrong proposals?** - Choose different path
- **Not learning?** - Patterns update after each recovery

### Formatting Issues
- **Missing TOC?** - Required for ALL tickets (sections only)
- **TOC has subsections?** - Remove Key Problems/Reasons from TOC
- **No dividers?** - Add `---` between ALL sections
- **Wrong Key Problems?** - Use `### → Key problems:` with 2+ items
- **Wrong Reasons Why?** - Use `### → Reasons why:` with 2+ items
- **No QA warning?** - Add above Resolution Checklist
- **No Designs section?** - Add with ◳ symbol and placeholders

### Artifact Issues
- **Not creating artifacts?** - ALL outputs must be artifacts
- **Text as direct response?** - Even snippets need artifacts

### Mode Selection
- **Discovery not working?** - That's the default, no command needed
- **Wrong mode triggered?** - Use $ prefix for direct mode
- **Complexity wrong?** - Provide more context for better detection

### Platform Integration
- **Not seeing offer?** - Appears after creation in chat
- **MCP unavailable?** - Check Docker container status
- **Pattern not tracking?** - Choices recorded after 3 similar

.

## ⚠️ Important Notes

### New in v7.0.0
- **ATLAS Framework** - Universal thinking methodology
- **Challenge Mode** - Automatic at 3+ rounds
- **REPAIR Protocol** - Structured error recovery
- **Pattern Learning** - Session-based adaptation
- **Streamlined Docs** - 50% size reduction
- **Artifact Enforcement** - ALL outputs as artifacts

### Critical Requirements (Maintained)
- **Table of Contents** - MANDATORY for all tickets (sections only)
- **Key Problems/Reasons** - NOT in TOC, ### → format, 2+ items
- **QA Warning** - Above Resolution Checklist
- **Dividers** - Between ALL sections
- **Bullet Format** - ONLY use `- text` never symbols
- **Designs Section** - ALWAYS include with ◳ symbol
- **Dependencies** - Include with ⋈ when needed

### Core Architecture
- **6 essential documents** - Streamlined and consolidated
- **Native thinking** - User-controlled rounds (1-10)
- **Unified ticket mode** - Intelligent auto-scaling
- **5 operating modes** - All interactive
- **Strict standards** - Consistent formatting
- **Challenge integration** - Lean bias throughout

### Key Principles
- **Challenge complexity** - Always seek simpler solutions
- **Learn continuously** - Adapt from every interaction
- **Phase delivery** - Break down large initiatives
- **User empowerment** - Control thinking depth
- **Constructive pushback** - Don't just accept
- **Pattern recognition** - Apply successful approaches
- **Error recovery** - REPAIR and learn

.

## 📦 Version History

- **v7.0.0**: ATLAS Framework, Challenge Mode, REPAIR Protocol, pattern learning, streamlined docs (50% reduction)
- **v6.2.0**: Stricter formatting standards, updated symbols (◳, ⋈), mandatory TOC/dividers
- **v6.1.0**: Enhanced troubleshooting, improved examples, format validation
- **v6.0.0**: New $text mode, 52% size reduction, 5-doc architecture
- **v5.1.0**: Native Claude thinking, user-controlled rounds
- **v5.0.0**: Unified $ticket mode, all modes interactive
- **v4.4.0**: Documentation mode, user guides
- **v4.3.0**: Platform integration
- **v4.2.0**: First heading "About"
- **v4.0.0**: Multiple modes, interactive offers
- **v3.0.0**: Resolution checklists
- **v2.0.0**: Interactive default
- **v1.0.0**: WHAT/WHY philosophy

.

## 📚 Additional Resources

### Core System Documents
- `product-owner-main-updated.md` - Main system prompt
- `Product Owner - ATLAS Thinking Framework.md` - Universal thinking methodology
- `Product Owner - Reference Guide.md` - Symbols, templates, standards
- `Product Owner - Interactive Flows.md` - Mode interactions with challenges
- `Product Owner - Quick Card.md` - Daily command reference
- `Product Owner - Platform Integration.md` - ClickUp handoff
- `Product Owner - Prompt Improvement.md` - Request clarity enhancement

### Thinking & Methodology
- [ATLAS Framework Guide](Product Owner - ATLAS Thinking Framework.md) - Universal thinking methodology
- [Challenge Patterns](Product Owner - Interactive Flows.md#challenge-mode) - Complexity challenging templates
- [REPAIR Protocol](Product Owner - ATLAS Thinking Framework.md#repair-protocol) - Error recovery framework
- [Pattern Learning](Product Owner - Interactive Flows.md#pattern-learning) - Adaptation mechanisms

### Product Management
- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Lean Product Development](https://www.agilealliance.org/agile101/subway-map-to-agile-practices/)
- [Phased Delivery](https://www.productplan.com/glossary/iterative-development/)

### Platform Documentation
- [ClickUp API Docs](https://clickup.com/api)
- [Claude Projects Guide](https://claude.ai/docs/projects)
- [MCP Protocol](https://modelcontextprotocol.io/docs)

### Technical Resources
- [MDN Web Docs](https://developer.mozilla.org/)
- [React Documentation](https://react.dev/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Claude Desktop Setup](https://claude.ai/docs/desktop)

.

*Product Owner v7.0.0: Streamlined for clarity. ATLAS Framework for universal thinking. Challenge Mode for lean solutions. REPAIR Protocol for graceful recovery. Pattern learning for continuous improvement. Five intelligent modes with user-controlled depth. Always challenging complexity, always seeking simplicity.*