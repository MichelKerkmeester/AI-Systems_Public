---
description: "Task list template for feature implementation"
---

# Tasks: [FEATURE NAME]

.

## 📋 Table of Contents
- [1. 🎯 Objective](#1--objective)
- [2. 🧭 Conventions](#2--conventions)
- [3. 🧱 Task Groups by Phase/Story](#3--task-groups-by-phasestory)
- [4. ✅ Validation Checklist](#4--validation-checklist)
- [5. 🧪 Optional Tests Guidance](#5--optional-tests-guidance)

.

## 1. 🎯 Objective

Metadata
- Category: Tasks
- Tags: [FEATURE], [AREA]
- Priority: [PRIORITY]

**Input**: Design documents from `/specs/[###-feature-name]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

.

## 2. 🧭 Conventions
- Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions
- ID format: `T###` (e.g., T012)
- Commit message hint: `tasks([SPEC_ID]): short action` (optional)
- Avoid parallel edits to the same file in different tasks

Path Conventions
- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths below assume single project - adjust based on plan.md structure

Example task line
```text path=null start=null
T012 [P] [US1] Implement service in src/services/[service].py (depends on T010, T011)
```

<!-- 
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.
  
  The /speckit.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/
  
  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment
  
  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

.

## 3. 🧱 Task Groups by Phase/Story

### Phase 1: Setup (Shared Infrastructure)
**Purpose**: Project initialization and basic structure
- [ ] T001 Create project structure per implementation plan
- [ ] T002 Initialize [language] project with [framework] dependencies
- [ ] T003 [P] Configure linting and formatting tools

---

### Phase 2: Foundational (Blocking Prerequisites)
**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):
- [ ] T004 Setup database schema and migrations framework
- [ ] T005 [P] Implement authentication/authorization framework
- [ ] T006 [P] Setup API routing and middleware structure
- [ ] T007 Create base models/entities that all stories depend on
- [ ] T008 Configure error handling and logging infrastructure
- [ ] T009 Setup environment configuration management

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

### Phase 3: User Story 1 - [Title] (Priority: P1) 🎯 MVP
**Goal**: [Brief description of what this story delivers]
**Independent Test**: [How to verify this story works on its own]

Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️
- [ ] T010 [P] [US1] Contract test for [endpoint] in tests/contract/test_[name].py
- [ ] T011 [P] [US1] Integration test for [user journey] in tests/integration/test_[name].py

Implementation for User Story 1
- [ ] T012 [P] [US1] Create [Entity1] model in src/models/[entity1].py
- [ ] T013 [P] [US1] Create [Entity2] model in src/models/[entity2].py
- [ ] T014 [US1] Implement [Service] in src/services/[service].py (depends on T012, T013)
- [ ] T015 [US1] Implement [endpoint/feature] in src/[location]/[file].py
- [ ] T016 [US1] Add validation and error handling
- [ ] T017 [US1] Add logging for user story 1 operations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

### Phase 4: User Story 2 - [Title] (Priority: P2)
**Goal**: [Brief description of what this story delivers]
**Independent Test**: [How to verify this story works on its own]

Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️
- [ ] T018 [P] [US2] Contract test for [endpoint] in tests/contract/test_[name].py
- [ ] T019 [P] [US2] Integration test for [user journey] in tests/integration/test_[name].py

Implementation for User Story 2
- [ ] T020 [P] [US2] Create [Entity] model in src/models/[entity].py
- [ ] T021 [US2] Implement [Service] in src/services/[service].py
- [ ] T022 [US2] Implement [endpoint/feature] in src/[location]/[file].py
- [ ] T023 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

### Phase 5: User Story 3 - [Title] (Priority: P3)
**Goal**: [Brief description of what this story delivers]
**Independent Test**: [How to verify this story works on its own]

Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️
- [ ] T024 [P] [US3] Contract test for [endpoint] in tests/contract/test_[name].py
- [ ] T025 [P] [US3] Integration test for [user journey] in tests/integration/test_[name].py

Implementation for User Story 3
- [ ] T026 [P] [US3] Create [Entity] model in src/models/[entity].py
- [ ] T027 [US3] Implement [Service] in src/services/[service].py
- [ ] T028 [US3] Implement [endpoint/feature] in src/[location]/[file].py

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

### Phase N: Polish & Cross-Cutting Concerns
**Purpose**: Improvements that affect multiple user stories
- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening
- [ ] TXXX Run quickstart.md validation

.

## 4. ✅ Validation Checklist
- Lint passes
- Tests pass (unit/integration as applicable)
- Docs updated (README/spec/plan/tasks)
- Owner review and sign-off
- Paths and naming follow conventions
- Commit messages clear and linked to spec where needed

.

## 5. 🧪 Optional Tests Guidance
- Unit: [What/where]
- Integration: [What/where]
- Data/Fixtures: [Notes]
- Coverage target (optional): [e.g., 70–80%]
