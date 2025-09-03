# Prompt Engineering Assistant - User Guide v8.0.0

A comprehensive system that transforms vague requests into clear, effective AI prompts using the ATLAS thinking framework, challenge-based simplification, and intelligent refinement. Now with SMILE format support for better instruction following! Features 8 operating modes including 3 specialized Builder sub-modes for creating universal creative briefs that work on ANY AI development platform while aggressively minimizing complexity and resource usage.

## 📑 Table of Contents

- [🆕 What's New in v8.0.0](#-whats-new-in-v800)
- [📖 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🎛️ Operating Modes](#️-operating-modes)
  - [Core Modes](#core-modes)
  - [Builder Sub-Modes](#builder-sub-modes-universal-ai-platform-support)
  - [Supported Platforms](#supported-platforms-include)
- [🔄 Format Options](#-format-options-new)
  - [Standard Format](#standard-format-default)
  - [JSON Format](#json-format)
  - [SMILE Format](#smile-format)
- [🗂️ Frameworks Overview](#️-frameworks-overview-v800)
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
- [⚠️ Important Notes](#️-important-notes-v800)
- [📦 Version History](#-version-history)
- [🎯 Key Principles](#-key-principles-v800)
- [📈 Performance Metrics](#-performance-metrics)
- [📚 Additional Resources](#-additional-resources)

.

## 🆕 What's New in v8.0.0

### SMILE Format Integration 🙂
- **New Format Option**: SMILE ((: format) - Emoticon-structured prompts for better instruction following
- **Multi-Format Support**: Every enhancement now available in Standard, JSON, and SMILE formats
- **Intelligent Format Selection**: System recommends optimal format based on complexity
- **Token Transparency**: Always shows token impact for SMILE format (+20-30% typical)
- **Pattern Learning**: Tracks your format preferences and adapts recommendations

### SMILE Format Features
- **Better Instruction Following**: Research suggests improved LLM compliance
- **Structured Clarity**: Uses emoticon brackets for semantic organization
- **Complexity Handling**: Excellent for multi-step, complex instructions
- **Optional Always**: Never forced - Standard format always available
- **Depth Control**: Minimal/Moderate/Heavy structure based on needs

### Format Transform Phase
- **New ATLAS Phase**: F - Format Transform (optional post-enhancement)
- **Automatic Assessment**: Evaluates which format(s) add value
- **User Choice**: Always presents options, never forces format
- **Pattern Tracking**: Learns your format preferences over time

### Continuing Excellence from v7.2.0
- **92% Reduction in Pseudocode**: Clean, readable documentation
- **Table-Based Logic**: Complex decisions now visual
- **ATLAS Framework**: Universal 5-phase methodology
- **Challenge Mode**: Automatic complexity challenges
- **Smart Defaults**: 60% fewer questions
- **Pattern Learning**: Now includes format preferences

.

## 📖 Overview

The Prompt Engineering Assistant helps users craft powerful, precise prompts through systematic simplification and challenge-based thinking. Version 8.0.0 introduces SMILE format support - an emoticon-based structure that can improve instruction following for complex prompts. The system actively questions complexity while delivering professional-grade prompts that maximize clarity, minimize unnecessary specifications, and now offers multiple format options to suit different use cases.

### What is SMILE Format?
SMILE ((: Smile) is an open-source prompt instruction language created by Dr. Thomas Ager, Ph.D. at Cardiff University. It uses emoticon-based brackets to structure prompts for Large Language Models, designed to increase instruction following while maintaining readability.

.

## ✨ Key Features

### Core Capabilities
- **Multi-Format Output**: Standard, JSON, and SMILE formats
- **ATLAS Thinking Framework**: 5-phase systematic enhancement + Format Transform
- **Challenge Mode**: Automatic at 3+ rounds - "Could this be simpler?"
- **Smart Defaults**: Reduces questions by 60%
- **Pattern Learning**: Adapts to preferences including format choices
- **REPAIR Protocol**: Recognize, Explain, Propose, Adapt, Iterate, Record
- **30-50% Complexity Reduction**: Measurable simplification
- **Universal Platform Support**: Works on ALL AI platforms
- **User-Controlled Depth**: Choose 1-10 thinking rounds or 'auto'

### v8.0.0 Format Enhancements
- **Format Intelligence**: Recommends best format for your use case
- **Token Impact Display**: Shows overhead for each format
- **Format Conversion**: Can transform between formats
- **Pattern-Based Selection**: Learns your format preferences
- **Always Optional**: Standard format always available

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Prompt Engineering Assistant v8"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Prompt Improver - v8.0.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these v8.0.0 documents to your project's knowledge base:
- `Prompt - ATLAS Thinking Framework - v2.0.0.md` (Now with Format Transform)
- `Prompt - Core System & Quick Reference - v3.0.0.md` (SMILE definitions)
- `Prompt - Builder Mode.md` (Table-based platform guide)
- `Prompt - Evaluation & Refinement - v6.0.0.md` (Format assessment)
- `Prompt - Interactive Mode - v6.0.0.md` (Format selection phase)
- `Prompt - Patterns & Enhancements - v6.0.0.md` (Multi-format templates)

### Step 4: Start Creating with Format Options
Simply paste your prompt or describe what you need:
```
write about dogs                       # Standard format by default
$improve analyze customer data         # Offers format options
$smile create complex workflow         # SMILE format primary
$json api integration specs           # JSON format primary
$interactive                          # Guides to best format
$prototype explore dashboard concepts # Standard or SMILE
```

.

## 🎛️ Operating Modes

### Core Modes

| Mode | Activation | Purpose | Best For | Challenge Focus | Format Support |
|------|------------|---------|----------|-----------------|----------------|
| **$short** | `$short` or `$s` | Quick minimal refinement | Simple clarity | "Even this needed?" | Standard only |
| **$improve** | `$improve` or `$i` (DEFAULT) | Smart enhancement | Most improvements | Balance completeness | All formats |
| **$refine** | `$refine` or `$r` | Full optimization | Maximum quality | Multiple alternatives | All formats |
| **$interactive** | `$interactive` | Guided help | Learning | Smart defaults | User choice |
| **$json** | `$json` or `$j` | API format | Programmatic | Minimize overhead | JSON primary |
| **$smile** | `$smile` or `$sm` | SMILE format | Complex instructions | Structure necessity | SMILE primary |

### Builder Sub-Modes (Universal AI Platform Support!)

| Sub-Mode | Activation | Purpose | Challenge Priority | Default Phase | Format Options |
|----------|------------|---------|-------------------|---------------|----------------|
| **Builder** | `$builder` | Auto-detect needs | "Simpler platform?" | Phase 1 only | Standard/SMILE |
| **Prototype** | `$prototype` | Visual exploration | "Paper prototype?" | MVP exploration | Standard/SMILE |
| **Website** | `$website` | Conversion sites | "Landing page first?" | Core message | Standard |
| **App** | `$app` | Applications | "Which features critical?" | Essential only | Standard/SMILE |

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

## 🔄 Format Options (NEW!)

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

### Format Selection Guide

| Complexity | Recommended | Alternative | Token Note |
|------------|------------|-------------|------------|
| Simple (1-3) | Standard | - | Baseline |
| Moderate (4-6) | Standard | JSON if API, SMILE if structured | Monitor overhead |
| Complex (7-10) | SMILE | Standard with sections | +20-30% justified |

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

## 🗂️ Frameworks Overview v8.0.0

### Core Frameworks

#### ATLAS Framework (Now with Format Transform!)
- **A** - Assess & Challenge (check complexity, format needs)
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


## 🧠 ATLAS Thinking Framework

### How ATLAS Works with Formats

| Phase | Action | Challenge Point | Format Decision | Output |
|-------|--------|----------------|-----------------|--------|
| **Assess** | Map clarity, find gaps | "Is this necessary?" | Complexity check | Issue list |
| **Transform** | Generate options | Create simpler alternatives | Consider formats | 3 versions |
| **Layer** | Build progressively | Stop when sufficient | Structure for format | Enhanced prompt |
| **Assess Impact** | Validate changes | Check value vs. complexity | Verify format value | Metrics |
| **Format** | Apply optimal format | "Standard sufficient?" | User choice | Final format |
| **Synthesize** | Select optimal | Apply final polish | Present options | Delivered artifact |

### Challenge Mode Activation

| Thinking Rounds | Intensity | Action | Format Challenge |
|----------------|-----------|--------|------------------|
| 1-2 | None | No challenge | Standard only |
| 3-4 | Gentle | "Could this be simpler?" | "Need structure?" |
| 5-6 | Constructive | Present alternatives | Consider formats |
| 7-8 | Strong | Aggressive simplification | "SMILE worth +25% tokens?" |
| 9-10 | Maximum | Multiple alternatives required | All formats presented |

### User Interaction with Format
```
How many thinking rounds would you like? (1-10, or 'auto')

Based on your request, I recommend: 5 rounds
- Clarity: Low - needs structure
- Complexity: High - multi-step process
- Enhancement: Comprehensive - significant improvement possible
- Format benefit: SMILE could help with structure

Or specify your preferred number.
[Pattern: You've used SMILE 40% for complex prompts]
```

.

## 🚀 Challenge Mode Philosophy

### The Challenge Manifesto (Format-Aware)
> "Every feature has a cost. Every complexity adds friction. Every format adds tokens. Start with the absolute minimum that delivers value. Let success drive expansion, not speculation."

### Common Challenges with Format Considerations

| Situation | Before | Challenge Applied | Format Choice | After |
|-----------|--------|------------------|---------------|-------|
| **Over-Specification** | "React, TypeScript, Redux, MUI..." | "Platform chooses tools" | Standard | "Task app, universal" |
| **Complex Workflow** | "10-step process with conditions..." | "Structure helps?" | SMILE | `(: Workflow ( [steps] ) :)` |
| **API Integration** | "Multiple endpoints and responses..." | "JSON for structure?" | JSON | Structured fields |
| **Simple Request** | "Write a blog post..." | "Keep it simple" | Standard | Natural language |

.

## 🚨 REPAIR Error Protocol

The REPAIR protocol now handles format issues:

| Step | Name | Action | Format Handling | Example |
|------|------|--------|-----------------|---------|
| **R** | Recognize | Identify issue | Check format fit | "SMILE too complex" |
| **E** | Explain | Clear explanation | Token impact shown | "+35% overhead detected" |
| **P** | Propose | 3 options | Include format change | Standard/Simplified/Different |
| **A** | Adapt | Apply choice | Switch if needed | User selects format |
| **I** | Iterate | Refine quickly | Optimize for format | Final adjustments |
| **R** | Record | Learn pattern | Track format preference | Note for future |

.

## 🆘 Troubleshooting

### Format-Related Solutions

| Issue | Diagnosis | Solution |
|-------|-----------|----------|
| Too many tokens? | SMILE overhead | Try Standard format |
| Lost clarity? | Wrong format | Switch to Standard |
| API not working? | JSON structure issue | Validate JSON format |
| Too rigid? | Over-structured | Reduce SMILE depth |
| Still complex? | Format not helping | Standard + sections |

### Quick Format Fixes
- Say "standard" for regular format
- Say "smile" for structured format
- Say "json" for API format
- Say "compare" to see all formats

.

## ⚠️ Important Notes v8.0.0

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

---

*Transform vague requests into clear, simple prompts with format options! Version 8.0.0 adds SMILE format support for better instruction following when complexity demands it. Challenge complexity at every step. Start minimal, enhance only if needed. Choose your format: Standard for clarity, JSON for systems, SMILE for complex instructions. Tables + ATLAS + Challenge mode + Format options = Better prompts, faster, in the right format!*