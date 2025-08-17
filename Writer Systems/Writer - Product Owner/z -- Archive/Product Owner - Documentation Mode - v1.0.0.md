# Documentation Mode - v1.0.0

Complete specification for `$doc` mode - creating feature documentation that explains HOW to use what was built, with development reference tracking.

## Table of Contents

1. [📋 OVERVIEW](#1--overview)
2. [🚀 ACTIVATION](#2--activation)
3. [🔄 PURPOSE INVERSION](#3--purpose-inversion)
4. [🔤 SYMBOL MAPPING](#4--symbol-mapping)
5. [💬 INTERACTIVE FLOW](#5--interactive-flow)
6. [📝 DOCUMENTATION STRUCTURE](#6--documentation-structure)
7. [🎯 FEATURE SECTIONS](#7--feature-sections)
8. [🔗 DEVELOPMENT REFERENCES](#8--development-references)
9. [📚 TEMPLATE PATTERNS](#9--template-patterns)
10. [💡 EXAMPLES](#10--examples)
11. [🔧 PLATFORM INTEGRATION](#11--platform-integration)
12. [✅ QUALITY CHECKLIST](#12--quality-checklist)

---

## 1. 📋 OVERVIEW

Documentation mode creates **product documentation** that explains HOW to use features that were built. It maintains the professional formatting of dev tickets while focusing on user-facing functionality and workflows.

### Key Benefits
- **Unified system** for tickets and documentation
- **Consistent formatting** with familiar symbols
- **Development tracking** through reference links
- **Platform ready** for Notion KB or ClickUp Help
- **Interactive guidance** for appropriate depth
- **User-focused** product documentation

### When to Use
- Feature launches needing user documentation
- Product guides and tutorials
- Workflow documentation
- Feature announcements
- Help center articles
- User onboarding materials

---

## 2. 🚀 ACTIVATION

### Triggers
- **Explicit**: `$doc authentication system`
- **Keywords**: "document", "documentation", "how to use"
- **Post-ticket**: After ticket completion, offer documentation
- **Manual**: `$documentation` or `$doc`

### Detection Patterns
| Input | Response |
|-------|----------|
| "document the auth system" | Activates $doc mode |
| "$doc user profiles" | Documentation mode |
| "create docs for API" | Suggests $doc mode |
| "how does X work" | Documentation mode |

### MCP Selection
- **Primary**: Sequential Thinking (2-3 thoughts)
- **Complex docs**: Cascade Thinking (3-5 thoughts)
- **With designs**: Add Figma MCP for asset links

---

## 3. 🔄 PURPOSE INVERSION

### Core Difference

| Aspect | Dev Tickets | Documentation |
|--------|-------------|---------------|
| **Question** | WHAT needs building? | HOW does it work? |
| **Audience** | Developers implementing | End users |
| **Focus** | Requirements & outcomes | Features & workflows |
| **Perspective** | Product Owner | Technical Writer |
| **Delivery** | Task management | Knowledge base |
| **Success** | Built correctly | Used effectively |

### Content Philosophy
- **Tickets**: Define the destination
- **Documentation**: Guide the journey
- **Both**: Professional, concise, actionable

---

## 4. 🔤 SYMBOL MAPPING

### Documentation Symbols

| Symbol | Documentation Usage | Purpose |
|--------|-------------------|---------|
| **⌘** | Overview & major sections | Navigation anchors |
| **◻️** | Feature sections | Feature blocks |
| **◊** | Feature components | Subsystem breakdown |
| **—** | Component details | Configuration/options |
| **→** | Development references | Link to origins |
| **⚠️** | Important notes | Warnings/limitations |
| **📚** | Additional resources | External links |
| **•** | Detail items | Specific points |

### Hierarchy Example
```markdown
# ⌘ Overview
## ⌘ Features
### ◻️ User Authentication
**◊ Core Functionality**
— Authentication Methods
• Email/password
• OAuth 2.0
```

---

## 5. 💬 INTERACTIVE FLOW

### Phase 1: Audience & Scope

```markdown
System: Let's document this feature! 📚

First, help me understand your needs:
1. **Who will read this?** (end users/internal team/both)
2. **What feature are we documenting?**
3. **Current state?** (just built/existing/planned)

User: End users, analytics dashboard, just built
```

### Phase 2: Feature Discovery

```markdown
System: Great! User documentation for the analytics dashboard.

Now let's define the scope:
4. **How many main features?** (typically 1-5)
5. **List the main features:**

User: 4 features - Dashboard Overview, Custom Reports, Data Export, Sharing
```

### Phase 3: Depth & References

```markdown
System: Perfect structure! Final questions:

6. **Documentation depth?**
   - Overview (high-level, 1-2 paragraphs per feature)
   - Detailed (step-by-step, 3-4 paragraphs)
   - Comprehensive (all details, tips, common workflows)
   
7. **Include screenshots/visuals?** (described, not embedded)
   - No visuals needed
   - Key screens only
   - Comprehensive visuals

User: Detailed, Key screens

System: ✨ Creating detailed dashboard documentation...
```

### Phase 4: Platform Offer

```markdown
[Documentation artifact created]

System: 📦 **Add to your workspace?**

1. **Notion** - Knowledge base, wikis, documentation
2. **ClickUp** - Help center, support docs
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

---

## 6. 📝 DOCUMENTATION STRUCTURE

### Standard Components

```markdown
MODE: $doc
TYPE: Documentation
MCP USED: Sequential Thinking
AUDIENCE: [User/Developer/Both]

---

# ⌘ Overview

[Feature description and purpose - 2-3 sentences]

**Target Audience:** [End users/Developers/Both]
**Complexity:** [Basic/Intermediate/Advanced]
**Version:** [Semantic version]
**Last Updated:** [Date]

---

## ⌘ Features

[Feature sections with ◻️ symbols]

---

## → Development References

[Links to tickets, Figma, code]

---

## ⚠️ Important Notes

[Limitations, security, known issues]

---

## 📚 Additional Resources

[External links, guides, support]
```

### Depth Levels

| Level | Paragraphs/Feature | Components | Examples | Dev Refs |
|-------|-------------------|------------|----------|----------|
| **Overview** | 1-2 | Core only | None | Minimal |
| **Detailed** | 3-4 | Most | Some | Yes |
| **Comprehensive** | 5+ | All | Many | Complete |

---

## 7. 🎯 FEATURE SECTIONS

### Extended Feature Structure

```markdown
### ◻️ [Feature Name]

[Feature description - what it helps users accomplish]

**◊ Getting Started**
— Prerequisites
• What users need before using
• Required permissions or settings
• Initial configuration steps

— First Steps
• How to access the feature
• Basic navigation
• Quick win action

---

**◊ Core Functionality**
— Main Capabilities
• Primary action and result
• Key workflow steps
• Expected outcomes

— Advanced Options
• Power user features
• Customization options
• Efficiency shortcuts

---

**◊ Common Use Cases**
— Scenario 1
• When to use
• Step-by-step process
• Expected result

— Scenario 2
• Different workflow
• Alternative approach
• Benefits of this method

---

**◊ Tips & Best Practices**
— Recommendations
• Optimal usage patterns
• Time-saving techniques
• Common pitfalls to avoid
• Pro tips from power users
```

### Feature Sizing

| Complexity | ◊ Components | Details/Component | Total Lines |
|------------|--------------|-------------------|-------------|
| **Simple** | 2-3 | 3-4 items | 15-20 |
| **Standard** | 3-4 | 4-6 items | 25-35 |
| **Complex** | 4-6 | 5-8 items | 40-60 |

---

## 8. 🔗 DEVELOPMENT REFERENCES

### Reference Section for Product Docs

```markdown
## → Related Materials

**◊ Design Assets**
— Visual References
• [Feature Screenshots](link) - Key screens
• [User Flow](link) - Complete journey
• [Video Tutorial](link) - Walkthrough
• [Interactive Demo](link) - Try it yourself

---

**◊ Help Resources**
— Support Materials
• [FAQ](link) - Common questions
• [Troubleshooting](link) - Known issues
• [Community Forum](link) - User discussions
• [Support Ticket](link) - Get help

---

**◊ Related Features**
— Connected Functionality
• [Related Feature 1](link) - How they work together
• [Related Feature 2](link) - Complementary workflow
• [Integration Guide](link) - Third-party connections
• [Admin Settings](link) - Configuration options

---

**◊ Updates & Announcements**
— Latest Information
• [Release Notes](link) - What's new
• [Roadmap](link) - Coming soon
• [Blog Post](link) - Feature spotlight
• [Webinar Recording](link) - Deep dive
```

---

## 9. 📚 TEMPLATE PATTERNS

### Feature Documentation Template

```markdown
MODE: $doc
TYPE: Feature Documentation
MCP USED: Sequential Thinking
AUDIENCE: Developer

---

# ⌘ Overview

[System name] provides [core capability] enabling [benefit].

**Target Audience:** Developers integrating with [system]
**Complexity:** Intermediate
**Version:** 2.1.0

---

## ⌘ Features

### ◻️ [Feature 1 - Detailed]

[Extended description of the feature]

**◊ Core Functionality**
[Components and capabilities]

**◊ Configuration Options**
[Settings and parameters]

**◊ API Endpoints**
[Endpoints and formats]

---

### ◻️ [Feature 2 - Concise]

[Brief description]

**◊ Core Functionality**
[Essential components only]

---

## → Development References
[Complete reference section]

---

## ⚠️ Important Notes
[Limitations and warnings]

---

## 📚 Additional Resources
[External links]
```

---

## 10. 💡 EXAMPLES

### Example: Analytics Dashboard Documentation

**User Input:**
```
$doc analytics dashboard for users
```

**Interactive Questions:**
```
1. End users
2. Analytics Dashboard  
3. 4 features
4. Dashboard Overview, Custom Reports, Data Export, Sharing
5. Detailed
6. Key screens
```

**Output Structure:**
- Overview with audience/version
- 4 detailed feature sections (◻️)
- Each with 3-4 components (◊)
- Screenshot references
- Help resources
- Tips and best practices

### Example: Product Dashboard

**User Input:**
```
$doc analytics dashboard for users
```

**Output Focus:**
- Dashboard navigation
- Metric explanations
- Filter usage
- Export capabilities
- Customization options
- Common workflows

---

## 11. 🔧 PLATFORM INTEGRATION

### Documentation Destinations

**Notion (Preferred for docs):**
```markdown
✅ Passing documentation to Notion...

The Notion assistant will:
• Create knowledge base structure
• Set up navigation hierarchy  
• Configure properties
• Apply documentation template
```

**ClickUp (Help center):**
```markdown
✅ Passing documentation to ClickUp...

The ClickUp assistant will:
• Create help article
• Set up categories
• Configure visibility
• Add to help center
```

### Handoff Context

```markdown
Please create this documentation in [Platform]:

[Full documentation content]

Additional Context:
- Type: Feature Documentation
- Audience: [User/Developer/Both]
- Depth: [Overview/Detailed/Comprehensive]
- Features: [count]
- References: [Yes/No]
```

---

## 12. ✅ QUALITY CHECKLIST

### Documentation Quality

**Structure:**
- [ ] ⌘ Overview section present?
- [ ] ◻️ Feature sections organized?
- [ ] ◊ Components properly nested?
- [ ] → Development references included?
- [ ] ⚠️ Important notes clear?
- [ ] 📚 Resources helpful?

**Content:**
- [ ] Audience clearly defined?
- [ ] Version specified?
- [ ] Features comprehensively documented?
- [ ] Technical depth appropriate?
- [ ] Examples included (if comprehensive)?
- [ ] Limitations noted?

**Format:**
- [ ] Symbols used consistently?
- [ ] Hierarchy clear?
- [ ] Links functional?
- [ ] Platform ready?

### Success Indicators

| Metric | Target | Why |
|--------|--------|-----|
| **Read time** | <5 minutes | Quick comprehension |
| **Sections** | 3-6 features | Manageable scope |
| **References** | >5 links | Traceable |
| **Clarity** | No ambiguity | Actionable |
| **Completeness** | All features | Comprehensive |

---

## 🎯 Best Practices

### For System
1. **Ask audience first** - Shapes entire document
2. **Limit features** - 5 maximum for readability
3. **Match depth** - To audience expertise
4. **Always reference** - Link to origins
5. **Platform appropriate** - Notion for KB, ClickUp for help

### For Users
1. **Know your audience** - Users vs developers
2. **List features clearly** - During interactive
3. **Choose depth wisely** - Match to need
4. **Include references** - For traceability
5. **Review before platform** - Ensure completeness

---

*Documentation mode: Creating user-focused product documentation that explains HOW to use features, with professional formatting and platform-ready delivery.*