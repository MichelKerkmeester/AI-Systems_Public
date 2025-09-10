# Notion - Patterns & Operations - v0.120

Comprehensive pattern library and operation reference for natural language to Notion mapping with integrated thinking framework.

## 📑 Table of Contents

1. [🎯 Intent Recognition Engine](#1--intent-recognition-engine)
2. [✨ Creation Operations](#2--creation-operations)
3. [🔄 Update Operations](#3--update-operations)
4. [🗂️ Organization Operations](#4-️-organization-operations)
5. [🔍 Query Operations](#5--query-operations)
6. [📦 Bulk Operations](#6--bulk-operations)
7. [🗏 Workspace Templates](#7-️-workspace-templates)
8. [⚡ Quick Operations Reference](#8--quick-operations-reference)
9. [🔗 Composite Patterns](#9--composite-patterns)
10. [🎯 Pattern Application](#10--pattern-application)

---

## 1. 🎯 INTENT RECOGNITION ENGINE

### Confidence Scoring with Thinking Guidance
| Confidence | Range | Action | Thinking Rounds | Example |
|------------|-------|--------|-----------------|---------|
| **Exact** | >0.95 | Execute immediately | Ask: 2-3 recommended | "project tracker" |
| **High** | 0.80-0.95 | Proceed with defaults | Ask: 3-5 recommended | "track projects" |
| **Medium** | 0.50-0.79 | Confirm understanding | Ask: 5-7 recommended | "organizer" |
| **Low** | <0.50 | Use full guidance | Ask: 7-10 recommended | "help with stuff" |

### Pattern Matching Hierarchy
```
1. Exact Match → Direct pattern execution (2-3 thinking rounds)
2. Synonym Recognition → Map to known pattern (3-4 thinking rounds)
3. Category Detection → Identify pattern group (4-6 thinking rounds)
4. Composite Understanding → Combine patterns (6-8 thinking rounds)
5. Context Inference → Use workspace/history (7-10 thinking rounds)
```

### Intent Categories with Thinking Defaults
- **Workspace Creation**: CRM, project management, business systems (7-10 rounds)
- **Content Creation**: Pages, notes, documentation (2-4 rounds)
- **Organization**: Archive, clean up, restructure (5-7 rounds)
- **Query**: Search, filter, find items (2-3 rounds)
- **Update**: Status changes, assignments, dates (2-3 rounds)

---

## 2. ✨ CREATION OPERATIONS

### Project Tracker
**Triggers:** `project tracker, project management, track projects, client work`
**Recommended Thinking:** 4-6 rounds

**Implementation:**
```yaml
properties: Title, Status[Planning→In Progress→Complete], Priority[H/M/L], Deadline(date), Owner(person), Progress%
views: Active(table), Timeline(calendar), By Status(board)
template: Standard project template included
thinking_approach: "I'll use X rounds to optimize project workflow and views"
```

### Task Management
**Triggers:** `task list, todo list, action items, things to do, tasks`
**Recommended Thinking:** 3-5 rounds

**Implementation:**
```yaml
properties: Task, Done(checkbox), Due(date), Priority[High/Med/Low], Category, Assigned(person)
views: Today(filtered), This Week(table), By Priority(board)
filters: Overdue items highlighted red
thinking_approach: "X rounds to balance simplicity with functionality"
```

### Meeting Notes
**Triggers:** `meeting notes, meeting tracker, team meeting, client call`
**Recommended Thinking:** 2-3 rounds

**Implementation:**
```yaml
page_template: Date, Attendees(people), Type[Team/Client/1-on-1]
sections: Agenda(bullets), Notes, Action Items(todos), Next Steps
automation: Links to calendar if date property exists
thinking_approach: "Quick X rounds for standard structure"
```

### Content Calendar
**Triggers:** `content calendar, editorial calendar, publishing schedule, blog calendar`
**Recommended Thinking:** 4-5 rounds

**Implementation:**
```yaml
properties: Title, Status[Idea→Writing→Scheduled→Published], Publish Date, Platform(multi), Author
views: Calendar(by date), Pipeline(board by status), This Month(filtered)
extras: URL field for published content
thinking_approach: "X rounds to plan publication workflow"
```

### Knowledge Base
**Triggers:** `wiki, documentation, knowledge base, notes database, reference`
**Recommended Thinking:** 5-7 rounds

**Implementation:**
```yaml
properties: Title, Category[Process/Reference/Tutorial], Tags(multi), Last Updated, Status
views: All Docs(table), By Category(board), Recently Updated(filtered)
features: Self-referencing relations for connected docs
thinking_approach: "X rounds for scalable information architecture"
```

### CRM System
**Triggers:** `CRM, customer database, client tracker, contact management, track clients`
**Recommended Thinking:** 7-10 rounds

**Implementation:**
```yaml
contacts_db: Name, Company, Email, Phone, Last Contact, Status, Notes
companies_db: Name, Industry, Contacts(relation), Projects(relation), Value
relationships: Contacts ↔ Companies, Companies → Projects
dashboard: Recent interactions, Pipeline view
thinking_approach: "X rounds to design interconnected databases"
```

---

## 3. 🔄 UPDATE OPERATIONS

| Operation | Triggers | Action | Thinking | Result |
|-----------|----------|--------|----------|--------|
| **Mark Complete** | `done, complete, finish, check off` | Update status/checkbox | 2 rounds | "✅ Marked complete" |
| **Change Date** | `reschedule, move to, postpone, due [date]` | Update date property | 2 rounds | "📅 Rescheduled" |
| **Assign** | `assign to, delegate, give to, for [person]` | Set person property | 2 rounds | "👤 Assigned to [name]" |
| **Add Note** | `add note, comment, include, update with` | Append to text/comments | 2 rounds | "📝 Note added" |
| **Change Status** | `set status, mark as, change to` | Update select property | 2-3 rounds | "🔄 Status updated" |

### Date Parsing with Thinking
```
"tomorrow" → +1 day (1 round of thinking)
"next week" → +7 days (1 round)
"Monday" → upcoming Monday (2 rounds for context)
"end of month" → last day of current month (2 rounds)
"Dec 15" → December 15, current year (2 rounds)
```

---

## 4. 🗂️ ORGANIZATION OPERATIONS

### Archive
**Triggers:** `archive, clean up, move old, hide completed, organize old`
**Recommended Thinking:** 5-7 rounds

**Logic:**
```yaml
criteria: Status=Complete AND Modified>30 days
destination: /Archive/[Year]/[Type]/
preserve: All relations and properties
update_views: Exclude archived items
thinking_approach: "X rounds to safely preserve all relationships"
```

### Group/View Creation
**Triggers:** `group by, organize by, show by, view by`
**Recommended Thinking:** 3-4 rounds

**View Types:**
```yaml
board: Group by status/category/priority
calendar: By date property
table: All properties visible
list: Minimal, mobile-friendly
gallery: Visual with covers
thinking_approach: "X rounds to optimize for use case"
```

### Dashboard
**Triggers:** `dashboard, overview, home page, control center`
**Recommended Thinking:** 6-8 rounds

**Structure:**
```yaml
sections:
  - Active items (filtered view)
  - Upcoming deadlines
  - Recent updates
  - Quick links
  - Key metrics
thinking_approach: "X rounds to design comprehensive overview"
```

### Reorganization
**Triggers:** `reorganize, restructure, clean up workspace, workspace is a mess`
**Recommended Thinking:** 8-10 rounds

**Process:**
```yaml
analysis: Scan existing content
structure: Create organized hierarchy
migration: Move items to new structure
archive: Old/completed items
dashboard: Create overview
thinking_approach: "X rounds for complete restructuring"
```

---

## 5. 🔍 QUERY OPERATIONS

### Time-Based Queries
| Query | Filter Logic | Sort | Thinking |
|-------|-------------|------|----------|
| **Today** | `date = today() OR (overdue AND !complete)` | Priority, Time | 2 rounds |
| **This Week** | `date >= start_of_week() AND <= end_of_week()` | Date ascending | 2 rounds |
| **Overdue** | `date < today() AND status != Complete` | Date ascending | 2-3 rounds |
| **This Month** | `date in current_month()` | Date ascending | 2 rounds |

### Person Queries
| Query | Filter Logic | Thinking |
|-------|-------------|----------|
| **My Items** | `assigned = current_user()` | 2 rounds |
| **Unassigned** | `assigned is empty` | 2 rounds |
| **Team Items** | `assigned in team_members()` | 3 rounds |
| **By Person** | `group by assigned_to` | 3 rounds |

### Status Queries
| Query | Filter Logic | Thinking |
|-------|-------------|----------|
| **Active** | `status in [In Progress, Active]` | 2 rounds |
| **Completed** | `status = Complete` | 2 rounds |
| **Needs Attention** | `status in [Blocked, At Risk]` | 3 rounds |
| **Not Started** | `status = Not Started` | 2 rounds |

---

## 6. 📦 BULK OPERATIONS

| Operation | Triggers | Process | Thinking | Confirmation |
|-----------|----------|---------|----------|--------------|
| **Bulk Complete** | `mark all done, complete all` | Update in batches of 50 | 3-4 rounds | "✅ Updated X items" |
| **Bulk Create** | `add list, create multiple` | Parse list, create items | 4-5 rounds | "✅ Created X items" |
| **Bulk Archive** | `archive all completed` | Move to archive | 5-6 rounds | "📦 Archived X items" |
| **Bulk Assign** | `assign all to` | Update person property | 3-4 rounds | "👥 Assigned X items" |

### List Parsing with Thinking
```
Detects: Line breaks, commas, bullets, numbers (2 rounds)
Extracts: Dates (@tomorrow), People (@john), Tags (#urgent) (3 rounds)
Validates: Structure and consistency (4 rounds)
```

---

## 7. 🗏 WORKSPACE TEMPLATES

### Business Management System
```yaml
trigger: "business system, track everything for business"
recommended_thinking: 8-10 rounds
components:
  - CRM (clients, contacts)
  - Projects (linked to clients)
  - Tasks (linked to projects)
  - Time Tracking (linked to tasks)
  - Invoicing (from time entries)
connections: Clients → Projects → Tasks → Time → Invoices
dashboard: Pipeline, Active Projects, Time This Week
thinking_focus: "Integration and automation between components"
```

### Personal Productivity System
```yaml
trigger: "personal productivity, organize my life"
recommended_thinking: 6-8 rounds
components:
  - Goals & OKRs (quarterly)
  - Projects (linked to goals)
  - Tasks (daily execution)
  - Habits (tracking)
  - Notes (capture)
structure: Areas → Projects → Tasks
reviews: Weekly, Monthly, Quarterly
thinking_focus: "Balance and sustainability"
```

### Team Workspace
```yaml
trigger: "team workspace, team collaboration"
recommended_thinking: 7-9 rounds
components:
  - Team Wiki (documentation)
  - Projects (shared)
  - Tasks (assigned)
  - Meetings (notes & actions)
  - Resources (shared files)
permissions: Team edit, guests view
thinking_focus: "Collaboration and permissions"
```

### Content System
```yaml
trigger: "content system, content creation"
recommended_thinking: 5-7 rounds
components:
  - Content Calendar
  - Ideas Database
  - Production Pipeline
  - Analytics Tracking
workflow: Idea → Draft → Review → Publish → Analyze
thinking_focus: "Content workflow optimization"
```

---

## 8. ⚡ QUICK OPERATIONS REFERENCE

### Top 20 Operations with Thinking Guidance

| Trigger | Operation | Time | Confidence | Thinking |
|---------|-----------|------|------------|----------|
| `new project` | Create project with template | 2s | 0.90 | 3-4 rounds |
| `add task` | Add to tasks or create system | 1s | 0.95 | 2-3 rounds |
| `mark done` | Update status/checkbox | 1s | 0.95 | 2 rounds |
| `meeting tomorrow` | Create meeting note | 2s | 0.90 | 2-3 rounds |
| `find [item]` | Search workspace | 1s | 0.85 | 2 rounds |
| `archive old` | Move completed to archive | 3s | 0.85 | 5-6 rounds |
| `my tasks` | Filter by current user | 1s | 0.95 | 2 rounds |
| `this week` | Create week view | 1s | 0.95 | 2 rounds |
| `assign to [person]` | Update person property | 1s | 0.90 | 2 rounds |
| `create dashboard` | Build overview page | 5s | 0.80 | 6-8 rounds |
| `group by status` | Create board view | 2s | 0.90 | 3 rounds |
| `reschedule` | Update date property | 1s | 0.90 | 2 rounds |
| `duplicate` | Copy with structure | 2s | 0.95 | 3-4 rounds |
| `share with team` | Update permissions | 2s | 0.85 | 3-4 rounds |
| `import CSV` | Create from data | 3s | 0.85 | 4-5 rounds |
| `weekly review` | Create review template | 3s | 0.85 | 4-5 rounds |
| `link to [item]` | Create relation | 2s | 0.85 | 3 rounds |
| `calendar view` | Create by date property | 2s | 0.95 | 2-3 rounds |
| `export` | Generate CSV | 2s | 0.95 | 2 rounds |
| `lock database` | Protect structure | 1s | 0.90 | 2 rounds |

---

## 9. 🔗 COMPOSITE PATTERNS

### CRM + Projects
```yaml
trigger: "track clients and projects"
recommended_thinking: 7-9 rounds
creates:
  - Clients database
  - Projects database with client relation
  - Automatic value rollups
  - Client dashboard with project list
thinking_focus: "Relationship optimization"
```

### Tasks + Time
```yaml
trigger: "tasks with time tracking"
recommended_thinking: 5-7 rounds
creates:
  - Tasks with estimated/actual hours
  - Time entries linked to tasks
  - Daily/weekly time reports
  - Billable/non-billable toggle
thinking_focus: "Time calculation accuracy"
```

### Content + Analytics
```yaml
trigger: "content with performance"
recommended_thinking: 6-8 rounds
creates:
  - Content database
  - Analytics tracking
  - Performance dashboard
  - ROI calculations
thinking_focus: "Metric relationships"
```

### Complete Reorganization
```yaml
trigger: "workspace is a mess, help organize"
recommended_thinking: 9-10 rounds
creates:
  - Organized folder structure
  - Proper databases for items
  - Archive for old content
  - Dashboard for overview
  - Clean navigation
thinking_focus: "Preservation and migration"
```

---

## 10. 🎯 PATTERN APPLICATION

### Selection Logic with Thinking Integration
1. Check exact trigger match (>0.95 confidence) → 2-3 rounds
2. Analyze context clues → 3-4 rounds
3. Consider user history → 4-5 rounds
4. Apply smart defaults → 5-6 rounds
5. Ask only if <0.50 confidence → 7-10 rounds

### Intent Detection Flow with Thinking
```
User Input
    ↓
Category Detection (workspace/content/organization/query)
    ↓
Pattern Matching (exact → synonym → category)
    ↓
Confidence Assessment
    ↓
Ask for Thinking Rounds
    ↓
Execution Path Selection
```

### Quality Standards with Thinking Transparency
Every pattern creates:
- Essential properties only
- Helpful default views
- Scalable structure
- Clear naming
- Best practices applied
- **Transparent thinking process**
- **User-controlled optimization depth**

### Performance Guidelines with Thinking Optimization
- Small database: <1,000 items (instant) → 2-3 rounds
- Medium: 1,000-10,000 (use filters) → 4-5 rounds
- Large: 10,000-50,000 (aggressive filtering + archive) → 6-8 rounds
- Very large: >50,000 (split databases) → 9-10 rounds

### Thinking Round Allocation

| Complexity | Rounds | Focus Areas |
|------------|--------|-------------|
| **Simple** | 2-3 | Basic structure, essential properties |
| **Standard** | 4-6 | Views, filters, basic relations |
| **Complex** | 7-8 | Multiple databases, automation |
| **Advanced** | 9-10 | Full systems, optimization, scaling |

---

*This pattern library enables instant understanding and execution of natural language requests with transparent, user-controlled thinking. By mapping triggers to implementations efficiently while letting users control the optimization depth, the assistant provides professional Notion structures tailored to their exact needs.*