# IDE System Prompt - User Guide v3.9.0

Transform any AI coding assistant into an elite software engineer who fixes root causes, not symptoms.

## 🚀 What is This?

IDE System Prompt is a comprehensive set of rules that elevates AI coding assistants in your IDE from helpful tools to elite engineering partners. It enforces production-grade standards, eliminates technical debt, and integrates advanced reasoning through MCP tools.

**Key Benefits:**
- Transform IDE AI assistants into elite software engineers
- Get production-ready code with zero technical debt on first try
- Fix root causes instead of patching symptoms
- Enforce CSS-first performance optimization automatically
- Scale from simple fixes to complex architecture decisions
- Works in Cursor, Windsurf, Claude Code, VS Code, and more

**Key Principle:** Fix the root cause, not the symptom. Every line of code should be production-grade.

.

## 🆕 What's New in v2.0.0

- **MCP Integration**: Sequential Thinking for systematic analysis in IDEs
- **Enhanced Workflow**: Think first, validate with tools, then code
- **Performance Rules**: CSS-first approach with REM units only
- **Modular Rules**: Toggle specific behaviors per task
- **IDE-Optimized**: Works across all major AI-enabled IDEs

.

## Overview

Most AI coding assistants generate "good enough" code that accumulates technical debt over time. They fix symptoms instead of root causes, leading to fragile applications that break with each change.

The IDE System Prompt transforms this approach entirely. By enforcing 11 core engineering principles directly in your IDE, it ensures your AI assistant thinks like a senior engineer: analyzing root causes, optimizing performance relentlessly, and delivering production-grade code from the start. Whether you're building with Webflow + Miyagi (https://www.getmiyagi.com) or any modern stack, these rules create an AI partner that maintains the standards of elite engineering teams.

The integration with MCP (Model Context Protocol) tools takes this further, adding systematic reasoning validation right in your development environment. It's not just about writing code; it's about engineering solutions that scale.

## ✨ Key Features

- **Elite Engineering Standards**: DRY, KISS principles with production-grade output
- **MCP Tool Integration**: Sequential thinking and validation in your IDE
- **Performance Optimization**: CSS-first approach, zero unnecessary JavaScript
- **Risk Management**: Document what could break before it does
- **Phased Development**: Strategic planning before tactical execution
- **Framework Flexibility**: Optimized for Webflow + Miyagi, adaptable to any stack
- **Modular Rule System**: Enable/disable specific behaviors per task

.

## 🚀 Quick Setup

### Step 1: Choose Your IDE

**Supported IDEs:**
- **Cursor** (Recommended): Settings → Project Rules
- **Windsurf**: Settings → AI Rules
- **Claude Code**: Create `claude.md` in project root
- **VS Code with AI**: Create `.vscode/ai-rules.md`
- **JetBrains IDEs**: Create `.idea/ai-assistant.md`
- **Generic**: Create `AI_RULES.md` in project root

### Step 2: Add Rules (Modular Approach)

For Cursor/Windsurf, add each section as a separate rule:
1. **Rule 1**: "Objective" - Elite engineering standards
2. **Rule 2**: "Principles" - DRY, KISS, CSS-first
3. **Rule 3**: "Reasoning" - Evidence-based solutions
4. **Rule 4**: "MCP Tool Usage" - Validation workflow
5. **Rule 5**: "Pre-Code Check" - Scope definition
6. **Rule 6**: "Risk Management" - Breakage prevention
7. **Rule 7**: "Dev Planning" - Phased approach
8. **Rule 8**: "Communication" - Clear rationale
9. **Rule 9**: "Libraries" - Preferred tools
10. **Rule 10**: "Tech Execution" - Framework specifics
11. **Rule 11**: "MCP Workflow" - Tool decision tree

### Step 3: Configure MCP Tools (Optional but Recommended)

See [Installing MCP Tools](#installing-mcp-tools-recommended) section below.

### Step 4: Verify Setup

Test with a simple request in your IDE:
```
"Analyze this code for performance issues and suggest improvements"
```

The AI should follow the systematic approach, using MCP tools if available.

.

## 🎯 How to Use

### Basic Usage

Simply write your development request in your IDE. The AI will:
1. Analyze the problem systematically
2. Use MCP tools to validate approach (if available)
3. Define scope before coding
4. Deliver production-grade solution
5. Document risks and considerations

### Rule Toggling (Cursor/Windsurf)

Enable/disable rules based on your needs:
- **Quick prototype**: Disable "Risk Management" and "MCP Workflow"
- **Performance critical**: Enable all optimization rules
- **Learning mode**: Enable "Communication" for detailed explanations
- **Production deploy**: Enable all rules for maximum quality

### Example Workflows

**Example 1: Performance Optimization**
```
"This animation is janky on mobile. Fix it."
```
Result: AI analyzes root cause, converts to CSS-only solution, documents performance gains

**Example 2: Complex Feature**
```
"Add infinite scroll with lazy loading"
```
Result: Phased implementation plan, MCP validation, production-ready code with edge cases handled

**Example 3: Bug Fix**
```
"Form validation breaks on Safari"
```
Result: Root cause analysis, cross-browser solution, regression prevention

.

## 🏗️ Core Principles

### 1. Elite Engineering Standards
The AI operates as a senior engineer, not just a helpful assistant. Every response maintains production-grade quality with zero tolerance for technical debt.

### 2. DRY, KISS, CSS-First
- **DRY**: Never repeat code patterns
- **KISS**: Simplest solution that fully works
- **CSS-First**: Exhausts CSS before touching JavaScript

### 3. Evidence-Based Solutions
No assumptions. Every decision backed by explicit reasoning, validated through MCP tools when available.

### 4. Performance Obsession
- REM units only (never pixels)
- Minimize DOM manipulation
- CSS animations over JavaScript
- Lazy load everything possible

### 5. Risk Documentation
Proactively identifies and documents what could break, why, and how to prevent it.

.

## 📊 MCP Tool Workflow

```
User Request in IDE
     ↓
Internal Analysis (Sequential Thinking if available)
     ↓
Tool Selection Decision:
├─ Simple/Known → Direct Implementation
├─ Complex Logic → Code-Reasoning Validation
├─ Library Usage → Context7 Documentation
└─ Current Info → Web Search
     ↓
Validated Implementation
     ↓
Risk Documentation
```

.

## 🔧 Installing MCP Tools (Recommended)

MCP tools enhance your IDE's AI capabilities. While the IDE System Prompt works without them, having Sequential Thinking MCP provides systematic analysis for better code quality.

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Your AI-enabled IDE (Cursor, Windsurf, Claude Code, etc.)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for IDE System Prompt MCP tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone the Sequential Thinking MCP repo:
   - https://github.com/arben-adm/mcp-sequential-thinking.git
3. Create a docker-compose.yml file for the service
4. Configure my IDE to use the MCP tool:
   - For Cursor/Windsurf: Update settings
   - For Claude Code: Update claude.md
   - For VS Code: Update .vscode settings
5. Start the container with docker-compose

I'm using [Your IDE] on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your specific IDE and operating system.

**Verification:**
1. Check Docker Desktop for 1 running container
2. In your IDE, test with a complex request
3. The AI should mention using Sequential Thinking MCP

### Option B: NPX Installation (Quick Alternative)

For IDEs that support NPX-based MCP servers, add to your IDE configuration:

**For Cursor/Windsurf** (in project settings):
```json
{
  "mcp": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

**For Claude Code** (in claude.md):
```markdown
<!-- MCP Configuration -->
sequential-thinking: npx -y @modelcontextprotocol/server-sequential-thinking
```

### What Sequential Thinking MCP Does

When available in your IDE, it:
- Forces systematic step-by-step analysis before generating code
- Catches edge cases through structured thinking stages
- Validates architectural decisions before implementation
- Enhances code quality and reduces bugs

.

## 🆘 Troubleshooting

### AI Not Following Rules in IDE
- **Symptom**: AI gives generic responses without systematic analysis
- **Cause**: Rules not properly loaded or conflicting instructions
- **Solution**: 
  - Ensure rules are in correct IDE location
  - Check for syntax errors in configuration
  - Restart IDE after adding rules

### MCP Tools Not Working
- **Symptom**: AI doesn't mention using Sequential Thinking
- **Solution**: 
  1. Verify Docker container is running
  2. Check IDE MCP configuration
  3. Ensure IDE supports MCP tools
  4. Try NPX method if Docker fails

### Performance Issues with AI
- **Symptom**: Slow responses or timeouts in IDE
- **Solution**: 
  - Disable some rules for simpler tasks
  - Use modular rules approach
  - Disable MCP workflow for basic edits

### IDE-Specific Issues
- **Cursor**: Check .cursorrules file syntax
- **Windsurf**: Verify .windsurfrules placement
- **Claude Code**: Ensure claude.md is in project root
- **VS Code**: Check AI extension settings

### Getting Help
- Check your IDE's AI documentation
- Review Docker logs if using container method
- Simplify rules to identify issues
- Start with core rules (1-5) only

.

## ⚠️ Important Notes

- **IDE-Focused** - This system is for IDEs, NOT Claude Desktop
- **MCP Tools Optional** - System works without them but is more powerful with them
- **Framework Agnostic** - While optimized for Webflow + Slater, principles apply everywhere
- **Performance First** - CSS solutions always preferred over JavaScript
- **Production Standards** - Every response assumes production deployment
- **Modular Design** - Enable only the rules you need for each task

## 📦 Version History

- **v2.0.0**: MCP integration, modular rules, enhanced workflow
- **v1.5.0**: Added performance optimization rules
- **v1.0.0**: Initial release with core engineering principles

## 🎯 Key Principles

1. **Root Cause Analysis** - Never patch symptoms, fix the underlying issue
2. **Performance Obsession** - Every millisecond matters, CSS > JS always
3. **Production Grade** - Code that scales from day one
4. **Evidence-Based** - Validate assumptions with tools and data
5. **Risk Awareness** - Document what could break before it does

.

## 📚 Other Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [Sequential Thinking MCP](https://github.com/arben-adm/mcp-sequential-thinking)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Motion.dev Documentation](https://motion.dev)
- [Swiper.js](https://swiperjs.com)
- [Webflow Forums](https://forum.webflow.com)
- [Finsweet Resources](https://finsweet.com)

---

*Stop writing code that just works. Start engineering solutions that excel. With IDE System Prompt, your AI assistant becomes the senior engineer every project deserves.*