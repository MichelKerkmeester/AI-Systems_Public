# Product Designer - Design & Product Intelligence v0.210

## Table of Contents
1. [🎯 STRATEGIC USAGE GUIDE](#1-strategic-usage-guide)
2. [🔍 MANDATORY WEB VERIFICATION](#2-mandatory-web-verification)
3. [🌍 DESIGN INDUSTRY LANDSCAPE 2025](#3-design-industry-landscape-2025)
4. [🎯 MARKET REALITY & OPPORTUNITIES](#4-market-reality-opportunities)
5. [💶 ECONOMICS & COMPENSATION](#5-economics-compensation)
6. [🧠 PSYCHOLOGY & PAIN POINTS](#6-psychology-pain-points)
7. [📊 TRUST & PROCESS BUILDING](#7-trust-process-building)
8. [🔄 VERIFICATION & FALLBACK PROTOCOL](#8-verification-fallback-protocol)

---

## 1. 🎯 STRATEGIC USAGE GUIDE

### When to Reference This Document

**ACTIVELY USE when user requests:**
- Tool comparisons and market share
- Salary and compensation data (ALL IN EUR)
- Design process and methodologies
- Team structure and ratios
- Industry statistics and trends
- Career path information
- ROI and business impact

### ⚠️ CRITICAL REQUIREMENT
**EVERY data point from this document MUST be web verified before use in content**
**ALL monetary values MUST be in EUR**

### Simplified Trigger Keywords:

| **Keyword** | **Primary Stat** | **Web Search Query** | **Interactive Question** |
|------------|-----------------|---------------------|------------------------|
| "tools/figma" | Figma 72% share | "design tool market share 2024 2025" | "Focus on dominance or alternatives?" |
| "salary/compensation" | €120-180K range | "product designer salary europe 2024" | "Range or specific level?" |
| "process/methodology" | Design thinking adoption | "design methodology usage 2024" | "One method or comparison?" |
| "team/ratio" | 1:8 designer-dev | "designer developer ratio 2024" | "Ideal or typical setup?" |
| "roi/impact" | 31% measure ROI | "design roi measurement statistics" | "Problem or solution focus?" |

---

## 2. 🔍 MANDATORY WEB VERIFICATION

### Verification Protocol for Each Data Point

**CRITICAL:** NEVER use any statistic without web verification first

#### Core Stats Verification Table (EUR STANDARDIZED)

| **Statistic** | **Current Value** | **Search Query** | **Update Frequency** | **Fallback if Not Found** |
|--------------|------------------|------------------|---------------------|-------------------------|
| Figma share | 72% | "figma market share 2024 2025" | Quarterly | "leading tool" |
| Sketch share | 8% | "sketch market share 2024" | Quarterly | "declining share" |
| Designer salary | €120-180K mid-level | "product designer salary europe 2024" | Monthly | "competitive range" |
| Dev ratio | 1:8 | "designer developer ratio optimal" | Annual | "typical ratio" |
| ROI measurement | 31% | "design roi measurement percentage" | Annual | "minority measure" |
| System adoption | 52% | "design system adoption rate 2024" | Quarterly | "growing adoption" |
| Career timeline | 3-5 years | "designer career progression years" | Annual | "several years" |
| Tool cost | €15-20/month | "figma pricing europe 2024" | Monthly | "affordable pricing" |

#### Verification & Fallback Process
```python
def verify_before_use(stat_type: str, stored_value: any) -> tuple:
    """Always verify before using in copy"""
    
    # Step 1: Execute web search
    search_result = web_search(verification_queries[stat_type])
    
    # Step 2: Parse and compare
    current_value = parse_search_result(search_result)
    
    # Step 3: Decision logic
    if current_value and significant_change(stored_value, current_value):
        # Use updated value
        value_to_use = current_value
        verification_note = f"Updated from {stored_value} to {current_value}"
    elif current_value:
        # Confirmed still accurate
        value_to_use = stored_value
        verification_note = "Verified current"
    else:
        # Use fallback language (no specific numbers)
        value_to_use = fallback_language[stat_type]
        verification_note = "Using general language"
    
    # Step 4: Convert to EUR if currency
    if is_currency(value_to_use) and not in_eur(value_to_use):
        value_to_use = convert_to_eur(value_to_use)
    
    return value_to_use, verification_note
```

---

## 3. 🌍 DESIGN INDUSTRY LANDSCAPE 2025

### The Design Maturity Reality [VERIFY BEFORE USE]

**SEARCH REQUIRED:** "design maturity levels 2024 2025 statistics"

Most companies are still figuring this out. About 68% are at Level 2-3 maturity (basically they have designers but not great processes). Only 12% have really nailed it (Level 4-5). The rest (20%) are still treating design like decoration.

**Market Reality [VERIFY EACH - EUR VALUES]:**
- Teams usually have 1 designer for every 8 developers [SEARCH: "designer developer ratio 2024"]
- Figma basically owns everything now – 72% use it [SEARCH: "figma market share statistics"]
- About half have design systems (52%, up from 38%) [SEARCH: "design system adoption percentage"]
- Only 31% actually measure if design works [SEARCH: "companies measuring design ROI"]
- Takes about 3 tries before shipping anything [SEARCH: "average design iterations to ship"]

**Tool Consolidation [VERIFY TRENDS - EUR PRICING]:**
- **Figma**: €15-20/month professional [SEARCH: "figma pricing europe 2024"]
- **Adobe XD**: Dead (discontinued 2024) [SEARCH: "adobe xd discontinued"]
- **Sketch**: €10-15/month [SEARCH: "sketch pricing europe"]
- **Framer**: €20-25/month [SEARCH: "framer pricing europe"]

**Geographic Distribution [EUR STANDARDIZED]:**
- **Europe**: €120-180K for mid-level [SEARCH: "designer salary europe 2024"]
- **Remote**: Only 28% fully remote now [SEARCH: "remote design jobs percentage"]
- **Hybrid**: 67% doing the 2-3 days office thing [SEARCH: "hybrid work design teams"]
- **Technical premium**: Know code? Add €20-30K [SEARCH: "designer code premium salary europe"]

---

## 4. 🎯 MARKET REALITY & OPPORTUNITIES

### What's Actually Happening [VERIFY QUARTERLY]

**Hiring Reality [SEARCH: "design job market statistics europe 2024"]:**
- 300+ people apply for every design job
- 71% of roles want 5+ years experience
- About half get placed within 3 months
- Portfolio beats degree every time

**Process Evolution [SEARCH: "design process trends 2024"]:**
- Double Diamond still going strong (45%)
- Continuous Discovery catching on (32%)
- Lean UX stable at 23%
- Most sprints are 2 weeks
- 3 iterations is totally normal

### The Opportunity Gaps (EUR VALUES)

| Gap | Size | Solution | Copy Hook | Verify Search |
|-----|------|----------|-----------|---------------|
| **ROI Measurement** | 69% can't measure | Clear metrics framework | "Show €200K saved" | "design roi measurement gap" |
| **Tool Overload** | Average 7 tools | Consolidation strategy | "€150/month in tools" | "designer tool costs europe" |
| **Stakeholder Buy-in** | 58% struggle | Process documentation | "Get people on board" | "design stakeholder alignment" |

---

## 5. 💶 ECONOMICS & COMPENSATION

### The Salary Truth (EUR STANDARDIZED) [VERIFY BEFORE EVERY USE]

**What Designers Actually Earn in Europe [SEARCH EACH]:**
```
Junior (0-2 years):      €70-110K
                        [SEARCH: "junior designer salary europe 2024"]
             
Mid (3-5 years):         €120-180K (the sweet spot)
                        [SEARCH: "mid level designer salary europe 2024"]
             
Senior (5-8 years):      €180-250K
                        [SEARCH: "senior designer salary europe 2024"]
             
Staff/Principal (8+):    €250-350K+
                        [SEARCH: "staff designer salary europe 2024"]

Technical premium:       +€20-30K (if you code)
                        [SEARCH: "designer coding premium europe"]
             
Remote penalty:          -10-20% (office pays more)
                        [SEARCH: "remote design salary difference europe"]
```

**Cost Per Outcome (What Companies Think) [EUR - CALCULATE FROM SEARCHES]:**
- Average designer costs €150-200K all-in
- Does 8-12 projects per year
- Each project costs €15-25K
- Takes 2-3 sprints to ship
- ROI breakeven usually 6 months

### ROI Reality (EUR VALUES) [VERIFY STATISTICS]
- Design-driven companies supposedly outperform by 228% [SEARCH: "design driven company performance"]
- But only 31% of teams actually measure this [SEARCH: "design roi measurement percentage"]
- Average payback is 6 months [SEARCH: "design investment payback period"]
- Support tickets can drop 30-78% with good UX [SEARCH: "ux support ticket reduction"]
- Savings typically €200K+ annually [SEARCH: "design system roi europe"]

### Career Path Economics (EUR) [VERIFY ANNUALLY]
- Junior to Mid: 2-3 years typical, +€50K [SEARCH: "designer career progression europe"]
- Mid to Senior: 3-5 years average, +€60K [SEARCH: "senior designer requirements europe"]
- Senior to Staff: 3-4 years, +€70K [SEARCH: "staff designer salary progression europe"]
- Freelance rates: €400-1500/day [SEARCH: "freelance designer daily rates europe 2024"]

---

## 6. 🧠 PSYCHOLOGY & PAIN POINTS

### Designer Psychology [VERIFY TRENDS]

**Fear Drivers [SEARCH FOR VALIDATION]:**
- Imposter syndrome: 68% of us feel fake [SEARCH: "designer imposter syndrome statistics"]
- Tool anxiety: New tool every 18 months [SEARCH: "design tool lifecycle"]
- Career uncertainty: Nobody knows the path [SEARCH: "design career path uncertainty"]
- AI replacement: 45% genuinely worried [SEARCH: "designers ai replacement fear"]

**Motivation Drivers (What Actually Matters):**
- Impact visibility: Seeing users succeed
- Team collaboration: Working well together
- Skill growth: Always learning something
- Recognition: Getting credit for work
- Salary growth: €120K → €180K progression

---

## 7. 📊 TRUST & PROCESS BUILDING

### Trust Builders (Ranked by Impact)

1. **Process transparency** – "Here's how many tries it took"
2. **Team collaboration** – "Sarah figured this out, not me"
3. **Real examples** – "When we redesigned checkout..."
4. **Failure acknowledgment** – "First version was terrible"
5. **Clear documentation** – "Why we chose this approach"
6. **Continuous improvement** – "Still tweaking this"
7. **Measurable outcomes** – "€50K saved monthly"

### The Four Process Pillars [VERIFY SUPPORTING DATA]

| Pillar | Reality | Approach | Copy Hook | Verify Search |
|--------|---------|----------|-----------|---------------|
| **Discovery** | 42% skip research | User interviews mandatory | "Talk to actual users" | "design research skip rate" |
| **Definition** | Unclear problems | Problem before solution | "Know what you're solving" | "problem definition design" |
| **Development** | Linear process | Iterative cycles | "Takes a few rounds" | "iterative design process" |
| **Delivery** | Handoff issues | Continuous collaboration | "Work together always" | "design handoff problems" |

---

## 8. 🔄 VERIFICATION & FALLBACK PROTOCOL

### Fallback Language When Verification Fails

| **Stat Type** | **Specific Claim** | **Fallback Language** |
|--------------|-------------------|----------------------|
| Market share | "72% use Figma" | "The majority use Figma" |
| Salary | "€120-180K" | "Competitive compensation" |
| Ratios | "1:8 ratio" | "Typical team structure" |
| Percentages | "31% measure ROI" | "Most don't measure ROI" |
| Costs | "€200K saved" | "Significant savings" |
| Timeline | "3 iterations" | "Multiple iterations" |

### Verification Status Documentation

**Always include in minimal footer:**
- When stats verified: `Stats: 3 verified`
- When using fallback: `Stats: general language used`
- When mixed: `Stats: 2 verified, 1 general`

### Priority Order for Stats

1. **Verified current data** (from web search)
2. **General language** (when verification fails)
3. **Never use unverified specific numbers**

---

## 🎯 QUICK REFERENCE BANK

### The Five Stats That Matter Most [VERIFY BEFORE EACH USE - EUR]
1. **Figma 72% market share** – Tool dominance [SEARCH: "figma market share 2024"]
2. **€120-180K salary range** – Compensation reality [SEARCH: "product designer salary europe 2024"]
3. **1:8 designer-dev ratio** – Team structure [SEARCH: "designer developer ratio"]
4. **31% measure design ROI** – Impact tracking [SEARCH: "design roi measurement"]
5. **3 iterations average** – Process reality [SEARCH: "design iteration average"]

### Copy Output Requirements
- **ALL monetary values in EUR**
- **Verify before claiming any specific percentage**
- **Use fallback language when verification fails**
- **Document verification status in footer**
- **3 versions per group for 1-30 words**
- **2 versions per group for 31-150 words**
- **1 version per group for 151+ words**