# Implementation Plan: [FEATURE]

.

## 📋 Table of Contents
- [1. 🎯 Objective](#1--objective)
- [2. 🔒 Quality Gates (Constitution Check)](#2--quality-gates-constitution-check)
- [3. 🗂 Project Structure](#3--project-structure)
- [4. 🚧 Implementation Phases](#4--implementation-phases)
- [5. 🧪 Testing Strategy](#5--testing-strategy)
- [6. 📏 Success Metrics](#6--success-metrics)
- [7. ⚠️ Risks & Mitigations](#7--risks--mitigations)
- [8. 🔗 Dependencies](#8--dependencies)
- [9. 📣 Communication & Review](#9--communication--review)
- [10. 📎 References](#10--references)

.

## 1. 🎯 Objective

Metadata
- Category: Plan
- Tags: [FEATURE], [AREA]
- Priority: [PRIORITY]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

Summary
- [Extract from feature spec: primary requirement + technical approach from research]

Technical Context
<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->
**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]  
**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]  
**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]  
**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]  
**Project Type**: [single/web/mobile - determines source structure]  
**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]  
**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]  
**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

.

## 2. 🔒 Quality Gates (Constitution Check)
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Definition of Ready (DoR)
- Problem statement clear; scope documented
- Stakeholders identified; decisions path agreed
- Constraints known; risks captured
- Success criteria measurable

Definition of Done (DoD)
- All acceptance criteria met; tests passing
- Docs updated (spec/plan/tasks/README)
- Performance/error budgets respected
- Rollback verified or not needed

Rollback guardrails
- [Signals to stop/rollback]
- [Recovery procedure reference]

.

## 3. 🗂 Project Structure

### Documentation (this feature)
```
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->
```
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
```

**Structure Decision**: [Document the selected structure and reference the real directories captured above]

Complexity Tracking (optional)
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

.

## 4. 🚧 Implementation Phases
- Phase 1: [Goal], Deliverables, Owners, Duration
- Phase 2: [Goal], …
- Parallelization: use [P] tag to denote tasks that can run in parallel

.

## 5. 🧪 Testing Strategy
- Unit/Integration/E2E scope and tools
- Test Data & Environments
- CI quality gates

.

## 6. 📏 Success Metrics
- [Metric] → Target
- [Metric] → Target

.

## 7. ⚠️ Risks & Mitigations
- [Risk] → [Mitigation]

.

## 8. 🔗 Dependencies
- [Internal/External, timelines, owners]

.

## 9. 📣 Communication & Review
- Stakeholders: [List]
- Checkpoints: [Standups cadence], [Demo date], [Review gates]
- Approvals: [Who signs off]

.

## 10. 📎 References
- This template is filled by the `/speckit.plan` command
- [Link additional docs]
