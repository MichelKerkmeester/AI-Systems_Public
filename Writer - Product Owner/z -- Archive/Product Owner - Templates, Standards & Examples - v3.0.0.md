# Templates, Standards & Examples - v3.0.0

Complete templates, standards, and examples for the Product & Dev Ticket Writer system. Reference this for all formatting, symbols, and structure patterns.

## Table of Contents

1. [🔤 SYMBOL REFERENCE](#1--symbol-reference)
2. [📋 TICKET TEMPLATES](#2--ticket-templates)
3. [📚 DOCUMENTATION TEMPLATES](#3--documentation-templates)
4. [💻 SPEC TEMPLATES](#4--spec-templates)
5. [🎯 MODE EXAMPLES](#5--mode-examples)
6. [📊 ARTIFACT STRUCTURE](#6--artifact-structure)
7. [✅ QUALITY STANDARDS](#7--quality-standards)
8. [🔧 FORMATTING RULES](#8--formatting-rules)
9. [💡 REAL EXAMPLES](#9--real-examples)
10. [🚨 COMMON MISTAKES](#10--common-mistakes)

---

## 1. 🔤 SYMBOL REFERENCE

### Primary Symbols

| Symbol | Name | Usage | Context |
|--------|------|-------|---------|
| **⌘** | Command | Section headers, "About" | All modes |
| **◇** | Diamond | Requirements header | Tickets |
| **◻️** | Square | Feature sections | Documentation |
| **◊** | Small Diamond | Sub-headings (bold) | All modes |
| **→** | Arrow | References, links | All modes |
| **✦** | Star | Success criteria | Tickets (bullets) |
| **✓** | Check | Resolution checklist | Tickets (checkboxes) |
| **⊗** | Cross | Dependencies | Tickets |
| **⚡** | Lightning | Risks | Tickets |
| **⚠️** | Warning | Key problems | All modes |
| **≈** | Approximate | Reasons why | Tickets |
| **📚** | Books | Resources | Documentation |
| **—** | Em dash | Sub-categories | Under ◊ only |
| **•** | Bullet | Detail items | All modes |

### Hierarchy Rules

```markdown
# ⌘ Top Level
## ⌘ Major Section
### ◻️ or ◇ Feature/Requirement
**◊** Sub-heading
— Sub-category
• Detail point
```

---

## 2. 📋 TICKET TEMPLATES

### Quick Mode Template ($q)

```markdown
[BE] Feature Name

# ⌘ About

Brief description of the feature.

⚠️ **Key problem:**
The main issue being solved.

≈ **Reason why:**
The benefit of solving this.

## ◇ Requirements

**◊ Core Features**
— Essential functionality
• Must-have feature 1
• Must-have feature 2

## ✦ Success Criteria
- Measurable outcome 1
- Measurable outcome 2

## ✓ Resolution Checklist
[] Build core functionality
[] Add basic tests
[] Deploy to staging

**Labels:** feature, priority-high
```

### Standard Mode Template ($s)

```markdown
[FS] Feature Name

# ⌘ About

Comprehensive description of the feature and its context.

⚠️ **Key problems:**
* **Problem 1** - Impact on users
* **Problem 2** - Current limitation

≈ **Reasons why:**
This solution provides value by enabling users to accomplish their goals more efficiently.

## ◇ Requirements

**◊ Frontend Components**
— User Interface
• Component structure
• State management
• User interactions

---

**◊ Backend Services**
— API Development
• Endpoint definitions
• Data models
• Business logic

---

**◊ Database Changes**
— Schema Updates
• New tables
• Migrations
• Indexes

## ✦ Success Criteria
- 95% of users can complete the workflow
- Page load time under 2 seconds
- Zero critical bugs in production
- Positive user feedback score >4.0

## ✓ Resolution Checklist

### Foundation
[] Design and approve API contracts
[] Set up database schema
[] Create component structure

### Development
[] Implement backend services
[] Build frontend components
[] Add comprehensive tests

### Deployment
[] Deploy to staging environment
[] Complete QA testing
[] Release to production

## ⊗ Dependencies
- Design system v2.0
- Authentication service
- Analytics integration

**Labels:** feature, full-stack, q1-priority
```

### Complex Mode Template ($c)

```markdown
[FS] Complex Initiative Name

# ⌘ About

Strategic description of the major initiative and its business impact.

⚠️ **Key problems:**
* **Market gap** - Competitors offer this capability
* **User retention** - 30% drop-off at this point
* **Technical debt** - Current system cannot scale

≈ **Reasons why:**
This initiative transforms our platform's capability, enabling new revenue streams and improving user satisfaction scores by an estimated 40%.

## ◇ Implementation Approach

### Option A: Phased Rollout

**◊ Phase 1: Foundation (Week 1-2)**
— Core Infrastructure
• Set up new microservices architecture
• Implement basic data models
• Create CI/CD pipelines

---

**◊ Phase 2: MVP Features (Week 3-4)**
— Essential Functionality
• User authentication flow
• Basic CRUD operations
• Initial UI components

---

**◊ Phase 3: Advanced Features (Week 5-6)**
— Enhanced Capabilities
• Real-time updates
• Advanced filtering
• Analytics integration

---

**◊ Phase 4: Polish & Launch (Week 7-8)**
— Production Readiness
• Performance optimization
• Security hardening
• Documentation completion

## ✦ Success Criteria
- System handles 10,000 concurrent users
- 99.9% uptime SLA maintained
- User satisfaction score increases by 40%
- Revenue impact of $500K in Q1
- Zero security vulnerabilities

## ✓ Resolution Checklist

### Phase 1: Foundation
[] Architecture design approved
[] Infrastructure provisioned
[] Core services deployed

### Phase 2: MVP
[] Basic features functional
[] Initial testing complete
[] Staging deployment successful

### Phase 3: Enhancement
[] Advanced features integrated
[] Performance benchmarks met
[] Security audit passed

### Phase 4: Launch
[] Production deployment complete
[] Monitoring established
[] Documentation published

## ⊗ Major Dependencies
- Infrastructure team capacity
- Third-party API availability
- Security review approval
- Marketing launch coordination

## ⚡ Risks
- **Technical:** Legacy system integration complexity
- **Resource:** Team availability during Q4
- **External:** Third-party API rate limits

**Labels:** initiative, complex, strategic, q4-priority
```

---

## 3. 📚 DOCUMENTATION TEMPLATES

### Standard Documentation Template

```markdown
Analytics Dashboard Documentation

MODE: $doc
TYPE: Feature Documentation
MCP USED: Sequential Thinking
AUDIENCE: End Users

---

# ⌘ Overview

The Analytics Dashboard provides real-time insights into your application's performance, user behavior, and business metrics.

**Target Audience:** Product managers and analysts
**Complexity:** Intermediate
**Version:** 2.1.0
**Last Updated:** January 2025

---

## ⌘ Features

### ◻️ Dashboard Overview

The main dashboard presents key metrics at a glance, enabling quick decision-making.

**◊ Getting Started**
— Prerequisites
• Active account with analytics permissions
• Data collection enabled for at least 7 days
• Modern browser (Chrome, Firefox, Safari)

— First Steps
• Navigate to Analytics from main menu
• Select your date range
• Choose your primary metric view

---

**◊ Core Metrics**
— Available Metrics
• User engagement (DAU, MAU, retention)
• Performance metrics (load time, error rate)
• Business KPIs (conversion, revenue)
• Custom metrics (user-defined)

---

### ◻️ Custom Reports

Create tailored reports for specific business needs.

**◊ Report Builder**
— Creating Reports
• Select metrics to track
• Apply filters and segments
• Choose visualization type
• Set refresh frequency

— Sharing Options
• Export to PDF/CSV
• Email scheduled reports
• Embed in presentations
• Share via link

---

### ◻️ Data Export

Export your data for external analysis.

**◊ Export Options**
— Formats Available
• CSV for spreadsheets
• JSON for APIs
• SQL for databases
• Parquet for big data

---

## → Development References

**◊ Design Assets**
— Visual References
• [Dashboard Screenshots](link)
• [Video Walkthrough](link)
• [Interactive Demo](link)

---

**◊ Help Resources**
— Support Materials
• [FAQ](link)
• [Troubleshooting Guide](link)
• [Community Forum](link)

---

## ⚠️ Important Notes

- Data refreshes every 15 minutes
- Historical data available for 365 days
- Export limited to 100,000 rows
- Custom metrics require admin approval

---

## 📚 Additional Resources

- [Analytics Best Practices](link)
- [Metric Definitions](link)
- [API Documentation](link)
- [Training Videos](link)
```

---

## 4. 💻 SPEC TEMPLATES

### Simple Spec Template

```markdown
# Hidden Scrollbar

## Objective
Hide scrollbar while maintaining scroll functionality.

## Implementation
```css
.container {
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE/Edge */
}

.container::-webkit-scrollbar {
  display: none; /* Chrome/Safari/Opera */
}
```

## Browser Compatibility
- Chrome/Edge: ✓
- Firefox: ✓
- Safari: ✓

## Key Points
- Pure CSS solution
- No JavaScript required
```

### Component Spec Template

```markdown
# Data Table Component

## Objective
Sortable, filterable table with pagination.

## Implementation
```typescript
interface DataTableProps {
  data: any[];
  columns: Column[];
  pageSize?: number;
}

export const DataTable: React.FC<DataTableProps> = ({ 
  data, 
  columns, 
  pageSize = 10 
}) => {
  const [page, setPage] = useState(0);
  const [sortBy, setSortBy] = useState(null);
  const [filterBy, setFilterBy] = useState('');
  
  const filtered = useMemo(() => 
    data.filter(row => 
      JSON.stringify(row).includes(filterBy)
    ), [data, filterBy]);
    
  const sorted = useMemo(() => {
    if (!sortBy) return filtered;
    return [...filtered].sort((a, b) => 
      a[sortBy] > b[sortBy] ? 1 : -1
    );
  }, [filtered, sortBy]);
  
  const paged = sorted.slice(
    page * pageSize, 
    (page + 1) * pageSize
  );
  
  return (
    <div>
      <input 
        placeholder="Filter..." 
        onChange={e => setFilterBy(e.target.value)}
      />
      <table>
        <thead>
          <tr>
            {columns.map(col => (
              <th key={col.key} onClick={() => setSortBy(col.key)}>
                {col.label}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {paged.map((row, i) => (
            <tr key={i}>
              {columns.map(col => (
                <td key={col.key}>{row[col.key]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      <Pagination 
        page={page} 
        total={Math.ceil(sorted.length / pageSize)}
        onChange={setPage}
      />
    </div>
  );
};
```

## Key Points
- Memoized filtering/sorting
- Configurable page size
- Add virtualization for large datasets
```

---

## 5. 🎯 MODE EXAMPLES

[Content continues with specific examples for each mode...]

---

## 6. 📊 ARTIFACT STRUCTURE

### Ticket Artifact Structure
```
[SCOPE] Feature Name (artifact title)
# ⌘ About (first heading)
Description with ⚠️ and ≈
## ◇ Requirements
## ✦ Success Criteria
## ✓ Resolution Checklist
## ⊗ Dependencies (if needed)
Labels: (at bottom)
```

### Documentation Artifact Structure
```
Product Documentation (artifact title)
# ⌘ Overview (first heading)
Metadata block
## ⌘ Features
### ◻️ Feature sections
## → References
## ⚠️ Important Notes
## 📚 Resources
```

---

## 7. ✅ QUALITY STANDARDS

### Ticket Quality
- Clear problem statement
- Measurable success criteria
- Actionable resolution items
- Proper symbol usage
- Dividers between subsections
- User-specified scope and labels

### Documentation Quality
- Defined audience
- Logical feature flow
- Appropriate depth
- Helpful resources
- Version information
- Clear limitations

---

## 8. 🔧 FORMATTING RULES

### Mandatory Rules
1. First heading always ⌘ About/Overview
2. Symbols required for all sections
3. ✦ for success (bullets only)
4. ✓ for resolution (checkboxes only)
5. Bold **◊** sub-headings
6. Em dash — only under ◊
7. Dividers between ◊ subsections
8. Platform offer in chat, not artifact

### Style Rules
- 20% more concise than v4.1
- No space in checkbox brackets []
- Max 3 items per resolution section
- Outcomes not tasks in resolution
- Brief descriptions with structure

---

## 9. 💡 REAL EXAMPLES

[Include actual ticket examples from real usage...]

---

## 10. 🚨 COMMON MISTAKES

### Avoid These
❌ Missing ⌘ in first heading
❌ Mixing ✦ and ✓ symbols
❌ Space in checkboxes [ ]
❌ Platform offer in artifact
❌ Skipping interactive offer for $s/$c
❌ Assuming scope or labels
❌ Implementation details in tickets
❌ Missing dividers between subsections

### Do These Instead
✅ # ⌘ About always first
✅ ✦ bullets, ✓ checkboxes
✅ [] no space in brackets
✅ Platform offer in chat
✅ Always offer interactive for $s/$c
✅ Ask for scope and labels
✅ Focus on WHAT not HOW
✅ Add --- between ◊ sections

---

*Complete reference for Product & Dev Ticket Writer. Use these templates and standards for consistent, professional output.*