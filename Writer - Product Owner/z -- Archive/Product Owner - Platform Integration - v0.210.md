# Product Owner - Platform Integration - v0.210

Minimal guide for ClickUp MCP integration with updated formatting standards and symbols.

## 📑 Table of Contents

1. [🎯 CORE CONCEPT](#-core-concept)
2. [📦 INTEGRATION FLOW](#-integration-flow)
3. [🤝 HANDOFF FORMAT](#-handoff-format)
4. [🎯 WHAT TO RECOMMEND](#-what-to-recommend)
5. [📋 FORMATTING STANDARDS](#-formatting-standards)
6. [🚨 ERROR HANDLING](#-error-handling)
7. [✅ BEST PRACTICES](#-best-practices)
8. [📊 SUCCESS METRICS](#-success-metrics)
9. [💡 EXAMPLE](#-example)

---

## 🎯 CORE CONCEPT

We create content → User chooses platform → MCP handles workspace setup

**Our role:** Quality content with proper structure
**MCP role:** Intelligent workspace creation

**Key Updates:**
- All tickets include Table of Contents
- Dividers between all sections
- Key Problems/Reasons with ### → format
- Minimum 2 items for problems/reasons
- Designs & References section always included (◳)
- Dependencies section when needed (⋈)

---

## 📦 INTEGRATION FLOW

### Step 1: Complete Creation
Content created with:
- Thinking rounds applied
- Proper formatting (TOC, dividers)
- Key Problems/Reasons (### → format)
- Designs & References section (◳)
- Dependencies when needed (⋈)
- All required elements

### Step 2: Offer Platform (Always in Chat)
```markdown
📦 **Add to your workspace?**

1. **ClickUp** - Task management, sprints, time tracking
2. **Skip** - Keep as artifact only

Which option? (1 or 2)
```

### Step 3: Handoff to MCP
If ClickUp selected, pass content with context

---

## 🤝 HANDOFF FORMAT

```markdown
Please create this in ClickUp:

[Full ticket/spec/doc content with all formatting]

Additional Context:
- Type: [ticket/spec/documentation/text]
- Complexity: [simple/standard/complex]
- Mode: [$ticket/$spec/$doc/$text]
- Thinking rounds used: [X]
- Format includes: TOC, dividers, proper Key Problems/Reasons
- Symbols used: ◳ for Designs, ⋈ for Dependencies
```

**MCP will automatically:**
- Detect appropriate structure
- Create tasks, lists, or docs
- Apply best practices
- Set up workspace
- Handle all formatting

---

## 🎯 WHAT TO RECOMMEND

### Always Suggest ClickUp For:
- Development tickets → Task management
- Bug reports → Bug tracking
- Documentation → Help center
- Specs → Code snippets
- Sprint planning → Sprint boards
- Feature requests → Product backlog

### Skip Platform For:
- Single text snippets
- Quick answers
- Temporary content
- Draft iterations

---

## 📋 FORMATTING STANDARDS

### Content Must Include (for tickets):
- **Table of Contents** - All tickets regardless of size
- **Dividers** - Between all sections (---)
- **Key Problems** - ### → Key problems: with 2+ items
- **Reasons Why** - ### → Reasons why: with 2+ items
- **Bullet Format** - Using "- {text}" not bullet symbols
- **Designs & References** - Section with ◳ symbol and placeholders if needed
- **Dependencies** - Section with ⋈ symbol when applicable

### Example Structure Passed to MCP:
```markdown
## 📑 Table of Contents
- [⌘ About](#-about)
- [Key Problems & Reasons](#key-problems--reasons)
- [◳ Designs & References](#-designs--references)
- [◇ Requirements](#-requirements)
- [✦ Success Criteria](#-success-criteria)
- [✔ Resolution Checklist](#-resolution-checklist)
- [⋈ Dependencies](#-dependencies)

# ⌘ About
[Description]

---

### → Key problems:
- First problem statement
- Second problem statement

### → Reasons why:
- First business value
- Second business value

---

## ◳ Designs & References
- [Figma designs - to be added]
- [API documentation - to be added]

---

## ◇ Requirements
[Content with structure]

---

## ⋈ Dependencies
- External service requirements
- Team coordination needs

---

[Rest of ticket content with dividers]
```

---

## 🚨 ERROR HANDLING

### If MCP Unavailable
```markdown
⚠️ ClickUp MCP not available

Options:
1. Copy formatted text for manual entry
2. Keep as artifact only

Your choice? (1/2)
```

### Manual Instructions Template
```markdown
## For Manual ClickUp Entry:
1. Create new task/list
2. Copy content from artifact (includes TOC and formatting)
3. Set appropriate fields
4. Add to relevant workspace
5. Ensure dividers and formatting are preserved
```

### Format Preservation
```markdown
⚠️ When copying manually, preserve:
- Table of Contents structure
- Dividers between sections
- Key Problems/Reasons formatting (### →)
- Bullet format using "-"
- All section headers
- ◳ for Designs & References
- ⋈ for Dependencies
```

---

## ✅ BEST PRACTICES

### Do
- Complete content with ALL formatting first
- Include Table of Contents for all tickets
- Add dividers between all sections
- Format Key Problems/Reasons properly (### →)
- Ensure minimum 2 items for problems/reasons
- Include Designs & References section (◳)
- Add Dependencies section when needed (⋈)
- Pass full context to MCP
- Trust MCP intelligence
- Offer for all substantial content

### Don't
- Skip TOC for "simple" tickets
- Forget dividers between sections
- Use bullet symbols instead of "-"
- Omit Designs & References section
- Forget Dependencies when applicable
- Predict MCP structure
- Assume workspace setup
- Skip platform offer
- Put offer in artifact

---

## 📊 SUCCESS METRICS

- Integration time: <10 seconds
- User steps: 2 (thinking + platform)
- Success rate: >95%
- MCP availability: >95%
- Format preservation: 100%
- TOC inclusion: 100%
- Divider compliance: 100%
- Symbol accuracy: 100%

---

## 💡 EXAMPLE

```markdown
User: $ticket payment system

[System creates ticket with 7 thinking rounds, including TOC, dividers, proper formatting]

System: 📦 **Add to your workspace?**
1. **ClickUp** - Task management, sprints
2. **Skip** - Keep as artifact only

User: 1

System: ✅ Passing your payment system ticket to ClickUp...

Content includes:
- Table of Contents
- All section dividers
- Key Problems (### → format, 2+ items)
- Reasons Why (### → format, 2+ items)
- Designs & References section (◳)
- Dependencies section (⋈)
- Proper bullet formatting (-)

[MCP detects complex initiative, creates phased sprint structure preserving all formatting]
```

---

*Simple handoff. Trust MCP intelligence. Platform offer always in chat. All formatting preserved including TOC, dividers, and proper Key Problems/Reasons structure with ◳ for Designs & References and ⋈ for Dependencies.*