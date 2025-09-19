# ClickUp & Notion - Patterns & Workflows - v0.100

Complete pattern library and workflow specifications for natural language productivity operations (Notion and ClickUp) with native API integration.

## 📋 Table of Contents
1. [📋 OVERVIEW](#1-📋-overview)
2. [🔌 MCP VERIFICATION PATTERNS](#2-🔌-mcp-verification-patterns)
3. [🎯 INTENT PATTERNS](#3-🎯-intent-patterns)
4. [🔄 WORKFLOW PATTERNS](#4-🔄-workflow-patterns)
5. [🗏 STRUCTURE PATTERNS](#5-🗏-structure-patterns)
6. [📊 DATABASE & LIST PATTERNS](#6-📊-database--list-patterns)
7. [⚡ OPTIMIZATION PATTERNS](#7-⚡-optimization-patterns)
8. [🔄 CROSS-PLATFORM PATTERNS](#8-🔄-cross-platform-patterns)
9. [🧠 THINKING PATTERNS](#9-🧠-thinking-patterns)
10. [🚀 COMPLETE WORKFLOWS](#10-🚀-complete-workflows)
11. [⚡ EMERGENCY PATTERNS](#11-⚡-emergency-patterns)

---

## 1. 📋 OVERVIEW

This document defines all pattern recognition and workflow orchestration logic for the ClickUp & Notion Helper. Each pattern maps natural language to specific operations with smart defaults and appropriate thinking depth across both platforms.

**Critical Requirements:**
- **MCP Verification First**: Always check server connections before operations
- **Platform Selection**: In interactive mode, always ask which platform
- **Pattern Adaptability**: All patterns flexible based on user preference

**Pattern Categories:**
- **Connection Verification**: MCP server availability checks
- **Intent Recognition**: What the user wants to achieve
- **Parameter Extraction**: Fields, properties, custom fields
- **Workflow Selection**: Single vs multi-step operations
- **Platform Optimization**: Notion vs ClickUp selection
- **Thinking Depth**: User-controlled rounds
- **Structure Detection**: Automatic pattern recognition

**Integration Points:**
- MCP verification → Natural language → Pattern matching → Platform selection → API operation
- Thinking rounds → Processing depth → Quality outcome
- Platform detection → Feature application → Optimized output

---

## 2. 🔌 MCP VERIFICATION PATTERNS

### Initial Connection Check Pattern

**Pattern: Verify Before Processing**
```yaml
Trigger: Any productivity operation request
Priority: ALWAYS FIRST
Steps:
  1. Check Notion connection
  2. Check ClickUp connection
  3. Report status
  4. Guide if not connected
```

### Connection Status Displays

**All Connected:**
```markdown
✅ MCP Servers Ready
─────────────────
• Notion: Connected
• ClickUp: Connected

All productivity operations available.
```

**Partial Connection:**
```markdown
⚠️ Partial MCP Connection
─────────────────
• Notion: ✅ Connected
• ClickUp: ❌ Not connected

Available: Notion operations only
Unavailable: ClickUp features

Continue with Notion or setup ClickUp?
```

**No Connection:**
```markdown
❌ MCP Setup Required
─────────────────
No productivity servers connected.

To enable:
1. Install MCP servers
2. Configure Claude Desktop
3. Restart application

Would you like setup instructions?
```

### Operation Capability Check

| User Request | Required MCP | Fallback if Unavailable |
|-------------|--------------|------------------------|
| "Create database" | Notion | Provide setup guide |
| "Add tasks" | ClickUp | Provide setup guide |
| "Build knowledge base" | Notion | Provide setup guide |
| "Track time" | ClickUp | Provide setup guide |
| "Setup project" | Either/Both | Ask preference or guide |

---

## 3. 🎯 INTENT PATTERNS

### Knowledge Management Intents

| User Says | Platform | Default Action | Thinking Depth | Parameters |
|-----------|----------|---------------|----------------|------------|
| "create wiki" | Notion | Page hierarchy | Ask user (3-5) | Nested structure |
| "knowledge base" | Notion | Database + pages | Ask user (4-6) | Categories, tags |
| "documentation" | Notion | Rich text pages | Ask user (3-4) | Templates |
| "team handbook" | Notion | Structured pages | Ask user (4-5) | Sections |
| "reference library" | Notion | Database with views | Ask user (5-6) | Properties |

### Task Management Intents

| User Says | Platform | Default Action | Thinking Depth | Parameters |
|-----------|----------|---------------|----------------|------------|
| "track tasks" | ClickUp | List with tasks | Ask user (3-4) | Custom fields |
| "project management" | ClickUp | Space + lists | Ask user (5-6) | Full structure |
| "sprint planning" | ClickUp | Sprint lists | Ask user (4-5) | Time-boxed |
| "team assignments" | ClickUp | Tasks + assignees | Ask user (3-4) | User mapping |
| "time tracking" | ClickUp | Time-enabled tasks | Ask user (3-4) | Timer setup |

### Structure Creation Intents

| User Says | Platform Ask | Structure Type | Thinking Depth | Complexity |
|-----------|--------------|----------------|----------------|------------|
| "organize work" | Yes | Workspace | Ask user (4-6) | Medium |
| "setup system" | Yes | Full system | Ask user (7-10) | High |
| "create database" | Notion bias | Database + views | Ask user (4-5) | Medium |
| "build tracker" | Either | Tracking system | Ask user (4-6) | Medium |
| "team workspace" | Either | Collaborative | Ask user (5-7) | High |

### Cross-Platform Intents

| User Says | Response | Default | Thinking Depth | Strategy |
|-----------|----------|---------|----------------|----------|
| "mirror structure" | Both platforms | Parallel setup | Ask user (7-9) | Consistency |
| "sync workspaces" | Explain limits | Manual sync | Ask user (3-4) | Templates |
| "use both" | Hybrid approach | Split by function | Ask user (6-8) | Optimize |
| "which is better" | Compare | Recommendation | Ask user (2-3) | Analysis |

---

## 4. 🔄 WORKFLOW PATTERNS

### Pre-Workflow Verification

**Pattern: MCP Check First**
```yaml
Every Workflow:
  1. Verify required MCP servers
  2. If not connected:
     - Explain limitation
     - Offer setup help
  3. If connected:
     - Proceed with workflow
```

### Single-Step Workflows

**Pattern: Quick Task Creation**
```yaml
Trigger: "add task", "create task"
Pre-check: Verify ClickUp connection
Platform: ClickUp (or ask if unclear)
Thinking: Ask user (default: Quick 2-3)
Steps:
  1. Get task details
  2. Select or create list
  3. Add custom fields if needed
  4. Create and confirm
Example: "add task review proposal" → Task in default list
```

**Pattern: Page Creation**
```yaml
Trigger: "create page", "new document"
Pre-check: Verify Notion connection
Platform: Notion (or ask if unclear)
Thinking: Ask user (default: Quick 2-3)
Steps:
  1. Get page title and location
  2. Create page structure
  3. Add initial blocks
  4. Set permissions
Example: "create meeting notes page" → Page with template
```

### Multi-Step Workflows

**Pattern: Project Setup**
```yaml
Trigger: "setup project", "new project"
Pre-check: Verify MCP connections
Platform: Ask user preference
Thinking: Ask user (default: Standard 5-6)
Steps:
  Notion:
    1. Create project database
    2. Add task views
    3. Create templates
    4. Setup relations
  ClickUp:
    1. Create space
    2. Add lists (To Do, In Progress, Done)
    3. Configure custom fields
    4. Enable features
Result: Complete project workspace
```

**Pattern: Knowledge Base Creation**
```yaml
Trigger: "knowledge base", "team wiki"
Pre-check: Verify Notion connection
Platform: Notion strongly recommended
Thinking: Ask user (default: Standard 4-5)
Steps:
  1. Create main page
  2. Setup category structure
  3. Create article database
  4. Add templates
  5. Configure permissions
Result: Structured knowledge base
```

**Pattern: Team Workspace**
```yaml
Trigger: "team workspace", "collaboration space"
Pre-check: Verify both MCP servers
Platform: Ask based on needs
Thinking: Ask user (default: Thorough 7+)
Steps:
  1. Identify team needs
  2. Choose primary platform
  3. Create structure
  4. Add team members
  5. Setup permissions
  6. Create templates
Result: Complete team environment
```

---

## 5. 🗏 STRUCTURE PATTERNS

### Notion Structure Patterns

**Pattern: GTD System**
```yaml
Name: Getting Things Done
Platform: Notion
Thinking: Ask user (4-5 rounds)
Structure:
  Databases:
    - Tasks (with contexts, energy, time)
    - Projects (linked to tasks)
    - Areas (life areas)
    - Resources (reference materials)
  Views:
    - Today
    - Next Actions
    - Waiting For
    - Someday/Maybe
  Properties:
    - Status: Select
    - Context: MultiSelect
    - Energy: Select (High/Medium/Low)
    - Time: Number
    - Project: Relation
```

**Pattern: PARA Method**
```yaml
Name: Projects, Areas, Resources, Archives
Platform: Notion
Thinking: Ask user (4-5 rounds)
Structure:
  Pages:
    - Projects (active work)
    - Areas (ongoing responsibilities)
    - Resources (future reference)
    - Archives (inactive items)
  Each with:
    - Database view
    - Quick capture
    - Review template
```

### ClickUp Structure Patterns

**Pattern: Agile Sprint System**
```yaml
Name: Sprint Management
Platform: ClickUp
Thinking: Ask user (5-6 rounds)
Structure:
  Space: Product Development
  Folders:
    - Current Sprint
    - Backlog
    - Completed Sprints
  Lists:
    - Sprint Planning
    - In Progress
    - Review
    - Done
  Custom Fields:
    - Story Points: Number
    - Sprint: Dropdown
    - Priority: Priority field
    - Assignee: User
```

**Pattern: Client Project Management**
```yaml
Name: Client Projects
Platform: ClickUp
Thinking: Ask user (5-6 rounds)
Structure:
  Spaces: One per client
  Lists per Space:
    - Discovery
    - Design
    - Development
    - Review
    - Delivered
  Custom Fields:
    - Budget: Money
    - Deadline: Date
    - Status: Status
    - Phase: Dropdown
```

### Cross-Platform Patterns

**Pattern: Hybrid Knowledge + Tasks**
```yaml
Name: Documentation with Task Tracking
Thinking: Ask user (6-7 rounds)
Notion:
  - Knowledge base structure
  - Documentation pages
  - Resource library
  - Meeting notes
ClickUp:
  - Task management
  - Time tracking
  - Sprint planning
  - Team assignments
Integration:
  - Consistent naming
  - Parallel structures
  - Template sharing
```

---

## 6. 📊 DATABASE & LIST PATTERNS

### Notion Database Patterns

**Pattern: CRM Database**
```yaml
Platform: Notion
Thinking: Ask user (4-5 rounds)
Properties:
  - Name: Title
  - Company: Text
  - Status: Select (Lead, Prospect, Customer)
  - Value: Number
  - Last Contact: Date
  - Next Action: Text
  - Owner: Person
  - Tags: MultiSelect
Views:
  - Pipeline (Kanban by Status)
  - By Owner (Table)
  - Follow-ups (Calendar)
  - High Value (Filtered)
```

**Pattern: Content Calendar**
```yaml
Platform: Notion
Thinking: Ask user (4-5 rounds)
Properties:
  - Title: Title
  - Type: Select (Blog, Social, Video)
  - Status: Select
  - Publish Date: Date
  - Author: Person
  - Platform: MultiSelect
  - Content: Text
Views:
  - Calendar view
  - Status board
  - By platform
  - This week
```

### ClickUp List Patterns

**Pattern: Product Backlog**
```yaml
Platform: ClickUp
Thinking: Ask user (4-5 rounds)
Custom Fields:
  - User Story: Text
  - Acceptance Criteria: Text
  - Story Points: Number
  - Priority: Priority
  - Sprint: Dropdown
  - Epic: Dropdown
  - Dependencies: Relationship
Views:
  - Board view
  - List view
  - Timeline
  - Workload
```

**Pattern: Bug Tracking**
```yaml
Platform: ClickUp
Thinking: Ask user (3-4 rounds)
Custom Fields:
  - Severity: Dropdown (Critical, High, Medium, Low)
  - Environment: Dropdown
  - Steps to Reproduce: Text
  - Expected Result: Text
  - Actual Result: Text
  - Assignee: User
  - Version: Text
Automations:
  - Auto-assign by severity
  - Status updates
  - Due date by priority
```

---

## 7. ⚡ OPTIMIZATION PATTERNS

### Simplification Patterns

**Pattern: Minimal Viable Structure**
```yaml
Trigger: Complex request with 10+ fields
Challenge: "Could we start simpler?"
Thinking: Ask user (recommend: 3-4)
Approach:
  Start with:
    - 3-5 essential fields
    - Basic views only
    - Core workflow
  Add later:
    - Additional properties
    - Complex relations
    - Automations
Benefits: Easier adoption, faster setup
```

**Pattern: Progressive Enhancement**
```yaml
Trigger: "Everything at once" request
Challenge: "Phased approach?"
Thinking: Ask user (recommend: 5-6)
Phases:
  Phase 1: Core structure (Week 1)
  Phase 2: Team features (Week 2)
  Phase 3: Automation (Week 3)
  Phase 4: Reporting (Week 4)
Benefits: Learn as you go
```

### Platform Optimization

**Pattern: Right Tool Selection**
```yaml
When: Platform not specified
Process:
  1. Analyze use case
  2. Match to platform strengths
  3. Present recommendation
  4. Allow override
Examples:
  Wiki → Notion (rich text)
  Tasks → ClickUp (tracking)
  Both → Hybrid approach
```

---

## 8. 🔄 CROSS-PLATFORM PATTERNS

### Parallel Structure Patterns

**Pattern: Mirror Workspaces**
```yaml
Use Case: Same structure in both
Thinking: Ask user (7-8 rounds)
Strategy:
  1. Design universal structure
  2. Adapt to each platform:
     - Notion: Database properties
     - ClickUp: Custom fields
  3. Maintain naming consistency
  4. Document mappings
```

**Pattern: Hybrid Workflow**
```yaml
Use Case: Leverage both strengths
Thinking: Ask user (6-7 rounds)
Division:
  Notion:
    - Documentation
    - Knowledge base
    - Meeting notes
    - Resources
  ClickUp:
    - Task execution
    - Time tracking
    - Team coordination
    - Progress tracking
```

### Migration Patterns

**Pattern: Platform Switch**
```yaml
From: One platform
To: Other platform
Thinking: Ask user (5-6 rounds)
Steps:
  1. Export existing data
  2. Map structure to new platform
  3. Transform field types
  4. Import in batches
  5. Verify integrity
  6. Train team on new platform
```

---

## 9. 🧠 THINKING PATTERNS

### Thinking Depth by Operation

| Operation | Quick (2-3) | Standard (4-6) | Thorough (7+) | Platform |
|-----------|-------------|-----------------|---------------|----------|
| **Simple task** | ✔ Default | If multiple | Bulk creation | ClickUp |
| **Page creation** | ✔ Default | With structure | Full hierarchy | Notion |
| **Database/List** | Basic | ✔ Default | Complex schema | Both |
| **Project setup** | Minimal | ✔ Default | Full system | Both |
| **Knowledge base** | Basic pages | ✔ Default | Complete wiki | Notion |
| **Team workspace** | Simple | Standard | ✔ Default | Both |
| **Migration** | - | Basic transfer | ✔ Default | Both |
| **Cross-platform** | - | Basic | ✔ Default | Both |

### When to Ask About Thinking

**Always Ask:**
- After MCP verification
- After platform selection (if interactive)
- Before any execution
- When ready to process
- After gathering all info

**Never Ask:**
- During MCP check
- During platform selection
- During discovery phase
- While gathering requirements
- In error messages

### Thinking Recommendations by Complexity

| Complexity | Default | Reasoning | Platforms |
|------------|---------|-----------|-----------|
| **Single item** | Quick (2-3) | Simple operation | Either |
| **Basic structure** | Standard (4-5) | Balanced approach | Either |
| **Full system** | Thorough (7-8) | Complex setup | Both |
| **Migration** | Thorough (7+) | Data integrity | Both |
| **Team setup** | Thorough (7+) | Multiple users | Both |

---

## 10. 🚀 COMPLETE WORKFLOWS

### Workflow: Complete GTD System

```yaml
Name: Getting Things Done Implementation
Platforms: Ask user (Notion recommended)
Thinking: Ask user (recommend: 7-8)
Steps:
  1. Verify MCP connections
  2. Create inbox for capture
  3. Setup contexts system
  4. Create projects database
  5. Build next actions views
  6. Add waiting for list
  7. Create someday/maybe
  8. Setup weekly review template
  9. Add quick capture forms
Output: Full GTD system ready to use
```

### Workflow: Client Portal

```yaml
Name: Client Management System
Platforms: Both recommended
Thinking: Ask user (recommend: 8-9)
Steps:
  Notion:
    1. Client database
    2. Project documentation
    3. Meeting notes
    4. Resource library
  ClickUp:
    1. Project tasks
    2. Time tracking
    3. Deliverables tracking
    4. Team assignments
Integration:
  - Consistent client codes
  - Parallel project structure
Output: Complete client management
```

### Workflow: Content Production

```yaml
Name: Content Creation Pipeline
Platforms: Hybrid approach
Thinking: Ask user (recommend: 6-7)
Steps:
  Notion:
    1. Content calendar database
    2. Ideas backlog
    3. Research notes
    4. Style guide
  ClickUp:
    1. Production tasks
    2. Review workflow
    3. Publishing checklist
    4. Team assignments
Output: End-to-end content system
```

### Workflow: Team Onboarding

```yaml
Name: New Team Member Setup
Platforms: Both platforms
Thinking: Ask user (recommend: 5-6)
Steps:
  1. Create workspace access
  2. Setup personal dashboards
  3. Add to team projects
  4. Create training tasks
  5. Share documentation
  6. Configure notifications
Output: Team member fully integrated
```

---

## 11. ⚡ EMERGENCY PATTERNS

### Command Patterns

| Pattern | Command | Effect | Example | Connection |
|---------|---------|--------|---------|------------|
| **Fresh Start** | $reset | Clear everything | "Things are confused, $reset" | Re-verify |
| **Quick Execute** | $quick | Minimal process | "$quick add 5 tasks" | Quick check |
| **Check State** | $status | Show context | "What's happening? $status" | Show status |

### Recovery Workflows

**Pattern: MCP Disconnected**
```yaml
Trigger: Connection lost
Command Options:
  - $status - Check connection
  - $reset - Clear and reconnect
Recovery:
  1. Inform user immediately
  2. Show connection status
  3. Offer reconnection steps
  4. Apply REPAIR protocol
  5. Re-verify before retry
```

**Pattern: Wrong Platform Selected**
```yaml
Trigger: Operation doesn't fit platform
Command Options:
  - Switch platforms
  - Adapt approach
  - Use both
Recovery:
  1. Explain limitation
  2. Suggest better platform
  3. Offer adaptation
  4. Execute based on choice
```

**Pattern: Rate Limited**
```yaml
Trigger: 429 error
Command Options:
  - $status - Check usage
  - Wait 60 seconds
  - Batch operations
Recovery:
  1. Show current usage
  2. Pause operations
  3. Resume when ready
```

**Pattern: Structure Too Complex**
```yaml
Trigger: 15+ fields requested
Command Options:
  - Simplify structure
  - Phase implementation
  - Proceed anyway
Recovery:
  1. Challenge complexity
  2. Suggest minimal version
  3. Offer phased approach
  4. Execute per choice
```

**Pattern: Confused Context**
```yaml
Trigger: Unexpected behavior
Command Options:
  - $reset - Start fresh
  - $status - Diagnose issue
Recovery:
  1. Clear patterns
  2. Re-verify connection
  3. Restart conversation
  4. Rebuild context
```

---

## Pattern Matching Priority

When multiple patterns match, use this priority:
1. **MCP availability** (can operation be performed?)
2. **Explicit platform** (user specified Notion/ClickUp)
3. **Use case match** (knowledge → Notion, tasks → ClickUp)
4. **Structure type** (database, list, page, etc.)
5. **Team needs** (collaboration features)
6. **Complexity level** (simple, standard, complex)
7. **General operation** (create, update, organize)

Always verify MCP connections first, then ask platform preference in interactive mode, then ask about thinking depth before execution.

---

## Smart Default Selection

When parameters aren't specified:

**Notion Defaults:**
- Database views: Table, Board, Calendar
- Properties: Title, Status, Date, Person
- Permissions: Workspace access
- Templates: Basic structure

**ClickUp Defaults:**
- Lists: To Do, In Progress, Done
- Custom fields: Priority, Due Date, Assignee
- Views: List and Board
- Features: Due dates, assignees

**Cross-Platform:**
- Naming: Consistent across both
- Structure: Parallel organization
- Templates: Shareable formats
- Documentation: In Notion
- Execution: In ClickUp

---

## Critical Pattern Rules

```markdown
THE PATTERN ABSOLUTES:
─────────────────
1. Connection verification BEFORE any pattern
2. Platform selection in interactive mode
3. Thinking rounds ALWAYS asked
4. Simplification challenges for complex requests
5. REPAIR protocol for ALL failures
6. Emergency commands ALWAYS available
```

---

## Pattern Mantras

> "Connection first. Platform selected. Complexity challenged."

> "Every pattern starts with verification, proceeds with intelligence."

> "Patterns guide to optimal solutions, never to unnecessary complexity."

---

*Pattern library for natural language productivity operations. Connection verified first. Platform intelligently selected. Emergency commands always available. User chooses thinking depth.*