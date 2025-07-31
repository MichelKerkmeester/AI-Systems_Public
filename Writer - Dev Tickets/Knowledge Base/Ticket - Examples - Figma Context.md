# Ticket Examples - Figma Context

Full specification of how to use Figma MCP for understanding designs and writing better tickets, with examples showing proper context usage without technical specification extraction.

## Table of Contents

1. [🎨 FIGMA CONTEXT EXAMPLES](#1--figma-context-examples)
2. [🔄 COMPONENT UPDATE EXAMPLES](#2--component-update-examples)
3. [📝 USAGE PATTERNS](#3--usage-patterns)
4. [✅ WHEN TO USE FIGMA](#4--when-to-use-figma)
5. [⚠️ COMMON PITFALLS TO AVOID](#5-️-common-pitfalls-to-avoid)

---

## 1. 🎨 FIGMA CONTEXT EXAMPLES

### 🖼️ Example 1: Customer Self-Service Portal

```markdown
MODE: $interactive → $complex
TICKET TYPE: Feature
MCP USED: Cascade Thinking + Figma
FIGMA INTEGRATED: Yes (for context)

---

### ❖ Customer Self-Service Portal

---

# ⌘ About

Our support team is overwhelmed with routine requests that customers could handle themselves. After reviewing the Figma designs, I can see this portal will provide a comprehensive self-service experience with account management, billing access, and automated troubleshooting.

**User Value:** Resolve common issues instantly without waiting for support responses

**Business Goal:** Reduce support ticket volume by 40% while improving customer satisfaction

---

[[*TOC*]]

---

## → Designs & References

- [Figma - Customer Portal Complete Flow](figma://file/XYZ789/Customer-Portal)
- [Figma - Mobile Responsive Views](figma://file/XYZ789/Customer-Portal?node-id=mobile)
- [Figma - Error States & Empty States](figma://file/XYZ789/Customer-Portal?node-id=states)

**Notice:** Figma shows 12 main screens with comprehensive error handling
**Notice:** Design includes both desktop and mobile responsive layouts
**Notice:** Empty states provided for all data-dependent sections

---

## ◇ Phase 1: Foundation & Authentication (Week 1-2)
- Secure login with SSO and traditional auth options
- Password reset flow with email verification
- Account switcher for users with multiple accounts
- Session management with timeout warnings
- Mobile-optimized authentication experience

---

## ◇ Phase 2: Account Management (Week 3-4)
- View and edit profile information
- Manage team members and permissions
- Configure notification preferences
- Set up two-factor authentication
- Download account data for compliance

---

## ◇ Phase 3: Billing & Subscriptions (Week 5-6)
- View current subscription and usage
- Access billing history and download invoices
- Update payment methods securely
- Manage subscription tier and add-ons
- Set up usage alerts and spending limits

---

## ◇ Phase 4: Self-Service Support (Week 7-8)
- Interactive troubleshooting wizard
- Searchable knowledge base integration
- Common issues resolution workflows
- System status and incident history
- Fallback to create support ticket when needed

---

## ✓ Success Criteria
- [ ] 40% reduction in support tickets for covered topics
- [ ] 80% of users successfully complete self-service tasks
- [ ] Average task completion under 3 minutes
- [ ] Mobile usage accounts for 30%+ of portal traffic
- [ ] Customer satisfaction score improves by 15%
- [ ] Zero security vulnerabilities in authentication
- [ ] Portal loads in under 2 seconds globally
- [ ] Accessibility score >95 (WCAG AA compliant)

---

## ⊗ Dependencies
- Requires: SSO provider integration (#4001)
- Requires: Billing API v2 upgrade (#4002)
- Requires: Knowledge base API access (#4003)
- Requires: Customer data migration plan (#4004)
- Blocks: Support team workflow automation (#4050)

---

## ⚠ Risks
- **Authentication complexity:** Multiple auth methods increase attack surface
  - Mitigation: Security audit before launch, penetration testing
- **Data sensitivity:** Portal exposes billing and account data
  - Mitigation: Role-based access control, audit logging
- **Mobile experience:** Complex features on small screens
  - Mitigation: Progressive disclosure, mobile-first design approach
- **Change management:** Customers used to calling support
  - Mitigation: Onboarding campaign, support team training

---

## 💡 Insights from Figma Review

**User Flow Understanding:**
- The design revealed 3 distinct user paths: quick tasks, detailed management, and troubleshooting
- Each path has appropriate shortcuts and escape hatches
- Progressive disclosure keeps initial screens simple

**States & Edge Cases Identified:**
- Empty states for new accounts without billing history
- Error states for failed payment method updates  
- Loading states for data-heavy sections
- Offline message when connection lost
- Permission-based UI variations

**Complexity Assessment:**
- 12 main screens + numerous substates = high complexity
- Mobile required significant layout adaptations
- Accessibility considerations throughout
- Multiple integration points visible in designs
```

---

### 📊 Example 2: Team Dashboard

```markdown
MODE: $interactive → $standard
TICKET TYPE: Feature
MCP USED: Cascade Thinking + Figma
FIGMA INTEGRATED: Yes (for context)

---

### ❖ Team Dashboard

**User Value:** See your team's progress and collaborate effectively in one central location

**Business Goal:** Increase team collaboration by 40% and reduce status meeting time by 50%

---

## → Designs & References
- [Figma - Team Dashboard Designs](figma://file/ABC123/Team-Dashboard)
- [Figma - Component Library](figma://file/DEF456/Components)

**Notice:** Designs show 3 main sections: activity feed, team metrics, and project status

---

## ◇ Requirements
- Display real-time team activity feed with recent updates
- Show team performance metrics in easy-to-scan cards  
- List active projects with progress indicators
- Support filtering by team member and time period
- Include quick actions for common team tasks
- Handle empty states when no data available
- Refresh automatically without losing user context

---

## ✓ Success Criteria
- [ ] Dashboard loads in under 2 seconds
- [ ] Team members check dashboard daily (track usage)
- [ ] 50% reduction in "what's the status?" messages
- [ ] All team data updates within 30 seconds
- [ ] Works smoothly on tablet and desktop devices

---

## ⊗ Dependencies
- Requires: Team API endpoints for activity data (#2001)
- Requires: Metrics calculation service (#2002)
- Requires: Real-time update infrastructure (#2003)

---

## 💡 Insights from Figma Review

**Layout Understanding:**
- Dashboard uses a 3-column layout on desktop
- Mobile view stacks sections vertically
- Cards have consistent height for visual alignment

**Interactive Elements:**
- Each metric card is clickable for details
- Filters persist across sessions
- Activity feed has infinite scroll
```

---

### 🔄 Example 3: Onboarding Flow Redesign

```markdown
MODE: $interactive → $standard
TICKET TYPE: Feature
MCP USED: Cascade Thinking + Figma
FIGMA INTEGRATED: Yes (for context)

---

### ❖ Streamlined Onboarding Flow

**User Value:** Complete account setup quickly with clear guidance at every step

**Business Goal:** Reduce new user drop-off from 60% to under 20%

---

## → Designs & References
- [Figma - Onboarding Flow](figma://file/XYZ789/Onboarding-Redesign)
- [Figma - Error States](figma://file/XYZ789/Onboarding-Redesign?node-id=errors)

**Notice:** Flow includes skip option for experienced users

---

## ◇ Requirements
- Welcome screen with value proposition and progress indicator
- Account setup with email verification and password requirements
- Team invite system supporting bulk invites via CSV
- Workspace configuration with templates for common setups
- Skip option for experienced users at each step
- Clear error messaging for all failure scenarios
- Progress saved between sessions
- Mobile-responsive design for setup on any device

---

## ✓ Success Criteria
- [ ] New user drop-off reduced to <20%
- [ ] Average setup completion time <5 minutes
- [ ] 90% of users successfully invite team members
- [ ] Skip option used by 30% of returning users
- [ ] Zero critical errors during setup flow

---

## ⊗ Dependencies
- Requires: Email verification service (#3001)
- Requires: CSV parsing for bulk invites (#3002)
- Requires: Workspace template system (#3003)

---

## 💡 Insights from Figma Review

**Flow Understanding:**
- 5 distinct steps with clear progression
- Alternative paths for different user types
- Each step can be completed in under 1 minute

**Edge Cases Found:**
- Email already exists error handling
- CSV format validation for bulk invites
- Session timeout during long setup
- Back navigation preserves entered data
```

---

## 2. 🔄 COMPONENT UPDATE EXAMPLES

### 🎨 Example 1: Profile Card Update

```markdown
### ❖ Update Profile Card Component

**User Value:** See team member information with improved visual hierarchy

**Business Goal:** Increase team recognition and collaboration

---

## → Designs & References
- [Figma - Updated Profile Card](figma://file/ABC123/Components?node-id=24:156)

**Notice:** Design includes new status indicators and updated layout

---

## ◇ Requirements
- Update profile card to match new Figma design
- Add status indicator showing availability
- Maintain all existing functionality
- Ensure backward compatibility with current data

---

## ✓ Success Criteria
- [ ] Component matches updated Figma design
- [ ] Status indicators display correctly
- [ ] No regression in existing features
- [ ] Loads with same performance
```

---

### 🔧 Example 2: Button Component Refresh

```markdown
### ❖ Update Button Component System

**User Value:** Experience consistent, modern interactions across the application

**Business Goal:** Improve perceived quality and reduce design debt

---

## → Designs & References
- [Figma - Button Component Updates](figma://file/DEF456/Design-System?node-id=buttons)

**Notice:** New design includes 3 sizes and 5 variants with updated states

---

## ◇ Requirements
- Update all button components to match new Figma designs
- Implement new size variants (small, medium, large)
- Add new button types (primary, secondary, ghost, danger, link)
- Update hover, active, and disabled states
- Maintain existing button functionality and event handlers

---

## ✓ Success Criteria
- [ ] All buttons match Figma design system
- [ ] Smooth state transitions implemented
- [ ] No functional regressions
- [ ] Accessibility maintained or improved
```

---

## 3. 📝 USAGE PATTERNS

### 🎯 Figma for Understanding

1. **Review for Completeness**
   - Identify all screens in a flow
   - Find edge cases and error states
   - Understand the full user journey

2. **Assess Complexity**
   - Count components and interactions
   - Identify technical challenges
   - Plan development phases

3. **Capture User Intent**
   - Understand design decisions
   - Note interaction patterns
   - Identify accessibility needs

### 📋 What to Document

**DO Include:**
- Number of screens or components
- Key user flows identified
- States discovered (empty, error, loading)
- Complexity assessment
- Notable design patterns

**DON'T Include:**
- Pixel measurements
- Color codes
- Font specifications
- CSS properties
- Technical implementation details

---

## 4. ✅ WHEN TO USE FIGMA

### 🟢 Good Candidates

**Complex UI Features:**
- Multi-step workflows
- Dashboard redesigns
- New feature modules
- Interactive components
- Data visualizations

**Design Updates:**
- Component library changes
- Visual refresh projects
- Style guide updates
- Responsive improvements

**User Flows:**
- Onboarding sequences
- Checkout processes
- Multi-screen features
- State-heavy interfaces

### 🔴 Skip Figma For

**Technical Features:**
- API development
- Database changes
- Performance improvements
- Backend logic
- Security updates

**When Figma Won't Add Value:**
- Text-only updates
- Backend bug fixes
- Non-visual features
- When user hasn't provided designs
- When explicitly told not to use it

---

## 5. ⚠️ COMMON PITFALLS TO AVOID

### ❌ In Figma Usage
- ⊗ Don't extract technical specifications unless user requests
- ⊗ Don't include CSS values or measurements unless asked
- ⊗ Don't turn tickets into design documentation automatically
- ⊗ Don't skip user value for design details
- ⊗ Don't force complexity where none exists

### ❌ In Requirements Writing
- ⊗ Don't describe HOW to implement (unless user asks)
- ⊗ Don't copy design specs without user request
- ⊗ Don't focus on visual details over function
- ⊗ Don't assume designs are final
- ⊗ Don't forget non-visual requirements

### ✅ Best Practices
- ✓ Use Figma to understand the complete picture
- ✓ Focus on user outcomes in requirements
- ✓ Reference designs with simple links
- ✓ Extract specs only when user explicitly asks
- ✓ Let developers reference Figma directly for details
- ✓ Use Figma for any UI feature when it helps (even simple ones)</document_content>