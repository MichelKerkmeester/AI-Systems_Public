(rework this, almost no relevant knowledge) # Content - Design & Product Intelligence - v0.112

## Table of Contents
1. [🎯 Strategic Usage Guide](#1-🎯-strategic-usage-guide)
2. [🌐 Industry Landscape 2025](#2-🌐-industry-landscape-2025)
3. [🔧 Current Methodologies](#3-🔧-current-methodologies)
4. [📊 Design Principles & Systems](#4-📊-design-principles--systems)
5. [💡 Product Strategy](#5-💡-product-strategy)
6. [🎨 Collaboration Models](#6-🎨-collaboration-models)
7. [🛠 Tool Ecosystem](#7-🛠-tool-ecosystem)
8. [📈 Success Metrics](#8-📈-success-metrics)
9. [📝 Content Formulas](#9-📝-content-formulas)
10. [🧠 DEPTH Intelligence Integration](#10-🧠-depth-intelligence-integration)
11. [📄 Historical Context Intelligence](#11-📄-historical-context-intelligence)

---

## 1. 🎯 STRATEGIC USAGE GUIDE

### When to Reference This Document

- **CRITICAL:** All knowledge depths and angles always available
- **BETA FEATURE:** System searches conversation history for knowledge usage patterns

**USE when writing about:**
- The convergence of design and development roles
- Current state of the design job market
- AI's impact on design workflows
- Design systems and token adoption
- Technical skills designers now need
- Salary ranges and compensation data
- Tool ecosystem changes (Figma dominance, etc.)
- Remote work realities in tech

**DEPTH Integration with Historical Context:**
```python
async def check_intelligence_need(request, depth_phase):
    """Check if knowledge needed with historical context"""
    
    # Get historical knowledge usage
    history = await conversation_search(
        query="design principles methodology industry",
        max_results=5
    )
    
    historical_note = ""
    if history:
        usage = analyze_knowledge_usage(history)
        historical_note = f"[Previously used: {usage['common_topics']}]"
    
    if depth_phase == 'Process':
        # Often pull intelligence during Process phase
        return True, historical_note
    elif 'design engineer' in request or 'AI tools' in request:
        return True, historical_note  # High relevance 2025 topics
    elif 'methodology' in request:
        return True, historical_note
    elif thinking_rounds >= 5:
        # Complex requests likely need context
        return True, historical_note
    return False, historical_note
```

### Trigger Keywords with Context Awareness:
- "design engineer" → Pull role evolution + salary data → **Context: Show usage history**
- "technical skills" → React/TypeScript requirements → **Challenge: "One key skill enough?"**  
- "AI tools" → Usage stats + trust levels → **Historical: Display previous uses**
- "design systems" → Token adoption rates → **Challenge: "Skip to the stat?"**
- "job market" → Placement rates + competition → **Context: Note urgency preference**

### Historical Context Display:
```python
async def get_knowledge_history():
    """See how knowledge was used before"""
    history = await conversation_search(
        query="design principles methodology industry",
        max_results=5
    )
    
    if history:
        return {
            'knowledge_depth': analyze_depth_preference(history),
            'topics_used': extract_knowledge_topics(history),
            'show_as': 'helpful_context',
            'all_depths': 'always_available'
        }
```

---

## 2. 🌐 INDUSTRY LANDSCAPE 2025

### The Great Convergence 

Traditional boundaries between design and development have dissolved (mostly). Design engineers now command $200-240K base salaries at companies like Vercel, Linear, and Stripe, with total compensation reaching $300K+ at senior levels.

**Market Reality:**
- Only 49.5% of designers find roles within 3 months (down from 67.9% in 2019)
- Less than 5% of companies hiring entry-level talent
- 95% of design job listings require React proficiency
- 85% require TypeScript knowledge
- 80% require design system experience
- 52% of postings no longer require degrees - skills matter more

[Historical Context: Track which stats create urgency in copy]
[All statistics available for use]

**Role Evolution:**
- **Design Engineers**: Bridge aesthetic sensibility with technical implementation. Work across branding, marketing, product, and design systems. The "engineering of visuals" per GitHub.
- **Traditional Designers**: Must rapidly add technical skills or risk obsolescence. Pure design roles becoming increasingly rare.
- **Product Designers**: Now expected to understand code, not just design. The days of "throwing designs over the wall" seem to be over.

### AI Integration Reality

74% of product teams use AI for user research and design tasks, but only 32% fully trust AI output (interesting gap there). AI seems to augment rather than replace human creativity:
- 58% efficiency improvement in workflows
- 57% faster turnaround times
- 300+ user responses analyzed in under 2 days
- $50M annual savings at companies like Lumen

[Historical Context: Note trust vs efficiency messaging preference]
[All angles remain available]

### Spatial Computing Emergence

AR/VR has moved from experimental to production-ready with Apple Vision Pro and Meta Quest 3. Real implementations include BMW training environments, Sheba Medical Center clinical interfaces, and collaborative design reviews at scale.

---

## 3. 🔧 CURRENT METHODOLOGIES

### What Teams Actually Use

**Lean UX (Most Common)**
Build-Measure-Learn cycles with teams under 10 people. Focus on outcomes over outputs. Most successful when combined with continuous discovery habits.

**Continuous Discovery**  
Weekly customer touchpoints, assumption mapping, opportunity solution trees, rapid experimentation cycles. Teresa Torres' methods becoming industry standard (or so it seems).

**Modified Design Sprints**
Traditional 5-day sprints compressed to 2-3 days. Remote-first facilitation, integrated into existing development cycles rather than standalone events.

**AI-Assisted Research**
Automated transcription, theme identification, dynamic follow-ups. Teams process 10x more user feedback but require human oversight for interpretation.

### The Reality Check
- Design Thinking: Usually non-linear in practice, not the neat diagram
- Agile: Rarely pure, almost always hybrid with waterfall elements
- Sprints: Days 4-5 often cut due to resource constraints
- Lean UX: "Measure" phase frequently skipped under pressure

[Challenge: "Just say 'test weekly'?" - Show acceptance history]
[All methodologies available for reference]

---

## 4. 📊 DESIGN PRINCIPLES & SYSTEMS

### Design System Evolution 2025 

**Token Adoption:**
84% of organizations use design tokens (up from 56% in 2024). Three-tier architecture:
- Primitive tokens: Basic brand values
- Semantic tokens: Contextual usage (e.g., `--p-bg-surface`)
- Component tokens: Theme customization

**Organizational Models:**
- 79% have dedicated design system teams
- 68% use hybrid governance (centralized control + distributed contribution)
- Success requires stable systems built over time with responsive feedback loops

**Industry Leaders:**
- Shopify Polaris: Semantic token naming excellence
- IBM Carbon: Multi-framework support
- Material Design 3: Expressive version with enhanced personalization

[Historical Context: Display technical depth tolerance in token discussion]
[All detail levels available]

### Core Design Principles That Still Seem to Matter
- Visual hierarchy guides attention (though stakeholder preferences often break it)
- Consistency reduces cognitive load (but must balance with innovation)
- Progressive disclosure for complex features (users often can't find hidden items though)
- Constraints breed creativity (teams perform better with limitations)

---

## 5. 💡 PRODUCT STRATEGY

### Strategy in the AI Era

**What We're Noticing:**
- AI integration is table stakes, not a differentiator
- Human + AI collaboration beats either alone
- Strategic thinking, emotional intelligence remain human domains
- Rapid prototyping now 10x faster with AI tools

**Growth Sectors 2025:**
- Government tech (UK hiring 2,500 roles)
- Healthcare digital transformation
- Financial services modernization
- Climate tech and sustainability

**Prioritization Evolution:**
Impact vs Effort remains the practical standard. RICE scores create false precision (we think). Most teams default to simpler "Must/Should/Could" frameworks.

[Challenge: "Skip frameworks, just ship?" - Context dependent]
[All frameworks available for discussion]

---

## 6. 🎨 COLLABORATION MODELS

### Design Engineer Workflows

**Three Primary Models:**
1. **Design Collaboration**: Designers sketch, design engineers implement in code. No handoff friction.
2. **Embedded Teams**: Design engineers join product teams for extended features.
3. **Independent Ownership**: Design engineers own design-led projects end-to-end.

[Historical Context: Note which model resonates with team structure]
[All models available for reference]

### Remote Work Reality 2025
- 53% require 3+ office days per week (up from 37%)
- Only 7% fully remote positions (down from 21%)
- 60% of workers prefer hybrid arrangements
- 40% would accept 5% pay cut for flexibility
- Geographic salary differences persist despite remote options

---

## 7. 🛠 TOOL ECOSYSTEM

### Current Landscape

**Design Tools:**
- Figma: 90%+ market share, comprehensive AI suite (First Draft, Magic Content, Visual Search)
- Figma 2025: Make (code generation), Sites (direct publishing)
- Sketch: Declining rapidly
- Adobe XD: Discontinued

**AI Design Tools:**
- Uizard: Multi-screen prototypes in 2 minutes
- Galileo: High-fidelity designs with Figma export
- Relume: Complete websites from descriptions
- Maze: AI-powered user research at scale

**Development Bridge:**
- GitHub Copilot: Model Context Protocol for design specs
- Storybook: Component development standard
- Design tokens: W3C standard progressing

**Spatial Tools:**
- Reality Composer Pro (Apple)
- Gravity Sketch (cross-platform)
- WebXR (browser-based)

[Challenge: "Just use Figma + Copilot?" - Show historical responses]
[All tools available for mention]

---

## 8. 📈 SUCCESS METRICS

### What Teams Measure

**AI Impact:**
- 58% efficiency improvement
- 57% faster turnaround
- 10x data processing capacity
- ROI measured in millions saved

**Design System Success:**
- 2.7x better outcomes with consistent tokens
- 5x brand perception improvement
- Adoption rates across teams
- Component reuse metrics

**Business Reality:**
Leading indicators (engagement) predict success better than lagging indicators (revenue). Focus on outcomes (user behavior) over outputs (designs delivered) - at least that's what seems to work.

---

## 9. 📝 CONTENT FORMULAS

### Patterns That Seem Effective for 2025

**Convergence Story:**
"Design and code aren't separate at [company]. Their design engineers [specific role/achievement], resulting in [measurable outcome]."

**AI Balance:**
"We use AI for [specific task]. It's [X]% faster but requires [human oversight aspect]. Our trust level: [honest assessment]."

**Market Reality:**
"The market demands [specific skills]. Without [capability], [consequence]. Here's how we're adapting: [actionable steps]."

**Process Transparency:**
"We tried [approach]. Failed because [reason]. Pivoted to [solution]. Result: [outcome]."

**Tool Decision:**
"Evaluated [options]. Chose [tool] because [specific reason]. Trade-off: [what we gave up]."

### Writing Guidelines

**Try to Include:**
- Specific companies and examples
- Real numbers and timeframes  
- Honest trade-offs
- Next steps

**Try to Avoid:**
- "Best practices" (say "what worked for us")
- "Obviously" (say "we discovered")
- "Should always" (say "consider trying")
- Perfect processes (show the messy reality)

---

## 10. 🧠 DEPTH INTELLIGENCE INTEGRATION

### When to Use Which Content with Historical Context

```python
async def scale_intelligence(thinking_rounds):
    """Scale intelligence with historical context"""
    
    # Get historical depth preference
    history = await recent_chats(n=5)
    historical_depth = "varies"
    
    if history:
        historical_depth = analyze_depth_preference(history)
    
    if rounds <= 2:
        suggestion = 'single_key_stat'  # "Design engineers earn $200K+"
    elif rounds <= 5:
        suggestion = '2-3_key_trends'  # Convergence + AI + market reality
    elif rounds <= 7:
        suggestion = 'comprehensive_context'  # Full landscape
    else:
        suggestion = 'full_positioning'
    
    return f"""
    Suggested depth: {suggestion}
    [Historical preference: {historical_depth}]
    All depths available - your choice?
    """
```

### DEPTH Phase Guidance with Context

**D - Discover:**
- Simple market facts
- Single role description
- One key stat
[Historical: Show previous discover depth]

**E - Explore:** 
- Add methodology context
- Include reality checks
- Show evolution
[Historical: Note exploration patterns]

**P - Process:**
- Full competitive landscape
- Complete tool ecosystem
- Detailed workflows
[Historical: Display process preferences]

**T - Test:**
- Case studies with metrics
- Multi-company examples
- Industry transformation
[Historical: Show test usage]

**H - Help:**
- Ongoing trends
- Future predictions
- Continuous learning needs
[Historical: Note help patterns]

---

## 11. 📄 HISTORICAL CONTEXT INTELLIGENCE

### Session Intelligence Display

```python
async def display_intelligence_context():
    """Display how knowledge has been used"""
    
    history = await conversation_search(
        query="industry landscape methodology principles",
        max_results=10
    )
    
    if history:
        patterns = analyze_intelligence_usage(history)
        return f"""
        Historical knowledge context:
        - Convergence messaging: Used {patterns['convergence']} times
        - Market urgency: Emphasized {patterns['urgency']} times  
        - AI pragmatism: Balanced {patterns['ai_balance']} times
        - Tool simplification: Suggested {patterns['tool_simple']} times
        - Reality checks: Included {patterns['reality']} times
        
        All knowledge angles remain available.
        """
    return "No historical knowledge usage detected yet."
```

### Context-Aware Knowledge Selection
```python
async def suggest_knowledge_depth():
    """Suggest but don't determine knowledge depth"""
    
    history = await recent_chats(n=5)
    
    if history:
        depth_patterns = analyze_knowledge_usage(history)
        print(f"""
        **Knowledge depth options (all available):**
        - Light (key principle only) [Used {depth_patterns['light']} times]
        - Medium (2-3 concepts) [Used {depth_patterns['medium']} times]
        - Heavy (full methodology) [Used {depth_patterns['heavy']} times]
        
        **Your preference?**
        """)
```

### Messages with Historical Context (All Available):
1. "$200K+ for design engineers" - Creates urgency [Usage noted]
2. "95% of jobs require React" - Clear skill need [Frequency shown]
3. "Only 32% trust AI fully" - Balanced perspective [Balance tracked]
4. "84% use design tokens" - Industry standard [Adoption shown]
5. "7% fully remote" - Market reality [Reality noted]

### Progressive Context Enhancement

| Sessions | Context Level | Display Type | User Control |
|----------|--------------|--------------|--------------|
| 1-2 | Building | None yet | 100% |
| 3-4 | Light | "Previously used X" | 100% |
| 5-6 | Medium | "Common topics: Y" | 100% |
| 7+ | Rich | Full usage patterns | 100% |

### Knowledge Application Examples

**With minimal context (early sessions):**
```
Using industry knowledge: Design engineers now earn $200K+
[No historical context yet]
All knowledge depths available
```

**With rich context (later sessions):**
```
Using industry knowledge: Design engineers now earn $200K+
[Historical: Salary data used 3 times, creates urgency]
[Common angle: Market reality (5 uses)]
[Typical depth: Medium detail]
All knowledge options remain available for selection
```

### Artifact Details Format
When including intelligence in artifacts, always use:

```markdown
---

**AI System:**

- **Framework:** [Name]
- **Mode:** $[mode]
- **Tone:** $[tone]

---

- **Thinking:** [User selected 1-10]
- **DEPTH:** [Phases used]

---

- **Challenge:** [Applied/Not applied]
- **Platform:** [If specified]
- **Context:** [Use case]

---

**Historical Context:**
- Knowledge usage patterns shown
- Previous intelligence topics noted
- All depths always available

**Knowledge angle:** [Industry insight/methodology/principle used]
```

---

*The 2025 reality (as we see it): Design and development converged. AI augments but doesn't replace. Technical skills are non-negotiable. The market is brutal but rewards those who adapt. Historical context enriches knowledge selection without restricting options. Challenge complexity when simpler works. Display what's been used before. Success seems to come from embracing both code and creativity, backed by systems thinking and continuous learning. All knowledge depths and angles remain available regardless of patterns. AI System header always appears above artifact details. Still figuring this out together.*