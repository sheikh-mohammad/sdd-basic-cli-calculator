"""Unit tests for calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for add function."""

    def test_add_basic(self) -> None:
        """Test basic addition."""
        assert add(2, 3) == 5

    def test_add_negative(self) -> None:
        """Test addition with negative numbers."""
        assert add(-5, 3) == -2

    def test_add_zero(self) -> None:
        """Test addition with zero."""
        assert add(0, 0) == 0


class TestSubtract:
    """Tests for subtract function."""

    def test_subtract_basic(self) -> None:
        """Test basic subtraction."""
        assert subtract(10, 4) == 6

    def test_subtract_negative(self) -> None:
        """Test subtraction with negative numbers."""
        assert subtract(5, 10) == -5

    def test_subtract_zero(self) -> None:
        """Test subtraction with zero."""
        assert subtract(0, 0) == 0


class TestMultiply:
    """Tests for multiply function."""

    def test_multiply_basic(self) -> None:
        """Test basic multiplication."""
        assert multiply(6, 7) == 42

    def test_multiply_negative(self) -> None:
        """Test multiplication with negative numbers."""
        assert multiply(-5, 2) == -10

    def test_multiply_zero(self) -> None:
        """Test multiplication with zero."""
        assert multiply(0, 5) == 0


class TestDivide:
    """Tests for divide function."""

    def test_divide_basic(self) -> None:
        """Test basic division."""
        assert divide(20, 4) == 5.0

    def test_divide_negative(self) -> None:
        """Test division with negative numbers."""
        assert divide(-10, -2) == 5.0

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError):
            divide(10, 0)


# Phase 4: Decimal tests
class TestAddDecimal:
    """Tests for add function with decimals."""

    def test_add_decimal(self) -> None:
        """Test decimal addition."""
        assert abs(add(3.5, 2.1) - 5.6) < 0.0001

    def test_add_decimal_small(self) -> None:
        """Test addition with small decimals."""
        assert abs(add(0.1, 0.2) - 0.3) < 0.0001


class TestSubtractDecimal:
    """Tests for subtract function with decimals."""

    def test_subtract_decimal(self) -> None:
        """Test decimal subtraction."""
        assert abs(subtract(10.5, 3.2) - 7.3) < 0.0001


class TestMultiplyDecimal:
    """Tests for multiply function with decimals."""

    def test_multiply_decimal(self) -> None:
        """Test decimal multiplication."""
        assert abs(multiply(2.5, 4) - 10.0) < 0.0001


class TestDivideDecimal:
    """Tests for divide function with decimals."""

    def test_divide_decimal(self) -> None:
        """Test decimal division."""
        result = divide(10, 3)
        assert abs(result - 3.333333) < 0.001

