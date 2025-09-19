# Ticket - Examples Library - v2.3.0

Concise examples showing real-world ticket implementations with developer clarity.

## Table of Contents

1. [🚀 QUICK MODE EXAMPLES](#1--quick-mode-examples)
2. [📋 STANDARD MODE EXAMPLES](#2--standard-mode-examples)
3. [🔧 COMPLEX MODE EXAMPLES](#3--complex-mode-examples)
4. [🐛 BUG TICKET EXAMPLES](#4--bug-ticket-examples)
5. [📈 IMPROVEMENT EXAMPLES](#5--improvement-examples)
6. [🎨 PARTIAL INPUT EXAMPLES](#6--partial-input-examples)
7. [🎯 FEATURE TYPE PATTERNS](#7--feature-type-patterns)
8. [💻 SPEC MODE EXAMPLES](#8--spec-mode-examples)

---

## 1. 🚀 QUICK MODE EXAMPLES

### Example: Profile Picture Upload

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A

---

# ■ About

Users need profile personalization but only have generic placeholders.

⚠️ **Key problems:**
* **Low engagement** - Profiles feel impersonal
* **Support tickets** - Weekly requests for profile pictures
* **Competitive gap** - All competitors offer this

≈ **Reasons why:**
Profile pictures with automatic processing increase engagement and reduce support burden.

**User Value:** Personalize your profile with a photo

**Business Goal:** Increase profile completion rate

---

## ◇ Requirements
- Upload from device
- Basic cropping
- Replace existing
- JPG/PNG support
- File size limit
- Auto thumbnails

---

## ✦ Success Criteria
- Images upload successfully
- Size limit enforced
- Photo displays immediately
- Thumbnails in seconds

---

## ✓ Resolution Checklist

### Implementation
[ ] Build upload handler
[ ] Configure S3 processing

### Testing
[ ] Verify across devices
[ ] Validate file limits

---

## Labels
`Backend-System`, `API`, `feature`, `User-Management`
```

---

## 2. 📋 STANDARD MODE EXAMPLES

### Example: Advanced Search Filters

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

# ■ About

Search functionality fails user needs, causing lost revenue.

⚠️ **Key problems:**
* **High abandonment** - Users give up before finding products
* **Multiple attempts** - Users repeatedly refine without success
* **Top complaint** - "Can't find products" most common ticket

≈ **Reasons why:**
Powerful filtering for category, price, and availability reduces abandonment and increases conversion.

**User Value:** Find exactly what you need with filters

**Business Goal:** Reduce search abandonment rate

---

## ◇ Requirements

**◊** Filter Panel
— Components
• Category multi-select
• Date range picker
• Price slider
• Status checkboxes
— Behavior
• Instant results (debounced)
• Active filter count
• Clear all button
• Session persistence

**◊** Mobile
— Layout
• Bottom sheet pattern
• Sticky apply button
— Interactions
• Swipe dismiss
• Tap outside close

---

## → Designs & References
- [Figma - Desktop](link)
- [Figma - Mobile](link)

**Notice:** Mobile uses bottom sheet for accessibility

---

## ✦ Success Criteria
- Results update quickly
- All combinations work
- Filter state persists
- Mobile gestures smooth

---

## ✓ Resolution Checklist

### Foundation
[ ] Build components
[ ] Connect to API

### Features
[ ] Implement all filters
[ ] Add mobile sheet

### Testing
[ ] Cross-browser testing
[ ] Performance verification

### Documentation
[ ] Update component docs
[ ] Create usage guide

---

## ⊗ Dependencies
- Requires: Search API v2 (#2234)
- Blocks: Saved searches (#2240)

---

## Labels
`[App]-App`, `UI`, `Search`, `feature`
```

---

## 3. 🔧 COMPLEX MODE EXAMPLES

### Example: Real-time Collaboration

```markdown
MODE: $c
TICKET TYPE: Complex
MCP USED: Cascade Thinking
INTERACTIVE OFFERED: Yes - Accepted

---

# ■ About

Real-time collaboration is critical for remote teams working asynchronously.

⚠️ **Key problems:**
* **Version conflicts** - Majority of documents have merge issues
* **Lost work** - Hours lost weekly to overwrites
* **Workflow delays** - Teams wait for document handoffs
* **Competitive pressure** - Losing enterprise deals

≈ **Reasons why:**
Google Docs-level collaboration with WebSockets and OT algorithms eliminates conflicts and enables seamless teamwork.

**User Value:** Work together without version conflicts

**Business Goal:** Increase team plan adoption

---

[[*TOC*]]

---

## → Designs & References

### ◻️ Editor
- [Figma - Cursors](link)
- [Figma - Presence](link)

### ◻️ Technical
- [WebSocket Architecture](link)
- [OT Algorithm](link)

**Notice:** Maximum 10 concurrent editors

---

## ◇ Implementation Approach

### Option A: Phased Development

#### Phase 1: Foundation (Week 1-2)

**◊** WebSocket
— Server
• Configuration
• Connection pooling
• Load balancing
— Client
• Client library
• Reconnection logic
• State management

**◊** Presence
— Backend
• Session tracking
• Heartbeat
— Frontend
• Indicators
• User list

#### Phase 2: Core (Week 3-4)

**◊** OT Algorithm
— Implementation
• Transform functions
• Operation queue
— Integration
• State management
• Conflict resolution

**◊** Multi-cursor
— Tracking
• Position calculation
• Broadcasting
— Rendering
• Cursor colors
• User labels

#### Phase 3: Polish (Week 5-6)

**◊** Optimization
— Performance
• Batch operations
• Compression
— Features
• Offline queue
• Sync on reconnect

---

## ✦ Success Criteria
- Minimal cursor latency
- Support 10 editors
- High uptime
- Seamless offline sync
- Zero data loss

---

## ✓ Resolution Checklist

### Phase 1
[ ] Set up WebSocket
[ ] Implement presence

### Phase 2
[ ] Implement OT
[ ] Build cursor system

### Phase 3
[ ] Optimize performance
[ ] Add monitoring

### Testing
[ ] Load test 10+ users
[ ] Verify failover

### Documentation
[ ] Document API
[ ] Create training

### Launch
[ ] Performance benchmarks
[ ] Rollback ready

---

## ⊗ Dependencies
- Requires: WebSocket infrastructure (#5001)
- Requires: Document versioning (#5002)
- Blocks: Enterprise features (#5050)

---

## ⚠ Risks
- **Scale:** WebSocket costs
- **Complexity:** OT edge cases
- **Browser:** Compatibility

---

## Labels
`Backend-System`, `[App]-App`, `WebSocket`, `feature`
```

---

## 4. 🐛 BUG TICKET EXAMPLES

### Example: Search Filter Reset Bug

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

# ■ About

Critical bug severely impacts search functionality.

⚠️ **Key problems:**
* **All users affected** - Everyone loses filters on back
* **High abandonment** - One in four users leave
* **Support volume** - Hundreds of complaints monthly

≈ **Reasons why:**
Fixing restores expected behavior and recovers lost revenue.

**User Value:** Keep filters when returning to search

**Business Goal:** Eliminate frustration and abandonment

---

## ◆ Current Behavior
1. Apply filters
2. Click result
3. Click back
4. **Bug:** Filters cleared

---

## ✦ Desired Behavior
- Filters persist
- Selected visible
- Results filtered
- URL reflects state

---

## ◈ Steps to Reproduce
1. Go to search
2. Apply category + date
3. Click any result
4. Click browser back
5. Observe reset

---

## → Evidence
- [Video - Bug](link)
- [Console Error](link)

**Notice:** Worked before v2.3.0

---

## ✦ Success Criteria
- Filters persist always
- Works all browsers
- No performance impact
- URL maintained

---

## ✓ Resolution Checklist

### Investigation
[ ] Identify root cause
[ ] Review v2.3.0 changes

### Fix
[ ] Fix state management
[ ] Add session backup

### Verification
[ ] Test all filters
[ ] Add regression tests

---

## Labels
`[App]-App`, `UI`, `bug`, `Search`
```

---

## 5. 📈 IMPROVEMENT EXAMPLES

### Example: Dashboard Performance

```markdown
MODE: $s
TICKET TYPE: Improvement
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Accepted

---

# ■ About

Dashboard is critical pain point driving users away.

⚠️ **Key problems:**
* **Slow load** - Blank screens for seconds
* **Poor interactivity** - Nothing clickable initially
* **High bounce** - Third of users leave

≈ **Reasons why:**
Code splitting, progressive rendering, and caching deliver instant data access users expect.

**User Value:** See data instantly

**Business Goal:** Reduce dashboard bounce rate

---

## ◈ Current State
- Initial load: 4-6 seconds
- Interactive: 8 seconds
- Bounce rate: 35%

---

## ◆ Target State
- Initial load: <1 second
- Interactive: <2 seconds
- Bounce rate: <20%

---

## ◇ Requirements

**◊** Frontend
— Bundle
• Code splitting
• Tree shaking
• CDN distribution
— Loading
• Progressive render
• Critical CSS inline
• Lazy load below-fold

**◊** Backend
— API
• Query optimization
• Response caching
— Data
• Pagination
• Partial responses

---

## ✦ Success Criteria
- Initial paint <1s
- Interactive <2s
- Lighthouse >90
- Bounce rate reduced

---

## ✓ Resolution Checklist

### Analysis
[ ] Profile bottlenecks
[ ] Set performance budget

### Frontend
[ ] Implement splitting
[ ] Add service worker

### Backend
[ ] Optimize queries
[ ] Implement caching

### Validation
[ ] Run performance tests
[ ] A/B test changes

---

## Labels
`[App]-App`, `performance`, `optimization`
```

---

## 6. 🎨 PARTIAL INPUT EXAMPLES

### Example: Technical List Enhancement

**User Input:**
```
Add filters:
- Category
- Date
- Price
- Status
```

**Enhanced to Standard:**
```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

# ■ About

Users need search control but scroll through unfiltered results.

⚠️ **Key problems:**
* **No filtering** - Can't narrow by category, date, price, status
* **Poor relevance** - Irrelevant results dominate
* **Lost conversions** - Users give up

≈ **Reasons why:**
Essential filters with real-time updates help users find exactly what they need quickly.

**User Value:** Find products faster with filtering

**Business Goal:** Increase conversion through better search

---

## ◇ Requirements

**◊** Filter Implementation
— Extracted
• Category multi-select
• Date range picker
• Price min/max
• Status checkboxes
— Inferred
• Active filter count
• Clear all option
• Instant updates
• Mobile responsive

**Needs:**
- Design mockups
- Status options
- Price boundaries

---

## ✦ Success Criteria
- All filters work
- Results update quickly
- Mobile compatible
- Filters combine properly

---

## ✓ Resolution Checklist

### Foundation
[ ] Build filter components
[ ] Set up state management

### Implementation
[ ] Connect to search API
[ ] Add URL sync

### Testing
[ ] Verify combinations
[ ] Check performance

---

## Labels
`[App]-App`, `UI`, `Search`, `feature`
```

---

## 7. 🎯 FEATURE TYPE PATTERNS

### Authentication Features

**◊** Security
— Password Rules
• 8+ characters
• Mixed case
• Special characters
— Session
• Token expiration
• Refresh logic
• Multi-device

**◊** Experience
— Login
• Remember me
• Social login
• 2FA/Biometric
— Recovery
• Password reset
• Security questions
• Recovery flow

### Search Features

**◊** Functionality
— Core
• Search as type
• Autocomplete
• Search history
— Advanced
• Boolean operators
• Fuzzy matching
• Synonyms

**◊** Results
— Display
• Sort options
• Results per page
• Infinite scroll
— Performance
• Response targets
• Caching strategy
• Query optimization

---

## 8. 💻 SPEC MODE EXAMPLES

### Example: Hide Scrollbar (Instant)

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A

User: $spec hide scrollbar

System: Browser compatibility needed?

User: yes

---

# Hidden Scrollbar Implementation

## Objective
Hide scrollbar while maintaining scroll.

## Implementation
```css
.scrollable-container {
  overflow-y: auto;
  scrollbar-width: none; /* Firefox */
  -ms-overflow-style: none; /* IE/Edge */
}

.scrollable-container::-webkit-scrollbar {
  display: none; /* Chrome/Safari/Edge */
}
```

## Browser Compatibility
- **Chrome/Edge**: ✓ `::-webkit-scrollbar`
- **Firefox**: ✓ `scrollbar-width: none`
- **Safari**: ✓ `::-webkit-scrollbar`
- **IE 10+**: ✓ `-ms-overflow-style: none`

## Key Points
- Pure CSS solution
- No JavaScript required
- Scroll preserved
```

### Example: Virtual Scroll Table

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A

User: $spec virtual scroll table

System: Quick setup:
1. Row count?
2. React/Vue?

User: 50k, React

---

# Virtual Scroll Table

## Objective
Efficiently render 50k rows without performance issues.

## Implementation
```typescript
import { FixedSizeList } from 'react-window';

export const VirtualTable = ({ data, rowHeight = 40 }) => {
  const Row = ({ index, style }) => (
    <div style={style} className="table-row">
      {Object.values(data[index]).map((val, i) => (
        <span key={i} className="cell">{val}</span>
      ))}
    </div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={data.length}
      itemSize={rowHeight}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
};
```

## Usage
```typescript
<VirtualTable data={largeDataset} />
```

## Key Points
- Only renders visible rows
- Smooth scrolling 50k+ items
- Add React.memo() for optimization
```

---

## Version History

- **v4.2.0**: First heading now "About", all examples 20% more concise
- **v4.1.0**: Updated formatting distinctions
- **v4.0.0**: Complex mode combines approaches, Spec mode concise

---

*All examples reference templates from Templates & Standards.md.*