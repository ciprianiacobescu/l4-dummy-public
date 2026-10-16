"""Order total helpers of the eval base project."""

from decimal import Decimal

from inventory.catalog import SkuCatalog
from pricing.rounding import round_cents


def order_total_cents(catalog: SkuCatalog, items: list[tuple[str, int]]) -> int:
    """The whole cents total of an order, rounding the exact sum once."""
    for sku, qty in items:
        if isinstance(qty, bool) or not isinstance(qty, int):
            raise TypeError(f"quantity of {sku} must be an int: {qty!r}")
        if qty < 1:
            raise ValueError(f"quantity of {sku} must be at least 1: {qty}")
    total = Decimal("0")
    for sku, qty in items:
        total += qty * catalog.unit_price(sku)
    return round_cents(total)
