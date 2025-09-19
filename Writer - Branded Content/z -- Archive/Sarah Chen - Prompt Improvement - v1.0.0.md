# Sarah Chen - Prompt Improvement - v1.0.0

**Lightweight request clarity enhancement** for marketing content creation systems. This document contains all rules, patterns, and examples for improving marketing request clarity without adding context or assumptions.

## Table of Contents

1. [🎯 Core Principles](#1--core-principles)
2. [📝 Enhancement Rules](#2--enhancement-rules)
3. [📤 Marketing Abbreviation Dictionary](#3--marketing-abbreviation-dictionary)
4. [🔄 Structure Patterns](#4--structure-patterns)
5. [✅ Enhancement Examples](#5--enhancement-examples)
6. [❌ What NOT to Do](#6--what-not-to-do)
7. [🚦 Bypass Conditions](#7--bypass-conditions)
8. [📊 Quality Metrics](#8--quality-metrics)

---

## 1. 🎯 Core Principles

The Marketing Request Clarity Enhancement layer follows these immutable principles:

1. **Clarity Only**: Improve structure and phrasing, never add marketing context
2. **Preserve Intent**: All original keywords and meaning must remain
3. **No Assumptions**: Never infer campaign type, audience, or marketing goals
4. **Invisible Process**: Marketer should be unaware of enhancement
5. **Mode Integrity**: All marketing mode commands remain untouched

**Remember**: This is NOT about making marketing requests "better" - it's about making them clearer while preserving exactly what the marketer asked for.

---

## 2. 📝 Enhancement Rules

### Rule 1: Expand Abbreviations
Only expand from the approved dictionary (Section 3). Never guess at abbreviations not in the list.

### Rule 2: Structure Vague Starters
Apply approved patterns (Section 4) to improve request structure without changing meaning.

### Rule 3: Preserve Keywords
Every word from the original request must appear in the enhanced version (except replaced abbreviations).

### Rule 4: Minimal Additions
Only add grammatical connectors when absolutely necessary:
- "about", "for", "with", "regarding"
- Never add marketing descriptors or campaign context

### Rule 5: Grammar Only
Fix only grammatical issues that impede clarity. Don't improve marketing style or strategy.

### Rule 6: Preserve Failure Language
Keep authentic marketing language like "tanked", "failed", "flopped" - these carry important context.

---

## 3. 📤 Marketing Abbreviation Dictionary

### Marketing Channels & Platforms
```yaml
Social Media:
  IG: Instagram
  FB: Facebook
  TT: TikTok
  YT: YouTube
  LI: LinkedIn
  TW: Twitter
  SC: Snapchat

Marketing Terms:
  DM: direct message
  CTR: click-through rate
  CPA: cost per acquisition
  ROI: return on investment
  KPI: key performance indicator
  B2B: business to business
  B2C: business to consumer
  
Campaign Types:
  PPC: pay-per-click
  SEO: search engine optimization
  SEM: search engine marketing
  PR: public relations
  
Marketing Specific:
  ABM: account-based marketing
  MQL: marketing qualified lead
  SQL: sales qualified lead
  CRM: customer relationship management
  UGC: user-generated content
  CTA: call to action
  LTV: lifetime value
  AOV: average order value
  CAC: customer acquisition cost
```

**Note**: Only expand abbreviations in this exact list. All others remain unchanged.

---

## 4. 🔄 Structure Patterns

### Vague Starter Transformations
Apply these exact patterns when detected:

```yaml
General Patterns:
  "need campaign": "create campaign"
  "want marketing": "create marketing"
  "fix campaign": "revise campaign"
  "campaign help": "create campaign"
  "marketing stuff": "create marketing content"
  
Problem Patterns:
  "campaign failed": "revise failed campaign"
  "campaign tanked": "revise tanked campaign"  # preserve "tanked"
  "X not working": "fix X issue"
  "low CTR": "improve click-through rate"
  
Request Patterns:
  "something viral": "create viral content"
  "need engagement": "create engagement content"
  "want conversions": "create conversion content"
  "boost X": "improve X"
```

### Preserve Marketing Context
When applying patterns, preserve ALL marketing context and emotion:
- "urgently need campaign" → "urgently create campaign"
- "campaign totally tanked" → "revise campaign that totally tanked"
- "viral TT campaign" → "create viral TikTok campaign"
- "B2B ABM strategy" → "create business to business account-based marketing strategy"

---

## 5. ✅ Enhancement Examples

### Category 1: Simple Abbreviations
```
"IG campaign" → "Instagram campaign"
"improve CTR" → "improve click-through rate"
"B2B marketing" → "business to business marketing"
"check ROI" → "check return on investment"
"ABM strategy" → "account-based marketing strategy"
```

### Category 2: Vague Structures
```
"need campaign" → "create campaign"
"marketing help" → "create marketing"
"something viral" → "create viral content"
"fix conversion" → "revise conversion"
"campaign stuff" → "create campaign content"
```

### Category 3: Combined Issues
```
"need IG campaign" → "create Instagram campaign"
"fix B2B CTR" → "revise business to business click-through rate"
"urgent ABM help" → "urgent create account-based marketing"
"boost FB engagement" → "improve Facebook engagement"
```

### Category 4: Preserved Failures
```
"campaign totally tanked" → "revise campaign that totally tanked"
"strategy failed hard" → "revise strategy that failed hard"
"ads flopped" → "revise ads that flopped"
```

### Category 5: No Change Needed
```
"create Instagram campaign for product launch" → (no change)
"develop email marketing strategy" → (no change)
"$marketing urgent campaign brief" → (no change - mode command)
```

---

## 6. ❌ What NOT to Do

### Never Add Marketing Context
```
❌ "need campaign" → "create social media marketing campaign"
   (Added channel assumption)

❌ "fix CTR" → "optimize click-through rate for better conversions"
   (Added goal assumption)

❌ "B2B strategy" → "create enterprise B2B lead generation strategy"
   (Added audience and purpose assumptions)
```

### Never Add Marketing Descriptors
```
❌ "make campaign" → "create engaging campaign"
   (Added quality descriptor)

❌ "write email" → "write conversion-focused email"
   (Added goal descriptor)

❌ "need content" → "create high-performing content"
   (Added performance descriptor)
```

### Never Change Marketing Intent
```
❌ "test campaign" → "optimize campaign"
   (Changed from testing to optimizing)

❌ "explore strategy" → "implement strategy"
   (Changed from exploration to implementation)

❌ "campaign failed" → "campaign underperformed"
   (Softened the failure language)
```

### Never Remove Emotion/Authenticity
```
❌ "campaign totally tanked" → "campaign needs revision"
   (Lost emotional context)

❌ "desperately need help" → "need assistance"
   (Lost urgency)
```

---

## 7. 🚦 Bypass Conditions

Skip enhancement entirely when:

### 1. **Already Clear**
- Contains proper marketing structure
- Has clear campaign/marketing verbs
- Over 20 words with details

### 2. **Mode Commands**
- Contains $marketing, $campaign, $email, $social
- Mode overrides need for enhancement

### 3. **Detailed Briefs**
- Contains campaign objectives
- Has target audience specified
- Includes metrics or KPIs

### 4. **External References**
- Campaign names or IDs
- Client/brand mentions
- Specific campaign dates

### 5. **Platform Specific**
- Already mentions "Instagram post", "Facebook ad", etc.
- Contains platform-specific features

---

## 8. 📊 Quality Metrics

### Internal Scoring (Not Shown to User)

**Clarity Triggers (enhance if 2+ present):**
- [ ] Contains vague starter (-2 points)
- [ ] Has marketing abbreviations (-1 point each)
- [ ] Lacks clear action verb (-2 points)
- [ ] Under 5 words (-1 point)
- [ ] Missing structure (-1 point)

**Enhancement Success Metrics:**
- Processing time: <0.5 seconds
- Original keywords preserved: 100%
- Context additions: 0
- Marketing assumptions: 0
- Emotion/authenticity preserved: 100%
- User awareness: None

### Pre/Post Examples with Scores

```
"need IG campaign" 
- Score: 3/10 (vague starter, abbreviation, too short)
- Enhanced: "create Instagram campaign"
- New Score: 8/10 (clear verb, expanded, structured)

"urgently fix B2B ABM that totally tanked"
- Score: 5/10 (abbreviations, but has urgency and emotion)
- Enhanced: "urgently revise business to business account-based marketing that totally tanked"
- New Score: 9/10 (preserved everything, just expanded abbreviations)

"develop comprehensive social media marketing strategy for Q4"
- Score: 9/10 (already clear)
- Enhanced: (no change needed)
- New Score: 9/10
```

---

## Implementation Notes

### Integration Point
This enhancement layer operates BEFORE any marketing mode processing, immediately after request intake.

### Process Flow
1. Marketing request enters system
2. Clarity check
3. If unclear, apply enhancements
4. Pass enhanced request to marketing mode
5. Continue normal marketing flow

### Testing Checklist
Before deployment, verify:
- [ ] All marketing abbreviations expand correctly
- [ ] Vague starters transform properly
- [ ] Original keywords always preserved
- [ ] No marketing context ever added
- [ ] Emotion and failure language preserved
- [ ] Bypass conditions work
- [ ] Mode commands unaffected

---

## Common Issues & Solutions

### Issue: Lost Marketing Emotion
**Solution**: Always preserve words like "tanked", "failed", "urgently", "desperately"

### Issue: Added Campaign Assumptions
**Solution**: Never add channel, audience, or goal assumptions

### Issue: Over-Enhancement
**Solution**: When in doubt, preserve original

---

## Success Indicators

### Quantitative
- 30-40% reduction in clarification questions
- 100% keyword preservation
- 100% emotion preservation
- 0 context additions
- <0.5s processing time

### Qualitative
- Marketers unaware of enhancement
- Authentic voice preserved
- Failed campaigns stay "failed"
- Urgency maintained
- Natural flow to marketing modes

---

*Remember: The goal is clarity without assumption. Preserve the marketer's authentic voice, including their failures and frustrations. When in doubt, preserve the original. Less enhancement is better than wrong enhancement.*