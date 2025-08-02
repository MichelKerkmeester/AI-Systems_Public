# Branded Content Writer - User Guide v3.0.0

A comprehensive system that transforms marketing challenges into authentic content through guided conversation, proven frameworks, and intelligent content planning. Features 5 operating modes, visual progress tracking, and Sarah Chen's collaborative marketing voice.

## 🆕 What's New in v3.0.0

- **Interactive Mode as Default**: Conversational content creation that uncovers campaign stories
- **5 Operating Modes**: From general writing ($write) to full optimization ($improve)
- **Visual VEST Dashboard**: Real-time quality scoring and improvement metrics
- **Marketing Story Discovery**: Finds failures, team wins, and genuine learnings
- **MCP Integration**: Supports Sequential and Cascade Thinking tools
- **Framework Library**: 9 proven marketing frameworks organized by complexity

.

## Overview

The Branded Content Writer helps marketers create compelling content that drives results. With Sarah Chen's authentic voice, strategic frameworks (SVC, CASE, PATH), and intelligent MCP selection, it delivers professional-grade marketing content with genuine human connection.

## ✨ Key Features

- **5 Specialized Modes**: $interactive (default), $write, $share, $connect, $improve
- **9 Marketing Frameworks**: Simple (SVC, QPT, DER), Medium (CASE, PATH, REAL), Complex (STORY, GUIDE, HELP)
- **Intelligent MCP Selection**: Automatic choice between Sequential and Cascade thinking
- **Visual Progress Tracking**: VEST scoring with improvement metrics
- **Campaign Story Mining**: Uncovers failures and team contributions
- **Triple-Variation Output**: Concise, Authentic, and Valuable versions
- **Natural Imperfections**: Preserves conversational rough edges
- **Artifact-Based Delivery**: All content in reusable markdown artifacts

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "Branded Content Writer v3.0"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Writer - Branded Content - v2.1.0.md`
4. Save the project

### Step 3: Upload Supporting Documents
Add these to your project's knowledge base:
- `Artifact Standards & Templates.md`
- `Copywriter Frameworks.md`
- `Interactive Mode.md`

### Step 4: Start Creating Content
Simply describe what you need or let interactive mode guide you:
```
Need help with email campaign copy
$write a LinkedIn post about A/B testing
$share insights from our failed product launch
$improve make this sound less corporate
```

.

## 🎛️ Operating Modes

| Mode | Activation | Purpose | Best For | MCP Usage |
|------|------------|---------|----------|-----------|
| **$interactive** | `$interactive` or `$int` (DEFAULT) | Guided creation with questions | First-timers, story discovery | Cascade (3-5+ thoughts) |
| **$write** | `$write` or `$w` | General content creation | Quick marketing copy | Sequential (2-3 thoughts) |
| **$share** | `$share` or `$s` | Knowledge & insights | Sharing learnings | Sequential (2-3 thoughts) |
| **$connect** | `$connect` or `$c` | Community building | Engagement posts | Sequential/Cascade (2-4 thoughts) |
| **$improve** | `$improve` or `$i` | Optimize existing copy | Guaranteed 18+ VEST score | Cascade (3-5+ thoughts) |

.

## 🏗️ Core Frameworks

### Simple Frameworks (3-Part)
- **SVC**: Situation • Value • Connection
- **QPT**: Question • Perspective • Takeaway
- **DER**: Do • Example • Result

### Medium Frameworks (4-Part)
- **CASE**: Context • Action • Stakes • Evolution
- **PATH**: Problem • Approach • Twist • Harvest
- **REAL**: Recognize • Explore • Apply • Learn

### Complex Frameworks (5+ Parts)
- **STORY**: Setup • Tension • Opportunity • Resolution • Yes-And
- **GUIDE**: Goal • Understand • Install • Demo • Extend
- **HELP**: Hook • Explain • List • Practice

.

## 📊 Visual Dashboard Example

```
📊 Marketing Copy Effectiveness Report
Overall Score: 19/20 (VEST Framework)

Value Breakdown:
V - Value Delivery ████████░░ 90% (Clear reader benefit)
E - Economy       ████████░░ 80% (Could trim 10%)
S - Sound         ██████████ 100% (Perfect Sarah voice)
T - Truth         ██████████ 100% (Data + humility)

Marketing Excellence:
✅ Story Arc - Problem → discovery → insight flows naturally
✅ Authenticity - Failure included, team credited
✅ Data Integration - Numbers support narrative
✅ Voice Consistency - Sounds like coffee chat
✅ Natural Imperfection - "Still figuring out" included

Framework Learning:
📚 Why PATH: Your story had a clear journey with unexpected discovery
💡 Key principle: The twist makes it memorable
🎯 Use this when: You learned something surprising
```

.

## 🤖 Interactive Mode

Perfect for discovering your marketing story:
- Asks about campaign challenges and wins
- Uncovers failures worth sharing
- Identifies team members to credit
- Builds content through conversation
- Teaches framework selection

Example:
```
User: $interactive
AI: "Hey! Let's create marketing content that actually works. What marketing challenge are you facing?"
```

.

## 📈 Quality System (VEST)

### VEST Framework (20 Points)
- **V**alue: Helps readers improve their marketing
- **E**conomy: Every sentence necessary
- **S**ound: Natural conversation tone
- **T**ruth: Specific examples and data

### Scoring Bands
- **18-20**: Ship immediately
- **15-17**: Quick polish needed
- **12-14**: Systematic revision
- **Below 12**: Complete rewrite

.

## 🔧 Technical Details

### MCP Selection Logic
- **Interactive mode** → Always Cascade (3-5+ thoughts)
- **Standard content** → Sequential (2-3 thoughts)
- **Complex narratives** → Cascade (3-5 thoughts)
- **Full improvement** → Cascade (5+ thoughts with branches)

### Voice Characteristics
Sarah Chen's authentic markers:
- Team credit ("Our designer spotted...")
- Process transparency ("Took 6 tests to figure out...")
- Genuine uncertainty ("Still not sure why...")
- Natural fragments. For emphasis.
- Data with stories ("CTR jumped 47%")

### Artifact Standards
- Always uses `text/markdown` type
- Includes framework and MCP notation
- 3 variations mandatory
- Complete structure every time

.

## 📚 Example Transformations

### Campaign Story Discovery
**User:** "We ran an email campaign"
**Interactive Mode:** "Congrats! What was broken before this campaign? What almost went wrong?"
**Result:** Story about accidental test email that revealed winning formula

### Quick Social Post
**User:** "$write LinkedIn post about stock photos"
**Result:** 
- Most concise: "Stock photos killed our CTR. Real employees: +47%. You?"
- Most authentic: "Client fought us on employee photos. We tested anyway..."
- Most valuable: "Marketing truth: Replace stock with real faces. CTR +47%..."

### Knowledge Sharing
**User:** "$share what we learned about pop-ups"
**Result:** PATH framework story about discovering exit intent vs immediate pop-ups

.

## 🔧 Installing MCP Tools (Recommended)

The system intelligently selects between these based on content complexity. Choose either Docker (stable) or NPX (quick) installation:

### Option A: AI-Powered Docker Setup (Recommended)

**Prerequisites:**
- Docker Desktop installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Claude Desktop app ([Download Claude](https://claude.ai/download))

**AI-Assisted Installation:**

Copy this prompt to Claude, ChatGPT, or any AI assistant:

```
Help me set up Docker containers for the Branded Content Writer MCP tools.

I need to:
1. Create a directory at "$HOME/MCP Servers"
2. Clone these repos:
   - https://github.com/arben-adm/mcp-sequential-thinking.git
   - https://github.com/drewdotpro/cascade-thinking-mcp.git
3. Create a docker-compose.yml file with services for both
4. Configure Claude Desktop's claude_desktop_config.json
5. Start the containers with docker-compose

I'm on [Windows/Mac/Linux]. Please give me the exact commands to run.
```

The AI will provide step-by-step commands for your operating system.

**Verification:**
1. Check Docker Desktop for 2 running containers
2. Look for the 🔌 icon in Claude Desktop showing available tools
3. Test with: "$write a post about marketing automation"

### Option B: NPX Installation (Quick but Less Stable)

Add to Claude Desktop config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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

Save and restart Claude Desktop.

.

## 🎨 Customization Guide

### Transform Into ANY Brand Voice

The system comes configured as "Sarah Chen" but is fully customizable using the [Prompt Improver](https://github.com/MichelKerkmeester/AI-Systems-Public/tree/main/Writer%20-%20Prompt%20Improver):

```
$full Improve this prompt '''
Transform the Branded Content Writer system into a [YOUR ROLE] writer for [YOUR BRAND].

Current: Sarah Chen, marketing leader, 10+ years, collaborative voice
Target: [YOUR NAME/BRAND], [YOUR ROLE], [YOUR EXPERIENCE], [YOUR VOICE TRAITS]

Keep the framework structure and 3-variation output system.
Adapt examples to [YOUR INDUSTRY].
'''
```

**Example for Tech Startup Founder:**
```
Transform into a startup founder voice:
- Replace marketing focus with product/growth focus
- Change from team credit to startup hustle stories
- Adjust from "still figuring out" to "rapidly iterating"
- Keep frameworks but use startup examples
```

.

## 💡 Pro Tips

### 1. Let Interactive Mode Guide You
Default mode asks the right questions to uncover great stories:
- What went wrong? (Finds authentic moments)
- Who helped? (Natural team credit)
- What surprised you? (Genuine insights)

### 2. Specify Platform for Optimization
```
Write a Twitter thread about conversion optimization
Create LinkedIn post celebrating team win
Draft email nurture sequence intro
```

### 3. Use Frameworks Directly
When you know what you need:
```
Use CASE framework for our product launch story
Apply PATH to explain our pivot
Create QPT post challenging marketing assumptions
```

### 4. The Magic of $improve Mode
- Creates initial content
- Evaluates with 20-point VEST framework
- Automatically refines weak areas
- Guarantees 18+ score
- Shows exactly what improved

### 5. Embrace Natural Imperfections
Best performing content includes:
- "Still testing why this works..."
- "Our intern spotted the pattern"
- "Took us 6 months to figure out"
- Fragments. For emphasis.

.

## 🆘 Troubleshooting

### MCP Connection Issues
- **Docker not running**: Start Docker Desktop
- **Can't connect**: Restart Claude Desktop
- **Wrong directory**: Check you're in "$HOME/MCP Servers"
- **Permission errors**: Run terminal as administrator (Windows) or use sudo (Mac/Linux)

### Common Setup Problems
- **"Command not found"**: Ensure Node.js is installed for NPX method
- **Containers won't start**: Check Docker Desktop is running
- **Tools not showing**: Restart Claude Desktop after config changes
- **Rate limits**: Both tools handle this gracefully with retries

### Content Issues
- **Too polished**: Let natural imperfections through
- **Missing story**: Use interactive mode to dig deeper
- **No team credit**: Ask "Who contributed to this?"
- **Lacks data**: Include specific metrics
- **Wrong voice**: Check Sarah's DO's and DON'T's

### Getting Help
- For Docker issues: Check container logs in Docker Desktop
- For NPX issues: Check Claude Desktop logs
- For content issues: Use $improve mode for automatic enhancement

.

## ⚠️ Important Notes

- **Always includes failures** - Authenticity builds trust
- **Credits team naturally** - "Our designer noticed..."
- **No em dashes** - Uses commas, colons, or periods
- **Works without MCPs** - But enhanced with them
- **Preserves rough edges** - Perfect polish feels fake

## 📦 Version History

- **v3.0.0**: Interactive mode default, VEST scoring, enhanced MCP integration
- **v2.0.0**: Added framework library and improve mode
- **v1.0.0**: Initial Sarah Chen voice implementation

## 🎯 Key Principles

1. **Great marketing admits what didn't work** - Failure stories teach
2. **Team credit makes everyone look good** - Collaboration beats ego
3. **Natural voice outperforms polish** - Authenticity drives engagement
4. **Process transparency builds trust** - Show the messy middle
5. **Data needs human context** - Numbers alone don't connect

.

## 📚 Other Resources

- [MCP Protocol Guide](https://modelcontextprotocol.io/)
- [Docker Desktop Help](https://docs.docker.com/desktop/)
- [Sequential Thinking MCP](https://github.com/arben-adm/mcp-sequential-thinking)
- [Cascade Thinking MCP](https://github.com/drewdotpro/cascade-thinking-mcp)
- [Prompt Improver](https://github.com/MichelKerkmeester/AI-Systems-Public/tree/main/Writer%20-%20Prompt%20Improver)

---

*Transform marketing challenges into human stories. Create content that actually works.*