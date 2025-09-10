# Notion - Patterns & Operations - v0.100

Comprehensive pattern library and operation reference for natural language to Notion mapping.

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring
| Confidence | Range | Action | Example |
|------------|-------|--------|---------|
| **Exact** | >0.95 | Execute immediately | "project tracker" |
| **High** | 0.80-0.95 | Proceed with defaults | "track projects" |
| **Medium** | 0.50-0.79 | Confirm understanding | "organizer" |
| **Low** | <0.50 | Use interactive mode | "help with stuff" |

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

### Project Tracker
**Triggers:** `project tracker, project management, track projects, client work`

**Implementation:**
```yaml
properties: Title, Status[Planning→In Progress→Complete], Priority[H/M/L], Deadline(date), Owner(person), Progress%
views: Active(table), Timeline(calendar), By Status(board)
template: Standard project template included
```

### Task Management
**Triggers:** `task list, todo list, action items, things to do`

**Implementation:**
```yaml
properties: Task, Done(checkbox), Due(date), Priority[High/Med/Low], Category, Assigned(person)
views: Today(filtered), This Week(table), By Priority(board)
filters: Overdue items highlighted red
```

### Meeting Notes
**Triggers:** `meeting notes, meeting tracker, team meeting, client call`

**Implementation:**
```yaml
page_template: Date, Attendees(people), Type[Team/Client/1-on-1]
sections: Agenda(bullets), Notes, Action Items(todos), Next Steps
automation: Links to calendar if date property exists
```

### Content Calendar
**Triggers:** `content calendar, editorial calendar, publishing schedule, blog calendar`

**Implementation:**
```yaml
properties: Title, Status[Idea→Writing→Scheduled→Published], Publish Date, Platform(multi), Author
views: Calendar(by date), Pipeline(board by status), This Month(filtered)
extras: URL field for published content
```

### Knowledge Base
**Triggers:** `wiki, documentation, knowledge base, notes database, reference`

**Implementation:**
```yaml
properties: Title, Category[Process/Reference/Tutorial], Tags(multi), Last Updated, Status
views: All Docs(table), By Category(board), Recently Updated(filtered)
features: Self-referencing relations for connected docs
```

### CRM System
**Triggers:** `CRM, customer database, client tracker, contact management`

**Implementation:**
```yaml
contacts_db: Name, Company, Email, Phone, Last Contact, Status, Notes
companies_db: Name, Industry, Contacts(relation), Projects(relation), Value
relationships: Contacts ↔ Companies, Companies → Projects
dashboard: Recent interactions, Pipeline view
```

---

## 3. 🔄 UPDATE OPERATIONS

| Operation | Triggers | Action | Result |
|-----------|----------|--------|--------|
| **Mark Complete** | `done, complete, finish, check off` | Update status/checkbox | "✅ Marked complete" |
| **Change Date** | `reschedule, move to, postpone, due [date]` | Update date property | "📅 Rescheduled" |
| **Assign** | `assign to, delegate, give to, for [person]` | Set person property | "👤 Assigned to [name]" |
| **Add Note** | `add note, comment, include, update with` | Append to text/comments | "📝 Note added" |
| **Change Status** | `set status, mark as, change to` | Update select property | "🔄 Status updated" |

### Date Parsing
```
"tomorrow" → +1 day
"next week" → +7 days
"Monday" → upcoming Monday
"end of month" → last day of current month
"Dec 15" → December 15, current year
```

---

## 4. 🗂️ ORGANIZATION OPERATIONS

### Archive
**Triggers:** `archive, clean up, move old, hide completed`

**Logic:**
```yaml
criteria: Status=Complete AND Modified>30 days
destination: /Archive/[Year]/[Type]/
preserve: All relations and properties
update_views: Exclude archived items
```

### Group/View Creation
**Triggers:** `group by, organize by, show by, view by`

**View Types:**
```yaml
board: Group by status/category/priority
calendar: By date property
table: All properties visible
list: Minimal, mobile-friendly
gallery: Visual with covers
```

### Dashboard
**Triggers:** `dashboard, overview, home page, control center`

**Structure:**
```yaml
sections:
  - Active items (filtered view)
  - Upcoming deadlines
  - Recent updates
  - Quick links
  - Key metrics
```

### Hierarchy
**Triggers:** `create structure, organize hierarchy, parent-child`

**Patterns:**
- Page hierarchy: Max 3 levels deep
- Database relations: Parent/child properties
- Mixed: Pages with embedded databases

---

## 5. 🔍 QUERY OPERATIONS

### Time-Based Queries
| Query | Filter Logic | Sort |
|-------|-------------|------|
| **Today** | `date = today() OR (overdue AND !complete)` | Priority, Time |
| **This Week** | `date >= start_of_week() AND <= end_of_week()` | Date ascending |
| **Overdue** | `date < today() AND status != Complete` | Date ascending |
| **This Month** | `date in current_month()` | Date ascending |

### Person Queries
| Query | Filter Logic |
|-------|-------------|
| **My Items** | `assigned = current_user()` |
| **Unassigned** | `assigned is empty` |
| **Team Items** | `assigned in team_members()` |
| **By Person** | `group by assigned_to` |

### Status Queries
| Query | Filter Logic |
|-------|-------------|
| **Active** | `status in [In Progress, Active]` |
| **Completed** | `status = Complete` |
| **Needs Attention** | `status in [Blocked, At Risk]` |
| **Not Started** | `status = Not Started` |

---

## 6. 📦 BULK OPERATIONS

| Operation | Triggers | Process | Confirmation |
|-----------|----------|---------|--------------|
| **Bulk Complete** | `mark all done, complete all` | Update in batches of 50 | "✅ Updated X items" |
| **Bulk Create** | `add list, create multiple` | Parse list, create items | "✅ Created X items" |
| **Bulk Archive** | `archive all completed` | Move to archive | "📦 Archived X items" |
| **Bulk Assign** | `assign all to` | Update person property | "👥 Assigned X items" |

### List Parsing
```
Detects: Line breaks, commas, bullets, numbers
Extracts: Dates (@tomorrow), People (@john), Tags (#urgent)
```

---

## 7. 🏗️ WORKSPACE TEMPLATES

### Business Management System
```yaml
components:
  - CRM (clients, contacts)
  - Projects (linked to clients)
  - Tasks (linked to projects)
  - Time Tracking (linked to tasks)
  - Invoicing (from time entries)
connections: Clients → Projects → Tasks → Time → Invoices
dashboard: Pipeline, Active Projects, Time This Week
```

### Personal Productivity System
```yaml
components:
  - Goals & OKRs (quarterly)
  - Projects (linked to goals)
  - Tasks (daily execution)
  - Habits (tracking)
  - Notes (capture)
structure: Areas → Projects → Tasks
reviews: Weekly, Monthly, Quarterly
```

### Team Workspace
```yaml
components:
  - Team Wiki (documentation)
  - Projects (shared)
  - Tasks (assigned)
  - Meetings (notes & actions)
  - Resources (shared files)
permissions: Team edit, guests view
```

### Content System
```yaml
components:
  - Content Calendar
  - Ideas Database
  - Production Pipeline
  - Analytics Tracking
workflow: Idea → Draft → Review → Publish → Analyze
```

---

## 8. ⚡ QUICK OPERATIONS REFERENCE

### Top 20 Operations

| Trigger | Operation | Time | Confidence Required |
|---------|-----------|------|-------------------|
| `new project` | Create project with template | 2s | 0.90 |
| `add task` | Add to tasks or create system | 1s | 0.95 |
| `mark done` | Update status/checkbox | 1s | 0.95 |
| `meeting tomorrow` | Create meeting note | 2s | 0.90 |
| `find [item]` | Search workspace | 1s | 0.85 |
| `archive old` | Move completed to archive | 3s | 0.85 |
| `my tasks` | Filter by current user | 1s | 0.95 |
| `this week` | Create week view | 1s | 0.95 |
| `assign to [person]` | Update person property | 1s | 0.90 |
| `create dashboard` | Build overview page | 5s | 0.80 |
| `group by status` | Create board view | 2s | 0.90 |
| `reschedule` | Update date property | 1s | 0.90 |
| `duplicate` | Copy with structure | 2s | 0.95 |
| `share with team` | Update permissions | 2s | 0.85 |
| `import CSV` | Create from data | 3s | 0.85 |
| `weekly review` | Create review template | 3s | 0.85 |
| `link to [item]` | Create relation | 2s | 0.85 |
| `calendar view` | Create by date property | 2s | 0.95 |
| `export` | Generate CSV | 2s | 0.95 |
| `lock database` | Protect structure | 1s | 0.90 |

---

## 9. 🔗 COMPOSITE PATTERNS

### CRM + Projects
```yaml
trigger: "track clients and projects"
creates:
  - Clients database
  - Projects database with client relation
  - Automatic value rollups
  - Client dashboard with project list
```

### Tasks + Time
```yaml
trigger: "tasks with time tracking"
creates:
  - Tasks with estimated/actual hours
  - Time entries linked to tasks
  - Daily/weekly time reports
  - Billable/non-billable toggle
```

### Content + Analytics
```yaml
trigger: "content with performance"
creates:
  - Content database
  - Analytics tracking
  - Performance dashboard
  - ROI calculations
```

### Knowledge + Learning
```yaml
trigger: "learning system"
creates:
  - Resources database
  - Progress tracking
  - Study calendar
  - Review system
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
- Essential properties only
- Helpful default views
- Scalable structure
- Clear naming
- Best practices applied

### Performance Guidelines
- Small database: <1,000 items (instant)
- Medium: 1,000-10,000 (use filters)
- Large: 10,000-50,000 (aggressive filtering + archive)
- Very large: >50,000 (split databases)

---

*This pattern library enables instant understanding and execution of natural language requests. By mapping triggers to implementations efficiently, the assistant provides professional Notion structures in seconds.*