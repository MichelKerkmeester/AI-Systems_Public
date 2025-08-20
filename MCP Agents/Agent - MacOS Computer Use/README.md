# macOS Computer Use Agent - User Guide v1.2.0

The macOS Computer Use Agent transforms natural language into precise UI operations, making computer control accessible through conversation. No technical knowledge required - just describe what you want to do and the system handles all complexity through intelligent dialogue.

## 📑 Table of Contents

- [🆕 What's New in v1.2.0](#-whats-new-in-v120)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 Intelligent Conversation System](#-intelligent-conversation-system)
- [💬 Conversation Examples](#-conversation-examples)
- [📊 Visual Feedback Standards](#-visual-feedback-standards)
- [🔧 Installing MCPs](#-installing-mcps)
- [📋 Common Automation Patterns](#-common-automation-patterns)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📊 Quality Standards](#-quality-standards)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## 🆕 What's New in v1.2.0

### Major Simplification
- **Unified Conversational Interface**: Removed all explicit modes and commands
- **Automatic Adaptation**: System adjusts conversation depth based on request clarity
- **Confidence-Based Response**: Dynamic interaction from immediate execution to full guidance
- **Intelligent MCP Selection**: Automatic tool selection based on complexity
- **Enhanced Element Finding**: Improved UI element discovery through conversation

### Maintained Excellence
- All v1.1.0 capabilities preserved
- Zero technical knowledge requirement
- Educational insights during automation
- Visual feedback for every action
- Safe operations with confirmation for destructive actions

.

## ✨ Key Features

- **Conversational Control**: Natural language interface with adaptive dialogue depth
- **Intelligent MCP Selection**: Automatic tool selection based on complexity
- **No Modes Required**: Unified conversational interface adapts to your needs
- **Element Finding**: Helps locate any UI element through conversation
- **Text Composition**: Assists with writing emails, documents, and forms
- **Visual Feedback**: Clear confirmation of every action taken
- **Educational Insights**: Learn shortcuts naturally during automation
- **Safe Operations**: Confirms before destructive actions
- **Zero Technical Knowledge**: No understanding of PIDs, coordinates, or commands needed

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "macOS Computer Use Agent v1.2"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - macOS Computer Use MCP - v1.2.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these core documents to your project:
- `macOS - Interactive Intelligence - v1.2.0.md` (Conversational interface specification)
- `macOS - Patterns & Workflows - v1.2.0.md` (All patterns and operation mappings)
- `macOS - Application Intelligence - v1.1.0.md` (App-specific best practices)

### Step 4: Build and Configure macOS Use MCP
The macOS Use MCP needs to be built from source:
1. Install Xcode Command Line Tools: `xcode-select --install`
2. Clone and build the MCP server (see installation section)
3. Configure Claude Desktop with the server path
4. Grant accessibility permissions when prompted

### Step 5: Start Automating
Simply describe what you need:
```
open Safari                      # High confidence - immediate execution
help me write an email          # Medium confidence - guided composition
find the save button            # Element finding with assistance
research climate change         # Complex workflow with planning
help                           # Full guidance through capabilities
```

.

## 🧠 Intelligent Conversation System

### Confidence-Based Response

The system automatically adjusts conversation depth based on request clarity:

| Confidence | Range | Response Strategy | Example |
|------------|-------|------------------|---------|
| **Exact** | >0.95 | Immediate execution | "open Safari" → Opens immediately |
| **High** | 0.80-0.95 | Single clarification | "browse the web" → "Safari or Chrome?" |
| **Medium** | 0.50-0.79 | Guided exploration | "do something online" → Options provided |
| **Low** | <0.50 | Full guidance | "help" → Complete capability overview |

### Intelligent MCP Selection

When thinking MCPs are available:

| Tool | When Used | Thought Count | Purpose |
|------|-----------|---------------|---------|
| **Sequential Thinking** | Simple operations | 2-3 thoughts | Linear tasks, single apps |
| **Cascade Thinking** | Complex workflows | 5-7 thoughts | Multi-app, element finding |
| **macOS Use MCP** | Always | N/A | Actual UI operations |

The system automatically selects the appropriate tool based on:
- Request complexity
- Number of apps involved
- Element finding needs
- Text composition requirements
- User confidence level

.

## 💬 Conversation Examples

### High Confidence - Direct Execution
```
User: open Safari

System: Opening Safari for you!
        
        ✔ Safari launched and ready
        
        Would you like to navigate to a website or search for something?
```

### Medium Confidence - Brief Clarification
```
User: I need to browse

System: I'll help you browse the web! 
        
        Which browser would you prefer:
        • Safari (Mac's default)
        • Chrome
        • Firefox
        
        Or just tell me what you're looking for and I'll use Safari.
```

### Element Finding
```
User: where's the print option?

System: I'll help you find the print option!

        🔍 Let me check the current application...
        You're in Safari.

        Found print options in multiple locations:
        1. File menu → Print (⌘P)
        2. Right-click context menu → Print
        3. Share button → Print

        The quickest way is pressing ⌘P. 

        Would you like me to:
        • Open the print dialog now
        • Show you where to click
        • Just remember the shortcut
```

### Complex Text Composition
```
User: help me write a thank you email to my boss

System: I'll help you write a professional thank you email to your boss!

        Let me set this up properly.

        Opening Mail app...
        ✔ Mail ready

        Creating new message...
        ✔ New email opened

        First, what's your boss's email address?

User: boss@company.com

System: Adding recipient...
        ✔ Added boss@company.com

        Now for the subject. For a thank you email, I suggest:
        • "Thank You - [Specific Reason]"
        • "Appreciation for Your Support"
        • "Grateful for the Opportunity"

        What are you thanking them for?

[Continues with guided composition...]
```

### Multi-App Workflow
```
User: I need to research something and take notes

System: I'll help you research and take notes efficiently!

        Here's my plan:
        1. Open Safari for research
        2. Open Notes app alongside
        3. Help you search and capture information

        What topic are you researching?

User: climate change impacts

System: Perfect! Setting up your research workspace...

        Opening Safari...
        ✔ Safari ready

        Navigating to Google...
        ✔ Search page loaded

        Searching for "climate change impacts"...
        ✔ Results loaded

        Now opening Notes app...
        ✔ Notes ready

        Arranging windows side by side...
        ✔ Windows arranged for easy reference

        💡 Tip: Use ⌘Tab to quickly switch between apps!

[Continues with research assistance...]
```

.

## 📊 Visual Feedback Standards

Every operation includes clear visual confirmation:

```
🖱️ Automating: Write and send email
📍 Current: Mail app
────────────────────────
Opening Mail...
✔ Mail opened (PID: 1234)

Creating new message...
✔ New email window opened

Adding recipient...
✔ Added: boss@company.com

Typing subject...
✔ Subject: "Thank You - Project Approval"

Composing message...
✔ Email body completed (247 words)

✅ Complete! Email ready to send

💡 Mail tip: Press ⌘⇧D to send quickly

Next steps:
• Send email (⌘⇧D)
• Add attachment (⌘⇧A)
• Save as draft
• Start another email
```

.

## 🔧 Installing MCPs

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

#### NPX Setup

Add to Claude Desktop config (after the macos-use entry):

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

**Benefits of Thinking MCPs:**
- **Sequential Thinking**: Faster simple operations
- **Cascade Thinking**: Better complex workflow design
- **Automatic selection**: Agent chooses the right tool
- **Intelligent patterns**: Explores all automation options

.

## 📋 Common Automation Patterns

### Application Control
```markdown
Navigation:
├── Open app (⌘Space → app name)
├── Switch windows (⌘Tab)
├── New document (⌘N)
├── Settings (⌘,)
└── Quit (⌘Q)
```

### Text Operations
```markdown
Text Entry:
├── Click field to focus
├── Type content
├── Tab to next field
├── Format with shortcuts
├── Save (⌘S)
└── Review and confirm
```

### Element Finding
```markdown
Finding UI Elements:
├── Check current window
├── Scan toolbar and menus
├── Search File/Edit/View menus
├── Look for keyboard shortcuts
├── Check preferences
└── Suggest alternatives
```

### Form Filling
```markdown
Form Automation:
├── Analyze form structure
├── Click first field
├── Type content
├── Tab navigation
├── Validate format
├── Review before submit
└── Confirm submission
```

### Research Workflow
```markdown
Web Research:
├── Open browser
├── Create tab group
├── Search multiple sources
├── Activate reader mode
├── Copy key points
├── Organize in Notes
└── Create summary
```

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **"Can't control apps"** | Grant accessibility permissions in System Settings |
| **"Element not found"** | System will help find through conversation |
| **"App won't open"** | Check if installed, try Spotlight search |
| **"Clicking wrong place"** | Provide more specific description |
| **"Permission denied"** | System Settings → Privacy & Security → Accessibility |
| **"MCP not connected"** | Restart Claude Desktop |
| **"Text not typing"** | Click field first, check focus |

### Build Issues
```bash
# Check Swift version
swift --version

# Clean and rebuild
cd "$HOME/MCP Servers/mcp-server-macos-use"
swift package clean
swift build -c debug

# Verify build
ls -la .build/debug/mcp-server-macos-use
```

### Connection Issues
- **Build failed**: Ensure Xcode Command Line Tools installed
- **Server not found**: Check path in config matches built executable
- **Can't connect**: Restart Claude Desktop after config changes
- **Accessibility blocked**: Grant permissions and restart

### Getting Help
- For build issues: Check Swift version with `swift --version`
- For config issues: Verify JSON syntax and paths
- For UI issues: Verify accessibility permissions
- For automation help: Just ask - the system will guide you
- For technical support: matt@mediar.ai or Discord: m13v_

.

## ⚠️ Important Notes

- **Conversational by default** - No modes or commands needed
- **Adaptive intelligence** - Automatically adjusts to your needs
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

## 📊 Quality Standards

Every automation ensures:
- ✅ Intent understood through conversation
- ✅ Appropriate guidance depth
- ✅ Elements found intelligently
- ✅ Operations executed efficiently
- ✅ Success confirmed visually
- ✅ Shortcuts taught naturally
- ✅ Next steps suggested
- ✅ Errors handled gracefully

Performance Metrics:
- **Intent Recognition**: >95% accuracy
- **Element Finding**: >90% success rate
- **User Satisfaction**: Natural conversation flow
- **Task Completion**: >90% success rate
- **Education Adoption**: >70% use taught shortcuts

.

## 📦 Version History

- **v1.2.0**: Unified conversational interface, removed explicit modes
- **v1.1.0**: Streamlined to 3 modes (Interactive, Quick, Workflow)
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

*Transform natural language into precise macOS UI operations through intelligent conversation. The system adapts to your needs automatically - no technical knowledge required. Just describe what you want to do and watch your Mac respond.*