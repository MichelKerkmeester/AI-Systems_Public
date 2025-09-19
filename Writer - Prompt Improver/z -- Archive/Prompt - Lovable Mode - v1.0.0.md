# Prompt - Lovable Mode - v1.0.0

**Domain-specific prompt optimization** for Lovable development with three specialized sub-modes.

## Table of Contents

1. [📱 OVERVIEW](#1--overview)
2. [🎯 THREE SUB-MODES](#2--three-sub-modes)
3. [🚀 ACTIVATION & USAGE](#3--activation--usage)
4. [🏗️ MODE FRAMEWORKS](#4-️-mode-frameworks)
5. [💻 ENHANCEMENT PATTERNS](#5--enhancement-patterns)
6. [🎨 VISUAL INTEGRATION](#6--visual-integration)
7. [📚 KNOWLEDGE BASE TEMPLATES](#7--knowledge-base-templates)
8. [🔧 TECHNICAL SPECIFICATIONS](#8--technical-specifications)
9. [💬 CHAT VS DEFAULT MODE STRATEGY](#9--chat-vs-default-mode-strategy)
10. [🚨 TROUBLESHOOTING GUIDE](#10--troubleshooting-guide)
11. [💡 BEST PRACTICES](#11--best-practices)

---

## 1. 📱 OVERVIEW

Lovable Mode v2.1 provides three specialized sub-modes optimized for different development scenarios on the Lovable platform, based on extensive research showing distinct use cases require different approaches.

### Core Tech Stack
- **Frontend**: React, Vite, Tailwind CSS, ShadCN
- **Backend**: Supabase (PostgreSQL, Auth, Realtime, Storage)
- **Integrations**: Stripe, GitHub, Builder.io (Figma)

### MCP Usage Guidelines
| Sub-Mode | MCP Tool | Thoughts | Use Case |
|----------|----------|----------|----------|
| **Prototype** | Sequential | 1-3 | Visual concepts, mockups |
| **Website** | Sequential | 2-4 | Landing pages, marketing |
| **App** | Cascade | 3-6 | Full-stack applications |

Note: Complex apps may use up to 8 thoughts for architecture planning

---

## 2. 🎯 THREE SUB-MODES

### 2.1 Prototype Mode (`$lovable-prototype` / `$lp`)
**Purpose**: Rapid visual prototyping for concept validation
**Best For**: Mockups, design systems, user flows, stakeholder demos
**Key Features**: High visual fidelity, animations, dummy data, no backend

### 2.2 Website Mode (`$lovable-website` / `$lw`)
**Purpose**: Production-ready marketing sites and landing pages
**Best For**: Landing pages, portfolios, blogs, e-commerce fronts
**Key Features**: SEO optimization, analytics, Stripe payments, performance focus

### 2.3 App Mode (`$lovable-app` / `$la`)
**Purpose**: Full-stack application development
**Best For**: SaaS platforms, dashboards, CRM systems, collaborative tools
**Key Features**: Supabase integration, real-time features, authentication, complex state

---

## 3. 🚀 ACTIVATION & USAGE

### Commands & Auto-Detection

| Mode | Command | Shortcut | Auto-Keywords | MCP Usage |
|------|---------|----------|---------------|-----------|
| **Prototype** | `$lovable-prototype` | `$lp` | mockup, design, wireframe | Sequential (1-3) |
| **Website** | `$lovable-website` | `$lw` | landing, marketing, blog | Sequential (2-4) |
| **App** | `$lovable-app` | `$la` | dashboard, auth, crud | Cascade (3-6) |

### Auto-Detection Priority (when using `$lovable` alone)
1. **App indicators** (weight: 1.0): dashboard, crud, auth, database, supabase
2. **Website indicators** (weight: 0.8): landing, marketing, SEO, conversion
3. **Prototype indicators** (weight: 0.6): mockup, design, wireframe, visual

**Conflict Resolution:**
- Multiple matches: Use highest weight
- Equal weights: Ask user for clarification
- No matches: Default to $lovable-app

---

## 4. 🏗️ MODE FRAMEWORKS

### 4.1 VISION Framework (Prototype)
- **V**isual Design - Layout, colors, typography
- **I**nteractions - Animations, transitions
- **S**creens - Page flow, navigation
- **I**teration - Quick refinements
- **O**bservable - User journey
- **N**otable - Memorable elements

### 4.2 CONVERT Framework (Website)
- **C**ontent - SEO, copy, metadata
- **O**ptimization - Performance, Core Web Vitals
- **N**avigation - User pathways
- **V**isual Impact - Hero sections, CTAs
- **E**ngagement - Forms, chat, social
- **R**esponsive - Mobile-first
- **T**esting - Analytics, A/B tests

### 4.3 SCALE Framework (App)
- **S**tructure - Database schema, architecture
- **C**omponents - Reusable UI elements
- **A**uthentication - User management
- **L**ogic - Business rules, validation
- **E**ndpoints - APIs, webhooks, real-time

---

## 5. 💻 ENHANCEMENT PATTERNS

### 5.1 Prototype Patterns

**Quick Concept**:
```
Create [type] prototype:
- Visual style: [reference]
- Key screens: [list]
- Interactions: [animations]
- Use dummy data
- Focus on visual polish
```

**User Flow**:
```
Prototype [process] flow:
1. Entry screen
2. Process screens
3. Success screen
Include transitions and error states visually
```

### 5.2 Website Patterns

**Landing Page**:
```
Build conversion-optimized landing:
- Hero: Headline + CTA + Visual
- Features: 3-column grid
- Social proof: Testimonials
- SEO: Meta tags, schema
- Performance: 90+ PageSpeed
```

**Marketing Site**:
```
Multi-page marketing website:
- Pages: Home, About, Products, Contact
- Global: Header, Footer, Analytics
- Integrations: Forms, Chat, Stripe
```

### 5.3 App Patterns

**Dashboard**:
```
Data dashboard with:
- Tech: React + Supabase + Recharts
- Auth: Email/password
- Features: KPIs, charts, filters
- Real-time updates
```

**CRUD System**:
```
[Entity] management:
- Operations: Create, Read, Update, Delete
- Features: Search, filter, pagination
- Supabase: RLS policies, triggers
```

---

## 6. 🎨 VISUAL INTEGRATION

### 6.1 Figma Workflow
1. **Prepare**: Use Auto-Layout, name layers
2. **Export**: Builder.io plugin → "Open in Lovable"
3. **Enhance**: Fix discrepancies, add responsive behavior

### 6.2 Screenshot to Code
```
Convert [screenshot] to Lovable:
- Match visual exactly
- Identify components
- Add responsive behavior
- Implement interactions
```

### 6.3 Design System
```
Colors: Primary, secondary, accent
Typography: Font scale, line heights
Spacing: 8px base unit
Components: Consistent variants
```

---

## 7. 📚 KNOWLEDGE BASE TEMPLATES

### Prototype PRD
```markdown
## Overview
Purpose: [Validation/Testing]
Users: [Personas]
Flows: [Main journeys]

## Visual
Style: [Modern/Classic]
Colors: [Palette]
Inspiration: [References]

## Screens
1. [Name]: [Purpose]
2. [Name]: [Purpose]

## Success Metrics
- Visual appeal
- Flow clarity
```

### Website PRD
```markdown
## Overview
Type: [Marketing/Portfolio]
Audience: [Demographics]
Goal: [Conversion/Engagement]

## Technical
SEO: [Keywords]
Performance: [Targets]
Analytics: [Tracking]

## Content
Pages: [List]
CTAs: [Primary/Secondary]
```

### App PRD
```markdown
## Overview
Type: [SaaS/Tool]
Users: [Roles]
Value: [Problem solved]

## Architecture
Frontend: React + Tailwind
Backend: Supabase
Auth: [Strategy]

## Features
MVP: [Core features]
Future: [Roadmap]

## Data Model
[Schema overview]
```

---

## 8. 🔧 TECHNICAL SPECIFICATIONS

### Platform Stack
| Layer | Prototype | Website | App |
|-------|-----------|---------|-----|
| **Frontend** | React + Tailwind | React + Vite + Tailwind | React + TypeScript + Tailwind |
| **Animation** | Framer Motion | CSS/Framer | Framer + Transitions |
| **Data** | Local/Mock | Forms + Analytics | Supabase Full Stack |
| **Auth** | None | Optional | Required (Supabase) |
| **Performance** | <2s load | <1.5s FCP, 95+ PageSpeed | <3s TTI |

### Mode-Specific Features

**Prototype**: Focus on animations, visual states, dummy content
**Website**: SEO tags, analytics, forms, payment integration
**App**: Database, real-time, RLS, file storage, background jobs

---

## 9. 💬 CHAT VS DEFAULT MODE STRATEGY

### Use Chat Mode For:
- **Planning & Architecture**
  - Database schema design
  - Component hierarchy
  - State management approach
  - API structure

- **Debugging & Understanding**
  - Error analysis
  - Performance issues
  - Integration problems
  - Lovable platform features

- **Design Decisions**
  - UI/UX choices
  - Technology trade-offs
  - Implementation strategies
  - Best practices

### Use Default Mode For:
- **Building & Implementation**
  - Component creation
  - Feature development
  - Styling updates
  - Function implementation

- **Testing & Refinement**
  - Bug fixes
  - UI polish
  - Performance optimization
  - Responsive adjustments

### Example Workflow:
```
1. Chat: "Let's plan the user authentication flow"
2. Chat: "What's the best database structure for this?"
3. Default: "Implement the login component with validation"
4. Default: "Add password reset functionality"
5. Chat: "Debug this Supabase RLS error"
6. Default: "Apply the fix we discussed"
```

---

## 10. 🚨 TROUBLESHOOTING GUIDE

### Common Lovable Issues & Solutions

#### Supabase Connection Errors
**Symptoms**: Auth failures, data not loading
**Solutions**:
- Check environment variables (no trailing slashes)
- Verify project URL and anon key
- Ensure RLS policies are configured
- Test in Supabase dashboard first

#### Component Rendering Issues
**Symptoms**: Blank screens, layout breaks
**Solutions**:
- Clear browser cache
- Check for conflicting Tailwind classes
- Verify ShadCN imports
- Use React DevTools to inspect

#### Build Failures
**Symptoms**: Red error messages, app won't compile
**Solutions**:
- Start with blank project
- Build incrementally
- Use "Try to Fix" button
- Check console for specific errors
- Verify all imports exist

#### Performance Problems
**Symptoms**: Slow loading, janky animations
**Solutions**:
- Optimize images (use WebP)
- Implement lazy loading
- Use React.memo for expensive components
- Check Supabase query efficiency
- Reduce bundle size

#### Real-time Not Working
**Symptoms**: Updates not appearing
**Solutions**:
- Enable realtime on Supabase tables
- Check subscription setup
- Verify RLS policies allow SELECT
- Test with Supabase dashboard

---

## 11. 💡 BEST PRACTICES

### Universal Principles
- ✅ Start with blank project, build incrementally
- ✅ Use Chat Mode for planning, Default for building
- ✅ Mobile-first responsive design
- ✅ Include "don't modify" constraints for stable code
- ✅ Test after each implementation step
- ✅ Commit working versions before major changes

### Mode-Specific Do's and Don'ts

**Prototype Mode**
- ✅ Visual references (Figma, screenshots)
- ✅ Focus on happy path
- ✅ Use realistic dummy data
- ✅ Prioritize animations
- ❌ No backend functionality
- ❌ No real authentication

**Website Mode**
- ✅ Optimize images and performance
- ✅ Implement SEO from start
- ✅ Test Core Web Vitals
- ✅ Include analytics tracking
- ❌ Don't over-engineer simple pages
- ❌ Don't skip meta tags

**App Mode**
- ✅ Plan database schema first
- ✅ Implement proper auth and RLS
- ✅ Use TypeScript for complex apps
- ✅ Add error boundaries
- ❌ Don't skip data validation
- ❌ Don't build everything at once

### Implementation Strategy

**Phase 1**: Foundation (Auth, routing, layout)
**Phase 2**: Core Features (Main functionality)
**Phase 3**: Enhancement (Polish, optimization)
**Phase 4**: Production (Testing, deployment)

### Performance Optimization
- Lazy load components and routes
- Optimize images (WebP, proper sizing)
- Use production builds for testing
- Implement caching strategies
- Monitor bundle size

### Security Considerations
- Always use RLS policies
- Validate all user inputs
- Sanitize data before display
- Use environment variables for secrets
- Implement rate limiting

---

*This specification defines how Lovable Mode creates domain-specific optimization for React/Supabase development with three specialized sub-modes, comprehensive troubleshooting capabilities, and strategic Chat vs Default mode guidance for maximum development efficiency.*