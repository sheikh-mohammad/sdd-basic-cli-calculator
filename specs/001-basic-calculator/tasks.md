---
description: "Task list for Basic CLI Calculator implementation"
---

# Tasks: Basic CLI Calculator

**Input**: Design documents from `/specs/001-basic-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included following TDD approach (Red-Green-Refactor). Tests are written FIRST and must FAIL before implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths: `src/calculator.py`, `src/cli.py`, `tests/unit/`, `tests/integration/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure: `src/`, `tests/unit/`, `tests/integration/` directories
- [x] T002 Initialize pyproject.toml with pytest dependency and Python 3.8+ requirement
- [x] T003 [P] Create `__init__.py` files in src/ and tests/ directories
- [x] T004 Create README.md with project overview and usage instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Create `src/calculator.py` module skeleton with type hints
- [x] T006 Create `src/cli.py` module skeleton with main entry point
- [x] T007 Create `tests/unit/test_calculator.py` test file skeleton
- [x] T008 Create `tests/integration/test_cli.py` test file skeleton
- [x] T009 Configure pytest in pyproject.toml with test discovery paths

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic Operations (Priority: P1) 🎯 MVP

**Goal**: Implement core arithmetic operations (addition, subtraction, multiplication, division) with correct results for integer inputs

**Independent Test**: Can be fully tested by running the calculator with various numeric inputs and operations, verifying correct results are returned.

### Tests for User Story 1 (TDD - Write FIRST, ensure they FAIL)

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Write unit tests for add() function in tests/unit/test_calculator.py (test cases: 2+3=5, -5+3=-2, 0+0=0)
- [ ] T011 [P] [US1] Write unit tests for subtract() function in tests/unit/test_calculator.py (test cases: 10-4=6, 5-10=-5, 0-0=0)
- [ ] T012 [P] [US1] Write unit tests for multiply() function in tests/unit/test_calculator.py (test cases: 6*7=42, -5*2=-10, 0*5=0)
- [ ] T013 [P] [US1] Write unit tests for divide() function in tests/unit/test_calculator.py (test cases: 20/4=5, 10/2=5, -10/-2=5)
- [ ] T014 [P] [US1] Write integration tests for CLI with basic operations in tests/integration/test_cli.py (test: `python -m src.cli 2 + 3` outputs `5`)

### Implementation for User Story 1

- [ ] T015 [P] [US1] Implement add(a: float, b: float) -> float in src/calculator.py
- [ ] T016 [P] [US1] Implement subtract(a: float, b: float) -> float in src/calculator.py
- [ ] T017 [P] [US1] Implement multiply(a: float, b: float) -> float in src/calculator.py
- [ ] T018 [P] [US1] Implement divide(a: float, b: float) -> float in src/calculator.py (no error handling yet)
- [ ] T019 [US1] Implement main(args: list[str]) -> int in src/cli.py to parse arguments and call calculator functions
- [ ] T020 [US1] Implement result formatting in src/cli.py to display integers without decimal point
- [ ] T021 [US1] Add __main__ entry point in src/cli.py to enable `python -m src.cli` invocation
- [ ] T022 [US1] Run all User Story 1 tests and verify they PASS

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Decimal Numbers (Priority: P1)

**Goal**: Support decimal number inputs and outputs with appropriate precision

**Independent Test**: Can be fully tested by running calculations with decimal inputs and verifying decimal results are correctly computed and displayed.

### Tests for User Story 2 (TDD - Write FIRST, ensure they FAIL)

- [ ] T023 [P] [US2] Write unit tests for decimal addition in tests/unit/test_calculator.py (test cases: 3.5+2.1=5.6, 0.1+0.2≈0.3)
- [ ] T024 [P] [US2] Write unit tests for decimal subtraction in tests/unit/test_calculator.py (test cases: 10.5-3.2=7.3)
- [ ] T025 [P] [US2] Write unit tests for decimal multiplication in tests/unit/test_calculator.py (test cases: 2.5*4=10.0)
- [ ] T026 [P] [US2] Write unit tests for decimal division in tests/unit/test_calculator.py (test cases: 10/3≈3.333...)
- [ ] T027 [US2] Write integration tests for CLI with decimal operations in tests/integration/test_cli.py (test: `python -m src.cli 3.5 + 2.1` outputs `5.6`)

### Implementation for User Story 2

- [ ] T028 [US2] Update result formatting in src/cli.py to handle decimal display (remove trailing zeros, e.g., 10.0 → 10, 5.6 → 5.6)
- [ ] T029 [US2] Run all User Story 2 tests and verify they PASS

**Checkpoint**: User Stories 1 AND 2 should both work independently with decimal support

---

## Phase 5: User Story 3 - Handle Negative Numbers (Priority: P1)

**Goal**: Support negative number inputs in all operations

**Independent Test**: Can be fully tested by running calculations with negative operands and verifying correct results.

### Tests for User Story 3 (TDD - Write FIRST, ensure they FAIL)

- [ ] T030 [P] [US3] Write unit tests for negative operands in tests/unit/test_calculator.py (test cases: -5+3=-2, 10*-2=-20, -10/-2=5)
- [ ] T031 [US3] Write integration tests for CLI with negative numbers in tests/integration/test_cli.py (test: `python -m src.cli -5 + 3` outputs `-2`)

### Implementation for User Story 3

- [ ] T032 [US3] Update src/cli.py argument parsing to handle negative numbers (use -- separator or quoted args)
- [ ] T033 [US3] Run all User Story 3 tests and verify they PASS

**Checkpoint**: User Stories 1, 2, AND 3 should all work independently with negative number support

---

## Phase 6: User Story 4 - Reject Division by Zero (Priority: P1)

**Goal**: Detect and handle division by zero with clear error message

**Independent Test**: Can be fully tested by attempting division by zero and verifying an appropriate error message is displayed.

### Tests for User Story 4 (TDD - Write FIRST, ensure they FAIL)

- [ ] T034 [P] [US4] Write unit tests for division by zero in tests/unit/test_calculator.py (test: divide(10, 0) raises ValueError)
- [ ] T035 [US4] Write integration tests for CLI division by zero in tests/integration/test_cli.py (test: `python -m src.cli 10 / 0` outputs error to stderr, exit code 1)

### Implementation for User Story 4

- [ ] T036 [US4] Add division by zero check in divide() function in src/calculator.py (raise ValueError("Division by zero"))
- [ ] T037 [US4] Add error handling in main() in src/cli.py to catch ValueError and print to stderr
- [ ] T038 [US4] Ensure main() returns exit code 1 on error in src/cli.py
- [ ] T039 [US4] Run all User Story 4 tests and verify they PASS

**Checkpoint**: User Stories 1-4 should all work independently with error handling for division by zero

---

## Phase 7: User Story 5 - Reject Invalid Input (Priority: P1)

**Goal**: Validate input and reject non-numeric operands and invalid operators with clear error messages

**Independent Test**: Can be fully tested by providing various invalid inputs and verifying appropriate error messages are displayed.

### Tests for User Story 5 (TDD - Write FIRST, ensure they FAIL)

- [ ] T040 [P] [US5] Write unit tests for invalid operand parsing in tests/unit/test_calculator.py (test: parse_operand("abc") raises ValueError)
- [ ] T041 [P] [US5] Write unit tests for invalid operator validation in tests/unit/test_calculator.py (test: validate_operator("^") raises ValueError)
- [ ] T042 [P] [US5] Write integration tests for CLI invalid input in tests/integration/test_cli.py (test: `python -m src.cli abc + 5` outputs error to stderr)
- [ ] T043 [P] [US5] Write integration tests for CLI invalid operator in tests/integration/test_cli.py (test: `python -m src.cli 5 ^ 3` outputs error to stderr)
- [ ] T044 [US5] Write integration tests for CLI missing arguments in tests/integration/test_cli.py (test: `python -m src.cli 5 +` outputs error to stderr)

### Implementation for User Story 5

- [ ] T045 [US5] Add input validation in main() in src/cli.py to check argument count (raise ValueError if not 3 args)
- [ ] T046 [US5] Add operand parsing with error handling in src/cli.py (catch ValueError from float() parsing)
- [ ] T047 [US5] Add operator validation in src/cli.py (check operator is in {+, -, *, /})
- [ ] T048 [US5] Update error messages in src/cli.py to be clear and actionable (e.g., "Error: Invalid operand 'abc' - must be a number")
- [ ] T049 [US5] Run all User Story 5 tests and verify they PASS

**Checkpoint**: All user stories (1-5) should now be independently functional with complete error handling

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T050 [P] Run full test suite with pytest and verify all tests PASS
- [ ] T051 [P] Check code coverage with pytest --cov=src (aim for >80%)
- [ ] T052 [P] Add type checking with mypy on src/ directory
- [ ] T053 Run quickstart.md validation (follow all examples and verify they work)
- [ ] T054 Update README.md with complete usage examples and error cases
- [ ] T055 Add docstrings to all functions in src/calculator.py and src/cli.py
- [ ] T056 Verify all code follows PEP 8 style guidelines
- [ ] T057 Create .gitignore for Python project (venv, __pycache__, .pytest_cache, etc.)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (US1 → US2 → US3 → US4 → US5)
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (TDD) MUST be written and FAIL before implementation
- Implementation tasks can run in parallel (different functions)
- All tests for a story must PASS before moving to next story
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- All implementation tasks marked [P] within a story can run in parallel (different functions)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (TDD - write first):
Task T010: Write unit tests for add()
Task T011: Write unit tests for subtract()
Task T012: Write unit tests for multiply()
Task T013: Write unit tests for divide()
Task T014: Write integration tests for CLI

# Verify all tests FAIL before implementation

# Launch all implementation tasks for User Story 1 together:
Task T015: Implement add()
Task T016: Implement subtract()
Task T017: Implement multiply()
Task T018: Implement divide()

# Then sequential tasks:
Task T019: Implement main() in CLI
Task T020: Implement result formatting
Task T021: Add __main__ entry point
Task T022: Run tests and verify PASS
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (basic arithmetic with integers)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (decimal support)
4. Add User Story 3 → Test independently → Deploy/Demo (negative numbers)
5. Add User Story 4 → Test independently → Deploy/Demo (division by zero handling)
6. Add User Story 5 → Test independently → Deploy/Demo (input validation)
7. Each story adds value without breaking previous stories

### TDD Workflow for Each Story

For each user story:

1. **RED**: Write all tests for the story (T0XX tasks)
2. Run tests → Verify they all FAIL
3. **GREEN**: Implement code to make tests pass (T0XX tasks)
4. Run tests → Verify they all PASS
5. **REFACTOR**: Clean up code if needed
6. Commit with clear message

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- **CRITICAL**: Verify tests FAIL before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- All functions must have type hints (constitution requirement)
- All errors must go to stderr; results to stdout
- Exit code 0 for success, 1 for error
