# Notion Assistant - Quick Operation Reference v0.100

This document provides a rapid lookup reference mapping common user requests to their Notion implementations. Each operation includes trigger phrases, implementation details, and success indicators.

## Table of Contents
1. [✨ CREATION QUICK OPS](#1--creation-quick-ops)
2. [🔄 UPDATE QUICK OPS](#2--update-quick-ops)
3. [🗂️ ORGANIZATION QUICK OPS](#3-️-organization-quick-ops)
4. [🔍 SEARCH QUICK OPS](#4--search-quick-ops)
5. [📦 BULK QUICK OPS](#5--bulk-quick-ops)
6. [📊 VIEW QUICK OPS](#6--view-quick-ops)
7. [🔗 RELATION QUICK OPS](#7--relation-quick-ops)
8. [📅 TIME-BASED QUICK OPS](#8--time-based-quick-ops)
9. [👥 COLLABORATION QUICK OPS](#9--collaboration-quick-ops)
10. [⚙️ SYSTEM QUICK OPS](#10-️-system-quick-ops)

---

## 1. ✨ CREATION QUICK OPS

### "new project"
**Trigger Variations:**
- "create project"
- "add project [name]"
- "start new project"
- "project for [client]"

**Notion Sequence:**
```yaml
1. create_database_item:
   database: Projects (find or create)
   properties:
     - Name: [Extracted name or "New Project"]
     - Status: "Planning"
     - Created: Today
     - Owner: Current user
     
2. apply_template:
   if exists: Project template
   
3. success_response:
   "Created '[Project Name]' in your projects!"
```

**Required Context:**
- Project name (optional, can default)
- Client/category (optional)

**Success Indicator:**
```
✅ Project created: "[Name]"
📍 Location: /Projects/
🎯 Next: "Add tasks to [project]"
```

### "meeting tomorrow"
**Trigger Variations:**
- "schedule meeting"
- "meeting at 2pm"
- "team meeting Tuesday"
- "client call next week"

**Notion Sequence:**
```yaml
1. determine_type:
   - If calendar exists: Create calendar event
   - Else: Create meeting note
   
2. create_page:
   title: "Meeting - [Date]"
   properties:
     - Date: [Parsed date/time]
     - Type: [Meeting type]
     - Attendees: []
     
3. add_template:
   - Agenda section
   - Notes section
   - Action items
```

**Success Indicator:**
```
📅 Meeting scheduled: Tomorrow at [time]
📝 Note template ready
💡 Tip: Add agenda items before the meeting
```

### "task list"
**Trigger Variations:**
- "create todo list"
- "new task tracker"
- "to-do list"
- "action items"

**Notion Sequence:**
```yaml
1. create_database:
   name: "Tasks"
   icon: "✓"
   properties:
     - Task: title
     - Done: checkbox
     - Due: date
     - Priority: select ["High", "Medium", "Low"]
     
2. create_views:
   - Today (filtered)
   - All Tasks (table)
   - By Priority (board)
```

**Success Indicator:**
```
✅ Task system ready!
📋 0 tasks (ready to add)
🎯 Try: "Add task 'Email client'"
```

### "team page"
**Trigger Variations:**
- "create team space"
- "department page"
- "team hub"
- "project team page"

**Notion Sequence:**
```yaml
1. create_page:
   title: "[Team] Team"
   icon: "👥"
   
2. add_sections:
   - Team Members (people list)
   - Quick Links (bookmarks)
   - Team Resources (database)
   - Recent Updates (linked view)
   
3. set_permissions:
   team_members: edit
   others: view
```

---

## 2. 🔄 UPDATE QUICK OPS

### "mark done"
**Trigger Variations:**
- "complete task"
- "finish [item]"
- "check off"
- "[item] is done"
- "completed"

**Notion Sequence:**
```yaml
1. identify_item:
   search: title contains keywords
   context: recent items first
   
2. update_properties:
   if checkbox exists: Set true
   if status exists: Set "Complete"
   
3. confirmation:
   "✅ Marked '[item]' as complete!"
```

**Ambiguity Handling:**
```yaml
multiple_matches:
  show_options: "Which one?"
  - Task: "Send report" (due today)
  - Task: "Send report" (due next week)
  - Project: "Report redesign"
```

### "change date"
**Trigger Variations:**
- "move to tomorrow"
- "reschedule to Monday"
- "due next week"
- "postpone 3 days"
- "deadline is [date]"

**Notion Sequence:**
```yaml
1. parse_date:
   relative: tomorrow, next week, +3 days
   specific: Monday, Dec 15, 12/15
   
2. find_date_property:
   priority: Due Date > Deadline > Date
   
3. update_value:
   old: [current]
   new: [parsed date]
```

**Date Parsing Examples:**
```
"tomorrow" → +1 day from today
"next Monday" → upcoming Monday
"in 2 weeks" → +14 days
"end of month" → last day of current month
"Dec 15" → December 15, current year
```

### "add note"
**Trigger Variations:**
- "add comment"
- "include note: [text]"
- "add description"
- "note that [information]"

**Notion Sequence:**
```yaml
1. determine_location:
   - Comments section
   - Notes property
   - Description field
   - Page content
   
2. append_content:
   format: Add with timestamp
   preserve: Existing content
```

### "assign to"
**Trigger Variations:**
- "give to [person]"
- "delegate to [name]"
- "[person]'s task now"
- "reassign to [team member]"
- "I'll take this"

**Notion Sequence:**
```yaml
1. resolve_person:
   "me" → current user
   "John" → search workspace members
   "[email]" → exact match
   
2. update_person_property:
   clear: previous assignee
   set: new assignee
   notify: if enabled
```

---

## 3. 🗂️ ORGANIZATION QUICK OPS

### "archive old"
**Trigger Variations:**
- "archive completed"
- "clean up old items"
- "move finished to archive"
- "archive 2024"
- "hide completed tasks"

**Notion Sequence:**
```yaml
1. identify_items:
   criteria:
     - Status = "Complete" AND
     - Modified > 30 days ago
     OR specific: Year = 2024
     
2. create_archive:
   location: /Archive/[Year]/[Type]/
   
3. batch_move:
   items: [selected]
   preserve: relations, properties
   
4. update_views:
   filter: exclude archived
```

**User Confirmation:**
```
📦 Ready to archive 47 items:
• Completed over 30 days ago
• Will move to /Archive/2025/

[Archive Now] [Review Items] [Cancel]
```

### "group by status"
**Trigger Variations:**
- "organize by status"
- "show by category"
- "sort by priority"
- "view by project"

**Notion Sequence:**
```yaml
1. create_view:
   type: Board (for grouping)
   name: "By [Property]"
   
2. configure_grouping:
   group_by: [detected property]
   sort_in_groups: date ascending
   
3. visual_settings:
   color_by: group
   hide_empty: false
```

### "create dashboard"
**Trigger Variations:**
- "overview page"
- "home dashboard"
- "control center"
- "summary view"

**Notion Sequence:**
```yaml
1. create_page:
   title: "Dashboard"
   icon: "📊"
   
2. add_widgets:
   - Active tasks (filtered view)
   - Recent projects (linked db)
   - Quick stats (callout)
   - Important links (bookmarks)
   
3. layout:
   columns: 2-3 for desktop
   responsive: mobile-friendly
```

---

## 4. 🔍 SEARCH QUICK OPS

### "find project X"
**Trigger Variations:**
- "where is [project]"
- "search for [name]"
- "locate [item]"
- "show me [title]"

**Notion Sequence:**
```yaml
1. search_strategy:
   - Exact title match
   - Contains keywords
   - Similar names
   - Recent items
   
2. search_scope:
   - Current database
   - Related databases
   - Full workspace
   
3. present_results:
   confidence: high/medium/low
   show: top 5 matches
```

### "overdue tasks"
**Trigger Variations:**
- "what's overdue"
- "past due items"
- "missed deadlines"
- "late tasks"

**Notion Sequence:**
```yaml
1. create_filter:
   due_date: < today()
   AND status: != "Complete"
   
2. create_view:
   name: "Overdue"
   sort: due_date ascending
   
3. visual_indicator:
   highlight: red
   emoji: "⚠️"
```

### "recent updates"
**Trigger Variations:**
- "what changed"
- "latest edits"
- "recent activity"
- "updated this week"

**Notion Sequence:**
```yaml
1. create_view:
   sort: last_edited descending
   
2. add_filter:
   last_edited: >= past_week()
   
3. show_editor:
   property: last_edited_by
```

### "unassigned"
**Trigger Variations:**
- "no owner tasks"
- "needs assignment"
- "unassigned items"
- "nobody assigned"

**Notion Sequence:**
```yaml
1. filter_creation:
   assigned_to: is_empty()
   
2. view_setup:
   highlight: these items
   suggest: bulk assign
```

---

## 5. 📦 BULK QUICK OPS

### "update all"
**Trigger Variations:**
- "change all status"
- "mark all complete"
- "update everything"
- "bulk edit"

**Notion Sequence:**
```yaml
1. scope_confirmation:
   count: "This affects 23 items"
   show: preview of changes
   
2. batch_update:
   chunks: 50 items
   progress: visual indicator
   
3. rollback_option:
   save: previous state
   offer: undo if needed
```

### "archive completed"
**Trigger Variations:**
- "bulk archive"
- "move all done"
- "clean up finished"
- "archive everything complete"

**Notion Sequence:**
```yaml
1. identify_targets:
   filter: status = "Complete"
   count: show total
   
2. create_archive_structure:
   path: /Archive/[Year]/[Month]/
   
3. execute_move:
   batch_size: 100
   preserve: all properties
```

### "create weekly"
**Trigger Variations:**
- "weekly tasks"
- "recurring items"
- "create for each day"
- "weekly meetings"

**Notion Sequence:**
```yaml
1. determine_pattern:
   frequency: weekly
   count: how many weeks
   
2. create_items:
   template: if exists
   naming: "[Item] - Week of [Date]"
   
3. set_dates:
   increment: by frequency
   start: from today or specified
```

### "import list"
**Trigger Variations:**
- "add these items"
- "bulk create"
- "paste list"
- "import from text"

**Notion Sequence:**
```yaml
1. parse_input:
   detect_format:
     - Line breaks
     - Commas
     - Numbered list
     - Bullets
     
2. extract_properties:
   smart_detection:
     - Dates in text
     - @mentions
     - #tags
     - Priorities
     
3. create_items:
   show_preview: before creating
   map_properties: intelligently
```

**Parsing Examples:**
```
Input: "Task 1 due tomorrow high priority"
Parses to:
  - Title: "Task 1"
  - Due: Tomorrow's date
  - Priority: "High"

Input: "Meeting with @John next Monday 2pm"
Parses to:
  - Title: "Meeting with John"
  - Date: Next Monday 2:00 PM
  - Attendees: John
```

---

## 6. 📊 VIEW QUICK OPS

### "calendar view"
**Trigger Variations:**
- "show calendar"
- "timeline view"
- "monthly view"
- "schedule view"

**Notion Sequence:**
```yaml
1. identify_date_property:
   priority: Due > Date > Created
   
2. create_calendar_view:
   name: "Calendar"
   calendar_by: [date property]
   
3. settings:
   default: month view
   show: title + time
```

### "kanban board"
**Trigger Variations:**
- "board view"
- "cards view"
- "pipeline view"
- "workflow board"

**Notion Sequence:**
```yaml
1. identify_grouping_property:
   prefer: Status > Priority > Category
   
2. create_board_view:
   group_by: [property]
   cards: show 2-3 properties
   
3. enable:
   drag_drop: between groups
```

### "my view"
**Trigger Variations:**
- "just my items"
- "personal view"
- "assigned to me"
- "my tasks only"

**Notion Sequence:**
```yaml
1. create_filtered_view:
   name: "My [Items]"
   filter: assigned_to = current_user()
   
2. additional_filters:
   - Active items only
   - Not completed
   
3. personalization:
   set_as: default for user
```

---

## 7. 🔗 RELATION QUICK OPS

### "link to project"
**Trigger Variations:**
- "connect to [project]"
- "relate to [item]"
- "associate with"
- "add relationship"

**Notion Sequence:**
```yaml
1. find_databases:
   source: current item's database
   target: mentioned database
   
2. create_relation:
   type: based on context
   bidirectional: usually yes
   
3. link_items:
   source: current
   target: found item
```

### "show related"
**Trigger Variations:**
- "connected items"
- "linked tasks"
- "related projects"
- "associated with"

**Notion Sequence:**
```yaml
1. identify_relations:
   on_current: database
   
2. create_view:
   include: relation columns
   expand: inline preview
   
3. or_filter:
   by: specific relation
```

---

## 8. 📅 TIME-BASED QUICK OPS

### "today's tasks"
**Trigger Variations:**
- "due today"
- "today's agenda"
- "what's on today"
- "daily tasks"

**Notion Sequence:**
```yaml
1. create_today_filter:
   due_date = today()
   OR overdue: < today() AND !complete
   
2. view_settings:
   sort: priority desc, time asc
   name: "Today"
```

### "this week"
**Trigger Variations:**
- "weekly view"
- "this week's work"
- "next 7 days"
- "week ahead"

**Notion Sequence:**
```yaml
1. date_range_filter:
   start: beginning_of_week()
   end: end_of_week()
   
2. grouping:
   by: day_of_week
   
3. include:
   overdue: from before this week
```

### "monthly report"
**Trigger Variations:**
- "last month"
- "monthly summary"
- "month view"
- "30 day review"

**Notion Sequence:**
```yaml
1. determine_month:
   "last month": -1 month
   "this month": current
   specific: parse month
   
2. create_filtered_view:
   date >= month_start
   date <= month_end
   
3. summary_stats:
   - Count by status
   - Completion rate
   - Key metrics
```

---

## 9. 👥 COLLABORATION QUICK OPS

### "share with team"
**Trigger Variations:**
- "give team access"
- "collaborate on this"
- "let others edit"
- "team permissions"

**Notion Sequence:**
```yaml
1. identify_scope:
   - Current page
   - Database
   - Parent space
   
2. set_permissions:
   team: can_edit
   structure: locked
   
3. notify:
   if requested: send invite
```

### "assign to John"
**Trigger Variations:**
- "@john this task"
- "for sarah"
- "delegate to mike"
- "owner: lisa"

**Notion Sequence:**
```yaml
1. resolve_person:
   match: workspace members
   fuzzy: handle variations
   
2. update_assignment:
   clear: previous
   set: new person
   
3. notification:
   if enabled: notify assignee
```

### "comment on"
**Trigger Variations:**
- "add feedback"
- "note about this"
- "comment: [text]"
- "discussion on"

**Notion Sequence:**
```yaml
1. add_comment:
   location: item comments
   format: with timestamp
   
2. mention:
   if @person: notify them
   
3. thread:
   maintain: conversation context
```

---

## 10. ⚙️ SYSTEM QUICK OPS

### "duplicate this"
**Trigger Variations:**
- "copy [item]"
- "clone database"
- "make another"
- "duplicate with data"

**Notion Sequence:**
```yaml
1. determine_scope:
   - Item only
   - Structure only
   - With all data
   
2. execute_duplication:
   name: "[Original] Copy"
   location: same parent
   
3. handle_relations:
   update: if needed
   maintain: internal links
```

### "export data"
**Trigger Variations:**
- "download csv"
- "export to excel"
- "backup data"
- "get spreadsheet"

**Notion Sequence:**
```yaml
1. prepare_export:
   format: CSV (default)
   scope: current view
   
2. include_options:
   - All properties
   - Visible only
   - Include files
   
3. generate:
   filename: "[Database]-[Date].csv"
```

### "lock database"
**Trigger Variations:**
- "prevent changes"
- "protect structure"
- "lock schema"
- "read only"

**Notion Sequence:**
```yaml
1. lock_settings:
   structure: locked
   content: editable
   
2. or_full_lock:
   structure: locked
   content: read-only
   
3. admin_override:
   maintain: for admins
```

### "create template"
**Trigger Variations:**
- "save as template"
- "reusable format"
- "template from this"
- "standard format"

**Notion Sequence:**
```yaml
1. capture_structure:
   properties: included
   content: as placeholder
   
2. save_template:
   name: descriptive
   location: database templates
   
3. make_available:
   button: "New from template"
```

---

## 🎯 Quick Reference Usage

### Confidence Matching
```yaml
exact_match: 0.95+ confidence
partial_match: 0.70-0.94 confidence  
fuzzy_match: 0.50-0.69 confidence
no_match: <0.50 use interactive mode
```

### Context Requirements
```yaml
always_needed:
  - Operation target (what)
  - Basic intent (action)
  
sometimes_needed:
  - Location (where)
  - Specific values
  - Time context
  
rarely_needed:
  - Technical details
  - Complex options
```

### Success Verification
Every operation should:
1. Confirm what was done
2. Show where it is
3. Suggest next action
4. Teach when relevant

---

*This quick reference enables rapid understanding and execution of common Notion operations. By mapping natural language to specific implementations, the assistant can respond instantly to frequent requests while maintaining quality and best practices.*