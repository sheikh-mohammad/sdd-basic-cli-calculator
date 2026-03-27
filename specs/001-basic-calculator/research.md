# Research & Design Decisions: Basic CLI Calculator

**Feature**: Basic CLI Calculator
**Date**: 2026-03-27
**Phase**: 0 - Research & Clarification

## Overview

This document consolidates research findings and design decisions for the basic CLI calculator. All technical context items from the plan are resolved with no NEEDS CLARIFICATION markers remaining.

## Design Decisions

### 1. CLI Argument Parsing Strategy

**Decision**: Use `sys.argv` with manual parsing (no external library)

**Rationale**:
- Specification requires simple format: `calculator <operand1> <operator> <operand2>`
- Manual parsing is straightforward for this fixed format
- Avoids external dependencies, aligns with YAGNI principle
- Easier to test and debug

**Alternatives Considered**:
- `argparse` library: Overkill for fixed 3-argument format; adds unnecessary complexity
- `click` library: External dependency not needed for simple CLI

**Implementation**: Parse `sys.argv[1:3]` directly in `cli.py`

---

### 2. Numeric Type Handling

**Decision**: Use Python's built-in `float` type for all numeric operations

**Rationale**:
- `float` handles both integers and decimals natively
- Specification requires decimal support with "at least 2 decimal places" precision
- Python's `float` provides standard IEEE 754 precision (sufficient for calculator use)
- Simplifies code: no need for separate int/float branches

**Alternatives Considered**:
- `Decimal` module: Overkill for basic calculator; adds complexity
- Separate int/float handling: Unnecessary branching

**Implementation**: Parse operands as `float(operand_str)`, perform operations, format output

---

### 3. Error Handling Strategy

**Decision**: Validate input early, raise exceptions, catch at CLI boundary

**Rationale**:
- Specification requires clear error messages to stderr
- Separates validation logic (core) from error presentation (CLI)
- Enables testable error cases
- Aligns with TDD principle: test error paths explicitly

**Error Categories**:
1. **Invalid operand** (non-numeric): Catch `ValueError` from `float()` parsing
2. **Invalid operator** (not in +, -, *, /): Explicit check before operation
3. **Missing/extra arguments**: Check `len(sys.argv)` at CLI entry
4. **Division by zero**: Explicit check before division operation

**Implementation**:
- Core logic raises `ValueError` with descriptive message
- CLI catches exceptions and prints to stderr with exit code 1

---

### 4. Output Formatting

**Decision**: Format decimal results to remove trailing zeros; display integers without decimal point

**Rationale**:
- User-friendly: `5` instead of `5.0`, `5.6` instead of `5.60000`
- Specification requires "human-readable format"
- Maintains precision while avoiding clutter

**Implementation**:
```python
result = operand1 op operand2
if result == int(result):
    print(int(result))
else:
    print(result)
```

---

### 5. Type Hints Strategy

**Decision**: Full type hints on all functions and parameters

**Rationale**:
- Constitution requires type hints on all functions and class attributes
- Enables static type checking (mypy)
- Improves code clarity and IDE support
- Catches type errors early

**Implementation**:
- Function signatures: `def add(a: float, b: float) -> float:`
- CLI functions: `def main(args: list[str]) -> int:`
- Return types always specified

---

### 6. Testing Strategy

**Decision**: TDD with pytest; separate unit and integration tests

**Rationale**:
- Constitution mandates TDD (Red-Green-Refactor)
- Unit tests: Pure calculator functions (no I/O)
- Integration tests: CLI argument parsing and output

**Test Structure**:
- `tests/unit/test_calculator.py`: Test each operation (+, -, *, /) with various inputs
- `tests/integration/test_cli.py`: Test CLI with subprocess calls

**Test Coverage**:
- Happy path: Valid operations with integers, decimals, negatives
- Error path: Division by zero, invalid input, missing arguments
- Edge cases: Very large numbers, precision limits

---

## Technology Stack Confirmation

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Language | Python 3.8+ | Specified in constitution; widely available |
| Testing | pytest | Standard Python testing framework; simple syntax |
| Dependency Manager | uv | Specified in constitution; fast, reliable |
| Type Checking | Built-in type hints | Constitution requirement; no external tool needed |
| External Dependencies | None (core) | YAGNI principle; standard library sufficient |

---

## Implementation Approach

### Phase 1: Core Logic (calculator.py)

1. Define pure functions for each operation: `add()`, `subtract()`, `multiply()`, `divide()`
2. All functions: `(float, float) -> float` with type hints
3. `divide()` raises `ValueError` if divisor is 0
4. No I/O; no side effects

### Phase 2: CLI Interface (cli.py)

1. Parse `sys.argv` into operands and operator
2. Validate operator is in {+, -, *, /}
3. Parse operands as floats (catches non-numeric input)
4. Call appropriate calculator function
5. Format and print result to stdout
6. Catch exceptions, print to stderr, exit with code 1

### Phase 3: Tests

1. Unit tests: Each operation with 5+ test cases (happy path + edge cases)
2. Integration tests: CLI with subprocess, verify stdout/stderr
3. Run with pytest; aim for >80% coverage

---

## Assumptions Validated

- ✅ Single-operation mode: Confirmed by spec (one calculation per invocation)
- ✅ CLI argument format: Confirmed by spec (`calculator <op1> <op> <op2>`)
- ✅ Decimal precision: Standard float precision acceptable per spec
- ✅ No complex expressions: Spec explicitly excludes operator precedence
- ✅ Python 3.8+: Widely available; type hints supported
- ✅ No persistence: Single-operation, no data storage needed

---

## Next Steps

1. Generate data-model.md (Phase 1)
2. Generate contracts/ (Phase 1)
3. Generate quickstart.md (Phase 1)
4. Proceed to /sp.tasks for task breakdown
