# Product Owner - Platform Integration - v2.0.0

Minimal guide for ClickUp MCP integration.

## 📑 Table of Contents

1. [🎯 CORE CONCEPT](#-core-concept)
2. [📦 INTEGRATION FLOW](#-integration-flow)
3. [🤝 HANDOFF FORMAT](#-handoff-format)
4. [🎯 WHAT TO RECOMMEND](#-what-to-recommend)
5. [🚨 ERROR HANDLING](#-error-handling)
6. [✅ BEST PRACTICES](#-best-practices)
7. [📊 SUCCESS METRICS](#-success-metrics)
8. [💡 EXAMPLE](#-example)

---

## 🎯 CORE CONCEPT

We create content → User chooses platform → MCP handles workspace setup

**Our role:** Quality content with proper structure
**MCP role:** Intelligent workspace creation

---

## 📦 INTEGRATION FLOW

### Step 1: Complete Creation
Content created with thinking rounds, proper formatting

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

[Full ticket/spec/doc content]

Additional Context:
- Type: [ticket/spec/documentation/text]
- Complexity: [simple/standard/complex]
- Mode: [$ticket/$spec/$doc/$text]
- Thinking rounds used: [X]
```

**MCP will automatically:**
- Detect appropriate structure
- Create tasks, lists, or docs
- Apply best practices
- Set up workspace

---

## 🎯 WHAT TO RECOMMEND

### Always Suggest ClickUp For:
- Development tickets → Task management
- Bug reports → Bug tracking
- Documentation → Help center
- Specs → Code snippets
- Sprint planning → Sprint boards

### Skip Platform For:
- Single text snippets
- Quick answers
- Temporary content

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
2. Copy content from artifact
3. Set appropriate fields
4. Add to relevant workspace
```

---

## ✅ BEST PRACTICES

### Do
- Complete content first
- Pass full context to MCP
- Trust MCP intelligence
- Offer for all substantial content

### Don't
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

---

## 💡 EXAMPLE

```markdown
User: $ticket payment system

[System creates ticket with 7 thinking rounds]

System: 📦 **Add to your workspace?**
1. **ClickUp** - Task management, sprints
2. **Skip** - Keep as artifact only

User: 1

System: ✅ Passing your payment system ticket to ClickUp...

[MCP detects complex initiative, creates phased sprint structure]
```

---

*Simple handoff. Trust MCP intelligence. Platform offer always in chat.*