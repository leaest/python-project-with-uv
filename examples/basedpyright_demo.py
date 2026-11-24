"""Show type errors that basedpyright reports.

Run: uv run basedpyright examples/basedpyright_demo.py
"""


def greet(name: str) -> str:
    """Return a greeting for name."""
    return "Hello, " + name


def demo() -> None:
    """Call greet with the wrong types."""
    greet(42)  # error: int is not assignable to str
    count: int = greet("Ada")  # error: str is not assignable to int
    print(count.upper())  # error: int has no attribute "upper"
