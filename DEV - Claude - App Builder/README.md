# Claude App Builder - User Guide v2.0

## 🚀 What is This?

The Claude App Builder transforms Claude into an elite app architect, building functional web applications and AI demos directly in Claude artifacts. Instead of explaining how to code, Claude builds complete, working applications ready for immediate use.

**Key Benefits:**
- Transform ideas into functional web apps in minutes
- No coding knowledge required - just describe what you want
- Professional UI/UX with fluid responsive design built-in
- Three specialized modes for different app types
- Sequential thinking ensures thoughtful architecture
- Works immediately in Claude artifacts (no external setup)
- Complete documentation with every app
- **Enhanced with MCP tools for search, docs, and UI components**

**Key Principle:** If you can imagine it, Claude can build it as a working app.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Claude App Builder v2.0"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `DEV - Claude App Builder - v1.3.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Upload all reference documents to your project:
- `Claude App Builder - Artifact Standards - v1.0.1.md` (technical constraints)
- `Claude App Builder - Fluid Responsive Guide - v1.0.1.md` (scaling formulas)
- `Claude App Builder - Visual Pattern Libraries - v1.0.0.md` (UI components)

### Step 4: Start Building Apps!
Simply describe what you want with the appropriate mode:
```
Build a $app todo list manager
Create an $ai chatbot assistant
Make a $data sales dashboard
```

.

## 🧠 Enhanced Intelligence: MCP Integration

### Available MCP Enhancements
The App Builder can leverage these optional MCP tools:

1. **Sequential Thinking MCP** - **REQUIRED** for optimization step
2. **Web Search MCPs** - For `$search` shortcut (Tavily or Brave)
3. **Documentation MCP** - For `$docs` shortcut (Context7)
4. **UI Component MCPs** - For `$ui` and `$magic` shortcuts

### Feature Shortcuts
| Shortcut | Feature | MCP Required |
|----------|---------|--------------|
| `$search` | Web search integration | Tavily or Brave Search MCP |
| `$docs` | Documentation access | Context7 MCP |
| `$ui` | Shadcn UI components | Built-in (no MCP needed) |
| `$magic` | Animation effects | Built-in (no MCP needed) |

### Sequential Thinking Process
Every app goes through mandatory optimization:
- **Step 1:** Understand requirements
- **Step 2:** Plan architecture
- **Step 3:** Design user flow
- **Step 4:** Optimize performance
- **Step 5:** Build and document

.

## 🎯 How to Use

### Basic Usage
Simply describe what you want with a mode:
```
Build a $app for tracking expenses
```

The system will:
1. Activate Sequential Thinking for planning
2. Design the architecture
3. Create a fluid responsive interface
4. Build the complete app
5. Include comprehensive documentation

### Mode Selection
| Mode | Command | Use For | Examples |
|------|---------|---------|----------|
| **$app** | `$app` | General web applications | Todo lists, calculators, tools |
| **$ai** | `$ai` | AI-powered interfaces | Chatbots, assistants, demos |
| **$data** | `$data` | Data visualization | Dashboards, analytics, reports |

### Example Requests

**Simple App:**
```
Build a $app countdown timer for events
```

**AI Interface:**
```
Create an $ai writing assistant with multiple personalities
```

**Data Dashboard:**
```
Make a $data dashboard for analyzing CSV sales data
```

**With Enhancements:**
```
Build a $app recipe finder with $search capabilities
Create an $ai code helper with $docs access to MDN
```

.

## ✅ Output Format

### Every App Includes:
1. **Complete working artifact** (React component)
2. **Fluid responsive design** (scales 320px-1920px)
3. **Professional UI/UX** (Tailwind utilities)
4. **Comprehensive README** (in app footer)
5. **Version history** (semantic versioning)
6. **Usage instructions** (clear examples)
7. **Technical documentation** (architecture details)

### Example Output Structure:
```jsx
MODE: $app
TYPE: Expense Tracker
MCP USED: Sequential Thinking
FEATURES: Local state management, CSV export, charts

// Complete React component with:
// - Fluid typography using clamp()
// - Responsive layout
// - Professional styling
// - Error handling
// - Accessibility features
```

.

## 🛠️ Technical Stack

### Pre-loaded Libraries
- **Core:** React 18, Tailwind CSS (utilities only)
- **Data:** Recharts, Lodash, Papaparse, XLSX
- **3D/Visual:** Three.js r128, D3.js, Chart.js
- **AI/Audio:** TensorFlow.js, Tone.js
- **UI:** Lucide-react icons, shadcn/ui components

### Claude-Specific APIs
- `window.claude.complete()` - AI completions
- `window.fs.readFile()` - File reading
- **No localStorage** - React state only
- **Client-side only** - No server capabilities

### Design Constraints
- **Fluid scaling:** 320px to 1920px viewports
- **Static Tailwind:** Pre-compiled utilities only
- **Single artifact:** Everything in one component
- **No external APIs:** Except window.claude

.

## 🔧 Installing MCP Tools (Recommended)

### Option A: AI-Powered Setup (Recommended)

**Prerequisites:**
- Claude Desktop app ([Download Claude](https://claude.ai/download))
- Python 3.10+ with UV (for uvx method) OR Node.js (for npx method)

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up MCP tools for Claude App Builder.

I need to install:
1. Sequential Thinking MCP (REQUIRED)
   - Option A: uvx method (full features)
   - Option B: npx method (simpler)
2. Web Search MCPs (optional for $search)
   - Tavily (need API key)
   - Brave Search (need API key)
3. Context7 MCP (optional for $docs)
4. UI Component MCPs (built-in, but can add if needed)

I'm on [Windows/Mac/Linux]. Please give me the exact configuration for Claude Desktop's settings.
```

The AI will provide the complete JSON configuration for your system.

### Option B: Manual Installation

**1. Sequential Thinking (REQUIRED):**

Using uvx (full features):
```json
{
  "sequential-thinking": {
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/arben-adm/mcp-sequential-thinking",
      "--with",
      "portalocker",
      "mcp-sequential-thinking"
    ]
  }
}
```

Using npx (simpler):
```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
  }
}
```

**2. Search MCPs (for $search):**

Tavily:
```json
{
  "tavily": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-tavily"],
    "env": {
      "TAVILY_API_KEY": "your-api-key"
    }
  }
}
```

Brave:
```json
{
  "brave-search": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-brave-search"],
    "env": {
      "BRAVE_API_KEY": "your-api-key"
    }
  }
}
```

**3. Documentation (for $docs):**
```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@context7/mcp-server"]
  }
}
```

**Verification:**
1. Restart Claude Desktop after adding MCPs
2. Look for the 🔌 icon showing available tools
3. Test with: "Build a $app calculator"

.

## 🆘 Troubleshooting

### "App won't render"
- Check React syntax errors in console
- Ensure all imports are from allowed libraries
- Verify no localStorage usage
- Confirm single artifact structure

### "Responsive design issues"
- All measurements use clamp() formulas
- Test at 320px, 768px, and 1920px widths
- Check fluid typography scaling
- Verify container constraints

### "Can't use external data"
- Use window.fs.readFile for uploaded files
- No external API calls allowed
- Work with local state only
- Consider mock data for demos

### "Sequential Thinking not working"
- Ensure MCP is installed correctly
- Restart Claude Desktop
- Check for Python/Node.js installation
- Try alternative installation method

### MCP Connection Issues
- **MCP not found**: Check installation path
- **Can't connect**: Restart Claude Desktop
- **Permission errors**: Run as administrator (Windows) or use sudo (Mac/Linux)
- **API key issues**: Verify keys are correct and active

### Common Setup Problems
- **"Command not found"**: Install Python/UV for uvx or Node.js for npx
- **Tools not showing**: Restart Claude Desktop after config changes
- **Rate limits**: API services may have usage limits
- **Version conflicts**: Update to latest MCP versions

### App-Specific Issues
- **Performance**: Optimize with React.memo and useMemo
- **State management**: Use useReducer for complex state
- **File reading**: Handle errors gracefully
- **AI completions**: Add loading states

### Getting Help
- Check browser console for errors
- Review artifact constraints in documentation
- Test in different viewport sizes
- The AI assistant can debug specific issues

.

## ⚠️ Important Notes

- **Sequential Thinking is REQUIRED** - Won't work properly without it
- **No localStorage** - Always use React state
- **Client-side only** - No server functionality
- **Single artifact** - Everything in one file
- **Works without other MCPs** - But enhanced with them

## 📦 Version History

- **v2.0.0**: Enhanced MCP integration guide, standardized setup
- **v1.3.1**: Added Sequential Thinking requirement
- **v1.3.0**: Three modes with optimization
- **v1.0.0**: Initial app builder system

## 🎯 Key Principles

1. **Immediate functionality** - Apps work instantly, no setup
2. **Professional quality** - Production-ready UI/UX
3. **Fluid responsiveness** - Perfect on any device
4. **Complete documentation** - Every app fully documented
5. **User-focused design** - Intuitive and accessible

.

## 📚 Other Resources

- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Sequential Thinking MCP](https://github.com/arben-adm/mcp-sequential-thinking)
- [Tavily Search API](https://tavily.com/)
- [Brave Search API](https://brave.com/search/api/)
- [Context7 Documentation](https://context7.com/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Claude Desktop Download](https://claude.ai/download)

---

*Transform ideas into working web applications instantly. Focus on what you want to build, not how to build it.*