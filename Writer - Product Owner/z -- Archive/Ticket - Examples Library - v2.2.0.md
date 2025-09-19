# Ticket - Examples Library - v2.2.0

Categorized examples showing real-world ticket implementations with developer-first clarity.

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

# ❖ [BE] Profile Picture Upload

Users need the ability to personalize their profiles but currently can only use generic placeholder images.

⚠︎ **Key problems:**
* **Low engagement** - Profiles feel impersonal and generic
* **Support tickets** - Weekly requests asking how to add profile pictures
* **Competitive disadvantage** - All major competitors offer this basic functionality

⁉ **Reasons why:**
By implementing profile picture upload with automatic image processing, we'll increase user engagement and profile completion rates while reducing support burden.

**User Value:** Personalize your account with a profile photo

**Business Goal:** Significantly increase profile completion rate

---

## ◇ Requirements
- Upload image from device
- Basic image cropping
- Replace existing photo
- Support JPG/PNG formats
- Reasonable file size limit
- Automatic thumbnail generation

---

## ✦ Success Criteria
- Images upload successfully
- File size limit properly enforced
- Photo displays immediately
- Thumbnails generated within seconds

---

## ✓ Resolution Checklist

### Implementation
[ ] Build upload handler with validation
[ ] Configure S3 and image processing

### Testing
[ ] Verify across devices and formats
[ ] Validate file size limits

---

## Labels
`Backend-System`, `API`, `feature`, `User-Management`
```

**Template Used:** → Ticket - Templates & Standards.md#improvement-template

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

**Enhanced to Standard Ticket:**
```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

### ❖ [FE] Search Filter Enhancement

Users need more control over search results but currently must scroll through hundreds of unfiltered results.

⚠︎ **Key problems/changes:**
* **No filtering options** - Users can't narrow results by category, date, price, or status
* **Poor relevance** - Irrelevant results dominate the list
* **User frustration** - Leading to search abandonment
* **Lost conversions** - Users give up before finding what they need

⁉ **Reasons why:**
By adding these essential filter types with real-time updates, users will find exactly what they need quickly, increasing conversion rates and reducing support tickets.

**User Value:** Find products faster with advanced filtering

**Business Goal:** Increase conversion rate by improving search

---

## ◇ Requirements

**◊** Filter Implementation
— Extracted from request
• Category filter with multi-select
• Date range picker
• Price range with min/max
• Status checkboxes

— Inferred additions
• Show active filter count
• Clear all filters option
• Results update instantly
• Mobile-responsive design

**Needs:**
- Design mockups for filter UI
- Specific status options
- Price range boundaries

---

## ✦ Success Criteria
- All filters work correctly
- Results update quickly
- Works on mobile devices
- Filters combine properly

---

## ✓ Resolution Checklist

### Foundation
[ ] Build filter components
[ ] Set up state management

### Implementation
[ ] Connect to search API
[ ] Add URL synchronization
[ ] Implement mobile layout

### Testing
[ ] Verify all filter combinations
[ ] Check performance and compatibility

---

## Labels
`[App]-App`, `UI`, `Search`, `feature`
```

**Pattern:** Extract obvious requirements, mark inferences, flag gaps

---

## 7. 🎯 FEATURE TYPE PATTERNS

### Authentication Features

Common requirements to consider:

**◊** Security Requirements
— Password Rules
• Minimum 8 characters
• Mix of upper/lowercase
• Special characters required
• Password history check
— Session Management
• Token expiration
• Refresh token logic
• Multi-device handling
• Force logout capability

**◊** User Experience
— Login Flow
• Remember me option
• Social login providers
• Two-factor authentication
• Biometric support
— Recovery Options
• Password reset email
• Security questions
• Account recovery flow
• Temporary access codes

### Search Features

Common requirements to consider:

**◊** Search Functionality
— Core Features
• Search as you type
• Autocomplete suggestions
• Search history
• Recent searches
— Advanced Options
• Boolean operators
• Wildcard support
• Fuzzy matching
• Synonym handling

**◊** Results Management
— Display Options
• Sort by relevance/date/price
• Results per page
• Infinite scroll vs pagination
• Quick preview
— Performance
• Response time targets
• Caching strategy
• Index optimization
• Query optimization

---

## 8. 💻 SPEC MODE EXAMPLES

### Example: Hide Scrollbar (CSS - Instant)

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A (Minimal conversation)

User: $spec hide scrollbar

System: Browser compatibility needed?

User: yes

---

# Hidden Scrollbar Implementation

## Objective
Hide scrollbar while maintaining scroll functionality.

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
- Scroll functionality preserved
```

### Example: Virtual Scroll Table (Component - 2 Questions)

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A (Minimal conversation)

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

interface Props {
  data: Array<{ id: string; [key: string]: any }>;
  rowHeight?: number;
}

export const VirtualTable = ({ data, rowHeight = 40 }: Props) => {
  const Row = ({ index, style }: any) => (
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
<VirtualTable data={largeDataset} rowHeight={40} />
```

## Key Points
- Only renders visible rows
- Smooth scrolling for 50k+ items
- Adjustable row height
- Add React.memo() for row optimization
```

---

## Version History

- **v2.2.0**: Updated formatting - Success Criteria (bullets only), Resolution Checklist (checkboxes only)
- **v2.1.0**: All examples updated with global Resolution Checklist approach (max 3 items per section, outcome-focused)
- **v2.0.0**: Complex mode combines phased and child ticket approaches, Spec mode now concise with minimal conversation
- **v1.0.0**: Initial examples library

---

*All examples reference templates from Ticket - Templates & Standards.md.* & Standards.md#quick-mode

---

## 2. 📋 STANDARD MODE EXAMPLES

### Example: Advanced Search Filters (With Interactive Offer)

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

# ❖ [FE] Advanced Search Filters

Our search functionality is failing to meet user needs, resulting in lost revenue and frustrated customers.

⚠︎ **Key problems:**
* **High abandonment rate** - Majority of users give up before finding what they need
* **Multiple search attempts** - Users repeatedly refine queries without success
* **Top support complaint** - "Can't find products" is our most common ticket
* **Lost revenue** - Substantial annual revenue loss from failed product discovery

⁉ **Reasons why:**
By implementing powerful filtering capabilities for category, price, availability, and date ranges, we'll help users find exactly what they need quickly, dramatically reducing search abandonment and increasing conversion rates.

**User Value:** Find exactly what you need with powerful filtering options

**Business Goal:** Dramatically reduce search abandonment rate

---

## ◇ Requirements

**◊** Filter Panel
— UI Components
• Category dropdown with multi-select
• Date range picker with calendar
• Price range slider with inputs
• Status checkboxes
— Behavior
• Results update instantly (debounced)
• Show active filter count badge
• Clear all filters button
• Filters persist in session storage

**◊** Mobile Experience
— Layout
• Bottom sheet pattern
• Sticky apply button
• Collapsible sections
— Interactions
• Swipe to dismiss
• Tap outside to close
• Smooth animations

---

## → Designs & References
- [Figma - Filter Panel Desktop](link)
- [Figma - Mobile Bottom Sheet](link)

**Notice:** Mobile uses bottom sheet pattern for better accessibility

---

## ✦ Success Criteria
- Results update quickly
- All filter combinations work correctly
- Filter state persists on back navigation
- Mobile gesture support works smoothly

---

## ✓ Resolution Checklist

### Foundation
[ ] Build filter components and state management
[ ] Connect to search API with URL sync

### Core Features
[ ] Implement all filter types
[ ] Add mobile bottom sheet
[ ] Apply animations and transitions

### Testing & Polish
[ ] Complete cross-browser testing
[ ] Verify performance targets
[ ] Conduct accessibility review

### Documentation
[ ] Update component library docs
[ ] Create usage guidelines

---

## ⊗ Dependencies
- Requires: Search API v2 (#2234)
- Blocks: Saved searches (#2240)

---

## Labels
`[App]-App`, `UI`, `Search`, `Discovery`, `feature`
```

**Template Used:** → Ticket - Templates & Standards.md#standard-mode

---

## 3. 🔧 COMPLEX MODE EXAMPLES

### Example: Real-time Collaboration (Option A: Phased)

```markdown
MODE: $c
TICKET TYPE: Complex
MCP USED: Cascade Thinking
INTERACTIVE OFFERED: Yes - Accepted

---

# ❖ [FS] Multi-user Document Editing

Real-time collaboration has become a critical requirement for our platform as teams increasingly work remotely and asynchronously.

⚠︎ **Key problems:**
* **Version conflicts** - Majority of shared documents experience merge conflicts requiring manual resolution
* **Lost work** - Users report losing hours weekly due to overwrites
* **Workflow delays** - Teams wait substantial time for document handoffs
* **Competitive pressure** - Losing enterprise deals to competitors with real-time features
* **No audit trail** - Can't track who changed what and when

⁉ **Reasons why:**
This comprehensive implementation will transform our document system with Google Docs-level collaboration capabilities while maintaining enterprise security standards. Through WebSocket infrastructure, Operational Transformation algorithms, and intelligent conflict resolution, we'll eliminate version conflicts and enable seamless team collaboration.

---

# ⌘ About

Enable teams to collaborate on documents in real-time, seeing each other's changes instantly. This positions us competitively with Google Docs while maintaining our security standards.

**User Value:** Work together on documents without version conflicts

**Business Goal:** Increase team plan adoption by 40%

---

[[*TOC*]]

---

## → Designs & References

### ◻︎ Editor Experience
- [Figma - Cursor States](link)
- [Figma - User Presence](link)
- [Figma - Conflict Resolution](link)

### ◻︎ Technical Specs
- [WebSocket Architecture](link)
- [OT Algorithm Docs](link)

**Notice:** Maximum 10 concurrent editors per document

---

## ◇ Implementation Approach

### Option A: Phased Development

#### Phase 1: Foundation (Week 1-2)

**◊** WebSocket Infrastructure
— Server Setup
• WebSocket server configuration
• Connection pooling
• Load balancing setup
• SSL/TLS implementation
— Client Integration
• WebSocket client library
• Reconnection logic
• Connection state management
• Error handling

**◊** User Presence System
— Backend
• User session tracking
• Presence broadcasts
• Heartbeat mechanism
• Cleanup on disconnect
— Frontend
• Presence indicators
• User avatars/colors
• Active user list
• Connection status

#### Phase 2: Core Editing (Week 3-4)

**◊** Operational Transformation
— Algorithm Implementation
• Text operation types
• Transform functions
• Operation composition
• Convergence guarantee
— Integration
• Document state management
• Operation queue
• Conflict resolution
• History tracking

**◊** Multi-cursor Display
— Cursor Tracking
• Position calculation
• Selection ranges
• Cursor broadcasting
• Smooth animations
— Visual Rendering
• Cursor colors
• User labels
• Selection highlights
• Focus indicators

#### Phase 3: Polish & Scale (Week 5-6)

**◊** Performance Optimization
— Message Optimization
• Batch operations
• Compression
• Delta encoding  
• Throttling

**◊** Advanced Features
— Offline Support
• Local operation queue
• Sync on reconnect
• Status indicators

---

## ✦ Success Criteria
- Cursor updates have minimal latency
- Support 10 concurrent editors
- Extremely high uptime for sync service
- Offline changes sync seamlessly
- Zero data loss in conflicts

---

## ✓ Resolution Checklist

### Phase 1: Foundation
[ ] Set up WebSocket infrastructure
[ ] Implement presence system
[ ] Complete connection management

### Phase 2: Core Features
[ ] Implement OT algorithm
[ ] Build cursor tracking system
[ ] Add conflict resolution

### Phase 3: Production Ready
[ ] Optimize performance and caching
[ ] Add monitoring and admin tools
[ ] Complete security audit

### Testing & Validation
[ ] Load test with 10+ users
[ ] Verify failover scenarios
[ ] Complete integration testing

### Documentation & Training
[ ] Document API and architecture
[ ] Create team training materials
[ ] Update user guides

### Launch Preparation
[ ] Performance benchmarks met
[ ] Rollback strategy ready
[ ] Go-live checklist complete

---

## ⊗ Dependencies
- Requires: WebSocket infrastructure (#5001)
- Requires: Document versioning (#5002)
- Blocks: Enterprise features (#5050)

---

## ⚠ Risks
- **Scale:** WebSocket costs at high concurrency
- **Complexity:** OT algorithm edge cases
- **Browser:** Older browser compatibility

---

## Labels
`Backend-System`, `[App]-App`, `WebSocket`, `Real-time`, `feature`
```

**Template Used:** → Ticket - Templates & Standards.md#complex-mode

---

## 4. 🐛 BUG TICKET EXAMPLES

### Example: Search Results Reset Bug

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Declined

---

# ❖ [FE] Bug: Search Filters Reset on Back Navigation

A critical user experience bug is severely impacting our search functionality and causing measurable business harm.

⚠︎ **Key problems:**
* **All users affected** - Every user who applies filters loses their selection on back navigation
* **High abandonment** - Nearly one in four users leave after encountering this bug
* **Support volume** - Hundreds of complaints this month about "broken search"
* **Revenue loss** - Substantial monthly revenue impact from frustrated users

⁉ **Reasons why:**
Fixing this bug will restore expected browser behavior, eliminate a major source of user frustration, and recover lost revenue from abandoned sessions.

**User Value:** Keep your selected filters when returning to search

**Business Goal:** Eliminate user frustration and dramatically reduce abandonment rate

---

## ◆ Current Behavior
1. User applies multiple filters
2. User clicks on search result
3. User clicks browser back
4. **Bug:** All filters are cleared

---

## ✦ Desired Behavior
- Filters persist on back navigation
- Selected filters remain visible
- Results show filtered state
- URL reflects filter state

---

## ◈ Steps to Reproduce
1. Go to search page
2. Apply category + date filters
3. Click any result
4. Click browser back button
5. Observe filters are reset

---

## → Evidence
- [Video - Bug Behavior](link)
- [Screenshot - Console Error](link)

**Notice:** Worked correctly before v2.3.0

---

## ✦ Success Criteria
- Filters persist every time without fail
- Works in all major browsers
- No performance impact
- URL parameters maintained

---

## ✓ Resolution Checklist

### Investigation
[ ] Reproduce and identify root cause
[ ] Review v2.3.0 changes

### Implementation
[ ] Fix state management and history handling
[ ] Add session storage backup

### Verification
[ ] Test all filter types and browsers
[ ] Add regression tests

---

## ⊗ Dependencies
- Related: URL structure update (#1454)
- Blocks: Search analytics (#1455)

---

## Labels
`[App]-App`, `UI`, `bug`, `Search`
```

**Template Used:** → Ticket - Templates & Standards.md#bug-template

---

## 5. 📈 IMPROVEMENT EXAMPLES

### Example: Dashboard Performance

```markdown
MODE: $s
TICKET TYPE: Improvement
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: Yes - Accepted

---

# ❖ [FE] Improvement: Dashboard Load Time Optimization

Our analytics dashboard has become a critical pain point that's driving users away and damaging our reputation.

⚠︎ **Key problems:**
* **Extremely slow initial load** - Users stare at blank screens for many seconds
* **Poor interactivity** - Nothing clickable for additional seconds after content appears
* **High bounce rate** - Over one-third of users leave before page loads
* **Mobile performance** - Load times exceed acceptable thresholds on average connections

⁉ **Reasons why:**
By implementing code splitting, progressive rendering, smart caching, and API optimization, we'll deliver instant data access that users expect, saving our product's reputation and retaining customers.

**User Value:** See your data instantly without waiting

**Business Goal:** Dramatically reduce dashboard bounce rate

---

## ◈ Current State
- Initial load: 4-6 seconds
- Time to interactive: 8 seconds
- Bounce rate: 35%
- User complaints about speed

---

## ◆ Target State
- Initial load: <1 second
- Time to interactive: <2 seconds
- Bounce rate: <20%
- Core Web Vitals: all green

---

## ◇ Requirements

**◊** Frontend Optimization
— Bundle Size
• Code splitting by route
• Tree shaking unused code
• Minification and compression
• CDN distribution
— Loading Strategy
• Progressive rendering
• Critical CSS inline
• Lazy load below-fold
• Preload key resources

**◊** Backend Optimization
— API Performance
• Query optimization
• Response caching
• Database indexing
• Connection pooling
— Data Strategy
• Pagination implementation
• Partial responses
• GraphQL for specific fields
• Batch requests

---

## → Designs & References
- [Figma - Loading States](link)
- [Performance Audit Report](link)

---

## ✦ Success Criteria
- Initial paint under 1 second
- Interactive in under 2 seconds
- Lighthouse score above 90
- Substantial bounce rate reduction

---

## ✓ Resolution Checklist

### Analysis & Planning
[ ] Profile performance bottlenecks
[ ] Set performance budget

### Frontend Optimization
[ ] Implement code splitting and lazy loading
[ ] Add service worker and compression

### Backend Optimization
[ ] Optimize queries and add caching
[ ] Implement pagination and batching

### Validation & Monitoring
[ ] Run performance tests
[ ] A/B test changes
[ ] Set up monitoring

---

## Labels
`[App]-App`, `performance`, `optimization`, `UI`
```

**Template Used:** → Ticket - Templates