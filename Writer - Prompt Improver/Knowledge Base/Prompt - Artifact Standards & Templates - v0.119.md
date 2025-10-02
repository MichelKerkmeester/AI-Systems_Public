# Prompt - Artifact Standards & Templates - v0.119

Ultra-minimal artifact delivery standards for prompt engineering system with automatic DEPTH processing, MANDATORY artifact delivery, RCAF/CRAFT framework formatting, and single-line header only.

---

## 📋 Table of Contents

1. [🔴 CRITICAL REQUIREMENTS](#-critical-requirements)
2. [📦 DELIVERY STANDARDS](#-delivery-standards)
3. [📋 MANDATORY STRUCTURE](#-mandatory-structure)
4. [🎯 ARTIFACT TEMPLATE](#-artifact-template)
5. [✅ QUALITY CHECKLIST](#-quality-checklist)
6. [🚨 ERROR RECOVERY](#-error-recovery)
7. [💡 EXAMPLES](#-examples)

---

<a id="-critical-requirements"></a>

## 1. 🔴 CRITICAL REQUIREMENTS

### MANDATORY Artifact Delivery

**RULE #8 ENFORCEMENT:**
- **EVERY enhancement MUST be in artifact format**
- **NEVER deliver prompts in chat**
- **If artifact creation fails, STOP and retry**
- **Use `$retry` command if needed**

### MANDATORY Artifact Type

**RULE #10 ENFORCEMENT:**
- **ALWAYS use `text/markdown`**
- **NEVER use `text/plain`**
- **No exceptions allowed**

### MANDATORY Processing

**AUTOMATIC DEPTH:**
- **Standard mode: 10 rounds automatically applied**
- **Quick mode: 1-5 rounds auto-scaled by complexity**
  - Complexity 1-2: 1-2 rounds
  - Complexity 3-4: 3 rounds
  - Complexity 5-6: 4 rounds
  - Complexity 7+: 5 rounds
- **No user input required for processing depth**
- **Processing status shown in single-line header**

### MANDATORY Minimal Format

**ULTRA-MINIMAL STRUCTURE:**
- **ONLY single-line header + content**
- **NO Format Options section**
- **NO CLEAR Evaluation breakdown**
- **NO Processing Applied section**
- **NO additional metadata**

### Pre-Delivery Validation

```python
def validate_artifact_mandatory():
    """MANDATORY validation before any delivery"""
    
    checks = {
        'processing_applied': self.processing_depth > 0,
        'artifact_type': self.type == 'text/markdown',
        'artifact_created': self.artifact is not None,
        'clear_scored': self.clear_score >= 35,  # Minimum viable
        'clear_target': self.clear_score >= 40,  # Standard target
        'framework_identified': self.framework is not None,
        'only_header_and_content': self.has_no_extra_sections,
        'header_format': self.header_has_dollar_prefix
    }
    
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise ArtifactError(f"CANNOT DELIVER. Failed: {failed}")
        
    return True
```

---

<a id="-delivery-standards"></a>

## 2. 📦 DELIVERY STANDARDS

### Critical Requirements
**MANDATORY: Always use `text/markdown` artifact type for ALL prompt deliverables**

### Never:
- Use `text/plain` → Causes raw markdown display
- Deliver in chat → Violates Rule #8
- Mix artifact and response text
- Add Format Options section
- Add CLEAR Evaluation breakdown
- Add Processing Applied section
- Add any sections beyond header + content
- Use multi-line headers
- Place header at bottom
- Omit $ prefix from mode in header

### Always:
- **VERIFY artifact creation** → Retry if failed
- **Use proper `text/markdown` type** → No exceptions
- **Single-line header at TOP** → Only metadata with $ prefix
- **Content immediately follows** → No extra sections
- **NOTHING ELSE** → Ultra-minimal format

---

<a id="-mandatory-structure"></a>

## 3. 📋 MANDATORY STRUCTURE

### Ultra-Minimal Artifact Format

```markdown
Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50

[Enhanced prompt content in RCAF or CRAFT format]
```

### Structure Components (ONLY TWO)
1. **Single-line header** - Mode (with $ prefix), Complexity, Framework, CLEAR score
2. **Enhanced content** - The prompt itself

### CRITICAL: Nothing Else Allowed
- ❌ NO Format Options section
- ❌ NO CLEAR Evaluation breakdown
- ❌ NO Processing Applied section
- ❌ NO additional metadata
- ❌ NO dividers (except within content if needed)
- ❌ NO footers
- ❌ NO extra information

---

<a id="-artifact-template"></a>

## 4. 🎯 ARTIFACT TEMPLATE

### Complete Template

```markdown
Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50

[Enhanced prompt using RCAF or CRAFT framework]

Role: [If RCAF - specific expertise]
Context: [Essential background]
Action: [Clear measurable task]
Format: [Output requirements]
[Target: If CRAFT - success metrics]
```

### Header Components

| Component | Format | Example | Required |
|-----------|--------|---------|----------|
| **Mode** | `$[mode]` | `$improve` | Yes |
| **Complexity** | `Low/Medium/High` | `Medium` | Yes |
| **Framework** | `RCAF/CRAFT` | `RCAF` | Yes |
| **CLEAR** | `[X]/50` | `43/50` | Yes |

### Header Format Rules
- **Single line only**
- **Pipe separators** between components
- **$ prefix** for mode (e.g., $improve, $refine, $json)
- **No line breaks** in header
- **Exact format**: `Mode: $X | Complexity: Y | Framework: Z | CLEAR: A/50`

### CLEAR Score Guidelines

**CLEAR Scoring System:**
- Each dimension: 1-10 points
- 5 dimensions × 10 = 50 total possible
- DEPTH processing adds +1 per dimension = +5 total

**Score Hierarchy:**
| Range | Status | Interpretation | Action |
|-------|--------|----------------|--------|
| **45-50** | Excellent | 90%+ quality | Ship immediately |
| **40-44** | Standard Target | 80-88% quality | Minor polish only |
| **35-39** | Minimum Viable | 70-78% quality | Target weak areas |
| **30-34** | Below Target | 60-68% quality | Framework switch recommended |
| **<30** | Failing | <60% quality | Complete rewrite needed |

---

<a id="-quality-checklist"></a>

## 5. ✅ QUALITY CHECKLIST

### Artifact Requirements Checklist

- [✓] **MANDATORY: Artifact type is `text/markdown`**
- [✓] **MANDATORY: Delivered as artifact, not chat**
- [✓] **MANDATORY: Automatic processing applied**
- [✓] **MANDATORY: Single-line header at TOP**
- [✓] **MANDATORY: NO extra sections**
- [✓] **Header Format:** `Mode: $X | Complexity: Y | Framework: Z | CLEAR: A/50`
- [✓] **Mode has $ prefix:** $improve, $refine, $json, etc.
- [✓] **Content Only:** Enhanced prompt follows header
- [✓] **Framework Clear:** RCAF or CRAFT in header
- [✓] **CLEAR Score:** Shown in header, ≥40/50 target
- [✓] **NO Format Options section**
- [✓] **NO CLEAR breakdown section**
- [✓] **NO Processing section**
- [✓] **NO additional metadata**
- [✓] **Ultra-minimal:** Two components only

### Quality Gates

- [✓] **Processing applied:** Automatic depth used (10 standard, 1-5 quick)
- [✓] **Artifact created:** Not in chat
- [✓] **Type correct:** text/markdown
- [✓] **Header minimal:** Single line at top with $ prefix
- [✓] **No extra sections:** Content only
- [✓] **CLEAR ≥ 40/50:** Standard target met (80%+)
- [✓] **CLEAR ≥ 35/50:** Minimum viable met (70%+)
- [✓] **Expression ≥ 7/10:** Clear enough
- [✓] **Framework Fit:** Appropriate choice

---

<a id="-error-recovery"></a>

## 6. 🚨 ERROR RECOVERY

### Common Artifact Issues & Fixes

| Issue | Recognition | Fix | Impact |
|-------|------------|-----|--------|
| **Not artifact** | Chat delivery | Force artifact | CRITICAL |
| **Wrong type** | text/plain | Change to text/markdown | Display |
| **Extra sections** | Format Options, CLEAR breakdown, etc. | Remove all extras | Format |
| **Multi-line header** | Header spans multiple lines | Collapse to single line | Structure |
| **Missing header** | No metadata line | Add single-line header | Critical |
| **Header at bottom** | Misplaced | Move to top | Standards |
| **No $ prefix** | Mode without $ | Add $ prefix | Consistency |
| **No processing** | Missing status | Apply DEPTH | Quality |

### REPAIR Protocol for Artifacts

```markdown
**R** - Recognize: Extra sections identified
**E** - Explain: Violates ultra-minimal format
**P** - Propose: Remove all sections except header + content
**A** - Apply: Create proper minimal artifact
**I** - Iterate: Verify only header + content remain
**R** - Record: Note for future prevention
```

---

<a id="-examples"></a>

## 7. 💡 EXAMPLES

### Example 1: Perfect RCAF Artifact (Standard Format)

```markdown
Mode: $improve | Complexity: Medium | Framework: RCAF | CLEAR: 44/50

**Role:** Data scientist with machine learning expertise specializing in churn prediction.
**Context:** B2B SaaS platform with 10,000+ customers, 24-month historical data, 15% annual churn.
**Action:** Identify top 3 predictive factors for churn and recommend specific retention strategies.
**Format:** Executive report with visualizations and 3-5 actionable retention tactics.
```

### Example 2: YAML Format Artifact

```markdown
Mode: $yaml | Complexity: Medium | Framework: RCAF | CLEAR: 43/50

```yaml
role: UX designer specializing in mobile app onboarding
context: Banking app for ages 25-45, requiring KYC compliance, targeting <20% drop-off
action:
  primary: Design intuitive 5-minute onboarding flow
  requirements:
    - ensure regulatory compliance
    - minimize friction points
format:
  type: user_flow_diagram
  include:
    - screen descriptions
    - success metrics
    - drop-off analysis
```
```

### Example 3: JSON Format Artifact

```markdown
Mode: $json | Complexity: Low | Framework: RCAF | CLEAR: 41/50

```json
{
  "role": "Customer support specialist",
  "context": "E-commerce platform handling return requests",
  "action": "Process return request and provide clear next steps",
  "format": {
    "structure": "email_template",
    "requirements": ["3-step process", "friendly tone", "clear timeline"]
  }
}
```
```

### Example 4: Quick Mode Artifact

```markdown
Mode: $quick | Complexity: Low | Framework: RCAF | CLEAR: 38/50

**Role:** Customer support specialist
**Context:** E-commerce platform, handling return requests
**Action:** Process return request and provide clear next steps
**Format:** Email template with 3-step process
```

### Example 5: Complex CRAFT Artifact

```markdown
Mode: $refine | Complexity: High | Framework: CRAFT | CLEAR: 46/50

**Context:** Enterprise SaaS company launching new AI-powered analytics dashboard for Fortune 500 clients. Current onboarding takes 45 days, targeting 15-day reduction.
**Role:** Product manager with enterprise software expertise and change management background.
**Action:** Design comprehensive 30-day onboarding program including technical setup, team training, and adoption metrics tracking.
**Format:** Structured implementation plan with weekly milestones, resource allocation, and success metrics for each phase.
**Target:** Achieve 80% feature adoption within 30 days, reduce support tickets by 40%, maintain 95% client satisfaction score.
```

### CRITICAL: What These Examples Contain
1. ✔ Single-line header with $ prefix
2. ✔ Enhanced prompt content
3. ❌ NO Format Options section
4. ❌ NO CLEAR Evaluation breakdown
5. ❌ NO Processing Applied section
6. ❌ NO additional sections

---

## SUMMARY: Ultra-Minimal Format

**Every artifact contains EXACTLY:**
```
Mode: $[mode] | Complexity: [level] | Framework: [RCAF/CRAFT] | CLEAR: [X]/50

[Enhanced prompt content]
```

**Header Requirements:**
- Mode with $ prefix (e.g., $improve, $json)
- Complexity level (Low, Medium, High)
- Framework used (RCAF or CRAFT)
- CLEAR score out of 50 (target ≥40)

**CLEAR Score Targets:**
- Minimum viable: 35/50 (70%)
- Standard target: 40/50 (80%)
- Excellent: 45+/50 (90%+)

**Nothing more. Nothing less.**