# Prompt Engineering Assistant - User Guide v8.1.0

A comprehensive system that transforms vague requests into clear, effective AI prompts using the ATLAS thinking framework, challenge-based simplification, and intelligent refinement. Now with MANDATORY thinking rounds, professional artifact standards, enhanced pattern learning, and SMILE format support for better instruction following! Features 8 operating modes including 3 specialized Builder sub-modes for creating universal creative briefs that work on ANY AI development platform while aggressively minimizing complexity and resource usage.

## 📑 Table of Contents

- [🆕 What's New in v8.1.0](#-whats-new-in-v810)
- [📖 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
  - [Core Modes](#core-modes)
  - [Builder Sub-Modes](#builder-sub-modes-universal-ai-platform-support)
  - [Supported Platforms](#supported-platforms-include)
- [📄 Format Options](#-format-options-new)
  - [Standard Format](#standard-format-default)
  - [JSON Format](#json-format)
  - [SMILE Format](#smile-format)
- [🗂️ Frameworks Overview](#️-frameworks-overview-v810)
  - [Core Frameworks](#core-frameworks)
  - [Builder Creative Frameworks](#builder-creative-frameworks-universal)
- [📊 Enhanced Report Examples](#-enhanced-report-examples)
- [💰 Smart Resource Optimization](#-smart-resource-optimization-enhanced)
- [🧠 ATLAS Thinking Framework](#-atlas-thinking-framework)
  - [How ATLAS Works](#how-atlas-works)
  - [Challenge Mode](#challenge-mode)
  - [User Interaction](#user-interaction)
- [🚀 Challenge Mode Philosophy](#-challenge-mode-philosophy)
- [🚨 REPAIR Error Protocol](#-repair-error-protocol)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes-v810)
- [📦 Version History](#-version-history)
- [🎯 Key Principles](#-key-principles-v810)
- [📈 Performance Metrics](#-performance-metrics)
- [📚 Additional Resources](#-additional-resources)

.

## 🆕 What's New in v8.1.0

### Critical System Improvements 🔴
- **MANDATORY Thinking Rounds**: System ALWAYS asks "How many thinking rounds? (1-10)" - NO EXCEPTIONS, even for simple requests
- **Professional Artifact Standards**: New document enforcing AI System details at bottom, proper formatting
- **Enhanced Interactive Mode**: Clean formatting with **bold headers** and • bullet points
- **Advanced Pattern Learning**: Uses `conversation_search()` and `recent_chats()` for intelligent context

### Enhanced Features from v8.0.0
- **SMILE Format Integration**: Emoticon-structured prompts for better instruction following
- **Multi-Format Support**: Every enhancement now available in Standard, JSON, and SMILE formats
- **Intelligent Format Selection**: System recommends optimal format based on complexity and patterns
- **Token Transparency**: Always shows token impact for SMILE format (+20-30% typical)
- **Pattern Learning**: Now searches conversation history for your preferences

### v8.1.0 Mandatory Process
```markdown
**How many thinking rounds would you like? (1-10, or 'auto' for my recommendation)**

Based on your request, I recommend: **[X] rounds**
• **Clarity:** [Low/Medium/High] - [specific reason]
• **Complexity:** [Simple/Standard/Complex] - [specific aspect]
• **Enhancement:** [Minimal/Moderate/Comprehensive] - [opportunity level]

[Previous patterns: You typically choose [X] rounds for similar prompts]

Your choice?
```
**System WAITS for response - NO AUTO-PROCEEDING**

.

## 📖 Overview

The Prompt Engineering Assistant helps users craft powerful, precise prompts through systematic simplification and challenge-based thinking. Version 8.1.0 MANDATES thinking rounds for every enhancement, enforces professional artifact standards with AI System details at bottom, and uses conversation history for intelligent pattern learning. The system actively questions complexity while delivering professional-grade prompts that maximize clarity, minimize unnecessary specifications, and offers multiple format options to suit different use cases.

### What is SMILE Format?
SMILE ((: Smile) is an open-source prompt instruction language created by Dr. Thomas Ager, Ph.D. at Cardiff University. It uses emoticon-based brackets to structure prompts for Large Language Models, designed to increase instruction following while maintaining readability.

### v8.1.0 Core Changes
- **Thinking Rounds**: MANDATORY - asked every time, no exceptions
- **Artifact Standards**: Professional formatting with AI System at bottom
- **Pattern Learning**: Searches your conversation history for context
- **User Control**: Absolute - all options always available

.

## ✨ Key Features

### Core Capabilities
- **MANDATORY Thinking Rounds**: 1-10 or 'auto' - ALWAYS ASKED
- **Professional Artifacts**: AI System details at bottom, proper formatting
- **Pattern Learning**: Uses conversation history for intelligent suggestions
- **Multi-Format Output**: Standard, JSON, and SMILE formats
- **ATLAS Thinking Framework**: 5-phase systematic enhancement + Format Transform
- **Challenge Mode**: Automatic at 3+ rounds - "Could this be simpler?"
- **Smart Defaults**: Reduces questions by 60% using patterns
- **REPAIR Protocol**: Recognize, Explain, Propose, Adapt, Iterate, Record
- **30-50% Complexity Reduction**: Measurable simplification
- **Universal Platform Support**: Works on ALL AI platforms

### v8.1.0 Enhancements
- **Conversation Search**: Finds patterns in your history
- **Recent Chats**: Analyzes recent interactions
- **Format Intelligence**: Learns your format preferences
- **Token Impact Display**: Shows overhead for each format
- **Interactive Formatting**: Professional bold headers and bullets
- **Never Restrictive**: Patterns as context only

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Prompt Engineering Assistant v8.1"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Prompt Improver - v8.1.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these v8.1.0 documents to your project's knowledge base:

**Critical Documents (v8.1.0):**
- `Prompt - Core System & Quick Reference - v3.2.0.md` (Mandatory behaviors)
- `Prompt - Artifact Standards & Templates - v1.0.0.md` (NEW - Required formatting)
- `Prompt - ATLAS Thinking Framework - v2.0.0.md` (With Format Transform)

**Mode Documents (v8.1.0):**
- `Prompt - Interactive Mode - v6.1.0.md` (Professional formatting)
- `Prompt - Builder Mode - v4.1.0.md` (Table-based platform guide)
- `Prompt - Evaluation & Refinement - v6.0.0.md` (Format assessment)
- `Prompt - Patterns & Enhancements - v6.0.0.md` (Multi-format templates)

### Step 4: Start Creating with Mandatory Process
Simply paste your prompt or describe what you need:
```
write about dogs                       # Asks thinking rounds, then enhances
$improve analyze customer data         # Asks thinking rounds, offers formats
$smile create complex workflow         # Asks thinking rounds, SMILE primary
$json api integration specs           # Asks thinking rounds, JSON primary
$interactive                          # Guided with professional formatting
$prototype explore dashboard concepts # Asks thinking rounds, then builds
```

.

## 🎛️ Operating Modes

### Core Modes

| Mode | Activation | Purpose | Best For | Challenge Focus | Thinking Mandatory | Format Support |
|------|------------|---------|----------|-----------------|-------------------|----------------|
| **$short** | `$short` or `$s` | Quick minimal refinement | Simple clarity | "Even this needed?" | YES (1-2) | Standard only |
| **$improve** | `$improve` or `$i` (DEFAULT) | Smart enhancement | Most improvements | Balance completeness | YES (3-4) | All formats |
| **$refine** | `$refine` or `$r` | Full optimization | Maximum quality | Multiple alternatives | YES (5-8) | All formats |
| **$interactive** | `$interactive` | Guided help | Learning | Smart defaults | YES (variable) | User choice |
| **$json** | `$json` or `$j` | API format | Programmatic | Minimize overhead | YES (2-3) | JSON primary |
| **$smile** | `$smile` or `$sm` | SMILE format | Complex instructions | Structure necessity | YES (2-3) | SMILE primary |

### Builder Sub-Modes (Universal AI Platform Support!)

| Sub-Mode | Activation | Purpose | Challenge Priority | Default Phase | Thinking Mandatory | Format Options |
|----------|------------|---------|-------------------|---------------|-------------------|----------------|
| **Builder** | `$builder` | Auto-detect needs | "Simpler platform?" | Phase 1 only | YES | Standard/SMILE |
| **Prototype** | `$prototype` | Visual exploration | "Paper prototype?" | MVP exploration | YES | Standard/SMILE |
| **Website** | `$website` | Conversion sites | "Landing page first?" | Core message | YES | Standard |
| **App** | `$app` | Applications | "Which features critical?" | Essential only | YES | Standard/SMILE |

### Supported Platforms Include:
- **Bolt.new** - Challenge: "Start with Phase 1"
- **MagicPatterns** - Challenge: "Simpler components?"
- **v0 by Vercel** - Challenge: "Necessary features only"
- **Cursor/Windsurf** - Challenge: "Reduce dependencies"
- **Replit** - Challenge: "MVP first"
- **Lovable** - Challenge: "Minimize credit usage"
- **No-code platforms** - Challenge: "Why custom code?"
- **ANY AI Platform** - Universal principles apply

.

## 📄 Format Options (NEW!)

### Standard Format (Default)
- **Purpose**: Natural language clarity, maximum readability
- **Token Impact**: Baseline
- **Best For**: Most prompts, human understanding, simple to moderate complexity
- **Always Available**: Yes

Example:
```
As a data analyst, analyze Q4 sales data focusing on revenue drivers and growth patterns. 
Create an executive summary with actionable insights.
```

### JSON Format
- **Purpose**: Structured for APIs and programmatic use
- **Token Impact**: Usually -5% to +5%
- **Best For**: Technical integration, system interfaces, structured data
- **Availability**: When structured data benefits
- **Pattern Learning**: System tracks when you prefer JSON

Example:
```json
{
  "role": "data_analyst",
  "task": "analyze_q4_sales",
  "focus": ["revenue_drivers", "growth_patterns"],
  "output": "executive_summary",
  "requirements": ["actionable_insights"]
}
```

### SMILE Format
- **Purpose**: Enhanced instruction following through emoticon structure
- **Token Impact**: +20-30% typically
- **Best For**: Complex multi-step instructions, detailed requirements
- **Availability**: Complexity > 3 or when structure helps
- **Pattern Tracking**: System learns your SMILE usage preferences

Example:
```
(: Sales Analysis Task
  [: Role [ Data analyst ] :]
  [= Task =] Analyze Q4 sales data
  
  [: Requirements [
    [! Priority: Revenue drivers !]
    • Growth pattern analysis
    • Trend identification
    • Actionable insights
  ] :]
  
  [: Output Format [
    Executive Summary
    {Key findings with data}
    {Strategic recommendations}
  ] :]
) :)
```

### Format Selection Guide (v8.1.0 Enhanced)

| Complexity | Recommended | Alternative | Pattern Context | Token Note |
|------------|------------|-------------|-----------------|------------|
| Simple (1-3) | Standard | - | Previous choices shown | Baseline |
| Moderate (4-6) | Standard | JSON if API, SMILE if structured | Format history displayed | Monitor overhead |
| Complex (7-10) | SMILE | Standard with sections | SMILE preference tracked | +20-30% justified |

### SMILE Symbol Reference

| Symbol | Purpose | When to Use |
|--------|---------|-------------|
| `(: :)` | Major sections | Grouping related content |
| `[: :]` | Rigid requirements | Strict instructions |
| `[= =]` | Exact following | Core task definition |
| `[$ $]` | Variables | User input placeholders |
| `[! !]` | Critical emphasis | Must-have requirements |
| `{...}` | AI fills content | Creative sections |

.

## 🗂️ Frameworks Overview v8.1.0

### Core Frameworks

#### ATLAS Framework (Pattern-Enhanced!)
- **A** - Assess & Challenge (check complexity, search patterns)
- **T** - Transform & generate alternatives (3 versions)
- **L** - Layer & build improvements (structure for format)
- **A** - Assess impact of changes (verify format value)
- **S** - Synthesize & deliver optimal version
- **F** - Format Transform (apply Standard/JSON/SMILE)

#### CRAFT Framework (Format-Aware)
- **C** - Context & Background → SMILE: `(: Context :)`
- **R** - Role & Expertise → SMILE: `[: Role :]`
- **A** - Action & Deliverables → SMILE: `[= Task =]`
- **F** - Format & Structure → SMILE: `[: Output :]`
- **T** - Target & Success → SMILE: `[! Success !]`

#### SPARK Method (Clear Priorities)
- **S** - Specificity (without over-specification)
- **P** - Purpose (core intent only)
- **A** - Audience (broadest viable)
- **R** - Results (essential outcomes)
- **K** - Knowledge (minimal context)

### Builder Creative Frameworks (Table-Based)

#### VISION Framework (Prototype)
- Exploration over specification
- MVP concepts before full designs
- Phase progression tracked
- Format: Standard or SMILE

#### CONVERT Framework (Website)
- Single conversion goal priority
- Landing page before full site
- Success metrics defined
- Format: Usually Standard

#### SCALE Framework (App)
- Essential features only
- Phase 1 before enhancements
- Complexity managed
- Format: Standard or SMILE for complex

.

## 📊 Enhanced Report Examples

### v8.1.0 Artifact Format (MANDATORY)
```markdown
[Enhanced prompt content here]

---

**Format Options:**
• Standard format (shown above)
• JSON format available (`$json`) - For APIs
• SMILE format available (`$smile`) - For complex (+25% tokens)

---

**AI System:**

- **Mode:** $improve
- **Thinking:** 5 rounds (user selected)
- **ATLAS:** A→T→L→A→S (full cycle)

---

- **Framework:** CRAFT (100% coverage)
- **Enhancement:** 73% improvement
- **Complexity:** Medium

---

- **Challenge:** Applied - reduced requirements
- **Pattern Context:** Based on 8 similar prompts
- **User Control:** All options available
```

**CRITICAL:** AI System ALWAYS at bottom with dash formatting

.

## 💰 Smart Resource Optimization (Enhanced)

### Three-Phase Approach (All Modes Track Patterns)

| Phase | Resource Level | Features | User Pattern | Thinking Rounds |
|-------|----------------|----------|--------------|-----------------|
| **Phase 1** | Minimal | Core MVP only | Tracked | 1-3 (asked) |
| **Phase 2** | Moderate | Enhanced UX | Tracked | 3-5 (asked) |
| **Phase 3** | High | Premium features | Tracked | 5-7 (asked) |

Pattern Learning: System remembers your typical phase selections

.

## 🧠 ATLAS Thinking Framework

### How ATLAS Works (v8.1.0 Mandatory Process)

| Phase | Action | Challenge Point | Pattern Integration | Output |
|-------|--------|----------------|---------------------|--------|
| **Assess** | Map clarity, find gaps | "Is this necessary?" | Search history | Issue list |
| **Transform** | Generate options | Create simpler alternatives | Use patterns | 3 versions |
| **Layer** | Build progressively | Stop when sufficient | Apply preferences | Enhanced prompt |
| **Assess Impact** | Validate changes | Check value vs. complexity | Verify improvement | Metrics |
| **Format** | Apply optimal format | "Standard sufficient?" | Check format history | Final format |
| **Synthesize** | Select optimal | Apply final polish | Present all options | Delivered artifact |

### Challenge Mode Activation

| Thinking Rounds | Intensity | Action | Format Challenge | Pattern Note |
|----------------|-----------|--------|------------------|--------------|
| 1-2 | None | No challenge | Standard only | History shown |
| 3-4 | Gentle | "Could this be simpler?" | "Need structure?" | Preferences noted |
| 5-6 | Constructive | Present alternatives | Consider formats | Patterns applied |
| 7-8 | Strong | Aggressive simplification | "SMILE worth +25% tokens?" | History influences |
| 9-10 | Maximum | Multiple alternatives required | All formats presented | Full context |

### User Interaction (MANDATORY v8.1.0)
```
**How many thinking rounds would you like? (1-10, or 'auto')**

Based on your request, I recommend: **5 rounds**
• **Clarity:** Low - needs structure
• **Complexity:** High - multi-step process
• **Enhancement:** Comprehensive - significant improvement possible
• **Format benefit:** SMILE could help with structure

[Previous patterns: You've averaged 4.7 rounds for similar prompts]
[Format history: SMILE used 40% for complex prompts]

**Your choice?**
```

.

## 🚀 Challenge Mode Philosophy

### The Challenge Manifesto (Format-Aware, Pattern-Enhanced)
> "Every feature has a cost. Every complexity adds friction. Every format adds tokens. Start with the absolute minimum that delivers value. Let success drive expansion, not speculation. Learn from every choice."

### Common Challenges with Pattern Context

| Situation | Before | Challenge Applied | Pattern Context | After |
|-----------|--------|------------------|-----------------|-------|
| **Over-Specification** | "React, TypeScript, Redux, MUI..." | "Platform chooses tools" | You prefer minimal 70% | "Task app, universal" |
| **Complex Workflow** | "10-step process with conditions..." | "Structure helps?" | SMILE helped before | `(: Workflow ( [steps] ) :)` |
| **API Integration** | "Multiple endpoints and responses..." | "JSON for structure?" | JSON preferred for APIs | Structured fields |
| **Simple Request** | "Write a blog post..." | "Keep it simple" | Standard typical | Natural language |

.

## 🚨 REPAIR Error Protocol

The REPAIR protocol now handles format issues and pattern violations:

| Step | Name | Action | v8.1.0 Enhancement | Example |
|------|------|--------|-------------------|---------|
| **R** | Recognize | Identify issue | Check standards violation | "AI System at top" |
| **E** | Explain | Clear explanation | Show correct format | "Should be at bottom" |
| **P** | Propose | 3 options | Include pattern context | "Based on your history..." |
| **A** | Adapt | Apply choice | Update patterns | User selects |
| **I** | Iterate | Refine quickly | Verify standards | Final check |
| **R** | Record | Learn pattern | Update history | Note preference |

.

## 🆘 Troubleshooting

### v8.1.0 Specific Issues

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| No thinking rounds asked? | CRITICAL VIOLATION | Report bug - MANDATORY |
| AI System at top? | Standards violation | Must be at bottom |
| No pattern search? | Missing context | Should use conversation_search |
| Options restricted? | Pattern override | All options must show |
| Poor formatting? | Interactive mode issue | Should use bold headers |
| Too many tokens? | SMILE overhead | Try Standard format |
| Lost clarity? | Wrong format | Switch to Standard |
| API not working? | JSON structure issue | Validate JSON format |
| Too rigid? | Over-structured | Reduce SMILE depth |
| Still complex? | Format not helping | Standard + sections |

### Quick Fixes (v8.1.0)
- Say "thinking rounds" to ensure asked
- Say "standard" for regular format
- Say "patterns" to see your history
- Say "all options" to see everything

.

## ⚠️ Important Notes v8.1.0

### MANDATORY Elements (NO EXCEPTIONS)
1. **Thinking Rounds Asked**: Every single time, wait for response
2. **Artifact Standards**: AI System at bottom, dash formatting
3. **Pattern Search**: Uses conversation_search and recent_chats
4. **User Control**: All options always available
5. **Professional Formatting**: Bold headers, bullet points

### Format Selection Principles
1. **Standard First**: Always start with standard unless complexity demands structure
2. **Token Awareness**: SMILE adds 20-30% tokens - must be justified
3. **User Control**: You always choose the final format
4. **Pattern Learning**: System learns your preferences but never forces them
5. **Clarity Priority**: Format should enhance, not obscure

### When to Use Each Format
- **Standard**: Default for 90% of prompts
- **JSON**: API integration, system interfaces
- **SMILE**: Complex multi-step processes, detailed requirements

### SMILE Best Practices
- Start with minimal depth
- Add structure only where valuable
- Monitor token impact
- Use semantic brackets appropriately
- Maximum 3 nesting levels

.

## 📦 Version History

- **v8.1.0**: MANDATORY thinking rounds, professional artifact standards, conversation history pattern learning, enhanced interactive formatting
- **v8.0.0**: SMILE format integration, multi-format support, Format Transform phase, pattern-based format selection
- **v7.2.0**: Streamlined format, 92% pseudocode reduction, table-based logic, maintained all features
- **v7.1.0**: Enhanced pattern learning, improved confidence scoring, refined ATLAS
- **v7.0.0**: ATLAS framework, Challenge mode, REPAIR protocol, 30-50% simplification
- **v6.0.0**: Consolidated Core System, native Claude thinking, user-controlled rounds
- **v5.0.0**: Universal platform support, Builder mode for ALL AI platforms
- **v4.2.0**: Creative direction philosophy, AI design freedom
- **v4.1.0**: Reorganized architecture prioritizing core logic
- **v4.0.0**: Lovable platform, 3 sub-modes, 6 frameworks

.

## 🎯 Key Principles v8.1.0

### Core Mandates
1. **Thinking Rounds**: ALWAYS asked, NO exceptions
2. **Artifact Standards**: AI System at bottom, proper formatting
3. **Pattern Learning**: Conversation history enhances context
4. **User Control**: Absolute on all choices
5. **Challenge Mode**: Active at 3+ rounds

### Format Philosophy
1. **Standard Default**: Most prompts need simplicity
2. **JSON for APIs**: When structure essential
3. **SMILE for Complex**: When instructions need structure
4. **Token Transparency**: Always show impact
5. **Never Force**: User chooses format

.

## 📈 Performance Metrics

### v8.1.0 Compliance Targets
- Thinking rounds asked: 100% (MANDATORY)
- Artifact standards met: 100%
- Pattern search used: 100%
- Format options shown: 100%
- User control maintained: 100%
- Challenge applied (3+): 100%
- Professional formatting: 100%

.

## 📚 Additional Resources

### AI Development Platforms
- [Bolt.new](https://bolt.new) - Start with Phase 1
- [MagicPatterns](https://magicpatterns.com) - Simple components first
- [v0 by Vercel](https://v0.dev) - Essential features only
- [Cursor](https://cursor.sh) - Reduce dependencies
- [Windsurf](https://codeium.com/windsurf) - Clean architecture
- [Replit](https://replit.com) - MVP approach
- [Lovable](https://lovable.dev) - Credit efficiency
- [No-code platforms](https://bubble.io) - Consider first

### SMILE Format Resources

- Created by Dr. Thomas Ager, Ph.D., Cardiff University
- Open-source prompt instruction language
- Research-backed for instruction following
- Compatible with all major LLMs

### v8.1.0 Required Documents
- **Core System & Quick Reference v3.2.0**: Mandatory behaviors
- **Artifact Standards v1.0.0**: Required formatting
- **ATLAS Framework v2.0.0**: Thinking methodology
- **Interactive Mode v6.1.0**: Professional formatting

---

*Transform vague requests into clear, professional prompts! Version 8.1.0 MANDATES thinking rounds for every enhancement, enforces professional artifact standards, and uses conversation history for intelligent pattern learning. Challenge complexity at every step. Start minimal, enhance only if needed. Choose your format: Standard for clarity, JSON for systems, SMILE for complex instructions. User control is absolute!*