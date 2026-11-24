"""Provide the web layer. It may import the domain layer."""

from shop.domain import Order


def render(order: Order) -> str:
    """Return the order as text."""
    return f"Order {order.number}"
