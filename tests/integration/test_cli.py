"""Integration tests for CLI interface."""

import subprocess
import sys
from typing import Tuple


def run_calculator(args: list[str]) -> Tuple[str, str, int]:
    """Run calculator CLI and return stdout, stderr, and exit code.

    Args:
        args: Command-line arguments to pass to calculator

    Returns:
        Tuple of (stdout, stderr, exit_code)
    """
    result = subprocess.run(
        [sys.executable, "-m", "src.cli"] + args,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


class TestCLIBasicOperations:
    """Tests for CLI with basic operations."""

    def test_cli_addition(self) -> None:
        """Test CLI addition."""
        pass

    def test_cli_subtraction(self) -> None:
        """Test CLI subtraction."""
        pass

    def test_cli_multiplication(self) -> None:
        """Test CLI multiplication."""
        pass

    def test_cli_division(self) -> None:
        """Test CLI division."""
        pass


class TestCLIErrorHandling:
    """Tests for CLI error handling."""

    def test_cli_division_by_zero(self) -> None:
        """Test CLI division by zero error."""
        pass

    def test_cli_invalid_operand(self) -> None:
        """Test CLI with invalid operand."""
        pass

    def test_cli_invalid_operator(self) -> None:
        """Test CLI with invalid operator."""
        pass

    def test_cli_missing_arguments(self) -> None:
        """Test CLI with missing arguments."""
        pass
