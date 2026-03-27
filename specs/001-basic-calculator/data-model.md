# Data Model: Basic CLI Calculator

**Feature**: Basic CLI Calculator
**Date**: 2026-03-27
**Phase**: 1 - Design & Contracts

## Overview

The basic CLI calculator is a stateless, single-operation system. There is no persistent data model. This document describes the transient data structures used during calculation.

## Core Entities

### Operand

**Type**: `float`

**Description**: A numeric value (integer or decimal, positive or negative) provided by the user as input.

**Constraints**:
- Must be parseable as a valid floating-point number
- Can be positive, negative, or zero
- Precision limited to standard IEEE 754 float representation
- Range: Typical float range (-1.8e308 to 1.8e308)

**Validation Rules**:
- Non-empty string
- Contains only digits, optional decimal point, optional leading minus sign
- Examples: `5`, `-3.14`, `0`, `100.5`
- Invalid: `abc`, `1.2.3`, `--5`, `1e10` (scientific notation not supported)

---

### Operator

**Type**: `str` (single character)

**Description**: An arithmetic symbol that specifies the operation to perform on two operands.

**Valid Values**:
- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)

**Constraints**:
- Must be exactly one of the four valid operators
- Case-sensitive
- No whitespace allowed

**Validation Rules**:
- Must be in {`+`, `-`, `*`, `/`}
- Invalid: `x`, `add`, `**`, `//`, ` + ` (with spaces)

---

### Result

**Type**: `float`

**Description**: The numeric output of the calculation.

**Constraints**:
- Computed from two operands and one operator
- Precision limited to standard IEEE 754 float representation
- For division: undefined if divisor is zero (error condition)

**Formatting Rules**:
- Display as integer if result is whole number (e.g., `5` not `5.0`)
- Display with decimal places if fractional (e.g., `5.6`)
- No trailing zeros (e.g., `5.5` not `5.50`)

**Examples**:
- `2 + 3` → `5`
- `3.5 + 2.1` → `5.6`
- `10 / 4` → `2.5`
- `-5 * 2` → `-10`

---

## State Transitions

The calculator follows a simple linear flow with no state persistence:

```
Input (CLI args)
    ↓
Parse & Validate
    ↓
Perform Operation
    ↓
Format & Output
    ↓
Exit
```

**No state is retained between invocations.**

---

## Error States

### Invalid Operand

**Trigger**: User provides non-numeric input for operand

**Example**: `calculator abc + 5`

**Error Message**: `Error: Invalid operand '<value>' - must be a number`

**Exit Code**: 1

---

### Invalid Operator

**Trigger**: User provides operator not in {+, -, *, /}

**Example**: `calculator 5 ^ 3`

**Error Message**: `Error: Invalid operator '<value>' - must be one of: +, -, *, /`

**Exit Code**: 1

---

### Division by Zero

**Trigger**: User attempts to divide by zero

**Example**: `calculator 10 / 0`

**Error Message**: `Error: Division by zero`

**Exit Code**: 1

---

### Missing or Extra Arguments

**Trigger**: User provides fewer than 3 or more than 3 arguments

**Example**: `calculator 5 +` or `calculator 5 + 3 + 2`

**Error Message**: `Error: Invalid number of arguments - expected 3, got <N>`

**Exit Code**: 1

---

## Type Definitions (Python)

```python
# Core types
Operand = float
Operator = str  # One of: '+', '-', '*', '/'
Result = float

# Function signatures
def add(a: float, b: float) -> float: ...
def subtract(a: float, b: float) -> float: ...
def multiply(a: float, b: float) -> float: ...
def divide(a: float, b: float) -> float: ...  # Raises ValueError if b == 0

def parse_operand(s: str) -> float: ...  # Raises ValueError if not numeric
def parse_operator(s: str) -> str: ...   # Raises ValueError if not valid
def format_result(r: float) -> str: ...  # Returns human-readable string
```

---

## Validation Summary

| Entity | Validation | Error Handling |
|--------|-----------|-----------------|
| Operand | Numeric, parseable as float | Raise `ValueError` with message |
| Operator | One of {+, -, *, /} | Raise `ValueError` with message |
| Division | Divisor ≠ 0 | Raise `ValueError` with message |
| Arguments | Exactly 3 provided | Check `len(sys.argv)`, raise `ValueError` |

---

## No Persistence

- No database
- No file storage
- No session state
- No configuration files
- Each invocation is independent and stateless
