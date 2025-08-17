# Documentation Mode - v5.0.0

Complete specification for `$doc` mode - creating user-focused product documentation through interactive guidance.

## Table of Contents

1. [📋 OVERVIEW](#1--overview)
2. [🚀 ACTIVATION](#2--activation)
3. [💬 INTERACTIVE FLOW](#3--interactive-flow)
4. [📤 SYMBOL MAPPING](#4--symbol-mapping)
5. [📝 DOCUMENTATION STRUCTURE](#6--documentation-structure)
6. [🎯 FEATURE SECTIONS](#7--feature-sections)
7. [🔗 DEVELOPMENT REFERENCES](#8--development-references)
8. [📚 TEMPLATE PATTERNS](#9--template-patterns)
9. [💡 EXAMPLES](#10--examples)
10. [🔧 PLATFORM INTEGRATION](#11--platform-integration)
11. [✅ QUALITY CHECKLIST](#12--quality-checklist)

---

## 1. 📋 OVERVIEW

Documentation mode creates **product documentation** through interactive guidance, explaining HOW to use features while maintaining professional formatting consistent with the ticket system.

### Key Benefits
- **Interactive guidance** ensures completeness
- **Unified system** with tickets and specs
- **Consistent formatting** with familiar symbols
- **Platform ready** for Notion KB or ClickUp Help
- **User-focused** product documentation
- **Skips discovery** - knows it's documentation

### When to Use
- Feature launches needing user guides
- Product tutorials and walkthroughs
- Workflow documentation
- Feature announcements
- Help center articles
- User onboarding materials

---

## 2. 🚀 ACTIVATION

### Direct Trigger
```markdown
User: $doc analytics dashboard

System: Let's document the analytics dashboard! 📚
[Skips discovery, goes straight to documentation questions]
```

### From Discovery
```markdown
User: need to explain how dashboard works

System: Welcome! Let's figure out what you need. 🤔
[Discovery flow leading to documentation]
```

### MCP Selection
- **Primary**: Sequential Thinking (2-3 thoughts)
- **Complex docs**: Cascade Thinking (3-5 thoughts)
- **With designs**: Add Figma MCP for asset links

---

## 3. 💬 INTERACTIVE FLOW

### Phase 1: Audience & Purpose

```markdown
System: Let's document this feature! 📚

I'll help create clear user documentation.

First, tell me:
1. **Who will read this?** (end users/internal team/both)
2. **What feature are we documenting?**
3. **Current state?** (live/beta/planned)

User: End users, analytics dashboard, live
```

### Phase 2: Feature Discovery

```markdown
System: Perfect! User documentation for the live analytics dashboard.

Now let's define the scope:
4. **How many main features?** (typically 1-5)
5. **List the main features:**

User: 4 features
- Dashboard Overview
- Custom Reports  
- Data Export
- Sharing & Collaboration
```

### Phase 3: Depth & Details

```markdown
System: Great structure! Final questions:

6. **Documentation depth?**
   - Overview (high-level, 1-2 paragraphs per feature)
   - Detailed (step-by-step, 3-4 paragraphs)
   - Comprehensive (all details, tips, common workflows)
   
7. **Include screenshots/visuals?** (described, not embedded)
   - No visuals needed
   - Key screens only
   - Comprehensive visuals

User: Detailed, key screens

System: ✨ Creating detailed dashboard documentation with key screen references...
```

### Phase 4: Platform Integration

```markdown
[Documentation artifact created]

System: 📦 **Add to your workspace?**

1. **ClickUp** - Help center, support docs
2. **Notion** - Knowledge base, wikis (recommended)
3. **Skip** - Keep as artifact only

Which option? (1, 2, or 3)
```

---

## 4. 📤 SYMBOL MAPPING

### Documentation Symbols

| Symbol | Usage | Purpose |
|--------|-------|---------|
| **⌘** | Overview & major sections | Navigation |
| **◻️** | Feature sections | Feature blocks |
| **◊** | Feature components | Subsystem breakdown |
| **—** | Component details | Options/configuration |
| **→** | Development references | Link to resources |
| **⚠️** | Important notes | Warnings/limitations |
| **📚** | Additional resources | External links |
| **•** | Detail items | Specific points |

### Hierarchy
```markdown
# ⌘ Overview
## ⌘ Features
### ◻️ Feature Name
**◊ Component**
— Details
• Specific points
```

---

## 5. 📝 DOCUMENTATION STRUCTURE

### Standard Components

```markdown
MODE: $doc
TYPE: Feature Documentation
MCP USED: Sequential Thinking
AUDIENCE: [User/Developer/Both]

---

# ⌘ Overview

[Feature description - 2-3 sentences]

**Target Audience:** [End users/Developers/Both]
**Complexity:** [Basic/Intermediate/Advanced]
**Version:** [Semantic version]
**Last Updated:** [Date]

---

## ⌘ Features

[Feature sections with ◻️ symbols]

---

## → Development References

[Links to resources]

---

## ⚠️ Important Notes

[Limitations, warnings]

---

## 📚 Additional Resources

[External links, guides]
```

---

## 7. 🎯 FEATURE SECTIONS

### Depth-Based Structure

#### Overview Depth (1-2 paragraphs)
```markdown
### ◻️ Dashboard Overview

Quick access to all your key metrics in one place. View trends, monitor performance, and identify opportunities at a glance.

**◊ Key Capabilities**
— Available metrics
• User engagement
• Performance data
• Business KPIs
```

#### Detailed Depth (3-4 paragraphs)
```markdown
### ◻️ Dashboard Overview

Your central command center for data-driven decisions. The dashboard presents real-time metrics with customizable views.

**◊ Getting Started**
— Prerequisites
• Account with analytics permissions
• Data collection enabled (7+ days)
• Modern browser

— Navigation
• Access from main menu
• Select date range (top right)
• Choose metric view

---

**◊ Core Functionality**
— Metric Display
• Real-time updates every 15 minutes
• Historical comparisons
• Trend indicators
• Custom thresholds

---

**◊ Customization**
— Personalization Options
• Rearrange widget layout
• Select preferred metrics
• Set refresh intervals
• Save custom views

---

*Documentation creation that adapts to complexity. Smart depth detection guides users from overview to implementation. Every section scales to user needs.*