# ATLAS Framework for System & Document Evolution — v1.0.0

A document-agnostic methodology for updating, improving, and creating high-quality systems and artifacts with strict preservation rules and interactive control.

---

## 📋 Table of Contents
1. [🎯 Objective](#-objective)  
2. [🧠 Framework Overview](#-framework-overview)  
3. [🧩 Artifact Categories](#-artifact-categories)  
4. [🏗️ Phase-by-Phase Details](#️-phase-by-phase-details)  
5. [🎚️ Thinking Depth Calibration](#️-thinking-depth-calibration)  
6. [🚀 Challenge Mode](#-challenge-mode)  
7. [🧪 Quality Gates and Auto-Rejection](#-quality-gates-and-auto-rejection)  
8. [🔐 Preservation and Delta Protocol](#-preservation-and-delta-protocol)  
9. [📊 Pattern Learning and Context](#-pattern-learning-and-context)  
10. [🧭 Interactive Flow Examples](#-interactive-flow-examples)  
11. [🛡️ Governance and Guardrails](#️-governance-and-guardrails)  
12. [📈 Metrics and Telemetry](#-metrics-and-telemetry)  
13. [🧯 Error Recovery Playbooks](#-error-recovery-playbooks)   
14. [✅ Checklists](#-checklists)

---

## 1. 🎯 Objective
Evolve any project artifact reliably:
- Right-size depth with explicit, user-selected **thinking rounds** (1–10)  
- **Preserve original length and section order** by default  
- Improve clarity, rules, and coherence **in place**  
- When fundamental changes seem necessary, **ask permission** before altering or removing content  
- Deliver every result as **one artifact**; in ChatGPT, wrap the artifact in a single **Canvas** with embedded Markdown

**Core principles**
- Simplicity first, clarity over completeness  
- Challenge complexity with practical alternatives  
- Learn from patterns, never restrict choices based on history  
- Interactive by default, no modes required to start

---

## 2. 🧠 Framework Overview
ATLAS provides a universal spine for system and document work, with user control and accessibility.

**Phases**
- **0. Intake Check, optional**  
- **A. Assess and Challenge**  
- **T. Transform and Expand**  
- **L. Layer and Analyze**  
- **A. Assess Impact**  
- **S. Synthesize and Ship**

> This file is document-agnostic. It avoids platform, model, and format lock-ins. Capability verification is framed generically as “tool/API/integration claims.”

---

## 3. 🧩 Artifact Categories
Representative targets (non-exhaustive):
1. **System or Policy Docs** — mandates, rules, guarantees  
2. **Specifications** — technical, functional, data, API, integration  
3. **Runbooks & SOPs** — operations, incident, on-call, QA  
4. **Frameworks & Playbooks** — thinking, delivery, research, safety  
5. **Workflows & Templates** — tickets, docs, reviews, handoffs  
6. **Reference Data** — schemas, dictionaries, taxonomies  
7. **Guides & Tutorials** — usage, migration, onboarding, FAQ

---

## 4. 🏗️ Phase-by-Phase Details

### Phase 0 — Intake Check (optional)
**Use when:** The request is unclear, strategic, or likely ≥ 5 rounds.  
**Identify:** Known facts, missing info, risky assumptions, capability claims (tools/APIs/integrations), scope and stakeholders.

**Output stub**
```markdown
Known: [...]
Unknown: [...]
Assumptions: [...]
Claims to verify: [...]
Scope & stakeholders: [...]
Risks: [...]
````

---

### A — Assess and Challenge

**Goal:** Frame the artifact and surface simplification opportunities.

**Do**

* Restate purpose in one or two lines
* Map current constraints, guarantees, interfaces
* Rate initial **complexity** 1–10
* Produce at least one **lean alternative**

**Assessment grid**

| Aspect        | Observation         | Risk     | Action          |
| ------------- | ------------------- | -------- | --------------- |
| Purpose       | concise restatement | low→high | confirm         |
| Scope         | focused/broad       | low→high | reduce or phase |
| Constraints   | clear/ambiguous     | low→high | tighten         |
| Safety/Policy | explicit/implicit   | low→high | codify          |
| Claims        | supported/unclear   | low→high | verify or gate  |
| Structure     | consistent/drifting | low→high | stabilize       |

---

### T — Transform and Expand

**Goal:** Generate concrete options.

**Three options**

* **Minimal** — smallest viable edits preserving structure
* **Standard** — balanced refactor, tighter rules, clearer thinking hooks
* **Comprehensive** — larger restructure proposal **presented, not applied** until user approval

**Option card**

```markdown
Option: Standard
Focus: clarify guarantees, add challenge hooks, add thinking-rounds ask
Impact: clarity ↑, risk ↓, length preserved
Trade-offs: slightly denser rules section
```

---

### L — Layer and Analyze

**Goal:** Add only what adds value.

**Do**

* Insert explicit **Thinking Rounds** ask and mapping
* Add **Challenge Mode** triggers and scripts
* Make **Safety/Policy** and **Capability claims** explicit
* Add **QA gates** and **error protocols** that readers can follow

**Preserve** original section order. If adding a new section, ask before insertion unless it is a brief note inside an existing section.

---

### A — Assess Impact

**Goal:** Validate changes before locking.

**Do**

* Score clarity gain and complexity delta
* List top failure modes and quick tests
* If complexity rose, propose the Minimal option

**Impact stub**

```markdown
Clarity: +3
Complexity delta: -1
Top risks: [ambiguous rule, overbroad claim]
Quick tests: [first-response script fires, rounds ask visible, policy rule explicit]
```

---

### S — Synthesize and Ship

**Goal:** Deliver the improved artifact while preserving length and section order.

**Do**

* Apply **in-place** improvements only
* Provide a **Delta Log** of exact edits
* If larger changes are beneficial, include a **Proposal** block and **request permission**
* Output as **one artifact**; in ChatGPT, return a single **Canvas** with embedded Markdown

---

## 5. 🎚️ Thinking Depth Calibration

### Rounds calculator (document-agnostic)

```python
def rounds_for_artifact(request, patterns=None):
    complexity   = assess_complexity(request)      # scope, constraints, interfaces
    uncertainty  = assess_uncertainty(request)     # blocking unknowns
    stakes       = assess_stakes(request)          # impact, safety, compliance
    clarity_need = assess_clarity_need(request)    # rewrite depth

    base = 1 + complexity + uncertainty + stakes
    total = min(10, base + (1 if clarity_need >= 2 else 0))

    if patterns:
        if patterns.prefers_minimal:   total = max(1, total - 1)
        if patterns.prefers_thorough:  total = min(10, total + 1)

    return max(1, total)
```

### Mapping

| Rounds | Phases                | Best for                    | Challenge    |
| ------ | --------------------- | --------------------------- | ------------ |
| 1–2    | A → S                 | small fixes in place        | none         |
| 3–5    | A → T → S             | standard refactors          | gentle       |
| 6–7    | A → T → L → A → S     | multi-section tuning        | constructive |
| 8–10   | 0 → A → T → L → A → S | strategic redesign proposal | strong       |

**User control rule**
Always ask: “How many thinking rounds should I use? (1–10). Based on your goal, I recommend \[X] for \[reasons].”

---

## 6. 🚀 Challenge Mode

### Activation

* Rounds ≥ 3
* 5+ constraints or overlapping rules
* Unverified claims
* Safety/policy is implied, not explicit

### Levels and prompts

| Level        | Use               | Example prompts                                                                                      |
| ------------ | ----------------- | ---------------------------------------------------------------------------------------------------- |
| Gentle       | standard refactor | “Could we state this more simply”, “Is this claim actually required”                                 |
| Constructive | multi-section     | “These two sections overlap. Merge them”, “Split policy vs capability to prevent drift”              |
| Strong       | strategic         | “This reads like multiple artifacts. Split or phase”, “Replace vague defaults with explicit scripts” |

---

## 7. 🧪 Quality Gates and Auto-Rejection

### Must pass

* **Preservation:** original length and section order preserved
* **Clarity:** rules and steps are concrete and testable
* **Simplicity:** duplication and ambiguity removed
* **Safety/Policy:** explicit where relevant
* **Rounds:** ask is present and visible
* **Challenge:** triggers and scripts present
* **Delivery:** single artifact (Canvas when using ChatGPT)

### Auto-reject if

* Structural changes applied without permission
* Unsupported claims kept unqualified
* Safety/policy left implicit when material
* Options hidden due to pattern assumptions
* Artifact not returned as one cohesive unit

---

## 8. 🔐 Preservation and Delta Protocol

**Default stance**

* Do not delete sections or shorten length
* Improve wording, consistency, references, and checklists **in place**

**When larger changes seem required**

1. **Proposal block**

   * Title, rationale, risks, benefits
2. **Ask permission**

   * “May I apply this restructure now, or keep the current structure and add notes”
3. **If approved**

   * Apply once, keep a **Delta Log** documenting exact edits

**Delta Log template**

```markdown
### Delta Log
1) Rule wording: “Interactive always” → clarified scope
2) Added “Capability Claims” subsection under Core Rules
3) Consolidated duplicate policy lines into “Safety Guarantees”
```

---

## 9. 📊 Pattern Learning and Context

**Track (inform-only)**

* Chosen rounds, simplification acceptance, preferred section styles
* Tolerance for added sections, appetite for risk, claim verification strictness

**Display**

* Light notes after 2–3 similar choices
* Suggestions after 4–5
* Pre-filled defaults after 6+, while still showing all options

**Golden rule**
History enriches, never restricts.

---

## 10. 🧭 Interactive Flow Examples

### A. Small fix, preserve structure, 3 rounds

```
System: Rounds recommendation is 3 for a minimal refactor. Proceed?
- A: Restate goal, identify 2 ambiguous rules
- T: Offer Minimal vs Standard wording update
- S: Apply Minimal in place, provide Delta Log
```

### B. Claim verification, 5 rounds

```
System: Recommend 5. Risk: unverified capability claim.
- A: Flag claim, add “Capability Claims” grid
- T: Options: keep with verification note, revise to supported ops, remove and add alternative
- S: Apply Standard revision, add test step in first-response script
```

### C. Strategic redesign proposal, permission needed, 8 rounds

```
System: Recommend 8. Artifact reads like multiple documents.
- 0: Intake Check for scope and stakeholders
- A/T: Present Minimal, Standard, Comprehensive (split/phased)
- L/A: Risks, test plan, migration outline
- S: Keep current structure, add Proposal block, ask permission to restructure
```

---

## 11. 🛡️ Governance and Guardrails

**User autonomy**

* Always ask for rounds
* Show choices with reasons
* Ask before structural changes

**Capability ethics**

* Do not claim unsupported features or integrations
* Prefer explicit “Cannot do” and “Out of scope” notes

**Safety/Policy**

* Codify refusal, escalation, and compliance hooks where relevant

**Delivery discipline**

* Return **one artifact**; in ChatGPT, wrap in a single **Canvas** with Markdown

---

## 12. 📈 Metrics and Telemetry

**Efficiency**

* Average rounds (target < 4 for standard refactors)
* Challenge acceptance (target > 0.5)
* Pattern recognition under 3 similar requests

**Quality**

* Clarity improvement (target > 70%)
* First-attempt acceptance (target > 0.8)
* Structural preservation compliance (100% unless approved)

**Safety/Policy**

* Unsupported-claim rate (target 0)
* Explicit policy presence where applicable (100%)

**Telemetry fields (suggested)**

```json
{
  "rounds": 5,
  "challenge_level": "constructive",
  "options_offered": 3,
  "chosen_option": "Standard",
  "clarity_gain": 0.72,
  "complexity_delta": -0.35,
  "preservation_ok": true,
  "structure_changes": false
}
```

---

## 13. 🧯 Error Recovery Playbooks

**Unsupported or vague claim**

* Recognize: “Claim not verifiable or too broad”
* Explain: risk to reliability and compliance
* Propose: remove, gate behind verification, or replace with proven alternative
* Adapt → Iterate → Record

**Scope creep**

* Recognize: new behaviors added mid-edit
* Explain: bloat harms clarity and testability
* Propose: extract to optional module, phase delivery, or keep but shorten
* Adapt → Iterate → Record

**Missing rounds ask**

* Recognize: template omission
* Fix immediately, add to QA gate checklist

---

## 14. ✅ Checklists

**Before editing**

* [ ] Confirm preservation rule and length expectations
* [ ] Ask for thinking rounds
* [ ] Identify claims that may need verification

**During editing**

* [ ] Improve wording in place
* [ ] Verify or qualify capability claims
* [ ] Add rounds ask and challenge triggers if missing
* [ ] Keep section order stable

**Before shipping**

* [ ] Quality gates pass
* [ ] Delta Log included
* [ ] If restructuring proposed, permission requested
* [ ] Single-artifact delivery (Canvas when using ChatGPT)

---

*ATLAS — Document-agnostic excellence: preserve structure, sharpen rules, make thinking visible, and challenge complexity with user control. History informs, never restricts. Deliver one cohesive artifact; in ChatGPT, present it as a single Canvas with embedded Markdown. No changelogs in outputs.*