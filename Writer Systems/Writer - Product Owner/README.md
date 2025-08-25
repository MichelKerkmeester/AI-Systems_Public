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
- **📐 Professional Symbols**: ⌘, ◇, ◻️, ◊, ◳, →, ✦, ✓, ⋈, ⚡, 📚
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
3. Copy and paste: `product-owner-v7.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these **8 core documents** to your project's knowledge base:
- `product-owner-universal-atlas-framework-v1.md` (ATLAS thinking methodology)
- `product-owner-reference-guide-v2-fixed.md` (symbols, templates, standards)
- `product-owner-interactive-flows-v2.md` (all mode interactions with Challenge Mode)
- `product-owner-quick-card-v5.md` (daily command reference)
- `product-owner-platform-integration-v2-fixed.md` (ClickUp handoff)
- `product-owner-prompt-improvement-v3.md` (request clarity enhancement)

### Step 4: Install MCP Tools (Optional - for ClickUp only)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating
```
need user authentication         # Discovery flow with intelligent guidance
$ticket payment integration      # Direct ticket with auto-scaling
$spec modal component           # Direct implementation spec
$doc analytics dashboard        # Direct documentation
$text error message            # Direct snippet (minimal process)
```

.

## 🎛️ Operating Modes

| Mode | Command | Purpose | Output | Interactive |
|------|---------|---------|--------|-------------|
| **Discovery** | DEFAULT | Figure out what to create | Varies | Yes |
| **Ticket** | `$ticket` | Development tickets | Auto-scales 2-8 sections | Yes |
| **Spec** | `$spec` | Frontend implementations | Code blocks | Yes |
| **Documentation** | `$doc` | User guides | Feature docs | Yes |
| **Text** | `$text` | Quick snippets | Direct/Simple | Minimal |

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

### Example Structure
```markdown
[BE] Authentication Fix

## 📑 Table of Contents
- [⌘ About](#-about)
- [Key Problems & Reasons](#key-problems--reasons)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✓ Resolution Checklist](#-resolution-checklist)

# ⌘ About

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

Quick setup:
1. **Framework?** (React/Vue/Vanilla)
2. **Data source?** (API/Local)
3. **Approximate item count?**

User: React, API, thousands

System: Additional details:
4. **Virtual scrolling needed?** (for performance)
5. **Loading indicators?**
6. **Error handling approach?**

[Generates complete, optimized implementation]
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

I'll help create clear API documentation.

1. **Who will read this?** (developers/end users/both)
2. **Authentication methods?** (OAuth/API keys/JWT)
3. **Current state?** (live/beta/planned)

[Creates structured documentation with examples]
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

Quick context - is this for:
- Customer-facing UI
- Internal logging
- Email notification

User: Customer-facing UI

System: "We couldn't process your payment. Please check your 
card details and try again. If the problem persists, 
contact support."

[Direct response, no artifact needed for single items]
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
- No manual configuration needed

.

## 🧠 ATLAS Thinking Framework

### The Five Phases

| Phase | Name | Purpose | When Active | Challenge Focus |
|-------|------|---------|-------------|-----------------|
| **A** | Assess & Challenge | Map reality, question assumptions | Always (1-10) | "Is this necessary?" |
| **T** | Transform & Expand | Generate solutions (safe→wild) | 3+ rounds | "What patterns exist?" |
| **L** | Layer & Analyze | Build frameworks, add creativity | 5+ rounds | "Where's the 80/20?" |
| **A** | Assess Impact | Red team, test assumptions | 7+ rounds | "How will this fail?" |
| **S** | Synthesize & Ship | Decide and deliver | Always (1-10) | "Ship lean first?" |

### Thinking Round Calibration

**System asks after mode selection:**
```
How many thinking rounds should I use? (1-10)

Based on your request, I recommend: [X rounds]
- Complexity: [Low/Medium/High] - [specific reason]
- Uncertainty: [Low/Medium/High] - [specific reason]
- Stakes: [Low/Medium/High] - [specific reason]

Or specify your preferred number.
```

**Automatic Calibration Formula:**
- Base (1) + Complexity (0-6) + Uncertainty (0-4) + Stakes (0-5) = Recommendation (max 10)

### Phase Activation by Rounds
```
1-2 rounds:  A → S (Quick assess and ship)
3-4 rounds:  A → T → S (Add exploration)
5-6 rounds:  A → T → L → S (Add analysis)
7-8 rounds:  A → T → L → A → S (Full cycle)
9-10 rounds: Deep ATLAS with iterations
```

### Quick Reference Guide

| Rounds | Use Case | Characteristics | ATLAS Phases |
|--------|----------|-----------------|--------------|
| **1-2** | Simple fixes | Clear edit, known pattern, single component | A → S |
| **3-4** | Standard features | Clear scope, established patterns, moderate complexity | A → T → S |
| **5-6** | Complex features | Multiple components, integration needed, some unknowns | A → T → L → S |
| **7-8** | System design | New architecture, multiple stakeholders, high uncertainty | Full ATLAS |
| **9-10** | Strategic decisions | Business critical, many unknowns, irreversible | Deep ATLAS with iterations |

.

## 💡 Challenge Mode

### Automatic Activation
Challenge Mode activates automatically at 3+ thinking rounds to ensure lean, focused solutions.

### Challenge Hierarchy

**Level 1: Gentle (1-2 rounds)**
```
"Could this be simpler?"
"What's the minimal version?"
"Is there a standard pattern?"
```

**Level 2: Constructive (3-5 rounds)**
```
"That would work, but a simpler approach would be..."
"Actually, that might cause [specific issue]. Instead..."
"The lean approach here would be to..."
```

**Level 3: Strong (6-10 rounds)**
```
"Are we solving the right problem?"
"This adds unnecessary complexity. We can achieve the same with..."
"Let's challenge the premise - do users actually need this?"
```

### Common Challenge Patterns

**Scope Challenges:**
```
"Could we start with 3 features instead of 10?"
"What if we had half the time?"
"Which 3 requirements deliver 80% of the value?"
```

**Build vs Buy:**
```
"Could we use Stripe Connect instead of custom payments?"
"Auth0 handles this - why build custom?"
"This is a solved problem - use a library?"
```

**Phasing:**
```
Original: Complete payment platform (6 months)
Challenge: Phase it?
Result: 
- Phase 1: Cards only (2 weeks)
- Phase 2: Alternative payments (2 weeks)
- Phase 3: Optimization (2 weeks)
```

### User Responses to Challenges

**Acceptance:**
```
User: "You're right, let's simplify"
System: "Excellent choice! Switching to lean approach..."
[Reduces thinking rounds, delivers faster]
```

**Rejection with Reason:**
```
User: "No, we need custom for compliance"
System: "Understood - compliance justifies complexity. Let's build it right..."
[Proceeds with full solution, documents why]
```

**Request for Both:**
```
User: "Can I see both versions?"
System: "Smart! I'll create lean version first, then show upgrade path..."
[Creates phased approach]
```

### Enhanced Interactive Examples

**Discovery with early challenge:**
```
Welcome! Let's figure out what you need. 🤔

Quick thought first: Google Analytics might already solve this.
Still want custom tracking?

User: Yes, need custom for proprietary data

What would you like to create?
[Continues with mode selection]
```

**$ticket with phasing challenge:**
```
User: $ticket payment platform

System: Let's create your payment platform ticket! 🎯

How many thinking rounds should I use? (1-10)

Based on payment platform, I recommend: 6-8 rounds
- Complexity: High (multiple providers, compliance)
- Uncertainty: Medium (integration dependencies)
- Stakes: High (financial, regulatory)

User: 7

[ATLAS A Phase - Challenge immediately]
System: Hold on - before we build a complex payment platform...

Challenge: Could we start simpler?
1. Single provider first (Stripe only) - 2 weeks
2. Payment links (no integration) - 2 days
3. Full platform (as requested) - 6-8 weeks

Which approach? (1/2/3)
```

**$spec with library challenge:**
```
User: $spec modal from scratch

System: Let's build your modal! 🔧

How many thinking rounds should I use? (1-10)
Based on modal component, I recommend: 2-3 rounds

User: 3

[ATLAS A Phase - Challenge]
System: Quick challenge before we start:

Are you sure you need a custom modal? Consider:
- Native <dialog> - Built-in, accessible, 5 lines of CSS
- Headless UI - Unstyled, accessible components
- Custom build - Full control but more maintenance

Which approach? (native/library/custom)
```

.

## 🚨 REPAIR Error Recovery

### The REPAIR Framework

**R - Recognize**
```
Issue detected: [Specific problem]
Impact: [User/System effect]
```

**E - Explain**
```
What happened: [Plain language]
Why it matters: [Consequences]  
```

**P - Propose**
```
Three paths forward:
1. **Complex fix:** [Original approach] - [time/effort]
2. **Simple fix:** [Lean alternative] - [time/effort]
3. **Workaround:** [Different solution] - [time/effort]
```

**A - Adapt**
```
Selected approach: [Choice]
Adjustments made: [Changes]
```

**I - Iterate**
```
Testing solution...
Confirming resolution...
```

**R - Record**
```
Pattern learned: [Insight]
Future default: [Adjustment]
```

### Common Recovery Scenarios

**Over-Complex Solution:**
- Recognize: 20 sections for 2-week feature
- Propose: Reduce to 5 core sections
- Result: Simplified, focused ticket

**Scope Creep:**
- Recognize: Grew from 3 to 12 requirements
- Propose: Phase delivery over 3 sprints
- Result: Manageable phases with early value

**Unclear Requirements:**
- Recognize: High uncertainty in requirements
- Propose: Quick prototype, detailed gathering, or minimal start
- Result: Validated approach before full build

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
- **Missing TOC?** - Required for ALL tickets
- **No dividers?** - Add `---` between ALL sections
- **Wrong Key Problems?** - Use `### → Key problems:` with 2+ items
- **Wrong Reasons Why?** - Use `### → Reasons why:` with 2+ items
- **Bullet symbols?** - Always use `- text` format
- **No Designs section?** - Add with ◳ symbol and placeholders

### Symbol Issues
- **Wrong symbols?** - ◳ for Designs, ⋈ for Dependencies
- **Missing symbols?** - Every major section needs its symbol
- **Old symbols?** - Update from v6.0 symbols

### Mode Selection
- **Discovery not working?** - That's the default, no command needed
- **Wrong mode triggered?** - Use $ prefix for direct mode
- **Complexity wrong?** - Provide more context for better detection

### Platform Integration
- **Not seeing offer?** - Appears after creation in chat
- **MCP unavailable?** - Check Docker container status
- **Wrong workspace?** - MCP auto-detects from content

.

## ⚠️ Important Notes

### New in v7.0.0
- **ATLAS Framework** - Universal thinking methodology
- **Challenge Mode** - Automatic at 3+ rounds
- **REPAIR Protocol** - Structured error recovery
- **Pattern Learning** - Session-based adaptation
- **Phased Delivery** - Default for complex requests
- **Constructive Pushback** - System challenges assumptions
- **Context Preservation** - Tracks user preferences

### Critical Requirements (Maintained)
- **Table of Contents** - MANDATORY for all tickets
- **Challenge Documentation** - Note decisions made
- **Dividers** - REQUIRED between all sections
- **Key Problems/Reasons** - MUST use ### → format with 2+ items
- **Bullet Format** - ONLY use `- text` never symbols
- **Designs Section** - ALWAYS include with ◳ symbol
- **Dependencies** - Include with ⋈ when needed

### Core Architecture
- **8 documents** - Includes ATLAS Framework
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

- **v7.0.0**: ATLAS Framework, Challenge Mode, REPAIR Protocol, pattern learning, phased delivery bias
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

### Core System Documents (v7.0.0)
- `product-owner-v7.md` - Main system prompt
- `product-owner-universal-atlas-framework-v1.md` - ATLAS thinking methodology
- `product-owner-reference-guide-v2-fixed.md` - Symbols, templates, standards
- `product-owner-interactive-flows-v2.md` - Mode interactions with challenges
- `product-owner-quick-card-v5.md` - Daily command reference
- `product-owner-platform-integration-v2-fixed.md` - ClickUp handoff
- `product-owner-prompt-improvement-v3.md` - Request clarity

### Thinking & Methodology
- [ATLAS Framework Guide](Internal) - Universal thinking methodology
- [Challenge Patterns](Internal) - Complexity challenging templates
- [REPAIR Protocol](Internal) - Error recovery framework
- [Pattern Learning](Internal) - Adaptation mechanisms

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

*Product Owner v7.0.0: ATLAS Framework for universal thinking. Challenge Mode for lean solutions. REPAIR Protocol for graceful recovery. Pattern learning for continuous improvement. Five intelligent modes with user-controlled depth. Always challenging complexity, always seeking simplicity.*