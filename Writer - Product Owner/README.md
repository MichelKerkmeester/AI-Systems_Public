# Product Owner System - User Guide v8.1.0

The Product Owner system transforms requests into professional development tickets, implementation specs, documentation, text snippets, and beautifully formatted documents through intelligent interactive guidance with built-in complexity challenging. By focusing on WHAT needs doing and WHY it matters (not HOW to implement), it creates lean, actionable artifacts that bridge the communication gap between product and development teams.

## 📋 Table of Contents

- [🆕 What's New in v8.1.0](#-whats-new-in-v810)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
- [🎯 Automatic Complexity Detection](#-automatic-complexity-detection)
- [📄 Document Beautifier](#-document-beautifier-beautify)
- [💻 Implementation Specs](#-implementation-specs-spec)
- [📚 Documentation](#-documentation-doc)
- [✍️ Text Snippets](#️-text-snippets-text)
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

## 🆕 What's New in v8.1.0

### Streamlined Architecture
**Removed Prompt Improvement Module:**
- Simplified system architecture by removing the prompt improvement layer
- Direct mode detection without request enhancement preprocessing
- Reduced document count from 7 to 6 essential files
- Faster processing with cleaner request analysis
- Focus on core functionality without intermediary transformations

### Maintained from v8.0.0

**Document Beautifier Mode:**
- Transform unstructured text into clean, scannable documents
- Extreme simplification bias (challenges at 2+ rounds vs 3+ for other modes)
- Two content modes: **Strict** (preserve only) vs **Enhanced** (add clarifications)
- Three format levels: **Minimal** → **Standard** → **Deep** (always starts minimal)
- FORM scoring: Flow (20%), Organization (30%), Readability (35%), Metadata (15%)
- Structure frameworks: SCAN (70%), HIERARCHY (20%), PREP (10%)
- Content integrity reports for every beautified document

**ATLAS Thinking Framework:**
- Universal thinking methodology with 5-phase structured approach
- Adaptive depth calibration (1-10 rounds, 1-5 for beautify)
- User-controlled thinking for optimal output quality
- Different phases activate based on complexity

**Challenge Mode:**
- Automatic activation at 3+ thinking rounds (2+ for beautify)
- Constructive pushback against unnecessary complexity
- Three intensity levels based on thinking depth
- Always proposes simpler, leaner alternatives

**REPAIR Error Recovery:**
- Structured recovery protocol for handling errors
- Multiple solution paths offered
- Pattern learning from errors
- Graceful degradation maintaining functionality

.

## ✨ Key Features

- **📄 NEW Beautify Mode**: Document formatting with extreme simplification bias
- **🧠 ATLAS Framework**: 5-phase universal thinking methodology with adaptive depth
- **💡 Challenge Mode**: Active complexity challenging with lean alternatives
- **🎯 Smart Complexity**: Automatic detection and scaling
- **📄 Pattern Learning**: Adapts to user preferences and successful patterns
- **🚨 REPAIR Protocol**: Structured error recovery with learning
- **📊 Thinking Calibration**: Formula-based recommendations (1-10 rounds)
- **🎛️ 6 Intelligent Modes**: Discovery, $ticket, $spec, $doc, $text, $beautify
- **🔗 Platform Ready**: Direct ClickUp integration after creation
- **📝 Professional Symbols**: ⌘, ◇, ◊, ◳, →, ✦, ✓, ⋈, ∅, ⌆
- **📋 Strict Formatting**: TOC, dividers, proper Key Problems/Reasons format
- **⚡ Phased Delivery**: Automatic breakdown of large initiatives
- **🎪 Session Context**: Tracks preferences and adapts behavior

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Product Owner v8.1.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Product Owner - v8.1.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these **6 essential documents** to your project's knowledge base:
- `Product Owner - ATLAS Thinking Framework.md` (ATLAS thinking methodology)
- `Product Owner - Reference Guide.md` (symbols, templates, standards, beautify templates)
- `Product Owner - Interactive Mode.md` (all mode interactions with Challenge Mode)
- `Product Owner - Quick Card.md` (daily command reference)
- `Product Owner - Platform Integration.md` (ClickUp handoff)

### Step 4: Install MCP Tools (Optional - for ClickUp only)
See [MCP Installation](#-installing-mcp-tools) section below

### Step 5: Start Creating
```
need user authentication         # Discovery flow with intelligent guidance
$ticket payment integration      # Direct ticket with auto-scaling
$spec modal component           # Direct implementation spec
$doc analytics dashboard        # Direct documentation
$text error message            # Direct snippet (always artifact)
$beautify meeting notes        # Format document (NEW!)
```

.

## 🎛️ Operating Modes

| Mode | Command | Purpose | Output | Interactive | Challenge |
|------|---------|---------|--------|-------------|-----------|
| **Discovery** | DEFAULT | Figure out what to create | Varies | Yes | 3+ rounds |
| **Ticket** | `$ticket` | Development tickets | Auto-scales 2-8 sections | Yes | 3+ rounds |
| **Spec** | `$spec` | Frontend implementations | Code blocks | Yes | 3+ rounds |
| **Documentation** | `$doc` | User guides | Feature docs | Yes | 3+ rounds |
| **Text** | `$text` | Quick snippets | Artifact always | Minimal | Rarely |
| **Beautify** | `$beautify` | Format documents | Clean structure | Yes | **2+ rounds** |

### Discovery Flow (Default)
When no mode is specified, the system helps determine what to create:

```
Welcome! Let's figure out what you need. 🤔

What would you like to create?
1. Development ticket - Feature or bug for developers
2. Implementation spec - Frontend code/styling solution
3. Product documentation - User guide or feature docs
4. Text snippet - Quick description or copy
5. Document formatting - Clean up and organize existing text

Which best fits? (1-5)
```

### Direct Mode Activation
Use $ prefix to skip discovery:
- `$ticket` → Straight to ticket questions
- `$spec` → Straight to implementation questions
- `$doc` → Straight to documentation questions
- `$text` → Minimal questions for quick content
- `$beautify` → Straight to formatting options

.

## 🎯 Automatic Complexity Detection

### For $ticket Mode

The system intelligently detects complexity based on your responses:

| Indicators | Complexity | Sections | Resolution Items |
|------------|------------|----------|------------------|
| Bug fix, update | **Simple** | 2-3 | 4-6 |
| Feature, dashboard | **Standard** | 4-5 | 8-12 |
| Platform, architecture | **Complex** | 6-8 with phases | 12-20 |

### For $beautify Mode

Document complexity based on length and structure:

| Word Count | Format Level | Elements | Challenge |
|------------|--------------|----------|-----------|
| <500 | **Minimal** | Headers only, no TOC | Never |
| 500-2000 | **Standard** | Headers + TOC + sections | If complex |
| >2000 | **Deep** | Full restructure | Always |

### Mandatory Formatting (ALL Tickets)

Every ticket MUST include:
- **Table of Contents** - Sections only (no subsections)
- **Dividers** - Between ALL sections (---)
- **Key Problems** - `### → Key problems:` with 2+ items, NOT in TOC
- **Reasons Why** - `### → Reasons why:` with 2+ items, NOT in TOC
- **QA Warning** - Above Resolution Checklist
- **Designs & References** - Section with ◳ symbol (placeholders if no links)
- **Dependencies** - Section with ⋈ symbol when applicable


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
- **◇** - Feature sections
- **◊** - Sub-headings (bold)
- **→** - References
- **⌆** - Additional resources

.

## ✍️ Text Snippets ($text)

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

System: Let's write your error message! ✍️

How many thinking rounds should I use? (1-2 typical for snippets)

User: 1

Quick context - is this for:
- Customer-facing UI
- Internal logging

User: Customer-facing UI

[Creates artifact with error message]
```

.

## 📄 Document Beautifier ($beautify)

### Transform Unstructured Text

The beautify mode transforms messy, unformatted text into clean, professional documents with extreme simplification bias.

### Interactive Flow
```
User: $beautify [pastes unformatted text]

System: Let's transform your document for clarity! 📄

How many thinking rounds should I use? (1-5)
Based on your document, I recommend: 2 rounds

User: 2

[CHALLENGE ACTIVATES at 2+ rounds for beautify]
System: I could achieve excellent results with just 1 round using minimal formatting.

Would you like:
1. Lean approach (1 round, minimal) - recommended
2. Full analysis (2 rounds) as requested

User: 1

System: What format level would work best?

1. **Minimal** - Just headers and emphasis (usually perfect!)
   • 3-5 main headers
   • Bold for 3 key points
   • No TOC needed

2. **Standard** - Headers + TOC + sections
   • Full section structure
   • Table of contents

3. **Deep** - Complete restructuring
   • Reorganize all content
   • Multiple hierarchy levels

Which suits your needs? [I recommend Minimal]

User: 1

System: How should I handle your content?

1️⃣ **Strict Mode** - Preserve Only (Recommended)
   • Zero content additions
   • Maintains your authentic voice

2️⃣ **Enhanced Mode** - Improve & Clarify
   • Add helpful transitions [AI-ADDED]
   • Expand acronyms [AI-ADDED]

Which would you prefer? (1 or 2) [Default: 1]
```

### Structure Frameworks

**SCAN Framework (70% of documents):**
- **S**ummary - Top-level overview (10%)
- **C**ore Content - Main body (70%)
- **A**dditional Details - Supporting info (15%)
- **N**avigation/Next Steps - Actions (5%)

**HIERARCHY Framework (20% of documents):**
- Nested structure with maximum 2 levels
- Challenged first - "Could flatter structure be clearer?"

**PREP Framework (10% of documents):**
- **P**urpose/Problem
- **R**esearch/Results
- **E**vidence/Examples
- **P**lan/Proposal

### Content Integrity Report

Every beautified document includes:
```markdown
## 📊 Content Integrity Report
✅ Mode: STRICT (preserved exactly)
✅ Format: Minimal (headers only)
✅ Changes: 3 headers added
✅ FORM Score: 75/100
✅ Alternative: None needed - minimal is optimal
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

### Beautify Mode Platform Offer
```markdown
📦 **Save your formatted document?**

1. **ClickUp** - As document/wiki page
2. **Skip** - Keep as artifact only

[Pattern: You typically skip platform for formatted docs]
```

### Smart Handoff
- System creates content with proper structure
- User chooses platform
- MCP handles workspace creation
- All formatting preserved
- Pattern learning tracks preferences by mode

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
# Beautify mode capped at 5 rounds
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
- **Most modes:** Activates at 3+ thinking rounds
- **Beautify mode:** Activates at 2+ thinking rounds (lower threshold)

### Challenge Hierarchy

**Level 1: Gentle (1-2 rounds)**
```
"Could this be simpler?"
"What's the minimal version?"
"Would minimal formatting be cleaner?" (beautify)
```

**Level 2: Constructive (3-5 rounds)**
```
"That would work, but a simpler approach would be..."
"The lean approach here would be to..."
"Strict mode preserves your voice better?" (beautify)
```

**Level 3: Strong (6-10 rounds)**
```
"Are we solving the right problem?"
"This adds unnecessary complexity. We can achieve the same with..."
"Are we over-formatting?" (beautify)
```

### Beautify-Specific Challenges

**Format Level:**
- "Minimal format often sufficient - try it?"
- "Could we use fewer hierarchy levels?"

**Content Mode:**
- "Strict preserves your voice - better?"
- "These additions may help but change your tone"

**Structure:**
- "Would flatter structure be clearer?"
- "Could we consolidate to 3-4 sections?"

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

**Over-Formatted Document (Beautify):**
- Recognize: Excessive formatting (5+ heading levels)
- Explain: Formatting overwhelming content
- Propose: Strip to essential headers only
- Result: Clean, minimal structure

**Scope Creep:**
- Recognize: Requirements expanded during creation
- Propose: Phase delivery
- Result: Manageable sprints

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

### Beautify Mode Issues
- **Over-formatting?** - Default to minimal, challenge at 2+ rounds
- **Wrong content mode?** - Strict preserves voice, Enhanced changes it
- **Too many sections?** - SCAN framework works for 70% of docs
- **No FORM score?** - Included in every content integrity report

### Challenge Mode Issues
- **Too aggressive?** - Specify lower thinking rounds
- **Not challenging?** - Check if threshold met (3+ rounds, 2+ for beautify)
- **Wrong alternatives?** - Provide more context

### ATLAS Framework
- **Phase confusion?** - Check thinking round mapping
- **Skipped phases?** - Normal for low-round requests
- **Too much thinking?** - Reduce rounds (beautify capped at 5)

### Pattern Learning
- **Not adapting?** - Patterns establish after 3 similar requests
- **Wrong defaults?** - Will adjust after 2 overrides
- **Different by mode?** - System tracks patterns per mode

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
- **Different for beautify?** - Offers document/wiki page option
- **Pattern not tracking?** - Choices recorded after 3 similar

.

## ⚠️ Important Notes

### New in v8.1.0
- **Streamlined Architecture** - Removed prompt improvement module for cleaner processing
- **Direct Mode Detection** - No preprocessing layer, faster response
- **Reduced Complexity** - 6 essential documents instead of 7
- **Maintained Core Features** - All v8.0.0 functionality preserved

### Critical Requirements (Maintained)
- **Table of Contents** - MANDATORY for all tickets (sections only)
- **Key Problems/Reasons** - NOT in TOC, ### → format, 2+ items
- **QA Warning** - Above Resolution Checklist
- **Dividers** - Between ALL sections
- **Bullet Format** - ONLY use `- text` never symbols
- **Designs Section** - ALWAYS include with ◳ symbol
- **Dependencies** - Include with ⋈ when needed

### Core Architecture
- **6 essential documents** - Streamlined documentation set
- **Native thinking** - User-controlled rounds (1-10, 1-5 for beautify)
- **6 operating modes** - All interactive including beautify
- **Strict standards** - Consistent formatting
- **Challenge integration** - Earlier for beautify (2+ rounds)

### Key Principles
- **Challenge complexity** - Even earlier for beautify mode
- **Preserve voice** - Strict mode default (90% usage)
- **Start minimal** - Add only if proven necessary
- **Learn continuously** - Mode-specific patterns
- **FORM optimize** - Balance all readability factors
- **Pattern recognition** - Different preferences by mode

.

## 📦 Version History

- **v8.1.0**: Removed prompt improvement module, streamlined to 6 documents, direct mode detection
- **v8.0.0**: Beautify mode added with extreme simplification bias, 2+ round challenges, Strict/Enhanced modes, FORM scoring
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
- `Writer - Product Owner.md` - Main system prompt (v8.1.0)
- `Product Owner - ATLAS Thinking Framework.md` - Universal thinking methodology
- `Product Owner - Reference Guide.md` - Symbols, templates, standards, beautify templates
- `Product Owner - Interactive Mode.md` - Mode interactions with challenges
- `Product Owner - Quick Card.md` - Daily command reference
- `Product Owner - Platform Integration.md` - ClickUp handoff

### Beautify Mode Resources
- [Beautify Templates](Product Owner - Reference Guide.md#beautify-templates) - All format templates
- [FORM Scoring](Product Owner - Reference Guide.md#form-scoring) - Readability metrics
- [Structure Frameworks](Product Owner - Reference Guide.md#structure-frameworks) - SCAN, HIERARCHY, PREP
- [Content Modes](Product Owner - Reference Guide.md#content-modes) - Strict vs Enhanced

### Thinking & Methodology
- [ATLAS Framework Guide](Product Owner - ATLAS Thinking Framework.md) - Universal thinking methodology
- [Challenge Patterns](Product Owner - Interactive Mode.md#challenge-mode) - Complexity challenging templates
- [REPAIR Protocol](Product Owner - ATLAS Thinking Framework.md#repair-protocol) - Error recovery framework
- [Pattern Learning](Product Owner - Interactive Mode.md#pattern-learning) - Adaptation mechanisms

### Product Management
- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Lean Product Development](https://www.agilealliance.org/agile101/subway-map-to-agile-practices/)
- [Document Design Principles](https://www.nngroup.com/articles/how-users-read-on-the-web/)

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

*Product Owner v8.1.0: Streamlined architecture without prompt improvement layer. Beautify mode for document transformation. Extreme simplification bias with 2+ round challenges. Strict mode preserves voice. FORM scoring ensures readability. Six intelligent modes with user-controlled depth. Always challenging complexity, always seeking simplicity.*