# Artifacts, Templates & Examples - v0.310

**Comprehensive standards, templates, and examples** for delivering enhanced prompts via artifacts. Primary focus on NORMAL PROMPTS with AI Builder prompts as powerful secondary capability. Now with native Claude thinking integration.

## Table of Contents

### PART 1: NORMAL PROMPTS (Primary Focus)
1. [📦 ARTIFACT DELIVERY STANDARDS](#1--artifact-delivery-standards)
2. [🎯 MANDATORY ARTIFACT STRUCTURE](#2--mandatory-artifact-structure)
3. [📊 COMPACT OPTIMIZATION REPORT](#3--compact-optimization-report)
4. [🎨 MODE-SPECIFIC TEMPLATES](#4--mode-specific-templates)
5. [✅ QUALITY CHECKLIST](#5--quality-checklist)
6. [📚 NORMAL PROMPT EXAMPLES](#6--normal-prompt-examples)

### PART 2: AI BUILDER PROMPTS (Secondary Feature)
7. [📱 BUILDER MODE STANDARDS](#7--builder-mode-standards)
8. [💻 BUILDER TEMPLATES](#8--builder-templates)
9. [🌐 UNIVERSAL BUILDER EXAMPLES](#9--universal-builder-examples)
10. [🎯 SPECIAL CASES & COMBINATIONS](#10--special-cases--combinations)

---

# PART 1: NORMAL PROMPTS (Primary Focus)

## 1. 📦 ARTIFACT DELIVERY STANDARDS

**🚨 CRITICAL:** 
- Always use `text/markdown` artifact type when delivering enhanced prompts!
- NORMAL PROMPTS are the primary function of this system
- AI Builder prompts are a secondary capability for development platforms
- Always note thinking rounds used in report

Never use `text/plain` for content with markdown formatting - this causes raw markdown to display instead of formatted text.

### Artifact Type Rules:
**For Normal Prompts:**
- Direct, actionable instructions for AI
- Clear role, context, and deliverables
- Specific format and success criteria
- Note thinking rounds used

**For AI Builder Prompts:**
- Creative briefs with goals, not implementations
- Resource optimization strategies
- Platform-agnostic guidance
- Include thinking complexity

**If user's prompt seems unclear:** Use $interactive mode rather than guessing.

---

## 2. 🎯 MANDATORY ARTIFACT STRUCTURE

### For NORMAL Prompts (Most Common):

```
MODE USED: [$short/$improve/$refine/$interactive/$json]
THINKING ROUNDS: [X rounds used/requested by user]
ENHANCEMENT METHOD: [CRAFT/SPARK/Patterns/Full Framework]
COMPLEXITY LEVEL: [Simple/Medium/Complex]

[Enhanced prompt here - direct, actionable instructions]

---

[Optimization Report - if applicable]
```

### For AI BUILDER Prompts (When Detected):

```
MODE USED: [$prototype/$website/$app/$builder]
THINKING ROUNDS: [X rounds used/requested by user]
ENHANCEMENT METHOD: [VISION/CONVERT/SCALE/Universal Framework]
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM COMPATIBILITY: [Universal/Platform-Specific]

[Enhanced prompt here - creative brief with goals and phases]

---

[Optimization Report - including resource strategy]
```

---

## 3. 📊 COMPACT OPTIMIZATION REPORT

### Standard Report Format (Normal Prompts)
```
📊 Enhancement: X% ↗ | Mode: $[mode] | Thinking: X rounds

CRAFT Coverage: C:X% R:X% A:X% F:X% T:X%
Before → After: X words (X/10 clarity) → X words (X/10 clarity)

Key Improvements:
✔ [Improvement 1] • [Improvement 2]
✔ [Improvement 3] • [Improvement 4]
✔ [Additional improvements as needed]
```

### Builder Mode Additional Metrics
For Prototype/Website/App modes, add:
```
Platform Compatibility: Universal ✔
Resource Usage: [Low/Medium/High]
Resource Strategy: [Phased exploration approach]
Creative Freedom: [Areas for innovation]
Thinking Rounds: X (user requested)
Note: This is a creative brief for ANY AI platform
```

---

## 4. 🎨 MODE-SPECIFIC TEMPLATES

### 4.1 Normal Prompt Templates (Primary)

#### $short Mode Template
```
MODE USED: $short
THINKING ROUNDS: 2 (user requested)
ENHANCEMENT METHOD: Essential CRAFT
COMPLEXITY LEVEL: Simple

[1-3 sentence enhanced prompt with clear action and context]
```

#### $improve Mode Template (DEFAULT)
```
MODE USED: $improve
THINKING ROUNDS: 4 (auto recommendation accepted)
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium

As a [specific role], [action verb] [specific deliverable] for [target audience].

Context: [Background information]
Requirements: [Specific needs]
Format: [Structure and style]
Success criteria: [Measurable outcomes]

---

📊 Enhancement: X% ↗ | Mode: $improve | Thinking: 4 rounds

CRAFT Coverage: C:90% R:100% A:100% F:90% T:80%
Before → After: X words (X/10 clarity) → X words (9/10 clarity)

Key Improvements:
✔ Role defined • Context added
✔ Requirements specified • Format clarified
✔ Success metrics included • Audience identified
```

#### $refine Mode Template
```
MODE USED: $refine
THINKING ROUNDS: 7 (user requested)
ENHANCEMENT METHOD: Full 3-Phase Optimization
COMPLEXITY LEVEL: Complex

[Fully optimized prompt with comprehensive specifications]

---

📊 Enhancement: X% ↗ | Mode: $refine | Thinking: 7 rounds

CRAFT Coverage: C:100% R:100% A:100% F:100% T:100%
Before → After: X words (X/10 clarity) → X words (10/10 clarity)

Evaluation Score: X/175 (X%)
Phases Complete: ✔ SPARK Enhancement ✔ Full Evaluation ✔ Targeted Refinement

Key Improvements:
✔ Complete context • Clear expertise
✔ Detailed requirements • Specific format
✔ Measurable success • Edge cases handled
```

### 4.2 AI Builder Templates (Secondary)

#### $prototype Template (Universal)
```
MODE USED: $prototype
THINKING ROUNDS: 3 (user requested)
ENHANCEMENT METHOD: VISION Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM COMPATIBILITY: Universal

Create a PROMPT for exploring [concept description] on ANY AI platform:

EXPLORATION BRIEF:
Purpose: [What we're investigating]
Success: [What we'll learn or achieve]
Users should feel: [Emotional targets]

💰 RESOURCE OPTIMIZATION STRATEGY:

PHASE 1 - Concept Exploration (Minimal Resources):
- Explore different approaches to [core need]
- Test various patterns
- Focus on [primary goal]
- Use platform's native components

PHASE 2 - Enhancement (Moderate Resources):
- Build on successful patterns from Phase 1
- Add personality and polish
- Leverage platform features

PHASE 3 - Premium (High Resources - Needs Confirmation):
⚠️ The following will significantly increase resource usage:
- Complex features
- Advanced interactions
Ask: "Should we explore these premium features?"

CREATIVE DIRECTION:
- Mood: [Adjectives describing desired feel]
- Users should feel: [Emotional journey]
- Freedom to explore: [Areas for creativity]
- Platform strengths: Let each excel differently

SUCCESS CRITERIA:
- Users can: [Functional outcomes]
- Users feel: [Emotional outcomes]
- Works on: Bolt.new, MagicPatterns, v0, any AI platform

Note: This is a creative exploration brief for ANY platform

---

📊 Builder Enhancement Report | Thinking: 3 rounds

VISION Coverage: V:X% I:X% S:X% I:X% O:X% N:X%
Platform Compatibility: Universal
Resource Usage: Low-Medium
Creative Freedom: High

Key Optimizations:
✔ Goals defined • Platform-agnostic
✔ Mood established • Resource phasing
✔ Success criteria • Universal compatibility
```

---

## 5. ✅ QUALITY CHECKLIST

### For Normal Prompts (Primary):
- [ ] Clear role and expertise defined
- [ ] Specific action and deliverables
- [ ] Context and background provided
- [ ] Format and structure specified
- [ ] Success criteria measurable
- [ ] Thinking rounds noted
- [ ] Compact report included
- [ ] In markdown artifact
- [ ] Mode notation clear

### For AI Builder Prompts (Secondary):
- [ ] Creates creative brief, not implementation
- [ ] Goals and outcomes clear
- [ ] Resource phases defined
- [ ] Platform-agnostic language
- [ ] Success metrics included
- [ ] Creative freedom areas identified
- [ ] High-cost features flagged
- [ ] Universal compatibility noted
- [ ] Thinking rounds documented

---

## 6. 📚 NORMAL PROMPT EXAMPLES

### 6.1 Content Creation
**Before:** "write blog"

**User interaction:** "How many thinking rounds would you like me to use? (1-10, or 'auto' for my recommendation)"
**User:** "auto"
**System:** "I'll use 4 rounds for this standard content enhancement."

**After ($improve):**
```
MODE USED: $improve
THINKING ROUNDS: 4 (auto recommendation)
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium

As a technology journalist with expertise in AI and digital transformation, write a comprehensive 1,500-word blog post titled "The Hidden Costs of AI Implementation: What CTOs Need to Know."

CONTEXT:
You're writing for an audience of C-suite executives and IT decision-makers at Fortune 500 companies who are considering or currently implementing AI solutions. Recent surveys show 70% of AI projects fail to deliver expected ROI.

REQUIREMENTS:
- Open with a compelling statistic or case study
- Cover 5 hidden cost categories with real examples
- Include expert quotes from at least 2 industry leaders
- Provide actionable mitigation strategies for each cost
- End with a decision framework for AI investment

FORMAT:
- Executive summary (150 words)
- Introduction with hook (200 words)
- 5 main sections (250 words each)
- Conclusion with call-to-action (100 words)
- Sidebar: "Red Flags Checklist"

SUCCESS CRITERIA:
- Reader can identify potential hidden costs in their organization
- Provides specific, actionable next steps
- Balances caution with opportunity
- Citable by executives in board presentations

---

📊 Enhancement: 92% ↗ | Mode: $improve | Thinking: 4 rounds

CRAFT Coverage: C:100% R:100% A:95% F:100% T:90%
Before → After: 2 words → 198 words (9.5/10 clarity)

Key Improvements:
✔ Expert role established • Target audience defined
✔ Specific requirements listed • Clear structure provided
✔ Success metrics included • Context explained
```

### 6.2 Data Analysis
**Before:** "analyze sales data"

**User interaction:** "How many thinking rounds would you like me to use?"
**User:** "5"

**After ($improve):**
```
MODE USED: $improve
THINKING ROUNDS: 5 (user requested)
ENHANCEMENT METHOD: CRAFT + SPARK
COMPLEXITY LEVEL: Medium

As a senior data analyst specializing in e-commerce analytics and revenue optimization, conduct a comprehensive analysis of Q4 2024 sales data to identify growth opportunities for Q1 2025.

CONTEXT:
Analyzing 3 months of transaction data from an online retail platform with 50,000 SKUs across 12 categories. The company experienced 15% YoY growth but missed Q4 targets by 8%. Management needs actionable insights for the upcoming board meeting.

ANALYSIS REQUIREMENTS:
1. Segment performance by category, region, and customer cohort
2. Identify top 10 underperforming products with highest potential
3. Analyze seasonal patterns and predict Q1 demand
4. Calculate customer lifetime value by acquisition channel
5. Discover cross-selling opportunities using basket analysis

DELIVERABLES:
- Executive dashboard with 5 key metrics
- Detailed findings document (10-15 pages)
- Statistical significance for all insights (p < 0.05)
- Visualization package (15-20 charts)
- Recommendations matrix (effort vs. impact)

SUCCESS METRICS:
- Identify opportunities worth $2M+ in Q1 revenue
- Provide 5 immediately actionable recommendations
- All insights backed by statistical evidence
- Presentation ready for C-suite review

---

📊 Enhancement: 88% ↗ | Mode: $improve | Thinking: 5 rounds

CRAFT Coverage: C:95% R:100% A:100% F:95% T:100%
Before → After: 3 words → 187 words (9/10 clarity)

Key Improvements:
✔ Analyst expertise specified • Business context provided
✔ Analysis scope defined • Deliverables listed
✔ Statistical rigor required • Success metrics quantified
```

### 6.3 Problem Solving
**Before:** "fix performance issues"

**User interaction:** "How many thinking rounds for this complex problem?"
**User:** "8"

**After ($refine):**
```
MODE USED: $refine
THINKING ROUNDS: 8 (user requested)
ENHANCEMENT METHOD: Full 3-Phase Optimization
COMPLEXITY LEVEL: Complex

As a senior performance engineer with 10+ years optimizing high-traffic web applications, diagnose and provide a comprehensive remediation plan for critical performance degradation affecting our e-commerce platform's checkout flow.

PROBLEM CONTEXT:
Our React-based checkout process has degraded from 2-second load times to 8-12 seconds over the past month, resulting in a 35% increase in cart abandonment and $500K weekly revenue loss. The issue affects 100,000 daily users, peaks during flash sales, and particularly impacts mobile users (15-second load times). Recent changes include a new payment provider integration, expanded shipping calculator, and migration to microservices architecture.

DIAGNOSTIC SCOPE:
1. Frontend Performance Analysis
   - Bundle size and code splitting effectiveness
   - React component rendering optimization
   - Third-party script impact (analytics, chat, payments)
   - Memory leaks and garbage collection
   - Network waterfall and critical path

2. Backend Performance Investigation
   - API response times by endpoint
   - Database query performance
   - Microservices communication overhead
   - Cache hit rates and effectiveness
   - Payment gateway latency

3. Infrastructure Assessment
   - CDN configuration and cache headers
   - Load balancer health and distribution
   - Auto-scaling triggers and effectiveness
   - Database connection pooling
   - Redis/Memcached utilization

REQUIRED DELIVERABLES:
1. Root Cause Analysis Document
   - Performance timeline with degradation points
   - Bottleneck identification with data
   - Impact assessment by component
   - Evidence chain with metrics

2. Immediate Fixes (< 24 hours)
   - Quick wins with minimal risk
   - Expected improvement per fix
   - Implementation steps
   - Rollback procedures

3. Short-term Optimizations (1 week)
   - High-impact improvements
   - Resource requirements
   - Testing protocols
   - Performance benchmarks

4. Long-term Architecture Recommendations
   - Scalability improvements
   - Technology migrations if needed
   - Cost-benefit analysis
   - 6-month roadmap

SUCCESS CRITERIA:
- Checkout load time < 3 seconds (P95)
- Mobile performance < 5 seconds
- Support 2x current traffic
- Cart abandonment reduced to baseline (pre-issue)
- All fixes maintain backward compatibility
- Zero downtime during implementation

CONSTRAINTS:
- Budget: $50K for immediate fixes
- Team: 3 engineers available
- Timeline: Critical fixes within 48 hours
- Technology: Must maintain React/Node.js stack
- Compliance: PCI DSS standards must be maintained

---

📊 Enhancement: 96% ↗ | Mode: $refine | Thinking: 8 rounds

CRAFT Coverage: C:100% R:100% A:100% F:100% T:100%
Before → After: 3 words → 412 words (10/10 clarity)

Evaluation Score: 168/175 (96%)
Phases Complete: ✔ SPARK Enhancement ✔ Full Evaluation ✔ Targeted Refinement

Key Improvements:
✔ Complete problem context • Specific expertise defined
✔ Comprehensive diagnostic scope • Detailed deliverables
✔ Clear success metrics • Constraints acknowledged
✔ Prioritized approach • Risk mitigation included
```

---

# PART 2: AI BUILDER PROMPTS (Secondary Feature)

## 7. 📱 BUILDER MODE STANDARDS

### When to Use Builder Mode
- User mentions: Bolt.new, MagicPatterns, v0, Lovable, Cursor, Windsurf, Replit
- Keywords: build app, create website, design prototype, develop dashboard
- Context: AI-assisted development platforms

### Builder Mode Principles
- **Universal compatibility** - Works on ANY AI platform
- **Goals over specifications** - Define what, not how
- **Resource optimization** - Three-phase approach
- **Creative freedom** - Let AI explore solutions
- **Platform strengths** - Each platform excels differently
- **User-controlled thinking** - They choose depth

---

## 8. 💻 BUILDER TEMPLATES

### 8.1 Universal App Template ($app)
```
MODE USED: $app
THINKING ROUNDS: 5 (user requested)
ENHANCEMENT METHOD: SCALE Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM COMPATIBILITY: Universal

Create a PROMPT for developing [app type] application on ANY AI platform:

FUNCTIONAL BRIEF:
Core purpose: [what users accomplish]
Key workflows: [main user tasks]
Success criteria: [measurable outcomes]
Works on: Bolt.new, Cursor, Windsurf, Replit, any AI platform

💰 RESOURCE OPTIMIZATION:

PHASE 1 - MVP Core (Minimal Resources):
- Essential functionality only
- Basic user workflows
- Simple, effective interface
- Use platform's native components
- Free tier services where possible

PHASE 2 - Enhanced Experience (Moderate Resources):
- Improved workflows based on Phase 1
- Additional features users need
- Better user experience
- Platform-specific optimizations

PHASE 3 - Advanced Features (High Resources - Needs Confirmation):
⚠️ These will significantly increase resource usage:
- Complex integrations
- Real-time features
- Advanced analytics
Ask: "Should we add these premium features?"

USER EXPERIENCE GOALS:
- Users should feel: [emotions]
- Interface should be: [characteristics]
- Workflows should: [qualities]
- Success looks like: [outcomes]

PLATFORM FLEXIBILITY:
- Bolt.new: Leverage instant deployment
- Cursor/Windsurf: Focus on code quality
- Replit: Use collaborative features
- v0: Utilize shadcn/ui components
- Any platform: Optimize for strengths

Note: This is a requirements brief for ANY AI platform
```

### 8.2 Universal Website Template ($website)
```
MODE USED: $website
THINKING ROUNDS: 3 (auto recommendation)
ENHANCEMENT METHOD: CONVERT Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM COMPATIBILITY: Universal

Create a PROMPT for building [type] website on ANY AI platform:

STRATEGIC BRIEF:
Primary goal: [conversion/engagement metric]
Target audience: [user description]
Value proposition: [core message]
Compatible with: All AI website builders

💰 RESOURCE OPTIMIZATION:

PHASE 1 - Foundation (Minimal Resources):
- Core message and value
- Essential user pathways
- Mobile-responsive approach
- Platform templates/themes
- Basic SEO setup

PHASE 2 - Engagement (Moderate Resources):
- Interactive elements
- Enhanced user experience
- Trust-building features
- Platform-specific features
- Analytics integration

PHASE 3 - Premium (High Resources - Confirm First):
⚠️ High resource usage:
- Advanced integrations
- Custom animations
- A/B testing setup
- Enterprise features
Ask: "Implement premium features now?"

BRAND DIRECTION:
- Personality: [adjectives]
- Emotional impact: [desired feelings]
- Visual tone: [general direction]
- Creative freedom in: [design decisions]

SUCCESS METRICS:
- Conversion: [specific goals]
- Engagement: [measurable outcomes]
- Performance: [technical metrics]
- Works on: Any AI platform

Note: This is a strategic brief for ANY platform
```

### 8.3 Universal Prototype Template ($prototype)
```
MODE USED: $prototype
THINKING ROUNDS: 2 (user requested)
ENHANCEMENT METHOD: VISION Framework
COMPLEXITY LEVEL: [Simple/Medium/Complex]
PLATFORM COMPATIBILITY: Universal

Create a PROMPT for exploring [concept] on ANY AI platform:

EXPLORATION BRIEF:
Purpose: [What we're investigating]
Target users: [Who will use this]
Success: [What we'll learn/achieve]
Works on: MagicPatterns, v0, Bolt.new, any AI builder

💰 PHASED EXPLORATION:

PHASE 1 - Concept Testing (Minimal Resources):
- Explore various approaches
- Test different patterns
- Focus on core journey
- Use platform components
- Keep simple for testing

PHASE 2 - Enhance Winners (Moderate Resources):
- Build on successful concepts
- Add personality and delight
- Refine interactions
- Platform optimizations

PHASE 3 - Premium Polish (High Resources - If Justified):
- Advanced animations
- Complex interactions
- Multiple user flows
- Platform premium features

CREATIVE EXPLORATION:
- Experiment with: [design approaches]
- Consider: [user psychology]
- Explore: [visual metaphors]
- Freedom in: [all design decisions]

PLATFORM ADVANTAGES:
- MagicPatterns: Design-first exploration
- v0: Component-based approach
- Bolt.new: Instant preview
- Figma: Visual prototyping
- Any tool: Creative interpretation

Note: This is a concept exploration brief for ANY platform
```

---

## 9. 🌐 UNIVERSAL BUILDER EXAMPLES

### 9.1 Task Management App (Universal)
**Before:** "create todo app"

**User interaction:** "How many thinking rounds would you like for this app prompt?"
**User:** "6"

**After ($app - Universal):**
```
MODE USED: $app
THINKING ROUNDS: 6 (user requested)
ENHANCEMENT METHOD: SCALE Framework
COMPLEXITY LEVEL: Medium
PLATFORM COMPATIBILITY: Universal

Create a PROMPT for developing a team task management application on ANY AI platform:

FUNCTIONAL BRIEF:
Core purpose: Enable teams to organize, track, and complete work efficiently
Target users: Small teams (5-20 people) who need simple, effective task coordination
Success criteria: 50% reduction in missed deadlines, 80% daily active usage
Works on: Bolt.new, Cursor, Windsurf, Replit, v0, or any AI development platform

💰 RESOURCE OPTIMIZATION STRATEGY:

PHASE 1 - Essential MVP (Minimal Resources):
- Core task CRUD operations (create, read, update, delete)
- Simple project organization
- Basic user authentication
- Task assignment and due dates
- Mobile-responsive design
- Use platform's component library
- Deploy with platform's free tier
Goal: Validate core value proposition with minimal investment

PHASE 2 - Team Features (Moderate Resources):
Build on validated patterns:
- Real-time collaboration
- Comments and activity feeds
- File attachments
- Email notifications
- Calendar view
- Basic reporting
- Platform-specific integrations (Slack, etc.)
- Enhanced UI/UX based on user feedback
Goal: Achieve product-market fit

PHASE 3 - Advanced Platform (High Resources - Needs Confirmation):
⚠️ Significant resource investment required:
- AI-powered task suggestions
- Advanced analytics dashboard
- Custom workflows and automation
- Time tracking and billing
- API for third-party integrations
- White-label options
- Offline mode with sync
Ask: "Should we build these enterprise features now or after achieving 1000 users?"

USER EXPERIENCE GOALS:
- First use: Create first task in < 30 seconds
- Daily use: Feel organized and in control
- Team adoption: Everyone understands in 5 minutes
- Long-term: Becomes indispensable tool

PLATFORM-SPECIFIC OPTIMIZATIONS:
- Bolt.new: Use WebContainers for instant preview, deploy to Netlify
- Cursor/Windsurf: Implement with clean architecture, comprehensive testing
- Replit: Enable multiplayer collaboration, use Replit DB
- v0: Build with Next.js and shadcn/ui components
- Lovable: Optimize for credit efficiency with Supabase
- MagicPatterns: Start with Figma design system
- Any platform: Leverage native strengths

TECHNICAL FLEXIBILITY:
- Frontend: Platform's preferred framework (React, Vue, Svelte)
- Backend: Platform's optimal solution (Node, Python, Go)
- Database: Platform's recommendation (PostgreSQL, MongoDB, SQLite)
- Auth: Platform's auth system or Auth0/Supabase
- Hosting: Platform's deployment solution

SUCCESS METRICS:
- User activation: 80% create project within 2 minutes
- Retention: 60% weekly active after 1 month
- Performance: All actions < 200ms response
- Scalability: Support 10,000 concurrent users
- Cross-platform: Works on all modern browsers and devices

Note: This universal PROMPT adapts to ANY AI development platform while maintaining consistent quality and user experience goals.

---

📊 Builder Enhancement Report | Thinking: 6 rounds

SCALE Coverage: S:95% C:100% A:90% L:85% E:100%
Platform Compatibility: Universal ✔
Resource Strategy: Three-phase approach
Creative Freedom: High
Implementation Flexibility: Maximum

Key Optimizations:
✔ Platform-agnostic design • Phased resource approach
✔ Clear success metrics • Universal compatibility
✔ User experience focus • Technical flexibility
```

### 9.2 SaaS Marketing Website (Universal)
**Before:** "make landing page"

**User interaction:** "How many thinking rounds?"
**User:** "auto"
**System:** "I'll use 4 rounds for this website prompt."

**After ($website - Universal):**
```
MODE USED: $website
THINKING ROUNDS: 4 (auto recommendation)
ENHANCEMENT METHOD: CONVERT Framework
COMPLEXITY LEVEL: Medium
PLATFORM COMPATIBILITY: Universal

Create a PROMPT for building a high-converting SaaS marketing website on ANY AI platform:

STRATEGIC BRIEF:
Primary goal: Achieve 5% visitor-to-trial conversion rate
Target audience: SMB owners seeking productivity solutions
Value proposition: "Cut administrative work by 70% with AI automation"
Compatible with: Bolt.new, WordPress, Webflow, Framer, v0, any website builder

💰 RESOURCE OPTIMIZATION STRATEGY:

PHASE 1 - Conversion Foundation (Minimal Resources):
- Hero section with clear value proposition
- Problem/solution narrative
- 3 key benefits with icons
- Simple pricing table
- Email capture with lead magnet
- Mobile-first responsive design
- Use platform's best template
- Basic analytics setup
Investment: Minimal, focus on message clarity

PHASE 2 - Trust & Engagement (Moderate Resources):
- Customer testimonials section
- Case studies (3-5)
- Interactive product demo
- Comparison chart vs competitors
- FAQ section
- Blog with 10 SEO articles
- Chat widget integration
- A/B testing setup
Investment: Moderate, optimize conversion

PHASE 3 - Full Marketing Platform (High Resources - Confirm):
⚠️ Requires significant resources:
- Personalization engine
- Marketing automation
- Advanced analytics dashboard
- Multi-language support
- Custom illustrations/animations
- Video testimonials
- Webinar system
- Partner portal
Ask: "Build complete platform now or after product-market fit?"

CONVERSION PSYCHOLOGY:
- First 3 seconds: Clear value proposition visible
- First 10 seconds: Problem resonates with visitor
- First 30 seconds: Solution seems achievable
- First minute: Trust established through social proof
- Call-to-action: Multiple, clear, non-threatening

CREATIVE DIRECTION:
- Mood: Professional yet approachable
- Colors: Trust-building (blues/greens) with energetic accents
- Typography: Clean, modern, highly readable
- Imagery: Real people, authentic situations
- Motion: Subtle, purposeful, performance-conscious

PLATFORM OPTIMIZATIONS:
- Bolt.new: Full-stack with integrated backend
- Webflow: Visual design with CMS
- WordPress: SEO-optimized with plugins
- Framer: Interactive animations
- v0: Next.js with server components
- MagicPatterns: Component-first approach
- Any platform: Use native strengths

SUCCESS METRICS:
- Conversion rate: 5% visitor to trial
- Page load: < 2 seconds
- Bounce rate: < 40%
- SEO: First page for 10 keywords
- Mobile score: > 95 PageSpeed

Note: This universal website PROMPT creates a conversion-focused marketing site on ANY platform.

---

📊 Website Enhancement Report | Thinking: 4 rounds

CONVERT Coverage: C:100% O:95% N:90% V:100% E:95% R:90% T:100%
Platform Compatibility: Universal ✔
Resource Usage: Phased approach
Conversion Focus: High
Creative Freedom: Maintained

Key Optimizations:
✔ Clear conversion goals • Platform flexibility
✔ Psychological triggers • Resource phases
✔ Trust elements • Universal approach
```

---

## 10. 🎯 SPECIAL CASES & COMBINATIONS

### 10.1 Normal + Builder Hybrid
When user wants both prompt improvement AND building:
```
MODE USED: $improve + $builder
THINKING ROUNDS: 5 (user requested)
ENHANCEMENT METHOD: CRAFT + SCALE
COMPLEXITY LEVEL: Complex
DUAL PURPOSE: Prompt Enhancement + Builder Brief

PART 1 - ENHANCED PROMPT:
As a [role], create [specific deliverable] that [achieves goal].
[Standard prompt enhancement following CRAFT]

PART 2 - BUILDER IMPLEMENTATION:
If implementing on an AI platform, consider:
- Phase 1: [Minimal resource approach]
- Phase 2: [Enhanced features]
- Phase 3: [Premium additions]
- Platform flexibility: Works on any AI builder

Note: Part 1 is the primary prompt, Part 2 enables AI platform implementation
```

### 10.2 Platform Auto-Detection
When platform keywords detected:
```
Platform: [Detected platform] ✔
Auto-detected from: [keywords that triggered]
Approach: Universal builder brief
Compatibility: All platforms supported
Thinking rounds: [User preference]
```

### 10.3 Budget-Conscious Request
When user emphasizes minimal resources:
```
💰 BUDGET-CONSCIOUS APPROACH:
Phase 1 Only Implementation
- Core functionality only
- Simplest effective solutions
- Platform free tiers
- No premium features
- Defer all enhancements
- Thinking: Minimal rounds (1-2)

Success with constraints:
- Still achieves: [primary goal]
- Users still feel: [core emotion]
- Value delivered: [essential benefit]
```

### 10.4 Mode Combinations
When modes are combined:
```
MODE USED: $improve + $interactive + $builder
Thinking: Variable (ask at each stage)
Approach: Guided enhancement with builder capability
Process: Interactive questions → Enhanced prompt → Builder brief
Output: Complete prompt with implementation guidance
```

### 10.5 Clarification Needed
When intent is unclear:
```
CLARIFICATION NEEDED:
Your request could be interpreted as:
1. A normal prompt for [specific task]
2. A builder prompt for [AI platform development]

For normal prompt: I'll enhance with role, context, and deliverables
For builder prompt: I'll create a creative brief with resource phases

Which would you prefer?
How many thinking rounds should I use? (1-10, or 'auto')
```

---

## Final Quality Standards

### Universal Principles
✅ Normal prompts are the PRIMARY function
✅ Builder prompts are SECONDARY capability
✅ Always ask for thinking rounds preference
✅ Document thinking rounds used
✅ Maintain platform neutrality
✅ Include resource optimization
✅ Preserve creative freedom
✅ Use appropriate frameworks
✅ Deliver in proper artifact format

### Hierarchy Reminder
1. **First Priority**: Normal prompt enhancement (direct AI instructions)
2. **Second Priority**: Builder prompts (creative briefs for AI platforms)
3. **Always Clear**: Which type is being delivered
4. **User Choice**: Let user specify when unclear
5. **Thinking Control**: User decides complexity depth

---

*Remember: This system PRIMARILY creates enhanced prompts for AI interactions. The builder capability is a powerful SECONDARY feature for AI development platforms. Always