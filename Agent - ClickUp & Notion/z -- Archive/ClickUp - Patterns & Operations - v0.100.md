# ClickUp - Patterns & Operations - v0.100

Comprehensive pattern library and operation reference for natural language to ClickUp mapping.

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring
| Confidence | Range | Action | Example |
|------------|-------|--------|---------|
| **Exact** | >0.95 | Execute immediately | "sprint board" |
| **High** | 0.80-0.95 | Proceed with defaults | "track sprints" |
| **Medium** | 0.50-0.79 | Confirm understanding | "agile stuff" |
| **Low** | <0.50 | Use interactive mode | "help with work" |

### Pattern Matching Hierarchy
```
1. Exact Match → Direct pattern execution
2. Synonym Recognition → Map to known pattern  
3. Category Detection → Identify pattern group
4. Composite Understanding → Combine patterns
5. Context Inference → Use workspace/history
```

---

## 2. ✨ CREATION OPERATIONS

### Sprint Planning
**Triggers:** `sprint board, sprint planning, agile sprints, scrum board`

**Implementation:**
```yaml
list_name: Sprint [Number]
custom_fields: 
  - Story Points (number)
  - Sprint Goal (text)
  - Acceptance Criteria (text)
  - Epic (dropdown)
statuses: Backlog→To Do→In Progress→Review→Done
views: Board(default), List, Calendar, Gantt
template: Sprint planning template included
```

### Task Management
**Triggers:** `task list, todo list, action items, things to do`

**Implementation:**
```yaml
custom_fields:
  - Priority (Urgent/High/Normal/Low)
  - Due Date (date)
  - Time Estimate (duration)
  - Tags (labels)
statuses: To Do→In Progress→Review→Complete
views: List(default), Board, Calendar, Me Mode
automations: Due date reminders enabled
```

### Bug Tracking
**Triggers:** `bug tracker, issue tracking, bug list, defects`

**Implementation:**
```yaml
custom_fields:
  - Severity (Critical/High/Medium/Low)
  - Environment (Dev/Staging/Prod)
  - Steps to Reproduce (text)
  - Expected vs Actual (text)
  - Reporter (user)
statuses: New→Confirmed→In Progress→Testing→Resolved→Closed
views: List(priority), Board(status), Calendar(found date)
```

### Client Projects
**Triggers:** `client work, client projects, agency projects, customer work`

**Implementation:**
```yaml
space_structure:
  - Clients (folder)
    - [Client Name] (list per client)
custom_fields:
  - Project Value (money)
  - Timeline (date range)
  - Client Contact (user)
  - Status (Planning/Active/Review/Complete)
  - Deliverables (checklist)
views: List, Board, Gantt(timeline), Calendar
```

### Content Calendar
**Triggers:** `content calendar, editorial calendar, publishing schedule, social calendar`

**Implementation:**
```yaml
custom_fields:
  - Publish Date (date)
  - Channel (Social/Blog/Email/Video)
  - Status (Idea→Draft→Review→Scheduled→Published)
  - Author (user)
  - Performance (number)
views: Calendar(primary), Board(by status), List, Table
automations: Publishing reminders
```

### OKR Tracking
**Triggers:** `OKRs, objectives, goals, key results`

**Implementation:**
```yaml
hierarchy:
  - Objectives (folder)
    - Key Results (lists)
custom_fields:
  - Quarter (Q1/Q2/Q3/Q4)
  - Progress (percentage)
  - Owner (user)
  - Status (On Track/At Risk/Behind)
views: List(by objective), Progress(dashboard), Timeline
```

### Meeting Notes
**Triggers:** `meeting notes, meeting tracker, team meetings, 1-on-1s`

**Implementation:**
```yaml
doc_template:
  - Date & Attendees
  - Agenda items
  - Discussion notes
  - Action items (tasks)
  - Next steps
task_creation: Action items become tasks
recurring: Weekly/monthly templates
```

---

## 3. 🔄 UPDATE OPERATIONS

| Operation | Triggers | Action | Result |
|-----------|----------|--------|--------|
| **Complete Task** | `done, complete, finish, check off` | Update status to Done | "✅ Marked complete" |
| **Change Due Date** | `reschedule, move to, postpone, due [date]` | Update due date field | "📅 Rescheduled" |
| **Assign Task** | `assign to, delegate, give to, for [person]` | Set assignee field | "👤 Assigned to [name]" |
| **Add Comment** | `add note, comment, mention, update with` | Add to comments | "💬 Comment added" |
| **Change Status** | `set status, mark as, move to [status]` | Update status field | "🔄 Status updated" |
| **Set Priority** | `urgent, high priority, low priority` | Update priority field | "🚨 Priority set" |
| **Add Time** | `log time, add hours, track time` | Add time entry | "⏱️ Time logged" |

### Date Parsing
```
"tomorrow" → +1 day
"next week" → +7 days
"Monday" → upcoming Monday
"end of month" → last day of current month
"Dec 15" → December 15, current year
"in 2 hours" → +2 hours from now
```

---

## 4. 🗂️ ORGANIZATION OPERATIONS

### Archive
**Triggers:** `archive, clean up, move old, hide completed`

**Logic:**
```yaml
criteria: Status=Complete AND Modified>30 days
destination: Archived folder in space
preserve: All fields and relationships
update_views: Exclude archived items
automation: Auto-archive after X days
```

### View Creation
**Triggers:** `show as, view by, group by, filter by`

**View Types:**
```yaml
board: Group by status/assignee/priority
calendar: By due date/start date
gantt: Timeline with dependencies
list: All tasks with filters
table: Spreadsheet view
timeline: Project timeline
activity: Recent changes
map: Location-based
workload: Team capacity
```

### Space Organization
**Triggers:** `create space, organize by department, team structure`

**Structure:**
```yaml
space:
  - Folders (categories)
    - Lists (work items)
      - Tasks (individual items)
hierarchy_depth: Maximum 5 levels
permissions: Space-level control
```

### Dashboard Creation
**Triggers:** `dashboard, overview, metrics, KPIs`

**Components:**
```yaml
widgets:
  - Task distribution
  - Status overview
  - Time tracked
  - Velocity chart
  - Custom calculations
  - Goal progress
  - Team workload
layout: Customizable grid
```

---

## 5. 🔍 QUERY OPERATIONS

### Time-Based Queries
| Query | Filter Logic | Sort |
|-------|-------------|------|
| **Today** | `due_date = today() OR (overdue AND !complete)` | Priority, Time |
| **This Week** | `due_date >= start_of_week() AND <= end_of_week()` | Due date ascending |
| **Overdue** | `due_date < today() AND status != Complete` | Due date ascending |
| **This Sprint** | `sprint = current_sprint()` | Priority descending |
| **This Month** | `due_date in current_month()` | Due date ascending |

### Assignee Queries
| Query | Filter Logic |
|-------|-------------|
| **My Tasks** | `assignees contains current_user()` |
| **Unassigned** | `assignees is empty` |
| **Team Tasks** | `assignees in team_members()` |
| **By Person** | `group by assignees` |
| **Workload** | `assignees with sum(time_estimate)` |

### Status Queries
| Query | Filter Logic |
|-------|-------------|
| **Active** | `status in [In Progress, Review]` |
| **Blocked** | `status = Blocked OR dependencies blocked` |
| **Completed** | `status = Done OR Complete` |
| **Ready** | `status = To Do AND no blockers` |

### Priority Queries
| Query | Filter Logic |
|-------|-------------|
| **Urgent** | `priority = Urgent` |
| **High Priority** | `priority in [Urgent, High]` |
| **Quick Wins** | `time_estimate < 1h AND priority >= Normal` |

---

## 6. 📦 BULK OPERATIONS

| Operation | Triggers | Process | Confirmation |
|-----------|----------|---------|--------------|
| **Bulk Complete** | `mark all done, complete all` | Update in batches of 100 | "✅ Updated X tasks" |
| **Bulk Create** | `add list, create multiple, import` | Parse and create items | "✅ Created X tasks" |
| **Bulk Archive** | `archive completed, clean up` | Move to archive | "📦 Archived X items" |
| **Bulk Assign** | `assign all to` | Update assignee field | "👥 Assigned X tasks" |
| **Bulk Reschedule** | `move all to [date]` | Update due dates | "📅 Rescheduled X tasks" |
| **Bulk Tag** | `tag all with` | Add tags to items | "🏷️ Tagged X items" |

### List Parsing
```
Detects: Line breaks, commas, bullets, numbers
Extracts: Dates (@tomorrow), People (@john), Priority (!high), Time (2h)
Creates: Individual tasks with parsed attributes
```

---

## 7. 🏗️ WORKSPACE TEMPLATES

### Software Development
```yaml
structure:
  - Development Space
    - Sprints (folder)
      - Sprint 1, 2, 3... (lists)
    - Backlog (list)
    - Bugs (list)
    - Features (list)
    - Releases (folder)
custom_fields: Story Points, Epic, Sprint, Component
automations: Sprint rollover, bug escalation
dashboards: Velocity, burndown, bug trends
```

### Marketing Agency
```yaml
structure:
  - Clients (space)
    - [Client Name] (folder)
      - Projects (list)
      - Tasks (list)
      - Assets (docs)
  - Campaigns (space)
    - Active (folder)
    - Planning (folder)
    - Archive (folder)
custom_fields: Client, Budget, ROI, Channel
views: Calendar, Gantt, Board
```

### Product Management
```yaml
structure:
  - Product Space
    - Roadmap (list with timeline)
    - Features (list)
    - User Feedback (list)
    - Experiments (list)
    - Metrics (dashboard)
relationships: Features→Experiments→Metrics
custom_fields: Impact, Effort, RICE Score
```

### Sales Pipeline
```yaml
structure:
  - Sales Space
    - Leads (list)
    - Opportunities (list)
    - Accounts (list)
    - Activities (list)
stages: Lead→Qualified→Proposal→Negotiation→Closed
custom_fields: Deal Value, Probability, Close Date
automations: Stage progression, activity reminders
```

### HR & Recruiting
```yaml
structure:
  - Recruiting Space
    - Open Positions (list)
    - Candidates (list)
    - Interviews (list)
    - Onboarding (list)
pipeline: Applied→Screened→Interview→Offer→Hired
custom_fields: Position, Salary Range, Start Date
```

---

## 8. ⚡ QUICK OPERATIONS REFERENCE

### Top 25 Operations

| Trigger | Operation | Time | Confidence Required |
|---------|-----------|------|-------------------|
| `new task` | Create task with defaults | 1s | 0.95 |
| `add to sprint` | Add task to current sprint | 1s | 0.90 |
| `mark done` | Update status to complete | 1s | 0.95 |
| `assign to me` | Set current user as assignee | 1s | 0.95 |
| `due tomorrow` | Set due date to tomorrow | 1s | 0.95 |
| `high priority` | Set priority to high | 1s | 0.95 |
| `start timer` | Begin time tracking | 1s | 0.90 |
| `create sprint` | New sprint list with template | 3s | 0.90 |
| `bug report` | Create bug with template | 2s | 0.90 |
| `meeting notes` | Create meeting doc | 2s | 0.90 |
| `my tasks` | Filter by current user | 1s | 0.95 |
| `this week` | Show week view | 1s | 0.95 |
| `overdue` | Show overdue items | 1s | 0.95 |
| `board view` | Switch to kanban board | 1s | 0.95 |
| `add comment` | Add comment to task | 1s | 0.90 |
| `link tasks` | Create dependency | 2s | 0.85 |
| `duplicate` | Copy task/list | 2s | 0.90 |
| `archive` | Move to archive | 2s | 0.90 |
| `create template` | Save as template | 2s | 0.85 |
| `bulk update` | Update multiple items | 3s | 0.85 |
| `import CSV` | Create from data | 3s | 0.85 |
| `time report` | Generate time summary | 2s | 0.85 |
| `workload view` | Show team capacity | 2s | 0.85 |
| `recurring task` | Set up recurrence | 2s | 0.85 |
| `guest access` | Configure permissions | 2s | 0.80 |

---

## 9. 🔗 COMPOSITE PATTERNS

### Sprint + Backlog
```yaml
trigger: "agile development setup"
creates:
  - Product backlog list
  - Sprint lists (templated)
  - Sprint planning automation
  - Velocity tracking dashboard
```

### Client + Time
```yaml
trigger: "billable client work"
creates:
  - Client space structure
  - Time tracking custom fields
  - Billable/non-billable toggle
  - Invoice preparation views
```

### Goals + Tasks
```yaml
trigger: "goal tracking system"
creates:
  - Goals/OKRs lists
  - Linked task lists
  - Progress rollups
  - Quarterly review templates
```

### Campaign + Content
```yaml
trigger: "marketing campaign"
creates:
  - Campaign brief doc
  - Content production list
  - Asset library
  - Performance tracking
```

### Pipeline + Activities
```yaml
trigger: "sales process"
creates:
  - Deal pipeline
  - Activity tracking
  - Contact management
  - Forecast dashboards
```

---

## 10. 🎯 PATTERN APPLICATION

### Selection Logic
1. Check exact trigger match (>0.95 confidence)
2. Analyze context clues
3. Consider user history
4. Apply smart defaults
5. Ask only if <0.50 confidence

### Quality Standards
Every pattern creates:
- Essential custom fields only
- Helpful default views
- Scalable structure
- Clear naming
- Best practices applied

### Performance Guidelines
- Small list: <1,000 tasks (instant)
- Medium: 1,000-5,000 (use filters)
- Large: 5,000-25,000 (aggressive filtering + folders)
- Very large: >25,000 (split into spaces)

### ClickUp-Specific Optimizations
- Use custom fields over description parsing
- Leverage ClickApps when beneficial
- Enable time tracking for billable work
- Use dependencies for complex projects
- Configure automations for recurring patterns

---

*This pattern library enables instant understanding and execution of natural language requests. By mapping triggers to ClickUp implementations efficiently, the assistant provides professional workspace structures in seconds.*