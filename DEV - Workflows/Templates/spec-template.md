# Feature Specification: [FEATURE NAME]

.

## 📋 Table of Contents
- [1. 🎯 Objective](#1--objective)
- [2. 🧩 Scope](#2--scope)
- [3. 👤 Users & Stories](#3--users--stories)
- [4. ✅ Functional Requirements](#4--functional-requirements)
- [5. 🧪 Non-Functional Requirements](#5--non-functional-requirements)
- [6. 🧷 Edge Cases](#6--edge-cases)
- [7. 📏 Success Criteria](#7--success-criteria)
- [8. 🔗 Dependencies & Risks](#8--dependencies--risks)
- [9. 🚫 Out of Scope](#9--out-of-scope)
- [10. ❓ Open Questions](#10--open-questions)
- [11. 📎 Appendix](#11--appendix)

.

## 1. 🎯 Objective

Metadata
- Category: Spec
- Tags: [FEATURE], [AREA]
- Priority: [PRIORITY]

**Feature Branch**: `[###-feature-name]`  
**Created**: [DATE]  
**Status**: Draft  
**Input**: User description: "$ARGUMENTS"

Stakeholders
- [List key stakeholders/roles: Product, Engineering, Design, QA]

Purpose
- [One-sentence outcome; technology-agnostic]

### 1.1 Assumptions
- [NEEDS CLARIFICATION]: [Assumption about environment/platform]
- [NEEDS CLARIFICATION]: [Assumption about users/data]
- [NEEDS CLARIFICATION]: [Assumption about scope/constraints]

.

## 2. 🧩 Scope
- In-scope: [Items]
- Out-of-scope: [Items]

.

## 3. 👤 Users & Stories

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP that delivers value.
-->

### User Story 1 - [Brief Title] (Priority: P1)
[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently - e.g., "Can be fully tested by [specific action] and delivers [specific value]"]

**Acceptance Scenarios**:
1. **Given** [initial state], **When** [action], **Then** [expected outcome]
2. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 2 - [Brief Title] (Priority: P2)
[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**Acceptance Scenarios**:
1. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

### User Story 3 - [Brief Title] (Priority: P3)
[Describe this user journey in plain language]

**Why this priority**: [Explain the value and why it has this priority level]

**Independent Test**: [Describe how this can be tested independently]

**Acceptance Scenarios**:
1. **Given** [initial state], **When** [action], **Then** [expected outcome]

---

[Add more user stories as needed, each with an assigned priority]

.

## 4. ✅ Functional Requirements

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

- **FR-001**: System MUST [specific capability, e.g., "allow users to create accounts"]
- **FR-002**: System MUST [specific capability, e.g., "validate email addresses"]  
- **FR-003**: Users MUST be able to [key interaction, e.g., "reset their password"]
- **FR-004**: System MUST [data requirement, e.g., "persist user preferences"]
- **FR-005**: System MUST [behavior, e.g., "log all security events"]

*Unclear requirements examples:*
- **FR-006**: System MUST authenticate users via [NEEDS CLARIFICATION: auth method not specified - email/password, SSO, OAuth?]
- **FR-007**: System MUST retain user data for [NEEDS CLARIFICATION: retention period not specified]

Traceability
- Map User Stories → FRs (e.g., Story #1 → FR-001, FR-003)

.

## 5. 🧪 Non-Functional Requirements
- NFR-001: [Performance/Security/Operability + metric]
- NFR-002: [SLO/SLA/Compliance]

.

## 6. 🧷 Edge Cases

<!--
  ACTION REQUIRED: Fill this with the right edge cases.
-->
- What happens when [boundary condition]?
- How does system handle [error scenario]?

.

## 7. 📏 Success Criteria

### Measurable Outcomes
- **SC-001**: [Measurable metric, e.g., "Users can complete account creation in under 2 minutes"]
- **SC-002**: [Measurable metric, e.g., "System handles 1000 concurrent users without degradation"]
- **SC-003**: [User satisfaction metric, e.g., "90% of users successfully complete primary task on first attempt"]
- **SC-004**: [Business metric, e.g., "Reduce support tickets related to [X] by 50%"]

### 7.1 KPI Examples (pick relevant ones)
- Adoption: [% of target users using feature in N days]
- Quality: [Defect rate P0/P1 = 0 within N days]
- Performance: [p95 latency ≤ X ms]
- Reliability: [Error budget impact ≤ Y%]

.

## 8. 🔗 Dependencies & Risks
- Dependencies: [Systems/Teams]
- Risks: [Risk] → Mitigation: [Plan]

### 8.1 Risk Table (optional)
| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Example] | High | Medium | [Plan] |

.

## 9. 🚫 Out of Scope
- [Explicit exclusions to reduce ambiguity]

.

## 10. ❓ Open Questions
- [NEEDS CLARIFICATION]: [Question]
- [NEEDS CLARIFICATION]: [Question]

.

## 11. 📎 Appendix
- References, diagrams, notes
- Do not keep sample content in final output
