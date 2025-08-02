# Ticket - Examples Library - v1.0.0

Categorized examples showing real-world ticket implementations. All examples reference templates from Ticket - Templates & Standards.md.

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

### ❖ Profile Picture Upload

**User Value:** Personalize your account with a profile photo

**Business Goal:** Increase profile completion rate by 40%

---

## ◇ Requirements
- Upload image from device
- Basic image cropping
- Replace existing photo
- Support JPG/PNG formats

---

## ✓ Success Criteria
- [ ] Images upload successfully
- [ ] 5MB max file size enforced
- [ ] Photo displays immediately

---

## ✓ Resolution Checklist
- [ ] Implement file upload component
- [ ] Add image validation
- [ ] Test on mobile devices
- [ ] Update user profile API
- [ ] Add success notification
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

### ❖ Advanced Search Filters

**User Value:** Find exactly what you need with powerful filtering options

**Business Goal:** Reduce search abandonment from 67% to 30%

---

## ◇ Requirements
- **Filter Types**
  - Category with multi-select
  - Date range picker
  - Price range slider
  - Status checkboxes
- **Filter Behavior**
  - Results update instantly
  - Show active filter count
  - Clear all filters option
  - Filters persist in session

---

## → Designs & References
- [Figma - Filter Panel](link)
- [Figma - Mobile Filters](link)

**Notice:** Mobile uses bottom sheet pattern

---

## ✓ Success Criteria
- [ ] Results update within 300ms
- [ ] All filter combinations work
- [ ] Filter state persists on back navigation
- [ ] Mobile gesture support works

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

### ❖ Multi-user Document Editing

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
- WebSocket infrastructure setup
- Basic cursor position sharing
- User presence indicators
- Connection status handling
- Graceful disconnection

---

## ◇ Phase 2: Core Editing (Week 3-4)
- Operational transformation for text
- Multi-cursor display
- Selection synchronization
- Basic conflict resolution
- Change attribution

---

## ◇ Phase 3: Polish & Scale (Week 5-6)
- Performance optimization
- Offline support with sync
- Advanced permissions
- Activity notifications
- Analytics integration

---

## ✓ Success Criteria
- [ ] <50ms latency for cursor updates
- [ ] Support 10 concurrent editors
- [ ] 99.9% uptime for sync service
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

### ❖ Epic: Native Mobile Applications

**User Value:** Access full platform features on iOS and Android

**Business Goal:** Capture 30% mobile market share

---

## ⌘ Overview
Launch native mobile apps with feature parity to web, optimized for mobile workflows and leveraging device capabilities for superior user experience.

---

## ✓ Success Metrics
- [ ] 4.5+ star app store rating
- [ ] 60% monthly active usage
- [ ] <2 second app launch time
- [ ] 30% of total platform usage

---

## ◇ Child Tickets

### ◻︎ Phase 1: Core Infrastructure
- [ ] **App Architecture** - Foundation and navigation setup
- [ ] **Authentication** - Secure login with biometrics
- [ ] **Data Sync** - Offline-first architecture
- [ ] **Push Notifications** - System integration

### ◻︎ Phase 2: Feature Parity
- [ ] **Dashboard Mobile** - Key metrics view
- [ ] **Core Feature 1** - Primary workflow
- [ ] **Core Feature 2** - Secondary workflow
- [ ] **Search & Nav** - Mobile patterns

### ◻︎ Phase 3: Mobile Native
- [ ] **Camera Integration** - Document scanning
- [ ] **Location Services** - Context features
- [ ] **Share Extension** - System integration
- [ ] **Widgets** - Home screen widgets

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

### ❖ Bug: Search Filters Reset on Back Navigation

**User Value:** Keep your selected filters when returning to search

**Business Goal:** Reduce user frustration and 23% abandonment rate

---

## ◆ Current Behavior
1. User applies multiple filters
2. User clicks on search result
3. User clicks browser back
4. **Bug:** All filters are cleared

---

## ✓ Expected Behavior
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
- [ ] Filters persist 100% of time
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

### ❖ Improvement: Dashboard Load Time Optimization

**User Value:** See your data instantly without waiting

**Business Goal:** Reduce dashboard bounce rate by 50%

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
- Implement code splitting
- Add progressive loading
- Optimize bundle size
- Cache API responses
- Lazy load below-fold content

---

## → Designs & References
- [Figma - Loading States](link)
- [Performance Audit](link)

---

## ✓ Success Criteria
- [ ] Initial paint <1 second
- [ ] Interactive <2 seconds
- [ ] Lighthouse score >90
- [ ] 50% bounce reduction

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

### ❖ Search Filter Enhancement

**User Value:** Find products faster with advanced filtering

**Business Goal:** Increase conversion rate by improving search

---

## ◇ Requirements
**Extracted from request:**
- Category filter with multi-select
- Date range picker
- Price range with min/max
- Status checkboxes

**Inferred additions:**
- Show active filter count
- Clear all filters option
- Results update instantly
- Mobile-responsive design

**Needs:**
- Design mockups for filter UI
- Specific status options
- Price range boundaries

---

## ✓ Success Criteria
- [ ] All filters work correctly
- [ ] Results update <500ms
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
```

**Pattern:** Extract obvious requirements, mark inferences, flag gaps

---

## 8. 🎯 FEATURE TYPE PATTERNS

### Authentication Features

Common requirements to consider:
- Password requirements
- Session management
- Remember me option
- Security features (2FA)
- Social login options
- Password recovery
- Account lockout rules

### Search Features

Common requirements to consider:
- Search as you type
- Search history
- Suggestions/autocomplete
- Filters and sorting
- No results handling
- Search analytics
- Performance targets

### Dashboard Features

Common requirements to consider:
- Data refresh rates
- Widget customization
- Mobile responsiveness
- Export capabilities
- Time range selection
- Role-based visibility
- Performance metrics

### Payment Features

Common requirements to consider:
- Payment methods
- Security compliance
- Receipt generation
- Refund handling
- Currency support
- Tax calculation
- Failed payment handling

---

*All examples reference templates from Ticket - Templates & Standards.md. Use these patterns as starting points and adapt based on specific requirements.*