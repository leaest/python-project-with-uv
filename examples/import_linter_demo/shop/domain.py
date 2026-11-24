"""Provide the domain layer. It must not import the web layer."""

from dataclasses import dataclass

from shop.web import render  # breaks the contract: domain -> web


@dataclass
class Order:
    """Hold an order."""

    number: int

    def describe(self) -> str:
        """Return the order as text."""
        return render(self)
