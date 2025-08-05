# Ticket - Examples Library - v1.3.0

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

---

## 1. 🚀 QUICK MODE EXAMPLES

### Example: Profile Picture Upload

```markdown
MODE: $q
TICKET TYPE: Feature
MCP USED: Sequential Thinking

---

# ❖ [BE] Profile Picture Upload

Users have been requesting the ability to personalize their profiles with custom avatars, as our current system only shows generic placeholder images. This creates several challenges: **Low engagement** - Profiles feel impersonal and users don't connect with the platform; **Support tickets** - We receive numerous requests weekly asking how to add profile pictures; **Competitive disadvantage** - All major competitors offer this basic functionality. By implementing a robust profile picture upload system with automatic image processing, we'll give users the personalization they expect while ensuring consistent image quality and reasonable storage costs across our platform.

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

Our search functionality is failing to meet user needs, resulting in significant business impact and user frustration. Current analytics reveal: **High search abandonment rate** - Majority of users give up before finding what they need; **Multiple search attempts** - Users repeatedly refine queries without success; **Top support complaint** - "Can't find products" represents our most common ticket type; **Lost revenue** - Substantial annual revenue loss from failed product discovery. The root cause is our basic keyword search that returns hundreds of irrelevant results. Users need powerful filtering capabilities to narrow results by category, price, availability, date ranges, and custom attributes. This implementation will provide: **Desktop experience** - Sidebar filter panel with instant results updating; **Mobile experience** - Bottom sheet pattern optimized for touch interaction; **Performance focus** - Fast response times with smart caching; **Accessibility** - Full keyboard navigation and screen reader support.

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

Real-time collaboration has become a critical requirement for our platform as teams increasingly work remotely and asynchronously. Our current file-based sharing system creates significant friction: **Version conflicts** - Majority of shared documents experience merge conflicts requiring manual resolution; **Lost work** - Users report losing significant work time weekly due to overwrites; **Workflow delays** - Teams experience substantial wait times for document handoffs; **Competitive pressure** - We're losing enterprise deals to competitors with real-time features. This comprehensive implementation will transform our document system with Google Docs-level collaboration capabilities while maintaining our enterprise security standards. Technical Approach: **WebSocket infrastructure** for minimal latency updates across all users; **Operational Transformation** algorithms ensuring mathematical convergence of all edits; **Intelligent conflict resolution** that preserves intent from all collaborators; **Offline support** with automatic sync when connection restored. Key Differentiators: **Enterprise security** - All data encrypted in transit and at rest; **Audit trail** - Complete history of who changed what and when; **Performance at scale** - Support 10 concurrent editors without degradation; **No data loss guarantee** - Every keystroke saved and recoverable. The implementation will be delivered in three phases over 6 weeks, starting with basic presence awareness and culminating in full offline support with conflict resolution.

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

The mobile revolution has fundamentally shifted how users interact with digital services, and we're currently missing out on this critical market segment. Market Reality: **Majority of traffic** comes from mobile devices, but our web experience delivers poor mobile UX; **App store opportunity** - Users spend vast majority of mobile time in apps vs. mobile web; **Competitor advantage** - Top competitors all have highly-rated mobile apps; **Revenue impact** - Mobile apps show dramatically higher conversion rates than mobile web. Strategic Imperatives: **User retention** - Push notifications significantly increase retention; **Brand presence** - App icon on home screen ensures daily brand visibility; **Native capabilities** - Biometrics, offline mode, camera integration enhance UX; **Performance gains** - Native apps deliver substantially faster interactions than web. This epic encompasses our complete mobile strategy, from initial architecture decisions through successful app store launches. We'll build native iOS and Android applications that not only match our web functionality but leverage platform-specific capabilities to deliver superior mobile experiences. Phased Approach: 1. **Foundation (Weeks 1-5)** - Core infrastructure, authentication, data sync; 2. **Feature Parity (Weeks 6-10)** - Implement all critical web features; 3. **Mobile Native (Weeks 11-15)** - Platform-specific enhancements; 4. **Launch (Weeks 16-20)** - Beta testing, marketing, app store optimization. Success requires unprecedented coordination across all teams, but the payoff—capturing significant mobile market share—justifies this investment.

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

A critical user experience bug is severely impacting our search functionality and causing measurable business harm. Impact Assessment: **All users affected** - Every user who applies filters and navigates back loses their selection; **High abandonment rate** - Nearly one in four users leave the site after encountering this bug; **Support volume** - Hundreds of complaints this month about "broken search"; **Revenue loss** - Substantial monthly revenue impact from frustrated users not completing purchases. User Journey Breakdown: 1. User carefully selects multiple filters (category, price range, availability); 2. User clicks on a promising search result to view details; 3. User decides item isn't quite right, clicks browser back button; 4. **FAILURE** - All filters cleared, results reset to default view; 5. User must re-apply all filters from scratch (average 6 clicks); 6. After multiple occurrences, users abandon the site entirely. Technical Investigation: The issue emerged after our v2.3.0 release which updated our routing library. Initial debugging reveals: Filter state stored only in component memory (not preserved across navigation); Browser history API not properly integrated with our state management; URL parameters not syncing with filter selections; Session storage backup mechanism was accidentally removed. This is a P0 issue requiring immediate attention as it directly impacts our core user flow and revenue.

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

**Notice:** Worked correctly before v2.3.0

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
- [ ] Review v2.3.0 changes
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

Our analytics dashboard has become a critical pain point that's driving users away from our platform and damaging our reputation. Current Performance Crisis: **Extremely slow initial load** - Users stare at blank screens or spinners for many seconds; **Poor interactivity** - Even after content appears, nothing is clickable for additional seconds; **High bounce rate** - Over one-third of users leave before the page loads; **Mobile performance** - Load times exceed acceptable thresholds on average connections. Business Impact: **User complaints** - "Slow dashboard" is now our second most common support topic; **Churn risk** - Multiple enterprise clients cited performance in non-renewal discussions; **Competitive disadvantage** - Competitors advertise "Lightning fast analytics" against us; **Team productivity** - Our own internal teams waste significant time daily waiting for loads. Root Cause Analysis: Our performance profiling revealed multiple compounding issues: **Bundle size explosion** - JavaScript bundle larger than many mobile apps; **Sequential API calls** - Multiple requests that could be parallelized; **No caching strategy** - Every page load fetches everything fresh; **Render blocking resources** - Large CSS loads before any content appears. Optimization Strategy: We'll implement a comprehensive performance overhaul focusing on: **Code splitting** - Load only what's needed for the current view; **Progressive rendering** - Show content as it becomes available; **Smart caching** - Service worker + HTTP caching for instant subsequent loads; **API optimization** - Parallel requests and GraphQL for precise data fetching. This isn't just a performance improvement—it's about saving our product's reputation and retaining customers who expect instant access to their data.

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

Users need more control over search results to find relevant items quickly. Currently, they must scroll through hundreds of unfiltered results, leading to frustration and abandoned searches. This feature adds four essential filter types to narrow search results effectively. Each filter will update results in real-time, helping users find exactly what they need without excessive scrolling or multiple searches.

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

*All examples reference templates from Ticket - Templates & Standards.md. Version 1.3.0 updates: 1-paragraph descriptions, "Desired Behavior" for bugs, removed Technical Details sections.*