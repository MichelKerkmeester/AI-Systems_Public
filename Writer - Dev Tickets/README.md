# Dev Ticket Writer - User Guide v3.4.0

A comprehensive system that transforms development requests into clear, actionable tickets with developer-first clarity. Features scope prefixes, rich descriptions, technical details, automatic label mapping, and 5 operating modes including educational Interactive mode.

## 🆕 What's New in v3.4.0

- **Scope Prefixes**: Every ticket now starts with [BE], [FE], [Mobile], [FS], [DevOps], or [QA] for immediate clarity
- **Rich Descriptions**: 1-2 comprehensive paragraphs with bullet points explaining context and impact
- **Technical Details Section**: Dedicated section for components, APIs, and architecture details
- **Automatic Label Mapping**: Smart detection assigns relevant labels based on content
- **H1 Titles**: Main ticket titles now use # for better prominence
- **No Percentages**: All metrics use descriptive language instead of specific percentages

## Overview

The Dev Ticket Writer helps teams create professional development tickets that are "clear at first glance" for developers while teaching product thinking principles. By focusing on WHAT needs to be done and WHY it matters (not HOW to implement), it bridges the communication gap between product and development.

## ✨ Key Features

- **Developer-First Clarity**: Scope prefixes, rich descriptions, and technical details
- **5 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $epic
- **Enhanced Symbol System**: Professional symbols (❖, ◇, **◊**, →, ✓, ⊗) for visual hierarchy
- **Prompt Improvement**: Clarifies vague requests without adding assumptions
- **Educational Focus**: Interactive mode teaches product management through practice
- **Resolution Checklists**: Required actionable steps scaled by complexity
- **Figma Integration**: Optional design extraction for UI features
- **2-Minute Rule**: All tickets readable in under 2 minutes
- **Artifact Delivery**: Every ticket in reusable markdown artifacts
- **Smart Detection**: Automatic scope identification and label assignment

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v3.3"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v3.3.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Quick Reference Card - v1.2.0.md` (Daily companion with scope prefixes)
- `Ticket - Templates & Standards - v1.2.0.md` (Updated templates with descriptions)
- `Ticket - Examples Library - v1.2.0.md` (Examples with developer clarity)
- `Ticket - Interactive Mode - v1.3.0.md` (Conversational spec)
- `Ticket - Prompt Improvement - v1.0.0.md` (Request clarification)

### Step 4: Start Creating Tickets
Simply describe what you need:
```
fix login bug
need user profiles  
$s dashboard feature
add API endpoint
```

## 🎯 Scope Prefixes (NEW)

Every ticket title includes a scope prefix for immediate clarity:

| Prefix | Use For | Example |
|--------|---------|---------|
| **[BE]** | Backend features | `# ❖ [BE] User Authentication` |
| **[FE]** | Frontend features | `# ❖ [FE] Dashboard Redesign` |
| **[Mobile]** | Mobile app features | `# ❖ [Mobile] Push Notifications` |
| **[FS]** | Full stack features | `# ❖ [FS] Real-time Chat` |
| **[DevOps]** | Infrastructure | `# ❖ [DevOps] CI/CD Pipeline` |
| **[QA]** | Testing features | `# ❖ [QA] Test Automation` |

## 📝 Rich Descriptions (NEW)

Every ticket now includes 1-2 comprehensive paragraphs after the title:

**First paragraph** covers:
- Current situation and problems
- User pain points with bullet points
- Business impact
- Why this matters now

**Second paragraph** covers:
- Proposed solution approach
- Expected benefits
- Technical considerations
- Success indicators

Example:
```markdown
# ❖ [FE] Advanced Search Filters

Our search functionality is failing users, with the majority abandoning searches before finding what they need. Current issues include:

• **No filtering options** - Users scroll through hundreds of irrelevant results
• **Poor relevance** - Basic keyword matching returns unrelated items
• **Mobile frustration** - Search is nearly unusable on small screens

By implementing comprehensive filtering capabilities, we'll dramatically improve product discovery. The solution includes category filters, price ranges, availability toggles, and smart sorting that updates results in real-time, helping users find exactly what they need without frustration.
```

## 🎛️ Operating Modes

| Mode | Command | When to Use | Resolution Checklist | MCP Usage |
|------|---------|-------------|---------------------|-----------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Adaptive | Cascade (3-5 thoughts) |
| **Quick** | `$q` | Simple features (explicit request) | 3-5 items | Sequential (1-2 thoughts) |
| **Standard** | `$s` | Full features (explicit request) | 8-15 items | Sequential (2-3 thoughts) |
| **Complex** | `$c` | Multi-phase implementations | 15-30 items | Cascade (3-5 thoughts) |
| **Epic** | `$e` | Major initiatives | 10-20 items | Cascade (5+ thoughts) |

**Note:** Interactive mode is the default unless explicitly specified otherwise.

## 🏷️ Automatic Label Mapping (NEW)

The system automatically assigns labels based on detected content:

| Detected Content | Auto-Applied Labels |
|-----------------|-------------------|
| Backend code | `Backend-System`, `API` |
| Frontend UI | `[App]-App`, `UI` |
| Mobile features | `Mobile-App` |
| Authentication | `Authentication`, `Security` |
| Database work | `Database`, `Backend-System` |
| Bug fixes | `bug`, `defect` |
| New features | `feature`, `enhancement` |
| Performance | `performance`, `optimization` |

## 📝 How Prompt Improvement Works

The system invisibly enhances vague requests before processing:

### What Gets Enhanced
```
"fix auth" → "create bug fix ticket for authentication"
"DB slow" → "create performance ticket for database"
"need API docs" → "create feature ticket for application programming interface documentation"
```

### Common Developer Abbreviations
- **Technical**: API, DB, UI, UX, FE, BE, auth, config, env, repo
- **Process**: QA, CI/CD, MVP, POC, PR
- **Performance**: perf, opt, mem
- **Security**: sec, vuln, 2FA

### What DOESN'T Change
- Implementation details (never added)
- Priority or complexity (never assumed)
- Mode commands ($q, $s, etc.)
- Already clear requests
- The need for Interactive mode questions

## 🏗️ Core Components

### WHAT/WHY Philosophy
- **WHAT**: Clear description of the feature/fix needed
- **WHY**: User value and business outcomes
- **NOT HOW**: Leave implementation to developers

### Enhanced Symbol System (Required)
- **❖** - Titles and major features (with H1)
- **◇** - Requirements and main sections
- **◊** - Sub-headings within sections
- **→** - Designs & References
- **✓** - Success criteria AND Resolution Checklist
- **⊗** - Dependencies
- **—** - Sub-categories under **◊** sub-headings

### Complete Ticket Structure
1. Title with `# ❖ [SCOPE]` format
2. Rich 1-2 paragraph description
3. User Value statement
4. Business Goal (measurable, no percentages)
5. Requirements (outcome-focused)
   - Use **◊** for complex sections
   - Use — for sub-categories
6. Technical Details section (NEW)
7. Success Criteria (checkboxes)
8. Resolution Checklist (REQUIRED)
9. Dependencies (if any)
10. Labels (auto-generated)

## 🔧 Technical Details Section (NEW)

Every ticket includes technical specifics for developers:

```markdown
## ◇ Technical Details

**◊** Architecture
- **Component:** Backend-System (Go)
- **API:** POST /users/auth
- **Database:** PostgreSQL

**◊** Integration
- **External Services:** Email service
- **Authentication:** JWT tokens
- **Security:** Rate limiting required
```

## 📊 Interactive Mode Example

```
User: need login
System: [Invisibly enhances to "create feature ticket for login"]
System: [Detects authentication = backend feature]

System: Great! Let's create a clear ticket together. I'll help you think through the key aspects:

1. What specific problem does login solve for your users?
2. What type of login do you need (email/password, social, both)?
3. How will we measure if this feature is successful?

User: Users can't save preferences. Email/password. High registration rate.

System: Perfect! Do you have any Figma designs for the login flow?

[Creates complete ticket with [BE] prefix, rich description, technical details, and labels]
```

## 🤖 Educational Focus

Interactive mode teaches product thinking by:
- Asking strategic questions about user value
- Focusing on business outcomes (without percentages)
- Showing quality metrics and scores
- Providing learning points
- Building skills through practice
- Demonstrating proper ticket structure

## 📈 Quality Assurance

### 2-Minute Readability
All tickets must be scannable and understood in under 2 minutes. Enhanced by:
- Clear scope prefixes for instant understanding
- Rich descriptions that tell the complete story
- Technical details in dedicated section
- Visual hierarchy with symbols
- Structured requirements

### Resolution Checklist Scaling
- **Quick**: 3-5 simple tasks
- **Standard**: 8-15 tasks in categories
- **Complex**: 15-30 phase-based tasks
- **Epic**: 10-20 coordination tasks

### Success Metrics (No Percentages)
- Vast majority of users complete ticket creation
- Nearly all tickets meet quality standards
- Brief average conversation time
- All maintain readability standards
- Clear improvement in developer understanding

## 🔧 MCP Tools Integration

The system intelligently selects thinking tools based on complexity:

### Sequential Thinking MCP
- Simple requests and clear requirements
- Quick ($q) and Standard ($s) modes
- 1-3 thoughts for analysis

### Cascade Thinking MCP
- Interactive mode (always)
- Complex ($c) and Epic ($e) modes
- Unclear requirements needing exploration
- 3-5+ thoughts with branching

### Figma MCP (Optional)
- UI feature tickets
- Design extraction and understanding
- Never required, always beneficial

## 📚 Example with Complete Structure

### Complex Feature Request
**Input:** "update search filters"
**Result:** 
```markdown
# ❖ [FE] Advanced Search Filters

Our users struggle to find products efficiently, leading to high abandonment rates and lost revenue. Key problems include:

• **Information overload** - Hundreds of unfiltered results
• **No refinement options** - Users can't narrow searches
• **Poor mobile experience** - Filters don't work on small screens

This implementation provides comprehensive filtering with real-time updates, helping users find exactly what they need through category selection, price ranges, and smart sorting.

**User Value:** Find products quickly with powerful filters

**Business Goal:** Dramatically reduce search abandonment

---

## ◇ Requirements

**◊** Filter Panel
— UI Components
• Category dropdown with multi-select
• Date range picker
• Price slider
— Behavior
• Instant results update
• Clear all option
• Session persistence

---

## ◇ Technical Details

**◊** Frontend Architecture
- **Framework:** Angular
- **State:** NgRx for filter state
- **API:** GET /api/search
- **Performance:** Debounced updates

---

## Labels
`[App]-App`, `UI`, `Search`, `feature`
```

## ⚠️ Important Notes

- **Scope prefixes required** - Every title needs [BE], [FE], etc.
- **Rich descriptions mandatory** - 1-2 paragraphs with context
- **Technical Details required** - Developers need specifics
- **No percentages** - Use descriptive language instead
- **Labels auto-generated** - Based on content detection
- **Interactive is default** - Unless mode explicitly specified
- **Never provides implementation** - Only creates tickets
- **Always uses artifacts** - Every ticket in markdown

## 📦 Version History

- **v3.3.0**: Developer-first clarity with scope prefixes, rich descriptions, technical details, labels
- **v3.2.0**: Added **◊** sub-heading pattern and structured em dash usage
- **v3.1.0**: Added prompt improvement layer and developer abbreviations
- **v3.0.0**: Introduced mandatory Resolution Checklists
- **v2.0.0**: Interactive mode as default, enhanced educational focus
- **v1.0.0**: Initial WHAT/WHY philosophy implementation

## 🎯 Key Principles

1. **Developer clarity first** through scope prefixes and technical details
2. **Rich context** via comprehensive descriptions
3. **Democratize product thinking** through guided creation
4. **Focus on user value** not technical implementation
5. **Teach through practice** with Interactive mode
6. **Maintain 2-minute readability** for all tickets
7. **Scale complexity appropriately** with different modes

## 🆘 Troubleshooting

### Developer Clarity Issues
- **Missing scope prefix**: Required in every title
- **Short description**: Need 1-2 full paragraphs
- **No technical details**: Add dedicated section
- **Missing labels**: Should auto-generate

### Symbol Usage Issues
- **Wrong title format**: Use `# ❖ [SCOPE]`
- **Missing ◊**: Required for complex requirements
- **Wrong em dash**: Only use — under **◊** sub-headings
- **Hierarchy confusion**: Follow ◇ → **◊** → — → • pattern

### Content Issues
- **Using percentages**: Replace with descriptive terms
- **Implementation details**: Remove HOW, keep WHAT/WHY
- **Missing symbols**: Required in all sections
- **No Resolution Checklist**: Required for every ticket

### Interactive Mode
- **Too many questions**: System limits to 3-4 maximum
- **Not getting guidance**: Ensure no mode specified
- **Figma not connecting**: It's optional, continue without

## 📚 Additional Resources

- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [Figma for Developers](https://help.figma.com/hc/en-us/articles/360040028273)

---

*Transform vague requests into crystal-clear tickets that developers understand at first glance. Teach product thinking through practice. Focus on WHAT and WHY, never HOW. Make every ticket immediately actionable with scope, context, and technical clarity.*
