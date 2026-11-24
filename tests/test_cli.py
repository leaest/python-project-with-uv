"""Verify the command line entry point."""

from typing import TYPE_CHECKING

from change_me.cli import main

if TYPE_CHECKING:
    import pytest


def test_main_prints_sum(capsys: pytest.CaptureFixture[str]) -> None:
    """Print the sum of the two arguments."""
    assert main(["2", "3"]) == 0
    assert capsys.readouterr().out == "5\n"


def test_main_rejects_wrong_argument_count(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Return exit code 2 and print the usage."""
    assert main(["2"]) == 2
    assert "usage" in capsys.readouterr().err
