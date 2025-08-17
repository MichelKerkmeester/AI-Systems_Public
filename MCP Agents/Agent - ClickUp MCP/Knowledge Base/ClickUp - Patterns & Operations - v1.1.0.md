# ClickUp - Patterns & Operations - v1.1.0

Comprehensive pattern library and operation reference for natural language to ClickUp mapping. All patterns executed through intelligent conversation.

## Table of Contents

1. [🎯 Intent Recognition Engine](#1-🎯-intent-recognition-engine)
2. [✨ Creation Operations](#2-✨-creation-operations)
3. [🔄 Update Operations](#3-🔄-update-operations)
4. [🗂️ Organization Operations](#4-🗂️-organization-operations)
5. [🔍 Query Operations](#5-🔍-query-operations)
6. [🏗️ Workspace Templates](#6-🏗️-workspace-templates)
7. [⚡ Quick Operations Reference](#7-⚡-quick-operations-reference)
8. [🔗 Composite Patterns](#8-🔗-composite-patterns)
9. [🎯 Pattern Application Rules](#9-🎯-pattern-application-rules)
10. [🔄 Pattern Evolution](#10-🔄-pattern-evolution)

---

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring System
| Confidence | Range | Conversation Approach | Example |
|------------|-------|----------------------|---------|
| **Exact** | >0.95 | Confirm and execute immediately | "create sprint board" → "Creating your sprint board now!" |
| **High** | 0.80-0.95 | Single clarification then proceed | "track sprints" → "Setting up sprints! 2-week cycles?" |
| **Medium** | 0.50-0.79 | 2-3 questions for clarity | "agile stuff" → "Let's set up agile! Team size?" |
| **Low** | <0.50 | Full conversational guidance | "help with work" → "What type of work?" |

### Pattern Matching Hierarchy
```
1. Exact Match → Quick confirm + execute
2. Synonym Recognition → Brief clarification + execute
3. Category Detection → Guided questions + execute
4. Composite Understanding → Design conversation + execute
5. Context Inference → Full exploration + execute
```

---

## 2. ✨ CREATION OPERATIONS

### Sprint Planning
**Triggers:** `sprint board, sprint planning, agile sprints, scrum board, iteration planning`

**Conversation Approach:**
- High confidence: Ask sprint length only
- Medium confidence: Ask team size and sprint length
- Low confidence: Full agile exploration

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
```

### Task Management
**Triggers:** `task list, todo list, action items, things to do, daily tasks`

**Conversation Approach:**
- Ask: "Personal or work tasks?" if unclear
- Skip: Team features if personal context

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
```

### Bug Tracking
**Triggers:** `bug tracker, issue tracking, bug list, defects, problem tracking`

**Conversation Approach:**
- Always include severity levels
- Ask about environment tracking if development context

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
```

### Client Projects
**Triggers:** `client work, client projects, agency projects, customer work`

**Conversation Approach:**
- Ask: "How many clients?" (determines structure)
- Ask: "Billing method?" (hourly vs project)

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
```

### Content Calendar
**Triggers:** `content calendar, editorial calendar, publishing schedule, social calendar`

**Conversation Approach:**
- Ask: "Which platforms?" (determines fields)
- Assume: Publishing dates needed

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
```

### CRM System
**Triggers:** `CRM, customer management, contact tracking, sales pipeline`

**Conversation Approach:**
- Ask: "Track deals/opportunities too?"
- Ask: "Team size?" (for assignment features)

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
```

### Documentation
**Triggers:** `meeting notes, documentation, knowledge base, notes`

**Conversation Approach:**
- Ask: "One-time or template?" for meetings
- Ask: "Team shared or personal?" for access

**Implementation:**
```yaml
doc_structure:
  - Title and metadata
  - Sections based on type
  - Action items (linked tasks)
  - Attachments area
templates: Meeting, Report, Brief, Specification
features: Collaborative editing, version history
```

---

## 3. 🔄 UPDATE OPERATIONS

All update operations use conversational confirmation:

| Operation | Triggers | Conversation | Action |
|-----------|----------|--------------|--------|
| **Complete Task** | `done, complete, finish` | "Marking [task] complete!" | Status → Done |
| **Reschedule** | `move to, postpone, delay` | "When should this be due?" | Update date |
| **Assign** | `assign to, give to` | "Who should handle this?" | Set assignee |
| **Prioritize** | `urgent, high priority` | "Setting to high priority!" | Priority → High |
| **Add Time** | `log time, track hours` | "How many hours?" | Add time entry |
| **Update Status** | `mark as, change to` | "Moving to [status]!" | Update status |

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

## 4. 🗂️ ORGANIZATION OPERATIONS

### Archive Operations
**Triggers:** `archive, clean up, move old, organize completed`

**Conversation Flow:**
```
User: "archive old stuff"
System: "I'll help archive completed items!
         I'll move items completed over 30 days ago.
         Keep for reference or prepare for deletion?"
User: "keep them"
System: "Archiving to /Archive/2024/..."
```

**Implementation:**
```yaml
criteria: 
  - Status = Complete
  - Modified > 30 days
  - No active dependencies
destination: /Archive/[Year]/[Month]/
preserve: All data and relationships
```

### View Creation
**Triggers:** `show as, view by, group by, filter by, create view`

**Conversation Approach:**
- Detect intent (calendar for dates, board for workflow)
- Ask grouping preference if unclear
- Apply smart defaults

**View Types:**
```yaml
board: Status or assignee grouping
calendar: Due dates or start dates
gantt: Timeline with dependencies
list: Filtered and sorted
table: All fields visible
timeline: High-level planning
workload: Team capacity
```

### Bulk Operations
**Triggers:** `update all, change multiple, bulk edit, mass update`

**Conversation Flow:**
```
User: "mark all project X tasks done"
System: "I'll mark all tasks in Project X as complete.
         Found 23 tasks. Proceed?"
User: "yes"
System: "✅ 23 tasks marked complete!"
```

---

## 5. 🔍 QUERY OPERATIONS

### Time-Based Queries

All queries use conversational response:

| Query | Triggers | Response Pattern |
|-------|----------|-----------------|
| **Today** | `today, what's due` | "Here's what needs attention today..." |
| **This Week** | `this week, weekly` | "Your week looks like..." |
| **Overdue** | `overdue, late` | "These items are overdue..." |
| **Upcoming** | `upcoming, next` | "Coming up next..." |

### Filter Patterns
```yaml
my_tasks: "Showing your assigned tasks..."
unassigned: "These tasks need an owner..."
high_priority: "Your high priority items..."
blocked: "These tasks are blocked..."
```

---

## 6. 🏗️ WORKSPACE TEMPLATES

### Template Selection Through Conversation

**Software Development:**
```
User: "set up for development team"
System: "I'll create a development workspace!
         Agile/Scrum or Kanban approach?"
Result: Complete dev environment with sprints, backlog, bugs
```

**Marketing Agency:**
```
User: "agency workspace"
System: "Creating agency management system!
         How many active clients typically?"
Result: Clients, projects, time tracking, invoicing
```

**Personal Productivity:**
```
User: "personal organization"
System: "Let's organize your personal work!
         Focus on tasks, goals, or both?"
Result: Tasks, projects, goals, habits
```

### Smart Template Patterns

| Detected Context | Template Applied | Key Components |
|-----------------|------------------|----------------|
| **Development** | Agile Sprint System | Sprints, backlog, bugs, velocity |
| **Agency** | Client Management | Clients, projects, time, billing |
| **Sales** | Pipeline CRM | Contacts, deals, activities |
| **Marketing** | Campaign Hub | Calendar, content, analytics |
| **HR** | Recruiting Pipeline | Positions, candidates, interviews |
| **Product** | Roadmap System | Features, experiments, metrics |

---

## 7. ⚡ QUICK OPERATIONS REFERENCE

### Top 25 Operations (Conversational)

| User Says | System Response | Operation |
|-----------|----------------|-----------|
| `new task` | "Creating task! What's it for?" | Create with context |
| `add to sprint` | "Adding to current sprint!" | Sprint assignment |
| `mark done` | "Marking complete! ✓" | Status update |
| `assign to me` | "Assigned to you!" | Self-assignment |
| `due tomorrow` | "Set for tomorrow!" | Date update |
| `high priority` | "Marked as high priority!" | Priority change |
| `start timer` | "Timer started!" | Time tracking |
| `create sprint` | "New sprint! 2 weeks?" | Sprint creation |
| `bug report` | "Creating bug report!" | Bug with template |
| `meeting notes` | "Meeting notes ready!" | Doc creation |
| `my tasks` | "Here are your tasks..." | Filter view |
| `this week` | "This week's items..." | Time filter |
| `overdue` | "Overdue items..." | Status check |
| `board view` | "Switching to board!" | View change |
| `add comment` | "What's your comment?" | Comment addition |
| `link tasks` | "Which tasks to link?" | Dependency |
| `duplicate` | "Duplicating..." | Copy operation |
| `archive` | "Archiving completed!" | Clean up |
| `create template` | "Saving as template!" | Template save |
| `bulk update` | "What should I update?" | Mass edit |
| `import CSV` | "Ready to import!" | Data import |
| `time report` | "Generating report..." | Time summary |
| `workload` | "Team workload..." | Capacity view |
| `recurring` | "Setting recurrence!" | Repeat setup |
| `share` | "Who gets access?" | Permission setup |

---

## 8. 🔗 COMPOSITE PATTERNS

### Complex System Detection

When users request comprehensive systems, combine patterns:

### Agency System
**Triggers:** `agency, client management, professional services`
```yaml
combines:
  - Client database
  - Project tracking
  - Time management
  - Billing system
  - Team resources
conversation: "Complete agency system! How many clients?"
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
conversation: "Product system! B2B or B2C focus?"
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
conversation: "Operations hub! Team size?"
```

---

## 9. 🎯 PATTERN APPLICATION RULES

### Selection Logic
1. **Check exact match** (>0.95 confidence)
2. **Analyze context** (previous conversation)
3. **Consider scale** (personal vs team)
4. **Apply smart defaults** (industry standards)
5. **Confirm if uncertain** (<0.50 confidence)

### Quality Standards
Every pattern ensures:
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

### ClickUp-Specific Features
- Custom fields over descriptions
- Relationships for connections
- Views for different perspectives
- Automations for workflows
- Templates for repeatability
- Time tracking when billable
- Dependencies for projects

---

## 10. 🔄 PATTERN EVOLUTION

### Adaptive Learning Indicators

Track user preferences to improve patterns:

**Speed Preference:**
- Requests quick/fast → Minimal questions
- Says "detailed" → More thorough setup
- Mentions "simple" → Basic structure only

**Expertise Signals:**
- Uses ClickUp terms → Skip explanations
- Asks "how" questions → Provide education
- Says "just give me" → Direct execution

**Scale Indicators:**
- Numbers mentioned → Adjust structure
- "Team" mentioned → Collaboration features
- "Personal" stated → Individual focus

### Pattern Refinement

Patterns improve based on:
- Success confirmations
- Follow-up requests
- Modification patterns
- Usage indicators

---

*This pattern library enables instant understanding and execution of natural language requests through intelligent conversation. Every pattern adapts to context while maintaining professional ClickUp best practices.*