# Notion Assistant - Pattern Library v1.0.0

This document provides a comprehensive library of patterns for recognizing user intent and mapping natural language to optimal Notion operations. Each pattern includes triggers, implementation, and variations.

## Table of Contents
1. [🎯 INTENT RECOGNITION PATTERNS](#1--intent-recognition-patterns)
2. [✨ CREATION PATTERNS](#2--creation-patterns)
3. [🔄 UPDATE PATTERNS](#3--update-patterns)
4. [🗂️ ORGANIZATION PATTERNS](#4-️-organization-patterns)
5. [🔍 QUERY PATTERNS](#5--query-patterns)
6. [📦 BULK OPERATION PATTERNS](#6--bulk-operation-patterns)
7. [🏗️ WORKSPACE SETUP PATTERNS](#7-️-workspace-setup-patterns)
8. [🔗 INTEGRATION PATTERNS](#8--integration-patterns)
9. [📊 VIEW PATTERNS](#9--view-patterns)
10. [🧩 COMPOSITE PATTERNS](#10--composite-patterns)

---

## 1. 🎯 INTENT RECOGNITION PATTERNS

### Core Recognition Engine

**Pattern Matching Hierarchy:**
```
1. Exact Match (0.95+ confidence)
   "project tracker" → PROJECT_TRACKING_PATTERN
   
2. Synonym Recognition (0.85+ confidence)
   "todo list" = "task list" = "action items" → TASK_PATTERN
   
3. Category Detection (0.75+ confidence)
   "organize meetings" → SCHEDULING_CATEGORY → MEETING_PATTERN
   
4. Composite Understanding (0.70+ confidence)
   "client work tracker" → CRM_PATTERN + PROJECT_PATTERN
   
5. Contextual Inference (0.60+ confidence)
   "track books" + user_is_student → STUDY_MATERIALS_PATTERN
```

### Confidence Scoring Framework

**High Confidence Triggers (>0.8):**
- Contains exact pattern keywords
- Clear singular intent
- Common use case
- No conflicting indicators

**Medium Confidence Triggers (0.5-0.8):**
- Partial pattern match
- Multiple possible intents
- Requires context
- Some ambiguity

**Low Confidence Triggers (<0.5):**
- Vague language
- No pattern match
- Multiple interpretations
- Needs clarification

### Ambiguity Resolution Patterns

**Multiple Match Resolution:**
```
User: "tracker"
Matches: [task_tracker, habit_tracker, time_tracker, expense_tracker]

Resolution Strategy:
1. Check context for clues
2. Look for modifier words  
3. Consider user history
4. Ask clarifying question if needed
```

**Context Clue Detection:**
- Time-related words → Time tracking
- Money/cost words → Expense tracking
- Daily/routine words → Habit tracking
- Work/project words → Task tracking

---

## 2. ✨ CREATION PATTERNS

### Project Tracker Pattern
**Triggers:**
```
Primary: "project tracker", "project management", "track projects"
Secondary: "manage projects", "project system", "project database"
Contextual: "client work", "team projects", "project pipeline"
```

**Notion Implementation:**
```yaml
database:
  properties:
    - name: "Project Name"
      type: title
    - name: "Status"
      type: select
      options: ["Planning", "In Progress", "Review", "Complete", "On Hold"]
    - name: "Priority"
      type: select
      options: ["High", "Medium", "Low"]
    - name: "Deadline"
      type: date
    - name: "Owner"
      type: person
    - name: "Progress"
      type: number
      format: percent
    - name: "Client"
      type: relation
      database_id: clients_db (if exists)
    - name: "Budget"
      type: number
      format: currency
  views:
    - name: "Active Projects"
      type: table
      filter: status != "Complete"
    - name: "Timeline"
      type: calendar
      calendar_by: "Deadline"
    - name: "By Status"
      type: board
      group_by: "Status"
```

**Variations:**
- Personal projects → Remove Client, Budget
- Team projects → Add Team Members (people)
- Agile projects → Add Sprint (select), Story Points
- Creative projects → Add Inspiration, Assets

### Task Management Pattern
**Triggers:**
```
Primary: "task list", "todo list", "task tracker"
Secondary: "things to do", "action items", "task management"
Contextual: "daily tasks", "work tasks", "personal todos"
```

**Notion Implementation:**
```yaml
database:
  properties:
    - name: "Task"
      type: title
    - name: "Done"
      type: checkbox
    - name: "Due Date"
      type: date
    - name: "Priority"
      type: select
      options: ["🔴 High", "🟡 Medium", "🟢 Low"]
    - name: "Category"
      type: select
      options: ["Work", "Personal", "Home", "Errands"]
    - name: "Assigned To"
      type: person
    - name: "Project"
      type: relation
  views:
    - name: "Today"
      type: table
      filter: due_date = today() OR (due_date < today() AND !done)
    - name: "This Week"
      type: table
      filter: due_date <= end_of_week()
    - name: "By Priority"
      type: board
      group_by: "Priority"
```

### Meeting Notes Pattern
**Triggers:**
```
Primary: "meeting notes", "meeting tracker", "meeting minutes"
Secondary: "track meetings", "meeting log", "meeting records"
Contextual: "team meetings", "client meetings", "1-on-1s"
```

**Notion Implementation:**
```yaml
page_template:
  properties:
    - name: "Meeting Title"
      type: title
    - name: "Date"
      type: date
      default: today()
    - name: "Attendees"
      type: multi_person
    - name: "Type"
      type: select
      options: ["Team", "Client", "1-on-1", "All Hands"]
    - name: "Related Project"
      type: relation
  content_blocks:
    - type: heading_2
      content: "Agenda"
    - type: bulleted_list
      content: placeholder
    - type: heading_2
      content: "Notes"
    - type: text
      content: placeholder
    - type: heading_2
      content: "Action Items"
    - type: todo_list
      content: placeholder
    - type: heading_2
      content: "Next Steps"
```

### Content Calendar Pattern
**Triggers:**
```
Primary: "content calendar", "editorial calendar", "publishing schedule"
Secondary: "blog calendar", "social media calendar", "content plan"
Contextual: "youtube schedule", "post planning", "content pipeline"
```

**Notion Implementation:**
```yaml
database:
  properties:
    - name: "Content Title"
      type: title
    - name: "Status"
      type: select
      options: ["Idea", "Writing", "Review", "Scheduled", "Published"]
    - name: "Publish Date"
      type: date
    - name: "Platform"
      type: multi_select
      options: ["Blog", "YouTube", "Instagram", "Twitter", "LinkedIn"]
    - name: "Content Type"
      type: select
      options: ["Article", "Video", "Infographic", "Podcast"]
    - name: "Author"
      type: person
    - name: "Tags"
      type: multi_select
    - name: "URL"
      type: url
  views:
    - name: "Calendar"
      type: calendar
      calendar_by: "Publish Date"
    - name: "Pipeline"
      type: board
      group_by: "Status"
    - name: "This Month"
      type: table
      filter: publish_date >= start_of_month()
```

### Knowledge Base Pattern
**Triggers:**
```
Primary: "knowledge base", "wiki", "documentation"
Secondary: "notes database", "reference library", "info hub"
Contextual: "team knowledge", "personal wiki", "research database"
```

**Notion Implementation:**
```yaml
database:
  properties:
    - name: "Title"
      type: title
    - name: "Category"
      type: select
      options: ["Process", "Reference", "Tutorial", "Policy"]
    - name: "Tags"
      type: multi_select
    - name: "Last Updated"
      type: last_edited_time
    - name: "Author"
      type: created_by
    - name: "Status"
      type: select
      options: ["Draft", "Review", "Published", "Outdated"]
    - name: "Related Docs"
      type: relation
      self_referencing: true
  views:
    - name: "All Docs"
      type: table
      sort: last_updated desc
    - name: "By Category"
      type: board
      group_by: "Category"
    - name: "Recently Updated"
      type: table
      filter: last_updated > one_week_ago()
```

---

## 3. 🔄 UPDATE PATTERNS

### Status Update Pattern
**Triggers:**
```
Primary: "mark as done", "complete task", "finish item"
Secondary: "update status", "change status", "set to complete"
Contextual: "done with [item]", "completed [item]", "[item] is finished"
```

**Implementation Logic:**
```python
def update_status_pattern(intent):
    # Extract item reference
    item = extract_item_reference(intent)
    
    # Determine new status
    if any(word in intent for word in ["done", "complete", "finish"]):
        new_status = "Complete"
        checkbox_value = True
    elif "in progress" in intent:
        new_status = "In Progress"
    elif "start" in intent:
        new_status = "In Progress"
    
    # Find item and update
    return update_item_property(item, status=new_status)
```

### Date Change Pattern
**Triggers:**
```
Primary: "change date", "update deadline", "reschedule"
Secondary: "move to tomorrow", "push to next week", "due [date]"
Contextual: "postpone", "delay", "extend deadline"
```

**Date Parsing Logic:**
```python
relative_dates = {
    "tomorrow": +1 day,
    "next week": +7 days,
    "next month": +30 days,
    "monday": next_monday()
}

specific_patterns = [
    r"due (\d+/\d+)",
    r"on ([A-Za-z]+day)",
    r"by (.*)"
]
```

### Assignment Pattern
**Triggers:**
```
Primary: "assign to", "give to", "delegate to"
Secondary: "for [person]", "[person]'s task", "owner: [person]"
Contextual: "I'll take this", "reassign", "change owner"
```

**Implementation:**
```yaml
steps:
  1. identify_item:
     - Search by title
     - Use context if ambiguous
  2. identify_person:
     - Match workspace members
     - Handle "me" as current user
  3. update_property:
     - Set person property
     - Notify if enabled
```

### Property Addition Pattern
**Triggers:**
```
Primary: "add note", "add comment", "add description"
Secondary: "include [info]", "also [detail]", "with [property]"
Contextual: "forgot to mention", "also needs", "update with"
```

**Property Append Logic:**
- Text properties: Append with newline
- Multi-select: Add to existing
- Relations: Add connection
- Number: Mathematical operation

---

## 4. 🗂️ ORGANIZATION PATTERNS

### Archive Pattern
**Triggers:**
```
Primary: "archive old", "archive completed", "clean up"
Secondary: "move old items", "hide finished", "organize done"
Contextual: "archive last month", "clean 2023", "archive project X"
```

**Implementation:**
```yaml
archive_strategy:
  identify_items:
    - status = "Complete" OR
    - date < threshold OR
    - specific_criteria
  create_archive:
    - location: /Archive/[Year]/
    - maintain_structure: true
    - preserve_relations: true
  move_items:
    - batch_size: 50
    - verify_each: true
  update_views:
    - exclude_archived: true
```

### Grouping Pattern
**Triggers:**
```
Primary: "group by", "organize by", "categorize by"
Secondary: "sort into", "arrange by", "split by"
Contextual: "see by project", "show by person", "view by status"
```

**Grouping Implementation:**
```yaml
view_creation:
  - type: board
    group_by: [detected_property]
    sort_within_groups: 
      - priority: desc
      - date: asc
  - collapse_empty: true
    show_count: true
```

### Hierarchy Creation Pattern
**Triggers:**
```
Primary: "create structure", "organize hierarchy", "nested organization"
Secondary: "parent-child", "main and sub", "folders and files"
Contextual: "department > team > project", "area/project/task"
```

**Structure Types:**
```
1. Page Hierarchy:
   Area/
   ├── Project A/
   │   ├── Task Database
   │   └── Resources
   └── Project B/

2. Database Relations:
   - Parent Project (relation)
   - Sub-items (relation)
   - Hierarchy Level (number)

3. Mixed Approach:
   - Top level pages
   - Databases within
   - Relations across
```

### Dashboard Pattern
**Triggers:**
```
Primary: "create dashboard", "overview page", "control center"
Secondary: "home page", "summary view", "quick access"
Contextual: "see everything", "bird's eye view", "mission control"
```

**Dashboard Components:**
```yaml
dashboard_blocks:
  - type: heading
    content: "📊 [Area] Dashboard"
  - type: linked_database
    config:
      source: tasks_db
      view: "This Week"
      show_title: true
  - type: linked_database
    config:
      source: projects_db
      view: "Active"
  - type: callout
    content: "Quick Stats"
    children:
      - "Open Tasks: {count}"
      - "Due Today: {count}"
  - type: toggle_list
    content: "Resources"
```

---

## 5. 🔍 QUERY PATTERNS

### Date-Based Query Pattern
**Triggers:**
```
Primary: "show today", "this week", "overdue"
Secondary: "due soon", "upcoming", "past due"
Contextual: "what's due", "deadline approaching", "next 7 days"
```

**Filter Implementations:**
```yaml
today:
  filter: date = today()
  
this_week:
  filter: date >= start_of_week() AND date <= end_of_week()
  
overdue:
  filter: date < today() AND status != "Complete"
  
upcoming:
  filter: date >= today() AND date <= days_from_now(7)
  
this_month:
  filter: date >= start_of_month() AND date <= end_of_month()
```

### Person-Based Query Pattern
**Triggers:**
```
Primary: "my items", "assigned to me", "[person]'s tasks"
Secondary: "for [person]", "owned by", "responsible: [person]"
Contextual: "what do I own", "team member's work", "unassigned"
```

**Person Filters:**
```yaml
my_items:
  filter: assigned_to = current_user()
  
specific_person:
  filter: assigned_to = resolve_person(name)
  
unassigned:
  filter: assigned_to is empty
  
team_items:
  filter: assigned_to in team_members()
```

### Status-Based Query Pattern
**Triggers:**
```
Primary: "in progress", "completed items", "active projects"
Secondary: "not started", "on hold", "needs review"
Contextual: "what's active", "finished work", "pending items"
```

**Status Configurations:**
```yaml
active_items:
  filter: status in ["In Progress", "Active", "Started"]
  
completed:
  filter: status in ["Complete", "Done", "Finished"]
  
needs_attention:
  filter: status in ["Blocked", "At Risk", "Overdue"]
  
not_started:
  filter: status in ["Not Started", "Planned", "Backlog"]
```

### Multi-Criteria Query Pattern
**Triggers:**
```
Primary: "high priority this week", "my overdue tasks", "urgent from John"
Secondary: "important and urgent", "completed last month", "team's active"
```

**Complex Filter Logic:**
```yaml
high_priority_this_week:
  filters:
    - priority = "High"
    - AND date >= start_of_week()
    - AND date <= end_of_week()
    
my_overdue_urgent:
  filters:
    - assigned_to = current_user()
    - AND date < today()
    - AND priority = "High"
    - AND status != "Complete"
```

---

## 6. 📦 BULK OPERATION PATTERNS

### Bulk Status Update Pattern
**Triggers:**
```
Primary: "mark all done", "complete all", "archive all finished"
Secondary: "update all statuses", "bulk complete", "finish everything"
Contextual: "all of these are done", "complete this project's tasks"
```

**Implementation:**
```yaml
bulk_update_flow:
  1. identify_scope:
     - all_in_view
     - matching_filter
     - specific_selection
  2. confirm_count:
     - "This will update X items"
  3. execute_batch:
     - batch_size: 50
     - show_progress: true
  4. verify_completion:
     - success_count
     - failure_handling
```

### Bulk Creation Pattern
**Triggers:**
```
Primary: "create multiple", "add list", "bulk add"
Secondary: "create 10 tasks", "add these items", "import list"
Contextual: "create weekly tasks", "monthly pages", "team assignments"
```

**Parsing Strategies:**
```python
# List detection
- Line-by-line parsing
- Comma-separated values
- Numbered lists
- Bullet points

# Pattern repetition
- Daily for week
- Weekly for month
- Template × count

# Import from text
- Parse structure
- Detect properties
- Map to fields
```

### Bulk Move Pattern
**Triggers:**
```
Primary: "move all to", "relocate items", "transfer everything"
Secondary: "change location", "bulk move", "migrate to"
Contextual: "put these in archive", "move to new database"
```

**Move Operations:**
```yaml
move_strategies:
  within_database:
    - Update property values
    - Change parent relations
    - Maintain connections
  
  between_databases:
    - Check schema compatibility
    - Map properties
    - Create in destination
    - Verify and delete source
    
  to_archive:
    - Create archive structure
    - Preserve all data
    - Update references
```

### Bulk Delete Pattern
**Triggers:**
```
Primary: "delete all completed", "remove old", "clear out"
Secondary: "bulk delete", "clean up", "purge items"
Contextual: "delete last year's", "remove archived", "clear test data"
```

**Safety Measures:**
```yaml
deletion_flow:
  1. scope_confirmation:
     - Show exact items
     - Count display
     - "This will delete X items"
  2. backup_option:
     - "Export before delete?"
     - Quick CSV export
  3. final_confirmation:
     - "Type 'DELETE' to confirm"
  4. soft_delete:
     - Move to trash first
     - 30-day recovery
```

---

## 7. 🏗️ WORKSPACE SETUP PATTERNS

### Complete System Pattern
**Triggers:**
```
Primary: "set up workspace", "create full system", "complete setup"
Secondary: "business system", "productivity setup", "organize everything"
Contextual: "GTD system", "PARA method", "company workspace"
```

**System Templates:**

**Business Management:**
```yaml
components:
  - CRM database
  - Projects tracker
  - Tasks system
  - Time tracking
  - Invoice management
  - Dashboard hub
  
connections:
  - Clients → Projects
  - Projects → Tasks
  - Tasks → Time entries
  - Time → Invoices
```

**Personal Productivity:**
```yaml
components:
  - Goals & OKRs
  - Projects database
  - Task manager
  - Habit tracker
  - Note system
  - Weekly reviews
  
structure:
  - Life areas as top pages
  - Databases within areas
  - Central dashboard
```

### Team Workspace Pattern
**Triggers:**
```
Primary: "team workspace", "shared system", "collaborative setup"
Secondary: "department hub", "team wiki", "project space"
```

**Team Components:**
```yaml
standard_team_setup:
  - Team wiki/docs
  - Project tracker
  - Task assignments
  - Meeting notes
  - Team calendar
  - Resource library
  
permissions:
  - Admin: Full access
  - Members: Edit content
  - Guests: View only
```

### Migration Pattern
**Triggers:**
```
Primary: "import from", "migrate data", "move from [tool]"
Secondary: "transfer from Excel", "copy from Trello", "switch from Asana"
```

**Migration Mappings:**
```yaml
excel_to_notion:
  - Rows → Database items
  - Columns → Properties
  - Sheets → Separate databases
  - Formulas → Formula properties

trello_to_notion:
  - Boards → Databases
  - Lists → Status property
  - Cards → Database items
  - Labels → Tags/Multi-select
```

---

## 8. 🔗 INTEGRATION PATTERNS

### Cross-Database Linking Pattern
**Triggers:**
```
Primary: "connect databases", "link between", "create relations"
Secondary: "reference from", "connect to", "associate with"
Contextual: "projects with tasks", "contacts to companies"
```

**Relation Types:**
```yaml
one_to_many:
  example: "One project has many tasks"
  implementation:
    - Parent: Project
    - Children: Tasks
    - Rollup: Task count, completion %

many_to_many:
  example: "Tasks have multiple tags"
  implementation:
    - Items: Tasks
    - Categories: Tags
    - Junction: Optional

hierarchical:
  example: "Company > Department > Team"
  implementation:
    - Self-referencing relations
    - Level tracking
    - Breadcrumb generation
```

### Sync Pattern
**Triggers:**
```
Primary: "keep in sync", "mirror data", "auto-update"
Secondary: "sync with", "reflect changes", "connected data"
```

**Sync Strategies:**
```yaml
property_sync:
  - Relation + Rollup
  - Formula references
  - Filter inheritance

view_sync:
  - Linked databases
  - Shared filters
  - Consistent sorting

template_sync:
  - Recurring items
  - Consistent structure
  - Property inheritance
```

### Automation Pattern
**Triggers:**
```
Primary: "automate", "auto-create", "trigger when"
Secondary: "recurring tasks", "automatic status", "scheduled creation"
```

**Automation Types:**
```yaml
recurring_creation:
  - Daily standup notes
  - Weekly reports
  - Monthly reviews
  
status_progression:
  - Date-based status changes
  - Completion cascades
  - Dependency tracking

template_application:
  - New item defaults
  - Property calculations
  - Relation auto-fill
```

---

## 9. 📊 VIEW PATTERNS

### Calendar View Pattern
**Triggers:**
```
Primary: "calendar view", "see schedule", "timeline view"
Secondary: "by date", "monthly view", "show calendar"
Contextual: "when things are due", "schedule layout"
```

**Calendar Configurations:**
```yaml
calendar_setup:
  calendar_by: [date_property]
  show_properties:
    - Title
    - Time
    - Status indicator
  color_by: priority or status
  default_view: month
```

### Kanban Board Pattern
**Triggers:**
```
Primary: "kanban board", "board view", "pipeline view"
Secondary: "by status", "workflow view", "drag and drop"
Contextual: "see stages", "move between states"
```

**Board Setup:**
```yaml
kanban_config:
  group_by: status
  show_properties:
    - Owner avatar
    - Due date
    - Priority badge
  hide_empty_groups: false
  card_preview: cover + description
```

### Gallery View Pattern
**Triggers:**
```
Primary: "gallery view", "card view", "visual layout"
Secondary: "with images", "preview cards", "pinterest style"
Contextual: "see thumbnails", "visual browser"
```

**Gallery Options:**
```yaml
gallery_setup:
  card_preview: page_cover
  properties_shown: 3
  card_size: medium
  fit_image: cover
  open_as: side_peek
```

### List View Pattern
**Triggers:**
```
Primary: "list view", "simple list", "minimal view"
Secondary: "just titles", "clean view", "reading list"
Contextual: "simple layout", "mobile friendly"
```

**List Configuration:**
```yaml
list_setup:
  show_properties: minimal
  properties:
    - Title (always)
    - Status badge
    - Due date (if exists)
  group_by: optional
  compact: true
```

---

## 10. 🧩 COMPOSITE PATTERNS

### CRM + Project Pattern
**Triggers:**
```
"track clients and their projects"
"customer project management"
"client work system"
```

**Implementation:**
```yaml
system_components:
  clients_db:
    - Company info
    - Contact details
    - Industry/Type
    - Total value (rollup)
    
  projects_db:
    - Client relation
    - Project phases
    - Budget/Hours
    - Team members
    
  connections:
    - One client → Many projects
    - Projects sum to client value
    - Shared team directory
```

### Content + Analytics Pattern
**Triggers:**
```
"content with performance"
"track content metrics"
"publishing and analytics"
```

**Implementation:**
```yaml
content_system:
  content_db:
    - Title and type
    - Publish date
    - Platform tags
    - Content status
    
  analytics_db:
    - Content relation
    - View counts
    - Engagement rates
    - Revenue data
    
  dashboard:
    - Top performers
    - Publishing calendar
    - Performance trends
```

### Task + Time Pattern
**Triggers:**
```
"tasks with time tracking"
"billable hours system"
"work time management"
```

**Implementation:**
```yaml
integrated_system:
  tasks:
    - Standard task fields
    - Estimated hours
    - Actual hours (rollup)
    
  time_entries:
    - Task relation
    - Start/End times
    - Duration calc
    - Billable toggle
    
  reporting:
    - Hours by project
    - Billable summary
    - Productivity metrics
```

### Knowledge + Learning Pattern
**Triggers:**
```
"learning management"
"study system"
"knowledge and progress"
```

**Implementation:**
```yaml
learning_system:
  resources_db:
    - Title and type
    - Category/Subject
    - Difficulty level
    - Source URL
    
  progress_db:
    - Resource relation
    - Status/Completion
    - Notes/Highlights
    - Review dates
    
  study_tools:
    - Spaced repetition
    - Progress tracking
    - Study calendar
```

---

## 🎯 Pattern Application Guidelines

### Selection Logic
1. **Exact Match First**: Check primary triggers
2. **Context Analysis**: Look for modifying words
3. **User History**: Consider previous patterns
4. **Smart Defaults**: Apply when confidence high
5. **Ask When Unsure**: Single clarifying question

### Confidence Thresholds
- **>0.9**: Execute immediately with pattern
- **0.7-0.9**: Confirm understanding first
- **0.5-0.7**: Show options to user
- **<0.5**: Use interactive mode

### Pattern Combination Rules
- Compatible patterns can merge
- Conflicting patterns need resolution
- User intent overrides defaults
- Maintain simplicity when possible

### Quality Assurance
Every pattern implementation must:
- Include helpful views
- Apply best practices
- Scale appropriately
- Provide clear value
- Enable easy modification

---

*This pattern library enables the Notion Assistant to understand natural language and create optimal Notion structures. Patterns are continuously refined based on usage and user feedback.*