# ClickUp - Patterns & Operations - v0.120

Comprehensive pattern library and operation reference for natural language to ClickUp mapping. All patterns executed through intelligent conversation with user-controlled thinking depth.

## Table of Contents

1. [🎯 Intent Recognition Engine](#1-🎯-intent-recognition-engine)
2. [🧠 Thinking Depth System](#2-🧠-thinking-depth-system)
3. [✨ Creation Operations](#3-✨-creation-operations)
4. [📄 Update Operations](#4-📄-update-operations)
5. [🗂️ Organization Operations](#5-🗂️-organization-operations)
6. [🔍 Query Operations](#6-🔍-query-operations)
7. [🏗️ Workspace Templates](#7-🏗️-workspace-templates)
8. [⚡ Quick Operations Reference](#8-⚡-quick-operations-reference)
9. [🔗 Composite Patterns](#9-🔗-composite-patterns)
10. [🎯 Pattern Application Rules](#10-🎯-pattern-application-rules)
11. [📄 Pattern Evolution](#11-📄-pattern-evolution)

---

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring System
| Confidence | Range | Conversation Approach | Thinking Prompt |
|------------|-------|----------------------|-----------------|
| **Exact** | >0.95 | Confirm + ask rounds + execute | "How many thinking rounds?" → Execute |
| **High** | 0.80-0.95 | Single clarification + ask rounds | "2-week cycles? Thinking depth?" |
| **Medium** | 0.50-0.79 | 2-3 questions, then ask rounds | Questions first, then "Thinking rounds?" |
| **Low** | <0.50 | Full guidance, ask rounds when ready | Guide fully, then "Ready? Thinking depth?" |

### Pattern Matching Hierarchy
```
1. Exact Match → Ask thinking rounds → Quick execute
2. Synonym Recognition → Brief clarify → Ask rounds → Execute
3. Category Detection → Guided questions → Ask rounds → Execute
4. Composite Understanding → Design conversation → Ask rounds → Execute
5. Context Inference → Full exploration → Ask rounds → Execute
```

---

## 2. 🧠 THINKING DEPTH SYSTEM

### Always Ask Before Execution

**Standard Question Format:**
```
"How many rounds of thinking should I use?
• Quick (2-3) - [context-specific description]
• Standard (4-6) - [context-specific description]
• Thorough (7-10) - [context-specific description]
Or specify a number!"
```

### Context-Specific Thinking Recommendations

| Operation Type | Quick (2-3) | Standard (4-6) | Thorough (7-10) | Maximum (10+) |
|---------------|-------------|----------------|-----------------|---------------|
| **Single Task** | Basic creation | With relationships | Full integration | N/A |
| **List Creation** | Simple fields | Standard setup | Complex fields | Enterprise scale |
| **Workspace** | Basic structure | Department level | Multi-team | Organization-wide |
| **Templates** | Simple repeat | Standard patterns | Complex automation | Industry best practices |
| **Organization** | Quick archive | Structured cleanup | Full reorganization | Complete migration |

### Thinking Depth by Pattern

| Pattern | Default Rounds | User Often Chooses |
|---------|---------------|-------------------|
| Task creation | 2-3 | Quick |
| Sprint setup | 4-6 | Standard |
| Bug tracking | 4-6 | Standard |
| CRM system | 7-10 | Thorough |
| Agency workspace | 7-10 | Thorough |
| Personal tasks | 2-3 | Quick |
| Archive operation | 2-3 | Quick |
| Dashboard creation | 4-6 | Standard |

---

## 3. ✨ CREATION OPERATIONS

### Sprint Planning
**Triggers:** `sprint board, sprint planning, agile sprints, scrum board, iteration planning`

**Conversation Approach:**
- High confidence: Ask sprint length + thinking rounds
- Medium confidence: Ask team size, sprint length + thinking rounds
- Low confidence: Full agile exploration, then thinking rounds

**Thinking Recommendations:**
```
"How many thinking rounds for your sprint system?
• Quick (2-3) - Basic sprint board
• Standard (4-6) - Full sprint planning (recommended)
• Thorough (7-10) - Complete agile workspace"
```

**Implementation:**
```yaml
list_name: Sprint [Number]
custom_fields: 
  - Story Points (number)
  - Sprint Goal (text)
  - Acceptance Criteria (text)
  - Epic (dropdown)
  - Component (labels)
statuses: Backlog→To Do→In Progress→Review→Done
views: Board(default), List, Calendar, Gantt, Velocity
template: Sprint planning template included
automations: Sprint rollover enabled
default_thinking: Standard (4-6)
```

### Task Management
**Triggers:** `task list, todo list, action items, things to do, daily tasks`

**Conversation Approach:**
- Ask: "Personal or work tasks?" if unclear
- Ask: "How many thinking rounds?"
- Skip: Team features if personal context

**Thinking Recommendations:**
```
"Thinking depth for your task system?
• Quick (2-3) - Simple list (recommended for personal)
• Standard (4-6) - Full tracking (recommended for work)"
```

**Implementation:**
```yaml
custom_fields:
  - Priority (Urgent/High/Normal/Low)
  - Due Date (date)
  - Time Estimate (duration)
  - Category (labels)
  - Project (relationship)
statuses: To Do→In Progress→Review→Complete
views: Today(default), This Week, By Project, All
automations: Due date reminders, overdue alerts
default_thinking: Quick (2-3) for personal, Standard (4-6) for work
```

### Bug Tracking
**Triggers:** `bug tracker, issue tracking, bug list, defects, problem tracking`

**Conversation Approach:**
- Always include severity levels
- Ask about environment tracking if development context
- Ask thinking rounds with recommendation

**Thinking Recommendations:**
```
"How thorough should the bug tracking design be?
• Quick (2-3) - Basic tracking
• Standard (4-6) - Full bug system (recommended)
• Thorough (7-10) - QA integration"
```

**Implementation:**
```yaml
custom_fields:
  - Severity (Critical/High/Medium/Low)
  - Environment (Dev/Staging/Prod)
  - Steps to Reproduce (text)
  - Expected vs Actual (text)
  - Reporter (user)
  - Component (dropdown)
statuses: New→Confirmed→In Progress→Testing→Resolved→Closed
views: List(by priority), Board(by status), Calendar(found date)
automations: Critical bug alerts
default_thinking: Standard (4-6)
```

### Client Projects
**Triggers:** `client work, client projects, agency projects, customer work`

**Conversation Approach:**
- Ask: "How many clients?" (determines structure)
- Ask: "Billing method?" (hourly vs project)
- Ask: "Thinking depth?" with thorough recommendation

**Thinking Recommendations:**
```
"This needs careful design. Thinking rounds?
• Standard (4-6) - Basic client tracking
• Thorough (7-10) - Full agency system (recommended)
• Maximum (10+) - Enterprise agency"
```

**Implementation:**
```yaml
space_structure:
  - Clients (folder)
    - [Client Name] (list per client)
custom_fields:
  - Project Value (money)
  - Timeline (date range)
  - Client Contact (email)
  - Status (Planning/Active/Review/Complete)
  - Deliverables (checklist)
  - Billable (checkbox)
views: List, Board, Gantt(timeline), Calendar
relationships: Projects → Tasks → Time Entries
default_thinking: Thorough (7-10)
```

### Content Calendar
**Triggers:** `content calendar, editorial calendar, publishing schedule, social calendar`

**Conversation Approach:**
- Ask: "Which platforms?" (determines fields)
- Assume: Publishing dates needed
- Ask: "Thinking rounds?"

**Thinking Recommendations:**
```
"Content system thinking depth?
• Quick (2-3) - Simple calendar
• Standard (4-6) - Multi-platform (recommended)
• Thorough (7-10) - Full content operations"
```

**Implementation:**
```yaml
custom_fields:
  - Publish Date (date/time)
  - Platform (Social/Blog/Email/Video)
  - Status (Idea→Draft→Review→Scheduled→Published)
  - Author (user)
  - Campaign (relationship)
  - Performance (number)
views: Calendar(primary), Pipeline(status), Platform, Month
automations: Publishing reminders, status updates
default_thinking: Standard (4-6)
```

### CRM System
**Triggers:** `CRM, customer management, contact tracking, sales pipeline`

**Conversation Approach:**
- Ask: "Track deals/opportunities too?"
- Ask: "Team size?" (for assignment features)
- Ask: "Thinking depth?" with thorough recommendation

**Thinking Recommendations:**
```
"CRM systems benefit from thorough planning:
• Standard (4-6) - Basic CRM
• Thorough (7-10) - Full sales system (recommended)
• Maximum (10+) - Enterprise CRM"
```

**Implementation:**
```yaml
databases:
  - Contacts (people and details)
  - Companies (organizations)
  - Opportunities (deals/pipeline)
  - Activities (interactions)
relationships: Company → Contacts → Opportunities
pipeline_stages: Lead→Qualified→Proposal→Negotiation→Closed
custom_fields: Deal Value, Probability, Close Date, Owner
default_thinking: Thorough (7-10)
```

---

## 4. 📄 UPDATE OPERATIONS

All update operations use conversational confirmation with thinking depth:

| Operation | Triggers | Conversation | Default Thinking |
|-----------|----------|--------------|------------------|
| **Complete Task** | `done, complete, finish` | "Marking [task] complete! Quick thinking?" | Quick (2) |
| **Reschedule** | `move to, postpone, delay` | "When? Thinking rounds?" | Quick (2-3) |
| **Assign** | `assign to, give to` | "Who? Analysis depth?" | Quick (2) |
| **Prioritize** | `urgent, high priority` | "Setting high! Thinking?" | Quick (2) |
| **Add Time** | `log time, track hours` | "How many hours? Rounds?" | Quick (2-3) |
| **Update Status** | `mark as, change to` | "Moving to [status]! Depth?" | Quick (2) |

### Intelligent Date Parsing
```
"tomorrow" → Next day
"next week" → +7 days
"Monday" → Upcoming Monday
"end of month" → Last day
"Dec 15" → December 15
"in 2 hours" → +2 hours
"next sprint" → Sprint start date
```

---

## 5. 🗂️ ORGANIZATION OPERATIONS

### Archive Operations
**Triggers:** `archive, clean up, move old, organize completed`

**Conversation Flow:**
```
User: "archive old stuff"
System: "I'll help archive completed items!
         I'll move items completed over 30 days ago.
         Keep for reference or prepare for deletion?"
User: "keep them"
System: "How many thinking rounds for the organization?
         • Quick (2-3) - Simple archive
         • Standard (4-6) - Organized structure"
User: "quick"
System: "Archiving with quick analysis to /Archive/2024/..."
```

**Implementation:**
```yaml
criteria: 
  - Status = Complete
  - Modified > 30 days
  - No active dependencies
destination: /Archive/[Year]/[Month]/
preserve: All data and relationships
default_thinking: Quick (2-3)
```

### View Creation
**Triggers:** `show as, view by, group by, filter by, create view`

**Conversation Approach:**
- Detect intent (calendar for dates, board for workflow)
- Ask grouping preference if unclear
- Ask thinking rounds
- Apply smart defaults

**Thinking for Views:**
```
"How thorough should the view design be?
• Quick (2-3) - Basic view
• Standard (4-6) - Optimized filters"
```

### Bulk Operations
**Triggers:** `update all, change multiple, bulk edit, mass update`

**Conversation Flow:**
```
User: "mark all project X tasks done"
System: "I'll mark all tasks in Project X as complete.
         Found 23 tasks. 
         Thinking rounds? (Quick 2-3 recommended)"
User: "quick"
System: "Using quick analysis... ✅ 23 tasks marked complete!"
```

---

## 6. 🔍 QUERY OPERATIONS

### Time-Based Queries

All queries use conversational response with optional thinking:

| Query | Triggers | Thinking Prompt | Default |
|-------|----------|-----------------|---------|
| **Today** | `today, what's due` | "Analysis depth for today view?" | Quick (2) |
| **This Week** | `this week, weekly` | "How thorough?" | Quick (2-3) |
| **Overdue** | `overdue, late` | "Thinking rounds?" | Quick (2-3) |
| **Upcoming** | `upcoming, next` | "Analysis level?" | Quick (2-3) |

### Filter Patterns
```yaml
my_tasks: "Showing your tasks... (Quick thinking: 2 rounds)"
unassigned: "Finding unassigned... (Quick thinking: 2 rounds)"
high_priority: "Priority items... (Standard thinking: 4 rounds)"
blocked: "Blocked tasks... (Standard thinking: 5 rounds)"
```

---

## 7. 🏗️ WORKSPACE TEMPLATES

### Template Selection Through Conversation

**Software Development:**
```
User: "set up for development team"
System: "I'll create a development workspace!
         Agile/Scrum or Kanban approach?"
User: "Agile"
System: "Perfect! How many thinking rounds?
         • Standard (4-6) - Basic agile
         • Thorough (7-10) - Full system (recommended)"
Result: Complete dev environment with chosen depth
```

**Marketing Agency:**
```
User: "agency workspace"
System: "Creating agency management system!
         How many active clients typically?"
User: "15"
System: "That's substantial! Thinking depth?
         • Standard (4-6) - Core features
         • Thorough (7-10) - Full integration (recommended)
         • Maximum (10+) - Enterprise scale"
Result: Scaled agency system
```

**Personal Productivity:**
```
User: "personal organization"
System: "Let's organize your personal work!
         Focus on tasks, goals, or both?"
User: "both"
System: "Comprehensive! Thinking rounds?
         • Quick (2-3) - Simple system
         • Standard (4-6) - Full productivity (recommended)"
Result: Personal productivity hub
```

### Smart Template Patterns

| Detected Context | Template Applied | Key Components | Default Thinking |
|-----------------|------------------|----------------|------------------|
| **Development** | Agile Sprint System | Sprints, backlog, bugs, velocity | Standard (4-6) |
| **Agency** | Client Management | Clients, projects, time, billing | Thorough (7-10) |
| **Sales** | Pipeline CRM | Contacts, deals, activities | Thorough (7-10) |
| **Marketing** | Campaign Hub | Calendar, content, analytics | Standard (4-6) |
| **HR** | Recruiting Pipeline | Positions, candidates, interviews | Standard (4-6) |
| **Product** | Roadmap System | Features, experiments, metrics | Thorough (7-10) |

---

## 8. ⚡ QUICK OPERATIONS REFERENCE

### Top 25 Operations (With Thinking)

| User Says | System Response | Thinking | Operation |
|-----------|----------------|----------|-----------|
| `new task` | "Creating task! Quick thinking (2)?" | Quick | Create with context |
| `add to sprint` | "Adding! Rounds?" | Quick | Sprint assignment |
| `mark done` | "Completing! Quick?" | Quick | Status update |
| `assign to me` | "Assigning! Depth?" | Quick | Self-assignment |
| `due tomorrow` | "Setting! Rounds?" | Quick | Date update |
| `high priority` | "Prioritizing! Quick?" | Quick | Priority change |
| `start timer` | "Timer! Analysis?" | Quick | Time tracking |
| `create sprint` | "Sprint! Thinking (4-6)?" | Standard | Sprint creation |
| `bug report` | "Bug! Depth (4-6)?" | Standard | Bug with template |
| `meeting notes` | "Notes! Quick or standard?" | Quick/Standard | Doc creation |
| `my tasks` | "Finding... Thinking?" | Quick | Filter view |
| `this week` | "Week view! Depth?" | Quick | Time filter |
| `overdue` | "Checking... Rounds?" | Quick | Status check |
| `board view` | "Switching! Quick?" | Quick | View change |
| `add comment` | "Comment! Thinking?" | Quick | Comment addition |
| `link tasks` | "Linking! Analysis?" | Standard | Dependency |
| `duplicate` | "Duplicating! Depth?" | Quick | Copy operation |
| `archive` | "Archiving! Rounds (2-3)?" | Quick | Clean up |
| `create template` | "Template! Thinking (4-6)?" | Standard | Template save |
| `bulk update` | "Bulk! Depth?" | Standard | Mass edit |
| `import CSV` | "Import! Analysis (4-6)?" | Standard | Data import |
| `time report` | "Report! Thinking?" | Standard | Time summary |
| `workload` | "Workload! Depth?" | Standard | Capacity view |
| `recurring` | "Recurrence! Rounds?" | Standard | Repeat setup |
| `share` | "Sharing! Quick?" | Quick | Permission setup |

---

## 9. 🔗 COMPOSITE PATTERNS

### Complex System Detection

When users request comprehensive systems, combine patterns with appropriate thinking:

### Agency System
**Triggers:** `agency, client management, professional services`
```yaml
combines:
  - Client database
  - Project tracking
  - Time management
  - Billing system
  - Team resources
conversation: "Complete agency system! Thinking rounds (7-10 recommended)?"
default_thinking: Thorough (8-9)
```

### Product Development
**Triggers:** `product management, roadmap, feature tracking`
```yaml
combines:
  - Roadmap timeline
  - Feature requests
  - User feedback
  - Experiments
  - Metrics dashboard
conversation: "Product system! Analysis depth (7-10 suggested)?"
default_thinking: Thorough (8)
```

### Operations Hub
**Triggers:** `operations, ops management, business operations`
```yaml
combines:
  - Process tracking
  - Team workload
  - Resource planning
  - Performance metrics
  - Documentation
conversation: "Operations hub! Thinking rounds (6-8 typical)?"
default_thinking: Standard (6-7)
```

---

## 10. 🎯 PATTERN APPLICATION RULES

### Selection Logic
1. **Check exact match** (>0.95 confidence)
2. **Analyze context** (previous conversation)
3. **Consider scale** (personal vs team)
4. **Ask thinking preference** (always before execution)
5. **Apply smart defaults** (industry standards)
6. **Confirm if uncertain** (<0.50 confidence)

### Quality Standards
Every pattern ensures:
- User chooses thinking depth
- Essential fields only (5-8 max)
- Helpful default views (3-4)
- Scalable structure (<5000 items)
- Clear naming conventions
- Best practices applied

### Performance Optimization
- **Small lists**: <1,000 tasks (all features)
- **Medium lists**: 1,000-5,000 (filtered views)
- **Large lists**: 5,000+ (split or archive)
- **Mobile**: Simplified views (3-4 fields)
- **Automation**: Simple rules only
- **Thinking**: Scale with complexity

### ClickUp-Specific Features
- Custom fields over descriptions
- Relationships for connections
- Views for different perspectives
- Automations for workflows
- Templates for repeatability
- Time tracking when billable
- Dependencies for projects
- User-chosen thinking depth

---

## 11. 📄 PATTERN EVOLUTION

### Adaptive Learning Indicators

Track user preferences to improve patterns:

**Speed Preference:**
- Requests quick/fast → Suggest Quick thinking (2-3)
- Says "detailed" → Suggest Thorough (7-10)
- Mentions "simple" → Suggest Quick (2-3)

**Expertise Signals:**
- Uses ClickUp terms → Offer full range
- Asks "how" questions → Provide education + standard
- Says "just give me" → Quick with option to increase

**Scale Indicators:**
- Numbers mentioned → Adjust structure + thinking
- "Team" mentioned → Collaboration features + standard
- "Personal" stated → Individual focus + quick

### Pattern Refinement with Thinking

Patterns improve based on:
- Thinking depth preferences (track common choices)
- Success confirmations at different depths
- Follow-up requests after initial thinking
- Modification patterns by thinking level
- Usage indicators correlated with depth

### User Preference Learning

**Common Patterns:**
- New users → Often choose Standard (4-6)
- Power users → Often choose Quick (2-3) or specify exact
- Complex requests → Users appreciate Thorough option
- Simple tasks → Quick almost always sufficient
- First time → Often ask "what do you recommend?"

---

*This pattern library enables instant understanding and execution of natural language requests through intelligent conversation with user-controlled thinking depth. Every pattern adapts to context while maintaining professional ClickUp best practices and giving users complete control over analysis depth.*