# Dev Ticket Writer - User Guide v3.4.0

A comprehensive system that transforms development requests into clear, actionable tickets with developer-first clarity. Features scope prefixes, structured problem/solution descriptions, technical implementation specs, automatic label mapping, and 6 operating modes including educational Interactive mode.

## 🆕 What's New in v3.4.0

- **Structured Descriptions**: New format with ⚠︎ Key problems/changes and ⁉ Reasons why sections
- **Spec Mode ($spec)**: Create technical implementation specifications with code examples
- **Implementation Spec References**: Link HOW-to guides within standard tickets
- **Concise Problem Lists**: Bullet points replace long paragraphs for better scanning
- **New Icons**: ⚠︎ and ⁉ for visual hierarchy in descriptions
- **No More Technical Details Section**: Replaced by optional spec references

## Overview

The Dev Ticket Writer helps teams create professional development tickets that are "clear at first glance" for developers while teaching product thinking principles. By focusing on WHAT needs to be done and WHY it matters (not HOW to implement), it bridges the communication gap between product and development. When implementation details are needed, the new Spec mode provides technical specifications with code examples.

## ✨ Key Features

- **Developer-First Clarity**: Scope prefixes, structured descriptions, and optional spec links
- **6 Specialized Modes**: $interactive (default), $quick, $standard, $complex, $epic, $spec (NEW)
- **Enhanced Symbol System**: Professional symbols (❖, ◇, **◊**, →, ✓, ⊗, ⚠︎, ⁉) for visual hierarchy
- **Prompt Improvement**: Clarifies vague requests without adding assumptions
- **Educational Focus**: Interactive mode teaches product management through practice
- **Resolution Checklists**: Required actionable steps scaled by complexity
- **Implementation Specs**: Technical HOW-to guides with code examples (NEW)
- **Figma Integration**: Optional design extraction for UI features
- **2-Minute Rule**: All tickets readable in under 2 minutes
- **Artifact Delivery**: Every ticket in reusable markdown artifacts
- **Smart Detection**: Automatic scope identification and label assignment

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v3.4"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Dev Tickets - v3.4.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Ticket - Quick Reference Card - v1.3.0.md` (Daily companion with spec mode)
- `Ticket - Templates & Standards - v1.3.0.md` (Updated templates with new format)
- `Ticket - Examples Library - v1.3.0.md` (Examples with structured descriptions)
- `Ticket - Interactive Mode - v1.3.0.md` (Conversational spec with spec detection)
- `Ticket - Prompt Improvement - v1.0.0.md` (Request clarification)

### Step 4: Start Creating Tickets
Simply describe what you need:
```
fix login bug
need user profiles  
$s dashboard feature
add API endpoint
$spec hide scrollbar CSS
```

## 🎯 Scope Prefixes

Every ticket title includes a scope prefix for immediate clarity:

| Prefix | Use For | Example |
|--------|---------|---------|
| **[BE]** | Backend features | `# ❖ [BE] User Authentication` |
| **[FE]** | Frontend features | `# ❖ [FE] Dashboard Redesign` |
| **[Mobile]** | Mobile app features | `# ❖ [Mobile] Push Notifications` |
| **[FS]** | Full stack features | `# ❖ [FS] Real-time Chat` |
| **[DevOps]** | Infrastructure | `# ❖ [DevOps] CI/CD Pipeline` |
| **[QA]** | Testing features | `# ❖ [QA] Test Automation` |

**Note:** Spec mode doesn't use scope prefixes.

## 📝 Structured Descriptions (NEW FORMAT)

Every ticket now uses a concise, structured description format:

```markdown
# ❖ [FE] Advanced Search Filters

Our search functionality is failing to meet user needs and causing lost revenue.

⚠︎ **Key problems/changes:**
* **High abandonment rate** - Majority of users give up before finding what they need
* **No filtering options** - Users scroll through hundreds of irrelevant results
* **Poor relevance** - Basic keyword matching returns unrelated items
* **Mobile frustration** - Search interface breaks on small screens

⁉ **Reasons why:**
By implementing comprehensive filtering capabilities with real-time updates, we'll dramatically improve product discovery, reduce abandonment rates, and increase conversion.

**User Value:** Find exactly what you need with powerful filters
**Business Goal:** Dramatically reduce search abandonment rate
```

## 🎛️ Operating Modes

| Mode | Command | When to Use | Resolution Checklist | Focus |
|------|---------|-------------|---------------------|-------|
| **Interactive** | DEFAULT | No mode specified, guidance needed | Adaptive | User value teaching |
| **Quick** | `$q` | Simple features (explicit request) | 3-5 items | Essential requirements |
| **Standard** | `$s` | Full features (explicit request) | 8-15 items | Complete context |
| **Complex** | `$c` | Multi-phase implementations | 15-30 items | Phased approach |
| **Epic** | `$e` | Major initiatives | 10-20 items | Child ticket breakdown |
| **Spec** | `$spec` | Technical implementation details | 5-10 tests | HOW to implement |

**Note:** Interactive mode is the default unless explicitly specified otherwise.

## 🔧 Spec Mode (NEW)

Create technical implementation specifications when developers need HOW-to guidance:

### When to Use $spec
- User asks "how to implement"
- Request for CSS/JS code
- Technical approach needed
- Browser compatibility questions
- Performance optimization techniques

### Spec Structure
```markdown
# Scrollbar Visibility Implementation Spec

## Objective
Implement dual-container layout with hidden scrollbar on right container.

## CSS Implementation
```css
.right-container {
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE/Edge */
}

.right-container::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}
```

## Browser Compatibility
- **Chrome/Edge**: ✓ `::-webkit-scrollbar`
- **Firefox**: ✓ `scrollbar-width: none`
- **Safari**: ✓ `::-webkit-scrollbar`
- **IE 10+**: ✓ `-ms-overflow-style: none`

## Key Points
- Properties scoped to specific selectors
- No JavaScript required
- Scroll functionality preserved

## Testing Checklist
- [ ] Scrollbar hidden on right container
- [ ] Scroll still functional
- [ ] Works in all browsers
```

## 🔗 Implementation Spec References (NEW)

Standard tickets can now reference implementation specs for technical clarity:

```markdown
## ◇ Requirements

**◊** Search Filters
— Filter Types
• Category multi-select
• Date range picker
• Price range slider
— How to implement?
• Check and follow this implementation spec:
• {Search Filter Implementation Spec}
```

This pattern maintains WHAT/WHY focus while linking to HOW when needed.

## 🏷️ Automatic Label Mapping

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
| Implementation specs | `implementation`, `technical-spec` |

## 📝 How Prompt Improvement Works

The system invisibly enhances vague requests before processing:

### What Gets Enhanced
```
"fix auth" → "create bug fix ticket for authentication"
"DB slow" → "create performance ticket for database"
"how to hide scrollbar" → "create implementation spec for hiding scrollbar"
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
- Mode commands ($q, $s, $spec, etc.)
- Already clear requests
- The need for Interactive mode questions

## 🏗️ Core Components

### WHAT/WHY Philosophy (except $spec mode)
- **WHAT**: Clear description of the feature/fix needed
- **WHY**: User value and business outcomes
- **NOT HOW**: Leave implementation to developers (link to specs if needed)

### Enhanced Symbol System (Required)
- **❖** - Titles and major features (with H1)
- **◇** - Requirements and main sections
- **◊** - Sub-headings within sections
- **→** - Designs & References
- **✓** - Success criteria AND Resolution Checklist
- **⊗** - Dependencies
- **⚠︎** - Key problems/changes in descriptions
- **⁉** - Reasons why in descriptions
- **—** - Sub-categories under **◊** sub-headings

### Complete Ticket Structure
1. Title with `# ❖ [SCOPE]` format
2. Brief intro + ⚠︎ problems + ⁉ reasons
3. User Value statement
4. Business Goal (measurable, no percentages)
5. Requirements (outcome-focused)
   - Use **◊** for complex sections
   - Use — for sub-categories
   - Optional: — How to implement? with spec reference
6. Success Criteria (checkboxes)
7. Resolution Checklist (REQUIRED)
8. Dependencies (if any)
9. Labels (auto-generated)

## 📊 Interactive Mode Example

```
User: how to hide scrollbar on container
System: I notice you're asking HOW to implement something technically. 

Would you like me to create:
1. An implementation spec - with CSS code examples and browser compatibility
2. A development ticket - describing what needs to be done

Which would be more helpful?

User: Implementation spec please

System: Perfect! Let me create a technical implementation spec for you:

[Creates spec with code examples, browser compatibility, and testing checklist]
```

## 🤖 Educational Focus

Interactive mode teaches product thinking by:
- Asking strategic questions about user value
- Focusing on business outcomes (without percentages)
- Detecting when technical specs are needed
- Showing quality metrics and scores
- Providing learning points
- Building skills through practice

## 📈 Quality Assurance

### 2-Minute Readability
All tickets must be scannable and understood in under 2 minutes. Enhanced by:
- Clear scope prefixes for instant understanding
- Structured ⚠︎ problems and ⁉ reasons format
- Visual hierarchy with symbols and icons
- Bullet points instead of paragraphs
- Optional spec links for technical details

### Resolution Checklist Scaling
- **Quick**: 3-5 simple tasks
- **Standard**: 8-15 tasks in categories
- **Complex**: 15-30 phase-based tasks
- **Epic**: 10-20 coordination tasks
- **Spec**: 5-10 testing items

### Success Metrics (No Percentages)
- Vast majority of users complete ticket creation
- Nearly all tickets meet quality standards
- Brief average conversation time
- All maintain readability standards
- Technical specs used when appropriate

## 🔧 MCP Tools Integration

The system intelligently selects thinking tools based on complexity:

### Sequential Thinking MCP
- Simple requests and clear requirements
- Quick ($q), Standard ($s), and Spec ($spec) modes
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

### Standard Feature Request
**Input:** "need better search"
**Result:** 
```markdown
# ❖ [FE] Advanced Search Functionality

Users struggle to find products efficiently, leading to frustration and lost sales.

⚠︎ **Key problems/changes:**
* **Poor relevance** - Search returns unrelated items
* **No filters** - Can't narrow results by category or price
* **Slow performance** - Results take 3-5 seconds to load
* **Mobile issues** - Search UI breaks on small screens

⁉ **Reasons why:**
By implementing advanced search with filters, relevance scoring, and performance optimization, we'll dramatically improve product discovery and increase conversion rates.

**User Value:** Find exactly what you need quickly

**Business Goal:** Increase search-to-purchase conversion

---

## ◇ Requirements

**◊** Search Improvements
— Core Features
• Relevance-based ranking
• Autocomplete suggestions
• Search history
— Filters
• Category selection
• Price range
• Availability toggle
— How to implement?
• Check and follow this implementation spec:
• {Advanced Search Implementation Spec}

---

## Labels
`[App]-App`, `UI`, `Search`, `feature`
```

## ⚠️ Important Notes

- **Scope prefixes required** - Every title needs [BE], [FE], etc. (except spec mode)
- **Structured descriptions** - Use ⚠︎ and ⁉ format
- **Spec mode for HOW** - When implementation details needed
- **No percentages** - Use descriptive language instead
- **Labels auto-generated** - Based on content detection
- **Interactive is default** - Unless mode explicitly specified
- **Never provides implementation** - Except in spec mode
- **Always uses artifacts** - Every ticket/spec in markdown

## 📦 Version History

- **v3.4.0**: Structured descriptions (⚠︎/⁉), Spec mode, implementation references
- **v3.3.0**: Developer-first clarity with scope prefixes, rich descriptions, labels
- **v3.2.0**: Added **◊** sub-heading pattern and structured em dash usage
- **v3.1.0**: Added prompt improvement layer and developer abbreviations
- **v3.0.0**: Introduced mandatory Resolution Checklists
- **v2.0.0**: Interactive mode as default, enhanced educational focus
- **v1.0.0**: Initial WHAT/WHY philosophy implementation

## 🎯 Key Principles

1. **Developer clarity first** through scope prefixes and structured problems
2. **Scannable format** via ⚠︎ problems and ⁉ reasons structure
3. **Separate concerns** - WHAT/WHY in tickets, HOW in specs
4. **Democratize product thinking** through guided creation
5. **Focus on user value** not technical implementation (except spec mode)
6. **Teach through practice** with Interactive mode
7. **Maintain 2-minute readability** for all tickets

## 🆘 Troubleshooting

### Description Issues
- **Long paragraphs**: Use ⚠︎ and ⁉ structure instead
- **Missing icons**: Required for problem/reason sections
- **No bullet points**: Problems should be bulleted list
- **Mixed content**: Keep problems and reasons separate

### Spec Mode Issues
- **No code examples**: Specs must include implementation code
- **Missing compatibility**: Always include browser support
- **No testing checklist**: Required for all specs
- **Business justification**: Specs focus on HOW, not WHY

### Symbol Usage Issues
- **Wrong title format**: Use `# ❖ [SCOPE]` (except spec mode)
- **Missing ◊**: Required for complex requirements
- **Wrong em dash**: Only use — under **◊** sub-headings
- **Missing ⚠︎ or ⁉**: Required in descriptions

### Content Issues
- **Using percentages**: Replace with descriptive terms
- **Implementation in tickets**: Move to spec mode or reference
- **Missing symbols**: Required in all sections
- **No Resolution Checklist**: Required for every ticket

### Interactive Mode
- **Not detecting spec need**: System offers choice for HOW questions
- **Too many questions**: System limits to 3-4 maximum
- **Figma not connecting**: It's optional, continue without

## 📚 Additional Resources

- [Product Management Basics](https://www.productplan.com/learn/product-management-basics/)
- [User Story Writing](https://www.atlassian.com/agile/project-management/user-stories)
- [Writing Clear Requirements](https://www.atlassian.com/agile/requirements)
- [MDN Web Docs](https://developer.mozilla.org/) (for spec mode)
- [Can I Use](https://caniuse.com/) (for browser compatibility)

---

<<<<<<< Updated upstream
*Transform vague requests into crystal-clear tickets that developers understand at first glance. Teach product thinking through practice. Focus on WHAT and WHY, never HOW. Make every ticket immediately actionable with scope, context, and technical clarity.*
=======
*Transform vague requests into crystal-clear tickets with structured problem identification. Create technical specs when HOW matters. Teach product thinking through practice. Make every ticket scannable in under 2 minutes with visual hierarchy and smart formatting.*
>>>>>>> Stashed changes
