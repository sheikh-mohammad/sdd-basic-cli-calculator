# Calculator Module Contract

**Module**: `src.calculator`
**Type**: Pure function library
**Language**: Python 3.8+
**Status**: Design specification

## Overview

The calculator module provides pure functions for basic arithmetic operations. All functions are stateless, have no side effects, and include full type hints.

## Function Signatures

### add

```python
def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a: First operand
        b: Second operand

    Returns:
        Sum of a and b

    Raises:
        TypeError: If operands are not numeric
    """
```

**Examples**:
- `add(2, 3)` → `5`
- `add(3.5, 2.1)` → `5.6`
- `add(-5, 3)` → `-2`

---

### subtract

```python
def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.

    Args:
        a: Minuend
        b: Subtrahend

    Returns:
        Difference (a - b)

    Raises:
        TypeError: If operands are not numeric
    """
```

**Examples**:
- `subtract(10, 4)` → `6`
- `subtract(10.5, 3.2)` → `7.3`
- `subtract(-10, -2)` → `-8`

---

### multiply

```python
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    Args:
        a: First operand
        b: Second operand

    Returns:
        Product of a and b

    Raises:
        TypeError: If operands are not numeric
    """
```

**Examples**:
- `multiply(6, 7)` → `42`
- `multiply(2.5, 4)` → `10.0`
- `multiply(10, -2)` → `-20`

---

### divide

```python
def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Quotient (a / b)

    Raises:
        ValueError: If b is zero (division by zero)
        TypeError: If operands are not numeric
    """
```

**Examples**:
- `divide(20, 4)` → `5.0`
- `divide(10, 3)` → `3.3333...`
- `divide(10, 0)` → raises `ValueError("Division by zero")`

---

## Error Handling

All functions raise exceptions for invalid inputs:

| Error | Condition | Message |
|-------|-----------|---------|
| `ValueError` | Division by zero | `"Division by zero"` |
| `TypeError` | Non-numeric operand | `"unsupported operand type(s)"` |

---

## Type Hints

All functions use complete type hints:

```python
from typing import Union

# All operands are float (Python's numeric type)
# Return type is always float
# No optional parameters
```

---

## Guarantees

- ✅ Pure functions: No side effects, no state mutation
- ✅ Deterministic: Same inputs always produce same outputs
- ✅ Type-safe: Full type hints on all parameters and returns
- ✅ Testable: Each function independently testable
- ✅ No I/O: No file, network, or console operations
