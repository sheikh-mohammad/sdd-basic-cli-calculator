# CLI Interface Contract

**Module**: `src.cli`
**Type**: Command-line interface
**Language**: Python 3.8+
**Status**: Design specification

## Overview

The CLI module provides the command-line interface for the calculator. It handles argument parsing, input validation, error handling, and output formatting.

## Invocation

### Command Format

```bash
python -m src.cli <operand1> <operator> <operand2>
```

### Arguments

| Position | Name | Type | Description |
|----------|------|------|-------------|
| 1 | operand1 | string | First numeric operand (integer or decimal, can be negative) |
| 2 | operator | string | Arithmetic operator: `+`, `-`, `*`, or `/` |
| 3 | operand2 | string | Second numeric operand (integer or decimal, can be negative) |

### Examples

```bash
# Basic operations
python -m src.cli 2 + 3
python -m src.cli 10 - 4
python -m src.cli 6 \* 7
python -m src.cli 20 / 4

# Decimal numbers
python -m src.cli 3.5 + 2.1
python -m src.cli 10.5 - 3.2

# Negative numbers
python -m src.cli -5 + 3
python -m src.cli 10 \* -2
```

---

## Output

### Success Case

**Destination**: stdout

**Format**: Human-readable number (no trailing zeros)

**Examples**:
```
5
6
42
5.6
-2
```

**Exit Code**: 0

---

### Error Cases

**Destination**: stderr

**Format**: `Error: <message>`

**Exit Code**: 1

#### Invalid Operand

**Trigger**: Operand is not a valid number

**Message**: `Error: Invalid operand '<value>' - must be a number`

**Example**:
```bash
$ python -m src.cli abc + 5
Error: Invalid operand 'abc' - must be a number
```

---

#### Invalid Operator

**Trigger**: Operator is not one of {+, -, *, /}

**Message**: `Error: Invalid operator '<value>' - must be one of: +, -, *, /`

**Example**:
```bash
$ python -m src.cli 5 ^ 3
Error: Invalid operator '^' - must be one of: +, -, *, /
```

---

#### Division by Zero

**Trigger**: Attempting to divide by zero

**Message**: `Error: Division by zero`

**Example**:
```bash
$ python -m src.cli 10 / 0
Error: Division by zero
```

---

#### Invalid Number of Arguments

**Trigger**: Fewer than 3 or more than 3 arguments provided

**Message**: `Error: Invalid number of arguments - expected 3, got <N>`

**Example**:
```bash
$ python -m src.cli 5 +
Error: Invalid number of arguments - expected 3, got 2
```

---

## Implementation Requirements

### Argument Parsing

```python
def main(args: list[str]) -> int:
    """
    Main CLI entry point.

    Args:
        args: Command-line arguments (sys.argv[1:])

    Returns:
        Exit code (0 for success, 1 for error)
    """
```

**Steps**:
1. Check `len(args) == 3`
2. Parse `args[0]` as operand1 (float)
3. Validate `args[1]` is in {+, -, *, /}
4. Parse `args[2]` as operand2 (float)
5. Call appropriate calculator function
6. Format and print result to stdout
7. Return 0

**Error Handling**:
- Catch `ValueError` from float parsing → print error to stderr, return 1
- Catch `ValueError` from calculator (division by zero) → print error to stderr, return 1
- Catch invalid operator → print error to stderr, return 1

---

## Type Hints

```python
def main(args: list[str]) -> int: ...

def parse_operand(s: str) -> float: ...  # Raises ValueError

def parse_operator(s: str) -> str: ...   # Raises ValueError

def format_result(r: float) -> str: ...  # Returns string
```

---

## Guarantees

- ✅ Deterministic: Same arguments always produce same output
- ✅ Fail-fast: Validates all inputs before calling calculator
- ✅ Clear errors: All error messages are actionable
- ✅ Proper exit codes: 0 for success, 1 for error
- ✅ Correct I/O streams: Results to stdout, errors to stderr
- ✅ Type-safe: Full type hints on all functions
