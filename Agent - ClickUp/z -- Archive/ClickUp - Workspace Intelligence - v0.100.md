# ClickUp - Workspace Intelligence - v0.100

Best practices, decision frameworks, and error recovery for optimal ClickUp workspace design.

## 1. 📊 DECISION FRAMEWORKS

### List vs Space Decision Matrix

| Use LIST When | Use SPACE When |
|---------------|----------------|
| Related tasks/items | Different departments/teams |
| Same workflow applies | Different workflows needed |
| Under 5,000 items | Multiple lists needed |
| Single view sufficient | Separate permissions required |
| One team manages | Multiple teams involved |
| Shared custom fields | Different field requirements |

**Quick Rule:** If you'll have more than 3 distinct workflows, use separate spaces.

### Custom Field Selection

| Field Type | Use When | Example |
|------------|----------|---------|
| **Dropdown** | Finite options, single choice | Status, Priority, Category |
| **Labels** | Multiple tags needed | Skills, Features, Tags |
| **Users** | Assignment/responsibility | Owner, Reviewer, Assignee |
| **Date** | Time-specific tracking | Due date, Start date |
| **Number** | Calculations needed | Hours, Points, Budget |
| **Text** | Short unique content | ID, Reference, Note |
| **Text Area** | Detailed information | Description, Steps |
| **Checkbox** | Binary state | Complete, Approved, Billable |
| **Money** | Financial tracking | Budget, Cost, Revenue |
| **Progress** | Percentage tracking | Completion, Progress |
| **Rating** | Quality measurement | Priority, Satisfaction |
| **Phone/Email** | Contact info | Client contact |
| **Location** | Geographic data | Office, Site, Region |
| **Relationship** | Connect items | Depends on, Blocks, Related |

### View Optimization Matrix

| View Type | Best For | When to Use | Avoid When |
|-----------|----------|-------------|------------|
| **List** | Quick scanning | Default view, mobile | Visual workflow needed |
| **Board** | Workflow stages | Status management | Many columns (>7) |
| **Calendar** | Date-driven work | Scheduling, deadlines | No dates available |
| **Gantt** | Project timeline | Dependencies exist | Simple task lists |
| **Table** | Data analysis | Bulk editing | Mobile primary |
| **Timeline** | High-level planning | Roadmaps | Detailed tasks |
| **Workload** | Capacity planning | Team management | Solo work |
| **Activity** | Recent changes | Collaboration | Static content |
| **Map** | Location-based | Field work | No location data |
| **Mind Map** | Brainstorming | Ideation phase | Execution phase |

---

## 2. 🏗️ WORKSPACE ARCHITECTURE

### Hierarchy Best Practices

**✅ Optimal Structure:**
```
Workspace
├── Spaces (departments/teams)
│   ├── Folders (categories)
│   │   ├── Lists (work streams)
│   │   │   └── Tasks (items)
```

**⚠️ Warning Signs:**
- More than 5 hierarchy levels
- Over 20 lists in one space
- Duplicate list names
- Inconsistent naming

### Organization Methods

**Team-Based Structure**
```
🏢 Company
├── 💻 Engineering
│   ├── Sprints
│   ├── Bugs
│   └── Features
├── 📣 Marketing
│   ├── Campaigns
│   ├── Content
│   └── Analytics
└── 💰 Sales
    ├── Pipeline
    ├── Activities
    └── Accounts
```

**Project-Based Structure**
```
📁 Projects
├── 🚀 Project Alpha
│   ├── Planning
│   ├── Execution
│   └── Review
├── 🎯 Project Beta
│   ├── Planning
│   ├── Execution
│   └── Review
```

**Client-Based Structure**
```
👥 Clients
├── 🏢 Client A
│   ├── Projects
│   ├── Tasks
│   └── Communication
├── 🏢 Client B
│   ├── Projects
│   ├── Tasks
│   └── Communication
```

### Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| **Spaces** | [Emoji] [Department/Team] | 💻 Engineering |
| **Folders** | [Category] - [Descriptor] | Projects - Active |
| **Lists** | [Type] : [Specific] | Sprint : 23 |
| **Tasks** | [Action] [Object] | Review Homepage Design |
| **Templates** | [TEMPLATE] [Name] | TEMPLATE Sprint Planning |
| **Archives** | [ARCHIVE] [Year] [Type] | ARCHIVE 2024 Completed |

---

## 3. ⚡ PERFORMANCE OPTIMIZATION

### List Size Guidelines

| Size | Tasks | Performance | Strategy |
|------|-------|-------------|----------|
| **Small** | <1,000 | Instant | All features available |
| **Medium** | 1,000-5,000 | Good | Use filtered views |
| **Large** | 5,000-25,000 | Slower | Folders + aggressive filtering |
| **Very Large** | >25,000 | Poor | Split into multiple lists/spaces |

### Performance Best Practices

**Fast Patterns:**
- Limit visible custom fields (5-7)
- Simple filters (AND logic preferred)
- Archive completed items regularly
- Use list view for large datasets
- Minimize dependencies
- Limit automation complexity

**Slow Patterns to Avoid:**
- Showing all custom fields
- Complex nested filters (multiple ORs)
- Too many relationships
- Unfiltered views on large lists
- Heavy automation chains
- Multiple formula fields

### Archive Strategy

| Archive Trigger | Timing | Destination |
|-----------------|--------|-------------|
| **Status-based** | Complete + 30 days | /Space/Archive/[Year]/ |
| **Sprint-based** | Sprint end + 14 days | /Sprints/Archive/[Sprint#]/ |
| **Quarter-based** | Quarterly | /Archive/[Year]/Q[#]/ |
| **Size-based** | >5,000 items | /Archive/[List]/ |

**Archive Rules:**
- Preserve all relationships
- Maintain custom fields
- Keep searchable
- Create archive views
- Document location

---

## 4. 🚨 ERROR RECOVERY SYSTEM

### API Error Handling

| Error | User Message | Recovery |
|-------|-------------|----------|
| **Rate Limit** | "Processing your request..." | Queue with exponential backoff |
| **Permission** | "Need access. Try personal space?" | Offer alternatives |
| **Not Found** | "Can't find X. Did you mean Y?" | Suggest similar items |
| **Validation** | "I'll adjust that for you" | Auto-correct and retry |
| **Network** | "Connection issue. Retrying..." | Automatic retry (3x) |
| **Duplicate** | "Already exists. Update instead?" | Offer update or rename |

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **Can't find task** | Wrong list/space | Search across workspace |
| **Duplicate tasks** | Import issue | Merge or archive duplicates |
| **Broken dependencies** | Task deleted | Remove or reconnect |
| **View not loading** | Too many items | Add filters, reduce fields |
| **Automation failing** | Trigger issue | Check conditions, simplify |
| **Time tracking gaps** | Timer not stopped | Add manual entries |
| **Guest can't access** | Permission scope | Share parent folder/space |

### Recovery Strategies

**Graceful Degradation Path:**
```
1. Optimal → Full features with automation
2. Reduced → Core features, manual processes
3. Minimal → Basic structure only
4. Manual → Guide user through UI steps
```

**Alternative Approaches:**
- Can't create space → Use folders in existing space
- Complex automation fails → Use simpler triggers
- Custom field limit → Use tags or description
- Can't add dependency → Use relationship field
- API timeout → Batch operations smaller

---

## 5. 🎯 BEST PRACTICES

### Essential Custom Fields
Every list should consider:
1. **Status** - Workflow progression
2. **Priority** - Urgency/importance
3. **Due Date** - Deadline tracking
4. **Assignees** - Responsibility
5. **Time Estimate** - Planning
6. **Tags/Labels** - Categorization

### Status Workflow Design

**Standard Workflow:**
```
To Do → In Progress → Review → Complete
```

**Development Workflow:**
```
Backlog → Ready → In Development → Testing → Deploy → Done
```

**Content Workflow:**
```
Idea → Research → Writing → Editing → Review → Published
```

**Sales Workflow:**
```
Lead → Qualified → Proposal → Negotiation → Closed Won/Lost
```

### Automation Patterns

**Time-Saving Automations:**
```yaml
When: Status changes to Complete
Then: Move to Archive folder

When: Due date is approaching (1 day)
Then: Change priority to High

When: Task created
Then: Assign to project owner

When: Sprint ends
Then: Move incomplete to next sprint

When: Priority is Urgent
Then: Add to Today view
```

### Relationship Best Practices

**Dependency Types:**
- **Waiting On**: Task can't start until dependency completes
- **Blocking**: Task prevents others from starting
- **Related**: Reference connection without blocking

**Relationship Guidelines:**
- Limit chains to 3-4 levels deep
- Avoid circular dependencies
- Document critical path
- Use for project tasks, not simple todos

---

## 6. 👥 COLLABORATION PATTERNS

### Permission Levels

| Level | Can Do | Can't Do | Use For |
|-------|--------|----------|---------|
| **Owner** | Everything | Delete workspace | Admins |
| **Admin** | Manage all | Delete workspace | Managers |
| **Member** | Create & edit | Change settings | Team members |
| **Guest** | View & comment | Create new | Clients |

### Sharing Best Practices

**Lists:**
- Default: Member access for team
- Guest access for client review
- Share parent folder for bulk access

**Tasks:**
- Assignees get notifications
- Watchers for stakeholders
- Comments for collaboration

**Docs:**
- Collaborative editing enabled
- Version history maintained
- Export options available

### Team Patterns

**Task Assignment:**
- Single assignee for accountability
- Multiple assignees for collaboration
- Clear handoff in workflow
- @mentions for urgency

**Communication Flow:**
- Task comments for work discussion
- Docs for documentation
- Chat integration for quick questions
- Email for external communication

---

## 7. 📈 SCALABILITY GUIDELINES

### Growth Planning

**Phase 1: Foundation (0-6 months)**
- Basic lists and folders
- Essential custom fields
- Simple statuses
- Manual processes

**Phase 2: Optimization (6-12 months)**
- Views for each role
- Basic automations
- Time tracking
- Templates created

**Phase 3: Scale (12+ months)**
- Multiple spaces
- Complex automations
- Dashboards & reporting
- Integration ecosystem

### When to Split

| Split By | When | Example |
|----------|------|---------|
| **Team** | >10 people | Dev Space, Marketing Space |
| **Client** | >5 active clients | Client A Space, Client B Space |
| **Project** | Complex with >100 tasks | Project gets own space |
| **Time** | Yearly archives | 2024 Archive, 2025 Active |
| **Region** | Multiple offices | US Space, EU Space |

### Migration Patterns

**From Other Tools:**
```yaml
Trello → ClickUp:
  - Boards become Lists
  - Cards become Tasks
  - Lists become Statuses
  
Asana → ClickUp:
  - Projects become Lists
  - Sections become Statuses
  - Custom fields transfer

Jira → ClickUp:
  - Projects become Spaces
  - Epics become Folders
  - Issues become Tasks

Monday → ClickUp:
  - Boards become Lists
  - Groups become Views
  - Items become Tasks
```

---

## 8. 🎨 TEMPLATE DESIGN

### Template Components

**Every Template Includes:**
1. Pre-configured custom fields
2. Standard subtasks/checklist
3. Description template
4. Automation triggers
5. Default assignee logic

### Template Types

| Template Type | Use Case | Key Elements |
|---------------|----------|--------------|
| **Task Templates** | Repeated work | Checklist, time estimate |
| **List Templates** | New projects | Views, fields, statuses |
| **Space Templates** | Department setup | Full structure |
| **Doc Templates** | Meetings, reports | Sections, formatting |
| **Automation Templates** | Workflows | Triggers, actions |

### Template Best Practices

```yaml
Sprint Template:
  - Duration: 2 weeks
  - Ceremonies: Planning, Daily, Retro
  - Fields: Points, Epic, Component
  - Views: Board, Burndown, Velocity

Project Template:
  - Phases: Initiate, Plan, Execute, Close
  - Documents: Charter, Plan, Reports
  - Fields: Budget, Timeline, Owner
  - Views: Gantt, Progress, Risks

Client Template:
  - Structure: Info, Projects, Communication
  - Fields: Value, Industry, Contact
  - Documents: Contract, Notes
  - Views: Overview, Active, History
```

---

## 9. 📱 CROSS-PLATFORM DESIGN

### Mobile Optimization

**Mobile-Friendly:**
- List view (not table)
- 3-4 visible fields max
- Large touch targets
- Simple navigation
- Quick actions available

**Desktop-Optimized:**
- Table view with many columns
- Complex dashboards
- Keyboard shortcuts
- Bulk operations
- Advanced filtering

### View Strategy by Device

| Platform | Primary View | Fields Shown | Features |
|----------|-------------|--------------|----------|
| **Mobile** | List | Title, Status, Due | Quick add, comments |
| **Tablet** | Board | 5-6 key fields | Drag-drop, filters |
| **Desktop** | Table/Gantt | All relevant | Bulk edit, reports |

### Responsive Patterns

- Use Me Mode for personal mobile views
- Simplify mobile dashboard widgets
- Enable offline mode for mobile
- Configure mobile notifications
- Quick create shortcuts for mobile

---

## 10. ✅ QUALITY CHECKLIST

### Every Workspace Must Have:
- [ ] Clear space/folder/list hierarchy
- [ ] Consistent naming conventions
- [ ] Essential custom fields defined
- [ ] Helpful default views created
- [ ] Archive strategy documented
- [ ] Templates for repeated work
- [ ] Automations for common patterns
- [ ] Team permissions configured
- [ ] Mobile views optimized
- [ ] Dashboard for overview

### Common Mistakes to Avoid

| Mistake | Why Bad | Better Approach |
|---------|---------|-----------------|
| Too many custom fields | Overwhelming, slow | 5-8 essential only |
| No archive plan | Lists become huge | Regular archiving |
| Deep nesting | Hard to navigate | 3-4 levels max |
| Everyone admin | Security risk | Appropriate roles |
| No templates | Inconsistent work | Standard templates |
| Over-automation | Brittle, confusing | Simple, clear rules |
| Single view | Limits usability | Multiple perspectives |
| Complex dependencies | Fragile chains | Simple relationships |
| Ignoring mobile | Poor adoption | Mobile-first views |

### Performance Indicators

**Healthy Workspace:**
- Tasks complete in <3 clicks
- Views load in <2 seconds
- 80% tasks have clear status
- <5% overdue items
- Regular activity (daily updates)

**Warning Signs:**
- Lists taking >5 seconds to load
- Duplicate work being created
- Team not updating statuses
- Automations frequently failing
- Archive larger than active

---

*This intelligence layer ensures every ClickUp workspace is well-structured, performant, and scalable. By encoding expertise into automatic decisions, users get professional-quality workspaces without needing ClickUp expertise.*