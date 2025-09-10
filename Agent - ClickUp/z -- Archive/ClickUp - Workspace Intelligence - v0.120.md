# ClickUp - Workspace Intelligence - v0.120

Best practices, decision frameworks, and error recovery for optimal ClickUp workspace design. All decisions made through intelligent conversation with user-controlled thinking depth.

## Table of Contents

1. [📊 Decision Frameworks](#1-📊-decision-frameworks)
2. [🧠 Thinking Depth Guidelines](#2-🧠-thinking-depth-guidelines)
3. [🏗 Workspace Architecture](#3-🏗-workspace-architecture)
4. [⚡ Performance Optimization](#4-⚡-performance-optimization)
5. [🚨 Error Recovery System](#5-🚨-error-recovery-system)
6. [🎯 Best Practices](#6-🎯-best-practices)
7. [👥 Collaboration Patterns](#7-👥-collaboration-patterns)
8. [📈 Scalability Guidelines](#8-📈-scalability-guidelines)
9. [🎨 Template Intelligence](#9-🎨-template-intelligence)
10. [📱 Cross-Platform Optimization](#10-📱-cross-platform-optimization)
11. [✅ Quality Assurance](#11-✅-quality-assurance)
12. [📄 Continuous Improvement](#12-📄-continuous-improvement)

---

## 1. 📊 DECISION FRAMEWORKS

### List vs Space Decision (Through Conversation)

The system determines structure through natural dialogue:

```
User: "organize my work"
System: "I'll help you organize! Are you managing different types of projects 
        or similar work that follows the same process?"

Based on answer:
- Similar work → Single list with views
- Different types → Multiple lists or spaces

System: "How many thinking rounds should I use for the design?
        • Quick (2-3) - Basic structure
        • Standard (4-6) - Well-organized system"
```

| Use LIST When | Use SPACE When | Thinking Depth |
|---------------|----------------|----------------|
| Related tasks/items | Different departments/teams | Quick (2-3) |
| Same workflow applies | Different workflows needed | Standard (4-6) |
| Under 5,000 items | Multiple lists needed | Standard (4-6) |
| Single view sufficient | Separate permissions required | Thorough (7-10) |
| One team manages | Multiple teams involved | Thorough (7-10) |
| Shared custom fields | Different field requirements | Standard (4-6) |

**Quick Rule:** If you'll have more than 3 distinct workflows, use separate spaces.

### Custom Field Selection (Intelligent Defaults)

The system automatically selects appropriate fields based on context and thinking depth:

| Field Type | Auto-Applied When | Thinking Impact |
|------------|------------------|-----------------|
| **Dropdown** | Status/category needed | More rounds = more options |
| **Labels** | Multiple tags detected | Standard+ adds categories |
| **Users** | Team collaboration mentioned | Standard+ adds roles |
| **Date** | Timeline/deadline mentioned | Quick adds basic, Standard+ adds ranges |
| **Number** | Metrics/counting detected | More rounds = better calculations |
| **Money** | Financial context | Thorough adds profitability |
| **Progress** | Completion tracking needed | Standard+ adds milestones |
| **Checkbox** | Yes/no decision | Quick for all depths |
| **Relationship** | Connection mentioned | Thorough adds full hierarchy |

### View Optimization (Automatic Selection)

Based on detected use case and thinking depth:

| Primary Use Case | Views Created | Default View | Thinking Impact |
|-----------------|---------------|--------------|-----------------|
| Task Management | List, Board, Calendar | List (mobile) / Board (desktop) | More rounds = more views |
| Project Tracking | Gantt, Board, Table | Gantt | Thorough adds dependencies |
| Sprint Planning | Board, List, Velocity | Board | Standard+ adds metrics |
| Content Calendar | Calendar, Pipeline, List | Calendar | More rounds = platform views |
| CRM/Sales | Pipeline, List, Table | Pipeline | Thorough adds analytics |
| Bug Tracking | List (priority), Board | List | Standard+ adds severity matrix |

---

## 2. 🧠 THINKING DEPTH GUIDELINES

### When to Recommend Each Depth

**Quick Thinking (2-3 rounds):**
- Single item operations
- Basic lists without relationships
- Simple archiving/cleanup
- Clear, specific requests
- Personal task management
- Time-sensitive requests

**Standard Thinking (4-6 rounds):**
- Multi-field lists
- Basic workspace setup
- Team collaboration features
- Template creation
- Standard business processes
- Typical user requests

**Thorough Thinking (7-10 rounds):**
- Complete workspace systems
- Multi-list relationships
- Complex automations
- Department-wide solutions
- Integration planning
- Unclear/broad requests

**Maximum Thinking (10+ rounds):**
- Enterprise architecture
- Cross-functional systems
- Complex migration planning
- Industry-specific solutions
- Regulatory compliance needs
- Mission-critical systems

### Thinking Depth Impact on Features

| Feature | Quick (2-3) | Standard (4-6) | Thorough (7-10) | Maximum (10+) |
|---------|-------------|----------------|-----------------|---------------|
| **Custom Fields** | 3-4 essential | 5-7 relevant | 8-10 comprehensive | All needed |
| **Views** | 2 basic | 3-4 useful | 5-6 complete | All applicable |
| **Automations** | 1-2 simple | 3-5 helpful | 6-8 integrated | Full workflow |
| **Relationships** | None/basic | Parent-child | Multi-level | Complete graph |
| **Templates** | Basic | Standard | Advanced | Industry-specific |
| **Permissions** | Simple | Role-based | Granular | Enterprise |

### User Guidance for Choosing Depth

```
System: "How many thinking rounds should I use?

Quick (2-3): Fast setup, essential features only
• Best for: Simple tasks, personal use, urgent needs
• Time: ~30 seconds analysis

Standard (4-6): Balanced approach, good practices
• Best for: Most requests, team work, typical projects  
• Time: ~1 minute analysis

Thorough (7-10): Complete system, all integrations
• Best for: Complex needs, multiple teams, long-term use
• Time: ~2 minutes analysis

Or specify exact rounds (1-15) for custom depth!"
```

---

## 3. 🏗 WORKSPACE ARCHITECTURE

### Intelligent Structure Design

The system determines optimal hierarchy through conversation and thinking depth:

**Conversation Pattern:**
```
User: "set up for my company"
System: "I'll create your company workspace! 
        Is this for a single team or multiple departments?"
        
User: "multiple departments"
System: "Perfect! I'll create a space for each department.
        Main departments to include? (Engineering, Marketing, Sales...)
        
        Also, how thorough should my analysis be?
        • Standard (4-6) - Core structure
        • Thorough (7-10) - Full integration (recommended)"
```

**Optimal Structure (varies by thinking depth):**
```
Workspace (Thorough: 8+ rounds)
├── Spaces (departments/teams)
│   ├── Folders (categories)
│   │   ├── Lists (work streams)
│   │   │   └── Tasks (items)

Workspace (Standard: 4-6 rounds)
├── Spaces (main areas)
│   ├── Lists (work types)
│   │   └── Tasks (items)

Workspace (Quick: 2-3 rounds)
├── Lists (basic organization)
│   └── Tasks (items)
```

### Organization Methods (Auto-Selected by Thinking Depth)

**Team-Based** (Detected: "departments", "teams")
```
🏢 Company (Thorough: 8+ rounds)
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

Quick version (2-3 rounds): Single list with team tags
Standard version (4-6 rounds): Separate lists per team
```

**Project-Based** (Detected: "projects", "initiatives")
```
📊 Projects (Standard thinking creates basic structure)
├── 🚀 Project Alpha
│   ├── Planning
│   ├── Execution
│   └── Review
├── 🎯 Project Beta
│   ├── Planning
│   ├── Execution
│   └── Review

Thorough thinking (7-10): Adds dependencies, resource allocation, risk tracking
```

### Naming Conventions (Applied Based on Thinking Depth)

| Type | Pattern | Example | Thinking Impact |
|------|---------|---------|-----------------|
| **Spaces** | [Emoji] [Department/Team] | 💻 Engineering | All depths |
| **Folders** | [Category] - [Descriptor] | Projects - Active | Standard+ |
| **Lists** | [Type] : [Specific] | Sprint : 23 | All depths |
| **Tasks** | [Action] [Object] | Review Homepage Design | All depths |
| **Templates** | [TEMPLATE] [Name] | TEMPLATE Sprint Planning | Standard+ |
| **Archives** | [ARCHIVE] [Year] [Type] | ARCHIVE 2024 Completed | Standard+ |

---

## 4. ⚡ PERFORMANCE OPTIMIZATION

### List Size Management (Automatic with Thinking Awareness)

The system monitors and suggests optimization based on thinking depth:

| Size | Tasks | System Response | Thinking Adjustment |
|------|-------|-----------------|---------------------|
| **Small** | <1,000 | All features enabled | Any depth works |
| **Medium** | 1,000-5,000 | "I'll add filtered views for performance" | Standard+ recommended |
| **Large** | 5,000-25,000 | "Let's split this into folders" | Thorough required |
| **Very Large** | >25,000 | "This needs separate lists for speed" | Maximum thinking needed |

### Performance Best Practices (Auto-Applied by Depth)

**Fast Patterns Applied:**
- Quick (2-3): Minimal fields, simple views
- Standard (4-6): Optimized fields, smart filters
- Thorough (7-10): Full features with performance guards
- Maximum (10+): Enterprise optimization patterns

**Patterns by Thinking Depth:**
| Depth | Fields | Views | Automations | Relationships |
|-------|--------|-------|-------------|---------------|
| Quick | 3-4 max | 2 simple | 1-2 basic | None/simple |
| Standard | 5-7 optimal | 3-4 filtered | 3-5 helpful | Parent-child |
| Thorough | 8-10 complete | 5-6 optimized | 6-8 chained | Multi-level |
| Maximum | As needed | All required | Full workflow | Complete |

### Archive Strategy (Automatic Setup by Depth)

| Context | Archive Rule | Destination | Thinking Impact |
|---------|-------------|-------------|-----------------|
| **Tasks** | Complete + 30 days | /Archive/[Year]/Tasks/ | All depths |
| **Sprints** | Sprint end + 14 days | /Archive/Sprints/[Sprint#]/ | Standard+ |
| **Projects** | Complete + 60 days | /Archive/Projects/[Year]/ | Standard+ |
| **Quarterly** | Every 3 months | /Archive/[Year]/Q[#]/ | Thorough+ |

---

## 5. 🚨 ERROR RECOVERY SYSTEM

### Conversational Error Handling with Thinking Awareness

| Error | User-Friendly Response | Recovery Path | Thinking Note |
|-------|------------------------|---------------|---------------|
| **Rate Limit** | "Processing your large request..." | Batch in smaller groups | Maintain chosen depth |
| **Permission** | "I need access to that space" | Offer alternatives | Same thinking depth |
| **Not Found** | "Can't find that. Similar options:" | Show suggestions | Ask for new depth |
| **Duplicate** | "That already exists!" | Update or rename | Quick decision |
| **Network** | "Connection hiccup. Retrying..." | Auto-retry 3x | Keep depth |
| **Validation** | "Let me adjust that for you" | Fix and proceed | Same depth |

### Common Issues & Smart Solutions

**Permission Denied:**
```
System: "I can't access that space, but no problem!
        I can:
        • Create in your personal space instead
        • Help you request access
        • Use a different location
        Which works best?
        (I'll use the same thinking depth you chose)"
```

**Already Exists:**
```
System: "You have a 'Tasks' list already!
        Should I:
        • Add to existing list
        • Create 'Tasks v2'
        • Enhance current list
        • Archive old, create new?
        
        Quick decision - how many thinking rounds?
        • Quick (2) - Just rename
        • Standard (4) - Merge smartly"
```

**Too Complex:**
```
System: "That's quite comprehensive!
        For best performance, I recommend:
        • Start with core features (Quick: 2-3 rounds)
        • Build complete system (Thorough: 7-10 rounds)
        • Create everything (Maximum: 10+ rounds)
        
What fits your needs?"
```

### Recovery Strategies

**Graceful Degradation:**
1. Try optimal approach (with chosen thinking)
2. Fallback to simpler version (reduce thinking if needed)
3. Offer manual alternative (quick thinking)
4. Guide through UI if needed (minimal thinking)

**Alternative Paths:**
- Can't create space → Use folders (same depth)
- Complex automation fails → Simple rules (reduce depth)
- Custom field limit → Use tags (quick adjustment)
- Can't add dependency → Use relationships (standard depth)
- API timeout → Smaller batches (maintain depth)

---

## 6. 🎯 BEST PRACTICES

### Essential Custom Fields (Auto-Selected by Context and Thinking)

Every list gets context-appropriate fields scaled by thinking depth:

**Task Lists:**
| Field | Quick (2-3) | Standard (4-6) | Thorough (7-10) |
|-------|-------------|----------------|-----------------|
| Status | ✓ Basic | ✓ Full workflow | ✓ Complex stages |
| Priority | ✓ High/Low | ✓ 4 levels | ✓ Matrix system |
| Due Date | ✓ Simple | ✓ With reminders | ✓ Dependencies |
| Assignee | Optional | ✓ Single | ✓ Multiple + roles |
| Time Estimate | - | ✓ Hours | ✓ Detailed tracking |
| Category | - | ✓ Tags | ✓ Hierarchical |

**Project Lists:**
| Field | Quick (2-3) | Standard (4-6) | Thorough (7-10) |
|-------|-------------|----------------|-----------------|
| Phase | ✓ Simple | ✓ Standard | ✓ Gate system |
| Timeline | ✓ Dates | ✓ Range | ✓ Milestones |
| Budget | - | ✓ Total | ✓ Breakdown |
| Owner | ✓ Single | ✓ Team | ✓ RACI matrix |
| Risk Level | - | ✓ Basic | ✓ Full assessment |
| Progress | ✓ % | ✓ Weighted | ✓ Earned value |

### Status Workflow Design (Intelligent Selection by Depth)

**Standard Task Flow:**
- Quick: `To Do → In Progress → Done`
- Standard: `To Do → In Progress → Review → Complete`
- Thorough: `Backlog → To Do → In Progress → Review → Testing → Complete → Archived`

**Development Flow:**
- Quick: `Todo → Doing → Done`
- Standard: `Backlog → Ready → In Development → Testing → Done`
- Thorough: `Backlog → Ready → In Development → Code Review → Testing → Staging → Deploy → Done`

### Automation Patterns (Auto-Configured by Thinking Depth)

**Automations by Thinking Level:**
```yaml
Quick (2-3 rounds):
  - Status Complete → Archive after 30 days
  - Due date today → Priority High

Standard (4-6 rounds):
  - Due date approaching → Priority to High
  - Task created → Assign to project owner
  - Overdue → Send notification
  - Sprint ends → Move incomplete to next

Thorough (7-10 rounds):
  - Complex conditional workflows
  - Multi-step approval processes
  - Cross-list dependencies
  - Resource allocation rules
  - SLA tracking
  - Escalation paths

Maximum (10+ rounds):
  - Enterprise workflow orchestration
  - Compliance tracking
  - Audit trails
  - Complex integrations
```

### Relationship Configuration by Depth

**Smart Relationship Setup:**
- Quick: Basic parent-child only
- Standard: Dependencies for project tasks
- Thorough: Full relationship graph
- Maximum: Enterprise architecture

**Guidelines Applied by Thinking:**
- Quick: Max 2 relationship levels
- Standard: Max 3-4 relationship levels
- Thorough: Full hierarchy as needed
- All: No circular dependencies

---

## 7. 👥 COLLABORATION PATTERNS

### Permission Setup (Conversation-Based with Thinking)

```
System: "Who needs access to this?
        • Just you (private)
        • Your team (collaborate)
        • Clients too (guest access)
        
        Also, thinking depth for permissions?
        • Quick (2) - Basic access
        • Standard (4) - Role-based
        • Thorough (7) - Granular control"
        
Based on answers, applies appropriate permissions
```

### Permission Levels Applied by Thinking Depth

| Level | Quick Setup | Standard Setup | Thorough Setup |
|-------|------------|----------------|----------------|
| **Owner** | You only | Admin team | Department heads |
| **Admin** | - | Team leads | Project managers |
| **Member** | Everyone | Team members | Contributors |
| **Guest** | - | Clients | Stakeholders + vendors |

### Team Collaboration Features by Depth

**Automatically Enabled:**
- Quick (2-3): Basic assignments, simple sharing
- Standard (4-6): @mentions, shared views, workload
- Thorough (7-10): Full RACI, resource planning, capacity
- Maximum (10+): Enterprise governance, approval chains

---

## 8. 📈 SCALABILITY GUIDELINES

### Growth Planning (Proactive with Thinking)

The system plans for growth based on thinking depth:

**Starting Small (Quick thinking):**
```
System: "I'm setting this up simply for now.
        We can always expand later!"
```

**Growth Ready (Standard thinking):**
```
System: "I'm structuring this to grow with you.
        Room for team expansion built in!"
```

**Enterprise Scale (Thorough thinking):**
```
System: "Building with full scalability.
        Ready for hundreds of users!"
```

### When to Split (Automatic Suggestions by Usage)

| Indicator | System Suggestion | Thinking to Handle |
|-----------|------------------|-------------------|
| >10 team members | "Consider department spaces" | Standard (4-6) |
| >5 active clients | "Let's create client folders" | Standard (4-6) |
| >100 tasks/project | "Project needs own list" | Thorough (7-10) |
| >1000 items/list | "Time to add folders" | Standard (4-6) |
| Yearly transition | "Archive last year's work" | Quick (2-3) |

### Migration Support with Thinking

**From Other Tools (Detected in conversation):**
```
User: "moving from Trello"
System: "I'll structure this to make migration easy!
        
        How thorough should the migration planning be?
        • Quick (2-3) - Basic structure match
        • Standard (4-6) - Enhanced Trello features
        • Thorough (7-10) - Complete transformation
        
        Your boards → lists, cards → tasks, with chosen enhancements!"
```

---

## 9. 🎨 TEMPLATE INTELLIGENCE

### Template Creation (Automatic with Thinking)

When patterns repeat, system suggests templates:

```
System: "I notice you're creating similar projects!
        Should I save this as a template?
        
        Template complexity:
        • Quick (2) - Basic structure
        • Standard (4) - With automations
        • Thorough (7) - Full system template"
```

### Smart Template Components by Depth

**Every Template Includes (scaled by thinking):**
1. Pre-configured custom fields (more with depth)
2. Standard subtasks/checklist (detailed with depth)
3. Description template (comprehensive with depth)
4. Default assignee logic (complex with depth)
5. Automation triggers (advanced with depth)

### Template Types (Context-Based with Thinking)

| Detected Pattern | Quick Template | Standard Template | Thorough Template |
|-----------------|---------------|------------------|------------------|
| Repeated sprints | Basic sprint | Sprint + ceremonies | Full agile template |
| Similar projects | Project outline | Project + phases | Complete methodology |
| Regular meetings | Simple agenda | Meeting + actions | Full documentation |
| Client onboarding | Basic checklist | Onboarding flow | Complete playbook |

---

## 10. 📱 CROSS-PLATFORM OPTIMIZATION

### Device Detection & Optimization with Thinking

```
System: "I'll optimize this for how you work!
        Primarily desktop, mobile, or both?
        
        Also, interface complexity:
        • Quick (2-3) - Simple, works everywhere
        • Standard (4-6) - Optimized per platform
        • Thorough (7-10) - Full feature set
        
Based on answer, creates appropriate views"
```

### View Strategy by Platform and Thinking

| Platform | Quick (2-3) | Standard (4-6) | Thorough (7-10) |
|----------|-------------|----------------|-----------------|
| **Mobile** | Simple list | List + board | Full Me Mode |
| **Tablet** | List + board | Board + calendar | Multi-view |
| **Desktop** | All basics | Table + Gantt | Everything |

### Responsive Design Patterns by Thinking

**Mobile Optimization (scales with depth):**
- Quick: Essential fields only
- Standard: Me Mode + quick actions
- Thorough: Full mobile workspace

**Desktop Power Features (scales with depth):**
- Quick: Basic views
- Standard: Multi-column + filters
- Thorough: Full analytics + dashboards

---

## 11. ✅ QUALITY ASSURANCE

### Every Workspace Includes (Checked by Thinking Depth)

**Automatic Quality Checks:**
- [ ] Clear hierarchy structure (all depths)
- [ ] Consistent naming conventions (all depths)
- [ ] Essential custom fields only (scaled by depth)
- [ ] Appropriate views created (scaled by depth)
- [ ] Archive strategy in place (Standard+)
- [ ] Templates for repeated work (Standard+)
- [ ] Basic automations configured (Standard+)
- [ ] Permissions properly set (all depths)
- [ ] Mobile views optimized (Standard+)
- [ ] Success metrics defined (Thorough+)

### Common Pitfalls Avoided by Thinking Level

| Pitfall | Why Bad | Quick Fix | Standard Fix | Thorough Fix |
|---------|---------|-----------|--------------|--------------|
| Too many fields | Overwhelming | 3-4 max | 5-7 optimal | 8-10 organized |
| No archive plan | Lists huge | Manual | 30-day auto | Smart rules |
| Deep nesting | Hard to nav | 2 levels | 3-4 levels | Organized hierarchy |
| Everyone admin | Security | Owner only | Roles | Granular |
| No templates | Inconsistent | - | Basic | Advanced |
| Over-automation | Brittle | Minimal | Balanced | Sophisticated |

### Success Indicators by Thinking Depth

**Healthy Workspace Signs:**
- Quick: Tasks manageable, basic organization
- Standard: Efficient workflow, good structure
- Thorough: Scalable system, full tracking
- Maximum: Enterprise ready, compliant

**System Monitoring:**
```
System notices issues and adjusts suggestions based on thinking:
"Your list is getting large! Should I help you archive?
 • Quick (2) - Simple archive
 • Standard (4) - Organized structure"
```

---

## 12. 📄 CONTINUOUS IMPROVEMENT

### Learning from Usage with Thinking Patterns

The system adapts based on patterns:

**Frequently Asked → Becomes Default:**
- User always chooses "Thorough" → Suggest as default
- User prefers "Quick" → Start with quick option
- User specifies exact numbers → Remember preference

**Conversation Refinement by Thinking:**
- Quick chosen often → Reduce initial questions
- Thorough chosen often → Offer more options
- Mixed choices → Always ask preference

### Intelligent Suggestions Based on History

**Proactive Improvements:**
```
"I noticed you usually prefer Standard thinking (4-6 rounds).
 Should I make that your default?"

"Your sprints are consistent! With Standard thinking,
 I can create the next 4 automatically."

"You have 50+ completed tasks. Quick cleanup (2 rounds)
 or organized archive (4 rounds)?"
```

### User Preference Learning

**Pattern Recognition:**
- New users: Guide to appropriate depth
- Power users: Remember preferred depths
- Context-aware: Different depths for different tasks
- Adaptive: Learn from success/failure

**Depth Preference Tracking:**
- Personal tasks → Usually Quick (2-3)
- Team projects → Usually Standard (4-6)
- System setup → Usually Thorough (7-10)
- Migrations → Often Maximum (10+)

---

*This intelligence layer ensures every ClickUp workspace is well-structured, performant, and scalable through user-controlled thinking depth. Through natural conversation and adaptive intelligence, it applies expertise automatically while educating users and respecting their preferences for analysis depth.*