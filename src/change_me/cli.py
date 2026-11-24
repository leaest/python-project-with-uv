"""Provide the command line entry point."""

import sys

from change_me.core import add


def main(argv: list[str] | None = None) -> int:
    """Print the sum of two integers from the command line.

    Args:
        argv: The arguments without the program name. Defaults to sys.argv.

    Returns:
        The exit code.

    """
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("usage: change-me A B", file=sys.stderr)
        return 2
    print(add(int(args[0]), int(args[1])))
    return 0
