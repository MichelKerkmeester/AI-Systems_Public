# 🤖 Claude App Builder v1.4.0

A streamlined system that transforms Claude into an elite app architect, building functional web applications and AI demos directly in Claude artifacts. Now with intelligent thinking tool selection for optimal problem-solving.

## 🆕 What's New in v1.4.0

- **Intelligent Thinking Tool Selection**: Automatically chooses between Sequential and Cascade Thinking based on task complexity
- **Dynamic Thought Expansion**: Starts with just 1 thought, expands only when complexity demands
- **Complexity Scoring**: Smart algorithm to assess task requirements
- **Graceful Fallbacks**: Works seamlessly even without thinking MCPs
- **MCP Usage Documentation**: Clear indication of which tool was used in outputs

## Overview

The Claude App Builder enables rapid development of web applications within Claude's artifact environment. With three focused modes ($app, $ai, $data) and intelligent thinking optimization, it delivers production-ready applications that work immediately.

## ✨ Key Features

- **3 Specialized Modes**: $app (general apps), $ai (AI-powered interfaces), $data (dashboards & visualization)
- **Intelligent Thinking Tools**: Automatic selection between Sequential (linear) and Cascade (exploratory) thinking
- **MCP Integration**: Optional enhancements via $search, $docs, $ui, and $magic shortcuts
- **Fluid Responsive Design**: Smooth scaling using CSS clamp() formulas
- **Minimal Thought Overhead**: Starts with 1 thought, expands dynamically
- **Visual Pattern Libraries**: Reference UI patterns for professional designs
- **Zero External Dependencies**: Everything works within artifact constraints
- **Comprehensive Documentation**: Each app includes detailed README

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Claude App Builder v1.4"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `DEV - Claude App Builder - v1.4.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Claude App Builder - Artifact Standards - v1.0.1.md`
- `Claude App Builder - Fluid Responsive Guide - v1.0.1.md`
- `Claude App Builder - Visual Pattern Libraries - v1.0.0.md`

### Step 4: Enable MCP Features
Available MCP shortcuts for enhanced features:
- `$search` - Web search integration (requires Tavily or Brave Search MCP)
- `$docs` - Documentation access (requires Context7 MCP)
- `$ui` - Shadcn UI components (built-in, no MCP needed)
- `$magic` - Animation effects (built-in, only when explicitly requested)

### Step 5: Install Thinking Tools (Recommended)
The system intelligently selects between these based on task complexity:

#### Sequential Thinking (for linear tasks)
```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

#### Cascade Thinking (for exploratory tasks)
```json
{
  "cascade-thinking": {
    "command": "npx",
    "args": ["-y", "cascade-thinking-mcp"]
  }
}
```

### Step 6: Start Building
Simply describe what you want with the appropriate mode:
```
Build a $app todo list manager
Create an $ai chatbot assistant
Make a $data sales dashboard
```

## 🧠 Intelligent Thinking Tool Selection

The system automatically chooses the best thinking approach:

### Complexity Scoring
- **Mode**: $ai (3pts) > $data (2pts) > $app (1pt)
- **MCP Integration**: +2pts per MCP feature
- **Keywords**: +3pts for exploratory terms, -2pts for simple/basic
- **Threshold**: Score ≥5 uses Cascade, <5 uses Sequential

### Examples
- "Simple $app calculator" → Sequential (1 thought)
- "$ai multi-agent system with $search" → Cascade (starts with 1, may expand to 3-5)
- "$data dashboard" → Sequential (1-2 thoughts)

**Note**: The system works without these tools but provides enhanced analysis and planning capabilities when available. When tools are used, you'll see "MCP USED: [tool name]" in the documentation.

## 📋 System Modes

| Mode | Purpose | Use Cases | Typical Thinking |
|------|---------|-----------|------------------|
| **$app** | General web applications | Tools, utilities, CRUD apps | Sequential (1-3 thoughts) |
| **$ai** | AI-powered interfaces | Chatbots, assistants, multi-agent systems | Cascade (1-5 thoughts) |
| **$data** | Data visualization | Dashboards, analytics, CSV analysis | Sequential/Cascade (1-4 thoughts) |

## 🛠️ Technical Stack

### Pre-loaded Libraries
- React 18, Tailwind CSS (utilities only)
- Recharts, Lodash, Papaparse, XLSX
- Three.js r128, D3.js, Chart.js
- TensorFlow.js, Tone.js

### Claude-Specific APIs
- `window.claude.complete()` - AI completions
- `window.fs.readFile()` - File reading
- No localStorage - React state only
- Client-side only - No server capabilities

## 🔧 Constraints

- **No localStorage**: Use React state
- **No external APIs**: Except window.claude.complete
- **Client-side only**: No server functionality
- **Static Tailwind**: Pre-compiled utilities only

## 📚 Documentation

Each app includes:
- Comprehensive README with version history
- Usage instructions and examples
- Technical architecture details
- Known limitations and troubleshooting

## 📦 Complete MCP Installation Guide

### Thinking Tools (Highly Recommended)

**Sequential Thinking (for methodical, linear tasks):**
```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

**Cascade Thinking (for exploratory, multi-path tasks):**
```json
{
  "cascade-thinking": {
    "command": "npx",
    "args": ["-y", "cascade-thinking-mcp"]
  }
}
```

### Web Search MCPs (for $search)

**Tavily Search:**
```json
{
  "tavily": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-tavily"],
    "env": {
      "TAVILY_API_KEY": "your-api-key-here"
    }
  }
}
```

**Brave Search:**
```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "your-api-key-here"
    }
  }
}
```

### UI Component MCPs (for $ui and $magic)

**Shadcn UI (for $ui):**
```json
{
  "shadcn": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-shadcn"]
  }
}
```

**Magic UI (for $magic):**
```json
{
  "magic-ui": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-magic-ui"]
  }
}
```

### Documentation Access (for $docs)
**Context7:**
```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@context7/mcp-server"]
  }
}
```

### Notes:
- Replace `your-api-key-here` with actual API keys from the respective services
- Restart Claude Desktop after adding MCPs
- The thinking tools are optional but highly recommended for optimal performance
- The system works without any MCPs but is enhanced with them
- You'll see "MCP tools not available" notation if thinking tools aren't installed

## 🎯 Version History

- **v1.4.0**: Intelligent thinking tool selection, dynamic thought expansion
- **v1.3.1**: Enhanced visual patterns, mandatory sequential thinking
- **v1.3.0**: Fluid responsive design, comprehensive documentation
- **v1.2.0**: MCP integration, $ui and $magic components
- **v1.1.0**: Three specialized modes ($app, $ai, $data)
- **v1.0.0**: Initial release

---

*Build complete, functional web applications that work immediately. Focus on user experience and visual quality with intelligent optimization.*