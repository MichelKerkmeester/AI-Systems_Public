# Document Beautifier - Structure Templates v1.1.0

Template patterns and transformations for all document types.

## 📋 Table of Contents

1. [Template Overview](#1-template-overview)
2. [General Templates](#2-general-templates)
3. [Technical Templates](#3-technical-templates)
4. [Academic Templates](#4-academic-templates)
5. [Business Templates](#5-business-templates)
6. [Before & After Examples](#6-before--after-examples)
7. [Special Formats](#7-special-formats)
8. [Mixed Content Solutions](#8-mixed-content-solutions)

---

## 1. Template Overview

### Universal Base Pattern
```markdown
# Title
[Type | Date | Version]

## Table of Contents
## Summary/Overview
## Main Sections
## Conclusion/Next Steps
## Appendices/References
```

### Template Selection Process
1. **Ask for thinking rounds** (1-5)
2. **Linear thinking (1-3)**: Clear template structure
3. **Exploratory thinking (3-5)**: Multiple template options

---

## 2. General Templates

### Standard Report Pattern
**Structure:** Executive Summary → Introduction → Findings → Analysis → Recommendations → Conclusion
**Sections:** Use numbered headings (1, 1.1, 1.2)
**Required:** TOC, executive summary, key findings box, next steps
**Thinking:** 2-3 rounds typically sufficient

### How-To Guide Pattern
**Structure:** Overview → Prerequisites → Steps → Tips → Troubleshooting → Resources
**Format:** Numbered steps, tip callouts, troubleshooting table
**Required:** Time estimate, difficulty level, required tools list
**Thinking:** 1-2 rounds for clear guides

---

## 3. Technical Templates

### API Documentation Pattern
**Thinking:** User chooses (recommend 2-3 rounds)
**Structure:** Intro → Auth → Base URL → Endpoints → Errors → Rate Limits → Examples

**Endpoint Format:**
```markdown
### GET /resource
**Parameters:**
| Name | Type | Required | Description |
**Response:** JSON example
**Errors:** Status codes table
```

### Software Manual Pattern
**Thinking:** User chooses (recommend 2 rounds)
**Structure:** Requirements → Installation → Configuration → UI → Features → Troubleshooting
**Sections:** Platform-specific instructions, command examples, FAQ

---

## 4. Academic Templates

### Research Paper Pattern
**Thinking:** User chooses (recommend 2-3 rounds)
```markdown
## Abstract (150-250 words)
## 1. Introduction
   ### 1.1 Background
   ### 1.2 Problem Statement
   ### 1.3 Research Questions
## 2. Literature Review
## 3. Methodology
## 4. Results
## 5. Discussion
## 6. Conclusion
## References (APA/MLA/Chicago)
## Appendices
```

### Essay Pattern
**Structure:** Introduction (hook + thesis) → Body (3+ paragraphs) → Conclusion
**Format:** Topic sentences, evidence, analysis, transitions
**Required:** Thesis statement, works cited
**Thinking:** 2 rounds usually adequate

---

## 5. Business Templates

### Business Proposal Pattern
**Thinking:** User chooses (recommend 2-3 rounds)
```markdown
## Executive Summary
- Problem | Solution | Investment | ROI
## 1. Background
## 2. Proposed Solution
   | Component | Description | Benefit |
## 3. Implementation Plan
   Phase 1: Discovery → Phase 2: Development → Phase 3: Deployment
## 4. Investment & ROI
## 5. Why Choose Us
## 6. Next Steps
```

### Executive Memo Pattern
**Structure:** TO/FROM/DATE/RE → Purpose → Key Points → Recommendations → Next Steps
**Format:** Maximum 1 page, bullet points, action items
**Thinking:** 1-2 rounds for simple memos

---

## 6. Before & After Examples

### Wall of Text → Structured Report

**BEFORE:**
```
Our company has been experiencing issues with customer satisfaction 
over the past quarter response times increased from 2 to 8 hours 
support team overwhelmed with 500 tickets daily NPS dropped from 
72 to 45 we need to hire more staff...
```

**AFTER Pattern (with thinking):**
```markdown
System: How many thinking rounds should I use? (1-5)
(Recommend: 3 for restructuring)

User: 3 rounds

System: [Thinking: 3 rounds analyzing structure]

# Customer Support Crisis Analysis
*Internal Report | Q3 2024 | Priority: High*

## Executive Summary
[Key metrics in table: Response Time, Tickets, NPS]

## 1. Current Situation
### 1.1 Performance Metrics
[Data table]
### 1.2 Impact
[Bullet points: Customer, Team, Business]

## 2. Root Causes
[Numbered list]

## 3. Recommendations
### Immediate (Week 1)
### Short-term (Month 1)
### Long-term (Quarter)
```

### Random Notes → Meeting Minutes

**Pattern:** Date/Attendees → Topics (numbered) → Action Items (table) → Next Meeting
**Thinking:** 1-2 rounds for simple organization

---

## 7. Special Formats

### FAQ Pattern
```markdown
## Category Name
### Q: Question?
**A:** Answer in 2-3 sentences or bullet points
```
**Thinking:** 1 round for basic Q&A structure

### Tutorial Pattern
```markdown
## What You'll Learn
## Prerequisites  
## Lesson 1: Concept
- Objective
- Explanation
- Example
- Exercise
## Summary & Next Steps
```
**Thinking:** 2-3 rounds for educational structure

---

## 8. Mixed Content Solutions

### Hybrid Document Pattern
**Thinking:** User chooses (recommend 4-5 rounds)
```markdown
System: How many thinking rounds for this mixed content? (1-5)
(Complex mix suggests 4-5 rounds)

User: 5 rounds

System: [Thinking: 5 rounds exploring all patterns]

## Document Overview
**Primary Type:** [Main type]
**Secondary Elements:** [Other types]

## Part 1: [Type A Section]
[Use Type A template]

## Part 2: [Type B Section]  
[Use Type B template]

## Synthesis
[Unified conclusion]
```

### Progressive Complexity Pattern
```markdown
## 🟢 Level 1: Executive Summary (1 page)
## 🟡 Level 2: Standard Detail (3-5 pages)
## 🔴 Level 3: Technical Deep Dive (unlimited)
```
**Thinking:** 3-4 rounds to create layers

---

## Template Selection Matrix

| Length | Single Topic | Multiple Topics | Unknown |
|--------|--------------|-----------------|---------|
| <500 words | Quick format (1-2 rounds) | Basic sections (2-3 rounds) | Interactive (ask rounds) |
| 500-2000 | Standard template (2-3 rounds) | Section template (3-4 rounds) | Standard + TOC (ask rounds) |
| 2000-5000 | Full template (3 rounds) | Multi-part (4-5 rounds) | Deep restructure (ask rounds) |
| >5000 | Full + summary (3-4 rounds) | Part-based (5 rounds) | Interactive Deep (ask rounds) |

---

## 🎯 Quick Recognition

| Keywords | Template | Recommended Rounds |
|----------|----------|-------------------|
| "Abstract", "hypothesis" | Academic | 2-3 |
| "API", "function" | Technical | 2-3 |
| "ROI", "stakeholder" | Business | 2-3 |
| "Step 1", "How to" | Guide | 1-2 |
| Mixed indicators | Hybrid | 4-5 |

---

## 🤔 Thinking Integration

**Always Remember:**
1. Ask user for thinking rounds (1-5)
2. Provide recommendation based on complexity
3. Use specified rounds for analysis
4. Note rounds used in final output

**Exception:** Don't ask during discovery/requirements gathering

---

*Templates are patterns, not rigid rules. User-controlled thinking depth ensures the right template adaptation for each document.*