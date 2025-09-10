# Ticket - Interactive Mode - v0.191

Complete specification for `$interactive` mode - the conversational ticket creation system that guides users through writing clear, actionable tickets.

## Table of Contents

1. [📋 OVERVIEW](#1--overview)
2. [🚀 ACTIVATION](#2--activation)
3. [📄 CONVERSATION FLOW](#3--conversation-flow)
4. [❓ QUESTION SYSTEM](#4--question-system)
5. [🚨 INTERACTIVE OFFERS](#5--interactive-offers)
6. [🎨 FIGMA INTEGRATION](#6--figma-integration)
7. [💬 CONVERSATION EXAMPLES](#7--conversation-examples)
8. [📊 VISUAL DASHBOARD](#8--visual-dashboard)
9. [🚨 ERROR HANDLING](#9--error-handling)
10. [✅ BEST PRACTICES](#10--best-practices)

---

## 1. 📋 OVERVIEW

Interactive mode is the **DEFAULT** for all ticket creation. It provides conversational guidance to ensure quality and consistency.

### Key Benefits
- Democratizes professional ticket writing
- Teaches WHAT/WHY vs HOW thinking
- Ensures consistent quality
- Maintains 2-minute readability
- Optional Figma integration
- **20% more concise than v4.1**
- **First heading always "About" with ⌘ icon**
- **Checkbox format `[]` without space**
- **Dividers between requirement subsections**

### When Active
- **Default**: Any request without mode
- **Offered**: When users specify $s or $c
- **Automatic**: Vague/incomplete requests
- **Manual**: `$interactive` or `$int`

---

## 2. 🚀 ACTIVATION

### Automatic Triggers
- No mode specified (DEFAULT)
- Request under 10 words
- Missing critical context
- Keywords: "help", "not sure", "guide me"

### Offered When
- User specifies `$s` or `$c`
- System offers guidance option

### Manual
```
$interactive "feature idea"
$int search improvement
```

### Smart Detection
| Input | Response |
|-------|----------|
| "need login" | Activates interactive |
| "$s user profiles" | **Offers interactive first** |
| "$c payment" | **Offers interactive first** |
| "help with tickets" | Activates with welcome |

---

## 3. 📄 CONVERSATION FLOW

### Phase 1: Welcome

**First-Time:**
```markdown
🎯 **Welcome to Dev Ticket Writer!**

I'll help you create clear tickets that communicate user value and business outcomes.

I'll guide you through:
1. Understanding user needs
2. Identifying scope and labels
3. Defining success criteria (✦ bullets)
4. Creating resolution checklists (✓ checkboxes with `[]` format)

**Ready?** Tell me about your feature!
```

**Returning:**
```markdown
Welcome back! 👋 Let's create another ticket.

What feature or improvement today?
```

**From Offer:**
```markdown
Great choice! Let's build this together.

First, the core problem...