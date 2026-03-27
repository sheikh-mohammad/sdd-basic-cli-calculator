# Quickstart: Basic CLI Calculator

**Feature**: Basic CLI Calculator
**Date**: 2026-03-27
**Phase**: 1 - Design & Contracts

## Overview

This quickstart guide explains how to use and develop the basic CLI calculator.

## Installation

### Prerequisites

- Python 3.8 or later
- `uv` package manager

### Setup

```bash
# Clone the repository
git clone <repo-url>
cd sdd-basic-cli-calculator

# Create virtual environment and install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## Usage

### Basic Operations

```bash
# Addition
python -m src.cli 2 + 3
# Output: 5

# Subtraction
python -m src.cli 10 - 4
# Output: 6

# Multiplication
python -m src.cli 6 * 7
# Output: 42

# Division
python -m src.cli 20 / 4
# Output: 5
```

### Decimal Numbers

```bash
python -m src.cli 3.5 + 2.1
# Output: 5.6

python -m src.cli 10.5 - 3.2
# Output: 7.3
```

### Negative Numbers

```bash
python -m src.cli -5 + 3
# Output: -2

python -m src.cli 10 \* -2
# Output: -20
```

### Error Handling

```bash
# Division by zero
python -m src.cli 10 / 0
# Output (stderr): Error: Division by zero
# Exit code: 1

# Invalid input
python -m src.cli abc + 5
# Output (stderr): Error: Invalid operand 'abc' - must be a number
# Exit code: 1

# Invalid operator
python -m src.cli 5 ^ 3
# Output (stderr): Error: Invalid operator '^' - must be one of: +, -, *, /
# Exit code: 1

# Missing arguments
python -m src.cli 5 +
# Output (stderr): Error: Invalid number of arguments - expected 3, got 2
# Exit code: 1
```

## Development

### Project Structure

```
src/
├── calculator.py       # Core calculator logic
└── cli.py             # CLI interface

tests/
├── unit/
│   └── test_calculator.py    # Unit tests
└── integration/
    └── test_cli.py           # Integration tests

pyproject.toml         # Project configuration
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/unit/test_calculator.py

# Run with verbose output
pytest -v
```

### Code Style

All code must include type hints:

```python
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b
```

### Development Workflow

1. Write test first (Red)
2. Run test, verify it fails
3. Implement code (Green)
4. Run test, verify it passes
5. Refactor if needed (Refactor)
6. Commit with clear message

### Example: Adding a New Operation

If we were to add a new operation (e.g., modulo), the workflow would be:

1. **Red**: Write test in `tests/unit/test_calculator.py`
   ```python
   def test_modulo():
       assert modulo(10, 3) == 1
   ```

2. **Green**: Implement in `src/calculator.py`
   ```python
   def modulo(a: float, b: float) -> float:
       """Return remainder of a divided by b."""
       if b == 0:
           raise ValueError("Division by zero")
       return a % b
   ```

3. **Refactor**: Review and optimize if needed

4. **Update CLI**: Add operator handling in `src/cli.py`

## Architecture

### Core Logic (`src/calculator.py`)

- Pure functions with no side effects
- All functions have type hints
- Each operation is independently testable
- Raises `ValueError` for invalid operations (e.g., division by zero)

### CLI Interface (`src/cli.py`)

- Parses command-line arguments
- Validates input
- Calls appropriate calculator function
- Formats and displays results
- Handles errors gracefully

### Testing

- **Unit tests**: Test calculator functions in isolation
- **Integration tests**: Test CLI with subprocess calls
- **Coverage goal**: >80% of code

## Troubleshooting

### "ModuleNotFoundError: No module named 'src'"

Ensure you're running from the repository root and have activated the virtual environment:

```bash
cd sdd-basic-cli-calculator
source .venv/bin/activate
python -m src.cli 2 + 3
```

### "Invalid operand" error with negative numbers

Negative numbers must come after the operator or be quoted:

```bash
# Correct
python -m src.cli -- -5 + 3
python -m src.cli "-5" + 3

# Incorrect (shell interprets -5 as flag)
python -m src.cli -5 + 3
```

### Precision issues with decimals

Python's `float` uses IEEE 754 standard precision. For most use cases, this is sufficient:

```bash
python -m src.cli 0.1 + 0.2
# Output: 0.30000000000000004 (expected floating-point behavior)
```

## Next Steps

- Run tests: `pytest`
- Review code: `src/calculator.py` and `src/cli.py`
- Extend functionality: Add new operations following TDD workflow
- Deploy: Package as executable or distribute via PyPI
