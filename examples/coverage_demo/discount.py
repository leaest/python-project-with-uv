"""Hold code that the demo tests cover only in part."""


def discount(total: float, member: bool) -> float:
    """Return the discount for a total."""
    if total <= 0:
        raise ValueError("total must be positive")  # not covered
    if member:
        return total * 0.1
    return 0.0  # not covered
