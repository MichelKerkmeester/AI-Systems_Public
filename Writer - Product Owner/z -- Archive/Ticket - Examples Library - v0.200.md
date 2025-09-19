# Ticket - Examples Library - v0.200

Categorized examples showing real-world ticket implementations with developer-first clarity. All examples reference templates from Ticket - Templates & Standards.md.

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

## ✓ Success Criteria
- [ ] Images upload successfully
- [ ] File size limit properly enforced
- [ ] Photo displays immediately
- [ ] Thumbnails generated within seconds

---

## ✓ Resolution Checklist
- [ ] Implement file upload handler
- [ ] Add image validation
- [ ] Configure S3 integration
- [ ] Set up image processing
- [ ] Test on mobile devices
- [ ] Update user profile API

---

## Labels
`Backend-System`, `API`, `feature`, `User-Management`
```

**Template Used:** → Ticket - Templates & Standards.md#quick-mode

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

## ✓ Success Criteria
- [ ] Results update quickly
- [ ] All filter combinations work correctly
- [ ] Filter state persists on back navigation
- [ ] Mobile gesture support works smoothly

---

## ✓ Resolution Checklist

### Implementation
- [ ] Build filter components
- [ ] Implement filter logic
- [ ] Connect to search API
- [ ] Add URL parameter sync

### Testing & QA
- [ ] Test filter combinations
- [ ] Verify performance targets
- [ ] Cross-browser testing
- [ ] Mobile gesture testing

### Polish
- [ ] Add loading states
- [ ] Implement animations
- [ ] Accessibility review

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

## ✓ Success Criteria
- [ ] Cursor updates have minimal latency
- [ ] Support 10 concurrent editors
- [ ] Extremely high uptime for sync service
- [ ] Offline changes sync seamlessly
- [ ] Zero data loss in conflicts

---

## ✓ Resolution Checklist

### Phase 1: Foundation
- [ ] Set up WebSocket server
- [ ] Implement connection manager
- [ ] Create presence system
- [ ] Add heartbeat mechanism
- [ ] Build reconnection logic
- [ ] Test with 5 users

### Phase 2: Core Features
- [ ] Implement OT algorithm
- [ ] Build cursor tracking
- [ ] Add selection sync
- [ ] Create conflict resolver
- [ ] Implement change history
- [ ] Load test with 10 users

### Phase 3: Production Ready
- [ ] Optimize message size
- [ ] Add compression
- [ ] Implement caching
- [ ] Set up monitoring
- [ ] Create admin tools
- [ ] Document API

### Launch Preparation
- [ ] Security audit complete
- [ ] Performance benchmarks met
- [ ] Failover tested
- [ ] Team training done

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

## ✓ Desired Behavior
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

**Notice:** Worked correctly before v0.230

---

## ✓ Success Criteria
- [ ] Filters persist every time without fail
- [ ] Works in all major browsers
- [ ] No performance impact
- [ ] URL parameters maintained

---

## ✓ Resolution Checklist

### Investigation
- [ ] Reproduce in dev environment
- [ ] Check browser history API
- [ ] Review v0.230 changes
- [ ] Identify root cause

### Implementation
- [ ] Fix state management
- [ ] Update history handling
- [ ] Preserve URL parameters
- [ ] Add session storage backup

### Verification
- [ ] Test all filter types
- [ ] Verify on mobile browsers
- [ ] Check back/forward nav
- [ ] Add regression tests

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

## ✓ Success Criteria
- [ ] Initial paint under 1 second
- [ ] Interactive in under 2 seconds
- [ ] Lighthouse score above 90
- [ ] Substantial bounce rate reduction

---

## ✓ Resolution Checklist

### Analysis
- [ ] Profile current performance
- [ ] Identify bottlenecks
- [ ] Set performance budget
- [ ] Create metrics dashboard

### Implementation
- [ ] Split code by route
- [ ] Implement lazy loading
- [ ] Add service worker
- [ ] Optimize images
- [ ] Enable compression

### Validation
- [ ] Run performance tests
- [ ] Check all metrics
- [ ] A/B test changes
- [ ] Monitor for regressions

---

## Labels
`[App]-App`, `performance`, `optimization`, `UI`
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

## ✓ Success Criteria
- [ ] All filters work correctly
- [ ] Results update quickly
- [ ] Works on mobile devices
- [ ] Filters combine properly

---

## ✓ Resolution Checklist

### Implementation
- [ ] Build filter components
- [ ] Connect to search API
- [ ] Add state management
- [ ] Implement URL sync

### Testing
- [ ] Test filter combinations
- [ ] Verify mobile layout
- [ ] Check performance
- [ ] Browser compatibility

---

## Labels
`[App]-App`, `UI`, `Search`, `feature`
```

**Pattern:** Extract obvious requirements, mark inferences, flag gaps

### Example: Implementation Request

**User Input:**
```
how to hide scrollbar on right container but keep it scrollable
```

**System Response:**
```
This sounds like you need a frontend implementation spec. Let me create that for you with $spec mode.

$spec hide scrollbar on container
[Proceeds with minimal spec conversation]
```

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

### Dashboard Features

Common requirements to consider:

**◊** Data Display
— Widgets
• Metric cards
• Charts and graphs
• Data tables
• Activity feeds
— Customization
• Widget arrangement
• Show/hide options
• Size adjustments
• Theme selection

**◊** Interactivity
— User Actions
• Refresh data
• Export options
• Drill-down capability
• Time range selection
— Real-time Features
• Auto-refresh intervals
• Live data indicators
• Push notifications
• Change highlights

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

User: 50k rows, React

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

### Example: Debounced Search (Utility - 1 Question)

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A (Minimal conversation)

User: $spec debounced search input

System: React or Vanilla JS?

User: React

---

# Debounced Search Input

## Objective
Prevent excessive API calls while typing.

## Implementation
```typescript
import { useState, useCallback, useEffect } from 'react';

export const DebouncedSearch = ({ onSearch, delay = 300 }) => {
  const [query, setQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedQuery(query);
    }, delay);

    return () => clearTimeout(timer);
  }, [query, delay]);

  useEffect(() => {
    if (debouncedQuery) {
      onSearch(debouncedQuery);
    }
  }, [debouncedQuery, onSearch]);

  return (
    <input
      type="text"
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Search..."
    />
  );
};
```

## Key Points
- 300ms default delay
- Cancels pending calls on new input
- Only triggers after user stops typing
```

### Example: Responsive Grid (Complex - 3 Questions)

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A (Minimal conversation)

User: $spec responsive grid layout

System: Quick setup:
1. CSS Grid or Flexbox?
2. How many columns max?
3. Need gap control?

User: Grid, 4 columns, yes

---

# Responsive Grid Layout

## Objective
Create responsive grid: 4 columns desktop, 2 tablet, 1 mobile.

## Implementation
```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--gap, 20px);
  padding: 20px;
}

/* Explicit breakpoints for precise control */
@media (min-width: 1200px) {
  .grid-container {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (min-width: 768px) and (max-width: 1199px) {
  .grid-container {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}

.grid-item {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
}
```

## Usage
```html
<div class="grid-container" style="--gap: 24px;">
  <div class="grid-item">Item 1</div>
  <div class="grid-item">Item 2</div>
  <!-- More items -->
</div>
```

## Key Points
- Auto-fit with 250px minimum
- CSS custom property for gap
- Clean breakpoint control
- No JavaScript needed
```

### Example: API Error Handler (Utility - 2 Questions)

```markdown
MODE: $spec
TYPE: Frontend Implementation
MCP USED: Sequential Thinking
INTERACTIVE OFFERED: N/A (Minimal conversation)

User: $spec API error handling

System: Quick setup:
1. React/Vue/Vanilla?
2. Toast notifications or inline?

User: React, toast

---

# API Error Handler

## Objective
Consistent error handling with user-friendly messages.

## Implementation
```typescript
// Error handler hook
import { useState } from 'react';
import { toast } from 'react-toastify'; // or your toast library

const errorMessages: Record<number, string> = {
  400: 'Invalid request. Please check your input.',
  401: 'Please log in to continue.',
  403: 'You don\'t have permission to do this.',
  404: 'Resource not found.',
  429: 'Too many requests. Please wait.',
  500: 'Server error. Please try again.',
  503: 'Service temporarily unavailable.'
};

export const useApiCall = () => {
  const [loading, setLoading] = useState(false);

  const callApi = async (url: string, options?: RequestInit) => {
    setLoading(true);
    try {
      const response = await fetch(url, options);
      
      if (!response.ok) {
        const message = errorMessages[response.status] || 
                       'An unexpected error occurred.';
        toast.error(message);
        throw new Error(message);
      }
      
      return await response.json();
    } catch (error) {
      if (error instanceof TypeError) {
        toast.error('Network error. Check your connection.');
      }
      throw error;
    } finally {
      setLoading(false);
    }
  };

  return { callApi, loading };
};
```

## Usage
```typescript
const { callApi, loading } = useApiCall();

const fetchData = async () => {
  try {
    const data = await callApi('/api/users');
    // Handle success
  } catch (error) {
    // Already toasted, just handle UI state
  }
};
```

## Key Points
- User-friendly error messages
- Automatic loading state
- Network error detection
- Reusable across components
```

**Template Used:** → Ticket - Templates & Standards.md#spec-mode

---

*All examples reference templates from Ticket - Templates & Standards.md. Version 2.0.0 updates: Complex mode combines phased and child ticket approaches, Spec mode now concise with minimal conversation (1-3 questions max), focused on copy-paste ready implementations.*