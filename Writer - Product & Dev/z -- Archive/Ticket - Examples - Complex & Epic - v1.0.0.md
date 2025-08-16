# Ticket Examples - Complex & Epic

## 1. 🔧 COMPLEX MODE EXAMPLES ($c)

### 🔍 Example 1: Search Experience Overhaul

```markdown
### ❖ Search Experience Overhaul

---

# ⌘ About

Our search is failing users - 67% abandon without finding what they need. Competitors offer smart filtering and personalization. We need a complete overhaul to remain competitive.

**User Value:** Find exactly what they need with smart filters and suggestions

**Business Goal:** Increase search-to-conversion from 12% to 25%

---

[[*TOC*]]

---

## → Designs & References

### ◻︎ Flows
- [Figma - Search Journey Complete](link)
- [Figma - Filter Interactions](link)
- [Figma - Personalization States](link)

### ◻︎ Components
- [Figma - Filter Components](link)
- [Figma - Search Results](link)
- [Figma - Mobile Patterns](link)

**Notice:** Design includes A/B test variations for filter placement.

---

## ◇ Phase 1: Basic Filters (Sprint 1)
- Category and date filters
- Mobile-responsive design  
- Real-time result updates
- Clear all functionality

---

## ◇ Phase 2: Smart Features (Sprint 2)
- Auto-suggestions while typing
- Popular filter combinations
- Recent search history
- Filter usage analytics

---

## ◇ Phase 3: Personalization (Sprint 3)
- Saved filter sets
- Recommended filters based on behavior
- Quick filter shortcuts
- Personalized result ranking

---

## ✓ Success Criteria
- [ ] 50% reduction in "no results" searches
- [ ] Average results found in <3 clicks  
- [ ] Search-to-conversion rate reaches 25%
- [ ] Mobile usage increases by 40%

---

## ⊗ Dependencies
- Requires: New search infrastructure (#1230)
- Requires: User behavior tracking (#1231)  
- Blocks: AI recommendations (#1250)

---

## ⚠ Risks
- **Performance:** May need caching for <300ms response
- **Adoption:** Users attached to current search
- **Data Privacy:** Personalization requires consent
```

---

### 💬 Example 2: Real-time Collaboration System

```markdown
### ❖ Multi-user Document Editing

---

# ⌘ About

Enable teams to collaborate on documents in real-time, seeing each other's changes instantly. This positions us competitively with Google Docs and Notion while maintaining our unique value propositions.

**User Value:** Work together on documents without version conflicts or delays

**Business Goal:** Increase team plan adoption by 40% through collaboration features

---

[[*TOC*]]

---

## → Designs & References

### ◻︎ Editor Experience
- [Figma - Cursor & Selection States](link)
- [Figma - User Presence Indicators](link)
- [Figma - Conflict Resolution](link)

### ◻︎ Collaboration Features
- [Figma - Comment System](link)
- [Figma - Version History](link)
- [Figma - Permission Models](link)

**Notice:** Maximum 10 concurrent editors per document

---

## ◇ Phase 1: Foundation (Week 1-2)
- WebSocket infrastructure
- Basic cursor sharing
- User presence indicators
- Connection status handling

---

## ◇ Phase 2: Core Editing (Week 3-4)
- Operational transformation for text
- Multi-cursor display
- Selection synchronization
- Basic conflict resolution

---

## ◇ Phase 3: Collaboration Tools (Week 5-6)
- Inline commenting system
- Change attribution
- Follow user's cursor
- Activity notifications

---

## ◇ Phase 4: Polish & Scale (Week 7-8)
- Performance optimization
- Offline support with sync
- Permission granularity
- Analytics integration

---

## ✓ Success Criteria
- [ ] <50ms latency for cursor updates
- [ ] Support 10 concurrent editors
- [ ] 99.9% conflict-free merges
- [ ] Offline changes sync seamlessly
- [ ] 40% increase in team collaboration

---

## ⊗ Dependencies
- Requires: WebSocket infrastructure (#5001)
- Requires: Document versioning system (#5002)
- Blocks: Enterprise security features (#5050)

---

## ⚠ Risks
- **Scalability:** WebSocket costs at high concurrency
- **Complexity:** OT algorithm edge cases
- **Browser Support:** Older browsers need fallback
- **Security:** Real-time data exposure risks
```

---

## 2. 🚀 EPIC MODE EXAMPLES ($e)

### 🎯 Example 1: Customer Self-Service Portal

```markdown
### ❖ Epic: Customer Self-Service Portal

**User Value:** Customers resolve issues without waiting for support

**Business Goal:** Reduce support tickets by 40%

---

## ⌘ Overview
Enable customers to manage their accounts, view data, and resolve common issues independently through a dedicated portal.

---

## ✓ Success Metrics
- [ ] 40% reduction in support tickets
- [ ] 80% of users self-serve successfully
- [ ] Average resolution time < 5 minutes

---

## ◇ Child Tickets

### ◻︎ Phase 1: Foundation
- [ ] **Authentication & Access** - Secure login and role management
- [ ] **Dashboard Overview** - Key account info at a glance
- [ ] **Navigation Structure** - Intuitive portal layout

### ◻︎ Phase 2: Core Features  
- [ ] **Account Management** - Update profile and preferences
- [ ] **Billing & Invoices** - View and download statements
- [ ] **Usage Analytics** - Track product usage

### ◻︎ Phase 3: Self-Service
- [ ] **Knowledge Base Integration** - Searchable help articles
- [ ] **Automated Troubleshooting** - Common issue resolution
- [ ] **Ticket Submission** - When self-service isn't enough

---

## ⊗ Dependencies
- Requires: SSO infrastructure (#1200)
- Requires: API rate limiting (#1201)

---

## ⌘ Timeline
12 weeks (4 weeks per phase)
```

---

### 📱 Example 2: Mobile App Launch

```markdown
### ❖ Epic: Native Mobile Applications

**User Value:** Access full platform features on iOS and Android devices

**Business Goal:** Capture 30% of mobile market share in our category

---

## ⌘ Overview
Launch native mobile apps with feature parity to web, optimized for mobile workflows and leveraging device capabilities.

---

## ✓ Success Metrics
- [ ] 4.5+ star rating in app stores
- [ ] 60% monthly active usage
- [ ] 30% of total platform usage on mobile
- [ ] <2 second app launch time

---

## ◇ Child Tickets

### ◻︎ Phase 1: Core Infrastructure
- [ ] **App Architecture Setup** - Foundation and navigation
- [ ] **Authentication Flow** - Secure mobile login with biometrics
- [ ] **Data Sync Engine** - Offline-first architecture
- [ ] **Push Notifications** - System setup and permissions

### ◻︎ Phase 2: Essential Features
- [ ] **Dashboard Mobile** - Responsive key metrics view
- [ ] **Core Workflow 1** - Primary user journey
- [ ] **Core Workflow 2** - Secondary user journey  
- [ ] **Search & Navigation** - Mobile-optimized finding

### ◻︎ Phase 3: Mobile-Specific
- [ ] **Camera Integration** - Document scanning
- [ ] **Location Services** - Contextual features
- [ ] **Share Extension** - System integration
- [ ] **Widget Support** - Home screen widgets

### ◻︎ Phase 4: Launch Preparation
- [ ] **App Store Optimization** - Listing and screenshots
- [ ] **Onboarding Flow** - First-time user experience
- [ ] **Analytics Integration** - Usage tracking
- [ ] **Beta Testing Program** - User feedback loop

---

## ⊗ Dependencies
- Requires: Mobile API development (#7001)
- Requires: Design system mobile components (#7002)
- Requires: Security audit for mobile (#7003)

---

## ⌘ Timeline
20 weeks total (5 weeks per phase)

---

## ⚠ Risks
- **App Store Approval:** Policy compliance needed
- **Device Fragmentation:** Android version support
- **Performance:** Older device compatibility
- **Resources:** Dedicated mobile team needed
```

---

## 3. 📐 PHASE BREAKDOWN PATTERNS

### 🔧 Complex Ticket Phases

Complex tickets should have 3-5 phases with clear boundaries:

1. **Foundation Phase**
   - Infrastructure setup
   - Basic functionality
   - Core dependencies

2. **Feature Phase**  
   - Main user features
   - Primary workflows
   - Integration points

3. **Enhancement Phase**
   - Advanced features
   - Optimization
   - Polish

4. **Scale Phase** (optional)
   - Performance tuning
   - Load handling
   - Monitoring

---

### 🚀 Epic Child Ticket Patterns

Epic child tickets should be:
- **Independent:** Can be developed separately
- **Valuable:** Delivers user value alone
- **Estimable:** 1-2 week scope each
- **Testable:** Clear acceptance criteria

Group by:
- **Technical Layer:** Frontend, Backend, Infrastructure
- **User Journey:** Onboarding, Core Use, Advanced
- **Feature Set:** Must-have, Should-have, Nice-to-have

---

## 4. 📊 COMPLEXITY INDICATORS

### 🔧 When to Use Complex Mode ($c)
- Multiple development phases required
- Significant technical uncertainty
- Cross-team coordination needed
- 3+ week development time
- Progressive rollout planned

### 🚀 When to Use Epic Mode ($e)
- Initiative spans multiple sprints
- Requires dedicated team
- Multiple independent features
- Strategic business objective
- Quarterly-level planning

### ⚖️ Complex vs Epic Decision
- **Complex:** One feature, multiple phases
- **Epic:** Multiple features, one goal

---

## 5. ✅ QUALITY MARKERS

### 🔧 Well-Written Complex Ticket
- ✓ Clear phase boundaries
- ✓ Progressive value delivery
- ✓ Risk mitigation included
- ✓ Dependencies mapped
- ✓ Each phase independently valuable

### 🚀 Well-Written Epic
- ✓ Strategic objective clear
- ✓ Child tickets independent
- ✓ Success metrics at epic level
- ✓ Timeline realistic
- ✓ Resource needs identified