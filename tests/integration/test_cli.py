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
        stdout, stderr, code = run_calculator(["2", "+", "3"])
        assert code == 0
        assert stdout == "5"

    def test_cli_subtraction(self) -> None:
        """Test CLI subtraction."""
        stdout, stderr, code = run_calculator(["10", "-", "4"])
        assert code == 0
        assert stdout == "6"

    def test_cli_multiplication(self) -> None:
        """Test CLI multiplication."""
        stdout, stderr, code = run_calculator(["6", "*", "7"])
        assert code == 0
        assert stdout == "42"

    def test_cli_division(self) -> None:
        """Test CLI division."""
        stdout, stderr, code = run_calculator(["20", "/", "4"])
        assert code == 0
        assert stdout == "5"


class TestCLIDecimalOperations:
    """Tests for CLI with decimal operations."""

    def test_cli_decimal_addition(self) -> None:
        """Test CLI decimal addition."""
        stdout, stderr, code = run_calculator(["3.5", "+", "2.1"])
        assert code == 0
        assert float(stdout) == pytest.approx(5.6, abs=0.0001)

    def test_cli_decimal_subtraction(self) -> None:
        """Test CLI decimal subtraction."""
        stdout, stderr, code = run_calculator(["10.5", "-", "3.2"])
        assert code == 0
        assert float(stdout) == pytest.approx(7.3, abs=0.0001)

    def test_cli_decimal_multiplication(self) -> None:
        """Test CLI decimal multiplication."""
        stdout, stderr, code = run_calculator(["2.5", "*", "4"])
        assert code == 0
        assert float(stdout) == pytest.approx(10.0, abs=0.0001)

    def test_cli_decimal_division(self) -> None:
        """Test CLI decimal division."""
        stdout, stderr, code = run_calculator(["10", "/", "3"])
        assert code == 0
        assert float(stdout) == pytest.approx(3.333333, abs=0.001)


class TestCLIErrorHandling:
    """Tests for CLI error handling."""

    def test_cli_division_by_zero(self) -> None:
        """Test CLI division by zero error."""
        stdout, stderr, code = run_calculator(["10", "/", "0"])
        assert code == 1
        assert "Division by zero" in stderr

    def test_cli_invalid_operand(self) -> None:
        """Test CLI with invalid operand."""
        stdout, stderr, code = run_calculator(["abc", "+", "5"])
        assert code == 1
        assert "Invalid operand" in stderr or "must be a number" in stderr

    def test_cli_invalid_operator(self) -> None:
        """Test CLI with invalid operator."""
        stdout, stderr, code = run_calculator(["5", "^", "3"])
        assert code == 1
        assert "Invalid operator" in stderr or "must be one of" in stderr

    def test_cli_missing_arguments(self) -> None:
        """Test CLI with missing arguments."""
        stdout, stderr, code = run_calculator(["5", "+"])
        assert code == 1
        assert "Invalid number of arguments" in stderr or "expected 3" in stderr


# Import pytest for approx
import pytest

