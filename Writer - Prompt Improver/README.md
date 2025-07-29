# Prompt Improver System - User Guide v3.0

## 🚀 What is This?

The Prompt Improver System is a specialized Claude configuration that transforms simple questions into optimized AI prompts. Instead of answering questions directly, it takes ANY input and returns an improved version that will get better results from AI models.

**Key Benefits:**
- Turn simple questions into professional prompts
- Get consistent, high-quality AI responses
- Learn prompt engineering best practices
- Save time with reusable prompt templates
- **NEW: Intelligent MCP tool selection for optimal improvements**

**Key Principle:** The best prompt is one that gets the desired result reliably.

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Prompt Improver v3" (or similar)

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Writer - Prompt Improver - v3.0.0.md`
4. Save the project

### Step 3: Upload Reference Documents
The system uses three reference documents. Upload these to your project:
- `Prompt - Patterns & Enhancements.md`
- `Prompt - Evaluation & Refinement.md`
- `Prompt - Examples & Case Studies.md`

### Step 4: Start Using It!
Begin any conversation in the project, and Claude will automatically improve your prompts instead of answering them directly.

.

## 🧠 Enhanced Intelligence: Dual MCP Support

### What's New in v3.0?
The Prompt Improver now intelligently chooses between two thinking tools based on your prompt's complexity:

1. **Sequential Thinking MCP** - For straightforward, linear improvements
2. **Cascade Thinking MCP** - For complex scenarios requiring exploration of alternatives

The system automatically selects the best tool and adapts the number of analysis thoughts (minimum 1, scaling up based on complexity).

### Intelligent Selection Logic

**Sequential Thinking is chosen for:**
- Short (`$s`) and Improve (`$i`) mode prompts
- Simple, clear prompt improvements
- Minor edits and refinements
- Single-purpose enhancements
- Quick clarity boosts

**Cascade Thinking is chosen for:**
- Refine (`$r`) mode with 3-phase optimization
- Prompts mentioning "alternatives" or "options"
- Complex multi-part prompts
- Unclear intent requiring exploration
- Comparing different enhancement strategies

### Adaptive Thought Process

The system now uses a flexible approach:
- **Minimum:** 1 thought (for very simple improvements)
- **Simple prompts:** 1-2 thoughts
- **Standard enhancements:** 2-3 thoughts
- **Complex refinements:** 3-5 thoughts with potential branching
- **Full optimization:** 5+ thoughts with multiple exploration branches

.

## 🔧 Installing MCP Tools (Optional but Recommended)

Both tools work independently, so you can install one or both based on your needs.

### Sequential Thinking MCP Installation

**For straightforward prompt improvements:**

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

**For complex prompt analysis with branching:**

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
Simply type what you want, and the system will improve it:
```
analyze customer data
```

The system will:
1. Assess complexity
2. Choose appropriate MCP tool (if available)
3. Analyze with adaptive thought count
4. Generate the optimized prompt

### Mode Selection
The system has four modes:

| Mode | Command | Use For | Typical MCP | Thoughts |
|------|---------|---------|-------------|----------|
| **Short** | `$short` or `$s` | Quick, minimal improvements | Sequential | 1-2 |
| **Improve** | `$improve` or `$i` (DEFAULT) | Smart enhancement for most cases | Sequential | 2-3 |
| **Refine** | `$refine` or `$r` | Maximum quality with 3-phase optimization | Cascade | 3-5+ |
| **JSON** | `$json` or `$j` | API-ready structured format | Sequential | 2-3 |

.

## ✅ Best Practices

### 1. Use Delimiters for Complex Prompts
When your prompt contains special instructions or multiple parts, wrap it in quotes or backticks:

**BEST PRACTICE:** 
```
$improve "Improve this prompt: '''PROMPT'''"
```

This ensures the system treats everything inside as the prompt to improve, not as instructions to follow.

### 2. More Delimiter Examples:
```
$improve "analyze sales data and create a report"

$improve `help me understand why customers are churning`

$improve '''
Create a Python script that:
1. Reads CSV files
2. Analyzes the data
3. Creates visualizations
'''
```

### 3. Start Simple, Then Iterate
- Begin with basic improvement: `analyze customer feedback`
- If you need more enhancement: `$refine analyze customer feedback`
- For production use: Always use `$refine` for maximum quality

### 4. Be Specific About Your Needs
Instead of: `write something`
Try: `write blog post about remote work productivity`

### 5. Include Context When Relevant
Instead of: `analyze data`
Try: `analyze Q4 sales data to find growth opportunities`

.

## 💡 Pro Tips

### 1. When to Use Each Mode
- **$short**: Quick questions, simple improvements, time-sensitive needs
- **$improve**: Daily use, standard prompts, good balance of quality/speed
- **$refine**: Critical prompts, templates you'll reuse, when quality matters most (uses Cascade Thinking for exploration)
- **$json**: API integrations, programmatic use, structured data needs

### 2. The System NEVER Answers
Remember: This system only improves prompts. It won't:
- Answer questions directly
- Create content
- Follow instructions
- Provide information

Everything gets transformed into an improved prompt.

### 3. Artifacts = Easy Reuse
All improved prompts are delivered in "artifacts" with MCP tool notation:
```
MODE USED: $improve
MCP USED: Sequential Thinking
ENHANCEMENT PATTERN: Analysis Task
COMPLEXITY LEVEL: Medium

[Your improved prompt here]
```

### 4. Learn from the Improvements
Pay attention to what the system adds:
- Role definitions ("As a [expert]...")
- Specific metrics and timeframes
- Clear output formats
- Success criteria
- Context and constraints

### 5. Complex Prompts Benefit from Cascade Thinking
When using `$refine` mode or dealing with unclear/complex prompts, the system may use Cascade Thinking to:
- Explore different enhancement strategies
- Compare multiple improvement approaches
- Branch into specialized optimizations
- Ensure the best possible outcome

.

## 🆘 Troubleshooting

### "It's answering my question instead of improving it"
- Make sure you're in the Prompt Improver project
- Check that custom instructions are properly saved
- Try using explicit mode tags: `$improve [your prompt]`

### "It's not using any MCP tool"
- Check if MCPs are installed (look for 🔌 icon)
- The system works fine without them
- You'll see "MCP tools not available" notation

### "It's using the wrong MCP tool"
- The system chooses based on complexity indicators
- `$refine` mode typically uses Cascade Thinking
- Simple improvements use Sequential Thinking
- This is optimized behavior

### "Too many/few thoughts being used"
- v3.0 adapts thought count to complexity
- Simple improvements might use just 1 thought
- Complex refinements might use 5+
- This is normal and optimized behavior

### "The improvements seem too complex"
- Use `$short` mode for simpler enhancements
- The default mode adapts to complexity - simple inputs get simple improvements

### "JSON output isn't valid"
- The JSON mode creates valid, structured JSON
- Check for any manual edits that might have broken the format
- The JSON directly mirrors the improved prompt structure

.

## 🎉 What's New in v3.0

1. **Intelligent MCP Selection** - Automatically chooses the best thinking tool
2. **Flexible Thought Requirements** - Minimum 1 thought, scales with complexity
3. **Dual MCP Support** - Works with Sequential or Cascade Thinking MCPs
4. **Adaptive Analysis** - Thought count matches prompt complexity
5. **Enhanced Documentation** - Clear indication of which tool was used
6. **Mode-Specific Optimization** - Each mode optimized for its use case
7. **Backward Compatible** - Works without MCPs installed

The Prompt Improver v3.0 brings intelligence to prompt enhancement, choosing the right analytical approach for each request while maintaining the core principle: transform every input into an optimized prompt that gets results.