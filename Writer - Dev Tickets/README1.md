# Dev Ticket Writer - User Guide v2.0

## 🚀 What is This?

The Dev Ticket Writer system transforms any request into clear, actionable development tickets. Instead of vague requirements or technical jargon, you get tickets that communicate user value and business outcomes, letting developers focus on HOW to implement.

**Key Benefits:**
- Transform unclear requests into actionable tickets
- Communicate user value and business impact clearly
- Get consistent ticket format across your team
- Focus on WHAT and WHY, not HOW
- Save time with structured templates
- Professional presentation with icons in all modes
- **NEW: Intelligent MCP tool selection for optimal analysis**

**Key Principle:** If a ticket takes more than 2 minutes to read, it's too long.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Dev Ticket Writer v2"

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Writer - Dev Tickets - v2.0.0.md`
4. Save the project

### Step 3: Upload Reference Document
Upload the examples document to your project:
- `Dev Tickets - Examples & Patterns.md` (contains all ticket examples and patterns)

### Step 4: Start Writing Tickets!
Begin any conversation in the project, and Claude will transform your requests into proper dev tickets.

.

## 🧠 Enhanced Intelligence: Dual MCP Support

### What's New in v2.0?
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
- Requests mentioning "alternatives" or "options"
- Complex (`$c`) and Epic (`$e`) mode tickets
- Multi-phase implementations
- Unclear scope requiring exploration
- Comparing different solutions
- Features with interconnected dependencies

### Adaptive Thought Process

The system now uses a flexible approach:
- **Minimum:** 1 thought (for very simple requests)
- **Simple requests:** 1-2 thoughts
- **Standard features:** 2-3 thoughts
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

### Basic Usage
Simply describe what you need:
```
We need search filters for our product catalog
```

The system will:
1. Assess complexity
2. Choose appropriate MCP tool (if available)
3. Analyze with adaptive thought count
4. Generate the perfect ticket

### Mode Selection
The system has four modes for different complexity levels:

| Mode | Command | Use For | Typical MCP | Thoughts |
|------|---------|---------|-------------|----------|
| **Quick** | `$q` | Simple, single features | Sequential | 1-2 |
| **Standard** | `$s` (DEFAULT) | Most features and improvements | Sequential | 2-3 |
| **Complex** | `$c` | Multi-phase implementations | Cascade | 3-5 |
| **Epic** | `$e` | Major initiatives with child tickets | Cascade | 5+ |

### Mode Examples:
```
$q add logout button to header

$s implement user profile editing with avatar upload

$c rebuild search system with filters, personalization, and analytics

$e create customer self-service portal
```

.

## ✅ Output Format

### Every Ticket Includes:
1. **Always in an artifact** (for easy copying)
2. **MCP tool notation** (which tool was used for analysis)
3. **User Value statement** (why it matters)
4. **Business Goal** (measurable impact)
5. **Requirements** (outcome-focused, not technical)
6. **Success Criteria** (measurable checkboxes)
7. **Design links** (when applicable)
8. **Dependencies** (related tickets)
9. **Icons throughout** (for visual hierarchy in all modes)

### Example Output Structure:
```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking

### ❖ Search Filters

**User Value:** Find relevant products faster

**Business Goal:** Reduce search abandonment by 30%

---

## ◇ Requirements
- Filter by category, price, availability
- Results update instantly
- Mobile-responsive design

## → Design
- [Figma - Search Filters](link)

## ✓ Success Criteria
- [ ] Filters work on all devices
- [ ] Results update in <300ms
- [ ] 30% reduction in abandonment

## ⊗ Dependencies
- Requires: Search API v2 (#1234)
```

.

## 🆘 Troubleshooting

### "It's not using any MCP tool"
- Check if MCPs are installed (look for 🔌 icon)
- The system works fine without them
- You'll see "MCP tools not available" notation

### "It's using the wrong MCP tool"
- The system chooses based on complexity indicators
- You can hint at complexity: "explore alternatives" → Cascade
- Simple, clear requests → Sequential

### "Too many/few thoughts being used"
- v2.0 adapts thought count to complexity
- Simple edits might use just 1 thought
- Complex epics might use 10+
- This is normal and optimized behavior

### "The ticket is too long/detailed"
- Use `$q` mode for simpler tickets
- Default `$s` mode balances completeness and brevity
- Remember: 2-minute read rule

### "Missing design links"
- The system will note "Needs: Design mockups"
- Tickets can proceed with placeholder for designs
- Add actual links when available

### "Icons aren't showing in tickets"
- Icons should appear in ALL modes
- Every major section should have an icon
- Check that you're using v2.0 or later

.

## 🎉 What's New in v2.0

1. **Intelligent MCP Selection** - Automatically chooses the best thinking tool
2. **Flexible Thought Requirements** - Minimum 1 thought, scales with complexity
3. **Dual MCP Support** - Works with Sequential or Cascade Thinking MCPs
4. **Adaptive Analysis** - Thought count matches request complexity
5. **Enhanced Documentation** - Clear indication of which tool was used
6. **Backward Compatible** - Works without MCPs installed

The Dev Ticket Writer v2.0 brings intelligence to ticket creation, choosing the right analytical approach for each request while maintaining the core principle: focus on WHAT and WHY, not HOW.