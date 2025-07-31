# Branded Content Writer - User Guide v3.0

## 🚀 What is This?

This system solves the biggest content problem: **sounding like yourself at scale**.

Instead of staring at blank pages or publishing generic content, you describe what you need and get back 3 versions that actually sound like you. The secret? A mix of writing modes for different purposes, tones for different contexts, frameworks that structure your ideas, and **intelligent content planning** that adapts to complexity.

**Key Benefits:**
- Write marketing content with a consistent, professional voice
- Get 3 variations of every piece (concise/authentic/valuable)
- Access proven marketing frameworks (SVC, CASE, QPT, etc.)
- Create content that drives engagement and action
- Learn from a voice that balances data with humanity
- **NEW: Intelligent MCP tool selection for optimal content strategy**

→ Your personality + proven structures + smart planning = content that's on-brand.

.

## ⚡ Ready to level up?

This starter system creates on-brand content fast.

**Build it into an enterprise-ready content engine by adding:**

- Expanded library of frameworks, examples and case studies 
- Focus modes that adapt output to strategic themes such as sustainability, innovation or customer value
- Platform-specific guidelines, including frameworks, tone, and focus combination presets
- Improved request analysis, routing and response scaling guidelines
- Curated market, industry, and competitor research optimized for LLM integration
- Repositories of product or service information, either as knowledge base item or through custom MCP integration

.

## 🎨 PRO TIP: Make This YOUR Brand Voice!

**Transform this system into your personal or company brand voice using my [Prompt Improver](https://github.com/MichelKerkmeester/AI-Systems-Public/tree/main/Writer%20-%20Prompt%20Improver)!**

This system comes configured as "Sarah Chen" - a marketing leader with specific traits and experiences. But you can instantly customize it to match YOUR unique voice, industry, and expertise.

**Example customization prompt:**
```
$full Improve this prompt '''
Transform the Branded Content Writer system into a [YOUR ROLE] writer for [YOUR BRAND].

Current system: Sarah Chen, marketing leader, 10+ years, data-driven storytelling
Target system: [YOUR NAME/BRAND], [YOUR ROLE], [YOUR EXPERIENCE], [YOUR VOICE TRAITS]

Keep the framework structure and 3-variation output system.
'''
```

See the full "Customization" section below for detailed instructions.

.

## 🧠 Enhanced Intelligence: Dual MCP Support

### What's New in v3.0?
The Branded Content Writer now intelligently chooses between two thinking tools based on your content's complexity:

1. **Sequential Thinking MCP** - For straightforward, linear content creation
2. **Cascade Thinking MCP** - For complex content requiring exploration of multiple approaches

The system automatically selects the best tool and adapts the number of analysis thoughts (minimum 1, scaling up based on complexity).

### Intelligent Selection Logic

**Sequential Thinking is chosen for:**
- Clear content requests with specified platform/format
- Write (`$w`) and Share (`$s`) modes with simple requirements
- Single framework applications
- Direct edits or rewrites
- Straightforward marketing insights
- Quick social media posts

**Cascade Thinking is chosen for:**
- Improve (`$i`) mode with VEST evaluation and refinement
- Unclear platform/audience requiring exploration
- Content mentioning "different approaches" or "variations"
- Complex campaign narratives
- Multiple framework options that could work
- Strategic content requiring angle exploration
- Creating 3 variations that need different strategic approaches

### Adaptive Thought Process

The system now uses a flexible approach:
- **Minimum:** 1 thought (for very simple edits)
- **Simple posts:** 1-2 thoughts
- **Standard content:** 2-3 thoughts
- **Complex narratives:** 3-5 thoughts with potential branching
- **Full improvement cycles:** 5+ thoughts with multiple exploration branches

.

## 📋 Quick Setup in Claude

### Step 1: Create a New Project
1. Go to [claude.ai](https://claude.ai)
2. Click "Projects" in the sidebar
3. Click "Create project"
4. Name it "Branded Content Writer v3" (or your customized version)

### Step 2: Add the System Instructions
1. In your project, click "Edit project details"
2. Find the "Custom instructions" section
3. Copy and paste the main system file: `Writer - Branded Content - v3.0.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Upload these documents to your project knowledge base:
- `Artifact Standards & Templates.md` (mandatory artifact structures - update with MCP notation)
- `Copywriter Frameworks.md` (all writing frameworks)

### Step 4: Start Creating!
Begin any conversation in the project, and Claude will write in the configured brand voice (default: Sarah Chen), delivering marketing content in artifacts with 3 variations.

.

## 🔧 Installing MCP Tools (Optional but Recommended)

Both tools work independently, so you can install one or both based on your needs.

### Sequential Thinking MCP Installation

**For straightforward content creation:**

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

**For complex content strategy with branching:**

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

**Note**: The system works without these tools but provides enhanced content planning when available.

.

## 🎯 How to Use

### Basic Usage
Simply describe what you need:
```
Write a LinkedIn post about the importance of A/B testing
```

The system will:
1. Assess complexity
2. Choose appropriate MCP tool (if available)
3. Analyze with adaptive thought count
4. Generate content with 3 variations

### Mode Selection
The system has four specialized modes:

| Mode | Command | Use For | Example Output Style | Typical MCP | Thoughts |
|------|---------|---------|---------------------|-------------|----------|
| **Write** | `$write` or `$w` (DEFAULT) | General content needs | Balanced marketing insights | Sequential | 2-3 |
| **Share** | `$share` or `$s` | Knowledge & insights | "Here's what worked..." | Sequential | 2-3 |
| **Connect** | `$connect` or `$c` | Building relationships | "Ever notice how we all..." | Sequential/Cascade | 2-4 |
| **Improve** | `$improve` or `$i` | Optimize content | Full VEST evaluation + refined versions | Cascade | 3-5+ |

### Mode Examples:
```
$write a post about marketing automation best practices

$share insights from our email campaign

$connect with other marketers about budget constraints

$improve [creates content then automatically refines it]
```

.

## 🎨 Tone Modifiers

### Add Tones for Different Contexts
Combine modes with tones for precise voice control:

| Tone | Code | Best For |
|------|------|----------|
| **Natural** | `$natural` (DEFAULT) | Authentic voice with genuine uncertainty |
| **Casual** | `$casual` | Social media, team updates |
| **Technical** | `$technical` | Data reports, analytics |
| **Educational** | `$educational` | Tutorials, guides |
| **Minimal** | `$minimal` | Ad copy, headlines |

### Tone Combination Examples:
```
$write + $casual a social media post about our new feature

$share + $casual insights about influencer marketing

$write + $technical on setting up GA4 conversion tracking

$connect + $educational about marketing measurement challenges
```

.

## ✅ Output Format

### Every Response Includes:
1. **Always in an artifact** (text/markdown format)
2. **Mandatory structure with metadata:**
   - Framework used (if applicable)
   - Mode (write/share/connect/improve)
   - Tone (natural by default)
   - Platform (if specified)
   - Context (from your query)
   - **MCP USED** (which tool was used for planning)
3. **3 variations minimum:**
   - **Most concise:** Fewest words, maximum impact
   - **Most authentic:** Natural Sarah voice with stories
   - **Most valuable:** Maximum actionable takeaway

### Example Output Structure:
```
FRAMEWORK: SVC (Situation•Value•Connection)
MODE: $write
TONE: $natural
PLATFORM: LinkedIn
CONTEXT: A/B testing importance for marketers
MCP USED: Sequential Thinking

Stock photos killed our CTR. Real employees increased it by 47%.

---

## Variations

### Most concise:
Stock photos killed our CTR. Real employees: +47%. You?

### Most authentic:
Client fought us on using employee photos vs stock. We A/B tested anyway. 
Real faces won by 47%. Sometimes "unprofessional" is exactly what people 
want. When's your last visual audit?

### Most valuable:
Marketing truth: We replaced stock photos with real employee shots. CTR 
jumped 47%, cost per lead dropped 31%. Test: Swap one hero image for 
authentic photo. Track for 2 weeks. Share results?
```

.

## 🎯 Full Customization Guide

### Transform Into ANY Brand Voice
The Branded Content Writer system is fully customizable. While it comes configured as "Sarah Chen" (a marketing leader), you can adapt it to any role, industry, or brand voice.

**Quick customization with [Prompt Improver](https://github.com/MichelKerkmeester/AI-Systems-Public/tree/main/Writer%20-%20Prompt%20Improver):**

```
$full Improve this prompt '''
Transform the Branded Content Writer system (currently configured as Sarah Chen, marketing leader) into a [YOUR ROLE] writer system for [YOUR COMPANY/BRAND].

Key changes needed:
- Replace Sarah Chen with [YOUR NAME/BRAND]
- Change from marketing focus to [YOUR INDUSTRY/FOCUS]
- Adjust experience from "10+ years in marketing" to [YOUR BACKGROUND]
- Modify voice characteristics from "data-driven storytelling" to [YOUR VOICE TRAITS]
- Keep the framework structure but adapt examples to [YOUR FIELD]
- Maintain the 3-variation output system
'''
```

**Example for a Technical Writer:**
```
$full Improve this prompt '''
Transform the Branded Content Writer system into a technical documentation writer system for a developer-focused SaaS company.

Key changes:
- Replace marketing storytelling with technical clarity
- Change campaign examples to API documentation examples
- Adjust tone from "human stories" to "developer-friendly precision"
- Keep the quality frameworks but optimize for technical accuracy
'''
```

.

## 💡 Pro Tips

### 1. Specify Platform for Optimized Content
```
Write a Twitter thread about content marketing ROI

Create an Instagram caption for our new campaign launch

Draft a LinkedIn article about marketing automation
```

### 2. Use Frameworks Directly
Request specific frameworks when you know what you need:
```
Use the CASE framework to tell our product launch story

Apply QPT to challenge assumptions about email marketing

Create a PATH framework story about fixing our attribution
```

### 3. The Magic of $improve Mode
This mode automatically:
- Creates initial content
- Evaluates it with the 20-point VEST framework
- Identifies weaknesses
- Delivers refined versions
- Shows you exactly what was improved
- **Uses Cascade Thinking to explore multiple improvement strategies**

Perfect for high-stakes content!

### 4. Complex Content Benefits from Cascade Thinking
When dealing with unclear requirements or needing multiple strategic approaches, the system may use Cascade Thinking to:
- Explore different framework options
- Test various tone combinations
- Branch into specialized content strategies
- Ensure the best possible variations

### 5. Natural Voice is Default
The system defaults to `$natural` tone - authentic voice with:
- Genuine uncertainty ("Still figuring out why...")
- Conversational fragments
- Real campaign stories
- Team credit naturally included

.

## 🆘 Troubleshooting

### "It's not using any MCP tool"
- Check if MCPs are installed (look for 🔌 icon)
- The system works fine without them
- You'll see "MCP tools not available" notation

### "It's using the wrong MCP tool"
- The system chooses based on complexity indicators
- `$improve` mode typically uses Cascade Thinking
- Simple content uses Sequential Thinking
- This is optimized behavior

### "Too many/few thoughts being used"
- v3.0 adapts thought count to complexity
- Simple edits might use just 1 thought
- Complex content might use 5+
- This is normal and optimized behavior

### "The content feels generic"
- Add more context about your campaign/audience
- Specify platform for optimized voice
- Use specific frameworks for structure
- Include real metrics/examples in your request

### "Wrong tone for my brand"
- See customization guide above
- Adjust Sarah Chen's voice to match yours
- Keep the system structure, change the personality

.

## 🎉 What's New in v3.0

1. **Intelligent MCP Selection** - Automatically chooses the best thinking tool
2. **Flexible Thought Requirements** - Minimum 1 thought, scales with complexity
3. **Dual MCP Support** - Works with Sequential or Cascade Thinking MCPs
4. **Adaptive Analysis** - Thought count matches content complexity
5. **Enhanced Documentation** - Clear indication of which tool was used
6. **Mode-Specific Optimization** - Each mode optimized for its use case
7. **Strategic Branching** - Complex content explores multiple approaches
8. **Backward Compatible** - Works without MCPs installed

The Branded Content Writer v3.0 brings intelligence to content creation, choosing the right analytical approach for each request while maintaining Sarah Chen's authentic marketing voice and the proven 3-variation system.