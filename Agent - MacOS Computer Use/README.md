# macOS Computer Use Agent - User Guide v1.1.0

The macOS Computer Use Agent transforms natural language into precise UI operations, making computer control 10x easier. By focusing on WHAT you want to accomplish (not HOW to click), it bridges the gap between intention and automation. Interactive mode guides you through complex workflows with smart questions.

.

## ✨ Key Features

- **Natural Language First**: Describe what you want to do in plain English
- **3 Specialized Modes**: $interactive (default), $quick, $workflow
- **Triple MCP Support**: macOS Use MCP (core), Sequential Thinking (simple), Cascade Thinking (complex)
- **Interactive Guidance**: Default mode guides step-by-step through automations
- **Best Practices Built-in**: Uses keyboard shortcuts when faster than clicking
- **Visual Feedback**: Shows what's being clicked, typed, or navigated
- **Educational Focus**: Teaches shortcuts while automating
- **Safe Automation**: Always confirms before destructive operations
- **Zero Technical Knowledge**: No understanding of accessibility trees or coordinates required

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "macOS Computer Use Agent v1.1"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - macOS Computer Use MCP - v1.1.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these streamlined documents to your project:
- `Interactive Mode - v1.1.0.md` (Conversational automation specification)
- `Patterns & Workflows - v1.1.0.md` (All patterns and operation mappings)
- `Application Intelligence - v1.0.0.md` (App-specific best practices)

### Step 4: Build and Configure macOS Use MCP
The macOS Use MCP needs to be built from source:
1. Install Xcode Command Line Tools: `xcode-select --install`
2. Clone and build the MCP server (see installation section)
3. Configure Claude Desktop with the server path
4. Grant accessibility permissions when prompted

### Step 5: Start Automating
Simply describe what you need:
```
help me write an email           # Interactive mode (default)
find the preferences menu         # Interactive mode handles element finding
$q open Safari                    # Quick mode for immediate action
$q type my report                 # Quick mode for simple typing
$w research and summarize topic   # Workflow mode for multi-app tasks
```

.

## 🧠 Intelligent MCP Selection

The v1.1.0 release brings intelligent MCP tool selection with streamlined modes:

### Automatic Tool Selection

| Tool | When Used | Thought Count | Purpose |
|------|-----------|---------------|---------|
| **macOS Use MCP** | Always | N/A | All actual UI operations |
| **Sequential Thinking** | Simple operations | 2-3 thoughts | Linear tasks, single apps, quick typing |
| **Cascade Thinking** | Complex workflows | 5-7 thoughts | Multi-app workflows, element finding, complex text |

### Selection by Mode

| Mode | Primary MCP | Complexity | Interactive? |
|------|------------|------------|--------------|
| **Interactive** | Cascade | Adaptive | Yes (Default) |
| **Quick** | Sequential | Low | No |
| **Workflow** | Cascade | High | Optional |

### Example Intelligence

```markdown
User: I need to research laptops and create a comparison

System: [Selects Cascade Thinking for multi-app workflow]
I'll help you research laptops and create a comparison!

Let me set up an efficient workflow:
1. Open Safari for research
2. Create comparison document
3. Organize findings

Which format for the comparison?
• Spreadsheet (Numbers/Excel)
• Document (Pages/Word)
• Notes (quick capture)

[Based on answer, orchestrates complete workflow]
```

.

## 🎛️ Operating Modes

| Mode | Command | When to Use | MCP Strategy | Focus |
|------|---------|-------------|--------------|-------|
| **Interactive** | DEFAULT | Guidance needed, finding elements, complex text | Cascade (5-7) | Step-by-step guidance |
| **Quick** | `$q` | Single operations, simple typing | Sequential (2-3) | Speed over explanation |
| **Workflow** | `$w` | Multi-app sequences | Cascade (5-7) | Complete automation |

**Note:** Interactive mode is the default unless explicitly specified with $.

### Mode Capabilities

**Interactive Mode (Default)**
- Guided automation with questions
- Finding UI elements
- Complex text composition
- Form filling assistance
- Multi-step operations
- Educational explanations

**Quick Mode ($q)**
- Immediate single actions
- Simple text input
- Direct clicks
- Basic navigation
- No explanations
- Fast execution

**Workflow Mode ($w)**
- Multi-app orchestration
- Complex sequences
- Document creation
- Research workflows
- Data processing
- Automated pipelines

.

## 💬 Interactive Mode Flow

The default conversational experience:

### Typical Flow
1. User describes need (no mode specified)
2. System identifies apps and complexity
3. Asks strategic questions if needed
4. Shows automation preview
5. Executes operations step-by-step
6. Provides visual confirmation
7. Suggests logical next steps

### Quality Indicators
```markdown
🖱️ Automation Report
────────────────────────
MCP Used: Cascade Thinking (5 thoughts)
Complexity: Medium
Time to Complete: 15 seconds

✅ Completed Successfully:
✔ Opened Mail app
✔ Created new message
✔ Added recipient
✔ Typed subject
✔ Composed email body
✔ Attached 3 files

💡 macOS Tip: Press ⌘⇧D to send emails quickly
```

.

## 📝 Automation Patterns

Every automation uses intelligent patterns:

### Email Workflow
```markdown
Email Composition:
├── Open Mail (⌘Space → "Mail")
├── New Message (⌘N)
├── Fill recipient (Tab navigation)
├── Add subject (Tab)
├── Type content (with formatting)
└── Send (⌘⇧D)
```

### Research Workflow
```markdown
Web Research:
├── Open Safari (new window)
├── Create tab group
├── Search multiple sources
├── Use Reader mode (⌘⇧R)
├── Copy key points
└── Create summary document
```

### Form Filling
```markdown
Form Automation:
├── Click first field
├── Type content
├── Tab to next field
├── Space for checkboxes
├── Arrow keys for dropdowns
└── Return to submit
```

### Element Finding
```markdown
Finding UI Elements:
├── Refresh UI tree
├── Search by label
├── Check similar names
├── Verify position
├── Click when found
└── Confirm success
```

### Text Input
```markdown
Text Entry:
├── Identify text field
├── Click to focus
├── Type content
├── Format if needed
├── Tab to continue
└── Save when complete
```

.

## 🔌 UI Operations

The system provides these core operations:

### Essential Operations
- **open_application_and_traverse** - Launch and explore apps
- **click_and_traverse** - Click elements and update UI tree
- **type_and_traverse** - Input text with verification
- **press_key_and_traverse** - Keyboard shortcuts
- **refresh_traversal** - Update UI understanding

### Smart Defaults
- **Browser needed** → Safari (default) or Chrome
- **Text editing** → TextEdit or Notes
- **Email** → Mail app
- **Settings** → System Settings
- **Documents** → Pages or Word

### Common Shortcuts Applied
- **⌘N** → New window/document
- **⌘T** → New tab
- **⌘W** → Close window
- **⌘Tab** → Switch apps
- **⌘Space** → Spotlight search

.

## 📋 Examples

### Interactive Mode (Default)
```
User: help me write an email
System: [Starts conversation, selects Cascade Thinking]
I'll help you write an email! Which app would you like to use?
• Mail (Apple's email app)
• Gmail in browser
• Outlook
```

```
User: find the save button
System: [Uses Interactive mode for element finding]
Let me find the save button for you...
🔍 Searching UI elements...
✔ Found "Save" button at top toolbar
Clicking it now...
```

### Quick Mode
```
User: $q click Safari
System: [Uses Sequential Thinking for immediate action]
✔ Clicked Safari
```

```
User: $q type Hello World
System: [Quick typing without guidance]
✔ Typed: "Hello World"
```

### Workflow Mode
```
User: $w research and summarize AI trends
System: [Uses Cascade Thinking for complete workflow]
Creating research workflow...
Opening Safari, setting up tabs, preparing document...
```

### Complex System Example
```markdown
User: help me prepare for my presentation
System: I'll help you prepare your presentation!

What do you need help with?
1. Creating slides (Keynote/PowerPoint)
2. Research and content gathering
3. Speaker notes preparation
4. All of the above

[Creates integrated workflow across multiple apps]

✅ Presentation Prep Complete:
• Research tabs organized in Safari
• Keynote presentation created
• 10 slides with titles
• Speaker notes added
• Images inserted
• Transitions configured
```

.

## 🔧 Installing MCPs (Required & Optional)

### Required: macOS Use MCP

The macOS Use MCP needs to be built from source using Swift.

#### Installation Steps

**Prerequisites:**
- macOS (Monterey or later recommended)
- Xcode Command Line Tools installed
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**Step 1: Install Xcode Command Line Tools**
```bash
xcode-select --install
```

**Step 2: Clone and Build the MCP Server**
```bash
# Create directory for MCP servers
mkdir -p "$HOME/MCP Servers"
cd "$HOME/MCP Servers"

# Clone the repository
git clone https://github.com/mediar-ai/mcp-server-macos-use.git
cd mcp-server-macos-use

# Build the server (use 'debug' for development, 'release' for production)
swift build -c debug
```

**Step 3: Configure Claude Desktop**

Add to Claude Desktop config:

**Config Location:**
- Mac: `~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "macos-use": {
      "command": "/Users/YOUR_USERNAME/MCP Servers/mcp-server-macos-use/.build/debug/mcp-server-macos-use"
    }
  }
}
```

*Replace `YOUR_USERNAME` with your actual macOS username.*

**Step 4: Grant Accessibility Permissions**
1. System Settings → Privacy & Security → Accessibility
2. Click the lock to make changes
3. Add Claude Desktop (click + and navigate to Applications)
4. Enable the checkbox next to Claude
5. Restart Claude Desktop

**Verification:**
1. Look for the 🔌 icon in Claude Desktop showing "macos-use" connected
2. Test with: "open Safari" or "help me write an email"

### Optional: Thinking MCPs (Enhanced Intelligence)

For even better automation design, add thinking tools:

#### Option A: AI-Powered Installation Assistant

**Prerequisites:**
- Node.js installed ([Download Node.js](https://nodejs.org/))
- Claude Desktop app already configured

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up the thinking MCPs for the macOS Computer Use Agent.

I need to:
1. Install Node.js if not already installed
2. Configure Claude Desktop's config file at ~/.config/claude/claude_desktop_config.json
3. Add the Sequential Thinking and Cascade Thinking MCPs using NPX
4. Verify the tools are connected

I'm on macOS. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your setup.

#### Option B: Manual NPX Setup

Add to Claude Desktop config (after the macos-use entry):

**Config Location:**
- Mac: `~/.config/claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "macos-use": {
      "command": "/Users/YOUR_USERNAME/MCP Servers/mcp-server-macos-use/.build/debug/mcp-server-macos-use"
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "cascade-thinking": {
      "command": "npx",
      "args": ["-y", "cascade-thinking-mcp"]
    }
  }
}
```

**Verification:**
1. Restart Claude Desktop
2. Look for the 🔌 icon showing all three tools connected
3. Test with: "help me organize my desktop"

**Benefits of Thinking MCPs:**
- **Sequential Thinking**: 2x faster simple operations
- **Cascade Thinking**: Smarter workflow design
- **Automatic selection**: Agent chooses the right tool
- **Better patterns**: Explores all automation options
- **Intelligent decisions**: Evaluates most efficient approach

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Can't control apps"** | Grant accessibility permissions in System Settings |
| **"Element not found"** | Use Interactive mode to help find elements |
| **"App won't open"** | Check if app is installed, try Spotlight |
| **"Clicking wrong place"** | Use more specific element description |
| **"Permission denied"** | System Settings → Privacy & Security → Accessibility |
| **"MCP not connected"** | Restart Claude Desktop |

### Quick Fixes

**Build Issues:**
```bash
# Check Swift version
swift --version

# Clean and rebuild
cd "$HOME/MCP Servers/mcp-server-macos-use"
swift package clean
swift build -c debug

# Check if server is built
ls -la .build/debug/mcp-server-macos-use
```

**Accessibility Issues:**
```bash
# Check accessibility permissions
System Settings → Privacy & Security → Accessibility
# Enable for Claude Desktop
# Restart Claude Desktop
```

**NPX Issues:**
- Ensure Node.js installed
- Check config file syntax
- Restart Claude Desktop

### Interactive Mode Help
- **Too many steps?** System breaks down complex tasks
- **Want direct action?** Use explicit mode ($q, $w)
- **Need different app?** System adapts to available apps
- **Can't find element?** Interactive mode guides the search

### MCP Connection Issues
- **Build failed**: Ensure Xcode Command Line Tools installed
- **Server not found**: Check path in config matches built executable
- **Can't connect**: Restart Claude Desktop after config changes
- **Accessibility blocked**: Grant permissions and restart
- **Wrong path**: Use absolute path to the built executable

### Common Setup Problems
- **"swift: command not found"**: Install Xcode Command Line Tools
- **Build errors**: Ensure you're on macOS Monterey or later
- **Config not working**: Check JSON syntax and absolute paths
- **No UI control**: Accessibility permissions required
- **Frozen automation**: Press Esc to cancel, restart if needed

### Getting Help
- For build issues: Check Swift version with `swift --version`
- For config issues: Verify JSON syntax and paths
- For UI issues: Verify accessibility permissions
- For general issues: The AI assistant can help diagnose problems
- For technical support: Reach out to matt@mediar.ai or Discord: m13v_

.

## ⚠️ Important Notes

- **Interactive is default** - No $ prefix needed
- **Accessibility required** - Must grant permissions
- **Build from source** - macOS Use MCP requires Swift build
- **Safety first** - Confirms destructive operations
- **Best practices automatic** - Uses shortcuts when faster
- **Works without thinking MCPs** - But enhanced with them
- **Educational by design** - Teaches shortcuts while automating
- **Visual feedback always** - See what's happening
- **Reversible actions** - Most operations can be undone with ⌘Z
- **macOS only** - Requires macOS Monterey or later

.

## 📦 Version History

- **v1.1.0**: Streamlined to 3 modes (removed Navigate and Type modes)
- **v1.0.0**: Initial release with 5 modes

.

## 📚 Resources

### Core Tools
- [macOS Use MCP](https://github.com/mediar-ai/mcp-server-macos-use) (Required)
- [Sequential Thinking MCP](https://github.com/modelcontextprotocol/server-sequential-thinking) (Optional)
- [Cascade Thinking MCP](https://github.com/cascadethinking/cascade-thinking-mcp) (Optional)

### Documentation
- [macOS Accessibility Guide](https://support.apple.com/guide/mac-help/control-mac-accessibility-shortcuts-mh43607/mac)
- [macOS Keyboard Shortcuts](https://support.apple.com/en-us/HT201236)
- [MCP Protocol](https://modelcontextprotocol.io/)

### Quick Links
- [System Settings](x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility)
- [Claude Projects](https://claude.ai)
- [macOS Terminal Guide](https://support.apple.com/guide/terminal/welcome/mac)

.

---

*Transform natural language into precise macOS UI operations through conversation. Interactive mode guides you step-by-step. Complex workflows automated in seconds. Just describe what you want to do and watch your Mac respond.*