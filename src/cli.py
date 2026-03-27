"""CLI interface for the calculator."""

import sys
from typing import List

from src.calculator import add, subtract, multiply, divide


def format_result(result: float) -> str:
    """Format result for display, removing trailing zeros.

    Args:
        result: The numeric result to format

    Returns:
        Formatted result string
    """
    if result == int(result):
        return str(int(result))
    return str(result)


def main(args: List[str]) -> int:
    """Main CLI entry point.

    Args:
        args: Command-line arguments (sys.argv[1:])

    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Validate argument count
        if len(args) != 3:
            raise ValueError(f"Invalid number of arguments - expected 3, got {len(args)}")

        # Parse operands
        try:
            operand1 = float(args[0])
        except ValueError:
            raise ValueError(f"Invalid operand '{args[0]}' - must be a number")

        operator = args[1]

        try:
            operand2 = float(args[2])
        except ValueError:
            raise ValueError(f"Invalid operand '{args[2]}' - must be a number")

        # Validate operator
        if operator not in {"+", "-", "*", "/"}:
            raise ValueError(f"Invalid operator '{operator}' - must be one of: +, -, *, /")

        # Perform calculation
        if operator == "+":
            result = add(operand1, operand2)
        elif operator == "-":
            result = subtract(operand1, operand2)
        elif operator == "*":
            result = multiply(operand1, operand2)
        elif operator == "/":
            result = divide(operand1, operand2)

        # Format and print result
        print(format_result(result))
        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

