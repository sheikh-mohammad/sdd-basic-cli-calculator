"""CLI interface for the calculator."""

import sys
from typing import List


def main(args: List[str]) -> int:
    """Main CLI entry point.

    Args:
        args: Command-line arguments (sys.argv[1:])

    Returns:
        Exit code (0 for success, 1 for error)
    """
    pass


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
