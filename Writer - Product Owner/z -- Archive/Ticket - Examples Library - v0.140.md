# Ticket - Examples Library - v0.140

Categorized examples showing real-world ticket implementations with developer-first clarity, including scope prefixes, comprehensive descriptions, and updated structure. All examples reference templates from Ticket - Templates & Standards.md.

## Table of Contents

1. [🚀 QUICK MODE EXAMPLES](#1--quick-mode-examples)
2. [📋 STANDARD MODE EXAMPLES](#2--standard-mode-examples)
3. [🔧 COMPLEX MODE EXAMPLES](#3--complex-mode-examples)
4. [🚀 EPIC MODE EXAMPLES](#4--epic-mode-examples)
5. [🐛 BUG TICKET EXAMPLES](#5--bug-ticket-examples)
6. [📈 IMPROVEMENT EXAMPLES](#6--improvement-examples)
7. [🎨 PARTIAL INPUT EXAMPLES](#7--partial-input-examples)
8. [🎯 FEATURE TYPE PATTERNS](#8--feature-type-patterns)
9. [🔧 SPEC MODE EXAMPLES](#9--spec-mode-examples)

---

## 1. 🚀 QUICK MODE EXAMPLES

### Example: Profile Picture Upload

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking

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

### Example: Advanced Search Filters

```markdown
MODE: $s
TICKET TYPE: Feature
MCP USED: Sequential Thinking

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
* Category dropdown with multi-select
* Date range picker with calendar
* Price range slider with inputs
* Status checkboxes
— Behavior
* Results update instantly (debounced)
* Show active filter count badge
* Clear all filters button
* Filters persist in session storage

**◊** Mobile Experience
— Layout
* Bottom sheet pattern
* Sticky apply button
* Collapsible sections
— Interactions
* Swipe to dismiss
* Tap outside to close
* Smooth animations

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

### Example: Real-time Collaboration

```markdown
MODE: $c
TICKET TYPE: Feature
MCP USED: Cascade Thinking

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

## ◇ Phase 1: Foundation (Week 1-2)

**◊** WebSocket Infrastructure
— Server Setup
* WebSocket server configuration
* Connection pooling
* Load balancing setup
* SSL/TLS implementation
— Client Integration
* WebSocket client library
* Reconnection logic
* Connection state management
* Error handling

**◊** User Presence System
— Backend
* User session tracking
* Presence broadcasts
* Heartbeat mechanism
* Cleanup on disconnect
— Frontend
* Presence indicators
* User avatars/colors
* Active user list
* Connection status

---

## ◇ Phase 2: Core Editing (Week 3-4)

**◊** Operational Transformation
— Algorithm Implementation
* Text operation types
* Transform functions
* Operation composition
* Convergence guarantee
— Integration
* Document state management
* Operation queue
* Conflict resolution
* History tracking

**◊** Multi-cursor Display
— Cursor Tracking
* Position calculation
* Selection ranges
* Cursor broadcasting
* Smooth animations
— Visual Rendering
* Cursor colors
* User labels
* Selection highlights
* Focus indicators

---

## ◇ Phase 3: Polish & Scale (Week 5-6)

**◊** Performance Optimization
— Message Optimization
* Batch operations
* Compression
* Delta encoding  
* Throttling

**◊** Advanced Features
— Offline Support
* Local operation queue
* Sync on reconnect
* Status indicators

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

## 4. 🚀 EPIC MODE EXAMPLES

### Example: Mobile App Launch

```markdown
MODE: $e
TICKET TYPE: Epic
MCP USED: Cascade Thinking

---

# ❖ [Mobile] Epic: Native Mobile Applications

The mobile revolution has fundamentally shifted how users interact with digital services, and we're currently missing this critical market segment.

⚠︎ **Key problems:**
* **Majority of traffic** from mobile devices gets poor web experience
* **App store opportunity** - Users spend vast majority of time in apps vs web
* **Competitor advantage** - All top competitors have highly-rated mobile apps
* **Revenue impact** - Mobile apps show dramatically higher conversion rates
* **User retention** - Missing push notifications and native features

⁉ **Reasons why:**
This epic encompasses our complete mobile strategy from architecture through app store launches. Native iOS and Android applications will leverage platform capabilities for superior UX, capture significant mobile market share, and dramatically increase user retention through push notifications and offline functionality.

**User Value:** Access full platform features on iOS and Android

**Business Goal:** Capture substantial mobile market share

---

## ⌘ Overview
Launch native mobile apps with feature parity to web, optimized for mobile workflows and leveraging device capabilities for superior user experience.

---

## ✓ Success Metrics
- [ ] Achieve top-tier app store rating
- [ ] Majority of users actively use mobile app
- [ ] Fast app launch time
- [ ] Mobile represents significant portion of platform usage

---

## ◇ Child Tickets

### ◻︎ Phase 1: Core Infrastructure
- [ ] **[Mobile] App Architecture** - Foundation and navigation setup
- [ ] **[Mobile] Authentication** - Secure login with biometrics
- [ ] **[Mobile] Data Sync** - Offline-first architecture
- [ ] **[Mobile] Push Notifications** - System integration

### ◻︎ Phase 2: Feature Parity
- [ ] **[Mobile] Dashboard** - Key metrics view
- [ ] **[Mobile] Core Feature 1** - Primary workflow
- [ ] **[Mobile] Core Feature 2** - Secondary workflow
- [ ] **[Mobile] Search & Nav** - Mobile patterns

### ◻︎ Phase 3: Mobile Native
- [ ] **[Mobile] Camera Integration** - Document scanning
- [ ] **[Mobile] Location Services** - Context features
- [ ] **[Mobile] Share Extension** - System integration
- [ ] **[Mobile] Widgets** - Home screen widgets

---

## ✓ Resolution Checklist

### Epic Planning
- [ ] Create all child tickets
- [ ] Assign team leads
- [ ] Set up tracking dashboard
- [ ] Define success metrics

### Technical Foundation
- [ ] Choose tech stack
- [ ] Set up CI/CD
- [ ] Create test devices lab
- [ ] Establish code standards

### Go-to-Market
- [ ] App store optimization
- [ ] Beta testing program
- [ ] Marketing materials
- [ ] Support documentation

---

## ⊗ Dependencies
- Requires: Mobile API development (#7001)
- Requires: Design system mobile (#7002)

---

## ⌘ Timeline
20 weeks (5 weeks per phase)

---

## Labels
`Mobile-App`, `epic`
```

**Template Used:** → Ticket - Templates & Standards.md#epic-mode

---

## 5. 🐛 BUG TICKET EXAMPLES

### Example: Search Results Reset Bug

```markdown
MODE: $s
TICKET TYPE: Bug
MCP USED: Sequential Thinking

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

## 6. 📈 IMPROVEMENT EXAMPLES

### Example: Dashboard Performance

```markdown
MODE: $s
TICKET TYPE: Improvement
MCP USED: Sequential Thinking

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
* Code splitting by route
* Tree shaking unused code
* Minification and compression
* CDN distribution
— Loading Strategy
* Progressive rendering
* Critical CSS inline
* Lazy load below-fold
* Preload key resources

**◊** Backend Optimization
— API Performance
* Query optimization
* Response caching
* Database indexing
* Connection pooling
— Data Strategy
* Pagination implementation
* Partial responses
* GraphQL for specific fields
* Batch requests

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

## 7. 🎨 PARTIAL INPUT EXAMPLES

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
This sounds like you need an implementation spec rather than a development ticket. Would you like me to create a technical specification showing HOW to implement this?

If yes, I'll create a spec with:
- CSS code examples
- Browser compatibility notes  
- Testing checklist

Or would you prefer a standard ticket describing WHAT needs to be done?
```

---

## 8. 🎯 FEATURE TYPE PATTERNS

### Authentication Features

Common requirements to consider:

**◊** Security Requirements
— Password Rules
* Minimum 8 characters
* Mix of upper/lowercase
* Special characters required
* Password history check
— Session Management
* Token expiration
* Refresh token logic
* Multi-device handling
* Force logout capability

**◊** User Experience
— Login Flow
* Remember me option
* Social login providers
* Two-factor authentication
* Biometric support
— Recovery Options
* Password reset email
* Security questions
* Account recovery flow
* Temporary access codes

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

## 9. 🔧 SPEC MODE EXAMPLES

### Example: Scrollbar Visibility Implementation

```markdown
MODE: $spec
TYPE: Implementation Spec
MCP USED: Sequential Thinking

---

# Scrollbar Visibility Implementation Spec

## Objective
Implement a dual-container layout where the left container displays a visible scrollbar and the right container maintains scroll functionality with a hidden scrollbar.

## CSS Implementation

### 1. Base Container Styles
```css
/* Left Container - Visible Scrollbar */
.left-container {
  overflow-y: auto;
  /* Standard scrollbar remains visible */
}

/* Right Container - Hidden Scrollbar */
.right-container {
  overflow-y: auto;
  
  /* Firefox */
  scrollbar-width: none;
  
  /* IE 10+ and Legacy Edge */
  -ms-overflow-style: none;
}

/* Webkit Browsers (Chrome, Safari, Modern Edge) */
.right-container::-webkit-scrollbar {
  display: none;
}
```

### 2. HTML Structure
```html
<div class="container-wrapper">
  <div class="left-container">
    <!-- Content with visible scrollbar -->
  </div>
  <div class="right-container">
    <!-- Content with hidden scrollbar -->
  </div>
</div>
```

## Browser Compatibility
- **Chrome/Edge (Chromium)**: ✓ `::-webkit-scrollbar`
- **Firefox**: ✓ `scrollbar-width: none`
- **Safari**: ✓ `::-webkit-scrollbar`
- **IE 10+**: ✓ `-ms-overflow-style: none`

## Key Points
- Properties are scoped to specific selectors
- No impact on containers without these classes
- Scroll functionality preserved in both containers
- Zero JavaScript required
- Class names are examples - use your project's naming convention

## Testing Checklist
- [ ] Left container shows scrollbar when content overflows
- [ ] Right container scrolls without visible scrollbar
- [ ] Test in Chrome, Firefox, Safari, and Edge
- [ ] Verify touch/trackpad scrolling works in both containers
- [ ] Confirm keyboard navigation (arrow keys) functions properly
```

### Example: Responsive Grid Layout

```markdown
MODE: $spec
TYPE: Implementation Spec
MCP USED: Sequential Thinking

---

# Responsive Grid Layout Implementation Spec

## Objective
Create a responsive grid that displays 4 columns on desktop, 2 on tablet, and 1 on mobile, with automatic item wrapping and consistent spacing.

## CSS Grid Implementation

### 1. Grid Container
```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}

/* Optional: Max width for very large screens */
@media (min-width: 1400px) {
  .grid-container {
    grid-template-columns: repeat(4, 1fr);
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

### 2. Grid Items
```css
.grid-item {
  background: #f0f0f0;
  padding: 20px;
  border-radius: 8px;
  min-height: 200px;
  
  /* Ensure content doesn't overflow */
  overflow: hidden;
}
```

### 3. Alternative Flexbox Approach
```css
.flex-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
}

.flex-item {
  flex: 1 1 250px; /* Grow, shrink, basis */
  max-width: calc(25% - 15px); /* 4 columns minus gap */
  background: #f0f0f0;
  padding: 20px;
  border-radius: 8px;
}

@media (max-width: 1024px) {
  .flex-item {
    max-width: calc(50% - 10px); /* 2 columns */
  }
}

@media (max-width: 640px) {
  .flex-item {
    max-width: 100%; /* 1 column */
  }
}
```

## Browser Compatibility
- **CSS Grid**: All modern browsers (IE 11 with prefixes)
- **Flexbox**: All modern browsers including IE 11
- **Gap property**: Not supported in older Safari (use margins as fallback)

## Key Points
- Grid approach is cleaner and more flexible
- Flexbox has better legacy browser support
- `minmax()` creates truly responsive columns
- Gap property simplifies spacing management
- Consider container queries for component-based responsiveness

## Testing Checklist
- [ ] Verify 4 columns on desktop (>1024px)
- [ ] Verify 2 columns on tablet (768px-1024px)
- [ ] Verify 1 column on mobile (<768px)
- [ ] Test window resize for smooth transitions
- [ ] Check gap/spacing consistency
- [ ] Verify no horizontal scroll at any breakpoint
```

### Example: API Error Handling

```markdown
MODE: $spec
TYPE: Implementation Spec
MCP USED: Sequential Thinking

---

# API Error Handling Implementation Spec

## Objective
Implement consistent error handling for API responses with user-friendly messages, retry logic, and proper logging.

## JavaScript Implementation

### 1. Error Handler Utility
```javascript
class APIError extends Error {
  constructor(status, message, code) {
    super(message);
    this.status = status;
    this.code = code;
    this.name = 'APIError';
  }
}

const handleAPIError = (error) => {
  // Network errors
  if (!error.response) {
    return {
      message: 'Unable to connect. Please check your internet connection.',
      canRetry: true,
      code: 'NETWORK_ERROR'
    };
  }
  
  // Server errors by status code
  const status = error.response.status;
  const errorMap = {
    400: { message: 'Invalid request. Please check your input.', canRetry: false },
    401: { message: 'Please log in to continue.', canRetry: false },
    403: { message: 'You don\'t have permission to perform this action.', canRetry: false },
    404: { message: 'The requested resource was not found.', canRetry: false },
    429: { message: 'Too many requests. Please try again later.', canRetry: true },
    500: { message: 'Server error. Please try again.', canRetry: true },
    502: { message: 'Service temporarily unavailable.', canRetry: true },
    503: { message: 'Service under maintenance.', canRetry: true }
  };
  
  return errorMap[status] || {
    message: 'An unexpected error occurred.',
    canRetry: status >= 500
  };
};
```

### 2. Fetch Wrapper with Retry
```javascript
const fetchWithRetry = async (url, options = {}, maxRetries = 3) => {
  let lastError;
  
  for (let i = 0; i <= maxRetries; i++) {
    try {
      const response = await fetch(url, {
        ...options,
        signal: AbortSignal.timeout(30000) // 30s timeout
      });
      
      if (!response.ok) {
        throw new APIError(
          response.status,
          `HTTP ${response.status}`,
          response.statusText
        );
      }
      
      return await response.json();
    } catch (error) {
      lastError = error;
      
      // Don't retry on client errors (4xx)
      if (error.status && error.status < 500) {
        break;
      }
      
      // Exponential backoff
      if (i < maxRetries) {
        const delay = Math.min(1000 * Math.pow(2, i), 10000);
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }
  
  throw lastError;
};
```

### 3. React Hook Example
```javascript
const useAPICall = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const callAPI = useCallback(async (url, options) => {
    setLoading(true);
    setError(null);
    
    try {
      const data = await fetchWithRetry(url, options);
      return data;
    } catch (err) {
      const errorInfo = handleAPIError(err);
      setError(errorInfo);
      
      // Log to monitoring service
      console.error('API Error:', {
        url,
        status: err.status,
        message: err.message,
        timestamp: new Date().toISOString()
      });
      
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);
  
  return { callAPI, loading, error };
};
```

## Browser Compatibility
- **Fetch API**: All modern browsers (polyfill for IE)
- **AbortSignal.timeout**: Chrome 103+, Firefox 100+ (use AbortController for older)
- **Async/Await**: All modern browsers (transpile for older)

## Key Points
- Always provide user-friendly error messages
- Implement exponential backoff for retries
- Don't retry client errors (4xx status codes)
- Log errors for monitoring and debugging
- Consider implementing circuit breaker for repeated failures
- Handle network timeouts explicitly

## Testing Checklist
- [ ] Test network failure (offline mode)
- [ ] Test each HTTP error status code
- [ ] Verify retry logic with server errors
- [ ] Check exponential backoff timing
- [ ] Confirm error messages are user-friendly
- [ ] Verify errors are logged properly
- [ ] Test timeout handling
```

**Template Used:** → Ticket - Templates & Standards.md#spec-mode

---

*All examples reference templates from Ticket - Templates & Standards.md. Version 1.3.0 updates: 1-paragraph descriptions, "Desired Behavior" for bugs, removed Technical Details sections, added Spec Mode examples for implementation specifications.*