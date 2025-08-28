# ClickUp Agent - User Guide v2.1.0

The ClickUp Agent transforms natural language into organized ClickUp workspaces while actively challenging unnecessary complexity. Through intelligent conversation with user-controlled thinking depth, it builds minimal viable structures that actually get used, not admired.

## 📋 Table of Contents

- [🆕 What's New in v2.1.0](#-whats-new-in-v210)
- [✨ Key Features](#-key-features)
- [🚀 Quick Setup](#-quick-setup)
- [🧠 How It Works](#-how-it-works)
- [💬 Example Interactions](#-example-interactions)
- [📊 What Gets Built](#-what-gets-built)
- [🔧 Installing ClickUp MCP](#-installing-clickup-mcp)
- [🆘 Troubleshooting](#-troubleshooting)
- [⚠️ Important Notes](#️-important-notes)
- [📦 Version History](#-version-history)
- [📚 Resources](#-resources)

.

## 🆕 What's New in v2.1.0

### Major Clarifications
- **API Reality Documented**: Clear distinction between using existing fields vs creating new
- **Automation Limitations**: Explains can only trigger existing automation rules
- **Document Support Added**: Full document management when enabled
- **Workaround Patterns**: Clear alternatives for unsupported features
- **Better Error Messages**: Explains API limitations transparently

### Updated Features
- **Field Management**: Uses existing custom field definitions only
- **Automation Handling**: Works with existing rules, cannot create new
- **Document Operations**: Create/update documents and pages (when enabled)
- **Recurring Tasks**: Provides workarounds (not supported by API)
- **Template Alternatives**: Copy existing tasks instead

.

## ✨ Key Features

### Core Capabilities
- **Natural Language First**: Describe what you want in plain English
- **Complexity Challenges**: Questions unnecessary features before building
- **User-Controlled Thinking**: You choose analysis depth (1-10 rounds)
- **Pattern Learning**: Adapts to your simplicity preferences
- **API Transparency**: Clear about what can and cannot be done
- **Document Management**: Create/edit documents when enabled
- **Visual Progress**: Clear structure previews and metrics
- **Educational Insights**: Explains API limitations and workarounds
- **Error Recovery**: REPAIR protocol handles all issues gracefully
- **Performance Optimized**: Built for real-world usage limits

### What Gets Challenged
- 🤔 **Multi-space systems** → "Single space clearer?"
- 🤔 **Many custom fields** → "Which existing fields to use?"
- 🤔 **New automation rules** → "Can use existing or manual?"
- 🤔 **Deep hierarchies** → "Would flat structure work?"
- 🤔 **Unsupported features** → "Here's a workaround..."

### API Realities
| Feature | Can Do | Cannot Do | Workaround |
|---------|--------|-----------|------------|
| **Custom Fields** | ✅ Use existing fields | ❌ Create new definitions | Request from admin |
| **Automations** | ✅ Trigger existing | ❌ Create new rules | Manual process |
| **Templates** | ✅ Copy tasks | ❌ Create templates | Duplicate existing |
| **Recurring** | ❌ Not supported | ❌ API limitation | Create multiple |
| **Documents** | ✅ Full support (if enabled) | ⚠️ Needs config | Enable in MCP |
| **Attachments** | ✅ Up to 10MB | ❌ Larger files | Use external URLs |

.

## 🚀 Quick Setup

### Step 1: Create a Claude Project
1. Go to claude.ai
2. Click "Projects" in sidebar
3. Click "Create project"
4. Name it "ClickUp Agent v2.1"

### Step 2: Add System Instructions
1. In your project, click "Edit project details"
2. Find "Custom instructions" section
3. Copy and paste: `Agent - MCP - ClickUp - v2.1.0.md`
4. Save the project

### Step 3: Upload Reference Documents
Add these updated documents to your project:
- `Agent - MCP - ClickUp - v2.1.0.md` (Main system with API clarity)
- `ClickUp - ATLAS Thinking Framework - v1.0.0.md` (Thinking methodology)
- `ClickUp - Interactive Intelligence - v2.0.0.md` (Conversational interface)
- `ClickUp - Patterns & Workflows - v2.0.0.md` (Operation patterns)
- `ClickUp - MCP Knowledge - v1.1.0.md` (Updated with API limits)
- `README - v2.1.0.md` (This guide)

### Step 4: Get Your ClickUp API Key
1. Go to [ClickUp Settings](https://app.clickup.com/settings/apps)
2. Click "Apps" in the left sidebar
3. Generate a personal API token
4. Copy the token for MCP configuration

### Step 5: Install ClickUp MCP (With Optional Features)
Follow the installation guide below, including optional document support.

### Step 6: Start Creating (Within API Limits!)
```
organize my tasks              # Uses existing fields
create sprint board            # Works with what exists
set up CRM                     # Maps to available fields
enable documents               # If configured
help me with projects          # Guides within limits
```

.

## 🧠 How It Works

### ATLAS Thinking Framework with API Awareness

Every request goes through 5 phases with API reality checks:

**A - Assess & Challenge**
- Understand request
- Check if API supports it
- Verify fields exist
- Check user patterns

**T - Transform to Minimal**
- Convert to API-possible version
- Map to existing fields
- Identify workarounds for unsupported

**L - Layer with Scrutiny**
- Add only what API allows
- Use existing structures
- Challenge each addition

**A - Assess Impact**
- Check performance implications
- Validate against API limits
- Ensure scalability

**S - Synthesize Solution**
- Deliver API-compliant solution
- Document limitations
- Provide workarounds

### API Reality Levels

**Fully Supported ✅**
- Task CRUD operations
- Workspace hierarchy
- Comments and attachments (≤10MB)
- Time tracking
- Document management (if enabled)

**Limited Support ⚠️**
- Custom fields (existing only)
- Automation (trigger only)
- Bulk operations (20 max)
- Large files (use URLs)

**Not Supported ❌**
- Field definition creation
- Automation rule creation
- Recurring tasks
- Templates
- Dashboards/Reports
- Goals/Portfolios

.

## 💬 Example Interactions

### Working with Existing Fields
```
User: create project tracker with custom fields

System: How many thinking rounds should I use? (1-10)
Note: I can only use existing custom fields in your workspace
Recommended: 3 rounds (using existing fields)

User: 3

System: Let me check what fields exist in your workspace...

I found these existing custom fields:
• Priority (dropdown)
• Client (text)
• Budget (money)
• Phase (dropdown)
• Due Date (date)

Building project tracker with available fields...
✅ Created with existing fields!

Need different fields? Ask your workspace admin to create them.
```

### Automation Limitation Example
```
User: set up automated task assignment

System: I cannot create new automation rules (API limitation).

Let me check existing automations...
Found: "Auto-assign by priority"

Options:
1. Use this existing automation
2. Set up manual assignment process
3. Request new automation from admin

Which works for you?

User: use existing

System: ✅ Configured to use existing auto-assign automation!
```

### Document Management (When Enabled)
```
User: create project documentation

System: I can create documents if enabled in MCP!

Checking configuration...
✅ Document support is enabled

Creating document structure:
• Project overview page
• Requirements section
• Timeline section
• Resources section

All in markdown format.

Building documentation...
✅ Document created successfully!
```

### Unsupported Feature with Workaround
```
User: create recurring weekly team meeting

System: Recurring tasks aren't supported by the API.

Here are good alternatives:
1. Create next 4 weekly meetings now
2. Set a reminder to create more monthly
3. Use ClickUp's UI for true recurring

Which approach works?

User: create 4 weeks

System: Creating 4 weekly meeting tasks...
✅ Created meetings for:
• Jan 15 - Team Meeting
• Jan 22 - Team Meeting
• Jan 29 - Team Meeting
• Feb 5 - Team Meeting

Set a reminder to create more on Feb 1st!
```

.

## 📊 What Gets Built

### Within API Capabilities (Reality-Based)

**Task Management:**
```
API Compliant Version:
├── Single task list
├── Uses existing custom fields
├── Triggers existing automations
└── Standard views

NOT creating new field definitions
NOT creating automation rules
NOT setting up recurring tasks
```

**Project System:**
```
What Gets Built:
├── Project list with existing fields
├── Task list with relationships
├── Manual workflows documented
└── Existing automation triggers

What Doesn't:
• New custom field types
• New automation rules
• Custom templates
• Analytics dashboards
```

**Document Structure (If Enabled):**
```
When DOCUMENT_SUPPORT=true:
├── Markdown documents
├── Multiple pages
├── Basic formatting
└── Update capabilities

Requires MCP configuration
```

### Performance Limits (Enforced)

| Element | Recommended | Maximum | API Reality |
|---------|-------------|---------|-------------|
| **Items per list** | <1,000 | 5,000 | Hard limit |
| **Custom fields** | Existing only | 10 used | Cannot create new |
| **Bulk batch** | 20 items | 20 items | API limit |
| **Attachments** | <5MB | 10MB | Use URLs for larger |
| **API calls** | 30/min | 60/min | Rate limited |

.

## 🔧 Installing ClickUp MCP

### Complete Setup with Document Support

#### Option A: Full-Featured Docker Setup (Recommended)

```dockerfile
# Dockerfile
FROM node:18-alpine
WORKDIR /app
RUN npm install -g @clickup/mcp-server-clickup
CMD ["clickup-mcp"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  clickup-mcp:
    build: .
    environment:
      - CLICKUP_API_KEY=${CLICKUP_API_KEY}
      - CLICKUP_TEAM_ID=${CLICKUP_TEAM_ID}
      - DOCUMENT_SUPPORT=true  # Enable documents
      - LOG_LEVEL=info
    restart: unless-stopped
```

#### Option B: NPM with Full Configuration

```bash
# Install globally
npm install -g @clickup/mcp-server-clickup

# Verify installation
clickup-mcp --version
```

Claude Desktop config with all features:
```json
{
  "mcpServers": {
    "clickup": {
      "command": "clickup-mcp",
      "env": {
        "CLICKUP_API_KEY": "your-token-here",
        "CLICKUP_TEAM_ID": "your-team-id",
        "DOCUMENT_SUPPORT": "true",
        "LOG_LEVEL": "info"
      }
    }
  }
}
```

#### Option C: Quick Test Setup

```json
{
  "mcpServers": {
    "clickup": {
      "command": "npx",
      "args": ["-y", "@clickup/mcp-server-clickup"],
      "env": {
        "CLICKUP_API_KEY": "your-token-here",
        "CLICKUP_TEAM_ID": "your-team-id",
        "DOCUMENT_SUPPORT": "false"
      }
    }
  }
}
```

.

## 🆘 Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **"Cannot create field"** | API limitation | Use existing fields only |
| **"Automation failed"** | Trying to create new | Use existing automation |
| **"Recurring not working"** | Not supported | Create multiple tasks |
| **"Template error"** | Cannot create templates | Copy existing task |
| **"Dashboard missing"** | No API access | Use ClickUp UI directly |
| **"Document failed"** | Not enabled | Set DOCUMENT_SUPPORT=true |
| **"Large file error"** | >10MB limit | Upload to cloud, share URL |

### API Limitation Guidance

**When you need features the API doesn't support:**
1. **Check if it exists** - Many features must be created in ClickUp UI first
2. **Use workarounds** - System provides alternatives
3. **Request from admin** - Some features need workspace admin
4. **Use ClickUp directly** - Some features only available in UI

### Recovery Patterns (REPAIR)

**If feature not supported:**
1. **R**ecognize: System identifies API limitation
2. **E**xplain: Clear explanation of what's not possible
3. **P**ropose: Workaround options provided
4. **A**dapt: Apply chosen alternative
5. **I**terate: Implement workaround
6. **R**ecord: Learn preference

.

## ⚠️ Important Notes

### API Reality Check
- **Cannot create new** - Field definitions, automation rules, templates
- **Can only use existing** - Must be set up in ClickUp first
- **Performance matters** - Keep lists under 1000 items for speed
- **Attachments limited** - 10MB via API, use URLs for larger
- **Documents optional** - Requires configuration flag

### Best Practices
1. Check what fields exist before planning
2. Use existing automation when possible
3. Accept manual processes initially
4. Create multiple tasks instead of recurring
5. Use ClickUp UI for unsupported features
6. Enable documents if needed
7. Keep structures simple for performance

### Performance Guidelines
- **Simple operations**: 2-3 thinking rounds
- **Using existing fields**: 3-4 thinking rounds  
- **Complex mapping**: 5-6 thinking rounds
- **Unsupported features**: Immediate alternatives

.

## 📦 Version History

### v2.1.0 (Current)
- **API clarity**: Documents what can/cannot be created
- **Field reality**: Uses existing definitions only
- **Automation truth**: Triggers existing rules only
- **Document support**: Full management when enabled
- **Better errors**: Explains limitations clearly
- **Workarounds**: Provides alternatives for unsupported

### v2.0.0
- ATLAS Framework
- Challenge Mode
- Pattern Learning
- REPAIR Protocol

### v1.x
- Initial releases
- Basic functionality

.

## 📚 Resources

### Core Tools
- [ClickUp MCP Server](https://github.com/clickup/mcp-server-clickup) (Required)
- [Claude Projects](https://claude.ai) (Platform)

### Documentation
- [ClickUp API Docs](https://clickup.com/api) - See what's possible
- [MCP Protocol](https://modelcontextprotocol.io/) - Technical details
- [ClickUp Help](https://help.clickup.com/) - Platform features

### Understanding Limitations
- [ClickUp Custom Fields](https://help.clickup.com/hc/en-us/articles/6303472739863) - Must create in UI first
- [ClickUp Automations](https://help.clickup.com/hc/en-us/articles/6318924258711) - Create rules in UI
- [ClickUp Templates](https://help.clickup.com/hc/en-us/articles/6325298758039) - Not available via API

### Quick Links
- [ClickUp Login](https://app.clickup.com)
- [Get API Token](https://app.clickup.com/settings/apps)
- [Claude Desktop](https://claude.ai/download)
- [Workspace Settings](https://app.clickup.com/settings) - Create fields here

---

*Transform natural language into organized ClickUp workspaces. Work within API realities. Use existing structures wisely. Challenge unnecessary complexity. Provide clear workarounds for limitations.*