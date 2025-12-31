---

description: "Task list template for feature implementation"
---

# Tasks: Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
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

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Initialize Python project with Python 3.13+ support
- [x] T003 [P] Create src directory and all subdirectories (models, services, cli)
- [x] T004 [P] Create tests directory and all subdirectories
- [x] T005 Create __init__.py files in src/ and all subdirectories
- [x] T006 Create __init__.py files in tests/ and all subdirectories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T007 Create base Task model in src/models/task.py
- [x] T008 Create in-memory task storage implementation in src/services/task_service.py
- [x] T009 [P] Create base CLI interface structure in src/cli/cli_interface.py
- [x] T010 Create main application entry point in src/main.py
- [x] T011 Create basic configuration for UV environment

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks with a title and optional description, and the task should appear in the task list

**Independent Test**: The application should allow a user to add a new task with a title and optional description, and the task should appear in the task list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T012 [P] [US1] Unit test for Task model in tests/test_task.py
- [x] T013 [P] [US1] Unit test for adding task functionality in tests/test_task_service.py

### Implementation for User Story 1

- [x] T014 [P] [US1] Implement Task model with ID, title, description, completed status in src/models/task.py
- [x] T015 [US1] Implement add_task method in src/services/task_service.py
- [x] T016 [US1] Implement add task functionality in CLI interface in src/cli/cli_interface.py
- [x] T017 [US1] Integrate add task menu option in main application loop in src/main.py
- [x] T018 [US1] Add validation for non-empty title in src/services/task_service.py
- [x] T019 [US1] Add error handling for empty title in src/cli/cli_interface.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Tasks List (Priority: P1)

**Goal**: Allow users to view all tasks in a readable format with their status and ID

**Independent Test**: The application should display all tasks in a readable format with their status and ID.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T020 [P] [US2] Unit test for viewing tasks functionality in tests/test_task_service.py
- [x] T021 [P] [US2] Unit test for CLI view tasks functionality in tests/test_cli_interface.py

### Implementation for User Story 2

- [x] T022 [P] [US2] Implement get_all_tasks method in src/services/task_service.py
- [x] T023 [US2] Implement view tasks functionality in CLI interface in src/cli/cli_interface.py
- [x] T024 [US2] Integrate view tasks menu option in main application loop in src/main.py
- [x] T025 [US2] Format task display with ID, status indicator ([ ] or [x]), title, and truncated description
- [x] T026 [US2] Handle case when no tasks exist in src/cli/cli_interface.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete/Incomplete (Priority: P1)

**Goal**: Allow users to toggle the completion status of a task

**Independent Test**: The application should allow a user to toggle the completion status of a task.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T027 [P] [US3] Unit test for mark task complete functionality in tests/test_task_service.py
- [x] T028 [P] [US3] Unit test for mark task incomplete functionality in tests/test_task_service.py

### Implementation for User Story 3

- [x] T029 [P] [US3] Implement mark_task_complete method in src/services/task_service.py
- [x] T030 [P] [US3] Implement mark_task_incomplete method in src/services/task_service.py
- [x] T031 [US3] Implement mark complete/incomplete functionality in CLI interface in src/cli/cli_interface.py
- [x] T032 [US3] Integrate mark complete menu option in main application loop in src/main.py
- [x] T033 [US3] Integrate mark incomplete menu option in main application loop in src/main.py
- [x] T034 [US3] Add error handling for invalid task ID in src/services/task_service.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Allow users to update the title or description of an existing task

**Independent Test**: The application should allow a user to update the title or description of an existing task.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [x] T035 [P] [US4] Unit test for update task functionality in tests/test_task_service.py
- [x] T036 [P] [US4] Unit test for CLI update task functionality in tests/test_cli_interface.py

### Implementation for User Story 4

- [x] T037 [P] [US4] Implement update_task method in src/services/task_service.py
- [x] T038 [US4] Implement update task functionality in CLI interface in src/cli/cli_interface.py
- [x] T039 [US4] Integrate update task menu option in main application loop in src/main.py
- [x] T040 [US4] Add validation for task ID in src/services/task_service.py
- [x] T041 [US4] Add error handling for invalid task ID in src/cli/cli_interface.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P2)

**Goal**: Allow users to delete a specific task by its ID

**Independent Test**: The application should allow a user to delete a specific task by its ID.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [x] T042 [P] [US5] Unit test for delete task functionality in tests/test_task_service.py
- [x] T043 [P] [US5] Unit test for CLI delete task functionality in tests/test_cli_interface.py

### Implementation for User Story 5

- [x] T044 [P] [US5] Implement delete_task method in src/services/task_service.py
- [x] T045 [US5] Implement delete task functionality in CLI interface in src/cli/cli_interface.py
- [x] T046 [US5] Integrate delete task menu option in main application loop in src/main.py
- [x] T047 [US5] Add confirmation prompt for deletion in src/cli/cli_interface.py
- [x] T048 [US5] Add error handling for invalid task ID in src/cli/cli_interface.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T049 [P] Add type hints to all functions in all modules
- [x] T050 [P] Add docstrings to all functions/classes in Google or NumPy style
- [x] T051 Add comprehensive error handling throughout application
- [x] T052 [P] Create README.md with project overview, UV setup instructions, run command
- [x] T053 [P] Create feature demo in README.md with text examples
- [x] T054 Run quickstart.md validation to ensure instructions work correctly
- [x] T055 [P] Add input validation for all user inputs
- [x] T056 Add proper exit functionality to main application loop

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
T012 [P] [US1] Unit test for Task model in tests/test_task.py
T013 [P] [US1] Unit test for adding task functionality in tests/test_task_service.py

# Launch all implementation for User Story 1 together:
T014 [P] [US1] Implement Task model with ID, title, description, completed status in src/models/task.py
T015 [US1] Implement add_task method in src/services/task_service.py
T016 [US1] Implement add task functionality in CLI interface in src/cli/cli_interface.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Add User Story 1 → Test independently → Deploy/Demo (MVP!)
   - Add User Story 2 → Test independently → Deploy/Demo
   - Add User Story 3 → Test independently → Deploy/Demo
   - Add User Story 4 → Test independently → Deploy/Demo
   - Add User Story 5 → Test independently → Deploy/Demo
3. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
