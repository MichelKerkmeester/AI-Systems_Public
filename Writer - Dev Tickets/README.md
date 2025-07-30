# Dev Ticket Writer - User Guide v2.1

## 🚀 What is This?

The Dev Ticket Writer system transforms any request into clear, actionable development tickets. Instead of vague requirements or technical jargon, you get tickets that communicate user value and business outcomes, letting developers focus on HOW to implement.

**Key Benefits:**
- Transform unclear requests into actionable tickets
- Communicate user value and business impact clearly
- Get consistent ticket format across your team
- Focus on WHAT and WHY, not HOW
- Save time with structured templates
- Professional presentation with abstract symbols throughout
- **NEW: Interactive mode for guided ticket creation (DEFAULT)**
- **NEW: Intelligent partial input enhancement**
- **NEW: Enhanced MCP tool selection for optimal analysis**

**Key Principle:** If a ticket takes more than 2 minutes to read, it's too long.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v2.1"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Writer - Dev Tickets - v2.1.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Upload all reference documents to your project:
- `Ticket - Interactive Mode - v1.1.0.md` (conversational ticket creation)
- `Ticket - Examples - Quick & Standard - v1.1.0.md` (mode examples)
- `Ticket - Examples - Complex & Epic - v1.1.0.md` (advanced examples)
- `Ticket - Examples - Bugs & Improvements - v1.1.0.md` (specialized types)
- `Ticket - Examples - Partial Input Handling - v1.1.0.md` (enhancement patterns)
- `Ticket - Patterns & Methodology - v1.1.0.md` (quality patterns)

### Step 4: Start Writing Tickets!
Begin any conversation in the project, and Claude will default to Interactive Mode, guiding you through creating professional tickets.

.

## 🧠 Enhanced Intelligence: Dual MCP Support

### What's New in v2.1?
The Dev Ticket Writer now intelligently chooses between two thinking tools based on your request complexity:

1. **Sequential Thinking MCP** - For straightforward, linear analysis
2. **Cascade Thinking MCP** - For complex scenarios requiring exploration of alternatives

The system automatically selects the best tool and adapts the number of analysis thoughts (minimum 1, scaling up based on complexity).

### Intelligent Selection Logic

**Sequential Thinking is chosen for:**
- Simple feature requests with clear scope
- Quick (`$q`) and Standard (`$s`) mode tickets
- Bug fixes and performance improvements
- Single-feature implementations
- Straightforward requirement updates

**Cascade Thinking is chosen for:**
- Interactive mode conversations (`$interactive`)
- Complex (`$c`) and Epic (`$e`) mode tickets
- Requests mentioning "alternatives" or "options"
- Multi-phase implementations
- Unclear scope requiring exploration
- Comparing different solutions
- Features with interconnected dependencies

### Adaptive Thought Process

The system now uses a flexible approach:
- **Minimum:** 1 thought (for very simple requests)
- **Simple requests:** 1-2 thoughts
- **Standard features:** 2-3 thoughts
- **Interactive conversations:** 3-5 thoughts
- **Complex analysis:** 3-5 thoughts with potential branching
- **Epic breakdown:** 5+ thoughts with multiple exploration branches

.

## 🔧 Installing MCP Tools (Optional but Recommended)

Both tools work independently, so you can install one or both based on your needs.

### Sequential Thinking MCP Installation

**For simpler, linear ticket analysis:**

1. **Edit your Claude Desktop configuration:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Add Sequential Thinking:**
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

### Cascade Thinking MCP Installation

**For complex ticket analysis with branching:**

1. **Add to the same configuration file:**
```json
{
  "mcpServers": {
    "cascade-thinking": {
      "command": "npx",
      "args": ["-y", "cascade-thinking-mcp"]
    }
  }
}
```

### Installing Both Tools

**For maximum flexibility:**
```json
{
  "mcpServers": {
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

3. **Save and restart Claude Desktop**

4. **Verify installation** by looking for the 🔌 icon showing available tools

**Note**: The system works without these tools but provides enhanced analysis when available.

.

## 🎯 How to Use

### Basic Usage (Interactive Mode - DEFAULT)
Simply describe what you need:
```
We need search filters for our product catalog
```

The system will:
1. Start Interactive Mode by default
2. Guide you through key questions
3. Choose appropriate MCP tool (if available)
4. Analyze with adaptive thought count
5. Generate the perfect ticket

### Mode Selection
The system has five modes for different complexity levels:

| Mode | Command | Use For | Typical MCP | Thoughts |
|------|---------|---------|-------------|----------|
| **Interactive** | `$interactive` or `$int` | DEFAULT - Guided creation | Cascade | 3-5 |
| **Quick** | `$q` | Simple, single features (explicit only) | Sequential | 1-2 |
| **Standard** | `$s` | Most features and improvements (explicit only) | Sequential | 2-3 |
| **Complex** | `$c` | Multi-phase implementations (explicit only) | Cascade | 3-5 |
| **Epic** | `$e` | Major initiatives with child tickets (explicit only) | Cascade | 5+ |

### Mode Examples:
```
need user profiles
(Automatically starts Interactive Mode)

$interactive need user profiles
(Explicitly starts guided conversation)

$q add logout button to header
(Quick mode - must be explicitly requested)

$s implement user profile editing with avatar upload
(Standard mode - must be explicitly requested)

$c rebuild search system with filters, personalization, and analytics
(Complex mode with phases)

$e create customer self-service portal
(Epic with child tickets)
```

### Interactive Mode Features:
- **Conversational approach** - Asks targeted questions
- **Educational** - Teaches product thinking through practice
- **Adaptive** - Detects complexity and selects appropriate final mode
- **Smart questions** - Priority-weighted based on what's missing
- **Visual dashboard** - Shows ticket quality metrics

.

## ✅ Output Format

### Every Ticket Includes:
1. **Always in an artifact** (for easy copying)
2. **MCP tool notation** (which tool was used for analysis)
3. **Mode notation** (which mode was used)
4. **User Value statement** (why it matters)
5. **Business Goal** (measurable impact)
6. **Requirements** (outcome-focused, not technical)
7. **Success Criteria** (measurable checkboxes)
8. **Design links** (when applicable)
9. **Dependencies** (related tickets)
10. **Abstract symbols throughout** (❖, ◇, →, ✓, ⊗)

### Example Output Structure:
```markdown
MODE: $interactive → $s
TICKET TYPE: Feature
MCP USED: Cascade Thinking

### ❖ Search Filters

**User Value:** Find relevant products faster with smart filtering

**Business Goal:** Reduce search abandonment by 30%

---

## ◇ Requirements
- Filter by category, price, availability
- Results update instantly without refresh
- Mobile-responsive filter panel
- Clear all filters option

---

## → Designs & References
- [Figma - Search Filters](link)
- **Notice:** Mobile uses collapsible panel

---

## ✓ Success Criteria
- [ ] Filters work on all devices
- [ ] Results update in <300ms
- [ ] 30% reduction in abandonment
- [ ] Filter state persists during session

---

## ⊗ Dependencies
- Requires: Search API v2 (#1234)
- Blocks: Saved searches (#1235)
```

### Interactive Mode Dashboard:
```
📊 Interactive Mode Report
Overall Quality Score: 4.5/5 ⭐

✅ Ticket Structure Checklist:
✓ User value clearly stated
✓ Business goal measurable
✓ Requirements outcome-focused
✓ Success criteria verifiable
✓ Dependencies identified
✓ All symbols properly used
✓ 2-minute read test: PASS (1:45)

Product Management Insights:
• We chose $standard mode for clear scope
• Success criteria focus on user outcomes
• Requirements use WHAT not HOW language
```

.

## 🆘 Troubleshooting

### "It's not using any MCP tool"
- Check if MCPs are installed (look for 🔌 icon)
- The system works fine without them
- You'll see "MCP tools not available" notation

### "It's using the wrong MCP tool"
- The system chooses based on complexity indicators
- Interactive mode typically uses Cascade
- Simple, clear requests → Sequential

### "I don't want Interactive Mode"
- Explicitly specify your preferred mode: `$q`, `$s`, `$c`, or `$e`
- Interactive is only the default when no mode is specified

### "Too many/few thoughts being used"
- v2.1 adapts thought count to complexity
- Simple edits might use just 1 thought
- Complex epics might use 10+
- This is normal and optimized behavior

### "The ticket is too long/detailed"
- Use `$q` mode for simpler tickets
- Interactive mode helps find the right balance
- Remember: 2-minute read rule

### "How do I handle partial inputs?"
- System automatically enhances incomplete requests
- Extracts from screenshots and lists
- Marks assumptions with "Inferred:"
- Flags gaps with "Needs:"

### "Abstract symbols aren't showing"
- Symbols (❖, ◇, →, ✓, ⊗) should appear throughout
- Every major section needs appropriate symbol
- Check that you're using v2.1 or later

.

## 🎉 What's New in v2.1

1. **Interactive Mode (DEFAULT)** - Conversational ticket creation for everyone
2. **Partial Input Enhancement** - Intelligently handles incomplete requests
3. **Enhanced Symbol System** - Professional abstract symbols throughout
4. **Educational Layer** - Teaches product thinking through practice
5. **Smart Question Priority** - Asks only what's critical
6. **Visual Quality Dashboard** - Shows ticket quality metrics
7. **Improved MCP Selection** - Better matching of tool to complexity
8. **No Em Dash Rule** - Clearer punctuation throughout

The Dev Ticket Writer v2.1 democratizes product management by making professional ticket creation accessible to everyone through Interactive Mode, while maintaining the core principle: focus on WHAT and WHY, not HOW.