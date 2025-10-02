# Prompt Engineering Assistant - User Guide v0.860

Transforms vague requests into clear, effective AI prompts through intelligent framework selection, quality evaluation, and automatic optimization with DEPTH processing.

## 📋 Table of Contents

- [🆕 What's New In V0.860](#whats-new-in-v0860)
- [🔧 What's Improved](#whats-improved)
- [✨ Key Features](#key-features)
- [🚀 Quick Setup](#quick-setup)
- [🎛️ Operating Modes](#operating-modes)
- [🔄 Output Formats](#output-formats)
- [🧠 DEPTH Thinking Framework](#depth-thinking-framework)
- [🎯 Automatic Complexity Detection](#automatic-complexity-detection)
- [⭐ RCAF Framework](#rcaf-framework)
- [✅ CLEAR Evaluation System](#clear-evaluation-system)
- [📊 Header Format](#header-format)
- [🆘 Troubleshooting](#troubleshooting)
- [📦 Version History](#version-history)

---

<a id="whats-new-in-v0860"></a>
## 🆕 What's New In V0.860

### Major System Updates
- **Interactive Mode Enhanced:** Improved conversational flow with clearer decision points
- **Bug Fixes Applied:** Resolved various logic issues for more reliable performance
- **UX Improvements:** Cleaner interface with simpler messages and smoother interactions
- **Smart Quick Mode:** Auto-scales processing rounds (1-5) based on complexity

### Enhanced Processing
- **Automatic DEPTH:** 10-round comprehensive analysis for standard modes
- **Quick Mode Scaling:** Intelligent 1-5 round processing based on complexity
- **Silent Excellence:** All optimization happens invisibly behind simple messages
- **Better Defaults:** Smarter automatic framework and format selections

### Updated Files
- **Writer:** v0.860 - Core system with improved logic
- **DEPTH Framework:** v0.102 - Silent processing methodology
- **Interactive Mode:** v0.632 - Enhanced conversation patterns
- **Artifact Standards:** v0.119 - Minimal header format
- **Patterns & Enhancements:** v0.612 - Framework templates
- **Evaluation & Refinement:** v0.612 - CLEAR scoring system

---

<a id="whats-improved"></a>
## 🔧 What's Improved

### Interactive Mode Enhancements ✅
**Better Flow:**
- Single comprehensive question when complexity requires choice
- Clearer framework selection at complexity 5-6
- Automatic simplification offer at complexity 7+
- Reduced unnecessary questions

**Smarter Decisions:**
- Framework choice only when beneficial (complexity 5-6)
- Output structure always offered (Standard/JSON/YAML)
- Challenge mode activates automatically at high complexity
- Session pattern learning within conversation

### Quick Mode Intelligence ✅
**Auto-Scaled Processing:**
- Complexity 1-2: 1-2 rounds (minimal)
- Complexity 3-4: 3 rounds (moderate)
- Complexity 5-6: 4 rounds (substantial)
- Complexity 7+: 5 rounds (comprehensive)

### System Simplification ✅
**Cleaner Operation:**
- Removed deprecated features
- Consolidated processing logic
- Unified error handling
- Better separation of concerns

---

<a id="key-features"></a>
## ✨ Key Features

- **🚀 Seven Modes**: Interactive (default), Short, Improve, Refine, Quick, JSON, YAML
- **🧠 DEPTH Framework**: 5-phase methodology with automatic processing
- **🎯 Smart Complexity**: Automatic detection and framework scaling
- **⚡ Quick Mode**: Fast processing with auto-scaled depth (1-5 rounds)
- **💬 Interactive Default**: Guided enhancement with smart questions
- **🤖 Automatic Processing**: System-controlled optimization (no user choice)
- **📊 Header at Top**: Single-line metadata with $ prefix
- **📝 Output Constraints**: Enhanced prompt matches exact request
- **📦 Minimal Artifacts**: Header + content only, no extra sections

---

<a id="quick-setup"></a>
## 🚀 Quick Setup

### Step 1: Create A Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Create new project named "Prompt Engineering Assistant"

### Step 2: Add System Instructions
1. Click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Prompt Improver - v0.860.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these documents to your project:

**Core Documents (Current Versions):**
- `Prompt - DEPTH Thinking Framework - v0.102.md`
- `Prompt - Interactive Mode - v0.632.md`
- `Prompt - Artifact Standards & Templates - v0.119.md`

**Enhancement Documents:**
- `Prompt - Patterns & Enhancements - v0.612.md`
- `Prompt - Evaluation & Refinement - v0.612.md`

**Format Guides:**
- `Prompt - JSON Format Guide.md`
- `Prompt - YAML Format Guide.md`

### Step 4: Start Enhancing
```
analyze customer data            # Interactive discovery flow
$quick fix grammar              # Immediate enhancement (1-5 rounds auto)
$improve generate insights      # Standard enhancement (10 rounds auto)
$json api endpoint              # JSON format with full processing
```

---

<a id="operating-modes"></a>
## 🎛️ Operating Modes

**Default Mode:** The system defaults to `interactive` unless a command is specified.

| Mode | Command | Purpose | DEPTH Processing | Output Format | Speed |
|------|---------|---------|------------------|---------------|-------|
| **Interactive** | (default) | Guided enhancement | 10 rounds auto | User choice | Standard |
| **$short** | `$short`/`$s` | Minimal refinement | 3 rounds quick | User choice | Fast |
| **$improve** | `$improve`/`$i` | Standard enhancement | 10 rounds auto | User choice | Standard |
| **$refine** | `$refine`/`$r` | Maximum optimization | 10 rounds auto | User choice | Thorough |
| **$quick** | `$quick`/`$q` | Fast processing | 1-5 auto-scaled | Auto-selected | Very Fast |
| **$json** | `$json`/`$j` | API format | 10 rounds auto | JSON preset | Standard |
| **$yaml** | `$yaml`/`$y` | Config format | 10 rounds auto | YAML preset | Standard |

### Interactive Flow (Default) - Smart Questions
```
Welcome! I'll help enhance your prompt for maximum effectiveness. 🎯

Please share:
- Your current prompt, or
- What you need the AI to do

[SYSTEM ANALYZES COMPLEXITY]

[IF COMPLEXITY 5-6:]
Framework Selection Available:

Option A: RCAF (Recommended)
✓ 4 essential elements
✓ Better clarity score

Option B: CRAFT
✓ 5 comprehensive elements
✓ More complete coverage

Which framework? (A or B)

[THEN ALWAYS:]
Output Structure Selection:
1. Standard - Natural language
2. JSON - Structured data
3. YAML - Configuration structure

Your choice? (1, 2, or 3)
```

---

<a id="output-formats"></a>
## 🔄 Output Formats

### Three Format System
| Format | Best For | Token Impact | CLEAR Average | Symbol |
|--------|----------|--------------|---------------|---------|
| **Standard** | Natural language, clarity | Baseline | 43/50 | 📝 |
| **JSON** | API integration, structured | +5-10% | 41/50 | 🔧 |
| **YAML** | Templates, configuration | +3-7% | 42/50 | ⚙️ |

### Format Selection Matrix
| Use Case | Recommended Format | Reasoning |
|----------|-------------------|-----------|
| Human interaction | Standard | Maximum clarity |
| API endpoints | JSON | Machine-parseable |
| Config files | YAML | Human-editable |
| Templates | YAML | Easy customization |
| Documentation | Standard | Readability |

---

<a id="depth-thinking-framework"></a>
## 🧠 DEPTH Thinking Framework

### Automatic DEPTH Processing System
| Mode | Processing Depth | User Choice | Application | Output |
|------|-----------------|-------------|-------------|---------|
| **Standard Modes** | 10 rounds enforced | None | Automatic | Enhanced prompt |
| **$quick Mode** | 1-5 auto-scaled | None | Complexity-based | Enhanced prompt |

**DEPTH Definition:**
DEPTH methodology (Discover, Engineer, Prototype, Test, Harmonize) automatically optimizes every prompt while maintaining exact scope.

### DEPTH Phases (Applied Silently)
| Phase | Purpose | Internal Process | User Sees |
|-------|---------|------------------|-----------|
| **D**iscover | Requirements analysis | Multiple perspectives on SAME prompt | "🎯 Analyzing your request..." |
| **E**ngineer | Framework application | Optimal structure for SAME prompt | "• Optimizing structure" |
| **P**rototype | Build enhancement | Create exact enhancement | "• Enhancing clarity" |
| **T**est | Quality validation | CLEAR scoring (target 40+/50) | "• Building framework" |
| **H**armonize | Final polish | Excellence for output | Polished artifact |

### Quick Mode Scaling
```markdown
Complexity Detection → Auto-Scale Rounds:
- Simple (1-2): 1-2 rounds → 38/50 CLEAR
- Low (3-4): 3 rounds → 40/50 CLEAR
- Medium (5-6): 4 rounds → 41/50 CLEAR
- High (7+): 5 rounds → 40/50 CLEAR
```

---

<a id="automatic-complexity-detection"></a>
## 🎯 Automatic Complexity Detection

### For Prompt Enhancement
| Indicators | Complexity | Framework | User Choice | DEPTH | Output |
|------------|------------|-----------|-------------|-------|---------|
| fix, improve, clarify | **Simple (1-4)** | RCAF auto | Format only | 10 rounds (1-2 if $quick) | Enhanced prompt |
| analyze, create, generate | **Moderate (5-6)** | User choice | Framework + Format | 10 rounds (4 if $quick) | Enhanced prompt |
| comprehensive, system, platform | **High (7+)** | Challenge offered | Simplify option + Format | 10 rounds (5 if $quick) | Enhanced prompt |

### Framework Selection Logic
System automatically determines optimal approach:
- Simple requests → RCAF framework automatic
- Moderate complexity → Offers RCAF vs CRAFT choice
- High complexity → Suggests streamlined vs comprehensive
- Defaults to RCAF when unclear (70% of cases)

### Output Guarantee Examples
```
User: "write about dogs"
→ RCAF framework for THAT dog content only
NOT: Multiple prompts about animals

User: "analyze customer data"
→ Enhanced prompt for THAT analysis only
NOT: Extra analysis features

User: "comprehensive platform system"
→ Challenge mode for THAT system only
NOT: Multiple system prompts
```

---

<a id="rcaf-framework"></a>
## ⭐ RCAF Framework

### The Essential Four Elements
**Primary framework for 70% of prompts - maximum clarity with minimum complexity**

| Element | Symbol | Purpose | Example |
|---------|--------|---------|---------|
| **Role** | 👤 | Specific expertise | "Data analyst with visualization expertise" |
| **Context** | 🌍 | Essential background | "Q4 2024 sales data, 100K transactions" |
| **Action** | 🎯 | Clear, measurable task | "Identify top 3 revenue drivers" |
| **Format** | 📋 | Output requirements | "Executive dashboard with insights" |

### RCAF vs CRAFT Decision
| Complexity | Framework | Elements | When to Use |
|------------|-----------|----------|-------------|
| **1-4** | RCAF | 4 | Automatic selection |
| **5-6** | User choice | 4 or 5 | Based on preference |
| **7+** | Challenge mode | 4 (streamlined) or 5 (comprehensive) | Simplification offered |

### Example Transformation
```markdown
Before (Vague):
"analyze the data"
CLEAR Score: 20/50

After (RCAF Enhanced):
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

Role: Business analyst with predictive modeling expertise.
Context: Q4 2024 performance data across all departments.
Action: Identify top 3 growth opportunities and predict Q1 2025 trends.
Format: Executive presentation with 5 key insights and actionable recommendations.

Improvement: +23 points (115% gain)
```

---

<a id="clear-evaluation-system"></a>
## ✅ CLEAR Evaluation System

### Five Dimensions of Quality
Every prompt automatically scored on these dimensions (1-10 points each):

| Dimension | Focus | Target | Measures |
|-----------|-------|--------|----------|
| **C**orrectness | Accuracy | 8+/10 | Requirements captured correctly |
| **L**ogic/Coverage | Completeness | 8+/10 | All aspects addressed |
| **E**xpression | Clarity | 9+/10 | How clearly expressed |
| **A**rrangement | Structure | 8+/10 | Organization quality |
| **R**euse | Adaptability | 7+/10 | Template potential |

### CLEAR Grade Scale
| Score | Grade | Action | Processing |
|-------|-------|--------|------------|
| **45-50** | A+ | Ship immediately | Minimal polish |
| **40-44** | A | Minor improvements | Standard target |
| **35-39** | B | Enhance weak areas | Focus on low scores |
| **30-34** | C | Switch to RCAF | Framework change |
| **<30** | D/F | Complete rewrite | Full restructure |

---

<a id="header-format"></a>
## 📊 Header Format

### Artifact Delivery Standard
**Every artifact has exactly:**
```
Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50

[Enhanced prompt content]
```

### Header Components
| Component | Format | Example | Required |
|-----------|--------|---------|----------|
| **Mode** | `$[command]` | `$improve` | Yes |
| **Complexity** | Low/Medium/High | `Medium` | Yes |
| **Framework** | RCAF or CRAFT | `RCAF` | Yes |
| **CLEAR** | Score/50 | `43/50` | Yes |

### What's NOT Included
- ❌ Format Options section
- ❌ CLEAR breakdown details
- ❌ Processing methodology
- ❌ Extra dividers
- ❌ Additional metadata

---

<a id="troubleshooting"></a>
## 🆘 Troubleshooting

### Common Issues & Solutions
| Issue | Solution | Prevention |
|-------|----------|------------|
| Unclear request | System asks for clarification | Provide complete context |
| High complexity | Challenge mode offers simplification | Accept streamlined option |
| Wrong format | Specify format command ($json, $yaml) | Use format modes directly |
| Too verbose | Switch to RCAF framework | Choose Option A when offered |

### Error Recovery (REPAIR)
- **R**ecognize - Detect issue automatically
- **E**xplain - Simple message to user
- **P**ropose - Offer solution
- **A**dapt - Apply fix silently
- **I**terate - Verify quality
- **R**ecord - Learn for session

---

<a id="version-history"></a>
## 📦 Version History

### v0.860 (Current)
- Enhanced interactive mode flow
- Smart quick mode scaling (1-5 rounds)
- Bug fixes and logic improvements
- Better UX with cleaner messages

### v0.850
- Automatic DEPTH processing
- Silent excellence implementation
- Framework selection at complexity 5-6
- Challenge mode at complexity 7+

### Future Roadmap
- Additional format options
- Enhanced pattern library
- Improved session learning
- Extended framework support

---

## 🎯 Quick Command Reference

### Standard Commands
```markdown
[request]            # Interactive mode with guided questions
$improve [request]   # Standard enhancement with RCAF
$refine [request]    # Maximum optimization
$short [request]     # Minimal quick enhancement
```

### Speed Command
```markdown
$quick [request]     # Immediate enhancement, 1-5 rounds auto-scaled
```

### Format Commands
```markdown
$json [request]      # JSON structure output
$yaml [request]      # YAML configuration output
```

---

## 📚 Core Principles Summary

### DEPTH Processing Guarantee
```
User Request: "analyze customer data"
↓
Internal DEPTH Analysis:
- 5 perspectives analyze SAME data task
- Framework optimized for SAME analysis
- Quality enhanced for SAME requirement
↓
Output: ONE enhanced prompt
- Exactly what user requested
- No additional features
- Perfect RCAF format
- CLEAR score 40+/50
```

### Best Practices
- Use interactive mode for guidance
- Trust automatic complexity detection
- Accept framework recommendations
- Let system handle DEPTH silently
- Expect exact enhancement of request