"""Test one branch of discount, so the report shows the missing lines."""

from discount import discount


def test_member_discount() -> None:
    """Give members 10 percent."""
    assert discount(100, member=True) == 10
