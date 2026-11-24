"""Verify the core arithmetic helpers."""

from change_me.core import add


def test_add() -> None:
    """Sum two integers."""
    assert add(2, 3) == 5
